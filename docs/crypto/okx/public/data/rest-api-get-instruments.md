---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#public-data-rest-api-get-instruments
anchor_id: public-data-rest-api-get-instruments
api_type: REST
updated_at: 2026-07-03 19:40:27.254228
---

# Get instruments

Retrieve a list of instruments with open contracts for OKX. Retrieve available instruments info of current account, please refer to [Get instruments](/docs-v5/en/#trading-account-rest-api-get-instruments).  
  
#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP + Instrument Type

#### HTTP Request

`GET /api/v5/public/instruments`

> Request Example
    
    
    GET /api/v5/public/instruments?instType=SPOT
    
    
    
    import okx.PublicData as PublicData
    
    flag = "0"  # Production trading: 0, Demo trading: 1
    
    publicDataAPI = PublicData.PublicAPI(flag=flag)
    
    # Retrieve a list of instruments with open contracts
    result = publicDataAPI.get_instruments(
        instType="SPOT"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | Yes | Instrument type  
`SPOT`: Spot  
`MARGIN`: Margin  
`SWAP`: Perpetual Futures  
`FUTURES`: Expiry Futures  
`OPTION`: Option  
`EVENTS`: Event Contracts  
seriesId | String | Conditional | Series ID, e.g. `BTC-ABOVE-DAILY`. Required when instType is `EVENTS`  
instFamily | String | Conditional | Instrument family  
Only applicable to `FUTURES`/`SWAP`/`OPTION`. If instType is `OPTION`, `instFamily` is required.  
instId | String | No | Instrument ID  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
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
                "tradeQuoteCcyList": [
                    "USDT"
                ],
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
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instType | String | Instrument type  
seriesId | String | Series ID, e.g. `BTC-ABOVE-DAILY`. Only applicable to `EVENTS`  
instId | String | Instrument ID, e.g. `BTC-USD-SWAP`  
uly | String | Underlying, e.g. `BTC-USD`   
Only applicable to `MARGIN/FUTURES`/`SWAP`/`OPTION`  
groupId | String | Instrument trading fee group ID  
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
instFamily | String | Instrument family, e.g. `BTC-USD`   
Only applicable to `MARGIN/FUTURES`/`SWAP`/`OPTION`  
category | String | Currency category. Note: this parameter is already deprecated  
baseCcy | String | Base currency, e.g. `BTC` in`BTC-USDT`   
Only applicable to `SPOT`/`MARGIN`  
quoteCcy | String | Quote currency, e.g. `USDT` in `BTC-USDT`   
Only applicable to `SPOT`/`MARGIN`  
settleCcy | String | Settlement and margin currency, e.g. `BTC`   
Only applicable to `FUTURES`/`SWAP`/`OPTION`  
ctVal | String | Face value of one contract. Denomination depends on `ctType`: for linear contracts, `ctVal` is in the base currency (e.g., ctVal=0.01 BTC for BTC-USDT-SWAP); for inverse contracts, `ctVal` is in USD (e.g., ctVal=100 USD for BTC-USD-SWAP). Notional: linear = sz × ctVal × markPx (in quote ccy); inverse = sz × ctVal (in USD, fixed).   
Only applicable to `FUTURES`/`SWAP`/`OPTION`  
ctMult | String | Contract multiplier   
Only applicable to `FUTURES`/`SWAP`/`OPTION`  
ctValCcy | String | Contract value currency   
Only applicable to `FUTURES`/`SWAP`/`OPTION`  
optType | String | Option type, `C`: Call `P`: put   
Only applicable to `OPTION`  
stk | String | Strike price   
Only applicable to `OPTION`  
listTime | String | Listing time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
auctionEndTime | String | ~~The end time of call auction, Unix timestamp format in milliseconds, e.g.`1597026383085`   
Only applicable to `SPOT` that are listed through call auctions, return "" in other cases (deprecated, use contTdSwTime)~~  
contTdSwTime | String | Continuous trading switch time. The switch time from call auction, prequote to continuous trading, Unix timestamp format in milliseconds. e.g. `1597026383085`.  
Only applicable to `SPOT`/`MARGIN` that are listed through call auction or prequote, return "" in other cases.  
preMktSwTime | String | The time premarket swap switched to normal swap, Unix timestamp format in milliseconds, e.g. `1597026383085`.   
Only applicable premarket `SWAP`  
openType | String | Open type  
`fix_price`: fix price opening  
`pre_quote`: pre-quote  
`call_auction`: call auction   
Only applicable to `SPOT`/`MARGIN`, return "" for all other business lines  
expTime | String | Expiry time   
Applicable to `SPOT`/`MARGIN`/`FUTURES`/`SWAP`/`OPTION`. For `FUTURES`/`OPTION`, it is natural delivery/exercise time. It is the instrument offline time when there is `SPOT/MARGIN/FUTURES/SWAP/` manual offline. Update once change.  
lever | String | Exchange-defined maximum leverage ceiling for this instrument. The actual leverage available to a specific account may be lower based on VIP tier and position size. Use GET /api/v5/account/leverage-info for the user's current configured leverage.   
Not applicable to `SPOT`, `OPTION`  
tickSz | String | Minimum price increment, e.g. `0.0001`.  
For `OPTION`/`EVENTS`, it is the minimum tickSz among tick band. Use "Get instrument tick bands" endpoint with the corresponding `instType` for accurate tickSz per price range.  
lotSz | String | Lot size — the minimum order size increment. All order quantities (sz) must be a multiple of `lotSz`. Violation returns error 51121.  
If it is a derivatives contract, the value is the number of contracts.  
If it is `SPOT`/`MARGIN`, the value is the quantity in `base currency`.  
minSz | String | Minimum order size. Order size must satisfy both: sz ≥ `minSz` AND sz is a multiple of `lotSz`.  
If it is a derivatives contract, the value is the number of contracts.  
If it is `SPOT`/`MARGIN`, the value is the quantity in `base currency`.  
ctType | String | Contract type  
`linear`: linear contract — margin, P&L, and settlement in the quote currency (e.g., USDT for BTC-USDT-SWAP).  
`inverse`: inverse contract — margin, P&L, and settlement in the base currency (e.g., BTC for BTC-USD-SWAP). For inverse contracts, P&L in USD terms is non-linear: the USD value of a fixed BTC gain changes with the BTC price.   
Only applicable to `FUTURES`/`SWAP`  
alias | String | Contract alias (deprecated — use expTime to obtain the delivery time, will be removed by the end of April 2026)  
`this_week`  
`next_week`  
`this_month`  
`next_month`  
`quarter`  
`next_quarter`  
`third_quarter`  
`this_five_years`: current 5-year contract  
`next_five_years`: next 5-year contract  
Only applicable to `FUTURES`  
state | String | Instrument status  
`live`   
`suspend`  
`rebase`: can’t be traded during rebasing, only applicable to `SWAP`  
`post_only`: only post-only orders are accepted; existing post-only orders can be amended and cancelled. Other order types (market, IOC, FOK, normal limit) are rejected. Only applicable to `SWAP`  
`preopen`. e.g. There will be `preopen` before the Futures and Options new contracts state is live.  
`test`: Test pairs, can’t be traded  
`settling`: Settling, only applicable to `EVENTS`  
ruleType | String | Trading rule types  
`normal`: normal trading  
`pre_market`: pre-market trading  
`rebase_contract`: pre-market rebase contract  
`xperp`: perpetual-style futures, only applicable to certain `FUTURES` contracts  
maxLmtSz | String | The maximum order quantity of a single limit order.  
If it is a derivatives contract, the value is the number of contracts.  
If it is `SPOT`/`MARGIN`, the value is the quantity in `base currency`.  
maxMktSz | String | The maximum order quantity of a single market order.  
If it is a derivatives contract, the value is the number of contracts.  
If it is `SPOT`/`MARGIN`, the value is the quantity in `USDT`.  
maxLmtAmt | String | Max USD amount for a single limit order  
maxMktAmt | String | Max USD amount for a single market order   
Only applicable to `SPOT`/`MARGIN`  
maxTwapSz | String | The maximum order quantity of a single TWAP order.  
If it is a derivatives contract, the value is the number of contracts.  
If it is `SPOT`/`MARGIN`, the value is the quantity in `base currency`.   
The minimum order quantity of a single TWAP order is minSz*2  
maxIcebergSz | String | The maximum order quantity of a single iceBerg order.  
If it is a derivatives contract, the value is the number of contracts.  
If it is `SPOT`/`MARGIN`, the value is the quantity in `base currency`.  
maxTriggerSz | String | The maximum order quantity of a single trigger order.  
If it is a derivatives contract, the value is the number of contracts.  
If it is `SPOT`/`MARGIN`, the value is the quantity in `base currency`.  
maxStopSz | String | The maximum order quantity of a single stop market order.  
If it is a derivatives contract, the value is the number of contracts.  
If it is `SPOT`/`MARGIN`, the value is the quantity in `USDT`.  
futureSettlement | Boolean | Whether daily settlement for expiry feature is enabled  
Applicable to `FUTURES` `cross`  
tradeQuoteCcyList | Array of strings | List of quote currencies available for trading, e.g. ["USD", "USDC”].  
instIdCode | Integer | Instrument ID code.   
For simple binary encoding, you must use `instIdCode` instead of `instId`.  
For the same `instId`, it's value may be different between production and demo trading.   
It is `null` when the value is not generated.  
instCategory | String | The asset category of the instrument’s base asset (the first segment of the instrument ID). For example, for `BTC-USDT-SWAP`, the `instCategory` represents the asset category of `BTC`.   
`1`: Crypto   
`3`: Stocks   
`4`: Commodities   
`5`: Forex   
`6`: Bonds   
`""`: Not available  
initPxLmtPct | String | Initial price-limit band applied during the first 10 minutes after contract listing, e.g. `0.05` represents 5%. Use GET /api/v5/public/price-limit for the computed price limits.  
Only applicable to `SPOT`/`MARGIN`/`SWAP`/`FUTURES`, returns `""` for `OPTION` and `EVENTS`.  
floatPxLmtPct | String | Floating price-limit band during normal trading, e.g. `0.03` represents 3%. Use GET /api/v5/public/price-limit for the computed price limits.  
Only applicable to `SPOT`/`MARGIN`/`SWAP`/`FUTURES`, returns `""` for `OPTION` and `EVENTS`.  
maxPxLmtPct | String | Maximum price-limit cap (hard ceiling on order-price deviation from the index price), e.g. `0.15` represents 15%. Use GET /api/v5/public/price-limit for the computed price limits.  
Only applicable to `SPOT`/`MARGIN`/`SWAP`/`FUTURES`, returns `""` for `OPTION` and `EVENTS`.  
upcChg | Array of objects | Upcoming changes. It is [] when there is no upcoming change.  
> param | String | The parameter name to be updated.   
`tickSz`  
`minSz`: For `FUTURES`/`SWAP`, `lotSz` will be modified synchronously.  
`maxMktSz`  
> newValue | String | The parameter value that will replace the current one.  
> effTime | String | Effective time. Unix timestamp format in milliseconds, e.g. `1597026383085`  
When a new contract is going to be listed, the instrument data of the new contract will be available with status preopen. When a product is going to be delisted (e.g. when a FUTURES contract is settled or OPTION contract is exercised), the instrument will not be available   
listTime and contTdSwTime  
For spot symbols listed through a call auction or pre-open, listTime represents the start time of the auction or pre-open, and contTdSwTime indicates the end of the auction or pre-open and the start of continuous trading. For other scenarios, listTime will mark the beginning of continuous trading, and contTdSwTime will return an empty value "".  state  
For `SPOT`, `MARGIN`, `SWAP`, and `FUTURES`, the state changes from `preopen` to `live` when the `listTime` is reached. For `OPTION` contracts, the state may change to `live` slightly after `listTime` due to internal processing. It is recommended to verify that `state` is `live` before placing orders.  
When a product is going to be delisted (e.g. when a FUTURES contract is settled or OPTION contract is exercised), the instrument will not be available.  Instruments REST endpoints and WebSocket channel will update `expTime` once the delisting announcement is published.  
Instruments REST endpoint and WebSocket channel will update `listTime` once the listing announcement is published:  
1\. For `SPOT/MARGIN/SWAP`, this event is only applicable to `instType`, `instId`, `listTime`, `state`.  
2\. For `FUTURES`, this event is only applicable to `instType`, `instFamily`, `listTime`, `state`.  
3\. Other fields will be "" temporarily, but they will be updated at least 5 minutes in advance of the `listTime`, then the WebSocket subscription using related `instId`/`instFamily` can be available.

---

# 获取交易产品基础信息

获取所有可交易产品的信息列表。  
  
#### 限速：20次/2s

#### 限速规则：IP + Instrument Type

#### HTTP请求

`GET /api/v5/public/instruments`

> 请求示例
    
    
    GET /api/v5/public/instruments?instType=SPOT
    
    
    
    import okx.PublicData as PublicData
    
    flag = "0"  # 实盘:0 , 模拟盘：1
    
    publicDataAPI = PublicData.PublicAPI(flag=flag)
    
    # 获取交易产品基础信息
    result = publicDataAPI.get_instruments(
        instType="SPOT"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 是 | 产品类型  
`SPOT`：币币  
`MARGIN`：币币杠杆  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`OPTION`：期权  
`EVENTS`：事件合约  
seriesId | String | 可选 | 系列 ID，如 `BTC-ABOVE-DAILY`。当 `instType` 为 `EVENTS` 时必填  
instFamily | String | 否 | 交易品种，仅适用于`交割`/`永续`/`期权`  
instId | String | 否 | 产品ID  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
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
                "tradeQuoteCcyList": [
                    "USDT"
                ],
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
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
instType | String | 产品类型  
seriesId | String | 系列 ID，如 `BTC-ABOVE-DAILY`。仅适用于 `EVENTS`  
instId | String | 产品id， 如 `BTC-USDT`  
uly | String | 标的指数，如 `BTC-USD`，仅适用于`杠杆/交割/永续/期权`  
groupId | String | 交易产品手续费分组ID  
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
instFamily | String | 交易品种，如 `BTC-USD`，仅适用于`杠杆/交割/永续/期权`  
category | String | ~~币种类别~~ （已废弃）  
baseCcy | String | 交易货币币种，如 `BTC-USDT` 中的 `BTC` ，仅适用于`币币/币币杠杆`  
quoteCcy | String | 计价货币币种，如 `BTC-USDT` 中的`USDT` ，仅适用于`币币/币币杠杆`  
settleCcy | String | 盈亏结算和保证金币种，如 `BTC` 仅适用于`交割`/`永续`/`期权`  
ctVal | String | 每张合约的面值。计价货币取决于 `ctType`：线性合约以标的货币计（如BTC-USDT-SWAP，ctVal=0.01 BTC）；反向合约以USD计（如BTC-USD-SWAP，ctVal=100 USD）。名义价值：线性 = 张数 × ctVal × 标记价格（计价货币）；反向 = 张数 × ctVal（USD固定）。  
仅适用于 `FUTURES`/`SWAP`/`OPTION`  
ctMult | String | 合约乘数，仅适用于`交割`/`永续`/`期权`  
ctValCcy | String | 合约面值计价币种，仅适用于`交割`/`永续`/`期权`  
optType | String | 期权类型，`C`或`P` 仅适用于`期权`  
stk | String | 行权价格，仅适用于`期权`  
listTime | String | 上线时间   
Unix时间戳的毫秒数格式，如 `1597026383085`  
auctionEndTime | String | ~~集合竞价结束时间，Unix时间戳的毫秒数格式，如`1597026383085`   
仅适用于通过集合竞价方式上线的`币币`，其余情况返回""（已废弃，请使用contTdSwTime）~~  
contTdSwTime | String | 连续交易开始时间，从集合竞价、提前挂单切换到连续交易的时间，Unix时间戳格式，单位为毫秒。e.g. `1597026383085`。  
仅适用于通过集合竞价或提前挂单上线的`SPOT`/`MARGIN`，在其他情况下返回""。  
preMktSwTime | String | 盘前永续合约转为普通永续合约的时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
仅适用于盘前`SWAP`  
openType | String | 开盘类型  
`fix_price`: 定价开盘  
`pre_quote`: 提前挂单  
`call_auction`: 集合竞价   
只适用于`SPOT`/`MARGIN`，其他业务线返回""  
expTime | String | 产品下线时间  
适用于`币币/杠杆/交割/永续/期权`，对于 `交割/期权`，为交割/行权日期；亦可以为产品下线时间，有变动就会推送。  
lever | String | 交易所对该合约设定的最大杠杆上限。账户实际可用杠杆可能因VIP等级和仓位大小而更低。用户当前配置的杠杆请使用 GET /api/v5/account/leverage-info 查询。  
不适用于 `SPOT`、`OPTION`  
tickSz | String | 最小价格变动单位，如 `0.0001`。  
对于 `OPTION`/`EVENTS`，该值为 tick band 中的最小 tickSz。如需获取各价格区间的精确 tickSz，请使用"获取期权价格梯度"接口并传入对应的 `instType` 参数。  
lotSz | String | 合约面值最小变动单位（委托量步长），所有委托量（sz）必须为 `lotSz` 的整数倍，违反则返回错误51121。下单数量精度  
合约的数量单位是`张`，现货的数量单位是`交易货币`  
minSz | String | 最小委托量。委托量必须同时满足：sz ≥ `minSz` 且 sz 为 `lotSz` 的整数倍。最小下单数量  
合约的数量单位是`张`，现货的数量单位是`交易货币`  
ctType | String | 合约类型  
`linear`：正向合约，保证金、盈亏及结算均以计价货币计（如BTC-USDT-SWAP以USDT计）。  
`inverse`：反向合约，保证金、盈亏及结算均以标的货币计（如BTC-USD-SWAP以BTC计）。反向合约的USD盈亏为非线性：固定BTC盈亏的USD价值随BTC价格变化。  
仅适用于 `FUTURES`/`SWAP`  
alias | String | 合约日期别名（已废弃，将于 2026 年 4 月底下线，请使用 expTime 字段获取交割时间）  
`this_week`：本周  
`next_week`：次周  
`this_month`：本月  
`next_month`：次月  
`quarter`：季度  
`next_quarter`：次季度  
`third_quarter`：第三季度  
`this_five_years`：当期五年合约  
`next_five_years`：次期五年合约  
仅适用于`交割`  
state | String | 产品状态  
`live`：交易中   
`suspend`：暂停中  
`rebase`：合约在变基中，不可交易，仅适用于`SWAP`  
`post_only`：仅接受 post-only 订单；已有 post-only 订单可改单和撤单。其他订单类型（市价单、IOC、FOK、普通限价单）将被拒绝。仅适用于 `SWAP`  
`preopen`：预上线，交割和期权合约轮转生成到开始交易；部分交易产品上线前  
`test`：测试中（测试产品，不可交易）  
`settling`：结算中，仅适用于 `EVENTS`  
ruleType | String | 交易规则类型  
`normal`：普通交易  
`pre_market`：盘前交易  
`rebase_contract`：盘前变基合约  
`xperp`：永续合约风格的交割合约，仅适用于部分 `FUTURES` 合约  
maxLmtSz | String | 限价单的单笔最大委托数量  
合约的数量单位是`张`，现货的数量单位是`交易货币`  
maxMktSz | String | 市价单的单笔最大委托数量  
合约的数量单位是`张`，现货的数量单位是`USDT`  
maxLmtAmt | String | 限价单的单笔最大美元价值  
maxMktAmt | String | 市价单的单笔最大美元价值  
仅适用于`币币/币币杠杆`  
maxTwapSz | String | 时间加权单的单笔最大委托数量  
合约的数量单位是`张`，现货的数量单位是`交易货币`。  
单笔最小委托数量为 minSz*2  
maxIcebergSz | String | 冰山委托的单笔最大委托数量  
合约的数量单位是`张`，现货的数量单位是`交易货币`  
maxTriggerSz | String | 计划委托委托的单笔最大委托数量  
合约的数量单位是`张`，现货的数量单位是`交易货币`  
maxStopSz | String | 止盈止损市价委托的单笔最大委托数量  
合约的数量单位是`张`，现货的数量单位是`USDT`  
futureSettlement | Boolean | 交割合约是否支持每日结算  
适用于`全仓``交割`  
tradeQuoteCcyList | Array of strings | 可用于交易的计价币种列表，如 ["USD", "USDC”].  
instIdCode | Integer | 产品唯一标识代码。  
对于简单二进制编码，您必须使用 `instIdCode` 而不是 `instId`。  
对于同一`instId`，实盘和模拟盘的值可能会不一样。   
当值还未生成时，返回 `null`。  
instCategory | String | 标的资产类别（产品ID的第一部分）。例如：对于 `BTC-USDT-SWAP`，instCategory 表示 `BTC` 所属的资产类别。  
`1`: 加密货币   
`3`: 股票类资产   
`4`: 大宗商品   
`5`: 外汇   
`6`: 债券   
`""` 当值不可用时返回空字符串  
initPxLmtPct | String | 合约上线后前 10 分钟内的初始价格限制区间，小数百分比，例如 `0.05` 代表 5%。通过 GET /api/v5/public/price-limit 可获取对应价格限制。  
适用于 `SPOT`/`MARGIN`/`SWAP`/`FUTURES`；`OPTION` 和 `EVENTS` 返回 `""`。  
floatPxLmtPct | String | 常规交易期间的浮动价格限制区间，小数百分比，例如 `0.03` 代表 3%。通过 GET /api/v5/public/price-limit 可获取对应价格限制。  
适用于 `SPOT`/`MARGIN`/`SWAP`/`FUTURES`；`OPTION` 和 `EVENTS` 返回 `""`。  
maxPxLmtPct | String | 最大价格限制上限（下单价格相对指数价格偏离的硬性上限），小数百分比，例如 `0.15` 代表 15%。通过 GET /api/v5/public/price-limit 可获取对应价格限制。  
适用于 `SPOT`/`MARGIN`/`SWAP`/`FUTURES`；`OPTION` 和 `EVENTS` 返回 `""`。  
upcChg | Array of objects | 即将变更的参数列表。当没有即将变更的参数时，返回空数组 []  
> param | String | 即将变更的参数名称。  
`tickSz`  
`minSz`：若为交割/永续合约（`FUTURES`/`SWAP`），`lotSz` 会同步变更。  
`maxMktSz`  
> newValue | String | 即将变更的参数值。  
> effTime | String | 生效时间。Unix 时间戳格式，例如 `1597026383085`  
当合约预上线时，状态变更为预上线（即新生成一个合约，新合约会处于预上线状态）；  listTime以及contTdSwTime  
对于通过集合竞价/提前挂单方式上线的币币，listTime为集合竞价/提前挂单的开始时间，contTdSwTime为集合竞价/提前挂单的结束时间、连续交易的开始时间；对于其他情况及业务线，listTime即为连续交易开始时间，contTdSwTime将返回""  state  
对于`币币`、`杠杆`、`永续`和`交割`，状态state在时间到达listTime时由`preopen`转变为`live`。对于`期权`合约，由于内部处理原因，状态可能在`listTime`之后短暂延迟变为`live`。建议在下单前确认`state`为`live`。  
当产品下线的时候（如交割合约被交割的时候，期权合约被行权的时候），查询不到该产品  产品下线公告一经发出，接口及频道会更新下线时间(expTime)。  
产品上线公告一经发出，接口及频道会更新上线时间：  
1\. 对于币币/杠杆/永续， 该事件仅适用于产品类型(instType), 交易产品ID(instId), 上线时间(listTime), 产品状态(state)字段；  
2\. 对于交割，该事件仅适用于产品类型(instType), 交易品种(instFamily), 上线时间(listTime), 产品状态(state)字段；  
3\. 其他字段暂时为空，会比上线时间至少提前 5 分钟更新完整，然后 WebSocket 才会支持通过对应的交易产品ID/交易品种进行订阅。