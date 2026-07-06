---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#funding-account-rest-api-get-buy-sell-currencies
anchor_id: funding-account-rest-api-get-buy-sell-currencies
api_type: REST
updated_at: 2026-07-06 19:54:32.083551
---

# Get buy/sell currencies

#### Rate Limit: 6 requests per second  
  
#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/fiat/buy-sell/currencies`

> Request Example
    
    
    GET /api/v5/fiat/buy-sell/currencies
    

> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
               "fiatCcyList":[
                    {
                        "ccy": "USD"
                    },
                    {
                        "ccy": "EUR"
                    },
                    ...
                ],
                "cryptoCcyList":[
                    {
                        "ccy": "BTC"
                    },
                    ...
                ],
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
fiatCcyList | Array of objects | Fiat currency list  
>ccy | String | Currency, e.g. `BTC`  
cryptoCcyList | Array of objects | Crypto currency list  
>ccy | String | Currency, e.g. `USD`  
  
This feature is only available to Bahamas institutional users at the moment.

---

# 获取买卖交易币种

#### 限速：6次/s  
  
#### 限速规则：User ID

#### 权限：读取

#### HTTP 请求

`GET /api/v5/fiat/buy-sell/currencies`

> 请求示例
    
    
    GET /api/v5/fiat/buy-sell/currencies
    

> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
               "fiatCcyList":[
                    {
                        "ccy": "USD"
                    },
                    {
                        "ccy": "EUR"
                    },
                    ...
                ],
                "cryptoCcyList":[
                    {
                        "ccy": "BTC"
                    },
                    ...
                ],
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
fiatCcyList | Array of objects | 法币列表  
>ccy | String | 币种，如 `BTC`  
cryptoCcyList | Array of objects | 加密货币列表  
>ccy | String | 币种，如 `USD`  
此功能目前仅对巴哈马机构用户开放。