---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-grid-trading-post-adjust-margin-balance
anchor_id: order-book-trading-grid-trading-post-adjust-margin-balance
api_type: API
updated_at: 2026-07-04 19:37:48.214700
---

# POST / Adjust margin balance

#### Rate Limit: 20 requests per 2 seconds  
  
#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/tradingBot/grid/margin-balance`

> Request Example
    
    
    POST /api/v5/tradingBot/grid/margin-balance
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
amt | String | Conditional | Adjust margin balance amount  
Either `amt` or `percent` is required.  
percent | String | Conditional | Adjust margin balance percentage  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "algoClOrdId": "",
                "algoId": "123456"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
algoId | String | Algo ID  
algoClOrdId | String | Client-supplied Algo ID

---

# POST / 调整保证金

#### 限速：20次/2s  
  
#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/tradingBot/grid/margin-balance`

> 请求示例
    
    
    POST /api/v5/tradingBot/grid/margin-balance
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
amt | String | 可选 | 调整保证金数量  
`amt`和`percent`必须传一个  
percent | String | 可选 | 调整保证金百分比  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "algoClOrdId": "",
                "algoId": "123456"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
algoId | String | 策略订单ID  
algoClOrdId | String | 用户自定义策略ID