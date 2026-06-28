---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin/account/Get-CM-Account-Detail
api_type: Account
updated_at: 2026-01-15T23:44:46.650133
---

# Get CM Account Detail(USER_DATA)

## API Description[​](/docs/derivatives/portfolio-margin/account/Get-CM-Account-Detail#api-description "Direct link to API Description")

Get current CM account asset and position information.

## HTTP Request[​](/docs/derivatives/portfolio-margin/account/Get-CM-Account-Detail#http-request "Direct link to HTTP Request")

GET `/papi/v1/cm/account`

## Request Weight[​](/docs/derivatives/portfolio-margin/account/Get-CM-Account-Detail#request-weight "Direct link to Request Weight")

**5**

## Request Parameters[​](/docs/derivatives/portfolio-margin/account/Get-CM-Account-Detail#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/derivatives/portfolio-margin/account/Get-CM-Account-Detail#response-example "Direct link to Response Example")
    
    
    {  
        "assets": [  
            {  
                "asset": "BTC",  // asset name   
                "crossWalletBalance": "0.00241969",  // total wallet balance  
                "crossUnPnl": "0.00000000",  // unrealized profit or loss  
                "maintMargin": "0.00000000",    // maintenance margin  
                "initialMargin": "0.00000000",  // total intial margin required with the latest mark price  
                "positionInitialMargin": "0.00000000",  // positions" margin required with the latest mark price  
                "openOrderInitialMargin": "0.00000000",  // open orders" intial margin required with the latest mark price  
                "updateTime": 1625474304765 // last update time    
             }  
         ],  
         "positions": [  
             {  
                "symbol": "BTCUSD_201225",  
                "positionAmt":"0",  // position amount  
                "initialMargin": "0",  
                "maintMargin": "0",  
                "unrealizedProfit": "0.00000000",  
                "positionInitialMargin": "0",  
                "openOrderInitialMargin": "0",  
                "leverage": "125",  
                "positionSide": "BOTH", // BOTH means that it is the position of One-way Mode    
                "entryPrice": "0.0",  
                "maxQty": "50",  // maximum quantity of base asset  
                "updateTime": 0  
            }  
         ]  
    }

---

# 获取CM账户信息(USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-CM-Account-Detail#接口描述 "接口描述的直接链接")

获取现有CM账户资产和仓位信息

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-CM-Account-Detail#http请求 "HTTP请求的直接链接")

GET `/papi/v1/cm/account`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-CM-Account-Detail#请求权重 "请求权重的直接链接")

**5**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-CM-Account-Detail#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-CM-Account-Detail#响应示例 "响应示例的直接链接")
    
    
    {  
        "assets": [  
            {  
                "asset": "BTC",  // 资产  
                "crossWalletBalance": "0.00241969",  // 全仓账户余额  
                "crossUnPnl": "0.00000000",  // 全仓持仓未实现盈亏  
                "maintMargin": "0.00000000",    // 维持保证金  
                "initialMargin": "0.00000000",  // 当前所需起始保证金  
                "positionInitialMargin": "0.00000000",  // 持仓所需起始保证金(基于最新标记价格)  
                "openOrderInitialMargin": "0.00000000",  // 当前挂单所需起始保证金(基于最新标记价格)e  
                "updateTime": 1625474304765 // 更新时间  
             }  
         ],  
         "positions": [  
             {  
                "symbol": "BTCUSD_201225",  
                "positionAmt":"0",    
                "initialMargin": "0",  
                "maintMargin": "0",  
                "unrealizedProfit": "0.00000000",  
                "positionInitialMargin": "0",  
                "openOrderInitialMargin": "0",  
                "leverage": "125",  
                "positionSide": "BOTH",  
                "entryPrice": "0.0",  
                "maxQty": "50",    
                "updateTime": 0  
            }  
         ]  
    }