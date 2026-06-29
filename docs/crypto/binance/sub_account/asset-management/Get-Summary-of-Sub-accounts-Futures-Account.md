---
exchange: binance
source_url: https://developers.binance.com/docs/sub_account/asset-management/Get-Summary-of-Sub-accounts-Futures-Account
api_type: Account
updated_at: 2026-06-29 19:14:33.227185
---

# Get Summary of Sub-account's Futures Account (For Master Account) (USER_DATA)

## API Description[​](/docs/sub_account/asset-management/Get-Summary-of-Sub-accounts-Futures-Account#api-description "Direct link to API Description")

Get Summary of Sub-account's Futures Account

## HTTP Request[​](/docs/sub_account/asset-management/Get-Summary-of-Sub-accounts-Futures-Account#http-request "Direct link to HTTP Request")

GET `/sapi/v1/sub-account/futures/accountSummary`

## Request Weight(IP)[​](/docs/sub_account/asset-management/Get-Summary-of-Sub-accounts-Futures-Account#request-weightip "Direct link to Request Weight\(IP\)")

**1**

## Request Parameters[​](/docs/sub_account/asset-management/Get-Summary-of-Sub-accounts-Futures-Account#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
page| INT| YES| default:1  
limit| INT| YES| default:20  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/sub_account/asset-management/Get-Summary-of-Sub-accounts-Futures-Account#response-example "Direct link to Response Example")
    
    
    {  
        "totalInitialMargin": "9.83137400",   
        "totalMaintenanceMargin": "0.41568700",   
        "totalMarginBalance": "23.03235621",   
        "totalOpenOrderInitialMargin": "9.00000000",  
        "totalPositionInitialMargin": "0.83137400",  
        "totalUnrealizedProfit": "0.03219710",  
        "totalWalletBalance": "22.15879444",  
        "asset": "USD",  // The sum of BUSD and USDT  
        "subAccountList":[  
            {  
                "email": "123@test.com",  
                "totalInitialMargin": "9.00000000",   
                "totalMaintenanceMargin": "0.00000000",   
                "totalMarginBalance": "22.12659734",   
                "totalOpenOrderInitialMargin": "9.00000000",  
                "totalPositionInitialMargin": "0.00000000",  
                "totalUnrealizedProfit": "0.00000000",  
                "totalWalletBalance": "22.12659734",  
                "asset": "USD" //The sum of BUSD and USDT  
            },  
            {   
                "email": "345@test.com",  
                "totalInitialMargin": "0.83137400",   
                "totalMaintenanceMargin": "0.41568700",   
                "totalMarginBalance": "0.90575887",   
                "totalOpenOrderInitialMargin": "0.00000000",  
                "totalPositionInitialMargin": "0.83137400",  
                "totalUnrealizedProfit": "0.03219710",  
                "totalWalletBalance": "0.87356177",  
                "asset": "USD"  
            }  
        ]  
    }

---

# 查询子账户Futures账户汇总 (适用主账户) (USER_DATA)

## 接口描述[​](/docs/zh-CN/sub_account/asset-management/Get-Summary-of-Sub-accounts-Futures-Account#接口描述 "接口描述的直接链接")

查询子账户Futures账户汇总

## HTTP请求[​](/docs/zh-CN/sub_account/asset-management/Get-Summary-of-Sub-accounts-Futures-Account#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/sub-account/futures/accountSummary`

## 请求权重(IP)[​](/docs/zh-CN/sub_account/asset-management/Get-Summary-of-Sub-accounts-Futures-Account#请求权重ip "请求权重\(IP\)的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/sub_account/asset-management/Get-Summary-of-Sub-accounts-Futures-Account#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
page| INT| YES| 默认:1  
limit| INT| YES| 默认:20  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/sub_account/asset-management/Get-Summary-of-Sub-accounts-Futures-Account#响应示例 "响应示例的直接链接")
    
    
    {  
        "totalInitialMargin": "9.83137400",   
        "totalMaintenanceMargin": "0.41568700",   
        "totalMarginBalance": "23.03235621",   
        "totalOpenOrderInitialMargin": "9.00000000",  
        "totalPositionInitialMargin": "0.83137400",  
        "totalUnrealizedProfit": "0.03219710",  
        "totalWalletBalance": "22.15879444",  
        "asset": "USD",  //USDT和BUSD资产汇总  
        "subAccountList":[  
            {  
                "email": "123@test.com",  
                "totalInitialMargin": "9.00000000",   
                "totalMaintenanceMargin": "0.00000000",   
                "totalMarginBalance": "22.12659734",   
                "totalOpenOrderInitialMargin": "9.00000000",  
                "totalPositionInitialMargin": "0.00000000",  
                "totalUnrealizedProfit": "0.00000000",  
                "totalWalletBalance": "22.12659734",  
                "asset": "USD"  //USDT和BUSD资产汇总  
            },  
            {   
                "email": "345@test.com",  
                "totalInitialMargin": "0.83137400",   
                "totalMaintenanceMargin": "0.41568700",  
                "totalMarginBalance": "0.90575887",  
                "totalOpenOrderInitialMargin": "0.00000000",  
                "totalPositionInitialMargin": "0.83137400",  
                "totalUnrealizedProfit": "0.03219710",  
                "totalWalletBalance": "0.87356177",  
                "asset": "USD"  
            }  
        ]  
    }