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
source_url: 'https://docs.polymarket.com/cn/market-data/public-analytics'
updated_at: 2026-11-13
---

# 分析

> 了解 Polymarket 上的活动与表现。

使用这些读取操作，了解交易活动集中在哪些市场，以及交易者和集成应用随时间推移的表现。

## 市场活动

以下示例假设你已经有一个市场对象。要查找或获取市场，请参阅
[**发现市场**](https://docs.polymarket.com/cn/market-data/discover-markets.md)。

> [tab] TypeScript
>
> 给定一个市场，读取其条件 ID 和事件 ID：
>
> ```ts theme={null}
> const conditionId = market.conditionId;
> const eventId = market.events[0].id;
> ```

> [tab] Python
>
> 给定一个市场，读取其条件 ID 和事件 ID：
>
> ```python theme={null}
> condition_id = market.condition_id
> event_id = market.events[0].id
> ```

> [tab] API
>
> 给定一个市场对象，可以从以下字段获取其条件 ID 和事件 ID：
>
> ```json theme={null}
> {
>   "conditionId": "<condition_id>",
>   "events": [{ "id": "<event_id>" }]
> }
> ```
>
> 为下方请求设置这些标识符：
>
> ```bash theme={null}
> CONDITION_ID="<condition_id>"
> EVENT_ID="<event_id>"
> ```

### 最近成交

查看市场中最近撮合的成交，包括方向、价格、数量、结果、钱包和时间戳。
成交始终按时间戳降序返回（最新的在前）。

> [tab] TypeScript
>
> 在 `PublicClient` 或 `SecureClient` 上调用 `listTrades()`。
>
> ```ts theme={null}
> const pages = client.listTrades({ conditionId: [conditionId], pageSize: 1 });
>
> for await (const page of pages) {
>   // page.items: Trade[]
> }
> ```
>
> > [accordion] 输出：Trade\[]
> >
> > ```ts Trade Type theme={null}
> > type Trade = {
> >   wallet: EvmAddress;
> >   side: OrderSide;
> >   assetId: TokenId | PositionId;
> >   conditionId: ConditionId;
> >   size: DecimalString;
> >   price: DecimalString;
> >   timestamp: EpochMilliseconds;
> >   transactionHash: TxHash;
> >   title?: string;
> >   slug?: string;
> >   icon?: string;
> >   eventSlug?: string;
> >   outcome?: string;
> >   outcomeIndex?: number;
> >   name?: string;
> >   pseudonym?: string;
> >   bio?: string;
> >   profileImage?: string;
> >   profileImageOptimized?: string;
> > };
> > ```
> >
> > ```json Trade Example theme={null}
> > [
> >   {
> >     "side": "SELL",
> >     "conditionId": "0x747dc809fb79e1b05be09c42d6179459a58de2ef3e40f02484a4e1260f741f75",
> >     "size": "42.62",
> >     "price": "0.91",
> >     "timestamp": 1782752879000,
> >     "title": "Will the US confirm that aliens exist before 2027?",
> >     "outcome": "No",
> >     "wallet": "0x50a0cebecfb81dbcbfa6d38f82040343f1e3d95f",
> >     "assetId": "7305630249804085635496399869905769372294302716159034447326228509068694952392",
> >     "transactionHash": "0x4f3d2c1b0a9876543210fedcba9876543210fedcba9876543210fedcba987654"
> >   }
> > ]
> > ```

> [tab] Python
>
> 在已创建的 `AsyncPublicClient` 或 `AsyncSecureClient` 上调用 `list_trades()`。
>
> ```python theme={null}
> pages = client.list_trades(condition_id=[condition_id], page_size=1)
>
> async for page in pages:
>     # page.items: tuple[Trade, ...]
>     pass
> ```
>
> > [accordion] Output: Trade
> >
> > ```python Trade Type theme={null}
> > class Trade:
> >     wallet: EvmAddress
> >     asset_id: ClobAssetId
> >     condition_id: ConditionId
> >     side: OrderSide
> >     size: Decimal
> >     price: Decimal
> >     timestamp: datetime
> >     transaction_hash: TransactionHash
> >     title: str | None
> >     slug: str | None
> >     icon: str | None
> >     event_slug: str | None
> >     outcome: str | None
> >     outcome_index: int | None
> >     name: str | None
> >     pseudonym: str | None
> >     bio: str | None
> >     profile_image: str | None
> >     profile_image_optimized: str | None
> > ```
> >
> > ```json Trade Example theme={null}
> > {
> >   "wallet": "0x84cfffc3f16dcc353094de30d4a45226eccd2f63",
> >   "asset_id": "100621704916396384184205224105871827982844371725320616822883322969092312254616",
> >   "condition_id": "0xc8a2f17f42fa8493ebae503abec9d51efa7b57c3cc59a7b88933bffaa3618387",
> >   "side": "BUY",
> >   "size": "78.55",
> >   "price": "0.62",
> >   "timestamp": "2026-09-08T17:03:34Z",
> >   "transaction_hash": "0x8b2fd0c7480cd78bd9f57e8b935cf10c6635d2c479c66ea26d358e1425f44a95",
> >   "title": "Will Real Madrid CF win on 2026-09-08?",
> >   "slug": "ucl-rma-int-2026-09-08-rma",
> >   "icon": "https://polymarket-upload.s3.us-east-2.amazonaws.com/champions-league-pic-QIUFsL8vaDdq.png",
> >   "event_slug": null,
> >   "outcome": "Yes",
> >   "outcome_index": null,
> >   "name": "mooseborzoi",
> >   "pseudonym": "Agitated-Bricklaying",
> >   "bio": null,
> >   "profile_image": "https://polymarket-upload.s3.us-east-2.amazonaws.com/profile-image-7634413-4dea3150-84ad-4278-9e45-d96e51769b7e.png",
> >   "profile_image_optimized": null
> > }
> > ```
>
> `size` 的单位为份额，`price` 的单位为每份额 USDC。读取钱包的完整交易历史时，传入 `user=address, full_history=True`。`full_history` 不能与 `start` 或 `end` 同时使用。

> [tab] API
>
> 列出某个市场的最近成交：
>
> ```bash theme={null}
> curl "https://data-api.polymarket.com/v2/trades?condition=$CONDITION_ID&limit=1"
> ```
>
> 响应包含最近成交（为简洁起见省略了部分行字段）：
>
> > [accordion] 响应
> >
> > ```json theme={null}
> > {
> >   "data": [
> >     {
> >       "proxy_wallet": "0xc6a5ceb4083f9209c31c45dc86f5714583f552e3",
> >       "side": "SELL",
> >       "token_id": "7305630249804085635496399869905769372294302716159034447326228509068694952392",
> >       "condition_id": "0x747dc809fb79e1b05be09c42d6179459a58de2ef3e40f02484a4e1260f741f75",
> >       "size": 6.96,
> >       "price": 0.962,
> >       "timestamp": 1788204232,
> >       "transaction_hash": "0x6929c40832394d64d84a0a9170c4174f9d9f18de23f82de05a750fdbf7350ca9",
> >       "title": "Will the US confirm that aliens exist before 2027?",
> >       "outcome": "No"
> >     }
> >   ],
> >   "pagination": {
> >     "limit": 1,
> >     "offset": 0,
> >     "has_more": true,
> >     "next_cursor": "eyJkYXRhIjp7InR5cGUiOiJ0cmFkZXMi…"
> >   }
> > }
> > ```

### 未平仓量

衡量一个或多个市场当前未平仓头寸中持有的价值。

> [tab] TypeScript
>
> 在 `PublicClient` 或 `SecureClient` 上调用 `fetchOpenInterest()`。最多可传
> 20 个条件 ID；省略 `conditionIds` 时返回全局的单一数值（以
> `conditionId: null` 表示）。
>
> ```ts theme={null}
> const openInterest = await client.fetchOpenInterest({
>   conditionIds: [conditionId],
> });
>
> // openInterest: OpenInterest[]
> ```
>
> > [accordion] 输出：OpenInterest\[]
> >
> > ```ts OpenInterest Type theme={null}
> > type OpenInterest = {
> >   conditionId: ConditionId | null;
> >   value: DecimalString;
> > };
> > ```
> >
> > ```json OpenInterest Example theme={null}
> > [
> >   {
> >     "conditionId": "0x747dc809fb79e1b05be09c42d6179459a58de2ef3e40f02484a4e1260f741f75",
> >     "value": "7484304.679057"
> >   }
> > ]
> > ```

> [tab] Python
>
> 在已创建的 `AsyncPublicClient` 或 `AsyncSecureClient` 上调用 `get_open_interests()`。
>
> ```python theme={null}
> open_interest = await client.get_open_interests()
>
> # open_interest: tuple[OpenInterest, ...]
> ```
>
> > [accordion] Output: OpenInterest
> >
> > ```python OpenInterest Type theme={null}
> > class OpenInterest:
> >     condition_id: ConditionId | None
> >     value: Decimal
> > ```
> >
> > ```json OpenInterest Example theme={null}
> > {
> >   "condition_id": null,
> >   "value": "356037494.1056115"
> > }
> > ```
>
> 结果为 `OpenInterest` 元组。全局未平仓量的 `condition_id` 为 `None`。传入 `condition_ids=[condition_id]` 可读取单个市场的未平仓量。数值单位为 USDC。

> [tab] API
>
> 获取某个市场的未平仓量：
>
> ```bash theme={null}
> curl "https://data-api.polymarket.com/v2/oi?condition=$CONDITION_ID"
> ```
>
> 响应包含按市场划分的未平仓量：
>
> > [accordion] 响应
> >
> > ```json theme={null}
> > {
> >   "data": [
> >     {
> >       "condition_id": "0x747dc809fb79e1b05be09c42d6179459a58de2ef3e40f02484a4e1260f741f75",
> >       "value": 7113116.142022
> >     }
> >   ]
> > }
> > ```

### 市场持仓者

查找市场中每个结果的最大公开持仓者。

> [tab] TypeScript
>
> 在 `PublicClient` 或 `SecureClient` 上调用 `listMarketHolders()` 并按游标翻页。
> `pageSize` 分别作用于每个结果代币，因此跨页时请按 `assetId` 合并分组。设置
> `includePnl: true`（限一个条件 ID、页大小至多 100）可为每个持仓者行附加持仓经济数据。
>
> ```ts theme={null}
> const pages = client.listMarketHolders({
>   conditionIds: [conditionId],
>   pageSize: 1,
> });
>
> for await (const page of pages) {
>   // page.items: MetaHolder[]
> }
> ```
>
> > [accordion] 输出：MetaHolder\[]
> >
> > ```ts MetaHolder Type theme={null}
> > type Holder = {
> >   wallet: EvmAddress;
> >   assetId: TokenId | PositionId;
> >   /** Net holding in shares; per-side gross when `includePnl` is set. */
> >   amount: DecimalString;
> >   outcomeIndex: number | null;
> >   verified: boolean;
> >   name: string | null;
> >   pseudonym: string | null;
> >   bio: string | null;
> >   displayUsernamePublic: boolean;
> >   profileImage: string | null;
> >   profileImageOptimized: string | null;
> >   avgPrice?: DecimalString | null;
> >   entryCostUsdc?: DecimalString | null;
> >   currentPrice?: DecimalString | null;
> >   currentValue?: DecimalString | null;
> >   realizedPnl?: DecimalString | null;
> >   unrealizedPnl?: DecimalString | null;
> >   totalPnl?: DecimalString | null;
> > };
> >
> > type MetaHolder = {
> >   assetId: TokenId | PositionId;
> >   /** Holders for this outcome, ordered by amount descending. */
> >   holders: Holder[];
> > };
> > ```
> >
> > ```json MetaHolder Example theme={null}
> > [
> >   {
> >     "assetId": "92338023949892178944669766466918011858071833335063600591564160751176113496073",
> >     "holders": [
> >       {
> >         "wallet": "0x1b5ca5e84705cd14ca9953b57434094cac726c0f",
> >         "amount": "1878.77239",
> >         "outcomeIndex": 0,
> >         "verified": false,
> >         "name": null
> >       }
> >     ]
> >   }
> > ]
> > ```

> [tab] Python
>
> 在已创建的 `AsyncPublicClient` 或 `AsyncSecureClient` 上调用 `list_market_holders()`。
>
> ```python theme={null}
> pages = client.list_market_holders(condition_ids=[condition_id], page_size=1)
>
> async for page in pages:
>     # page.items: tuple[MetaHolder, ...]
>     pass
> ```
>
> `page_size` 分别应用于每个结果资产。跨页时按 `asset_id` 合并分组。设置 `include_pnl=True` 可读取单个条件的仓位经济数据，此时每页最多 100 条。
>
> > [accordion] Output: MetaHolder
> >
> > ```python Holder Type theme={null}
> > class Holder:
> >     wallet: EvmAddress
> >     asset_id: ClobAssetId
> >     amount: Decimal
> >     outcome_index: int | None
> >     display_username_public: bool
> >     verified: bool
> >     name: str | None
> >     pseudonym: str | None
> >     bio: str | None
> >     profile_image: str | None
> >     profile_image_optimized: str | None
> >     avg_price: Decimal | None
> >     entry_cost_usdc: Decimal | None
> >     current_price: Decimal | None
> >     current_value: Decimal | None
> >     realized_pnl: Decimal | None
> >     unrealized_pnl: Decimal | None
> >     total_pnl: Decimal | None
> > ```
> >
> > ```python MetaHolder Type theme={null}
> > class MetaHolder:
> >     asset_id: ClobAssetId
> >     holders: tuple[Holder, ...]
> > ```
> >
> > ```json MetaHolder Example theme={null}
> > {
> >   "asset_id": "92338023949892178944669766466918011858071833335063600591564160751176113496073",
> >   "holders": [
> >     {
> >       "wallet": "0x1b5ca5e84705cd14ca9953b57434094cac726c0f",
> >       "asset_id": "92338023949892178944669766466918011858071833335063600591564160751176113496073",
> >       "amount": "1878.77239",
> >       "outcome_index": 0,
> >       "display_username_public": false,
> >       "verified": false,
> >       "name": null,
> >       "pseudonym": null,
> >       "bio": null,
> >       "profile_image": null,
> >       "profile_image_optimized": null,
> >       "avg_price": "0.2794",
> >       "entry_cost_usdc": "524.991",
> >       "current_price": "1.0",
> >       "current_value": "1878.7723",
> >       "realized_pnl": "0.0001",
> >       "unrealized_pnl": "1353.7812",
> >       "total_pnl": "1353.7813"
> >     }
> >   ]
> > }
> > ```

> [tab] API
>
> 列出某个市场的最大持仓者：
>
> ```bash theme={null}
> curl "https://data-api.polymarket.com/v2/holders?condition=$CONDITION_ID&limit=1"
> ```
>
> 响应按结果对持仓者分组（为简洁起见省略了部分持仓者字段）：
>
> > [accordion] 响应
> >
> > ```json theme={null}
> > {
> >   "data": [
> >     {
> >       "token_id": "107505882767731489358349912513945399560393482969656700824895970500493757150417",
> >       "holders": [
> >         {
> >           "proxy_wallet": "0xcd09c7f5132a160b41578a79a9e3453da7aeda63",
> >           "amount": 550253.927993,
> >           "outcome_index": 0,
> >           "name": "ShayaEredyon"
> >         }
> >       ]
> >     },
> >     {
> >       "token_id": "7305630249804085635496399869905769372294302716159034447326228509068694952392",
> >       "holders": [
> >         {
> >           "proxy_wallet": "0xa2cd4ccda9a1f95949df7a3355c4c2daa0642ba0",
> >           "amount": 1455975.51944,
> >           "outcome_index": 1,
> >           "name": "0xA2cd4CcdA9A1f95949DF7A3355C4c2DAa0642Ba0-1729178570395"
> >         }
> >       ]
> >     }
> >   ],
> >   "pagination": {
> >     "limit": 1,
> >     "offset": 0,
> >     "has_more": true,
> >     "next_cursor": "eyJkYXRhIjp7InR5cGUiOiJob2xkZXJzIi…"
> >   }
> > }
> > ```

### 事件实时交易量

汇总一个事件的整体活动，并按市场细分交易量。

> [tab] TypeScript
>
> 在 `PublicClient` 或 `SecureClient` 上调用 `fetchEventLiveVolume()`。可传入
> 一个或多个事件 ID；传入列表时跨事件汇总，返回单个结果。
>
> ```ts theme={null}
> const liveVolume = await client.fetchEventLiveVolume({
>   eventIds: [eventId],
> });
>
> // liveVolume: LiveVolume
> ```
>
> > [accordion] 输出：LiveVolume
> >
> > ```ts LiveVolume Type theme={null}
> > type MarketLiveVolume = {
> >   /** Condition ID of the market, or `null` when the source row is unidentified. */
> >   conditionId: ConditionId | null;
> >   /** Cumulative one-side taker volume in shares. */
> >   takerVolume: DecimalString;
> > };
> >
> > type LiveVolume = {
> >   /** Sum of every returned market's taker volume, in shares. */
> >   takerVolumeTotal: DecimalString;
> >   /** Markets ordered by taker volume descending. */
> >   markets: MarketLiveVolume[];
> > };
> > ```
> >
> > ```json LiveVolume Example theme={null}
> > {
> >   "takerVolumeTotal": "698627.625937",
> >   "markets": [
> >     {
> >       "conditionId": "0x435620fa180dbedb59d34f164d82a447304436b57e87850ca3d1ab2070667006",
> >       "takerVolume": "631069.486412"
> >     },
> >     {
> >       "conditionId": "0xce67b495c754cd29548e0381d18e9b4701446fa9e32c29d7eec3e7e72ad55152",
> >       "takerVolume": "67558.139525"
> >     }
> >   ]
> > }
> > ```

> [tab] Python
>
> 在已创建的 `AsyncPublicClient` 或 `AsyncSecureClient` 上调用 `get_event_live_volume()`。
>
> ```python theme={null}
> live_volume = await client.get_event_live_volume(event_ids=[int(event_id)])
>
> # live_volume: LiveVolume
> ```
>
> > [accordion] Output: LiveVolume
> >
> > ```python MarketLiveVolume Type theme={null}
> > class MarketLiveVolume:
> >     condition_id: ConditionId | None
> >     taker_volume: Decimal
> > ```
> >
> > ```python LiveVolume Type theme={null}
> > class LiveVolume:
> >     taker_volume_total: Decimal
> >     markets: tuple[MarketLiveVolume, ...]
> > ```
> >
> > ```json LiveVolume Example theme={null}
> > {
> >   "taker_volume_total": "4439931.266595",
> >   "markets": [
> >     {
> >       "condition_id": "0xe7f239d76b59c4e614f0bdb80467026da833083e38a31a27fde8e0907417ea12",
> >       "taker_volume": "1057493.399838"
> >     },
> >     {
> >       "condition_id": "0x4d162a40c3e3f458b0e0017485d7f9e6ead0cdd0573e38b26e0d5420525ccfa4",
> >       "taker_volume": "780331.374022"
> >     },
> >     {
> >       "condition_id": "0xc8929e80e74ae959b3ed9b9e1c5e0903ad38e02e1339462e3acf8b49bbca35a9",
> >       "taker_volume": "588112.023677"
> >     },
> >     {
> >       "condition_id": "0x02507350fc2b81c3af36c659a805adbda9b0a81e63a27b29cb273cdd7dbc072e",
> >       "taker_volume": "576353.148052"
> >     },
> >     {
> >       "condition_id": "0x626d0441b078eefbe2c49047960e7a3b6b4512c235507a2528ccc0f95f2474a6",
> >       "taker_volume": "507319.025175"
> >     },
> >     {
> >       "condition_id": "0xb4022c0b2718eca7ad27195f2d48f06527fa000269d188e1d3001ff8bbc16956",
> >       "taker_volume": "479549.81298"
> >     },
> >     {
> >       "condition_id": "0xc60022fe066abd6f96c375adb09f38d92c4931f09c10b805354581b4e5465e93",
> >       "taker_volume": "313649.055908"
> >     },
> >     {
> >       "condition_id": "0x4092815fea8f91e60586882d45fa2f61bfca8a36d595f47fdea9eec5d2893025",
> >       "taker_volume": "137123.426943"
> >     }
> >   ]
> > }
> > ```
>
> 传入一个或多个整数事件 ID，可获得合并结果。`taker_volume_total` 表示以份额计的吃单总成交量。`markets` 包含各市场的明细。

> [tab] API
>
> 获取某个事件的实时交易量：
>
> ```bash theme={null}
> curl "https://data-api.polymarket.com/v2/live-volume?event_id=$EVENT_ID"
> ```
>
> 响应包含事件的 taker 总成交量及其市场明细（为简洁起见，已省略其余行）：
>
> > [accordion] 响应
> >
> > ```json theme={null}
> > {
> >   "data": {
> >     "taker_volume_total": 65834357.807271,
> >     "conditions": [
> >       {
> >         "condition_id": "0x747dc809fb79e1b05be09c42d6179459a58de2ef3e40f02484a4e1260f741f75",
> >         "taker_volume": 37828643.727694
> >       },
> >       {
> >         "condition_id": "0xa7962b12241616d83dcb8c70fc33aa0f48b1ec46a3ad6a23db21d3885dedc4cb",
> >         "taker_volume": 11161362.976257
> >       }
> >     ]
> >   }
> > }
> > ```
>
> 市场按 taker 成交量排序，最大的市场排在最前。

### 市场结算

查看市场的结算进度。

> [tab] TypeScript
>
> 在已有的 `PublicClient` 或 `SecureClient` 上调用 `fetchResolutions()`。如尚未创建客户端，请先[创建公共客户端](https://docs.polymarket.com/cn/getting-started/typescript.md)。
>
> ```ts theme={null}
> const resolutions = await client.fetchResolutions({
>   conditionIds: [conditionId],
> });
>
> for (const resolution of resolutions) {
>   console.log(
>     resolution.status,
>     resolution.transactionHash,
>     resolution.logIndex,
>   );
> }
>
> // resolutions: Resolution[]
> ```
>
> 每条记录包含 `status` 和 `lastUpdatedAt`，公布派彩后还会包含 `payouts`。没有匹配的结算记录时返回空数组。
>
> 对 UMA 问题生命周期记录，`transactionHash` 指向最近一次生命周期事件的交易，而 `logIndex` 是最初 `RequestPrice` 事件的日志索引。两者可能属于不同的交易，不要将其组合为日志定位信息。
>
> 此规则不适用于所有记录：V2 仅按条件提供的记录可能将两者都返回为 `null`。CTF 条件结算回退记录中的交易与日志索引则共同指向对应的条件结算事件。
>
> `Resolution` 使用以下可选字段提供结算时间预估：
>
> | 字段 | 类型 |
> | - | - |
> | `expectedSettlementTime` | `IsoDateTimeString` 或 `undefined` |
> | `settlementTimeBasis` | `ResolutionSettlementTimeBasis` 或 `undefined` |
>
> `expectedSettlementTime` 是 UTC 的 ISO 日期时间字符串。没有可用预估时，这两个字段会省略。从 `@polymarket/client` 导入 `ResolutionSettlementTimeBasis`，即可判断预估依据：
>
> | 枚举成员 | 预估时间 |
> | - | - |
> | `ManagedProposalExpiration` | 托管 UMA 提案的质疑窗口结束时间 |
> | `ProposalExpiration` | 普通 UMA 提案的质疑窗口结束时间 |
> | `DvmRoundEstimate` | 该争议最早可结算的 UMA 投票轮次结束时间 |
> | `Liveness` | 提案时间加上 Polymarket v2 预言机的存活窗口 |

> [tab] Python
>
> 在已创建的 `AsyncPublicClient` 或 `AsyncSecureClient` 上调用 `get_resolutions()`。
> 如尚未创建客户端，请先[创建公共客户端](https://docs.polymarket.com/cn/getting-started/python.md)。
>
> ```python theme={null}
> resolutions = await client.get_resolutions(condition_ids=[condition_id])
>
> for resolution in resolutions:
>     print(resolution.status, resolution.transaction_hash, resolution.log_index)
>
> # resolutions: tuple[Resolution, ...]
> ```
>
> 每行包含 `status` 和 `last_updated_at`。如果已公布赔付，`payouts` 包含对应数值。没有匹配的结算记录时返回空元组。
>
> 对 UMA 问题生命周期记录，`transaction_hash` 指向最近一次生命周期事件的交易，而 `log_index` 是最初 `RequestPrice` 事件的日志索引。两者可能属于不同的交易，不要将其组合为日志定位信息。
>
> 此规则不适用于所有记录：V2 仅按条件提供的记录可能将两者都返回为 `None`。CTF 条件结算回退记录中的交易与日志索引则共同指向对应的条件结算事件。
>
> `Resolution` 使用以下字段提供结算时间预估：
>
> | 字段 | 类型 |
> | - | - |
> | `expected_settlement_time` | `datetime` 或 `None` |
> | `settlement_time_basis` | `ResolutionSettlementTimeBasis` 或 `None` |
>
> `expected_settlement_time` 是带时区的 UTC `datetime`。没有可用预估时，这两个字段为 `None`。从 `polymarket` 导入 `ResolutionSettlementTimeBasis`，即可判断预估依据：
>
> | 枚举成员 | 预估时间 |
> | - | - |
> | `MANAGED_PROPOSAL_EXPIRATION` | 托管 UMA 提案的质疑窗口结束时间 |
> | `PROPOSAL_EXPIRATION` | 普通 UMA 提案的质疑窗口结束时间 |
> | `DVM_ROUND_ESTIMATE` | 该争议最早可结算的 UMA 投票轮次结束时间 |
> | `LIVENESS` | 提案时间加上 Polymarket v2 预言机的存活窗口 |

> [tab] API
>
> 获取市场的结算进度：
>
> ```bash theme={null}
> curl "https://data-api.polymarket.com/v2/resolutions?condition=$CONDITION_ID"
> ```
>
> 以下为示例响应，省略了部分字段：
>
> > [accordion] 响应：结算记录
> >
> > ```json theme={null}
> > {
> >   "data": [
> >     {
> >       "condition_id": "0x02507350fc2b81c3af36c659a805adbda9b0a81e63a27b29cb273cdd7dbc072e",
> >       "status": "resolved",
> >       "transaction_hash": "0x1fc7a1df48dcac15859af515ebd77183c3487591181469a60dbf115b705f005a",
> >       "log_index": "170",
> >       "last_update_timestamp": "1785355919"
> >     }
> >   ]
> > }
> > ```
>
> `data` 包含带有 `status` 和 `last_update_timestamp` 的结算记录。没有匹配记录时为空列表。市场等待预言机结果期间，记录还可能带有下文所述的结算时间预估字段。
>
> 对 UMA 问题生命周期记录，`transaction_hash` 指向最近一次生命周期事件的交易，而 `log_index` 是最初 `RequestPrice` 事件的日志索引（数字字符串）。两者可能属于不同的交易，不要将其组合为日志定位信息。
>
> V2 仅按条件提供的记录可能为两者返回空字符串，表示无可用来源信息。CTF 条件结算回退记录则返回共同指向条件结算事件的交易与日志索引。
>
> 等待预言机结果的记录可能带有 `expected_settlement_time`（RFC3339 UTC）和 `settlement_time_basis`。凡是没有可用预估的情况，包括已结算的市场和处于延长审核中的提案，这两个字段都会省略。
>
> | `settlement_time_basis` | 记录状态 | `expected_settlement_time` |
> | - | - | - |
> | `managed_proposal_expiration` | 托管预言机上的 UMA 提案，仍处于质疑窗口内 | 质疑窗口结束时间 |
> | `proposal_expiration` | 普通预言机上的 UMA 提案，仍处于质疑窗口内 | 质疑窗口结束时间 |
> | `dvm_round_estimate` | 处于争议中的 UMA 提案 | 该争议最早可结算的 UMA 投票轮次结束时间 |
> | `liveness` | Polymarket v2 预言机上的提案 | 提案时间加上其存活窗口 |

#### 结算时间预估

请把预估值理解为市场最早可能结算的时间，而不是截止时间。争议投票可能顺延到下一轮；提案等待最终确认时，其存活窗口也可能已经结束。

已结算的市场、处于延长审核中的提案，以及仍处于初始化或活跃状态的市场，都没有可用的结算时间预估。

### 代币查询

查询代币所属的市场与结果，或一次列出某个条件下的全部代币。

> [tab] TypeScript
>
> 在已有的 `PublicClient` 或 `SecureClient` 上调用 `fetchTokenReferences()`。如尚未创建客户端，请先[创建公共客户端](https://docs.polymarket.com/cn/getting-started/typescript.md)。
>
> ```ts theme={null}
> const assetId =
>   "107505882767731489358349912513945399560393482969656700824895970500493757150417";
> const references = await client.fetchTokenReferences({ assetIds: [assetId] });
>
> for (const reference of references) {
>   console.log(reference.assetId, reference.outcome, reference.outcomeIndex);
> }
>
> // references: TokenReference[]
> ```
>
> > [accordion] 输出：TokenReference\[]
> >
> > ```ts TokenReference Type theme={null}
> > type TokenReference = {
> >   assetId: ClobAssetId;
> >   conditionId: ConditionId;
> >   structuralConditionId: ConditionId | null;
> >   module: TokenModule;
> >   outcomeIndex: number;
> >   clobIndex: number | null;
> >   outcome: string | null;
> >   oppositeAssetId: ClobAssetId | null;
> >   resolved: boolean;
> >   finalPrice: DecimalString | null;
> >   title: string | null;
> >   marketSlug: string | null;
> >   closed: boolean | null;
> >   negRisk: boolean | null;
> >   negRiskMarketId: ConditionId | null;
> >   questionIndex: number | null;
> >   eventId: EventId | null;
> >   eventSlug: string | null;
> > };
> > ```
>
> `finalPrice` 是结算派彩的十进制字符串，不可用时为 `null`。结算数据可能延迟最多一分钟。
>
> 按条件查询时，改为只传 `conditionIds`：
>
> ```ts theme={null}
> const references = await client.fetchTokenReferences({
>   conditionIds: [conditionId],
> });
> ```
>
> 每次传入最多 50 个 `assetIds` 或 10 个 `conditionIds`，不要同时传入两者。结果不分页，未知的资产 ID 会被省略。

> [tab] Python
>
> 在已有的 `AsyncPublicClient` 或 `AsyncSecureClient` 上调用 `get_token_references()`。如尚未创建客户端，请先[创建公共客户端](https://docs.polymarket.com/cn/getting-started/python.md)。同步客户端也提供相同方法。
>
> ```python theme={null}
> asset_id = "107505882767731489358349912513945399560393482969656700824895970500493757150417"
> references = await client.get_token_references(asset_ids=[asset_id])
>
> for reference in references:
>     print(reference.asset_id, reference.outcome, reference.outcome_index)
>
> # references: tuple[TokenReference, ...]
> ```
>
> > [accordion] 输出：TokenReference
> >
> > ```python TokenReference Type theme={null}
> > class TokenReference(BaseModel):
> >     asset_id: ClobAssetId
> >     condition_id: ConditionId
> >     structural_condition_id: ConditionId | None
> >     module: TokenModule
> >     outcome_index: int
> >     clob_index: int | None
> >     outcome: str | None
> >     opposite_asset_id: ClobAssetId | None
> >     resolved: bool
> >     final_price: Decimal | None
> >     title: str | None
> >     market_slug: str | None
> >     closed: bool | None
> >     neg_risk: bool | None
> >     neg_risk_market_id: ConditionId | None
> >     question_index: int | None
> >     event_id: EventId | None
> >     event_slug: str | None
> > ```
>
> `final_price` 是结算派彩的 `Decimal` 值，不可用时为 `None`。结算数据可能延迟最多一分钟。
>
> 按条件查询时，改为只传 `condition_ids`：
>
> ```python theme={null}
> references = await client.get_token_references(condition_ids=[condition_id])
> ```
>
> 每次传入最多 50 个 `asset_ids` 或 10 个 `condition_ids`，不要同时传入两者。结果不分页，未知的资产 ID 会被省略。

> [tab] API
>
> 按代币 ID 查询：
>
> ```bash theme={null}
> curl "https://data-api.polymarket.com/v2/tokens?token_id=$TOKEN_ID,$OTHER_TOKEN_ID"
> ```
>
> 以下为示例响应：
>
> > [accordion] 响应：代币引用
> >
> > ```json theme={null}
> > {
> >   "data": [
> >     {
> >       "token_id": "123",
> >       "condition_id": "0x747dc809fb79e1b05be09c42d6179459a58de2ef3e40f02484a4e1260f741f75",
> >       "structural_condition_id": null,
> >       "module": "v1_ctf",
> >       "outcome_index": 1,
> >       "clob_index": 0,
> >       "outcome": "Yes",
> >       "opposite_token_id": "124",
> >       "resolved": true,
> >       "final_price": 0.5,
> >       "title": "Example Market",
> >       "market_slug": "example-market",
> >       "closed": true,
> >       "neg_risk": false,
> >       "neg_risk_market_id": null,
> >       "question_index": null,
> >       "event_id": 1234,
> >       "event_slug": "example-event"
> >     }
> >   ]
> > }
> > ```
>
> 按条件查询全部代币：
>
> ```bash theme={null}
> curl "https://data-api.polymarket.com/v2/tokens?condition=$NEG_RISK_MARKET_ID"
> ```
>
> 每次使用 `token_id`（最多 50 个 ID）或 `condition`（最多 10 个 ID），不要同时传入两者。多个 ID 用逗号分隔。结果不分页，未知的代币 ID 会被省略。

## 交易者排行榜

比较选定时间段内交易者的交易量和盈亏。

> [tab] TypeScript
>
> 在 `PublicClient` 或 `SecureClient` 上调用 `listTraderLeaderboard()`。
> `window` 默认一天，`category` 默认 overall，`sortBy` 默认按盈亏。并列的交易者
> 共享同一名次，其后的名次相应跳过。
>
> ```ts theme={null}
> import { LeaderboardWindow, TraderLeaderboardSort } from "@polymarket/client";
>
> const pages = client.listTraderLeaderboard({
>   window: LeaderboardWindow.Day,
>   sortBy: TraderLeaderboardSort.Pnl,
>   pageSize: 1,
> });
>
> for await (const page of pages) {
>   // page.items: TraderLeaderboardEntry[]
> }
> ```
>
> > [accordion] 输出：TraderLeaderboardEntry\[]
> >
> > ```ts TraderLeaderboardEntry Type theme={null}
> > type TraderLeaderboardEntry = {
> >   /** Competition rank; ties share a rank and the next rank skips. */
> >   rank: number;
> >   wallet: EvmAddress;
> >   /** PnL in USD for the selected window. */
> >   pnl: DecimalString;
> >   /** Both-sides traded volume in shares. */
> >   volume: DecimalString;
> >   userName: string | null;
> >   profileImage: string | null;
> >   xUsername: string | null;
> >   verified: boolean;
> > };
> > ```
> >
> > ```json TraderLeaderboardEntry Example theme={null}
> > [
> >   {
> >     "rank": 1,
> >     "wallet": "0xfe787d2da716d60e8acff57fb87eb13cd4d10319",
> >     "pnl": "372027.33333288063",
> >     "volume": "3036239.1641930016",
> >     "userName": "ferrariChampions2026",
> >     "verified": false
> >   }
> > ]
> > ```
>
> 在 `PublicClient` 或 `SecureClient` 上调用
> `fetchTraderLeaderboardStanding()`，读取某个钱包在两个榜单上的名次。
>
> ```ts theme={null}
> const standing = await client.fetchTraderLeaderboardStanding({
>   user: wallet,
>   window: LeaderboardWindow.Day,
> });
>
> // standing: TraderLeaderboardStanding | null
> ```
>
> 在 `SecureClient` 上调用时，可以省略 `user`，默认使用已认证账户的钱包。
>
> > [accordion] 输出：TraderLeaderboardStanding
> >
> > ```ts TraderLeaderboardStanding Type theme={null}
> > type TraderLeaderboardStanding = {
> >   wallet: EvmAddress;
> >   pnl: DecimalString;
> >   volume: DecimalString;
> >   pnlRank: number | null;
> >   volumeRank: number | null;
> >   userName: string | null;
> >   profileImage: string | null;
> >   xUsername: string | null;
> >   verified: boolean;
> > };
> > ```
> >
> > ```json TraderLeaderboardStanding Example theme={null}
> > {
> >   "wallet": "0xfe787d2da716d60e8acff57fb87eb13cd4d10319",
> >   "pnl": "420711.02199365385",
> >   "volume": "3920263.4910460007",
> >   "pnlRank": 1,
> >   "volumeRank": 1,
> >   "userName": "ferrariChampions2026",
> >   "profileImage": null,
> >   "xUsername": null,
> >   "verified": false
> > }
> > ```
>
> 名次为 `null` 表示该钱包未进入对应榜单。

> [tab] Python
>
> 在已创建的 `AsyncPublicClient` 或 `AsyncSecureClient` 上调用 `list_trader_leaderboard()`。
>
> ```python theme={null}
> pages = client.list_trader_leaderboard(window="day", sort_by="PNL", page_size=1)
>
> async for page in pages:
>     # page.items: tuple[TraderLeaderboardEntry, ...]
>     pass
> ```
>
> > [accordion] Output: TraderLeaderboardEntry
> >
> > ```python TraderLeaderboardEntry Type theme={null}
> > class TraderLeaderboardEntry:
> >     rank: int
> >     wallet: EvmAddress
> >     pnl: Decimal
> >     volume: Decimal
> >     user_name: str | None
> >     profile_image: str | None
> >     x_username: str | None
> >     verified: bool
> > ```
> >
> > ```json TraderLeaderboardEntry Example theme={null}
> > {
> >   "rank": 1,
> >   "wallet": "0x31e5d54aded22aa7cd80dbe9e33102abe2504879",
> >   "pnl": "966725.5781960003",
> >   "volume": "1491184.383039",
> >   "user_name": "Noprajsk",
> >   "profile_image": null,
> >   "x_username": null,
> >   "verified": false
> > }
> > ```
>
> `pnl` 的单位为 USDC，`volume` 的单位为份额。并列交易者共享排名，后续名次相应跳过。
>
> 在已创建的 `AsyncPublicClient` 或 `AsyncSecureClient` 上调用 `get_trader_leaderboard_standing()`。
>
> ```python theme={null}
> standing = await client.get_trader_leaderboard_standing(
>     user="0x983eedfbd75803602e4a6e6ea9aab6dc6b9c6748",
>     window="day",
> )
>
> # standing: TraderLeaderboardStanding | None
> ```
>
> > [accordion] Output: TraderLeaderboardStanding
> >
> > ```python TraderLeaderboardStanding Type theme={null}
> > class TraderLeaderboardStanding:
> >     wallet: EvmAddress
> >     pnl: Decimal
> >     volume: Decimal
> >     user_name: str | None
> >     profile_image: str | None
> >     x_username: str | None
> >     verified: bool
> >     pnl_rank: int | None
> >     volume_rank: int | None
> > ```
> >
> > ```json TraderLeaderboardStanding Example theme={null}
> > {
> >   "wallet": "0x7c3db723f1d4d8cb9c550095203b686cb11e5c6b",
> >   "pnl": "957.4473660823187",
> >   "volume": "64431.760178000004",
> >   "user_name": "Car",
> >   "profile_image": "https://polymarket-upload.s3.us-east-2.amazonaws.com/profile-image-501613-aa434e55-7732-41b1-9650-83a9d1d716ef.png",
> >   "x_username": "CarOnPolymarket",
> >   "verified": true,
> >   "pnl_rank": 1045,
> >   "volume_rank": 424
> > }
> > ```
>
> 返回 `None` 表示没有可用排名。某项排名为 `None` 表示钱包未进入该榜单。安全客户端默认使用已认证钱包作为 `user`。

> [tab] API
>
> 列出某个时间段的交易者排行榜。榜单默认按盈亏排名；传入
> `sort_by=VOLUME` 获取交易量榜：
>
> ```bash theme={null}
> curl "https://data-api.polymarket.com/v2/leaderboard?time_period=day&limit=1"
> ```
>
> 响应包含按排名排列的交易者（为简洁起见，已省略部分行内字段）：
>
> > [accordion] 响应
> >
> > ```json theme={null}
> > {
> >   "data": [
> >     {
> >       "rank": 1,
> >       "user_id": "0x34dd4a4b70eaf79a17878f7938263c801d4dfd83",
> >       "user_name": "vito3corleone",
> >       "pnl": 470760.47323424,
> >       "volume": 1485869.23,
> >       "verified": false
> >     }
> >   ],
> >   "pagination": {
> >     "limit": 1,
> >     "offset": 0,
> >     "has_more": true,
> >     "next_cursor": "eyJkYXRhIjp7InR5cGUiOiJsZWFkZXJib2FyZCI…"
> >   }
> > }
> > ```

## 最大盈利榜

按结算时的利润比较单个获胜持仓。

> [tab] TypeScript
>
> 在 `PublicClient` 或 `SecureClient` 上调用 `listBiggestWinners()`。
>
> ```ts theme={null}
> import { LeaderboardWindow } from "@polymarket/client";
>
> const pages = client.listBiggestWinners({
>   window: LeaderboardWindow.Day,
>   pageSize: 10,
> });
>
> for await (const page of pages) {
>   // page.items: BiggestWinner[]
> }
> ```
>
> `window` 选择结算时间段。每条记录代表一个持仓。使用 `eventId` 前请检查 `kind`，Combo 的 `eventId` 为 `null`。

> [tab] Python
>
> 在已创建的 `AsyncPublicClient` 或 `AsyncSecureClient` 上调用 `list_biggest_winners()`。
>
> ```python theme={null}
> pages = client.list_biggest_winners(window="day", page_size=10)
>
> async for page in pages:
>     # page.items: tuple[MarketBiggestWinner | ComboBiggestWinner, ...]
>     pass
> ```
>
> `window` 选择结算时间段。每行表示一个盈利仓位。访问市场专属字段前先检查 `kind`。`MarketBiggestWinner` 使用 `asset_id` 标识资产，并包含 `event_id`。`ComboBiggestWinner` 使用 `position_id`。

> [tab] API
>
> 列出最近一天结算的最大盈利持仓：
>
> ```bash theme={null}
> curl "https://data-api.polymarket.com/v2/biggest-winners?time_period=day&limit=10"
> ```
>
> `data` 的每条记录代表一个获胜持仓。将 `pagination.next_cursor` 作为 `cursor` 继续请求，直到其为 `null`。

## Builder 分析

通过归因到 Builder 集成的交易活动，评估其覆盖范围。

### Builder 排行榜

根据归因交易量和活跃用户数比较各个 Builder。

> [tab] TypeScript
>
> 在 `PublicClient` 或 `SecureClient` 上调用 `listBuilderLeaderboard()`。
>
> ```ts theme={null}
> import { LeaderboardWindow } from "@polymarket/client";
>
> const pages = client.listBuilderLeaderboard({
>   window: LeaderboardWindow.Day,
>   pageSize: 1,
> });
>
> for await (const page of pages) {
>   // page.items: BuilderStanding[]
> }
> ```
>
> > [accordion] 输出：BuilderStanding\[]
> >
> > ```ts BuilderStanding Type theme={null}
> > type BuilderStanding = {
> >   rank: number;
> >   /** Display name; use `builderCode` as the stable identifier. */
> >   builderName: string;
> >   builderCode: BuilderCode;
> >   profileImage?: string;
> >   verified: boolean;
> >   /** Builder-attributed volume in shares. */
> >   volume: DecimalString;
> >   activeUsers: number;
> > };
> > ```
> >
> > ```json BuilderStanding Example theme={null}
> > [
> >   {
> >     "rank": 1,
> >     "builderName": "betmoar",
> >     "builderCode": "0xceebf77a833b30520287ddd9478ff51abbdffa30aa90a8d655dba0e8a79ce0c1",
> >     "verified": true,
> >     "volume": "1994518.4590840002",
> >     "activeUsers": 150
> >   }
> > ]
> > ```

> [tab] Python
>
> 在已创建的 `AsyncPublicClient` 或 `AsyncSecureClient` 上调用 `list_builder_leaderboard()`。
>
> ```python theme={null}
> pages = client.list_builder_leaderboard(window="day", page_size=1)
>
> async for page in pages:
>     # page.items: tuple[BuilderStanding, ...]
>     pass
> ```
>
> > [accordion] Output: BuilderStanding
> >
> > ```python BuilderStanding Type theme={null}
> > class BuilderStanding:
> >     rank: int
> >     builder_name: str
> >     builder_code: HexString
> >     profile_image: str | None
> >     verified: bool
> >     volume: Decimal
> >     active_users: int
> > ```
> >
> > ```json BuilderStanding Example theme={null}
> > {
> >   "rank": 1,
> >   "builder_name": "betmoar",
> >   "builder_code": "0xceebf77a833b30520287ddd9478ff51abbdffa30aa90a8d655dba0e8a79ce0c1",
> >   "profile_image": "https://polymarket-upload.s3.us-east-2.amazonaws.com/betmoar_2.png",
> >   "verified": true,
> >   "volume": "3420022.424486001",
> >   "active_users": 165
> > }
> > ```
>
> 使用 `builder_code` 作为稳定标识。`volume` 是归属于该 Builder 的交易份额。

> [tab] API
>
> 列出某个时间段的 Builder 排行榜：
>
> ```bash theme={null}
> curl "https://data-api.polymarket.com/v2/builders/leaderboard?time_period=day&limit=1"
> ```
>
> 响应包含按排名排列的 Builder（为简洁起见，已省略部分行内字段）：
>
> > [accordion] 响应
> >
> > ```json theme={null}
> > {
> >   "data": [
> >     {
> >       "rank": 1,
> >       "builder_name": "betmoar",
> >       "builder_code": "0xceebf77a833b30520287ddd9478ff51abbdffa30aa90a8d655dba0e8a79ce0c1",
> >       "verified": true,
> >       "volume": 3001409.090169,
> >       "active_users": 160
> >     }
> >   ],
> >   "pagination": {
> >     "limit": 1,
> >     "offset": 0,
> >     "has_more": true,
> >     "next_cursor": "eyJkYXRhIjp7InR5cGUiOiJidWlsZGVyc19sZWFkZXJib2FyZCI…"
> >   }
> > }
> > ```

### Builder 交易量

跟踪归因到 Builder 的交易量和活跃用户数随时间的变化。

> [tab] TypeScript
>
> 在 `PublicClient` 或 `SecureClient` 上调用 `fetchBuilderVolume()`。
> `interval` 选择时间桶宽度，`bucketLimit` 计数最近的完整时间桶（至多 90 个）；
> 每个在桶内有活动的 Builder 各占一行。
>
> ```ts theme={null}
> import { BuilderVolumeInterval } from "@polymarket/client";
>
> const builderVolume = await client.fetchBuilderVolume({
>   interval: BuilderVolumeInterval.Day,
>   bucketLimit: 1,
> });
>
> // builderVolume: BuilderVolumePoint[]
> ```
>
> > [accordion] 输出：BuilderVolumePoint\[]
> >
> > ```ts BuilderVolumePoint Type theme={null}
> > type BuilderVolumePoint = {
> >   /** UTC start date of the volume bucket. */
> >   bucketDate: IsoCalendarDateString;
> >   /** Builder rank within this bucket. */
> >   rank: number;
> >   /** Display name; use `builderCode` as the stable identifier. */
> >   builderName: string;
> >   builderCode: BuilderCode;
> >   profileImage?: string;
> >   verified: boolean;
> >   /** Builder-attributed volume in shares for this bucket. */
> >   volume: DecimalString;
> >   activeUsers: number;
> > };
> > ```
> >
> > ```json BuilderVolumePoint Example theme={null}
> > [
> >   {
> >     "bucketDate": "2026-09-03",
> >     "rank": 1,
> >     "builderName": "betmoar",
> >     "builderCode": "0xceebf77a833b30520287ddd9478ff51abbdffa30aa90a8d655dba0e8a79ce0c1",
> >     "verified": true,
> >     "volume": "1990330.1396780002",
> >     "activeUsers": 150
> >   }
> > ]
> > ```

> [tab] Python
>
> 在已创建的 `AsyncPublicClient` 或 `AsyncSecureClient` 上调用 `get_builder_volumes()`。
>
> ```python theme={null}
> builder_volume = await client.get_builder_volumes(interval="day", bucket_limit=1)
>
> # builder_volume: tuple[BuilderVolumePoint, ...]
> ```
>
> > [accordion] Output: BuilderVolumePoint
> >
> > ```python BuilderVolumePoint Type theme={null}
> > class BuilderVolumePoint:
> >     rank: int
> >     builder_name: str
> >     builder_code: HexString
> >     profile_image: str | None
> >     verified: bool
> >     volume: Decimal
> >     active_users: int
> >     bucket_date: date
> > ```
> >
> > ```json BuilderVolumePoint Example theme={null}
> > {
> >   "rank": 1,
> >   "builder_name": "betmoar",
> >   "builder_code": "0xceebf77a833b30520287ddd9478ff51abbdffa30aa90a8d655dba0e8a79ce0c1",
> >   "profile_image": "https://polymarket-upload.s3.us-east-2.amazonaws.com/betmoar_2.png",
> >   "verified": true,
> >   "volume": "3419926.8151110006",
> >   "active_users": 165,
> >   "bucket_date": "2026-09-08"
> > }
> > ```
>
> 结果为日历时间桶元组。`bucket_limit` 计算日期数而非行数，最大为 90。每个活跃 Builder 在该日期对应一行。`volume` 的单位为份额。

> [tab] API
>
> 获取 Builder 交易量走势。每一行是某个 Builder 在一个时间桶内的
> 交易量及其在该桶内的排名；`limit` 计数最近的时间桶数量：
>
> ```bash theme={null}
> curl "https://data-api.polymarket.com/v2/builders/volume?interval=day&limit=1"
> ```
>
> 响应包含按时间桶划分的 Builder 活动（为简洁起见，已省略部分行内字段及其余行）：
>
> > [accordion] 响应
> >
> > ```json theme={null}
> > {
> >   "data": [
> >     {
> >       "date": "2026-08-31",
> >       "rank": 1,
> >       "builder_name": "betmoar",
> >       "builder_code": "0xceebf77a833b30520287ddd9478ff51abbdffa30aa90a8d655dba0e8a79ce0c1",
> >       "verified": true,
> >       "volume": 2961462.652905,
> >       "active_users": 160
> >     },
> >     {
> >       "date": "2026-08-31",
> >       "rank": 2,
> >       "builder_name": "traderline",
> >       "builder_code": "0x6b0e773fada0a2ec67c956b25a737d353a534ea33db56c717ba7854346c67984",
> >       "verified": true,
> >       "volume": 2445464.426092,
> >       "active_users": 112
> >     }
> >   ]
> > }
> > ```


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
