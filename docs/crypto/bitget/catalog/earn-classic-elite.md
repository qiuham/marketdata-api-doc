---
exchange: bitget
source_url: https://www.bitget.com/docs/catalog/earn-classic-elite
api_type: REST
updated_at: 2026-11-18 19:01:28.409625
---

# Classic On-chain Elite Earn

Classic account on-chain Elite product, subscription, redemption, and record APIs.

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v2/earn/elite/product` — Get Elite Product
- `POST /api/v2/earn/elite/subscribe` — Elite Subscribe
- `GET /api/v2/earn/elite/subscribe-result` — Get Elite Subscribe Result
- `GET /api/v2/earn/elite/subscribe-info` — Get Elite Subscribe Info
- `POST /api/v2/earn/elite/redeem` — Elite Redeem
- `GET /api/v2/earn/elite/redeem-info` — Get Redeem Info
- `GET /api/v2/earn/elite/assets` — Get Elite Assets
- `GET /api/v2/earn/elite/records` — Get Elite Records

## Get Elite Product

`GET /api/v2/earn/elite/product`

Query On-Chain Selected Product List

- Rate limit:  5/sec/UID

- Permission: Spot Trading. (Read Only)

Operation ID: `classicEarnEliteGetEliteProduct`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].productId | string |  | Product ID |
| data[].coin | string |  | Coin name |
| data[].minApr | string |  | Minimum APR,<br><br> in percentage format, e.g. 1.50 means 1.5% |
| data[].maxApr | string |  | Maximum APR,<br><br> in percentage format, e.g. 1.50 means 1.5% |
| data[].subscriptionCoinList | object[] |  | List of subscription coins |
| data[].subscriptionCoinList[].subscriptionCoin | string |  | Subscription coin |
| data[].subscriptionCoinList[].precision | string |  | Subscription precision,<br><br> positive integer. 1 means 1 decimal place |
| data[].subscriptionCoinList[].feeRate | string |  | Fee rate |
| data[].subscriptionCoinList[].exchangeRate | string |  | Exchange rate,<br><br> in decimal format |
| data[].sellOut | string |  | Whether sold out:<br><br> `YES` Sold out <br><br> `NO` Not sold out |

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

## Elite Subscribe

`POST /api/v2/earn/elite/subscribe`

Perform On-Chain Selected Product Subscription

- Rate limit:  5/sec/UID

- Permission: Spot Trading. (Read & Write)

Operation ID: `classicEarnEliteEliteSubscribe`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| productSubId | string | 是 | Product sub-ID |
| amount | string | 是 | Subscription amount |
| coin | string |  | Subscription coin.<br><br> Required when subscribing to BGUSD. Can be USDT or USDC;<br><br> classic accounts support subscription with USDT/USDC; unified accounts only support subscription with USDC |
| paymentAccount | string |  | Debit account:<br><br> `spot` Funding account;<br><br> `unified` Unified account (supported only in unified account mode); <br><br>if not provided, the default is the funding account |

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

`GET /api/v2/earn/elite/subscribe-result`

Query On-Chain Selected Subscription Result

- Rate limit:  5/sec/UID

- Permission: Spot Trading. (Read Only)

Operation ID: `classicEarnEliteGetEliteSubscribeResult`

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
| data.result | string |  | Subscription result:<br><br> `settled` Subscription successful;<br><br> `pending` Subscription in progress;<br><br> `rejected` Subscription failed |

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

## Get Elite Subscribe Info

`GET /api/v2/earn/elite/subscribe-info`

Query On-Chain Selected Subscription Details

- Rate limit:  5/sec/UID

- Permission: Spot Trading. (Read Only)

Operation ID: `classicEarnEliteGetEliteSubscribeInfo`

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
| data.exchangeRate | string |  | Exchange rate,<br><br> only applicable to BGBTC / BGSOL |
| data.productCoin | string |  | Product coin |
| data.interestTime | string |  | Interest accrual start time in Unix milliseconds;<br><br> only applicable to BGUSD / BGBTC |
| data.settleTime | string |  | Interest distribution time in Unix milliseconds;<br><br> only applicable to BGUSD / BGBTC |
| data.precision | string |  | Subscription yield precision,<br><br> positive integer. 1 means 1 decimal place |
| data.feeRate | string |  | Fee rate |
| data.subscriptionCoinList | object[] |  | List of subscription coins,<br><br> only applicable to BGUSD |
| data.subscriptionCoinList[].subscriptionCoin | string |  | Subscription coin |
| data.subscriptionCoinList[].remainQuota | string |  | Remaining subscription quota |
| data.subscriptionCoinList[].precision | string |  | Subscription precision,<br><br> positive integer. 1 means 1 decimal place |
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

## Elite Redeem

`POST /api/v2/earn/elite/redeem`

Perform On-Chain Selected Redemption

- Rate limit:  5/sec/UID

- Permission: Spot Trading. (Read & Write)

Operation ID: `classicEarnEliteEliteRedeem`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| productId | string | 是 | Product ID |
| productSubId | string | 是 | Product sub-ID |
| redeemType | string | 是 | Redemption type<br><br>`fast` Fast redemption<br><br>`standard` Standard redemption - BGUSD supports both fast and standard redemption; BGSOL/BGBTC only support standard redemption |
| amount | string | 是 | Subscription amount |
| receiveAccount | string | 是 | Crediting account type<br><br>- `spot` Funding account<br><br>- `unified` Unified account (supported only in unified account mode) |
| advancedSettle | string |  | Whether to redeem early<br><br>`yes` Yes<br><br>`no` No<br><br>Default value: `no`<br><br>Only applicable to BGBTC |
| coin | string |  | Subscription currency - Required for BGUSD |

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

## Get Redeem Info

`GET /api/v2/earn/elite/redeem-info`

Query On-Chain Selected Redemption Information

- Rate limit:  5/sec/UID

- Permission: Spot Trading. (Read Only)

Operation ID: `classicEarnEliteGetRedeemInfo`

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
| data.exchangeRate | string |  | Exchange rate,<br><br> used for BGBTC/BGSOL |
| data.totalUnPayInterestAmount | string |  | Total undistributed interest amount |
| data.preSettleApr | string |  | Early settlement APR |
| data.receivedCoin | string |  | Credited coin,<br><br> used for BGBTC/BGSOL |
| data.unsettledPoints | string |  | Unsettled points,<br><br> available for BGBTC |
| data.bgusdReceiveCoinList | object[] |  | List of BGUSD credited coins,<br><br> used for BGUSD |
| data.bgusdReceiveCoinList[].bgusdReceiveCoin | string |  | BGUSD credited coin, <br><br>used for BGUSD |
| data.bgusdReceiveCoinList[].bgusdExchangeRate | string |  | BGUSD exchange rate, <br><br>available for BGUSD |
| data.redeemModeList | object[] |  | Redemption mode list |
| data.redeemModeList[].redeemFeeRate | string |  | Redemption fee rate |
| data.redeemModeList[].remainQuota | string |  | Remaining quota |
| data.redeemModeList[].redeemType | string |  | Redemption type:<br><br> `fast` Fast redemption;<br><br> `standard` Standard redemption |
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

## Get Elite Assets

`GET /api/v2/earn/elite/assets`

Query On-Chain Selected Asset Information

- Rate limit:  5/sec/UID

- Permission: Spot Trading. (Read Only)

Operation ID: `classicEarnEliteGetEliteAssets`

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
| data.resultList[].apr | string |  | Annualized yield in percentage format,<br><br> e.g. 4.20 means 4.20%;<br><br> applicable to BGSOL / BGBTC |
| data.resultList[].minApy | string |  | Minimum APY,<br><br> only applicable to BGUSD |
| data.resultList[].maxApy | string |  | Maximum APY,<br><br> only applicable to BGUSD |
| data.resultList[].subscriptionCoin | string |  | Subscription coin |
| data.resultList[].exchangeAmount | string |  | Exchange amount |
| data.resultList[].projectList | object[] |  | Project list,<br><br> only applicable to BGBTC |
| data.resultList[].projectList[].projectName | string |  | Project name,<br><br> only applicable to BGBTC |
| data.resultList[].unsettledBGPoints | string |  | Unsettled BG points,<br><br> only applicable to BGBTC |
| data.resultList[].interestCoin | string |  | Interest distribution coin,<br><br> only applicable to BGUSD |
| data.resultList[].totalProfit | string |  | Cumulative profit,<br><br> only applicable to BGUSD |

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

`GET /api/v2/earn/elite/records`

Query On-Chain Selected History

- Rate limit:  5/sec/UID

- Permission: Spot Trading. (Read Only)

Operation ID: `classicEarnEliteGetEliteRecords`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| startTime | query | string |  | Start timestamp in Unix milliseconds,<br><br> e.g. 1597026383085;<br><br> the maximum time range supported is three months; <br><br>if not provided, the default end time is three months |
| endTime | query | string |  | End timestamp in Unix milliseconds,<br><br> e.g. 1597026383085 |
| limit | query | string |  | Number of records to query, <br><br>default is 20, maximum is 100 |
| cursor | query | string |  | Cursor ID.<br><br> Request paginated content after this ID (updated data); the value passed should be the `endId` from the corresponding API |
| type | query | string | 是 | Record type:<br><br> `subscribe` Subscription;<br><br> `redeem` Redemption;<br><br> `interest` Interest distribution |

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
| data.recordList[].status | string |  | Order status. <br><br>Subscription:<br><br> `settled` Subscription successful,<br><br> `pending` Subscription in progress, <br><br>`rejected` Subscription failed;<br><br> Redemption: <br><br>`settled` Redemption successful, <br><br>`pending` Redemption in progress;<br><br> Interest distribution:<br><br> `settled` Interest distribution successful,<br><br> `pending` Interest distribution in progress |
| data.recordList[].exchangeRate | string |  | Exchange rate |
| data.recordList[].receivedCoin | string |  | Received coin |
| data.recordList[].receivedAmount | string |  | Received amount |
| data.recordList[].investAmount | string |  | Investment amount |
| data.recordList[].feeRate | string |  | Fee rate |
| data.recordList[].redeemType | string |  | Redemption type:<br><br> `fast` Fast redemption;<br><br> `standard` Standard redemption |
| data.recordList[].receivingAccount | string |  | Redemption account:<br><br> `spot` Funding account;<br><br> `unified` Unified account (supported only in unified account mode); <br><br>returned only when `type=redeem` |
| data.recordList[].actualReceivingAccount | string |  | Actual redemption account:<br><br> `spot` Funding account;<br><br> `unified` Unified account (supported only in unified account mode);<br><br> returned only when `type=redeem` |
| data.recordList[].paymentAccount | string[] |  | Payment account: <br><br>`spot` Funding account;<br><br> `unified` Unified account (supported only in unified account mode);<br><br> returned only when `type=subscribe` |
| data.recordList[].settlePoints | string |  | Settled points,<br><br> returned only for BGBTC when `type=interest` |
| data.recordList[].fee | string |  | Fee, <br><br>only applicable to `type=redeem` & `type=subscribe` |
| data.endId | string |  | End ID for pagination |

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
        "fee": "0"
      }
    ],
    "endId": "1421055235278839808"
  }
}
```


---

经典账户链上精选产品、申购、赎回与记录接口。

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v2/earn/elite/product` — 获取链上精选产品列表
- `POST /api/v2/earn/elite/subscribe` — 链上精选申购
- `GET /api/v2/earn/elite/subscribe-result` — 获取链上精选申购结果
- `GET /api/v2/earn/elite/subscribe-info` — 获取链上精选申购详情
- `POST /api/v2/earn/elite/redeem` — 链上精选赎回
- `GET /api/v2/earn/elite/redeem-info` — 获取链上精选赎回信息
- `GET /api/v2/earn/elite/assets` — 获取链上精选资产信息
- `GET /api/v2/earn/elite/records` — 获取链上精选历史记录

## 获取链上精选产品列表

`GET /api/v2/earn/elite/product`

查询链上精选产品列表。

- 限频: 5次/s

- 权限:

- - 现货 - 交易 - 只读

Operation ID: `classicEarnEliteGetEliteProduct`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].productId | string |  | 产品ID |
| data[].coin | string |  | 币种名称 |
| data[].minApr | string |  | 最小年化收益  <br><br>百分比形式，如1.50代表1.5% |
| data[].maxApr | string |  | 最大年化收益   <br><br>百分比形式，如1.50代表1.5% |
| data[].subscriptionCoinList | object[] |  | 申购币种列表 |
| data[].subscriptionCoinList[].subscriptionCoin | string |  | 申购币种 |
| data[].subscriptionCoinList[].precision | string |  | 申购精度   <br><br>正整数。1代表精度为1位小数 |
| data[].subscriptionCoinList[].feeRate | string |  | 手续费率 |
| data[].subscriptionCoinList[].exchangeRate | string |  | 兑换率 <br><br>小数形式 |
| data[].sellOut | string |  | 是否已售罄 <br><br>`YES` 已售罄；<br><br>`NO` 未售罄; |

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

## 链上精选申购

`POST /api/v2/earn/elite/subscribe`

进行链上精选产品申购。

- 限频: 5次/s

- 权限:

- - 现货 - 交易 - 读写

Operation ID: `classicEarnEliteEliteSubscribe`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| productSubId | string | 是 | 产品子Id |
| amount | string | 是 | 申购金额 |
| coin | string |  | 申购币种<br><br> 申购 BGUSD 时必传，可传 USDT 或 USDC；<br><br>经典账户支持 USDT/USDC 申购；<br><br>统一账户仅支持 USDC 申购 |
| paymentAccount | string |  | 扣款账户<br><br> `spot` 资金账户；<br><br>`unified` 统一账户（仅统一账户模式下支持）；<br><br>如不填，默认为资金账户 |

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

`GET /api/v2/earn/elite/subscribe-result`

查询链上精选申购结果。

- 限频: 5次/s

- 权限:

- - 现货 - 交易 - 只读

Operation ID: `classicEarnEliteGetEliteSubscribeResult`

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
| data.result | string |  | 申购结果<br><br>  `settled` 申购成功；<br><br>`pending` 申购进行中；<br><br>`rejected` 申购失败; |

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

## 获取链上精选申购详情

`GET /api/v2/earn/elite/subscribe-info`

查询链上精选申购详情

- 限频: 5次/s

- 权限:

- - 现货 - 交易 - 只读

Operation ID: `classicEarnEliteGetEliteSubscribeInfo`

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
| data.exchangeRate | string |  | 兑换率  <br><br>仅适用于 BGBTC / BGSOL |
| data.productCoin | string |  | 产品币种 |
| data.interestTime | string |  | 起息时间 <br><br>Unix毫秒时间戳；<br><br>仅适用于 BGUSD / BGBTC |
| data.settleTime | string |  | 派息时间 <br><br> Unix毫秒时间戳；<br><br>仅适用于 BGUSD / BGBTC |
| data.precision | string |  | 申购收益精度 <br><br>正整数。1代表精度为1位小数 |
| data.feeRate | string |  | 手续费率 |
| data.subscriptionCoinList | object[] |  | 申购币种列表 <br><br>仅适用于 BGUSD |
| data.subscriptionCoinList[].subscriptionCoin | string |  | 申购币种 |
| data.subscriptionCoinList[].remainQuota | string |  | 剩余申购额度 |
| data.subscriptionCoinList[].precision | string |  | 申购精度 <br><br>正整数。1代表精度为1位小数 |
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

## 链上精选赎回

`POST /api/v2/earn/elite/redeem`

进行链上精选赎回。

- 限频: 5次/s

- 权限:

- - 现货 - 交易 - 读写

Operation ID: `classicEarnEliteEliteRedeem`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| productId | string | 是 | 产品Id |
| productSubId | string | 是 | 产品子Id |
| redeemType | string | 是 | 赎回类型<br><br>`fast`快速赎回<br><br>`standard`标准赎回 <br><br>- BGUSD支持快速赎回及标准赎回<br><br>- BGSOL/BGBTC仅支持标准赎回 |
| amount | string | 是 | 申购金额 |
| receiveAccount | string | 是 | 到账账户类型<br><br>- `spot`资金账户<br><br>- `unified`统一账户（仅统一账户模式下支持） |
| advancedSettle | string |  | 是否提前赎回<br><br>`yes`是<br><br>`no`否<br><br>默认值为`no`<br><br>仅BGBTC使用 |
| coin | string |  | 申购币种<br><br>- BGUSD必传 |

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

## 获取链上精选赎回信息

`GET /api/v2/earn/elite/redeem-info`

查询链上精选赎回信息。

- 限频: 5次/s

- 权限:

- - 现货 - 交易 - 只读

Operation ID: `classicEarnEliteGetRedeemInfo`

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
| data.exchangeRate | string |  | 兑换率 <br><br>BGBTC/BGSOL使用 |
| data.totalUnPayInterestAmount | string |  | 累计未发放收益 |
| data.preSettleApr | string |  | 提前结算APR |
| data.receivedCoin | string |  | 到账币种<br><br>BGBTC/BGSOL使用 |
| data.unsettledPoints | string |  | 未结算积分<br><br>BGBTC有值 |
| data.bgusdReceiveCoinList | object[] |  | BGUSD到账币种列表<br><br>BGUSD使用 |
| data.bgusdReceiveCoinList[].bgusdReceiveCoin | string |  | BGUSD到账币种<br><br>BGUSD使用 |
| data.bgusdReceiveCoinList[].bgusdExchangeRate | string |  | BGUSD兑换率<br><br>BGUSD有值 |
| data.redeemModeList | object[] |  | 赎回模式列表 |
| data.redeemModeList[].redeemFeeRate | string |  | 赎回手续费率 |
| data.redeemModeList[].remainQuota | string |  | 剩余额度 |
| data.redeemModeList[].redeemType | string |  | 赎回类型 <br><br> `fast` 快速赎回；<br><br>`standard` 标准赎回; |
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

## 获取链上精选资产信息

`GET /api/v2/earn/elite/assets`

查询链上精选资产信息。

- 限频: 5次/s

- 权限:

- - 现货 - 交易 - 只读

Operation ID: `classicEarnEliteGetEliteAssets`

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
| data.resultList[].apr | string |  | 年化收益率<br><br>百分比形式，如4.20代表4.20%；<br><br>适用于 BGSOL / BGBTC |
| data.resultList[].minApy | string |  | 最小年化收益率<br><br>仅适用于 BGUSD |
| data.resultList[].maxApy | string |  | 最大年化收益率 <br><br>仅适用于 BGUSD |
| data.resultList[].subscriptionCoin | string |  | 申购币种 |
| data.resultList[].exchangeAmount | string |  | 兑换金额 |
| data.resultList[].projectList | object[] |  | 项目列表 <br><br>仅适用于 BGBTC |
| data.resultList[].projectList[].projectName | string |  | 项目名称 <br><br>仅适用于 BGBTC |
| data.resultList[].unsettledBGPoints | string |  | 未结算BG积分<br><br>仅适用于 BGBTC |
| data.resultList[].interestCoin | string |  | 派息币种<br><br>仅适用于 BGUSD |
| data.resultList[].totalProfit | string |  | 累计收益<br><br>仅适用于 BGUSD |

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

`GET /api/v2/earn/elite/records`

查询链上精选历史记录。

- 限频: 5次/s

- 权限:

- - 现货 - 交易 - 只读

Operation ID: `classicEarnEliteGetEliteRecords`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| startTime | query | string |  | 开始时间戳<br><br> Unix毫秒时间戳，如1597026383085；时间跨度最大支持三个月；<br><br>若不传，则默认结束时间为三个月 |
| endTime | query | string |  | 结束时间戳<br><br>Unix毫秒时间戳，如1597026383085 |
| limit | query | string |  | 查询条数<br><br>默认20，最大100 |
| cursor | query | string |  | 游标ID <br><br>请求此ID之后（更新的数据）的分页内容，传的值为对应接口的 endId |
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
| data.recordList[].status | string |  | 订单状态<br><br>申购：<br><br>`settled` 申购成功<br><br>  `pending` 申购进行中<br><br> `rejected`申购失败；<br><br>赎回：<br><br>`settled` 赎回成功<br><br> `pending`赎回进行中；<br><br>派息：<br><br>`settled`派息成功<br><br>  `pending`派息中 |
| data.recordList[].exchangeRate | string |  | 兑换率 |
| data.recordList[].receivedCoin | string |  | 接收币种 |
| data.recordList[].receivedAmount | string |  | 接收金额 |
| data.recordList[].investAmount | string |  | 投资金额 |
| data.recordList[].feeRate | string |  | 手续费率 |
| data.recordList[].redeemType | string |  | 赎回类型<br><br>`fast` 快速赎回；<br><br>`standard` 标准赎回 |
| data.recordList[].receivingAccount | string |  | 赎回账户  <br><br>   `spot` 资金账户；<br><br>`unified` 统一账户（仅统一账户模式下支持）；<br><br>仅在 `type=redeem` 时返回 |
| data.recordList[].actualReceivingAccount | string |  | 实际赎回账户<br><br>      `spot` 资金账户；<br><br>`unified` 统一账户（仅统一账户模式下支持）；<br><br>仅在 `type=redeem` 时返回 |
| data.recordList[].paymentAccount | string[] |  | 付款账户 <br><br>   `spot` 资金账户；<br><br>`unified` 统一账户（仅统一账户模式下支持）；<br><br>仅在 `type=subscribe` 时返回 |
| data.recordList[].settlePoints | string |  | 结算积分 <br><br>仅在 BGBTC 且 `type=interest` 时返回 |
| data.recordList[].fee | string |  | 手续费  <br><br>仅适用于`type=redeem`&`type=subscribe` |
| data.endId | string |  | 分页结束ID |

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
        "fee": "0"
      }
    ],
    "endId": "1421055235278839808"
  }
}
```