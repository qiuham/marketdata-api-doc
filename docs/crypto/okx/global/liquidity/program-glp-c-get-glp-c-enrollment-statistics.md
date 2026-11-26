---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#global-liquidity-program-glp-c-get-glp-c-enrollment-statistics
anchor_id: global-liquidity-program-glp-c-get-glp-c-enrollment-statistics
api_type: API
updated_at: 2026-11-26 19:00:30.346439
---

# Get GLP-C enrollment statistics

Retrieve the total, registered and open-for-registration instrument counts.

#### Rate Limit: 5 requests per second

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/users/glp-c/enroll/stats`

> Request Example
    
    
    GET /api/v5/users/glp-c/enroll/stats?instType=SPOT
    

#### Request Parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
instType | String | Yes | Instrument type  
`SPOT`  
`PERP`  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": {
            "totalInstCount": 500,
            "registeredInstCount": 40,
            "availableInstCount": 460
        }
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
totalInstCount | Integer | Total number of instruments  
registeredInstCount | Integer | Number of registered instruments  
availableInstCount | Integer | Number of instruments open for registration  
`availableInstCount` is not necessarily equal to `totalInstCount` − `registeredInstCount`.

---

# 获取 GLP-C 注册统计

获取产品总数、已注册产品数及可注册产品数。

#### 限速：5次/s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/users/glp-c/enroll/stats`

> 请求示例
    
    
    GET /api/v5/users/glp-c/enroll/stats?instType=SPOT
    

#### 请求参数

**参数名** | **类型** | **是否必须** | **描述**  
---|---|---|---  
instType | String | 是 | 产品类型  
`SPOT`  
`PERP`  
  
> 返回示例
    
    
    {
        "code": "0",
        "msg": "",
        "data": {
            "totalInstCount": 500,
            "registeredInstCount": 40,
            "availableInstCount": 460
        }
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
totalInstCount | Integer | 产品总数  
registeredInstCount | Integer | 已注册产品数  
availableInstCount | Integer | 可注册产品数  
`availableInstCount` 不一定等于 `totalInstCount` − `registeredInstCount`。