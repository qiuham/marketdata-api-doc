---
exchange: binance
source_url: https://developers.binance.com/docs/wallet/travel-rule/deposit-provide-info-v2
api_type: REST
updated_at: 2026-07-01 19:11:48.082348
---

# Get Region List (USER_DATA)

## API Description[​](/docs/wallet/travel-rule/region-list#api-description "Direct link to API Description")

Query the active region/city list for a given country. Currently, only supports AU entity.

## HTTP Request[​](/docs/wallet/travel-rule/region-list#http-request "Direct link to HTTP Request")

GET `/sapi/v1/localentity/region/list`

## Request Weight(IP)[​](/docs/wallet/travel-rule/region-list#request-weightip "Direct link to Request Weight\(IP\)")

**1**

## Request Parameters[​](/docs/wallet/travel-rule/region-list#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
countryCode| STRING| YES| ISO 2-digit country code (from `Country List` API).  
timestamp| LONG| YES|   
  
## Response Example[​](/docs/wallet/travel-rule/region-list#response-example "Direct link to Response Example")
    
    
    {  
        "countryCode": "au",  
        "regions": [  
            {  
                "regionName": "New South Wales",  
                "blockType": "supported",  
                "depositAllowed": true,  
                "withdrawalAllowed": true  
            }  
        ],  
        "lastUpdated": 1716300000000  
    }  
    

## Response Fields[​](/docs/wallet/travel-rule/region-list#response-fields "Direct link to Response Fields")

Name| Type| Description  
---|---|---  
countryCode| STRING| Echoed country code (lowercase).  
regions| ARRAY| List of active regions for the given country.  
regions[].regionName| STRING| Region/city display name (use this value in questionnaire answers).  
regions[].blockType| STRING| `supported`, `limited`, or `blocked`.  
regions[].depositAllowed| BOOLEAN| Whether deposit is allowed for this region.  
regions[].withdrawalAllowed| BOOLEAN| Whether withdrawal is allowed for this region.  
lastUpdated| LONG| Last data update timestamp (epoch milliseconds); 0 if empty.

---

# 地区列表(USER_DATA)

## 接口描述[​](/docs/zh-CN/wallet/travel-rule/region-list#接口描述 "接口描述的直接链接")

查询指定国家下的活跃地区/城市列表。目前仅支持澳大利亚站。

## HTTP请求[​](/docs/zh-CN/wallet/travel-rule/region-list#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/localentity/region/list`

## 请求权重(IP)[​](/docs/zh-CN/wallet/travel-rule/region-list#请求权重ip "请求权重\(IP\)的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/wallet/travel-rule/region-list#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
countryCode| STRING| YES| ISO 2位国家代码（来自`国家列表`接口）  
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/wallet/travel-rule/region-list#响应示例 "响应示例的直接链接")
    
    
    {  
        "countryCode": "au",  
        "regions": [  
            {  
                "regionName": "New South Wales",  
                "blockType": "supported",  
                "depositAllowed": true,  
                "withdrawalAllowed": true  
            }  
        ],  
        "lastUpdated": 1716300000000  
    }  
    

## 响应字段[​](/docs/zh-CN/wallet/travel-rule/region-list#响应字段 "响应字段的直接链接")

名称| 类型| 描述  
---|---|---  
countryCode| STRING| 回显查询的国家代码（小写）  
regions| ARRAY| 该国家下的活跃地区列表  
regions[].regionName| STRING| 地区/城市显示名称（问卷答案中使用此值）  
regions[].blockType| STRING| `supported`、`limited` 或 `blocked`  
regions[].depositAllowed| BOOLEAN| 该地区是否允许充值  
regions[].withdrawalAllowed| BOOLEAN| 该地区是否允许提现  
lastUpdated| LONG| 数据最后更新时间戳（毫秒级 epoch）；为空时返回 0