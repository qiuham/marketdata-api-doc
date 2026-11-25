---
exchange: bitget
source_url: https://www.bitget.com/docs/catalog/classic-broker-apikey
api_type: REST
updated_at: 2026-11-25 19:02:28.022644
---

# Classic Broker API Key API

Classic account — broker subaccount API key management.

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `POST /api/v2/broker/manage/create-subaccount-apikey` — Create Subaccount ApiKey
- `POST /api/v2/broker/manage/delete-subaccount-apikey` — Delete Subaccount ApiKey
- `GET /api/v2/broker/manage/subaccount-apikey-list` — Get Subaccount Apikey
- `POST /api/v2/broker/manage/modify-subaccount-apikey` — Modify Subaccount ApiKey

## Create Subaccount ApiKey

`POST /api/v2/broker/manage/create-subaccount-apikey`

Frequency limit:10 times/1s (User ID)

Only applicable for ND broker main-account

Create ApiKey for the specified subaccount

Operation ID: `classicBrokerApikeyCreateSubaccountApiKey`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subUid | string | 是 | Sub account UID |
| passphrase | string | 是 | Passphrase, length between 6 and 32 |
| label | string | 是 | remark, length < 20 |
| ipList | string[] | 是 | IP whitelist, max 30 IP entries<br><br>it's optional when `permType` is `readonly` |
| permType | string | 是 | Permission type<br><br>`read_and_write`<br><br>`readonly` |
| permList | string[] | 是 | Permission list<br><br>contract_order<br><br>contract_position<br><br>spot_trade<br><br>margin_trade: spot margin trade<br><br>copytrading_trade<br><br>wallet_transfer: `permType` should be `read_and_write` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.subUid | string |  | Sub account UID |
| data.label | string |  | apikey remark |
| data.apiKey | string |  | API key |
| data.secretKey | string |  | Secret key |
| data.permType | string |  | Permission type<br><br>read_and_write<br><br>readonly |
| data.permList | string[] |  | Permission list<br><br>contract_order<br><br>contract_position<br><br>spot_trade<br><br>margin_trade: spot margin trade<br><br>copytrading_trade<br><br>wallet_transfer: permType should be 'read_and_write' |
| data.ipList | string[] |  | IP whitelist |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695785738672,
  "data": {
    "subUid": "1",
    "apiKey": "xx_xxx",
    "secretKey": "xxxxxx",
    "label": " old remark ",
    "ipList": [
      "127.0.0.1"
    ],
    "permType": "readonly",
    "permList": [
      "spot_trade"
    ]
  }
}
```

## Delete Subaccount ApiKey

`POST /api/v2/broker/manage/delete-subaccount-apikey`

Frequency limit:10 times/1s (User ID)

Only applicable for ND broker main-account

Delete ApiKey for the specified subaccount

Operation ID: `classicBrokerApikeyDeleteSubaccountApiKey`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subUid | string | 是 | Sub account UID |
| apiKey | string | 是 | API Key |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string |  | success: delete successed |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1739774869632,
  "data": "success"
}
```

## Get Subaccount Apikey

`GET /api/v2/broker/manage/subaccount-apikey-list`

Frequency limit:10 times/1s (User ID)

Only applicable for ND broker main-account

Operation ID: `classicBrokerApikeySubaccountApikeyList`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| subUid | query | string | 是 | Sub account UID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].subUid | string |  | Sub account UID |
| data[].label | string |  | apikey remark |
| data[].apiKey | string |  | apikey |
| data[].secretKey | string |  | Secret key |
| data[].permType | string |  | Permission type:<br><br>read_and_write<br><br>readonly |
| data[].permList | string[] |  | Permission list:<br><br>contract_order<br><br>contract_position<br><br>spot_trade<br><br>margin_trade: spot margin trade<br><br>copytrading_trade<br><br>wallet_transfer: permType should be 'read_and_write' |
| data[].ipList | string[] |  | IP whitelist |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695786824200,
  "data": [
    {
      "subUid": "************",
      "label": " old remark ",
      "apiKey": "bg_********************",
      "secretKey": "xxxxxx",
      "permType": "readonly",
      "permList": [
        "spot_trade"
      ],
      "ipList": [
        "127.0.0.1"
      ]
    }
  ]
}
```

## Modify Subaccount ApiKey

`POST /api/v2/broker/manage/modify-subaccount-apikey`

Rate limit:  10 req/sec/UID

Only applicable for ND broker main-account to modify ApiKey for the specified sub-account

Operation ID: `classicBrokerApikeyModifySubaccountApiKey`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subUid | string | 是 | Sub account UID |
| apiKey | string | 是 | Sub account API Key |
| label | string |  | remark, length < 20 |
| passphrase | string | 是 | Passphrase, please recreate if forgot |
| ipList | string[] |  | IP whitelist, override, max 30 IP entries. Empty means no change |
| permType | string | 是 | Permission type, override. Empty means no change<br><br>`read_and_write`: read and write<br><br>`readonly`: read only |
| permList | string[] | 是 | Permission list, override. Empty means not change<br><br>`contract_order`: contract orders<br><br>`contract_position`: contract positions<br><br>`spot_trade`: spot trade<br><br>`margin_trade`: spot margin trade<br><br>`copytrading_trade`: copy trading trade<br><br>`wallet_transfer`: wallet transfer(available when `permType` is `read_and_write`) |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.subUid | string |  | Sub account UID |
| data.label | string |  | apikey remark |
| data.apiKey | string |  | apikey |
| data.permType | string |  | Permission type<br><br>read_and_write<br><br>readonly |
| data.permList | string[] |  | Permission list<br><br>contract_order<br><br>contract_position<br><br>spot_trade<br><br>margin_trade: spot margin trade<br><br>copytrading_trade<br><br>wallet_transfer: permType should be 'read_and_write' |
| data.ipList | string[] |  | IP whitelist |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695785738672,
  "data": {
    "subUid": "*********",
    "apiKey": "bg_**********************",
    "label": "old remark",
    "ipList": [
      "127.0.0.1"
    ],
    "permType": "readonly",
    "permList": [
      "spot_trade"
    ]
  }
}
```


---

经典账户 — 经纪商子账户 API Key 管理。

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `POST /api/v2/broker/manage/create-subaccount-apikey` — 创建子账户API key
- `POST /api/v2/broker/manage/delete-subaccount-apikey` — 删除子账户API key
- `GET /api/v2/broker/manage/subaccount-apikey-list` — 获取子账户API key 列表
- `POST /api/v2/broker/manage/modify-subaccount-apikey` — 修改子账户API key权限

## 创建子账户API key

`POST /api/v2/broker/manage/create-subaccount-apikey`

限速规则 10次/1s (UID)

独立经纪商母账户创建子账户ApiKey ，仅限主账户请求

Operation ID: `classicBrokerApikeyCreateSubaccountApiKey`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subUid | string | 是 | 子账户uid |
| passphrase | string | 是 | Passphrase 是调用 API 接口的必要参数，如果遗失请重新创建API key |
| label | string | 是 | 备注 |
| ipList | string[] | 是 | IP数组，最多传入30个<br><br>当`permType`为`readonly`时为非必填 |
| permType | string | 是 | 权限类型：<br><br>read_and_write 读写权限<br><br>readonly 只读权限 |
| permList | string[] | 是 | 选择只读权限类型时传入钱包提币无效，提币没有只读权限<br><br>权限数组，权限枚举：<br><br>contract_order 合约订单<br><br>contract_position 合约持仓<br><br>spot_trade 现货交易<br><br>margin_trade 现货杠杆交易<br><br>copytrading_trade 跟单交易<br><br>wallet_transfer 钱包划转(`permType`需要为`read_and_write`类型) |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.subUid | string |  | 子账户uid |
| data.label | string |  | apikey备注 |
| data.apiKey | string |  | API key |
| data.secretKey | string |  | 私钥 |
| data.permType | string |  | 权限类型：<br><br>read_and_write 读写权限<br><br>readonly 只读权限 |
| data.permList | string[] |  | 权限数组，权限枚举：<br><br>contract_order 合约订单<br><br>contract_position 合约持仓<br><br>spot_trade 现货交易<br><br>margin_trade 现货杠杆交易<br><br>copytrading_trade 跟单交易<br><br>wallet_transfer 钱包划转 |
| data.ipList | string[] |  | IP数组 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695785738672,
  "data": {
    "subUid": "************",
    "apiKey": "bg_****************",
    "secretKey": "xxxxxx",
    "label": " old remark ",
    "ipList": [
      "127.0.0.1"
    ],
    "permType": "readonly",
    "permList": [
      "spot_trade"
    ]
  }
}
```

## 删除子账户API key

`POST /api/v2/broker/manage/delete-subaccount-apikey`

限速规则 3次/1s (UID)

独立经纪商母账户删除子账户ApiKey ，仅限主账户请求

Operation ID: `classicBrokerApikeyDeleteSubaccountApiKey`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subUid | string | 是 | 子账户uid |
| apiKey | string | 是 | API key |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string |  | success: 删除成功 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1739774869632,
  "data": "success"
}
```

## 获取子账户API key 列表

`GET /api/v2/broker/manage/subaccount-apikey-list`

限速规则 10次/1s (UID)

独立经纪商母账户获取子账户ApiKey 信息

Operation ID: `classicBrokerApikeySubaccountApikeyList`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| subUid | query | string | 是 | 子账户uid |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].subUid | string |  | 子账户uid |
| data[].label | string |  | apikey备注 |
| data[].apiKey | string |  | apikey |
| data[].secretKey | string |  | 私钥 |
| data[].permType | string |  | 权限类型：<br><br>read_and_write 读写权限<br><br>readonly 只读权限 |
| data[].permList | string[] |  | 权限数组，权限枚举：<br><br>contract_order 合约订单<br><br>contract_position 合约持仓<br><br>spot_trade 现货交易<br><br>margin_trade 现货杠杆交易<br><br>copytrading_trade 跟单交易<br><br>wallet_transfer 钱包划转 |
| data[].ipList | string[] |  | IP数组 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695786824200,
  "data": [
    {
      "subUid": "***********",
      "label": " old remark ",
      "apiKey": "bg_**********************",
      "secretKey": "xxxxxx",
      "permType": "readonly",
      "permList": [
        "spot_trade"
      ],
      "ipList": [
        "127.0.0.1"
      ]
    }
  ]
}
```

## 修改子账户API key权限

`POST /api/v2/broker/manage/modify-subaccount-apikey`

限速规则 10次/1s (UID)

独立经纪商母账户修改子账户API key权限，仅限主账户请求

Operation ID: `classicBrokerApikeyModifySubaccountApiKey`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subUid | string | 是 | 子账户uid |
| apiKey | string | 是 | 子账户apikey |
| label | string |  | 备注 |
| passphrase | string | 是 | 创建API key时的传入的口令，如果忘记passphrase请重新创建API key |
| ipList | string[] |  | IP数组，新传入IP组会覆盖旧的IP组，最多传入30个；不传则视为不变 |
| permType | string | 是 | 新增权限组会覆盖旧权限组，不传则视为不变<br><br>权限类型：<br><br>`read_and_write`: 读写权限<br><br>`readonly`: 只读权限 |
| permList | string[] |  | 新增权限组会覆盖旧权限组，不传则视为不变<br><br>权限枚举：<br><br>`contract_order`: 合约订单<br><br>`contract_position`: 合约持仓<br><br>`spot_trade`: 现货交易<br><br>`margin_trade`: 现货杠杆交易<br><br>`copytrading_trade`: 跟单交易<br><br>`wallet_transfer`: 钱包划转 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.subUid | string |  | 子账户uid |
| data.label | string |  | apikey备注 |
| data.apiKey | string |  | apikey |
| data.permType | string |  | 权限类型：<br><br>read_and_write 读写权限<br><br>readonly 只读权限 |
| data.permList | string[] |  | 权限枚举：<br><br>`contract_order`: 合约订单<br><br>`contract_position`: 合约持仓<br><br>`spot_trade`: 现货交易<br><br>`margin_trade`: 现货杠杆交易<br><br>`copytrading_trade`: 跟单交易<br><br>`wallet_transfer`: 钱包划转 |
| data.ipList | string[] |  | IP数组 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695785738672,
  "data": {
    "subUid": "*************",
    "apiKey": "bg_*****************",
    "label": "old remark",
    "ipList": [
      "127.0.0.1"
    ],
    "permType": "readonly",
    "permList": [
      "spot_trade"
    ]
  }
}
```