---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#financial-product-eth-staking-post-cancel-redeem
anchor_id: financial-product-eth-staking-post-cancel-redeem
api_type: API
updated_at: 2026-07-15 19:20:38.655971
---

# POST / Cancel redeem

#### Rate Limit: 2 requests per second

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/finance/staking-defi/eth/cancel-redeem`

> Request Example
    
    
    POST /api/v5/finance/staking-defi/eth/cancel-redeem
    body
    {
        "ordId": "1234567890"
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
ordId | String | Yes | Order ID  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "ordId": "1234567890"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ordId | String | Order ID

---

# POST / 撤销赎回

#### 限速：2 次/s

#### 限速规则：User ID

#### 权限：交易

#### HTTP 请求

`POST /api/v5/finance/staking-defi/eth/cancel-redeem`

> 请求示例
    
    
    POST /api/v5/finance/staking-defi/eth/cancel-redeem
    body
    {
        "ordId": "1234567890"
    }
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
ordId | String | 是 | 订单ID  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "ordId": "1234567890"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ordId | String | 订单ID