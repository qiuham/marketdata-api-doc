---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/rest-api/Taker-Buy-Sell-Volume
api_type: Market Data
updated_at: 2026-01-15T23:39:24.291968
---

# Taker Buy/Sell Volume

## API Description[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Taker-Buy-Sell-Volume#api-description "Direct link to API Description")

Taker Buy Volume: the total volume of buy orders filled by takers within the period. Taker Sell Volume: the total volume of sell orders filled by takers within the period.

## HTTP Request[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Taker-Buy-Sell-Volume#http-request "Direct link to HTTP Request")

GET `/futures/data/takerBuySellVol`

## Request Weight[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Taker-Buy-Sell-Volume#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Taker-Buy-Sell-Volume#request-parameters "Direct link to Request Parameters")

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


## Response Example[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Taker-Buy-Sell-Volume#response-example "Direct link to Response Example")
    
    
    [    
       {  
    	  "pair": "BTCUSD",  
    	  "contractType": "CURRENT_QUARTER",  
    	  "takerBuyVol": "387",  //unit: cont  
    	  "takerSellVol": "248",  //unit: cont  
    	  "takerBuyVolValue": "2342.1220", //unit: base asset  
    	  "takerSellVolValue": "4213.9800", //unit: base asset  
    	  "timestamp": 1591261042378  
       },  
       {  
         "pair": "BTCUSD",  
    	  "contractType": "CURRENT_QUARTER",  
    	  "takerBuyVol": "234",  //unit: cont  
    	  "takerSellVol": "121",  //unit: cont  
    	  "takerBuyVolValue": "4563.1320", //unit: base asset  
    	  "takerSellVolValue": "3313.3940", //unit: base asset  
    	  "timestamp": 1585615200000  
       }  
    ]

---

# 合约主动买卖量

## 接口描述[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Taker-Buy-Sell-Volume#接口描述 "接口描述的直接链接")

主动买入量：展示单位时间内主动买盘（Taker吃单买入）的成交量。 主动卖出量：展示单位时间内主动卖盘（Taker吃单卖出）的成交量。

## HTTP请求[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Taker-Buy-Sell-Volume#http请求 "HTTP请求的直接链接")

GET `/futures/data/takerBuySellVol`

## 请求权重[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Taker-Buy-Sell-Volume#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Taker-Buy-Sell-Volume#请求参数 "请求参数的直接链接")

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


## 响应示例[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Taker-Buy-Sell-Volume#响应示例 "响应示例的直接链接")
    
    
    [    
       {  
    	  "pair": "BTCUSD",  
    	  "contractType": "CURRENT_QUARTER",  
    	  "takerBuyVol": "387",  //unit: cont  
    	  "takerSellVol": "248",  //unit: cont  
    	  "takerBuyVolValue": "2342.1220", //unit: base asset  
    	  "takerSellVolValue": "4213.9800", //unit: base asset  
    	  "timestamp": 1591261042378  
       },  
       {  
         "pair": "BTCUSD",  
    	  "contractType": "CURRENT_QUARTER",  
    	  "takerBuyVol": "234",  //unit: cont  
    	  "takerSellVol": "121",  //unit: cont  
    	  "takerBuyVolValue": "4563.1320", //unit: base asset  
    	  "takerSellVolValue": "3313.3940", //unit: base asset  
    	  "timestamp": 1585615200000  
       }  
    ]