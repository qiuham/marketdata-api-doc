---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#financial-product-eth-staking
anchor_id: financial-product-eth-staking
api_type: API
updated_at: 2026-07-11 19:14:30.092348
---

# ETH staking

ETH Staking, also known as Ethereum Staking, is the process of participating in the Ethereum blockchain's Proof-of-Stake (PoS) consensus mechanism.  
Stake to receive BETH for liquidity at 1:1 ratio and earn daily BETH rewards  
[Learn more about ETH Staking](https://www.okx.com/earn/ethereum-staking)  
  
### GET / Product info

#### Rate Limit: 3 requests per second

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/finance/staking-defi/eth/product-info`

> Request Example
    
    
    GET /api/v5/finance/staking-defi/eth/product-info
    
    
    
    
    import okx.Finance.EthStaking as EthStaking
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    StackingAPI = EthStaking.EthStakingAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StackingAPI.eth_product_info()
    print(result)
    

> Response Example
    
    
    {
        "code": "0",
        "data": [
          {
            "fastRedemptionDailyLimit": "100",
            "rate": "2.23",
            "redemptDays": "8",
            "minAmt": "0.001"
          }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
fastRedemptionDailyLimit | String | Fast redemption daily limit  
The master account and sub-accounts share the same limit  
rate | String | Latest BETH APY  
redemptDays | String | Redemption days of BETH  
minAmt | String | Minimum subscription amount of BETH  
  
### POST / Purchase

Staking ETH for BETH  
Only the assets in the funding account can be used.  

#### Rate Limit: 2 requests per second

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/finance/staking-defi/eth/purchase`

> Request Example
    
    
    POST /api/v5/finance/staking-defi/eth/purchase
    body 
    {
        "amt":"100"
    }
    
    
    
    import okx.Finance.EthStaking as EthStaking
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    StackingAPI = EthStaking.EthStakingAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StackingAPI.eth_purchase(amt="1")
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

Only the assets in the funding account can be used. If your BETH is in your trading account, you can make funding transfer first.  

#### Rate Limit: 2 requests per second

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/finance/staking-defi/eth/redeem`

> Request Example
    
    
    POST /api/v5/finance/staking-defi/eth/redeem
    body 
    {
        "amt": "10"
    }
    
    
    
    import okx.Finance.EthStaking as EthStaking
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    StackingAPI = EthStaking.EthStakingAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StackingAPI.eth_redeem(amt="1")
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

### POST / Cancel redeem

#### Rate Limit: 2 requests per second

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/finance/staking-defi/eth/cancel-redeem`

> Request Example
    
    
    POST /api/v5/finance/staking-defi/eth/cancel-redeem
    body
    {
        "ordId": "1234567890"
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
ordId | String | Yes | Order ID  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "ordId": "1234567890"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ordId | String | Order ID  
  
### GET / Balance

The balance represents the real-time total BETH holdings across the entire account, including assets in the trading account, funding account, and those currently in the redeeming process.

#### Rate Limit: 6 requests per second

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/finance/staking-defi/eth/balance`

> Request Example
    
    
    GET /api/v5/finance/staking-defi/eth/balance
    
    
    
    import okx.Finance.EthStaking as EthStaking
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    StackingAPI = EthStaking.EthStakingAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StackingAPI.eth_balance()
    print(result)
    

#### Request Parameters

None

> Response Example
    
    
    {
        "code": "0",
        "data": [
          {
            "amt": "0.63926191",
            "ccy": "BETH",
            "latestInterestAccrual": "0.00006549",
            "totalInterestAccrual": "0.01490596",
            "ts": "1699257600000"
          }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ccy | String | Currency, e.g. `BETH`  
amt | String | Currency amount  
latestInterestAccrual | String | Latest interest accrual  
totalInterestAccrual | String | Total interest accrual  
ts | String | Query data time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
### GET / Purchase&Redeem history

#### Rate Limit: 6 requests per second

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/finance/staking-defi/eth/purchase-redeem-history`

> Request Example
    
    
    GET /api/v5/finance/staking-defi/eth/purchase-redeem-history
    
    
    
    import okx.Finance.EthStaking as EthStaking
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    StackingAPI = EthStaking.EthStakingAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StackingAPI.eth_purchase_redeem_history()
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
`cancelled`  
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
`cancelled`  
ordId | String | Order ID  
requestTime | String | Request time of make purchase/redeem, Unix timestamp format in milliseconds, e.g. `1597026383085`  
completedTime | String | Completed time of redeem settlement, Unix timestamp format in milliseconds, e.g. `1597026383085`  
estCompletedTime | String | Estimated completed time of redeem settlement, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
### GET / APY history (Public)

Public endpoints don't need authorization.

#### Rate Limit: 6 requests per second

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/finance/staking-defi/eth/apy-history`

> Request Example
    
    
    GET /api/v5/finance/staking-defi/eth/apy-history?days=2
    
    
    
    
    import okx.Finance.EthStaking as EthStaking
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    StackingAPI = EthStaking.EthStakingAPI(flag=flag)
    
    result = StackingAPI.eth_apy_history(days="7")
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
                "rate": "0.02690000",
                "ts": "1734195600000"
            },
            {
                "rate": "0.02840000",
                "ts": "1734109200000"
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

# ETH质押

ETH 质押，也称为以太坊质押，是参与以太坊区块链权益证明 (Proof of Stake, PoS) 共识机制的过程。  
质押 ETH 即获 1:1 BETH 并赚取每日奖励，享受更高流动性  
[了解更多](https://www.okx.com/zh-hans/earn/ethereum-staking)  
  
### GET / 获取产品信息 

#### 限速：3 次/s

#### 限速规则：User ID

#### 权限：读取

#### HTTP 请求

`GET /api/v5/finance/staking-defi/eth/product-info`

> 请求示例
    
    
    GET /api/v5/finance/staking-defi/eth/product-info
    
    
    
    
    import okx.Finance.EthStaking as EthStaking
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    StackingAPI = EthStaking.EthStakingAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StackingAPI.eth_product_info()
    print(result)
    

> 返回结果
    
    
    {
        "code": "0",
        "data": [
          {
            "fastRedemptionDailyLimit": "100",
            "rate": "2.23",
            "redemptDays": "8",
            "minAmt": "0.001"
          }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
fastRedemptionDailyLimit | String | 快速赎回每日最高份额  
母账户和子账户共享同一个限额  
rate | String | 最新 BETH 年化收益率  
redemptDays | String | BETH 赎回天数  
minAmt | String | BETH 最低申购数量  
  
### POST / 申购 

质押ETH获取BETH  
仅资金账户中的资产支持ETH质押。

#### 限速：2次/s

#### 限速规则：User ID

#### 权限：交易

#### HTTP 请求

`POST /api/v5/finance/staking-defi/eth/purchase`

> 请求示例
    
    
    POST /api/v5/finance/staking-defi/eth/purchase
    body 
    {
        "amt":"100"
    }
    
    
    
    import okx.Finance.EthStaking as EthStaking
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    StackingAPI = EthStaking.EthStakingAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StackingAPI.eth_purchase(amt="1")
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

只能赎回资金账户中的 BETH 资产，交易账户中的 BETH 资产需要您先做资金划转到资金账户后赎回。

#### 限速：2次/s

#### 限速规则：User ID

#### 权限：交易

#### HTTP 请求

`POST /api/v5/finance/staking-defi/eth/redeem`

> 请求示例
    
    
    POST /api/v5/finance/staking-defi/eth/redeem
    body 
    {
        "amt":"10"
    }
    
    
    
    import okx.Finance.EthStaking as EthStaking
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    StackingAPI = EthStaking.EthStakingAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StackingAPI.eth_redeem(amt="1")
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

### POST / 撤销赎回 

#### 限速：2 次/s

#### 限速规则：User ID

#### 权限：交易

#### HTTP 请求

`POST /api/v5/finance/staking-defi/eth/cancel-redeem`

> 请求示例
    
    
    POST /api/v5/finance/staking-defi/eth/cancel-redeem
    body
    {
        "ordId": "1234567890"
    }
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
ordId | String | 是 | 订单ID  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "ordId": "1234567890"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ordId | String | 订单ID  
  
### GET / 获取余额 

该余额表示账户内 BETH 的实时总持仓，包括交易账户、资金账户以及处于赎回过程中的资产。

#### 限速：6 次/s

#### 限速规则：User ID

#### 权限：读取

#### HTTP 请求

`GET /api/v5/finance/staking-defi/eth/balance`

> 请求示例
    
    
    GET /api/v5/finance/staking-defi/eth/balance
    
    
    
    
    import okx.Finance.EthStaking as EthStaking
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    StackingAPI = EthStaking.EthStakingAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StackingAPI.eth_balance()
    print(result)
    

#### 请求参数

None

> 返回结果
    
    
    {
        "code": "0",
        "data": [
          {
            "amt": "0.63926191",
            "ccy": "BETH",
            "latestInterestAccrual": "0.00006549",
            "totalInterestAccrual": "0.01490596",
            "ts": "1699257600000"
          }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ccy | String | 币种名称，如 `BETH`  
amt | String | 币种数量  
latestInterestAccrual | String | 最近收益  
totalInterestAccrual | String | 历史总收益  
ts | String | 快照时间，值为时间戳，Unix时间戳为毫秒数格式，如 `1597026383085`  
  
### GET / 获取申购赎回记录 

#### 限速：6 次/s

#### 限速规则：User ID

#### 权限：读取

#### HTTP 请求

`GET /api/v5/finance/staking-defi/eth/purchase-redeem-history`

> 请求示例
    
    
    GET /api/v5/finance/staking-defi/eth/purchase-redeem-history
    
    
    
    
    import okx.Finance.EthStaking as EthStaking
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    StackingAPI = EthStaking.EthStakingAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StackingAPI.eth_purchase_redeem_history()
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
`cancelled`：已取消  
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
`cancelled`：已取消  
ordId | String | 订单ID  
requestTime | String | 发起 申购/赎回 请求的时间，值为时间戳，Unix时间戳为毫秒数格式，如 `1597026383085`  
completedTime | String | 赎回请求处理完成的时间，值为时间戳，Unix时间戳为毫秒数格式，如 `1597026383085`  
estCompletedTime | String | 预估完成赎回的时间，值为时间戳，Unix时间戳为毫秒数格式，如 `1597026383085`  
  
### GET / 获取历史收益率(公共) 

公共接口无须鉴权

#### 限速：6次/s

#### 限速规则：IP

#### HTTP 请求

`GET /api/v5/finance/staking-defi/eth/apy-history`

> 请求示例
    
    
    GET /api/v5/finance/staking-defi/eth/apy-history?days=2
    
    
    
    
    import okx.Finance.EthStaking as EthStaking
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    StackingAPI = EthStaking.EthStakingAPI(flag=flag)
    
    result = StackingAPI.eth_apy_history(days="7")
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
                "rate": "0.02690000",
                "ts": "1734195600000"
            },
            {
                "rate": "0.02840000",
                "ts": "1734109200000"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
rate | String | 年化收益率，如 `0.01`代表`1%`  
ts | String | 时间，值为时间戳，Unix时间戳为毫秒数格式，如 `1597026383085`