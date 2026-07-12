---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-grid-trading-post-spot-grid-withdraw-income
anchor_id: order-book-trading-grid-trading-post-spot-grid-withdraw-income
api_type: API
updated_at: 2026-07-12 19:15:44.754833
---

# POST / Spot grid withdraw income

#### Rate Limit: 20 requests per 2 seconds  
  
#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/tradingBot/grid/withdraw-income`

> Request Example
    
    
    POST /api/v5/tradingBot/grid/withdraw-income
    body
    {
        "algoId":"448965992920907776"
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
algoId | String | Yes | Algo ID  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "algoClOrdId": "",
                "algoId":"448965992920907776",
                "profit":"100"
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
algoId | String | Algo ID  
algoClOrdId | String | Client-supplied Algo ID  
profit | String | Withdraw profit

---

# POST / 现货网格提取利润

#### 限速：20次/2s  
  
#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/tradingBot/grid/withdraw-income`

> 请求示例
    
    
    POST /api/v5/tradingBot/grid/withdraw-income
    body
    {
        "algoId":"448965992920907776"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoId | String | 是 | 策略订单ID  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "algoClOrdId": "",
                "algoId":"448965992920907776",
                "profit":"100"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
algoId | String | 策略订单ID  
algoClOrdId | String | 用户自定义策略ID  
profit | String | 提取的利润