---
exchange: binance
source_url: https://developers.binance.com/docs/sub_account/asset-management/Get-Sub-account-Deposit-History
api_type: Account
updated_at: 2026-05-27 19:02:22.114701
---

# Get Summary of Sub-account's Futures Account V2 (For Master Account) (USER_DATA)

## API Description[​](/docs/sub_account/asset-management/Get-Summary-of-Sub-accounts-Futures-Account-V2#api-description "Direct link to API Description")

Get Summary of Sub-account's Futures Account

## HTTP Request[​](/docs/sub_account/asset-management/Get-Summary-of-Sub-accounts-Futures-Account-V2#http-request "Direct link to HTTP Request")

GET `/sapi/v2/sub-account/futures/accountSummary`

## Request Weight(IP)[​](/docs/sub_account/asset-management/Get-Summary-of-Sub-accounts-Futures-Account-V2#request-weightip "Direct link to Request Weight\(IP\)")

**10**

## Request Parameters[​](/docs/sub_account/asset-management/Get-Summary-of-Sub-accounts-Futures-Account-V2#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
futuresType| INT| YES| 1:USDT Margined Futures, 2:COIN Margined Futures  
page| INT| NO| default:1  
limit| INT| NO| default:10, max:20  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/sub_account/asset-management/Get-Summary-of-Sub-accounts-Futures-Account-V2#response-example "Direct link to Response Example")

> USDT Margined Futures：
    
    
    {  
      "futureAccountSummaryResp": {  
        "totalInitialMargin": "9.83137400",   
        "totalMaintenanceMargin": "0.41568700",   
        "totalMarginBalance": "23.03235621",   
        "totalOpenOrderInitialMargin": "9.00000000",  
        "totalPositionInitialMargin": "0.83137400",  
        "totalUnrealizedProfit": "0.03219710",  
        "totalWalletBalance": "22.15879444",  
        "asset": "USD",  //The sum of BUSD and USDT  
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
                "asset": "USD"  //The sum of BUSD and USDT  
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
    }  
    

> COIN Margined Futures：
    
    
    {  
      "deliveryAccountSummaryResp": {  
        "totalMarginBalanceOfBTC": "25.03221121",   
        "totalUnrealizedProfitOfBTC": "0.12233410",  
        "totalWalletBalanceOfBTC": "22.15879444",  
        "asset": "BTC",  
        "subAccountList":[  
            {  
                "email": "123@test.com",  
                "totalMarginBalance": "22.12659734",   
                "totalUnrealizedProfit": "0.00000000",  
                "totalWalletBalance": "22.12659734",  
                "asset": "BTC"  
            },  
            {   
                "email": "345@test.com",  
                "totalMarginBalance": "0.90575887",  
                "totalUnrealizedProfit": "0.03219710",  
                "totalWalletBalance": "0.87356177",  
                "asset": "BTC"  
            }  
        ]  
      }  
    }

---

# 查询子账户Futures账户汇总V2 (适用主账户) (USER_DATA)

## 接口描述[​](/docs/zh-CN/sub_account/asset-management/Get-Summary-of-Sub-accounts-Futures-Account-V2#接口描述 "接口描述的直接链接")

查询子账户Futures账户汇总

## HTTP请求[​](/docs/zh-CN/sub_account/asset-management/Get-Summary-of-Sub-accounts-Futures-Account-V2#http请求 "HTTP请求的直接链接")

GET `/sapi/v2/sub-account/futures/accountSummary`

## 请求权重(IP)[​](/docs/zh-CN/sub_account/asset-management/Get-Summary-of-Sub-accounts-Futures-Account-V2#请求权重ip "请求权重\(IP\)的直接链接")

**10**

## 请求参数[​](/docs/zh-CN/sub_account/asset-management/Get-Summary-of-Sub-accounts-Futures-Account-V2#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
futuresType| INT| YES| 1:USDT Margined Futures, 2:COIN Margined Futures  
page| INT| NO| default:1  
limit| INT| NO| default:10, max:20  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/sub_account/asset-management/Get-Summary-of-Sub-accounts-Futures-Account-V2#响应示例 "响应示例的直接链接")

> USDT Margined Futures：
    
    
    {  
      "futureAccountSummaryResp": {  
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
    }  
    

> COIN Margined Futures：
    
    
    {  
      "deliveryAccountSummaryResp": {  
        "totalMarginBalanceOfBTC": "25.03221121",   
        "totalUnrealizedProfitOfBTC": "0.12233410",  
        "totalWalletBalanceOfBTC": "22.15879444",  
        "asset": "BTC",  
        "subAccountList":[  
            {  
                "email": "123@test.com",  
                "totalMarginBalance": "22.12659734",   
                "totalUnrealizedProfit": "0.00000000",  
                "totalWalletBalance": "22.12659734",  
                "asset": "BTC"  
            },  
            {   
                "email": "345@test.com",  
                "totalMarginBalance": "0.90575887",  
                "totalUnrealizedProfit": "0.03219710",  
                "totalWalletBalance": "0.87356177",  
                "asset": "BTC"  
            }  
        ]  
      }  
    }