---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#financial-product-dual-investment-post-request-for-quote
anchor_id: financial-product-dual-investment-post-request-for-quote
api_type: API
updated_at: 2026-07-04 19:39:47.286269
---

# POST / Request for quote

Requests a real-time quote for a dual investment product. The quote has a TTL and must be used before expiry.  
  
#### Rate Limit: 10 requests per 60 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/finance/sfp/dcd/quote`

> Request Example
    
    
    POST /api/v5/finance/sfp/dcd/quote
    body
    {
        "productId": "BTC-USDT-260327-77000-C",
        "notionalSz": "1.5",
        "notionalCcy": "BTC"
    }
    

#### Request Parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
productId | String | Yes | Product ID  
notionalSz | String | Yes | Investment size  
notionalCcy | String | Yes | Investment currency  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "absYield": "0.00135182",
                "annualizedYield": "69.65",
                "interestAccrualTime": "1773241200000",
                "notionalSz": "0.001",
                "notionalCcy": "BTC",
                "productId": "BTC-USDT-260312-72000-C",
                "quoteId": "qtbcDCD-QUOTE17732395560537636",
                "validUntil": "1774584000000",
                "idxPx": "69000"
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
absYield | String | Absolute yield  
annualizedYield | String | Annualized yield  
interestAccrualTime | String | Interest accrual start time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
notionalSz | String | Investment size  
notionalCcy | String | Investment currency  
productId | String | Product ID  
quoteId | String | Quote ID  
validUntil | String | Quote valid until, Unix timestamp format in milliseconds, e.g. `1597026383085`  
idxPx | String | Index price

---

# POST / 获取报价

为双币赢产品请求实时报价。报价有有效期，须在到期前使用。  
  
#### 限速：10次/60s

#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/finance/sfp/dcd/quote`

> 请求示例
    
    
    POST /api/v5/finance/sfp/dcd/quote
    body
    {
        "productId": "BTC-USDT-260327-77000-C",
        "notionalSz": "1.5",
        "notionalCcy": "BTC"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
productId | String | 是 | 产品ID  
notionalSz | String | 是 | 投资数量  
notionalCcy | String | 是 | 投资币种  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "absYield": "0.00135182",
                "annualizedYield": "69.65",
                "interestAccrualTime": "1773241200000",
                "notionalSz": "0.001",
                "notionalCcy": "BTC",
                "productId": "BTC-USDT-260312-72000-C",
                "quoteId": "qtbcDCD-QUOTE17732395560537636",
                "validUntil": "1774584000000",
                "idxPx": "69000"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
absYield | String | 绝对收益率  
annualizedYield | String | 年化收益率  
interestAccrualTime | String | 利息开始计算时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
notionalSz | String | 投资数量  
notionalCcy | String | 投资币种  
productId | String | 产品ID  
quoteId | String | 报价ID  
validUntil | String | 报价有效期，Unix时间戳的毫秒数格式，如 `1597026383085`  
idxPx | String | 指数价格