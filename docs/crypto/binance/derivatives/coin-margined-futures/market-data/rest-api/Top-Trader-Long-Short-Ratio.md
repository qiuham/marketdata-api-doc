---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/rest-api/Top-Trader-Long-Short-Ratio
api_type: Market Data
updated_at: 2026-01-15T23:39:24.426577
---

# Top Trader Long/Short Ratio (Positions)

## API Description[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Top-Trader-Long-Short-Ratio#api-description "Direct link to API Description")

The proportion of net long and net short positions to total open positions of the top 20% users with the highest margin balance. Long Position % = Long positions of top traders / Total open positions of top traders Short Position % = Short positions of top traders / Total open positions of top traders Long/Short Ratio (Positions) = Long Position % / Short Position %

## HTTP Request[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Top-Trader-Long-Short-Ratio#http-request "Direct link to HTTP Request")

GET `/futures/data/topLongShortPositionRatio`

## Request Weight[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Top-Trader-Long-Short-Ratio#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Top-Trader-Long-Short-Ratio#request-parameters "Direct link to Request Parameters")

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


## Response Example[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Top-Trader-Long-Short-Ratio#response-example "Direct link to Response Example")
    
    
    [    
       {  
    	  "pair": "BTCUSD",  
    	  "longShortRatio": "0.7869",  
    	  "longPosition": "0.6442",  //64.42%  
    	  "shortPosition": "0.4404",  //44.04%  
    	  "timestamp": 1592870400000  
       },  
       {  
         "pair": "BTCUSD",  
    	  "longShortRatio": "1.1231",  
    	  "longPosition": "0.2363",    
    	  "shortPosition": "0.4537",    
    	  "timestamp": 1592956800000  
    	}  
    ]

---

# 大户持仓量多空比

## 接口描述[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Top-Trader-Long-Short-Ratio#接口描述 "接口描述的直接链接")

大户的多头和空头总持仓量占比，大户指保证金余额排名前20%的用户。 多仓持仓量比例 = 大户多仓持仓量 / 大户总持仓量 空仓持仓量比例 = 大户空仓持仓量 / 大户总持仓量 多空持仓量比值 = 多仓持仓量比例 / 空仓持仓量比例

## HTTP请求[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Top-Trader-Long-Short-Ratio#http请求 "HTTP请求的直接链接")

GET `/futures/data/topLongShortPositionRatio`

## 请求权重[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Top-Trader-Long-Short-Ratio#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Top-Trader-Long-Short-Ratio#请求参数 "请求参数的直接链接")

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


## 响应示例[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Top-Trader-Long-Short-Ratio#响应示例 "响应示例的直接链接")
    
    
    [    
       {  
    	  "pair": "BTCUSD",  
    	  "longShortRatio": "0.7869",  
    	  "longPosition": "0.6442",  //64.42%  
    	  "shortPosition": "0.4404",  //44.04%  
    	  "timestamp": 1592870400000  
       },  
       {  
         "pair": "BTCUSD",  
    	  "longShortRatio": "1.1231",  
    	  "longPosition": "0.2363",    
    	  "shortPosition": "0.4537",    
    	  "timestamp": 1592956800000  
    	}  
    ]