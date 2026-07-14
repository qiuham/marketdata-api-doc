---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-signal-bot-trading-post-place-sub-order
anchor_id: order-book-trading-signal-bot-trading-post-place-sub-order
api_type: API
updated_at: 2026-07-14 19:19:28.591747
---

# POST / Place sub order

You can place an order only if you have sufficient funds.  
  
  
  
#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/tradingBot/signal/sub-order`

> Request Example
    
    
    POST /api/v5/tradingBot/signal/sub-order
    body
    {
        "algoId":"1222",
        "instId":"BTC-USDT-SWAP",
        "side":"buy",
        "ordType":"limit",
        "px":"2.15",
        "sz":"2"
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instId | String | Yes | Instrument ID, e.g. `BTC-USDT-SWAP`  
algoId | String | Yes | Algo ID  
side | String | Yes | Order side, `buy` `sell`  
ordType | String | Yes | Order type   
`market`: Market order   
`limit`: Limit order  
sz | String | Yes | Quantity to buy or sell  
px | String | Conditional | Order price. Only applicable to `limit` order.  
reduceOnly | Boolean | No | Whether orders can only reduce in position size.   
Valid options: `true` or `false`. The default value is `false`.   
Only applicable to `Futures mode`/`Multi-currency margin`  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
code | String | The result code, `0` means success  
msg | String | The error message, empty if the code is 0  
data | Array of objects | Array of objects contains the response results  
ordType  
Order type. When creating a new order, you must specify the order type. The order type you specify will affect: 1) what order parameters are required, and 2) how the matching system executes your order. The following are valid order types:  
`limit`: Limit order, which requires specified sz and px.  
`market`: Market order. It will be filled with market price (by swiping opposite order book). Market order will be placed to order book with most aggressive price allowed by Price Limit Mechanism.  sz refers to the number of contracts。  reduceOnly  
When placing an order with this parameter set to true, it means that the order will reduce the size of the position only The sum of the current order size and all reverse direction reduce-only pending orders which's price-time priority is higher than the current order, cannot exceed the contract quantity of position. Only applicable to `Futures mode` and `Multi-currency margin`

---

# POST / 下单

只有当您的账户有足够的资金才能下单。  
  
  
  
#### 限速：20次/2s

#### 权限：交易

#### HTTP请求

`POST /api/v5/tradingBot/signal/sub-order`

> 请求示例
    
    
    POST /api/v5/tradingBot/signal/sub-order
    body
    {
        "algoId":"1222",
        "instId":"BTC-USDT-SWAP",
        "side":"buy",
        "ordType":"limit",
        "px":"2.15",
        "sz":"2"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instId | String | 是 | 产品ID，如 `BTC-USDT-SWAP`  
algoId | String | 是 | 策略订单ID  
side | String | 是 | 订单方向  
`buy`：买， `sell`：卖  
ordType | String | 是 | 订单类型   
`market`：市价单  
`limit`：限价单  
sz | String | 是 | 委托数量  
px | String | 可选 | 委托价格，仅适用于`limit`  
reduceOnly | Boolean | 否 | 是否只减仓，`true` 或 `false`，默认`false`  
仅适用于`合约模式`和`跨币种保证金模式`  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
code | String | 结果代码，`0`表示成功  
msg | String | 错误信息，代码为0时，该字段为空  
data | Array of objects | 包含结果的对象数组  
ordType  
订单类型，创建新订单时必须指定，您指定的订单类型将影响需要哪些订单参数和撮合系统如何执行您的订单，以下是有效的ordType：  
普通委托：  
limit：限价单，要求指定sz 和 px  
market：自动以最高买/最低卖价格委托，遵循限价机制  
sz 指合约张数。  reduceOnly  
只减仓，下单时，此参数设置为 true 时，表示此笔订单具有减仓属性，只会减少持仓数量，不会增加新的持仓仓位  
当前只减仓下单张数，加上价格时间优先于当前只减仓下单的只减仓挂单张数总和，不能超过持仓数量  
仅适用于`合约模式`和`跨币种保证金模式`