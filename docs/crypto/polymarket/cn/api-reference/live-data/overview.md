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
source_url: 'https://docs.polymarket.com/cn/api-reference/live-data/overview'
updated_at: 2026-11-13
---

# PolyBolt WebSocket

> 通过一个 WebSocket 连接实时接收加密货币、股票类资产和 TWAP 参考价格。

PolyBolt 通过一个连接推送加密货币、股票类资产和 TWAP 参考价格。订阅需要 CLOB API 凭据。

如果你目前使用 RTDS，请阅读[从 RTDS 迁移到 PolyBolt](https://docs.polymarket.com/cn/migrate/rtds-to-polybolt.md)。

## 连接

建立 WebSocket 连接：

```text theme={null}
wss://ws-live-v2.polymarket.com/ws
```

选择频道，完成认证，然后发送订阅请求。

## 频道

| 频道 | 数据 | 过滤条件 | 访问权限 |
| - | - | - | - |
| `price.crypto` | 加密货币参考价格 | `{"symbol": "btcusd"}` | CLOB API 凭据 |
| `price.equity` | 股票、ETF、外汇、贵金属和大宗商品参考价格 | `{"symbol": "aapl"}` | CLOB API 凭据 |
| `price.crypto.twap` | Chainlink 的 60 秒时间加权平均价格（TWAP） | `{"symbol": "btcusd", "window_seconds": 60}` | CLOB API 凭据 |

符号使用小写。

## 为需授权频道认证

订阅参考价格前，在已建立的连接上发送你的 [CLOB API 凭据](https://docs.polymarket.com/cn/getting-started/api.md#身份验证)：

```json theme={null}
{
  "op": "auth",
  "rid": "a1",
  "auth": {
    "apiKey": "<api key>",
    "secret": "<api secret>",
    "passphrase": "<api passphrase>"
  }
}
```

等待服务端确认认证成功：

```json theme={null}
{
  "op": "authed",
  "rid": "a1"
}
```

服务端通过错误确认报告认证问题，例如：

```json theme={null}
{
  "op": "error",
  "code": "auth_required",
  "channel": "price.crypto",
  "rid": "s1"
}
```

以下错误不会关闭连接：

| 错误码 | 含义 | 处理方式 |
| - | - | - |
| `auth_required` | 订阅时尚未认证。 | 完成认证后重新发送订阅。 |
| `auth_invalid` | 凭据被拒绝。 | 修正凭据后重试。 |
| `auth_unavailable` | 认证服务暂时不可用。 | 等待后重试认证。 |

## 订阅

发送要订阅的频道和过滤条件。以下请求在已认证的连接上订阅 BTC 参考价格：

```json theme={null}
{
  "op": "subscribe",
  "rid": "s1",
  "subscriptions": [
    { "channel": "price.crypto", "filter": { "symbol": "btcusd" } }
  ]
}
```

一个批量帧只计一次速率限制。

## 信封

数据信封承载快照和实时更新。确认帧报告请求的处理结果。

```json 实时更新 theme={null}
{
  "v": 1,
  "channel": "price.crypto",
  "seq": 2,
  "ts": 1788973001000,
  "payload": {
    "symbol": "btcusd",
    "value": 64126.0,
    "full_accuracy_value": "64126.00000000",
    "timestamp": 1788973001000
  }
}
```

```json 快照 theme={null}
{
  "v": 1,
  "channel": "price.crypto",
  "seq": 1,
  "ts": 1788973000000,
  "snapshot": true,
  "payload": {
    "symbol": "btcusd",
    "data": [
      {
        "timestamp": 1788972880000,
        "value": 64123.5,
        "full_accuracy_value": "64123.50000000"
      },
      {
        "timestamp": 1788972881000,
        "value": 64125.1,
        "full_accuracy_value": "64125.10000000"
      }
    ]
  }
}
```

```json 确认帧 theme={null}
{
  "op": "subscribed",
  "channel": "price.crypto",
  "rid": "s1"
}
```

请求包含 `rid` 时，确认帧会原样返回该值。

| `op` | 含义 |
| - | - |
| `authed` | 认证成功，可以订阅需授权的频道。 |
| `subscribed` | 订阅已接受。`channel` 标识对应频道。 |
| `unsubscribed` | 取消订阅请求已接受。`channel` 标识对应频道。 |
| `pong` | 服务端已收到应用层 `ping` 请求。 |
| `error` | 请求失败。`code` 标识原因。违反策略还可能导致连接关闭。 |

每个新订阅都会收到确认和一帧快照。使用快照初始化本地状态，再应用最新价格。快照包含前两分钟的数据，没有近期数据时 `data` 数组为空。重复订阅已有的频道和过滤条件会再次收到确认，但不会收到新快照。

数据信封中的字段：

* `seq` 按连接、按频道连续，快照也占用序号。重连后序号重置。
* `ts` 是生产方的事件时间，单位为 Unix 毫秒。
* `snapshot: true` 标识初始快照。
* 可选字段 `dropped` 表示自上一帧送达后，该频道因客户端落后而丢弃的帧数。

只在同一连接的同一频道内比较序号。每种消息的完整结构见[实时数据频道](https://docs.polymarket.com/cn/api-reference/wss/polybolt.md)。机器可读的契约位于 `https://ws-live-v2.polymarket.com/asyncapi.json`。

## 取消订阅

使用相同的频道和过滤条件，并将 `op` 设为 `"unsubscribe"`：

```json theme={null}
{
  "op": "unsubscribe",
  "subscriptions": [
    { "channel": "price.crypto", "filter": { "symbol": "btcusd" } }
  ]
}
```

服务端通过 `unsubscribed` 确认取消订阅。`subscribe` 和 `unsubscribe` 都支持单个 `channel` 与 `filter`，或 `subscriptions` 数组。

## 支持的符号

### 加密货币价格

| 频道 | 符号 |
| - | - |
| `price.crypto` | `btcusd`、`ethusd`、`solusd`、`xrpusd`、`dogeusd`、`hypeusd`、`bnbusd`、`zecusd` |
| `price.crypto.twap` | `btcusd`、`ethusd`、`solusd`、`xrpusd`、`dogeusd`、`hypeusd`、`bnbusd`、`zecusd` |

`price.crypto.twap` 使用 `window_seconds: 60`。其他窗口不提供数据。

### 股票类资产价格

`price.equity` 支持以下小写符号：

| 资产类别 | 符号 |
| - | - |
| 股票 | `aapl`、`tsla`、`msft`、`googl`、`amzn`、`meta`、`nvda`、`nflx`、`pltr`、`open`、`rklb`、`abnb`、`coin`、`hood`、`spcx`、`intc`、`mstr`、`crcl`、`mu` |
| ETF | `qqq`、`spy`、`ewy`、`vxx` |
| 外汇 | `eurusd`、`gbpusd`、`usdcad`、`usdjpy`、`usdkrw`、`usdchf`、`usdmxn`、`usdzar`、`usdbrl`、`usdnok`、`usdsek`、`usdtry`、`dxy`（美元指数） |
| 贵金属 | `xauusd`、`xagusd` |
| 大宗商品 | `cll`（WTI 原油近月期货）、`hn`（亨利港天然气近月期货）、`cc3m`（铜三个月合约）；近月期货在合约滚动时沿用同一符号 |

## 限制与存活检测

| 限制 | 值 | 超限后 |
| - | - | - |
| 每连接活跃订阅数 | 64 个 `(channel, filter)` | `sub_limit` 错误，然后关闭 `4008` |
| subscribe/unsubscribe 帧 | 每秒 20 帧（批量帧计一次） | `rate_limited` 错误，然后关闭 `4008` |
| 帧大小 | 64 KB | 关闭 `4008` |
| 每连接 auth 帧数 | 8 | `auth_attempts` 错误，然后关闭 `4008` |

服务端每 25 秒发送一次 WebSocket ping，标准客户端会自动回应。连续两次未收到 pong 时，连接以 `4002` 关闭。

也可以发送 `{ "op": "ping" }` 在应用层检查连接。服务端回复 `pong`。

## 关闭码与重连

根据关闭码选择重试方式：

| 码 | 含义 | 客户端行为 |
| - | - | - |
| `4001` | 认证失败 | 修正认证后再重连。 |
| `4002` | 消费过慢或 pong 超时 | 使用指数退避并添加随机延迟。反复发生时减少订阅量。 |
| `4003` | 服务端排空连接 | 在 0 到 10 秒的均匀随机延迟后重连。 |
| `4008` | 违反策略 | 修正请求或超限问题后再重连。 |
| `1006` | 异常断开 | 使用指数退避和完全随机抖动，基数为 1 秒，上限为 30 秒。 |

如果连接请求被以 HTTP `429` 或 `503` 拒绝，将 `Retry-After` 视为最短等待时间并添加随机延迟。浏览器客户端看到的握手失败表现为 `1006`，应使用指数退避和完全随机抖动。

重连后，为需授权频道重新认证并重新发送订阅。使用新快照初始化应用，序号从头开始。


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
