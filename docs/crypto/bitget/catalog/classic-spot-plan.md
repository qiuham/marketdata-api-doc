---
exchange: bitget
source_url: https://www.bitget.com/docs/catalog/classic-spot-plan
api_type: REST
updated_at: 2026-11-22 19:01:11.532044
---

# Classic Spot Trigger API

Spot trigger (plan) order endpoints — place, modify, cancel, and query trigger orders.

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `POST /api/v2/spot/trade/place-plan-order` — Place Plan Order
- `POST /api/v2/spot/trade/modify-plan-order` — Modify Plan Order
- `POST /api/v2/spot/trade/cancel-plan-order` — Cancel Plan Order
- `POST /api/v2/spot/trade/batch-cancel-plan-order` — Cancel Plan Orders in Batch
- `GET /api/v2/spot/trade/current-plan-order` — Get Current Plan Orders
- `GET /api/v2/spot/trade/history-plan-order` — Get History Plan Orders
- `GET /api/v2/spot/trade/plan-sub-order` — Get Plan Sub Order

## Place Plan Order

`POST /api/v2/spot/trade/place-plan-order`

Frequency limit: 20 times/1s (UID)

Place plan order

- **API Broker rebate identifier**: The following code block needs to be added to the HTTP Header of the request.

  > "X-CHANNEL-API-CODE":"your-channel-api-code"

Operation ID: `classicSpotPlanPlacePlanOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string | 是 | Trading pair name, e.g. BTCUSDT |
| side | string | 是 | Direction<br><br>`buy`: Buy<br><br>`sell`: Sell |
| triggerPrice | string | 是 | Trigger price |
| orderType | string | 是 | Order type<br><br>`limit`: Limit orders<br><br>`market`: Market orders |
| executePrice | string |  | Execution price. It's required when `orderType`=`limit` |
| planType | string |  | Order type<br><br>`amount`: By amount of the order(base coin)<br><br>`total`: By trading volume of the order(quote coin)<br><br>The default value is `amount` |
| size | string | 是 | Quantity to buy. If `planType`=`amount`, it is the base coin. If `planType`=`total`, it is the quote coin. |
| triggerType | string | 是 | Trigger type<br><br>`fill_price`: filled price<br><br>`mark_price`: mark price |
| clientOid | string |  | Client customized ID |
| stpMode | string |  | STP Mode, default `none`<br><br>`none` not setting STP<br><br>`cancel_taker` cancel taker order<br><br>`cancel_maker` cancel maker order<br><br>`cancel_both` cancel both of taker and maker orders |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | Order ID |
| data.clientOid | string |  | Client customized ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1668134576535,
  "data": {
    "orderId": "121211212122",
    "clientOid": "121211212122"
  }
}
```

## Modify Plan Order

`POST /api/v2/spot/trade/modify-plan-order`

Frequency limit: 20 times/1s (UID)

Modify Plan Order

Operation ID: `classicSpotPlanModifyPlanOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderId | string |  | Either 'orderId' or 'clientOid' is required. |
| clientOid | string |  | Either 'orderId' or 'clientOid' is required. |
| triggerPrice | string | 是 | Trigger price |
| orderType | string | 是 | Order type<br><br>limit: Limit price<br><br>market: Market price |
| executePrice | string |  | Execution price, cannot be null if orderType=limit |
| size | string | 是 | Quantity to buy. If planType=amount, the quote currency is the base coin. If planType=total, the quote currency is the quote coin. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | Order ID |
| data.clientOid | string |  | Client customized ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1668134576535,
  "data": {
    "orderId": "121211212122",
    "clientOid": "121211212122"
  }
}
```

## Cancel Plan Order

`POST /api/v2/spot/trade/cancel-plan-order`

Frequency limit: 20 times/1s (UID)

Cancel Plan order

Operation ID: `classicSpotPlanCancelPlanOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderId | string |  | Either 'orderId' or 'clientOid' is required. |
| clientOid | string |  | Either 'orderId' or 'clientOid' is required. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.result | string |  | Result is success or failure |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1668134497496,
  "data": {
    "result": "success"
  }
}
```

## Cancel Plan Orders in Batch

`POST /api/v2/spot/trade/batch-cancel-plan-order`

Rate limit: 5 req/sec/UID

Cancel Plan Orders in Batch

Operation ID: `classicSpotPlanBatchCancelPlanOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbolList | string[] |  | Collection of trading pairs: ["BTCUSDT", "ETHUSDT"], If no value is set, all spot trigger orders will be cancelled. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.successList | object[] |  | The collection of successfully cancelled orders. |
| data.successList[].orderId | string |  | Order ID |
| data.successList[].clientOid | string |  | Customize order ID |
| data.failureList | object[] |  | The collection of unsuccessfully cancelled orders. |
| data.failureList[].orderId | string |  | Order ID |
| data.failureList[].clientOid | string |  | Customize order ID |
| data.failureList[].errorMsg | string |  | Failure reason |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1683876261117,
  "data": {
    "successList": [
      {
        "orderId": "121211212122",
        "clientOid": "121211212122"
      }
    ],
    "failureList": [
      {
        "orderId": "121211212122",
        "clientOid": "121211212122",
        "errorMsg": "failure"
      }
    ]
  }
}
```

## Get Current Plan Orders

`GET /api/v2/spot/trade/current-plan-order`

Frequency limit: 20 times/1s (UID)

Get Current Plan Orders

Operation ID: `classicSpotPlanGetCurrentPlanOrder`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | Trading pair, e.g. BTCUSDT |
| limit | query | string |  | Default is 20 Max is 100 |
| idLessThan | query | string |  | Requests the content on the page before this ID (older data), the value input should be the orderId of the corresponding interface. |
| startTime | query | string |  | The start time of the record for the query. Unix millisecond timestamp, e.g. 1690196141868. The startTime and endTime should be within 90 days. |
| endTime | query | string |  | The end time of the record for the query. Unix millisecond timestamp, e.g. 1690196141868. The startTime and endTime should be within 90 days. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.nextFlag | boolean |  | If Has next query data by idLessThan or not |
| data.idLessThan | string |  | Requests the content on the page before this ID (older data), the value input should be the endId of the corresponding interface. |
| data.orderList | object[] |  | Order List |
| data.orderList[].orderId | string |  | Order ID |
| data.orderList[].clientOid | string |  | Client customized ID |
| data.orderList[].symbol | string |  | Trading pair |
| data.orderList[].triggerPrice | string |  | Trigger price |
| data.orderList[].orderType | string |  | Order type<br><br>`limit`: limit order<br><br>`market`: market order |
| data.orderList[].executePrice | string |  | Execution price |
| data.orderList[].planType | string |  | Order type<br><br>`amount`: By amount of the order<br><br>`total`: By trading volume of the order |
| data.orderList[].size | string |  | Quantity to buy. If `placeType`=`amount`, the quote currency is the base coin. If `placeType`=`total`, the quote currency is the quote coin. |
| data.orderList[].status | string |  | Order status<br><br>`live`: not triggered<br><br>`executing`: order placing |
| data.orderList[].side | string |  | Direction `buy` or `sell` |
| data.orderList[].triggerType | string |  | Trigger type<br><br>`fill_price`: filled price<br><br>`mark_price`: mark price |
| data.orderList[].enterPointSource | string |  | Order source<br><br>`WEB`: Orders created on the website<br><br>`API`: Orders created on API<br><br>`SYS`: System managed orders, usually generated by forced liquidation logic<br><br>`ANDROID`: Orders created on the Android app<br><br>`IOS`: Orders created on the iOS app |
| data.orderList[].cTime | string |  | Creation time, Unix millisecond timestamp, e.g. 1690196141868 |
| data.orderList[].uTime | string |  | Update time, Unix millisecond timestamp, e.g. 1690196141868 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1668134581005,
  "data": {
    "nextFlag": false,
    "idLessThan": "1",
    "orderList": [
      {
        "orderId": "121211212122",
        "clientOid": "121211212122",
        "symbol": "TRXUSDT",
        "size": "151",
        "executePrice": "0.041572",
        "triggerPrice": "0.041572",
        "status": "not_trigger",
        "orderType": "limit",
        "side": "buy",
        "planType": "amount",
        "triggerType": "fill_price",
        "enterPointSource": "API",
        "uTime": "1668134576563",
        "cTime": "1668134576563"
      }
    ]
  }
}
```

## Get History Plan Orders

`GET /api/v2/spot/trade/history-plan-order`

Frequency limit: 20 times/1s (UID)

Get History Plan Orders

Operation ID: `classicSpotPlanGetHistoryPlanOrder`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | Trading pair, e.g. BTCUSDT |
| startTime | query | string |  | The start time of the historical trigger orders, i.e. to get orders after that timestamp. Unix millisecond timestamp, e.g. 1690196141868. The interval between startTime and endTime must not exceed 90 days |
| endTime | query | string |  | The end time of the historical trigger orders, i.e., getting orders prior to that timestamp. Unix millisecond timestamp, e.g. 1690196141868. The interval between startTime and endTime must not exceed 90 days. |
| idLessThan | query | string |  | Requests the content on the page before this ID (older data), the value input should be the endId of the corresponding interface. |
| limit | query | string |  | Limit. Default is 100, max is 100 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.nextFlag | boolean |  | If Has next query data by idLessThan or not |
| data.idLessThan | string |  | Requests the content on the page before this ID (older data), the value input should be the endId of the corresponding interface. |
| data.orderList | object[] |  | Order List |
| data.orderList[].orderId | string |  | Order ID |
| data.orderList[].clientOid | string |  | Client customized ID |
| data.orderList[].symbol | string |  | Trading pair |
| data.orderList[].triggerPrice | string |  | Trigger price |
| data.orderList[].orderType | string |  | Order type<br><br>`limit`: limit order<br><br>`market`: market order |
| data.orderList[].executePrice | string |  | Execution price |
| data.orderList[].planType | string |  | Order type<br><br>`amount`: By amount of the order<br><br>`total`: By trading volume of the order |
| data.orderList[].size | string |  | Quantity. If `placeType`=`amount`, the quote currency is the base coin. If `placeType`=`total`, the quote currency is the quote coin. |
| data.orderList[].status | string |  | Status<br><br>`executed`: Executed successfully<br><br>`fail_execute`: Fail in execution<br><br>`cancelled`: Cancelled |
| data.orderList[].side | string |  | Direction: `buy` or `sell` |
| data.orderList[].triggerType | string |  | Trigger type<br><br>`fill_price`: filled price<br><br>`mark_price`: mark price |
| data.orderList[].enterPointSource | string |  | Order source<br><br>`WEB`: Orders created on the website<br><br>`API`: Orders created on API<br><br>`SYS`: System managed orders, usually generated by forced liquidation logic<br><br>`ANDROID`: Orders created on the Android app<br><br>`IOS`: Orders created on the iOS app |
| data.orderList[].cTime | string |  | Creation time, Unix millisecond timestamp, e.g. 1690196141868 |
| data.orderList[].uTime | string |  | Update time, Unix millisecond timestamp, e.g. 1690196141868 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1668134581005,
  "data": {
    "nextFlag": false,
    "idLessThan": "1",
    "orderList": [
      {
        "orderId": "121211212122",
        "clientOid": "121211212122",
        "symbol": "TRXUSDT",
        "size": "151",
        "executePrice": "0.041572",
        "triggerPrice": "0.041572",
        "status": "not_trigger",
        "orderType": "limit",
        "side": "buy",
        "planType": "amount",
        "triggerType": "fill_price",
        "enterPointSource": "API",
        "uTime": "1668134576563",
        "cTime": "1668134576563"
      }
    ]
  }
}
```

## Get Plan Sub Order

`GET /api/v2/spot/trade/plan-sub-order`

Frequency limit: 20 times/1s (UID)

Get Plan Sub Order

Operation ID: `classicSpotPlanGetPlanSubOrder`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| planOrderId | query | string | 是 | Plan Order ID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].orderId | string |  | Spot order ID |
| data[].price | string |  | Order price |
| data[].type | string |  | Order type<br><br>limit Limit price<br><br>market Market price |
| data[].status | string |  | Plan order trigger status<br><br>success: trigger success<br><br>fail: trigger failed<br><br>cancelled: cancelled<br><br>in_progress: trigger spot placing order<br><br>in_progress_tracking: tracking trigger |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1710813939206,
  "data": [
    {
      "orderId": "xxxxxxxxxxxxx",
      "price": "0.4188",
      "type": "limit",
      "status": "success"
    }
  ]
}
```


---

现货计划委托接口 —— 下单、修改、撤销及查询计划委托。

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `POST /api/v2/spot/trade/place-plan-order` — 下单计划委托
- `POST /api/v2/spot/trade/modify-plan-order` — 修改计划委托
- `POST /api/v2/spot/trade/cancel-plan-order` — 撤销计划委托
- `POST /api/v2/spot/trade/batch-cancel-plan-order` — 批量撤销计划委托
- `GET /api/v2/spot/trade/current-plan-order` — 获取当前计划委托
- `GET /api/v2/spot/trade/history-plan-order` — 获取历史计划委托
- `GET /api/v2/spot/trade/plan-sub-order` — 获取计划委托触发条件单

## 下单计划委托

`POST /api/v2/spot/trade/place-plan-order`

限速规则 20次/1s (UID)

下单计划委托

- **API Broker返佣标识**: 需在HTTP Header请求头中添加如下代码块

  > "X-CHANNEL-API-CODE":"your-channel-api-code"

Operation ID: `classicSpotPlanPlacePlanOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbol | string | 是 | 交易对名称，如BTCUSDT |
| side | string | 是 | 方向<br><br>`buy`：买入<br><br>`sell`：卖出 |
| triggerPrice | string | 是 | 触发价格 |
| orderType | string | 是 | 订单类型<br><br>`limit`：限价<br><br>`market`：市价 |
| executePrice | string |  | 执行价格，orderType=limit时不能为空 |
| planType | string |  | 委托类型<br><br>`amount`：数量委托(左币)<br><br>`total`：交易额委托(右币)<br><br>默认值为amount数量委托 |
| size | string | 是 | 购买数量。planType=amount时, 计价单位是base coin（左币）。planType=total时, 计价单位是quote coin（右币） |
| triggerType | string | 是 | 触发类型<br><br>`fill_price`：成交价格<br><br>`mark_price`：标记价格 |
| clientOid | string |  | 客户自定义ID |
| stpMode | string |  | STP模式， default `none`<br><br>`none` 不设置STP<br><br>`cancel_taker` 取消taker单<br><br>`cancel_maker` 取消maker单<br><br>`cancel_both` 两者都取消 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | 订单ID |
| data.clientOid | string |  | 客户自定义ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1668134576535,
  "data": {
    "orderId": "1",
    "clientOid": "1"
  }
}
```

## 修改计划委托

`POST /api/v2/spot/trade/modify-plan-order`

限速规则 20次/1s (UID)

修改计划委托

Operation ID: `classicSpotPlanModifyPlanOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderId | string |  | 订单ID, 'orderId' 或 'clientOid' 必需提供一个 |
| clientOid | string |  | clientOid, 'orderId' 或 'clientOid' 必需提供一个 |
| triggerPrice | string | 是 | 触发价格 |
| orderType | string | 是 | 订单类型<br><br>limit限价<br><br>market市价 |
| executePrice | string |  | 执行价格，orderType=limit时不能为空 |
| size | string | 是 | 购买数量。planType=amount时, 计价单位是base coin（左币）。planType=total时, 计价单位是quote coin（右币） |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | 订单ID |
| data.clientOid | string |  | 客户自定义ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1668134576535,
  "data": {
    "orderId": "1",
    "clientOid": "1"
  }
}
```

## 撤销计划委托

`POST /api/v2/spot/trade/cancel-plan-order`

限速规则 20次/1s (UID)

撤销计划委托

Operation ID: `classicSpotPlanCancelPlanOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderId | string |  | 订单ID, 'orderId' 或 'clientOid' 必需提供一个 |
| clientOid | string |  | clientOid, 'orderId' 或 'clientOid' 必需提供一个 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.result | string |  | success 成功 ,fail 失败 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1668134497496,
  "data": {
    "result": "success"
  }
}
```

## 批量撤销计划委托

`POST /api/v2/spot/trade/batch-cancel-plan-order`

限速规则：5次/秒/UID

批量撤销计划委托

Operation ID: `classicSpotPlanBatchCancelPlanOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| symbolList | string[] |  | 币对集合：["BTCUSDT", "ETHUSDT"], 如不传值，会撤销所有现货计划委托单 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.successList | object[] |  | 成功订单数组 |
| data.successList[].orderId | string |  | 订单ID |
| data.successList[].clientOid | string |  | 客户端订单ID |
| data.failureList | object[] |  | 失败订单数组 |
| data.failureList[].orderId | string |  | 订单ID |
| data.failureList[].clientOid | string |  | 客户端订单ID |
| data.failureList[].errorMsg | string |  | 错误信息 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1683876261117,
  "data": {
    "successList": [
      {
        "orderId": "121211212122",
        "clientOid": "121211212122"
      }
    ],
    "failureList": [
      {
        "orderId": "121211212122",
        "clientOid": "121211212122",
        "errorMsg": "failure"
      }
    ]
  }
}
```

## 获取当前计划委托

`GET /api/v2/spot/trade/current-plan-order`

限速规则 20次/1s (UID)

获取当前计划委托

Operation ID: `classicSpotPlanGetCurrentPlanOrder`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | 交易对名称，如BTCUSDT |
| limit | query | string |  | 分页, 默认20，最大值100 |
| idLessThan | query | string |  | 最后ID，分页需要 |
| startTime | query | string |  | 开始时间(毫秒)，开始和结束时间间隔应小于90天 |
| endTime | query | string |  | 结束时间(毫秒)，开始和结束时间间隔应小于90天 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.nextFlag | boolean |  | 是否还有下一页数据 |
| data.idLessThan | string |  | 上一次查询的最后一条数据的orderId |
| data.orderList | object[] |  | 委托列表 |
| data.orderList[].orderId | string |  | 订单ID |
| data.orderList[].clientOid | string |  | 客户自定义ID |
| data.orderList[].symbol | string |  | 交易对名称 |
| data.orderList[].triggerPrice | string |  | 触发价格 |
| data.orderList[].orderType | string |  | 订单类型<br><br>`limit` 限价单，<br><br>`market` 市价单 |
| data.orderList[].executePrice | string |  | 执行价格 |
| data.orderList[].planType | string |  | 委托类型<br><br>`amount` 数量委托<br><br>`total` 交易额委托 |
| data.orderList[].size | string |  | 购买数量。`placeType`=`amount`时, 计价单位是base coin（左币）。`placeType`=`total`时, 计价单位是quote coin（右币） |
| data.orderList[].status | string |  | 状态<br><br>`live`: 待执行<br><br>`executing`: 下单中 |
| data.orderList[].side | string |  | 交易方向<br><br>`buy`: 买入<br><br>`sell`: 卖出 |
| data.orderList[].triggerType | string |  | 触发类型<br><br>`fill_price`成交价格<br><br>`mark_price`标记价格 |
| data.orderList[].enterPointSource | string |  | 订单来源<br><br>`WEB`: WEB客户端<br><br>`IOS`: IOS客户端<br><br>`ANDROID`: Andriod客户端<br><br>`API`: API客户端<br><br>`SYS`: 系统, 通常为爆仓 |
| data.orderList[].cTime | string |  | 创建时间，Unix毫秒时间戳，例如1690196141868 |
| data.orderList[].uTime | string |  | 更新时间，Unix毫秒时间戳，例如1690196141868 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1668134581005,
  "data": {
    "nextFlag": false,
    "idLessThan": "1",
    "orderList": [
      {
        "orderId": "1",
        "clientOid": "xxx001",
        "symbol": "TRXUSDT",
        "size": "151",
        "executePrice": "0.041572",
        "triggerPrice": "0.041572",
        "status": "not_trigger",
        "orderType": "limit",
        "side": "buy",
        "planType": "amount",
        "triggerType": "fill_price",
        "enterPointSource": "API",
        "uTime": "1668134576563",
        "cTime": "1668134576563"
      }
    ]
  }
}
```

## 获取历史计划委托

`GET /api/v2/spot/trade/history-plan-order`

限速规则 20次/1s (UID)

获取历史计划委托

Operation ID: `classicSpotPlanGetHistoryPlanOrder`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | 交易对名称，如BTCUSDT |
| startTime | query | string |  | 历史计划委托的开始时间，即获取该时间戳以后的订单。Unix毫秒时间戳，例如1690196141868。`startTime`和`endTime`的时间间隔不超过90天 |
| endTime | query | string |  | 历史计划委托的结束时间，即获取该时间戳以前的订单。Unix毫秒时间戳，例如1690196141868。`startTime`和`endTime`的时间间隔不超过90天 |
| idLessThan | query | string |  | 请求获取此 ID 之前的内容（更早的数据），输入值应为相应的 endId。 |
| limit | query | string |  | 分页 默认值100，最大值100 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.nextFlag | boolean |  | 下次查询是否还有数据 |
| data.idLessThan | string |  | data数据里最小的ID，通常用来翻页查询 |
| data.orderList | object[] |  | 订单列表 |
| data.orderList[].orderId | string |  | 订单ID |
| data.orderList[].clientOid | string |  | 客户自定义ID |
| data.orderList[].symbol | string |  | 交易对名称 |
| data.orderList[].triggerPrice | string |  | 触发价格 |
| data.orderList[].orderType | string |  | 订单类型<br><br>`limit` 限价单，<br><br>`market` 市价单 |
| data.orderList[].executePrice | string |  | 执行价格 |
| data.orderList[].planType | string |  | 委托类型<br><br>`amount`: 数量委托<br><br>`total`: 交易额委托 |
| data.orderList[].size | string |  | 购买数量。`placeType`=`amount`时, 计价单位是base coin（左币）。`placeType`=`total`时, 计价单位是quote coin（右币） |
| data.orderList[].status | string |  | 订单状态<br><br>`executed`: 执行成功<br><br>`fail_execute`: 执行失败<br><br>`cancelled`: 取消执行 |
| data.orderList[].side | string |  | 交易方向<br><br>`buy`: 买入<br><br>`sell`: 卖出 |
| data.orderList[].triggerType | string |  | 触发类型<br><br>`fill_price`: 成交价格<br><br>`mark_price`: 标记价格 |
| data.orderList[].enterPointSource | string |  | 订单来源<br><br>`WEB`: WEB客户端<br><br>`IOS`: IOS客户端<br><br>`ANDROID`: Andriod客户端<br><br>`API`: API客户端<br><br>`SYS`: 系统, 通常为爆仓 |
| data.orderList[].cTime | string |  | 创建时间，Unix毫秒时间戳，例如1690196141868 |
| data.orderList[].uTime | string |  | 更新时间，Unix毫秒时间戳，例如1690196141868 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1668134626684,
  "data": {
    "nextFlag": false,
    "idLessThan": "1",
    "orderList": [
      {
        "orderId": "1",
        "clientOid": "xxx001",
        "symbol": "TRXUSDT",
        "size": "156",
        "executePrice": "0.041272",
        "triggerPrice": "0.041222",
        "status": "cancel",
        "orderType": "limit",
        "side": "buy",
        "planType": "amount",
        "triggerType": "fill_price",
        "enterPointSource": "API",
        "uTime": "1668134576563",
        "cTime": "1668134576563"
      }
    ]
  }
}
```

## 获取计划委托触发条件单

`GET /api/v2/spot/trade/plan-sub-order`

限速规则 20次/1s (UID)

获取计划委托触发条件单（计划委托触发后执行的现货订单）

Operation ID: `classicSpotPlanGetPlanSubOrder`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| planOrderId | query | string | 是 | 计划委托订单ID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].orderId | string |  | 现货订单ID |
| data[].price | string |  | 委托价格 |
| data[].type | string |  | 订单类型<br><br>limit限价<br><br>market市价 |
| data[].status | string |  | 计划委托单触发状态<br><br>success: 执行成功<br><br>fail: 执行失败<br><br>cancelled: 取消<br><br>in_progress: 下单中<br><br>in_progress_tracking: 执行追踪中 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1710813939206,
  "data": [
    {
      "orderId": "xxxxxxxxxxxxx",
      "price": "0.4188",
      "type": "limit",
      "status": "success"
    }
  ]
}
```