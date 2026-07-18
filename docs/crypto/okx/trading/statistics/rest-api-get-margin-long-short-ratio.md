---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#trading-statistics-rest-api-get-margin-long-short-ratio
anchor_id: trading-statistics-rest-api-get-margin-long-short-ratio
api_type: REST
updated_at: 2026-07-18 20:04:50.859708
---

# Get margin long/short ratio

Retrieve the ratio of cumulative amount of quote currency to base currency.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/rubik/stat/margin/loan-ratio`

> Request Example
    
    
    GET /api/v5/rubik/stat/margin/loan-ratio?ccy=BTC
    
    
    
    import okx.TradingData as TradingData_api
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    tradingDataAPI = TradingData_api.TradingDataAPI(flag=flag)
    
    # Retrieve the ratio of cumulative amount between currency margin quote currency and base currency
    result = tradingDataAPI.get_margin_lending_ratio(
        ccy="BTC",
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
ccy | String | Yes | Currency  
begin | String | No | Begin time, e.g. `1597026383085`  
end | String | No | End time, e.g. `1597026383085`  
period | String | No | Period  
`m`: Minute, `H`: Hour, `D`: Day  
the default is `5m`, e.g. [`5m`/`1H`/`1D`]   
`5m` granularity can only query data within two days at most  
`1H` granularity can only query data within 30 days at most  
`1D` granularity can only query data within 180 days at most  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            [
                "1630492800000",
                "0.4614"
            ],
            [
                "1630492500000",
                "0.5767"
            ]
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
ts | String | Timestamp  
ratio | String | Margin lending ratio  
The return value array order is: [ts,ratio]

---

# 获取杠杆多空比

获取借入计价货币与借入交易货币的累计数额比值。

#### 限速：5次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/rubik/stat/margin/loan-ratio`

> 请求示例
    
    
    GET /api/v5/rubik/stat/margin/loan-ratio?ccy=BTC
    
    
    
    import okx.TradingData as TradingData_api
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    tradingDataAPI = TradingData_api.TradingDataAPI(flag=flag)
    
    # 获取杠杆多空比
    result = tradingDataAPI.get_margin_lending_ratio(
        ccy="BTC",
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 是 | 币种  
begin | String | 否 | 开始时间，如 `1597026383085`  
end | String | 否 | 结束时间，如 `1597026383011`  
period | String | 否 | 时间粒度  
`m`：分钟，`H`：小时，`D`：天  
默认值`5m`，支持[`5m`/`1H`/`1D`]   
`5m`粒度最多只能查询两天之内的数据  
`1H`粒度最多只能查询30天之内的数据   
`1D`粒度最多只能查询180天之内的数据  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            [
                "1630492800000",
                "0.4614"
            ],
            [
                "1630492500000",
                "0.5767"
            ]
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
ts | String | 数据产生时间  
ratio | String | 多空比值  
返回值数组顺序分别为是：[ts,ratio]