---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/rest-api/Basis
api_type: Market Data
updated_at: 2026-01-15T23:37:57.965641
---

# Basis

## API Description[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Basis#api-description "Direct link to API Description")

Query basis

## HTTP Request[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Basis#http-request "Direct link to HTTP Request")

GET `/futures/data/basis`

## Request Weight[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Basis#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Basis#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
pair| STRING| YES| BTCUSD  
contractType| ENUM| YES| CURRENT_QUARTER, NEXT_QUARTER, PERPETUAL  
period| ENUM| YES| "5m","15m","30m","1h","2h","4h","6h","12h","1d"  
limit| LONG| NO| Default 30,Max 500  
startTime| LONG| NO|   
endTime| LONG| NO|   
  
>   * If startTime and endTime are not sent, the most recent data is returned.
>   * Only the data of the latest 30 days is available.
> 


## Response Example[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Basis#response-example "Direct link to Response Example")
    
    
    [    
       {  
            "indexPrice": "29269.93972727",  
            "contractType": "CURRENT_QUARTER",  
            "basisRate": "0.0024",  
            "futuresPrice": "29341.3",  
            "annualizedBasisRate": "0.0283",  
            "basis": "71.36027273",  
            "pair": "BTCUSD",  
            "timestamp": 1653381600000  
       }  
    ]

---

# 基差

## 接口描述[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Basis#接口描述 "接口描述的直接链接")

查询基差

## HTTP请求[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Basis#http请求 "HTTP请求的直接链接")

GET `/futures/data/basis`

## 请求权重[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Basis#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Basis#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
pair| STRING| YES| BTCUSD  
contractType| ENUM| YES| CURRENT_QUARTER, NEXT_QUARTER, PERPETUAL  
period| ENUM| YES| "5m","15m","30m","1h","2h","4h","6h","12h","1d"  
limit| LONG| NO| Default 30,Max 500  
startTime| LONG| NO|   
endTime| LONG| NO|   
  
>   * 若无 startime 和 endtime 限制， 则默认返回当前时间往前的limit值
>   * 仅支持最近30天的数据
> 


## 响应示例[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Basis#响应示例 "响应示例的直接链接")
    
    
    [    
       {  
            "indexPrice": "29269.93972727",  
            "contractType": "CURRENT_QUARTER",  
            "basisRate": "0.0024",  
            "futuresPrice": "29341.3",  
            "annualizedBasisRate": "0.0283",  
            "basis": "71.36027273",  
            "pair": "BTCUSD",  
            "timestamp": 1653381600000  
       }  
    ]