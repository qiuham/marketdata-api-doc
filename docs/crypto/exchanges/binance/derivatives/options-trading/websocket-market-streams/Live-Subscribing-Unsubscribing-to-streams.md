---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/options-trading/websocket-market-streams/Live-Subscribing-Unsubscribing-to-streams
api_type: WebSocket
updated_at: 2026-01-15T23:43:52.747046
---

# Live Subscribing/Unsubscribing to streams

* The following data can be sent through the websocket instance in order to subscribe/unsubscribe from streams. Examples can be seen below.
  * The `id` used in the JSON payloads is an unsigned INT used as an identifier to uniquely identify the messages going back and forth.



## Subscribe to a stream[​](/docs/derivatives/options-trading/websocket-market-streams/Live-Subscribing-Unsubscribing-to-streams#subscribe-to-a-stream "Direct link to Subscribe to a stream")

> **Response**
    
    
    {  
      "result": null,  
      "id": 1  
    }  
    

  * **Request**



{  
"method": "SUBSCRIBE",  
"params":  
[  
"BTC-210630-9000-P@ticker",  
"BTC-210630-9000-P@depth"  
],  
"id": 1  
}

## Unsubscribe to a stream[​](/docs/derivatives/options-trading/websocket-market-streams/Live-Subscribing-Unsubscribing-to-streams#unsubscribe-to-a-stream "Direct link to Unsubscribe to a stream")

> **Response**
    
    
    {  
      "result": null,  
      "id": 312  
    }  
    

  * **Request**

{  
"method": "UNSUBSCRIBE",  
"params":  
[  
"BTC-210630-9000-P@ticker"  
],  
"id": 312  
}




## Listing Subscriptions[​](/docs/derivatives/options-trading/websocket-market-streams/Live-Subscribing-Unsubscribing-to-streams#listing-subscriptions "Direct link to Listing Subscriptions")

> **Response**
    
    
    {  
      "result": [  
        "BTC-210630-9000-P@ticker"  
      ],  
      "id": 3  
    }  
    

  * **Request**

{  
"method": "LIST_SUBSCRIPTIONS",  
"id": 3  
}




## Setting Properties[​](/docs/derivatives/options-trading/websocket-market-streams/Live-Subscribing-Unsubscribing-to-streams#setting-properties "Direct link to Setting Properties")

Currently, the only property can be set is to set whether `combined` stream payloads are enabled are not. The combined property is set to `false` when connecting using `/ws/` ("raw streams") and `true` when connecting using `/stream/`.

> **Response**
    
    
    {  
      "result": null,  
      "id": 5  
    }  
    

  * **Request**

{  
"method": "SET_PROPERTY",  
"params":  
[  
"combined",  
true  
],  
"id": 5  
}




## Retrieving Properties[​](/docs/derivatives/options-trading/websocket-market-streams/Live-Subscribing-Unsubscribing-to-streams#retrieving-properties "Direct link to Retrieving Properties")

> **Response**
    
    
    {  
      "result": true, // Indicates that combined is set to true.  
      "id": 2  
    }  
    

  * **Request**

{  
"method": "GET_PROPERTY",  
"params":  
[  
"combined"  
],  
"id": 2  
}      




## Error Messages[​](/docs/derivatives/options-trading/websocket-market-streams/Live-Subscribing-Unsubscribing-to-streams#error-messages "Direct link to Error Messages")

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

---

# 实时订阅/取消数据流

* 以下数据可以通过websocket发送以实现订阅或取消订阅数据流。示例如下。
  * 响应内容中的`id`是无符号整数，作为往来信息的唯一标识。



## 订阅一个信息流[​](/docs/zh-CN/derivatives/options-trading/websocket-market-streams/Live-Subscribing-Unsubscribing-to-streams#订阅一个信息流 "订阅一个信息流的直接链接")

> **响应**
    
    
    {  
      "result": null,  
      "id": 1  
    }  
    

  * **请求**

{  
"method": "SUBSCRIBE",  
"params":  
[  
"BTC-210630-9000-P@ticker",  
"BTC-210630-9000-P@depth"  
],  
"id": 1  
}




## 取消订阅一个信息流[​](/docs/zh-CN/derivatives/options-trading/websocket-market-streams/Live-Subscribing-Unsubscribing-to-streams#取消订阅一个信息流 "取消订阅一个信息流的直接链接")

> **响应**
    
    
    {  
      "result": null,  
      "id": 312  
    }  
    

  * **请求**

{  
"method": "UNSUBSCRIBE",  
"params":  
[  
"BTC-210630-9000-P@ticker"  
],  
"id": 312  
}




## 已订阅信息流[​](/docs/zh-CN/derivatives/options-trading/websocket-market-streams/Live-Subscribing-Unsubscribing-to-streams#已订阅信息流 "已订阅信息流的直接链接")

> **响应**
    
    
    {  
      "result": [  
        "BTC-210630-9000-P@ticker"  
      ],  
      "id": 3  
    }  
    

  * **请求**

{  
"method": "LIST_SUBSCRIPTIONS",  
"id": 3  
}




## 设定属性[​](/docs/zh-CN/derivatives/options-trading/websocket-market-streams/Live-Subscribing-Unsubscribing-to-streams#设定属性 "设定属性的直接链接")

当前，唯一可以设置的属性是设置是否启用`combined`("组合")信息流。  
当使用`/ws/`("原始信息流")进行连接时，combined属性设置为`false`，而使用 `/stream/`进行连接时则将属性设置为`true`。

> **响应**
    
    
    {  
      "result": null  
      "id": 5  
    }  
    

  * **请求**

{  
"method": "SET_PROPERTY",  
"params":  
[  
"combined",  
true  
],  
"id": 5  
}




## 检索属性[​](/docs/zh-CN/derivatives/options-trading/websocket-market-streams/Live-Subscribing-Unsubscribing-to-streams#检索属性 "检索属性的直接链接")

> **响应**
    
    
    {  
      "result": true, // Indicates that combined is set to true.  
      "id": 2  
    }  
    

  * **请求**

{  
"method": "GET_PROPERTY",  
"params":  
[  
"combined"  
],  
"id": 2  
}




## 错误信息[​](/docs/zh-CN/derivatives/options-trading/websocket-market-streams/Live-Subscribing-Unsubscribing-to-streams#错误信息 "错误信息的直接链接")

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