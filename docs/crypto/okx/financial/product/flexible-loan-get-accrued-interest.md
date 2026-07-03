---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#financial-product-flexible-loan-get-accrued-interest
anchor_id: financial-product-flexible-loan-get-accrued-interest
api_type: REST
updated_at: 2026-07-03 19:41:21.818475
---

# GET / Accrued interest

Retrieves the interest accrual history for flexible loans over the past 30 days.  
  
#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/finance/flexible-loan/interest-accrued`

> Request Example
    
    
    GET /api/v5/finance/flexible-loan/interest-accrued
    
    
    
    from okx.Finance import FlexibleLoan
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    flexibleLoanAPI = FlexibleLoan.FlexibleLoanAPI(apikey, secretkey, passphrase, False, flag)
    result = flexibleLoanAPI.interest_accrued()
    print(result)
    

#### Request Parameters

**Parameters** | **Types** | **Required** | **Description**  
---|---|---|---  
ccy | String | No | Loan currency, e.g. `BTC`  
after | String | No | Pagination of data to return records earlier than the requested `refId`(not include)  
before | String | No | Pagination of data to return records newer than the requested `refId`(not include)  
limit | String | No | Number of results per request. The maximum is `100`. The default is `100`.  
ordId | String | No | Order ID of your flexible loan.  
If `ordId` is not passed, system will return data of all orders  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "ccy": "USDC",
                "interest": "0.00004054",
                "interestRate": "0.41",
                "loan": "0.86599309",
                "refId": "17319133035195744",
                "ts": "1731913200000"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
refId | String | Reference ID  
ccy | String | Loan currency, e.g. `BTC`  
loan | String | Loan when calculated interest  
interest | String | Interest  
interestRate | String | APY, e.g. `0.01` represents `1%`  
ts | String | Timestamp to calculated interest, Unix timestamp format in milliseconds, e.g. `1597026383085`

---

# GET / 计息记录

获取最近30天的计息记录。  
  
#### 限速：5次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/finance/flexible-loan/interest-accrued`

> 请求示例
    
    
    GET /api/v5/finance/flexible-loan/interest-accrued
    
    
    
    from okx.Finance import FlexibleLoan
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    flexibleLoanAPI = FlexibleLoan.FlexibleLoanAPI(apikey, secretkey, passphrase, False, flag)
    result = flexibleLoanAPI.interest_accrued()
    print(result)
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 否 | 借贷币种，如 `BTC`  
after | String | 否 | 请求此 ID 之前（更旧的数据）的分页内容，传的值为对应接口的`refId`（不包含）  
before | String | 否 | 请求此 ID 之后（更新的数据）的分页内容，传的值为对应接口的`refId`（不包含）  
limit | String | 否 | 返回结果的数量，最大为`100`，默认`100`条  
ordId | String | 否 | 活期借币订单 ID。  
如果不传 `ordId`，系统将返回所有订单数据  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "ccy": "USDC",
                "interest": "0.00004054",
                "interestRate": "0.41",
                "loan": "0.86599309",
                "refId": "17319133035195744",
                "ts": "1731913200000"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
refId | String | 对应记录ID  
ccy | String | 币种，如 `BTC`  
loan | String | 计息时负债  
interest | String | 利息  
interestRate | String | 年化利率，如 `0.01`代表`1%`  
ts | String | 计息时间，Unix 时间戳为毫秒数格式，如 `1597026383085`