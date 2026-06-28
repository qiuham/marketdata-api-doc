---
exchange: binance
source_url: https://developers.binance.com/docs/alpha/market-data/rest-api/aggregated-trades
api_type: Market Data
updated_at: 2026-01-15T23:50:42.026165
---

# Aggregated Trades

## Endpoint: /bapi/defi/v1/public/alpha-trade/agg-trades[​](/docs/alpha/market-data/rest-api/aggregated-trades#endpoint-bapidefiv1publicalpha-tradeagg-trades "Direct link to Endpoint: /bapi/defi/v1/public/alpha-trade/agg-trades")

## Full URL Example[​](/docs/alpha/market-data/rest-api/aggregated-trades#full-url-example "Direct link to Full URL Example")

<https://www.binance.com/bapi/defi/v1/public/alpha-trade/agg-trades?symbol=ALPHA_118USDC>

## Description[​](/docs/alpha/market-data/rest-api/aggregated-trades#description "Direct link to Description")

Retrieves compressed, aggregated historical trades for a specific symbol. Useful for recent trade history.

## Parameters[​](/docs/alpha/market-data/rest-api/aggregated-trades#parameters "Direct link to Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES| e.g., "ALPHA_118USDC" – use token ID from Token List  
fromId| LONG| NO| starting trade ID to fetch from  
startTime| LONG| NO| start timestamp (milliseconds)  
endTime| LONG| NO| end timestamp (milliseconds)  
limit| INT| NO| number of results to return (default 500, max 1000)  
  
## Response Structure[​](/docs/alpha/market-data/rest-api/aggregated-trades#response-structure "Direct link to Response Structure")

Array of objects, each representing an aggregated trade:

  * `a`: Integer (aggregate trade ID)
  * `p`: String (price)
  * `q`: String (quantity)
  * `f`: Integer (first trade ID)
  * `l`: Integer (last trade ID)
  * `T`: Integer (timestamp)
  * `m`: Boolean (true if buyer is market maker) ← deprecated field, can ignore

---

# 聚合交易查询

## 接口：/bapi/defi/v1/public/alpha-trade/agg-trades[​](/docs/zh-CN/alpha/market-data/rest-api/aggregated-trades#接口bapidefiv1publicalpha-tradeagg-trades "接口：/bapi/defi/v1/public/alpha-trade/agg-trades的直接链接")

## 完整URL示例[​](/docs/zh-CN/alpha/market-data/rest-api/aggregated-trades#完整url示例 "完整URL示例的直接链接")

<https://www.binance.com/bapi/defi/v1/public/alpha-trade/agg-trades?symbol=ALPHA_118USDC>

## 描述[​](/docs/zh-CN/alpha/market-data/rest-api/aggregated-trades#描述 "描述的直接链接")

获取指定交易对的压缩聚合历史成交数据，适用于查询近期成交记录。

## 参数[​](/docs/zh-CN/alpha/market-data/rest-api/aggregated-trades#参数 "参数的直接链接")

名称| 类型| 是否必填| 描述  
---|---|---|---  
symbol| STRING| 是| 例如 "ALPHA_118USDC"，需使用Token列表中的代币ID  
fromId| LONG| 否| 起始成交ID  
startTime| LONG| 否| 起始时间戳（毫秒）  
endTime| LONG| 否| 结束时间戳（毫秒）  
limit| INT| 否| 返回结果数量（默认500，最大1000）  
  
## 响应结构[​](/docs/zh-CN/alpha/market-data/rest-api/aggregated-trades#响应结构 "响应结构的直接链接")

对象数组，每个对象代表一条聚合成交：

  * `a`: 整数，聚合成交ID
  * `p`: 字符串，价格
  * `q`: 字符串，数量
  * `f`: 整数，首笔成交ID
  * `l`: 整数，末笔成交ID
  * `T`: 整数，时间戳
  * `m`: 布尔值（买方是否是做市商），该字段已废弃，可忽略