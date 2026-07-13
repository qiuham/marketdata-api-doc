---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#financial-product-sol-staking
anchor_id: financial-product-sol-staking
api_type: API
updated_at: 2026-07-13 19:29:28.130648
---

# SOL staking

By staking SOL tokens and delegating them to validators on the Solana network, you can receive equivalent OKSOL and earn extra OKSOL rewards.  
Stake SOL on Solana to receive OKSOL at a 1:1 ratio for liquidity  
[Learn more about OKSOL Staking](/earn/solana-staking#from=finance_crypto)  
  
### GET / Product info

#### Rate Limit: 3 requests per second

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/finance/staking-defi/sol/product-info`

> Request Example
    
    
    GET /api/v5/finance/staking-defi/sol/product-info
    
    
    
    
    

> Response Example
    
    
    {
        "code": "0",
        "data": {
            "fastRedemptionAvail": "240",
            "fastRedemptionDailyLimit": "240",
            "rate": "5.57",
            "redemptDays": "2",
            "minAmt": "0.01"
        },
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
fastRedemptionDailyLimit | String | Fast redemption daily limit  
The master account and sub-accounts share the same limit  
fastRedemptionAvail | String | Currently fast redemption max available amount  
rate | String | Latest OKSOL APY  
redemptDays | String | Redemption days of OKSOL  
minAmt | String | Minimum subscription amount of OKSOL  
  
### POST / Purchase

Staking SOL for OKSOL  
Only the assets in the funding account can be used.  

#### Rate Limit: 2 requests per second

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/finance/staking-defi/sol/purchase`

> Request Example
    
    
    POST /api/v5/finance/staking-defi/sol/purchase
    body 
    {
        "amt":"100"
    }
    
    
    
    import okx.Finance.SolStaking as SolStaking
    
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    StackingAPI = SolStaking.SolStakingAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StackingAPI.sol_purchase(amt="1")
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
amt | String | Yes | Investment amount  
  
> Response Example
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
      ]
    }
    

#### Response Parameters

code = `0` means your request has been successfully handled.

### POST / Redeem

Only the assets in the funding account can be used. If your OKSOL is in your trading account, you can make funding transfer first.  

#### Rate Limit: 2 requests per second

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/finance/staking-defi/sol/redeem`

> Request Example
    
    
    POST /api/v5/finance/staking-defi/sol/redeem
    body 
    {
        "amt": "10"
    }
    
    
    
    import okx.Finance.SolStaking as SolStaking
    
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    StackingAPI = SolStaking.SolStakingAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StackingAPI.sol_redeem(amt="1")
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
amt | String | Yes | Redeeming amount  
  
> Response Example
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
      ]
    }
    

#### Response Parameters

code = `0` means your request has been successfully handled.

### GET / Balance

The balance represents the real-time total OKSOL holdings across the entire account, including assets in the trading account, funding account, and those currently in the redeeming process.

#### Rate Limit: 6 requests per second

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/finance/staking-defi/sol/balance`

> Request Example
    
    
    GET /api/v5/finance/staking-defi/sol/balance
    
    
    
    import okx.Finance.SolStaking as SolStaking
    
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    StackingAPI = SolStaking.SolStakingAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StackingAPI.sol_balance()
    print(result)
    

#### Request Parameters

None

> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "amt": "0.01100012",
                "ccy": "OKSOL",
                "latestInterestAccrual": "0.00000012",
                "totalInterestAccrual": "0.00000012"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ccy | String | Currency, e.g. `OKSOL`  
amt | String | Currency amount  
latestInterestAccrual | String | Latest interest accrual  
totalInterestAccrual | String | Total interest accrual  
  
### GET / Purchase&Redeem history

#### Rate Limit: 6 requests per second

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/finance/staking-defi/sol/purchase-redeem-history`

> Request Example
    
    
    GET /api/v5/finance/staking-defi/sol/purchase-redeem-history
    
    
    
    import okx.Finance.SolStaking as SolStaking
    
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    StackingAPI = SolStaking.SolStakingAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StackingAPI.sol_purchase_redeem_history()
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
type | String | No | Type  
`purchase`  
`redeem`  
status | String | No | Status  
`pending`  
`success`  
`failed`  
after | String | No | Pagination of data to return records earlier than the `requestTime`. The value passed is the corresponding `timestamp`  
before | String | No | Pagination of data to return records newer than the `requestTime`. The value passed is the corresponding `timestamp`  
limit | String | No | Number of results per request. The default is `100`. The maximum is `100`.  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "amt": "0.62666630",
                "completedTime": "1683413171000",
                "estCompletedTime": "",
                "redeemingAmt": "",
                "requestTime": "1683413171000",
                "status": "success",
                "type": "purchase"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
type | String | Type  
`purchase`  
`redeem`  
amt | String | Purchase/Redeem amount  
redeemingAmt | String | Redeeming amount  
status | String | Status  
`pending`  
`success`  
`failed`  
requestTime | String | Request time of make purchase/redeem, Unix timestamp format in milliseconds, e.g. `1597026383085`  
completedTime | String | Completed time of redeem settlement, Unix timestamp format in milliseconds, e.g. `1597026383085`  
estCompletedTime | String | Estimated completed time of redeem settlement, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
### GET / APY history (Public)

Public endpoints don't need authorization.

#### Rate Limit: 6 requests per second

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/finance/staking-defi/sol/apy-history`

> Request Example
    
    
    GET /api/v5/finance/staking-defi/sol/apy-history?days=2
    
    
    
    
    import okx.Finance.SolStaking as SolStaking
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    StackingAPI = SolStaking.SolStakingAPI(flag=flag)
    
    result = StackingAPI.sol_apy_history(days="7")
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
days | String | Yes | Get the days of APY(Annual percentage yield) history record in the past  
No more than 365 days  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "rate": "0.11280000",
                "ts": "1734192000000"
            },
            {
                "rate": "0.11270000",
                "ts": "1734105600000"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
rate | String | APY(Annual percentage yield), e.g. `0.01` represents `1%`  
ts | String | Data time, Unix timestamp format in milliseconds, e.g. `1597026383085`

---

# SOL质押

通过质押 SOL 代币并将其委托给 Solana 网络上的验证者，您可以收到等值的 OKSOL 并获得每日 OKSOL 奖励。  
在 Solana 上质押 SOL，即获 1:1 OKSOL，享受更高流动性  
[了解更多](/zh-hans/earn/solana-staking#from=finance_crypto)  
  
### GET / 获取产品信息 

#### 限速：3 次/s

#### 限速规则：User ID

#### 权限：读取

#### HTTP 请求

`GET /api/v5/finance/staking-defi/sol/product-info`

> 请求示例
    
    
    GET /api/v5/finance/staking-defi/sol/product-info
    
    
    
    
    

> 返回结果
    
    
    {
        "code": "0",
        "data": {
            "fastRedemptionAvail": "240",
            "fastRedemptionDailyLimit": "240",
            "rate": "5.57",
            "redemptDays": "2",
            "minAmt": "0.01"
        },
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
fastRedemptionDailyLimit | String | 快速赎回每日最高份额  
母账户和子账户共享同一个限额  
fastRedemptionAvail | String | 当前剩余最大可赎回数量  
rate | String | 最新 OKSOL 年化收益率  
redemptDays | String | OKSOL 赎回天数  
minAmt | String | OKSOL 最低申购数量  
  
### POST / 申购 

质押 SOL 获取 OKSOL  
仅资金账户中的资产支持 SOL 质押。

#### 限速：2次/s

#### 限速规则：User ID

#### 权限：交易

#### HTTP 请求

`POST /api/v5/finance/staking-defi/sol/purchase`

> 请求示例
    
    
    POST /api/v5/finance/staking-defi/sol/purchase
    body 
    {
        "amt":"100"
    }
    
    
    
    import okx.Finance.SolStaking as SolStaking
    
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    StackingAPI = SolStaking.SolStakingAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StackingAPI.sol_purchase(amt="1")
    print(result)
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
amt | String | 是 | 投资数量  
  
> 返回结果
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
      ]
    }
    

#### 返回参数

code = `0`代表请求已被成功处理

### POST / 赎回 

只能赎回资金账户中的 OKSOL 资产，交易账户中的 OKSOL 资产需要您先做资金划转到资金账户后赎回。

#### 限速：2次/s

#### 限速规则：User ID

#### 权限：交易

#### HTTP 请求

`POST /api/v5/finance/staking-defi/sol/redeem`

> 请求示例
    
    
    POST /api/v5/finance/staking-defi/sol/redeem
    body 
    {
        "amt":"10"
    }
    
    
    
    import okx.Finance.SolStaking as SolStaking
    
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    StackingAPI = SolStaking.SolStakingAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StackingAPI.sol_redeem(amt="1")
    print(result)
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
amt | String | 是 | 赎回数量  
  
> 返回结果
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
      ]
    }
    

#### 返回参数

code = `0`代表请求已被成功处理

### GET / 获取余额 

该余额表示账户内 OKSOL 的实时总持仓，包括交易账户、资金账户以及处于赎回过程中的资产。

#### 限速：6 次/s

#### 限速规则：User ID

#### 权限：读取

#### HTTP 请求

`GET /api/v5/finance/staking-defi/sol/balance`

> 请求示例
    
    
    GET /api/v5/finance/staking-defi/sol/balance
    
    
    
    
    import okx.Finance.SolStaking as SolStaking
    
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    StackingAPI = SolStaking.SolStakingAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StackingAPI.sol_balance()
    print(result)
    

#### 请求参数

None

> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "amt": "0.01100012",
                "ccy": "OKSOL",
                "latestInterestAccrual": "0.00000012",
                "totalInterestAccrual": "0.00000012"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ccy | String | 币种名称，如 `OKSOL`  
amt | String | 币种数量  
latestInterestAccrual | String | 最近收益  
totalInterestAccrual | String | 历史总收益  
  
### GET / 获取申购赎回记录 

#### 限速：6 次/s

#### 限速规则：User ID

#### 权限：读取

#### HTTP 请求

`GET /api/v5/finance/staking-defi/sol/purchase-redeem-history`

> 请求示例
    
    
    GET /api/v5/finance/staking-defi/sol/purchase-redeem-history
    
    
    
    
    import okx.Finance.SolStaking as SolStaking
    
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    StackingAPI = SolStaking.SolStakingAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StackingAPI.sol_purchase_redeem_history()
    print(result)
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
type | String | 否 | 类型  
`purchase`：申购  
`redeem`：赎回  
status | String | 否 | 状态  
`pending`：处理中  
`success`：成功处理  
`failed`：处理失败  
after | String | 否 | 请求此`requestTime`之前（更旧的数据）的分页内容，值为时间戳，Unix 时间戳为毫秒数格式，如 `1597026383085`  
before | String | 否 | 请求此`requestTime`之后（更新的数据）的分页内容，值为时间戳，Unix 时间戳为毫秒数格式，如 `1597026383085`  
limit | String | 否 | 返回结果的数量，默认100条，最大值为100条  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "amt": "0.62666630",
                "completedTime": "1683413171000",
                "estCompletedTime": "",
                "redeemingAmt": "",
                "requestTime": "1683413171000",
                "status": "success",
                "type": "purchase"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
type | String | 类型  
`purchase`：申购  
`redeem`：赎回  
amt | String | 申购/赎回 的数量  
redeemingAmt | String | 赎回中的数量  
status | String | 状态  
`pending`：处理中  
`success`：成功处理  
`failed`：处理失败  
requestTime | String | 发起 申购/赎回 请求的时间，值为时间戳，Unix时间戳为毫秒数格式，如 `1597026383085`  
completedTime | String | 赎回请求处理完成的时间，值为时间戳，Unix时间戳为毫秒数格式，如 `1597026383085`  
estCompletedTime | String | 预估完成赎回的时间，值为时间戳，Unix时间戳为毫秒数格式，如 `1597026383085`  
  
### GET / 获取历史收益率(公共) 

公共接口无须鉴权

#### 限速：6次/s

#### 限速规则：IP

#### HTTP 请求

`GET /api/v5/finance/staking-defi/sol/apy-history`

> 请求示例
    
    
    GET /api/v5/finance/staking-defi/sol/apy-history?days=2
    
    
    
    
    import okx.Finance.SolStaking as SolStaking
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    StackingAPI = SolStaking.SolStakingAPI(flag=flag)
    
    result = StackingAPI.sol_apy_history(days="7")
    print(result)
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
days | String | 是 | 查询最近多少天内的数据，不超过365天  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "rate": "0.11280000",
                "ts": "1734192000000"
            },
            {
                "rate": "0.11270000",
                "ts": "1734105600000"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
rate | String | 年化收益率，如 `0.01`代表`1%`  
ts | String | 时间，值为时间戳，Unix时间戳为毫秒数格式，如 `1597026383085`