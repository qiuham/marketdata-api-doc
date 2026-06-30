---
exchange: binance
source_url: https://developers.binance.com/docs/margin_trading/account/Get-Summary-Of-Margin-Account
api_type: Account
updated_at: 2026-06-30 19:06:38.616699
---

# Query Enabled Isolated Margin Account Limit (USER_DATA)

## API Description[​](/docs/margin_trading/account/Query-Enabled-Isolated-Margin-Account-Limit#api-description "Direct link to API Description")

Query enabled isolated margin account limit.

## HTTP Request[​](/docs/margin_trading/account/Query-Enabled-Isolated-Margin-Account-Limit#http-request "Direct link to HTTP Request")

GET `/sapi/v1/margin/isolated/accountLimit`

## Request Weight[​](/docs/margin_trading/account/Query-Enabled-Isolated-Margin-Account-Limit#request-weight "Direct link to Request Weight")

**1(IP)**

## Request Parameters[​](/docs/margin_trading/account/Query-Enabled-Isolated-Margin-Account-Limit#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
recvWindow| LONG| NO| No more than 60000  
timestamp| LONG| YES|   
  
## Response Example[​](/docs/margin_trading/account/Query-Enabled-Isolated-Margin-Account-Limit#response-example "Direct link to Response Example")
    
    
    {  
      "enabledAccount": 5,  
      "maxAccount": 20  
    }

---

# 查询杠杆逐仓账户启用限制 (USER_DATA)

## 接口描述[​](/docs/zh-CN/margin_trading/account/Query-Enabled-Isolated-Margin-Account-Limit#接口描述 "接口描述的直接链接")

查询杠杆逐仓账户启用限制。

## HTTP请求[​](/docs/zh-CN/margin_trading/account/Query-Enabled-Isolated-Margin-Account-Limit#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/margin/isolated/accountLimit`

## 请求权重[​](/docs/zh-CN/margin_trading/account/Query-Enabled-Isolated-Margin-Account-Limit#请求权重 "请求权重的直接链接")

**1(IP)**

## 请求参数[​](/docs/zh-CN/margin_trading/account/Query-Enabled-Isolated-Margin-Account-Limit#请求参数 "请求�参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
recvWindow| LONG| NO| 不能大于 `60000`  
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/margin_trading/account/Query-Enabled-Isolated-Margin-Account-Limit#响应示例 "响应示例的直接链接")
    
    
    {  
      "enabledAccount": 5,  
      "maxAccount": 20  
    }