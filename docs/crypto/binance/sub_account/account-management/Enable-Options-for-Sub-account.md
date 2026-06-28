---
exchange: binance
source_url: https://developers.binance.com/docs/sub_account/account-management/Enable-Options-for-Sub-account
api_type: Account
updated_at: 2026-05-27 19:01:58.536662
---

# Get Futures Position-Risk of Sub-account V2 (For Master Account) (USER_DATA)

## API Description[​](/docs/sub_account/account-management/Get-Futures-Position-Risk-of-Sub-account-V2#api-description "Direct link to API Description")

Get Futures Position-Risk of Sub-account V2

## HTTP Request[​](/docs/sub_account/account-management/Get-Futures-Position-Risk-of-Sub-account-V2#http-request "Direct link to HTTP Request")

GET `/sapi/v2/sub-account/futures/positionRisk`

## Request Weight(IP)[​](/docs/sub_account/account-management/Get-Futures-Position-Risk-of-Sub-account-V2#request-weightip "Direct link to Request Weight\(IP\)")

**1**

## Request Parameters[​](/docs/sub_account/account-management/Get-Futures-Position-Risk-of-Sub-account-V2#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
email| STRING| YES| [Sub-account email](/docs/sub_account/account-management/Get-Futures-Position-Risk-of-Sub-account-V2#email-address)  
futuresType| INT| YES| 1:USDT Margined Futures, 2:COIN Margined Futures  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/sub_account/account-management/Get-Futures-Position-Risk-of-Sub-account-V2#response-example "Direct link to Response Example")

> USDT Margined Futures：
    
    
    {  
      "futurePositionRiskVos": [  
         {  
            "entryPrice": "9975.12000",  
            "leverage": "50",              // current initial leverage  
            "maxNotional": "1000000",      // notional value limit of current initial leverage  
            "liquidationPrice": "7963.54",  
            "markPrice": "9973.50770517",  
            "positionAmount": "0.010",  
            "symbol": "BTCUSDT",  
            "unrealizedProfit": "-0.01612295"  
         }  
       ]  
    }  
    

> COIN Margined Futures：
    
    
    {  
      "deliveryPositionRiskVos": [  
         {  
            "entryPrice": "9975.12000",  
            "markPrice": "9973.50770517",  
            "leverage": "20",            
            "isolated": "false",                  
            "isolatedWallet": "9973.50770517",  
            "isolatedMargin": "0.00000000",  
            "isAutoAddMargin": "false",  
            "positionSide": "BOTH",  
            "positionAmount": "1.230",  
            "symbol": "BTCUSD_201225",  
            "unrealizedProfit": "-0.01612295"  
         }  
       ]  
    }

---

# 查询子账户合约持仓信息V2 (仅适用主账户) (USER_DATA)

## 接口描述[​](/docs/zh-CN/sub_account/account-management/Get-Futures-Position-Risk-of-Sub-account-V2#接口描述 "接口描述的直接链接")

查询子账户合约持仓信息

## HTTP请求[​](/docs/zh-CN/sub_account/account-management/Get-Futures-Position-Risk-of-Sub-account-V2#http请求 "HTTP请求的直接链接")

GET `/sapi/v2/sub-account/futures/positionRisk`

## 请求权重(IP)[​](/docs/zh-CN/sub_account/account-management/Get-Futures-Position-Risk-of-Sub-account-V2#请求权重ip "请求权重\(IP\)的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/sub_account/account-management/Get-Futures-Position-Risk-of-Sub-account-V2#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
email| STRING| YES| 子账户邮箱 [备注](/docs/zh-CN/sub_account/account-management/Get-Futures-Position-Risk-of-Sub-account-V2#request-email-address)  
futuresType| INT| YES| 1:USDT Margined Futures, 2:COIN Margined Futures  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/sub_account/account-management/Get-Futures-Position-Risk-of-Sub-account-V2#响应示例 "响应示例的直接链接")

> USDT Margined Futures：
    
    
    {  
      "futurePositionRiskVos": [  
         {  
            "entryPrice": "9975.12000",  
            "leverage": "50",              // current initial leverage  
            "maxNotional": "1000000",      // notional value limit of current initial leverage  
            "liquidationPrice": "7963.54",  
            "markPrice": "9973.50770517",  
            "positionAmount": "0.010",  
            "symbol": "BTCUSDT",  
            "unrealizedProfit": "-0.01612295"  
         }  
       ]  
    }  
    

> COIN Margined Futures：
    
    
    {  
      "deliveryPositionRiskVos": [  
         {  
            "entryPrice": "9975.12000",  
            "markPrice": "9973.50770517",  
            "leverage": "20",            
            "isolated": "false",                  
            "isolatedWallet": "9973.50770517",  
            "isolatedMargin": "0.00000000",  
            "isAutoAddMargin": "false",  
            "positionSide": "BOTH",  
            "positionAmount": "1.230",  
            "symbol": "BTCUSD_201225",  
            "unrealizedProfit": "-0.01612295"  
         }  
       ]  
    }