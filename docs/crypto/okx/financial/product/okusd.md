---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#financial-product-okusd
anchor_id: financial-product-okusd
api_type: API
updated_at: 2026-07-11 19:14:36.973605
---

# OKUSD

OKUSD is OKX's stablecoin receipt issued at a 1:1 rate against USDT. Holders earn daily APR with no action required, and OKUSD can be used as trading margin to improve capital efficiency.  
Subscription and redemption operate on the funding account. Use the `/limits` endpoint to check your remaining daily quota before subscribing or redeeming.  
  
### GET / OKUSD limits

Retrieve your remaining daily OKUSD subscription quota and both fast and standard redemption quotas. All limits are calculated at the master-account level and shared across sub-accounts.

#### Rate Limit: 2 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

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

#### Permission: Trade

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

#### Permission: Trade

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

---

# OKUSD

OKUSD 是 OKX 以 1:1 汇率发行的稳定币凭证，用户以 USDT 申购后持有即可享受每日收益，同时可用作交易账户保证金以提升资本效率。  
申购与赎回均在资金账户中操作。申购或赎回前可调用 `/limits` 接口查询当日剩余限额。  
  
### GET / 查询限额 

查询您当日 OKUSD 申购剩余限额及即时/标准赎回剩余限额。所有限额均以母账户维度计算，子账户共享。

#### 限速：2次/2s

#### 限速规则：User ID

#### 权限：读取

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

#### 权限：交易

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

#### 权限：交易

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