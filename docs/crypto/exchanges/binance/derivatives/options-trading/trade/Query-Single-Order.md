---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/options-trading/trade/Query-Single-Order
api_type: Trading
updated_at: 2026-01-15T23:43:04.775244
---

# Query Single Order (TRADE)

## API Description[​](/docs/derivatives/options-trading/trade/Query-Single-Order#api-description "Direct link to API Description")

Check an order status.

  * These orders will not be found: 
    * order status is `CANCELED` or `REJECTED`, **AND**
    * order has NO filled trade, **AND**
    * created time + 3 days < current time



## HTTP Request[​](/docs/derivatives/options-trading/trade/Query-Single-Order#http-request "Direct link to HTTP Request")

GET `/eapi/v1/order`

## Request Weight[​](/docs/derivatives/options-trading/trade/Query-Single-Order#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/options-trading/trade/Query-Single-Order#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES| Option trading pair, e.g BTC-200730-9000-C  
orderId| LONG| NO| Order id  
clientOrderId| STRING| NO| User-defined order ID cannot be repeated in pending orders  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * Either `orderId` or `clientOrderId ` must be sent.
> 


## Response Example[​](/docs/derivatives/options-trading/trade/Query-Single-Order#response-example "Direct link to Response Example")
    
    
    {  
      "orderId": 4611875134427365377,     // System order id  
      "symbol": "BTC-200730-9000-C",      // Option trading pair  
      "price": "100",                     // Order Price  
      "quantity": "1",                    // Order Quantity  
      "executedQty": "0",                 // Number of executed quantity  
      "side": "BUY",                      // Buy/sell direction  
      "type": "LIMIT",                    // Order type  
      "timeInForce": "GTC",               // Time in force method  
      "reduceOnly": false,                // Order is reduce only Y/N  
      "createTime": 1592465880683,        // Order Time  
      "updateTime": 1566818724722,        // Update time  
      "status": "NEW",                    // Order status  
      "avgPrice": "0",                    // Average price of completed trade  
      "clientOrderId": "",                 // Client order ID  
      "priceScale": 2,  
      "quantityScale": 2,  
      "optionSide": "CALL",  
      "quoteAsset": "USDT",  
      "mmp": false  
    }  
    

> **No Order Response:**
    
    
    {  
        "code": -2013,  
        "msg": "Order does not exist"  
    }

---

# 查询单个订单(TRADE)

## 接口描述[​](/docs/zh-CN/derivatives/options-trading/trade/Query-Single-Order#接口描述 "接口描述的直接链接")

查询订单状态。

  * 以下订单无法找到: 
    * 订单状态为 `CANCELED` or `REJECTED`， **AND**
    * 订单没有成交记录， **AND**
    * 订单生成时间 + 3天 < 当前时间



## HTTP请求[​](/docs/zh-CN/derivatives/options-trading/trade/Query-Single-Order#http请求 "HTTP请求的直接链接")

GET `/eapi/v1/order`

## 请求权重[​](/docs/zh-CN/derivatives/options-trading/trade/Query-Single-Order#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/options-trading/trade/Query-Single-Order#请求参数 "请求参数的直接链接")

**参数:**

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES| 交易对如：BTC-200730-9000-C  
orderId| LONG| NO| 订单id  
clientOrderId| STRING| NO| 用户自定义的订单号  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * 至少需要发送 `orderId` 或 `clientOrderId`
> 


## 响应示例[​](/docs/zh-CN/derivatives/options-trading/trade/Query-Single-Order#响应示例 "响应示例的直接链接")

> **响应:**
    
    
    {  
      "orderId": 4611875134427365377,     // 订单号  
      "symbol": "BTC-200730-9000-C",      // 交易对  
      "price": "100",                     // 订单价格  
      "quantity": "1",                    // 订单数量  
      "executedQty": "0",                 // 执行数量  
      "side": "BUY",                      // 订单方向  
      "type": "LIMIT",                    // 订单类型  
      "timeInForce": "GTC",               // 有效时间  
      "reduceOnly": false,                // 仅减仓  
      "postOnly": false,                  // 仅做maker  
      "createTime": 1592465880683,        // 下单时间  
      "updateTime": 1566818724722,        // 更新时间  
      "status": "NEW",                    // 订单状态  
      "avgPrice": "0",                    // 成交均价  
      "clientOrderId": ""                 // 自定义id  
      "priceScale": 2,  
      "quantityScale": 2,  
      "optionSide": "CALL",  
      "quoteAsset": "USDT",  
      "mmp": false  
    }  
    

> **无订单响应:**
    
    
    {  
        "code": -2013,  
        "msg": "Order does not exist"  
    }