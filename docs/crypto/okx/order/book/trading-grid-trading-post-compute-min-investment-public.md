---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-grid-trading-post-compute-min-investment-public
anchor_id: order-book-trading-grid-trading-post-compute-min-investment-public
api_type: API
updated_at: 2026-07-19 19:15:17.591686
---

# POST / Compute min investment (public)

Authentication is not required for this public endpoint.  
  
#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`POST /api/v5/tradingBot/grid/min-investment`

> Request Example
    
    
    POST /api/v5/tradingBot/grid/min-investment
    body 
    {
        "instId": "ETH-USDT",
        "algoOrdType":"grid",
        "gridNum": "50",
        "maxPx":"5000",
        "minPx":"3000",
        "runType":"1",
        "investmentData":[
            {
                "amt":"0.01",
                "ccy":"ETH"
            },
            {
                "amt":"100",
                "ccy":"USDT"
            }
        ]
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instId | String | Yes | Instrument ID, e.g. `BTC-USDT-SWAP`  
algoOrdType | String | Yes | Algo order type  
`grid`: Spot grid  
`contract_grid`: Contract grid  
maxPx | String | Yes | Upper price of price range  
minPx | String | Yes | Lower price of price range  
gridNum | String | Yes | Grid quantity  
runType | String | Yes | Grid type  
`1`: Arithmetic, `2`: Geometric  
direction | String | Conditional | Contract grid type  
`long`,`short`,`neutral`  
Only applicable to `contract grid`  
lever | String | Conditional | Leverage  
Only applicable to `contract grid`  
basePos | Boolean | No | Whether or not open a position when the strategy activates  
Default is `false`  
Neutral contract grid should omit the parameter  
Only applicable to `contract grid`  
investmentType | String | No | Investment type, only applicable to `grid`  
`quote`  
`base`  
`dual`  
triggerStrategy | String | No | Trigger stragety,   
`instant`  
`price`  
`rsi`  
topUpAmt | String | No | Top up amount, only applicable to spot grid  
investmentData | Array of objects | No | Invest Data  
> amt | String | Yes | Invest amount  
> ccy | String | Yes | Invest currency  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
               "minInvestmentData": [  
                   {
                       "amt":"0.1",
                       "ccy":"ETH"
                   },
                   {
                       "amt":"100",
                       "ccy":"USDT"
                   }
               ],
               "singleAmt":"10"
           }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
minInvestmentData | Array of objects | Minimum invest Data  
> amt | String | Minimum invest amount  
> ccy | String | Minimum Invest currency  
singleAmt | String | Single grid trading amount  
In terms of `spot grid`, the unit is `quote currency`  
In terms of `contract grid`, the unit is `contract`

---

# POST / 计算最小投资数量（公共）

公共接口无须鉴权  
  
#### 限速：20次/2s

#### 限速规则：IP

#### HTTP请求

`POST /api/v5/tradingBot/grid/min-investment`

> 请求示例
    
    
    POST /api/v5/tradingBot/grid/min-investment
    body
    {
        "instId": "ETH-USDT",
        "algoOrdType":"grid",
        "gridNum": "50",
        "maxPx":"5000",
        "minPx":"3000",
        "runType":"1",
        "investmentData":[
            {
                "amt":"0.01",
                "ccy":"ETH"
            },
            {
                "amt":"100",
                "ccy":"USDT"
            }
        ]
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instId | String | 是 | 产品ID，如`BTC-USDT`  
algoOrdType | String | 是 | 策略订单类型  
`grid`：现货网格委托  
`contract_grid`：合约网格委托  
gridNum | String | 是 | 网格数量  
maxPx | String | 是 | 区间最高价格  
minPx | String | 是 | 区间最低价格  
runType | String | 是 | 网格类型  
`1`：等差，`2`：等比  
direction | String | 可选 | 合约网格类型  
`long`：做多，`short`：做空，`neutral`：中性  
适用于合约网格  
lever | String | 可选 | 杠杆倍数  
适用于合约网格  
basePos | Boolean | 否 | 是否开底仓  
默认为`false`  
investmentType | String | 否 | 投资类型, 仅适用于现货网格  
`quote`: 计价货币  
`base`: 交易货币  
`dual`: 计价货币和交易货币  
triggerStrategy | String | 否 | 触发策略,   
`instant`: 立即触发   
`price`: 价格触发  
`rsi`: rsi 触发  
topUpAmt | String | 否 | 增加的投资额，仅适用于现货网格  
investmentData | Array of objects | 否 | 投资信息  
> amt | String | 是 | 投资数量  
> ccy | String | 是 | 投资币种  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
               "minInvestmentData": [  
                   {
                       "amt":"0.1",
                       "ccy":"ETH"
                   },
                   {
                       "amt":"100",
                       "ccy":"USDT"
                   }
               ],
               "singleAmt":"10"
           }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
minInvestmentData | Array of objects | 最小投入信息  
> amt | String | 最小投入数量  
> ccy | String | 最小投入币种  
singleAmt | String | 单网格买卖量  
现货网格单位为计价币  
合约网格单位为张