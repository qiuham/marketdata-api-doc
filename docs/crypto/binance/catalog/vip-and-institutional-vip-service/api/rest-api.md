---
exchange: binance
source_url: https://developers.binance.com/en/docs/catalog/vip-and-institutional-vip-service/api/rest-api
api_type: REST
updated_at: 2026-11-22 18:46:18.759512
---

# VIP Service REST API

Schema: https://developers.binance.com/en/docs/catalog/vip-and-institutional-vip-service/api/rest-api/1.0.0/schema.yaml

Query VIP account configuration, fee tiers, rate limits, and commission settings via the VIP Service API.

通过 VIP Service API 查询 VIP 账户配置、费率等级、速率限制和佣金设置。

版本: 1.0.0

## 服务地址

- `https://api.binance.com`
- `https://api-gcp.binance.com`
- `https://api1.binance.com`
- `https://api2.binance.com`
- `https://api3.binance.com`
- `https://api4.binance.com`

## 接口列表

- `GET /sapi/v1/vip/vip-portal/futures/ip-whitelists` — Query Futures IP Whitelists
- `POST /sapi/v1/vip/vip-portal/futures/ip-whitelists` — Add Futures IP Whitelists
- `DELETE /sapi/v1/vip/vip-portal/futures/ip-whitelists` — Remove Futures IP Whitelists
- `GET /sapi/v1/vip/vip-portal/futures/rate-limits/ips` — Query Futures IP Rate Limits
- `GET /sapi/v1/vip/vip-portal/futures/rate-limits/ips/pages` — Query Futures IP Rate Limits With Pagination
- `GET /sapi/v1/vip/vip-portal/futures/rate-limits/orders` — Query Futures USER ORDER Rate Limits
- `GET /sapi/v1/vip/vip-portal/futures/rate-limits/orders/pages` — Query Futures USER ORDER Rate Limits With Pagination
- `GET /sapi/v1/vip/liquidity-programs/overview` — Query Liquidity Program Overview
- `GET /sapi/v1/vip/liquidity-programs/performance` — Query Liquidity Program Performance
- `GET /sapi/v1/vip/liquidity-programs/weekly-result` — Query Liquidity Program Weekly Results
- `GET /sapi/v1/commission/queryCommissionFee` — Query Symbol Commission Fee

## Query Futures IP Whitelists（查询合约IP白名单）

`GET /sapi/v1/vip/vip-portal/futures/ip-whitelists`

Query Futures IP Whitelists

- Query IP whitelist for each endpoint and connections count
- Please note that the connection -1 means the IP is being added to the whitelist, -2 means the IP is failed to update, the other values indicate the current live connections

查询合约IP白名单
- 查询每个端点的 IP 白名单和连接数
- 请注意，连接数 -1 表示 IP 正在添加到白名单，-2 表示 IP 更新失败，其他值表示当前活跃连接数

Operation ID: `queryFuturesIpWhitelists`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| recvWindow | query | integer (int64) |  | 例: `5000` |
| endpoint | query | string |  | 枚举: `FAPI-MM`, `FSTREAM-MM`<br>例: `FAPI-MM` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Futures IP Whitelists / 合约 IP 白名单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| status | string |  | 例: `OK` |
| type | string |  | 例: `GENERAL` |
| code | string |  | 例: `000000000` |
| data | object[] |  |  |
| data[].endpoint | string |  | 例: `FAPI-MM` |
| data[].totalConnectionQuota | integer (int64) |  | 例: `600` |
| data[].connectionCount | integer (int64) |  | 例: `200` |
| data[].ipLimit | integer (int64) |  | 例: `350` |
| data[].addIpCount | integer (int64) |  | 例: `200` |
| data[].ipConnections | object |  |  |
| data[].ipConnections.192.168.1.0 | integer (int64) |  | 0 means added successfully.<br>0 表示添加成功。<br>例: `0` |
| data[].ipConnections.192.168.1.1 | integer (int64) |  | -1 means in progress for update.<br>-1 表示正在更新中。<br>例: `-1` |
| data[].ipConnections.192.168.1.2 | integer (int64) |  | -2 means update failed.<br>-2 表示更新失败。<br>例: `-2` |
| data[].ipConnections.192.168.1.3 | integer (int64) |  | 例: `10` |

## Add Futures IP Whitelists（添加合约IP白名单）

`POST /sapi/v1/vip/vip-portal/futures/ip-whitelists`

Add IP(s) to FAPI-MM or FSTREAM-MM whitelist endpoints

将 IP 添加到 FAPI-MM 或 FSTREAM-MM 白名单

Operation ID: `addFuturesIpWhitelists`

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| recvWindow | integer (int64) |  | 例: `5000` |
| endpoint | string | 是 | 枚举: `FAPI-MM`, `FSTREAM-MM`<br>例: `FAPI-MM` |
| ipAddresses | string[] | 是 |  |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Add Futures IP Whitelists / 添加合约 IP 白名单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| status | string |  | 例: `OK` |
| type | string |  | 例: `GENERAL` |
| code | string |  | 例: `000000000` |

## Remove Futures IP Whitelists（移除合约IP白名单）

`DELETE /sapi/v1/vip/vip-portal/futures/ip-whitelists`

Remove IP(s) to FAPI-MM or FSTREAM-MM whitelist endpoints

将 IP 从 FAPI-MM 或 FSTREAM-MM 白名单中移除

Operation ID: `removeFuturesIpWhitelists`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| recvWindow | query | integer (int64) |  | 例: `5000` |
| endpoint | query | string | 是 | 枚举: `FAPI-MM`, `FSTREAM-MM`<br>例: `FAPI-MM` |
| ipAddresses | query | string[] | 是 |  |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Remove Futures IP Whitelists / 移除合约 IP 白名单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| status | string |  | 例: `OK` |
| type | string |  | 例: `GENERAL` |
| code | string |  | 例: `000000000` |

## Query Futures IP Rate Limits（查询期货IP速率限制）

`GET /sapi/v1/vip/vip-portal/futures/rate-limits/ips`

Query Futures IP Rate Limits

查询期货IP速率限制

Operation ID: `queryFuturesIpRateLimits`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| recvWindow | query | integer (int64) |  | 例: `5000` |
| productType | query | string | 是 | 枚举: `CM`, `UM`<br>例: `CM` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Futures IP Rate Limits / 合约 IP 速率限制

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| status | string |  | 例: `OK` |
| type | string |  | 例: `GENERAL` |
| code | string |  | 例: `000000000` |
| data | object[] |  |  |
| data[].ipAddress | string |  | 例: `192.168.1.1` |
| data[].limit | integer (int64) |  | 例: `2400` |

## Query Futures IP Rate Limits With Pagination（使用分页查询期货 IP 速率限制）

`GET /sapi/v1/vip/vip-portal/futures/rate-limits/ips/pages`

Query Futures IP Rate Limits With Pagination

使用分页查询期货 IP 速率限制

Operation ID: `queryFuturesIpRateLimitsWithPagination`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| recvWindow | query | integer (int64) |  | 例: `5000` |
| productType | query | string | 是 | 枚举: `CM`, `UM`<br>例: `CM` |
| pageIndex | query | integer (int64) | 是 | 例: `1` |
| pageSize | query | integer (int64) | 是 | 例: `1` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Futures IP Rate Limits With Pagination / 分页查询合约 IP 速率限制

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| status | string |  | 例: `OK` |
| type | string |  | 例: `GENERAL` |
| code | string |  | 例: `000000000` |
| data | object |  |  |
| data.total | integer (int64) |  | 例: `100` |
| data.rows | object[] |  |  |
| data.rows[].ipAddress | string |  | 例: `192.168.1.1` |
| data.rows[].limit | integer (int64) |  | 例: `2400` |

## Query Futures USER ORDER Rate Limits（查询合约用户订单速率限制）

`GET /sapi/v1/vip/vip-portal/futures/rate-limits/orders`

Query Futures USER ORDER Rate Limits

查询合约用户订单速率限制

Operation ID: `queryFuturesUserorderRateLimits`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| recvWindow | query | integer (int64) |  | 例: `5000` |
| productType | query | string | 是 | 枚举: `CM`, `UM`<br>例: `CM` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Futures USER ORDER Rate Limits / 合约用户订单速率限制

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| status | string |  | 例: `OK` |
| type | string |  | 例: `GENERAL` |
| code | string |  | 例: `000000000` |
| data | object[] |  |  |
| data[].userId | integer (int64) |  | 例: `1000001` |
| data[].userEmail | string |  | 例: `user@email.com` |
| data[].limit | integer (int64) |  | 例: `1200` |

## Query Futures USER ORDER Rate Limits With Pagination（分页查询合约用户订单速率限制）

`GET /sapi/v1/vip/vip-portal/futures/rate-limits/orders/pages`

Query Futures USER ORDER Rate Limits With Pagination

分页查询合约用户订单速率限制

Operation ID: `queryFuturesUserorderRateLimitsWithPagination`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| recvWindow | query | integer (int64) |  | 例: `5000` |
| productType | query | string | 是 | 枚举: `CM`, `UM`<br>例: `CM` |
| pageIndex | query | integer (int64) | 是 | 例: `1` |
| pageSize | query | integer (int64) | 是 | 例: `1` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Futures USER ORDER Rate Limits With Pagination / 分页查询合约用户订单速率限制

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| status | string |  | 例: `OK` |
| type | string |  | 例: `GENERAL` |
| code | string |  | 例: `000000000` |
| data | object |  |  |
| data.total | integer (int64) |  | 例: `100` |
| data.rows | object[] |  |  |
| data.rows[].userId | integer (int64) |  | 例: `1000001` |
| data.rows[].userEmail | string |  | 例: `user@email.com` |
| data.rows[].limit | integer (int64) |  | 例: `1200` |

## Query Liquidity Program Overview（查询流动性计划概览）

`GET /sapi/v1/vip/liquidity-programs/overview`

Return user Liquidity Program overview

返回用户流动性计划概述

Operation ID: `queryLiquidityProgramOverview`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Liquidity Program Overview / 流动性计划概览

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| status | string |  | 例: `OK` |
| type | string |  | 例: `GENERAL` |
| code | string |  | 例: `000000000` |
| data | object[] |  |  |
| data[].userId | integer (int64) |  | 例: `10000001` |
| data[].spotMakerTier | integer (int64) |  | 例: `1` |
| data[].spotMakerRebate | string |  | 例: `0.0001` |
| data[].umMakerTier | integer (int64) |  | 例: `1` |
| data[].umMakerRebate | string |  | 例: `0.0001` |
| data[].umTakerTier | integer (int64) |  | 例: `1` |
| data[].umTakerRebate | string |  | 例: `0.0001` |
| data[].cmMakerTier | integer (int64) |  | 例: `1` |
| data[].cmMakerRebate | string |  | 例: `0.0001` |
| data[].optionMakerTier | integer (int64) |  | 例: `1` |
| data[].optionMakerRebate | string |  | 例: `0.0001` |
| data[].optionTakerTier | integer (int64) |  | 例: `1` |
| data[].optionTakerRebate | string |  | 例: `0.0001` |
| data[].fiatMakerTier | integer (int64) |  | 例: `1` |
| data[].fiatMakerRebate | string |  | 例: `0.0001` |

## Query Liquidity Program Performance（查询流动性计划表现）

`GET /sapi/v1/vip/liquidity-programs/performance`

Return user Liquidity Program performance with daily and weekly statistics

通过每日和每周统计数据返回用户流动性计划绩效

Operation ID: `queryLiquidityProgramPerformance`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| recvWindow | query | integer (int64) |  | 例: `5000` |
| dt | query | integer (int64) |  | Query on a specific date. Format is milliseconds.<br>Default: query latest data on Today - 1.<br>查询指定日期的数据，格式为毫秒时间戳。<br>默认：查询前一日的最新数据。<br>例: `1770736694138` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Liquidity Program Performance / 流动性计划表现

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| status | string |  | 例: `OK` |
| type | string |  | 例: `GENERAL` |
| code | string |  | 例: `000000000` |
| data | object[] |  |  |
| data[].userId | integer (int64) |  | 例: `10000001` |
| data[].spotMakerProgram | object |  |  |
| data[].spotMakerProgram.date | integer (int64) |  | 例: `1716940800000` |
| data[].spotMakerProgram.dailyStats | object |  |  |
| data[].spotMakerProgram.dailyStats.makerVol24h | string |  | 例: `1000.0` |
| data[].spotMakerProgram.dailyStats.makerVol24hPct | string |  | 例: `1.12` |
| data[].spotMakerProgram.weeklyStats | object |  |  |
| data[].spotMakerProgram.weeklyStats.weeklyMakerVol | string |  | 例: `1000.0` |
| data[].spotMakerProgram.weeklyStats.weeklyMakerVolPct | string |  | 例: `1.12` |
| data[].umMakerProgram | object |  |  |
| data[].umMakerProgram.date | integer (int64) |  | 例: `1716940800000` |
| data[].umMakerProgram.dailyStats | object |  |  |
| data[].umMakerProgram.dailyStats.makerVol24h | string |  | 例: `1000.0` |
| data[].umMakerProgram.dailyStats.makerVol24hExclBTC | string |  | 例: `1000.0` |
| data[].umMakerProgram.dailyStats.makerVol24hPct | string |  | 例: `1.12` |
| data[].umMakerProgram.dailyStats.makerVol24hPctExclBTC | string |  | 例: `1.23` |
| data[].umMakerProgram.dailyStats.makerVol24hPctUSDC | string |  | 例: `0.97` |
| data[].umMakerProgram.weeklyStats | object |  |  |
| data[].umMakerProgram.weeklyStats.weeklyMakerVol | string |  | 例: `1000.0` |
| data[].umMakerProgram.weeklyStats.weeklyMakerVolExclBTC | string |  | 例: `1000.0` |
| data[].umMakerProgram.weeklyStats.weeklyMakerVolPct | string |  | 例: `1.12` |
| data[].umMakerProgram.weeklyStats.weeklyMakerVolPctExclBTC | string |  | 例: `1.23` |
| data[].umMakerProgram.weeklyStats.weeklyMakerVolPctUSDC | string |  | 例: `0.97` |
| data[].cmMakerProgram | object |  |  |
| data[].cmMakerProgram.date | integer (int64) |  | 例: `1716940800000` |
| data[].cmMakerProgram.dailyStats | object |  |  |
| data[].cmMakerProgram.dailyStats.makerVol24h | string |  | 例: `1000.0` |
| data[].cmMakerProgram.dailyStats.makerVol24hExclBTC | string |  | 例: `1000.0` |
| data[].cmMakerProgram.dailyStats.makerVol24hPct | string |  | 例: `2.01` |
| data[].cmMakerProgram.dailyStats.makerVol24hPctExclBTC | string |  | 例: `2.35` |
| data[].cmMakerProgram.weeklyStats | object |  |  |
| data[].cmMakerProgram.weeklyStats.weeklyMakerVol | string |  | 例: `1000.0` |
| data[].cmMakerProgram.weeklyStats.weeklyMakerVolExclBTC | string |  | 例: `1000.0` |
| data[].cmMakerProgram.weeklyStats.weeklyMakerVolPct | string |  | 例: `2.01` |
| data[].cmMakerProgram.weeklyStats.weeklyMakerVolPctExclBTC | string |  | 例: `2.35` |
| data[].umTakerProgram | object |  |  |
| data[].umTakerProgram.date | integer (int64) |  | 例: `1716940800000` |
| data[].umTakerProgram.dailyStats | object |  |  |
| data[].umTakerProgram.dailyStats.takerVol24hBTC | string |  | 例: `1000.0` |
| data[].umTakerProgram.dailyStats.takerVol24hAlt | string |  | 例: `1000.0` |
| data[].umTakerProgram.dailyStats.takerVol24hTotal | string |  | 例: `1000.0` |
| data[].umTakerProgram.dailyStats.takerVol24hPctBTC | string |  | 例: `0.97` |
| data[].umTakerProgram.dailyStats.takerVol24hPctAlt | string |  | 例: `0.97` |
| data[].umTakerProgram.weeklyStats | object |  |  |
| data[].umTakerProgram.weeklyStats.weeklyTakerVolBTC | string |  | 例: `1000.0` |
| data[].umTakerProgram.weeklyStats.weeklyTakerVolAlt | string |  | 例: `1000.0` |
| data[].umTakerProgram.weeklyStats.weeklyTakerVolTotal | string |  | 例: `1000.0` |
| data[].umTakerProgram.weeklyStats.weeklyTakerVolPctBTC | string |  | 例: `0.97` |
| data[].umTakerProgram.weeklyStats.weeklyTakerVolPctAlt | string |  | 例: `0.97` |

## Query Liquidity Program Weekly Results（查询流动性计划每周结果）

`GET /sapi/v1/vip/liquidity-programs/weekly-result`

Query Liquidity Program Weekly Results

- Return user Liquidity Program weekly results with final rebates
- Please note that the response will only update when each evaluation cycle is completed; data will be updated each Monday around 10:00 UTC

查询流动性计划每周结果
- 每周向用户返还流动性计划结果及最终返利
- 请注意，回复仅在每个评估周期完成后更新；数据将于每周一 UTC 时间 10:00 左右更新

Operation ID: `queryLiquidityProgramWeeklyResults`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| recvWindow | query | integer (int64) |  | 例: `5000` |
| dt | query | integer (int64) |  | Query on a specific week. Format is milliseconds.<br>Default: query latest data on previous week.<br>查询指定周的数据，格式为毫秒时间戳。<br>默认：查询上一周的最新数据。<br>例: `1770736694138` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Liquidity Program Weekly Results / 流动性计划每周结果

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| status | string |  | 例: `OK` |
| type | string |  | 例: `GENERAL` |
| code | string |  | 例: `000000000` |
| data | object[] |  |  |
| data[].userId | integer (int64) |  | 例: `10000001` |
| data[].spotMakerProgram | object |  |  |
| data[].spotMakerProgram.weekStart | integer (int64) |  | 例: `1717372800000` |
| data[].spotMakerProgram.finalRebate | string |  | 例: `-0.0001` |
| data[].spotMakerProgram.weeklyStats | object |  |  |
| data[].spotMakerProgram.weeklyStats.weeklyMakerVol | string |  | 例: `1000.0` |
| data[].spotMakerProgram.weeklyStats.weeklyMakerVolPct | string |  | 例: `1.0` |
| data[].umMakerProgram | object |  |  |
| data[].umMakerProgram.weekStart | integer (int64) |  | 例: `1717372800000` |
| data[].umMakerProgram.finalRebateUsdt | number (float) |  | 例: `-0.0001` |
| data[].umMakerProgram.weeklyStats | object |  |  |
| data[].umMakerProgram.weeklyStats.weeklyMakerVol | string |  | 例: `1000.0` |
| data[].umMakerProgram.weeklyStats.weeklyMakerVolExclBTC | string |  | 例: `1000.0` |
| data[].umMakerProgram.weeklyStats.weeklyMakerVolPct | string |  | 例: `1.0` |
| data[].umMakerProgram.weeklyStats.weeklyMakerVolPctExclBTC | string |  | 例: `1.0` |
| data[].umMakerProgram.weeklyStats.weeklyMakerVolPctUSDC | string |  | 例: `1.0` |
| data[].cmMakerProgram | object |  |  |
| data[].cmMakerProgram.weekStart | integer (int64) |  | 例: `1717372800000` |
| data[].cmMakerProgram.finalRebate | string |  | 例: `-0.00005` |
| data[].cmMakerProgram.weeklyStats | object |  |  |
| data[].cmMakerProgram.weeklyStats.weeklyMakerVol | string |  | 例: `1000.0` |
| data[].cmMakerProgram.weeklyStats.weeklyMakerVolExclBTC | string |  | 例: `1000.0` |
| data[].cmMakerProgram.weeklyStats.weeklyMakerVolPct | string |  | 例: `5.75` |
| data[].cmMakerProgram.weeklyStats.weeklyMakerVolPctExclBTC | string |  | 例: `3.56` |
| data[].umTakerProgram | object |  |  |
| data[].umTakerProgram.weekStart | integer (int64) |  | 例: `1717372800000` |
| data[].umTakerProgram.finalUsdtDiscount | string |  | 例: `-0.0001` |
| data[].umTakerProgram.finalUsdcDiscount | string |  | 例: `-0.0001` |
| data[].umTakerProgram.weeklyStats | object |  |  |
| data[].umTakerProgram.weeklyStats.weeklyTakerVolBTC | string |  | 例: `1000.0` |
| data[].umTakerProgram.weeklyStats.weeklyTakerVolAlt | string |  | 例: `1000.0` |
| data[].umTakerProgram.weeklyStats.weeklyTakerVolTotal | string |  | 例: `1000.0` |
| data[].umTakerProgram.weeklyStats.weeklyTakerVolPctBTC | string |  | 例: `1.0` |
| data[].umTakerProgram.weeklyStats.weeklyTakerVolPctAlt | string |  | 例: `1.0` |

## Query Symbol Commission Fee（查询现货交易对费率）

`GET /sapi/v1/commission/queryCommissionFee`

Query Symbol Commission Fee

- The master account can query the fee rate on a specific symbol of the specified sub-account
- Broker accounts are not supported
- The fee rate does not include the Spot market maker rebate rate
- The fee rate does not reflect the impact of the BNB discount

查询现货交易对费率

- 主账户可查询指定子账户特定交易品种的费率
- 不支持经纪商账户
- 此费率不包含现货做市商返佣率
- 此费率不反映BNB折扣的影响

Operation ID: `querySymbolCommissionFee`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| recvWindow | query | integer (int64) |  | 例: `5000` |
| userId | query | integer (int64) |  | 例: `1` |
| symbol | query | string | 是 | 例: `BNBUSDT` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Symbol Commission Fee / 交易对手续费费率

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| userId | integer (int64) |  | 例: `103909` |
| symbol | string |  | 例: `BNBUSDT` |
| makerCommission | string |  | 例: `0.001` |
| takerCommission | string |  | 例: `0.001` |