---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-grid-trading-get-grid-ai-parameter-public
anchor_id: order-book-trading-grid-trading-get-grid-ai-parameter-public
api_type: API
updated_at: 2026-06-30 19:54:41.986212
---

# GET / Grid AI parameter (public)

Authentication is not required for this public endpoint.  
  
#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP

#### Permission: Read

#### HTTP Request

`GET /api/v5/tradingBot/grid/ai-param`

> Request Example
    
    
    GET /api/v5/tradingBot/grid/ai-param?instId=BTC-USDT&algoOrdType=grid
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
algoOrdType | String | Yes | Algo order type  
`grid`: Spot grid  
`contract_grid`: Contract grid  
instId | String | Yes | Instrument ID, e.g. `BTC-USDT`  
direction | String | Conditional | Contract grid type  
`long`,`short`,`neutral`  
Required in the case of `contract_grid`  
duration | String | No | Back testing duration in number of days  
Spot grid default is `7D` with available durations of `7D`, `30D` and `180D`  
Contract grid default is `14D` with available durations of `7D`, `14D` and `30D`  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "algoOrdType": "grid",
                "annualizedRate": "1.5849",
                "ccy": "USDT",
                "direction": "",
                "duration": "7D",
                "gridNum": "5",
                "instId": "BTC-USDT",
                "lever": "0",
                "maxPx": "21373.3",
                "minInvestment": "0.89557758",
                "minPx": "15544.2",
                "perGridProfitRatio": "4.566226200302574",
                "perMaxProfitRate": "0.0733865364573281",
                "perMinProfitRate": "0.0561101403446263",
                "runType": "1",
                "sourceCcy": ""
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instId | String | Instrument ID, e.g. BTC-USDT-SWAP  
algoOrdType | String | Algo order type  
`grid`: Spot grid  
`contract_grid`: Contract grid  
duration | String | Back testing duration  
`7D`: 7 Days, `30D`: 30 Days, `180D`: 180 Days  
gridNum | String | Grid quantity  
maxPx | String | Upper price of price range  
minPx | String | Lower price of price range  
perMaxProfitRate | String | Estimated maximum Profit margin per grid  
perMinProfitRate | String | Estimated minimum Profit margin per grid  
perGridProfitRatio | String | Per grid profit ratio  
annualizedRate | String | Grid annualized rate  
minInvestment | String | The minimum invest amount  
ccy | String | The invest currency  
runType | String | Grid type  
`1`: Arithmetic, `2`: Geometric  
direction | String | Contract grid type  
`long`,`short`,`neutral`  
Only applicable to contract grid  
lever | String | Leverage  
Only applicable to contract grid  
sourceCcy | String | Source currency

---

# GET / 网格策略智能回测（公共）

公共接口无须鉴权  
  
#### 限速：20次/2s

#### 限速规则：IP

#### 权限：读取

#### HTTP请求

`GET /api/v5/tradingBot/grid/ai-param`

> 请求示例
    
    
    GET /api/v5/tradingBot/grid/ai-param?instId=BTC-USDT&algoOrdType=grid
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoOrdType | String | 是 | 策略订单类型  
`grid`：现货网格委托  
`contract_grid`：合约网格委托  
instId | String | 是 | 产品ID，如`BTC-USDT`  
direction | String | 可选 | 合约网格类型  
`long`：做多，`short`：做空，`neutral`：中性  
合约网格必填  
duration | String | 否 | 回测时长，单位为天  
现货网格默认 `7D`，可选：`7D`、`30D`、`180D`  
合约网格默认 `14D`，可选：`7D`、`14D`、`30D`  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "algoOrdType": "grid",
                "annualizedRate": "1.5849",
                "ccy": "USDT",
                "direction": "",
                "duration": "7D",
                "gridNum": "5",
                "instId": "BTC-USDT",
                "lever": "0",
                "maxPx": "21373.3",
                "minInvestment": "0.89557758",
                "minPx": "15544.2",
                "perGridProfitRatio": "4.566226200302574",
                "perMaxProfitRate": "0.0733865364573281",
                "perMinProfitRate": "0.0561101403446263",
                "runType": "1",
                "sourceCcy": ""
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
instId | String | 产品ID  
algoOrdType | String | 策略订单类型  
`grid`：现货网格委托  
`contract_grid`：合约网格委托  
duration | String | 回测周期  
`7D`：7天，`30D`：30天，`180D`：180天  
gridNum | String | 网格数量  
maxPx | String | 区间最高价格  
minPx | String | 区间最低价格  
perMaxProfitRate | String | 单网格最高利润率  
perMinProfitRate | String | 单网格最低利润率  
perGridProfitRatio | String | 单网格利润率  
annualizedRate | String | 网格年化收益率  
minInvestment | String | 最小投资数量  
ccy | String | 投资币种  
runType | String | 网格类型  
`1`：等差，`2`：等比  
direction | String | 合约网格类型  
仅适用于`合约网格`  
lever | String | 杠杆倍数  
仅适用于`合约网格`  
sourceCcy | String | 来源币种