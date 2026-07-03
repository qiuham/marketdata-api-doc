---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-copy-trading-post-close-lead-position
anchor_id: order-book-trading-copy-trading-post-close-lead-position
api_type: API
updated_at: 2026-07-03 19:39:44.292655
---

# POST / Close lead position

You can only close a lead position once a time.   
It is required to pass subPosId which can get from [Get existing leading positions](/docs-v5/en/#order-book-trading-copy-trading-get-existing-lead-positions).  
  
#### Rate limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP request

`POST /api/v5/copytrading/close-subposition`

> Request example
    
    
    POST /api/v5/copytrading/close-subposition
    body
    {
        "subPosId": "518541406042591232",
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | No | Instrument type  
`SPOT`  
`SWAP`, the default value  
subPosId | String | Yes | Lead position ID  
ordType | String | No | Order type  
`market`：Market order, the default value  
`limit`：Limit order  
  
px | String | No | Order price. Only applicable to `limit` order and `SPOT` lead trader   
If the price is 0, the pending order will be canceled.   
It is modifying order if you set `px` after placing limit order.  
tag | String | No | Order tag  
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 16 characters.  
  
> Response example
    
    
    {
        "code": "0",
        "data": [
            {
                "subPosId": "518560559046594560",
                "tag":""
            }
        ],
        "msg": ""
    }
    

#### Response parameters

**Parameter** | **Type** | **Description**  
---|---|---  
subPosId | String | Lead position ID  
tag | String | Order tag

---

# POST / 平仓带单

一次仅可平仓一个带单仓位。  
`subPosId` 为必填参数，需要通过[交易员获取当前带单](/docs-v5/zh/#order-book-trading-copy-trading-get-existing-lead-positions)接口获取。  
  
#### 限速：20次/2s

#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/copytrading/close-subposition`

> 请求示例
    
    
    POST /api/v5/copytrading/close-subposition
    body
    {
        "subPosId": "518541406042591232"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 否 | 产品类型  
SPOT：币币  
SWAP：永续合约，默认值  
subPosId | String | 是 | 带单仓位ID  
tag | String | 否 | 订单标签  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字，且长度在1-16位之间。  
ordType | String | 否 | 订单类型  
`market`：市价单  
`limit`：限价单  
默认为市价单  
px | String | 否 | 委托价格，仅适用于`limit`类型的订单，且仅适用于现货交易员  
委托价格为 0 代表撤销挂单  
已经设置了限价单，仍为该条目设置价格时，视为改单。  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "subPosId": "518560559046594560",
                "tag":""
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
subPosId | String | 带单仓位ID  
tag | String | 订单标签