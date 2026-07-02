---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#block-trading-websocket-private-channel-quotes-channel
anchor_id: block-trading-websocket-private-channel-quotes-channel
api_type: WebSocket
updated_at: 2026-07-02 19:44:12.947344
---

# Quotes channel

Retrieve the Quotes sent or received by the user. Data will be pushed whenever the user sends or receives a Quote.

#### URL Path

/ws/v5/business (required login)

> Request Example
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "quotes"
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
              "channel": "quotes"
            }
        ]
    
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
`quotes`  
  
> Successful Response Example
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "quotes"
      },
      "connId": "a4d3ae55"
    }
    

> Failure Response Example
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"quotes\"}]}",
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
> channel | String | Yes | Channel name  
`quotes`  
code | String | No | Error code  
msg | String | No | Error message  
connId | String | Yes | WebSocket connection ID  
  
> Push Data Example
    
    
    {
        "arg":{
            "channel":"quotes",
            "uid": "77982378738415879"
        },
        "data":[
            {
                "validUntil":"1608997227854",
                "uTime":"1608267227834",
                "cTime":"1608267227834",
                "legs":[
                    {
                        "px":"0.0023",
                        "sz":"25.0",
                        "instId":"BTC-USD-220114-25000-C",
                        "tdMode":"cross",
                        "ccy":"USDT",
                        "side":"sell",
                        "posSide": "long",
                        "tgtCcy":""
    
                    },
                    {
                        "px":"0.0045",
                        "sz":"25",
                        "instId":"BTC-USD-220114-35000-C",
                        "tdMode":"cross",
                        "ccy":"USDT",
                        "side":"buy",
                        "posSide": "long",
                        "tgtCcy":""
    
                    }
                ],
                "quoteId":"25092",
                "rfqId":"18753",
                "tag":"123456",
                "traderCode":"SATS",
                "quoteSide":"sell",
                "state":"canceled",
                "reason":"mmp_canceled",
                "clQuoteId":""
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
> cTime | String | The timestamp the Quote was created, Unix timestamp format in milliseconds.  
> uTime | String | The timestamp the Quote was updated latest, Unix timestamp format in milliseconds.  
> state | String | The status of the quote. Valid values can be `active` `canceled` `filled` `expired` or `failed`.  
> reason | String | Reasons of state. Valid values can be mmp_canceled.  
> validUntil | String | The timestamp the Quote expires. Unix timestamp format in milliseconds.  
> rfqId | String | RFQ ID.  
> clRfqId | String | Client-supplied RFQ ID. This attribute is treated as client sensitive information. It will not be exposed to the Maker, just return empty string "" for Maker.  
> quoteId | String | Quote ID  
> clQuoteId | String | Client-supplied Quote ID. This attribute is treated as client sensitive information. It will not be exposed to the Taker, just return empty string "" for Taker.  
> tag | String | Quote tag. The block trade associated with the Quote will have the same tag.  
> traderCode | String | A unique identifier of maker. Empty If anonymous mode of Quote is `True`.  
> quoteSide | String | Top level side of Quote. Its value can be buy or sell.  
> legs | Array of objects | The legs of the Quote.  
>> instId | String | The instrument name of quoted leg.  
>> tdMode | String | Trade mode   
Margin mode: `cross` `isolated`   
Non-Margin mode: `cash`.   
If not provided, tdMode will inherit default values set by the system shown below:   
Futures mode & SPOT: `cash`   
Buy options in Futures mode and Multi-currency Margin: `isolated`   
Other cases: `cross`  
>> ccy | String | Margin currency.   
Only applicable to `cross` `MARGIN` orders in `Futures mode`. The parameter will be ignored in other scenarios.  
>> sz | String | The size of the quoted leg in contracts or spot.  
>> px | String | The price of the leg.  
>> side | String | The direction of the leg. Valid values can be buy or sell.  
>> posSide | String | Position side.   
The default is `net` in the net mode. If not specified, return "", which is equivalent to net.   
It can only be `long` or `short` in the long/short mode. If not specified, return "", which corresponds to the direction that opens new positions for the trade (buy => long, sell => short).   
Only applicable to `FUTURES`/`SWAP`.  
>> tgtCcy | String | Defines the unit of the “sz” attribute.   
Only applicable to instType = SPOT.   
The valid enumerations are `base_ccy` and `quote_ccy`. When not specified this is equal to `base_ccy` by default.  
>> tradeQuoteCcy | String | The quote currency used for trading. Only applicable to SPOT.   
The default value is the quote currency of the instId, for example: for `BTC-USD`, the default is `USD`.

---

# 报价频道

获取用户自身发送或接收的报价信息。每当用户自身发送或接收报价时，数据都将被推送。

#### 服务地址

/ws/v5/business (需要登录)

> 请求示例
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "quotes"
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
              "channel": "quotes"
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
`quotes`  
  
> 成功返回示例
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "quotes"
      },
      "connId": "a4d3ae55"
    }
    

> 失败返回示例
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"quotes\"}]}",
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
`quotes`  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID  
  
> 推送示例
    
    
    {
        "arg":{
            "channel":"quotes",
            "uid": "77982378738415879"
        },
        "data":[
            {
                "validUntil":"1608997227854",
                "uTime":"1608267227834",
                "cTime":"1608267227834",
                "legs":[
                    {
                        "px":"0.0023",
                        "sz":"25.0",
                        "instId":"BTC-USD-220114-25000-C",
                        "tdMode":"cross",
                        "ccy":"USDT",
                        "side":"sell",
                        "posSide": "long",
                        "tgtCcy":""
    
                    },
                    {
                        "px":"0.0045",
                        "sz":"25",
                        "instId":"BTC-USD-220114-35000-C",
                        "tdMode":"cross",
                        "ccy":"USDT",
                        "side":"buy",
                        "posSide": "long",
                        "tgtCcy":""
    
                    }
                ],
                "quoteId":"25092",
                "rfqId":"18753",
                "tag":"123456",
                "traderCode":"SATS",
                "quoteSide":"sell",
                "state":"canceled",
                "reason":"mmp_canceled",
                "clQuoteId":""
            }
        ]
    }
    

#### 推送数据参数

**参数名** | **类型** | **描述**  
---|---|---  
arg | Object | 订阅成功的频道  
> channel | String | 频道名  
> uid | String | 账户ID，账户uid和app上的一致  
data | Array of objects | 订阅的数据  
> cTime | String | 报价单创建时间，Unix时间戳的毫秒数格式。  
> uTime | String | 报价单状态更新时间，Unix时间戳的毫秒数格式。  
> state | String | 报价单的状态  
`active`  
`canceled`  
`filled`  
`expired`  
`failed`  
> reason | String | 状态原因  
`mmp_canceled`  
> validUntil | String | 报价单的过期时间，Unix时间戳的毫秒数格式。  
> rfqId | String | 询价单ID  
> clRfqId | String | 询价单自定义ID，为客户敏感信息，不会公开，对报价方返回""。  
> quoteId | String | 报价单ID  
> clQuoteId | String | 报价单自定义ID，为客户敏感信息，不会公开，对询价方返回""。  
> tag | String | 报价单标签，与此报价单关联的大宗交易将有相同的标签。  
> traderCode | String | 报价方唯一标识代码，报价时 Anonymous 设置为 `True` 时不可见。  
> quoteSide | String | 报价单方向  
`buy`  
`sell`  
当报价单方向为`buy`，对maker来说，执行方向与legs里的方向相同，对taker来说相反。反之同理。  
> legs | Array of objects | 组合交易  
>> instId | String | 产品ID  
>> tdMode | String | 交易模式  
保证金模式 `cross`：全仓 `isolated`：逐仓   
非保证金模式 `cash`：非保证金  
如未提供，tdMode 将继承系统设置的默认值：   
合约模式 & 现货模式: `cash`   
合约模式和跨币种保证金模式下买入期权： `isolated`   
其他情况: `cross`  
>> ccy | String | 保证金币种，仅适用于`合约模式`下的`全仓杠杆`订单   
在其他情况下该参数将被忽略。  
>> sz | String | 委托数量  
>> px | String | 委托价格  
>> side | String | 报价单方向  
>> posSide | String | 持仓方向  
买卖模式下默认为`net`。如未指定，则返回""，相当于`net`。   
在开平仓模式下仅可选择`long`或`short`。 如未指定，则返回""，对应于为交易开新仓位的方向（买入=>`long`，卖出=>`short`）。  
仅适用交割、永续。  
>> tgtCcy | String | 委托数量的类型   
定义`sz`属性的单位。仅适用于 instType=`SPOT`。有效值为`base_ccy`和`quote_ccy`。未指定时，默认为`base_ccy`。  
>> tradeQuoteCcy | String | 交易使用的计价币种。仅适用于 SPOT。  
默认值为 instId 的报价币种，例如：对于 `BTC-USD`，默认值为 `USD`.