---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#global-liquidity-program-glp-c
anchor_id: global-liquidity-program-glp-c
api_type: API
updated_at: 2026-11-27 18:59:29.271553
---

# GLP-C

### GLP-C API  
  
GLP-C (Global Liquidity Program - C) APIs let eligible market makers discover and enroll instruments, and query their quote assessment results.

**Category** | **Endpoint**  
---|---  
Enrollment | Get eligible instruments · Enroll instruments · Get enrollment statistics  
Quote assessment | Get minute assessment · Get hourly instrument assessment · Get hourly assessment summary  
  
**Program rules**

Instruments are grouped into G1 / G2 / G3 with required bilateral weighted quoting share of 5% / 10% / 15%. Top 3 price levels are weighted 2 / 1 / 0.5. An instrument qualifies for an hour when it qualifies in at least 70% of minutes. Spot and Perpetuals are assessed separately. The tier is based directly on the number of qualified instruments, without a multiplier: Tier 1 ≥ 40 → VIP 9 Maker; Tier 2 30–39 → VIP 8; Tier 3 20–29 → VIP 7; Tier 4 10–19 → VIP 6. Taker fees follow the organic VIP tier.

During the public beta (24 Nov – 1 Dec 2026), the hourly uptime requirement is 50%, and `requiredUptime` / `requiredHourlyUptime` return `"0.5"`. From 1 Dec 2026, the requirement is 70% (`"0.7"`).

**General notes**

  * In requests, use `PERP` for perpetuals (including X-Perp). The hourly assessment summary returns `SWAP` for the same category.

  * Only accounts whitelisted for GLP-C can call these endpoints. Results are returned for the participant of the authenticated account. No user ID parameter is accepted.

  * An instrument is identified by `instType` \+ `instId`. The same `instId` can exist under different `instType`.

  * Timestamps use Unix timestamp format in milliseconds (UTC), e.g. `1795154400000`. Query ranges are inclusive. Assessment data is available for the last 72 hours.

  * Quote assessment endpoints return all values as strings. Unavailable values are returned as `""`. Empty results are returned as `[]`.

#### Assessment reason codes

**Reason code** | **Description**  
---|---  
QUALIFIED | The minute meets the qualification requirements  
BELOW_THRESHOLD | Share is below the threshold  
NO_CUSTOMER_QUOTE | No quotes from the account in this minute  
MARKET_DENOMINATOR_ZERO | No market quotes in this minute  
SOURCE_DATA_MISSING | Market snapshot is missing  
SOURCE_DATA_INVALID | Market snapshot is unusable  
  
### Get GLP-C eligible instruments

Retrieve GLP-C instruments eligible for the current account, with registration counts and qualification requirements.

#### Rate Limit: 5 requests per second

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/users/glp-c/instruments`

> Request Example
    
    
    GET /api/v5/users/glp-c/instruments?instType=SPOT&page=1&pageSize=10&filterType=1
    

#### Request Parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
instType | String | Yes | Instrument type  
`SPOT`: Spot  
`PERP`: Perpetual  
page | Integer | Yes | Page number, starting from `1`  
pageSize | Integer | Yes | Number of results per page. The maximum is `100`  
filterType | Integer | Yes | `1`: All eligible instruments  
`2`: Registered  
`3`: Open for registration  
instId | String | No | Instrument ID, e.g. `BTC-USDT`  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": {
            "page": 1,
            "pageSize": 10,
            "total": 1,
            "startIndex": 0,
            "hasNextPage": false,
            "rows": [
                {
                    "instType": "SPOT",
                    "instId": "BTC-USDT",
                    "instGroup": "G1",
                    "registeredClientCount": 0,
                    "dailyAvgPlatTv7d": "0",
                    "b3PriceLevel": "5",
                    "b3PriceQuoteSize": "25",
                    "requiredMarketShare": "0.05",
                    "requiredUptime": "0.7"
                }
            ]
        }
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
page | Integer | Current page number  
pageSize | Integer | Number of results per page  
total | Integer | Total number of results before pagination  
startIndex | Integer | Zero-based offset of the current page: (page − 1) × pageSize  
hasNextPage | Boolean | Whether there is a next page  
rows | Array of objects | Instrument list. `[]` if there are no results  
> instType | String | Instrument type  
> instId | String | Instrument ID  
> instGroup | String | Instrument group  
`G1`  
`G2`  
`G3`  
> registeredClientCount | Integer | Number of clients registered for the instrument  
> dailyAvgPlatTv7d | String | 7-day daily average platform trading volume  
> b3PriceLevel | String | Average spread between the third-best ask and bid over the past 7 days, calculated as (ask₃ − bid₃) ÷ their midpoint × 10,000, in bp. Lower values indicate a tighter order book.  
> b3PriceQuoteSize | String | Average combined bid and ask quote size across order book levels 1–3 over the past 7 days, in USD. For example, `25` means 25 USD.  
> requiredMarketShare | String | Required minute market share. e.g. `0.05` means 5%.  
> requiredUptime | String | Required hourly uptime. e.g. `0.7` means 70%  
Only instruments tradable by the current account are returned. 

### POST / Enroll GLP-C instruments

Enroll one or more instruments in GLP-C. Enrollment applies to the whole participant and is assessed from the current minute.

#### Rate Limit: 5 requests per second

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/users/glp-c/enroll-instruments`

> Request Example
    
    
    POST /api/v5/users/glp-c/enroll-instruments
    body
    {
        "instsToEnroll": [
            {"instType": "SPOT", "instId": "BTC-USDT"},
            {"instType": "PERP", "instId": "BTC-USDT"}
        ]
    }
    

#### Request Parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
instsToEnroll | Array of objects | Yes | Instruments to enroll  
> instType | String | Yes | Instrument type  
`SPOT`  
`PERP`  
> instId | String | Yes | Instrument ID, e.g. `BTC-USDT`  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": {
            "enrolledInsts": [
                {"instType": "SPOT", "instId": "BTC-USDT"}
            ],
            "failedInsts": [
                {"instType": "PERP", "instId": "BTC-USDT"}
            ]
        }
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
enrolledInsts | Array of objects | Instruments enrolled successfully  
> instType | String | Instrument type  
> instId | String | Instrument ID  
failedInsts | Array of objects | Instruments that failed to enroll, because they are invalid or not eligible for the account  
> instType | String | Instrument type  
> instId | String | Instrument ID  
Enrolling an instrument that is already enrolled returns it in `enrolledInsts`. Withdrawal is not supported in this phase. 

### Get GLP-C enrollment statistics

Retrieve the total, registered and open-for-registration instrument counts.

#### Rate Limit: 5 requests per second

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/users/glp-c/enroll/stats`

> Request Example
    
    
    GET /api/v5/users/glp-c/enroll/stats?instType=SPOT
    

#### Request Parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
instType | String | Yes | Instrument type  
`SPOT`  
`PERP`  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": {
            "totalInstCount": 500,
            "registeredInstCount": 40,
            "availableInstCount": 460
        }
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
totalInstCount | Integer | Total number of instruments  
registeredInstCount | Integer | Number of registered instruments  
availableInstCount | Integer | Number of instruments open for registration  
`availableInstCount` is not necessarily equal to `totalInstCount` − `registeredInstCount`. 

### Get GLP-C minute assessment

Retrieve minute-level assessment results of one instrument, including the share against the threshold and quote sizes by price level.

#### Rate Limit: 5 requests per second

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/users/glp-c/quote-assessment/minute`

> Request Example
    
    
    GET /api/v5/users/glp-c/quote-assessment/minute?instType=PERP&instIdCode=10459&beginTs=1795154460000&endTs=1795154519999
    

#### Request Parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
instType | String | No | Instrument type  
`SPOT`  
`PERP` (including X-Perp)  
instId | String | Conditional | Instrument ID, e.g. `BTC-USDT-SWAP`. Either `instId` or `instIdCode` is required  
instIdCode | String | Conditional | Instrument ID code, e.g. `10459`. If both are passed, `instIdCode` is used  
beginTs | Integer | Yes | Start time, Unix timestamp in milliseconds. Within the last 72 hours  
endTs | Integer | Yes | End time, Unix timestamp in milliseconds. Not later than the request time  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "instIdCode": "10459",
                "instType": "PERP",
                "instId": "BTC-USDT-SWAP",
                "minuteTs": "1795154460000",
                "bilateralWeightedShare": "0.0600000000",
                "threshold": "0.05",
                "minuteStatus": "QUALIFIED",
                "reasonCode": "QUALIFIED",
                "participantBidOriginalQuoteSizeUsd": "2300",
                "participantAskOriginalQuoteSizeUsd": "2300",
                "participantBidWeightedQuoteSizeUsd": "3050",
                "participantAskWeightedQuoteSizeUsd": "3250",
                "levels": [
                    {"level": "1", "multiplier": "2", "bidQuoteSizeUsd": "1000", "askQuoteSizeUsd": "1200", "bidMultipliedSizeUsd": "2000", "askMultipliedSizeUsd": "2400"},
                    {"level": "2", "multiplier": "1", "bidQuoteSizeUsd": "800", "askQuoteSizeUsd": "600", "bidMultipliedSizeUsd": "800", "askMultipliedSizeUsd": "600"},
                    {"level": "3", "multiplier": "0.5", "bidQuoteSizeUsd": "500", "askQuoteSizeUsd": "500", "bidMultipliedSizeUsd": "250", "askMultipliedSizeUsd": "250"}
                ]
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instIdCode | String | Instrument ID code  
instType | String | Instrument type  
instId | String | Instrument ID  
minuteTs | String | Start of the minute, Unix timestamp in milliseconds  
bilateralWeightedShare | String | Bilateral weighted share, 10 decimal places. e.g. `0.0600000000` means 6%  
threshold | String | Share threshold for this minute  
minuteStatus | String | `QUALIFIED`  
`NOT_QUALIFIED`  
reasonCode | String | Assessment reason. See Assessment reason codes in GLP-C API  
participantBidOriginalQuoteSizeUsd | String | Total bid quote size, in USD  
participantAskOriginalQuoteSizeUsd | String | Total ask quote size, in USD  
participantBidWeightedQuoteSizeUsd | String | Total weighted bid quote size, in USD  
participantAskWeightedQuoteSizeUsd | String | Total weighted ask quote size, in USD  
levels | Array of objects | Details by price level. `[]` if there are no details  
> level | String | Price level, starting from `1`  
> multiplier | String | Weight of the price level  
> bidQuoteSizeUsd | String | Bid quote size, in USD  
> askQuoteSizeUsd | String | Ask quote size, in USD  
> bidMultipliedSizeUsd | String | bidQuoteSizeUsd × multiplier, in USD  
> askMultipliedSizeUsd | String | askQuoteSizeUsd × multiplier, in USD  
Results are sorted by `minuteTs` in ascending order. Minutes without results are not filled in. 

### Get GLP-C hourly instrument assessment

Retrieve hourly qualification results of one instrument for ended hours.

#### Rate Limit: 5 requests per second

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/users/glp-c/quote-assessment/hour/instrument`

> Request Example
    
    
    GET /api/v5/users/glp-c/quote-assessment/hour/instrument?instType=PERP&instIdCode=10459&beginTs=1795154400000&endTs=1795157999999
    

#### Request Parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
instType | String | No | Instrument type  
`SPOT`  
`PERP` (including X-Perp)  
instId | String | Conditional | Instrument ID, e.g. `BTC-USDT-SWAP`. Either `instId` or `instIdCode` is required  
instIdCode | String | Conditional | Instrument ID code, e.g. `10459`. If both are passed, `instIdCode` is used  
beginTs | Integer | Yes | Start time, Unix timestamp in milliseconds. Within the last 72 hours  
endTs | Integer | Yes | End time, Unix timestamp in milliseconds. Not later than the request time  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "instIdCode": "10459",
                "instType": "PERP",
                "instId": "BTC-USDT-SWAP",
                "assessmentHour": "1795154400000",
                "instGroup": "G1",
                "threshold": "0.05",
                "requiredHourlyUptime": "0.7",
                "qualifiedMinutes": "1",
                "notQualifiedMinutes": "1",
                "hourlyUptime": "0.0166666667",
                "hourStatus": "DELAYED",
                "intendedEffectiveHour": "1795158000000",
                "finalizedAt": "",
                "minuteStatusDetail": [
                    {"minuteTs": "1795154400000", "minuteStatus": "NOT_QUALIFIED", "reasonCode": "BELOW_THRESHOLD"},
                    {"minuteTs": "1795154460000", "minuteStatus": "QUALIFIED", "reasonCode": "QUALIFIED"}
                ]
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instIdCode | String | Instrument ID code  
instType | String | Instrument type  
instId | String | Instrument ID  
assessmentHour | String | Start of the assessment hour, Unix timestamp in milliseconds  
instGroup | String | Instrument group for this hour  
threshold | String | Minute share threshold for this hour  
requiredHourlyUptime | String | Required hourly uptime. e.g. `0.7` means 70%  
qualifiedMinutes | String | Number of qualified minutes  
notQualifiedMinutes | String | Number of not-qualified minutes  
hourlyUptime | String | qualifiedMinutes ÷ 60, 10 decimal places  
hourStatus | String | `QUALIFIED`  
`NOT_QUALIFIED`  
`DELAYED`: the hour has ended but is not finalized  
intendedEffectiveHour | String | Hour in which the result is intended to take effect, Unix timestamp in milliseconds  
finalizedAt | String | Finalization time, Unix timestamp in milliseconds. `""` if `DELAYED`  
minuteStatusDetail | Array of objects | Result of each minute  
> minuteTs | String | Start of the minute, Unix timestamp in milliseconds  
> minuteStatus | String | `QUALIFIED`  
`NOT_QUALIFIED`  
> reasonCode | String | Assessment reason  
An hour is qualified when `qualifiedMinutes` ≥ ceil(`requiredHourlyUptime` × 60). For example, 70% requires at least 42 qualified minutes. The current hour is not returned. 

### Get GLP-C hourly assessment summary

Retrieve hourly qualified instrument counts and the calculated GLP-C tier.

#### Rate Limit: 5 requests per second

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/users/glp-c/quote-assessment/hour/summary`

> Request Example
    
    
    GET /api/v5/users/glp-c/quote-assessment/hour/summary?instType=PERP&beginTs=1795150800000&endTs=1795158000000
    

#### Request Parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
instType | String | No | Instrument type  
`SPOT`  
`PERP` (including X-Perp)  
If not passed, both are returned  
beginTs | Integer | Yes | Start time, Unix timestamp in milliseconds. Within the last 72 hours  
endTs | Integer | Yes | End time, Unix timestamp in milliseconds. Not later than the request time. The current hour can be included  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "assessmentHour": "1795150800000",
                "instType": "SWAP",
                "state": "finalized",
                "registeredInstCount": "47",
                "qualifiedInstCount": "23",
                "qualifiedInstRatio": "0.4893617021",
                "tier": "3",
                "intendedEffectiveHour": "1795154400000"
            },
            {
                "assessmentHour": "1795158000000",
                "instType": "SWAP",
                "state": "in_progress",
                "registeredInstCount": "47",
                "qualifiedInstCount": "0",
                "qualifiedInstRatio": "0.0000000000",
                "tier": "",
                "intendedEffectiveHour": "1795161600000"
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
assessmentHour | String | Start of the assessment hour, Unix timestamp in milliseconds  
instType | String | Instrument type  
`SPOT`  
`SWAP` (including X-Perp)  
state | String | `in_progress`: current hour, provisional  
`finalized`  
`delayed`: ended but not finalized  
registeredInstCount | String | Number of registered instruments assessed in this hour  
qualifiedInstCount | String | Number of qualified instruments  
qualifiedInstRatio | String | qualifiedInstCount ÷ registeredInstCount, 10 decimal places  
tier | String | Calculated GLP-C tier, based directly on the number of qualified instruments in the hour. `1`: ≥ 40 (VIP 9 Maker); `2`: 30–39 (VIP 8); `3`: 20–29 (VIP 7); `4`: 10–19 (VIP 6). `""` if fewer than 10 or unknown. For the current hour, this is the estimated tier for the next hour.  
intendedEffectiveHour | String | Hour in which the result is intended to take effect, Unix timestamp in milliseconds  
Results are sorted by `assessmentHour` in ascending order, with `SPOT` before `SWAP` in the same hour. `tier` and `intendedEffectiveHour` do not confirm the fee tier actually applied.

---

# GLP-C

### GLP-C API   
  
GLP-C（Global Liquidity Program - C）API 供符合条件的做市商查询及注册产品，并查询其报价考核结果。

**类别** | **接口**  
---|---  
注册 | 获取可参与产品 · 注册产品 · 获取注册统计  
报价考核 | 获取分钟考核 · 获取产品小时考核 · 获取小时考核汇总  
  
**计划规则**

产品分为 G1 / G2 / G3，双边加权报价份额门槛分别为 5% / 10% / 15%。前三档价格权重分别为 2 / 1 / 0.5。一个小时内至少 70% 的分钟达标，该产品才在该小时达标。现货和永续合约分开考核。等级直接按达标产品数量计算，不使用 multiplier 加权：Tier 1 ≥ 40 → VIP 9 Maker；Tier 2 为 30–39 → VIP 8；Tier 3 为 20–29 → VIP 7；Tier 4 为 10–19 → VIP 6。Taker 费率按原生 VIP 等级执行。

公测期间（2026 年 11 月 24 日至 12 月 1 日），小时在线率要求为 50%，`requiredUptime` / `requiredHourlyUptime` 返回 `"0.5"`。自 2026 年 12 月 1 日起，要求为 70%（`"0.7"`）。

**通用说明**

  * 请求中使用 `PERP` 表示永续合约（含 X-Perp）；小时考核汇总响应使用 `SWAP` 表示相同类别。

  * 仅 GLP-C 白名单账户可调用这些接口。返回结果为当前鉴权账户所属 participant 的数据。不支持传入用户 ID 参数。

  * 产品由 `instType` \+ `instId` 唯一确定。同一 `instId` 可能存在于不同的 `instType` 下。

  * 时间戳均为 Unix 毫秒时间戳（UTC），如 `1795154400000`。查询时间范围为闭区间。考核数据保留最近 72 小时。

  * 报价考核接口的所有数值均以字符串返回。不可用的值返回 `""`。无结果时返回 `[]`。

#### 考核原因码

**原因码** | **描述**  
---|---  
QUALIFIED | 该分钟满足达标要求  
BELOW_THRESHOLD | 份额低于门槛  
NO_CUSTOMER_QUOTE | 该分钟内账户无报价  
MARKET_DENOMINATOR_ZERO | 该分钟内市场无报价  
SOURCE_DATA_MISSING | 市场快照缺失  
SOURCE_DATA_INVALID | 市场快照不可用  
  
### 获取 GLP-C 可参与产品 

获取当前账户可参与 GLP-C 的产品，包括注册数量及达标要求。

#### 限速：5次/s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/users/glp-c/instruments`

> 请求示例
    
    
    GET /api/v5/users/glp-c/instruments?instType=SPOT&page=1&pageSize=10&filterType=1
    

#### 请求参数

**参数名** | **类型** | **是否必须** | **描述**  
---|---|---|---  
instType | String | 是 | 产品类型  
`SPOT`：现货  
`PERP`：永续合约  
page | Integer | 是 | 页码，从 `1` 开始  
pageSize | Integer | 是 | 每页返回的结果数量，最大为 `100`  
filterType | Integer | 是 | `1`：全部可参与产品  
`2`：已注册  
`3`：可注册  
instId | String | 否 | 产品 ID，如 `BTC-USDT`  
  
> 返回示例
    
    
    {
        "code": "0",
        "msg": "",
        "data": {
            "page": 1,
            "pageSize": 10,
            "total": 1,
            "startIndex": 0,
            "hasNextPage": false,
            "rows": [
                {
                    "instType": "SPOT",
                    "instId": "BTC-USDT",
                    "instGroup": "G1",
                    "registeredClientCount": 0,
                    "dailyAvgPlatTv7d": "0",
                    "b3PriceLevel": "5",
                    "b3PriceQuoteSize": "25",
                    "requiredMarketShare": "0.05",
                    "requiredUptime": "0.7"
                }
            ]
        }
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
page | Integer | 当前页码  
pageSize | Integer | 每页返回的结果数量  
total | Integer | 分页前的结果总数  
startIndex | Integer | 当前页的起始偏移量（从 0 开始）：(page − 1) × pageSize  
hasNextPage | Boolean | 是否有下一页  
rows | Array of objects | 产品列表。无结果时返回 `[]`  
> instType | String | 产品类型  
> instId | String | 产品 ID  
> instGroup | String | 产品分组  
`G1`  
`G2`  
`G3`  
> registeredClientCount | Integer | 已注册该产品的客户数量  
> dailyAvgPlatTv7d | String | 平台近 7 日日均交易量  
> b3PriceLevel | String | 过去 7 天第三档卖价与买价之间价差的平均值，计算公式为（ask₃ − bid₃）÷ 两者中间价 × 10,000，单位为 bp。数值越低表示订单簿价差越小。  
> b3PriceQuoteSize | String | 过去 7 天订单簿买卖两侧第 1–3 档合计报价量的平均值，单位为 USD。例如，`25` 表示 25 USD。  
> requiredMarketShare | String | 要求的分钟市场份额，如 `0.05` 表示 5%。  
> requiredUptime | String | 要求的小时在线率。如 `0.7` 表示 70%  
仅返回当前账户可交易的产品。 

### POST / 注册 GLP-C 产品 

为一个或多个产品注册 GLP-C。注册对整个 participant 生效，并从当前分钟起计入考核。

#### 限速：5次/s

#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/users/glp-c/enroll-instruments`

> 请求示例
    
    
    POST /api/v5/users/glp-c/enroll-instruments
    body
    {
        "instsToEnroll": [
            {"instType": "SPOT", "instId": "BTC-USDT"},
            {"instType": "PERP", "instId": "BTC-USDT"}
        ]
    }
    

#### 请求参数

**参数名** | **类型** | **是否必须** | **描述**  
---|---|---|---  
instsToEnroll | Array of objects | 是 | 要注册的产品  
> instType | String | 是 | 产品类型  
`SPOT`  
`PERP`  
> instId | String | 是 | 产品 ID，如 `BTC-USDT`  
  
> 返回示例
    
    
    {
        "code": "0",
        "msg": "",
        "data": {
            "enrolledInsts": [
                {"instType": "SPOT", "instId": "BTC-USDT"}
            ],
            "failedInsts": [
                {"instType": "PERP", "instId": "BTC-USDT"}
            ]
        }
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
enrolledInsts | Array of objects | 注册成功的产品  
> instType | String | 产品类型  
> instId | String | 产品 ID  
failedInsts | Array of objects | 注册失败的产品，原因为产品无效或当前账户不可参与  
> instType | String | 产品类型  
> instId | String | 产品 ID  
注册已注册的产品时，该产品会在 `enrolledInsts` 中返回。本期不支持退出注册。 

### 获取 GLP-C 注册统计 

获取产品总数、已注册产品数及可注册产品数。

#### 限速：5次/s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/users/glp-c/enroll/stats`

> 请求示例
    
    
    GET /api/v5/users/glp-c/enroll/stats?instType=SPOT
    

#### 请求参数

**参数名** | **类型** | **是否必须** | **描述**  
---|---|---|---  
instType | String | 是 | 产品类型  
`SPOT`  
`PERP`  
  
> 返回示例
    
    
    {
        "code": "0",
        "msg": "",
        "data": {
            "totalInstCount": 500,
            "registeredInstCount": 40,
            "availableInstCount": 460
        }
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
totalInstCount | Integer | 产品总数  
registeredInstCount | Integer | 已注册产品数  
availableInstCount | Integer | 可注册产品数  
`availableInstCount` 不一定等于 `totalInstCount` − `registeredInstCount`。 

### 获取 GLP-C 分钟考核 

获取单个产品的分钟级考核结果，包括份额与门槛的对比及各价格档位的报价数量。

#### 限速：5次/s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/users/glp-c/quote-assessment/minute`

> 请求示例
    
    
    GET /api/v5/users/glp-c/quote-assessment/minute?instType=PERP&instIdCode=10459&beginTs=1795154460000&endTs=1795154519999
    

#### 请求参数

**参数名** | **类型** | **是否必须** | **描述**  
---|---|---|---  
instType | String | 否 | 产品类型  
`SPOT`  
`PERP`（含 X-Perp）  
instId | String | 可选 | 产品 ID，如 `BTC-USDT-SWAP`。`instId` 和 `instIdCode` 必须传其一  
instIdCode | String | 可选 | 产品唯一标识代码，如 `10459`。若同时传入，以 `instIdCode` 为准  
beginTs | Integer | 是 | 开始时间，Unix 毫秒时间戳。须在最近 72 小时内  
endTs | Integer | 是 | 结束时间，Unix 毫秒时间戳。不晚于请求时间  
  
> 返回示例
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "instIdCode": "10459",
                "instType": "PERP",
                "instId": "BTC-USDT-SWAP",
                "minuteTs": "1795154460000",
                "bilateralWeightedShare": "0.0600000000",
                "threshold": "0.05",
                "minuteStatus": "QUALIFIED",
                "reasonCode": "QUALIFIED",
                "participantBidOriginalQuoteSizeUsd": "2300",
                "participantAskOriginalQuoteSizeUsd": "2300",
                "participantBidWeightedQuoteSizeUsd": "3050",
                "participantAskWeightedQuoteSizeUsd": "3250",
                "levels": [
                    {"level": "1", "multiplier": "2", "bidQuoteSizeUsd": "1000", "askQuoteSizeUsd": "1200", "bidMultipliedSizeUsd": "2000", "askMultipliedSizeUsd": "2400"},
                    {"level": "2", "multiplier": "1", "bidQuoteSizeUsd": "800", "askQuoteSizeUsd": "600", "bidMultipliedSizeUsd": "800", "askMultipliedSizeUsd": "600"},
                    {"level": "3", "multiplier": "0.5", "bidQuoteSizeUsd": "500", "askQuoteSizeUsd": "500", "bidMultipliedSizeUsd": "250", "askMultipliedSizeUsd": "250"}
                ]
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
instIdCode | String | 产品唯一标识代码  
instType | String | 产品类型  
instId | String | 产品 ID  
minuteTs | String | 该分钟的开始时间，Unix 毫秒时间戳  
bilateralWeightedShare | String | 双边加权份额，保留 10 位小数。如 `0.0600000000` 表示 6%  
threshold | String | 该分钟的份额门槛  
minuteStatus | String | `QUALIFIED`  
`NOT_QUALIFIED`  
reasonCode | String | 考核原因。详见 GLP-C API中的考核原因码  
participantBidOriginalQuoteSizeUsd | String | 买方报价总量，单位为 USD  
participantAskOriginalQuoteSizeUsd | String | 卖方报价总量，单位为 USD  
participantBidWeightedQuoteSizeUsd | String | 买方加权报价总量，单位为 USD  
participantAskWeightedQuoteSizeUsd | String | 卖方加权报价总量，单位为 USD  
levels | Array of objects | 各价格档位详情。无详情时返回 `[]`  
> level | String | 价格档位，从 `1` 开始  
> multiplier | String | 该价格档位的权重  
> bidQuoteSizeUsd | String | 买方报价数量，单位为 USD  
> askQuoteSizeUsd | String | 卖方报价数量，单位为 USD  
> bidMultipliedSizeUsd | String | bidQuoteSizeUsd × multiplier，单位为 USD  
> askMultipliedSizeUsd | String | askQuoteSizeUsd × multiplier，单位为 USD  
结果按 `minuteTs` 升序排列。无结果的分钟不补齐。 

### 获取 GLP-C 产品小时考核 

获取单个产品已结束小时的小时达标结果。

#### 限速：5次/s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/users/glp-c/quote-assessment/hour/instrument`

> 请求示例
    
    
    GET /api/v5/users/glp-c/quote-assessment/hour/instrument?instType=PERP&instIdCode=10459&beginTs=1795154400000&endTs=1795157999999
    

#### 请求参数

**参数名** | **类型** | **是否必须** | **描述**  
---|---|---|---  
instType | String | 否 | 产品类型  
`SPOT`  
`PERP`（含 X-Perp）  
instId | String | 可选 | 产品 ID，如 `BTC-USDT-SWAP`。`instId` 和 `instIdCode` 必须传其一  
instIdCode | String | 可选 | 产品唯一标识代码，如 `10459`。若同时传入，以 `instIdCode` 为准  
beginTs | Integer | 是 | 开始时间，Unix 毫秒时间戳。须在最近 72 小时内  
endTs | Integer | 是 | 结束时间，Unix 毫秒时间戳。不晚于请求时间  
  
> 返回示例
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "instIdCode": "10459",
                "instType": "PERP",
                "instId": "BTC-USDT-SWAP",
                "assessmentHour": "1795154400000",
                "instGroup": "G1",
                "threshold": "0.05",
                "requiredHourlyUptime": "0.7",
                "qualifiedMinutes": "1",
                "notQualifiedMinutes": "1",
                "hourlyUptime": "0.0166666667",
                "hourStatus": "DELAYED",
                "intendedEffectiveHour": "1795158000000",
                "finalizedAt": "",
                "minuteStatusDetail": [
                    {"minuteTs": "1795154400000", "minuteStatus": "NOT_QUALIFIED", "reasonCode": "BELOW_THRESHOLD"},
                    {"minuteTs": "1795154460000", "minuteStatus": "QUALIFIED", "reasonCode": "QUALIFIED"}
                ]
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
instIdCode | String | 产品唯一标识代码  
instType | String | 产品类型  
instId | String | 产品 ID  
assessmentHour | String | 考核小时的开始时间，Unix 毫秒时间戳  
instGroup | String | 该小时的产品分组  
threshold | String | 该小时的分钟份额门槛  
requiredHourlyUptime | String | 要求的小时在线率。如 `0.7` 表示 70%  
qualifiedMinutes | String | 达标分钟数  
notQualifiedMinutes | String | 未达标分钟数  
hourlyUptime | String | qualifiedMinutes ÷ 60，保留 10 位小数  
hourStatus | String | `QUALIFIED`  
`NOT_QUALIFIED`  
`DELAYED`：该小时已结束但尚未最终确定  
intendedEffectiveHour | String | 该结果预计生效的小时，Unix 毫秒时间戳  
finalizedAt | String | 最终确定时间，Unix 毫秒时间戳。`DELAYED` 时返回 `""`  
minuteStatusDetail | Array of objects | 每分钟的结果  
> minuteTs | String | 该分钟的开始时间，Unix 毫秒时间戳  
> minuteStatus | String | `QUALIFIED`  
`NOT_QUALIFIED`  
> reasonCode | String | 考核原因  
当 `qualifiedMinutes` ≥ ceil(`requiredHourlyUptime` × 60) 时，该小时达标。例如，70% 要求至少 42 个达标分钟。不返回当前小时。 

### 获取 GLP-C 小时考核汇总 

获取每小时的达标产品数量及计算得出的 GLP-C 等级。

#### 限速：5次/s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/users/glp-c/quote-assessment/hour/summary`

> 请求示例
    
    
    GET /api/v5/users/glp-c/quote-assessment/hour/summary?instType=PERP&beginTs=1795150800000&endTs=1795158000000
    

#### 请求参数

**参数名** | **类型** | **是否必须** | **描述**  
---|---|---|---  
instType | String | 否 | 产品类型  
`SPOT`  
`PERP`（含 X-Perp）  
不传时两者均返回  
beginTs | Integer | 是 | 开始时间，Unix 毫秒时间戳。须在最近 72 小时内  
endTs | Integer | 是 | 结束时间，Unix 毫秒时间戳。不晚于请求时间。可包含当前小时  
  
> 返回示例
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "assessmentHour": "1795150800000",
                "instType": "SWAP",
                "state": "finalized",
                "registeredInstCount": "47",
                "qualifiedInstCount": "23",
                "qualifiedInstRatio": "0.4893617021",
                "tier": "3",
                "intendedEffectiveHour": "1795154400000"
            },
            {
                "assessmentHour": "1795158000000",
                "instType": "SWAP",
                "state": "in_progress",
                "registeredInstCount": "47",
                "qualifiedInstCount": "0",
                "qualifiedInstRatio": "0.0000000000",
                "tier": "",
                "intendedEffectiveHour": "1795161600000"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
assessmentHour | String | 考核小时的开始时间，Unix 毫秒时间戳  
instType | String | 产品类型  
`SPOT`  
`SWAP`（含 X-Perp）  
state | String | `in_progress`：当前小时，结果为临时值  
`finalized`  
`delayed`：已结束但尚未最终确定  
registeredInstCount | String | 该小时参与考核的已注册产品数  
qualifiedInstCount | String | 达标产品数  
qualifiedInstRatio | String | qualifiedInstCount ÷ registeredInstCount，保留 10 位小数  
tier | String | GLP-C 等级，直接按该小时的达标产品数量计算。`1`：≥ 40（VIP 9 Maker）；`2`：30–39（VIP 8）；`3`：20–29（VIP 7）；`4`：10–19（VIP 6）。少于 10 个或未知时返回 `""`。对于当前小时，为下一小时的预估等级。  
intendedEffectiveHour | String | 该结果预计生效的小时，Unix 毫秒时间戳  
结果按 `assessmentHour` 升序排列，同一小时内 `SPOT` 排在 `SWAP` 之前。`tier` 和 `intendedEffectiveHour` 不代表实际适用的费率等级。