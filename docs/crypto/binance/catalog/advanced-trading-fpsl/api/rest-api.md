---
exchange: binance
source_url: https://developers.binance.com/en/docs/catalog/advanced-trading-fpsl/api/rest-api
api_type: REST
updated_at: 2026-11-22 18:46:17.667208
---

# FPSL REST API

Schema: https://developers.binance.com/en/docs/catalog/advanced-trading-fpsl/api/rest-api/1.0.0/schema.yaml

REST APIs for Binance Fully Paid Securities Lending (FPSL). All endpoints under `/sapi/v1/equity/fpsl/*`.

Binance 全额支付证券出借（FPSL）REST API。所有接口位于 `/sapi/v1/equity/fpsl/*`。

版本: 1.0.0

## 服务地址

- `https://api.binance.com`

## 接口列表

- `GET /sapi/v1/equity/fpsl/disclaimer` — Get FPSL Disclaimer (USER_DATA)
- `POST /sapi/v1/equity/fpsl/enroll` — Submit FPSL Enroll (TRADE)
- `GET /sapi/v1/equity/fpsl/status` — Get FPSL Status (USER_DATA)
- `POST /sapi/v1/equity/fpsl/switch/close` — Cancel FPSL (Switch Close) (TRADE)
- `POST /sapi/v1/equity/fpsl/switch/open` — Reopen FPSL (Switch Open) (TRADE)
- `GET /sapi/v1/equity/fpsl/overview` — Get FPSL Overview (USER_DATA)
- `GET /sapi/v1/equity/fpsl/on-loan` — Get FPSL On-Loan (USER_DATA)
- `GET /sapi/v1/equity/fpsl/symbol/history` — Get FPSL Symbol History (USER_DATA)

## Get FPSL Disclaimer (USER_DATA)（披露与自我认证签署 (Disclaimer) (USER_DATA)）

`GET /sapi/v1/equity/fpsl/disclaimer`

Get the Fully Paid Securities Lending (FPSL) disclaimer, the confirmations and eligibility criteria the user must accept to opt in, and the user's current opt-in status.

查询全额支付证券出借（FPSL）免责声明、用户参与前需确认的条款和资格条件，以及用户当前的参与状态。

权重: 1

Operation ID: `fpslDisclaimer`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| locale | query | string |  | Language of the copy, e.g. `en`, `zh-CN`, `ja`. Default `en` if not sent.<br>文案语言，例如 `en`、`zh-CN`、`ja`；不传时为 `en`。<br>例: `en` |
| recvWindow | query | integer (int64) |  | The value cannot be greater than `60000`.<br>赋值不能大于 `60000`。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Timestamp in milliseconds.<br>时间戳（毫秒）。<br>例: `1770736694138` |

### 响应 200：FPSL Disclaimer / FPSL 免责声明响应

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| isOptedIn | boolean |  | Whether the user has opted in.<br>用户是否已参与。<br>例: `False` |
| title | string |  | Disclaimer title.<br>免责声明标题。<br>例: `Securities Lending Disclaimer` |
| body | string |  | Disclaimer body.<br>免责声明正文。<br>例: `You may choose to opt-in to Securities Lending. If you opt-in, Binance will act as principal lender of your Securities to Alpaca in accordance with clause 10 of the Securities Trading Product Terms. ... In order to proceed to engage in Securities Lending, please confirm the following:` |
| confirmations | object[] |  | Confirmations the user must accept.<br>用户必须确认的条款。 |
| confirmations[].key | string |  | Confirmation key.<br>条款标识。<br>例: `AGREE_CLAUSE_10` |
| confirmations[].required | boolean |  | Whether the confirmation is required.<br>是否必须确认。<br>例: `True` |
| confirmations[].text | string |  | Confirmation text.<br>条款文案。<br>例: `I agree to opt in to Securities Lending and I expressly accept each sub-clause of clause 10 of the Securities Trading Product Terms.` |
| eligibilityPrompt | string |  | Eligibility prompt text.<br>资格条件提示文案。<br>例: `Please also confirm that you fulfill at least one of the following criteria:` |
| eligibilityRule | string |  | Eligibility rule. `AT_LEAST_ONE` means at least one criterion must be met.<br>资格规则。`AT_LEAST_ONE` 表示至少满足一项。<br>例: `AT_LEAST_ONE` |
| eligibilityCriteria | object[] |  | Eligibility criteria.<br>资格条件列表。 |
| eligibilityCriteria[].key | string |  | Criterion key: `BALANCE`, `INCOME`, `LIQUID_ASSETS` or `EXPERIENCE`.<br>条件标识：`BALANCE`、`INCOME`、`LIQUID_ASSETS` 或 `EXPERIENCE`。<br>例: `BALANCE` |
| eligibilityCriteria[].text | string |  | Criterion text.<br>条件文案。<br>例: `My Account Balance (Spot + Funding) is at least US$2,500.` |
| legalLinks | object[] |  | Legal document links.<br>法律文件链接。 |
| legalLinks[].key | string |  | Link key.<br>链接标识。<br>例: `TERMS_OF_USE` |
| legalLinks[].url | string |  | Link URL.<br>链接地址。<br>例: `https://www.binance.com/en/terms` |
| ctaText | string |  | Call-to-action button text.<br>按钮文案。<br>例: `Confirm` |

## Submit FPSL Enroll (TRADE)（提交自我认证 (Enroll) (TRADE)）

`POST /sapi/v1/equity/fpsl/enroll`

Submit the self-certification to enroll in Fully Paid Securities Lending (FPSL).

**Notes:**

- Calling enroll is treated as agreeing to the Disclaimer, equivalent to clicking Confirm in the App.
- At least one of the four declarations must be `true` to meet the eligibility requirement. The criteria are self-certified by the user.
- If none of the four parameters is sent, error `420001` (invalid parameter) is returned. If they are sent but all `false`, the response is HTTP 200 with `enrolled=false`.

提交自我认证，参与全额支付证券出借（FPSL）。

**注意：**

- 调用 enroll 即视为同意 Disclaimer，与 App 点击 Confirm 等价。
- 四项至少一项传 `true` 为满足资格，由用户自证。
- 四项都不传，返回错误码 `420001`（参数错误）；传了但都是 `false` 时返回 HTTP 200，`enrolled=false`。

权重: 1

Operation ID: `fpslEnroll`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| q1BalanceDeclared | query | boolean |  | Declare that the account balance (Spot + Funding) is at least US$2,500.<br>声明账户余额（Spot + Funding）≥ US$2,500。<br>例: `True` |
| q2IncomeDeclared | query | boolean |  | Declare that the annual income is at least US$20,000.<br>声明年收入 ≥ US$20,000。<br>例: `True` |
| q3LiquidAssetsDeclared | query | boolean |  | Declare that liquid assets or net worth is at least US$20,000.<br>声明流动资产或净资产 ≥ US$20,000。<br>例: `False` |
| q4ExperienceDeclared | query | boolean |  | Declare that the user has more than one year of stock investing experience.<br>声明股票投资经验超过 1 年。<br>例: `False` |
| recvWindow | query | integer (int64) |  | The value cannot be greater than `60000`.<br>赋值不能大于 `60000`。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Timestamp in milliseconds.<br>时间戳（毫秒）。<br>例: `1770736694138` |

### 响应 200：FPSL Enroll / FPSL 自我认证响应

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| enrolled | boolean |  | Whether enrollment succeeded. `false` when the eligibility check fails.<br>是否参与成功。资格校验未通过时为 `false`。<br>例: `True` |
| consentedAt | integer (int64) |  | Consent time in milliseconds. Returned on success.<br>同意时间（毫秒）。成功时返回。<br>例: `1789654400000` |
| fpslStatus | string |  | FPSL status. Returned on success.<br>FPSL 状态。成功时返回。<br>例: `ACTIVE` |
| passReasons | string[] |  | Passed criteria. Returned on failure.<br>通过的条件。失败时返回。 |
| failureReasons | string[] |  | Failure reasons. Returned on failure.<br>失败原因。失败时返回。 |
| q1Threshold | string |  | Balance threshold (USD) for q1. Returned on failure.<br>q1 的余额门槛（USD）。失败时返回。<br>例: `2500` |

## Get FPSL Status (USER_DATA)（查询当前状态 (USER_DATA)）

`GET /sapi/v1/equity/fpsl/status`

Get the user's current FPSL status.

**Notes:**

- For a user who has never opted in, the response is empty (no data is returned).
- Switch limits: counted by the number of calls to `/switch/open` and `/switch/close`, which share one quota. `/enroll` is not counted.
- Both limits apply at the same time: at most 3 switches per day (the day rolls over at 00:00 US Eastern time), and at least 5 minutes between two consecutive switches.
- Opening and closing each count as one switch, so opening and then closing counts as 2. The quota is deducted as soon as the request reaches the switch endpoint.

查询用户当前的 FPSL 状态。

**注意：**

- 从未参与过的用户，返回为空（无数据）。
- 开关次数统计：`/switch/open` 与 `/switch/close` 共用一份额度，`/enroll` 不计入。
- 两条限制同时生效：每天最多 3 次，按美东时间 00:00 切日；相邻两次至少间隔 5 分钟。
- 开、关各算一次，先开再关算 2 次。只要请求进入 switch 接口就会扣减额度。

权重: 1

Operation ID: `fpslStatus`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | The value cannot be greater than `60000`.<br>赋值不能大于 `60000`。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Timestamp in milliseconds.<br>时间戳（毫秒）。<br>例: `1770736694138` |

### 响应 200：FPSL Status / FPSL 状态响应

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| fpslStatus | string |  | FPSL status, e.g. `ACTIVE`, `INACTIVE`.<br>FPSL 状态，如 `ACTIVE`、`INACTIVE`。<br>例: `INACTIVE` |
| tierId | string |  | Identifier of the interest-sharing tier on the Alpaca side. It is an identifier only and does not need to be parsed.<br>Alpaca 侧利息分成等级的标识。仅作标识，客户端无需解析。<br>例: `3f8b1d2a-4c5e-6f7a-8b9c-0d1e2f3a4b5c` |
| rateLimit | object |  | Switch rate limit, see the notes above.<br>开关频率限制，规则见上方说明。 |
| rateLimit.dailyRemaining | integer |  | Remaining switches today.<br>今日剩余次数。<br>例: `2` |
| rateLimit.dailyMax | integer |  | Maximum switches per day.<br>每日最大次数。<br>例: `3` |
| rateLimit.cooldownSecondsLeft | integer |  | Remaining cooldown in seconds.<br>剩余冷却时间（秒）。<br>例: `0` |

## Cancel FPSL (Switch Close) (TRADE)（取消 FPSL (Cancel / switch-close) (TRADE)）

`POST /sapi/v1/equity/fpsl/switch/close`

Turn off FPSL. New lending stops after this call.

**Notes:**

- Takes effect immediately: the status is set to `INACTIVE` (PATCH Alpaca) and new lending stops right away. Assets are not frozen.
- Whether and when the portion already lent out is recalled is determined by Alpaca's rules.
- Switch limits: counted by the number of calls to `/switch/open` and `/switch/close`, which share one quota. `/enroll` is not counted.
- Both limits apply at the same time: at most 3 switches per day (the day rolls over at 00:00 US Eastern time), and at least 5 minutes between two consecutive switches.
- Opening and closing each count as one switch, so opening and then closing counts as 2. The quota is deducted as soon as the request reaches the switch endpoint.

关闭 FPSL，调用后将停止新的出借。

**注意：**

- 立即生效：状态置为 `INACTIVE`（PATCH Alpaca），立即停止新的出借，资产不会被冻结。
- 已借出的部分是否收回及何时收回，由 Alpaca 侧规则决定。
- 开关次数统计：`/switch/open` 与 `/switch/close` 共用一份额度，`/enroll` 不计入。
- 两条限制同时生效：每天最多 3 次，按美东时间 00:00 切日；相邻两次至少间隔 5 分钟。
- 开、关各算一次，先开再关算 2 次。只要请求进入 switch 接口就会扣减额度。

权重: 1

Operation ID: `fpslCancel`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | The value cannot be greater than `60000`.<br>赋值不能大于 `60000`。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Timestamp in milliseconds.<br>时间戳（毫秒）。<br>例: `1770736694138` |

### 响应 200：Cancel FPSL / 取消 FPSL 响应

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| fpslStatus | string |  | FPSL status after the call.<br>调用后的 FPSL 状态。<br>例: `INACTIVE` |
| changedAt | integer (int64) |  | Status change time in milliseconds.<br>状态变更时间（毫秒）。<br>例: `1789654400000` |

## Reopen FPSL (Switch Open) (TRADE)（重新开启 (switch-open) (TRADE)）

`POST /sapi/v1/equity/fpsl/switch/open`

Turn FPSL back on.

**Notes:**

- Switch limits: counted by the number of calls to `/switch/open` and `/switch/close`, which share one quota. `/enroll` is not counted.
- Both limits apply at the same time: at most 3 switches per day (the day rolls over at 00:00 US Eastern time), and at least 5 minutes between two consecutive switches.
- Opening and closing each count as one switch, so opening and then closing counts as 2. The quota is deducted as soon as the request reaches the switch endpoint.

重新开启 FPSL。

**注意：**

- 开关次数统计：`/switch/open` 与 `/switch/close` 共用一份额度，`/enroll` 不计入。
- 两条限制同时生效：每天最多 3 次，按美东时间 00:00 切日；相邻两次至少间隔 5 分钟。
- 开、关各算一次，先开再关算 2 次。只要请求进入 switch 接口就会扣减额度。

权重: 1

Operation ID: `fpslReopen`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | The value cannot be greater than `60000`.<br>赋值不能大于 `60000`。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Timestamp in milliseconds.<br>时间戳（毫秒）。<br>例: `1770736694138` |

### 响应 200：Reopen FPSL / 重新开启 FPSL 响应

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| fpslStatus | string |  | FPSL status after the call.<br>调用后的 FPSL 状态。<br>例: `ACTIVE` |
| changedAt | integer (int64) |  | Status change time in milliseconds.<br>状态变更时间（毫秒）。<br>例: `1789654400000` |

## Get FPSL Overview (USER_DATA)（借贷概览 (Overview) (USER_DATA)）

`GET /sapi/v1/equity/fpsl/overview`

Get an overview of the user's securities lending.

**Notes:**

- If nothing has been settled yet, `totalInterest` is `"0"` and `lastExecutedAt` is not returned.
- The data is a T-1 snapshot.

查询用户的证券借贷概览。

**注意：**

- 从未结算：`totalInterest` 为 `"0"`，`lastExecutedAt` 不返回。
- 数据为 T-1 快照。

权重: 1

Operation ID: `fpslOverview`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | The value cannot be greater than `60000`.<br>赋值不能大于 `60000`。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Timestamp in milliseconds.<br>时间戳（毫秒）。<br>例: `1770736694138` |

### 响应 200：FPSL Overview / FPSL 借贷概览响应

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| stocksOnLoan | integer |  | Number of distinct stocks currently on loan, e.g. lending AAPL and TSLA gives 2. This is not a share quantity.<br>当前在贷的不同股票的数量，例如借出 AAPL 和 TSLA 则为 2。不是股数。<br>例: `3` |
| totalInterest | string |  | Total interest earned.<br>累计利息。<br>例: `12.345678` |
| lastExecutedAt | integer (int64) |  | Last execution time in milliseconds. Not returned if nothing has been settled.<br>最近一次执行时间（毫秒）。从未结算时不返回。<br>例: `1789654400000` |
| currency | string |  | Interest currency.<br>利息币种。<br>例: `USDC` |

## Get FPSL On-Loan (USER_DATA)（在贷列表 (On-Loan) (USER_DATA)）

`GET /sapi/v1/equity/fpsl/on-loan`

Get the list of the user's stocks on loan, grouped by day.

**Notes:**

- `days` is sorted by date in descending order and only includes dates with loan records. The data is up to T-1 in US Eastern time.
- When the query range includes the current US Eastern date, `today` is returned, indicating that the data for the current day will be available the next day. Otherwise this field is not returned.
- Assets are identified by the Equity `assetCode` (e.g. `EQ_AAPL`).

查询用户的在贷股票列表，按日期分组。

**注意：**

- `days` 按日期倒序排列，只包含有借出记录的日期，数据截止到美东 T-1。
- 查询范围包含美东当天时返回 `today`，表示当天数据预计次日可查；否则不返回该字段。
- 资产标识使用 equity 的 `assetCode`（如 `EQ_AAPL`）。

权重: 1

Operation ID: `fpslOnLoan`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| startDate | query | string | 是 | Start date (inclusive), format `YYYY-MM-DD`, a date in US Eastern time (America/New_York).<br>开始日期（含），格式 `YYYY-MM-DD`，美东（America/New_York）日期。<br>例: `2026-10-01` |
| endDate | query | string | 是 | End date (inclusive), same format as above. The span is at most 60 days by default.<br>结束日期（含），格式同上；跨度默认最多 60 天。<br>例: `2026-10-20` |
| recvWindow | query | integer (int64) |  | The value cannot be greater than `60000`.<br>赋值不能大于 `60000`。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Timestamp in milliseconds.<br>时间戳（毫秒）。<br>例: `1770736694138` |

### 响应 200：FPSL On-Loan / FPSL 在贷列表响应

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| startDate | string |  | Start date of the query, as requested.<br>查询的开始日期，与请求一致。<br>例: `2026-10-01` |
| endDate | string |  | End date of the query, as requested.<br>查询的结束日期，与请求一致。<br>例: `2026-10-20` |
| days | object[] |  | Loan records grouped by day, in descending date order.<br>按日期分组的借出记录，日期倒序。 |
| days[].date | string |  | Date in US Eastern time.<br>美东日期。<br>例: `2026-10-19` |
| days[].items | object[] |  | Assets on loan on this date.<br>当日在贷资产。 |
| days[].items[].assetCode | string |  | Equity asset code.<br>Equity 资产代码。<br>例: `EQ_AAPL` |
| days[].items[].quantity | string |  | Quantity on loan.<br>在贷数量。<br>例: `541.1234567890` |
| today | object |  | Returned only when the query range includes the current US Eastern date.<br>仅当查询范围包含美东当天时返回。 |
| today.nyTodayDate | string |  | Current US Eastern date.<br>美东当天日期。<br>例: `2026-10-20` |
| today.nyTomorrowDate | string |  | Next US Eastern date, when today's data becomes available.<br>美东次日日期，当天数据预计此日可查。<br>例: `2026-10-21` |

## Get FPSL Symbol History (USER_DATA)（单资产历史借贷 (Symbol History) (USER_DATA)）

`GET /sapi/v1/equity/fpsl/symbol/history`

Get the loan history of a single asset.

查询单个资产的历史借贷记录。

权重: 1

Operation ID: `fpslSymbolHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| assetCode | query | string | 是 | e.g. `EQ_AAPL`. Length must not exceed 64.<br>如 `EQ_AAPL`，长度 ≤ 64。<br>例: `EQ_AAPL` |
| page | query | integer |  | Page number, starting from 1. Default `1`.<br>页码，从 1 开始，默认 `1`。<br>默认: `1`<br>例: `1` |
| size | query | integer |  | Number of records per page. Default `20`, range `1`-`100`.<br>每页条数，默认 `20`，取值 `1`-`100`。<br>默认: `20`<br>例: `20` |
| recvWindow | query | integer (int64) |  | The value cannot be greater than `60000`.<br>赋值不能大于 `60000`。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Timestamp in milliseconds.<br>时间戳（毫秒）。<br>例: `1770736694138` |

### 响应 200：FPSL Symbol History / FPSL 单资产历史借贷响应

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| assetCode | string |  | Equity asset code.<br>Equity 资产代码。<br>例: `EQ_AAPL` |
| items | object[] |  | Loan records.<br>借贷记录。 |
| items[].date | integer (int64) |  | Record date, as the Unix timestamp in milliseconds of 00:00 US Eastern time (America/New_York) on that date.<br>记录日期，为该日美东（America/New_York）00:00 对应的 Unix 毫秒时间戳。<br>例: `1792382400000` |
| items[].quantity | string |  | Quantity on loan.<br>在贷数量。<br>例: `541.1234567890` |
| total | integer |  | Total number of records.<br>记录总数。<br>例: `30` |
| page | integer |  | Current page.<br>当前页码。<br>例: `1` |
| size | integer |  | Page size.<br>每页条数。<br>例: `20` |