---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-trade-ws-amend-order
anchor_id: order-book-trading-trade-ws-amend-order
api_type: WebSocket
updated_at: 2026-07-17 19:16:14.002967
---

# WS / Amend order

Amend an incomplete order.  
  
#### URL Path

/ws/v5/private (required login)

#### Rate Limit: 60 requests per 2 seconds

#### Rate Limit of lead trader lead instruments for Copy Trading: 4 requests per 2 seconds

#### Rate limit rule (except Options): User ID + Instrument ID

#### Rate limit rule (Options only): User ID + Instrument Family

Rate limit of this endpoint will also be affected by the rules [Sub-account rate limit](/docs-v5/en/#overview-rate-limits-sub-account-rate-limit) and [Fill ratio based sub-account rate limit](/docs-v5/en/#overview-rate-limits-fill-ratio-based-sub-account-rate-limit).

Rate limit is shared with the `Amend order` REST API endpoints 

> Request Example
    
    
    {
      "id": "1512",
      "op": "amend-order",
      "args": [
        {
          "instIdCode": 123456,
          "ordId": "2510789768709120",
          "newSz": "2"
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
`amend-order`  
args | Array of objects | Yes | Request Parameters  
> instIdCode | Integer | Yes | Instrument ID code  
> cxlOnFail | Boolean | No | Whether the order needs to be automatically canceled when the order amendment fails   
Valid options: `false` or `true`, the default is `false`.  
> ordId | String | Conditional | Order ID   
Either `ordId` or `clOrdId` is required, if both are passed, `ordId` will be used.  
> clOrdId | String | Conditional | Client Order ID as assigned by the client  
> reqId | String | No | Client Request ID as assigned by the client for order amendment   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
> newSz | String | Conditional | New quantity after amendment and it has to be larger than 0. Either `newSz` or `newPx` is required. When amending a partially-filled order, the `newSz` should include the amount that has been filled.  
> newPx | String | Conditional | New price after amendment.   
When modifying options orders, users can only fill in one of the following: newPx, newPxUsd, or newPxVol. It must be consistent with parameters when placing orders. For example, if users placed the order using px, they should use newPx when modifying the order.  
> speedBump | String | Conditional | Speed bump  
`1`: Event contract speed bumps (the delay duration will be changed subject to adjustment without prior notice). Required for non-post-only orders of `EVENTS` symbols.  
> newPxUsd | String | Conditional | Modify options orders using USD prices   
Only applicable to options.   
When modifying options orders, users can only fill in one of the following: newPx, newPxUsd, or newPxVol.  
> newPxVol | String | Conditional | Modify options orders based on implied volatility, where 1 represents 100%   
Only applicable to options.   
When modifying options orders, users can only fill in one of the following: newPx, newPxUsd, or newPxVol.  
> pxAmendType | String | No | The price amendment type for orders  
`0`: Do not allow the system to amend to order price if `newPx` exceeds the price limit   
`1`: Allow the system to amend the price to the best available value within the price limit if `newPx` exceeds the price limit  
The default value is `0`  
expTime | String | No | Request effective deadline. Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
> Successful Response Example
    
    
    {
      "id": "1512",
      "op": "amend-order",
      "data": [
        {
          "clOrdId": "",
          "ordId": "2510789768709120",
          "ts": "1695190491421",
          "reqId": "b12344",
          "sCode": "0",
          "sMsg": "",
          "subCode": ""
        }
      ],
      "code": "0",
      "msg": "",
      "inTime": "1695190491421339",
      "outTime": "1695190491423240"
    }
    

> Failure Response Example
    
    
    {
      "id": "1512",
      "op": "amend-order",
      "data": [
        {
          "clOrdId": "",
          "ordId": "2510789768709120",
          "ts": "1695190491421",
          "reqId": "b12344",
          "sCode": "51008",
          "sMsg": "Order failed. Insufficient USDT balance in account",
          "subCode": "10000"
        }
      ],
      "code": "1",
      "msg": "",
      "inTime": "1695190491421339",
      "outTime": "1695190491423240"
    }
    

> Response Example When Format Error
    
    
    {
      "id": "1512",
      "op": "amend-order",
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
> reqId | String | Client Request ID as assigned by the client for order amendment  
> sCode | String | Order status code, `0` means success  
> sMsg | String | Order status message  
> subCode | String | Sub-code of sCode.  
Returns `""` when sCode is 0 (request successful).  
When sCode is not 0 (request failed), returns the sub-code if available; otherwise returns `""`.  
inTime | String | Timestamp at Websocket gateway when the request is received, Unix timestamp format in microseconds, e.g. `1597026383085123`  
outTime | String | Timestamp at Websocket gateway when the response is sent, Unix timestamp format in microseconds, e.g. `1597026383085123`  
newSz   
If the new quantity of the order is less than or equal to the filled quantity when you are amending a partially-filled order, the order status will be changed to filled.  The amend order returns sCode equal to 0. It is not strictly considered that the order has been amended. It only means that your amend order request has been accepted by the system server. The result of the amend is subject to the status pushed by the order channel or the order status query

---

# WS / 改单

修改当前未成交的订单  
  
#### 服务地址

/ws/v5/private (需要登录)

#### 限速：60次/2s

#### 跟单交易带单员带单产品的限速：4次/2s

#### 限速规则（期权以外）：User ID + Instrument ID

#### 限速规则（只限期权）：User ID + Instrument Family

该接口限速同时受到 [子账户限速](/docs-v5/log_zh/#upcoming-changes-sub-account-rate-limit) 及 [基于成交比率的子账户限速](/docs-v5/log_zh/#upcoming-changes-fill-ratio-based-sub-account-rate-limit) 限速规则的影响。

同`改单` REST API 共享限速 

> 请求示例
    
    
    {
        "id": "1512",
        "op": "amend-order",
        "args": [{
            "instIdCode": 123456,
            "ordId": "2510789768709120",
            "newSz": "2"
        }]
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
id | String | 是 | 消息的唯一标识   
用户提供，返回参数中会返回以便于找到相应的请求。  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度必须要在1-32位之间。  
op | String | 是 | 支持的业务操作，如 `amend-order`  
args | Array of objects | 是 | 请求参数  
> instIdCode | Integer | 是 | 产品唯一标识代码  
> cxlOnFail | Boolean | 否 | 当订单修改失败时，该订单是否需要自动撤销。默认为`false`  
`false`：不自动撤单  
`true`：自动撤单  
> ordId | String | 可选 | 订单ID  
ordId和clOrdId必须传一个，若传两个，以 ordId 为主  
> clOrdId | String | 可选 | 用户提供的订单ID  
> reqId | String | 否 | 用户提供的reqId  
如果提供，那在返回参数中返回reqId，方便找到相应的修改请求。  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度要在1-32位之间。  
> newSz | String | 可选 | 请求修改的新数量，必须大于0。`newSz`和`newPx`不可同时为空。对于部分成交订单，该数量应包含已成交数量。  
> newPx | String | 可选 | 修改后的新价格  
修改的新价格期权改单时，newPx/newPxUsd/newPxVol 只能填一个，且必须与下单参数保持一致，如下单用px，改单时需使用newPx  
> speedBump | String | 可选 | 减速带  
`1`：事件合约速度限制（延迟可能因市场情况调整，不提前通知）。对 `EVENTS` 产品的非只挂单操作为必填。  
> newPxUsd | String | 可选 | 以USD价格进行期权改单   
仅适用于期权，期权改单时，newPx/newPxUsd/newPxVol 只能填一个  
> newPxVol | String | 可选 | 以隐含波动率进行期权改单，例如 1 代表 100%   
仅适用于期权，期权改单时，newPx/newPxUsd/newPxVol 只能填一个  
> pxAmendType | String | 否 | 订单价格修正类型  
`0`：当`newPx`超出价格限制时，不允许系统修改订单价格  
`1`：当`newPx`超出价格限制时，允许系统将价格修改为限制范围内的最优值  
默认值为`0`  
expTime | String | 否 | 请求有效截止时间。Unix时间戳的毫秒数格式，如 `1597026383085`  
  
> 成功返回示例
    
    
    {
        "id": "1512",
        "op": "amend-order",
        "data": [{
            "clOrdId": "",
            "ordId": "2510789768709120",
            "ts": "1695190491421",
            "reqId": "b12344",
            "sCode": "0",
            "sMsg": "",
            "subCode": ""
        }],
        "code": "0",
        "msg": "",
        "inTime": "1695190491421339",
        "outTime": "1695190491423240"
    } 
    

> 失败返回示例
    
    
    {
        "id": "1512",
        "op": "amend-order",
        "data": [{
            "clOrdId": "",
            "ordId": "2510789768709120",
            "ts": "1695190491421",
            "reqId": "b12344",
            "sCode": "51008",
            "sMsg": "Order failed. Insufficient USDT balance in account",
            "subCode": "1000"
        }],
        "code": "1",
        "msg": "",
        "inTime": "1695190491421339",
        "outTime": "1695190491423240"
    }
    

> 格式错误返回示例
    
    
    {
        "id": "1512",
        "op": "amend-order",
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
> clOrdId | String | 用户提供的订单ID  
> ts | String | 订单创建时间，Unix时间戳的毫秒数格式，如 `1597026383085`。与订单频道中的 `cTime` 相同。  
> reqId | String | 用户提供的reqId  
如果用户在请求中提供reqId，则返回相应reqId  
> sCode | String | 订单状态码，0 代表成功  
> sMsg | String | 订单状态消息  
> subCode | String | sCode 的子码。  
当 sCode 为 0（请求成功）时，返回 `""`。  
当 sCode 不为 0（请求失败）且存在子码时，返回对应的子码；若无子码，则返回 `""`。  
inTime | String | WebSocket 网关接收请求时的时间戳，Unix时间戳的微秒数格式，如 `1597026383085123`  
outTime | String | WebSocket 网关发送响应时的时间戳，Unix时间戳的微秒数格式，如 `1597026383085123`  
  
newSz : 当修改已经部分成交的订单时，新的委托数量必须大于等于已成交数量 

修改订单返回sCode等于0不能严格认为该订单已经被修改，只表示您的修改订单请求被系统服务器所接受，改单结果以订单频道推送的状态或者查询订单状态为准