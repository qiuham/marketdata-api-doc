---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#overview-websocket-unsubscribe
anchor_id: overview-websocket-unsubscribe
api_type: WebSocket
updated_at: 2026-07-23 19:20:42.318790
---

# Unsubscribe

Unsubscribe from one or more channels.  
  
> Request format description
    
    
    {
      "op": "unsubscribe",
      "args": ["< SubscriptionTopic> "]
    }
    

> Request Example
    
    
    {
      "op": "unsubscribe",
      "args": [
        {
          "channel": "tickers",
          "instId": "BTC-USDT"
        }
      ]
    }
    

**Request parameters**

Parameter | Type | Required | Description  
---|---|---|---  
op | String | Yes | Operation  
`unsubscribe`  
args | Array of objects | Yes | List of channels to unsubscribe from  
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
        "event": "unsubscribe",
        "arg": {
            "channel": "tickers",
            "instId": "BTC-USDT"
        },
        "connId": "d0b44253"
    }
    

**Response parameters**

Parameter | Type | Required | Description  
---|---|---|---  
event | String | Yes | Event  
`unsubscribe`  
`error`  
arg | Object | No | Unsubscribed channel  
> channel | String | Yes | Channel name  
> instType | String | No | Instrument type  
`SPOT`  
`MARGIN`  
`SWAP`  
`FUTURES`  
`OPTION`  
> instFamily | String | No | Instrument family  
Applicable to `FUTURES`/`SWAP`/`OPTION`  
> instId | String | No | Instrument ID  
code | String | No | Error code  
msg | String | No | Error message

---

# 取消订阅

可以取消一个或者多个频道  
  
> 请求格式说明
    
    
    {
        "op": "unsubscribe",
        "args": ["< SubscriptionTopic > "]
    }
    

> 请求示例
    
    
    {
      "op": "unsubscribe",
      "args": [
        {
          "channel": "tickers",
          "instId": "BTC-USDT"
        }
      ]
    }
    

**请求参数**

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
op | String | 是 | 操作，`unsubscribe`  
args | Array of objects | 是 | 取消订阅的频道列表  
> channel | String | 是 | 频道名  
> instType | String | 否 | 产品类型  
`SPOT`：币币  
`MARGIN`：币币杠杆  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`OPTION`：期权  
`ANY`：全部  
> instFamily | String | 否 | 交易品种  
适用于`交割`/`永续`/`期权`  
> instId | String | 否 | 产品ID  
  
> 返回示例
    
    
    {
        "event": "unsubscribe",
        "arg": {
            "channel": "tickers",
            "instId": "BTC-USDT"
        },
        "connId": "d0b44253"
    }
    

**返回参数**

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
event | String | 是 | 事件，`unsubscribe` `error`  
arg | Object | 否 | 取消订阅的频道  
> channel | String | 是 | 频道名  
> instType | String | 否 | 产品类型  
`SPOT`：币币  
`MARGIN`：币币杠杆  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`OPTION`：期权  
`ANY`：全部  
> instFamily | String | 否 | 交易品种  
适用于`交割`/`永续`/`期权`  
> instId | String | 否 | 产品ID  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID