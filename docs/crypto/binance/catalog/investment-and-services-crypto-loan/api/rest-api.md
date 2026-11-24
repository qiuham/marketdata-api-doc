---
exchange: binance
source_url: https://developers.binance.com/en/docs/catalog/investment-and-services-crypto-loan/api/rest-api
api_type: REST
updated_at: 2026-11-24 18:49:21.733681
---

# Crypto Loan REST API

Schema: https://developers.binance.com/en/docs/catalog/investment-and-services-crypto-loan/api/rest-api/1.0.0/schema.yaml

Access Binance Crypto Loans to query assets, subscribe to loans, and manage loan positions.

访问 Binance 加密货币借贷服务，以查询资产、申购借贷并管理借贷仓位。

版本: 1.0.0

## 服务地址

- `https://api.binance.com`
- `https://api-gcp.binance.com`
- `https://api1.binance.com`
- `https://api2.binance.com`
- `https://api3.binance.com`
- `https://api4.binance.com`

## 接口列表

- `GET /sapi/v2/loan/flexible/repay/rate` — Check Collateral Flexible Repay Rate (USER_DATA)
- `POST /sapi/v2/loan/flexible/adjust/ltv` — Flexible Loan Adjust LTV (TRADE)
- `POST /sapi/v2/loan/flexible/borrow` — Flexible Loan Borrow (TRADE)
- `POST /sapi/v2/loan/flexible/repay` — Flexible Loan Repay (TRADE)
- `GET /sapi/v2/loan/flexible/loanable/data` — Get Flexible Loan Assets Data (USER_DATA)
- `GET /sapi/v2/loan/flexible/borrow/history` — Get Flexible Loan Borrow History (USER_DATA)
- `GET /sapi/v2/loan/flexible/collateral/data` — Get Flexible Loan Collateral Assets Data (USER_DATA)
- `GET /sapi/v2/loan/interestRateHistory` — Get Flexible Loan Interest Rate History (USER_DATA)
- `GET /sapi/v2/loan/flexible/liquidation/history` — Get Flexible Loan Liquidation History (USER_DATA)
- `GET /sapi/v2/loan/flexible/ltv/adjustment/history` — Get Flexible Loan LTV Adjustment History (USER_DATA)
- `GET /sapi/v2/loan/flexible/ongoing/orders` — Get Flexible Loan Ongoing Orders (USER_DATA)
- `GET /sapi/v2/loan/flexible/repay/history` — Get Flexible Loan Repayment History (USER_DATA)

## Check Collateral Flexible Repay Rate (USER_DATA)（查询抵押还款汇率 (USER_DATA)）

`GET /sapi/v2/loan/flexible/repay/rate`

Get the latest rate of collateral coin/loan coin when using collateral repay.

获取使用抵押还款时的抵押币/借币最新汇率。

Operation ID: `checkCollateralRepayRate`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| loanCoin | query | string | 是 | 例: `BUSD` |
| collateralCoin | query | string | 是 | 例: `BNB` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Check Collateral Repay Rate / 查询抵押还款汇率

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| loanCoin | string |  | 例: `BUSD` |
| collateralCoin | string |  | 例: `BNB` |
| rate | string |  | rate of collateral coin/loan coin<br>例: `300.36781234` |

## Flexible Loan Adjust LTV (TRADE)（活期借币调整质押率 (TRADE)）

`POST /sapi/v2/loan/flexible/adjust/ltv`

Flexible Loan Adjust LTV

活期借币调整质押率

Operation ID: `flexibleLoanAdjustLtv`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| loanCoin | string | 是 | 例: `BUSD` |
| collateralCoin | string | 是 | 例: `BNB` |
| adjustmentAmount | number (float) | 是 | 例: `1` |
| direction | string | 是 | 枚举: `ADDITIONAL`, `REDUCED`<br>例: `ADDITIONAL` |
| recvWindow | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Flexible Loan Adjust LTV / 活期借币调整质押率

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| loanCoin | string |  | 例: `BUSD` |
| collateralCoin | string |  | 例: `BNB` |
| direction | string |  | 例: `ADDITIONAL` |
| adjustmentAmount | string |  | 例: `5.235` |
| currentLTV | string |  | 例: `0.52` |
| status | string |  | Succeeds, Failed, Processing<br>Succeeds（成功）、Failed（失败）、Processing（处理中）<br>例: `Succeeds` |

## Flexible Loan Borrow (TRADE)（活期借币借贷 (TRADE)）

`POST /sapi/v2/loan/flexible/borrow`

Borrow Flexible Loan

借入活期借币。

Operation ID: `flexibleLoanBorrow`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| loanCoin | string | 是 | 例: `BUSD` |
| loanAmount | number (float) |  | Mandatory when collateralAmount is empty<br>当 collateralAmount 为空时，需必填<br>例: `1` |
| collateralCoin | string | 是 | 例: `BNB` |
| collateralAmount | number (float) |  | Mandatory when loanAmount is empty<br>当 loanAmount 为空时，需必填<br>例: `1` |
| recvWindow | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Flexible Loan Borrow / 活期借币借贷

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| loanCoin | string |  | 例: `BUSD` |
| loanAmount | string |  | 例: `100.5` |
| collateralCoin | string |  | 例: `BNB` |
| collateralAmount | string |  | 例: `50.5` |
| status | string |  | Succeeds, Failed, Processing<br>例: `Succeeds` |

## Flexible Loan Repay (TRADE)（活期借币还款 (TRADE)）

`POST /sapi/v2/loan/flexible/repay`

Flexible Loan Repay

活期借币还款

Operation ID: `flexibleLoanRepay`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| loanCoin | string | 是 | 例: `BUSD` |
| collateralCoin | string | 是 | 例: `BNB` |
| repayAmount | number (float) | 是 | 例: `1` |
| collateralReturn | boolean |  | TRUE: Return extra collateral to spot account; FALSE: Keep extra collateral in the order and lower<br>LTV.<br>TRUE：多余抵押金退回现货钱包；FALSE：多余抵押金保留在原订单中并降低 LTV。<br>默认: `True`<br>例: `True` |
| fullRepayment | boolean |  | TRUE: Full repayment; FALSE: Partial repayment based on loan amount<br>TRUE：全部偿还；FALSE：按借贷金额部分偿还。<br>默认: `False`<br>例: `False` |
| repaymentType | integer (int64) |  | 1: Repayment with loan asset; 2: Repayment with collateral<br>1：借贷资产还款；2：抵押物还款。<br>枚举: `1`, `2`<br>默认: `1`<br>例: `1` |
| recvWindow | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Flexible Loan Repay / 活期借币还款

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| loanCoin | string |  | 例: `BUSD` |
| collateralCoin | string |  | 例: `BNB` |
| remainingDebt | string |  | 例: `100.5` |
| remainingCollateral | string |  | 例: `5.253` |
| fullRepayment | boolean |  | 例: `False` |
| currentLTV | string |  | 例: `0.25` |
| repayStatus | string |  | REPAID, REPAYING, FAILED<br>REPAID（已还款）、REPAYING（还款中）、FAILED（失败）<br>例: `REPAID` |

## Get Flexible Loan Assets Data (USER_DATA)（查询活期借币可借币种数据 (USER_DATA)）

`GET /sapi/v2/loan/flexible/loanable/data`

Get interest rate and borrow limit of flexible loanable assets. The borrow limit is shown in USD value.

获取活期借币可借币种的利率和借贷限额。借入限额以美元价值显示。

Operation ID: `getFlexibleLoanAssetsData`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| loanCoin | query | string |  | 例: `BUSD` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Flexible Loan Assets Data / 查询活期借币可借币种数据

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| rows | object[] |  |  |
| rows[].loanCoin | string |  | 例: `BUSD` |
| rows[].flexibleInterestRate | string |  | 例: `0.00000491` |
| rows[].flexibleMinLimit | string |  | 例: `100` |
| rows[].flexibleMaxLimit | string |  | 例: `1000000` |
| total | integer (int64) |  | 例: `1` |

## Get Flexible Loan Borrow History (USER_DATA)（查询活期借币历史记录 (USER_DATA)）

`GET /sapi/v2/loan/flexible/borrow/history`

Get Flexible Loan Borrow History.

查询活期借币借款历史。

Operation ID: `getFlexibleLoanBorrowHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| loanCoin | query | string |  | 例: `BUSD` |
| collateralCoin | query | string |  | 例: `BNB` |
| startTime | query | integer (int64) |  | 例: `1623319461670` |
| endTime | query | integer (int64) |  | 例: `1641782889000` |
| current | query | integer (int64) |  | Current querying page<br>当前查询页<br>默认: `1`<br>例: `1` |
| limit | query | integer (int64) |  | Number of records to return<br>返回记录数量<br>默认: `10`<br>例: `10` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Flexible Loan Borrow History / 查询活期借币历史记录

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| rows | object[] |  |  |
| rows[].loanCoin | string |  | 例: `BUSD` |
| rows[].initialLoanAmount | string |  | 例: `10000` |
| rows[].collateralCoin | string |  | 例: `BNB` |
| rows[].initialCollateralAmount | string |  | 例: `49.27565492` |
| rows[].borrowTime | integer (int64) |  | 例: `1575018510000` |
| rows[].status | string |  | SUCCESS, FAILED, PENDING<br>例: `SUCCESS` |
| total | integer (int64) |  | 例: `1` |

## Get Flexible Loan Collateral Assets Data (USER_DATA)（查询活期借币抵押币种数据 (USER_DATA)）

`GET /sapi/v2/loan/flexible/collateral/data`

Get LTV information and collateral limit of flexible loan's collateral assets. The collateral limit is shown in
USD value.

获取活期借币抵押币种质押率信息和质押限额。质押限额以美元价值显示。

Operation ID: `getFlexibleLoanCollateralAssetsData`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| collateralCoin | query | string |  | 例: `BNB` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Flexible Loan Collateral Assets Data / 查询活期借币抵押币种数据

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| rows | object[] |  |  |
| rows[].collateralCoin | string |  | 例: `BNB` |
| rows[].initialLTV | string |  | 例: `0.65` |
| rows[].marginCallLTV | string |  | 例: `0.75` |
| rows[].liquidationLTV | string |  | 例: `0.83` |
| rows[].maxLimit | string |  | 例: `1000000` |
| total | integer (int64) |  | 例: `1` |

## Get Flexible Loan Interest Rate History (USER_DATA)（获取活期借币利率历史 (USER_DATA)）

`GET /sapi/v2/loan/interestRateHistory`

Check Flexible Loan interest rate history

查询活期借币利率历史

Operation ID: `getFlexibleLoanInterestRateHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| coin | query | string | 是 | 例: `USDT` |
| startTime | query | integer (int64) |  | 例: `1623319461670` |
| endTime | query | integer (int64) |  | 例: `1641782889000` |
| current | query | integer (int64) |  | Current querying page<br>当前查询页<br>默认: `1`<br>例: `1` |
| limit | query | integer (int64) |  | Number of records to return<br>返回记录数量<br>默认: `10`<br>例: `10` |
| recvWindow | query | integer (int64) | 是 | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Flexible Loan Interest Rate History / 获取活期借币利率历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| rows | object[] |  |  |
| rows[].coin | string |  | 例: `USDT` |
| rows[].annualizedInterestRate | string |  | 例: `0.0647` |
| rows[].time | integer (int64) |  | 例: `1575018510000` |
| total | integer (int64) |  | 例: `2` |

## Get Flexible Loan Liquidation History (USER_DATA)（查询活期借币清算历史记录 (USER_DATA)）

`GET /sapi/v2/loan/flexible/liquidation/history`

Get Flexible Loan Liquidation History

查询活期借币清算历史记录。

Operation ID: `getFlexibleLoanLiquidationHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| loanCoin | query | string |  | 例: `BUSD` |
| collateralCoin | query | string |  | 例: `BNB` |
| startTime | query | integer (int64) |  | 例: `1623319461670` |
| endTime | query | integer (int64) |  | 例: `1641782889000` |
| current | query | integer (int64) |  | Current querying page<br>当前查询页<br>默认: `1`<br>例: `1` |
| limit | query | integer (int64) |  | Number of records to return<br>返回记录数量<br>默认: `10`<br>例: `10` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Flexible Loan Liquidation History / 查询活期借币清算历史记录

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| rows | object[] |  |  |
| rows[].loanCoin | string |  | 例: `BUSD` |
| rows[].liquidationDebt | string |  | 例: `10000` |
| rows[].collateralCoin | string |  | 例: `BNB` |
| rows[].liquidationCollateralAmount | string |  | 例: `123` |
| rows[].returnCollateralAmount | string |  | 例: `0.2` |
| rows[].liquidationFee | string |  | 例: `1.2` |
| rows[].liquidationStartingPrice | string |  | 例: `49.27565492` |
| rows[].liquidationStartingTime | integer (int64) |  | 例: `1575018510000` |
| rows[].status | string |  | Liquidating<br>例: `Liquidated` |
| total | integer (int64) |  | 例: `1` |

## Get Flexible Loan LTV Adjustment History (USER_DATA)（查询活期借币质押率调整历史 (USER_DATA)）

`GET /sapi/v2/loan/flexible/ltv/adjustment/history`

Get Flexible Loan LTV Adjustment History.

查询活期借币 LTV 调整历史。

Operation ID: `getFlexibleLoanLtvAdjustmentHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| loanCoin | query | string |  | 例: `BUSD` |
| collateralCoin | query | string |  | 例: `BNB` |
| startTime | query | integer (int64) |  | 例: `1623319461670` |
| endTime | query | integer (int64) |  | 例: `1641782889000` |
| current | query | integer (int64) |  | Current querying page<br>当前查询页<br>默认: `1`<br>例: `1` |
| limit | query | integer (int64) |  | Number of records to return<br>返回记录数量<br>默认: `10`<br>例: `10` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Flexible Loan LTV Adjustment History / 查询活期借币质押率调整历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| rows | object[] |  |  |
| rows[].loanCoin | string |  | 例: `BUSD` |
| rows[].collateralCoin | string |  | 例: `BNB` |
| rows[].direction | string |  | 例: `ADDITIONAL` |
| rows[].collateralAmount | string |  | 例: `5.235` |
| rows[].preLTV | string |  | 例: `0.78` |
| rows[].afterLTV | string |  | 例: `0.56` |
| rows[].adjustTime | integer (int64) |  | 例: `1575018510000` |
| total | integer (int64) |  | 例: `1` |

## Get Flexible Loan Ongoing Orders (USER_DATA)（查询活期借款中订单列表 (USER_DATA)）

`GET /sapi/v2/loan/flexible/ongoing/orders`

Get Flexible Loan Ongoing Orders

查询活期借款中订单列表

Operation ID: `getFlexibleLoanOngoingOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| loanCoin | query | string |  | 例: `BUSD` |
| collateralCoin | query | string |  | 例: `BNB` |
| current | query | integer (int64) |  | Current querying page<br>当前查询页<br>默认: `1`<br>例: `1` |
| limit | query | integer (int64) |  | Number of records to return<br>返回记录数量<br>默认: `10`<br>例: `10` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Flexible Loan Ongoing Orders / 查询活期借款中订单列表

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| rows | object[] |  |  |
| rows[].loanCoin | string |  | 例: `BUSD` |
| rows[].totalDebt | string |  | 例: `10000` |
| rows[].collateralCoin | string |  | 例: `BNB` |
| rows[].collateralAmount | string |  | 例: `49.27565492` |
| rows[].currentLTV | string |  | 例: `0.57` |
| total | integer (int64) |  | 例: `1` |

## Get Flexible Loan Repayment History (USER_DATA)（查询活期借币还款记录历史 (USER_DATA)）

`GET /sapi/v2/loan/flexible/repay/history`

Get Flexible Loan Repayment History.

查询活期借币还款历史。

Operation ID: `getFlexibleLoanRepaymentHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| loanCoin | query | string |  | 例: `BUSD` |
| collateralCoin | query | string |  | 例: `BNB` |
| startTime | query | integer (int64) |  | 例: `1623319461670` |
| endTime | query | integer (int64) |  | 例: `1641782889000` |
| current | query | integer (int64) |  | Current querying page<br>当前查询页<br>默认: `1`<br>例: `1` |
| limit | query | integer (int64) |  | Number of records to return<br>返回记录数量<br>默认: `10`<br>例: `10` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Flexible Loan Repayment History / 查询活期借币还款记录历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| rows | object[] |  |  |
| rows[].loanCoin | string |  | 例: `BUSD` |
| rows[].repayAmount | string |  | 例: `10000` |
| rows[].collateralCoin | string |  | 例: `BNB` |
| rows[].collateralReturn | string |  | 例: `49.27565492` |
| rows[].repayStatus | string |  | REPAID, REPAYING, FAILED<br>例: `REPAID` |
| rows[].repayTime | integer (int64) |  | 例: `1575018510000` |
| total | integer (int64) |  | 例: `1` |