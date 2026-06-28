---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/rest-api/Account-Trade-List
api_type: Trading
updated_at: 2026-01-15T23:39:31.160766
---

# Account Trade List (USER_DATA)

## API Description[​](/docs/derivatives/coin-margined-futures/trade/rest-api/Account-Trade-List#api-description "Direct link to API Description")

Get trades for a specific account and symbol.

## HTTP Request[​](/docs/derivatives/coin-margined-futures/trade/rest-api/Account-Trade-List#http-request "Direct link to HTTP Request")

GET `/dapi/v1/userTrades`

## Request Weight[​](/docs/derivatives/coin-margined-futures/trade/rest-api/Account-Trade-List#request-weight "Direct link to Request Weight")

**20** with symbol，**40** with pair

## Request Parameters[​](/docs/derivatives/coin-margined-futures/trade/rest-api/Account-Trade-List#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| NO|   
pair| STRING| NO|   
orderId| STRING| NO|   
startTime| LONG| NO|   
endTime| LONG| NO|   
fromId| LONG| NO| Trade id to fetch from. Default gets most recent trades.  
limit| INT| NO| Default 50; max 1000  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * Either symbol or pair must be sent
>   * Symbol and pair cannot be sent together
>   * Pair and fromId cannot be sent together
>   * OrderId can only be sent together with symbol
>   * If a pair is sent,tickers for all symbols of the pair will be returned
>   * The parameter `fromId` cannot be sent with `startTime` or `endTime`
>   * If startTime and endTime are both not sent, then the last 7 days' data will be returned.
>   * The time between startTime and endTime cannot be longer than 7 days.
> 


## Response Example[​](/docs/derivatives/coin-margined-futures/trade/rest-api/Account-Trade-List#response-example "Direct link to Response Example")
    
    
    [  
    	{  
    		'symbol': 'BTCUSD_200626',  
    	  	'id': 6,  
    	  	'orderId': 28,  
    	  	'pair': 'BTCUSD',  
    	  	'side': 'SELL',  
    	  	'price': '8800',  
    	  	'qty': '1',  
    	  	'realizedPnl': '0',  
    	  	'marginAsset': 'BTC',  
    	  	'baseQty': '0.01136364',  
    	  	'commission': '0.00000454',  
    	  	'commissionAsset': 'BTC',  
    	  	'time': 1590743483586,  
    	  	'positionSide': 'BOTH',  
    	  	'buyer': false,  
    	  	'maker': false  
    	}  
    ]

---

# 账户成交历史 (USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/coin-margined-futures/trade/rest-api/Account-Trade-List#接口描述 "接口描述的直接链接")

获取成交历史

## HTTP请求[​](/docs/zh-CN/derivatives/coin-margined-futures/trade/rest-api/Account-Trade-List#http请求 "HTTP请求的直接链接")

GET `/dapi/v1/userTrades`

## 请求权重[​](/docs/zh-CN/derivatives/coin-margined-futures/trade/rest-api/Account-Trade-List#请求权重 "请求权重的直接链接")

传symbol **20** ，不传pairs **40**

## 请求参数[​](/docs/zh-CN/derivatives/coin-margined-futures/trade/rest-api/Account-Trade-List#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| NO| 交易对  
pair| STRING| NO| 标的交易对  
orderId| STRING| NO| 订单号  
startTime| LONG| NO| 起始时间  
endTime| LONG| NO| 结束时间  
fromId| LONG| NO| 返回该fromId及之后的成交,缺省返回最近的成交,仅支持配合symbol使用  
limit| INT| NO| 返回的结果集数量 默认值:50 最大值:1000  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * symbol 或 pair 其中一个必传
>   * symbol 和 pair 不可同时提供
>   * fromId 和 pair 不可同时提供
>   * orderId必须和symbol一起提供
>   * 发送 pair的,返回pair对应所有正在交易的symbol数据
>   * 参数 fromId 不能和startTime 与 endTime一起发送
>   * 如果startTime 和 endTime 均未发送, 只会返回最近7天的数据。
>   * startTime 和 endTime 的最大间隔为7天
> 


## 响应示例[​](/docs/zh-CN/derivatives/coin-margined-futures/trade/rest-api/Account-Trade-List#响应示例 "响应示例的直接链接")
    
    
    [  
    	{  
    		'symbol': 'BTCUSD_200626',		// 交易对  
    	  	'id': 6,						// 交易ID  
    	  	'orderId': 28,					// 订单ID  
    	  	'pair': 'BTCUSD',				// 标的交易对  
    	  	'side': 'SELL',					// 买卖方向  
    	  	'price': '8800',				// 成交价  
    	  	'qty': '1',						// 成交量(张数)  
    	  	'realizedPnl': '0',				// 实现盈亏  
    	  	'marginAsset': 'BTC',			// 保证金币种  
    	  	'baseQty': '0.01136364',		// 成交额(标的数量)  
    	  	'commission': '0.00000454',	// 手续费  
    	  	'commissionAsset': 'BTC',		// 手续费单位  
    	  	'time': 1590743483586,			// 时间  
    	  	'positionSide': 'BOTH',			// 持仓方向  
    	  	'buyer': false,					// 是否是买方  
    	  	'maker': false					// 是否是挂单方  
    	}  
    ]