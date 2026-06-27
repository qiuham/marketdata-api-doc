---
exchange: binance
source_url: https://developers.binance.com/docs/sub_account/asset-management/Get-Move-Position-History-for-Sub-account
api_type: Account
updated_at: 2026-05-27 19:02:17.807411
---

# Get Sub-account Deposit Address (For Master Account) (USER_DATA)

## API Description[​](/docs/sub_account/asset-management/Get-Sub-account-Deposit-Address#api-description "Direct link to API Description")

Fetch sub-account deposit address

## HTTP Request[​](/docs/sub_account/asset-management/Get-Sub-account-Deposit-Address#http-request "Direct link to HTTP Request")

GET `/sapi/v1/capital/deposit/subAddress`

## Request Weight(IP)[​](/docs/sub_account/asset-management/Get-Sub-account-Deposit-Address#request-weightip "Direct link to Request Weight\(IP\)")

**1**

## Request Parameters[​](/docs/sub_account/asset-management/Get-Sub-account-Deposit-Address#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
email| STRING| YES| Sub account email  
coin| STRING| YES|   
network| STRING| NO|   
amount| DECIMAL| NO|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * `amount` needs to be sent if using LIGHTNING network
> 


## Response Example[​](/docs/sub_account/asset-management/Get-Sub-account-Deposit-Address#response-example "Direct link to Response Example")
    
    
    {  
    	"address":"TDunhSa7jkTNuKrusUTU1MUHtqXoBPKETV",  
    	"coin":"USDT",  
    	"tag":"",  
    	"url":"https://tronscan.org/#/address/TDunhSa7jkTNuKrusUTU1MUHtqXoBPKETV"  
    }

---

# 获取子账户充值地址 (适用主账户) (USER_DATA)

## 接口描述[​](/docs/zh-CN/sub_account/asset-management/Get-Sub-account-Deposit-Address#接口描述 "接口描述的直接链接")

获取子账户充值地址

## HTTP请求[​](/docs/zh-CN/sub_account/asset-management/Get-Sub-account-Deposit-Address#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/capital/deposit/subAddress`

## 请求权重(IP)[​](/docs/zh-CN/sub_account/asset-management/Get-Sub-account-Deposit-Address#请求权重ip "请求权重\(IP\)的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/sub_account/asset-management/Get-Sub-account-Deposit-Address#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
email| STRING| YES| 子账户邮箱 [备注](/docs/zh-CN/sub_account/asset-management/Get-Sub-account-Deposit-Address#request-email-address)  
coin| STRING| YES|   
network| STRING| NO|   
amount| DECIMAL| NO|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * 使用LIGHTNING网络时，`amount`必须传
> 


## 响应示例[​](/docs/zh-CN/sub_account/asset-management/Get-Sub-account-Deposit-Address#响应示例 "响应示例的直接链接")
    
    
    {  
    	"address":"TDunhSa7jkTNuKrusUTU1MUHtqXoBPKETV",  
    	"coin":"USDT",  
    	"tag":"",  
    	"url":"https://tronscan.org/#/address/TDunhSa7jkTNuKrusUTU1MUHtqXoBPKETV"  
    }