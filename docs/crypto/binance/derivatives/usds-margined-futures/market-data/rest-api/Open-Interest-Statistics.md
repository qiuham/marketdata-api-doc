---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Open-Interest-Statistics
api_type: Market Data
updated_at: 2026-01-15T23:46:56.652300
---

# Open Interest Statistics

## API Description[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Open-Interest-Statistics#api-description "Direct link to API Description")

Open Interest Statistics

## HTTP Request[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Open-Interest-Statistics#http-request "Direct link to HTTP Request")

GET `/futures/data/openInterestHist`

## Request Weight[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Open-Interest-Statistics#request-weight "Direct link to Request Weight")

**0**

## Request Parameters[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Open-Interest-Statistics#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
period| ENUM| YES| "5m","15m","30m","1h","2h","4h","6h","12h","1d"  
limit| LONG| NO| default 30, max 500  
startTime| LONG| NO|   
endTime| LONG| NO|   
  
>   * If startTime and endTime are not sent, the most recent data is returned.
>   * Only the data of the latest 1 month is available.
>   * IP rate limit 1000 requests/5min
> 


## Response Example[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Open-Interest-Statistics#response-example "Direct link to Response Example")
    
    
    [  
        {   
             "symbol":"BTCUSDT",  
    	      "sumOpenInterest":"20403.63700000",  // total open interest   
    	      "sumOpenInterestValue": "150570784.07809979",   // total open interest value  
              "CMCCirculatingSupply": "165880.538", // circulating supply provided by CMC  
    	      "timestamp":"1583127900000"  
        },       
        {   
             "symbol":"BTCUSDT",  
             "sumOpenInterest":"20401.36700000",  
             "sumOpenInterestValue":"149940752.14464448",  
             "CMCCirculatingSupply": "165900.14853",  
             "timestamp":"1583128200000"      
        },     
    ]

---

# 合约持仓量历史

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Open-Interest-Statistics#接口描述 "接口描述的直接链接")

查询合约持仓量历史

## HTTP请求[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Open-Interest-Statistics#http请求 "HTTP请求的直接链接")

GET `/futures/data/openInterestHist`

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Open-Interest-Statistics#请求权重 "请求权重的直接链接")

**0**

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Open-Interest-Statistics#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES|   
period| ENUM| YES| "5m","15m","30m","1h","2h","4h","6h","12h","1d"  
limit| LONG| NO| default 30, max 500  
startTime| LONG| NO|   
endTime| LONG| NO|   
  
>   * 若无 startime 和 endtime 限制， 则默认返回当前时间往前的limit值
>   * 仅支持最近1个月的数据
>   * IP限频为1000次/5min
> 


## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Open-Interest-Statistics#响应示例 "响应示例的直接链接")
    
    
    [  
        {   
             "symbol":"BTCUSDT",  
    	      "sumOpenInterest":"20403.12345678",// 持仓总数量  
    	      "sumOpenInterestValue": "176196512.12345678", // 持仓总价值  
              "CMCCirculatingSupply": "165880.538", // CMC提供的流通供应量  
    	      "timestamp":"1583127900000"  
          
         },  
         {  
           
             "symbol":"BTCUSDT",  
             "sumOpenInterest":"20401.36700000",  
             "sumOpenInterestValue":"149940752.14464448",  
             "CMCCirculatingSupply": "165900.14853",  
             "timestamp":"1583128200000"  
         },     
    ]