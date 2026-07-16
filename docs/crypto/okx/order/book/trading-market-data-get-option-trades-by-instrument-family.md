---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-market-data-get-option-trades-by-instrument-family
anchor_id: order-book-trading-market-data-get-option-trades-by-instrument-family
api_type: API
updated_at: 2026-07-16 19:20:30.292255
---

# GET / Option trades by instrument family

Retrieve the recent transactions of an instrument under same instFamily. The maximum is 100.  
  
#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/market/option/instrument-family-trades`

> Request Example
    
    
    GET /api/v5/market/option/instrument-family-trades?instFamily=BTC-USD
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instFamily | String | Yes | Instrument family, e.g. BTC-USD  
Applicable to `OPTION`  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "vol24h": "103381",
                "tradeInfo": [
                    {
                        "instId": "BTC-USD-221111-17750-C",
                        "side": "sell",
                        "sz": "1",
                        "px": "0.0075",
                        "tradeId": "20",
                        "ts": "1668090715058"
                    },
                    {
                        "instId": "BTC-USD-221111-17750-C",
                        "side": "sell",
                        "sz": "91",
                        "px": "0.01",
                        "tradeId": "19",
                        "ts": "1668090421062"
                    }
                ],
                "optType": "C"
            },
            {
                "vol24h": "144499",
                "tradeInfo": [
                    {
                        "instId": "BTC-USD-230127-10000-P",
                        "side": "sell",
                        "sz": "82",
                        "px": "0.019",
                        "tradeId": "23",
                        "ts": "1668090967057"
                    },
                    {
                        "instId": "BTC-USD-221111-16250-P",
                        "side": "sell",
                        "sz": "102",
                        "px": "0.0045",
                        "tradeId": "24",
                        "ts": "1668090885050"
                    }
                ],
                "optType": "P"
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
vol24h | String | 24h trading volume, with a unit of contract.  
optType | String | Option type, C: Call P: Put  
tradeInfo | Array of objects | The list trade data  
> instId | String | The Instrument ID  
> tradeId | String | Trade ID  
> px | String | Trade price  
> sz | String | Trade quantity. The unit is contract.  
> side | String | Trade side  
`buy`  
`sell`  
> ts | String | Trade time, Unix timestamp format in milliseconds, e.g. 1597026383085.

---

# GET / 获取期权品种公共成交数据

查询期权同一个交易品种下的成交信息数据，最多返回100条。  
  
#### 限速：20次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/market/option/instrument-family-trades`

> 请求示例
    
    
    GET /api/v5/market/option/instrument-family-trades?instFamily=BTC-USD
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instFamily | String | 是 | 交易品种，如 BTC-USD，适用于期权  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "vol24h": "103381",
                "tradeInfo": [
                    {
                        "instId": "BTC-USD-221111-17750-C",
                        "side": "sell",
                        "sz": "1",
                        "px": "0.0075",
                        "tradeId": "20",
                        "ts": "1668090715058"
                    },
                    {
                        "instId": "BTC-USD-221111-17750-C",
                        "side": "sell",
                        "sz": "91",
                        "px": "0.01",
                        "tradeId": "19",
                        "ts": "1668090421062"
                    }
                ],
                "optType": "C"
            },
            {
                "vol24h": "144499",
                "tradeInfo": [
                    {
                        "instId": "BTC-USD-230127-10000-P",
                        "side": "sell",
                        "sz": "82",
                        "px": "0.019",
                        "tradeId": "23",
                        "ts": "1668090967057"
                    },
                    {
                        "instId": "BTC-USD-221111-16250-P",
                        "side": "sell",
                        "sz": "102",
                        "px": "0.0045",
                        "tradeId": "24",
                        "ts": "1668090885050"
                    }
                ],
                "optType": "P"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
vol24h | String | 24小时成交量，以张为单位  
optType | String | 期权类型，`C`：看涨期权 `P`：看跌期权  
tradeInfo | Array of objects | 成交数据列表  
> instId | String | 产品ID  
> tradeId | String | 成交ID  
> px | String | 成交价格  
> sz | String | 成交数量，单位为张。  
> side | String | 成交方向  
`buy`：买  
`sell`：卖  
> ts | String | 成交时间，Unix时间戳的毫秒数格式， 如1597026383085