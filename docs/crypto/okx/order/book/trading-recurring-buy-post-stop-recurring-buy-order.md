---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-recurring-buy-post-stop-recurring-buy-order
anchor_id: order-book-trading-recurring-buy-post-stop-recurring-buy-order
api_type: API
updated_at: 2026-07-09 19:37:23.970769
---

# POST / Stop recurring buy order

A maximum of 10 orders can be stopped per request.  
  
#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/tradingBot/recurring/stop-order-algo`

> Request Example
    
    
    POST /api/v5/tradingBot/recurring/stop-order-algo
    body
    [
        {
            "algoId":"560472804207104000"
        }
    ]
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
algoId | String | Yes | Algo ID  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "algoClOrdId": "",
                "algoId": "1839309556514557952",
                "sCode": "0",
                "sMsg": "",
                "tag": ""
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
algoId | String | Algo ID  
algoClOrdId | String | Client-supplied Algo ID  
sCode | String | The code of the event execution result, 0 means success  
sMsg | String | Rejection message if the request is unsuccessful  
tag | String | ~~Order tag~~(Deprecated)

---

# POST / 定投策略停止

每次最多可以撤销10个定投策略订单。  
  
#### 限速：20次/2s

#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/tradingBot/recurring/stop-order-algo`

> 请求示例
    
    
    POST /api/v5/tradingBot/recurring/stop-order-algo
    body
    [
        {
            "algoId":"560472804207104000"
        }
    ]
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoId | String | 是 | 策略订单ID  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "algoClOrdId": "",
                "algoId": "1839309556514557952",
                "sCode": "0",
                "sMsg": "",
                "tag": ""
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
algoId | String | 策略订单ID  
algoClOrdId | String | 客户自定义订单ID  
sCode | String | 事件执行结果的code，0代表成功  
sMsg | String | 事件执行失败时的msg  
tag | String | ~~订单标签~~ （已废弃）