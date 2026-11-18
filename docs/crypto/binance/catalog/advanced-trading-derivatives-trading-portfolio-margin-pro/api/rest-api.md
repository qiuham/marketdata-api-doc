---
exchange: binance
source_url: https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin-pro/api/rest-api
api_type: REST
updated_at: 2026-11-18 18:48:24.345808
---

# Portfolio Margin Pro REST API

Schema: https://developers.binance.com/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin-pro/api/rest-api/1.0.0/schema.yaml

Access advanced account management and high-frequency trading with Binance Portfolio Margin Pro.

通过 Binance Portfolio Margin Pro 进行高级账户管理和高频交易。

版本: 1.0.0

## 服务地址

- `https://api.binance.com`
- `https://api1.binance.com`
- `https://api2.binance.com`
- `https://api3.binance.com`
- `https://api4.binance.com`

## 接口列表

- `POST /sapi/v1/portfolio/bnb-transfer` — BNB transfer (USER_DATA)
- `GET /sapi/v1/portfolio/repay-futures-switch` — Get Auto-repay-futures Status (USER_DATA)
- `POST /sapi/v1/portfolio/repay-futures-switch` — Change Auto-repay-futures Status (TRADE)
- `POST /sapi/v1/portfolio/auto-collection` — Fund Auto-collection (USER_DATA)
- `POST /sapi/v1/portfolio/asset-collection` — Fund Collection by Asset (USER_DATA)
- `GET /sapi/v1/portfolio/delta-mode` — Get Delta Mode Status (USER_DATA)
- `POST /sapi/v1/portfolio/delta-mode` — Switch Delta Mode (TRADE)
- `GET /sapi/v1/portfolio/balance` — Get Portfolio Margin Pro Account Balance (USER_DATA)
- `GET /sapi/v1/portfolio/account` — Get Portfolio Margin Pro Account Info (USER_DATA)
- `GET /sapi/v2/portfolio/account` — Get Portfolio Margin Pro SPAN Account Info (USER_DATA)
- `GET /sapi/v1/portfolio/earn-asset-balance` — Get Transferable Earn Asset Balance for Portfolio Margin (USER_DATA)
- `POST /sapi/v1/portfolio/repay` — Portfolio Margin Pro Bankruptcy Loan Repay (TRADE)
- `GET /sapi/v1/portfolio/pmLoan` — Query Portfolio Margin Pro Bankruptcy Loan Amount (USER_DATA)
- `GET /sapi/v1/portfolio/pmloan-history` — Query Portfolio Margin Pro Bankruptcy Loan Repay History (USER_DATA)
- `GET /sapi/v1/portfolio/interest-history` — Query Portfolio Margin Pro Negative Balance Interest History (USER_DATA)
- `POST /sapi/v1/portfolio/repay-futures-negative-balance` — Repay futures Negative Balance (USER_DATA)
- `POST /sapi/v1/portfolio/earn-asset-transfer` — Transfer LDUSDT/RWUSD for Portfolio Margin (TRADE)
- `GET /sapi/v1/portfolio/margin-call-level` — Get Margin Call Level (USER_DATA)
- `POST /sapi/v1/portfolio/margin-call-level` — Set Margin Call Level (USER_DATA)
- `DELETE /sapi/v1/portfolio/margin-call-level` — Delete Margin Call Level (USER_DATA)
- `GET /sapi/v1/portfolio/margin-asset-leverage` — Get Portfolio Margin Asset Leverage (USER_DATA)
- `GET /sapi/v1/portfolio/collateralRate` — Portfolio Margin Collateral Rate (MARKET_DATA)
- `GET /sapi/v2/portfolio/collateralRate` — Portfolio Margin Pro Tiered Collateral Rate (USER_DATA)
- `GET /sapi/v2/portfolio/retail/collateralRate` — Get Portfolio Margin Tiered Collateral Rates (MARKET_DATA)
- `GET /sapi/v1/portfolio/asset-index-price` — Query Portfolio Margin Asset Index Price (MARKET_DATA)

## BNB transfer (USER_DATA)（BNB划转 (USER_DATA)）

`POST /sapi/v1/portfolio/bnb-transfer`

BNB transfer can be between Margin Account and USDM Account

BNB在杠杆账户和USD-M期货账户划转

Operation ID: `bnbTransfer`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| amount | number (float) | 是 | 例: `1.0` |
| transferSide | string | 是 | 枚举: `TO_UM`, `FROM_UM`<br>例: `TO_UM` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：BNB transfer / BNB 划转

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| tranId | integer (int64) |  | tran Id.<br>请参见英文说明：tran Id.<br>例: `100000001` |

## Get Auto-repay-futures Status (USER_DATA)（查询自动清还合约负余额模式 (USER_DATA)）

`GET /sapi/v1/portfolio/repay-futures-switch`

Query Auto-repay-futures Status

查询自动清还合约负余额模式

Operation ID: `getAutoRepayFuturesStatus`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Auto-repay-futures Status / 获取Auto-repay-futures 状态

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| autoRepay | boolean |  | "true" for turn on the auto-repay futures; "false" for turn off the auto-repay futures<br>`true`代表自动清还合约负余额; `false`代表关闭自动清还合约负余额<br>例: `True` |

## Change Auto-repay-futures Status (TRADE)（更改自动清还合约负余额模式 (TRADE)）

`POST /sapi/v1/portfolio/repay-futures-switch`

Change Auto-repay-futures Status

更改自动支付合约负余额模式

Operation ID: `changeAutoRepayFuturesStatus`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| autoRepay | string | 是 | `false` for turn off the auto-repay futures negative balance function<br>`false`代表关闭自动清还合约负余额<br>枚举: `true`, `false`<br>默认: `true`<br>例: `true` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Change Auto-repay-futures Status / 修改Auto-repay-futures 状态

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| msg | string |  | msg.<br>请参见英文说明：msg.<br>例: `success` |

## Fund Auto-collection (USER_DATA)（资金归集 (USER_DATA)）

`POST /sapi/v1/portfolio/auto-collection`

Transfers all assets from Futures Account to Margin account

将期货账户下所有资产归集至杠杆账户。

Operation ID: `fundAutoCollection`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Fund Auto-collection / 请参见英文说明：Fund Auto-collection

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| msg | string |  | msg.<br>请参见英文说明：msg.<br>例: `success` |

## Fund Collection by Asset (USER_DATA)（特定资产资金归集 (USER_DATA)）

`POST /sapi/v1/portfolio/asset-collection`

Transfers specific asset from Futures Account to Margin account

特定资产账户资金归集，从合约账户划转到杠杆账户

Operation ID: `fundCollectionByAsset`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| asset | string | 是 | 例: `USDT` |
| amount | number (float) |  | Amount to collect. When provided, `futureType` is required.<br>待归集的数量。传入该参数时，`futureType` 为必填。<br>例: `10` |
| futureType | string |  | Target wallet for the collection. `OPTION` is for SPAN only. Cannot be sent without `amount`. `amount` and `futureType` must be provided together. If neither is provided, existing behavior is unchanged (query all wallets + transfer).<br>归集的目标钱包。`OPTION` 仅支持 SPAN。不能在不传 `amount` 的情况下传入。`amount` 和 `futureType` 必须同时传入。均不传入时行为不变（查询所有钱包并划转）。<br>枚举: `UM`, `CM`, `OPTION`<br>例: `UM` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Fund Collection by Asset / Fund Collection by 资产

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| msg | string |  | msg.<br>请参见英文说明：msg.<br>例: `success` |

## Get Delta Mode Status (USER_DATA)（查询账户Delta模式状态 (USER_DATA)）

`GET /sapi/v1/portfolio/delta-mode`

Query the Delta mode status of current account.

查询账户Delta模式状态

Operation ID: `getDeltaModeStatus`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Delta Mode Status / 获取Delta Mode 状态

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| deltaEnabled | boolean |  | delta Enabled.<br>请参见英文说明：delta Enabled.<br>例: `False` |

## Switch Delta Mode (TRADE)（切换账户Delta模式 (TRADE)）

`POST /sapi/v1/portfolio/delta-mode`

Switch the Delta mode for existing PM PRO / PM RETAIL accounts.

切换当前 PM PRO / PM RETAIL账户Delta 模式

Operation ID: `switchDeltaMode`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| deltaEnabled | string | 是 | `true` to enable Delta mode; `false` to disable Delta mode<br>`true`为开启Delta模式; `false`代表关闭Delta模式<br>枚举: `true`, `false`<br>例: `true` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Switch Delta Mode / 请参见英文说明：Switch Delta Mode

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| msg | string |  | msg.<br>请参见英文说明：msg.<br>例: `success` |

## Get Portfolio Margin Pro Account Balance (USER_DATA)（查询统一账户专业版账户余额 (USER_DATA)）

`GET /sapi/v1/portfolio/balance`

Query Portfolio Margin Pro account balance

查询统一账户专业版账户余额

Operation ID: `getPortfolioMarginProAccountBalance`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| asset | query | string |  | 例: `BTC` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Portfolio Margin Pro Account Balance / 获取Portfolio 杠杆 Pro 账户 Balance

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].asset | string |  | asset.<br>请参见英文说明：asset.<br>例: `USDT` |
| [].totalWalletBalance | string |  | total Wallet Balance.<br>请参见英文说明：total Wallet Balance.<br>例: `122607.35137903` |
| [].crossMarginAsset | string |  | cross Margin Asset.<br>请参见英文说明：cross Margin Asset.<br>例: `92.27530794` |
| [].crossMarginBorrowed | string |  | cross Margin Borrowed.<br>请参见英文说明：cross Margin Borrowed.<br>例: `10.00000000` |
| [].crossMarginFree | string |  | cross Margin Free.<br>请参见英文说明：cross Margin Free.<br>例: `100.00000000` |
| [].crossMarginInterest | string |  | cross Margin Interest.<br>请参见英文说明：cross Margin Interest.<br>例: `0.72469206` |
| [].crossMarginLocked | string |  | cross Margin Locked.<br>请参见英文说明：cross Margin Locked.<br>例: `3.00000000` |
| [].umWalletBalance | string |  | um Wallet Balance.<br>请参见英文说明：um Wallet Balance.<br>例: `0.00000000` |
| [].umUnrealizedPNL | string |  | um Unrealized PNL.<br>请参见英文说明：um Unrealized PNL.<br>例: `23.72469206` |
| [].cmWalletBalance | string |  | cm Wallet Balance.<br>请参见英文说明：cm Wallet Balance.<br>例: `23.72469206` |
| [].cmUnrealizedPNL | string |  | cm Unrealized PNL.<br>请参见英文说明：cm Unrealized PNL.<br>例: `` |
| [].updateTime | integer (int64) |  | update Time.<br>请参见英文说明：update Time.<br>例: `1617939110373` |
| [].negativeBalance | string |  | negative Balance.<br>请参见英文说明：negative Balance.<br>例: `0` |
| [].optionWalletBalance | string |  | option Wallet Balance.<br>请参见英文说明：option Wallet Balance.<br>例: `0` |
| [].optionEquity | string |  | option Equity.<br>请参见英文说明：option Equity.<br>例: `0` |

## Get Portfolio Margin Pro Account Info (USER_DATA)（查询统一账户专业版账户信息 (USER_DATA)）

`GET /sapi/v1/portfolio/account`

Get Portfolio Margin Pro Account Info

查询统一账户专业版账户信息

Operation ID: `getPortfolioMarginProAccountInfo`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Portfolio Margin Pro Account Info / 获取Portfolio 杠杆 Pro 账户 Info

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| uniMMR | string |  | Classic Portfolio margin account maintenance margin rate<br>经典统一账户模式维持保证金率<br>例: `5167.92171923` |
| accountEquity | string |  | Account equity, unit：USD<br>经典统一账户总权益，单位为USD<br>例: `122607.35137903` |
| actualEquity | string |  | Actual equity, unit：USD<br>不考虑质押率经典统一账户总权益，单位为USD<br>例: `142607.35137903` |
| accountMaintMargin | string |  | Classic Portfolio margin account maintenance margin, unit：USD<br>经典统一账户维持保证金，即账户开仓及借贷总共需要的维持保证金，单位为USD<br>例: `23.72469206` |
| accountInitialMargin | string |  | Ignored for PM PRO and PM PRO SPAN<br>PM PRO and PM PRO SPAN请忽略<br>例: `47.44938412` |
| totalAvailableBalance | string |  | Ignored for PM PRO and PM PRO SPAN<br>PM PRO and PM PRO SPAN请忽略<br>例: `122,559.90199491` |
| accountStatus | string |  | Classic Portfolio margin account status:"NORMAL", "MARGIN_CALL", "SUPPLY_MARGIN", "REDUCE_ONLY", "ACTIVE_LIQUIDATION", "FORCE_LIQUIDATION", "BANKRUPTED"<br>经典统一账户当前账户状态:"NORMAL"正常状态, "MARGIN_CALL"补充保证金, "SUPPLY_MARGIN"再一次补充保证金, "REDUCE_ONLY"触发交易限制, "ACTIVE_LIQUIDATION"手动强制平仓, "FORCE_LIQUIDATION"强制平仓, "BANKRUPTED"破产<br>例: `NORMAL` |
| accountType | string |  | PM_1 for PM PRO, PM_2 for PM, PM_3 for PM PRO SPAN<br>PM_1统一账户专业版, PM_2统一账户， PM_2统一账户专业版SPAN<br>例: `PM_1` |

## Get Portfolio Margin Pro SPAN Account Info (USER_DATA)（查询统一账户专业版SPAN账户信息 (USER_DATA)）

`GET /sapi/v2/portfolio/account`

Get Portfolio Margin Pro SPAN Account Info (For Portfolio Margin Pro SPAN users only)

查询统一账户专业版SPAN账户信息

Operation ID: `getPortfolioMarginProSpanAccountInfo`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Portfolio Margin Pro SPAN Account Info / 获取Portfolio 杠杆 Pro SPAN 账户 Info

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| uniMMR | string |  | uni MMR.<br>请参见英文说明：uni MMR.<br>例: `5167.92171923` |
| accountEquity | string |  | Account equity, unit：USD<br>例: `122607.35137903` |
| actualEquity | string |  | Actual equity, unit：USD<br>例: `142607.35137903` |
| accountMaintMargin | string |  | Account maintenance margin, unit：USD<br>例: `23.72469206` |
| riskUnitMMList | object[] |  |  |
| riskUnitMMList[].asset | string |  | asset.<br>请参见英文说明：asset.<br>例: `BTC` |
| riskUnitMMList[].uniMaintainUsd | string |  | uni Maintain Usd.<br>请参见英文说明：uni Maintain Usd.<br>例: `23.72469206` |
| marginMM | string |  | margin MM.<br>请参见英文说明：margin MM.<br>例: `0.00000000` |
| otherMM | string |  | other MM.<br>请参见英文说明：other MM.<br>例: `0.00000000` |
| accountStatus | string |  | Classic Portfolio margin account status:"NORMAL", "MARGIN_CALL", "SUPPLY_MARGIN", "REDUCE_ONLY", "ACTIVE_LIQUIDATION", "FORCE_LIQUIDATION", "BANKRUPTED"<br>例: `NORMAL` |
| accountType | string |  | PM_1 for classic PM, PM_2 for PM, PM_3 for PM Pro(SPAN)<br>例: `PM_3` |

## Get Transferable Earn Asset Balance for Portfolio Margin (USER_DATA)（获取划转able Earn 资产 Balance 用于 Portfolio 杠杆 (USER_DATA)）

`GET /sapi/v1/portfolio/earn-asset-balance`

Get transferable earn asset balance for all types of Portfolio Margin account

获取transferable earn 资产 balance 用于 all types of Portfolio 杠杆 账户

Operation ID: `getTransferableEarnAssetBalanceForPortfolioMargin`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| asset | query | string | 是 | `LDUSDT` only<br>`LDUSDT` 仅<br>例: `LDUSDT` |
| transferType | query | string | 是 | 枚举: `EARN_TO_FUTURE`, `FUTURE_TO_EARN`<br>例: `EARN_TO_FUTURE` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Transferable Earn Asset Balance for Portfolio Margin / 获取划转able Earn 资产 Balance 用于 Portfolio 杠杆

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| asset | string |  | asset.<br>请参见英文说明：asset.<br>例: `LDUSDT` |
| amount | string |  | amount.<br>请参见英文说明：amount.<br>例: `0.55` |

## Portfolio Margin Pro Bankruptcy Loan Repay (TRADE)（偿还统一账户专业版穿仓负债 (TRADE)）

`POST /sapi/v1/portfolio/repay`

Repay Portfolio Margin Pro Bankruptcy Loan

偿还统一账户专业版穿仓负债

Operation ID: `portfolioMarginProBankruptcyLoanRepay`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Portfolio Margin Pro Bankruptcy Loan Repay / Portfolio 杠杆 Pro Bankruptcy 借贷 还款

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| tranId | integer (int64) |  | tran Id.<br>请参见英文说明：tran Id.<br>例: `58203331886213500` |

## Query Portfolio Margin Pro Bankruptcy Loan Amount (USER_DATA)（查询统一账户专业版穿仓借贷金额 (USER_DATA)）

`GET /sapi/v1/portfolio/pmLoan`

Query Portfolio Margin Pro Bankruptcy Loan Amount

查询统一账户专业版穿仓借贷金额

Operation ID: `queryPortfolioMarginProBankruptcyLoanAmount`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Portfolio Margin Pro Bankruptcy Loan Amount / Portfolio 杠杆 Pro Bankruptcy 借贷 数量

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| asset | string |  | asset.<br>请参见英文说明：asset.<br>例: `BUSD` |
| amount | string |  | portfolio margin bankruptcy loan amount in BUSD<br>统一账户用户强平穿仓负债，单位为BUSD<br>例: `579.45` |

## Query Portfolio Margin Pro Bankruptcy Loan Repay History (USER_DATA)（查询经典统一账户专业版穿仓借贷偿还历史 (USER_DATA)）

`GET /sapi/v1/portfolio/pmloan-history`

Query repay history of pmloan for portfolio margin pro.

查询统一账户专业版穿仓借贷偿还历史

Operation ID: `queryPortfolioMarginProBankruptcyLoanRepayHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| startTime | query | integer (int64) |  | Start time<br>起始时间<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | End time<br>结束时间<br>例: `1641782889000` |
| size | query | integer (int64) |  | Number of results returned.<br>返回的结果集数量 默认值:10 最大值:100<br>默认: `10`<br>例: `10` |
| current | query | integer (int64) |  | Currently querying page. Start from 1.<br>默认值：1<br>默认: `1`<br>例: `1` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Portfolio Margin Pro Bankruptcy Loan Repay History / Portfolio 杠杆 Pro Bankruptcy 借贷 还款 历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| total | integer (int64) |  | total.<br>请参见英文说明：total.<br>例: `3` |
| rows | object[] |  |  |
| rows[].asset | string |  | asset.<br>请参见英文说明：asset.<br>例: `USDT` |
| rows[].amount | string |  | amount.<br>请参见英文说明：amount.<br>例: `404.80294503` |
| rows[].repayTime | integer (int64) |  | repay Time.<br>请参见英文说明：repay Time.<br>例: `1731336427804` |

## Query Portfolio Margin Pro Negative Balance Interest History (USER_DATA)（查询经典统一账户专业版期货负余额收息历史 (USER_DATA)）

`GET /sapi/v1/portfolio/interest-history`

Query interest history of negative balance for portfolio margin.

查询统一账户专业版期货负余额收息历史

Operation ID: `queryPortfolioMarginProNegativeBalanceInterestHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| asset | query | string |  | 例: `USDT` |
| startTime | query | integer (int64) |  | Start time<br>起始时间<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | End time<br>结束时间<br>例: `1641782889000` |
| size | query | integer (int64) |  | Number of results returned.<br>返回的结果集数量 默认值:10 最大值:100<br>默认: `10`<br>例: `10` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Portfolio Margin Pro Negative Balance Interest History / Portfolio 杠杆 Pro Negative Balance 利息 历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].asset | string |  | asset.<br>请参见英文说明：asset.<br>例: `USDT` |
| [].interest | string |  | interest amount<br>利息金额<br>例: `24.4440` |
| [].interestAccruedTime | integer (int64) |  | interest Accrued Time.<br>请参见英文说明：interest Accrued Time.<br>例: `1670227200000` |
| [].interestRate | string |  | daily interest rate<br>日利率<br>例: `0.0001164` |
| [].principal | string |  | principal.<br>请参见英文说明：principal.<br>例: `210000` |

## Repay futures Negative Balance (USER_DATA)（清还合约负余额 (USER_DATA)）

`POST /sapi/v1/portfolio/repay-futures-negative-balance`

Repay futures Negative Balance

清还合约负余额

Operation ID: `repayFuturesNegativeBalance`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Repay futures Negative Balance / 还款 合约 Negative Balance

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| msg | string |  | msg.<br>请参见英文说明：msg.<br>例: `success` |

## Transfer LDUSDT/RWUSD for Portfolio Margin (TRADE)（统一账户转入LDUSDT/RWUSD资产 (TRADE)）

`POST /sapi/v1/portfolio/earn-asset-transfer`

Transfer LDUSDT/RWUSD as collateral for all types of Portfolio Margin account

LDUSDT/RWUSD转入，支持所有的统一账户类型

Operation ID: `transferLdusdtRwusdForPortfolioMargin`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| asset | string | 是 | 枚举: `LDUSDT`, `RWUSD`<br>例: `LDUSDT` |
| transferType | string | 是 | 枚举: `EARN_TO_FUTURE`, `FUTURE_TO_EARN`<br>例: `EARN_TO_FUTURE` |
| amount | number (float) | 是 | 例: `1` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Transfer LDUSDT/RWUSD for Portfolio Margin / 划转 LDUSDT/RWUSD 用于 Portfolio 杠杆

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| msg | string |  | msg.<br>请参见英文说明：msg.<br>例: `success` |

## Get Margin Call Level (USER_DATA)（查询强平预警线 (USER_DATA)）

`GET /sapi/v1/portfolio/margin-call-level`

Get the margin call level for a Portfolio Margin account.

查询统一保证金账户的强平预警线。

Operation ID: `getMarginCallLevel`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Margin Call Level / 查询强平预警线

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| marginCallLevel | string |  | The margin call level value. Empty object returned if not set.<br>强平预警线值。未设置时返回空对象。<br>例: `1.67354637` |

## Set Margin Call Level (USER_DATA)（设置强平预警线 (USER_DATA)）

`POST /sapi/v1/portfolio/margin-call-level`

Set the margin call level for a Portfolio Margin account. When the account's uniMMR drops to the specified level, a notification will be sent via email and push/inbox.

设置统一保证金账户的强平预警线。当账户的 uniMMR 降至指定水平时，系统将通过邮件和推送/站内信发送通知。

Operation ID: `setMarginCallLevel`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| marginCallLevel | number (float) | 是 | The value must be within the range [1.1, 2.0].<br>取值范围必须在 [1.1, 2.0] 之间。<br>例: `1.5` |
| recvWindow | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Set Margin Call Level / 设置强平预警线

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| marginCallLevel | string |  | The margin call level that was set<br>已设置的强平预警线值<br>例: `1.67354637` |

## Delete Margin Call Level (USER_DATA)（删除强平预警线 (USER_DATA)）

`DELETE /sapi/v1/portfolio/margin-call-level`

Delete the margin call level for a Portfolio Margin account.

删除统一保证金账户的强平预警线。

Operation ID: `deleteMarginCallLevel`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Delete Margin Call Level / 删除强平预警线

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| msg | string |  | 例: `success` |

## Get Portfolio Margin Asset Leverage (USER_DATA)（查询统一账户资产支持杠杆倍数 (USER_DATA)）

`GET /sapi/v1/portfolio/margin-asset-leverage`

Get Portfolio Margin Asset Leverage

查询统一账户资产支持杠杆倍数

Operation ID: `getPortfolioMarginAssetLeverage`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Portfolio Margin Asset Leverage / 获取Portfolio 杠杆 资产 Leverage

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].asset | string |  | asset.<br>请参见英文说明：asset.<br>例: `USDC` |
| [].leverage | integer (int64) |  | leverage.<br>请参见英文说明：leverage.<br>例: `10` |

## Portfolio Margin Collateral Rate (MARKET_DATA)（统一账户资产质押率 (MARKET_DATA)）

`GET /sapi/v1/portfolio/collateralRate`

Portfolio Margin Collateral Rate

统一账户资产质押率

Operation ID: `portfolioMarginCollateralRate`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 响应 200：Portfolio Margin Collateral Rate / Portfolio 杠杆 抵押 利率

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].asset | string |  | asset.<br>请参见英文说明：asset.<br>例: `USDC` |
| [].collateralRate | string |  | collateral Rate.<br>质押率<br>例: `1.0000` |

## Portfolio Margin Pro Tiered Collateral Rate (USER_DATA)（统一账户专业版资产阶梯质押率 (USER_DATA)）

`GET /sapi/v2/portfolio/collateralRate`

Portfolio Margin PRO Tiered Collateral Rate

统一账户专业版资产阶梯质押率

Operation ID: `portfolioMarginProTieredCollateralRate`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Portfolio Margin Pro Tiered Collateral Rate / Portfolio 杠杆 Pro Tiered 抵押 利率

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].asset | string |  | asset.<br>请参见英文说明：asset.<br>例: `BNB` |
| [].collateralInfo | object[] |  |  |
| [].collateralInfo[].tierFloor | string |  | tier Floor.<br>请参见英文说明：tier Floor.<br>例: `0.0000` |
| [].collateralInfo[].tierCap | string |  | tier Cap.<br>请参见英文说明：tier Cap.<br>例: `1000.0000` |
| [].collateralInfo[].collateralRate | string |  | collateral Rate.<br>请参见英文说明：collateral Rate.<br>例: `1.0000` |
| [].collateralInfo[].cum | string |  | account equity quick addition number<br>账户权益计算速算数<br>例: `0.0000` |

## Get Portfolio Margin Tiered Collateral Rates (MARKET_DATA)（获取统一账户阶梯质押率 (MARKET_DATA)）

`GET /sapi/v2/portfolio/retail/collateralRate`

Query the tiered collateral rate configurations for Portfolio Margin assets.

查询统一账户各资产的完整阶梯质押率配置。统一账户和统一账户专业版的质押率参数独立配置。本接口返回 Portfolio Margin 账户适用的配置。

Operation ID: `getPortfolioMarginTieredCollateralRates`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 响应 200：Portfolio Margin Tiered Collateral Rates / 统一账户阶梯质押率

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].asset | string |  | asset.<br>资产<br>例: `BNB` |
| [].collateralInfo | object[] |  |  |
| [].collateralInfo[].tierFloor | string |  | tier Floor.<br>阶梯下限<br>例: `0.0000` |
| [].collateralInfo[].tierCap | string |  | tier Cap.<br>阶梯上限<br>例: `1000.0000` |
| [].collateralInfo[].collateralRate | string |  | collateral Rate.<br>质押率<br>例: `1.0000` |
| [].collateralInfo[].cum | string |  | account equity quick addition number.<br>账户权益计算速算数<br>例: `0.0000` |

## Query Portfolio Margin Asset Index Price (MARKET_DATA)（查询统一账户资产价格指数 (MARKET_DATA)）

`GET /sapi/v1/portfolio/asset-index-price`

Query Portfolio Margin Asset Index Price

查询统一账户资产价格指数

权重: - 1 if `asset` is sent
- 50 if `asset` is not sent

Operation ID: `queryPortfolioMarginAssetIndexPrice`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| asset | query | string |  | 例: `BTC` |

### 响应 200：Portfolio Margin Asset Index Price / Portfolio 杠杆 资产 Index 价格

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].asset | string |  | asset.<br>请参见英文说明：asset.<br>例: `BTC` |
| [].assetIndexPrice | string |  | in USD<br>USD价格指数<br>例: `28251.9136906` |
| [].time | integer (int64) |  | time.<br>请参见英文说明：time.<br>例: `1683518338121` |