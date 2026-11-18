---
exchange: binance
source_url: https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/ws-api
api_type: WebSocket API
updated_at: 2026-11-18 02:46:45.349675
---

# Futures (USDⓈ-M) WebSocket API

Schema: https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/ws-api/1.0.0/schema.yaml

Access market data, manage accounts, and trade USDⓈ-M perpetual futures.

访问市场数据、管理账户，并交易 USDⓈ-M 永续合约。

版本: 1.0.0

## 服务地址

- `wss://ws-fapi.binance.com/ws-fapi/v1`
- `wss://testnet.binancefuture.com/ws-fapi/v1`

## 接口列表

- `POST /account.status` — Account Information (USER_DATA)
- `POST /v2/account.status` — Account Information V2 (USER_DATA)
- `POST /account.balance` — Futures Account Balance (USER_DATA)
- `POST /v2/account.balance` — Futures Account Balance V2 (USER_DATA)
- `POST /depth` — Order Book
- `POST /ticker.book` — Symbol Order Book Ticker
- `POST /ticker.price` — Symbol Price Ticker
- `POST /algoOrder.cancel` — Cancel Algo Order (TRADE)
- `POST /order.cancel` — Cancel Order (TRADE)
- `POST /order.modify` — Modify Order (TRADE)
- `POST /algoOrder.place` — New Algo Order (TRADE)
- `POST /order.place` — New Order (TRADE)
- `POST /account.position` — Position Information (USER_DATA)
- `POST /v2/account.position` — Position Information V2 (USER_DATA)
- `POST /order.status` — Query Order (USER_DATA)
- `POST /userDataStream.stop` — Close User Data Stream (USER_STREAM)
- `POST /userDataStream.ping` — Keepalive User Data Stream (USER_STREAM)
- `POST /userDataStream.start` — Start User Data Stream (USER_STREAM)

## Account Information (USER_DATA)（账户信息 (USER_DATA)）

`POST /account.status`

Get current account information. User in single-asset/ multi-assets mode will see different value, see comments in response section for detail.

现有账户信息。 用户在单资产模式和多资产模式下会看到不同结果，响应部分的注释解释了两种模式下的不同。

Operation ID: `accountInformation`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | Id.<br>请求 ID。<br>例: `e9d6b4349871b40611412680b3445fac` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `account.status`<br>例: `account.status` |
| params | object | 是 |  |
| params.recvWindow | integer (int64) |  | Recv Window.<br>接收窗口。<br>例: `5000` |
| params.timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |
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
| id | string |  | 例: `605a6d20-6588-4cb9-afa0-b0ab087507ba` |
| status | integer (int64) |  | 例: `200` |
| result | object |  |  |
| result.feeTier | integer (int64) |  | account commission tier<br>手续费等级<br>例: `0` |
| result.canTrade | boolean |  | if can trade<br>是否可交易<br>例: `True` |
| result.canDeposit | boolean |  | if can transfer in asset<br>是否可入金<br>例: `True` |
| result.canWithdraw | boolean |  | if can transfer out asset<br>是否可出金<br>例: `True` |
| result.updateTime | integer (int64) |  | reserved property, please ignore<br>保留字段，请忽略<br>例: `0` |
| result.multiAssetsMargin | boolean |  | 例: `True` |
| result.tradeGroupId | integer (int64) |  | 例: `-1` |
| result.totalInitialMargin | string |  | total initial margin required with current mark price (useless with isolated positions), only for USDT asset<br>例: `0.00000000` |
| result.totalMaintMargin | string |  | the sum of USD value of all cross positions maintenance margin<br>全仓持仓维持保证金总额（USD 计价）。<br>例: `0.00000000` |
| result.totalWalletBalance | string |  | total wallet balance, only for USDT asset<br>账户总钱包余额，仅 USDT 资产。<br>例: `126.72469206` |
| result.totalUnrealizedProfit | string |  | total unrealized profit, only for USDT asset<br>未实现盈亏总额，仅 USDT 资产。<br>例: `0.00000000` |
| result.totalMarginBalance | string |  | total margin balance, only for USDT asset<br>保证金余额总额，仅 USDT 资产。<br>例: `126.72469206` |
| result.totalPositionInitialMargin | string |  | initial margin required for positions with current mark price, only for USDT asset<br>例: `0.00000000` |
| result.totalOpenOrderInitialMargin | string |  | initial margin required for open orders with current mark price, only for USDT asset<br>例: `0.00000000` |
| result.totalCrossWalletBalance | string |  | crossed wallet balance, only for USDT asset<br>全仓钱包余额，仅 USDT 资产。<br>例: `126.72469206` |
| result.totalCrossUnPnl | string |  | unrealized profit of crossed positions, only for USDT asset<br>全仓持仓未实现盈亏，仅 USDT 资产。<br>例: `0.00000000` |
| result.availableBalance | string |  | available balance, only for USDT asset<br>可用余额，仅 USDT 资产。<br>例: `126.72469206` |
| result.maxWithdrawAmount | string |  | maximum amount for transfer out, only for USDT asset<br>最大可转出金额，仅 USDT 资产。<br>例: `126.72469206` |
| result.assets | object[] |  |  |
| result.assets[].asset | string |  | asset name<br>资产名称<br>例: `USDT` |
| result.assets[].walletBalance | string |  | wallet balance<br>钱包余额<br>例: `23.72469206` |
| result.assets[].unrealizedProfit | string |  | unrealized profit<br>未实现盈亏<br>例: `0.00000000` |
| result.assets[].marginBalance | string |  | margin balance<br>保证金余额<br>例: `23.72469206` |
| result.assets[].maintMargin | string |  | maintenance margin required<br>所需维持保证金<br>例: `0.00000000` |
| result.assets[].initialMargin | string |  | total initial margin required with current mark price<br>当前标记价格下所需总起始保证金。<br>例: `0.00000000` |
| result.assets[].positionInitialMargin | string |  | initial margin required for positions with current mark price<br>当前标记价格下持仓所需起始保证金。<br>例: `0.00000000` |
| result.assets[].openOrderInitialMargin | string |  | initial margin required for open orders with current mark price<br>当前标记价格下挂单所需起始保证金。<br>例: `0.00000000` |
| result.assets[].crossWalletBalance | string |  | crossed wallet balance<br>全仓钱包余额<br>例: `23.72469206` |
| result.assets[].crossUnPnl | string |  | unrealized profit of crossed positions<br>全仓持仓未实现盈亏<br>例: `0.00000000` |
| result.assets[].availableBalance | string |  | available balance, only for USDT asset<br>可用余额，仅 USDT 资产。<br>例: `126.72469206` |
| result.assets[].maxWithdrawAmount | string |  | maximum amount for transfer out, only for USDT asset<br>最大可转出金额，仅 USDT 资产。<br>例: `23.72469206` |
| result.assets[].marginAvailable | boolean |  | whether the asset can be used as margin in Multi-Assets mode<br>该资产是否可在多资产模式下作为保证金。<br>例: `True` |
| result.assets[].updateTime | integer (int64) |  | reserved property, please ignore<br>保留字段，请忽略<br>例: `1625474304765` |
| result.positions | object[] |  | positions of all symbols in the market are returned<br>返回市场中所有交易对的持仓。 |
| result.positions[].symbol | string |  | symbol name<br>交易对名称<br>例: `BTCUSDT` |
| result.positions[].initialMargin | string |  | total initial margin required with current mark price<br>当前标记价格下所需总起始保证金。<br>例: `0` |
| result.positions[].maintMargin | string |  | maintenance margin required<br>所需维持保证金<br>例: `0` |
| result.positions[].unrealizedProfit | string |  | unrealized profit<br>未实现盈亏<br>例: `0.00000000` |
| result.positions[].positionInitialMargin | string |  | initial margin required for positions with current mark price<br>当前标记价格下持仓所需起始保证金。<br>例: `0` |
| result.positions[].openOrderInitialMargin | string |  | initial margin required for open orders with current mark price<br>当前标记价格下挂单所需起始保证金。<br>例: `0` |
| result.positions[].leverage | string |  | current initial leverage<br>当前初始杠杆<br>例: `100` |
| result.positions[].isolated | boolean |  | if the position is isolated<br>是否逐仓持仓<br>例: `True` |
| result.positions[].entryPrice | string |  | average entry price<br>持仓成本价<br>例: `0.00000` |
| result.positions[].maxNotional | string |  | maximum available notional with current leverage<br>当前杠杆下最大可用名义价值。<br>例: `250000` |
| result.positions[].bidNotional | string |  | bids notional, ignore<br>买单名义价值（忽略）。<br>例: `0` |
| result.positions[].askNotional | string |  | ask notional, ignore<br>卖单名义价值（忽略）。<br>例: `0` |
| result.positions[].positionSide | string |  | position side<br>持仓方向<br>例: `BOTH` |
| result.positions[].positionAmt | string |  | position amount<br>持仓数量<br>例: `0` |
| result.positions[].updateTime | integer (int64) |  | reserved property, please ignore<br>保留字段，请忽略<br>例: `0` |
| result.positions[].breakEvenPrice | string |  | average entry price<br>持仓成本价<br>例: `0.0` |
| rateLimits | object[] |  |  |
| rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| rateLimits[].interval | string |  | 例: `MINUTE` |
| rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| rateLimits[].limit | integer (int64) |  | 例: `2400` |
| rateLimits[].count | integer (int64) |  | 例: `20` |

## Account Information V2 (USER_DATA)（账户信息V2 (USER_DATA)）

`POST /v2/account.status`

Get current account information. User in single-asset/ multi-assets mode will see different value, see comments in response section for detail.

现有账户信息。 用户在单资产模式和多资产模式下会看到不同结果，响应部分的注释解释了两种模式下的不同。

Operation ID: `accountInformationV2`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | Id.<br>请求 ID。<br>例: `e9d6b4349871b40611412680b3445fac` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `v2/account.status`<br>例: `v2/account.status` |
| params | object | 是 |  |
| params.recvWindow | integer (int64) |  | Recv Window.<br>接收窗口。<br>例: `5000` |
| params.timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |
| params.apiKey | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

```json
{
  "id": "e9d6b4349871b40611412680b3445fac",
  "method": "v2/account.status",
  "params": {
    "recvWindow": 5000,
    "timestamp": 1770736694138,
    "apiKey": "API_KEY"
  }
}
```

### 响应 Successful Response：Account Information V2 / 账户 信息 V2

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string |  | 例: `605a6d20-6588-4cb9-afa0-b0ab087507ba` |
| status | integer (int64) |  | 例: `200` |
| result | object |  |  |
| result.totalInitialMargin | string |  | total initial margin required with current mark price (useless with isolated positions), only for USDT asset<br>例: `0.00000000` |
| result.totalMaintMargin | string |  | the sum of USD value of all cross positions maintenance margin<br>全仓持仓维持保证金总额（USD 计价）。<br>例: `0.00000000` |
| result.totalWalletBalance | string |  | total wallet balance, only for USDT asset<br>账户总钱包余额，仅 USDT 资产。<br>例: `126.72469206` |
| result.totalUnrealizedProfit | string |  | total unrealized profit, only for USDT asset<br>未实现盈亏总额，仅 USDT 资产。<br>例: `0.00000000` |
| result.totalMarginBalance | string |  | total margin balance, only for USDT asset<br>保证金余额总额，仅 USDT 资产。<br>例: `126.72469206` |
| result.totalPositionInitialMargin | string |  | initial margin required for positions with current mark price, only for USDT asset<br>例: `0.00000000` |
| result.totalOpenOrderInitialMargin | string |  | initial margin required for open orders with current mark price, only for USDT asset<br>例: `0.00000000` |
| result.totalCrossWalletBalance | string |  | crossed wallet balance, only for USDT asset<br>全仓钱包余额，仅 USDT 资产。<br>例: `126.72469206` |
| result.totalCrossUnPnl | string |  | unrealized profit of crossed positions, only for USDT asset<br>全仓持仓未实现盈亏，仅 USDT 资产。<br>例: `0.00000000` |
| result.availableBalance | string |  | available balance, only for USDT asset<br>可用余额，仅 USDT 资产。<br>例: `126.72469206` |
| result.maxWithdrawAmount | string |  | maximum amount for transfer out, only for USDT asset<br>最大可转出金额，仅 USDT 资产。<br>例: `126.72469206` |
| result.assets | object[] |  | For assets that are quote assets, USDT/USDC/BTC<br>报价资产列表（USDT/USDC/BTC）。 |
| result.assets[].asset | string |  | asset name<br>资产名称<br>例: `USDT` |
| result.assets[].walletBalance | string |  | wallet balance<br>钱包余额<br>例: `23.72469206` |
| result.assets[].unrealizedProfit | string |  | unrealized profit<br>未实现盈亏<br>例: `0.00000000` |
| result.assets[].marginBalance | string |  | margin balance<br>保证金余额<br>例: `23.72469206` |
| result.assets[].maintMargin | string |  | maintenance margin required<br>所需维持保证金<br>例: `0.00000000` |
| result.assets[].initialMargin | string |  | total initial margin required with current mark price<br>当前标记价格下所需总起始保证金。<br>例: `0.00000000` |
| result.assets[].positionInitialMargin | string |  | initial margin required for positions with current mark price<br>当前标记价格下持仓所需起始保证金。<br>例: `0.00000000` |
| result.assets[].openOrderInitialMargin | string |  | initial margin required for open orders with current mark price<br>当前标记价格下挂单所需起始保证金。<br>例: `0.00000000` |
| result.assets[].crossWalletBalance | string |  | crossed wallet balance<br>全仓钱包余额<br>例: `23.72469206` |
| result.assets[].crossUnPnl | string |  | unrealized profit of crossed positions<br>全仓持仓未实现盈亏<br>例: `0.00000000` |
| result.assets[].availableBalance | string |  | available balance, only for USDT asset<br>可用余额，仅 USDT 资产。<br>例: `23.72469206` |
| result.assets[].maxWithdrawAmount | string |  | maximum amount for transfer out, only for USDT asset<br>最大可转出金额，仅 USDT 资产。<br>例: `23.72469206` |
| result.assets[].marginAvailable | boolean |  | whether the asset can be used as margin in Multi-Assets mode<br>该资产是否可在多资产模式下作为保证金。<br>例: `True` |
| result.assets[].updateTime | integer (int64) |  | last update time<br>最后更新时间<br>例: `1625474304765` |
| result.positions | object[] |  | positions of all symbols user had position/ open orders are returned<br>返回用户有持仓或有挂单的所有交易对持仓。 |
| result.positions[].symbol | string |  | 例: `BTCUSDT` |
| result.positions[].positionSide | string |  | position side<br>持仓方向<br>例: `BOTH` |
| result.positions[].positionAmt | string |  | 例: `1.000` |
| result.positions[].unrealizedProfit | string |  | unrealized profit<br>未实现盈亏<br>例: `0.00000000` |
| result.positions[].isolatedMargin | string |  | 例: `0.00000000` |
| result.positions[].notional | string |  | 例: `0` |
| result.positions[].isolatedWallet | string |  | 例: `0` |
| result.positions[].initialMargin | string |  | total initial margin required with current mark price<br>当前标记价格下所需总起始保证金。<br>例: `0` |
| result.positions[].maintMargin | string |  | maintenance margin required<br>所需维持保证金<br>例: `0` |
| result.positions[].updateTime | integer (int64) |  | last update time<br>最后更新时间<br>例: `0` |
| rateLimits | object[] |  |  |
| rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| rateLimits[].interval | string |  | 例: `MINUTE` |
| rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| rateLimits[].limit | integer (int64) |  | 例: `2400` |
| rateLimits[].count | integer (int64) |  | 例: `20` |

## Futures Account Balance (USER_DATA)（账户余额 (USER_DATA)）

`POST /account.balance`

Futures Account Balance

账户余额

Operation ID: `futuresAccountBalance`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | Id.<br>请求 ID。<br>例: `e9d6b4349871b40611412680b3445fac` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `account.balance`<br>例: `account.balance` |
| params | object | 是 |  |
| params.recvWindow | integer (int64) |  | Recv Window.<br>接收窗口。<br>例: `5000` |
| params.timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |
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

### 响应 Successful Response：Futures Account Balance / 合约账户余额

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string |  | 例: `605a6d20-6588-4cb9-afa0-b0ab087507ba` |
| status | integer (int64) |  | 例: `200` |
| result | object[] |  |  |
| result[].accountAlias | string |  | unique account code<br>唯一账户标识<br>例: `SgsR` |
| result[].asset | string |  | asset name<br>资产名称<br>例: `USDT` |
| result[].balance | string |  | wallet balance<br>钱包余额<br>例: `122607.35137903` |
| result[].crossWalletBalance | string |  | crossed wallet balance<br>全仓钱包余额<br>例: `23.72469206` |
| result[].crossUnPnl | string |  | unrealized profit of crossed positions<br>全仓持仓未实现盈亏<br>例: `0.00000000` |
| result[].availableBalance | string |  | available balance<br>可用余额<br>例: `23.72469206` |
| result[].maxWithdrawAmount | string |  | maximum amount for transfer out<br>最大可转出金额<br>例: `23.72469206` |
| result[].marginAvailable | boolean |  | whether the asset can be used as margin in Multi-Assets mode<br>该资产是否可在多资产模式下作为保证金。<br>例: `True` |
| result[].updateTime | integer (int64) |  | 例: `1617939110373` |
| rateLimits | object[] |  |  |
| rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| rateLimits[].interval | string |  | 例: `MINUTE` |
| rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| rateLimits[].limit | integer (int64) |  | 例: `2400` |
| rateLimits[].count | integer (int64) |  | 例: `20` |

## Futures Account Balance V2 (USER_DATA)（账户余额V2 (USER_DATA)）

`POST /v2/account.balance`

Futures Account Balance V2

账户余额V2

Operation ID: `futuresAccountBalanceV2`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | Id.<br>请求 ID。<br>例: `e9d6b4349871b40611412680b3445fac` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `v2/account.balance`<br>例: `v2/account.balance` |
| params | object | 是 |  |
| params.recvWindow | integer (int64) |  | Recv Window.<br>接收窗口。<br>例: `5000` |
| params.timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |
| params.apiKey | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

```json
{
  "id": "e9d6b4349871b40611412680b3445fac",
  "method": "v2/account.balance",
  "params": {
    "recvWindow": 5000,
    "timestamp": 1770736694138,
    "apiKey": "API_KEY"
  }
}
```

### 响应 Successful Response：Futures Account Balance V2 / 合约账户余额 V2

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string |  | 例: `605a6d20-6588-4cb9-afa0-b0ab087507ba` |
| status | integer (int64) |  | 例: `200` |
| result | object[] |  |  |
| result[].accountAlias | string |  | unique account code<br>唯一账户标识<br>例: `SgsR` |
| result[].asset | string |  | asset name<br>资产名称<br>例: `USDT` |
| result[].balance | string |  | wallet balance<br>钱包余额<br>例: `122607.35137903` |
| result[].crossWalletBalance | string |  | crossed wallet balance<br>全仓钱包余额<br>例: `23.72469206` |
| result[].crossUnPnl | string |  | unrealized profit of crossed positions<br>全仓持仓未实现盈亏<br>例: `0.00000000` |
| result[].availableBalance | string |  | available balance<br>可用余额<br>例: `23.72469206` |
| result[].maxWithdrawAmount | string |  | maximum amount for transfer out<br>最大可转出金额<br>例: `23.72469206` |
| result[].marginAvailable | boolean |  | whether the asset can be used as margin in Multi-Assets mode<br>该资产是否可在多资产模式下作为保证金。<br>例: `True` |
| result[].updateTime | integer (int64) |  | 例: `1617939110373` |
| rateLimits | object[] |  |  |
| rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| rateLimits[].interval | string |  | 例: `MINUTE` |
| rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| rateLimits[].limit | integer (int64) |  | 例: `2400` |
| rateLimits[].count | integer (int64) |  | 例: `20` |

## Order Book（深度信息）

`POST /depth`

Get current order book. Note that this request returns limited market
depth.

If you need to continuously monitor order book updates, please consider
using Websocket Market Streams:
  * `<symbol>@depth<levels>`
  * `<symbol>@depth`

You can use `depth` request together with `<symbol>@depth` streams to
maintain a local order book.

**Note:**

- Retail Price Improvement(RPI) orders are not visible and excluded in
the response message.

获取当前订单簿。请注意，此请求返回有限的市场深度。
如果您需要持续监控订单簿更新，请考虑使用Websocket市场流：
  * `<symbol>@depth<levels>`
  * `<symbol>@depth`

您可以将`depth`请求与`<symbol>@depth`流一起使用以维护本地订单簿。
**注意：**
- 零点价订单在响应消息中不可见且被排除在外。

权重: Adjusted based on the limit:

| Limit         | Weight |
| ------------- | ------ |
| 5, 10, 20, 50 | 2      |
| 100           | 5      |
| 500           | 10     |
| 1000          | 20     |

Operation ID: `orderBook`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | Id.<br>请求 ID。<br>例: `e9d6b4349871b40611412680b3445fac` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `depth`<br>例: `depth` |
| params | object | 是 |  |
| params.symbol | string | 是 | Symbol.<br>交易对。<br>例: `BTCUSDT` |
| params.limit | integer (int64) |  | Valid limits:[5, 10, 20, 50, 100, 500, 1000]<br>有效限制：[5, 10, 20, 50, 100, 500, 1000]<br>默认: `500`<br>例: `10` |

```json
{
  "id": "e9d6b4349871b40611412680b3445fac",
  "method": "depth",
  "params": {
    "symbol": "BTCUSDT",
    "limit": 10
  }
}
```

### 响应 Successful Response：Order Book / 订单簿

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string |  | 例: `51e2affb-0aba-4821-ba75-f2625006eb43` |
| status | integer (int64) |  | 例: `200` |
| result | object |  |  |
| result.lastUpdateId | integer (int64) |  | 例: `1027024` |
| result.E | integer (int64) |  | Message output time<br>消息输出时间<br>例: `1589436922972` |
| result.T | integer (int64) |  | Transaction time<br>成交时间<br>例: `1589436922959` |
| bids | oneOf[][] |  | Bid orders. Each entry is [price, quantity].<br>买单列表。每项为 [价格, 数量]。 |
| asks | oneOf[][] |  | Ask orders. Each entry is [price, quantity].<br>卖单列表。每项为 [价格, 数量]。 |
| rateLimits | object[] |  |  |
| rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| rateLimits[].interval | string |  | 例: `MINUTE` |
| rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| rateLimits[].limit | integer (int64) |  | 例: `2400` |
| rateLimits[].count | integer (int64) |  | 例: `5` |

## Symbol Order Book Ticker（当前最优挂单）

`POST /ticker.book`

Best price/qty on the order book for a symbol or symbols.

**Note:**

- Retail Price Improvement(RPI) orders are not visible and excluded in
the response message.

交易对订单簿最优挂单价格和数量。
**注意：**
- 零售价格改进（RPI）订单在响应消息中不可见且被排除在外。

权重: **2** for a single symbol;
**5** when the symbol parameter is omitted

Operation ID: `symbolOrderBookTicker`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | Id.<br>请求 ID。<br>例: `e9d6b4349871b40611412680b3445fac` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `ticker.book`<br>例: `ticker.book` |
| params | object |  |  |
| params.symbol | string |  | Symbol.<br>交易对。<br>例: `BTCUSDT` |

```json
{
  "id": "e9d6b4349871b40611412680b3445fac",
  "method": "ticker.book",
  "params": {
    "symbol": "BTCUSDT"
  }
}
```

### 响应 Successful Response：Symbol Order Book Ticker / 交易对 订单 最优挂单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| (oneOf 1).id | string |  | 例: `9d32157c-a556-4d27-9866-66760a174b57` |
| (oneOf 1).status | integer (int64) |  | 例: `200` |
| (oneOf 1).result | object |  |  |
| (oneOf 1).result.lastUpdateId | integer (int64) |  | 例: `1027024` |
| (oneOf 1).result.symbol | string |  | 例: `BTCUSDT` |
| (oneOf 1).result.bidPrice | string |  | 例: `4.00000000` |
| (oneOf 1).result.bidQty | string |  | 例: `431.00000000` |
| (oneOf 1).result.askPrice | string |  | 例: `4.00000200` |
| (oneOf 1).result.askQty | string |  | 例: `9.00000000` |
| (oneOf 1).result.time | integer (int64) |  | Transaction time<br>成交时间<br>例: `1589437530011` |
| (oneOf 1).rateLimits | object[] |  |  |
| (oneOf 1).rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| (oneOf 1).rateLimits[].interval | string |  | 例: `MINUTE` |
| (oneOf 1).rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| (oneOf 1).rateLimits[].limit | integer (int64) |  | 例: `2400` |
| (oneOf 1).rateLimits[].count | integer (int64) |  | 例: `2` |
| (oneOf 2).id | string |  | 例: `9d32157c-a556-4d27-9866-66760a174b57` |
| (oneOf 2).status | integer (int64) |  | 例: `200` |
| (oneOf 2).result | object[] |  |  |
| (oneOf 2).result[].lastUpdateId | integer (int64) |  | 例: `1027024` |
| (oneOf 2).result[].symbol | string |  | 例: `BTCUSDT` |
| (oneOf 2).result[].bidPrice | string |  | 例: `4.00000000` |
| (oneOf 2).result[].bidQty | string |  | 例: `431.00000000` |
| (oneOf 2).result[].askPrice | string |  | 例: `4.00000200` |
| (oneOf 2).result[].askQty | string |  | 例: `9.00000000` |
| (oneOf 2).result[].time | integer (int64) |  | Transaction time<br>成交时间<br>例: `1589437530011` |
| (oneOf 2).rateLimits | object[] |  |  |
| (oneOf 2).rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| (oneOf 2).rateLimits[].interval | string |  | 例: `MINUTE` |
| (oneOf 2).rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| (oneOf 2).rateLimits[].limit | integer (int64) |  | 例: `2400` |
| (oneOf 2).rateLimits[].count | integer (int64) |  | 例: `2` |

## Symbol Price Ticker（最新价格）

`POST /ticker.price`

Latest price for a symbol or symbols.

返回最近价格

权重: **1** for a single symbol;
**2** when the symbol parameter is omitted

Operation ID: `symbolPriceTicker`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | Id.<br>请求 ID。<br>例: `e9d6b4349871b40611412680b3445fac` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `ticker.price`<br>例: `ticker.price` |
| params | object |  |  |
| params.symbol | string |  | Symbol.<br>交易对。<br>例: `BTCUSDT` |

```json
{
  "id": "e9d6b4349871b40611412680b3445fac",
  "method": "ticker.price",
  "params": {
    "symbol": "BTCUSDT"
  }
}
```

### 响应 Successful Response：Symbol Price Ticker / 交易对 价格 行情

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| (oneOf 1).id | string |  | 例: `9d32157c-a556-4d27-9866-66760a174b57` |
| (oneOf 1).status | integer (int64) |  | 例: `200` |
| (oneOf 1).result | object |  |  |
| (oneOf 1).result.symbol | string |  | 例: `BTCUSDT` |
| (oneOf 1).result.price | string |  | 例: `6000.01` |
| (oneOf 1).result.time | integer (int64) |  | Transaction time<br>成交时间<br>例: `1589437530011` |
| (oneOf 1).rateLimits | object[] |  |  |
| (oneOf 1).rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| (oneOf 1).rateLimits[].interval | string |  | 例: `MINUTE` |
| (oneOf 1).rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| (oneOf 1).rateLimits[].limit | integer (int64) |  | 例: `2400` |
| (oneOf 1).rateLimits[].count | integer (int64) |  | 例: `2` |
| (oneOf 2).id | string |  | 例: `9d32157c-a556-4d27-9866-66760a174b57` |
| (oneOf 2).status | integer (int64) |  | 例: `200` |
| (oneOf 2).result | object[] |  |  |
| (oneOf 2).result[].symbol | string |  | 例: `BTCUSDT` |
| (oneOf 2).result[].price | string |  | 例: `6000.01` |
| (oneOf 2).result[].time | integer (int64) |  | Transaction time<br>成交时间<br>例: `1589437530011` |
| (oneOf 2).rateLimits | object[] |  |  |
| (oneOf 2).rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| (oneOf 2).rateLimits[].interval | string |  | 例: `MINUTE` |
| (oneOf 2).rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| (oneOf 2).rateLimits[].limit | integer (int64) |  | 例: `2400` |
| (oneOf 2).rateLimits[].count | integer (int64) |  | 例: `2` |

## Cancel Algo Order (TRADE)（条件单撤销订单 (TRADE)）

`POST /algoOrder.cancel`

Cancel an active algo order.

撤销条件订单

Operation ID: `cancelAlgoOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | Id.<br>请求 ID。<br>例: `e9d6b4349871b40611412680b3445fac` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `algoOrder.cancel`<br>例: `algoOrder.cancel` |
| params | object | 是 |  |
| params.algoId | integer (int64) |  | Algo Id.<br>条件单 ID。<br>例: `2000000002162519` |
| params.clientAlgoId | string |  | Client Algo Id.<br>自定义条件单 ID。<br>例: `rDMG8WSde6LkyMNtk6s825` |
| params.recvWindow | integer (int64) |  | Recv Window.<br>接收窗口。<br>例: `5000` |
| params.timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |
| params.apiKey | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

```json
{
  "id": "e9d6b4349871b40611412680b3445fac",
  "method": "algoOrder.cancel",
  "params": {
    "algoId": 2000000002162519,
    "clientAlgoId": "rDMG8WSde6LkyMNtk6s825",
    "recvWindow": 5000,
    "timestamp": 1770736694138,
    "apiKey": "API_KEY"
  }
}
```

### 响应 Successful Response：Cancel Algo Order / 取消Algo 订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string |  | 例: `unique-cancel-request-id-5678` |
| status | integer (int64) |  | 例: `200` |
| result | object |  |  |
| result.algoId | integer (int64) |  | 例: `2000000002162519` |
| result.clientAlgoId | string |  | 例: `rDMG8WSde6LkyMNtk6s825` |
| result.code | string |  | 例: `200` |
| result.msg | string |  | 例: `success` |
| rateLimits | object[] |  |  |
| rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| rateLimits[].interval | string |  | 例: `MINUTE` |
| rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| rateLimits[].limit | integer (int64) |  | 例: `2400` |
| rateLimits[].count | integer (int64) |  | 例: `6` |

## Cancel Order (TRADE)（撤销订单 (TRADE)）

`POST /order.cancel`

Cancel an active order.

撤销订单

Operation ID: `cancelOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | Id.<br>请求 ID。<br>例: `e9d6b4349871b40611412680b3445fac` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `order.cancel`<br>例: `order.cancel` |
| params | object | 是 |  |
| params.symbol | string | 是 | Symbol.<br>交易对。<br>例: `BTCUSDT` |
| params.orderId | integer (int64) |  | Order Id.<br>系统订单号。<br>例: `1` |
| params.origClientOrderId | string |  | Orig Client Order Id.<br>原客户端订单号。<br>例: `1` |
| params.recvWindow | integer (int64) |  | Recv Window.<br>接收窗口。<br>例: `5000` |
| params.timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |
| params.apiKey | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

```json
{
  "id": "e9d6b4349871b40611412680b3445fac",
  "method": "order.cancel",
  "params": {
    "symbol": "BTCUSDT",
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
| id | string |  | 例: `5633b6a2-90a9-4192-83e7-925c90b6a2fd` |
| status | integer (int64) |  | 例: `200` |
| result | object |  |  |
| result.clientOrderId | string |  | 例: `myOrder1` |
| result.cumQty | string |  | 例: `0` |
| result.executedQty | string |  | 例: `0` |
| result.orderId | integer (int64) |  | 例: `283194212` |
| result.origQty | string |  | 例: `11` |
| result.origType | string |  | 例: `TRAILING_STOP_MARKET` |
| result.price | string |  | 例: `0` |
| result.reduceOnly | boolean |  | 例: `False` |
| result.side | string |  | 例: `BUY` |
| result.positionSide | string |  | 例: `SHORT` |
| result.status | string |  | 例: `CANCELED` |
| result.stopPrice | string |  | 例: `9300` |
| result.closePosition | boolean |  | 例: `False` |
| result.symbol | string |  | 例: `BTCUSDT` |
| result.timeInForce | string |  | 例: `GTC` |
| result.type | string |  | 例: `TRAILING_STOP_MARKET` |
| result.activatePrice | string |  | 例: `9020` |
| result.priceRate | string |  | 例: `0.3` |
| result.updateTime | integer (int64) |  | 例: `1571110484038` |
| result.workingType | string |  | 例: `CONTRACT_PRICE` |
| result.priceProtect | boolean |  | 例: `False` |
| result.priceMatch | string |  | 例: `NONE` |
| result.selfTradePreventionMode | string |  | 例: `EXPIRE_MAKER` |
| result.goodTillDate | integer (int64) |  | 例: `0` |
| rateLimits | object[] |  |  |
| rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| rateLimits[].interval | string |  | 例: `MINUTE` |
| rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| rateLimits[].limit | integer (int64) |  | 例: `2400` |
| rateLimits[].count | integer (int64) |  | 例: `1` |

## Modify Order (TRADE)（修改订单 (TRADE)）

`POST /order.modify`

Order modify function, currently only LIMIT order modification is supported, modified orders will be reordered in the match queue

修改订单功能，当前只支持限价（LIMIT）订单修改，修改后会在撮合队列里重新排序

权重: 1 on 10s order rate limit(X-MBX-ORDER-COUNT-10S);
1 on 1min order rate limit(X-MBX-ORDER-COUNT-1M);
0 on IP rate limit(x-mbx-used-weight-1m)

Operation ID: `modifyOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | Id.<br>请求 ID。<br>例: `e9d6b4349871b40611412680b3445fac` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `order.modify`<br>例: `order.modify` |
| params | object | 是 |  |
| params.orderId | integer (int64) |  | Order Id.<br>系统订单号。<br>例: `1` |
| params.origClientOrderId | string |  | Orig Client Order Id.<br>原客户端订单号。<br>例: `1` |
| params.symbol | string | 是 | Symbol.<br>交易对。<br>例: `BTCUSDT` |
| params.side | string | 是 | `SELL`, `BUY`<br>`SELL`、`BUY`<br>枚举: `BUY`, `SELL`<br>例: `BUY` |
| params.quantity | number (float) | 是 | Order quantity, cannot be sent with `closePosition=true`<br>下单数量，不可与 `closePosition=true` 同时传。<br>例: `1.0` |
| params.price | number (float) | 是 | Price.<br>价格。<br>例: `1.0` |
| params.priceMatch | string |  | only avaliable for LIMIT/STOP/TAKE_PROFIT order; Can't be passed together with price<br>枚举: `OPPONENT`, `OPPONENT_5`, `OPPONENT_10`, `OPPONENT_20`, `QUEUE`, `QUEUE_5`, `QUEUE_10`, `QUEUE_20`<br>例: `OPPONENT` |
| params.modifyId | integer (int64) |  | User-defined modification identifier, returned as-is in the response. Optional; not validated for uniqueness.<br>用户自定义的改单标识，原样返回。可选；服务端不校验唯一性。<br>例: `1` |
| params.reduceOnly | string |  | See notes below for behavior.<br>行为说明见下方备注。<br>枚举: `true`, `false`<br>默认: `false`<br>例: `false` |
| params.recvWindow | integer (int64) |  | Recv Window.<br>接收窗口。<br>例: `5000` |
| params.timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |
| params.apiKey | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

```json
{
  "id": "e9d6b4349871b40611412680b3445fac",
  "method": "order.modify",
  "params": {
    "orderId": 1,
    "origClientOrderId": "1",
    "symbol": "BTCUSDT",
    "side": "BUY",
    "quantity": "1.0",
    "price": "1.0",
    "priceMatch": "OPPONENT",
    "modifyId": 1,
    "reduceOnly": "false",
    "recvWindow": 5000,
    "timestamp": 1770736694138,
    "apiKey": "API_KEY"
  }
}
```

### 响应 Successful Response：Modify Order / 修改订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string |  | 例: `c8c271ba-de70-479e-870c-e64951c753d9` |
| status | integer (int64) |  | 例: `200` |
| result | object |  |  |
| result.orderId | integer (int64) |  | 例: `328971409` |
| result.symbol | string |  | 例: `BTCUSDT` |
| result.status | string |  | 例: `NEW` |
| result.clientOrderId | string |  | 例: `xGHfltUMExx0TbQstQQfRX` |
| result.modifyId | integer (int64) |  | user-defined modification identifier, only returned if provided in the request<br>用户自定义的改单标识，仅当请求中传入时返回<br>例: `1` |
| result.price | string |  | 例: `43769.10` |
| result.origQty | string |  | 例: `0.110` |
| result.executedQty | string |  | 例: `0.000` |
| result.cumQty | string |  | 例: `0.000` |
| result.timeInForce | string |  | 例: `GTC` |
| result.type | string |  | 例: `LIMIT` |
| result.reduceOnly | boolean |  | 例: `False` |
| result.closePosition | boolean |  | 例: `False` |
| result.side | string |  | 例: `SELL` |
| result.positionSide | string |  | 例: `SHORT` |
| result.stopPrice | string |  | 例: `0.00` |
| result.workingType | string |  | 例: `CONTRACT_PRICE` |
| result.priceProtect | boolean |  | 例: `False` |
| result.origType | string |  | 例: `LIMIT` |
| result.priceMatch | string |  | 例: `NONE` |
| result.selfTradePreventionMode | string |  | 例: `EXPIRE_MAKER` |
| result.goodTillDate | integer (int64) |  | 例: `0` |
| result.updateTime | integer (int64) |  | 例: `1703426756190` |
| rateLimits | object[] |  |  |
| rateLimits[].rateLimitType | string |  | 例: `ORDERS` |
| rateLimits[].interval | string |  | 例: `SECOND` |
| rateLimits[].intervalNum | integer (int64) |  | 例: `10` |
| rateLimits[].limit | integer (int64) |  | 例: `300` |
| rateLimits[].count | integer (int64) |  | 例: `1` |

## New Algo Order (TRADE)（条件单下单 (TRADE)）

`POST /algoOrder.place`

Send in a new algo order.

条件单下单

Operation ID: `newAlgoOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | Id.<br>请求 ID。<br>例: `e9d6b4349871b40611412680b3445fac` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `algoOrder.place`<br>例: `algoOrder.place` |
| params | object | 是 |  |
| params.algoType | string | 是 | Only support `CONDITIONAL`<br>仅支持 `CONDITIONAL`。<br>枚举: `CONDITIONAL`<br>例: `CONDITIONAL` |
| params.symbol | string | 是 | Symbol.<br>交易对。<br>例: `BTCUSDT` |
| params.side | string | 是 | Side.<br>买卖方向。<br>枚举: `BUY`, `SELL`<br>例: `BUY` |
| params.positionSide | string |  | Default BOTH for One-way Mode ; LONG or SHORT for Hedge Mode. It must be sent in Hedge Mode.<br>单向模式默认 `BOTH`；双向模式可为 `LONG` 或 `SHORT`，双向模式必传。<br>枚举: `BOTH`, `LONG`, `SHORT`<br>例: `BOTH` |
| params.type | string | 是 | For `CONDITIONAL` algoType, `STOP_MARKET`/`TAKE_PROFIT_MARKET`/`STOP`/`TAKE_PROFIT`/`TRAILING_STOP_MARKET` as order type<br>当 algoType=`CONDITIONAL` 时，订单类型可为 `STOP_MARKET`/`TAKE_PROFIT_MARKET`/`STOP`/`TAKE_PROFIT`/`TRAILING_STOP_MARKET` 之一。<br>枚举: `STOP_MARKET`, `TAKE_PROFIT_MARKET`, `STOP`, `TAKE_PROFIT`, `TRAILING_STOP_MARKET`<br>例: `STOP_MARKET` |
| params.timeInForce | string |  | `IOC` or `GTC` or `FOK`, default `GTC`<br>`IOC`、`GTC` 或 `FOK`，默认 `GTC`。<br>枚举: `IOC`, `GTC`, `FOK`<br>例: `GTC` |
| params.quantity | number (float) |  | Cannot be sent with `closePosition`=`true`(Close-All)<br>不可与 `closePosition=true`（全平）同时传。<br>例: `1.0` |
| params.price | number (float) |  | Price.<br>价格。<br>例: `1.0` |
| params.triggerPrice | number (float) |  | Trigger Price.<br>触发价格。<br>例: `1.0` |
| params.workingType | string |  | triggerPrice triggered by: `MARK_PRICE`, `CONTRACT_PRICE`. Default `CONTRACT_PRICE`<br>触发价格类型：`MARK_PRICE` 或 `CONTRACT_PRICE`，默认 `CONTRACT_PRICE`。<br>枚举: `MARK_PRICE`, `CONTRACT_PRICE`<br>默认: `CONTRACT_PRICE`<br>例: `MARK_PRICE` |
| params.priceMatch | string |  | only avaliable for LIMIT/STOP/TAKE_PROFIT order; Can't be passed together with price<br>仅适用于 LIMIT/STOP/TAKE_PROFIT；不可与 price 同时传。<br>枚举: `OPPONENT`, `OPPONENT_5`, `OPPONENT_10`, `OPPONENT_20`, `QUEUE`, `QUEUE_5`, `QUEUE_10`, `QUEUE_20`<br>例: `OPPONENT` |
| params.closePosition | string |  | Close-All，used with STOP_MARKET or TAKE_PROFIT_MARKET.<br>全平，仅用于 `STOP_MARKET` 或 `TAKE_PROFIT_MARKET`。<br>枚举: `true`, `false`<br>例: `true` |
| params.priceProtect | string |  | Used with STOP_MARKET or TAKE_PROFIT_MARKET order. when price reaches the triggerPrice ，the difference rate between "MARK_PRICE" and "CONTRACT_PRICE" cannot be larger than the Price Protection Threshold of the symbol.<br>用于 STOP_MARKET 或 TAKE_PROFIT_MARKET；当价格触达 triggerPrice 时，MARK_PRICE 与 CONTRACT_PRICE 的价差比例不得超过该交易对的价格保护阈值。<br>枚举: `true`, `false`<br>默认: `false`<br>例: `true` |
| params.reduceOnly | string |  | Cannot be sent in Hedge Mode; cannot be sent with closePosition=true<br>双向持仓模式不可传；不可与 closePosition=true 同时传。<br>枚举: `true`, `false`<br>默认: `false`<br>例: `true` |
| params.activatePrice | number (float) |  | Used with TRAILING_STOP_MARKET orders, default as the latest price(supporting different workingType)<br>仅用于 TRAILING_STOP_MARKET，默认使用最新价（支持不同 workingType）。<br>例: `1.0` |
| params.callbackRate | number (float) |  | Used with TRAILING_STOP_MARKET orders<br>仅用于 `TRAILING_STOP_MARKET`。<br>例: `1` |
| params.clientAlgoId | string |  | A unique id among open orders. Automatically generated if not sent. Can only be string following the rule: `^[\.A-Z\:/a-z0-9_-]{1,36}$`<br>挂单中的唯一客户端订单 ID；未传则自动生成。仅支持匹配 `^[\\.A-Z\\:/a-z0-9_-]{1,36}$` 的字符串。<br>例: `1` |
| params.newOrderRespType | string |  | "ACK", "RESULT", default "ACK"<br>`ACK` 或 `RESULT`，默认 `ACK`。<br>枚举: `ACK`, `RESULT`<br>例: `ACK` |
| params.selfTradePreventionMode | string |  | `EXPIRE_TAKER`: expire taker order when STP triggers/ `EXPIRE_MAKER`: expire taker order when STP triggers/ `EXPIRE_BOTH`: expire both orders when STP triggers; default `NONE`<br>`EXPIRE_TAKER`（触发时撤吃单）/ `EXPIRE_MAKER`（触发时撤挂单）/ `EXPIRE_BOTH`（触发时两边都撤）；默认 `NONE`<br>枚举: `NONE`, `EXPIRE_TAKER`, `EXPIRE_BOTH`, `EXPIRE_MAKER`<br>例: `EXPIRE_TAKER` |
| params.goodTillDate | integer (int64) |  | order cancel time for timeInForce `GTD`, mandatory when `timeInforce` set to `GTD`; order the timestamp only retains second-level precision, ms part will be ignored; The goodTillDate timestamp must be greater than the current time plus 600 seconds and smaller than 253402300799000<br>`timeInForce=GTD` 时的撤单时间（必传）；仅保留秒级精度（毫秒会被忽略）；必须大于当前时间+600秒且小于<br>253402300799000。<br>例: `1770736694138` |
| params.recvWindow | integer (int64) |  | Recv Window.<br>接收窗口。<br>例: `5000` |
| params.timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |
| params.apiKey | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

```json
{
  "id": "e9d6b4349871b40611412680b3445fac",
  "method": "algoOrder.place",
  "params": {
    "algoType": "CONDITIONAL",
    "symbol": "BTCUSDT",
    "side": "BUY",
    "positionSide": "BOTH",
    "type": "STOP_MARKET",
    "timeInForce": "GTC",
    "quantity": "1.0",
    "price": "1.0",
    "triggerPrice": "1.0",
    "workingType": "MARK_PRICE",
    "priceMatch": "OPPONENT",
    "closePosition": "true",
    "priceProtect": "true",
    "reduceOnly": "true",
    "activatePrice": "1.0",
    "callbackRate": 1,
    "clientAlgoId": "1",
    "newOrderRespType": "ACK",
    "selfTradePreventionMode": "EXPIRE_TAKER",
    "goodTillDate": 1770736694138,
    "recvWindow": 5000,
    "timestamp": 1770736694138,
    "apiKey": "API_KEY"
  }
}
```

### 响应 Successful Response：New Algo Order / 下单（算法单）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string |  | 例: `06c9dbd8-ccbf-4ecf-a29c-fe31495ac73f` |
| status | integer (int64) |  | 例: `200` |
| result | object |  |  |
| result.algoId | integer (int64) |  | 例: `3000000000003505` |
| result.clientAlgoId | string |  | 例: `0Xkl1p621E4EryvufmYre1` |
| result.algoType | string |  | 例: `CONDITIONAL` |
| result.orderType | string |  | 例: `TAKE_PROFIT` |
| result.symbol | string |  | 例: `BTCUSDT` |
| result.side | string |  | 例: `SELL` |
| result.positionSide | string |  | 例: `SHORT` |
| result.timeInForce | string |  | 例: `GTC` |
| result.quantity | string |  | 例: `1.000` |
| result.algoStatus | string |  | 例: `NEW` |
| result.triggerPrice | string |  | 例: `120000.00` |
| result.price | string |  | 例: `160000.00` |
| result.icebergQuantity | string |  | Reserved field, ignore.<br>预留字段，请忽略。<br>例: `null` |
| result.selfTradePreventionMode | string |  | 例: `EXPIRE_MAKER` |
| result.workingType | string |  | 例: `CONTRACT_PRICE` |
| result.priceMatch | string |  | 例: `NONE` |
| result.closePosition | boolean |  | 例: `False` |
| result.priceProtect | boolean |  | 例: `False` |
| result.reduceOnly | boolean |  | 例: `False` |
| result.createTime | integer (int64) |  | 例: `1762507264142` |
| result.updateTime | integer (int64) |  | 例: `1762507264143` |
| result.triggerTime | integer (int64) |  | 例: `0` |
| result.goodTillDate | integer (int64) |  | 例: `0` |
| rateLimits | object[] |  |  |
| rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| rateLimits[].interval | string |  | 例: `MINUTE` |
| rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| rateLimits[].limit | integer (int64) |  | 例: `2400` |
| rateLimits[].count | integer (int64) |  | 例: `1` |

## New Order (TRADE)（下单 (TRADE)）

`POST /order.place`

Send in a new order.

下单

Operation ID: `newOrder`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | Id.<br>请求 ID。<br>例: `e9d6b4349871b40611412680b3445fac` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `order.place`<br>例: `order.place` |
| params | object | 是 |  |
| params.symbol | string | 是 | Symbol.<br>交易对。<br>例: `BTCUSDT` |
| params.side | string | 是 | Side.<br>买卖方向。<br>枚举: `BUY`, `SELL`<br>例: `BUY` |
| params.positionSide | string |  | Default `BOTH` for One-way Mode ; `LONG` or `SHORT` for Hedge Mode. It must be sent in Hedge Mode.<br>枚举: `BOTH`, `LONG`, `SHORT`<br>例: `BOTH` |
| params.type | string | 是 | 枚举: `LIMIT`, `MARKET`<br>例: `LIMIT` |
| params.timeInForce | string |  | Time In Force.<br>有效方式。<br>枚举: `GTC`, `IOC`, `FOK`, `GTX`, `GTD`, `RPI`<br>例: `GTC` |
| params.reduceOnly | string |  | Cannot be sent in Hedge Mode<br>双向持仓模式下不可传。<br>枚举: `true`, `false`<br>默认: `false`<br>例: `false` |
| params.quantity | number (float) |  | 例: `1.0` |
| params.price | number (float) |  | Price.<br>价格。<br>例: `1.0` |
| params.newClientOrderId | string |  | A unique id among open orders. Automatically generated if not sent. Can only be string following the rule: `^[\.A-Z\:/a-z0-9_-]{1,36}$`<br>挂单中的唯一客户端订单 ID；未传则自动生成。仅支持匹配 `^[\\.A-Z\\:/a-z0-9_-]{1,36}$` 的字符串。<br>例: `1` |
| params.newOrderRespType | string |  | 枚举: `ACK`, `RESULT`<br>默认: `ACK`<br>例: `ACK` |
| params.priceMatch | string |  | only available for `LIMIT` order; Can't be passed together with `price`<br>仅 `LIMIT` 订单可用；不能与 `price` 同时传。<br>枚举: `OPPONENT`, `OPPONENT_5`, `OPPONENT_10`, `OPPONENT_20`, `QUEUE`, `QUEUE_5`, `QUEUE_10`, `QUEUE_20`<br>例: `OPPONENT` |
| params.selfTradePreventionMode | string |  | `NONE`: No STP / `EXPIRE_TAKER`: expire taker order when STP triggers/ `EXPIRE_MAKER`: expire taker order when STP triggers/ `EXPIRE_BOTH`: expire both orders when STP triggers; default `NONE`<br>自成交保护模式，默认 `NONE`。<br>枚举: `NONE`, `EXPIRE_TAKER`, `EXPIRE_BOTH`, `EXPIRE_MAKER`<br>默认: `NONE`<br>例: `NONE` |
| params.goodTillDate | integer (int64) |  | order cancel time for timeInForce `GTD`, mandatory when `timeInforce` set to `GTD`; order the timestamp only retains second-level precision, ms part will be ignored; The goodTillDate timestamp must be greater than the current time plus 600 seconds and smaller than 253402300799000<br>例: `1770736694138` |
| params.recvWindow | integer (int64) |  | Recv Window.<br>接收窗口。<br>例: `5000` |
| params.timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |
| params.apiKey | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

```json
{
  "id": "e9d6b4349871b40611412680b3445fac",
  "method": "order.place",
  "params": {
    "symbol": "BTCUSDT",
    "side": "BUY",
    "positionSide": "BOTH",
    "type": "LIMIT",
    "timeInForce": "GTC",
    "reduceOnly": "false",
    "quantity": "1.0",
    "price": "1.0",
    "newClientOrderId": "1",
    "newOrderRespType": "ACK",
    "priceMatch": "OPPONENT",
    "selfTradePreventionMode": "NONE",
    "goodTillDate": 1770736694138,
    "recvWindow": 5000,
    "timestamp": 1770736694138,
    "apiKey": "API_KEY"
  }
}
```

### 响应 Successful Response：New Order / 下单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string |  | 例: `3f7df6e3-2df4-44b9-9919-d2f38f90a99a` |
| status | integer (int64) |  | 例: `200` |
| result | object |  |  |
| result.orderId | integer (int64) |  | 例: `325078477` |
| result.symbol | string |  | 例: `BTCUSDT` |
| result.status | string |  | 例: `NEW` |
| result.clientOrderId | string |  | 例: `iCXL1BywlBaf2sesNUrVl3` |
| result.price | string |  | 例: `43187.00` |
| result.origQty | string |  | 例: `0.100` |
| result.executedQty | string |  | 例: `0.000` |
| result.cumQty | string |  | 例: `0.000` |
| result.timeInForce | string |  | 例: `GTC` |
| result.type | string |  | 例: `LIMIT` |
| result.reduceOnly | boolean |  | 例: `False` |
| result.closePosition | boolean |  | 例: `False` |
| result.side | string |  | 例: `BUY` |
| result.positionSide | string |  | 例: `BOTH` |
| result.stopPrice | string |  | 例: `0.00` |
| result.workingType | string |  | 例: `CONTRACT_PRICE` |
| result.priceProtect | boolean |  | 例: `False` |
| result.origType | string |  | 例: `LIMIT` |
| result.priceMatch | string |  | 例: `NONE` |
| result.selfTradePreventionMode | string |  | 例: `EXPIRE_MAKER` |
| result.goodTillDate | integer (int64) |  | 例: `0` |
| result.updateTime | integer (int64) |  | 例: `1702555534435` |
| rateLimits | object[] |  |  |
| rateLimits[].rateLimitType | string |  | 例: `ORDERS` |
| rateLimits[].interval | string |  | 例: `SECOND` |
| rateLimits[].intervalNum | integer (int64) |  | 例: `10` |
| rateLimits[].limit | integer (int64) |  | 例: `300` |
| rateLimits[].count | integer (int64) |  | 例: `1` |

## Position Information (USER_DATA)（用户持仓风险V2 (USER_DATA)）

`POST /account.position`

Get current position information.

查询持仓风险

Operation ID: `positionInformation`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | Id.<br>请求 ID。<br>例: `e9d6b4349871b40611412680b3445fac` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `account.position`<br>例: `account.position` |
| params | object | 是 |  |
| params.symbol | string |  | Symbol.<br>交易对。<br>例: `BTCUSDT` |
| params.recvWindow | integer (int64) |  | Recv Window.<br>接收窗口。<br>例: `5000` |
| params.timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |
| params.apiKey | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

```json
{
  "id": "e9d6b4349871b40611412680b3445fac",
  "method": "account.position",
  "params": {
    "symbol": "BTCUSDT",
    "recvWindow": 5000,
    "timestamp": 1770736694138,
    "apiKey": "API_KEY"
  }
}
```

### 响应 Successful Response：Position Information / 持仓 信息

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string |  | 例: `605a6d20-6588-4cb9-afa0-b0ab087507ba` |
| status | integer (int64) |  | 例: `200` |
| result | object[] |  |  |
| result[].entryPrice | string |  | 例: `0.00000` |
| result[].breakEvenPrice | string |  | 例: `0.0` |
| result[].marginType | string |  | 例: `isolated` |
| result[].isAutoAddMargin | string |  | 例: `false` |
| result[].isolatedMargin | string |  | 例: `0.00000000` |
| result[].leverage | string |  | 例: `10` |
| result[].liquidationPrice | string |  | 例: `0` |
| result[].markPrice | string |  | 例: `6679.50671178` |
| result[].maxNotionalValue | string |  | 例: `20000000` |
| result[].positionAmt | string |  | 例: `0.000` |
| result[].notional | string |  | 例: `0` |
| result[].isolatedWallet | string |  | 例: `0` |
| result[].symbol | string |  | 例: `BTCUSDT` |
| result[].unRealizedProfit | string |  | 例: `0.00000000` |
| result[].positionSide | string |  | 例: `BOTH` |
| result[].updateTime | integer (int64) |  | 例: `1625474304765` |
| rateLimits | object[] |  |  |
| rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| rateLimits[].interval | string |  | 例: `MINUTE` |
| rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| rateLimits[].limit | integer (int64) |  | 例: `2400` |
| rateLimits[].count | integer (int64) |  | 例: `20` |

## Position Information V2 (USER_DATA)（用户持仓风险V2 (USER_DATA)）

`POST /v2/account.position`

Get current position information(only symbol that has position or open
orders will be returned).

查询持仓风险，仅返回有仓位或挂单的交易对

Operation ID: `positionInformationV2`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | Id.<br>请求 ID。<br>例: `e9d6b4349871b40611412680b3445fac` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `v2/account.position`<br>例: `v2/account.position` |
| params | object | 是 |  |
| params.symbol | string |  | Symbol.<br>交易对。<br>例: `BTCUSDT` |
| params.recvWindow | integer (int64) |  | Recv Window.<br>接收窗口。<br>例: `5000` |
| params.timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |
| params.apiKey | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

```json
{
  "id": "e9d6b4349871b40611412680b3445fac",
  "method": "v2/account.position",
  "params": {
    "symbol": "BTCUSDT",
    "recvWindow": 5000,
    "timestamp": 1770736694138,
    "apiKey": "API_KEY"
  }
}
```

### 响应 Successful Response：Position Information V2 / 持仓 信息 V2

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string |  | 例: `605a6d20-6588-4cb9-afa0-b0ab087507ba` |
| status | integer (int64) |  | 例: `200` |
| result | object[] |  |  |
| result[].symbol | string |  | 例: `ADAUSDT` |
| result[].positionSide | string |  | Position Side<br>持仓方向<br>例: `BOTH` |
| result[].positionAmt | string |  | 例: `30` |
| result[].entryPrice | string |  | 例: `0.385` |
| result[].breakEvenPrice | string |  | 例: `0.385077` |
| result[].markPrice | string |  | 例: `0.41047590` |
| result[].unRealizedProfit | string |  | Unrealized Profit<br>未实现盈亏<br>例: `0.76427700` |
| result[].liquidationPrice | string |  | 例: `0` |
| result[].isolatedMargin | string |  | 例: `0` |
| result[].notional | string |  | 例: `12.31427700` |
| result[].marginAsset | string |  | 例: `USDT` |
| result[].isolatedWallet | string |  | 例: `0` |
| result[].initialMargin | string |  | Initial Margin<br>起始保证金<br>例: `0.61571385` |
| result[].maintMargin | string |  | Maintainance Margin<br>维持保证金<br>例: `0.08004280` |
| result[].positionInitialMargin | string |  | Position Initial Margin<br>持仓起始保证金<br>例: `0.61571385` |
| result[].openOrderInitialMargin | string |  | Open Order Initial Margin<br>挂单起始保证金<br>例: `0` |
| result[].adl | integer (int64) |  | 例: `2` |
| result[].bidNotional | string |  | 例: `0` |
| result[].askNotional | string |  | 例: `0` |
| result[].updateTime | integer (int64) |  | Update Time<br>更新时间<br>例: `1720736417660` |
| rateLimits | object[] |  |  |
| rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| rateLimits[].interval | string |  | 例: `MINUTE` |
| rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| rateLimits[].limit | integer (int64) |  | 例: `2400` |
| rateLimits[].count | integer (int64) |  | 例: `20` |

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
| id | string | 是 | Id.<br>请求 ID。<br>例: `e9d6b4349871b40611412680b3445fac` |
| method | string | 是 | WebSocket API method name.<br>WebSocket API 方法名称。<br>枚举: `order.status`<br>例: `order.status` |
| params | object | 是 |  |
| params.symbol | string | 是 | Symbol.<br>交易对。<br>例: `BTCUSDT` |
| params.orderId | integer (int64) |  | Order Id.<br>系统订单号。<br>例: `1` |
| params.origClientOrderId | string |  | Orig Client Order Id.<br>原客户端订单号。<br>例: `1` |
| params.recvWindow | integer (int64) |  | Recv Window.<br>接收窗口。<br>例: `5000` |
| params.timestamp | integer (int64) | 是 | Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and is validated by the server for signed endpoints.<br>用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.<br>例: `1770736694138` |
| params.apiKey | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |

```json
{
  "id": "e9d6b4349871b40611412680b3445fac",
  "method": "order.status",
  "params": {
    "symbol": "BTCUSDT",
    "orderId": 1,
    "origClientOrderId": "1",
    "recvWindow": 5000,
    "timestamp": 1770736694138,
    "apiKey": "API_KEY"
  }
}
```

### 响应 Successful Response：Order Status / 订单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string |  | 例: `605a6d20-6588-4cb9-afa0-b0ab087507ba` |
| status | integer (int64) |  | 例: `200` |
| result | object |  |  |
| result.avgPrice | string |  | 例: `0.00000` |
| result.clientOrderId | string |  | 例: `abc` |
| result.cumQuote | string |  | 例: `0` |
| result.executedQty | string |  | 例: `0` |
| result.orderId | integer (int64) |  | 例: `1573346959` |
| result.origQty | string |  | 例: `0.40` |
| result.origType | string |  | 例: `TRAILING_STOP_MARKET` |
| result.price | string |  | 例: `0` |
| result.reduceOnly | boolean |  | 例: `False` |
| result.side | string |  | 例: `BUY` |
| result.positionSide | string |  | 例: `SHORT` |
| result.status | string |  | 例: `NEW` |
| result.stopPrice | string |  | please ignore when order type is TRAILING_STOP_MARKET<br>当订单类型为 `TRAILING_STOP_MARKET` 时请忽略。<br>例: `9300` |
| result.closePosition | boolean |  | if Close-All<br>是否全平<br>例: `False` |
| result.symbol | string |  | 例: `BTCUSDT` |
| result.time | integer (int64) |  | order time<br>下单时间<br>例: `1579276756075` |
| result.timeInForce | string |  | 例: `GTC` |
| result.type | string |  | 例: `TRAILING_STOP_MARKET` |
| result.activatePrice | string |  | activation price, only return with TRAILING_STOP_MARKET order<br>激活价格，仅 `TRAILING_STOP_MARKET` 返回。<br>例: `9020` |
| result.priceRate | string |  | callback rate, only return with TRAILING_STOP_MARKET order<br>回调比例，仅 `TRAILING_STOP_MARKET` 返回。<br>例: `0.3` |
| result.updateTime | integer (int64) |  | update time<br>更新时间<br>例: `1579276756075` |
| result.workingType | string |  | 例: `CONTRACT_PRICE` |
| result.priceProtect | boolean |  | if conditional order trigger is protected<br>条件单触发是否启用保护。<br>例: `False` |
| result.priceMatch | string |  | 例: `NONE` |
| result.selfTradePreventionMode | string |  | Self-trade prevention mode<br>自我交易预防模式<br>例: `EXPIRE_MAKER` |
| result.goodTillDate | integer (int64) |  | Order good till date timestamp<br>订单有效截止时间戳<br>例: `0` |

## Close User Data Stream (USER_STREAM)（Websocket API关闭listenKey (USER_STREAM)）

`POST /userDataStream.stop`

Close out a user data stream.

关闭某账户数据流

Operation ID: `closeUserDataStream`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | Id.<br>请求 ID。<br>例: `e9d6b4349871b40611412680b3445fac` |
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

### 响应 Successful Response：Close User Data Stream / 关闭用户数据流

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string |  | 例: `819e1b1b-8c06-485b-a13e-131326c69599` |
| status | integer (int64) |  | 例: `200` |
| result | object |  |  |
| rateLimits | object[] |  |  |
| rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| rateLimits[].interval | string |  | 例: `MINUTE` |
| rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| rateLimits[].limit | integer (int64) |  | 例: `2400` |
| rateLimits[].count | integer (int64) |  | 例: `2` |

## Keepalive User Data Stream (USER_STREAM)（Websocket API延长listenKey有效期 (USER_STREAM)）

`POST /userDataStream.ping`

Keepalive a user data stream to prevent a time out. User data streams will close after 60 minutes. It's recommended to send a ping about every 60 minutes.

有效期延长至本次调用后60分钟

Operation ID: `keepaliveUserDataStream`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | Id.<br>请求 ID。<br>例: `e9d6b4349871b40611412680b3445fac` |
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

### 响应 Successful Response：Keepalive User Data Stream / 延长用户数据流有效期

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string |  | 例: `815d5fce-0880-4287-a567-80badf004c74` |
| status | integer (int64) |  | 例: `200` |
| result | object |  |  |
| result.listenKey | string |  | 例: `3HBntNTepshgEdjIwSUIBgB9keLyOCg5qv3n6bYAtktG8ejcaW5HXz9Vx1JgIieg` |
| rateLimits | object[] |  |  |
| rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| rateLimits[].interval | string |  | 例: `MINUTE` |
| rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| rateLimits[].limit | integer (int64) |  | 例: `2400` |
| rateLimits[].count | integer (int64) |  | 例: `2` |

## Start User Data Stream (USER_STREAM)（Websocket API生成listenKey (USER_STREAM)）

`POST /userDataStream.start`

Start a new user data stream. The stream will close after 60 minutes unless a keepalive is sent. If the account has an active `listenKey`, that `listenKey` will be returned and its validity will be extended for 60 minutes.

创建一个新的user data stream，返回值为一个listenKey，即websocket订阅的stream名称。如果该帐户具有有效的`listenKey`，则将返回该`listenKey`并将其有效期延长60分钟。

Operation ID: `startUserDataStream`

### 请求体（application/json）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string | 是 | Id.<br>请求 ID。<br>例: `e9d6b4349871b40611412680b3445fac` |
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

### 响应 Successful Response：Start User Data Stream / 启动用户数据流

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| id | string |  | 例: `d3df8a61-98ea-4fe0-8f4e-0fcea5d418b0` |
| status | integer (int64) |  | 例: `200` |
| result | object |  |  |
| result.listenKey | string |  | 例: `xs0mRXdAKlIPDRFrlPcw0qI41Eh3ixNntmymGyhrhgqo7L6FuLaWArTD7RLP` |
| rateLimits | object[] |  |  |
| rateLimits[].rateLimitType | string |  | 例: `REQUEST_WEIGHT` |
| rateLimits[].interval | string |  | 例: `MINUTE` |
| rateLimits[].intervalNum | integer (int64) |  | 例: `1` |
| rateLimits[].limit | integer (int64) |  | 例: `2400` |
| rateLimits[].count | integer (int64) |  | 例: `2` |