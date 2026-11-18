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
updated_at: 2026-11-18
---

# PolyBolt WebSocket

> 通过一个 WebSocket 连接实时接收加密货币、股票类资产和 TWAP 参考价格。

PolyBolt 通过一个连接推送加密货币、股票类资产和 TWAP 参考价格。订阅需要 CLOB API 凭据。

如果你目前使用 RTDS，请阅读[从 RTDS 迁移到 PolyBolt](https://docs.polymarket.com/cn/migrate/rtds-to-polybolt.md)。

> [!WARNING]
>
> 价格订阅必须指定数据提供方。由 Chainlink
> 提供的订阅还需要你的 Chainlink API 密钥。见[发送你的 Chainlink API
> 密钥](#发送你的-chainlink-api-密钥)和[指定价格数据提供方](#指定价格数据提供方)。

## 连接

建立 WebSocket 连接：

```text theme={null}
wss://ws-live-v2.polymarket.com/ws
```

选择频道，完成认证，然后发送订阅请求。

## 频道

| 频道 | 数据 | 过滤条件 | 访问权限 |
| - | - | - | - |
| `price.crypto` | 加密货币参考价格 | `{"symbol": "btcusd", "provider": "chainlink"}` | CLOB API 凭据 |
| `price.equity` | 股票、ETF、外汇、贵金属和大宗商品参考价格 | `{"symbol": "aapl", "provider": "pyth"}` | CLOB API 凭据 |
| `price.crypto.twap` | Chainlink 的 60 秒时间加权平均价格（TWAP） | `{"symbol": "btcusd", "window_seconds": 60, "provider": "chainlink"}` | CLOB API 凭据 |
| `price.equity.twap` | Chainlink 的 60 秒外汇 TWAP 价格（`eurusd` 和 `usdjpy`） | `{"symbol": "eurusd", "window_seconds": 60, "provider": "chainlink"}` | CLOB API 凭据 |

符号使用小写，并在每个过滤条件中指定数据提供方（见[指定价格数据提供方](#指定价格数据提供方)）。

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

### 发送你的 Chainlink API 密钥

由 Chainlink 提供的订阅（包括 TWAP）除 CLOB API 凭据外，还需要你的 Chainlink API 密钥。

> [tab] TypeScript
>
> 使用已认证的 [SecureClient](https://docs.polymarket.com/cn/trading/wallets-auth.md)，指定 Chainlink 并通过 `providerApiKey` 传入密钥。
>
> ```ts theme={null}
> import { PriceProvider } from "@polymarket/client";
>
> const stream = await client.subscribe([
>   {
>     topic: "prices.crypto.twap",
>     symbols: ["btcusd"],
>     provider: PriceProvider.Chainlink,
>     providerApiKey: "<chainlink api key>",
>   },
> ]);
>
> try {
>   for await (const event of stream) {
>     // event: CryptoTwapPriceEvent
>   }
> } finally {
>   await stream.close();
> }
> ```

> [tab] Python
>
> 使用已认证的 [AsyncSecureClient](https://docs.polymarket.com/cn/trading/wallets-auth.md)，指定 Chainlink 并通过 `provider_api_key` 传入密钥。
>
> ```python theme={null}
> from polymarket.streams import CryptoTwapPriceSpec
>
> async with await client.subscribe(
>     CryptoTwapPriceSpec(
>         symbols=["btcusd"],
>         provider="chainlink",
>         provider_api_key="<chainlink api key>",
>     )
> ) as stream:
>     async for event in stream:
>         # event: CryptoTwapPriceEvent
>         pass
> ```

> [tab] API
>
> 在第一个 `auth` 帧中通过 `chainlink_api_key` 与 CLOB API 凭据一并发送密钥。如需更改密钥，请建立新连接。
>
> ```json theme={null}
> {
>   "op": "auth",
>   "rid": "a1",
>   "auth": {
>     "apiKey": "<api key>",
>     "secret": "<api secret>",
>     "passphrase": "<api passphrase>"
>   },
>   "chainlink_api_key": "<chainlink api key>"
> }
> ```

其他数据提供方的订阅不需要 Chainlink API 密钥。如果请求的数据提供方回退到 Chainlink，仍然需要该密钥。

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
| `chainlink_key_required` | 在未携带 Chainlink API 密钥认证的连接上发送了由 Chainlink 提供的订阅。 | 建立新连接，使用 `chainlink_api_key` 认证，然后重新发送订阅。 |

`chainlink_key_required` 还带有数值 `status` `4010`。它不是关闭码：连接保持打开。

## 订阅

发送要订阅的频道和过滤条件。以下请求在已使用 Chainlink API 密钥认证的连接上订阅来自 Chainlink 的 BTC 参考价格：

```json theme={null}
{
  "op": "subscribe",
  "rid": "s1",
  "subscriptions": [
    { "channel": "price.crypto", "filter": { "symbol": "btcusd", "provider": "chainlink" } }
  ]
}
```

一个批量帧只计一次速率限制。

### 指定价格数据提供方

加密货币和股票类资产价格可能来自多个数据提供方。每个负载都会在 `source` 中标明生产方。在过滤条件中添加 `provider` 来选择数据提供方：

```json theme={null}
{
  "op": "subscribe",
  "rid": "s2",
  "subscriptions": [
    { "channel": "price.crypto", "filter": { "symbol": "btcusd", "provider": "pyth" } }
  ]
}
```

`provider` 可取 `chainlink`、`pyth` 或 `binance`。Binance 仅提供 `price.crypto`，以规范的 USD 符号提供 USDT 现货收盘价。`subscribed` 确认帧会标明实际提供数据的提供方。服务端无法为该符号提供所指定的提供方时，会回退到该符号的默认提供方，并在确认帧中标明回退结果，因此请始终读取确认帧，而不要假设指定已生效。TWAP 频道仅由 Chainlink 提供，因此请指定 `chainlink`。

`chainlink`、`pyth` 和 `binance` 以外的值会被拒绝，返回 `bad_filter` 错误。

`price.crypto`、`price.equity`、`price.crypto.twap` 和 `price.equity.twap` 必须提供 `provider`。未提供 `provider` 的订阅会返回以下错误，连接保持打开：

```json theme={null}
{
  "op": "error",
  "code": "provider_required",
  "status": 4011,
  "channel": "price.crypto",
  "rid": "s2"
}
```

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
  "rid": "s1",
  "provider": "chainlink"
}
```

请求包含 `rid` 时，确认帧会原样返回该值。

| `op` | 含义 |
| - | - |
| `authed` | 认证成功，可以订阅需授权的频道。 |
| `subscribed` | 订阅已接受。`channel` 标识对应频道；在价格频道上，`provider` 标明实际提供数据的提供方。 |
| `unsubscribed` | 取消订阅请求已接受。`channel` 标识对应频道。 |
| `pong` | 服务端已收到应用层 `ping` 请求。 |
| `error` | 请求失败。`code` 标识原因。违反策略还可能导致连接关闭。 |

`chainlink_key_required` 和 `provider_required` 错误还带有数值 `status`，分别为 `4010` 和 `4011`。两者都不会关闭连接。

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
    { "channel": "price.crypto", "filter": { "symbol": "btcusd", "provider": "chainlink" } }
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
| `price.equity.twap` | `eurusd`、`usdjpy` |

TWAP 频道使用 `window_seconds: 60`。其他窗口不提供数据。

每个 `price.crypto` 符号都由 Chainlink（默认提供方）和 Binance 提供。`btcusd`、`ethusd`、`solusd`、`xrpusd`、`dogeusd` 和 `bnbusd` 也由 Pyth 提供；对 `hypeusd` 和 `zecusd` 指定 `pyth` 会回退到 Chainlink。`price.crypto.twap` 仅由 Chainlink 提供。

### 股票类资产价格

`price.equity` 支持以下小写符号：

| 资产类别 | 符号 |
| - | - |
| 股票 | `aapl`、`tsla`、`msft`、`googl`、`amzn`、`meta`、`nvda`、`nflx`、`pltr`、`open`、`rklb`、`abnb`、`coin`、`hood`、`spcx`、`intc`、`mstr`、`crcl`、`mu` |
| ETF | `qqq`、`spy`、`ewy`、`vxx` |
| 外汇 | `eurusd`、`gbpusd`、`usdcad`、`usdjpy`、`usdkrw`、`usdchf`、`usdmxn`、`usdzar`、`usdbrl`、`usdnok`、`usdsek`、`usdtry`、`dxy`（美元指数） |
| 贵金属 | `xauusd`、`xagusd` |
| 大宗商品 | `cll`（WTI 原油近月期货）、`hn`（亨利港天然气近月期货）、`cc3m`（铜三个月合约），以及 Chainlink 的 `wti`（WTI 原油期货）、`brent`（布伦特原油期货）和 `natgas`（天然气期货）；期货在合约滚动时沿用同一符号 |

每个股票类资产符号都有一个默认提供方，它会为该符号不支持的任何指定提供数据，包括所有 `binance` 指定：

| 符号 | 默认提供方 | 可指定 |
| - | - | - |
| `xauusd`、`xagusd`、`nvda`、`googl`、`tsla`、`spcx`、`mu` | `chainlink` | `pyth` |
| `intc`、`mstr`、`crcl`、`wti`、`brent`、`natgas` | `chainlink` | 无 |
| `eurusd`、`usdjpy` | `pyth` | `chainlink` |
| 其他所有股票类资产符号 | `pyth` | 无 |

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

重连后，为需授权频道重新认证，并连同 `provider` 重新发送订阅。使用新快照初始化应用，序号从头开始。


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
