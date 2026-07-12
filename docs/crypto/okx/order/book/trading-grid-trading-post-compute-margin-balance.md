---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-grid-trading-post-compute-margin-balance
anchor_id: order-book-trading-grid-trading-post-compute-margin-balance
api_type: API
updated_at: 2026-07-12 19:15:45.065002
---

# POST / Compute margin balance

#### Rate Limit: 20 requests per 2 seconds  
  
#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/tradingBot/grid/compute-margin-balance`

> Request Example
    
    
    POST /api/v5/tradingBot/grid/compute-margin-balance
    body {
       "algoId":"123456",
       "type":"add",
       "amt":"10"
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
algoId | String | Yes | Algo ID  
type | String | Yes | Adjust margin balance type  
`add` `reduce`  
amt | String | No | Adjust margin balance amount  
Default is zero.  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "lever": "0.3877200981166066",
                "maxAmt": "1.8309562403342999"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
maxAmt | String | Maximum adjustable margin balance amount  
lever | String | Leverage after adjustment of margin balance

---

# POST / 调整保证金计算

#### 限速：20次/2s  
  
#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/tradingBot/grid/compute-margin-balance`

> 请求示例
    
    
    POST /api/v5/tradingBot/grid/compute-margin-balance
    body {
       "algoId":"123456",
       "type":"add",
       "amt":"10"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoId | String | 是 | 策略订单ID  
type | String | 是 | 调整保证金类型  
`add`：增加，`reduce`：减少  
amt | String | 否 | 调整保证金数量  
  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "lever": "0.3877200981166066",
                "maxAmt": "1.8309562403342999"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
maxAmt | String | 最多可调整的保证金数量  
lever | String | 调整保证金后的杠杠倍数