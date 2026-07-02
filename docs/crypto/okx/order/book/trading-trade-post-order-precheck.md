---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-trade-post-order-precheck
anchor_id: order-book-trading-trade-post-order-precheck
api_type: API
updated_at: 2026-07-02 19:43:16.151413
---

# POST / Order precheck

This endpoint is used to precheck the account information before and after placing the order.   
Only applicable to `Multi-currency margin mode`, and `Portfolio margin mode`.  
  
#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/trade/order-precheck`

> Request Example
    
    
    # place order for SPOT
    POST /api/v5/trade/order-precheck
     body
     {
        "instId":"BTC-USDT",
        "tdMode":"cash",
        "clOrdId":"b15",
        "side":"buy",
        "ordType":"limit",
        "px":"2.15",
        "sz":"2"
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instId | String | Yes | Instrument ID, e.g. `BTC-USDT`  
tdMode | String | Yes | Trade mode  
Margin mode `cross` `isolated`  
Non-Margin mode `cash`  
`spot_isolated` (only applicable to SPOT lead trading, `tdMode` should be `spot_isolated` for `SPOT` lead trading.)  
side | String | Yes | Order side, `buy` `sell`  
posSide | String | Conditional | Position side   
The default is `net` in the `net` mode   
It is required in the `long/short` mode, and can only be `long` or `short`.   
Only applicable to `FUTURES`/`SWAP`.  
ordType | String | Yes | Order type   
`market`: Market order   
`limit`: Limit order   
`post_only`: Post-only order   
`fok`: Fill-or-kill order   
`ioc`: Immediate-or-cancel order   
`optimal_limit_ioc`: Market order with immediate-or-cancel order (applicable only to Expiry Futures and Perpetual Futures).   
`elp`: Enhanced Liquidity Program order  
sz | String | Yes | Quantity to buy or sell  
px | String | Conditional | Order price. Only applicable to `limit`,`post_only`,`fok`,`ioc`,`mmp`,`mmp_and_post_only` order.  
outcome | String | Conditional | The market outcome users trade on.  
`yes`  
`no`  
Only applicable and required for `EVENTS`  
reduceOnly | Boolean | No | Whether orders can only reduce in position size.   
Valid options: `true` or `false`. The default value is `false`.  
Only applicable to `MARGIN` orders, and `FUTURES`/`SWAP` orders in `net` mode   
Only applicable to `Futures mode` and `Multi-currency margin`  
tgtCcy | String | No | Whether the target currency uses the quote or base currency.  
`base_ccy`: Base currency ,`quote_ccy`: Quote currency   
Only applicable to `SPOT` Market Orders  
Default is `quote_ccy` for buy, `base_ccy` for sell  
attachAlgoOrds | Array of objects | No | Attached TP/SL or trailing stop order information  
> attachAlgoClOrdId | String | No | Client-supplied Algo ID when placing order with attached TP/SL or trailing stop  
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
It will be posted to `algoClOrdId` when placing the attached algo order once the general order is filled completely.  
> tpTriggerPx | String | Conditional | Take-profit trigger price  
For condition TP order, if you fill in this parameter, you should fill in the take-profit order price as well.  
> tpOrdPx | String | Conditional | Take-profit order price   
  
For condition TP order, if you fill in this parameter, you should fill in the take-profit trigger price as well.   
For limit TP order, you need to fill in this parameter, take-profit trigger needn‘t to be filled.   
If the price is -1, take-profit will be executed at the market price.  
> tpOrdKind | String | No | TP order kind  
`condition`  
`limit`  
The default is `condition`  
> slTriggerPx | String | Conditional | Stop-loss trigger price  
If you fill in this parameter, you should fill in the stop-loss order price.  
> slOrdPx | String | Conditional | Stop-loss order price  
If you fill in this parameter, you should fill in the stop-loss trigger price.  
If the price is -1, stop-loss will be executed at the market price.  
> tpTriggerPxType | String | No | Take-profit trigger price type  
`last`: last price   
`index`: index price   
`mark`: mark price   
The default is last  
> slTriggerPxType | String | No | Stop-loss trigger price type  
`last`: last price   
`index`: index price   
`mark`: mark price   
The default is last  
> sz | String | Conditional | Size. Only applicable to TP order of split TPs, and it is required for TP order of split TPs  
> callbackRatio | String | Conditional | Callback ratio, e.g. `0.05` represents 5%.  
Either `callbackRatio` or `callbackSpread` is required. Only one can be passed.  
Only applicable when `ordType` = `move_order_stop`  
> callbackSpread | String | Conditional | Callback spread (price distance).  
Either `callbackRatio` or `callbackSpread` is required. Only one can be passed.  
Only applicable when `ordType` = `move_order_stop`  
> activePx | String | No | Activation price.  
The trailing stop is activated when the market price reaches the activation price. After activation, the system starts calculating the actual trigger price. If not provided, the trailing stop is activated immediately upon order placement.  
Only applicable when `ordType` = `move_order_stop`  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "adjEq": "41.94347460746277",
                "adjEqChg": "-226.05616481626",
                "availBal": "0",
                "availBalChg": "0",
                "imr": "0",
                "imrChg": "57.74709688430927",
                "liab": "0",
                "liabChg": "0",
                "liabChgCcy": "",
                "liqPx": "6764.8556232031115",
                "liqPxDiff": "-57693.044376796888536773622035980224609375",
                "liqPxDiffRatio": "-0.8950500152315991",
                "mgnRatio": "0",
                "mgnRatioChg": "0",
                "mmr": "0",
                "mmrChg": "0",
                "posBal": "",
                "posBalChg": "",
                "type": ""
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
adjEq | String | Current adjusted / Effective equity in `USD`  
adjEqChg | String | After placing order, changed quantity of adjusted / Effective equity in `USD`  
imr | String | Current initial margin requirement in `USD`  
imrChg | String | After placing order, changed quantity of initial margin requirement in `USD`  
mmr | String | Current Maintenance margin requirement in `USD`  
mmrChg | String | After placing order, changed quantity of maintenance margin requirement in `USD`  
mgnRatio | String | Current Maintenance margin ratio in `USD`  
mgnRatioChg | String | After placing order, changed quantity of Maintenance margin ratio in `USD`  
availBal | String | Current available balance in margin coin currency, only applicable to turn auto borrow off  
availBalChg | String | After placing order, changed quantity of available balance after placing order, only applicable to turn auto borrow off  
liqPx | String | Current estimated liquidation price  
liqPxDiff | String | After placing order, the distance between estimated liquidation price and mark price  
liqPxDiffRatio | String | After placing order, the distance rate between estimated liquidation price and mark price  
posBal | String | Current positive asset, only applicable to margin isolated position  
posBalChg | String | After placing order, positive asset of margin isolated, only applicable to margin isolated position  
liab | String | Current liabilities of currency  
For cross, it is cross liabilities  
For isolated position, it is isolated liabilities  
liabChg | String | After placing order, changed quantity of liabilities  
For cross, it is cross liabilities  
For isolated position, it is isolated liabilities  
liabChgCcy | String | After placing order, the unit of changed liabilities quantity  
only applicable cross and in auto borrow  
type | String | Unit type of positive asset, only applicable to margin isolated position  
`1`: it is both base currency before and after placing order   
`2`: before plaing order, it is base currency. after placing order, it is quota currency.  
`3`: before plaing order, it is quota currency. after placing order, it is base currency  
`4`: it is both quota currency before and after placing order

---

# POST / 订单预检查

用来预先查看订单下单前后的账户的对比信息，仅适用于`跨币种保证金模式`和`组合保证金模式`。  
  
#### 限速：5次/2s

#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/trade/order-precheck`

> 请求示例
    
    
    POST /api/v5/trade/order-precheck
    body
    {
        "instId":"BTC-USDT",
        "tdMode":"cash",
        "clOrdId":"b15",
        "side":"buy",
        "ordType":"limit",
        "px":"2.15",
        "sz":"2"
    }
    
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instId | String | 是 | 产品ID，如 `BTC-USDT`  
tdMode | String | 是 | 交易模式  
保证金模式：`isolated`：逐仓 ；`cross`：全仓   
非保证金模式：`cash`：非保证金  
`spot_isolated`：现货逐仓(仅适用于现货带单) ，现货带单时，`tdMode` 的值需要指定为`spot_isolated`  
side | String | 是 | 订单方向  
`buy`：买， `sell`：卖  
posSide | String | 可选 | 持仓方向  
在开平仓模式下必填，且仅可选择 `long` 或 `short`。 仅适用交割、永续。  
ordType | String | 是 | 订单类型   
`market`：市价单  
`limit`：限价单   
`post_only`：只做maker单   
`fok`：全部成交或立即取消   
`ioc`：立即成交并取消剩余   
`optimal_limit_ioc`：市价委托立即成交并取消剩余（仅适用交割、永续）  
`elp`：流动性增强计划订单  
sz | String | 是 | 委托数量  
px | String | 可选 | 委托价格，仅适用于`limit`、`post_only`、`fok`、`ioc`类型的订单  
outcome | String | 可选 | 用户交易的市场结果方向。  
`yes`  
`no`  
仅适用于 `EVENTS`，且为必填  
reduceOnly | Boolean | 否 | 是否只减仓，`true` 或 `false`，默认`false`  
仅适用于`币币杠杆`，以及买卖模式下的`交割/永续`  
仅适用于`合约模式`和`跨币种保证金模式`  
tgtCcy | String | 否 | 市价单委托数量`sz`的单位，仅适用于`币币`市价订单  
`base_ccy`: 交易货币 ；`quote_ccy`：计价货币  
买单默认`quote_ccy`， 卖单默认`base_ccy`  
attachAlgoOrds | Array of objects | 否 | 附带止盈止损或移动止盈止损订单信息  
> attachAlgoClOrdId | String | 否 | 下单附带止盈止损或移动止盈止损时，客户自定义的策略订单ID   
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度要在1-32位之间。  
订单完全成交，下附带策略委托单时，该值会传给`algoClOrdId`  
> tpTriggerPx | String | 可选 | 止盈触发价  
对于条件止盈单，如果填写此参数，必须填写 止盈委托价  
> tpOrdPx | String | 可选 | 止盈委托价  
对于条件止盈单，如果填写此参数，必须填写 止盈触发价  
对于限价止盈单，需填写此参数，不需要填写止盈触发价  
委托价格为-1时，执行市价止盈  
> tpOrdKind | String | 否 | 止盈订单类型  
`condition`: 条件单  
`limit`: 限价单  
默认为`condition`  
> slTriggerPx | String | 可选 | 止损触发价，如果填写此参数，必须填写 止损委托价  
> slOrdPx | String | 可选 | 止损委托价，如果填写此参数，必须填写 止损触发价  
委托价格为-1时，执行市价止损  
> tpTriggerPxType | String | 否 | 止盈触发价类型  
`last`：最新价格  
`index`：指数价格  
`mark`：标记价格  
默认为`last`  
> slTriggerPxType | String | 否 | 止损触发价类型  
`last`：最新价格  
`index`：指数价格  
`mark`：标记价格  
默认为`last`  
> sz | String | 可选 | 数量。仅适用于”多笔止盈”的止盈订单，且对于”多笔止盈”的止盈订单必填  
> callbackRatio | String | 可选 | 回调幅度的比例，如 `0.05` 代表 5%。  
`callbackRatio` 和 `callbackSpread` 必须传入其中一个，且只能传入一个。  
仅适用于 `ordType` = `move_order_stop`  
> callbackSpread | String | 可选 | 回调幅度的价距。  
`callbackRatio` 和 `callbackSpread` 必须传入其中一个，且只能传入一个。  
仅适用于 `ordType` = `move_order_stop`  
> activePx | String | 否 | 激活价格。  
激活价格是移动止盈止损的激活条件，当市场最新成交价达到或超过激活价格，委托被激活。激活后系统开始计算止盈止损的实际触发价格。如果不填写激活价格，即下单后就被激活。  
仅适用于 `ordType` = `move_order_stop`  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "adjEq": "41.94347460746277",
                "adjEqChg": "-226.05616481626",
                "availBal": "0",
                "availBalChg": "0",
                "imr": "0",
                "imrChg": "57.74709688430927",
                "liab": "0",
                "liabChg": "0",
                "liabChgCcy": "",
                "liqPx": "6764.8556232031115",
                "liqPxDiff": "-57693.044376796888536773622035980224609375",
                "liqPxDiffRatio": "-0.8950500152315991",
                "mgnRatio": "0",
                "mgnRatioChg": "0",
                "mmr": "0",
                "mmrChg": "0",
                "posBal": "",
                "posBalChg": "",
                "type": ""
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
adjEq | String | 当前美金层面有效保证金  
adjEqChg | String | 下单后，美金层面有效保证金的变动数量  
imr | String | 当前美金层面占用保证金  
imrChg | String | 下单后，美金层面占用保证金的变动数量  
mmr | String | 当前美金层面维持保证金  
mmrChg | String | 下单后，美金层面维持保证金的变动数量  
mgnRatio | String | 当前美金层面维持保证金率  
mgnRatioChg | String | 下单后，美金层面维持保证金率的变动数量  
availBal | String | 当前币种可用余额，仅适用于关闭自动借币时  
availBalChg | String | 下单后，币种可用余额的变动数量，仅适用于关闭自动借币时  
liqPx | String | 当前预估强平价  
liqPxDiff | String | 下单后，预估强平价与标记价格的差距  
liqPxDiffRatio | String | 下单后，预估强平价与标记价格的差距比率  
posBal | String | 当前杠杆逐仓仓位正资产，仅适用于逐仓杠杆  
posBalChg | String | 下单后，杠杆逐仓仓位正资产的变动数量，仅适用于逐仓杠杆  
liab | String | 当前负债  
如果是全仓，对应全仓负债，如果是逐仓，对应逐仓负债  
liabChg | String | 下单后，当前负债的变动数量  
如果是全仓，对应全仓负债，如果是逐仓，对应逐仓负债  
liabChgCcy | String | 下单后，当前负债变动数量的单位  
仅适用于全仓，开启自动借币时  
type | String | 仓位正资产(`posBal`)的单位类型，仅适用于杠杆逐仓，用来确定`posBal`的单位   
`1`:下单前后都是交易货币  
`2`:下单前是交易货币，下单后是计价货币  
`3`:下单前是计价货币，下单后是交易货币  
`4`:下单前后都是计价货币