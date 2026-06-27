---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/account/websocket-api/Account-Information-V2
api_type: WebSocket
updated_at: 2026-01-15T23:46:33.288705
---

# Account Information V2(USER_DATA)

## API Description[​](/docs/derivatives/usds-margined-futures/account/websocket-api/Account-Information-V2#api-description "Direct link to API Description")

Get current account information. User in single-asset/ multi-assets mode will see different value, see comments in response section for detail.

## Method[​](/docs/derivatives/usds-margined-futures/account/websocket-api/Account-Information-V2#method "Direct link to Method")

`v2/account.status`

## Request[​](/docs/derivatives/usds-margined-futures/account/websocket-api/Account-Information-V2#request "Direct link to Request")
    
    
    {  
        "id": "605a6d20-6588-4cb9-afa0-b0ab087507ba",  
        "method": "v2/account.status",  
        "params": {  
            "apiKey": "xTaDyrmvA9XT2oBHHjy39zyPzKCvMdtH3b9q4xadkAg2dNSJXQGCxzui26L823W2",  
            "timestamp": 1702620814781,  
            "signature": "6bb98ef84170c70ba3d01f44261bfdf50fef374e551e590de22b5c3b729b1d8c"  
        }  
    }  
    

 

## Request Weight[​](/docs/derivatives/usds-margined-futures/account/websocket-api/Account-Information-V2#request-weight "Direct link to Request Weight")

**5**

## Request Parameters[​](/docs/derivatives/usds-margined-futures/account/websocket-api/Account-Information-V2#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/derivatives/usds-margined-futures/account/websocket-api/Account-Information-V2#response-example "Direct link to Response Example")

> Single Asset Mode
    
    
    {  
      "id": "605a6d20-6588-4cb9-afa0-b0ab087507ba",  
      "status": 200,  
      "result": {     
      	"totalInitialMargin": "0.00000000",            // total initial margin required with current mark price (useless with isolated positions), only for USDT asset  
      	"totalMaintMargin": "0.00000000",  	           // total maintenance margin required, only for USDT asset  
      	"totalWalletBalance": "103.12345678",           // total wallet balance, only for USDT asset  
      	"totalUnrealizedProfit": "0.00000000",         // total unrealized profit, only for USDT asset  
      	"totalMarginBalance": "103.12345678",           // total margin balance, only for USDT asset  
      	"totalPositionInitialMargin": "0.00000000",    // initial margin required for positions with current mark price, only for USDT asset  
      	"totalOpenOrderInitialMargin": "0.00000000",   // initial margin required for open orders with current mark price, only for USDT asset  
      	"totalCrossWalletBalance": "103.12345678",      // crossed wallet balance, only for USDT asset  
      	"totalCrossUnPnl": "0.00000000",	           // unrealized profit of crossed positions, only for USDT asset  
      	"availableBalance": "103.12345678",             // available balance, only for USDT asset  
      	"maxWithdrawAmount": "103.12345678"             // maximum amount for transfer out, only for USDT asset  
      	"assets": [ // For assets that are quote assets, USDT/USDC/BTC  
      		{  
      			"asset": "USDT",			            // asset name  
      			"walletBalance": "23.72469206",         // wallet balance  
      			"unrealizedProfit": "0.00000000",       // unrealized profit  
      			"marginBalance": "23.72469206",         // margin balance  
      			"maintMargin": "0.00000000",	        // maintenance margin required  
      			"initialMargin": "0.00000000",          // total initial margin required with current mark price   
      			"positionInitialMargin": "0.00000000",  // initial margin required for positions with current mark price  
      			"openOrderInitialMargin": "0.00000000", // initial margin required for open orders with current mark price  
      			"crossWalletBalance": "23.72469206",    // crossed wallet balance  
      			"crossUnPnl": "0.00000000"              // unrealized profit of crossed positions  
      			"availableBalance": "23.72469206",      // available balance  
      			"maxWithdrawAmount": "23.72469206",     // maximum amount for transfer out  
      			"updateTime": 1625474304765             // last update time   
      		},     
       		{  
      			"asset": "USDC",			            // asset name  
      			"walletBalance": "103.12345678",         // wallet balance  
      			"unrealizedProfit": "0.00000000",       // unrealized profit  
      			"marginBalance": "103.12345678",         // margin balance  
      			"maintMargin": "0.00000000",	        // maintenance margin required  
      			"initialMargin": "0.00000000",          // total initial margin required with current mark price   
      			"positionInitialMargin": "0.00000000",  // initial margin required for positions with current mark price  
      			"openOrderInitialMargin": "0.00000000", // initial margin required for open orders with current mark price  
      			"crossWalletBalance": "103.12345678",    // crossed wallet balance  
      			"crossUnPnl": "0.00000000"              // unrealized profit of crossed positions  
      			"availableBalance": "126.72469206",      // available balance  
      			"maxWithdrawAmount": "103.12345678",     // maximum amount for transfer out  
      			"updateTime": 1625474304765             // last update time   
      		},      
          ],  
      	"positions": [  // positions of all symbols user had position/ open orders are returned  
      		            // only "BOTH" positions will be returned with One-way mode  
      		            // only "LONG" and "SHORT" positions will be returned with Hedge mode  
         	  {  
                 "symbol": "BTCUSDT",     
                 "positionSide": "BOTH",            // position side   
                 "positionAmt": "1.000",    
                 "unrealizedProfit": "0.00000000",  // unrealized profit        
                 "isolatedMargin": "0.00000000",	  
                 "notional": "0",  
                 "isolatedWallet": "0",  
                 "initialMargin": "0",              // initial margin required with current mark price   
                 "maintMargin": "0",                // maintenance margin required  
                 "updateTime": 0  
        	  }   
      	]  
      },  
      "rateLimits": [  
        {  
          "rateLimitType": "REQUEST_WEIGHT",  
          "interval": "MINUTE",  
          "intervalNum": 1,  
          "limit": 2400,  
          "count": 20  
        }  
      ]  
    }  
    

> Multi-Asset Mode
    
    
    {  
      "id": "605a6d20-6588-4cb9-afa0-b0ab087507ba",  
      "status": 200,  
      "result": {     
      	"totalInitialMargin": "0.00000000",            // the sum of USD value of all cross positions/open order initial margin  
      	"totalMaintMargin": "0.00000000",  	           // the sum of USD value of all cross positions maintenance margin  
      	"totalWalletBalance": "126.72469206",          // total wallet balance in USD  
      	"totalUnrealizedProfit": "0.00000000",         // total unrealized profit in USD  
      	"totalMarginBalance": "126.72469206",          // total margin balance in USD  
      	"totalPositionInitialMargin": "0.00000000",    // the sum of USD value of all cross positions initial margin  
      	"totalOpenOrderInitialMargin": "0.00000000",   // initial margin required for open orders with current mark price in USD  
      	"totalCrossWalletBalance": "126.72469206",     // crossed wallet balance in USD  
      	"totalCrossUnPnl": "0.00000000",	           // unrealized profit of crossed positions in USD  
      	"availableBalance": "126.72469206",            // available balance in USD  
      	"maxWithdrawAmount": "126.72469206"            // maximum virtual amount for transfer out in USD  
      	"assets": [  
      		{  
      			"asset": "USDT",			         // asset name  
      			"walletBalance": "23.72469206",      // wallet balance  
      			"unrealizedProfit": "0.00000000",    // unrealized profit  
      			"marginBalance": "23.72469206",      // margin balance  
      			"maintMargin": "0.00000000",	     // maintenance margin required  
      			"initialMargin": "0.00000000",       // total initial margin required with current mark price   
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
       	"positions": [  // positions of all symbols user had position are returned  
                          // only "BOTH" positions will be returned with One-way mode  
      		            // only "LONG" and "SHORT" positions will be returned with Hedge mode  
         	  {  
                 "symbol": "BTCUSDT",     
                 "positionSide": "BOTH",            // position side   
                 "positionAmt": "1.000",    
                 "unrealizedProfit": "0.00000000",  // unrealized profit        
                 "isolatedMargin": "0.00000000",	  
                 "notional": "0",  
                 "isolatedWallet": "0",  
                 "initialMargin": "0",              // initial margin required with current mark price   
                 "maintMargin": "0",                // maintenance margin required  
                 "updateTime": 0  
        	  }   
      	]   
      },  
      "rateLimits": [  
        {  
          "rateLimitType": "REQUEST_WEIGHT",  
          "interval": "MINUTE",  
          "intervalNum": 1,  
          "limit": 2400,  
          "count": 20  
        }  
      ]  
    }

---

# 账户信息V2 (USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/account/websocket-api/Account-Information-V2#接口描述 "接口描述的直接链接")

现有账户信息。 用户在单资产模式和多资产模式下会看到不同结果，响应部分的注释解释了两种模式下的不同。

## 方式[​](/docs/zh-CN/derivatives/usds-margined-futures/account/websocket-api/Account-Information-V2#方式 "方式的直接链接")

`v2/account.status`

## 请求[​](/docs/zh-CN/derivatives/usds-margined-futures/account/websocket-api/Account-Information-V2#请求 "请求的直接链接")
    
    
    {  
        "id": "605a6d20-6588-4cb9-afa0-b0ab087507ba",  
        "method": "v2/account.status",  
        "params": {  
            "apiKey": "xTaDyrmvA9XT2oBHHjy39zyPzKCvMdtH3b9q4xadkAg2dNSJXQGCxzui26L823W2",  
            "timestamp": 1702620814781,  
            "signature": "6bb98ef84170c70ba3d01f44261bfdf50fef374e551e590de22b5c3b729b1d8c"  
        }  
    }  
    

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/account/websocket-api/Account-Information-V2#请求权重 "请求权重的直接链接")

**5**

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/account/websocket-api/Account-Information-V2#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/account/websocket-api/Account-Information-V2#响应示例 "响应示例的直接链接")

> 单资产模式
    
    
    {  
      "id": "605a6d20-6588-4cb9-afa0-b0ab087507ba",  
      "status": 200,  
      "result": {     
    	"totalInitialMargin": "0.00000000",            // 当前所需起始保证金总额(存在逐仓请忽略), 仅计算usdt资产positions), only for USDT asset  
    	"totalMaintMargin": "0.00000000",  	           // 维持保证金总额, 仅计算usdt资产  
    	"totalWalletBalance": "103.12345678",          // 账户总余额, 仅计算usdt资产  
    	"totalUnrealizedProfit": "0.00000000",         // 持仓未实现盈亏总额, 仅计算usdt资产  
    	"totalMarginBalance": "103.12345678",          // 保证金总余额, 仅计算usdt资产  
    	"totalPositionInitialMargin": "0.00000000",    // 持仓所需起始保证金(基于最新标记价格), 仅计算usdt资产  
    	"totalOpenOrderInitialMargin": "0.00000000",   // 当前挂单所需起始保证金(基于最新标记价格), 仅计算usdt资产  
    	"totalCrossWalletBalance": "103.12345678",     // 全仓账户余额, 仅计算usdt资产  
    	"totalCrossUnPnl": "0.00000000",	           // 全仓持仓未实现盈亏总额, 仅计算usdt资产  
    	"availableBalance": "103.12345678",            // 可用余额, 仅计算usdt资产  
    	"maxWithdrawAmount": "103.12345678"            // 最大可转出余额, 仅计算usdt资产  
    	"assets": [   
    		{  
    			"asset": "USDT",			            // 资产  
    			"walletBalance": "23.72469206",         // 余额  
    			"unrealizedProfit": "0.00000000",       // 未实现盈亏  
    			"marginBalance": "23.72469206",         // 保证金余额  
    			"maintMargin": "0.00000000",	        // 维持保证金  
    			"initialMargin": "0.00000000",          // 当前所需起始保证金  
    			"positionInitialMargin": "0.00000000",  // 持仓所需起始保证金(基于最新标记价格)  
    			"openOrderInitialMargin": "0.00000000", // 当前挂单所需起始保证金(基于最新标记价格)  
    			"crossWalletBalance": "23.72469206",    // 全仓账户余额  
    			"crossUnPnl": "0.00000000"              // 全仓持仓未实现盈亏  
    			"availableBalance": "23.72469206",      // 可用余额  
    			"maxWithdrawAmount": "23.72469206",     // 最大可转出余额  
    			"updateTime": 1625474304765             // 更新时间  
    		},     
    		{  
    			"asset": "USDC",			            
    			"walletBalance": "103.12345678",        
    			"unrealizedProfit": "0.00000000",       
    			"marginBalance": "103.12345678",        
    			"maintMargin": "0.00000000",	       
    			"initialMargin": "0.00000000",     
    			"positionInitialMargin": "0.00000000",     
    			"openOrderInitialMargin": "0.00000000",    
    			"crossWalletBalance": "103.12345678",      
    			"crossUnPnl": "0.00000000"        
    			"availableBalance": "126.72469206",   
    			"maxWithdrawAmount": "103.12345678",   
    			"updateTime": 1625474304765   
    		}  
        ],  
    	"positions": [  // 仅有仓位或挂单的交易对会被返回  
    		            // 根据用户持仓模式展示持仓方向，即单向模式下只返回BOTH持仓情况，双向模式下只返回 LONG 和 SHORT 持仓情况  
       	  {  
               "symbol": "BTCUSDT",               // 交易对  
               "positionSide": "BOTH",            // 持仓方向  
               "positionAmt": "1.000",            // 持仓数量  
               "unrealizedProfit": "0.00000000",  // 持仓未实现盈亏     
               "isolatedMargin": "0.00000000",	  
               "notional": "0",  
               "isolatedWallet": "0",  
               "initialMargin": "0",              // 持仓所需起始保证金(基于最新标记价格)  
               "maintMargin": "0",                // 当前杠杆下用户可用的最大名义价值  
               "updateTime": 0                    // 更新时间   
      	  }   
    	]  
      },  
      "rateLimits": [  
        {  
          "rateLimitType": "REQUEST_WEIGHT",  
          "interval": "MINUTE",  
          "intervalNum": 1,  
          "limit": 2400,  
          "count": 20  
        }  
      ]  
    }  
    

> 多资产模式
    
    
    {  
      "id": "605a6d20-6588-4cb9-afa0-b0ab087507ba",  
      "status": 200,  
      "result": {     
    	"totalInitialMargin": "0.00000000",          // 以USD计价的所需起始保证金总额  
    	"totalMaintMargin": "0.00000000",  	         // 以USD计价的维持保证金总额  
    	"totalWalletBalance": "126.72469206",        // 以USD计价的账户总余额  
    	"totalUnrealizedProfit": "0.00000000",       // 以USD计价的持仓未实现盈亏总额  
    	"totalMarginBalance": "126.72469206",        // 以USD计价的保证金总余额   
    	"totalPositionInitialMargin": "0.00000000",  // 以USD计价的持仓所需起始保证金(基于最新标记价格)  
    	"totalOpenOrderInitialMargin": "0.00000000", // 以USD计价的当前挂单所需起始保证金(基于最新标记价格)  
    	"totalCrossWalletBalance": "126.72469206",   // 以USD计价的全仓账户余额  
    	"totalCrossUnPnl": "0.00000000",	         // 以USD计价的全仓持仓未实现盈亏总额  
    	"availableBalance": "126.72469206",          // 以USD计价的可用余额  
    	"maxWithdrawAmount": "126.72469206"          // 以USD计价的最大可转出余额  
    	"assets": [  
    		{  
    			"asset": "USDT",			            // 资产  
    			"walletBalance": "23.72469206",         // 余额  
    			"unrealizedProfit": "0.00000000",       // 未实现盈亏  
    			"marginBalance": "23.72469206",         // 保证金余额  
    			"maintMargin": "0.00000000",	        // 维持保证金  
    			"initialMargin": "0.00000000",          // 当前所需起始保证金  
    			"positionInitialMargin": "0.00000000",  // 持仓所需起始保证金(基于最新标记价格)  
    			"openOrderInitialMargin": "0.00000000", // 当前挂单所需起始保证金(基于最新标记价格)  
    			"crossWalletBalance": "23.72469206",    // 全仓账户余额  
    			"crossUnPnl": "0.00000000"              // 全仓持仓未实现盈亏  
    			"availableBalance": "23.72469206",      // 可用余额  
    			"maxWithdrawAmount": "23.72469206",     // 最大可转出余额  
    			"updateTime": 1625474304765             // 更新时间  
    		},     
    		{  
    			"asset": "USDC",			            
    			"walletBalance": "103.12345678",        
    			"unrealizedProfit": "0.00000000",       
    			"marginBalance": "103.12345678",        
    			"maintMargin": "0.00000000",	       
    			"initialMargin": "0.00000000",     
    			"positionInitialMargin": "0.00000000",     
    			"openOrderInitialMargin": "0.00000000",    
    			"crossWalletBalance": "103.12345678",      
    			"crossUnPnl": "0.00000000"        
    			"availableBalance": "126.72469206",   
    			"maxWithdrawAmount": "103.12345678",   
    			"updateTime": 1625474304765   
    		}  
    	],  
    	"positions": [  // 仅有仓位或挂单的交易对会被返回  
    		            // 根据用户持仓模式展示持仓方向，即单向模式下只返回BOTH持仓情况，双向模式下只返回 LONG 和 SHORT 持仓情况  
       	  {  
               "symbol": "BTCUSDT",               // 交易对  
               "positionSide": "BOTH",            // 持仓方向  
               "positionAmt": "1.000",            // 持仓数量  
               "unrealizedProfit": "0.00000000",  // 持仓未实现盈亏     
               "isolatedMargin": "0.00000000",	  
               "notional": "0",  
               "isolatedWallet": "0",  
               "initialMargin": "0",              // 持仓所需起始保证金(基于最新标记价格)  
               "maintMargin": "0",                // 当前杠杆下用户可用的最大名义价值  
               "updateTime": 0                    // 更新时间   
      	  }   
    	]  
      },  
      "rateLimits": [  
        {  
          "rateLimitType": "REQUEST_WEIGHT",  
          "interval": "MINUTE",  
          "intervalNum": 1,  
          "limit": 2400,  
          "count": 20  
        }  
      ]  
    }