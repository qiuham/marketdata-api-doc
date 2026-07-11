---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#trading-account-rest-api-get-interest-rate
anchor_id: trading-account-rest-api-get-interest-rate
api_type: REST
updated_at: 2026-07-11 19:12:10.915591
---

# Get interest rate

Get the user's current leveraged currency borrowing market interest rate  
  
#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/account/interest-rate`

> Request Example
    
    
    GET /api/v5/account/interest-rate
    
    
    
    import okx.Account as Account
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading:0 , demo trading:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # Get the user's current leveraged currency borrowing interest rate
    result = accountAPI.get_interest_rate()
    print(result)
    

#### Request Parameters

**Parameters** | **Types** | **Required** | **Description**  
---|---|---|---  
ccy | String | No | Currency, e.g. `BTC`  
      
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "ccy":"BTC",
                "interestRate":"0.0001"
            },
            {
                "ccy":"LTC",
                "interestRate":"0.0003"
            }
        ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
interestRate | String | Hourly borrowing interest rate  
ccy | String | Currency

---

# 获取用户当前市场借币利率

#### 限速：5次/2s  
  
#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/account/interest-rate`

> 请求示例
    
    
    GET /api/v5/account/interest-rate
    
    
    
    
    import okx.Account as Account
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # 获取用户当前市场借币利率
    result = accountAPI.get_interest_rate()
    print(result)
    

#### 请求参数

**参数名** | **类型** | 是否必须 | 描述  
---|---|---|---  
ccy | String | 否 | 币种  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "ccy":"BTC",
                "interestRate":"0.0001"
            },
            {
                "ccy":"LTC",
                "interestRate":"0.0003"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
interestRate | String | 每小时借币利率  
ccy | String | 币种