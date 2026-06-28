---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/coin-margined-futures/account/rest-api/Futures-Account-Balance
api_type: Account
updated_at: 2026-01-15T23:37:32.359679
---

# Futures Account Balance (USER_DATA)

## API Description[​](/docs/derivatives/coin-margined-futures/account/rest-api/Futures-Account-Balance#api-description "Direct link to API Description")

Check futures account balance

## HTTP Request[​](/docs/derivatives/coin-margined-futures/account/rest-api/Futures-Account-Balance#http-request "Direct link to HTTP Request")

GET `/dapi/v1/balance`

## Request Weight[​](/docs/derivatives/coin-margined-futures/account/rest-api/Futures-Account-Balance#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/coin-margined-futures/account/rest-api/Futures-Account-Balance#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/derivatives/coin-margined-futures/account/rest-api/Futures-Account-Balance#response-example "Direct link to Response Example")
    
    
    [  
     	{  
     		"accountAlias": "SgsR",    // unique account code  
     		"asset": "BTC",  
     		"balance": "0.00250000",  
     		"withdrawAvailable": "0.00250000",  
     		"crossWalletBalance": "0.00241969",  
      		"crossUnPnl": "0.00000000",  
      		"availableBalance": "0.00241969",  
     		"updateTime": 1592468353979  
    	}  
    ]

---

# 账户余额(USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/coin-margined-futures/account/rest-api/Futures-Account-Balance#接口描述 "接口描述的直接链接")

查询账户余额

## HTTP请求[​](/docs/zh-CN/derivatives/coin-margined-futures/account/rest-api/Futures-Account-Balance#http请求 "HTTP请求的直接链接")

GET `/dapi/v1/balance`

## 请求权重[​](/docs/zh-CN/derivatives/coin-margined-futures/account/rest-api/Futures-Account-Balance#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/coin-margined-futures/account/rest-api/Futures-Account-Balance#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/derivatives/coin-margined-futures/account/rest-api/Futures-Account-Balance#响应示例 "响应示例的直接链接")
    
    
    [  
     	{  
     		"accountAlias": "SgsR",    // 账户唯一识别码  
     		"asset": "BTC",		// 资产  
     		"balance": "0.00250000",	// 账户余额  
     		"withdrawAvailable": "0.00250000", // 最大可提款金额,同`GET /dapi/account`中"maxWithdrawAmount"  
     		"crossWalletBalance": "0.00241969", // 全仓账户余额  
      		"crossUnPnl": "0.00000000",	// 全仓持仓未实现盈亏  
      		"availableBalance": "0.00241969",	 // 可用下单余额  
     		"updateTime": 1592468353979  
    	}  
    ]