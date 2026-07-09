---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#sub-account-rest-api-delete-the-api-key-of-sub-accounts
anchor_id: sub-account-rest-api-delete-the-api-key-of-sub-accounts
api_type: REST
updated_at: 2026-07-09 19:38:46.766967
---

# Delete the API Key of sub-accounts

Applies to master accounts only and master accounts API Key must be linked to IP addresses.  
  
#### Rate limit：1 request per second

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP request

`POST /api/v5/users/subaccount/delete-apikey`

> Request sample
    
    
    POST /api/v5/users/subaccount/delete-apikey
    body
    {
        "subAcct":"test00001",
        "apiKey":"******"
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
subAcct | String | Yes | Sub-account name  
apiKey | String | Yes | API public key  
  
> Returned results
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
            "subAcct": "test00001"
        }]
    }
    

#### Response parameters

**Parameter name** | **Type** | **Description**  
---|---|---  
subAcct | String | Sub-account name

---

# 删除子账户的API Key

仅适用于母账户，且母账户APIKey必须绑定IP。  
  
#### 限速：1次/s

#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/users/subaccount/delete-apikey`

> 请求示例
    
    
    POST /api/v5/users/subaccount/delete-apikey
    body
    {
        "subAcct":"test00001",
        "apiKey":"******"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
subAcct | String | 是 | 子账户名称  
apiKey | String | 是 | API的公钥  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
            "subAcct": "test00001"
        }]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
subAcct | String | 子账户名称