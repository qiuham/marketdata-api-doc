---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#block-trading-rest-api-get-quote-products
anchor_id: block-trading-rest-api-get-quote-products
api_type: REST
updated_at: 2026-07-22 19:20:01.302963
---

# Get Quote products

Retrieve the products which makers want to quote and receive RFQs for, and the corresponding price and size limit. 

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/rfq/maker-instrument-settings`

> Request Example
    
    
    GET /api/v5/rfq/maker-instrument-settings
    

#### Request parameters

None

> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "instType": "OPTION",
                "includeAll": true,
                "data": [
                    {
                        "instFamily": "BTC-USD",
                        "maxBlockSz": "10000",
                        "makerPxBand": "5"
                    },
                    {
                        "instFamily": "SOL-USD",
                        "maxBlockSz": "100000",
                        "makerPxBand": "15"
                    }
                ]
            },
            {
                "instType": "FUTURES",
                "includeAll": false,
                "data": [
                    {
                        "instFamily": "BTC-USD",
                        "maxBlockSz": "10000",
                        "makerPxBand": "5"
                    },
                    {
                        "instFamily": "ETH-USDT",
                        "maxBlockSz": "100000",
                        "makerPxBand": "15"
                    }
                ]
            },
            {
                "instType:": "SWAP",
                "includeAll": false,
                "data": [
                    {
                        "instFamily": "BTC-USD",
                        "maxBlockSz": "10000",
                        "makerPxBand": "5"
                    },
                    {
                        "instFamily": "ETH-USDT"
                    }
                ]
            },
            {
                "instType:": "SPOT",
                "includeAll": false,
                "data": [
                    {
                        "instId": "BTC-USDT"
                    },
                    {
                        "instId": "TRX-USDT"
                    }
                ]
            }
        ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
code | String | The result code, `0` means success.  
msg | String | The error message, not empty if the code is not `0`.  
data | Array of objects | Return data of the request.  
> instType | String | Type of instrument. Valid value can be `FUTURES`, `OPTION`, `SWAP` or `SPOT`.  
> includeAll | Boolean | Receive all instruments or not under specific instType setting.   
Valid value can be boolean (`True`/`False`). By default, the value will be `false`.  
> data | Array of objects | Elements of the instType.  
>> instFamily | String | Instrument family. Required for `FUTURES`, `OPTION` and `SWAP` only.  
>> instId | String | Instrument ID. Required for `SPOT` only.  
>> maxBlockSz | String | Max trade quantity for the product(s).   
For `FUTURES`, `OPTION` and `SWAP`, the max quantity of the RFQ/Quote is in unit of contracts. For `SPOT`, this parameter is in base currency.  
>> makerPxBand | String | Price bands in unit of ticks, measured against mark price.   
Setting makerPxBand to 1 tick means:   
If Bid price > Mark + 1 tick, it will be stopped   
If Ask price < Mark - 1 tick, It will be stopped

---

# 获取可报价产品

用于maker查询特定的接受询价和报价的产品, 以及数量和价格范围。

#### 限速: 5次/2s

#### 限速规则：User ID

#### HTTP Requests

`GET /api/v5/rfq/maker-instrument-settings`

> 请求示例
    
    
    GET /api/v5/rfq/maker-instrument-settings
    

#### 请求参数

无

> 返回示例
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "instType": "OPTION",
                "includeAll": true,
                "data": [
                    {
                        "instFamily": "BTC-USD",
                        "maxBlockSz": "10000",
                        "makerPxBand": "5"
                    },
                    {
                        "instFamily": "SOL-USD",
                        "maxBlockSz": "100000",
                        "makerPxBand": "15"
                    }
                ]
            },
            {
                "instType": "FUTURES",
                "includeAll": false,
                "data": [
                    {
                        "instFamily": "BTC-USD",
                        "maxBlockSz": "10000",
                        "makerPxBand": "5"
                    },
                    {
                        "instFamily": "ETH-USDT",
                        "maxBlockSz": "100000",
                        "makerPxBand": "15"
                    }
                ]
            },
            {
                "instType:": "SWAP",
                "includeAll": false,
                "data": [
                    {
                        "instFamily": "BTC-USD",
                        "maxBlockSz": "10000",
                        "makerPxBand": "5"
                    },
                    {
                        "instFamily": "ETH-USDT"
                    }
                ]
            },
            {
                "instType:": "SPOT",
                "includeAll": false,
                "data": [
                    {
                        "instId": "BTC-USDT"
                    },
                    {
                        "instId": "TRX-USDT"
                    }
                ]
            }
        ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
code | String | 结果代码，`0` 表示成功  
msg | String | 错误信息，如果代码不为`0`，则不为空  
data | Array of objects | 请求返回值，包含请求结果  
> instType | String | 产品类别，枚举值包括`FUTURES`,`OPTION`,`SWAP`和`SPOT`  
> includeAll | Boolean | 是否接收该instType下所有产品。有效值为`true`或`false`。默认`false`。  
> data | Array of objects | instType的元素  
>> instFamily | String | 交易品种  
`交割`/`永续`/`期权`情况下必填  
>> instId | String | 产品ID，如 `BTC-USDT`。对`SPOT`产品类别有效且必须。  
>> maxBlockSz | String | 该种产品最大可交易数量。FUTURES, OPTION and SWAP 的单位是合约数量。SPOT的单位是交易货币。  
>> makerPxBand | String | 价格限制以价格精度tick为单位，以标记价格为基准。  
设置makerPxBand为1个tick代表:   
如果买一价 > 标记价格 + 1 tick, 操作将被拦截   
如果 买一价 < 标记价格 - 1 tick, 操作将被拦截