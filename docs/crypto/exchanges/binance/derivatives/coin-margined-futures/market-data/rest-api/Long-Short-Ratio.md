---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/rest-api/Long-Short-Ratio
api_type: Market Data
updated_at: 2026-01-15T23:38:29.407360
---

# Long/Short Ratio

## API Description[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Long-Short-Ratio#api-description "Direct link to API Description")

Query symbol Long/Short Ratio

## HTTP Request[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Long-Short-Ratio#http-request "Direct link to HTTP Request")

GET `/futures/data/globalLongShortAccountRatio`

## Request Weight[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Long-Short-Ratio#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Long-Short-Ratio#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
pair| STRING| YES| BTCUSD  
period| ENUM| YES| "5m","15m","30m","1h","2h","4h","6h","12h","1d"  
limit| LONG| NO| Default 30,Max 500  
startTime| LONG| NO|   
endTime| LONG| NO|   
  
>   * If startTime and endTime are not sent, the most recent data is returned.
>   * Only the data of the latest 30 days is available.
> 


## Response Example[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Long-Short-Ratio#response-example "Direct link to Response Example")
    
    
    [    
       {  
    	  "pair": "BTCUSD",  
    	  "longShortRatio": "0.1960",  
    	  "longAccount": "0.6622",  //66.22%  
    	  "shortAccount": "0.3378",  //33.78%  
    	  "timestamp": 1583139600000  
       },  
       {  
         "pair": "BTCUSD",  
    	  "longShortRatio": "1.9559",  
    	  "longAccount": "0.6617",    
    	  "shortAccount": "0.3382",    
    	  "timestamp": 1583139900000  
    	}  
    ]

---

# 多空持仓人数比

## 接口描述[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Long-Short-Ratio#接口描述 "接口描述的直接链接")

多空持仓人数比

## HTTP请求[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Long-Short-Ratio#http请求 "HTTP请求的直接链接")

GET `/futures/data/globalLongShortAccountRatio`

## 请求权重[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Long-Short-Ratio#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Long-Short-Ratio#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
pair| STRING| YES| BTCUSD  
period| ENUM| YES| "5m","15m","30m","1h","2h","4h","6h","12h","1d"  
limit| LONG| NO| Default 30,Max 500  
startTime| LONG| NO|   
endTime| LONG| NO|   
  
>   * 若无 startime 和 endtime 限制， 则默认返回当前时间往前的limit值
>   * 仅支持最近30天的数据
> 


## 响应示例[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Long-Short-Ratio#响应示例 "响应示例的直接链接")
    
    
    [    
       {  
    	  "pair": "BTCUSD",  
    	  "longShortRatio": "0.1960",  
    	  "longAccount": "0.6622",  //66.22%  
    	  "shortAccount": "0.3378",  //33.78%  
    	  "timestamp": 1583139600000  
       },  
       {  
         "pair": "BTCUSD",  
    	  "longShortRatio": "1.9559",  
    	  "longAccount": "0.6617",    
    	  "shortAccount": "0.3382",    
    	  "timestamp": 1583139900000  
    	}  
    ]