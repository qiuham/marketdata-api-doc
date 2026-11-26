---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#global-liquidity-program-glp-c-get-glp-c-hourly-assessment-summary
anchor_id: global-liquidity-program-glp-c-get-glp-c-hourly-assessment-summary
api_type: API
updated_at: 2026-11-26 19:00:30.405418
---

# Get GLP-C hourly assessment summary

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

# 获取 GLP-C 小时考核汇总

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