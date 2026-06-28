---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Long-Short-Ratio
api_type: Market Data
updated_at: 2026-01-15T23:46:53.315617
---

# Long/Short Ratio

## API Description[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Long-Short-Ratio#api-description "Direct link to API Description")

Query symbol Long/Short Ratio

## HTTP Request[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Long-Short-Ratio#http-request "Direct link to HTTP Request")

GET `/futures/data/globalLongShortAccountRatio`

## Request Weight[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Long-Short-Ratio#request-weight "Direct link to Request Weight")

**0**

## Request Parameters[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Long-Short-Ratio#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
period| ENUM| YES| "5m","15m","30m","1h","2h","4h","6h","12h","1d"  
limit| LONG| NO| default 30, max 500  
startTime| LONG| NO|   
endTime| LONG| NO|   
  
>   * If startTime and endTime are not sent, the most recent data is returned.
>   * Only the data of the latest 30 days is available.
>   * IP rate limit 1000 requests/5min
> 


## Response Example[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Long-Short-Ratio#response-example "Direct link to Response Example")
    
    
    [  
        {   
             "symbol":"BTCUSDT",  // long/short account num ratio of all traders  
    	      "longShortRatio":"0.1960",  //long account num ratio of all traders  
    	      "longAccount": "0.6622",   // short account num ratio of all traders  
    	      "shortAccount":"0.3378",   
    	      "timestamp":"1583139600000"  
          
         },  
           
         {  
               
             "symbol":"BTCUSDT",  
    	      "longShortRatio":"1.9559",  
    	      "longAccount": "0.6617",   
    	      "shortAccount":"0.3382", 	                  
    	      "timestamp":"1583139900000"  
    	                 
            },     
    	      
    ]

---

# 多空持仓人数比

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Long-Short-Ratio#接口描述 "接口描述的直接链接")

多空持仓人数比

## HTTP请求[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Long-Short-Ratio#http请求 "HTTP请求的直接链接")

GET `/futures/data/globalLongShortAccountRatio`

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Long-Short-Ratio#请求权重 "请求权重的直接链接")

**0**

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Long-Short-Ratio#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES|   
period| ENUM| YES| "5m","15m","30m","1h","2h","4h","6h","12h","1d"  
limit| LONG| NO| default 30, max 500  
startTime| LONG| NO|   
endTime| LONG| NO|   
  
>   * 若无 startime 和 endtime 限制， 则默认返回当前时间往前的limit值
>   * 仅支持最近30天的数据
>   * IP限频为1000次/5min
> 


## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Long-Short-Ratio#响应示例 "响应示例的直接链接")
    
    
    [  
        {   
             "symbol":"BTCUSDT",  
    	      "longShortRatio":"0.1960", // 多空人数比值  
    	      "longAccount": "0.6622", // 多仓人数比例  
    	      "shortAccount":"0.3378", // 空仓人数比例  
    	      "timestamp":"1583139600000"  
          
         },  
           
         {  
               
             "symbol":"BTCUSDT",  
    	      "longShortRatio":"1.9559",  
    	      "longAccount": "0.6617",   
    	      "shortAccount":"0.3382", 	                  
    	      "timestamp":"1583139900000"  
    	                 
            },     
    	      
    ]