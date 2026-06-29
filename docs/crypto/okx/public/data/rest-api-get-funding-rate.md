---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#public-data-rest-api-get-funding-rate
anchor_id: public-data-rest-api-get-funding-rate
api_type: REST
updated_at: 2026-06-29 19:57:14.739668
---

# Get funding rate

Retrieve funding rate.  
  
#### Rate Limit: 10 requests per 2 seconds

#### Rate limit rule: IP + Instrument ID

#### HTTP Request

`GET /api/v5/public/funding-rate`

> Request Example
    
    
    GET /api/v5/public/funding-rate?instId=BTC-USD-SWAP
    
    
    
    import okx.PublicData as PublicData
    
    flag = "0"  # Production trading: 0, Demo trading: 1
    
    publicDataAPI = PublicData.PublicAPI(flag=flag)
    
    # Retrieve funding rate
    result = publicDataAPI.get_funding_rate(
        instId="BTC-USD-SWAP",
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instId | String | Yes | Instrument ID, e.g. `BTC-USD-SWAP` or X-Perps futures instId, or `ANY` to return the funding rate info of all perpetual and X-Perps futures contracts  
Applicable to `SWAP` and X-Perps `FUTURES`  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "formulaType": "noRate",
                "fundingRate": "0.0000182221218054",
                "fundingTime": "1743609600000",
                "impactValue": "",
                "instId": "BTC-USDT-SWAP",
                "instType": "SWAP",
                "interestRate": "",
                "maxFundingRate": "0.00375",
                "method": "current_period",
                "minFundingRate": "-0.00375",
                "nextFundingRate": "",
                "nextFundingTime": "1743638400000",
                "premium": "0.0000910113652644",
                "settFundingRate": "0.0000145824401745",
                "settState": "settled",
                "ts": "1743588686291"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instType | String | Instrument type  
`SWAP`: Perpetual futures  
`FUTURES`: X-Perps futures  
instId | String | Instrument ID, e.g. `BTC-USD-SWAP` or `ANY`  
method | String | Funding rate mechanism   
`current_period` ~~  
`next_period`~~(no longer supported)  
formulaType | String | Formula type  
`noRate`: old funding rate formula  
`withRate`: new funding rate formula  
fundingRate | String | Predicted funding rate for the upcoming settlement period. Sign: positive = long positions pay short positions at the next `fundingTime`; negative = short positions pay long positions. This is a forecast — the final settled rate may differ. See `settFundingRate` for the last settled rate. Note: the settlement interval is typically 8 hours but may be adjusted; use the difference between `fundingTime` and `nextFundingTime` to determine the actual interval.  
nextFundingRate | String | ~~Forecasted funding rate for the next period  
The nextFundingRate will be "" if the method is `current_period`~~(no longer supported)  
fundingTime | String | Settlement time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
nextFundingTime | String | Forecasted funding time for the next period , Unix timestamp format in milliseconds, e.g. `1597026383085`  
minFundingRate | String | The lower limit of the funding rate  
maxFundingRate | String | The upper limit of the funding rate  
interestRate | String | Interest rate  
impactValue | String | Depth weighted amount (in the unit of quote currency)  
settState | String | Settlement state of funding rate   
`processing`   
`settled`  
settFundingRate | String | If settState = `processing`, it is the funding rate that is being used for current settlement cycle.   
If settState = `settled`, it is the funding rate that is being used for previous settlement cycle  
premium | String | Premium index  
formula: [Max (0, Impact bid price – Index price) – Max (0, Index price – Impact ask price)] / Index price  
ts | String | Data return time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
For some altcoins perpetual swaps with significant fluctuations in funding rates, OKX will closely monitor market changes. When necessary, the funding rate collection frequency, currently set at 8 hours, may be adjusted to higher frequencies such as 6 hours, 4 hours, 2 hours, or 1 hour. Thus, users should focus on the difference between `fundingTime` and `nextFundingTime` fields to determine the funding fee interval of a contract.

---

# 获取合约当前资金费率

获取合约当前资金费率  
  
#### 限速：10次/2s

#### 限速规则：IP + Instrument ID

#### HTTP请求

`GET /api/v5/public/funding-rate`

> 请求示例
    
    
    GET /api/v5/public/funding-rate?instId=BTC-USD-SWAP
    
    
    
    import okx.PublicData as PublicData
    
    flag = "0"  # 实盘:0 , 模拟盘：1
    
    publicDataAPI = PublicData.PublicAPI(flag=flag)
    
    # 获取合约当前资金费率
    result = publicDataAPI.get_funding_rate(
        instId="BTC-USD-SWAP",
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instId | String | 是 | 产品ID，如 `BTC-USD-SWAP` 或 X-Perps 交割合约 instId，传入 `ANY` 时返回所有 X-Perps 交割合约及永续合约的资金费率信息  
适用于`永续`及 X-Perps `交割`  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "formulaType": "noRate",
                "fundingRate": "0.0000182221218054",
                "fundingTime": "1743609600000",
                "impactValue": "",
                "instId": "BTC-USDT-SWAP",
                "instType": "SWAP",
                "interestRate": "",
                "maxFundingRate": "0.00375",
                "method": "current_period",
                "minFundingRate": "-0.00375",
                "nextFundingRate": "",
                "nextFundingTime": "1743638400000",
                "premium": "0.0000910113652644",
                "settFundingRate": "0.0000145824401745",
                "settState": "settled",
                "ts": "1743588686291"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
instType | String | 产品类型  
`SWAP`：永续合约  
`FUTURES`：X-Perps 交割合约  
instId | String | 产品ID，如`BTC-USD-SWAP` 或 `ANY`  
method | String | 资金费收取逻辑   
`current_period`：当期收 ~~  
`next_period`：跨期收~~（不再支持跨期收合约）  
formulaType | String | 公式类型  
`noRate`：旧资金费率计算公式  
`withRate`：新资金费率计算公式  
fundingRate | String | 下一结算周期的预测资金费率。正数表示多头向空头支付资金费；负数表示空头向多头支付资金费。此为预测值，最终结算费率可能有所不同，请参阅 `settFundingRate` 查看上次实际结算费率。注意：结算周期通常为8小时，但可能调整；实际周期请通过 `fundingTime` 与 `nextFundingTime` 之差确定。  
nextFundingRate | String | ~~下一期预测资金费率  
当收取逻辑为`current_period`时，nextFundingRate字段将返回""~~（不再支持跨期收合约）  
fundingTime | String | 资金费时间 ，Unix时间戳的毫秒数格式，如 `1597026383085`  
nextFundingTime | String | 下一期资金费时间 ，Unix时间戳的毫秒数格式，如 `1622851200000`  
minFundingRate | String | 资金费率下限  
maxFundingRate | String | 资金费率上限  
interestRate | String | 利率  
impactValue | String | 深度加权金额（计价币数量）  
settState | String | 资金费率结算状态   
`processing`：结算中   
`settled`：已结算  
settFundingRate | String | 若 settState = `processing`，该字段代表用于本轮结算的资金费率；若 settState = `settled`，该字段代表用于上轮结算的资金费率  
premium | String | 溢价指数  
公式：[max (0，深度加权买价 - 指数价格) – max (0，指数价格 – 深度加权卖价)] / 指数价格  
ts | String | 数据更新时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
针对一些资金费率波动较大的小币种，OKX也将实时关注行情变化，在必要时候，将资金费率收取频率从8小时收付，改成频率较高的6小时/4小时/2小时/1小时收付。因此，用户应关注`fundingTime`及`nextFundingTime`字段以确定合约的资金费收取频率。