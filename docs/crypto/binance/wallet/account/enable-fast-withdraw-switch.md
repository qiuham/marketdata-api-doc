---
exchange: binance
source_url: https://developers.binance.com/docs/wallet/account/enable-fast-withdraw-switch
api_type: Account
updated_at: 2026-05-27 18:58:53.927085
---

# Asset Detail (USER_DATA)

## API Description[​](/docs/wallet/asset#api-description "Direct link to API Description")

Fetch details of assets supported on Binance.

## HTTP Request[​](/docs/wallet/asset#http-request "Direct link to HTTP Request")

GET `/sapi/v1/asset/assetDetail`

## Request Weight(IP)[​](/docs/wallet/asset#request-weightip "Direct link to Request Weight\(IP\)")

**1**

## Request Parameters[​](/docs/wallet/asset#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
asset| STRING| NO|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
  * Please get network and other deposit or withdraw details from `GET /sapi/v1/capital/config/getall`.



## Response Example[​](/docs/wallet/asset#response-example "Direct link to Response Example")
    
    
    {  
        "CTR": {  
            "minWithdrawAmount": "70.00000000",             // min withdraw amount  
            "depositStatus": false,                         // deposit status (false if ALL of networks' are false)  
            "withdrawFee": 35,                              // withdraw fee  
            "withdrawStatus": true,                         // withdraw status (false if ALL of networks' are false)  
            "depositTip": "Delisted, Deposit Suspended"     // reason  
        },  
        "SKY": {  
            "minWithdrawAmount": "0.02000000",  
            "depositStatus": true,  
            "withdrawFee": 0.01,  
            "withdrawStatus": true  
        }  
    }

---

# 上架资产详情 (USER_DATA)

## 接口描述[​](/docs/zh-CN/wallet/asset#接口描述 "接口描述的直接链接")

获取上架资产详情

## HTTP请求[​](/docs/zh-CN/wallet/asset#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/asset/assetDetail`

## 请求权重(IP)[​](/docs/zh-CN/wallet/asset#请求权重ip "请求权重\(IP\)的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/wallet/asset#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
asset| STRING| NO|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * 充提币信息，建议查询 `GET /sapi/v1/capital/config/getall` 获取详情。
> 


## 响应示例[​](/docs/zh-CN/wallet/asset#响应示例 "响应示例的直接链接")
    
    
    {  
        "CTR": {  
            "minWithdrawAmount": "70.00000000",             // 最小提现数量  
            "depositStatus": false,                         // 是否可以充值(只有所有网络都关闭充值才为false)  
            "withdrawFee": 35,                              // 提现手续费  
            "withdrawStatus": true,                         // 是否开放提现(只有所有网络都关闭提币才为false)  
            "depositTip": "Delisted, Deposit Suspended"     // 暂停充值的原因(如果暂停才有这一项)  
        },  
        "SKY": {  
            "minWithdrawAmount": "0.02000000",  
            "depositStatus": true,  
            "withdrawFee": 0.01,  
            "withdrawStatus": true  
        }  
    }