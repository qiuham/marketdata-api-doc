---
exchange: binance
source_url: https://developers.binance.com/en/docs/catalog/vip-and-institutional-vip-caas/api/rest-api
api_type: REST
updated_at: 2026-11-21 18:49:07.350628
---

# VIP CAAS REST API

Schema: https://developers.binance.com/en/docs/catalog/vip-and-institutional-vip-caas/api/rest-api/1.0.0/schema.yaml

Crypto-as-a-Service Commission Markup APIs.

Crypto-as-a-Service 佣金加点 API。

版本: 1.0.0

## 服务地址

- `https://api.binance.com`
- `https://api-gcp.binance.com`
- `https://api1.binance.com`
- `https://api2.binance.com`
- `https://api3.binance.com`
- `https://api4.binance.com`

## 接口列表

- `GET /sapi/v1/vip/caas/commission/fee-groups` — Query Fee Groups (USER_DATA)
- `POST /sapi/v1/vip/caas/commission/fee-groups` — Create Fee Group (TRADE)
- `DELETE /sapi/v1/vip/caas/commission/fee-groups` — Delete Fee Group (TRADE)
- `PUT /sapi/v1/vip/caas/commission/fee-groups/commission` — Update Fee Group Commission (TRADE)
- `GET /sapi/v1/vip/caas/commission/fee-groups/members` — Query Fee Group Members (USER_DATA)
- `POST /sapi/v1/vip/caas/commission/fee-groups/members` — Assign Members to Fee Group (TRADE)
- `DELETE /sapi/v1/vip/caas/commission/fee-groups/members` — Unassign Members from Fee Group (TRADE)
- `GET /sapi/v1/vip/caas/commission/member-fee-group` — Query One Member's Fee Group (USER_DATA)
- `GET /sapi/v1/vip/caas/commission/markup-trade-aggregations` — Query Markup Trade Commission Aggregation Reportings (USER_DATA)
- `GET /sapi/v1/vip/caas/commission/markup-trade-details` — Query Markup Trade Detail Reportings (USER_DATA)

## Query Fee Groups (USER_DATA)（查询费率组 (USER_DATA)）

`GET /sapi/v1/vip/caas/commission/fee-groups`

Query all fee groups for the authenticated master account with pagination.

分页查询已认证母账号下的所有费率组。

Operation ID: `queryFeeGroups`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| pageIndex | query | integer | 是 | Page index, starting from 1<br>页码，从 1 开始<br>例: `1` |
| pageSize | query | integer | 是 | Page size (1-100)<br>每页条数 (1-100)<br>例: `10` |
| recvWindow | query | integer (int64) |  | No more than 60000<br>不超过 60000<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | 例: `1770736694138` |

### 响应 200：Query Fee Groups / 查询费率组

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| status | string |  | 例: `OK` |
| type | string |  | 例: `GENERAL` |
| code | string |  | 例: `000000000` |
| data | object |  |  |
| data.total | integer |  | 例: `2` |
| data.rows | object[] |  |  |
| data.rows[].groupCode | string |  | 例: `FG001` |
| data.rows[].groupName | string |  | 例: `Premium Tier` |
| data.rows[].makerMarkup | string |  | 例: `0.002` |
| data.rows[].takerMarkup | string |  | 例: `0.003` |
| data.rows[].subAccountCount | integer |  | 例: `15` |
| data.rows[].createdTime | integer (int64) |  | 例: `1654645645654` |
| data.rows[].updatedTime | integer (int64) |  | 例: `1654645645654` |

## Create Fee Group (TRADE)（创建费率组 (TRADE)）

`POST /sapi/v1/vip/caas/commission/fee-groups`

Create a new fee group for the authenticated master account.

You need to enable "trade" option for the API key which requests this endpoint.

为已认证的母账号创建新的费率组。

需要为请求此接口的 API key 启用 "trade" 选项。

Operation ID: `createFeeGroup`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| groupName | string | 是 | Fee group name (max 32 characters)<br>费率组名称（最多 32 个字符）<br>例: `Premium Tier` |
| makerMarkup | number (double) | 是 | Maker markup rate (e.g., 0.002)<br>Maker 加点费率（例如 0.002）<br>例: `0.002` |
| takerMarkup | number (double) | 是 | Taker markup rate (e.g., 0.003)<br>Taker 加点费率（例如 0.003）<br>例: `0.003` |
| recvWindow | integer (int64) |  | No more than 60000<br>不超过 60000<br>例: `5000` |
| timestamp | integer (int64) | 是 | 例: `1770736694138` |

### 响应 200：Create Fee Group / 创建费率组

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| status | string |  | 例: `OK` |
| type | string |  | 例: `GENERAL` |
| code | string |  | 例: `000000000` |
| data | object |  |  |
| data.groupCode | string |  | 例: `FG001` |
| data.groupName | string |  | 例: `Premium Tier` |
| data.makerMarkup | string |  | 例: `0.002` |
| data.takerMarkup | string |  | 例: `0.003` |
| data.subAccountCount | integer |  | 例: `0` |
| data.createdTime | integer (int64) |  | 例: `1654645645654` |
| data.updatedTime | integer (int64) |  | 例: `1654645645654` |

## Delete Fee Group (TRADE)（删除费率组 (TRADE)）

`DELETE /sapi/v1/vip/caas/commission/fee-groups`

Delete a fee group. All sub-accounts must be unassigned first.

You need to enable "trade" option for the API key which requests this endpoint.

删除费率组。所有子账号必须先取消分配。

需要为请求此接口的 API key 启用 "trade" 选项。

Operation ID: `deleteFeeGroup`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| groupCode | query | string | 是 | Fee group code<br>费率组编码<br>例: `FG001` |
| recvWindow | query | integer (int64) |  | No more than 60000<br>不超过 60000<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | 例: `1770736694138` |

### 响应 200：Delete Fee Group / 删除费率组

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| status | string |  | 例: `OK` |
| type | string |  | 例: `GENERAL` |
| code | string |  | 例: `000000000` |

## Update Fee Group Commission (TRADE)（更新费率组佣金 (TRADE)）

`PUT /sapi/v1/vip/caas/commission/fee-groups/commission`

Update commission rates for a fee group.

You need to enable "trade" option for the API key which requests this endpoint.

更新费率组的佣金费率。

需要为请求此接口的 API key 启用 "trade" 选项。

Operation ID: `updateFeeGroupCommission`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| groupCode | query | string | 是 | Fee group code<br>费率组编码<br>例: `FG001` |
| recvWindow | query | integer (int64) |  | No more than 60000<br>不超过 60000<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | 例: `1770736694138` |

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| makerMarkup | number (double) | 是 | New maker markup rate<br>新的 Maker 加点费率<br>例: `0.003` |
| takerMarkup | number (double) | 是 | New taker markup rate<br>新的 Taker 加点费率<br>例: `0.004` |

### 响应 200：Update Fee Group Commission / 更新费率组佣金

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| status | string |  | 例: `OK` |
| type | string |  | 例: `GENERAL` |
| code | string |  | 例: `000000000` |

## Query Fee Group Members (USER_DATA)（查询费率组成员 (USER_DATA)）

`GET /sapi/v1/vip/caas/commission/fee-groups/members`

Query sub-accounts assigned to a fee group with pagination.

分页查询费率组下已分配的子账号。

Operation ID: `queryFeeGroupMembers`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| groupCode | query | string | 是 | Fee group code<br>费率组编码<br>例: `FG001` |
| pageIndex | query | integer | 是 | Page index, starting from 1<br>页码，从 1 开始<br>例: `1` |
| pageSize | query | integer | 是 | Page size (1-100)<br>每页条数 (1-100)<br>例: `10` |
| recvWindow | query | integer (int64) |  | No more than 60000<br>不超过 60000<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | 例: `1770736694138` |

### 响应 200：Query Fee Group Members / 查询费率组成员

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| status | string |  | 例: `OK` |
| type | string |  | 例: `GENERAL` |
| code | string |  | 例: `000000000` |
| data | object |  |  |
| data.total | integer |  | 例: `2` |
| data.rows | object[] |  |  |
| data.rows[].subUserId | integer (int64) |  | 例: `2000001` |
| data.rows[].groupCode | string |  | 例: `FG001` |
| data.rows[].groupName | string |  | 例: `Premium Tier` |
| data.rows[].makerMarkup | string |  | 例: `0.002` |
| data.rows[].takerMarkup | string |  | 例: `0.003` |

## Assign Members to Fee Group (TRADE)（分配成员到费率组 (TRADE)）

`POST /sapi/v1/vip/caas/commission/fee-groups/members`

Assign sub-accounts to a fee group.

You need to enable "trade" option for the API key which requests this endpoint.

将子账号分配到费率组。

需要为请求此接口的 API key 启用 "trade" 选项。

Operation ID: `assignMembersToFeeGroup`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| groupCode | query | string | 是 | Fee group code<br>费率组编码<br>例: `FG001` |
| recvWindow | query | integer (int64) |  | No more than 60000<br>不超过 60000<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | 例: `1770736694138` |

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subUserIds | integer (int64)[] | 是 | List of sub-user IDs to assign. Maximum 10 per request; sending more returns `-1102`.<br>要分配的子用户 ID 列表。每次请求最多 10 个；超过将返回 `-1102`。 |

### 响应 200：Assign Members to Fee Group / 分配成员到费率组

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| status | string |  | 例: `OK` |
| type | string |  | 例: `GENERAL` |
| code | string |  | 例: `000000000` |
| data | object |  |  |
| data.successCount | integer |  | 例: `2` |
| data.failedList | object[] |  |  |
| data.failedList[].subUserId | integer (int64) |  | 例: `2000003` |
| data.failedList[].errorMessage | string |  | 例: `Sub-account does not belong to master` |

## Unassign Members from Fee Group (TRADE)（从费率组移除成员 (TRADE)）

`DELETE /sapi/v1/vip/caas/commission/fee-groups/members`

Remove sub-accounts from a fee group.

You need to enable "trade" option for the API key which requests this endpoint.

从费率组中移除子账号。

需要为请求此接口的 API key 启用 "trade" 选项。

Operation ID: `unassignMembersFromFeeGroup`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| groupCode | query | string | 是 | Fee group code<br>费率组编码<br>例: `FG001` |
| recvWindow | query | integer (int64) |  | No more than 60000<br>不超过 60000<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | 例: `1770736694138` |

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subUserIds | integer (int64)[] | 是 | List of sub-user IDs to unassign. Maximum 10 per request; sending more returns `-1102`.<br>要移除的子用户 ID 列表。每次请求最多 10 个；超过将返回 `-1102`。 |

### 响应 200：Unassign Members from Fee Group / 从费率组移除成员

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| status | string |  | 例: `OK` |
| type | string |  | 例: `GENERAL` |
| code | string |  | 例: `000000000` |
| data | object |  |  |
| data.successCount | integer |  | 例: `2` |
| data.failedList | object[] |  |  |
| data.failedList[].subUserId | integer (int64) |  | 例: `2000003` |
| data.failedList[].errorMessage | string |  | 例: `Sub-account does not belong to group` |

## Query One Member's Fee Group (USER_DATA)（查询单个成员的费率组 (USER_DATA)）

`GET /sapi/v1/vip/caas/commission/member-fee-group`

Query which fee group a sub-account is assigned to.

查询某个子账号所属的费率组。

Operation ID: `queryOneMembersFeeGroup`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| subUserId | query | integer (int64) | 是 | Sub-user ID<br>子用户 ID<br>例: `2000001` |
| recvWindow | query | integer (int64) |  | No more than 60000<br>不超过 60000<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | 例: `1770736694138` |

### 响应 200：Query One Member's Fee Group / 查询单个成员的费率组

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| status | string |  | 例: `OK` |
| type | string |  | 例: `GENERAL` |
| code | string |  | 例: `000000000` |
| data | object |  |  |
| data.subUserId | integer (int64) |  | 例: `2000001` |
| data.groupCode | string |  | 例: `FG001` |
| data.groupName | string |  | 例: `Premium Tier` |
| data.makerMarkup | string |  | 例: `0.002` |
| data.takerMarkup | string |  | 例: `0.003` |

## Query Markup Trade Commission Aggregation Reportings (USER_DATA)（查询加点交易佣金聚合报表 (USER_DATA)）

`GET /sapi/v1/vip/caas/commission/markup-trade-aggregations`

Query aggregated markup fee history records by date, sub-account, and fee group.

按日期、子账号和费率组查询聚合加点费用历史记录。

Operation ID: `queryMarkupTradeCommissionAggregationReportings`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| groupCode | query | string |  | Fee group code filter<br>费率组编码筛选<br>例: `FG001` |
| subUserId | query | integer (int64) |  | Sub-user ID filter<br>子用户 ID 筛选<br>例: `2000001` |
| startTime | query | integer (int64) | 是 | Start of search window (milliseconds)<br>查询开始时间（毫秒）<br>例: `1654560000000` |
| endTime | query | integer (int64) | 是 | End of search window (milliseconds)<br>查询结束时间（毫秒）<br>例: `1654646400000` |
| pageIndex | query | integer | 是 | Page index, starting from 1<br>页码，从 1 开始<br>例: `1` |
| pageSize | query | integer | 是 | Page size (1-100)<br>每页条数 (1-100)<br>例: `10` |
| recvWindow | query | integer (int64) |  | No more than 60000<br>不超过 60000<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | 例: `1770736694138` |

### 响应 200：Query Markup Trade Commission Aggregation Reportings / 查询加点交易佣金聚合报表

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| status | string |  | 例: `OK` |
| type | string |  | 例: `GENERAL` |
| code | string |  | 例: `000000000` |
| data | object |  |  |
| data.total | integer |  | 例: `2` |
| data.rows | object[] |  |  |
| data.rows[].date | integer (int64) |  | 例: `1654646400000` |
| data.rows[].subUserId | integer (int64) |  | 例: `2000001` |
| data.rows[].groupCode | string |  | 例: `FG001` |
| data.rows[].groupName | string |  | 例: `Premium Tier` |
| data.rows[].totalVolumeUsdt | string |  | 例: `150000.50` |
| data.rows[].markupAsset | string |  | 例: `USDT` |
| data.rows[].markupMakerIncome | string |  | 例: `150.00` |
| data.rows[].markupTakerIncome | string |  | 例: `225.00` |

## Query Markup Trade Detail Reportings (USER_DATA)（查询加点交易明细报表 (USER_DATA)）

`GET /sapi/v1/vip/caas/commission/markup-trade-details`

Query trade-level markup fee details.

查询逐笔交易级别的加点费用详情。

Operation ID: `queryMarkupTradeDetailReportings`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| subUserId | query | integer (int64) |  | Sub-user ID filter<br>子用户 ID 筛选<br>例: `2000001` |
| groupCode | query | string |  | Fee group code filter<br>费率组编码筛选<br>例: `FG001` |
| symbol | query | string |  | Trading symbol filter (e.g., BTCUSDT)<br>交易对筛选（例如 BTCUSDT）<br>例: `BTCUSDT` |
| startTime | query | integer (int64) | 是 | Start of search window (milliseconds)<br>查询开始时间（毫秒）<br>例: `1654560000000` |
| endTime | query | integer (int64) | 是 | End of search window (milliseconds)<br>查询结束时间（毫秒）<br>例: `1654646400000` |
| pageIndex | query | integer | 是 | Page index, starting from 1<br>页码，从 1 开始<br>例: `1` |
| pageSize | query | integer | 是 | Page size (1-100)<br>每页条数 (1-100)<br>例: `10` |
| recvWindow | query | integer (int64) |  | No more than 60000<br>不超过 60000<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | 例: `1770736694138` |

### 响应 200：Query Markup Trade Detail Reportings / 查询加点交易明细报表

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| status | string |  | 例: `OK` |
| type | string |  | 例: `GENERAL` |
| code | string |  | 例: `000000000` |
| data | object |  |  |
| data.total | integer |  | 例: `1` |
| data.rows | object[] |  |  |
| data.rows[].orderId | integer (int64) |  | 例: `123456789` |
| data.rows[].subUserId | integer (int64) |  | 例: `2000001` |
| data.rows[].groupCode | string |  | 例: `FG001` |
| data.rows[].groupName | string |  | 例: `Premium Tier` |
| data.rows[].product | string |  | 例: `SPOT` |
| data.rows[].symbol | string |  | 例: `BTCUSDT` |
| data.rows[].tradeSide | string |  | 例: `BUY` |
| data.rows[].tradeType | string |  | 例: `TAKER` |
| data.rows[].price | string |  | 例: `45000.00` |
| data.rows[].qty | string |  | 例: `0.5` |
| data.rows[].baseAsset | string |  | 例: `BTC` |
| data.rows[].quoteAsset | string |  | 例: `USDT` |
| data.rows[].quoteQty | string |  | 例: `22500.00` |
| data.rows[].baseRate | string |  | 例: `0.001` |
| data.rows[].markupRate | string |  | 例: `0.003` |
| data.rows[].totalFeeRate | string |  | 例: `0.004` |
| data.rows[].feeAsset | string |  | 例: `BTC` |
| data.rows[].transactionTime | integer (int64) |  | 例: `1654646500000` |
| data.rows[].markupAsset | string |  | 例: `USDT` |
| data.rows[].markupAmount | string |  | 例: `67.50` |
| data.rows[].markupAmountUsdt | string |  | 例: `67.50` |
| data.rows[].markupConvertRate | string |  | 例: `1.0` |
| data.rows[].markupConvertTime | integer (int64) |  | 例: `1654732800000` |