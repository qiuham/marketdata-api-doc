---
exchange: binance
source_url: https://developers.binance.com/en/docs/catalog/investment-and-services-c2-c/api/rest-api
api_type: REST
updated_at: 2026-11-26 18:50:08.243757
---

# C2C REST API

Schema: https://developers.binance.com/en/docs/catalog/investment-and-services-c2-c/api/rest-api/1.0.0/schema.yaml

Query fiat transaction history via the C2C REST API.

通过 C2C REST API 查询法币交易历史记录。

版本: 1.0.0

## 服务地址

- `https://api.binance.com`
- `https://api-gcp.binance.com`
- `https://api1.binance.com`
- `https://api2.binance.com`
- `https://api3.binance.com`
- `https://api4.binance.com`

## 接口列表

- `GET /sapi/v1/c2c/orderMatch/listUserOrderHistory` — Get C2C Trade History (USER_DATA)

## Get C2C Trade History (USER_DATA)（获取C2C交易历史记录 (USER_DATA)）

`GET /sapi/v1/c2c/orderMatch/listUserOrderHistory`

Get C2C (also known as P2P) trade history, including both buy and sell orders.

获取C2C（即P2P）交易历史记录，包含买入和卖出订单。

Operation ID: `getC2CTradeHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| tradeType | query | string |  | Trade side filter<br>交易方向筛选<br>枚举: `BUY`, `SELL`<br>例: `BUY` |
| startTimestamp | query | integer (int64) |  | 例: `1770736694138` |
| endTimestamp | query | integer (int64) |  | 例: `1770736694138` |
| page | query | integer (int64) |  | Page number<br>页码<br>默认: `1`<br>例: `1` |
| rows | query | integer (int64) |  | Number of records per page<br>每页记录数<br>默认: `100`<br>例: `100` |

### 响应 200：Get C2C Trade History / 获取 C2C 交易历史记录

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  | API response code. "000000" indicates success.<br>API 响应码。"000000" 表示成功。<br>例: `000000` |
| message | string |  | Response message.<br>响应消息。<br>例: `success` |
| data | object[] |  |  |
| data[].orderNumber | string |  | Order Number<br>例: `20219644646554779648` |
| data[].advNo | string |  | Adv Number<br>例: `11218246497340923904` |
| data[].tradeType | string |  | "BUY" or "SELL"<br>例: `SELL` |
| data[].asset | string |  | Crypto asset<br>例: `BUSD` |
| data[].fiat | string |  | Fiat currency<br>例: `CNY` |
| data[].fiatSymbol | string |  | Fiat currency symbol<br>例: `￥` |
| data[].amount | string |  | Quantity (in Crypto)<br>数量（以数字货币计）<br>例: `5000.00000000` |
| data[].totalPrice | string |  | Total order amount in fiat<br>订单总金额（法币）<br>例: `33400.00000000` |
| data[].unitPrice | string |  | Unit Price (in Fiat)<br>单价（以法币计）<br>例: `6.68` |
| data[].orderStatus | string |  | PENDING, TRADING, BUYER_PAYED, DISTRIBUTING, COMPLETED, IN_APPEAL, CANCELLED, CANCELLED_BY_SYSTEM<br>枚举: `PENDING`, `TRADING`, `BUYER_PAYED`, `DISTRIBUTING`, `COMPLETED`, `IN_APPEAL`, `CANCELLED`, `CANCELLED_BY_SYSTEM`<br>例: `COMPLETED` |
| data[].createTime | integer (int64) |  | Order creation timestamp in milliseconds<br>订单创建时间戳（毫秒）<br>例: `1619361369000` |
| data[].commission | string |  | Transaction Fee (in Crypto)<br>交易手续费（以数字货币计）<br>例: `0` |
| data[].counterPartNickName | string |  | Counterparty nickname<br>交易对手昵称<br>例: `阿涛❤***` |
| data[].payMethodName | string |  | Identifier of the payment method<br>付款方式标识<br>例: `BANK` |
| data[].additionalKycVerify | integer (int64) |  | KYC verification status. 0: not required, 1: not verified, 2: verified<br>KYC 验证状态。0: 不需要, 1: 未验证, 2: 已验证<br>例: `0` |
| data[].takerCommissionRate | string |  | Taker commission rate<br>Taker 手续费率<br>例: `0` |
| data[].takerCommission | string |  | Taker commission amount<br>Taker 手续费金额<br>例: `0` |
| data[].takerAmount | string |  | Taker trade amount<br>Taker 交易金额<br>例: `343.4` |
| data[].advertisementRole | string |  | 枚举: `MAKER`, `TAKER`<br>例: `TAKER` |
| total | integer (int64) |  | Total number of records<br>记录总数<br>例: `1` |
| success | boolean |  | Whether request is successful<br>请求是否成功<br>例: `True` |