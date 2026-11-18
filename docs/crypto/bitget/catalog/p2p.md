---
exchange: bitget
source_url: https://www.bitget.com/docs/catalog/p2p
api_type: REST
updated_at: 2026-11-18 19:01:32.391793
---

# P2P

P2P common, advertisement, order management, and account management APIs.

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v3/p2p/balance` — Get Balance
- `GET /api/v3/p2p/ad-list` — Get Ad List
- `GET /api/v3/p2p/exchange-rate` — Get Exchange Rate
- `POST /api/v3/p2p/fee-simulate` — Fee Simulate
- `GET /api/v3/p2p/ad-limit` — Get Ad Limit
- `POST /api/v3/p2p/ad-create` — Create Ad
- `POST /api/v3/p2p/ad-update` — Update Ad
- `POST /api/v3/p2p/ad-operate` — Operate Ad
- `GET /api/v3/p2p/ad-info` — Get Ad Info
- `GET /api/v3/p2p/my-ads` — Get My Ads
- `GET /api/v3/p2p/pending-orders` — Get Pending Orders
- `GET /api/v3/p2p/all-orders` — Get All Orders
- `GET /api/v3/p2p/order-info` — Get Order Info
- `POST /api/v3/p2p/order-pay` — Confirm Payment
- `POST /api/v3/p2p/order-release` — Release Asset
- `GET /api/v3/p2p/user-info` — Get User Info
- `GET /api/v3/p2p/currencies` — Get Currencies
- `GET /api/v3/p2p/pay-method` — Get Pay Methods

## Get Balance

`GET /api/v3/p2p/balance`

Rate limit: 10 times/1s/UID

Permission: UTA P2P (read)

Get the P2P account balance for a specified cryptocurrency, including total, frozen, and available balances.

Operation ID: `getP2pBalance`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| token | query | string | 是 | Currency name |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.token | string |  | Currency |
| data.totalBalance | string |  | Total balance (excluding frozen balance) |
| data.frozenBalance | string |  | Frozen balance |
| data.availableBalance | string |  | Available balance |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "token": "USDT",
    "totalBalance": "10000",
    "frozenBalance": "500",
    "availableBalance": "9500"
  }
}
```

## Get Ad List

`GET /api/v3/p2p/ad-list`

Rate limit: 10/sec/UID

Permission: UTA P2P (read)

Get the list of public P2P advertisements. Only ads in the published (on-shelf) status are returned.

Operation ID: `p2pAdManagementGetAdList`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| token | query | string | 是 | Cryptocurrency, e.g. USDT, USDC |
| fiat | query | string | 是 | Fiat currency, e.g. CNY, USD |
| side | query | string | 是 | Trade direction:<br><br>`buy` buy<br><br>`sell` sell |
| amount | query | string |  | Trade amount in fiat currency, used to filter eligible ads |
| pageNum | query | string | 是 | Page number, starting from 1. |
| limit | query | string | 是 | Number of items per page. Maximum: 10 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].advId | string |  | Ad ID |
| data[].merchantId | string |  | Merchant ID |
| data[].merchantName | string |  | Merchant name |
| data[].token | string |  | Cryptocurrency |
| data[].fiat | string |  | Fiat currency |
| data[].side | string |  | Trade direction:<br><br>`buy` buy<br><br>`sell` sell |
| data[].price | string |  | Ad price in fiat currency |
| data[].minAmount | string |  | Minimum trade amount per order in fiat currency |
| data[].maxAmount | string |  | Maximum trade amount per order in fiat currency |
| data[].quantity | string |  | Remaining tradable quantity in cryptocurrency |
| data[].payMethods | object[] |  | Supported payment methods |
| data[].payMethods[].payMethodId | string |  | Payment method ID |
| data[].payMethods[].payMethodName | string |  | Payment method name |
| data[].completedOrderNum | string |  | Total completed orders |
| data[].completedRate | string |  | Historical completion rate |
| data[].avgReleaseTime | string |  | Average coin release time in minutes |
| data[].createdTime | string |  | Ad creation time (ms timestamp) |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": [
    {
      "advId": "1234567890",
      "merchantId": "9876543210",
      "merchantName": "MerchantA",
      "token": "USDT",
      "fiat": "CNY",
      "side": "buy",
      "price": "7.28",
      "minAmount": "100",
      "maxAmount": "10000",
      "quantity": "500",
      "payMethods": [
        {
          "payMethodId": "1",
          "payMethodName": "Alipay"
        }
      ],
      "completedOrderNum": "1200",
      "completedRate": "0.99",
      "avgReleaseTime": "5",
      "createdTime": "1740000000000"
    }
  ]
}
```

## Get Exchange Rate

`GET /api/v3/p2p/exchange-rate`

Rate limit: 10/sec/UID

Permission: UTA P2P (read)

Get the current P2P exchange rate for a cryptocurrency/fiat currency pair.

Operation ID: `p2pAdManagementGetExchangeRate`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| token | query | string | 是 | Cryptocurrency, e.g. USDT |
| fiat | query | string | 是 | Fiat currency, e.g. CNY |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.rate | string |  | Exchange rate of the currency pair |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "rate": "7.28"
  }
}
```

## Fee Simulate

`POST /api/v3/p2p/fee-simulate`

Rate limit: 10/sec/UID

Permission: UTA P2P (read and write)

Pre-calculate the fee and tax for publishing a P2P advertisement. Use this endpoint before creating an ad to confirm the expected fee details.

Operation ID: `p2pAdManagementFeeSimulate`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| token | query | string | 是 | Cryptocurrency, e.g. USDT |
| fiat | query | string | 是 | Fiat currency, e.g. CNY |
| side | query | string | 是 | Trade direction:<br><br>`buy` buy<br><br>`sell` sell |
| marketType | query | string | 是 | Market type:<br><br>`public` public<br><br>`private` private |
| amount | query | string | 是 | Ad quantity in cryptocurrency |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.feeToken | string |  | Fee currency |
| data.feeAmount | string |  | Fee amount |
| data.taxToken | string |  | Tax currency |
| data.taxAmount | string |  | Tax amount |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "feeToken": "USDT",
    "feeAmount": "0.5",
    "taxToken": "USDT",
    "taxAmount": "0.1"
  }
}
```

## Get Ad Limit

`GET /api/v3/p2p/ad-limit`

Rate limit: 10/sec/UID

Permission: UTA P2P (read)

Get the minimum and maximum quantity limits for publishing a P2P advertisement.

Operation ID: `p2pAdManagementGetAdLimit`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| token | query | string | 是 | Cryptocurrency |
| fiat | query | string | 是 | Fiat currency |
| side | query | string | 是 | Trade direction:<br><br>`buy` buy<br><br>`sell` sell |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.buyMinTokenAmount | string |  | Buy ad - minimum cryptocurrency amount, in USDT |
| data.buyMaxTokenAmount | string |  | Buy ad - maximum cryptocurrency amount, in USDT |
| data.sellMinTokenAmount | string |  | Sell ad - minimum cryptocurrency amount, in USDT |
| data.sellMaxTokenAmount | string |  | Sell ad - maximum cryptocurrency amount, in USDT |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "buyMinTokenAmount": "10",
    "buyMaxTokenAmount": "100000",
    "sellMinTokenAmount": "10",
    "sellMaxTokenAmount": "100000"
  }
}
```

## Create Ad

`POST /api/v3/p2p/ad-create`

Rate limit: 10/sec/UID

Permission: UTA P2P (read and write)

Create a new P2P advertisement. Merchants can set fixed or floating price, payment methods, quantity limits, and trader requirements.

Operation ID: `p2pAdManagementCreateAd`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| token | query | string | 是 | Cryptocurrency, e.g. USDT |
| fiat | query | string | 是 | Fiat currency, e.g. CNY |
| side | query | string | 是 | Trade direction:<br><br>`buy` buy<br><br>`sell` sell |
| priceType | query | string | 是 | Price type:<br><br>`fixed` fixed price<br><br>`floating` floating price |
| price | query | string |  | Fixed unit price<br><br>Required when `priceType=fixed` |
| premium | query | string |  | Premium rate<br><br>Required when `priceType=floating` |
| minAmount | query | string | 是 | Minimum trade amount per order in fiat currency |
| maxAmount | query | string | 是 | Maximum trade amount per order in fiat currency |
| quantity | query | string | 是 | Total ad quantity in cryptocurrency |
| payMethodIds | query | object[] | 是 | Payment method ID array |
| remark | query | string |  | Ad remarks |
| tradeTerms | query | string |  | Trade terms |
| payTimeLimit | query | string | 是 | Payment time limit in minutes: 5, 10 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.advId | string |  | Ad ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "advId": "1234567890"
  }
}
```

## Update Ad

`POST /api/v3/p2p/ad-update`

Rate limit: 3/sec/UID

Permission: UTA P2P (read and write)

Update an existing P2P advertisement. Only the fields provided will be updated.

Operation ID: `p2pAdManagementUpdateAd`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| advId | query | string | 是 | Ad ID |
| priceType | query | string |  | Price type:<br><br>`fixed` fixed price<br><br>`floating` floating price |
| price | query | string |  | Fixed unit price<br><br>Required when `priceType=fixed` |
| premium | query | string |  | Premium rate<br><br>Required when `priceType=floating` |
| minAmount | query | string |  | Minimum trade amount per order in fiat currency |
| maxAmount | query | string |  | Maximum trade amount per order in fiat currency |
| quantity | query | string |  | Total ad quantity in cryptocurrency |
| payMethodIds | query | object[] |  | Payment method ID array |
| payTimeLimit | query | string | 是 | Payment time limit in minutes: 5, 10 |
| remark | query | string |  | Ad remarks |
| tradeTerms | query | string |  | Trade terms |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string |  | Result of the operation |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": "success"
}
```

## Operate Ad

`POST /api/v3/p2p/ad-operate`

Rate limit: 10/sec/UID

Permission: UTA P2P (read and write)

Change the status of a P2P advertisement: publish (on-shelf), delist (off-shelf), or remove.

Operation ID: `p2pAdManagementOperateAd`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| advId | query | string | 是 | Ad ID |
| operation | query | string | 是 | Operation:<br><br>`publish` publish (on-shelf)<br><br>`delist` delist (off-shelf)<br><br>`remove` remove |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string |  | Result of the operation |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": "success"
}
```

## Get Ad Info

`GET /api/v3/p2p/ad-info`

Rate limit: 10/sec/UID

Permission: UTA P2P (read)

Get detailed information for a specific P2P advertisement.

Operation ID: `p2pAdManagementGetAdInfo`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| advId | query | string | 是 | Ad ID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.advId | string |  | Ad ID |
| data.side | string |  | Trade direction:<br><br>`buy` buy<br><br>`sell` sell |
| data.priceType | string |  | Price type:<br><br>`fixed` fixed price<br><br>`floating` floating price |
| data.token | string |  | Cryptocurrency |
| data.fiat | string |  | Fiat currency |
| data.price | string |  | Ad price |
| data.amount | string |  | Ad quantity |
| data.minAmount | string |  | Minimum trade amount per order |
| data.maxAmount | string |  | Maximum trade amount per order |
| data.payDuration | string |  | Payment time limit in minutes |
| data.soldAmount | string |  | Sold quantity |
| data.lastAmount | string |  | Remaining quantity |
| data.premium | string |  | Premium rate |
| data.turnover | string |  | Turnover |
| data.remark | string |  | Ad remarks |
| data.tradeTerm | string |  | Trade terms |
| data.payMethodIds | object[] |  | Payment method ID array |
| data.payMethodIds[].payMethodId | string |  | Payment method ID |
| data.payMethodIds[].userPayMethodId | string |  | User payment method ID |
| data.tokenPrecision | string |  | Cryptocurrency decimal precision |
| data.fiatPrecision | string |  | Fiat currency decimal precision |
| data.market | string |  | Ad market:<br><br>`public` public<br><br>`private` private |
| data.avgTime | string |  | Average processing time (release time for sell / payment time for buy) |
| data.createdTime | string |  | Ad creation time |
| data.updatedTime | string |  | Ad last update time |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "advId": "1234567890",
    "side": "sell",
    "priceType": "fixed",
    "token": "USDT",
    "fiat": "CNY",
    "price": "7.28",
    "amount": "1000",
    "minAmount": "100",
    "maxAmount": "10000",
    "payDuration": "15",
    "soldAmount": "300",
    "lastAmount": "700",
    "premium": "",
    "turnover": "2184",
    "remark": "Fast release",
    "tradeTerm": "",
    "payMethodIds": [
      {
        "payMethodId": "1",
        "userPayMethodId": "101"
      }
    ],
    "tokenPrecision": "2",
    "fiatPrecision": "2",
    "market": "public",
    "avgTime": "5",
    "createdTime": "1740000000000",
    "updatedTime": "1740000001000"
  }
}
```

## Get My Ads

`GET /api/v3/p2p/my-ads`

Rate limit: 10/sec/UID

Permission: UTA P2P (read)

Get the list of advertisements created by the current merchant account, with support for filtering by status, time range, currency, and pagination via cursor.

Operation ID: `p2pAdManagementGetMyAds`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| startTime | query | string |  | Start time. Unix timestamp in milliseconds, e.g. 1597026383085. Maximum query range: 90 days; single query range: 30 days |
| endTime | query | string |  | End time. Unix timestamp in milliseconds, e.g. 1597026383085 |
| limit | query | string |  | Number of items per page. Default: 10 |
| cursor | query | string |  | Cursor ID for pagination. Leave empty for the first request; pass the `nextId` returned in the previous response for subsequent requests |
| advId | query | string |  | Ad ID |
| token | query | string |  | Cryptocurrency |
| fiat | query | string |  | Fiat currency |
| status | query | string |  | Ad status:<br><br>`publish` on-shelf<br><br>`delist` off-shelf<br><br>`remove` removed. Returns all statuses if not provided |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.items | object[] |  | Data list |
| data.items[].advId | string |  | Ad ID |
| data.items[].side | string |  | Trade direction:<br><br>`buy` buy<br><br>`sell` sell |
| data.items[].priceType | string |  | Price type:<br><br>`fixed` fixed price<br><br>`floating` floating price |
| data.items[].token | string |  | Cryptocurrency |
| data.items[].fiat | string |  | Fiat currency |
| data.items[].price | string |  | Ad price |
| data.items[].soldAmount | string |  | Sold quantity |
| data.items[].lastAmount | string |  | Remaining quantity |
| data.items[].payMethods | object[] |  | Payment method array |
| data.items[].payMethods[].payMethodId | string |  | Payment method ID |
| data.items[].status | string |  | Ad status:<br><br>`publish` on-shelf<br><br>`delist` off-shelf<br><br>`remove` removed |
| data.items[].createdTime | string |  | Ad creation time |
| data.items[].updatedTime | string |  | Ad last update time |
| data.nextId | string |  | Next page cursor ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "items": [
      {
        "advId": "1234567890",
        "side": "sell",
        "priceType": "fixed",
        "token": "USDT",
        "fiat": "CNY",
        "price": "7.28",
        "soldAmount": "300",
        "lastAmount": "700",
        "payMethods": [
          {
            "payMethodId": "1"
          }
        ],
        "status": "publish",
        "createdTime": "1740000000000",
        "updatedTime": "1740000001000"
      }
    ],
    "nextId": "1234567889"
  }
}
```

## Get Pending Orders

`GET /api/v3/p2p/pending-orders`

Rate limit: 10/sec/UID

Permission: UTA P2P (read)

Get the list of ongoing P2P orders (pending payment, pending release, or in appeal).

Operation ID: `p2pOrderManagementGetPendingOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string |  | Order ID |
| side | query | string |  | Trade direction:<br><br>`buy` buy<br><br>`sell` sell. Returns all types if not provided |
| startTime | query | string |  | Query start time. Unix timestamp in milliseconds |
| endTime | query | string |  | Query end time. Unix timestamp in milliseconds |
| cursor | query | string |  | Cursor for pagination |
| limit | query | string |  | Number of items per page. Maximum: 10 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.items | object[] |  | Data list |
| data.items[].orderId | string |  | Order ID |
| data.items[].side | string |  | Trade direction:<br><br>`buy` buy<br><br>`sell` sell |
| data.items[].token | string |  | Cryptocurrency |
| data.items[].fiat | string |  | Fiat currency |
| data.items[].price | string |  | Trade unit price |
| data.items[].amount | string |  | Trade amount in fiat currency |
| data.items[].quantity | string |  | Trade quantity in cryptocurrency |
| data.items[].fee | string |  | Fee |
| data.items[].counterparty | string |  | Counterparty nickname |
| data.items[].status | string |  | Order status:<br><br>`pending_payment` pending payment<br><br>`pending_release` pending release<br><br>`in_appeal` in appeal |
| data.items[].createdTime | string |  | Order creation time. Unix timestamp in milliseconds |
| data.items[].updatedTime | string |  | Order last update time. Unix timestamp in milliseconds |
| data.nextId | string |  | Next page cursor ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "items": [
      {
        "orderId": "ORD123456",
        "side": "sell",
        "token": "USDT",
        "fiat": "CNY",
        "price": "7.28",
        "amount": "728",
        "quantity": "100",
        "fee": "0",
        "counterparty": "UserA",
        "status": "pending_release",
        "createdTime": "1740000000000",
        "updatedTime": "1740000001000"
      }
    ],
    "nextId": "ORD123455"
  }
}
```

## Get All Orders

`GET /api/v3/p2p/all-orders`

Rate limit: 10/sec/UID

Permission: UTA P2P (read)

Get the full history of P2P orders with support for filtering by status, time range, and pagination via cursor. Maximum query range is 90 days; single query range cannot exceed 30 days.

Operation ID: `p2pOrderManagementGetAllOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| startTime | query | string |  | Start time. Unix timestamp in milliseconds, e.g. 1597026383085. Maximum query range: 90 days; single query range: 30 days |
| endTime | query | string |  | End time. Unix timestamp in milliseconds, e.g. 1597026383085 |
| limit | query | string |  | Number of items per page. Default: 10 |
| cursor | query | string |  | Cursor ID for pagination. Leave empty for the first request; pass the `nextId` returned in the previous response for subsequent requests |
| orderId | query | string |  | Order ID |
| side | query | string |  | Trade direction:<br><br>`buy` buy<br><br>`sell` sell. Returns all types if not provided |
| status | query | string |  | Order status:<br><br>`pending_payment` pending payment<br><br>`pending_release` pending release<br><br>`completed` completed<br><br>`cancelled` cancelled<br><br>`in_appeal` in appeal. Returns all statuses if not provided |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.items | object[] |  | Data list |
| data.items[].orderId | string |  | Order ID |
| data.items[].side | string |  | Trade direction:<br><br>`buy` buy<br><br>`sell` sell |
| data.items[].token | string |  | Cryptocurrency |
| data.items[].fiat | string |  | Fiat currency |
| data.items[].price | string |  | Trade unit price |
| data.items[].amount | string |  | Trade amount in fiat currency |
| data.items[].quantity | string |  | Trade quantity in cryptocurrency |
| data.items[].fee | string |  | Fee |
| data.items[].counterparty | string |  | Counterparty |
| data.items[].status | string |  | Order status:<br><br>`0` `pending_payment` pending payment<br><br>`1` `pending_release` pending release<br><br>`2` `completed` completed<br><br>`3` `cancelled` cancelled<br><br>`4` `in_appeal` in appeal |
| data.items[].createdTime | string |  | Order creation time. Unix timestamp in milliseconds |
| data.items[].updatedTime | string |  | Order last update time. Unix timestamp in milliseconds |
| data.nextId | string |  | Next page cursor ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "items": [
      {
        "orderId": "ORD123456",
        "side": "sell",
        "token": "USDT",
        "fiat": "CNY",
        "price": "7.28",
        "amount": "728",
        "quantity": "100",
        "fee": "0",
        "counterparty": "UserA",
        "status": "completed",
        "createdTime": "1740000000000",
        "updatedTime": "1740000001000"
      }
    ],
    "nextId": "ORD123455"
  }
}
```

## Get Order Info

`GET /api/v3/p2p/order-info`

Rate limit: 10/sec/UID

Permission: UTA P2P (read)

Get detailed information for a specific P2P order, including payment method details, buyer/seller info, and order status.

Operation ID: `p2pOrderManagementGetOrderInfo`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string | 是 | Order ID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | Order ID |
| data.side | string |  | Trade direction:<br><br>`buy` buy<br><br>`sell` sell |
| data.token | string |  | Cryptocurrency |
| data.fiat | string |  | Fiat currency |
| data.price | string |  | Trade unit price |
| data.quantity | string |  | Trade quantity in cryptocurrency |
| data.amount | string |  | Trade amount in fiat currency |
| data.status | string |  | Order status:<br><br>`pending_payment` pending payment<br><br>`pending_release` pending release<br><br>`completed` completed<br><br>`cancelled` cancelled<br><br>`in_appeal` in appeal |
| data.advId | string |  | Corresponding ad ID |
| data.remark | string |  | Ad remarks |
| data.orderCancelCountdown | string |  | Remaining countdown for order cancellation in seconds |
| data.fee | string |  | Fee |
| data.verifyCapital | string |  | Whether asset-verification order:<br><br>`yes` yes<br><br>`no` no |
| data.payMethodDetail | object |  | Payment method details. Only returned for non-asset-verification orders |
| data.payMethodDetail.payMethodId | string |  | Payment method ID |
| data.payMethodDetail.payMethodName | string |  | Payment method name |
| data.payMethodDetail.payMethodUserName | string |  | Payee username |
| data.payMethodDetail.postscript | string |  | Postscript |
| data.payMethodDetail.payMethodInfo | object[] |  | Payment method info |
| data.payMethodDetail.payMethodInfo[].name | string |  | Field name |
| data.payMethodDetail.payMethodInfo[].type | string |  | Field type:<br><br>`file` image<br><br>`number` number<br><br>`txt` text |
| data.payMethodDetail.payMethodInfo[].value | string |  | Field value |
| data.sellUserInfo | object |  | Seller details |
| data.sellUserInfo.nickName | string |  | Nickname |
| data.sellUserInfo.realName | string |  | Real name |
| data.buyUserInfo | object |  | Buyer details |
| data.buyUserInfo.nickName | string |  | Nickname |
| data.buyUserInfo.realName | string |  | Real name |
| data.createdTime | string |  | Order creation time in ms |
| data.updatedTime | string |  | Order last update time in ms |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "orderId": "ORD123456",
    "side": "sell",
    "token": "USDT",
    "fiat": "CNY",
    "price": "7.28",
    "quantity": "100",
    "amount": "728",
    "status": "pending_release",
    "advId": "1234567890",
    "remark": "Fast release",
    "orderCancelCountdown": "600",
    "fee": "0",
    "verifyCapital": "no",
    "payMethodDetail": {
      "payMethodId": "1",
      "payMethodName": "Alipay",
      "payMethodUserName": "UserA",
      "postscript": "",
      "payMethodInfo": [
        {
          "name": "Account",
          "type": "txt",
          "value": "13800138000"
        }
      ]
    },
    "sellUserInfo": {
      "nickName": "MerchantA",
      "realName": "A"
    },
    "buyUserInfo": {
      "nickName": "UserA",
      "realName": "B"
    },
    "createdTime": "1740000000000",
    "updatedTime": "1740000001000"
  }
}
```

## Confirm Payment

`POST /api/v3/p2p/order-pay`

Rate limit: 10/sec/UID

Permission: UTA P2P (read and write)

Mark a P2P order as paid. Call this endpoint after the buyer has completed the payment to notify the seller.

Operation ID: `p2pOrderManagementConfirmPayment`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string | 是 | Order ID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string |  | Operation result |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": "success"
}
```

## Release Asset

`POST /api/v3/p2p/order-release`

Rate limit: 10/sec/UID

Permission: UTA withdrawal

Confirm coin release for a P2P sell order after verifying the buyer's payment. This endpoint requires the withdrawal IP whitelist to be configured.

Operation ID: `p2pOrderManagementReleaseAsset`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string | 是 | Order ID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string |  | Operation result |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": "success"
}
```

## Get User Info

`GET /api/v3/p2p/user-info`

Rate limit: 10/sec/UID

Permission: UTA P2P (read)

Get the current merchant's P2P account information, including account level, trading statistics, and posting limits.

Operation ID: `p2pUserInfoGetUserInfo`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.uid | string |  | Account ID |
| data.nickName | string |  | Nickname |
| data.accountLevel | string |  | Account level:<br><br>`starter` regular user<br><br>`advanced` advanced merchant<br><br>`master` top merchant |
| data.completedOrderNum | string |  | Total completed orders |
| data.positiveRate | string |  | Positive review rate (decimal, e.g. 0.99 = 99%) |
| data.completedOrderNum30D | string |  | Orders completed in the last 30 days |
| data.completedRate30D | string |  | Completion rate in the last 30 days |
| data.avgPayTime30D | string |  | Average payment time in the last 30 days in minutes |
| data.avgReleaseTime30D | string |  | Average coin release time in the last 30 days in minutes |
| data.equityDetail | object |  | Posting limit details |
| data.equityDetail.maxAdvSellNum | string |  | Maximum number of sell ads |
| data.equityDetail.maxAdvSellLimit | string |  | Maximum sell ad total amount in USDT |
| data.equityDetail.maxAdvBuyNum | string |  | Maximum number of buy ads |
| data.equityDetail.maxAdvBuyLimit | string |  | Maximum buy ad total amount in USDT |
| data.equityDetail.totalMaxPendingOrder | string |  | Maximum total pending orders |
| data.equityDetail.advMaxPendingOrder | string |  | Maximum pending orders per ad |
| data.registerTime | string |  | Registration time. Unix timestamp in milliseconds |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "uid": "1234567890",
    "nickName": "MerchantA",
    "accountLevel": "advanced",
    "completedOrderNum": "500",
    "positiveRate": "0.99",
    "completedOrderNum30D": "50",
    "completedRate30D": "0.98",
    "avgPayTime30D": "3",
    "avgReleaseTime30D": "5",
    "equityDetail": {
      "maxAdvSellNum": "5",
      "maxAdvSellLimit": "100000",
      "maxAdvBuyNum": "5",
      "maxAdvBuyLimit": "100000",
      "totalMaxPendingOrder": "20",
      "advMaxPendingOrder": "5"
    },
    "registerTime": "1600000000000"
  }
}
```

## Get Currencies

`GET /api/v3/p2p/currencies`

Rate limit: 10/sec/UID

Permission: UTA P2P (read)

Get the list of supported cryptocurrencies and fiat currencies for P2P trading, along with their precision, price limits, and available payment methods.

Operation ID: `p2pUserInfoGetCurrencies`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.tokenDetailList | object[] |  | Cryptocurrency list |
| data.tokenDetailList[].token | string |  | Cryptocurrency, e.g. USDT |
| data.tokenDetailList[].precision | string |  | Decimal places |
| data.fiatDetailList | object[] |  | Fiat currency list |
| data.fiatDetailList[].fiat | string |  | Fiat currency, e.g. CNY |
| data.fiatDetailList[].precision | string |  | Decimal places |
| data.fiatDetailList[].floatRateMin | string |  | Minimum floating price ratio |
| data.fiatDetailList[].floatRateMax | string |  | Maximum floating price ratio |
| data.fiatDetailList[].fixedRateMin | string |  | Minimum fixed price ratio |
| data.fiatDetailList[].fixedRateMax | string |  | Maximum fixed price ratio |
| data.fiatDetailList[].adMinLimit | string |  | Ad minimum amount limit |
| data.fiatDetailList[].adMaxLimit | string |  | Ad maximum amount limit |
| data.fiatDetailList[].payMethods | object |  | Payment method info |
| data.fiatDetailList[].payMethods.payMethodName | string |  | Payment method name |
| data.fiatDetailList[].payMethods.iconUrl | string |  | Payment method icon URL |
| data.fiatDetailList[].payMethods.payMethodId | string |  | Payment method ID |
| data.fiatDetailList[].withdrawalLimit | object |  | Withdrawal limits (required for private ads) |
| data.fiatDetailList[].withdrawalLimit.withdrawLimitKey | string |  | Display name, e.g. T+1 |
| data.fiatDetailList[].withdrawalLimit.withdrawLimitValue | string |  | Value, e.g. 1 |
| data.fiatDetailList[].payTimeLimit | integer[] |  | Available payment time limits for ads, e.g. [10, 20] |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "tokenDetailList": [
      {
        "token": "USDT",
        "precision": "2"
      }
    ],
    "fiatDetailList": [
      {
        "fiat": "CNY",
        "precision": "2",
        "floatRateMin": "0.8",
        "floatRateMax": "1.2",
        "fixedRateMin": "6.5",
        "fixedRateMax": "8.5",
        "adMinLimit": "100",
        "adMaxLimit": "1000000",
        "payMethods": {
          "payMethodName": "Alipay",
          "iconUrl": "https://example.com/icon.png",
          "payMethodId": "1"
        },
        "withdrawalLimit": {
          "withdrawLimitKey": "T+1",
          "withdrawLimitValue": "1"
        },
        "payTimeLimit": [
          10,
          20
        ]
      }
    ]
  }
}
```

## Get Pay Methods

`GET /api/v3/p2p/pay-method`

Rate limit: 10/sec/UID

Permission: UTA P2P (read)

Get the payment methods configured for the current merchant account. Use the returned IDs when creating or updating ads.

Operation ID: `p2pUserInfoGetPayMethods`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].payMethodId | string |  | Payment method ID |
| data[].payMethodName | string |  | Payment method name |
| data[].payMethodUserName | string |  | Payee username |
| data[].userPayMethodId | string |  | User payment method ID |
| data[].payMethodInfo | object[] |  | Payment method info |
| data[].payMethodInfo[].name | string |  | Field name |
| data[].payMethodInfo[].type | string |  | Field type:<br><br>`file` image<br><br>`number` number<br><br>`txt` text |
| data[].payMethodInfo[].value | string |  | Field value |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": [
    {
      "payMethodId": "1",
      "payMethodName": "Alipay",
      "payMethodUserName": "UserA",
      "userPayMethodId": "101",
      "payMethodInfo": [
        {
          "name": "Account",
          "type": "txt",
          "value": "13800138000"
        }
      ]
    }
  ]
}
```


---

P2P 公共信息、广告管理、订单管理与账户管理接口。

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v3/p2p/balance` — 查询当前账户余额
- `GET /api/v3/p2p/ad-list` — 获取公开广告列表
- `GET /api/v3/p2p/exchange-rate` — 查询汇率
- `POST /api/v3/p2p/fee-simulate` — 广告前置（手续费试算）
- `GET /api/v3/p2p/ad-limit` — 发布广告查询限额信息
- `POST /api/v3/p2p/ad-create` — 创建广告
- `POST /api/v3/p2p/ad-update` — 更新广告
- `POST /api/v3/p2p/ad-operate` — 变更广告状态
- `GET /api/v3/p2p/ad-info` — 获取广告详情
- `GET /api/v3/p2p/my-ads` — 获取我的广告列表
- `GET /api/v3/p2p/pending-orders` — 获取进行中订单
- `GET /api/v3/p2p/all-orders` — 获取全部订单
- `GET /api/v3/p2p/order-info` — 获取订单详情
- `POST /api/v3/p2p/order-pay` — 标记订单已付款（确认付款）
- `POST /api/v3/p2p/order-release` — 释放资产（确认放币）
- `GET /api/v3/p2p/user-info` — 获取当前商家账户信息
- `GET /api/v3/p2p/currencies` — 获取支持交易的法币/数字币信息
- `GET /api/v3/p2p/pay-method` — 获取当前账户支付方式

## 查询当前账户余额

`GET /api/v3/p2p/balance`

限频: 10次/秒/UID

权限: 统一账户P2P只读权限

查询指定加密货币的P2P账户余额，包括总余额、冻结余额和可用余额。

Operation ID: `getP2pBalance`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| token | query | string | 是 | 币种名称 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.token | string |  | 币种 |
| data.totalBalance | string |  | 余额（不包括冻结余额） |
| data.frozenBalance | string |  | 冻结余额 |
| data.availableBalance | string |  | 可用余额 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "token": "USDT",
    "totalBalance": "10000",
    "frozenBalance": "500",
    "availableBalance": "9500"
  }
}
```

## 获取公开广告列表

`GET /api/v3/p2p/ad-list`

限频: 10次/秒/UID

权限: 统一账户P2P只读权限

获取P2P公开广告列表，仅返回上架状态的广告。

Operation ID: `p2pAdManagementGetAdList`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| token | query | string | 是 | 加密货币，如 USDT、USDC |
| fiat | query | string | 是 | 法币，如 CNY、USD |
| side | query | string | 是 | 交易方向：<br><br>`buy` 买入<br><br>`sell` 卖出 |
| amount | query | string |  | 交易金额，单位为法币，用于过滤可接单广告 |
| pageNum | query | string | 是 | 页码，从1开始 |
| limit | query | string | 是 | 每页条数，最大 10 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].advId | string |  | 广告ID |
| data[].merchantId | string |  | 广告商编号 |
| data[].merchantName | string |  | 广告商名称 |
| data[].token | string |  | 加密货币币种 |
| data[].fiat | string |  | 法币币种 |
| data[].side | string |  | 交易方向：<br><br>`buy` 买入<br><br>`sell` 卖出 |
| data[].price | string |  | 广告价格，单位为法币 |
| data[].minAmount | string |  | 单笔最小交易额，单位为法币 |
| data[].maxAmount | string |  | 单笔最大交易额，单位为法币 |
| data[].quantity | string |  | 剩余可交易数量，单位为加密货币 |
| data[].payMethods | object[] |  | 支持的支付方式列表 |
| data[].payMethods[].payMethodId | string |  | 支付方式ID |
| data[].payMethods[].payMethodName | string |  | 支付方式名称 |
| data[].completedOrderNum | string |  | 累计完成订单数 |
| data[].completedRate | string |  | 历史成交率 |
| data[].avgReleaseTime | string |  | 平均放币时长，单位为分钟 |
| data[].createdTime | string |  | 广告创建时间（ms时间戳） |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": [
    {
      "advId": "1234567890",
      "merchantId": "9876543210",
      "merchantName": "MerchantA",
      "token": "USDT",
      "fiat": "CNY",
      "side": "buy",
      "price": "7.28",
      "minAmount": "100",
      "maxAmount": "10000",
      "quantity": "500",
      "payMethods": [
        {
          "payMethodId": "1",
          "payMethodName": "支付宝"
        }
      ],
      "completedOrderNum": "1200",
      "completedRate": "0.99",
      "avgReleaseTime": "5",
      "createdTime": "1740000000000"
    }
  ]
}
```

## 查询汇率

`GET /api/v3/p2p/exchange-rate`

限频: 10次/秒/UID

权限: 统一账户P2P只读权限

查询指定加密货币与法币的P2P实时汇率。

Operation ID: `p2pAdManagementGetExchangeRate`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| token | query | string | 是 | 加密货币，如 USDT |
| fiat | query | string | 是 | 法币，如 CNY |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.rate | string |  | 币对汇率 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "rate": "7.28"
  }
}
```

## 广告前置（手续费试算）

`POST /api/v3/p2p/fee-simulate`

限频: 10次/秒/UID

权限: 统一账户P2P读写权限

发布广告前预先计算手续费和税费。建议在创建广告前调用此接口以确认预期费用。

Operation ID: `p2pAdManagementFeeSimulate`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| token | query | string | 是 | 加密货币，如 USDT |
| fiat | query | string | 是 | 法币，如 CNY |
| side | query | string | 是 | 交易方向：<br><br>`buy` 买入<br><br>`sell` 卖出 |
| marketType | query | string | 是 | 市场类型：<br><br>`public` 公开<br><br>`private` 私有 |
| amount | query | string | 是 | 发布广告数量，单位为加密货币 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.feeToken | string |  | 手续费币种 |
| data.feeAmount | string |  | 手续费数量 |
| data.taxToken | string |  | 收税币种 |
| data.taxAmount | string |  | 收税数量 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "feeToken": "USDT",
    "feeAmount": "0.5",
    "taxToken": "USDT",
    "taxAmount": "0.1"
  }
}
```

## 发布广告查询限额信息

`GET /api/v3/p2p/ad-limit`

限频: 10次/秒/UID

权限: 统一账户P2P只读权限

查询发布P2P广告的数量最小值和最大值限制。

Operation ID: `p2pAdManagementGetAdLimit`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| token | query | string | 是 | 数字货币 |
| fiat | query | string | 是 | 法币 |
| side | query | string | 是 | 交易方向：<br><br>`buy` 买入<br><br>`sell` 卖出 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.buyMinTokenAmount | string |  | 购买广告-数字币最小限额，单位为USDT |
| data.buyMaxTokenAmount | string |  | 购买广告-数字币最大限额，单位为USDT |
| data.sellMinTokenAmount | string |  | 出售广告-数字币最小限额，单位为USDT |
| data.sellMaxTokenAmount | string |  | 出售广告-数字币最大限额，单位为USDT |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "buyMinTokenAmount": "10",
    "buyMaxTokenAmount": "100000",
    "sellMinTokenAmount": "10",
    "sellMaxTokenAmount": "100000"
  }
}
```

## 创建广告

`POST /api/v3/p2p/ad-create`

限频: 10次/秒/UID

权限: 统一账户P2P读写权限

创建新的P2P广告。商家可设置固定价或浮动价、支付方式、数量限制及交易方要求。

Operation ID: `p2pAdManagementCreateAd`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| token | query | string | 是 | 加密货币，如 USDT |
| fiat | query | string | 是 | 法币，如 CNY |
| side | query | string | 是 | 交易方向：<br><br>`buy` 买入<br><br>`sell` 卖出 |
| priceType | query | string | 是 | 价格类型：<br><br>`fixed` 固定价<br><br>`floating` 浮动价 |
| price | query | string |  | 固定单价<br><br>`priceType=fixed` 时必填 |
| premium | query | string |  | 溢价率<br><br>`priceType=floating` 时必填 |
| minAmount | query | string | 是 | 单笔最小交易额，单位为法币 |
| maxAmount | query | string | 是 | 单笔最大交易额，单位为法币 |
| quantity | query | string | 是 | 挂单总量，单位为加密货币 |
| payMethodIds | query | object[] | 是 | 支付方式ID数组 |
| remark | query | string |  | 广告备注 |
| tradeTerms | query | string |  | 交易条款 |
| payTimeLimit | query | string | 是 | 付款期限，单位为分钟：5、10 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.advId | string |  | 广告ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "advId": "1234567890"
  }
}
```

## 更新广告

`POST /api/v3/p2p/ad-update`

限频: 3次/秒/UID

权限: 统一账户P2P读写权限

更新已有的P2P广告信息，仅传入的字段会被更新。

Operation ID: `p2pAdManagementUpdateAd`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| advId | query | string | 是 | 广告ID |
| priceType | query | string |  | 价格类型：<br><br>`fixed` 固定价<br><br>`floating` 浮动价 |
| price | query | string |  | 固定单价<br><br>`priceType=fixed` 时必填 |
| premium | query | string |  | 溢价率<br><br>`priceType=floating` 时必填 |
| minAmount | query | string |  | 单笔最小交易额，单位为法币 |
| maxAmount | query | string |  | 单笔最大交易额，单位为法币 |
| quantity | query | string |  | 挂单总量，单位为加密货币 |
| payMethodIds | query | object[] |  | 支付方式ID数组 |
| payTimeLimit | query | string | 是 | 付款期限，单位为分钟：5、10 |
| remark | query | string |  | 广告备注 |
| tradeTerms | query | string |  | 交易条款 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string |  | 操作结果 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": "success"
}
```

## 变更广告状态

`POST /api/v3/p2p/ad-operate`

限频: 10次/秒/UID

权限: 统一账户P2P读写权限

变更P2P广告状态：上架、下架或移除。

Operation ID: `p2pAdManagementOperateAd`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| advId | query | string | 是 | 广告ID |
| operation | query | string | 是 | 操作：<br><br>`publish` 上架<br><br>`delist` 下架<br><br>`remove` 移除 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string |  | 操作结果 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": "success"
}
```

## 获取广告详情

`GET /api/v3/p2p/ad-info`

限频: 10次/秒/UID

权限: 统一账户P2P只读权限

获取指定P2P广告的详细信息。

Operation ID: `p2pAdManagementGetAdInfo`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| advId | query | string | 是 | 广告ID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.advId | string |  | 广告ID |
| data.side | string |  | 交易方向：<br><br>`buy` 买入<br><br>`sell` 卖出 |
| data.priceType | string |  | 价格类型：<br><br>`fixed` 固定价<br><br>`floating` 浮动价 |
| data.token | string |  | 数字货币 |
| data.fiat | string |  | 法币 |
| data.price | string |  | 广告价格 |
| data.amount | string |  | 广告数量 |
| data.minAmount | string |  | 单笔最小交易额 |
| data.maxAmount | string |  | 单笔最大交易额 |
| data.payDuration | string |  | 付款时限，单位为分钟 |
| data.soldAmount | string |  | 已售出数量 |
| data.lastAmount | string |  | 剩余数量 |
| data.premium | string |  | 溢价率 |
| data.turnover | string |  | 成交量 |
| data.remark | string |  | 广告备注 |
| data.tradeTerm | string |  | 交易条款 |
| data.payMethodIds | object[] |  | 支付方式ID数组 |
| data.payMethodIds[].payMethodId | string |  | 支付方式ID |
| data.payMethodIds[].userPayMethodId | string |  | 用户支付方式ID |
| data.tokenPrecision | string |  | 数字货币精度 |
| data.fiatPrecision | string |  | 法币精度 |
| data.market | string |  | 广告市场：<br><br>`public` 公开<br><br>`private` 私有 |
| data.avgTime | string |  | 平均用时（出售为放币，购买为付款） |
| data.createdTime | string |  | 广告创建时间 |
| data.updatedTime | string |  | 广告更新时间 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "advId": "1234567890",
    "side": "sell",
    "priceType": "fixed",
    "token": "USDT",
    "fiat": "CNY",
    "price": "7.28",
    "amount": "1000",
    "minAmount": "100",
    "maxAmount": "10000",
    "payDuration": "15",
    "soldAmount": "300",
    "lastAmount": "700",
    "premium": "",
    "turnover": "2184",
    "remark": "快速放币",
    "tradeTerm": "",
    "payMethodIds": [
      {
        "payMethodId": "1",
        "userPayMethodId": "101"
      }
    ],
    "tokenPrecision": "2",
    "fiatPrecision": "2",
    "market": "public",
    "avgTime": "5",
    "createdTime": "1740000000000",
    "updatedTime": "1740000001000"
  }
}
```

## 获取我的广告列表

`GET /api/v3/p2p/my-ads`

限频: 10次/秒/UID

权限: 统一账户P2P只读权限

获取当前商家账号发布的广告列表，支持按状态、时间范围、币种筛选以及游标分页。

Operation ID: `p2pAdManagementGetMyAds`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| startTime | query | string |  | 开始时间戳，Unix时间戳的毫秒数格式，如 1597026383085。最大查询范围90天，单次查询范围不超过30天 |
| endTime | query | string |  | 结束时间戳，Unix时间戳的毫秒数格式，如 1597026383085 |
| limit | query | string |  | 每页条目数，默认 10 |
| cursor | query | string |  | 游标ID，用于翻页。首次调用不传，后续调用传上次返回的 `nextId` |
| advId | query | string |  | 广告ID |
| token | query | string |  | 加密货币币种 |
| fiat | query | string |  | 法币币种 |
| status | query | string |  | 广告状态：<br><br>`publish` 已上架<br><br>`delist` 已下架<br><br>`remove` 已删除。不传则默认返回全部状态 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.items | object[] |  | 数据集合 |
| data.items[].advId | string |  | 广告ID |
| data.items[].side | string |  | 交易方向：<br><br>`buy` 买入<br><br>`sell` 卖出 |
| data.items[].priceType | string |  | 价格类型：<br><br>`fixed` 固定价<br><br>`floating` 浮动价 |
| data.items[].token | string |  | 数字货币 |
| data.items[].fiat | string |  | 法币 |
| data.items[].price | string |  | 广告价格 |
| data.items[].soldAmount | string |  | 已售出数量 |
| data.items[].lastAmount | string |  | 剩余数量 |
| data.items[].payMethods | object[] |  | 支付方式数组 |
| data.items[].payMethods[].payMethodId | string |  | 支付方式ID |
| data.items[].status | string |  | 广告状态：<br><br>`publish` 已上架<br><br>`delist` 已下架<br><br>`remove` 已删除 |
| data.items[].createdTime | string |  | 广告创建时间 |
| data.items[].updatedTime | string |  | 广告更新时间 |
| data.nextId | string |  | 下一页标识ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "items": [
      {
        "advId": "1234567890",
        "side": "sell",
        "priceType": "fixed",
        "token": "USDT",
        "fiat": "CNY",
        "price": "7.28",
        "soldAmount": "300",
        "lastAmount": "700",
        "payMethods": [
          {
            "payMethodId": "1"
          }
        ],
        "status": "publish",
        "createdTime": "1740000000000",
        "updatedTime": "1740000001000"
      }
    ],
    "nextId": "1234567889"
  }
}
```

## 获取进行中订单

`GET /api/v3/p2p/pending-orders`

限频规则: 10次/秒/UID

权限: 统一账户P2P只读权限

获取进行中的P2P订单列表（待付款、待放币或申诉中）。

Operation ID: `p2pOrderManagementGetPendingOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string |  | 订单编号 |
| side | query | string |  | 交易方向：<br><br>`buy` 买入<br><br>`sell` 卖出。不传则默认为全部类型 |
| startTime | query | string |  | 查询开始时间，Unix毫秒时间戳 |
| endTime | query | string |  | 查询结束时间，Unix毫秒时间戳 |
| cursor | query | string |  | 游标 |
| limit | query | string |  | 每页条数，最大 10 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.items | object[] |  | 数据集合 |
| data.items[].orderId | string |  | 订单编号 |
| data.items[].side | string |  | 交易方向：<br><br>`buy` 买入<br><br>`sell` 卖出 |
| data.items[].token | string |  | 加密货币币种 |
| data.items[].fiat | string |  | 法币币种 |
| data.items[].price | string |  | 成交单价 |
| data.items[].amount | string |  | 成交金额，单位为法币 |
| data.items[].quantity | string |  | 成交数量，单位为加密货币 |
| data.items[].fee | string |  | 手续费 |
| data.items[].counterparty | string |  | 交易对象昵称 |
| data.items[].status | string |  | 订单状态：<br><br>`pending_payment` 待付款<br><br>`pending_release` 待放币<br><br>`in_appeal` 申诉中 |
| data.items[].createdTime | string |  | 订单创建时间，Unix毫秒时间戳 |
| data.items[].updatedTime | string |  | 订单更新时间，Unix毫秒时间戳 |
| data.nextId | string |  | 下一页标识ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "items": [
      {
        "orderId": "ORD123456",
        "side": "sell",
        "token": "USDT",
        "fiat": "CNY",
        "price": "7.28",
        "amount": "728",
        "quantity": "100",
        "fee": "0",
        "counterparty": "UserA",
        "status": "pending_release",
        "createdTime": "1740000000000",
        "updatedTime": "1740000001000"
      }
    ],
    "nextId": "ORD123455"
  }
}
```

## 获取全部订单

`GET /api/v3/p2p/all-orders`

限频规则: 10次/秒/UID

权限: 统一账户P2P只读权限

获取P2P全部历史订单，支持按状态、时间范围筛选及游标分页。最大查询范围90天，单次查询范围不超过30天。

Operation ID: `p2pOrderManagementGetAllOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| startTime | query | string |  | 开始时间戳，Unix时间戳的毫秒数格式，如 1597026383085。最大查询范围90天，单次查询范围不超过30天 |
| endTime | query | string |  | 结束时间戳，Unix时间戳的毫秒数格式，如 1597026383085 |
| limit | query | string |  | 每页条目数，默认 10 |
| cursor | query | string |  | 游标ID，用于翻页。首次调用不传，后续调用传上次返回的 `nextId` |
| orderId | query | string |  | 订单编号 |
| side | query | string |  | 交易方向：<br><br>`buy` 买入<br><br>`sell` 卖出。不传则默认为全部类型 |
| status | query | string |  | 订单状态：<br><br>`pending_payment` 待付款<br><br>`pending_release` 待放币<br><br>`completed` 已完成<br><br>`cancelled` 已取消<br><br>`in_appeal` 申诉中。不传则默认为全部状态 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.items | object[] |  | 数据集合 |
| data.items[].orderId | string |  | 订单编号 |
| data.items[].side | string |  | 交易方向：<br><br>`buy` 买入<br><br>`sell` 卖出 |
| data.items[].token | string |  | 加密货币币种 |
| data.items[].fiat | string |  | 法币币种 |
| data.items[].price | string |  | 成交单价 |
| data.items[].amount | string |  | 成交金额，单位为法币 |
| data.items[].quantity | string |  | 成交数量，单位为加密货币 |
| data.items[].fee | string |  | 手续费 |
| data.items[].counterparty | string |  | 交易对象 |
| data.items[].status | string |  | 订单状态：<br><br>`0` `pending_payment` 待付款<br><br>`1` `pending_release` 待放币<br><br>`2` `completed` 已完成<br><br>`3` `cancelled` 已取消<br><br>`4` `in_appeal` 申诉中 |
| data.items[].createdTime | string |  | 订单创建时间，Unix毫秒时间戳 |
| data.items[].updatedTime | string |  | 订单更新时间，Unix毫秒时间戳 |
| data.nextId | string |  | 下一页标识ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "items": [
      {
        "orderId": "ORD123456",
        "side": "sell",
        "token": "USDT",
        "fiat": "CNY",
        "price": "7.28",
        "amount": "728",
        "quantity": "100",
        "fee": "0",
        "counterparty": "UserA",
        "status": "completed",
        "createdTime": "1740000000000",
        "updatedTime": "1740000001000"
      }
    ],
    "nextId": "ORD123455"
  }
}
```

## 获取订单详情

`GET /api/v3/p2p/order-info`

限频规则: 10次/秒/UID

权限: 统一账户P2P只读权限

获取指定P2P订单的详细信息，包括支付方式详情、买卖双方信息及订单状态。

Operation ID: `p2pOrderManagementGetOrderInfo`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string | 是 | 订单ID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | 订单ID |
| data.side | string |  | 交易方向：<br><br>`buy` 买<br><br>`sell` 卖 |
| data.token | string |  | 加密货币 |
| data.fiat | string |  | 法币 |
| data.price | string |  | 成交单价 |
| data.quantity | string |  | 成交数量（加密货币） |
| data.amount | string |  | 成交金额（法币） |
| data.status | string |  | 订单状态：<br><br>`pending_payment` 待付款<br><br>`pending_release` 待放币<br><br>`completed` 已完成<br><br>`cancelled` 已取消<br><br>`in_appeal` 申诉中 |
| data.advId | string |  | 对应广告ID |
| data.remark | string |  | 广告备注 |
| data.orderCancelCountdown | string |  | 订单取消倒计时剩余时间，单位为秒 |
| data.fee | string |  | 手续费 |
| data.verifyCapital | string |  | 是否验资订单：<br><br>`yes` 验资单<br><br>`no` 非验资单 |
| data.payMethodDetail | object |  | 支付方式详情，仅非验资订单返回 |
| data.payMethodDetail.payMethodId | string |  | 支付方式ID |
| data.payMethodDetail.payMethodName | string |  | 支付方式名称 |
| data.payMethodDetail.payMethodUserName | string |  | 收款方用户名称 |
| data.payMethodDetail.postscript | string |  | 附言内容 |
| data.payMethodDetail.payMethodInfo | object[] |  | 支付方式信息 |
| data.payMethodDetail.payMethodInfo[].name | string |  | 字段名称 |
| data.payMethodDetail.payMethodInfo[].type | string |  | 字段类型：<br><br>`file` 图片<br><br>`number` 数字<br><br>`txt` 文本 |
| data.payMethodDetail.payMethodInfo[].value | string |  | 字段值 |
| data.sellUserInfo | object |  | 卖家详情 |
| data.sellUserInfo.nickName | string |  | 昵称 |
| data.sellUserInfo.realName | string |  | 真实姓名 |
| data.buyUserInfo | object |  | 买家详情 |
| data.buyUserInfo.nickName | string |  | 昵称 |
| data.buyUserInfo.realName | string |  | 真实姓名 |
| data.createdTime | string |  | 订单创建时间（ms） |
| data.updatedTime | string |  | 最近更新时间（ms） |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "orderId": "ORD123456",
    "side": "sell",
    "token": "USDT",
    "fiat": "CNY",
    "price": "7.28",
    "quantity": "100",
    "amount": "728",
    "status": "pending_release",
    "advId": "1234567890",
    "remark": "快速放币",
    "orderCancelCountdown": "600",
    "fee": "0",
    "verifyCapital": "no",
    "payMethodDetail": {
      "payMethodId": "1",
      "payMethodName": "支付宝",
      "payMethodUserName": "UserA",
      "postscript": "",
      "payMethodInfo": [
        {
          "name": "账号",
          "type": "txt",
          "value": "13800138000"
        }
      ]
    },
    "sellUserInfo": {
      "nickName": "MerchantA",
      "realName": "A"
    },
    "buyUserInfo": {
      "nickName": "UserA",
      "realName": "B"
    },
    "createdTime": "1740000000000",
    "updatedTime": "1740000001000"
  }
}
```

## 标记订单已付款（确认付款）

`POST /api/v3/p2p/order-pay`

限频规则: 10次/秒/UID

权限: 统一账户P2P读写权限

将P2P订单标记为已付款。买方完成付款后调用此接口通知卖方。

Operation ID: `p2pOrderManagementConfirmPayment`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string | 是 | 订单ID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string |  | 操作结果 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": "success"
}
```

## 释放资产（确认放币）

`POST /api/v3/p2p/order-release`

限频规则: 10次/秒/UID

权限: 统一账户提币权限

P2P出售订单中，卖方确认收款后调用此接口释放加密货币给买方。此接口需要配置提币IP白名单。

Operation ID: `p2pOrderManagementReleaseAsset`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string | 是 | 订单ID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string |  | 操作结果 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": "success"
}
```

## 获取当前商家账户信息

`GET /api/v3/p2p/user-info`

限频: 10次/秒/UID

权限: 统一账户P2P只读权限

获取当前商家的P2P账户信息，包括账户等级、交易统计数据和发布权益限制。

Operation ID: `p2pUserInfoGetUserInfo`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.uid | string |  | 账户ID |
| data.nickName | string |  | 昵称 |
| data.accountLevel | string |  | 账户等级：<br><br>`starter` 普通用户<br><br>`advanced` 进阶商家<br><br>`master` 顶级商家 |
| data.completedOrderNum | string |  | 交易总订单数 |
| data.positiveRate | string |  | 好评率，小数形式，如0.99代表99% |
| data.completedOrderNum30D | string |  | 30日成单 |
| data.completedRate30D | string |  | 30日成单率 |
| data.avgPayTime30D | string |  | 30日平均付款时长，单位为分钟 |
| data.avgReleaseTime30D | string |  | 30日平均放币时长，单位为分钟 |
| data.equityDetail | object |  | 权益详情 |
| data.equityDetail.maxAdvSellNum | string |  | 发布出售广告最大数量 |
| data.equityDetail.maxAdvSellLimit | string |  | 发布出售广告最大限额，单位为USDT |
| data.equityDetail.maxAdvBuyNum | string |  | 发布购买广告最大数量 |
| data.equityDetail.maxAdvBuyLimit | string |  | 发布购买广告最大限额，单位为USDT |
| data.equityDetail.totalMaxPendingOrder | string |  | 最大进行中订单数量 |
| data.equityDetail.advMaxPendingOrder | string |  | 单个广告下最大进行中订单数量 |
| data.registerTime | string |  | 注册时间，Unix毫秒时间戳 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "uid": "1234567890",
    "nickName": "MerchantA",
    "accountLevel": "advanced",
    "completedOrderNum": "500",
    "positiveRate": "0.99",
    "completedOrderNum30D": "50",
    "completedRate30D": "0.98",
    "avgPayTime30D": "3",
    "avgReleaseTime30D": "5",
    "equityDetail": {
      "maxAdvSellNum": "5",
      "maxAdvSellLimit": "100000",
      "maxAdvBuyNum": "5",
      "maxAdvBuyLimit": "100000",
      "totalMaxPendingOrder": "20",
      "advMaxPendingOrder": "5"
    },
    "registerTime": "1600000000000"
  }
}
```

## 获取支持交易的法币/数字币信息

`GET /api/v3/p2p/currencies`

限频: 10次/秒/UID

权限: 统一账户P2P只读权限

获取P2P交易支持的加密货币和法币列表，以及精度、价格限制和可用支付方式。

Operation ID: `p2pUserInfoGetCurrencies`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.tokenDetailList | object[] |  | 数字币列表 |
| data.tokenDetailList[].token | string |  | 加密货币，如 USDT |
| data.tokenDetailList[].precision | string |  | 小数位 |
| data.fiatDetailList | object[] |  | 法币列表 |
| data.fiatDetailList[].fiat | string |  | 法币，如 CNY |
| data.fiatDetailList[].precision | string |  | 小数位 |
| data.fiatDetailList[].floatRateMin | string |  | 最小浮动价格比率 |
| data.fiatDetailList[].floatRateMax | string |  | 最大浮动价格比率 |
| data.fiatDetailList[].fixedRateMin | string |  | 最小固定价格比率 |
| data.fiatDetailList[].fixedRateMax | string |  | 最大固定价格比率 |
| data.fiatDetailList[].adMinLimit | string |  | 广告最小限额 |
| data.fiatDetailList[].adMaxLimit | string |  | 广告最大限额 |
| data.fiatDetailList[].payMethods | object |  | 支付方式信息 |
| data.fiatDetailList[].payMethods.payMethodName | string |  | 支付方式名称 |
| data.fiatDetailList[].payMethods.iconUrl | string |  | 支付方式图标 |
| data.fiatDetailList[].payMethods.payMethodId | string |  | 支付方式ID |
| data.fiatDetailList[].withdrawalLimit | object |  | 提现限制（私有广告时需要） |
| data.fiatDetailList[].withdrawalLimit.withdrawLimitKey | string |  | 展示名，如 T+1 |
| data.fiatDetailList[].withdrawalLimit.withdrawLimitValue | string |  | 值，如 1 |
| data.fiatDetailList[].payTimeLimit | integer[] |  | 广告发布可选超时时间，如 [10, 20] |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "tokenDetailList": [
      {
        "token": "USDT",
        "precision": "2"
      }
    ],
    "fiatDetailList": [
      {
        "fiat": "CNY",
        "precision": "2",
        "floatRateMin": "0.8",
        "floatRateMax": "1.2",
        "fixedRateMin": "6.5",
        "fixedRateMax": "8.5",
        "adMinLimit": "100",
        "adMaxLimit": "1000000",
        "payMethods": {
          "payMethodName": "支付宝",
          "iconUrl": "https://example.com/icon.png",
          "payMethodId": "1"
        },
        "withdrawalLimit": {
          "withdrawLimitKey": "T+1",
          "withdrawLimitValue": "1"
        },
        "payTimeLimit": [
          10,
          20
        ]
      }
    ]
  }
}
```

## 获取当前账户支付方式

`GET /api/v3/p2p/pay-method`

限频: 10次/秒/UID

权限: 统一账户P2P只读权限

获取当前商家账号配置的支付方式，创建或更新广告时使用返回的ID。

Operation ID: `p2pUserInfoGetPayMethods`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].payMethodId | string |  | 支付方式ID |
| data[].payMethodName | string |  | 支付方式名称 |
| data[].payMethodUserName | string |  | 收款方用户名称 |
| data[].userPayMethodId | string |  | 用户支付方式ID |
| data[].payMethodInfo | object[] |  | 支付方式信息 |
| data[].payMethodInfo[].name | string |  | 字段名称 |
| data[].payMethodInfo[].type | string |  | 字段类型：<br><br>`file` 图片<br><br>`number` 数字<br><br>`txt` 文本 |
| data[].payMethodInfo[].value | string |  | 字段值 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": [
    {
      "payMethodId": "1",
      "payMethodName": "支付宝",
      "payMethodUserName": "UserA",
      "userPayMethodId": "101",
      "payMethodInfo": [
        {
          "name": "账号",
          "type": "txt",
          "value": "13800138000"
        }
      ]
    }
  ]
}
```