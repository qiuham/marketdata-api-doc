---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#spread-trading-websocket-trade-api-ws-amend-order
anchor_id: spread-trading-websocket-trade-api-ws-amend-order
api_type: WebSocket
updated_at: 2026-07-10 19:31:49.249401
---

# WS / Amend order

Amend an incomplete order.

#### URL Path

/ws/v5/business (required login)

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

Rate limit is shared with the `Amend order` REST API endpoints 

> Request Example
    
    
    {
       "id":"1512",
       "op":"sprd-amend-order",
       "args":[
          {
             "ordId":"2510789768709120",
             "newSz":"2"
          }
       ]
    }
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
id | String | Yes | Unique identifier of the messageProvided by client.   
It will be returned in response message for identifying the corresponding request.   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
op | String | Yes | Operation  
`sprd-amend-order`  
args | Array of objects | Yes | Request Parameters  
> ordId | String | Conditional | Order ID   
Either `ordId` or `clOrdId` is required, if both are passed, `ordId` will be used.  
> clOrdId | String | Conditional | Client Order ID as assigned by the client  
> reqId | String | No | Client Request ID as assigned by the client for order amendment   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
> newSz | String | Conditional | New quantity after amendment.   
Either `newSz` or `newPx` is required. When amending a partially-filled order, the newSz should include the amount that has been filled and failed.  
> newPx | String | Conditional | New price after amendment.  
  
> Successful Response Example
    
    
    {
      "id": "1512",
      "op": "sprd-amend-order",
      "data": [
        {
          "clOrdId": "",
          "ordId": "2510789768709120",
          "reqId": "b12344",
          "sCode": "0",
          "sMsg": ""
        }
      ],
      "code": "0",
      "msg": ""
    }
    
    

> Failure Response Example
    
    
    {
      "id": "1512",
      "op": "sprd-amend-order",
      "data": [
        {
          "clOrdId": "",
          "ordId": "2510789768709120",
          "reqId": "b12344",
          "sCode": "5XXXX",
          "sMsg": "order not exist"
        }
      ],
      "code": "1",
      "msg": ""
    }
    
    

> Response Example When Format Error
    
    
    {
      "id": "1512",
      "op": "sprd-amend-order",
      "data": [],
      "code": "60013",
      "msg": "Invalid args"
    }
    
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
id | String | Unique identifier of the message  
op | String | Operation  
code | String | Error Code  
msg | String | Error message  
data | Array of objects | Data  
> ordId | String | Order ID  
> clOrdId | String | Client Order ID as assigned by the client  
> reqId | String | Client Request ID as assigned by the client for order amendment  
> sCode | String | Order status code, 0 means success  
> sMsg | String | Order status message  
newSz  
If the new quantity of the order is less than or equal to the (accFillSz + canceledSz + pendingSettleSz), after pendingSettleSz is settled, the order status will be transitioned into filled (if canceledSz = 0), or canceled (if canceledSz > 0).  The amend order returns sCode equal to 0  
It is not strictly considered that the order has been amended. It only means that your amend order request has been accepted by the system server. The result of the amend is subject to the status pushed by the order channel or the order status query.

---

# WS / 改单

修改当前未成交的订单

#### 服务地址

/ws/v5/business (需要登录)

#### 限速：20次/2s

#### 限速规则：User ID

同Nitro Spread`改单` REST API 共享限速 

> 请求示例
    
    
    {
       "id":"1512",
       "op":"sprd-amend-order",
       "args":[
          {
             "ordId":"2510789768709120",
             "newSz":"2"
          }
       ]
    }
    
    

#### 请求参数

Parameter | Type | Required | Description  
---|---|---|---  
id | String | 是 | 消息的唯一标识   
用户提供，返回参数中会返回以便于找到相应的请求。  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度必须要在1-32位之间。  
op | String | 是 | 支持的业务操作，`sprd-amend-order`  
args | Array of objects | 是 | 请求参数  
> ordId | String | 可选 | 订单ID   
ordId 和 clOrdId必须传一个，若传两个，以 ordId 为主  
> clOrdId | String | 可选 | 由用户设置的订单ID  
> reqId | String | 否 | 用户自定义修改事件ID   
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度要在1-32位之间。  
> newSz | String | 可选 | 修改的新数量，对于部分成交订单，该数量应包含已成交数量。  
`newSz` 或 `newPx`至少传一个。  
> newPx | String | 可选 | 修改后的新价格  
  
> 成功返回示例
    
    
    {
      "id": "1512",
      "op": "sprd-amend-order",
      "data": [
        {
          "clOrdId": "",
          "ordId": "2510789768709120",
          "reqId": "b12344",
          "sCode": "0",
          "sMsg": ""
        }
      ],
      "code": "0",
      "msg": ""
    }
    
    

> 失败返回示例
    
    
    {
      "id": "1512",
      "op": "sprd-amend-order",
      "data": [
        {
          "clOrdId": "",
          "ordId": "2510789768709120",
          "reqId": "b12344",
          "sCode": "5XXXX",
          "sMsg": "order not exist"
        }
      ],
      "code": "1",
      "msg": ""
    }
    
    

> 格式错误返回示例
    
    
    {
      "id": "1512",
      "op": "sprd-amend-order",
      "data": [],
      "code": "60013",
      "msg": "Invalid args"
    }
    
    

#### 返回参数

参数 | 类型 | 描述  
---|---|---  
id | String | 消息的唯一标识  
op | String | 操作  
code | String | 代码  
msg | String | 消息  
data | Array of objects | 请求成功后返回的数据  
> ordId | String | 订单ID  
> clOrdId | String | 由用户设置的订单ID  
> reqId | String | 用户自定义修改事件ID  
> sCode | String | 订单状态码，0 代表成功  
> sMsg | String | 订单状态消息  
newSz  
若修改订单时，订单修改后的新数量小于或等于 (accFillSz + canceledSz + pendingSettleSz)，在 pendingSettleSz 结算后，订单状态会根据 canceledSz 的不同而不同。当 canceledSz = 0，订单状态将被改为 filled；当 canceledSz > 0，订单状态将被改为 canceled。  修改订单返回sCode等于0不能严格认为该订单已经被修改，只表示您的修改订单请求被系统服务器所接受，改单结果以订单频道推送的状态或者查询订单状态为准