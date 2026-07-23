---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-signal-bot-trading-post-adjust-margin-balance
anchor_id: order-book-trading-signal-bot-trading-post-adjust-margin-balance
api_type: API
updated_at: 2026-07-23 19:21:38.002136
---

# POST / Adjust margin balance

#### Rate Limit: 20 requests per 2 seconds  
  
#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/tradingBot/signal/margin-balance`

> Request Example
    
    
    POST /api/v5/tradingBot/signal/margin-balance
    body
    {
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
amt | String | Yes | Adjust margin balance amount  
Either `amt` or `percent` is required.  
allowReinvest | Boolean | No | Whether to reinvest with newly added margin. The default value is `false`.   
`false`:it will be used as passive margin to prevent liquidation and will not be used as active investment  
`true`:the margin added here will furthermore be accounted for in calculations of your total investment amount, and furthermore your order size。  
Only applicable to your signal comes in with an “investmentType” of “percentage_investment”  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "algoId": "123456"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
algoId | String | Algo ID

---

# POST / 调整保证金

#### 限速：20次/2s  
  
#### 限速规则：User ID

#### HTTP请求

`POST /api/v5/tradingBot/signal/margin-balance`

> 请求示例
    
    
    POST /api/v5/tradingBot/signal/margin-balance
    body
    {
       "algoId":"123456",
       "type":"add",
       "amt":"10"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoId | String | 是 | 策略ID  
type | String | 是 | 调整保证金类型  
`add`：增加，`reduce`：减少  
amt | String | 是 | 调整保证金数量  
allowReinvest | Boolean | 否 | 是否允许复投调整后的保证金，默认false。true 或者 false `false`:新投入的资金仅作为保证金用于避免爆仓  
`true`:新投入的资金将可用于进行复投。  
仅适用于进场设定为“TradingView 信号”或“初始投资比例”的策略  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "algoId": "123456"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
algoId | String | 策略ID