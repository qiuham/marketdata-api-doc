---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/Account-Information-V2
api_type: Account
updated_at: 2026-01-15T23:46:14.039639
---

# Account Information V2(USER_DATA)

## API Description[​](/docs/derivatives/usds-margined-futures/account/rest-api/Account-Information-V2#api-description "Direct link to API Description")

Get current account information. User in single-asset/ multi-assets mode will see different value, see comments in response section for detail.

## HTTP Request[​](/docs/derivatives/usds-margined-futures/account/rest-api/Account-Information-V2#http-request "Direct link to HTTP Request")

GET `/fapi/v2/account`

 

## Request Weight[​](/docs/derivatives/usds-margined-futures/account/rest-api/Account-Information-V2#request-weight "Direct link to Request Weight")

**5**

## Request Parameters[​](/docs/derivatives/usds-margined-futures/account/rest-api/Account-Information-V2#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/derivatives/usds-margined-futures/account/rest-api/Account-Information-V2#response-example "Direct link to Response Example")

> single-asset mode
    
    
    {     
    	"feeTier": 0,  		// account commission tier   
    	"feeBurn": true,  	// "true": Fee Discount On; "false": Fee Discount Off	"canTrade": true,  	// if can trade  
    	"canDeposit": true,  	// if can transfer in asset  
    	"canWithdraw": true, 	// if can transfer out asset  
    	"updateTime": 0,        // reserved property, please ignore   
    	"multiAssetsMargin": false,  
    	"tradeGroupId": -1,  
    	"totalInitialMargin": "0.00000000",    // total initial margin required with current mark price (useless with isolated positions), only for USDT asset  
    	"totalMaintMargin": "0.00000000",  	  // total maintenance margin required, only for USDT asset  
    	"totalWalletBalance": "23.72469206",     // total wallet balance, only for USDT asset  
    	"totalUnrealizedProfit": "0.00000000",   // total unrealized profit, only for USDT asset  
    	"totalMarginBalance": "23.72469206",     // total margin balance, only for USDT asset  
    	"totalPositionInitialMargin": "0.00000000",    // initial margin required for positions with current mark price, only for USDT asset  
    	"totalOpenOrderInitialMargin": "0.00000000",   // initial margin required for open orders with current mark price, only for USDT asset  
    	"totalCrossWalletBalance": "23.72469206",      // crossed wallet balance, only for USDT asset  
    	"totalCrossUnPnl": "0.00000000",	  // unrealized profit of crossed positions, only for USDT asset  
    	"availableBalance": "23.72469206",       // available balance, only for USDT asset  
    	"maxWithdrawAmount": "23.72469206"     // maximum amount for transfer out, only for USDT asset  
    	"assets": [  
    		{  
    			"asset": "USDT",			// asset name  
    			"walletBalance": "23.72469206",      // wallet balance  
    			"unrealizedProfit": "0.00000000",    // unrealized profit  
    			"marginBalance": "23.72469206",      // margin balance  
    			"maintMargin": "0.00000000",	    // maintenance margin required  
    			"initialMargin": "0.00000000",    // total initial margin required with current mark price   
    			"positionInitialMargin": "0.00000000",    //initial margin required for positions with current mark price  
    			"openOrderInitialMargin": "0.00000000",   // initial margin required for open orders with current mark price  
    			"crossWalletBalance": "23.72469206",      // crossed wallet balance  
    			"crossUnPnl": "0.00000000"       // unrealized profit of crossed positions  
    			"availableBalance": "23.72469206",       // available balance  
    			"maxWithdrawAmount": "23.72469206",     // maximum amount for transfer out  
    			"marginAvailable": true,    // whether the asset can be used as margin in Multi-Assets mode  
    			"updateTime": 1625474304765 // last update time   
    		},  
    		{  
    			"asset": "BUSD",			// asset name  
    			"walletBalance": "103.12345678",      // wallet balance  
    			"unrealizedProfit": "0.00000000",    // unrealized profit  
    			"marginBalance": "103.12345678",      // margin balance  
    			"maintMargin": "0.00000000",	    // maintenance margin required  
    			"initialMargin": "0.00000000",    // total initial margin required with current mark price   
    			"positionInitialMargin": "0.00000000",    //initial margin required for positions with current mark price  
    			"openOrderInitialMargin": "0.00000000",   // initial margin required for open orders with current mark price  
    			"crossWalletBalance": "103.12345678",      // crossed wallet balance  
    			"crossUnPnl": "0.00000000"       // unrealized profit of crossed positions  
    			"availableBalance": "103.12345678",       // available balance  
    			"maxWithdrawAmount": "103.12345678",     // maximum amount for transfer out  
    			"marginAvailable": true,    // whether the asset can be used as margin in Multi-Assets mode  
    			"updateTime": 1625474304765 // last update time  
    		}  
    	],  
    	"positions": [  // positions of all symbols in the market are returned  
    		// only "BOTH" positions will be returned with One-way mode  
    		// only "LONG" and "SHORT" positions will be returned with Hedge mode  
    		{  
    			"symbol": "BTCUSDT",  	// symbol name  
    			"initialMargin": "0",	// initial margin required with current mark price   
    			"maintMargin": "0",		// maintenance margin required  
    			"unrealizedProfit": "0.00000000",  // unrealized profit  
    			"positionInitialMargin": "0",      // initial margin required for positions with current mark price  
    			"openOrderInitialMargin": "0",     // initial margin required for open orders with current mark price  
    			"leverage": "100",		// current initial leverage  
    			"isolated": true,  		// if the position is isolated  
    			"entryPrice": "0.00000",  	// average entry price  
    			"maxNotional": "250000",  	// maximum available notional with current leverage  
    			"bidNotional": "0",  // bids notional, ignore  
    			"askNotional": "0",  // ask notional, ignore  
    			"positionSide": "BOTH",  	// position side  
    			"positionAmt": "0",			// position amount  
    			"updateTime": 0           // last update time  
    		}  
    	]  
    }  
    

> OR multi-assets mode
    
    
    {     
    	"feeTier": 0,  		// account commission tier   
    	"feeBurn": true,  	// "true": Fee Discount On; "false": Fee Discount Off	"canTrade": true,  	// if can trade  
    	"canTrade": true,  	// if can trade  
    	"canDeposit": true,  	// if can transfer in asset  
    	"canWithdraw": true, 	// if can transfer out asset  
    	"updateTime": 0,        // reserved property, please ignore   
    	"multiAssetsMargin": true,  
    	"tradeGroupId": -1,  
    	"totalInitialMargin": "0.00000000",    // the sum of USD value of all cross positions/open order initial margin  
    	"totalMaintMargin": "0.00000000",  	  // the sum of USD value of all cross positions maintenance margin  
    	"totalWalletBalance": "126.72469206",     // total wallet balance in USD  
    	"totalUnrealizedProfit": "0.00000000",   // total unrealized profit in USD  
    	"totalMarginBalance": "126.72469206",     // total margin balance in USD  
    	"totalPositionInitialMargin": "0.00000000",    // the sum of USD value of all cross positions initial margin  
    	"totalOpenOrderInitialMargin": "0.00000000",   // initial margin required for open orders with current mark price in USD  
    	"totalCrossWalletBalance": "126.72469206",      // crossed wallet balance in USD  
    	"totalCrossUnPnl": "0.00000000",	  // unrealized profit of crossed positions in USD  
    	"availableBalance": "126.72469206",       // available balance in USD  
    	"maxWithdrawAmount": "126.72469206"     // maximum virtual amount for transfer out in USD  
    	"assets": [  
    		{  
    			"asset": "USDT",			// asset name  
    			"walletBalance": "23.72469206",      // wallet balance  
    			"unrealizedProfit": "0.00000000",    // unrealized profit  
    			"marginBalance": "23.72469206",      // margin balance  
    			"maintMargin": "0.00000000",	    // maintenance margin required  
    			"initialMargin": "0.00000000",    // total initial margin required with current mark price   
    			"positionInitialMargin": "0.00000000",    //initial margin required for positions with current mark price  
    			"openOrderInitialMargin": "0.00000000",   // initial margin required for open orders with current mark price  
    			"crossWalletBalance": "23.72469206",      // crossed wallet balance  
    			"crossUnPnl": "0.00000000"       // unrealized profit of crossed positions  
    			"availableBalance": "126.72469206",       // available balance  
    			"maxWithdrawAmount": "23.72469206",     // maximum amount for transfer out  
    			"marginAvailable": true,    // whether the asset can be used as margin in Multi-Assets mode  
    			"updateTime": 1625474304765 // last update time   
    		},  
    		{  
    			"asset": "BUSD",			// asset name  
    			"walletBalance": "103.12345678",      // wallet balance  
    			"unrealizedProfit": "0.00000000",    // unrealized profit  
    			"marginBalance": "103.12345678",      // margin balance  
    			"maintMargin": "0.00000000",	    // maintenance margin required  
    			"initialMargin": "0.00000000",    // total initial margin required with current mark price   
    			"positionInitialMargin": "0.00000000",    //initial margin required for positions with current mark price  
    			"openOrderInitialMargin": "0.00000000",   // initial margin required for open orders with current mark price  
    			"crossWalletBalance": "103.12345678",      // crossed wallet balance  
    			"crossUnPnl": "0.00000000"       // unrealized profit of crossed positions  
    			"availableBalance": "126.72469206",       // available balance  
    			"maxWithdrawAmount": "103.12345678",     // maximum amount for transfer out  
    			"marginAvailable": true,    // whether the asset can be used as margin in Multi-Assets mode  
    			"updateTime": 1625474304765 // last update time  
    		}  
    	],  
    	"positions": [  // positions of all symbols in the market are returned  
    		// only "BOTH" positions will be returned with One-way mode  
    		// only "LONG" and "SHORT" positions will be returned with Hedge mode  
    		{  
    			"symbol": "BTCUSDT",  	// symbol name  
    			"initialMargin": "0",	// initial margin required with current mark price   
    			"maintMargin": "0",		// maintenance margin required  
    			"unrealizedProfit": "0.00000000",  // unrealized profit  
    			"positionInitialMargin": "0",      // initial margin required for positions with current mark price  
    			"openOrderInitialMargin": "0",     // initial margin required for open orders with current mark price  
    			"leverage": "100",		// current initial leverage  
    			"isolated": true,  		// if the position is isolated  
    			"entryPrice": "0.00000",  	// average entry price  
    			"maxNotional": "250000",  	// maximum available notional with current leverage  
    			"bidNotional": "0",  // bids notional, ignore  
    			"askNotional": "0",  // ask notional, ignore  
    			"positionSide": "BOTH",  	// position side  
    			"positionAmt": "0",			// position amount  
    			"updateTime": 0           // last update time  
    		}  
    	]  
    }

---

# 账户信息V2 (USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Account-Information-V2#接口描述 "接口描述的直接链接")

现有账户信息。 用户在单资产模式和多资产模式下会看到不同结果，响应部分的注释解释了两种模式下的不同。

## HTTP请求[​](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Account-Information-V2#http请求 "HTTP请求的直接链接")

GET `/fapi/v2/account`

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Account-Information-V2#请求权重 "请求权重的直接链接")

**5**

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Account-Information-V2#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Account-Information-V2#响应示例 "响应示例的直接链接")

> 单资产模式
    
    
    {  
    	"feeTier": 0,  // 手续费等级  
    	"feeBurn": true,   // "true": 手续费抵扣开; "false": 手续费抵扣关  
    	"canTrade": true,  // 是否可以交易  
    	"canDeposit": true,  // 是否可以入金  
    	"canWithdraw": true, // 是否可以出金  
    	"updateTime": 0,     // 保留字段，请忽略  
    	"multiAssetsMargin": false,  
    	"tradeGroupId": -1,  
    	"totalInitialMargin": "0.00000000",  // 当前所需起始保证金总额(存在逐仓请忽略), 仅计算usdt资产  
    	"totalMaintMargin": "0.00000000",  // 维持保证金总额, 仅计算usdt资产  
    	"totalWalletBalance": "23.72469206",   // 账户总余额, 仅计算usdt资产  
    	"totalUnrealizedProfit": "0.00000000",  // 持仓未实现盈亏总额, 仅计算usdt资产  
    	"totalMarginBalance": "23.72469206",  // 保证金总余额, 仅计算usdt资产  
    	"totalPositionInitialMargin": "0.00000000",  // 持仓所需起始保证金(基于最新标记价格), 仅计算usdt资产  
    	"totalOpenOrderInitialMargin": "0.00000000",  // 当前挂单所需起始保证金(基于最新标记价格), 仅计算usdt资产  
    	"totalCrossWalletBalance": "23.72469206",  // 全仓账户余额, 仅计算usdt资产  
    	"totalCrossUnPnl": "0.00000000",	// 全仓持仓未实现盈亏总额, 仅计算usdt资产  
    	"availableBalance": "23.72469206",       // 可用余额, 仅计算usdt资产  
    	"maxWithdrawAmount": "23.72469206"     // 最大可转出余额, 仅计算usdt资产  
    	"assets": [  
    		{  
    			"asset": "USDT",	 	//资产  
    			"walletBalance": "23.72469206",  //余额  
    			"unrealizedProfit": "0.00000000",  // 未实现盈亏  
    			"marginBalance": "23.72469206",  // 保证金余额  
    			"maintMargin": "0.00000000",	// 维持保证金  
    			"initialMargin": "0.00000000",  // 当前所需起始保证金  
    			"positionInitialMargin": "0.00000000",  // 持仓所需起始保证金(基于最新标记价格)  
    			"openOrderInitialMargin": "0.00000000", // 当前挂单所需起始保证金(基于最新标记价格)  
    			"crossWalletBalance": "23.72469206",  //全仓账户余额  
    			"crossUnPnl": "0.00000000" // 全仓持仓未实现盈亏  
    			"availableBalance": "126.72469206",       // 可用余额  
    			"maxWithdrawAmount": "23.72469206",     // 最大可转出余额  
    			"marginAvailable": true,   // 是否可用作联合保证金  
    			"updateTime": 1625474304765  //更新时间  
    		},  
    		{  
    			"asset": "BUSD",	 	//资产  
    			"walletBalance": "103.12345678",  //余额  
    			"unrealizedProfit": "0.00000000",  // 未实现盈亏  
    			"marginBalance": "103.12345678",  // 保证金余额  
    			"maintMargin": "0.00000000",	// 维持保证金  
    			"initialMargin": "0.00000000",  // 当前所需起始保证金  
    			"positionInitialMargin": "0.00000000",  // 持仓所需起始保证金(基于最新标记价格)  
    			"openOrderInitialMargin": "0.00000000", // 当前挂单所需起始保证金(基于最新标记价格)  
    			"crossWalletBalance": "103.12345678",  //全仓账户余额  
    			"crossUnPnl": "0.00000000" // 全仓持仓未实现盈亏  
    			"availableBalance": "126.72469206",       // 可用余额  
    			"maxWithdrawAmount": "103.12345678",     // 最大可转出余额  
    			"marginAvailable": true,   // 否可用作联合保证金  
    			"updateTime": 0  // 更新时间  
    			}  
    	],  
    	"positions": [  // 头寸，将返回所有市场symbol。  
    		//根据用户持仓模式展示持仓方向，即单向模式下只返回BOTH持仓情况，双向模式下只返回 LONG 和 SHORT 持仓情况  
    		{  
    			"symbol": "BTCUSDT",  // 交易对  
    			"initialMargin": "0",	// 当前所需起始保证金(基于最新标记价格)  
    			"maintMargin": "0",	//维持保证金  
    			"unrealizedProfit": "0.00000000",  // 持仓未实现盈亏  
    			"positionInitialMargin": "0",  // 持仓所需起始保证金(基于最新标记价格)  
    			"openOrderInitialMargin": "0",  // 当前挂单所需起始保证金(基于最新标记价格)  
    			"leverage": "100",	// 杠杆倍率  
    			"isolated": true,  // 是否是逐仓模式  
    			"entryPrice": "0.00000",  // 持仓成本价  
    			"maxNotional": "250000",  // 当前杠杆下用户可用的最大名义价值  
    			"bidNotional": "0",  // 买单净值，忽略  
    			"askNotional": "0",  // 卖单净值，忽略  
    			"positionSide": "BOTH",  // 持仓方向  
    			"positionAmt": "0",		 // 持仓数量  
    			"updateTime": 0         // 更新时间   
    		}  
    	]  
    }  
    

> 多资产模式
    
    
    {  
    	"feeTier": 0,  // 手续费等级  
    	"feeBurn": true,   // "true": 手续费抵扣开; "false": 手续费抵扣关  
    	"canTrade": true,  // 是否可以交易  
    	"canDeposit": true,  // 是否可以入金  
    	"canWithdraw": true, // 是否可以出金  
    	"updateTime": 0,     // 保留字段，请忽略  
    	"multiAssetsMargin": true,  
    	"tradeGroupId": -1,  
    	"totalInitialMargin": "0.00000000",  // 以USD计价的所需起始保证金总额  
    	"totalMaintMargin": "0.00000000",  // 以USD计价的维持保证金总额  
    	"totalWalletBalance": "126.72469206",   // 以USD计价的账户总余额  
    	"totalUnrealizedProfit": "0.00000000",  // 以USD计价的持仓未实现盈亏总额  
    	"totalMarginBalance": "126.72469206",  // 以USD计价的保证金总余额  
    	"totalPositionInitialMargin": "0.00000000",  // 以USD计价的持仓所需起始保证金(基于最新标记价格)  
    	"totalOpenOrderInitialMargin": "0.00000000",  // 以USD计价的当前挂单所需起始保证金(基于最新标记价格)  
    	"totalCrossWalletBalance": "126.72469206",  // 以USD计价的全仓账户余额  
    	"totalCrossUnPnl": "0.00000000",	// 以USD计价的全仓持仓未实现盈亏总额  
    	"availableBalance": "126.72469206",       // 以USD计价的可用余额  
    	"maxWithdrawAmount": "126.72469206"     // 以USD计价的最大可转出余额  
    	"assets": [  
    		{  
    			"asset": "USDT",	 	//资产  
    			"walletBalance": "23.72469206",  //余额  
    			"unrealizedProfit": "0.00000000",  // 未实现盈亏  
    			"marginBalance": "23.72469206",  // 保证金余额  
    			"maintMargin": "0.00000000",	// 维持保证金  
    			"initialMargin": "0.00000000",  // 当前所需起始保证金  
    			"positionInitialMargin": "0.00000000",  // 持仓所需起始保证金(基于最新标记价格)  
    			"openOrderInitialMargin": "0.00000000", // 当前挂单所需起始保证金(基于最新标记价格)  
    			"crossWalletBalance": "23.72469206",  //全仓账户余额  
    			"crossUnPnl": "0.00000000" // 全仓持仓未实现盈亏  
    			"availableBalance": "23.72469206",       // 可用余额  
    			"maxWithdrawAmount": "23.72469206",     // 最大可转出余额  
    			"marginAvailable": true,   // 是否可用作联合保证金  
    			"updateTime": 1625474304765  //更新时间  
    		},  
    		{  
    			"asset": "BUSD",	 	//资产  
    			"walletBalance": "103.12345678",  //余额  
    			"unrealizedProfit": "0.00000000",  // 未实现盈亏  
    			"marginBalance": "103.12345678",  // 保证金余额  
    			"maintMargin": "0.00000000",	// 维持保证金  
    			"initialMargin": "0.00000000",  // 当前所需起始保证金  
    			"positionInitialMargin": "0.00000000",  // 持仓所需起始保证金(基于最新标记价格)  
    			"openOrderInitialMargin": "0.00000000", // 当前挂单所需起始保证金(基于最新标记价格)  
    			"crossWalletBalance": "103.12345678",  //全仓账户余额  
    			"crossUnPnl": "0.00000000" // 全仓持仓未实现盈亏  
    			"availableBalance": "103.12345678",       // 可用余额  
    			"maxWithdrawAmount": "103.12345678",     // 最大可转出余额  
    			"marginAvailable": true,   // 否可用作联合保证金  
    			"updateTime": 0  // 更新时间  
    			}  
    	],  
    	"positions": [  // 头寸，将返回所有市场symbol。  
    		//根据用户持仓模式展示持仓方向，即单向模式下只返回BOTH持仓情况，双向模式下只返回 LONG 和 SHORT 持仓情况  
    		{  
    			"symbol": "BTCUSDT",  // 交易对  
    			"initialMargin": "0",	// 当前所需起始保证金(基于最新标记价格)  
    			"maintMargin": "0",	//维持保证金  
    			"unrealizedProfit": "0.00000000",  // 持仓未实现盈亏  
    			"positionInitialMargin": "0",  // 持仓所需起始保证金(基于最新标记价格)  
    			"openOrderInitialMargin": "0",  // 当前挂单所需起始保证金(基于最新标记价格)  
    			"leverage": "100",	// 杠杆倍率  
    			"isolated": true,  // 是否是逐仓模式  
    			"entryPrice": "0.00000",  // 持仓成本价  
    			"maxNotional": "250000",  // 当前杠杆下用户可用的最大名义价值  
    			"bidNotional": "0",  // 买单净值，忽略  
    			"askNotional": "0",  // 买单净值，忽略  
    			"positionSide": "BOTH",  // 持仓方向  
    			"positionAmt": "0",		 // 持仓数量  
    			"updateTime": 0         // 更新时间   
    		}  
    	]  
    }