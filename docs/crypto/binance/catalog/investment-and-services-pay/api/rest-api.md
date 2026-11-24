---
exchange: binance
source_url: https://developers.binance.com/en/docs/catalog/investment-and-services-pay/api/rest-api
api_type: REST
updated_at: 2026-11-24 18:49:24.782235
---

# Binance Pay REST API

Schema: https://developers.binance.com/en/docs/catalog/investment-and-services-pay/api/rest-api/1.0.0/schema.yaml

Query Binance Pay transaction history.

查询 Binance Pay 交易历史。

版本: 1.0.0

## 服务地址

- `https://api.binance.com`
- `https://api-gcp.binance.com`
- `https://api1.binance.com`
- `https://api2.binance.com`
- `https://api3.binance.com`
- `https://api4.binance.com`

## 接口列表

- `GET /sapi/v1/pay/transactions` — Get Pay Trade History

## Get Pay Trade History（获取Pay交易历史记录）

`GET /sapi/v1/pay/transactions`

Get Pay Trade History

获取Pay交易历史记录

Operation ID: `getPayTradeHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| startTime | query | integer (int64) |  | Start time in milliseconds.<br>开始时间戳（毫秒）。<br>例: `1623319461670` |
| endTime | query | integer (int64) |  | End time in milliseconds.<br>结束时间戳（毫秒）。<br>例: `1641782889000` |
| limit | query | integer (int64) |  | Number of records to return.<br>返回记录数量。<br>默认: `100`<br>例: `100` |
| recvWindow | query | integer (int64) |  | Request validity window in milliseconds.<br>请求有效时间窗口，单位为毫秒。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and<br>is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |

### 响应 200：Get Pay Trade History / 获取 Pay 交易历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  | 例: `000000` |
| message | string |  | 例: `success` |
| data | object[] |  |  |
| data[].orderType | string |  | Order type. Enum: PAY, PAY_REFUND, C2C, CRYPTO_BOX, CRYPTO_BOX_RF, C2C_HOLDING, C2C_HOLDING_RF, PAYOUT, REMITTANCE.<br>交易类型。枚举值：PAY、PAY_REFUND、C2C、CRYPTO_BOX、CRYPTO_BOX_RF、C2C_HOLDING、C2C_HOLDING_RF、PAYOUT、REMITTANCE。<br>例: `C2C` |
| data[].transactionId | string |  | Transaction ID.<br>流水编号。<br>例: `M_P_71505104267788288` |
| data[].transactionTime | integer (int64) |  | Trade timestamp.<br>交易时间戳。<br>例: `1610090460133` |
| data[].amount | string |  | Order amount (up to 8 decimal places). Positive means income; negative means expenditure.<br>订单金额，最多 8 位小数。正数表示收入，负数表示支出。<br>例: `23.72469206` |
| data[].currency | string |  | Order asset.<br>订单币种。<br>例: `BNB` |
| data[].walletType | integer (int64) |  | Main wallet type: 1=funding wallet, 2=spot wallet, 3=fiat wallet, 4 or 6=card payment, 5=earn wallet.<br>主钱包类型：1 资金钱包；2 现货钱包；3 法币钱包；4 或 6 卡支付；5 理财钱包。<br>例: `1` |
| data[].walletTypes | integer (int64)[] |  | Array format of wallet types. Multiple values may appear for combined payments.<br>钱包类型数组。使用组合支付时会有多个值。 |
| data[].fundsDetail | object[] |  | Funds usage details.<br>使用资金明细。 |
| data[].fundsDetail[].currency | string |  | Asset.<br>使用资金币种。<br>例: `USDT` |
| data[].fundsDetail[].amount | string |  | Asset amount.<br>使用资金金额（正值）。<br>例: `1.2` |
| data[].fundsDetail[].walletAssetCost | object |  | Asset cost details per wallet type. Keys are wallet type IDs (e.g. "1", "2"), values are cost amounts.<br>每个钱包类型的资金支出明细。键为钱包类型 ID（如 "1"、"2"），值为支出金额。 |
| data[].payerInfo | object |  |  |
| data[].payerInfo.name | string |  | Nickname or merchant name.<br>个人昵称或商户名称。<br>例: `Jack` |
| data[].payerInfo.type | string |  | Account type: USER for personal, MERCHANT for merchant.<br>账户类型，USER 表示个人账户，MERCHANT 表示商家账户。<br>例: `USER` |
| data[].payerInfo.binanceId | string |  | Binance UID.<br>Binance 用户 ID。<br>例: `12345678` |
| data[].receiverInfo | object |  |  |
| data[].receiverInfo.name | string |  | Nickname or merchant name.<br>个人昵称或商户名称。<br>例: `Alan` |
| data[].receiverInfo.type | string |  | Account type: USER for personal, MERCHANT for merchant.<br>账户类型，USER 表示个人账户，MERCHANT 表示商家账户。<br>例: `MERCHANT` |
| data[].receiverInfo.email | string |  | Email.<br>邮箱。<br>例: `alan@binance.com` |
| data[].receiverInfo.binanceId | string |  | Binance UID.<br>Binance 用户 ID。<br>例: `34355667` |
| data[].receiverInfo.accountId | string |  | Binance Pay ID.<br>Binance Pay 账户 ID。<br>例: `21326891` |
| data[].receiverInfo.countryCode | string |  | International area code.<br>国际区号。<br>例: `1` |
| data[].receiverInfo.phoneNumber | string |  | Phone number.<br>手机号。<br>例: `8057651210` |
| data[].receiverInfo.mobileCode | string |  | Country code.<br>国家代码。<br>例: `US` |
| data[].receiverInfo.extend | object |  | Extension fields.<br>扩展字段。 |
| data[].receiverInfo.extend.institutionName | string |  | Bank name or digital wallet name.<br>银行名称或电子钱包名称。<br>例: `` |
| data[].receiverInfo.extend.cardNumber | string |  | Card number.<br>银行卡号。<br>例: `` |
| data[].receiverInfo.extend.digitalWalletId | string |  | Digital wallet ID.<br>电子钱包 ID。<br>例: `` |
| success | boolean |  | 例: `True` |