---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#trading-statistics-rest-api-get-put-call-ratio
anchor_id: trading-statistics-rest-api-get-put-call-ratio
api_type: REST
updated_at: 2026-07-17 19:17:44.905547
---

# Get put/call ratio

Retrieve the open interest ratio and trading volume ratio of calls vs puts.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/rubik/stat/option/open-interest-volume-ratio`

> Request Example
    
    
    GET /api/v5/rubik/stat/option/open-interest-volume-ratio?ccy=BTC
    
    
    
    import okx.TradingData as TradingData_api
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    tradingDataAPI = TradingData_api.TradingDataAPI(flag=flag)
    
    # Retrieve the open interest ratio and trading volume ratio of calls vs puts
    result = tradingDataAPI.get_put_call_ratio(
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
                "1630512000000",
                "2.7261",
                "2.3447"
            ],
            [
                "1630425600000",
                "2.8101",
                "2.3438"
            ]
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
ts | String | Timestamp of data generation time  
oiRatio | String | Long/Short open interest ratio  
volRatio | String | Long/Short trading volume ratio  
The return value array order is: [ts,oiRatio,volRatio]

---

# 看涨/看跌期权合约 持仓总量比/交易总量比

获取看涨期权和看跌期权的持仓量比值，以及交易量比值。

#### 限速：5次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/rubik/stat/option/open-interest-volume-ratio`

> 请求示例
    
    
    GET /api/v5/rubik/stat/option/open-interest-volume-ratio?ccy=BTC
    
    
    
    import okx.TradingData as TradingData_api
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    tradingDataAPI = TradingData_api.TradingDataAPI(flag=flag)
    
    # 看涨/看跌期权合约 持仓总量比/交易总量比
    result = tradingDataAPI.get_put_call_ratio(
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
                "1630512000000",
                "2.7261",
                "2.3447"
            ],
            [
                "1630425600000",
                "2.8101",
                "2.3438"
            ]
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
ts | String | 数据产生时间  
oiRatio | String | 看涨/看跌 持仓总量比  
volRatio | String | 看涨/看跌 交易总量比  
返回值数组顺序分别为是：[ts,oiRatio,volRatio]