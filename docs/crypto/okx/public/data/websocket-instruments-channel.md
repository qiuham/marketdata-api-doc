---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#public-data-websocket-instruments-channel
anchor_id: public-data-websocket-instruments-channel
api_type: WebSocket
updated_at: 2026-07-04 19:39:02.159717
---

# Instruments channel

The triggering scenarios for incremental data are:  
1\. When there is any change to the instrument’s state (such as delivery of FUTURES, exercise of OPTION, listing of new contracts / trading pairs, trading suspension, etc.)  
2\. When the trading parameters change (tickSz,minSz,maxMktSz)  
3\. When the expTime or listTime changes  
  
  
#### URL Path

/ws/v5/public

> Request Example
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "instruments",
          "instType": "SPOT"
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
              "channel": "instruments",
              "instType": "SPOT"
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
`instruments`  
> instType | String | Yes | Instrument type  
`SPOT`  
`MARGIN`  
`SWAP`  
`FUTURES`  
`OPTION`  
`EVENTS`  
  
> Successful Response Example
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "instruments",
        "instType": "SPOT"
      },
      "connId": "a4d3ae55"
    }
    

> Failure Response Example
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"instruments\", \"instType\" : \"FUTURES\"}]}",
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
> instType | String | Yes | Instrument type  
`SPOT`  
`MARGIN`  
`SWAP`  
`FUTURES`  
`OPTION`  
`EVENTS`  
code | String | No | Error code  
msg | String | No | Error message  
connId | String | Yes | WebSocket connection ID  
  
> Push Data Example
    
    
    {
      "arg": {
        "channel": "instruments",
        "instType": "SPOT"
      },
      "data": [
        {
            "alias": "",
            "auctionEndTime": "",
            "baseCcy": "BTC",
            "category": "1",
            "ctMult": "",
            "ctType": "",
            "ctVal": "",
            "ctValCcy": "",
            "contTdSwTime": "1704876947000",
            "expTime": "",
            "futureSettlement": false,
            "groupId": "1",
            "instFamily": "",
            "instId": "BTC-USDT",
            "instType": "SPOT",
            "lever": "10",
            "listTime": "1606468572000",
            "lotSz": "0.00000001",
            "maxIcebergSz": "9999999999.0000000000000000",
            "maxLmtAmt": "1000000",
            "maxLmtSz": "9999999999",
            "maxMktAmt": "1000000",
            "maxMktSz": "",
            "maxStopSz": "",
            "maxTriggerSz": "9999999999.0000000000000000",
            "maxTwapSz": "9999999999.0000000000000000",
            "minSz": "0.00001",
            "optType": "",
            "openType": "call_auction",
            "preMktSwTime": "",
            "quoteCcy": "USDT",
            "settleCcy": "",
            "state": "live",
            "ruleType": "normal",
            "stk": "",
            "tickSz": "0.1",
            "uly": "",
            "instIdCode": 1000000000,
            "instCategory": "1",
            "upcChg": [
                {
                    "param": "tickSz",
                    "newValue": "0.0001",
                    "effTime": "1704876947000"
                }
            ]
        }
      ]
    }
    

#### Push data parameters

Parameter | Type | Description  
---|---|---  
arg | Object | Subscribed channel  
> channel | String | Channel name  
> instType | String | Instrument type  
data | Array of objects | Subscribed data  
> instType | String | Instrument type  
> seriesId | String | Series ID, e.g. `BTC-ABOVE-DAILY`. Only applicable to `EVENTS`  
> instId | String | Instrument ID, e.g. `BTC-UST`  
> uly | String | Underlying, e.g. `BTC-USD`   
Only applicable to `FUTURES`/`SWAP`/`OPTION`  
> groupId | String | Instrument trading fee group ID  
Spot:  
`1`: Spot USDT  
`2`: Spot USDC & Crypto  
`3`: Spot TRY  
`4`: Spot EUR  
`5`: Spot BRL  
`7`: Spot AED  
`8`: Spot AUD  
`9`: Spot USD  
`10`: Spot SGD  
`11`: Spot zero  
`12`: Spot group one  
`13`: Spot group two  
`14`: Spot group three  
`15`: Spot special rule  
  
Expiry futures:  
`1`: Expiry futures crypto-margined  
`2`: Expiry futures USDT-margined  
`3`: Expiry futures USDC-margined  
`4`: Expiry futures premarket  
`5`: Expiry futures group one  
`6`: Expiry futures group two  
  
Perpetual futures:  
`1`: Perpetual futures crypto-margined  
`2`: Perpetual futures USDT-margined  
`3`: Perpetual futures USDC-margined  
`4`: Perpetual futures group one  
`5`: Perpetual futures group two  
`6`: Stock perpetual futures   
  
Options:  
`1`: Options crypto-margined  
`2`: Options USDC-margined  
  
**instType and groupId should be used together to determine a trading fee group. Users should use this endpoint together with[fee rates endpoint](/docs-v5/en/#trading-account-rest-api-get-fee-rates) to get the trading fee of a specific symbol.**   
  
**Some enum values may not apply to you; the actual return values shall prevail.**  
> instFamily | String | Instrument family, e.g. `BTC-USD`   
Only applicable to `FUTURES`/`SWAP`/`OPTION`  
> category | String | Currency category. Note: this parameter is already deprecated  
> baseCcy | String | Base currency, e.g. `BTC` in `BTC-USDT`   
Only applicable to `SPOT`/`MARGIN`  
> quoteCcy | String | Quote currency, e.g. `USDT` in `BTC-USDT`   
Only applicable to `SPOT`/`MARGIN`  
> settleCcy | String | Settlement and margin currency, e.g. `BTC`   
Only applicable to `FUTURES`/`SWAP`/`OPTION`  
> ctVal | String | Contract value  
> ctMult | String | Contract multiplier  
> ctValCcy | String | Contract value currency  
> optType | String | Option type  
`C`: Call  
`P`: Put  
Only applicable to `OPTION`  
> stk | String | Strike price  
Only applicable to `OPTION`  
> listTime | String | Listing time  
Only applicable to `FUTURES`/`SWAP`/`OPTION`  
> auctionEndTime | String | ~~The end time of call auction, Unix timestamp format in milliseconds, e.g.`1597026383085`   
Only applicable to `SPOT` that are listed through call auctions, return "" in other cases (deprecated, use contTdSwTime)~~  
> contTdSwTime | String | Continuous trading switch time. The switch time from call auction, prequote to continuous trading, Unix timestamp format in milliseconds. e.g. `1597026383085`.  
Only applicable to `SPOT`/`MARGIN` that are listed through call auction or prequote, return "" in other cases.  
> preMktSwTime | String | The time premarket swap switched to normal swap, Unix timestamp format in milliseconds, e.g. `1597026383085`.   
Only applicable premarket `SWAP`  
> openType | String | Open type  
`fix_price`: fix price opening  
`pre_quote`: pre-quote  
`call_auction`: call auction   
Only applicable to `SPOT`/`MARGIN`, return "" for all other business lines  
> expTime | String | Expiry time  
Applicable to `SPOT`/`MARGIN`/`FUTURES`/`SWAP`/`OPTION`. For `FUTURES`/`OPTION`, it is the delivery/exercise time. It can also be the delisting time of the trading instrument. Update once change.  
> lever | String | Max Leverage  
Not applicable to `SPOT`/`OPTION`, used to distinguish between `MARGIN` and `SPOT`.  
> tickSz | String | Tick size, e.g. `0.0001`.  
For `OPTION`/`EVENTS`, it is the minimum tickSz among tick band.  
> lotSz | String | Lot size  
If it is a derivatives contract, the value is the number of contracts.  
If it is `SPOT`/`MARGIN`, the value is the quantity in `base currency`  
> minSz | String | Minimum order size  
If it is a derivatives contract, the value is the number of contracts.  
If it is `SPOT`/`MARGIN`, the value is the quantity in `base currency`  
> ctType | String | Contract type  
`linear`: linear contract  
`inverse`: inverse contract  
Only applicable to `FUTURES`/`SWAP`  
> alias | String | Contract alias (deprecated — use expTime to obtain the delivery time, will be removed by the end of April 2026)  
`this_week`  
`next_week`  
`this_month`  
`next_month`  
`quarter`  
`next_quarter`  
`this_five_years`: current 5-year contract  
`next_five_years`: next 5-year contract  
Only applicable to `FUTURES`  
> state | String | Instrument status  
`live`  
`suspend`  
`expired`  
`rebase`: can't be traded during rebasing, only applicable to `SWAP`  
`post_only`: only post-only orders are accepted; existing post-only orders can be amended and cancelled. Other order types (market, IOC, FOK, normal limit) are rejected. Only applicable to `SWAP`  
`preopen`. e.g. There will be `preopen` before the Futures and Options new contracts state is live.  
`test`: Test pairs, can't be traded  
`settling`: Settling, only applicable to `EVENTS`  
> ruleType | String | Trading rule types  
`normal`: normal trading  
`pre_market`: pre-market trading  
`rebase_contract`: pre-market rebase contract  
`xperp`: perpetual-style futures, only applicable to certain `FUTURES` contracts  
> maxLmtSz | String | The maximum order quantity of a single limit order.  
If it is a derivatives contract, the value is the number of contracts.  
If it is `SPOT`/`MARGIN`, the value is the quantity in `base currency`.  
> maxMktSz | String | The maximum order quantity of a single market order.  
If it is a derivatives contract, the value is the number of contracts.  
If it is `SPOT`/`MARGIN`, the value is the quantity in `USDT`.  
> maxTwapSz | String | The maximum order quantity of a single TWAP order.  
If it is a derivatives contract, the value is the number of contracts.  
If it is `SPOT`/`MARGIN`, the value is the quantity in `base currency`.  
> maxIcebergSz | String | The maximum order quantity of a single iceBerg order.  
If it is a derivatives contract, the value is the number of contracts.  
If it is `SPOT`/`MARGIN`, the value is the quantity in `base currency`.  
> maxTriggerSz | String | The maximum order quantity of a single trigger order.  
If it is a derivatives contract, the value is the number of contracts.  
If it is `SPOT`/`MARGIN`, the value is the quantity in `base currency`.  
> maxStopSz | String | The maximum order quantity of a single stop market order.  
If it is a derivatives contract, the value is the number of contracts.  
If it is `SPOT`/`MARGIN`, the value is the quantity in `USDT`.  
> futureSettlement | Boolean | Whether daily settlement for expiry feature is enabled  
Applicable to `FUTURES` `cross`  
> instIdCode | Integer | Instrument ID code.   
For simple binary encoding, you must use `instIdCode` instead of `instId`.  
For the same `instId`, it's value may be different between production and demo trading.   
It is `null` when the value is not generated.  
> instCategory | String | The asset category of the instrument’s base asset (the first segment of the instrument ID). For example, for `BTC-USDT-SWAP`, the `instCategory` represents the asset category of `BTC`.   
`1`: Crypto   
`3`: Stocks   
`4`: Commodities   
`5`: Forex   
`6`: Bonds   
`""`: Not available  
> upcChg | Array of objects | Upcoming changes. It is [] when there is no upcoming change.  
>> param | String | The parameter name to be updated.   
`tickSz`  
`minSz`: For `FUTURES`/`SWAP`, `lotSz` will be modified synchronously.  
`maxMktSz`  
>> newValue | String | The parameter value that will replace the current one.  
>> effTime | String | Effective time. Unix timestamp format in milliseconds, e.g. `1597026383085`  
Instrument status will trigger pushing of incremental data from instruments channel. When a new contract is going to be listed, the instrument data of the new contract will be available with status preopen. When a product is going to be delisted (e.g. when a FUTURES contract is settled or OPTION contract is exercised), the instrument status will be changed to expired.  listTime and contTdSwTime  
For spot symbols listed through a call auction or pre-open, listTime represents the start time of the auction or pre-open, and contTdSwTime indicates the end of the auction or pre-open and the start of continuous trading. For other scenarios, listTime will mark the beginning of continuous trading, and contTdSwTime will return an empty value "".  state  
For `SPOT`, `MARGIN`, `SWAP`, and `FUTURES`, the state changes from `preopen` to `live` when the `listTime` is reached. For `OPTION` contracts, the state may change to `live` slightly after `listTime` due to internal processing. It is recommended to verify that `state` is `live` before placing orders. Certain symbols will now have `state:preopen` before they go live. Before going live, the instruments channel will push data for pre-listing symbols with `state:preopen`. If the listing is cancelled, the channel will send full data excluding the cancelled symbol, without additional notification. When the symbol goes live (at or shortly after `listTime` for `OPTION`), the channel will push data with `state:live`. Users can also query the corresponding data via the REST endpoint.  
When a product is going to be delisted (e.g. when a FUTURES contract is settled or OPTION contract is exercised), the instrument will not be available.

---

# 产品频道

增量数据的触发场景有：  
1\. 当有产品状态 state 变化时（如期货交割、期权行权、新合约/币对上线、人工暂停/恢复交易等）  
2\. 当交易参数变更（tickSz,minSz,maxMktSz）时  
3\. 当上线时间或者下线时间（expTime， listTime）变更时  
  
  
#### URL Path

/ws/v5/public

> 请求示例
    
    
    { 
      "id": "1512",
      "op": "subscribe",  
      "args":   [    
        {     
          "channel": "instruments",
          "instType": "SPOT"
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
              "channel": "instruments",
              "instType": "SPOT"
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
`instruments`  
> instType | String | 是 | 产品类型  
`SPOT`：币币  
`MARGIN`：币币杠杆  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`OPTION`：期权  
`EVENTS`：事件合约  
  
> 成功返回示例
    
    
    {
      "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "instruments",
            "instType": "SPOT"
        },
        "connId": "a4d3ae55"
    }
    

> 失败返回示例
    
    
    {
      "id": "1512",
        "event": "error",
        "code": "60012",
        "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"instruments\", \"instType\" : \"FUTURES\"}]}",
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
> instType | String | 是 | 产品类型  
`SPOT`：币币  
`MARGIN`：币币杠杆  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`OPTION`：期权  
`EVENTS`：事件合约  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID  
  
> 推送示例
    
    
    {
      "arg": {
        "channel": "instruments",
        "instType": "SPOT"
      },
      "data": [
        {
            "alias": "",
            "auctionEndTime": "",
            "baseCcy": "BTC",
            "category": "1",
            "ctMult": "",
            "ctType": "",
            "ctVal": "",
            "ctValCcy": "",
            "contTdSwTime": "1704876947000",
            "expTime": "",
            "futureSettlement": false,
            "groupId": "1",
            "instFamily": "",
            "instId": "BTC-USDT",
            "instType": "SPOT",
            "lever": "10",
            "listTime": "1606468572000",
            "lotSz": "0.00000001",
            "maxIcebergSz": "9999999999.0000000000000000",
            "maxLmtAmt": "1000000",
            "maxLmtSz": "9999999999",
            "maxMktAmt": "1000000",
            "maxMktSz": "",
            "maxStopSz": "",
            "maxTriggerSz": "9999999999.0000000000000000",
            "maxTwapSz": "9999999999.0000000000000000",
            "minSz": "0.00001",
            "optType": "",
            "openType": "call_auction",
            "preMktSwTime": "",
            "quoteCcy": "USDT",
            "settleCcy": "",
            "state": "live",
            "ruleType": "normal",
            "stk": "",
            "tickSz": "0.1",
            "uly": "",
            "instIdCode": 1000000000，
            "instCategory": "1",
            "upcChg": [
                {
                    "param": "tickSz",
                    "newValue": "0.0001",
                    "effTime": "1704876947000"
                }
            ]
        }
      ]
    }
    

#### 推送数据参数

参数名 | 类型 | 描述  
---|---|---  
arg | Object | 订阅的频道  
> channel | String | 频道名  
> instType | String | 产品类型  
data | Array of objects | 订阅的数据  
> instType | String | 产品类型  
> seriesId | String | 系列 ID，如 `BTC-ABOVE-DAILY`。仅适用于 `EVENTS`  
> instId | String | 产品ID，如 `BTC-USDT`  
> category | String | ~~币种类别~~ （已废弃）  
> uly | String | 标的指数，如 `BTC-USD`，仅适用于`交割`/`永续`/`期权`  
> groupId | String | 交易产品手续费分组ID  
现货：  
`1`：USDT现货  
`2`：USDC及Crypto现货  
`3`：TRY现货  
`4`：EUR现货  
`5`：BRL现货  
`7`：AED现货  
`8`：AUD现货  
`9`：USD现货  
`10`：SGD现货  
`11`：零手续费现货  
`12`：现货分组一  
`13`：现货分组二  
`14`：现货分组三  
`15`: 现货特别分组  
  
交割合约：  
`1`：币本位交割合约  
`2`：USDT本位交割合约  
`3`：USDC本位交割合约  
`4`：盘前交易交割合约  
`5`：交割合约分组一  
`6`：交割合约分组二  
  
永续合约：  
`1`：币本位永续合约  
`2`：USDT本位永续合约  
`3`：USDC本位永续合约  
`4`：永续合约分组一  
`5`：永续合约分组二  
`6`：股票永续合约  
  
期权：  
`1`：币本位期权  
`2`：USDC本位期权  
  
**用户需要同时使用instType和groupId来确定一个交易产品的交易手续费分组；用户应该将此接口和[获取当前账户交易手续费费率](/docs-v5/zh/#trading-account-rest-api-get-fee-rates)一起使用，以获取特定交易产品的手续费率**   
  
**部分枚举值可能不适用于您，以实际返回为准**  
> instFamily | String | 交易品种，如 `BTC-USD`，仅适用于`交割`/`永续`/`期权`  
> baseCcy | String | 交易货币币种，如 `BTC-USDT`中`BTC`，仅适用于`币币/币币杠杆`  
> quoteCcy | String | 计价货币币种，如 `BTC-USDT`中`USDT`，仅适用于`币币/币币杠杆`  
> settleCcy | String | 盈亏结算和保证金币种，如 `BTC`，仅适用于 `交割`/`永续`/`期权`  
> ctVal | String | 合约面值  
> ctMult | String | 合约乘数  
> ctValCcy | String | 合约面值计价币种  
> optType | String | 期权类型  
`C`：看涨期权  
`P`：看跌期权  
仅适用于`期权`  
> stk | String | 行权价格，仅适用于 `期权`  
> listTime | String | 上线时间  
> auctionEndTime | String | ~~集合竞价结束时间，Unix时间戳的毫秒数格式，如`1597026383085`   
仅适用于通过集合竞价方式上线的`币币`，其余情况返回""（已废弃，请使用contTdSwTime）~~  
> contTdSwTime | String | 连续交易开始时间，从集合竞价、提前挂单切换到连续交易的时间，Unix时间戳格式，单位为毫秒。e.g. `1597026383085`。  
仅适用于通过集合竞价或提前挂单上线的`SPOT`/`MARGIN`，在其他情况下返回""。  
> preMktSwTime | String | 盘前永续合约转为普通永续合约的时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
仅适用于盘前`SWAP`  
> openType | String | 开盘类型  
`fix_price`: 定价开盘  
`pre_quote`: 提前挂单  
`call_auction`: 集合竞价   
只适用于`SPOT`/`MARGIN`，其他业务线返回""  
> expTime | String | 产品下线时间  
适用于`币币/杠杆/交割/永续/期权`，对于 `交割/期权`，为自然的交割/行权时间；如果`币币/杠杆/交割/永续`产品人工下线，为产品下线时间，有变动就会推送。  
> lever | String | 该产品支持的最大杠杆倍数  
不适用于`币币`/`期权`。可用来区分`币币杠杆`和`币币`  
> tickSz | String | 下单价格精度，如 `0.0001`。  
对于 `OPTION`/`EVENTS`，该值为 tick band 中的最小下单价格精度。  
> lotSz | String | 下单数量精度  
合约的数量单位是`张`，现货的数量单位是`交易货币`  
> minSz | String | 最小下单数  
合约的数量单位是`张`，现货的数量单位是`交易货币`  
> ctType | String | 合约类型  
`linear`：正向合约  
`inverse`：反向合约  
仅适用于`交割/永续`  
> alias | String | 合约日期别名（已废弃，将于 2026 年 4 月底下线，请使用 expTime 字段获取交割时间）  
`this_week`：本周  
`next_week`：次周  
`this_month`：本月  
`next_month`：次月  
`quarter`：季度  
`next_quarter`：次季度  
`this_five_years`：当期五年合约  
`next_five_years`：次期五年合约  
仅适用于`交割`  
> state | String | 产品状态  
`live`：交易中   
`suspend`：暂停中  
`expired`：已过期  
`rebase`：合约在变基中，不可交易，仅适用于`SWAP`  
`post_only`：仅接受 post-only 订单；已有 post-only 订单可改单和撤单。其他订单类型（市价单、IOC、FOK、普通限价单）将被拒绝。仅适用于 `SWAP`  
`preopen`：预上线，交割和期权合约轮转生成到开始交易；部分交易产品上线前  
`test`：测试中（测试产品，不可交易）  
`settling`：结算中，仅适用于 `EVENTS`  
> ruleType | String | 交易规则类型  
`normal`：普通交易  
`pre_market`：盘前交易  
`rebase_contract`：盘前变基合约  
`xperp`：永续合约风格的交割合约，仅适用于部分 `FUTURES` 合约  
> maxLmtSz | String | 限价单的单笔最大委托数量  
合约的数量单位是`张`，现货的数量单位是`交易货币`  
> maxMktSz | String | 市价单的单笔最大委托数量  
合约的数量单位是`张`，现货的数量单位是`USDT`  
> maxTwapSz | String | 时间加权单的单笔最大委托数量  
合约的数量单位是`张`，现货的数量单位是`交易货币`  
> maxIcebergSz | String | 冰山委托的单笔最大委托数量  
合约的数量单位是`张`，现货的数量单位是`交易货币`  
> maxTriggerSz | String | 计划委托委托的单笔最大委托数量  
合约的数量单位是`张`，现货的数量单位是`交易货币`  
> maxStopSz | String | 止盈止损市价委托的单笔最大委托数量  
合约的数量单位是`张`，现货的数量单位是`USDT`  
> futureSettlement | Boolean | 交割合约是否支持每日结算  
适用于`全仓``交割`  
> instIdCode | Integer | 产品唯一标识代码。  
对于简单二进制编码，您必须使用 `instIdCode` 而不是 `instId`。  
对于同一`instId`，实盘和模拟盘的值可能会不一样。   
当值还未生成时，返回 `null`。  
> instCategory | String | 标的资产类别（产品ID的第一部分）。例如：对于 `BTC-USDT-SWAP`，instCategory 表示 `BTC` 所属的资产类别。  
`1`: 加密货币   
`3`: 股票类资产   
`4`: 大宗商品   
`5`: 外汇   
`6`: 债券   
`""` 当值不可用时返回空字符串  
> upcChg | Array of objects | 即将变更的参数列表。当没有即将变更的参数时，返回空数组 []  
>> param | String | 即将变更的参数名称。  
`tickSz`  
`minSz`：若为交割/永续合约（`FUTURES`/`SWAP`），`lotSz` 会同步变更。  
`maxMktSz`  
>> newValue | String | 即将变更的参数值。  
>> effTime | String | 生效时间。Unix 时间戳格式，例如 `1597026383085`  
产品状态变更，是触发instrument接口推送条件： 当合约预上线时，状态变更为预上线（即新生成一个合约，新合约会处于预上线状态）； 当产品下线的时候（如交割合约被交割的时候，期权合约被行权的时候），状态变更为已过期  listTime以及contTdSwTime  
对于通过集合竞价/提前挂单方式上线的币币，listTime为集合竞价/提前挂单的开始时间，contTdSwTime为集合竞价/提前挂单的结束时间、连续交易的开始时间；对于其他情况及业务线，listTime即为连续交易开始时间，contTdSwTime将返回""  state  
对于`币币`、`杠杆`、`永续`和`交割`，状态state在时间到达listTime时由`preopen`转变为`live`。对于`期权`合约，由于内部处理原因，状态可能在`listTime`之后短暂延迟变为`live`。建议在下单前确认`state`为`live`。上线前，交易产品频道将推送预上线产品，状态为`state:preopen`；若上线被取消，频道将全量推送数据，其中不包括被取消的预上线产品，不做额外通知。交易产品上线时（`期权`合约可能在listTime之后短暂时间内），频道将推送状态为交易中`state:live`。用户亦可以通过REST接口查询到相应数据。  
当产品下线的时候（如交割合约被交割的时候，期权合约被行权的时候），查询不到该产品