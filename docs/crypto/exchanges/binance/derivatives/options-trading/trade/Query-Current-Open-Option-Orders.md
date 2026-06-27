---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/options-trading/trade/Query-Current-Open-Option-Orders
api_type: Trading
updated_at: 2026-01-15T23:42:46.463462
---

# Query Current Open Option Orders (USER_DATA)

## API Description[​](/docs/derivatives/options-trading/trade/Query-Current-Open-Option-Orders#api-description "Direct link to API Description")

Query current all open orders, status: ACCEPTED PARTIALLY_FILLED

## HTTP Request[​](/docs/derivatives/options-trading/trade/Query-Current-Open-Option-Orders#http-request "Direct link to HTTP Request")

GET `/eapi/v1/openOrders`

## Request Weight[​](/docs/derivatives/options-trading/trade/Query-Current-Open-Option-Orders#request-weight "Direct link to Request Weight")

**1** for a single symbol; **40** when the symbol parameter is omitted

## Request Parameters[​](/docs/derivatives/options-trading/trade/Query-Current-Open-Option-Orders#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| NO| return all orders if don't pass, Option trading pair, e.g BTC-200730-9000-C,  
orderId| LONG| NO| Returns the orderId and subsequent orders, the most recent order is returned by default  
startTime| LONG| NO| Start Time  
endTime| LONG| NO| End Time  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/derivatives/options-trading/trade/Query-Current-Open-Option-Orders#response-example "Direct link to Response Example")
    
    
    [  
      {  
        "orderId": 4611875134427365377,     // System order number  
        "symbol": "BTC-200730-9000-C",      // Option trading pair  
        "price": "100",                     // Order Price  
        "quantity": "1",                    // Order Quantity  
        "executedQty": "0",                 // Number of completed trades  
        "side": "BUY",                      // Buy/sell direction  
        "type": "LIMIT",                    // Order type  
        "timeInForce": "GTC",               // Time in force method  
        "reduceOnly": false,                // Order is reduce only Y/N  
        "createTime": 1592465880683,        // Order Time  
        "updateTime": 1592465880683,        // Update Time  
        "status": "NEW",                    // Order status  
        "avgPrice": "0",                    // Average price of completed trade  
        "clientOrderId": "",                 // Client order ID           
        "priceScale": 2,  
        "quantityScale": 2,  
        "optionSide": "CALL",  
        "quoteAsset": "USDT",  
        "mmp": false  
      }  
    ]

---

# 查询当前挂单 (USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/options-trading/trade/Query-Current-Open-Option-Orders#接口描述 "接口描述的直接链接")

查询当前挂单（包含状态为ACCEPTED/ PARTIALLY_FILLED的订单）

## HTTP请求[​](/docs/zh-CN/derivatives/options-trading/trade/Query-Current-Open-Option-Orders#http请求 "HTTP请求的直接链接")

GET `/eapi/v1/openOrders`

## 请求权重[​](/docs/zh-CN/derivatives/options-trading/trade/Query-Current-Open-Option-Orders#请求权重 "请求权重的直接链接")

带symbol **1** ，不带**40**

## 请求参数[​](/docs/zh-CN/derivatives/options-trading/trade/Query-Current-Open-Option-Orders#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| NO| 交易对(不传返回所有订单)  
orderId| LONG| NO| 只返回此orderID及之后的订单，缺省返回最近的订单  
startTime| LONG| NO| 开始时间  
endTime| LONG| NO| 结束时间  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/derivatives/options-trading/trade/Query-Current-Open-Option-Orders#响应示例 "响应示例的直接链接")
    
    
    [  
      {  
        "orderId": 4611875134427365377,     // 订单Id  
        "symbol": "BTC-200730-9000-C",      // 交易对  
        "price": "100",                     // 订单价格  
        "quantity": "1",                    // 订单数量  
        "executedQty": "0",                 // 已经成交的交易量  
        "side": "BUY",                      // 订单方向  
        "type": "LIMIT",                    // 订单类型  
        "timeInForce": "GTC",               // 有效时间  
        "reduceOnly": false,                // 仅减仓  
        "createTime": 1592465880683,        // 订单创建时间  
        "updateTime": 1592465880683,        // 订单更新时间  
        "status": "NEW",                    // 订单状态  
        "avgPrice": "0",                    // 已成交平均价  
        "clientOrderId": "",                // 用户自定义订单id         
        "priceScale": 2,                    // 价格精度    
        "quantityScale": 2,                 // 数量精度  
        "optionSide": "CALL",               // 期权类型  
        "quoteAsset": "USDT",               // 报价资产  
        "mmp": false                        // 是否为MMP订单  
      }  
    ]