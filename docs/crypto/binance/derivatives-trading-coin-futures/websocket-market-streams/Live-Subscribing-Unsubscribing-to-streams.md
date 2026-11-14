---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/derivatives-trading-coin-futures/websocket-market-streams/Live-Subscribing-Unsubscribing-to-streams
api_type: WebSocket
updated_at: 2026-11-13 20:27:49.081115
---

# Live Subscribing/Unsubscribing to streams

* The following data can be sent through the websocket instance in order to subscribe/unsubscribe from streams. Examples can be seen below.
  * The `id` used in the JSON payloads is an unsigned INT used as an identifier to uniquely identify the messages going back and forth.



## Subscribe to a stream

> **Request**
    
    
    Code
    
    {
      "method": "SUBSCRIBE",
      "params": ["btcusd_200925@aggTrade", "btcusd_200925@depth"],
      "id": 1
    }

> **Response**
    
    
    Code
    
    {
      "result": null,
      "id": 1
    }

## Unsubscribe to a stream

> **Request**
    
    
    Code
    
    {
      "method": "UNSUBSCRIBE",
      "params": ["btcusd_200925@depth"],
      "id": 312
    }

> **Response**
    
    
    Code
    
    {
      "result": null,
      "id": 312
    }

## Listing Subscriptions

> **Request**
    
    
    Code
    
    {
      "method": "LIST_SUBSCRIPTIONS",
      "id": 3
    }

> **Response**
    
    
    Code
    
    {
      "result": ["btcusd_200925@aggTrade"],
      "id": 3
    }

## Setting Properties

Currently, the only property can be set is to set whether `combined` stream payloads are enabled are not. The combined property is set to `false` when connecting using `/ws/` ("raw streams") and `true` when connecting using `/stream/`.

> **Request**
    
    
    Code
    
    {
      "method": "SET_PROPERTY",
      "params": ["combined", true],
      "id": 5
    }

> **Response**
    
    
    Code
    
    {
      "result": null,
      "id": 5
    }

## Retrieving Properties

> **Request**
    
    
    Code
    
    {
      "method": "GET_PROPERTY",
      "params": ["combined"],
      "id": 2
    }

> **Response**
    
    
    Code
    
    {
      "result": true, // Indicates that combined is set to true.
      "id": 2
    }

Was this page helpful?

Last modified on November 12, 2026

[Connect](/en/docs/products/derivatives-trading-coin-futures/websocket-market-streams/Connect)[How to manage a local order book correctly](/en/docs/products/derivatives-trading-coin-futures/websocket-market-streams/How-to-manage-a-local-order-book-correctly)

---

# 实时订阅/取消数据流

* 以下数据可以通过websocket发送以实现订阅或取消订阅数据流。示例如下。
  * 响应内容中的`id`是无符号整数，作为往来信息的唯一标识。



## 订阅一个信息流

> **请求**
    
    
    Code
    
    {
      "method": "SUBSCRIBE",
      "params": ["btcusd_200925@aggTrade", "btcusd_200925@depth"],
      "id": 1
    }

> **响应**
    
    
    Code
    
    {
      "result": null,
      "id": 1
    }

## 取消订阅一个信息流

> **请求**
    
    
    Code
    
    {
      "method": "UNSUBSCRIBE",
      "params": ["btcusd_200925@depth"],
      "id": 312
    }

> **响应**
    
    
    Code
    
    {
      "result": null,
      "id": 312
    }

## 已订阅信息流

> **请求**
    
    
    Code
    
    {
      "method": "LIST_SUBSCRIPTIONS",
      "id": 3
    }

> **响应**
    
    
    Code
    
    {
      "result": ["btcusd_200925@aggTrade"],
      "id": 3
    }

## 设定属性

当前，唯一可以设置的属性是设置是否启用`combined`("组合")信息流。  
当使用`/ws/`("原始信息流")进行连接时，combined属性设置为`false`，而使用 `/stream/`进行连接时则将属性设置为`true`。

> **请求**
    
    
    Code
    
    {
      "method": "SET_PROPERTY",
      "params": ["combined", true],
      "id": 5
    }

> **响应**
    
    
    Code
    
    {
      "result": null
      "id": 5
    }

## 检索属性

> **请求**
    
    
    Code
    
    {
      "method": "GET_PROPERTY",
      "params": ["combined"],
      "id": 2
    }

> **响应**
    
    
    Code
    
    {
      "result": true, // Indicates that combined is set to true.
      "id": 2
    }

此页面是否有帮助？

Last modified on November 12, 2026

[市场数据连接](/zh-CN/docs/products/derivatives-trading-coin-futures/websocket-market-streams/Connect)[如何正确在本地维护一个orderbook副本](/zh-CN/docs/products/derivatives-trading-coin-futures/websocket-market-streams/How-to-manage-a-local-order-book-correctly)