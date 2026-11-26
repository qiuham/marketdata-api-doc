---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#global-liquidity-program-glp-a-glp-b
anchor_id: global-liquidity-program-glp-a-glp-b
api_type: API
updated_at: 2026-11-26 19:00:30.206714
---

# GLP-A / GLP-B

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

---

# GLP-A / GLP-B

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