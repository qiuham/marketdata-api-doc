---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-trade-ws-cancel-order
anchor_id: order-book-trading-trade-ws-cancel-order
api_type: WebSocket
updated_at: 2026-07-14 19:19:06.959643
---

# WS / Cancel order

Cancel an incomplete order

#### URL Path

/ws/v5/private (required login)

#### Rate Limit: 60 requests per 2 seconds

#### Rate limit rule (except Options): User ID + Instrument ID

#### Rate limit rule (Options only): User ID + Instrument Family

Rate limit is shared with the `Cancel order` REST API endpoints 

> Request Example
    
    
    {
      "id": "1514",
      "op": "cancel-order",
      "args": [
        {
          "instIdCode": 123456,
          "ordId": "2510789768709120"
        }
      ]
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
id | String | Yes | Unique identifier of the message   
Provided by client. It will be returned in response message for identifying the corresponding request.   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
op | String | Yes | Operation  
`cancel-order`  
args | Array of objects | Yes | Request Parameters  
> instIdCode | Integer | Yes | Instrument ID code  
> ordId | String | Conditional | Order ID   
Either `ordId` or `clOrdId` is required, if both are passed, ordId will be used  
> clOrdId | String | Conditional | Client Order ID as assigned by the client   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
  
> Successful Response Example
    
    
    {
      "id": "1514",
      "op": "cancel-order",
      "data": [
        {
          "clOrdId": "",
          "ordId": "2510789768709120",
          "ts": "1695190491421",
          "sCode": "0",
          "sMsg": ""
        }
      ],
      "code": "0",
      "msg": "",
      "inTime": "1695190491421339",
      "outTime": "1695190491423240"
    }
    

> Failure Response Example
    
    
    {
      "id": "1514",
      "op": "cancel-order",
      "data": [
        {
          "clOrdId": "",
          "ordId": "2510789768709120",
          "ts": "1695190491421",
          "sCode": "5XXXX",
          "sMsg": "Order not exist"
        }
      ],
      "code": "1",
      "msg": "",
      "inTime": "1695190491421339",
      "outTime": "1695190491423240"
    }
    

> Response Example When Format Error
    
    
    {
      "id": "1514",
      "op": "cancel-order",
      "data": [],
      "code": "60013",
      "msg": "Invalid args",
      "inTime": "1695190491421339",
      "outTime": "1695190491423240"
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
> ts | String | Order creation time. Unix timestamp format in milliseconds, e.g. `1597026383085`. Equivalent to `cTime` in the order channel.  
> sCode | String | Order status code, `0` means success  
> sMsg | String | Order status message  
inTime | String | Timestamp at Websocket gateway when the request is received, Unix timestamp format in microseconds, e.g. `1597026383085123`  
outTime | String | Timestamp at Websocket gateway when the response is sent, Unix timestamp format in microseconds, e.g. `1597026383085123`  
Cancel order returns with sCode equal to 0. It is not strictly considered that the order has been canceled. It only means that your cancellation request has been accepted by the system server. The result of the cancellation is subject to the state pushed by the order channel or the get order state.

---

# WS / 撤单

撤销当前未完成订单

#### 服务地址

/ws/v5/private (需要登录)

#### 限速：60次/2s

#### 限速规则（期权以外）：User ID + Instrument ID

#### 限速规则（只限期权）：User ID + Instrument Family

同`撤单` REST API 共享限速 

> 请求示例
    
    
    {
        "id": "1514",
        "op": "cancel-order",
        "args": [{
            "instIdCode": 123456,
            "ordId": "2510789768709120"
        }]
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
id | String | 是 | 消息的唯一标识  
用户提供，返回参数中会返回以便于找到相应的请求。  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度必须要在1-32位之间。  
op | String | 是 | 支持的业务操作，如 `cancel-order`  
args | Array of objects | 是 | 请求参数  
> instIdCode | Integer | 是 | 产品唯一标识代码  
> ordId | String | 可选 | 订单ID  
ordId和clOrdId必须传一个，若传两个，以 ordId 为主  
> clOrdId | String | 可选 | 用户提供的订单ID  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字，且长度要在1-32位之间。  
  
> 成功返回示例
    
    
    {
        "id": "1514",
        "op": "cancel-order",
        "data": [{
            "clOrdId": "",
            "ordId": "2510789768709120",
            "ts": "1695190491421",
            "sCode": "0",
            "sMsg": ""
        }],
        "code": "0",
        "msg": "",
        "inTime": "1695190491421339",
        "outTime": "1695190491423240"
    }
    

> 失败返回示例
    
    
    {
        "id": "1514",
        "op": "cancel-order",
        "data": [{
            "clOrdId": "",
            "ordId": "2510789768709120",
            "ts": "1695190491421",
            "sCode": "5XXXX",
            "sMsg": "Order not exist"
        }],
        "code": "1",
        "msg": "",
        "inTime": "1695190491421339",
        "outTime": "1695190491423240"
    }
    

> 格式错误返回示例
    
    
    {
        "id": "1514",
        "op": "cancel-order",
        "data": [],
        "code": "60013",
        "msg": "Invalid args",
        "inTime": "1695190491421339",
        "outTime": "1695190491423240"
    }
    

#### 返回参数

参数 | 类型 | 描述  
---|---|---  
id | String | 消息的唯一标识  
op | String | 业务操作  
code | String | 代码  
msg | String | 消息  
data | Array of objects | 请求成功后返回的数据  
> ordId | String | 订单ID  
> clOrdId | String | 由用户设置的订单ID  
> ts | String | 订单创建时间，Unix时间戳的毫秒数格式，如 `1597026383085`。与订单频道中的 `cTime` 相同。  
> sCode | String | 订单状态码，0 代表成功  
> sMsg | String | 订单状态消息  
inTime | String | WebSocket 网关接收请求时的时间戳，Unix时间戳的微秒数格式，如 `1597026383085123`  
outTime | String | WebSocket 网关发送响应时的时间戳，Unix时间戳的微秒数格式，如 `1597026383085123`  
撤单返回sCode等于0不能严格认为该订单已经被撤销，只表示您的撤单请求被系统服务器所接受，撤单结果以订单频道推送的状态或者查询订单状态为准