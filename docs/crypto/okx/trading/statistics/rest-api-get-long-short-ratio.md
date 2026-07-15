---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#trading-statistics-rest-api-get-long-short-ratio
anchor_id: trading-statistics-rest-api-get-long-short-ratio
api_type: REST
updated_at: 2026-07-15 19:20:14.298167
---

# Get long/short ratio

Retrieve the ratio of users with net long vs net short positions for Expiry Futures and Perpetual Futures.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/rubik/stat/contracts/long-short-account-ratio`

> Request Example
    
    
    GET /api/v5/rubik/stat/contracts/long-short-account-ratio?ccy=BTC
    
    
    
    import okx.TradingData as TradingData_api
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    tradingDataAPI = TradingData_api.TradingDataAPI(flag=flag)
    
    # Retrieve the ratio of users with net long vs net short positions for Expiry Futures and Perpetual Futures
    result = tradingDataAPI.get_long_short_ratio(
        ccy="BTC",
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
ccy | String | Yes | Currency  
begin | String | No | Begin time, e.g. `1597026383085`  
end | String | No | End time, e.g. `1597026383011`  
period | String | No | Period, the default is `5m`, e.g. [`5m/1H/1D`]   
`5m` granularity can only query data within two days at most  
`1H` granularity can only query data within 30 days at most   
`1D` granularity can only query data within 180 days at most  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            [
                "1630502100000",
                "1.25"
            ]
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
ts | String | Timestamp  
ratio | String | Long/Short ratio  
The return value array order is: [ts,ratio]

---

# 获取多空持仓人数比

获取交割永续净开多持仓用户数与净开空持仓用户数的比值。

#### 限速：5次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/rubik/stat/contracts/long-short-account-ratio`

> 请求示例
    
    
    GET /api/v5/rubik/stat/contracts/long-short-account-ratio?ccy=BTC
    
    
    
    import okx.TradingData as TradingData_api
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    tradingDataAPI = TradingData_api.TradingDataAPI(flag=flag)
    
    # 获取合约多空持仓人数比
    result = tradingDataAPI.get_long_short_ratio(
        ccy="BTC",
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 是 | 币种  
begin | String | 否 | 开始时间，如 `1597026383085`  
end | String | 否 | 结束时间，如 `1597026383011`  
period | String | 否 | 时间粒度，默认值`5m`。支持[5m/1H/1D]   
`5m`粒度最多只能查询两天之内的数据  
`1H`粒度最多只能查询30天之内的数据   
`1D`粒度最多只能查询180天之内的数据  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            [
                "1630502100000",
                "1.25"
            ]
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
ts | String | 数据产生时间  
ratio | String | 多空人数比  
返回值数组顺序分别为是：[ts,ratio]