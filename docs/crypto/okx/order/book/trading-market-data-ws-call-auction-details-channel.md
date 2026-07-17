---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-market-data-ws-call-auction-details-channel
anchor_id: order-book-trading-market-data-ws-call-auction-details-channel
api_type: WebSocket
updated_at: 2026-07-17 19:16:56.410886
---

# WS / Call auction details channel

Retrieve call auction details.

#### URL Path

/ws/v5/public

> Request Example
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [{
            "channel": "call-auction-details",
            "instId": "ONDO-USDC"
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
            "channel": "call-auction-details",
            "instId": "ONDO-USDC"
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
`call-auction-details`  
> instId | String | Yes | Instrument ID  
  
> Successful Response Example
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
          "channel": "call-auction-details",
          "instId": "ONDO-USDC"
        },
      "connId": "a4d3ae55"
    }
    
    

> Failure Response Example
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"call-auction-details\", \"instId\" : \"BTC-USD-191227\"}]}",
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
> channel | String | yes | channel name  
> instId | String | Yes | Instrument ID  
code | String | No | Error code  
msg | String | No | Error message  
connId | String | Yes | WebSocket connection ID  
  
> Push Data Example
    
    
    {
      "arg": {
        "channel": "call-auction-details",
        "instId": "ONDO-USDC"
      },
      "data": [
            {
                "instId": "ONDO-USDC",
                "unmatchedSz": "9988764",
                "eqPx": "0.6",
                "matchedSz": "44978",
                "state": "continuous_trading",
                "auctionEndTime": "1726542000000",
                "ts": "1726542000007"
            }
      ]
    }
    
    

#### Push data parameters

**Parameter** | **Type** | **Description**  
---|---|---  
arg | Object | Successfully subscribed channel  
> channel | String | Channel name  
> instId | String | Instrument ID  
data | Array of objects | Subscribed data  
> instId | String | Instrument ID  
> eqPx | String | Equilibrium price  
> matchedSz | String | Matched size for both buy and sell  
The unit is in base currency  
> unmatchedSz | String | Unmatched size  
> auctionEndTime | String | Call auction end time. Unix timestamp in milliseconds.  
> state | String | Trading state of the symbol  
`call_auction`  
`continuous_trading`  
> ts | String | Data generation time. Unix timestamp in millieseconds.  
During call auction, users can get the updates of equilibrium price, matched size, unmatched size, and auction end time. The data will be updated around once a second. When call auction ends, this channel will push the last message, returning the actual open price, matched size, and unmatched size, with trading state as `continuous_trading`.

---

# WS / 集合竞价信息频道

获取集合竞价相关信息

#### URL Path

/ws/v5/public

> 请求示例
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [{
            "channel": "call-auction-details",
            "instId": "ONDO-USDC"
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
            "channel": "call-auction-details",
            "instId": "ONDO-USDC"
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
`call-auction-details`  
> instId | String | 是 | 产品ID  
  
> 成功返回示例
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
          "channel": "call-auction-details",
          "instId": "ONDO-USDC"
        },
      "connId": "a4d3ae55"
    }
    
    

> 失败返回示例
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"call-auction-details\", \"instId\" : \"BTC-USD-191227\"}]}",
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
> instId | String | 是 | 产品ID  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID  
  
> 推送示例
    
    
    {
      "arg": {
        "channel": "call-auction-details",
        "instId": "ONDO-USDC"
      },
      "data": [
            {
                "instId": "ONDO-USDC",
                "unmatchedSz": "9988764",
                "eqPx": "0.6",
                "matchedSz": "44978",
                "state": "continuous_trading",
                "auctionEndTime": "1726542000000",
                "ts": "1726542000007"
            }
      ]
    }
    
    

#### 推送数据参数

参数名 | 类型 | 描述  
---|---|---  
arg | Object | 订阅成功的频道  
> channel | String | 频道名  
> instId | String | 产品ID  
data | Array of objects | 订阅的数据  
> instId | String | 产品ID  
> eqPx | String | 均衡价格  
> matchedSz | String | 买卖双边的匹配数量，单位为交易货币  
> unmatchedSz | String | 未匹配数量  
> auctionEndTime | String | 集合竞价结束时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
> state | String | 交易状态  
`call_auction`：集合竞价  
`continuous_trading`：连续交易  
> ts | String | 数据产生时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
在集合竞价期间，用户可以获取均衡价格、匹配数量、未匹配数量和集合竞价结束时间的更新。数据大约每秒更新一次。当集合竞价结束时，该频道将推送最后一条消息，返回实际开盘价、匹配数量和未匹配数量，交易状态state为`continuous_trading`。