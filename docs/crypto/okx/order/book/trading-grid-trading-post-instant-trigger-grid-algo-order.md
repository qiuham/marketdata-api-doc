---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-grid-trading-post-instant-trigger-grid-algo-order
anchor_id: order-book-trading-grid-trading-post-instant-trigger-grid-algo-order
api_type: API
updated_at: 2026-07-20 19:35:43.362136
---

# POST / Instant trigger grid algo order

#### Rate Limit: 20 requests per 2 seconds  
  
#### Rate limit rule: User ID + Instrument ID

#### HTTP Request

`POST /api/v5/tradingBot/grid/order-instant-trigger`

> Request Example
    
    
    POST /api/v5/tradingBot/grid/order-instant-trigger
    body
    {
        "algoId":"561564133246894080"
    }
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
algoId | String | Yes | Algo ID  
topUpAmt | String | No | Top up amount, only applicable to spot grid  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "algoClOrdId": "",
                "algoId": "561564133246894080"
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

# POST / 网格策略立即触发

#### 限速：20次/2s  
  
#### 限速规则：User ID + Instrument ID

#### HTTP请求

`POST /api/v5/tradingBot/grid/order-instant-trigger`

> 请求示例
    
    
    POST /api/v5/tradingBot/grid/order-instant-trigger
    body
    {
        "algoId":"561564133246894080"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoId | String | 是 | 策略订单ID  
topUpAmt | String | 否 | 增加的投资额，仅适用于现货网格  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "algoClOrdId": "",
                "algoId": "561564133246894080"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
algoId | String | 策略订单ID  
algoClOrdId | String | 用户自定义策略ID