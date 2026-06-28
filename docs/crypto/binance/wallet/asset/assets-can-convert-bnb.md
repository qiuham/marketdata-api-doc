---
exchange: binance
source_url: https://developers.binance.com/docs/wallet/asset/assets-can-convert-bnb
api_type: REST
updated_at: 2026-06-28 18:53:58.946377
---

# Dust Convertible Assets (USER_DATA)

## API Description[​](/docs/wallet/asset/dust-convertible-assets#api-description "Direct link to API Description")

Query dust convertible assets

## HTTP Request[​](/docs/wallet/asset/dust-convertible-assets#http-request "Direct link to HTTP Request")

POST `/sapi/v1/asset/dust-convert/query-convertible-assets`

## Request Weight(IP)[​](/docs/wallet/asset/dust-convertible-assets#request-weightip "Direct link to Request Weight\(IP\)")

**1**

## Request Parameters[​](/docs/wallet/asset/dust-convertible-assets#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
accountType| STRING| NO| `SPOT` or `MARGIN`, default `SPOT`  
targetAsset| STRING| YES|   
dustQuotaAssetToTargetAssetPrice| BIGDECIMAL| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/wallet/asset/dust-convertible-assets#response-example "Direct link to Response Example")
    
    
    {  
        "dribbletPercentage": "0.02",  
        "totalTransferQuotaAssetAmount": "0.7899968",  
        "totalTransferTargetAssetAmount": "0.7899968",  
        "dribbletBase": "10",  
        "details": [  
            {  
                "asset": "AR",  
                "assetFullName": "AR",  
                "amountFree": "0.00856",  
                "exchange": "0.00073616",  
                "toQuotaAssetAmount": "0.036808",  
                "toTargetAssetAmount": "0.036808",  
                "toTargetAssetOffExchange": "0.03607184"  
            },  
            {  
                "asset": "BNB",  
                "assetFullName": "BNB",  
                "amountFree": "0.00082768",  
                "exchange": "0.01506378",  
                "toQuotaAssetAmount": "0.7531888",  
                "toTargetAssetAmount": "0.7531888",  
                "toTargetAssetOffExchange": "0.73812502"  
            }  
        ]  
    }

---

# 小额可以兑换的资产(USER_DATA)

## 接口描述[​](/docs/zh-CN/wallet/asset/dust-convertible-assets#接口描述 "接口描述的直接链接")

获取小额可以兑换的资产

## HTTP请求[​](/docs/zh-CN/wallet/asset/dust-convertible-assets#http请求 "HTTP请求的直接链接")

POST `/sapi/v1/asset/dust-convert/query-convertible-assets`

## 请求权重(IP)[​](/docs/zh-CN/wallet/asset/dust-convertible-assets#请求权重ip "请求权重\(IP\)的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/wallet/asset/dust-convertible-assets#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
accountType| STRING| NO| `SPOT` 或 `MARGIN`，默认 `SPOT`  
targetAsset| STRING| YES|   
dustQuotaAssetToTargetAssetPrice| BIGDECIMAL| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/wallet/asset/dust-convertible-assets#响应示例 "响应示例的直接链接")
    
    
    {  
        "dribbletPercentage": "0.02",  
        "totalTransferQuotaAssetAmount": "0.7899968",  
        "totalTransferTargetAssetAmount": "0.7899968",  
        "dribbletBase": "10",  
        "details": [  
            {  
                "asset": "AR",  
                "assetFullName": "AR",  
                "amountFree": "0.00856",  
                "exchange": "0.00073616",  
                "toQuotaAssetAmount": "0.036808",  
                "toTargetAssetAmount": "0.036808",  
                "toTargetAssetOffExchange": "0.03607184"  
            },  
            {  
                "asset": "BNB",  
                "assetFullName": "BNB",  
                "amountFree": "0.00082768",  
                "exchange": "0.01506378",  
                "toQuotaAssetAmount": "0.7531888",  
                "toTargetAssetAmount": "0.7531888",  
                "toTargetAssetOffExchange": "0.73812502"  
            }  
        ]  
    }