---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-signal-bot-trading-post-cancel-signal-bots
anchor_id: order-book-trading-signal-bot-trading-post-cancel-signal-bots
api_type: API
updated_at: 2026-07-13 19:27:50.111527
---

# POST / Cancel signal bots

A maximum of 10 orders can be stopped per request.  
  
#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/tradingBot/signal/stop-order-algo`

> Request Example
    
    
    POST /api/v5/tradingBot/signal/stop-order-algo
    body
    [
        {
            "algoId":"448965992920907776"
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
                "algoId": "448965992920907776",
                "sCode": "0",
                "sMsg": "",
                "algoClOrdId": ""
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
algoId | String | Algo ID  
sCode | String | The code of the event execution result, `0` means success.  
sMsg | String | Rejection or success message of event execution.  
algoClOrdId | String | Client-supplied Algo ID

---

# POST / 停止信号策略

每次最多可以撤销10个信号策略。  
  
#### 限速：20次/2s

#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/tradingBot/signal/stop-order-algo`

> 请求示例
    
    
    POST /api/v5/tradingBot/signal/stop-order-algo
    body
    [
        {
            "algoId":"448965992920907776"
        }
    ]
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoId | String | 是 | 策略ID  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "algoId": "448965992920907776",
                "sCode": "0",
                "sMsg": "",
                "algoClOrdId": ""
    
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
algoId | String | 策略ID  
sCode | String | 事件执行结果的code，0代表成功  
sMsg | String | 事件执行失败时的msg  
algoClOrdId | String | 客户自定义订单ID