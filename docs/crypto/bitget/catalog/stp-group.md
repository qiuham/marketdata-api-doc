---
exchange: bitget
source_url: https://www.bitget.com/docs/catalog/stp-group
api_type: REST
updated_at: 2026-11-18 08:38:29.421835
---

# STP Group

Create and manage Self-Trade Prevention (STP) groups for sub-accounts. Only available to MM (Market Maker) whitelist users under the Unified Trading Account.

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `POST /api/v3/account/create-stp-groups` — Create STP Group
- `GET /api/v3/account/stp-groups` — Get STP Group List
- `POST /api/v3/account/add-groups-members` — Add STP Group Members
- `POST /api/v3/account/remove-groups-members` — Remove STP Group Members

## Create STP Group

`POST /api/v3/account/create-stp-groups`

Create a custom Self-Trade Prevention (STP) group. Sub-accounts within the same group will not match against each other; sub-accounts in different groups can trade with each other normally.

> **Note**: This endpoint is only available to **MM (Market Maker)** whitelist users.

- Rate limit: 20/sec/UID

- Permission: UTA mgt. (read & write)

Operation ID: `utaAccountCreateStpGroup`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| groupName | string | 是 | STP Group name<br><br>Max 32 characters, must be unique |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.groupId | string |  | STP Group ID (system-generated numeric ID) |
| data.groupName | string |  | STP Group name |
| data.createdTime | string |  | Creation time, Unix millisecond timestamp |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1729760000000.0,
  "data": {
    "groupId": "1001",
    "groupName": "Team-A",
    "createdTime": "1729760000000"
  }
}
```

## Get STP Group List

`GET /api/v3/account/stp-groups`

Query the custom STP Group list and member sub-accounts under the current master account.

> **Note**: This endpoint is only available to **MM (Market Maker)** whitelist users.

- Rate limit: 20/sec/UID

- Permission: UTA mgt. (read)

Operation ID: `utaAccountGetStpGroupList`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.groups | object[] |  | STP Group list |
| data.groups[].groupId | string |  | STP Group ID |
| data.groups[].groupName | string |  | STP Group name |
| data.groups[].createdTime | string |  | Creation time, Unix millisecond timestamp |
| data.groups[].members | object[] |  | Member list |
| data.groups[].members[].uid | string |  | Sub-account UID |
| data.groups[].members[].joinedTime | string |  | Time joined, Unix millisecond timestamp |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1729760000000.0,
  "data": {
    "groups": [
      {
        "groupId": "1001",
        "groupName": "Team-A",
        "createdTime": "1729760000000",
        "members": [
          {
            "uid": "1122334455",
            "joinedTime": "1729760100000"
          }
        ]
      }
    ]
  }
}
```

## Add STP Group Members

`POST /api/v3/account/add-groups-members`

Add sub-accounts to an existing STP Group. Each sub-account can only belong to one STP Group; adding a sub-account to a new group automatically removes it from its previous group.

> **Note**: This endpoint is only available to **MM (Market Maker)** whitelist users.

- Rate limit: 20/sec/UID

- Permission: UTA mgt. (read & write)

Operation ID: `utaAccountAddStpGroupMembers`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| uids | string | 是 | Sub-account UIDs to add to the group<br><br>Max 50 per call; can only add sub-accounts under this master account. Multiple UIDs separated by commas. |
| groupId | string | 是 | STP Group ID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.createdTime | string |  | Creation time, Unix millisecond timestamp |
| data.successUids | object[] |  | Successfully added UID list |
| data.successUids[].uid | string |  | Successfully added UID |
| data.failedUids | object[] |  | Failed UID list |
| data.failedUids[].uid | string |  | Failed UID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1729760000000.0,
  "data": {
    "createdTime": "1729760000000",
    "successUids": [
      {
        "uid": "1122334455"
      }
    ],
    "failedUids": []
  }
}
```

## Remove STP Group Members

`POST /api/v3/account/remove-groups-members`

Remove sub-accounts from an STP Group. After removal, a sub-account reverts to the default behavior (stp_uid = parent_uid).

> **Note**: This endpoint is only available to **MM (Market Maker)** whitelist users.

- Rate limit: 20/sec/UID

- Permission: UTA mgt. (read & write)

Operation ID: `utaAccountRemoveStpGroupMembers`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| uids | string | 是 | Sub-account UIDs to remove from the group<br><br>Max 50 per call; can only remove sub-accounts currently in this STP Group. Multiple UIDs separated by commas. |
| groupId | string | 是 | STP Group ID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.createdTime | string |  | Creation time, Unix millisecond timestamp |
| data.successUids | object[] |  | Successfully removed UID list |
| data.successUids[].uid | string |  | Successfully removed UID |
| data.failedUids | object[] |  | Failed removed UID list |
| data.failedUids[].uid | string |  | Failed removed UID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1729760000000.0,
  "data": {
    "createdTime": "1729760000000",
    "successUids": [
      {
        "uid": "1122334455"
      }
    ],
    "failedUids": []
  }
}
```


---

创建和管理子账户自成交预防（STP）分组。仅做市商（MM）白名单用户在统一账户下可用。

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `POST /api/v3/account/create-stp-groups` — 创建 STP 分组
- `GET /api/v3/account/stp-groups` — 查询 STP 分组列表
- `POST /api/v3/account/add-groups-members` — 添加 STP 分组成员
- `POST /api/v3/account/remove-groups-members` — 移除 STP 分组成员

## 创建 STP 分组

`POST /api/v3/account/create-stp-groups`

创建自定义自成交预防（STP）分组。同一分组内的子账户之间不会相互撮合；不同分组的子账户可以正常互相交易。

> **注意**：该接口仅对 **MM（做市商）** 白名单用户开放。

- 限频规则: 20次/秒/UID

- 权限：统一账户管理 — 读写

Operation ID: `utaAccountCreateStpGroup`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| groupName | string | 是 | STP Group 名称<br><br>最长 32 个字符，需唯一 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.groupId | string |  | STP Group ID（系统自动生成的数字 ID） |
| data.groupName | string |  | STP Group 名称 |
| data.createdTime | string |  | 创建时间，Unix 毫秒时间戳 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1729760000000.0,
  "data": {
    "groupId": "1001",
    "groupName": "Team-A",
    "createdTime": "1729760000000"
  }
}
```

## 查询 STP 分组列表

`GET /api/v3/account/stp-groups`

查询当前母账户下的自定义 STP Group 列表及成员子账户。

> **注意**：该接口仅对 **MM（做市商）** 白名单用户开放。

- 限频规则: 20次/秒/UID

- 权限：统一账户管理 — 只读

Operation ID: `utaAccountGetStpGroupList`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.groups | object[] |  | STP Group 列表 |
| data.groups[].groupId | string |  | STP Group ID |
| data.groups[].groupName | string |  | STP Group 名称 |
| data.groups[].createdTime | string |  | 创建时间，Unix 毫秒时间戳 |
| data.groups[].members | object[] |  | 成员列表 |
| data.groups[].members[].uid | string |  | 子账户 UID |
| data.groups[].members[].joinedTime | string |  | 加入时间，Unix 毫秒时间戳 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1729760000000.0,
  "data": {
    "groups": [
      {
        "groupId": "1001",
        "groupName": "Team-A",
        "createdTime": "1729760000000",
        "members": [
          {
            "uid": "1122334455",
            "joinedTime": "1729760100000"
          }
        ]
      }
    ]
  }
}
```

## 添加 STP 分组成员

`POST /api/v3/account/add-groups-members`

将子账户添加到已有的 STP Group。每个子账户只能属于一个 STP Group；将子账户加入新 Group 时会自动退出原 Group。

> **注意**：该接口仅对 **MM（做市商）** 白名单用户开放。

- 限频规则: 20次/秒/UID

- 权限：统一账户管理 — 读写

Operation ID: `utaAccountAddStpGroupMembers`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| uids | string | 是 | 要加入 Group 的子账户 UID 列表<br><br>单次最多 50 个；只能添加本母账户下的子账户。多个 UID 之间逗号分隔。 |
| groupId | string | 是 | STP Group ID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.createdTime | string |  | 创建时间，Unix 毫秒时间戳 |
| data.successUids | object[] |  | 成功加入的 UID 列表 |
| data.successUids[].uid | string |  | 成功加入的 UID |
| data.failedUids | object[] |  | 失败的 UID 列表 |
| data.failedUids[].uid | string |  | 失败的 UID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1729760000000.0,
  "data": {
    "createdTime": "1729760000000",
    "successUids": [
      {
        "uid": "1122334455"
      }
    ],
    "failedUids": []
  }
}
```

## 移除 STP 分组成员

`POST /api/v3/account/remove-groups-members`

将子账户从 STP Group 中移除。移除后，子账户回退到默认行为（stp_uid = parent_uid）。

> **注意**：该接口仅对 **MM（做市商）** 白名单用户开放。

- 限频规则: 20次/秒/UID

- 权限：统一账户管理 — 读写

Operation ID: `utaAccountRemoveStpGroupMembers`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| uids | string | 是 | 要移除的子账户 UID 列表<br><br>单次最多 50 个；只能移除当前 STP 组内的子账户。多个 UID 之间逗号分隔。 |
| groupId | string | 是 | STP Group ID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.createdTime | string |  | 创建时间，Unix 毫秒时间戳 |
| data.successUids | object[] |  | 成功移除的 UID 列表 |
| data.successUids[].uid | string |  | 成功移除的 UID |
| data.failedUids | object[] |  | 失败移除的 UID 列表 |
| data.failedUids[].uid | string |  | 失败移除的 UID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1729760000000.0,
  "data": {
    "createdTime": "1729760000000",
    "successUids": [
      {
        "uid": "1122334455"
      }
    ],
    "failedUids": []
  }
}
```