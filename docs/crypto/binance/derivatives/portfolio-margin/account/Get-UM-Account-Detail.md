---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin/account/Get-UM-Account-Detail
api_type: Account
updated_at: 2026-01-15T23:44:58.545297
---

# Get UM Account Detail(USER_DATA)

## API Description[​](/docs/derivatives/portfolio-margin/account/Get-UM-Account-Detail#api-description "Direct link to API Description")

Get current UM account asset and position information.

## HTTP Request[​](/docs/derivatives/portfolio-margin/account/Get-UM-Account-Detail#http-request "Direct link to HTTP Request")

GET `/papi/v1/um/account`

## Request Weight[​](/docs/derivatives/portfolio-margin/account/Get-UM-Account-Detail#request-weight "Direct link to Request Weight")

**5**

## Request Parameters[​](/docs/derivatives/portfolio-margin/account/Get-UM-Account-Detail#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/derivatives/portfolio-margin/account/Get-UM-Account-Detail#response-example "Direct link to Response Example")
    
    
    {     
        "assets": [  
            {  
                "asset": "USDT",            // asset name  
                "crossWalletBalance": "23.72469206",      // wallet balance  
                "crossUnPnl": "0.00000000",    // unrealized profit  
                "maintMargin": "0.00000000",        // maintenance margin required  
                "initialMargin": "0.00000000",    // total initial margin required with current mark price   
                "positionInitialMargin": "0.00000000",    //initial margin required for positions with current mark price  
                "openOrderInitialMargin": "0.00000000",   // initial margin required for open orders with current mark price  
                "updateTime": 1625474304765 // last update time   
            }  
        ],  
        "positions": [  // positions of all symbols in the market are returned  
            // only "BOTH" positions will be returned with One-way mode  
            // only "LONG" and "SHORT" positions will be returned with Hedge mode  
            {  
                "symbol": "BTCUSDT",    // symbol name  
                "initialMargin": "0",   // initial margin required with current mark price   
                "maintMargin": "0",     // maintenance margin required  
                "unrealizedProfit": "0.00000000",  // unrealized profit  
                "positionInitialMargin": "0",      // initial margin required for positions with current mark price  
                "openOrderInitialMargin": "0",     // initial margin required for open orders with current mark price  
                "leverage": "100",      // current initial leverage  
                "entryPrice": "0.00000",    // average entry price  
                "maxNotional": "250000",    // maximum available notional with current leverage  
                "bidNotional": "0",  // bids notional, ignore  
                "askNotional": "0",  // ask notional, ignore  
                "positionSide": "BOTH",     // position side  
                "positionAmt": "0",         // position amount  
                "updateTime": 0           // last update time  
            }  
        ]  
    }

---

# 获取UM账户信息(USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-UM-Account-Detail#接口描述 "接口描述的直接链接")

现有UM账户资产和仓位信息

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-UM-Account-Detail#http请求 "HTTP请求的直接链接")

GET `/papi/v1/um/account`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-UM-Account-Detail#请求权重 "请求权重的直接链接")

**5**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-UM-Account-Detail#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-UM-Account-Detail#响应示例 "响应示例的直接链接")
    
    
    {     
        "assets": [  
            {  
                "asset": "USDT",            // 资产  
                "crossWalletBalance": "23.72469206",      // 全仓账户余额  
                "crossUnPnl": "0.00000000",    // 全仓持仓未实现盈亏  
                "maintMargin": "0.00000000",   // 维持保证金  
                "initialMargin": "0.00000000", // 当前所需起始保证金  
                "positionInitialMargin": "0.00000000",  //持仓所需起始保证金(基于最新标记价格)  
                "openOrderInitialMargin": "0.00000000", //当前挂单所需起始保证金(基于最新标记价格)  
                "updateTime": 1625474304765 // 更新时间  
            }  
        ],  
        "positions": [  // 头寸，将返回所有市场symbol。  
            //根据用户持仓模式展示持仓方向，即单向模式下只返回BOTH持仓情况，双向模式下只返回 LONG 和 SHORT 持仓情况  
            {  
                "symbol": "BTCUSDT",    // 交易对  
                "initialMargin": "0",   // 当前所需起始保证金(基于最新标记价格)  
                "maintMargin": "0",     // 维持保证金  
                "unrealizedProfit": "0.00000000",  // 持仓未实现盈亏  
                "positionInitialMargin": "0",      //持仓所需起始保证金(基于最新标记价格)  
                "openOrderInitialMargin": "0",     // 当前挂单所需起始保证金(基于最新标记价格)  
                "leverage": "100",      // 杠杆倍率  
                "entryPrice": "0.00000",    // 持仓成本价  
                "maxNotional": "250000",    // 当前杠杆下用户可用的最大名义价值  
                "bidNotional": "0",  // 买单净值，忽略  
                "askNotional": "0",  // 卖单净值，忽略  
                "positionSide": "BOTH",     // 持仓方向  
                "positionAmt": "0",         //  持仓数量  
                "updateTime": 0           // 更新时间  
            }  
        ]  
    }