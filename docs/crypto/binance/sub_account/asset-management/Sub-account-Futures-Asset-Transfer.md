---
exchange: binance
source_url: https://developers.binance.com/docs/sub_account/asset-management/Sub-account-Futures-Asset-Transfer
api_type: Account
updated_at: 2026-06-30 19:12:20.753167
---

# Universal Transfer (For Master Account) (USER_DATA)

## API Description[​](/docs/sub_account/asset-management/Universal-Transfer#api-description "Direct link to API Description")

Universal Transfer

## HTTP Request[​](/docs/sub_account/asset-management/Universal-Transfer#http-request "Direct link to HTTP Request")

POST `/sapi/v1/sub-account/universalTransfer`

## Request Weight(IP)[​](/docs/sub_account/asset-management/Universal-Transfer#request-weightip "Direct link to Request Weight\(IP\)")

**1**

## Request Weight(UID)[​](/docs/sub_account/asset-management/Universal-Transfer#request-weightuid "Direct link to Request Weight\(UID\)")

**360**

## Request Parameters[​](/docs/sub_account/asset-management/Universal-Transfer#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
fromEmail| STRING| NO|   
toEmail| STRING| NO|   
fromAccountType| STRING| YES| "SPOT","USDT_FUTURE","COIN_FUTURE","MARGIN"(Cross),"ISOLATED_MARGIN"  
toAccountType| STRING| YES| "SPOT","USDT_FUTURE","COIN_FUTURE","MARGIN"(Cross),"ISOLATED_MARGIN"  
clientTranId| STRING| NO| Must be unique  
symbol| STRING| NO| Only supported under ISOLATED_MARGIN type  
asset| STRING| YES|   
amount| DECIMAL| YES|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * You need to enable "internal transfer" option for the api key which requests this endpoint.
>   * Transfer from master account by default if fromEmail is not sent.
>   * Transfer to master account by default if toEmail is not sent.
>   * At least either fromEmail or toEmail need to be sent when the fromAccountType and the toAccountType are the same.
>   * Supported transfer scenarios: 
>     * `SPOT` transfer to `SPOT`, `USDT_FUTURE`, `COIN_FUTURE` (regardless of master or sub)
>     * `SPOT`, `USDT_FUTURE`, `COIN_FUTURE` transfer to `SPOT` (regardless of master or sub)
>     * Master account `SPOT` transfer to sub-account `MARGIN(Cross)`, `ISOLATED_MARGIN`
>     * Sub-account `MARGIN(Cross)`, `ISOLATED_MARGIN` transfer to master account `SPOT`
>     * Sub-account `MARGIN(Cross)` transfer to Sub-account `MARGIN(Cross)`
>     * `ALPHA` to `ALPHA` (regardless of master or sub)
> 


## Response Example[​](/docs/sub_account/asset-management/Universal-Transfer#response-example "Direct link to Response Example")
    
    
    {  
        "tranId":11945860693,  
        "clientTranId":"test"  
    }

---

# 子母账户万能划转 (适用主账户) (USER_DATA)

## 接口描述[​](/docs/zh-CN/sub_account/asset-management/Universal-Transfer#接口描述 "接口描述的直接链接")

子母账户万能划转

## HTTP请求[​](/docs/zh-CN/sub_account/asset-management/Universal-Transfer#http请求 "HTTP请求的直接链接")

POST `/sapi/v1/sub-account/universalTransfer`

## 请求权重(IP)[​](/docs/zh-CN/sub_account/asset-management/Universal-Transfer#请求权重ip "请求权重\(IP\)的直接链接")

**1**

## 请求权重(UID)[​](/docs/zh-CN/sub_account/asset-management/Universal-Transfer#请求权重uid "请求权重\(UID\)的直接链接")

**360**

## 请求参数[​](/docs/zh-CN/sub_account/asset-management/Universal-Transfer#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
fromEmail| STRING| NO|   
toEmail| STRING| NO|   
fromAccountType| STRING| YES| "SPOT","USDT_FUTURE","COIN_FUTURE","MARGIN"(Cross),"ISOLATED_MARGIN"  
toAccountType| STRING| YES| "SPOT","USDT_FUTURE","COIN_FUTURE","MARGIN"(Cross),"ISOLATED_MARGIN"  
clientTranId| STRING| NO| 不可重复  
symbol| STRING| NO| 仅在ISOLATED_MARGIN类型下使用  
asset| STRING| YES|   
amount| DECIMAL| YES|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * 需要开启母账户apikey“允许子母账户划转”权限。
>   * 若 fromEmail 未传，默认从母账户转出。
>   * 若 toEmail 未传，默认转入母账户。
>   * 最少指定fromEmail和toEmail 其中之一。
>   * 该接口支持的划转操作有： 
>     * `现货账户`划转到`现货账户`、`U本位合约账户`、`币本位合约账户`（无论母账户或子账户）
>     * `现货账户`、`U本位合约账户`、`币本位合约账户`划转到`现货账户`（无论母账户或子账户）
>     * 母账户`现货账户`划转到子账户`杠杆全仓账户`、`杠杆逐仓账户`
>     * 子账户`杠杆全仓账户`、`杠杆逐仓账户`划转到母账户`现货账户`
>     * 子账户`杠杆全仓账户`划转到子账户`杠杆全仓账户`
>     * `ALPHA` 划转到 `ALPHA` (无论母账户或子账户)
> 


## 响应示例[​](/docs/zh-CN/sub_account/asset-management/Universal-Transfer#响应示例 "响应示例的直接链接")
    
    
    {  
        "tranId":11945860693,  
        "clientTranId":"test"  
    }