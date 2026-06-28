---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Composite-Index-Symbol-Information
api_type: Market Data
updated_at: 2026-01-15T23:46:42.860314
---

# Composite Index Symbol Information

## API Description[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Composite-Index-Symbol-Information#api-description "Direct link to API Description")

Query composite index symbol information

## HTTP Request[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Composite-Index-Symbol-Information#http-request "Direct link to HTTP Request")

GET `/fapi/v1/indexInfo`

## Request Weight[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Composite-Index-Symbol-Information#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Composite-Index-Symbol-Information#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| NO|   
  
>   * Only for composite index symbols
> 


## Response Example[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Composite-Index-Symbol-Information#response-example "Direct link to Response Example")
    
    
    [  
    	{   
    		"symbol": "DEFIUSDT",  
    		"time": 1589437530011,    // Current time  
    		"component": "baseAsset", //Component asset  
    		"baseAssetList":[  
    			{  
    				"baseAsset":"BAL",  
    				"quoteAsset": "USDT",  
    				"weightInQuantity":"1.04406228",  
    				"weightInPercentage":"0.02783900"  
    			},  
    			{  
    				"baseAsset":"BAND",  
    				"quoteAsset": "USDT",  
    				"weightInQuantity":"3.53782729",  
    				"weightInPercentage":"0.03935200"  
    			}  
    		]  
    	}  
    ]

---

# 综合指数交易对信息

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Composite-Index-Symbol-Information#接口描述 "接口描述的直接链接")

获取交易对为综合指数的基础成分信息。

## HTTP请求[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Composite-Index-Symbol-Information#http请求 "HTTP请求的直接链接")

GET `/fapi/v1/indexInfo`

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Composite-Index-Symbol-Information#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Composite-Index-Symbol-Information#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| NO|   
  
## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Composite-Index-Symbol-Information#响应示例 "响应示例的直接链接")
    
    
    [  
    	{   
    		"symbol": "DEFIUSDT",  
    		"time": 1589437530011,    // 请求时间  
    		"component": "baseAsset", //成分资产  
    		"baseAssetList":[  
    			{  
    				"baseAsset":"BAL",	  // 基础资产  
    				"quoteAsset": "USDT", // 报价资产  
    				"weightInQuantity":"1.04406228",  //权重(数量)  
    				"weightInPercentage":"0.02783900" //权重(比例)  
    			},  
    			{  
    				"baseAsset":"BAND",  
    				"quoteAsset": "USDT",   
    				"weightInQuantity":"3.53782729",  
    				"weightInPercentage":"0.03935200"  
    			}  
    		]  
    	}  
    ]