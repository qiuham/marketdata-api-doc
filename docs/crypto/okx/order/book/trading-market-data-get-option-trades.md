---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-market-data-get-option-trades
anchor_id: order-book-trading-market-data-get-option-trades
api_type: API
updated_at: 2026-06-29 19:56:40.160475
---

# GET / Option trades

The maximum is 100.  
  
#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/public/option-trades`

> Request Example
    
    
    GET /api/v5/public/option-trades?instFamily=BTC-USD
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instId | String | Conditional | Instrument ID, e.g. BTC-USD-221230-4000-C, Either `instId` or `instFamily` is required. If both are passed, `instId` will be used.  
instFamily | String | Conditional | Instrument family, e.g. BTC-USD  
optType | String | No | Option type, `C`: Call `P`: put  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "fillVol": "0.24415013671875",
                "fwdPx": "16676.907614127158",
                "idxPx": "16667",
                "instFamily": "BTC-USD",
                "instId": "BTC-USD-221230-16600-P",
                "markPx": "0.006308943261227884",
                "optType": "P",
                "px": "0.005",
                "side": "sell",
                "sz": "30",
                "tradeId": "65",
                "ts": "1672225112048"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instId | String | Instrument ID  
instFamily | String | Instrument family  
tradeId | String | Trade ID  
px | String | Trade price  
sz | String | Trade quantity. The unit is contract.  
side | String | Trade side   
`buy`   
`sell`  
optType | String | Option type, C: Call P: Put  
fillVol | String | Implied volatility while trading (Correspond to trade price)  
fwdPx | String | Forward price while trading  
idxPx | String | Index price while trading  
markPx | String | Mark price while trading  
ts | String | Trade time, Unix timestamp format in milliseconds, e.g. `1597026383085`.

---

# GET / 获取期权公共成交数据

最多返回最近的100条成交数据  
  
#### 限速：20次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/public/option-trades`

> 请求示例
    
    
    GET /api/v5/public/option-trades?instFamily=BTC-USD
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instId | String | 可选 | 产品ID，如 BTC-USD-221230-4000-C，`instId` 和 `instFamily` 必须传一个，若传两个，以 `instId` 为主  
instFamily | String | 可选 | 交易品种，如 BTC-USD  
optType | String | 否 | 期权类型，`C`：看涨期权 `P`：看跌期权  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "fillVol": "0.24415013671875",
                "fwdPx": "16676.907614127158",
                "idxPx": "16667",
                "instFamily": "BTC-USD",
                "instId": "BTC-USD-221230-16600-P",
                "markPx": "0.006308943261227884",
                "optType": "P",
                "px": "0.005",
                "side": "sell",
                "sz": "30",
                "tradeId": "65",
                "ts": "1672225112048"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
instId | String | 产品ID  
instFamily | String | 交易品种  
tradeId | String | 成交ID  
px | String | 成交价格  
sz | String | 成交数量。单位为张。  
side | String | 成交方向   
`buy`：买   
`sell`：卖  
optType | String | 期权类型，C：看涨期权 P：看跌期权 ，仅适用于期权  
fillVol | String | 成交时的隐含波动率（对应成交价格）  
fwdPx | String | 成交时的远期价格  
idxPx | String | 成交时的指数价格  
markPx | String | 成交时的标记价格  
ts | String | 成交时间，Unix时间戳的毫秒数格式， 如`1597026383085`