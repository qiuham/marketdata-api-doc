---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#announcement-get-announcement-types
anchor_id: announcement-get-announcement-types
api_type: API
updated_at: 2026-07-03 19:41:29.177459
---

# GET / Announcement types

Authentication is not required for this public endpoint.  
  
  
The response is restricted based on your request IP.

#### Rate Limit: 1 request per 2 seconds

#### Rate limit rule: IP

#### Permission: Read

#### HTTP Request

`GET /api/v5/support/announcement-types`

> Request Example
    
    
    GET /api/v5/support/announcement-types
    
    

#### Request Parameters

None

> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "annType": "announcements-new-listings",
                "annTypeDesc": "New listings"
            },
            {
                "annType": "announcements-delistings",
                "annTypeDesc": "Delistings"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
annType | String | Announcement type  
annTypeDesc | String | Announcement type description

---

# GET / 公告类型

公共接口不需要鉴权  
  
  
响应根据请求 IP 进行限制。

#### 限速：1次/2s

#### 限速规则：IP

#### 权限：读取

#### HTTP请求

`GET /api/v5/support/announcement-types`

> 请求示例
    
    
    GET /api/v5/support/announcement-types
    
    

#### 请求参数

#### 请求示例

无

> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "annType": "announcements-new-listings",
                "annTypeDesc": "New listings"
            },
            {
                "annType": "announcements-delistings",
                "annTypeDesc": "Delistings"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
annType | String | 公告类型  
annTypeDesc | String | 公告类型描述