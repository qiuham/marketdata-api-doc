---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#announcement-get-announcements
anchor_id: announcement-get-announcements
api_type: API
updated_at: 2026-07-14 19:21:17.743499
---

# GET / Announcements

Get announcements, the response is sorted by `pTime` and `businessPTime` with the most recent first. The sort will not be affected if the announcement is updated. Every page has 20 records  
  
  
  
When Accept-Language in HTTP header is set to en-US, the response will be in English. When set to zh-CN, the response will be in Chinese.  
  

Authentication is optional for this endpoint.  

It will be regarded as private endpoint and authentication is required if OK-ACCESS-KEY in HTTP header is delivered.  
It will be regarded as public endpoint and authentication isn't required if OK-ACCESS-KEY in HTTP header isn't delivered.   
  

There are differences between public endpoint and private endpoint.   
For public endpoint, the response is restricted based on your request IP.  
For private endpoint, the response is restricted based on your country of residence.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID(Private) or IP(Public)

#### Permission: Read

#### HTTP Request

`GET /api/v5/support/announcements`

> Request Example
    
    
    GET /api/v5/support/announcements
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
annType | String | No | Announcement type. Delivering the `annType` from "GET / Announcement types"  
Returning all when it is not posted  
page | String | No | Page for pagination.   
The default is 1  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "details": [
                    {
                        "annType": "announcements-new-listings",
                        "title": "OKX to list Virtuals Protocol (VIRTUAL) for spot trading",
                        "url": "https://www.okx.com/help/okx-to-list-virtuals-protocol-virtual-for-spot-trading",
                        "pTime": "1761620404821",
                        "businessPTime": "1761620400000"
                    },
                    {
                        "annType": "announcements-web3",
                        "title": "Completion of X Layer Mainnet Upgrade",
                        "url": "https://www.okx.com/help/completion-of-x-layer-mainnet-upgrade",
                        "pTime": "1761582756071",
                        "businessPTime": "1761580800000"
                    },
                ],
                "totalPage": "123"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
totalPage | String | Total number of pages  
details | Array of objects | List of announcements  
> title | String | Announcement title  
> annType | String | Announcement type  
> businessPTime | String | The time displayed on the announcement page for user reference. Unix timestamp format in milliseconds, e.g. `1597026383085`  
> pTime | String | The actual time the announcement was first published. Unix timestamp format in milliseconds, e.g. `1597026383085`. Response may be delayed around 5 minutes.  
> url | String | Announcement url

---

# GET / 公告

获取公告信息，以`pTime`和`businessPTime`倒序排序，公告更新不会影响排序。每页默认有 20 条公告  
  
  
请求头中 Accept-Language 设置为 en-US 时返回英文公告；设置为 zh-CN 时返回中文公告  
  

该接口鉴权是可选的：  

当 HTTP 请求头中有 OK-ACCESS-KEY 时，该接口会被视为私有接口且鉴权是必须的  
当 HTTP 请求头中没有 OK-ACCESS-KEY 时，该接口会被视为公共接口，不需要鉴权  
  

当为公共接口时，响应根据请求 IP 进行限制  
当为私有接口时，响应会根据居住国家进行限制  

#### 限速：5次/2s

#### 限速规则：User ID(私有接口时) 或者 IP (公共接口时)

#### 权限：读取

#### HTTP请求

`GET /api/v5/support/announcements`

> 请求示例
    
    
    GET /api/v5/support/announcements
    
    
    

#### 请求参数

#### 请求示例

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
annType | String | 否 | 公告类型。仅支持传从"GET / 公告类型" 接口返回的公告类型  
不传时返回所有类型  
page | String | 否 | 查询页数.   
默认为`1`  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "details": [
                    {
                        "annType": "announcements-new-listings",
                        "title": "OKX to list Virtuals Protocol (VIRTUAL) for spot trading",
                        "url": "https://www.okx.com/help/okx-to-list-virtuals-protocol-virtual-for-spot-trading",
                        "pTime": "1761620404821",
                        "businessPTime": "1761620400000"
                    },
                    {
                        "annType": "announcements-web3",
                        "title": "Completion of X Layer Mainnet Upgrade",
                        "url": "https://www.okx.com/help/completion-of-x-layer-mainnet-upgrade",
                        "pTime": "1761582756071",
                        "businessPTime": "1761580800000"
                    },
                ],
                "totalPage": "123"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
totalPage | String | 总的页数  
details | Array of objects | 公告列表  
> title | String | 公告标题  
> annType | String | 公告类型  
> businessPTime | String | 公告页面展示时间，供用户参考。Unix 毫秒时间戳，例如 `1597026383085`  
> pTime | String | 公告首次实际发布时间，Unix时间戳的毫秒数格式，如 `1597026383085`。响应可能延迟约 5 分钟。  
> url | String | 公告链接