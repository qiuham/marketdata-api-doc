---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-grid-trading-post-stop-grid-algo-order
anchor_id: order-book-trading-grid-trading-post-stop-grid-algo-order
api_type: API
updated_at: 2026-07-20 19:35:42.430406
---

# POST / Stop grid algo order

A maximum of 10 orders can be stopped per request.  
  
#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/tradingBot/grid/stop-order-algo`

> Request Example
    
    
    POST /api/v5/tradingBot/grid/stop-order-algo
    body
    [
        {
            "algoId":"448965992920907776",
            "instId":"BTC-USDT",
            "stopType":"1",
            "algoOrdType":"grid"
        }
    ]
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
algoId | String | Yes | Algo ID  
instId | String | Yes | Instrument ID, e.g. `BTC-USDT`  
algoOrdType | String | Yes | Algo order type  
`grid`: Spot grid  
`contract_grid`: Contract grid  
stopType | String | Yes | Stop type  
Spot grid `1`: Sell base currency `2`: Keep base currency  
Contract grid `1`: Market Close All positions `2`: Keep positions  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "algoClOrdId": "",
                "algoId": "448965992920907776",
                "sCode": "0",
                "sMsg": "",
                "tag": ""
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
algoId | String | Algo ID  
algoClOrdId | String | Client-supplied Algo ID  
sCode | String | The code of the event execution result, `0` means success.  
sMsg | String | Rejection message if the request is unsuccessful.  
tag | String | Order tag

---

# POST / 网格策略停止

每次最多可以撤销10个网格策略。  
  
#### 限速：20次/2s

#### 限速规则：User ID

#### HTTP请求

`POST /api/v5/tradingBot/grid/stop-order-algo`

> 请求示例
    
    
    POST /api/v5/tradingBot/grid/stop-order-algo
    body
    [
        {
            "algoId":"448965992920907776",
            "instId":"BTC-USDT",
            "stopType":"1",
            "algoOrdType":"grid"
        }
    ]
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoId | String | 是 | 策略订单ID  
instId | String | 是 | 产品ID，如`BTC-USDT`  
algoOrdType | String | 是 | 策略订单类型  
`grid`：现货网格委托  
`contract_grid`：合约网格委托  
stopType | String | 是 | 网格策略停止类型  
现货网格 `1`：卖出交易币，`2`：不卖出交易币  
合约网格 `1`：市价全平 `2`：停止不平仓  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "algoClOrdId": "",
                "algoId": "448965992920907776",
                "sCode": "0",
                "sMsg": "",
                "tag": ""
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
algoId | String | 策略订单ID  
algoClOrdId | String | 用户自定义策略ID  
sCode | String | 事件执行结果的code，0代表成功  
sMsg | String | 事件执行失败时的msg  
tag | String | 订单标签