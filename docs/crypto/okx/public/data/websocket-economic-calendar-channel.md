---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#public-data-websocket-economic-calendar-channel
anchor_id: public-data-websocket-economic-calendar-channel
api_type: WebSocket
updated_at: 2026-07-06 19:54:15.689673
---

# Economic calendar channel

This endpoint is only supported in production environment.   
  
Retrieve the most up-to-date economic calendar data. This endpoint is only applicable to VIP 1 and above users in the trading fee tier.

#### URL Path

/ws/v5/business (required login)

> Request Example
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [
          {
              "channel": "economic-calendar"
          }
        ]
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
            url = "wss://ws.okx.com:8443/ws/v5/business",
            useServerTime=False
        )
        await ws.start()
        args = [
          {
              "channel": "economic-calendar"
          }
        ]
    
        await ws.subscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
        await ws.unsubscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
    
    asyncio.run(main())
    
    

#### Request parameters

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
`economic-calendar`  
  
> Successful Response Example
    
    
    {
        "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "economic-calendar"
        },
        "connId": "a4d3ae55"
    }
    
    

> Failure Response Example
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"economic-calendar\", \"instId\" : \"LTC-USD-190628\"}]}",
      "connId": "a4d3ae55"
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
code | String | No | Error code  
msg | String | No | Error message  
connId | String | Yes | WebSocket connection ID  
  
> Push Data Example
    
    
    {
        "arg": {
            "channel": "economic-calendar"
        },
        "data": [
            {
                "calendarId": "319275",
                "date": "1597026383085",
                "region": "United States",
                "category": "Manufacturing PMI",
                "event": "S&P Global Manufacturing PMI Final",
                "refDate": "1597026383085",
                "actual": "49.2",
                "previous": "47.3",
                "forecast": "49.3",
                "importance": "2",
                "prevInitial": "",
                "ccy": "",
                "unit": "",
                "ts": "1698648096590"
            }
        ]
    }
    

#### Push data parameters

Parameter | Type | Description  
---|---|---  
arg | Object | Successfully subscribed channel  
> channel | String | Channel name  
`economic-calendar`  
data | Array of objects | Subscribed data  
> event | string | Event name  
> region | string | Country, region or entity  
> category | string | Category name  
> actual | string | The actual value of this event  
> previous | string | Latest actual value of the previous period   
The value will be revised if revision is applicable  
> forecast | string | Average forecast among a representative group of economists  
> prevInitial | string | The initial value of the previous period   
Only applicable when revision happens  
> date | string | Estimated release time of the value of actual field, millisecond format of Unix timestamp, e.g. `1597026383085`  
> refDate | string | Date for which the datapoint refers to  
> calendarId | string | Calendar ID  
> unit | string | Unit of the data  
> ccy | string | Currency of the data  
> importance | string | Level of importance  
`1`: low   
`2`: medium   
`3`: high  
> ts | string | The time of the latest update

---

# 经济日历频道

仅支持实盘服务   
  
获取最新经济日历数据。 该频道仅开放给交易费等级VIP1及以上的用户。

#### 服务地址

/ws/v5/business (需要登录)

> 请求示例
    
    
    {
        "id": "1512"  
        "op": "subscribe",
        "args": [
          {
              "channel": "economic-calendar"
          }
        ]
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
            url = "wss://ws.okx.com:8443/ws/v5/business",
            useServerTime=False
        )
        await ws.start()
        args = [
          {
              "channel": "economic-calendar"
          }
        ]
    
        await ws.subscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
        await ws.unsubscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
    
    asyncio.run(main())
    
    

#### 请求参数

参数名 | 类型 | 是否必填 | 描述  
---|---|---|---  
id | String | 否 | 消息的唯一标识。  
用户提供，返回参数中会返回以便于找到相应的请求。  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度必须要在1-32位之间。  
op | String | 是 | 操作  
`subscribe`  
`unsubscribe`  
  
args | Array of objects | 是 | 请求订阅的频道列表  
> channel | String | 是 | 频道名  
`economic-calendar`  
  
> 成功返回示例
    
    
    {
        "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "economic-calendar"
        },
        "connId": "a4d3ae55"
    }
    
    

> 失败返回示例
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"economic-calendar\", \"instId\" : \"LTC-USD-190628\"}]}",
      "connId": "a4d3ae55"
    }
    
    

#### 返回参数

参数名 | 类型 | 是否必填 | 描述  
---|---|---|---  
id | String | 否 | 消息的唯一标识  
event | String | 是 | 操作  
`subscribe`  
`unsubscribe`  
`error`  
arg | Object | 否 | 订阅的频道  
> channel | String | 是 | 频道名  
`economic-calendar`  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID  
  
> 推送示例
    
    
    {
        "arg": {
            "channel": "economic-calendar"
        },
        "data": [
            {
                "calendarId": "319275",
                "date": "1597026383085",
                "region": "United States",
                "category": "Manufacturing PMI",
                "event": "S&P Global Manufacturing PMI Final",
                "refDate": "1597026383085",
                "actual": "49.2",
                "previous": "47.3",
                "forecast": "49.3",
                "importance": "2",
                "prevInitial": "",
                "ccy": "",
                "unit": "",
                "ts": "1698648096590"
            }
        ]
    }
    

#### 推送数据参数

**参数名** | **类型** | **描述**  
---|---|---  
arg | Object | 订阅成功的频道  
> channel | String | 频道名  
data | Array of objects | 订阅的数据  
> event | string | 事件名  
> region | string | 国家，地区或实体  
> category | string | 类别名  
> actual | string | 事件实际值  
> previous | string | 当前事件上个周期的最新实际值   
若发生数据修正，该字段存储上个周期修正后的实际值  
> forecast | string | 由权威经济学家共同得出的预测值  
> prevInitial | string | 该事件上一周期的初始值   
仅在修正发生时有值  
> date | string | actual字段值的预期发布时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
> refDate | string | 当前事件指向的日期  
> calendarId | string | 经济日历ID  
> unit | string | 事件实际值对应的单位  
> ccy | string | 事件实际值对应的货币  
> importance | string | 重要性   
`1`: 低   
`2`: 中等   
`3`: 高  
> ts | string | 推送时间