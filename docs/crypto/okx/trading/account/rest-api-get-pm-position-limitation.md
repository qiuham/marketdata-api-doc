---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#trading-account-rest-api-get-pm-position-limitation
anchor_id: trading-account-rest-api-get-pm-position-limitation
api_type: REST
updated_at: 2026-07-20 19:35:16.218193
---

# Get PM position limitation

Retrieve cross position limitation of SWAP/FUTURES/OPTION under Portfolio margin mode.  
  
#### Rate Limit: 10 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/account/position-tiers`

> Request Example
    
    
    # Query limitation of BTC-USDT
    GET /api/v5/account/position-tiers?instType=SWAP&uly=BTC-USDT
    
    
    
    
    import okx.Account as Account
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading:0 , demo trading:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # Get PM position limitation
    result = accountAPI.get_account_position_tiers(
        instType="SWAP",
        uly="BTC-USDT"
    )
    print(result)
    

#### Request Parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
instType | String | Yes | Instrument type  
`SWAP`  
`FUTURES`  
`OPTION`  
instFamily | String | Yes | Single instrument family or instrument families (no more than 5) separated with comma.  
  
> Response Example
    
    
    {
      "code": "0",
      "data": [
        {
          "instFamily": "BTC-USDT",
          "maxSz": "10000",
          "posType": "",
          "uly": "BTC-USDT"
        }
      ],
      "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
uly | String | Underlying  
Applicable to `FUTURES`/`SWAP`/`OPTION`  
instFamily | String | Instrument family  
Applicable to `FUTURES`/`SWAP`/`OPTION`  
maxSz | String | Max number of positions  
posType | String | Limitation of position type, only applicable to cross `OPTION` under portfolio margin mode   
`1`: Contracts of pending orders and open positions for all derivatives instruments. `2`: Contracts of pending orders for all derivatives instruments. `3`: Pending orders for all derivatives instruments. `4`: Contracts of pending orders and open positions for all derivatives instruments on the same side. `5`: Pending orders for one derivatives instrument. `6`: Contracts of pending orders and open positions for one derivatives instrument. `7`: Contracts of one pending order.

---

# 获取组合保证金模式仓位限制

仅支持获取组合保证金模式下，交割、永续和期权的全仓仓位限制。  
  
#### 限速：10次/2s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/account/position-tiers`

> 请求示例
    
    
    # 查看BTC-USDT在组合保证金模式下的全仓限制
    GET /api/v5/account/position-tiers?instType=SWAP&uly=BTC-USDT
    
    
    
    
    import okx.Account as Account
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # 获取组合保证金模式仓位限制
    result = accountAPI.get_account_position_tiers(
        instType="SWAP",
        uly="BTC-USDT"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 是 | 产品类型  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`OPTION`：期权  
  
instFamily | String | 是 | 交易品种，如 `BTC-USDT`，支持多个查询（不超过5个），`instFamily`之间半角逗号分隔  
  
> 返回结果
    
    
    {
      "code": "0",
      "data": [
        {
          "instFamily": "BTC-USD",
          "maxSz": "10000",
          "posType": "",
          "uly": "BTC-USDT"
        }
      ],
      "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
uly | String | 标的指数  
适用于`交割`/`永续`/`期权`  
instFamily | String | 交易品种  
适用于`交割`/`永续`/`期权`  
maxSz | String | 最大持仓量  
posType | String | 限仓类型，仅适用于组合保证金模式下的期权全仓。  
`1`：所有合约挂单 + 持仓张数，`2`：所有合约总挂单张数，`3`：所有合约总挂单单数，`4`：同方向合约挂单 + 持仓张数，`5`：单一合约总挂单单数，`6`：单一合约挂单 + 持仓张数，`7`：单笔挂单张数"