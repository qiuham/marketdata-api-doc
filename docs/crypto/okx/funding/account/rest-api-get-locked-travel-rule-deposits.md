---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#funding-account-rest-api-get-locked-travel-rule-deposits
anchor_id: funding-account-rest-api-get-locked-travel-rule-deposits
api_type: REST
updated_at: 2026-11-20 18:59:11.129476
---

# Get locked Travel Rule deposits

Retrieve the list of deposits currently locked under the Travel Rule. Returns an empty array if the user has no locked deposits. The maximum number of locked deposits is limited to 50.

#### Rate Limit: 3 requests per second

#### Rate limit rule: User ID + IP

#### HTTP Request

`GET /api/v5/asset/travel-rule/get-locked`

> Request Example
    
    
    GET /api/v5/asset/travel-rule/get-locked
    
    
    
    import okx.Funding as Funding
    
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading: 0, Demo trading: 1
    
    fundingAPI = Funding.FundingAPI(apikey, secretkey, passphrase, False, flag)
    
    result = fundingAPI.get_travel_rule_locked_deposits()
    print(result)
    

#### Request Parameters

None. User identity is resolved from API key authentication.

> Response Example
    
    
    {
      "code": "0",
      "data": [
        {
          "depId": "98765",
          "txId": "0xabc123def456789...",
          "addr": "0xdef456abc789012...",
          "ccy": "USDT",
          "chain": "ERC20",
          "amt": "100.00000000",
          "ts": "1714564800000"
        }
      ],
      "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
depId | String | Deposit ID  
txId | String | On-chain transaction hash  
addr | String | Receiving deposit address  
ccy | String | Currency, e.g. `USDT`. Empty string if currency lookup fails.  
chain | String | Network/chain name, e.g. `ERC20`. Empty string if chain lookup fails.  
amt | String | Deposit amount  
ts | String | Data generation time. Unix timestamp in milliseconds, e.g. `1714564800000`

---

# 获取因国际转账规则而锁定的充值记录

获取当前因国际转账规则而被锁定的充值列表。如果用户没有被锁定的充值，则返回空数组。锁定充值的最大数量限制为 50 条。

#### 限速：3次/s

#### 限速规则：User ID + IP

#### HTTP 请求

`GET /api/v5/asset/travel-rule/get-locked`

> 请求示例
    
    
    GET /api/v5/asset/travel-rule/get-locked
    
    
    
    import okx.Funding as Funding
    
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    fundingAPI = Funding.FundingAPI(apikey, secretkey, passphrase, False, flag)
    
    result = fundingAPI.get_travel_rule_locked_deposits()
    print(result)
    

#### 请求参数

无。用户身份通过 API Key 认证解析。

> 返回示例
    
    
    {
      "code": "0",
      "data": [
        {
          "depId": "98765",
          "txId": "0xabc123def456789...",
          "addr": "0xdef456abc789012...",
          "ccy": "USDT",
          "chain": "ERC20",
          "amt": "100.00000000",
          "ts": "1714564800000"
        }
      ],
      "msg": ""
    }
    

#### 返回参数

参数 | 类型 | 描述  
---|---|---  
depId | String | 充值 ID  
txId | String | 链上交易哈希  
addr | String | 充值地址  
ccy | String | 币种，如 `USDT`。如果币种查询失败则返回空字符串  
chain | String | 网络/链名称，如 `ERC20`。如果链查询失败则返回空字符串  
amt | String | 充值数量  
ts | String | 数据生成时间，Unix 时间戳的毫秒数格式，如 `1714564800000`