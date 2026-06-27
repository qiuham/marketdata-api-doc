---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Taker-BuySell-Volume
api_type: Market Data
updated_at: 2026-01-15T23:47:03.278179
---

# Taker Buy/Sell Volume

## API Description[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Taker-BuySell-Volume#api-description "Direct link to API Description")

Taker Buy/Sell Volume

## HTTP Request[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Taker-BuySell-Volume#http-request "Direct link to HTTP Request")

GET `/futures/data/takerlongshortRatio`

## Request Weight[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Taker-BuySell-Volume#request-weight "Direct link to Request Weight")

**0**

## Request Parameters[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Taker-BuySell-Volume#request-parameters "Direct link to Request Parameters")

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


## Response Example[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Taker-BuySell-Volume#response-example "Direct link to Response Example")
    
    
    [  
        {   
    	    "buySellRatio":"1.5586",  
    	    "buyVol": "387.3300",   
    	    "sellVol":"248.5030",   
    	    "timestamp":"1585614900000"  
        },  
        {   
    	    "buySellRatio":"1.3104",  
    	    "buyVol": "343.9290",   
    	    "sellVol":"248.5030", 	                  
    	    "timestamp":"1583139900000"          
        },      
    ]

---

# 合约主动买卖量

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Taker-BuySell-Volume#接口描述 "接口描述的直接链接")

合约主动买卖量

## HTTP请求[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Taker-BuySell-Volume#http请求 "HTTP请求的直接链接")

GET `/futures/data/takerlongshortRatio`

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Taker-BuySell-Volume#请求权重 "请求权重的直接链接")

**0**

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Taker-BuySell-Volume#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES|   
period| ENUM| YES| "5m","15m","30m","1h","2h","4h","6h","12h","1d"  
limit| LONG| NO| default 30, max 500  
startTime| LONG| NO|   
endTime| LONG| NO|   
  
>   * 若无 startime 和 endtime 限制， 则默认返回当前时间往前的 limit 值
>   * 仅支持最近 30 天的数据
>   * IP限频为1000次/5min
> 


## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Taker-BuySell-Volume#响应示例 "响应示例的直接链接")
    
    
    [  
      {  
        buySellRatio: "1.5586",  
        buyVol: "387.3300", // 主动买入量  
        sellVol: "248.5030", // 主动卖出量  
        timestamp: "1585614900000",  
      },  
      
      {  
        buySellRatio: "1.3104",  
        buyVol: "343.9290",  
        sellVol: "248.5030",  
        timestamp: "1583139900000",  
      },  
    ]