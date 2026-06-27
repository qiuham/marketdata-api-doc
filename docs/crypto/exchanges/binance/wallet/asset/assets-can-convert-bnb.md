---
exchange: binance
source_url: https://developers.binance.com/docs/wallet/asset/assets-can-convert-bnb
api_type: REST
updated_at: 2026-05-27 18:58:59.135677
---

# Asset Dividend Record (USER_DATA)

## API Description[​](/docs/wallet/asset/assets-divided-record#api-description "Direct link to API Description")

Query asset dividend record.

## HTTP Request[​](/docs/wallet/asset/assets-divided-record#http-request "Direct link to HTTP Request")

GET `/sapi/v1/asset/assetDividend`

## Request Weight(IP)[​](/docs/wallet/asset/assets-divided-record#request-weightip "Direct link to Request Weight\(IP\)")

**10**

## Request Parameters[​](/docs/wallet/asset/assets-divided-record#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
asset| STRING| NO|   
startTime| LONG| NO|   
endTime| LONG| NO|   
limit| INT| NO| Default 20, max 500  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * There cannot be more than 180 days between parameter `startTime` and `endTime`.
> 


## Response Example[​](/docs/wallet/asset/assets-divided-record#response-example "Direct link to Response Example")
    
    
    {  
        "rows": [  
            {  
                "id": 1637366104,  
                "amount": "10.00000000",  
                "asset": "BHFT",  
                "divTime": 1563189166000,  
                "enInfo": "BHFT distribution",  
                "tranId": 2968885920,  
                "direction": 1 //direction: 1 for Asset credited (inflow), -1 for Asset debited (outflow)  
            },  
            {  
                "id": 1631750237,  
                "amount": "10.00000000",  
                "asset": "BHFT",  
                "divTime": 1563189165000,  
                "enInfo": "BHFT distribution",  
                "tranId": 2968885920,  
                "direction": 1  
            }  
        ],  
        "total": 2  
    }

---

# 资产利息记录(USER_DATA)

## 接口描述[​](/docs/zh-CN/wallet/asset/assets-divided-record#接口描述 "接口描述的直接链接")

获取资产利息记录。

## HTTP请求[​](/docs/zh-CN/wallet/asset/assets-divided-record#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/asset/assetDividend`

## 请求权重(IP)[​](/docs/zh-CN/wallet/asset/assets-divided-record#请求权重ip "请求权重\(IP\)的直接链接")

**10**

## 请求参数[​](/docs/zh-CN/wallet/asset/assets-divided-record#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
asset| STRING| NO|   
startTime| LONG| NO|   
endTime| LONG| NO|   
limit| INT| NO| Default 20, max 500  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * `startTime` 与 `endTime`之间最多只可以相差180天。
> 


## 响应示例[​](/docs/zh-CN/wallet/asset/assets-divided-record#响应示例 "响应示例的直接链接")
    
    
    {  
        "rows": [  
            {  
                "id": 1637366104,  
                "amount": "10.00000000",  
                "asset": "BHFT",  
                "divTime": 1563189166000,  
                "enInfo": "BHFT distribution",  
                "tranId": 2968885920,  
                "direction": 1 // direction：1 表示资产记账入账（资产流入），-1 表示资产记账出账（资产流出）  
            },  
            {  
                "id": 1631750237,  
                "amount": "10.00000000",  
                "asset": "BHFT",  
                "divTime": 1563189165000,  
                "enInfo": "BHFT distribution",  
                "tranId": 2968885920,  
                "direction": 1  
            }  
        ],  
        "total": 2  
    }