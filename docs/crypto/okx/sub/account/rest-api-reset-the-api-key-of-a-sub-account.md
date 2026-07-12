---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#sub-account-rest-api-reset-the-api-key-of-a-sub-account
anchor_id: sub-account-rest-api-reset-the-api-key-of-a-sub-account
api_type: REST
updated_at: 2026-07-12 19:17:24.349921
---

# Reset the API Key of a sub-account

Applies to master accounts only and master accounts API Key must be linked to IP addresses.  
  
#### Rate limit：1 request per second

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP request

`POST /api/v5/users/subaccount/modify-apikey`

> Request sample
    
    
    POST /api/v5/users/subaccount/modify-apikey
    body
    {
        "subAcct":"yongxu",
        "apiKey":"******"
        "ip":"1.1.1.1"
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
apiKey | String | Yes | Sub-account APIKey  
label | String | No | Sub-account API Key label. The label will be reset if this is passed through.  
perm | String | No | Sub-account API Key permissions  
`read_only`: Read  
`trade`: Trade  
Separate with commas if more than one.   
The permission will be reset if this is passed through.  
ip | String | No | Sub-account API Key linked IP addresses, separate with commas if more than one. Support up to 20 IP addresses.  
The IP will be reset if this is passed through.  
If `ip` is set to "", then no IP addresses is linked to the APIKey.  
  
> Returned results
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
            "subAcct": "yongxu",
            "label": "v5",
            "apiKey": "******",
            "perm": "read,trade",
            "ip": "1.1.1.1",
            "ts": "1597026383085"
        }]
    }
    

#### Response parameters

**Parameter name** | **Type** | **Description**  
---|---|---  
subAcct | String | Sub-account name  
apiKey | String | Sub-accountAPI public key  
label | String | Sub-account API Key label  
perm | String | Sub-account API Key permissions  
`read_only`: Read  
`trade`: Trade  
ip | String | Sub-account API Key IP addresses that linked with API Key  
ts | String | Creation time

---

# 重置子账户的APIKey

仅适用于母账户，且母账户APIKey必须绑定IP。  
  
#### 限速：1次/s

#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/users/subaccount/modify-apikey`

> 请求示例
    
    
    POST /api/v5/users/subaccount/modify-apikey
    body
    {
        "subAcct":"yongxu",
        "apiKey":"******"
        "ip":"1.1.1.1"
    }
    
    
    
    import okx.SubAccount as SubAccount
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘：1
    
    subAccountAPI = SubAccount.SubAccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # 重置子账户的APIKey
    result = subAccountAPI.reset_subaccount_apikey(
        subAcct="hahawang1",
        apiKey="",
        ip=""
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
subAcct | String | 是 | 子账户名称  
apiKey | String | 是 | 子账户API的公钥  
label | String | 否 | 子账户APIKey的备注，如果填写该字段，则该字段会被重置  
perm | String | 否 | 子账户APIKey权限  
`read_only`：读取  
`trade`：交易  
多个权限用半角逗号隔开。  
如果填写该字段，则该字段会被重置。  
ip | String | 否 | 子账户APIKey绑定ip地址，多个ip用半角逗号隔开，最多支持20个ip。  
如果填写该字段，那该字段会被重置。  
如果ip传""，则表示解除IP绑定。  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
            "subAcct": "yongxu",
            "label": "v5",
            "apiKey": "******",
            "perm": "read,trade",
            "ip": "1.1.1.1",
            "ts": "1597026383085"
        }]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
subAcct | String | 子账户名称  
label | String | APIKey的备注  
apiKey | String | API公钥  
perm | String | APIKey权限  
ip | String | APIKey绑定的ip地址  
ts | String | 创建时间