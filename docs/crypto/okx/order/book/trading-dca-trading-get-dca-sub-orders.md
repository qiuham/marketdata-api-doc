---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-dca-trading-get-dca-sub-orders
anchor_id: order-book-trading-dca-trading-get-dca-sub-orders
api_type: API
updated_at: 2026-07-18 20:03:36.297871
---

# GET / DCA sub orders

#### Rate Limit: 20 requests per 2 seconds  
  
#### Rate Limit Rule: User ID

#### HTTP Request

`GET /api/v5/tradingBot/dca/orders`

> Request Example
    
    
    GET /api/v5/tradingBot/dca/orders?algoId=2833925189933756416&algoOrdType=contract_dca
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
algoId | String | Yes | Algo ID  
algoOrdType | String | Yes | Algo order type  
`contract_dca`: Contract DCA order  
`spot_dca`: Spot DCA order  
cycleId | String | No | Cycle ID  
after | String | No | Pagination of data to return records earlier than the requested `ordId`  
before | String | No | Pagination of data to return records newer than the requested `ordId`  
limit | String | No | Number of results per request. The maximum is 100. The default is 100  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "cycleId": "9876543",
                "ordId": "570627699870375936",
                "avgFillPx": "41500",
                "direction": "long",
                "side": "buy",
                "ordType": "init_order",
                "px": "41000",
                "sz": "10",
                "filledSz": "10",
                "state": "filled",
                "fee": "-0.2",
                "rebate": "0",
                "rebateCcy": "USDT",
                "lever": "3",
                "instId": "BTC-USDT-SWAP",
                "ctVal": "0.01",
                "fillTime": "1597026383085",
                "cTime": "1597026383085",
                "uTime": "1597026383085",
                "tradeQuoteCcy": ""
            }
        ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
cycleId | String | Cycle ID  
ordId | String | Sub order ID  
avgFillPx | String | Average filled price  
direction | String | Position direction  
Contract DCA: `long`: Long position, `short`: Short position  
Spot DCA: `long`: Long position  
side | String | Order side  
`buy`  
`sell`  
ordType | String | Sub order type  
`init_order`: Initial order  
`safety_order`: Safety order  
`tp_order`: Take-profit order  
`sl_order`: Stop-loss order  
`manual_add_order`: Manually added order  
`close_position`: Close position order  
`manual_close_position`: Manual close position order  
px | String | Order price  
sz | String | Order size  
filledSz | String | Filled size  
state | String | Order status  
`live`: Pending fill  
`partially_filled`: Partially filled  
`filled`: Fully filled  
`canceled`: Canceled  
`cancelling`: Cancelling  
fee | String | Accumulated fee  
Negative number represents the user transaction fee charged by the platform. Positive number represents rebate.  
rebate | String | Rebate amount  
rebateCcy | String | Rebate currency  
lever | String | Leverage  
Only applicable to `contract_dca`  
instId | String | Instrument ID, e.g. `BTC-USDT-SWAP`  
ctVal | String | Contract value  
Only applicable to `contract_dca`  
fillTime | String | Last filled time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
cTime | String | Order created time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
uTime | String | Order updated time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
tradeQuoteCcy | String | Quote currency for trading  
Only applicable to `spot_dca`

---

# GET / 获取马丁策略子订单列表

#### 限速：20次/2s  
  
#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/tradingBot/dca/orders`

> 请求示例
    
    
    GET /api/v5/tradingBot/dca/orders?algoId=2833925189933756416&algoOrdType=contract_dca
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoId | String | 是 | 策略订单 ID  
algoOrdType | String | 是 | 策略订单类型  
`contract_dca`：合约马丁委托  
`spot_dca`：现货马丁委托  
cycleId | String | 否 | 策略周期 ID  
after | String | 否 | 请求此ID之前（更旧的数据）的分页内容，传的值为对应接口的 `ordId`  
before | String | 否 | 请求此ID之后（更新的数据）的分页内容，传的值为对应接口的 `ordId`  
limit | String | 否 | 返回结果的数量，最大为100，默认100条  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "cycleId": "9876543",
                "ordId": "570627699870375936",
                "avgFillPx": "41500",
                "direction": "long",
                "side": "buy",
                "ordType": "init_order",
                "px": "41000",
                "sz": "10",
                "filledSz": "10",
                "state": "filled",
                "fee": "-0.2",
                "rebate": "0",
                "rebateCcy": "USDT",
                "lever": "3",
                "instId": "BTC-USDT-SWAP",
                "ctVal": "0.01",
                "fillTime": "1597026383085",
                "cTime": "1597026383085",
                "uTime": "1597026383085",
                "tradeQuoteCcy": ""
            }
        ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
cycleId | String | 策略周期 ID  
ordId | String | 子订单 ID  
avgFillPx | String | 子订单平均成交价格  
direction | String | 持仓方向  
合约马丁类型：`long`：多仓，`short`：空仓  
现货马丁类型：`long`：做多  
side | String | 子订单方向  
`buy`：买  
`sell`：卖  
ordType | String | 子订单类型  
`init_order`：初始订单  
`safety_order`：加仓订单  
`tp_order`：止盈单  
`sl_order`：止损单  
`manual_add_order`：手动加仓单  
`close_position`：平仓单  
`manual_close_position`：手动平仓单  
px | String | 子订单委托价格  
sz | String | 子订单委托数量  
filledSz | String | 子订单成交数量  
state | String | 子订单状态  
`live`：等待成交  
`partially_filled`：部分成交  
`filled`：完全成交  
`canceled`：撤单成功  
`cancelling`：撤单中  
fee | String | 子订单手续费数量  
rebate | String | 子订单返佣数量  
rebateCcy | String | 子订单返佣币种  
lever | String | 杠杆倍数  
仅适用于 `contract_dca`  
instId | String | 产品 ID，如 `BTC-USDT-SWAP`  
ctVal | String | 合约面值  
仅适用于 `contract_dca`  
fillTime | String | 子订单成交时间，Unix 时间戳毫秒数，如 `1597026383085`  
cTime | String | 子订单创建时间，Unix 时间戳毫秒数，如 `1597026383085`  
uTime | String | 子订单更新时间，Unix 时间戳毫秒数，如 `1597026383085`  
tradeQuoteCcy | String | 指定交易计价货币  
仅适用于 `spot_dca`