---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#trading-account-rest-api-get-greeks
anchor_id: trading-account-rest-api-get-greeks
api_type: REST
updated_at: 2026-07-01 19:53:33.206158
---

# Get Greeks

Retrieve a greeks list of all assets in the account.  
  
#### Rate Limit: 10 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/account/greeks`

> Request Example
    
    
    # Get the greeks of all assets in the account
    GET /api/v5/account/greeks
    
    # Get the greeks of BTC assets in the account
    GET /api/v5/account/greeks?ccy=BTC
    
    
    
    
    import okx.Account as Account
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading:0 , demo trading:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # Retrieve a greeks list of all assets in the account
    result = accountAPI.get_greeks()
    print(result)
    

#### Request Parameters

**Parameters** | **Types** | **Required** | **Description**  
---|---|---|---  
ccy | String | No | Single currency, e.g. `BTC`.  
  
> Response Example
    
    
    {
        "code":"0",
        "data":[
            {            
               "thetaBS": "",
               "thetaPA":"",
               "deltaBS":"",
               "deltaPA":"",
               "gammaBS":"",
               "gammaPA":"",
               "vegaBS":"",    
               "vegaPA":"",
               "ccy":"BTC",
               "ts":"1620282889345"
            }
        ],
        "msg":""
    }
    

#### Response Parameters

**Parameters** | **Types** | **Description**  
---|---|---  
deltaBS | String | delta: Black-Scholes Greeks in dollars  
deltaPA | String | delta: Greeks in coins  
gammaBS | String | gamma: Black-Scholes Greeks in dollars, only applicable to OPTION  
gammaPA | String | gamma: Greeks in coins, only applicable to OPTION  
thetaBS | String | theta: Black-Scholes Greeks in dollars, only applicable to `OPTION`  
thetaPA | String | theta: Greeks in coins, only applicable to `OPTION`  
vegaBS | String | vega: Black-Scholes Greeks in dollars, only applicable to `OPTION`  
vegaPA | String | vega：Greeks in coins, only applicable to `OPTION`  
ccy | String | Currency  
ts | String | Time of getting Greeks, Unix timestamp format in milliseconds, e.g. 1597026383085

---

# 查看账户Greeks

获取账户资产的greeks信息。  
  
#### 限速：10次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/account/greeks`

> 请求示例
    
    
    # 获取账户中所有资产的greeks
    GET /api/v5/account/greeks
    
    # 获取账户中BTC的greeks
    GET /api/v5/account/greeks?ccy=BTC
    
    
    
    
    import okx.Account as Account
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # 查看账户Greeks
    result = accountAPI.get_greeks()
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 否 | 币种，如 `BTC`  
  
> 返回结果
    
    
    {
        "code":"0",
        "data":[
            {            
               "thetaBS": "",
               "thetaPA":"",
               "deltaBS":"",
               "deltaPA":"",
               "gammaBS":"",
               "gammaPA":"",
               "vegaBS":"",    
               "vegaPA":"",
               "ccy":"BTC",
               "ts":"1620282889345"
            }
        ],
        "msg":""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
deltaBS | String | 美金本位账户资产delta  
deltaPA | String | 币本位账户资产delta  
gammaBS | String | 美金本位账户资产gamma，仅适用于`期权`  
gammaPA | String | 币本位账户资产gamma，仅适用于`期权`  
thetaBS | String | 美金本位账户资产theta，仅适用于`期权`  
thetaPA | String | 币本位账户资产theta，仅适用于`期权`  
vegaBS | String | 美金本位账户资产vega，仅适用于`期权`  
vegaPA | String | 币本位账户资产vega，仅适用于`期权`  
ccy | String | 币种  
ts | String | 获取greeks的时间，Unix时间戳的毫秒数格式，如 1597026383085