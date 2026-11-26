---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#global-liquidity-program-deprecated-get-glp-today-performance
anchor_id: global-liquidity-program-deprecated-get-glp-today-performance
api_type: API
updated_at: 2026-11-26 19:00:30.504438
---

# Get GLP today performance

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

---

# 获取 GLP 当日表现

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