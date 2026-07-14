---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#financial-product-dual-investment-get-order-state
anchor_id: financial-product-dual-investment-get-order-state
api_type: API
updated_at: 2026-07-14 19:21:13.330243
---

# GET / Order state

Returns the current state of a dual investment order.  
  
#### Rate Limit: 3 requests per second

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/finance/sfp/dcd/order-status`

> Request Example
    
    
    GET /api/v5/finance/sfp/dcd/order-status?ordId=987654321
    

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
                "state": "live"
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
ordId | String | Order ID  
state | String | Order state  
`initial`  
`live`  
`pending_settle`  
`settled`  
`pending_redeem`  
`redeemed`  
`rejected`

---

# GET / 获取订单状态

返回双币赢订单的当前状态。  
  
#### 限速：3次/s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/finance/sfp/dcd/order-status`

> 请求示例
    
    
    GET /api/v5/finance/sfp/dcd/order-status?ordId=987654321
    

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
                "state": "live"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
ordId | String | 订单ID  
state | String | 订单状态  
`initial`  
`live`  
`pending_settle`  
`settled`  
`pending_redeem`  
`redeemed`  
`rejected`