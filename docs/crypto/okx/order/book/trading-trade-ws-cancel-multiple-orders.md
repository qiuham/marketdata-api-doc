---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-trade-ws-cancel-multiple-orders
anchor_id: order-book-trading-trade-ws-cancel-multiple-orders
api_type: WebSocket
updated_at: 2026-07-23 19:21:19.532142
---

# WS / Cancel multiple orders

Cancel incomplete orders in batches. Maximum 20 orders can be canceled per request.

#### URL Path

/ws/v5/private (required login)

#### Rate Limit: 300 orders per 2 seconds

#### Rate limit rule (except Options): User ID + Instrument ID

#### Rate limit rule (Options only): User ID + Instrument Family

Unlike other endpoints, the rate limit of this endpoint is determined by the number of orders. If there is only one order in the request, it will consume the rate limit of `Cancel order`.  Rate limit is shared with the `Cancel multiple orders` REST API endpoints 

> Request Example
    
    
    {
      "id": "1515",
      "op": "batch-cancel-orders",
      "args": [
        {
          "instIdCode": 123456,
          "ordId": "2517748157541376"
        },
        {
          "instIdCode": 654321,
          "ordId": "2517748155771904"
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
`batch-cancel-orders`  
args | Array of objects | Yes | Request Parameters  
> instIdCode | Integer | Yes | Instrument ID code  
> ordId | String | Conditional | Order ID   
Either `ordId` or `clOrdId` is required, if both are passed, ordId will be used  
> clOrdId | String | Conditional | Client Order ID as assigned by the client   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
  
> Response Example When All Succeed
    
    
    {
      "id": "1515",
      "op": "batch-cancel-orders",
      "data": [
        {
          "clOrdId": "oktswap6",
          "ordId": "2517748157541376",
          "ts": "1695190491421",
          "sCode": "0",
          "sMsg": ""
        },
        {
          "clOrdId": "oktswap7",
          "ordId": "2517748155771904",
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
    

> Response Example When partially successfully
    
    
    {
      "id": "1515",
      "op": "batch-cancel-orders",
      "data": [
        {
          "clOrdId": "oktswap6",
          "ordId": "2517748157541376",
          "ts": "1695190491421",
          "sCode": "0",
          "sMsg": ""
        },
        {
          "clOrdId": "oktswap7",
          "ordId": "2517748155771904",
          "ts": "1695190491421",
          "sCode": "5XXXX",
          "sMsg": "order not exist"
        }
      ],
      "code": "2",
      "msg": "",
      "inTime": "1695190491421339",
      "outTime": "1695190491423240"
    }
    

> Response Example When All Failed
    
    
    {
      "id": "1515",
      "op": "batch-cancel-orders",
      "data": [
        {
          "clOrdId": "oktswap6",
          "ordId": "2517748157541376",
          "ts": "1695190491421",
          "sCode": "5XXXX",
          "sMsg": "order not exist"
        },
        {
          "clOrdId": "oktswap7",
          "ordId": "2517748155771904",
          "ts": "1695190491421",
          "sCode": "5XXXX",
          "sMsg": "order not exist"
        }
      ],
      "code": "1",
      "msg": "",
      "inTime": "1695190491421339",
      "outTime": "1695190491423240"
    }
    

> Response Example When Format Error
    
    
    {
      "id": "1515",
      "op": "batch-cancel-orders",
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

---

# WS / 批量撤单

批量进行撤单操作，每次可批量撤销不同类型的产品，最多撤销20个

#### 服务地址

/ws/v5/private (需要登录)

#### 限速：300个/2s

#### 限速规则（期权以外）：User ID + Instrument ID

#### 限速规则（只限期权）：User ID + Instrument Family

与其他限速按接口调用次数不同，该接口限速按订单的总个数限速。如果单次批量请求中只有一个元素，则算在单个`撤单`限速中。  同`批量撤单` REST API 共享限速 

> 请求示例
    
    
    {
        "id": "1515",
        "op": "batch-cancel-orders",
        "args": [{
            "instIdCode": 123456,
            "ordId": "2517748157541376"
        }, {
            "instIdCode": 654321,
            "ordId": "2517748155771904"
        }]
    }
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
id | String | 是 | 消息的唯一标识  
用户提供，返回参数中会返回以便于找到相应的请求。  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度必须要在1-32位之间。  
op | String | 是 | 支持的业务操作，如 `batch-cancel-orders`  
args | Array of objects | 是 | 请求参数  
> instIdCode | Integer | 是 | 产品唯一标识代码  
> ordId | String | 可选 | 订单ID  
ordId和clOrdId必须传一个，若传两个，以ordId 为主  
> clOrdId | String | 可选 | 用户提供的订单ID  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字，且长度要在1-32位之间。  
  
> 全部成功返回示例
    
    
    {
        "id": "1515",
        "op": "batch-cancel-orders",
        "data": [{
            "clOrdId": "oktswap6",
            "ordId": "2517748157541376",
            "ts": "1695190491421",
            "sCode": "0",
            "sMsg": ""
        }, {
            "clOrdId": "oktswap7",
            "ordId": "2517748155771904",
            "ts": "1695190491421",
            "sCode": "0",
            "sMsg": ""
        }],
        "code": "0",
        "msg": "",
        "inTime": "1695190491421339",
        "outTime": "1695190491423240"
    }
    

> 部分成功的返回示例
    
    
    {
        "id": "1515",
        "op": "batch-cancel-orders",
        "data": [{
            "clOrdId": "oktswap6",
            "ordId": "2517748157541376",
            "ts": "1695190491421",
            "sCode": "0",
            "sMsg": ""
        }, {
            "clOrdId": "oktswap7",
            "ordId": "2517748155771904",
            "ts": "1695190491421",
            "sCode": "5XXXX",
            "sMsg": "order not exist"
        }],
        "code": "2",
        "msg": "",
        "inTime": "1695190491421339",
        "outTime": "1695190491423240"
    }
    

> 全部失败的返回示例
    
    
    {
        "id": "1515",
        "op": "batch-cancel-orders",
        "data": [{
            "clOrdId": "oktswap6",
            "ordId": "2517748157541376",
            "ts": "1695190491421",
            "sCode": "5XXXX",
            "sMsg": "order not exist"
        }, {
            "clOrdId": "oktswap7",
            "ordId": "2517748155771904",
            "ts": "1695190491421",
            "sCode": "5XXXX",
            "sMsg": "order not exist"
        }],
        "code": "1",
        "msg": "",
        "inTime": "1695190491421339",
        "outTime": "1695190491423240"
    }
    

> 格式错误示例
    
    
    {
        "id": "1515",
        "op": "batch-cancel-orders",
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