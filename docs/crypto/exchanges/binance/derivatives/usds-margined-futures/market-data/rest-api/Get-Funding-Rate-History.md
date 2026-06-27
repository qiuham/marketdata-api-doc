---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Get-Funding-Rate-History
api_type: Market Data
updated_at: 2026-01-15T23:46:49.716187
---

# Get Funding Rate History

## API Description[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Get-Funding-Rate-History#api-description "Direct link to API Description")

Get Funding Rate History

## HTTP Request[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Get-Funding-Rate-History#http-request "Direct link to HTTP Request")

GET `/fapi/v1/fundingRate`

## Request Weight[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Get-Funding-Rate-History#request-weight "Direct link to Request Weight")

share 500/5min/IP rate limit with GET /fapi/v1/fundingInfo

## Request Parameters[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Get-Funding-Rate-History#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| NO|   
startTime| LONG| NO| Timestamp in ms to get funding rate from INCLUSIVE.  
endTime| LONG| NO| Timestamp in ms to get funding rate until INCLUSIVE.  
limit| INT| NO| Default 100; max 1000  
  
>   * If `startTime` and `endTime` are not sent, the most recent 200 records are returned.
>   * If the number of data between `startTime` and `endTime` is larger than `limit`, return as `startTime` \+ `limit`.
>   * In ascending order.
> 


## Response Example[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Get-Funding-Rate-History#response-example "Direct link to Response Example")
    
    
    [  
    	{  
        	"symbol": "BTCUSDT",  
        	"fundingRate": "-0.03750000",  
        	"fundingTime": 1570608000000,  
    		"markPrice": "34287.54619963"   // mark price associated with a particular funding fee charge  
    	},  
    	{  
       		"symbol": "BTCUSDT",  
        	"fundingRate": "0.00010000",  
        	"fundingTime": 1570636800000,  
    		"markPrice": "34287.54619963"   
    	}  
    ]

---

# 查询资金费率历史

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Get-Funding-Rate-History#接口描述 "接口描述的直接链接")

查询资金费率历史

## HTTP请求[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Get-Funding-Rate-History#http请求 "HTTP请求的直接链接")

GET `/fapi/v1/fundingRate`

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Get-Funding-Rate-History#请求权重 "请求权重的直接链接")

和GET /fapi/v1/fundingInfo共享500/5min/IP

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Get-Funding-Rate-History#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| NO| 交易对  
startTime| LONG| NO| 起始时间  
endTime| LONG| NO| 结束时间  
limit| INT| NO| 默认值:100 最大值:1000  
  
>   * 如果 `startTime` 和 `endTime` 都未发送, 返回最近200条数据.
>   * 如果 `startTime` 和 `endTime` 之间的数据量大于 `limit`, 返回 `startTime` \+ `limit`情况下的数据。
> 


## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Get-Funding-Rate-History#响应示例 "响应示例的直接链接")
    
    
    [  
    	{  
        	"symbol": "BTCUSDT",			// 交易对  
        	"fundingRate": "-0.03750000",	// 资金费率  
        	"fundingTime": 1570608000000,	// 资金费时间  
            "markPrice": "34287.54619963"   // 资金费对应标记价格  
    	},  
    	{  
       		"symbol": "BTCUSDT",  
        	"fundingRate": "0.00010000",  
        	"fundingTime": 1570636800000,  
            "markPrice": "34287.54619963"   // 资金费对应标记价格  
    	}  
    ]