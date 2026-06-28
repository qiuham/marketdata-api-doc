---
exchange: binance
source_url: https://developers.binance.com/docs/alpha/market-data/rest-api/24hr-ticker-price-change
api_type: Market Data
updated_at: 2026-01-15T23:50:41.963892
---

# Ticker (24hr Price Statistics)

## Endpoint: /bapi/defi/v1/public/alpha-trade/ticker[​](/docs/alpha/market-data/rest-api/24hr-ticker-price-change#endpoint-bapidefiv1publicalpha-tradeticker "Direct link to Endpoint: /bapi/defi/v1/public/alpha-trade/ticker")

## Full URL Example[​](/docs/alpha/market-data/rest-api/24hr-ticker-price-change#full-url-example "Direct link to Full URL Example")

<https://www.binance.com/bapi/defi/v1/public/alpha-trade/ticker?symbol=ALPHA_175USDT>

## Description[​](/docs/alpha/market-data/rest-api/24hr-ticker-price-change#description "Direct link to Description")

Gets the 24-hour rolling window price change statistics for a symbol, including volume and price changes.

## Parameters[​](/docs/alpha/market-data/rest-api/24hr-ticker-price-change#parameters "Direct link to Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES| e.g., "ALPHA_175USDT" – use token ID from Token List  
  
## Response Structure[​](/docs/alpha/market-data/rest-api/24hr-ticker-price-change#response-structure "Direct link to Response Structure")

  * `code`: String, Response status code; "000000" indicates success.
  * `message`: String, Optional message or error detail; none here.
  * `messageDetail`: String, Additional message details; none here.
  * `success`: Boolean, Indicates request success; here true.
  * `data`: Object containing ticker information for a trading symbol, with fields: 
    * `symbol`: String, trading pair symbol, e.g., "ALPHA_175USDT"
    * `priceChange`: String, absolute price change during the period, e.g., "-0.00025072"
    * `priceChangePercent`: String, percentage price change during the period, e.g., "-12.742" (%)
    * `weightedAvgPrice`: String, weighted average price over the period, e.g., "0.00174014"
    * `lastPrice`: String, latest traded price, e.g., "0.00171695"
    * `lastQty`: String, quantity of the last trade, e.g., "11587.95000000"
    * `openPrice`: String, opening price of the period, e.g., "0.00196767"
    * `highPrice`: String, highest price during the period, e.g., "0.00197493"
    * `lowPrice`: String, lowest price during the period, e.g., "0.00166000"
    * `volume`: String, trading volume (base asset) during the period, e.g., "4664046.98000000"
    * `quoteVolume`: String, trading volume in quote asset during the period, e.g., "8116.07360317"
    * `openTime`: Integer (timestamp in milliseconds), period start time, e.g., 1752568680000
    * `closeTime`: Integer (timestamp in milliseconds), period end time, e.g., 1752654774140
    * `firstId`: Integer, trade ID of the first trade in the period, e.g., 58470
    * `lastId`: Integer, trade ID of the last trade in the period, e.g., 58665
    * `count`: Integer, total number of trades during the period, e.g., 258

---

# 24hr价格变动情况

## 接口：/bapi/defi/v1/public/alpha-trade/ticker[​](/docs/zh-CN/alpha/market-data/rest-api/24hr-ticker-price-change#接口bapidefiv1publicalpha-tradeticker "接口：/bapi/defi/v1/public/alpha-trade/ticker的直接链接")

## 完整URL示例[​](/docs/zh-CN/alpha/market-data/rest-api/24hr-ticker-price-change#完整url示例 "完整URL示例的直接链接")

<https://www.binance.com/bapi/defi/v1/public/alpha-trade/ticker?symbol=ALPHA_175USDT>

## 描述[​](/docs/zh-CN/alpha/market-data/rest-api/24hr-ticker-price-change#描述 "描述的直接链接")

获取某交易对24小时滚动窗口的价格变动统计信息，包括成交量和价格变化。

## 参数[​](/docs/zh-CN/alpha/market-data/rest-api/24hr-ticker-price-change#参数 "参数的直接链接")

名称| 类型| 是否必填| 描述  
---|---|---|---  
symbol| STRING| 是| 例如 "ALPHA_175USDT"，需使用Token列表中的代币ID  
  
## 响应结构[​](/docs/zh-CN/alpha/market-data/rest-api/24hr-ticker-price-change#响应结构 "响应结构的直接链接")

  * `code`: 字符串，响应状态码；"000000"表示成功。
  * `message`: 字符串，可选信息或错误详情，此处无。
  * `messageDetail`: 字符串，附加消息详情，此处无。
  * `success`: 布尔值，表示请求是否成功，此处为true。
  * `data`: 对象，包含交易对的行情信息，字段包括： 
    * `symbol`: 字符串，交易对符号，如 "ALPHA_175USDT"
    * `priceChange`: 字符串，期间绝对价格变动，如 "-0.00025072"
    * `priceChangePercent`: 字符串，期间价格变动百分比，如 "-12.742"（%）
    * `weightedAvgPrice`: 字符串，期间加权平均价格，如 "0.00174014"
    * `lastPrice`: 字符串，最新成交价，如 "0.00171695"
    * `lastQty`: 字符串，最后一笔成交量，如 "11587.95000000"
    * `openPrice`: 字符串，期间开盘价，如 "0.00196767"
    * `highPrice`: 字符串，期间最高价，如 "0.00197493"
    * `lowPrice`: 字符串，期间最低价，如 "0.00166000"
    * `volume`: 字符串，期间基础资产成交量，如 "4664046.98000000"
    * `quoteVolume`: 字符串，期间计价资产成交量，如 "8116.07360317"
    * `openTime`: 整数（毫秒时间戳），期间开始时间，如 1752568680000
    * `closeTime`: 整数（毫秒时间戳），期间结束时间，如 1752654774140
    * `firstId`: 整数，期间第一笔成交ID，如 58470
    * `lastId`: 整数，期间最后一笔成交ID，如 58665
    * `count`: 整数，期间成交总数，如 258