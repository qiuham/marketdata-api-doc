---
exchange: binance
source_url: https://developers.binance.com/docs/alpha/market-data/rest-api/klines
api_type: Market Data
updated_at: 2026-01-15T23:50:43.856790
---

# Klines (Candlestick Data)

## Endpoint: /bapi/defi/v1/public/alpha-trade/klines[​](/docs/alpha/market-data/rest-api/klines#endpoint-bapidefiv1publicalpha-tradeklines "Direct link to Endpoint: /bapi/defi/v1/public/alpha-trade/klines")

## Full URL Example[​](/docs/alpha/market-data/rest-api/klines#full-url-example "Direct link to Full URL Example")

[https://www.binance.com/bapi/defi/v1/public/alpha-trade/klines?interval=1h&limit=2&symbol=ALPHA_175USDT](https://www.binance.com/bapi/defi/v1/public/alpha-trade/klines?interval=1h&limit=2&symbol=ALPHA_175USDT)

## Description[​](/docs/alpha/market-data/rest-api/klines#description "Direct link to Description")

Fetches Kline/candlestick bars for a symbol, which include open/high/low/close prices and volume over intervals. Useful for charting and analysis.

## Parameters[​](/docs/alpha/market-data/rest-api/klines#parameters "Direct link to Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES| e.g., "ALPHA_175USDT" – use token ID from Token List  
interval| STRING| YES| e.g., "1h" – supported intervals: 1s, 15s, 1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w, 1M  
limit| INT| NO| default 500, max 1500 – number of klines to return  
startTime| LONG| NO| start timestamp in milliseconds  
endTime| LONG| NO| end timestamp in milliseconds  
  
## Response Structure[​](/docs/alpha/market-data/rest-api/klines#response-structure "Direct link to Response Structure")

  * `code`: String, response status code, "000000" indicates success.
  * `message`: String, typically used for optional messages or errors; empty here.
  * `messageDetail`: String, further details about the message; empty here.
  * `success`: Boolean, indicates whether the request was successful; here true.
  * `data`: Array of arrays, each inner array contains multiple string entries representing candlestick data: 
    1. Open time (timestamp in milliseconds as string), e.g., "1752642000000"
    2. Open price (string), e.g., "0.00171473"
    3. High price (string), e.g., "0.00172515"
    4. Low price (string), e.g., "0.00171473"
    5. Close price (string), e.g., "0.00172515"
    6. Volume (string), e.g., "1771.86000000"
    7. Close time (timestamp in milliseconds as string), e.g., "1752645599999"
    8. Quote asset volume (string), e.g., "3.05093481"
    9. Number of trades (integer as string), e.g., "2"
    10. Taker buy base asset volume (string), e.g., "1771.86000000"
    11. Taker buy quote asset volume (string), e.g., "3.05093481"
    12. 0 (static, please ignore)

---

# K线

## 接口：/bapi/defi/v1/public/alpha-trade/klines[​](/docs/zh-CN/alpha/market-data/rest-api/klines#接口bapidefiv1publicalpha-tradeklines "接口：/bapi/defi/v1/public/alpha-trade/klines的直接链接")

## 完整URL示例[​](/docs/zh-CN/alpha/market-data/rest-api/klines#完整url示例 "完整URL示例的直接链接")

[https://www.binance.com/bapi/defi/v1/public/alpha-trade/klines?interval=1h&limit=2&symbol=ALPHA_175USDT](https://www.binance.com/bapi/defi/v1/public/alpha-trade/klines?interval=1h&limit=2&symbol=ALPHA_175USDT)

## 描述[​](/docs/zh-CN/alpha/market-data/rest-api/klines#描述 "描述的直接链接")

获取某一交易对的K线/蜡烛图数据，包含开盘价、最高价、最低价、收盘价及成交量等信息，适用于图表绘制和行情分析。

## 参数[​](/docs/zh-CN/alpha/market-data/rest-api/klines#参数 "参数的直接链接")

名称| 类型| 是否必填| 描述  
---|---|---|---  
symbol| STRING| 是| 例如 "ALPHA_175USDT"，需使用Token列表中的代币ID  
interval| STRING| 是| 例如 "1h"，支持时间区间：1s, 15s, 1m、3m、5m、15m、30m、1h、2h、4h、6h、8h、12h、1d、3d、1w、1M  
limit| INT| 否| 默认500，最大1500，返回的K线数量  
startTime| LONG| 否| 起始时间戳（毫秒）  
endTime| LONG| 否| 结束时间戳（毫秒）  
  
## 响应结构[​](/docs/zh-CN/alpha/market-data/rest-api/klines#响应结构 "响应结构的直接链接")

  * `code`: 字符串，响应状态码，"000000"表示成功。
  * `message`: 字符串，通常用于返回附加消息或错误提示，此处为空。
  * `messageDetail`: 字符串，消息详细信息，此处为空。
  * `success`: 布尔值，表示请求是否成功，此处为true。
  * `data`: 嵌套数组，每个内层数组包含多个字符串，表示一根K线数据内容： 
    1. 开盘时间（毫秒时间戳，字符串），如 "1752642000000"
    2. 开盘价（字符串），如 "0.00171473"
    3. 最高价（字符串），如 "0.00172515"
    4. 最低价（字符串），如 "0.00171473"
    5. 收盘价（字符串），如 "0.00172515"
    6. 成交量（字符串），如 "1771.86000000"
    7. 收盘时间（毫秒时间戳，字符串），如 "1752645599999"
    8. 计价资产成交量（字符串），如 "3.05093481"
    9. 成交笔数（字符串整型），如 "2"
    10. 主动买入基础资产成交量（字符串），如 "1771.86000000"
    11. 主动买入计价资产成交量（字符串），如 "3.05093481"
    12. 静态值0，请忽略