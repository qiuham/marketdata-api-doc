---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-signal-bot-trading-get-signal-bot-sub-orders
anchor_id: order-book-trading-signal-bot-trading-get-signal-bot-sub-orders
api_type: API
updated_at: 2026-07-23 19:21:41.424613
---

# GET / Signal bot sub orders

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/tradingBot/signal/sub-orders`

> Request Example
    
    
    # Get historical filled sub orders
    GET /api/v5/tradingBot/signal/sub-orders?algoId=623833708424069120&algoOrdType=contract&state=filled
    
    # Get designated sub order
    GET /api/v5/tradingBot/signal/sub-orders?algoId=623833708424069120&algoOrdType=contract&signalOrdId=O632302662327996418
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
algoId | String | Yes | Algo ID  
algoOrdType | String | Yes | Algo order type  
`contract`: Contract signal  
state | String | Conditional | Sub order state  
`live`  
`partially_filled`  
`filled`  
`cancelled`  
Either `state` or `signalOrdId` is required, if both are passed in, only `state` is valid.  
signalOrdId | String | Conditional | Sub order ID  
after | String | No | Pagination of data to return records earlier than the requested `ordId`  
before | String | No | Pagination of data to return records newer than the requested `ordId`.  
begin | String | No | Return records of `ctime` after than the requested timestamp (include), Unix timestamp format in milliseconds, e.g. `1597026383085`  
end | String | No | Return records of `ctime` before than the requested timestamp (include), Unix timestamp format in milliseconds, e.g. `1597026383085`  
limit | String | No | Number of results per request. The maximum is 100. The default is 100.  
type | String | No | Sub order type   
`live`  
`filled`  
Either `type` or `clOrdId` is required, if both are passed in, only `clOrdId` is valid.  
clOrdId | String | No | Sub order client-supplied ID.   
`It will be deprecated soon`  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "accFillSz": "18",
                "algoClOrdId": "",
                "algoId": "623833708424069120",
                "algoOrdType": "contract",
                "avgPx": "1572.81",
                "cTime": "1697024702320",
                "ccy": "",
                "clOrdId": "O632302662327996418",
                "ctVal": "0.01",
                "fee": "-0.1415529",
                "feeCcy": "USDT",
                "instId": "ETH-USDT-SWAP",
                "instType": "SWAP",
                "lever": "10",
                "ordId": "632302662351958016",
                "ordType": "market",
                "pnl": "-2.6784",
                "posSide": "net",
                "px": "",
                "side": "buy",
                "state": "filled",
                "sz": "18",
                "tag": "",
                "tdMode": "cross",
                "uTime": "1697024702322"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
algoId | String | Algo ID  
algoClOrdId | String | Client-supplied Algo ID. Used to be extended in the future  
instType | String | Instrument type  
instId | String | Instrument ID  
algoOrdType | String | Algo order type  
`contract`: Contract signal  
ordId | String | Sub order ID  
clOrdId | String | Sub order client-supplied ID.   
It is equal to `signalOrdId`  
cTime | String | Sub order created time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
uTime | String | Sub order updated time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
tdMode | String | Sub order trade mode  
Margin mode: `cross`/`isolated`  
Non-Margin mode: `cash`  
ccy | String | Margin currency  
Only applicable to cross MARGIN orders in `Futures mode`.  
ordType | String | Sub order type  
`market`: Market order  
`limit`: Limit order  
`ioc`: Immediate-or-cancel order  
sz | String | Sub order quantity to buy or sell  
state | String | Sub order state  
`canceled`  
`live`  
`partially_filled`  
`filled`  
`cancelling`  
side | String | Sub order side  
`buy`,`sell`  
px | String | Sub order price  
fee | String | Sub order fee amount  
feeCcy | String | Sub order fee currency  
avgPx | String | Sub order average filled price  
accFillSz | String | Sub order accumulated fill quantity  
posSide | String | Sub order position side  
`net`  
pnl | String | Sub order profit and loss  
ctVal | String | Contract value  
Only applicable to `FUTURES`/`SWAP`  
lever | String | Leverage  
tag | String | Order tag

---

# GET / 获取信号策略子订单信息

#### 限速：20次/2s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/tradingBot/signal/sub-orders`

> 请求示例
    
    
    # 查询已成交历史子订单
    GET /api/v5/tradingBot/signal/sub-orders?algoId=623833708424069120&algoOrdType=contract&state=filled
    
    # 查询指定子订单
    GET /api/v5/tradingBot/signal/sub-orders?algoId=623833708424069120&algoOrdType=contract&signalOrdId=O632302662327996418
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoId | String | 是 | 策略ID  
algoOrdType | String | 是 | 策略类型  
`contract`：合约信号  
state | String | 可选 | 子订单状态  
`live`：未成交  
`partially_filled`：部分成交  
`filled`：已成交  
`canceled`：已取消  
state 和 signalOrdId 必须传一个，若传两个，以 state 为主  
signalOrdId | String | 可选 | 子订单ID  
after | String | 否 | 请求此ID之前（更旧的数据）的分页内容，传的值为对应接口的`ordId`  
before | String | 否 | 请求此ID之后（更新的数据）的分页内容，传的值为对应接口的`ordId`  
begin | String | 否 | 请求`cTime`在此时间戳之后(包含)的数据，值为时间戳，Unix 时间戳为毫秒数格式，如 `1597026383085`  
end | String | 否 | 请求`cTime`在此时间戳之前(包含)的数据，值为时间戳，Unix 时间戳为毫秒数格式，如 `1597026383085`  
limit | String | 否 | 返回结果的数量，最大为100，默认100条  
type | String | 否 | 子订单类型  
`live`：未成交  
`filled`：已成交  
`即将废弃`  
clOrdId | String | 否 | 子订单自定义订单ID   
`即将废弃`  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "accFillSz": "18",
                "algoClOrdId": "",
                "algoId": "623833708424069120",
                "algoOrdType": "contract",
                "avgPx": "1572.81",
                "cTime": "1697024702320",
                "ccy": "",
                "clOrdId": "O632302662327996418",
                "ctVal": "0.01",
                "fee": "-0.1415529",
                "feeCcy": "USDT",
                "instId": "ETH-USDT-SWAP",
                "instType": "SWAP",
                "lever": "10",
                "ordId": "632302662351958016",
                "ordType": "market",
                "pnl": "-2.6784",
                "posSide": "net",
                "px": "",
                "side": "buy",
                "state": "filled",
                "sz": "18",
                "tag": "",
                "tdMode": "cross",
                "uTime": "1697024702322"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
algoId | String | 策略ID  
algoClOrdId | String | 用户自定义策略ID，将来扩展使用。  
instType | String | 产品类型  
instId | String | 交易产品ID  
algoOrdType | String | 策略类型  
`contract`：合约信号  
ordId | String | 子订单ID  
clOrdId | String | 子订单自定义ID，等同于`signalOrdId`  
cTime | String | 子订单创建时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
uTime | String | 子订单更新时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
tdMode | String | 子订单交易模式  
`cross`：全仓  
`isolated`：逐仓  
`cash`：非保证金  
ccy | String | 保证金币种  
仅适用于`合约模式`下的`全仓杠杆`订单  
ordType | String | 子订单类型  
`market`：市价单  
`limit`：限价单  
`ioc`：立即成交并取消剩余  
sz | String | 子订单委托数量  
state | String | 子订单状态  
`canceled`：撤单成功  
`live`：等待成交  
`partially_filled`：部分成交  
`filled`：完全成交  
`cancelling`：撤单中  
side | String | 子订单订单方向  
`buy`：买  
`sell`：卖  
px | String | 子订单委托价格  
fee | String | 子订单手续费数量  
feeCcy | String | 子订单手续费币种  
avgPx | String | 子订单平均成交价格  
accFillSz | String | 子订单累计成交数量  
posSide | String | 子订单持仓方向  
`net`：买卖模式  
pnl | String | 子订单收益  
ctVal | String | 合约面值  
仅支持`FUTURES/SWAP`  
lever | String | 杠杆倍数  
tag | String | 订单标签