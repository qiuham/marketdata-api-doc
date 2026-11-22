---
exchange: binance
source_url: https://developers.binance.com/en/docs/catalog/web3-wallet-prediction-trading/api/rest-api
api_type: REST
updated_at: 2026-11-22 18:46:24.608482
---

# Prediction Trading REST API

Schema: https://developers.binance.com/en/docs/catalog/web3-wallet-prediction-trading/api/rest-api/1.0.0/schema.yaml

Place and manage prediction market orders, query positions, and transfer funds via the Prediction Trading REST API.

通過預測市場交易 REST API 下單、管理預測訂單、查詢持倉並進行資金劃轉。

版本: 1.0.0

## 服务地址

- `https://api.binance.com`
- `https://api-gcp.binance.com`
- `https://api1.binance.com`
- `https://api2.binance.com`
- `https://api3.binance.com`
- `https://api4.binance.com`

## 接口列表

- `GET /sapi/v1/w3w/wallet/prediction/category/list` — List Prediction Categories
- `GET /sapi/v1/w3w/wallet/prediction/market/list` — List Prediction Markets
- `GET /sapi/v1/w3w/wallet/prediction/market/search` — Market Search
- `GET /sapi/v1/w3w/wallet/prediction/market/detail` — Get Market Detail
- `GET /sapi/v1/w3w/wallet/prediction/order-book` — Query Order Book
- `GET /sapi/v1/w3w/wallet/prediction/order-book/last-trade-price` — Query Last Trade Price
- `GET /sapi/v1/w3w/wallet/prediction/wallet/list` — List Prediction Wallets (PREDICTION_TRADE)
- `GET /sapi/v1/w3w/wallet/prediction/pnl/portfolio` — Get Portfolio (PREDICTION_TRADE)
- `GET /sapi/v1/w3w/wallet/prediction/quota/limit/status` — Get Quota Status (PREDICTION_TRADE)
- `GET /sapi/v1/w3w/wallet/prediction/balance/payment-options` — Query Payment Option Balances (PREDICTION_TRADE)
- `POST /sapi/v1/w3w/wallet/prediction/trade/get-quote` — Get Quote (PREDICTION_TRADE)
- `POST /sapi/v1/w3w/wallet/prediction/trade/place-order-bundle` — Place Order (PREDICTION_TRADE)
- `POST /sapi/v1/w3w/wallet/prediction/trade/batch-cancel` — Batch Cancel Orders (PREDICTION_TRADE)
- `GET /sapi/v1/w3w/wallet/prediction/order/list` — Query Active Orders (PREDICTION_TRADE)
- `GET /sapi/v1/w3w/wallet/prediction/order/history` — Query Order History (PREDICTION_TRADE)
- `GET /sapi/v1/w3w/wallet/prediction/position/list` — Query Positions (PREDICTION_TRADE)
- `GET /sapi/v1/w3w/wallet/prediction/position/filter` — Query Positions by Filter (PREDICTION_TRADE)
- `GET /sapi/v1/w3w/wallet/prediction/position/token` — Get Position by Token (PREDICTION_TRADE)
- `GET /sapi/v1/w3w/wallet/prediction/pnl/query` — Query PnL (PREDICTION_TRADE)
- `GET /sapi/v1/w3w/wallet/prediction/position/settled-history` — Query Settled Position History (PREDICTION_TRADE)
- `POST /sapi/v1/w3w/wallet/prediction/batch-redeem` — Batch Redeem (PREDICTION_TRADE)
- `GET /sapi/v1/w3w/wallet/prediction/redeem/status` — Get Redeem Status (PREDICTION_TRADE)
- `POST /sapi/v1/w3w/wallet/prediction/transfer/inbound` — Create Inbound Transfer (PREDICTION_TRADE)
- `POST /sapi/v1/w3w/wallet/prediction/transfer/outbound` — Create Outbound Transfer (PREDICTION_TRADE)
- `GET /sapi/v1/w3w/wallet/prediction/transfer/list` — Query Transfer List (PREDICTION_TRADE)
- `GET /sapi/v1/w3w/wallet/prediction/transfer/status` — Query Transfer Status (PREDICTION_TRADE)
- `POST /sapi/v1/w3w/wallet/prediction/deposit/apply` — Apply MM Deposit (PREDICTION_TRADE)
- `POST /sapi/v1/w3w/wallet/prediction/withdraw/apply` — Apply MM Withdraw (PREDICTION_TRADE)
- `POST /sapi/v1/w3w/wallet/prediction/otc/blocktrade/create` — Create OTC Blocktrade (PREDICTION_TRADE)
- `POST /sapi/v1/w3w/wallet/prediction/otc/blocktrade/list` — List OTC Blocktrades (PREDICTION_TRADE)
- `POST /sapi/v1/w3w/wallet/prediction/otc/blocktrade/detail` — Get OTC Blocktrade Detail (PREDICTION_TRADE)
- `POST /sapi/v1/w3w/wallet/prediction/otc/blocktrade/events` — Get OTC Blocktrade Events (PREDICTION_TRADE)
- `POST /sapi/v1/w3w/wallet/prediction/otc/blocktrade/preview` — Preview OTC Blocktrade (PREDICTION_TRADE)
- `POST /sapi/v1/w3w/wallet/prediction/otc/blocktrade/fulfil` — Fulfil OTC Blocktrade (PREDICTION_TRADE)
- `POST /sapi/v1/w3w/wallet/prediction/otc/blocktrade/remove` — Remove OTC Blocktrades (PREDICTION_TRADE)
- `POST /sapi/v1/w3w/wallet/prediction/otc/blocktrade/reserved-balances` — Get OTC Reserved Balances (PREDICTION_TRADE)

## List Prediction Categories（獲取預測分類列表）

`GET /sapi/v1/w3w/wallet/prediction/category/list`

Get all available prediction market categories (L1 and L2).

獲取所有可用的預測市場分類（一級和二級分類）。

Operation ID: `listPredictionCategories`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：List Prediction Categories / 獲取預測分類列表

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| categories | object[] |  |  |
| categories[].id | string |  | 例: `crypto` |
| categories[].name | string |  | 例: `Crypto` |
| categories[].icon | string |  | 例: `crypto_icon` |
| categories[].order | integer |  | 例: `1` |
| categories[].subcategories | object[] |  |  |
| categories[].subcategories[].id | string |  | 例: `up-down` |
| categories[].subcategories[].name | string |  | 例: `Up/Down` |
| categories[].subcategories[].icon | string |  | 例: `updown_icon` |
| categories[].subcategories[].order | integer |  | 例: `1` |

## List Prediction Markets（獲取預測市場列表）

`GET /sapi/v1/w3w/wallet/prediction/market/list`

Get a paginated list of prediction market topics, with optional category and sort filters.

獲取預測市場主題的分頁列表，支援分類篩選和排序。

Operation ID: `listPredictionMarkets`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| l1Category | query | string |  | Level-1 category filter<br>一級分類篩選<br>例: `crypto` |
| l2Category | query | string |  | Level-2 category filter<br>二級分類篩選<br>例: `up-down` |
| sortBy | query | string |  | Sort field. Enum: `RECOMMENDED`, `VOLUME`, `PARTICIPANTS`, `CREATED_TIME`, `END_DATE`<br>排序欄位。列舉值：`RECOMMENDED`、`VOLUME`、`PARTICIPANTS`、`CREATED_TIME`、`END_DATE`<br>枚举: `RECOMMENDED`, `VOLUME`, `PARTICIPANTS`, `CREATED_TIME`, `END_DATE`<br>例: `VOLUME` |
| orderBy | query | string |  | Sort direction. Enum: `ASC`, `DESC`<br>排序方向。列舉值：`ASC`、`DESC`<br>枚举: `ASC`, `DESC`<br>例: `DESC` |
| offset | query | integer (int32) |  | Pagination offset. Default `0`<br>分頁偏移量，預設 `0`<br>默认: `0`<br>例: `0` |
| limit | query | integer (int32) |  | Page size. Default `20`, range 1–100<br>每頁數量，預設 `20`，範圍 1–100<br>默认: `20`<br>例: `20` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：List Prediction Markets / 獲取預測市場列表

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| marketTopics | object[] |  |  |
| marketTopics[].marketTopicId | integer (int64) |  | 例: `4229564` |
| marketTopics[].vendor | string |  | 例: `PREDICT_FUN` |
| marketTopics[].chainId | string |  | 例: `56` |
| marketTopics[].slug | string |  | 例: `btc-price-1h-up-or-down` |
| marketTopics[].title | string |  | 例: `BTC Price 1h Up or Down?` |
| marketTopics[].question | string |  | 例: `Will BTC price go UP in the next 1 hour?` |
| marketTopics[].description | string |  | 例: `Resolves YES if BTC spot price is higher than the starting price at resolution time.` |
| marketTopics[].imageUrl | string |  | 例: `https://cdn.example.com/prediction/btc-1h.png` |
| marketTopics[].topicType | string |  | 例: `FLAT` |
| marketTopics[].chartType | string |  | 例: `CRYPTO_UP_DOWN` |
| marketTopics[].symbol | string |  | 例: `BTCUSDT` |
| marketTopics[].participantCount | integer |  | 例: `3420` |
| marketTopics[].collateral | string |  | 例: `USDT` |
| marketTopics[].feeRateBps | integer |  | 例: `200` |
| marketTopics[].slippageBps | integer |  | 例: `1200` |
| marketTopics[].isYieldBearing | boolean |  | 例: `False` |
| marketTopics[].tradeVolume | string |  | 例: `158234.56` |
| marketTopics[].liquidity | string |  | 例: `45000.00` |
| marketTopics[].publishedAt | integer (int64) |  | 例: `1748100000000` |
| marketTopics[].startDate | integer (int64) |  | 例: `1748131200000` |
| marketTopics[].endDate | integer (int64) |  | 例: `1748134800000` |
| marketTopics[].status | string |  | 例: `REGISTERED` |
| marketTopics[].markets | object[] |  |  |
| total | integer |  | 例: `128` |
| offset | integer |  | 例: `0` |
| limit | integer |  | 例: `20` |
| hasMore | boolean |  | 例: `True` |

## Market Search（市場搜尋）

`GET /sapi/v1/w3w/wallet/prediction/market/search`

Semantic search for prediction market topics by keyword.

通過關鍵詞對預測市場主題進行語義搜尋。

Operation ID: `marketSearch`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| query | query | string | 是 | Search keyword. Not blank<br>搜尋關鍵詞，不可為空<br>例: `BTC price` |
| topK | query | integer (int32) |  | Max number of results to return. Default `20`, range 1–50<br>最多返回結果數量，預設 `20`，範圍 1–50<br>默认: `20`<br>例: `20` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Market Search / 市場搜尋

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].marketTopicId | integer (int64) |  | 例: `4229564` |
| [].vendor | string |  | 例: `PREDICT_FUN` |
| [].chainId | string |  | 例: `56` |
| [].slug | string |  | 例: `btc-price-1h-up-or-down` |
| [].title | string |  | 例: `BTC Price 1h Up or Down?` |
| [].question | string |  | 例: `Will BTC price go UP in the next 1 hour?` |
| [].description | string |  | 例: `Resolves YES if BTC spot price is higher than the starting price.` |
| [].topicType | string |  | 例: `FLAT` |
| [].chartType | string |  | 例: `CRYPTO_UP_DOWN` |
| [].symbol | string |  | 例: `BTCUSDT` |
| [].participantCount | integer |  | 例: `3420` |
| [].collateral | string |  | 例: `USDT` |
| [].tradeVolume | string |  | 例: `158234.56` |
| [].liquidity | string |  | 例: `45000.00` |
| [].startDate | integer (int64) |  | 例: `1748131200000` |
| [].endDate | integer (int64) |  | 例: `1748134800000` |
| [].status | string |  | 例: `REGISTERED` |
| [].markets | object[] |  |  |

## Get Market Detail（獲取市場詳情）

`GET /sapi/v1/w3w/wallet/prediction/market/detail`

Get full details for a specific prediction market topic, including variant data and timeline.

獲取指定預測市場主題的完整詳情，包括變體資料和時間線。

Operation ID: `getMarketDetail`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| marketTopicId | query | integer (int64) | 是 | Market topic ID. Must be > 0<br>市場主題 ID，必須大於 0<br>例: `4229564` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Market Detail / 獲取市場詳情

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| marketTopicId | integer (int64) |  | 例: `4229564` |
| vendor | string |  | 例: `PREDICT_FUN` |
| chainId | string |  | 例: `56` |
| slug | string |  | 例: `btc-price-1h-up-or-down` |
| title | string |  | 例: `BTC Price 1h Up or Down?` |
| question | string |  | 例: `Will BTC price go UP in the next 1 hour?` |
| description | string |  | 例: `Resolves YES if BTC spot price is higher than the starting price at resolution time.` |
| imageUrl | string |  | 例: `https://cdn.example.com/prediction/btc-1h.png` |
| topicType | string |  | 例: `FLAT` |
| chartType | string |  | 例: `CRYPTO_UP_DOWN` |
| symbol | string |  | 例: `BTCUSDT` |
| variantData | object |  |  |
| variantData.type | string |  | 例: `CRYPTO_UP_DOWN` |
| variantData.startPrice | string |  | 例: `67890.12` |
| variantData.endPrice | string |  | 例: `None` |
| variantData.priceFeedId | string |  | 例: `0xpricefeedid123` |
| variantData.priceFeedProvider | string |  | 例: `BINANCE` |
| variantData.priceFeedSymbol | string |  | 例: `BTCUSDT` |
| participantCount | integer |  | 例: `3420` |
| collateral | string |  | 例: `USDT` |
| feeRateBps | integer |  | 例: `200` |
| slippageBps | integer |  | 例: `1200` |
| isYieldBearing | boolean |  | 例: `False` |
| tradeVolume | string |  | 例: `158234.56` |
| liquidity | string |  | 例: `45000.00` |
| publishedAt | integer (int64) |  | 例: `1748100000000` |
| startDate | integer (int64) |  | 例: `1748131200000` |
| endDate | integer (int64) |  | 例: `1748134800000` |
| status | string |  | 例: `REGISTERED` |
| timeline | object[] |  |  |
| timeline[].marketTopicId | integer (int64) |  | 例: `4229560` |
| timeline[].startDate | integer (int64) |  | 例: `1748127600000` |
| timeline[].endDate | integer (int64) |  | 例: `1748131200000` |
| markets | object[] |  |  |
| markets[].marketId | integer (int64) |  | 例: `5567895` |
| markets[].externalId | string |  | 例: `ext_001` |
| markets[].title | string |  | 例: `UP` |
| markets[].question | string |  | 例: `Will BTC go UP?` |
| markets[].description | string |  | 例: `Resolves YES if BTC price increases.` |
| markets[].conditionId | string |  | 例: `0xabc123` |
| markets[].status | string |  | 枚举: `REGISTERED`, `RESOLVED`, `PAUSED`, `CLOSED`<br>例: `REGISTERED` |
| markets[].tradingStatus | string |  | 枚举: `OPEN`, `MATCHING_NOT_ENABLED`, `CANCEL_ONLY`, `CLOSED`<br>例: `OPEN` |
| markets[].tradeVolume | string |  | 例: `90000.00` |
| markets[].liquidity | string |  | 例: `25000.00` |
| markets[].decimalPrecision | integer |  | Price precision of the market, in decimal places. The price tick is 10 to the power of minus `decimalPrecision`, for example `2` means a tick of 0.01. A limit price that is not on the tick is truncated down<br>市場的價格精度（小數位數）。價格步長為 10 的負 `decimalPrecision` 次方，例如 `2` 表示步長 0.01。不在步長上的限價會被向下截斷<br>例: `2` |
| markets[].outcomes | object[] |  |  |
| markets[].outcomes[].name | string |  | 例: `YES` |
| markets[].outcomes[].price | string |  | 例: `0.52` |
| markets[].outcomes[].chance | string |  | 例: `0.52` |
| markets[].outcomes[].index | integer |  | 例: `0` |
| markets[].outcomes[].tokenId | string |  | 例: `112233` |
| markets[].outcomes[].winner | boolean |  | Whether this outcome won. Returned only after the market is resolved. More than one outcome can be `true` when the payout is split<br>該結果是否勝出。僅在市場裁定後返回。兌付拆分時可能有多個結果為 `true`<br>例: `True` |

## Query Order Book（查詢訂單簿）

`GET /sapi/v1/w3w/wallet/prediction/order-book`

Get the current order book (bids and asks) for a specific prediction market outcome token.

獲取指定預測市場結果 Token 的當前訂單簿（買單和賣單）。

Operation ID: `queryOrderBook`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| vendor | query | string | 是 | Vendor identifier (e.g. `predict_fun`)<br>供應商標識（例如 `predict_fun`）<br>例: `predict_fun` |
| marketId | query | integer (int64) | 是 | Market ID. Must be > 0<br>市場 ID，必須大於 0<br>例: `5567895` |
| tokenId | query | string | 是 | Prediction outcome token ID<br>預測結果 Token ID<br>例: `112233` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Query Order Book / 查詢訂單簿

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| outcome | string |  | 例: `YES` |
| tokenId | string |  | 例: `112233` |
| timestamp | integer (int64) |  | 例: `1748131800000` |
| bids | object[] |  |  |
| bids[].price | string |  | 例: `0.51` |
| bids[].size | string |  | 例: `5000.00` |
| asks | object[] |  |  |
| asks[].price | string |  | 例: `0.52` |
| asks[].size | string |  | 例: `3000.00` |

## Query Last Trade Price（查詢最新成交價）

`GET /sapi/v1/w3w/wallet/prediction/order-book/last-trade-price`

Get the most recent trade price for a prediction market.

獲取預測市場的最新成交價。

Operation ID: `queryLastTradePrice`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| marketId | query | integer (int64) | 是 | Market ID. Must be > 0<br>市場 ID，必須大於 0<br>例: `5567895` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Query Last Trade Price / 查詢最新成交價

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| marketId | integer (int64) |  | 例: `5567895` |
| lastTradePrice | string |  | 例: `0.52` |

## List Prediction Wallets (PREDICTION_TRADE)（獲取預測錢包列表 (PREDICTION_TRADE)）

`GET /sapi/v1/w3w/wallet/prediction/wallet/list`

Get all prediction wallets registered for the authenticated user.

獲取當前使用者已註冊的所有預測錢包。

Operation ID: `listPredictionWallets`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用於請求簽名的 Unix 時間戳，單位為毫秒. 該值必須反映客戶端當前時間，並會在簽名介面中由伺服器進行校驗.<br>例: `1770736694138` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>請求有效時間視窗（毫秒）<br>例: `5000` |

### 响应 200：List Prediction Wallets / 獲取預測錢包列表

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| wallets | object[] |  |  |
| wallets[].walletAddress | string |  | 例: `0x12e32db8817e292508c34111cbc4b23340df542c` |
| wallets[].walletId | string |  | 例: `5b5c1ec3be4e4416a5872b21c1ca5d20` |
| wallets[].registeredTime | integer (int64) |  | 例: `1748000000000` |

## Get Portfolio (PREDICTION_TRADE)（獲取投資組合 (PREDICTION_TRADE)）

`GET /sapi/v1/w3w/wallet/prediction/pnl/portfolio`

Get the authenticated user's prediction portfolio overview including active positions count, aggregated PnL, and full position list.

獲取當前使用者預測投資組合概覽，包括活躍持倉數量、彙總盈虧及完整持倉列表。

Operation ID: `getPortfolio`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| walletAddress | query | string | 是 | User's prediction wallet address<br>使用者預測錢包地址<br>例: `0x12e32db8817e292508c34111cbc4b23340df542c` |
| tokenId | query | string |  | Filter by prediction token ID<br>按預測 Token ID 篩選<br>例: `112233` |
| marketId | query | integer (int64) |  | Filter by market ID. Must be > 0<br>按市場 ID 篩選，必須大於 0<br>例: `5567895` |
| marketTopicId | query | integer (int64) |  | Filter by market topic ID. Must be > 0<br>按市場主題 ID 篩選，必須大於 0<br>例: `4229564` |
| activeOnly | query | boolean |  | If `true`, return only active (unresolved) positions<br>若為 `true`，僅返回活躍（未結算）持倉<br>例: `False` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用於請求簽名的 Unix 時間戳，單位為毫秒. 該值必須反映客戶端當前時間，並會在簽名介面中由伺服器進行校驗.<br>例: `1770736694138` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>請求有效時間視窗（毫秒）<br>例: `5000` |

### 响应 200：Get Portfolio / 獲取投資組合

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| chainId | string |  | 例: `56` |
| walletAddress | string |  | 例: `0x12e32db8817e292508c34111cbc4b23340df542c` |
| activePositionsCount | integer |  | 例: `3` |
| totalRealizedPnl | string |  | 例: `120.50` |
| totalUnrealizedPnl | string |  | 例: `15.30` |
| totalPnl | string |  | 例: `135.80` |
| totalCostBasis | string |  | 例: `450.00` |
| totalCurrentValue | string |  | 例: `465.30` |
| positions | object[] |  |  |
| positions[].id | integer (int64) |  | 例: `10001` |
| positions[].walletAddress | string |  | 例: `0x12e32db8817e292508c34111cbc4b23340df542c` |
| positions[].marketTopicId | integer (int64) |  | 例: `4229564` |
| positions[].marketId | integer (int64) |  | 例: `5567895` |
| positions[].tokenId | string |  | 例: `112233` |
| positions[].vendor | string |  | 例: `PREDICT_FUN` |
| positions[].currentShares | string |  | 例: `1923.07` |
| positions[].avgPrice | string |  | 例: `0.52` |
| positions[].currentPrice | string |  | 例: `0.55` |
| positions[].realizedPnl | string |  | 例: `0.00` |
| positions[].unrealizedPnl | string |  | 例: `0.06` |
| positions[].totalPnl | string |  | 例: `0.06` |
| positions[].pnlPercentage | string |  | 例: `6.00` |
| positions[].isResolved | boolean |  | 例: `False` |

## Get Quota Status (PREDICTION_TRADE)（查詢配額限制狀態 (PREDICTION_TRADE)）

`GET /sapi/v1/w3w/wallet/prediction/quota/limit/status`

Query the current user's daily trading quota limit and remaining allowance for prediction markets.

查詢當前使用者預測市場的每日交易配額限制及剩餘額度。

Operation ID: `getQuotaStatus`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用於請求簽名的 Unix 時間戳，單位為毫秒. 該值必須反映客戶端當前時間，並會在簽名介面中由伺服器進行校驗.<br>例: `1770736694138` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>請求有效時間視窗（毫秒）<br>例: `5000` |

### 响应 200：Get Quota Status / 查詢配額限制狀態

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| dailyLimit | string |  | 例: `10000.00` |
| remainingDailyLimit | string |  | 例: `8500.00` |

## Query Payment Option Balances (PREDICTION_TRADE)（查詢支付選項餘額 (PREDICTION_TRADE)）

`GET /sapi/v1/w3w/wallet/prediction/balance/payment-options`

Get available balances for each payment option that can be used for prediction trading.

獲取可用於預測交易的各支付選項餘額。

Operation ID: `queryPaymentOptionBalances`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用於請求簽名的 Unix 時間戳，單位為毫秒. 該值必須反映客戶端當前時間，並會在簽名介面中由伺服器進行校驗.<br>例: `1770736694138` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>請求有效時間視窗（毫秒）<br>例: `5000` |

### 响应 200：Query Payment Option Balances / 查詢支付選項餘額

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| items | object[] |  |  |
| items[].accountType | string |  | 例: `SPOT` |
| items[].availableBalanceDisplay | string |  | 例: `1000.00` |
| items[].enabled | boolean |  | 例: `True` |

## Get Quote (PREDICTION_TRADE)（獲取報價 (PREDICTION_TRADE)）

`POST /sapi/v1/w3w/wallet/prediction/trade/get-quote`

Get a price quote for a prediction order. The returned `quoteId` must be used in the subsequent Place Order request.

獲取預測訂單的價格報價。返回的 `quoteId` 必須在後續下單請求中使用。

Operation ID: `getQuote`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| walletAddress | string | 是 | User's prediction wallet address<br>使用者預測錢包地址<br>例: `0x12e32db8817e292508c34111cbc4b23340df542c` |
| tokenId | string | 是 | Prediction outcome token ID<br>預測結果 Token ID<br>例: `112233` |
| side | string | 是 | Trade direction. Enum: `BUY`, `SELL`<br>交易方向。列舉值：`BUY`、`SELL`<br>枚举: `BUY`, `SELL`<br>例: `BUY` |
| amountIn | string | 是 | Input amount in wei (18 decimals). Must be > 0. The minimum is set by the server and may change, see the response notes. Example: `1000000000000000000` = 1 USDT<br>輸入金額（wei，18位小數），必須大於 0。最小值由服務端決定，可能調整，詳見響應說明。示例：`1000000000000000000` = 1 USDT<br>例: `1000000000000000000` |
| orderType | string | 是 | Order type. Enum: `MARKET`, `LIMIT`<br>訂單型別。列舉值：`MARKET`、`LIMIT`<br>枚举: `MARKET`, `LIMIT`<br>例: `MARKET` |
| slippageBps | integer (int32) | 是 | Slippage tolerance in basis points. Range 1–10000<br>滑點容忍度（基點）。範圍 1–10000<br>例: `1200` |
| priceLimit | string |  | Limit price. Required when `orderType=LIMIT`. Must be > 0. A price that is not on the price tick of the market (see `decimalPrecision` in Get Market Detail) is truncated down instead of being rejected, unless the result is 0<br>限價價格。當 `orderType=LIMIT` 時必填，必須大於 0。不在市場價格步長上的價格（見獲取市場詳情中的 `decimalPrecision`）會被向下截斷而不是被拒絕，截斷結果為 0 時除外<br>例: `0.5` |
| chainId | string |  | Chain ID. Default `56` (BSC)<br>鏈 ID。預設 `56`（BSC）<br>默认: `56`<br>例: `56` |
| feeRateBps | integer (int32) |  | Fee rate in basis points. Default `200`, range 1–10000<br>費率（基點）。預設 `200`，範圍 1–10000<br>默认: `200`<br>例: `200` |
| fundingSource | string |  | Funding source. Enum: `MPC`, `CEX`. Default `MPC`<br>資金來源。列舉值：`MPC`、`CEX`。預設 `MPC`<br>枚举: `MPC`, `CEX`<br>默认: `MPC`<br>例: `MPC` |
| fundTransferAmount | string |  | Auto-transfer amount before order (wei). Must be > 0 if provided<br>下單前自動劃轉金額（wei），如填寫必須大於 0<br>例: `1000000000000000000` |

### 响应 200：Get Quote / 獲取報價

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| quoteId | string |  | 例: `q_20260525_abc123xyz` |
| tokenId | string |  | 例: `112233` |
| chance | string |  | 例: `0.52` |
| vendor | string |  | 例: `PREDICT_FUN` |
| marketTitle | string |  | 例: `UP` |
| marketExtId | string |  | 例: `ext_001` |
| side | string |  | 例: `BUY` |
| amountIn | string |  | 例: `1000000000000000000` |
| amountOut | string |  | 例: `1923070000000000000` |
| isMinAmountOut | boolean |  | 例: `False` |
| feeAmount | string |  | 例: `20000000000000000` |
| feeDiscountBps | string |  | 例: `0` |
| averagePrice | number |  | 例: `0.52` |
| lastPrice | number |  | 例: `0.52` |
| priceImpact | number |  | 例: `0.001` |
| timestamp | integer (int64) |  | 例: `1748131500000` |
| chainId | string |  | 例: `56` |
| userId | integer (int64) |  | 例: `100103755893` |
| walletAddress | string |  | 例: `0x12e32db8817e292508c34111cbc4b23340df542c` |
| orderType | string |  | 例: `MARKET` |
| slippageBps | integer |  | 例: `1200` |
| feeRateBps | integer |  | 例: `200` |
| minReceive | string |  | 例: `1900000000000000000` |
| expireAt | integer (int64) |  | 例: `1748131800000` |
| priceLimit | string |  | 例: `None` |

## Place Order (PREDICTION_TRADE)（下單 (PREDICTION_TRADE)）

`POST /sapi/v1/w3w/wallet/prediction/trade/place-order-bundle`

Place a prediction order using a previously obtained quote. Requires SAS authorization.

使用此前獲取的報價下達預測訂單。需要 SAS 授權。

Operation ID: `placeOrder`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| walletAddress | string | 是 | User's prediction wallet address. Must be a valid address owned by the calling UID — a well-formed address not owned by the UID and a malformed (non-address) value both return the same generic `-3026`. An empty string instead returns `-1102` naming the field.<br>使用者預測錢包地址，必須是屬於調用方 UID 的合法地址——格式合法但不屬於該 UID、以及格式非法（非地址）這兩種情況都會返回同樣的通用 `-3026`；傳空字串則會返回會點名該欄位的 `-1102`。<br>例: `0x12e32db8817e292508c34111cbc4b23340df542c` |
| walletId | string | 是 | Wallet ID<br>錢包 ID<br>例: `5b5c1ec3be4e4416a5872b21c1ca5d20` |
| quoteId | string | 是 | Quote ID obtained from `Get Quote`<br>從 `獲取報價` 介面獲得的報價 ID<br>例: `q_20260525_abc123xyz` |
| timeInForce | string | 是 | Must match `orderType`: `FOK` for `MARKET`, `GTC` for `LIMIT`<br>必須與 `orderType` 匹配：`MARKET` 對應 `FOK`，`LIMIT` 對應 `GTC`<br>例: `FOK` |
| accountType | string | 是 | Payment account type. Enum: `SPOT`, `FUNDING`. This only determines the settlement/reference account — it does not control which balance is debited. See `fundingSource` below for that.<br>支付賬戶型別。列舉值：`SPOT`、`FUNDING`。僅決定結算/參考賬戶，並不代表實際扣款來源，扣款來源請見下方 `fundingSource`。<br>枚举: `SPOT`, `FUNDING`<br>例: `SPOT` |
| orderType | string | 是 | Order type. Enum: `MARKET`, `LIMIT` only. Do not combine with `timeInForce` (e.g. `LIMIT_GTC` is not a valid value) — set `timeInForce` separately per the Validation Rules table below.<br>訂單型別。僅接受 `MARKET`、`LIMIT`，請勿與 `timeInForce` 合併傳遞（例如 `LIMIT_GTC` 為非法值），`timeInForce` 須依下方校驗規則表單獨傳遞。<br>枚举: `MARKET`, `LIMIT`<br>例: `MARKET` |
| slippageBps | integer (int32) | 是 | Slippage tolerance in basis points. Range 1–10000<br>滑點容忍度（基點）。範圍 1–10000<br>例: `1200` |
| priceLimit | string |  | Limit price. Required when `orderType=LIMIT`, must be > 0. Omitting it when `orderType=LIMIT` returns a generic `-3026` (no field name in the message).<br>限價價格。當 `orderType=LIMIT` 時必填，必須大於 0。若 `orderType=LIMIT` 時漏傳此欄位，會返回不帶欄位名稱的通用 `-3026`。<br>例: `0.5` |
| fundingSource | string |  | Funding source. Enum: `MPC`, `CEX`. Default `MPC`. This determines which balance is actually debited, independent of `accountType`.<br>資金來源。列舉值：`MPC`、`CEX`。預設 `MPC`。實際扣款來源由此欄位決定，與 `accountType` 無關。<br>枚举: `MPC`, `CEX`<br>默认: `MPC`<br>例: `MPC` |
| fundTransferAmount | string |  | Auto-transfer amount before order (wei). Must be > 0 if provided<br>下單前自動劃轉金額（wei），如填寫必須大於 0<br>例: `1000000000000000000` |

### 响应 200：Place Order / 下單

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderId | string |  | 例: `54124` |

## Batch Cancel Orders (PREDICTION_TRADE)（批次撤單 (PREDICTION_TRADE)）

`POST /sapi/v1/w3w/wallet/prediction/trade/batch-cancel`

Cancel one or more active prediction orders in a single request. Requires SAS authorization.

**Known Issue — Bracket Encoding Incompatibility:**
This endpoint uses indexed bracket notation (`cancelInfoList[0].orderId`). Binance SAPI signature verification runs over the **raw, unencoded** canonical string. However, mainstream HTTP libraries (Python `requests`, Java `HttpURLConnection`/`URI`, Go `net/url`, Node.js `url`) automatically percent-encode `[` → `%5B` and `]` → `%5D`, producing a signature mismatch with error `-1022 Signature for this request is not valid`. Postman is unaffected because it does not encode keys.

**Workarounds** (use low-level HTTP APIs that do not normalize URLs):
- **Python:** use `http.client` (stdlib) and hand-build the body string.
- **Java:** use `HttpURLConnection` and write the raw body bytes directly.
- **Go:** use `strings.NewReader` with a hand-built body instead of `url.Values.Encode()`.

在單次請求中撤銷一個或多個活躍預測訂單。需要 SAS 授權。

**已知問題 — 方括號編碼相容性問題：**
該介面使用帶索引的方括號表示法（`cancelInfoList[0].orderId`）。Binance SAPI 對**原始未編碼**的參數字串進行簽名校驗，但主流 HTTP 庫（Python `requests`、Java `HttpURLConnection`/`URI`、Go `net/url`、Node.js `url`）會將 `[` 自動編碼為 `%5B`，`]` 編碼為 `%5D`，導致簽名不匹配，返回 `-1022 Signature for this request is not valid`。Postman 不受此影響，因其不對鍵名進行編碼。

**臨時繞過方案**（使用不自動規範化 URL 的底層 HTTP 介面）：
- **Python：** 使用 `http.client`（標準庫），手動拼接 body 字串。
- **Java：** 使用 `HttpURLConnection`，直接寫入原始 body 位元組。
- **Go：** 使用 `strings.NewReader` 手動構建 body，不使用 `url.Values.Encode()`。

Operation ID: `batchCancelOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| walletAddress | string | 是 | User's prediction wallet address<br>使用者預測錢包地址<br>例: `0x12e32db8817e292508c34111cbc4b23340df542c` |
| walletId | string | 是 | Wallet ID<br>錢包 ID<br>例: `5b5c1ec3be4e4416a5872b21c1ca5d20` |
| cancelInfoList | object[] |  | List of orders to cancel (index `i` starts from 0)<br>待撤銷訂單列表（索引 `i` 從 0 開始） |
| cancelInfoList[].orderId | string | 是 | Internal order ID to cancel<br>待撤銷的內部訂單 ID<br>例: `54124` |

### 响应 200：Batch Cancel Orders / 批次撤單

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| canceled | string[] |  |  |
| failed | object[] |  |  |
| failed[].orderId | string |  | 例: `54126` |
| failed[].reason | string |  | 例: `ORDER_NOT_FOUND` |

## Query Active Orders (PREDICTION_TRADE)（查詢活躍訂單 (PREDICTION_TRADE)）

`GET /sapi/v1/w3w/wallet/prediction/order/list`

Get active (open) prediction orders for the authenticated user.

獲取當前使用者的活躍（未完成）預測訂單。

Operation ID: `queryActiveOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| walletAddress | query | string | 是 | User's prediction wallet address<br>使用者預測錢包地址<br>例: `0x12e32db8817e292508c34111cbc4b23340df542c` |
| tradeSide | query | string |  | Filter by trade side. Enum: `BUY`, `SELL`<br>按交易方向篩選。列舉值：`BUY`、`SELL`<br>枚举: `BUY`, `SELL`<br>例: `BUY` |
| l1Category | query | string |  | Filter by level-1 category<br>按一級分類篩選<br>例: `crypto` |
| marketId | query | integer (int64) |  | Filter by market ID<br>按市場 ID 篩選<br>例: `5567895` |
| offset | query | integer (int32) |  | Pagination offset. Default `0`<br>分頁偏移量，預設 `0`<br>默认: `0`<br>例: `0` |
| limit | query | integer (int32) |  | Page size. Default `20`, range 1–100<br>每頁數量，預設 `20`，範圍 1–100<br>默认: `20`<br>例: `20` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用於請求簽名的 Unix 時間戳，單位為毫秒. 該值必須反映客戶端當前時間，並會在簽名介面中由伺服器進行校驗.<br>例: `1770736694138` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>請求有效時間視窗（毫秒）<br>例: `5000` |

### 响应 200：Query Active Orders / 查詢活躍訂單

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| total | integer |  | 例: `2` |
| offset | integer |  | 例: `0` |
| limit | integer |  | 例: `20` |
| orders | object[] |  |  |
| orders[].orderId | string |  | 例: `54124` |
| orders[].vendorOrderId | string |  | 例: `0x1234abcd...` |
| orders[].vendor | string |  | 例: `PREDICT_FUN` |
| orders[].marketTopicId | integer (int64) |  | 例: `4229564` |
| orders[].slug | string |  | 例: `btc-price-1h-up-or-down` |
| orders[].marketTopicTitle | string |  | 例: `BTC Price 1h Up or Down?` |
| orders[].marketId | integer (int64) |  | 例: `5567895` |
| orders[].marketTitle | string |  | 例: `UP` |
| orders[].outcome | string |  | 例: `YES` |
| orders[].outcomeIndex | integer |  | 例: `0` |
| orders[].status | string |  | 例: `OPENING` |
| orders[].side | string |  | 例: `BUY` |
| orders[].orderType | string |  | 例: `LIMIT` |
| orders[].createTime | integer (int64) |  | 例: `1748131500000` |
| orders[].modifyTime | integer (int64) |  | 例: `1748131500000` |
| orders[].makerUsdtAmount | string |  | 例: `1.00` |
| orders[].makerShareQty | string |  | 例: `2000.00` |
| orders[].filledUsdtAmount | string |  | 例: `0.00` |
| orders[].filledShareQty | string |  | 例: `0.00` |
| orders[].fillPercentage | string |  | 例: `0.00` |
| orders[].price | string |  | 例: `0.50` |
| orders[].marketProviderFee | string |  | 例: `0.02` |
| orders[].networkFee | string |  | 例: `0.000001` |

## Query Order History (PREDICTION_TRADE)（查詢歷史訂單 (PREDICTION_TRADE)）

`GET /sapi/v1/w3w/wallet/prediction/order/history`

Get historical prediction orders (all statuses) for the authenticated user, with optional filters.

獲取當前使用者的歷史預測訂單（所有狀態），支援可選篩選條件。

Operation ID: `queryOrderHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| walletAddress | query | string | 是 | User's prediction wallet address<br>使用者預測錢包地址<br>例: `0x12e32db8817e292508c34111cbc4b23340df542c` |
| l1Category | query | string |  | Filter by level-1 category<br>按一級分類篩選<br>例: `crypto` |
| orderType | query | string |  | Filter by order type. Enum: `MARKET`, `LIMIT`<br>按訂單型別篩選。列舉值：`MARKET`、`LIMIT`<br>枚举: `MARKET`, `LIMIT`<br>例: `MARKET` |
| status | query | string |  | Filter by order status<br>按訂單狀態篩選<br>例: `CLOSED` |
| startDate | query | string |  | Start date. Format: `yyyy-MM-dd`. Must be ≤ `endDate`<br>開始日期。格式：`yyyy-MM-dd`，必須 ≤ `endDate`<br>例: `2026-05-01` |
| endDate | query | string |  | End date. Format: `yyyy-MM-dd`. Must be ≥ `startDate`<br>結束日期。格式：`yyyy-MM-dd`，必須 ≥ `startDate`<br>例: `2026-05-25` |
| offset | query | integer (int32) |  | Pagination offset. Default `0`<br>分頁偏移量，預設 `0`<br>默认: `0`<br>例: `0` |
| limit | query | integer (int32) |  | Page size. Default `20`, range 1–100<br>每頁數量，預設 `20`，範圍 1–100<br>默认: `20`<br>例: `20` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用於請求簽名的 Unix 時間戳，單位為毫秒. 該值必須反映客戶端當前時間，並會在簽名介面中由伺服器進行校驗.<br>例: `1770736694138` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>請求有效時間視窗（毫秒）<br>例: `5000` |

### 响应 200：Query Order History / 查詢歷史訂單

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| total | integer |  | 例: `15` |
| offset | integer |  | 例: `0` |
| limit | integer |  | 例: `20` |
| orders | object[] |  |  |
| orders[].orderId | string |  | 例: `54100` |
| orders[].vendorOrderId | string |  | 例: `0xabcd5678...` |
| orders[].vendor | string |  | 例: `PREDICT_FUN` |
| orders[].marketTopicId | integer (int64) |  | 例: `4229500` |
| orders[].slug | string |  | 例: `btc-price-1h-up-or-down-prev` |
| orders[].marketTopicTitle | string |  | 例: `BTC Price 1h Up or Down?` |
| orders[].marketId | integer (int64) |  | 例: `5567800` |
| orders[].marketTitle | string |  | 例: `UP` |
| orders[].outcome | string |  | 例: `YES` |
| orders[].outcomeIndex | integer |  | 例: `0` |
| orders[].status | string |  | 例: `CLOSED` |
| orders[].side | string |  | 例: `BUY` |
| orders[].orderType | string |  | 例: `MARKET` |
| orders[].createTime | integer (int64) |  | 例: `1748045100000` |
| orders[].modifyTime | integer (int64) |  | 例: `1748045101000` |
| orders[].terminalTime | integer (int64) |  | 例: `1748045101000` |
| orders[].makerUsdtAmount | string |  | 例: `1.00` |
| orders[].makerShareQty | string |  | 例: `1923.07` |
| orders[].filledUsdtAmount | string |  | 例: `1.00` |
| orders[].filledShareQty | string |  | 例: `1923.07` |
| orders[].fillPercentage | string |  | 例: `1.00` |
| orders[].price | string |  | 例: `0.52` |
| orders[].marketProviderFee | string |  | 例: `0.02` |
| orders[].networkFee | string |  | 例: `0.000001` |

## Query Positions (PREDICTION_TRADE)（查詢持倉列表 (PREDICTION_TRADE)）

`GET /sapi/v1/w3w/wallet/prediction/position/list`

Get the authenticated user's prediction token positions with portfolio summary and tab-based filtering.

獲取當前使用者的預測 Token 持倉，包含投資組合彙總及基於標籤頁的篩選。

Operation ID: `queryPositions`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| walletAddress | query | string | 是 | User's prediction wallet address<br>使用者預測錢包地址<br>例: `0x12e32db8817e292508c34111cbc4b23340df542c` |
| tab | query | string |  | Position status tab. Values from `PositionQueryType`. Default `ONGOING`<br>持倉狀態標籤頁。取值來自 `PositionQueryType`。預設 `ONGOING`<br>默认: `ONGOING`<br>例: `ONGOING` |
| offset | query | integer (int32) |  | Pagination offset. Default `0`<br>分頁偏移量，預設 `0`<br>默认: `0`<br>例: `0` |
| limit | query | integer (int32) |  | Page size. Default `20`, range 1–100<br>每頁數量，預設 `20`，範圍 1–100<br>默认: `20`<br>例: `20` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用於請求簽名的 Unix 時間戳，單位為毫秒. 該值必須反映客戶端當前時間，並會在簽名介面中由伺服器進行校驗.<br>例: `1770736694138` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>請求有效時間視窗（毫秒）<br>例: `5000` |

### 响应 200：Query Positions / 查詢持倉列表

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| summary | object |  |  |
| summary.totalValue | string |  | 例: `1523.45` |
| summary.positionValue | string |  | 例: `523.45` |
| summary.walletBalance | string |  | 例: `1000.00` |
| summary.totalClaimableAmount | string |  | 例: `50.00` |
| summary.todayRealizedPnl | string |  | 例: `15.30` |
| summary.todayRealizedPnlPercent | string |  | 例: `3.10` |
| summary.todayTotalCost | string |  | 例: `493.55` |
| counts | object |  |  |
| counts.ongoingCount | integer |  | 例: `3` |
| counts.endedCount | integer |  | 例: `12` |
| counts.pendingClaimCount | integer |  | 例: `1` |
| positions | object[] |  |  |
| positions[].positionId | integer (int64) |  | 例: `1001` |
| positions[].vendor | string |  | 例: `PREDICT_FUN` |
| positions[].chainId | string |  | 例: `56` |
| positions[].tokenId | string |  | 例: `112233` |
| positions[].collateralSymbol | string |  | 例: `USDT` |
| positions[].topicType | string |  | 例: `FLAT` |
| positions[].marketTopicId | integer (int64) |  | 例: `4229564` |
| positions[].marketId | integer (int64) |  | 例: `5567895` |
| positions[].marketTopicTitle | string |  | 例: `BTC Price 1h Up or Down?` |
| positions[].marketTitle | string |  | 例: `UP` |
| positions[].outcomeName | string |  | 例: `YES` |
| positions[].outcomeIndex | integer |  | 例: `0` |
| positions[].shares | string |  | 例: `1923.07` |
| positions[].avgPrice | string |  | 例: `0.52` |
| positions[].totalCost | string |  | 例: `1.00` |
| positions[].value | string |  | 例: `1.06` |
| positions[].currentPrice | string |  | 例: `0.55` |
| positions[].toWin | string |  | 例: `1923.07` |
| positions[].positionStatus | string |  | 例: `OPEN` |
| positions[].canClaim | boolean |  | 例: `False` |
| positions[].endDate | integer (int64) |  | 例: `1748134800000` |
| positions[].unrealizedPnl | string |  | 例: `0.06` |
| positions[].unrealizedPnlPercent | string |  | 例: `6.00` |
| positions[].realizedPnl | string |  | 例: `0.00` |
| positions[].pnl | string |  | 例: `0.06` |
| positions[].createdTime | integer (int64) |  | 例: `1748131500000` |
| positions[].updatedTime | integer (int64) |  | 例: `1748132000000` |

## Query Positions by Filter (PREDICTION_TRADE)（按條件查詢持倉 (PREDICTION_TRADE)）

`GET /sapi/v1/w3w/wallet/prediction/position/filter`

Get prediction positions filtered by wallet address and/or market topic ID. Both parameters are optional.

按錢包地址和/或市場主題 ID 篩選預測持倉。兩個參數均為可選。

Operation ID: `queryPositionsByFilter`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| walletAddress | query | string |  | User's prediction wallet address<br>使用者預測錢包地址<br>例: `0x12e32db8817e292508c34111cbc4b23340df542c` |
| marketTopicId | query | integer (int64) |  | Filter by market topic ID<br>按市場主題 ID 篩選<br>例: `4229564` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用於請求簽名的 Unix 時間戳，單位為毫秒. 該值必須反映客戶端當前時間，並會在簽名介面中由伺服器進行校驗.<br>例: `1770736694138` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>請求有效時間視窗（毫秒）<br>例: `5000` |

### 响应 200：Query Positions by Filter / 按條件查詢持倉

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| positions | object[] |  |  |
| positions[].positionId | integer (int64) |  | 例: `1001` |
| positions[].vendor | string |  | 例: `PREDICT_FUN` |
| positions[].chainId | string |  | 例: `56` |
| positions[].tokenId | string |  | 例: `112233` |
| positions[].collateralSymbol | string |  | 例: `USDT` |
| positions[].topicType | string |  | 例: `FLAT` |
| positions[].marketTopicId | integer (int64) |  | 例: `4229564` |
| positions[].marketId | integer (int64) |  | 例: `5567895` |
| positions[].marketTopicTitle | string |  | 例: `BTC Price 1h Up or Down?` |
| positions[].marketTitle | string |  | 例: `UP` |
| positions[].outcomeName | string |  | 例: `YES` |
| positions[].outcomeIndex | integer |  | 例: `0` |
| positions[].shares | string |  | 例: `1923.07` |
| positions[].avgPrice | string |  | 例: `0.52` |
| positions[].totalCost | string |  | 例: `1.00` |
| positions[].value | string |  | 例: `1.06` |
| positions[].currentPrice | string |  | 例: `0.55` |
| positions[].positionStatus | string |  | 例: `OPEN` |
| positions[].endDate | integer (int64) |  | 例: `1748134800000` |
| positions[].unrealizedPnl | string |  | 例: `0.06` |
| positions[].realizedPnl | string |  | 例: `0.00` |
| positions[].pnl | string |  | 例: `0.06` |
| positions[].createdTime | integer (int64) |  | 例: `1748131500000` |
| positions[].updatedTime | integer (int64) |  | 例: `1748132000000` |

## Get Position by Token (PREDICTION_TRADE)（按 Token 查詢持倉 (PREDICTION_TRADE)）

`GET /sapi/v1/w3w/wallet/prediction/position/token`

Get the authenticated user's position detail for a specific prediction token.

獲取當前使用者指定預測 Token 的持倉詳情。

Operation ID: `getPositionByToken`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| walletAddress | query | string | 是 | User's prediction wallet address<br>使用者預測錢包地址<br>例: `0x12e32db8817e292508c34111cbc4b23340df542c` |
| tokenId | query | string | 是 | Prediction outcome token ID<br>預測結果 Token ID<br>例: `112233` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用於請求簽名的 Unix 時間戳，單位為毫秒. 該值必須反映客戶端當前時間，並會在簽名介面中由伺服器進行校驗.<br>例: `1770736694138` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>請求有效時間視窗（毫秒）<br>例: `5000` |

### 响应 200：Get Position by Token / 按 Token 查詢持倉

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| position | object |  |  |
| position.positionId | integer (int64) |  | 例: `1001` |
| position.vendor | string |  | 例: `PREDICT_FUN` |
| position.chainId | string |  | 例: `56` |
| position.tokenId | string |  | 例: `112233` |
| position.collateralSymbol | string |  | 例: `USDT` |
| position.topicType | string |  | 例: `FLAT` |
| position.marketTopicId | integer (int64) |  | 例: `4229564` |
| position.marketId | integer (int64) |  | 例: `5567895` |
| position.marketTopicTitle | string |  | 例: `BTC Price 1h Up or Down?` |
| position.marketTitle | string |  | 例: `UP` |
| position.outcomeName | string |  | 例: `YES` |
| position.outcomeIndex | integer |  | 例: `0` |
| position.shares | string |  | 例: `1923.07` |
| position.avgPrice | string |  | 例: `0.52` |
| position.totalCost | string |  | 例: `1.00` |
| position.value | string |  | 例: `1.06` |
| position.currentPrice | string |  | 例: `0.55` |
| position.positionStatus | string |  | 例: `OPEN` |
| position.endDate | integer (int64) |  | 例: `1748134800000` |
| position.unrealizedPnl | string |  | 例: `0.06` |
| position.realizedPnl | string |  | 例: `0.00` |
| position.pnl | string |  | 例: `0.06` |
| position.createdTime | integer (int64) |  | 例: `1748131500000` |
| position.updatedTime | integer (int64) |  | 例: `1748132000000` |

## Query PnL (PREDICTION_TRADE)（查詢盈虧 (PREDICTION_TRADE)）

`GET /sapi/v1/w3w/wallet/prediction/pnl/query`

Query profit and loss records for the authenticated user's prediction positions. When `tokenId` is provided, returns a single record in `pnl`; otherwise returns a list in `pnlList`.

查詢當前使用者預測持倉的盈虧記錄。當提供 `tokenId` 時，在 `pnl` 中返回單條記錄；否則在 `pnlList` 中返回列表。

Operation ID: `queryPnL`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| walletAddress | query | string | 是 | User's prediction wallet address<br>使用者預測錢包地址<br>例: `0x12e32db8817e292508c34111cbc4b23340df542c` |
| tokenId | query | string |  | Filter by prediction token ID<br>按預測 Token ID 篩選<br>例: `112233` |
| marketId | query | integer (int64) |  | Filter by market ID. Must be > 0<br>按市場 ID 篩選，必須大於 0<br>例: `5567895` |
| marketTopicId | query | integer (int64) |  | Filter by market topic ID. Must be > 0<br>按市場主題 ID 篩選，必須大於 0<br>例: `4229564` |
| activeOnly | query | boolean |  | If `true`, return only active (unresolved) positions<br>若為 `true`，僅返回活躍（未結算）持倉<br>例: `False` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用於請求簽名的 Unix 時間戳，單位為毫秒. 該值必須反映客戶端當前時間，並會在簽名介面中由伺服器進行校驗.<br>例: `1770736694138` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>請求有效時間視窗（毫秒）<br>例: `5000` |

### 响应 200：Query PnL / 查詢盈虧

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| chainId | string |  | 例: `56` |
| walletAddress | string |  | 例: `0x12e32db8817e292508c34111cbc4b23340df542c` |
| pnl | object |  | 例: `None` |
| pnlList | object[] |  |  |
| pnlList[].id | integer (int64) |  | 例: `10001` |
| pnlList[].walletAddress | string |  | 例: `0x12e32db8817e292508c34111cbc4b23340df542c` |
| pnlList[].marketTopicId | integer (int64) |  | 例: `4229564` |
| pnlList[].marketId | integer (int64) |  | 例: `5567895` |
| pnlList[].tokenId | string |  | 例: `112233` |
| pnlList[].vendor | string |  | 例: `PREDICT_FUN` |
| pnlList[].currentShares | string |  | 例: `1923.07` |
| pnlList[].avgPrice | string |  | 例: `0.52` |
| pnlList[].currentPrice | string |  | 例: `0.55` |
| pnlList[].realizedPnl | string |  | 例: `0.00` |
| pnlList[].unrealizedPnl | string |  | 例: `0.06` |
| pnlList[].totalPnl | string |  | 例: `0.06` |
| pnlList[].pnlPercentage | string |  | 例: `6.00` |
| pnlList[].isResolved | boolean |  | 例: `False` |
| totalCount | integer |  | 例: `1` |
| totalRealizedPnl | string |  | 例: `0.00` |
| totalUnrealizedPnl | string |  | 例: `0.06` |
| totalPnl | string |  | 例: `0.06` |

## Query Settled Position History (PREDICTION_TRADE)（查詢已結算持倉歷史 (PREDICTION_TRADE)）

`GET /sapi/v1/w3w/wallet/prediction/position/settled-history`

Get the authenticated user's settled (resolved) prediction position history with optional filters.

獲取當前使用者已結算（已裁定）的預測持倉歷史，支援可選篩選條件。

Operation ID: `querySettledPositionHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| walletAddress | query | string | 是 | User's prediction wallet address<br>使用者預測錢包地址<br>例: `0x12e32db8817e292508c34111cbc4b23340df542c` |
| l1Category | query | string |  | Filter by level-1 category<br>按一級分類篩選<br>例: `crypto` |
| result | query | integer (int32) |  | Settlement result filter<br>結算結果篩選<br>例: `1` |
| startDate | query | string |  | Start date. Format: `yyyy-MM-dd`. Must be ≤ `endDate`<br>開始日期。格式：`yyyy-MM-dd`，必須 ≤ `endDate`<br>例: `2026-05-01` |
| endDate | query | string |  | End date. Format: `yyyy-MM-dd`. Must be ≥ `startDate`<br>結束日期。格式：`yyyy-MM-dd`，必須 ≥ `startDate`<br>例: `2026-05-25` |
| offset | query | integer (int32) |  | Pagination offset. Default `0`<br>分頁偏移量，預設 `0`<br>默认: `0`<br>例: `0` |
| limit | query | integer (int32) |  | Page size. Default `20`, range 1–100<br>每頁數量，預設 `20`，範圍 1–100<br>默认: `20`<br>例: `20` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用於請求簽名的 Unix 時間戳，單位為毫秒. 該值必須反映客戶端當前時間，並會在簽名介面中由伺服器進行校驗.<br>例: `1770736694138` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>請求有效時間視窗（毫秒）<br>例: `5000` |

### 响应 200：Query Settled Position History / 查詢已結算持倉歷史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| totalCount | integer |  | 例: `5` |
| positions | object[] |  |  |
| positions[].positionId | integer (int64) |  | 例: `998` |
| positions[].vendor | string |  | 例: `PREDICT_FUN` |
| positions[].chainId | string |  | 例: `56` |
| positions[].tokenId | string |  | 例: `112200` |
| positions[].collateralSymbol | string |  | 例: `USDT` |
| positions[].topicType | string |  | 例: `FLAT` |
| positions[].marketTopicId | integer (int64) |  | 例: `4229500` |
| positions[].marketId | integer (int64) |  | 例: `5567800` |
| positions[].marketTopicTitle | string |  | 例: `BTC Price 1h Up or Down?` |
| positions[].marketTitle | string |  | 例: `UP` |
| positions[].outcomeName | string |  | 例: `YES` |
| positions[].outcomeIndex | integer |  | 例: `0` |
| positions[].shares | string |  | 例: `5000.00` |
| positions[].avgPrice | string |  | 例: `0.30` |
| positions[].totalCost | string |  | 例: `1.50` |
| positions[].value | string |  | 例: `5000.00` |
| positions[].currentPrice | string |  | 例: `1.00` |
| positions[].toWin | string |  | 例: `5000.00` |
| positions[].positionStatus | string |  | 例: `CLAIMED` |
| positions[].isWinner | boolean |  | 例: `True` |
| positions[].redeemStatus | string |  | 例: `CONFIRMED` |
| positions[].endDate | integer (int64) |  | 例: `1748040000000` |
| positions[].finalOutcome | string |  | 例: `YES` |
| positions[].realizedPnl | string |  | 例: `4998.50` |
| positions[].pnl | string |  | 例: `4998.50` |
| positions[].claimAmount | string |  | 例: `5000.00` |
| positions[].settledDate | integer (int64) |  | 例: `1748040000000` |
| positions[].createdTime | integer (int64) |  | 例: `1748020000000` |
| positions[].updatedTime | integer (int64) |  | 例: `1748040500000` |

## Batch Redeem (PREDICTION_TRADE)（批次贖回 (PREDICTION_TRADE)）

`POST /sapi/v1/w3w/wallet/prediction/batch-redeem`

Redeem one or more settled prediction tokens on-chain to claim winnings. Requires SAS authorization.

在鏈上贖回一個或多個已結算的預測 Token 以領取獎金。需要 SAS 授權。

Operation ID: `batchRedeem`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| walletAddress | string | 是 | User's prediction wallet address<br>使用者預測錢包地址<br>例: `0x12e32db8817e292508c34111cbc4b23340df542c` |
| walletId | string | 是 | Wallet ID<br>錢包 ID<br>例: `5b5c1ec3be4e4416a5872b21c1ca5d20` |
| tokenIds | string[] | 是 | List of prediction token IDs to redeem. Not empty. Example: `tokenIds=112233&tokenIds=112234`<br>待贖回的預測 Token ID 列表，不可為空。示例：`tokenIds=112233&tokenIds=112234` |
| chainId | string |  | Chain ID. Default `56` (BSC)<br>鏈 ID。預設 `56`（BSC）<br>默认: `56`<br>例: `56` |

### 响应 200：Batch Redeem / 批次贖回

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| batchId | string |  | 例: `batch_20260525_redeem_001` |
| results | object[] |  |  |
| results[].requestId | string |  | 例: `req_001` |
| results[].txHash | string |  | 例: `0xabc123def456789abcdef123456789abcdef123456789abcdef123456789abcd` |
| results[].status | string |  | 例: `PENDING` |
| results[].error | string |  | 例: `None` |

## Get Redeem Status (PREDICTION_TRADE)（查詢贖回狀態 (PREDICTION_TRADE)）

`GET /sapi/v1/w3w/wallet/prediction/redeem/status`

Query the on-chain transaction status of a previously submitted redeem request.

查詢此前提交的贖回請求的鏈上交易狀態。

Operation ID: `getRedeemStatus`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| walletAddress | query | string | 是 | User's prediction wallet address<br>使用者預測錢包地址<br>例: `0x12e32db8817e292508c34111cbc4b23340df542c` |
| txHash | query | string | 是 | Redeem transaction hash<br>贖回交易雜湊<br>例: `0xabc123def456789abcdef123456789abcdef123456789abcdef123456789abcd` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用於請求簽名的 Unix 時間戳，單位為毫秒. 該值必須反映客戶端當前時間，並會在簽名介面中由伺服器進行校驗.<br>例: `1770736694138` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>請求有效時間視窗（毫秒）<br>例: `5000` |

### 响应 200：Get Redeem Status / 查詢贖回狀態

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| txHash | string |  | 例: `0xabc123def456789abcdef123456789abcdef123456789abcdef123456789abcd` |
| status | string |  | 例: `CONFIRMED` |

## Create Inbound Transfer (PREDICTION_TRADE)（建立入金劃轉 (PREDICTION_TRADE)）

`POST /sapi/v1/w3w/wallet/prediction/transfer/inbound`

Transfer funds from the prediction wallet back to the user's CEX account (SPOT or FUNDING). Requires SAS authorization.

⚠️ **SAS Authorization Required:** This endpoint enforces SAS (Self-Authorization Service) authorization. If SAS is not enabled for the wallet, the request will be rejected with `-31003 SAS authorization required`. Enable SAS for your wallet before calling this endpoint.

將資金從預測錢包劃轉回使用者的 CEX 賬戶（現貨或資金賬戶）。需要 SAS 授權。

⚠️ **需要 SAS 授權：** 該介面強制要求 SAS（自助授權服務）授權。若錢包未開啟 SAS，請求將被拒絕並返回 `-31003 SAS authorization required`。呼叫該介面前請先為錢包開啟 SAS。

Operation ID: `createInboundTransfer`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| walletId | string | 是 | Wallet ID<br>錢包 ID<br>例: `5b5c1ec3be4e4416a5872b21c1ca5d20` |
| walletAddress | string | 是 | User's prediction wallet address<br>使用者預測錢包地址<br>例: `0x12e32db8817e292508c34111cbc4b23340df542c` |
| fromTokenAmount | string | 是 | Transfer amount in wei (18 decimals). Must be > 0. Example: `1000000000000000000` = 1 USDT<br>劃轉金額（wei，18位小數），必須大於 0。示例：`1000000000000000000` = 1 USDT<br>例: `1000000000000000000` |
| accountType | string | 是 | Destination CEX account. Enum: `SPOT`, `FUNDING`<br>目標 CEX 賬戶。列舉值：`SPOT`、`FUNDING`<br>枚举: `SPOT`, `FUNDING`<br>例: `SPOT` |
| fromToken | string |  | Source token symbol. Default `USDT`<br>來源 Token 符號。預設 `USDT`<br>默认: `USDT`<br>例: `USDT` |
| toToken | string |  | Destination token symbol. Default `USDT`<br>目標 Token 符號。預設 `USDT`<br>默认: `USDT`<br>例: `USDT` |
| chainId | string |  | Chain ID. Default `56` (BSC)<br>鏈 ID。預設 `56`（BSC）<br>默认: `56`<br>例: `56` |

### 响应 200：Create Inbound Transfer / 建立入金劃轉

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| transferId | string |  | 例: `tf_20260525_in_001` |
| status | string |  | 例: `PROCESSING` |

## Create Outbound Transfer (PREDICTION_TRADE)（創建出金劃轉 (PREDICTION_TRADE)）

`POST /sapi/v1/w3w/wallet/prediction/transfer/outbound`

Transfer funds from the user's CEX account (SPOT or FUNDING) into the prediction wallet. Requires SAS authorization.

將資金從使用者的 CEX 賬戶（現貨或資金賬戶）劃轉至預測錢包。需要 SAS 授權。

Operation ID: `createOutboundTransfer`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| walletId | string | 是 | Wallet ID<br>錢包 ID<br>例: `5b5c1ec3be4e4416a5872b21c1ca5d20` |
| walletAddress | string | 是 | User's prediction wallet address<br>使用者預測錢包地址<br>例: `0x12e32db8817e292508c34111cbc4b23340df542c` |
| fromTokenAmount | string | 是 | Transfer amount in wei (18 decimals). Must be > 0. Example: `1000000000000000000` = 1 USDT<br>劃轉金額（wei，18位小數），必須大於 0。示例：`1000000000000000000` = 1 USDT<br>例: `1000000000000000000` |
| accountType | string | 是 | Source CEX account. Enum: `SPOT`, `FUNDING`<br>來源 CEX 賬戶。列舉值：`SPOT`、`FUNDING`<br>枚举: `SPOT`, `FUNDING`<br>例: `SPOT` |
| sourceBiz | string | 是 | Business source. Enum: `USER_TRANSFER`, `PREDICTION_BUY`<br>業務來源。列舉值：`USER_TRANSFER`、`PREDICTION_BUY`<br>枚举: `USER_TRANSFER`, `PREDICTION_BUY`<br>例: `USER_TRANSFER` |
| fromToken | string |  | Source token symbol. Default `USDT`<br>來源 Token 符號。預設 `USDT`<br>默认: `USDT`<br>例: `USDT` |
| toToken | string |  | Destination token symbol. Default `USDT`<br>目標 Token 符號。預設 `USDT`<br>默认: `USDT`<br>例: `USDT` |
| chainId | string |  | Chain ID. Default `56` (BSC)<br>鏈 ID。預設 `56`（BSC）<br>默认: `56`<br>例: `56` |

### 响应 200：Create Outbound Transfer / 創建出金劃轉

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| transferId | string |  | 例: `tf_20260525_out_001` |
| status | string |  | 例: `PROCESSING` |

## Query Transfer List (PREDICTION_TRADE)（查詢劃轉記錄 (PREDICTION_TRADE)）

`GET /sapi/v1/w3w/wallet/prediction/transfer/list`

Get the authenticated user's prediction wallet transfer history within a date range.

獲取當前使用者預測錢包在指定日期範圍內的劃轉歷史。

Operation ID: `queryTransferList`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| walletAddress | query | string | 是 | User's prediction wallet address<br>使用者預測錢包地址<br>例: `0x12e32db8817e292508c34111cbc4b23340df542c` |
| startDate | query | string | 是 | Start date. Format: `yyyy-MM-dd`. Must be ≤ `endDate`<br>開始日期。格式：`yyyy-MM-dd`，必須 ≤ `endDate`<br>例: `2026-05-01` |
| endDate | query | string | 是 | End date. Format: `yyyy-MM-dd`. Must be ≥ `startDate`<br>結束日期。格式：`yyyy-MM-dd`，必須 ≥ `startDate`<br>例: `2026-05-25` |
| tokenSymbol | query | string |  | Filter by token symbol (e.g. `USDT`)<br>按 Token 符號篩選（例如 `USDT`）<br>例: `USDT` |
| direction | query | string |  | Filter by direction. Enum: `INBOUND`, `OUTBOUND`<br>按方向篩選。列舉值：`INBOUND`、`OUTBOUND`<br>枚举: `INBOUND`, `OUTBOUND`<br>例: `OUTBOUND` |
| offset | query | integer (int32) |  | Pagination offset. Default `0`<br>分頁偏移量，預設 `0`<br>默认: `0`<br>例: `0` |
| limit | query | integer (int32) |  | Page size. Default `20`, range 1–100<br>每頁數量，預設 `20`，範圍 1–100<br>默认: `20`<br>例: `20` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用於請求簽名的 Unix 時間戳，單位為毫秒. 該值必須反映客戶端當前時間，並會在簽名介面中由伺服器進行校驗.<br>例: `1770736694138` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>請求有效時間視窗（毫秒）<br>例: `5000` |

### 响应 200：Query Transfer List / 查詢劃轉記錄

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| transfers | object[] |  |  |
| transfers[].transferId | string |  | 例: `tf_20260525_out_001` |
| transfers[].direction | string |  | 例: `OUTBOUND` |
| transfers[].status | string |  | 例: `SUCCESS` |
| transfers[].walletAddress | string |  | 例: `0x12e32db8817e292508c34111cbc4b23340df542c` |
| transfers[].fromToken | string |  | 例: `USDT` |
| transfers[].fromTokenAmount | string |  | 例: `100.00` |
| transfers[].toToken | string |  | 例: `USDT` |
| transfers[].toTokenAmount | string |  | 例: `100.00` |
| transfers[].errorCode | string |  | 例: `None` |
| transfers[].errorMessage | string |  | 例: `None` |
| transfers[].createTime | string |  | 例: `2026-05-25T04:00:00.000+00:00` |
| transfers[].updateTime | string |  | 例: `2026-05-25T04:00:05.000+00:00` |
| transfers[].completeAt | string |  | 例: `2026-05-25T04:00:05.000+00:00` |

## Query Transfer Status (PREDICTION_TRADE)（查詢劃轉狀態 (PREDICTION_TRADE)）

`GET /sapi/v1/w3w/wallet/prediction/transfer/status`

Query the current status of a prediction wallet transfer by transfer ID.

**`status` values:** Terminal states are `COMPLETED` and `FAILED`. Intermediate states are `PROCESSING` and `PENDING`. **Do not** poll for `SUCCESS` — it is not a valid terminal state.

通過劃轉 ID 查詢預測錢包劃轉的當前狀態。

**`status` 列舉值：** 終態為 `COMPLETED` 和 `FAILED`，中間態為 `PROCESSING` 和 `PENDING`。**不要**輪詢 `SUCCESS`，該值不是有效的終態。

Operation ID: `queryTransferStatus`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| transferId | query | string | 是 | Transfer ID returned from outbound/inbound transfer<br>出金/入金劃轉返回的劃轉 ID<br>例: `tf_20260525_out_001` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用於請求簽名的 Unix 時間戳，單位為毫秒. 該值必須反映客戶端當前時間，並會在簽名介面中由伺服器進行校驗.<br>例: `1770736694138` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>請求有效時間視窗（毫秒）<br>例: `5000` |

### 响应 200：Query Transfer Status / 查詢劃轉狀態

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| transferId | string |  | 例: `tf_20260525_out_001` |
| direction | string |  | 例: `OUTBOUND` |
| status | string |  | 枚举: `COMPLETED`, `FAILED`, `PROCESSING`, `PENDING`<br>例: `COMPLETED` |
| fromToken | string |  | 例: `USDT` |
| fromTokenAmount | string |  | 例: `100.00` |
| toToken | string |  | 例: `USDT` |
| toTokenAmount | string |  | 例: `100.00` |
| errorCode | string |  | 例: `None` |
| errorMessage | string |  | 例: `None` |
| createTime | string |  | 例: `2026-05-25T04:00:00.000+00:00` |
| updateTime | string |  | 例: `2026-05-25T04:00:05.000+00:00` |

## Apply MM Deposit (PREDICTION_TRADE)（申請 MM 入金 (PREDICTION_TRADE)）

`POST /sapi/v1/w3w/wallet/prediction/deposit/apply`

Move funds from the user's bound CeDeFi MPC wallet to their CEX account (SPOT/FUNDING) via a contract escrow + credit flow. The maker wallet is resolved server-side by `userId`; the caller does not pass wallet or signature.

將資金從使用者綁定的 CeDeFi MPC 錢包劃轉到 CEX 賬戶（現貨/資金賬戶），透過合約 escrow + credit 流程完成。 maker 錢包由服務端根據 `userId` 解析，呼叫方無需傳錢包或簽名。

Operation ID: `applyMmDeposit`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| fromToken | string | 是 | Source token symbol (e.g. `USDT`)<br>來源 token 代號（如 `USDT`）<br>例: `USDT` |
| fromTokenAmount | string | 是 | Source token amount in WEI (18 decimals). Example: `1000000000000000000` = 1 USDT<br>來源 token 金額（wei，18 位小數）。示例：`1000000000000000000` = 1 USDT<br>例: `1000000000000000000` |
| toToken | string | 是 | Target token symbol (e.g. `USDT`)<br>目標 token 代號（如 `USDT`）<br>例: `USDT` |
| accountType | string | 是 | Target CEX account type. Enum: `SPOT`, `FUNDING`<br>目標 CEX 賬戶型別。列舉值：`SPOT`、`FUNDING`<br>枚举: `SPOT`, `FUNDING`<br>例: `SPOT` |
| chainId | string |  | Chain ID. Default `56` (BSC)<br>鏈 ID。預設 `56`（BSC）<br>默认: `56`<br>例: `56` |

### 响应 200：Apply MM Deposit / 申請 MM 入金

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| transferId | string |  | 例: `26080400000000454343` |
| status | string |  | 例: `PROCESSING` |

## Apply MM Withdraw (PREDICTION_TRADE)（申請 MM 出金 (PREDICTION_TRADE)）

`POST /sapi/v1/w3w/wallet/prediction/withdraw/apply`

Withdraw funds from the user's CEX account (SPOT/FUNDING) to their bound CeDeFi MPC wallet address. Unlike `v1/capital/withdraw/apply`, the caller does NOT pass `address`; the backend resolves the user's bound CeDeFi MPC wallet address by `userId` and reuses the existing capital withdraw flow with that address as the target.

將資金從使用者 CEX 賬戶（現貨/資金賬戶）出金到綁定的 CeDeFi MPC 錢包地址。與 `v1/capital/withdraw/apply` 不同， 呼叫方無需傳 `address`；後端根據 `userId` 解析綁定的 CeDeFi MPC 錢包地址，複用現有出金流程，以該地址作為目標。

Operation ID: `applyMmWithdraw`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| coin | string | 是 | Coin to withdraw (e.g. `USDT`)<br>出金幣種（如 `USDT`）<br>例: `USDT` |
| network | string | 是 | Network (e.g. `BEP20`)<br>網路（如 `BEP20`）<br>例: `BEP20` |
| amount | string | 是 | Amount to withdraw (must be > 0)<br>出金數量（必須 > 0）<br>例: `100.00` |
| withdrawOrderId | string |  | Client withdraw order id (idempotency key)<br>客戶端出金訂單 ID（冪等鍵）<br>例: `wd_20260814_001` |
| walletType | integer |  | Source CEX account type. Enum: `0` (SPOT), `1` (FUNDING). Default `0`. Must be `0` or `1`; any other value is rejected<br>來源 CEX 賬戶型別。列舉值：`0`（現貨）、`1`（資金賬戶）。預設 `0`。必須為 `0` 或 `1`，其他值會被拒絕<br>枚举: `0`, `1`<br>默认: `0`<br>例: `0` |
| name | string |  | Remark for the withdraw<br>出金備註<br>例: `MM withdraw` |

### 响应 200：Apply MM Withdraw / 申請 MM 出金

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string |  | 例: `123456789` |
| walletId | string |  | 例: `0ecd3be8e3674b54b1258e24f9c3706b` |
| walletAddress | string |  | 例: `0x2ac3a1fb164da5c4e76f67ae6dbe6be821c000c8` |
| transferId | string |  | 例: `26080400000000454344` |

## Create OTC Blocktrade (PREDICTION_TRADE)（建立 OTC 大宗交易 (PREDICTION_TRADE)）

`POST /sapi/v1/w3w/wallet/prediction/otc/blocktrade/create`

Create an OTC blocktrade as the maker (BID to buy outcome shares with USDT, or ASK to sell outcome shares for USDT). The maker wallet is resolved server-side by `userId`; signing is done server-side via SAS `typedDataSign`. Returns `orderId` and a one-time `secretToken` to share out-of-band with the intended taker.

作為 maker 建立一筆 OTC 大宗交易（BID 用 USDT 買入 outcome shares，或 ASK 賣出 outcome shares 換取 USDT）。 maker 錢包由服務端根據 `userId` 解析，簽名透過 SAS `typedDataSign` 在服務端完成。 返回 `orderId` 和一次性 `secretToken`，用於與指定 taker 在帶外分享。

Operation ID: `createOtcBlocktrade`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| marketId | string | 是 | PredictFun market id<br>PredictFun 市場 ID<br>例: `123` |
| tokenId | string | 是 | ERC-1155 outcome token id<br>例: `71321045679252212594626385532706912750332728571942532289631379312455583992563` |
| side | string | 是 | Trade side. Enum: `BUY` (BID), `SELL` (ASK)<br>交易方向。列舉值：`BUY`（BID）、`SELL`（ASK）<br>枚举: `BUY`, `SELL`<br>例: `BUY` |
| makerAmount | string | 是 | Maker amount in wei. BID：USDT; ASK：shares<br>maker 金額（wei）。BID：USDT；ASK：shares<br>例: `600000000000000000000` |
| takerAmount | string | 是 | Taker amount in wei. BID：shares; ASK：USDT<br>taker 金額（wei）。BID：shares；ASK：USDT<br>例: `1000000000000000000000` |
| pricePerShare | string | 是 | Price per share (decimal ether, e.g. `0.65`)<br>每股價格（decimal ether，如 `0.65`）<br>例: `0.65` |
| expiration | integer (int64) | 是 | Expiration timestamp in seconds (GTD order)<br>過期時間戳（秒，GTD 訂單）<br>例: `1790000000` |

### 响应 200：Create OTC Blocktrade / 建立 OTC 大宗交易

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderId | string |  | 例: `26080500000001234567` |
| secretToken | string |  | 例: `a1b2c3d4-e5f6-7890-abcd-ef1234567890` |

## List OTC Blocktrades (PREDICTION_TRADE)（查詢 OTC 大宗交易列表 (PREDICTION_TRADE)）

`POST /sapi/v1/w3w/wallet/prediction/otc/blocktrade/list`

List the maker's own blocktrades with optional status filter and cursor pagination.

查詢 maker 自己的大宗交易列表，支援按狀態過濾和游標分頁。

Operation ID: `listOtcBlocktrades`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| first | integer (int32) |  | Page size<br>每頁筆數<br>例: `20` |
| after | string |  | Pagination cursor (from previous response)<br>分頁游標（來自上一次回應）<br>例: `next-cursor-string` |
| status | string |  | Filter by status. Enum: `OPEN`, `FULFILLED`, `MATCHED`, `CANCELLED`, `EXPIRED`, `FAILED`<br>按狀態過濾。列舉值：`OPEN`、`FULFILLED`、`MATCHED`、`CANCELLED`、`EXPIRED`、`FAILED`<br>枚举: `OPEN`, `FULFILLED`, `MATCHED`, `CANCELLED`, `EXPIRED`, `FAILED`<br>例: `OPEN` |

### 响应 200：List OTC Blocktrades / 查詢 OTC 大宗交易列表

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| cursor | string |  | 例: `next-cursor-string` |
| blocktrades | object[] |  |  |
| blocktrades[].status | string |  | 例: `OPEN` |
| blocktrades[].marketId | string |  | 例: `123` |
| blocktrades[].tokenId | string |  | 例: `71321045679252212594626385532706912750332728571942532289631379312455583992563` |
| blocktrades[].side | integer |  | 0 = BUY (Bid), 1 = SELL (Ask) — see Create OTC Blocktrade for the side/quoteType mapping<br>0 = BUY（Bid），1 = SELL（Ask）——side/quoteType 對照見「建立 OTC 大宗交易」<br>例: `0` |
| blocktrades[].maker | string |  | 例: `0x12e32db8817e292508c34111cbc4b23340df542c` |
| blocktrades[].makerAmount | string |  | 例: `600000000000000000000` |
| blocktrades[].takerAmount | string |  | 例: `1000000000000000000000` |
| blocktrades[].price | number |  | 例: `0.65` |
| blocktrades[].quoteType | string |  | 例: `Bid` |
| blocktrades[].createdAt | string |  | 例: `2026-08-05T10:30:00.000Z` |
| blocktrades[].secretToken | string |  | 例: `a1b2c3d4-e5f6-7890-abcd-ef1234567890` |

## Get OTC Blocktrade Detail (PREDICTION_TRADE)（查詢 OTC 大宗交易詳情 (PREDICTION_TRADE)）

`POST /sapi/v1/w3w/wallet/prediction/otc/blocktrade/detail`

Query the maker's own blocktrade by `orderId`. Returns full order data including status and `secretToken`.

maker 透過 `orderId` 查詢自己的大宗交易。返回完整訂單資料，包含狀態和 `secretToken`。

Operation ID: `getOtcBlocktradeDetail`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderId | string | 是 | Maker order id (returned by create)<br>maker 訂單 ID（由 create 返回）<br>例: `26080500000001234567` |

### 响应 200：Get OTC Blocktrade Detail / 查詢 OTC 大宗交易詳情

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderId | string |  | 例: `26080500000001234567` |
| status | string |  | 例: `OPEN` |
| orderData | object |  |  |
| orderData.status | string |  | 例: `OPEN` |
| orderData.marketId | string |  | 例: `123` |
| orderData.tokenId | string |  | 例: `71321045679252212594626385532706912750332728571942532289631379312455583992563` |
| orderData.side | integer |  | 0 = BUY (Bid), 1 = SELL (Ask) — see Create OTC Blocktrade for the side/quoteType mapping<br>0 = BUY（Bid），1 = SELL（Ask）——side/quoteType 對照見「建立 OTC 大宗交易」<br>例: `0` |
| orderData.maker | string |  | 例: `0x12e32db8817e292508c34111cbc4b23340df542c` |
| orderData.taker | string |  | 例: `None` |
| orderData.makerAmount | string |  | 例: `600000000000000000000` |
| orderData.takerAmount | string |  | 例: `1000000000000000000000` |
| orderData.price | number |  | 例: `0.65` |
| orderData.orderType | string |  | 例: `GTD` |
| orderData.timeInForce | string |  | 例: `GTD` |
| orderData.expiration | integer (int64) |  | 例: `1790000000` |
| orderData.filledAmount | string |  | 例: `0` |
| orderData.quoteType | string |  | 例: `Bid` |
| orderData.createdAt | string |  | 例: `2026-08-05T10:30:00.000Z` |
| orderData.isNegRisk | boolean |  | 例: `False` |
| orderData.isYieldBearing | boolean |  | 例: `False` |
| orderData.secretToken | string |  | 例: `a1b2c3d4-e5f6-7890-abcd-ef1234567890` |

## Get OTC Blocktrade Events (PREDICTION_TRADE)（查詢 OTC 大宗交易事件 (PREDICTION_TRADE)）

`POST /sapi/v1/w3w/wallet/prediction/otc/blocktrade/events`

Paginated feed of blocktrade lifecycle and settlement events (CREATE, FULFIL, MATCH_SUBMIT, MATCH_SUCCESS, EXPIRE, FAILED, etc.).

分頁查詢大宗交易的生命週期和結算事件（CREATE、FULFIL、MATCH_SUBMIT、MATCH_SUCCESS、EXPIRE、FAILED 等）。

Operation ID: `getOtcBlocktradeEvents`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| first | integer (int32) |  | Page size<br>每頁筆數<br>例: `20` |
| after | string |  | Pagination cursor<br>分頁游標<br>例: `next-cursor-string` |
| eventTypes | string[] |  | Filter by event types (e.g. `["MATCH_SUCCESS","EXPIRE"]`)<br>按事件類型過濾（如 `["MATCH_SUCCESS","EXPIRE"]`） |
| marketId | integer (int64) |  | Filter by market id<br>按市場 ID 過濾<br>例: `123` |

### 响应 200：Get OTC Blocktrade Events / 查詢 OTC 大宗交易事件

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| cursor | string |  | 例: `next-cursor-string` |
| events | object[] |  |  |
| events[].event | string |  | 例: `CREATE` |
| events[].blocktradeId | string |  | 例: `pf-bt-001` |
| events[].orderId | string |  | 例: `26080500000001234567` |
| events[].marketId | integer |  | 例: `123` |
| events[].amount | string |  | 例: `600000000000000000000` |
| events[].fee | string |  | 例: `1000000000000000` |
| events[].effectiveFee | string |  | 例: `1000000000000000` |
| events[].price | string |  | 例: `650000000000000000` |
| events[].transactionHash | string |  | 例: `None` |
| events[].reason | string |  | 例: `None` |
| events[].isMaker | boolean |  | 例: `True` |
| events[].timestamp | string |  | 例: `2026-08-05T10:30:00.000Z` |

## Preview OTC Blocktrade (PREDICTION_TRADE)（預覽 OTC 大宗交易 (PREDICTION_TRADE)）

`POST /sapi/v1/w3w/wallet/prediction/otc/blocktrade/preview`

Inspect an open blocktrade by `secretToken` (no `orderId` needed). Taker uses this to preview the maker order before fulfilling. Returns the same shape as `Get Blocktrade Detail`, but `orderId` is `null` and `secretToken` is never returned from this endpoint.

透過 `secretToken` 預覽未結清的大宗交易（無需 `orderId`）。taker 在完成交易前用此介面預覽 maker 訂單。 返回結構與「查詢 OTC 大宗交易詳情」相同，但 `orderId` 為 `null`，且本介面不會返回 `secretToken`。

Operation ID: `previewOtcBlocktrade`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| secretToken | string | 是 | One-time fulfilment token the maker shared out-of-band<br>maker 在帶外分享的一次性完成權杖<br>例: `a1b2c3d4-e5f6-7890-abcd-ef1234567890` |

### 响应 200：Preview OTC Blocktrade / 預覽 OTC 大宗交易

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderId | string |  | 例: `None` |
| status | string |  | 例: `OPEN` |
| orderData | object |  |  |
| orderData.status | string |  | 例: `OPEN` |
| orderData.marketId | string |  | 例: `123` |
| orderData.tokenId | string |  | 例: `71321045679252212594626385532706912750332728571942532289631379312455583992563` |
| orderData.side | integer |  | 0 = BUY (Bid), 1 = SELL (Ask) — see Create OTC Blocktrade for the side/quoteType mapping<br>0 = BUY（Bid），1 = SELL（Ask）——side/quoteType 對照見「建立 OTC 大宗交易」<br>例: `0` |
| orderData.maker | string |  | 例: `0x12e32db8817e292508c34111cbc4b23340df542c` |
| orderData.taker | string |  | 例: `None` |
| orderData.makerAmount | string |  | 例: `600000000000000000000` |
| orderData.takerAmount | string |  | 例: `1000000000000000000000` |
| orderData.price | number |  | 例: `0.65` |
| orderData.orderType | string |  | 例: `GTD` |
| orderData.timeInForce | string |  | 例: `GTD` |
| orderData.expiration | integer (int64) |  | 例: `1790000000` |
| orderData.filledAmount | string |  | 例: `0` |
| orderData.quoteType | string |  | 例: `Bid` |
| orderData.createdAt | string |  | 例: `2026-08-05T10:30:00.000Z` |
| orderData.isNegRisk | boolean |  | 例: `False` |
| orderData.isYieldBearing | boolean |  | 例: `False` |

## Fulfil OTC Blocktrade (PREDICTION_TRADE)（完成 OTC 大宗交易 (PREDICTION_TRADE)）

`POST /sapi/v1/w3w/wallet/prediction/otc/blocktrade/fulfil`

Fulfil an open maker blocktrade as the taker, using the `secretToken` the maker shared out-of-band. All-or-nothing fill (no partial fill); the taker order is the server-derived symmetric inverse of the maker order.

作為 taker，使用 maker 在帶外分享的 `secretToken` 完成一筆未結清的 maker 大宗交易。 全部成交（無部分成交）；taker 訂單是服務端推導的 maker 訂單的對稱反向訂單。

Operation ID: `fulfilOtcBlocktrade`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderId | string | 是 | Maker order id (returned by maker create)<br>maker 訂單 ID（由 maker create 返回）<br>例: `26080500000001234567` |
| secretToken | string | 是 | One-time fulfilment token the maker shared out-of-band<br>maker 在帶外分享的一次性完成權杖<br>例: `a1b2c3d4-e5f6-7890-abcd-ef1234567890` |

### 响应 200：Fulfil OTC Blocktrade / 完成 OTC 大宗交易

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderId | string |  | 例: `26080500000001234568` |

## Remove OTC Blocktrades (PREDICTION_TRADE)（撤銷 OTC 大宗交易 (PREDICTION_TRADE)）

`POST /sapi/v1/w3w/wallet/prediction/otc/blocktrade/remove`

Cancel open or fulfilled-but-unsettled blocktrades. Terminal orders (already `MATCHED`/`CANCELLED`/`EXPIRED`/`FAILED`) are returned in `noop` instead of `removed`.

撤銷未結清或已成交但未結算的大宗交易。已進入終態的訂單（`MATCHED`/`CANCELLED`/`EXPIRED`/`FAILED`）會返回在 `noop` 中，而不是 `removed`。

Operation ID: `removeOtcBlocktrades`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderIds | string[] | 是 | Order ids to remove (max 100). Must be the `orderId` returned by Create OTC Blocktrade<br>要撤銷的訂單 ID 列表（最多 100 個）。必須是「建立 OTC 大宗交易」返回的 `orderId` |

### 响应 200：Remove OTC Blocktrades / 撤銷 OTC 大宗交易

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| removed | string[] |  |  |
| noop | string[] |  |  |

## Get OTC Reserved Balances (PREDICTION_TRADE)（查詢 OTC 預留餘額 (PREDICTION_TRADE)）

`POST /sapi/v1/w3w/wallet/prediction/otc/blocktrade/reserved-balances`

Query PredictFun reserved balances for the caller's bound wallet — these are funds locked by the caller's open OTC blocktrade orders (maker BID locks USDT, maker ASK locks shares). Not tied to a specific blocktrade id; the path nesting under `otc/blocktrade` reflects the cause of the lock, not a per-order query. Returns one entry per requested asset, aligned with the request order. Pass `{type:"USDT"}` for reserved USDT, or `{type:"SHARE", tokenId:"..."}` for a specific outcome token's reserved shares.

查詢呼叫方綁定錢包在 PredictFun 的預留餘額——這些資金是因呼叫方未結清的 OTC 大宗交易訂單而被鎖定的（maker BID 鎖定 USDT，maker ASK 鎖定 shares）。 不與特定大宗交易 ID 綁定；路徑嵌套在 `otc/blocktrade` 下反映的是鎖定原因，而非按訂單查詢。按請求的資產順序返回。 傳 `{type:"USDT"}` 查詢 USDT 預留餘額，傳 `{type:"SHARE", tokenId:"..."}` 查詢指定 outcome token 的 shares 預留餘額。

Operation ID: `getOtcReservedBalances`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| assets | object[] | 是 | Assets to query (max 50)<br>要查詢的資產列表（最多 50 個） |
| assets[].type | string |  | 枚举: `USDT`, `SHARE` |
| assets[].tokenId | string |  | 例: `71321045679252212594626385532706912750332728571942532289631379312455583992563` |

### 响应 200：Get OTC Reserved Balances / 查詢 OTC 預留餘額

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| balances | object[] |  |  |
| balances[].type | string |  | 例: `USDT` |
| balances[].tokenId | string |  | 例: `None` |
| balances[].amount | string |  | 例: `500000000000000000000` |