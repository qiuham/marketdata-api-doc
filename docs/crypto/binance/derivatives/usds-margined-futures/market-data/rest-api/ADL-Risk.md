---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/ADL-Risk
api_type: Market Data
updated_at: 2026-01-15T23:46:42.673616
---

# ADL Risk

## API Description[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/ADL-Risk#api-description "Direct link to API Description")

Query the symbol-level ADL risk rating. The ADL risk rating measures the likelihood of ADL during liquidation, and the rating takes into account the insurance fund balance, position concentration on the symbol, order book depth, price volatility, average leverage, unrealized PnL, and margin utilization at the symbol level. The rating can be high, medium and low, and is updated every 30 minutes.

## HTTP Request[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/ADL-Risk#http-request "Direct link to HTTP Request")

GET `/fapi/v1/symbolAdlRisk`

## Request Weight[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/ADL-Risk#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/ADL-Risk#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| NO|   
  
## Response Example[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/ADL-Risk#response-example "Direct link to Response Example")

> **Response:**
    
    
    {  
    	"symbol": "BTCUSDT",  
    	"adlRisk": "low",  // ADL Risk rating  
    	"updateTime": 1597370495002  
    }  
    

> **OR (when symbol not sent)**
    
    
    [  
    	{  
    	    "symbol": "BTCUSDT",  
    	    "adlRisk": "low",  // ADL Risk rating  
    	    "updateTime": 1597370495002  
    	},  
    	{  
    	    "symbol": "ETHUSDT",  
    	    "adlRisk": "high", // ADL Risk rating  
    	    "updateTime": 1597370495004  
    	}  
    ]

---

# 自动减仓风险评级

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/ADL-Risk#接口描述 "接口描述的直接链接")

查询symbol级别的 ADL 风险评级。 ADL 风险评级用于衡量在发生强平时触发 ADL 的可能性，该评级会综合考虑该symbol的保险基金余额、仓位集中度、盘口深度、价格波动率、平均杠杆水平、未实现盈亏以及保证金利用率。 风险等级分为高、中、低，每半小时更新一次。

## HTTP请求[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/ADL-Risk#http请求 "HTTP请求的直接链接")

GET `/fapi/v1/symbolAdlRisk`

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/ADL-Risk#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/ADL-Risk#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| NO| 交易对  
  
## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/ADL-Risk#响应示例 "响应示例的直接链接")

> **响应:**
    
    
    {  
    	"symbol": "BTCUSDT",  
    	"adlRisk": "low",  // 自动减仓风险评级  
    	"updateTime": 1597370495002  
    }  
    

> **当不指定symbol时相应**
    
    
    [  
    	{  
    	    "symbol": "BTCUSDT",  
    	    "adlRisk": "low",  // 自动减仓风险评级  
    	    "updateTime": 1597370495002  
    	},  
    	{  
    	    "symbol": "ETHUSDT",  
    	    "adlRisk": "high", // 自动减仓风险评级  
    	    "updateTime": 1597370495004  
    	}  
    ]