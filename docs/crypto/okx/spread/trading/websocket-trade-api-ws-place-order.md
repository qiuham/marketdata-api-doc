---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#spread-trading-websocket-trade-api-ws-place-order
anchor_id: spread-trading-websocket-trade-api-ws-place-order
api_type: WebSocket
updated_at: 2026-07-21 19:26:50.213879
---

# WS / Place order

You can place an order only if you have sufficient funds.  
  
  
#### URL Path

/ws/v5/business (required login)

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

Rate limit is shared with the Nitro Spread `Place order` REST API endpoints 

> Request Example
    
    
    {
      "id": "1512",
      "op": "sprd-order",
      "args": [
        {
           "sprdId":"BTC-USDT_BTC-USDT-SWAP",
           "clOrdId":"b15",
           "side":"buy",
           "ordType":"limit",
           "px":"2.15",
           "sz":"2"
        }
      ]
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
id | String | Yes | Unique identifier of the message provided by client. It will be returned in response message for identifying the corresponding request.   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
op | String | Yes | Operation  
`sprd-order`  
args | Array of objects | Yes | Request parameters  
> sprdId | String | Yes | spread ID, e.g. BTC-USDT_BTC-USD-SWAP  
> clOrdId | String | No | Client Order ID as assigned by the client   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
> tag | String | No | Order tag   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 16 characters.  
> side | String | Yes | Order side   
`buy`   
`sell`  
> ordType | String | Yes | Order type:  
`market`: Market order   
`limit`: Limit order   
`post_only`: Post-only order   
`ioc`: Immediate-or-cancel order  
> sz | String | Yes | Quantity to buy or sell  
> px | String | Yes | Order price. Only applicable to `limit, post_only, ioc` order.  
  
> ##### Successful Response Example
    
    
    {
      "id": "1512",
      "op": "sprd-order",
      "data": [
        {
          "clOrdId": "",
          "ordId": "12345689",
          "tag": "",
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
      "op": "sprd-order",
      "data": [
        {
          "clOrdId": "",
          "ordId": "",
          "tag": "",
          "sCode": "5XXXX",
          "sMsg": "not exist"
        }
      ],
      "code": "1",
      "msg": ""
    }
    

> Response Example When Format Error
    
    
    {
      "id": "1512",
      "op": "sprd-order",
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
> tag | String | Order tag  
> sCode | String | Order status code, `0` means success  
> sMsg | String | Rejection or success message of event execution.  
clOrdId  
clOrdId is a user-defined unique ID used to identify the order. It will be included in the response parameters if you have specified during order submission, and can be used as a request parameter to the endpoints to query, cancel and amend orders.   
clOrdId must be unique among the clOrdIds of all pending orders.

---

# WS / 下单

只有当您的账户有足够的资金才能下单。  
  
#### 服务地址

/ws/v5/business (需要登录)

#### 限速：20次/2s

#### 限速规则：User ID

同Nitro Spread`下单` REST API 共享限速 

> 请求示例
    
    
    {
      "id": "1512",
      "op": "sprd-order",
      "args": [
        {
           "sprdId":"BTC-USDT_BTC-USDT-SWAP",
           "clOrdId":"b15",
           "side":"buy",
           "ordType":"limit",
           "px":"2.15",
           "sz":"2"
        }
      ]
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
id | String | 是 | 消息的唯一标识   
用户提供，返回参数中会返回以便于找到相应的请求。  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度必须要在1-32位之间。  
op | String | 是 | 支持的业务操作，`sprd-order`  
args | Array of objects | 是 | 请求参数  
> sprdId | String | 是 | 产品ID，如 `BTC-USDT_BTC-USDT-SWAP`  
> clOrdId | String | 否 | 由用户设置的订单ID  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度要在1-32位之间。  
> tag | String | 否 | 订单标签  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度要在1-16位之间。  
> side | String | 是 | 订单方向，`buy` `sell`  
> ordType | String | 是 | 订单类型  
`market`：市价单   
`limit`：限价单   
`post_only`：只做maker单   
`ioc`：立即成交并取消剩余  
> sz | String | 是 | 委托数量  
> px | String | 是 | 委托价，仅适用于`limit`、`post_only`、`ioc`类型的订单  
  
> 成功返回示例
    
    
    {
        "id": "1512",
        "op": "sprd-order",
        "data": [{
            "clOrdId": "",
            "ordId": "12345689",
            "tag": "",
            "sCode": "0",
            "sMsg": ""
        }],
        "code": "0",
        "msg": ""
    }
    

> 失败返回示例
    
    
    {
        "id": "1512",
        "op": "sprd-order",
        "data": [{
            "clOrdId": "",
            "ordId": "",
            "tag": "",
            "sCode": "5XXXX",
            "sMsg": "not exist"
        }],
        "code": "1",
        "msg": ""
    }
    

> 格式错误返回示例
    
    
    {
        "id": "1512",
        "op": "sprd-order",
        "data": [],
        "code": "60013",
        "msg": "Invalid args"
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
id | String | 消息的唯一标识  
op | String | 业务操作  
code | String | 代码  
msg | String | 消息  
data | Array of objects | 请求成功后返回的数据  
> ordId | String | 订单ID  
> clOrdId | String | 由用户设置的订单ID  
> tag | String | 订单标签  
> sCode | String | 订单状态码，0 代表成功  
> sMsg | String | 订单状态消息  
clOrdId  
clOrdId是用户自定义的唯一ID用来识别订单。如果在请求参数中传入了，那它一定会在返回参数内，并且可以用于查询订单，撤销订单，修改订单等接口。 clOrdId不能与当前所有的挂单的clOrdId重复