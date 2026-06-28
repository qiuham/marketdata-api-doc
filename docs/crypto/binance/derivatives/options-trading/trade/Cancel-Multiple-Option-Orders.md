---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/options-trading/trade/Cancel-Multiple-Option-Orders
api_type: Trading
updated_at: 2026-01-15T23:42:29.582193
---

# Cancel Multiple Option Orders (TRADE)

## API Description[​](/docs/derivatives/options-trading/trade/Cancel-Multiple-Option-Orders#api-description "Direct link to API Description")

Cancel multiple orders.

## HTTP Request[​](/docs/derivatives/options-trading/trade/Cancel-Multiple-Option-Orders#http-request "Direct link to HTTP Request")

DELETE `/eapi/v1/batchOrders`

## Request Weight[​](/docs/derivatives/options-trading/trade/Cancel-Multiple-Option-Orders#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/options-trading/trade/Cancel-Multiple-Option-Orders#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES| Option trading pair, e.g BTC-200730-9000-C  
orderIds| LIST<LONG>| NO| Order ID, e.g [4611875134427365377,4611875134427365378]  
clientOrderIds| LIST<STRING>| NO| User-defined order ID, e.g ["my_id_1","my_id_2"]  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * At least one instance of `orderId` and `clientOrderId` must be sent.
> 


## Response Example[​](/docs/derivatives/options-trading/trade/Cancel-Multiple-Option-Orders#response-example "Direct link to Response Example")
    
    
    [  
        {  
            "orderId": 4611875134427365377,     // System order number  
            "symbol": "BTC-200730-9000-C",      // Option trading pair  
            "price": "100",                     // Order Price  
            "quantity": "1",                    // Order Quantity  
            "executedQty": "0",                 // Number of completed quantity  
            "side": "BUY",                      // Buy/sell direction  
            "type": "LIMIT",                    // Order type  
            "timeInForce": "GTC",               // Time in force method  
            "reduceOnly": false,                // Order is reduce only Y/N  
            "createTime": 1592465880683,        // Order Time  
            "updateTime": 1566818724722,        // Update time   
            "status": "NEW",                    // Order status  
            "avgPrice": "0",                    // Average price of completed trade  
            "source": "API",  
            "clientOrderId": "",                 // Client order ID  
            "priceScale": 3,  
            "quantityScale": 4,  
            "optionSide": "CALL",  
            "quoteAsset": "USDT",  
            "mmp": false  
        }  
    ]

---

# 批量撤销订单(TRADE)

## 接口描述[​](/docs/zh-CN/derivatives/options-trading/trade/Cancel-Multiple-Option-Orders#接口描述 "接口描述的直接链接")

批量撤销订单。

## HTTP请求[​](/docs/zh-CN/derivatives/options-trading/trade/Cancel-Multiple-Option-Orders#http请求 "HTTP请求的直接链接")

DELETE `/eapi/v1/batchOrders`

## 请求权重[​](/docs/zh-CN/derivatives/options-trading/trade/Cancel-Multiple-Option-Orders#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/options-trading/trade/Cancel-Multiple-Option-Orders#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES| 交易对  
orderIds| LIST<LONG>| NO| 系统订单号   
  
比如 [4611875134427365377,4611875134427365378]  
clientOrderIds| LIST<STRING>| NO| 用户自定义的订单号   
  
比如["my_id_1","my_id_2"] 需要encode双引号。逗号后面没有空格。  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * `orderIds` 与 `clientOrderIds` 必须至少发送一个，不可同时发送
> 


## 响应示例[​](/docs/zh-CN/derivatives/options-trading/trade/Cancel-Multiple-Option-Orders#响应示例 "响应示例的直接链接")
    
    
    [  
      {  
        "orderId": 4611875134427365377,     // 订单Id  
        "symbol": "BTC-200730-9000-C",      // 交易对  
        "price": "100",                     // 订单价格  
        "quantity": "1",                    // 订单数量  
        "executedQty": "0",                 // 已经成交数量  
        "fee": "0",                         // 手续费   
        "side": "BUY",                      // 订单方向  
        "type": "LIMIT",                    // 订单类型  
        "timeInForce": "GTC",               // 有效时间  
        "reduceOnly": false,                // 仅减仓  
        "createTime": 1592465880683,        // 订单创建时间  
        "updateTime": 1566818724722,        // 订单更新时间  
        "status": "ACCEPTED",               // 订单类型  
        "avgPrice": "0",                    // 平均成交价  
        "clientOrderId": ""                 // 用户自定义的订单号  
        "priceScale": 3,  
        "quantityScale": 4,  
        "optionSide": "CALL",  
        "quoteAsset": "USDT",  
        "mmp": false  
      }  
    ]