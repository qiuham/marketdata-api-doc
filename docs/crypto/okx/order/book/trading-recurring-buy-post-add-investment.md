---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-recurring-buy-post-add-investment
anchor_id: order-book-trading-recurring-buy-post-add-investment
api_type: API
updated_at: 2026-07-10 19:31:08.214439
---

# POST / Add investment

#### Rate Limit: 20 requests per 2 seconds  
  
#### Rate Limit Rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/tradingBot/recurring/add-investment`

> Request Example
    
    
    POST /api/v5/tradingBot/recurring/add-investment
    body
    {
        "algoId": "2837428373700509696",
        "amount": "20"
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
algoId | String | Yes | Algo order ID  
amount | String | Yes | Additional investment amount. Only the investment currency used when the strategy was created is supported  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "algoId": "2837428373700509696",
                "sCode": "0",
                "sMsg": ""
            }
        ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
algoId | String | Algo order ID  
sCode | String | Event execution status code, `0` indicates success  
sMsg | String | Error message if the event execution failed

---

# POST / 手动加仓

#### 限速：20次/2s  
  
#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/tradingBot/recurring/add-investment`

> 请求示例
    
    
    POST /api/v5/tradingBot/recurring/add-investment
    body
    {
        "algoId": "2837428373700509696",
        "amount": "20"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoId | String | 是 | 策略订单ID  
amount | String | 是 | 加仓投入金额，仅支持创建策略时的投资币种  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "algoId": "2837428373700509696",
                "sCode": "0",
                "sMsg": ""
            }
        ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
algoId | String | 策略订单ID  
sCode | String | 事件执行结果的 code，0 代表成功  
sMsg | String | 事件执行失败时的 msg