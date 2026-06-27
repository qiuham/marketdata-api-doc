---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/rest-api/Open-Interest-Statistics
api_type: Market Data
updated_at: 2026-01-15T23:38:50.323148
---

# Open Interest Statistics

## API Description[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Open-Interest-Statistics#api-description "Direct link to API Description")

Query open interest stats

## HTTP Request[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Open-Interest-Statistics#http-request "Direct link to HTTP Request")

GET `/futures/data/openInterestHist`

## Request Weight[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Open-Interest-Statistics#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Open-Interest-Statistics#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
pair| STRING| YES| BTCUSD  
contractType| ENUM| YES| ALL, CURRENT_QUARTER, NEXT_QUARTER, PERPETUAL  
period| ENUM| YES| "5m","15m","30m","1h","2h","4h","6h","12h","1d"  
limit| LONG| NO| Default 30,Max 500  
startTime| LONG| NO|   
endTime| LONG| NO|   
  
>   * If startTime and endTime are not sent, the most recent data is returned.
>   * Only the data of the latest 30 days is available.
> 


## Response Example[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Open-Interest-Statistics#response-example "Direct link to Response Example")
    
    
    [    
       {  
    	  "pair": "BTCUSD",  
    	  "contractType": "CURRENT_QUARTER",  
    	  "sumOpenInterest": "20403",  //unit: cont  
    	  "sumOpenInterestValue": "176196512.23400000", //unit: base asset  
    	  "timestamp": 1591261042378  
       },  
       {  
         "pair": "BTCUSD",  
    	  "contractType": "CURRENT_QUARTER",  
    	  "sumOpenInterest": "20401",    
    	  "sumOpenInterestValue": "176178704.98700000",   
    	  "timestamp": 1583128200000  
       }  
    ]

---

# 合约持仓量

## 接口描述[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Open-Interest-Statistics#接口描述 "接口描述的直接链接")

合约持仓量

## HTTP请求[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Open-Interest-Statistics#http请求 "HTTP请求的直接链接")

GET `/futures/data/openInterestHist`

## 请求权重[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Open-Interest-Statistics#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Open-Interest-Statistics#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
pair| STRING| YES| BTCUSD  
contractType| ENUM| YES| ALL, CURRENT_QUARTER, NEXT_QUARTER, PERPETUAL  
period| ENUM| YES| "5m","15m","30m","1h","2h","4h","6h","12h","1d"  
limit| LONG| NO| Default 30,Max 500  
startTime| LONG| NO|   
endTime| LONG| NO|   
  
>   * 若无 startime 和 endtime 限制， 则默认返回当前时间往前的limit值
>   * 仅支持最近30天的数据
> 


## 响应示例[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Open-Interest-Statistics#响应示例 "响应示例的直接链接")
    
    
    [    
       {  
    	  "pair": "BTCUSD",  
    	  "contractType": "CURRENT_QUARTER",  
    	  "sumOpenInterest": "20403",  //unit: cont  
    	  "sumOpenInterestValue": "176196512.23400000", //unit: base asset  
    	  "timestamp": 1591261042378  
       },  
       {  
         "pair": "BTCUSD",  
    	  "contractType": "CURRENT_QUARTER",  
    	  "sumOpenInterest": "20401",    
    	  "sumOpenInterestValue": "176178704.98700000",   
    	  "timestamp": 1583128200000  
       }  
    ]