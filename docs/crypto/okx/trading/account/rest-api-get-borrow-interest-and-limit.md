---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#trading-account-rest-api-get-borrow-interest-and-limit
anchor_id: trading-account-rest-api-get-borrow-interest-and-limit
api_type: REST
updated_at: 2026-07-17 19:15:51.095774
---

# Get borrow interest and limit

#### Rate Limit: 5 requests per 2 seconds  
  
#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/account/interest-limits`

> Request Example
    
    
    GET /api/v5/account/interest-limits?ccy=BTC
    
    
    
    
    import okx.Account as Account
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading:0 , demo trading:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # Get borrow interest and limit
    result = accountAPI.get_interest_limits(
        ccy="BTC"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
type | String | No | Loan type  
`2`: Market loans  
Default is `2`  
ccy | String | No | Loan currency, e.g. `BTC`  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "debt": "0.85893159114900247077000000000000",
                "interest": "0.00000000000000000000000000000000",
                "loanAlloc": "",
                "nextDiscountTime": "1729490400000",
                "nextInterestTime": "1729490400000",
                "records": [
                    {
                        "availLoan": "",
                        "avgRate": "",
                        "ccy": "BTC",
                        "interest": "0",
                        "loanQuota": "175.00000000",
                        "posLoan": "",
                        "rate": "0.0000276",
                        "surplusLmt": "175.00000000",
                        "surplusLmtDetails": {},
                        "usedLmt": "0.00000000",
                        "usedLoan": "",
                        "interestFreeLiab": "",
                        "potentialBorrowingAmt": ""
                    }
                ]
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
debt | String | Current debt in `USD`  
interest | String | Current interest in `USD`, the unit is `USD`  
Only applicable to `Market loans`  
nextDiscountTime | String | Next deduct time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
nextInterestTime | String | Next accrual time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
loanAlloc | String | VIP Loan allocation for the current trading account  
1\. The unit is percent(%). Range is [0, 100]. Precision is 0.01%  
2\. If master account did not assign anything, then "0"  
3\. "" if shared between master and sub-account  
records | Array of objects | Details for currencies  
> ccy | String | Loan currency, e.g. `BTC`  
> rate | String | Current daily borrowing rate  
> loanQuota | String | Borrow limit of master account  
If loan allocation has been assigned, then it is the borrow limit of the current trading account  
> surplusLmt | String | Available amount across all sub-accounts  
If loan allocation has been assigned, then it is the available amount to borrow by the current trading account  
> usedLmt | String | Borrowed amount for current account  
If loan allocation has been assigned, then it is the borrowed amount by the current trading account  
> interest | String | Interest to be deducted  
Only applicable to `Market loans`  
> interestFreeLiab | String | Interest-free liability for current account  
> potentialBorrowingAmt | String | Potential borrowing amount for current account  
> surplusLmtDetails | Object | ~~The details of available amount across all sub-accounts  
The value of `surplusLmt` is the minimum value within this array. It can help you judge the reason that `surplusLmt` is not enough.  
Only applicable to `VIP loans`~~Deprecated  
>> allAcctRemainingQuota | String | ~~Total remaining quota for master account and sub-accounts~~ Deprecated  
>> curAcctRemainingQuota | String | ~~The remaining quota for the current account.  
Only applicable to the case in which the sub-account is assigned the loan allocation~~Deprecated  
>> platRemainingQuota | String | ~~Remaining quota for the platform.  
The format like "600" will be returned when it is more than `curAcctRemainingQuota` or `allAcctRemainingQuota`~~Deprecated  
> posLoan | String | ~~Frozen amount for current account (Within the locked quota)  
Only applicable to `VIP loans`~~Deprecated  
> availLoan | String | ~~Available amount for current account (Within the locked quota)  
Only applicable to `VIP loans`~~Deprecated  
> usedLoan | String | ~~Borrowed amount for current account  
Only applicable to `VIP loans`~~Deprecated  
> avgRate | String | ~~Average hourly interest of borrowed coin  
only applicable to `VIP loans`~~Deprecated

---

# 获取借币利率与限额

#### 限速：5次/2s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/account/interest-limits`

> 请求示例
    
    
    GET /api/v5/account/interest-limits?ccy=BTC
    
    
    
    
    import okx.Account as Account
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # 获取借币利率与限额
    result = accountAPI.get_interest_limits(
        ccy="BTC"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
type | String | 否 | 借币类型  
`2`：市场借币  
默认为`2`  
ccy | String | 否 | 借贷币种，如 `BTC`  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "debt": "0.85893159114900247077000000000000",
                "interest": "0.00000000000000000000000000000000",
                "loanAlloc": "",
                "nextDiscountTime": "1729490400000",
                "nextInterestTime": "1729490400000",
                "records": [
                    {
                        "availLoan": "",
                        "avgRate": "",
                        "ccy": "BTC",
                        "interest": "0",
                        "loanQuota": "175.00000000",
                        "posLoan": "",
                        "rate": "0.0000276",
                        "surplusLmt": "175.00000000",
                        "surplusLmtDetails": {},
                        "usedLmt": "0.00000000",
                        "usedLoan": "",
                        "interestFreeLiab": "",
                        "potentialBorrowingAmt": ""
                    }
                ]
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
debt | String | 当前负债，单位为`USD`  
interest | String | 当前记息，单位为`USD`  
仅适用于`市场借币`  
nextDiscountTime | String | 下次扣息时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
nextInterestTime | String | 下次计息时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
loanAlloc | String | ~~当前交易账户尊享借币可用额度的比率（百分比）  
1\. 范围为[0, 100]. 精度为 0.01% (2位小数)  
2\. 0 代表母账户没有为子账户分配；  
3\. "" 代表母子账户共享~~  
已废弃  
records | Array of objects | 各币种详细信息  
> ccy | String | 借贷币种，如 `BTC`  
> rate | String | 当前日借币利率  
> loanQuota | String | 母账户维度借币限额  
如果已配置可用额度，该字段代表当前交易账户的借币限额  
> usedLmt | String | 当前账户已借额度  
如果已配置可用额度，该字段代表当前交易账户的已借额度  
> interest | String | 已计未扣利息  
仅适用于`市场借币`  
> interestFreeLiab | String | 当前账户免息负债  
> potentialBorrowingAmt | String | 当前账户潜在借币量  
> surplusLmt | String | 母子账户剩余可借  
如果已配置可用额度，该字段代表当前交易账户的剩余可借  
> surplusLmtDetails | Object | ~~母子账户剩余可借额度详情，母子账户剩余可借额度的值取该数组中的最小值，可以用来判断是什么原因导致可借额度不足  
仅适用于`尊享借币`~~  
已废弃  
>> allAcctRemainingQuota | String | 母子账户剩余额度  
>> curAcctRemainingQuota | String | 当前账户剩余额度  
仅适用于为子账户分配限额的场景  
>> platRemainingQuota | String | 平台剩余额度，当平台剩余额度大于`curAcctRemainingQuota`或者`allAcctRemainingQuota`时，会显示大于某个值，如">1000"  
> posLoan | String | ~~当前账户负债占用（锁定额度内）  
仅适用于`尊享借币`~~  
已废弃  
> availLoan | String | ~~当前账户剩余可用（锁定额度内）  
仅适用于`尊享借币`~~  
已废弃  
> usedLoan | String | ~~当前账户已借额度  
仅适用于`尊享借币`~~  
已废弃  
> avgRate | String | ~~已借币种平均每小时利率，仅适用于`尊享借币`~~  
已废弃