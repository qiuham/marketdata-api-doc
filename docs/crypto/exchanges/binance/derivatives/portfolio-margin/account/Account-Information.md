---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin/account/Account-Information
api_type: Account
updated_at: 2026-01-15T23:44:31.925192
---

# Account Information(USER_DATA)

## API Description[​](/docs/derivatives/portfolio-margin/account/Account-Information#api-description "Direct link to API Description")

Query account information

## HTTP Request[​](/docs/derivatives/portfolio-margin/account/Account-Information#http-request "Direct link to HTTP Request")

GET `/papi/v1/account`

## Request Weight[​](/docs/derivatives/portfolio-margin/account/Account-Information#request-weight "Direct link to Request Weight")

**20**

## Request Parameters[​](/docs/derivatives/portfolio-margin/account/Account-Information#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/derivatives/portfolio-margin/account/Account-Information#response-example "Direct link to Response Example")
    
    
    {  
       "uniMMR": "5167.92171923",        // Portfolio margin account maintenance margin rate  
       "accountEquity": "122607.35137903",   // Account equity, in USD value  
       "actualEquity": "73.47428058",   //Account equity without collateral rate, in USD value  
       "accountInitialMargin": "23.72469206",   
       "accountMaintMargin": "23.72469206", // Portfolio margin account maintenance margin, unit：USD  
       "accountStatus": "NORMAL"   // Portfolio margin account status:"NORMAL", "MARGIN_CALL", "SUPPLY_MARGIN", "REDUCE_ONLY", "ACTIVE_LIQUIDATION", "FORCE_LIQUIDATION", "BANKRUPTED"  
       "virtualMaxWithdrawAmount": "1627523.32459208"   // Portfolio margin maximum amount for transfer out in USD  
       "totalAvailableBalance":"",  
       "totalMarginOpenLoss":"", // in USD margin open order  
       "updateTime": 1657707212154 // last update time   
    }

---

# 查询账户信息(USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/account/Account-Information#接口描述 "接口描述的直接链接")

查询账户信息

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/account/Account-Information#http请求 "HTTP请求的直接链接")

GET `/papi/v1/account`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/account/Account-Information#请求权重 "请求权重的直接链接")

**20**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/account/Account-Information#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/account/Account-Information#响应示例 "响应示例的直接链接")
    
    
    {  
       "uniMMR": "5167.92171923",   // 统一账户维持保证金率  
       "accountEquity": "73.47428058",   // 以USD计价的账户权益  
       "actualEquity": "122607.35137903",   // 不考虑质押率的以USD计价账户权益  
       "accountInitialMargin": "23.72469206",   
       "accountMaintMargin": "23.72469206", // 以USD计价统一账户维持保证金  
       "accountStatus": "NORMAL"   // 统一账户账户状态："NORMAL", "MARGIN_CALL", "SUPPLY_MARGIN", "REDUCE_ONLY", "ACTIVE_LIQUIDATION", "FORCE_LIQUIDATION", "BANKRUPTED"  
       "virtualMaxWithdrawAmount": "1627523.32459208"  // 以USD计价的最大可转出  
       "totalAvailableBalance":"",  
       "totalMarginOpenLoss":"",   
       "updateTime": 1657707212154 // 更新时间   
    }