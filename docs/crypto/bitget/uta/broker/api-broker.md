---
exchange: bitget
source_url: https://www.bitget.com/docs/uta/broker/api-broker
api_type: Guide
updated_at: 2026-11-26 19:02:55.621610
---

# API Broker

## Broker Program Introduction

The Bitget Broker Program aims to establish a comprehensive commission-sharing framework that enables referrers to invite and earn commissions from diverse user segments, covering both new user acquisitions and the expansion of existing users' trading activity on the platform.

Ideal partners include trading bot providers, social trading platforms, open-source trading libraries, trade execution platforms, exchange aggregators, asset management platforms, and quantitative trading platforms and their affiliates.

Through the Broker Program, third-party partners can leverage Bitget's existing exchange infrastructure without needing to build their own or manage matching, clearing, risk control, fund security, or compliance. This allows partners to focus on their core strengths in user acquisition, community operations, and product development while benefiting from Bitget's established trading ecosystem.


This article introduces the **Bitget API Broker program**, including how to apply, how to obtain your Broker code, how to include the Broker code in REST / WebSocket requests, and which endpoints currently support it.


## How to Apply

1. Contact your Bitget BD (Business Development), or submit an application via the [application portal](https://www.bitget.com/broker)

## How to Get Your API Broker Code

1. Log in to the [Affiliate Platform](https://newaffiliates.bitget.com/login)
2. Open the [User Profile](https://newaffiliates.bitget.com/dashboard/panel-board)
3. Click **Manage Brokers** --> **Broker overview** and copy the `Channel API Code` in **Broker info**

:::tip{title="Note"}
If you don't see the `Channel API Code` option on the page, please contact your BD to enable this feature for you in the Bitget back office.
:::

## Integration

### REST API

Add the `X-CHANNEL-API-CODE` header to the HTTP request of supported REST endpoints:

| Header | Type | Required | Description |
|:-------|:-----|:---------|:------------|
| X-CHANNEL-API-CODE | String | No | API Broker commission identifier |

```bash title="Request example (UTA place order)"
curl -X POST "https://api.bitget.com/api/v3/trade/place-order" \
  -H "ACCESS-KEY: your-api-key" \
  -H "ACCESS-SIGN: *******" \
  -H "ACCESS-PASSPHRASE: your-passphrase" \
  -H "ACCESS-TIMESTAMP: 1750034396082" \
  -H "X-CHANNEL-API-CODE: your-Channel-API-Code" \
  -H "Content-Type: application/json" \
  -d '{"category":"spot","symbol":"BTCUSDT","side":"buy","orderType":"limit","price":"100","qty":"0.1","timeInForce":"gtc"}'
```

```python title="Request example (Python)"
headers = {
    "ACCESS-KEY": api_key,
    "ACCESS-SIGN": sign,
    "ACCESS-PASSPHRASE": passphrase,
    "ACCESS-TIMESTAMP": timestamp,
    "X-CHANNEL-API-CODE": "your-Channel-API-Code",
    "Content-Type": "application/json",
}
requests.post("https://api.bitget.com/api/v3/trade/place-order", headers=headers, data=body)
```

:::tip{title="Signature"}
The `X-CHANNEL-API-CODE` header is not included in the signature calculation; sign the request the same way as a normal request.
:::

### WebSocket

WebSocket orders cannot set per-request HTTP headers. Pass `apiCode` as a **top-level** field of the order request instead:

| Parameter | Type | Required | Description |
|:----------|:-----|:---------|:------------|
| apiCode | String | No | API Broker code commission identifier |

```json title="Request example (UTA WebSocket place order)"
{
  "op": "trade",
  "id": "1750034396082",
  "category": "spot",
  "topic": "place-order",
  "apiCode": "your-Channel-API-Code",
  "args": [
    {
      "symbol": "BTCUSDT",
      "orderType": "limit",
      "side": "buy",
      "price": "100",
      "qty": "0.1",
      "timeInForce": "gtc"
    }
  ]
}
```

```json title="Request example (Classic WebSocket spot place order)"
{
  "op": "trade",
  "apiCode": "your-Channel-API-Code",
  "args": [
    {
      "id": "xxxxx-xxx-xxx-xxxx-xxxxxx",
      "instType": "SPOT",
      "instId": "BTCUSDT",
      "channel": "place-order",
      "params": {
        "orderType": "limit",
        "side": "buy",
        "size": "1",
        "price": "252",
        "force": "gtc"
      }
    }
  ]
}
```

## Endpoints Supporting API Broker Code

The following endpoints support carrying the API Broker code in the request.

### Unified Trading Account (UTA)

:::tip{title="Permissions"}
Placing orders with a Unified Trading Account requires the API Key to have Unified Trading Account read-write permission.
:::

| Type | Endpoint | Description | How to pass |
|:-----|:---------|:------------|:------------|
| REST | `POST /api/v3/trade/place-order` | [Place Order](/docs/catalog/trading/order-management#place-order) | Add header `X-CHANNEL-API-CODE` |
| REST | `POST /api/v3/trade/place-batch` | [Batch Order](/docs/catalog/trading/order-management#batch-order) | Add header `X-CHANNEL-API-CODE` |
| REST | `POST /api/v3/trade/place-reality-order` | [Place rToken Order](/docs/catalog/reality/trading#place-reality-order) | Add header `X-CHANNEL-API-CODE` |
| REST | `POST /api/v3/trade/close-positions` | [Close All Positions](/docs/catalog/trading/position-management#close-all-positions) | Add header `X-CHANNEL-API-CODE` |
| REST | `POST /api/v3/trade/place-strategy-order` | [Place Strategy Order (TPSL only)](/docs/catalog/trading/strategy-trading#place-strategy-order) | Add header `X-CHANNEL-API-CODE` |
| WebSocket | `place-order` | [Place Order](/docs/uta/websocket/private/Place-Order-Channel) | Top-level field `apiCode` |
| WebSocket | `batch-place` | [Batch Place Order](/docs/uta/websocket/private/Batch-Place-Order-Channel) | Top-level field `apiCode` |

### Classic Account

:::tip{title="Permissions"}
Placing orders with a Classic Account requires the API Key to have Classic Account spot and futures read-write permissions.
:::

| Type | Endpoint | Description | How to pass |
|:-----|:---------|:------------|:------------|
| REST | `POST /api/v2/spot/trade/place-order` | [Spot Place Order](/docs/catalog/classic-spot-trade/classic-spot-trade#place-order) | Add header `X-CHANNEL-API-CODE` |
| REST | `POST /api/v2/spot/trade/batch-orders` | [Spot Batch Place Orders](/docs/catalog/classic-spot-trade/classic-spot-trade#batch-place-orders) | Add header `X-CHANNEL-API-CODE` |
| REST | `POST /api/v2/spot/trade/cancel-replace-order` | [Spot Cancel and Replace Order](/docs/catalog/classic-spot-trade/classic-spot-trade#cancel-an-existing-order-and-send-a-new-order) | Add header `X-CHANNEL-API-CODE` |
| REST | `POST /api/v2/spot/trade/batch-cancel-replace-order` | [Spot Batch Cancel and Replace Orders](/docs/catalog/classic-spot-trade/classic-spot-trade#batch-cancel-existing-order-and-send-new-orders) | Add header `X-CHANNEL-API-CODE` |
| REST | `POST /api/v2/spot/trade/place-plan-order` | [Spot Place Plan Order](/docs/catalog/classic-spot-plan/classic-spot-plan#place-plan-order) | Add header `X-CHANNEL-API-CODE` |
| REST | `POST /api/v2/mix/order/place-order` | [Futures Place Order](/docs/catalog/classic-contract-trade/classic-contract-trade#place-order) | Add header `X-CHANNEL-API-CODE` |
| REST | `POST /api/v2/mix/order/batch-place-order` | [Futures Batch Order](/docs/catalog/classic-contract-trade/classic-contract-trade#batch-order) | Add header `X-CHANNEL-API-CODE` |
| REST | `POST /api/v2/mix/order/click-backhand` | [Futures Reversal](/docs/catalog/classic-contract-trade/classic-contract-trade#reversal) | Add header `X-CHANNEL-API-CODE` |
| REST | `POST /api/v2/mix/order/close-positions` | [Futures Flash Close Position](/docs/catalog/classic-contract-trade/classic-contract-trade#flash-close-position) | Add header `X-CHANNEL-API-CODE` |
| REST | `POST /api/v2/mix/order/place-plan-order` | [Futures Place Trigger Order](/docs/catalog/classic-contract-plan/classic-contract-plan#place-trigger-order) | Add header `X-CHANNEL-API-CODE` |
| REST | `POST /api/v2/mix/order/place-tpsl-order` | [Futures Stop-profit and Stop-loss Plan Orders](/docs/catalog/classic-contract-plan/classic-contract-plan#stop-profit-and-stop-loss-plan-orders) | Add header `X-CHANNEL-API-CODE` |
| REST | `POST /api/v2/mix/order/place-pos-tpsl` | [Futures Simultaneous Stop-profit and Stop-loss Plan Orders](/docs/catalog/classic-contract-plan/classic-contract-plan#simultaneous-stop-profit-and-stop-loss-plan-orders) | Add header `X-CHANNEL-API-CODE` |
| WebSocket | `place-order` (Spot) | [Spot Place Order](/docs/classic/websocket/spot/private/Place-Order-Channel) | Top-level field `apiCode` |
| WebSocket | `place-order` (Futures) | [Futures Place Order](/docs/classic/websocket/contract/private/Place-Order-Channel) | Top-level field `apiCode` |

## Commission Data

Once orders carry your API Broker code, you can verify commission attribution and data via the following endpoints:

| Endpoint | Description |
|:---------|:------------|
| `GET /api/v2/broker/rebate-info` | [Get user broker rebate info](/docs/catalog/classic-broker-commission) |
| `GET /api/v2/broker/order-commission` | [Get broker order commission](/docs/catalog/classic-broker-commission) |
| `GET /api/v2/broker/total-commission` | [Get broker total commission](/docs/catalog/classic-broker-commission) |

## FAQ

### 1. Where can I view commission data?

You can query it programmatically via the Broker Commission APIs listed in "Commission Data" above.

### 2. When is commission data settled / updated?

T+1. Data is updated around 10:30 AM (UTC+8) on the following day.

### 3. Will the order fail if an incorrect API Broker code is passed in the header / request?

No, the order will not fail, but the backend will be unable to attribute the commission correctly.

### 4. How can I tell whether an API Key belongs to a Unified Trading Account or a Classic Account?

If the API Key can call the UTA [Get Account Info](/docs/catalog/account/account-settings#get-account-info) endpoint and receives a normal response, the account is in Unified Trading Account mode; if it returns error code "40084", the account is in Classic Account mode.

---

# API 经纪商

## 经纪商介绍
Bitget 经纪商计划旨在建立一套完善的佣金分成体系，帮助推荐方邀请不同类型的用户并从中获得佣金，既覆盖新用户的获取，也覆盖平台现有用户交易活动的拓展。

理想的合作伙伴包括：交易机器人提供商、社交交易平台、开源交易库、交易执行平台、交易所聚合平台、资产管理平台、量化交易平台及其关联方。

通过经纪商计划，第三方合作伙伴可以直接使用 Bitget 现有的交易所基础设施，无需自行搭建，也无需管理撮合、清算、风控、资金安全或合规等环节。合作伙伴因此能够专注于用户获取、社区运营和产品开发等核心优势，同时享受 Bitget 成熟交易生态带来的价值。

本文介绍 **Bitget API 经纪商**（API Broker）计划，包括如何申请 Broker code、如何在 REST / WebSocket 请求中携带 Broker code，以及目前支持 Broker code 的接口列表。


## 申请入口

1. 联系您的 Bitget BD（Business Development）或通过 [申请入口](https://www.bitget.com/broker) 提交申请

## API Broker Code获取方式

1. 登陆 [代理商平台](https://newaffiliates.bitget.com/zh-CN/login)
2. 打开[用户主页](https://newaffiliates.bitget.com/dashboard/panel-board)
3. 点击 【经纪商管理】 --> 【经纪商总览】 复制 【经纪商信息】下方的 `Channel API Code`

:::tip{title="说明"}
如果您在页面上看不到`Channel API Code`选项，请联系您的BD，由其在Bitget后台为您开启该功能。
:::


## 接入方式

### REST API

在支持的 REST 接口的 HTTP 请求头中添加 `X-CHANNEL-API-CODE`字段：

| 请求头 | 类型 | 是否必须 | 说明 |
|:-------|:-----|:---------|:-----|
| X-CHANNEL-API-CODE | String | 否 | API Broker 返佣标识 |

```bash title="请求示例（统一账户下单）"
curl -X POST "https://api.bitget.com/api/v3/trade/place-order" \
  -H "ACCESS-KEY: your-api-key" \
  -H "ACCESS-SIGN: *******" \
  -H "ACCESS-PASSPHRASE: your-passphrase" \
  -H "ACCESS-TIMESTAMP: 1750034396082" \
  -H "X-CHANNEL-API-CODE: your-Channel-API-Code" \
  -H "Content-Type: application/json" \
  -d '{"category":"spot","symbol":"BTCUSDT","side":"buy","orderType":"limit","price":"100","qty":"0.1","timeInForce":"gtc"}'
```

```python title="请求示例（Python）"
headers = {
    "ACCESS-KEY": api_key,
    "ACCESS-SIGN": sign,
    "ACCESS-PASSPHRASE": passphrase,
    "ACCESS-TIMESTAMP": timestamp,
    "X-CHANNEL-API-CODE": "your-Channel-API-Code",
    "Content-Type": "application/json",
}
requests.post("https://api.bitget.com/api/v3/trade/place-order", headers=headers, data=body)
```

:::tip{title="签名说明"}
`X-CHANNEL-API-CODE` 请求头不参与签名计算，签名方式与普通请求一致。
:::

### WebSocket

WebSocket 下单无法设置单次请求的 HTTP 请求头，请在下单请求的**顶层**字段中传入 `apiCode`：

| 参数名 | 参数类型 | 是否必须 | 描述 |
|:-------|:---------|:---------|:-----|
| apiCode | String | 否 | API Broker code 返佣标识 |

```json title="请求示例（统一账户 WebSocket 下单）"
{
  "op": "trade",
  "id": "1750034396082",
  "category": "spot",
  "topic": "place-order",
  "apiCode": "your-Channel-API-Code",
  "args": [
    {
      "symbol": "BTCUSDT",
      "orderType": "limit",
      "side": "buy",
      "price": "100",
      "qty": "0.1",
      "timeInForce": "gtc"
    }
  ]
}
```

```json title="请求示例（经典账户 WebSocket 现货下单）"
{
  "op": "trade",
  "apiCode": "your-Channel-API-Code",
  "args": [
    {
      "id": "xxxxx-xxx-xxx-xxxx-xxxxxx",
      "instType": "SPOT",
      "instId": "BTCUSDT",
      "channel": "place-order",
      "params": {
        "orderType": "limit",
        "side": "buy",
        "size": "1",
        "price": "252",
        "force": "gtc"
      }
    }
  ]
}
```

## 支持 API Broker code 的接口

以下接口支持请求头携带API Broker code

### 统一账户（UTA）

:::tip{title="权限说明"}
统一账户下单需要API Key拥有统一账户读写权限
:::

| 类型 | 接口 | 说明 | 携带方式 |
|:-----|:-----|:-----|:---------|
| REST | `POST /api/v3/trade/place-order` | [下单](/zh-CN/docs/catalog/trading/order-management#place-order) | 请求头添加 `X-CHANNEL-API-CODE` |
| REST | `POST /api/v3/trade/place-batch` | [批量下单](/zh-CN/docs/catalog/trading/order-management#batch-order) | 请求头添加 `X-CHANNEL-API-CODE` |
| REST | `POST /api/v3/trade/place-reality-order` | [rToken 下单](/zh-CN/docs/catalog/reality/trading#place-reality-order) | 请求头添加 `X-CHANNEL-API-CODE` |
| REST | `POST /api/v3/trade/close-positions` | [一键平仓](/zh-CN/docs/catalog/trading/position-management#close-all-positions) | 请求头添加 `X-CHANNEL-API-CODE` |
| REST | `POST /api/v3/trade/place-strategy-order` | [创建策略单(仅支持tpsl)](/zh-CN/docs/catalog/trading/strategy-trading#place-strategy-order) | 请求头添加 `X-CHANNEL-API-CODE` |
| WebSocket | `place-order` | [下单](/zh-CN/docs/uta/websocket/private/Place-Order-Channel) | 顶层字段 `apiCode` |
| WebSocket | `batch-place` | [批量下单](/zh-CN/docs/uta/websocket/private/Batch-Place-Order-Channel) | 顶层字段 `apiCode` |

### 经典账户（Classic）

:::tip{title="权限说明"}
经典账户下单需要API Key拥有经典账户现货、合约读写权限
:::

| 类型 | 接口 | 说明 | 携带方式 |
|:-----|:-----|:-----|:---------|
| REST | `POST /api/v2/spot/trade/place-order` | [现货下单](/zh-CN/docs/catalog/classic-spot-trade/classic-spot-trade#place-order) | 请求头添加 `X-CHANNEL-API-CODE` |
| REST | `POST /api/v2/spot/trade/batch-orders` | [现货批量下单](/zh-CN/docs/catalog/classic-spot-trade/classic-spot-trade#batch-place-orders) | 请求头添加 `X-CHANNEL-API-CODE` |
| REST | `POST /api/v2/spot/trade/cancel-replace-order` | [现货撤单再下单](/zh-CN/docs/catalog/classic-spot-trade/classic-spot-trade#cancel-an-existing-order-and-send-a-new-order) | 请求头添加 `X-CHANNEL-API-CODE` |
| REST | `POST /api/v2/spot/trade/batch-cancel-replace-order` | [现货批量撤单再下单](/zh-CN/docs/catalog/classic-spot-trade/classic-spot-trade#batch-cancel-existing-order-and-send-new-orders) | 请求头添加 `X-CHANNEL-API-CODE` |
| REST | `POST /api/v2/spot/trade/place-plan-order` | [现货计划委托下单](/zh-CN/docs/catalog/classic-spot-plan/classic-spot-plan#place-plan-order) | 请求头添加 `X-CHANNEL-API-CODE` |
| REST | `POST /api/v2/mix/order/place-order` | [合约下单](/zh-CN/docs/catalog/classic-contract-trade/classic-contract-trade#place-order) | 请求头添加 `X-CHANNEL-API-CODE` |
| REST | `POST /api/v2/mix/order/batch-place-order` | [合约批量下单](/zh-CN/docs/catalog/classic-contract-trade/classic-contract-trade#batch-order) | 请求头添加 `X-CHANNEL-API-CODE` |
| REST | `POST /api/v2/mix/order/click-backhand` | [合约一键反手](/zh-CN/docs/catalog/classic-contract-trade/classic-contract-trade#reversal) | 请求头添加 `X-CHANNEL-API-CODE` |
| REST | `POST /api/v2/mix/order/close-positions` | [合约一键市价平仓](/zh-CN/docs/catalog/classic-contract-trade/classic-contract-trade#flash-close-position) | 请求头添加 `X-CHANNEL-API-CODE` |
| REST | `POST /api/v2/mix/order/place-plan-order` | [合约计划委托下单](/zh-CN/docs/catalog/classic-contract-plan/classic-contract-plan#place-trigger-order) | 请求头添加 `X-CHANNEL-API-CODE` |
| REST | `POST /api/v2/mix/order/place-tpsl-order` | [合约止盈止损计划委托下单](/zh-CN/docs/catalog/classic-contract-plan/classic-contract-plan#stop-profit-and-stop-loss-plan-orders) | 请求头添加 `X-CHANNEL-API-CODE` |
| REST | `POST /api/v2/mix/order/place-pos-tpsl` | [合约止盈止损同时下单](/zh-CN/docs/catalog/classic-contract-plan/classic-contract-plan#simultaneous-stop-profit-and-stop-loss-plan-orders) | 请求头添加 `X-CHANNEL-API-CODE` |
| WebSocket | `place-order`（现货） | [现货下单](/zh-CN/docs/classic/websocket/spot/private/Place-Order-Channel) | 顶层字段 `apiCode` |
| WebSocket | `place-order`（合约） | [合约下单](/zh-CN/docs/classic/websocket/contract/private/Place-Order-Channel) | 顶层字段 `apiCode` |

## 返佣数据查询

订单携带 API Broker code 后，您可以通过以下接口核对返佣归属和佣金数据：

| 接口 | 说明 |
|:-----|:-----|
| `GET /api/v2/broker/rebate-info` | [获取用户的经纪商返佣信息](/zh-CN/docs/catalog/classic-broker-commission) |
| `GET /api/v2/broker/order-commission` | [获取经纪商订单返佣数据](/zh-CN/docs/catalog/classic-broker-commission) |
| `GET /api/v2/broker/total-commission` | [获取经纪商佣金数据](/zh-CN/docs/catalog/classic-broker-commission) |

## 常见问题

### 1. 返佣数据在哪里查看？

您可以通过上方「返佣数据查询」中的经纪商佣金接口以程序方式查询。

### 2. 返佣数据的结算/更新时间是什么？

T+1，隔日的10:30AM UTC+8 左右更新。

### 3. 如果HEADER/请求中传入了错误的Broker API code，会下单失败吗？

不会下单失败，但是后端会无法识别正确返佣

### 4. 通过API Key如何判断账户是统一账户还是经典账户？

如果API Key可以调用UTA[获取账户信息](/zh-CN/docs/catalog/account/account-settings#get-account-info)接口得到正常的响应则为统一账户模式; 如果返回Error code: "40084"，则为经典账户模式