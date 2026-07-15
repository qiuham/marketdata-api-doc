---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-grid-trading-post-copy-grid-algo-order
anchor_id: order-book-trading-grid-trading-post-copy-grid-algo-order
api_type: API
updated_at: 2026-07-15 19:18:54.923223
---

# POST / Copy grid algo order

#### Rate Limit: 20 requests per 2 seconds  
  
#### Rate Limit Rule: User ID + Instrument ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/tradingBot/grid/copy-order-algo`

> Request Example
    
    
    # Spot grid copy
    POST /api/v5/tradingBot/grid/copy-order-algo
    body
    {
        "instId": "BTC-USDT",
        "algoOrdType": "grid",
        "sourceAlgoId": "580007082221121536",
        "quoteSz": "1000"
    }
    
    
    
    # Contract grid copy
    POST /api/v5/tradingBot/grid/copy-order-algo
    body
    {
        "instId": "BTC-USDT-SWAP",
        "algoOrdType": "contract_grid",
        "sourceAlgoId": "580007082221121536",
        "lever": "3",
        "autoReserve": true,
        "sz": "5000"
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instId | String | Yes | Instrument ID, e.g. `BTC-USDT`  
algoOrdType | String | Yes | Algo order type  
`grid`: Spot grid  
`contract_grid`: Contract grid  
sourceAlgoId | String | Yes | Lead algo order ID to follow and copy from  
quoteSz | String | No | Quote currency investment amount  
Only applicable to `grid`  
lever | String | No | Leverage  
Only applicable to `contract_grid`  
autoReserve | Boolean | No | Whether to auto-reserve margin. Only applicable to `contract_grid`  
`true`: Actual margin and extra margin are automatically calculated based on `sz`  
`false`: Manually specify `actualMarginSz` and `extraMarginSz`  
sz | String | No | Total investment amount in USDT. Required when `autoReserve` is `true`  
Only applicable to `contract_grid`  
actualMarginSz | String | No | Actual margin. Required when `autoReserve` is `false`  
Only applicable to `contract_grid`  
extraMarginSz | String | No | Extra margin reserved. Defaults to `0` when unspecified  
Only applicable to `contract_grid`  
algoClOrdId | String | No | Client-supplied Algo ID  
tag | String | No | Order tag  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "algoId": "581234567890123456",
                "algoClOrdId": "",
                "sCode": "0",
                "sMsg": "",
                "tag": ""
            }
        ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
algoId | String | Algo order ID  
algoClOrdId | String | Client-supplied Algo ID  
sCode | String | Event execution status code, `0` indicates success  
sMsg | String | Error message if the event execution failed  
tag | String | Order tag

---

# POST / 网格跟单下单

#### 限速：20次/2s  
  
#### 限速规则：User ID + Instrument ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/tradingBot/grid/copy-order-algo`

> 请求示例
    
    
    # 现货网格跟单
    POST /api/v5/tradingBot/grid/copy-order-algo
    body
    {
        "instId": "BTC-USDT",
        "algoOrdType": "grid",
        "sourceAlgoId": "580007082221121536",
        "quoteSz": "1000"
    }
    
    
    
    # 合约网格跟单
    POST /api/v5/tradingBot/grid/copy-order-algo
    body
    {
        "instId": "BTC-USDT-SWAP",
        "algoOrdType": "contract_grid",
        "sourceAlgoId": "580007082221121536",
        "lever": "3",
        "autoReserve": true,
        "sz": "5000"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instId | String | 是 | 产品ID，如 `BTC-USDT`  
algoOrdType | String | 是 | 策略订单类型  
`grid`：现货网格  
`contract_grid`：合约网格  
sourceAlgoId | String | 是 | 被跟单的策略订单ID  
quoteSz | String | 否 | 计价币投入金额  
仅适用于 `grid`  
lever | String | 否 | 杠杆倍数  
仅适用于 `contract_grid`  
autoReserve | Boolean | 否 | 是否自动预留保证金，仅适用于 `contract_grid`  
`true`：自动计算实际保证金和额外保证金  
`false`：手动指定 `actualMarginSz` 和 `extraMarginSz`  
sz | String | 否 | 合约网格总投入金额（USDT），当 `autoReserve` 为 `true` 时必填  
仅适用于 `contract_grid`  
actualMarginSz | String | 否 | 实际保证金，当 `autoReserve` 为 `false` 时必填  
仅适用于 `contract_grid`  
extraMarginSz | String | 否 | 额外保证金，当 `autoReserve` 为 `false` 时选填，默认为 `0`  
仅适用于 `contract_grid`  
algoClOrdId | String | 否 | 客户自定义策略单ID  
tag | String | 否 | 订单标签  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "algoId": "581234567890123456",
                "algoClOrdId": "",
                "sCode": "0",
                "sMsg": "",
                "tag": ""
            }
        ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
algoId | String | 策略订单ID  
algoClOrdId | String | 客户自定义策略单ID  
sCode | String | 事件执行结果的 code，0 代表成功  
sMsg | String | 事件执行失败时的 msg  
tag | String | 订单标签