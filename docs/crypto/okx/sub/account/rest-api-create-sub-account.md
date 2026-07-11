---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#sub-account-rest-api-create-sub-account
anchor_id: sub-account-rest-api-create-sub-account
api_type: REST
updated_at: 2026-07-11 19:14:23.184506
---

# Create sub-account

Applies to master accounts only and master accounts API Key must be linked to IP addresses.  
  
#### Rate limit：1 request per second

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP request

`POST /api/v5/users/subaccount/create-subaccount`

> Request sample
    
    
    POST /api/v5/users/subaccount/create-subaccount
    body
    {
        "subAcct": "subAccount002",
        "type": "1",
        "label": "123456"
    }
    
    
    
    import okx.SubAccount as SubAccount
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading: 0, Demo trading: 1
    
    subAccountAPI = SubAccount.SubAccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # Reset the API Key of a sub-account
    result = subAccountAPI.reset_subaccount_apikey(
        subAcct="hahawang1",
        apiKey="",
        ip=""
    )
    print(result)
    

#### Request Parameters

Parameter name | Type | Required | Description  
---|---|---|---  
subAcct | String | Yes | Sub-account name  
type | String | Yes | Sub-account type   
`1`: Standard sub-account   
`5`: Custody trading sub-account - Copper  
`12`: Custody trading sub-account - Komainu  
label | String | No | Sub-account notes. 6-32 letters (case sensitive), numbers or special characters like *.  
pwd | String | Conditional | Sub-account login password, it is required for KYB users only.  
Your password must contain:  
8 - 32 characters long.  
1 lowercase character (a-z).  
1 uppercase character (A-Z).  
1 number.  
1 special character e.g. ! @ # $ %  
  
> Returned results
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "label": "123456 ",
                "subAcct": "subAccount002",
                "ts": "1744875304520",
                "uid": "698827017768230914"
            }
        ]
    }
    

#### Response parameters

**Parameter name** | **Type** | **Description**  
---|---|---  
subAcct | String | Sub-account name  
label | String | Sub-account notes  
uid | String | Sub-account ID  
ts | String | Creation time

---

# 创建子账户

仅适用于母账户，且母账户APIKey必须绑定IP。  
  
#### 限速：1次/s

#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/users/subaccount/create-subaccount`

> 请求示例
    
    
    POST /api/v5/users/subaccount/create-subaccount
    body
    {
        "subAcct": "subAccount002",
        "type": "1",
        "label": "123456"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
subAcct | String | 是 | 子账户名称，支持6-20位字母和数字组合（区分大小写，不支持空格符号）  
type | String | 是 | 子账户类型   
`1`：普通子账户   
`5`：托管交易子账户 - Copper  
`12`：托管交易子账户 - Komainu  
label | String | 是 | API Key的备注，支持6-32位字母（区分大小写），数字，或者特殊字符如: *  
pwd | String | 可选 | 子账户登录密码，仅 KYB 账户必填  
您的密码必须满足以下条件：  
长度为 8 ~ 32 个字符。  
1 个小写字母 (a-z)   
1 个大写字母 (A-Z)   
1 个数字   
1 个符号，如：！@ # $ %  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "label": "123456",
                "subAcct": "subAccount002",
                "ts": "1744875304520",
                "uid": "698827017768230914"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
subAcct | String | 子账户名称  
label | String | 子账户的备注  
uid | String | 子账户 ID  
ts | String | 创建时间