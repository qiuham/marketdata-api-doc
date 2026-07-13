---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-signal-bot-trading-post-close-position
anchor_id: order-book-trading-signal-bot-trading-post-close-position
api_type: API
updated_at: 2026-07-13 19:27:52.938721
---

# POST / Close position

Close the position of an instrument via a market order.  
  
#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/tradingBot/signal/close-position`

> Request Example
    
    
    POST /api/v5/tradingBot/signal/close-position
    body
    {
        "instId":"BTC-USDT-SWAP",
        "algoId":"448965992920907776"
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
algoId | String | Yes | Algo ID  
instId | String | Yes | Instrument ID  
  
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

# POST / 市价仓位全平

市价平掉指定交易产品的持仓  
  
#### 限速：20次/2s

#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/tradingBot/signal/close-position`

> 请求示例
    
    
    POST /api/v5/tradingBot/signal/close-position
    body
    {
        "instId":"BTC-USDT-SWAP",
        "algoId":"448965992920907776"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoId | String | 是 | 策略ID  
instId | String | 是 | 产品ID  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "algoId": "448965992920907776"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
algoId | String | 策略ID