---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-grid-trading-post-add-investment
anchor_id: order-book-trading-grid-trading-post-add-investment
api_type: API
updated_at: 2026-07-08 19:27:39.100994
---

# POST / Add investment

It is used to add investment and only applicable to contract gird.  
  
#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/tradingBot/grid/adjust-investment`

> Request Example
    
    
    POST /api/v5/tradingBot/grid/adjust-investment
    body
    {
        "algoId":"448965992920907776",
        "amt":"12"
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
algoId | String | Yes | Algo ID  
amt | String | Yes | The amount is going to be added  
allowReinvestProfit | String | No | Whether reinvesting profits, only applicable to spot grid.  
`true` or `false`. The default is true.  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "algoId": "448965992920907776"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
algoId | String | Algo ID

---

# POST / 加仓

该接口用于加仓，仅适用于合约网格。  
  
#### 限速：20次/2s

#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/tradingBot/grid/adjust-investment`

> 请求示例
    
    
    POST /api/v5/tradingBot/grid/adjust-investment
    body
    {
        "algoId":"448965992920907776",
        "amt":"12"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoId | String | 是 | 策略订单ID  
amt | String | 是 | 加仓数量  
allowReinvestProfit | String | 否 | 是否复投利润，仅适用于现货网格。  
`true` 或者 `false`。默认为 true。  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "algoId":"448965992920907776"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
algoId | String | 策略订单ID