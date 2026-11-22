---
exchange: binance
source_url: https://developers.binance.com/en/docs/catalog/vip-and-institutional-fund-account/api/rest-api
api_type: REST
updated_at: 2026-11-22 18:46:18.973588
---

# Fund Account REST API

Schema: https://developers.binance.com/en/docs/catalog/vip-and-institutional-fund-account/api/rest-api/1.0.0/schema.yaml

Query account information and manage Binance Fund Account operations.

查询账户信息并管理 Binance 资金账户操作。

版本: 1.0.0

## 服务地址

- `https://api.binance.com`
- `https://api-gcp.binance.com`
- `https://api1.binance.com`
- `https://api2.binance.com`
- `https://api3.binance.com`
- `https://api4.binance.com`

## 接口列表

- `GET /sapi/v1/vip/fund-info/fund-info-basic-info` — Query Portfolio Info for Portfolio Manager
- `GET /sapi/v1/vip/fund-info/fund-nav-info` — Query Portfolio NAV History
- `GET /sapi/v1/vip/fund-info/fund-investor-his-info` — Query Investor Operation History
- `GET /sapi/v1/capital-connect/redemption/calendar` — Redemption Calendar
- `GET /sapi/v2/portfolio-account/trading-team/portfolio-basic-info` — Query Portfolio Basic Info for Trading Team V2
- `GET /sapi/v2/portfolio-account/trading-team/portfolio-nav-info` — Query Portfolio NAV History for Trading Team V2
- `GET /sapi/v2/portfolio-account/trading-team/investor-portfolio-his-info` — Query Investor Operation History for Trading Team V2
- `GET /sapi/v1/portfolio-account/investor/portfolio-nav-info` — Query Portfolio NAV History for Investor
- `GET /sapi/v2/capital-connect/trading-team/redemption/calendar` — Redemption Calendar V2

## Query Portfolio Info for Portfolio Manager（查询投资组合基本信息（适用于资金管理者））

`GET /sapi/v1/vip/fund-info/fund-info-basic-info`

Query basic info for one or all portfolios managed by the IM.

查询 IM 管理的单个或全部投资组合的基本信息。

Operation ID: `queryFundInfoForFundManager`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |
| portfolioId | query | string |  | CC portfolio ID. Omit to list all portfolios.<br>CC portfolio ID，省略则返回所有投资组合。<br>例: `CC00876646` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Portfolio Info for Portfolio Manager / 投资组合基本信息（适用于资金管理者）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].portfolioId | string |  | CC portfolio ID<br>例: `CC00876646` |
| [].fundid | integer (int64) |  | Internal fund ID<br>内部基金 ID<br>例: `38` |
| [].fundName | string |  | Portfolio name<br>投资组合名称<br>例: `Apolloplan Alpha Investment Fund` |
| [].fundCurrency | string |  | Portfolio currency<br>投资组合币种<br>例: `USDT` |
| [].totalUnits | string |  | Total outstanding units<br>总发行份额<br>例: `836557.27100000` |
| [].estNavPerUnit | string |  | Estimated NAV per unit<br>预估每份净值<br>例: `1.05230000` |
| [].investorInfos | object[] |  | Investor holdings list<br>投资者持仓列表 |
| [].investorInfos[].investorAccountId | integer (int64) |  | Investor sub-account ID<br>投资者子账户 ID<br>例: `1140211237` |
| [].investorInfos[].investorUnit | string |  | Investor's units<br>投资者持有份额<br>例: `100000.00000000` |
| [].subAccInfo | object[] |  | Sub-account balances<br>子账户余额 |
| [].subAccInfo[].accountId | integer (int64) |  | Sub-account ID<br>子账户 ID<br>例: `1140211237` |
| [].subAccInfo[].accountBalance | string |  | Sub-account balance<br>子账户余额<br>例: `880123.45000000` |

## Query Portfolio NAV History（查询投资组合净值历史）

`GET /sapi/v1/vip/fund-info/fund-nav-info`

Query NAV history (last 30 days) for a specific portfolio.

查询指定投资组合最近 30 天的净资产价值（NAV）历史记录。

Operation ID: `queryFundNavHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |
| portfolioId | query | string | 是 | CC portfolio ID<br>例: `CC00876646` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Portfolio NAV History / 投资组合净值历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].portfolioId | string |  | CC portfolio ID<br>例: `CC00876646` |
| [].fundName | string |  | Portfolio name<br>投资组合名称<br>例: `Apolloplan Alpha Investment Fund` |
| [].fundNavs | object[] |  | Daily NAV entries<br>每日 NAV 条目 |
| [].fundNavs[].date | string |  | Date (YYYYMMDD)<br>日期 (YYYYMMDD)<br>例: `20260327` |
| [].fundNavs[].nav | string |  | Total NAV<br>总净值<br>例: `880123.45000000` |
| [].fundNavs[].unit | string |  | Total units<br>总份额<br>例: `836557.27100000` |
| [].fundNavs[].navPerUnit | string |  | NAV per unit<br>每份净值<br>例: `1.05230000` |

## Query Investor Operation History（查询投资人操作历史（适用于资金管理者））

`GET /sapi/v1/vip/fund-info/fund-investor-his-info`

Query completed subscription and redemption history for a specific investor in a specific portfolio.

查询指定投资者在投资组合下的申购赎回记录

Operation ID: `queryInvestorOperationHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |
| portfolioId | query | string | 是 | CC portfolio ID<br>例: `CC00876646` |
| investorCcId | query | integer (int64) | 是 | Investor's CC ID (6-digit)<br>投资者 CC ID（6 位）<br>例: `876646` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Investor Operation History / 投资者操作历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| portfolioId | string |  | CC portfolio ID<br>例: `CC00876646` |
| fundName | string |  | Portfolio name<br>投资组合名称<br>例: `Apolloplan Alpha Investment Fund` |
| investorSubscriptions | object[] |  | Completed subscriptions<br>已完成的申购记录 |
| investorSubscriptions[].date | integer (int64) |  | Subscription date (timestamp)<br>申购日期（时间戳）<br>例: `1711584000000` |
| investorSubscriptions[].subscriptionAmt | string |  | Amount subscribed<br>申购金额<br>例: `100000.00000000` |
| investorSubscriptions[].status | string |  | Request status: DONE<br>请求状态：DONE<br>例: `DONE` |
| investorSubscriptions[].result | string |  | Transfer result: SUCCESS / FAILED<br>划转结果：SUCCESS / FAILED<br>例: `SUCCESS` |
| investorRedemptions | object[] |  | Completed redemptions<br>已完成的赎回记录 |
| investorRedemptions[].date | integer (int64) |  | Redemption date (timestamp)<br>赎回日期（时间戳）<br>例: `1711670400000` |
| investorRedemptions[].redemptionUnits | string |  | Units redeemed<br>赎回份额<br>例: `50000.00000000` |
| investorRedemptions[].redemptionAmt | string |  | Amount redeemed<br>赎回金额<br>例: `52615.00000000` |
| investorRedemptions[].status | string |  | Request status: DONE<br>请求状态：DONE<br>例: `DONE` |
| investorRedemptions[].result | string |  | Transfer result: SUCCESS / FAILED<br>划转结果：SUCCESS / FAILED<br>例: `SUCCESS` |

## Redemption Calendar（赎回日历）

`GET /sapi/v1/capital-connect/redemption/calendar`

Query upcoming redemption forecast for the next 8 days across all portfolios managed by the IM.

查询 IM 管理的所有投资组合未来 8 天的赎回预测。

Operation ID: `redemptionCalendar`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Redemption Calendar / 赎回日历

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| items | object[] |  | Per-portfolio daily forecast entries<br>按投资组合和日期的预测条目 |
| items[].portfolioId | string |  | CC portfolio ID<br>例: `CC00123456` |
| items[].portfolioName | string |  | Portfolio name<br>投资组合名称<br>例: `Alpha Strategy Fund` |
| items[].currency | string |  | Portfolio currency<br>投资组合币种<br>例: `USDT` |
| items[].forecastDate | integer (int64) |  | Forecast date as Unix timestamp (ms)<br>预测日期，Unix 时间戳（毫秒）<br>例: `1711584000000` |
| items[].units | string |  | Total units pending redemption<br>待赎回总份额<br>例: `1000.00000000` |
| items[].navPerUnit | string |  | NAV per unit (T-1). null if not available<br>每份净值（T-1），不可用时为 null<br>例: `1.05230000` |
| items[].estimatedAmount | string |  | units x navPerUnit. null if NAV not available<br>units × navPerUnit，NAV 不可用时为 null<br>例: `1052.30000000` |

## Query Portfolio Basic Info for Trading Team V2（查询投资组合基本信息（适用于交易团队）V2）

`GET /sapi/v2/portfolio-account/trading-team/portfolio-basic-info`

Query basic info for one or all portfolios managed by the trading team. This is the v2 replacement for Query Fund Info for Fund Manager (/sapi/v1/vip/fund-info/fund-info-basic-info).

查询交易团队管理的单个或全部投资组合的基本信息。本接口为查询资金账户信息（适用于资金管理者）（/sapi/v1/vip/fund-info/fund-info-basic-info）的 v2 替代接口。

Operation ID: `queryPortfolioBasicInfoForTradingTeamV2`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| portfolioAccountId | query | integer (int64) |  | Portfolio account ID. Omit to list all portfolios managed by this trading team.<br>投资组合所属账户 ID，省略则返回该交易团队管理的所有投资组合。<br>例: `1000299351640` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Portfolio Basic Info for Trading Team / 交易团队投资组合基本信息

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].portfolioId | string |  | CC portfolio ID<br>例: `CC00556589` |
| [].portfolioAccountId | integer (int64) |  | Portfolio account ID<br>投资组合所属账户 ID<br>例: `1000299351640` |
| [].portfolioName | string |  | Portfolio name<br>投资组合名称<br>例: `Fund USDT e3aa8545` |
| [].portfolioCurrency | string |  | Portfolio currency<br>投资组合币种<br>例: `USDT` |
| [].totalAllocation | string |  | Total outstanding allocation<br>总份额<br>例: `21718.95220000` |
| [].estNavPerAllocation | string |  | Estimated NAV per allocation<br>预估每份净值<br>例: `0.01968874` |
| [].investorInfos | object[] |  | Investor holdings list<br>投资人持仓列表 |
| [].investorInfos[].investorId | integer (int64) |  | Investor ID (6-digit CC investor ID; falls back to real UID when no CC ID mapping exists, e.g. the trading team's own self-investment)<br>投资人 ID（6 位 CC 投资人 ID；若无 ccId 映射（如交易团队自投资）则回退为真实 UID）<br>例: `821792` |
| [].investorInfos[].investorAllocation | string |  | Investor's allocation<br>投资人份额<br>例: `20761.88930000` |
| [].subAccountInfos | object[] |  | Sub-account balances<br>子账户余额列表 |
| [].subAccountInfos[].subAccountId | integer (int64) |  | Sub-account ID<br>子账户 ID<br>例: `1000299351640` |
| [].subAccountInfos[].subAccountBalance | string |  | Sub-account balance<br>子账户余额<br>例: `427.56083463` |

## Query Portfolio NAV History for Trading Team V2（查询投资组合净值历史（适用于交易团队）V2）

`GET /sapi/v2/portfolio-account/trading-team/portfolio-nav-info`

Query NAV history (last 30 days) for a specific portfolio. This is the v2 replacement for Query Fund NAV History (/sapi/v1/vip/fund-info/fund-nav-info). Unlike v1, which returned a top-level array, this endpoint returns a single object.

查询指定投资组合最近 30 天的净资产价值（NAV）历史记录。本接口为查询投资组合净值历史（/sapi/v1/vip/fund-info/fund-nav-info）的 v2 替代接口。与 v1 接口（返回顶层数组）不同，本接口返回单个对象。

Operation ID: `queryPortfolioNavHistoryForTradingTeamV2`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| portfolioAccountId | query | integer (int64) | 是 | Portfolio account ID<br>投资组合所属账户 ID<br>例: `1000299351640` |
| beginNavDay | query | string |  | yyyyMMdd<br>例: `20260601` |
| endNavDay | query | string |  | yyyyMMdd<br>例: `20260625` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Portfolio NAV History for Trading Team / 交易团队投资组合净值历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| portfolioId | string |  | CC portfolio ID<br>例: `CC00556589` |
| portfolioAccountId | integer (int64) |  | Portfolio account ID<br>投资组合所属账户 ID<br>例: `1000299351640` |
| portfolioName | string |  | Portfolio name<br>投资组合名称<br>例: `Fund USDT e3aa8545` |
| portfolioNavs | object[] |  | Daily NAV entries<br>每日 NAV 条目 |
| portfolioNavs[].date | string |  | Date (YYYYMMDD)<br>日期 (YYYYMMDD)<br>例: `20260625` |
| portfolioNavs[].nav | string |  | Total NAV<br>总净值<br>例: `427.56083463` |
| portfolioNavs[].allocation | string |  | Total allocation<br>总份额<br>例: `19.52412599` |
| portfolioNavs[].navPerAllocation | string |  | NAV per allocation<br>每份净值<br>例: `21.89910242` |

## Query Investor Operation History for Trading Team V2（查询投资人操作历史（适用于交易团队）V2）

`GET /sapi/v2/portfolio-account/trading-team/investor-portfolio-his-info`

Query completed subscription and redemption history for a specific investor in a specific portfolio. This is the v2 replacement for Query Investor Operation History (/sapi/v1/vip/fund-info/fund-investor-his-info).

查询指定投资者在投资组合下的申购赎回记录。本接口为查询投资人操作历史（适用于资金管理者）（/sapi/v1/vip/fund-info/fund-investor-his-info）的 v2 替代接口。

Operation ID: `queryInvestorOperationHistoryForTradingTeamV2`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| portfolioAccountId | query | integer (int64) | 是 | Portfolio account ID<br>投资组合所属账户 ID<br>例: `1000299351640` |
| investorId | query | integer (int64) | 是 | Investor ID (6-digit CC ID)<br>投资人 ID（6 位 CC ID）<br>例: `821792` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Investor Operation History for Trading Team / 交易团队投资人操作历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| portfolioId | string |  | CC portfolio ID<br>例: `CC00556589` |
| portfolioAccountId | integer (int64) |  | Portfolio account ID<br>投资组合所属账户 ID<br>例: `1000299351640` |
| portfolioName | string |  | Portfolio name<br>投资组合名称<br>例: `Fund USDT e3aa8545` |
| investorSubscriptions | object[] |  | Completed subscriptions<br>已完成的申购记录 |
| investorSubscriptions[].date | integer (int64) |  | Subscription date (timestamp)<br>申购日期（时间戳）<br>例: `1749636000000` |
| investorSubscriptions[].subscriptionAmt | string |  | Amount subscribed<br>申购金额<br>例: `3000.00000000` |
| investorSubscriptions[].status | string |  | Request status: DONE<br>请求状态：DONE<br>例: `DONE` |
| investorSubscriptions[].result | string |  | Transfer result: SUCCESS / FAILED<br>划转结果：SUCCESS / FAILED<br>例: `SUCCESS` |
| investorRedemptions | object[] |  | Completed redemptions<br>已完成的赎回记录 |
| investorRedemptions[].date | integer (int64) |  | Redemption date (timestamp)<br>赎回日期（时间戳）<br>例: `1749722400000` |
| investorRedemptions[].redemptionAllocation | string |  | Allocation redeemed<br>赎回份额<br>例: `50000.00000000` |
| investorRedemptions[].redemptionAmt | string |  | Amount redeemed<br>赎回金额<br>例: `52615.00000000` |
| investorRedemptions[].status | string |  | Request status: DONE<br>请求状态：DONE<br>例: `DONE` |
| investorRedemptions[].result | string |  | Transfer result: SUCCESS / FAILED<br>划转结果：SUCCESS / FAILED<br>例: `SUCCESS` |

## Query Portfolio NAV History for Investor（查询投资组合净值历史（适用于投资人））

`GET /sapi/v1/portfolio-account/investor/portfolio-nav-info`

Query NAV history for a portfolio, from the investor's own perspective. Only the date and NAV per allocation are returned - the caller's own allocation and the portfolio's total NAV are not exposed. This is a new, standalone endpoint (no v1 counterpart).

从投资人视角查询投资组合的净值历史，仅返回日期与每份净值，不暴露投资人自身份额及投资组合总净值。本接口为全新接口，无 v1 对应版本。

Operation ID: `queryPortfolioNavHistoryForInvestor`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| portfolioId | query | string | 是 | CC portfolio ID<br>例: `CC00556589` |
| beginNavDay | query | string |  | yyyyMMdd<br>例: `20260601` |
| endNavDay | query | string |  | yyyyMMdd<br>例: `20260625` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Portfolio NAV History for Investor / 投资人投资组合净值历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| portfolioId | string |  | CC portfolio ID<br>例: `CC00556589` |
| portfolioName | string |  | Portfolio name<br>投资组合名称<br>例: `Fund USDT e3aa8545` |
| portfolioNavs | object[] |  | Daily NAV entries<br>每日 NAV 条目 |
| portfolioNavs[].date | string |  | Date (YYYYMMDD)<br>日期 (YYYYMMDD)<br>例: `20260625` |
| portfolioNavs[].navPerAllocation | string |  | NAV per allocation<br>每份净值<br>例: `0.14449552` |

## Redemption Calendar V2（赎回日历V2）

`GET /sapi/v2/capital-connect/trading-team/redemption/calendar`

Query upcoming redemption forecast, grouped by date, across all portfolios managed by the trading team. This is the v2 replacement for Redemption Calendar (/sapi/v1/capital-connect/redemption/calendar).

按日期分组查询交易团队管理的所有投资组合的未来赎回预测。本接口为赎回日历（/sapi/v1/capital-connect/redemption/calendar）的 v2 替代接口。

Operation ID: `redemptionCalendarV2`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Redemption Calendar V2 / 赎回日历V2

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| items | object[] |  | Per-date redemption forecast entries<br>按日期分组的赎回预测条目 |
| items[].date | string |  | Redemption date (ISO-8601)<br>赎回日期（ISO-8601）<br>例: `2026-06-26T00:00:00.000+00:00` |
| items[].redemptions | object[] |  | Per-portfolio redemption entries for this date<br>当日各投资组合的赎回条目 |
| items[].redemptions[].portfolioId | string |  | CC portfolio ID<br>例: `CC00556589` |
| items[].redemptions[].portfolioName | string |  | Portfolio name<br>投资组合名称<br>例: `Fund USDT e3aa8545` |
| items[].redemptions[].currency | string |  | Portfolio currency<br>投资组合币种<br>例: `USDT` |
| items[].redemptions[].allocations | string |  | Total allocations pending redemption<br>待赎回总份额<br>例: `3410.98700000` |
| items[].redemptions[].navPerAllocation | string |  | NAV per allocation (T-1)<br>每份净值（T-1）<br>例: `1.08340000` |
| items[].redemptions[].estimatedAmount | string |  | allocations x navPerAllocation<br>allocations × navPerAllocation<br>例: `3695.34580000` |
| items[].currencyTotals | object[] |  | Totals grouped by currency for this date<br>当日按币种汇总 |
| items[].currencyTotals[].currency | string |  | Currency<br>币种<br>例: `USDT` |
| items[].currencyTotals[].totalAmount | string |  | Sum of estimatedAmount across portfolios in this currency<br>该币种下 estimatedAmount 汇总<br>例: `3695.34580000` |