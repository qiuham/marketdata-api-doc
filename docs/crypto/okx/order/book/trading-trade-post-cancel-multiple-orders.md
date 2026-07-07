---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-trade-post-cancel-multiple-orders
anchor_id: order-book-trading-trade-post-cancel-multiple-orders
api_type: API
updated_at: 2026-07-07 19:41:40.712672
---

# POST / Cancel multiple orders

Cancel incomplete orders in batches. Maximum 20 orders can be canceled per request. Request parameters should be passed in the form of an array.

#### Rate Limit: 300 orders per 2 seconds

#### Rate limit rule (except Options): User ID + Instrument ID

#### Rate limit rule (Options only): User ID + Instrument Family

#### Permission: Trade

Unlike other endpoints, the rate limit of this endpoint is determined by the number of orders. If there is only one order in the request, it will consume the rate limit of `Cancel order`. 

#### HTTP Request

`POST /api/v5/trade/cancel-batch-orders`

> Request Example
    
    
    POST /api/v5/trade/cancel-batch-orders
    body
    [
        {
            "instId":"BTC-USDT",
            "ordId":"590908157585625111"
        },
        {
            "instId":"BTC-USDT",
            "ordId":"590908544950571222"
        }
    ]
    
    
    
    import okx.Trade as Trade
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading: 0, Demo trading: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)
    
    # Cancel multiple orders by ordId
    cancel_orders_with_orderId = [
        {"instId": "BTC-USDT", "ordId": "590908157585625111"},
        {"instId": "BTC-USDT", "ordId": "590908544950571222"}
    ]
    
    result = tradeAPI.cancel_multiple_orders(cancel_orders_with_orderId)
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instId | String | Yes | Instrument ID, e.g. `BTC-USDT`  
ordId | String | Conditional | Order ID  
Either `ordId` or `clOrdId` is required. If both are passed, `ordId` will be used.  
clOrdId | String | Conditional | Client Order ID as assigned by the client  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "clOrdId":"oktswap6",
                "ordId":"12345689",
                "ts":"1695190491421",
                "sCode":"0",
                "sMsg":""
            },
            {
                "clOrdId":"oktswap7",
                "ordId":"12344",
                "ts":"1695190491421",
                "sCode":"0",
                "sMsg":""
            }
        ],
        "inTime": "1695190491421339",
        "outTime": "1695190491423240"
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
code | String | The result code, `0` means success  
msg | String | The error message, empty if the code is 0  
data | Array of objects | Array of objects contains the response results  
> ordId | String | Order ID  
> clOrdId | String | Client Order ID as assigned by the client  
> ts | String | Timestamp when the order request processing is finished by our system, Unix timestamp format in milliseconds, e.g. `1597026383085`  
> sCode | String | The code of the event execution result, `0` means success.  
> sMsg | String | Rejection message if the request is unsuccessful.  
inTime | String | Timestamp at REST gateway when the request is received, Unix timestamp format in microseconds, e.g. `1597026383085123`   
The time is recorded after authentication.  
outTime | String | Timestamp at REST gateway when the response is sent, Unix timestamp format in microseconds, e.g. `1597026383085123`

---

# POST / 批量撤单

撤销未完成的订单，每次最多可以撤销20个订单。请求参数应该按数组格式传递。

#### 限速：300个/2s

#### 限速规则（期权以外）：User ID + Instrument ID

#### 限速规则（只限期权）：User ID + Instrument Family

#### 权限：交易

与其他限速按接口调用次数不同，该接口限速按订单的总个数限速。如果单次批量请求中只有一个元素，则算在单个`撤单`限速中。 

#### HTTP请求

`POST /api/v5/trade/cancel-batch-orders`

> 请求示例
    
    
    POST /api/v5/trade/cancel-batch-orders
    body
    [
        {
            "instId":"BTC-USDT",
            "ordId":"590908157585625111"
        },
        {
            "instId":"BTC-USDT",
            "ordId":"590908544950571222"
        }
    ]
    
    
    
    
    import okx.Trade as Trade
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘: 0, 模拟盘: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)
    
    # 按ordId撤单
    cancel_orders_with_orderId = [
        {"instId": "BTC-USDT", "ordId": "590908157585625111"},
        {"instId": "BTC-USDT", "ordId": "590908544950571222"}
    ]
    
    result = tradeAPI.cancel_multiple_orders(cancel_orders_with_orderId)
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instId | String | 是 | 产品ID，如 `BTC-USD-190927`  
ordId | String | 可选 | 订单ID， `ordId`和`clOrdId`必须传一个，若传两个，以`ordId`为主  
clOrdId | String | 可选 | 用户自定义ID  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "clOrdId":"oktswap6",
                "ordId":"12345689",
                "ts":"1695190491421",
                "sCode":"0",
                "sMsg":""
            },
            {
                "clOrdId":"oktswap7",
                "ordId":"12344",
                "ts":"1695190491421",
                "sCode":"0",
                "sMsg":""
            }
        ],
        "inTime": "1695190491421339",
        "outTime": "1695190491423240"
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
code | String | 结果代码，`0`表示成功  
msg | String | 错误信息，代码为0时，该字段为空  
data | Array of objects | 包含结果的对象数组  
> ordId | String | 订单ID  
> clOrdId | String | 客户自定义订单ID  
> ts | String | 系统完成订单请求处理的时间戳，Unix时间戳的毫秒数格式，如 `1597026383085`  
> sCode | String | 事件执行结果的code，0代表成功  
> sMsg | String | 事件执行失败时的msg  
inTime | String | REST网关接收请求时的时间戳，Unix时间戳的微秒数格式，如 `1597026383085123`   
返回的时间是请求验证后的时间。  
outTime | String | REST网关发送响应时的时间戳，Unix时间戳的微秒数格式，如 `1597026383085123`