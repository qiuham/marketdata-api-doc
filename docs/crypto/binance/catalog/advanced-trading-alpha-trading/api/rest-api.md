---
exchange: binance
source_url: https://developers.binance.com/en/docs/catalog/advanced-trading-alpha-trading/api/rest-api
api_type: REST
updated_at: 2026-11-25 18:49:29.648792
---

# Alpha Trading REST API

Schema: https://developers.binance.com/en/docs/catalog/advanced-trading-alpha-trading/api/rest-api/1.0.0/schema.yaml

APIs for Binance Alpha Trading.

Binance Alpha Trading 的 API。

版本: 1.0.0

## 服务地址

- `https://www.binance.com`

## 接口列表

- `GET /bapi/defi/v1/public/alpha-trade/agg-trades` — Aggregated Trades
- `GET /bapi/defi/v1/public/alpha-trade/fullDepth` — Full Depth
- `GET /bapi/defi/v1/public/alpha-trade/get-exchange-info` — Get Exchange Info
- `GET /bapi/defi/v1/public/alpha-trade/klines` — Klines
- `GET /bapi/defi/v1/public/alpha-trade/ticker` — Ticker
- `GET /bapi/defi/v1/public/wallet-direct/buw/wallet/cex/alpha/all/token/list` — Token List

## Aggregated Trades（聚合交易查询）

`GET /bapi/defi/v1/public/alpha-trade/agg-trades`

Retrieves compressed, aggregated historical trades for a specific symbol. Useful for recent trade history.

获取指定交易对的压缩聚合历史成交数据，适用于查询近期成交记录。

Operation ID: `aggregatedTrades`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Trading pair symbol, e.g. ALPHA_118USDC (use token ID from Token List).<br>交易对符号，例如 ALPHA_118USDC（请使用 Token 列表中的代币 ID）。<br>例: `ALPHA_118USDC` |
| fromId | query | integer (int64) |  | Starting aggregate trade ID to fetch from.<br>起始聚合成交 ID。<br>例: `58470` |
| startTime | query | integer (int64) |  | Start timestamp in milliseconds.<br>起始时间戳（毫秒）。<br>例: `1752568680000` |
| endTime | query | integer (int64) |  | End timestamp in milliseconds.<br>结束时间戳（毫秒）。<br>例: `1752572280000` |
| limit | query | integer (int64) |  | Number of results to return.<br>返回结果数量。<br>默认: `500`<br>例: `500` |

### 响应 200：Aggregated Trades / 聚合交易

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  | API response code. "000000" indicates success.<br>API 响应码。"000000" 表示成功。<br>例: `000000` |
| message | string |  | Response message.<br>响应消息。<br>例: `` |
| messageDetail | string |  | Detailed response message.<br>响应详细消息。<br>例: `` |
| data | object[] |  | Array of aggregated trades.<br>聚合成交数据数组。 |
| data[].a | integer (int64) |  | Aggregate trade ID.<br>聚合成交 ID。<br>例: `58470` |
| data[].p | string |  | Trade price.<br>成交价格。<br>例: `1.00` |
| data[].q | string |  | Trade quantity.<br>成交数量。<br>例: `1.00` |
| data[].f | integer (int64) |  | First trade ID in the aggregation.<br>聚合中的首笔成交 ID。<br>例: `58470` |
| data[].l | integer (int64) |  | Last trade ID in the aggregation.<br>聚合中的末笔成交 ID。<br>例: `58665` |
| data[].T | integer (int64) |  | Trade timestamp in milliseconds.<br>成交时间戳（毫秒）。<br>例: `1752568680000` |
| data[].m | boolean |  | Whether buyer is the market maker (deprecated).<br>买方是否为做市方（已废弃）。<br>例: `True` |

## Full Depth（完整深度（订单簿））

`GET /bapi/defi/v1/public/alpha-trade/fullDepth`

Fetches the full order book depth (UI & API orders) for a symbol, including bid and ask orders with their prices and quantities.

获取指定交易对的完整订单簿深度（UI 和 API 订单），包括买单和卖单的价格和数量。

Operation ID: `fullDepth`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Trading pair symbol, e.g. ALPHA_175USDT (use token ID from Token List).<br>交易对符号，例如 ALPHA_175USDT（请使用 Token 列表中的代币 ID）。<br>例: `ALPHA_175USDT` |
| limit | query | integer (int64) |  | Number of price levels to return. Valid values: 5, 10, 20, 50, 100, 500, 1000.<br>返回的价格档位数量。有效值：5、10、20、50、100、500、1000。<br>枚举: `5`, `10`, `20`, `50`, `100`, `500`, `1000`<br>默认: `500`<br>例: `500` |

### 响应 200：Full Depth / 完整深度

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  | API response code. "000000" indicates success.<br>API 响应码。"000000" 表示成功。<br>例: `000000` |
| message | string |  | Response message.<br>响应消息。<br>例: `None` |
| messageDetail | string |  | Detailed response message.<br>响应详细消息。<br>例: `None` |
| success | boolean |  | Whether request is successful.<br>请求是否成功。<br>例: `True` |
| data | object |  | Order book data.<br>订单簿数据。 |
| data.lastUpdateId | integer (int64) |  | Last order book update ID.<br>最新订单簿更新 ID。<br>例: `47534656223` |
| data.symbol | string |  | Trading pair symbol.<br>交易对符号。<br>例: `ALPHA_175USDT` |
| data.bids | oneOf[][] |  | Bid orders. Each entry is [price, quantity].<br>买单列表。每项为 [价格, 数量]。 |
| data.asks | oneOf[][] |  | Ask orders. Each entry is [price, quantity].<br>卖单列表。每项为 [价格, 数量]。 |
| data.E | integer (int64) |  | Event time in milliseconds.<br>事件时间（毫秒）。<br>例: `1775027836086` |
| data.T | integer (int64) |  | Transaction time in milliseconds.<br>交易时间（毫秒）。<br>例: `1775027836072` |

## Get Exchange Info（交易对信息）

`GET /bapi/defi/v1/public/alpha-trade/get-exchange-info`

Fetches general exchange information, such as supported symbols, rate limits, and server time.

获取通用的交易所信息，如支持的交易对、限速信息及服务器时间。

Operation ID: `getExchangeInfo`

### 响应 200：Get Exchange Info / 获取交易对信息

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  | API response code. "000000" indicates success.<br>API 响应码。"000000" 表示成功。<br>例: `000000` |
| message | string |  | Response message.<br>响应消息。<br>例: `` |
| messageDetail | string |  | Detailed response message.<br>响应详细消息。<br>例: `` |
| success | boolean |  | Whether request is successful.<br>请求是否成功。<br>例: `True` |
| data | object |  | Exchange metadata, including assets and symbols.<br>交易所元数据，包含资产和交易对信息。 |
| data.timezone | string |  | Timezone of market data.<br>行情数据时区。<br>例: `UTC` |
| data.assets | object[] |  | Supported assets.<br>支持的资产列表。 |
| data.assets[].asset | string |  | Asset symbol.<br>资产符号。<br>例: `USDT` |
| data.symbols | object[] |  | Supported trading symbols.<br>支持的交易对列表。 |
| data.symbols[].symbol | string |  | Trading symbol.<br>交易对。<br>例: `ALPHA_105USDT` |
| data.symbols[].status | string |  | Trading status.<br>交易状态。<br>例: `TRADING` |
| data.symbols[].baseAsset | string |  | Base asset symbol.<br>基础资产符号。<br>例: `ALPHA_105` |
| data.symbols[].quoteAsset | string |  | Quote asset symbol.<br>计价资产符号。<br>例: `USDT` |
| data.symbols[].pricePrecision | integer (int64) |  | Allowed precision for price.<br>价格精度。<br>例: `8` |
| data.symbols[].quantityPrecision | integer (int64) |  | Allowed precision for quantity.<br>数量精度。<br>例: `8` |
| data.symbols[].baseAssetPrecision | integer (int64) |  | Base asset precision.<br>基础资产精度。<br>例: `8` |
| data.symbols[].quotePrecision | integer (int64) |  | Quote asset precision.<br>计价资产精度。<br>例: `8` |
| data.symbols[].filters | object[] |  | Trading filters and constraints.<br>交易过滤器与限制。 |
| data.symbols[].filters[].filterType | string |  | Filter type.<br>过滤器类型。<br>例: `PRICE_FILTER` |
| data.symbols[].filters[].minPrice | string |  | Minimum price.<br>最小价格。<br>例: `0.00000001` |
| data.symbols[].filters[].maxPrice | string |  | Maximum price.<br>最大价格。<br>例: `1000` |
| data.symbols[].filters[].tickSize | string |  | Tick size.<br>价格步长。<br>例: `0.00000001` |
| data.symbols[].filters[].stepSize | string |  | Step size.<br>数量步长。<br>例: `0.01000000` |
| data.symbols[].filters[].maxQty | string |  | Maximum quantity.<br>最大数量。<br>例: `277778` |
| data.symbols[].filters[].minQty | string |  | Minimum quantity.<br>最小数量。<br>例: `0.01000000` |
| data.symbols[].filters[].limit | integer (int64) |  | Maximum allowed orders for this rule.<br>该规则允许的最大订单数。<br>例: `200` |
| data.symbols[].filters[].minNotional | string |  | Minimum notional value.<br>最小名义价值。<br>例: `0.1` |
| data.symbols[].filters[].maxNotional | string |  | Maximum notional value.<br>最大名义价值。<br>例: `1000000` |
| data.symbols[].filters[].multiplierDown | string |  | Lower multiplier bound.<br>下限倍率。<br>例: `0.20000` |
| data.symbols[].filters[].multiplierUp | string |  | Upper multiplier bound.<br>上限倍率。<br>例: `5` |
| data.symbols[].filters[].bidMultiplierUp | string |  | Upper multiplier bound for bids.<br>买单上限倍率。<br>例: `5` |
| data.symbols[].filters[].askMultiplierUp | string |  | Upper multiplier bound for asks.<br>卖单上限倍率。<br>例: `5` |
| data.symbols[].filters[].bidMultiplierDown | string |  | Lower multiplier bound for bids.<br>买单下限倍率。<br>例: `0.20000` |
| data.symbols[].filters[].askMultiplierDown | string |  | Lower multiplier bound for asks.<br>卖单下限倍率。<br>例: `0.20000` |
| data.symbols[].orderTypes | string[] |  | Supported order types for this symbol.<br>该交易对支持的订单类型。 |
| data.orderTypes | string |  | Order types metadata returned by backend.<br>后端返回的订单类型元数据。<br>例: `` |

## Klines（K线）

`GET /bapi/defi/v1/public/alpha-trade/klines`

Fetches Kline/candlestick bars for a symbol, which include open/high/low/close prices and volume over intervals. Useful for charting and analysis.

获取某一交易对的K线/蜡烛图数据，包含开盘价、最高价、最低价、收盘价及成交量等信息，适用于图表绘制和行情分析。

Operation ID: `klines`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Trading pair symbol, e.g. ALPHA_175USDT (use token ID from Token List).<br>交易对符号，例如 ALPHA_175USDT（请使用 Token 列表中的代币 ID）。<br>例: `ALPHA_175USDT` |
| interval | query | string | 是 | Kline interval.<br>K 线间隔。<br>枚举: `1s`, `15s`, `1m`, `3m`, `5m`, `15m`, `30m`, `1h`, `2h`, `4h`, `6h`, `8h`, `12h`, `1d`, `3d`, `1w`, `1M`<br>例: `1h` |
| limit | query | integer (int64) |  | Number of klines to return.<br>返回 K 线数量。<br>默认: `500`<br>例: `500` |
| startTime | query | integer (int64) |  | Start timestamp in milliseconds.<br>起始时间戳（毫秒）。<br>例: `1752642000000` |
| endTime | query | integer (int64) |  | End timestamp in milliseconds.<br>结束时间戳（毫秒）。<br>例: `1752645599999` |

### 响应 200：Klines / K 线

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  | API response code. "000000" indicates success.<br>API 响应码。"000000" 表示成功。<br>例: `000000` |
| message | string |  | Response message.<br>响应消息。<br>例: `` |
| messageDetail | string |  | Detailed response message.<br>响应详细消息。<br>例: `` |
| success | boolean |  | Whether request is successful.<br>请求是否成功。<br>例: `True` |
| data | oneOf[][] |  | Array of kline rows. Each row contains: open time, open, high, low, close, volume, close time, quote volume, trade count, taker buy base volume, taker buy quote volume, and a static 0.<br>K 线数组。每一项依次为：开盘时间、开盘价、最高价、最低价、收盘价、成交量、收盘时间、计价成交量、成交笔数、主动买入基础资产量、主动买入计价资产量，以及静态值 0。 |

## Ticker（24hr价格变动情况）

`GET /bapi/defi/v1/public/alpha-trade/ticker`

Gets the 24-hour rolling window price change statistics for a symbol, including volume and price changes.

获取某个交易对过去 24 小时滚动窗口的价格变化统计， 包括成交量和价格变化。

Operation ID: `ticker`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Trading pair symbol, e.g. ALPHA_175USDT (use token ID from Token List).<br>交易对符号，例如 ALPHA_175USDT（请使用 Token 列表中的代币 ID）。<br>例: `ALPHA_175USDT` |

### 响应 200：Ticker / 行情

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  | API response code. "000000" indicates success.<br>API 响应码。"000000" 表示成功。<br>例: `000000` |
| message | string |  | Response message.<br>响应消息。<br>例: `` |
| messageDetail | string |  | Detailed response message.<br>响应详细消息。<br>例: `` |
| data | object |  | 24-hour rolling window ticker statistics.<br>24 小时滚动窗口行情统计。 |
| data.symbol | string |  | Trading pair symbol.<br>交易对符号。<br>例: `ALPHA_175USDT` |
| data.priceChange | string |  | Absolute price change in the 24h window.<br>24 小时窗口内绝对价格变化。<br>例: `-0.00007172` |
| data.priceChangePercent | string |  | Percentage price change in the 24h window.<br>24 小时窗口内价格变化百分比。<br>例: `-8.841` |
| data.weightedAvgPrice | string |  | Weighted average price in the 24h window.<br>24 小时窗口内加权平均价格。<br>例: `0.00079608` |
| data.lastPrice | string |  | Latest traded price.<br>最新成交价。<br>例: `0.00073954` |
| data.lastQty | string |  | Quantity of the latest trade.<br>最新一笔成交数量。<br>例: `12600.43000000` |
| data.openPrice | string |  | Opening price of the 24h window.<br>24 小时窗口开盘价。<br>例: `0.00081126` |
| data.highPrice | string |  | Highest price in the 24h window.<br>24 小时窗口最高价。<br>例: `0.00081126` |
| data.lowPrice | string |  | Lowest price in the 24h window.<br>24 小时窗口最低价。<br>例: `0.00073954` |
| data.volume | string |  | Base asset volume in the 24h window.<br>24 小时窗口基础资产成交量。<br>例: `1204754.30000000` |
| data.quoteVolume | string |  | Quote asset volume in the 24h window.<br>24 小时窗口计价资产成交量。<br>例: `959.07729927` |
| data.openTime | integer (int64) |  | Start time of the 24h window (milliseconds).<br>24 小时窗口开始时间（毫秒）。<br>例: `1768808100000` |
| data.closeTime | integer (int64) |  | End time of the 24h window (milliseconds).<br>24 小时窗口结束时间（毫秒）。<br>例: `1768893244772` |
| data.firstId | integer (int64) |  | First trade ID in the 24h window.<br>24 小时窗口内首笔成交 ID。<br>例: `93742` |
| data.lastId | integer (int64) |  | Last trade ID in the 24h window.<br>24 小时窗口内末笔成交 ID。<br>例: `93768` |
| data.count | integer (int64) |  | Total number of trades in the 24h window.<br>24 小时窗口内成交总笔数。<br>例: `38` |
| success | boolean |  | Whether request is successful.<br>请求是否成功。<br>例: `True` |

## Token List（代币列表）

`GET /bapi/defi/v1/public/wallet-direct/buw/wallet/cex/alpha/all/token/list`

Retrieves a list of all available ALPHA tokens, including their IDs and symbols. Use this to find the token ID for constructing symbols in other endpoints.

获取所有可用ALPHA代币的列表，包括它们的ID和符号。用于在其它接口构造symbol参数时查找代币ID。

Operation ID: `tokenList`

### 响应 200：Token List / 代币列表

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  | API response code. "000000" indicates success.<br>API 响应码。"000000" 表示成功。<br>例: `000000` |
| message | string |  | Response message.<br>响应消息。<br>例: `` |
| messageDetail | string |  | Detailed response message.<br>响应详细消息。<br>例: `` |
| success | boolean |  | Whether request is successful.<br>请求是否成功。<br>例: `True` |
| data | object[] |  | List of ALPHA tokens and metadata.<br>ALPHA 代币及其元数据列表。 |
| data[].tokenId | string |  | Unique token identifier.<br>代币唯一标识。<br>例: `3F350C8B3621770A673159B7A19BC034` |
| data[].chainId | string |  | Chain ID.<br>链 ID。<br>例: `56` |
| data[].chainIconUrl | string |  | Chain icon URL.<br>链图标 URL。<br>例: `https://bin.bnbstatic.com/image/admin_mgs_image_upload/20250228/d0216ce4-a3e9-4bda-8937-4a6aa943ccf2.png` |
| data[].chainName | string |  | Chain name.<br>链名称。<br>例: `BSC` |
| data[].contractAddress | string |  | Token contract address.<br>代币合约地址。<br>例: `0xcf640fdf9b3d9e45cbd69fda91d7e22579c14444` |
| data[].name | string |  | Token name.<br>代币名称。<br>例: `gorilla` |
| data[].symbol | string |  | Token symbol.<br>代币符号。<br>例: `gorilla` |
| data[].iconUrl | string |  | Token icon URL.<br>代币图标 URL。<br>例: `https://bin.bnbstatic.com/images/web3-data/public/token/logos/248b5406f88a4ee28913a29107875339.png` |
| data[].price | string |  | Latest token price.<br>代币最新价格。<br>例: `0.00080595003978242023` |
| data[].percentChange24h | string |  | 24-hour price change percentage.<br>24 小时价格涨跌幅。<br>例: `-7.42` |
| data[].volume24h | string |  | 24-hour trading volume.<br>24 小时成交量。<br>例: `14847.711222633409558029675` |
| data[].marketCap | string |  | 例: `805950.03978242` |
| data[].fdv | string |  | 例: `805950.03978242` |
| data[].liquidity | string |  | 例: `263192.72813121626034` |
| data[].totalSupply | string |  | 例: `1000000000` |
| data[].circulatingSupply | string |  | 例: `1000000000` |
| data[].holders | string |  | 例: `7120` |
| data[].decimals | integer (int64) |  | 例: `18` |
| data[].listingCex | boolean |  | 例: `False` |
| data[].hotTag | boolean |  | 例: `False` |
| data[].cexCoinName | string |  | 例: `` |
| data[].canTransfer | boolean |  | 例: `False` |
| data[].denomination | integer (int64) |  | 例: `1` |
| data[].offline | boolean |  | 例: `False` |
| data[].tradeDecimal | integer (int64) |  | 例: `8` |
| data[].alphaId | string |  | ALPHA token ID, e.g. ALPHA_175.<br>ALPHA 代币 ID，例如 ALPHA_175。<br>例: `ALPHA_175` |
| data[].offsell | boolean |  | 例: `False` |
| data[].priceHigh24h | string |  | 例: `0.00088873864475645879` |
| data[].priceLow24h | string |  | 例: `0.0008020805165487083` |
| data[].count24h | string |  | 例: `166` |
| data[].onlineTge | boolean |  | 例: `False` |
| data[].onlineAirdrop | boolean |  | 例: `False` |
| data[].score | integer (int64) |  | 例: `1` |
| data[].cexOffDisplay | boolean |  | 例: `False` |
| data[].stockState | boolean |  | 例: `False` |
| data[].listingTime | integer (int64) |  | 例: `1746686700000` |
| data[].mulPoint | integer (int64) |  | 例: `1` |
| data[].bnExclusiveState | boolean |  | 例: `False` |