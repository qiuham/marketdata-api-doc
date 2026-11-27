---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#global-liquidity-program-glp-a-glp-b-get-glp-v2-assessment-details
anchor_id: global-liquidity-program-glp-a-glp-b-get-glp-v2-assessment-details
api_type: API
updated_at: 2026-11-27 18:59:29.216549
---

# Get GLP v2 assessment details

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

---

# 获取 GLP v2 考核详情

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