---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#funding-account-rest-api-get-buy-sell-trade-history
anchor_id: funding-account-rest-api-get-buy-sell-trade-history
api_type: REST
updated_at: 2026-07-15 19:20:28.220498
---

# Get buy/sell trade history

#### Rate Limit: 6 requests per second

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/fiat/buy-sell/history`

> Request Example
    
    
    GET /api/v5/fiat/buy-sell/history
    

#### Request Parameters

Parameters | Types | Required | Description  
---|---|---|---  
ordId | String | No | Order ID  
clOrdId | String | No | Client Order ID as assigned by the client   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
state | String | No | Trade state   
`processing`   
`completed`   
`failed`  
begin | String | No | Filter with a begin timestamp. Unix timestamp format in milliseconds, e.g. `1597026383085`  
end | String | No | Filter with an end timestamp. Unix timestamp format in milliseconds, e.g. `1597026383085`  
limit | String | No | Number of results per request. The maximum is 100. The default is 100.  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "ordId": "1234",
                "clOrdId": "",
                "quoteId": "quoterBTC-USD16461885104612381",
                "state":"completed",
                "side":"buy",
                "fromCcy": "USD",
                "toCcy": "BTC",
                "rfqAmt": "30",
                "rfqCcy": "USD",
                "fillPx": "2932.40104429",
                "fillQuoteCcy": "USD",
                "fillFromAmt": "30",
                "fillToAmt": "0.01",
                "cTime": "1646188510461",
                "uTime": "1646188510461"
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
fromCcy | String | Currency to sell  
toCcy | String | Currency to buy  
rfqAmt | String | RFQ amount  
rfqCcy | String | RFQ currency  
fillPx | String | Filled price based on quote currency  
fillQuoteCcy | String | Filled price quote currency   
e.g. `USD`  
fillFromAmt | String | Filled amount unit in fromCcy  
fillToAmt | String | Filled amount unit in toCcy  
cTime | String | Request time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
uTime | String | Updated time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
This feature is only available to Bahamas institutional users at the moment.

---

# 获取买卖交易历史

#### 限速：6次/s

#### 限速规则：User ID

#### 权限：读取

#### HTTP 请求

`GET /api/v5/fiat/buy-sell/history`

> 请求示例
    
    
    GET /api/v5/fiat/buy-sell/history
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
ordId | String | 否 | 订单ID  
clOrdId | String | 否 | 用户自定义的订单标识  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度要在1-32位之间  
state | String | 否 | 交易状态  
`processing`：处理中  
`completed`：已完成  
`failed`：失败  
begin | String | 否 | 开始时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
end | String | 否 | 结束时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
limit | String | 否 | 返回的结果集数量，默认为100，最大为100  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "ordId": "1234",
                "clOrdId": "",
                "quoteId": "quoterBTC-USD16461885104612381",
                "state":"completed",
                "side":"buy",
                "fromCcy": "USD",
                "toCcy": "BTC",
                "rfqAmt": "30",
                "rfqCcy": "USD",
                "fillPx": "2932.40104429",
                "fillQuoteCcy": "USD",
                "fillFromAmt": "30",
                "fillToAmt": "0.01",
                "cTime": "1646188510461",
                "uTime": "1646188510461"
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
fromCcy | String | 卖出币种  
toCcy | String | 买入币种  
rfqAmt | String | 询价数量  
rfqCcy | String | 询价币种  
fillPx | String | 成交价格，单位为报价币种  
fillQuoteCcy | String | 成交价格报价币种  
如 `USD`  
fillFromAmt | String | 成交数量，单位为 `fromCcy`  
fillToAmt | String | 成交数量，单位为 `toCcy`  
cTime | String | 请求时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
uTime | String | 更新时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
此功能目前仅对巴哈马机构用户开放。