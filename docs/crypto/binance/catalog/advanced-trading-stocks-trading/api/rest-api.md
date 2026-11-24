---
exchange: binance
source_url: https://developers.binance.com/en/docs/catalog/advanced-trading-stocks-trading/api/rest-api
api_type: REST
updated_at: 2026-11-24 18:49:16.323166
---

# Stocks Trading REST API

Schema: https://developers.binance.com/en/docs/catalog/advanced-trading-stocks-trading/api/rest-api/1.0.0/schema.yaml

REST APIs for Binance Stocks Trading. All endpoints under `/sapi/v1/equity/*`.

Binance 股票交易 REST API。所有接口位于 `/sapi/v1/equity/*`。

版本: 1.0.0

## 服务地址

- `https://api.binance.com`

## 接口列表

- `GET /sapi/v1/equity/market/exchangeInfo` — Exchange Info (MARKET_DATA)
- `GET /sapi/v1/equity/market/tokenized-assets` — Tokenized Assets (MARKET_DATA)
- `GET /sapi/v1/equity/market/quote` — Latest Quote (MARKET_DATA)
- `POST /sapi/v1/equity/order/place` — Place Equity Order (TRADE)
- `POST /sapi/v1/equity/order/cancel` — Cancel Equity Order (TRADE)
- `POST /sapi/v1/equity/order/cancel-all` — Cancel All Equity Orders (TRADE)
- `GET /sapi/v1/equity/order/open-orders` — Current Open Orders (USER_DATA)
- `GET /sapi/v1/equity/order/history` — Equity Order History (USER_DATA)
- `GET /sapi/v1/equity/order/detail` — Equity Order Detail (USER_DATA)
- `GET /sapi/v1/equity/trade/history` — Equity Trade History (USER_DATA)
- `POST /sapi/v1/equity/tokenized/mint` — Tokenized Mint (TRADE)
- `POST /sapi/v1/equity/tokenized/redeem` — Tokenized Redeem (TRADE)
- `GET /sapi/v1/equity/tokenized/convert-status` — Tokenized Convert Status (USER_DATA)
- `GET /sapi/v1/equity/tokenized/history` — Tokenized Convert History (USER_DATA)
- `POST /sapi/v1/equity/account/disclaimer` — Sign US Equity Disclaimer (TRADE)
- `POST /sapi/v1/equity/listenKey` — Create / Renew Listen Key (USER_STREAM)

## Exchange Info (MARKET_DATA)（交易规则与 Symbol 列表 (MARKET_DATA)）

`GET /sapi/v1/equity/market/exchangeInfo`

Returns current exchange trading rules and the list of tradable US-equity symbols. MARKET_DATA endpoint — requires an API key (`X-MBX-APIKEY`) but no signature. Response is served from a server-side cache.

返回当前交易规则与可交易美股 Symbol 列表。MARKET_DATA 接口——需携带 API key（`X-MBX-APIKEY`），但无需签名。响应来自服务端缓存。

权重: 1

Operation ID: `exchangeInfo`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string |  | Filter to a single US-equity ticker, e.g. `AAPL`. When omitted, returns all active symbols. An unknown ticker returns an empty `symbols` array (HTTP 200), not an error.<br>过滤单只美股 ticker，例如 `AAPL`。省略时返回所有上架 symbol。未知 ticker 返回空 `symbols` 数组（HTTP 200），而非报错。<br>例: `AAPL` |

### 响应 200：Exchange Info / 交易规则与 Symbol 列表

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| timezone | string |  | Always `UTC`.<br>固定为 `UTC`。<br>例: `UTC` |
| symbols | object[] |  | List of tradable symbols with trading rules.<br>可交易 symbol 列表及其交易规则。 |
| symbols[].symbol | string |  | US-equity ticker, e.g. `AAPL`.<br>美股 ticker，例如 `AAPL`。<br>例: `AAPL` |
| symbols[].tradability | string |  | Trading direction allowed — one of `BUY_SELL` / `BUY` / `SELL` / `NONE`.<br>允许的交易方向，取值之一：`BUY_SELL` / `BUY` / `SELL` / `NONE`。<br>枚举: `BUY_SELL`, `BUY`, `SELL`, `NONE`<br>例: `BUY_SELL` |
| symbols[].tradabilityUpdateTime | integer (int64) |  | Last time the `tradability` value was updated (ms epoch).<br>`tradability` 值最后更新时间（毫秒时间戳）。<br>例: `1735900000000` |
| symbols[].overnightSupported | boolean |  | Whether the symbol supports overnight trading.<br>该 symbol 是否支持夜盘交易。<br>例: `True` |
| symbols[].fractionable | boolean |  | Whether fractional shares are supported during the regular session.<br>常规时段是否支持分数股。<br>例: `True` |
| symbols[].fractionableEh | boolean |  | Whether fractional shares are supported during extended hours.<br>延长时段是否支持分数股。<br>例: `False` |
| symbols[].extendedSession | boolean |  | Whether extended-session trading is enabled.<br>是否启用延长时段交易。<br>例: `True` |
| symbols[].maxNumOrders | integer |  | Maximum number of open orders a user may have for this symbol.<br>用户对此 symbol 可持有的最大挂单数。<br>例: `200` |
| symbols[].stepSize | string |  | Lot size — minimum increment for `quantity`.<br>`quantity` 的最小步长（手数）。<br>例: `0.000000001` |
| symbols[].multiplierUp | string |  | Upper price multiplier limit relative to reference.<br>相对参考价格的上限倍率。<br>例: `1.10` |
| symbols[].multiplierDown | string |  | Lower price multiplier limit relative to reference.<br>相对参考价格的下限倍率。<br>例: `0.90` |
| symbols[].minQty | string |  | Minimum allowed `quantity`.<br>允许的最小 `quantity`。<br>例: `0.000000001` |
| symbols[].maxQty | string |  | Maximum allowed `quantity`.<br>允许的最大 `quantity`。<br>例: `100000.00000000` |
| symbols[].minNotional | string |  | Minimum order notional (USD).<br>最小订单名义金额（USD）。<br>例: `1.00` |
| symbols[].maxNotional | string |  | Maximum order notional (USD).<br>最大订单名义金额（USD）。<br>例: `1000000.00` |
| symbols[].listingTime | integer (int64) |  | Listing timestamp (ms epoch).<br>上架时间（毫秒时间戳）。<br>例: `1700000000000` |
| symbols[].delistingTime | integer (int64) |  | Scheduled delisting timestamp (ms epoch); `null` if not scheduled for delisting.<br>计划下架时间（毫秒时间戳）；未计划下架时为 `null`。<br>例: `None` |

## Tokenized Assets (MARKET_DATA)（代币化资产列表 (MARKET_DATA)）

`GET /sapi/v1/equity/market/tokenized-assets`

Returns the list of all tokenized assets currently available for mint / redeem, together with each asset's underlying equity symbol and conversion multiplier. MARKET_DATA endpoint — requires an API key (`X-MBX-APIKEY`) but no signature. Response is served from a server-side cache.

返回当前可铸造 / 赎回的全部代币化资产列表，包含每个资产的标的美股 Symbol 和转换倍数。MARKET_DATA 接口——需携带 API key（`X-MBX-APIKEY`），但无需签名。响应来自服务端缓存。

权重: 1

Operation ID: `tokenizedAssets`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 响应 200：Tokenized Assets / 代币化资产列表

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].assetCode | string |  | Tokenized asset code, e.g. `AAPLB`.<br>代币化资产代码，例如 `AAPLB`。<br>例: `AAPLB` |
| [].assetName | string |  | Human-readable display name of the tokenized asset.<br>代币化资产的人类可读名称。<br>例: `Apple Inc. Tokenized Stock` |
| [].underlyingEquitySymbol | string |  | Underlying US-equity ticker, e.g. `AAPL`. Use this when calling `/tokenized/mint` or `/tokenized/redeem`.<br>标的美股 ticker，例如 `AAPL`。调用 `/tokenized/mint` 或 `/tokenized/redeem` 时使用此字段。<br>例: `AAPL` |
| [].multiplier | string |  | Conversion multiplier between the underlying equity and the tokenized asset.<br>标的股票与代币化资产之间的转换倍数。<br>例: `1` |
| [].multiplierValid | boolean |  | Whether the multiplier is currently valid and applicable.<br>当前倍数是否有效且可适用。<br>例: `True` |

## Latest Quote (MARKET_DATA)（最新报价 (MARKET_DATA)）

`GET /sapi/v1/equity/market/quote`

Returns the latest best bid / best ask for a single US-equity ticker. The returned value is at most ~5 seconds stale. Returns an **empty response body** (not the literal `null`) when no quote is available for the supplied ticker (e.g. the ticker is unknown, halted, or de-listed).

返回单只美股的最优买一 / 卖一报价，数据最多延迟约 5 秒。当指定 ticker 没有可用报价时（如未知、停牌或已下架）返回**空响应体**（非字面 `null`，客户端需容错）。

权重: 1

Operation ID: `latestQuote`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | US-equity ticker, e.g. `AAPL`, `TSLA`. Case-insensitive; uppercased server-side.<br>美股 ticker，例如 `AAPL`、`TSLA`。大小写不敏感，服务端统一转为大写。<br>例: `AAPL` |

### 响应 200：Latest Quote / 最新报价

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string |  | US-equity ticker.<br>美股 ticker。<br>例: `AAPL` |
| bidPrice | string |  | Best bid price (USD).<br>最优买一价（USD）。<br>例: `180.50` |
| askPrice | string |  | Best ask price (USD).<br>最优卖一价（USD）。<br>例: `180.52` |
| bidSize | integer |  | Best bid size (shares).<br>最优买一量（股数）。<br>例: `100` |
| askSize | integer |  | Best ask size (shares).<br>最优卖一量（股数）。<br>例: `200` |

## Place Equity Order (TRADE)（下单 (TRADE)）

`POST /sapi/v1/equity/order/place`

Place a new equity order. Supports all combinations of `LIMIT` /
`MARKET` × `BUY` / `SELL`. For `LIMIT BUY` orders the commission fee is
automatically computed and reserved by the server at placement time —
callers submit `price` and `quantity` only, no `fee` field is required.


**Field combination matrix**


| Side | OrderType | Required | Forbidden |
| ---- | --------- | -------- | --------- |
| BUY | LIMIT | `price`, `quantity`, `tradingSession` | `notional` |
| BUY | MARKET | `notional` | `price`, `quantity`, `tradingSession` |
| SELL | LIMIT | `price`, `quantity`, `tradingSession` | `notional` |
| SELL | MARKET | `quantity` | `price`, `notional`, `tradingSession` |


**Fractional shares**: when `quantity` has a decimal component, or an
order is placed by `notional`, it is treated as a fractional-share
order. A fractional-share `GTC` order must be paired with
`tradingSession = EXTENDED` or `24H`.


Rate limit: 200 requests / min (UID).

下一笔股票订单。支持 `LIMIT` / `MARKET` × `BUY` / `SELL`
的所有组合。对于 `LIMIT BUY`
订单，服务端在下单时自动计算并冻结手续费——调用方只需提交 `price` 和
`quantity`，无需传 `fee` 字段。


**字段组合矩阵**


| Side | OrderType | 必填 | 禁传 |
| ---- | --------- | ---- | ---- |
| BUY | LIMIT | `price`、`quantity`、`tradingSession` | `notional` |
| BUY | MARKET | `notional` | `price`、`quantity`、`tradingSession` |
| SELL | LIMIT | `price`、`quantity`、`tradingSession` | `notional` |
| SELL | MARKET | `quantity` | `price`、`notional`、`tradingSession` |


**碎股**：当 `quantity` 带小数，或使用 `notional`
下单时，订单被视为碎股订单。碎股 `GTC` 订单必须搭配 `tradingSession =
EXTENDED` 或 `24H`。


频率限制：200 次 / 分钟（UID）。

权重: 1

Operation ID: `placeEquityOrder`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | US stock ticker, e.g. `AAPL`, `TSLA`. Must be a tradable US-equity symbol — verify via `/sapi/v1/equity/market/exchangeInfo`. Tokenization enablement (verifiable via `/sapi/v1/equity/market/tokenized-assets`) is *not* required; non-tokenized symbols are accepted and settle as traditional underlying-equity trades. The `tokenize` parameter only takes effect on tokenization-enabled symbols and is silently ignored otherwise.<br>美股 ticker，如 `AAPL`、`TSLA`。必须是可交易的美股 symbol——可通过 `/sapi/v1/equity/market/exchangeInfo` 查询。是否已开启代币化（可通过 `/sapi/v1/equity/market/tokenized-assets` 查询）*并非*必要条件；未开启代币化的 symbol 同样可以下单，并以传统的底层股票交易方式结算。`tokenize` 参数仅在 symbol 已开启代币化时生效，否则会被静默忽略。<br>例: `AAPL` |
| quoteAsset | query | string |  | Quote asset. Defaults to `USDC`; must be within the server's allowed set.<br>计价资产，默认 `USDC`；必须在服务端允许集合内。<br>例: `USDC` |
| side | query | string | 是 | `BUY` / `SELL`.<br>`BUY` / `SELL`。<br>枚举: `BUY`, `SELL`<br>例: `BUY` |
| orderType | query | string | 是 | `MARKET` / `LIMIT`.<br>`MARKET` / `LIMIT`。<br>枚举: `MARKET`, `LIMIT`<br>例: `LIMIT` |
| price | query | string |  | **Required** for `LIMIT`; **forbidden** for `MARKET`. Maximum 2 decimal places.<br>`LIMIT` **必填**；`MARKET` **禁传**。最多 2 位小数。<br>例: `180.50` |
| quantity | query | string |  | **Required** for `LIMIT` (both sides) and `SELL MARKET`; **forbidden** for `BUY MARKET`.<br>`LIMIT`（买卖两侧）与 `SELL MARKET` **必填**；`BUY MARKET` **禁传**。<br>例: `1` |
| notional | query | string |  | **Required** for `BUY MARKET`; **forbidden** for `LIMIT` and `SELL MARKET`.<br>`BUY MARKET` **必填**；`LIMIT` 与 `SELL MARKET` **禁传**。<br>例: `1000.00` |
| timeInForce | query | string |  | `DAY` (default) / `GTC`. `GTC` is only supported for `LIMIT` orders; a fractional-share `GTC` order must be paired with `tradingSession = EXTENDED` or `24H`.<br>`DAY`（默认）/ `GTC`。`GTC` 仅支持 `LIMIT` 订单；碎股 `GTC` 订单必须搭配 `tradingSession = EXTENDED` 或 `24H`。<br>枚举: `DAY`, `GTC`<br>例: `DAY` |
| tradingSession | query | string |  | `RTH` / `EXTENDED` / `24H`. **Required** for `LIMIT`; **forbidden** for `MARKET`.<br>`RTH` / `EXTENDED` / `24H`。`LIMIT` **必填**；`MARKET` **禁传**。<br>枚举: `RTH`, `EXTENDED`, `24H`<br>例: `RTH` |
| walletType | query | string |  | Payment wallet for `BUY` orders: `CARD` (default) / `MAIN`. `SELL` orders always settle to `CARD`.<br>`BUY` 侧付款钱包：`CARD`（默认）/ `MAIN`。`SELL` 侧固定结算至 `CARD`。<br>枚举: `CARD`, `MAIN`<br>例: `CARD` |
| clientOrderId | query | string |  | Client-supplied order id. Format `^[a-zA-Z0-9-_]{32,36}$`. Auto-generated when omitted.<br>客户端自定义订单 ID。格式 `^[a-zA-Z0-9-_]{32,36}$`。不传则服务端自动生成。<br>例: `web_2c9c92b74f1e4a7c8f3b9e1a2d3c4b5a` |
| tokenize | query | boolean |  | Whether to tokenize the purchased stock asset upon settlement. Default `true`. Only takes effect when the symbol is tokenization-enabled (check via `/market/tokenized-assets`); silently ignored for non-tokenized symbols, which always settle as traditional underlying-equity trades.<br>结算后是否将买入的股票资产代币化。默认 `true`。仅在 symbol 已开启代币化（可通过 `/market/tokenized-assets` 查询）时生效；对于未开启代币化的 symbol 会被静默忽略，此类订单始终以传统的底层股票交易方式结算。<br>例: `True` |
| tokenizedAssetSettleWalletType | query | string |  | Wallet that receives the tokenized asset minted after the order fills. `MAIN` = Spot wallet, `CARD` = Funding wallet. Default `CARD`. Only applies when `side` = `BUY` and `tokenize` = `true`; ignored for `SELL` or `tokenize` = `false`. If `MAIN` is sent while Spot wallet settlement is not enabled, the request is rejected as an illegal parameter.<br>订单成交后铸造的代币化资产所划入的钱包。`MAIN` = 现货钱包，`CARD` = 资金钱包。默认 `CARD`。仅在 `side` = `BUY` 且 `tokenize` = `true` 时生效；`SELL` 或 `tokenize` = `false` 时忽略。若未开启现货钱包结算而传入 `MAIN`，请求将因参数非法被拒绝。<br>枚举: `MAIN`, `CARD`<br>默认: `CARD`<br>例: `CARD` |
| recvWindow | query | integer (int64) |  | The value cannot be greater than `60000`.<br>赋值不能大于 `60000`。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Timestamp in milliseconds.<br>时间戳（毫秒）。<br>例: `1770736694138` |

### 响应 200：Place Equity Order / 下单响应

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| status | string |  | Acknowledgement code: `S` = accepted, `F` = failed. Not an order lifecycle status — to poll lifecycle, call `/order/detail` or `/order/history`.<br>请求确认码：`S` = 已接受，`F` = 失败。这不是订单生命周期状态——如需查询生命周期，请调用 `/order/detail` 或 `/order/history`。<br>例: `S` |
| orderId | string |  | Order id (UUID).<br>订单 ID（UUID）。<br>例: `c3c58f49-7b0d-4b9e-a2db-1a2f9a3b8c71` |
| clientOrderId | string |  | Echoes the supplied or server-generated client order id.<br>回显提交的或服务端生成的客户端订单 ID。<br>例: `web_2c9c92b74f1e4a7c8f3b9e1a2d3c4b5a` |

## Cancel Equity Order (TRADE)（撤单 (TRADE)）

`POST /sapi/v1/equity/order/cancel`

Cancel a single open order by its `orderId`.

按 `orderId` 撤销单笔挂单。

权重: 1

Operation ID: `cancelEquityOrder`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| orderId | query | string | 是 | Equity order id returned by `/order/place` or a query endpoint.<br>由 `/order/place` 或查询接口返回的股票订单 ID。<br>例: `c3c58f49-7b0d-4b9e-a2db-1a2f9a3b8c71` |
| recvWindow | query | integer (int64) |  | The value cannot be greater than `60000`.<br>赋值不能大于 `60000`。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Timestamp in milliseconds.<br>时间戳（毫秒）。<br>例: `1770736694138` |

### 响应 200：Cancel Equity Order / 撤单响应

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderId | string |  | Echoes the requested order id.<br>回显请求的订单 ID。<br>例: `c3c58f49-7b0d-4b9e-a2db-1a2f9a3b8c71` |
| status | string |  | Acknowledgement code: `S` = cancel accepted by upstream, `F` = cancel failed. Not an order lifecycle status — use `/order/detail` for lifecycle poll.<br>请求确认码：`S` = 撤单已被上游接受，`F` = 撤单失败。这不是订单生命周期状态——如需查询生命周期请使用 `/order/detail`。<br>例: `S` |

## Cancel All Equity Orders (TRADE)（全部撤单 (TRADE)）

`POST /sapi/v1/equity/order/cancel-all`

Cancel all open orders for the caller. No request body is required — the scope is all of the caller's open orders. The downstream service handles idempotency; to inspect per-order outcomes, query `/order/history` after the call.

撤销调用方所有未成交订单。无需额外请求参数——范围固定为调用方所有未成交订单。下游服务保证幂等性；如需查看每笔订单的结果，请在调用后查询 `/order/history`。

权重: 1

Operation ID: `cancelAllEquityOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | The value cannot be greater than `60000`.<br>赋值不能大于 `60000`。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Timestamp in milliseconds.<br>时间戳（毫秒）。<br>例: `1770736694138` |

### 响应 200：Cancel All Equity Orders / 全部撤单响应

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| success | boolean |  | `true` when the cancel-all request was accepted by upstream. Per-order outcomes live in `/order/history`.<br>撤单请求被上游接受时为 `true`。每笔订单的结果请查询 `/order/history`。<br>例: `True` |

## Current Open Orders (USER_DATA)（当前挂单 (USER_DATA)）

`GET /sapi/v1/equity/order/open-orders`

Query all unfinished (open) orders for the caller. No business parameters are needed — user identity is derived from the signature.

查询调用方所有未完成（挂单中）的股票订单。无需业务参数——用户身份由签名推导。

权重: 1

Operation ID: `currentOpenOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | The value cannot be greater than `60000`.<br>赋值不能大于 `60000`。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Timestamp in milliseconds.<br>时间戳（毫秒）。<br>例: `1770736694138` |

### 响应 200：Current Open Orders / 当前挂单响应

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].orderId | string |  | Equity order id.<br>股票订单 ID。<br>例: `c3c58f49-7b0d-4b9e-a2db-1a2f9a3b8c71` |
| [].symbol | string |  | US-equity ticker.<br>美股 ticker。<br>例: `AAPL` |
| [].quote | string |  | Quote asset (e.g. `USDC`).<br>计价资产（如 `USDC`）。<br>例: `USDC` |
| [].side | string |  | `BUY` / `SELL`.<br>`BUY` / `SELL`。<br>例: `BUY` |
| [].orderType | string |  | `MARKET` / `LIMIT`.<br>`MARKET` / `LIMIT`。<br>例: `LIMIT` |
| [].limitPrice | string |  | Limit price (USD). Non-null for `LIMIT` orders, `null` for `MARKET`.<br>限价（USD）。`LIMIT` 订单非空，`MARKET` 订单为 `null`。<br>例: `180.50` |
| [].avgFilledPrice | string |  | Average fill price (USD). `null` until the first fill.<br>平均成交价（USD）。首笔成交前为 `null`。<br>例: `None` |
| [].qty | string |  | Requested quantity. `null` for `BUY MARKET` (use `notional` instead).<br>请求股数。`BUY MARKET` 时为 `null`（使用 `notional` 替代）。<br>例: `1` |
| [].notional | string |  | Requested notional. Non-null for `BUY MARKET`; `null` otherwise.<br>请求名义金额。`BUY MARKET` 非空；其他情况为 `null`。<br>例: `None` |
| [].filledQty | string |  | Cumulative filled quantity.<br>累计成交数量。<br>例: `0` |
| [].filledTotal | string |  | Cumulative filled notional. Populated only for `BUY MARKET`.<br>累计成交名义金额，仅 `BUY MARKET` 有值。<br>例: `None` |
| [].fee | string |  | Total commission fee (USD).<br>总手续费（USD）。<br>例: `0` |
| [].session | string |  | Trading session the order was placed under: `RTH` / `EXTENDED` / `24H`. `null` for `MARKET` orders.<br>下单时的交易时段：`RTH` / `EXTENDED` / `24H`。`MARKET` 订单为 `null`。<br>例: `RTH` |
| [].status | string |  | Order lifecycle status — one of `NEW` / `ACCEPTED` / `PARTIALLY_FILLED` / `FILLED` / `CANCELED` / `EXPIRED` / `REJECTED`.<br>订单生命周期状态，取值之一：`NEW` / `ACCEPTED` / `PARTIALLY_FILLED` / `FILLED` / `CANCELED` / `EXPIRED` / `REJECTED`。<br>例: `NEW` |
| [].createdAt | integer (int64) |  | Order creation time (ms epoch).<br>订单创建时间（毫秒时间戳）。<br>例: `1735900000000` |
| [].updatedAt | integer (int64) |  | Last update time (ms epoch).<br>最后更新时间（毫秒时间戳）。<br>例: `1735900000000` |

## Equity Order History (USER_DATA)（订单历史 (USER_DATA)）

`GET /sapi/v1/equity/order/history`

Paged order history for the caller. Filters by symbol, order type, side, status, and time range.

调用方的分页订单历史，可按 symbol、订单类型、方向、状态和时间段过滤。

权重: 1

Operation ID: `equityOrderHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string |  | US-equity ticker filter, e.g. `NVDA`.<br>美股 ticker 过滤，例如 `NVDA`。<br>例: `NVDA` |
| orderType | query | string |  | Order type filter: `MARKET` / `LIMIT`.<br>订单类型过滤：`MARKET` / `LIMIT`。<br>枚举: `MARKET`, `LIMIT`<br>例: `LIMIT` |
| side | query | string |  | Side filter: `BUY` / `SELL`.<br>方向过滤：`BUY` / `SELL`。<br>枚举: `BUY`, `SELL`<br>例: `BUY` |
| orderStatus | query | string |  | Comma-separated status filter. Allowed values: `FILLED`, `PARTIALLY_FILLED`, `CANCELED`, `EXPIRED`, `REJECTED`.<br>逗号分隔的状态过滤，允许值：`FILLED`、`PARTIALLY_FILLED`、`CANCELED`、`EXPIRED`、`REJECTED`。<br>例: `FILLED,CANCELED` |
| startTime | query | integer (int64) | 是 | Start time (ms epoch).<br>开始时间（毫秒时间戳）。<br>例: `1735800000000` |
| endTime | query | integer (int64) | 是 | End time (ms epoch).<br>结束时间（毫秒时间戳）。<br>例: `1735900000000` |
| current | query | integer |  | Page number, 1-based. Default `1`.<br>页码，从 1 起，默认 `1`。<br>例: `1` |
| size | query | integer |  | Page size. Default `20`, max `100`.<br>每页大小，默认 `20`，最大 `100`。<br>例: `20` |
| recvWindow | query | integer (int64) |  | The value cannot be greater than `60000`.<br>赋值不能大于 `60000`。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Timestamp in milliseconds.<br>时间戳（毫秒）。<br>例: `1770736694138` |

### 响应 200：Equity Order History / 订单历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| total | integer (int64) |  | Total number of rows matching the filter.<br>符合过滤条件的总行数。<br>例: `2` |
| page | integer |  | Current page (echoes `current`).<br>当前页码（回显 `current`）。<br>例: `1` |
| size | integer |  | Current page size (echoes `size`).<br>当前页大小（回显 `size`）。<br>例: `20` |
| rows | object[] |  | Order rows on this page. Empty array if nothing matches.<br>本页订单列表，无匹配时为空数组。 |
| rows[].orderId | string |  | Equity order id.<br>股票订单 ID。<br>例: `c3c58f49-7b0d-4b9e-a2db-1a2f9a3b8c71` |
| rows[].symbol | string |  | US-equity ticker.<br>美股 ticker。<br>例: `AAPL` |
| rows[].quote | string |  | Quote asset (e.g. `USDC`).<br>计价资产（如 `USDC`）。<br>例: `USDC` |
| rows[].side | string |  | `BUY` / `SELL`.<br>`BUY` / `SELL`。<br>例: `BUY` |
| rows[].orderType | string |  | `MARKET` / `LIMIT`; stop-limit orders placed in the app are `STOP_LOSS_LIMIT` / `TAKE_PROFIT_LIMIT`, and stop-limit orders not placed through Binance are `STOP_LIMIT`.<br>`MARKET` / `LIMIT`；在 App 内下的止损限价 / 止盈限价单为 `STOP_LOSS_LIMIT` / `TAKE_PROFIT_LIMIT`，未经币安下单链路的止损限价单为 `STOP_LIMIT`。<br>例: `LIMIT` |
| rows[].limitPrice | string |  | Limit price (USD). Returned for `LIMIT` and stop-limit orders; `MARKET` orders have no limit price (`null`).<br>限价（USD）。`LIMIT` 及止损限价 / 止盈限价订单返回；`MARKET` 订单没有限价（`null`）。<br>例: `180.50` |
| rows[].avgFilledPrice | string |  | Average fill price (USD) as reported by the broker, returned for all order types. `null` until the first fill.<br>平均成交价（USD，券商回报），所有订单类型都返回；首笔成交前为 `null`。<br>例: `180.48` |
| rows[].qty | string |  | Requested quantity. `null` for `BUY MARKET` (use `notional` instead).<br>请求股数。`BUY MARKET` 时为 `null`（使用 `notional` 替代）。<br>例: `1` |
| rows[].notional | string |  | Requested notional. Non-null for `BUY MARKET`; `null` otherwise.<br>请求名义金额。`BUY MARKET` 非空；其他情况为 `null`。<br>例: `None` |
| rows[].filledQty | string |  | Cumulative filled quantity.<br>累计成交数量。<br>例: `1` |
| rows[].filledTotal | string |  | Cumulative filled notional. Populated only for `BUY MARKET`.<br>累计成交名义金额，仅 `BUY MARKET` 有值。<br>例: `None` |
| rows[].fee | string |  | Total commission fee (USD).<br>总手续费（USD）。<br>例: `0.10` |
| rows[].session | string |  | Trading session the order was placed under: `RTH` / `EXTENDED` / `24H`. `null` for `MARKET` orders.<br>下单时的交易时段：`RTH` / `EXTENDED` / `24H`。`MARKET` 订单为 `null`。<br>例: `RTH` |
| rows[].status | string |  | Order lifecycle status — one of `NEW` / `ACCEPTED` / `PARTIALLY_FILLED` / `FILLED` / `CANCELED` / `EXPIRED` / `REJECTED`.<br>订单生命周期状态，取值之一：`NEW` / `ACCEPTED` / `PARTIALLY_FILLED` / `FILLED` / `CANCELED` / `EXPIRED` / `REJECTED`。<br>例: `FILLED` |
| rows[].createdAt | integer (int64) |  | Order creation time (ms epoch).<br>订单创建时间（毫秒时间戳）。<br>例: `1735900000000` |
| rows[].updatedAt | integer (int64) |  | Last update time (ms epoch).<br>最后更新时间（毫秒时间戳）。<br>例: `1735900120000` |

## Equity Order Detail (USER_DATA)（订单详情 (USER_DATA)）

`GET /sapi/v1/equity/order/detail`

Returns a single order along with its trade execution list. Callers can only read their own orders — the user identity is derived from the signed request.

返回单笔订单及其成交明细列表。调用方只能查询自己的订单——用户身份从签名请求中解析。

权重: 1

Operation ID: `equityOrderDetail`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| orderId | query | string |  | Equity order id. Either `orderId` or `clientOrderId` must be provided.<br>股票订单 ID。`orderId` 与 `clientOrderId` 必须提供其中一个。<br>例: `c3c58f49-7b0d-4b9e-a2db-1a2f9a3b8c71` |
| clientOrderId | query | string |  | Client-supplied order id. Either `orderId` or `clientOrderId` must be provided.<br>客户端自定义订单 ID。`orderId` 与 `clientOrderId` 必须提供其中一个。<br>例: `web_2c9c92b74f1e4a7c8f3b9e1a2d3c4b5a` |
| recvWindow | query | integer (int64) |  | The value cannot be greater than `60000`.<br>赋值不能大于 `60000`。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Timestamp in milliseconds.<br>时间戳（毫秒）。<br>例: `1770736694138` |

### 响应 200：Equity Order Detail / 订单详情

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderId | string |  | Equity order id.<br>股票订单 ID。<br>例: `c3c58f49-7b0d-4b9e-a2db-1a2f9a3b8c71` |
| clientOrderId | string |  | Client-supplied order id. Present only in Order Detail, not in Order History.<br>客户端自定义订单 ID。仅订单详情接口返回，订单历史接口不包含此字段。<br>例: `web_2c9c92b74f1e4a7c8f3b9e1a2d3c4b5a` |
| symbol | string |  | US-equity ticker.<br>美股 ticker。<br>例: `AAPL` |
| quote | string |  | Quote asset.<br>计价资产。<br>例: `USDC` |
| side | string |  | `BUY` / `SELL`.<br>`BUY` / `SELL`。<br>例: `BUY` |
| orderType | string |  | `MARKET` / `LIMIT`.<br>`MARKET` / `LIMIT`。<br>例: `LIMIT` |
| limitPrice | string |  | Limit price (USD). Non-null for `LIMIT`, `null` for `MARKET`.<br>限价（USD）。`LIMIT` 非空，`MARKET` 为 `null`。<br>例: `180.50` |
| avgFilledPrice | string |  | Average fill price (USD). Only present when the order has at least one fill.<br>平均成交价（USD）。仅当订单至少有一笔成交时返回。<br>例: `180.48` |
| qty | string |  | Requested quantity.<br>请求股数。<br>例: `1` |
| notional | string |  | Requested notional.<br>请求名义金额。<br>例: `None` |
| filledQty | string |  | Cumulative filled quantity.<br>累计成交数量。<br>例: `1` |
| filledTotal | string |  | Cumulative filled notional.<br>累计成交名义金额。<br>例: `None` |
| fee | string |  | Total commission fee (USD).<br>总手续费（USD）。<br>例: `0.10` |
| session | string |  | Trading session.<br>交易时段。<br>例: `RTH` |
| status | string |  | Order lifecycle status.<br>订单生命周期状态。<br>例: `FILLED` |
| createdAt | integer (int64) |  | Order creation time (ms epoch).<br>订单创建时间（毫秒时间戳）。<br>例: `1735900000000` |
| updatedAt | integer (int64) |  | Last update time (ms epoch).<br>最后更新时间（毫秒时间戳）。<br>例: `1735900120000` |
| trades | object[] |  | Trade executions for this order, most recent first. Empty array when no fills.<br>此订单的成交明细，最新成交在前。无成交时为空数组。 |
| trades[].executionId | string |  | Execution (fill) id.<br>成交（逐笔）ID。<br>例: `exec-20260504-0001` |
| trades[].executionAt | integer (int64) |  | Execution time (ms epoch).<br>成交时间（毫秒时间戳）。<br>例: `1735900115000` |
| trades[].price | string |  | Fill price for this execution (USD).<br>此笔成交价格（USD）。<br>例: `180.48` |
| trades[].qty | string |  | Fill quantity.<br>成交数量。<br>例: `1` |

## Equity Trade History (USER_DATA)（成交历史 (USER_DATA)）

`GET /sapi/v1/equity/trade/history`

Paged equity trade (per-fill) history for the caller. Each row is one execution, not one order — a partially filled order produces multiple rows. Filters by symbol, side, specific `orderId`, and time range.

调用方的分页逐笔成交历史。每行为一笔执行，而非一笔订单——部分成交订单会产生多行。可按 symbol、方向、指定 `orderId` 和时间段过滤。

权重: 1

Operation ID: `equityTradeHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string |  | US-equity ticker filter, e.g. `NVDA`.<br>美股 ticker 过滤，例如 `NVDA`。<br>例: `NVDA` |
| side | query | string |  | Side filter: `BUY` / `SELL`.<br>方向过滤：`BUY` / `SELL`。<br>枚举: `BUY`, `SELL`<br>例: `BUY` |
| orderId | query | string |  | Narrow the result to executions of a single order.<br>将结果限定为单笔订单的成交记录。<br>例: `c3c58f49-7b0d-4b9e-a2db-1a2f9a3b8c71` |
| startTime | query | integer (int64) | 是 | Start time (ms epoch).<br>开始时间（毫秒时间戳）。<br>例: `1735800000000` |
| endTime | query | integer (int64) | 是 | End time (ms epoch).<br>结束时间（毫秒时间戳）。<br>例: `1735900000000` |
| current | query | integer |  | Page number, 1-based. Default `1`.<br>页码，从 1 起，默认 `1`。<br>例: `1` |
| size | query | integer |  | Page size. Default `20`, max `100`.<br>每页大小，默认 `20`，最大 `100`。<br>例: `20` |
| recvWindow | query | integer (int64) |  | The value cannot be greater than `60000`.<br>赋值不能大于 `60000`。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Timestamp in milliseconds.<br>时间戳（毫秒）。<br>例: `1770736694138` |

### 响应 200：Equity Trade History / 成交历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| total | integer (int64) |  | Total number of rows matching the filter.<br>符合过滤条件的总行数。<br>例: `1` |
| page | integer |  | Current page.<br>当前页码。<br>例: `1` |
| size | integer |  | Current page size.<br>当前页大小。<br>例: `20` |
| rows | object[] |  | Trade rows on this page. Empty when nothing matches.<br>本页成交列表，无匹配时为空数组。 |
| rows[].executionId | string |  | Execution (per-fill) id.<br>逐笔成交 ID。<br>例: `exec-20260504-0001` |
| rows[].orderId | string |  | The owning order's id.<br>所属订单 ID。<br>例: `c3c58f49-7b0d-4b9e-a2db-1a2f9a3b8c71` |
| rows[].symbol | string |  | US-equity ticker.<br>美股 ticker。<br>例: `AAPL` |
| rows[].quote | string |  | Quote asset.<br>计价资产。<br>例: `USDC` |
| rows[].side | string |  | `BUY` / `SELL`.<br>`BUY` / `SELL`。<br>例: `BUY` |
| rows[].orderType | string |  | `MARKET` / `LIMIT`.<br>`MARKET` / `LIMIT`。<br>例: `LIMIT` |
| rows[].price | string |  | Execution price (USD).<br>成交价格（USD）。<br>例: `180.50` |
| rows[].qty | string |  | Executed quantity.<br>成交数量。<br>例: `1` |
| rows[].total | string |  | Notional of this execution (`qty × price`).<br>此笔成交名义金额（`qty × price`）。<br>例: `180.50` |
| rows[].executionAt | integer (int64) |  | Execution time (ms epoch).<br>成交时间（毫秒时间戳）。<br>例: `1735900115000` |
| rows[].updatedAt | integer (int64) |  | Last update time (ms epoch).<br>最后更新时间（毫秒时间戳）。<br>例: `1735900115200` |

## Tokenized Mint (TRADE)（铸造代币化资产 (TRADE)）

`POST /sapi/v1/equity/tokenized/mint`

Mint a tokenized asset from an underlying equity holding. The caller's underlying equity (e.g. `AAPL`) is burned (or locked), and the corresponding tokenized asset (e.g. `AAPLB`) is credited. The tokenized asset is resolved server-side from `underlyingAsset`; callers only provide the underlying ticker and quantity. Mint is asynchronous: the endpoint returns an `issuerRequestId` immediately with a transient status; poll `/tokenized/convert-status` to observe the terminal state, or inspect `/tokenized/history` for the full record. Rate limit: 50 requests / min (UID).

从标的股票持仓铸造代币化资产。调用方的标的股票（如 `AAPL`）被销毁（或锁定），对应代币化资产（如 `AAPLB`）被划入账户。目标代币由服务端根据 `underlyingAsset` 查找；调用方只需提供标的 ticker 和数量。铸造为异步操作：接口立即返回 `issuerRequestId` 及临时状态；轮询 `/tokenized/convert-status` 查看终态，或查询 `/tokenized/history` 获取完整记录。频率限制：50 次 / 分钟（UID）。

权重: 1

Operation ID: `tokenizedMint`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| underlyingAsset | query | string | 是 | Underlying US-equity ticker, e.g. `AAPL`, `TSLA`. Resolved against the active-symbol list; unknown tickers return `-26004`. The target tokenized asset is looked up from this field via `/market/tokenized-assets`.<br>标的美股 ticker，例如 `AAPL`、`TSLA`。在上架 symbol 列表中解析；未知 ticker 返回 `-26004`。目标代币化资产通过 `/market/tokenized-assets` 接口根据此字段查找。<br>例: `AAPL` |
| underlyingAssetAmount | query | string | 是 | Quantity of the underlying asset to mint from. Must be > 0.<br>铸造所需标的资产数量，必须大于 0。<br>例: `1` |
| clientOrderId | query | string |  | Client order id for idempotency. Format `^[a-zA-Z0-9-_]{32,36}$`. Auto-generated when omitted.<br>客户端幂等 ID，格式 `^[a-zA-Z0-9-_]{32,36}$`，不传则自动生成。<br>例: `mint-client-id-32chars-0000000001` |
| tokenizedAssetSettleWalletType | query | string |  | Wallet that receives the minted tokenized asset. `MAIN` = Spot wallet, `CARD` = Funding wallet. Default `CARD`. If `MAIN` is sent while Spot wallet settlement is not enabled, the request is rejected as an illegal parameter.<br>接收所铸造代币化资产的钱包。`MAIN` = 现货钱包，`CARD` = 资金钱包。默认 `CARD`。若未开启现货钱包结算而传入 `MAIN`，请求将因参数非法被拒绝。<br>枚举: `MAIN`, `CARD`<br>默认: `CARD`<br>例: `CARD` |
| recvWindow | query | integer (int64) |  | The value cannot be greater than `60000`.<br>赋值不能大于 `60000`。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Timestamp in milliseconds.<br>时间戳（毫秒）。<br>例: `1770736694138` |

### 响应 200：Tokenized Mint / 铸造响应

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| issuerRequestId | string |  | Server-assigned convert request id. Use it to poll `/tokenized/convert-status`.<br>服务端分配的转换请求 ID，用于轮询 `/tokenized/convert-status`。<br>例: `mint-20260505-8f3b9e1a2d3c4b5a` |
| status | string |  | Convert status code: `P` = processing, `S` = success, `F` = failed.<br>转换状态码：`P` = 处理中，`S` = 成功，`F` = 失败。<br>枚举: `P`, `S`, `F`<br>例: `P` |
| tokenizedAssetSettleWalletType | string |  | The wallet the tokenized asset is settled in: `MAIN` = Spot wallet, `CARD` = Funding wallet.<br>代币化资产实际结算所用的钱包：`MAIN` = 现货钱包，`CARD` = 资金钱包。<br>例: `CARD` |

## Tokenized Redeem (TRADE)（赎回代币化资产 (TRADE)）

`POST /sapi/v1/equity/tokenized/redeem`

Redeem a tokenized asset back into the underlying equity. The caller's tokenized asset (e.g. `AAPLB`) is burned, and the corresponding underlying equity (e.g. `AAPL`) is released. The underlying asset is resolved server-side from `tokenizedAsset`; callers only provide the tokenized asset and quantity. Redeem is asynchronous: the endpoint returns an `issuerRequestId` immediately with a transient status; poll `/tokenized/convert-status` to observe the terminal state, or inspect `/tokenized/history` for the full record. Rate limit: 200 requests / min (UID).

将代币化资产赎回为标的股票。调用方的代币化资产（如 `AAPLB`）被销毁，对应标的股票（如 `AAPL`）被释放。目标标的由服务端根据 `tokenizedAsset` 查找；调用方只需提供代币化资产和数量。赎回为异步操作：接口立即返回 `issuerRequestId` 及临时状态；轮询 `/tokenized/convert-status` 查看终态，或查询 `/tokenized/history` 获取完整记录。频率限制：200 次 / 分钟（UID）。

权重: 1

Operation ID: `tokenizedRedeem`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| tokenizedAsset | query | string | 是 | Tokenized asset to redeem, e.g. `AAPLB`. Not a US-equity ticker — this is the on-chain tokenized asset identifier. Unknown asset returns `-1102` (the message currently says the parameter was empty/malformed, but it was in fact sent — it is simply unknown). The target underlying ticker is looked up from this field via `/market/tokenized-assets`.<br>要赎回的代币化资产，例如 `AAPLB`。这不是美股 ticker，而是链上代币化资产标识符。未知资产返回 `-1102`（当前报错信息称参数为空/畸形，但其实已发送、只是不存在）。目标标的 ticker 通过 `/market/tokenized-assets` 接口根据此字段查找。<br>例: `AAPLB` |
| tokenizedAssetAmount | query | string | 是 | Quantity of the tokenized asset to redeem. Must be > 0.<br>要赎回的代币化资产数量，必须大于 0。<br>例: `1` |
| clientOrderId | query | string |  | Client order id for idempotency. Format `^[a-zA-Z0-9-_]{32,36}$`. Auto-generated when omitted.<br>客户端幂等 ID，格式 `^[a-zA-Z0-9-_]{32,36}$`，不传则自动生成。<br>例: `redeem-client-id-32chars-000000001` |
| tokenizedAssetSettleWalletType | query | string |  | Wallet the tokenized asset is deducted from on redeem. `MAIN` = Spot wallet, `CARD` = Funding wallet. Default `CARD`. If `MAIN` is sent while Spot wallet settlement is not enabled, the request is rejected as an illegal parameter.<br>赎回时扣减代币化资产的钱包。`MAIN` = 现货钱包，`CARD` = 资金钱包。默认 `CARD`。若未开启现货钱包结算而传入 `MAIN`，请求将因参数非法被拒绝。<br>枚举: `MAIN`, `CARD`<br>默认: `CARD`<br>例: `CARD` |
| recvWindow | query | integer (int64) |  | The value cannot be greater than `60000`.<br>赋值不能大于 `60000`。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Timestamp in milliseconds.<br>时间戳（毫秒）。<br>例: `1770736694138` |

### 响应 200：Tokenized Redeem / 赎回响应

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| issuerRequestId | string |  | Server-assigned convert request id. Use it to poll `/tokenized/convert-status`.<br>服务端分配的转换请求 ID，用于轮询 `/tokenized/convert-status`。<br>例: `redeem-20260505-a1b2c3d4e5f6` |
| status | string |  | Convert status code: `P` = processing, `S` = success, `F` = failed.<br>转换状态码：`P` = 处理中，`S` = 成功，`F` = 失败。<br>枚举: `P`, `S`, `F`<br>例: `P` |
| tokenizedAssetSettleWalletType | string |  | The wallet the tokenized asset is settled in: `MAIN` = Spot wallet, `CARD` = Funding wallet.<br>代币化资产实际结算所用的钱包：`MAIN` = 现货钱包，`CARD` = 资金钱包。<br>例: `CARD` |

## Tokenized Convert Status (USER_DATA)（代币化转换状态 (USER_DATA)）

`GET /sapi/v1/equity/tokenized/convert-status`

Query the current status of a single mint / redeem request by its `issuerRequestId`. Returns an empty object when no record matches (caller's ID scope only).

通过 `issuerRequestId` 查询单笔铸造 / 赎回请求的当前状态。无匹配记录时返回空对象（仅限调用方 ID 范围）。

权重: 1

Operation ID: `tokenizedConvertStatus`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| issuerRequestId | query | string | 是 | Convert request id returned by `/tokenized/mint` or `/redeem`.<br>由 `/tokenized/mint` 或 `/tokenized/redeem` 返回的转换请求 ID。<br>例: `mint-20260505-8f3b9e1a2d3c4b5a` |
| convertType | query | string | 是 | `MINT` or `REDEEM`.<br>`MINT` 或 `REDEEM`。<br>枚举: `MINT`, `REDEEM`<br>例: `MINT` |
| recvWindow | query | integer (int64) |  | The value cannot be greater than `60000`.<br>赋值不能大于 `60000`。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Timestamp in milliseconds.<br>时间戳（毫秒）。<br>例: `1770736694138` |

### 响应 200：Tokenized Convert Status / 代币化转换状态

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| underlyingAsset | string |  | Underlying US-equity ticker, e.g. `AAPL`.<br>标的美股 ticker，例如 `AAPL`。<br>例: `AAPL` |
| underlyingAssetAmount | string |  | Quantity of the underlying asset involved.<br>涉及的标的资产数量。<br>例: `1.000000000` |
| tokenizedAsset | string |  | Tokenized asset, e.g. `AAPLB`.<br>代币化资产，例如 `AAPLB`。<br>例: `AAPLB` |
| tokenizedAssetAmount | string |  | Quantity of the tokenized asset involved.<br>涉及的代币化资产数量。<br>例: `1.000000000` |
| issuerRequestId | string |  | Echoes the requested id.<br>回显请求的 ID。<br>例: `mint-20260505-8f3b9e1a2d3c4b5a` |
| convertType | string |  | `MINT` or `REDEEM`.<br>`MINT` 或 `REDEEM`。<br>例: `MINT` |
| status | string |  | Convert status: `P` = processing, `S` = success, `F` = failed.<br>转换状态：`P` = 处理中，`S` = 成功，`F` = 失败。<br>枚举: `P`, `S`, `F`<br>例: `S` |
| createdAt | integer (int64) |  | Creation time (ms epoch).<br>创建时间（毫秒时间戳）。<br>例: `1735900000000` |
| updatedAt | integer (int64) |  | Last update time (ms epoch).<br>最后更新时间（毫秒时间戳）。<br>例: `1735900060000` |
| tokenizedAssetSettleWalletType | string |  | The wallet the tokenized asset is settled in: `MAIN` = Spot wallet, `CARD` = Funding wallet.<br>代币化资产实际结算所用的钱包：`MAIN` = 现货钱包，`CARD` = 资金钱包。<br>例: `CARD` |

## Tokenized Convert History (USER_DATA)（代币化转换历史 (USER_DATA)）

`GET /sapi/v1/equity/tokenized/history`

Paged history of mint / redeem conversions for the caller. Cursor-style pagination — supply the `nextLastId` from the previous page's response to fetch the next page.

调用方的分页铸造 / 赎回转换历史。游标分页——提供上一页响应中的 `nextLastId` 作为 `lastId` 来获取下一页。

权重: 1

Operation ID: `tokenizedConvertHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| startTime | query | integer (int64) |  | Start time (ms epoch).<br>开始时间（毫秒时间戳）。<br>例: `1735800000000` |
| endTime | query | integer (int64) |  | End time (ms epoch).<br>结束时间（毫秒时间戳）。<br>例: `1735900000000` |
| lastId | query | integer (int64) |  | Last record id from the previous page. Omit (or leave unset) to fetch the first page.<br>上一页最后一条记录的 ID。省略（或不传）表示从第一页开始。<br>例: `10019` |
| size | query | integer |  | Page size. Default `20`, max `100`.<br>每页大小，默认 `20`，最大 `100`。<br>例: `20` |
| recvWindow | query | integer (int64) |  | The value cannot be greater than `60000`.<br>赋值不能大于 `60000`。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Timestamp in milliseconds.<br>时间戳（毫秒）。<br>例: `1770736694138` |

### 响应 200：Tokenized Convert History / 代币化转换历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| rows | object[] |  | Convert history rows on this page. Empty array if nothing matches.<br>本页转换历史列表，无匹配时为空数组。 |
| rows[].underlyingAsset | string |  | Underlying US-equity ticker, e.g. `AAPL`.<br>标的美股 ticker，例如 `AAPL`。<br>例: `AAPL` |
| rows[].underlyingAssetAmount | string |  | Quantity of the underlying asset involved.<br>涉及的标的资产数量。<br>例: `1.000000000` |
| rows[].tokenizedAsset | string |  | Tokenized asset, e.g. `AAPLB`.<br>代币化资产，例如 `AAPLB`。<br>例: `AAPLB` |
| rows[].tokenizedAssetAmount | string |  | Quantity of the tokenized asset involved.<br>涉及的代币化资产数量。<br>例: `1.000000000` |
| rows[].issuerRequestId | string |  | Convert request id.<br>转换请求 ID。<br>例: `mint-20260505-8f3b9e1a2d3c4b5a` |
| rows[].convertType | string |  | `MINT` or `REDEEM`.<br>`MINT` 或 `REDEEM`。<br>例: `MINT` |
| rows[].status | string |  | Convert status: `P` = processing, `S` = success, `F` = failed.<br>转换状态：`P` = 处理中，`S` = 成功，`F` = 失败。<br>枚举: `P`, `S`, `F`<br>例: `S` |
| rows[].createdAt | integer (int64) |  | Creation time (ms epoch).<br>创建时间（毫秒时间戳）。<br>例: `1735900000000` |
| rows[].updatedAt | integer (int64) |  | Last update time (ms epoch).<br>最后更新时间（毫秒时间戳）。<br>例: `1735900060000` |
| rows[].tokenizedAssetSettleWalletType | string |  | The wallet the tokenized asset is settled in: `MAIN` = Spot wallet, `CARD` = Funding wallet.<br>代币化资产实际结算所用的钱包：`MAIN` = 现货钱包，`CARD` = 资金钱包。<br>例: `CARD` |
| hasMore | boolean |  | `true` when more pages exist — pass `nextLastId` as `lastId` on the next request.<br>还有更多页时为 `true`——将 `nextLastId` 作为下次请求的 `lastId`。<br>例: `True` |
| nextLastId | integer (int64) |  | Pass this value as `lastId` on the next request to get the following page.<br>将此值作为下次请求的 `lastId` 以获取下一页。<br>例: `10020` |

## Sign US Equity Disclaimer (TRADE)（签署美股免责声明 (TRADE)）

`POST /sapi/v1/equity/account/disclaimer`

Records the user's acknowledgement and acceptance of the US equity disclaimer. This must be completed before the account can access certain US equity trading features. The acceptance is tied to the account associated with the API key.

记录用户对美股免责声明的确认与接受。账户必须先完成此步骤，才能使用部分美股交易功能。接受状态与该 API key 关联的账户绑定。

权重: 1

Operation ID: `signUsEquityDisclaimer`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | The value cannot be greater than `60000`.<br>赋值不能大于 `60000`。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Timestamp in milliseconds.<br>时间戳（毫秒）。<br>例: `1770736694138` |

### 响应 200：Sign US Equity Disclaimer / 签署美股免责声明响应

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| success | boolean |  | `true` = acceptance recorded successfully.<br>`true` = 已成功记录接受。<br>例: `True` |

## Create / Renew Listen Key (USER_STREAM)（创建 / 续期 Listen Key (USER_STREAM)）

`POST /sapi/v1/equity/listenKey`

Create a new stock user-data-stream `listenKey`, or renew an existing one. Calling this endpoint for the same user with an active `listenKey` extends its validity; if there is no active key, a new one is issued. Use the returned `listenKey` to subscribe to the stock user data stream.

创建新的 股票用户数据流 `listenKey`，或对已有的 `listenKey` 续期。对同一用户调用此接口且有活跃 `listenKey` 时，会延长其有效期；无活跃 key 时则创建新 key。使用返回的 `listenKey` 订阅 股票用户数据流。

权重: 1

Operation ID: `createRenewListenKey`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | The value cannot be greater than `60000`.<br>赋值不能大于 `60000`。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Timestamp in milliseconds.<br>时间戳（毫秒）。<br>例: `1770736694138` |

### 响应 200：Create / Renew Listen Key / 创建 / 续期 Listen Key 响应

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| listenKey | string |  | Session identifier for the stock user data stream.<br>股票用户数据流的会话标识符。<br>例: `pqia91ma19a5s61cv6a81va65sdf19v8a65s1cv1zuz3ee1c5xz2ef6ad7` |