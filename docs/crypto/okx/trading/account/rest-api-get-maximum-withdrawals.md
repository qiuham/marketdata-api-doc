---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#trading-account-rest-api-get-maximum-withdrawals
anchor_id: trading-account-rest-api-get-maximum-withdrawals
api_type: REST
updated_at: 2026-07-10 19:30:17.948090
---

# Get maximum withdrawals

Retrieve the maximum transferable amount from trading account to funding account. If no currency is specified, the transferable amount of all owned currencies will be returned.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/account/max-withdrawal`

> Request Example
    
    
    GET /api/v5/account/max-withdrawal
    
    
    
    
    import okx.Account as Account
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading:0 , demo trading:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # Get maximum withdrawals
    result = accountAPI.get_max_withdrawal()
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
ccy | String | No | Single currency or multiple currencies (no more than 20) separated with comma, e.g. `BTC` or `BTC,ETH`.  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
                "ccy": "BTC",
                "maxWd": "124",
                "maxWdEx": "125",
                "spotOffsetMaxWd": "",
                "spotOffsetMaxWdEx": ""
            },
            {
                "ccy": "ETH",
                "maxWd": "10",
                "maxWdEx": "12",
                "spotOffsetMaxWd": "",
                "spotOffsetMaxWdEx": ""
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
ccy | String | Currency  
maxWd | String | Max withdrawal (excluding borrowed assets under `Spot mode`/`Multi-currency margin`/`Portfolio margin`)  
maxWdEx | String | Max withdrawal (including borrowed assets under `Spot mode`/`Multi-currency margin`/`Portfolio margin`)  
spotOffsetMaxWd | String | Max withdrawal under Spot-Derivatives risk offset mode (excluding borrowed assets under `Portfolio margin`)  
Applicable to `Portfolio margin`  
spotOffsetMaxWdEx | String | Max withdrawal under Spot-Derivatives risk offset mode (including borrowed assets under `Portfolio margin`)  
Applicable to `Portfolio margin`

---

# 查看账户最大可转余额

当指定币种时会返回该币种的交易账户到资金账户的最大可划转数量，不指定币种会返回所有拥有的币种资产可划转数量。

#### 限速：20次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/account/max-withdrawal`

> 请求示例
    
    
    GET /api/v5/account/max-withdrawal
    
    
    
    
    import okx.Account as Account
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # 查看账户最大可转余额
    result = accountAPI.get_max_withdrawal()
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 否 | 币种，如 `BTC`  
支持多币种查询（不超过20个），币种之间半角逗号分隔  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
                "ccy": "BTC",
                "maxWd": "124",
                "maxWdEx": "125",
                "spotOffsetMaxWd": "",
                "spotOffsetMaxWdEx": ""
            },
            {
                "ccy": "ETH",
                "maxWd": "10",
                "maxWdEx": "12",
                "spotOffsetMaxWd": "",
                "spotOffsetMaxWdEx": ""
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
ccy | String | 币种  
maxWd | String | 最大可划转数量（不包含 `跨币种保证金模式`/`组合保证金模式` 借币金额）  
maxWdEx | String | 最大可划转数量（包含 `跨币种保证金模式`/`组合保证金模式` 借币金额）  
spotOffsetMaxWd | String | 现货对冲不支持借币最大可转数量  
仅适用于`组合保证金模式`  
spotOffsetMaxWdEx | String | 现货对冲支持借币的最大可转数量  
仅适用于`组合保证金模式`