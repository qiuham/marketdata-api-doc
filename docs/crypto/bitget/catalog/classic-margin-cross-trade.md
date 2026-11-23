---
exchange: bitget
source_url: https://www.bitget.com/docs/catalog/classic-margin-cross-trade
api_type: REST
updated_at: 2026-11-23 19:02:32.513017
---

# Classic Cross Margin Trade API

Classic account — cross margin order placement & queries.

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `POST /api/v2/margin/crossed/place-order` — Cross Place Order
- `POST /api/v2/margin/crossed/batch-place-order` — Cross Batch Orders
- `POST /api/v2/margin/crossed/cancel-order` — Cross Cancel Order
- `POST /api/v2/margin/crossed/batch-cancel-order` — Cross Batch Cancel Orders
- `GET /api/v2/margin/crossed/open-orders` — Get Cross Current Orders
- `GET /api/v2/margin/crossed/history-orders` — Get Cross History Orders
- `GET /api/v2/margin/crossed/fills` — Get Cross Order Fills
- `GET /api/v2/margin/crossed/liquidation-order` — Get Cross Liquidation Orders

## Cross Place Order

`POST /api/v2/margin/crossed/place-order`

Rate Limit: 10 req/sec/UID

Operation ID: `classicMarginCrossTradeCrossPlaceOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string | 是 | Trading pairs, like BTCUSDT |
| orderType | string | 是 | Order type<br><br>limit: limit price<br><br>market: market price |
| price | string |  | Price |
| loanType | string | 是 | Margin order model<br><br>normal: place a normal order<br><br>autoLoan place an order with auto-borrow<br><br>autoRepay place an order with auto-repay<br><br>autoLoanAndRepay place an order with auto-borrow and auto-repay |
| force | string | 是 | Time in force (invalid when `orderType` is `market`)<br><br>gtc: Normal limit order, good till canceled<br><br>post_only: Post only<br><br>fok: Fill or kill<br><br>ioc: Immediate or cancel |
| baseSize | string |  | Must fill limit and market sell. Sell order presents quantity of based currency (the left coin). |
| quoteSize | string |  | Must fill market buy. Buy order presents quantity of quote currency (the right coin). |
| clientOid | string |  | Customized ID<br><br>The idempotency time is 6 hours, only valid when orders are unfilled. |
| side | string | 是 | Direction<br><br>sell: Sell<br><br>buy: Buy |
| stpMode | string |  | STP Mode, default `none` <br><br> `none` not setting STP <br><br> `cancel_taker` cancel taker order <br><br>  `cancel_maker` cancel maker order <br><br>  `cancel_both` cancel both of taker and maker orders |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | Order ID |
| data.clientOid | string |  | Customized ID |

```json
{
  "code": "00000",
  "data": {
    "orderId": "121211212122",
    "clientOid": "121211212122"
  },
  "msg": "success",
  "requestTime": 1627293504612
}
```

## Cross Batch Orders

`POST /api/v2/margin/crossed/batch-place-order`

Frequency limit:10 times/1s (UID)

Operation ID: `classicMarginCrossTradeCrossBatchOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string | 是 | Trading pairs, like BTCUSDT |
| orderList | string[] | 是 | Order entries |
| orderType | string | 是 | Order type<br><br>limit: limit price<br><br>market: market price |
| price | string |  | Price |
| loanType | string | 是 | Margin order model<br><br>normal: place a normal order<br><br>autoLoan place an order with auto-borrow<br><br>autoRepay place an order with auto-repay<br><br>autoLoanAndRepay place an order with auto-borrow and auto-repay |
| force | string | 是 | Time in force (invalid when `orderType` is `market`)<br><br>gtc: normal limit order, good till canceled<br><br>post_only: Post only<br><br>fok: Fill or kill<br><br>ioc: Immediate or cancel |
| baseSize | string |  | Must fill limit and market sell. Sell order presents quantity of based currency (the left coin). |
| quoteSize | string |  | Must fill market buy. Buy order presents quantity of quote currency (the right coin). |
| clientOid | string |  | Customized ID |
| side | string | 是 | Direction<br><br>sell: Sell<br><br>buy: Buy |
| stpMode | string |  | STP Mode, default `none` <br><br> `none` not setting STP <br><br> `cancel_taker` cancel taker order <br><br>  `cancel_maker` cancel maker order <br><br>  `cancel_both` cancel both of taker and maker orders |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.successList | object[] |  | Successful order array |
| data.successList[].orderId | string |  | Order ID |
| data.successList[].clientOid | string |  | Client customized ID |
| data.failureList | object[] |  | Failed order array |
| data.failureList[].clientOid | string |  | Client customized ID |
| data.failureList[].errorMsg | string |  | Error information |

```json
{
  "code": "00000",
  "data": {
    "successList": [
      {
        "orderId": "121211212122",
        "clientOid": "121211212122"
      }
    ],
    "failureList": [
      {
        "clientOid": "121211212122",
        "errorMsg": "Order Cancelled"
      }
    ]
  },
  "msg": "success",
  "requestTime": 1627293504612
}
```

## Cross Cancel Order

`POST /api/v2/margin/crossed/cancel-order`

Frequency limit:10 times/1s (UID)

Operation ID: `classicMarginCrossTradeCrossCancelOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string | 是 | Trading pairs, like BTCUSDT |
| orderId | string |  | Order ID<br><br>Either orderId or clientOid |
| clientOid | string |  | Client customized ID<br><br>Either orderId or clientOid |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | Order ID |
| data.clientOid | string |  | Customized ID |

```json
{
  "code": "00000",
  "data": {
    "orderId": "121211212122",
    "clientOid": "BITGET#121211212122"
  },
  "msg": "success",
  "requestTime": 1627293504612
}
```

## Cross Batch Cancel Orders

`POST /api/v2/margin/crossed/batch-cancel-order`

Frequency limit:10 times/1s (UID)

Operation ID: `classicMarginCrossTradeCrossBatchCancelOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string | 是 | Trading pairs, like BTCUSDT |
| orderIdList | object[] | 是 | Order ID list <br><br>Either orderId or clientOid |
| orderIdList[].orderId | string |  | Order ID <br><br>Either orderId or clientOid |
| orderIdList[].clientOid | string |  | Client customized ID  <br><br>Either orderId or clientOid |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.successList | object[] |  | Successful order array |
| data.successList[].orderId | string |  | Order ID |
| data.successList[].clientOid | string |  | Client customized ID |
| data.failureList | object[] |  | Failed order array |
| data.failureList[].orderId | string |  | Order ID |
| data.failureList[].clientOid | string |  | Client customized ID |
| data.failureList[].errorMsg | string |  | Error information |

```json
{
  "code": "00000",
  "data": {
    "successList": [
      {
        "orderId": "121211212122",
        "clientOid": "BITGET#121211212122"
      }
    ],
    "failureList": [
      {
        "orderId": "121211212122",
        "clientOid": "BITGET#121211212122",
        "errorMsg": "Order Cancelled"
      }
    ]
  },
  "msg": "success",
  "requestTime": 1627293504612
}
```

## Get Cross Current Orders

`GET /api/v2/margin/crossed/open-orders`

Frequency limit:10 times/1s (UID)

Operation ID: `classicMarginCrossTradeGetCrossOpenOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Trading pairs, like BTCUSDT |
| orderId | query | string |  | Order ID |
| clientOid | query | string |  | Client customized ID |
| startTime | query | string | 是 | Start time, Unix millisecond timestamp |
| endTime | query | string |  | End time, Unix millisecond timestamp |
| limit | query | string |  | Number of quiries<br><br>Default: 100 entries |
| idLessThan | query | string |  | For turning pages. The first query is not passed. When querying data in the second page and the data beyond, the last loanId returned in the last query is used, and the result will return data with a value less than this one; the query response time will be shortened. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderList | object[] |  | Order list |
| data.orderList[].symbol | string |  | Trading pair |
| data.orderList[].orderId | string |  | Order no. |
| data.orderList[].clientOid | string |  | Client customized ID |
| data.orderList[].size | string |  | Filled quantity |
| data.orderList[].priceAvg | string |  | Order price |
| data.orderList[].amount | string |  | Filled quantity |
| data.orderList[].force | string |  | Order bot<br><br>gtc: normal limit order, good till canceled<br><br>post_only: Post only<br><br>fok: Fill or kill<br><br>ioc: Immediate or cancel |
| data.orderList[].price | string |  | Order price |
| data.orderList[].enterPointSource | string |  | Order source<br><br>WEB: Orders created on the website<br><br>API: Orders created on API<br><br>SYS: System managed orders, usually generated by forced liquidation logic<br><br>ANDROID: Orders created on the Android app<br><br>IOS: Orders created on the iOS app |
| data.orderList[].status | string |  | Order status<br><br>`live`: New order<br><br>`partially_fill`: Partially filled<br><br>`filled`: Fully filled<br><br>`cancelled`: Cancelled<br><br>`reject`: Rejected |
| data.orderList[].side | string |  | Direction<br><br>`sell`: Sell<br><br>`buy`: Buy<br><br>`liquidation-buy`: Settlement – buy<br><br>`liquidation-sell`: Settlement – sell<br><br>`systemRepay-buy`: Repay by system – buy<br><br>`systemRepay-selll`:  Repay by system – sell |
| data.orderList[].baseSize | string |  | Quantity of the base currency |
| data.orderList[].quoteSize | string |  | Quantity of the quote currency |
| data.orderList[].orderType | string |  | Order type<br><br>limit: limit price<br><br>market: market price |
| data.orderList[].cTime | string |  | Creation time |
| data.orderList[].uTime | string |  | Updated time |
| data.orderList[].loanType | string |  | Margin order model<br><br>normal: place a normal order<br><br>autoLoan place an order with auto-borrow<br><br>autoRepay place an order with auto-repay<br><br>autoLoanAndRepay place an order with auto-borrow and auto-repay |
| data.maxId | string |  | Max ID of current search result |
| data.minId | string |  | Min ID of current search result, use: `idLessThan=minId` in the next query |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695636829522,
  "data": {
    "orderList": [
      {
        "orderId": "121211212122",
        "symbol": "BTCUSDT",
        "orderType": "limit",
        "enterPointSource": "API",
        "clientOid": "myClientOid001",
        "loanType": "normal",
        "price": "32111",
        "side": "buy",
        "status": "live",
        "baseSize": "0.01",
        "quoteSize": "1000",
        "priceAvg": "32111",
        "size": "0.01",
        "amount": "1000",
        "force": "gtc",
        "cTime": "1695629859821",
        "uTime": "1695629890839"
      }
    ],
    "maxId": "1",
    "minId": "1"
  }
}
```

## Get Cross History Orders

`GET /api/v2/margin/crossed/history-orders`

Rate limit:10 req/sec/UID

You can export your historical orders on our <a href="https://www.bitget.com/asset/export/downOrders">web</a>.

Operation ID: `classicMarginCrossTradeGetCrossOrderHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Trading pairs, like BTCUSDT |
| orderId | query | string |  | Order ID |
| enterPointSource | query | string |  | Order source<br><br>WEB: Orders created on the website<br><br>API: Orders created on API<br><br>SYS: System managed orders, usually generated by forced liquidation logic<br><br>ANDROID: Orders created on the Android app<br><br>IOS: Orders created on the iOS app |
| clientOid | query | string |  | Client customized ID |
| startTime | query | string | 是 | Start time, Unix millisecond timestamp |
| endTime | query | string |  | End time, Unix millisecond timestamp<br><br>Maximum interval between start time and end time is 90 days |
| limit | query | string |  | Number of quiries<br><br>Default: 100, maximum: 500 |
| idLessThan | query | string |  | For turning pages<br><br>It's not needed in the first query. When querying data in the second page and the data beyond, the last endId returned in the last query is used, and the result will return data with a value less than this one; the query response time will be shortened. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderList | object[] |  | Order list |
| data.orderList[].symbol | string |  | Trading pair |
| data.orderList[].orderId | string |  | Order ID |
| data.orderList[].clientOid | string |  | Client customized ID |
| data.orderList[].size | string |  | Filled quantity |
| data.orderList[].priceAvg | string |  | Order price |
| data.orderList[].amount | string |  | Filled volume |
| data.orderList[].force | string |  | Time in force<br><br>`gtc`: normal limit order, good till canceled<br><br>`post_only`: Post only<br><br>`fok`: Fill or kill<br><br>`ioc`: Immediate or cancel |
| data.orderList[].price | string |  | Order price |
| data.orderList[].enterPointSource | string |  | Order source<br><br>WEB: Orders created on the website<br><br>API: Orders created on API<br><br>SYS: System managed orders, usually generated by forced liquidation logic<br><br>ANDROID: Orders created on the Android app<br><br>IOS: Orders created on the iOS app |
| data.orderList[].status | string |  | Order status<br><br>`live`: New order<br><br>`partially_fill`: Partially filled<br><br>`filled`: Fully filled<br><br>`cancelled`: Cancelled<br><br>`reject`: Rejected |
| data.orderList[].side | string |  | Direction<br><br>`sell`: Sell<br><br>`buy`: Buy<br><br>`liquidation-buy`: Settlement – buy<br><br>`liquidation-sell`: Settlement – sell<br><br>`systemRepay-buy`: Repay by system – buy<br><br>`systemRepay-selll`:  Repay by system – sell |
| data.orderList[].baseSize | string |  | Quantity of the base currency |
| data.orderList[].quoteSize | string |  | Quantity of the quote currency |
| data.orderList[].orderType | string |  | Order type<br><br>limit: limit price<br><br>market: market price |
| data.orderList[].cTime | string |  | Creation time |
| data.orderList[].uTime | string |  | Updated time |
| data.orderList[].loanType | string |  | Margin order model<br><br>normal: place a normal order<br><br>autoLoan place an order with auto-borrow<br><br>autoRepay place an order with auto-repay<br><br>autoLoanAndRepay place an order with auto-borrow and auto-repay |
| data.maxId | string |  | Max ID of current search result |
| data.minId | string |  | Min ID of current search result, use: `idLessThan=minId` in the next query |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695636829522,
  "data": {
    "orderList": [
      {
        "orderId": "121211212122",
        "symbol": "BTCUSDT",
        "orderType": "limit",
        "enterPointSource": "API",
        "clientOid": "myClientOid001",
        "loanType": "normal",
        "price": "32111",
        "side": "buy",
        "status": "filled",
        "baseSize": "0.01",
        "quoteSize": "1000",
        "priceAvg": "32111",
        "size": "0.01",
        "amount": "1000",
        "force": "gtc",
        "cTime": "1695629859821",
        "uTime": "1695629890839"
      }
    ],
    "maxId": "121211212122",
    "minId": "121211212122"
  }
}
```

## Get Cross Order Fills

`GET /api/v2/margin/crossed/fills`

Frequency limit:10 times/1s (UID)

You can export your historical orders on our <a href="https://www.bitget.com/asset/export/downOrders">web</a>.

Operation ID: `classicMarginCrossTradeGetCrossOrderFills`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Trading pairs, like BTCUSDT |
| orderId | query | string |  | Order ID |
| idLessThan | query | string |  | Match order ID, relative parameters of turning pages. The first query is not passed. When querying data in the second page and the data beyond, the last fillId returned in the last query is used, and the result will return data with a value less than this one; the query response time will be shortened. |
| startTime | query | string | 是 | Start time, Unix millisecond timestamp |
| endTime | query | string |  | End time, Unix millisecond timestamp<br><br>Maximum interval between start time and end time is 90 days |
| limit | query | string |  | Number of quiries<br><br>Default: 100, maximum: 500 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.fills | object[] |  | Fill list |
| data.fills[].orderId | string |  | Order no. |
| data.fills[].tradeId | string |  | Transaction detail ID |
| data.fills[].size | string |  | Filled quantity |
| data.fills[].priceAvg | string |  | Order price |
| data.fills[].amount | string |  | Filled quantity |
| data.fills[].side | string |  | Direction<br><br>sell: Sell<br><br>buy: Buy<br><br>liquidation_buy: Settlement – buy<br><br>liquidation_sell: Settlement – sell<br><br>system_repay_buy: Repay by system – buy<br><br>system_repay_sell:  Repay by system – sell |
| data.fills[].orderType | string |  | Order type<br><br>limit: limit price<br><br>market: market price |
| data.fills[].tradeScope | string |  | Trader tag<br><br>taker: Taker<br><br>maker: Maker |
| data.fills[].cTime | string |  | Creation time, millisecond timestamp |
| data.fills[].uTime | string |  | Update time, millisecond timestamp |
| data.fills[].feeDetail | object[] |  | Transaction fee details |
| data.fills[].feeDetail[].deduction | string |  | Discount or not |
| data.fills[].feeDetail[].feeCoin | string |  | Coin for transaction fee |
| data.fills[].feeDetail[].totalDeductionFee | string |  | Total discounted transaction fee |
| data.fills[].feeDetail[].totalFee | string |  | Total transaction fee |
| data.maxId | string |  | Max ID of current search result |
| data.minId | string |  | Min ID of current search result, use: `idLessThan=minId` in the next query |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695636829522,
  "data": {
    "fills": [
      {
        "orderId": "121211212122",
        "tradeId": "121211212122",
        "orderType": "limit",
        "side": "buy",
        "priceAvg": "32111",
        "size": "0.01",
        "amount": "1000",
        "tradeScope": "taker",
        "cTime": "1695629859821",
        "uTime": "1695629890839",
        "feeDetail": {
          "deduction": "yes",
          "feeCoin": "BGB",
          "totalDeductionFee": "-0.017118519726",
          "totalFee": "-0.017118519726"
        }
      }
    ],
    "maxId": "121211212122",
    "minId": "121211212122"
  }
}
```

## Get Cross Liquidation Orders

`GET /api/v2/margin/crossed/liquidation-order`

Frequency limit:10 times/1s (UID)

Operation ID: `classicMarginCrossTradeGetCrossLiquidationOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| type | query | string |  | Type<br><br>`swap`: swap <br><br> `place_order`: place order(default) |
| symbol | query | string |  | Trading pairs, like BTCUSDT <br><br>  This field only takes effect when `type=place_order` <br><br> Default all symbols |
| fromCoin | query | string |  | Swap from coin <br><br>  This field only takes effect when `type=swap` |
| toCoin | query | string |  | Swap to coin <br><br>  This field only takes effect when `type=swap` |
| startTime | query | string |  | Start time, Unix millisecond timestamp |
| endTime | query | string |  | End time, Unix millisecond timestamp<br><br>Maximum interval between start time and end time is 90 days |
| limit | query | string |  | Number of quiries<br><br>Default: 100, maximum: 500 |
| idLessThan | query | string |  | For turning pages. The first query is not passed. When querying data in the second page and the data beyond, the last endId returned in the last query is used, and the result will return data with a value less than this one; the query response time will be shortened. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.resultList | object[] |  | Result list |
| data.resultList[].orderId | string |  | Order no. |
| data.resultList[].symbol | string |  | Trading pair <br><br>  This field only takes effect when `type=place_order` |
| data.resultList[].orderType | string |  | Order type <br><br>market: market price <br><br>  This field only takes effect when `type=place_order` |
| data.resultList[].side | string |  | Direction<br><br>liquidation_sell: Settlement – sell<br><br>liquidation_buy: Settlement – buy <br><br>  This field only takes effect when `type=place_order` |
| data.resultList[].priceAvg | string |  | Filled price <br><br>  This field only takes effect when `type=place_order` |
| data.resultList[].price | string |  | Order price <br><br>  This field only takes effect when `type=place_order` |
| data.resultList[].fillSize | string |  | Filled quantity <br><br>  This field only takes effect when `type=place_order` |
| data.resultList[].size | string |  | Order quantity <br><br>  This field only takes effect when `type=place_order` |
| data.resultList[].amount | string |  | Filled amount <br><br>  This field only takes effect when `type=place_order` |
| data.resultList[].fromCoin | string |  | Conversion source currency <br><br>  This field only takes effect when `type=swap` |
| data.resultList[].fromSize | string |  | The size of conversion source currency <br><br>  This field only takes effect when `type=swap` |
| data.resultList[].toCoin | string |  | Conversion target currency <br><br>  This field only takes effect when `type=swap` |
| data.resultList[].toSize | string |  | The size of conversion target currency <br><br>  This field only takes effect when `type=swap` |
| data.resultList[].cTime | string |  | Creation time |
| data.resultList[].uTime | string |  | Updated time |
| data.idLessThan | string |  | Min ID of current search result, use: `idLessThan=idLessThan` in the next query |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1708654712083,
  "data": {
    "resultList": [
      {
        "symbol": "BTCUSDT",
        "orderType": "market",
        "side": "liquidation-sell",
        "priceAvg": "43024.762472",
        "price": "43024.762472",
        "fillSize": "1",
        "size": "1",
        "amount": "43024.762472",
        "orderId": "xxxx",
        "fromCoin": "",
        "toCoin": "",
        "fromSize": "",
        "toSize": "",
        "cTime": "1705474028200",
        "uTime": "1705474028398"
      }
    ],
    "idLessThan": "1131405566368010241"
  }
}
```


---

经典账户 — 全仓杠杆下单与订单查询。

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `POST /api/v2/margin/crossed/place-order` — 全仓下单
- `POST /api/v2/margin/crossed/batch-place-order` — 全仓批量下单
- `POST /api/v2/margin/crossed/cancel-order` — 全仓撤单
- `POST /api/v2/margin/crossed/batch-cancel-order` — 全仓批量撤单
- `GET /api/v2/margin/crossed/open-orders` — 获取全仓当前委托
- `GET /api/v2/margin/crossed/liquidation-order` — 获取全仓强平订单
- `GET /api/v2/margin/crossed/history-orders` — 获取全仓历史委托
- `GET /api/v2/margin/crossed/fills` — 获取全仓成交明细

## 全仓下单

`POST /api/v2/margin/crossed/place-order`

限速规则 10次/1s (UID)

Operation ID: `classicMarginCrossTradeCrossPlaceOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string | 是 | 交易对，如BTCUSDT |
| orderType | string | 是 | 订单类型<br><br>limit 限价<br><br>market 市价 |
| price | string |  | 价格 |
| loanType | string | 是 | 杠杆订单模式<br><br>normal        普通下单<br><br>autoLoan        自动借款下单<br><br>autoRepay        自动还款下单<br><br>autoLoanAndRepay        自动借款还款下单 |
| force | string | 是 | 订单策略（`orderType`为`market`时无效）<br><br>gtc  普通限价单，一直有效直至取消<br><br>post_only   只做maker订单<br><br>fok        全部成交或立即取消<br><br>ioc        立即成交并取消剩余 |
| baseSize | string |  | limit必填，market sell 必填，卖单代表baseCoin（左币）数量 |
| quoteSize | string |  | market buy必填，买单代表quote Coin（右币）数量 |
| clientOid | string |  | 自定义ID |
| side | string | 是 | 交易方向<br><br>sell 卖<br><br>buy 买 |
| stpMode | string |  | STP模式， default `none` <br><br> `none` 不设置STP <br><br> `cancel_taker` 取消taker单 <br><br>  `cancel_maker` 取消maker单 <br><br>  `cancel_both` 两者都取消 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | 订单ID |
| data.clientOid | string |  | 自定义ID |

```json
{
  "code": "00000",
  "data": {
    "orderId": "121211212122",
    "clientOid": "121211212122"
  },
  "msg": "success",
  "requestTime": 1627293504612
}
```

## 全仓批量下单

`POST /api/v2/margin/crossed/batch-place-order`

限速规则 5次/1s (UID)

Operation ID: `classicMarginCrossTradeCrossBatchOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string | 是 | 交易对，如BTCUSDT |
| orderList | string[] | 是 | 订单条目 |
| orderType | string | 是 | 订单类型<br><br>limit 限价<br><br>market 市价 |
| price | string |  | 价格 |
| loanType | string | 是 | 杠杆订单模式<br><br>normal        普通下单<br><br>autoLoan        自动借款下单<br><br>autoRepay        自动还款下单<br><br>autoLoanAndRepay        自动借款还款下单 |
| force | string | 是 | 订单策略（`orderType`为`market`时无效）<br><br>gtc  普通限价单，一直有效直至取消<br><br>post_only   只做maker订单<br><br>fok        全部成交或立即取消<br><br>ioc        立即成交并取消剩余 |
| baseSize | string |  | limit必填，market sell 必填，卖单代表baseCoin（左币）数量 |
| quoteSize | string |  | market buy必填，买单代表quote Coin（右币）数量 |
| clientOid | string |  | 自定义ID |
| side | string | 是 | 交易方向<br><br>sell 卖<br><br>buy 买 |
| stpMode | string |  | STP模式， default `none` <br><br> `none` 不设置STP <br><br> `cancel_taker` 取消taker单 <br><br>  `cancel_maker` 取消maker单 <br><br>  `cancel_both` 两者都取消 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.successList | object[] |  | 成功订单数组 |
| data.successList[].orderId | string |  | 订单ID |
| data.successList[].clientOid | string |  | 客户端自定义ID |
| data.failureList | object[] |  | 失败订单数组 |
| data.failureList[].clientOid | string |  | 客户端自定义ID |
| data.failureList[].errorMsg | string |  | 错误信息 |

```json
{
  "code": "00000",
  "data": {
    "successList": [
      {
        "orderId": "121211212122",
        "clientOid": "121211212122"
      }
    ],
    "failureList": [
      {
        "clientOid": "121211212122",
        "errorMsg": "Order Cancelled"
      }
    ]
  },
  "msg": "success",
  "requestTime": 1627293504612
}
```

## 全仓撤单

`POST /api/v2/margin/crossed/cancel-order`

限速规则 10次/1s (UID)

Operation ID: `classicMarginCrossTradeCrossCancelOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string | 是 | 交易对，如BTCUSDT |
| orderId | string |  | 订单ID<br><br>orderId和clientOid 二选一 |
| clientOid | string |  | 客户自定义ID<br><br>orderId和clientOid 二选一 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | 订单ID |
| data.clientOid | string |  | 自定义ID |

```json
{
  "code": "00000",
  "data": {
    "orderId": "121211212122",
    "clientOid": "BITGET#121211212122"
  },
  "msg": "success",
  "requestTime": 1627293504612
}
```

## 全仓批量撤单

`POST /api/v2/margin/crossed/batch-cancel-order`

限速规则 5次/1s (UID)

Operation ID: `classicMarginCrossTradeCrossBatchCancelOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string | 是 | 交易对，如BTCUSDT |
| orderIdList | object[] | 是 | 订单ID集合 <br><br>orderId和clientOid二选一 |
| orderIdList[].orderId | string |  | 订单ID <br><br>orderId和clientOid二选一 |
| orderIdList[].clientOid | string |  | 客户自定义ID <br><br>orderId和clientOid二选一 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.successList | object[] |  | 成功订单数组 |
| data.successList[].orderId | string |  | 订单ID |
| data.successList[].clientOid | string |  | 客户端自定义ID |
| data.failureList | object[] |  | 失败订单数组 |
| data.failureList[].orderId | string |  | 订单ID |
| data.failureList[].clientOid | string |  | 客户端自定义ID |
| data.failureList[].errorMsg | string |  | 错误信息 |

```json
{
  "code": "00000",
  "data": {
    "successList": [
      {
        "orderId": "121211212122",
        "clientOid": "BITGET#121211212122"
      }
    ],
    "failureList": [
      {
        "orderId": "121211212122",
        "clientOid": "BITGET#121211212122",
        "errorMsg": "Order Cancelled"
      }
    ]
  },
  "msg": "success",
  "requestTime": 1627293504612
}
```

## 获取全仓当前委托

`GET /api/v2/margin/crossed/open-orders`

限速规则 10次/1s (UID)

Operation ID: `classicMarginCrossTradeGetCrossOpenOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 交易对，如BTCUSDT |
| orderId | query | string |  | 订单ID |
| clientOid | query | string |  | 客户自定义ID |
| startTime | query | string | 是 | 开始时间，Unix毫秒时间戳 |
| endTime | query | string |  | 结束时间，Unix毫秒时间戳 |
| limit | query | string |  | 查询条数<br><br>默认值为 100 条 |
| idLessThan | query | string |  | 用于翻页。首次查询不传，查询第二页及后面的数据时，取上一次查询返回的最后一条loanId，结果会返回小于该值的数据；可以缩短查询响应时间 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderList | object[] |  | 订单列表 |
| data.orderList[].symbol | string |  | 交易对名称 |
| data.orderList[].orderId | string |  | 订单号 |
| data.orderList[].clientOid | string |  | 客户端自定义id |
| data.orderList[].size | string |  | 成交数量 |
| data.orderList[].priceAvg | string |  | 成交价格 |
| data.orderList[].amount | string |  | 成交金额 |
| data.orderList[].force | string |  | 订单策略<br><br>gtc  普通限价单，一直有效直至取消<br><br>post_only   只做maker订单<br><br>fok        全部成交或立即取消<br><br>ioc        立即成交并取消剩余 |
| data.orderList[].price | string |  | 委托价格 |
| data.orderList[].enterPointSource | string |  | 订单来源<br><br>WEB    WEB客户端<br><br>IOS    IOS客户端<br><br>ANDROID    Andriod客户端<br><br>API    API客户端<br><br>SYS    系统, 通常为爆仓 |
| data.orderList[].status | string |  | 订单状态<br><br>`live`: 新建订单<br><br>`partial_fill`：部分成交<br><br>`filled`：全部成交<br><br>`cancelled` ：已撤销<br><br>`reject`: 已拒绝 |
| data.orderList[].side | string |  | 交易方向<br><br>`sell`: 卖<br><br>`buy`: 买<br><br>`liquidation-buy`: 结算-买入<br><br>`liquidation-sell`: 结算-卖出<br><br>`systemRepay-buy` 系统还款-买入<br><br>`systemRepay-sell` 系统还款-卖出 |
| data.orderList[].baseSize | string |  | 基础币数量 |
| data.orderList[].quoteSize | string |  | 计价币数量 |
| data.orderList[].orderType | string |  | 订单类型<br><br>limit 限价<br><br>market 市价 |
| data.orderList[].cTime | string |  | 创建时间 |
| data.orderList[].uTime | string |  | 更新时间 |
| data.orderList[].loanType | string |  | 杠杆订单模式<br><br>normal        普通下单<br><br>autoLoan        自动借款下单<br><br>autoRepay        自动还款下单<br><br>autoLoanAndRepay        自动借款还款下单 |
| data.maxId | string |  | 当前查询结果中的最大ID |
| data.minId | string |  | 当前查询结果中的最小ID，下次查询时使用 `idLessThan=minId` |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695636829522,
  "data": {
    "orderList": [
      {
        "orderId": "121211212122",
        "symbol": "BTCUSDT",
        "orderType": "limit",
        "enterPointSource": "API",
        "clientOid": "myClientOid001",
        "loanType": "normal",
        "price": "32111",
        "side": "buy",
        "status": "live",
        "baseSize": "0.01",
        "quoteSize": "1000",
        "priceAvg": "32111",
        "size": "0.01",
        "amount": "1000",
        "force": "gtc",
        "cTime": "1695629859821",
        "uTime": "1695629890839"
      }
    ],
    "maxId": "121211212122",
    "minId": "121211212122"
  }
}
```

## 获取全仓强平订单

`GET /api/v2/margin/crossed/liquidation-order`

限速规则 10次/1s (UID)

Operation ID: `classicMarginCrossTradeGetCrossLiquidationOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| type | query | string |  | 强平类型 <br><br>`swap` <br><br> `place_order`(默认) |
| symbol | query | string |  | 交易对，如BTCUSDT <br><br>  该字段在 `type=place_order` 时返回数据 <br><br> 默认返回全部币对 |
| fromCoin | query | string |  | 兑换来源币种 <br><br>  该字段在 `type=swap` 时返回数据 |
| toCoin | query | string |  | 兑换目标币对 <br><br>  该字段在 `type=swap` 时返回数据 |
| startTime | query | string |  | 开始时间, Unix毫秒时间戳 |
| endTime | query | string |  | 结束时间，Unix毫秒时间戳<br><br>开始和结束时间的最大间隔为90天 |
| limit | query | string |  | 查询条数<br><br>默认值为100条，最大值为500条 |
| idLessThan | query | string |  | 用于翻页。首次查询不传，查询第二页及后面的数据时，取上一次查询返回的endId，结果会返回小于该值的数据；可以缩短查询响应时间 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.resultList | object[] |  | 结果列表 |
| data.resultList[].orderId | string |  | 订单号 |
| data.resultList[].symbol | string |  | 交易对名称 <br><br>  该字段在 `type=place_order` 时返回数据 |
| data.resultList[].orderType | string |  | 订单类型 <br><br>market 市价 <br><br>  该字段在 `type=place_order` 时返回数据 |
| data.resultList[].side | string |  | 交易方向 <br><br>liquidation_buy 结算-买入<br><br>liquidation_sell 结算-卖出 <br><br>  该字段在 `type=place_order` 时返回数据 |
| data.resultList[].priceAvg | string |  | 成交价格 <br><br>  该字段在 `type=place_order` 时返回数据 |
| data.resultList[].price | string |  | 委托价格 <br><br>  该字段在 `type=place_order` 时返回数据 |
| data.resultList[].fillSize | string |  | 成交数量 <br><br>  该字段在 `type=place_order` 时返回数据 |
| data.resultList[].size | string |  | 委托数量 <br><br>  该字段在 `type=place_order` 时返回数据 |
| data.resultList[].amount | string |  | 成交金额 <br><br>  该字段在 `type=place_order` 时返回数据 |
| data.resultList[].fromCoin | string |  | 兑换来源币种 <br><br> 该字段在 `type=swap` 时返回数据 |
| data.resultList[].fromSize | string |  | 兑换来源币种数量 <br><br>  该字段在 `type=swap` 时返回数据 |
| data.resultList[].toCoin | string |  | 兑换目标币种<br><br>  该字段在 `type=swap` 时返回数据 |
| data.resultList[].toSize | string |  | 兑换目标币种数量  <br><br>  该字段在 `type=swap` 时返回数据 |
| data.resultList[].cTime | string |  | 创建时间 |
| data.resultList[].uTime | string |  | 更新时间 |
| data.idLessThan | string |  | 当前查询结果中的最小ID，下次查询时使用 `idLessThan=idLessThan` |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1708654712083,
  "data": {
    "resultList": [
      {
        "symbol": "BTCUSDT",
        "orderType": "market",
        "side": "liquidation-sell",
        "priceAvg": "43024.762472",
        "price": "43024.762472",
        "fillSize": "1",
        "size": "1",
        "amount": "43024.762472",
        "orderId": "xxxx",
        "fromCoin": "",
        "toCoin": "",
        "fromSize": "",
        "toSize": "",
        "cTime": "1705474028200",
        "uTime": "1705474028398"
      }
    ],
    "idLessThan": "1131405566368010241"
  }
}
```

## 获取全仓历史委托

`GET /api/v2/margin/crossed/history-orders`

限速规则 10次/1s (UID)

您可以在网页端<a href="https://www.bitget.com/zh-CN/asset/export/downOrders">导出</a>历史订单。

Operation ID: `classicMarginCrossTradeGetCrossOrderHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 交易对，如BTCUSDT |
| orderId | query | string |  | 订单ID |
| enterPointSource | query | string |  | 订单来源<br><br>WEB    WEB客户端<br><br>IOS    IOS客户端<br><br>ANDROID    Andriod客户端<br><br>API    API客户端<br><br>SYS    系统, 通常为爆仓 |
| clientOid | query | string |  | 客户自定义ID |
| startTime | query | string | 是 | 开始时间, Unix毫秒时间戳 |
| endTime | query | string |  | 结束时间，Unix毫秒时间戳<br><br>开始和结束时间的最大间隔为90天 |
| limit | query | string |  | 查询条数<br><br>默认值为100条，最大值为500条 |
| idLessThan | query | string |  | 用于翻页。首次查询不传，查询第二页及后面的数据时，取上一次查询返回的endId，结果会返回小于该值的数据；可以缩短查询响应时间 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderList | object[] |  | 订单列表 |
| data.orderList[].symbol | string |  | 交易对名称 |
| data.orderList[].orderId | string |  | 订单号 |
| data.orderList[].clientOid | string |  | 客户端自定义id |
| data.orderList[].size | string |  | 成交数量 |
| data.orderList[].priceAvg | string |  | 成交价格 |
| data.orderList[].amount | string |  | 成交金额 |
| data.orderList[].force | string |  | 订单策略<br><br>gtc  普通限价单，一直有效直至取消<br><br>post_only   只做maker订单<br><br>fok        全部成交或立即取消<br><br>ioc        立即成交并取消剩余 |
| data.orderList[].price | string |  | 委托价格 |
| data.orderList[].enterPointSource | string |  | 订单来源<br><br>WEB    WEB客户端<br><br>IOS    IOS客户端<br><br>ANDROID    Andriod客户端<br><br>API    API客户端<br><br>SYS    系统, 通常为爆仓 |
| data.orderList[].status | string |  | 订单状态<br><br>`live`: 创建订单<br><br>`partial_fill`: 部分成交<br><br>`filled`: 全部成交<br><br>`cancelled`: 已撤销<br><br>`reject`: 已拒绝 |
| data.orderList[].side | string |  | 交易方向<br><br>`sell`: 卖<br><br>`buy`: 买<br><br>`liquidation-buy`: 结算-买入<br><br>`liquidation-sell`: 结算-卖出<br><br>`systemRepay-buy` 系统还款-买入<br><br>`systemRepay-sell` 系统还款-卖出 |
| data.orderList[].baseSize | string |  | 基础币数量 |
| data.orderList[].quoteSize | string |  | 计价币数量 |
| data.orderList[].orderType | string |  | 订单类型<br><br>limit 限价<br><br>market 市价 |
| data.orderList[].cTime | string |  | 创建时间 |
| data.orderList[].uTime | string |  | 更新时间 |
| data.orderList[].loanType | string |  | 杠杆订单模式<br><br>normal        普通下单<br><br>autoLoan        自动借款下单<br><br>autoRepay        自动还款下单<br><br>autoLoanAndRepay        自动借款还款下单 |
| data.maxId | string |  | 当前查询结果中的最大ID |
| data.minId | string |  | 当前查询结果中的最小ID，下次查询时使用 `idLessThan=minId` |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695636829522,
  "data": {
    "orderList": [
      {
        "orderId": "121211212122",
        "symbol": "BTCUSDT",
        "orderType": "limit",
        "enterPointSource": "API",
        "clientOid": "myClientOid001",
        "loanType": "normal",
        "price": "32111",
        "side": "buy",
        "status": "filled",
        "baseSize": "0.01",
        "quoteSize": "1000",
        "priceAvg": "32111",
        "size": "0.01",
        "amount": "1000",
        "force": "gtc",
        "cTime": "1695629859821",
        "uTime": "1695629890839"
      }
    ],
    "maxId": "121211212122",
    "minId": "121211212122"
  }
}
```

## 获取全仓成交明细

`GET /api/v2/margin/crossed/fills`

限速规则 10次/1s (UID)

您可以在网页端<a href="https://www.bitget.com/zh-CN/asset/export/downOrders">导出</a>历史订单。

Operation ID: `classicMarginCrossTradeGetCrossOrderFills`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 交易对，如BTCUSDT |
| orderId | query | string |  | 订单ID |
| idLessThan | query | string |  | 撮合ID, 翻页相关参数，首次查询不传，查询第二页及后面的数据时，取上一次查询返回的最后一条fillId，结果会返回小于该值的数据；可以缩短查询响应时间 |
| startTime | query | string | 是 | 开始时间，Unix毫秒时间戳 |
| endTime | query | string |  | 结束时间，Unix毫秒时间戳<br><br>开始和结束时间的最大间隔为90天 |
| limit | query | string |  | 查询条数<br><br>默认值为100条，最大值为500条 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.fills | object[] |  | 成交明细列表 |
| data.fills[].orderId | string |  | 订单号 |
| data.fills[].tradeId | string |  | 成交明细ID |
| data.fills[].size | string |  | 成交数量 |
| data.fills[].priceAvg | string |  | 成交价格 |
| data.fills[].amount | string |  | 成交金额 |
| data.fills[].side | string |  | 交易方向<br><br>sell 卖<br><br>buy 买<br><br>liquidation_buy 结算-买入<br><br>liquidation_sell 结算-卖出<br><br>system_repay_buy 系统还款-买入<br><br>system_repay_sell 系统还款-卖出 |
| data.fills[].orderType | string |  | 订单类型<br><br>limit 限价<br><br>market 市价 |
| data.fills[].tradeScope | string |  | 交易者标识<br><br>taker 吃单方<br><br>maker 挂单方 |
| data.fills[].cTime | string |  | 创建时间，毫秒时间戳 |
| data.fills[].uTime | string |  | 更新时间，毫秒时间戳 |
| data.fills[].feeDetail | object[] |  | 手续费明细 |
| data.fills[].feeDetail[].deduction | string |  | 是否折扣 |
| data.fills[].feeDetail[].feeCoin | string |  | 手续费币种 |
| data.fills[].feeDetail[].totalDeductionFee | string |  | 总计折扣手续费 |
| data.fills[].feeDetail[].totalFee | string |  | 总计手续费 |
| data.maxId | string |  | 当前查询结果中的最大ID |
| data.minId | string |  | 当前查询结果中的最小ID，下次查询时使用 `idLessThan=minId` |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695636829522,
  "data": {
    "fills": [
      {
        "orderId": "121211212122",
        "tradeId": "121211212122",
        "orderType": "limit",
        "side": "buy",
        "priceAvg": "32111",
        "size": "0.01",
        "amount": "1000",
        "tradeScope": "taker",
        "cTime": "1695629859821",
        "uTime": "1695629890839",
        "feeDetail": {
          "deduction": "yes",
          "feeCoin": "BGB",
          "totalDeductionFee": "-0.017118519726",
          "totalFee": "-0.017118519726"
        }
      }
    ],
    "maxId": "121211212122",
    "minId": "121211212122"
  }
}
```