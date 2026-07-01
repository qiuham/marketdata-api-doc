---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-grid-trading-post-cancel-close-position-order-for-contract-grid
anchor_id: order-book-trading-grid-trading-post-cancel-close-position-order-for-contract-grid
api_type: API
updated_at: 2026-07-01 19:54:00.453934
---

# POST / Cancel close position order for contract grid

#### Rate Limit: 20 requests per 2 seconds  
  
#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/tradingBot/grid/cancel-close-order`

> Request Example
    
    
    POST /api/v5/tradingBot/grid/cancel-close-order
    body
    {
        "algoId":"448965992920907776",
        "ordId":"570627699870375936"
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
algoId | String | Yes | Algo ID  
ordId | String | Yes | Close position order ID  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "algoClOrdId": "",
                "algoId": "448965992920907776",
                "ordId": "570627699870375936",
                "tag": ""
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
algoId | String | Algo ID  
ordId | String | Close position order ID  
algoClOrdId | String | Client-supplied Algo ID  
tag | String | Order tag

---

# POST / 撤销合约网格平仓单

#### 限速：20次/2s  
  
#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/tradingBot/grid/cancel-close-order`

> 请求示例
    
    
    POST /api/v5/tradingBot/grid/cancel-close-order
    body
    {
        "algoId":"448965992920907776",
        "ordId":"570627699870375936"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoId | String | 是 | 策略订单ID  
ordId | String | 是 | 平仓单ID  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "algoClOrdId": "",
                "algoId": "448965992920907776",
                "ordId": "570627699870375936",
                "tag": ""
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
algoId | String | 策略订单ID  
ordId | String | 平仓单ID  
algoClOrdId | String | 用户自定义策略ID  
tag | String | 订单标签