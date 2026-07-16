---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#financial-product-stable-rewards
anchor_id: financial-product-stable-rewards
api_type: API
updated_at: 2026-07-16 19:21:49.295233
---

# Stable Rewards

OKX Stable Rewards automatically distributes daily rewards to holders of eligible stablecoins (e.g. `USDG`) without any action required once enrolled.  
Subscribe from the funding account; rewards and redemptions settle to the trading account by default.  
  
> **Deprecation Notice**
> 
> `POST /api/v5/finance/stable-rewards/quote`, `POST /api/v5/finance/stable-rewards/trade`, and `GET /api/v5/finance/stable-rewards/subscribe-redeem-history` have been decommissioned. Please use the standard [order book trading APIs](/docs-v5/en/#order-book-trading) to trade USDG and other stablecoins.

### GET / Product info

Retrieve product-level information for the specified stablecoin, including all currencies eligible for subscription and redemption, applicable fee rates, amount limits, daily quotas, and current redemption availability.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/finance/stable-rewards/product-info`

> Request Example
    
    
    GET /api/v5/finance/stable-rewards/product-info?ccy=USDG
    

#### Request Parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
ccy | String | Yes | Stablecoin, e.g. `USDG`  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "details": [
                    {
                        "ccy": "USDG",
                        "settleCcy": "USDC",
                        "subFeeRate": "0.0003",
                        "redemptFeeRate": "0",
                        "minSubAmt": "1",
                        "minRedeemAmt": "0.0000001",
                        "remainingSubQuota": "1000000",
                        "remainingRedemptQuota": "500000",
                        "canRedeem": true
                    },
                    {
                        "ccy": "USDG",
                        "settleCcy": "USDT",
                        "subFeeRate": "0.0003",
                        "redemptFeeRate": "",
                        "minSubAmt": "1",
                        "minRedeemAmt": "",
                        "remainingSubQuota": "1000000",
                        "remainingRedemptQuota": "",
                        "canRedeem": false
                    }
                ],
                "ts": "1718035200000"
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
details | Array of objects | List of supported settlement currencies and their subscription/redemption details  
> ccy | String | Subscribable stablecoin, e.g. `USDG`  
> settleCcy | String | Settlement currency that can be used to subscribe to `ccy`, e.g. `USDC`, `USDT`  
> subFeeRate | String | Subscription fee rate, e.g. `0.01` represents `1%`  
> redemptFeeRate | String | Redemption fee rate, e.g. `0.01` represents `1%`  
Returns `""` if redemption to the given `settleCcy` is not available  
> minSubAmt | String | Minimum subscription amount, denominated in `settleCcy`  
> minRedeemAmt | String | Minimum redemption amount, denominated in `ccy`  
Returns `""` if redemption to the given `settleCcy` is not available  
> remainingSubQuota | String | Remaining daily subscription quota per master user ID  
Returns `-1` if unlimited  
> remainingRedemptQuota | String | Remaining daily redemption quota per master user ID  
Returns `-1` if unlimited  
Returns `""` if redemption to the given `settleCcy` is not available  
> canRedeem | Boolean | Whether redemption to the given `settleCcy` is currently available  
`true`: Available  
`false`: Unavailable  
ts | String | Data query time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
### GET / Balance

Retrieve the real-time Stable Rewards balance across the account (trading account, funding account, and in-progress redemptions combined), along with lifetime earnings and the current earning state for each stablecoin.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/finance/stable-rewards/balance`

> Request Example
    
    
    GET /api/v5/finance/stable-rewards/balance?ccy=USDG
    

#### Request Parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
ccy | String | No | Stablecoin, e.g. `USDG`  
Returns all supported stablecoins if not specified  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "details": [
                    {
                        "ccy": "USDG",
                        "amt": "100",
                        "totalEarnAccrual": "0.0003",
                        "state": "earning"
                    }
                ],
                "ts": "1718035200000"
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
details | Array of objects | Real-time balance details per stablecoin  
> ccy | String | Stablecoin, e.g. `USDG`  
> amt | String | Currency amount held across the entire account  
> totalEarnAccrual | String | Total interest accrued over the lifetime of the holding  
> state | String | Earning state  
`earning`: The balance is currently accruing rewards  
`pending`: The balance is not currently accruing (e.g. auto-earn is off, or the balance is below the activation threshold)  
ts | String | Query data time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
### GET / APY history

Retrieve the historical daily APY of the specified stablecoin. The returned rate reflects the user's current VIP level.

#### Rate Limit: 6 requests per second

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/finance/stable-rewards/apy-history`

> Request Example
    
    
    GET /api/v5/finance/stable-rewards/apy-history?ccy=USDG
    

#### Request Parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
ccy | String | Yes | Stablecoin, e.g. `USDG`  
days | String | No | Number of historical days to return. The default is `100`. The maximum is `100`  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "rate": "0.004",
                "ts": "1718035200000"
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
rate | String | Daily APY for the user's current VIP level, e.g. `0.041` represents `4.1%`  
ts | String | Snapshot time (UTC+0), Unix timestamp format in milliseconds, e.g. `1597026383085`

---

# Stable Rewards

OKX Stable Rewards 自动为持有合格稳定币（如 `USDG`）的用户每日发放奖励，启用后无需任何操作即可持续赚取收益。  
订阅时从资金账户扣款；收益及赎回默认结算至交易账户。  
  
> **下线说明**
> 
> `POST /api/v5/finance/stable-rewards/quote`、`POST /api/v5/finance/stable-rewards/trade` 及 `GET /api/v5/finance/stable-rewards/subscribe-redeem-history` 接口已停用。如需交易 USDG 等稳定币，请使用标准[订单簿交易 API](/docs-v5/zh/#order-book-trading)。

### GET / 获取产品信息 

获取指定稳定币的产品信息，包括支持订阅/赎回的结算币种、适用手续费率、申购/赎回金额限制、每日配额以及当前赎回可用状态。

#### 限速：5次/2s

#### 限速规则：User ID

#### HTTP 请求

`GET /api/v5/finance/stable-rewards/product-info`

> 请求示例
    
    
    GET /api/v5/finance/stable-rewards/product-info?ccy=USDG
    

#### 请求参数

**参数名** | **类型** | **是否必须** | **描述**  
---|---|---|---  
ccy | String | 是 | 稳定币，如 `USDG`  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "details": [
                    {
                        "ccy": "USDG",
                        "settleCcy": "USDC",
                        "subFeeRate": "0.0003",
                        "redemptFeeRate": "0",
                        "minSubAmt": "1",
                        "minRedeemAmt": "0.0000001",
                        "remainingSubQuota": "1000000",
                        "remainingRedemptQuota": "500000",
                        "canRedeem": true
                    },
                    {
                        "ccy": "USDG",
                        "settleCcy": "USDT",
                        "subFeeRate": "0.0003",
                        "redemptFeeRate": "",
                        "minSubAmt": "1",
                        "minRedeemAmt": "",
                        "remainingSubQuota": "1000000",
                        "remainingRedemptQuota": "",
                        "canRedeem": false
                    }
                ],
                "ts": "1718035200000"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
details | Array of objects | 当前稳定币支持的结算币种及其订阅/赎回信息列表  
> ccy | String | 可订阅的稳定币，如 `USDG`  
> settleCcy | String | 可用于订阅 `ccy` 的结算币种，如 `USDC`、`USDT`  
> subFeeRate | String | 订阅手续费率，如 `0.01` 代表 `1%`  
> redemptFeeRate | String | 赎回手续费率，如 `0.01` 代表 `1%`  
当前 `settleCcy` 不支持赎回时返回 `""`  
> minSubAmt | String | 最小订阅数量，以 `settleCcy` 计价  
> minRedeemAmt | String | 最小赎回数量，以 `ccy` 计价  
当前 `settleCcy` 不支持赎回时返回 `""`  
> remainingSubQuota | String | 每日剩余订阅额度，按母账户 ID 统计  
`-1` 代表无上限  
> remainingRedemptQuota | String | 每日剩余赎回额度，按母账户 ID 统计  
`-1` 代表无上限  
当前 `settleCcy` 不支持赎回时返回 `""`  
> canRedeem | Boolean | 当前 `settleCcy` 是否支持赎回  
`true`：可赎回  
`false`：不可赎回  
ts | String | 数据查询时间，Unix 时间戳，单位为毫秒，如 `1597026383085`  
  
### GET / 获取余额 

查询 Stable Rewards 的实时余额，余额涵盖交易账户、资金账户以及正在赎回中的资产合计，同时返回累计收益与当前收益状态。

#### 限速：5次/2s

#### 限速规则：User ID

#### HTTP 请求

`GET /api/v5/finance/stable-rewards/balance`

> 请求示例
    
    
    GET /api/v5/finance/stable-rewards/balance?ccy=USDG
    

#### 请求参数

**参数名** | **类型** | **是否必须** | **描述**  
---|---|---|---  
ccy | String | 否 | 稳定币，如 `USDG`  
不传则返回全部支持的稳定币  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "details": [
                    {
                        "ccy": "USDG",
                        "amt": "100",
                        "totalEarnAccrual": "0.0003",
                        "state": "earning"
                    }
                ],
                "ts": "1718035200000"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
details | Array of objects | 按稳定币返回的实时余额明细  
> ccy | String | 稳定币，如 `USDG`  
> amt | String | 整个账户范围内的持有数量  
> totalEarnAccrual | String | 持有期间的累计收益  
> state | String | 收益状态  
`earning`：正在产生收益  
`pending`：未在产生收益（如自动赚币已关闭，或余额低于起息门槛）  
ts | String | 数据查询时间，Unix 时间戳，单位为毫秒，如 `1597026383085`  
  
### GET / 获取历史收益率 

查询指定稳定币的历史每日年化收益率。返回值为用户当前 VIP 等级对应的收益率。

#### 限速：6次/s

#### 限速规则：IP

#### HTTP 请求

`GET /api/v5/finance/stable-rewards/apy-history`

> 请求示例
    
    
    GET /api/v5/finance/stable-rewards/apy-history?ccy=USDG
    

#### 请求参数

**参数名** | **类型** | **是否必须** | **描述**  
---|---|---|---  
ccy | String | 是 | 稳定币，如 `USDG`  
days | String | 否 | 查询最近多少天的历史数据。默认 `100`，最大 `100`  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "rate": "0.004",
                "ts": "1718035200000"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
rate | String | 用户当前 VIP 等级对应的日度年化收益率，如 `0.041` 代表 `4.1%`  
ts | String | 数据快照时间（UTC+0），Unix 时间戳，单位为毫秒，如 `1597026383085`