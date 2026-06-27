---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/rest-api/Index-Price-and-Mark-Price
api_type: Market Data
updated_at: 2026-01-15T23:38:10.661241
---

# Index Price and Mark Price

## API Description[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Index-Price-and-Mark-Price#api-description "Direct link to API Description")

Query index price and mark price

## HTTP Request[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Index-Price-and-Mark-Price#http-request "Direct link to HTTP Request")

GET `/dapi/v1/premiumIndex`

## Request Weight[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Index-Price-and-Mark-Price#request-weight "Direct link to Request Weight")

**10**

## Request Parameters[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Index-Price-and-Mark-Price#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| NO|   
pair| STRING| NO|   
  
## Response Example[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Index-Price-and-Mark-Price#response-example "Direct link to Response Example")

> with symbol
    
    
    [  
    	{  
    		"symbol": "BTCUSD_PERP",  
      		"pair": "BTCUSD",  
      		"markPrice": "11029.69574559",	// mark price  
      		"indexPrice": "10979.14437500",	// index price  
      		"estimatedSettlePrice": "10981.74168236",  // Estimated Settle Price, only useful in the last hour before the settlement starts.  
      		"lastFundingRate": "0.00071003",	 // the lasted funding rate, for perpetual contract symbols only. For delivery symbols, "" will be shown.  
      		"interestRate": "0.00010000",		// the base asset interest rate, for perpetual contract symbols only. For delivery symbols, "" will be shown.  
      		"nextFundingTime": 1596096000000,	 // For perpetual contract symbols only. For delivery symbols, 0 will be shown  
      		"time": 1596094042000  
      	},  
     	{  
     		"symbol": "BTCUSD_200925",	  
     		"pair": "BTCUSD",  
      		"markPrice": "12077.01343750",  
      		"indexPrice": "10979.10312500",  
      		"estimatedSettlePrice": "10981.74168236",  
      		"lastFundingRate": "",  
      		"interestRate": "",	  
      		"nextFundingTime": 0,  
      		"time": 1596094042000  
      	}  
    ]

---

# 最新现货指数价格和Mark Price

## 接口描述[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Index-Price-and-Mark-Price#接口描述 "接口描述的直接链接")

查询最新现货指数价格和Mark Price

## HTTP请求[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Index-Price-and-Mark-Price#http请求 "HTTP请求的直接链接")

GET `/dapi/v1/premiumIndex`

## 请求权重[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Index-Price-and-Mark-Price#请求权重 "请求权重的直接链接")

10

## 请求参数[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Index-Price-and-Mark-Price#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| NO| 交易对  
pair| STRING| NO| 标的交易对  
  
## 响应示例[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Index-Price-and-Mark-Price#响应示例 "响应示例的直接链接")
    
    
    [  
    	{  
    		"symbol": "BTCUSD_PERP",	// 交易对  
      		"pair": "BTCUSD",			// 基础标的  
      		"markPrice": "11029.69574559",	// 标记价格  
      		"indexPrice": "10979.14437500",	// 指数价格  
      		"estimatedSettlePrice": "10981.74168236",  // 预估结算价,仅在交割开始前最后一小时有意义  
      		"lastFundingRate": "0.00071003",	  // 最近更新的资金费率,只对永续合约有效，其他合约返回""  
      		"interestRate": "0.00010000",		// 标的资产基础利率,只对永续合约有效，其他合约返回""  
      		"nextFundingTime": 1596096000000,	 // 下次资金费时间，只对永续合约有效，其他合约返回0  
      		"time": 1596094042000	// 更新时间  
      	},  
     	{  
     		"symbol": "BTCUSD_200925",	  
     		"pair": "BTCUSD",  
      		"markPrice": "12077.01343750",  
      		"indexPrice": "10979.10312500",  
      		"estimatedSettlePrice": "10981.74168236",  
      		"lastFundingRate": "",  
      		"interestRate": "",  
      		"nextFundingTime": 0,  
      		"time": 1596094042000  
      	}  
    ]