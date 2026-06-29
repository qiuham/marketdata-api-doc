---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#spread-trading-rest-api-cancel-all-orders
anchor_id: spread-trading-rest-api-cancel-all-orders
api_type: REST
updated_at: 2026-06-29 19:57:02.485604
---

# Cancel All orders

Cancel all pending orders.

#### Rate Limit: 10 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/sprd/mass-cancel`

> Request Example
    
    
    POST /api/v5/sprd/mass-cancel
    body
    {
        "sprdId": "BTC-USDT_BTC-USDT-SWAP"
    }
    
    
    
    import okx.SpreadTrading as SpreadTrading
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading:0 , demo trading:1
    
    spreadAPI = SpreadTrading.SpreadTradingAPI(apikey, secretkey, passphrase, False, flag)
    
    # cancel all
    result = spreadAPI.cancel_all_orders(sprdId="BTC-USDT_BTC-USDT-SWAP")
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
sprdId | String | No | spread ID  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "result":true
            }
        ]
    }
    

#### Response Example

Parameter | Type | Description  
---|---|---  
result | Boolean | Result of the request `true`, `false`  
Getting a response with result=true means your request has been successfully received and will be processed. The result of the cancellation is subject to the state pushed by the order channel or the get order state.

---

# 全部撤单

撤销所有挂单

#### 限速：10次/2s

#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/sprd/mass-cancel`

> 请求示例
    
    
    POST /api/v5/sprd/mass-cancel
     body
     {
        "sprdId": "BTC-USDT_BTC-USDT-SWAP"
    }
    
    
    
    
    import okx.SpreadTrading as SpreadTrading
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘:1
    
    spreadAPI = SpreadTrading.SpreadTradingAPI(apikey, secretkey, passphrase, False, flag)
    
    # 全部撤单
    result = spreadAPI.cancel_all_orders(sprdId="BTC-USDT_BTC-USDT-SWAP")
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
sprdId | String | 否 | spread ID  
  
#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
result | Boolean | 请求结果`true`, `false`  
  
> 返回示例
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "result": true
            }
        ]
    }
    
    

返回结果中result=true 代表您的请求已被成功接收，并将会被处理。撤单的实际结果会通过`sprd-orders`频道推送。