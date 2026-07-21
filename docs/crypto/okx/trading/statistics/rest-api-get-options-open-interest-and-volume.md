---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#trading-statistics-rest-api-get-options-open-interest-and-volume
anchor_id: trading-statistics-rest-api-get-options-open-interest-and-volume
api_type: REST
updated_at: 2026-07-21 19:27:14.270449
---

# Get options open interest and volume

Retrieve the open interest and trading volume for options.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/rubik/stat/option/open-interest-volume`

> Request Example
    
    
    GET /api/v5/rubik/stat/option/open-interest-volume?ccy=BTC
    
    
    
    import okx.TradingData as TradingData_api
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    tradingDataAPI = TradingData_api.TradingDataAPI(flag=flag)
    
    # Retrieve the open interest and trading volume for options
    result = tradingDataAPI.get_options_interest_volume(
        ccy="BTC",
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
ccy | String | Yes | Currency  
period | String | No | Period, the default is `8H`. e.g. [`8H/1D`]   
Each granularity can only query 72 pieces of data at the earliest  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            [
                "1630368000000",
                "3458.1000",
                "78.8000"
            ]
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
ts | String | Timestamp  
oi | String | Total open interest , unit in `ccy` (in request parameter)  
vol | String | Total trading volume , unit in `ccy` (in request parameter)  
The return value array order is: [ts,oi,vol]

---

# 获取期权持仓量及交易量

获取期权的持仓量和交易量。

#### 限速：5次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/rubik/stat/option/open-interest-volume`

> 请求示例
    
    
    GET /api/v5/rubik/stat/option/open-interest-volume?ccy=BTC
    
    
    
    import okx.TradingData as TradingData_api
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    tradingDataAPI = TradingData_api.TradingDataAPI(flag=flag)
    
    # 获取期权持仓量及交易量
    result = tradingDataAPI.get_options_interest_volume(
        ccy="BTC",
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 是 | 币种  
period | String | 否 | 时间粒度，默认值`8H`。支持[`8H/1D`]   
每个粒度最多只能查询72条数据  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            [
                "1630368000000",
                "3458.1000",
                "78.8000"
            ]
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
ts | String | 数据产生时间  
oi | String | 持仓总量，单位为请求参数的`ccy`  
vol | String | 交易总量，单位为请求参数的`ccy`  
返回值数组顺序分别为是：[ts,oi,vol]