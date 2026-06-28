---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/rest-api/Get-Position-Margin-Change-History
api_type: Trading
updated_at: 2026-01-15T23:39:44.489844
---

# Get Position Margin Change History(TRADE)

## API Description[​](/docs/derivatives/coin-margined-futures/trade/rest-api/Get-Position-Margin-Change-History#api-description "Direct link to API Description")

Get position margin change history

## HTTP Request[​](/docs/derivatives/coin-margined-futures/trade/rest-api/Get-Position-Margin-Change-History#http-request "Direct link to HTTP Request")

GET `/dapi/v1/positionMargin/history`

## Request Weight[​](/docs/derivatives/coin-margined-futures/trade/rest-api/Get-Position-Margin-Change-History#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/coin-margined-futures/trade/rest-api/Get-Position-Margin-Change-History#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
type| INT| NO| 1: Add position margin,2: Reduce position margin  
startTime| LONG| NO|   
endTime| LONG| NO|   
limit| INT| NO| Default: 50  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/derivatives/coin-margined-futures/trade/rest-api/Get-Position-Margin-Change-History#response-example "Direct link to Response Example")
    
    
    [  
    	{  
    		"amount": "23.36332311",  
    	  	"asset": "BTC",  
    	  	"symbol": "BTCUSD_200925",  
    	  	"time": 1578047897183,  
    	  	"type": 1,  
    	  	"positionSide": "BOTH"  
    	},  
    	{  
    		"amount": "100",  
    	  	"asset": "BTC",  
    	  	"symbol": "BTCUSD_200925",  
    	  	"time": 1578047900425,  
    	  	"type": 1,  
    	  	"positionSide": "LONG"  
    	}  
    ]

---

# 逐仓保证金变动历史(TRADE)

## 接口描述[​](/docs/zh-CN/derivatives/coin-margined-futures/trade/rest-api/Get-Position-Margin-Change-History#接口描述 "接口描述的直接链接")

逐仓保证金变动历史

## HTTP请求[​](/docs/zh-CN/derivatives/coin-margined-futures/trade/rest-api/Get-Position-Margin-Change-History#http请求 "HTTP请求的直接链接")

GET `/dapi/v1/positionMargin/history`

## 请求权重[​](/docs/zh-CN/derivatives/coin-margined-futures/trade/rest-api/Get-Position-Margin-Change-History#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/coin-margined-futures/trade/rest-api/Get-Position-Margin-Change-History#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES| 交易对  
type| INT| NO| 调整方向 1: 增加逐仓保证金,2: 减少逐仓保证金  
startTime| LONG| NO| 起始时间  
endTime| LONG| NO| 结束时间  
limit| INT| NO| 返回的结果集数量 默认值: 50  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/derivatives/coin-margined-futures/trade/rest-api/Get-Position-Margin-Change-History#响应示例 "响应示例的直接链接")
    
    
    [  
    	{  
    		"amount": "23.36332311", // 数量  
    	  	"asset": "BTC", // 资产  
    	  	"symbol": "BTCUSD_200925", // 交易对  
    	  	"time": 1578047897183, // 时间  
    	  	"type": 1,  // 调整方向  
    	  	"positionSide": "BOTH"  // 持仓方向  
    	},  
    	{  
    		"amount": "100",  
    	  	"asset": "BTC",  
    	  	"symbol": "BTCUSD_200925",  
    	  	"time": 1578047900425,  
    	  	"type": 1,  
    	  	"positionSide": "LONG"   
    	}  
    ]