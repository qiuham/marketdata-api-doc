---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#block-trading-websocket-private-channel-rfqs-channel
anchor_id: block-trading-websocket-private-channel-rfqs-channel
api_type: WebSocket
updated_at: 2026-07-17 19:17:08.087416
---

# Rfqs channel

Retrieve the RFQs sent or received by the user. Data will be pushed whenever the user sends or receives an RFQ.

#### URL Path

/ws/v5/business (required login)

> Request Example
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "rfqs"
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
              "channel": "rfqs"
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
`rfqs`  
  
> Successful Response Example 
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "rfqs"
      },
      "connId": "a4d3ae55"
    }
    

> Failure Response Example
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"rfqs\"}]}",
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
`rfqs`  
code | String | No | Error code  
msg | String | No | Error message  
connId | String | Yes | WebSocket connection ID  
  
> Push Data Example
    
    
    {
        "arg":{
            "channel":"rfqs",
            "uid": "77982378738415879"
        },
        "data":[
            {
                "cTime":"1611033737572",
                "uTime":"1611033737572",
                "traderCode":"DSK2",
                "rfqId":"22534",
                "clRfqId":"",
                "tag":"123456",
                "state":"active",
                "flowType":"",
                "validUntil":"1611033857557",
                "allowPartialExecution": false,
                "counterparties":[
                    "DSK4",
                    "DSK5"
                ],
                "legs":[
                    {
                        "instId":"BTCUSD-211208-36000-C",
                        "tdMode":"cross",
                        "ccy":"USDT",
                        "sz":"25.0",
                        "side":"buy",
                        "posSide": "long",
                        "tgtCcy":""
                    },
                    {
                        "instId":"ETHUSD-211208-45000-C",
                        "tdMode":"cross",
                        "ccy":"USDT",
                        "sz":"25.0",
                        "side":"sell",
                        "posSide": "long",
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
> cTime | String | The timestamp the RFQ was created, Unix timestamp format in milliseconds.  
> uTime | String | The timestamp the RFQ was updated latest, Unix timestamp format in milliseconds.  
> state | String | The status of the RFQ. Valid values can be `active`, `canceled`, `filled`, `expired` `traded_away` or `failed`.   
`filled` indicates the RFQ was successfully executed against the maker's quote.   
`traded_away` only applies to Maker. The same RFQ can appear as `filled` to one maker and `traded_away` to another.   
Example: taker creates RFQ → makerA quotes pxA, makerB quotes pxB → pxA is better than pxB → taker executes quoteA → makerA sees `filled`, makerB sees `traded_away`.  
> counterparties | Array of Strings | The list of counterparties traderCode the RFQ was broadcasted to.  
> validUntil | String | The timestamp the RFQ expires. Unix timestamp format in milliseconds.  
> clRfqId | String | Client-supplied RFQ ID. This attribute is treated as client sensitive information. It will not be exposed to the Maker. Return empty for Maker, eg. "".  
> tag | String | RFQ tag. The block trade associated with the RFQ will have the same tag.  
> flowType | String | Identify the type of the RFQ.   
Only applicable to Makers, return "" for Takers  
> traderCode | String | A unique identifier of taker. Empty If anonymous mode is `True`.  
> rfqId | String | RFQ ID  
> allowPartialExecution | Boolean | Whether the RFQ can be partially filled provided that the shape of legs stays the same.   
Valid value is `true` or `false`.   
`false` by default.  
> legs | Array of objects | An Array of objects containing each leg of the RFQ.  
>> instId | String | Instrument ID, e.g. BTC-USDT-SWAP  
>> tdMode | String | Trade mode   
Margin mode: `cross` `isolated`   
Non-Margin mode: `cash`.   
If not provided, tdMode will inherit default values set by the system shown below:   
Futures mode & SPOT: `cash`   
Buy options in Futures mode and Multi-currency Margin: `isolated`   
Other cases: `cross`  
>> ccy | String | Margin currency.   
Only applicable to `cross` `MARGIN` orders in `Futures mode`. The parameter will be ignored in other scenarios.  
>> sz | String | Size of the leg.  
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
> groupId | String | Group RFQ ID  
Only applicable to group RFQ, return "" for normal RFQ  
> acctAlloc | Array of objects | Account level allocation of the RFQ  
This is only applicable to the taker.  
>> acct | String | The name of the allocated account of the RFQ.  
>> legs | Array of objects | The allocated legs of the account.  
>>> instId | String | The Instrument ID of each leg. Example : "BTC-USDT-SWAP"  
>>> sz | String | The allocated size of each leg.  
>>> tdMode | String | Trade mode  
>>> ccy | String | Margin currency  
>>> posSide | String | Position side  
state: pending_fill is a kind of moment state, and this channel doesn't update it.  Group RFQ introduction  
  
1\. allowPartialExecution field is always true for group RFQ for taker and maker.  
2\. Add a new response parameter acctAlloc with all account allocation the same as the initial request, but it is only applicable to takers.  
3\. Add a new response parameter groupId, applicable to both takers and makers.  
4\. For group RFQ state,  
        1\. if any allocated account is pending execution, then pending_fill  
        2\. otherwise,  
                1\. if any allocated account is filled, then filled  
                2\. if all allocated accounts are failed, then failed

---

# 询价频道

获取用户自身发送或接收的询价信息。每当用户自身发送或接收询价时，数据都将被推送。

#### 服务地址

/ws/v5/business (需要登录)

> 请求示例
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "rfqs"
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
              "channel": "rfqs"
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
`rfqs`  
  
> 成功返回示例 
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "rfqs"
      },
      "connId": "a4d3ae55"
    }
    

> 失败返回示例
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"rfqs\"}]}",
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
`rfqs`  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID  
  
> 推送示例
    
    
    {
        "arg":{
            "channel":"rfqs",
            "uid": "77982378738415879"
        },
        "data":[
            {
                "cTime":"1611033737572",
                "uTime":"1611033737572",
                "traderCode":"DSK2",
                "rfqId":"22534",
                "clRfqId":"",
                "tag":"123456",
                "state":"active",
                "flowType": "",
                "validUntil":"1611033857557",
                "allowPartialExecution": false,
                "counterparties":[
                    "DSK4",
                    "DSK5"
                ],
                "legs":[
                    {
                        "instId":"BTCUSD-211208-36000-C",
                        "tdMode":"cross",
                        "ccy":"USDT",
                        "sz":"25.0",
                        "side":"buy",
                        "posSide": "long",
                        "tgtCcy":""
                    },
                    {
                        "instId":"ETHUSD-211208-45000-C",
                        "tdMode":"cross",
                        "ccy":"USDT",
                        "sz":"25.0",
                        "side":"sell",
                        "posSide": "long",
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
> cTime | String | 询价单创建时间，Unix时间戳的毫秒数格式。  
> uTime | String | 询价单状态更新时间，Unix时间戳的毫秒数格式。  
> state | String | 询价单的状态  
有效值有 `active` `canceled` `filled` `expired` `traded_away` `failed`  
`filled` 表示询价单已成功按照做市商的报价成交。  
`traded_away` 仅适用于报价方。同一笔询价单可能对一个报价方显示为 `filled`，而对另一个报价方显示为 `traded_away`。  
示例：询价方创建询价单 → 做市商A报价 pxA，做市商B报价 pxB → pxA 优于 pxB → 询价方执行做市商A的报价 → 做市商A看到 `filled`，做市商B看到 `traded_away`。  
> counterparties | Array of Strings | 报价方列表  
> validUntil | String | 询价单的过期时间，Unix时间戳的毫秒数格式。  
> clRfqId | String | 询价单自定义ID，为客户敏感信息，不会公开，对报价方返回""。  
> tag | String | 询价单标签，与此询价单关联的大宗交易将有相同的标签。  
> flowType | String | 识别询价单的类型。   
仅适用于报价方，返回""给询价方。  
> traderCode | String | 询价方唯一标识代码，询价时 Anonymous 设置为 `True` 时不可见  
> rfqId | String | 询价单ID  
> allowPartialExecution | Boolean | RFQ是否可以被部分执行，如果腿的比例和原RFQ一致。>有效值为`true`或`false`。  
> legs | Array of objects | 组合交易  
>> instId | String | 产品ID  
>> tdMode | String | 交易模式   
保证金模式：`cross`全仓 `isolated`逐仓   
非保证金模式：`cash`非保证金.   
如未提供，tdMode 将继承系统设置的默认值：   
合约模式 & 现货: `cash`   
合约模式和跨币种保证金模式下买入期权： `isolated`   
其他情况: `cross`  
>> ccy | String | 保证金币种，仅适用于`合约模式`下的`全仓杠杆`订单   
在其他情况下该参数将被忽略。  
>> sz | String | 委托数量  
>> side | String | 询价单方向  
>> posSide | String | 持仓方向   
买卖模式下默认为`net`。如未指定，则返回""，相当于`net`。   
在开平仓模式下仅可选择`long`或`short`。 如未指定，则返回""，对应于为交易开新仓位的方向（买入=>`long`，卖出=>`short`）。  
仅适用交割、永续。  
>> tgtCcy | String | 委托数量的类型   
定义`sz`属性的单位。仅适用于 instType=`SPOT`。有效值为`base_ccy`和`quote_ccy`。未指定时，默认为`base_ccy`。  
>> tradeQuoteCcy | String | 交易使用的计价币种。仅适用于 SPOT。  
默认值为 instId 的报价币种，例如：对于 `BTC-USD`，默认值为 `USD`.  
> groupId | String | 组合询价单ID  
只适用于组合询价单，普通询价单返回 ""  
> acctAlloc | Array of objects | 组合询价单的账户分配  
只适用于 Taker  
>> acct | String | 账户名  
>> legs | Array of objects | 组合交易  
>>> instId | String | 产品ID  
>>> sz | String | 委托数量  
>>> tdMode | String | 交易模式  
>>> ccy | String | 保证金币种  
>>> posSide | String | 持仓方向  
state: pending_fill 是一个瞬间状态，该频道不会推送。  组合询价单介绍  
  
1\. allowPartialExecution 字段始终为 true，适用于 Taker 和 Maker 的组合询价单。  
2\. 新增返回参数 acctAlloc ，包含所有账户分配信息，但仅适用于 Taker。  
3\. 新增返回参数 groupId，适用于 Taker 和 Maker。  
4\. 对于组合询价单状态  
        1\. 如果任何分配账户处于待执行状态，则状态为 pending_fill  
        2\. 否则，  
                1\. 如果任何分配账户已成交，则状态为 filled  
                2\. 如果所有分配账户均失败，则状态为 failed