#!/usr/bin/env python3
"""
把打包后的 JS 模块里的对象字面量读成 Python 数据，不执行任何 JS。

用于 Bitget 文档站（Zudoku）：每份 OpenAPI 规格编进一个 JS 模块，形如
    Array.from({length:0},()=>({}));var e={openapi:`3.1.1`,...};export{e as schema};
这里只认字面量：对象、数组、字符串（`...`、"..."、'...'）、数字、true/false/null、
压缩写法 !0 / !1 / void 0、十六进制整数，以及模块顶层 `var x=...` 定义过、再被引用的变量名。
遇到别的写法（函数调用、${} 插值等）就报错，不去猜。
"""
import re
from typing import Any, Dict, Tuple

_IDENT = re.compile(r'[A-Za-z_$][A-Za-z0-9_$]*')
_NUMBER = re.compile(r'-?(?:0[xX][0-9a-fA-F]+|\d+\.?\d*(?:[eE][+-]?\d+)?|\.\d+(?:[eE][+-]?\d+)?)')
_ESCAPES = {'n': '\n', 't': '\t', 'r': '\r', 'b': '\b', 'f': '\f', 'v': '\v', '0': '\0'}


class JsLiteralError(ValueError):
    pass


class _Parser:
    def __init__(self, text: str, variables: Dict[str, Any]):
        self.s = text
        self.i = 0
        self.vars = variables

    def error(self, msg: str) -> JsLiteralError:
        return JsLiteralError(f'{msg} at {self.i}: {self.s[self.i:self.i + 60]!r}')

    def ws(self) -> None:
        while self.i < len(self.s) and self.s[self.i] in ' \t\r\n':
            self.i += 1

    def value(self) -> Any:
        self.ws()
        c = self.s[self.i:self.i + 1]
        if c == '{':
            return self.obj()
        if c == '[':
            return self.arr()
        if c in '`"\'':
            return self.string()
        if self.s.startswith('!0', self.i):
            self.i += 2
            return True
        if self.s.startswith('!1', self.i):
            self.i += 2
            return False
        if self.s.startswith('void 0', self.i):
            self.i += 6
            return None
        m = _NUMBER.match(self.s, self.i)
        if m:
            self.i = m.end()
            text = m.group(0)
            if text.lstrip('-')[:2] in ('0x', '0X'):  # 压缩器把大整数写成十六进制
                return int(text, 16)
            return float(text) if any(ch in text for ch in '.eE') else int(text)
        m = _IDENT.match(self.s, self.i)
        if m:
            self.i = m.end()
            name = m.group(0)
            if name in ('true', 'false', 'null', 'undefined'):
                return {'true': True, 'false': False}.get(name)
            if name in self.vars:
                return self.vars[name]
            raise self.error(f'unknown name {name}')
        raise self.error('unexpected token')

    def string(self) -> str:
        quote = self.s[self.i]
        self.i += 1
        out = []
        while True:
            if self.i >= len(self.s):
                raise self.error('unterminated string')
            c = self.s[self.i]
            if c == quote:
                self.i += 1
                return ''.join(out)
            if quote == '`' and self.s.startswith('${', self.i):
                raise self.error('template interpolation')
            if c == '\\':
                n = self.s[self.i + 1]
                if n == 'u':
                    if self.s[self.i + 2] == '{':
                        end = self.s.index('}', self.i)
                        out.append(chr(int(self.s[self.i + 3:end], 16)))
                        self.i = end + 1
                    else:
                        out.append(chr(int(self.s[self.i + 2:self.i + 6], 16)))
                        self.i += 6
                    continue
                if n == 'x':
                    out.append(chr(int(self.s[self.i + 2:self.i + 4], 16)))
                    self.i += 4
                    continue
                if n == '\n':  # 续行
                    self.i += 2
                    continue
                out.append(_ESCAPES.get(n, n))
                self.i += 2
                continue
            out.append(c)
            self.i += 1

    def key(self) -> str:
        self.ws()
        c = self.s[self.i:self.i + 1]
        if c in '`"\'':
            return self.string()
        m = _IDENT.match(self.s, self.i) or _NUMBER.match(self.s, self.i)
        if not m:
            raise self.error('bad key')
        self.i = m.end()
        return m.group(0)

    def expect(self, ch: str) -> None:
        self.ws()
        if self.s[self.i:self.i + 1] != ch:
            raise self.error(f'expected {ch!r}')
        self.i += 1

    def obj(self) -> Dict[str, Any]:
        self.expect('{')
        out: Dict[str, Any] = {}
        while True:
            self.ws()
            if self.s[self.i] == '}':
                self.i += 1
                return out
            if self.s.startswith('...', self.i):  # 展开另一个变量
                self.i += 3
                spread = self.value()
                if not isinstance(spread, dict):
                    raise self.error('spread of non-object')
                out.update(spread)
            else:
                k = self.key()
                self.ws()
                if self.s[self.i] == ':':
                    self.i += 1
                    out[k] = self.value()
                elif k in self.vars:  # 简写 {x}
                    out[k] = self.vars[k]
                else:
                    raise self.error('expected ":"')
            self.ws()
            if self.s[self.i] == ',':
                self.i += 1

    def arr(self) -> list:
        self.expect('[')
        out = []
        while True:
            self.ws()
            if self.s[self.i] == ']':
                self.i += 1
                return out
            out.append(self.value())
            self.ws()
            if self.s[self.i] == ',':
                self.i += 1


def parse_literal(text: str, variables: Dict[str, Any] = None) -> Tuple[Any, int]:
    """读一个字面量，返回 (值, 读到的位置)。"""
    p = _Parser(text, variables or {})
    v = p.value()
    return v, p.i


_VAR = re.compile(r'(?:^|[;\s])(?:var|let|const)\s+')
_EXPORT = re.compile(r'export\s*\{([^}]*)\}')


def parse_module_export(text: str, export_name: str) -> Any:
    """从打包后的模块里取出名为 export_name 的导出值（例如 Zudoku 的 schema）。"""
    m = _EXPORT.search(text)
    if not m:
        raise JsLiteralError('no export statement')
    local = None
    for item in m.group(1).split(','):
        parts = item.strip().split(' as ')
        if (parts[-1].strip()) == export_name:
            local = parts[0].strip()
    if not local:
        raise JsLiteralError(f'module does not export {export_name}')
    variables: Dict[str, Any] = {}
    # 依次读顶层的 var 定义：var a=..., b=...;  字符串里碰巧出现的 “var ” 已在读过的范围内，跳过
    consumed = 0
    for vm in _VAR.finditer(text, 0, m.start()):
        if vm.start() < consumed:
            continue
        pos = vm.end()
        while True:
            name_m = _IDENT.match(text, pos)
            if not name_m or text[name_m.end():name_m.end() + 1] != '=':
                break
            value, used = parse_literal(text[name_m.end() + 1:], variables)
            variables[name_m.group(0)] = value
            pos = name_m.end() + 1 + used
            consumed = pos
            if text[pos:pos + 1] != ',':
                break
            pos += 1
    if local not in variables:
        raise JsLiteralError(f'cannot find value of {local}')
    return variables[local]
