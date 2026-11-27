---
exchange: bitget
source_url: https://www.bitget.com/docs/catalog/earn
api_type: REST
updated_at: 2026-11-27 19:02:51.995125
---

# Earn

On-chain Elite, Cash+, Simple Earn and SharkFin product endpoints for subscribing, redeeming, and querying assets, positions and history.

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v3/earn/elite-product` — Get Elite Product
- `GET /api/v3/earn/elite-subscribe-info` — Get Elite Subscribe Info
- `POST /api/v3/earn/elite-subscribe` — Elite Subscribe
- `GET /api/v3/earn/elite-subscribe-result` — Get Elite Subscribe Result
- `GET /api/v3/earn/elite-redeem-info` — Get Redeem Info
- `POST /api/v3/earn/elite-redeem` — Elite Redeem
- `GET /api/v3/earn/elite-assets` — Get Elite Assets
- `GET /api/v3/earn/elite-records` — Get Elite Records
- `GET /api/v3/earn/cashplus/subscribe-info` — Get Cash+ Subscribe Info
- `POST /api/v3/earn/cashplus/subscribe` — Cash+ Subscribe
- `GET /api/v3/earn/cashplus/subscribe-result` — Get Cash+ Subscribe Result
- `GET /api/v3/earn/cashplus/redeem-info` — Get Cash+ Redeem Info
- `POST /api/v3/earn/cashplus/redeem` — Cash+ Redeem
- `GET /api/v3/earn/cashplus/redeem-result` — Get Cash+ Redeem Result
- `GET /api/v3/earn/cashplus/positions` — Get Cash+ Positions
- `GET /api/v3/earn/cashplus/history-orders` — Get Cash+ History Orders
- `GET /api/v3/earn/savings/product` — Get Simple Earn Product List
- `GET /api/v3/earn/savings/account` — Simple Earn Account
- `GET /api/v3/earn/savings/assets` — Simple Earn Assets
- `GET /api/v3/earn/savings/records` — Simple Earn Records
- `GET /api/v3/earn/savings/subscribe-info` — Simple Earn Subscription Detail
- `POST /api/v3/earn/savings/subscribe` — Subscribe Simple Earn
- `GET /api/v3/earn/savings/subscribe-result` — Simple Earn Subscription Result
- `POST /api/v3/earn/savings/redeem` — Redeem Simple Earn
- `GET /api/v3/earn/savings/redeem-result` — Simple Earn Redemption Results
- `GET /api/v3/earn/sharkfin/product` — Get Sharkfin Products
- `GET /api/v3/earn/sharkfin/account` — SharkFin Account
- `GET /api/v3/earn/sharkfin/assets` — SharkFin Assets
- `GET /api/v3/earn/sharkfin/records` — SharkFin Records
- `GET /api/v3/earn/sharkfin/subscribe-info` — SharkFin Subscription Detail
- `POST /api/v3/earn/sharkfin/subscribe` — Subscribe SharkFin
- `GET /api/v3/earn/sharkfin/subscribe-result` — SharkFin Subscription Result

## Get Elite Product

`GET /api/v3/earn/elite-product`

Rate limit: 5/sec/UID

Permission: UTA mgt. (read)

Query On-Chain Selected Product List

Operation ID: `getEliteProduct`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].productId | string |  | Product ID |
| data[].coin | string |  | Coin name |
| data[].minApr | string |  | Minimum APR, in percentage format, e.g. 1.50 means 1.5% |
| data[].maxApr | string |  | Maximum APR, in percentage format, e.g. 1.50 means 1.5% |
| data[].subscriptionCoinList | object[] |  | List of subscription coins |
| data[].subscriptionCoinList[].subscriptionCoin | string |  | Subscription coin |
| data[].subscriptionCoinList[].precision | string |  | Subscription precision, positive integer. 1 means 1 decimal place |
| data[].subscriptionCoinList[].feeRate | string |  | Fee rate |
| data[].subscriptionCoinList[].exchangeRate | string |  | Exchange rate, in decimal format |
| data[].sellOut | string |  | Whether sold out: YES Sold out; NO Not sold out |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1774530922891,
  "data": [
    {
      "productId": "1216935633797513220",
      "coin": "BGUSD",
      "minApr": "4.00",
      "maxApr": "4.00",
      "subscriptionCoinList": [
        {
          "subscriptionCoin": "USDC",
          "precision": "8",
          "feeRate": "0",
          "exchangeRate": "1"
        },
        {
          "subscriptionCoin": "USDT",
          "precision": "8",
          "feeRate": "0",
          "exchangeRate": "0.99963927"
        }
      ],
      "sellOut": "NO"
    },
    {
      "productId": "1216935633797513219",
      "coin": "BGBTC",
      "minApr": "0.80",
      "maxApr": "0.80",
      "subscriptionCoinList": [
        {
          "subscriptionCoin": "BTC",
          "precision": "",
          "feeRate": "0",
          "exchangeRate": "1"
        }
      ],
      "sellOut": "NO"
    },
    {
      "productId": "1216935633797513218",
      "coin": "BGSOL",
      "minApr": "5.93",
      "maxApr": "5.93",
      "subscriptionCoinList": [
        {
          "subscriptionCoin": "SOL",
          "precision": "",
          "feeRate": "0",
          "exchangeRate": "1.14251924"
        }
      ],
      "sellOut": "NO"
    }
  ]
}
```

## Get Elite Subscribe Info

`GET /api/v3/earn/elite-subscribe-info`

Rate limit: 5/sec/UID

Permission: UTA mgt. (read)

Query On-Chain Selected Subscription Details

Operation ID: `getEliteSubscribeInfo`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| productId | query | string | 是 | Product ID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.productSubId | string |  | Product sub-ID |
| data.minAmount | string |  | Minimum subscription amount |
| data.remainQuota | string |  | Remaining subscription quota |
| data.exchangeRate | string |  | Exchange rate, only applicable to BGBTC / BGSOL |
| data.productCoin | string |  | Product coin |
| data.interestTime | string |  | Interest accrual start time in Unix milliseconds; only applicable to BGUSD / BGBTC |
| data.settleTime | string |  | Interest distribution time in Unix milliseconds; only applicable to BGUSD / BGBTC |
| data.precision | string |  | Subscription yield precision, positive integer. 1 means 1 decimal place |
| data.feeRate | string |  | Fee rate |
| data.subscriptionCoinList | object[] |  | List of subscription coins, only applicable to BGUSD |
| data.subscriptionCoinList[].subscriptionCoin | string |  | Subscription coin |
| data.subscriptionCoinList[].remainQuota | string |  | Remaining subscription quota |
| data.subscriptionCoinList[].precision | string |  | Subscription precision, positive integer. 1 means 1 decimal place |
| data.subscriptionCoinList[].feeRate | string |  | Fee rate |
| data.subscriptionCoinList[].exchangeRate | string |  | Exchange rate |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1774532838451,
  "data": {
    "productSubId": "1216935633814290435",
    "minAmount": "0.00000001",
    "remainQuota": "24995.76563944",
    "exchangeRate": "",
    "productCoin": "BGUSD",
    "interestTime": "1774540800000",
    "settleTime": "1774656000000",
    "precision": "8",
    "feeRate": "",
    "subscriptionCoinList": [
      {
        "subscriptionCoin": "USDC",
        "precision": "8",
        "feeRate": "0",
        "exchangeRate": "1",
        "remainQuota": "24995.76563944",
        "minAmount": "0.1"
      },
      {
        "subscriptionCoin": "USDT",
        "precision": "8",
        "feeRate": "0",
        "exchangeRate": "0.99979509",
        "remainQuota": "24995.76563944",
        "minAmount": "10"
      }
    ]
  }
}
```

## Elite Subscribe

`POST /api/v3/earn/elite-subscribe`

Rate limit: 5/sec/UID

Permission: UTA mgt. (read & write)

Perform On-Chain Selected Product Subscription

Operation ID: `subscribeElite`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| productSubId | query | string | 是 | Product sub-ID |
| amount | query | string | 是 | Subscription amount |
| coin | query | string |  | Subscription coin.<br><br>Required when subscribing to BGUSD. Can be USDT or USDC;<br><br>classic accounts support subscription with USDT/USDC; unified accounts only support subscription with USDC |
| paymentAccount | query | string |  | Debit account:<br><br>`spot` Funding account;<br><br>`unified` Unified account (supported only in unified account mode);<br><br>if not provided, the default is the funding account |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | Subscription Order ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1774534443629,
  "data": {
    "orderId": "142102777777777777"
  }
}
```

## Get Elite Subscribe Result

`GET /api/v3/earn/elite-subscribe-result`

Rate limit: 5/sec/UID

Permission: UTA mgt. (read)

Query On-Chain Selected Subscription Result

Operation ID: `getEliteSubscribeResult`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string | 是 | Subscription order ID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.result | string |  | Subscription result:<br><br>`settled` Subscription successful;<br><br>`pending` Subscription in progress;<br><br>`rejected` Subscription failed |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1774535103055,
  "data": {
    "result": "settled"
  }
}
```

## Get Redeem Info

`GET /api/v3/earn/elite-redeem-info`

Rate limit: 5/sec/UID

Permission: UTA mgt. (read)

Query On-Chain Selected Redemption Information

Operation ID: `getRedeemInfo`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| productId | query | string | 是 | Product ID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.productId | string |  | Product ID |
| data.productSubId | string |  | Product sub-ID |
| data.productCoin | string |  | Product coin |
| data.subscriptionCoin | string |  | Subscription coin |
| data.profitCoin | string |  | Profit coin |
| data.exchangeRate | string |  | Exchange rate, used for BGBTC/BGSOL |
| data.totalUnPayInterestAmount | string |  | Total undistributed interest amount |
| data.preSettleApr | string |  | Early settlement APR |
| data.receivedCoin | string |  | Credited coin, used for BGBTC/BGSOL |
| data.unsettledPoints | string |  | Unsettled points, available for BGBTC |
| data.bgusdReceiveCoinList | object[] |  | List of BGUSD credited coins, used for BGUSD |
| data.bgusdReceiveCoinList[].bgusdReceiveCoin | string |  | BGUSD credited coin, used for BGUSD |
| data.bgusdReceiveCoinList[].bgusdExchangeRate | string |  | BGUSD exchange rate, available for BGUSD |
| data.redeemModeList | object[] |  | Redemption mode list |
| data.redeemModeList[].redeemFeeRate | string |  | Redemption fee rate |
| data.redeemModeList[].remainQuota | string |  | Remaining quota |
| data.redeemModeList[].redeemType | string |  | Redemption type:<br><br>`fast` Fast redemption;<br><br>`standard` Standard redemption |
| data.redeemModeList[].redeemScale | string |  | Redemption precision |
| data.redeemModeList[].redeemDelayDate | string |  | Redemption delayed crediting time |
| data.redeemModeList[].minRedeemAmount | string |  | Minimum redemption amount |
| data.redeemModeList[].redeemTime | string |  | Redemption time |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1774536688556,
  "data": {
    "productId": "1216935633797513220",
    "productSubId": "1216935633814290435",
    "productCoin": "BGUSD",
    "subscriptionCoin": "",
    "profitCoin": "",
    "exchangeRate": "",
    "totalUnPayInterestAmount": "",
    "preSettleApr": "",
    "receivedCoin": "",
    "unsettledPoints": "",
    "bgusdReceiveCoinList": [
      {
        "bgusdReceiveCoin": "USDC",
        "bgusdExchangeRate": "1"
      },
      {
        "bgusdReceiveCoin": "USDT",
        "bgusdExchangeRate": "1.00035041"
      }
    ],
    "redeemModeList": [
      {
        "redeemFeeRate": "0.0005",
        "remainQuota": "9999.00000000",
        "redeemType": "fast",
        "redeemScale": "8",
        "redeemDelayDate": "10",
        "minRedeemAmount": "0.00000001",
        "redeemTime": "1774537288495"
      },
      {
        "redeemFeeRate": "0.0005",
        "remainQuota": "10000000.00000000",
        "redeemType": "standard",
        "redeemScale": "8",
        "redeemDelayDate": "3",
        "minRedeemAmount": "0.00000001",
        "redeemTime": "1774795888542"
      }
    ]
  }
}
```

## Elite Redeem

`POST /api/v3/earn/elite-redeem`

Rate limit: 5/sec/UID

Permission: UTA mgt. (read & write)

Perform On-Chain Selected Redemption

Operation ID: `redeemElite`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| productId | query | string | 是 | Product ID |
| productSubId | query | string | 是 | Product sub-ID |
| redeemType | query | string | 是 | Redemption type<br><br>`fast` Fast redemption<br><br>`standard` Standard redemption - BGUSD supports both fast and standard redemption; BGSOL/BGBTC only support standard redemption |
| amount | query | string | 是 | Subscription amount |
| receiveAccount | query | string | 是 | Crediting account type<br><br>`spot` Funding account<br><br>`unified` Unified account (supported only in unified account mode) |
| advancedSettle | query | string |  | Whether to redeem early<br><br>`yes` Yes<br><br>`no` No<br><br>Default value: `no`<br><br>Only applicable to BGBTC |
| coin | query | string |  | Subscription currency - Required for BGUSD |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | Redemption Order ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1774534443629,
  "data": {
    "orderId": "142102777777777777"
  }
}
```

## Get Elite Assets

`GET /api/v3/earn/elite-assets`

Rate limit: 5/sec/UID

Permission: UTA mgt. (read)

Query On-Chain Selected Asset Information

Operation ID: `getEliteAssets`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.resultList | object[] |  | Asset list |
| data.resultList[].productId | string |  | Product ID |
| data.resultList[].productCoin | string |  | Product coin |
| data.resultList[].holdingAmount | string |  | Holdings |
| data.resultList[].usdtHoldingAmount | string |  | Holdings (in USDT equivalent) |
| data.resultList[].exchangeRate | string |  | Exchange rate |
| data.resultList[].apr | string |  | Annualized yield in percentage format, e.g. 4.20 means 4.20%; applicable to BGSOL / BGBTC |
| data.resultList[].minApy | string |  | Minimum APY, only applicable to BGUSD |
| data.resultList[].maxApy | string |  | Maximum APY, only applicable to BGUSD |
| data.resultList[].subscriptionCoin | string |  | Subscription coin |
| data.resultList[].exchangeAmount | string |  | Exchange amount |
| data.resultList[].projectList | object[] |  | Project list, only applicable to BGBTC |
| data.resultList[].projectList[].projectName | string |  | Project name, only applicable to BGBTC |
| data.resultList[].unsettledBGPoints | string |  | Unsettled BG points, only applicable to BGBTC |
| data.resultList[].interestCoin | string |  | Interest distribution coin, only applicable to BGUSD |
| data.resultList[].totalProfit | string |  | Cumulative profit, only applicable to BGUSD |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1774531452270,
  "data": {
    "resultList": [
      {
        "productId": "1216935633797513220",
        "productCoin": "BGUSD",
        "holdingAmount": "3.23436056",
        "usdtHoldingAmount": "3.23553532",
        "exchangeRate": "1",
        "apr": "4.00",
        "subscriptionCoin": "USDC",
        "exchangeAmount": "3.23436056",
        "unsettledBGPoints": "",
        "interestCoin": "BGUSD",
        "totalProfit": "0.16769105"
      }
    ]
  }
}
```

## Get Elite Records

`GET /api/v3/earn/elite-records`

Rate limit: 5/sec/UID

Permission: UTA mgt. (read)

Query On-Chain Selected History

Operation ID: `getEliteRecords`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| startTime | query | string |  | Start timestamp in Unix milliseconds, e.g. 1597026383085;<br><br>the maximum time range supported is three months;<br><br>if not provided, the default end time is three months |
| endTime | query | string |  | End timestamp in Unix milliseconds, e.g. 1597026383085 |
| limit | query | string |  | Number of records to query, default is 20, maximum is 100 |
| cursor | query | string |  | Cursor ID.<br><br>Request paginated content after this ID (updated data); the value passed should be the `endId` from the corresponding API |
| type | query | string | 是 | Record type:<br><br>`subscribe` Subscription;<br><br>`redeem` Redemption;<br><br>`interest` Interest distribution |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.recordList | object[] |  | Record list |
| data.recordList[].recordId | string |  | Record ID |
| data.recordList[].productId | string |  | Product ID |
| data.recordList[].coin | string |  | Coin name |
| data.recordList[].status | string |  | Order status.<br><br>Subscription: `settled` Subscription successful, `pending` Subscription in progress, `rejected` Subscription failed;<br><br>Redemption: `settled` Redemption successful, `pending` Redemption in progress;<br><br>Interest distribution: `settled` Interest distribution successful, `pending` Interest distribution in progress |
| data.recordList[].exchangeRate | string |  | Exchange rate |
| data.recordList[].receivedCoin | string |  | Received coin |
| data.recordList[].receivedAmount | string |  | Received amount |
| data.recordList[].investAmount | string |  | Investment amount |
| data.recordList[].feeRate | string |  | Fee rate |
| data.recordList[].redeemType | string[] |  | Redemption type:<br><br>`fast` Fast redemption;<br><br>`standard` Standard redemption |
| data.recordList[].receivingAccount | string |  | Redemption account:<br><br>`spot` Funding account;<br><br>`unified` Unified account (supported only in unified account mode);<br><br>returned only when `type=redeem` |
| data.recordList[].actualReceivingAccount | string |  | Actual redemption account:<br><br>`spot` Funding account;<br><br>`unified` Unified account (supported only in unified account mode);<br><br>returned only when `type=redeem` |
| data.recordList[].paymentAccount | string[] |  | Payment account:<br><br>`spot` Funding account;<br><br>`unified` Unified account (supported only in unified account mode);<br><br>returned only when `type=subscribe` |
| data.recordList[].settlePoints | string |  | Settled points, returned only for BGBTC when `type=interest` |
| data.recordList[].fee | string |  | Fee, only applicable to `type=redeem` & `type=subscribe` |
| data.recordList[].bizTime | string |  | Business time |
| data.endId | string |  | Cursor ID for next page (the smallest record ID in current page; pass it to `cursor` to query older records) |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1774531930360,
  "data": {
    "recordList": [
      {
        "recordId": "1421055362391416832",
        "productId": "1216935633797513218",
        "coin": "BGSOL",
        "status": "settled",
        "exchangeRate": "0.87525878",
        "receivedCoin": "BGSOL",
        "receivedAmount": "0.00875258",
        "investAmount": "0.01",
        "feeRate": "",
        "redeemType": "",
        "receivingAccount": "",
        "actualReceivingAccount": "",
        "paymentAccount": [
          "spot"
        ],
        "settlePoints": "",
        "fee": "0",
        "bizTime": "1774531930360"
      }
    ],
    "endId": "1421055235278839808"
  }
}
```

## Get Cash+ Subscribe Info

`GET /api/v3/earn/cashplus/subscribe-info`

Rate limit: 10/sec/UID

Permission: UTA mgt. (read)

Query the subscription prerequisites of Cash+, including the annualized rate and the subscribable coin list.

Operation ID: `getCashPlusSubscribeInfo`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.profitSourceCoin | string |  | Coin the profit is sourced from<br/>Currently `USDGO` |
| data.cashPlusApr | string |  | Current Cash+ annualized rate<br/>Expressed as a decimal: `0.04` means 4% |
| data.subscribeCoinList | object[] |  | List of subscribable coins |
| data.subscribeCoinList[].productSubId | string |  | Product sub-ID<br/>Used for Cash+ subscription and redemption |
| data.subscribeCoinList[].coin | string |  | Coin name |
| data.subscribeCoinList[].minAmount | string |  | Minimum subscription amount<br/>Unit: coin |
| data.subscribeCoinList[].conversionRate | string |  | Conversion rate<br/>Expressed as a decimal, default is `1`<br/>Represents how much Cash+ 1 unit of this coin can be converted into |
| data.subscribeCoinList[].subscribeScale | string |  | Subscription precision<br/>Number of decimal places |
| data.subscribeCoinList[].profitScale | string |  | Profit precision<br/>Number of decimal places |
| data.subscribeCoinList[].soldOut | string |  | Whether sold out<br/>`yes` Sold out<br/>`no` Not sold out |
| data.interestTime | string |  | Interest accrual start time, Unix millisecond timestamp |
| data.payInterestTime | string |  | Interest distribution time, Unix millisecond timestamp |
| data.subscribeTime | string |  | Subscription time, Unix millisecond timestamp |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1789368447497,
  "data": {
    "profitSourceCoin": "USDGO",
    "cashPlusApr": "0.04",
    "subscribeCoinList": [
      {
        "productSubId": "1358292433724211201",
        "coin": "USDT",
        "minAmount": "10",
        "conversionRate": "1",
        "subscribeScale": "2",
        "profitScale": "8",
        "soldOut": "no"
      },
      {
        "productSubId": "1358292433724211202",
        "coin": "USDC",
        "minAmount": "10",
        "conversionRate": "1",
        "subscribeScale": "2",
        "profitScale": "8",
        "soldOut": "no"
      }
    ],
    "interestTime": "1789368447497",
    "payInterestTime": "1789454847497",
    "subscribeTime": "1789368447497"
  }
}
```

## Cash+ Subscribe

`POST /api/v3/earn/cashplus/subscribe`

Rate limit: 1/sec/UID

Permission: UTA mgt. (read & write)

Subscribe to Cash+ with the selected coin and amount.

Operation ID: `cashPlusSubscribe`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| productSubId | string | 是 | Product sub-ID<br/>Obtained from `subscribe-info` |
| amount | number | 是 | Subscription amount, in the subscription coin |
| accountType | string |  | Debit account type<br/>`funding` Funding account<br/>`uta` Unified account<br/>`otc` OTC account<br/>Multiple values are supported, separated by commas (for example `funding,uta`). Defaults to the funding account when omitted |
| idempotentNo | string |  | Idempotency ID, used to prevent duplicate submissions |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | Subscription order ID, used to query the subscription result |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1789368447497,
  "data": {
    "orderId": "1483284264811290624"
  }
}
```

## Get Cash+ Subscribe Result

`GET /api/v3/earn/cashplus/subscribe-result`

Rate limit: 10/sec/UID

Permission: UTA mgt. (read)

Query the result of a Cash+ subscription order.

Operation ID: `getCashPlusSubscribeResult`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string | 是 | Order ID returned by the subscription API |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | Subscription order ID |
| data.status | string |  | Subscription order status<br/>`processing` In progress<br/>`success` Subscription successful<br/>`failed` Subscription failed |
| data.coin | string |  | Subscription coin |
| data.amount | string |  | Subscription amount |
| data.subscribeTime | string |  | Subscription time, Unix millisecond timestamp |
| data.interestTime | string |  | Interest accrual start time, Unix millisecond timestamp |
| data.dividendTime | string |  | First interest distribution time, Unix millisecond timestamp |
| data.paymentAccountList | object[] |  | List of payment accounts |
| data.paymentAccountList[].accountType | string |  | Account type<br/>`funding` Funding account<br/>`uta` Unified account<br/>`otc` OTC account |
| data.paymentAccountList[].payAmount | string |  | Amount paid from this account |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1789368447497,
  "data": {
    "orderId": "1483284264811290624",
    "status": "success",
    "coin": "USDT",
    "amount": "100",
    "subscribeTime": "1789368447497",
    "interestTime": "1789368447497",
    "dividendTime": "1789454847497",
    "paymentAccountList": [
      {
        "accountType": "funding",
        "payAmount": "60"
      },
      {
        "accountType": "uta",
        "payAmount": "40"
      }
    ]
  }
}
```

## Get Cash+ Redeem Info

`GET /api/v3/earn/cashplus/redeem-info`

Rate limit: 10/sec/UID

Permission: UTA mgt. (read)

Query the redemption prerequisites of Cash+, including the redeemable coin list and the redeemable position.

Operation ID: `getCashPlusRedeemInfo`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.redeemCoinList | object[] |  | List of coins credited on redemption |
| data.redeemCoinList[].productSubId | string |  | Product sub-ID<br/>Used for Cash+ subscription and redemption |
| data.redeemCoinList[].coin | string |  | Coin name |
| data.redeemCoinList[].conversionRate | string |  | Redemption conversion rate<br/>Represents how much of this coin 1 unit of Cash+ equals |
| data.redeemCoinList[].redeemAvailable | string |  | Redeemable Cash+ position |
| data.redeemCoinList[].redeemMinAmount | string |  | Minimum redemption amount |
| data.redeemCoinList[].redeemScale | string |  | Redemption amount precision, number of decimal places |
| data.redeemCoinList[].redeemTime | string |  | Unlock request time, Unix millisecond timestamp |
| data.redeemCoinList[].receivedTime | string |  | Estimated redemption arrival time, Unix millisecond timestamp |
| data.userRemainingQuota | string |  | Remaining redemption quota of the user for today |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1789368447497,
  "data": {
    "redeemCoinList": [
      {
        "productSubId": "1358292433724211201",
        "coin": "USDT",
        "conversionRate": "1",
        "redeemAvailable": "100.00000000",
        "redeemMinAmount": "0.01",
        "redeemScale": "2",
        "redeemTime": "1789368447497",
        "receivedTime": "1789372047497"
      }
    ],
    "userRemainingQuota": "50000"
  }
}
```

## Cash+ Redeem

`POST /api/v3/earn/cashplus/redeem`

Rate limit: 1/sec/UID

Permission: UTA mgt. (read & write)

Redeem Cash+ into the selected coin.

Operation ID: `cashPlusRedeem`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| productSubId | string | 是 | Product sub-ID |
| amount | string | 是 | Amount of Cash+ to redeem |
| accountType | string |  | Credit account type<br/>`funding` Funding account<br/>`uta` Unified account<br/>Defaults to the funding account when omitted |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | Redemption order ID, used to query the redemption result |
| data.redeemTime | integer (int64) |  | Redemption request time, Unix millisecond timestamp |
| data.receiveTime | integer (int64) |  | Estimated arrival time, Unix millisecond timestamp |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1789368447497,
  "data": {
    "orderId": "1483284264811290624",
    "redeemTime": 1789368447497,
    "receiveTime": 1789368447497
  }
}
```

## Get Cash+ Redeem Result

`GET /api/v3/earn/cashplus/redeem-result`

Rate limit: 10/sec/UID

Permission: UTA mgt. (read)

Query the result of a Cash+ redemption order.

Operation ID: `getCashPlusRedeemResult`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string | 是 | Order ID returned by the redemption API |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | Redemption order ID |
| data.status | string |  | Redemption status<br/>`processing` In progress<br/>`success` Redemption successful<br/>`failed` Redemption failed |
| data.redeemTime | string |  | Redemption request time, Unix millisecond timestamp |
| data.receiveTime | string |  | Estimated arrival time, Unix millisecond timestamp |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1789368447497,
  "data": {
    "orderId": "1483284264811290624",
    "status": "success",
    "redeemTime": "1789368447497",
    "receiveTime": "1789368447497"
  }
}
```

## Get Cash+ Positions

`GET /api/v3/earn/cashplus/positions`

Rate limit: 10/sec/UID

Permission: UTA mgt. (read)

Query the user's Cash+ holding.

Operation ID: `getCashPlusPositions`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.balance | string |  | Cash+ holding<br/>Converted to USD amount |
| data.totalProfit | string |  | Cumulative profit<br/>Converted to USD amount |
| data.yesterdayProfit | string |  | Profit from yesterday<br/>Converted to USD amount |
| data.apr | string |  | Annualized rate of return<br/>A compound annual rate for reference |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1789368447497,
  "data": {
    "balance": "100.00",
    "totalProfit": "0.05",
    "yesterdayProfit": "0.01",
    "apr": "0.04"
  }
}
```

## Get Cash+ History Orders

`GET /api/v3/earn/cashplus/history-orders`

Rate limit: 10/sec/UID

Permission: UTA mgt. (read)

Query the Cash+ history records with cursor-based pagination.

Operation ID: `getCashPlusHistoryOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| startTime | query | string |  | Query start time, Unix millisecond timestamp |
| endTime | query | string |  | Query end time, Unix millisecond timestamp |
| recordType | query | string |  | Record type<br/>`subscribe` Subscription<br/>`redeem` Redemption<br/>`compound_interest` Compound interest<br/>`liquidation_redeem` Liquidation redemption |
| limit | query | string |  | Number of entries per page<br/>Default 20, maximum 100 |
| cursor | query | string |  | Cursor ID<br/>Pass the `nextCursor` returned by the previous page to fetch the next page. Omit it for the first page |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.items | object[] |  | Record list |
| data.items[].recordId | string |  | Record ID |
| data.items[].recordType | string |  | Record type<br/>`subscribe` Subscription<br/>`redeem` Redemption<br/>`compound_interest` Compound interest<br/>`liquidation_redeem` Liquidation redemption |
| data.items[].status | string |  | Record status<br/>`processing` In progress<br/>`success` Successful<br/>`failed` Failed |
| data.items[].amount | string |  | Change amount |
| data.items[].coin | string |  | Coin name |
| data.items[].createdTime | integer (int64) |  | Record creation time, Unix millisecond timestamp |
| data.items[].accountType | string |  | Account type<br/>`funding` Funding account<br/>`uta` Unified account<br/>`otc` OTC account<br/>For a subscription record, this is the debit account<br/>For an interest or redemption record, this is the credit account |
| data.nextCursor | string |  | Cursor ID of the next page |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1789368447497,
  "data": {
    "items": [
      {
        "recordId": "1483284264811290624",
        "recordType": "subscribe",
        "status": "success",
        "amount": "100",
        "coin": "USDT",
        "createdTime": 1789368447497,
        "accountType": "funding"
      }
    ],
    "nextCursor": "1483284264811290623"
  }
}
```

## Get Simple Earn Product List

`GET /api/v3/earn/savings/product`

Rate limit: 10/sec/UID

Get savings product list.

Operation ID: `getSavingsProduct`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string |  | Coin e.g. BTC |
| filter | query | string |  | Filter conditions<br><br>`available` Available for subscription<br><br>`held` Held<br><br>`available_and_held` Available for subscription and held<br><br>`all` Query all including those that have been removed from the shelves |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].productId | string |  | Product id |
| data[].coin | string |  | Simple Earn subscription coin |
| data[].periodType | string |  | Period type<br><br>`flexible` flexible period<br><br>`fixed` fixed period |
| data[].period | string |  | Period<br><br>`flexible` This value is not returned |
| data[].apyType | string |  | Interest rate type<br><br>`single` single interest rate<br><br>`ladder` ladder income |
| data[].advanceRedeem | string |  | Whether early redemption is allowed<br><br>`Yes` allowed<br><br>`No` not allowed |
| data[].settleMethod | string |  | Settlement method<br><br>`daily` daily interest and daily settlement<br><br>`maturity` repayment of principal and interest at maturity |
| data[].apyList | object[] |  | Ladder interest rate information |
| data[].apyList[].rateLevel | string |  | Rate level |
| data[].apyList[].minStepVal | string |  | Ladder minimum amount value |
| data[].apyList[].maxStepVal | string |  | Ladder maximum amount value |
| data[].apyList[].currentApy | string |  | Current tiered annual interest rate |
| data[].status | string |  | Product status<br><br>`not_started` Warming up<br><br>`in_progress` Subscribing<br><br>`paused` Paused<br><br>`completed` Ended<br><br>`sold_out` Sold out<br><br>`off_line` Off line |
| data[].productLevel | string |  | Product level<br><br>`beginner` beginner product<br><br>`normal` normal product<br><br>`VIP` VIP product |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1696747382760,
  "data": [
    {
      "productId": "12313123",
      "coin": "BGB",
      "periodType": "flexible",
      "period": "",
      "apyType": "ladder",
      "advanceRedeem": "",
      "settleMethod": "",
      "apyList": [
        {
          "rateLevel": "0",
          "minStepVal": "0.000000",
          "maxStepVal": "200.000000",
          "currentApy": "6.00"
        },
        {
          "rateLevel": "1",
          "minStepVal": "200.000000",
          "maxStepVal": "5000.000000",
          "currentApy": "50.00"
        }
      ],
      "status": "in_progress",
      "productLevel": "normal"
    }
  ]
}
```

## Simple Earn Account

`GET /api/v3/earn/savings/account`

Rate limit: 10/sec/UID

Get savings account info.

Operation ID: `getSavingsAccount`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.btcAmount | string |  | Estimated total asset value in BTC |
| data.usdtAmount | string |  | Estimated total asset value in USDT |
| data.btc24hEarning | string |  | 24-hour earning in BTC |
| data.usdt24hEarning | string |  | 24-hour earning in USDT |
| data.btcTotalEarning | string |  | Cumulative earning in BTC |
| data.usdtTotalEarning | string |  | Cumulative earning in USDT |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1696748551073,
  "data": {
    "btcAmount": "0.35821314",
    "usdtAmount": "9481.55500000",
    "btc24hEarning": "0.00000009",
    "usdt24hEarning": "0.00263912",
    "btcTotalEarning": "0.00000761",
    "usdtTotalEarning": "0.20145653"
  }
}
```

## Simple Earn Assets

`GET /api/v3/earn/savings/assets`

Rate limit: 10/sec/UID

Get savings assets.

Operation ID: `getSavingsAssets`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| periodType | query | string | 是 | Period type<br><br>`flexible` demand deposit<br><br>`fixed` time deposit |
| startTime | query | string |  | Start timestamp<br><br>(Simple Earn creation time)<br><br>Milliseconds format of timestamp Unix, e.g. 1597026383085<br><br>(The maximum time span supported is three months. The default start time is three months ago if no value is set for the start time.) |
| endTime | query | string |  | End timestamp<br><br>(Simple Earn creation time)<br><br>Milliseconds format of timestamp Unix, e.g. 1597026383085<br><br>(The maximum time span supported is three months. The default end time is now if no value is set for the end time.) |
| limit | query | string |  | Number of queries: Default: 20, maximum: 100. |
| cursor | query | string |  | Cursor ID<br><br>Used for pagination. Omit it on the first call. For subsequent calls, pass in the last `endId` returned by the previous query. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.resultList | object[] |  | Simple Earn assets list |
| data.resultList[].productId | string |  | Product ID |
| data.resultList[].orderId | string |  | assets order ID<br><br>only for `fixed` |
| data.resultList[].productCoin | string |  | Simple Earn subscription coin |
| data.resultList[].interestCoin | string |  | Interest earning coin |
| data.resultList[].periodType | string |  | Period type<br><br>`flexible` flexible current<br><br>`fixed` fixed term |
| data.resultList[].period | string |  | Duration<br><br>`flexible` This value is not returned |
| data.resultList[].holdAmount | string |  | Current subscription size |
| data.resultList[].lastProfit | string |  | Profit in the last day |
| data.resultList[].totalProfit | string |  | Profit in total |
| data.resultList[].holdDays | string |  | Days of holding |
| data.resultList[].status | string |  | Product Status<br><br>`in_holding` In holding |
| data.resultList[].allowRedemption | string |  | Whether early redemption is allowed<br><br>`Yes` allowed<br><br>`No` not allowed |
| data.resultList[].productLevel | string |  | Product level<br><br>`beginner` beginner product<br><br>`normal` normal product<br><br>`VIP` VIP product |
| data.resultList[].apy | object[] |  | Ladder interest rate info |
| data.resultList[].apy[].rateLevel | string |  | Rate level |
| data.resultList[].apy[].minApy | string |  | Minimum APY |
| data.resultList[].apy[].maxApy | string |  | Maximum APY |
| data.resultList[].apy[].currentApy | string |  | Current tiered APY |
| data.endId | string |  | End ID for pagination |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1696748867881,
  "data": {
    "resultList": [
      {
        "productId": "123123123",
        "orderId": "xxxx",
        "productCoin": "BGB",
        "interestCoin": "BGB",
        "periodType": "flexible",
        "period": "",
        "holdAmount": "100.000",
        "lastProfit": "0.01643800",
        "totalProfit": "1.25479000",
        "holdDays": "",
        "status": "in_holding",
        "allowRedemption": "",
        "productLevel": "normal",
        "apy": [
          {
            "rateLevel": "1",
            "minApy": "0.000000",
            "maxApy": "200.000000",
            "currentApy": "6.00"
          }
        ]
      }
    ],
    "endId": "123456789"
  }
}
```

## Simple Earn Records

`GET /api/v3/earn/savings/records`

Rate limit: 10/sec/UID

Get savings records.

Operation ID: `getSavingsRecords`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string |  | Subscribe coin |
| periodType | query | string | 是 | Period type<br><br>`flexible` flexible current<br><br>`fixed` fixed term |
| orderType | query | string |  | Record type<br><br>`subscribe` subscription<br><br>`redeem` redemption<br><br>`pay_interest` interest payment<br><br>`deduction` penalty interest (only supports regular periods) |
| startTime | query | string |  | Start timestamp<br><br>(Copy trade creation time)<br><br>Milliseconds format of timestamp Unix, e.g. 1597026383085<br><br>(The maximum time span supported is three months. The default end time is three months if no value is set for the end time.) |
| endTime | query | string |  | End timestamp<br><br>(Copy trade creation time)<br><br>Milliseconds format of timestamp Unix, e.g. 1597026383085<br><br>(The maximum time span supported is three months. The default start time is three months ago if no value is set for the start time.) |
| limit | query | string |  | Number of queries: Default: 20, maximum: 100. |
| cursor | query | string |  | Cursor ID<br><br>Used for pagination. Omit it on the first call. For subsequent calls, pass in the last `endId` returned by the previous query. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.resultList | object[] |  | Data list |
| data.resultList[].orderId | string |  | Record id |
| data.resultList[].coinName | string |  | Product Subscribe coin |
| data.resultList[].settleCoinName | string |  | Settled coin |
| data.resultList[].productType | string |  | Period type<br><br>`flexible` flexible current<br><br>`fixed` fixed term |
| data.resultList[].period | string |  | Duration<br><br>`flexible` This value is not returned |
| data.resultList[].productLevel | string |  | Product level<br><br>`beginner` beginner product<br><br>`normal` normal product<br><br>`VIP` VIP product |
| data.resultList[].amount | string |  | Subscribe amount |
| data.resultList[].ts | string |  | Subscribe time timestamp |
| data.resultList[].orderType | string |  | Record type<br><br>`subscribe` subscription<br><br>`redeem` redemption<br><br>`pay_interest` interest payment<br><br>`deduction` penalty interest (only supports regular periods) |
| data.endId | string |  | End ID for pagination |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1696749517654,
  "data": {
    "resultList": [
      {
        "orderId": "123123123123",
        "coinName": "BGB",
        "settleCoinName": "BGB",
        "productType": "flexible",
        "period": "",
        "productLevel": "normal",
        "amount": "200.000000",
        "ts": "1695797014392",
        "orderType": "redeem"
      }
    ],
    "endId": "456456456456"
  }
}
```

## Simple Earn Subscription Detail

`GET /api/v3/earn/savings/subscribe-info`

Rate limit: 10/sec/UID

Get subscription detail before subscribe savings.

Operation ID: `getSavingsSubscribeInfo`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| productId | query | string | 是 | Product ID |
| periodType | query | string | 是 | Period type<br><br>`flexible` flexible period<br><br>`fixed` fixed period |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.singleMinAmount | string |  | Minimum limit for a single transaction |
| data.singleMaxAmount | string |  | Maximum limit for a single transaction |
| data.remainingAmount | string |  | Amount held remaing |
| data.subscribePrecision | string |  | Subscription precision |
| data.profitPrecision | string |  | Profit precison |
| data.subscribeTime | string |  | Subscription time, Unix millisecond timestamp |
| data.interestTime | string |  | Interest generation time, Unix millisecond timestamp |
| data.settleTime | string |  | Interest settlement time, Unix millisecond timestamp |
| data.expireTime | string |  | Expiration time, Unix millisecond timestamp |
| data.redeemTime | string |  | Redemption time, Unix millisecond timestamp |
| data.settleMethod | string |  | Settlement method |
| data.apyList | object[] |  | Ladder interest rate info |
| data.apyList[].rateLevel | string |  | Rate level |
| data.apyList[].minStepVal | string |  | Ladder minimum amount value |
| data.apyList[].maxStepVal | string |  | Ladder maximum amount value |
| data.apyList[].currentApy | string |  | Current tiered annual interest rate |
| data.redeemDelay | string |  | The number of days of delay in the redemption's arrival. The return value is D+1, which means the redemption is delayed by one day, and so on. |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1696751519392,
  "data": {
    "singleMinAmount": "10.000000",
    "singleMaxAmount": "2000.000000",
    "remainingAmount": "4899.999990",
    "subscribePrecision": "6",
    "profitPrecision": "6",
    "subscribeTime": "1696751519451",
    "interestTime": "1696780800000",
    "settleTime": "1696867200000",
    "expireTime": "",
    "redeemTime": "",
    "settleMethod": "",
    "apyList": [
      {
        "rateLevel": "0",
        "minStepVal": "0.000000",
        "maxStepVal": "200.000000",
        "currentApy": "6.00"
      },
      {
        "rateLevel": "1",
        "minStepVal": "200.000000",
        "maxStepVal": "5000.000000",
        "currentApy": "50.00"
      }
    ],
    "redeemDelay": ""
  }
}
```

## Subscribe Simple Earn

`POST /api/v3/earn/savings/subscribe`

Rate limit: 10/sec/UID

Subscribe savings.

Operation ID: `savingsSubscribe`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| productId | string | 是 | Product ID |
| periodType | string | 是 | Period type<br><br>`flexible` flexible period<br><br>`fixed` fixed period |
| amount | string | 是 | Subscribe amount |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | Successful subscription order ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1748783837837,
  "data": {
    "orderId": "1313060074239184896"
  }
}
```

## Simple Earn Subscription Result

`GET /api/v3/earn/savings/subscribe-result`

Rate limit: 10/sec/UID

Get savings subscription result.

Operation ID: `getSavingsSubscribeResult`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string | 是 | Order ID |
| periodType | query | string | 是 | Period type<br><br>`flexible` flexible period<br><br>`fixed` fixed period |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.result | string |  | Subscription result<br><br>`success` Success<br><br>`fail` Fail |
| data.msg | string |  | There will be an error message when the result is `fail` |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1696752594890,
  "data": {
    "result": "success",
    "msg": ""
  }
}
```

## Redeem Simple Earn

`POST /api/v3/earn/savings/redeem`

Rate limit: 10/sec/UID

Redeem savings.

The interval of each redeem should be more than 1min, or it would return error.

Operation ID: `savingsRedeem`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| productId | string | 是 | Product ID |
| orderId | string |  | Assets Order ID<br><br>get this for `/assets` orderId |
| periodType | string | 是 | Period type<br><br>`flexible` flexible period<br><br>`fixed` fixed period |
| amount | string | 是 | Subscribe amount |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | Redemption successful order ID |
| data.status | string |  | Order status |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1696751519392,
  "data": {
    "orderId": "123123123",
    "status": "2000.000000"
  }
}
```

## Simple Earn Redemption Results

`GET /api/v3/earn/savings/redeem-result`

Rate limit: 10/sec/UID

Get savings redeem result.

Operation ID: `getSavingsRedeemResult`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string | 是 | Subscription order ID |
| periodType | query | string | 是 | Period type<br><br>`flexible` flexible current<br><br>`fixed` fixed term |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.result | string |  | Redemption result<br><br>`success` Success<br><br>`fail` Fail |
| data.msg | string |  | There will be an error message when the result is `fail` |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1696752594890,
  "data": {
    "result": "success",
    "msg": ""
  }
}
```

## Get Sharkfin Products

`GET /api/v3/earn/sharkfin/product`

Rate limit: 10/sec/UID

Get sharkfin products.

Operation ID: `getSharkfinProduct`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string | 是 | Shark coin |
| limit | query | string |  | Number of queries: Default: 20, maximum: 100. |
| cursor | query | string |  | Cursor ID<br><br>Used for pagination. Omit it on the first call. For subsequent calls, pass in the last `endId` returned by the previous query. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.resultList | object[] |  | Sharkfin product list info |
| data.resultList[].productId | string |  | Product ID |
| data.resultList[].productName | string |  | Sharkfin product name |
| data.resultList[].productCoin | string |  | Sharkfin product coin |
| data.resultList[].subscribeCoin | string |  | Sharkfin Subscribe coin |
| data.resultList[].farmingStartTime | string |  | Start time, Unix millisecond timestamp |
| data.resultList[].farmingEndTime | string |  | End time, Unix millisecond timestamp |
| data.resultList[].lowerRate | string |  | Minimum rate |
| data.resultList[].defaultRate | string |  | Default rate |
| data.resultList[].upperRate | string |  | Maximum rate |
| data.resultList[].period | string |  | Investment period |
| data.resultList[].interestStartTime | string |  | Interest calculation start time |
| data.resultList[].status | string |  | Product status<br><br>`not_started` Warming up<br><br>`in_progress` Subscribing<br><br>`paused` Paused<br><br>`interest_pending` Interest is accruing<br><br>`settle_pending` Pending settlement<br><br>`settled` Settled<br><br>`redeemed` redeemed<br><br>`sold_out` Sold out |
| data.resultList[].minAmount | string |  | Product minimum limit |
| data.resultList[].limitAmount | string |  | Product limit<br><br>If there is no limit, return `unlimited` |
| data.resultList[].soldAmount | string |  | Sold amount |
| data.resultList[].startTime | string |  | Start timestamp<br><br>Milliseconds format of timestamp Unix, e.g. 1597026383085 |
| data.resultList[].endTime | string |  | End timestamp<br><br>Milliseconds format of timestamp Unix, e.g. 1597026383085 |
| data.endId | string |  | End ID for pagination |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1696754489003,
  "data": {
    "resultList": [
      {
        "productId": "1",
        "productName": "USDT/ETH_20231009",
        "productCoin": "ETH",
        "subscribeCoin": "USDT",
        "farmingStartTime": "1696744800000",
        "farmingEndTime": "1696831200000",
        "lowerRate": "7.06",
        "defaultRate": "7",
        "upperRate": "8.8",
        "period": "7",
        "interestStartTime": "1696838400000",
        "status": "in_progress",
        "minAmount": "0.1",
        "limitAmount": "500001.0",
        "soldAmount": "310187.2",
        "endTime": "1696831200000",
        "startTime": "1696744800000"
      }
    ],
    "endId": "1"
  }
}
```

## SharkFin Account

`GET /api/v3/earn/sharkfin/account`

Rate limit: 10/sec/UID

Get sharkfin account info.

Operation ID: `getSharkfinAccount`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.btcSubscribeAmount | string |  | Estimated total asset value in BTC |
| data.usdtSubscribeAmount | string |  | Estimated total asset value in USDT |
| data.btcHistoricalAmount | string |  | 24-hour earning in BTC |
| data.usdtHistoricalAmount | string |  | 24-hour earning in USDT |
| data.btcTotalEarning | string |  | Cumulative earning in BTC |
| data.usdtTotalEarning | string |  | Cumulative earning in USDT |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1696755312297,
  "data": {
    "btcSubscribeAmount": "0.00000000",
    "usdtSubscribeAmount": "0.00",
    "btcHistoricalAmount": "0.00000000",
    "usdtHistoricalAmount": "0.00000000",
    "btcTotalEarning": "0.00000000",
    "usdtTotalEarning": "0.00000000"
  }
}
```

## SharkFin Assets

`GET /api/v3/earn/sharkfin/assets`

Rate limit: 10/sec/UID

Get sharkfin assets.

Operation ID: `getSharkfinAssets`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| status | query | string | 是 | Shark status<br><br>`subscribed` Subscribed(default)<br><br>`settled` Settled |
| startTime | query | string |  | Start timestamp<br><br>(Sharkfin creation time)<br><br>Milliseconds format of timestamp Unix, e.g. 1597026383085<br><br>(The maximum time span supported is three months. The default start time is three months ago if no value is set for the start time.) |
| endTime | query | string |  | End timestamp<br><br>(Sharkfin creation time)<br><br>Milliseconds format of timestamp Unix, e.g. 1597026383085<br><br>(The maximum time span supported is three months. The default end time is now if no value is set for the end time.) |
| limit | query | string |  | Number of queries: Default: 20, maximum: 100. |
| cursor | query | string |  | Cursor ID<br><br>Used for pagination. Omit it on the first call. For subsequent calls, pass in the last `endId` returned by the previous query. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.resultList | object[] |  | Sharkfin product list info |
| data.resultList[].productId | string |  | Product ID |
| data.resultList[].interestStartTime | string |  | Interest accrual start time |
| data.resultList[].interestEndTime | string |  | Interest accrual end time |
| data.resultList[].productCoin | string |  | Product subscription coin |
| data.resultList[].subscribeCoin | string |  | Subscription coin |
| data.resultList[].trend | string |  | Trend<br><br>`up` rise<br><br>`down` fall |
| data.resultList[].settleTime | string |  | Settlement time, Unix millisecond timestamp |
| data.resultList[].interestAmount | string |  | Interest amount |
| data.resultList[].productStatus | string |  | Product status<br><br>`running` Subscription<br><br>`pause` has been suspended<br><br>`wait_interest` is pending<br><br>`wait_settle` is pending settlement<br><br>`settle` has been settled<br><br>`redeem` has been redeemed<br><br>`sell_out` sold out |
| data.endId | string |  | End ID for pagination |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1696756316611,
  "data": {
    "resultList": [
      {
        "productId": "12312313",
        "interestStartTime": "1697199180000",
        "interestEndTime": "1697803980000",
        "productCoin": "BTC",
        "subscribeCoin": "USDT",
        "trend": "up",
        "settleTime": "1697803980000",
        "interestAmount": "",
        "productStatus": "running"
      }
    ],
    "endId": "456456456"
  }
}
```

## SharkFin Records

`GET /api/v3/earn/sharkfin/records`

Rate limit: 10/sec/UID

Get sharkfin records.

Operation ID: `getSharkfinRecords`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string |  | Subscribe coin |
| type | query | string | 是 | Transaction type<br><br>`subscription` subscription<br><br>`redemption` redemption<br><br>`interest` interest payment |
| startTime | query | string |  | Start timestamp<br><br>(Copy trade creation time)<br><br>Milliseconds format of timestamp Unix, e.g. 1597026383085<br><br>(The maximum time span supported is three months. The default start time is three months ago if no value is set for the start time.) |
| endTime | query | string |  | End timestamp<br><br>(Copy trade creation time)<br><br>Milliseconds format of timestamp Unix, e.g. 1597026383085<br><br>(The maximum time span supported is three months. The default end time is now if no value is set for the end time.) |
| limit | query | string |  | Number of queries: Default: 20, maximum: 100. |
| cursor | query | string |  | Cursor ID<br><br>Used for pagination. Omit it on the first call. For subsequent calls, pass in the last `endId` returned by the previous query. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.resultList | object[] |  | Record list |
| data.resultList[].orderId | string |  | RecordId |
| data.resultList[].product | string |  | Sharkfin productName |
| data.resultList[].period | string |  | Investment period |
| data.resultList[].amount | string |  | Subscribe amount |
| data.resultList[].ts | string |  | Create timestamp<br><br>Milliseconds format of timestamp Unix, e.g. 1597026383085 |
| data.resultList[].type | string |  | Transaction type<br><br>`subscription` subscription<br><br>`redemption` redemption<br><br>`interest` interest payment |
| data.endId | string |  | End ID for pagination |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1696757048457,
  "data": {
    "resultList": [
      {
        "orderId": "1",
        "product": "USDT/BTC_20231013",
        "period": "7",
        "amount": "100.00000000",
        "ts": "1696756278760",
        "type": "subscription"
      }
    ],
    "endId": "1"
  }
}
```

## SharkFin Subscription Detail

`GET /api/v3/earn/sharkfin/subscribe-info`

Rate limit: 10/sec/UID

Get subscription detail before subscribe sharkfin.

Operation ID: `getSharkfinSubscribeInfo`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| productId | query | string | 是 | Product ID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.productCoin | string |  | Product coin |
| data.subscribeCoin | string |  | Subscribe coin |
| data.interestTime | string |  | Interest start date in Unix timestamp format (in milliseconds) |
| data.expirationTime | string |  | Settlement time Unix timestamp format in milliseconds |
| data.minPrice | string |  | Minimum price of price range |
| data.currentPrice | string |  | Current price |
| data.maxPrice | string |  | The maximum price of the price range |
| data.minRate | string |  | Minimum rate |
| data.defaultRate | string |  | Default rate |
| data.maxRate | string |  | Maximum rate |
| data.period | string |  | Investment period |
| data.productMinAmount | string |  | Product minimum limit |
| data.availableBalance | string |  | Available Balance |
| data.userAmount | string |  | User quota |
| data.remainingAmount | string |  | Remaining balance |
| data.profitPrecision | string |  | Interest calculation scale |
| data.subscribePrecision | string |  | Subscribe calculation scale |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1696757209022,
  "data": {
    "productCoin": "BTC",
    "subscribeCoin": "USDT",
    "interestTime": "1697199180000",
    "expirationTime": "1697803980000",
    "minPrice": "28000.00",
    "currentPrice": "30211.23",
    "maxPrice": "32000.00",
    "minRate": "5.00",
    "defaultRate": "1.00",
    "maxRate": "20.00",
    "period": "7",
    "productMinAmount": "0.00100000",
    "availableBalance": "788",
    "userAmount": "500.00000000",
    "remainingAmount": "400.00000000",
    "profitPrecision": "8",
    "subscribePrecision": "8"
  }
}
```

## Subscribe SharkFin

`POST /api/v3/earn/sharkfin/subscribe`

Rate limit: 10/sec/UID

Subscribe sharkfin.

Operation ID: `sharkfinSubscribe`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| productId | string | 是 | Product ID |
| amount | string | 是 | Subscription amount |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | Order Id |
| data.status | string |  | Order status |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1696751519392,
  "data": {
    "orderId": "123123123",
    "status": "2000.000000"
  }
}
```

## SharkFin Subscription Result

`GET /api/v3/earn/sharkfin/subscribe-result`

Rate limit: 5/sec/UID

Get sharkfin subscription result.

Operation ID: `getSharkfinSubscribeResult`

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
| data.result | string |  | Is the subscription successful<br><br>`success` Success<br><br>`fail` Fail |
| data.msg | string |  | There will be an error message when the result is `fail` |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1696752594890,
  "data": {
    "result": "success",
    "msg": ""
  }
}
```


---

链上精选、现金宝（Cash+）、简单赚币与鲨鱼鳍理财产品接口，支持申购、赎回与资产/持仓/历史查询。

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v3/earn/elite-product` — 获取链上精选产品列表
- `GET /api/v3/earn/elite-subscribe-info` — 获取链上精选申购详情
- `POST /api/v3/earn/elite-subscribe` — 链上精选申购
- `GET /api/v3/earn/elite-subscribe-result` — 获取链上精选申购结果
- `GET /api/v3/earn/elite-redeem-info` — 获取链上精选赎回信息
- `POST /api/v3/earn/elite-redeem` — 链上精选赎回
- `GET /api/v3/earn/elite-assets` — 获取链上精选资产信息
- `GET /api/v3/earn/elite-records` — 获取链上精选历史记录
- `GET /api/v3/earn/cashplus/subscribe-info` — 获取现金宝申购详情
- `POST /api/v3/earn/cashplus/subscribe` — 现金宝申购
- `GET /api/v3/earn/cashplus/subscribe-result` — 获取现金宝申购结果
- `GET /api/v3/earn/cashplus/redeem-info` — 获取现金宝赎回详情
- `POST /api/v3/earn/cashplus/redeem` — 现金宝赎回
- `GET /api/v3/earn/cashplus/redeem-result` — 获取现金宝赎回结果
- `GET /api/v3/earn/cashplus/positions` — 获取现金宝持仓
- `GET /api/v3/earn/cashplus/history-orders` — 获取现金宝历史订单
- `GET /api/v3/earn/savings/product` — 简单赚币产品列表
- `GET /api/v3/earn/savings/account` — 简单赚币账户信息
- `GET /api/v3/earn/savings/assets` — 简单赚币资产信息
- `GET /api/v3/earn/savings/records` — 简单赚币历史记录
- `GET /api/v3/earn/savings/subscribe-info` — 简单赚币申购详情
- `POST /api/v3/earn/savings/subscribe` — 简单赚币申购
- `GET /api/v3/earn/savings/subscribe-result` — 简单赚币申购结果
- `POST /api/v3/earn/savings/redeem` — 简单赚币赎回
- `GET /api/v3/earn/savings/redeem-result` — 简单赚币赎回结果
- `GET /api/v3/earn/sharkfin/product` — 鲨鱼鳍产品列表
- `GET /api/v3/earn/sharkfin/account` — 鲨鱼鳍账户信息
- `GET /api/v3/earn/sharkfin/assets` — 鲨鱼鳍资产信息
- `GET /api/v3/earn/sharkfin/records` — 鲨鱼鳍历史记录
- `GET /api/v3/earn/sharkfin/subscribe-info` — 鲨鱼鳍申购详情
- `POST /api/v3/earn/sharkfin/subscribe` — 鲨鱼鳍申购
- `GET /api/v3/earn/sharkfin/subscribe-result` — 鲨鱼鳍申购结果

## 获取链上精选产品列表

`GET /api/v3/earn/elite-product`

限频: 5次/s

权限: 统一账户管理 - 只读

查询链上精选产品列表。

Operation ID: `getEliteProduct`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].productId | string |  | 产品ID |
| data[].coin | string |  | 币种名称 |
| data[].minApr | string |  | 最小年化收益，百分比形式，如1.50代表1.5% |
| data[].maxApr | string |  | 最大年化收益，百分比形式，如1.50代表1.5% |
| data[].subscriptionCoinList | object[] |  | 申购币种列表 |
| data[].subscriptionCoinList[].subscriptionCoin | string |  | 申购币种 |
| data[].subscriptionCoinList[].precision | string |  | 申购精度，正整数。1代表精度为1位小数 |
| data[].subscriptionCoinList[].feeRate | string |  | 手续费率 |
| data[].subscriptionCoinList[].exchangeRate | string |  | 兑换率，小数形式 |
| data[].sellOut | string |  | 是否已售罄：YES 已售罄；NO 未售罄 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1774530922891,
  "data": [
    {
      "productId": "1216935633797513220",
      "coin": "BGUSD",
      "minApr": "4.00",
      "maxApr": "4.00",
      "subscriptionCoinList": [
        {
          "subscriptionCoin": "USDC",
          "precision": "8",
          "feeRate": "0",
          "exchangeRate": "1"
        },
        {
          "subscriptionCoin": "USDT",
          "precision": "8",
          "feeRate": "0",
          "exchangeRate": "0.99963927"
        }
      ],
      "sellOut": "NO"
    },
    {
      "productId": "1216935633797513219",
      "coin": "BGBTC",
      "minApr": "0.80",
      "maxApr": "0.80",
      "subscriptionCoinList": [
        {
          "subscriptionCoin": "BTC",
          "precision": "",
          "feeRate": "0",
          "exchangeRate": "1"
        }
      ],
      "sellOut": "NO"
    },
    {
      "productId": "1216935633797513218",
      "coin": "BGSOL",
      "minApr": "5.93",
      "maxApr": "5.93",
      "subscriptionCoinList": [
        {
          "subscriptionCoin": "SOL",
          "precision": "",
          "feeRate": "0",
          "exchangeRate": "1.14251924"
        }
      ],
      "sellOut": "NO"
    }
  ]
}
```

## 获取链上精选申购详情

`GET /api/v3/earn/elite-subscribe-info`

限频: 5次/s

权限: 统一账户管理 - 只读

查询链上精选申购详情。

Operation ID: `getEliteSubscribeInfo`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| productId | query | string | 是 | 产品Id |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.productSubId | string |  | 产品子ID |
| data.minAmount | string |  | 最小申购金额 |
| data.remainQuota | string |  | 剩余申购额度 |
| data.exchangeRate | string |  | 兑换率，仅适用于 BGBTC / BGSOL |
| data.productCoin | string |  | 产品币种 |
| data.interestTime | string |  | 起息时间，Unix毫秒时间戳；仅适用于 BGUSD / BGBTC |
| data.settleTime | string |  | 派息时间，Unix毫秒时间戳；仅适用于 BGUSD / BGBTC |
| data.precision | string |  | 申购收益精度，正整数。1代表精度为1位小数 |
| data.feeRate | string |  | 手续费率 |
| data.subscriptionCoinList | object[] |  | 申购币种列表，仅适用于 BGUSD |
| data.subscriptionCoinList[].subscriptionCoin | string |  | 申购币种 |
| data.subscriptionCoinList[].remainQuota | string |  | 剩余申购额度 |
| data.subscriptionCoinList[].precision | string |  | 申购精度，正整数。1代表精度为1位小数 |
| data.subscriptionCoinList[].feeRate | string |  | 手续费率 |
| data.subscriptionCoinList[].exchangeRate | string |  | 兑换率 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1774532838451,
  "data": {
    "productSubId": "1216935633814290435",
    "minAmount": "0.00000001",
    "remainQuota": "24995.76563944",
    "exchangeRate": "",
    "productCoin": "BGUSD",
    "interestTime": "1774540800000",
    "settleTime": "1774656000000",
    "precision": "8",
    "feeRate": "",
    "subscriptionCoinList": [
      {
        "subscriptionCoin": "USDC",
        "precision": "8",
        "feeRate": "0",
        "exchangeRate": "1",
        "remainQuota": "24995.76563944",
        "minAmount": "0.1"
      },
      {
        "subscriptionCoin": "USDT",
        "precision": "8",
        "feeRate": "0",
        "exchangeRate": "0.99979509",
        "remainQuota": "24995.76563944",
        "minAmount": "10"
      }
    ]
  }
}
```

## 链上精选申购

`POST /api/v3/earn/elite-subscribe`

限频: 5次/s

权限: 统一账户管理 - 读写

进行链上精选产品申购。

Operation ID: `subscribeElite`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| productSubId | query | string | 是 | 产品子Id |
| amount | query | string | 是 | 申购金额 |
| coin | query | string |  | 申购币种<br><br>申购 BGUSD 时必传，可传 USDT 或 USDC；<br><br>经典账户支持 USDT/USDC 申购；<br><br>统一账户仅支持 USDC 申购 |
| paymentAccount | query | string |  | 扣款账户<br><br>`spot` 资金账户；<br><br>`unified` 统一账户（仅统一账户模式下支持）；<br><br>如不填，默认为资金账户 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | 申购订单ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1774534443629,
  "data": {
    "orderId": "142102777777777777"
  }
}
```

## 获取链上精选申购结果

`GET /api/v3/earn/elite-subscribe-result`

限频: 5次/s

权限: 统一账户管理 - 只读

查询链上精选申购结果。

Operation ID: `getEliteSubscribeResult`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string | 是 | 申购订单ID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.result | string |  | 申购结果<br><br>`settled` 申购成功；<br><br>`pending` 申购进行中；<br><br>`rejected` 申购失败 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1774535103055,
  "data": {
    "result": "settled"
  }
}
```

## 获取链上精选赎回信息

`GET /api/v3/earn/elite-redeem-info`

限频: 5次/s

权限: 统一账户管理 - 只读

查询链上精选赎回信息。

Operation ID: `getRedeemInfo`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| productId | query | string | 是 | 产品Id |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.productId | string |  | 产品Id |
| data.productSubId | string |  | 产品子Id |
| data.productCoin | string |  | 产品币种 |
| data.subscriptionCoin | string |  | 申购币种 |
| data.profitCoin | string |  | 收益币种 |
| data.exchangeRate | string |  | 兑换率，BGBTC/BGSOL使用 |
| data.totalUnPayInterestAmount | string |  | 累计未发放收益 |
| data.preSettleApr | string |  | 提前结算APR |
| data.receivedCoin | string |  | 到账币种，BGBTC/BGSOL使用 |
| data.unsettledPoints | string |  | 未结算积分，BGBTC有值 |
| data.bgusdReceiveCoinList | object[] |  | BGUSD到账币种列表，BGUSD使用 |
| data.bgusdReceiveCoinList[].bgusdReceiveCoin | string |  | BGUSD到账币种，BGUSD使用 |
| data.bgusdReceiveCoinList[].bgusdExchangeRate | string |  | BGUSD兑换率，BGUSD有值 |
| data.redeemModeList | object[] |  | 赎回模式列表 |
| data.redeemModeList[].redeemFeeRate | string |  | 赎回手续费率 |
| data.redeemModeList[].remainQuota | string |  | 剩余额度 |
| data.redeemModeList[].redeemType | string |  | 赎回类型<br><br>`fast` 快速赎回；<br><br>`standard` 标准赎回 |
| data.redeemModeList[].redeemScale | string |  | 赎回精度 |
| data.redeemModeList[].redeemDelayDate | string |  | 赎回延迟到账时间 |
| data.redeemModeList[].minRedeemAmount | string |  | 最小赎回金额 |
| data.redeemModeList[].redeemTime | string |  | 赎回时间 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1774536688556,
  "data": {
    "productId": "1216935633797513220",
    "productSubId": "1216935633814290435",
    "productCoin": "BGUSD",
    "subscriptionCoin": "",
    "profitCoin": "",
    "exchangeRate": "",
    "totalUnPayInterestAmount": "",
    "preSettleApr": "",
    "receivedCoin": "",
    "unsettledPoints": "",
    "bgusdReceiveCoinList": [
      {
        "bgusdReceiveCoin": "USDC",
        "bgusdExchangeRate": "1"
      },
      {
        "bgusdReceiveCoin": "USDT",
        "bgusdExchangeRate": "1.00035041"
      }
    ],
    "redeemModeList": [
      {
        "redeemFeeRate": "0.0005",
        "remainQuota": "9999.00000000",
        "redeemType": "fast",
        "redeemScale": "8",
        "redeemDelayDate": "10",
        "minRedeemAmount": "0.00000001",
        "redeemTime": "1774537288495"
      },
      {
        "redeemFeeRate": "0.0005",
        "remainQuota": "10000000.00000000",
        "redeemType": "standard",
        "redeemScale": "8",
        "redeemDelayDate": "3",
        "minRedeemAmount": "0.00000001",
        "redeemTime": "1774795888542"
      }
    ]
  }
}
```

## 链上精选赎回

`POST /api/v3/earn/elite-redeem`

限频: 5次/s

权限: 统一账户管理 - 读写

进行链上精选赎回。

Operation ID: `redeemElite`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| productId | query | string | 是 | 产品Id |
| productSubId | query | string | 是 | 产品子Id |
| redeemType | query | string | 是 | 赎回类型<br><br>`fast` 快速赎回<br><br>`standard` 标准赎回<br><br>BGUSD支持快速赎回及标准赎回；BGSOL/BGBTC仅支持标准赎回 |
| amount | query | string | 是 | 申购金额 |
| receiveAccount | query | string | 是 | 到账账户类型<br><br>`spot` 资金账户<br><br>`unified` 统一账户（仅统一账户模式下支持） |
| advancedSettle | query | string |  | 是否提前赎回<br><br>`yes` 是<br><br>`no` 否<br><br>默认值为 `no`<br><br>仅BGBTC使用 |
| coin | query | string |  | 申购币种，BGUSD必传 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | 赎回订单ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1774534443629,
  "data": {
    "orderId": "142102777777777777"
  }
}
```

## 获取链上精选资产信息

`GET /api/v3/earn/elite-assets`

限频: 5次/s

权限: 统一账户管理 - 只读

查询链上精选资产信息。

Operation ID: `getEliteAssets`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.resultList | object[] |  | 资产列表 |
| data.resultList[].productId | string |  | 产品Id |
| data.resultList[].productCoin | string |  | 产品币种 |
| data.resultList[].holdingAmount | string |  | 持有资产 |
| data.resultList[].usdtHoldingAmount | string |  | 持有资产(折U) |
| data.resultList[].exchangeRate | string |  | 兑换率 |
| data.resultList[].apr | string |  | 年化收益率，百分比形式，如4.20代表4.20%；适用于 BGSOL / BGBTC |
| data.resultList[].minApy | string |  | 最小年化收益率，仅适用于 BGUSD |
| data.resultList[].maxApy | string |  | 最大年化收益率，仅适用于 BGUSD |
| data.resultList[].subscriptionCoin | string |  | 申购币种 |
| data.resultList[].exchangeAmount | string |  | 兑换金额 |
| data.resultList[].projectList | object[] |  | 项目列表，仅适用于 BGBTC |
| data.resultList[].projectList[].projectName | string |  | 项目名称，仅适用于 BGBTC |
| data.resultList[].unsettledBGPoints | string |  | 未结算BG积分，仅适用于 BGBTC |
| data.resultList[].interestCoin | string |  | 派息币种，仅适用于 BGUSD |
| data.resultList[].totalProfit | string |  | 累计收益，仅适用于 BGUSD |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1774531452270,
  "data": {
    "resultList": [
      {
        "productId": "1216935633797513220",
        "productCoin": "BGUSD",
        "holdingAmount": "3.23436056",
        "usdtHoldingAmount": "3.23553532",
        "exchangeRate": "1",
        "apr": "4.00",
        "subscriptionCoin": "USDC",
        "exchangeAmount": "3.23436056",
        "unsettledBGPoints": "",
        "interestCoin": "BGUSD",
        "totalProfit": "0.16769105"
      }
    ]
  }
}
```

## 获取链上精选历史记录

`GET /api/v3/earn/elite-records`

限频: 5次/s

权限: 统一账户管理 - 只读

查询链上精选历史记录。

Operation ID: `getEliteRecords`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| startTime | query | string |  | 开始时间戳<br><br>Unix毫秒时间戳，如1597026383085；时间跨度最大支持三个月；<br><br>若不传，则默认结束时间为三个月 |
| endTime | query | string |  | 结束时间戳<br><br>Unix毫秒时间戳，如1597026383085 |
| limit | query | string |  | 查询条数<br><br>默认20，最大100 |
| cursor | query | string |  | 游标ID<br><br>请求此ID之后（更新的数据）的分页内容，传的值为对应接口的 `endId` |
| type | query | string | 是 | 记录类型<br><br>`subscribe` 申购；<br><br>`redeem` 赎回；<br><br>`interest` 派息 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.recordList | object[] |  | 记录列表 |
| data.recordList[].recordId | string |  | 记录ID |
| data.recordList[].productId | string |  | 产品ID |
| data.recordList[].coin | string |  | 币种名称 |
| data.recordList[].status | string |  | 订单状态<br><br>申购：`settled` 申购成功，`pending` 申购进行中，`rejected` 申购失败；<br><br>赎回：`settled` 赎回成功，`pending` 赎回进行中；<br><br>派息：`settled` 派息成功，`pending` 派息中 |
| data.recordList[].exchangeRate | string |  | 兑换率 |
| data.recordList[].receivedCoin | string |  | 接收币种 |
| data.recordList[].receivedAmount | string |  | 接收金额 |
| data.recordList[].investAmount | string |  | 投资金额 |
| data.recordList[].feeRate | string |  | 手续费率 |
| data.recordList[].redeemType | string[] |  | 赎回类型<br><br>`fast` 快速赎回；<br><br>`standard` 标准赎回 |
| data.recordList[].receivingAccount | string |  | 赎回账户<br><br>`spot` 资金账户；<br><br>`unified` 统一账户（仅统一账户模式下支持）；<br><br>仅在 `type=redeem` 时返回 |
| data.recordList[].actualReceivingAccount | string |  | 实际赎回账户<br><br>`spot` 资金账户；<br><br>`unified` 统一账户（仅统一账户模式下支持）；<br><br>仅在 `type=redeem` 时返回 |
| data.recordList[].paymentAccount | string[] |  | 付款账户<br><br>`spot` 资金账户；<br><br>`unified` 统一账户（仅统一账户模式下支持）；<br><br>仅在 `type=subscribe` 时返回 |
| data.recordList[].settlePoints | string |  | 结算积分，仅在 BGBTC 且 `type=interest` 时返回 |
| data.recordList[].fee | string |  | 手续费，仅适用于 `type=redeem` 与 `type=subscribe` |
| data.recordList[].bizTime | string |  | 业务时间 |
| data.endId | string |  | 翻页游标 ID（取当前页最小记录 ID，传入 `cursor` 查询更早的记录） |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1774531930360,
  "data": {
    "recordList": [
      {
        "recordId": "1421055362391416832",
        "productId": "1216935633797513218",
        "coin": "BGSOL",
        "status": "settled",
        "exchangeRate": "0.87525878",
        "receivedCoin": "BGSOL",
        "receivedAmount": "0.00875258",
        "investAmount": "0.01",
        "feeRate": "",
        "redeemType": "",
        "receivingAccount": "",
        "actualReceivingAccount": "",
        "paymentAccount": [
          "spot"
        ],
        "settlePoints": "",
        "fee": "0",
        "bizTime": "1774531930360"
      }
    ],
    "endId": "1421055235278839808"
  }
}
```

## 获取现金宝申购详情

`GET /api/v3/earn/cashplus/subscribe-info`

限频: 10次/s

权限: 统一账户管理 - 只读

查询现金宝申购前置信息，包括当前年化及可申购币种列表。

Operation ID: `getCashPlusSubscribeInfo`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.profitSourceCoin | string |  | 收益来源币种<br/>当前为 `USDGO` |
| data.cashPlusApr | string |  | 现金宝当前年化<br/>小数形式表示，如 `0.04` 代表 4% |
| data.subscribeCoinList | object[] |  | 申购币种列表 |
| data.subscribeCoinList[].productSubId | string |  | 产品子ID<br/>用于现金宝申购及赎回 |
| data.subscribeCoinList[].coin | string |  | 币种名称 |
| data.subscribeCoinList[].minAmount | string |  | 最小申购数量<br/>单位为 coin |
| data.subscribeCoinList[].conversionRate | string |  | 兑换比例<br/>数字形式，默认值为 `1`<br/>代表数量为 1 的当前币种能兑换多少现金宝 |
| data.subscribeCoinList[].subscribeScale | string |  | 申购精度<br/>小数位数 |
| data.subscribeCoinList[].profitScale | string |  | 收益精度<br/>小数位数 |
| data.subscribeCoinList[].soldOut | string |  | 是否售罄<br/>`yes` 已售罄<br/>`no` 未售罄 |
| data.interestTime | string |  | 起息时间，Unix 毫秒时间戳 |
| data.payInterestTime | string |  | 派息时间，Unix 毫秒时间戳 |
| data.subscribeTime | string |  | 申购时间，Unix 毫秒时间戳 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1789368447497,
  "data": {
    "profitSourceCoin": "USDGO",
    "cashPlusApr": "0.04",
    "subscribeCoinList": [
      {
        "productSubId": "1358292433724211201",
        "coin": "USDT",
        "minAmount": "10",
        "conversionRate": "1",
        "subscribeScale": "2",
        "profitScale": "8",
        "soldOut": "no"
      },
      {
        "productSubId": "1358292433724211202",
        "coin": "USDC",
        "minAmount": "10",
        "conversionRate": "1",
        "subscribeScale": "2",
        "profitScale": "8",
        "soldOut": "no"
      }
    ],
    "interestTime": "1789368447497",
    "payInterestTime": "1789454847497",
    "subscribeTime": "1789368447497"
  }
}
```

## 现金宝申购

`POST /api/v3/earn/cashplus/subscribe`

限频: 1次/s

权限: 统一账户管理 - 读写

使用指定币种及数量申购现金宝。

Operation ID: `cashPlusSubscribe`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| productSubId | string | 是 | 产品子ID<br/>由 `申购详情` 接口获取 |
| amount | number | 是 | 申购数量，单位为申购币种 |
| accountType | string |  | 转入账户类型<br/>`funding` 资金账户<br/>`uta` 统一账户<br/>`otc` OTC账户<br/>支持多选，多个账户类型用英文逗号分隔（如 `funding,uta`）。不传时默认为资金账户 |
| idempotentNo | string |  | 幂等ID，用于防止重复提交 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | 申购订单ID，用于查询申购结果 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1789368447497,
  "data": {
    "orderId": "1483284264811290624"
  }
}
```

## 获取现金宝申购结果

`GET /api/v3/earn/cashplus/subscribe-result`

限频: 10次/s

权限: 统一账户管理 - 只读

查询现金宝申购订单的结果。

Operation ID: `getCashPlusSubscribeResult`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string | 是 | 申购接口返回的订单ID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | 申购订单ID |
| data.status | string |  | 申购订单状态<br/>`processing` 进行中<br/>`success` 申购成功<br/>`failed` 申购失败 |
| data.coin | string |  | 申购币种 |
| data.amount | string |  | 申购数量 |
| data.subscribeTime | string |  | 申购时间，Unix 毫秒时间戳 |
| data.interestTime | string |  | 起息时间，Unix 毫秒时间戳 |
| data.dividendTime | string |  | 首次派息时间，Unix 毫秒时间戳 |
| data.paymentAccountList | object[] |  | 支付账户列表 |
| data.paymentAccountList[].accountType | string |  | 账户类型<br/>`funding` 资金账户<br/>`uta` 统一账户<br/>`otc` OTC账户 |
| data.paymentAccountList[].payAmount | string |  | 该账户支付金额 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1789368447497,
  "data": {
    "orderId": "1483284264811290624",
    "status": "success",
    "coin": "USDT",
    "amount": "100",
    "subscribeTime": "1789368447497",
    "interestTime": "1789368447497",
    "dividendTime": "1789454847497",
    "paymentAccountList": [
      {
        "accountType": "funding",
        "payAmount": "60"
      },
      {
        "accountType": "uta",
        "payAmount": "40"
      }
    ]
  }
}
```

## 获取现金宝赎回详情

`GET /api/v3/earn/cashplus/redeem-info`

限频: 10次/s

权限: 统一账户管理 - 只读

查询现金宝赎回前置信息，包括赎回到账币种列表及可赎回持仓。

Operation ID: `getCashPlusRedeemInfo`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.redeemCoinList | object[] |  | 赎回到账币种列表 |
| data.redeemCoinList[].productSubId | string |  | 产品子ID<br/>用于现金宝申购及赎回 |
| data.redeemCoinList[].coin | string |  | 币种名称 |
| data.redeemCoinList[].conversionRate | string |  | 赎回兑换率<br/>即数量为 1 的现金宝等于多少该币种 |
| data.redeemCoinList[].redeemAvailable | string |  | 可赎回的现金宝持仓数量 |
| data.redeemCoinList[].redeemMinAmount | string |  | 最小赎回金额 |
| data.redeemCoinList[].redeemScale | string |  | 赎回金额精度，小数位数 |
| data.redeemCoinList[].redeemTime | string |  | 解锁申请时间，Unix 毫秒时间戳 |
| data.redeemCoinList[].receivedTime | string |  | 赎回预计到账时间，Unix 毫秒时间戳 |
| data.userRemainingQuota | string |  | 今日用户剩余可赎回额度 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1789368447497,
  "data": {
    "redeemCoinList": [
      {
        "productSubId": "1358292433724211201",
        "coin": "USDT",
        "conversionRate": "1",
        "redeemAvailable": "100.00000000",
        "redeemMinAmount": "0.01",
        "redeemScale": "2",
        "redeemTime": "1789368447497",
        "receivedTime": "1789372047497"
      }
    ],
    "userRemainingQuota": "50000"
  }
}
```

## 现金宝赎回

`POST /api/v3/earn/cashplus/redeem`

限频: 1次/s

权限: 统一账户管理 - 读写

将现金宝赎回为指定币种。

Operation ID: `cashPlusRedeem`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| productSubId | string | 是 | 产品子ID |
| amount | string | 是 | 赎回的现金宝数量 |
| accountType | string |  | 到账账户类型<br/>`funding` 资金账户<br/>`uta` 统一账户<br/>不传时默认为资金账户 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | 赎回订单ID，用于查询赎回结果 |
| data.redeemTime | integer (int64) |  | 赎回申请时间，Unix 毫秒时间戳 |
| data.receiveTime | integer (int64) |  | 预计到账时间，Unix 毫秒时间戳 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1789368447497,
  "data": {
    "orderId": "1483284264811290624",
    "redeemTime": 1789368447497,
    "receiveTime": 1789368447497
  }
}
```

## 获取现金宝赎回结果

`GET /api/v3/earn/cashplus/redeem-result`

限频: 10次/s

权限: 统一账户管理 - 只读

查询现金宝赎回订单的结果。

Operation ID: `getCashPlusRedeemResult`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string | 是 | 赎回接口返回的订单ID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | 赎回订单ID |
| data.status | string |  | 赎回状态<br/>`processing` 进行中<br/>`success` 赎回成功<br/>`failed` 赎回失败 |
| data.redeemTime | string |  | 赎回申请时间，Unix 毫秒时间戳 |
| data.receiveTime | string |  | 预计到账时间，Unix 毫秒时间戳 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1789368447497,
  "data": {
    "orderId": "1483284264811290624",
    "status": "success",
    "redeemTime": "1789368447497",
    "receiveTime": "1789368447497"
  }
}
```

## 获取现金宝持仓

`GET /api/v3/earn/cashplus/positions`

限频: 10次/s

权限: 统一账户管理 - 只读

查询用户的现金宝持仓。

Operation ID: `getCashPlusPositions`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.balance | string |  | 现金宝持仓<br/>折合 USD 金额 |
| data.totalProfit | string |  | 累计收益<br/>折合 USD 金额 |
| data.yesterdayProfit | string |  | 昨日收益<br/>折合 USD 金额 |
| data.apr | string |  | 年化收益率<br/>可用作参考的复合年利率 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1789368447497,
  "data": {
    "balance": "100.00",
    "totalProfit": "0.05",
    "yesterdayProfit": "0.01",
    "apr": "0.04"
  }
}
```

## 获取现金宝历史订单

`GET /api/v3/earn/cashplus/history-orders`

限频: 10次/s

权限: 统一账户管理 - 只读

使用游标分页查询现金宝历史记录。

Operation ID: `getCashPlusHistoryOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| startTime | query | string |  | 查询起始时间，Unix 毫秒时间戳 |
| endTime | query | string |  | 查询结束时间，Unix 毫秒时间戳 |
| recordType | query | string |  | 记录类型<br/>`subscribe` 申购<br/>`redeem` 赎回<br/>`compound_interest` 复利收益<br/>`liquidation_redeem` 清算赎回 |
| limit | query | string |  | 每页条目数<br/>默认 20，最大 100 |
| cursor | query | string |  | 游标ID<br/>传入上一页返回的 `nextCursor` 用于翻页。首页不传 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.items | object[] |  | 记录列表 |
| data.items[].recordId | string |  | 记录ID |
| data.items[].recordType | string |  | 记录类型<br/>`subscribe` 申购<br/>`redeem` 赎回<br/>`compound_interest` 复利收益<br/>`liquidation_redeem` 清算赎回 |
| data.items[].status | string |  | 记录状态<br/>`processing` 进行中<br/>`success` 成功<br/>`failed` 失败 |
| data.items[].amount | string |  | 变动数量 |
| data.items[].coin | string |  | 币种名称 |
| data.items[].createdTime | integer (int64) |  | 记录创建时间，Unix 毫秒时间戳 |
| data.items[].accountType | string |  | 账户类型<br/>`funding` 资金账户<br/>`uta` 统一账户<br/>`otc` OTC账户<br/>类型为转入时，对应支出账户<br/>类型为利息或转出时，对应到账账户 |
| data.nextCursor | string |  | 下一页游标ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1789368447497,
  "data": {
    "items": [
      {
        "recordId": "1483284264811290624",
        "recordType": "subscribe",
        "status": "success",
        "amount": "100",
        "coin": "USDT",
        "createdTime": 1789368447497,
        "accountType": "funding"
      }
    ],
    "nextCursor": "1483284264811290623"
  }
}
```

## 简单赚币产品列表

`GET /api/v3/earn/savings/product`

限频规则: 10次/秒/UID

获取简单赚币产品列表。

Operation ID: `getSavingsProduct`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string |  | 币种 |
| filter | query | string |  | 筛选条件<br><br>`available` 可申购的<br><br>`held` 持有中<br><br>`available_and_held` 申购和持有中<br><br>`all` 查询全部 包含下架的 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].productId | string |  | 产品Id |
| data[].coin | string |  | 产品申购币种 |
| data[].periodType | string |  | 期限类型<br><br>`flexible` 活期<br><br>`fixed` 定期 |
| data[].period | string |  | 期限时长<br><br>`flexible` 不返回此值 |
| data[].apyType | string |  | 利率类型<br><br>`single` 单一利率<br><br>`ladder` 阶梯收益 |
| data[].advanceRedeem | string |  | 是否允许提前赎回<br><br>`Yes` 允许<br><br>`No` 不允许 |
| data[].settleMethod | string |  | 结算方式<br><br>`daily` 日息日结<br><br>`maturity` 到期还本付息 |
| data[].apyList | object[] |  | 阶梯利率信息 |
| data[].apyList[].rateLevel | string |  | 费率级别 |
| data[].apyList[].minStepVal | string |  | 阶梯最小金额值 |
| data[].apyList[].maxStepVal | string |  | 阶梯最大金额值 |
| data[].apyList[].currentApy | string |  | 当前阶梯年利率 |
| data[].status | string |  | 产品状态<br><br>`not_started` 预热中<br><br>`in_progress` 申购中<br><br>`paused` 已暂停<br><br>`completed` 已结束<br><br>`sold_out` 已售罄<br><br>`off_line` 已下线 |
| data[].productLevel | string |  | 产品级别<br><br>`beginner` 新手产品<br><br>`normal` 普通产品<br><br>`VIP` VIP 产品 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1696747382760,
  "data": [
    {
      "productId": "12313123",
      "coin": "BGB",
      "periodType": "flexible",
      "period": "",
      "apyType": "ladder",
      "advanceRedeem": "",
      "settleMethod": "",
      "apyList": [
        {
          "rateLevel": "0",
          "minStepVal": "0.000000",
          "maxStepVal": "200.000000",
          "currentApy": "6.00"
        },
        {
          "rateLevel": "1",
          "minStepVal": "200.000000",
          "maxStepVal": "5000.000000",
          "currentApy": "50.00"
        }
      ],
      "status": "in_progress",
      "productLevel": "normal"
    }
  ]
}
```

## 简单赚币账户信息

`GET /api/v3/earn/savings/account`

限频规则: 10次/秒/UID

获取简单赚币账户信息。

Operation ID: `getSavingsAccount`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.btcAmount | string |  | BTC计价的预估资产总值 |
| data.usdtAmount | string |  | USDT计价的预估资产总值 |
| data.btc24hEarning | string |  | BTC计价的24小时收益 |
| data.usdt24hEarning | string |  | USDT计价的24小时收益 |
| data.btcTotalEarning | string |  | BTC计价的累计收益 |
| data.usdtTotalEarning | string |  | USDT计价的累计收益 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1696748551073,
  "data": {
    "btcAmount": "0.35821314",
    "usdtAmount": "9481.55500000",
    "btc24hEarning": "0.00000009",
    "usdt24hEarning": "0.00263912",
    "btcTotalEarning": "0.00000761",
    "usdtTotalEarning": "0.20145653"
  }
}
```

## 简单赚币资产信息

`GET /api/v3/earn/savings/assets`

限频规则: 10次/秒/UID

获取简单赚币资产信息。

Operation ID: `getSavingsAssets`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| periodType | query | string | 是 | 期限类型<br><br>`flexible` 活期<br><br>`fixed` 定期 |
| startTime | query | string |  | 开始时间戳<br><br>（跟单创建时间）<br><br>Unix时间戳的毫秒数格式，如 1597026383085<br><br>（时间跨度最大支持三个月，若不传结束时间，则默认结束时间为三个月。） |
| endTime | query | string |  | 结束时间戳<br><br>（跟单创建时间）<br><br>Unix时间戳的毫秒数格式，如 1597026383085<br><br>（时间跨度最大支持三个月，若不传开始时间，则默认开始时间为三个月。） |
| limit | query | string |  | 查询条数<br><br>默认20，最大100 |
| cursor | query | string |  | 游标ID<br><br>用于分页。首次调用不传。后续调用传入上次查询返回的最后一个`endId` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.resultList | object[] |  | 资产列表 |
| data.resultList[].productId | string |  | 产品Id |
| data.resultList[].orderId | string |  | 申购记录Id<br><br>定期赎回使用 |
| data.resultList[].productCoin | string |  | 产品申购币种 |
| data.resultList[].interestCoin | string |  | 产品派息币种 |
| data.resultList[].periodType | string |  | 期限类型<br><br>`flexible` 活期<br><br>`fixed` 定期 |
| data.resultList[].period | string |  | 期限时长<br><br>`flexible` 不返回此值 |
| data.resultList[].holdAmount | string |  | 当前申购数量 |
| data.resultList[].lastProfit | string |  | 昨日收益 |
| data.resultList[].totalProfit | string |  | 累计收益 |
| data.resultList[].holdDays | string |  | 目前已持有天数 |
| data.resultList[].status | string |  | 产品状态<br><br>`in_holding` 持有中 |
| data.resultList[].allowRedemption | string |  | 是否允许提前赎回<br><br>`Yes` 允许<br><br>`No` 不允许 |
| data.resultList[].productLevel | string |  | 产品等级<br><br>`beginner` 新手产品<br><br>`normal` 普通产品<br><br>`VIP` VIP 产品 |
| data.resultList[].apy | object[] |  | 阶梯利率信息 |
| data.resultList[].apy[].rateLevel | string |  | 费率级别 |
| data.resultList[].apy[].minApy | string |  | 阶梯最小金额值 |
| data.resultList[].apy[].maxApy | string |  | 阶梯最大金额值 |
| data.resultList[].apy[].currentApy | string |  | 当前阶梯年利率 |
| data.endId | string |  | 分页结束ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1696748867881,
  "data": {
    "resultList": [
      {
        "productId": "123123123",
        "orderId": "xxxx",
        "productCoin": "BGB",
        "interestCoin": "BGB",
        "periodType": "flexible",
        "period": "",
        "holdAmount": "100.000",
        "lastProfit": "0.01643800",
        "totalProfit": "1.25479000",
        "holdDays": "",
        "status": "in_holding",
        "allowRedemption": "",
        "productLevel": "normal",
        "apy": [
          {
            "rateLevel": "1",
            "minApy": "0.000000",
            "maxApy": "200.000000",
            "currentApy": "6.00"
          }
        ]
      }
    ],
    "endId": "123456789"
  }
}
```

## 简单赚币历史记录

`GET /api/v3/earn/savings/records`

限频规则: 10次/秒/UID

获取简单赚币历史记录。

Operation ID: `getSavingsRecords`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string |  | 申购币种 |
| periodType | query | string | 是 | 期限类型<br><br>`flexible` 活期<br><br>`fixed` 定期 |
| orderType | query | string |  | 记录类型<br><br>`subscribe` 申购<br><br>`redeem` 赎回<br><br>`pay_interest` 利息支付<br><br>`deduction` 罚息 (仅支持定期) |
| startTime | query | string |  | 开始时间戳<br><br>（跟单创建时间）<br><br>Unix时间戳的毫秒数格式，如 1597026383085<br><br>（时间跨度最大支持三个月，若不传结束时间，则默认结束时间为三个月。） |
| endTime | query | string |  | 结束时间戳<br><br>（跟单创建时间）<br><br>Unix时间戳的毫秒数格式，如 1597026383085<br><br>（时间跨度最大支持三个月，若不传开始时间，则默认开始时间为三个月。） |
| limit | query | string |  | 查询条数<br><br>默认20，最大100 |
| cursor | query | string |  | 游标ID<br><br>用于分页。首次调用不传。后续调用传入上次查询返回的最后一个`endId` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.resultList | object[] |  | 记录列表 |
| data.resultList[].orderId | string |  | 记录Id |
| data.resultList[].coinName | string |  | 产品申购币种 |
| data.resultList[].settleCoinName | string |  | 结算币种 |
| data.resultList[].productType | string |  | 期限类型<br><br>`flexible` 活期<br><br>`fixed` 定期 |
| data.resultList[].period | string |  | 期限时长<br><br>`flexible` 不返回此值 |
| data.resultList[].productLevel | string |  | 产品级别<br><br>`beginner` 新手产品<br><br>`normal` 普通产品<br><br>`VIP` VIP 产品 |
| data.resultList[].amount | string |  | 金额 |
| data.resultList[].ts | string |  | 创建时间 时间戳 |
| data.resultList[].orderType | string |  | 订单类型<br><br>`subscribe` 申购<br><br>`redeem` 赎回<br><br>`pay_interest` 利息支付<br><br>`deduction` 罚息 (仅支持定期) |
| data.endId | string |  | 分页结束ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1696749517654,
  "data": {
    "resultList": [
      {
        "orderId": "123123123123",
        "coinName": "BGB",
        "settleCoinName": "BGB",
        "productType": "flexible",
        "period": "",
        "productLevel": "normal",
        "amount": "200.000000",
        "ts": "1695797014392",
        "orderType": "redeem"
      }
    ],
    "endId": "456456456456"
  }
}
```

## 简单赚币申购详情

`GET /api/v3/earn/savings/subscribe-info`

限频规则: 10次/秒/UID

获取简单赚币申购详情。

Operation ID: `getSavingsSubscribeInfo`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| productId | query | string | 是 | 产品Id |
| periodType | query | string | 是 | 期限类型<br><br>`flexible` 活期<br><br>`fixed` 定期 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.singleMinAmount | string |  | 单笔最小限额 |
| data.singleMaxAmount | string |  | 单笔最大限额 |
| data.remainingAmount | string |  | 持有中总额 |
| data.subscribePrecision | string |  | 申购精度 |
| data.profitPrecision | string |  | 收益精度 |
| data.subscribeTime | string |  | 申购时间，Unix毫秒时间戳 |
| data.interestTime | string |  | 起息时间，Unix毫秒时间戳 |
| data.settleTime | string |  | 派息时间，Unix毫秒时间戳 |
| data.expireTime | string |  | 到期时间，Unix毫秒时间戳 |
| data.redeemTime | string |  | 赎回时间，Unix毫秒时间戳 |
| data.settleMethod | string |  | 结算方式 |
| data.apyList | object[] |  | 阶梯利率信息 |
| data.apyList[].rateLevel | string |  | 费率级别 |
| data.apyList[].minStepVal | string |  | 阶梯最小金额值 |
| data.apyList[].maxStepVal | string |  | 阶梯最大金额值 |
| data.apyList[].currentApy | string |  | 当前阶梯年利率 |
| data.redeemDelay | string |  | 赎回到账延迟时间天数<br><br>返回值为D+1，则代表延迟一天到账，以此类推 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1696751519392,
  "data": {
    "singleMinAmount": "10.000000",
    "singleMaxAmount": "2000.000000",
    "remainingAmount": "4899.999990",
    "subscribePrecision": "6",
    "profitPrecision": "6",
    "subscribeTime": "1696751519451",
    "interestTime": "1696780800000",
    "settleTime": "1696867200000",
    "expireTime": "",
    "redeemTime": "",
    "settleMethod": "",
    "apyList": [
      {
        "rateLevel": "0",
        "minStepVal": "0.000000",
        "maxStepVal": "200.000000",
        "currentApy": "6.00"
      },
      {
        "rateLevel": "1",
        "minStepVal": "200.000000",
        "maxStepVal": "5000.000000",
        "currentApy": "50.00"
      }
    ],
    "redeemDelay": ""
  }
}
```

## 简单赚币申购

`POST /api/v3/earn/savings/subscribe`

限频规则: 10次/秒/UID

简单赚币申购。

Operation ID: `savingsSubscribe`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| productId | string | 是 | 产品Id |
| periodType | string | 是 | 期限类型<br><br>`flexible` 活期<br><br>`fixed` 定期 |
| amount | string | 是 | 申购金额 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | 申购成功订单Id |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1748783837837,
  "data": {
    "orderId": "1313060074239184896"
  }
}
```

## 简单赚币申购结果

`GET /api/v3/earn/savings/subscribe-result`

限频规则: 10次/秒/UID

获取简单赚币申购结果。

Operation ID: `getSavingsSubscribeResult`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string | 是 | 订单Id |
| periodType | query | string | 是 | 期限类型<br><br>`flexible` 活期<br><br>`fixed` 定期 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.result | string |  | 申购是否成功<br><br>`success` 成功<br><br>`fail` 失败 |
| data.msg | string |  | 只有失败时才会返回信息 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1696752594890,
  "data": {
    "result": "success",
    "msg": ""
  }
}
```

## 简单赚币赎回

`POST /api/v3/earn/savings/redeem`

限频规则: 10次/秒/UID

简单赚币赎回。

每次赎回间隔应大于1分钟，否则可能会报错。

Operation ID: `savingsRedeem`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| productId | string | 是 | 产品Id |
| orderId | string |  | 申购记录Id<br><br>从 assets 获取 |
| periodType | string | 是 | 期限类型<br><br>`flexible` 活期<br><br>`fixed` 定期 |
| amount | string | 是 | 申购金额 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | 赎回成功订单Id |
| data.status | string |  | 订单状态 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1696751519392,
  "data": {
    "orderId": "123123123",
    "status": "2000.000000"
  }
}
```

## 简单赚币赎回结果

`GET /api/v3/earn/savings/redeem-result`

限频规则: 10次/秒/UID

获取简单赚币赎回结果。

Operation ID: `getSavingsRedeemResult`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string | 是 | 申购订单Id |
| periodType | query | string | 是 | 期限类型<br><br>`flexible` 活期<br><br>`fixed` 定期 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.result | string |  | 赎回是否成功<br><br>`success` 成功<br><br>`fail` 失败 |
| data.msg | string |  | 只有失败时才会返回信息 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1696752594890,
  "data": {
    "result": "success",
    "msg": ""
  }
}
```

## 鲨鱼鳍产品列表

`GET /api/v3/earn/sharkfin/product`

限频规则: 10次/秒/UID

获取鲨鱼鳍产品列表。

Operation ID: `getSharkfinProduct`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string | 是 | 币种 |
| limit | query | string |  | 查询条数<br><br>默认20，最大100 |
| cursor | query | string |  | 游标ID<br><br>用于分页。首次调用不传。后续调用传入上次查询返回的最后一个`endId` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.resultList | object[] |  | 鲨鱼鳍产品信息 |
| data.resultList[].productId | string |  | 产品Id |
| data.resultList[].productName | string |  | 产品名称 |
| data.resultList[].productCoin | string |  | 产品申购币种 |
| data.resultList[].subscribeCoin | string |  | 派息币种 |
| data.resultList[].farmingStartTime | string |  | 开始时间，Unix毫秒时间戳 |
| data.resultList[].farmingEndTime | string |  | 停止时间，Unix毫秒时间戳 |
| data.resultList[].lowerRate | string |  | 费率最小值 |
| data.resultList[].defaultRate | string |  | 费率默认值 |
| data.resultList[].upperRate | string |  | 费率最大值 |
| data.resultList[].period | string |  | 投资期限 |
| data.resultList[].interestStartTime | string |  | 计息开始时间 |
| data.resultList[].status | string |  | 产品状态<br><br>`not_started` 预热中<br><br>`in_progress` 申购中<br><br>`paused` 已暂停<br><br>`interest_pending` 计息中<br><br>`settle_pending` 待结算<br><br>`settled` 已结算<br><br>`redeemed` 已赎回<br><br>`sold_out` 已售罄 |
| data.resultList[].minAmount | string |  | 产品最小限额 |
| data.resultList[].limitAmount | string |  | 产品额度<br><br>若无限制则返回 `unlimited` |
| data.resultList[].soldAmount | string |  | 已售额度 |
| data.resultList[].startTime | string |  | 开始时间<br><br>Unix时间戳的毫秒数格式 |
| data.resultList[].endTime | string |  | 结束时间<br><br>Unix时间戳的毫秒数格式 |
| data.endId | string |  | 分页结束ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1696754489003,
  "data": {
    "resultList": [
      {
        "productId": "1",
        "productName": "USDT/ETH_20231009",
        "productCoin": "ETH",
        "subscribeCoin": "USDT",
        "farmingStartTime": "1696744800000",
        "farmingEndTime": "1696831200000",
        "lowerRate": "7.06",
        "defaultRate": "7",
        "upperRate": "8.8",
        "period": "7",
        "interestStartTime": "1696838400000",
        "status": "in_progress",
        "minAmount": "0.1",
        "limitAmount": "500001.0",
        "soldAmount": "310187.2",
        "endTime": "1696831200000",
        "startTime": "1696744800000"
      }
    ],
    "endId": "1"
  }
}
```

## 鲨鱼鳍账户信息

`GET /api/v3/earn/sharkfin/account`

限频规则: 10次/秒/UID

获取鲨鱼鳍账户信息。

Operation ID: `getSharkfinAccount`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.btcSubscribeAmount | string |  | BTC计价的预估资产总值 |
| data.usdtSubscribeAmount | string |  | USDT计价的预估资产总值 |
| data.btcHistoricalAmount | string |  | BTC计价的24小时收益 |
| data.usdtHistoricalAmount | string |  | USDT计价的24小时收益 |
| data.btcTotalEarning | string |  | BTC计价的累计收益 |
| data.usdtTotalEarning | string |  | USDT计价的累计收益 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1696755312297,
  "data": {
    "btcSubscribeAmount": "0.00000000",
    "usdtSubscribeAmount": "0.00",
    "btcHistoricalAmount": "0.00000000",
    "usdtHistoricalAmount": "0.00000000",
    "btcTotalEarning": "0.00000000",
    "usdtTotalEarning": "0.00000000"
  }
}
```

## 鲨鱼鳍资产信息

`GET /api/v3/earn/sharkfin/assets`

限频规则: 10次/秒/UID

获取鲨鱼鳍资产信息。

Operation ID: `getSharkfinAssets`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| status | query | string | 是 | 鲨鱼鳍状态<br><br>`subscribed` 已申购(默认)<br><br>`settled` 已结算 |
| startTime | query | string |  | 开始时间戳<br><br>（跟单创建时间）<br><br>Unix时间戳的毫秒数格式，如 1597026383085<br><br>（时间跨度最大支持三个月，若不传结束时间，则默认结束时间为三个月。） |
| endTime | query | string |  | 结束时间戳<br><br>（跟单创建时间）<br><br>Unix时间戳的毫秒数格式，如 1597026383085<br><br>（时间跨度最大支持三个月，若不传开始时间，则默认开始时间为三个月。） |
| limit | query | string |  | 查询条数<br><br>默认20，最大100 |
| cursor | query | string |  | 游标ID<br><br>用于分页。首次调用不传。后续调用传入上次查询返回的最后一个`endId` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.resultList | object[] |  | 鲨鱼鳍产品信息 |
| data.resultList[].productId | string |  | 产品Id |
| data.resultList[].interestStartTime | string |  | 计息开始时间 |
| data.resultList[].interestEndTime | string |  | 计息结束时间 |
| data.resultList[].productCoin | string |  | 产品申购币种 |
| data.resultList[].subscribeCoin | string |  | 派息币种 |
| data.resultList[].trend | string |  | 趋势<br><br>`up` 涨<br><br>`down` 跌 |
| data.resultList[].settleTime | string |  | 结算时间，Unix毫秒时间戳 |
| data.resultList[].interestAmount | string |  | 收益 |
| data.resultList[].productStatus | string |  | 产品状态<br><br>`running` 申购中<br><br>`pause` 已暂停<br><br>`wait_interest` 待起息<br><br>`wait_settle` 待结算<br><br>`settle` 已结算<br><br>`redeem` 已赎回<br><br>`sell_out` 已售罄 |
| data.endId | string |  | 分页结束ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1696756316611,
  "data": {
    "resultList": [
      {
        "productId": "12312313",
        "interestStartTime": "1697199180000",
        "interestEndTime": "1697803980000",
        "productCoin": "BTC",
        "subscribeCoin": "USDT",
        "trend": "up",
        "settleTime": "1697803980000",
        "interestAmount": "",
        "productStatus": "running"
      }
    ],
    "endId": "456456456"
  }
}
```

## 鲨鱼鳍历史记录

`GET /api/v3/earn/sharkfin/records`

限频规则: 10次/秒/UID

获取鲨鱼鳍历史记录。

Operation ID: `getSharkfinRecords`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string |  | 申购币种 |
| type | query | string | 是 | 交易类型<br><br>`subscription` 申购<br><br>`redemption` 赎回<br><br>`interest` 利息派付 |
| startTime | query | string |  | 开始时间戳<br><br>Unix时间戳的毫秒数格式，如 1597026383085<br><br>（时间跨度最大支持三个月，若不传结束时间，则默认结束时间为三个月。） |
| endTime | query | string |  | 结束时间戳<br><br>Unix时间戳的毫秒数格式，如 1597026383085<br><br>（时间跨度最大支持三个月，若不传开始时间，则默认开始时间为三个月。） |
| limit | query | string |  | 查询条数<br><br>默认20，最大100 |
| cursor | query | string |  | 游标ID<br><br>用于分页。首次调用不传。后续调用传入上次查询返回的最后一个`endId` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.resultList | object[] |  | 记录列表 |
| data.resultList[].orderId | string |  | 记录Id |
| data.resultList[].product | string |  | 产品名称 |
| data.resultList[].period | string |  | 期限时长 |
| data.resultList[].amount | string |  | 金额 |
| data.resultList[].ts | string |  | 创建时间 时间戳 |
| data.resultList[].type | string |  | 交易类型<br><br>`subscription` 申购<br><br>`redemption` 赎回<br><br>`interest` 利息派付 |
| data.endId | string |  | 分页结束ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1696757048457,
  "data": {
    "resultList": [
      {
        "orderId": "1",
        "product": "USDT/BTC_20231013",
        "period": "7",
        "amount": "100.00000000",
        "ts": "1696756278760",
        "type": "subscription"
      }
    ],
    "endId": "1"
  }
}
```

## 鲨鱼鳍申购详情

`GET /api/v3/earn/sharkfin/subscribe-info`

限频规则: 10次/秒/UID

获取鲨鱼鳍申购详情。

Operation ID: `getSharkfinSubscribeInfo`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| productId | query | string | 是 | 产品Id |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.productCoin | string |  | 产品币种 |
| data.subscribeCoin | string |  | 申购币种 |
| data.interestTime | string |  | 起息日期 Unix时间戳的毫秒数格式 |
| data.expirationTime | string |  | 结算时间 Unix时间戳的毫秒数格式 |
| data.minPrice | string |  | 价格区间的最小价格 |
| data.currentPrice | string |  | 当前价格 |
| data.maxPrice | string |  | 价格区间的最大价格 |
| data.minRate | string |  | 派费率最小值 |
| data.defaultRate | string |  | 费率默认值 |
| data.maxRate | string |  | 费率最大值 |
| data.period | string |  | 投资期限 |
| data.productMinAmount | string |  | 产品最小限额 |
| data.availableBalance | string |  | 可用余额 |
| data.userAmount | string |  | 单人额度 |
| data.remainingAmount | string |  | 剩余额度 |
| data.profitPrecision | string |  | 计息精度 |
| data.subscribePrecision | string |  | 申购金额精度 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1696757209022,
  "data": {
    "productCoin": "BTC",
    "subscribeCoin": "USDT",
    "interestTime": "1697199180000",
    "expirationTime": "1697803980000",
    "minPrice": "28000.00",
    "currentPrice": "30211.23",
    "maxPrice": "32000.00",
    "minRate": "5.00",
    "defaultRate": "1.00",
    "maxRate": "20.00",
    "period": "7",
    "productMinAmount": "0.00100000",
    "availableBalance": "788",
    "userAmount": "500.00000000",
    "remainingAmount": "400.00000000",
    "profitPrecision": "8",
    "subscribePrecision": "8"
  }
}
```

## 鲨鱼鳍申购

`POST /api/v3/earn/sharkfin/subscribe`

限频规则: 10次/秒/UID

鲨鱼鳍申购。

Operation ID: `sharkfinSubscribe`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| productId | string | 是 | 产品Id |
| amount | string | 是 | 申购金额 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | 申购成功订单Id |
| data.status | string |  | 订单状态 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1696751519392,
  "data": {
    "orderId": "123123123",
    "status": "2000.000000"
  }
}
```

## 鲨鱼鳍申购结果

`GET /api/v3/earn/sharkfin/subscribe-result`

限频规则: 5次/秒/UID

获取鲨鱼鳍申购结果。

Operation ID: `getSharkfinSubscribeResult`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| orderId | query | string | 是 | 订单Id |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.result | string |  | 申购是否成功<br><br>`success` 成功<br><br>`fail` 失败 |
| data.msg | string |  | 只有失败时才会返回信息 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1696752594890,
  "data": {
    "result": "success",
    "msg": ""
  }
}
```