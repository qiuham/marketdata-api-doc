---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#global-liquidity-program-deprecated-get-glp-historical-performance
anchor_id: global-liquidity-program-deprecated-get-glp-historical-performance
api_type: API
updated_at: 2026-11-27 18:59:29.422923
---

# Get GLP historical performance

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

# 获取 GLP 历史表现

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