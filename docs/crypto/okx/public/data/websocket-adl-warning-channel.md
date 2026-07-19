---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#public-data-websocket-adl-warning-channel
anchor_id: public-data-websocket-adl-warning-channel
api_type: WebSocket
updated_at: 2026-07-19 19:16:33.681244
---

# ADL warning channel

Auto-deleveraging warning channel.

Data is only pushed in the `warning` or `adl` state, once every second, displaying the security fund balance and related risk information. No data is pushed in the `normal` state.

For more ADL details, please refer to [Introduction to Auto-deleveraging](https://www.okx.com/help/iv-introduction-to-auto-deleveraging-adl)

#### URL Path

/ws/v5/public

> Request Example
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [{
            "channel": "adl-warning",
            "instType": "FUTURES",
            "instFamily": "BTC-USDT"
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
            "channel": "adl-warning",
            "instType": "FUTURES",
            "instFamily": "BTC-USDT"
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
`subscribe`  
`unsubscribe`  
  
args | Array of objects | Yes | List of subscribed channels  
> channel | String | Yes | Channel name  
`adl-warning`  
> instType | String | Yes | Instrument type  
`SWAP`  
`FUTURES`  
`OPTION`  
> instFamily | String | No | Instrument family  
  
> Successful Response Example
    
    
    {
       "id": "1512",
       "event":"subscribe",
       "arg":{
          "channel":"adl-warning",
          "instType":"FUTURES",
          "instFamily":"BTC-USDT"
       },
       "connId":"48d8960a"
    }
    
    

> Failure Response Example
    
    
    {
       "id": "1512",
       "event":"error",
       "msg":"Illegal request: { \"event\": \"subscribe\", \"arg\": { \"channel\": \"adl-warning\", \"instType\": \"FUTURES\", \"instFamily\": \"BTC-USDT\" } }",
       "code":"60012",
       "connId":"48d8960a"
    }
    
    

#### Response parameters

Parameter | Type | Required | Description  
---|---|---|---  
id | String | No | Unique identifier of the message  
event | String | Yes | Event  
`subscribe`  
`unsubscribe`  
`error`  
arg | Object | No | Subscribed channel  
> channel | String | Yes | Channel name  
`adl-warning`  
> instType | String | Yes | Instrument type  
> instFamily | String | No | Instrument family  
code | String | No | Error code  
msg | String | No | Error message  
connId | String | Yes | WebSocket connection ID  
  
> Push Data Example
    
    
    {
       "arg":{
          "channel":"adl-warning",
          "instType":"FUTURES",
          "instFamily":"BTC-USDT"
       },
       "data":[
          {
             "instType":"FUTURES",
             "instFamily":"BTC-USDT",
             "state":"warning",
             "bal":"280784384.9564228289548144",
             "ccy":"",
             "maxBal":"",
             "maxBalTs":"",
             "adlType":"",
             "adlBal":"",
             "adlRecBal":"",
             "ts":"1700210763001",
             "decRate":"",
             "adlRate":"",
             "adlRecRate":""
          }
       ]
    }
    
    

#### Push data parameters

Parameter | Type | Description  
---|---|---  
arg | Object | Subscribed channel  
> channel | String | Channel name  
`adl-warning`  
> instType | String | Instrument type  
> instFamily | String | Instrument family  
data | Array of objects | Subscribed data  
> instType | String | Instrument type  
> instFamily | String | Instrument family  
> state | String | state   
`warning`   
`adl`  
> bal | String | Real-time security fund balance  
> ccy | String | ~~The corresponding currency of security fund balance~~(Deprecated, returns `""`. To be removed in a future update)  
> maxBal | String | ~~Maximum security fund balance in the past eight hours  
  
Applicable when state is `warning` or `adl`~~(Deprecated, returns `""`. To be removed in a future update)  
> maxBalTs | String | ~~Timestamp when security fund balance reached maximum in the past eight hours, Unix timestamp format in milliseconds, e.g.`1597026383085`~~(Deprecated, returns `""`. To be removed in a future update)  
> adlType | String | ~~ADL related events  
`rate_adl_start`: ADL begins due to high security fund decline rate   
`bal_adl_start`: ADL begins due to security fund balance falling   
`pos_adl_start`：ADL begins due to the volume of liquidation orders falls to a certain level (only applicable to premarket symbols)   
`adl_end`: ADL ends~~(Deprecated, returns `""`. To be removed in a future update)  
> adlBal | String | ~~security fund balance that triggers ADL~~(Deprecated, returns `""`. To be removed in a future update)  
> adlRecBal | String | ~~security fund balance that turns off ADL~~(Deprecated, returns `""`. To be removed in a future update)  
> ts | String | Data push time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
> decRate | String | ~~Real-time security fund decline rate (compare bal and maxBal)  
  
Applicable when state is `warning` or `adl`~~(Deprecated)  
> adlRate | String | ~~security fund decline rate that triggers ADL~~(Deprecated)  
> adlRecRate | String | ~~security fund decline rate that turns off ADL~~(Deprecated)

---

# 自动减仓预警频道

自动减仓预警。

仅在 `warning` 或 `adl` 状态下推送数据，每1秒推送一次，展示风险保证金余额及相关风险信息。`normal` 状态下不再推送数据。

更多自动减仓细节，请见[自动减仓机制介绍](https://www.okx.com/cn/help/iv-introduction-to-auto-deleveraging-adl)

#### 服务地址

/ws/v5/public

> 请求示例
    
    
    {
       "id": "1512",
        "op": "subscribe",
        "args": [{
            "channel": "adl-warning",
            "instType": "FUTURES",
            "instFamily": "BTC-USDT"
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
            "channel": "adl-warning",
            "instType": "FUTURES",
            "instFamily": "BTC-USDT"
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
`adl-warning`  
> instType | String | 是 | 产品类型  
`FUTURES`：交割合约  
`SWAP`：永续合约  
`OPTION`：期权  
> instFamily | String | 否 | 交易品种  
  
> 成功返回示例
    
    
    {
       "id": "1512",
       "event":"subscribe",
       "arg":{
          "channel":"adl-warning",
          "instType":"FUTURES",
          "instFamily":"BTC-USDT"
       },
       "connId":"48d8960a"
    }
    
    

> 失败返回示例
    
    
    {
       "id": "1512",
       "event":"error",
       "msg":"Illegal request: { \"event\": \"subscribe\", \"arg\": { \"channel\": \"adl-warning\", \"instType\": \"FUTURES\", \"instFamily\": \"BTC-USDT\" } }",
       "code":"60012",
       "connId":"48d8960a"
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
`adl-warning`  
> instType | String | 是 | 产品类型  
> instFamily | String | 否 | 交易品种  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID  
  
> 推送示例
    
    
    {
       "arg":{
          "channel":"adl-warning",
          "instType":"FUTURES",
          "instFamily":"BTC-USDT"
       },
       "data":[
          {
             "instType":"FUTURES",
             "instFamily":"BTC-USDT",
             "state":"warning",
             "bal":"280784384.9564228289548144",
             "ccy":"",
             "maxBal":"",
             "maxBalTs":"",
             "adlType":"",
             "adlBal":"",
             "adlRecBal":"",
             "ts":"1700210763001",
             "decRate":"",
             "adlRate":"",
             "adlRecRate":""
          }
       ]
    }
    
    

#### 推送数据参数

参数名 | 类型 | 描述  
---|---|---  
arg | Object | 请求订阅的频道  
> channel | String | 频道名  
`adl-warning`  
> instType | String | 产品类型  
> instFamily | String | 交易品种  
data | Array of objects | 订阅的数据  
> instType | String | 产品类型  
> instFamily | String | 交易品种  
> state | String | 状态   
`warning`：预警状态   
`adl`：已开启自动减仓  
> bal | String | 实时风险保证金余额  
> ccy | String | ~~风险保证金余额对应币种~~ （已弃用，返回 `""`。将在后续更新中删除）  
> maxBal | String | ~~过去八小时内的风险保证金余额最大值  
仅在状态为`warning`及`adl`时推送，状态为`normal`时推送空字符串""~~（已弃用，返回 `""`。将在后续更新中删除）  
> maxBalTs | String | ~~过去八小时内风险保证金余额最大值对应的时间戳，Unix时间戳的毫秒数格式，如`1597026383085`~~（已弃用，返回 `""`。将在后续更新中删除）  
> adlType | String | ~~关于自动减仓的事件  
`rate_adl_start`：由于风险保证金下降率过高造成的自动减仓开始   
`bal_adl_start`：由于风险保证金余额下降过高造成的自动减仓开始   
`pos_adl_start`：由于强平单的规模积累到一定程度的自动减仓开始（仅适用于盘前交易市场）   
`adl_end`：自动减仓结束~~（已弃用，返回 `""`。将在后续更新中删除）  
> adlBal | String | ~~触发自动减仓的风险保证金余额~~ （已弃用，返回 `""`。将在后续更新中删除）  
> adlRecBal | String | ~~自动减仓结束的风险保证金余额~~ （已弃用，返回 `""`。将在后续更新中删除）  
> ts | String | 数据更新时间，Unix时间戳的毫秒数格式，如 1597026383085  
> decRate | String | ~~风险保证金实时下降率（bal与maxBal相比较）  
仅在状态为`warning`及`adl`时推送，状态为`normal`时推送空字符串""~~（已弃用）  
> adlRate | String | ~~触发自动减仓的风险保证金下降率~~ （已弃用）  
> adlRecRate | String | ~~自动减仓结束的风险保证金下降率~~ （已弃用）