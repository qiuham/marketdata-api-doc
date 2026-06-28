---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/coin-margined-futures/account/websocket-api
api_type: WebSocket
updated_at: 2026-01-15T23:37:51.844816
---

# Futures Account Balance(USER_DATA)

## API Description[​](/docs/derivatives/coin-margined-futures/account/websocket-api#api-description "Direct link to API Description")

Query account balance info

## Method[​](/docs/derivatives/coin-margined-futures/account/websocket-api#method "Direct link to Method")

`account.balance`

## Request[​](/docs/derivatives/coin-margined-futures/account/websocket-api#request "Direct link to Request")
    
    
    {  
      "id": "9328e612-1560-4108-979e-283bf85b5acb",  
      "method": "account.balance",  
      "params": {  
        "apiKey": "",  
        "timestamp": 1727810404936,  
        "signature": "0f04368b2d22aafd0ggc8809ea34297eff602272917b5f01267db4efbc1c9422"  
       }  
    }  
    

## Request Weight[​](/docs/derivatives/coin-margined-futures/account/websocket-api#request-weight "Direct link to Request Weight")

**5**

## Request Parameters[​](/docs/derivatives/coin-margined-futures/account/websocket-api#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/derivatives/coin-margined-futures/account/websocket-api#response-example "Direct link to Response Example")
    
    
    {  
      "id": "9328e612-1560-4108-979e-283bf85b5acb",  
      "status": 200,  
      "result": [  
        {  
          "accountAlias": "fWAuTiuXoCuXmY",  
          "asset": "WLD",  
          "balance": "0.00000000",  
          "withdrawAvailable": "0.00000000",  
          "crossWalletBalance": "0.00000000",  
          "crossUnPnl": "0.00000000",  
          "availableBalance": "0.00000000",  
          "updateTime": 0  
        },  
        // ... ...  
      ],  
      "rateLimits": [  
        {  
          "rateLimitType": "REQUEST_WEIGHT",  
          "interval": "MINUTE",  
          "intervalNum": 1,  
          "limit": 2400,  
          "count": 10  
        }  
      ]  
    }

---

# 账户余额 (USER_DATA)

查询账户余额

## 方式[​](/docs/zh-CN/derivatives/coin-margined-futures/account/websocket-api#方式 "方式的直接链接")

`account.balance`

## 请求[​](/docs/zh-CN/derivatives/coin-margined-futures/account/websocket-api#请求 "请求的直接链接")
    
    
    {  
      "id": "9328e612-1560-4108-979e-283bf85b5acb",  
      "method": "account.balance",  
      "params": {  
        "apiKey": "",  
        "timestamp": 1727810404936,  
        "signature": "0f04368b2d22aafd0ggc8809ea34297eff602272917b5f01267db4efbc1c9422"  
       }  
    }  
    

## 请求权重[​](/docs/zh-CN/derivatives/coin-margined-futures/account/websocket-api#请求权重 "请求权重的直接链接")

**5**

## 请求参数[​](/docs/zh-CN/derivatives/coin-margined-futures/account/websocket-api#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/derivatives/coin-margined-futures/account/websocket-api#响应示例 "响应示例的直接链接")
    
    
    {  
      "id": "9328e612-1560-4108-979e-283bf85b5acb",  
      "status": 200,  
      "result": [  
        {  
          "accountAlias": "fWAuTiuXoCuXmY",  
          "asset": "WLD",  
          "balance": "0.00000000",  
          "withdrawAvailable": "0.00000000",  
          "crossWalletBalance": "0.00000000",  
          "crossUnPnl": "0.00000000",  
          "availableBalance": "0.00000000",  
          "updateTime": 0  
        },  
        // ... ...  
      ],  
      "rateLimits": [  
        {  
          "rateLimitType": "REQUEST_WEIGHT",  
          "interval": "MINUTE",  
          "intervalNum": 1,  
          "limit": 2400,  
          "count": 10  
        }  
      ]  
    }