---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-signal-bot-trading-post-set-instruments
anchor_id: order-book-trading-signal-bot-trading-post-set-instruments
api_type: API
updated_at: 2026-07-13 19:27:51.041469
---

# POST / Set instruments

#### Rate Limit: 20 requests per 2 seconds  
  
#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/tradingBot/signal/set-instruments`

> Request Example
    
    
    POST /api/v5/tradingBot/signal/set-instruments
    body
    {
        "algoId": "637039348240277504",
        "instIds": [
            "SHIB-USDT-SWAP",
            "ETH-USDT-SWAP"
        ]
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
algoId | String | Yes | Algo ID  
instIds | Array of strings | Yes | Instrument IDs. When `includeAll` is `true`, it is ignored  
includeAll | Boolean | Yes | Whether to include all USDT-margined contract.The default value is `false`. `true`: include `false` : exclude  
  
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

# POST / 设置币对

#### 限速：20次/2s  
  
#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/tradingBot/signal/set-instruments`

> 请求示例
    
    
    POST /api/v5/tradingBot/signal/set-instruments
    body
    {
        "algoId": "637039348240277504",
        "instIds": [
            "SHIB-USDT-SWAP",
            "ETH-USDT-SWAP"
        ]
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoId | String | 是 | 策略ID  
instIds | Array of strings | 是 | 产品Id 列表，当 includeAll 为 true 时，忽略此参数。  
includeAll | Boolean | 是 | 是否包含所有USDT 本位永续合约，默认false `true`: 包含 `false` : 不包含  
  
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