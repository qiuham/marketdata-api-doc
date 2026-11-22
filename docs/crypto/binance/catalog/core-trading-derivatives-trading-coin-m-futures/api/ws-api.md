---
exchange: binance
source_url: https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/ws-api
api_type: WebSocket API
updated_at: 2026-11-22 18:46:05.418762
---

# Futures (COIN-M) WebSocket API

Schema: https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-coin-m-futures/api/ws-api/1.0.0/schema.yaml

Access market data, manage accounts, and trade COIN-M perpetual and delivery futures.

访问市场数据、管理账户，并交易 COIN-M 永续合约和交割合约。

版本: 1.0.0

## 服务地址

- `wss://ws-dapi.binance.com/ws-dapi/v1`
- `wss://testnet.binancefuture.com/ws-dapi/v1`

## 接口列表

- `POST /account.status` — Account Information (USER_DATA)
- `POST /account.balance` — Futures Account Balance (USER_DATA)
- `POST /order.cancel` — Cancel Order (TRADE)
- `POST /order.modify` — Modify Order (TRADE)
- `POST /order.place` — New Order (TRADE)
- `POST /account.position` — Position Information (USER_DATA)
- `POST /order.status` — Query Order (USER_DATA)
- `POST /userDataStream.stop` — Close User Data Stream (USER_STREAM)
- `POST /userDataStream.ping` — Keepalive User Data Stream (USER_STREAM)
- `POST /userDataStream.start` — Start User Data Stream (USER_STREAM)

## Account Information (USER_DATA)（账户信息 (USER_DATA)）

`POST /account.status`

Get current account information. User in single-asset/ multi-assets mode
will see different value, see comments in response section for detail.

现有账户信息。

Operation ID: `accountInformation`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | 例: `e9d6b4349871b40611412680b3445fac` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `account.status`<br>例: `account.status` |
| params | object | 是 |  |
| params.recvWindow | integer (int64) |  | 例: `5000` |
| params.timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The<br>value must reflect the current client time and is validated<br>by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |
| params.apiKey | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

```json
{
  "id": "e9d6b4349871b40611412680b3445fac",
  "method": "account.status",
  "params": {
    "recvWindow": 5000,
    "timestamp": 1770736694138,
    "apiKey": "API_KEY"
  }
}
```

### 响应 Successful Response：Account Information / 账户 信息

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string |  | positionId<br>持仓 ID<br>例: `baaec739-c5cf-4920-b448-c0b9c5431410` |
| status | integer (int64) |  | 例: `200` |
| result | object |  | Indicates that combined is set to true. |
| result.feeTier | integer (int64) |  | Fee tier level.<br>手续费等级.<br>例: `0` |
| result.canTrade | boolean |  | Whether trading is enabled.<br>是否可交易.<br>例: `True` |
| result.canDeposit | boolean |  | Whether deposits are enabled.<br>是否可充值.<br>例: `True` |
| result.canWithdraw | boolean |  | Whether withdrawals are enabled.<br>是否可提现.<br>例: `True` |
| result.updateTime | integer (int64) |  | update time<br>更新时间<br>例: `0` |
| result.assets | object[] |  | Supported assets.<br>支持的资产列表。 |
| result.assets[].asset | string |  | asset name<br>资产<br>例: `WLD` |
| result.assets[].walletBalance | string |  | total wallet balance<br>账户余额<br>例: `0.00000000` |
| result.assets[].unrealizedProfit | string |  | unrealized profit or loss<br>全部持仓未实现盈亏<br>例: `0.00000000` |
| result.assets[].marginBalance | string |  | margin balance<br>保证金余额<br>例: `0.00000000` |
| result.assets[].maintMargin | string |  | maintenance margin<br>维持保证金<br>例: `0.00000000` |
| result.assets[].initialMargin | string |  | total intial margin required with the latest mark price<br>当前所需起始保证金(按最新标标记价格)<br>例: `0.00000000` |
| result.assets[].positionInitialMargin | string |  | positions" margin required with the latest mark price<br>当前所需持仓起始保证金(按最新标标记价格)<br>例: `0.00000000` |
| result.assets[].openOrderInitialMargin | string |  | open orders" intial margin required with the latest mark price<br>当前所需挂单起始保证金(按最新标标记价格)<br>例: `0.00000000` |
| result.assets[].maxWithdrawAmount | string |  | maximum amount for transfer out<br>最大可转出余额<br>例: `0.00000000` |
| result.assets[].crossWalletBalance | string |  | wallet balance for crossed margin<br>可用于全仓的账户余额<br>例: `0.00000000` |
| result.assets[].crossUnPnl | string |  | total unrealized profit or loss of crossed positions<br>所有全仓持仓的未实现盈亏<br>例: `0.00000000` |
| result.assets[].availableBalance | string |  | available margin balance<br>可用下单余额<br>例: `0.00000000` |
| result.assets[].updateTime | integer (int64) |  | update time<br>更新时间<br>例: `0` |
| result.positions | object[] |  | Position list.<br>持仓列表. |
| result.positions[].symbol | string |  | Trading symbol<br>交易对<br>例: `ETHUSD_220930` |
| result.positions[].initialMargin | string |  | total intial margin required with the latest mark price<br>当前所需起始保证金(按最新标标记价格)<br>例: `0` |
| result.positions[].maintMargin | string |  | maintenance margin<br>维持保证金<br>例: `0` |
| result.positions[].unrealizedProfit | string |  | unrealized profit or loss<br>全部持仓未实现盈亏<br>例: `0.00000000` |
| result.positions[].positionInitialMargin | string |  | positions" margin required with the latest mark price<br>当前所需持仓起始保证金(按最新标标记价格)<br>例: `0` |
| result.positions[].openOrderInitialMargin | string |  | open orders" intial margin required with the latest mark price<br>当前所需挂单起始保证金(按最新标标记价格)<br>例: `0` |
| result.positions[].leverage | string |  | Leverage value.<br>杠杆倍数.<br>例: `7` |
| result.positions[].isolated | boolean |  | Whether isolated margin mode is enabled.<br>是否为逐仓模式.<br>例: `False` |
| result.positions[].positionSide | string |  | Position side<br>持仓方向<br>例: `BOTH` |
| result.positions[].entryPrice | string |  | Position entry price.<br>持仓开仓价格.<br>例: `0.00000000` |
| result.positions[].maxQty | string |  | maximum quantity of base asset<br>数量上限, 最大数量<br>例: `1000` |
| result.positions[].notionalValue | string |  | Notional value.<br>名义价值.<br>例: `0` |
| result.positions[].isolatedWallet | string |  | Isolated wallet balance.<br>逐仓钱包余额.<br>例: `0` |
| result.positions[].updateTime | integer (int64) |  | update time<br>更新时间<br>例: `0` |
| result.positions[].positionAmt | string |  | position amount<br>持仓数量<br>例: `0` |
| result.positions[].breakEvenPrice | string |  | break-even price<br>盈亏平衡价<br>例: `0.00000000` |
| rateLimits | object[] |  | Rate limit definitions.<br>频率限制定义. |
| rateLimits[].rateLimitType | string |  | Rate limit type.<br>频率限制类型.<br>例: `REQUEST_WEIGHT` |
| rateLimits[].interval | string |  | Rate limit interval.<br>频率限制区间.<br>例: `MINUTE` |
| rateLimits[].intervalNum | integer (int64) |  | Rate limit interval multiplier.<br>频率限制区间倍数.<br>例: `1` |
| rateLimits[].limit | integer (int64) |  | Maximum allowed orders for this rule.<br>该规则允许的最大订单数。<br>例: `2400` |
| rateLimits[].count | integer (int64) |  | Total number of trades in the 24h window.<br>24 小时窗口内成交总笔数。<br>例: `10` |

## Futures Account Balance (USER_DATA)（账户余额 (USER_DATA)）

`POST /account.balance`

Futures Account Balance

账户余额

Operation ID: `futuresAccountBalance`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | 例: `e9d6b4349871b40611412680b3445fac` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `account.balance`<br>例: `account.balance` |
| params | object | 是 |  |
| params.recvWindow | integer (int64) |  | 例: `5000` |
| params.timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The<br>value must reflect the current client time and is validated<br>by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |
| params.apiKey | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

```json
{
  "id": "e9d6b4349871b40611412680b3445fac",
  "method": "account.balance",
  "params": {
    "recvWindow": 5000,
    "timestamp": 1770736694138,
    "apiKey": "API_KEY"
  }
}
```

### 响应 Successful Response：Futures Account Balance / 合约 账户 Balance

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string |  | positionId<br>持仓 ID<br>例: `9328e612-1560-4108-979e-283bf85b5acb` |
| status | integer (int64) |  | 例: `200` |
| result | object[] |  | Indicates that combined is set to true. |
| result[].accountAlias | string |  | unique account code<br>账户唯一识别码<br>例: `fWAuTiuXoCuXmY` |
| result[].asset | string |  | asset name<br>资产<br>例: `WLD` |
| result[].balance | string |  | Account balance.<br>账户余额.<br>例: `0.00000000` |
| result[].withdrawAvailable | string |  | Available amount for withdrawal.<br>可提现金额.<br>例: `0.00000000` |
| result[].crossWalletBalance | string |  | wallet balance for crossed margin<br>可用于全仓的账户余额<br>例: `0.00000000` |
| result[].crossUnPnl | string |  | total unrealized profit or loss of crossed positions<br>所有全仓持仓的未实现盈亏<br>例: `0.00000000` |
| result[].availableBalance | string |  | available margin balance<br>可用下单余额<br>例: `0.00000000` |
| result[].updateTime | integer (int64) |  | update time<br>更新时间<br>例: `0` |
| rateLimits | object[] |  | Rate limit definitions.<br>频率限制定义. |
| rateLimits[].rateLimitType | string |  | Rate limit type.<br>频率限制类型.<br>例: `REQUEST_WEIGHT` |
| rateLimits[].interval | string |  | Rate limit interval.<br>频率限制区间.<br>例: `MINUTE` |
| rateLimits[].intervalNum | integer (int64) |  | Rate limit interval multiplier.<br>频率限制区间倍数.<br>例: `1` |
| rateLimits[].limit | integer (int64) |  | Maximum allowed orders for this rule.<br>该规则允许的最大订单数。<br>例: `2400` |
| rateLimits[].count | integer (int64) |  | Total number of trades in the 24h window.<br>24 小时窗口内成交总笔数。<br>例: `10` |

## Cancel Order (TRADE)（撤销订单 (TRADE)）

`POST /order.cancel`

Cancel an active order.

撤销订单

Operation ID: `cancelOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | 例: `e9d6b4349871b40611412680b3445fac` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `order.cancel`<br>例: `order.cancel` |
| params | object | 是 |  |
| params.symbol | string | 是 | 例: `BTCUSD_PERP` |
| params.orderId | integer (int64) |  | 例: `1` |
| params.origClientOrderId | string |  | 例: `1` |
| params.recvWindow | integer (int64) |  | 例: `5000` |
| params.timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The<br>value must reflect the current client time and is validated<br>by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |
| params.apiKey | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

```json
{
  "id": "e9d6b4349871b40611412680b3445fac",
  "method": "order.cancel",
  "params": {
    "symbol": "BTCUSD_PERP",
    "orderId": 1,
    "origClientOrderId": "1",
    "recvWindow": 5000,
    "timestamp": 1770736694138,
    "apiKey": "API_KEY"
  }
}
```

### 响应 Successful Response：Cancel Order / 取消订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string |  | positionId<br>持仓 ID<br>例: `a8627ea5-8b9f-452f-90ae-4136f2b442e2` |
| status | integer (int64) |  | 例: `200` |
| result | object |  | Indicates that combined is set to true. |
| result.orderId | integer (int64) |  | Sub-order ID<br>子订单 ID<br>例: `333245211` |
| result.symbol | string |  | Trading symbol<br>交易对<br>例: `BTCUSD_PERP` |
| result.pair | string |  | Pair<br>标的交易对<br>例: `BTCUSD` |
| result.status | string |  | Status.<br>订单状态<br>例: `CANCELED` |
| result.clientOrderId | string |  | Client order ID.<br>客户端订单 ID.<br>例: `5SztZiGFAxgAqw4J9EN9fA` |
| result.price | string |  | Latest token price.<br>代币最新价格。<br>例: `51000` |
| result.origQty | string |  | Original order quantity<br>原始委托数量<br>例: `1` |
| result.executedQty | string |  | Executed quantity<br>执行数量<br>例: `0` |
| result.cumQty | string |  | Cumulative filled quantity.<br>累计成交数量.<br>例: `0` |
| result.timeInForce | string |  | Time in force<br>有效方式<br>例: `GTC` |
| result.type | string |  | Order type.<br>订单类型.<br>例: `LIMIT` |
| result.reduceOnly | boolean |  | Whether the order is reduce-only.<br>是否为只减仓订单.<br>例: `False` |
| result.closePosition | boolean |  | if Close-All<br>是否条件全平仓<br>例: `False` |
| result.side | string |  | Trading side<br>买卖方向<br>例: `BUY` |
| result.positionSide | string |  | Position side<br>持仓方向<br>例: `BOTH` |
| result.stopPrice | string |  | please ignore when order type is TRAILING_STOP_MARKET<br>触发价,对`TRAILING_STOP_MARKET`无效<br>例: `0` |
| result.workingType | string |  | Stop trigger price type.<br>止损触发价格类型.<br>例: `CONTRACT_PRICE` |
| result.priceProtect | boolean |  | if conditional order trigger is protected<br>是否开启条件单触发保护<br>例: `False` |
| result.origType | string |  | Original order type.<br>原始订单类型.<br>例: `LIMIT` |
| result.updateTime | integer (int64) |  | update time<br>更新时间<br>例: `1728416138285` |
| rateLimits | object[] |  | Rate limit definitions.<br>频率限制定义. |
| rateLimits[].rateLimitType | string |  | Rate limit type.<br>频率限制类型.<br>例: `REQUEST_WEIGHT` |
| rateLimits[].interval | string |  | Rate limit interval.<br>频率限制区间.<br>例: `MINUTE` |
| rateLimits[].intervalNum | integer (int64) |  | Rate limit interval multiplier.<br>频率限制区间倍数.<br>例: `1` |
| rateLimits[].limit | integer (int64) |  | Maximum allowed orders for this rule.<br>该规则允许的最大订单数。<br>例: `2400` |
| rateLimits[].count | integer (int64) |  | Total number of trades in the 24h window.<br>24 小时窗口内成交总笔数。<br>例: `6` |

## Modify Order (TRADE)（修改订单 (TRADE)）

`POST /order.modify`

Order modify function, currently only LIMIT order modification is
supported, modified orders will be reordered in the match queue

修改订单功能，当前只支持限价（LIMIT）订单修改，修改后会在撮合队列里重新排序

权重: 1 on 10s order rate limit(X-MBX-ORDER-COUNT-10S);
1 on 1min order rate limit(X-MBX-ORDER-COUNT-1M);
1 on IP rate limit(x-mbx-used-weight-1m)

Operation ID: `modifyOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | 例: `e9d6b4349871b40611412680b3445fac` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `order.modify`<br>例: `order.modify` |
| params | object | 是 |  |
| params.orderId | integer (int64) |  | 例: `1` |
| params.origClientOrderId | string |  | 例: `1` |
| params.symbol | string | 是 | 例: `BTCUSD_PERP` |
| params.side | string | 是 | 枚举: `BUY`, `SELL`<br>例: `BUY` |
| params.quantity | number (float) | 是 | Order quantity, cannot be sent with `closePosition=true`<br>请参见英文说明：Order quantity, cannot be sent with `closePosition=true`<br>例: `1.0` |
| params.price | number (float) | 是 | 例: `1.0` |
| params.priceMatch | string |  | only avaliable for `LIMIT`/`STOP`/`TAKE_PROFIT` order; Can't be passed together with `price`<br>仅对 `LIMIT`/`STOP`/`TAKE_PROFIT` 订单有效；不能与 `price` 参数同时传递<br>枚举: `OPPONENT`, `OPPONENT_5`, `OPPONENT_10`, `OPPONENT_20`, `QUEUE`, `QUEUE_5`, `QUEUE_10`, `QUEUE_20`<br>例: `OPPONENT` |
| params.modifyId | integer (int64) |  | User-defined modification identifier, returned as-is in the response. Optional; not validated for uniqueness.<br>用户自定义的改单标识，原样返回。可选；服务端不校验唯一性。<br>例: `1` |
| params.recvWindow | integer (int64) |  | 例: `5000` |
| params.timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The<br>value must reflect the current client time and is validated<br>by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |
| params.apiKey | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

```json
{
  "id": "e9d6b4349871b40611412680b3445fac",
  "method": "order.modify",
  "params": {
    "orderId": 1,
    "origClientOrderId": "1",
    "symbol": "BTCUSD_PERP",
    "side": "BUY",
    "quantity": "1.0",
    "price": "1.0",
    "priceMatch": "OPPONENT",
    "modifyId": 1,
    "recvWindow": 5000,
    "timestamp": 1770736694138,
    "apiKey": "API_KEY"
  }
}
```

### 响应 Successful Response：Modify Order / Modify 订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string |  | positionId<br>持仓 ID<br>例: `88601d02-bd0d-430d-8733-2708a569ebda` |
| status | integer (int64) |  | 例: `200` |
| result | object |  | Indicates that combined is set to true. |
| result.orderId | integer (int64) |  | Sub-order ID<br>子订单 ID<br>例: `333245211` |
| result.symbol | string |  | Trading symbol<br>交易对<br>例: `BTCUSD_PERP` |
| result.pair | string |  | Pair<br>标的交易对<br>例: `BTCUSD` |
| result.status | string |  | Status.<br>订单状态<br>例: `NEW` |
| result.clientOrderId | string |  | Client order ID.<br>客户端订单 ID.<br>例: `5SztZiGFAxgAqw4J9EN9fA` |
| result.modifyId | integer (int64) |  | user-defined modification identifier, only returned if provided in the request<br>用户自定义的改单标识，仅当请求中传入时返回<br>例: `1` |
| result.price | string |  | Latest token price.<br>代币最新价格。<br>例: `51000` |
| result.origQty | string |  | Original order quantity<br>原始委托数量<br>例: `1` |
| result.executedQty | string |  | Executed quantity<br>执行数量<br>例: `0` |
| result.cumQty | string |  | Cumulative filled quantity.<br>累计成交数量.<br>例: `0` |
| result.timeInForce | string |  | Time in force<br>有效方式<br>例: `GTC` |
| result.type | string |  | Order type.<br>订单类型.<br>例: `LIMIT` |
| result.reduceOnly | boolean |  | Whether the order is reduce-only.<br>是否为只减仓订单.<br>例: `False` |
| result.closePosition | boolean |  | if Close-All<br>是否条件全平仓<br>例: `False` |
| result.side | string |  | Trading side<br>买卖方向<br>例: `BUY` |
| result.positionSide | string |  | Position side<br>持仓方向<br>例: `BOTH` |
| result.stopPrice | string |  | please ignore when order type is TRAILING_STOP_MARKET<br>触发价,对`TRAILING_STOP_MARKET`无效<br>例: `0` |
| result.workingType | string |  | Stop trigger price type.<br>止损触发价格类型.<br>例: `CONTRACT_PRICE` |
| result.priceProtect | boolean |  | if conditional order trigger is protected<br>是否开启条件单触发保护<br>例: `False` |
| result.origType | string |  | Original order type.<br>原始订单类型.<br>例: `LIMIT` |
| result.updateTime | integer (int64) |  | update time<br>更新时间<br>例: `1728415765493` |
| rateLimits | object[] |  | Rate limit definitions.<br>频率限制定义. |
| rateLimits[].rateLimitType | string |  | Rate limit type.<br>频率限制类型.<br>例: `REQUEST_WEIGHT` |
| rateLimits[].interval | string |  | Rate limit interval.<br>频率限制区间.<br>例: `MINUTE` |
| rateLimits[].intervalNum | integer (int64) |  | Rate limit interval multiplier.<br>频率限制区间倍数.<br>例: `1` |
| rateLimits[].limit | integer (int64) |  | Maximum allowed orders for this rule.<br>该规则允许的最大订单数。<br>例: `2400` |
| rateLimits[].count | integer (int64) |  | Total number of trades in the 24h window.<br>24 小时窗口内成交总笔数。<br>例: `6` |

## New Order (TRADE)（下单 (TRADE)）

`POST /order.place`

Send in a new order.

下单

Operation ID: `newOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | 例: `e9d6b4349871b40611412680b3445fac` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `order.place`<br>例: `order.place` |
| params | object | 是 |  |
| params.symbol | string | 是 | 例: `BTCUSD_PERP` |
| params.side | string | 是 | 枚举: `BUY`, `SELL`<br>例: `BUY` |
| params.positionSide | string |  | Default `BOTH` for One-way Mode; `LONG` or `SHORT` for Hedge Mode.  It must be sent in Hedge Mode.<br>One-way 模式默认 `BOTH`；Hedge 模式 `LONG` 或 `SHORT`，Hedge 模式必须发送<br>枚举: `BOTH`, `LONG`, `SHORT`<br>例: `BOTH` |
| params.type | string | 是 | **After CM migration, stop-type values (`STOP`, `STOP_MARKET`, `TAKE_PROFIT`, `TAKE_PROFIT_MARKET`, `TRAILING_STOP_MARKET`) are no longer accepted and will return `-4120`. Use the REST `/dapi/v1/algoOrder` endpoint instead.**<br>**迁移后,本接口不再接受 stop 类型(`STOP`/`STOP_MARKET`/`TAKE_PROFIT`/`TAKE_PROFIT_MARKET`/`TRAILING_STOP_MARKET`),会返回 `-4120`。请改用 REST 接口 `/dapi/v1/algoOrder`。**<br>枚举: `LIMIT`, `MARKET`, `STOP`, `STOP_MARKET`, `TAKE_PROFIT`, `TAKE_PROFIT_MARKET`, `TRAILING_STOP_MARKET`<br>例: `LIMIT` |
| params.timeInForce | string |  | 枚举: `GTC`, `IOC`, `FOK`, `GTX`<br>例: `GTC` |
| params.quantity | number (float) |  | Quantity measured by contract number, Cannot be sent with `closePosition`=`true`<br>请参见英文说明：Quantity measured by contract number, Cannot be sent with `closePosition`=`true`<br>例: `1.0` |
| params.reduceOnly | string |  | Cannot be sent in Hedge Mode; cannot be sent with `closePosition`=`true` (Close-All)"<br>请参见英文说明：Cannot be sent in Hedge Mode; cannot be sent with `closePosition`=`true` (Close-All)<br>枚举: `true`, `false`<br>默认: `false`<br>例: `true` |
| params.price | number (float) |  | 例: `1.0` |
| params.newClientOrderId | string |  | A unique id among open orders. Automatically generated if not sent. Can only be string following the rule: `^[\.A-Z\:/a-z0-9_-]{1,36}$`<br>请参见英文说明：A unique id among open orders. Automatically generated if not sent. Can only be string following the rule: `^[\.A-Z\:/a-z0-9_-]{1,36}$`<br>例: `1` |
| params.stopPrice | number (float) |  | Used with `STOP/STOP_MARKET` or `TAKE_PROFIT/TAKE_PROFIT_MARKET` orders.<br>请参见英文说明：Used with `STOP/STOP_MARKET` or `TAKE_PROFIT/TAKE_PROFIT_MARKET` orders.<br>例: `1.0` |
| params.closePosition | string |  | `true`, `false`；Close-All，used with `STOP_MARKET` or `TAKE_PROFIT_MARKET`.<br>请参见英文说明：`true`, `false`；Close-All，used with `STOP_MARKET` or `TAKE_PROFIT_MARKET`.<br>枚举: `true`, `false`<br>例: `true` |
| params.activationPrice | number (float) |  | Used with `TRAILING_STOP_MARKET` orders, default as the latest price(supporting different workingType)<br>请参见英文说明：Used with `TRAILING_STOP_MARKET` orders, default as the latest price(supporting different workingType)<br>例: `1.0` |
| params.callbackRate | number (float) |  | Used with `TRAILING_STOP_MARKET` orders, min 0.1, max 10 where 1 for 1%<br>请参见英文说明：Used with `TRAILING_STOP_MARKET` orders, min 0.1, max 10 where 1 for 1%<br>例: `5000.0` |
| params.workingType | string |  | stopPrice triggered by: "MARK_PRICE", "CONTRACT_PRICE". Default "CONTRACT_PRICE"<br>请参见英文说明：stopPrice triggered by: "MARK_PRICE", "CONTRACT_PRICE". Default "CONTRACT_PRICE"<br>枚举: `MARK_PRICE`, `CONTRACT_PRICE`<br>默认: `CONTRACT_PRICE`<br>例: `MARK_PRICE` |
| params.priceProtect | string |  | Used with `STOP/STOP_MARKET` or `TAKE_PROFIT/TAKE_PROFIT_MARKET` orders.'<br>Used with `STOP/STOP_MARKET` or `TAKE_PROFIT/TAKE_PROFIT_MARKET` orders.<br>枚举: `true`, `false`<br>默认: `false`<br>例: `true` |
| params.newOrderRespType | string |  | 枚举: `ACK`, `RESULT`<br>默认: `ACK`<br>例: `ACK` |
| params.priceMatch | string |  | only available for `LIMIT`/`STOP`/`TAKE_PROFIT` order; Can't be passed together with `price`<br>请参见英文说明：only available for `LIMIT`/`STOP`/`TAKE_PROFIT` order; Can't be passed together with `price`<br>枚举: `OPPONENT`, `OPPONENT_5`, `OPPONENT_10`, `OPPONENT_20`, `QUEUE`, `QUEUE_5`, `QUEUE_10`, `QUEUE_20`<br>例: `OPPONENT` |
| params.selfTradePreventionMode | string |  | `NONE`: No STP / `EXPIRE_TAKER`: expire taker order when STP triggers/ `EXPIRE_MAKER`: expire taker order when STP triggers/ `EXPIRE_BOTH`: expire both orders when STP triggers<br>请参见英文说明：`NONE`: No STP / `EXPIRE_TAKER`: expire taker order when STP triggers/ `EXPIRE_MAKER`: expire taker order when STP triggers/ `EXPIRE_BOTH`: expire both orders when STP triggers<br>枚举: `NONE`, `EXPIRE_TAKER`, `EXPIRE_BOTH`, `EXPIRE_MAKER`<br>默认: `NONE`<br>例: `NONE` |
| params.recvWindow | integer (int64) |  | 例: `5000` |
| params.timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The<br>value must reflect the current client time and is validated<br>by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |
| params.apiKey | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

```json
{
  "id": "e9d6b4349871b40611412680b3445fac",
  "method": "order.place",
  "params": {
    "symbol": "BTCUSD_PERP",
    "side": "BUY",
    "positionSide": "BOTH",
    "type": "LIMIT",
    "timeInForce": "GTC",
    "quantity": "1.0",
    "reduceOnly": "true",
    "price": "1.0",
    "newClientOrderId": "1",
    "stopPrice": "1.0",
    "closePosition": "true",
    "activationPrice": "1.0",
    "callbackRate": "5000.0",
    "workingType": "MARK_PRICE",
    "priceProtect": "true",
    "newOrderRespType": "ACK",
    "priceMatch": "OPPONENT",
    "selfTradePreventionMode": "NONE",
    "recvWindow": 5000,
    "timestamp": 1770736694138,
    "apiKey": "API_KEY"
  }
}
```

### 响应 Successful Response：New Order / New 订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string |  | positionId<br>持仓 ID<br>例: `60fa4366-f96e-42fe-a82b-f819952c6db4` |
| status | integer (int64) |  | 例: `200` |
| result | object |  | Indicates that combined is set to true. |
| result.orderId | integer (int64) |  | Sub-order ID<br>子订单 ID<br>例: `333245211` |
| result.symbol | string |  | Trading symbol<br>交易对<br>例: `BTCUSD_PERP` |
| result.pair | string |  | Pair<br>标的交易对<br>例: `BTCUSD` |
| result.status | string |  | Status.<br>订单状态<br>例: `NEW` |
| result.clientOrderId | string |  | Client order ID.<br>客户端订单 ID.<br>例: `5SztZiGFAxgAqw4J9EN9fA` |
| result.price | string |  | Latest token price.<br>代币最新价格。<br>例: `50000` |
| result.origQty | string |  | Original order quantity<br>原始委托数量<br>例: `1` |
| result.executedQty | string |  | Executed quantity<br>执行数量<br>例: `0` |
| result.cumQty | string |  | Cumulative filled quantity.<br>累计成交数量.<br>例: `0` |
| result.timeInForce | string |  | Time in force<br>有效方式<br>例: `GTC` |
| result.type | string |  | Order type.<br>订单类型.<br>例: `LIMIT` |
| result.reduceOnly | boolean |  | Whether the order is reduce-only.<br>是否为只减仓订单.<br>例: `False` |
| result.closePosition | boolean |  | if Close-All<br>是否条件全平仓<br>例: `False` |
| result.side | string |  | Trading side<br>买卖方向<br>例: `BUY` |
| result.positionSide | string |  | Position side<br>持仓方向<br>例: `BOTH` |
| result.stopPrice | string |  | please ignore when order type is TRAILING_STOP_MARKET<br>触发价,对`TRAILING_STOP_MARKET`无效<br>例: `0` |
| result.workingType | string |  | Stop trigger price type.<br>止损触发价格类型.<br>例: `CONTRACT_PRICE` |
| result.priceProtect | boolean |  | if conditional order trigger is protected<br>是否开启条件单触发保护<br>例: `False` |
| result.origType | string |  | Original order type.<br>原始订单类型.<br>例: `LIMIT` |
| result.updateTime | integer (int64) |  | update time<br>更新时间<br>例: `1728413795125` |
| rateLimits | object[] |  | Rate limit definitions.<br>频率限制定义. |
| rateLimits[].rateLimitType | string |  | Rate limit type.<br>频率限制类型.<br>例: `REQUEST_WEIGHT` |
| rateLimits[].interval | string |  | Rate limit interval.<br>频率限制区间.<br>例: `MINUTE` |
| rateLimits[].intervalNum | integer (int64) |  | Rate limit interval multiplier.<br>频率限制区间倍数.<br>例: `1` |
| rateLimits[].limit | integer (int64) |  | Maximum allowed orders for this rule.<br>该规则允许的最大订单数。<br>例: `2400` |
| rateLimits[].count | integer (int64) |  | Total number of trades in the 24h window.<br>24 小时窗口内成交总笔数。<br>例: `6` |

## Position Information (USER_DATA)（用户持仓风险 (USER_DATA)）

`POST /account.position`

Get current position information.

查询持仓风险

Operation ID: `positionInformation`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | 例: `e9d6b4349871b40611412680b3445fac` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `account.position`<br>例: `account.position` |
| params | object | 是 |  |
| params.marginAsset | string |  | 例: `USDT` |
| params.pair | string |  | 例: `BTCUSD` |
| params.recvWindow | integer (int64) |  | 例: `5000` |
| params.timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The<br>value must reflect the current client time and is validated<br>by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |
| params.apiKey | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

```json
{
  "id": "e9d6b4349871b40611412680b3445fac",
  "method": "account.position",
  "params": {
    "marginAsset": "USDT",
    "pair": "BTCUSD",
    "recvWindow": 5000,
    "timestamp": 1770736694138,
    "apiKey": "API_KEY"
  }
}
```

### 响应 Successful Response：Position Information / 持仓 信息

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string |  | positionId<br>持仓 ID<br>例: `233b8741-a96d-48e8-8ce1-160f43548aeb` |
| status | integer (int64) |  | 例: `200` |
| result | object[] |  | Indicates that combined is set to true. |
| result[].symbol | string |  | Trading symbol<br>交易对<br>例: `BTCUSD_PERP` |
| result[].positionAmt | string |  | position amount<br>持仓数量<br>例: `0` |
| result[].entryPrice | string |  | Position entry price.<br>持仓开仓价格.<br>例: `0.00000000` |
| result[].markPrice | string |  | mark price<br>标记价格<br>例: `62297.60417296` |
| result[].unRealizedProfit | string |  | Unrealized profit.<br>未实现盈亏.<br>例: `0.00000000` |
| result[].liquidationPrice | string |  | Liquidation price.<br>强平价格.<br>例: `0` |
| result[].leverage | string |  | Leverage value.<br>杠杆倍数.<br>例: `7` |
| result[].maxQty | string |  | maximum quantity of base asset<br>数量上限, 最大数量<br>例: `100` |
| result[].marginType | string |  | Margin type.<br>保证金模式.<br>例: `cross` |
| result[].isolatedMargin | string |  | Isolated margin amount.<br>逐仓保证金数量.<br>例: `0.00000000` |
| result[].isAutoAddMargin | string |  | Whether auto-add margin is enabled.<br>是否开启自动追加保证金.<br>例: `false` |
| result[].positionSide | string |  | Position side<br>持仓方向<br>例: `BOTH` |
| result[].notionalValue | string |  | Notional value.<br>名义价值.<br>例: `0` |
| result[].isolatedWallet | string |  | Isolated wallet balance.<br>逐仓钱包余额.<br>例: `0` |
| result[].updateTime | integer (int64) |  | update time<br>更新时间<br>例: `1726731195634` |
| result[].breakEvenPrice | string |  | break-even price<br>盈亏平衡价<br>例: `0.00000000` |
| rateLimits | object[] |  | Rate limit definitions.<br>频率限制定义. |
| rateLimits[].rateLimitType | string |  | Rate limit type.<br>频率限制类型.<br>例: `REQUEST_WEIGHT` |
| rateLimits[].interval | string |  | Rate limit interval.<br>频率限制区间.<br>例: `MINUTE` |
| rateLimits[].intervalNum | integer (int64) |  | Rate limit interval multiplier.<br>频率限制区间倍数.<br>例: `1` |
| rateLimits[].limit | integer (int64) |  | Maximum allowed orders for this rule.<br>该规则允许的最大订单数。<br>例: `2400` |
| rateLimits[].count | integer (int64) |  | Total number of trades in the 24h window.<br>24 小时窗口内成交总笔数。<br>例: `10` |

## Query Order (USER_DATA)（查询订单 (USER_DATA)）

`POST /order.status`

Check an order's status.

* These orders will not be found:
  * order status is `CANCELED` or `EXPIRED` **AND** order has NO filled trade **AND** created time + 3 days < current time
  * order create time + 90 days < current time

查询订单状态

* 请注意，如果订单满足如下条件，不会被查询到：
  * 订单的最终状态为 `CANCELED` 或者 `EXPIRED` **并且** 订单没有任何的成交记录 **并且** 订单生成时间 + 3天 < 当前时间
  * 订单创建时间 + 90天 < 当前时间

Operation ID: `queryOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | 例: `e9d6b4349871b40611412680b3445fac` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `order.status`<br>例: `order.status` |
| params | object | 是 |  |
| params.symbol | string | 是 | 例: `BTCUSD_PERP` |
| params.orderId | integer (int64) |  | 例: `1` |
| params.origClientOrderId | string |  | 例: `1` |
| params.recvWindow | integer (int64) |  | 例: `5000` |
| params.timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The<br>value must reflect the current client time and is validated<br>by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |
| params.apiKey | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

```json
{
  "id": "e9d6b4349871b40611412680b3445fac",
  "method": "order.status",
  "params": {
    "symbol": "BTCUSD_PERP",
    "orderId": 1,
    "origClientOrderId": "1",
    "recvWindow": 5000,
    "timestamp": 1770736694138,
    "apiKey": "API_KEY"
  }
}
```

### 响应 Successful Response：Order / 订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string |  | positionId<br>持仓 ID<br>例: `0ce5d070-a5e5-4ff2-b57f-1556741a4204` |
| status | integer (int64) |  | 例: `200` |
| result | object |  | Indicates that combined is set to true. |
| result.orderId | integer (int64) |  | Sub-order ID<br>子订单 ID<br>例: `328999071` |
| result.symbol | string |  | Trading symbol<br>交易对<br>例: `BTCUSD_PERP` |
| result.pair | string |  | Pair<br>标的交易对<br>例: `BTCUSD` |
| result.status | string |  | Status.<br>订单状态<br>例: `NEW` |
| result.clientOrderId | string |  | Client order ID.<br>客户端订单 ID.<br>例: `ArY8Ng1rln0s9x3fclmAHy` |
| result.price | string |  | Latest token price.<br>代币最新价格。<br>例: `58000` |
| result.avgPrice | string |  | Average execution price<br>平均价格<br>例: `0.00` |
| result.origQty | string |  | Original order quantity<br>原始委托数量<br>例: `1` |
| result.executedQty | string |  | Executed quantity<br>执行数量<br>例: `0` |
| result.cumQty | string |  | Cumulative filled quantity.<br>累计成交数量.<br>例: `0` |
| result.cumBase | string |  | Cumulative base asset amount.<br>累计基础资产数量.<br>例: `0` |
| result.timeInForce | string |  | Time in force<br>有效方式<br>例: `GTC` |
| result.type | string |  | Order type.<br>订单类型.<br>例: `LIMIT` |
| result.reduceOnly | boolean |  | Whether the order is reduce-only.<br>是否为只减仓订单.<br>例: `False` |
| result.closePosition | boolean |  | if Close-All<br>是否条件全平仓<br>例: `False` |
| result.side | string |  | Trading side<br>买卖方向<br>例: `BUY` |
| result.positionSide | string |  | Position side<br>持仓方向<br>例: `LONG` |
| result.stopPrice | string |  | please ignore when order type is TRAILING_STOP_MARKET<br>触发价,对`TRAILING_STOP_MARKET`无效<br>例: `0` |
| result.workingType | string |  | Stop trigger price type.<br>止损触发价格类型.<br>例: `CONTRACT_PRICE` |
| result.priceProtect | boolean |  | if conditional order trigger is protected<br>是否开启条件单触发保护<br>例: `False` |
| result.origType | string |  | Original order type.<br>原始订单类型.<br>例: `LIMIT` |
| result.selfTradePreventionMode | string |  | self trading preventation mode<br>订单自成交保护模式<br>例: `EXPIRE_TAKER` |
| result.time | integer (int64) |  | Time<br>时间<br>例: `1733740063619` |
| result.updateTime | integer (int64) |  | update time<br>更新时间<br>例: `1733740063619` |
| result.priceMatch | string |  | price match mode<br>盘口价格下单模式<br>例: `NONE` |
| rateLimits | object[] |  | Rate limit definitions.<br>频率限制定义. |
| rateLimits[].rateLimitType | string |  | Rate limit type.<br>频率限制类型.<br>例: `REQUEST_WEIGHT` |
| rateLimits[].interval | string |  | Rate limit interval.<br>频率限制区间.<br>例: `MINUTE` |
| rateLimits[].intervalNum | integer (int64) |  | Rate limit interval multiplier.<br>频率限制区间倍数.<br>例: `1` |
| rateLimits[].limit | integer (int64) |  | Maximum allowed orders for this rule.<br>该规则允许的最大订单数。<br>例: `2400` |
| rateLimits[].count | integer (int64) |  | Total number of trades in the 24h window.<br>24 小时窗口内成交总笔数。<br>例: `6` |

## Close User Data Stream (USER_STREAM)（Websocket API关闭listenKey (USER_STREAM)）

`POST /userDataStream.stop`

Close out a user data stream.

关闭某账户数据流

Operation ID: `closeUserDataStream`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | 例: `e9d6b4349871b40611412680b3445fac` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `userDataStream.stop`<br>例: `userDataStream.stop` |
| params | object | 是 |  |
| params.apiKey | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

```json
{
  "id": "e9d6b4349871b40611412680b3445fac",
  "method": "userDataStream.stop",
  "params": {
    "apiKey": "API_KEY"
  }
}
```

### 响应 Successful Response：Close User Data Stream / 关闭 用户 Data Stream

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string |  | positionId<br>持仓 ID<br>例: `819e1b1b-8c06-485b-a13e-131326c69599` |
| status | integer (int64) |  | 例: `200` |
| result | object |  | Indicates that combined is set to true. |
| rateLimits | object[] |  | Rate limit definitions.<br>频率限制定义. |
| rateLimits[].rateLimitType | string |  | Rate limit type.<br>频率限制类型.<br>例: `REQUEST_WEIGHT` |
| rateLimits[].interval | string |  | Rate limit interval.<br>频率限制区间.<br>例: `MINUTE` |
| rateLimits[].intervalNum | integer (int64) |  | Rate limit interval multiplier.<br>频率限制区间倍数.<br>例: `1` |
| rateLimits[].limit | integer (int64) |  | Maximum allowed orders for this rule.<br>该规则允许的最大订单数。<br>例: `2400` |
| rateLimits[].count | integer (int64) |  | Total number of trades in the 24h window.<br>24 小时窗口内成交总笔数。<br>例: `2` |

## Keepalive User Data Stream (USER_STREAM)（Websocket API延长listenKey有效期 (USER_STREAM)）

`POST /userDataStream.ping`

Keepalive a user data stream to prevent a time out. User data streams
will close after 60 minutes. It's recommended to send a ping about every
60 minutes.

有效期延长至本次调用后60分钟

Operation ID: `keepaliveUserDataStream`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | 例: `e9d6b4349871b40611412680b3445fac` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `userDataStream.ping`<br>例: `userDataStream.ping` |
| params | object | 是 |  |
| params.apiKey | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

```json
{
  "id": "e9d6b4349871b40611412680b3445fac",
  "method": "userDataStream.ping",
  "params": {
    "apiKey": "API_KEY"
  }
}
```

### 响应 Successful Response：Keepalive User Data Stream / Keepalive 用户 Data Stream

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string |  | positionId<br>持仓 ID<br>例: `815d5fce-0880-4287-a567-80badf004c74` |
| status | integer (int64) |  | 例: `200` |
| result | object |  | Indicates that combined is set to true. |
| result.listenKey | string |  | Listen key.<br>监听密钥.<br>例: `3HBntNTepshgEdjIwSUIBgB9keLyOCg5qv3n6bYAtktG8ejcaW5HXz9Vx1JgIieg` |
| rateLimits | object[] |  | Rate limit definitions.<br>频率限制定义. |
| rateLimits[].rateLimitType | string |  | Rate limit type.<br>频率限制类型.<br>例: `REQUEST_WEIGHT` |
| rateLimits[].interval | string |  | Rate limit interval.<br>频率限制区间.<br>例: `MINUTE` |
| rateLimits[].intervalNum | integer (int64) |  | Rate limit interval multiplier.<br>频率限制区间倍数.<br>例: `1` |
| rateLimits[].limit | integer (int64) |  | Maximum allowed orders for this rule.<br>该规则允许的最大订单数。<br>例: `2400` |
| rateLimits[].count | integer (int64) |  | Total number of trades in the 24h window.<br>24 小时窗口内成交总笔数。<br>例: `2` |

## Start User Data Stream (USER_STREAM)（Websocket API生成listenKey (USER_STREAM)）

`POST /userDataStream.start`

Start a new user data stream. The stream will close after 60 minutes
unless a keepalive is sent. If the account has an active `listenKey`,
that `listenKey` will be returned and its validity will be extended for
60 minutes.

创建一个新的user data
stream，返回值为一个listenKey，即websocket订阅的stream名称。如果该帐户具有有效的`listenKey`，则将返回该`listenKey`并将其有效期延长60分钟。

Operation ID: `startUserDataStream`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | 例: `e9d6b4349871b40611412680b3445fac` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `userDataStream.start`<br>例: `userDataStream.start` |
| params | object | 是 |  |
| params.apiKey | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

```json
{
  "id": "e9d6b4349871b40611412680b3445fac",
  "method": "userDataStream.start",
  "params": {
    "apiKey": "API_KEY"
  }
}
```

### 响应 Successful Response：Start User Data Stream / 开始 用户 Data Stream

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string |  | positionId<br>持仓 ID<br>例: `d3df8a61-98ea-4fe0-8f4e-0fcea5d418b0` |
| status | integer (int64) |  | 例: `200` |
| result | object |  | Indicates that combined is set to true. |
| result.listenKey | string |  | Listen key.<br>监听密钥.<br>例: `xs0mRXdAKlIPDRFrlPcw0qI41Eh3ixNntmymGyhrhgqo7L6FuLaWArTD7RLP` |
| rateLimits | object[] |  | Rate limit definitions.<br>频率限制定义. |
| rateLimits[].rateLimitType | string |  | Rate limit type.<br>频率限制类型.<br>例: `REQUEST_WEIGHT` |
| rateLimits[].interval | string |  | Rate limit interval.<br>频率限制区间.<br>例: `MINUTE` |
| rateLimits[].intervalNum | integer (int64) |  | Rate limit interval multiplier.<br>频率限制区间倍数.<br>例: `1` |
| rateLimits[].limit | integer (int64) |  | Maximum allowed orders for this rule.<br>该规则允许的最大订单数。<br>例: `2400` |
| rateLimits[].count | integer (int64) |  | Total number of trades in the 24h window.<br>24 小时窗口内成交总笔数。<br>例: `2` |