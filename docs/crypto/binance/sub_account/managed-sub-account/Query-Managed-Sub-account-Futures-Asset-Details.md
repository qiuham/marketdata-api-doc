---
exchange: binance
source_url: https://developers.binance.com/docs/sub_account/managed-sub-account/Query-Managed-Sub-account-Futures-Asset-Details
api_type: Account
updated_at: 2026-05-27 19:03:06.419375
---

# Query Managed Sub-account Margin Asset Details (For Investor Master Account) (USER_DATA)

## API Description[​](/docs/sub_account/managed-sub-account/Query-Managed-Sub-account-Margin-Asset-Details#api-description "Direct link to API Description")

Investor can use this api to query managed sub account margin asset details

## HTTP Request[​](/docs/sub_account/managed-sub-account/Query-Managed-Sub-account-Margin-Asset-Details#http-request "Direct link to HTTP Request")

GET `/sapi/v1/managed-subaccount/marginAsset`

## Request Weight(IP)[​](/docs/sub_account/managed-sub-account/Query-Managed-Sub-account-Margin-Asset-Details#request-weightip "Direct link to Request Weight\(IP\)")

**1**

## Request Parameters[​](/docs/sub_account/managed-sub-account/Query-Managed-Sub-account-Margin-Asset-Details#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
email| STRING| YES| Managed Sub Account Email  
accountType| STRING| NO| No input or input "MARGIN" to get Cross Margin account details. Input "ISOLATED_MARGIN" to get Isolated Margin account details.  
  
## Response Example[​](/docs/sub_account/managed-sub-account/Query-Managed-Sub-account-Margin-Asset-Details#response-example "Direct link to Response Example")
    
    
    {  
      "marginLevel":"999"  
      "totalAssetOfBtc":"0"  
      "totalLiabilityOfBtc":"0"  
      "totalNetAssetOfBtc":"0"  
      "userAssets":[  
        {  
        "asset":"MATIC"  
        "borrowed":"0"  
        "free":"0"  
        "interest":"0"  
        "locked":"0"  
        "netAsset":"0"  
        },  
        {  
        "asset":"VET"  
        "borrowed":"0"  
        "free":"0"  
        "interest":"0"  
        "locked":"0"  
        "netAsset":"0"  
        },  
        {  
        "asset":"BAKE"  
        "borrowed":"0"  
        "free":"0"  
        "interest":"0"  
        "locked":"0"  
        "netAsset":"0"  
        }  
      ]  
    }

---

# 投资人账户查询托管子账户杠杆资产 (适用投资人母账户) (USER_DATA)

## 接口描述[​](/docs/zh-CN/sub_account/managed-sub-account/Query-Managed-Sub-account-Margin-Asset-Details#接口描述 "接口描述的直接链接")

投资人可以根据此接口查询其托管子账户杠杆资产

## HTTP请求[​](/docs/zh-CN/sub_account/managed-sub-account/Query-Managed-Sub-account-Margin-Asset-Details#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/managed-subaccount/marginAsset`

## 请求权重(IP)[​](/docs/zh-CN/sub_account/managed-sub-account/Query-Managed-Sub-account-Margin-Asset-Details#请求权重ip "请求权重\(IP\)的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/sub_account/managed-sub-account/Query-Managed-Sub-account-Margin-Asset-Details#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
email| STRING| YES| 托管子账户邮箱  
accountType| STRING| NO| 不输入或输入MARGIN，取得全仓帐户资产。 输入ISOLATED_MARGIN，取得逐仓帐户资产。  
  
## 响应示例[​](/docs/zh-CN/sub_account/managed-sub-account/Query-Managed-Sub-account-Margin-Asset-Details#响应示例 "响应示例的直接链接")
    
    
    {  
      "marginLevel":"999",  
      "totalAssetOfBtc":"0",  
      "totalLiabilityOfBtc":"0",  
      "totalNetAssetOfBtc":"0",  
      "userAssets":[  
        {  
        "asset":"MATIC",  
        "borrowed":"0",  
        "free":"0",  
        "interest":"0",  
        "locked":"0",  
        "netAsset":"0"  
        },  
        {  
        "asset":"VET",  
        "borrowed":"0",  
        "free":"0",  
        "interest":"0",  
        "locked":"0",  
        "netAsset":"0"  
        },  
        {  
        "asset":"BAKE",  
        "borrowed":"0",  
        "free":"0",  
        "interest":"0",  
        "locked":"0",  
        "netAsset":"0"  
        }  
      ]  
    }