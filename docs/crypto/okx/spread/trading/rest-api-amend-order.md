---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#spread-trading-rest-api-amend-order
anchor_id: spread-trading-rest-api-amend-order
api_type: REST
updated_at: 2026-07-06 19:53:51.088921
---

# Amend order

Amend an incomplete order.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/sprd/amend-order`

> Request Example
    
    
    POST /api/v5/sprd/amend-order
    body
    {
        "ordId":"2510789768709120",
        "newSz":"2"
    }
    
    

#### Response parameters

Parameter | Type | Required | Description  
---|---|---|---  
ordId | String | Conditional | Order ID   
Either `ordId` or `clOrdId` is required. If both are passed, ordId will be used.  
clOrdId | String | Conditional | Client Order ID as assigned by the client  
reqId | String | No | Client Request ID as assigned by the client for order amendment   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.   
The response will include the corresponding reqId to help you identify the request if you provide it in the request.  
newSz | String | Conditional | New quantity after amendment   
Either `newSz` or `newPx` is required.   
When amending a partially-filled order, the newSz should include the amount that has been filled.  
newPx | String | Conditional | New price after amendment   
Either `newSz` or `newPx` is required.  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
             "clOrdId":"",
             "ordId":"12344",
             "reqId":"b12344",
             "sCode":"0",
             "sMsg":""
            }
        ]
    }
    
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ordId | String | Order ID  
clOrdId | String | Client Order ID as assigned by the client.  
reqId | String | Client Request ID as assigned by the client for order amendment.  
sCode | String | The code of the event execution result, 0 means success.  
sMsg | String | Rejection message if the request is unsuccessful.  
newSz  
If the new quantity of the order is less than or equal to the (accFillSz + canceledSz + pendingSettleSz), after pendingSettleSz is settled, the order status will be transitioned into filled (if canceledSz = 0), or canceled (if canceledSz > 0).  The amend order returns sCode equal to 0  
It is not strictly considered that the order has been amended. It only means that your amend order request has been accepted by the system server. The result of the amend is subject to the status pushed by the order channel or the order status query.

---

# 修改订单

修改当前未成交的挂单  

#### 限速：20次/2s

#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/sprd/amend-order`

> 请求示例
    
    
    POST /api/v5/sprd/amend-order
    body
    {
        "ordId":"2510789768709120",
        "newSz":"2"
    }
    
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
ordId | String | 可选 | 订单ID， `ordId`和`clOrdId`必须传一个，若传两个，以`ordId`为主  
clOrdId | String | 可选 | 用户自定义order ID  
reqId | String | 否 | 用户自定义修改事件ID  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度要在1-32位之间。  
newSz | String | 可选 | 修改的新数量，对于部分成交订单，该数量应包含已成交数量。   
`newSz` 和 `newPx`不可同时为空。  
newPx | String | 可选 | 修改后的新价格。  
`newSz` 和 `newPx`不可同时为空。  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
             "clOrdId":"",
             "ordId":"12344",
             "reqId":"b12344",
             "sCode":"0",
             "sMsg":""
            }
        ]
    }
    
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ordId | String | 订单ID  
clOrdId | String | 用户自定义order ID  
reqId | String | 用户自定义修改事件ID  
sCode | String | 事件执行结果的code，0代表成功  
sMsg | String | 事件执行失败或成功时的msg  
newSz  
若修改订单时，订单修改后的新数量小于或等于 (accFillSz + canceledSz + pendingSettleSz)，在 pendingSettleSz 结算后，订单状态会根据 canceledSz 的不同而不同。当 canceledSz = 0，订单状态将被改为 filled；当 canceledSz > 0，订单状态将被改为 canceled。  修改订单返回sCode等于0不能严格认为该订单已经被修改，只表示您的修改订单请求被系统服务器所接受，改单结果以订单频道推送的状态或者查询订单状态为准