---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#trading-account-rest-api-get-bill-types
anchor_id: trading-account-rest-api-get-bill-types
api_type: REST
updated_at: 2026-07-10 19:30:12.922213
---

# Get bill types

Get all bill types, and the mapping of bill type and subType.  
  
#### Rate limit: 20 requests per 2 seconds

#### Rate limit rule: UserId

#### Permission: Read

#### HTTP request

`GET /api/v5/account/subtypes`

> Request example
    
    
    GET /api/v5/account/subtypes
    

#### Request parameters

Parameter | Type | Required | Description  
---|---|---|---  
type | String | No | Bill type. Multiple values are supported, separated by commas, e.g. `1,2,3`. If not specified, all types are returned.  
  
> Response example
    
    
    {
        "code": "0",
        "data": [
            {
                "type": "1",
                "typeDesc": "Transfer",
                "subTypeDetails": [
                    {
                        "subType": "11",
                        "subTypeDesc": "Transfer in"
                    },
                    {
                        "subType": "12",
                        "subTypeDesc": "Transfer out"
                    }
                ]
            }
        ],
        "msg": ""
    }
    

#### Response parameters

Parameter | Type | Description  
---|---|---  
type | String | Bill type  
typeDesc | String | Bill type description, "" means the type is not enabled.  
subTypeDetails | Array of objects | Sub-type details  
> subType | String | Sub-type  
> subTypeDesc | String | Sub-type description, "" means the type is not enabled.

---

# 获取账单类型

获取所有账单类型，以及账单类型（type）与子类型（subType）的映射关系。  
  
#### 限速：20次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/account/subtypes`

> 请求示例
    
    
    GET /api/v5/account/subtypes
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
type | String | 否 | 账单类型，支持多个，用英文逗号分隔，如 `1,2,3`；不填则返回所有类型。  
  
> 返回示例
    
    
    {
        "code": "0",
        "data": [
            {
                "type": "1",
                "typeDesc": "Transfer",
                "subTypeDetails": [
                    {
                        "subType": "11",
                        "subTypeDesc": "Transfer in"
                    },
                    {
                        "subType": "12",
                        "subTypeDesc": "Transfer out"
                    }
                ]
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
type | String | 账单类型  
typeDesc | String | 账单类型描述，为 "" 代表该类型还未启用  
subTypeDetails | Array of objects | 子类型详情列表  
> subType | String | 子类型  
> subTypeDesc | String | 子类型描述，为 "" 代表该类型还未启用