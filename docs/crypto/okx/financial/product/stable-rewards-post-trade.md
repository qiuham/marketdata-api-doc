---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#financial-product-stable-rewards-post-trade
anchor_id: financial-product-stable-rewards-post-trade
api_type: API
updated_at: 2026-07-12 19:17:35.930463
---

# POST / Trade

Execute a subscription or redemption using a valid `quoteId` obtained from `POST /quote`.  
Subscription: assets are deducted from the funding account; on success, the stablecoin is credited to the trading account by default.  
Redemption: the stablecoin is deducted from the funding account by default; the settlement currency is credited to the trading account by default.  
  
#### Rate Limit: 2 requests per second

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/finance/stable-rewards/trade`

> Request Example
    
    
    POST /api/v5/finance/stable-rewards/trade
    body
    {
        "quoteId": "1234567890"
    }
    

#### Request Parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
quoteId | String | Yes | Quote ID returned by `POST /quote`. The quote must not have expired  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "quoteId": "1234567890",
                "ordId": "987654321"
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
quoteId | String | Quote ID  
ordId | String | Order ID

---

# POST / 下单

使用 `POST /quote` 返回的有效 `quoteId` 执行订阅或赎回。  
订阅：从资金账户扣款，成功后稳定币默认入账至交易账户。  
赎回：默认从资金账户扣除稳定币，结算币种默认入账至交易账户。  
  
#### 限速：2次/s

#### 限速规则：User ID

#### 权限：交易

#### HTTP 请求

`POST /api/v5/finance/stable-rewards/trade`

> 请求示例
    
    
    POST /api/v5/finance/stable-rewards/trade
    body
    {
        "quoteId": "1234567890"
    }
    

#### 请求参数

**参数名** | **类型** | **是否必须** | **描述**  
---|---|---|---  
quoteId | String | 是 | 由 `POST /quote` 返回的报价 ID，须在报价未过期前提交  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "quoteId": "1234567890",
                "ordId": "987654321"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
quoteId | String | 报价 ID  
ordId | String | 订单 ID