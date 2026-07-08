---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-trade-get-order-details
anchor_id: order-book-trading-trade-get-order-details
api_type: API
updated_at: 2026-07-08 19:27:21.735734
---

# GET / Order details

Retrieve order details.

#### Rate Limit: 60 requests per 2 seconds

#### Rate limit rule (except Options): User ID + Instrument ID

#### Rate limit rule (Options only): User ID + Instrument Family

#### Permission: Read

#### HTTP Request

`GET /api/v5/trade/order`

> Request Example
    
    
    GET /api/v5/trade/order?ordId=1753197687182819328&instId=BTC-USDT
    
    
    
    
    import okx.Trade as Trade
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading: 0, Demo trading: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)
    
    # Retrieve order details by ordId
    result = tradeAPI.get_order(
        instId="BTC-USDT",
        ordId="680800019749904384"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instId | String | Yes | Instrument ID, e.g. `BTC-USDT`  
Only applicable to live instruments  
ordId | String | Conditional | Order ID   
Either `ordId` or `clOrdId` is required, if both are passed, `ordId` will be used  
clOrdId | String | Conditional | Client Order ID as assigned by the client  
If the `clOrdId` is associated with multiple orders, only the latest one will be returned.  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "accFillSz": "0.00192834",
                "algoClOrdId": "",
                "algoId": "",
                "attachAlgoClOrdId": "",
                "attachAlgoOrds": [],
                "avgPx": "51858",
                "cTime": "1708587373361",
                "cancelSource": "",
                "cancelSourceReason": "",
                "category": "normal",
                "ccy": "",
                "clOrdId": "",
                "fee": "-0.00000192834",
                "feeCcy": "BTC",
                "fillPx": "51858",
                "fillSz": "0.00192834",
                "fillTime": "1708587373361",
                "instId": "BTC-USDT",
                "instType": "SPOT",
                "isTpLimit": "false",
                "lever": "",
                "linkedAlgoOrd": {
                    "algoId": ""
                },
                "ordId": "680800019749904384",
                "ordType": "market",
                "pnl": "0",
                "posSide": "net",
                "px": "",
                "pxType": "",
                "pxUsd": "",
                "pxVol": "",
                "quickMgnType": "",
                "rebate": "0",
                "rebateCcy": "USDT",
                "reduceOnly": "false",
                "side": "buy",
                "slOrdPx": "",
                "slTriggerPx": "",
                "slTriggerPxType": "",
                "source": "",
                "state": "filled",
                "stpId": "",
                "stpMode": "",
                "sz": "100",
                "tag": "",
                "tdMode": "cash",
                "tgtCcy": "quote_ccy",
                "tpOrdPx": "",
                "tpTriggerPx": "",
                "tpTriggerPxType": "",
                "tradeId": "744876980",
                "tradeQuoteCcy": "USDT",
                "uTime": "1708587373362"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instType | String | Instrument type  
`SPOT`  
`MARGIN`  
`SWAP`  
`FUTURES`  
`OPTION`  
`EVENTS`  
instId | String | Instrument ID  
tgtCcy | String | Order quantity unit setting for `sz`  
`base_ccy`: Base currency ,`quote_ccy`: Quote currency   
Only applicable to `SPOT` Market Orders  
Default is `quote_ccy` for buy, `base_ccy` for sell  
ccy | String | Margin currency   
Applicable to all `isolated` `MARGIN` orders and `cross` `MARGIN` orders in `Futures mode`, `FUTURES` and `SWAP` contracts.  
ordId | String | Order ID  
clOrdId | String | Client Order ID as assigned by the client  
tag | String | Order tag  
px | String | Price  
For options, use coin as unit (e.g. BTC, ETH)  
pxUsd | String | Options price in USDOnly applicable to options; return "" for other instrument types  
pxVol | String | Implied volatility of the options orderOnly applicable to options; return "" for other instrument types  
pxType | String | Price type of options   
`px`: Place an order based on price, in the unit of coin (the unit for the request parameter px is BTC or ETH)   
`pxVol`: Place an order based on pxVol   
`pxUsd`: Place an order based on pxUsd, in the unit of USD (the unit for the request parameter px is USD)  
sz | String | Quantity to buy or sell  
pnl | String | Profit and loss (excluding the fee).  
Applicable to orders which have a trade and aim to close position. It always is 0 in other conditions  
ordType | String | Order type   
`market`: Market order   
`limit`: Limit order   
`post_only`: Post-only order   
`fok`: Fill-or-kill order   
`ioc`: Immediate-or-cancel order   
`optimal_limit_ioc`: Market order with immediate-or-cancel order  
`mmp`: Market Maker Protection (only applicable to Option in Portfolio Margin mode)  
`mmp_and_post_only`: Market Maker Protection and Post-only order(only applicable to Option in Portfolio Margin mode)   
`op_fok`: Simple options (fok)  
`elp`: Enhanced Liquidity Program order  
side | String | Order side  
posSide | String | Position side  
tdMode | String | Trade mode  
accFillSz | String | Running total of filled quantity since order creation. In WebSocket order channel push events, `accFillSz` always represents the cumulative total, not the increment since the last push.  
The unit is `base_ccy` for SPOT and MARGIN, e.g. BTC-USDT, the unit is BTC;  
The unit is contract for `FUTURES`/`SWAP`/`OPTION`  
fillPx | String | Last filled price. If none is filled, it will return "".  
tradeId | String | Last traded ID  
fillSz | String | Quantity of the most recent individual fill event (not cumulative). For the running total of all fills, use `accFillSz`.  
The unit is `base_ccy` for SPOT and MARGIN, e.g. BTC-USDT, the unit is BTC;  
The unit is contract for `FUTURES`/`SWAP`/`OPTION`  
fillTime | String | Last filled time  
avgPx | String | Average filled price. If none is filled, it will return "".  
state | String | Order state:  
`live`: on the order book, no fills yet.  
`partially_filled`: partially executed, still active on book.  
`filled`: fully executed, terminal state.  
`canceled`: cancelled, terminal state. For IOC orders partially filled before cancellation, `accFillSz` may be non-zero.  
`mmp_canceled`: automatically cancelled by Market Maker Protection, terminal state.  
Note: GET /api/v5/trade/orders-pending only returns `live` and `partially_filled`; GET /api/v5/trade/orders-history returns `filled`, `canceled`, and `mmp_canceled`.  
stpId | String | ~~Self trade prevention ID  
Return "" if self trade prevention is not applicable~~ (Deprecated)  
stpMode | String | Self trade prevention mode  
lever | String | Leverage, from `0.01` to `125`.   
Only applicable to `MARGIN/FUTURES/SWAP`  
attachAlgoClOrdId | String | Client-supplied Algo ID when placing order with attached TP/SL or trailing stop.  
tpTriggerPx | String | Take-profit trigger price.  
tpTriggerPxType | String | Take-profit trigger price type.   
`last`: last price  
`index`: index price  
`mark`: mark price  
tpOrdPx | String | Take-profit order price.  
slTriggerPx | String | Stop-loss trigger price.  
slTriggerPxType | String | Stop-loss trigger price type.   
`last`: last price  
`index`: index price  
`mark`: mark price  
slOrdPx | String | Stop-loss order price.  
attachAlgoOrds | Array of objects | Attached TP/SL or trailing stop order information  
> attachAlgoId | String | The order ID of the attached TP/SL or trailing stop order. It can be used to identify the attached order when amending. It will not be posted to algoId when placing the attached algo order after the general order is filled completely.  
> attachAlgoClOrdId | String | Client-supplied Algo ID when placing order with attached TP/SL or trailing stop  
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
It will be posted to `algoClOrdId` when placing the attached algo order once the general order is filled completely.  
> tpOrdKind | String | TP order kind  
`condition`  
`limit`  
> tpTriggerPx | String | Take-profit trigger price.  
> tpTriggerRatio | String | Take profit trigger ratio, 0.3 represents 30%   
Only applicable to FUTURES and SWAP.  
> tpTriggerPxType | String | Take-profit trigger price type.   
`last`: last price  
`index`: index price  
`mark`: mark price  
> tpOrdPx | String | Take-profit order price.  
> slTriggerPx | String | Stop-loss trigger price.  
> slTriggerRatio | String | Stop-loss trigger ratio, 0.3 represents 30%   
Only applicable to FUTURES and SWAP.  
> slTriggerPxType | String | Stop-loss trigger price type.   
`last`: last price  
`index`: index price  
`mark`: mark price  
> slOrdPx | String | Stop-loss order price.  
> sz | String | Size. Only applicable to TP order of split TPs  
> amendPxOnTriggerType | String | Whether to enable Cost-price SL. Only applicable to SL order of split TPs.   
`0`: disable, the default value   
`1`: Enable  
> callbackRatio | String | Callback ratio, e.g. `0.05` represents 5%  
> callbackSpread | String | Callback spread (price distance)  
> activePx | String | Activation price  
> failCode | String | The error code when failing to place TP/SL order, e.g. 51020   
The default is ""  
> failReason | String | The error reason when failing to place TP/SL order.   
The default is ""  
linkedAlgoOrd | Object | Linked SL order detail, only applicable to the order that is placed by one-cancels-the-other (OCO) order that contains the TP limit order.  
> algoId | String | Algo ID  
feeCcy | String | Fee currency  
For maker sell orders of Spot and Margin, this represents the quote currency. For all other cases, it represents the currency in which fees are charged.  
fee | String | Fee amount. Sign convention: negative = net fee paid to platform; positive = net rebate received from platform. The net amount reflects fee minus rebate.  
For Spot and Margin (excluding maker sell orders): accumulated fee charged by the platform, always negative.  
For maker sell orders in Spot and Margin, Expiry Futures, Perpetual Futures and Options: accumulated fee and rebate (always in quote currency for maker sell orders in Spot and Margin).  
For split accounting, use `feeCcy` \+ `fee` together with `rebateCcy` \+ `rebate`. `feeCcy` and `rebateCcy` may differ.  
rebateCcy | String | Rebate currency  
For maker sell orders of Spot and Margin, this represents the base currency. For all other cases, it represents the currency in which rebates are paid.  
rebate | String | Rebate amount, only applicable to Spot and Margin  
For maker sell orders: ~~Accumulated fee and~~ rebate amount in the unit of base currency.  
For all other cases, it represents the maker rebate amount, always positive, return "" if no rebate.  
source | String | Order source (non-exhaustive — handle unknown values gracefully as new types may be added):  
`6`: The normal order triggered by the `trigger order`  
`7`: The normal order triggered by the `TP/SL order`   
`13`: The normal order triggered by the algo order  
`25`: The normal order triggered by the `trailing stop order`  
`34`: The normal order triggered by the chase order.  
All values represent system-generated child orders triggered by parent algo or strategy orders.  
category | String | Category:  
`normal`: standard user-placed order.  
`twap`: forced repayment order generated by the system (not a TWAP algorithmic strategy).  
`adl`: auto-deleveraging, system-triggered position reduction.  
`full_liquidation`: forced full position close due to margin breach.  
`partial_liquidation`: forced partial position close.  
`delivery`: futures/options expiry settlement execution.  
`ddh`: delta dynamic hedge order placed by the options market-maker system.  
`auto_conversion`: system-triggered asset conversion.  
reduceOnly | String | Whether the order can only reduce the position size. Valid options: true or false.  
isTpLimit | String | Whether it is TP limit order. true or false  
cancelSource | String | Code of the cancellation source.  
cancelSourceReason | String | Reason for the cancellation.  
quickMgnType | String | ~~Quick Margin type, Only applicable to Quick Margin Mode of isolated margin  
`manual`, `auto_borrow`, `auto_repay`~~ (Deprecated)  
algoClOrdId | String | Client-supplied Algo ID. There will be a value when algo order attaching `algoClOrdId` is triggered, or it will be "".  
algoId | String | Algo ID. There will be a value when algo order is triggered, or it will be "".  
uTime | String | Update time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
cTime | String | Creation time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
tradeQuoteCcy | String | The quote currency used for trading.  
outcome | String | The market outcome the user traded on.  
`yes`  
`no`  
Only applicable to `EVENTS`

---

# GET / 获取订单信息

查订单信息

#### 限速：60次/2s

#### 限速规则（期权以外）：User ID + Instrument ID

#### 限速规则（只限期权）：User ID + Instrument Family

#### 权限：读取

#### HTTP请求

`GET /api/v5/trade/order`

> 请求示例
    
    
    GET /api/v5/trade/order?ordId=1753197687182819328&instId=BTC-USDT
    
    
    
    
    import okx.Trade as Trade
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘: 0, 模拟盘: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)
    
    # 通过 ordId 查询订单
    result = tradeAPI.get_order(
        instId="BTC-USDT",
        ordId="680800019749904384"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instId | String | 是 | 产品ID，如 `BTC-USDT`  
只适用于交易中的产品  
ordId | String | 可选 | 订单ID，`ordId`和`clOrdId`必须传一个，若传两个，以`ordId`为主  
clOrdId | String | 可选 | 用户自定义ID  
如果`clOrdId`关联了多个订单，只会返回最近的那笔订单  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "accFillSz": "0.00192834",
                "algoClOrdId": "",
                "algoId": "",
                "attachAlgoClOrdId": "",
                "attachAlgoOrds": [],
                "avgPx": "51858",
                "cTime": "1708587373361",
                "cancelSource": "",
                "cancelSourceReason": "",
                "category": "normal",
                "ccy": "",
                "clOrdId": "",
                "fee": "-0.00000192834",
                "feeCcy": "BTC",
                "fillPx": "51858",
                "fillSz": "0.00192834",
                "fillTime": "1708587373361",
                "instId": "BTC-USDT",
                "instType": "SPOT",
                "isTpLimit": "false",
                "lever": "",
                "linkedAlgoOrd": {
                    "algoId": ""
                },
                "ordId": "680800019749904384",
                "ordType": "market",
                "pnl": "0",
                "posSide": "net",
                "px": "",
                "pxType": "",
                "pxUsd": "",
                "pxVol": "",
                "quickMgnType": "",
                "rebate": "0",
                "rebateCcy": "USDT",
                "reduceOnly": "false",
                "side": "buy",
                "slOrdPx": "",
                "slTriggerPx": "",
                "slTriggerPxType": "",
                "source": "",
                "state": "filled",
                "stpId": "",
                "stpMode": "",
                "sz": "100",
                "tag": "",
                "tdMode": "cash",
                "tgtCcy": "quote_ccy",
                "tpOrdPx": "",
                "tpTriggerPx": "",
                "tpTriggerPxType": "",
                "tradeId": "744876980",
                "tradeQuoteCcy": "USDT",
                "uTime": "1708587373362"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
instType | String | 产品类型  
`SPOT`：币币  
`MARGIN`：币币杠杆  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`OPTION`：期权  
`EVENTS`：事件合约  
instId | String | 产品ID  
tgtCcy | String | 币币市价单委托数量`sz`的单位  
`base_ccy`: 交易货币 ；`quote_ccy`：计价货币  
仅适用于`币币`市价订单  
默认买单为`quote_ccy`，卖单为`base_ccy`  
ccy | String | 保证金币种，适用于`逐仓杠杆`及`合约模式`下的`全仓杠杆`订单以及交割、永续和期权合约订单。  
ordId | String | 订单ID  
clOrdId | String | 客户自定义订单ID  
tag | String | 订单标签  
px | String | 委托价格，对于期权，以币(如BTC, ETH)为单位  
pxUsd | String | 期权价格，以USD为单位   
仅适用于期权，其他业务线返回空字符串""  
pxVol | String | 期权订单的隐含波动率   
仅适用于期权，其他业务线返回空字符串""  
pxType | String | 期权的价格类型   
`px`：代表按价格下单，单位为币 (请求参数 px 的数值单位是BTC或ETH)   
`pxVol`：代表按pxVol下单   
`pxUsd`：代表按照pxUsd下单，单位为USD (请求参数px 的数值单位是USD)  
sz | String | 委托数量  
pnl | String | 收益(不包括手续费)  
适用于有成交的平仓订单，其他情况均为0  
ordType | String | 订单类型   
`market`：市价单  
`limit`：限价单   
`post_only`：只做maker单   
`fok`：全部成交或立即取消   
`ioc`：立即成交并取消剩余   
`optimal_limit_ioc`：市价委托立即成交并取消剩余（仅适用交割、永续）  
`mmp`：做市商保护(仅适用于组合保证金账户模式下的期权订单)  
`mmp_and_post_only`：做市商保护且只做maker单(仅适用于组合保证金账户模式下的期权订单)   
`op_fok`：期权简选（全部成交或立即取消）  
`elp`：流动性增强计划订单  
side | String | 订单方向  
posSide | String | 持仓方向  
tdMode | String | 交易模式  
accFillSz | String | 自下单以来的累计成交数量。在WebSocket订单频道推送中，`accFillSz` 始终表示累计总量，而非本次推送的增量。  
对于`币币`和`杠杆`，单位为交易货币，如 BTC-USDT, 单位为 BTC；  
对于交割、永续以及期权，单位为张。  
fillPx | String | 最新成交价格，如果成交数量为0，该字段为""  
tradeId | String | 最新成交ID  
fillSz | String | 最近一次单笔成交数量（非累计）。累计成交总量请使用 `accFillSz`。  
对于`币币`和`杠杆`，单位为交易货币，如 BTC-USDT, 单位为 BTC；  
对于交割、永续以及期权，单位为张。  
fillTime | String | 最新成交时间  
avgPx | String | 成交均价，如果成交数量为0，该字段也为""  
state | String | 订单状态：  
`live`：已在订单簿中，尚无成交。  
`partially_filled`：部分成交，仍在订单簿中。  
`filled`：完全成交，终态。  
`canceled`：撤单，终态。IOC 订单被撤销时可能存在部分成交，此时 `accFillSz` 不为零。  
`mmp_canceled`：由做市商保护机制自动撤单，终态。  
注意：GET /api/v5/trade/orders-pending 仅返回 `live` 和 `partially_filled`；GET /api/v5/trade/orders-history 返回 `filled`、`canceled` 和 `mmp_canceled`。  
lever | String | 杠杆倍数，0.01到125之间的数值，仅适用于 `币币杠杆/交割/永续`  
attachAlgoClOrdId | String | 下单附带止盈止损或移动止盈止损时，客户自定义的策略订单ID  
tpTriggerPx | String | 止盈触发价  
tpTriggerPxType | String | 止盈触发价类型  
`last`：最新价格  
`index`：指数价格  
`mark`：标记价格  
tpOrdPx | String | 止盈委托价  
slTriggerPx | String | 止损触发价  
slTriggerPxType | String | 止损触发价类型  
`last`：最新价格  
`index`：指数价格  
`mark`：标记价格  
slOrdPx | String | 止损委托价  
attachAlgoOrds | Array of objects | 附带止盈止损或移动止盈止损订单信息  
> attachAlgoId | String | 附带止盈止损或移动止盈止损的订单ID，改单时，可用来标识该笔附带止盈止损订单。下附带策略委托单时，该值不会传给 algoId  
> attachAlgoClOrdId | String | 下单附带止盈止损或移动止盈止损时，客户自定义的策略订单ID  
> tpOrdKind | String | 止盈订单类型  
`condition`: 条件单  
`limit`: 限价单  
> tpTriggerPx | String | 止盈触发价  
> tpTriggerRatio | String | 止盈触发比例，0.3 代表 30%   
仅适用于`交割`/`永续`合约  
> tpTriggerPxType | String | 止盈触发价类型  
`last`：最新价格  
`index`：指数价格  
`mark`：标记价格  
> tpOrdPx | String | 止盈委托价  
> slTriggerPx | String | 止损触发价  
> slTriggerRatio | String | 止损触发比例，0.3 代表 30%   
仅适用于`交割`/`永续`合约  
> slTriggerPxType | String | 止损触发价类型  
`last`：最新价格  
`index`：指数价格  
`mark`：标记价格  
> slOrdPx | String | 止损委托价  
> sz | String | 张数。仅适用于“多笔止盈”的止盈订单  
> amendPxOnTriggerType | String | 是否启用开仓价止损，仅适用于分批止盈的止损订单  
`0`：不开启，默认值   
`1`：开启  
> callbackRatio | String | 回调幅度的比例，如 `0.05` 代表 5%  
> callbackSpread | String | 回调幅度的价距  
> activePx | String | 激活价格  
> failCode | String | 委托失败的错误码，默认为"",  
委托失败时有值，如 51020  
> failReason | String | 委托失败的原因，默认为""  
委托失败时有值  
linkedAlgoOrd | Object | 止损订单信息，仅适用于包含限价止盈单的双向止盈止损订单，触发后生成的普通订单  
> algoId | String | 策略订单唯一标识  
stpId | String | ~~自成交保护ID  
如果自成交保护不适用则返回""~~（已弃用）  
stpMode | String | 自成交保护模式  
feeCcy | String | 手续费币种  
对于币币和杠杆的挂单卖单，表示计价币种；其他情况下，表示收取手续费的币种。  
fee | String | 手续费金额。符号规则：负数表示向平台净支付手续费；正数表示从平台净获得返佣。该净额已包含手续费与返佣的轧差。  
对于币币和杠杆（除挂单卖单外）：平台收取的累计手续费，始终为负数。  
对于币币和杠杆的挂单卖单、交割、永续和期权：累计手续费和返佣（币币和杠杆挂单卖单始终以计价币种计算）。  
如需分开核算，请结合 `feeCcy`+`fee` 与 `rebateCcy`+`rebate` 使用，两者货币种类可能不同。  
rebateCcy | String | 返佣币种  
对于币币和杠杆的挂单卖单，表示交易币种；其他情况下，表示支付返佣的币种。  
rebate | String | 返佣金额，仅适用于币币和杠杆  
对于挂单卖单：以交易币种为单位的~~累计手续费和~~ 返佣金额。  
其他情况下，表示挂单返佣金额，始终为正数，如无返佣则返回""。  
source | String | 订单来源（列表不完整——如遇未知值请做容错处理，后续可能新增类型）：  
`6`：计划委托策略触发后生成的普通单  
`7`：止盈止损策略触发后生成的普通单  
`13`：策略委托单触发后生成的普通单  
`25`：移动止盈止损策略触发后生成的普通单  
`34`：追逐限价委托生成的普通单  
所有值均表示由母策略或算法订单触发生成的系统子单。  
category | String | 订单种类：  
`normal`：用户正常下单。  
`twap`：系统生成的强制还款单（非TWAP算法策略）。  
`adl`：ADL自动减仓，系统触发的仓位削减。  
`full_liquidation`：因保证金不足触发的全仓强制平仓。  
`partial_liquidation`：因保证金不足触发的部分强制平仓。  
`delivery`：期货/期权到期结算执行。  
`ddh`：期权做市商系统触发的Delta动态对冲单。  
`auto_conversion`：系统触发的资产自动转换单。  
reduceOnly | String | 是否只减仓，`true` 或 `false`  
cancelSource | String | 订单取消来源的原因枚举值代码  
cancelSourceReason | String | 订单取消来源的对应具体原因  
quickMgnType | String | ~~一键借币类型，仅适用于杠杆逐仓的一键借币模式  
`manual`：手动，`auto_borrow`：自动借币，`auto_repay`：自动还币~~（已弃用）  
algoClOrdId | String | 客户自定义策略订单ID。策略订单触发，且策略单有`algoClOrdId`时有值，否则为"",  
algoId | String | 策略委托单ID，策略订单触发时有值，否则为""  
isTpLimit | String | 是否为限价止盈，true 或 false.  
uTime | String | 订单状态更新时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
cTime | String | 订单创建时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
tradeQuoteCcy | String | 用于交易的计价币种。  
outcome | String | 用户交易的市场结果方向。  
`yes`  
`no`  
仅适用于 `EVENTS`