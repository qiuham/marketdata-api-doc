---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#financial-product-dual-investment-post-redeem
anchor_id: financial-product-dual-investment-post-redeem
api_type: API
updated_at: 2026-07-18 20:05:29.401546
---

# POST / Redeem

Confirms early redemption using a valid redeem quote. This is step 2 of the two-step early redemption flow.  
  
#### Rate Limit: 2 requests per 60 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/finance/sfp/dcd/redeem`

> Request Example
    
    
    POST /api/v5/finance/sfp/dcd/redeem
    body
    {
        "ordId": "987654321",
        "quoteId": "quoterbcDCD-REDEEM17732116652401234"
    }
    

#### Request Parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
ordId | String | Yes | Order ID  
quoteId | String | Yes | Quote ID  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "ordId": "987654321",
                "state": "pending_redeem_booking"
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
ordId | String | Order ID  
state | String | order state  
`pending_redeem_booking`: redeem received, waiting for liquidity provider further processing  
`pending_redeem`: liquidity provider booked, waiting for transfer  
`redeeming`: redemption in progress  
`redeemed`: redemption completed

---

# POST / 赎回

使用有效的赎回报价确认提前赎回。这是两步赎回流程的第二步。  
  
#### 限速：2次/60s

#### 限速规则：User ID

#### HTTP请求

`POST /api/v5/finance/sfp/dcd/redeem`

> 请求示例
    
    
    POST /api/v5/finance/sfp/dcd/redeem
    body
    {
        "ordId": "987654321",
        "quoteId": "quoterbcDCD-REDEEM17732116652401234"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
ordId | String | 是 | 订单ID  
quoteId | String | 是 | 报价ID  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "ordId": "987654321",
                "state": "pending_redeem_booking"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
ordId | String | 订单ID  
state | String | 订单状态  
`pending_redeem_booking`：赎回请求已接收，等待流动性提供商确认  
`pending_redeem`：流动性提供商已确认，等待资金划转  
`redeeming`：赎回处理中  
`redeemed`：赎回完成