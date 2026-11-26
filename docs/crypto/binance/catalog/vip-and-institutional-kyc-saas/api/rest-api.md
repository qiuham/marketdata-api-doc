---
exchange: binance
source_url: https://developers.binance.com/en/docs/catalog/vip-and-institutional-kyc-saas/api/rest-api
api_type: REST
updated_at: 2026-11-26 18:50:04.893928
---

# KYC SaaS REST API

Schema: https://developers.binance.com/en/docs/catalog/vip-and-institutional-kyc-saas/api/rest-api/1.0.0/schema.yaml

Integrate identity verification and manage KYC workflows via the Binance Link KYC API.

通过 Binance Link KYC API 集成身份验证并管理 KYC 工作流。

版本: 1.0.0

## 服务地址

- `https://cb.link-kycapi.com`

## 接口列表

- `POST /bapi/ekyc/v2/public/ekyc/customer/check-kyc-status` — Check KYC Status
- `POST /bapi/ekyc/v2/public/ekyc/customer/page-query-rfi-records` — Kyc RFI Records Query API
- `POST /bapi/ekyc/v2/public/ekyc/customer/submit-rfi-record` — Kyc RFI Record Submit API
- `POST /bapi/ekyc/v2/public/ekyc/customer/share-kyc-data` — KYC Sharing
- `POST /bapi/ekyc/v2/public/ekyc/customer/add-account-info-list` — Link Multiple Accounts
- `POST /bapi/ekyc/v2/public/ekyc/customer/query-submit-rfi-result` — Query Kyc RFI Record Submit Result API
- `POST /bapi/ekyc/v2/public/ekyc/customer/inner-query-kyc-status` — Query KYC status By Broker SubAccountId
- `POST /bapi/ekyc/v2/public/ekyc/customer/query-kyc-info` — Query KYC status By EntityCustomerId
- `POST /bapi/ekyc/v2/public/ekyc/customer/query-linked-accounts` — Query Linked Accounts Info
- `POST /bapi/ekyc/v2/public/ekyc/customer/query-share-data-status` — Query Share KYC Info Status API
- `POST /bapi/ekyc/v2/public/ekyc/customer/refused-kyc-data` — Refused User KYC Data
- `POST /bapi/ekyc/v2/public/ekyc/customer/unlink-kyc-data` — Unlink User KYC Data

## Check KYC Status（检查 KYC 状态）

`POST /bapi/ekyc/v2/public/ekyc/customer/check-kyc-status`

Check KYC Status

检查 KYC 状态

Operation ID: `checkKycStatus`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-SHA2-Signature | header | string | 是 | Request signature. HMAC-SHA256 of the JSON request body, hex-encoded. See [API request signing](/products/kyc-saas/basics/2.request-signing).<br>请求签名。对 JSON 请求体进行 HMAC-SHA256 签名并以十六进制输出。参见 [API request signing](/products/kyc-saas/basics/2.request-signing)。<br>例: `SIGNATURE` |

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| bizEntityKey | string | 是 | business entity key, each access entity has its own bizEntityKey<br>业务实体标识，每个接入方实体都有其专属的 bizEntityKey。<br>例: `BROKERKEY` |
| entityCustomerId | string | 是 | customer id，that is, the user id of the access entity site<br>客户 ID，即接入方站点中的用户 ID。<br>例: `1` |
| kycType | string | 是 | kyc type，USER<br>KYC 类型，例如 USER。<br>例: `USER` |
| brokerMainAccountId | string | 是 | broker main account id<br>经纪商主账户 ID。<br>例: `1` |
| brokerSubAccountId | string | 是 | broker sub account id<br>经纪商子账户 ID。<br>例: `1` |

### 响应 200：Check KYC Status / 检查 KYC 状态

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  | 例: `000000` |
| message | string |  | 例: `null` |
| messageDetail | string |  | 例: `null` |
| data | object |  |  |
| data.statusInfo | object |  |  |
| data.statusInfo.bizEntityKey | string |  | 例: `BROKERKEY` |
| data.statusInfo.entityCustomerId | string |  | 例: `4574117426369925632` |
| data.statusInfo.kycUserId | string |  | 例: `4575836000526931200` |
| data.statusInfo.userType | string |  | 例: `USER` |
| data.statusInfo.kycType | string |  | 例: `USER` |
| data.statusInfo.businessType | string |  | 例: `null` |
| data.statusInfo.status | string |  | 例: `null` |
| data.statusInfo.expectTime | string |  | 例: `null` |
| data.statusInfo.expectTimeText | string |  | 例: `null` |
| data.statusInfo.kycStatus | string |  | 例: `REJECT` |
| data.statusInfo.failReason | string |  | 例: `This ID number has been used. Log in to your original account to complete the transaction.` |
| data.statusInfo.basicStatus | string |  | 例: `PASS` |
| data.statusInfo.basicExpectTime | string |  | 例: `null` |
| data.statusInfo.basicExpectTimeText | string |  | 例: `null` |
| data.statusInfo.basicFailReason | string |  | 例: `` |
| data.statusInfo.basicSubStatus | string |  | 例: `null` |
| data.statusInfo.documentStatus | string |  | 例: `null` |
| data.statusInfo.documentExpectTime | string |  | 例: `null` |
| data.statusInfo.documentExpectTimeText | string |  | 例: `null` |
| data.statusInfo.documentFailReason | string |  | 例: `null` |
| data.statusInfo.identityStatus | string |  | 例: `REJECT` |
| data.statusInfo.identityExpectTime | string |  | 例: `null` |
| data.statusInfo.identityExpectTimeText | string |  | 例: `null` |
| data.statusInfo.identityFailReason | string |  | 例: `This ID number has been used. Log in to your original account to complete the transaction.` |
| data.statusInfo.identityFailCode | string |  | 例: `null` |
| data.statusInfo.faceStatus | string |  | 例: `REJECT` |
| data.statusInfo.faceExpectTime | string |  | 例: `null` |
| data.statusInfo.faceExpectTimeText | string |  | 例: `null` |
| data.statusInfo.faceFailReason | string |  | 例: `This ID number has been used. Log in to your original account to complete the transaction.` |
| data.statusInfo.faceEmailStatus | string |  | 例: `null` |
| data.statusInfo.faceEmailMask | string |  | 例: `null` |
| data.statusInfo.wckStatus | string |  | 例: `INITIAL` |
| data.statusInfo.wckExpectTime | string |  | 例: `null` |
| data.statusInfo.wckExpectTimeText | string |  | 例: `null` |
| data.statusInfo.wckFailReason | string |  | 例: `null` |
| data.statusInfo.firstName | string |  | 例: `null` |
| data.statusInfo.middleName | string |  | 例: `null` |
| data.statusInfo.lastName | string |  | 例: `null` |
| data.statusInfo.poaStatus | string |  | 例: `null` |
| data.statusInfo.poaExpectTime | string |  | 例: `null` |
| data.statusInfo.poaExpectTimeText | string |  | 例: `null` |
| data.statusInfo.poaFailReason | string |  | 例: `null` |
| data.statusInfo.eddStatus | string |  | 例: `null` |
| data.statusInfo.eddExpectTime | string |  | 例: `null` |
| data.statusInfo.eddExpectTimeText | string |  | 例: `null` |
| data.statusInfo.eddFailReason | string |  | 例: `null` |
| data.statusInfo.dbCreateTime | integer (int64) |  | 例: `1750699479373` |
| data.statusInfo.dbModifyTime | integer (int64) |  | 例: `1750699512711` |
| data.statusInfo.questionStatus | string |  | 例: `null` |
| data.statusInfo.questionFailReason | string |  | 例: `null` |
| data.statusInfo.completeTime | string |  | 例: `null` |
| data.statusInfo.basicCompleteTime | string |  | 例: `null` |
| data.statusInfo.documentCompleteTime | string |  | 例: `null` |
| data.statusInfo.identityCompleteTime | integer (int64) |  | 例: `1750699512647` |
| data.statusInfo.faceCompleteTime | integer (int64) |  | 例: `1750699512651` |
| data.statusInfo.wckCompleteTime | string |  | 例: `null` |
| data.statusInfo.poaCompleteTime | string |  | 例: `null` |
| data.statusInfo.eddCompleteTime | string |  | 例: `null` |
| data.statusInfo.questionCompleteTime | string |  | 例: `null` |
| data.statusInfo.kycSubType | string |  | 例: `null` |
| data.statusInfo.kycSubStatus | string |  | 例: `null` |
| data.statusInfo.credentialStatus | string |  | 例: `null` |
| data.statusInfo.credentialFailReason | string |  | 例: `null` |
| data.statusInfo.fiatPtStatus | string |  | 例: `null` |
| data.statusInfo.fiatPtFailReason | string |  | 例: `null` |
| data.statusInfo.memberStatus | string |  | 例: `null` |
| data.statusInfo.remediationStatus | string |  | 例: `null` |
| data.statusInfo.remediationExpectTime | string |  | 例: `null` |
| data.statusInfo.riskRateLevel | string |  | 例: `MEDIUM` |
| data.statusInfo.riskRateScore | number (float) |  | 例: `31` |
| data.levelInfo | object |  |  |
| data.levelInfo.currentLevel | object |  |  |
| data.levelInfo.currentLevel.levelName | string |  | 例: `INTERMEDIATE` |
| data.levelInfo.currentLevel.levelDesc | string |  | 例: `INTERMEDIATE` |
| data.levelInfo.currentLevel.kycStatus | string |  | 例: `REFUSED` |
| data.levelInfo.currentLevel.kycLevelSubStatus | string |  | 例: `null` |
| data.levelInfo.currentLevel.limit | object |  |  |
| data.levelInfo.currentLevel.limit.fiatCurrency | string |  | 例: `USD` |
| data.levelInfo.currentLevel.limit.depositFiatDailyLimit | string |  | 例: `null` |
| data.levelInfo.currentLevel.limit.withdrawFiatDailyLimit | integer (int64) |  | 例: `20000` |
| data.levelInfo.currentLevel.limit.totalFiatDailyLimit | string |  | 例: `null` |
| data.levelInfo.currentLevel.limit.depositFiatMonthlyLimit | string |  | 例: `null` |
| data.levelInfo.currentLevel.limit.withdrawFiatMonthlyLimit | string |  | 例: `null` |
| data.levelInfo.currentLevel.limit.totalFiatMonthlyLimit | string |  | 例: `null` |
| data.levelInfo.currentLevel.limit.depositFiatYearlyLimit | string |  | 例: `null` |
| data.levelInfo.currentLevel.limit.withdrawFiatYearlyLimit | string |  | 例: `null` |
| data.levelInfo.currentLevel.limit.totalFiatYearlyLimit | string |  | 例: `null` |
| data.levelInfo.currentLevel.limit.depositFiatLifeTimeLimit | string |  | 例: `null` |
| data.levelInfo.currentLevel.limit.withdrawFiatLifeTimeLimit | string |  | 例: `null` |
| data.levelInfo.currentLevel.limit.totalFiatLifeTimeLimit | string |  | 例: `null` |
| data.levelInfo.currentLevel.limit.cryptoCurrency | string |  | 例: `BTC` |
| data.levelInfo.currentLevel.limit.depositCryptoDailyLimit | integer (int64) |  | 例: `-1` |
| data.levelInfo.currentLevel.limit.withdrawCryptoDailyLimit | integer (int64) |  | 例: `100` |
| data.levelInfo.currentLevel.limit.totalCryptoDailyLimit | string |  | 例: `null` |
| data.levelInfo.completedLevel | string |  | 例: `null` |
| data.levelInfo.passedLevel | string |  | 例: `null` |
| data.levelInfo.definedKycPassLevel | string |  | 例: `null` |
| data.levelInfo.kycPass | boolean |  | 例: `False` |
| data.levelInfo.hasMultipleLevels | boolean |  | 例: `False` |
| data.levelInfo.passedLevels | string[] |  |  |
| data.remainingSteps | string |  | 例: `null` |
| data.nonExisted | string |  | 例: `null` |
| data.oauthUserInfo | string |  | 例: `null` |
| data.version | integer (int64) |  | 例: `1750699512711` |
| success | boolean |  | 例: `True` |

## Kyc RFI Records Query API（KYC RFI 记录查询接口）

`POST /bapi/ekyc/v2/public/ekyc/customer/page-query-rfi-records`

Kyc RFI Records Query API

KYC RFI 记录查询接口

Operation ID: `kycRfiRecordsQueryApi`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-SHA2-Signature | header | string | 是 | Request signature. HMAC-SHA256 of the JSON request body, hex-encoded. See [API request signing](/products/kyc-saas/basics/2.request-signing).<br>请求签名。对 JSON 请求体进行 HMAC-SHA256 签名并以十六进制输出。参见 [API request signing](/products/kyc-saas/basics/2.request-signing)。<br>例: `SIGNATURE` |

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| bizEntityKey | string | 是 | business entity key, each access entity has its own bizEntityKey<br>业务实体标识，每个接入方实体都有其专属的 bizEntityKey。<br>例: `BROKERKEY` |
| entityCustomerId | string |  | customer id, that is, the user id of the access entity site.<br>客户 ID，即接入方站点中的用户 ID。<br>例: `1` |
| kycType | string |  | kyc type，USER<br>KYC 类型，例如 USER。<br>例: `USER` |
| recordId | string |  | Rfi Record Id<br>RFI 记录 ID。<br>例: `1` |
| status | string |  | Rfi record status:<br>PROCESS(under process)<br>UPLOADING(uploading files)<br>REVIEW(under<br>review)<br>PASS(file review pass)<br>REFUSED(file refused)<br>EXPIRED(file expired)<br>CLOSE(close<br>file flow)<br>RFI 记录状态：<br>PROCESS（处理中）<br>UPLOADING（上传中）<br>REVIEW（审核中）<br>PASS（审核通过）<br>REFUSED（审核拒绝）<br>EXPIRED（已过期）<br>CLOSE（流程关闭）<br>例: `PROCESS` |
| startTime | string |  | min create time, yyyy-MM-dd<br>最小创建时间，格式 yyyy-MM-dd。<br>例: `1623319461670` |
| endTime | string |  | max create time, yyyy-MM-dd<br>最大创建时间，格式 yyyy-MM-dd。<br>例: `1641782889000` |
| page | integer (int64) | 是 | page number, start from 1<br>页码，从 1 开始。<br>例: `1` |
| rows | integer (int64) | 是 | rows<br>每页条数。<br>例: `10` |

### 响应 200：Kyc RFI Records API / KYC RFI 记录查询接口

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  | 例: `000000` |
| message | string |  | 例: `null` |
| messageDetail | string |  | 例: `null` |
| data | object |  |  |
| data.total | integer (int64) |  | 例: `1` |
| data.rows | object[] |  |  |
| data.rows[].recordId | string |  | 例: `12345` |
| data.rows[].bizEntityKey | string |  | 例: `BROKERKEY` |
| data.rows[].kycUserId | string |  | 例: `4276875665261234567` |
| data.rows[].entityCustomerId | string |  | 例: `45712345678999212345` |
| data.rows[].kycType | string |  | 例: `USER` |
| data.rows[].status | string |  | 例: `PROCESS` |
| data.rows[].subStatus | string |  | 例: `INIT` |
| data.rows[].fileTypes | string[] |  |  |
| data.rows[].fileData | string |  | 例: `null` |
| data.rows[].expireTime | integer (int64) |  | 例: `1752105600000` |
| data.rows[].requestComment | string |  | 例: `test` |
| data.rows[].recordType | string |  | 例: `IDENTITY` |
| data.rows[].reason | string |  | 例: `null` |
| data.rows[].remark | string |  | 例: `null` |
| data.rows[].creator | string |  | 例: `test@example.com` |
| data.rows[].submitter | string |  | 例: `null` |
| data.rows[].auditor | string |  | 例: `null` |
| data.rows[].auditTime | string |  | 例: `null` |
| data.rows[].completeTime | string |  | 例: `null` |
| data.rows[].dbCreateTime | integer (int64) |  | 例: `1750927524935` |
| data.rows[].dbModifyTime | integer (int64) |  | 例: `1750927524935` |
| success | boolean |  | 例: `True` |

## Kyc RFI Record Submit API（KYC RFI 记录提交接口）

`POST /bapi/ekyc/v2/public/ekyc/customer/submit-rfi-record`

Kyc RFI Record Submit API


RFI Upload API is in async mode. <br>Upon completion, the system will
notify the process result via notify webhook with eventType =
USER-RFI-SUBMIT-RESULT<br>User can also use POST
`/bapi/ekyc/v2/public/ekyc/customer/query-submit-rfi-result` to query
the RFI status/result.

KYC RFI 记录提交接口。

RFI 上传接口为异步模式。<br>处理完成后，系统会通过 notify webhook 回调通知处理结果，
eventType = USER-RFI-SUBMIT-RESULT。<br>用户也可以调用 POST
`/bapi/ekyc/v2/public/ekyc/customer/query-submit-rfi-result` 查询 RFI 状态/结果。

Operation ID: `kycRfiRecordSubmitApi`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-SHA2-Signature | header | string | 是 | Request signature. HMAC-SHA256 of the JSON request body, hex-encoded. See [API request signing](/products/kyc-saas/basics/2.request-signing).<br>请求签名。对 JSON 请求体进行 HMAC-SHA256 签名并以十六进制输出。参见 [API request signing](/products/kyc-saas/basics/2.request-signing)。<br>例: `SIGNATURE` |

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| bizEntityKey | string | 是 | business entity key, each access entity has its own bizEntityKey<br>业务实体标识，每个接入方实体都有其专属的 bizEntityKey。<br>例: `BROKERKEY` |
| entityCustomerId | string | 是 | customer id, that is, the user id of the access entity site.<br>客户 ID，即接入方站点中的用户 ID。<br>例: `45712345678999212345` |
| kycType | string | 是 | kyc type, USER<br>KYC 类型，例如 USER。<br>例: `USER` |
| recordId | string | 是 | Rfi Record Id, got from \"RFI Records Query API\" response<br>RFI 记录 ID，可从“RFI 记录查询接口”响应中获取。<br>例: `12345` |
| fileDataList | object[] | 是 | File data info list, KycFileGroupInfoVo<br>文件数据列表，类型为 KycFileGroupInfoVo。 |
| fileDataList[].type | string |  | Rfi Record required file type, got from \"RFI Records Query API\" response<br>RFI 记录要求的文件类型，可从“RFI 记录查询接口”响应中获取。<br>例: `SOF` |
| fileDataList[].files | object[] |  | File url info list. Supported file extensions: jpg, jpeg, png, pdf, mp4, mov; file size<br>limit: <= 10M.<br>文件 URL 信息列表。支持扩展名：jpg、jpeg、png、pdf、mp4、mov；文件大小限制 <= 10M。 |
| fileDataList[].files[].fileUrl | string |  | file download url<br>文件下载地址。<br>例: `https://image.cnbcfm.com/api/v1/image/104853635-GettyImages-870113330.jpg?v=1709055832&w=740&h=416&ffmt=webp&vtcrop=y` |

### 响应 200：Kyc RFI Record Submit API / KYC RFI 记录提交接口

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  | 例: `000000` |
| message | string |  | 例: `null` |
| messageDetail | string |  | 例: `null` |
| data | object |  |  |
| data.requestNo | string |  | request biz no, used for query result later<br>请求业务编号，用于后续查询结果。<br>例: `6286de2c976243a38ce4da8bebc403cf` |
| success | boolean |  | 例: `True` |

## KYC Sharing（KYC 信息共享）

`POST /bapi/ekyc/v2/public/ekyc/customer/share-kyc-data`

Share Crypto-As-A-Service (CAAS) User KYC Info API.

For **KZ Entity Brokers** (Partial Sharing mode), each data section is optional and may be
submitted independently across multiple requests. At least one of `basicInfo`,
`identityInfo`, `tncInfo` or `questionnaireInfo` must be non-null per request.

For **Standard Brokers**, `basicInfo` and `identityInfo` are both mandatory.

共享 Crypto-As-A-Service (CAAS) 用户 KYC 信息接口。

对于 **KZ Entity 经纪商**（部分共享模式），各数据段均为可选，可分多次请求独立提交。每次请求中 `basicInfo`、`identityInfo`、`tncInfo`、`questionnaireInfo` 至少需有一个不为空。

对于**标准经纪商**，`basicInfo` 与 `identityInfo` 均为必填。

Operation ID: `kycSharing`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-SHA2-Signature | header | string | 是 | Request signature. HMAC-SHA256 of the JSON request body, hex-encoded. See [API request signing](/products/kyc-saas/basics/2.request-signing).<br>请求签名。对 JSON 请求体进行 HMAC-SHA256 签名并以十六进制输出。参见 [API request signing](/products/kyc-saas/basics/2.request-signing)。<br>例: `SIGNATURE` |

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| bizEntityKey | string | 是 | business entity key, each access entity has its own bizEntityKey<br>业务实体标识，每个接入方实体都有其专属的 bizEntityKey。<br>例: `BROKERKEY` |
| requestNo | string | 是 | Unique request number<br>请求唯一编号。<br>例: `23454312345365012111113` |
| kycInfo | object | 是 | KycInfo<br>KYC 信息对象。 |
| kycInfo.userInfo | object | 是 | UserInfo<br>用户信息。 |
| kycInfo.userInfo.bizEntityKey | string | 是 | business entity key, each access entity has its own bizEntityKey<br>业务实体标识，每个接入方实体都有其专属的 bizEntityKey。<br>例: `BROKERKEY` |
| kycInfo.userInfo.entityCustomerId | string | 是 | Customer ID, that is, the user ID on the access entity site<br>客户 ID，即接入方站点中的用户 ID。<br>例: `12345678123456767` |
| kycInfo.userInfo.brokerMainAccountId | string | 是 | broker main account id<br>经纪商主账户 ID。<br>例: `1234567` |
| kycInfo.userInfo.brokerSubAccountId | string | 是 | broker sub account id<br>经纪商子账户 ID。<br>例: `12345678123456767` |
| kycInfo.userInfo.notifyUrl | string | 是 | notify url when kyc status changed<br>KYC 状态变更时的通知回调地址。<br>例: `https://webhook.site/` |
| kycInfo.userInfo.extra | string |  | extra info in JSON format<br>JSON 格式的额外信息。<br>例: `extraTestData` |
| kycInfo.basicInfo | object |  | BasicInfo. Required for standard brokers; optional for KZ Entity brokers.<br>基础信息。标准经纪商必填；KZ Entity 经纪商可选。 |
| kycInfo.basicInfo.firstName | string | 是 | 例: `AA` |
| kycInfo.basicInfo.middleName | string |  | 例: `testMiddleName` |
| kycInfo.basicInfo.lastName | string | 是 | 例: `BB` |
| kycInfo.basicInfo.residentialCountry | string | 是 | country of residence, 2-alpha code in UPPER CASE<br>居住国家，使用大写 2 位国家码。<br>例: `AE` |
| kycInfo.basicInfo.dob | string | 是 | yyyy-MM-dd<br>日期格式 yyyy-MM-dd。<br>例: `1999-09-19` |
| kycInfo.basicInfo.country | string | 是 | nationality, 2-alpha code in UPPER CASE<br>国籍，使用大写 2 位国家码。<br>例: `AE` |
| kycInfo.basicInfo.userSubmitIp | string | 是 | 例: `192.168.1.1` |
| kycInfo.basicInfo.address | string | 是 | Address<br>地址。<br>例: `aaa` |
| kycInfo.basicInfo.city | string | 是 | City<br>城市。<br>例: `bbb` |
| kycInfo.basicInfo.postalCode | string |  | Postal code<br>邮政编码。<br>例: `123456` |
| kycInfo.identityInfo | object |  | IdentityInfo. Required for standard brokers; optional for KZ Entity brokers.<br>身份信息。标准经纪商必填；KZ Entity 经纪商可选。 |
| kycInfo.identityInfo.documentType | string | 是 | document type, e.g. ID_CARD, PASSPORT, DRIVING_LICENSE, RESIDENCE_PERMIT<br>证件类型，例如 ID_CARD、PASSPORT、DRIVING_LICENSE、RESIDENCE_PERMIT。<br>例: `ID_CARD` |
| kycInfo.identityInfo.selectCountry | string | 是 | user selected country when doing ID verification, 2-alpha code in UPPER CASE<br>用户进行证件校验时选择的国家，使用大写 2 位国家码。<br>例: `SG` |
| kycInfo.identityInfo.frontFileUrl | string | 是 | ID front image download url<br>证件正面图片下载地址。<br>例: `https://image.cnbcfm.com/api/v1/image/104853635-GettyImages-870113330.jpg?v=1709055832&w=740&h=416&ffmt=webp&vtcrop=y` |
| kycInfo.identityInfo.backFileUrl | string |  | ID back image download url<br>证件反面图片下载地址。<br>例: `https://cdn.shortpixel.ai/spai/q_lossless+w_1776+to_webp+ret_img/independent-photo.com/wp-content/uploads/2022/03/Karen-Pape-1800x1200.jpeg` |
| kycInfo.identityInfo.faceFileUrl | string | 是 | face image download url<br>人脸图片下载地址。<br>例: `https://cdn.shortpixel.ai/spai/q_lossless+w_1776+to_webp+ret_img/independent-photo.com/wp-content/uploads/2022/03/Karen-Pape-1800x1200.jpeg` |
| kycInfo.identityInfo.firstName | string | 是 | must match BasicInfo.firstName, otherwise request will be rejected<br>必须与 BasicInfo.firstName 一致，否则会被拒绝。<br>例: `testFirstName` |
| kycInfo.identityInfo.middleName | string |  | 例: `testMiddleNameboli` |
| kycInfo.identityInfo.lastName | string | 是 | must match BasicInfo.lastName, otherwise request will be rejected<br>必须与 BasicInfo.lastName 一致，否则会被拒绝。<br>例: `testLastNameLItest01` |
| kycInfo.identityInfo.dob | string | 是 | date of birth, yyyy-MM-dd<br>出生日期，格式 yyyy-MM-dd。<br>例: `1999-09-19` |
| kycInfo.identityInfo.idType | string | 是 | ID document type, e.g. ID_CARD, PASSPORT, DRIVING_LICENSE, RESIDENCE_PERMIT<br>证件类型，例如 ID_CARD、PASSPORT、DRIVING_LICENSE、RESIDENCE_PERMIT。<br>例: `ID_CARD` |
| kycInfo.identityInfo.idSubType | string |  | ID document sub type<br>证件子类型。<br>例: `INTERNATIONAL_PASSPORT` |
| kycInfo.identityInfo.idCountry | string | 是 | 2-alpha code in UPPER CASE<br>使用大写 2 位国家码。<br>例: `AE` |
| kycInfo.identityInfo.nationalityCountry | string | 是 | 2-alpha code in UPPER CASE<br>使用大写 2 位国家码。<br>例: `AE` |
| kycInfo.identityInfo.idNumber | string | 是 | ID number<br>证件号码。<br>例: `testSaasBrokers0144288491` |
| kycInfo.identityInfo.idExpiry | string |  | yyyy-MM-dd<br>日期格式 yyyy-MM-dd。<br>例: `2030-09-19` |
| kycInfo.identityInfo.userSubmitIp | string | 是 | 例: `192.168.1.1` |
| kycInfo.identityInfo.idUsState | string |  | 例: `testIdUsState` |
| kycInfo.identityInfo.personalNumber | string |  | 例: `personalNumber6462313972` |
| kycInfo.identityInfo.gender | string |  | 例: `M` |
| kycInfo.identityInfo.issuingAuthority | string |  | 例: `firstName` |
| kycInfo.identityInfo.issuingDate | string |  | yyyy-MM-dd<br>日期格式 yyyy-MM-dd。<br>例: `2010-09-19` |
| kycInfo.identityInfo.issuingPlace | string |  | 例: `AE` |
| kycInfo.identityInfo.registrationNumber | string |  | 例: `registrationNumber4039460415` |
| kycInfo.identityInfo.city | string |  | 例: `testCity` |
| kycInfo.identityInfo.stateCode | string |  | 例: `QWER` |
| kycInfo.identityInfo.postalCode | string |  | 例: `123456` |
| kycInfo.identityInfo.address | string |  | 例: `testAddressData` |
| kycInfo.tncInfo | object |  | KZ Entity brokers only. T&C acceptance info. This section is optional - omit it if no TNC data needs to be submitted in this request.<br>仅限 KZ Entity 经纪商。条款与条件接受信息。该数据段为可选 —— 若本次请求无需提交 TNC 数据可省略。 |
| kycInfo.tncInfo.userSubmitIp | string | 是 | IP address of the user at the time of TNC submission<br>用户提交 TNC 时的 IP 地址<br>例: `192.168.1.1` |
| kycInfo.tncInfo.tncVersion | string | 是 | Version of the T&C document the user consented to. Format: `a.b`, e.g. `1.0`<br>用户所同意的条款与条件文档版本。格式：`a.b`，例如 `1.0`<br>例: `1.0` |
| kycInfo.tncInfo.consent | boolean | 是 | Whether the user explicitly consented to the T&C. Must not be null.<br>用户是否明确同意条款与条件。不得为空。<br>例: `True` |
| kycInfo.tncInfo.signTime | string | 是 | Timestamp of the user's consent action. ISO-8601 format<br>用户同意操作的时间戳。ISO-8601 格式<br>例: `2024-01-01T12:00:00Z` |
| kycInfo.questionnaireInfo | object |  | KZ Entity brokers only. Questionnaire answers. The submitted answers are validated against the questionnaire template registered for the provided `version`. Every question defined for that version must be answered.<br>仅限 KZ Entity 经纪商。问卷答案。提交的答案会按所提供 `version` 对应的问卷模板进行校验，该版本下定义的所有问题都必须作答。 |
| kycInfo.questionnaireInfo.version | string | 是 | Questionnaire version identifier, e.g. `kz_v6`. Must correspond to a questionnaire version configured for your broker.<br>问卷版本标识符，例如 `kz_v6`。必须与为您的经纪商所配置的问卷版本一致。<br>例: `kz_v6` |
| kycInfo.questionnaireInfo.answers | object[] | 是 | List of question and answer pairs. Must not be empty, and must cover every question defined for the given `version`.<br>问题与答案的列表。不得为空，且必须覆盖该 `version` 下定义的所有问题。 |
| kycInfo.questionnaireInfo.answers[].title | string | 是 | Question title key. Must match a question configured for the given `version`.<br>问题标题键。必须与该 `version` 下配置的问题一致。<br>例: `kz_v6_useFor` |
| kycInfo.questionnaireInfo.answers[].option | string | 是 | Selected option key (single choice). Must be a valid option from the configured option list for that question.<br>所选选项键（单选）。必须是该问题所配置选项列表中的有效值。<br>例: `kz_v6_useFor_investmentTrading` |

```json
{
  "bizEntityKey": "BROKERKEY",
  "requestNo": "23454312345365012111113",
  "kycInfo": {
    "userInfo": {
      "bizEntityKey": "BROKERKEY",
      "entityCustomerId": "12345678123456767",
      "brokerMainAccountId": "1234567",
      "brokerSubAccountId": "12345678123456767",
      "notifyUrl": "https://webhook.site/",
      "extra": "extraTestData"
    },
    "basicInfo": {
      "firstName": "AA",
      "middleName": "testMiddleName",
      "lastName": "BB",
      "residentialCountry": "AE",
      "dob": "1999-09-19",
      "country": "AE",
      "userSubmitIp": "192.168.1.1",
      "address": "aaa",
      "city": "bbb",
      "postalCode": "123456"
    },
    "identityInfo": {
      "documentType": "ID_CARD",
      "selectCountry": "SG",
      "frontFileUrl": "https://example.com/id-front.jpg",
      "faceFileUrl": "https://example.com/face.jpg",
      "firstName": "AA",
      "lastName": "BB",
      "dob": "1999-09-19",
      "idType": "ID_CARD",
      "idCountry": "AE",
      "nationalityCountry": "AE",
      "idNumber": "testIdNumber001",
      "idExpiry": "2030-09-19",
      "userSubmitIp": "192.168.1.1"
    }
  }
}
```

### 响应 200：KYC Sharing / KYC 信息共享

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  | 例: `000000` |
| message | string |  | 例: `null` |
| messageDetail | string |  | 例: `null` |
| data | string |  | 例: `null` |
| success | boolean |  | 例: `True` |

## Link Multiple Accounts（关联多个账户）

`POST /bapi/ekyc/v2/public/ekyc/customer/add-account-info-list`

If one person has multiple accounts, you can link these accounts together so the customers have to do KYC once.
The only step you need to do is call `add-account-info-list` API


This is also the relevant endpoint for utilizing Oauth Link.

One person can link maximum 5 accounts.

如果同一用户有多个账户，可以将这些账户关联在一起，让用户只需完成一次 KYC。您只需要调用
`add-account-info-list` 接口即可。该接口同样适用于 Oauth Link 场景。

单人最多可关联 5 个账户。

Operation ID: `linkMultipleAccounts`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-SHA2-Signature | header | string | 是 | Request signature. HMAC-SHA256 of the JSON request body, hex-encoded. See [API request signing](/products/kyc-saas/basics/2.request-signing).<br>请求签名。对 JSON 请求体进行 HMAC-SHA256 签名并以十六进制输出。参见 [API request signing](/products/kyc-saas/basics/2.request-signing)。<br>例: `SIGNATURE` |

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| bizEntityKey | string | 是 | business entity key, each access entity has its own bizEntityKey<br>业务实体标识，每个接入方实体都有其专属的 bizEntityKey。<br>例: `BROKERKEY` |
| accountList | object[] | 是 | Account relation list<br>账户关联列表 |
| accountList[].entityCustomerId | string |  | customer id, that is, the user id of the access entity site, Not Required for OAuth Link<br>客户 ID，即接入方站点中的用户 ID；在 OAuth Link 场景下非必填。<br>例: `ABC` |
| accountList[].openId | string |  | Required for OAuth Link<br>OAuth Link 场景必填。<br>例: `1` |
| accountList[].oauthClientId | string |  | Required for OAuth Link<br>OAuth Link 场景必填。<br>例: `1` |
| accountList[].brokerMainAccountId | string |  | Broker main account id<br>经纪商主账户 ID。<br>例: `123456789` |
| accountList[].brokerSubAccountId | string |  | Broker sub account id<br>经纪商子账户 ID。<br>例: `2789382993653477377` |

### 响应 200：Link Multiple Accounts / 关联多个账户

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  | 例: `000000` |
| message | string |  | 例: `null` |
| messageDetail | string |  | 例: `null` |
| data | string |  | 例: `null` |
| success | boolean |  | 例: `True` |

## Query Kyc RFI Record Submit Result API（查询 KYC RFI 提交结果接口）

`POST /bapi/ekyc/v2/public/ekyc/customer/query-submit-rfi-result`

Query Kyc RFI Record Submit Result API

查询 KYC RFI 提交结果接口

Operation ID: `queryKycRfiRecordSubmitResultApi`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-SHA2-Signature | header | string | 是 | Request signature. HMAC-SHA256 of the JSON request body, hex-encoded. See [API request signing](/products/kyc-saas/basics/2.request-signing).<br>请求签名。对 JSON 请求体进行 HMAC-SHA256 签名并以十六进制输出。参见 [API request signing](/products/kyc-saas/basics/2.request-signing)。<br>例: `SIGNATURE` |

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| bizEntityKey | string | 是 | business entity key, each access entity has its own bizEntityKey<br>业务实体标识，每个接入方实体都有其专属的 bizEntityKey。<br>例: `BROKERKEY` |
| entityCustomerId | string | 是 | customer id, that is, the user id of the access entity site.<br>客户 ID，即接入方站点中的用户 ID。<br>例: `1` |
| kycType | string | 是 | kyc type，USER<br>KYC 类型，例如 USER。<br>例: `USER` |
| recordId | string | 是 | Rfi Record Id<br>RFI 记录 ID。<br>例: `1` |
| requestNo | string | 是 | Rfi submit record request no, got from " RFI Record Submit API" response<br>RFI 提交记录请求号，可从“RFI 记录提交接口”响应中获取。<br>例: `6286de2c976243a38ce4da8bebc403cf` |

### 响应 200：Kyc RFI Record Submit Result API / 查询 KYC RFI 提交结果接口

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  | 例: `000000` |
| message | string |  | 例: `null` |
| messageDetail | string |  | 例: `null` |
| data | object |  |  |
| data.result | string |  | 例: `SUCCESS` |
| data.failReason | string |  | 例: `null` |
| success | boolean |  | 例: `True` |

## Query KYC status By Broker SubAccountId（按经纪商子账户 ID 查询 KYC 状态）

`POST /bapi/ekyc/v2/public/ekyc/customer/inner-query-kyc-status`

Query KYC status By Crypto-As-A-Service (CAAS) SubAccountId

按 Crypto-As-A-Service (CAAS) 子账户 ID 查询 KYC 状态

Operation ID: `queryKycStatusByBrokerSubAccountId`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-SHA2-Signature | header | string | 是 | Request signature. HMAC-SHA256 of the JSON request body, hex-encoded. See [API request signing](/products/kyc-saas/basics/2.request-signing).<br>请求签名。对 JSON 请求体进行 HMAC-SHA256 签名并以十六进制输出。参见 [API request signing](/products/kyc-saas/basics/2.request-signing)。<br>例: `SIGNATURE` |

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| bizEntityKey | string | 是 | business entity key, each access entity has its own bizEntityKey<br>业务实体标识，每个接入方实体都有其专属的 bizEntityKey。<br>例: `BROKERKEY` |
| brokerMainAccountId | string | 是 | broker main account id<br>经纪商主账户 ID。<br>例: `1` |
| brokerSubAccountId | string | 是 | broker sub account id<br>经纪商子账户 ID。<br>例: `1` |

### 响应 200：KYC status By Broker SubAccountId / 按经纪商子账户 ID 查询 KYC 状态

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  | 例: `000000` |
| message | string |  | 例: `null` |
| messageDetail | string |  | 例: `null` |
| data | object |  |  |
| data.statusInfo | object |  |  |
| data.statusInfo.bizEntityKey | string |  | 例: `BROKERKEY` |
| data.statusInfo.entityCustomerId | string |  | 例: `45712345678999212345` |
| data.statusInfo.kycUserId | string |  | 例: `4575836000526931200` |
| data.statusInfo.userType | string |  | 例: `USER` |
| data.statusInfo.kycType | string |  | 例: `USER` |
| data.statusInfo.businessType | string |  | 例: `null` |
| data.statusInfo.status | string |  | 例: `null` |
| data.statusInfo.expectTime | string |  | 例: `null` |
| data.statusInfo.expectTimeText | string |  | 例: `null` |
| data.statusInfo.kycStatus | string |  | 例: `REJECT` |
| data.statusInfo.failReason | string |  | 例: `This ID number has been used. Log in to your original account to complete the transaction.` |
| data.statusInfo.basicStatus | string |  | 例: `PASS` |
| data.statusInfo.basicExpectTime | string |  | 例: `null` |
| data.statusInfo.basicExpectTimeText | string |  | 例: `null` |
| data.statusInfo.basicFailReason | string |  | 例: `` |
| data.statusInfo.basicSubStatus | string |  | 例: `null` |
| data.statusInfo.documentStatus | string |  | 例: `null` |
| data.statusInfo.documentExpectTime | string |  | 例: `null` |
| data.statusInfo.documentExpectTimeText | string |  | 例: `null` |
| data.statusInfo.documentFailReason | string |  | 例: `null` |
| data.statusInfo.identityStatus | string |  | 例: `REJECT` |
| data.statusInfo.identityExpectTime | string |  | 例: `null` |
| data.statusInfo.identityExpectTimeText | string |  | 例: `null` |
| data.statusInfo.identityFailReason | string |  | 例: `This ID number has been used. Log in to your original account to complete the transaction.` |
| data.statusInfo.identityFailCode | string |  | 例: `null` |
| data.statusInfo.faceStatus | string |  | 例: `REJECT` |
| data.statusInfo.faceExpectTime | string |  | 例: `null` |
| data.statusInfo.faceExpectTimeText | string |  | 例: `null` |
| data.statusInfo.faceFailReason | string |  | 例: `This ID number has been used. Log in to your original account to complete the transaction.` |
| data.statusInfo.faceEmailStatus | string |  | 例: `null` |
| data.statusInfo.faceEmailMask | string |  | 例: `null` |
| data.statusInfo.wckStatus | string |  | 例: `INITIAL` |
| data.statusInfo.wckExpectTime | string |  | 例: `null` |
| data.statusInfo.wckExpectTimeText | string |  | 例: `null` |
| data.statusInfo.wckFailReason | string |  | 例: `null` |
| data.statusInfo.firstName | string |  | 例: `null` |
| data.statusInfo.middleName | string |  | 例: `null` |
| data.statusInfo.lastName | string |  | 例: `null` |
| data.statusInfo.poaStatus | string |  | 例: `null` |
| data.statusInfo.poaExpectTime | string |  | 例: `null` |
| data.statusInfo.poaExpectTimeText | string |  | 例: `null` |
| data.statusInfo.poaFailReason | string |  | 例: `null` |
| data.statusInfo.eddStatus | string |  | 例: `null` |
| data.statusInfo.eddExpectTime | string |  | 例: `null` |
| data.statusInfo.eddExpectTimeText | string |  | 例: `null` |
| data.statusInfo.eddFailReason | string |  | 例: `null` |
| data.statusInfo.dbCreateTime | integer (int64) |  | 例: `1750699479373` |
| data.statusInfo.dbModifyTime | integer (int64) |  | 例: `1750699512711` |
| data.statusInfo.questionStatus | string |  | 例: `null` |
| data.statusInfo.questionFailReason | string |  | 例: `null` |
| data.statusInfo.completeTime | string |  | 例: `null` |
| data.statusInfo.basicCompleteTime | string |  | 例: `null` |
| data.statusInfo.documentCompleteTime | string |  | 例: `null` |
| data.statusInfo.identityCompleteTime | integer (int64) |  | 例: `1750699512647` |
| data.statusInfo.faceCompleteTime | integer (int64) |  | 例: `1750699512651` |
| data.statusInfo.wckCompleteTime | string |  | 例: `null` |
| data.statusInfo.poaCompleteTime | string |  | 例: `null` |
| data.statusInfo.eddCompleteTime | string |  | 例: `null` |
| data.statusInfo.questionCompleteTime | string |  | 例: `null` |
| data.statusInfo.kycSubType | string |  | 例: `null` |
| data.statusInfo.kycSubStatus | string |  | 例: `null` |
| data.statusInfo.credentialStatus | string |  | 例: `null` |
| data.statusInfo.credentialFailReason | string |  | 例: `null` |
| data.statusInfo.fiatPtStatus | string |  | 例: `null` |
| data.statusInfo.fiatPtFailReason | string |  | 例: `null` |
| data.statusInfo.memberStatus | string |  | 例: `null` |
| data.statusInfo.remediationStatus | string |  | 例: `null` |
| data.statusInfo.remediationExpectTime | string |  | 例: `null` |
| data.statusInfo.riskRateLevel | string |  | 例: `MEDIUM` |
| data.statusInfo.riskRateScore | number (float) |  | 例: `31` |
| data.levelInfo | object |  |  |
| data.levelInfo.currentLevel | object |  |  |
| data.levelInfo.currentLevel.levelName | string |  | 例: `INTERMEDIATE` |
| data.levelInfo.currentLevel.levelDesc | string |  | 例: `INTERMEDIATE` |
| data.levelInfo.currentLevel.kycStatus | string |  | 例: `REFUSED` |
| data.levelInfo.currentLevel.kycLevelSubStatus | string |  | 例: `null` |
| data.levelInfo.currentLevel.limit | object |  |  |
| data.levelInfo.currentLevel.limit.fiatCurrency | string |  | 例: `USD` |
| data.levelInfo.currentLevel.limit.depositFiatDailyLimit | string |  | 例: `null` |
| data.levelInfo.currentLevel.limit.withdrawFiatDailyLimit | integer (int64) |  | 例: `20000` |
| data.levelInfo.currentLevel.limit.totalFiatDailyLimit | string |  | 例: `null` |
| data.levelInfo.currentLevel.limit.depositFiatMonthlyLimit | string |  | 例: `null` |
| data.levelInfo.currentLevel.limit.withdrawFiatMonthlyLimit | string |  | 例: `null` |
| data.levelInfo.currentLevel.limit.totalFiatMonthlyLimit | string |  | 例: `null` |
| data.levelInfo.currentLevel.limit.depositFiatYearlyLimit | string |  | 例: `null` |
| data.levelInfo.currentLevel.limit.withdrawFiatYearlyLimit | string |  | 例: `null` |
| data.levelInfo.currentLevel.limit.totalFiatYearlyLimit | string |  | 例: `null` |
| data.levelInfo.currentLevel.limit.depositFiatLifeTimeLimit | string |  | 例: `null` |
| data.levelInfo.currentLevel.limit.withdrawFiatLifeTimeLimit | string |  | 例: `null` |
| data.levelInfo.currentLevel.limit.totalFiatLifeTimeLimit | string |  | 例: `null` |
| data.levelInfo.currentLevel.limit.cryptoCurrency | string |  | 例: `BTC` |
| data.levelInfo.currentLevel.limit.depositCryptoDailyLimit | integer (int64) |  | 例: `-1` |
| data.levelInfo.currentLevel.limit.withdrawCryptoDailyLimit | integer (int64) |  | 例: `100` |
| data.levelInfo.currentLevel.limit.totalCryptoDailyLimit | string |  | 例: `null` |
| data.levelInfo.completedLevel | string |  | 例: `null` |
| data.levelInfo.passedLevel | string |  | 例: `null` |
| data.levelInfo.definedKycPassLevel | string |  | 例: `null` |
| data.levelInfo.kycPass | boolean |  | 例: `False` |
| data.levelInfo.hasMultipleLevels | boolean |  | 例: `False` |
| data.levelInfo.passedLevels | string[] |  |  |
| data.remainingSteps | string |  | 例: `null` |
| data.nonExisted | string |  | 例: `null` |
| data.oauthUserInfo | string |  | 例: `null` |
| data.version | integer (int64) |  | 例: `1750699512711` |
| success | boolean |  | 例: `True` |

## Query KYC status By EntityCustomerId（按 EntityCustomerId 查询 KYC 状态）

`POST /bapi/ekyc/v2/public/ekyc/customer/query-kyc-info`

Query KYC Detail INFO Query API

查询 KYC 详情信息接口

Operation ID: `queryKycStatusByEntityCustomerId`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-SHA2-Signature | header | string | 是 | Request signature. HMAC-SHA256 of the JSON request body, hex-encoded. See [API request signing](/products/kyc-saas/basics/2.request-signing).<br>请求签名。对 JSON 请求体进行 HMAC-SHA256 签名并以十六进制输出。参见 [API request signing](/products/kyc-saas/basics/2.request-signing)。<br>例: `SIGNATURE` |

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| bizEntityKey | string | 是 | business entity key, each access entity has its own bizEntityKey<br>业务实体标识，每个接入方实体都有其专属的 bizEntityKey。<br>例: `BROKERKEY` |
| entityCustomerId | string | 是 | customer id，that is, the user id of the access entity site<br>客户 ID，即接入方站点中的用户 ID。<br>例: `1` |
| kycType | string | 是 | kyc type，USER<br>KYC 类型，例如 USER。<br>例: `USER` |

### 响应 200：KYC status By EntityCustomerId / 按 EntityCustomerId 查询 KYC 状态

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  | 例: `000000` |
| message | string |  | 例: `null` |
| messageDetail | string |  | 例: `null` |
| data | object |  |  |
| data.statusInfo | object |  |  |
| data.statusInfo.bizEntityKey | string |  | 例: `BROKERKEY` |
| data.statusInfo.entityCustomerId | string |  | 例: `45712345678999212345` |
| data.statusInfo.kycUserId | string |  | 例: `4575836000526931200` |
| data.statusInfo.userType | string |  | 例: `USER` |
| data.statusInfo.kycType | string |  | 例: `USER` |
| data.statusInfo.businessType | string |  | 例: `null` |
| data.statusInfo.status | string |  | 例: `null` |
| data.statusInfo.expectTime | string |  | 例: `null` |
| data.statusInfo.expectTimeText | string |  | 例: `null` |
| data.statusInfo.kycStatus | string |  | 例: `REJECT` |
| data.statusInfo.failReason | string |  | 例: `This ID number has been used. Log in to your original account to complete the transaction.` |
| data.statusInfo.basicStatus | string |  | 例: `PASS` |
| data.statusInfo.basicExpectTime | string |  | 例: `null` |
| data.statusInfo.basicExpectTimeText | string |  | 例: `null` |
| data.statusInfo.basicFailReason | string |  | 例: `` |
| data.statusInfo.basicSubStatus | string |  | 例: `null` |
| data.statusInfo.documentStatus | string |  | 例: `null` |
| data.statusInfo.documentExpectTime | string |  | 例: `null` |
| data.statusInfo.documentExpectTimeText | string |  | 例: `null` |
| data.statusInfo.documentFailReason | string |  | 例: `null` |
| data.statusInfo.identityStatus | string |  | 例: `REJECT` |
| data.statusInfo.identityExpectTime | string |  | 例: `null` |
| data.statusInfo.identityExpectTimeText | string |  | 例: `null` |
| data.statusInfo.identityFailReason | string |  | 例: `This ID number has been used. Log in to your original account to complete the transaction.` |
| data.statusInfo.identityFailCode | string |  | 例: `null` |
| data.statusInfo.faceStatus | string |  | 例: `REJECT` |
| data.statusInfo.faceExpectTime | string |  | 例: `null` |
| data.statusInfo.faceExpectTimeText | string |  | 例: `null` |
| data.statusInfo.faceFailReason | string |  | 例: `This ID number has been used. Log in to your original account to complete the transaction.` |
| data.statusInfo.faceEmailStatus | string |  | 例: `null` |
| data.statusInfo.faceEmailMask | string |  | 例: `null` |
| data.statusInfo.wckStatus | string |  | 例: `INITIAL` |
| data.statusInfo.wckExpectTime | string |  | 例: `null` |
| data.statusInfo.wckExpectTimeText | string |  | 例: `null` |
| data.statusInfo.wckFailReason | string |  | 例: `null` |
| data.statusInfo.firstName | string |  | 例: `null` |
| data.statusInfo.middleName | string |  | 例: `null` |
| data.statusInfo.lastName | string |  | 例: `null` |
| data.statusInfo.poaStatus | string |  | 例: `null` |
| data.statusInfo.poaExpectTime | string |  | 例: `null` |
| data.statusInfo.poaExpectTimeText | string |  | 例: `null` |
| data.statusInfo.poaFailReason | string |  | 例: `null` |
| data.statusInfo.eddStatus | string |  | 例: `null` |
| data.statusInfo.eddExpectTime | string |  | 例: `null` |
| data.statusInfo.eddExpectTimeText | string |  | 例: `null` |
| data.statusInfo.eddFailReason | string |  | 例: `null` |
| data.statusInfo.dbCreateTime | integer (int64) |  | 例: `1750699479373` |
| data.statusInfo.dbModifyTime | integer (int64) |  | 例: `1750699512711` |
| data.statusInfo.questionStatus | string |  | 例: `null` |
| data.statusInfo.questionFailReason | string |  | 例: `null` |
| data.statusInfo.completeTime | string |  | 例: `null` |
| data.statusInfo.basicCompleteTime | string |  | 例: `null` |
| data.statusInfo.documentCompleteTime | string |  | 例: `null` |
| data.statusInfo.identityCompleteTime | integer (int64) |  | 例: `1750699512647` |
| data.statusInfo.faceCompleteTime | integer (int64) |  | 例: `1750699512651` |
| data.statusInfo.wckCompleteTime | string |  | 例: `null` |
| data.statusInfo.poaCompleteTime | string |  | 例: `null` |
| data.statusInfo.eddCompleteTime | string |  | 例: `null` |
| data.statusInfo.questionCompleteTime | string |  | 例: `null` |
| data.statusInfo.kycSubType | string |  | 例: `null` |
| data.statusInfo.kycSubStatus | string |  | 例: `null` |
| data.statusInfo.credentialStatus | string |  | 例: `null` |
| data.statusInfo.credentialFailReason | string |  | 例: `null` |
| data.statusInfo.fiatPtStatus | string |  | 例: `null` |
| data.statusInfo.fiatPtFailReason | string |  | 例: `null` |
| data.statusInfo.memberStatus | string |  | 例: `null` |
| data.statusInfo.remediationStatus | string |  | 例: `null` |
| data.statusInfo.remediationExpectTime | string |  | 例: `null` |
| data.statusInfo.riskRateLevel | string |  | 例: `MEDIUM` |
| data.statusInfo.riskRateScore | number (float) |  | 例: `31` |
| data.basicInfo | object |  |  |
| data.basicInfo.id | integer (int64) |  | 例: `4575836001114133500` |
| data.basicInfo.bizEntityKey | string |  | 例: `BROKERKEY` |
| data.basicInfo.bizKey | string |  | 例: `BROKERKEY` |
| data.basicInfo.kycUserId | string |  | 例: `4575836000526931200` |
| data.basicInfo.basicType | string |  | 例: `USER` |
| data.basicInfo.basicStatus | string |  | 例: `PASS` |
| data.basicInfo.basicFailReason | string |  | 例: `null` |
| data.basicInfo.auditor | string |  | 例: `null` |
| data.basicInfo.auditorTime | string |  | 例: `null` |
| data.basicInfo.firstName | string |  | 例: `BO` |
| data.basicInfo.middleName | string |  | 例: `testMiddleName` |
| data.basicInfo.lastName | string |  | 例: `LI` |
| data.basicInfo.residentialCountry | string |  | 例: `AE` |
| data.basicInfo.dob | string |  | 例: `1986-08-14` |
| data.basicInfo.postalCode | string |  | 例: `123456` |
| data.basicInfo.city | string |  | 例: `bbb` |
| data.basicInfo.address | string |  | 例: `aaa` |
| data.basicInfo.emailAddress | string |  | 例: `null` |
| data.basicInfo.authFileKey | string |  | 例: `null` |
| data.basicInfo.authFilePath | string |  | 例: `null` |
| data.basicInfo.companyName | string |  | 例: `null` |
| data.basicInfo.companyRegistrationNumber | string |  | 例: `null` |
| data.basicInfo.companyIncorporationDate | string |  | 例: `null` |
| data.basicInfo.contactMobileCode | string |  | 例: `null` |
| data.basicInfo.contactMobile | string |  | 例: `null` |
| data.basicInfo.corporateEmail | string |  | 例: `null` |
| data.basicInfo.companyRegisteredCountry | string |  | 例: `null` |
| data.basicInfo.companyRegisteredPostalCode | string |  | 例: `null` |
| data.basicInfo.companyRegisteredCity | string |  | 例: `null` |
| data.basicInfo.companyRegisteredAddress | string |  | 例: `null` |
| data.basicInfo.companyOperatingCountry | string |  | 例: `null` |
| data.basicInfo.companyOperatingPostalCode | string |  | 例: `null` |
| data.basicInfo.companyOperatingCity | string |  | 例: `null` |
| data.basicInfo.companyOperatingAddress | string |  | 例: `null` |
| data.basicInfo.sourceOfFunds | string |  | 例: `null` |
| data.basicInfo.sourceOfWealth | string |  | 例: `null` |
| data.basicInfo.submitIp | string |  | 例: `192.168.1.1` |
| data.basicInfo.submitClient | string |  | 例: `null` |
| data.basicInfo.submitSource | string |  | 例: `null` |
| data.basicInfo.submitDevice | string |  | 例: `null` |
| data.basicInfo.dbCreateTime | integer (int64) |  | 例: `1750699479396` |
| data.basicInfo.dbModifyTime | integer (int64) |  | 例: `1750699479396` |
| data.basicInfo.gender | string |  | 例: `null` |
| data.basicInfo.country | string |  | 例: `AE` |
| data.basicInfo.idType | string |  | 例: `null` |
| data.basicInfo.idCardNumber | string |  | 例: `null` |
| data.basicInfo.regionState | string |  | 例: `null` |
| data.basicInfo.tin | string |  | 例: `null` |
| data.basicInfo.suburb | string |  | 例: `null` |
| data.basicInfo.issuer | string |  | 例: `null` |
| data.basicInfo.countryOfIssue | string |  | 例: `null` |
| data.basicInfo.npwp | string |  | 例: `null` |
| data.basicInfo.phoneNumber | string |  | 例: `null` |
| data.basicInfo.placeOfBirth | string |  | 例: `null` |
| data.basicInfo.panId | string |  | 例: `null` |
| data.basicInfo.requestTime | integer (int64) |  | 例: `1750699479396` |
| data.basicInfo.requestIp | string |  | 例: `192.168.1.1` |
| data.basicInfo.website | string |  | 例: `null` |
| data.basicInfo.applyReason | string |  | 例: `null` |
| data.basicInfo.memberType | string |  | 例: `null` |
| data.basicInfo.ext | string |  | 例: `null` |
| data.basicInfo.entityUserId | string |  | 例: `null` |
| data.identityInfo | object |  |  |
| data.identityInfo.bizEntityKey | string |  | 例: `BROKERKEY` |
| data.identityInfo.bizKey | string |  | 例: `BROKERKEY` |
| data.identityInfo.kycUserId | string |  | 例: `4575836000526931200` |
| data.identityInfo.bizNo | string |  | 例: `88ed88b9ec854503abfe905548211b56` |
| data.identityInfo.vendorsCode | string |  | 例: `` |
| data.identityInfo.documentType | string |  | 例: `ID_CARD` |
| data.identityInfo.selectCountry | string |  | 例: `SG` |
| data.identityInfo.frontFileKey | string |  | 例: `ae6dd72112ec41d9b74be3d965d499d8` |
| data.identityInfo.frontFilePath | string |  | 例: `/SAAS/BROKERKEY/USER_UPLOAD/20250623/4575836000526931200_identity_front_172439955986.jpg` |
| data.identityInfo.frontFileUrl | string |  | 例: `https://www.somepage.com` |
| data.identityInfo.backFileKey | string |  | 例: `a0090a3067fc4dffaebed9d0fbecb341` |
| data.identityInfo.backFilePath | string |  | 例: `/SAAS/BROKERKEY/USER_UPLOAD/20250623/4575836000526931200_identity_back_172439508427.jpeg` |
| data.identityInfo.backFileUrl | string |  | 例: `https://www.somepage.com` |
| data.identityInfo.faceFileKey | string |  | 例: `8c05214b836946e89fc8a10443d522d1` |
| data.identityInfo.faceFilePath | string |  | 例: `/SAAS/BROKERKEY/USER_UPLOAD/20250623/4575836000526931200_identity_face_172439508685.jpeg` |
| data.identityInfo.faceFileUrl | string |  | 例: `https://www.somepage.com` |
| data.identityInfo.faceDetectFileKey | string |  | 例: `null` |
| data.identityInfo.faceDetectFilePath | string |  | 例: `null` |
| data.identityInfo.faceDetectFileUrl | string |  | 例: `null` |
| data.identityInfo.applyStatus | string |  | 例: `REJECT` |
| data.identityInfo.failReason | string |  | 例: `This ID number has been used. Log in to your original account to complete the transaction.` |
| data.identityInfo.vendorsStatus | string |  | 例: `null` |
| data.identityInfo.vendorsReason | string |  | 例: `null` |
| data.identityInfo.auditor | string |  | 例: `null` |
| data.identityInfo.auditorTime | string |  | 例: `null` |
| data.identityInfo.completeTime | string |  | 例: `null` |
| data.identityInfo.submitIp | string |  | 例: `192.168.1.1` |
| data.identityInfo.submitClient | string |  | 例: `null` |
| data.identityInfo.submitSource | string |  | 例: `null` |
| data.identityInfo.submitDevice | string |  | 例: `null` |
| data.identityInfo.firstName | string |  | 例: `testFirstName` |
| data.identityInfo.middleName | string |  | 例: `testMiddleNameboli` |
| data.identityInfo.lastName | string |  | 例: `testLastNameLItest01` |
| data.identityInfo.dob | string |  | 例: `1986-08-14` |
| data.identityInfo.idType | string |  | 例: `ID_CARD` |
| data.identityInfo.idSubType | string |  | 例: `INTERNATIONAL_PASSPORT` |
| data.identityInfo.idCountry | string |  | 例: `AE` |
| data.identityInfo.nationalityCountry | string |  | 例: `AE` |
| data.identityInfo.idNumber | string |  | 例: `testSaasBrokers0144288491` |
| data.identityInfo.idExpiry | string |  | 例: `2030-08-15` |
| data.identityInfo.idUsState | string |  | 例: `testIdUsState` |
| data.identityInfo.personalNumber | string |  | 例: `personalNumber6462313972` |
| data.identityInfo.gender | string |  | 例: `M` |
| data.identityInfo.nationality | string |  | 例: `null` |
| data.identityInfo.issuingAuthority | string |  | 例: `firstName` |
| data.identityInfo.issuingDate | string |  | 例: `2000-08-16` |
| data.identityInfo.issuingPlace | string |  | 例: `AE` |
| data.identityInfo.registrationNumber | string |  | 例: `registrationNumber4039460415` |
| data.identityInfo.city | string |  | 例: `testCity` |
| data.identityInfo.stateCode | string |  | 例: `QWER` |
| data.identityInfo.postalCode | string |  | 例: `123456` |
| data.identityInfo.address | string |  | 例: `testAddressData` |
| data.identityInfo.remarks | string |  | 例: `IMPORT` |
| data.identityInfo.language | string |  | 例: `null` |
| data.identityInfo.solarisReportPath | string |  | 例: `null` |
| data.identityInfo.solarisReportUrl | string |  | 例: `null` |
| data.identityInfo.idExpirySubStatus | string |  | 例: `null` |
| data.identityInfo.idGracePeriodRedoSubStatus | string |  | 例: `null` |
| data.identityInfo.sourceType | string |  | 例: `IMPORT` |
| data.identityInfo.identityApplyExtraInfo | string |  | 例: `null` |
| data.identityInfo.ocrDocumentType | string |  | 例: `null` |
| data.poaInfo | string |  | 例: `null` |
| data.eddInfo | string |  | 例: `null` |
| data.eddInfos | string |  | 例: `null` |
| data.eddTriggersAndInfos | string |  | 例: `null` |
| data.questionInfo | object[] |  | Questionnaire answer records for KZ Entity broker users. Empty if no questionnaire has been submitted.<br>KZ Entity 经纪商用户的问卷答案记录。如未提交问卷则为空。 |
| data.questionInfo[].flowType | string |  | Questionnaire group / version identifier<br>问卷组/版本标识符<br>例: `kz_v6` |
| data.questionInfo[].questionTitle | string |  | Question title key<br>问题标题键<br>例: `kz_v6_useFor` |
| data.questionInfo[].questionSubTitle | string |  | 例: `` |
| data.questionInfo[].questionId | integer (int64) |  | 例: `11` |
| data.questionInfo[].questionType | string |  | 例: `KYC_COMP_QUESTION_USE_FOR` |
| data.questionInfo[].answers | string[] |  |  |
| data.questionInfo[].sourceType | string |  | 例: `IMPORT` |
| data.questionInfo[].dbCreateTime | string |  | 例: `2024-05-01T08:30:00Z` |
| data.questionInfo[].dbModifyTime | string |  | 例: `2024-05-01T08:30:00Z` |
| data.tncInfo | object |  | T&C sign info for KZ Entity broker users. null if no TNC record exists.<br>KZ Entity 经纪商用户的条款与条件签署信息。无记录时为 null。 |
| data.tncInfo.tncVersion | string |  | Version of the T&C document (format: a.b)<br>条款与条件文档版本（格式：a.b）<br>例: `1.0` |
| data.tncInfo.consent | boolean |  | Whether the user consented<br>用户是否同意<br>例: `True` |
| data.tncInfo.signTime | string |  | Timestamp of consent<br>同意时间<br>例: `2024-05-01T08:30:00Z` |
| data.tncInfo.userSubmitIp | string |  | IP address at submission time<br>提交时的 IP 地址<br>例: `192.168.1.1` |
| data.tncInfo.sourceType | string |  | 例: `IMPORT` |
| data.tncInfo.dbCreateTime | string |  | 例: `2024-05-01T08:30:00Z` |
| data.riskScore | object |  |  |
| data.riskScore.id | integer (int64) |  | 例: `4575836012002464000` |
| data.riskScore.bizEntityKey | string |  | 例: `BROKERKEY` |
| data.riskScore.bizKey | string |  | 例: `BROKERKEY` |
| data.riskScore.kycUserId | string |  | 例: `4575836000526931200` |
| data.riskScore.riskScore | integer (int64) |  | 例: `31` |
| data.riskScore.riskLevel | string |  | 例: `MEDIUM` |
| data.riskScore.dob | string |  | 例: `1986-08-14` |
| data.riskScore.pep | string |  | 例: `null` |
| data.riskScore.sanctionHit | string |  | 例: `null` |
| data.riskScore.documentHit | string |  | 例: `null` |
| data.riskScore.nationality | string |  | 例: `AE` |
| data.riskScore.residenceCountry | string |  | 例: `AE` |
| data.riskScore.kycLevelName | string |  | 例: `INTERMEDIATE` |
| data.riskScore.operator | string |  | 例: `null` |
| data.riskScore.remark | string |  | 例: `null` |
| data.riskScore.fiatCurrency | string |  | 例: `null` |
| data.riskScore.depositFiatDailyLimit | string |  | 例: `null` |
| data.riskScore.depositFiatMonthlyLimit | string |  | 例: `null` |
| data.riskScore.depositFiatYearlyLimit | string |  | 例: `null` |
| data.riskScore.depositFiatLifeTimeLimit | string |  | 例: `null` |
| data.riskScore.withdrawFiatDailyLimit | string |  | 例: `null` |
| data.riskScore.withdrawFiatMonthlyLimit | string |  | 例: `null` |
| data.riskScore.withdrawFiatYearlyLimit | string |  | 例: `null` |
| data.riskScore.withdrawFiatLifeTimeLimit | string |  | 例: `null` |
| data.riskScore.riskTemplate | string |  | 例: `DEFAULT` |
| data.riskScore.dbCreateTime | integer (int64) |  | 例: `1750699480048` |
| data.riskScore.dbModifyTime | integer (int64) |  | 例: `1750699480048` |
| data.riskScore.riskScoreDetail | string |  | 例: `null` |
| data.riskScore.adminVo | string |  | 例: `null` |
| data.riskScore.sourceType | string |  | 例: `NORMAL` |
| data.riskScore.sanctionHitEternal | string |  | 例: `null` |
| data.riskScore.adverseMediaEternal | string |  | 例: `null` |
| data.riskScore.dryRun | boolean |  | 例: `False` |
| data.levelInfo | object |  |  |
| data.levelInfo.currentLevel | object |  |  |
| data.levelInfo.currentLevel.levelName | string |  | 例: `INTERMEDIATE` |
| data.levelInfo.currentLevel.levelDesc | string |  | 例: `INTERMEDIATE` |
| data.levelInfo.currentLevel.kycStatus | string |  | 例: `REFUSED` |
| data.levelInfo.currentLevel.kycLevelSubStatus | string |  | 例: `null` |
| data.levelInfo.currentLevel.limit | object |  |  |
| data.levelInfo.currentLevel.limit.fiatCurrency | string |  | 例: `USD` |
| data.levelInfo.currentLevel.limit.depositFiatDailyLimit | string |  | 例: `null` |
| data.levelInfo.currentLevel.limit.withdrawFiatDailyLimit | integer (int64) |  | 例: `20000` |
| data.levelInfo.currentLevel.limit.totalFiatDailyLimit | string |  | 例: `null` |
| data.levelInfo.currentLevel.limit.depositFiatMonthlyLimit | string |  | 例: `null` |
| data.levelInfo.currentLevel.limit.withdrawFiatMonthlyLimit | string |  | 例: `null` |
| data.levelInfo.currentLevel.limit.totalFiatMonthlyLimit | string |  | 例: `null` |
| data.levelInfo.currentLevel.limit.depositFiatYearlyLimit | string |  | 例: `null` |
| data.levelInfo.currentLevel.limit.withdrawFiatYearlyLimit | string |  | 例: `null` |
| data.levelInfo.currentLevel.limit.totalFiatYearlyLimit | string |  | 例: `null` |
| data.levelInfo.currentLevel.limit.depositFiatLifeTimeLimit | string |  | 例: `null` |
| data.levelInfo.currentLevel.limit.withdrawFiatLifeTimeLimit | string |  | 例: `null` |
| data.levelInfo.currentLevel.limit.totalFiatLifeTimeLimit | string |  | 例: `null` |
| data.levelInfo.currentLevel.limit.cryptoCurrency | string |  | 例: `BTC` |
| data.levelInfo.currentLevel.limit.depositCryptoDailyLimit | integer (int64) |  | 例: `-1` |
| data.levelInfo.currentLevel.limit.withdrawCryptoDailyLimit | integer (int64) |  | 例: `100` |
| data.levelInfo.currentLevel.limit.totalCryptoDailyLimit | string |  | 例: `null` |
| data.levelInfo.completedLevel | string |  | 例: `null` |
| data.levelInfo.passedLevel | string |  | 例: `null` |
| data.levelInfo.definedKycPassLevel | object |  |  |
| data.levelInfo.definedKycPassLevel.levelName | string |  | 例: `INTERMEDIATE` |
| data.levelInfo.definedKycPassLevel.levelDesc | string |  | 例: `INTERMEDIATE` |
| data.levelInfo.definedKycPassLevel.kycStatus | string |  | 例: `REFUSED` |
| data.levelInfo.definedKycPassLevel.kycLevelSubStatus | string |  | 例: `null` |
| data.levelInfo.definedKycPassLevel.limit | object |  |  |
| data.levelInfo.definedKycPassLevel.limit.fiatCurrency | string |  | 例: `USD` |
| data.levelInfo.definedKycPassLevel.limit.depositFiatDailyLimit | string |  | 例: `null` |
| data.levelInfo.definedKycPassLevel.limit.withdrawFiatDailyLimit | integer (int64) |  | 例: `20000` |
| data.levelInfo.definedKycPassLevel.limit.totalFiatDailyLimit | string |  | 例: `null` |
| data.levelInfo.definedKycPassLevel.limit.depositFiatMonthlyLimit | string |  | 例: `null` |
| data.levelInfo.definedKycPassLevel.limit.withdrawFiatMonthlyLimit | string |  | 例: `null` |
| data.levelInfo.definedKycPassLevel.limit.totalFiatMonthlyLimit | string |  | 例: `null` |
| data.levelInfo.definedKycPassLevel.limit.depositFiatYearlyLimit | string |  | 例: `null` |
| data.levelInfo.definedKycPassLevel.limit.withdrawFiatYearlyLimit | string |  | 例: `null` |
| data.levelInfo.definedKycPassLevel.limit.totalFiatYearlyLimit | string |  | 例: `null` |
| data.levelInfo.definedKycPassLevel.limit.depositFiatLifeTimeLimit | string |  | 例: `null` |
| data.levelInfo.definedKycPassLevel.limit.withdrawFiatLifeTimeLimit | string |  | 例: `null` |
| data.levelInfo.definedKycPassLevel.limit.totalFiatLifeTimeLimit | string |  | 例: `null` |
| data.levelInfo.definedKycPassLevel.limit.cryptoCurrency | string |  | 例: `BTC` |
| data.levelInfo.definedKycPassLevel.limit.depositCryptoDailyLimit | integer (int64) |  | 例: `-1` |
| data.levelInfo.definedKycPassLevel.limit.withdrawCryptoDailyLimit | integer (int64) |  | 例: `100` |
| data.levelInfo.definedKycPassLevel.limit.totalCryptoDailyLimit | string |  | 例: `null` |
| data.levelInfo.kycPass | boolean |  | 例: `False` |
| data.levelInfo.hasMultipleLevels | boolean |  | 例: `False` |
| data.levelInfo.passedLevels | string[] |  |  |
| data.nonExisted | string |  | 例: `null` |
| data.wckInfo | string |  | 例: `null` |
| success | boolean |  | 例: `True` |

## Query Linked Accounts Info（查询关联账户信息）

`POST /bapi/ekyc/v2/public/ekyc/customer/query-linked-accounts`

Query Linked Accounts Info

查询关联账户信息

Operation ID: `queryLinkedAccountsInfo`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-SHA2-Signature | header | string | 是 | Request signature. HMAC-SHA256 of the JSON request body, hex-encoded. See [API request signing](/products/kyc-saas/basics/2.request-signing).<br>请求签名。对 JSON 请求体进行 HMAC-SHA256 签名并以十六进制输出。参见 [API request signing](/products/kyc-saas/basics/2.request-signing)。<br>例: `SIGNATURE` |

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| bizEntityKey | string | 是 | business entity key, each access entity has its own bizEntityKey<br>业务实体标识，每个接入方实体都有其专属的 bizEntityKey。<br>例: `BROKERKEY` |
| entityCustomerId | string | 是 | customer id, that is, the user id of the access entity site. Not Required for OAuth Link<br>客户 ID，即接入方站点中的用户 ID；在 OAuth Link 场景下非必填。<br>例: `1` |
| brokerMainAccountId | string | 是 | Broker main account id<br>经纪商主账户 ID<br>例: `1` |
| openId | string |  | Required for Oauth Link<br>OAuth Link 场景必填。<br>例: `1` |
| oauthClientId | string |  | Required for Oauth Link<br>OAuth Link 场景必填。<br>例: `1` |

### 响应 200：Linked Accounts Info / 关联账户信息

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  | 例: `000000` |
| message | string |  | 例: `null` |
| messageDetail | string |  | 例: `null` |
| data | object |  |  |
| data.accountList | object[] |  |  |
| data.accountList[].brokerMainAccountId | string |  | 例: `123456789` |
| data.accountList[].brokerSubAccountId | string |  | 例: `45712345678999212345` |
| success | boolean |  | 例: `True` |

## Query Share KYC Info Status API（查询共享 KYC 信息状态接口）

`POST /bapi/ekyc/v2/public/ekyc/customer/query-share-data-status`

Query Share KYC Info Status API

查询共享 KYC 信息状态接口

Operation ID: `queryShareKycInfoStatusApi`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-SHA2-Signature | header | string | 是 | Request signature. HMAC-SHA256 of the JSON request body, hex-encoded. See [API request signing](/products/kyc-saas/basics/2.request-signing).<br>请求签名。对 JSON 请求体进行 HMAC-SHA256 签名并以十六进制输出。参见 [API request signing](/products/kyc-saas/basics/2.request-signing)。<br>例: `SIGNATURE` |

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| bizEntityKey | string | 是 | business entity key, each access entity has its own bizEntityKey<br>业务实体标识，每个接入方实体都有其专属的 bizEntityKey。<br>例: `BROKERKEY` |
| entityCustomerId | string | 是 | customer id, that is, the user id of the access entity site<br>客户 ID，即接入方站点中的用户 ID。<br>例: `1` |
| requestNo | string | 是 | Unique request number. To search a previous request, use the previous `requestNo`.<br>请求唯一编号。若要查询历史请求，请使用之前的 `requestNo`。<br>例: `6286de2c976243a38ce4da8bebc403cf` |

### 响应 200：Share KYC Info Status API / 共享 KYC 信息状态接口

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  | 例: `000000` |
| message | string |  | 例: `null` |
| messageDetail | string |  | 例: `null` |
| data | object |  | Share data status information<br>共享数据状态信息 |
| data.bizEntityKey | string |  | Business entity key<br>业务实体键<br>例: `abc123` |
| data.entityCustomerId | string |  | Entity customer ID<br>实体客户 ID<br>例: `customer001` |
| data.failMessage | string |  | Failure message if status is FAIL<br>失败原因（当状态为 FAIL 时）<br>例: `` |
| data.requestNo | string |  | Request number<br>请求编号<br>例: `req123456` |
| data.status | string |  | Sharing status: INIT, SUCCESS, FAIL<br>共享状态：INIT（初始化）、SUCCESS（成功）、FAIL（失败）<br>枚举: `INIT`, `SUCCESS`, `FAIL`<br>例: `SUCCESS` |
| success | boolean |  | 例: `True` |

## Refused User KYC Data（拒绝用户 KYC 数据）

`POST /bapi/ekyc/v2/public/ekyc/customer/refused-kyc-data`

Refuse User KYC Data

拒绝用户 KYC 数据

Operation ID: `refusedUserKycData`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-SHA2-Signature | header | string | 是 | Request signature. HMAC-SHA256 of the JSON request body, hex-encoded. See [API request signing](/products/kyc-saas/basics/2.request-signing).<br>请求签名。对 JSON 请求体进行 HMAC-SHA256 签名并以十六进制输出。参见 [API request signing](/products/kyc-saas/basics/2.request-signing)。<br>例: `SIGNATURE` |

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| bizEntityKey | string | 是 | business entity key, each access entity has its own bizEntityKey<br>业务实体标识，每个接入方实体都有其专属的 bizEntityKey。<br>例: `BROKERKEY` |
| entityCustomerId | string | 是 | customer id，that is, the user id of the access entity site<br>客户 ID，即接入方站点中的用户 ID。<br>例: `1` |

### 响应 200：Refused User KYC Data / 拒绝用户 KYC 数据

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  | 例: `000000` |
| message | string |  | 例: `null` |
| messageDetail | string |  | 例: `null` |
| data | string |  | 例: `null` |
| success | boolean |  | 例: `True` |

## Unlink User KYC Data（解除用户 KYC 数据关联）

`POST /bapi/ekyc/v2/public/ekyc/customer/unlink-kyc-data`

Unlink User KYC Data

解除用户 KYC 数据关联

Operation ID: `unlinkUserKycData`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-SHA2-Signature | header | string | 是 | Request signature. HMAC-SHA256 of the JSON request body, hex-encoded. See [API request signing](/products/kyc-saas/basics/2.request-signing).<br>请求签名。对 JSON 请求体进行 HMAC-SHA256 签名并以十六进制输出。参见 [API request signing](/products/kyc-saas/basics/2.request-signing)。<br>例: `SIGNATURE` |

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| bizEntityKey | string | 是 | business entity key, each access entity has its own bizEntityKey<br>业务实体标识，每个接入方实体都有其专属的 bizEntityKey。<br>例: `BROKERKEY` |
| entityCustomerId | string | 是 | customer id，that is, the user id of the access entity site<br>客户 ID，即接入方站点中的用户 ID。<br>例: `1` |
| brokerMainAccountId | string | 是 | broker main account id<br>经纪商主账户 ID。<br>例: `1` |
| brokerSubAccountId | string | 是 | broker sub account id<br>经纪商子账户 ID。<br>例: `1` |

### 响应 200：Unlink User KYC Data / 解除用户 KYC 数据关联

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  | 例: `000000` |
| message | string |  | 例: `null` |
| messageDetail | string |  | 例: `null` |
| data | string |  | 例: `null` |
| success | boolean |  | 例: `True` |