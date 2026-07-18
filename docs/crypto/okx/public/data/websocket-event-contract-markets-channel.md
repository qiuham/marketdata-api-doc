---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#public-data-websocket-event-contract-markets-channel
anchor_id: public-data-websocket-event-contract-markets-channel
api_type: WebSocket
updated_at: 2026-07-18 20:04:44.752109
---

# Event contract markets channel

Pushes event contract market status updates and floorStrike generation. No initial snapshot push.

#### URL Path

/ws/v5/public

> Request Example
    
    
    {
        "op": "subscribe",
        "args": [
            {
                "channel": "event-contract-markets",
                "instType": "EVENTS"
            }
        ]
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
id | String | No | Unique identifier of the message. Provided by client. Returned in response. Alphanumeric, 1-32 characters.  
op | String | Yes | Operation.  
`subscribe`  
`unsubscribe`  
args | Array of objects | Yes | List of subscribed channels  
> channel | String | Yes | Channel name.  
`event-contract-markets`  
> instType | String | Yes | Instrument type.  
`EVENTS`  
  
> Successful Response Example
    
    
    {
        "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "event-contract-markets",
            "instType": "EVENTS"
        },
        "connId": "a4d3ae55"
    }
    

> Failure Response Example
    
    
    {
        "id": "1512",
        "event": "error",
        "code": "60012",
        "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{\"channel\": \"event-contract-markets\", \"instType\": \"EVENTS\"}]}",
        "connId": "a4d3ae55"
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
id | String | Unique identifier of the message  
event | String | Event.  
`subscribe`  
`unsubscribe`  
`error`  
arg | Object | Subscribed channel  
> channel | String | Channel name  
> instType | String | Instrument type  
code | String | Error code  
msg | String | Error message  
connId | String | WebSocket connection ID  
  
> Push Data Example
    
    
    {
        "arg": {
            "channel": "event-contract-markets"
        },
        "data": [
            {
                "seriesId": "BTC-ABOVE-DAILY",
                "eventId": "BTC-ABOVE-DAILY-260224-1600",
                "instId": "BTC-ABOVE-DAILY-260224-1600-65000",
                "listTime": "1769697132335",
                "fixTime": "",
                "expTime": "1769697132335",
                "state": "live",
                "outcome": "0",
                "floorStrike": "120000",
                "capStrike": "",
                "settleValue": "",
                "disputed": false,
                "hitDir": ""
            }
        ]
    }
    

#### Push Data Parameters

Parameter | Type | Description  
---|---|---  
arg | Object | Subscribed channel  
> channel | String | Channel name  
data | Array of objects | Subscribed data  
> seriesId | String | Series ID, e.g. `BTC-ABOVE-DAILY`  
> eventId | String | Event ID, e.g. `BTC-ABOVE-DAILY-260224-1600`  
> instId | String | Instrument ID, e.g. `BTC-ABOVE-DAILY-260224-1600-65000`  
> listTime | String | Listing time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
> fixTime | String | Strike price fixing time, Unix timestamp format in milliseconds, e.g. `1597026383085`. Only applicable to `price_up_down` settlement method.  
> expTime | String | Strike time for this event, Unix timestamp format in milliseconds, e.g. `1597026383085`. Updated once the market is settled.  
> state | String | Market state.  
`preopen`  
`live`  
`settling`  
`expired`  
> outcome | String | Market outcome.  
`0`: Not available  
`1`: YES  
`2`: NO.  
`1`/`2` only applicable when state is `expired`  
> floorStrike | String | Minimum expiration value that leads to a YES outcome  
> capStrike | String | Maximum expiration value that leads to a YES outcome for `between` method. `"INF"` indicates no upper bound (the topmost bracket).  
Returns `""` for non-`between` methods.  
> settleValue | String | Settlement value  
Only return when the state is `expired`  
> disputed | Boolean | Whether the market has been disputed.  
`true`  
`false`  
> hitDir | String | Hit direction. Only applicable when the settlement method is `hit`.  
`up`: price hit from below  
`dn`: price hit from above  
`""`: not applicable (non-`hit` methods)

---

# 事件合约市场频道

推送事件合约市场状态更新及 floorStrike 生成。不推送初始快照。

#### URL Path

/ws/v5/public

> 请求示例
    
    
    {
        "op": "subscribe",
        "args": [
            {
                "channel": "event-contract-markets",
                "instType": "EVENTS"
            }
        ]
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
id | String | 否 | 消息的唯一标识。用户提供，返回参数中会返回以便于找到相应的请求。字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度必须要在1-32位之间。  
op | String | 是 | 操作。  
`subscribe`  
`unsubscribe`  
args | Array of objects | 是 | 订阅频道列表  
> channel | String | 是 | 频道名。  
`event-contract-markets`  
> instType | String | 是 | 产品类型。  
`EVENTS`  
  
> 成功返回示例
    
    
    {
        "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "event-contract-markets",
            "instType": "EVENTS"
        },
        "connId": "a4d3ae55"
    }
    

> 失败返回示例
    
    
    {
        "id": "1512",
        "event": "error",
        "code": "60012",
        "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{\"channel\": \"event-contract-markets\", \"instType\": \"EVENTS\"}]}",
        "connId": "a4d3ae55"
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
id | String | 消息的唯一标识  
event | String | 事件。  
`subscribe`  
`unsubscribe`  
`error`  
arg | Object | 订阅的频道  
> channel | String | 频道名  
> instType | String | 产品类型  
code | String | 错误码  
msg | String | 错误消息  
connId | String | WebSocket 连接 ID  
  
> 推送数据示例
    
    
    {
        "arg": {
            "channel": "event-contract-markets"
        },
        "data": [
            {
                "seriesId": "BTC-ABOVE-DAILY",
                "eventId": "BTC-ABOVE-DAILY-260224-1600",
                "instId": "BTC-ABOVE-DAILY-260224-1600-65000",
                "listTime": "1769697132335",
                "fixTime": "",
                "expTime": "1769697132335",
                "state": "live",
                "outcome": "0",
                "floorStrike": "120000",
                "capStrike": "",
                "settleValue": "",
                "disputed": false,
                "hitDir": ""
            }
        ]
    }
    

#### 推送数据参数

参数名 | 类型 | 描述  
---|---|---  
arg | Object | 订阅的频道  
> channel | String | 频道名  
data | Array of objects | 订阅数据  
> seriesId | String | 系列 ID，如 `BTC-ABOVE-DAILY`  
> eventId | String | 事件 ID，如 `BTC-ABOVE-DAILY-260224-1600`  
> instId | String | 产品 ID，如 `BTC-ABOVE-DAILY-260224-1600-65000`  
> listTime | String | 上线时间。Unix时间戳的毫秒数格式，如 `1597026383085`  
> fixTime | String | 行权价格确定时间。Unix时间戳的毫秒数格式，如 `1597026383085`。仅适用于 `price_up_down` 结算方式。  
> expTime | String | 行权时间。Unix时间戳的毫秒数格式，如 `1597026383085`。结算后更新。  
> state | String | 市场状态。  
`preopen`  
`live`  
`settling`  
`expired`  
> outcome | String | 市场结果。  
`0`：未确定  
`1`：YES  
`2`：NO。  
`1`/`2` 仅在 state 为 `expired` 时适用  
> floorStrike | String | 导致 YES 结果的最低到期价格  
> capStrike | String | `between` 结算方式中导致 YES 结果的最大到期值。`"INF"` 表示无上限（最高区间）。  
非 `between` 方式返回 `""`。  
> settleValue | String | 结算价格。  
仅在 state 为 `expired` 时返回  
> disputed | Boolean | 是否存在争议。  
`true`  
`false`  
> hitDir | String | 触及方向。仅在结算方式为 `hit` 时适用。  
`up`：价格从下方触及  
`dn`：价格从上方触及  
`""`：不适用（非 `hit` 方式）