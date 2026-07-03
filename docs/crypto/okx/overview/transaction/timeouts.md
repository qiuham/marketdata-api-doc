---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#overview-transaction-timeouts
anchor_id: overview-transaction-timeouts
api_type: API
updated_at: 2026-07-03 19:38:39.273314
---

# Transaction Timeouts

Orders may not be processed in time due to network delay or busy OKX servers. You can configure the expiry time of the request using `expTime` if you want the order request to be discarded after a specific time.

If `expTime` is specified in the requests for Place (multiple) orders or Amend (multiple) orders, the request will not be processed if the current system time of the server is after the `expTime`.

### REST API

Set the following parameters in the request header

Parameter | Type | Required | Description  
---|---|---|---  
expTime | String | No | Request effective deadline. Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
The following endpoints are supported:

  * [Place order](/docs-v5/en/#order-book-trading-trade-post-place-order)
  * [Place multiple orders](/docs-v5/en/#order-book-trading-trade-post-place-multiple-orders)
  * [Amend order](/docs-v5/en/#order-book-trading-trade-post-amend-order)
  * [Amend multiple orders](/docs-v5/en/#order-book-trading-trade-post-amend-multiple-orders)
  * [POST / Place sub order](/docs-v5/en/#order-book-trading-signal-bot-trading-post-place-sub-order) under signal bot trading

> Request Example
    
    
    curl -X 'POST' \
      'https://openapi.okx.com/api/v5/trade/order' \
      -H 'accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'OK-ACCESS-KEY: *****' \
      -H 'OK-ACCESS-SIGN: *****'' \
      -H 'OK-ACCESS-TIMESTAMP: *****'' \
      -H 'OK-ACCESS-PASSPHRASE: *****'' \
      -H 'expTime: 1597026383085' \   // request effective deadline
      -d '{
      "instId": "BTC-USDT",
      "tdMode": "cash",
      "side": "buy",
      "ordType": "limit",
      "px": "1000",
      "sz": "0.01"
    }'
    

### WebSocket

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

# 交易时效性

由于网络延时或者OKX服务器繁忙会导致订单无法及时处理。如果您对交易时效性有较高的要求，可以灵活设置请求有效截止时间`expTime`以达到你的要求。

（批量）下单，（批量）改单接口请求中如果包含`expTime`，如果服务器当前系统时间超过`expTime`，则该请求不会被服务器处理。

### REST API 

请求头中设置如下参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
expTime | String | 否 | 请求有效截止时间。Unix时间戳的毫秒数格式，如 `1597026383085`  
  
目前支持如下接口： 

  * [下单](/docs-v5/zh/#order-book-trading-trade-post-place-order)
  * [批量下单](/docs-v5/zh/#order-book-trading-trade-post-place-multiple-orders)
  * [修改订单](/docs-v5/zh/#order-book-trading-trade-post-amend-order)
  * [批量修改订单](/docs-v5/zh/#order-book-trading-trade-post-amend-multiple-orders)
  * 信号交易的 [POST / 下单](/docs-v5/zh/#order-book-trading-signal-bot-trading-post-place-sub-order)

> 请求示例
    
    
    curl -X 'POST' \
      'https://openapi.okx.com/api/v5/trade/order' \
      -H 'accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'OK-ACCESS-KEY: *****' \
      -H 'OK-ACCESS-SIGN: *****'' \
      -H 'OK-ACCESS-TIMESTAMP: *****'' \
      -H 'OK-ACCESS-PASSPHRASE: *****'' \
      -H 'expTime: 1597026383085' \   // 有效截止时间
      -d '{
      "instId": "BTC-USDT",
      "tdMode": "cash",
      "side": "buy",
      "ordType": "limit",
      "px": "1000",
      "sz": "0.01"
    }'
    

### WebSocket 

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