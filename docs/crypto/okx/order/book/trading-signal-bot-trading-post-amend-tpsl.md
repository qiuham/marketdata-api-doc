---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-signal-bot-trading-post-amend-tpsl
anchor_id: order-book-trading-signal-bot-trading-post-amend-tpsl
api_type: API
updated_at: 2026-07-02 19:43:37.280616
---

# POST / Amend TPSL

#### Rate Limit: 20 requests per 2 seconds  
  
#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/tradingBot/signal/amendTPSL`

> Request Example
    
    
    POST /api/v5/tradingBot/signal/amendTPSL
    body
    {
        "algoId": "637039348240277504",
        "exitSettingParam": {
            "tpSlType": "pnl",
            "tpPct": "0.01",
            "slPct": "0.01"
        }
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
algoId | String | Yes | Algo ID  
exitSettingParam | String | Yes | Exit setting  
> tpSlType | String | Yes | Type of set the take-profit and stop-loss trigger price  
`pnl`: Based on the estimated profit and loss percentage from the entry point  
`price`: Based on price increase or decrease from the crypto’s entry price  
> tpPct | String | No | Take-profit percentage  
> slPct | String | No | Stop-loss percentage  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "algoId": "637039348240277504"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
algoId | String | Algo ID

---

# POST / 修改止盈止损

#### 限速：20次/2s  
  
#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/tradingBot/signal/amendTPSL`

> 请求示例
    
    
    POST /api/v5/tradingBot/signal/amendTPSL
    body
    {
        "algoId": "637039348240277504",
        "exitSettingParam": {
            "tpSlType": "pnl",
            "tpPct": "0.01",
            "slPct": "0.01"
        }
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoId | String | 是 | 策略ID  
exitSettingParam | String | 是 | 离场参数设定  
> tpSlType | String | 是 | 止盈止损类型  
> tpPct | String | 否 | 止盈百分比  
> slPct | String | 否 | 止损百分比  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "algoId": "637039348240277504"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
algoId | String | 策略ID