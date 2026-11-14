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
source_url: 'https://docs.polymarket.com/cn/migrate/rtds-to-polybolt'
updated_at: 2026-11-13
---

# 从 RTDS 迁移到 PolyBolt

> 通过 TypeScript、Python SDK 或 WebSocket API 将价格订阅从 RTDS 迁移到 PolyBolt。

把参考价格订阅迁移到 PolyBolt，同时保留应用中按事件处理价格的流程。参考价格需要认证。

## 迁移 API 集成

更新连接、认证和订阅帧。完整协议见[实时数据频道](https://docs.polymarket.com/cn/api-reference/wss/polybolt.md)。

### 变化点

| RTDS | PolyBolt |
| - | - |
| `wss://ws-live-data.polymarket.com` | `wss://ws-live-v2.polymarket.com/ws` |
| 每 5 秒发送文本帧 `PING` | 无需发送。服务端每 25 秒 ping（可选 `{"op":"ping"}`） |
| `{"action":"subscribe","subscriptions":[{"topic","type","filters"}]}` | `{"op":"subscribe","subscriptions":[{"channel","filter"}]}`。`filter` 是 JSON 对象而非字符串 |
| 带数据源名称的价格和 TWAP 主题 | 频道 `price.crypto`、`price.crypto.twap`、`price.equity`（见下方映射） |
| 每条消息 `{"topic","type","timestamp","payload"}` | `{"v":1,"channel","seq","ts","snapshot"?,"dropped"?,"payload"}`。负载取决于频道 |
| 安静的符号没有任何消息 | 每个订阅一帧快照（`snapshot: true`），可能为空 |
| 无序号 | 按频道连续的 `seq` 与 `dropped` 计数 |
| 公开 | 参考价格频道需通过 `{"op":"auth"}` 提交 CLOB API 凭据 |
| 无限制 | 64 个订阅、每秒 20 个订阅帧、64 KB 帧、8 个 auth 帧。超限关闭 `4008` |
| 原始 `1006` 关闭 | `4001` 认证、`4002` 消费过慢、`4003` 排空、`4008` 策略 |

### 主题映射

| RTDS 主题 | RTDS 过滤条件 | PolyBolt 频道 | PolyBolt 过滤条件 | 说明 |
| - | - | - | - | - |
| `crypto_prices`（Binance） | `btcusdt` | `price.crypto` | `{"symbol":"btcusd"}` | 数据源默认改为 Chainlink，计价货币从 USDT 改为 USD。 |
| `crypto_prices_chainlink` | `{"symbol":"btc/usd"}` | `price.crypto` | `{"symbol":"btcusd"}` | 数据源仍为 Chainlink，即 `price.crypto` 的默认数据源。使用 `btcusd` 代替 `btc/usd`。 |
| `crypto_prices_twap_sixty` | `{"symbol":"btc/usd"}` | `price.crypto.twap` | `{"symbol":"btcusd","window_seconds":60}` | 60 秒 Chainlink TWAP |
| `crypto_prices_twap_thirty` | `{"symbol":"btc/usd"}` | 无 | 无 | PolyBolt 不提供 30 秒窗口 |
| `equity_prices` | `{"symbol":"AAPL"}` | `price.equity` | `{"symbol":"aapl"}` | 目录相同，改为小写：股票、ETF、外汇、贵金属及大宗商品 `wti`、`cc`、`ngd` |

> [!WARNING]
>
> 加密货币现货和 TWAP 订阅现在使用以 `usd` 结尾的小写符号，不再使用 `usdt`。请将
> `btcusdt` 或 `btc/usd` 改为 `btcusd`，并对所有订阅的加密货币符号使用相同格式。

实时价格负载包含 `symbol`、`value`、`full_accuracy_value`、`timestamp` 和标识价格提供商的 `source`。对于 Chainlink 支持的符号，`price.crypto` 和 `price.equity` 默认使用 Chainlink；可在过滤条件中添加 `provider` 来指定价格提供商。股票类更新还可能包含 `received_at` 和 `is_carried_forward`。TWAP 使用 `window_seconds`。请优先使用精确小数 `full_accuracy_value`，而非浮点 `value`。旧版 TWAP 帧使用 `window_s` 和 E18 定点价格，不要对 PolyBolt 的小数字符串再进行 E18 换算。

### 迁移前后

```json RTDS theme={null}
{
  "action": "subscribe",
  "subscriptions": [
    { "topic": "crypto_prices", "type": "update", "filters": "btcusdt" }
  ]
}
```

```json PolyBolt theme={null}
{ "op": "auth", "auth": { "apiKey": "<api key>", "secret": "<api secret>", "passphrase": "<api passphrase>" } }
{ "op": "subscribe", "subscriptions": [ { "channel": "price.crypto", "filter": { "symbol": "btcusd" } } ] }
```

### 客户端清单

1. 指向 `wss://ws-live-v2.polymarket.com/ws`，删除 `PING` 文本心跳。
2. 订阅价格频道前先发送带 CLOB API 凭据的 `{"op":"auth", ...}`。
3. 在每个连接上批量发送订阅，活跃订阅不超过 64 个。
4. 使用快照初始化本地状态，再应用实时更新。只在同一连接的同一频道内比较 `seq`。
5. `4003` 做一次带抖动的重连，`4008` 视为 bug，每次重连后重新订阅。

## 评论数据流停用

实时评论数据流即将停用，且不会提供替代的流式频道。支持的评论列表查询方式见[评论](https://docs.polymarket.com/cn/market-data/realtime-data.md#评论)。

## RTDS 活动数据流

`activity` 主题继续使用 RTDS，目前没有对应的 PolyBolt 频道。

## 将 SDK 迁移到 PolyBolt

### 迁移 60 秒 TWAP 订阅

> [tab] TypeScript
>
> `@polymarket/client` 从 `0.11.0` 版本开始支持 PolyBolt。
> 通过 `createSecureClient` 迁移 BTC/USD 的 60 秒 TWAP 订阅。已弃用的 RTDS 价格主题计划在 `0.11.0` 发布一个月后移除。
>
> > [accordion] 迁移前：RTDS
> >
> > ```ts theme={null}
> > import { createPublicClient } from "@polymarket/client";
> >
> > const client = createPublicClient();
> > const stream = await client.subscribe([
> >   {
> >     topic: "prices.crypto.chainlink.twap",
> >     symbols: ["btc/usd"],
> >     windowSeconds: 60,
> >   },
> > ]);
> >
> > try {
> >   for await (const event of stream) {
> >     if (event.type === "update") {
> >       const price = event.payload.value;
> >     }
> >   }
> > } finally {
> >   await stream.close();
> > }
> > ```
>
> **1. 创建已认证客户端**
>
> 设置 `POLYMARKET_PRIVATE_KEY`。本例使用签名者的 EOA 地址，默认连接生产环境。
>
> ```ts theme={null}
> import { createSecureClient } from "@polymarket/client";
> import { privateKey } from "@polymarket/client/viem";
>
> const signer = privateKey(process.env.POLYMARKET_PRIVATE_KEY);
> const client = await createSecureClient({
>   signer,
>   wallet: await signer.getAddress(),
> });
> ```
>
> **2. 订阅价格**
>
> 将主题从 `prices.crypto.chainlink.twap` 改为 `prices.crypto.twap`，并显式提供 `symbols` 列表。将 `btc/usd` 改为 `btcusd`，并从订阅输入中移除 `windowSeconds`。新主题固定使用 60 秒窗口。
>
> ```ts theme={null}
> const stream = await client.subscribe([
>   { topic: "prices.crypto.twap", symbols: ["btcusd"] },
> ]);
>
> try {
>   for await (const event of stream) {
>     // event: CryptoTwapPriceEvent
>     if (event.type === "subscribe") {
>       const history = event.payload.data;
>       // Seed local state from the snapshot.
>     } else {
>       const price = event.payload.value;
>       const observedAt = event.payload.timestamp;
>       // Apply the latest price.
>     }
>   }
> } finally {
>   await stream.close();
> }
> ```
>
> > [accordion] Output: CryptoTwapPriceEvent
> >
> > **events: CryptoTwapPriceEvent\[]**
> >
> > ```ts CryptoTwapPriceEvent Union theme={null}
> > type CryptoTwapPriceEvent =
> >   | {
> >       topic: "prices.crypto.twap";
> >       type: "subscribe";
> >       timestamp: EpochMilliseconds;
> >       seq?: number;
> >       dropped?: number;
> >       payload: {
> >         symbol: string;
> >         data: { timestamp: EpochMilliseconds; value: DecimalString }[];
> >         windowSeconds: 60;
> >       };
> >     }
> >   | {
> >       topic: "prices.crypto.twap";
> >       type: "update";
> >       timestamp: EpochMilliseconds;
> >       seq?: number;
> >       dropped?: number;
> >       payload: {
> >         symbol: string;
> >         timestamp: EpochMilliseconds;
> >         value: DecimalString;
> >         windowSeconds: 60;
> >       };
> >     };
> > ```
> >
> > ```json CryptoTwapPriceEvent Example theme={null}
> > [
> >   {
> >     "topic": "prices.crypto.twap",
> >     "type": "subscribe",
> >     "timestamp": 1788886175000,
> >     "seq": 2,
> >     "payload": {
> >       "symbol": "btcusd",
> >       "data": [
> >         {
> >           "timestamp": 1788886057000,
> >           "value": "78788.525642908795142144"
> >         },
> >         {
> >           "timestamp": 1788886058000,
> >           "value": "78788.786579938813673472"
> >         },
> >         {
> >           "timestamp": 1788886059000,
> >           "value": "78789.052518750893375488"
> >         }
> >       ],
> >       "windowSeconds": 60
> >     }
> >   },
> >   {
> >     "topic": "prices.crypto.twap",
> >     "type": "update",
> >     "timestamp": 1788886177000,
> >     "seq": 3,
> >     "payload": {
> >       "symbol": "btcusd",
> >       "timestamp": 1788886177000,
> >       "value": "78803.715261094101516288",
> >       "windowSeconds": 60
> >     }
> >   }
> > ]
> > ```
>
> 返回事件仍包含 `windowSeconds: 60`。旧版 30 秒 TWAP 工作流没有 PolyBolt 替代方案。
>
> `subscribe()` 等待服务端接受订阅。快照事件的 `payload.data` 用于初始化历史。更新事件保留 `symbol`、`timestamp`、小数字符串 `value` 和 `windowSeconds`。
>
> 新的加密货币主题要求显式提供 `btcusd` 等小写 USD 符号。`btc/usd`、`btcusdt` 和 `BTCUSD` 会触发 `UserInputError`，SDK 不会自动改写这些输入。

> [tab] Python
>
> 使用 `AsyncSecureClient.subscribe` 迁移 BTC/USD 的 60 秒 TWAP 订阅。在异步函数中运行以下步骤。
>
> > [!NOTE]
> >
> > `polymarket-client` 从 `0.11.0` 版本开始支持 PolyBolt。旧版 RTDS
> > 价格规格已标记为弃用。
>
> > [accordion] 迁移前：RTDS
> >
> > 旧版订阅通过 `AsyncPublicClient.subscribe` 或 `AsyncSecureClient.subscribe` 使用以下规格：
> >
> > ```python theme={null}
> > from polymarket.streams import CryptoPricesChainlinkTwapSpec
> >
> > spec = CryptoPricesChainlinkTwapSpec(symbols=["btc/usd"], window_seconds=60)
> > ```
>
> **1. 创建已认证的客户端**
>
> 将 `POLYMARKET_PRIVATE_KEY` 设置为签名者私钥。本例使用签名者的 EOA 地址。`AsyncSecureClient.create` 会派生或获取 API 凭据。
>
> ```python theme={null}
> import os
>
> from eth_account import Account
> from polymarket import AsyncSecureClient
>
> private_key = os.environ["POLYMARKET_PRIVATE_KEY"]
> client = await AsyncSecureClient.create(
>     private_key=private_key,
>     wallet=Account.from_key(private_key).address,
> )
> ```
>
> **2. 订阅价格**
>
> 使用 `CryptoTwapPriceSpec` 指定 BTC/USD。异步上下文管理器会在退出时关闭订阅。
>
> ```python theme={null}
> from polymarket.streams import CryptoTwapPriceSpec
>
> async with await client.subscribe(
>     CryptoTwapPriceSpec(symbols=["btcusd"])
> ) as stream:
>     async for event in stream:
>         # event: CryptoTwapPriceEvent
>         if event.type == "subscribe":
>             history = event.payload.data
>             # 使用快照初始化本地状态。
>         else:
>             price = event.payload.value
>             observed_at = event.payload.timestamp
>             # 应用最新价格。
> ```
>
> > [accordion] Output: CryptoTwapPriceEvent
> >
> > **event: CryptoTwapPriceEvent**
> >
> > ```python CryptoTwapPriceEvent Union theme={null}
> > class RealtimePricePoint:
> >     timestamp: datetime
> >     value: Decimal
> >
> > class RealtimeTwapSnapshot:
> >     symbol: str
> >     data: tuple[RealtimePricePoint, ...]
> >     window_seconds: Literal[60]
> >
> > class RealtimeTwapUpdate:
> >     symbol: str
> >     timestamp: datetime
> >     value: Decimal
> >     window_seconds: Literal[60]
> >
> > class CryptoTwapPriceSnapshotEvent:
> >     topic: Literal["prices.crypto.twap"]
> >     type: Literal["subscribe"]
> >     timestamp: datetime
> >     seq: int | None
> >     dropped: int | None
> >     payload: RealtimeTwapSnapshot
> >
> > class CryptoTwapPriceUpdateEvent:
> >     topic: Literal["prices.crypto.twap"]
> >     type: Literal["update"]
> >     timestamp: datetime
> >     seq: int | None
> >     dropped: int | None
> >     payload: RealtimeTwapUpdate
> >
> > CryptoTwapPriceEvent = CryptoTwapPriceSnapshotEvent | CryptoTwapPriceUpdateEvent
> > ```
> >
> > ```json CryptoTwapPriceEvent Example theme={null}
> > {
> >   "timestamp": "2026-09-08T16:49:37Z",
> >   "seq": 3,
> >   "topic": "prices.crypto.twap",
> >   "type": "update",
> >   "payload": {
> >     "timestamp": "2026-09-08T16:49:37Z",
> >     "value": "78803.715261094101516288",
> >     "symbol": "btcusd",
> >     "window_seconds": 60
> >   }
> > }
> > ```
>
> `subscribe()` 等待服务端接受订阅。SDK 负责认证、心跳、重连，以及超过每连接 64 个过滤条件时的连接分配。创建订阅和迭代数据流时都可能出错。接受订阅超过 30 秒会失败。`seq` 仅在同一连接的同一频道内有效，重连后重置。
>
> 加密货币符号必须明确使用小写 USD 格式，例如 `btcusd`。`btc/usd`、`btcusdt` 和 `BTCUSD` 会触发 `UserInputError`。

### 迁移加密货币现货价格

> [tab] TypeScript
>
> 使用上方创建的已认证 `client`。将符号后缀从 `usdt` 改为 `usd`，例如将 `btcusdt` 改为 `btcusd`。移除斜杠分隔符，例如将 `btc/usd` 改为 `btcusd`。新主题要求显式提供小写 USD 符号。
>
> `prices.crypto` 主题默认使用 Chainlink 价格，因此从旧版 Chainlink 现货主题迁移会保留数据源。从 Binance 迁移则会同时改变数据源和计价货币，计价货币从 USDT 改为 USD。切换前，请确认新价格源满足你的定价需求。
>
> > [accordion] 迁移前：RTDS
> >
> > ```ts theme={null}
> > import { createPublicClient } from "@polymarket/client";
> >
> > const client = createPublicClient();
> > const stream = await client.subscribe([
> >   { topic: "prices.crypto.chainlink", symbols: ["btc/usd"] },
> >   { topic: "prices.crypto.binance", symbols: ["btcusdt"] },
> > ]);
> >
> > try {
> >   for await (const event of stream) {
> >     if (event.type === "update") {
> >       const price = event.payload.value;
> >     }
> >   }
> > } finally {
> >   await stream.close();
> > }
> > ```
>
> 替换为以下订阅：
>
> ```ts theme={null}
> const stream = await client.subscribe([
>   { topic: "prices.crypto", symbols: ["btcusd"] },
> ]);
> try {
>   for await (const event of stream) {
>     if (event.type === "subscribe") {
>       const history = event.payload.data; // 历史价格快照。
>     } else {
>       const price = event.payload.value;
>     }
>   }
> } finally {
>   await stream.close();
> }
> ```
>
> > [accordion] Output: CryptoPriceEvent
> >
> > **events: CryptoPriceEvent\[]**
> >
> > ```ts CryptoPriceEvent Union theme={null}
> > type CryptoPriceEvent =
> >   | {
> >       topic: "prices.crypto";
> >       type: "subscribe";
> >       timestamp: EpochMilliseconds;
> >       seq?: number;
> >       dropped?: number;
> >       payload: {
> >         symbol: string;
> >         data: { timestamp: EpochMilliseconds; value: DecimalString }[];
> >       };
> >     }
> >   | {
> >       topic: "prices.crypto";
> >       type: "update";
> >       timestamp: EpochMilliseconds;
> >       seq?: number;
> >       dropped?: number;
> >       payload: {
> >         symbol: string;
> >         timestamp: EpochMilliseconds;
> >         value: DecimalString;
> >         receivedAt: EpochMilliseconds | undefined;
> >         isCarriedForward: boolean | undefined;
> >       };
> >     };
> > ```
> >
> > ```json CryptoPriceEvent Example theme={null}
> > [
> >   {
> >     "topic": "prices.crypto",
> >     "type": "subscribe",
> >     "timestamp": 1788886176000,
> >     "seq": 1,
> >     "payload": {
> >       "symbol": "btcusd",
> >       "data": [
> >         {
> >           "timestamp": 1788886057000,
> >           "value": "78803.76173179"
> >         },
> >         {
> >           "timestamp": 1788886058000,
> >           "value": "78801.86287741"
> >         },
> >         {
> >           "timestamp": 1788886059000,
> >           "value": "78798.28703224"
> >         }
> >       ]
> >     }
> >   },
> >   {
> >     "topic": "prices.crypto",
> >     "type": "update",
> >     "timestamp": 1788886177000,
> >     "seq": 5,
> >     "payload": {
> >       "symbol": "btcusd",
> >       "timestamp": 1788886177000,
> >       "value": "78794.15450441"
> >     }
> >   }
> > ]
> > ```

> [tab] Python
>
> 使用上方创建的已认证 `client`，然后调用 `client.subscribe`。
>
> > [accordion] 迁移前：RTDS
> >
> > 旧版订阅通过 `AsyncPublicClient.subscribe` 或 `AsyncSecureClient.subscribe` 使用以下规格：
> >
> > ```python theme={null}
> > from polymarket.streams import CryptoPricesSpec
> >
> > specs = [
> >     CryptoPricesSpec(topic="prices.crypto.chainlink", symbols=["btc/usd"]),
> >     CryptoPricesSpec(topic="prices.crypto.binance", symbols=["btcusdt"]),
> > ]
> > ```
>
> 将 `CryptoPricesSpec` 替换为 `CryptoPriceSpec`，并明确选择 USD 价格。Binance 的 `btcusdt` 以 USDT 计价；`btcusd` 以 USD 计价且默认使用 Chainlink，因此从旧版 Chainlink 现货主题迁移会保留数据源，从 Binance 迁移则会改变数据源。请确认新价格源满足你的定价需求。
>
> 用以下订阅替换旧版调用：
>
> ```python theme={null}
> from polymarket.streams import CryptoPriceSpec
>
> async with await client.subscribe(
>     CryptoPriceSpec(symbols=["btcusd"])
> ) as stream:
>     async for event in stream:
>         # event: CryptoPriceEvent
>         if event.type == "subscribe":
>             history = event.payload.data  # 历史价格快照。
>         else:
>             price = event.payload.value
>             observed_at = event.payload.timestamp
> ```
>
> > [accordion] Output: CryptoPriceEvent
> >
> > **event: CryptoPriceEvent**
> >
> > ```python CryptoPriceEvent Union theme={null}
> > class RealtimePricePoint:
> >     timestamp: datetime
> >     value: Decimal
> >
> > class RealtimePriceSnapshot:
> >     symbol: str
> >     data: tuple[RealtimePricePoint, ...]
> >
> > class RealtimePriceUpdate:
> >     symbol: str
> >     timestamp: datetime
> >     value: Decimal
> >     received_at: datetime | None
> >     is_carried_forward: bool | None
> >
> > class CryptoPriceSnapshotEvent:
> >     topic: Literal["prices.crypto"]
> >     type: Literal["subscribe"]
> >     timestamp: datetime
> >     seq: int | None
> >     dropped: int | None
> >     payload: RealtimePriceSnapshot
> >
> > class CryptoPriceUpdateEvent:
> >     topic: Literal["prices.crypto"]
> >     type: Literal["update"]
> >     timestamp: datetime
> >     seq: int | None
> >     dropped: int | None
> >     payload: RealtimePriceUpdate
> >
> > CryptoPriceEvent = CryptoPriceSnapshotEvent | CryptoPriceUpdateEvent
> > ```
> >
> > ```json CryptoPriceEvent Example theme={null}
> > {
> >   "timestamp": "2026-09-08T16:49:37Z",
> >   "seq": 5,
> >   "topic": "prices.crypto",
> >   "type": "update",
> >   "payload": {
> >     "timestamp": "2026-09-08T16:49:37Z",
> >     "value": "78794.15450441",
> >     "symbol": "btcusd"
> >   }
> > }
> > ```
>
> `subscribe` 事件的 `payload.data` 是历史价格点元组。`update` 事件提供最新价格。`value` 为 `Decimal`，时间戳均为 UTC `datetime`。
>
> 明确指定小写 USD 符号，例如 `btcusd`。如只需要实时价格，可跳过 `type == "subscribe"` 的事件。

### 迁移股票价格

> [tab] TypeScript
>
> 使用上方创建的已认证 `client`。更改主题时保留 `symbol` 和 `types`。
>
> > [accordion] 迁移前：RTDS
> >
> > ```ts theme={null}
> > import { createPublicClient } from "@polymarket/client";
> >
> > const client = createPublicClient();
> > const stream = await client.subscribe([
> >   { topic: "prices.equity.pyth", symbol: "aapl", types: ["update"] },
> > ]);
> >
> > try {
> >   for await (const event of stream) {
> >     if (event.type === "update") {
> >       const price = event.payload.value;
> >     }
> >   }
> > } finally {
> >   await stream.close();
> > }
> > ```
>
> 替换为以下订阅：
>
> ```ts theme={null}
> const stream = await client.subscribe([
>   { topic: "prices.equity", symbol: "aapl", types: ["update"] },
> ]);
> try {
>   for await (const event of stream) {
>     if (event.type === "update") {
>       const price = event.payload.value;
>     }
>   }
> } finally {
>   await stream.close();
> }
> ```
>
> > [accordion] Output: EquityPriceEvent
> >
> > **events: EquityPriceEvent\[]**
> >
> > ```ts EquityPriceEvent Union theme={null}
> > type EquityPriceEvent =
> >   | {
> >       topic: "prices.equity";
> >       type: "subscribe";
> >       timestamp: EpochMilliseconds;
> >       seq?: number;
> >       dropped?: number;
> >       payload: {
> >         symbol: string;
> >         data: { timestamp: EpochMilliseconds; value: DecimalString }[];
> >       };
> >     }
> >   | {
> >       topic: "prices.equity";
> >       type: "update";
> >       timestamp: EpochMilliseconds;
> >       seq?: number;
> >       dropped?: number;
> >       payload: {
> >         symbol: string;
> >         timestamp: EpochMilliseconds;
> >         value: DecimalString;
> >         receivedAt: EpochMilliseconds | undefined;
> >         isCarriedForward: boolean | undefined;
> >       };
> >     };
> > ```
> >
> > ```json EquityPriceEvent Example theme={null}
> > [
> >   {
> >     "topic": "prices.equity",
> >     "type": "subscribe",
> >     "timestamp": 1788886176400,
> >     "seq": 1,
> >     "payload": {
> >       "symbol": "aapl",
> >       "data": [
> >         {
> >           "timestamp": 1788886056800,
> >           "value": "316.11"
> >         },
> >         {
> >           "timestamp": 1788886057000,
> >           "value": "316.11"
> >         },
> >         {
> >           "timestamp": 1788886057200,
> >           "value": "316.11001"
> >         }
> >       ]
> >     }
> >   },
> >   {
> >     "topic": "prices.equity",
> >     "type": "update",
> >     "timestamp": 1788886176600,
> >     "seq": 2,
> >     "payload": {
> >       "symbol": "aapl",
> >       "timestamp": 1788886176600,
> >       "value": "316.1",
> >       "receivedAt": 1788886176600
> >     }
> >   }
> > ]
> > ```
>
> `types: ["update"]` 仅接收实时更新。省略 `types` 即可同时接收历史快照。

> [tab] Python
>
> 使用上方创建的已认证 `client`，然后调用 `client.subscribe`。
>
> > [accordion] 迁移前：RTDS
> >
> > 旧版订阅通过 `AsyncPublicClient.subscribe` 或 `AsyncSecureClient.subscribe` 使用以下规格：
> >
> > ```python theme={null}
> > from polymarket.streams import EquityPricesSpec
> >
> > spec = EquityPricesSpec(symbol="AAPL", types=["update"])
> > ```
>
> 将 `EquityPricesSpec` 替换为 `EquityPriceSpec`，保留 `symbol` 和 `types`。符号会去除首尾空格并转换为小写。`types=["update"]` 只接收实时更新。省略 `types` 可同时接收历史快照。
>
> 用以下订阅替换旧版调用：
>
> ```python theme={null}
> from polymarket.streams import EquityPriceSpec
>
> async with await client.subscribe(
>     EquityPriceSpec(symbol="aapl", types=["update"])
> ) as stream:
>     async for event in stream:
>         # event: EquityPriceEvent
>         if event.type == "update":
>             price = event.payload.value
>             observed_at = event.payload.timestamp
> ```
>
> > [accordion] Output: EquityPriceEvent
> >
> > **event: EquityPriceEvent**
> >
> > ```python EquityPriceEvent Union theme={null}
> > class RealtimePricePoint:
> >     timestamp: datetime
> >     value: Decimal
> >
> > class RealtimePriceSnapshot:
> >     symbol: str
> >     data: tuple[RealtimePricePoint, ...]
> >
> > class RealtimePriceUpdate:
> >     symbol: str
> >     timestamp: datetime
> >     value: Decimal
> >     received_at: datetime | None
> >     is_carried_forward: bool | None
> >
> > class EquityPriceSnapshotEvent:
> >     topic: Literal["prices.equity"]
> >     type: Literal["subscribe"]
> >     timestamp: datetime
> >     seq: int | None
> >     dropped: int | None
> >     payload: RealtimePriceSnapshot
> >
> > class EquityPriceUpdateEvent:
> >     topic: Literal["prices.equity"]
> >     type: Literal["update"]
> >     timestamp: datetime
> >     seq: int | None
> >     dropped: int | None
> >     payload: RealtimePriceUpdate
> >
> > EquityPriceEvent = EquityPriceSnapshotEvent | EquityPriceUpdateEvent
> > ```
> >
> > ```json EquityPriceEvent Example theme={null}
> > {
> >   "timestamp": "2026-09-08T16:49:36.600000Z",
> >   "seq": 2,
> >   "topic": "prices.equity",
> >   "type": "update",
> >   "payload": {
> >     "timestamp": "2026-09-08T16:49:36.600000Z",
> >     "value": "316.1",
> >     "symbol": "aapl",
> >     "received_at": "2026-09-08T16:49:36.600000Z"
> >   }
> > }
> > ```
>
> `subscribe` 事件的 `payload.data` 是历史价格点元组。`update` 事件提供最新价格。`value` 为 `Decimal`，时间戳均为 UTC `datetime`。
>
> 更新可能附带 `received_at` 与 `is_carried_forward`。


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
