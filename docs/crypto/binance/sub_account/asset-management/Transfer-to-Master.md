---
exchange: binance
source_url: https://developers.binance.com/docs/sub_account/asset-management/Transfer-to-Master
api_type: Account
updated_at: 2026-05-27 19:02:43.432982
---

# Transfer to Master (For Sub-account) (USER_DATA)

## API Description[​](/docs/sub_account/asset-management/Transfer-to-Master#api-description "Direct link to API Description")

Transfer to Master

## HTTP Request[​](/docs/sub_account/asset-management/Transfer-to-Master#http-request "Direct link to HTTP Request")

POST `/sapi/v1/sub-account/transfer/subToMaster`

## Request Weight(IP)[​](/docs/sub_account/asset-management/Transfer-to-Master#request-weightip "Direct link to Request Weight\(IP\)")

**1**

## Request Parameters[​](/docs/sub_account/asset-management/Transfer-to-Master#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
asset| STRING| YES|   
amount| DECIMAL| YES|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * You need to open Enable Spot & Margin Trading permission for the API Key which requests this endpoint.
> 


## Response Example[​](/docs/sub_account/asset-management/Transfer-to-Master#response-example "Direct link to Response Example")
    
    
    {  
        "txnId":"2966662589"  
    }

---

# 向主账户主动划转 (仅适用子账户) (USER_DATA)

## 接口描述[​](/docs/zh-CN/sub_account/asset-management/Transfer-to-Master#接口描述 "接口描述的直接链接")

向主账户主动划转

## HTTP请求[​](/docs/zh-CN/sub_account/asset-management/Transfer-to-Master#http请求 "HTTP请求的直接链接")

POST `/sapi/v1/sub-account/transfer/subToMaster`

## 请求权重(IP)[​](/docs/zh-CN/sub_account/asset-management/Transfer-to-Master#请求权重ip "请求权重\(IP\)的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/sub_account/asset-management/Transfer-to-Master#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
asset| STRING| YES|   
amount| DECIMAL| YES|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * 您需要打开 API Key 的 Spot & Margin Trading 权限以使用此接口。
> 


## 响应示例[​](/docs/zh-CN/sub_account/asset-management/Transfer-to-Master#响应示例 "响应示例的直接链接")
    
    
    {  
        "txnId":"2966662589"  
    }