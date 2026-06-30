---
exchange: binance
source_url: https://developers.binance.com/docs/sub_account/asset-management
api_type: Account
updated_at: 2026-06-30 19:11:54.833820
---

# Get Detail on Sub-account's Futures Account V2 (For Master Account) (USER_DATA)

## API Description[​](/docs/sub_account/asset-management/Get-Detail-on-Sub-accounts-Futures-Account-V2#api-description "Direct link to API Description")

Get Detail on Sub-account's Futures Account

## HTTP Request[​](/docs/sub_account/asset-management/Get-Detail-on-Sub-accounts-Futures-Account-V2#http-request "Direct link to HTTP Request")

GET `/sapi/v2/sub-account/futures/account`

## Request Weight(IP)[​](/docs/sub_account/asset-management/Get-Detail-on-Sub-accounts-Futures-Account-V2#request-weightip "Direct link to Request Weight\(IP\)")

**1**

## Request Parameters[​](/docs/sub_account/asset-management/Get-Detail-on-Sub-accounts-Futures-Account-V2#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
email| STRING| YES| [Sub-account email](/docs/sub_account/asset-management/Get-Detail-on-Sub-accounts-Futures-Account-V2#email-address)  
futuresType| INT| YES| 1:USDT Margined Futures, 2:COIN Margined Futures  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/sub_account/asset-management/Get-Detail-on-Sub-accounts-Futures-Account-V2#response-example "Direct link to Response Example")

> USDT Margined Futures：
    
    
    {  
    	"futureAccountResp": {  
    	"email": "abc@test.com",  
    	"assets":[  
    		{  
    		  	"asset": "USDT",  
    		   	"initialMargin": "0.00000000",  
    		   	"maintenanceMargin": "0.00000000",  
    		   	"marginBalance": "0.88308000",  
    		   	"maxWithdrawAmount": "0.88308000",  
    		   	"openOrderInitialMargin": "0.00000000",  
    		   	"positionInitialMargin": "0.00000000",  
    		   	"unrealizedProfit": "0.00000000",  
    		   	"walletBalance": "0.88308000"  
    		 }  
    	],  
    	"canDeposit": true,  
    	"canTrade": true,  
    	"canWithdraw": true,  
    	"feeTier": 2,  
    	"maxWithdrawAmount": "0.88308000",  
    	"totalInitialMargin": "0.00000000",  
    	"totalMaintenanceMargin": "0.00000000",  
    	"totalMarginBalance": "0.88308000",  
    	"totalOpenOrderInitialMargin": "0.00000000",  
    	"totalPositionInitialMargin": "0.00000000",  
    	"totalUnrealizedProfit": "0.00000000",  
    	"totalWalletBalance": "0.88308000",  
    	"updateTime": 1576756674610  
     }  
    }  
    

> COIN Margined Futures：
    
    
    {  
    	"deliveryAccountResp": {  
            "email": "abc@test.com",  
            "assets":[  
                {  
                    "asset": "BTC",  
                    "initialMargin": "0.00000000",  
                    "maintenanceMargin": "0.00000000",  
                    "marginBalance": "0.88308000",  
                    "maxWithdrawAmount": "0.88308000",  
                    "openOrderInitialMargin": "0.00000000",  
                    "positionInitialMargin": "0.00000000",  
                    "unrealizedProfit": "0.00000000",  
                    "walletBalance": "0.88308000"  
                 }  
            ],  
            "canDeposit": true,  
            "canTrade": true,  
            "canWithdraw": true,  
            "feeTier": 2,  
            "updateTime": 1598959682001  
        }  
    }

---

# 查询子账户Futures账户详情V2 (适用主账户) (USER_DATA)

## 接口描述[​](/docs/zh-CN/sub_account/asset-management/Get-Detail-on-Sub-accounts-Futures-Account-V2#接口描述 "接口描述的直接链接")

查询子账户Futures账户详情

## HTTP请求[​](/docs/zh-CN/sub_account/asset-management/Get-Detail-on-Sub-accounts-Futures-Account-V2#http请求 "HTTP请求的直接链接")

GET `/sapi/v2/sub-account/futures/account`

## 请求权重(IP)[​](/docs/zh-CN/sub_account/asset-management/Get-Detail-on-Sub-accounts-Futures-Account-V2#请求权重ip "请求权重\(IP\)的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/sub_account/asset-management/Get-Detail-on-Sub-accounts-Futures-Account-V2#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
email| STRING| YES| 子账户邮箱 [备注](/docs/zh-CN/sub_account/asset-management/Get-Detail-on-Sub-accounts-Futures-Account-V2#request-email-address)  
futuresType| INT| YES| 1:USDT Margined Futures, 2:COIN Margined Futures  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/sub_account/asset-management/Get-Detail-on-Sub-accounts-Futures-Account-V2#响应示例 "响应示例的直接链接")

> USDT Margined Futures：
    
    
    {  
    	"futureAccountResp": {  
    	"email": "abc@test.com",  
    	"assets":[  
    		{  
    		  	"asset": "USDT",  
    		   	"initialMargin": "0.00000000",  
    		   	"maintenanceMargin": "0.00000000",  
    		   	"marginBalance": "0.88308000",  
    		   	"maxWithdrawAmount": "0.88308000",  
    		   	"openOrderInitialMargin": "0.00000000",  
    		   	"positionInitialMargin": "0.00000000",  
    		   	"unrealizedProfit": "0.00000000",  
    		   	"walletBalance": "0.88308000"  
    		 }  
    	],  
    	"canDeposit": true,  
    	"canTrade": true,  
    	"canWithdraw": true,  
    	"feeTier": 2,  
    	"maxWithdrawAmount": "0.88308000",  
    	"totalInitialMargin": "0.00000000",  
    	"totalMaintenanceMargin": "0.00000000",  
    	"totalMarginBalance": "0.88308000",  
    	"totalOpenOrderInitialMargin": "0.00000000",  
    	"totalPositionInitialMargin": "0.00000000",  
    	"totalUnrealizedProfit": "0.00000000",  
    	"totalWalletBalance": "0.88308000",  
    	"updateTime": 1576756674610  
     }  
    }  
      
    

> COIN Margined Futures：
    
    
      
    {  
    	"deliveryAccountResp": {  
            "email": "abc@test.com",  
            "assets":[  
                {  
                    "asset": "BTC",  
                    "initialMargin": "0.00000000",  
                    "maintenanceMargin": "0.00000000",  
                    "marginBalance": "0.88308000",  
                    "maxWithdrawAmount": "0.88308000",  
                    "openOrderInitialMargin": "0.00000000",  
                    "positionInitialMargin": "0.00000000",  
                    "unrealizedProfit": "0.00000000",  
                    "walletBalance": "0.88308000"  
                 }  
            ],  
            "canDeposit": true,  
            "canTrade": true,  
            "canWithdraw": true,  
            "feeTier": 2,  
            "updateTime": 1598959682001  
        }  
    }