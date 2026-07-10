---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#financial-product-dual-investment-post-request-for-redeem-quote
anchor_id: financial-product-dual-investment-post-request-for-redeem-quote
api_type: API
updated_at: 2026-07-10 19:32:50.666282
---

# POST / Request for redeem quote

Requests an early redemption quote for a live dual investment order. This is step 1 of the two-step early redemption flow; call POST / Redeem to confirm.  
  
#### Rate Limit: 10 requests per 60 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/finance/sfp/dcd/redeem-quote`

> Request Example
    
    
    POST /api/v5/finance/sfp/dcd/redeem-quote
    body
    {
        "ordId": "987654321"
    }
    

#### Request Parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
ordId | String | Yes | Order ID  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "ordId": "987654321",
                "quoteId": "quoterbcDCD-REDEEM17732116652401234",
                "redeemCcy": "BTC",
                "redeemSz": "1.4856",
                "termRate": "-0.50",
                "validUntil": "1774598400000"
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
ordId | String | Order ID  
quoteId | String | Quote ID  
redeemSz | String | Redeem size  
redeemCcy | String | Redeem currency  
termRate | String | Term rate  
validUntil | String | Redeem quote valid until, Unix timestamp format in milliseconds, e.g. `1597026383085`

---

# POST / 获取赎回报价

为生效中的双币赢订单申请提前赎回报价。这是两步赎回流程的第一步，之后需调用 POST / 赎回 确认。  
  
#### 限速：10次/60s

#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/finance/sfp/dcd/redeem-quote`

> 请求示例
    
    
    POST /api/v5/finance/sfp/dcd/redeem-quote
    body
    {
        "ordId": "987654321"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
ordId | String | 是 | 订单ID  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "ordId": "987654321",
                "quoteId": "quoterbcDCD-REDEEM17732116652401234",
                "redeemCcy": "BTC",
                "redeemSz": "1.4856",
                "termRate": "-0.50",
                "validUntil": "1774598400000"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
ordId | String | 订单ID  
quoteId | String | 报价ID  
redeemSz | String | 赎回数量  
redeemCcy | String | 赎回币种  
termRate | String | 期限利率  
validUntil | String | 赎回报价有效期，Unix时间戳的毫秒数格式，如 `1597026383085`