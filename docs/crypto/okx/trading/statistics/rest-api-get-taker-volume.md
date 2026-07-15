---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#trading-statistics-rest-api-get-taker-volume
anchor_id: trading-statistics-rest-api-get-taker-volume
api_type: REST
updated_at: 2026-07-15 19:20:12.430244
---

# Get taker volume

Retrieve the taker volume for both buyers and sellers.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/rubik/stat/taker-volume`

> Request Example
    
    
    GET /api/v5/rubik/stat/taker-volume?ccy=BTC&instType=SPOT
    
    
    
    import okx.TradingData as TradingData_api
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    tradingDataAPI = TradingData_api.TradingDataAPI(flag=flag)
    
    # Retrieve the taker volume for both buyers and sellers
    result = tradingDataAPI.get_taker_volume(
        ccy="BTC",
        instType="SPOT"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
ccy | String | Yes | Currency  
instType | String | Yes | Instrument type  
`SPOT`  
`CONTRACTS`  
begin | String | No | Begin time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
end | String | No | End time, Unix timestamp format in milliseconds, e.g. `1597026383011`  
period | String | No | Period, the default is `5m`, e.g. [`5m`/`1H`/`1D`]   
`5m` granularity can only query data within two days at most  
`1H` granularity can only query data within 30 days at most   
`1D` granularity can only query data within 180 days at most  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            [
                "1630425600000",
                "7596.2651",
                "7149.4855"
            ],
            [
                "1630339200000",
                "5312.7876",
                "7002.7541"
            ]
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
ts | String | Timestamp  
sellVol | String | Sell volume  
buyVol | String | Buy volume  
The return value array order is: [ts,sellVol,buyVol]

---

# 获取主动买入/卖出情况

获取taker主动买入和卖出的交易量

#### 限速：5次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/rubik/stat/taker-volume`

> 请求示例
    
    
    GET /api/v5/rubik/stat/taker-volume?ccy=BTC&instType=SPOT
    
    
    
    import okx.TradingData as TradingData_api
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    tradingDataAPI = TradingData_api.TradingDataAPI(flag=flag)
    
    # 获取主动买入/卖出情况
    result = tradingDataAPI.get_taker_volume(
        ccy="BTC",
        instType="SPOT"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 是 | 币种  
instType | String | 是 | 产品类型  
`SPOT`：币币  
`CONTRACTS`：衍生品  
begin | String | 否 | 开始时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
end | String | 否 | 结束时间，Unix时间戳的毫秒数格式，如 `1597026383011`  
period | String | 否 | 时间粒度，默认值`5m`。支持[`5m`/`1H`/`1D`]   
`5m`粒度最多只能查询两天之内的数据  
`1H`粒度最多只能查询30天之内的数据  
`1D`粒度最多只能查询180天之内的数据  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            [
                "1630425600000",
                "7596.2651",
                "7149.4855"
            ],
            [
                "1630339200000",
                "5312.7876",
                "7002.7541"
            ]
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
ts | String | 数据产生时间  
sellVol | String | 卖出量  
buyVol | String | 买入量  
返回值数组顺序分别为是：[ts,sellVol,buyVol]