---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Position-Information-V2
api_type: Trading
updated_at: 2026-01-15T23:47:26.972175
---

# Position Information V2 (USER_DATA)

## API Description[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Position-Information-V2#api-description "Direct link to API Description")

Get current position information.

## HTTP Request[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Position-Information-V2#http-request "Direct link to HTTP Request")

GET `/fapi/v2/positionRisk`

## Request Weight[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Position-Information-V2#request-weight "Direct link to Request Weight")

**5**

## Request Parameters[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Position-Information-V2#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| NO|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
**Note**

> Please use with user data stream `ACCOUNT_UPDATE` to meet your timeliness and accuracy needs.

## Response Example[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Position-Information-V2#response-example "Direct link to Response Example")

> For One-way position mode:
    
    
    [  
      	{  
      		"entryPrice": "0.00000",  
            "breakEvenPrice": "0.0",    
      		"marginType": "isolated",   
      		"isAutoAddMargin": "false",  
      		"isolatedMargin": "0.00000000",	  
      		"leverage": "10",   
      		"liquidationPrice": "0",   
      		"markPrice": "6679.50671178",	  
      		"maxNotionalValue": "20000000",   
      		"positionAmt": "0.000",  
      		"notional": "0",,   
      		"isolatedWallet": "0",  
      		"symbol": "BTCUSDT",   
      		"unRealizedProfit": "0.00000000",   
      		"positionSide": "BOTH",  
      		"updateTime": 0  
      	}  
    ]  
    

> For Hedge position mode:
    
    
    [  
        {  
            "symbol": "BTCUSDT",  
            "positionAmt": "0.001",  
            "entryPrice": "22185.2",  
            "breakEvenPrice": "0.0",    
            "markPrice": "21123.05052574",  
            "unRealizedProfit": "-1.06214947",  
            "liquidationPrice": "19731.45529116",  
            "leverage": "4",  
            "maxNotionalValue": "100000000",  
            "marginType": "cross",  
            "isolatedMargin": "0.00000000",  
            "isAutoAddMargin": "false",  
            "positionSide": "LONG",  
            "notional": "21.12305052",  
            "isolatedWallet": "0",  
            "updateTime": 1655217461579  
        },  
        {  
            "symbol": "BTCUSDT",  
            "positionAmt": "0.000",  
            "entryPrice": "0.0",  
            "breakEvenPrice": "0.0",    
            "markPrice": "21123.05052574",  
            "unRealizedProfit": "0.00000000",  
            "liquidationPrice": "0",  
            "leverage": "4",  
            "maxNotionalValue": "100000000",  
            "marginType": "cross",  
            "isolatedMargin": "0.00000000",  
            "isAutoAddMargin": "false",  
            "positionSide": "SHORT",  
            "notional": "0",  
            "isolatedWallet": "0",  
            "updateTime": 0  
        }  
    ]

---

# 用户持仓风险V2 (USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Position-Information-V2#接口描述 "接口描述的直接链接")

查询持仓风险

## HTTP请求[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Position-Information-V2#http请求 "HTTP请求的直接链接")

GET `/fapi/v2/positionRisk`

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Position-Information-V2#请求权重 "请求权重的直接链接")

**5**

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Position-Information-V2#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| NO|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
**注意**

>   * 请与账户推送信息`ACCOUNT_UPDATE`配合使用，以满足您的及时性和准确性需求。
> 


## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Position-Information-V2#响应示例 "响应示例的直接链接")

> 单向持仓模式下：
    
    
    [  
      	{  
      		"entryPrice": "0.00000", // 开仓均价  
    		"breakEvenPrice": "0.0",  // 盈亏平衡价  
      		"marginType": "isolated", // 逐仓模式或全仓模式  
      		"isAutoAddMargin": "false",  
      		"isolatedMargin": "0.00000000",	// 逐仓保证金  
      		"leverage": "10", // 当前杠杆倍数  
      		"liquidationPrice": "0", // 参考强平价格  
      		"markPrice": "6679.50671178",	// 当前标记价格  
      		"maxNotionalValue": "20000000", // 当前杠杆倍数允许的名义价值上限  
      		"positionAmt": "0.000", // 头寸数量，符号代表多空方向, 正数为多，负数为空  
      		"notional": "0",  
      		"isolatedWallet": "0",  
      		"symbol": "BTCUSDT", // 交易对  
      		"unRealizedProfit": "0.00000000", // 持仓未实现盈亏  
      		"positionSide": "BOTH", // 持仓方向  
      		"updateTime": 1625474304765   // 更新时间  
      	}  
    ]  
    

> 双向持仓模式下：
    
    
    [  
        {  
            "symbol": "BTCUSDT", // 交易对  
            "positionAmt": "0.001", // 头寸数量，符号代表多空方向, 正数为多，负数为空  
            "entryPrice": "22185.2", // 开仓均价  
    		"breakEvenPrice": "0.0",  // 盈亏平衡价  
            "markPrice": "21123.05052574", // 当前标记价格  
            "unRealizedProfit": "-1.06214947", // 持仓未实现盈亏  
            "liquidationPrice": "19731.45529116", // 参考强平价格  
            "leverage": "4", // 当前杠杆倍数  
            "maxNotionalValue": "100000000", // 当前杠杆倍数允许的名义价值上限  
            "marginType": "cross", // 逐仓模式或全仓模式  
            "isolatedMargin": "0.00000000", // 逐仓保证金  
            "isAutoAddMargin": "false",  
            "positionSide": "LONG", // 持仓方向  
            "notional": "21.12305052",  
            "isolatedWallet": "0",  
            "updateTime": 1655217461579 //更新时间  
        },  
        {  
            "symbol": "BTCUSDT",  
            "positionAmt": "0.000",  
            "entryPrice": "0.0",  
            "breakEvenPrice": "0.0",    
            "markPrice": "21123.05052574",  
            "unRealizedProfit": "0.00000000",  
            "liquidationPrice": "0",  
            "leverage": "4",  
            "maxNotionalValue": "100000000",  
            "marginType": "cross",  
            "isolatedMargin": "0.00000000",  
            "isAutoAddMargin": "false",  
            "positionSide": "SHORT",  
            "notional": "0",  
            "isolatedWallet": "0",  
            "updateTime": 0  
        }  
    ]