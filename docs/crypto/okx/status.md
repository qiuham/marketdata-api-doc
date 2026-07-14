---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#status
anchor_id: status
api_type: API
updated_at: 2026-07-14 19:21:16.497919
---

# Status

## GET / Status  
  
Get event status of system upgrade.

Planned system maintenance that may result in short interruption (lasting less than 5 seconds) or websocket disconnection (users can immediately reconnect) will not be announced. The maintenance will only be performed during times of low market volatility.

#### Rate Limit: 1 request per 5 seconds

#### HTTP Request

`GET /api/v5/system/status`

> Request Example
    
    
    GET /api/v5/system/status
    
    GET /api/v5/system/status?state=canceled
    
    
    
    
    import okx.Status as Status
    
    flag = "0"  # Production trading: 0, Demo trading: 1
    statusAPI = Status.StatusAPI(
        domain="https://openapi.okx.com",
        flag=flag,
    )
    
    # Get event status of system upgrade
    result = statusAPI.status()
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
state | String | No | System maintenance status  
`scheduled`: waiting  
`ongoing`: processing  
`pre_open`: pre_open  
`completed`: completed  
`canceled`: canceled  
Generally, `pre_open` last about 10 minutes. There will be `pre_open` when the time of upgrade is too long.   
If this parameter is not filled, the data with status `scheduled`, `ongoing` and `pre_open` will be returned by default  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "begin": "1672823400000",
                "end": "1672823520000",
                "href": "",
                "preOpenBegin": "",
                "scheDesc": "",
                "serviceType": "8",
                "state": "completed",
                "maintType": "1",
                "env": "1",
                "system": "unified",
                "title": "Trading account system upgrade (in batches of accounts)"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
title | String | The title of system maintenance instructions  
state | String | System maintenance status  
begin | String | Begin time of system maintenance, Unix timestamp format in milliseconds, e.g. `1617788463867`  
end | String | Time of resuming trading totally. Unix timestamp format in milliseconds, e.g. `1617788463867`.  
It is expected end time before `completed`, changed to actual end time after `completed`.  
preOpenBegin | String | The time of pre_open. Canceling orders, placing Post Only orders, and transferring funds to trading accounts are back after `preOpenBegin`.  
href | String | Hyperlink for system maintenance details, if there is no return value, the default value will be empty. e.g. ""  
serviceType | String | Service type  
`0`: WebSocket  
`5`: Trading service  
`6`: Block trading  
`7`: Trading bot  
`8`: Trading service (in batches of accounts)  
`9`: Trading service (in batches of products)  
`10`: Spread trading  
`11`: Copy trading  
`99`: Others (e.g. Suspend partial instruments)  
system | String | System  
`unified`: Trading account  
scheDesc | String | Rescheduled description, e.g. `Rescheduled from 2021-01-26T16:30:00.000Z` to `2021-01-28T16:30:00.000Z`  
maintType | String | Maintenance type  
`1`: Scheduled maintenance  
`2`: Unscheduled maintenance  
`3`: System disruption  
env | String | Environment  
`1`: Production Trading  
`2`: Demo Trading  
  
## WS / Status channel

Get the status of system maintenance and push when rescheduling and the system maintenance status and end time changes. First subscription: "Push the latest change data"; every time there is a state change, push the changed content.

Planned system maintenance that may result in short interruption (lasting less than 5 seconds) or websocket disconnection (users can immediately reconnect) will not be announced. The maintenance will only be performed during times of low market volatility.

#### URL Path

/ws/v5/public

> Request Example
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "status"
        }
      ]
    }
    
    
    
    import asyncio
    from okx.websocket.WsPublicAsync import WsPublicAsync
    
    def callbackFunc(message):
        print(message)
    
    async def main():
        ws = WsPublicAsync(url="wss://wspap.okx.com:8443/ws/v5/public")
        await ws.start()
        args = [{
            "channel": "status"
        }]
    
        await ws.subscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
        await ws.unsubscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
    asyncio.run(main())
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
id | String | No | Unique identifier of the message   
Provided by client. It will be returned in response message for identifying the corresponding request.   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
op | String | Yes | `subscribe` `unsubscribe`  
args | Array of objects | Yes | List of subscribed channels  
> channel | String | Yes | Channel name  
`status`  
  
> Successful Response Example
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "status"
      },
      "connId": "a4d3ae55"
    }
    

> Failure Response Example
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"statuss\"}]}",
      "connId": "a4d3ae55"
    }
    

#### Response parameters

Parameter | Type | Required | Description  
---|---|---|---  
id | String | No | Unique identifier of the message  
event | String | Yes | `subscribe` `unsubscribe` `error`  
arg | Object | No | Subscribed channel  
> channel | String | Yes | Channel name  
`status`  
code | String | No | Error code  
msg | String | No | Error message  
connId | String | Yes | WebSocket connection ID  
  
> Push Data Example
    
    
    {
        "arg": {
            "channel": "status"
        },
        "data": [
            {
                "begin": "1672823400000",
                "end": "1672825980000",
                "href": "",
                "preOpenBegin": "",
                "scheDesc": "",
                "serviceType": "0",
                "state": "completed",
                "system": "unified",
                "maintType": "1",
                "env": "1",
                "title": "Trading account WebSocket system upgrade",
                "ts": "1672826038470"
            }
        ]
    }
    

#### Push data parameters

Parameter | Type | Description  
---|---|---  
arg | Object | Successfully subscribed channel  
> channel | String | Channel name  
data | Array of objects | Subscribed data  
> title | String | The title of system maintenance instructions  
> state | String | System maintenance status,`scheduled`: waiting; `ongoing`: processing; `pre_open`: pre_open; `completed`: completed ;`canceled`: canceled.   
Generally, `pre_open` last about 10 minutes. There will be `pre_open` when the time of upgrade is too long.  
> begin | String | Start time of system maintenance, Unix timestamp format in milliseconds, e.g. `1617788463867`  
> end | String | Time of resuming trading totally. Unix timestamp format in milliseconds, e.g. `1617788463867`.  
It is expected end time before `completed`, changed to actual end time after `completed`.  
> preOpenBegin | String | The time of pre_open. Canceling orders, placing Post Only orders, and transferring funds to trading accounts are back after `preOpenBegin`.  
> href | String | Hyperlink for system maintenance details, if there is no return value, the default value will be empty. e.g. “”  
> serviceType | String | Service type, `0`: WebSocket ; `5`: Trading service; `6`: Block trading; `7`: Trading bot; `8`: Trading service (in batches of accounts); `9`: Trading service (in batches of products); `10`: Spread trading; `11`: Copy trading; `99`: Others (e.g. Suspend partial instruments)  
> system | String | System, `unified`: Trading account  
> scheDesc | String | Rescheduled description, e.g. `Rescheduled from 2021-01-26T16:30:00.000Z to 2021-01-28T16:30:00.000Z`  
> maintType | String | Maintenance type  
`1`: Scheduled maintenance; `2`: Unscheduled maintenance; `3`: System disruption  
> env | String | Environment.  
`1`: Production Trading, `2`: Demo Trading  
> ts | String | Push time due to change event, Unix timestamp format in milliseconds, e.g. `1617788463867`

---

# Status

## GET / Status   
  
获取系统升级事件的状态。

由计划系统维护引起的短暂不可用（<5秒）和WebSocket闪断连接（用户可以立即重连）将不会公布。此类维护只会在市场波动性低的时期进行。

#### 限速：1次/5s

#### HTTP请求

`GET /api/v5/system/status`

> 请求示例
    
    
    GET /api/v5/system/status
    
    GET /api/v5/system/status?state=canceled
    
    
    
    
    import okx.Status as Status
    
    flag = "0"  # 实盘:0 , 模拟盘：1
    statusAPI = Status.StatusAPI(
        domain="https://openapi.okx.com",
        flag=flag,
    )
    
    # 获取系统升级事件的状态
    result = statusAPI.status()
    print(result)
    

#### 请求参数

#### 请求示例

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
state | String | 否 | 系统的状态  
`scheduled`：等待中  
`ongoing`：进行中  
`pre_open`：预开放  
`completed`：已完成  
`canceled`：已取消   
当维护时间过长，会存在预开放时间，一般持续10分钟左右。  
不填写此参数，默认返回 等待中、进行中和预开放 的数据  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "begin": "1672823400000",
                "end": "1672823520000",
                "href": "",
                "preOpenBegin": "",
                "scheDesc": "",
                "serviceType": "8",
                "state": "completed",
                "maintType": "1",
                "env": "1",
                "system": "unified",
                "title": "Trading account system upgrade (in batches of accounts)"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
title | String | 系统维护说明的标题  
state | String | 系统维护的状态  
begin | String | 系统维护的开始时间，Unix时间戳的毫秒数格式 如：`1617788463867`  
end | String | 交易全面开放的时间，Unix时间戳的毫秒数格式 如：`1617788463867`   
在维护完成前，是预期结束时间；维护完成后，会变更为实际结束时间。  
preOpenBegin | String | 预开放开始的时间，开放撤单、Post Only 下单和资金转入功能的时间  
href | String | 系统维护详情的超级链接,若无返回值，默认值为空，如 ""  
serviceType | String | 服务类型  
`0`：WebSocket  
`5`：交易服务  
`6`：大宗交易  
`7`：策略交易  
`8`：交易服务 (按账户分批次)  
`9`：交易服务 (按产品分批次)  
`10`：价差交易  
`11`：跟单交易  
`99`：其他（如：停止部分产品交易）  
system | String | 系统  
`unified`：交易账户  
scheDesc | String | 改期进度说明，如 `由 2021-01-26T16:30:00.000Z`改期到`2021-01-28T16:30:00.000Z`  
maintType | String | 维护类型  
`1`：计划维护  
`2`：临时维护  
`3`：系统故障  
env | String | 环境  
`1`：实盘  
`2`：模拟盘  
  
## WS / Status 频道 

获取系统维护的状态，当系统维护状态改变，改期，以及修改结束时间时推送。首次订阅：”推送最新一条的变化数据“；后续每次有状态变化，推送变化的内容。

由计划系统维护引起的短暂不可用（<5秒）和WebSocket闪断连接（用户可以立即重连）将不会公布。此类维护只会在市场波动性低的时期进行。

#### URL Path

/ws/v5/public

> 请求示例
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [{
            "channel": "status"
        }]
    }
    
    
    
    import asyncio
    from okx.websocket.WsPublicAsync import WsPublicAsync
    
    def callbackFunc(message):
        print(message)
    
    async def main():
        ws = WsPublicAsync(url="wss://wspap.okx.com:8443/ws/v5/public")
        await ws.start()
        args = [{
            "channel": "status"
        }]
    
        await ws.subscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
        await ws.unsubscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
    asyncio.run(main())
    
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
id | String | 否 | 消息的唯一标识。  
用户提供，返回参数中会返回以便于找到相应的请求。  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度必须要在1-32位之间。  
op | String | 是 | 操作  
`subscribe`  
`unsubscribe`  
args | Array of objects | 是 | 请求订阅的频道列表  
> channel | String | 是 | 频道名  
`status`  
  
> 成功返回示例
    
    
    {
        "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "status"
        },
        "connId": "a4d3ae55"
    }
    
    

> 失败返回示例
    
    
    {
        "id": "1512",
        "event": "error",
        "code": "60012",
        "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"statuss\"}]}",
        "connId": "a4d3ae55"
    }
    

#### 返回参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
id | String | 否 | 消息的唯一标识  
event | String | 是 | 事件  
`subscribe`  
`unsubscribe`  
`error`  
arg | Object | 否 | 订阅的频道  
> channel | String | 是 | 频道名  
`status`  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID  
  
> 推送示例
    
    
    {
        "arg": {
            "channel": "status"
        },
        "data": [
            {
                "begin": "1672823400000",
                "end": "1672825980000",
                "href": "",
                "preOpenBegin": "",
                "scheDesc": "",
                "serviceType": "0",
                "state": "completed",
                "system": "unified",
                "maintType": "1",
                "env": "1",
                "title": "Trading account WebSocket system upgrade",
                "ts": "1672826038470"
            }
        ]
    }
    

#### 推送数据参数

参数名 | 类型 | 描述  
---|---|---  
arg | Object | 订阅成功的频道  
> channel | String | 频道名  
`status`  
data | Array of objects | 订阅的数据  
> title | String | 系统维护说明的标题  
> state | String | 系统的状态，`scheduled`:等待中 ; `ongoing`:进行中 ; `pre_open`:预开放；`completed`:已完成 `canceled`: 已取消   
当维护时间过长，会存在预开放时间，一般持续10分钟左右。  
> begin | String | 系统维护的开始时间，Unix时间戳的毫秒数格式 如：`1617788463867`  
> end | String | 交易全面开放的时间，Unix时间戳的毫秒数格式 如：`1617788463867`   
在维护完成前，是预期结束时间；维护完成后，会变更为实际结束时间。  
> preOpenBegin | String | 预开放开始的时间，开放撤单、Post Only 下单和资金转入功能的时间  
> href | String | 系统维护详情的超级链接,若无返回值，默认值为空，如：“”  
> serviceType | String | 服务类型， `0`：WebSocket ; `5`：交易服务；`6`：大宗交易；`7`：策略交易；`8`：交易服务 (按账户分批次)；`9`：交易服务 (按产品分批次)；`10`：价差交易；`11`：跟单交易；`99`：其他（如：停止部分产品交易）  
> system | String | 系统，`unified`：交易账户  
> scheDesc | String | 改期进度说明，如： `由 2021-01-26T16:30:00.000Z 改期到 2021-01-28T16:30:00.000Z`  
> maintType | String | 维护类型。  
`1`：计划维护；`2`：临时维护；`3`：系统故障  
> env | String | 环境。  
`1`：实盘，`2`：模拟盘  
> ts | String | 事件变更的推送时间，Unix时间戳的毫秒数格式，如：`1617788463867`