---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#trading-statistics-rest-api-get-open-interest-and-volume-strike
anchor_id: trading-statistics-rest-api-get-open-interest-and-volume-strike
api_type: REST
updated_at: 2026-07-18 20:04:53.662953
---

# Get open interest and volume (strike)

Retrieve the taker volume for both buyers and sellers of calls and puts.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/rubik/stat/option/open-interest-volume-strike`

> Request Example
    
    
    GET /api/v5/rubik/stat/option/open-interest-volume-strike?ccy=BTC&expTime=20210901
    
    
    
    import okx.TradingData as TradingData_api
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    tradingDataAPI = TradingData_api.TradingDataAPI(flag=flag)
    
    # Retrieve the taker volume for both buyers and sellers of calls and puts
    result = tradingDataAPI.get_interest_volume_strike(
        ccy="BTC",
        expTime="20210623"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
ccy | String | Yes | Currency  
expTime | String | Yes | Contract expiry date, the format is `YYYYMMdd`, e.g. `20210623`  
period | String | No | Period, the default is `8H`. e.g. [`8H/1D`]   
Each granularity can provide only one latest piece of data  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            [
                "1630540800000",
                "10000",
                "0",
                "0.5",
                "0",
                "0"
            ],
            [
                "1630540800000",
                "14000",
                "0",
                "5.2",
                "0",
                "0"
            ]
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
ts | String | Timestamp  
strike | String | Strike price  
callOI | String | Total call open interest (`coin` as the unit)  
putOI | String | Total put open interest (`coin` as the unit)  
callVol | String | Total call trading volume (`coin` as the unit)  
putVol | String | Total put trading volume (`coin` as the unit)  
The return value array order is: [ts,strike,callOI,putOI,callVol,putVol]

---

# 看涨看跌持仓总量及交易总量（按执行价格分）

获取看涨期权和看跌期权的taker主动买入和卖出的交易量。

#### 限速：5次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/rubik/stat/option/open-interest-volume-strike`

> 请求示例
    
    
    GET /api/v5/rubik/stat/option/open-interest-volume-strike?ccy=BTC&expTime=20210901
    
    
    
    import okx.TradingData as TradingData_api
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    tradingDataAPI = TradingData_api.TradingDataAPI(flag=flag)
    
    # 看涨看跌持仓总量及交易总量（按执行价格分）
    result = tradingDataAPI.get_interest_volume_strike(
        ccy="BTC",
        expTime="20210623"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 是 | 币种  
expTime | String | 是 | 到期日（格式: `YYYYMMdd`，如 "20210623"）  
period | String | 否 | 时间粒度，默认值`8H`。支持[`8H/1D`]   
每个粒度仅展示最新的一份数据  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            [
                "1630540800000",
                "10000",
                "0",
                "0.5",
                "0",
                "0"
            ],
            [
                "1630540800000",
                "14000",
                "0",
                "5.2",
                "0",
                "0"
            ]
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
ts | String | 数据产生时间  
strike | String | 执行价格  
callOI | String | 看涨持仓总量（以`币`为单位）  
putOI | String | 看跌持仓总量（以`币`为单位）  
callVol | String | 看涨交易总量（以`币`为单位）  
putVol | String | 看跌交易总量（以`币`为单位）  
返回值数组顺序分别为是：[ts,strike,callOI,putOI,callVol,putVol]