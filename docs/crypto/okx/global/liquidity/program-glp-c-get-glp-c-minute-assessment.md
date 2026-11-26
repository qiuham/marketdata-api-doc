---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#global-liquidity-program-glp-c-get-glp-c-minute-assessment
anchor_id: global-liquidity-program-glp-c-get-glp-c-minute-assessment
api_type: API
updated_at: 2026-11-26 19:00:30.362135
---

# Get GLP-C minute assessment

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

---

# 获取 GLP-C 分钟考核

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