---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#block-trading-websocket-private-channel-structure-block-trades-channel
anchor_id: block-trading-websocket-private-channel-structure-block-trades-channel
api_type: WebSocket
updated_at: 2026-06-28 19:37:36.362297
---

# Structure block trades channel

Retrieve user's block trades data. All the legs in the same block trade are included in the same update. Data will be pushed whenever there is a block trade that the user is a counterparty for (i.e. the taker or the executing maker). Makers who received a `traded_away` status will not receive data from this channel.  
  
#### URL Path

/ws/v5/business (required login)

> Request Example
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "struc-block-trades"
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
              "channel": "struc-block-trades"
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
`struc-block-trades`  
  
> Successful Response Example
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "struc-block-trades"
      },
      "connId": "a4d3ae55"
    }
    

> Failure Response Example
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"struc-block-trades\""}]}",
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
`struc-block-trades`  
code | String | No | Error code  
msg | String | No | Error message  
connId | String | Yes | WebSocket connection ID  
  
> Push Data Example
    
    
    {
        "arg":{
            "channel":"struc-block-trades",
            "uid": "77982378738415879"
        },
        "data":[
            {
                "cTime":"1608267227834",
                "rfqId":"18753",
                "clRfqId":"",
                "quoteId":"25092",
                "clQuoteId":"",
                "blockTdId":"180184",
                "tag":"123456",
                "tTraderCode":"ANAND",
                "mTraderCode":"WAGMI",
                "isSuccessful": true,
                "errorCode": "",
                "legs":[
                    {
                        "px":"0.0023",
                        "sz":"25.0",
                        "instId":"BTC-USD-20220630-60000-C",
                        "side":"sell",
                        "fee":"0.1001",
                        "feeCcy":"BTC",
                        "tradeId":"10211",
                        "tgtCcy":""
    
                    },
                    {
                        "px":"0.0033",
                        "sz":"25",
                        "instId":"BTC-USD-20220630-50000-C",
                        "side":"buy",
                        "fee":"0.1001",
                        "feeCcy":"BTC",
                        "tradeId":"10212",
                        "tgtCcy":""
    
                    }
                ]
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
> cTime | String | The time the trade was executed. Unix timestamp in milliseconds.  
> rfqId | String | RFQ ID.  
> clRfqId | String | Client-supplied RFQ ID. This attribute is treated as client sensitive information. It will not be exposed to the Maker, just return empty string "" for Maker.  
> quoteId | String | Quote ID.  
> clQuoteId | String | Client-supplied Quote ID. This attribute is treated as client sensitive information. It will not be exposed to the Taker, just return empty string "" for Taker.  
> blockTdId | String | Block trade ID.  
> tag | String | Trade tag. The block trade will have the tag of the RFQ or Quote it corresponds to.  
> tTraderCode | String | A unique identifier of the Taker. Empty If anonymous mode of RFQ is `True`.  
> mTraderCode | String | A unique identifier of the Maker. Empty If anonymous mode of Quote is `True`.  
> isSuccessful | Boolean | Whether the trade is filled successfully  
> errorCode | String | Error code for unsuccessful trades.   
It is "" for successful trade.  
> legs | Array of objects | Legs of trade  
>> instId | String | Instrument ID, e.g. BTC-USDT-SWAP  
>> px | String | The price the leg executed  
>> sz | String | Size of the leg.  
>> side | String | The direction of the leg. Valid value can be buy or sell.  
>> tgtCcy | String | Defines the unit of the “sz” attribute.   
Only applicable to instType = SPOT.   
The valid enumerations are `base_ccy` and `quote_ccy`. When not specified this is equal to `base_ccy` by default.  
>> fee | String | Fee. Negative number represents the user transaction fee charged by the platform. Positive fee represents rebate.  
>> feeCcy | String | Fee currency  
>> tradeId | String | Last traded ID.  
> acctAlloc | Array of objects | Applicable to both taker, maker  
>> blockTdId | String | Block trade ID  
>> errorCode | String | Error code for unsuccessful trades.It is "0" for successful trade.  
>> acct | String | The name of the allocated account of the RFQOnly applicable to taker, return "" to makers  
>> legs | Array of objects | The allocated legs of the account.  
>>> instId | String | The Instrument ID of each leg. Example : "BTC-USDT-SWAP"  
>>> sz | String | Filled size  
>>> tradeId | String | Trade ID  
>>> fee | String | Fee  
>>> feeCcy | String | Fee currency  
Group RFQ introduction  
  
1\. This endpoint is at parent RFQ level and contains account allocation. For parent RFQ, we should return the actual executed size, i.e. failed execution size should not be included in the parent RFQ level.  
2\. For account allocation, we should include both filled and failed child RFQ but add an errorCode to indicate whether a child RFQ is filled.  
3\. Trade results will only be returned to group RFQ creator. Allocated subaccounts and MSAs will not see trade results. Allocated accounts are expected to get these trades through trading bills.  
4\. Trades data will only be returned after all child RFQs are execuated.  
5\. For parent RFQ isSuccessful field,  
        1\. it will return true if any child RFQs are filled  
        2\. otherwise, if all child RFQ fails, it will return false  
6\. Parent RFQ blockTdId or legs tradeId will be empty. However, account allocation breakdown will be offered and tradeId will be attached.

---

# 大宗交易频道

获取用户自身的大宗交易信息。同一大宗交易中的所有腿都包含在同一更新中。只要用户自身作为交易对手（即询价方或成交的报价方）进行大宗交易，数据都将被推送。状态为 `traded_away` 的报价方将不会收到本频道的推送。  
  
#### 服务地址

/ws/v5/business (需要登录)

> 请求示例
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "struc-block-trades"
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
              "channel": "struc-block-trades"
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
`struc-block-trades`  
  
> 成功返回示例
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "struc-block-trades"
      },
      "connId": "a4d3ae55"
    }
    

> 失败返回示例
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"struc-block-trades\"}]}",
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
`struc-block-trades`  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID  
  
> 推送示例
    
    
    {
        "arg":{
            "channel":"struc-block-trades",
            "uid": "77982378738415879"
        },
        "data":[
            {
                "cTime":"1608267227834",
                "rfqId":"18753",
                "clRfqId":"",
                "quoteId":"25092",
                "clQuoteId":"",
                "blockTdId":"180184",
                "tag":"123456",
                "tTraderCode":"ANAND",
                "mTraderCode":"WAGMI",
                "isSuccessful": true,
                "errorCode": "",
                "legs":[
                    {
                        "px":"0.0023",
                        "sz":"25.0",
                        "instId":"BTC-USD-20220630-60000-C",
                        "side":"sell",
                        "fee":"0.1001",
                        "feeCcy":"BTC",
                        "tradeId":"10211",
                        "tgtCcy":""
    
                    },
                    {
                        "px":"0.0033",
                        "sz":"25",
                        "instId":"BTC-USD-20220630-50000-C",
                        "side":"buy",
                        "fee":"0.1001",
                        "feeCcy":"BTC",
                        "tradeId":"10212",
                        "tgtCcy":""
    
                    }
                ]
            }
        ]
    }
    

#### 推送数据参数

**参数名** | **类型** | **描述**  
---|---|---  
arg | Object | 订阅成功的频道  
> channel | String | 频道名  
> uid | String | 用户标识  
data | Array of objects | 订阅的数据  
> cTime | String | 执行创建的时间戳，Unix 时间戳格式，以毫秒为单位。  
> rfqId | String | RFQ ID.  
> clRfqId | String | 由用户设置的 RFQ ID。 此属性被视为客户端敏感信息。 不会暴露给 Maker，只返回空字符串“”给 Maker。  
> quoteId | String | Quote ID.  
> clQuoteId | String | 由用户设置的 Quote ID。 此属性被视为客户端敏感信息。 不会暴露给 Taker，只为 Taker 返回空字符串“”。  
> blockTdId | String | 大宗交易ID  
> tag | String | 交易标签，大宗交易将有与其对应的询价单或报价单相同的标签。  
> tTraderCode | String | 报价方唯一标识代码。询价时 Anonymous 设置为 `True` 时不可见。  
> mTraderCode | String | 询价方唯一标识代码。报价时 Anonymous 设置为 `True` 时不可见。  
> isSuccessful | Boolean | 交易是否成功  
> errorCode | String | 未成功交易的错误码。  
对于成功交易为 ""。  
> legs | Array of objects | 组合交易  
>> instId | String | 产品ID  
>> px | String | 成交价格  
>> sz | String | 成交数量  
>> side | String | 询价单方向  
>> tgtCcy | String | 委托数量的类型   
定义`sz`属性的单位。仅适用于 instType=`SPOT`。有效值为`base_ccy`和`quote_ccy`。未指定时，默认为`base_ccy`。  
>> fee | String | 手续费，正数代表平台返佣 ，负数代表平台扣除。  
>> feeCcy | String | 手续费币种  
>> tradeId | String | 最新成交Id  
> acctAlloc | Array of objects | 组合询价单的账户分配  
>> blockTdId | String | 大宗交易ID  
>> errorCode | String | 事件执行结果的code，0代表成功  
>> acct | String | 账户名  
只适用于 Taker，对于 Maker 返回""  
>> legs | Array of objects | 组合交易  
>>> instId | String | 产品ID  
>>> sz | String | 成交数量  
>>> tradeId | String | 最新的成交Id  
>>> fee | String | 手续费  
>>> feeCcy | String | 手续费币种  
组合询价单介绍  
  
1\. 该频道返回的数据应为父级询价单级别，而不是子级询价单执行级别。  
2\. 对于账户分配，包含所有已成交和未成交的子级询价单，但添加 errorCode 来指示子级询价单是否已成交。  
3\. 交易结果将仅返回给组合询价单 Taker 及 Maker。分配的子账户和资管账户将无法看到交易结果。分配的账户应通过交易账单获取这些交易。  
4\. 交易数据仅在所有子级询价单执行后返回。  
5\. 对于父级询价单的 isSuccessful 字段，  
        1\. 如果任何子级询价单已成交，则返回 true  
        2\. 否则，如果所有子级询价单均失败，则返回 false  
6\. 父级询价单的 blockTdId 或 legs 的 tradeId 将为空。但将提供账户分配的详细信息，并附带 blockTdId 以及 tradeId。