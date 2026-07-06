---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#funding-account-rest-api-get-convert-history
anchor_id: funding-account-rest-api-get-convert-history
api_type: REST
updated_at: 2026-07-06 19:54:29.262347
---

# Get convert history

#### Rate Limit: 6 requests per second  
  
#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/asset/convert/history`

> Request Example
    
    
    GET /api/v5/asset/convert/history
    
    

#### Request Parameters

**Parameters** | **Types** | **Required** | **Description**  
---|---|---|---  
clTReqId | String | No | Client Order ID as assigned by the client  
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
after | String | No | Pagination of data to return records earlier than the requested `ts`, Unix timestamp format in milliseconds, e.g. `1597026383085`  
before | String | No | Pagination of data to return records newer than the requested `ts`, Unix timestamp format in milliseconds, e.g. `1597026383085`  
limit | String | No | Number of results per request. The maximum is `100`. The default is `100`.  
tag | String | No | Order tag  
Applicable to broker user  
If the convert trading used `tag`, this parameter is also required.  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "clTReqId": "",
                "instId": "ETH-USDT",
                "side": "buy",
                "fillPx": "2932.401044",
                "baseCcy": "ETH",
                "quoteCcy": "USDT",
                "fillBaseSz": "0.01023052",
                "state": "fullyFilled",
                "tradeId": "trader16461885203381437",
                "fillQuoteSz": "30",
                "ts": "1646188520000"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
tradeId | String | Trade ID  
clTReqId | String | Client Order ID as assigned by the client  
state | String | Trade state  
`fullyFilled` : success   
`rejected` : failed  
instId | String | Currency pair, e.g. `BTC-USDT`  
baseCcy | String | Base currency, e.g. `BTC` in `BTC-USDT`  
quoteCcy | String | Quote currency, e.g. `USDT` in `BTC-USDT`  
side | String | Trade side based on `baseCcy`  
`buy` `sell`  
fillPx | String | Filled price based on quote currency  
fillBaseSz | String | Filled amount for base currency  
fillQuoteSz | String | Filled amount for quote currency  
ts | String | Convert trade time, Unix timestamp format in milliseconds, e.g. `1597026383085`

---

# 获取闪兑交易历史

#### 限速：6次/s  
  
#### 限速规则：User ID

#### 权限：读取

#### HTTP 请求

`GET /api/v5/asset/convert/history`

> 请求示例
    
    
    GET /api/v5/asset/convert/history
    
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
clTReqId | String | 否 | 用户自定义的订单标识  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度要在1-32位之间。  
after | String | 否 | 查询在此之前的内容，值为时间戳，Unix时间戳为毫秒数格式，如 `1597026383085`  
before | String | 否 | 查询在此之后的内容，值为时间戳，Unix时间戳为毫秒数格式，如 `1597026383085`  
limit | String | 否 | 返回的结果集数量，默认为100，最大为100  
tag | String | 否 | 订单标签  
适用于broker用户  
如果闪兑交易带上了`tag`,查询时必须也带上此参数  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "clTReqId": "",
                "instId": "ETH-USDT",
                "side": "buy",
                "fillPx": "2932.401044",
                "baseCcy": "ETH",
                "quoteCcy": "USDT",
                "fillBaseSz": "0.01023052",
                "state": "fullyFilled",
                "tradeId": "trader16461885203381437",
                "fillQuoteSz": "30",
                "ts": "1646188520000"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
tradeId | String | 成交ID  
clTReqId | String | 用户自定义的订单标识  
state | String | `fullyFilled`：交易成功  
`rejected`：交易失败  
instId | String | 币对，如 `BTC-USDT`  
baseCcy | String | 交易货币币种，如 `BTC-USDT`中的`BTC`  
quoteCcy | String | 计价货币币种，如 `BTC-USDT`中的`USDT`  
side | String | 交易方向  
买：`buy` 卖：`sell`  
fillPx | String | 成交价格，单位为计价币  
fillBaseSz | String | 成交的交易币数量  
fillQuoteSz | String | 成交的计价币数量  
ts | String | 闪兑交易时间，值为时间戳，Unix时间戳为毫秒数格式，如 `1597026383085`