---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#financial-product-dual-investment-post-trade
anchor_id: financial-product-dual-investment-post-trade
api_type: API
updated_at: 2026-07-08 19:29:38.154731
---

# POST / Trade

Places a dual investment order using a valid quote.  
  
#### Rate Limit: 2 requests per 60 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/finance/sfp/dcd/trade`

> Request Example
    
    
    POST /api/v5/finance/sfp/dcd/trade
    body
    {
        "quoteId": "quoterbpDCD-QUOTE17732116652401234"
    }
    

#### Request Parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
quoteId | String | Yes | Quote ID  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "quoteId": "quoterbpDCD-QUOTE17732116652401234",
                "ordId": "987654321",
                "state": "live"
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
quoteId | String | Quote ID  
ordId | String | Order ID  
state | String | Order state  
`initial`: request has been received by system, will further process  
`pending_book`: trade received by liquidity provider, pending further processing  
`live`: trade is live  
`rejected`: trade has been rejected

---

# POST / 下单

使用有效报价下单双币赢。  
  
#### 限速：2次/60s

#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/finance/sfp/dcd/trade`

> 请求示例
    
    
    POST /api/v5/finance/sfp/dcd/trade
    body
    {
        "quoteId": "quoterbpDCD-QUOTE17732116652401234"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
quoteId | String | 是 | 报价ID  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "quoteId": "quoterbpDCD-QUOTE17732116652401234",
                "ordId": "987654321",
                "state": "live"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
quoteId | String | 报价ID  
ordId | String | 订单ID  
state | String | 订单状态  
`initial`：系统已接收请求，待处理  
`pending_book`：流动性提供商已接收请求，待处理  
`live`：交易已生效  
`rejected`：交易已拒绝