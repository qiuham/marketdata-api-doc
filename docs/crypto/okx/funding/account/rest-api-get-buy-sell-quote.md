---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#funding-account-rest-api-get-buy-sell-quote
anchor_id: funding-account-rest-api-get-buy-sell-quote
api_type: REST
updated_at: 2026-07-17 19:17:57.263171
---

# Get buy/sell quote

#### Rate Limit: 10 requests per second

#### Rate limit rule: User ID

#### Rate Limit: 1 request per 5 seconds

#### Rate limit rule: Instrument ID

#### HTTP Request

`POST /api/v5/fiat/buy-sell/quote`

> Request Example
    
    
    # Sell USD to buy 0.1 BTC
    POST /api/v5/fiat/buy-sell/quote
    body
    {
        "side":"buy",
        "fromCcy": "USD",
        "toCcy": "BTC",
        "rfqAmt": "0.1",
        "rfqCcy": "BTC"
    }
    
    # Sell 30 USD to buy BTC
    POST /api/v5/fiat/buy-sell/quote
    body
    {
        "side":"buy",
        "fromCcy": "USD",
        "toCcy": "BTC",
        "rfqAmt": "30",
        "rfqCcy": "USD"
    }
    
    # Sell BTC to buy 30 USD
    POST /api/v5/fiat/buy-sell/quote
    body
    {
        "side":"sell",
        "fromCcy": "BTC",
        "toCcy": "USD",
        "rfqAmt": "30",
        "rfqCcy": "USD"
    }
    
    # Sell 0.1 BTC to buy USD
    POST /api/v5/fiat/buy-sell/quote
    body
    {
        "side":"sell",
        "fromCcy": "BTC",
        "toCcy": "USD",
        "rfqAmt": "0.1",
        "rfqCcy": "BTC"
    }
    

#### Request Parameters

Parameters | Types | Required | Description  
---|---|---|---  
side | String | Yes | Side   
`buy`: Buy Crypto / Fiat with Fiat   
`sell`: Sell Crypto to Crypto / Fiat  
fromCcy | String | Yes | Currency to sell  
toCcy | String | Yes | Currency to buy  
rfqAmt | String | Yes | RFQ amount  
rfqCcy | String | Yes | RFQ currency  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "quoteId": "quoterBTC-USD16461885104612381",
                "fromCcy": "USD",
                "toCcy": "BTC",
                "rfqAmt": "30",
                "rfqCcy": "USD",
                "quotePx": "2932.40104429",
                "quoteCcy": "USD",
                "quoteFromAmt": "30",
                "quoteToAmt": "30",
                "quoteTime": "1646188510461",
                "ttlMs": "10000"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
quoteId | String | Quote ID  
side | String | Side   
`buy`: Buy Crypto / Fiat with Fiat   
`sell`: Sell Crypto to Crypto / Fiat  
fromCcy | String | Currency to sell, e.g. `USD`  
toCcy | String | Currency to buy, e.g. `BTC`  
rfqAmt | String | RFQ amount  
rfqCcy | String | RFQ currency  
quotePx | String | Quote price  
quoteCcy | String | Quote price unit   
e.g. `USD`  
quoteFromAmt | String | Quote amount, unit in `fromCcy`  
quoteToAmt | String | Quote amount, unit in `toCcy`  
quoteTime | String | Quotation generation time, Unix timestamp format in milliseconds, e.g. 1597026383085  
ttlMs | String | The validity period of quotation in milliseconds   
e.g. `10000` represents the quotation only valid for 10 seconds  
  
This feature is only available to Bahamas institutional users at the moment.

---

# 获取买卖交易报价

#### 限速：10次/s

#### 限速规则：User ID

#### 限速：1次/5s

#### 限速规则：Instrument ID

#### HTTP 请求

`POST /api/v5/fiat/buy-sell/quote`

> 请求示例
    
    
    # 卖出USD买入0.1 BTC
    POST /api/v5/fiat/buy-sell/quote
    body
    {
        "side":"buy",
        "fromCcy": "USD",
        "toCcy": "BTC",
        "rfqAmt": "0.1",
        "rfqCcy": "BTC"
    }
    
    # 卖出30 USD买入BTC
    POST /api/v5/fiat/buy-sell/quote
    body
    {
        "side":"buy",
        "fromCcy": "USD",
        "toCcy": "BTC",
        "rfqAmt": "30",
        "rfqCcy": "USD"
    }
    
    # 卖出BTC买入30 USD
    POST /api/v5/fiat/buy-sell/quote
    body
    {
        "side":"sell",
        "fromCcy": "BTC",
        "toCcy": "USD",
        "rfqAmt": "30",
        "rfqCcy": "USD"
    }
    
    # 卖出0.1 BTC买入USD
    POST /api/v5/fiat/buy-sell/quote
    body
    {
        "side":"sell",
        "fromCcy": "BTC",
        "toCcy": "USD",
        "rfqAmt": "0.1",
        "rfqCcy": "BTC"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
side | String | 是 | 交易方向  
`buy`: 法币买入加密货币  
`sell`: 加密货币卖出法币  
fromCcy | String | 是 | 卖出币种  
toCcy | String | 是 | 买入币种  
rfqAmt | String | 是 | 询价数量  
rfqCcy | String | 是 | 询价币种  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "quoteId": "quoterBTC-USD16461885104612381",
                "fromCcy": "USD",
                "toCcy": "BTC",
                "rfqAmt": "30",
                "rfqCcy": "USD",
                "quotePx": "2932.40104429",
                "quoteCcy": "USD",
                "quoteFromAmt": "30",
                "quoteToAmt": "30",
                "quoteTime": "1646188510461",
                "ttlMs": "10000"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
quoteId | String | 报价ID  
side | String | 交易方向  
`buy`: 使用法币购买加密货币/法币  
`sell`: 将加密货币出售为加密货币/法币  
fromCcy | String | 卖出币种，如 `USD`  
toCcy | String | 买入币种，如 `BTC`  
rfqAmt | String | 询价数量  
rfqCcy | String | 询价币种  
quotePx | String | 报价价格  
quoteCcy | String | 报价价格单位  
如 `USD`  
quoteFromAmt | String | 报价数量，单位为 `fromCcy`  
quoteToAmt | String | 报价数量，单位为 `toCcy`  
quoteTime | String | 报价生成时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
ttlMs | String | 报价有效期，单位为毫秒  
如 `10000` 表示报价仅10秒内有效  
此功能目前仅对巴哈马机构用户开放。