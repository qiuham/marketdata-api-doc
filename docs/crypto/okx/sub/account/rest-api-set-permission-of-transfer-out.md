---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#sub-account-rest-api-set-permission-of-transfer-out
anchor_id: sub-account-rest-api-set-permission-of-transfer-out
api_type: REST
updated_at: 2026-07-14 19:20:55.727933
---

# Set permission of transfer out

Set permission of transfer out for sub-account (only applicable to master account API key). Sub-account can transfer out to master account by default.  
  
#### Rate Limit: 1 request per second

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/users/subaccount/set-transfer-out`

> Request Example
    
    
    POST /api/v5/users/subaccount/set-transfer-out
    body
    {
        "subAcct": "Test001,Test002",
        "canTransOut": true
    }
    
    
    
    import okx.SubAccount as SubAccount
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading: 0, Demo trading: 1
    
    subAccountAPI = SubAccount.SubAccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # Set permission of transfer out for sub-account
    result = subAccountAPI.set_permission_transfer_out(
        subAcct="hahawang1",
        canTransOut=False
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
subAcct | String | Yes | Name of the sub-account. Single sub-account or multiple sub-account (no more than 20) separated with comma.  
canTransOut | Boolean | No | Whether the sub-account has the right to transfer out. The default is `true`.  
`false`: cannot transfer out   
`true`: can transfer out  
  
> Returned result
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "subAcct": "Test001",
                "canTransOut": true
            },
            {
                "subAcct": "Test002",
                "canTransOut": true
            }
        ]
    }
    
    

#### Response parameters

**Parameter** | **Type** | **Description**  
---|---|---  
subAcct | String | Name of the sub-account  
canTransOut | Boolean | Whether the sub-account has the right to transfer out.   
`false`: cannot transfer out   
`true`: can transfer out

---

# 设置子账户主动转出权限

设置子账户转出权限（仅适用于母账户），默认可转出至母账户。  
  
#### 限速：1次/s

#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/users/subaccount/set-transfer-out`

> 请求示例
    
    
    POST /api/v5/users/subaccount/set-transfer-out
    body
    {
        "subAcct": "Test001,Test002",
        "canTransOut": true
    }
    
    
    
    import okx.SubAccount as SubAccount
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘：1
    
    subAccountAPI = SubAccount.SubAccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # 设置子账户主动转出权限
    result = subAccountAPI.set_permission_transfer_out(
        subAcct="hahawang1",
        canTransOut=False
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
subAcct | String | 是 | 子账户名称，支持设置多个（不超过20个），子账户名称之间半角逗号分隔  
canTransOut | Boolean | 否 | 是否可以主动转出，默认为`true`  
`false`：不可转出  
`true`：可以转出  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "subAcct": "Test001",
                "canTransOut": true
            },
            {
                "subAcct": "Test002",
                "canTransOut": true
            }
        ]
    }
    
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
subAcct | String | 子账户名称  
canTransOut | Boolean | 是否可以主动转出   
`false`：不可转出  
`true`：可以转出