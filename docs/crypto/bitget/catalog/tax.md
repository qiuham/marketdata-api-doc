---
exchange: bitget
source_url: https://www.bitget.com/docs/catalog/tax
api_type: REST
updated_at: 2026-11-19 19:08:08.564979
---

# Tax

Query unified-account tax records for tax reporting.

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v3/tax/records` — Get Unified Account Tax Records

## Get Unified Account Tax Records

`GET /api/v3/tax/records`

Rate limit: 1/sec/UID

Data query range: 366 days

Access requirements: Please use the tax API Key to request. [Creation Portal](https://www.bitget.com/taxes-api).

Operation ID: `taxGetTaxRecords`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| bizType | query | string | 是 | Product type <br><br>`SPOT` Spot trading <br><br>`MARGIN` Margin trading <br><br>`USDT-FUTURES` USDT futures <br><br>`COIN-FUTURES` Coin-M futures <br><br>`USDC-FUTURES` USDC futures <br><br>`OTHER` Other |
| marginType | query | string |  | Margin Type<br><br>`isolated` isolated margin<br><br>`crossed` cross margin<br><br>This field is effective when `category=MARGIN`.<br><br>If not specified, the default is `crossed` (cross margin). |
| coin | query | string |  | Coin name<br><br>If not specified, tax records for all coins will be returned. |
| startTime | query | string | 是 | Start timestamp <br><br>A Unix timestamp in milliseconds e.g.,`1597026383085` |
| endTime | query | string | 是 | End timestamp <br><br>A Unix timestamp in milliseconds e.g.,`1597026383185`<br><br>The time range between `startTime` and `endTime` must not exceed 7 days |
| limit | query | string |  | Limit per page<br><br>Default: `500`. Maximum: `500` |
| cursor | query | string |  | Cursor ID <br><br>Used for pagination. Do not include it for the first query.<br><br>When querying the second page and subsequent data, use the `id` returned from the previous query. The interface will then return the data for the next page. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].id | string |  | Tax record id |
| data[].coin | string |  | Coin name |
| data[].type | string |  | Tax Type <br><br>Refer to the [Enumeration](https://www.bitget.com/api-doc/uta/enum) page for detailed types. |
| data[].amount | string |  | Amount<br><br>The unit is `coin` |
| data[].fee | string |  | Fee <br><br>The unit is `coin` |
| data[].balance | string |  | Balance <br><br>The unit is `coin` |
| data[].ts | string |  | The timestamp that system generated the data<br><br>A Unix millisecond timestamp. |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1763688181556,
  "data": [
    {
      "id": "1375573238088888369",
      "coin": "USDT",
      "type": "ORDER_DEALT_FROZEN_OUT",
      "amount": "-1.9998656",
      "fee": "0",
      "balance": "42.41856383400698",
      "ts": "1763688137552"
    },
    {
      "id": "1375573238088888368",
      "coin": "BGB",
      "type": "ORDER_PLF_FEE_OUT",
      "amount": "-0.0004556178732628",
      "fee": "0",
      "balance": "2.1598531923916739",
      "ts": "1763688137552"
    },
    {
      "id": "1375573238088888367",
      "coin": "BGB",
      "type": "ORDER_DEALT_IN",
      "amount": "0.5696",
      "fee": "0",
      "balance": "2.1603088102649367",
      "ts": "1763688137552"
    }
  ]
}
```


---

查询统一账户税务记录，用于税务申报。

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v3/tax/records` — 获取统一账户税务记录

## 获取统一账户税务记录

`GET /api/v3/tax/records`

限频规则: 1次/秒/UID

数据查询范围： 366天

访问要求：请通过税务API Key访问。[创建入口](https://www.bitget.com/taxes-api)。

Operation ID: `taxGetTaxRecords`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| bizType | query | string | 是 | 产品类型<br><br>`SPOT` 现货交易<br><br>`MARGIN` 杠杆交易<br><br>`USDT-FUTURES` USDT合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约<br><br>`OTHER` 其它 |
| marginType | query | string |  | 杠杆类型<br><br>`isolated`逐仓杠杆<br><br>`crossed`全仓杠杆<br><br>当`category=MARGIN`时，该字段生效<br><br>如不填，默认为`crossed`全仓杠杆 |
| coin | query | string |  | 币种名称<br><br>如不填，则返回全部币种税务记录 |
| startTime | query | string | 是 | 开始时间戳 <br><br>Unix时间戳的毫秒数格式，如 1597026383085 |
| endTime | query | string | 是 | 结束时间戳 <br><br>Unix时间戳的毫秒数格式，如 1597026383085<br><br>`startTime`和`endTime`间隔不超过7天 |
| limit | query | string |  | 每页条目数<br><br>如不填，默认值为500。最大值为500 |
| cursor | query | string |  | 游标ID <br><br>用于翻页，首次查询不传<br><br>查询第二页及后续数据时，取上一次查询返回的id，接口会返回下一页的数据 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].id | string |  | 税务ID |
| data[].coin | string |  | 币种 |
| data[].type | string |  | 税务类型 <br><br>详细类型参考[枚举](https://www.bitget.com/zh-CN/api-doc/uta/enum)页面获取 |
| data[].amount | string |  | 数量<br><br>单位为`coin` |
| data[].fee | string |  | 手续费 <br><br>单位为`coin` |
| data[].balance | string |  | 账户余额 <br><br>单位为`coin` |
| data[].ts | string |  | 该记录产生时间<br><br>Unix毫秒时间戳 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1763688181556,
  "data": [
    {
      "id": "1375573238088888369",
      "coin": "USDT",
      "type": "ORDER_DEALT_FROZEN_OUT",
      "amount": "-1.9998656",
      "fee": "0",
      "balance": "42.41856383400698",
      "ts": "1763688137552"
    },
    {
      "id": "1375573238088888368",
      "coin": "BGB",
      "type": "ORDER_PLF_FEE_OUT",
      "amount": "-0.0004556178732628",
      "fee": "0",
      "balance": "2.1598531923916739",
      "ts": "1763688137552"
    },
    {
      "id": "1375573238088888367",
      "coin": "BGB",
      "type": "ORDER_DEALT_IN",
      "amount": "0.5696",
      "fee": "0",
      "balance": "2.1603088102649367",
      "ts": "1763688137552"
    }
  ]
}
```