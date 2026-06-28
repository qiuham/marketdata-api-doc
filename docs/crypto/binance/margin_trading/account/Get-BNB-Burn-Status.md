---
exchange: binance
source_url: https://developers.binance.com/docs/margin_trading/account/Get-BNB-Burn-Status
api_type: Account
updated_at: 2026-05-27 18:56:11.308375
---

# Get Summary of Margin account (USER_DATA)

## API Description[​](/docs/margin_trading/account/Get-Summary-Of-Margin-Account#api-description "Direct link to API Description")

Get personal margin level information

## HTTP Request[​](/docs/margin_trading/account/Get-Summary-Of-Margin-Account#http-request "Direct link to HTTP Request")

GET `/sapi/v1/margin/tradeCoeff`

## Request Weight[​](/docs/margin_trading/account/Get-Summary-Of-Margin-Account#request-weight "Direct link to Request Weight")

**10(IP)**

## Request Parameters[​](/docs/margin_trading/account/Get-Summary-Of-Margin-Account#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/margin_trading/account/Get-Summary-Of-Margin-Account#response-example "Direct link to Response Example")
    
    
    {  
      "normalBar": "1.5",  
      "marginCallBar": "1.3",  
      "forceLiquidationBar": "1.1"  
    }

---

# 查询Margin账户信息汇总 (USER_DATA)

## 接口描述[​](/docs/zh-CN/margin_trading/account/Get-Summary-Of-Margin-Account#接口描述 "接口描述的直接链接")

获取用户个人杠杆账户信息汇总

## HTTP请求[​](/docs/zh-CN/margin_trading/account/Get-Summary-Of-Margin-Account#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/margin/tradeCoeff`

## 请求权重[​](/docs/zh-CN/margin_trading/account/Get-Summary-Of-Margin-Account#请求权重 "请求权重的直接链接")

**10(IP)**

## 请求参数[​](/docs/zh-CN/margin_trading/account/Get-Summary-Of-Margin-Account#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/margin_trading/account/Get-Summary-Of-Margin-Account#响应示例 "响应示例的直接链接")
    
    
    {  
      "normalBar": "1.5",  
      "marginCallBar": "1.3",  
      "forceLiquidationBar": "1.1"  
    }