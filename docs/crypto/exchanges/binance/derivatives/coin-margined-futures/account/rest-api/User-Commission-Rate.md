---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/coin-margined-futures/account/rest-api/User-Commission-Rate
api_type: Account
updated_at: 2026-01-15T23:37:51.779127
---

# User Commission Rate (USER_DATA)

## API Description[​](/docs/derivatives/coin-margined-futures/account/rest-api/User-Commission-Rate#api-description "Direct link to API Description")

Query user commission rate

## HTTP Request[​](/docs/derivatives/coin-margined-futures/account/rest-api/User-Commission-Rate#http-request "Direct link to HTTP Request")

GET `/dapi/v1/commissionRate`

## Request Weight[​](/docs/derivatives/coin-margined-futures/account/rest-api/User-Commission-Rate#request-weight "Direct link to Request Weight")

**20**

## Request Parameters[​](/docs/derivatives/coin-margined-futures/account/rest-api/User-Commission-Rate#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/derivatives/coin-margined-futures/account/rest-api/User-Commission-Rate#response-example "Direct link to Response Example")
    
    
    {  
    	"symbol": "BTCUSD_PERP",  
      	"makerCommissionRate": "0.00015",  // 0.015%  
      	"takerCommissionRate": "0.00040"   // 0.040%  
    }

---

# 用户手续费率 (USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/coin-margined-futures/account/rest-api/User-Commission-Rate#接口描述 "接口描述的直接链接")

查询用户手续费率

## HTTP请求[​](/docs/zh-CN/derivatives/coin-margined-futures/account/rest-api/User-Commission-Rate#http请求 "HTTP请求的直接链接")

GET `/dapi/v1/commissionRate`

## 请求权重[​](/docs/zh-CN/derivatives/coin-margined-futures/account/rest-api/User-Commission-Rate#请求权重 "请求权重的直接链接")

**20**

## 请求参数[​](/docs/zh-CN/derivatives/coin-margined-futures/account/rest-api/User-Commission-Rate#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/derivatives/coin-margined-futures/account/rest-api/User-Commission-Rate#响应示例 "响应示例的直接链接")
    
    
    {  
    	"symbol": "BTCUSD_PERP",  
      	"makerCommissionRate": "0.00015",  // 0.015%  
      	"takerCommissionRate": "0.00040"   // 0.040%  
    }