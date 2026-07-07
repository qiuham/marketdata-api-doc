---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-market-data-ws-order-book-channel
anchor_id: order-book-trading-market-data-ws-order-book-channel
api_type: WebSocket
updated_at: 2026-07-07 19:42:31.794624
---

# WS / Order book channel

Retrieve order book data. Best ask price may be lower than the best bid price during the pre-open period.  
  
  
Use `books` for 400 depth levels, `books5` for 5 depth levels, `bbo-tbt` tick-by-tick 1 depth level, `books50-l2-tbt` tick-by-tick 50 depth levels, and `books-l2-tbt` for tick-by-tick 400 depth levels.   

  * `books`: 400 depth levels will be pushed in the initial full snapshot. Incremental data will be pushed every 100 ms for the changes in the order book during that period of time.   

  * `books-elp`: only push ELP orders. 400 depth levels will be pushed in the initial full snapshot. Incremental data will be pushed every 100 ms for the changes in the order book during that period of time.   

  * `books5`: 5 depth levels snapshot will be pushed in the initial push. Snapshot data will be pushed every 100 ms when there are changes in the 5 depth levels snapshot.  

  * `bbo-tbt`: 1 depth level snapshot will be pushed in the initial push. Snapshot data will be pushed every 10 ms when there are changes in the 1 depth level snapshot.   

  * `books-l2-tbt`: 400 depth levels will be pushed in the initial full snapshot. Incremental data will be pushed every 10 ms for the changes in the order book during that period of time.   

  * `books50-l2-tbt`: 50 depth levels will be pushed in the initial full snapshot. Incremental data will be pushed every 10 ms for the changes in the order book during that period of time.
  * The push sequence for order book channels within the same connection and trading symbols is fixed as: bbo-tbt -> books-l2-tbt -> books50-l2-tbt -> books -> books-elp -> books5.
  * Users can not simultaneously subscribe to `books-l2-tbt` and `books50-l2-tbt/books` channels for the same trading symbol. 
    * For more details, please refer to the changelog [2024-07-17](/docs-v5/log_en/#2024-07-17)

Only API users who are VIP4 and above in trading fee tier are allowed to subscribe to "books-l2-tbt" 400 depth channels. Other users will receive error code 64003.  
Only API users who are VIP4 and above in trading fee tier are allowed to subscribe to "books50-l2-tbt" 50 depth channels. Other users will receive error code 64003.  

Identity verification refers to [Login](/docs-v5/en/#overview-websocket-login)

#### URL Path

/ws/v5/public

> Request Example
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "books",
          "instId": "BTC-USDT"
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
        args = [
          {
            "channel": "books",
            "instId": "BTC-USDT"
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
`books`  
`books5`  
`bbo-tbt`  
`books50-l2-tbt`  
`books-l2-tbt`  
> instId | String | Yes | Instrument ID  
  
> Response Example
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "books",
        "instId": "BTC-USDT"
      },
      "connId": "a4d3ae55"
    }
    

> Failure example
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"books\", \"instId\" : \"BTC-USD-191227\"}]}",
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
> instId | String | Yes | Instrument ID  
msg | String | No | Error message  
code | String | No | Error code  
connId | String | Yes | WebSocket connection ID  
  
> Push Data Example: Full Snapshot
    
    
    {
      "arg": {
        "channel": "books",
        "instId": "BTC-USDT"
      },
      "action": "snapshot",
      "data": [
        {
          "asks": [
            ["8476.98", "415", "0", "13"],
            ["8477", "7", "0", "2"],
            ["8477.34", "85", "0", "1"],
            ["8477.56", "1", "0", "1"],
            ["8505.84", "8", "0", "1"],
            ["8506.37", "85", "0", "1"],
            ["8506.49", "2", "0", "1"],
            ["8506.96", "100", "0", "2"]
          ],
          "bids": [
            ["8476.97", "256", "0", "12"],
            ["8475.55", "101", "0", "1"],
            ["8475.54", "100", "0", "1"],
            ["8475.3", "1", "0", "1"],
            ["8447.32", "6", "0", "1"],
            ["8447.02", "246", "0", "1"],
            ["8446.83", "24", "0", "1"],
            ["8446", "95", "0", "3"]
          ],
          "ts": "1597026383085",
          "checksum": 0,
          "prevSeqId": -1,
          "seqId": 123456
        }
      ]
    }
    

> Push Data Example: Incremental Data
    
    
    {
      "arg": {
        "channel": "books",
        "instId": "BTC-USDT"
      },
      "action": "update",
      "data": [
        {
          "asks": [
            ["8476.98", "415", "0", "13"],
            ["8477", "7", "0", "2"],
            ["8477.34", "85", "0", "1"],
            ["8477.56", "1", "0", "1"],
            ["8505.84", "8", "0", "1"],
            ["8506.37", "85", "0", "1"],
            ["8506.49", "2", "0", "1"],
            ["8506.96", "100", "0", "2"]
          ],
          "bids": [
            ["8476.97", "256", "0", "12"],
            ["8475.55", "101", "0", "1"],
            ["8475.54", "100", "0", "1"],
            ["8475.3", "1", "0", "1"],
            ["8447.32", "6", "0", "1"],
            ["8447.02", "246", "0", "1"],
            ["8446.83", "24", "0", "1"],
            ["8446", "95", "0", "3"]
          ],
          "ts": "1597026383085",
          "checksum": 0,
          "prevSeqId": 123456,
          "seqId": 123457
        }
      ]
    }
    

#### Push data parameters

**Parameter** | **Type** | **Description**  
---|---|---  
arg | Object | Successfully subscribed channel  
> channel | String | Channel name  
> instId | String | Instrument ID  
action | String | Push data action, incremental data or full snapshot.   
`snapshot`: full   
`update`: incremental  
data | Array of objects | Subscribed data  
> asks | Array of Arrays | Order book on sell side  
> bids | Array of Arrays | Order book on buy side  
> ts | String | Order book generation time, Unix timestamp format in milliseconds, e.g. `1597026383085`   
Exception: For the `bbo-tbt` channel, `ts` is the timestamp when the book is generated by matching engine.  
> checksum | Integer | ~~Checksum~~ (Deprecated). The field remains in the push for `books`, `books-l2-tbt`, and `books50-l2-tbt`, but its value is fixed to `0` and must no longer be used for integrity verification. Please use `seqId/prevSeqId` to verify data continuity and accuracy.  
> prevSeqId | Integer | Sequence ID of the last sent message. Only applicable to `books`, `books-l2-tbt`, `books50-l2-tbt`  
> seqId | Integer | Sequence ID of the current message, implementation details below  
An example of the array of asks and bids values: ["411.8", "10", "0", "4"]  
\- "411.8" is the depth price  
\- "10" is the quantity at the price (number of contracts for derivatives, quantity in base currency for Spot and Spot Margin)  
\- "0" is part of a deprecated feature and it is always "0"  
\- "4" is the number of orders at the price.  If you need to subscribe to many 50 or 400 depth level channels, it is recommended to subscribe through multiple websocket connections, with each of less than 30 channels.  The order book data will be updated around once a second during the call auction.  `books/books5/bbo-tbt/books-l2-tbt/books50-l2-tbt` don't return ELP orders  
`books-elp` only return ELP orders, including both valid and invalid parts (invalid parts means ELP buy orders with a price higher than best bid of non-ELP orders; or ELP sell orders with a price lower than best ask of non-ELP orders). Users should distinguish valid and invalid parts using the best bid/ask price of non-ELP orders. 

#### Sequence ID

`seqId` is the sequence ID of the market data published. The set of sequence ID received by users is the same if users are connecting to the same channel through multiple websocket connections. Each `instId` has an unique set of sequence ID. Users can use `prevSeqId` and `seqId` to build the message sequencing for incremental order book updates. Generally the value of seqId is larger than prevSeqId. The `prevSeqId` in the new message matches with `seqId` of the previous message. The smallest possible sequence ID value is 0, except in snapshot messages where the prevSeqId is always -1.  

Exceptions:  
1\. If there are no updates to the depth for an extended period(Around 60 seconds), for the channel that always updates snapshot data, OKX will send the latest snapshot, for the channel that has incremental data, OKX will send a message with `'asks': [], 'bids': []` to inform users that the connection is still active. `seqId` is the same as the last sent message and `prevSeqId` equals to `seqId`. 2\. The sequence number may be reset due to maintenance, and in this case, users will receive an incremental message with `seqId` smaller than `prevSeqId`. However, subsequent messages will follow the regular sequencing rule.

##### Example

  1. Snapshot message: prevSeqId = -1, seqId = 10
  2. Incremental message 1 (normal update): prevSeqId = 10, seqId = 15
  3. Incremental message 2 (no update): prevSeqId = 15, seqId = 15
  4. Incremental message 3 (sequence reset): prevSeqId = 15, seqId = 3
  5. Incremental message 4 (normal update): prevSeqId = 3, seqId = 5

> Push Data Example of bbo-tbt channel
    
    
    {
      "arg": {
        "channel": "bbo-tbt",
        "instId": "BCH-USDT-SWAP"
      },
      "data": [
        {
          "asks": [
            [
              "111.06","55154","0","2"
            ]
          ],
          "bids": [
            [
              "111.05","57745","0","2"
            ]
          ],
          "ts": "1670324386802",
          "seqId": 363996337
        }
      ]
    }
    

> Push Data Example of books5 channel
    
    
    {
      "arg": {
        "channel": "books5",
        "instId": "BCH-USDT-SWAP"
      },
      "data": [
        {
          "asks": [
            ["111.06","55154","0","2"],
            ["111.07","53276","0","2"],
            ["111.08","72435","0","2"],
            ["111.09","70312","0","2"],
            ["111.1","67272","0","2"]],
          "bids": [
            ["111.05","57745","0","2"],
            ["111.04","57109","0","2"],
            ["111.03","69563","0","2"],
            ["111.02","71248","0","2"],
            ["111.01","65090","0","2"]],
          "instId": "BCH-USDT-SWAP",
          "ts": "1670324386802",
          "seqId": 363996337
        }
      ]
    }

---

# WS / 深度频道

获取深度数据。在提前挂单阶段，best ask的价格有机会低于best bid。`books`是400档频道，`books5`是5档频道， `bbo-tbt`是先1档后实时推送的频道，`books-l2-tbt`是先400档后实时推送的频道，`books50-l2-tbt`是先50档后实时推的频道；  
  
  * `books` 首次推400档快照数据，以后增量推送，每100毫秒推送一次变化的数据  

  * `books-elp` 仅推送ELP订单，首次推400档快照数据，以后增量推送，每100毫秒推送一次变化的数据  

  * `books5` 首次推5档快照数据，以后定量推送，每100毫秒当5档快照数据有变化推送一次5档数据  

  * `bbo-tbt` 首次推1档快照数据，以后定量推送，每10毫秒当1档快照数据有变化推送一次1档数据  

  * `books-l2-tbt` 首次推400档快照数据，以后增量推送，每10毫秒推送一次变化的数据  

  * `books50-l2-tbt` 首次推50档快照数据，以后增量推送，每10毫秒推送一次变化的数据
  * 单个连接、交易产品维度，深度频道的推送顺序固定为：bbo-tbt -> books-l2-tbt -> books50-l2-tbt -> books -> books-elp -> books5。
  * 在相同连接下，用户将无法为相同交易产品同时订阅 `books-l2-tbt` 以及 `books50-l2-tbt/books`频道 
    * 更多细节，请参阅更新日志 [2024-07-17](/docs-v5/log_zh/#2024-07-17)

books-l2-tbt400档深度频道，只允许交易手续费等级VIP4及以上的API用户订阅，其他用户接入将收到错误码64003。  
books50-l2-tbt50档深度频道，只允许交易手续费等级VIP4及以上的API用户订阅，其他用户接入将收到错误码64003。  

身份认证参考[登录](/docs-v5/zh/#overview-websocket-login)功能 

#### 服务地址

/ws/v5/public

> 请求示例
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [{
            "channel": "books",
            "instId": "BTC-USDT"
        }]
    }
    
    
    
    import asyncio
    
    from okx.websocket.WsPublicAsync import WsPublicAsync
    
    
    def callbackFunc(message):
        print(message)
    
    
    async def main():
        ws = WsPublicAsync(url="wss://wspap.okx.com:8443/ws/v5/public")
        await ws.start()
        args = [
          {
            "channel": "books",
            "instId": "BTC-USDT"
          }
        ]
    
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
`books`  
`books5`  
`bbo-tbt`  
`books-l2-tbt`  
`books50-l2-tbt`  
> instId | String | 是 | 产品ID  
  
> 返回示例
    
    
    {
        "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "books",
            "instId": "BTC-USDT"
        },
        "connId": "a4d3ae55"
    }
    

> 失败示例
    
    
    {
        "id": "1512",
        "event": "error",
        "code": "60012",
        "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"books\", \"instId\" : \"BTC-USD-191227\"}]}",
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
msg | String | 否 | 错误消息  
code | String | 否 | 错误码  
connId | String | 是 | WebSocket连接ID  
  
> 推送示例 ：全量
    
    
    {
        "arg": {
            "channel": "books",
            "instId": "BTC-USDT"
        },
        "action": "snapshot",
        "data": [{
            "asks": [
                ["8476.98", "415", "0", "13"],
                ["8477", "7", "0", "2"],
                ["8477.34", "85", "0", "1"],
                ["8477.56", "1", "0", "1"],
                ["8505.84", "8", "0", "1"],
                ["8506.37", "85", "0", "1"],
                ["8506.49", "2", "0", "1"],
                ["8506.96", "100", "0", "2"]
            ],
            "bids": [
                ["8476.97", "256", "0", "12"],
                ["8475.55", "101", "0", "1"],
                ["8475.54", "100", "0", "1"],
                ["8475.3", "1", "0", "1"],
                ["8447.32", "6", "0", "1"],
                ["8447.02", "246", "0", "1"],
                ["8446.83", "24", "0", "1"],
                ["8446", "95", "0", "3"]
            ],
            "ts": "1597026383085",
            "checksum": 0,
            "prevSeqId": -1,
            "seqId": 123456
        }]
    }
    

> 推送示例：增量
    
    
    {
        "arg": {
            "channel": "books",
            "instId": "BTC-USDT"
        },
        "action": "update",
        "data": [{
            "asks": [
                ["8476.98", "415", "0", "13"],
                ["8477", "7", "0", "2"],
                ["8477.34", "85", "0", "1"],
                ["8477.56", "1", "0", "1"],
                ["8505.84", "8", "0", "1"],
                ["8506.37", "85", "0", "1"],
                ["8506.49", "2", "0", "1"],
                ["8506.96", "100", "0", "2"]
            ],
            "bids": [
                ["8476.97", "256", "0", "12"],
                ["8475.55", "101", "0", "1"],
                ["8475.54", "100", "0", "1"],
                ["8475.3", "1", "0", "1"],
                ["8447.32", "6", "0", "1"],
                ["8447.02", "246", "0", "1"],
                ["8446.83", "24", "0", "1"],
                ["8446", "95", "0", "3"]
            ],
            "ts": "1597026383085",
            "checksum": 0,
            "prevSeqId": 123456,
            "seqId": 123457
        }]
    }
    

#### 推送数据参数

**参数名** | **类型** | **描述**  
---|---|---  
arg | Object | 订阅成功的频道  
> channel | String | 频道名  
> instId | String | 产品ID  
action | String | 推送数据动作，增量推送数据还是全量推送数据  
`snapshot`：全量   
`update`：增量  
data | Array of objects | 订阅的数据  
> asks | Array of Arrays | 卖方深度  
> bids | Array of Arrays | 买方深度  
> ts | String | 数据更新时间戳，Unix时间戳的毫秒数格式，如 `1597026383085`   
例外： 对于`bbo-tbt` 频道，`ts` 为撮合引擎触发时的时间戳  
> checksum | Integer | ~~检验和~~ （已弃用）。该字段仍会在 `books`、`books-l2-tbt`、`books50-l2-tbt` 推送中保留，但其值固定为 `0`，不应再用于数据完整性校验。请改用 `seqId/prevSeqId` 校验数据的连续性和准确性。  
> prevSeqId | Integer | 上一个推送的序列号。仅适用 `books`，`books-l2-tbt`，`books50-l2-tbt`  
> seqId | Integer | 推送的序列号 （下方注解）  
asks和bids值数组举例说明： ["411.8", "10", "0", "4"]  
\- 411.8为深度价格  
\- 10为此价格的数量 （合约交易为张数，现货/币币杠杆为交易币的数量  
\- 0该字段已弃用(始终为0)  
\- 4为此价格的订单数量  如果需要订阅多个50或400档频道，建议通过多个链接进行订阅，每个链接低于30条频道。  集合竞价期间，深度数据大约每秒更新一次  `books/books5/bbo-tbt/books-l2-tbt/books50-l2-tbt`不包含ELP订单  
`books-elp`仅返回 ELP 订单，包含有效部分及无效部分（无效部分指 ELP 买单价格高于非 ELP 订单最佳买单价；或 ELP 卖单价格低于非 ELP 订单最佳卖单价）。用户需根据非 ELP 订单的最佳买/卖价区分有效部分和无效部分。 

#### 序列号

`seqId`是交易所行情的一个序号。如果用户通过多个websocket连接同一频道，收到的序列号会是相同的。每个`instId`对应一套。用户可以使用在增量推送频道的`prevSeqId`和`seqId`来构建消息序列。这将允许用户检测数据包丢失和消息的排序。正常场景下`seqId`的值大于`prevSeqId`。新消息中的`prevSeqId`与上一条消息的`seqId`匹配。最小序列号值为0，除了快照消息的`prevSeqId`为-1。  

异常情况：  
1\. 如果一段时间内（约 60 秒）没有深度更新，对于定量推送频道，OKX 会推送最近的一条更新，对于增量推送频道，OKX将发一条消息`'asks': [], 'bids': []`以通知用户连接是正常的。推送的`seqId`跟上一条信息的一样，`prevSeqId`等于`seqId`。 2\. 序列号可能由于维护而重置，在这种情况下，用户将收到一条`seqId`小于`prevSeqId`的增量消息。随后的消息将遵循常规的排序规则。

##### 示例

  1. 快照推送：`prevSeqId = -1`，`seqId = 10`
  2. 增量推送1（正常更新）：`prevSeqId = 10`，`seqId = 15`
  3. 增量推送2（无更新）：`prevSeqId = 15`，`seqId = 15`
  4. 增量推送3（序列重置）：`prevSeqId = 15`，`seqId = 3`
  5. 增量推送4（正常更新）：`prevSeqId = 3`，`seqId = 5`

> bbo-tbt 频道推送示例
    
    
    {
      "arg": {
        "channel": "bbo-tbt",
        "instId": "BCH-USDT-SWAP"
      },
      "data": [
        {
          "asks": [
            [
              "111.06","55154","0","2"
            ]
          ],
          "bids": [
            [
              "111.05","57745","0","2"
            ]
          ],
          "ts": "1670324386802",
          "seqId": 363996337
        }
      ]
    }
    

> books5 频道推送示例
    
    
    {
      "arg": {
        "channel": "books5",
        "instId": "BCH-USDT-SWAP"
      },
      "data": [
        {
          "asks": [
            ["111.06","55154","0","2"],
            ["111.07","53276","0","2"],
            ["111.08","72435","0","2"],
            ["111.09","70312","0","2"],
            ["111.1","67272","0","2"]],
          "bids": [
            ["111.05","57745","0","2"],
            ["111.04","57109","0","2"],
            ["111.03","69563","0","2"],
            ["111.02","71248","0","2"],
            ["111.01","65090","0","2"]],
          "instId": "BCH-USDT-SWAP",
          "ts": "1670324386802",
          "seqId": 363996337
        }
      ]
    }