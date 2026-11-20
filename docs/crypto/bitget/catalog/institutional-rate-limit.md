---
exchange: bitget
source_url: https://www.bitget.com/docs/catalog/institutional-rate-limit
api_type: REST
updated_at: 2026-11-20 19:02:15.148236
---

# Institutional Rate Limit

Set and query institutional rate limit quotas for accounts.

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v3/user/rate-limit-quota` — Get RateLimit Quota
- `POST /api/v3/user/set-rate-limit-quota` — Set RateLimit Quota

## Get RateLimit Quota

`GET /api/v3/user/rate-limit-quota`

Query the rate limit quota configuration for accounts. Supports querying the quota allocation for a single account or listing all sub-account quotas under a master account.

This endpoint also supports being called directly by a sub-account using its own API Key, to query its own rate limit quota.

> **Note**: This endpoint is only available to **MM (Market Maker) and PRO** institutional users.

- Rate limit: 10/sec/UID

- Permission: UTA mgt. (read)

Operation ID: `utaUserRateLimitGetRateLimitQuota`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| category | query | string | 是 | Product type<br><br>`spot` Spot <br><br>`futures` Futures |
| uid | query | string |  | Account UID<br><br>Used to query a single account's rate limit quota; omit to list all sub-accounts<br><br>When called by a sub-account itself, this field is not required and is ignored — the sub-account's own quota is returned |
| cursor | query | string |  | Cursor<br><br>Used for pagination in subsequent queries |
| limit | query | string |  | Limit per page<br><br>Default: `100`. Maximum: `100` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.category | string |  | Product type<br><br>`spot` Spot <br><br>`futures` Futures |
| data.quotaList | object[] |  | Sub-account rate limit quota list |
| data.quotaList[].uid | string |  | Account UID |
| data.quotaList[].quota | string |  | The actual configured single account rate limit value |
| data.masterSubQuota | string |  | The actual configured master-sub account rate limit value |
| data.masterSubCap | string |  | Master-sub account rate limit Cap |
| data.cursor | string |  | Cursor<br><br>Used for pagination in subsequent queries |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1753987234567,
  "data": {
    "category": "futures",
    "quotaList": [
      {
        "uid": "123456",
        "quota": "100"
      }
    ],
    "masterSubQuota": "10000",
    "masterSubCap": "80000",
    "cursor": "1"
  }
}
```

## Set RateLimit Quota

`POST /api/v3/user/set-rate-limit-quota`

1. Set rate limit quotas for sub-accounts. This endpoint allows master accounts to allocate rate limit quotas for spot and futures trading at the sub-account level.

2. Supports single or batch quota allocation for multiple sub-accounts by business line.

3. The single account rate limit Quota must not exceed the single account rate limit Cap.

4. The sum of all sub-account rate limit Quotas (i.e., the Master-Sub Quota) must not exceed the Master-Sub total rate limit Cap.

5. If adjusting a sub-account's Quota causes the total Master-Sub Quota to exceed the Master-Sub Cap, the API call will be rejected.

6. This endpoint also supports being called directly by a sub-account using its own API Key, to set its own rate limit quota. The rules are the same as when called by the master account.

> **Note**: This endpoint is only available to **MM (Market Maker) and PRO** institutional users.

- Rate limit: 5/sec/UID

- Permission: UTA mgt. (read & write)

Operation ID: `utaUserRateLimitSetRateLimitQuota`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| category | string | 是 | Product type<br><br>`spot` Spot <br><br>`futures` Futures |
| uids | string[] | 是 | Sub-account UIDs<br><br>Up to 50 UIDs per request<br><br>Required when called by the master account; when called by a sub-account itself, this field is not required and is ignored |
| quota | string | 是 | Rate limit quota<br><br>Must not exceed the single account rate limit Cap |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data |  |  | Response data |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1753987234567,
  "data": "success"
}
```


---

设置与查询账户的机构限频配额。

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v3/user/rate-limit-quota` — 获取限频配额
- `POST /api/v3/user/set-rate-limit-quota` — 设置限频配额

## 获取限频配额

`GET /api/v3/user/rate-limit-quota`

查询账户限频配额配置。支持查询单个账户的额度分配情况，或列出母账户下所有子账户的限频配额。

该接口现已支持子账号使用自身API Key直接调用，查询子账号自身的限频配额。

> **注意**：该接口仅对 **MM（做市商）和 PRO** 机构用户开放。

- 限频规则: 10次/秒/UID

- 权限：统一账户管理 — 只读

Operation ID: `utaUserRateLimitGetRateLimitQuota`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| category | query | string | 是 | 业务线<br><br>`spot` 现货<br><br>`futures` 合约 |
| uid | query | string |  | 账户UID<br><br>用于单个账户限频配额查询；不填则列出所有子账户<br><br>子账号自行调用时该字段非必填，会被忽略，直接返回该子账号自身的限频配额 |
| cursor | query | string |  | 游标<br><br>后续查询的页码游标 |
| limit | query | string |  | 每页条目数<br><br>默认值：`100`，最大值：`100` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.category | string |  | 业务线<br><br>`spot` 现货<br><br>`futures` 合约 |
| data.quotaList | object[] |  | 子账户限频配额列表 |
| data.quotaList[].uid | string |  | 账户UID |
| data.quotaList[].quota | string |  | 单账户限频实际设置值 |
| data.masterSubQuota | string |  | 母子账户限频实际设置值 |
| data.masterSubCap | string |  | 母子账户限频硬顶 |
| data.cursor | string |  | 游标<br><br>后续查询的页码游标 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1753987234567,
  "data": {
    "category": "futures",
    "quotaList": [
      {
        "uid": "123456",
        "quota": "100"
      }
    ],
    "masterSubQuota": "10000",
    "masterSubCap": "80000",
    "cursor": "1"
  }
}
```

## 设置限频配额

`POST /api/v3/user/set-rate-limit-quota`

1. 设置子账户限频配额。该接口支持母账户为子账户设定现货与合约交易的独立限频额度。

2. 该接口支持按照业务线维度的单个或批量账户额度分配。

3. 单账户限频Quota数值不得超过单账户限频Cap，否则接口报错

4. 所有子账户的单账户限频Quota总和（即母子账户限频Quota）不得超过母子账户总限频硬顶Cap。

5. 如果调整某账户限频Quota后，母子账户限频Quota超出母子账户硬顶Cap，则当次接口调用不会成功

6. 该接口现已支持子账号使用自身API Key直接调用，自行设置机构限频配额，规则与母账号设置相同。

> **注意**：该接口仅对 **MM（做市商）和 PRO** 机构用户开放。

- 限频规则: 5次/秒/UID

- 权限：统一账户管理 — 读写

Operation ID: `utaUserRateLimitSetRateLimitQuota`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| category | string | 是 | 业务线<br><br>`spot` 现货<br><br>`futures` 合约 |
| uids | string[] | 是 | 子账户UID<br><br>单次最多可传 50 个 UID<br><br>母账号调用时必填；子账号调用时该字段非必填，会被忽略 |
| quota | string | 是 | 限频额度<br><br>额度不得超过单账户限频 Cap |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data |  |  | Response data |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1753987234567,
  "data": "success"
}
```