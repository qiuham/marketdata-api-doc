---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/derivatives-trading-coin-futures/websocket-market-streams/Live-Subscribing-Unsubscribing-to-streams
api_type: WebSocket
updated_at: 2026-11-18 02:22:45.339531
---

# Live Subscribing/Unsubscribing to streams

- The following data can be sent through the websocket instance in order to subscribe/unsubscribe
  from streams. Examples can be seen below.
- The `id` used in the JSON payloads is an unsigned INT used as an identifier to uniquely identify
  the messages going back and forth.

## Subscribe to a stream

> **Request**

```json
{
  "method": "SUBSCRIBE",
  "params": ["btcusd_200925@aggTrade", "btcusd_200925@depth"],
  "id": 1
}
```

> **Response**

```json
{
  "result": null,
  "id": 1
}
```

## Unsubscribe to a stream

> **Request**

```json
{
  "method": "UNSUBSCRIBE",
  "params": ["btcusd_200925@depth"],
  "id": 312
}
```

> **Response**

```json
{
  "result": null,
  "id": 312
}
```

## Listing Subscriptions

> **Request**

```json
{
  "method": "LIST_SUBSCRIPTIONS",
  "id": 3
}
```

> **Response**

```json
{
  "result": ["btcusd_200925@aggTrade"],
  "id": 3
}
```

## Setting Properties

Currently, the only property can be set is to set whether `combined` stream payloads are enabled are
not. The combined property is set to `false` when connecting using `/ws/` ("raw streams") and `true`
when connecting using `/stream/`.

> **Request**

```json
{
  "method": "SET_PROPERTY",
  "params": ["combined", true],
  "id": 5
}
```

> **Response**

```json
{
  "result": null,
  "id": 5
}
```

## Retrieving Properties

> **Request**

```json
{
  "method": "GET_PROPERTY",
  "params": ["combined"],
  "id": 2
}
```

> **Response**

```json
{
  "result": true, // Indicates that combined is set to true.
  "id": 2
}
```

---

# 实时订阅/取消数据流

- 以下数据可以通过websocket发送以实现订阅或取消订阅数据流。示例如下。
- 响应内容中的`id`是无符号整数，作为往来信息的唯一标识。

## 订阅一个信息流

> **请求**

```json
{
  "method": "SUBSCRIBE",
  "params": ["btcusd_200925@aggTrade", "btcusd_200925@depth"],
  "id": 1
}
```

> **响应**

```json
{
  "result": null,
  "id": 1
}
```

## 取消订阅一个信息流

> **请求**

```json
{
  "method": "UNSUBSCRIBE",
  "params": ["btcusd_200925@depth"],
  "id": 312
}
```

> **响应**

```json
{
  "result": null,
  "id": 312
}
```

## 已订阅信息流

> **请求**

```json
{
  "method": "LIST_SUBSCRIPTIONS",
  "id": 3
}
```

> **响应**

```json
{
  "result": ["btcusd_200925@aggTrade"],
  "id": 3
}
```

## 设定属性

当前，唯一可以设置的属性是设置是否启用`combined`("组合")信息流。  
当使用`/ws/`("原始信息流")进行连接时，combined属性设置为`false`，而使用 `/stream/`进行连接时则将属性设置为`true`。

> **请求**

```json
{
  "method": "SET_PROPERTY",
  "params": ["combined", true],
  "id": 5
}
```

> **响应**

```json
{
  "result": null
  "id": 5
}
```

## 检索属性

> **请求**

```json
{
  "method": "GET_PROPERTY",
  "params": ["combined"],
  "id": 2
}
```

> **响应**

```json
{
  "result": true, // Indicates that combined is set to true.
  "id": 2
}
```