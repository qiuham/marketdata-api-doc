---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#financial-product-flexible-loan-post-maximum-loan-amount
anchor_id: financial-product-flexible-loan-post-maximum-loan-amount
api_type: API
updated_at: 2026-07-07 19:43:54.835589
---

# POST / Maximum loan amount

#### Rate Limit: 5 requests per 2 seconds  
  
#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`POST /api/v5/finance/flexible-loan/max-loan`

> Request Example
    
    
    POST /api/v5/finance/flexible-loan/max-loan
    body
    {
        "ordId": "12345",
        "borrowCcy": "USDT"
    }
    
    
    
    
    from okx.Finance import FlexibleLoan
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    flexibleLoanAPI = FlexibleLoan.FlexibleLoanAPI(apikey, secretkey, passphrase, False, flag)
    result = flexibleLoanAPI.max_loan(ordId="12345", borrowCcy="USDT")
    print(result)
    

#### Request Parameters

**Parameters** | **Types** | **Required** | **Description**  
---|---|---|---  
borrowCcy | String | Yes | Currency to borrow, e.g. `USDT`  
ordId | String | No | Order ID of your flexible loan.  
If `ordId` is not passed, system will assume it is acting against the existing order with the earliest order start time.  
If there are no existing orders, system will return empty result data.  
supCollateral | Array of objects | No | Supplementary collateral assets  
> ccy | String | Yes | Currency, e.g. `BTC`  
> amt | String | Yes | Amount  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "borrowCcy": "USDT",
                "maxLoan": "0.01113",
                "notionalUsd": "0.01113356",
                "remainingQuota": "3395000"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
borrowCcy | String | Currency to borrow, e.g. `USDT`  
maxLoan | String | Maximum available loan  
notionalUsd | String | Maximum available loan notional value, unit in `USD`  
remainingQuota | String | Remaining quota, unit in `borrowCcy`

---

# POST / 最大可借

#### 限速：5次/2s  
  
#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`POST /api/v5/finance/flexible-loan/max-loan`

> 请求示例
    
    
    POST /api/v5/finance/flexible-loan/max-loan
    body
    {
        "ordId": "12345",
        "borrowCcy": "USDT"
    }
    
    
    
    
    from okx.Finance import FlexibleLoan
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    flexibleLoanAPI = FlexibleLoan.FlexibleLoanAPI(apikey, secretkey, passphrase, False, flag)
    result = flexibleLoanAPI.max_loan(ordId="12345", borrowCcy="USDT")
    print(result)
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
borrowCcy | String | 是 | 借币币种，如 `USDT`  
ordId | String | 否 | 活期借币订单 ID。  
如果不传 `ordId`，系统将默认对起始时间最早的现存订单进行操作。  
如果没有现存订单，系统将返回空数据。  
supCollateral | Array of objects | 否 | 补充抵押资产信息  
> ccy | String | 是 | 币种，如 `BTC`  
> amt | String | 是 | 数量  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "borrowCcy": "USDT",
                "maxLoan": "0.01113",
                "notionalUsd": "0.01113356",
                "remainingQuota": "3395000"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
borrowCcy | String | 借币币种，如 `USDT`  
maxLoan | String | 最大可借数量  
notionalUsd | String | 最大可借美元价值  
remainingQuota | String | 剩余可借额度，单位为`borrowCcy`