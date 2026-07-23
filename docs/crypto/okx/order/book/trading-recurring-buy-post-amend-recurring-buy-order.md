---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-recurring-buy-post-amend-recurring-buy-order
anchor_id: order-book-trading-recurring-buy-post-amend-recurring-buy-order
api_type: API
updated_at: 2026-07-23 19:21:42.715939
---

# POST / Amend recurring buy order

#### Rate Limit: 20 requests per 2 seconds  
  
#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/tradingBot/recurring/amend-order-algo`

> Request Example
    
    
    POST /api/v5/tradingBot/recurring/amend-order-algo
    body
    {
        "algoId":"448965992920907776",
        "stgyName":"stg1"
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
algoId | String | Yes | Algo ID  
stgyName | String | Yes | New custom name for trading bot after adjustment, no more than 40 characters  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "algoId":"448965992920907776",
                "algoClOrdId":"",
                "sCode":"0",
                "sMsg":""
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
algoId | String | Algo ID  
algoClOrdId | String | Client-supplied Algo ID  
sCode | String | The code of the event execution result, 0 means success  
sMsg | String | Rejection message if the request is unsuccessful

---

# POST / 修改定投策略订单

#### 限速：20次/2s  
  
#### 限速规则：User ID

#### HTTP请求

`POST /api/v5/tradingBot/recurring/amend-order-algo`

> 请求示例
    
    
    POST /api/v5/tradingBot/recurring/amend-order-algo
    body
    {
        "algoId":"448965992920907776",
        "stgyName":"stg1"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoId | String | 是 | 策略订单ID  
stgyName | String | 是 | 调整后的策略自定义名称  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "algoId":"448965992920907776",
                "algoClOrdId":"",
                "sCode":"0",
                "sMsg":""
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
algoId | String | 策略订单ID  
algoClOrdId | String | 客户自定义订单ID  
sCode | String | 事件执行结果的code，0代表成功  
sMsg | String | 事件执行失败时的msg