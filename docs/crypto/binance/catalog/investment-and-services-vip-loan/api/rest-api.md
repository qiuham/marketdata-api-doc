---
exchange: binance
source_url: https://developers.binance.com/en/docs/catalog/investment-and-services-vip-loan/api/rest-api
api_type: REST
updated_at: 2026-11-18 02:46:59.171715
---

# VIP Loan REST API

Schema: https://developers.binance.com/en/docs/catalog/investment-and-services-vip-loan/api/rest-api/1.0.0/schema.yaml

Access over-collateralized loan services, manage positions, and monitor collateral via the VIP Loan API.

通过 VIP Loan API 访问超额抵押借贷服务、管理仓位并监控抵押品。

版本: 1.0.0

## 服务地址

- `https://api.binance.com`
- `https://api-gcp.binance.com`
- `https://api1.binance.com`
- `https://api2.binance.com`
- `https://api3.binance.com`
- `https://api4.binance.com`

## 接口列表

- `GET /sapi/v1/loan/vip/request/interestRate` — Get Borrow Interest Rate (USER_DATA)
- `GET /sapi/v1/loan/vip/collateral/data` — Get Collateral Asset Data (USER_DATA)
- `GET /sapi/v1/loan/vip/loanable/data` — Get Loanable Assets Data (USER_DATA)
- `GET /sapi/v1/loan/vip/interestRateHistory` — Get VIP Loan Interest Rate History (USER_DATA)
- `GET /sapi/v1/loan/vip/fixed/market` — Query VIP Loan Fixed Rate Market (USER_DATA)
- `POST /sapi/v1/loan/vip/borrow` — VIP Loan Borrow (TRADE)
- `POST /sapi/v1/loan/vip/fixed/borrow` — VIP Loan Fixed Rate Borrow (TRADE)
- `POST /sapi/v1/loan/vip/renew` — VIP Loan Renew (TRADE)
- `POST /sapi/v1/loan/vip/repay` — VIP Loan Repay (TRADE)
- `GET /sapi/v1/loan/vip/collateral/account` — Check VIP Loan Collateral Account (USER_DATA)
- `GET /sapi/v1/loan/vip/accruedInterest` — Get VIP Loan Accrued Interest (USER_DATA)
- `GET /sapi/v1/loan/vip/ongoing/orders` — Get VIP Loan Ongoing Orders (USER_DATA)
- `GET /sapi/v1/loan/vip/repay/history` — Get VIP Loan Repayment History (USER_DATA)
- `GET /sapi/v1/loan/vip/request/data` — Query Application Status (USER_DATA)

## Get Borrow Interest Rate (USER_DATA)（查询借币利率 (USER_DATA)）

`GET /sapi/v1/loan/vip/request/interestRate`

Get Borrow Interest Rate

查询借币利率

Operation ID: `getBorrowInterestRate`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| loanCoin | query | string | 是 | Max 10 assets, Multiple split by ","<br>最多 10 个资产，多个资产用 "," 分隔<br>例: `BTC` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Borrow Interest Rate / 查询借币利率

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].asset | string |  | 例: `BUSD` |
| [].flexibleDailyInterestRate | string |  | 例: `0.001503` |
| [].flexibleYearlyInterestRate | string |  | 例: `0.548595` |
| [].time | integer (int64) |  | 例: `1577233578000` |

## Get Collateral Asset Data (USER_DATA)（查询 VIP 借币抵押币种数据 (USER_DATA)）

`GET /sapi/v1/loan/vip/collateral/data`

Get Collateral Asset Data

查询 VIP 借币抵押币种数据

Operation ID: `getCollateralAssetData`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| collateralCoin | query | string |  | 例: `BUSD` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Collateral Asset Data / 查询抵押资产数据

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| rows | object[] |  |  |
| rows[].collateralCoin | string |  | 例: `BUSD` |
| rows[]._1stCollateralRatio | string |  | 例: `100%` |
| rows[]._1stCollateralRange | string |  | 例: `1-10000000` |
| rows[]._2ndCollateralRatio | string |  | 例: `80%` |
| rows[]._2ndCollateralRange | string |  | 例: `10000000-100000000` |
| rows[]._3rdCollateralRatio | string |  | 例: `60%` |
| rows[]._3rdCollateralRange | string |  | 例: `100000000-1000000000` |
| rows[]._4thCollateralRatio | string |  | 例: `0%` |
| rows[]._4thCollateralRange | string |  | 例: `>10000000000` |
| total | integer (int64) |  | 例: `1` |

## Get Loanable Assets Data (USER_DATA)（查询 VIP 借币可借币种数据 (USER_DATA)）

`GET /sapi/v1/loan/vip/loanable/data`

Get interest rate and borrow limit of loanable assets. The borrow limit is shown in USD value.

获取可借币种的利率和借贷限额。借入限额以美元价值显示。

Operation ID: `getLoanableAssetsData`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| loanCoin | query | string |  | 例: `BUSD` |
| vipLevel | query | integer (int64) |  | Defaults to the user's VIP level.<br>默认值：用户的 VIP 等级<br>例: `1` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Loanable Assets Data / 查询可借币种数据

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| rows | object[] |  |  |
| rows[].loanCoin | string |  | 例: `BUSD` |
| rows[]._flexibleDailyInterestRate | string |  | 例: `0.001503` |
| rows[]._flexibleYearlyInterestRate | string |  | 例: `0.548595` |
| rows[]._30dDailyInterestRate | string |  | 例: `0.000136` |
| rows[]._30dYearlyInterestRate | string |  | 例: `0.03450` |
| rows[]._60dDailyInterestRate | string |  | 例: `0.000145` |
| rows[]._60dYearlyInterestRate | string |  | 例: `0.04103` |
| rows[].minLimit | string |  | 例: `100` |
| rows[].maxLimit | string |  | 例: `1000000` |
| rows[].vipLevel | integer (int64) |  | 例: `1` |
| total | integer (int64) |  | 例: `1` |

## Get VIP Loan Interest Rate History (USER_DATA)（查询VIP借币利率历史 (USER_DATA)）

`GET /sapi/v1/loan/vip/interestRateHistory`

Check VIP Loan flexible interest rate history

查询VIP借币活期利率历史记录

Operation ID: `getVIPLoanInterestRateHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| coin | query | string | 是 | 例: `USDT` |
| startTime | query | integer (int64) |  | If both startTime and endTime are omitted, the most recent 90 days are returned.<br>如果 startTime 和 endTime 均未传，默认返回最近 90 天数据。<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | Maximum interval between startTime and endTime is 180 days. Time is based on UTC+0.<br>startTime 与 endTime 最大间隔为 180 天，时间基于 UTC+0。<br>例: `1641782889000` |
| current | query | integer (int64) |  | Current page number, starting from 1.<br>当前查询页，从 1 开始。<br>默认: `1`<br>例: `1` |
| limit | query | integer (int64) |  | Number of records per page.<br>每页返回记录数。<br>默认: `10`<br>例: `10` |
| recvWindow | query | integer (int64) | 是 | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get VIP Loan Interest Rate History / 查询 VIP 借币利率历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| rows | object[] |  |  |
| rows[].coin | string |  | 例: `USDT` |
| rows[].annualizedInterestRate | string |  | 例: `0.0647` |
| rows[].time | integer (int64) |  | 例: `1575018510000` |
| total | integer (int64) |  | 例: `1` |

## Query VIP Loan Fixed Rate Market (USER_DATA)（查询VIP借币固定利率市场 (USER_DATA)）

`GET /sapi/v1/loan/vip/fixed/market`

Query the VIP Loan fixed rate market. Returns a paginated list of fixed-rate supply orders.

查询VIP借币固定利率市场。返回固定利率供给挂单的分页列表。

Operation ID: `queryVIPLoanFixedRateMarket`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| loanCoin | query | string | 是 | Loan coin<br>借贷币种<br>例: `USDT` |
| duration | query | integer (int64) |  | Duration in days, minimum 1<br>期限（天），最小 1<br>例: `30` |
| current | query | integer (int64) |  | Page number, default 1, minimum 1<br>页码，默认 1，最小 1<br>例: `1` |
| size | query | integer (int64) |  | Page size, default 10, range [1, 100]<br>每页条数，默认 10，范围 [1, 100]<br>例: `10` |
| recvWindow | query | integer (int64) |  | The value cannot be greater than `60000`<br>值不能大于 `60000`<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Query VIP Loan Fixed Rate Market / 查询VIP借币固定利率市场

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| total | integer (int64) |  | Total number of records<br>总记录数<br>例: `25` |
| rows | object[] |  | Current page data<br>当前页数据 |
| rows[].requestId | integer (int64) |  | Supply request ID<br>供给方请求ID<br>例: `1234567890` |
| rows[].requestNo | integer (int64) |  | Request number<br>请求编号<br>例: `100001` |
| rows[].coin | string |  | Coin<br>币种<br>例: `USDT` |
| rows[].interestRate | string |  | Annual interest rate<br>年化利率<br>例: `0.05` |
| rows[].duration | integer (int64) |  | Duration in days<br>期限（天）<br>例: `30` |
| rows[].minimumAmount | string |  | Minimum borrow amount<br>最小借贷金额<br>例: `100` |
| rows[].availableAmount | string |  | Maximum available borrow amount<br>最大可借金额<br>例: `1000000` |
| rows[].estimatedInterest | string |  | Estimated interest<br>预估利息<br>例: `4109.59` |

## VIP Loan Borrow (TRADE)（VIP借币借款 (TRADE)）

`POST /sapi/v1/loan/vip/borrow`

VIP loan is available for VIP users only.

VIP 借币仅对 VIP 用户开放。

Operation ID: `vipLoanBorrow`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| loanAccountId | integer (int64) | 是 | 例: `1` |
| loanCoin | string | 是 | 例: `BTC` |
| loanAmount | number (float) | 是 | 例: `1.0` |
| collateralAccountId | string | 是 | Collateral account ID(s). Multiple split by `,`<br>抵押账户 ID，多个用 `,` 分隔<br>例: `12345678,12345678,12345678` |
| collateralCoin | string | 是 | Collateral coin(s), multiple separated by `,`. Use `<ASSET>-Earn` for a Simple Earn Flexible position; it must be sent together with its Spot asset, e.g. `USDT,USDT-Earn`.<br>抵押币种，多个用 `,` 分隔。活期理财持仓使用 `<ASSET>-Earn`，且必须同时传入对应的现货币种，如 `USDT,USDT-Earn`。<br>例: `BUSD,USDT,USDT-Earn,ETH` |
| isFlexibleRate | boolean | 是 | TRUE: flexible rate; FALSE: fixed rate<br>TRUE：浮动利率；FALSE：固定利率<br>默认: `True`<br>例: `True` |
| loanTerm | integer (int64) |  | Mandatory for fixed rate. Optional for flexible rate. e.g. 30/60 days<br>固定利率时必填，浮动利率时可选。例如 30/60 天<br>例: `30` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：VIP Loan Borrow / VIP 借币借款

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| loanAccountId | string |  | Loan receiving account.<br>收款借币账户。<br>例: `12345678` |
| requestId | string |  | 例: `12345678` |
| loanCoin | string |  | 例: `BTC` |
| isFlexibleRate | string |  | 例: `Yes` |
| loanAmount | string |  | 例: `100.55` |
| collateralAccountId | string |  | 例: `12345678,12345678,12345678` |
| collateralCoin | string |  | Includes `<ASSET>-Earn` entries when a Simple Earn Flexible position is pledged.<br>抵押活期理财持仓时，包含 `<ASSET>-Earn`。<br>例: `BUSD,USDT,USDT-Earn,ETH` |
| loanTerm | string |  | 例: `30` |

## VIP Loan Fixed Rate Borrow (TRADE)（VIP借币固定利率借款 (TRADE)）

`POST /sapi/v1/loan/vip/fixed/borrow`

Submit a fixed rate borrow request by matching market supply orders.

匹配市场挂单提交固定利率借贷申请。

Operation ID: `vipLoanFixedRateBorrow`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| supplyRequest | string | 是 | Supply request string, positional encoding (no key). Multiple entries separated by `;`, fields separated by `:`, order: `<requestId>:<interestRate>:<amount>`. Example: `1212:0.12:100;3434:0.13:50`<br>挂单请求字符串，按位置编码（无 key）。多笔用 `;` 分隔，字段用 `:` 分隔，顺序固定：`<requestId>:<interestRate>:<amount>`。示例：`1212:0.12:100;3434:0.13:50`<br>例: `1212:0.12:100;3434:0.13:50` |
| borrowCoin | string | 是 | Borrow coin<br>借贷币种<br>例: `BUSD` |
| loanTerm | integer (int64) | 是 | Loan term in days<br>贷款期限（天）<br>例: `30` |
| borrowUid | integer (int64) | 是 | Borrow receiving account UID<br>借款收款账户 UID<br>例: `12345678` |
| collateralCoin | string | 是 | Collateral coin(s), multiple separated by `,`. Only coin names, no amount (VIP loan collateral amount = entire Spot balance of the coin; for `<ASSET>-Earn`, the Simple Earn Flexible position of the asset). `<ASSET>-Earn` must be sent together with its Spot asset, e.g. `BNB,BNB-Earn`.<br>抵押币种，多个用 `,` 分隔（只携带币种，无 amount；VIP 借币抵押金额 = 该币种的全部现货余额；`<ASSET>-Earn` 则为该币种的活期理财持仓）。`<ASSET>-Earn` 必须同时传入对应的现货币种，如 `BNB,BNB-Earn`。<br>例: `BNB,BNB-Earn,ETH,BTC` |
| collateralAccountId | string | 是 | Collateral account ID(s), multiple separated by `,`<br>抵押账户 ID，多个用 `,` 分隔<br>例: `12345,67890,13579` |
| autoRepay | boolean |  | Default: `true`. `true`: auto repay at expiration; `false`: auto-convert to flexible (floating rate) at expiration<br>默认：`true`。`true`：到期自动还款；`false`：到期自动转为浮动利率<br>默认: `True`<br>例: `True` |
| recvWindow | integer (int64) |  | The value cannot be greater than `60000`<br>值不能大于 `60000`<br>例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：VIP Loan Fixed Rate Borrow / VIP借币固定利率借款

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| borrowCoin | string |  | Echo of input parameter<br>echo 入参<br>例: `BUSD` |
| borrowAmount | string |  | Actual total borrow amount (aggregated when multiple supplyRequest)<br>实际借款总额（多笔 supplyRequest 时为聚合值）<br>例: `100.5` |
| actualReceivedAmount | string |  | Actual received amount<br>实际到账金额<br>例: `98.75` |
| collateralCoin | string |  | Echo of input parameter, comma-separated<br>echo 入参，逗号分隔<br>例: `BNB,BNB-Earn,ETH,BTC` |
| collateralAccountId | string |  | Echo of input parameter, comma-separated<br>echo 入参，逗号分隔<br>例: `12345,67890,13579` |
| borrowInterestRate | string |  | Actual borrow interest rate (weighted average when multiple)<br>实际借款利率（多笔时为加权平均）<br>例: `0.01501231` |
| duration | string |  | `{loanTerm}Days`, e.g. "30Days"<br>`{loanTerm}Days`，如 "30Days"<br>例: `30Days` |
| autoRepay | boolean |  | Echo of input parameter<br>echo 入参<br>例: `True` |
| orderId | integer (int64) |  | Order ID<br>订单 ID<br>例: `123456789` |
| status | string |  | `Succeeds` / `Failed` / `Processing`<br>例: `Succeeds` |

## VIP Loan Renew (TRADE)（VIP借币续期 (TRADE)）

`POST /sapi/v1/loan/vip/renew`

VIP loan is available for VIP users only.

VIP 借币仅对 VIP 用户开放

Operation ID: `vipLoanRenew`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderId | integer (int64) | 是 | 例: `1` |
| loanTerm | integer (int64) | 是 | 30/60 days<br>30/60 天<br>例: `30` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：VIP Loan Renew / VIP 借币续期

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| loanAccountId | string |  | Loan receiving account.<br>收款借币账户。<br>例: `12345678` |
| loanCoin | string |  | 例: `BTC` |
| loanAmount | string |  | 例: `100.55` |
| collateralAccountId | string |  | 例: `12345677,12345678,12345679` |
| collateralCoin | string |  | 例: `BUSD,USDT,ETH` |
| loanTerm | string |  | 例: `30` |

## VIP Loan Repay (TRADE)（VIP借币还款 (TRADE)）

`POST /sapi/v1/loan/vip/repay`

VIP loan is available for VIP users only.

VIP 借币仅对 VIP 用户开放

Operation ID: `vipLoanRepay`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderId | integer (int64) | 是 | 例: `1` |
| amount | number (float) | 是 | 例: `1.0` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：VIP Loan Repay / VIP 借贷 还款

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| loanCoin | string |  | 例: `BUSD` |
| repayAmount | string |  | 例: `200.5` |
| remainingPrincipal | string |  | 例: `100.5` |
| remainingInterest | string |  | 例: `0` |
| collateralCoin | string |  | 例: `BNB,BTC,ETH` |
| currentLTV | string |  | 例: `0.25` |
| repayStatus | string |  | Repayment status (`Repaid`, `Repaying`, `Failed`).<br>还款状态（`Repaid`、`Repaying`、`Failed`）。<br>例: `Repaid` |

## Check VIP Loan Collateral Account (USER_DATA)（查询VIP借币抵押账户 (USER_DATA)）

`GET /sapi/v1/loan/vip/collateral/account`

VIP loan is available for VIP users only

VIP 借币仅对 VIP 用户开放

Operation ID: `checkVIPLoanCollateralAccount`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| orderId | query | integer (int64) |  | 例: `1` |
| collateralAccountId | query | integer (int64) |  | 例: `1` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Check VIP Loan Collateral Account / 查询 VIP 借币抵押账户

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| rows | object[] |  |  |
| rows[].collateralAccountId | string |  | 例: `12345678` |
| rows[].collateralCoin | string |  | 例: `BNB,BTC,ETH` |
| total | integer (int64) |  | 例: `2` |

## Get VIP Loan Accrued Interest (USER_DATA)（查询VIP借币利息记录 (USER_DATA)）

`GET /sapi/v1/loan/vip/accruedInterest`

Check VIP Loan interest record

查询历史累计计息记录

Operation ID: `getVIPLoanAccruedInterest`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| orderId | query | integer (int64) |  | 例: `1` |
| loanCoin | query | string |  | 例: `BTC` |
| startTime | query | integer (int64) |  | If both startTime and endTime are omitted, the most recent 90 days are returned.<br>如果 startTime 和 endTime 均未传，默认返回最近 90 天数据。<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | Maximum interval between startTime and endTime is 90 days.<br>startTime 与 endTime 最大间隔为 90 天。<br>例: `1641782889000` |
| current | query | integer (int64) |  | Current page number, starting from 1.<br>当前查询页，从 1 开始。<br>默认: `1`<br>例: `1` |
| limit | query | integer (int64) |  | Number of records per page.<br>每页返回记录数。<br>默认: `10`<br>例: `10` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get VIP Loan Accrued Interest / 查询 VIP 借币累计利息

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| rows | object[] |  |  |
| rows[].loanCoin | string |  | 例: `USDT` |
| rows[].principalAmount | string |  | 例: `10000` |
| rows[].interestAmount | string |  | 例: `1.2` |
| rows[].annualInterestRate | string |  | 例: `0.001273` |
| rows[].accrualTime | integer (int64) |  | 例: `1575018510000` |
| rows[].orderId | integer (int64) |  | Latest order ID for the renewal order.<br>续期订单对应的最新订单 ID。<br>例: `756783308056935400` |
| total | integer (int64) |  | 例: `1` |

## Get VIP Loan Ongoing Orders (USER_DATA)（查询VIP借币借款中订单 (USER_DATA)）

`GET /sapi/v1/loan/vip/ongoing/orders`

VIP loan is available for VIP users only.

VIP 借币仅对 VIP 用户开放

Operation ID: `getVIPLoanOngoingOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| orderId | query | integer (int64) |  | 例: `1` |
| collateralAccountId | query | integer (int64) |  | 例: `1` |
| loanCoin | query | string |  | 例: `BUSD` |
| collateralCoin | query | string |  | 例: `BNB,BTC,ETH` |
| current | query | integer (int64) |  | 默认: `1`<br>例: `1` |
| limit | query | integer (int64) |  | 默认: `10`<br>例: `10` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get VIP Loan Ongoing Orders / 查询 VIP 借币进行中订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| rows | object[] |  |  |
| rows[].orderId | integer (int64) |  | 例: `100000001` |
| rows[].loanCoin | string |  | 例: `BUSD` |
| rows[].totalDebt | string |  | 例: `10000` |
| rows[].loanRate | string |  | For flexible loans, this is the flexible rate.<br>对于活期借币，该值为活期利率。<br>例: `0.0123` |
| rows[].residualInterest | string |  | 例: `10.27687923` |
| rows[].collateralAccountId | string |  | 例: `12345678,23456789` |
| rows[].collateralCoin | string |  | Includes `<ASSET>-Earn` entries when a Simple Earn Flexible position is pledged.<br>抵押活期理财持仓时，包含 `<ASSET>-Earn`。<br>例: `BNB,BNB-Earn,BTC,ETH` |
| rows[].totalCollateralValueAfterHaircut | string |  | 例: `25000.27565492` |
| rows[].lockedCollateralValue | string |  | 例: `25000.27565492` |
| rows[].currentLTV | string |  | 例: `0.57` |
| rows[].expirationTime | integer (int64) |  | For flexible loans, this value is `0`.<br>对于活期借币，该值为 `0`。<br>例: `1575018510000` |
| rows[].loanDate | string |  | 例: `1676851200000` |
| rows[].loanTerm | string |  | For flexible loans, this value is `open term`.<br>对于活期借币，该值为 `open term`。<br>例: `30days` |
| total | integer (int64) |  | 例: `1` |

## Get VIP Loan Repayment History (USER_DATA)（查询VIP借币还款记录历史 (USER_DATA)）

`GET /sapi/v1/loan/vip/repay/history`

VIP Loans are available only to VIP users.

VIP 借币仅对 VIP 用户开放

Operation ID: `getVIPLoanRepaymentHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| orderId | query | integer (int64) |  | 例: `1` |
| loanCoin | query | string |  | 例: `BUSD` |
| startTime | query | integer (int64) |  | If both startTime and endTime are omitted, the most recent 90 days are returned.<br>如果 startTime 和 endTime 均未传，默认返回最近 90 天数据。<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | Maximum interval between startTime and endTime is 180 days.<br>startTime 与 endTime 最大间隔为 180 天。<br>例: `1641782889000` |
| current | query | integer (int64) |  | Current page number, starting from 1.<br>当前查询页，从 1 开始。<br>默认: `1`<br>例: `1` |
| limit | query | integer (int64) |  | Number of records per page.<br>每页返回记录数。<br>默认: `10`<br>例: `10` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get VIP Loan Repayment History / 查询 VIP 借币还款历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| rows | object[] |  |  |
| rows[].loanCoin | string |  | 例: `BUSD` |
| rows[].repayAmount | string |  | 例: `10000` |
| rows[].repayPrincipal | string |  | 例: `9500` |
| rows[].repayInterest | string |  | 例: `500` |
| rows[].collateralCoin | string |  | 例: `BNB,BTC,ETH` |
| rows[].repayStatus | string |  | Repayment status (`Repaid`, `Repaying`, `Failed`).<br>还款状态（`Repaid`、`Repaying`、`Failed`）。<br>例: `Repaid` |
| rows[].loanDate | string |  | 例: `1676851200000` |
| rows[].repayTime | string |  | 例: `1575018510000` |
| rows[].orderId | string |  | 例: `756783308056935434` |
| total | integer (int64) |  | 例: `1` |

## Query Application Status (USER_DATA)（查询申请状态 (USER_DATA)）

`GET /sapi/v1/loan/vip/request/data`

Query Application Status

查询申请状态

Operation ID: `queryApplicationStatus`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| current | query | integer (int64) |  | Current page number, starting from 1.<br>当前查询页，从 1 开始。<br>默认: `1`<br>例: `1` |
| limit | query | integer (int64) |  | 默认: `10`<br>例: `10` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Application Status / 申请状态

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| rows | object[] |  |  |
| rows[].loanAccountId | string |  | Loan receiving account.<br>收款借币账户。<br>例: `12345678` |
| rows[].orderId | string |  | 例: `12345678` |
| rows[].requestId | string |  | 例: `12345678` |
| rows[].loanCoin | string |  | 例: `BTC` |
| rows[].loanAmount | string |  | 例: `100.55` |
| rows[].collateralAccountId | string |  | 例: `12345678,12345678,12345678` |
| rows[].collateralCoin | string |  | Includes `<ASSET>-Earn` entries when a Simple Earn Flexible position is pledged.<br>抵押活期理财持仓时，包含 `<ASSET>-Earn`。<br>例: `BUSD,USDT,USDT-Earn,ETH` |
| rows[].loanTerm | string |  | 例: `30` |
| rows[].status | string |  | Order status (`Accruing_Interest`, `Overdue`, `Liquidating`, `Repaying`, `Repaid`, `Liquidated`, `Pending`, `Failed`).<br>订单状态（`Accruing_Interest`、`Overdue`、`Liquidating`、`Repaying`、`Repaid`、`Liquidated`、`Pending`、`Failed`）。<br>例: `Repaid` |
| rows[].loanDate | string |  | 例: `1676851200000` |
| total | integer (int64) |  | 例: `1` |