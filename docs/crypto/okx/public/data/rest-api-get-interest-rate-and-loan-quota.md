---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#public-data-rest-api-get-interest-rate-and-loan-quota
anchor_id: public-data-rest-api-get-interest-rate-and-loan-quota
api_type: REST
updated_at: 2026-07-16 19:21:08.172188
---

# Get interest rate and loan quota

Retrieve interest rate  
  
#### Rate Limit: 2 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/public/interest-rate-loan-quota`

> Request Example
    
    
    GET /api/v5/public/interest-rate-loan-quota
    
    
    
    import okx.PublicData as PublicData
    
    flag = "0"  # Production trading: 0, Demo trading: 1
    
    publicDataAPI = PublicData.PublicAPI(flag=flag)
    
    # Retrieve interest rate and loan quota
    result = publicDataAPI.get_interest_rate_loan_quota()
    print(result)
    

> Response Example
    
    
    {
        "code": "0",
        "data": [
            {   
                "configCcyList": [
                    {
                        "ccy": "USDT",
                        "rate": "0.00043728",
                    }
                ],
                "basic": [
                    {
                        "ccy": "USDT",
                        "quota": "500000",
                        "rate": "0.00043728"
                    },
                    {
                        "ccy": "BTC",
                        "quota": "10",
                        "rate": "0.00019992"
                    }
                ],
                "vip": [
                    {
                        "irDiscount": "",
                        "loanQuotaCoef": "6",
                        "level": "VIP1"
                    },
                    {
                        "irDiscount": "",
                        "loanQuotaCoef": "7",
                        "level": "VIP2"
                    }
                ],
                "config": [
                    {
                        "ccy": "USDT",
                        "stgyType": "0",    // normal
                        "quota": "xxxxxx",
                        "level": "VIP 8"
                    },
                    ......
                    {
                        "ccy": "USDT",
                        "stgyType": "1",    // delta neutral
                        "quota": "xxxxx",
                        "level": "VIP 1"
                    },
                    ......
                ],
                "regular": [
                    {
                        "irDiscount": "",
                        "loanQuotaCoef": "1",
                        "level": "Lv1"
                    },
                    {
                        "irDiscount": "",
                        "loanQuotaCoef": "2",
                        "level": "Lv1"
                    }
                ]
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
basic | Array of objects | Basic interest rate  
> ccy | String | Currency  
> rate | String | Daily borrowing rate  
> quota | String | Max borrow  
vip | Array of objects | Interest info for vip users  
> level | String | VIP Level, e.g. `VIP1`  
> loanQuotaCoef | String | Loan quota coefficient. Loan quota = `quota` * `level`  
> irDiscount | String | ~~Interest rate discount~~(Deprecated)  
regular | Array of objects | Interest info for regular users  
> level | String | Regular user Level, e.g. `Lv1`  
> loanQuotaCoef | String | Loan quota coefficient. Loan quota = `quota` * `level`  
> irDiscount | String | ~~Interest rate discount~~(Deprecated)  
configCcyList | Array of strings | Currencies that have loan quota configured using customized absolute value.  
Users should refer to config to get the loan quota of a currency which is listed in configCcyList, instead of getting it from basic/vip/regular.  
> ccy | String | Currency  
> rate | String | Daily rate  
config | Array of objects | The currency details of loan quota configured using customized absolute value  
> ccy | String | Currency  
> stgyType | String | Strategy type  
`0`: general strategy  
`1`: delta neutral strategy  
If only `0` is returned for a currency, it means the loan quota is shared between accounts in general strategy and accounts in delta neutral strategy; if both `0/1` are returned for a currency, it means accounts in delta neutral strategy have separate loan quotas.  
> quota | String | Loan quota in absolute value  
> level | String | VIP level

---

# 获取市场借币杠杆利率和借币限额

#### 限速：2次/2s  
  
#### 限速规则：IP

#### HTTP请求

`GET /api/v5/public/interest-rate-loan-quota`

> 请求示例
    
    
    GET /api/v5/public/interest-rate-loan-quota
    
    
    
    import okx.PublicData as PublicData
    
    flag = "0"  # 实盘:0 , 模拟盘：1
    
    publicDataAPI = PublicData.PublicAPI(flag=flag)
    
    # 获取市场借币杠杆利率和借币限额
    result = publicDataAPI.get_interest_rate_loan_quota()
    print(result)
    

> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "configCcyList": [
                    {
                        "ccy": "USDT",
                        "rate": "0.00043728",
                    }
                ],
                "basic": [
                    {
                        "ccy": "USDT",
                        "quota": "500000",
                        "rate": "0.00043728"
                    },
                    {
                        "ccy": "BTC",
                        "quota": "10",
                        "rate": "0.00019992"
                    }
                ],
                "vip": [
                    {
                        "irDiscount": "",
                        "loanQuotaCoef": "6",
                        "level": "VIP1"
                    },
                    {
                        "irDiscount": "",
                        "loanQuotaCoef": "7",
                        "level": "VIP2"
                    }
                ],
                "config": [
                    {
                        "ccy": "USDT",
                        "stgyType": "0",    // normal
                        "quota": "xxxxxx",
                        "level": "VIP 8"
                    },
                    ......
                    {
                        "ccy": "USDT",
                        "stgyType": "1",    // delta neutral
                        "quota": "xxxxx",
                        "level": "VIP 1"
                    },
                    ......
                ],
                "regular": [
                    {
                        "irDiscount": "",
                        "loanQuotaCoef": "1",
                        "level": "Lv1"
                    }
                ]
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
basic | Array of objects | 基础利率和借币限额  
> ccy | String | 币种  
> rate | String | 日借币利率  
> quota | String | 基础借币限额  
vip | Array of objects | 专业用户  
> level | String | 账户交易手续费等级，如 `VIP1`  
> loanQuotaCoef | String | 借币限额系数，借币限额 = 基础借币限额 * 该系数  
> irDiscount | String | ~~利率的折扣率~~(已废弃)  
regular | Array of objects | 普通用户  
> level | String | 账户交易手续费等级，如 `Lv1`  
> loanQuotaCoef | String | 借币限额系数，借币限额 = 基础借币限额 * 该系数  
> irDiscount | String | ~~利率的折扣率~~(已废弃)  
configCcyList | Array of strings | 由自定义绝对值方式配置借币限额的币种  
当币种在configCcyList中时，用户应该参考config以获取相应限额，而非使用basic/vip/regular  
> ccy | String | 币种  
> rate | String | 基础杠杆日利率  
config | Array of objects | 由自定义绝对值方式配置借币限额的币种详情  
> ccy | String | 币种  
> stgyType | String | 策略类型  
`0`：普通策略模式  
`1`：delta 中性策略模式  
如果某个币种仅返回0，则表示该借贷额度由普通策略模式的账户和 delta 中性策略模式的账户共享；如果某个币种同时返回0/1，则表示 delta 中性策略模式的账户拥有单独的借贷额度。  
> quota | String | 借币限额  
> level | String | 账户交易手续费等级，如 `VIP1`