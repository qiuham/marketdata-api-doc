---
exchange: binance
source_url: https://developers.binance.com/en/docs/catalog/investment-and-services-rebate/api/rest-api
api_type: REST
updated_at: 2026-11-26 18:50:09.393341
---

# Rebate REST API

Schema: https://developers.binance.com/en/docs/catalog/investment-and-services-rebate/api/rest-api/1.0.0/schema.yaml

Query spot trading rebate history records.

查询现货交易返佣历史记录。

版本: 1.0.0

## 服务地址

- `https://api.binance.com`
- `https://api-gcp.binance.com`
- `https://api1.binance.com`
- `https://api2.binance.com`
- `https://api3.binance.com`
- `https://api4.binance.com`

## 接口列表

- `GET /sapi/v1/rebate/taxQuery` — Get Spot Rebate History Records (USER_DATA)

## Get Spot Rebate History Records (USER_DATA)（获取现货返佣历史记录 (USER_DATA)）

`GET /sapi/v1/rebate/taxQuery`

Get Spot Rebate History Records

获取现货返佣历史记录

Operation ID: `getSpotRebateHistoryRecords`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| startTime | query | integer (int64) |  | Start time in milliseconds.<br>开始时间戳（毫秒）。<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | End time in milliseconds.<br>结束时间戳（毫秒）。<br>例: `1641782889000` |
| page | query | integer (int64) |  | Page number.<br>页码。<br>默认: `1`<br>例: `1` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds.<br>请求有效时间窗口，单位为毫秒。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Spot Rebate History Records / 获取现货返佣历史记录

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| status | string |  | 例: `OK` |
| type | string |  | 例: `GENERAL` |
| code | string |  | 例: `000000000` |
| data | object |  |  |
| data.page | integer (int64) |  | Current page number.<br>当前页码。<br>例: `1` |
| data.totalRecords | integer (int64) |  | Total number of records.<br>总记录数。<br>例: `2` |
| data.totalPageNum | integer (int64) |  | Total number of pages.<br>总页数。<br>例: `1` |
| data.data | object[] |  | Rebate records.<br>返佣记录列表。 |
| data.data[].asset | string |  | Rebate asset.<br>返佣资产。<br>例: `USDT` |
| data.data[].type | integer (int64) |  | 1 is commission rebate, 2 is referral kickback<br>返佣类型：1为推荐人返佣，2为被推荐人返现<br>例: `1` |
| data.data[].amount | string |  | Rebate amount.<br>返佣金额。<br>例: `0.0001126` |
| data.data[].updateTime | integer (int64) |  | Update timestamp.<br>更新时间戳。<br>例: `1637651320000` |