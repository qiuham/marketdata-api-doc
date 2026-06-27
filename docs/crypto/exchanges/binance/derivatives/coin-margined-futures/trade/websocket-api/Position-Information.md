---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/websocket-api/Position-Information
api_type: WebSocket
updated_at: 2026-01-15T23:40:04.053935
---

# Position Information(USER_DATA)

## API Description[​](/docs/derivatives/coin-margined-futures/trade/websocket-api/Position-Information#api-description "Direct link to API Description")

Get current position information.

## Method[​](/docs/derivatives/coin-margined-futures/trade/websocket-api/Position-Information#method "Direct link to Method")

`account.position`

## Request[​](/docs/derivatives/coin-margined-futures/trade/websocket-api/Position-Information#request "Direct link to Request")
    
    
    {  
      "id": "233b8741-a96d-48e8-8ce1-160f43548aeb",  
      "method": "account.position",  
      "params": {  
        "apiKey": "",  
        "pair": "BTCUSD",  
        "timestamp": 1727825241779,  
        "signature": "0f04368b2d22aafd0ggc8809ea34297eff602272917b5f01267db4efbc1c9422"  
       }  
    }  
    

## Request Weight[​](/docs/derivatives/coin-margined-futures/trade/websocket-api/Position-Information#request-weight "Direct link to Request Weight")

**5**

## Request Parameters[​](/docs/derivatives/coin-margined-futures/trade/websocket-api/Position-Information#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
marginAsset| STRING| NO|   
pair| STRING| NO|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
**Note**

>   * Please use with user data stream `ACCOUNT_UPDATE` to meet your timeliness and accuracy needs.
> 


## Response Example[​](/docs/derivatives/coin-margined-futures/trade/websocket-api/Position-Information#response-example "Direct link to Response Example")
    
    
    {  
        "id": "233b8741-a96d-48e8-8ce1-160f43548aeb",  
        "status": 200,  
        "result": [  
            {  
                "symbol": "BTCUSD_PERP",  
                "positionAmt": "0",  
                "entryPrice": "0.00000000",  
                "markPrice": "62297.60417296",  
                "unRealizedProfit": "0.00000000",  
                "liquidationPrice": "0",  
                "leverage": "7",  
                "maxQty": "100",  
                "marginType": "cross",  
                "isolatedMargin": "0.00000000",  
                "isAutoAddMargin": "false",  
                "positionSide": "BOTH",  
                "notionalValue": "0",  
                "isolatedWallet": "0",  
                "updateTime": 1726731195634,  
                "breakEvenPrice": "0.00000000"  
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

# 用户持仓风险 (USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/coin-margined-futures/trade/websocket-api/Position-Information#接口描述 "接口描述的直接链接")

查询持仓风险

## 方式[​](/docs/zh-CN/derivatives/coin-margined-futures/trade/websocket-api/Position-Information#方式 "方式的直接链接")

`account.position`

## 请求[​](/docs/zh-CN/derivatives/coin-margined-futures/trade/websocket-api/Position-Information#请求 "请求的直接链接")
    
    
    {  
      "id": "233b8741-a96d-48e8-8ce1-160f43548aeb",  
      "method": "account.position",  
      "params": {  
        "apiKey": "",  
        "pair": "BTCUSD",  
        "timestamp": 1727825241779,  
        "signature": "0f04368b2d22aafd0ggc8809ea34297eff602272917b5f01267db4efbc1c9422"  
       }  
    }  
    

## 请求权重[​](/docs/zh-CN/derivatives/coin-margined-futures/trade/websocket-api/Position-Information#请求权重 "请求权重的直接链接")

**5**

## 请求参数[​](/docs/zh-CN/derivatives/coin-margined-futures/trade/websocket-api/Position-Information#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
marginAsset| STRING| NO|   
pair| STRING| NO|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
**注意**

>   * 请与账户推送信息`ACCOUNT_UPDATE`配合使用，以满足您的及时性和准确性需求。
> 


## 响应示例[​](/docs/zh-CN/derivatives/coin-margined-futures/trade/websocket-api/Position-Information#响应示例 "响应示例的直接链接")
    
    
    {  
        "id": "233b8741-a96d-48e8-8ce1-160f43548aeb",  
        "status": 200,  
        "result": [  
            {  
                "symbol": "BTCUSD_PERP",  
                "positionAmt": "0",  
                "entryPrice": "0.00000000",  
                "markPrice": "62297.60417296",  
                "unRealizedProfit": "0.00000000",  
                "liquidationPrice": "0",  
                "leverage": "7",  
                "maxQty": "100",  
                "marginType": "cross",  
                "isolatedMargin": "0.00000000",  
                "isAutoAddMargin": "false",  
                "positionSide": "BOTH",  
                "notionalValue": "0",  
                "isolatedWallet": "0",  
                "updateTime": 1726731195634,  
                "breakEvenPrice": "0.00000000"  
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