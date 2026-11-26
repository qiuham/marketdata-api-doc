---
exchange: binance
source_url: https://developers.binance.com/en/docs/catalog/vip-and-institutional-portfolio-account/api/rest-api
api_type: REST
updated_at: 2026-11-26 18:50:03.561893
---

# Portfolio Account REST API

Schema: https://developers.binance.com/en/docs/catalog/vip-and-institutional-portfolio-account/api/rest-api/1.0.0/schema.yaml

Query account information and manage Binance Portfolio Account operations.

查询账户信息并管理 Binance 投资组合账户操作。

版本: 1.0.0

## 服务地址

- `https://api.binance.com`
- `https://api-gcp.binance.com`
- `https://api1.binance.com`
- `https://api2.binance.com`
- `https://api3.binance.com`
- `https://api4.binance.com`

## 接口列表

- `GET /sapi/v2/portfolio-account/trading-team/portfolio-basic-info` — Query Portfolio Basic Info for Trading Team V2
- `GET /sapi/v2/portfolio-account/trading-team/portfolio-nav-info` — Query Portfolio NAV History for Trading Team V2
- `GET /sapi/v2/portfolio-account/trading-team/investor-portfolio-his-info` — Query Investor Operation History for Trading Team V2
- `GET /sapi/v2/capital-connect/trading-team/redemption/calendar` — Redemption Calendar for Trading Team V2
- `POST /sapi/v2/portfolio-account/trading-team/change-api-sharing-switch` — Change API Sharing Switch
- `GET /sapi/v2/portfolio-account/trading-team/api-sharing-status` — Query API Sharing Status
- `GET /sapi/v1/portfolio-account/investor/portfolio-nav-info` — Query Portfolio NAV History for Investor
- `GET /sapi/v1/portfolio-account/investor/portfolio-history-info` — Query Investor Portfolio History Info
- `GET /sapi/v1/portfolio-account/investor/portfolio-realtime-asset-value` — Query Investor Portfolio Realtime Asset Value

## Query Portfolio Basic Info for Trading Team V2（查询投资组合基本信息（适用于交易团队）V2）

`GET /sapi/v2/portfolio-account/trading-team/portfolio-basic-info`

Query basic info for one or all portfolios managed by the trading team.

查询交易团队管理的单个或全部投资组合的基本信息。

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

Query NAV history (last 30 days) for a specific portfolio.

查询指定投资组合最近 30 天的净资产价值（NAV）历史记录。

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

Query completed subscription and redemption history for a specific investor in a specific portfolio.

查询指定投资者在投资组合下的申购赎回记录。

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

## Redemption Calendar for Trading Team V2（赎回日历（适用于交易团队）V2）

`GET /sapi/v2/capital-connect/trading-team/redemption/calendar`

Query upcoming redemption forecast, grouped by date, across all portfolios managed by the trading team.

按日期分组查询交易团队管理的所有投资组合的未来赎回预测。

Operation ID: `redemptionCalendarV2`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Redemption Calendar for Trading Team / 赎回日历（适用于交易团队）

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

## Change API Sharing Switch（修改 API 数据共享开关）

`POST /sapi/v2/portfolio-account/trading-team/change-api-sharing-switch`

Enable or disable investor access to portfolio-level data through the API. Requires a key on the Manager Parent Account (trading team administrator).

开启或关闭投资人通过 API 查询投资组合层面数据的权限。需使用管理人母账户（交易团队管理员）的 API Key。

Operation ID: `changeApiSharingSwitch`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| portfolioAccountId | query | string | 是 | Portfolio Account ID<br>投资组合账户 ID<br>例: `CC00556589` |
| enabled | query | boolean | 是 | true to enable investor API data sharing, false to disable<br>true 表示开启投资人 API 数据共享，false 表示关闭<br>例: `True` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：API sharing switch changed / API 数据共享开关已修改

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| portfolioAccountId | string |  | Portfolio Account ID<br>投资组合账户 ID<br>例: `CC00556589` |
| apiSharingEnabled | boolean |  | Resulting state after the change<br>修改后的开关状态<br>例: `True` |
| updatedAt | string |  | Time the change took effect, UTC, ISO 8601<br>修改生效时间，UTC，ISO 8601<br>例: `2026-10-30T05:25:30Z` |

## Query API Sharing Status（查询 API 数据共享状态）

`GET /sapi/v2/portfolio-account/trading-team/api-sharing-status`

Return the current investor API data-sharing setting for a portfolio. Requires a key on the Manager Parent Account.

查询投资组合当前的投资人 API 数据共享设置。需使用管理人母账户的 API Key。

Operation ID: `queryApiSharingStatus`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| portfolioAccountId | query | string | 是 | Portfolio Account ID<br>投资组合账户 ID<br>例: `CC00556589` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Current API sharing status / 当前 API 数据共享状态

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| portfolioAccountId | string |  | Portfolio Account ID<br>投资组合账户 ID<br>例: `CC00556589` |
| apiSharingEnabled | boolean |  | Whether investor API data sharing is enabled<br>是否开启投资人 API 数据共享<br>例: `True` |
| updatedAt | string |  | Time of the last change, UTC, ISO 8601<br>最近一次修改时间，UTC，ISO 8601<br>例: `2026-10-30T05:25:30Z` |

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

## Query Investor Portfolio History Info（查询投资组合操作历史（适用于投资人））

`GET /sapi/v1/portfolio-account/investor/portfolio-history-info`

Return the calling investor's own subscription and redemption records for a portfolio. Requires a key on the investor's own account.

查询调用投资人自己在某个投资组合中的申购和赎回记录。需使用投资人自己账户的 API Key。

Operation ID: `queryInvestorPortfolioHistoryInfo`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| portfolioId | query | string | 是 | Portfolio ID<br>投资组合 ID<br>例: `CC00556589` |
| beginDay | query | string |  | Start date, yyyyMMdd. Defaults to the last 90 days<br>开始日期，yyyyMMdd。默认为最近 90 天<br>例: `20260601` |
| endDay | query | string |  | End date, yyyyMMdd<br>结束日期，yyyyMMdd<br>例: `20260625` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Investor subscription and redemption history / 投资人申购和赎回历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| portfolioId | string |  | Portfolio ID<br>投资组合 ID<br>例: `CC00556589` |
| portfolioName | string |  | Portfolio name<br>投资组合名称<br>例: `Fund USDT e3aa8545` |
| historyRecords | object[] |  | Subscription and redemption records<br>申购和赎回记录 |
| historyRecords[].type | string |  | Record type<br>记录类型<br>枚举: `SUBSCRIBE`, `REDEEM`<br>例: `SUBSCRIBE` |
| historyRecords[].date | string |  | Operation date (yyyyMMdd)<br>操作日期 (yyyyMMdd)<br>例: `20260601` |
| historyRecords[].amount | string |  | Amount, string decimal<br>金额，字符串小数<br>例: `50000.00` |
| historyRecords[].currency | string |  | Asset<br>币种<br>例: `USDT` |
| historyRecords[].status | string |  | Record status<br>记录状态<br>枚举: `SUCCESS`, `FAIL`, `PENDING`<br>例: `SUCCESS` |

## Query Investor Portfolio Realtime Asset Value（查询投资组合实时资产价值（适用于投资人））

`GET /sapi/v1/portfolio-account/investor/portfolio-realtime-asset-value`

Return the current NAV per allocation and the calling investor's current equity. Requires a key on the investor's own account.

查询当前每份净值以及调用投资人当前的权益。需使用投资人自己账户的 API Key。

Operation ID: `queryInvestorPortfolioRealtimeAssetValue`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| portfolioId | query | string | 是 | Portfolio ID<br>投资组合 ID<br>例: `CC00556589` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Realtime NAV per allocation and investor equity / 实时每份净值和投资人权益

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| portfolioId | string |  | Portfolio ID<br>投资组合 ID<br>例: `CC00556589` |
| portfolioName | string |  | Portfolio name<br>投资组合名称<br>例: `Fund USDT e3aa8545` |
| timestamp | string |  | Query time, UTC, ISO 8601<br>查询时间，UTC，ISO 8601<br>例: `2026-10-30T05:25:30Z` |
| navPerAllocation | string |  | Realtime NAV per allocation<br>实时每份净值<br>例: `0.14450128` |
| investorShares | string |  | The investor's current allocations<br>投资人当前持有份额<br>例: `1000000.00000000` |
| investorNav | string |  | navPerAllocation × investorShares<br>例: `144501.28` |