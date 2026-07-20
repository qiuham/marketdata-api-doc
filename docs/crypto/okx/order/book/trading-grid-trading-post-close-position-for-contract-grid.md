---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-grid-trading-post-close-position-for-contract-grid
anchor_id: order-book-trading-grid-trading-post-close-position-for-contract-grid
api_type: API
updated_at: 2026-07-20 19:35:42.741446
---

# POST / Close position for contract grid

Close position when the contract grid stop type is 'keep position'.  
  
#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/tradingBot/grid/close-position`

> Request Example
    
    
    POST /api/v5/tradingBot/grid/close-position
    body
    {
        "algoId":"448965992920907776",
        "mktClose":true
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
algoId | String | Yes | Algo ID  
mktClose | Boolean | Yes | Market close all the positions or not  
`true`: Market close all position, `false`: Close part of position  
sz | String | Conditional | Close position amount, with unit of `contract`  
If `mktClose` is `false`, the parameter is required.  
px | String | Conditional | Close position price  
If `mktClose` is `false`, the parameter is required.  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "algoClOrdId": "",
                "algoId": "448965992920907776",
                "ordId": "",
                "tag": ""
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
algoId | String | Algo ID  
ordId | String | Close position order ID  
If `mktClose` is `true`, the parameter will return "".  
algoClOrdId | String | Client-supplied Algo ID  
tag | String | Order tag

---

# POST / 合约网格平仓

只有处于已停止未平仓状态合约网格可使用该接口  
  
#### 限速：20次/2s

#### 限速规则：User ID

#### HTTP请求

`POST /api/v5/tradingBot/grid/close-position`

> 请求示例
    
    
    POST /api/v5/tradingBot/grid/close-position
    body
    {
        "algoId":"448965992920907776",
        "mktClose":true
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoId | String | 是 | 策略订单ID  
mktClose | Boolean | 是 | 是否市价全平  
`true`：市价全平，`false`：部分平仓  
sz | String | 可选 | 平仓数量,单位为张  
部分平仓时必传  
px | String | 可选 | 平仓价格   
部分平仓时必传  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "algoClOrdId": "",
                "algoId":"448965992920907776",
                "ordId":"",
                "tag": ""
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
algoId | String | 策略订单ID  
ordId | String | 平仓单ID  
市价全平时，该字段为""  
algoClOrdId | String | 用户自定义策略ID  
tag | String | 订单标签