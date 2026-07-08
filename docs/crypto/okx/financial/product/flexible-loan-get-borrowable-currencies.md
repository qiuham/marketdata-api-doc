---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#financial-product-flexible-loan-get-borrowable-currencies
anchor_id: financial-product-flexible-loan-get-borrowable-currencies
api_type: API
updated_at: 2026-07-08 19:29:34.382488
---

# GET / Borrowable currencies

Get borrowable currencies  
  
#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/finance/flexible-loan/borrow-currencies`

> Request Example
    
    
    GET /api/v5/finance/flexible-loan/borrow-currencies
    
    
    
    from okx.Finance import FlexibleLoan
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    flexibleLoanAPI = FlexibleLoan.FlexibleLoanAPI(apikey, secretkey, passphrase, False, flag)
    result = flexibleLoanAPI.borrow_currencies()
    print(result)
    

> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "borrowCcy": "USDT"
            },
            {
                "borrowCcy": "USDC"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
borrowCcy | String | Borrowable currency, e.g. `BTC`

---

# GET / 可借币种列表

获取可借币种列表  
  
#### 限速：5次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/finance/flexible-loan/borrow-currencies`

> 请求示例
    
    
    GET /api/v5/finance/flexible-loan/borrow-currencies
    
    
    
    from okx.Finance import FlexibleLoan
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    flexibleLoanAPI = FlexibleLoan.FlexibleLoanAPI(apikey, secretkey, passphrase, False, flag)
    result = flexibleLoanAPI.borrow_currencies()
    print(result)
    

> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "borrowCcy": "USDT"
            },
            {
                "borrowCcy": "USDC"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
borrowCcy | String | 可借币种，如 `BTC`