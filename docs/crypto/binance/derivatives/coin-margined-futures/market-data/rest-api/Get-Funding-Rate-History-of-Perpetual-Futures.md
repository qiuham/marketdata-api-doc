---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/rest-api/Get-Funding-Rate-History-of-Perpetual-Futures
api_type: Market Data
updated_at: 2026-01-15T23:38:10.468786
---

# Get Funding Rate History of Perpetual Futures

## API Description[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Get-Funding-Rate-History-of-Perpetual-Futures#api-description "Direct link to API Description")

Get Funding Rate History of Perpetual Futures

## HTTP Request[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Get-Funding-Rate-History-of-Perpetual-Futures#http-request "Direct link to HTTP Request")

GET `/dapi/v1/fundingRate`

## Request Weight[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Get-Funding-Rate-History-of-Perpetual-Futures#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Get-Funding-Rate-History-of-Perpetual-Futures#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
startTime| LONG| NO| Timestamp in ms to get funding rate from INCLUSIVE.  
endTime| LONG| NO| Timestamp in ms to get funding rate until INCLUSIVE.  
limit| INT| NO| Default 100; max 1000  
  
>   * empty array will be returned for delivery symbols.
> 


## Response Example[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Get-Funding-Rate-History-of-Perpetual-Futures#response-example "Direct link to Response Example")
    
    
    [  
    	{  
    		"symbol": "BTCUSD_PERP",  
      		"fundingTime": 1596038400000,	  
      		"fundingRate": "-0.00300000"  
      	},  
     	{  
     		"symbol": "BTCUSD_PERP",  
      		"fundingTime": 1596067200000,  
      		"fundingRate": "-0.00300000"  
      	}  
    ]

---

# 查询永续合约资金费率历史

## 接口描述[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Get-Funding-Rate-History-of-Perpetual-Futures#接口描述 "接口描述的直接链接")

查询永续合约资金费率历史

## HTTP请求[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Get-Funding-Rate-History-of-Perpetual-Futures#http请求 "HTTP请求的直接链接")

GET `/dapi/v1/fundingRate`

## 请求权重[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Get-Funding-Rate-History-of-Perpetual-Futures#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Get-Funding-Rate-History-of-Perpetual-Futures#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES| 交易对  
startTime| LONG| NO| 起始时间  
endTime| LONG| NO| 结束时间  
limit| INT| NO| 默认值:100 最大值:1000  
  
>   * 对非永续合约，将返回空列表
> 


## 响应示例[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Get-Funding-Rate-History-of-Perpetual-Futures#响应示例 "响应示例的直接链接")
    
    
    [  
    	{  
    		"symbol": "BTCUSD_PERP",	// 交易对  
      		"fundingTime": 1596038400000,	// 资金费时间  
      		"fundingRate": "-0.00300000"	// 资金费率  
      	},  
     	{  
     		"symbol": "BTCUSD_PERP",  
      		"fundingTime": 1596067200000,  
      		"fundingRate": "-0.00300000"  
      	}  
    ]