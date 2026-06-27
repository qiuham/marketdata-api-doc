---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/rest-api/Exchange-Information
api_type: Market Data
updated_at: 2026-01-15T23:38:04.623248
---

# Exchange Information

## API Description[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Exchange-Information#api-description "Direct link to API Description")

Current exchange trading rules and symbol information

## HTTP Request[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Exchange-Information#http-request "Direct link to HTTP Request")

GET `/dapi/v1/exchangeInfo`

## Request Weight[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Exchange-Information#request-weight "Direct link to Request Weight")

1

## Request Parameters[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Exchange-Information#request-parameters "Direct link to Request Parameters")

NONE

## Response Example[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Exchange-Information#response-example "Direct link to Response Example")
    
    
    {  
    	"exchangeFilters": [],  
     	"rateLimits": [   
     		{  
     			"interval": "MINUTE",   
       			"intervalNum": 1,   
       			"limit": 6000,   
       			"rateLimitType": "REQUEST_WEIGHT"   
       		},  
      		{  
      			"interval": "MINUTE",  
       			"intervalNum": 1,  
       			"limit": 6000,  
       			"rateLimitType": "ORDERS"  
       		}  
       	],  
     	"serverTime": 1565613908500, // Ignore please. If you want to check current server time, please check via "GET /dapi/v1/time"  
     	"symbols": [ // contract symbols  
     		{  
     			"filters": [  
     				{  
     					"filterType": "PRICE_FILTER",   
         				"maxPrice": "100000",   
         				"minPrice": "0.1",   
         				"tickSize": "0.1"   
         			},  
        			{  
        				"filterType": "LOT_SIZE",   
         				"maxQty": "100000",   
         				"minQty": "1",   
         				"stepSize": "1"   
         			},  
        			{  
        				"filterType": "MARKET_LOT_SIZE",   
         				"maxQty": "100000",   
         				"minQty": "1",   
         				"stepSize": "1"   
         			},  
         			{  
        				"filterType": "MAX_NUM_ORDERS",   
        				"limit": 200  
      				},  
      				{  
        				"filterType": "PERCENT_PRICE",   
        				"multiplierUp": "1.0500",   
        				"multiplierDown": "0.9500",   
        				"multiplierDecimal": "4"  
      				}  
        		],  
       			"OrderType": [   
       				"LIMIT",   
       				"MARKET",   
       				"STOP",  
       				"TAKE_PROFIT",  
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
       			"symbol": "BTCUSD_200925", // contract symbol name  
       			"pair": "BTCUSD",  // underlying symbol  
       			"contractType": "CURRENT_QUARTER",   
       			"deliveryDate": 1601020800000,  
       			"onboardDate": 1590739200000,  
       			"contractStatus": "TRADING",   
       			"contractSize": 100,      
       			"quoteAsset": "USD",  
       			"baseAsset": "BTC",     
       			"marginAsset": "BTC",  
       			"pricePrecision": 1,	// please do not use it as tickSize  
    		   	"quantityPrecision": 0,	// please do not use it as stepSize  
    		   	"baseAssetPrecision": 8,  
    		   	"quotePrecision": 8,  
    		   	"equalQtyPrecision": 4,	 // ignore  
    		   	"triggerProtect": "0.0500",	// threshold for algo order with "priceProtect"  
    		   	"maintMarginPercent": "2.5000",  // ignore  
    		   	"requiredMarginPercent": "5.0000",  // ignore  
    		   	"underlyingType": "COIN",   
    		   	"underlyingSubType": []	  
       		}  
       	],  
    	"timezone": "UTC"  
    }

---

# 获取交易规则和交易对

## 接口描述[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Exchange-Information#接口描述 "接口描述的直接链接")

获取交易规则和交易对

## HTTP请求[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Exchange-Information#http请求 "HTTP请求的直接链接")

GET `/dapi/v1/exchangeInfo`

## 请求权重[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Exchange-Information#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Exchange-Information#请求参数 "请求参数的直接链接")

NONE

## 响应示例[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Exchange-Information#响应示例 "响应示例的直接链接")
    
    
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
     	"serverTime": 1565613908500, // 请忽略。如果需要获取系统时间，请查询接口 “GET /dapi/v1/time”  
     	"symbols": [ // 交易对信息  
     		{  
     			"filters": [  
     				{  
     					"filterType": "PRICE_FILTER", // 价格限制  
         				"maxPrice": "100000", // 价格上限, 最大价格  
         				"minPrice": "0.1", // 价格下限, 最小价格  
         				"tickSize": "0.1" // 下单最小价格间隔  
         			},  
        			{  
        				"filterType": "LOT_SIZE", // 数量限制  
         				"maxQty": "100000", // 数量上限, 最大数量  
         				"minQty": "1", // 数量下限, 最小数量  
         				"stepSize": "1" // 下单最小数量间隔  
         			},  
        			{  
        				"filterType": "MARKET_LOT_SIZE", // 市价订单数量限制  
         				"maxQty": "100000", // 数量上限, 最大数量  
         				"minQty": "1", // 数量下限, 最小数量  
         				"stepSize": "1" // 允许的步进值  
         			},  
         			{  
        				"filterType": "MAX_NUM_ORDERS", // 最多挂单数限制  
        				"limit": 200  
      				},  
      				{  
        				"filterType": "PERCENT_PRICE", // 价格比限制  
        				"multiplierUp": "1.0500", // 价格上限百分比  
        				"multiplierDown": "0.9500", // 价格下限百分比  
        				"multiplierDecimal": 4  
      				}  
        		],  
       			"OrderType": [ // 订单类型  
       				"LIMIT",  // 限价单  
       				"MARKET",  // 市价单  
       				"STOP", // 止损单  
       				"TAKE_PROFIT", // 止盈单  
       				"TRAILING_STOP_MARKET" // 跟踪止损单  
       			],  
       			"timeInForce": [ // 有效方式  
       				"GTC", // 成交为止, 一直有效  
       				"IOC", // 无法立即成交(吃单)的部分就撤销  
       				"FOK", // 无法全部立即成交就撤销  
       				"GTX" // 无法成为挂单方就撤销  
       			],  
       			"liquidationFee": "0.010000",	// 强平费率  
       			"marketTakeBound": "0.30",	// 市价吃单(相对于标记价格)允许可造成的最大价格偏离比例  
       			"symbol": "BTCUSD_200925", // 交易对  
       			"pair": "BTCUSD",	// 标的交易对  
       			"contractType": "CURRENT_QUARTER",   // 合约类型  
       			"deliveryDate": 1601020800000,  
       			"onboardDate": 1590739200000,  
       			"contractStatus": "TRADING", // 交易对状态  
       			"contractSize": 100,     //  
       			"quoteAsset": "USD", // 报价币种  
       			"baseAsset": "BTC",  // 标的物  
       			"marginAsset": "BTC",	// 保证金币种  
       			"pricePrecision": 1,   // 价格小数点位数(仅作为系统精度使用，注意同tickSize 区分)  
       			"quantityPrecision": 0, // 数量小数点位数(仅作为系统精度使用，注意同stepSize 区分)  
    		 	"baseAssetPrecision": 8,  
    		   	"quotePrecision": 8,  
    		   	"equalQtyPrecision": 4,		// 请忽略  
    		   	"triggerProtect": "0.0500",	// 开启"priceProtect"的条件订单的触发阈值  
    		   	"maintMarginPercent": "2.5000", // 请忽略  
    		   	"requiredMarginPercent": "5.0000", // 请忽略  
    		   	"underlyingType": "COIN",  // 标的类型  
    		   	"underlyingSubType": []		// 标的物子类型  
       		}  
       	],  
    	"timezone": "UTC" // 服务器所用的时间区域  
    }