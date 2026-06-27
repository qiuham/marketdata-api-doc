---
exchange: binance
source_url: https://developers.binance.com/docs/alpha/market-data/rest-api/get-exchange-info
api_type: Market Data
updated_at: 2026-01-15T23:50:43.788132
---

# Get Exchange Info

## Endpoint: /bapi/defi/v1/public/alpha-trade/get-exchange-info[​](/docs/alpha/market-data/rest-api/get-exchange-info#endpoint-bapidefiv1publicalpha-tradeget-exchange-info "Direct link to Endpoint: /bapi/defi/v1/public/alpha-trade/get-exchange-info")

## Full URL[​](/docs/alpha/market-data/rest-api/get-exchange-info#full-url "Direct link to Full URL")

<https://www.binance.com/bapi/defi/v1/public/alpha-trade/get-exchange-info>

## Description[​](/docs/alpha/market-data/rest-api/get-exchange-info#description "Direct link to Description")

Fetches general exchange information, such as supported symbols, rate limits, and server time.

## Parameters[​](/docs/alpha/market-data/rest-api/get-exchange-info#parameters "Direct link to Parameters")

None

## Response Structure[​](/docs/alpha/market-data/rest-api/get-exchange-info#response-structure "Direct link to Response Structure")

  * `code`: String, the API response code. Here, "000000" indicates success.
  * `message`: Null, generally used for returning informational messages.
  * `messageDetail`: Null, usually for more detailed messages or error descriptions.
  * `success`: Boolean, indicates whether the API call was successful (true).
  * `data`: Object, containing trading and asset related information: 
    * `timezone`: String, representing the timezone of the trading data, e.g., "UTC".
    * `assets`: Array of objects, each with fields: 
      * `asset`: String, the asset symbol, e.g., "USDT".
    * `symbols`: Array of objects, each representing a trading symbol or pair with fields: 
      * `symbol`: String, trading pair name, e.g., "ALPHA_105USDT".
      * `status`: String, trading status of the symbol, e.g., "TRADING".
      * `baseAsset`: String, base asset of the trading pair, e.g., "ALPHA_105".
      * `quoteAsset`: String, quote asset of the trading pair, e.g., "USDT".
      * `pricePrecision`: Integer, number of decimals allowed for the price.
      * `quantityPrecision`: Integer, number of decimals allowed for quantity.
      * `baseAssetPrecision`: Integer, precision of the base asset.
      * `quotePrecision`: Integer, precision of the quote asset.
      * `filters`: Array of objects, each representing trading rules or constraints with common fields: 
        * `filterType`: String, type of filter (e.g., "PRICE_FILTER", "LOT_SIZE", "MIN_NOTIONAL").
        * `minPrice`: String, min Price
        * `maxPrice`: String, max Price
        * `tickSize`: String, tick Size
        * `stepSize`: String, step Size
        * `maxQty`: String, max Quantity
        * `minQty`: String, min Quantity
        * `limit`: Integer, limit of max num orders
        * `minNotional`: String, minimum of notional
        * `maxNotional`: String, max of notional
        * `multiplierDown`: String, lower bound multiplier
        * `multiplierUp`: String, upper bound multiplier
        * `bidMultiplierUp`: String, upper bound multiplier for bid (buy) prices
        * `askMultiplierUp`: String, upper bound multiplier for ask (buy) prices
        * `bidMultiplierDown`: String, lower bound multiplier for bid price
        * `askMultiplierDown`: String, lower bound multiplier for ask price
      * `orderTypes`: Array of strings, listing supported order types for the symbol, e.g., ["LIMIT"].

---

# 交易对信息

## 接口：/bapi/defi/v1/public/alpha-trade/get-exchange-info[​](/docs/zh-CN/alpha/market-data/rest-api/get-exchange-info#接口bapidefiv1publicalpha-tradeget-exchange-info "接口：/bapi/defi/v1/public/alpha-trade/get-exchange-info的直接链接")

## 完整URL[​](/docs/zh-CN/alpha/market-data/rest-api/get-exchange-info#完整url "完整URL的直接链接")

<https://www.binance.com/bapi/defi/v1/public/alpha-trade/get-exchange-info>

## 描述[​](/docs/zh-CN/alpha/market-data/rest-api/get-exchange-info#描述 "描述的直接链接")

获取通用的交易所信息，如支持的交易对、限速信息及服务器时间。

## 参数[​](/docs/zh-CN/alpha/market-data/rest-api/get-exchange-info#参数 "参数的直接链接")

无

## 响应结构[​](/docs/zh-CN/alpha/market-data/rest-api/get-exchange-info#响应结构 "响应结构的直接链接")

  * `code`: 字符串，API响应码，此处“000000”表示成功。
  * `message`: 空，通常用于返回信息提示。
  * `messageDetail`: 空，通常用于更详细信息或错误描述。
  * `success`: 布尔值，表示此次API调用是否成功（true）。
  * `data`: 对象，包含交易及资产相关信息： 
    * `timezone`: 字符串，表示交易数据的时区，如“UTC”。
    * `assets`: 对象数组，每个对象包含字段： 
      * `asset`: 字符串，资产符号，如“USDT”。
    * `symbols`: 对象数组，每个对象代表一个交易对，包含字段： 
      * `symbol`: 字符串，交易对名称，如“ALPHA_105USDT”。
      * `status`: 字符串，交易对状态，如“TRADING”。
      * `baseAsset`: 字符串，基础资产，如“ALPHA_105”。
      * `quoteAsset`: 字符串，计价资产，如“USDT”。
      * `pricePrecision`: 整数，价格小数位数。
      * `quantityPrecision`: 整数，数量小数位数。
      * `baseAssetPrecision`: 整数，基础资产精度。
      * `quotePrecision`: 整数，计价资产精度。
      * `filters`: 对象数组，每个对象代表交易规则或限制，通常包含字段： 
        * `filterType`: 字符串，过滤器类型（例如“PRICE_FILTER”、“LOT_SIZE”、“MIN_NOTIONAL”）。
        * `minPrice`: 字符串，最小价格
        * `maxPrice`: 字符串，最高价格
        * `tickSize`: 字符串，价格步长
        * `stepSize`: 字符串，数量步长
        * `maxQty`: 字符串，最大数量
        * `minQty`: 字符串，最小数量
        * `limit`: 整数，最大订单数限制
        * `minNotional`: 字符串，最小名义金额
        * `maxNotional`: 字符串，最大名义金额
        * `multiplierDown`: 字符串，下限倍数
        * `multiplierUp`: 字符串，上限倍数
        * `bidMultiplierUp`: 字符串，买单价格上限倍数
        * `askMultiplierUp`: 字符串，卖单价格上限倍数
        * `bidMultiplierDown`: 字符串，买单价格下限倍数
        * `askMultiplierDown`: 字符串，卖单价格下限倍数
      * `orderTypes`: 字符串数组，列出该交易对支持的订单类型，如["LIMIT"]。