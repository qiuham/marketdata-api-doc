---
exchange: binance
source_url: https://developers.binance.com/docs/margin_trading/trade/Query-Special-Key-of-Low-Latency-Trading
api_type: Trading
updated_at: 2026-06-29 19:10:40.839250
---

# Small Liability Exchange (MARGIN)

## API Description[​](/docs/margin_trading/trade/Small-Liability-Exchange#api-description "Direct link to API Description")

Small Liability Exchange

## HTTP Request[​](/docs/margin_trading/trade/Small-Liability-Exchange#http-request "Direct link to HTTP Request")

POST `/sapi/v1/margin/exchange-small-liability`

## Request Weight[​](/docs/margin_trading/trade/Small-Liability-Exchange#request-weight "Direct link to Request Weight")

**3000(UID)**

## Request Parameters[​](/docs/margin_trading/trade/Small-Liability-Exchange#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
assetNames| ARRAY| YES| The assets list of small liability exchange， Example: assetNames = BTC,ETH  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
  * Only convert once within 6 hours
  * Only liability valuation less than 10 USDT are supported
  * The maximum number of coin is 10



## Response Example[​](/docs/margin_trading/trade/Small-Liability-Exchange#response-example "Direct link to Response Example")

---

# 全仓杠杆小额负债转换 (MARGIN)

## 接口描述[​](/docs/zh-CN/margin_trading/trade/Small-Liability-Exchange#接口描述 "接口描述的直接链接")

全仓杠杆小额负债转换

## HTTP请求[​](/docs/zh-CN/margin_trading/trade/Small-Liability-Exchange#http请求 "HTTP请求的直接链接")

POST `/sapi/v1/margin/exchange-small-liability`

## 请求权重[​](/docs/zh-CN/margin_trading/trade/Small-Liability-Exchange#请求权重 "请求权重的直接链接")

**3000(UID)**

## 请求参数[​](/docs/zh-CN/margin_trading/trade/Small-Liability-Exchange#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
assetNames| ARRAY| YES| 小额转换的资产列表，举例: assetNames = BTC,ETH  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
  * 兑换请求限流6小时一次
  * 币种负债小于10USDT
  * 币种数量最大10个



## 响应示例[​](/docs/zh-CN/margin_trading/trade/Small-Liability-Exchange#响应示例 "响应示例的直接链接")