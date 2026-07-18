---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#trading-account-rest-api-get-instruments
anchor_id: trading-account-rest-api-get-instruments
api_type: REST
updated_at: 2026-07-18 20:02:50.107814
---

# Get instruments

Retrieve available instruments info of current account.  
  
#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID + Instrument Type

#### HTTP Request

`GET /api/v5/account/instruments`

> Request Example
    
    
    GET /api/v5/account/instruments?instType=SPOT
    
    
    
    import okx.Account as Account
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1" # Production trading: 0, Demo trading: 1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    result = accountAPI.get_instruments(instType="SPOT")
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
        "code": "0",
        "data": [
            {
                "auctionEndTime": "",
                "baseCcy": "BTC",
                "ctMult": "",
                "ctType": "",
                "ctVal": "",
                "ctValCcy": "",
                "contTdSwTime": "1704876947000",
                "elp": "0",
                "expTime": "",
                "futureSettlement": false,
                "groupId": "4",
                "instFamily": "",
                "instId": "BTC-EUR",
                "instType": "SPOT",
                "lever": "",
                "listTime": "1704876947000",
                "lotSz": "0.00000001",
                "maxIcebergSz": "9999999999.0000000000000000",
                "maxLmtAmt": "1000000",
                "maxLmtSz": "9999999999",
                "maxMktAmt": "1000000",
                "maxMktSz": "1000000",
                "maxPlatOILmt": "1000000000",
                "maxPlatOICoinLmt": "",
                "maxStopSz": "1000000",
                "maxTriggerSz": "9999999999.0000000000000000",
                "maxTwapSz": "9999999999.0000000000000000",
                "minSz": "0.00001",
                "optType": "",
                "openType": "call_auction",
                "preMktSwTime": "",
                "posLmtPct": "30",
                "posLmtAmt": "2500000",
                "quoteCcy": "EUR",
                "tradeQuoteCcyList": [
                    "EUR"
                ],
                "settleCcy": "",
                "state": "live",
                "ruleType": "normal",
                "stk": "",
                "tickSz": "1",
                "uly": "",
                "instIdCode": 1000000000,   
                "instCategory": "1",
                "initPxLmtPct": "0.05",
                "floatPxLmtPct": "0.03",
                "maxPxLmtPct": "0.15",
                "upcChg": [
                    {
                        "param": "tickSz",
                        "newValue": "0.0001",
                        "effTime": "1704876947000"
                    }
                ]
            }
        ],
        "msg": ""
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
`3`: Spot TRY  
`5`: Spot BRL  
`7`: Spot AED  
`8`: Spot AUD  
`10`: Spot SGD  
`11`: Spot zero  
`12`: Spot group one  
`13`: Spot group two  
`14`: Spot group three  
`15`: Spot special rule  
`17`: Spot stablecoin  
  
Expiry futures:  
`5`: Expiry futures group one  
`6`: Expiry futures group two  
`8`: XPERP group two  
`10`: XPERP RWA group two  
  
Perpetual futures:  
`4`: Perpetual futures group one  
`5`: Perpetual futures group two  
`6`: SWAP RWA group one  
`7`: SWAP RWA group two  
  
Options:  
`1`: Options crypto-margined  
  
**instType and groupId should be used together to determine a trading fee group. Users should use this endpoint together with[fee rates endpoint](/docs-v5/en/#trading-account-rest-api-get-fee-rates) to get the trading fee of a specific symbol.**   
  
**Some enum values may not apply to you; the actual return values shall prevail.**  
instFamily | String | Instrument family, e.g. `BTC-USD`   
Only applicable to `MARGIN/FUTURES`/`SWAP`/`OPTION`  
baseCcy | String | Base currency, e.g. `BTC` in`BTC-USDT`   
Only applicable to `SPOT`/`MARGIN`  
quoteCcy | String | Quote currency, e.g. `USDT` in `BTC-USDT`   
Only applicable to `SPOT`/`MARGIN`  
settleCcy | String | Settlement and margin currency, e.g. `BTC`   
Only applicable to `FUTURES`/`SWAP`/`OPTION`  
ctVal | String | Contract value   
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
preMktSwTime | String | The time a pre-market instrument switched to normal trading, Unix timestamp format in milliseconds, e.g. `1597026383085`.   
Only applicable to pre-market `SWAP` and pre-market X-Perp `FUTURES`. Populated when a pre-market X-Perp converts to a normal X-Perp  
openType | String | Open type  
`fix_price`: fix price opening  
`pre_quote`: pre-quote  
`call_auction`: call auction   
Only applicable to `SPOT`/`MARGIN`, return "" for all other business lines  
elp | String | ELP maker permission  
`0`: ELP is not enabled for this symbol  
`1`: ELP is enabled for this symbol, but current users don't have permission to place ELP orders for it.   
`2`: ELP is enabled for this symbol, and current users have permission to place ELP orders for it.   
  
It doesn't mean there will be ELP liquidity when elp is `1/2`.  
expTime | String | Expiry time   
Applicable to `SPOT`/`MARGIN`/`FUTURES`/`SWAP`/`OPTION`. For `FUTURES`/`OPTION`, it is natural delivery/exercise time. It is the instrument offline time when there is `SPOT/MARGIN/FUTURES/SWAP/` manual offline. Update once change.  
lever | String | Max Leverage,   
Not applicable to `SPOT`, `OPTION`  
tickSz | String | Tick size, e.g. `0.0001`.  
For `OPTION`/`EVENTS`, it is the minimum tickSz among tick band. Use "Get instrument tick bands" endpoint with the corresponding `instType` for accurate tickSz per price range.  
lotSz | String | Lot size  
If it is a derivatives contract, the value is the number of contracts.  
If it is `SPOT`/`MARGIN`, the value is the quantity in `base currency`.  
minSz | String | Minimum order size  
If it is a derivatives contract, the value is the number of contracts.  
If it is `SPOT`/`MARGIN`, the value is the quantity in `base currency`.  
ctType | String | Contract type  
`linear`: linear contract  
`inverse`: inverse contract   
Only applicable to `FUTURES`/`SWAP`  
state | String | Instrument status  
`live`   
`suspend`  
`rebase`: can't be traded during rebasing, only applicable to `SWAP`  
`post_only`: only post-only orders are accepted; existing post-only orders can be amended and cancelled. Other order types (market, IOC, FOK, normal limit) are rejected. Only applicable to `SWAP`  
`preopen` e.g. Futures and options contracts rollover from generation to trading start; certain symbols before they go live  
`test`: Test pairs, can't be traded  
`settling`: Settling, only applicable to `EVENTS`  
ruleType | String | Trading rule types  
`normal`: normal trading  
`pre_market`: pre-market trading, including pre-market X-Perp `FUTURES`  
`rebase_contract`: pre-market rebase contract  
`xperp`: perpetual-style futures, only applicable to certain `FUTURES` contracts. A pre-market X-Perp changes from `pre_market` to `xperp` after it converts to a normal X-Perp  
posLmtAmt | String | Maximum position value (USD) for this instrument at the user level (shared across master and sub-accounts), based on the notional value of all same-direction open positions and resting orders. The effective user limit is max(posLmtAmt, oiUSD × posLmtPct). Applicable to `SWAP`/`FUTURES`.  
posLmtPct | String | Maximum position ratio (e.g., 30 for 30%) a user (shared across master and sub-accounts) may hold relative to the platform's current total position value. The effective user limit is max(posLmtAmt, oiUSD × posLmtPct). Applicable to `SWAP`/`FUTURES`.  
maxPlatOILmt | String | Platform-wide maximum position value (USD) for this instrument. If the platform total open interest (USD) reaches or exceeds this value, all users’ new opening orders for this instrument are rejected; otherwise, orders pass.  
Applicable to `SWAP`/`FUTURES`  
maxPlatOICoinLmt | String | Platform-wide maximum position value (coins) for this instrument. If the platform total open interest (coins) reaches or exceeds this value, all users’ new opening orders for this instrument are rejected; otherwise, orders pass.  
Applicable to `SWAP`/`FUTURES`  
longPosRemainingQuota | String | The remaining long position value (USD) the user is permitted to open, netting all existing long positions and resting buy orders. The quota is shared across the master account and all subaccounts.  
shortPosRemainingQuota | String | The remaining short position value (USD) the user is permitted to open, netting all existing short positions and resting sell orders. The quota is shared across the master account and all subaccounts.  
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
tradeQuoteCcyList | Array of strings | List of quote currencies available for trading, e.g. ["USD", "USDC"].  
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
listTime and contTdSwTime  
For spot symbols listed through a call auction or pre-open, listTime represents the start time of the auction or pre-open, and contTdSwTime indicates the end of the auction or pre-open and the start of continuous trading. For other scenarios, listTime will mark the beginning of continuous trading, and contTdSwTime will return an empty value "".  state  
For `SPOT`, `MARGIN`, `SWAP`, and `FUTURES`, the state changes from `preopen` to `live` when the `listTime` is reached. For `OPTION` contracts, the state may change to `live` slightly after `listTime` due to internal processing. It is recommended to verify that `state` is `live` before placing orders.  
When a product is going to be delisted (e.g. when a FUTURES contract is settled or OPTION contract is exercised), the instrument will not be available.

---

# 获取交易产品基础信息

获取当前账户可交易产品的信息列表。  
  
#### 限速：20次/2s

#### 限速规则：User ID + Instrument Type

#### HTTP请求

`GET /api/v5/account/instruments`

> 请求示例
    
    
    GET /api/v5/account/instruments?instType=SPOT
    
    
    
    import okx.Account as Account
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    result = accountAPI.get_instruments(instType="SPOT")
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
seriesId | String | 可选 | 系列 ID，如 `BTC-ABOVE-DAILY`。当 instType 为 `EVENTS` 时必填  
instFamily | String | 可选 | 交易品种，仅适用于`交割`/`永续`/`期权`，期权必填  
instId | String | 否 | 产品ID  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "auctionEndTime": "",
                "baseCcy": "BTC",
                "ctMult": "",
                "ctType": "",
                "ctVal": "",
                "ctValCcy": "",
                "contTdSwTime": "1704876947000",
                "elp": "0",
                "expTime": "",
                "futureSettlement": false,
                "groupId": "4",
                "instFamily": "",
                "instId": "BTC-EUR",
                "instType": "SPOT",
                "lever": "",
                "listTime": "1704876947000",
                "lotSz": "0.00000001",
                "maxIcebergSz": "9999999999.0000000000000000",
                "maxLmtAmt": "1000000",
                "maxLmtSz": "9999999999",
                "maxMktAmt": "1000000",
                "maxMktSz": "1000000",
                "maxPlatOILmt": "1000000000",
                "maxPlatOICoinLmt": "",
                "maxStopSz": "1000000",
                "maxTriggerSz": "9999999999.0000000000000000",
                "maxTwapSz": "9999999999.0000000000000000",
                "minSz": "0.00001",
                "optType": "",
                "openType": "call_auction",
                "preMktSwTime": "",
                "posLmtPct": "30",
                "posLmtAmt": "2500000",
                "quoteCcy": "EUR",
                "tradeQuoteCcyList": [
                    "EUR"
                ],
                "settleCcy": "",
                "state": "live",
                "ruleType": "normal",
                "stk": "",
                "tickSz": "1",
                "uly": "",
                "instIdCode": 1000000000,
                "instCategory": "1",
                "initPxLmtPct": "0.05",
                "floatPxLmtPct": "0.03",
                "maxPxLmtPct": "0.15",
                "upcChg": [
                    {
                        "param": "tickSz",
                        "newValue": "0.0001",
                        "effTime": "1704876947000"
                    }
                ]
            }
        ],
        "msg": ""
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
`3`：TRY现货  
`5`：BRL现货  
`7`：AED现货  
`8`：AUD现货  
`10`：SGD现货  
`11`：零手续费现货  
`12`：现货分组一  
`13`：现货分组二  
`14`：现货分组三  
`15`: 现货特别分组  
`17`：现货稳定币分组  
  
交割合约：  
`5`：交割合约分组一  
`6`：交割合约分组二  
`8`：XPERP分组二  
`10`：XPERP RWA分组二  
  
永续合约：  
`4`：永续合约分组一  
`5`：永续合约分组二  
`6`：SWAP RWA分组一  
`7`：SWAP RWA分组二  
  
期权：  
`1`：币本位期权  
  
**用户需要同时使用instType和groupId来确定一个交易产品的交易手续费分组；用户应该将此接口和[获取当前账户交易手续费费率](/docs-v5/zh/#trading-account-rest-api-get-fee-rates)一起使用，以获取特定交易产品的手续费率**   
  
**部分枚举值可能不适用于您，以实际返回为准**  
instFamily | String | 交易品种，如 `BTC-USD`，仅适用于`杠杆/交割/永续/期权`  
baseCcy | String | 交易货币币种，如 `BTC-USDT` 中的 `BTC` ，仅适用于`币币/币币杠杆`  
quoteCcy | String | 计价货币币种，如 `BTC-USDT` 中的`USDT` ，仅适用于`币币/币币杠杆`  
settleCcy | String | 盈亏结算和保证金币种，如 `BTC` 仅适用于`交割`/`永续`/`期权`  
ctVal | String | 合约面值，仅适用于`交割`/`永续`/`期权`  
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
preMktSwTime | String | 盘前交易产品切换为正常交易的时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
仅适用于盘前`SWAP` 与盘前 X-Perp `FUTURES`。当盘前 X-Perp 转换为正常 X-Perp 时填充  
openType | String | 开盘类型  
`fix_price`: 定价开盘  
`pre_quote`: 提前挂单  
`call_auction`: 集合竞价   
只适用于`SPOT`/`MARGIN`，其他业务线返回""  
elp | String | ELP 下单权限  
`0`：该币对不支持 ELP  
`1`：该币对支持 ELP 但用户没有权限为其下 ELP 订单  
`2`：该币对支持 ELP 且用户有权限为其下 ELP 订单  
  
`1/2`不代表深度中一定有 ELP 挂单  
expTime | String | 产品下线时间  
适用于`币币/杠杆/交割/永续/期权`，对于 `交割/期权`，为交割/行权日期；亦可以为产品下线时间，有变动就会推送。  
lever | String | 该`instId`支持的最大杠杆倍数，不适用于`币币`、`期权`  
tickSz | String | 下单价格精度，如 `0.0001`。  
对于 `OPTION`/`EVENTS`，该值为 tick band 中的最小 tickSz。如需获取各价格区间的精确 tickSz，请使用"获取期权价格梯度"接口并传入对应的 `instType` 参数。  
lotSz | String | 下单数量精度  
合约的数量单位是`张`，现货的数量单位是`交易货币`  
minSz | String | 最小下单数量  
合约的数量单位是`张`，现货的数量单位是`交易货币`  
ctType | String | 合约类型  
`linear`：正向合约  
`inverse`：反向合约  
仅适用于`交割/永续`  
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
`pre_market`：盘前交易，含盘前 X-Perp `FUTURES`  
`rebase_contract`：盘前变基合约  
`xperp`：永续合约风格的交割合约，仅适用于部分 `FUTURES` 合约。盘前 X-Perp 转换为正常 X-Perp 后，由 `pre_market` 变为 `xperp`  
posLmtAmt | String | 单一用户（母子账户共享）层面的该产品最大持仓名义价值（USD），按同方向已持仓与挂单的美元名义价值计算。单用户有效上限为 max(posLmtAmt, oiUSD × posLmtPct)。适用于 `SWAP`/`FUTURES`。  
posLmtPct | String | 单一用户（母子账户共享）相对于平台当前总持仓名义价值可持有的最大比例（如 30 表示 30%）。单用户有效上限为 max(posLmtAmt, oiUSD × posLmtPct)。适用于 `SWAP`/`FUTURES`。  
maxPlatOILmt | String | 该产品的全平台最大持仓名义价值（USD）。当平台总持仓量（USD）达到或超过该值时，系统将拒绝所有用户对该产品的新开仓委托；否则订单通过校验。  
适用于 `SWAP`/`FUTURES`  
maxPlatOICoinLmt | String | 该产品的全平台最大持仓名义价值（币量）。当平台总持仓量（币量）达到或超过该值时，系统将拒绝所有用户对该产品的新开仓委托；否则订单通过校验。  
适用于 `SWAP`/`FUTURES`  
longPosRemainingQuota | String | 单一用户维度（母子账户共享），在该产品下扣除已有多头仓位及挂单中的买入订单后，仍可开立的多头仓位剩余额度（以 USD 计）。  
shortPosRemainingQuota | String | 单一用户维度（母子账户共享），在该产品下扣除已有空头仓位及挂单中的卖出订单后，仍可开立的空头仓位剩余额度（以 USD 计）。  
maxLmtSz | String | 限价单的单笔最大委托数量  
合约的数量单位是`张`，现货的数量单位是`交易货币`  
maxMktSz | String | 市价单的单笔最大委托数量  
合约的数量单位是`张`，现货的数量单位是`USDT`  
maxLmtAmt | String | 限价单的单笔最大美元价值  
maxMktAmt | String | 市价单的单笔最大美元价值  
仅适用于`币币/币币杠杆`  
maxTwapSz | String | 时间加权单的单笔最大委托数量  
合约的数量单位是`张`，现货的数量单位是`交易货币`   
单笔最小委托数量为 minSz*2  
maxIcebergSz | String | 冰山委托的单笔最大委托数量  
合约的数量单位是`张`，现货的数量单位是`交易货币`  
maxTriggerSz | String | 计划委托委托的单笔最大委托数量  
合约的数量单位是`张`，现货的数量单位是`交易货币`  
maxStopSz | String | 止盈止损市价委托的单笔最大委托数量  
合约的数量单位是`张`，现货的数量单位是`USDT`  
futureSettlement | Boolean | 交割合约是否支持每日结算  
适用于`全仓``交割`  
tradeQuoteCcyList | Array of strings | 可用于交易的计价币种列表，如 ["USD", "USDC"].  
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
listTime以及contTdSwTime  
对于通过集合竞价/提前挂单方式上线的币币，listTime为集合竞价/提前挂单的开始时间，contTdSwTime为集合竞价/提前挂单的结束时间、连续交易的开始时间；对于其他情况及业务线，listTime即为连续交易开始时间，contTdSwTime将返回""  state  
对于`币币`、`杠杆`、`永续`和`交割`，状态state在时间到达listTime时由`preopen`转变为`live`。对于`期权`合约，由于内部处理原因，状态可能在`listTime`之后短暂延迟变为`live`。建议在下单前确认`state`为`live`。  
当产品下线的时候（如交割合约被交割的时候，期权合约被行权的时候），查询不到该产品