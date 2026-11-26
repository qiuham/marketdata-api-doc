---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#global-liquidity-program-glp-a-glp-b-get-glp-v2-overview
anchor_id: global-liquidity-program-glp-a-glp-b-get-glp-v2-overview
api_type: API
updated_at: 2026-11-26 19:00:30.233099
---

# Get GLP v2 overview

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

---

# 获取 GLP v2 概览

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