---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#trading-account-rest-api-set-position-mode
anchor_id: trading-account-rest-api-set-position-mode
api_type: REST
updated_at: 2026-07-12 19:15:08.003377
---

# Set position mode

Futures mode and Multi-currency mode: `FUTURES` and `SWAP` support both `long/short` mode and `net` mode. In `net` mode, users can only have positions in one direction; In `long/short` mode, users can hold positions in long and short directions.  
Portfolio margin mode: `FUTURES` and `SWAP` only support `net` mode  
  
#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/account/set-position-mode`

> Request Example
    
    
    POST /api/v5/account/set-position-mode
    body 
    {
        "posMode":"long_short_mode"
    }
    
    
    
    
    import okx.Account as Account
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading:0 , demo trading:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # Set position mode
    result = accountAPI.set_position_mode(
        posMode="long_short_mode"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
posMode | String | Yes | Position mode  
`long_short_mode`: long/short, only applicable to `FUTURES`/`SWAP`  
`net_mode`: net  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
            "posMode": "long_short_mode"
        }]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
posMode | String | Position mode  
  
Portfolio margin account only supports net mode

---

# 设置持仓模式

`合约模式`和`跨币种保证金模式`：交割和永续合约支持开平仓模式和买卖模式。买卖模式只会有一个方向的仓位；开平仓模式可以分别持有多、空2个方向的仓位。  
`组合保证金模式`：交割和永续仅支持买卖模式  
  
#### 限速：5次/2s

#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/account/set-position-mode`

> 请求示例
    
    
    POST /api/v5/account/set-position-mode
    body 
    {
        "posMode":"long_short_mode"
    }
    
    
    
    
    import okx.Account as Account
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # 设置持仓模式
    result = accountAPI.set_position_mode(
        posMode="long_short_mode"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
posMode | String | 是 | 持仓方式  
`long_short_mode`：开平仓模式 `net_mode`：买卖模式  
仅适用`交割/永续`  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
            "posMode": "long_short_mode"
        }]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
posMode | String | 持仓方式