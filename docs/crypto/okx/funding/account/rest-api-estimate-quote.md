---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#funding-account-rest-api-estimate-quote
anchor_id: funding-account-rest-api-estimate-quote
api_type: REST
updated_at: 2026-07-05 19:35:19.114186
---

# Estimate quote

#### Rate Limit: 10 requests per second  
  
#### Rate limit rule: User ID

#### Rate Limit: 1 request per 5 seconds

#### Rate limit rule: Instrument ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/asset/convert/estimate-quote`

> Request Example
    
    
    POST /api/v5/asset/convert/estimate-quote
    body
    {
        "baseCcy": "ETH",
        "quoteCcy": "USDT",
        "side": "buy",
        "rfqSz": "30",
        "rfqSzCcy": "USDT"
    }
    

#### Request Parameters

**Parameters** | **Types** | **Required** | **Description**  
---|---|---|---  
baseCcy | String | Yes | Base currency, e.g. `BTC` in `BTC-USDT`  
quoteCcy | String | Yes | Quote currency, e.g. `USDT` in `BTC-USDT`  
side | String | Yes | Trade side based on `baseCcy`  
`buy` `sell`  
rfqSz | String | Yes | RFQ amount  
rfqSzCcy | String | Yes | RFQ currency  
clQReqId | String | No | Client Order ID as assigned by the client  
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
tag | String | No | Order tag  
Applicable to broker user  
convertMode | String | No | `0`: standard convert (default)   
`1`: large order convert for VIP  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "baseCcy": "ETH",
                "baseSz": "0.01023052",
                "clQReqId": "",
                "cnvtPx": "2932.40104429",
                "origRfqSz": "30",
                "quoteCcy": "USDT",
                "quoteId": "quoterETH-USDT16461885104612381",
                "quoteSz": "30",
                "quoteTime": "1646188510461",
                "rfqSz": "30",
                "rfqSzCcy": "USDT",
                "side": "buy",
                "ttlMs": "10000"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
quoteTime | String | Quotation generation time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
ttlMs | String | Validity period of quotation in milliseconds  
clQReqId | String | Client Order ID as assigned by the client  
quoteId | String | Quote ID  
baseCcy | String | Base currency, e.g. `BTC` in `BTC-USDT`  
quoteCcy | String | Quote currency, e.g. `USDT` in `BTC-USDT`  
side | String | Trade side based on `baseCcy`  
origRfqSz | String | Original RFQ amount  
rfqSz | String | Real RFQ amount  
rfqSzCcy | String | RFQ currency  
cnvtPx | String | Convert price based on quote currency  
baseSz | String | Convert amount of base currency  
quoteSz | String | Convert amount of quote currency

---

# 闪兑预估询价

#### 限速：10次/s  
  
#### 限速规则：User ID

#### 限速：1次/5s

#### 限速规则：Instrument ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/asset/convert/estimate-quote`

> 请求示例
    
    
    POST /api/v5/asset/convert/estimate-quote
    body
    {
        "baseCcy": "ETH",
        "quoteCcy": "USDT",
        "side": "buy",
        "rfqSz": "30",
        "rfqSzCcy": "USDT"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
baseCcy | String | 是 | 交易货币币种，如 `BTC-USDT`中的`BTC`  
quoteCcy | String | 是 | 计价货币币种，如 `BTC-USDT`中的`USDT`  
side | String | 是 | 交易方向  
买：`buy` 卖：`sell`  
描述的是对于baseCcy的交易方向  
rfqSz | String | 是 | 询价数量  
rfqSzCcy | String | 是 | 询价币种  
clQReqId | String | 否 | 客户端自定义的订单标识  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度要在1-32位之间。  
tag | String | 否 | 订单标签  
适用于broker用户  
convertMode | String | 否 | `0`：标准闪兑（默认）  
`1`：VIP大额闪兑  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "baseCcy": "ETH",
                "baseSz": "0.01023052",
                "clQReqId": "",
                "cnvtPx": "2932.40104429",
                "origRfqSz": "30",
                "quoteCcy": "USDT",
                "quoteId": "quoterETH-USDT16461885104612381",
                "quoteSz": "30",
                "quoteTime": "1646188510461",
                "rfqSz": "30",
                "rfqSzCcy": "USDT",
                "side": "buy",
                "ttlMs": "10000"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
quoteTime | String | 生成报价时间，Unix时间戳的毫秒数格式  
ttlMs | String | 报价有效期，单位为毫秒  
clQReqId | String | 客户端自定义的订单标识  
quoteId | String | 报价ID  
baseCcy | String | 交易货币币种，如 BTC-USDT 中BTC  
quoteCcy | String | 计价货币币种，如 BTC-USDT 中USDT  
side | String | 交易方向  
买：`buy` 卖：`sell`  
origRfqSz | String | 原始报价的数量  
rfqSz | String | 实际报价的数量  
rfqSzCcy | String | 报价的币种  
cnvtPx | String | 闪兑价格，单位为计价币  
baseSz | String | 闪兑交易币数量  
quoteSz | String | 闪兑计价币数量