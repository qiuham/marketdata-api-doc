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
source_url: 'https://docs.polymarket.com/cn/market-data/prices-order-books'
updated_at: 2026-11-13
---

# 价格与订单簿

> 了解价格与订单簿如何反映 Polymarket 上的交易活动。

Polymarket 的每个结果都有一个在 CLOB 上交易的资产。资产价格反映交易者愿意支付的金额，订单簿则显示当前挂出的买单和卖单。

以下示例假设你已经有一个市场对象，可以从中读取结果 ID。要查找或获取市场，请参阅
[**发现市场**](https://docs.polymarket.com/cn/market-data/discover-markets.md)。

> [tab] TypeScript
>
> 根据市场版本选择每个结果 ID：
>
> ```ts theme={null}
> const yesAssetId =
>   market.version === "v2"
>     ? market.outcomes.yes.positionId
>     : market.outcomes.yes.tokenId;
> const noAssetId =
>   market.version === "v2"
>     ? market.outcomes.no.positionId
>     : market.outcomes.no.tokenId;
> ```

> [tab] Python
>
> 根据市场版本选择每个结果 ID：
>
> ```python theme={null}
> yes_asset_id = (
>     market.outcomes.yes.position_id
>     if market.version == "v2"
>     else market.outcomes.yes.token_id
> )
> no_asset_id = (
>     market.outcomes.no.position_id
>     if market.version == "v2"
>     else market.outcomes.no.token_id
> )
> ```

> [tab] API
>
> Gamma 将结果 ID 存储为 JSON 编码的数组。请根据市场版本选择数组：
>
> ```json theme={null}
> {
>   "version": "v2",
>   "positionIds": "[\"<yes_asset_id>\", \"<no_asset_id>\"]"
> }
> ```
>
> 解析数组，然后选择要读取的结果：
>
> ```bash theme={null}
> ASSET_ID="<yes_asset_id>"
> ```

## 订单簿

获取某个结果当前挂出的买单和卖单。买单按价格升序排列，卖单按价格降序排列，因此最优买价和卖价分别位于对应数组的最后一项。每个响应还包含订单簿状态的 `hash`。将其与上一次响应的哈希比较，即可判断两次读取之间订单簿是否发生变化。

### 获取订单簿

> [tab] TypeScript
>
> 在 `PublicClient` 或 `SecureClient` 上调用 `fetchOrderBook()`，获取某个结果的订单簿。
>
> ```ts theme={null}
> const book = await client.fetchOrderBook({ assetId: yesAssetId });
>
> // book: OrderBook
> ```
>
> 返回的 `OrderBook` 描述各价格档位，以及解读这些档位所需的市场详情：
>
> ```ts OrderBook Type theme={null}
> type OrderBookLevel = {
>   price: DecimalString;
>   size: DecimalString;
> };
>
> type OrderBook = {
>   conditionId: ConditionId;
>   assetId: ClobAssetId;
>   timestamp?: EpochMilliseconds | null;
>   bids: OrderBookLevel[];
>   asks: OrderBookLevel[];
>   minOrderSize: DecimalString;
>   tickSize: DecimalString;
>   negRisk: boolean;
>   lastTradePrice?: DecimalString | null;
>   hash: OrderBookHash;
> };
> ```
>
> ```json OrderBook Example theme={null}
> {
>   "conditionId": "0x747dc809fb79e1b05be09c42d6179459a58de2ef3e40f02484a4e1260f741f75",
>   "tokenId": "107505882767731489358349912513945399560393482969656700824895970500493757150417",
>   "timestamp": 1782753404902,
>   "bids": [
>     { "price": "0.01", "size": "2116131.59" },
>     { "price": "0.02", "size": "139963.89" },
>     { "price": "0.03", "size": "208169.44" },
>     "..."
>   ],
>   "asks": [
>     { "price": "0.99", "size": "93442.27" },
>     { "price": "0.98", "size": "13229.55" },
>     { "price": "0.97", "size": "4338.7" },
>     "..."
>   ],
>   "minOrderSize": "5",
>   "tickSize": "0.01",
>   "negRisk": false,
>   "lastTradePrice": "0.090",
>   "hash": "a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2"
> }
> ```

> [tab] Python
>
> 在 `AsyncPublicClient` 或 `AsyncSecureClient` 上调用 `get_order_book()`，获取某个结果的订单簿。同步 `PublicClient` 和 `SecureClient` 也提供相同方法。
>
> ```python theme={null}
> book = await client.get_order_book(asset_id=yes_asset_id)
>
> # book: OrderBook
> ```
>
> 返回的 `OrderBook` 描述各价格档位，以及解读这些档位所需的市场详情：
>
> ```python OrderBook Type theme={null}
> class OrderBookLevel:
>     price: Decimal
>     size: Decimal
>
> class OrderBook:
>     condition_id: ConditionId
>     asset_id: ClobAssetId
>     timestamp: datetime | None
>     bids: tuple[OrderBookLevel, ...]
>     asks: tuple[OrderBookLevel, ...]
>     min_order_size: Decimal
>     tick_size: Decimal
>     neg_risk: bool
>     last_trade_price: Decimal | None
>     hash: str
> ```
>
> ```json OrderBook Example theme={null}
> {
>   "condition_id": "0x747dc809fb79e1b05be09c42d6179459a58de2ef3e40f02484a4e1260f741f75",
>   "asset_id": "107505882767731489358349912513945399560393482969656700824895970500493757150417",
>   "timestamp": "2026-06-29T17:16:44.902000+00:00",
>   "bids": [
>     { "price": "0.01", "size": "2116131.59" },
>     { "price": "0.02", "size": "139963.89" },
>     { "price": "0.03", "size": "208169.44" },
>     "..."
>   ],
>   "asks": [
>     { "price": "0.99", "size": "93442.27" },
>     { "price": "0.98", "size": "13229.55" },
>     { "price": "0.97", "size": "4338.7" },
>     "..."
>   ],
>   "min_order_size": "5",
>   "tick_size": "0.01",
>   "neg_risk": false,
>   "last_trade_price": "0.090",
>   "hash": "a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2"
> }
> ```

> [tab] API
>
> 获取某个结果的订单簿：
>
> ```bash theme={null}
> curl "https://clob.polymarket.com/book?token_id=$ASSET_ID"
> ```
>
> 除价格档位外，响应还包含验证订单所需的交易限制：
>
> ```json theme={null}
> {
>   "market": "0x747dc809fb79e1b05be09c42d6179459a58de2ef3e40f02484a4e1260f741f75",
>   "asset_id": "107505882767731489358349912513945399560393482969656700824895970500493757150417",
>   "timestamp": "1782753357257",
>   "hash": "a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2",
>   "bids": [
>     { "price": "0.01", "size": "2151131.59" },
>     { "price": "0.02", "size": "139963.89" },
>     { "price": "0.03", "size": "208169.44" },
>     "..."
>   ],
>   "asks": [
>     { "price": "0.99", "size": "218442.27" },
>     { "price": "0.98", "size": "13229.55" },
>     { "price": "0.97", "size": "4338.7" },
>     "..."
>   ],
>   "min_order_size": "5",
>   "tick_size": "0.01",
>   "neg_risk": false,
>   "last_trade_price": "0.090"
> }
> ```

### 获取多个订单簿

批量读取订单簿可在一次请求中返回多个结果当前挂出的买单和卖单。

> [!NOTE]
>
> 每次请求最多 500 项。

> [tab] TypeScript
>
> 在 `PublicClient` 或 `SecureClient` 上调用 `fetchOrderBooks()`，通过一次请求获取多个订单簿。
>
> ```ts theme={null}
> const books = await client.fetchOrderBooks([
>   { assetId: yesAssetId },
>   { assetId: noAssetId },
> ]);
>
> // books: OrderBook[]
> ```
>
> 每一项都采用上文所述的 `OrderBook` 结构：
>
> ```json theme={null}
> [
>   {
>     "conditionId": "0x747dc809fb79e1b05be09c42d6179459a58de2ef3e40f02484a4e1260f741f75",
>     "bids": [
>       { "price": "0.01", "size": "2116131.59" },
>       { "price": "0.02", "size": "139963.89" },
>       { "price": "0.03", "size": "208169.44" },
>       "..."
>     ],
>     "asks": [
>       { "price": "0.99", "size": "93442.27" },
>       { "price": "0.98", "size": "13229.55" },
>       { "price": "0.97", "size": "4338.7" },
>       "..."
>     ]
>   },
>   {
>     "conditionId": "0x747dc809fb79e1b05be09c42d6179459a58de2ef3e40f02484a4e1260f741f75",
>     "bids": [
>       { "price": "0.01", "size": "93442.27" },
>       { "price": "0.02", "size": "13229.55" },
>       { "price": "0.03", "size": "4338.7" },
>       "..."
>     ],
>     "asks": [
>       { "price": "0.99", "size": "2116131.59" },
>       { "price": "0.98", "size": "139963.89" },
>       { "price": "0.97", "size": "208169.44" },
>       "..."
>     ]
>   }
> ]
> ```

> [tab] Python
>
> 在 `AsyncPublicClient` 或 `AsyncSecureClient` 上调用 `get_order_books()`，通过一次请求获取多个订单簿。同步 `PublicClient` 和 `SecureClient` 也提供相同方法。
>
> ```python theme={null}
> books = await client.get_order_books(asset_ids=[yes_asset_id, no_asset_id])
>
> # books: tuple[OrderBook, ...]
> ```
>
> 每一项都采用上文所述的 `OrderBook` 结构：
>
> ```json theme={null}
> [
>   {
>     "condition_id": "0x747dc809fb79e1b05be09c42d6179459a58de2ef3e40f02484a4e1260f741f75",
>     "bids": [
>       { "price": "0.01", "size": "2116131.59" },
>       { "price": "0.02", "size": "139963.89" },
>       { "price": "0.03", "size": "208169.44" },
>       "..."
>     ],
>     "asks": [
>       { "price": "0.99", "size": "93442.27" },
>       { "price": "0.98", "size": "13229.55" },
>       { "price": "0.97", "size": "4338.7" },
>       "..."
>     ]
>   },
>   {
>     "condition_id": "0x747dc809fb79e1b05be09c42d6179459a58de2ef3e40f02484a4e1260f741f75",
>     "bids": [
>       { "price": "0.01", "size": "93442.27" },
>       { "price": "0.02", "size": "13229.55" },
>       { "price": "0.03", "size": "4338.7" },
>       "..."
>     ],
>     "asks": [
>       { "price": "0.99", "size": "2116131.59" },
>       { "price": "0.98", "size": "139963.89" },
>       { "price": "0.97", "size": "208169.44" },
>       "..."
>     ]
>   }
> ]
> ```

> [tab] API
>
> 通过一次请求获取多个订单簿：
>
> ```bash theme={null}
> curl -X POST "https://clob.polymarket.com/books" \
>   -H "Content-Type: application/json" \
>   --data '[{"token_id":"<yes_asset_id>"},{"token_id":"<no_asset_id>"}]'
> ```
>
> 响应会为每个请求的资产 ID 返回一个订单簿：
>
> ```json theme={null}
> [
>   {
>     "market": "0x747dc809fb79e1b05be09c42d6179459a58de2ef3e40f02484a4e1260f741f75",
>     "asset_id": "107505882767731489358349912513945399560393482969656700824895970500493757150417",
>     "timestamp": "1782753357257",
>     "hash": "a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2",
>     "bids": [
>       { "price": "0.01", "size": "2151131.59" },
>       { "price": "0.02", "size": "139963.89" },
>       { "price": "0.03", "size": "208169.44" },
>       "..."
>     ],
>     "asks": [
>       { "price": "0.99", "size": "218442.27" },
>       { "price": "0.98", "size": "13229.55" },
>       { "price": "0.97", "size": "4338.7" },
>       "..."
>     ],
>     "min_order_size": "5",
>     "tick_size": "0.01",
>     "neg_risk": false,
>     "last_trade_price": "0.090"
>   },
>   {
>     "market": "0x747dc809fb79e1b05be09c42d6179459a58de2ef3e40f02484a4e1260f741f75",
>     "asset_id": "7305630249804085635496399869905769372294302716159034447326228509068694952392",
>     "timestamp": "1782753357257",
>     "hash": "f6e5d4c3b2a1f6e5d4c3b2a1f6e5d4c3b2a1f6e5d4c3b2a1f6e5d4c3b2a1f6e5",
>     "bids": [
>       { "price": "0.01", "size": "218442.27" },
>       { "price": "0.02", "size": "13229.55" },
>       { "price": "0.03", "size": "4338.7" },
>       "..."
>     ],
>     "asks": [
>       { "price": "0.99", "size": "2151131.59" },
>       { "price": "0.98", "size": "139963.89" },
>       { "price": "0.97", "size": "208169.44" },
>       "..."
>     ],
>     "min_order_size": "5",
>     "tick_size": "0.01",
>     "neg_risk": true,
>     "last_trade_price": "0.910"
>   }
> ]
> ```

## 最优市场价格

读取某个结果和方向的最优可成交价格。`BUY` 返回最低卖价，即买入时需要支付的价格；`SELL` 返回最高买价，即卖出时可以获得的价格。

### 获取价格

> [tab] TypeScript
>
> 在 `PublicClient` 或 `SecureClient` 上调用 `fetchPrice()`，获取某一方向的最优价格。对于 `BUY`，该方法返回最低卖价。
>
> ```ts theme={null}
> import { OrderSide } from "@polymarket/client";
>
> const price = await client.fetchPrice({
>   assetId: yesAssetId,
>   side: OrderSide.BUY,
> });
>
> // price: DecimalString
> ```
>
> 该方法以十进制字符串返回价格：
>
> ```json theme={null}
> "0.08"
> ```

> [tab] Python
>
> 在 `AsyncPublicClient` 或 `AsyncSecureClient` 上调用 `get_price()`，获取某一方向的最优价格。对于 `BUY`，该方法返回最低卖价。同步 `PublicClient` 和 `SecureClient` 也提供相同方法。
>
> ```python theme={null}
> price = await client.get_price(asset_id=yes_asset_id, side="BUY")
>
> # price: Decimal
> ```
>
> 该方法以 `Decimal` 返回价格：
>
> ```python theme={null}
> Decimal("0.08")
> ```

> [tab] API
>
> 获取买方可成交的最低卖价：
>
> ```bash theme={null}
> curl "https://clob.polymarket.com/price?token_id=$ASSET_ID&side=BUY"
> ```
>
> 响应包含以十进制字符串表示的价格：
>
> ```json theme={null}
> { "price": "0.08" }
> ```

### 获取多个价格

批量读取价格可在一次请求中返回多组“结果与方向”组合的最优市场价格。当同一视图或计算需要多个结果时，请使用此方式。

> [!NOTE]
>
> 每次请求最多 500 项。

> [tab] TypeScript
>
> 在 `PublicClient` 或 `SecureClient` 上调用 `fetchPrices()`，通过一次请求获取多个价格。
>
> ```ts theme={null}
> import { OrderSide } from "@polymarket/client";
>
> const prices = await client.fetchPrices([
>   { assetId: yesAssetId, side: OrderSide.BUY },
>   { assetId: noAssetId, side: OrderSide.BUY },
> ]);
>
> // prices: Prices (map of tokenId -> side -> price)
> ```
>
> `Prices` 将每个资产 ID 映射到请求的方向和价格：
>
> ```ts Prices Type theme={null}
> type Prices = Record<ClobAssetId, Partial<Record<OrderSide, DecimalString>>>;
> ```
>
> ```json Prices Example theme={null}
> {
>   "107505882767731489358349912513945399560393482969656700824895970500493757150417": {
>     "BUY": "0.08"
>   },
>   "7305630249804085635496399869905769372294302716159034447326228509068694952392": {
>     "BUY": "0.91"
>   }
> }
> ```

> [tab] Python
>
> 在 `AsyncPublicClient` 或 `AsyncSecureClient` 上调用 `get_prices()`，通过一次请求获取多个价格。同步 `PublicClient` 和 `SecureClient` 也提供相同方法。
>
> ```python theme={null}
> from polymarket import PriceRequest
>
> prices = await client.get_prices(
>     requests=[
>         PriceRequest(asset_id=yes_asset_id, side="BUY"),
>         PriceRequest(asset_id=no_asset_id, side="BUY"),
>     ],
> )
>
> # prices: dict[ClobAssetId, dict[OrderSide, Decimal]]
> ```
>
> 结果将每个资产 ID 映射到请求的方向和价格：
>
> ```json theme={null}
> {
>   "107505882767731489358349912513945399560393482969656700824895970500493757150417": {
>     "BUY": "0.08"
>   },
>   "7305630249804085635496399869905769372294302716159034447326228509068694952392": {
>     "BUY": "0.91"
>   }
> }
> ```

> [tab] API
>
> 通过一次请求获取多个价格：
>
> ```bash theme={null}
> curl -X POST "https://clob.polymarket.com/prices" \
>   -H "Content-Type: application/json" \
>   --data '[{"token_id":"<yes_asset_id>","side":"BUY"},{"token_id":"<no_asset_id>","side":"BUY"}]'
> ```
>
> 响应将每个资产 ID 映射到请求的方向和价格：
>
> ```json theme={null}
> {
>   "107505882767731489358349912513945399560393482969656700824895970500493757150417": {
>     "BUY": 0.08
>   },
>   "7305630249804085635496399869905769372294302716159034447326228509068694952392": {
>     "BUY": 0.91
>   }
> }
> ```

## 中间价

中间价是最优买价与最优卖价的平均值，用作订单簿买卖双方之间的参考价格。

### 获取中间价

> [tab] TypeScript
>
> 在 `PublicClient` 或 `SecureClient` 上调用 `fetchMidpoint()`，获取中间价。
>
> ```ts theme={null}
> const midpoint = await client.fetchMidpoint({ assetId: yesAssetId });
>
> // midpoint: DecimalString
> ```
>
> 该方法以十进制字符串返回中间价：
>
> ```json theme={null}
> "0.085"
> ```

> [tab] Python
>
> 在 `AsyncPublicClient` 或 `AsyncSecureClient` 上调用 `get_midpoint()`，获取中间价。同步 `PublicClient` 和 `SecureClient` 也提供相同方法。
>
> ```python theme={null}
> midpoint = await client.get_midpoint(asset_id=yes_asset_id)
>
> # midpoint: Decimal
> ```
>
> 该方法以 `Decimal` 返回中间价：
>
> ```python theme={null}
> Decimal("0.085")
> ```

> [tab] API
>
> 获取中间价：
>
> ```bash theme={null}
> curl "https://clob.polymarket.com/midpoint?token_id=$ASSET_ID"
> ```
>
> 响应包含以十进制字符串表示的中间价：
>
> ```json theme={null}
> { "mid": "0.085" }
> ```

### 获取多个中间价

通过一次请求获取多个结果的中间价。

> [!NOTE]
>
> 每次请求最多 500 项。

> [tab] TypeScript
>
> 在 `PublicClient` 或 `SecureClient` 上调用 `fetchMidpoints()`，获取多个中间价。
>
> ```ts theme={null}
> const midpoints = await client.fetchMidpoints([
>   { assetId: yesAssetId },
>   { assetId: noAssetId },
> ]);
>
> // midpoints: Midpoints
> ```
>
> `Midpoints` 将每个资产 ID 映射到其中间价：
>
> ```ts Midpoints Type theme={null}
> type Midpoints = Record<ClobAssetId, DecimalString>;
> ```
>
> ```json Midpoints Example theme={null}
> {
>   "107505882767731489358349912513945399560393482969656700824895970500493757150417": "0.085",
>   "7305630249804085635496399869905769372294302716159034447326228509068694952392": "0.915"
> }
> ```

> [tab] Python
>
> 在 `AsyncPublicClient` 或 `AsyncSecureClient` 上调用 `get_midpoints()`，获取多个中间价。同步 `PublicClient` 和 `SecureClient` 也提供相同方法。
>
> ```python theme={null}
> midpoints = await client.get_midpoints(asset_ids=[yes_asset_id, no_asset_id])
>
> # midpoints: dict[ClobAssetId, Decimal]
> ```
>
> 结果将每个资产 ID 映射到其中间价：
>
> ```json theme={null}
> {
>   "107505882767731489358349912513945399560393482969656700824895970500493757150417": "0.085",
>   "7305630249804085635496399869905769372294302716159034447326228509068694952392": "0.915"
> }
> ```

> [tab] API
>
> 通过一次请求获取多个中间价：
>
> ```bash theme={null}
> curl -X POST "https://clob.polymarket.com/midpoints" \
>   -H "Content-Type: application/json" \
>   --data '[{"token_id":"<yes_asset_id>"},{"token_id":"<no_asset_id>"}]'
> ```
>
> 响应将每个资产 ID 映射到其中间价：
>
> ```json theme={null}
> {
>   "107505882767731489358349912513945399560393482969656700824895970500493757150417": "0.085",
>   "7305630249804085635496399869905769372294302716159034447326228509068694952392": "0.915"
> }
> ```

## 买卖价差

买卖价差是最优卖价与最优买价之间的差值。价差越窄，表示订单簿买卖双方的价格越接近。

### 获取买卖价差

> [tab] TypeScript
>
> 在 `PublicClient` 或 `SecureClient` 上调用 `fetchSpread()`，获取买卖价差。
>
> ```ts theme={null}
> const spread = await client.fetchSpread({ assetId: yesAssetId });
>
> // spread: DecimalString
> ```
>
> 该方法以十进制字符串返回买卖价差：
>
> ```json theme={null}
> "0.01"
> ```

> [tab] Python
>
> 在 `AsyncPublicClient` 或 `AsyncSecureClient` 上调用 `get_spread()`，获取买卖价差。同步 `PublicClient` 和 `SecureClient` 也提供相同方法。
>
> ```python theme={null}
> spread = await client.get_spread(asset_id=yes_asset_id)
>
> # spread: Decimal
> ```
>
> 该方法以 `Decimal` 返回买卖价差：
>
> ```python theme={null}
> Decimal("0.01")
> ```

> [tab] API
>
> 获取买卖价差：
>
> ```bash theme={null}
> curl "https://clob.polymarket.com/spread?token_id=$ASSET_ID"
> ```
>
> 响应包含以十进制字符串表示的买卖价差：
>
> ```json theme={null}
> { "spread": "0.01" }
> ```

### 获取多个买卖价差

批量读取价差可在一次请求中返回多个结果的买卖价差。

> [!NOTE]
>
> 每次请求最多 500 项。

> [tab] TypeScript
>
> 在 `PublicClient` 或 `SecureClient` 上调用 `fetchSpreads()`，通过一次请求获取多个买卖价差。
>
> ```ts theme={null}
> const spreads = await client.fetchSpreads([
>   { assetId: yesAssetId },
>   { assetId: noAssetId },
> ]);
>
> // spreads: Spreads
> ```
>
> 结果将每个资产 ID 映射到其买卖价差：
>
> ```ts Spreads Type theme={null}
> type Spreads = Record<ClobAssetId, DecimalString>;
> ```
>
> ```json Spreads Example theme={null}
> {
>   "107505882767731489358349912513945399560393482969656700824895970500493757150417": "0.01",
>   "7305630249804085635496399869905769372294302716159034447326228509068694952392": "0.02"
> }
> ```

> [tab] Python
>
> 在 `AsyncPublicClient` 或 `AsyncSecureClient` 上调用 `get_spreads()`，通过一次请求获取多个买卖价差。同步 `PublicClient` 和 `SecureClient` 也提供相同方法。
>
> ```python theme={null}
> spreads = await client.get_spreads(asset_ids=[yes_asset_id, no_asset_id])
>
> # spreads: dict[ClobAssetId, Decimal]
> ```
>
> 结果将每个资产 ID 映射到其买卖价差：
>
> ```json theme={null}
> {
>   "107505882767731489358349912513945399560393482969656700824895970500493757150417": "0.01",
>   "7305630249804085635496399869905769372294302716159034447326228509068694952392": "0.02"
> }
> ```

> [tab] API
>
> 通过一次请求获取多个买卖价差：
>
> ```bash theme={null}
> curl -X POST "https://clob.polymarket.com/spreads" \
>   -H "Content-Type: application/json" \
>   --data '[{"token_id":"<yes_asset_id>"},{"token_id":"<no_asset_id>"}]'
> ```
>
> 响应将每个资产 ID 映射到其买卖价差：
>
> ```json theme={null}
> {
>   "107505882767731489358349912513945399560393482969656700824895970500493757150417": "0.01",
>   "7305630249804085635496399869905769372294302716159034447326228509068694952392": "0.02"
> }
> ```

## 最新成交价

最新成交价记录某个结果最近一次撮合成交的信息，包括成交价格和方向。

### 获取最新成交价

> [tab] TypeScript
>
> 在 `PublicClient` 或 `SecureClient` 上调用 `fetchLastTradePrice()`，获取最新成交记录。
>
> ```ts theme={null}
> const lastTrade = await client.fetchLastTradePrice({ assetId: yesAssetId });
>
> // lastTrade: LastTradePrice | null
> ```
>
> `LastTradePrice` 将成交价格与订单方向组合在一起：
>
> ```ts LastTradePrice Type theme={null}
> type LastTradePrice = {
>   price: DecimalString;
>   side: OrderSide;
> };
> ```
>
> ```json LastTradePrice Example theme={null}
> {
>   "price": "0.08",
>   "side": "SELL"
> }
> ```
>
> 如果代币从未成交，`fetchLastTradePrice()` 会返回 `null`，而不是
> `LastTradePrice` 对象：
>
> ```json theme={null}
> null
> ```

> [tab] Python
>
> 在 `AsyncPublicClient` 或 `AsyncSecureClient` 上调用 `get_last_trade_price()`，获取最新成交记录。同步 `PublicClient` 和 `SecureClient` 也提供相同方法。
>
> ```python theme={null}
> last_trade = await client.get_last_trade_price(asset_id=yes_asset_id)
>
> # last_trade: LastTradePrice | None
> ```
>
> `LastTradePrice` 将成交价格与订单方向组合在一起：
>
> ```python LastTradePrice Type theme={null}
> class LastTradePrice:
>     price: Decimal
>     side: OrderSide
> ```
>
> ```json LastTradePrice Example theme={null}
> {
>   "price": "0.08",
>   "side": "SELL"
> }
> ```
>
> 如果代币从未成交，`get_last_trade_price()` 会返回 `None`，而不是
> `LastTradePrice` 对象：
>
> ```python theme={null}
> None
> ```

> [tab] API
>
> 获取最新成交记录：
>
> ```bash theme={null}
> curl "https://clob.polymarket.com/last-trade-price?token_id=$ASSET_ID"
> ```
>
> 响应包含成交价格和方向：
>
> ```json theme={null}
> {
>   "price": "0.08",
>   "side": "SELL"
> }
> ```
>
> 如果代币从未成交且其订单簿为空，API 会返回占位价格 `"0.5"` 和空的
> `side` 字符串：
>
> ```json theme={null}
> {
>   "price": "0.5",
>   "side": ""
> }
> ```

### 获取多个最新成交价

通过一次请求获取多个结果最近一次撮合成交的信息。

> [!NOTE]
>
> 每次请求最多 500 项。

> [tab] TypeScript
>
> 在 `PublicClient` 或 `SecureClient` 上调用 `fetchLastTradePrices()`，获取多条最新成交记录。
>
> ```ts theme={null}
> const lastTrades = await client.fetchLastTradePrices([
>   { assetId: yesAssetId },
>   { assetId: noAssetId },
> ]);
>
> // lastTrades: LastTradePriceForAsset[]
> ```
>
> 每个 `LastTradePriceForAsset` 都标识相应结果及其成交价格和方向：
>
> ```ts LastTradePriceForAsset Type theme={null}
> type LastTradePriceForAsset = {
>   assetId: ClobAssetId;
>   price: DecimalString;
>   side: OrderSide;
> };
> ```
>
> ```json LastTradePriceForAsset Example theme={null}
> [
>   {
>     "tokenId": "107505882767731489358349912513945399560393482969656700824895970500493757150417",
>     "price": "0.08",
>     "side": "SELL"
>   },
>   {
>     "tokenId": "7305630249804085635496399869905769372294302716159034447326228509068694952392",
>     "price": "0.91",
>     "side": "BUY"
>   }
> ]
> ```

> [tab] Python
>
> 在 `AsyncPublicClient` 或 `AsyncSecureClient` 上调用 `get_last_trade_prices()`，获取多条最新成交记录。同步 `PublicClient` 和 `SecureClient` 也提供相同方法。
>
> ```python theme={null}
> last_trades = await client.get_last_trade_prices(
>     asset_ids=[yes_asset_id, no_asset_id]
> )
>
> # last_trades: tuple[LastTradePriceForAsset, ...]
> ```
>
> 每个 `LastTradePriceForAsset` 都标识相应结果及其成交价格和方向：
>
> ```python LastTradePriceForAsset Type theme={null}
> class LastTradePriceForAsset:
>     asset_id: ClobAssetId
>     price: Decimal
>     side: OrderSide
> ```
>
> ```json LastTradePriceForAsset Example theme={null}
> [
>   {
>     "asset_id": "107505882767731489358349912513945399560393482969656700824895970500493757150417",
>     "price": "0.08",
>     "side": "SELL"
>   },
>   {
>     "asset_id": "7305630249804085635496399869905769372294302716159034447326228509068694952392",
>     "price": "0.91",
>     "side": "BUY"
>   }
> ]
> ```

> [tab] API
>
> 通过一次请求获取多个最新成交价：
>
> ```bash theme={null}
> curl -X POST "https://clob.polymarket.com/last-trades-prices" \
>   -H "Content-Type: application/json" \
>   --data '[{"token_id":"<yes_asset_id>"},{"token_id":"<no_asset_id>"}]'
> ```
>
> 响应会标识每个结果及其成交价格和方向：
>
> ```json theme={null}
> [
>   {
>     "token_id": "107505882767731489358349912513945399560393482969656700824895970500493757150417",
>     "price": "0.08",
>     "side": "SELL"
>   },
>   {
>     "token_id": "7305630249804085635496399869905769372294302716159034447326228509068694952392",
>     "price": "0.91",
>     "side": "BUY"
>   }
> ]
> ```

## 价格历史

查看某个结果代币在所选时间段内的历史价格。

> [tab] TypeScript
>
> 在 `PublicClient` 或 `SecureClient` 上调用 `listPriceHistory()`。选择相对
> 时间窗口、指定时间范围或某个时间点。
>
> ```ts Relative Window theme={null}
> import { PriceHistoryInterval } from "@polymarket/client";
>
> const pages = client.listPriceHistory({
>   assetId: yesAssetId,
>   interval: PriceHistoryInterval.OneDay,
>   bucketSeconds: 3600,
> });
>
> for await (const page of pages) {
>   // page.items: PriceHistoryPoint[]
> }
> ```
>
> ```ts Absolute Range theme={null}
> const pages = client.listPriceHistory({
>   assetId: yesAssetId,
>   start: 1788278400,
>   end: 1788364800,
>   bucketSeconds: 3600,
> });
>
> for await (const page of pages) {
>   // page.items: PriceHistoryPoint[]
> }
> ```
>
> ```ts Point In Time theme={null}
> const pages = client.listPriceHistory({
>   assetId: yesAssetId,
>   asOf: 1788364800,
> });
> const observation = await pages.firstPage();
>
> // observation.items: PriceHistoryPoint[]（至多一个数据点）
> ```
>
> 每个 `PriceHistoryPoint` 携带以毫秒计的观测时间、以十进制字符串表示的价格，
> 以及它的观测粒度：
>
> > [accordion] Output: PriceHistoryPoint
> >
> > ```ts PriceHistoryPoint Type theme={null}
> > type PriceHistoryPoint = {
> >   /** Observation time as Unix epoch milliseconds. */
> >   timestamp: EpochMilliseconds;
> >   /** Observed price, normalized to a decimal string. */
> >   price: DecimalString;
> >   /** Width of the observation window in seconds; zero identifies an exact tick. */
> >   resolutionSeconds: number;
> > };
> > ```
> >
> > ```json PriceHistoryPoint Example theme={null}
> > [
> >   { "timestamp": 1788354000000, "price": "0.255", "resolutionSeconds": 3600 },
> >   { "timestamp": 1788357600000, "price": "0.255", "resolutionSeconds": 3600 },
> >   { "timestamp": 1788361200000, "price": "0.255", "resolutionSeconds": 3600 }
> > ]
> > ```
>
> 数据点按时间升序返回。末尾的真实观测可能不在桶边界上。请读取 `resolutionSeconds`，不要假设点间距固定。
>
> > [accordion] 时间窗口与分辨率
> >
> > * 显式 `start`/`end` 范围最多 15 天。`start` 包含边界，`end` 不包含边界。
> > * `PriceHistoryInterval.Max` 默认以 12 小时粒度返回完整历史。显式设置 `bucketSeconds` 为 10800 或 43200 也可获取完整历史。更细的粒度只返回最近 30 天。
> > * `bucketSeconds` 接受 60 到 86400 秒。`max`/`1m` 的下限为 600，`1w` 的下限为 300。省略时，服务端按时间范围与数据保留期选择粒度。
> > * 1 分钟数据保留 7 天，5 分钟保留 60 天，30 分钟保留 90 天。3 小时与 12 小时数据永久保留。显式请求已过保留期的粒度会返回空页。

> [tab] Python
>
> 在已创建的 `AsyncPublicClient` 或 `AsyncSecureClient` 上调用 `list_price_history()`。
>
> 选择相对时间窗口、指定时间范围或某个时间点。
>
> ```python 相对窗口 theme={null}
> pages = client.list_price_history(
>     asset_id=yes_asset_id,
>     interval="1d",
>     bucket_seconds=3600,
> )
>
> async for page in pages:
>     # page.items: tuple[PriceHistoryPoint, ...]
>     pass
> ```
>
> ```python 指定范围 theme={null}
> pages = client.list_price_history(
>     asset_id=yes_asset_id,
>     start=1788278400,
>     end=1788364800,
>     bucket_seconds=3600,
> )
>
> async for page in pages:
>     # page.items: tuple[PriceHistoryPoint, ...]
>     pass
> ```
>
> ```python 指定时间点 theme={null}
> pages = client.list_price_history(
>     asset_id=yes_asset_id,
>     as_of=1788364800,
> )
> page = await pages.first_page()
> observation = page.items[0] if page.items else None
>
> # observation: PriceHistoryPoint | None
> ```
>
> > [accordion] Output: PriceHistoryPoint
> >
> > ```python PriceHistoryPoint Type theme={null}
> > class PriceHistoryPoint:
> >     timestamp: datetime
> >     price: Decimal
> >     resolution_seconds: int
> > ```
> >
> > ```json PriceHistoryPoint Example theme={null}
> > {
> >   "timestamp": "2026-09-07T17:04:00Z",
> >   "price": "0.955",
> >   "resolution_seconds": 60
> > }
> > ```
>
> 数据按时间从早到晚排列。`timestamp` 是带时区的 `datetime`，`price` 是 `Decimal`。`resolution_seconds` 表示观测窗口的秒数，零表示精确成交时点。
>
> > [accordion] 历史窗口与精度
> >
> > * 指定范围最多跨越 15 天。包含 `start`，不包含 `end`。
> > * `interval`、`start` 和 `as_of` 三选一。使用 `as_of` 时不能设置 `bucket_seconds` 或 `page_size`。
> > * `bucket_seconds` 接受 60 到 86400 秒。`max`、`all` 和 `1m` 的最小值为 600，`1w` 的最小值为 300。不传此参数时由服务选择精度。
> > * 使用 `interval="max"` 并省略 `bucket_seconds`，以默认精度读取完整历史。

> [tab] API
>
> 传入 `token_id` 和恰好一种时间形式：相对窗口 `interval`、绝对范围 `start`
> （可选 `end`，Unix 秒，跨度至多 15 天），或时间点读取 `as_of`。
> `bucket_seconds` 以秒为单位设置桶宽；后续页仅通过 `?cursor=` 获取。
>
> ```bash Relative Window theme={null}
> curl "https://data-api.polymarket.com/v2/prices-history?token_id=$ASSET_ID&interval=1d&bucket_seconds=3600"
> ```
>
> ```bash Absolute Range theme={null}
> curl "https://data-api.polymarket.com/v2/prices-history?token_id=$ASSET_ID&start=1788278400&end=1788364800&bucket_seconds=3600"
> ```
>
> ```bash Point In Time theme={null}
> curl "https://data-api.polymarket.com/v2/prices-history?token_id=$ASSET_ID&as_of=1788364800"
> ```
>
> 响应在 `data` 下包含价格点（最旧在前），并携带游标分页对象：
>
> ```json theme={null}
> {
>   "data": [
>     { "timestamp": 1788354000, "price": 0.255, "resolution_seconds": 3600 },
>     { "timestamp": 1788357600, "price": 0.255, "resolution_seconds": 3600 },
>     { "timestamp": 1788361200, "price": 0.255, "resolution_seconds": 3600 }
>   ],
>   "pagination": {
>     "limit": 3,
>     "has_more": true,
>     "next_cursor": "eyJkYXRhIjp7InR5cGUiOiJwcmljZXNfaGlzdG9yeSI…"
>   }
> }
> ```
>
> 数据点按时间升序返回。末尾的真实观测可能不在桶边界上。请读取 `resolution_seconds`，不要假设点间距固定。
>
> > [accordion] 时间窗口与分辨率
> >
> > * 显式 `start`/`end` 范围最多 15 天。`start` 包含边界，`end` 不包含边界。
> > * `max` 默认以 12 小时粒度返回完整历史。显式设置 `bucket_seconds` 为 10800 或 43200 也可获取完整历史。更细的粒度只返回最近 30 天。
> > * `bucket_seconds` 接受 60 到 86400 秒。`max`/`1m` 的下限为 600，`1w` 的下限为 300。省略时，服务端按时间范围与数据保留期选择粒度。
> > * 1 分钟数据保留 7 天，5 分钟保留 60 天，30 分钟保留 90 天。3 小时与 12 小时数据永久保留。显式请求已过保留期的粒度会返回空页。


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
