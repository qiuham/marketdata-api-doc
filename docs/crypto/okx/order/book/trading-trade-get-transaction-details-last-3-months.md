---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-trade-get-transaction-details-last-3-months
anchor_id: order-book-trading-trade-get-transaction-details-last-3-months
api_type: API
updated_at: 2026-07-17 19:16:07.683038
---

# GET / Transaction details (last 3 months)

This endpoint can retrieve data from the last 3 months.

#### Rate Limit: 10 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/trade/fills-history`

> Request Example
    
    
    GET /api/v5/trade/fills-history?instType=SPOT
    
    
    
    
    import okx.Trade as Trade
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading: 0, Demo trading: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)
    
    # Retrieve SPOT transaction details in the last 3 months.
    result = tradeAPI.get_fills_history(
        instType="SPOT"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | YES | Instrument type  
`SPOT`  
`MARGIN`  
`SWAP`  
`FUTURES`  
`OPTION`  
`EVENTS`  
instFamily | String | No | Instrument family  
Applicable to `FUTURES`/`SWAP`/`OPTION`  
instId | String | No | Instrument ID, e.g. `BTC-USDT`  
ordId | String | No | Order ID  
subType | String | No | Transaction type   
`1`: Buy  
`2`: Sell  
`3`: Open long  
`4`: Open short  
`5`: Close long  
`6`: Close short   
`100`: Partial liquidation close long  
`101`: Partial liquidation close short  
`102`: Partial liquidation buy  
`103`: Partial liquidation sell  
`104`: Liquidation long  
`105`: Liquidation short  
`106`: Liquidation buy   
`107`: Liquidation sell   
`110`: Liquidation transfer in  
`111`: Liquidation transfer out   
`118`: System token conversion transfer in  
`119`: System token conversion transfer out  
`112`: Delivery long  
`113`: Delivery short   
`125`: ADL close long  
`126`: ADL close short  
`127`: ADL buy  
`128`: ADL sell   
`212`: Auto borrow of quick margin  
`213`: Auto repay of quick margin   
`204`: block trade buy  
`205`: block trade sell  
`206`: block trade open long  
`207`: block trade open short  
`208`: block trade close long  
`209`: block trade close short  
`236`: Easy convert in  
`237`: Easy convert out  
`270`: Spread trading buy  
`271`: Spread trading sell  
`272`: Spread trading open long  
`273`: Spread trading open short  
`274`: Spread trading close long  
`275`: Spread trading close short  
`324`: Move position buy  
`325`: Move position sell  
`326`: Move position open long  
`327`: Move position open short  
`328`: Move position close long  
`329`: Move position close short   
`376`: Collateralized borrowing auto conversion buy  
`377`: Collateralized borrowing auto conversion sell  
`410`: Buy yes  
`411`: Buy no  
`412`: Sell yes  
`413`: Sell no  
`414`: Yes expiry  
`415`: No expiry  
after | String | No | Pagination of data to return records earlier than the requested `billId`  
before | String | No | Pagination of data to return records newer than the requested `billId`  
begin | String | No | Filter with a begin timestamp `ts`. Unix timestamp format in milliseconds, e.g. `1597026383085`  
end | String | No | Filter with an end timestamp `ts`. Unix timestamp format in milliseconds, e.g. `1597026383085`  
limit | String | No | Number of results per request. The maximum is `100`; The default is `100`  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "side": "buy",
                "fillSz": "0.00192834",
                "fillPx": "51858",
                "fillPxVol": "",
                "fillFwdPx": "",
                "fee": "-0.00000192834",
                "fillPnl": "0",
                "ordId": "680800019749904384",
                "feeRate": "-0.001",
                "instType": "SPOT",
                "fillPxUsd": "",
                "instId": "BTC-USDT",
                "clOrdId": "",
                "posSide": "net",
                "billId": "680800019754098688",
                "subType": "1",
                "fillMarkVol": "",
                "tag": "",
                "fillTime": "1708587373361",
                "execType": "T",
                "fillIdxPx": "",
                "tradeId": "744876980",
                "fillMarkPx": "",
                "feeCcy": "BTC",
                "ts": "1708587373362",
                "tradeQuoteCcy": "USDT"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instType | String | Instrument type  
instId | String | Instrument ID  
tradeId | String | Last trade ID  
ordId | String | Order ID  
clOrdId | String | Client Order ID as assigned by the client  
billId | String | Bill ID  
subType | String | Transaction type  
tag | String | Order tag  
fillPx | String | Last filled price  
fillSz | String | Last filled quantity  
fillIdxPx | String | Index price at the moment of trade execution   
For cross currency spot pairs, it returns baseCcy-USDT index price. For example, for LTC-ETH, this field returns the index price of LTC-USDT.  
fillPnl | String | Last filled profit and loss, applicable to orders which have a trade and aim to close position. It always is 0 in other conditions  
fillPxVol | String | Implied volatility when filled   
Only applicable to options; return "" for other instrument types  
fillPxUsd | String | Options price when filled, in the unit of USD   
Only applicable to options; return "" for other instrument types  
fillMarkVol | String | Mark volatility when filled   
Only applicable to options; return "" for other instrument types  
fillFwdPx | String | Forward price when filled   
Only applicable to options; return "" for other instrument types  
fillMarkPx | String | Mark price when filled   
Applicable to `FUTURES`, `SWAP`, `OPTION`  
side | String | Order side  
`buy`  
`sell`  
posSide | String | Position side  
`long`  
`short`  
it returns `net` in`net` mode.  
execType | String | Liquidity taker or maker  
`T`: taker  
`M`: maker  
Not applicable to system orders such as ADL and liquidation  
feeCcy | String | Trading fee or rebate currency  
fee | String | The amount of trading fee or rebate. The trading fee deduction is negative, such as '-0.01'; the rebate is positive, such as '0.01'.  
ts | String | Data generation time, Unix timestamp format in milliseconds, e.g. `1597026383085`.  
fillTime | String | Trade time which is the same as `fillTime` for the order channel.  
feeRate | String | Fee rate. This field is returned for `SPOT` and `MARGIN` only  
tradeQuoteCcy | String | The quote currency for trading.  
tradeId  
When the order category to which the transaction details belong is partial_liquidation, full_liquidation, or adl, this field will be assigned a negative value to distinguish it from other matching transaction scenarios.  
ordId  
Order ID, always "" for block trading.  
clOrdId  
Client-supplied order ID, always "" for block trading.  We advise you to use Get Transaction details (last 3 days)when you request data for recent 3 days.

---

# GET / 获取成交明细（近三个月）

本接口可以查询最近 3 个月的成交明细数据。

#### 限速：10 次/2s

#### 限速规则：User ID

#### HTTP 请求

`GET /api/v5/trade/fills-history`

> 请求示例
    
    
    GET /api/v5/trade/fills-history?instType=SPOT
    
    
    
    
    import okx.Trade as Trade
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘: 0, 模拟盘: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)
    
    # 查询 币币 成交明细（3月内）
    result = tradeAPI.get_fills_history(
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
instFamily | String | 否 | 交易品种  
适用于`交割`/`永续`/`期权`  
instId | String | 否 | 产品 ID，如`BTC-USD-190927`  
ordId | String | 否 | 订单 ID  
subType | String | 否 | 成交类型   
`1`：买入  
`2`：卖出   
`3`：开多   
`4`：开空   
`5`：平多   
`6`：平空   
`100`：强减平多   
`101`：强减平空   
`102`：强减买入   
`103`：强减卖出   
`104`：强平平多   
`105`：强平平空   
`106`：强平买入   
`107`：强平卖出   
`110`：强平换币转入   
`111`：强平换币转出   
`118`：系统换币转入   
`119`：系统换币转出  
`112`：交割平多   
`113`：交割平空   
`125`：自动减仓平多   
`126`：自动减仓平空   
`127`：自动减仓买入   
`128`：自动减仓卖出   
`212`：一键借币的自动借币   
`213`：一键借币的自动还币   
`204`：大宗交易买   
`205`：大宗交易卖   
`206`：大宗交易开多   
`207`：大宗交易开空   
`208`：大宗交易平多   
`209`：大宗交易平空  
`236`：小额兑换买入  
`237`：小额兑换卖出  
`270`：价差交易买  
`271`：价差交易卖  
`272`：价差交易开多  
`273`：价差交易开空  
`274`：价差交易平多  
`275`：价差交易平空  
`324`：移仓买入  
`325`：移仓卖出  
`326`：移仓开多  
`327`：移仓开空  
`328`：移仓平多  
`329`：移仓平空  
`376`：质押借币超限买入  
`377`： 质押借币超限卖出  
`410`：买入yes  
`411`：买入no  
`412`：卖出yes  
`413`：卖出no  
`414`：yes结算  
`415`：no结算  
after | String | 否 | 请求此 ID 之前（更旧的数据）的分页内容，传的值为对应接口的 `billId`  
before | String | 否 | 请求此 ID 之后（更新的数据）的分页内容，传的值为对应接口的 `billId`  
begin | String | 否 | 筛选的开始时间戳 `ts`，Unix 时间戳为毫秒数格式，如 `1597026383085`  
end | String | 否 | 筛选的结束时间戳 `ts`，Unix 时间戳为毫秒数格式，如 `1597027383085`  
limit | String | 否 | 返回结果的数量，最大为100，默认100条  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "side": "buy",
                "fillSz": "0.00192834",
                "fillPx": "51858",
                "fillPxVol": "",
                "fillFwdPx": "",
                "fee": "-0.00000192834",
                "fillPnl": "0",
                "ordId": "680800019749904384",
                "feeRate": "-0.001",
                "instType": "SPOT",
                "fillPxUsd": "",
                "instId": "BTC-USDT",
                "clOrdId": "",
                "posSide": "net",
                "billId": "680800019754098688",
                "subType": "1",
                "fillMarkVol": "",
                "tag": "",
                "fillTime": "1708587373361",
                "execType": "T",
                "fillIdxPx": "",
                "tradeId": "744876980",
                "fillMarkPx": "",
                "feeCcy": "BTC",
                "ts": "1708587373362",
                "tradeQuoteCcy": "USDT"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
instType | String | 产品类型  
instId | String | 产品 ID  
tradeId | String | 最新成交 ID  
ordId | String | 订单 ID  
clOrdId | String | 用户自定义订单ID  
billId | String | 账单 ID  
subType | String | 成交类型  
tag | String | 订单标签  
fillPx | String | 最新成交价格，同"账单流水查询"的 px  
fillSz | String | 最新成交数量  
fillIdxPx | String | 交易执行时的指数价格  
对于交叉现货币对，返回 baseCcy-USDT 的指数价格。 如 LTC-ETH，该字段返回 LTC-USDT 的指数价格。  
fillPnl | String | 最新成交收益，适用于有成交的平仓订单。其他情况均为0。  
fillPxVol | String | 成交时的隐含波动率，仅适用于期权，其他业务线返回空字符串""  
fillPxUsd | String | 成交时的期权价格，以USD为单位，仅适用于期权，其他业务线返回空字符串""  
fillMarkVol | String | 成交时的标记波动率，仅适用于期权，其他业务线返回空字符串""  
fillFwdPx | String | 成交时的远期价格，仅适用于期权，其他业务线返回空字符串""  
fillMarkPx | String | 成交时的标记价格，仅适用于 `交割`/`永续`/`期权`  
side | String | 订单方向  
`buy`：买  
`sell`：卖  
posSide | String | 持仓方向  
`long`：多  
`short`：空  
买卖模式返回 `net`  
execType | String | 流动性方向  
`T`：taker  
`M`：maker  
不适用于系统订单比如强平和ADL  
feeCcy | String | 交易手续费币种或者返佣金币种  
fee | String | 手续费金额或者返佣金额  
手续费扣除为‘负数’，如 -0.01  
手续费返佣为‘正数’，如 0.01  
ts | String | 成交明细产生时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
fillTime | String | 成交时间，与订单频道的`fillTime`相同  
feeRate | String | 手续费费率。 该字段仅对 `币币`和`杠杆`返回  
tradeQuoteCcy | String | 用于交易的计价币种。  
tradeId  
当成交明细所归属的订单种类（category）为 partial_liquidation：强制减仓、full_liquidation：强制平仓、adl：ADL自动减仓时，tradeId字段的值为负数，以便和其他撮合成交场景区分  
ordId  
订单ID, 对于大宗交易总是 "" 。  
clOrdId  
用户自定义订单ID, 对于大宗交易总是 "" 。  获取近3天的成交明细时，建议使用获取成交明细（近三天）接口。