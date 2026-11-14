---
api_type: reference
source_type: llms_txt
version: ''
scope: crypto
asset_class: prediction_market
domain: exchanges
provider: polymarket
provider_name: Polymarket
product: api
product_id: polymarket
source_url: 'https://docs.polymarket.com/cn/migrate/data-api-v1-to-v2'
updated_at: 2026-11-13
---

# 从 Data API v1 迁移到 v2

> 把集成从原有的 Data API 路由迁移到 v2 对应路由：路由映射、契约变化，以及会计快照的停用。

Data API v2 用一套跨所有读取共享的契约取代了原有的按路由各自定义的契约。
可以逐个调用点迁移；新的集成应直接从 v2 开始。

v2 路由使用 `https://data-api.polymarket.com` 和 `/v2` 前缀。

> [!WARNING]
>
> **Data API v1 于 2026 年 11 月 2 日停用。** 请按下方的路由映射迁移到 v2 路由。

## 变化内容

**响应结构。** v1 路由返回裸数组或裸对象。v2 的每个响应都把有效负载包在
`data` 中，分页路由额外返回 `pagination` 对象。查询无结果时返回
`data: null` 或空列表，绝不会返回错误。

**分页。** v1 通过 `limit`/`offset` 分页，且 `offset` 上限为 10,000 行。
v2 通过不透明游标分页：跟随 `pagination.next_cursor` 直到其为 `null`，
无需管理 offset 计算，且数据流路由在新行写入期间保持一致。参见
[Data API v2 概览](https://docs.polymarket.com/cn/api-reference/data-api/overview.md)中的分页说明。

**字段命名。** v1 响应使用 `camelCase`（`proxyWallet`、`conditionId`）。
v2 响应使用 `snake_case`（`proxy_wallet`、`condition_id`）。v2 的请求参数
同时接受两种拼写。

**市场选择。** v1 用 `market` 参数选择市场。v2 统一为 `condition`
（别名 `condition_id`、`conditionId`），最多接受 20 个不同的逗号分隔
condition id。`event_id` 过滤保持不变。

**被拒绝的 v1 参数。** v2 会对旧的 `market`、`market_id`、`marketId` 与 `offset` 参数返回 HTTP `400`，而不是忽略它们。将市场筛选改为 `condition`、`condition_id` 或 `conditionId`。删除 `offset`，即使其值为 `0`。分页读取使用 `cursor`，非分页读取则不传分页参数。

**仓位生命周期。** v2 把三个 v1 路由合并为一个：`GET /v2/positions` 通过
`status` 过滤器（`OPEN`、`REDEEMABLE`、`REDEEMABLE_LOST`、`MERGEABLE`、`CLOSED`）服务完整生命周期，每行
携带 `redeemable` 与 `mergeable` 标志，取代了独立的 `/closed-positions`
和 `/v1/market-positions` 路由。

## 路由映射

| v1 路由 | v2 路由 | 说明 |
| - | - | - |
| `GET /positions` | `GET /v2/positions` | `status` 默认为未平仓仓位。`market` 改为 `condition` |
| `GET /closed-positions` | `GET /v2/positions?status=CLOSED` | 并入统一的生命周期 |
| `GET /v1/market-positions` | `GET /v2/positions?condition=…` | 通过同一路由按市场维度查询 |
| `GET /trades` | `GET /v2/trades` | |
| `GET /activity` | `GET /v2/activity` | |
| `GET /v1/activity/combos` | `GET /v2/activity/combos` | |
| `GET /v1/positions/combos` | `GET /v2/positions/combos` | |
| `GET /value` | `GET /v2/value` | |
| `GET /traded` | `GET /v2/user-stats` | `data.trades` 是已交易的不同市场数量。未知用户返回 `data: null` |
| `GET /holders` | `GET /v2/holders` | 可选的 `include_pnl=true` 为每个持仓者附加入场成本与盈亏 |
| `GET /oi` | `GET /v2/oi` | |
| `GET /live-volume` | `GET /v2/live-volume` | |
| `GET /v1/leaderboard` | `GET /v2/leaderboard` | |
| `GET /v1/builders/leaderboard` | `GET /v2/builders/leaderboard` | |
| `GET /v1/builders/volume` | `GET /v2/builders/volume` | |
| | `GET /v2/approvals` | |

每个 v2 接口页面记录了完整的参数集与行结构；多个路由接受 v1 对应路由
不支持的过滤器。

## v2 新增

v2 新增以下读取能力。用户资料统计也涵盖原有的已交易市场计数：

| 路由 | 返回内容 |
| - | - |
| `GET /v2/user-pnl` | 用户盈亏曲线 |
| `GET /v2/user-stats` | 用户资料统计 |
| `GET /v2/user-volume` | 用户交易量 |
| `GET /v2/biggest-winners` | 最大盈利榜 |
| `GET /v2/prices-history` | 代币价格历史 |
| `GET /v2/resolutions` | 市场结算状态 |
| `GET /v2/tokens` | 按代币 ID 或条件查询代币 |
| `GET /v2/status` | 数据新鲜度 |

## 会计快照停用

`GET /v1/accounting/snapshot` 于 2026 年 11 月 2 日随 Data API v1 停用。
其 CSV 文件 ZIP 归档没有 v2 对应版本。请移除对此路由的调用；v2 的组合价值、
仓位和活动读取不能提供等价的会计导出。

## SDK 迁移到 Data API V2

从 `0.10.0` 版本开始，两个官方 SDK 均支持 Data API v2：TypeScript 包
`@polymarket/client` 和 Python 包 `polymarket-client`。迁移时需要更新的
破坏性变更、方法重命名、响应字段和分页行为，请参阅
[TypeScript SDK 更新日志](https://docs.polymarket.com/changelog/sdks.md#typescript)或
[Python SDK 更新日志](https://docs.polymarket.com/changelog/sdks.md#python)。


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
