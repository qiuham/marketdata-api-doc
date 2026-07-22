---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#financial-product-flexible-loan
anchor_id: financial-product-flexible-loan
api_type: API
updated_at: 2026-07-22 19:21:16.972324
---

# Flexible loan

OKX Flexible Loan is a high-end loan product that allows users to increase cash flow without selling off their crypto. [More details](/loan)  
  
### GET / Borrowable currencies

Get borrowable currencies

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

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
  
### GET / Collateral assets

Get collateral assets in funding account.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/finance/flexible-loan/collateral-assets`

> Request Example
    
    
    GET /api/v5/finance/flexible-loan/collateral-assets?ordId=12345
    
    
    
    from okx.Finance import FlexibleLoan
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    flexibleLoanAPI = FlexibleLoan.FlexibleLoanAPI(apikey, secretkey, passphrase, False, flag)
    result = flexibleLoanAPI.collateral_assets(ordId="12345")
    print(result)
    

#### Request Parameters

**Parameters** | **Types** | **Required** | **Description**  
---|---|---|---  
ccy | String | No | Collateral currency, e.g. `BTC`  
ordId | String. | No | Order ID of your flexible loan.  
If `ordId` is not passed, system will assume it is acting against the existing order with the earliest order start time.  
If there are no existing orders, system will return empty result data.  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "assets": [
                    {
                        "amt": "1.7921483143067599",
                        "ccy": "BTC",
                        "notionalUsd": "158292.621793314105231"
                    },
                    {
                        "amt": "1.9400755578876945",
                        "ccy": "ETH",
                        "notionalUsd": "6325.6652712507628946"
                    },
                    {
                        "amt": "63.9795959720319628",
                        "ccy": "USDT",
                        "notionalUsd": "64.3650372635940345"
                    }
                ]
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
assets | Array of objects | Collateral assets data  
> ccy | String | Currency, e.g. `BTC`  
> amt | String | Available amount  
> notionalUsd | String | Notional value in `USD`  
  
### POST / Maximum loan amount

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

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
  
### GET / Maximum collateral redeem amount

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/finance/flexible-loan/max-collateral-redeem-amount`

> Request Example
    
    
    GET /api/v5/finance/flexible-loan/max-collateral-redeem-amount?ccy=USDT&ordId=12345
    
    
    
    
    from okx.Finance import FlexibleLoan
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    flexibleLoanAPI = FlexibleLoan.FlexibleLoanAPI(apikey, secretkey, passphrase, False, flag)
    result = flexibleLoanAPI.max_collateral_redeem_amount(ordId="12345", ccy="USDT")
    print(result)
    

#### Request Parameters

**Parameters** | **Types** | **Required** | **Description**  
---|---|---|---  
ccy | String | Yes | Collateral currency, e.g. `USDT`  
ordId | String | No | Order ID of your flexible loan.  
If `ordId` is not passed, system will assume it is acting against the existing order with the earliest order start time.  
If there are no existing orders, system will return empty result data.  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "ccy": "USDT",
                "maxRedeemAmt": "1"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
ccy | String | Collateral currency, e.g. `USDT`  
maxRedeemAmt | String | Maximum collateral redeem amount  
  
### POST / Adjust collateral

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/finance/flexible-loan/adjust-collateral`

> Request Example
    
    
    POST /api/v5/finance/flexible-loan/adjust-collateral
    body
    {
        "type":"add",
        "ordId": "12345",
        "collateralCcy": "BTC",
        "collateralAmt": "0.1"
    }
    
    
    
    
    from okx.Finance import FlexibleLoan
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    flexibleLoanAPI = FlexibleLoan.FlexibleLoanAPI(apikey, secretkey, passphrase, False, flag)
    result = flexibleLoanAPI.adjust_collateral(type="add", ordId="12345", collateralCcy="USDT", collateralAmt="1")
    print(result)
    

#### Request Parameters

**Parameters** | **Types** | **Required** | **Description**  
---|---|---|---  
type | String | Yes | Operation type  
`add`: Add collateral  
`reduce`: Reduce collateral  
collateralCcy | String | Yes | Collateral currency, e.g. `BTC`  
collateralAmt | String | Yes | Collateral amount  
ordId | String | No | Order ID of your flexible loan.  
If `ordId` is not passed, system will assume it is acting against the existing order with the earliest order start time.  
If there are no existing orders, system will return error `51063`  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
        ],
        "msg": ""
    }
    

#### Response Parameters

code = `0` means your request has been accepted (It doesn't mean the request has been successfully handled.)

### GET / Loan info

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/finance/flexible-loan/loan-info`

> Request Example
    
    
    GET /api/v5/finance/flexible-loan/loan-info
    
    
    
    from okx.Finance import FlexibleLoan
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    flexibleLoanAPI = FlexibleLoan.FlexibleLoanAPI(apikey, secretkey, passphrase, False, flag)
    result = flexibleLoanAPI.loan_info()
    print(result)
    

#### Request Parameters

**Parameters** | **Types** | **Required** | **Description**  
---|---|---|---  
ordId | String | No | Order ID of your flexible loan.  
If `ordId` is not passed, system will return data of all existing orders  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "ordId": "12345",
                "collateralData": [
                    {
                        "amt": "0.0000097",
                        "ccy": "COMP"
                    },
                    {
                        "amt": "0.78",
                        "ccy": "STX"
                    },
                    {
                        "amt": "0.001",
                        "ccy": "DOT"
                    },
                    {
                        "amt": "0.05357864",
                        "ccy": "LUNA"
                    }
                ],
                "collateralNotionalUsd": "1.5078763",
                "curLTV": "0.5742",
                "liqLTV": "0.8374",
                "loanData": [
                    {
                        "amt": "0.86590608",
                        "ccy": "USDC"
                    }
                ],
                "loanNotionalUsd": "0.8661285",
                "marginCallLTV": "0.7374",
                "riskWarningData": {
                    "instId": "",
                    "liqPx": ""
                }
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
ordId | String | Order ID  
loanNotionalUsd | String | Loan value in `USD`  
loanData | Array of objects | Loan data  
> ccy | String | Loan currency, e.g. `USDT`  
> amt | String | Loan amount  
collateralNotionalUsd | String | Adjusted collateral value in `USD`  
collateralData | Array of objects | Collateral data  
> ccy | String | Collateral currency, e.g. `BTC`  
> amt | String | Collateral amount  
riskWarningData | Object | Risk warning data  
> instId | String | Liquidation instrument ID, e.g. `BTC-USDT`  
This field is only valid when there is only one type of collateral and one type of borrowed currency. In other cases, it returns "".  
> liqPx | String | Liquidation price  
The unit of the liquidation price is the quote currency of the instrument, e.g. `USDT` in `BTC-USDT`.  
This field is only valid when there is only one type of collateral and one type of borrowed currency. In other cases, it returns "".  
curLTV | String | Current LTV, e.g. `0.1` represents `10%`  
Note: LTV = Loan to Value  
marginCallLTV | String | Margin call LTV, e.g. `0.1` represents `10%`  
If your loan hits the margin call LTV, our system will automatically warn you that your loan is getting close to forced liquidation.  
liqLTV | String | Liquidation LTV, e.g. `0.1` represents `10%`  
If your loan reaches liquidation LTV, it'll trigger forced liquidation. When this happens, you'll lose access to your collateral and any repayments made.  
  
### GET / Loan history

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/finance/flexible-loan/loan-history`

> Request Example
    
    
    GET /api/v5/finance/flexible-loan/loan-history
    
    
    
    from okx.Finance import FlexibleLoan
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    flexibleLoanAPI = FlexibleLoan.FlexibleLoanAPI(apikey, secretkey, passphrase, False, flag)
    result = flexibleLoanAPI.loan_history()
    print(result)
    

#### Request Parameters

**Parameters** | **Types** | **Required** | **Description**  
---|---|---|---  
type | String | No | Action type  
`borrowed`  
`repaid`  
`collateral_locked`  
`collateral_released`  
`forced_repayment_buy`  
`forced_repayment_sell`  
`forced_liquidation`  
`partial_liquidation`  
`sell_collateral`  
`buy_transition_coin`  
`sell_transition_coin`  
`buy_borrowed_coin`  
after | String | No | Pagination of data to return records earlier than the requested `refId`(not include)  
before | String | No | Pagination of data to return records newer than the requested `refId`(not include)  
limit | String | No | Number of results per request. The maximum is `100`. The default is `100`.  
ordId | String | No | Order ID of your flexible loan.  
If `ordId` is not passed, system will return data of all orders  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "amt": "-0.001",
                "ccy": "DOT",
                "refId": "17316594851045086",
                "ts": "1731659485000",
                "type": "collateral_locked"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
refId | String | Reference ID  
type | String | Action type  
ccy | String | Currency, e.g. `BTC`  
amt | String | Amount  
ts | String | Timestamp for the action, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
### GET / Accrued interest

Retrieves the interest accrual history for flexible loans over the past 30 days.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

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

# 活期借币

欧易活期借币是一款高端借贷产品，用户无需变卖数字货币即可增加现金流。[了解更多](/loan)  
  
### GET / 可借币种列表 

获取可借币种列表

#### 限速：5次/2s

#### 限速规则：User ID

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
  
### GET / 可抵押资产 

获取可抵押资产信息（仅支持资金账户中的资产）

#### 限速：5次/2s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/finance/flexible-loan/collateral-assets`

> 请求示例
    
    
    GET /api/v5/finance/flexible-loan/collateral-assets?ordId=12345
    
    
    
    from okx.Finance import FlexibleLoan
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    flexibleLoanAPI = FlexibleLoan.FlexibleLoanAPI(apikey, secretkey, passphrase, False, flag)
    result = flexibleLoanAPI.collateral_assets(ordId="12345")
    print(result)
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 否 | 币种，如 `BTC`  
ordId | String | 否 | 活期借币订单 ID。  
如果不传 `ordId`，系统将默认对起始时间最早的现存订单进行操作。  
如果没有现存订单，系统将返回空数据。  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "assets": [
                    {
                        "amt": "1.7921483143067599",
                        "ccy": "BTC",
                        "notionalUsd": "158292.621793314105231"
                    },
                    {
                        "amt": "1.9400755578876945",
                        "ccy": "ETH",
                        "notionalUsd": "6325.6652712507628946"
                    },
                    {
                        "amt": "63.9795959720319628",
                        "ccy": "USDT",
                        "notionalUsd": "64.3650372635940345"
                    }
                ]
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
assets | Array of objects | 可抵押资产信息  
> ccy | String | 币种，如 `BTC`  
> amt | String | 可用数量  
> notionalUsd | String | 可抵押资产的美金价值  
  
### POST / 最大可借 

#### 限速：5次/2s

#### 限速规则：User ID

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
  
### GET / 抵押物最大可赎回数量 

#### 限速：5次/2s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/finance/flexible-loan/max-collateral-redeem-amount`

> 请求示例
    
    
    GET /api/v5/finance/flexible-loan/max-collateral-redeem-amount?ccy=USDT&ordId=12345
    
    
    
    
    from okx.Finance import FlexibleLoan
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    flexibleLoanAPI = FlexibleLoan.FlexibleLoanAPI(apikey, secretkey, passphrase, False, flag)
    result = flexibleLoanAPI.max_collateral_redeem_amount(ordId="12345", ccy="USDT")
    print(result)
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 是 | 抵押物币种，如 `USDT`  
ordId | String | 否 | 活期借币订单 ID。  
如果不传 `ordId`，系统将默认对起始时间最早的现存订单进行操作。  
如果没有现存订单，系统将返回空数据。  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "ccy": "USDT",
                "maxRedeemAmt": "1"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
ccy | String | 抵押物币种，如 `USDT`  
maxRedeemAmt | String | 抵押物最大可赎回数量  
  
### POST / 调整抵押物 

#### 限速：5次/2s

#### 限速规则：User ID

#### HTTP请求

`POST /api/v5/finance/flexible-loan/adjust-collateral`

> 请求示例
    
    
    POST /api/v5/finance/flexible-loan/adjust-collateral
    body
    {
        "type":"add",
        "ordId": "12345",
        "collateralCcy": "BTC",
        "collateralAmt": "0.1"
    }
    
    
    
    
    from okx.Finance import FlexibleLoan
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    flexibleLoanAPI = FlexibleLoan.FlexibleLoanAPI(apikey, secretkey, passphrase, False, flag)
    result = flexibleLoanAPI.adjust_collateral(type="add", ordId="12345", collateralCcy="USDT", collateralAmt="1")
    print(result)
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
type | String | 是 | 操作类型  
`add`：补充抵押物  
`reduce`：减少抵押物  
collateralCcy | String | 是 | 抵押物币种，如 `BTC`  
collateralAmt | String | 是 | 抵押物数量  
ordId | String | 否 | 活期借币订单 ID。  
如果不传 `ordId`，系统将默认对起始时间最早的现存订单进行操作。  
如果没有现存订单，系统将返回错误 `51063`  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
        ],
        "msg": ""
    }
    

#### 返回参数

code = `0` 代表请求已被接受(不代表处理成功)

### GET / 借贷信息 

#### 限速：5次/2s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/finance/flexible-loan/loan-info`

> 请求示例
    
    
    GET /api/v5/finance/flexible-loan/loan-info
    
    
    
    from okx.Finance import FlexibleLoan
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    flexibleLoanAPI = FlexibleLoan.FlexibleLoanAPI(apikey, secretkey, passphrase, False, flag)
    result = flexibleLoanAPI.loan_info()
    print(result)
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
ordId | String | 否 | 活期借币订单 ID。  
如果不传 `ordId`，系统将返回所有现存订单数据  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "ordId": "12345",
                "collateralData": [
                    {
                        "amt": "0.0000097",
                        "ccy": "COMP"
                    },
                    {
                        "amt": "0.78",
                        "ccy": "STX"
                    },
                    {
                        "amt": "0.001",
                        "ccy": "DOT"
                    },
                    {
                        "amt": "0.05357864",
                        "ccy": "LUNA"
                    }
                ],
                "collateralNotionalUsd": "1.5078763",
                "curLTV": "0.5742",
                "liqLTV": "0.8374",
                "loanData": [
                    {
                        "amt": "0.86590608",
                        "ccy": "USDC"
                    }
                ],
                "loanNotionalUsd": "0.8661285",
                "marginCallLTV": "0.7374",
                "riskWarningData": {
                    "instId": "",
                    "liqPx": ""
                }
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
ordId | String | 订单 ID  
loanNotionalUsd | String | 借币资产美金价值  
loanData | Array of objects | 借币数据  
> ccy | String | 借贷币种  
> amt | String | 借贷数量  
collateralNotionalUsd | String | 调整后的抵押物美金价值  
collateralData | Array of objects | 抵押资产数据  
> ccy | String | 抵押币种  
> amt | String | 抵押数量  
riskWarningData | Object | 风险预警信息  
> instId | String | 清算交易产品，如 `BTC-USDT`  
仅当质押物和借币都只有一种时，该字段有效。其他情况返回""。  
> liqPx | String | 清算价格  
清算价格的单位为交易产品的计价币，如 `BTC-USDT`中的`USDT`。  
仅当质押物和借币都只有一种时，该字段有效。其他情况返回""。  
curLTV | String | 当前质押率，如 `0.1`代表`10%`  
注：LTV(Loan-to-Value，贷款价值比)  
marginCallLTV | String | 预警质押率，如 `0.1`代表`10%`  
您的质押率达到预警质押率时，系统将会提示您当前质押率过高，即将触发强平。  
liqLTV | String | 强平质押率，如 `0.1`代表`10%`  
若您的借贷达到强平质押率并被强平，您将损失质押物及已完成的还款。  
  
### GET / 借贷历史 

#### 限速：5次/2s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/finance/flexible-loan/loan-history`

> 请求示例
    
    
    GET /api/v5/finance/flexible-loan/loan-history
    
    
    
    from okx.Finance import FlexibleLoan
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    flexibleLoanAPI = FlexibleLoan.FlexibleLoanAPI(apikey, secretkey, passphrase, False, flag)
    result = flexibleLoanAPI.loan_history()
    print(result)
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
type | String | 否 | 操作类型  
`borrowed`：借入  
`repaid`：还币  
`collateral_locked`：锁定质押物  
`collateral_released`：释放质押物  
`forced_repayment_buy`：自动换币买入  
`forced_repayment_sell`：自动换币卖出  
`forced_liquidation`：强制平仓  
`partial_liquidation`：强制减仓  
`sell_collateral`：卖出质押资产  
`buy_transition_coin`：购买中介币种  
`sell_transition_coin`：卖出中介币种  
`buy_borrowed_coin`：购买借币币种  
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
                "amt": "-0.001",
                "ccy": "DOT",
                "refId": "17316594851045086",
                "ts": "1731659485000",
                "type": "collateral_locked"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
refId | String | 对应记录ID  
type | String | 操作类型  
ccy | String | 币种，如 `BTC`  
amt | String | 数量  
ts | String | 操作发生时间，Unix 时间戳为毫秒数格式，如 `1597026383085`  
  
### GET / 计息记录 

获取最近30天的计息记录。

#### 限速：5次/2s

#### 限速规则：User ID

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