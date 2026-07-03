---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#overview-websocket-subscribe
anchor_id: overview-websocket-subscribe
api_type: WebSocket
updated_at: 2026-07-03 19:38:36.784996
---

# Subscribe

**Subscription Instructions**

> Request format description
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": ["<SubscriptionTopic>"]
    }
    

WebSocket channels are divided into two categories: `public` and `private` channels.

`Public channels` \-- No authentication is required, include tickers channel, K-Line channel, limit price channel, order book channel, and mark price channel etc.

`Private channels` \-- including account channel, order channel, and position channel, etc -- require log in.

Users can choose to subscribe to one or more channels, and the total length of multiple channels cannot exceed 64 KB.

Below is an example of subscription parameters. The requirement of subscription parameters for each channel is different. For details please refer to the specification of each channels.

> Request Example
    
    
    {
        "id": "1512",
        "op":"subscribe",
        "args":[
            {
                "channel":"tickers",
                "instId":"BTC-USDT"
            }
        ]
    }
    

**Request parameters**

Parameter | Type | Required | Description  
---|---|---|---  
id | String | No | Unique identifier of the message   
Provided by client. It will be returned in response message for identifying the corresponding request.   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
op | String | Yes | Operation  
`subscribe`  
args | Array of objects | Yes | List of subscribed channels  
> channel | String | Yes | Channel name  
> instType | String | No | Instrument type  
`SPOT`  
`MARGIN`  
`SWAP`  
`FUTURES`  
`OPTION`  
`ANY`  
> instFamily | String | No | Instrument family  
Applicable to `FUTURES`/`SWAP`/`OPTION`  
> instId | String | No | Instrument ID  
  
> Response Example
    
    
    {
        "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "tickers",
            "instId": "BTC-USDT"
        },
        "connId": "accb8e21"
    }
    

**Return parameters**

Parameter | Type | Required | Description  
---|---|---|---  
id | String | No | Unique identifier of the message  
event | String | Yes | Event  
`subscribe`  
`error`  
arg | Object | No | Subscribed channel  
> channel | String | Yes | Channel name  
> instType | String | No | Instrument type  
`SPOT`  
`MARGIN`  
`SWAP`  
`FUTURES`  
`OPTION`  
`ANY`  
> instFamily | String | No | Instrument family  
Applicable to `FUTURES`/`SWAP`/`OPTION`  
> instId | String | No | Instrument ID  
code | String | No | Error code  
msg | String | No | Error message  
connId | String | Yes | WebSocket connection ID

---

# 订阅

**订阅说明**

> 请求格式说明
    
    
    {
        "op": "subscribe",
        "args": ["<SubscriptionTopic>"]
    }
    

WebSocket 频道分成两类： `公共频道` 和 `私有频道`

`公共频道`无需登录，包括行情频道，K线频道，交易数据频道，资金费率频道，限价范围频道，深度数据频道，标记价格频道等。

`私有频道`需登录，包括用户账户频道，用户交易频道，用户持仓频道等。

用户可以选择订阅一个或者多个频道，多个频道总长度不能超过 64 KB。

以下是一个请求参数的例子。每一个频道的请求参数的要求都不一样。请根据每一个频道的需求来订阅频道。

> 请求示例
    
    
    {
        "op":"subscribe",
        "args":[
            {
                "channel":"tickers",
                "instId":"BTC-USDT"
            }
        ]
    }
    
    

**请求参数**

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
op | String | 是 | 操作，`subscribe`  
args | Array of objects | 是 | 请求订阅的频道列表  
> channel | String | 是 | 频道名  
> instType | String | 否 | 产品类型  
`SPOT`：币币   
`MARGIN`：币币杠杆  
`SWAP`：永续  
`FUTURES`：交割  
`OPTION`：期权  
`ANY`：全部  
> instFamily | String | 否 | 交易品种  
适用于`交割`/`永续`/`期权`  
> instId | String | 否 | 产品ID  
  
> 返回示例 
    
    
    {
        "event": "subscribe",
        "arg": {
            "channel": "tickers",
            "instId": "BTC-USDT"
        },
        "connId": "accb8e21"
    }
    

**返回参数**

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
event | String | 是 | 事件，`subscribe` `error`  
arg | Object | 否 | 订阅的频道  
> channel | String | 是 | 频道名  
> instType | String | 否 | 产品类型  
`SPOT`：币币  
`MARGIN`：币币杠杆  
`SWAP`：永续  
`FUTURES`：交割  
`OPTION`：期权  
`ANY`：全部  
> instFamily | String | 否 | 交易品种  
适用于`交割`/`永续`/`期权`  
> instId | String | 否 | 产品ID  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID