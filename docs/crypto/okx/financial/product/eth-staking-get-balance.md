---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#financial-product-eth-staking-get-balance
anchor_id: financial-product-eth-staking-get-balance
api_type: API
updated_at: 2026-07-18 20:05:16.833943
---

# GET / Balance

The balance represents the real-time total BETH holdings across the entire account, including assets in the trading account, funding account, and those currently in the redeeming process.  
  
#### Rate Limit: 6 requests per second

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/finance/staking-defi/eth/balance`

> Request Example
    
    
    GET /api/v5/finance/staking-defi/eth/balance
    
    
    
    import okx.Finance.EthStaking as EthStaking
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    StackingAPI = EthStaking.EthStakingAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StackingAPI.eth_balance()
    print(result)
    

#### Request Parameters

None

> Response Example
    
    
    {
        "code": "0",
        "data": [
          {
            "amt": "0.63926191",
            "ccy": "BETH",
            "latestInterestAccrual": "0.00006549",
            "totalInterestAccrual": "0.01490596",
            "ts": "1699257600000"
          }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ccy | String | Currency, e.g. `BETH`  
amt | String | Currency amount  
latestInterestAccrual | String | Latest interest accrual  
totalInterestAccrual | String | Total interest accrual  
ts | String | Query data time, Unix timestamp format in milliseconds, e.g. `1597026383085`

---

# GET / 获取余额

该余额表示账户内 BETH 的实时总持仓，包括交易账户、资金账户以及处于赎回过程中的资产。  
  
#### 限速：6 次/s

#### 限速规则：User ID

#### HTTP 请求

`GET /api/v5/finance/staking-defi/eth/balance`

> 请求示例
    
    
    GET /api/v5/finance/staking-defi/eth/balance
    
    
    
    
    import okx.Finance.EthStaking as EthStaking
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    StackingAPI = EthStaking.EthStakingAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StackingAPI.eth_balance()
    print(result)
    

#### 请求参数

None

> 返回结果
    
    
    {
        "code": "0",
        "data": [
          {
            "amt": "0.63926191",
            "ccy": "BETH",
            "latestInterestAccrual": "0.00006549",
            "totalInterestAccrual": "0.01490596",
            "ts": "1699257600000"
          }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ccy | String | 币种名称，如 `BETH`  
amt | String | 币种数量  
latestInterestAccrual | String | 最近收益  
totalInterestAccrual | String | 历史总收益  
ts | String | 快照时间，值为时间戳，Unix时间戳为毫秒数格式，如 `1597026383085`