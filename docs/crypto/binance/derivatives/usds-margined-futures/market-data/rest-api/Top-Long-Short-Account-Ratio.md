---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Top-Long-Short-Account-Ratio
api_type: Market Data
updated_at: 2026-01-15T23:47:03.341546
---

# Top Trader Long/Short Ratio (Accounts)

## API Description[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Top-Long-Short-Account-Ratio#api-description "Direct link to API Description")

The proportion of net long and net short accounts to total accounts of the top 20% users with the highest margin balance. Each account is counted once only. Long Account % = Accounts of top traders with net long positions / Total accounts of top traders with open positions Short Account % = Accounts of top traders with net short positions / Total accounts of top traders with open positions Long/Short Ratio (Accounts) = Long Account % / Short Account %

## HTTP Request[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Top-Long-Short-Account-Ratio#http-request "Direct link to HTTP Request")

GET `/futures/data/topLongShortAccountRatio`

## Request Parameters[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Top-Long-Short-Account-Ratio#request-parameters "Direct link to Request Parameters")

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


## Response Example[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Top-Long-Short-Account-Ratio#response-example "Direct link to Response Example")
    
    
    [  
        {   
             "symbol":"BTCUSDT",  
    	      "longShortRatio":"1.8105",  // long/short account num ratio of top traders  
    	      "longAccount": "0.6442",   // long account num ratio of top traders   
    	      "shortAccount":"0.3558",   // long account num ratio of top traders   
    	      "timestamp":"1583139600000"  
        },   
        {       
             "symbol":"BTCUSDT",  
    	      "longShortRatio":"0.5576",  
    	      "longAccount": "0.3580",   
    	      "shortAccount":"0.6420", 	                  
    	      "timestamp":"1583139900000"           
        }    
    ]

---

# 大户账户数多空比

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Top-Long-Short-Account-Ratio#接口描述 "接口描述的直接链接")

持仓大户的净持仓多头和空头账户数占比，大户指保证金余额排名前20%的用户。一个账户记一次。 多仓账户数比例 = 持多仓大户数 / 总持仓大户数 空仓账户数比例 = 持空仓大户数 / 总持仓大户数 多空账户数比值 = 多仓账户数比例 / 空仓账户数比例

## HTTP请求[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Top-Long-Short-Account-Ratio#http请求 "HTTP请求的直接链接")

GET `/futures/data/topLongShortAccountRatio`

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Top-Long-Short-Account-Ratio#请求参数 "请求参数的直接链接")

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


## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Top-Long-Short-Account-Ratio#响应示例 "响应示例的直接链接")
    
    
    [  
        {   
             "symbol":"BTCUSDT",  
    	      "longShortRatio":"1.8105",// 大户多空账户数比值  
    	      "longAccount": "0.6442", // 大户多仓账户数比例  
    	      "shortAccount":"0.3558", // 大户空仓账户数比例  
    	      "timestamp":"1583139600000"  
        },  
        {  
               
             "symbol":"BTCUSDT",  
    	      "longShortRatio":"1.8233",  
    	      "longAccount": "0.5338",   
    	      "shortAccount":"0.3454", 	                  
    	      "timestamp":"1583139900000"  
    	}  
    ]