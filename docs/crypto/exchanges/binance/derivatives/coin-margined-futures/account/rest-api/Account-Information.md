---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/coin-margined-futures/account/rest-api/Account-Information
api_type: Account
updated_at: 2026-01-15T23:37:32.295639
---

# Account Information (USER_DATA)

## API Description[​](/docs/derivatives/coin-margined-futures/account/rest-api/Account-Information#api-description "Direct link to API Description")

Get current account information.

## HTTP Request[​](/docs/derivatives/coin-margined-futures/account/rest-api/Account-Information#http-request "Direct link to HTTP Request")

GET `/dapi/v1/account`

## Request Weight[​](/docs/derivatives/coin-margined-futures/account/rest-api/Account-Information#request-weight "Direct link to Request Weight")

**5**

## Request Parameters[​](/docs/derivatives/coin-margined-futures/account/rest-api/Account-Information#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * for One-way Mode user, the "positions" will only show the "BOTH" positions
>   * for Hedge Mode user, the "positions" will show "BOTH", "LONG", and "SHORT" positions.
> 


## Response Example[​](/docs/derivatives/coin-margined-futures/account/rest-api/Account-Information#response-example "Direct link to Response Example")
    
    
    {  
    	"assets": [  
    		{  
    			"asset": "BTC",  // asset name   
       			"walletBalance": "0.00241969",  // total wallet balance  
       			"unrealizedProfit": "0.00000000",  // unrealized profit or loss  
       			"marginBalance": "0.00241969",  // margin balance  
       			"maintMargin": "0.00000000",	// maintenance margin  
       			"initialMargin": "0.00000000",  // total intial margin required with the latest mark price  
       			"positionInitialMargin": "0.00000000",  // positions" margin required with the latest mark price  
       			"openOrderInitialMargin": "0.00000000",  // open orders" intial margin required with the latest mark price  
       			"maxWithdrawAmount": "0.00241969",  // available amount for transfer out  
       			"crossWalletBalance": "0.00241969",  // wallet balance for crossed margin  
       			"crossUnPnl": "0.00000000",  // total unrealized profit or loss of crossed positions  
       			"availableBalance": "0.00241969", // available margin balance  
    			"updateTime": 1625474304765 //update time  
       		}  
    	 ],  
    	 "positions": [  
    		 {  
    		 	"symbol": "BTCUSD_201225",  
    		 	"positionAmt":"0",	// position amount  
       			"initialMargin": "0",  
       			"maintMargin": "0",  
       			"unrealizedProfit": "0.00000000",  
       			"positionInitialMargin": "0",  
       			"openOrderInitialMargin": "0",  
       			"leverage": "125",  
       			"isolated": false,  
       			"positionSide": "BOTH", // BOTH means that it is the position of One-way Mode    
       			"entryPrice": "0.0",  
       			"breakEvenPrice": "0.0",  // break-even price  
       			"maxQty": "50",  // maximum quantity of base asset  
       			"updateTime": 0  
       		},  
      		{  
      			"symbol": "BTCUSD_201225",  
    		 	"positionAmt":"0",  
       			"initialMargin": "0",  
       			"maintMargin": "0",  
       			"unrealizedProfit": "0.00000000",  
       			"positionInitialMargin": "0",  
       			"openOrderInitialMargin": "0",  
       			"leverage": "125",  
       			"isolated": false,  
       			"positionSide": "LONG",  // LONG or SHORT means that it is the position of Hedge Mode   
       			"entryPrice": "0.0",  
       			"breakEvenPrice": "0.0",  // break-even price  
       			"maxQty": "50",  
       			"updateTime": 0  
       		},  
      		{  
      			"symbol": "BTCUSD_201225",  
    		 	"positionAmt":"0",  
       			"initialMargin": "0",  
       			"maintMargin": "0",  
       			"unrealizedProfit": "0.00000000",  
       			"positionInitialMargin": "0",  
       			"openOrderInitialMargin": "0",  
       			"leverage": "125",  
       			"isolated": false,  
       			"positionSide": "SHORT",  // LONG or SHORT means that it is the position of Hedge Mode   
       			"entryPrice": "0.0",  
       			"breakEvenPrice": "0.0",  // break-even price  
       			"maxQty": "50",  
    			"notionalValue": "0",  
       			"updateTime":1627026881327  
       		}  
    	 ],  
    	 "canDeposit": true,  
    	 "canTrade": true,  
    	 "canWithdraw": true,  
    	 "feeTier": 2,  
    	 "updateTime": 0  
    }

---

# 账户信息 (USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/coin-margined-futures/account/rest-api/Account-Information#接口描述 "接口描述的直接链接")

查询账户信息

## HTTP请求[​](/docs/zh-CN/derivatives/coin-margined-futures/account/rest-api/Account-Information#http请求 "HTTP请求的直接链接")

GET `/dapi/v1/account`

## 请求权重[​](/docs/zh-CN/derivatives/coin-margined-futures/account/rest-api/Account-Information#请求权重 "请求权重的直接链接")

**5**

## 请求参数[​](/docs/zh-CN/derivatives/coin-margined-futures/account/rest-api/Account-Information#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * 对于单向持仓模式，"positions"仅会展示"BOTH"方向的持仓
>   * 对于双向持仓模式，"positions"会展示所有"BOTH", "LONG", 和"SHORT"方向的持仓
> 


## 响应示例[​](/docs/zh-CN/derivatives/coin-margined-futures/account/rest-api/Account-Information#响应示例 "响应示例的直接链接")
    
    
      
    {  
    	"assets": [	// 资产内容  
    		{  
    			"asset": "BTC",  // 资产名  
       			"walletBalance": "0.00241969",  // 账户余额  
       			"unrealizedProfit": "0.00000000",  // 全部持仓未实现盈亏  
       			"marginBalance": "0.00241969",  // 保证金余额  
       			"maintMargin": "0.00000000",	// 维持保证金  
       			"initialMargin": "0.00000000",  // 当前所需起始保证金(按最新标标记价格)  
       			"positionInitialMargin": "0.00000000",  // 当前所需持仓起始保证金(按最新标标记价格)  
       			"openOrderInitialMargin": "0.00000000",  // 当前所需挂单起始保证金(按最新标标记价格)  
       			"maxWithdrawAmount": "0.00241969",  // 最大可提款金额  
       			"crossWalletBalance": "0.00241969",  // 可用于全仓的账户余额  
       			"crossUnPnl": "0.00000000",  // 所有全仓持仓的未实现盈亏  
       			"availableBalance": "0.00241969", // 可用下单余额  
    			"updateTime": 1625474304765  //更新时间  
       		}  
    	 ],  
    	 "positions": [	// 头寸  
    		 {  
    		 	"symbol": "BTCUSD_201225",	// 交易对   
    		 	"positionAmt": "0",	// 持仓数量  
       			"initialMargin": "0",	// 当前所需起始保证金(按最新标标记价格)  
       			"maintMargin": "0",	// 持仓维持保证金  
       			"unrealizedProfit": "0.00000000",  // 持仓未实现盈亏  
       			"positionInitialMargin": "0",  // 当前所需持仓起始保证金(按最新标标记价格)  
       			"openOrderInitialMargin": "0",  // 当前所需挂单起始保证金(按最新标标记价格)  
       			"leverage": "125",	// 杠杆倍率  
       			"isolated": false,	// 是否是逐仓模式  
       			"positionSide": "BOTH", // 持仓方向  
       			"entryPrice": "0.0",	// 平均持仓成本  
       			"breakEvenPrice": "0.0",  // 盈亏平衡价  
       			"updateTime":0,  // 最新更新时间  
       			"maxQty": "50"	// 当前杠杆下最大可开仓数(标的数量)  
       		},  
      		{  
      			"symbol": "BTCUSD_201225",  
    		 	"positionAmt": "0",  
       			"initialMargin": "0",  
       			"maintMargin": "0",  
       			"unrealizedProfit": "0.00000000",  
       			"positionInitialMargin": "0",  
       			"openOrderInitialMargin": "0",  
       			"leverage": "125",  
       			"isolated": false,  
       			"positionSide": "LONG",    
       			"entryPrice": "0.0",  
       			"breakEvenPrice": "0.0",  // 盈亏平衡价  
       			"maxQty": "50",  
       			"updateTime":0  
       		},  
      		{  
      			"symbol": "BTCUSD_201225",  
    		 	"positionAmt": "0",  
       			"initialMargin": "0",  
       			"maintMargin": "0",  
       			"unrealizedProfit": "0.00000000",  
       			"positionInitialMargin": "0",  
       			"openOrderInitialMargin": "0",  
       			"leverage": "125",  
       			"isolated": false,  
       			"positionSide": "SHORT",   
       			"entryPrice": "0.0",  
       			"breakEvenPrice": "0.0",  // 盈亏平衡价  
       			"maxQty": "50",  
    			"notionalValue": "0",  
       			"updateTime":1627026881327  
       		}  
    	 ],  
    	 "canDeposit": true, // 是否可以入金  
    	 "canTrade": true, // 是否可以交易  
    	 "canWithdraw": true, // 是否可以出金  
    	 "feeTier": 2, // 手续费等级  
    	 "updateTime": 0  
    }