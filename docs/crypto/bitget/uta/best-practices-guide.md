---
exchange: bitget
source_url: https://www.bitget.com/docs/uta/best-practices-guide
api_type: Guide
updated_at: 2026-11-18 19:00:15.458900
---

# Best Practices Guide

## Product Configuration

You can get the exchange's product configuration via `GET /api/v3/market/instruments`.

## Market Data

You can receive real-time market data updates from WebSocket channels.

**Depth channels**:

- `books` default push frequency: `50ms`
- `books5` default push frequency: `10ms`
- `books50` default push frequency: `20ms`
- `books1` default push frequency: `1ms`

- `books` provides full depth data — the first push is a `snapshot`, subsequent pushes are incremental `update`s.
- `books1` provides level-1 depth data — every push is a `snapshot`.
- `books5` provides level-5 depth data — every push is a `snapshot`.
- `books50` provides level-50 depth data — the first push is a `snapshot`, subsequent pushes are incremental `update`s.

No new snapshot is sent when the order book has not changed.

Order book data is updated and pushed on order events. In most cases, users receive the same order book data across all WebSocket connections and channels. When there is no order book change for a long time, the system triggers a compensating push via a scheduled task; in this case, sequence numbers may differ slightly across servers due to clock differences.

The system pushes the latest state of the order book. When the depth changes (including multiple changes within a short period, e.g. A→B→A), the system sends an update reflecting the final state.

## Configuring Accounts and Sub-accounts

After creating an API key, you can configure your account via the API or the website before trading.

### Account Configuration

You can check your current account configuration via the following REST API:

`GET  /api/v3/account/settings`

The API returns the account mode, position mode, asset mode, and many other account-related fields.

### Account Mode

The Unified Trading Account system provides three account modes: Spot Mode (coming soon), Stablecoin Margin Mode, and Multi-Asset Margin Mode.

| Account Mode | Tradable Products | Margin Support | Eligibility |
|:-------|:-------------------------|:--------------------------------------------------|:-----------------------------------|
| Spot Mode | Spot trading only; no leverage or futures trading | No margin used | Users under regulated entities: applied by default |
| Stablecoin Margin Mode | Spot, USDT-margined futures, USDC futures | Under Stablecoin Margin Mode, USDT- and USDC-denominated pairs share the same margin, and PnL can offset across these products | Users registered under global entities: applied by default. Requires completing a questionnaire to activate |
| Multi-Asset Margin Mode | Spot, margin, USDT-margined futures, USDC futures, coin-margined | All asset types support cross-margining | Account equity ≥ 1,000 USD: complete a questionnaire to activate |

Under **Multi-Asset Margin Mode**, assets across all product types can be used as shared margin, and PnL can offset each other.

The account mode can be changed via the API or on the website.

### Position Mode

The exchange currently supports two position modes.

| Position Mode | Description |
|:---------|:------|
| One-way Position Mode | Only long or short positions can be held. The exchange automatically opens/closes positions based on the specified position size |
| Hedge Position Mode | Long and short positions can be held simultaneously |

You can set the position mode via the following REST API (all positions must be closed and there must be no open orders beforehand):

`POST /api/v3/account/set-hold-mode`


### Cross/Isolated Margin Mode

The Unified Trading Account system supports both cross margin mode and isolated margin mode.

### Getting Leverage

You can get the leverage via the following REST API:

`GET /api/v3/account/settings`

Currently there is no global leverage setting — leverage must be set separately for each trading pair.

**Product Types**:

| Position Mode | Product Type   | Margin Mode | Level  |
|:---------|:--------|:-----------|:-----|
| One-way | USDT-margined futures  | Cross | Trading pair |
| One-way | USDC futures | Cross | Trading pair |
| One-way | Coin-margined perpetual  | Cross | Trading pair |
| Hedge | USDT-margined futures  | Cross | Trading pair |
| Hedge | USDT perpetual | Cross | Trading pair    |
| Hedge | USDC futures | Cross | Trading pair |

### Setting Leverage

After getting the leverage, you can set it as needed:

`POST /api/v3/account/set-leverage`

You can use the two APIs above to pre-set the leverage for each trading pair before trading.

#### Example

Assume the following setup and requirements:

- Account Mode: Multi-Asset Margin Mode
- Position Mode: One-way Position Mode
- Product to set leverage to 3 for:
  - BTCUSDT
- The above product uses cross margin mode

For spot margin, leverage is set at the coin level, so you can set it separately for BTC and USDT.

Example request body to set BTC leverage to 3 (applies to selling BTCUSDT):

```json
{
  "leverage": "3.0",
  "coin": "BTC",
  "productType": "MARGIN"
}
```

The request body for USDT is similar.

Next, set the leverage for the BTCUSDT perpetual futures contract.

Since this is a USDT-margined futures contract, it needs to be set separately:

```json
{
  "leverage": "3",
  "symbol": "BTCUSDT",
  "productType": "usdt-futures"
}
```

After sending the above REST API request, the leverage setting for these products is complete.

## Order Management

### Subscribing to the Order Channel

Before placing an order, you should first subscribe to the order channel via WebSocket so you can monitor order status (e.g. pending, fully filled) and take corresponding actions (e.g. placing a new order after a fill).

The order channel supports subscriptions at various dimensions. To subscribe to BTCUSDT order data, after connecting and logging in to the private WebSocket, send either of the requests below:

| Subscription Dimension | Product Type |
|:---------|:---------|
| **Request** | `{"op": "subscribe", "args": [{"instType": "UTA", "topic": "order"}]}` |
| **Success Response** | `{"event": "subscribe", "arg": {"topic": "order", "instType": "UTA"}}`  |

**Note**: The order channel does not push full data on first subscription — it only pushes updates for an order when its status changes (e.g. from pending to successfully canceled).

In other words, you cannot get current order data at the moment you subscribe to the order channel. To get data for orders that were unfilled before you subscribed, use the following REST API:

`GET /api/v3/trade/unfilled-orders`

### Placing Orders

To make it easier for the system to identify orders, we recommend that you fill in a custom order ID (the `clientOid` field) when placing an order. The custom order ID must match `^[0-9A-Za-z_:#\\-+\\s]{1,32}$`.

The `clientOid` uniqueness check applies only to all open orders, but we still recommend always using a unique `clientOid` to make troubleshooting easier.

In this example, we'll set the `clientOid` field to `testBTC0123`.

After subscribing to the order channel, you can prepare to place a BTCUSDT order.

You can place orders via REST or WebSocket.

#### REST API

You can place an order via the following REST API; the server returns an order ID (`orderId`) after receiving the request.

<div className="table-wrap-text">

| REST API  | `POST /api/v3/trade/place-order` |
|:----------|:----------------------------------|
| **Request Body**   | `{"category":"SPOT","symbol":"BGBUSDT","orderType":"limit","qty":"123","price":"1.11","side":"buy","posSide":"long","timeInForce":"gtc","reduceOnly":"no"}` |
| **Success Response**  | `{"code": "00000", "msg": "success", "requestTime": 1695806875837, "data": {"clientOid": "testBTC0123", "orderId": "1234567890"}}` |

</div>

**Note**: This only means the exchange has successfully received the request and assigned an order ID to the order. The order may not have reached the matching engine yet, so you need to further check the order status to confirm.

#### WebSocket

You can also place orders via WebSocket, which is theoretically more efficient and resource-saving than REST.

Since WebSocket operations are asynchronous, you need to provide a message ID (`id`) to identify the response.

After logging in to the private WebSocket, send the following WebSocket message:

```json
{
  "op": "trade",
  "id": "testBTC0123",
  "category": "spot",
  "topic": "place-order",
  "args": [
    {
      "orderType": "limit",
      "price": "100",
      "qty": "0.1",
      "side": "buy",
      "symbol": "BTCUSDT",
      "timeInForce": "gtc",
      "clientOid": "testBTC0123"
    }
  ]
}
```

After receiving the request, the server returns the result along with the message ID (i.e. `testBTC0123`), together with the order ID assigned by the exchange (`orderId`):

```json
{
  "event": "trade",
  "id": "testBTC0123",
  "category": "spot",
  "topic": "place-order",
  "args": [
    {
      "symbol": "BTCUSDT",
      "orderId": "1234567890",
      "clientOid": "testBTC0123",
      "cTime": "1750034397008"
    }
  ],
  "code": "0",
  "msg": "success",
  "ts": "1750034397076"
}
```

**Note**: This only means the exchange has successfully received the request and assigned an order ID to the order. The order may not have reached the matching engine yet, so you need to further check the order status to confirm.

### Checking Order Status

After placing an order, if it does not return an error (`"code": "0"`) and enters the matching engine, you will receive a push on the WebSocket order channel with the order status `new`.

After the order is fully filled, you will receive a push with the order status changed to `filled`, along with other fill-related fields.

If the order is partially or fully filled, WebSocket will return `state = partially_filled` and `filled` respectively.

For Immediate-or-Cancel (IOC), Fill-or-Kill (FOK), and post-only orders, these orders may be rejected by the matching engine, and you will receive a `canceled` status.

Your order may be canceled by the system for various reasons, such as liquidation or self-trade. You can refer to `cancelSource` to determine the reason the order was canceled.

An order's terminal status is either `canceled` or `filled`.

Each fill of an order is assigned a trade ID (`tradeId`) by the system.

**Possible Order Statuses**:

| Scenario | Status Change                                          |
|:------|:-----------------------------------------------|
| Rejected at entry | `code` is non-zero, no update pushed on the WebSocket order channel |
| Order placed and immediately fully filled | `new` → `filled`                              |
| Order placed and immediately filled via multiple trades | `new` → `partially_filled` → ... → `filled`  |
| Order placed and immediately canceled by the matching engine (e.g. IOC, FOK, post-only) | `canceled` (cancellation reason can be queried via `cancelSource`) |
| IOC order, partially filled then canceled by the system due to insufficient price depth | `partially_filled` → `canceled`      |

### Modifying Orders

The order modification API supports modification for all product types, allowing you to modify an order's price (`price` field) and/or quantity (`qty` field). The API also provides an `autoCancel` parameter to set whether the order is automatically canceled if the modification fails.

**REST**:

`POST /api/v3/trade/modify-order`

**WebSocket business action request parameters**:

```json
{
    "args": [
        {
            "autoCancel": "yes",
            "clientOid": "135423791666666666",
            "orderId": "1354237910666666666",
            "price": "5",
            "qty": "2",
            "symbol":"BTCUSDT"
        }
    ],
    "id": "ae5ea6df-215f-4750-a700-d487d03ac020",
    "op": "trade",
    "category": "usdt-futures",
    "topic": "modify-order"
}
```

Similar to placing an order, you should receive a success response from the corresponding REST/WebSocket call, and then receive an order update push on the WebSocket order channel.

**Note**: An order cannot be modified once it is fully filled or successfully canceled.

A success response only means the exchange has received the request — refer to the WebSocket order channel to confirm.

### Canceling Orders

You can cancel orders via REST or WebSocket in a similar way.

**REST**:

`POST /api/v3/trade/cancel-order`

**WebSocket business action request parameters**:

```json
{
    "args": [
        {
            "orderId": "xxxxxxxxxxxxxxxxxx",
            "clientOid": "xxxxxxxxxxxxxxxxxx"
        }
    ],
    "id": "c8a1999c-1f82-409d-870e-f40ff49c4072",
    "op": "trade",
    "topic": "cancel-order"
}
```

Similarly, you should receive a success response from the corresponding REST/WebSocket call. The order is only considered successfully canceled once you receive a push with status `canceled` on the WebSocket order channel.

**Note**: An order cannot be canceled once it is fully filled or successfully canceled.

A success response only means the exchange has received the request — refer to the WebSocket order channel to confirm.

### Batch Operations

Placing, modifying, and canceling orders all support batch operations, up to 20 orders per batch.

**REST**:

| Operation | API |
|:------|:-----|
| Place | `POST /api/v3/trade/place-batch` |
| Modify | `POST /api/v3/trade/batch-modify-order` |
| Cancel | `POST /api/v3/trade/cancel-batch` |

**WebSocket business action parameters**:

| Operation | Parameter |
|:------|:------|
| Place | `"topic": "batch-place"` |
| Modify | `"topic": "batch-modify"` |
| Cancel | `"topic": "batch-cancel"` |

Batch operations allow partial success. After receiving the response, check the `code` and `msg` fields for each order in the result to determine the outcome.

### Order Timestamps

Order data includes several timestamps for tracking order status and latency.

| Field            | Description                                 |
|:---------------|:------------------------------------|
| `createdTime` | The time the order management system created the order after risk checks |
| `updatedTime` | The last time the order management system updated the order. Updated after order modification, fills, and cancellation |
| `ts`          | The time the WebSocket gateway pushed the message                    |

## Pagination

Bitget provides pagination to help you easily retrieve the data you want from large datasets. The related request parameters are as follows:

| Parameter | Type | Required | Description |
|:--------|:------|:---------|:------|
| `cursor` | String | No | Used for pagination. Omit on the first query. For the second and later pages, use the smallest ID returned by the previous query; the result will return data smaller than that value |
| `startTime` | String | No | Start time, Unix timestamp (milliseconds) |
| `endTime` | String | No | End time, Unix timestamp (milliseconds) |
| `limit` | String | No | Number of results to return, maximum 100, default 100 |


The trading APIs that support pagination are listed below:

- `GET /api/v3/trade/unfilled-orders` - Get current orders
- `GET /api/v3/trade/history-orders` - Get order history
- `GET /api/v3/trade/fills` - Get fill details
- `GET /api/v3/account/financial-records` - Get financial records

## Self-Trade Prevention

The trading system enforces mandatory self-trade prevention (STP) at the master account level — no account under the same master account, including the master account itself and all sub-accounts, can self-trade. The default STP mode for an order is `none`; you can also specify an order's STP mode via the `stpMode` parameter of the order-placement API.

Bitget supports 4 STP modes (`stpMode`): `none`, `cancel_maker`, `cancel_taker`, and `cancel_both`.

**Note**: Mandatory self-trade prevention applies to all users, all order types, and all order-book trading products.

### Self-Trade Prevention Modes

Bitget provides users with four modes that define how self-trading is prevented. The STP outcome depends on the taker order's STP mode; the STP mode of existing orders in the order book (maker side) is not considered.

#### none mode

The order is not restricted by the STP mechanism — the system does not compare UIDs, and the trade executes normally.

#### cancel_taker mode

Cancels the taker order and keeps the maker order.

#### cancel_maker mode

Cancels the maker order and keeps the taker order.

#### cancel_both mode

Cancels both the taker and maker orders.

## Unified Account and Positions

### Account

#### WebSocket Subscription

We recommend subscribing to the account channel via WebSocket to receive account updates.

This endpoint returns the value of your assets denominated in USD, along with other parameters that are continuously updated due to price changes. Bitget sends update data to you when valuations change.

Example request and response after connecting to and logging in to the private WebSocket:

| Subscription Dimension       | Account                                                                          |
|:------------|:-----------------------------------------------------------------------------|
| **Request**     | `{"op": "subscribe","args": [ { "instType": "UTA","topic": "account" } ] }` |
| **Success Response**   | `{"event": "subscribe","arg": {"instType": "UTA","topic": "account"} }`     |

#### Initial Full Push on Subscription

Unlike the order channel, the account channel pushes full data on the first subscription.

#### Subsequent Pushes

Afterwards, you will receive account data pushes under the following circumstances:

| Push Type     | Description                                             |
|:----------|:------------------------------------------------|
| Event-triggered push   | Unified account spot/margin/futures order fills, funding settlement, balance changes (transfers, airdrops, lending, etc.) |

#### REST API

You can also check your account balance via the REST API:

`GET /api/v3/account/assets`
`GET /api/v3/account/funding-assets`

### Maximum Available Quantity

Under Multi-Asset Margin Mode, enabling auto-borrow lets you buy/sell a product in a quantity greater than your coin balance.

In this case, you may want to know the maximum buy/sell quantity for a product. You can poll the following REST API to get the maximum available quantity (including available balance and the exchange's maximum borrowable amount):

`POST /api/v3/account/max-open-available`

Example request and response:

| Request | `{"category":"SPOT","symbol":"BTCUSDT","orderType":"market","side":"sell"}` |
|:------------|:--------------------------------------------------------------------------------------------------------------------------------------------------|
| **Success Response**   | `{"code": "00000", "requestTime": 1741851607871, "data": {"available": "52.008255", "maxOpen": "", "buyOpenCost": "", "sellOpenCost": "", "maxBuyOpen": "", "maxSellOpen": ""}, "msg": "success"}` |

For spot/margin, `available` represents the quote currency quantity when side=buy, and the base currency quantity when side=sell.


### Maximum Transferable Amount

To get the maximum transferable amount for the unified account or a sub-account, use `GET /api/v3/account/max-transferable`.

This endpoint also supports getting the maximum transferable amount including borrowing.


### Positions

You should use WebSocket to get position information updates.

#### WebSocket Subscription

Similar to the order channel, the position channel supports subscriptions at various dimensions.

This endpoint returns the mark price and other continuously changing parameters. Bitget periodically pushes data updates to you.

To subscribe to BTCUSDT position data, after connecting and logging in to the private WebSocket, send either of the requests below:

| Subscription Dimension | Product Type |
|:---------|:---------|
| **Request** | `{"op": "subscribe","args": [{"instType": "UTA","topic": "position"}]}` |
| **Success Response** | `{"event": "subscribe","arg": {"instType": "UTA","topic": "position"} }` |


#### Initial Full Push on Subscription

Like the account channel, the position channel pushes full data on the first subscription, sending information for all positions that are not zero.

#### Subsequent Pushes

Afterwards, you will receive position data pushes under the following circumstances:

| Push Type | Description                                                     |
|:---------|:--------------------------------------------------------|
| Event-triggered push | Unified account futures close-order placement, unified account futures open-order fill, unified account futures close-order fill, unified account futures close-order modification, unified account futures close-order cancellation |

#### REST API

You can also check position information via the REST API:

`GET /api/v3/position/current-position`

---

# 最佳实践指南

## 产品配置

用户可以通过 `GET /api/v3/market/instruments` 获取交易所的产品配置。

## 市场数据

用户能够从 WebSocket 频道接收实时的市场数据更新。

**深度数据频道**：

- `books`默认推送频率：`50ms`
- `books5`默认推送频率：`10ms`
- `books50`默认推送频率：`20ms`
- `books1`默认推送频率：`1ms`

- `books` 对应全量深度数据，首次推送全量数据：`snapshot`，后续推送增量变化数据：`update`。
- `books1` 对应1档位深度数据，每次推送：`snapshot`。
- `books5` 对应5档位深度数据，每次推送：`snapshot`。
- `books50` 对应50档位深度数据，首次推送全量数据：`snapshot`，后续推送增量变化数据：`update`。

当订单簿没有变化时，系统不会发送新的快照。

订单簿数据由订单事件触发更新并推送。用户在大多数情况下从所有 WebSocket 连接和频道接收到的订单簿数据是相同的。在长时间未有订单簿变化时，系统会通过定时任务触发补偿推送，此时不同服务器可能因时钟差异导致推送序列号略有不同。

系统会推送订单簿的最新状态。当深度发生变化时（包括短时间内的多次变化，如 A→B→A），系统会发送最终状态的更新。

## 配置账户和子账户

创建 API 密钥后，用户可以在交易之前通过 API 或网页端配置账户。

### 账户配置

用户可以通过以下的 REST API 查看当前账户的配置：

`GET  /api/v3/account/settings`

API 会返回账户模式、持仓模式、资产模式以及许多其他与账户相关的信息。

### 账户模式

统一交易账户系统提供三个账户模式，分别为现货模式（即将推出）、稳定币保证金模式以及多币种保证金模式。

| 账户模式  | 可交易产品                   | 保证金支持                                            | 资格要求                              |
|:-------|:-------------------------|:--------------------------------------------------|:-----------------------------------|
| 现货模式  | 仅支持现货交易，不支持杠杆交易和合约交易    | 不使用保证金                                           | 受监管实体下的用户：默认适用该账户模式               |
| 稳定币保证金模式  | 现货、U本位合约、USDC合约         | 稳定币保证金模式下，以 USDT 和 USDC 计价的币对共用同一保证金，这些产品之间的盈亏可以相互抵扣 | 全球实体下注册的用户：默认适用该账户模式。需完成问卷以激活该模式 |
| 多币种保证金模式  | 现货、杠杆、U本位合约、USDC合约、币本位  | 所有资产支持相互保证金                                      | 账户权益 ≥ 1,000 USD：完成问卷调查以激活此模式     |

**多币种保证金模式**下，所有产品类型的资产都可以用作共享保证金，盈亏可以相互抵消。

更改账户模式可使用api或在网页上进行。

### 持仓模式

交易所目前支持两种持仓模式。

| 持仓模式 | 说明 |
|:---------|:------|
| 单向持仓模式 | 只可持有开多或开空仓位。交易所会根据您所指定的持仓数量自动开/平仓 |
| 双向持仓模式 | 可同时持有开多仓位和开空仓位 |

用户可以通过以下的 REST API 设置持仓模式（设置前需平掉所有仓位和没有挂单）：

`POST /api/v3/account/set-hold-mode`


### 全仓/逐仓保证金模式

统一交易账户系统同时支持全仓保证金模式和逐仓保证金模式

### 获取杠杆倍数

用户可以通过以下的 REST API 获取杠杆倍数：

`GET /api/v3/account/settings`

目前杠杆倍数没有全局设置，需按照产品交易对分开设置。

**产品类型**：

| 持仓模式 | 产品类型   | 保证金模式 | 层面  |
|:---------|:--------|:-----------|:-----|
| 单向持仓 | U本位合约  | 全仓 | 交易币对 |
| 单向持仓 | USDC合约 | 全仓 | 交易币对 |
| 单向持仓 | 币本位永续  | 全仓 | 交易币对 |
| 双向持仓 | U本位合约  | 全仓 | 交易币对 |
| 双向持仓 | USDT永续 | 全仓 | 交易币对    |
| 双向持仓 | USDC合约 | 全仓 | 交易币对 |

### 设置杠杆倍数

在获取杠杆倍数之后，用户可根据需要进行设置：

`POST /api/v3/account/set-leverage`

用户可以运用上述两个 API 接口，在交易前预先设置每个交易对的杠杆倍数。

#### 示例

假设我们有以下的设置和需求：

- 账户模式：多币种保证金模式
- 持仓模式：单向持仓模式
- 需要设置杠杆倍数为 3 的产品：
  - BTCUSDT
- 以上产品使用全仓保证金模式

现货杠杆的设置层面为币种，用户可以截取币种去逐一设置，即 BTC、USDT。

设置 BTC 币种杠杆倍数为 3 的请求体示例（适用于卖出 BTCUSDT）：

```json
{
  "leverage": "3.0",
  "coin": "BTC",
  "productType": "MARGIN"
}
```

设置 USDT的请求体也类似。

下一步就是设置 BTCUSDT 永续合约的杠杆倍数。

因为是U本位合约，用户需要分别设置：

```json
{
  "leverage": "3",
  "symbol": "BTCUSDT",
  "productType": "usdt-futures"
}
```

在发送了上面的 API REST 请求后，这些产品杠杆倍数的设置便完成了。

## 订单管理

### 订阅订单频道

下单前，用户应先使用 WebSocket 订阅订单频道，这样才能够监察订单状态（如等待成交、完全成交）和作出相应的操作（如在完全成交后下新单）。

订单频道提供多种维度的订阅。要订阅以上 BTCUSDT 订单的数据，用户可在连接到和登入私有 WebSocket 后，传送下表任一请求：

| 订阅维度 | 产品类型 |
|:---------|:---------|
| **请求** | `{"op": "subscribe", "args": [{"instType": "UTA", "topic": "order"}]}` |
| **成功返回** | `{"event": "subscribe", "arg": {"topic": "order", "instType": "UTA"}}`  |

**注**：订单频道不设首次订阅全量数据推送，只会在订单状态改变时（如由等待成交到撤单成功）推送该订单的更新。

换言之，用户无法在订阅订单频道时得知当时的订单数据。要获取订阅订单频道前未完成订单的数据，可通过以下的 REST API 查看：

`GET /api/v3/trade/unfilled-orders`

### 下单

为了系统能够更容易地识别订单，我们建议用户在下单时填上客户自定义订单 ID（`clientOid` 字段）。客户自定义订单 ID 需满足`^[0-9A-Za-z_:#\\-+\\s]{1,32}$`。

`clientOid` 唯一性检查仅适用于所有挂单，但我们仍推荐用户始终使用唯一的 `clientOid` 以便于故障排除等工作。

此示例我们会在 `clientOid` 字段填上 `testBTC0123`。

在订阅订单频道后，用户便可以准备 BTCUSDT 订单的下单。

用户可通过 REST 和 WebSocket 去下单。

#### REST API

用户可以通过以下的 REST API 下单，服务器收到请求后会返回订单 ID（`orderId`）。

<div className="table-wrap-text">

| REST API  | `POST /api/v3/trade/place-order` |
|:----------|:----------------------------------|
| **请求体**   | `{"category":"SPOT","symbol":"BGBUSDT","orderType":"limit","qty":"123","price":"1.11","side":"buy","posSide":"long","timeInForce":"gtc","reduceOnly":"no"}` |
| **成功返回**  | `{"code": "00000", "msg": "success", "requestTime": 1695806875837, "data": {"clientOid": "testBTC0123", "orderId": "1234567890"}}` |

</div>

**注**：这只代表交易所已成功收取请求，并把订单 ID 指派到该订单。此时订单有可能还没到撮合系统，用户需要进一步检查订单状态去确认。

#### WebSocket

用户亦可以通过 WebSocket 下单，理论上比 REST 更有效率及节约资源。

由于 WebSocket 操作为异步通信，用户需要提供信息 ID（`id`）以便识别其返回。

于私有 WebSocket 登录后，传送以下 WebSocket 信息：

```json
{
  "op": "trade",
  "id": "testBTC0123",
  "category": "spot",
  "topic": "place-order",
  "args": [
    {
      "orderType": "limit",
      "price": "100",
      "qty": "0.1",
      "side": "buy",
      "symbol": "BTCUSDT",
      "timeInForce": "gtc",
      "clientOid": "testBTC0123"
    }
  ]
}
```

服务器收到请求后，会连同信息 ID（即 `testBTC0123`）返回结果，并附上交易所指派的订单 ID（`orderId`）：

```json
{
  "event": "trade",
  "id": "testBTC0123",
  "category": "spot",
  "topic": "place-order",
  "args": [
    {
      "symbol": "BTCUSDT",
      "orderId": "1234567890",
      "clientOid": "testBTC0123",
      "cTime": "1750034397008"
    }
  ],
  "code": "0",
  "msg": "success",
  "ts": "1750034397076"
}
```

**注**：这只代表交易所已成功收取请求，并把订单 ID 指派到该订单。此时订单有可能还没到撮合系统，用户需要进一步检查订单状态去确认。

### 检查订单状态

下单后，若订单未返回任何错误（`"code": "0"`），订单进入撮合后，用户会在 WebSocket 订单频道收到该订单状态为 `new` 的信息。

订单完全成交后，用户会收到订单状态变更为 `filled` 的推送信息，并填上其他有关成交的字段。

如果订单部分或全部成交，WebSocket 将分别返回 `state = partially_filled` 和 `filled`。

对于立即成交并取消剩余（IOC）、全部成交或立即取消（FOK）以及仅挂单的订单（post only），这些订单可能会被撮合引擎拒绝，用户将收到 `canceled` 的状态。

用户订单可能会由于各种原因被系统取消，例如清算或自成交。用户可以参考 `cancelSource` 以确定订单被取消的原因。

一个订单的终止状态为 `canceled` 或 `filled`。

订单的每一笔成交都会被系统赋予一个成交 ID（`tradeId`）。

**可能的订单状态**：

| 场景 | 状态变化                                          |
|:------|:-----------------------------------------------|
| 在入口处被拒绝 | `code` 不为零，WebSocket 订单频道无更新推送                |
| 下单并立即全部成交 | `new` → `filled`                              |
| 下单并立即通过多笔交易成交 | `new` → `partially_filled` → ... → `filled`  |
| 下单但立即被撮合引擎取消（如 IOC、FOK、仅挂单） | `canceled`（取消原因可从 `cancelSource` 查询） |
| 下单为 IOC，部分成交后因价格深度不足而被系统取消 | `partially_filled` → `canceled`      |

### 改单

改单接口支持所有产品类型的改单，允许用户修改订单的价格（`price` 字段）和/或数量（`qty` 字段）。另外 API 也提供 `autoCancel` 参数，设置订单修改失败时自动撤单的操作。

**REST**：

`POST /api/v3/trade/modify-order`

**WebSocket 业务操作请求参数**：

```json
{
    "args": [
        {
            "autoCancel": "yes",
            "clientOid": "135423791666666666",
            "orderId": "1354237910666666666",
            "price": "5",
            "qty": "2",
            "symbol":"BTCUSDT"
        }
    ],
    "id": "ae5ea6df-215f-4750-a700-d487d03ac020",
    "op": "trade",
    "category": "usdt-futures",
    "topic": "modify-order"
}
```

与下单相似，用户应会收到服务器相应 REST / WebSocket 的成功返回，然后于 WebSocket 订单频道收到订单信息推送更新。

**注**：订单完全成交或撤单已成功时不能改单。

成功响应仅表示交易所已收到该请求，用户应参考 WebSocket 订单频道以进行确认。

### 撤单

用户可以以类似的方式，通过 REST 或 WebSocket 撤单。

**REST**：

`POST /api/v3/trade/cancel-order`

**WebSocket 业务操作请求参数**：

```json
{
    "args": [
        {
            "orderId": "xxxxxxxxxxxxxxxxxx",
            "clientOid": "xxxxxxxxxxxxxxxxxx"
        }
    ],
    "id": "c8a1999c-1f82-409d-870e-f40ff49c4072",
    "op": "trade",
    "topic": "cancel-order"
}
```

同样，用户应会收到服务器相应 REST / WebSocket 的成功返回。当用户从 WebSocket 订单频道收到订单状态为 `canceled` 的推送更新时，才代表订单撤单成功。

**注**：订单完全成交或撤单已成功时不能撤单。

成功响应仅表示交易所已收到该请求，用户应参考 WebSocket 订单频道以进行确认。

### 批量操作

下单、改单、撤单均支持批量操作，每次最多 20 个订单。

**REST**：

| 操作 | API |
|:------|:-----|
| 下单 | `POST /api/v3/trade/place-batch` |
| 改单 | `POST /api/v3/trade/batch-modify-order` |
| 撤单 | `POST /api/v3/trade/cancel-batch` |

**WebSocket 业务操作请求参数**：

| 操作 | 参数 |
|:------|:------|
| 下单 | `"topic": "batch-place"` |
| 改单 | `"topic": "batch-modify"` |
| 撤单 | `"topic": "batch-cancel"` |

批量操作容许部分订单操作成功。在收到返回后，用户应检查返回结果内每个订单的 `code` 和 `msg` 字段来判断订单的执行结果。

### 订单时间戳

订单数据中有多个时间戳，供用户跟踪订单状态和延迟。

| 字段            | 说明                                 |
|:---------------|:------------------------------------|
| `createdTime` | 订单管理系统在风险检查后的订单创建时间                |
| `updatedTime` | 订单管理系统最后一次更新订单的时间。在订单修改、成交和取消后进行更新 |
| `ts`          | websocket网关推送时间                    |

## 分页

Bitget 提供分页功能，以帮助用户从海量数据中轻松获得他们想要的数据。相关的请求参数如下：

| 参数名 | 类型 | 是否必须 | 描述 |
|:--------|:------|:---------|:------|
| `cursor` | String | 否 | 用于翻页，首次查询不传，查询第二页及后面的数据时，取上一次查询返回的最小Id，结果会返回小于该值的数据 |
| `startTime` | String | 否 | 开始时间，Unix 时间戳（毫秒） |
| `endTime` | String | 否 | 结束时间，Unix 时间戳（毫秒） |
| `limit` | String | 否 | 返回结果的数量，最大为 100，默认 100 条 |


拥有分页功能的交易接口罗列如下：

- `GET /api/v3/trade/unfilled-orders` - 获取当前委托
- `GET /api/v3/trade/history-orders` - 获取历史委托
- `GET /api/v3/trade/fills` - 获取成交明细
- `GET /api/v3/account/financial-records` - 获取财务记录

## 自成交保护

交易系统会以母账户维度实施强制自成交保护，同一母账户下所有账户，包括母账户本身和所有子账户，都无法进行自成交。订单的默认 STP 模式为 `none`，用户亦可以通过下单接口的 `stpMode` 参数指定订单的 STP 模式。

Bitget 将支持 4 种 STP 模式（`stpMode`），分别是 `none`、`cancel_maker`、`cancel_taker` 和 `cancel_both`。

**注**：强制自成交保护功能仅适用于所有用户，所有订单类型，以及所有订单簿交易产品。

### 自成交保护模式

Bitget 为用户提供了四种模式，定义了如何阻止自成交，STP 的执行结果取决于 Taker 订单的 STP 模式，挂单表中现有订单的 STP 模式不予考虑。

#### none模式

订单不受 STP 机制限制，系统不对比 UID，交易正常执行。

#### cancel_taker 模式

取消 Taker 订单，保留 Maker 订单。

#### cancel_maker 模式

取消 Maker 订单，保留 Taker 订单。

#### cancel_both 模式

同时取消 Taker 和 Maker 订单。

## 统一账户和持仓

### 账户

#### WebSocket 订阅

我们建议使用 WebSocket 订阅账户频道收取账户更新。

该端点返回用户以美元为单元的资产价值，以及其他由于价格变化而持续更新的参数。Bitget 在估值变化时向用户发送更新数据。

连接到私有 WebSocket 和登入后的请求和返回示例：


| 订阅维度       | 账户                                                                          |
|:------------|:-----------------------------------------------------------------------------|
| **请求**     | `{"op": "subscribe","args": [ { "instType": "UTA","topic": "account" } ] }` |
| **成功返回**   | `{"event": "subscribe","arg": {"instType": "UTA","topic": "account"} }`     |

#### 首次订阅全量数据

与订单频道不同，账户频道首次订阅会推送全量数据。

#### 后续推送

之后，用户会根据以下情况收到账户数据推送：

| 推送类型     | 说明                                             |
|:----------|:------------------------------------------------|
| 事件触发推送   | 统一账户现货/杠杆/合约委托单成交, 资金结算时，改变balance时（划转、空投、借贷等） |

#### REST API

用户亦可以通过 REST API 查看账户余额：

`GET /api/v3/account/assets`
`GET /api/v3/account/funding-assets`

### 最大可用数量

多币种保证金模式下，启用自动借币能让用户以多于币种余额的数量买入/卖出产品。

在这种情况下，用户便会想知道该产品最大的买入/卖出数量为多少。用户可以轮询以下的 REST API 得知最大可用数量（包括可用余额和交易所的最大可借）：

`POST /api/v3/account/max-open-available`

请求和返回示例：

| 请求 | `{"category":"SPOT","symbol":"BTCUSDT","orderType":"market","side":"sell"}` |
|:------------|:--------------------------------------------------------------------------------------------------------------------------------------------------|
| **成功返回**   | ` {"code": "00000", "requestTime": 1741851607871, "data": {"available": "52.008255", "maxOpen": "", "buyOpenCost": "", "sellOpenCost": "", "maxBuyOpen": "", "maxSellOpen": ""}, "msg": "success"}` |

现货/杠杆的 `available`，当 side=buy 时代表计价币数量，side=sell时代表基础币数量。


### 最大可转出

为了获得统一账户或是某个子账户的最大可转出金额，用户可以通过 `GET /api/v3/account/max-transferable` 获取最大可转出。

此端点支持获取借币最大可转出。


### 持仓

用户应该使用 WebSocket 获取持仓信息更新。

#### WebSocket 订阅

与订单频道类似，持仓频道提供多种维度的订阅。

该端点返回标识价格以及其他持续变化的参数。Bitget 会定期向用户推送数据更新。

要订阅 BTCUSDT 持仓的数据，用户可在连接到和登入私有 WebSocket 后，传送下表任一请求：

| 订阅维度 | 产品类型 |
|:---------|:---------|
| **请求** | `{"op": "subscribe","args": [{"instType": "UTA","topic": "position"}]}` |
| **成功返回** | `{"event": "subscribe","arg": {"instType": "UTA","topic": "position"} }` |


#### 首次订阅全量数据

与账户频道一样，持仓频道首次订阅会推送全量数据，推送所有持仓不为 0 的持仓信息。

#### 后续推送

之后，用户会根据以下情况收到持仓数据推送：

| 推送类型 | 说明                                                     |
|:---------|:--------------------------------------------------------|
| 事件触发推送 | 统一账户合约平仓委托单下单，统一账户合约开仓委托成交，统一账户合约平仓委托成交，统一账户合约平仓委托单改单，统一账户合约平仓委托单撤单 |

#### REST API

用户亦可以通过 REST API 查看持仓信息：

`GET /api/v3/position/current-position`