---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#financial-product-dual-investment-get-currency-pairs
anchor_id: financial-product-dual-investment-get-currency-pairs
api_type: API
updated_at: 2026-07-20 19:37:44.905254
---

# GET / Currency pairs

Returns available dual investment currency pairs.  
  
#### Rate Limit: 1 request per second

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/finance/sfp/dcd/currency-pair`

> Request Example
    
    
    GET /api/v5/finance/sfp/dcd/currency-pair
    

#### Request Parameters

None

> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "baseCcy": "BTC",
                "quoteCcy": "USDT",
                "optType": "C",
                "uly": "BTC-USD"
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
baseCcy | String | Base currency  
quoteCcy | String | Quote currency  
optType | String | Option type  
`C`: Call  
`P`: Put  
uly | String | Underlying

---

# GET / 获取币对

获取双币赢币对  
  
#### 限速：1次/s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/finance/sfp/dcd/currency-pair`

> 请求示例
    
    
    GET /api/v5/finance/sfp/dcd/currency-pair
    

#### 请求参数

无

> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "baseCcy": "BTC",
                "quoteCcy": "USDT",
                "optType": "C",
                "uly": "BTC-USD"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
baseCcy | String | 基础币种  
quoteCcy | String | 报价币种  
optType | String | 期权类型  
`C`：看涨  
`P`：看跌  
uly | String | 标的