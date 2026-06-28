---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/User-Commission-Rate
api_type: Account
updated_at: 2026-01-15T23:46:33.077242
---

# User Commission Rate (USER_DATA)

## API Description[​](/docs/derivatives/usds-margined-futures/account/rest-api/User-Commission-Rate#api-description "Direct link to API Description")

Get User Commission Rate

## HTTP Request[​](/docs/derivatives/usds-margined-futures/account/rest-api/User-Commission-Rate#http-request "Direct link to HTTP Request")

GET `/fapi/v1/commissionRate`

## Request Weight[​](/docs/derivatives/usds-margined-futures/account/rest-api/User-Commission-Rate#request-weight "Direct link to Request Weight")

**20**

## Request Parameters[​](/docs/derivatives/usds-margined-futures/account/rest-api/User-Commission-Rate#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/derivatives/usds-margined-futures/account/rest-api/User-Commission-Rate#response-example "Direct link to Response Example")
    
    
    {  
    	"symbol": "BTCUSDT",  
      	"makerCommissionRate": "0.0002",  // 0.02%  
      	"takerCommissionRate": "0.0004",  // 0.04%  
        "rpiCommissionRate": "0.00005"   // 0.005%  
    }

---

# 用户手续费率 (USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/User-Commission-Rate#接口描述 "接口描述的直接链接")

查询用户手续费率

## HTTP请求[​](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/User-Commission-Rate#http请求 "HTTP请求的直接链接")

GET `/fapi/v1/commissionRate`

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/User-Commission-Rate#请求权重 "请求权重的直接链接")

**20**

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/User-Commission-Rate#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/User-Commission-Rate#响应示例 "响应示例的直接链接")
    
    
    {  
    	"symbol": "BTCUSDT",  
      	"makerCommissionRate": "0.0002",  // 0.02%  
      	"takerCommissionRate": "0.0004",  // 0.04%  
    	"rpiCommissionRate": "0.00005"    // 0.005%  
    }