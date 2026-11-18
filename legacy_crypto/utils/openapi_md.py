#!/usr/bin/env python3
"""
把 OpenAPI 文档（dict）转成一篇 Markdown。

用于币安新文档站的 API 参考：每个 API（例如现货 WebSocket 行情推送）一份 schema.yaml，
里面英文写在 description / summary，中文写在 x-description-cn / x-summary-cn。
输出一篇双语 Markdown：每个接口一节，含地址、说明、参数表、请求体字段表、
响应字段表和响应示例。
"""
import json
from typing import Any, Dict, List, Optional, Tuple

_METHODS = ('get', 'post', 'put', 'delete', 'patch', 'head', 'options')
_MAX_DEPTH = 6


def _cn(obj: Dict[str, Any], key: str) -> str:
    return str(obj.get(f'x-{key}-cn') or '').strip()


def _cell(text: Any) -> str:
    text = '' if text is None else str(text)
    return text.replace('|', '\\|').replace('\r', '').replace('\n', '<br>').strip()


def _bilingual(en: str, cn: str) -> str:
    en, cn = (en or '').strip(), (cn or '').strip()
    if en and cn and cn != en:
        return f'{en}<br>{cn}'
    return en or cn


class OpenApiRenderer:
    def __init__(self, spec: Dict[str, Any]):
        self.spec = spec

    # ---------------------------------------------------------------- 引用
    def resolve(self, node: Any, seen: Tuple[str, ...] = ()) -> Tuple[Any, Tuple[str, ...]]:
        """解开 $ref；循环引用时返回 None。"""
        while isinstance(node, dict) and '$ref' in node:
            ref = node['$ref']
            if ref in seen or not ref.startswith('#/'):
                return None, seen
            seen = seen + (ref,)
            target: Any = self.spec
            for part in ref[2:].split('/'):
                target = target.get(part, {}) if isinstance(target, dict) else {}
            extra = {k: v for k, v in node.items() if k != '$ref'}
            node = {**target, **extra} if isinstance(target, dict) else target
        return node, seen

    # ---------------------------------------------------------------- 字段
    def _type_of(self, schema: Dict[str, Any]) -> str:
        t = schema.get('type')
        if not t:
            for key in ('oneOf', 'anyOf', 'allOf'):
                if key in schema:
                    return key
            return 'object' if 'properties' in schema else ''
        if t == 'array':
            items, _ = self.resolve(schema.get('items') or {})
            inner = self._type_of(items) if isinstance(items, dict) else ''
            return f'{inner}[]' if inner else 'array'
        if schema.get('format'):
            return f"{t} ({schema['format']})"
        return str(t)

    def _describe(self, schema: Dict[str, Any]) -> str:
        text = _bilingual(str(schema.get('description') or ''), _cn(schema, 'description'))
        extras = []
        if schema.get('enum'):
            extras.append('枚举: ' + ', '.join(f'`{v}`' for v in schema['enum']))
        if 'default' in schema:
            extras.append(f"默认: `{schema['default']}`")
        if 'example' in schema and not isinstance(schema['example'], (dict, list)):
            extras.append(f"例: `{schema['example']}`")
        return '<br>'.join(x for x in [text] + extras if x)

    def field_rows(self, schema: Any, prefix: str = '', depth: int = 0,
                   seen: Tuple[str, ...] = ()) -> List[Tuple[str, str, str, str]]:
        """展开对象字段，返回 (字段路径, 类型, 是否必填, 说明)。"""
        schema, seen = self.resolve(schema, seen)
        if not isinstance(schema, dict) or depth > _MAX_DEPTH:
            return []
        rows: List[Tuple[str, str, str, str]] = []
        if 'allOf' in schema:
            for part in schema['allOf']:
                rows += self.field_rows(part, prefix, depth, seen)
        for key in ('oneOf', 'anyOf'):
            if key in schema and not schema.get('properties'):
                for i, part in enumerate(schema[key], 1):
                    part_r, _ = self.resolve(part, seen)
                    if isinstance(part_r, dict) and (part_r.get('properties') or part_r.get('allOf')):
                        rows += self.field_rows(part, f'{prefix}({key} {i})', depth + 1, seen)
        if schema.get('type') == 'array' or ('items' in schema and 'properties' not in schema):
            items, items_seen = self.resolve(schema.get('items') or {}, seen)
            if isinstance(items, dict):
                rows += self.field_rows(items, f'{prefix}[]', depth + 1, items_seen)
            return rows
        required = set(schema.get('required') or [])
        for name, prop in (schema.get('properties') or {}).items():
            prop_r, prop_seen = self.resolve(prop, seen)
            if not isinstance(prop_r, dict):
                continue
            path = f'{prefix}.{name}' if prefix else str(name)
            rows.append((path, self._type_of(prop_r), '是' if name in required else '',
                         self._describe(prop_r)))
            rows += self.field_rows(prop_r, path, depth + 1, prop_seen)
        return rows

    @staticmethod
    def _table(rows: List[Tuple[str, ...]], header: Tuple[str, ...]) -> List[str]:
        if not rows:
            return []
        out = ['| ' + ' | '.join(header) + ' |', '|' + '---|' * len(header)]
        for row in rows:
            out.append('| ' + ' | '.join(_cell(c) for c in row) + ' |')
        return out + ['']

    def _example(self, media: Dict[str, Any]) -> Optional[Any]:
        if 'example' in media:
            return media['example']
        examples = media.get('examples') or {}
        for value in examples.values():
            value, _ = self.resolve(value)
            if isinstance(value, dict) and 'value' in value:
                return value['value']
        schema, _ = self.resolve(media.get('schema') or {})
        if isinstance(schema, dict) and 'example' in schema:
            return schema['example']
        return None

    @staticmethod
    def _code(value: Any) -> List[str]:
        text = value if isinstance(value, str) else json.dumps(value, ensure_ascii=False, indent=2)
        return ['```json', text.rstrip(), '```', '']

    # ---------------------------------------------------------------- 接口
    def operations(self) -> List[Tuple[str, str, Dict[str, Any], List[Any]]]:
        ops = []
        for path, item in (self.spec.get('paths') or {}).items():
            item, _ = self.resolve(item)
            if not isinstance(item, dict):
                continue
            shared = item.get('parameters') or []
            for method in _METHODS:
                if isinstance(item.get(method), dict):
                    ops.append((method.upper(), path, item[method], shared))
        return ops

    def render_operation(self, method: str, path: str, op: Dict[str, Any], shared: List[Any]) -> List[str]:
        product_type = self.spec.get('x-product-type', '')
        summary = op.get('summary') or op.get('operationId') or path
        summary_cn = _cn(op, 'summary')
        title = f'{summary}（{summary_cn}）' if summary_cn and summary_cn != summary else summary
        lines = [f'## {title}', '']
        if product_type == 'ws-streams':
            lines += [f'流名称: `{path.lstrip("/")}`', '']
        else:
            lines += [f'`{method} {path}`', '']
        for en, cn in ((op.get('description'), _cn(op, 'description')),):
            if en:
                lines += [str(en).strip(), '']
            if cn and cn != en:
                lines += [cn, '']
        if op.get('x-update-speed'):
            speed = _bilingual(str(op['x-update-speed']), _cn(op, 'update-speed')).replace('<br>', ' / ')
            lines += [f'更新速度: {speed}', '']
        if op.get('x-weight') is not None:
            lines += [f"权重: {op['x-weight']}", '']
        if op.get('operationId'):
            lines += [f"Operation ID: `{op['operationId']}`", '']

        params = []
        for p in list(shared) + list(op.get('parameters') or []):
            p, _ = self.resolve(p)
            if not isinstance(p, dict):
                continue
            schema, _ = self.resolve(p.get('schema') or {})
            schema = schema if isinstance(schema, dict) else {}
            desc = _bilingual(str(p.get('description') or ''), _cn(p, 'description'))
            extra = self._describe({k: v for k, v in schema.items() if k not in ('description',)})
            params.append((p.get('name', ''), p.get('in', ''), self._type_of(schema),
                           '是' if p.get('required') else '', '<br>'.join(x for x in (desc, extra) if x)))
        if params:
            lines += ['### 参数', ''] + self._table(params, ('名称', '位置', '类型', '必填', '说明'))

        body, _ = self.resolve(op.get('requestBody') or {})
        if isinstance(body, dict):
            for ctype, media in (body.get('content') or {}).items():
                rows = self.field_rows(media.get('schema') or {})
                example = self._example(media)
                if rows or example is not None:
                    lines += [f'### 请求体（{ctype}）', '']
                    lines += self._table(rows, ('字段', '类型', '必填', '说明'))
                    if example is not None:
                        lines += self._code(example)
                break

        for code, resp in (op.get('responses') or {}).items():
            resp, _ = self.resolve(resp)
            if not isinstance(resp, dict):
                continue
            desc = _bilingual(str(resp.get('description') or ''), _cn(resp, 'description')).replace('<br>', ' / ')
            lines += [f'### 响应 {code}' + (f'：{desc}' if desc else ''), '']
            for ctype, media in (resp.get('content') or {}).items():
                rows = self.field_rows(media.get('schema') or {})
                lines += self._table(rows, ('字段', '类型', '必填', '说明'))
                example = self._example(media)
                if example is not None:
                    lines += self._code(example)
                break
        return lines

    def render(self) -> Tuple[str, str]:
        """返回 (标题, 正文 Markdown，不含一级标题)。"""
        info = self.spec.get('info') or {}
        title = str(info.get('title') or 'API')
        lines: List[str] = []
        desc, desc_cn = str(info.get('description') or '').strip(), _cn(info, 'description')
        if desc:
            lines += [desc, '']
        if desc_cn and desc_cn != desc:
            lines += [desc_cn, '']
        if info.get('version'):
            lines += [f"版本: {info['version']}", '']
        servers = [s.get('url') for s in self.spec.get('servers') or [] if isinstance(s, dict) and s.get('url')]
        if servers:
            lines += ['## 服务地址', ''] + [f'- `{u}`' for u in servers] + ['']
        ops = self.operations()
        if ops:
            lines += ['## 接口列表', '']
            for method, path, op, _ in ops:
                name = op.get('summary') or op.get('operationId') or ''
                shown = path.lstrip('/') if self.spec.get('x-product-type') == 'ws-streams' else f'{method} {path}'
                lines.append(f'- `{shown}` — {name}')
            lines.append('')
        for method, path, op, shared in ops:
            lines += self.render_operation(method, path, op, shared)
        return title, '\n'.join(lines).strip() + '\n'
