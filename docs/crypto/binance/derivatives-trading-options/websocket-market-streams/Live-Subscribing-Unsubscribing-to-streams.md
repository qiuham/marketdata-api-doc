---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/derivatives-trading-options/websocket-market-streams/Live-Subscribing-Unsubscribing-to-streams
api_type: WebSocket
updated_at: 2026-11-13 20:28:00.984804
---

# Live Subscribing/Unsubscribing to streams

* The following data can be sent through the websocket instance in order to subscribe/unsubscribe from streams. Examples can be seen below.
  * The `id` used in the JSON payloads is an unsigned INT used as an identifier to uniquely identify the messages going back and forth.



## Subscribe to a stream

> **Request**
    
    
    Code
    
    {
      "method": "SUBSCRIBE",
      "params": ["btc-210630-9000-p@ticker", "btc-210630-9000-p@depth"],
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
      "params": ["btc-210630-9000-p@ticker"],
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
      "result": ["btc-210630-9000-p@ticker"],
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

## Error Messages

Error Message| Description  
---|---  
{"code": 0, "msg": "Unknown property"}| Parameter used in the `SET_PROPERTY` or `GET_PROPERTY` was invalid  
{"code": 1, "msg": "Invalid value type: expected Boolean"}| Value should only be `true` or `false`  
{"code": 2, "msg": "Invalid request: property name must be a string"}| Property name provided was invalid  
{"code": 2, "msg": "Invalid request: request ID must be an unsigned integer"}| Parameter `id` had to be provided or the value provided in the `id` parameter is an unsupported type  
{"code": 2, "msg": "Invalid request: unknown variant %s, expected one of `SUBSCRIBE`, `UNSUBSCRIBE`, `LIST_SUBSCRIPTIONS`, `SET_PROPERTY`, `GET_PROPERTY` at line 1 column 28"}| Possible typo in the provided method or provided method was neither of the expected values  
{"code": 2, "msg": "Invalid request: too many parameters"}| Unnecessary parameters provided in the data  
{"code": 2, "msg": "Invalid request: property name must be a string"}| Property name was not provided  
{"code": 2, "msg": "Invalid request: missing field `method` at line 1 column 73"}| `method` was not provided in the data  
{"code":3,"msg":"Invalid JSON: expected value at line %s column %s"}| JSON data sent has incorrect syntax.    ## Trade Streams  
  
Was this page helpful?

Last modified on November 12, 2026

[Connect](/en/docs/products/derivatives-trading-options/websocket-market-streams/Connect)[How to manage a local order book correctly](/en/docs/products/derivatives-trading-options/websocket-market-streams/How-to-manage-a-local-order-book-correctly)

---

# 实时订阅/取消数据流

* 以下数据可以通过websocket发送以实现订阅或取消订阅数据流。示例如下。
  * 响应内容中的`id`是无符号整数，作为往来信息的唯一标识。



## 订阅一个信息流

> **请求**
    
    
    Code
    
    {
      "method": "SUBSCRIBE",
      "params": ["btc-210630-9000-p@ticker", "btc-210630-9000-p@depth"],
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
      "params": ["btc-210630-9000-p@ticker"],
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
      "result": ["btc-210630-9000-p@ticker"],
      "id": 3
    }

## 设定属性

当前，唯一可以设置的属性是设置是否启用`combined`("组合")信息流。  
当使用`/ws/`("原始信息流")进行连接时，combined属性设置为`false`，而使用 `/stream/`进行连接时则将属性设置为`true`。

> **响应**
    
    
    Code
    
    {
      "result": null
      "id": 5
    }

> **请求**
    
    
    Code
    
    {
      "method": "SET_PROPERTY",
      "params": ["combined", true],
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

## 错误信息

错误信息| 描述  
---|---  
{"code": 0, "msg": "Unknown property"}| `SET_PROPERTY` 或 `GET_PROPERTY`中应用的参数无效  
{"code": 1, "msg": "Invalid value type: expected Boolean"}| 仅接受`true`或`false`  
{"code": 2, "msg": "Invalid request: property name must be a string"}| 提供的属性名无效  
{"code": 2, "msg": "Invalid request: request ID must be an unsigned integer"}| 参数`id`未提供或`id`值是无效类型  
{"code": 2, "msg": "Invalid request: unknown variant %s, expected one of `SUBSCRIBE`, `UNSUBSCRIBE`, `LIST_SUBSCRIPTIONS`, `SET_PROPERTY`, `GET_PROPERTY` at line 1 column 28"}| 错字提醒，或提供的值不是预期类型  
{"code": 2, "msg": "Invalid request: too many parameters"}| 数据中提供了不必要参数  
{"code": 2, "msg": "Invalid request: property name must be a string"}| 未提供属性名  
{"code": 2, "msg": "Invalid request: missing field `method` at line 1 column 73"}| 数据未提供`method`  
{"code":3,"msg":"Invalid JSON: expected value at line %s column %s"}| JSON 语法有误.  
  
此页面是否有帮助？

Last modified on November 12, 2026

[连接](/zh-CN/docs/products/derivatives-trading-options/websocket-market-streams/Connect)[如何正确在本地维护一个 orderbook 副本](/zh-CN/docs/products/derivatives-trading-options/websocket-market-streams/How-to-manage-a-local-order-book-correctly)