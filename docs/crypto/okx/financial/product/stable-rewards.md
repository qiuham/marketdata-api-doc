---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#financial-product-stable-rewards
anchor_id: financial-product-stable-rewards
api_type: API
updated_at: 2026-07-13 19:29:30.324153
---

# Stable Rewards

OKX Stable Rewards automatically distributes daily rewards to holders of eligible stablecoins (e.g. `USDG`) without any action required once enrolled.  
Subscribe from the funding account; rewards and redemptions settle to the trading account by default.  
  
### GET / Product info

Retrieve product-level information for the specified stablecoin, including all currencies eligible for subscription and redemption, applicable fee rates, amount limits, daily quotas, and current redemption availability.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

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
  
### POST / Quote

Request a quote before subscribing or redeeming. Only the assets in the funding account can be used. The returned `quoteId` must be submitted via `POST /trade` before `ttlMs` expires.

#### Rate Limit: 2 requests per second

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/finance/stable-rewards/quote`

> Request Example
    
    
    POST /api/v5/finance/stable-rewards/quote
    body
    {
        "ccy": "USDG",
        "settleCcy": "USDT",
        "action": "subscribe",
        "amt": "1000"
    }
    

#### Request Parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
ccy | String | Yes | Stablecoin to subscribe or redeem, e.g. `USDG`  
settleCcy | String | Yes | Settlement currency, e.g. `USDC`, `USDT`  
action | String | Yes | Action type  
`subscribe`  
`redeem`  
amt | String | Yes | Transaction amount  
For `subscribe`: denominated in `settleCcy`  
For `redeem`: denominated in `ccy`  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "quoteId": "1234567890",
                "quoteAmt": "998.88",
                "quoteCcy": "USDG",
                "exchRate": "0.99888110",
                "feeRate": "0.0003",
                "quoteTime": "1620282889345",
                "ttlMs": "10000"
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
quoteId | String | Quote ID. Submit this value via `POST /trade` before `ttlMs` expires to execute the transaction  
quoteAmt | String | Target amount denominated in `quoteCcy`  
quoteCcy | String | Currency of `quoteAmt`  
For `subscribe`: returns `ccy` (the stablecoin received)  
For `redeem`: returns `settleCcy` (the settlement currency received)  
exchRate | String | Exchange rate, 8 decimals  
For `subscribe`: units of `ccy` received per unit of `settleCcy`  
For `redeem`: units of `settleCcy` received per unit of `ccy`  
feeRate | String | Fee rate applied to this quote, e.g. `0.0003` represents `0.03%`  
quoteTime | String | Quotation generation time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
ttlMs | String | Quotation validity period in milliseconds, e.g. `10000` means the quote is valid for 10 seconds  
  
### POST / Trade

Execute a subscription or redemption using a valid `quoteId` obtained from `POST /quote`.  
Subscription: assets are deducted from the funding account; on success, the stablecoin is credited to the trading account by default.  
Redemption: the stablecoin is deducted from the funding account by default; the settlement currency is credited to the trading account by default.

#### Rate Limit: 2 requests per second

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/finance/stable-rewards/trade`

> Request Example
    
    
    POST /api/v5/finance/stable-rewards/trade
    body
    {
        "quoteId": "1234567890"
    }
    

#### Request Parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
quoteId | String | Yes | Quote ID returned by `POST /quote`. The quote must not have expired  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "quoteId": "1234567890",
                "ordId": "987654321"
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
quoteId | String | Quote ID  
ordId | String | Order ID  
  
### GET / Balance

Retrieve the real-time Stable Rewards balance across the account (trading account, funding account, and in-progress redemptions combined), along with lifetime earnings and the current earning state for each stablecoin.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

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

#### Permission: Read

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
  
### GET / Subscribe redeem history

Retrieve subscription and redemption records. Results are returned in reverse chronological order.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/finance/stable-rewards/subscribe-redeem-history`

> Request Example
    
    
    GET /api/v5/finance/stable-rewards/subscribe-redeem-history?ccy=USDG
    

#### Request Parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
ccy | String | Yes | Stablecoin, e.g. `USDG`  
type | String | No | Record type  
`subscribe`  
`redeem`  
Returns both types if not specified  
status | String | No | Order status  
`pending`  
`success`  
`failed`  
Returns all statuses if not specified  
after | String | No | Pagination of data to return records earlier than the requested `ordId`  
before | String | No | Pagination of data to return records newer than the requested `ordId`  
limit | String | No | Number of results per request. The default is `100`. The maximum is `100`  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "type": "subscribe",
                "status": "success",
                "ccy": "USDG",
                "settleCcy": "USDT",
                "ccyAmt": "998.88",
                "settleCcyAmt": "1000",
                "fee": "0.3",
                "quoteId": "1234567890",
                "ordId": "987654321",
                "ts": "1718035200000"
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
type | String | Record type  
`subscribe`  
`redeem`  
status | String | Order status  
`pending`  
`success`  
`failed`  
ccy | String | Stablecoin subscribed or redeemed, e.g. `USDG`  
settleCcy | String | Settlement currency, e.g. `USDC`, `USDT`  
ccyAmt | String | Amount denominated in `ccy`  
settleCcyAmt | String | Amount denominated in `settleCcy`  
fee | String | Fee charged, denominated in `settleCcy`  
quoteId | String | Quote ID  
ordId | String | Order ID  
ts | String | Order creation time, Unix timestamp format in milliseconds, e.g. `1597026383085`

---

# Stable Rewards

OKX Stable Rewards 自动为持有合格稳定币（如 `USDG`）的用户每日发放奖励，启用后无需任何操作即可持续赚取收益。  
订阅时从资金账户扣款；收益及赎回默认结算至交易账户。  
  
### GET / 获取产品信息 

获取指定稳定币的产品信息，包括支持订阅/赎回的结算币种、适用手续费率、申购/赎回金额限制、每日配额以及当前赎回可用状态。

#### 限速：5次/2s

#### 限速规则：User ID

#### 权限：读取

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
  
### POST / 询价 

在订阅或赎回前发起询价。仅资金账户中的资产可用于订阅。返回的 `quoteId` 须在 `ttlMs` 过期前通过 `POST /trade` 接口提交以完成交易。

#### 限速：2次/s

#### 限速规则：User ID

#### 权限：交易

#### HTTP 请求

`POST /api/v5/finance/stable-rewards/quote`

> 请求示例
    
    
    POST /api/v5/finance/stable-rewards/quote
    body
    {
        "ccy": "USDG",
        "settleCcy": "USDT",
        "action": "subscribe",
        "amt": "1000"
    }
    

#### 请求参数

**参数名** | **类型** | **是否必须** | **描述**  
---|---|---|---  
ccy | String | 是 | 订阅或赎回的稳定币，如 `USDG`  
settleCcy | String | 是 | 结算币种，如 `USDC`、`USDT`  
action | String | 是 | 操作类型  
`subscribe`：订阅  
`redeem`：赎回  
amt | String | 是 | 交易数量  
`subscribe` 时以 `settleCcy` 计价  
`redeem` 时以 `ccy` 计价  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "quoteId": "1234567890",
                "quoteAmt": "998.88",
                "quoteCcy": "USDG",
                "exchRate": "0.99888110",
                "feeRate": "0.0003",
                "quoteTime": "1620282889345",
                "ttlMs": "10000"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
quoteId | String | 报价 ID。须在 `ttlMs` 过期前通过 `POST /trade` 提交以完成交易  
quoteAmt | String | 报价数量，以 `quoteCcy` 计价  
quoteCcy | String | `quoteAmt` 对应的币种  
`subscribe` 时返回 `ccy`（用户获得的稳定币）  
`redeem` 时返回 `settleCcy`（用户获得的结算币种）  
exchRate | String | 兑换汇率，精度为 8 位小数  
`subscribe` 时：1 单位 `settleCcy` 可兑换的 `ccy` 数量  
`redeem` 时：1 单位 `ccy` 可兑换的 `settleCcy` 数量  
feeRate | String | 本次报价的手续费率，如 `0.0003` 代表 `0.03%`  
quoteTime | String | 报价生成时间，Unix 时间戳，单位为毫秒，如 `1597026383085`  
ttlMs | String | 报价有效期，单位为毫秒，如 `10000` 代表报价 10 秒内有效  
  
### POST / 下单 

使用 `POST /quote` 返回的有效 `quoteId` 执行订阅或赎回。  
订阅：从资金账户扣款，成功后稳定币默认入账至交易账户。  
赎回：默认从资金账户扣除稳定币，结算币种默认入账至交易账户。

#### 限速：2次/s

#### 限速规则：User ID

#### 权限：交易

#### HTTP 请求

`POST /api/v5/finance/stable-rewards/trade`

> 请求示例
    
    
    POST /api/v5/finance/stable-rewards/trade
    body
    {
        "quoteId": "1234567890"
    }
    

#### 请求参数

**参数名** | **类型** | **是否必须** | **描述**  
---|---|---|---  
quoteId | String | 是 | 由 `POST /quote` 返回的报价 ID，须在报价未过期前提交  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "quoteId": "1234567890",
                "ordId": "987654321"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
quoteId | String | 报价 ID  
ordId | String | 订单 ID  
  
### GET / 获取余额 

查询 Stable Rewards 的实时余额，余额涵盖交易账户、资金账户以及正在赎回中的资产合计，同时返回累计收益与当前收益状态。

#### 限速：5次/2s

#### 限速规则：User ID

#### 权限：读取

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

#### 权限：读取

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
  
### GET / 获取订阅赎回历史 

查询订阅与赎回记录，按时间倒序返回。

#### 限速：5次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP 请求

`GET /api/v5/finance/stable-rewards/subscribe-redeem-history`

> 请求示例
    
    
    GET /api/v5/finance/stable-rewards/subscribe-redeem-history?ccy=USDG
    

#### 请求参数

**参数名** | **类型** | **是否必须** | **描述**  
---|---|---|---  
ccy | String | 是 | 稳定币，如 `USDG`  
type | String | 否 | 记录类型  
`subscribe`：订阅  
`redeem`：赎回  
不传则返回全部类型  
status | String | 否 | 订单状态  
`pending`：处理中  
`success`：成功  
`failed`：失败  
不传则返回全部状态  
after | String | 否 | 请求此 `ordId` 之前（更早时间）的分页内容  
before | String | 否 | 请求此 `ordId` 之后（更新时间）的分页内容  
limit | String | 否 | 分页返回的结果数量。默认 `100`，最大 `100`  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "type": "subscribe",
                "status": "success",
                "ccy": "USDG",
                "settleCcy": "USDT",
                "ccyAmt": "998.88",
                "settleCcyAmt": "1000",
                "fee": "0.3",
                "quoteId": "1234567890",
                "ordId": "987654321",
                "ts": "1718035200000"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
type | String | 记录类型  
`subscribe`：订阅  
`redeem`：赎回  
status | String | 订单状态  
`pending`：处理中  
`success`：成功  
`failed`：失败  
ccy | String | 订阅/赎回的稳定币，如 `USDG`  
settleCcy | String | 结算币种，如 `USDC`、`USDT`  
ccyAmt | String | 以 `ccy` 计价的数量  
settleCcyAmt | String | 以 `settleCcy` 计价的数量  
fee | String | 订阅/赎回手续费，以 `settleCcy` 计价  
quoteId | String | 报价 ID  
ordId | String | 订单 ID  
ts | String | 订单创建时间，Unix 时间戳，单位为毫秒，如 `1597026383085`