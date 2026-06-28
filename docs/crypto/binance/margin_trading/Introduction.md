---
exchange: binance
source_url: https://developers.binance.com/docs/margin_trading/Introduction
api_type: REST
updated_at: 2026-05-27 18:56:05.787404
---

# Disable Isolated Margin Account (TRADE)

## API Description[​](/docs/margin_trading/account/Disable-Isolated-Margin-Account#api-description "Direct link to API Description")

Disable isolated margin account for a specific symbol. Each trading pair can only be deactivated once every 24 hours.

## HTTP Request[​](/docs/margin_trading/account/Disable-Isolated-Margin-Account#http-request "Direct link to HTTP Request")

DELETE `/sapi/v1/margin/isolated/account`

## Request Weight[​](/docs/margin_trading/account/Disable-Isolated-Margin-Account#request-weight "Direct link to Request Weight")

**300(UID)**

## Request Parameters[​](/docs/margin_trading/account/Disable-Isolated-Margin-Account#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
recvWindow| LONG| NO| No more than 60000  
timestamp| LONG| YES|   
  
## Response Example[​](/docs/margin_trading/account/Disable-Isolated-Margin-Account#response-example "Direct link to Response Example")
    
    
    {  
      "success": true,  
      "symbol": "BTCUSDT"  
    }

---

# 杠杆逐仓账户停用 (TRADE)

## 接口描述[​](/docs/zh-CN/margin_trading/account/Disable-Isolated-Margin-Account#接口描述 "接口描述的直接链接")

停用特定交易对的杠杆逐仓账户。每个交易对 24 小时内仅可停用一次。

## HTTP请求[​](/docs/zh-CN/margin_trading/account/Disable-Isolated-Margin-Account#http请求 "HTTP请求的直接链接")

DELETE `/sapi/v1/margin/isolated/account`

## 请求权重[​](/docs/zh-CN/margin_trading/account/Disable-Isolated-Margin-Account#请求权重 "请求权重的直接链接")

**300(UID)**

## 请求参数[​](/docs/zh-CN/margin_trading/account/Disable-Isolated-Margin-Account#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES|   
recvWindow| LONG| NO| 不能大于 `60000`  
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/margin_trading/account/Disable-Isolated-Margin-Account#响应示例 "响应示例的直接链接")
    
    
    {  
      "success": true,  
      "symbol": "BTCUSDT"  
    }