---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-grid-trading-get-grid-algo-sub-orders
anchor_id: order-book-trading-grid-trading-get-grid-algo-sub-orders
api_type: API
updated_at: 2026-07-06 19:52:56.102082
---

# GET / Grid algo sub orders

#### Rate Limit: 20 requests per 2 seconds  
  
#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/tradingBot/grid/sub-orders`

> Request Example
    
    
    GET /api/v5/tradingBot/grid/sub-orders?algoId=123456&type=live&algoOrdType=grid
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
algoOrdType | String | Yes | Algo order type  
`grid`: Spot grid  
`contract_grid`: Contract grid  
algoId | String | Yes | Algo ID  
type | String | Yes | Sub order state  
`live`  
`filled`  
groupId | String | No | Group ID  
after | String | No | Pagination of data to return records earlier than the requested `ordId`.  
before | String | No | Pagination of data to return records newer than the requested `ordId`.  
limit | String | No | Number of results per request. The maximum is 100. The default is 100  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "accFillSz": "0",
                "algoClOrdId": "",
                "algoId": "448965992920907776",
                "algoOrdType": "grid",
                "avgPx": "0",
                "cTime": "1653347949771",
                "ccy": "",
                "ctVal": "",
                "fee": "0",
                "feeCcy": "USDC",
                "groupId": "3",
                "instId": "BTC-USDC",
                "instType": "SPOT",
                "lever": "0",
                "ordId": "449109084439187456",
                "ordType": "limit",
                "pnl": "0",
                "posSide": "net",
                "px": "30404.3",
                "rebate": "0",
                "rebateCcy": "USDT",
                "side": "sell",
                "state": "live",    
                "sz": "0.00059213",
                "tag": "",
                "tdMode": "cash",
                "uTime": "1653347949831"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
algoId | String | Algo ID  
algoClOrdId | String | Client-supplied Algo ID  
instType | String | Instrument type  
instId | String | Instrument ID  
algoOrdType | String | Algo order type  
`grid`: Spot grid  
`contract_grid`: Contract grid  
groupId | String | Group ID  
ordId | String | Sub order ID  
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
`buy` `sell`  
px | String | Sub order price  
fee | String | Sub order fee amount  
feeCcy | String | Sub order fee currency  
rebate | String | Sub order rebate amount  
rebateCcy | String | Sub order rebate currency  
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

# GET / 获取网格策略委托子订单信息

#### 限速：20次/2s  
  
#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/tradingBot/grid/sub-orders`

> 请求示例
    
    
    GET /api/v5/tradingBot/grid/sub-orders?algoId=123456&type=live&algoOrdType=grid
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoId | String | 是 | 策略订单ID  
algoOrdType | String | 是 | 策略订单类型  
`grid`：现货网格委托  
`contract_grid`：合约网格委托  
type | String | 是 | 子订单状态  
`live`：未成交  
`filled`：已成交  
groupId | String | 否 | 组ID  
after | String | 否 | 请求此ID之前（更旧的数据）的分页内容，传的值为对应接口的`ordId`  
before | String | 否 | 请求此ID之后（更新的数据）的分页内容，传的值为对应接口的`ordId`  
limit | String | 否 | 返回结果的数量，最大为100，默认100条  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "accFillSz": "0",
                "algoClOrdId": "",
                "algoId": "448965992920907776",
                "algoOrdType": "grid",
                "avgPx": "0",
                "cTime": "1653347949771",
                "ccy": "",
                "ctVal": "",
                "fee": "0",
                "feeCcy": "USDC",
                "groupId": "3",
                "instId": "BTC-USDC",
                "instType": "SPOT",
                "lever": "0",
                "ordId": "449109084439187456",
                "ordType": "limit",
                "pnl": "0",
                "posSide": "net",
                "px": "30404.3",
                "rebate": "0",
                "rebateCcy": "USDT",
                "side": "sell",
                "state": "live",    
                "sz": "0.00059213",
                "tag": "",
                "tdMode": "cash",
                "uTime": "1653347949831"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
algoId | String | 策略订单ID  
algoClOrdId | String | 用户自定义策略ID  
instType | String | 产品类型  
instId | String | 产品ID  
algoOrdType | String | 策略订单类型  
`grid`：现货网格委托  
`contract_grid`：合约网格委托  
groupId | String | 组ID  
ordId | String | 子订单ID  
cTime | String | 子订单创建时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
uTime | String | 子订单更新时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
tdMode | String | 子订单交易模式  
`cross`：全仓  
`isolated`：逐仓  
`cash`：非保证金  
ccy | String | 保证金币种  
仅适用于`合约模式`模式下的`全仓杠杆`订单  
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
rebate | String | 子订单返佣数量  
rebateCcy | String | 子订单返佣币种  
avgPx | String | 子订单平均成交价格  
accFillSz | String | 子订单累计成交数量  
posSide | String | 子订单持仓方向  
`net`：买卖模式  
pnl | String | 子订单收益  
ctVal | String | 合约面值  
仅支持`FUTURES/SWAP`  
lever | String | 杠杆倍数  
tag | String | 订单标签