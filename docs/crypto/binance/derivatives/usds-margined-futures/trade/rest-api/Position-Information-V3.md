---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Position-Information-V3
api_type: Trading
updated_at: 2026-01-15T23:47:27.038137
---

# Position Information V3 (USER_DATA)

## API Description[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Position-Information-V3#api-description "Direct link to API Description")

Get current position information(only symbol that has position or open orders will be returned).

## HTTP Request[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Position-Information-V3#http-request "Direct link to HTTP Request")

GET `/fapi/v3/positionRisk`

## Request Weight[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Position-Information-V3#request-weight "Direct link to Request Weight")

**5**

## Request Parameters[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Position-Information-V3#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| NO|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
**Note**

> Please use with user data stream `ACCOUNT_UPDATE` to meet your timeliness and accuracy needs.

## Response Example[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Position-Information-V3#response-example "Direct link to Response Example")

> For One-way position mode:
    
    
    [  
      {  
            "symbol": "ADAUSDT",  
            "positionSide": "BOTH",               // position side   
            "positionAmt": "30",  
            "entryPrice": "0.385",  
            "breakEvenPrice": "0.385077",  
            "markPrice": "0.41047590",  
            "unRealizedProfit": "0.76427700",     // unrealized profit    
            "liquidationPrice": "0",  
            "isolatedMargin": "0",  
            "notional": "12.31427700",  
            "marginAsset": "USDT",  
            "isolatedWallet": "0",  
            "initialMargin": "0.61571385",        // initial margin required with current mark price   
            "maintMargin": "0.08004280",          // maintenance margin required  
            "positionInitialMargin": "0.61571385",// initial margin required for positions with current mark price  
            "openOrderInitialMargin": "0",        // initial margin required for open orders with current mark price   
            "adl": 2,  
            "bidNotional": "0",                   // bids notional, ignore  
            "askNotional": "0",                   // ask notional, ignore  
            "updateTime": 1720736417660  
      }  
    ]  
    

> For Hedge position mode:
    
    
    [  
      {  
            "symbol": "ADAUSDT",  
            "positionSide": "LONG",               // position side   
            "positionAmt": "30",  
            "entryPrice": "0.385",  
            "breakEvenPrice": "0.385077",  
            "markPrice": "0.41047590",  
            "unRealizedProfit": "0.76427700",     // unrealized profit    
            "liquidationPrice": "0",  
            "isolatedMargin": "0",  
            "notional": "12.31427700",  
            "marginAsset": "USDT",  
            "isolatedWallet": "0",  
            "initialMargin": "0.61571385",        // initial margin required with current mark price   
            "maintMargin": "0.08004280",          // maintenance margin required  
            "positionInitialMargin": "0.61571385",// initial margin required for positions with current mark price  
            "openOrderInitialMargin": "0",        // initial margin required for open orders with current mark price   
            "adl": 2,  
            "bidNotional": "0",                   // bids notional, ignore  
            "askNotional": "0",                   // ask notional, ignore  
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
    ]

---

# 用户持仓风险V3 (USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Position-Information-V3#接口描述 "接口描述的直接链接")

查询持仓风险，仅返回有持仓或挂单的交易对

## HTTP请求[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Position-Information-V3#http请求 "HTTP请求的直接链接")

GET `/fapi/v3/positionRisk`

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Position-Information-V3#请求权重 "请求权重的直接链接")

**5**

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Position-Information-V3#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| NO|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
**注意**

>   * 请与账户推送信息`ACCOUNT_UPDATE`配合使用，以满足您的及时性和准确性需求。
> 


## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Position-Information-V3#响应示例 "响应示例的直接链接")

> 单向持仓模式下：
    
    
    [  
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
    ]  
    

> 双向持仓模式下：
    
    
    [  
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
    ]