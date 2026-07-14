---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-grid-trading-get-max-grid-quantity-public
anchor_id: order-book-trading-grid-trading-get-max-grid-quantity-public
api_type: API
updated_at: 2026-07-14 19:19:17.907294
---

# GET / Max grid quantity (public)

Authentication is not required for this public endpoint.  
  
  
Maximum grid quantity can be retrieved from this endpoint. Minimum grid quantity always is 2.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: IP

#### Permission: Read

#### HTTP Request

`GET /api/v5/tradingBot/grid/grid-quantity`

> Request Example
    
    
    GET /api/v5/tradingBot/grid/grid-quantity?instId=BTC-USDT-SWAP&runType=1&algoOrdType=contract_grid&maxPx=70000&minPx=50000&lever=5
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instId | String | Yes | Instrument ID, e.g. `BTC-USDT`  
runType | String | Yes | Grid type  
`1`: Arithmetic  
`2`: Geometric  
algoOrdType | String | Yes | Algo order type  
`grid`: Spot grid  
`contract_grid`: Contract grid  
maxPx | String | Yes | Upper price of price range  
minPx | String | Yes | Lower price of price range  
lever | String | Conditional | Leverage, it is required for contract grid  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "maxGridQty": "285"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
maxGridQty | String | Maximum grid quantity

---

# GET / 最大网格数量（公共）

公共接口无须鉴权  
  
  
可通过该接口获取最大网格数量，最小网格数量总是 2。

#### 限速：5次/2s

#### 限速规则：IP

#### 权限：读取

#### HTTP请求

`GET /api/v5/tradingBot/grid/grid-quantity`

> 请求示例
    
    
    GET /api/v5/tradingBot/grid/grid-quantity?instId=BTC-USDT-SWAP&runType=1&algoOrdType=contract_grid&maxPx=70000&minPx=50000&lever=5
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instId | String | 是 | 产品ID，如`BTC-USDT`  
runType | String | 是 | 网格类型  
`1`: 等差  
`2`: 等比  
algoOrdType | String | 是 | 策略订单类型  
`grid`：现货网格委托  
`contract_grid`：合约网格委托  
maxPx | String | 是 | 区间最高价格  
minPx | String | 是 | 区间最低价格  
lever | String | 可选 | 杠杆倍数, 合约网格时必填  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "maxGridQty": "285"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
maxGridQty | String | 最大网格数量