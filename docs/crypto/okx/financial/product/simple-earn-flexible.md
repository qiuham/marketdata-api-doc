---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#financial-product-simple-earn-flexible
anchor_id: financial-product-simple-earn-flexible
api_type: API
updated_at: 2026-07-13 19:29:33.786584
---

# Simple earn flexible

Simple earn flexible (saving) is earned by lending to leveraged trading users in the lending market. [learn more](/earn/simple-earn)  
  
### GET / Saving balance

#### Rate Limit: 6 requests per second

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/finance/savings/balance`

> Request Example
    
    
    GET /api/v5/finance/savings/balance?ccy=USDT
    
    
    
    
    import okx.Finance.Savings as Savings
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    SavingsAPI = Savings.SavingsAPI(apikey, secretkey, passphrase, False, flag)
    
    result = SavingsAPI.get_saving_balance(ccy="USDT")
    print(result)
    

#### Request Parameters

**Parameters** | **Types** | **Required** | **Description**  
---|---|---|---  
ccy | String | No | Currency, e.g. `BTC`  
  
> Response Example
    
    
    {
        "code": "0",
        "msg":"",
        "data": [
            {
                "earnings": "0.0010737388791526",
                "redemptAmt": "",
                "rate": "0.0100000000000000",
                "ccy": "USDT",
                "amt": "11.0010737453457821",
                "loanAmt": "11.0010630707982819",
                "pendingAmt": "0.0000106745475002"
            }
        ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ccy | String | Currency  
amt | String | Currency amount  
earnings | String | Currency earnings  
rate | String | Minimum annual lending rate configured by users  
loanAmt | String | Lending amount  
pendingAmt | String | Pending amount  
redemptAmt | String | ~~Redempting amount~~ (Deprecated)  
  
### POST / Savings purchase/redemption

Only the assets in the funding account can be used for saving.

#### Rate Limit: 6 requests per second

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/finance/savings/purchase-redempt`

> Request Example
    
    
    POST /api/v5/finance/savings/purchase-redempt
    body
    {
        "ccy":"BTC",
        "amt":"1",
        "side":"purchase",
        "rate":"0.01"
    }
    
    
    
    
    import okx.Finance.Savings as Savings
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    SavingsAPI = Savings.SavingsAPI(apikey, secretkey, passphrase, False, flag)
    
    result = SavingsAPI.savings_purchase_redemption(ccy='USDT',amt="0.1",side="purchase",rate="1")
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
ccy | String | Yes | Currency, e.g. `BTC`  
amt | String | Yes | Purchase/redemption amount  
side | String | Yes | Action type.   
`purchase`: purchase saving shares   
`redempt`: redeem saving shares  
rate | String | Conditional | Annual purchase rate, e.g. `0.1` represents `10%`  
Only applicable to purchase saving shares  
The interest rate of the new subscription will cover the interest rate of the last subscription  
The rate value range is between 1% and 365%  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "ccy":"BTC",
                "amt":"1",
                "side":"purchase",
                "rate": "0.01"
            }
        ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ccy | String | Currency  
amt | String | Purchase/Redemption amount  
side | String | Action type  
rate | String | Annual purchase rate, e.g. `0.1` represents `10%`  
  
### POST / Set lending rate

#### Rate Limit: 6 requests per second

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/finance/savings/set-lending-rate`

> Request Example
    
    
    POST /api/v5/finance/savings/set-lending-rate
    body
    {
        "ccy":"BTC",
        "rate":"0.02"
    }
    
    
    
    
    import okx.Finance.Savings as Savings
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    SavingsAPI = Savings.SavingsAPI(apikey, secretkey, passphrase, False, flag)
    
    result = SavingsAPI.set_lending_rate(ccy='USDT',rate="1")
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
ccy | String | Yes | Currency, e.g. `BTC`  
rate | String | Yes | Annual lending rate  
The rate value range is between 1% and 365%  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
            "ccy": "BTC",
            "rate": "0.02"
        }]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ccy | String | Currency, e.g. `BTC`  
rate | String | Annual lending rate  
  
### GET / Lending history

Return data in the past month.

#### Rate Limit: 6 requests per second

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/finance/savings/lending-history`

> Request Example
    
    
    GET /api/v5/finance/savings/lending-history
    
    
    
    
    import okx.Finance.Savings as Savings
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    SavingsAPI = Savings.SavingsAPI(apikey, secretkey, passphrase, False, flag)
    
    result = SavingsAPI.get_lending_history()
    print(result)
    

#### Request Parameters

**Parameters** | **Types** | **Required** | **Description**  
---|---|---|---  
ccy | String | No | Currency, e.g. `BTC`  
after | String | No | Pagination of data to return records earlier than the requested `ts`, Unix timestamp format in milliseconds, e.g. `1597026383085`  
before | String | No | Pagination of data to return records newer than the requested `ts`, Unix timestamp format in milliseconds, e.g. `1597026383085`  
limit | String | No | Number of results per request. The maximum is `100`. The default is `100`.  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
                "ccy": "BTC",
                "amt": "0.01",
                "earnings": "0.001",
                "rate": "0.01",
                "ts": "1597026383085"
            },
            {
                "ccy": "ETH",
                "amt": "0.2",
                "earnings": "0.001",
                "rate": "0.01",
                "ts": "1597026383085"
            }
        ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ccy | String | Currency, e.g. `BTC`  
amt | String | Lending amount  
earnings | String | Currency earnings  
rate | String | Lending annual interest rate  
ts | String | Lending time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
### GET / Public borrow info (public)

Authentication is not required for this public endpoint.

#### Rate Limit: 6 requests per second

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/finance/savings/lending-rate-summary`

> Request Example
    
    
    GET /api/v5/finance/savings/lending-rate-summary
    
    
    
    
    import okx.Finance.Savings as Savings
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    SavingsAPI = Savings.SavingsAPI(flag=flag)
    
    result = SavingsAPI.get_public_borrow_info()
    print(result)
    

#### Request Parameters

**Parameters** | **Types** | **Required** | **Description**  
---|---|---|---  
ccy | String | No | Currency, e.g. `BTC`  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
            "ccy": "BTC",
            "avgAmt": "10000",
            "avgAmtUsd": "10000000000",
            "avgRate": "0.03",
            "preRate": "0.02",
            "estRate": "0.01"
        }]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ccy | String | Currency, e.g. `BTC`  
avgAmt | String | ~~24H average borrowing amount~~(deprecated)  
avgAmtUsd | String | ~~24H average borrowing amount in`USD` value~~(deprecated)  
avgRate | String | 24-hours average annual borrowing rate  
preRate | String | Last annual borrowing interest rate  
estRate | String | Next estimate annual borrowing interest rate  
  
### GET / Public borrow history (public)

Authentication is not required for this public endpoint.  
Only returned records after December 14, 2021.

#### Rate Limit: 6 requests per second

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/finance/savings/lending-rate-history`

> Request Example
    
    
    GET /api/v5/finance/savings/lending-rate-history
    
    
    
    
    import okx.Finance.Savings as Savings
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    SavingsAPI = Savings.SavingsAPI(flag=flag)
    
    result = SavingsAPI.get_public_borrow_history()
    print(result)
    

#### Request Parameters

**Parameters** | **Types** | **Required** | **Description**  
---|---|---|---  
ccy | String | No | Currency, e.g. `BTC`  
after | String | No | Pagination of data to return records earlier than the requested `ts`, Unix timestamp format in milliseconds, e.g. `1597026383085`  
before | String | No | Pagination of data to return records newer than the requested `ts`, Unix timestamp format in milliseconds, e.g. `1597026383085`  
limit | String | No | Number of results per request. The maximum is `100`. The default is `100`.  
If `ccy` is not specified, all data under the same `ts` will be returned, not limited by `limit`  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
            "ccy": "BTC",
            "amt": "0.01",
            "rate": "0.001",
            "lendingRate": "0.001",
            "ts": "1597026383085"
        }]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ccy | String | Currency, e.g. `BTC`  
amt | String | ~~Lending amount~~(deprecated)  
rate | String | Annual borrowing interest rate  
lendingRate | String | Annual lending interest rate  
ts | String | Time, Unix timestamp format in milliseconds, e.g. `1597026383085`

---

# 活期简单赚币

活期简单赚币通过在借贷市场出借给杠杆交易用户获取收益。[了解更多](/cn/earn/simple-earn)  
  
### GET / 获取活期简单赚币余额 

#### 限速：6次/s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/finance/savings/balance`

> 请求示例
    
    
    GET /api/v5/finance/savings/balance?ccy=BTC
    
    
    
    
    import okx.Finance.Savings as Savings
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    SavingsAPI = Savings.SavingsAPI(apikey, secretkey, passphrase, False, flag)
    
    result = SavingsAPI.get_saving_balance(ccy="USDT")
    print(result)
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 否 | 币种，如 `BTC`  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg":"",
        "data": [
            {
                "earnings": "0.0010737388791526",
                "redemptAmt": "",
                "rate": "0.0100000000000000",
                "ccy": "USDT",
                "amt": "11.0010737453457821",
                "loanAmt": "11.0010630707982819",
                "pendingAmt": "0.0000106745475002"
            }
        ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ccy | String | 币种，如 `BTC`  
amt | String | 币种数量  
earnings | String | 币种持仓收益  
rate | String | 用户配置的最低年化出借利率  
loanAmt | String | 已出借数量  
pendingAmt | String | 未出借数量  
redemptAmt | String | ~~赎回中的数量~~ （已废弃）  
  
### POST / 活期简单赚币申购/赎回 

仅资金账户中的资产支持活期简单赚币申购。

#### 限速：6次/s

#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/finance/savings/purchase-redempt`

> 请求示例
    
    
    POST /api/v5/finance/savings/purchase-redempt
    body
    {
        "ccy":"BTC",
        "amt":"1",
        "side":"purchase",
        "rate":"0.01"
    }
    
    
    
    
    import okx.Finance.Savings as Savings
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    SavingsAPI = Savings.SavingsAPI(apikey, secretkey, passphrase, False, flag)
    
    result = SavingsAPI.savings_purchase_redemption(ccy='USDT',amt="0.1",side="purchase",rate="1")
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 是 | 币种名称，如 `BTC`  
amt | String | 是 | 申购/赎回 数量  
side | String | 是 | 操作类型  
`purchase`：申购 `redempt`：赎回  
rate | String | 可选 | 申购年利率，如 `0.1`代表`10%`  
仅适用于申购，新申购的利率会覆盖上次申购的利率  
参数取值范围在1%到365%之间  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "ccy":"BTC",
                "amt":"1",
                "side":"purchase",
                "rate":"0.01"
            }
        ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ccy | String | 币种名称  
amt | String | 申购/赎回 数量  
side | String | 操作类型  
rate | String | 申购年利率，如 `0.1`代表`10%`  
  
### POST / 设置活期简单赚币借贷利率 

#### 限速：6次/s

#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/finance/savings/set-lending-rate`

> 请求示例
    
    
    POST /api/v5/finance/savings/set-lending-rate
    body
    {
        "ccy":"BTC",
        "rate":"0.02"
    }
    
    
    
    
    import okx.Finance.Savings as Savings
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    SavingsAPI = Savings.SavingsAPI(apikey, secretkey, passphrase, False, flag)
    
    result = SavingsAPI.set_lending_rate(ccy='USDT',rate="1")
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 是 | 币种名称，如 `BTC`  
rate | String | 是 | 贷出年利率  
参数取值范围在1%到365%之间  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
            "ccy": "BTC",
            "rate": "0.02"
        }]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ccy | String | 币种名称，如 `BTC`  
rate | String | 贷出年利率  
  
### GET / 获取活期简单赚币出借明细 

返回最近一个月的数据

#### 限速：6次/s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/finance/savings/lending-history`

> 请求示例
    
    
    GET /api/v5/finance/savings/lending-history
    
    
    
    
    import okx.Finance.Savings as Savings
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    SavingsAPI = Savings.SavingsAPI(apikey, secretkey, passphrase, False, flag)
    
    result = SavingsAPI.get_lending_history()
    print(result)
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 否 | 币种，如 `BTC`  
after | String | 否 | 查询在此之前的内容，值为时间戳，Unix 时间戳为毫秒数格式，如 `1597026383085`  
before | String | 否 | 查询在此之后的内容，值为时间戳，Unix 时间戳为毫秒数格式，如 `1597026383085`  
limit | String | 否 | 分页返回的结果集数量，最大为 100，不填默认返回 100 条  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
                "ccy": "BTC",
                "amt": "0.01",
                "earnings": "0.001",
                "rate": "0.01",
                "ts": "1597026383085"
            },
            {
                "ccy": "ETH",
                "amt": "0.2",
                "earnings": "0.001",
                "rate": "0.01",
                "ts": "1597026383085"
            }
        ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ccy | String | 币种，如 `BTC`  
amt | String | 出借数量  
earnings | String | 已赚取利息  
rate | String | 出借年利率  
ts | String | 出借时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
  
### GET / 获取市场借贷信息（公共）

公共接口无须鉴权

#### 限速：6次/s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/finance/savings/lending-rate-summary`

> 请求示例
    
    
    GET /api/v5/finance/savings/lending-rate-summary
    
    
    
    
    import okx.Finance.Savings as Savings
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    SavingsAPI = Savings.SavingsAPI(flag=flag)
    
    result = SavingsAPI.get_public_borrow_info()
    print(result)
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 否 | 币种，如 `BTC`  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
            "ccy": "BTC",
            "avgAmt": "10000",
            "avgAmtUsd": "10000000000",
            "avgRate": "0.03",
            "preRate": "0.02",
            "estRate": "0.01"
        }]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ccy | String | 币种，如 `BTC`  
avgAmt | String | ~~过去24小时平均借贷量~~(已弃用)  
avgAmtUsd | String | ~~过去24小时平均借贷美元价值~~(已弃用)  
avgRate | String | 过去24小时平均借入年利率  
preRate | String | 上一次借入年利率  
estRate | String | 下一次预估借入年利率  
  
### GET / 获取市场借贷历史（公共） 

公共接口无须鉴权  
返回2021年12月14日后的记录  

#### 限速：6次/s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/finance/savings/lending-rate-history`

> 请求示例
    
    
    GET /api/v5/finance/savings/lending-rate-history
    
    
    
    
    import okx.Finance.Savings as Savings
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    SavingsAPI = Savings.SavingsAPI(flag=flag)
    
    result = SavingsAPI.get_public_borrow_history()
    print(result)
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 否 | 币种，如 `BTC`  
after | String | 否 | 查询在此之前的内容，值为时间戳，Unix 时间戳为毫秒数格式，如 `1597026383085`  
before | String | 否 | 查询在此之后的内容，值为时间戳，Unix 时间戳为毫秒数格式，如 `1597026383085`  
limit | String | 否 | 分页返回的结果集数量，最大为100，不填默认返回100条  
如果不指定`ccy`,会返回同一个`ts`下的全部数据，不受`limit`限制  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
            "ccy": "BTC",
            "amt": "0.01",
            "rate": "0.001",
            "lendingRate": "0.001",
            "ts": "1597026383085"
        }]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ccy | String | 币种，如 `BTC`  
amt | String | ~~市场总出借数量~~ （已弃用）  
rate | String | 出借年利率  
lendingRate | String | 年化出借利率  
ts | String | 时间，Unix时间戳的毫秒数格式，如 `1597026383085`