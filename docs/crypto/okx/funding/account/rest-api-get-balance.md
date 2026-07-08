---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#funding-account-rest-api-get-balance
anchor_id: funding-account-rest-api-get-balance
api_type: REST
updated_at: 2026-07-08 19:29:04.027402
---

# Get balance

Retrieve the funding account balances of all the assets and the amount that is available or on hold.  
  
Only asset information of a currency with a balance greater than 0 will be returned. 

#### Rate Limit: 6 requests per second

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/asset/balances`

> Request Example
    
    
    GET /api/v5/asset/balances
    
    
    
    
    import okx.Funding as Funding
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading: 0, Demo trading: 1
    
    fundingAPI = Funding.FundingAPI(apikey, secretkey, passphrase, False, flag)
    
    # Get balane
    result = fundingAPI.get_balances()
    print(result)
    

#### Request Parameters

**Parameters** | **Types** | **Required** | **Description**  
---|---|---|---  
ccy | String | No | Single currency or multiple currencies (no more than 20) separated with comma, e.g. `BTC` or `BTC,ETH`.  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "availBal": "37.11827078",
                "bal": "37.11827078",
                "ccy": "ETH",
                "frozenBal": "0"
            }
        ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ccy | String | Currency  
bal | String | Balance  
frozenBal | String | Frozen balance  
availBal | String | Available balance

---

# 获取资金账户余额

获取资金账户所有资产列表，查询各币种的余额、冻结和可用等信息。  
  
只返回余额大于0的币资产信息。 

#### 限速：6次/s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/asset/balances`

> 请求示例
    
    
    GET /api/v5/asset/balances
    
    
    
    
    import okx.Funding as Funding
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    fundingAPI = Funding.FundingAPI(apikey, secretkey, passphrase, False, flag)
    
    # 获取资金账户余额
    result = fundingAPI.get_balances()
    print(result)
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 否 | 币种，如 `BTC`  
支持多币种查询（不超过20个），币种之间半角逗号分隔  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
                "availBal": "37.11827078",
                "bal": "37.11827078",
                "ccy": "ETH",
                "frozenBal": "0"
            }
        ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ccy | String | 币种，如 `BTC`  
bal | String | 余额  
frozenBal | String | 冻结余额  
availBal | String | 可用余额