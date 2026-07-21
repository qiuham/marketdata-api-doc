---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#funding-account-rest-api-buy-sell-trade
anchor_id: funding-account-rest-api-buy-sell-trade
api_type: REST
updated_at: 2026-07-21 19:27:27.266634
---

# Buy/sell trade

#### Rate Limit: 1 request per 5 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/fiat/buy-sell/trade`

> Request Example
    
    
    # Sell 30 USD to buy BTC
    POST /api/v5/fiat/buy-sell/trade
    body
    {
        "clOrdId":"123456",
        "side":"sell",
        "fromCcy": "USD",
        "toCcy": "BTC",
        "rfqAmt": "30",
        "rfqCcy": "USD",
        "paymentMethod":"balance",
        "quoteId": "quoterETH-USDT16461885104612381"
    }
    

#### Request Parameters

Parameters | Types | Required | Description  
---|---|---|---  
quoteId | String | Yes | Quote ID  
Get from Buy/Sell quote API  
side | String | Yes | Side   
`buy`: Buy Crypto / Fiat with Fiat   
`sell`: Sell Crypto to Crypto / Fiat   
Should be the same as the Quote request  
fromCcy | String | Yes | Currency to sell   
Should be the same as the Quote request  
toCcy | String | Yes | Currency to buy   
Should be the same as the Quote request  
rfqAmt | String | Yes | RFQ amount   
Should be the same as the Quote request  
rfqCcy | String | Yes | RFQ currency   
Should be the same as the Quote request  
paymentMethod | String | Yes | paymentMethod   
`balance`  
clOrdId | String | Yes | Client Order ID as assigned by the client   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "ordId": "1234",
                "clOrdId": "",
                "quoteId": "quoterBTC-USD16461885104612381",
                "side":"buy",
                "fromCcy": "USD",
                "toCcy": "BTC",
                "rfqAmt": "30",
                "rfqCcy": "USD",
                "fillPx": "2932.40104429",
                "fillQuoteCcy": "USD",
                "fillFromAmt": "30",
                "fillToAmt": "0.01",
                "cTime": "1646188510461"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ordId | String | Order ID  
clOrdId | String | Client Order ID as assigned by the client  
quoteId | String | Quote ID  
state | String | Trade state   
`processing`   
`completed`   
`failed`  
side | String | Side   
`buy`: Buy Crypto / Fiat with Fiat   
`sell`: Sell Crypto to Crypto / Fiat  
fromCcy | String | Currency to sell  
toCcy | String | Currency to buy  
rfqAmt | String | RFQ amount  
rfqCcy | String | RFQ currency  
fillPx | String | Filled price based on quote currency  
fillQuoteCcy | String | Filled price quote currency   
e.g. `USD`  
fillFromAmt | String | Sold amount, unit in `fromCcy`  
fillToAmt | String | Bought amount, unit in `toCcy`  
cTime | String | Request time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
This feature is only available to Bahamas institutional users at the moment.

---

# 买卖交易

#### 限速：1次/5s

#### 限速规则：User ID

#### HTTP 请求

`POST /api/v5/fiat/buy-sell/trade`

> 请求示例
    
    
    # 卖出30 USD买入BTC
    POST /api/v5/fiat/buy-sell/trade
    body
    {
        "clOrdId":"123456",
        "side":"sell",
        "fromCcy": "USD",
        "toCcy": "BTC",
        "rfqAmt": "30",
        "rfqCcy": "USD",
        "paymentMethod":"balance",
        "quoteId": "quoterETH-USDT16461885104612381"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
quoteId | String | 是 | 报价ID  
从获取买卖交易报价API获取  
side | String | 是 | 交易方向  
`buy`: 使用法币购买加密货币/法币  
`sell`: 将加密货币出售为加密货币/法币  
必须与报价请求一致  
fromCcy | String | 是 | 卖出币种  
必须与报价请求一致  
toCcy | String | 是 | 买入币种  
必须与报价请求一致  
rfqAmt | String | 是 | 询价数量  
必须与报价请求一致  
rfqCcy | String | 是 | 询价币种  
必须与报价请求一致  
paymentMethod | String | 是 | 支付方式  
`balance`  
clOrdId | String | 是 | 用户自定义的订单标识  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度要在1-32位之间  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "ordId": "1234",
                "clOrdId": "",
                "quoteId": "quoterBTC-USD16461885104612381",
                "side":"buy",
                "fromCcy": "USD",
                "toCcy": "BTC",
                "rfqAmt": "30",
                "rfqCcy": "USD",
                "fillPx": "2932.40104429",
                "fillQuoteCcy": "USD",
                "fillFromAmt": "30",
                "fillToAmt": "0.01",
                "cTime": "1646188510461"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ordId | String | 订单ID  
clOrdId | String | 用户自定义的订单标识  
quoteId | String | 报价ID  
state | String | 交易状态  
`processing`：处理中  
`completed`：已完成  
`failed`：失败  
side | String | 交易方向  
`buy`: 使用法币购买加密货币/法币  
`sell`: 将加密货币出售为加密货币/法币  
fromCcy | String | 卖出币种  
toCcy | String | 买入币种  
rfqAmt | String | 询价数量  
rfqCcy | String | 询价币种  
fillPx | String | 成交价格，单位为报价币种  
fillQuoteCcy | String | 成交价格报价币种  
如 `USD`  
fillFromAmt | String | 卖出数量，单位为 `fromCcy`  
fillToAmt | String | 买入数量，单位为 `toCcy`  
cTime | String | 请求时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
此功能目前仅对巴哈马机构用户开放。