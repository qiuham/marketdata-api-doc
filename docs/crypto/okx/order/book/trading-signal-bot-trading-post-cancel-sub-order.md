---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-signal-bot-trading-post-cancel-sub-order
anchor_id: order-book-trading-signal-bot-trading-post-cancel-sub-order
api_type: API
updated_at: 2026-07-06 19:53:10.197571
---

# POST / Cancel sub order

Cancel an incomplete order.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/tradingBot/signal/cancel-sub-order`

> Request Example
    
    
    POST /api/v5/tradingBot/signal/cancel-sub-order
    body
    {
        "algoId":"91664",
        "signalOrdId":"590908157585625111",
        "instId":"BTC-USDT-SWAP"
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
algoId | String | Yes | Algo ID  
instId | String | Yes | Instrument ID, e.g. BTC-USDT-SWAP  
signalOrdId | String | Yes | Order ID  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "signalOrdId":"590908157585625111",
                "sCode":"0",
                "sMsg":""
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
code | String | The result code, `0` means success  
msg | String | The error message, empty if the code is 0  
data | Array of objects | Array of objects contains the response results  
> signalOrdId | String | Order ID  
> sCode | String | The code of the event execution result, `0` means success.  
> sMsg | String | Rejection or success message of event execution.  
Cancel order returns with sCode equal to 0. It is not strictly considered that the order has been canceled. It only means that your cancellation request has been accepted by the system server. The result of the cancellation is subject to the state by get sub orders endpoint.

---

# POST / 撤单

撤销之前下的未完成订单。

#### 限速：20次/2s

#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/tradingBot/signal/cancel-sub-order`

> 请求示例
    
    
    POST /api/v5/tradingBot/signal/cancel-sub-order
    body
    {
        "algoId":"91664",
        "signalOrdId":"590908157585625111",
        "instId":"BTC-USDT-SWAP"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoId | String | 是 | 策略ID  
instId | String | 是 | 产品ID，如 BTC-USDT-SWAP  
signalOrdId | String | 是 | 订单ID  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "signalOrdId":"590908157585625111",
                "sCode":"0",
                "sMsg":""
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
code | String | 结果代码，`0`表示成功  
msg | String | 错误信息，代码为0时，该字段为空  
data | Array of objects | 包含结果的对象数组  
> signalOrdId | String | 订单ID  
> sCode | String | 事件执行结果的code，0代表成功  
> sMsg | String | 事件执行失败时的msg  
撤单返回sCode等于0不能严格认为该订单已经被撤销，只表示您的撤单请求被系统服务器所接受，撤单结果以者查询订单状态为准