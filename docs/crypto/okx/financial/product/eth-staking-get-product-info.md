---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#financial-product-eth-staking-get-product-info
anchor_id: financial-product-eth-staking-get-product-info
api_type: API
updated_at: 2026-07-20 19:37:31.057281
---

# GET / Product info

#### Rate Limit: 3 requests per second  
  
#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/finance/staking-defi/eth/product-info`

> Request Example
    
    
    GET /api/v5/finance/staking-defi/eth/product-info
    
    
    
    
    import okx.Finance.EthStaking as EthStaking
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    StackingAPI = EthStaking.EthStakingAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StackingAPI.eth_product_info()
    print(result)
    

> Response Example
    
    
    {
        "code": "0",
        "data": [
          {
            "fastRedemptionDailyLimit": "100",
            "rate": "2.23",
            "redemptDays": "8",
            "minAmt": "0.001"
          }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
fastRedemptionDailyLimit | String | Fast redemption daily limit  
The master account and sub-accounts share the same limit  
rate | String | Latest BETH APY  
redemptDays | String | Redemption days of BETH  
minAmt | String | Minimum subscription amount of BETH

---

# GET / 获取产品信息

#### 限速：3 次/s  
  
#### 限速规则：User ID

#### HTTP 请求

`GET /api/v5/finance/staking-defi/eth/product-info`

> 请求示例
    
    
    GET /api/v5/finance/staking-defi/eth/product-info
    
    
    
    
    import okx.Finance.EthStaking as EthStaking
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    StackingAPI = EthStaking.EthStakingAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StackingAPI.eth_product_info()
    print(result)
    

> 返回结果
    
    
    {
        "code": "0",
        "data": [
          {
            "fastRedemptionDailyLimit": "100",
            "rate": "2.23",
            "redemptDays": "8",
            "minAmt": "0.001"
          }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
fastRedemptionDailyLimit | String | 快速赎回每日最高份额  
母账户和子账户共享同一个限额  
rate | String | 最新 BETH 年化收益率  
redemptDays | String | BETH 赎回天数  
minAmt | String | BETH 最低申购数量