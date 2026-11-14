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
source_url: 'https://docs.polymarket.com/cn/market-data/realtime-data'
updated_at: 2026-11-13
---

# 实时数据

> 通过 Polymarket 的实时数据流持续更新市场数据。

使用 Polymarket 的实时数据流，在市场状况和相关数据发生变化时及时响应。
这些数据流无需重复轮询，即可让应用所依赖的公开市场数据保持最新。
如需经过身份验证的订单和交易更新，请参阅
[实时订单更新](https://docs.polymarket.com/cn/trading/realtime-order-updates.md)。

## 市场数据流

使用市场数据流，让应用与市场订单簿和交易状态的变化保持同步。

> [tab] TypeScript
>
> 使用 `PublicClient` 或 `SecureClient`，通过一个或多个资产 ID 订阅
> `market` 主题：
>
> ```ts theme={null}
> const assetId = "<asset_id>";
>
> const stream = await client.subscribe([
>   {
>     topic: "market",
>     assetIds: [assetId],
>   },
> ]);
>
> for await (const event of stream) {
>   switch (event.type) {
>     case "book":
>       // event: MarketBookEvent
>       break;
>     case "price_change":
>       // event: MarketPriceChangeEvent
>       break;
>     case "last_trade_price":
>       // event: MarketLastTradePriceEvent
>       break;
>     case "tick_size_change":
>       // event: MarketTickSizeChangeEvent
>       break;
>   }
> }
> ```
>
> > [accordion] 标准市场事件
> >
> > #### 订单簿
> >
> > ```ts MarketBookEvent Type theme={null}
> > type OrderBookLevel = {
> >   price: DecimalString;
> >   size: DecimalString;
> > };
> >
> > type MarketBookEvent = {
> >   topic: "market";
> >   type: "book";
> >   payload: {
> >     market: string;
> >     assetId: ClobAssetId;
> >     bids: OrderBookLevel[];
> >     asks: OrderBookLevel[];
> >     hash?: string | null;
> >     timestamp?: string | null;
> >     minOrderSize?: DecimalString | null;
> >     tickSize?: DecimalString | null;
> >     negRisk?: boolean | null;
> >     lastTradePrice?: DecimalString | null;
> >   };
> > };
> > ```
> >
> > ```json MarketBookEvent Example theme={null}
> > {
> >   "topic": "market",
> >   "type": "book",
> >   "payload": {
> >     "market": "0x747dc809fb79e1b05be09c42d6179459a58de2ef3e40f02484a4e1260f741f75",
> >     "assetId": "107505882767731489358349912513945399560393482969656700824895970500493757150417",
> >     "bids": [{ "price": "0.08", "size": "33343.4" }],
> >     "asks": [{ "price": "0.09", "size": "163939.58" }],
> >     "hash": "0xabc123…",
> >     "timestamp": "1782753357257"
> >   }
> > }
> > ```
> >
> > #### 价格变化
> >
> > ```ts MarketPriceChangeEvent Type theme={null}
> > type PriceChange = {
> >   assetId: ClobAssetId;
> >   price: DecimalString;
> >   size: DecimalString;
> >   side: OrderSide;
> >   hash?: string | null;
> >   bestBid?: DecimalString | null;
> >   bestAsk?: DecimalString | null;
> > };
> >
> > type MarketPriceChangeEvent = {
> >   topic: "market";
> >   type: "price_change";
> >   payload: {
> >     market: string;
> >     priceChanges: PriceChange[];
> >     timestamp?: string | null;
> >   };
> > };
> > ```
> >
> > ```json MarketPriceChangeEvent Example theme={null}
> > {
> >   "topic": "market",
> >   "type": "price_change",
> >   "payload": {
> >     "market": "0x747dc809fb79e1b05be09c42d6179459a58de2ef3e40f02484a4e1260f741f75",
> >     "priceChanges": [
> >       {
> >         "assetId": "107505882767731489358349912513945399560393482969656700824895970500493757150417",
> >         "price": "0.08",
> >         "size": "33343.4",
> >         "side": "BUY",
> >         "hash": "56621a121a47ed9333273e21c83b660cff37ae50",
> >         "bestBid": "0.08",
> >         "bestAsk": "0.09"
> >       }
> >     ],
> >     "timestamp": "1782753357257"
> >   }
> > }
> > ```
> >
> > #### 最新成交价
> >
> > ```ts MarketLastTradePriceEvent Type theme={null}
> > type MarketLastTradePriceEvent = {
> >   topic: "market";
> >   type: "last_trade_price";
> >   payload: {
> >     market: string;
> >     assetId: ClobAssetId;
> >     price: DecimalString;
> >     size?: DecimalString | null;
> >     feeRateBps?: DecimalString | null;
> >     side: OrderSide;
> >     timestamp?: string | null;
> >     transactionHash?: string | null;
> >   };
> > };
> > ```
> >
> > ```json MarketLastTradePriceEvent Example theme={null}
> > {
> >   "topic": "market",
> >   "type": "last_trade_price",
> >   "payload": {
> >     "market": "0x747dc809fb79e1b05be09c42d6179459a58de2ef3e40f02484a4e1260f741f75",
> >     "assetId": "107505882767731489358349912513945399560393482969656700824895970500493757150417",
> >     "price": "0.08",
> >     "size": "219.217767",
> >     "feeRateBps": "0",
> >     "side": "SELL",
> >     "timestamp": "1782753357257",
> >     "transactionHash": "0xeeefff…"
> >   }
> > }
> > ```
> >
> > #### 最小价格变动单位变化
> >
> > ```ts MarketTickSizeChangeEvent Type theme={null}
> > type MarketTickSizeChangeEvent = {
> >   topic: "market";
> >   type: "tick_size_change";
> >   payload: {
> >     market: string;
> >     assetId: ClobAssetId;
> >     oldTickSize?: DecimalString | null;
> >     newTickSize: DecimalString;
> >     timestamp?: string | null;
> >   };
> > };
> > ```
> >
> > ```json MarketTickSizeChangeEvent Example theme={null}
> > {
> >   "topic": "market",
> >   "type": "tick_size_change",
> >   "payload": {
> >     "market": "0x747dc809fb79e1b05be09c42d6179459a58de2ef3e40f02484a4e1260f741f75",
> >     "assetId": "107505882767731489358349912513945399560393482969656700824895970500493757150417",
> >     "oldTickSize": "0.01",
> >     "newTickSize": "0.001",
> >     "timestamp": "1782753357257"
> >   }
> > }
> > ```
>
> 启用 `customFeatureEnabled`，以接收最优买卖价和市场生命周期更新：
>
> ```ts theme={null}
> const stream = await client.subscribe([
>   {
>     topic: "market",
>     assetIds: [assetId],
>     customFeatureEnabled: true,
>   },
> ]);
>
> for await (const event of stream) {
>   switch (event.type) {
>     case "book":
>       // event: MarketBookEvent
>       break;
>     case "price_change":
>       // event: MarketPriceChangeEvent
>       break;
>     case "last_trade_price":
>       // event: MarketLastTradePriceEvent
>       break;
>     case "tick_size_change":
>       // event: MarketTickSizeChangeEvent
>       break;
>     case "best_bid_ask":
>       // event: MarketBestBidAskEvent
>       break;
>     case "new_market":
>       // event: NewMarketEvent
>       break;
>     case "market_resolved":
>       // event: MarketResolvedEvent
>       break;
>   }
> }
> ```
>
> > [accordion] 其他市场事件
> >
> > #### 最优买价和卖价
> >
> > ```ts MarketBestBidAskEvent Type theme={null}
> > type MarketBestBidAskEvent = {
> >   topic: "market";
> >   type: "best_bid_ask";
> >   payload: {
> >     market: string;
> >     assetId: ClobAssetId;
> >     bestBid?: DecimalString | null;
> >     bestAsk?: DecimalString | null;
> >     spread?: DecimalString | null;
> >     timestamp?: string | null;
> >   };
> > };
> > ```
> >
> > ```json MarketBestBidAskEvent Example theme={null}
> > {
> >   "topic": "market",
> >   "type": "best_bid_ask",
> >   "payload": {
> >     "market": "0x747dc809fb79e1b05be09c42d6179459a58de2ef3e40f02484a4e1260f741f75",
> >     "assetId": "107505882767731489358349912513945399560393482969656700824895970500493757150417",
> >     "bestBid": "0.08",
> >     "bestAsk": "0.09",
> >     "spread": "0.01",
> >     "timestamp": "1782753357257"
> >   }
> > }
> > ```
> >
> > #### 新市场
> >
> > ```ts NewMarketEvent Type theme={null}
> > type NewMarketEvent = {
> >   topic: "market";
> >   type: "new_market";
> >   payload: {
> >     id: string;
> >     question?: string | null;
> >     market: string;
> >     slug?: string | null;
> >     description?: string | null;
> >     assetIds?: ClobAssetId[] | null;
> >     outcomes?: string[] | null;
> >     eventMessage?: {
> >       id: string;
> >       ticker?: string | null;
> >       slug?: string | null;
> >       title?: string | null;
> >       description?: string | null;
> >     } | null;
> >     timestamp?: string | null;
> >     tags?: string[] | null;
> >     conditionId?: ConditionId | null;
> >     active?: boolean | null;
> >     clobTokenIds?: string[] | null;
> >     sportsMarketType?: string | null;
> >     line?: DecimalString | null;
> >     gameStartTime?: IsoDateTimeString | null;
> >     orderPriceMinTickSize?: DecimalString | null;
> >     groupItemTitle?: string | null;
> >     takerBaseFee?: DecimalString | null;
> >     feesEnabled?: boolean | null;
> >     feeSchedule?: unknown;
> >   };
> > };
> > ```
> >
> > ```json NewMarketEvent Example theme={null}
> > {
> >   "topic": "market",
> >   "type": "new_market",
> >   "payload": {
> >     "id": "123456",
> >     "market": "0x747dc809fb79e1b05be09c42d6179459a58de2ef3e40f02484a4e1260f741f75",
> >     "question": "Will the US confirm that aliens exist before 2027?",
> >     "slug": "will-the-us-confirm-that-aliens-exist-before-2027",
> >     "assetIds": [
> >       "107505882767731489358349912513945399560393482969656700824895970500493757150417",
> >       "7305630249804085635496399869905769372294302716159034447326228509068694952392"
> >     ],
> >     "outcomes": ["Yes", "No"],
> >     "active": true,
> >     "timestamp": "1782753357257"
> >   }
> > }
> > ```
> >
> > #### 市场已结算
> >
> > ```ts MarketResolvedEvent Type theme={null}
> > type MarketResolvedEvent = {
> >   topic: "market";
> >   type: "market_resolved";
> >   payload: {
> >     id: string;
> >     market: string;
> >     assetIds?: ClobAssetId[] | null;
> >     winningAssetId?: ClobAssetId | null;
> >     winningOutcome?: string | null;
> >     eventMessage?: {
> >       id: string;
> >       ticker?: string | null;
> >       slug?: string | null;
> >       title?: string | null;
> >       description?: string | null;
> >     } | null;
> >     timestamp?: string | null;
> >     tags?: string[] | null;
> >   };
> > };
> > ```
> >
> > ```json MarketResolvedEvent Example theme={null}
> > {
> >   "topic": "market",
> >   "type": "market_resolved",
> >   "payload": {
> >     "id": "123456",
> >     "market": "0x747dc809fb79e1b05be09c42d6179459a58de2ef3e40f02484a4e1260f741f75",
> >     "assetIds": [
> >       "107505882767731489358349912513945399560393482969656700824895970500493757150417",
> >       "7305630249804085635496399869905769372294302716159034447326228509068694952392"
> >     ],
> >     "winningAssetId": "107505882767731489358349912513945399560393482969656700824895970500493757150417",
> >     "winningOutcome": "Yes",
> >     "timestamp": "1782753357257"
> >   }
> > }
> > ```

> [tab] Python
>
> 使用 `AsyncPublicClient` 或 `AsyncSecureClient`，通过包含一个或多个代币
> ID 的 `MarketSpec` 订阅市场数据流：
>
> ```python theme={null}
> from polymarket.streams import MarketSpec
>
> asset_id = "<asset_id>"
>
> async with await client.subscribe(
>     MarketSpec(asset_ids=[asset_id]),
> ) as stream:
>     async for event in stream:
>         if event.type == "book":
>             ...  # event: MarketBookEvent
>         elif event.type == "price_change":
>             ...  # event: MarketPriceChangeEvent
>         elif event.type == "last_trade_price":
>             ...  # event: MarketLastTradePriceEvent
>         elif event.type == "tick_size_change":
>             ...  # event: MarketTickSizeChangeEvent
> ```
>
> > [accordion] 标准市场事件
> >
> > #### 订单簿
> >
> > ```python MarketBookEvent Type theme={null}
> > class OrderBookLevel:
> >     price: Decimal
> >     size: Decimal
> >
> > class MarketBookPayload:
> >     market: str
> >     asset_id: ClobAssetId
> >     bids: tuple[OrderBookLevel, ...]
> >     asks: tuple[OrderBookLevel, ...]
> >     hash: str | None
> >     timestamp: datetime | None
> >     min_order_size: Decimal | None
> >     tick_size: Decimal | None
> >     neg_risk: bool | None
> >     last_trade_price: Decimal | None
> >
> > class MarketBookEvent:
> >     topic: Literal["market"]
> >     type: Literal["book"]
> >     payload: MarketBookPayload
> > ```
> >
> > ```json MarketBookEvent Example theme={null}
> > {
> >   "topic": "market",
> >   "type": "book",
> >   "payload": {
> >     "market": "0x747dc809fb79e1b05be09c42d6179459a58de2ef3e40f02484a4e1260f741f75",
> >     "asset_id": "107505882767731489358349912513945399560393482969656700824895970500493757150417",
> >     "bids": [{ "price": "0.08", "size": "33343.4" }],
> >     "asks": [{ "price": "0.09", "size": "163939.58" }],
> >     "hash": "0xabc123…",
> >     "timestamp": "2026-06-29T17:15:57.257000Z"
> >   }
> > }
> > ```
> >
> > #### 价格变化
> >
> > ```python MarketPriceChangeEvent Type theme={null}
> > class PriceChange:
> >     asset_id: ClobAssetId
> >     price: Decimal
> >     size: Decimal
> >     side: Literal["BUY", "SELL"]
> >     hash: str | None
> >     best_bid: Decimal | None
> >     best_ask: Decimal | None
> >
> > class MarketPriceChangePayload:
> >     market: str
> >     price_changes: tuple[PriceChange, ...]
> >     timestamp: datetime | None
> >
> > class MarketPriceChangeEvent:
> >     topic: Literal["market"]
> >     type: Literal["price_change"]
> >     payload: MarketPriceChangePayload
> > ```
> >
> > ```json MarketPriceChangeEvent Example theme={null}
> > {
> >   "topic": "market",
> >   "type": "price_change",
> >   "payload": {
> >     "market": "0x747dc809fb79e1b05be09c42d6179459a58de2ef3e40f02484a4e1260f741f75",
> >     "price_changes": [
> >       {
> >         "asset_id": "107505882767731489358349912513945399560393482969656700824895970500493757150417",
> >         "price": "0.08",
> >         "size": "33343.4",
> >         "side": "BUY",
> >         "hash": "56621a121a47ed9333273e21c83b660cff37ae50",
> >         "best_bid": "0.08",
> >         "best_ask": "0.09"
> >       }
> >     ],
> >     "timestamp": "2026-06-29T17:15:57.257000Z"
> >   }
> > }
> > ```
> >
> > #### 最新成交价
> >
> > ```python MarketLastTradePriceEvent Type theme={null}
> > class MarketLastTradePricePayload:
> >     market: str
> >     asset_id: ClobAssetId
> >     price: Decimal
> >     size: Decimal | None
> >     side: Literal["BUY", "SELL"]
> >     fee_rate_bps: Decimal | None
> >     transaction_hash: str | None
> >     timestamp: datetime | None
> >
> > class MarketLastTradePriceEvent:
> >     topic: Literal["market"]
> >     type: Literal["last_trade_price"]
> >     payload: MarketLastTradePricePayload
> > ```
> >
> > ```json MarketLastTradePriceEvent Example theme={null}
> > {
> >   "topic": "market",
> >   "type": "last_trade_price",
> >   "payload": {
> >     "market": "0x747dc809fb79e1b05be09c42d6179459a58de2ef3e40f02484a4e1260f741f75",
> >     "asset_id": "107505882767731489358349912513945399560393482969656700824895970500493757150417",
> >     "price": "0.08",
> >     "size": "219.217767",
> >     "side": "SELL",
> >     "fee_rate_bps": "0",
> >     "transaction_hash": "0xeeefff…",
> >     "timestamp": "2026-06-29T17:15:57.257000Z"
> >   }
> > }
> > ```
> >
> > #### 最小价格变动单位变化
> >
> > ```python MarketTickSizeChangeEvent Type theme={null}
> > class MarketTickSizeChangePayload:
> >     market: str
> >     asset_id: ClobAssetId
> >     old_tick_size: Decimal | None
> >     new_tick_size: Decimal
> >     timestamp: datetime | None
> >
> > class MarketTickSizeChangeEvent:
> >     topic: Literal["market"]
> >     type: Literal["tick_size_change"]
> >     payload: MarketTickSizeChangePayload
> > ```
> >
> > ```json MarketTickSizeChangeEvent Example theme={null}
> > {
> >   "topic": "market",
> >   "type": "tick_size_change",
> >   "payload": {
> >     "market": "0x747dc809fb79e1b05be09c42d6179459a58de2ef3e40f02484a4e1260f741f75",
> >     "asset_id": "107505882767731489358349912513945399560393482969656700824895970500493757150417",
> >     "old_tick_size": "0.01",
> >     "new_tick_size": "0.001",
> >     "timestamp": "2026-06-29T17:15:57.257000Z"
> >   }
> > }
> > ```
>
> 启用 `custom_feature_enabled`，以接收最优买卖价和市场生命周期更新：
>
> ```python theme={null}
> async with await client.subscribe(
>     MarketSpec(asset_ids=[asset_id], custom_feature_enabled=True),
> ) as stream:
>     async for event in stream:
>         if event.type == "book":
>             ...  # event: MarketBookEvent
>         elif event.type == "price_change":
>             ...  # event: MarketPriceChangeEvent
>         elif event.type == "last_trade_price":
>             ...  # event: MarketLastTradePriceEvent
>         elif event.type == "tick_size_change":
>             ...  # event: MarketTickSizeChangeEvent
>         elif event.type == "best_bid_ask":
>             ...  # event: MarketBestBidAskEvent
>         elif event.type == "new_market":
>             ...  # event: NewMarketEvent
>         elif event.type == "market_resolved":
>             ...  # event: MarketResolvedEvent
> ```
>
> > [accordion] 其他市场事件
> >
> > #### 最优买价和卖价
> >
> > ```python MarketBestBidAskEvent Type theme={null}
> > class MarketBestBidAskPayload:
> >     market: str
> >     asset_id: ClobAssetId
> >     best_bid: Decimal | None
> >     best_ask: Decimal | None
> >     spread: Decimal | None
> >     timestamp: datetime | None
> >
> > class MarketBestBidAskEvent:
> >     topic: Literal["market"]
> >     type: Literal["best_bid_ask"]
> >     payload: MarketBestBidAskPayload
> > ```
> >
> > ```json MarketBestBidAskEvent Example theme={null}
> > {
> >   "topic": "market",
> >   "type": "best_bid_ask",
> >   "payload": {
> >     "market": "0x747dc809fb79e1b05be09c42d6179459a58de2ef3e40f02484a4e1260f741f75",
> >     "asset_id": "107505882767731489358349912513945399560393482969656700824895970500493757150417",
> >     "best_bid": "0.08",
> >     "best_ask": "0.09",
> >     "spread": "0.01",
> >     "timestamp": "2026-06-29T17:15:57.257000Z"
> >   }
> > }
> > ```
> >
> > #### 新市场
> >
> > ```python NewMarketEvent Type theme={null}
> > class MarketEventMessage:
> >     id: str
> >     ticker: str | None
> >     slug: str | None
> >     title: str | None
> >     description: str | None
> >
> > class NewMarketPayload:
> >     id: str
> >     market: str
> >     question: str | None
> >     slug: str | None
> >     description: str | None
> >     asset_ids: tuple[ClobAssetId, ...] | None
> >     outcomes: tuple[str, ...] | None
> >     event_message: MarketEventMessage | None
> >     timestamp: datetime | None
> >     tags: tuple[str, ...] | None
> >     condition_id: ConditionId | None
> >     active: bool | None
> >     clob_token_ids: tuple[str, ...] | None
> >     sports_market_type: str | None
> >     line: Decimal | None
> >     game_start_time: datetime | None
> >     order_price_min_tick_size: Decimal | None
> >     group_item_title: str | None
> >     taker_base_fee: Decimal | None
> >     fees_enabled: bool | None
> >     fee_schedule: object | None
> >
> > class NewMarketEvent:
> >     topic: Literal["market"]
> >     type: Literal["new_market"]
> >     payload: NewMarketPayload
> > ```
> >
> > ```json NewMarketEvent Example theme={null}
> > {
> >   "topic": "market",
> >   "type": "new_market",
> >   "payload": {
> >     "id": "123456",
> >     "market": "0x747dc809fb79e1b05be09c42d6179459a58de2ef3e40f02484a4e1260f741f75",
> >     "question": "Will the US confirm that aliens exist before 2027?",
> >     "slug": "will-the-us-confirm-that-aliens-exist-before-2027",
> >     "asset_ids": [
> >       "107505882767731489358349912513945399560393482969656700824895970500493757150417",
> >       "7305630249804085635496399869905769372294302716159034447326228509068694952392"
> >     ],
> >     "outcomes": ["Yes", "No"],
> >     "active": true,
> >     "timestamp": "2026-06-29T17:15:57.257000Z"
> >   }
> > }
> > ```
> >
> > #### 市场已结算
> >
> > ```python MarketResolvedEvent Type theme={null}
> > class MarketResolvedPayload:
> >     id: str
> >     market: str
> >     asset_ids: tuple[ClobAssetId, ...] | None
> >     winning_asset_id: ClobAssetId | None
> >     winning_outcome: str | None
> >     event_message: MarketEventMessage | None
> >     timestamp: datetime | None
> >     tags: tuple[str, ...] | None
> >
> > class MarketResolvedEvent:
> >     topic: Literal["market"]
> >     type: Literal["market_resolved"]
> >     payload: MarketResolvedPayload
> > ```
> >
> > ```json MarketResolvedEvent Example theme={null}
> > {
> >   "topic": "market",
> >   "type": "market_resolved",
> >   "payload": {
> >     "id": "123456",
> >     "market": "0x747dc809fb79e1b05be09c42d6179459a58de2ef3e40f02484a4e1260f741f75",
> >     "asset_ids": [
> >       "107505882767731489358349912513945399560393482969656700824895970500493757150417",
> >       "7305630249804085635496399869905769372294302716159034447326228509068694952392"
> >     ],
> >     "winning_asset_id": "107505882767731489358349912513945399560393482969656700824895970500493757150417",
> >     "winning_outcome": "Yes",
> >     "timestamp": "2026-06-29T17:15:57.257000Z"
> >   }
> > }
> > ```

> [tab] API
>
> 连接市场 WebSocket：
>
> ```text theme={null}
> wss://ws-subscriptions-clob.polymarket.com/ws/market
> ```
>
> > [!NOTE]
> >
> > 市场 WebSocket 使用应用层心跳。每 10 秒发送一次文本帧 `PING`； 服务器会回复
> > `PONG`。
>
> 连接后，发送包含一个或多个资产 ID 的 `market` 订阅帧：
>
> ```json theme={null}
> {
>   "assets_ids": ["<asset_id>"],
>   "type": "market"
> }
> ```
>
> > [accordion] 标准市场事件
> >
> > #### 订单簿
> >
> > ```json theme={null}
> > {
> >   "event_type": "book",
> >   "market": "0x747dc809fb79e1b05be09c42d6179459a58de2ef3e40f02484a4e1260f741f75",
> >   "asset_id": "107505882767731489358349912513945399560393482969656700824895970500493757150417",
> >   "timestamp": "1782753357257",
> >   "hash": "0xabc123…",
> >   "bids": [
> >     { "price": "0.08", "size": "33343.4" },
> >     { "price": "0.09", "size": "163939.58" }
> >   ],
> >   "asks": [
> >     { "price": "0.99", "size": "218442.27" },
> >     { "price": "0.98", "size": "13229.55" }
> >   ]
> > }
> > ```
> >
> > #### 价格变化
> >
> > ```json theme={null}
> > {
> >   "event_type": "price_change",
> >   "market": "0x747dc809fb79e1b05be09c42d6179459a58de2ef3e40f02484a4e1260f741f75",
> >   "price_changes": [
> >     {
> >       "asset_id": "107505882767731489358349912513945399560393482969656700824895970500493757150417",
> >       "price": "0.08",
> >       "size": "33343.4",
> >       "side": "BUY",
> >       "hash": "56621a121a47ed9333273e21c83b660cff37ae50",
> >       "best_bid": "0.08",
> >       "best_ask": "0.09"
> >     }
> >   ],
> >   "timestamp": "1782753357257"
> > }
> > ```
> >
> > #### 最新成交价
> >
> > ```json theme={null}
> > {
> >   "event_type": "last_trade_price",
> >   "market": "0x747dc809fb79e1b05be09c42d6179459a58de2ef3e40f02484a4e1260f741f75",
> >   "asset_id": "107505882767731489358349912513945399560393482969656700824895970500493757150417",
> >   "price": "0.08",
> >   "size": "219.217767",
> >   "fee_rate_bps": "0",
> >   "side": "SELL",
> >   "timestamp": "1782753357257",
> >   "transaction_hash": "0xeeefff…"
> > }
> > ```
> >
> > #### 最小价格变动单位变化
> >
> > ```json theme={null}
> > {
> >   "event_type": "tick_size_change",
> >   "market": "0x747dc809fb79e1b05be09c42d6179459a58de2ef3e40f02484a4e1260f741f75",
> >   "asset_id": "107505882767731489358349912513945399560393482969656700824895970500493757150417",
> >   "old_tick_size": "0.01",
> >   "new_tick_size": "0.001",
> >   "timestamp": "1782753357257"
> > }
> > ```
>
> 启用 `custom_feature_enabled`，以接收最优买卖价和市场生命周期更新：
>
> ```json theme={null}
> {
>   "assets_ids": ["<asset_id>"],
>   "type": "market",
>   "custom_feature_enabled": true
> }
> ```
>
> > [accordion] 其他市场事件
> >
> > #### 最优买价和卖价
> >
> > ```json theme={null}
> > {
> >   "event_type": "best_bid_ask",
> >   "market": "0x747dc809fb79e1b05be09c42d6179459a58de2ef3e40f02484a4e1260f741f75",
> >   "asset_id": "107505882767731489358349912513945399560393482969656700824895970500493757150417",
> >   "best_bid": "0.08",
> >   "best_ask": "0.09",
> >   "spread": "0.01",
> >   "timestamp": "1782753357257"
> > }
> > ```
> >
> > #### 新市场
> >
> > ```json theme={null}
> > {
> >   "event_type": "new_market",
> >   "id": "123456",
> >   "question": "Will the US confirm that aliens exist before 2027?",
> >   "market": "0x747dc809fb79e1b05be09c42d6179459a58de2ef3e40f02484a4e1260f741f75",
> >   "slug": "will-the-us-confirm-that-aliens-exist-before-2027",
> >   "assets_ids": [
> >     "107505882767731489358349912513945399560393482969656700824895970500493757150417",
> >     "7305630249804085635496399869905769372294302716159034447326228509068694952392"
> >   ],
> >   "outcomes": ["Yes", "No"],
> >   "timestamp": "1782753357257"
> > }
> > ```
> >
> > #### 市场已结算
> >
> > ```json theme={null}
> > {
> >   "event_type": "market_resolved",
> >   "id": "123456",
> >   "market": "0x747dc809fb79e1b05be09c42d6179459a58de2ef3e40f02484a4e1260f741f75",
> >   "assets_ids": [
> >     "107505882767731489358349912513945399560393482969656700824895970500493757150417",
> >     "7305630249804085635496399869905769372294302716159034447326228509068694952392"
> >   ],
> >   "winning_asset_id": "107505882767731489358349912513945399560393482969656700824895970500493757150417",
> >   "winning_outcome": "Yes",
> >   "timestamp": "1782753357257"
> > }
> > ```
>
> 无需建立新连接，即可添加或移除资产 ID：
>
> ```json Subscribe theme={null}
> {
>   "assets_ids": ["<new_asset_id>"],
>   "operation": "subscribe"
> }
> ```
>
> ```json Unsubscribe theme={null}
> {
>   "assets_ids": ["<old_asset_id>"],
>   "operation": "unsubscribe"
> }
> ```
>
> 这些帧只会更新当前市场数据流连接的代币集合。
>
> `"initial_dump": false` 仅对首个 `market` 订阅帧跳过快照。`subscribe` 帧总会为其新增的每个资产 ID 发送一条 `book` 快照，因此如需在不接收快照的情况下开始，请在首个订阅帧中发送全部资产 ID。

## 体育数据流

使用体育数据流，让实时比赛信息与体育市场保持同步。比赛开始直播、比分或
节次发生变化以及比赛结束时，都会收到更新。NFL 和 CFB 的更新还可能反映
球权变化。

> [!WARNING]
>
> 体育数据仅供参考，可能存在延迟、错误或遗漏近期事件。Polymarket 不提供
> 交易或投资建议，不应将这些数据作为交易决策的依据。

> [tab] TypeScript
>
> 使用 `PublicClient` 或 `SecureClient`，订阅 `sports` 主题以接收所有
> 比赛更新：
>
> ```ts theme={null}
> const stream = await client.subscribe([{ topic: "sports" }]);
>
> for await (const event of stream) {
>   // event: SportsEvent
> }
> ```
>
> > [accordion] 体育事件
> >
> > ```ts SportsEvent Type theme={null}
> > type SportsEvent = {
> >   topic: "sports";
> >   type: "sport_result";
> >   payload: {
> >     gameId: number;
> >     sportradarGameId?: string | null;
> >     slug?: string | null;
> >     leagueAbbreviation: string;
> >     homeTeam?: string | null;
> >     awayTeam?: string | null;
> >     status: string;
> >     live: boolean;
> >     ended: boolean;
> >     score: string;
> >     period?: string | null;
> >     elapsed?: string | null;
> >     finishedAt?: IsoDateTimeString | null;
> >     turn?: string | null;
> >   };
> > };
> > ```
> >
> > ```json SportsEvent Example theme={null}
> > {
> >   "topic": "sports",
> >   "type": "sport_result",
> >   "payload": {
> >     "gameId": 5127839,
> >     "leagueAbbreviation": "NBA",
> >     "homeTeam": "Los Angeles Lakers",
> >     "awayTeam": "Boston Celtics",
> >     "status": "InProgress",
> >     "live": true,
> >     "ended": false,
> >     "score": "98-94",
> >     "period": "Q4",
> >     "elapsed": "05:12"
> >   }
> > }
> > ```
> >
> > `score` 是组合后的 `"<home>-<away>"` 字符串，而不是主队和客队两个
> > 独立字段。

> [tab] Python
>
> 使用 `AsyncPublicClient` 或 `AsyncSecureClient`，通过 `SportsSpec`
> 订阅以接收所有比赛更新：
>
> ```python theme={null}
> from polymarket.streams import SportsSpec
>
> async with await client.subscribe(SportsSpec()) as stream:
>     async for event in stream:
>         ...  # event: SportsEvent
> ```
>
> > [accordion] 体育事件
> >
> > ```python SportsEvent Type theme={null}
> > class SportsGameResult:
> >     game_id: int
> >     sportradar_game_id: str | None
> >     slug: str | None
> >     league_abbreviation: str
> >     home_team: str | None
> >     away_team: str | None
> >     status: str
> >     live: bool
> >     ended: bool
> >     score: str
> >     period: str | None
> >     elapsed: str | None
> >     finished_at: datetime | None
> >     turn: str | None
> >
> > class SportsResultEvent:
> >     topic: Literal["sports"]
> >     type: Literal["sport_result"]
> >     payload: SportsGameResult
> >
> > SportsEvent = SportsResultEvent
> > ```
> >
> > ```json SportsEvent Example theme={null}
> > {
> >   "topic": "sports",
> >   "type": "sport_result",
> >   "payload": {
> >     "game_id": 5127839,
> >     "league_abbreviation": "NBA",
> >     "home_team": "Los Angeles Lakers",
> >     "away_team": "Boston Celtics",
> >     "status": "InProgress",
> >     "live": true,
> >     "ended": false,
> >     "score": "98-94",
> >     "period": "Q4",
> >     "elapsed": "05:12"
> >   }
> > }
> > ```
> >
> > `score` 是组合后的 `"<home>-<away>"` 字符串，而不是主队和客队两个
> > 独立字段。

> [tab] API
>
> 连接体育 WebSocket：
>
> ```text theme={null}
> wss://sports-api.polymarket.com/ws
> ```
>
> > [!NOTE]
> >
> > 体育 WebSocket 使用应用层心跳。服务器每 5 秒发送一次文本帧 `ping`； 请在 10
> > 秒内回复 `pong`，否则服务器会关闭连接。
>
> 连接后，服务器会开始推送所有比赛更新，无需发送订阅帧。
>
> > [accordion] 体育事件
> >
> > ```json theme={null}
> > {
> >   "gameId": 5127839,
> >   "leagueAbbreviation": "NBA",
> >   "homeTeam": "Los Angeles Lakers",
> >   "awayTeam": "Boston Celtics",
> >   "status": "InProgress",
> >   "live": true,
> >   "ended": false,
> >   "score": "98-94",
> >   "period": "Q4",
> >   "elapsed": "05:12"
> > }
> > ```
> >
> > 体育消息没有封装层或事件类型字段。每条消息本身就是比赛更新对象，
> > `score` 是组合后的 `"<home>-<away>"` 字符串。

### 节次值

节次的含义和格式因运动项目而异：

| 值 | 含义 |
| - | - |
| `1H`, `2H` | 上半场或下半场 |
| `1Q`, `2Q`, `3Q`, `4Q` | 节 |
| `HT` | 中场休息 |
| `FT` | 常规时间结束 |
| `FT OT` | 加时赛后全场结束 |
| `FT NR` | 全场结束，无结果 |
| `End 1`, `End 2`, … | MLB 某局结束 |
| `1/3`, `2/3`, `3/3` | 三局两胜系列赛中的地图编号 |
| `1/5`, `2/5`, … | 五局三胜系列赛中的地图编号 |

### 比赛状态值

状态值因运动项目而异，且区分大小写：

| 运动项目 | 值 |
| - | - |
| NFL | `Scheduled`, `InProgress`, `Final`, `F/OT`, `Suspended`, `Postponed`, `Delayed`, `Canceled`, `Forfeit`, `NotNecessary` |
| NHL | `Scheduled`, `InProgress`, `Final`, `F/OT`, `F/SO`, `Suspended`, `Postponed`, `Delayed`, `Canceled`, `Forfeit`, `NotNecessary` |
| MLB | `Scheduled`, `InProgress`, `Final`, `Suspended`, `Delayed`, `Postponed`, `Canceled`, `Forfeit`, `NotNecessary` |
| NBA 和 CBB | `Scheduled`, `InProgress`, `Final`, `F/OT`, `Suspended`, `Postponed`, `Delayed`, `Canceled`, `Forfeit`, `NotNecessary` |
| CFB | `Scheduled`, `InProgress`, `Final`, `F/OT`, `Suspended`, `Postponed`, `Delayed`, `Canceled`, `Forfeit` |
| 足球 | `Scheduled`, `InProgress`, `Break`, `Suspended`, `PenaltyShootout`, `Final`, `Awarded`, `Postponed`, `Canceled` |
| 电子竞技 | `not_started`, `running`, `finished`, `postponed`, `canceled` |
| 网球 | `scheduled`, `inprogress`, `suspended`, `finished`, `postponed`, `cancelled` |

## 参考价格

通过 Polymarket 接收加密货币、股票类资产和时间加权平均参考价格。完成认证，选择所需符号，然后处理历史价格和实时更新。

> [!NOTE]
>
> 参考价格订阅需要认证。
> 现有 RTDS
> 集成请参阅[迁移指南](https://docs.polymarket.com/cn/migrate/rtds-to-polybolt.md)。

使用小写符号。加密货币和 TWAP 的完整符号列表见 [PolyBolt 概览](https://docs.polymarket.com/cn/api-reference/live-data/overview.md#支持的符号)，股票类资产符号见下方对应部分。

### 历史快照

每个新订阅提供此前两分钟价格的快照，以及实时更新。使用快照初始化本地状态，再应用最新价格。只需要实时价格的应用可以忽略快照。

### 加密货币价格

接收美元加密货币参考价格，让相关市场的价格数据保持最新。

> [tab] TypeScript
>
> 使用 `@polymarket/client` 0.11.0 或更高版本中已认证的 `SecureClient` 调用 `client.subscribe`。如需创建客户端，请参阅[钱包集成](https://docs.polymarket.com/cn/getting-started/typescript.md#钱包集成)。
>
> ```ts theme={null}
> const stream = await client.subscribe([
>   { topic: "prices.crypto", symbols: ["btcusd", "ethusd"] },
> ]);
>
> try {
>   for await (const event of stream) {
>     // event: CryptoPriceEvent
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
>
> 只需要实时更新时，可跳过 `event.type === "subscribe"` 的事件。

> [tab] Python
>
> 使用 `polymarket-client` 0.11.0 或更高版本中已认证的 `AsyncSecureClient` 调用 `client.subscribe`。先完成[安全客户端设置](https://docs.polymarket.com/cn/getting-started/python.md#安全客户端)，并在异步函数中运行以下示例。
>
> ```python theme={null}
> from polymarket.streams import CryptoPriceSpec
>
> async with await client.subscribe(
>     CryptoPriceSpec(symbols=["btcusd", "ethusd"])
> ) as stream:
>     async for event in stream:
>         # event: CryptoPriceEvent
>         if event.type == "subscribe":
>             history = event.payload.data
>             # 使用快照初始化本地状态。
>         else:
>             price = event.payload.value
>             observed_at = event.payload.timestamp
>             # 应用最新价格。
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
> `value` 为 `Decimal`，时间戳均为 UTC `datetime`。
>
> 如只需要实时价格，可跳过 `type == "subscribe"` 的事件。

> [tab] API
>
> 连接到 PolyBolt 并完成认证，然后订阅加密货币价格。
>
> **1. 建立连接**
>
> 建立到以下地址的 WebSocket 连接：
>
> ```text theme={null}
> wss://ws-live-v2.polymarket.com/ws
> ```
>
> **2. 发送认证帧**
>
> 在已建立的连接上发送 [CLOB API 凭据](https://docs.polymarket.com/cn/getting-started/api.md#身份验证)：
>
> ```json theme={null}
> {
>   "op": "auth",
>   "rid": "a1",
>   "auth": {
>     "apiKey": "<api key>",
>     "secret": "<api secret>",
>     "passphrase": "<api passphrase>"
>   }
> }
> ```
>
> **3. 等待认证确认**
>
> 等待服务器确认认证成功后，再发送订阅：
>
> ```json theme={null}
> {
>   "op": "authed",
>   "rid": "a1"
> }
> ```
>
> **4. 订阅加密货币价格**
>
> 在已认证的连接上发送以下帧，订阅 BTC/USD：
>
> ```json theme={null}
> {
>   "op": "subscribe",
>   "rid": "s1",
>   "subscriptions": [
>     {
>       "channel": "price.crypto",
>       "filter": {
>         "symbol": "btcusd"
>       }
>     }
>   ]
> }
> ```

### 股票类资产价格

接收股票、ETF、外汇、贵金属和大宗商品参考价格。

> [tab] TypeScript
>
> 使用已认证的 `SecureClient` 调用 `client.subscribe`，订阅 `prices.equity` 主题和所需的交易符号。
>
> ```ts theme={null}
> const stream = await client.subscribe([
>   { topic: "prices.equity", symbol: "aapl" },
> ]);
>
> try {
>   for await (const event of stream) {
>     // event: EquityPriceEvent
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
> 只需要实时更新时，可跳过 `event.type === "subscribe"` 的事件。

> [tab] Python
>
> 使用已认证的 `AsyncSecureClient` 调用 `client.subscribe`，订阅 `prices.equity` 主题和所需的交易符号。
>
> ```python theme={null}
> from polymarket.streams import EquityPriceSpec
>
> async with await client.subscribe(
>     EquityPriceSpec(symbol="aapl")
> ) as stream:
>     async for event in stream:
>         # event: EquityPriceEvent
>         if event.type == "subscribe":
>             history = event.payload.data
>             # 使用快照初始化本地状态。
>         else:
>             price = event.payload.value
>             observed_at = event.payload.timestamp
>             # 应用最新价格。
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
> `value` 为 `Decimal`，时间戳均为 UTC `datetime`。
>
> 如只需要实时更新，设置 `types=["update"]`。省略 `types` 或传入空列表可同时接收历史和更新。更新可能附带 `received_at` 与 `is_carried_forward`。

> [tab] API
>
> 复用[加密货币价格](#加密货币价格) API 示例中已认证的连接，发送以下帧以订阅 AAPL：
>
> ```json theme={null}
> {
>   "op": "subscribe",
>   "rid": "s2",
>   "subscriptions": [
>     {
>       "channel": "price.equity",
>       "filter": {
>         "symbol": "aapl"
>       }
>     }
>   ]
> }
> ```

#### 支持的股票类资产符号

| 资产类别 | 支持的符号 |
| - | - |
| 股票 | `aapl`, `tsla`, `msft`, `googl`, `amzn`, `meta`, `nvda`, `nflx`, `pltr`, `open`, `rklb`, `abnb`, `coin`, `hood`, `spcx`, `intc`, `mstr`, `crcl`, `mu` |
| ETF | `qqq`, `spy`, `ewy`, `vxx` |
| 外汇 | `eurusd`, `gbpusd`, `usdcad`, `usdjpy`, `usdkrw`, `usdchf`, `usdmxn`, `usdzar`, `usdbrl`, `usdnok`, `usdsek`, `usdtry`, `dxy` |
| 贵金属 | `xauusd`, `xagusd` |
| 大宗商品 | `cll`, `hn`, `cc3m` |

#### 市场交易时间

当某项资产的市场休市时，数据流会继续发送其最后已知价格，并将该值标记为
沿用值。在市场交易时段内，每个数据源的价格每秒最多更新五次。

### TWAP 价格

时间加权平均价格（TWAP）表示资产在一段回看窗口内的价格。通过 Polymarket 接收 Chainlink 计算的加密货币 TWAP，回看窗口固定为 60 秒。

> [tab] TypeScript
>
> 使用已认证的 `SecureClient` 调用 `client.subscribe`，订阅 `prices.crypto.twap` 主题和所需的交易符号。
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
> 只需要实时更新时，可跳过 `event.type === "subscribe"` 的事件。 `payload.value` 已是精确小数字符串，不需要进行 E18 换算。
>
> 使用 `btcusd` 等规范符号。返回的 `windowSeconds: 60` 表示回看窗口，而非更新间隔。请使用 `payload.timestamp` 判断价格的新鲜度。

> [tab] Python
>
> 使用已认证的 `AsyncSecureClient` 调用 `client.subscribe`，订阅 `prices.crypto.twap` 主题和所需的交易符号。
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
> `value` 为 `Decimal`，时间戳均为 UTC `datetime`。
>
> `payload.window_seconds` 固定为 `60`，表示回看窗口。直接使用 `payload.value`，无需 E18 换算。用 `payload.timestamp` 检查价格的新鲜度。

> [tab] API
>
> 复用[加密货币价格](#加密货币价格) API 示例中已认证的连接，发送以下帧以订阅 60 秒 BTC/USD TWAP：
>
> ```json theme={null}
> {
>   "op": "subscribe",
>   "rid": "s3",
>   "subscriptions": [
>     {
>       "channel": "price.crypto.twap",
>       "filter": {
>         "symbol": "btcusd",
>         "window_seconds": 60
>       }
>     }
>   ]
> }
> ```

## 评论

> [!WARNING]
>
> 实时评论和表情回应数据流即将停用，且不会提供替代的流式频道。对应的获取方法见下文。

> [tab] TypeScript
>
> 创建公开客户端，调用 `client.listComments()` 获取事件的评论列表。该方法不提供实时评论或表情回应事件。
>
> ```ts theme={null}
> import {
>   CommentParentEntityType,
>   createPublicClient,
> } from "@polymarket/client";
>
> const client = createPublicClient();
> const pages = client.listComments({
>   parentEntityId: "18396",
>   parentEntityType: CommentParentEntityType.Event,
>   pageSize: 20,
>   order: "id",
>   ascending: true,
> });
> const page = await pages.firstPage();
>
> console.log(page.items);
> ```
>
> `page.items` 包含 `Comment` 对象。使用 `page.hasMore` 判断是否还有结果，并通过 `pages.from(page.nextCursor)` 继续获取。
>
> > [accordion] Output: Comment
> >
> > `page.items` 中的一条评论，序列化为 JSON，仅展示部分字段。
> >
> > ```json theme={null}
> > {
> >   "id": "1020073",
> >   "body": "@truce @yayyo",
> >   "parentEntityType": "Event",
> >   "parentEntityID": "18396",
> >   "createdAt": "2025-02-12T00:48:05.40822Z",
> >   "reactionCount": 2
> > }
> > ```

> [tab] Python
>
> 创建公开客户端，调用 `client.list_comments()` 获取事件的评论列表。该方法不提供实时评论或表情回应事件。
>
> ```python theme={null}
> from polymarket import AsyncPublicClient
>
> async with AsyncPublicClient() as client:
>     pages = client.list_comments(
>         parent_entity_id="18396",
>         parent_entity_type="Event",
>         page_size=20,
>         order="id",
>         ascending=True,
>     )
>     page = await pages.first_page()
>
>     print(page.items)
> ```
>
> `page.items` 包含 `Comment` 对象。使用 `page.has_more` 判断是否还有结果，并通过 `pages.from_cursor(page.next_cursor)` 继续获取。
>
> > [accordion] Output: Comment
> >
> > `page.items` 中的一条评论，序列化为 JSON，仅展示部分字段。
> >
> > ```json theme={null}
> > {
> >   "id": "1020073",
> >   "body": "@truce @yayyo",
> >   "parent_entity_type": "Event",
> >   "parent_entity_id": "18396",
> >   "created_at": "2025-02-12T00:48:05.408220Z",
> >   "reaction_count": 2
> > }
> > ```

> [tab] API
>
> 使用 Gamma API 的 `GET /comments` 获取事件的评论列表。该请求不提供实时评论或表情回应事件。
>
> ```bash theme={null}
> curl --get "https://gamma-api.polymarket.com/comments" \
>   --data-urlencode "parent_entity_id=18396" \
>   --data-urlencode "parent_entity_type=Event" \
>   --data-urlencode "limit=20" \
>   --data-urlencode "offset=0" \
>   --data-urlencode "order=id" \
>   --data-urlencode "ascending=true"
> ```
>
> 响应为评论数组。
>
> > [accordion] Output: Comment\[]
> >
> > 响应中的第一条评论，仅展示部分字段。
> >
> > ```json theme={null}
> > [
> >   {
> >     "id": "1020073",
> >     "body": "@truce @yayyo",
> >     "parentEntityType": "Event",
> >     "parentEntityID": 18396,
> >     "createdAt": "2025-02-12T00:48:05.40822Z",
> >     "reactionCount": 2
> >   }
> > ]
> > ```


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
