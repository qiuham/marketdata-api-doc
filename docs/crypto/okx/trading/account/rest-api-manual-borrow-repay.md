---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#trading-account-rest-api-manual-borrow-repay
anchor_id: trading-account-rest-api-manual-borrow-repay
api_type: REST
updated_at: 2026-06-29 19:55:38.152845
---

# Manual borrow / repay

Only applicable to `Spot mode` (enabled borrowing)  
  
#### Rate Limit: 1 request per 3 seconds

#### Rate limit rule: Master Account User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/account/spot-manual-borrow-repay`

> Request Example
    
    
    POST /api/v5/account/spot-manual-borrow-repay 
    body
    {
        "ccy":"USDT",
        "side":"borrow",
        "amt":"100"
    }
    
    
    
    import okx.Account as Account
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading:0 , demo trading:1
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    result = accountAPI.spot_manual_borrow_repay(ccy="USDT", side="borrow", amt= "1")
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
ccy | String | Yes | Currency, e.g. `BTC`  
side | String | Yes | Side  
`borrow`  
`repay`  
amt | String | Yes | Amount  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "ccy":"USDT",
                "side":"borrow",
                "amt":"100"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ccy | String | Currency, e.g. `BTC`  
side | String | Side  
`borrow`  
`repay`  
amt | String | Actual amount

---

# 手动借/还币

仅适用于`现货模式`已开通借币的情况。  
  
#### 限速：1次/3s

#### 限速规则：Master Account User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/account/spot-manual-borrow-repay`

> 请求示例
    
    
    POST /api/v5/account/spot-manual-borrow-repay 
    body
    {
        "ccy": "USDT",
        "side": "borrow",
        "amt": "100"
    }
    
    
    
    import okx.Account as Account
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘:1
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    result = accountAPI.spot_manual_borrow_repay(ccy="USDT", side="borrow", amt= "1")
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 是 | 币种，如 `BTC`  
side | String | 是 | 方向  
`borrow`：借币  
`repay`：还币  
amt | String | 是 | 数量  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "ccy":"USDT",
                "side":"borrow",
                "amt":"100"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ccy | String | 币种，如 `BTC`  
side | String | 方向  
`borrow`：借币  
`repay`：还币  
amt | String | 实际数量