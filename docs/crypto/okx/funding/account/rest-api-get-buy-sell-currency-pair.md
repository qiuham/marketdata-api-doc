---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#funding-account-rest-api-get-buy-sell-currency-pair
anchor_id: funding-account-rest-api-get-buy-sell-currency-pair
api_type: REST
updated_at: 2026-06-29 19:57:43.386314
---

# Get buy/sell currency pair

#### Rate Limit: 6 requests per second

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/fiat/buy-sell/currency-pair`

> Request Example
    
    
    GET /api/v5/fiat/buy-sell/currency-pair?fromCcy=USD&toCcy=BTC
    

#### Request Parameters

Parameters | Types | Required | Description  
---|---|---|---  
fromCcy | String | Yes | Currency to sell, e.g. `USD`  
toCcy | String | Yes | Currency to buy, e.g. `BTC`  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "side": "buy",
                "fromCcy": "USD",
                "toCcy": "BTC",
                "singleTradeMax": "1",
                "singleTradeMin": "0.01",
                "fixedPxRemainingDailyQuota": "", 
                "fixedPxDailyLimit": "", 
                "paymentMethods":["balance"]
            }
        ],
        "msg": ""
    }
    
    
    
    {
        "code": "0",
        "data": [
            {
                "side": "sell",
                "fromCcy": "BTC",
                "toCcy": "USD",
                "singleTradeMax": "1",
                "singleTradeMin": "0.01",
                "fixedPxRemainingDailyQuota": "", 
                "fixedPxDailyLimit": "", 
                "paymentMethods":["balance"]
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
side | String | Side  
`buy`: Fiat to crypto  
`sell`: Crypto to fiat  
May support both sides in the future, separated with a comma, e.g. `buy,sell`.  
fromCcy | String | Currency to sell, e.g. `USD`  
toCcy | String | Currency to buy, e.g. `BTC`  
singleTradeMax | String | The maximum amount of currency for a single trade, unit in `fromCcy`  
singleTradeMin | String | The minimum amount of currency for a single trade, unit in `fromCcy`  
fixedPxDailyLimit | String | Fixed price daily limit  
Applicable to Fiat to Fiat trade, else return ''.  
If `side` = `buy`, unit in `fromCcy`  
If `side` = `sell`, unit in `toCcy`  
fixedPxRemainingDailyQuota | String | Fixed price remaining daily quota  
Applicable to Fiat to Fiat trade, else return ''.  
If `side` = `buy`, unit in `fromCcy`  
If `side` = `sell`, unit in `toCcy`  
paymentMethods | Array of strings | Supported payment methods  
`balance`  
e.g. ["balance"]  
  
This feature is only available to Bahamas institutional users at the moment.

---

# 获取买卖交易币对

#### 限速：6次/s

#### 限速规则：User ID

#### 权限：读取

#### HTTP 请求

`GET /api/v5/fiat/buy-sell/currency-pair`

> 请求示例
    
    
    GET /api/v5/fiat/buy-sell/currency-pair?fromCcy=USD&toCcy=BTC
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
fromCcy | String | 是 | 卖出币种，如 `USD`  
toCcy | String | 是 | 买入币种，如 `BTC`  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "side": "buy",
                "fromCcy": "USD",
                "toCcy": "BTC",
                "singleTradeMax": "1",
                "singleTradeMin": "0.01",
                "fixedPxRemainingDailyQuota": "", 
                "fixedPxDailyLimit": "", 
                "paymentMethods":["balance"]
            }
        ],
        "msg": ""
    }
    
    {
        "code": "0",
        "data": [
            {
                "side": "sell",
                "fromCcy": "BTC",
                "toCcy": "USD",
                "singleTradeMax": "1",
                "singleTradeMin": "0.01",
                "fixedPxRemainingDailyQuota": "", 
                "fixedPxDailyLimit": "", 
                "paymentMethods":["balance"]
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
side | String | 交易方向  
`buy`: 使用法币购买加密货币/法币  
`sell`: 将加密货币出售为加密货币/法币  
未来可能同时支持双向交易，以逗号分隔，如 `buy,sell`  
fromCcy | String | 卖出币种，如 `USD`  
toCcy | String | 买入币种，如 `BTC`  
singleTradeMax | String | 单笔交易最大数量，单位为 `fromCcy`  
singleTradeMin | String | 单笔交易最小数量，单位为 `fromCcy`  
fixedPxDailyLimit | String | 固定价格每日限额  
仅适用于法币间交易，否则返回空字符串  
当`side` = `buy`时，单位为 `fromCcy`  
当`side` = `sell`时，单位为 `toCcy`  
fixedPxRemainingDailyQuota | String | 固定价格剩余每日限额  
仅适用于法币间交易，否则返回空字符串  
当`side` = `buy`时，单位为 `fromCcy`  
当`side` = `sell`时，单位为 `toCcy`  
paymentMethods | Array of strings | 支持的支付方式  
`balance`  
例如：["balance"]  
此功能目前仅对巴哈马机构用户开放。