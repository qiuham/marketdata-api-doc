---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Get-Position-Margin-Change-History
api_type: Trading
updated_at: 2026-01-15T23:47:17.454679
---

# Get Position Margin Change History (TRADE)

## API Description[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Get-Position-Margin-Change-History#api-description "Direct link to API Description")

Get Position Margin Change History

## HTTP Request[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Get-Position-Margin-Change-History#http-request "Direct link to HTTP Request")

GET `/fapi/v1/positionMargin/history`

## Request Weight[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Get-Position-Margin-Change-History#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Get-Position-Margin-Change-History#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
type| INT| NO| 1: Add position margin，2: Reduce position margin  
startTime| LONG| NO|   
endTime| LONG| NO| Default current time if not pass  
limit| INT| NO| Default: 500  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * Support querying future histories that are not older than 30 days
>   * The time between `startTime` and `endTime`can't be more than 30 days
> 


## Response Example[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Get-Position-Margin-Change-History#response-example "Direct link to Response Example")
    
    
    [  
    	{  
    	  	"symbol": "BTCUSDT",  
    	  	"type": 1,  
    		"deltaType": "USER_ADJUST",  
    		"amount": "23.36332311",  
    	  	"asset": "USDT",  
    	  	"time": 1578047897183,  
    	  	"positionSide": "BOTH"  
    	},  
    	{  
    		"symbol": "BTCUSDT",  
    	  	"type": 1,   
    		"deltaType": "USER_ADJUST",  
    		"amount": "100",  
    	  	"asset": "USDT",  
    	  	"time": 1578047900425,  
    	  	"positionSide": "LONG"   
    	}  
    ]

---

# 逐仓保证金变动历史(TRADE)

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Get-Position-Margin-Change-History#接口描述 "接口描述的直接链接")

查询逐仓保证金变动历史

## HTTP请求[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Get-Position-Margin-Change-History#http请求 "HTTP请求的直接链接")

GET `/fapi/v1/positionMargin/history`

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Get-Position-Margin-Change-History#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Get-Position-Margin-Change-History#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES| 交易对  
type| INT| NO| 调整方向 1: 增加逐仓保证金，2: 减少逐仓保证金  
startTime| LONG| NO| 起始时间  
endTime| LONG| NO| 结束时间，默认为当前时间  
limit| INT| NO| 返回的结果集数量 默认值: 500  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * `startTime`与`endTime`间隔不能超过30天
>   * 支持查询不超过1个月的合约数据
> 


## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Get-Position-Margin-Change-History#响应示例 "响应示例的直接链接")
    
    
    [  
    	{  
    	    "symbol": "BTCUSDT", // 交易对  
    	  	"type": 1, 	// 调整方向  
    		"deltaType": "USER_ADJUST", // 划转类型  
    		"amount": "23.36332311", // 数量  
    	  	"asset": "USDT", // 资产  
    	  	"time": 1578047897183, // 时间  
    	  	"positionSide": "BOTH"  // 持仓方向  
    	},  
    	{  
    		"symbol": "BTCUSDT",  
    	  	"type": 1,   
    		"deltaType": "USER_ADJUST",  
    		"amount": "100",  
    	  	"asset": "USDT",  
    	  	"time": 1578047900425,  
    	  	"positionSide": "LONG"   
    	}  
    ]