---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#sub-account-rest-api-create-an-api-key-for-a-sub-account
anchor_id: sub-account-rest-api-create-an-api-key-for-a-sub-account
api_type: REST
updated_at: 2026-07-15 19:20:30.879198
---

# Create an API Key for a sub-account

Applies to master accounts only and master accounts API Key must be linked to IP addresses.  
  
#### Rate limit：1 request per second

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP request

`POST /api/v5/users/subaccount/apikey`

> Request sample
    
    
    POST /api/v5/users/subaccount/apikey
    body
    {
        "subAcct":"panpanBroker2",
        "label":"broker3",
        "passphrase": "******",
        "perm":"trade"
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
subAcct | String | Yes | Sub-account name, supports 6 to 20 characters that include numbers and letters (case sensitive, space symbol is not supported).  
label | String | Yes | API Key note  
passphrase | String | Yes | API Key password, supports 8 to 32 alphanumeric characters containing at least 1 number, 1 uppercase letter, 1 lowercase letter and 1 special character.  
perm | String | No | API Key permissions   
`read_only`: Read only   
`trade`: Trade  
ip | String | No | Link IP addresses, separate with commas if more than one. Support up to 20 addresses.  
**For security reasons, it is recommended to bind IP addresses.**  
**API keys with trading or withdrawal permissions that are not bound to IPs will expire after 14 days of inactivity. (API keys in demo trading will not be deleted.)**  
  
> Returned result
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
            "subAcct": "test-1",
            "label": "v5",
            "apiKey": "******",
            "secretKey": "******",
            "passphrase": "******",
            "perm": "read_only,trade",
            "ip": "1.1.1.1,2.2.2.2",
            "ts": "1597026383085"
        }]
    }
    

#### Response parameters

**Parameter name** | **Type** | **Description**  
---|---|---  
subAcct | String | Sub-account name  
label | String | API Key note  
apiKey | String | API public key  
secretKey | String | API private key  
passphrase | String | API Key password  
perm | String | API Key access   
`read_only` : Read only `trade` : Trade  
ip | String | IP address that linked with API Key  
ts | String | Creation time

---

# 创建子账户的API Key

仅适用于母账户，且母账户APIKey必须绑定IP。  
  
#### 限速：1次/s

#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/users/subaccount/apikey`

> 请求示例
    
    
    POST /api/v5/users/subaccount/apikey
    body
    {
        "subAcct":"panpanBroker2",
        "label":"broker3",
        "passphrase": "******",
        "perm":"trade"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
subAcct | String | 是 | 子账户名称，支持6-20位字母和数字组合（区分大小写，不支持空格符号）  
label | String | 是 | API Key的备注  
passphrase | String | 是 | API Key密码，8-32位字母数字组合，至少包含一个数字、一个大写字母、一个小写字母、一个特殊字符  
perm | String | 否 | API Key权限  
`read_only`：读取  
`trade`：交易  
ip | String | 否 | 绑定ip地址，多个ip用半角逗号隔开，最多支持20个ip  
**安全性考虑，推荐绑定IP**   
**未绑定IP且拥有交易或提币权限的API key，将在闲置14天之后自动删除。(模拟盘的API key不会被删除)**  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
            "subAcct": "test-1",
            "label": "v5",
            "apiKey": "******",
            "secretKey": "******",
            "passphrase": "******",
            "perm": "read_only,trade",
            "ip": "1.1.1.1,2.2.2.2",
            "ts": "1597026383085"
        }]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
subAcct | String | 子账户名称  
label | String | APIKey的备注  
apiKey | String | API公钥  
secretKey | String | API的私钥  
passphrase | String | APIKey的密码  
perm | String | APIKey权限  
ip | String | APIKey绑定的ip地址  
ts | String | 创建时间