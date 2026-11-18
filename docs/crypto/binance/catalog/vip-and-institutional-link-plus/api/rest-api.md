---
exchange: binance
source_url: https://developers.binance.com/en/docs/catalog/vip-and-institutional-link-plus/api/rest-api
api_type: REST
updated_at: 2026-11-18 18:48:29.579829
---

# Link Plus REST API

Schema: https://developers.binance.com/en/docs/catalog/vip-and-institutional-link-plus/api/rest-api/1.0.0/schema.yaml

Manage advanced account operations and trading services for Binance Link Plus partners.

为 Binance Link Plus 合作伙伴管理高级账户操作和交易服务。

版本: 1.0.0

## 服务地址

- `https://api.binance.com`

## 接口列表

- `POST /sapi/v1/vip/link-plus/subgroups/{groupId}/accounts` — Add Accounts to Sub-Groups
- `POST /sapi/v1/vip/link-plus/subgroups` — Create New Sub-Groups
- `GET /sapi/v1/vip/link-plus/overview` — Query Link Plus Overview
- `GET /sapi/v1/vip/liquidity-programs/subgroups/overview` — Query Liquidity Program Overview for Sub-Groups
- `GET /sapi/v1/vip/liquidity-programs/subgroups/performance` — Query Liquidity Program Performance for Sub-Groups
- `GET /sapi/v1/vip/liquidity-programs/subgroups/weekly-result` — Query Liquidity Program Weekly Results for Sub-Groups
- `GET /sapi/v1/vip/link-plus/subgroups/detail` — Query Sub-Groups Details
- `PUT /sapi/v1/vip/link-plus/subgroups/{groupId}/name` — Update Name of Sub-Groups

## Add Accounts to Sub-Groups（子账号添加到子分组）

`POST /sapi/v1/vip/link-plus/subgroups/{groupId}/accounts`

Add one or multiple accounts to a specific group under the master account

将一个或多个账户添加到主账户下的特定组

Operation ID: `addAccountsToSubGroups`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| groupId | path | integer (int64) | 是 | Sub-group ID.<br>子分组 ID。<br>例: `1001` |

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| accountIds | integer (int64)[] | 是 | Sub-account IDs to be added into the sub-group.<br>要添加到子分组的子账户 ID 列表。 |
| recvWindow | integer (int64) |  | Request validity window in milliseconds.<br>请求有效时间窗口，单位为毫秒。<br>例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：OK / 成功

## Create New Sub-Groups（创建新子分组）

`POST /sapi/v1/vip/link-plus/subgroups`

Create a new sub-group under master account

在主账户下创建一个新的子组

Operation ID: `createNewSubGroups`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| groupName | string | 是 | Name of the sub-group.<br>子分组名称。<br>例: `Group New` |
| recvWindow | integer (int64) |  | Request validity window in milliseconds.<br>请求有效时间窗口，单位为毫秒。<br>例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：OK / 成功

## Query Link Plus Overview（查询 Link Plus 概览）

`GET /sapi/v1/vip/link-plus/overview`

Return master account information for all sub-groups, including total number of groups, total trading volumes and assets

返回所有子群组的主账户信息，包括群组总数、总交易量、总资产

Operation ID: `queryLinkPlusOverview`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds.<br>请求有效时间窗口，单位为毫秒。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Link Plus Overview / Link Plus 概览

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| status | string |  | 例: `OK` |
| type | string |  | 例: `GENERAL` |
| code | string |  | 例: `000000000` |
| data | object |  |  |
| data.vipLevel | integer (int64) |  | 例: `1` |
| data.bnbHold | string |  | 例: `10000.0` |
| data.totalGroups | integer (int64) |  | 例: `50` |
| data.groupLimit | integer (int64) |  | 例: `1000` |
| data.totalAssets | string |  | 例: `10000.0` |
| data.30dSpotVol | string |  | 例: `10000.0` |
| data.30dFutVol | string |  | 例: `10000.0` |

## Query Liquidity Program Overview for Sub-Groups（查询子分组的流动性计划概览）

`GET /sapi/v1/vip/liquidity-programs/subgroups/overview`

Return sub-group Liquidity Program status overview under the master account

返回主账户下子分组流动性计划概览

Operation ID: `queryLiquidityProgramOverviewForSubGroups`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds.<br>请求有效时间窗口，单位为毫秒。<br>例: `5000` |
| groupId | query | integer (int64) |  | Query specific groups.<br>Support multiple values. Max number of groupId is 50. Example:<br>&groupId=1001&groupId=1002. Default: query all active groups<br>查询指定分组。<br>支持多个值。groupId 最多 50 个。示例：&groupId=1001&groupId=1002。默认查询所有活跃分组。<br>例: `1` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Liquidity Program Overview for Sub-Groups / 子分组流动性计划概览

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| status | string |  | 例: `OK` |
| type | string |  | 例: `GENERAL` |
| code | string |  | 例: `000000000` |
| data | object[] |  |  |
| data[].userId | integer (int64) |  | 例: `10000001` |
| data[].groupId | integer (int64) |  | 例: `1001` |
| data[].spotMakerTier | integer (int64) |  | 例: `1` |
| data[].spotMakerRebate | string |  | 例: `0.0001` |
| data[].umMakerTier | integer (int64) |  | 例: `1` |
| data[].umMakerRebate | string |  | 例: `0.0001` |
| data[].umTakerTier | integer (int64) |  | 例: `1` |
| data[].umTakerRebate | string |  | 例: `0.0001` |
| data[].cmMakerTier | integer (int64) |  | 例: `1` |
| data[].cmMakerRebate | string |  | 例: `0.0001` |

## Query Liquidity Program Performance for Sub-Groups（查询子分组的流动性计划表现）

`GET /sapi/v1/vip/liquidity-programs/subgroups/performance`

Return sub-group Liquidity Program performance with daily and weekly statistics

返回子分组流动性计划表现的每日和每周统计数据

Operation ID: `queryLiquidityProgramPerformanceForSubGroups`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds.<br>请求有效时间窗口，单位为毫秒。<br>例: `5000` |
| groupId | query | integer (int64) |  | Query specific groups.<br>Support multiple values. Max number of groupId is 50.<br>Example:<br>&groupId=1001&groupId=1002<br>Default: query all active groups.<br>查询指定分组。<br>支持多个值。groupId 最多 50 个。<br>示例：&groupId=1001&groupId=1002<br>默认查询所有活跃分组。<br>例: `1001` |
| date | query | integer (int64) |  | Query on a specific date. Format is milliseconds.<br>Default: query latest data on Today - 1.<br>查询指定日期，格式为毫秒时间戳。<br>默认查询 T-1 的最新数据。<br>例: `1716940800000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Liquidity Program Performance for Sub-Groups / 子分组流动性计划表现

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| status | string |  | 例: `OK` |
| type | string |  | 例: `GENERAL` |
| code | string |  | 例: `000000000` |
| data | object[] |  |  |
| data[].userId | integer (int64) |  | 例: `10000001` |
| data[].groupId | integer (int64) |  | 例: `1001` |
| data[].groupName | string |  | 例: `Group 1` |
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

## Query Liquidity Program Weekly Results for Sub-Groups（查询子分组的流动性计划每周结果）

`GET /sapi/v1/vip/liquidity-programs/subgroups/weekly-result`

Return sub-group Liquidity Program weekly results with final rebates

返回子分组流动性计划的每周结果及最终返利

Operation ID: `queryLiquidityProgramWeeklyResultsForSubGroups`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds.<br>请求有效时间窗口，单位为毫秒。<br>例: `5000` |
| groupId | query | integer (int64) |  | Query specific groups.<br>Support multiple values. Max number of groupId is 50. Example:<br>&groupId=1001&groupId=1002. Default: query all active groups<br>查询指定分组。<br>支持多个值。groupId 最多 50 个。<br>示例：&groupId=1001&groupId=1002<br>默认查询所有活跃分组。<br>例: `1` |
| date | query | integer (int64) |  | Query on a specific week. Format is milliseconds.<br>Default: query latest data on previous week.<br>查询指定周，格式为毫秒时间戳。<br>默认查询上一周的最新数据。<br>例: `1770736694138` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Liquidity Program Weekly Results for Sub-Groups / 子分组流动性计划每周结果

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| status | string |  | 例: `OK` |
| type | string |  | 例: `GENERAL` |
| code | string |  | 例: `000000000` |
| data | object[] |  |  |
| data[].userId | integer (int64) |  | 例: `10000001` |
| data[].groupId | integer (int64) |  | 例: `1001` |
| data[].groupName | string |  | 例: `Group 1` |
| data[].spotMakerProgram | object |  |  |
| data[].spotMakerProgram.weekStart | integer (int64) |  | 例: `1717372800000` |
| data[].spotMakerProgram.finalRebate | string |  | 例: `-0.0001` |
| data[].spotMakerProgram.weeklyStats | object |  |  |
| data[].spotMakerProgram.weeklyStats.weeklyMakerVol | string |  | 例: `1000.0` |
| data[].spotMakerProgram.weeklyStats.weeklyMakerVolPct | string |  | 例: `1.0` |
| data[].umMakerProgram | object |  |  |
| data[].umMakerProgram.weekStart | integer (int64) |  | 例: `1717372800000` |
| data[].umMakerProgram.finalRebateUsdt | string |  | 例: `-0.0001` |
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
| data[].cmMakerProgram.weeklyStats.weeklyMakerVolPct | string |  | 例: `1.0` |
| data[].cmMakerProgram.weeklyStats.weeklyMakerVolPctExclBTC | string |  | 例: `1.0` |
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

## Query Sub-Groups Details（查询子分组详情）

`GET /sapi/v1/vip/link-plus/subgroups/detail`

Return sub-group information including trading volume, fee tiers and sub-account details

返回子分组信息，包括交易量、费用等级和子账户详细信息

Operation ID: `querySubGroupsDetails`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds.<br>请求有效时间窗口，单位为毫秒。<br>例: `5000` |
| groupId | query | integer (int64) |  | Query specific groups.<br>Support multiple values. Max number of groupId is 50. Example:<br>&groupId=1001&groupId=1002. Default: query all active groups<br>查询指定分组。<br>支持多个值。groupId 最多 50 个。<br>示例：&groupId=1001&groupId=1002<br>默认查询所有活跃分组。<br>例: `1` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Sub-Groups Details / 子分组详情

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| status | string |  | 例: `OK` |
| type | string |  | 例: `GENERAL` |
| code | string |  | 例: `000000000` |
| data | object[] |  |  |
| data[].groupId | integer (int64) |  | 例: `1001` |
| data[].groupName | string |  | 例: `arbitration` |
| data[].accountLimit | integer (int64) |  | 例: `50` |
| data[].tradeLevel | integer (int64) |  | 例: `2` |
| data[].feeTier | integer (int64) |  | 例: `1` |
| data[].groupAssets | string |  | 例: `1000.0` |
| data[].group30dSpotVol | string |  | 例: `1000.0` |
| data[].group30dFutVol | string |  | 例: `1000.0` |
| data[].subAccounts | object[] |  |  |
| data[].subAccounts[].accountId | integer (int64) |  | 例: `1000200159113` |
| data[].subAccounts[].accountEmail | string |  | 例: `account_1@test.com` |
| data[].subAccounts[].accountAsset | string |  | 例: `1000.0` |
| data[].subAccounts[].accountDailySpotVol | string |  | 例: `1000.0` |
| data[].subAccounts[].accountDailyFutVol | string |  | 例: `1000.0` |
| data[].subAccounts[].account30dSpotVol | string |  | 例: `1000.0` |
| data[].subAccounts[].account30dFutVol | string |  | 例: `1000.0` |

## Update Name of Sub-Groups（更新子分组的名称）

`PUT /sapi/v1/vip/link-plus/subgroups/{groupId}/name`

Update names of sub-groups under master account

更新主账号下子群组名称

Operation ID: `updateNameOfSubGroups`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| groupId | path | integer (int64) | 是 | Sub-group ID.<br>子分组 ID。<br>例: `1001` |

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| groupName | string | 是 | Updated name of the sub-group.<br>子分组更新后的名称。<br>例: `Group New 2` |
| recvWindow | integer (int64) |  | Request validity window in milliseconds.<br>请求有效时间窗口，单位为毫秒。<br>例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：OK / 成功