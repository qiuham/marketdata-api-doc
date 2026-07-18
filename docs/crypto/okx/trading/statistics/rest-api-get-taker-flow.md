---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#trading-statistics-rest-api-get-taker-flow
anchor_id: trading-statistics-rest-api-get-taker-flow
api_type: REST
updated_at: 2026-07-18 20:04:53.974020
---

# Get taker flow

This shows the relative buy/sell volume for calls and puts. It shows whether traders are bullish or bearish on price and volatility.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/rubik/stat/option/taker-block-volume`

> Request Example
    
    
    GET /api/v5/rubik/stat/option/taker-block-volume?ccy=BTC
    
    
    
    import okx.TradingData as TradingData_api
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    tradingDataAPI = TradingData_api.TradingDataAPI(flag=flag)
    
    # This shows the relative buy/sell volume for calls and puts. It shows whether traders are bullish or bearish on price and volatility
    result = tradingDataAPI.get_taker_block_volume(
        ccy="BTC",
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
ccy | String | Yes | currency  
period | String | No | period, the default is `8H`. e.g. [`8H/1D`]   
Each granularity can provide only one latest piece of data  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            "1630512000000",
            "8.55",
            "67.3",
            "16.05",
            "16.3",
            "126.4",
            "40.7"
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
ts | String | Timestamp  
callBuyVol | String | call option buy volume, in settlement currency  
callSellVol | String | call option sell volume, in settlement currency  
putBuyVol | String | put option buy volume, in settlement currency  
putSellVol | String | put option sell volume, in settlement currency  
callBlockVol | String | call block volume  
putBlockVol | String | put block volume  
The return value array order is: [ts,callBuyVol,callSellVol,putBuyVol,putSellVol,callBlockVol,putBlockVol]

---

# 看跌/看涨期权合约 主动买入/卖出量

该指标展示某一时刻，单位时间内看跌/看涨期权的主动（taker）买入/卖出交易量

#### 限速：5次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/rubik/stat/option/taker-block-volume`

> 请求示例
    
    
    GET /api/v5/rubik/stat/option/taker-block-volume?ccy=BTC
    
    
    
    import okx.TradingData as TradingData_api
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    tradingDataAPI = TradingData_api.TradingDataAPI(flag=flag)
    
    # 看跌/看涨期权合约 主动买入/卖出量
    result = tradingDataAPI.get_taker_block_volume(
        ccy="BTC",
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
            "1630512000000",
            "8.55",
            "67.3",
            "16.05",
            "16.3",
            "126.4",
            "40.7"
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
ts | String | 数据产生时间  
callBuyVol | String | 看涨买入量 以结算货币为单位  
callSellVol | String | 看涨卖出量 以结算货币为单位  
putBuyVol | String | 看跌买入量 以结算货币为单位  
putSellVol | String | 看跌卖出量 以结算货币为单位  
callBlockVol | String | 看涨大单  
putBlockVol | String | 看跌大单  
返回值数组顺序分别为是：[ts,callBuyVol,callSellVol,putBuyVol,putSellVol,callBlockVol,putBlockVol]