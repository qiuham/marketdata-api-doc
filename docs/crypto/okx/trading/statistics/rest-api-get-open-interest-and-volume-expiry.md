---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#trading-statistics-rest-api-get-open-interest-and-volume-expiry
anchor_id: trading-statistics-rest-api-get-open-interest-and-volume-expiry
api_type: REST
updated_at: 2026-07-12 19:17:08.276210
---

# Get open interest and volume (expiry)

Retrieve the open interest and trading volume of calls and puts for each upcoming expiration.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/rubik/stat/option/open-interest-volume-expiry`

> Request Example
    
    
    GET /api/v5/rubik/stat/option/open-interest-volume-expiry?ccy=BTC
    
    
    
    import okx.TradingData as TradingData_api
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    tradingDataAPI = TradingData_api.TradingDataAPI(flag=flag)
    
    # Retrieve the open interest and trading volume of calls and puts for each upcoming expiration
    result = tradingDataAPI.get_interest_volume_expiry(
        ccy="BTC"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
ccy | String | Yes | Currency  
period | String | No | Period, the default is `8H`. e.g. [`8H/1D`]   
Each granularity can provide only one latest piece of data  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            [
                "1630540800000",
                "20210902",
                "6.4",
                "18.4",
                "0.7",
                "0.4"
            ],
            [
                "1630540800000",
                "20210903",
                "47",
                "36.6",
                "1",
                "10.7"
            ]
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
ts | String | Timestamp  
expTime | String | Contract expiry date, the format is `YYYYMMDD`, e.g. `20210623`  
callOI | String | Total call open interest (`coin` as the unit)  
putOI | String | Total put open interest (`coin` as the unit)  
callVol | String | Total call trading volume (`coin` as the unit)  
putVol | String | Total put trading volume (`coin` as the unit)  
The return value array order is: [ts,expTime,callOI,putOI,callVol,putVol]

---

# 看涨看跌持仓总量及交易总量（按到期日分）

获取每个到期日上看涨期权和看跌期权的持仓量和交易量。

#### 限速：5次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/rubik/stat/option/open-interest-volume-expiry`

> 请求示例
    
    
    GET /api/v5/rubik/stat/option/open-interest-volume-expiry?ccy=BTC
    
    
    
    import okx.TradingData as TradingData_api
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    tradingDataAPI = TradingData_api.TradingDataAPI(flag=flag)
    
    # 看涨看跌持仓总量及交易总量（按到期日分）
    result = tradingDataAPI.get_interest_volume_expiry(
        ccy="BTC"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 是 | 币种  
period | String | 否 | 时间粒度，默认值`8H`。支持[`8H/1D`]   
每个粒度仅展示最新的一份数据  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            [
                "1630540800000",
                "20210902",
                "6.4",
                "18.4",
                "0.7",
                "0.4"
            ],
            [
                "1630540800000",
                "20210903",
                "47",
                "36.6",
                "1",
                "10.7"
            ]
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
ts | String | 数据产生时间  
expTime | String | 到期日（格式: YYYYMMDD，如 "20210623"）  
callOI | String | 看涨持仓总量（以`币`为单位）  
putOI | String | 看跌持仓总量（以`币`为单位）  
callVol | String | 看涨交易总量（以`币`为单位）  
putVol | String | 看跌交易总量（以`币`为单位）  
返回值数组顺序分别为是：[ts,expTime,callOI,putOI,callVol,putVol]