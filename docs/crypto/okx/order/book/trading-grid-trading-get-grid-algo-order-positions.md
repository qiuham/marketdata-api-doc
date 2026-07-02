---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-grid-trading-get-grid-algo-order-positions
anchor_id: order-book-trading-grid-trading-get-grid-algo-order-positions
api_type: API
updated_at: 2026-07-02 19:43:26.473909
---

# GET / Grid algo order positions

#### Rate Limit: 20 requests per 2 seconds  
  
#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/tradingBot/grid/positions`

> Request Example
    
    
    GET /api/v5/tradingBot/grid/positions?algoId=448965992920907776&algoOrdType=contract_grid
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
algoOrdType | String | Yes | Algo order type  
`contract_grid`: Contract grid  
algoId | String | Yes | Algo ID  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "adl": "1",
                "algoClOrdId": "",
                "algoId": "449327675342323712",
                "avgPx": "29215.0142857142857149",
                "cTime": "1653400065917",
                "ccy": "USDT",
                "imr": "2045.386",
                "instId": "BTC-USDT-SWAP",
                "instType": "SWAP",
                "last": "29206.7",
                "lever": "5",
                "liqPx": "661.1684795867162",
                "markPx": "29213.9",
                "mgnMode": "cross",
                "mgnRatio": "217.19370606167573",
                "mmr": "40.907720000000005",
                "notionalUsd": "10216.70307",
                "pos": "35",
                "posSide": "net",
                "uTime": "1653400066938",
                "upl": "1.674999999999818",
                "uplRatio": "0.0008190504784478"
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
instId | String | Instrument ID, e.g. `BTC-USDT-SWAP`  
cTime | String | Algo order created time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
uTime | String | Algo order updated time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
avgPx | String | Average open price  
ccy | String | Margin currency  
lever | String | Leverage  
liqPx | String | Estimated liquidation price  
posSide | String | Position side  
`net`  
pos | String | Quantity of positions  
mgnMode | String | Margin mode  
`cross`  
`isolated`  
mgnRatio | String | Maintenance margin ratio  
imr | String | Initial margin requirement  
mmr | String | Maintenance margin requirement  
upl | String | Unrealized profit and loss  
uplRatio | String | Unrealized profit and loss ratio  
last | String | Latest traded price  
notionalUsd | String | Notional value of positions in `USD`  
adl | String | Automatic-Deleveraging, signal area  
Divided into 5 levels, from 1 to 5, the smaller the number, the weaker the adl intensity.  
markPx | String | Mark price

---

# GET / 获取网格策略委托持仓

#### 限速：20次/2s  
  
#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/tradingBot/grid/positions`

> 请求示例
    
    
    GET /api/v5/tradingBot/grid/positions?algoId=448965992920907776&algoOrdType=contract_grid
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoOrdType | String | 是 | 订单类型  
`contract_grid`：合约网格委托  
algoId | String | 是 | 策略订单ID  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "adl": "1",
                "algoClOrdId": "",
                "algoId": "449327675342323712",
                "avgPx": "29215.0142857142857149",
                "cTime": "1653400065917",
                "ccy": "USDT",
                "imr": "2045.386",
                "instId": "BTC-USDT-SWAP",
                "instType": "SWAP",
                "last": "29206.7",
                "lever": "5",
                "liqPx": "661.1684795867162",
                "markPx": "29213.9",
                "mgnMode": "cross",
                "mgnRatio": "217.19370606167573",
                "mmr": "40.907720000000005",
                "notionalUsd": "10216.70307",
                "pos": "35",
                "posSide": "net",
                "uTime": "1653400066938",
                "upl": "1.674999999999818",
                "uplRatio": "0.0008190504784478"
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
instId | String | 产品ID，如 `BTC-USDT-SWAP`  
cTime | String | 策略订单创建时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
uTime | String | 策略订单更新时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
avgPx | String | 开仓均价  
ccy | String | 保证金币种  
lever | String | 杠杆倍数  
liqPx | String | 预估强平价  
posSide | String | 持仓方向  
`net`：买卖模式  
pos | String | 持仓数量  
mgnMode | String | 保证金模式  
`cross`：全仓  
`isolated`：逐仓  
mgnRatio | String | 维持保证金率  
imr | String | 初始保证金  
mmr | String | 维持保证金  
upl | String | 未实现收益  
uplRatio | String | 未实现收益率  
last | String | 最新成交价  
notionalUsd | String | 仓位美金价值  
adl | String | 自动减仓信号区  
分为5档，从1到5，数字越小代表adl强度越弱  
markPx | String | 标记价格