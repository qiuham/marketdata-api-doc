---
exchange: binance
source_url: https://developers.binance.com/en/docs/catalog/advanced-trading-institutional-loan/api/rest-api
api_type: REST
updated_at: 2026-11-25 18:49:29.406513
---

# Institutional Loan REST API

Schema: https://developers.binance.com/en/docs/catalog/advanced-trading-institutional-loan/api/rest-api/1.0.0/schema.yaml

Access institutional loan services for portfolio margin and futures trading.

访问机构借贷服务，用于统一账户和合约交易。

版本: 1.0.0

## 服务地址

- `https://api.binance.com`
- `https://api-gcp.binance.com`
- `https://api1.binance.com`
- `https://api2.binance.com`
- `https://api3.binance.com`
- `https://api4.binance.com`

## 接口列表

- `POST /sapi/v1/margin/loan-group/edit-member` — Add Collateral Accounts (TRADE)
- `GET /sapi/v1/margin/loan-group` — Query One Risk Unit Detail (USER_DATA)
- `DELETE /sapi/v1/margin/loan-group` — Close Risk Unit (TRADE)
- `GET /sapi/v1/margin/loan-groups/closed` — Query Closed Risk Unit Record (USER_DATA)
- `GET /sapi/v1/margin/loan-groups/activated` — Query Active Risk Units (USER_DATA)
- `GET /sapi/v1/margin/loan-group/ltv-details` — Query Risk Unit Details (USER_DATA)
- `POST /sapi/v1/margin/loan-group/borrow` — Risk Unit Borrow (TRADE)
- `GET /sapi/v1/margin/loan-group/borrow-repay` — Risk Unit Borrow/Repay Records (USER_DATA)
- `GET /sapi/v1/margin/loan-group/interest-history` — Risk Unit Interest History (USER_DATA)
- `POST /sapi/v1/margin/loan-group/repay` — Risk Unit Repay (TRADE)
- `GET /sapi/v1/margin/loan-group/interest-rebate-balance` — Query Interest Rebate Balance (USER_DATA)
- `GET /sapi/v1/margin/loan-group/interest-rebate-balance/records` — Query Interest Rebate Balance Records (USER_DATA)
- `GET /sapi/v1/margin/loan-group/max-borrowable` — Query Loan Group Max Borrowable (USER_DATA)
- `GET /sapi/v1/margin/loan-group/force-liquidation` — Get Risk Unit Force Liquidation Record (USER_DATA)
- `GET /sapi/v1/margin/loan-group/liquidation-transfer-record` — Query Risk Unit Liquidation Transfer Records (USER_DATA)
- `POST /sapi/v1/margin/loan-group/transfer-out` — Risk Unit Transfer (TRADE)

## Add Collateral Accounts (TRADE)（添加抵押子账户 (TRADE)）

`POST /sapi/v1/margin/loan-group/edit-member`

Add new collateral accounts for the Risk Unit. This endpoint is accessible only with the parent account API key.

* For the credit account, the enableMargin should always be TRUE.
* Collateral sub-accounts can be added to the Risk Unit but cannot be removed. Therefore, the enableSpot or enableMargin parameters cannot be switched from TRUE to FALSE once the sub-account is activated in the Risk Unit. If you need to remove credit or collateral sub-accounts from the Risk Unit, please contact the Binance Margin team for support.

添加风险单位的抵押子账户，仅支持母账户调用该接口。

* 如果参数subEmail 为信用贷账号，则参数enableMargin必须设置为TRUE，不能设置为FALSE。
* 参数enableSpot 和 enableMargin 只能从FALSE变更到TRUE，不能从TRUE变更到FALSE。即不能通过该接口移除抵押子账户，若想要移除抵押子账户，需联系杠杆团队。

Operation ID: `addCollateralAccounts`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| groupId | integer (int64) | 是 | 例: `1` |
| subEmail | string | 是 | 例: `abc@test.com` |
| enableSpot | boolean | 是 | 例: `True` |
| enableMargin | boolean | 是 | 例: `True` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Add Collateral Accounts / 添加抵押子账户

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| status | integer (int64) |  | 例: `0` |

## Query One Risk Unit Detail (USER_DATA)（查询单个风险单元详情 (USER_DATA)）

`GET /sapi/v1/margin/loan-group`

Query One Institution Loan Group Details which is executed by credit account

查询单个机构贷风险单位详情，仅支持放贷账户调用该接口。

Operation ID: `queryOneRiskUnitDetail`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：One Risk Unit Detail / 单个风险单元详情

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| groupId | integer (int64) |  | 例: `3` |
| parentEmail | string |  | 例: `parent001@test.com` |
| creditEmail | string |  | 例: `credit001@test.com` |
| updateTime | integer (int64) |  | 例: `1747910351205` |
| ltv | string |  | 例: `0.336` |
| totalNetEquity | string |  | 例: `598569.620904` |
| totalMaintenanceMargin | string |  | 例: `375.23555369` |
| totalLiability | string |  | 例: `200850.274625` |
| liabilities | object[] |  |  |
| liabilities[].assetName | string |  | 例: `USDT` |
| liabilities[].principal | string |  | 例: `200099.9` |
| liabilities[].interest | string |  | 例: `750.374625` |
| accountInfos | object[] |  |  |
| accountInfos[].email | string |  | 例: `collateral001@test.com` |
| accountInfos[].accountType | string |  | 例: `PORTFOLIO_MARGIN` |
| accountInfos[].netEquity | string |  | 例: `219961.43492975` |
| accountInfos[].maintainMargin | string |  | 例: `50.10676987` |

## Close Risk Unit (TRADE)（关闭风险单位 (TRADE)）

`DELETE /sapi/v1/margin/loan-group`

The closure of the Institutional Loan risk unit can only be initiated by API calls from the credit account. If
the closure is successful all the collateral accounts will be unlinked. Please note the following conditions
must be met:
  * The Institution Loan risk unit is active.
  * The outstanding institutional loan liabilities for that particular risk unit have been repaid.

关闭操作仅支持通过机构借贷子账户 API 执行。成功关闭后，系统将自动解除该风险单位与所有抵押账户的关联。请注意，操作前需满足以下条件：
  * 机构贷单位处于生效活跃状态。
  * 已全额偿还此风险单位内贷款及利息。

Operation ID: `closeRiskUnit`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| groupId | query | integer (int64) | 是 | Risk unit unique identifier<br>唯一风险单位标识符<br>例: `1` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Close Risk Unit / 关闭风险单位

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| groupId | integer (int64) |  | Risk unit unique identifier<br>唯一风险单位标识符<br>例: `10001` |
| status | string |  | CLOSED: This risk unit has been closed successfully<br>CLOSED: 此风险单位已成功关闭<br>例: `CLOSED` |

## Query Closed Risk Unit Record (USER_DATA)（查询关闭的风险单元记录 (USER_DATA)）

`GET /sapi/v1/margin/loan-groups/closed`

Query closed risk unit record. This endpoint is accessible only with the credit account API key.

查询已关闭的风险单元记录。仅支持放贷账户调用该接口。

Operation ID: `queryClosedRiskUnitRecord`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| current | query | integer (int64) |  | Current page number. Starts from 1.<br>当前页码，从 1 开始。<br>默认: `1`<br>例: `1` |
| size | query | integer (int64) |  | Number of records per page.<br>每页记录条数。<br>默认: `10`<br>例: `10` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Closed Risk Unit Records / 关闭的风险单元记录

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| total | integer (int64) |  | Total number of risk units returned by the query.<br>查询返回的风险单元总数。<br>例: `2` |
| rows | object[] |  |  |
| rows[].groupId | integer (int64) |  | Risk unit unique identifier.<br>唯一风险单位标识符。<br>例: `72` |
| rows[].parentEmail | string |  | Parent account  email<br>母账户邮箱。<br>例: `wdywgceiwbfq@test.com` |
| rows[].creditEmail | string |  | Credit account  email<br>放贷账户邮箱。<br>例: `wdywaxmzlnah@test.com` |
| rows[].enabled | boolean |  | The status of the group. TRUE for enabled; FALSE for disabled.<br>风险单位状态。TRUE 表示活跃；FALSE 表示关闭。<br>例: `False` |
| rows[].createTime | integer (int64) |  | The group create  timestamp (milliseconds)<br>风险单位创建时间戳（毫秒）。<br>例: `1753410654608` |
| rows[].closeTime | integer (int64) |  | The group close timestamp (milliseconds)<br>风险单位关闭时间戳（毫秒）。<br>例: `1753422899052` |

## Query Active Risk Units (USER_DATA)（查询有效风险单位 (USER_DATA)）

`GET /sapi/v1/margin/loan-groups/activated`

Retrieves the list of active institutional loan risk units. This endpoint is accessible only with the parent
account API key.

查询生效状态的机构贷风险单位列表。仅支持母账户查询该接口。

Operation ID: `queryActiveRiskUnits`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Active Risk Units

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].groupId | integer (int64) |  | Risk unit unique identifier<br>唯一风险单位标识符<br>例: `10001` |
| [].members | object[] |  |  |
| [].members[].email | string |  | Account registered email<br>账户注册邮箱<br>例: `1001@test.com` |
| [].members[].type | string |  | Credit sub account or Collateral sub account<br>放贷子账户或抵押子账户<br>例: `CREDIT` |
| [].members[].enableMargin | boolean |  | TRUE: include margin account as collateral. <br />FALSE: exclude margin account as collateral<br>TRUE: 杠杆账户包括在抵押账户内；FALSE: 杠杆账户不包括在抵押账户内<br>例: `True` |
| [].members[].enableSpot | boolean |  | TRUE: include spot account as collateral<br />FALSE: exclude spot account as collateral<br>TRUE: 现货账户包括在抵押账户内；FALSE: 现货账户不包括在抵押账户内<br>例: `True` |
| [].createTime | integer (int64) |  | Last update timestamp in milliseconds<br>最后更新时间戳（毫秒）<br>例: `1747637956083` |

## Query Risk Unit Details (USER_DATA)（查询风险单元详情 (USER_DATA)）

`GET /sapi/v1/margin/loan-group/ltv-details`

Queries institutional loan risk unit details. Both master accounts and borrowing accounts can call this
endpoint.

* Master account:
  * If `groupId` is not provided, details of all risk units are returned.
  * If a specific `groupId` is provided, details of that risk unit are returned.

* Borrowing account:
  * Only risk units bound to that borrowing account can be queried.

* Other account types:
  * LTV details cannot be queried and no results are returned.

查询机构贷风险单位详情，母账户和借贷账户均可调用该接口。

* 母账户：

* 当未提供 groupId 时，可以查询所有风险单位详情。
* 当提供特定 groupId 时，可以查询单个风险单位详情。
* 信用账户：

* 仅支持查询与该借贷账户绑定的风险单位详情。
* 其他账户：

* 无法查询LTV详情，无结果返回。

Operation ID: `queryRiskUnitDetails`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| groupId | query | integer (int64) |  | Risk unit unique identifier<br>唯一风险单位标识符<br>例: `1` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Risk Unit Details

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].groupId | integer (int64) |  | 例: `1` |
| [].leverageTier | string |  | Leverage tier of the risk unit, e.g. `5X`. It determines the LTV thresholds below.<br>风险单位的杠杆档位，例如 `5X`，决定以下各 LTV 阈值。<br>例: `5X` |
| [].initialLtv | string |  | Initial LTV threshold. A new borrow is rejected if it would raise the risk unit LTV above this value.<br>初始 LTV 阈值。若新借款会使风险单位 LTV 超过该值，借款将被拒绝。<br>例: `0.8` |
| [].marginCallLtv | string |  | Margin call LTV threshold. A margin call is triggered when the risk unit LTV reaches this value.<br>追加保证金 LTV 阈值。风险单位 LTV 达到该值时触发追加保证金通知。<br>例: `0.85` |
| [].liquidationLtv | string |  | Liquidation LTV threshold. Liquidation of the risk unit is triggered when its LTV reaches this value.<br>强平 LTV 阈值。风险单位 LTV 达到该值时触发强制平仓。<br>例: `0.9` |
| [].liquidationExitLtv | string |  | Liquidation exit LTV threshold. Liquidation stops once the risk unit LTV falls below this value.<br>强平结束 LTV 阈值。风险单位 LTV 降至该值以下时停止强平。<br>例: `0.8` |
| [].maxTransferOutLtv | string |  | Transfer-out LTV threshold. Assets can be transferred out of the risk unit only while `transferOutLtv` is below this value.<br>允许划出的 LTV 阈值。仅当 `transferOutLtv` 低于该值时，才可从风险单位划出资产。<br>例: `0.83` |
| [].parentEmail | string |  | 例: `andrew.kemmer001@test.com` |
| [].creditEmail | string |  | 例: `tst20241120@test.com` |
| [].updateTime | integer (int64) |  | 例: `1752137105623` |
| [].ltv | string |  | 例: `0.592` |
| [].totalNetEquity | string |  | 例: `26.35196946` |
| [].totalMaintenanceMargin | string |  | 例: `0.50106177` |
| [].totalLiability | string |  | 例: `15.30718771` |
| [].transferOutLtv | string |  | LTV used for transfer-out checks. Calculated in the same way as `ltv`, but only the net equity of Cross Margin and Portfolio Margin accounts is counted; collateral in Spot wallets is excluded, so it can be higher than `ltv`. `maxTransferOutAmount` and `parentAccountFrozenAmount` are based on this value.<br>用于划出校验的 LTV。计算方式与 `ltv` 相同，但仅计入全仓杠杆账户和统一账户的净资产，不计入现货钱包中的抵押品，因此可能高于 `ltv`。`maxTransferOutAmount` 与 `parentAccountFrozenAmount` 均基于该值计算。<br>例: `0.61` |
| [].parentAccountFrozenAmount | string |  | 例: `8.18753688` |
| [].maxTransferOutAmount | string |  | 例: `0` |
| [].maxAllowedBorrowLimit | string |  | The USDT-equivalent maximum borrowable amount for this risk unit. Note: this value does not account for the borrowed asset's collateral ratio. For assets with a collateral ratio below 100%, the actual maximum borrowable quantity still considers the borrowed asset's collateral ratio. The applicable collateral ratio depends on the margin mode of the credit account.<br>该风险单元的最大可借金额（以 USDT 等值计算）。注意：此数值未计入借入资产的抵押率。对于抵押率低于 100% 的借入资产，实际最大可借数量还需考虑借入资产的抵押率。适用的抵押率取决于放贷账户的杠杆模式。<br>例: `16.32397222` |
| [].liabilities | object[] |  |  |
| [].liabilities[].assetName | string |  | 例: `USDT` |
| [].liabilities[].principal | string |  | 例: `15.30718771` |
| [].liabilities[].interest | string |  | 例: `0` |
| [].collateralAccounts | object[] |  |  |
| [].collateralAccounts[].email | string |  | 例: `collateral001@test.com` |
| [].collateralAccounts[].type | string |  | 例: `COLLATERAL` |
| [].collateralAccounts[].wallets | object[] |  |  |
| [].collateralAccounts[].wallets[].accountType | string |  | 例: `SPOT` |
| [].collateralAccounts[].wallets[].netEquity | string |  | 例: `5` |
| [].collateralAccounts[].wallets[].maintainMargin | string |  | 例: `0` |

## Risk Unit Borrow (TRADE)（风险单位借款 (TRADE)）

`POST /sapi/v1/margin/loan-group/borrow`

This endpoint is used to perform a borrow request for that specified risk unit. This endpoint is accessible only
with the credit account API key.

* You need to open **Enable Spot & Margin Trading** permission for the API Key which requests this endpoint.
* The `amount` field refers to the quantity of the borrowed asset. The maximum allowable amount is subject to collateral ratio adjustment. The applicable collateral ratio depends on the margin mode of the credit account.

机构贷风险单位借款。仅支持放贷账户调用该接口。

* 您需要打开 API Key 的 **Spot & Margin Trading** 权限以使用此接口。
* `amount` 字段为借入资产的数量。最大可借数量须经抵押率调整，适用的抵押率取决于放贷账户的杠杆模式。

Operation ID: `riskUnitBorrow`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| groupId | integer (int64) | 是 | 例: `1` |
| assetName | string | 是 | Asset Name , USDT or USDC or BTC or U<br>资产名称，如 USDT 或 USDC 或 BTC 或 U<br>例: `USDT` |
| amount | number (float) | 是 | 例: `1` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Risk Unit Borrow / 风险单位借款

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| transactionId | integer (int64) |  | 例: `12317283617` |
| amount | number (float) |  | 例: `123456.78` |
| status | string |  | 例: `success` |

## Risk Unit Borrow/Repay Records (USER_DATA)（查询风险单元借贷/还款记录 (USER_DATA)）

`GET /sapi/v1/margin/loan-group/borrow-repay`

Get borrow/repay records in the Institution Loan Risk Unit. This endpoint is accessible only with the credit account API key.

查询风险单位借贷/还款记录，仅支持放贷账户调用该接口。

Operation ID: `riskUnitBorrowRepayRecords`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| groupId | query | integer (int64) |  | Risk unit unique identifier<br>唯一风险单位标识符<br>例: `1` |
| type | query | string | 是 | BORROW or REPAY<br>操作类型：BORROW 或 REPAY<br>枚举: `BORROW`, `REPAY`<br>例: `BORROW` |
| asset | query | string |  | Asset name, for example USDT or USDC<br>资产名称，例如 USDT 或 USDC<br>例: `USDT` |
| startTime | query | integer (int64) |  | Start time in milliseconds.<br>开始时间戳（毫秒）。<br>例: `1750420000000` |
| endTime | query | integer (int64) |  | End time in milliseconds.<br>结束时间戳（毫秒）。<br>例: `1750420899036` |
| current | query | integer (int64) |  | Current page number. Starts from 1.<br>当前页码，从 1 开始。<br>默认: `1`<br>例: `1` |
| size | query | integer (int64) |  | Number of records per page.<br>每页记录条数。<br>默认: `10`<br>例: `10` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds.<br>请求有效时间窗口，单位为毫秒。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Risk Unit Borrow/Repay Records / 风险单元借贷/还款记录

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| total | integer (int64) |  | 例: `1` |
| rows | object[] |  |  |
| rows[].tranId | integer (int64) |  | 例: `1648963682` |
| rows[].assetName | string |  | 例: `USDT` |
| rows[].amount | number (float) |  | 例: `300` |
| rows[].principal | number (float) |  | 例: `298` |
| rows[].interest | number (float) |  | 例: `2` |
| rows[].status | string |  | 例: `CONFIRM` |
| rows[].type | string |  | BORROW, NORMAL_REPAY, FORCE_REPAY<br>BORROW、NORMAL_REPAY、FORCE_REPAY<br>例: `BORROW` |
| rows[].timestamp | integer (int64) |  | Create Time<br>例: `1750420899036` |

## Risk Unit Interest History (USER_DATA)（风险单位历史利息 (USER_DATA)）

`GET /sapi/v1/margin/loan-group/interest-history`

Query Institutional loan risk unit interest history. This endpoint is accessible only with the credit account
API key.

查询机构贷风险单位给定时间段内的利息历史记录。此接口仅可使用信用账户API Key访问。

Operation ID: `riskUnitInterestHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| groupId | query | integer (int64) |  | Unique risk unit identifier<br>唯一风险单位标识符<br>例: `1` |
| asset | query | string |  | Asset name, for example USDT or USDC.<br>资产名称，例如 USDT 或 USDC。<br>例: `USDT` |
| startTime | query | integer (int64) |  | Start time in milliseconds.<br>开始时间戳（毫秒）。<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | End time in milliseconds.<br>结束时间戳（毫秒）。<br>例: `1641782889000` |
| current | query | integer (int64) |  | Current page number. Starts from 1.<br>当前页码，从 1 开始。<br>默认: `1`<br>例: `1` |
| size | query | integer (int64) |  | Number of records per page.<br>每页记录条数。<br>默认: `10`<br>例: `10` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Risk Unit Interest History / 风险单位利息历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| total | integer (int64) |  | Number of historical interest records.<br>历史利息记录总数。<br>例: `2` |
| rows | object[] |  | Interest history records.<br>利息历史记录列表。 |
| rows[].groupId | integer (int64) |  | 例: `2` |
| rows[].assetName | string |  | 例: `USDC` |
| rows[].principal | number (float) |  | 例: `851340.57601652` |
| rows[].interestRate | number (float) |  | 例: `8.33e-06` |
| rows[].interest | number (float) |  | 例: `7.09447643` |
| rows[].interestTimestamp | integer (int64) |  | 例: `1746442800000` |

## Risk Unit Repay (TRADE)（风险单位还款 (TRADE)）

`POST /sapi/v1/margin/loan-group/repay`

This endpoint is used to perform full or partial repayment of the specified risk unit. This endpoint is
accessible only with the credit account API key.

By default (repayFrom=MARGIN), funds are deducted from the credit account's Margin account. When repayFrom=SPOT, funds are deducted directly from the credit account's Spot account.

* You need to open **Enable Spot & Margin Trading** permission for the API Key which requests this endpoint.

机构贷风险单位全部或部分还款，仅支持放贷账户调用该接口。

默认情况下（repayFrom=MARGIN），资金从放贷账户的杠杆账户中扣除。当 repayFrom=SPOT 时，资金直接从放贷账户的现货账户中扣除。

* 您需要打开 API Key 的 **Spot & Margin Trading** 权限以使用此接口。

Operation ID: `riskUnitRepay`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| groupId | integer (int64) | 是 | 例: `1` |
| assetName | string | 是 | Asset name to repay<br>还款资产名称<br>例: `USDT` |
| amount | number (float) | 是 | 例: `1` |
| repayFrom | string |  | Funding source for repayment. MARGIN (default): deduct from credit account's Margin account. SPOT: deduct directly from credit account's Spot account.<br>还款资金来源。MARGIN（默认）：从放贷账户杠杆账户扣款；SPOT：直接从放贷账户现货账户扣款。<br>例: `MARGIN` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Risk Unit Repay / 风险单位还款

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| transactionId | integer (int64) |  | 例: `12317283617` |
| amount | number (float) |  | 例: `123456.78` |
| repayFrom | string |  | Funding source used for this repayment.<br>还款资金来源。<br>例: `MARGIN` |

## Query Interest Rebate Balance (USER_DATA)（查询利息减免额度 (USER_DATA)）

`GET /sapi/v1/margin/loan-group/interest-rebate-balance`

Query the interest rebate balance for an institutional loan master account, including the remaining balance, total granted amount, and total consumed amount, all denominated in USDT. This endpoint requires authentication with the parent account API key.

查询机构借贷的利息减免额度，包括剩余可用额度、累计发放金额及累计消耗金额，所有金额均以 USDT 计价。仅支持母账户调用该接口。

Operation ID: `queryInterestRebateBalance`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Query Interest Rebate Balance / 查询利息减免额度

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| asset | string |  | Asset name<br>资产名称<br>例: `USDT` |
| balance | string |  | Current rebate balance remaining; represents the amount still available to offset future interest charges<br>当前剩余可用利息减免额度，代表仍可用于抵扣未来机构借贷利息的金额<br>例: `91.64958606` |
| totalGranted | string |  | The total rebate amount that has ever been credited to your account<br>账户累计获得的减免总金额<br>例: `150.00000000` |
| totalConsumed | string |  | The total rebate amount that has already been used up to pay off interest<br>已用于抵扣利息的减免总金额<br>例: `58.35041394` |

## Query Interest Rebate Balance Records (USER_DATA)（查询利息减免额度变动记录 (USER_DATA)）

`GET /sapi/v1/margin/loan-group/interest-rebate-balance/records`

Query change records for an institutional loan interest rebate balance. Includes ADD (admin grant), DEDUCT (admin deduction), and INTEREST_OFFSET (system interest deduction) types.

查询机构贷利息减免额度的加减流水。包括发放(ADD)、扣减(DEDUCT)、利息抵扣(INTEREST_OFFSET)三种类型。

Operation ID: `queryInterestRebateBalanceRecords`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| type | query | integer |  | Record type filter: 0=ADD, 1=DEDUCT, 2=INTEREST_OFFSET. Returns all if not specified.<br>记录类型筛选: 0=发放, 1=扣减, 2=利息抵扣。不传则返回全部。<br>枚举: `0`, `1`, `2`<br>例: `0` |
| startTime | query | integer (int64) |  | Start time in ms<br>开始时间（毫秒）<br>例: `1711843200000` |
| endTime | query | integer (int64) |  | End time in ms<br>结束时间（毫秒）<br>例: `1712102400000` |
| current | query | integer (int64) |  | Page number, default 1<br>页码，默认 1<br>默认: `1`<br>例: `1` |
| size | query | integer (int64) |  | Page size, default 10, max 100<br>每页数量，默认 10，最大 100<br>默认: `10`<br>例: `10` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Query Interest Rebate Balance Records / 查询利息减免额度变动记录

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| total | integer (int64) |  | Total number of records<br>记录总数<br>例: `3` |
| rows | object[] |  |  |
| rows[].type | string |  | ADD / DEDUCT / INTEREST_OFFSET<br>发放(ADD) / 扣减(DEDUCT) / 利息抵扣(INTEREST_OFFSET)<br>枚举: `ADD`, `DEDUCT`, `INTEREST_OFFSET`<br>例: `ADD` |
| rows[].groupId | integer (int64) |  | Loan group ID (only for INTEREST_OFFSET)<br>贷款组 ID（仅利息抵扣）<br>例: `10005` |
| rows[].rebateAsset | string |  | Rebate asset (USDT)<br>额度币种（USDT）<br>例: `USDT` |
| rows[].delta | string |  | Amount change. Positive for ADD, negative for DEDUCT/INTEREST_OFFSET<br>变动金额。发放为正，扣减/抵扣为负<br>例: `5000.00000000` |
| rows[].liabilityAsset | string |  | Liability asset (only for INTEREST_OFFSET)<br>负债币种（仅利息抵扣）<br>例: `BTC` |
| rows[].deductedInterest | string |  | Deducted interest in liability asset (only for INTEREST_OFFSET)<br>抵扣利息金额，以负债币种计（仅利息抵扣）<br>例: `0.00050123` |
| rows[].exchangeRate | string |  | Exchange rate snapshot (only for INTEREST_OFFSET)<br>汇率快照（仅利息抵扣）<br>例: `0.00001000` |
| rows[].createTime | integer (int64) |  | Record creation time in ms<br>记录创建时间（毫秒）<br>例: `1711843200000` |

## Query Loan Group Max Borrowable (USER_DATA)（查询风险单位最大可借金额 (USER_DATA)）

`GET /sapi/v1/margin/loan-group/max-borrowable`

Query the maximum borrowable amount of a given asset for an institutional loan risk unit.

This endpoint can be accessed using the API key from either the parent or the credit account:

- If the API key belongs to the **credit account**, `groupId` is optional. When omitted, the member's own risk unit is used; when provided, it must match the member's risk unit, otherwise an empty result is returned.
- If the API key belongs to the **parent account**, `groupId` is **required** and must be owned by the parent account, otherwise an empty result is returned.
- If the caller is neither the parent account nor the credit member of the group (e.g., a collateral member, or no matching risk unit), `maxBorrowableAmount` is returned as empty/null.

查询机构借贷风险单位内指定币种的最大可借金额。

本接口可使用母账户或放贷账户的 API Key 进行访问：

- 若 API key 属于**放贷账户 (credit account)**：`groupId` 可选。不传时使用该成员所属的风险单位；传了则必须与成员所属风险单位一致，否则返回空结果。
- 若 API key 属于**母账户**：`groupId` **必传**，且必须归属于该母账户，否则返回空结果。
- 若调用方既不是母账户也不是该风险单位的放贷账户（如抵押子账户，或没有匹配的风险单位）：`maxBorrowableAmount` 返回空/null。

Operation ID: `queryLoanGroupMaxBorrowable`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| groupId | query | integer (int64) |  | Loan group id. Optional when the API key belongs to the credit member; required when it belongs to the parent account.<br>风险单位组 ID。key 为 credit 成员时可选；key 为母账户时必填。<br>例: `123456789` |
| assetName | query | string | 是 | Asset to borrow, e.g., `USDT`. Case-insensitive (normalized to upper-case). Must be a borrowable asset, otherwise an error is returned.<br>借贷币种，如 `USDT`。大小写不敏感（自动转大写）。必须是可借币种，否则报错。<br>例: `USDT` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Query Loan Group Max Borrowable / 查询风险单位最大可借金额

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| maxBorrowableAmount | string |  | Max borrowable amount of the asset for the risk unit. Empty/null when the caller has no matching risk unit.<br>该风险单位下指定币种的最大可借金额。无匹配的风险单位时返回空/null。<br>例: `12345.67890000` |

## Get Risk Unit Force Liquidation Record (USER_DATA)（查询风险单元强制平仓记录 (USER_DATA)）

`GET /sapi/v1/margin/loan-group/force-liquidation`

Get institutional loan risk unit force liquidation records. This endpoint is accessible only with the credit account API key.

获取风险单位强制平仓记录。仅支持放贷账户调用该接口。

Operation ID: `getRiskUnitForceLiquidationRecord`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| groupId | query | integer (int64) |  | Risk unit unique identifier<br>唯一风险单位标识符<br>例: `6` |
| startTime | query | integer (int64) |  | Start time in milliseconds.<br>开始时间戳（毫秒）。<br>例: `1748381716906` |
| endTime | query | integer (int64) |  | End time in milliseconds.<br>结束时间戳（毫秒）。<br>例: `1748525848742` |
| current | query | integer (int64) |  | Current page number. Starts from 1.<br>当前页码，从 1 开始。<br>默认: `1`<br>例: `1` |
| size | query | integer (int64) |  | Number of records per page.<br>每页记录条数。<br>默认: `10`<br>例: `10` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds.<br>请求有效时间窗口，单位为毫秒。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Risk Unit Force Liquidation Records / 风险单元强制平仓记录

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| total | integer (int64) |  | Total risk unit number<br>风险单位数量<br>例: `2` |
| rows | object[] |  |  |
| rows[].groupId | integer (int64) |  | Risk unit unique identifier.<br>唯一风险单位标识符。<br>例: `6` |
| rows[].startLtv | integer (int64) |  | The initial LTV for the risk unit<br>初始贷款价值比。<br>例: `1` |
| rows[].endLtv | integer (int64) |  | The current LTV for the risk unit<br>最新贷款价值比。<br>例: `0` |
| rows[].liquidationStartTime | integer (int64) |  | Liquidation start timestamp (milliseconds)<br>强平开始时间（毫秒）。<br>例: `1748381716906` |
| rows[].liquidationEndTime | integer (int64) |  | Liquidation end timestamp (milliseconds)<br>强平结束时间（毫秒）。<br>例: `1748525848742` |
| rows[].totalNetEquity | string |  | ∑Equity in all PM sub account + ( ∑Collateral Value - ∑(Liability + Interest) in all Cross Margin account + Free accepted tokens in spot<br>Σ所有统一账户子账户抵押品权益 + Σ 抵押品价值 - Σ 全仓杠杆账户（负债 + 利息） + 现货可用资产<br>例: `16671.5507973` |
| rows[].totalMaintenanceMargin | string |  | Aggregated Maintenance Margin<br>维持保证金总额。<br>例: `0` |
| rows[].totalLiability | string |  | Outstanding Loan Principal + Outstanding Loan Interest<br>未偿还贷款本金 + 未偿还贷款利息<br>例: `16667.926` |
| rows[].liquidationSnapshot | object |  |  |
| rows[].liquidationSnapshot.snapshots | object[] |  |  |
| rows[].liquidationSnapshot.snapshots[].subEmail | string |  | Sub account registered email<br>子账户注册邮箱<br>例: `1000255973134@test.com` |
| rows[].liquidationSnapshot.snapshots[].memberType | string |  | member type, "CREDIT" or "COLLATERAL"<br>子账号类型，可取值"CREDIT" 或 "COLLATERAL"<br>例: `CREDIT` |
| rows[].liquidationSnapshot.snapshots[].walletType | string |  | SPOT or PORTFOLIO MARGIN or CROSS MARGIN ACCOUNT<br>钱包类型，可取值 "PORTFOLIO_MARGIN", "SPOT" 或 "CROSS_MARGIN"<br>例: `PORTFOLIO_MARGIN` |
| rows[].liquidationSnapshot.snapshots[].netEquity | string |  | account net equity<br>账户净资产<br>例: `12671.05079731` |
| rows[].liquidationSnapshot.snapshots[].maintainMargin | string |  | maintenance margin<br>维持保证金<br>例: `0E-8` |
| rows[].liquidationSnapshot.liabilities | object[] |  |  |
| rows[].liquidationSnapshot.liabilities[].assetName | string |  | asset name<br>币种名称<br>例: `USDT` |
| rows[].liquidationSnapshot.liabilities[].principal | string |  | outstanding principal<br>未偿还贷款本金<br>例: `11667.92600000` |
| rows[].liquidationSnapshot.liabilities[].interest | string |  | outstanding interest<br>未偿还利息<br>例: `5000.00000000` |

## Query Risk Unit Liquidation Transfer Records (USER_DATA)（查询机构贷强制平仓划转记录 (USER_DATA)）

`GET /sapi/v1/margin/loan-group/liquidation-transfer-record`

Query transfer records during institutional loan risk unit forced liquidation. This endpoint is accessible only with the credit account API key.

查询机构贷款风险单位强制平仓期间的资金划转记录。仅支持放贷账户调用该接口。

Operation ID: `queryRiskUnitLiquidationTransferRecords`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| startTime | query | integer (int64) |  | Start time in milliseconds.<br>开始时间戳（毫秒）。<br>例: `1765374361589` |
| endTime | query | integer (int64) |  | End time in milliseconds.<br>结束时间戳（毫秒）。<br>例: `1765378830528` |
| current | query | integer (int64) |  | Current page number. Starts from 1.<br>当前页码，从 1 开始。<br>默认: `1`<br>例: `1` |
| size | query | integer (int64) |  | Number of records per page.<br>每页记录条数。<br>默认: `10`<br>例: `10` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds.<br>请求有效时间窗口，单位为毫秒。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Forced Liquidation Transfer Records / 强制平仓划转记录

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| total | integer (int64) |  | 例: `2` |
| rows | object[] |  |  |
| rows[].liquidationId | integer (int64) |  | Risk unit liquidation unique identifier.<br>唯一风险单位强制平仓标识符。<br>例: `56` |
| rows[].liquidationTransferRecord | object[] |  | List of transfer records related to the liquidationId.<br>与 liquidationId 相关的划转记录列表。 |
| rows[].liquidationTransferRecord[].transferTime | integer (int64) |  | Timestamp of the transfer event.<br>划转时间戳。<br>例: `1765378400855` |
| rows[].liquidationTransferRecord[].fromUid | string |  | UID of the account transferring assets.<br>划出资产账号 UID。<br>例: `1000277033525` |
| rows[].liquidationTransferRecord[].fromAccountType | string |  | SPOT or PORTFOLIO_MARGIN or CROSS_MARGIN.<br>账户类型：SPOT、PORTFOLIO_MARGIN 或 CROSS_MARGIN。<br>例: `PORTFOLIO_MARGIN` |
| rows[].liquidationTransferRecord[].toUid | string |  | UID of the account receiving assets.<br>接收资产账号 UID。<br>例: `1000277033505` |
| rows[].liquidationTransferRecord[].toAccountType | string |  | SPOT or PORTFOLIO_MARGIN or CROSS_MARGIN.<br>账户类型：SPOT、PORTFOLIO_MARGIN 或 CROSS_MARGIN。<br>例: `PORTFOLIO_MARGIN` |
| rows[].liquidationTransferRecord[].status | string |  | Current transfer status.<br>当前划转状态。<br>例: `CONFIRM` |
| rows[].liquidationTransferRecord[].assets | object[] |  | Transferred asset list.<br>划转资产列表。 |
| rows[].liquidationTransferRecord[].assets[].assetName | string |  | Name of the transferred token.<br>划转资产名称。<br>例: `USDT` |
| rows[].liquidationTransferRecord[].assets[].amount | string |  | Amount of the transferred token.<br>划转资产金额。<br>例: `17750.6316` |

## Risk Unit Transfer (TRADE)（风险单位资金划转 (TRADE)）

`POST /sapi/v1/margin/loan-group/transfer-out`

When specified risk unit LTV thresholds and/or the relevant product transfer out rules are met, the Risk Unit Transfer API allows users to perform the following:

Transfer of assets from margin collateral/credit accounts to spot accounts with the same Spot UID. This endpoint is accessible via each of the credit/collateral accounts with its API Key or parent account .
Please Note: To transfer funds out of the Institutional Loan Risk Unit, first transfer to the spot wallet using the dedicated Risk Unit Transfer API. After that, use the Universal Transfer API to move the assets to an account outside of the risk unit.

For all other designated use cases shown below, please use the Universal Transfer API.

Transfer assets between Credit Account and other Margin Collateral Accounts within the risk unit without LTV restrictions. Please see Universal Transfer API, this needs to be done via master account API key.
Transfers between Spot collateral account and accounts outside of the risk unit.

当达到特定的风险单位 LTV 阈值和/或相关产品的转出规则时，风险单位资金划转 API 允许用户执行以下操作：

将资产从杠杆抵押账户或放贷账户转至相同现货 UID 下的现货账户，此接口可支持单个抵押账户或放贷账户调用，也可由母账户调用。
请注意：要将资金转出机构借贷风险单位，首先要使用机构借贷特定的转账 API 将资金转入现货钱包。然后，使用万向转账 API 将资产转移到风险单元之外的账户。

此外的划转场景，请您使用万向转账 API 操作。

资金在放贷账户与风险单位内其他杠杆抵押账户之间划转，此划转不受转出 LTV 的限制，此接口需要通过母账户 API Key 操作。
现货账户与风险单位外的账户之间转账。

Operation ID: `riskUnitTransfer`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| subEmail | string |  | When the parent account calls this endpoint, the subEmail field is mandatory. If left empty, error<br>code -27026 will be returned.<br/>When a credit or collateral account calls this endpoint, the<br>subEmail field may be omitted and will default to the account's own subEmail.<br/>If the wrong<br>subEmail is inputted, error code -3003 will be returned.<br>抵押子账户或放贷子账户的邮箱地址<br/>母账户调用该接口时，subEmail必填，为空则报错；<br/>放贷账户或抵押账户调用该接口时，subEmail可为空，默认为其本身subEmail.<br>例: `collateral001@test.com` |
| asset | string | 是 | Asset name, for example USDT or USDC<br>资产名称，例如 USDT 或 USDC<br>例: `USDT` |
| amount | number (float) | 是 | Transfer amount of the asset. The real transferred amount = min(risk unit max transfer amount, collateral account max transfer amount).<br>转出金额。 注意 实际可转出金额取值于 min(风险单位最大可转出金额, 抵押账号最大可转出金额)， 两者取小。<br>例: `1000.5` |
| recvWindow | integer (int64) |  | Request validity window in milliseconds.<br>请求有效时间窗口，单位为毫秒。<br>例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Risk Unit Transfer Out Submitted / 风险单位资金划转已提交