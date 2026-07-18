---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#sub-account-rest-api-get-sub-account-funding-balance
anchor_id: sub-account-rest-api-get-sub-account-funding-balance
api_type: REST
updated_at: 2026-07-18 20:05:10.343177
---

# Get sub-account funding balance

Query detailed balance info of Funding Account of a sub-account via the master account (applies to master accounts only)

#### Rate limit：6 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP request

`GET /api/v5/asset/subaccount/balances`

> Request sample
    
    
    GET /api/v5/asset/subaccount/balances?subAcct=test1
    
    
    
    
    import okx.SubAccount as SubAccount
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading: 0, Demo trading: 1
    
    subAccountAPI = SubAccount.SubAccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # Get sub-account funding balance
    result = subAccountAPI.get_funding_balance(
        subAcct="hahawang1"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
subAcct | String | Yes | Sub-account name  
ccy | String | No | Single currency or multiple currencies (no more than 20) separated with comma, e.g. `BTC` or `BTC,ETH`.  
  
> Returned result
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
                "availBal": "37.11827078",
                "bal": "37.11827078",
                "ccy": "ETH",
                "frozenBal": "0"
            }
        ]
    }
    

#### Response parameters

Parameter | Type | Description  
---|---|---  
ccy | String | Currency  
bal | String | Balance  
frozenBal | String | Frozen balance  
availBal | String | Available balance

---

# 获取子账户资金账户余额

获取子账户资金账户余额（适用于母账户）

#### 限速：6次/2s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/asset/subaccount/balances`

> 请求示例
    
    
    GET /api/v5/asset/subaccount/balances?subAcct=test1
    
    
    
    
    import okx.SubAccount as SubAccount
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘：1
    
    subAccountAPI = SubAccount.SubAccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # 获取子账户资金账户余额
    result = subAccountAPI.get_funding_balance(
        subAcct="hahawang1"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
subAcct | String | 是 | 子账户名称  
ccy | String | 否 | 币种，如 `BTC`  
支持多币种查询（不超过20个），币种之间半角逗号分隔  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
                "availBal": "37.11827078",
                "bal": "37.11827078",
                "ccy": "ETH",
                "frozenBal": "0"
            }
        ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ccy | String | 币种，如 `BTC`  
bal | String | 余额  
frozenBal | String | 冻结余额（不可用）  
availBal | String | 可用余额