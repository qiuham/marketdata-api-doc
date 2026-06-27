---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/options-trading/market-data/Recent-Block-Trade-List
api_type: Market Data
updated_at: 2026-01-15T23:41:10.280243
---

# Recent Block Trades List

## API Description[​](/docs/derivatives/options-trading/market-data/Recent-Block-Trade-List#api-description "Direct link to API Description")

Get recent block trades

## HTTP Request[​](/docs/derivatives/options-trading/market-data/Recent-Block-Trade-List#http-request "Direct link to HTTP Request")

GET `/eapi/v1/blockTrades`

## Request Weight[​](/docs/derivatives/options-trading/market-data/Recent-Block-Trade-List#request-weight "Direct link to Request Weight")

**5**

## Request Parameters[​](/docs/derivatives/options-trading/market-data/Recent-Block-Trade-List#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory|  Description  
---|---|---|---  
symbol| STRING| NO| Option trading pair, e.g. BTC-200730-9000-C  
limit| INT| NO| Number of records; Default: 100 and Max: 500  
  
## Response Example[​](/docs/derivatives/options-trading/market-data/Recent-Block-Trade-List#response-example "Direct link to Response Example")
    
    
    [  
    	{  
    		"id": 1125899906901081078,  
    		"tradeId": 389,  
    		"symbol": "ETH-250725-1200-P",  
    		"price": "342.40",  
    		"qty": "-2167.20",  
    		"quoteQty": "-4.90",  
    		"side": -1,  
    		"time": 1733950676483  
    	},  
    	{  
    		"id": 1125899906901080972,  
    		"tradeId": 161,  
    		"symbol": "XRP-250904-0.086-P",  
    		"price": "3.0",  
    		"qty": "-6.0",  
    		"quoteQty": "-2.02",  
    		"side": -1,  
    		"time": 1733950488444  
    	}  
    ]

---

# 大宗交易历史

## 接口描述[​](/docs/zh-CN/derivatives/options-trading/market-data/Recent-Block-Trade-List#接口描述 "接口描述的直接链接")

查询最近的大宗交易历史

## HTTP请求[​](/docs/zh-CN/derivatives/options-trading/market-data/Recent-Block-Trade-List#http请求 "HTTP请求的直接链接")

GET `/eapi/v1/blockTrades`

## 请求权重[​](/docs/zh-CN/derivatives/options-trading/market-data/Recent-Block-Trade-List#�请求权重 "请求权重的直接链接")

**5**

## 请求参数[​](/docs/zh-CN/derivatives/options-trading/market-data/Recent-Block-Trade-List#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| NO| 交易对，如 BTC-200730-9000-C  
limit| INT| NO| 查询数量，默认100最大500  
  
## 响应示例[​](/docs/zh-CN/derivatives/options-trading/market-data/Recent-Block-Trade-List#响应示例 "响应示例的直接链接")
    
    
    [  
    	{  
    		"id": 1125899906901081078,  
    		"tradeId": 389,  
    		"symbol": "ETH-250725-1200-P",  
    		"price": "342.40",  
    		"qty": "-2167.20",  
    		"quoteQty": "-4.90",  
    		"side": -1,  
    		"time": 1733950676483  
    	},  
    	{  
    		"id": 1125899906901080972,  
    		"tradeId": 161,  
    		"symbol": "XRP-250904-0.086-P",  
    		"price": "3.0",  
    		"qty": "-6.0",  
    		"quoteQty": "-2.02",  
    		"side": -1,  
    		"time": 1733950488444  
    	}  
    ]