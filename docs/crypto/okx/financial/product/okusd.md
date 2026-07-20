---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#financial-product-okusd
anchor_id: financial-product-okusd
api_type: API
updated_at: 2026-07-20 19:37:36.711768
---

# OKUSD

OKUSD is OKX's stablecoin receipt issued at a 1:1 rate against USDT. Holders earn daily APR with no action required, and OKUSD can be used as trading margin to improve capital efficiency.  
Subscription and redemption operate on the funding account. Use the `/limits` endpoint to check your remaining daily quota before subscribing or redeeming.  
  
### GET / OKUSD limits

Retrieve your remaining daily OKUSD subscription quota and both fast and standard redemption quotas. All limits are calculated at the master-account level and shared across sub-accounts.

#### Rate Limit: 2 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/finance/okusd/limits`

> Request Example
    
    
    GET /api/v5/finance/okusd/limits
    

#### Request Parameters

None

> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "subLimit": {
                    "maxSubAmt": "45000000",
                    "personalDailyLimit": "5000000",
                    "personalUsedAmt": "500000",
                    "platformDailyLimit": "50000000",
                    "platformUsedAmt": "5000000"
                },
                "fastRedeemLimit": {
                    "personalDailyLimit": "10000",
                    "personalUsedAmt": "0",
                    "platformDailyLimit": "5000000",
                    "platformUsedAmt": "1000000",
                    "feeRate": "0.001"
                },
                "stdRedeemLimit": {
                    "personalDailyLimit": "1000000",
                    "personalUsedAmt": "0",
                    "platformDailyLimit": "40000000",
                    "platformUsedAmt": "0",
                    "feeRate": "0.00025"
                },
                "ts": "1718500000000"
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
subLimit | Object | Subscription limit information  
> maxSubAmt | String | Maximum subscribable amount for today (USDT). Equal to `min(personalDailyLimit - personalUsedAmt, platformDailyLimit - platformUsedAmt)`. Minimum value is `"0"`  
> personalDailyLimit | String | Your daily subscription limit based on your VIP tier (USDT)  
> personalUsedAmt | String | Amount you have already subscribed today (USDT)  
> platformDailyLimit | String | Platform-wide daily subscription cap (USDT)  
> platformUsedAmt | String | Total amount subscribed across the platform today (USDT)  
fastRedeemLimit | Object | Fast redemption limit information (real-time settlement)  
> personalDailyLimit | String | Your daily fast redemption limit based on your VIP tier (OKUSD)  
> personalUsedAmt | String | Fast redemption amount you have already used today (OKUSD)  
> platformDailyLimit | String | Platform-wide daily fast redemption cap (OKUSD)  
> platformUsedAmt | String | Total fast redemption amount used across the platform today (OKUSD)  
> feeRate | String | Fee rate for fast redemption  
stdRedeemLimit | Object | Standard redemption limit information  
> personalDailyLimit | String | Your daily standard redemption limit based on your VIP tier (OKUSD)  
> personalUsedAmt | String | Standard redemption amount you have already used today (OKUSD)  
> platformDailyLimit | String | Platform-wide daily standard redemption cap (OKUSD)  
> platformUsedAmt | String | Total standard redemption amount used across the platform today (OKUSD)  
> feeRate | String | Fee rate for standard redemption  
ts | String | Server timestamp, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
### POST / Subscribe OKUSD

Subscribe USDT to receive OKUSD at a 1:1 rate with no subscription fee. OKUSD is credited immediately to your funding account. Pass a unique `clOrdId` per request; resubmitting the same `clOrdId` returns the original order without re-executing the subscription.

#### Rate Limit: 1 request per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/finance/okusd/subscribe`

> Request Example
    
    
    POST /api/v5/finance/okusd/subscribe
    body
    {
        "amt": "1000.00000000",
        "clOrdId": "my-sub-001"
    }
    

#### Request Parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
amt | String | Yes | Amount of USDT to subscribe. Minimum: `1`. Maximum 8 decimal places. Scientific notation is not supported  
clOrdId | String | Yes | Client-defined order ID. Maximum 32 characters (letters, digits, `-`, `_`). Must be unique per UID. Used for order tracking and idempotency  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "ordId": "680012345678901234",
                "clOrdId": "my-sub-001",
                "ccy": "USDT",
                "amt": "1000.00000000",
                "okusdAmt": "1000.00000000",
                "state": "success",
                "ts": "1718500000000"
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
ordId | String | System-generated order ID  
clOrdId | String | Client-defined order ID (echoed back)  
ccy | String | Subscription currency. Always `"USDT"`  
amt | String | Actual USDT amount subscribed  
okusdAmt | String | OKUSD amount credited to your funding account (equal to `amt` at 1:1 rate; no subscription fee)  
state | String | Order status: `"success"` / `"pending"` / `"failed"`  
ts | String | Order creation time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
### POST / Redeem OKUSD

Redeem OKUSD back to USDT. Choose between fast redemption (real-time settlement) or standard redemption (D+5 or D+6 calendar days, depending on submission time). Fee rates vary by redemption type — call `GET /limits` to get current rates. All fee amounts are truncated (floor) to 8 decimal places. Pass a unique `clOrdId` per request; resubmitting the same `clOrdId` returns the original order without re-executing the redemption.

#### Rate Limit: 1 request per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/finance/okusd/redeem`

> Request Example (Fast Redemption)
    
    
    POST /api/v5/finance/okusd/redeem
    body
    {
        "amt": "1000.00000000",
        "redeemType": "1",
        "clOrdId": "my-redeem-001"
    }
    

#### Request Parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
amt | String | Yes | Amount of OKUSD to redeem. Minimum: `1`. Maximum 8 decimal places. Scientific notation is not supported  
redeemType | String | Yes | Redemption type. `"1"`: Fast redemption (real-time settlement); `"2"`: Standard redemption (D+5 calendar days if submitted before UTC+8 16:00; D+6 calendar days if submitted at or after UTC+8 16:00). See the `feeRate` fields returned by `GET /limits` for current fee rates  
clOrdId | String | Yes | Client-defined order ID. Maximum 32 characters (letters, digits, `-`, `_`). Must be unique per UID. Used for order tracking and idempotency  
  
> Response Example (Fast Redemption)
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "ordId": "680012345678905678",
                "clOrdId": "my-redeem-001",
                "ccy": "OKUSD",
                "amt": "1000.00000000",
                "fee": "1.00000000",
                "usdtAmt": "999.00000000",
                "redeemType": "1",
                "state": "success",
                "estSettlementTime": "1718500010000",
                "ts": "1718500000000"
            }
        ]
    }
    

> Response Example (Standard Redemption)
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "ordId": "680012345678906789",
                "clOrdId": "my-redeem-002",
                "ccy": "OKUSD",
                "amt": "50000.00000000",
                "fee": "12.50000000",
                "usdtAmt": "49987.50000000",
                "redeemType": "2",
                "state": "processing",
                "estSettlementTime": "1718932800000",
                "ts": "1718500000000"
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
ordId | String | System-generated order ID  
clOrdId | String | Client-defined order ID (echoed back)  
ccy | String | Redemption currency. Always `"OKUSD"`  
amt | String | OKUSD amount redeemed  
fee | String | Fee charged in USDT, truncated (floor) to 8 decimal places  
usdtAmt | String | Net USDT amount credited to your funding account (`amt - fee`, truncated to 8 decimal places)  
redeemType | String | Redemption type: `"1"` (fast) or `"2"` (standard)  
state | String | Order status: `"processing"` / `"success"` / `"failed"` / `"cancelled"`  
estSettlementTime | String | Estimated settlement time, Unix timestamp format in milliseconds. Fast redemption: current time. Standard redemption: D+5 calendar days if submitted before UTC+8 16:00; D+6 calendar days if submitted at or after UTC+8 16:00  
ts | String | Order creation time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
### GET / Get OKUSD Account

Retrieve your current OKUSD balance and lifetime accrued yield. All balances are aggregated at the master-account level and shared across sub-accounts.

#### Rate Limit: 2 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/finance/okusd/account`

> Request Example
    
    
    GET /api/v5/finance/okusd/account
    

#### Request Parameters

None

> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "ccy": "OKUSD",
                "amt": "10000.00000000",
                "totalEarnAccrual": "123.45678900",
                "ts": "1718500000000"
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
ccy | String | Currency. Always `"OKUSD"`  
amt | String | Current OKUSD balance  
totalEarnAccrual | String | Cumulative yield accrued over the holding period, denominated in USDT  
ts | String | Server timestamp, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
### GET / Get Subscription History

Retrieve your OKUSD subscription order history. Results are returned in descending order by timestamp (newest first) and support time-range filtering.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/finance/okusd/subscribe/history`

> Request Example
    
    
    GET /api/v5/finance/okusd/subscribe/history?limit=2
    

#### Request Parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
limit | String | No | Number of results per page. Default `"100"`. Maximum `"100"`  
begin | String | No | Start time filter (order creation time `ts`, Unix ms, inclusive)  
end | String | No | End time filter (order creation time `ts`, Unix ms, inclusive)  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "ordId": "680012345678901234",
                "clOrdId": "my-sub-001",
                "ccy": "USDT",
                "amt": "1000.00000000",
                "settleCcy": "OKUSD",
                "settleCcyAmt": "1000.00000000",
                "status": "success",
                "ts": "1718500000000"
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
ordId | String | System-generated order ID  
clOrdId | String | Client-defined order ID (echoed back; empty string if not provided)  
ccy | String | Subscription currency. Always `"USDT"`  
amt | String | USDT amount subscribed  
settleCcy | String | Settlement currency. Always `"OKUSD"`  
settleCcyAmt | String | OKUSD amount credited (equal to `amt` at 1:1 rate)  
status | String | Terminal order status: `"success"` / `"failed"`  
ts | String | Order creation time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
### GET / Get Redemption History

Retrieve your OKUSD redemption order history. Results are returned in descending order by timestamp (newest first) and support time-range filtering and redemption-type filtering.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/finance/okusd/redeem/history`

> Request Example
    
    
    GET /api/v5/finance/okusd/redeem/history?type=fast
    

#### Request Parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
limit | String | No | Number of results per page. Default `"100"`. Maximum `"100"`  
begin | String | No | Start time filter (order creation time `ts`, Unix ms, inclusive)  
end | String | No | End time filter (order creation time `ts`, Unix ms, inclusive)  
type | String | No | Redemption type filter: `"fast"` for fast redemption only; `"standard"` for standard redemption only. Defaults to standard redemption if not specified  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "ordId": "680012345678905678",
                "clOrdId": "my-rdm-fast-001",
                "ccy": "OKUSD",
                "amt": "1000.00000000",
                "fee": "1.00000000",
                "settleCcy": "USDT",
                "settleCcyAmt": "999.00000000",
                "type": "fast",
                "status": "success",
                "estSettlementTime": "1718500010000",
                "ts": "1718500000000"
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
ordId | String | System-generated order ID  
clOrdId | String | Client-defined order ID (echoed back; empty string if not provided)  
ccy | String | Redemption currency. Always `"OKUSD"`  
amt | String | OKUSD amount redeemed  
fee | String | Fee charged in USDT, truncated (floor) to 8 decimal places  
settleCcy | String | Settlement currency. Always `"USDT"`  
settleCcyAmt | String | Net USDT amount credited (`amt - fee`, truncated to 8 decimal places)  
type | String | Redemption type: `"fast"` (real-time settlement) or `"standard"` (D+5/D+6 calendar days)  
status | String | Order status: `"pending"` / `"success"` / `"failed"` / `"canceled"`  
estSettlementTime | String | Estimated settlement time, Unix timestamp format in milliseconds. Empty string for settled fast redemption orders  
ts | String | Order creation time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
### GET / Get Rewards History

Retrieve your daily OKUSD yield distribution history. Results are returned in descending order by timestamp (newest first).

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/finance/okusd/rewards/history`

> Request Example
    
    
    GET /api/v5/finance/okusd/rewards/history?limit=7
    

#### Request Parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
limit | String | No | Number of results per page. Default `"30"`. Maximum `"100"`  
begin | String | No | Start time filter (`ts`, Unix ms, inclusive). Maximum query span is 6 months  
end | String | No | End time filter (`ts`, Unix ms, inclusive). Defaults to the current time if not provided  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "ccy": "USDT",
                "earnAmt": "1.14246575",
                "amt": "10000.00000000",
                "apr": "0.0418",
                "ts": "1718500000000"
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
ccy | String | Yield currency. Always `"USDT"`  
earnAmt | String | USDT yield distributed in this event  
amt | String | Your USDT principal balance at the time of distribution  
apr | String | APR applied for this distribution, e.g. `"0.0418"` represents 4.18%  
ts | String | Distribution timestamp, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
### GET / Get APR History

Retrieve the historical APR snapshots for OKUSD. Results are returned in descending order by timestamp (newest first). This endpoint requires API Key authentication even though the data is product-level and not user-specific.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/finance/okusd/rate/history`

> Request Example
    
    
    GET /api/v5/finance/okusd/rate/history?limit=10
    

#### Request Parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
limit | String | No | Number of results per page. Default `"30"`. Maximum `"100"`  
begin | String | No | Start time filter (`ts`, Unix ms, inclusive). Maximum query span is 6 months  
end | String | No | End time filter (`ts`, Unix ms, inclusive). Defaults to the current time if not provided  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            { "apr": "0.0418", "ts": "1718500000000" },
            { "apr": "0.0395", "ts": "1718413600000" }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
apr | String | OKUSD APR at this snapshot, e.g. `"0.0418"` represents 4.18%  
ts | String | Snapshot timestamp, Unix timestamp format in milliseconds, e.g. `1597026383085`

---

# OKUSD

OKUSD 是 OKX 以 1:1 汇率发行的稳定币凭证，用户以 USDT 申购后持有即可享受每日收益，同时可用作交易账户保证金以提升资本效率。  
申购与赎回均在资金账户中操作。申购或赎回前可调用 `/limits` 接口查询当日剩余限额。  
  
### GET / 查询限额 

查询您当日 OKUSD 申购剩余限额及即时/标准赎回剩余限额。所有限额均以母账户维度计算，子账户共享。

#### 限速：2次/2s

#### 限速规则：User ID

#### HTTP 请求

`GET /api/v5/finance/okusd/limits`

> 请求示例
    
    
    GET /api/v5/finance/okusd/limits
    

#### 请求参数

无

> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "subLimit": {
                    "maxSubAmt": "45000000",
                    "personalDailyLimit": "5000000",
                    "personalUsedAmt": "500000",
                    "platformDailyLimit": "50000000",
                    "platformUsedAmt": "5000000"
                },
                "fastRedeemLimit": {
                    "personalDailyLimit": "10000",
                    "personalUsedAmt": "0",
                    "platformDailyLimit": "5000000",
                    "platformUsedAmt": "1000000",
                    "feeRate": "0.001"
                },
                "stdRedeemLimit": {
                    "personalDailyLimit": "1000000",
                    "personalUsedAmt": "0",
                    "platformDailyLimit": "40000000",
                    "platformUsedAmt": "0",
                    "feeRate": "0.00025"
                },
                "ts": "1718500000000"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
subLimit | Object | 申购限额信息  
> maxSubAmt | String | 当日最大可申购数量（USDT），= min(personalDailyLimit - personalUsedAmt, platformDailyLimit - platformUsedAmt)，最小值为 `"0"`  
> personalDailyLimit | String | 根据您的 VIP 等级对应的每日申购上限（USDT）  
> personalUsedAmt | String | 您当日已申购金额（USDT）  
> platformDailyLimit | String | 平台每日申购总上限（USDT）  
> platformUsedAmt | String | 平台当日已申购总金额（USDT）  
fastRedeemLimit | Object | 即时赎回限额信息（实时到账）  
> personalDailyLimit | String | 根据您的 VIP 等级对应的每日即时赎回上限（OKUSD）  
> personalUsedAmt | String | 您当日已使用的即时赎回额度（OKUSD）  
> platformDailyLimit | String | 平台每日即时赎回总上限（OKUSD）  
> platformUsedAmt | String | 平台当日已使用的即时赎回额度（OKUSD）  
> feeRate | String | 即时赎回手续费率  
stdRedeemLimit | Object | 标准赎回限额信息  
> personalDailyLimit | String | 根据您的 VIP 等级对应的每日标准赎回上限（OKUSD）  
> personalUsedAmt | String | 您当日已使用的标准赎回额度（OKUSD）  
> platformDailyLimit | String | 平台每日标准赎回总上限（OKUSD）  
> platformUsedAmt | String | 平台当日已使用的标准赎回额度（OKUSD）  
> feeRate | String | 标准赎回手续费率  
ts | String | 服务器时间戳，Unix 时间戳，单位为毫秒，如 `1597026383085`  
  
### POST / 申购 OKUSD 

以 1:1 汇率将 USDT 申购为 OKUSD，无申购手续费，OKUSD 即时到账至资金账户。每次请求需传入唯一的 `clOrdId`；重复提交相同 `clOrdId` 将直接返回原始订单，不重复执行申购。

#### 限速：1次/2s

#### 限速规则：User ID

#### HTTP 请求

`POST /api/v5/finance/okusd/subscribe`

> 请求示例
    
    
    POST /api/v5/finance/okusd/subscribe
    body
    {
        "amt": "1000.00000000",
        "clOrdId": "my-sub-001"
    }
    

#### 请求参数

**参数名** | **类型** | **是否必须** | **描述**  
---|---|---|---  
amt | String | 是 | 申购 USDT 数量。最小值：`1`。最多 8 位小数。不支持科学计数法  
clOrdId | String | 是 | 客户自定义订单 ID，最多 32 字符（字母、数字、`-`、`_`）。同一 UID 下不可重复，用于订单追踪与幂等标识  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "ordId": "680012345678901234",
                "clOrdId": "my-sub-001",
                "ccy": "USDT",
                "amt": "1000.00000000",
                "okusdAmt": "1000.00000000",
                "state": "success",
                "ts": "1718500000000"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
ordId | String | 系统订单 ID  
clOrdId | String | 客户自定义订单 ID（原样返回）  
ccy | String | 申购货币，固定为 `"USDT"`  
amt | String | 实际申购 USDT 数量  
okusdAmt | String | 到账 OKUSD 数量（= `amt`，汇率 1:1，无申购手续费），到账至资金账户  
state | String | 订单状态：`"success"` / `"pending"` / `"failed"`  
ts | String | 订单创建时间，Unix 时间戳，单位为毫秒，如 `1597026383085`  
  
### POST / 赎回 OKUSD 

将 OKUSD 赎回为 USDT。支持即时赎回（实时到账）和标准赎回（D+5 或 D+6 自然日，取决于提交时间）。各类型手续费率请调用 `GET /limits` 查询。所有手续费均向下截断（floor）至 8 位小数。每次请求需传入唯一的 `clOrdId`；重复提交相同 `clOrdId` 将直接返回原始订单，不重复执行赎回。

#### 限速：1次/2s

#### 限速规则：User ID

#### HTTP 请求

`POST /api/v5/finance/okusd/redeem`

> 请求示例（即时赎回）
    
    
    POST /api/v5/finance/okusd/redeem
    body
    {
        "amt": "1000.00000000",
        "redeemType": "1",
        "clOrdId": "my-redeem-001"
    }
    

#### 请求参数

**参数名** | **类型** | **是否必须** | **描述**  
---|---|---|---  
amt | String | 是 | 赎回 OKUSD 数量。最小值：`1`。最多 8 位小数。不支持科学计数法  
redeemType | String | 是 | 赎回类型。`"1"`：即时赎回（实时到账）；`"2"`：标准赎回（UTC+8 16:00 前提交加 5 自然日，16:00 后（含）提交加 6 自然日）。各类型手续费率请参考 `/limits` 接口返回的 `feeRate` 字段  
clOrdId | String | 是 | 客户自定义订单 ID，最多 32 字符（字母、数字、`-`、`_`）。同一 UID 下不可重复，用于订单追踪与幂等标识  
  
> 返回结果（即时赎回）
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "ordId": "680012345678905678",
                "clOrdId": "my-redeem-001",
                "ccy": "OKUSD",
                "amt": "1000.00000000",
                "fee": "1.00000000",
                "usdtAmt": "999.00000000",
                "redeemType": "1",
                "state": "success",
                "estSettlementTime": "1718500010000",
                "ts": "1718500000000"
            }
        ]
    }
    

> 返回结果（标准赎回）
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "ordId": "680012345678906789",
                "clOrdId": "my-redeem-002",
                "ccy": "OKUSD",
                "amt": "50000.00000000",
                "fee": "12.50000000",
                "usdtAmt": "49987.50000000",
                "redeemType": "2",
                "state": "processing",
                "estSettlementTime": "1718932800000",
                "ts": "1718500000000"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
ordId | String | 系统订单 ID  
clOrdId | String | 客户自定义订单 ID（原样返回）  
ccy | String | 赎回货币，固定为 `"OKUSD"`  
amt | String | 赎回 OKUSD 数量  
fee | String | 实收手续费（USDT），向下截断至 8 位小数  
usdtAmt | String | 实际到账 USDT 数量（`amt - fee`，向下截断至 8 位小数），到账至资金账户  
redeemType | String | 赎回类型：`"1"`（即时）或 `"2"`（标准）  
state | String | 订单状态：`"processing"` / `"success"` / `"failed"` / `"cancelled"`  
estSettlementTime | String | 预计到账时间，Unix 时间戳，单位为毫秒。即时赎回为当前时间；标准赎回：UTC+8 16:00 前提交加 5 自然日，16:00 后（含）提交加 6 自然日  
ts | String | 订单创建时间，Unix 时间戳，单位为毫秒，如 `1597026383085`  
  
### GET / 查询账户余额及累计收益 

查询您当前的 OKUSD 余额及持仓期间累计收益。所有余额均以母账户维度聚合，子账户共享。

#### 限速：2次/2s

#### 限速规则：User ID

#### Permission: Read

#### HTTP 请求

`GET /api/v5/finance/okusd/account`

> 请求示例
    
    
    GET /api/v5/finance/okusd/account
    

#### 请求参数

无

> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "ccy": "OKUSD",
                "amt": "10000.00000000",
                "totalEarnAccrual": "123.45678900",
                "ts": "1718500000000"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
ccy | String | 持仓货币，固定为 `"OKUSD"`  
amt | String | 当前 OKUSD 余额  
totalEarnAccrual | String | 持仓期间累计收益（USDT）  
ts | String | 服务器时间戳，Unix 时间戳，单位为毫秒，如 `1597026383085`  
  
### GET / 查询申购历史 

查询您的 OKUSD 申购历史订单。结果按时间戳倒序返回（最新优先），支持时间范围过滤。

#### 限速：5次/2s

#### 限速规则：User ID

#### Permission: Read

#### HTTP 请求

`GET /api/v5/finance/okusd/subscribe/history`

> 请求示例
    
    
    GET /api/v5/finance/okusd/subscribe/history?limit=2
    

#### 请求参数

**参数名** | **类型** | **是否必须** | **描述**  
---|---|---|---  
limit | String | 否 | 每页返回条数，默认 `"100"`，最大 `"100"`  
begin | String | 否 | 起始时间过滤（订单创建时间 `ts`，Unix ms，含）  
end | String | 否 | 结束时间过滤（订单创建时间 `ts`，Unix ms，含）  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "ordId": "680012345678901234",
                "clOrdId": "my-sub-001",
                "ccy": "USDT",
                "amt": "1000.00000000",
                "settleCcy": "OKUSD",
                "settleCcyAmt": "1000.00000000",
                "status": "success",
                "ts": "1718500000000"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
ordId | String | 系统订单 ID  
clOrdId | String | 客户自定义订单 ID（原样返回；未传则为空字符串）  
ccy | String | 申购货币，固定为 `"USDT"`  
amt | String | 申购 USDT 数量  
settleCcy | String | 到账货币，固定为 `"OKUSD"`  
settleCcyAmt | String | 到账 OKUSD 数量（= `amt`，汇率 1:1）  
status | String | 订单终态：`"success"` / `"failed"`  
ts | String | 订单创建时间，Unix 时间戳，单位为毫秒，如 `1597026383085`  
  
### GET / 查询赎回历史 

查询您的 OKUSD 赎回历史订单。结果按时间戳倒序返回（最新优先），支持时间范围过滤及赎回类型过滤。

#### 限速：5次/2s

#### 限速规则：User ID

#### Permission: Read

#### HTTP 请求

`GET /api/v5/finance/okusd/redeem/history`

> 请求示例
    
    
    GET /api/v5/finance/okusd/redeem/history?type=fast
    

#### 请求参数

**参数名** | **类型** | **是否必须** | **描述**  
---|---|---|---  
limit | String | 否 | 每页返回条数，默认 `"100"`，最大 `"100"`  
begin | String | 否 | 起始时间过滤（订单创建时间 `ts`，Unix ms，含）  
end | String | 否 | 结束时间过滤（订单创建时间 `ts`，Unix ms，含）  
type | String | 否 | 赎回类型过滤：`"fast"` 仅返回即时赎回；`"standard"` 仅返回标准赎回；不传默认返回标准赎回  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "ordId": "680012345678905678",
                "clOrdId": "my-rdm-fast-001",
                "ccy": "OKUSD",
                "amt": "1000.00000000",
                "fee": "1.00000000",
                "settleCcy": "USDT",
                "settleCcyAmt": "999.00000000",
                "type": "fast",
                "status": "success",
                "estSettlementTime": "1718500010000",
                "ts": "1718500000000"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
ordId | String | 系统订单 ID  
clOrdId | String | 客户自定义订单 ID（原样返回；未传则为空字符串）  
ccy | String | 赎回货币，固定为 `"OKUSD"`  
amt | String | 赎回 OKUSD 数量  
fee | String | 实收手续费（USDT），向下截断至 8 位小数  
settleCcy | String | 到账货币，固定为 `"USDT"`  
settleCcyAmt | String | 实际到账 USDT 数量（`amt - fee`，向下截断至 8 位小数）  
type | String | 赎回类型：`"fast"`（即时赎回）或 `"standard"`（标准赎回，D+5/D+6 自然日）  
status | String | 订单状态：`"pending"` / `"success"` / `"failed"` / `"canceled"`  
estSettlementTime | String | 预计到账时间，Unix 时间戳，单位为毫秒。已结算的即时赎回订单返回空字符串  
ts | String | 订单创建时间，Unix 时间戳，单位为毫秒，如 `1597026383085`  
  
### GET / 查询收益发放历史 

查询您的 OKUSD 每日收益发放历史。结果按时间戳倒序返回（最新优先）。

#### 限速：5次/2s

#### 限速规则：User ID

#### Permission: Read

#### HTTP 请求

`GET /api/v5/finance/okusd/rewards/history`

> 请求示例
    
    
    GET /api/v5/finance/okusd/rewards/history?limit=7
    

#### 请求参数

**参数名** | **类型** | **是否必须** | **描述**  
---|---|---|---  
limit | String | 否 | 每页返回条数，默认 `"30"`，最大 `"100"`  
begin | String | 否 | 起始时间过滤（`ts`，Unix ms，含），最大查询跨度 6 个月  
end | String | 否 | 结束时间过滤（`ts`，Unix ms，含），不传默认取当前时间  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "ccy": "USDT",
                "earnAmt": "1.14246575",
                "amt": "10000.00000000",
                "apr": "0.0418",
                "ts": "1718500000000"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
ccy | String | 收益货币，固定为 `"USDT"`  
earnAmt | String | 本次发放的 USDT 收益数量  
amt | String | 发放时点用户 USDT 本金余额  
apr | String | 本次发放适用的 APR，如 `"0.0418"` 表示 4.18%  
ts | String | 发放时间戳，Unix 时间戳，单位为毫秒，如 `1597026383085`  
  
### GET / 查询 APR 历史 

查询 OKUSD 历史 APR 快照。结果按时间戳倒序返回（最新优先）。虽然数据为产品级（非用户维度），本接口仍需 API Key 鉴权。

#### 限速：5次/2s

#### 限速规则：User ID

#### Permission: Read

#### HTTP 请求

`GET /api/v5/finance/okusd/rate/history`

> 请求示例
    
    
    GET /api/v5/finance/okusd/rate/history?limit=10
    

#### 请求参数

**参数名** | **类型** | **是否必须** | **描述**  
---|---|---|---  
limit | String | 否 | 每页返回条数，默认 `"30"`，最大 `"100"`  
begin | String | 否 | 起始时间过滤（`ts`，Unix ms，含），最大查询跨度 6 个月  
end | String | 否 | 结束时间过滤（`ts`，Unix ms，含），不传默认取当前时间  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            { "apr": "0.0418", "ts": "1718500000000" },
            { "apr": "0.0395", "ts": "1718413600000" }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
apr | String | 该快照时刻的 OKUSD APR，如 `"0.0418"` 表示 4.18%  
ts | String | 快照时间戳，Unix 时间戳，单位为毫秒，如 `1597026383085`