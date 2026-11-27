---
exchange: binance
source_url: https://developers.binance.com/en/docs/catalog/investment-and-services-fiat/api/rest-api
api_type: REST
updated_at: 2026-11-27 18:48:08.877990
---

# Fiat REST API

Schema: https://developers.binance.com/en/docs/catalog/investment-and-services-fiat/api/rest-api/1.0.0/schema.yaml

Query Binance fiat deposit and withdrawal history.

查询 Binance 法币充值和提现历史。

版本: 1.0.0

## 服务地址

- `https://api.binance.com`
- `https://api-gcp.binance.com`
- `https://api1.binance.com`
- `https://api2.binance.com`
- `https://api3.binance.com`
- `https://api4.binance.com`

## 接口列表

- `POST /sapi/v1/fiat/deposit` — Deposit (TRADE)
- `POST /sapi/v2/fiat/withdraw` — Fiat Withdraw (TRADE)
- `GET /sapi/v1/fiat/orders` — Get Fiat Deposit/Withdraw History (USER_DATA)
- `GET /sapi/v1/fiat/payments` — Get Fiat Payments History (USER_DATA)
- `GET /sapi/v1/fiat/get-order-detail` — Get Order Detail (USER_DATA)

## Deposit (TRADE)（法币充值 (TRADE)）

`POST /sapi/v1/fiat/deposit`

Submit deposit request, in this version, we only support BRL deposit via pix.

For BRL deposit via pix, you need to place an order before making a transfer from your bank.

Before calling this api, please make sure you have already completed your KYC or KYB, and already activated your
fiat service on our website.

提交充值请求。目前版本仅支持通过 Pix 进行巴西雷亚尔 (BRL) 充值。

如需通过 Pix 进行巴西雷亚尔充值，您需要在从银行转账前下单。

调用此 API 前，请确保您已完成 KYC 或 KYB 验证，并在我们的网站上激活了法币服务。

Operation ID: `deposit`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| currency | string | 是 | 例: `BRL` |
| apiPaymentMethod | string | 是 | payment method; current supported: pix<br>支付方式；当前仅支持：pix<br>枚举: `pix`<br>例: `pix` |
| amount | string | 是 | deposit amount<br>充值金额<br>例: `1` |
| ext | object |  |  |

### 响应 200：Deposit / 法币充值

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  | 例: `000000` |
| message | string |  | 例: `success` |
| data | object |  |  |
| data.orderId | string |  | deposit order id<br>充值订单号<br>例: `04595xxxxxxxxx37` |

## Fiat Withdraw (TRADE)（法币提现 (TRADE)）

`POST /sapi/v2/fiat/withdraw`

Submit withdraw request, in this version, we support BRL,ARS,MXN withdrawal via bank_transfer.

You need to call this api first, and call query order detail api in a loop to get the status of the order until
this order is successful.

Before calling this api, please make sure you have already completed your KYC or KYB, and already activated your
fiat service on our website.

提交提现请求。此版本仅支持通过银行转账提现巴西雷亚尔。

您需要先调用此 API，然后循环调用查询订单详情 API 以获取订单状态，直至订单成功。

调用此 API 前，请确保您已完成 KYC 或 KYB 验证，并在我们的网站上激活了法币服务。

Operation ID: `fiatWithdraw`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds<br>请求有效时间窗口（毫秒）<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| currency | string | 是 | Fiat currency, such as BRL, ARS, MXN<br>法币币种，例如 BRL、ARS、MXN<br>例: `BRL` |
| apiPaymentMethod | string | 是 | payment method; current supported: bank_transfer<br>支付方式；当前仅支持：bank_transfer<br>枚举: `bank_transfer`<br>例: `bank_transfer` |
| amount | integer (int64) | 是 | withdraw amount<br>提现金额<br>例: `10` |
| accountInfo | object | 是 | withdraw account info<br>提现账户信息 |
| accountInfo.accountNumber | string | 是 | Your destination bank account number is required to receive the withdrawal. In Argentina, this will be your CBU/CVU; in Mexico, it will be your CLABE.<br>提现时必须提供收款银行账号。在阿根廷为 CBU/CVU；在墨西哥为 CLABE。<br>例: `1056894222` |
| accountInfo.agency | string |  | Bank agency code. If contains a hyphen (e.g. `123-4`), enter `123` only.<br>银行机构编号。若有连字符（如 `123-4`），请只填 `123`。<br>例: `1234` |
| accountInfo.bankCodeForPix | string |  | Bank code used for PIX routing.<br>用于 PIX 路由的银行代码。<br>例: `222` |
| accountInfo.accountType | string |  | Account type, e.g. `current` (Checking Account), `saving` (Savings Account), etc.<br>账户种类，例如 `current`（支票账户）、`saving`（储蓄账户）等。<br>例: `current` |
| ext | object |  |  |

### 响应 200：Fiat Withdraw / 法币提现

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  | 例: `000000` |
| message | string |  | 例: `success` |
| data | object |  |  |
| data.orderId | string |  | 例: `04595xxxxxxxxx37` |

## Get Fiat Deposit/Withdraw History (USER_DATA)（获取法币充值/提现历史记录 (USER_DATA)）

`GET /sapi/v1/fiat/orders`

Get Fiat Deposit/Withdraw History

获取法币充值/提现历史记录

Operation ID: `getFiatDepositWithdrawHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| transactionType | query | string | 是 | 0: deposit, 1: withdraw<br>0：充值，1：提现<br>例: `0` |
| beginTime | query | integer (int64) |  | 例: `1641782889000` |
| endTime | query | integer (int64) |  | 例: `1641782889000` |
| page | query | integer (int64) |  | 默认: `1`<br>例: `1` |
| rows | query | integer (int64) |  | 默认: `100`<br>例: `100` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Fiat Deposit/Withdraw History / 获取法币充值/提现历史记录

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  | 例: `000000` |
| message | string |  | 例: `success` |
| data | object[] |  |  |
| data[].orderNo | string |  | 例: `7d76d611-0568-4f43-afb6-24cac7767365` |
| data[].fiatCurrency | string |  | Fiat token<br>法币token<br>例: `BRL` |
| data[].indicatedAmount | string |  | Trade amount<br>交易金额<br>例: `10.00` |
| data[].amount | string |  | Actual amount (after fee deduction)<br>实际金额（扣除手续费）<br>例: `10.00` |
| data[].totalFee | string |  | Trade fee<br>交易手续费<br>例: `0.00` |
| data[].method | string |  | Trade method<br>交易方式<br>例: `BankAccount` |
| data[].status | string |  | Processing, Failed, Successful, Finished, Refunding, Refunded, Refund Failed, Order Partial Credit Stopped<br>处理中、失败、成功、已完成、退款中、已退款、退款失败、订单部分入账已停止<br>例: `Expired` |
| data[].createTime | integer (int64) |  | Order create time<br>订单创建时间<br>例: `1626144956000` |
| data[].updateTime | integer (int64) |  | Order update time<br>订单更新时间<br>例: `1626400907000` |
| total | integer (int64) |  | 例: `1` |
| success | boolean |  | 例: `True` |

## Get Fiat Payments History (USER_DATA)（获取法币支付历史记录 (USER_DATA)）

`GET /sapi/v1/fiat/payments`

Get Fiat Payments History

获取法币支付历史记录

Operation ID: `getFiatPaymentsHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| transactionType | query | string | 是 | 0: buy, 1: sell<br>0：买入，1：卖出<br>例: `0` |
| beginTime | query | integer (int64) |  | 例: `1641782889000` |
| endTime | query | integer (int64) |  | 例: `1641782889000` |
| page | query | integer (int64) |  | 默认: `1`<br>例: `1` |
| rows | query | integer (int64) |  | 默认: `100`<br>例: `100` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Fiat Payments History / 获取法币支付历史记录

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  | 例: `000000` |
| message | string |  | 例: `success` |
| data | object[] |  |  |
| data[].orderNo | string |  | 例: `353fca443f06466db0c4dc89f94f027a` |
| data[].sourceAmount | string |  | Fiat trade amount<br>法币交易数量<br>例: `20.0` |
| data[].fiatCurrency | string |  | Fiat token<br>法币token<br>例: `EUR` |
| data[].obtainAmount | string |  | Crypto trade amount<br>数字货币交易数量<br>例: `4.462` |
| data[].cryptoCurrency | string |  | Crypto token<br>数字货币token<br>例: `LUNA` |
| data[].totalFee | string |  | Trade fee<br>交易手续费<br>例: `0.2` |
| data[].price | string |  | Price<br>价格<br>例: `4.437472` |
| data[].status | string |  | Processing, Completed, Failed, Refunded<br>Processing处理中, Completed完成, Failed失败, Refunded退款<br>例: `Failed` |
| data[].paymentMethod | string |  | Payment method<br>支付方式<br>例: `Credit Card` |
| data[].createTime | integer (int64) |  | Order create time<br>订单创建时间<br>例: `1624529919000` |
| data[].updateTime | integer (int64) |  | Order update time<br>订单更新时间<br>例: `1624529919000` |
| total | integer (int64) |  | 例: `1` |
| success | boolean |  | 例: `True` |

## Get Order Detail (USER_DATA)（获取订单详情 (USER_DATA)）

`GET /sapi/v1/fiat/get-order-detail`

Get Order Detail

Before calling this api, please make sure you have already completed your KYC or KYB, and already activated your
fiat service on our website.

获取订单详情页

在调用此 API 之前，请确保您已完成 KYC 或 KYB 验证，并且已在我们的网站上激活您的法币服务。

Operation ID: `getOrderDetail`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| orderNo | query | string | 是 | Order ID retrieved from the withdrawal API<br>从提现接口获取的订单 ID<br>例: `036752*678` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Order Detail / 获取订单详情

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  | 例: `000000` |
| message | string |  | 例: `success` |
| data | object |  |  |
| data.orderId | string |  | Order id<br>订单号<br>例: `036752*678` |
| data.orderStatus | string |  | Order status<br>订单状态<br>例: `ORDER_INITIAL` |
| data.amount | string |  | Order amount<br>订单金额<br>例: `4.33` |
| data.fee | string |  | Trade fee<br>交易手续费<br>例: `0.43` |
| data.fiatCurrency | string |  | Fiat token<br>法币token<br>例: `***` |
| data.errorCode | string |  | Error code if any<br>错误代码（如有）<br>例: `` |
| data.errorMessage | string |  | Error message if any<br>错误信息（如有）<br>例: `` |
| data.ext | object |  | Extra info<br>额外信息 |