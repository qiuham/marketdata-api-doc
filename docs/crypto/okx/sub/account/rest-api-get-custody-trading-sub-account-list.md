---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#sub-account-rest-api-get-custody-trading-sub-account-list
anchor_id: sub-account-rest-api-get-custody-trading-sub-account-list
api_type: REST
updated_at: 2026-06-29 19:57:50.432399
---

# Get custody trading sub-account list

The trading team uses this interface to view the list of sub-accounts currently under escrow  
  
#### Rate limit：1 request per second

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP request

`GET /api/v5/users/entrust-subaccount-list`

> Request sample
    
    
    GET /api/v5/users/entrust-subaccount-list
    
    
    
    
    import okx.SubAccount as SubAccount
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading: 0, Demo trading: 1
    
    subAccountAPI = SubAccount.SubAccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # Get custody trading sub-account list
    result = subAccountAPI.get_entrust_subaccount_list()
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
subAcct | String | No | Sub-account name  
  
> Returned results
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
           {
              "subAcct":"test-1"
           },
           {
              "subAcct":"test-2"
           }
        ]
    }
    

#### Response parameters

**Parameter name** | **Type** | **Description**  
---|---|---  
subAcct | String | Sub-account name

---

# 查看被托管的子账户列表

交易团队使用该接口查看当前托管中的子账户列表  
  
#### 限速：1次/s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/users/entrust-subaccount-list`

> 请求示例
    
    
    GET /api/v5/users/entrust-subaccount-list
    
    
    
    
    import okx.SubAccount as SubAccount
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘：1
    
    subAccountAPI = SubAccount.SubAccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # 查看被托管的子账户列表
    result = subAccountAPI.get_entrust_subaccount_list()
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
subAcct | String | 否 | 子账户名称  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
           {
              "subAcct":"test-1"
           },
           {
              "subAcct":"test-2"
           }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
subAcct | String | 子账户名称