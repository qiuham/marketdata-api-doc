---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Change-Multi-Assets-Mode
api_type: Trading
updated_at: 2026-01-15T23:47:13.359404
---

# Change Multi-Assets Mode (TRADE)

## API Description[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Change-Multi-Assets-Mode#api-description "Direct link to API Description")

Change user's Multi-Assets mode (Multi-Assets Mode or Single-Asset Mode) on _**Every symbol**_

## HTTP Request[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Change-Multi-Assets-Mode#http-request "Direct link to HTTP Request")

POST `/fapi/v1/multiAssetsMargin`

## Request Weight[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Change-Multi-Assets-Mode#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Change-Multi-Assets-Mode#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
multiAssetsMargin| STRING| YES| "true": Multi-Assets Mode; "false": Single-Asset Mode  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Change-Multi-Assets-Mode#response-example "Direct link to Response Example")
    
    
    {  
    	"code": 200,  
    	"msg": "success"  
    }

---

# 更改联合保证金模式(TRADE)

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Change-Multi-Assets-Mode#接口描述 "接口描述的直接链接")

变换用户在 _**所有symbol**_ 合约上的联合保证金模式：开启或关闭联合保证金模式。

## HTTP请求[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Change-Multi-Assets-Mode#http请求 "HTTP请求的直接链接")

POST `/fapi/v1/multiAssetsMargin`

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Change-Multi-Assets-Mode#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Change-Multi-Assets-Mode#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
multiAssetsMargin| STRING| YES| "true": 联合保证金模式开启；"false": 联合保证金模式关闭  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Change-Multi-Assets-Mode#响应示例 "响应示例的直接链接")
    
    
    {  
    	"code": 200,  
    	"msg": "success"  
    }