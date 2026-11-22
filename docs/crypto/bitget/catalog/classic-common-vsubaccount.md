---
exchange: bitget
source_url: https://www.bitget.com/docs/catalog/classic-common-vsubaccount
api_type: REST
updated_at: 2026-11-22 19:01:00.600607
---

# Classic Virtual Subaccount API

Public virtual sub-account endpoints — create, modify, and query virtual sub-accounts and API keys.

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `POST /api/v2/user/create-virtual-subaccount` — Create Virtual Subaccount
- `POST /api/v2/user/batch-create-subaccount-and-apikey` — Batch Create Virtual Subaccount and Apikey
- `POST /api/v2/user/create-virtual-subaccount-apikey` — Create Virtual Subaccount Apikey
- `POST /api/v2/user/modify-virtual-subaccount` — Modify Virtual Subaccount
- `POST /api/v2/user/modify-virtual-subaccount-apikey` — Modify Virtual Subaccount Apikey
- `GET /api/v2/user/virtual-subaccount-list` — Get Virtual Subaccounts
- `GET /api/v2/user/virtual-subaccount-apikey-list` — Get Subaccount Apikey List
- `POST /api/v2/user/create-agent-subaccount` — Create Agent Subaccount

## Create Virtual Subaccount

`POST /api/v2/user/create-virtual-subaccount`

Frequency limit: 5 times/1s (User ID)

This interface currently supports the creation of virtual sub-accounts in batch.(It's required API key binding IP address)

Operation ID: `classicCommonVsubaccountCreateVirtualSubaccount`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subAccountList | string[] | 是 | Virtual alias 8-character English letters,Global unique |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.failureList | object[] |  | Sub-account array creation failed<br><br>- Alias already exists<br><br>- The number of sub-accounts created has reached the limit |
| data.successList | object[] |  | Sub-account array created successfully |
| data.successList[].subaAccountUid | string |  | Sub-account uid |
| data.successList[].subaAccountName | string |  | Sub-account name |
| data.successList[].status | string |  | Sub-account status<br><br>normal Normal<br><br>freeze Freeze<br><br>del Deleted |
| data.successList[].permList | string[] |  | Sub-account permissions<br><br>spot_trade Spot trade<br><br>contract_trade Futures trade read-write<br><br>read Read permissions |
| data.successList[].label | string |  | Note |
| data.successList[].cTime | string |  | Sub-account creation time, Unix millisecond timestamps. |
| data.successList[].uTime | string |  | Sub-account update time, Unix millisecond timestamps. |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1682660169412,
  "data": {
    "failureList": [
      {
        "subaAccountName": "****@*****.com"
      }
    ],
    "successList": [
      {
        "subaAccountUid": "**********",
        "subaAccountName": "****@*****.com",
        "status": "normal",
        "label": "",
        "permList": [
          "contract_trade",
          "spot_trade"
        ],
        "cTime": "1682660169573",
        "uTime": "1682660169573"
      }
    ]
  }
}
```

## Batch Create Virtual Subaccount and Apikey

`POST /api/v2/user/batch-create-subaccount-and-apikey`

Frequency limit: 1 times/1s (User ID)

Create the virtual sub-account and apikey in batch. (It's required API key binding IP address)

- The max length of list is 5 in each request.

- Every sub-account can create up to 10 API Key

- You can create up to 20 sub-accounts.

Operation ID: `classicCommonVsubaccountBatchCreateVirtualSubaccountAndApikey`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subAccountName | string | 是 | Virtual sub-account alias8-character English letters |
| passphrase | string | 是 | Passcode English letters of 8-32 characters + numbers |
| label | string | 是 | Sub-account note Length 20 |
| ipList | string[] |  | Virtual sub-account ApiKey ip whitelist, Max. 30 |
| permList | string[] | 是 | Sub-account permissions<br><br>`spot_trade`: Spot trade<br><br>`margin_trade`: Spot Marign trade<br><br>`contract_trade`: Futures trade read-write<br><br>`read`: Read permissions |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].subAccountUid | string |  | Virtual sub-account Uid |
| data[].subAccountName | string |  | Virtual sub-account alias8-character English letters |
| data[].label | string |  | Sub-account noteLength 20 |
| data[].subAccountApiKey | string |  | Sub-account apikey |
| data[].secretKey | string |  | Sub-account secret key |
| data[].permList | string[] |  | Sub-account permissions<br><br>`spot_trade`: Spot trade<br><br>`margin_trade`: Spot Marign trade<br><br>`contract_trade`: Futures trade read-write<br><br>`read`: Read permissions |
| data[].ipList | string[] |  | ip whitelist |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1682662465346,
  "data": [
    {
      "subAccountUid": "***********",
      "subAccountName": "*****@*******.com",
      "label": "1681808312065",
      "subAccountApiKey": "xx_xxx",
      "secretKey": "XXXXXXXXXXXXXXX",
      "permList": [
        "spot_trade",
        "margin_trade",
        "contract_trade"
      ],
      "ipList": [
        "127.0.0.1"
      ]
    }
  ]
}
```

## Create Virtual Subaccount Apikey

`POST /api/v2/user/create-virtual-subaccount-apikey`

Frequency limit: 5 times/1s (User ID)

Only supports API Key calls from the main account, and the API Key needs to be bound to an IP address.

Create the virtual sub-account apikey

Operation ID: `classicCommonVsubaccountCreateVirtualSubaccountApikey`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subAccountUid | string | 是 | Sub-account uid |
| passphrase | string | 是 | Passcode English letters of 8-32 characters + numbers |
| label | string | 是 | Note Length 20 |
| ipList | string[] |  | ip whitelist<br><br>Up to 30, if not then ip whitelist is set to empty. |
| permList | string[] | 是 | Sub-account permissions<br><br>`spot_trade`: Spot trade<br><br>`margin_trade`: Spot Marign trade<br><br>`contract_trade`: Futures trade read-write<br><br>`transfer`:Wallet transfer<br><br> `read`: Read permissions |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.subAccountUid | string |  | Sub-account uid |
| data.subAccountApiKey | string |  | Sub-account apikey |
| data.secretKey | string |  | Sub-account private key |
| data.permList | string[] |  | Sub-account permissions<br><br>`spot_trade`: Spot trade<br><br>`margin_trade`: Spot Marign trade<br><br>`contract_trade`: Futures trade read-write<br><br>`transfer`:Wallet transfer<br><br>`read`: Read permissions |
| data.label | string |  | Sub-account apikey note |
| data.ipList | string[] |  | ip whitelist |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1682660169412,
  "data": {
    "subAccountUid": "1",
    "label": "test1_account",
    "subAccountApiKey": "xx_xxx",
    "secretKey": "xxx",
    "permList": [
      "spot_trade"
    ],
    "ipList": [
      "127.0.0.1"
    ]
  }
}
```

## Modify Virtual Subaccount

`POST /api/v2/user/modify-virtual-subaccount`

Frequency limit: 5 times/1s (User ID)

Modify the virtual sub-account. (It's required API key binding IP address)

Operation ID: `classicCommonVsubaccountModifyVirtualSubaccount`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subAccountUid | string | 是 | Sub-account Uid |
| permList | string[] | 是 | Permissions<br><br>spot_trade Spot trade<br><br>contract_trade Futures trade read-write<br><br>read Read permissions |
| status | string | 是 | Sub-account status<br><br>normal Normal<br><br>freeze Freeze |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.result | string |  | Edit result<br><br>`success` Success<br><br>`failure` Failure |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1682660666458,
  "data": {
    "result": "success"
  }
}
```

## Modify Virtual Subaccount Apikey

`POST /api/v2/user/modify-virtual-subaccount-apikey`

Frequency limit: 5 times/1s (User ID)

Only supports API Key calls from the main account, and the API Key needs to be bound to an IP address

Modify the virtual sub-account or general sub-account API Key

Operation ID: `classicCommonVsubaccountModifyVirtualSubaccountApikey`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subAccountUid | string | 是 | Sub-account uid |
| passphrase | string | 是 | Passcode English letters of 8-32 characters + numbers |
| label | string | 是 | Note Length 20 |
| ipList | string[] |  | ip whitelist<br><br>Up to 30, if not then ip whitelist is set to empty. |
| permList | string[] |  | Sub-account permissions<br><br>`spot_trade`: Spot trade<br><br>`margin_trade`: Spot Marign trade<br><br>`contract_trade`: Futures trade read-write<br><br>`transfer`:Wallet transfer<br><br>`read`: Read permissions<br><br>If this parameter is not passed, it will be ignored, and the existing permissions will be retained<br><br>If an empty value is passed, the existing permissions of this API Key will be removed |
| subAccountApiKey | string | 是 | Sub-account ApiKey |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.subAccountUid | string |  | Sub-account uid |
| data.subAccountApiKey | string |  | Sub-account apikey |
| data.secretKey | string |  | secretKey |
| data.permList | string[] |  | Sub-account permissions<br><br>`spot_trade`: Spot trade<br><br>`margin_trade`: Spot Marign trade<br><br>`contract_trade`: Futures trade read-write<br><br>`transfer`:Wallet transfer<br><br>`read`: Read permissions |
| data.label | string |  | Sub-account apikey note |
| data.ipList | string[] |  | Sub-account apikey ip whitelist |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1682660169412,
  "data": {
    "subAccountUid": "1",
    "label": "sub api",
    "subAccountApiKey": "xx_xxx",
    "secretKey": "xxx",
    "permList": [
      "spot_trade",
      "contract_trade"
    ],
    "ipList": [
      "127.0.0.1"
    ]
  }
}
```

## Get Virtual Subaccounts

`GET /api/v2/user/virtual-subaccount-list`

Rate limit: 1 req/sec/UID

Get a list of virtual sub-account. (It's required API key binding IP address)

Operation ID: `classicCommonVsubaccountGetVirtualSubaccountList`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| limit | query | string |  | Entries per page<br><br>Default: 100, maximum: 500 |
| idLessThan | query | string |  | Final sub-account ID, required for paging. |
| status | query | string |  | Sub-account status<br><br>normal Normal<br><br>freeze Freeze |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.subAccountList | object[] |  | Sub-account array |
| data.subAccountList[].subAccountUid | string |  | Sub-account uid |
| data.subAccountList[].subAccountName | string |  | Sub-account username |
| data.subAccountList[].label | string |  | Sub-account ApiKey note, max length 20 |
| data.subAccountList[].status | string |  | Sub-account status<br><br>normal Normal<br><br>freeze Freeze<br><br>del Deleted |
| data.subAccountList[].permList | string[] |  | Sub-account permissions<br><br>spot_trade Spot trade<br><br>contract_trade Futures trade read-write<br><br>read Read permissions |
| data.subAccountList[].cTime | string |  | Sub-account creation time |
| data.subAccountList[].uTime | string |  | Sub-account update time |
| data.endId | string |  | This is used when idLessThan/idGreaterThan is set as a range. |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1656589586807,
  "data": {
    "endId": "51",
    "subAccountList": [
      {
        "subAccountUid": "********",
        "subAccountName": "****@*****.com",
        "status": "normal",
        "permList": [
          "read",
          "spot_trade",
          "contract_trade"
        ],
        "label": "mySub01",
        "cTime": "1653287983475",
        "uTime": "1682660169573"
      }
    ]
  }
}
```

## Get Subaccount Apikey List

`GET /api/v2/user/virtual-subaccount-apikey-list`

Rate Limit: 5 req/sec/UID

Only supports API Key calls from the main account, and the API Key needs to be bound to an IP address

Operation ID: `classicCommonVsubaccountGetVirtualSubaccountApikeyList`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| subAccountUid | query | string | 是 | Sub-account uid |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].subAccountUid | string |  | Sub-account uid |
| data[].subAccountApiKey | string |  | Sub-account ApiKey |
| data[].permList | string[] |  | Sub-account permissions<br><br>`spot_trade`: Spot trade<br><br>`margin_trade`: Spot Marign trade<br><br>`contract_trade`: Futures trade read-write<br><br>`transfer`:Wallet transfer<br><br>`read`: Read permissions |
| data[].label | string |  | Sub-account apikey note |
| data[].ipList | string[] |  | ip whitelist |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1682661432874,
  "data": [
    {
      "subAccountUid": "1",
      "label": "1682396356594",
      "subAccountApiKey": "xx_xxx",
      "permList": [
        "spot_trade",
        "margin_trade",
        "contract_trade"
      ],
      "ipList": [
        "127.0.0.1"
      ]
    }
  ]
}
```

## Create Agent Subaccount

`POST /api/v2/user/create-agent-subaccount`

Frequency limit: 1 times/1s (UID)

Create a dedicated sub-account for an AI Agent instance. Agent sub-accounts are not editable after creation (name, permissions, and other configurations cannot be modified). Each main account shares the total sub-account quota with regular sub-accounts.

Operation ID: `classicCommonVsubaccountCreateAgentSubaccount`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| username | string | 是 | Username used to generate the virtual email address. Only lowercase letters are allowed; maximum 20 characters |
| passphrase | string | 是 | API key passphrase. Must be 8-32 characters, consisting of letters and numbers |
| note | string |  | Sub-account note |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.username | string |  | Agent sub-account username |
| data.subUid | string |  | Agent sub-account ID |
| data.apiKey | string |  | Agent sub-account API key |
| data.secret | string |  | Agent sub-account secret |
| data.note | string |  | Note |
| data.createdTime | string |  | Creation time, Unix millisecond timestamp |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "username": "xxxx@virtual-bitget.com",
    "subUid": "xxxx",
    "apiKey": "***********************************",
    "secret": "*********************************************",
    "note": "xxxx",
    "createdTime": "1740211445041"
  }
}
```


---

公共虚拟子账户接口 —— 创建、修改与查询虚拟子账户及 API Key。

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `POST /api/v2/user/create-virtual-subaccount` — 创建虚拟子账户
- `POST /api/v2/user/batch-create-subaccount-and-apikey` — 批量创建虚拟子账户和apikey
- `POST /api/v2/user/create-virtual-subaccount-apikey` — 创建虚拟子账户Apikey
- `POST /api/v2/user/modify-virtual-subaccount` — 修改虚拟子账户
- `POST /api/v2/user/modify-virtual-subaccount-apikey` — 修改虚拟子账户Apikey
- `GET /api/v2/user/virtual-subaccount-list` — 查询子账户列表
- `GET /api/v2/user/virtual-subaccount-apikey-list` — 查询虚拟子账户Apikey列表
- `POST /api/v2/user/create-agent-subaccount` — 创建 Agent 子账户

## 创建虚拟子账户

`POST /api/v2/user/create-virtual-subaccount`

限速规则 5次/1s (UID)

该接口目前支持批量创建虚拟子账户（该接口需要API Key绑定IP地址才可调用）

Operation ID: `classicCommonVsubaccountCreateVirtualSubaccount`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subAccountList | string[] | 是 | 虚拟昵称 长度必须为8位的纯英文字母组合 全局唯一 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.failureList | object[] |  | 创建失败子账户数组<br><br>- 账户昵称存在重复<br><br>- 创建子账户创建数量达到限制 |
| data.successList | object[] |  | 创建成功子账户数组 |
| data.successList[].subaAccountUid | string |  | 子账户uid |
| data.successList[].subaAccountName | string |  | 子账户名称 |
| data.successList[].status | string |  | 子账户状态<br><br>normal 正常<br><br>freeze 冻结<br><br>del删除 |
| data.successList[].permList | string[] |  | 子账户权限<br><br>spot_trade 现货交易<br><br>contract_trade 合约交易读写<br><br>read read读取权限<br><br>子账户默认权限为spot_trade& contract_trade |
| data.successList[].label | string |  | 备注 |
| data.successList[].cTime | string |  | 子账户创建时间，Unix毫秒时间戳 |
| data.successList[].uTime | string |  | 子账户更新时间，Unix毫秒时间戳 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1682660169412,
  "data": {
    "failureList": [
      {
        "subaAccountName": "****@*****.com"
      }
    ],
    "successList": [
      {
        "subaAccountUid": "***********",
        "subaAccountName": "****@*****.com",
        "status": "normal",
        "label": "",
        "permList": [
          "contract_trade",
          "spot_trade"
        ],
        "cTime": "1682660169573",
        "uTime": "1682660169573"
      }
    ]
  }
}
```

## 批量创建虚拟子账户和apikey

`POST /api/v2/user/batch-create-subaccount-and-apikey`

限速规则 1次/1s (UID)

批量创建虚拟子账户和apikey（该接口需要API Key绑定IP地址才可调用）

- 每次请求的列表长度最大为5

- 每个虚拟子账户最多可创建10个API Key

- 每个账户默认最多可创建20个子账户

Operation ID: `classicCommonVsubaccountBatchCreateVirtualSubaccountAndApikey`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subAccountName | string | 是 | 虚拟子账户昵称 长度为8位的英文字母 |
| passphrase | string | 是 | 口令 长度为 8~32位的英文字母+数字 |
| label | string | 是 | 子账户备注 长度20 |
| ipList | string[] |  | 虚拟子账户ApiKey ip 白名单, 最大30 |
| permList | string[] | 是 | 子账户apiKey 权限<br><br>`spot_trade`: 现货交易<br><br>`margin_trade`: 现货杠杆交易<br><br>`contract_trade`: 合约交易读写<br><br>`read`:读取权限 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].subAccountUid | string |  | 虚拟子账户Uid |
| data[].subAccountName | string |  | 虚拟子账户昵称 长度为8位的英文字母 |
| data[].label | string |  | 子账户备注 长度为20位 |
| data[].subAccountApiKey | string |  | 子账户apikey |
| data[].secretKey | string |  | 子账户secret key |
| data[].permList | string[] |  | 子账户apiKey 权限<br><br>`spot_trade`: 现货交易<br><br>`margin_trade`: 现货杠杆交易<br><br>`contract_trade`: 合约交易读写<br><br>`read`:读取权限 |
| data[].ipList | string[] |  | ip白名单 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1682662465346,
  "data": [
    {
      "subAccountUid": "********",
      "subAccountName": "****@*****.com",
      "label": "1681808312065",
      "subAccountApiKey": "xx_xxx",
      "secretKey": "xx_xxx",
      "permList": [
        "contract_trade",
        "spot_trade"
      ],
      "ipList": [
        "127.0.0.1"
      ]
    }
  ]
}
```

## 创建虚拟子账户Apikey

`POST /api/v2/user/create-virtual-subaccount-apikey`

限速规则 5次/1s (UID)

仅支持主账户API Key调用，且API Key需要绑定IP地址

创建虚拟子账户API Key

Operation ID: `classicCommonVsubaccountCreateVirtualSubaccountApikey`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subAccountUid | string | 是 | 子账户UID |
| passphrase | string | 是 | 口令 长度为 8~32位的英文字母+数字 |
| label | string | 是 | 子账户备注 长度20 |
| ipList | string[] |  | 是否绑定ip，例如：1.1.1.1 |
| permList | string[] | 是 | 子账户apiKey 权限<br><br>`spot_trade`: 现货交易<br><br>`margin_trade`: 现货杠杆交易<br><br>`contract_trade`: 合约交易读写<br><br>`transfer`:钱包划转权限<br><br>`read`:读取权限 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.subAccountUid | string |  | 子账户UID |
| data.subAccountApiKey | string |  | 子账户Apikey |
| data.secretKey | string |  | 子账户secretKey |
| data.permList | string[] |  | 子账户apiKey 权限<br><br>`spot_trade`: 现货交易<br><br>`margin_trade`: 现货杠杆交易<br><br>`contract_trade`: 合约交易读写<br><br>`transfer`:钱包划转权限<br><br>`read`:读取权限 |
| data.label | string |  | 备注 |
| data.ipList | string[] |  | ip列表 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1682660169412,
  "data": {
    "subAccountUid": "1",
    "label": "test1_account",
    "subAccountApiKey": "xx_xxx",
    "secretKey": "xxx",
    "permList": [
      "contract_trade",
      "spot_trade"
    ],
    "ipList": [
      "127.0.0.1"
    ]
  }
}
```

## 修改虚拟子账户

`POST /api/v2/user/modify-virtual-subaccount`

限速规则 5次/1s (UID)

修改虚拟子账户（该接口需要API Key绑定IP地址才可调用）

Operation ID: `classicCommonVsubaccountModifyVirtualSubaccount`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subAccountUid | string | 是 | 子账号Uid |
| permList | string[] | 是 | 权限<br><br>spot_trade 现货交易<br><br>contract_trade 合约交易读写<br><br>read读取权限 |
| status | string | 是 | 子账号状态<br><br>normal 正常<br><br>freeze 冻结 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.result | string |  | 修改结果<br><br>success成功<br><br>failure失败 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1682660666458,
  "data": {
    "result": "success"
  }
}
```

## 修改虚拟子账户Apikey

`POST /api/v2/user/modify-virtual-subaccount-apikey`

限速规则 5次/1s (UID)

仅支持主账户API Key调用，且API Key需要绑定IP地址

支持修改虚拟子账户以及普通子账户的API Key

Operation ID: `classicCommonVsubaccountModifyVirtualSubaccountApikey`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subAccountUid | string | 是 | 子账户UID |
| passphrase | string | 是 | 口令 长度为 8~32位的英文字母+数字 |
| label | string | 是 | 子账户备注 长度20 |
| ipList | string[] |  | 是否绑定ip，例如：1.1.1.1 |
| permList | string[] |  | 子账户apiKey 权限<br><br>`spot_trade`: 现货交易<br><br>`margin_trade`: 现货杠杆交易<br><br>`contract_trade`: 合约交易读写<br><br>`transfer`:钱包划转权限<br><br>`read`:读取权限<br><br>如果该参数不传，则忽略该入参，保留现有权限<br><br>如果该传空值，则移除该API Key现有权限 |
| subAccountApiKey | string | 是 | 子账户Apikey |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.subAccountUid | string |  | 子账户UID |
| data.subAccountApiKey | string |  | 子账户Apikey |
| data.secretKey | string |  | 子账户secretKey |
| data.permList | string[] |  | 子账户apiKey 权限<br><br>`spot_trade`: 现货交易<br><br>`margin_trade`: 现货杠杆交易<br><br>`contract_trade`: 合约交易读写<br><br>`transfer`:钱包划转权限<br><br>`read`:读取权限 |
| data.label | string |  | 备注 |
| data.ipList | string[] |  | ip列表 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1682660169412,
  "data": {
    "subAccountUid": "1",
    "label": "sub api",
    "subAccountApiKey": "xx_xxx",
    "secretKey": "xxx",
    "permList": [
      "spot_trade",
      "contract_trade"
    ],
    "ipList": [
      "127.0.0.1"
    ]
  }
}
```

## 查询子账户列表

`GET /api/v2/user/virtual-subaccount-list`

限速规则 1次/1s (UID)

查询子账户列表（该接口需要API Key绑定IP地址才可调用）

Operation ID: `classicCommonVsubaccountGetVirtualSubaccountList`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| status | query | string |  | 子账户状态<br><br>normal<br><br>freeze<br><br>del |
| limit | query | string |  | 默认20 最大100 |
| idLessThan | query | string |  | 最后一条记录的ID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.subAccountList | object[] |  | 子账户列表 |
| data.subAccountList[].subAccountUid | string |  | 虚拟子账户Uid |
| data.subAccountList[].subAccountName | string |  | 虚拟子账户昵称 长度为8位的英文字母 |
| data.subAccountList[].label | string |  | 子账户备注 长度为20位 |
| data.subAccountList[].status | string |  | 子账户状态 |
| data.subAccountList[].permList | string[] |  | 子账户apiKey 权限<br><br>spot_trade 现货交易<br><br>contract_trade 合约交易读写<br><br>read read读取权限<br><br>子账户默认权限为spot_trade& contract_trade |
| data.subAccountList[].cTime | string |  | 创建时间 |
| data.subAccountList[].uTime | string |  | 最新修改时间 |
| data.endId | string |  | 查询数据返回最小ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1656589586807,
  "data": {
    "endId": "51",
    "subAccountList": [
      {
        "subAccountUid": "********",
        "subAccountName": "****@*****.com",
        "status": "normal",
        "permList": [
          "read",
          "spot_trade",
          "contract_trade"
        ],
        "label": "mySub01",
        "cTime": "1653287983475",
        "uTime": "1682660169573"
      }
    ]
  }
}
```

## 查询虚拟子账户Apikey列表

`GET /api/v2/user/virtual-subaccount-apikey-list`

限速规则：5次/秒/UID

仅支持主账户API Key调用，且API Key需要绑定IP地址

Operation ID: `classicCommonVsubaccountGetVirtualSubaccountApikeyList`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| subAccountUid | query | string | 是 | 子账户UID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].subAccountUid | string |  | 子账户UID |
| data[].subAccountApiKey | string |  | 子账户Apikey |
| data[].permList | string[] |  | 子账户apiKey 权限<br><br>`spot_trade`: 现货交易<br><br>`margin_trade`: 现货杠杆交易<br><br>`contract_trade`: 合约交易读写<br><br>`transfer`:钱包划转权限<br><br>`read`:读取权限 |
| data[].label | string |  | 备注 |
| data[].ipList | string[] |  | ip列表 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1682661432874,
  "data": [
    {
      "subAccountUid": "1",
      "label": "1682396356594",
      "subAccountApiKey": "xx_xxx",
      "permList": [
        "spot_trade",
        "margin_trade",
        "contract_trade"
      ],
      "ipList": [
        "127.0.0.1"
      ]
    }
  ]
}
```

## 创建 Agent 子账户

`POST /api/v2/user/create-agent-subaccount`

限速规则: 1次/1s/UID

为 AI Agent 实例创建专属子账户。Agent 子账户创建后不支持编辑（名称、权限等配置均不可修改）。每个主账户可创建的 Agent 子账户数量上限与普通子账户共享总配额。

Operation ID: `classicCommonVsubaccountCreateAgentSubaccount`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| username | string | 是 | 用于生成虚拟邮箱地址的用户名。只能是小写字母且不能超过20个字符 |
| passphrase | string | 是 | API Key 密钥，长度为8至32位的英文字母与数字组合 |
| note | string |  | 子账户备注 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.username | string |  | Agent 子账户昵称 |
| data.subUid | string |  | Agent 子账户 ID |
| data.apiKey | string |  | Agent 子账户 API Key |
| data.secret | string |  | Agent 子账户密钥 |
| data.note | string |  | 备注 |
| data.createdTime | string |  | 创建时间，Unix毫秒时间戳 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "username": "xxxx@virtual-bitget.com",
    "subUid": "xxxx",
    "apiKey": "***********************************",
    "secret": "*********************************************",
    "note": "xxxx",
    "createdTime": "1740211445041"
  }
}
```