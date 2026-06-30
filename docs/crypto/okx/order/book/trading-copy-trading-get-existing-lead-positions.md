---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-copy-trading-get-existing-lead-positions
anchor_id: order-book-trading-copy-trading-get-existing-lead-positions
api_type: API
updated_at: 2026-06-30 19:55:00.415948
---

# GET / Existing lead positions

Retrieve lead positions that are not closed.  
  
  
Returns reverse chronological order with `openTime`

#### Rate limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP request

`GET /api/v5/copytrading/current-subpositions`

> Request example
    
    
    GET /api/v5/copytrading/current-subpositions?instId=BTC-USDT-SWAP
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | No | Instrument type  
`SPOT`  
`SWAP`  
It returns all types by default.  
instId | String | No | Instrument ID, e.g. BTC-USDT-SWAP  
after | String | No | Pagination of data to return records earlier than the requested `subPosId`.  
before | String | No | Pagination of data to return records newer than the requested `subPosId`.  
limit | String | No | Number of results per request. Maximum is 500. Default is 500.  
  
> Response example
    
    
    {
        "code": "0",
        "data": [
            {
                "algoId": "",
                "ccy": "USDT",
                "instId": "BTC-USDT-SWAP",
                "instType": "SWAP",
                "lever": "3",
                "margin": "12.6417",
                "markPx": "38205.8",
                "mgnMode": "isolated",
                "openAvgPx": "37925.1",
                "openOrdId": "",
                "openTime": "1701231120479",
                "posSide": "net",
                "slOrdPx": "",
                "slTriggerPx": "",
                "subPos": "1",
                "subPosId": "649945658862370816",
                "tpOrdPx": "",
                "tpTriggerPx": "",
                "uniqueCode": "25CD5A80241D6FE6",
                "upl": "0.2807",
                "uplRatio": "0.0222042921442527",
                "availSubPos": "1"
            },
            {
                "algoId": "",
                "ccy": "USDT",
                "instId": "BTC-USDT-SWAP",
                "instType": "SWAP",
                "lever": "3",
                "margin": "12.6263333333333333",
                "markPx": "38205.8",
                "mgnMode": "isolated",
                "openAvgPx": "37879",
                "openOrdId": "",
                "openTime": "1701225074786",
                "posSide": "net",
                "slOrdPx": "",
                "slTriggerPx": "",
                "subPos": "1",
                "subPosId": "649920301388038144",
                "tpOrdPx": "",
                "tpTriggerPx": "",
                "uniqueCode": "25CD5A80241D6FE6",
                "upl": "0.3268",
                "uplRatio": "0.0258824150584758",
                "availSubPos": "1"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instId | String | Instrument ID, e.g. BTC-USDT-SWAP  
subPosId | String | Lead position ID  
posSide | String | Position side  
`long`   
`short`   
`net`  
(Long positions have positive subPos; short positions have negative subPos)  
mgnMode | String | Margin mode. `cross` `isolated`  
lever | String | Leverage  
openOrdId | String | Order ID for opening position, only applicable to lead position  
openAvgPx | String | Average open price  
openTime | String | Open time  
subPos | String | Quantity of positions  
tpTriggerPx | String | Take-profit trigger price.  
slTriggerPx | String | Stop-loss trigger price.  
algoId | String | Stop order ID  
instType | String | Instrument type  
tpOrdPx | String | Take-profit order price, it is -1 for market price  
slOrdPx | String | Stop-loss order price, it is -1 for market price  
margin | String | Margin  
upl | String | Unrealized profit and loss  
uplRatio | String | Unrealized profit and loss ratio  
markPx | String | Latest mark price, only applicable to contract  
uniqueCode | String | Lead trader unique code  
ccy | String | Margin currency  
availSubPos | String | Quantity of positions that can be closed

---

# GET / 获取当前带单

获取当前未平仓的带单仓位。  
  
  
按照开仓时间倒序排列。

#### 限速：20次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/copytrading/current-subpositions`

> 请求示例
    
    
    GET /api/v5/copytrading/current-subpositions?instId=BTC-USDT-SWAP
    
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 否 | 产品类型  
SPOT：币币  
SWAP：永续合约  
默认返回所有业务线的信息  
instId | String | 否 | 产品ID ，如`BTC-USDT-SWAP`  
after | String | 否 | 请求此id之前（更旧的数据）的分页内容，传的值为对应接口的`subPosId`  
before | String | 否 | 请求此id之后（更新的数据）的分页内容，传的值为对应接口的`subPosId`  
limit | String | 否 | 分页返回的结果集数量，最大为500，不填默认返回500条  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "algoId": "",
                "ccy": "USDT",
                "instId": "BTC-USDT-SWAP",
                "instType": "SWAP",
                "lever": "3",
                "margin": "12.6417",
                "markPx": "38205.8",
                "mgnMode": "isolated",
                "openAvgPx": "37925.1",
                "openOrdId": "",
                "openTime": "1701231120479",
                "posSide": "net",
                "slOrdPx": "",
                "slTriggerPx": "",
                "subPos": "1",
                "subPosId": "649945658862370816",
                "tpOrdPx": "",
                "tpTriggerPx": "",
                "uniqueCode": "25CD5A80241D6FE6",
                "upl": "0.2807",
                "uplRatio": "0.0222042921442527",
                "availSubPos": "1"
            },
            {
                "algoId": "",
                "ccy": "USDT",
                "instId": "BTC-USDT-SWAP",
                "instType": "SWAP",
                "lever": "3",
                "margin": "12.6263333333333333",
                "markPx": "38205.8",
                "mgnMode": "isolated",
                "openAvgPx": "37879",
                "openOrdId": "",
                "openTime": "1701225074786",
                "posSide": "net",
                "slOrdPx": "",
                "slTriggerPx": "",
                "subPos": "1",
                "subPosId": "649920301388038144",
                "tpOrdPx": "",
                "tpTriggerPx": "",
                "uniqueCode": "25CD5A80241D6FE6",
                "upl": "0.3268",
                "uplRatio": "0.0258824150584758",
                "availSubPos": "1"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
instId | String | 产品ID  
subPosId | String | 带单仓位ID  
posSide | String | 持仓方向  
long：开平仓模式开多   
short：开平仓模式开空   
net：买卖模式（subPos为正代表开多，subPos为负代表开空）  
mgnMode | String | 保证金模式，`isolated`：逐仓 ；`cross`：全仓  
lever | String | 杠杆倍数  
openOrdId | String | 交易员开仓订单号，仅适用于带单仓位  
openAvgPx | String | 开仓均价  
openTime | String | 开仓时间  
subPos | String | 持仓张数  
tpTriggerPx | String | 止盈触发价  
slTriggerPx | String | 止损触发价  
algoId | String | 止盈止损委托单ID  
instType | String | 产品类型  
SPOT：币币  
SWAP：永续合约  
tpOrdPx | String | 止盈委托价，市价时为-1  
slOrdPx | String | 止损委托价，市价时为-1  
margin | String | 保证金  
upl | String | 未实现收益  
uplRatio | String | 未实现收益率  
markPx | String | 最新标记价格，仅适用于合约  
uniqueCode | String | 交易员唯一标识代码  
ccy | String | 保证金币种  
availSubPos | String | 可平张数/币数