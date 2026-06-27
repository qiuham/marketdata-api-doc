---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Exchange-Information
api_type: Market Data
updated_at: 2026-01-15T23:46:46.142286
---

# Exchange Information

## API Description[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Exchange-Information#api-description "Direct link to API Description")

Current exchange trading rules and symbol information

## HTTP Request[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Exchange-Information#http-request "Direct link to HTTP Request")

GET `/fapi/v1/exchangeInfo`

## Request Weight[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Exchange-Information#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Exchange-Information#request-parameters "Direct link to Request Parameters")

NONE

## Response Example[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Exchange-Information#response-example "Direct link to Response Example")
    
    
    {  
    	"exchangeFilters": [],  
     	"rateLimits": [  
     		{  
     			"interval": "MINUTE",  
       			"intervalNum": 1,  
       			"limit": 2400,  
       			"rateLimitType": "REQUEST_WEIGHT"   
       		},  
      		{  
      			"interval": "MINUTE",  
       			"intervalNum": 1,  
       			"limit": 1200,  
       			"rateLimitType": "ORDERS"  
       		}  
       	],  
     	"serverTime": 1565613908500,    // Ignore please. If you want to check current server time, please check via "GET /fapi/v1/time"  
     	"assets": [ // assets information  
     		{  
     			"asset": "BTC",  
       			"marginAvailable": true, // whether the asset can be used as margin in Multi-Assets mode  
       			"autoAssetExchange": "-0.10" // auto-exchange threshold in Multi-Assets margin mode  
       		},  
     		{  
     			"asset": "USDT",  
       			"marginAvailable": true,  
       			"autoAssetExchange": "0"  
       		},  
     		{  
     			"asset": "BNB",  
       			"marginAvailable": false,  
       			"autoAssetExchange": null  
       		}  
       	],  
     	"symbols": [  
     		{  
     			"symbol": "BLZUSDT",  
     			"pair": "BLZUSDT",  
     			"contractType": "PERPETUAL",  
     			"deliveryDate": 4133404800000,  
     			"onboardDate": 1598252400000,  
     			"status": "TRADING",  
     			"maintMarginPercent": "2.5000",   // ignore  
     			"requiredMarginPercent": "5.0000",  // ignore  
     			"baseAsset": "BLZ",   
     			"quoteAsset": "USDT",  
     			"marginAsset": "USDT",  
     			"pricePrecision": 5,	// please do not use it as tickSize  
     			"quantityPrecision": 0, // please do not use it as stepSize  
     			"baseAssetPrecision": 8,  
     			"quotePrecision": 8,   
     			"underlyingType": "COIN",  
     			"underlyingSubType": ["STORAGE"],  
     			"settlePlan": 0,  
     			"triggerProtect": "0.15", // threshold for algo order with "priceProtect"  
     			"filters": [  
     				{  
     					"filterType": "PRICE_FILTER",  
         				"maxPrice": "300",  
         				"minPrice": "0.0001",   
         				"tickSize": "0.0001"  
         			},  
        			{  
        				"filterType": "LOT_SIZE",   
         				"maxQty": "10000000",  
         				"minQty": "1",  
         				"stepSize": "1"  
         			},  
        			{  
        				"filterType": "MARKET_LOT_SIZE",  
         				"maxQty": "590119",  
         				"minQty": "1",  
         				"stepSize": "1"  
         			},  
         			{  
        				"filterType": "MAX_NUM_ORDERS",  
        				"limit": 200  
      				},  
      				{  
      					"filterType": "MIN_NOTIONAL",  
      					"notional": "5.0",   
      				},  
      				{  
        				"filterType": "PERCENT_PRICE",  
        				"multiplierUp": "1.1500",  
        				"multiplierDown": "0.8500",  
        				"multiplierDecimal": "4"  
        			}  
       			],  
     			"OrderType": [  
       				"LIMIT",  
       				"MARKET",  
       				"STOP",  
       				"STOP_MARKET",  
       				"TAKE_PROFIT",  
       				"TAKE_PROFIT_MARKET",  
       				"TRAILING_STOP_MARKET"   
       			],  
       			"timeInForce": [  
       				"GTC",   
       				"IOC",   
       				"FOK",   
       				"GTX"   
     			],  
     			"liquidationFee": "0.010000",	// liquidation fee rate  
       			"marketTakeBound": "0.30",	// the max price difference rate( from mark price) a market order can make  
     		}  
       	],  
    	"timezone": "UTC"   
    }

---

# 获取交易规则和交易对

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Exchange-Information#接口描述 "接口描述的直接链接")

获取交易规则和交易对

## HTTP请求[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Exchange-Information#http请求 "HTTP请求的直接链接")

GET `/fapi/v1/exchangeInfo`

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Exchange-Information#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Exchange-Information#请求参数 "请求参数的直接链接")

NONE

## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Exchange-Information#响应示例 "响应示例的直接链接")
    
    
    {  
    	"exchangeFilters": [],  
     	"rateLimits": [ // API访问的限制  
     		{  
     			"interval": "MINUTE", // 按照分钟计算  
       			"intervalNum": 1, // 按照1分钟计算  
       			"limit": 2400, // 上限次数  
       			"rateLimitType": "REQUEST_WEIGHT" // 按照访问权重来计算  
       		},  
      		{  
      			"interval": "MINUTE",  
       			"intervalNum": 1,  
       			"limit": 1200,  
       			"rateLimitType": "ORDERS" // 按照订单数量来计算  
       		}  
       	],  
     	"serverTime": 1565613908500, // 请忽略。如果需要获取当前系统时间，请查询接口 “GET /fapi/v1/time”  
     	"assets": [ // 资产信息  
     		{  
     			"asset": "BTC",  
       			"marginAvailable": true, // 是否可用作保证金  
       			"autoAssetExchange": "-0.10" // 保证金资产自动兑换阈值  
       		},  
     		{  
     			"asset": "USDT",  
       			"marginAvailable": true, // 是否可用作保证金  
       			"autoAssetExchange": "0" // 保证金资产自动兑换阈值  
       		},  
     		{  
     			"asset": "BNB",  
       			"marginAvailable": false, // 是否可用作保证金  
       			"autoAssetExchange": null // 保证金资产自动兑换阈值  
       		}  
       	],  
     	"symbols": [ // 交易对信息  
     		{  
     			"symbol": "BLZUSDT",  // 交易对  
     			"pair": "BLZUSDT",  // 标的交易对  
     			"contractType": "PERPETUAL",	// 合约类型  
     			"deliveryDate": 4133404800000,  // 交割日期  
     			"onboardDate": 1598252400000,	  // 上线日期  
     			"status": "TRADING",  // 交易对状态  
     			"maintMarginPercent": "2.5000",  // 请忽略  
     			"requiredMarginPercent": "5.0000", // 请忽略  
     			"baseAsset": "BLZ",  // 标的资产  
     			"quoteAsset": "USDT", // 报价资产  
     			"marginAsset": "USDT", // 保证金资产  
     			"pricePrecision": 5,  // 价格小数点位数(仅作为系统精度使用，注意同tickSize 区分）  
     			"quantityPrecision": 0,  // 数量小数点位数(仅作为系统精度使用，注意同stepSize 区分）  
     			"baseAssetPrecision": 8,  // 标的资产精度  
     			"quotePrecision": 8,  // 报价资产精度  
     			"underlyingType": "COIN",  
     			"underlyingSubType": ["STORAGE"],  
     			"settlePlan": 0,  
     			"triggerProtect": "0.15", // 开启"priceProtect"的条件订单的触发阈值  
     			"filters": [  
     				{  
     					"filterType": "PRICE_FILTER", // 价格限制  
         				"maxPrice": "300", // 价格上限, 最大价格  
         				"minPrice": "0.0001", // 价格下限, 最小价格  
         				"tickSize": "0.0001" // 订单最小价格间隔  
         			},  
        			{  
        				"filterType": "LOT_SIZE", // 数量限制  
         				"maxQty": "10000000", // 数量上限, 最大数量  
         				"minQty": "1", // 数量下限, 最小数量  
         				"stepSize": "1" // 订单最小数量间隔  
         			},  
        			{  
        				"filterType": "MARKET_LOT_SIZE", // 市价订单数量限制  
         				"maxQty": "590119", // 数量上限, 最大数量  
         				"minQty": "1", // 数量下限, 最小数量  
         				"stepSize": "1" // 允许的步进值  
         			},  
         			{  
        				"filterType": "MAX_NUM_ORDERS", // 最多订单数限制  
        				"limit": 200  
      				},  
      				{  
      					"filterType": "MIN_NOTIONAL",  // 最小名义价值  
      					"notional": "5.0",   
      				},  
      				{  
        				"filterType": "PERCENT_PRICE", // 价格比限制  
        				"multiplierUp": "1.1500", // 价格上限百分比  
        				"multiplierDown": "0.8500", // 价格下限百分比  
        				"multiplierDecimal": "4"  
        			}  
       			],  
     			"OrderType": [ // 订单类型  
       				"LIMIT",  // 限价单  
       				"MARKET",  // 市价单  
       				"STOP", // 止损单  
       				"STOP_MARKET", // 止损市价单  
       				"TAKE_PROFIT", // 止盈单  
       				"TAKE_PROFIT_MARKET", // 止盈暑市价单  
       				"TRAILING_STOP_MARKET" // 跟踪止损市价单  
       			],  
       			"timeInForce": [ // 有效方式  
       				"GTC", // 成交为止, 一直有效  
       				"IOC", // 无法立即成交(吃单)的部分就撤销  
       				"FOK", // 无法全部立即成交就撤销  
       				"GTX" // 无法成为挂单方就撤销  
     			],  
     			"liquidationFee": "0.010000",	// 强平费率  
       			"marketTakeBound": "0.30",	// 市价吃单(相对于标记价格)允许可造成的最大价格偏离比例  
     		}  
       	],  
    	"timezone": "UTC" // 服务器所用的时间区域  
    }