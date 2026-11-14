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
source_url: 'https://docs.polymarket.com/cn/api-reference/data-api/overview'
updated_at: 2026-11-13
---

# Data API v2

> 通过统一的响应契约读取钱包投资组合、交易与活动流、市场状态以及排行榜。

Data API 回答“发生了什么、谁持有什么”：钱包投资组合与盈亏、交易与活动流、
持仓者与未平仓量等市场状态，以及各类排行榜。v2 让所有读取共享同一套契约：
统一的响应结构、游标分页和统一的标识符体系。掌握任意一个接口的用法后，
其余接口的消费方式完全相同。

所有 v2 路由的服务地址为：

```
https://data-api.polymarket.com/v2
```

无需 API key，也无需身份验证。

## 发起第一个请求

查询某个钱包的当前仓位：

```bash theme={null}
curl "https://data-api.polymarket.com/v2/positions?user=0x983eedfbd75803602e4a6e6ea9aab6dc6b9c6748&limit=1"
```

每个响应都把有效负载包在 `data` 中；分页路由额外返回 `pagination` 对象
（为简洁起见，以下示例省略了部分行字段）：

```json theme={null}
{
  "data": [
    {
      "proxy_wallet": "0x983eedfbd75803602e4a6e6ea9aab6dc6b9c6748",
      "condition_id": "0xd9b06e2fd9ddb7ab61c9e3d5d8e074c555802478bbf75145804ff709a4246f79",
      "token_id": "31974447302330162086995746309500877260929998201718217388109724292047967921664",
      "outcome": "Yes",
      "title": "Will ŠK Slovan Bratislava win on 2026-08-19?",
      "status": "REDEEMABLE",
      "current_size": 86780.64,
      "avg_price": 0.5203,
      "entry_cost_usdc": 45159.4653,
      "current_value": 0.0,
      "realized_pnl": -1082.5533,
      "unrealized_pnl": -45159.4653
    }
  ],
  "pagination": {
    "limit": 1,
    "offset": 0,
    "has_more": true,
    "next_cursor": "eyJkYXRhIjp7InR5cGUiOiJwb3NpdGlvbnMi…"
  }
}
```

查询无结果时返回 `data: null` 或空列表，绝不会返回错误。每个接口的参考页
描述了完整的行结构和所有过滤器。

## 使用游标分页

分页仅通过游标进行，没有 `offset` 查询参数。遍历结果集的步骤：

1. 发送第一个请求，可携带可选的 `limit`（各接口的默认值与上限见其文档）。
2. 从响应中读取 `pagination.next_cursor`，在下一个请求中携带
   `cursor=<next_cursor>` 重新发送。
3. 当 `next_cursor` 为 `null` 时停止。`has_more` 是精确值，页面为空或
   不满并不代表遍历已经结束。

游标是不透明、带签名、按接口区分类型的。保持遍历一致需要遵守两条规则：

* 在数据流接口（`/v2/trades`、`/v2/activity`、`/v2/activity/combos`）上，
  每一页都要重发相同的过滤条件。游标只携带定位锚点，中途更改过滤器会
  静默地重新定位数据流。
* 在游标绑定查询条件的接口（仓位、榜单、组合仓位）上，重申相同的条件可以，
  但与之矛盾会返回 `400`。`/v2/positions` 须继续发送相同的 `user` 或
  `condition` 锚点及全部筛选条件，包括 `title`、用于缩小范围的 `condition`
  和 `start`/`end`。游标不携带这些筛选条件；省略它们可能扩大结果范围。
  游标绑定锚点、状态、排序字段和方向。继续请求时，`/v2/positions/combos` 须携带
  `user` 和 `cursor`，`/v2/holders` 须携带 `condition` 和 `cursor`。
  其他此类接口仅需游标。

`limit` 参数只对第一页生效；一旦提供了 `cursor`，以游标自身的页大小为准。
`pagination` 中的 `offset` 字段仅用于跨页行号展示，不是请求参数。

## 通用约定

所有 v2 接口遵循相同的词汇与编码规则。

### 标识符

| 标识符 | 含义 |
| - | - |
| `condition` | 链上 condition id（`0x` 前缀、64 位十六进制）的统一查询键。`condition_id` 与 `conditionId` 是可接受的别名。在允许列表的地方，最多接受 20 个不同的逗号分隔值。 |
| `event_id` | 事件 id，与 Gamma API 的 `/events` 路由一致。 |
| `market_id` | 市场 id，与 Gamma API 的 `/markets` 路由一致。在响应行中与链上 `condition_id` 并列出现。 |
| `token_id` | 结果代币 id。`/v2/prices-history` 的查询键。 |

查询参数同时接受 `snake_case` 与 `camelCase` 两种拼写。

### 单位与哨兵值

* 不带后缀的 `volume` 和 `size` 值是结果代币**份额**；带 `_usdc` 后缀的
  字段是美元金额；带 `taker_` 前缀的交易量只统计每笔交易的一侧。
* 所有金额都是 JSON 数字。
* `outcome_index: 999` 表示无法标注该结果。
* 数字字段缺失或为 `null` 表示不可用，绝不表示零。

### 时间窗口

带时间窗口的路由通过 `start` 和 `end` 接收 epoch 秒。省略或为 `0` 的边界
在不同路由上的处理不同（例如 `/v2/activity` 会把省略的 `start` 下限设为
三年前，而 `/v2/prices-history` 会对 `0` 边界返回 `400`），依赖默认行为前
请先查阅各接口页面的参数文档。

### 价格历史的分辨率

`/v2/prices-history` 是唯一一条分辨率会随时间失效的路由，因此窗口的**起始时间
有多早**决定了它能以何种精度返回。一分钟数据保留 7 天，五分钟保留 60 天，
三十分钟保留 90 天；三小时与十二小时序列永久保留。因此 `bucket_seconds=60`
搭配一个月前开始的窗口是一对互不兼容的取值：两者各自合法，但它们的交集里
没有数据。

两种请求方式的行为有意不同：

* **传入 `bucket_seconds`**：严格按所请求的宽度返回。若窗口所处时段该分辨率
  已过期，则返回空页，而不会悄悄改用其他宽度替代。
* **省略该参数**：由服务端选择一个真正能服务该窗口的宽度，先按窗口跨度取值，
  若该粒度无法覆盖窗口的起点，则继续放宽。

每个数据点都带有 `resolution_seconds`，说明它实际以何种宽度返回；请读取该字段，
不要假定它等于近期窗口会给出的宽度。对于跨多天的窗口，建议传入与层级对齐的
`bucket_seconds`（300、1800、10800、43200）或直接省略；跨多天使用 60 秒宽度是
唯一一种既慢、且在超过 7 天后还会返回空结果的组合。

### 错误与限流

请求错误返回 `400` 与消息结构：

```json theme={null}
{ "error": "required query param 'user' or 'condition' not provided" }
```

负载过高时返回 `429` 并携带 `Retry-After` 响应头；请在给定延迟后重试。
`/v2` 路由基于 IP 的请求限制见[速率限制](https://docs.polymarket.com/cn/api-reference/rate-limits.md)页面。

## 接口列表

> [accordion] 钱包
>
> | 接口 | 返回内容 |
> | - | - |
> | `GET /v2/positions` | 用户或市场的仓位，覆盖完整生命周期（`OPEN`、`REDEEMABLE`、`REDEEMABLE_LOST`、`MERGEABLE`、`CLOSED`） |
> | `GET /v2/positions/combos` | 组合仓位 |
> | `GET /v2/value` | 投资组合价值 |
> | `GET /v2/approvals` | 钱包授权状态 |
> | `GET /v2/user-pnl` | [用户盈亏曲线](https://docs.polymarket.com/cn/trading/wallet-activity.md#钱包盈亏历史) |
> | `GET /v2/user-stats` | [用户资料统计](https://docs.polymarket.com/cn/trading/wallet-activity.md#钱包统计) |
> | `GET /v2/user-volume` | [用户交易量](https://docs.polymarket.com/cn/trading/wallet-activity.md#钱包交易量) |

> [accordion] 数据流
>
> | 接口 | 返回内容 |
> | - | - |
> | `GET /v2/trades` | 钱包、市场、事件或全局的交易流 |
> | `GET /v2/activity` | 账户活动 |
> | `GET /v2/activity/combos` | 组合活动 |

> [accordion] 市场数据
>
> | 接口 | 返回内容 |
> | - | - |
> | `GET /v2/holders` | 市场最大持仓者 |
> | `GET /v2/oi` | 市场未平仓量 |
> | `GET /v2/live-volume` | 事件实时成交量 |
> | `GET /v2/prices-history` | 代币价格历史 |
> | `GET /v2/resolutions` | [市场结算状态](https://docs.polymarket.com/cn/market-data/public-analytics.md#市场结算) |
> | `GET /v2/tokens` | [代币查询](https://docs.polymarket.com/cn/market-data/public-analytics.md#代币查询)：按代币 ID 或条件查询市场、结果与负风险结构 |

> [accordion] 榜单
>
> | 接口 | 返回内容 |
> | - | - |
> | `GET /v2/leaderboard` | 交易者榜单 |
> | `GET /v2/biggest-winners` | [最大盈利榜](https://docs.polymarket.com/cn/market-data/public-analytics.md#最大盈利榜) |
> | `GET /v2/builders/leaderboard` | Builder 排行榜 |
> | `GET /v2/builders/volume` | Builder 交易量走势 |

> [accordion] 服务
>
> | 接口 | 返回内容 |
> | - | - |
> | `GET /v2/status` | 数据新鲜度 |

完整的机器可读契约发布在
[`https://data-api.polymarket.com/v2/openapi.json`](https://data-api.polymarket.com/v2/openapi.json)，
交互式浏览器位于
[`https://data-api.polymarket.com/v2/docs`](https://data-api.polymarket.com/v2/docs)。

## 下一步

* 正在使用 v1 Data API 路由？参见
  [从 Data API v1 迁移到 v2](https://docs.polymarket.com/cn/migrate/data-api-v1-to-v2.md)。
* 在侧边栏浏览各接口页面，获取完整的参数与响应文档。


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
