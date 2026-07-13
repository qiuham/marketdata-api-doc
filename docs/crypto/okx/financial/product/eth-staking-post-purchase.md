---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#financial-product-eth-staking-post-purchase
anchor_id: financial-product-eth-staking-post-purchase
api_type: API
updated_at: 2026-07-13 19:29:26.252547
---

# POST / Purchase

Staking ETH for BETH  
Only the assets in the funding account can be used.  
  
  
#### Rate Limit: 2 requests per second

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/finance/staking-defi/eth/purchase`

> Request Example
    
    
    POST /api/v5/finance/staking-defi/eth/purchase
    body 
    {
        "amt":"100"
    }
    
    
    
    import okx.Finance.EthStaking as EthStaking
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    StackingAPI = EthStaking.EthStakingAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StackingAPI.eth_purchase(amt="1")
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
amt | String | Yes | Investment amount  
  
> Response Example
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
      ]
    }
    

#### Response Parameters

code = `0` means your request has been successfully handled.

---

# POST / 申购

质押ETH获取BETH  
仅资金账户中的资产支持ETH质押。  
  
#### 限速：2次/s

#### 限速规则：User ID

#### 权限：交易

#### HTTP 请求

`POST /api/v5/finance/staking-defi/eth/purchase`

> 请求示例
    
    
    POST /api/v5/finance/staking-defi/eth/purchase
    body 
    {
        "amt":"100"
    }
    
    
    
    import okx.Finance.EthStaking as EthStaking
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    StackingAPI = EthStaking.EthStakingAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StackingAPI.eth_purchase(amt="1")
    print(result)
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
amt | String | 是 | 投资数量  
  
> 返回结果
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
      ]
    }
    

#### 返回参数

code = `0`代表请求已被成功处理