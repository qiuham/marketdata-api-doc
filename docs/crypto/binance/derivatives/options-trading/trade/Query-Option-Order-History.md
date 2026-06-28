---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/options-trading/trade/Query-Option-Order-History
api_type: Trading
updated_at: 2026-01-15T23:42:46.526715
---

# Query Option Order History (TRADE)

## API Description[​](/docs/derivatives/options-trading/trade/Query-Option-Order-History#api-description "Direct link to API Description")

Query all finished orders within 5 days, finished status: CANCELLED FILLED REJECTED.

## HTTP Request[​](/docs/derivatives/options-trading/trade/Query-Option-Order-History#http-request "Direct link to HTTP Request")

GET `/eapi/v1/historyOrders`

## Request Weight[​](/docs/derivatives/options-trading/trade/Query-Option-Order-History#request-weight "Direct link to Request Weight")

**3**

## Request Parameters[​](/docs/derivatives/options-trading/trade/Query-Option-Order-History#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES| Option trading pair  
orderId| LONG| NO| Returns the orderId and subsequent orders, the most recent order is returned by default  
startTime| LONG| NO| Start Time, e.g 1593511200000  
endTime| LONG| NO| End Time, e.g 1593512200000  
limit| INT| NO| Number of result sets returned Default:100 Max:1000  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/derivatives/options-trading/trade/Query-Option-Order-History#response-example "Direct link to Response Example")
    
    
    [  
        {  
            "orderId": 4611922413427359795,  
            "symbol": "BTC-220715-2000-C",  
            "price": "18000.00000000",  
            "quantity": "-0.50000000",  
            "executedQty": "-0.50000000",  
            "side": "SELL",  
            "type": "LIMIT",  
            "timeInForce": "GTC",  
            "reduceOnly": false,  
            "createTime": 1657867694244,  
            "updateTime": 1657867888216,  
            "status": "FILLED",  
            "avgPrice": "18000.00000000",  
            "clientOrderId": "",  
            "priceScale": 2,  
            "quantityScale": 2,  
            "optionSide": "CALL",  
            "quoteAsset": "USDT",  
            "mmp": false  
        }  
    ]

---

# 查询历史订单(USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/options-trading/trade/Query-Option-Order-History#接口描述 "接口描述的直接链接")

查询5天内的历史订单，订单的最终状态为 `CANCELED` 或者 `FILLED` 或者 `REJECTED`

## HTTP请求[​](/docs/zh-CN/derivatives/options-trading/trade/Query-Option-Order-History#http请求 "HTTP请求的直接链接")

GET `/eapi/v1/historyOrders`

## 请求权重[​](/docs/zh-CN/derivatives/options-trading/trade/Query-Option-Order-History#请求权重 "请求权重的直接链接")

**3**

## 请求参数[​](/docs/zh-CN/derivatives/options-trading/trade/Query-Option-Order-History#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES| 交易对  
orderId| LONG| NO| 只返回此orderID及之后的订单，缺省返回最近的订单  
startTime| LONG| NO| 起始时间  
endTime| LONG| NO| 结束时间  
limit| INT| NO| 返回的结果集数量 默认值:500 最大值:1000  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/derivatives/options-trading/trade/Query-Option-Order-History#响应示例 "响应示例的直接链接")
    
    
    [  
      {  
        "orderId": 4611875134427365377,     // 订单Id  
        "symbol": "BTC-200730-9000-C",      // 交易对  
        "price": 100,                       // 订单价格  
        "quantity": 1,                      // 订单数量  
        "executedQty": 0,                   // 已经成交的交易量  
        "side": "BUY",                      // 订单方向  
        "type": "LIMIT",                    // 订单类型  
        "timeInForce": "GTC",               // 有效时间  
        "reduceOnly": false,                // 仅减仓  
        "createTime": 1592465880683,        // 订单创建时间  
        "updateTime": 1592465880683,        // 订单更新时间  
        "status": "ACCEPTED",               // 订单状态  
        "avgPrice": "0",                    // 已成交平均价  
        "clientOrderId": "",                // 用户自定义订单id         
        "priceScale": 2,                    // 价格精度    
        "quantityScale": 2,                 // 数量精度  
        "optionSide": "CALL",               // 期权类型  
        "quoteAsset": "USDT",               // 报价资产  
        "mmp": false                        // 是否为MMP订单  
      }  
    ]