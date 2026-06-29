---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#overview-transaction-timeouts-websocket
anchor_id: overview-transaction-timeouts-websocket
api_type: WebSocket
updated_at: 2026-06-29 19:55:25.417862
---

# WebSocket

The following parameters are set in the request

Parameter | Type | Required | Description  
---|---|---|---  
expTime | String | No | Request effective deadline. Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
The following endpoints are supported:

  * [Place order](/docs-v5/en/#order-book-trading-trade-ws-place-order)
  * [Place multiple orders](/docs-v5/en/#order-book-trading-trade-ws-place-multiple-orders)
  * [Amend order](/docs-v5/en/#order-book-trading-trade-ws-amend-order)
  * [Amend multiple orders](/docs-v5/en/#order-book-trading-trade-ws-amend-multiple-orders)

> Request Example
    
    
    {
        "id": "1512",
        "op": "order",
        "expTime":"1597026383085",  // request effective deadline
        "args": [{
            "side": "buy",
            "instId": "BTC-USDT",
            "tdMode": "isolated",
            "ordType": "market",
            "sz": "100"
        }]
    }

---

# WebSocket

请求中设置如下参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
expTime | String | 否 | 请求有效截止时间。Unix时间戳的毫秒数格式，如 `1597026383085`  
  
目前支持如下接口： 

  * [下单](/docs-v5/zh/#order-book-trading-trade-ws-place-order)
  * [批量下单](/docs-v5/zh/#order-book-trading-trade-ws-place-multiple-orders)
  * [修改订单](/docs-v5/zh/#order-book-trading-trade-ws-amend-order)
  * [批量修改订单](/docs-v5/zh/#order-book-trading-trade-ws-amend-multiple-orders)

> 请求示例
    
    
    {
        "id": "1512",
        "op": "order",
        "expTime":"1597026383085",  // 有效截止时间
        "args": [{
            "side": "buy",
            "instId": "BTC-USDT",
            "tdMode": "isolated",
            "ordType": "market",
            "sz": "100"
        }]
    }