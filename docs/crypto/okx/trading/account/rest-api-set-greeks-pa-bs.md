---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#trading-account-rest-api-set-greeks-pa-bs
anchor_id: trading-account-rest-api-set-greeks-pa-bs
api_type: REST
updated_at: 2026-07-21 19:25:19.259694
---

# Set greeks (PA/BS)

Set the display type of Greeks.  
  
#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/account/set-greeks`

> Request Example
    
    
    POST /api/v5/account/set-greeks 
    body
    {
        "greeksType":"PA"
    }
    
    
    
    
    import okx.Account as Account
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading:0 , demo trading:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # Set greeks (PA/BS)
    result = accountAPI.set_greeks(greeksType="PA")
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
greeksType | String | Yes | Display type of Greeks.  
`PA`: Greeks in coins   
`BS`: Black-Scholes Greeks in dollars  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
            "greeksType": "PA"
        }]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
greeksType | String | Display type of Greeks.

---

# 期权greeks的PA/BS切换

设置greeks的展示方式。  
  
#### 限速：5次/2s

#### 限速规则：User ID

#### HTTP请求

`POST /api/v5/account/set-greeks`

> 请求示例
    
    
    POST /api/v5/account/set-greeks 
    body
    {
        "greeksType":"PA"
    }
    
    
    
    
    import okx.Account as Account
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # 期权greeks的PA/BS切换
    result = accountAPI.set_greeks(greeksType="PA")
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
greeksType | String | 是 | 希腊字母展示方式  
`PA`：币本位，`BS`：美元本位  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
            "greeksType": "PA"
        }]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
greeksType | String | 当前希腊字母展示方式