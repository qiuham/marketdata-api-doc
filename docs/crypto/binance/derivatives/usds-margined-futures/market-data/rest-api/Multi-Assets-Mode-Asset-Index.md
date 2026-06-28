---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Multi-Assets-Mode-Asset-Index
api_type: Market Data
updated_at: 2026-01-15T23:46:53.502174
---

# Multi-Assets Mode Asset Index

## API Description[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Multi-Assets-Mode-Asset-Index#api-description "Direct link to API Description")

asset index for Multi-Assets mode

## HTTP Request[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Multi-Assets-Mode-Asset-Index#http-request "Direct link to HTTP Request")

GET `/fapi/v1/assetIndex`

## Request Weight[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Multi-Assets-Mode-Asset-Index#request-weight "Direct link to Request Weight")

**1** for a single symbol; **10** when the symbol parameter is omitted

## Request Parameters[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Multi-Assets-Mode-Asset-Index#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| NO| Asset pair  
  
## Response Example[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Multi-Assets-Mode-Asset-Index#response-example "Direct link to Response Example")

> **Response:**
    
    
    {  
    	"symbol": "ADAUSD",  
    	"time": 1635740268004,  
    	"index": "1.92957370",  
    	"bidBuffer": "0.10000000",   
    	"askBuffer": "0.10000000",   
    	"bidRate": "1.73661633",  
    	"askRate": "2.12253107",  
    	"autoExchangeBidBuffer": "0.05000000",  
    	"autoExchangeAskBuffer": "0.05000000",  
    	"autoExchangeBidRate": "1.83309501",  
    	"autoExchangeAskRate": "2.02605238"  
    }  
    

> Or(without symbol)
    
    
    [  
    	{  
    		"symbol": "ADAUSD",  
    		"time": 1635740268004,  
    		"index": "1.92957370",  
    		"bidBuffer": "0.10000000",   
    		"askBuffer": "0.10000000",   
    		"bidRate": "1.73661633",  
    		"askRate": "2.12253107",  
    		"autoExchangeBidBuffer": "0.05000000",  
    		"autoExchangeAskBuffer": "0.05000000",  
    		"autoExchangeBidRate": "1.83309501",  
    		"autoExchangeAskRate": "2.02605238"  
    	}  
    ]

---

# 多资产模式资产汇率指数

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Multi-Assets-Mode-Asset-Index#接口描述 "接口描述的直接链接")

多资产模式资产汇率指数

## HTTP请求[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Multi-Assets-Mode-Asset-Index#http请求 "HTTP请求的直接链接")

GET `/fapi/v1/assetIndex`

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Multi-Assets-Mode-Asset-Index#请求权重 "请求权重的直接链接")

**1** for a single symbol; **10** when the symbol parameter is omitted

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Multi-Assets-Mode-Asset-Index#请求参数 "请求参数的直接链接")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| NO| Asset pair  
  
## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Multi-Assets-Mode-Asset-Index#响应示例 "响应示例的直接链接")
    
    
    {  
    	"symbol": "ADAUSD",  
    	"time": 1635740268004,  
    	"index": "1.92957370",  
    	"bidBuffer": "0.10000000",   
    	"askBuffer": "0.10000000",   
    	"bidRate": "1.73661633",  
    	"askRate": "2.12253107",  
    	"autoExchangeBidBuffer": "0.05000000",  
    	"autoExchangeAskBuffer": "0.05000000",  
    	"autoExchangeBidRate": "1.83309501",  
    	"autoExchangeAskRate": "2.02605238"  
    }  
    

> 或(当不发送交易对信息)
    
    
    [  
    	{  
    		"symbol": "ADAUSD",  
    		"time": 1635740268004,  
    		"index": "1.92957370",  
    		"bidBuffer": "0.10000000",   
    		"askBuffer": "0.10000000",   
    		"bidRate": "1.73661633",  
    		"askRate": "2.12253107",  
    		"autoExchangeBidBuffer": "0.05000000",  
    		"autoExchangeAskBuffer": "0.05000000",  
    		"autoExchangeBidRate": "1.83309501",  
    		"autoExchangeAskRate": "2.02605238"  
    	}  
    ]