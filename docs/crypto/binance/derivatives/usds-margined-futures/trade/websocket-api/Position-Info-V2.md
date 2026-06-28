---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/websocket-api/Position-Info-V2
api_type: WebSocket
updated_at: 2026-01-15T23:47:37.606102
---

# Position Information V2 (USER_DATA)

## API Description[​](/docs/derivatives/usds-margined-futures/trade/websocket-api/Position-Info-V2#api-description "Direct link to API Description")

Get current position information(only symbol that has position or open orders will be returned).

## Method[​](/docs/derivatives/usds-margined-futures/trade/websocket-api/Position-Info-V2#method "Direct link to Method")

`v2/account.position`

## Request[​](/docs/derivatives/usds-margined-futures/trade/websocket-api/Position-Info-V2#request "Direct link to Request")
    
    
    {  
       	"id": "605a6d20-6588-4cb9-afa0-b0ab087507ba",  
        "method": "v2/account.position",  
        "params": {  
            "apiKey": "xTaDyrmvA9XT2oBHHjy39zyPzKCvMdtH3b9q4xadkAg2dNSJXQGCxzui26L823W2",  
            "symbol": "BTCUSDT",  
            "timestamp": 1702920680303,  
            "signature": "31ab02a51a3989b66c29d40fcdf78216978a60afc6d8dc1c753ae49fa3164a2a"  
        }  
    }  
    

## Request Weight[​](/docs/derivatives/usds-margined-futures/trade/websocket-api/Position-Info-V2#request-weight "Direct link to Request Weight")

**5**

## Request Parameters[​](/docs/derivatives/usds-margined-futures/trade/websocket-api/Position-Info-V2#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| NO|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
**Note**

>   * Please use with user data stream `ACCOUNT_UPDATE` to meet your timeliness and accuracy needs.
> 


## Response Example[​](/docs/derivatives/usds-margined-futures/trade/websocket-api/Position-Info-V2#response-example "Direct link to Response Example")

> For One-way position mode:
    
    
    {  
      "id": "605a6d20-6588-4cb9-afa0-b0ab087507ba",  
      "status": 200,  
      "result": [  
        {  
    	    "symbol": "BTCUSDT",    
    	    "positionSide": "BOTH",            // 持仓方向  
    	    "positionAmt": "1.000",    
    	    "entryPrice": "0.00000",  
    	    "breakEvenPrice": "0.0",    
    	    "markPrice": "6679.50671178",  
    	    "unrealizedProfit": "0.00000000",  // 持仓未实现盈亏   
    	    "liquidationPrice": "0",    
    	    "isolatedMargin": "0.00000000",	  
    	    "notional": "0",  
    	    "marginAsset": "USDT",   
    	    "isolatedWallet": "0",  
    	    "initialMargin": "0",              // 初始保证金  
    	    "maintMargin": "0",                // 维持保证金  
    	    "positionInitialMargin": "0",      // 仓位初始保证金  
    	    "openOrderInitialMargin": "0",     // 订单初始保证金  
    	    "adl": 0,  
    	    "bidNotional": "0",    
    	    "askNotional": "0",    
    	    "updateTime": 0                    // 更新时间  
        }  
    ],  
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
    

> For Hedge position mode:
    
    
    {  
      "id": "605a6d20-6588-4cb9-afa0-b0ab087507ba",  
      "status": 200,  
      "result": [  
       {  
    	    "symbol": "BTCUSDT",    
    	    "positionSide": "LONG",              
    	    "positionAmt": "1.000",    
    	    "entryPrice": "0.00000",  
    	    "breakEvenPrice": "0.0",    
    	    "markPrice": "6679.50671178",  
    	    "unrealizedProfit": "0.00000000",    
    	    "liquidationPrice": "0",    
    	    "isolatedMargin": "0.00000000",	  
    	    "notional": "0",  
    	    "marginAsset": "USDT",   
    	    "isolatedWallet": "0",  
    	    "initialMargin": "0",     
    	    "maintMargin": "0",      
    	    "positionInitialMargin": "0",        
    	    "openOrderInitialMargin": "0",       
    	    "adl": 0,  
    	    "bidNotional": "0",    
    	    "askNotional": "0",    
    	    "updateTime": 0  
        },  
        {  
    	    "symbol": "BTCUSDT",    
    	    "positionSide": "SHORT",             
    	    "positionAmt": "1.000",    
    	    "entryPrice": "0.00000",  
    	    "breakEvenPrice": "0.0",    
    	    "markPrice": "6679.50671178",  
    	    "unrealizedProfit": "0.00000000",    
    	    "liquidationPrice": "0",    
    	    "isolatedMargin": "0.00000000",	  
    	    "notional": "0",  
    	    "marginAsset": "USDT",   
    	    "isolatedWallet": "0",  
    	    "initialMargin": "0",     
    	    "maintMargin": "0",       
    	    "positionInitialMargin": "0",        
    	    "openOrderInitialMargin": "0",       
    	    "adl": 0,  
    	    "bidNotional": "0",    
    	    "askNotional": "0",   
    	    "updateTime": 0  
        }  
      ],  
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

# 用户持仓风险V2 (USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/websocket-api/Position-Info-V2#接口描述 "接口描述的直接链接")

查询持仓风险，仅返回有仓位或挂单的交易对

## 方式[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/websocket-api/Position-Info-V2#方式 "方式的直接链接")

`v2/account.position`

## 请求[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/websocket-api/Position-Info-V2#请求 "请求的直接链接")
    
    
    {  
       	"id": "605a6d20-6588-4cb9-afa0-b0ab087507ba",  
        "method": "v2/account.position",  
        "params": {  
            "apiKey": "xTaDyrmvA9XT2oBHHjy39zyPzKCvMdtH3b9q4xadkAg2dNSJXQGCxzui26L823W2",  
            "symbol": "BTCUSDT",  
            "timestamp": 1702920680303,  
            "signature": "31ab02a51a3989b66c29d40fcdf78216978a60afc6d8dc1c753ae49fa3164a2a"  
        }  
    }  
    

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/websocket-api/Position-Info-V2#请求权重 "请求权重的直接链接")

**5**

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/websocket-api/Position-Info-V2#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| NO|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
**注意**

>   * 请与账户推送信息`ACCOUNT_UPDATE`配合使用，以满足您的及时性和准确性需求。
> 


## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/websocket-api/Position-Info-V2#响应示例 "响应示例的直接链接")

> 单向持仓模式下：
    
    
    {  
      "id": "605a6d20-6588-4cb9-afa0-b0ab087507ba",  
      "status": 200,  
      "result":[  
        {  
            "symbol": "ADAUSDT",  
            "positionSide": "BOTH",               // 持仓方向  
            "positionAmt": "30",  
            "entryPrice": "0.385",  
            "breakEvenPrice": "0.385077",  
            "markPrice": "0.41047590",  
            "unRealizedProfit": "0.76427700",     // 持仓未实现盈亏   
            "liquidationPrice": "0",  
            "isolatedMargin": "0",  
            "notional": "12.31427700",  
            "marginAsset": "USDT",  
            "isolatedWallet": "0",  
            "initialMargin": "0.61571385",        // 初始保证金  
            "maintMargin": "0.08004280",          // 维持保证金  
            "positionInitialMargin": "0.61571385",// 仓位初始保证金  
            "openOrderInitialMargin": "0",        // 订单初始保证金  
            "adl": 2,  
            "bidNotional": "0",                     
            "askNotional": "0",                     
            "updateTime": 1720736417660           // 更新时间  
        }  
      ],  
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
    

> 双向持仓模式下：
    
    
    {  
      "id": "605a6d20-6588-4cb9-afa0-b0ab087507ba",  
      "status": 200,  
      "result": [  
      {  
            "symbol": "ADAUSDT",  
            "positionSide": "LONG",                 
            "positionAmt": "30",  
            "entryPrice": "0.385",  
            "breakEvenPrice": "0.385077",  
            "markPrice": "0.41047590",  
            "unRealizedProfit": "0.76427700",      
            "liquidationPrice": "0",  
            "isolatedMargin": "0",  
            "notional": "12.31427700",  
            "marginAsset": "USDT",  
            "isolatedWallet": "0",  
            "initialMargin": "0.61571385",          
            "maintMargin": "0.08004280",            
            "positionInitialMargin": "0.61571385",  
            "openOrderInitialMargin": "0",         
            "adl": 2,  
            "bidNotional": "0",                    
            "askNotional": "0",                  
            "updateTime": 1720736417660  
      },  
      {  
            "symbol": "COMPUSDT",  
            "positionSide": "SHORT",  
            "positionAmt": "-1.000",  
            "entryPrice": "70.92841",  
            "breakEvenPrice": "70.900038636",  
            "markPrice": "49.72023376",  
            "unRealizedProfit": "21.20817624",  
            "liquidationPrice": "2260.56757210",  
            "isolatedMargin": "0",  
            "notional": "-49.72023376",  
            "marginAsset": "USDT",  
            "isolatedWallet": "0",  
            "initialMargin": "2.48601168",  
            "maintMargin": "0.49720233",  
            "positionInitialMargin": "2.48601168",  
            "openOrderInitialMargin": "0",  
            "adl": 2,  
            "bidNotional": "0",  
            "askNotional": "0",  
            "updateTime": 1708943511656  
      }  
      ],  
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