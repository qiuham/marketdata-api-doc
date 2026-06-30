---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#spread-trading-rest-api-cancel-order
anchor_id: spread-trading-rest-api-cancel-order
api_type: REST
updated_at: 2026-06-30 19:55:34.337781
---

# Cancel order

Cancel an incomplete order.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/sprd/cancel-order`

> Request Example
    
    
    POST /api/v5/sprd/cancel-order
    body
    {
        "ordId":"2510789768709120"
    }
    
    
    
    import okx.SpreadTrading as SpreadTrading
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading:0 , demo trading:1
    
    spreadAPI = SpreadTrading.SpreadTradingAPI(apikey, secretkey, passphrase, False, flag)
    
    # cancel order
    result = spreadAPI.cancel_order(ordId='1905309079888199680')
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
ordId | String | Conditional | Order ID   
Either `ordId` or `clOrdId` is required. If both are passed, `ordId` will be used.  
clOrdId | String | Conditional | Client Order ID as assigned by the client  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "clOrdId":"oktswap6",
                "ordId":"12345689",
                "sCode":"0",
                "sMsg":""
            }
        ]
    }
    

#### Response Example

Parameter | Type | Description  
---|---|---  
ordId | String | Order ID  
clOrdId | String | Client Order ID as assigned by the client  
sCode | String | The code of the event execution result, 0 means success.  
sMsg | String | Rejection message if the request is unsuccessful.  
Cancel order returns with sCode equal to 0. It is not strictly considered that the order has been canceled. It only means that your cancellation request has been accepted by the system server. The result of the cancellation is subject to the state pushed by the order channel or the get order state.

---

# 撤单

撤销之前下的未完成订单。

#### 限速：20次/2s

#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/sprd/cancel-order`

> 请求示例
    
    
    POST /api/v5/sprd/cancel-order
    body
    {
        "ordId":"2510789768709120"
    }
    
    
    
    
    import okx.SpreadTrading as SpreadTrading
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘:1
    
    spreadAPI = SpreadTrading.SpreadTradingAPI(apikey, secretkey, passphrase, False, flag)
    
    # 撤单
    result = spreadAPI.cancel_order(ordId='1905309079888199680')
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
ordId | String | 可选 | 订单ID， `ordId`和`clOrdId`必须传一个，若传两个，以`ordId`为主  
clOrdId | String | 可选 | 用户自定义ID  
  
> 返回示例
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "clOrdId": "oktswap6",
                "ordId": "12345689",
                "sCode": "0",
                "sMsg": ""
            }
        ]
    }
    
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ordId | String | 订单ID  
clOrdId | String | 客户自定义订单ID  
sCode | String | 事件执行结果的code，0代表成功  
sMsg | String | 事件执行失败时的msg  
撤单返回sCode等于0不能严格认为该订单已经被撤销，只表示您的撤单请求被系统服务器所接受，撤单结果以订单频道推送的状态或者查询订单状态为准