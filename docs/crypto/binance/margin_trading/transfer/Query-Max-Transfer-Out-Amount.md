---
exchange: binance
source_url: https://developers.binance.com/docs/margin_trading/transfer/Query-Max-Transfer-Out-Amount
api_type: REST
updated_at: 2026-06-28 18:53:05.866337
---

# Query Max Transfer-Out Amount (USER_DATA)

## API Description[​](/docs/margin_trading/transfer/Query-Max-Transfer-Out-Amount#api-description "Direct link to API Description")

Query Max Transfer-Out Amount

## HTTP Request[​](/docs/margin_trading/transfer/Query-Max-Transfer-Out-Amount#http-request "Direct link to HTTP Request")

GET `/sapi/v1/margin/maxTransferable`

## Request Weight[​](/docs/margin_trading/transfer/Query-Max-Transfer-Out-Amount#request-weight "Direct link to Request Weight")

**50(IP)**

## Request Parameters[​](/docs/margin_trading/transfer/Query-Max-Transfer-Out-Amount#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
asset| STRING| YES|   
isolatedSymbol| STRING| NO| isolated symbol  
recvWindow| LONG| NO| The value cannot be greater than `60000`  
timestamp| LONG| YES|   
  
  * If isolatedSymbol is not sent, crossed margin data will be sent.



## Response Example[​](/docs/margin_trading/transfer/Query-Max-Transfer-Out-Amount#response-example "Direct link to Response Example")
    
    
     {  
          "amount": "3.59498107"  
     }

---

# 查询最大可转出额 (USER_DATA)

## 接口描述[​](/docs/zh-CN/margin_trading/transfer/Query-Max-Transfer-Out-Amount#接口描述 "接口描述的直接链接")

查询最大可转出额

## HTTP请求[​](/docs/zh-CN/margin_trading/transfer/Query-Max-Transfer-Out-Amount#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/margin/maxTransferable`

## 请求权重[​](/docs/zh-CN/margin_trading/transfer/Query-Max-Transfer-Out-Amount#请求权重 "请求权重的直接链接")

**50(IP)**

## 请求参数[​](/docs/zh-CN/margin_trading/transfer/Query-Max-Transfer-Out-Amount#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
asset| STRING| YES|   
isolatedSymbol| STRING| NO| 逐仓交易对，适用于逐仓查询  
recvWindow| LONG| NO| 默认值不能大于 `60000`  
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/margin_trading/transfer/Query-Max-Transfer-Out-Amount#响应示例 "响应示例的直接链接")
    
    
     {  
          "amount": "3.59498107"  
     }