---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#global-liquidity-program-glp-a-glp-b-get-glp-v2-performance-history
anchor_id: global-liquidity-program-glp-a-glp-b-get-glp-v2-performance-history
api_type: API
updated_at: 2026-11-28 18:57:22.900750
---

# Get GLP v2 performance history

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

# 获取 GLP v2 历史绩效

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