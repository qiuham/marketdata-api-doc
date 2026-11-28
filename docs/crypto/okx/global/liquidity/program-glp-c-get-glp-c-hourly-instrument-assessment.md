---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#global-liquidity-program-glp-c-get-glp-c-hourly-instrument-assessment
anchor_id: global-liquidity-program-glp-c-get-glp-c-hourly-instrument-assessment
api_type: API
updated_at: 2026-11-28 18:57:22.984341
---

# Get GLP-C hourly instrument assessment

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

---

# 获取 GLP-C 产品小时考核

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