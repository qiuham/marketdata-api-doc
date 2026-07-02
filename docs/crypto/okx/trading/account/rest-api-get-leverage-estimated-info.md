---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#trading-account-rest-api-get-leverage-estimated-info
anchor_id: trading-account-rest-api-get-leverage-estimated-info
api_type: REST
updated_at: 2026-07-02 19:42:52.380679
---

# Get leverage estimated info

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/account/adjust-leverage-info`

> Request Example
    
    
    GET /api/v5/account/adjust-leverage-info?instType=MARGIN&mgnMode=isolated&lever=3&instId=BTC-USDT
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | Yes | Instrument type  
`MARGIN`  
`SWAP`  
`FUTURES`  
mgnMode | String | Yes | Margin mode  
`isolated`  
`cross`  
lever | String | Yes | Leverage  
instId | String | Conditional | Instrument ID, e.g. BTC-USDT  
It is required for these scenarioes: `SWAP` and `FUTURES`, Margin isolation, Margin cross in `Futures mode`.  
ccy | String | Conditional | Currency used for margin, e.g. BTC  
It is required for isolated margin and cross margin in `Futures mode`, `Multi-currency margin` and `Portfolio margin`  
posSide | String | No | posSide  
`net`: The default value  
`long`  
`short`  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "estAvailQuoteTrans": "",
                "estAvailTrans": "1.1398040558348279",
                "estLiqPx": "",
                "estMaxAmt": "10.6095865868904898",
                "estMgn": "0.0701959441651721",
                "estQuoteMaxAmt": "176889.6871254563042714",
                "estQuoteMgn": "",
                "existOrd": false,
                "maxLever": "10",
                "minLever": "0.01"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
estAvailQuoteTrans | String | The estimated margin(in quote currency) can be transferred out under the corresponding leverage  
For cross, it is the maximum quantity that can be transferred from the trading account.  
For isolated, it is the maximum quantity that can be transferred from the isolated position  
Only applicable to `MARGIN`  
estAvailTrans | String | The estimated margin can be transferred out under the corresponding leverage.  
For cross, it is the maximum quantity that can be transferred from the trading account.  
For isolated, it is the maximum quantity that can be transferred from the isolated position  
The unit is base currency for `MARGIN`  
It is not applicable to the scenario when increasing leverage for isolated position under `FUTURES` and `SWAP`  
estLiqPx | String | The estimated liquidation price under the corresponding leverage. Only return when there is a position.  
estMgn | String | The estimated margin needed by position under the corresponding leverage.  
For the `MARGIN` position, it is margin in base currency  
estQuoteMgn | String | The estimated margin (in quote currency) needed by position under the corresponding leverage  
estMaxAmt | String | For `MARGIN`, it is the estimated maximum loan in base currency under the corresponding leverage  
For `SWAP` and `FUTURES`, it is the estimated maximum quantity of contracts that can be opened under the corresponding leverage  
estQuoteMaxAmt | String | The `MARGIN` estimated maximum loan in quote currency under the corresponding leverage.  
existOrd | Boolean | Whether there is pending orders   
`true`  
`false`  
maxLever | String | Maximum leverage  
minLever | String | Minimum leverage

---

# 获取杠杆倍数预估信息

获取指定杠杆倍数下，相关的预估信息。

#### 限速：5次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/account/adjust-leverage-info`

> 请求示例
    
    
    GET /api/v5/account/adjust-leverage-info?instType=MARGIN&mgnMode=isolated&lever=3&instId=BTC-USDT
    
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 是 | 产品类型  
`MARGIN`：币币杠杆  
`SWAP`：永续合约  
`FUTURES`：交割合约  
mgnMode | String | 是 | 保证金模式  
`isolated`：逐仓  
`cross`：全仓  
lever | String | 是 | 杠杆倍数  
instId | String | 可选 | 产品ID，如 `BTC-USDT`  
必填的场景有：交割永续，逐仓杠杆，以及`合约模式`下全仓杠杆。  
ccy | String | 可选 | 保证金币种，如 `BTC`  
逐仓杠杆及`合约模式`/`跨币种保证金模式`/`组合保证金模式`的全仓杠杆时必填。  
posSide | String | 否 | 持仓方向  
`net`: 默认值，代表买卖模式  
`long`: 开平模式下的多仓  
`short`：开平模式下的空仓  
适用于`交割`/`永续`。  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "estAvailQuoteTrans": "",
                "estAvailTrans": "1.1398040558348279",
                "estLiqPx": "",
                "estMaxAmt": "10.6095865868904898",
                "estMgn": "0.0701959441651721",
                "estQuoteMaxAmt": "176889.6871254563042714",
                "estQuoteMgn": "",
                "existOrd": false,
                "maxLever": "10",
                "minLever": "0.01"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
estAvailQuoteTrans | String | 对应杠杆倍数下，计价货币预估可转出的保证金数量  
全仓时，为交易账户最大可转出  
逐仓时，为逐仓仓位可减少的保证金。  
仅适用于`杠杆`  
estAvailTrans | String | 对应杠杆倍数下，预估可转出的保证金数量  
全仓时，为交易账户最大可转出  
逐仓时，为逐仓仓位可减少的保证金  
对于`杠杆`，单位为交易货币  
不适用于`交割`, `永续`的逐仓，调大杠杆的场景  
estLiqPx | String | 对应杠杆倍数下的预估强平价，仅在有仓位时有值  
estMgn | String | 对应杠杆倍数下，仓位预估所需的保证金数量  
对于杠杆仓位，为所需交易货币保证金  
对于交割或永续仓位，为仓位所需保证金  
estQuoteMgn | String | 对应杠杆倍数下，仓位预估所需的计价货币保证金数量  
estMaxAmt | String | 对于杠杆，为对应杠杆倍数下，交易货币预估最大可借  
对于交割和永续，为对应杠杆倍数下，预估的最大可开张数  
estQuoteMaxAmt | String | 对应杠杆倍数下，杠杆计价货币预估最大可借  
existOrd | Boolean | 当前是否存在挂单   
`true`：存在挂单  
`false`：不存在挂单  
maxLever | String | 最大杠杆倍数  
minLever | String | 最小杠杆倍数