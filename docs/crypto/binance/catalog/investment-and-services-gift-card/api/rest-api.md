---
exchange: binance
source_url: https://developers.binance.com/en/docs/catalog/investment-and-services-gift-card/api/rest-api
api_type: REST
updated_at: 2026-11-22 18:46:22.407270
---

# Gift Card REST API

Schema: https://developers.binance.com/en/docs/catalog/investment-and-services-gift-card/api/rest-api/1.0.0/schema.yaml

Create, redeem, and check the value of Binance crypto gift cards.

创建、兑换并查询 Binance 加密货币礼品卡的面值。

版本: 1.0.0

## 服务地址

- `https://api.binance.com`
- `https://api-gcp.binance.com`
- `https://api1.binance.com`
- `https://api2.binance.com`
- `https://api3.binance.com`
- `https://api4.binance.com`

## 接口列表

- `POST /sapi/v1/giftcard/buyCode` — Create a dual-token gift card (fixed value, discount feature) (TRADE)
- `POST /sapi/v1/giftcard/createCode` — Create a single-token gift card (USER_DATA)
- `GET /sapi/v1/giftcard/cryptography/rsa-public-key` — Fetch RSA Public Key (USER_DATA)
- `GET /sapi/v1/giftcard/buyCode/token-limit` — Fetch Token Limit (USER_DATA)
- `POST /sapi/v1/giftcard/redeemCode` — Redeem a Binance Gift Card (USER_DATA)
- `GET /sapi/v1/giftcard/verify` — Verify Binance Gift Card by Gift Card Number (USER_DATA)

## Create a dual-token gift card (fixed value, discount feature) (TRADE)（创建双币种礼品卡(固定价值，设置折扣) (TRADE)）

`POST /sapi/v1/giftcard/buyCode`

* This API is for creating a dual-token ( stablecoin-denominated) Binance Gift Card. You may create a gift card
using USDT as baseToken, that is redeemable to another designated token (faceToken). For example, you can create
a fixed-value BTC gift card and pay with 100 USDT plus minting fee. This gift card can keep the value fixed at
100 USDT before redemption, and will be redeemable to BTC equivalent to 100 USDT upon redemption.

* Once successfully created, the amount of baseToken (e.g. USDT) in the fixed-value gift card along with the fee
would be deducted from your Spot wallet.
  * To get started with, please make sure:
  * You have a Binance account
  * You have passed KYB
  * You have a sufﬁcient balance(Gift Card amount and fee amount) in your Binance Spot wallet
  * You need Enable Withdrawals for the API Key which requests this endpoint.

* 该API用于创建以双币种币安礼品卡，即以稳定币定值的非稳定币礼品卡。您可以通过USDT作为礼品卡的定值币种(baseToken)，来创建可兑现至其他不同币种（faceToken）的币安礼品卡。比如创建固定价值为100
USDT的BTC礼品卡，用USDT制卡，未兑现前始终保持100 USDT的价值，最终兑现出来的是100 USDT等值的BTC。

* 创建后，定值币种(baseToken, 比如USDT)相应的金额和手续费将从你的现货账户中被扣除。
  * 要开始使用，请确保：
  * 你有一个币安账户
  * 你已通过了 KYB
  * 币安现货账户中有足够的余额（礼品卡金额和手续费金额）
  * 你的API Key需要开启允许提现权限

Operation ID: `createADualTokenGiftCard`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| baseToken | string | 是 | The token you want to pay, example: BUSD<br>你用来支付的货币，例如：BUSD<br>例: `BUSD` |
| faceToken | string | 是 | The token you want to buy, example: BNB. If faceToken = baseToken, it's the same as createCode<br>endpoint.<br>你要创建的礼品卡面额币种，例如：BNB。若 `faceToken = baseToken`，则与 `createCode` 接口效果相同。<br>例: `BNB` |
| baseTokenAmount | number (float) | 是 | The base token asset quantity, example : 1.002<br>支付的货币数量，例如：1.002<br>例: `1` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Create a dual-token gift card / 创建双币种礼品卡

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  | 例: `000000` |
| message | string |  | 例: `success` |
| data | object |  |  |
| data.referenceNo | string |  | 例: `0033002144060553` |
| data.code | string |  | 例: `6H9EKF5ECCWFBHGE` |
| data.expiredTime | integer (int64) |  | 例: `1727417154000` |
| success | boolean |  | 例: `True` |

## Create a single-token gift card (USER_DATA)（创建单币种礼品卡 (USER_DATA)）

`POST /sapi/v1/giftcard/createCode`

This API is for creating a Binance Gift Card.

To get started with, please make sure:
  * You have a Binance account
  * You have passed KYB
  * You have a sufﬁcient balance(Gift Card amount and fee amount) in your Binance Spot wallet
  * You need `Enable Withdrawals` for the API Key which requests this endpoint.

该接口用于创建币安礼品卡。

使用前请确保：
  * 您已拥有币安账户
  * 您已通过 KYB
  * 您的币安现货钱包中有足够余额（礼品卡金额与手续费）
  * 发起该请求的 API Key 已启用 `Enable Withdrawals` 权限。

Operation ID: `createASingleTokenGiftCard`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| token | string | 是 | The token type contained in the Binance Gift Card<br>币安礼品卡中的数字货币币种<br>例: `BNB` |
| amount | number (float) | 是 | The amount of the token contained in the Binance Gift Card<br>币安礼品卡中的数字货币数量<br>例: `1` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Create a single-token gift card / 创建单币种礼品卡

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  | 例: `000000` |
| message | string |  | 例: `success` |
| data | object |  |  |
| data.referenceNo | string |  | 例: `0033002144060553` |
| data.code | string |  | 例: `6H9EKF5ECCWFBHGE` |
| data.expiredTime | integer (int64) |  | 例: `1727417154000` |
| success | boolean |  | 例: `True` |

## Fetch RSA Public Key (USER_DATA)（获取 RSA 公钥 (USER_DATA)）

`GET /sapi/v1/giftcard/cryptography/rsa-public-key`

This API is for fetching the RSA Public Key.
This RSA Public key will be used to encrypt the card code.

**Please note that the RSA Public key fetched is valid only for the current day.**

此接口用于获取 RSA 公钥。
该公钥可用于加密币安礼品卡兑换码。

**请注意：获取的 RSA 公钥仅在当日有效。**

Operation ID: `fetchRsaPublicKey`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Fetch RSA Public Key / 获取 RSA 公钥

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  | 例: `000000` |
| message | string |  | 例: `success` |
| data | string |  | 例: `MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCXBBVKLAc1GQ5FsIFFqOHrPTox5noBONIKr+IAedTR9FkVxq6e65updEbfdhRNkMOeYIO2i0UylrjGC0X8YSoIszmrVHeV0l06Zh1oJuZos1+7N+WLuz9JvlPaawof3GUakTxYWWCa9+8KIbLKsoKMdfS96VT+8iOXO3quMGKUmQIDAQAB` |
| success | boolean |  | 例: `True` |

## Fetch Token Limit (USER_DATA)（获取货币使用限制 (USER_DATA)）

`GET /sapi/v1/giftcard/buyCode/token-limit`

This API is to help you verify which tokens are available for you to create Stablecoin-Denominated gift cards as
mentioned in section 2 and its’ limitation.

此接口用于查看可用于创建稳定币定值礼品卡的币种及其限制。

Operation ID: `fetchTokenLimit`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| baseToken | query | string | 是 | The token you want to pay, example: BUSD<br>你用来支付的货币，例如：BUSD<br>例: `BUSD` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Fetch Token Limit / 获取币种限额

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  | 例: `000000` |
| message | string |  | 例: `success` |
| data | object[] |  |  |
| data[].coin | string |  | 例: `BNB` |
| data[].fromMin | string |  | 例: `0.01` |
| data[].fromMax | string |  | 例: `1` |
| success | boolean |  | 例: `True` |

## Redeem a Binance Gift Card (USER_DATA)（兑现币安礼品卡 (USER_DATA)）

`POST /sapi/v1/giftcard/redeemCode`

This API is for redeeming a Binance Gift Card. Once redeemed, the coins will be deposited in your Spot wallet.

该接口用于兑现币安礼品卡。兑现成功后，数字货币将存入您的现货钱包。

Operation ID: `redeemABinanceGiftCard`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

### 请求体（application/x-www-form-urlencoded）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string | 是 | Redemption code of Binance Gift Card to be redeemed, supports both Plaintext & Encrypted code.<br>用于赎回的币安礼品卡，支持加密&未加密两种方式<br>例: `6H9EKF5ECCWFBHGE` |
| externalUid | string |  | Each external unique ID represents a unique user on the partner platform. The function helps you to<br>identify the redemption behavior of different users, such as redemption frequency and amount. It<br>also helps risk and limit control of a single account, such as daily limit on redemption volume,<br>frequency, and incorrect number of entries. This will also prevent a single user account reach the<br>partner's daily redemption limits. We strongly recommend you to use this feature and transfer us the<br>User ID of your users if you have different users redeeming Binance Gift Cards on your platform. To<br>protect user data privacy, you may choose to transfer the user id in any desired format (max. 400<br>characters).<br>每个外部用户 ID<br>代表合作伙伴平台上的某个用户。该功能帮助您识别不同用户的兑现行为，例如兑现频次和金额。它还有助于对单个账户进行风险和限额控制，例如设置单个账户每日兑现金额、频次和卡密输错次数的上限。这也将防止单个帐户突破合作伙伴的每日兑现限额从而导致合作伙伴的账户在当日无法继续制码或者兑现。如果您有外部的网站且有不同的用户在您的平台上兑现<br>币安礼品卡，我们强烈建议您使用此功能并将您用户的用户 ID 传输给我们来进行风控。为保护用户的信息安全，您可以选择以任何格式（上限为 400 个字符）传输用户 ID。<br>例: `user-123` |
| recvWindow | integer (int64) |  | 例: `5000` |
| timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client<br>time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Redeem a Binance Gift Card / 兑换币安礼品卡

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  | 例: `000000` |
| message | string |  | 例: `success` |
| data | object |  |  |
| data.referenceNo | string |  | 例: `0033002328060227` |
| data.identityNo | string |  | 例: `10317392647411060736` |
| data.token | string |  | 例: `BNB` |
| data.amount | string |  | 例: `0.00000001` |
| success | boolean |  | 例: `True` |

## Verify Binance Gift Card by Gift Card Number (USER_DATA)（通过礼品卡卡号验证币安礼品卡 (USER_DATA)）

`GET /sapi/v1/giftcard/verify`

This API is for verifying whether the Binance Gift Card is valid or not by entering Gift Card Number.

**Please note that if you enter the wrong Gift Card Number 5 times within an hour, you will no longer be able to
verify any Gift Card Number for that hour.**

此 API 用于通过输入礼品卡卡号来验证币安礼品卡是否有效。
**请注意，如果您在一小时内输入错误的礼品卡卡号 5 次，您将无法在该小时内验证任何礼品卡卡号。**

Operation ID: `verifyBinanceGiftCardByGiftCardNumber`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| referenceNo | query | string | 是 | Enter the Gift Card Number<br>输入礼品卡卡号<br>例: `0033002328060227` |
| recvWindow | query | integer (int64) |  | 例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Verify Binance Gift Card by Gift Card Number / 通过礼品卡卡号验证币安礼品卡

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  | 例: `000000` |
| message | string |  | 例: `success` |
| data | object |  |  |
| data.valid | boolean |  | 例: `True` |
| data.token | string |  | coin<br>币种<br>例: `BNB` |
| data.amount | string |  | amount<br>金额<br>例: `0.00000001` |
| success | boolean |  | 例: `True` |