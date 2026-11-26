---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#global-liquidity-program
anchor_id: global-liquidity-program
api_type: API
updated_at: 2026-11-26 19:00:30.165464
---

# Global Liquidity Program

## Introduction

The OKX Global Liquidity Program (GLP) offers fee benefits to eligible market makers based on trading or quoting performance.

  * **GLP-A** : Type A (top) pairs. Assessed weekly on unadjusted trading market share, separately for Maker and Taker. Benefit: VIP 9 + Colo.
  * **GLP-B** : Type B pairs (most other pairs). Assessed weekly on adjusted trading market share, separately for Maker and Taker. Benefit: VIP 6–9, with Colo at VIP 9. Expiry Futures & Nitro Spreads are assessed across all pairs on unadjusted share.
  * **GLP-C** : Liquidity-incentive pairs (Spot and Perpetuals). Assessed hourly on bilateral weighted quoting share. Benefit: VIP 6–9 Maker fees from the next hour.

Participants must meet AUM and organic VIP tier requirements; see the [OKX Liquidity Program page](https://www.okx.com/fees/liquidity-program) for details. Where more than one program applies, the most favorable fee applies. Program participants are not eligible for other VIP-related or volume-related promotions or rebates.

Only enrolled accounts can access the user endpoints in this section. A sub-account API key returns the master account's data.

[Program details](https://www.okx.com/help/introducing-the-okx-global-liquidity-program) · [GLP Workspace](https://www.okx.com/glp-workspace) · To apply, contact your Relationship Manager or email `institutional@okx.com`.

**Common error codes**

Error code | HTTP status code | Error message  
---|---|---  
50001 | 503 | Service temporarily unavailable. Please try again later.  
50014 | 200 | Parameter {param0} can not be empty  
50016 | 200 | Parameter {param0} does not match parameter {param1}  
50026 | 500 | System error. Try again later  
50030 | 200 | You don't have permission to use this API endpoint  
51000 | 200 | Parameter error  
  
## GLP-A / GLP-B

### Get GLP instrument types

Retrieve the GLP-A / GLP-B classification of SPOT and SWAP instruments. Use this endpoint to check which program and pool an instrument is assessed under. Expiry Futures & Nitro Spreads are not classified by pair type; all pairs are assessed together. GLP-C instruments are listed by Get GLP-C eligible instruments. Classifications and volume weights are for reference only; the OKX website and the program brochure prevail.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/public/mm-instrument-types`

> Request Example
    
    
    GET /api/v5/public/mm-instrument-types?instType=SWAP
    
    
    
    import okx.PublicData as PublicData
    
    flag = "0"  # Production trading: 0, Demo trading: 1
    
    publicDataAPI = PublicData.PublicAPI(flag=flag)
    
    # Retrieve the list of GLP-A / GLP-B instrument classifications
    result = publicDataAPI.get_mm_instrument_types(
        instType="SWAP"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | No | Instrument type.  
`SPOT`  
`SWAP`  
When not specified, returns all types.  
instId | String | No | Instrument ID, e.g. `BTC-USDT`, `BTC-USDT-SWAP`.  
When specified, returns at most one record.  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "instId": "BTC-USDT-SWAP",
                "instType": "SWAP",
                "pairType": "A"
            },
            {
                "instId": "ETH-USDT-SWAP",
                "instType": "SWAP",
                "pairType": "A"
            },
            {
                "instId": "XAU-USDT-SWAP",
                "instType": "SWAP",
                "pairType": "B-TradFi"
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instId | String | Instrument ID, e.g. `BTC-USDT-SWAP`  
instType | String | Instrument type.  
`SPOT`  
`SWAP`  
pairType | String | GLP-A / GLP-B classification.  
`A`: Type A pair. Assessed under GLP-A (unadjusted share)  
`B-Crypto`: Type B crypto pair. Assessed under GLP-B; volume weight 1×  
`B-TradFi`: Type B TradFi pair (Spot and Perpetuals). Assessed under GLP-B; volume weight 2×  
`Type Special`: GLP Special Pair. Assessed under GLP-B; volume weight 4×  
  
### Get GLP v2 overview

Retrieve active GLP-A / GLP-B enrollments, current tiers, estimated next tiers, tier requirements, and week-to-date performance for the authenticated account. A sub-account API key retrieves the master account's data.

Weekly assessment: upgrades take effect on Tuesday 00:00 (UTC+8) and downgrades on Wednesday 00:00 (UTC+8). `gracePeriodEndTime` is the earliest time a downgrade can take effect.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/users/glp/v2/overview`

> Request Example
    
    
    GET /api/v5/users/glp/v2/overview
    

#### Request Parameters

No request parameters.

> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "programs": [
                    {
                        "bizId": "16",
                        "program": "GLP_B",
                        "side": "MAKER",
                        "instrument": "PERP",
                        "currentTier": "Tier 2",
                        "estNextTier": "Tier 2",
                        "estNextStatus": "qualify",
                        "gracePeriodEndTime": "",
                        "requirement": [
                            {
                                "tier": "Tier 1",
                                "share": "0.005"
                            },
                            {
                                "tier": "Tier 2",
                                "share": "0.003"
                            }
                        ],
                        "performance": [
                            {
                                "date": "1726531200000",
                                "assessPeriod": "PREVIOUS",
                                "share": "0.0035",
                                "vol": "140000"
                            },
                            {
                                "date": "1726876800000",
                                "assessPeriod": "CURRENT",
                                "share": "0.004",
                                "vol": "200"
                            }
                        ]
                    }
                ]
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
programs | Array of objects | Active GLP enrollments. Empty array when none available.  
> bizId | String | Product and trading-side identifier.  
`14`: SPOT MAKER  
`15`: FUT_NTO MAKER  
`16`: PERP MAKER  
`17`: SPOT TAKER  
`18`: FUT_NTO TAKER  
`19`: PERP TAKER  
> program | String | GLP program name.  
`GLP_A`  
`GLP_B`  
> side | String | Trading side.  
`MAKER`  
`TAKER`  
> instrument | String | GLP product category.  
`SPOT`: Spot trading  
`PERP`: Perpetuals  
`FUT_NTO`: Expiry Futures and Nitro  
> currentTier | String | GLP tier currently in effect. Empty string when unavailable.  
> estNextTier | String | Estimated GLP tier based on latest assessment. Empty string when unavailable.  
> estNextStatus | String | Estimated tier outcome.  
`disqualify`  
`downgrade`  
`qualify`  
`upgrade`  
Empty string when unavailable.  
> gracePeriodEndTime | String | Earliest date on which a downgrade can take effect. Unix timestamp in milliseconds. Empty string when not applicable.  
> requirement | Array of objects | Market-share thresholds for GLP tiers.  
>> tier | String | GLP tier name.  
>> share | String | Required market share as a decimal fraction. GLP-A thresholds are unadjusted share; GLP-B Spot / Perpetual thresholds are adjusted share. `"0.007"` = 0.7%. `null` when unavailable.  
> performance | Array of objects | Week-to-date performance by trading date.  
>> date | String | Trading date. Unix timestamp in milliseconds.  
>> assessPeriod | String | Assessment period containing this trading date.  
`PREVIOUS`  
`CURRENT`  
>> share | String | Week-to-date market share as a decimal fraction. `null` when unavailable.  
>> vol | String | Week-to-date trading volume. `null` when unavailable.  
  
### Get GLP v2 assessment details

Retrieve daily and week-to-date GLP-A / GLP-B performance for the selected product and trading side within the current assessment week. A sub-account API key retrieves the master account's data.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/users/glp/v2/details`

> Request Example
    
    
    GET /api/v5/users/glp/v2/details?bizId=16
    

#### Request Parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
bizId | String | Yes | Product and trading-side identifier.  
`14`: SPOT MAKER  
`15`: FUT_NTO MAKER  
`16`: PERP MAKER  
`17`: SPOT TAKER  
`18`: FUT_NTO TAKER  
`19`: PERP TAKER  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "assessStartTime": "1726790400000",
                "assessEndTime": "1727308800000",
                "performance": [
                    {
                        "date": "1726790400000",
                        "origVol": "100",
                        "origShare": "0.004",
                        "adjVol": "200",
                        "adjShare": "0.004",
                        "accOrigVol": "100",
                        "accOrigShare": "0.004",
                        "accAdjVol": "200",
                        "accAdjShare": "0.004"
                    },
                    {
                        "date": "1726876800000",
                        "origVol": "200",
                        "origShare": "0.004",
                        "adjVol": "400",
                        "adjShare": "0.004",
                        "accOrigVol": "300",
                        "accOrigShare": "0.004",
                        "accAdjVol": "600",
                        "accAdjShare": "0.004"
                    }
                ]
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
assessStartTime | String | Start of the assessment period. Unix timestamp in milliseconds.  
assessEndTime | String | End of the assessment period. Unix timestamp in milliseconds.  
performance | Array of objects | Daily and week-to-date performance. Empty array when no data available.  
> date | String | Trading date. Unix timestamp in milliseconds.  
> origVol | String | Daily unadjusted trading volume. Used for GLP-A and for Expiry Futures & Nitro. `null` when unavailable.  
> origShare | String | Daily unadjusted market share as a decimal fraction. Used for GLP-A and for Expiry Futures & Nitro. `null` when unavailable.  
> adjVol | String | Daily weighted Type B trading volume. Used for GLP-B Spot / Perpetuals. `null` when unavailable.  
> adjShare | String | Daily adjusted share as a decimal fraction. Used for GLP-B Spot / Perpetuals. Adjusted share = weighted Type B volume ÷ (platform Type B pool volume − GLP-A Tier 1 participants' volume in that pool). `null` when unavailable.  
> accOrigVol | String | Week-to-date trading volume before weighting. `null` when unavailable.  
> accOrigShare | String | Week-to-date market share as a decimal fraction. `null` when unavailable.  
> accAdjVol | String | Adjusted week-to-date trading volume. `null` when unavailable.  
> accAdjShare | String | Adjusted week-to-date market share as a decimal fraction. `null` when unavailable.  
  
### Get GLP v2 performance history

Retrieve weekly GLP-A / GLP-B assessment results, tier outcomes and performance for the selected product and trading side. A sub-account API key retrieves the master account's data.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/users/glp/v2/history/performance`

> Request Example
    
    
    GET /api/v5/users/glp/v2/history/performance?bizId=16
    

#### Request Parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
bizId | String | Yes | Product and trading-side identifier.  
`14`: SPOT MAKER  
`15`: FUT_NTO MAKER  
`16`: PERP MAKER  
`17`: SPOT TAKER  
`18`: FUT_NTO TAKER  
`19`: PERP TAKER  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "performance": [
                    {
                        "assessStartTime": "1726185600000",
                        "assessEndTime": "1726704000000",
                        "tier": "Tier 3",
                        "nextTier": "Tier 2",
                        "accOrigVol": "100000",
                        "accOrigShare": "0.004",
                        "accAdjVol": "200000",
                        "accAdjShare": "0.004",
                        "assessResult": "upgrade"
                    }
                ]
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
performance | Array of objects | Weekly assessment results. Empty array when no history available.  
> assessStartTime | String | Start of the assessment period. Unix timestamp in milliseconds.  
> assessEndTime | String | End of the assessment period. Unix timestamp in milliseconds.  
> tier | String | GLP tier used for this assessment.  
> nextTier | String | Tier determined by this assessment. Empty string when unavailable.  
> accOrigVol | String | Trading volume for the assessment period before weighting. `null` when unavailable.  
> accOrigShare | String | Market share for the assessment period as a decimal fraction. `null` when unavailable.  
> accAdjVol | String | Adjusted trading volume for the assessment period. `null` when unavailable.  
> accAdjShare | String | Adjusted market share for the assessment period as a decimal fraction. `null` when unavailable.  
> assessResult | String | Tier outcome.  
`disqualify`  
`downgrade`  
`qualify`  
`upgrade`  
Empty string when unavailable.  
  
## GLP-C

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

## Deprecated

### Get GLP today performance

**Deprecated.** This endpoint returns results of the previous monthly GLP assessment and is no longer maintained. Data covers assessments before September 2026 only. Use Get GLP v2 overview / assessment details / performance history for current GLP-A / GLP-B weekly assessment results.

Retrieve the current day and month-to-date (MTD) GLP performance snapshot for the authenticated account, covering all enrolled programs (Spot / Perp / Expiry & Nitro). No request parameters; the account is resolved from the API key. Only enrolled GLP market maker accounts can access this endpoint; sub-accounts resolve to their master account.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/users/glp/todayperformance`

> Request Example
    
    
    GET /api/v5/users/glp/todayperformance
    

#### Request Parameters

None. The account is resolved from the authenticated session.

> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "dataReady": true,
                "dataDate": "2026-07-13",
                "account": {
                    "masterAccountId": "832545488879789797",
                    "combinedAccountIds": ["832545488879789798"]
                },
                "programs": [
                    {
                        "program": "SPOT",
                        "marketMakerBusinessId": "1",
                        "enrollmentStatus": "ENROLLED",
                        "marketMakerLevelId": "42",
                        "enrolledTierDisplay": "Tier 1 Class A",
                        "qualifyingPool": "TYPE_A",
                        "qualifyingRows": ["TOTAL"],
                        "daily": {
                            "volume": {
                                "typeA": {"maker": "1000000.00", "taker": "1000000.00"},
                                "typeBTotal": {"maker": "1000000.00", "taker": "1000000.00"},
                                "tradfiX2": {"maker": "1000000.00", "taker": "1000000.00"},
                                "total": {"maker": "2000000.00", "taker": "2000000.00"}
                            },
                            "share": {
                                "typeA": {"maker": "0.0000", "taker": "0.0000"},
                                "typeBAdj": {"maker": "0.0000", "taker": "0.0000"},
                                "total": {"maker": "0.0000", "taker": "0.0000"}
                            }
                        },
                        "mtd": {
                            "volume": {
                                "typeA": {"maker": "30000000.00", "taker": "30000000.00"},
                                "typeBTotal": {"maker": "30000000.00", "taker": "30000000.00"},
                                "tradfiX2": {"maker": "30000000.00", "taker": "30000000.00"},
                                "total": {"maker": "60000000.00", "taker": "60000000.00"}
                            },
                            "share": {
                                "typeA": {"maker": "0.0000", "taker": "0.0000"},
                                "typeBAdj": {"maker": "0.0000", "taker": "0.0000"},
                                "total": {"maker": "0.0000", "taker": "0.0000"}
                            },
                            "mtdStatus": "QUALIFIED",
                            "qualifyingShare": {"maker": "0.0000", "taker": "0.0000"}
                        }
                    }
                ]
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
dataReady | Boolean | Whether data is available for the `dataDate`. When `false`, `programs` is an empty array  
dataDate | String | Data snapshot date in `yyyy-MM-dd` format (UTC+8). Typically T-1; falls back to T-2 when T-1 computation is incomplete  
account | Object | Account identity block  
> masterAccountId | String | Master account ID  
> combinedAccountIds | Array of strings | Sibling account IDs in the same institutional group (excludes self). Empty array if no group  
programs | Array of objects | Performance data for each enrolled GLP program. Empty when `dataReady` is `false`  
> program | String | GLP business line identifier.  
`SPOT`  
`PERP`  
`FUT_NTO`: Expiry & Nitro  
> marketMakerBusinessId | String | Market maker business ID for this program  
> enrollmentStatus | String | Enrollment status. Currently always `ENROLLED`  
> marketMakerLevelId | String | Current tier level ID  
> enrolledTierDisplay | String | Current tier display name, e.g. `Tier 1 Class A`  
> qualifyingPool | String | Pool that determines current tier.  
`TYPE_A`  
`TYPE_B_ADJ`  
`TYPE_A_AND_B`  
> qualifyingRows | Array of strings | Keys of qualifying rows for UI highlighting, e.g. `["TOTAL"]`  
> daily | Object | Today's performance metrics. Contains `volume` and `share` (see structure below)  
> mtd | Object | Month-to-date performance metrics. Contains `volume`, `share` (same structure as `daily`), plus the additional fields below  
>> mtdStatus | String | MTD qualification status.  
`QUALIFIED`  
`UPGRADE`  
`DOWNGRADE`  
>> qualifyingShare | Object | Share in the qualifying pool. Contains `maker` (String) and `taker` (String)  
  
**Volume and share structure**

Both `daily` and `mtd` contain a `volume` Object and a `share` Object. Each Object holds category keys, and each category is itself an Object with `maker` (String) and `taker` (String) fields.

**Category** | **In`volume`** | **In`share`** | **Description**  
---|---|---|---  
typeA | Yes | Yes | Type A. `null` for `FUT_NTO`  
typeBTotal | Yes | No | Type B total. `null` for `FUT_NTO`  
typeBAdj | No | Yes | Type B adjusted. `null` for `FUT_NTO`  
tradfiX2 | Yes | No | TradFi volume doubled. `null` for `FUT_NTO`  
total | Yes | Yes | Total across all types. Always present  
  
  * **`volume`** values: USD notional as String with 2 decimal places (e.g. `"1000000.00"`)
  * **`share`** values: decimal string with 4 decimal places, no `%` suffix (e.g. `"0.0012"`)

### Get GLP historical performance

**Deprecated.** This endpoint returns results of the previous monthly GLP assessment and is no longer maintained. Data covers assessments before September 2026 only. Use Get GLP v2 overview / assessment details / performance history for current GLP-A / GLP-B weekly assessment results.

Retrieve daily GLP performance history for a single program. Results are sorted newest-first (descending by date). Only enrolled GLP market maker accounts can access this endpoint; sub-accounts resolve to their master account.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/users/glp/historicalperformance`

> Request Example
    
    
    GET /api/v5/users/glp/historicalperformance?program=SPOT
    GET /api/v5/users/glp/historicalperformance?program=SPOT&begin=1751299200000&end=1753804800000&limit=31
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
program | String | Yes | GLP business line identifier.  
`SPOT`  
`PERP`  
`FUT_NTO`  
begin | String | No | Begin date filter (inclusive). Unix ms String, e.g. `"1751299200000"`. Default: first day of current month (UTC+8)  
end | String | No | End date filter (inclusive). Unix ms String. Default: today (UTC+8)  
limit | String | No | Max records per page. Default `"31"`, max `"100"`  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "date": "2026-07-13",
                "volume": {
                    "typeA": {"maker": "1000000.00", "taker": "1000000.00"},
                    "typeBTotal": {"maker": "1000000.00", "taker": "1000000.00"},
                    "tradfiX2": {"maker": "1000000.00", "taker": "1000000.00"},
                    "total": {"maker": "2000000.00", "taker": "2000000.00"}
                },
                "share": {
                    "typeA": {"maker": "0.0012", "taker": "0.0010"},
                    "typeBAdj": {"maker": "0.0008", "taker": "0.0007"},
                    "total": {"maker": "0.0010", "taker": "0.0009"}
                }
            },
            {
                "date": "2026-07-12",
                "volume": {
                    "typeA": {"maker": "950000.00", "taker": "980000.00"},
                    "typeBTotal": {"maker": "850000.00", "taker": "900000.00"},
                    "tradfiX2": {"maker": "800000.00", "taker": "820000.00"},
                    "total": {"maker": "1800000.00", "taker": "1880000.00"}
                },
                "share": {
                    "typeA": {"maker": "0.0011", "taker": "0.0009"},
                    "typeBAdj": {"maker": "0.0007", "taker": "0.0006"},
                    "total": {"maker": "0.0009", "taker": "0.0008"}
                }
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
date | String | Date in `yyyy-MM-dd` format (UTC+8)  
volume | Object | Trading volume by pool type (USD notional, 2 decimal places). Same structure as the today performance endpoint's `daily.volume`  
share | Object | Market share by pool type (decimal string, 4 decimal places, no `%` suffix). Same structure as the today performance endpoint's `daily.share`

---

# Global Liquidity Program

## 介绍 

OKX 全球流动性计划（GLP）根据交易或报价表现，为符合条件的做市商提供费率优惠。

  * **GLP-A** ：Type A（头部）交易对。按未加权的交易市场份额进行周度考核，Maker 和 Taker 分开考核。权益为 VIP 9 + Colo。
  * **GLP-B** ：Type B 交易对（大多数其他交易对）。按调整后的交易市场份额进行周度考核，Maker 和 Taker 分开考核。权益为 VIP 6–9，VIP 9 可享 Colo。交割合约和 Nitro Spreads 不区分交易对类型，所有交易对一起按未加权份额考核。
  * **GLP-C** ：流动性激励交易对（现货和永续合约）。按双边加权报价份额进行小时考核，从下一小时起享受 VIP 6–9 Maker 费率。

参与者须满足 AUM 和原生 VIP 等级要求，详情参见 [OKX 流动性计划页面](https://www.okx.com/fees/liquidity-program)。同时适用多个计划时，采用最优惠的费率。计划参与者不享受其他 VIP 相关或交易量相关的优惠活动或返佣。

本节用户接口仅限已报名账户调用。子账户 API key 返回主账户的数据。

[计划详情](https://www.okx.com/help/introducing-the-okx-global-liquidity-program) · [GLP 工作台](https://www.okx.com/glp-workspace) · 如需申请，请联系客户经理或发送邮件至 `institutional@okx.com`。

**通用错误码**

错误码 | HTTP 状态码 | 错误提示  
---|---|---  
50001 | 503 | 服务暂时不可用，请稍后重试  
50014 | 200 | 参数 {param0} 不能为空  
50016 | 200 | 参数 {param0} 与参数 {param1} 不匹配  
50026 | 500 | 系统错误，请稍后重试  
50030 | 200 | 您无权使用此 API 端点  
51000 | 200 | 参数错误  
  
## GLP-A / GLP-B 

### 获取 GLP 币对分类类型 

获取 SPOT 和 SWAP 产品的 GLP-A / GLP-B 分类，用于查询产品所属的考核计划及考核池。交割合约和 Nitro Spreads 不区分交易对类型，所有交易对一起考核。GLP-C 产品请参见获取 GLP-C 可参与产品。分类及交易量权重仅供参考，以 OKX 官网和计划手册为准。

#### 限速：每2秒5次请求

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/public/mm-instrument-types`

> 请求示例
    
    
    GET /api/v5/public/mm-instrument-types?instType=SWAP
    
    
    
    import okx.PublicData as PublicData
    
    flag = "0"  # 实盘:0 , 模拟盘：1
    
    publicDataAPI = PublicData.PublicAPI(flag=flag)
    
    # 获取 GLP 币对分类类型
    result = publicDataAPI.get_mm_instrument_types(
        instType="SWAP"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 否 | 产品类型  
`SPOT`  
`SWAP`  
未指定时返回全部类型  
instId | String | 否 | 产品ID，如 `BTC-USDT`、`BTC-USDT-SWAP`  
指定时返回至多一条记录  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "instId": "BTC-USDT-SWAP",
                "instType": "SWAP",
                "pairType": "A"
            },
            {
                "instId": "ETH-USDT-SWAP",
                "instType": "SWAP",
                "pairType": "A"
            },
            {
                "instId": "XAU-USDT-SWAP",
                "instType": "SWAP",
                "pairType": "B-TradFi"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
instId | String | 产品ID，如 `BTC-USDT-SWAP`  
instType | String | 产品类型  
`SPOT`  
`SWAP`  
pairType | String | GLP-A / GLP-B 分类类型。  
`A`：Type A 交易对，按 GLP-A 未加权份额考核  
`B-Crypto`：Type B 加密交易对，按 GLP-B 考核，交易量权重 1×  
`B-TradFi`：Type B 传统金融交易对（现货和永续合约），按 GLP-B 考核，交易量权重 2×  
`Type Special`：GLP 特殊交易对，按 GLP-B 考核，交易量权重 4×  
  
### 获取 GLP v2 概览 

获取当前鉴权账户有效的 GLP-A / GLP-B 报名信息、当前等级、下一期预估等级、等级要求及本周累计表现。子账户 API key 返回主账户的数据。

周度考核：升级于周二 00:00（UTC+8）生效，降级于周三 00:00（UTC+8）生效。`gracePeriodEndTime` 为最早可降级时间。

#### 限速：5次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/users/glp/v2/overview`

> 请求示例
    
    
    GET /api/v5/users/glp/v2/overview
    

#### 请求参数

无请求参数。

> 返回示例
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "programs": [
                    {
                        "bizId": "16",
                        "program": "GLP_B",
                        "side": "MAKER",
                        "instrument": "PERP",
                        "currentTier": "Tier 2",
                        "estNextTier": "Tier 2",
                        "estNextStatus": "qualify",
                        "gracePeriodEndTime": "",
                        "requirement": [
                            {
                                "tier": "Tier 1",
                                "share": "0.005"
                            },
                            {
                                "tier": "Tier 2",
                                "share": "0.003"
                            }
                        ],
                        "performance": [
                            {
                                "date": "1726531200000",
                                "assessPeriod": "PREVIOUS",
                                "share": "0.0035",
                                "vol": "140000"
                            },
                            {
                                "date": "1726876800000",
                                "assessPeriod": "CURRENT",
                                "share": "0.004",
                                "vol": "200"
                            }
                        ]
                    }
                ]
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
programs | Array of objects | 当前 GLP 注册信息。无可用数据时返回空数组。  
> bizId | String | 产品及交易方向标识。  
`14`：SPOT MAKER  
`15`：FUT_NTO MAKER  
`16`：PERP MAKER  
`17`：SPOT TAKER  
`18`：FUT_NTO TAKER  
`19`：PERP TAKER  
> program | String | GLP 项目名称。  
`GLP_A`  
`GLP_B`  
> side | String | 交易方向。  
`MAKER`  
`TAKER`  
> instrument | String | GLP 产品类别。  
`SPOT`：现货  
`PERP`：永续合约  
`FUT_NTO`：交割合约及 Nitro  
> currentTier | String | 当前生效的 GLP 等级。不可用时返回空字符串。  
> estNextTier | String | 基于最新考核的预估 GLP 等级。不可用时返回空字符串。  
> estNextStatus | String | 预估等级结果。  
`disqualify`  
`downgrade`  
`qualify`  
`upgrade`  
不可用时返回空字符串。  
> gracePeriodEndTime | String | 降级最早生效日期。Unix 毫秒时间戳。不适用时返回空字符串。  
> requirement | Array of objects | GLP 等级的市场份额门槛。  
>> tier | String | GLP 等级名称。  
>> share | String | 所需市场份额，以小数表示。GLP-A 门槛为未加权份额；GLP-B 现货和永续合约门槛为调整后的份额。`"0.007"` = 0.7%。不可用时为 `null`。  
> performance | Array of objects | 按交易日统计的本周绩效。  
>> date | String | 交易日。Unix 毫秒时间戳。  
>> assessPeriod | String | 该交易日所属的考核周期。  
`PREVIOUS`  
`CURRENT`  
>> share | String | 本周市场份额，以小数表示。不可用时为 `null`。  
>> vol | String | 本周交易量。不可用时为 `null`。  
  
### 获取 GLP v2 考核详情 

获取所选产品及交易方向在当前考核周内的 GLP-A / GLP-B 每日和本周累计表现。子账户 API key 返回主账户的数据。

#### 限速：5次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/users/glp/v2/details`

> 请求示例
    
    
    GET /api/v5/users/glp/v2/details?bizId=16
    

#### 请求参数

**参数名** | **类型** | **是否必须** | **描述**  
---|---|---|---  
bizId | String | 是 | 产品及交易方向标识。  
`14`：SPOT MAKER  
`15`：FUT_NTO MAKER  
`16`：PERP MAKER  
`17`：SPOT TAKER  
`18`：FUT_NTO TAKER  
`19`：PERP TAKER  
  
> 返回示例
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "assessStartTime": "1726790400000",
                "assessEndTime": "1727308800000",
                "performance": [
                    {
                        "date": "1726790400000",
                        "origVol": "100",
                        "origShare": "0.004",
                        "adjVol": "200",
                        "adjShare": "0.004",
                        "accOrigVol": "100",
                        "accOrigShare": "0.004",
                        "accAdjVol": "200",
                        "accAdjShare": "0.004"
                    },
                    {
                        "date": "1726876800000",
                        "origVol": "200",
                        "origShare": "0.004",
                        "adjVol": "400",
                        "adjShare": "0.004",
                        "accOrigVol": "300",
                        "accOrigShare": "0.004",
                        "accAdjVol": "600",
                        "accAdjShare": "0.004"
                    }
                ]
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
assessStartTime | String | 考核周期开始时间。Unix 毫秒时间戳。  
assessEndTime | String | 考核周期结束时间。Unix 毫秒时间戳。  
performance | Array of objects | 每日及本周绩效。无可用数据时返回空数组。  
> date | String | 交易日。Unix 毫秒时间戳。  
> origVol | String | 每日未加权交易量，用于 GLP-A 以及交割合约和 Nitro。不可用时为 `null`。  
> origShare | String | 每日未加权市场份额，以小数表示，用于 GLP-A 以及交割合约和 Nitro。不可用时为 `null`。  
> adjVol | String | 每日加权 Type B 交易量，用于 GLP-B 现货和永续合约。不可用时为 `null`。  
> adjShare | String | 每日调整后的份额，以小数表示，用于 GLP-B 现货和永续合约。调整后份额 = 加权 Type B 交易量 ÷（平台 Type B 池交易量 − GLP-A Tier 1 参与者在该池的交易量）。不可用时为 `null`。  
> accOrigVol | String | 加权前的本周累计交易量。不可用时为 `null`。  
> accOrigShare | String | 本周累计市场份额，以小数表示。不可用时为 `null`。  
> accAdjVol | String | 调整后的本周累计交易量。不可用时为 `null`。  
> accAdjShare | String | 调整后的本周累计市场份额，以小数表示。不可用时为 `null`。  
  
### 获取 GLP v2 历史绩效 

获取所选产品及交易方向的 GLP-A / GLP-B 周度考核结果、等级结果和表现。子账户 API key 返回主账户的数据。

#### 限速：5次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/users/glp/v2/history/performance`

> 请求示例
    
    
    GET /api/v5/users/glp/v2/history/performance?bizId=16
    

#### 请求参数

**参数名** | **类型** | **是否必须** | **描述**  
---|---|---|---  
bizId | String | 是 | 产品及交易方向标识。  
`14`：SPOT MAKER  
`15`：FUT_NTO MAKER  
`16`：PERP MAKER  
`17`：SPOT TAKER  
`18`：FUT_NTO TAKER  
`19`：PERP TAKER  
  
> 返回示例
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "performance": [
                    {
                        "assessStartTime": "1726185600000",
                        "assessEndTime": "1726704000000",
                        "tier": "Tier 3",
                        "nextTier": "Tier 2",
                        "accOrigVol": "100000",
                        "accOrigShare": "0.004",
                        "accAdjVol": "200000",
                        "accAdjShare": "0.004",
                        "assessResult": "upgrade"
                    }
                ]
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
performance | Array of objects | 每周考核结果。无历史数据时返回空数组。  
> assessStartTime | String | 考核周期开始时间。Unix 毫秒时间戳。  
> assessEndTime | String | 考核周期结束时间。Unix 毫秒时间戳。  
> tier | String | 本次考核使用的 GLP 等级。  
> nextTier | String | 本次考核确定的等级。不可用时返回空字符串。  
> accOrigVol | String | 考核周期内加权前的交易量。不可用时为 `null`。  
> accOrigShare | String | 考核周期内市场份额，以小数表示。不可用时为 `null`。  
> accAdjVol | String | 考核周期内调整后的交易量。不可用时为 `null`。  
> accAdjShare | String | 考核周期内调整后的市场份额，以小数表示。不可用时为 `null`。  
> assessResult | String | 等级变更结果。  
`disqualify`  
`downgrade`  
`qualify`  
`upgrade`  
不可用时返回空字符串。  
  
## GLP-C 

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

## Deprecated 

### 获取 GLP 当日表现 

**Deprecated（已弃用）。** 本接口返回旧版 GLP 月度考核结果，不再维护。数据仅覆盖 2026 年 9 月之前的考核。当前 GLP-A / GLP-B 周度考核结果请使用获取 GLP v2 概览 / 考核详情 / 历史绩效接口。

获取当前账户在所有已加入 GLP 业务线（Spot / Perp / Expiry & Nitro）的当日和月度累计（MTD）表现快照。无需请求参数，账户由 API key 自动解析。仅已加入且在有效期的 GLP 做市商账户可调用；子账户解析到其 master account。

#### 限速：5次/2s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/users/glp/todayperformance`

> 请求示例
    
    
    GET /api/v5/users/glp/todayperformance
    

#### 请求参数

无。账户由登录态自动解析。

> 返回示例
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "dataReady": true,
                "dataDate": "2026-07-13",
                "account": {
                    "masterAccountId": "832545488879789797",
                    "combinedAccountIds": ["832545488879789798"]
                },
                "programs": [
                    {
                        "program": "SPOT",
                        "marketMakerBusinessId": "1",
                        "enrollmentStatus": "ENROLLED",
                        "marketMakerLevelId": "42",
                        "enrolledTierDisplay": "Tier 1 Class A",
                        "qualifyingPool": "TYPE_A",
                        "qualifyingRows": ["TOTAL"],
                        "daily": {
                            "volume": {
                                "typeA": {"maker": "1000000.00", "taker": "1000000.00"},
                                "typeBTotal": {"maker": "1000000.00", "taker": "1000000.00"},
                                "tradfiX2": {"maker": "1000000.00", "taker": "1000000.00"},
                                "total": {"maker": "2000000.00", "taker": "2000000.00"}
                            },
                            "share": {
                                "typeA": {"maker": "0.0000", "taker": "0.0000"},
                                "typeBAdj": {"maker": "0.0000", "taker": "0.0000"},
                                "total": {"maker": "0.0000", "taker": "0.0000"}
                            }
                        },
                        "mtd": {
                            "volume": {
                                "typeA": {"maker": "30000000.00", "taker": "30000000.00"},
                                "typeBTotal": {"maker": "30000000.00", "taker": "30000000.00"},
                                "tradfiX2": {"maker": "30000000.00", "taker": "30000000.00"},
                                "total": {"maker": "60000000.00", "taker": "60000000.00"}
                            },
                            "share": {
                                "typeA": {"maker": "0.0000", "taker": "0.0000"},
                                "typeBAdj": {"maker": "0.0000", "taker": "0.0000"},
                                "total": {"maker": "0.0000", "taker": "0.0000"}
                            },
                            "mtdStatus": "QUALIFIED",
                            "qualifyingShare": {"maker": "0.0000", "taker": "0.0000"}
                        }
                    }
                ]
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
dataReady | Boolean | 该 `dataDate` 是否已有数据。为 `false` 时 `programs` 为空数组  
dataDate | String | 数据快照日期，`yyyy-MM-dd` 格式（UTC+8）。通常为 T-1；T-1 计算未完成时回退 T-2  
account | Object | 账户身份信息  
> masterAccountId | String | master account ID  
> combinedAccountIds | Array of strings | 同机构组的兄弟账户 ID（不含自己）。无组则为空数组  
programs | Array of objects | 各已加入 GLP 业务线的表现数据。`dataReady` 为 `false` 时为空数组  
> program | String | GLP 业务线标识。  
`SPOT`：现货  
`PERP`：永续合约  
`FUT_NTO`：交割合约 & Nitro  
> marketMakerBusinessId | String | 该业务线的做市商 business ID  
> enrollmentStatus | String | 加入状态。当前恒为 `ENROLLED`  
> marketMakerLevelId | String | 当前档位 ID  
> enrolledTierDisplay | String | 当前档位展示名，如 `Tier 1 Class A`  
> qualifyingPool | String | 决定当前档位的池。  
`TYPE_A`  
`TYPE_B_ADJ`  
`TYPE_A_AND_B`  
> qualifyingRows | Array of strings | 合格行 key，如 `["TOTAL"]`  
> daily | Object | 当日表现快照。包含 `volume` 和 `share`（结构见下方说明）  
> mtd | Object | 月度累计表现。包含 `volume`、`share`（同 `daily` 结构），以及以下额外字段  
>> mtdStatus | String | MTD 档位状态。  
`QUALIFIED`：达标  
`UPGRADE`：升档  
`DOWNGRADE`：降档  
>> qualifyingShare | Object | 决定档位的池的份额。包含 `maker`（String）和 `taker`（String）  
  
**交易量和份额结构**

`daily` 和 `mtd` 均包含 `volume`（交易量）和 `share`（份额）两个 Object。每个 Object 下含分类 key，每个分类为包含 `maker`（String）和 `taker`（String）字段的 Object。

**分类** | **在`volume` 中** | **在`share` 中** | **描述**  
---|---|---|---  
typeA | 是 | 是 | Type A。`FUT_NTO` 时为 `null`  
typeBTotal | 是 | 否 | Type B 合计。`FUT_NTO` 时为 `null`  
typeBAdj | 否 | 是 | Type B 调整后。`FUT_NTO` 时为 `null`  
tradfiX2 | 是 | 否 | TradFi 量（已 ×2）。`FUT_NTO` 时为 `null`  
total | 是 | 是 | 各类型合计。始终存在  
  
  * **`volume`** 值：美元名义量，String，保留 2 位小数（如 `"1000000.00"`）
  * **`share`** 值：小数字符串，4 位小数，无 `%` 后缀（如 `"0.0012"`）

### 获取 GLP 历史表现 

**Deprecated（已弃用）。** 本接口返回旧版 GLP 月度考核结果，不再维护。数据仅覆盖 2026 年 9 月之前的考核。当前 GLP-A / GLP-B 周度考核结果请使用获取 GLP v2 概览 / 考核详情 / 历史绩效接口。

获取单个 GLP 业务线的逐日表现记录，按日期降序排列（最新日期在前）。仅已加入且在有效期的 GLP 做市商账户可调用；子账户解析到其 master account。

#### 限速：5次/2s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/users/glp/historicalperformance`

> 请求示例
    
    
    GET /api/v5/users/glp/historicalperformance?program=SPOT
    GET /api/v5/users/glp/historicalperformance?program=SPOT&begin=1751299200000&end=1753804800000&limit=31
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
program | String | 是 | GLP 业务线标识。  
`SPOT`  
`PERP`  
`FUT_NTO`  
begin | String | 否 | 开始日期过滤（含）。Unix 毫秒字符串，如 `"1751299200000"`。默认：当月 1 号（UTC+8）  
end | String | 否 | 结束日期过滤（含）。Unix 毫秒字符串。默认：今天（UTC+8）  
limit | String | 否 | 每页最大记录数。默认 `"31"`，最大 `"100"`  
  
> 返回示例
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "date": "2026-07-13",
                "volume": {
                    "typeA": {"maker": "1000000.00", "taker": "1000000.00"},
                    "typeBTotal": {"maker": "1000000.00", "taker": "1000000.00"},
                    "tradfiX2": {"maker": "1000000.00", "taker": "1000000.00"},
                    "total": {"maker": "2000000.00", "taker": "2000000.00"}
                },
                "share": {
                    "typeA": {"maker": "0.0012", "taker": "0.0010"},
                    "typeBAdj": {"maker": "0.0008", "taker": "0.0007"},
                    "total": {"maker": "0.0010", "taker": "0.0009"}
                }
            },
            {
                "date": "2026-07-12",
                "volume": {
                    "typeA": {"maker": "950000.00", "taker": "980000.00"},
                    "typeBTotal": {"maker": "850000.00", "taker": "900000.00"},
                    "tradfiX2": {"maker": "800000.00", "taker": "820000.00"},
                    "total": {"maker": "1800000.00", "taker": "1880000.00"}
                },
                "share": {
                    "typeA": {"maker": "0.0011", "taker": "0.0009"},
                    "typeBAdj": {"maker": "0.0007", "taker": "0.0006"},
                    "total": {"maker": "0.0009", "taker": "0.0008"}
                }
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
date | String | 日期，`yyyy-MM-dd` 格式（UTC+8）  
volume | Object | 各池类型的交易量（美元名义，2 位小数）。结构同当日表现接口的 `daily.volume`  
share | Object | 各池类型的市场份额（小数字符串，4 位小数，无 `%` 后缀）。结构同当日表现接口的 `daily.share`