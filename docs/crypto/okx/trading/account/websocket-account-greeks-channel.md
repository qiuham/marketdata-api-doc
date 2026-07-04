---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#trading-account-websocket-account-greeks-channel
anchor_id: trading-account-websocket-account-greeks-channel
api_type: WebSocket
updated_at: 2026-07-04 19:37:25.957941
---

# Account greeks channel

Retrieve account greeks information. Data will be pushed when triggered by events such as increase/decrease positions or cash balance in account, and will also be pushed in regular interval according to subscription granularity.  
Concurrent connection to this channel will be restricted by the following rules: [WebSocket connection count limit](/docs-v5/en/#overview-websocket-connection-count-limit).

#### URL Path

/ws/v5/private (required login)

> Request Example
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [{
            "channel": "account-greeks"
        }]
    }
    
    
    
    import asyncio
    
    from okx.websocket.WsPrivateAsync import WsPrivateAsync
    
    
    def callbackFunc(message):
        print(message)
    
    async def main():
    
        ws = WsPrivateAsync(
            apiKey = "YOUR_API_KEY",
            passphrase = "YOUR_PASSPHRASE",
            secretKey = "YOUR_SECRET_KEY",
            url = "wss://ws.okx.com:8443/ws/v5/private",
            useServerTime=False
        )
        await ws.start()
        args = [{
            "channel": "account-greeks"
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
op | String | Yes | Operation  
`subscribe` `unsubscribe`  
args | Array of objects | Yes | List of subscribed channels  
> channel | String | Yes | Channel name  
`account-greeks`  
> ccy | String | No | Settlement currency  
When the user specifies a settlement currency, event push will only be triggered when the position of the same settlement currency changes. For example, when ccy=BTC, if the position of `BTC-USDT-SWAP` changes, no event push will be triggered.  
  
> Successful Response Example
    
    
    {
        "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "account-greeks"
        },
      "connId": "a4d3ae55"
    }
    

> Failure Response Example
    
    
    {
        "id": "1512",
        "event": "error",
        "code": "60012",
        "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"account-greeks\", \"ccy\" : \"BTC\"}]}",
      "connId": "a4d3ae55"
    }
    

#### Response parameters

Parameter | Type | Required | Description  
---|---|---|---  
id | String | No | Unique identifier of the message  
event | String | Yes | Operation  
`subscribe`  
`unsubscribe`  
`error`  
arg | Object | No | Subscribed channel  
> channel | String | Yes | Channel name,`account-greeks`  
> ccy | String | No | Settlement currency  
code | String | No | Error code  
msg | String | No | Error message  
connId | String | Yes | WebSocket connection ID  
  
> Push Data Example: single
    
    
    {
        "arg": {
            "channel": "account-greeks",
            "ccy": "BTC",
            "uid": "614488474791936"
        },
        "data": [
            {
                "ccy": "BTC",
                "deltaBS": "1.1246665401944310",
                "deltaPA": "-0.0074076183688949",
                "gammaBS": "0.0000000000000000",
                "gammaPA": "0.0148152367377899",
                "thetaBS": "2.0356991946421226",
                "thetaPA": "-0.0000000200174309",
                "ts": "1729179082006",
                "vegaBS": "0.0000000000000000",
                "vegaPA": "0.0000000000000000"
            }
        ]
    }
    

> Push Data Example
    
    
    {
        "arg": {
            "channel": "account-greeks",
            "uid": "614488474791936"
        },
        "data": [
            {
                "ccy": "BTC",
                "deltaBS": "1.1246665403011684",
                "deltaPA": "-0.0074021163991037",
                "gammaBS": "0.0000000000000000",
                "gammaPA": "0.0148042327982075",
                "thetaBS": "2.1342098201092528",
                "thetaPA": "-0.0000000200876441",
                "ts": "1729179001692",
                "vegaBS": "0.0000000000000000",
                "vegaPA": "0.0000000000000000"
            },
            {
                "ccy": "ETH",
                "deltaBS": "0.3810670161698570",
                "deltaPA": "-0.0688347042402955",
                "gammaBS": "-0.0000000000230396",
                "gammaPA": "0.1376693483440320",
                "thetaBS": "0.3314776517141782",
                "thetaPA": "0.0000000001316008",
                "ts": "1729179001692",
                "vegaBS": "-0.0000000045069794",
                "vegaPA": "-0.0000000000017267"
            }
        ]
    }
    

#### Push data parameters

**Parameters** | **Types** | **Description**  
---|---|---  
arg | Object | Successfully subscribed channel  
> channel | String | Channel name  
> uid | String | User Identifier  
data | Array of objects | Subscribed data  
> deltaBS | String | delta: Black-Scholes Greeks in dollars  
> deltaPA | String | delta: Greeks in coins  
> gammaBS | String | gamma: Black-Scholes Greeks in dollars, only applicable to OPTION cross  
> gammaPA | String | gamma: Greeks in coins, only applicable to OPTION cross  
> thetaBS | String | theta: Black-Scholes Greeks in dollars, only applicable to OPTION cross  
> thetaPA | String | theta: Greeks in coins, only applicable to OPTION cross  
> vegaBS | String | vega: Black-Scholes Greeks in dollars, only applicable to OPTION cross  
> vegaPA | String | vega: Greeks in coins, only applicable to OPTION cross  
> ccy | String | Currency  
> ts | String | Push time of account greeks, Unix timestamp format in milliseconds, e.g. 1597026383085  
The account greeks data is sent on event basis and regular basis   
\- The event push is not pushed in real-time. It is aggregated and pushed at a fixed time interval, around 50ms. For example, if multiple events occur within a fixed time interval, the system will aggregate them into a single message and push it at the end of the fixed time interval. If the data volume is too large, it may be split into multiple messages.   
\- When the user specifies a settlement currency in the subscribe request, event push will only be triggered when the position of the same settlement currency changes. For example, when subscribe `ccy`=BTC, if the position of `BTC-USDT-SWAP` changes, no event push will be triggered.   
\- The regular push sends updates regardless of whether there are activities or not.    
\- Only currencies in the account will be pushed. If the data is too large to be sent in a single push message, it will be split into multiple messages.   
\- For example, when subscribing to account-greeks channel without specifying ccy and there are 5 currencies are with non-zero balance, all 5 currencies data will be pushed in initial snapshot and in regular interval. Subsequently when there is change in balance or equity of an token, only the incremental data of that currency will be pushed triggered by this change.

---

# 账户greeks频道

获取账户资产的greeks信息。当增加或者减少币种余额、持仓数量等会触发事件推送，周期性的也会有定时推送。  
该频道的并发连接受到如下规则限制：[WebSocket 连接限制](/docs-v5/zh/#overview-websocket-connection-count-limit)

#### 服务地址

/ws/v5/private (需要登录)

> 请求示例
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [{
            "channel": "account-greeks"
        }]
    }
    
    
    
    import asyncio
    
    from okx.websocket.WsPrivateAsync import WsPrivateAsync
    
    
    def callbackFunc(message):
        print(message)
    
    async def main():
    
        ws = WsPrivateAsync(
            apiKey = "YOUR_API_KEY",
            passphrase = "YOUR_PASSPHRASE",
            secretKey = "YOUR_SECRET_KEY",
            url = "wss://ws.okx.com:8443/ws/v5/private",
            useServerTime=False
        )
        await ws.start()
        args = [{
            "channel": "account-greeks"
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
`account-greeks`  
> ccy | String | 否 | 保证金币种  
当用户指定了保证金，只有作为保证金的仓位发生变化的时候，才会触发事件推送。例如当指定了ccy = `BTC`，如果 `BTC-USDT-SWAP` 仓位发生变化，不会触发事件推送。  
  
> 成功返回示例
    
    
    {
        "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "account-greeks"
        },
      "connId": "a4d3ae55"
    }
    

> 失败返回示例
    
    
    {
        "id": "1512",
        "event": "error",
        "code": "60012",
        "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"account-greeks\", \"ccy\" : \"BTC\"}]}",
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
`account-greeks`  
> ccy | String | 否 | 保证金币种  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID  
  
> 推送示例：单个
    
    
    {
        "arg": {
            "channel": "account-greeks",
            "ccy": "BTC",
            "uid": "614488474791936"
        },
        "data": [
            {
                "ccy": "BTC",
                "deltaBS": "1.1246665401944310",
                "deltaPA": "-0.0074076183688949",
                "gammaBS": "0.0000000000000000",
                "gammaPA": "0.0148152367377899",
                "thetaBS": "2.0356991946421226",
                "thetaPA": "-0.0000000200174309",
                "ts": "1729179082006",
                "vegaBS": "0.0000000000000000",
                "vegaPA": "0.0000000000000000"
            }
        ]
    }
    

> 推送示例
    
    
    {
        "arg": {
            "channel": "account-greeks",
            "uid": "614488474791936"
        },
        "data": [
            {
                "ccy": "BTC",
                "deltaBS": "1.1246665403011684",
                "deltaPA": "-0.0074021163991037",
                "gammaBS": "0.0000000000000000",
                "gammaPA": "0.0148042327982075",
                "thetaBS": "2.1342098201092528",
                "thetaPA": "-0.0000000200876441",
                "ts": "1729179001692",
                "vegaBS": "0.0000000000000000",
                "vegaPA": "0.0000000000000000"
            },
            {
                "ccy": "ETH",
                "deltaBS": "0.3810670161698570",
                "deltaPA": "-0.0688347042402955",
                "gammaBS": "-0.0000000000230396",
                "gammaPA": "0.1376693483440320",
                "thetaBS": "0.3314776517141782",
                "thetaPA": "0.0000000001316008",
                "ts": "1729179001692",
                "vegaBS": "-0.0000000045069794",
                "vegaPA": "-0.0000000000017267"
            }
        ]
    }
    

#### 推送数据参数

**参数名** | **类型** | **描述**  
---|---|---  
arg | Object | 请求订阅的频道  
> channel | String | 频道名  
> uid | String | 用户标识  
data | Array of objects | 订阅的数据  
> deltaBS | String | 美金本位账户资产delta  
> deltaPA | String | 币本位账户资产delta  
> gammaBS | String | 美金本位账户资产gamma，仅适用于期权全仓  
> gammaPA | String | 币本位账户资产gamma，仅适用于期权全仓  
> thetaBS | String | 美金本位账户资产theta，仅适用于期权全仓  
> thetaPA | String | 币本位账户资产theta，仅适用于期权全仓  
> vegaBS | String | 美金本位账户资产vega，仅适用于期权全仓  
> vegaPA | String | 币本位账户资产vega，仅适用于期权全仓  
> ccy | String | 币种  
> ts | String | 获取greeks的时间，Unix时间戳的毫秒数格式，如 1597026383085  
账户greeks频道基于事件推送，并进行定时推送  
\- greeks频道的事件推送并非在事件发生时实时进行，而是按照大约50毫秒的固定时间窗口进行聚合推送。例如，在固定时间窗口内发生多个事件，系统将尽量聚合为一条消息并在固定时间窗口结束时进行推送。在数据量过大的情况下可能拆分为多条消息。   
\- 当用户订阅时指定了保证金币种(ccy)，只有作为保证金的仓位发生变化的时候，才会触发事件推送。例如订阅时指定了ccy=`BTC`，如果`BTC-USDT-SWAP`仓位发生变化，不会触发事件推送。   
\- 无论是否有greeks数据的变化，定时推送都会发送更新。    
\- 只推账户资产不为0的greeks数据。如果数据太大无法在单个推送消息中发送，它将被分成多个消息发送。   
\- 例：按照所有币种订阅且有5个币种资产都不为0，首次和定时推全部5个；账户的某个币种资产改变，那么账户greeks变更的触发只推这一个。