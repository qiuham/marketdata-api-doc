---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#trading-statistics-rest-api-get-contracts-open-interest-and-volume
anchor_id: trading-statistics-rest-api-get-contracts-open-interest-and-volume
api_type: REST
updated_at: 2026-07-21 19:27:13.961220
---

# Get contracts open interest and volume

Retrieve the open interest and trading volume for Expiry Futures and Perpetual Futures.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/rubik/stat/contracts/open-interest-volume`

> Request Example
    
    
    GET /api/v5/rubik/stat/contracts/open-interest-volume?ccy=BTC
    
    
    
    import okx.TradingData as TradingData_api
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    tradingDataAPI = TradingData_api.TradingDataAPI(flag=flag)
    
    # Retrieve the open interest and trading volume for Expiry Futures and Perpetual Futures
    result = tradingDataAPI.get_contracts_interest_volume(
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
                "1630502400000",
                "1713028741.6898",
                "39800873.554"
            ]
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
ts | String | Timestamp  
oi | String | Total open interest（USD）  
vol | String | Total trading volume（USD）  
The return value array order is: [ts,oi,vol]

---

# 获取合约持仓量及交易量

获取交割永续的持仓量和交易量。

#### 限速：5次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/rubik/stat/contracts/open-interest-volume`

> 请求示例
    
    
    GET /api/v5/rubik/stat/contracts/open-interest-volume?ccy=BTC
    
    
    
    import okx.TradingData as TradingData_api
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    tradingDataAPI = TradingData_api.TradingDataAPI(flag=flag)
    
    # 获取合约持仓量及交易量
    result = tradingDataAPI.get_contracts_interest_volume(
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
                "1630502400000",
                "1713028741.6898",
                "39800873.554"
            ]
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
ts | String | 数据产生时间  
oi | String | 持仓总量（USD）  
vol | String | 交易总量（USD）  
返回值数组顺序分别为是：[ts,oi,vol]