---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#trading-account-rest-api-set-trading-config
anchor_id: trading-account-rest-api-set-trading-config
api_type: REST
updated_at: 2026-07-07 19:41:34.108173
---

# Set trading config

#### Rate limit: 1 request per 2 seconds  
  
#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/account/set-trading-config`

> Request example
    
    
    POST /api/v5/account/set-trading-config
    body
    {
        "type": "stgyType",
        "stgyType":"1"
    }
    
    

#### Request parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
type | String | Yes | Trading config type  
`stgyType`  
stgyType | String | No | Strategy type  
`0`: general strategy  
`1`: delta neutral strategy  
Only applicable when type is `stgyType`  
  
> Response example
    
    
    {
       "code":"0",
       "msg":"",
       "data":[
          {
                "type": "stgyType",
                "stgyType":"1"
          }
       ]
    }
    
    

#### Response parameters

**Parameter** | **Type** | **Description**  
---|---|---  
type | String | Trading config type  
stgyType | String | Strategy type

---

# 设置交易配置

#### **限速：1次/2s**  
  
#### **限速规则：User ID**

#### 权限：交易

#### **HTTP请求**

`POST /api/v5/account/set-trading-config`

> 请求示例
    
    
    POST /api/v5/account/set-trading-config
    body
    {
        "type": "stgyType",
        "stgyType":"1"
    }
    
    

#### 请求参数

**参数名** | **类型** | **是否必须** | **描述**  
---|---|---|---  
type | String | Yes | 交易配置类型  
`stgyType`  
stgyType | String | No | 账号策略类型  
`0`：普通策略模式  
`1`：delta 中性策略模式  
仅适用于type为`stgyType`  
  
> 返回示例
    
    
    {
       "code":"0",
       "msg":"",
       "data":[
          {
                "type": "stgyType",
                "stgyType":"1"
          }
       ]
    }
    
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
type | String | 交易配置类型  
stgyType | String | 账号策略类型