---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Mark-Price
api_type: Market Data
updated_at: 2026-01-15T23:46:53.376752
---

# Mark Price

## API Description[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Mark-Price#api-description "Direct link to API Description")

Mark Price and Funding Rate

## HTTP Request[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Mark-Price#http-request "Direct link to HTTP Request")

GET `/fapi/v1/premiumIndex`

## Request Weight[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Mark-Price#request-weight "Direct link to Request Weight")

**1** with symbol, **10**  without symbol

## Request Parameters[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Mark-Price#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| NO|   
  
## Response Example[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Mark-Price#response-example "Direct link to Response Example")

> **Response:**
    
    
    {  
    	"symbol": "BTCUSDT",  
    	"markPrice": "11793.63104562",	// mark price  
    	"indexPrice": "11781.80495970",	// index price  
    	"estimatedSettlePrice": "11781.16138815", // Estimated Settle Price, only useful in the last hour before the settlement starts.  
    	"lastFundingRate": "0.00038246",  // This is the Latest funding rate  
    	"interestRate": "0.00010000",  
    	"nextFundingTime": 1597392000000,  
    	"time": 1597370495002  
    }  
    

> **OR (when symbol not sent)**
    
    
    [  
    	{  
    	    "symbol": "BTCUSDT",  
    	    "markPrice": "11793.63104562",	// mark price  
    	    "indexPrice": "11781.80495970",	// index price  
    	    "estimatedSettlePrice": "11781.16138815", // Estimated Settle Price, only useful in the last hour before the settlement starts.  
    	    "lastFundingRate": "0.00038246",  // This is the Latest funding rate  
    	    "interestRate": "0.00010000",  
    	    "nextFundingTime": 1597392000000,  
    	    "time": 1597370495002  
    	}  
    ]

---

# 最新标记价格和资金费率

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Mark-Price#接口描述 "接口描述的直接链接")

采集各大交易所数据加权平均

## HTTP请求[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Mark-Price#http请求 "HTTP请求的直接链接")

GET `/fapi/v1/premiumIndex`

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Mark-Price#请求权重 "请求权重的直接链接")

带symbol **1** , 不带symbol **10**

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Mark-Price#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| NO| 交易对  
  
## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Mark-Price#响应示例 "响应示例的直接链接")

> **响应:**
    
    
    {  
        "symbol": "BTCUSDT",				// 交易对  
        "markPrice": "11793.63104562",		// 标记价格  
        "indexPrice": "11781.80495970",		// 指数价格  
        "estimatedSettlePrice": "11781.16138815",  // 预估结算价,仅在交割开始前最后一小时有意义  
        "lastFundingRate": "0.00038246",	// 最近更新的资金费率  
        "interestRate": "0.00010000",		// 标的资产基础利率  
        "nextFundingTime": 1597392000000,	// 下次资金费时间  
        "time": 1597370495002				// 更新时间  
    }  
    

> **当不指定symbol时相应**
    
    
    [  
    	{  
        	"symbol": "BTCUSDT",			// 交易对  
        	"markPrice": "11793.63104562",	// 标记价格  
        	"indexPrice": "11781.80495970",	// 指数价格  
        	"estimatedSettlePrice": "11781.16138815",  // 预估结算价,仅在交割开始前最后一小时有意义  
        	"lastFundingRate": "0.00038246",	// 最近更新的资金费率  
        	"interestRate": "0.00010000",		// 标的资产基础利率  
        	"nextFundingTime": 1597392000000,	// 下次资金费时间  
        	"time": 1597370495002				// 更新时间  
    	}  
    ]