---
exchange: bitget
source_url: https://www.bitget.com/docs/classic/uta-api-upgrade-guide
api_type: Guide
updated_at: 2026-11-19 19:06:33.200027
---

# Upgrade to Unified Trading Account

This guide walks you through upgrading your integration from the Classic account API (v2) to the Unified Trading Account API (v3).

## Why Upgrade to the Unified Trading Account?

The [Unified Trading Account (UTA)](https://www.bitget.com/support/articles/12560603818930) offers the following advantages over the Classic account:

- **Higher capital efficiency**: Trade spot and derivatives from a single account, using multiple crypto assets as shared margin. You no longer need to transfer funds between separate spot, margin, and futures accounts, and profits/losses across products can offset each other.
- **Lower order latency**: UTA's unified account and matching architecture reduces the processing overhead of cross-account and cross-product operations, resulting in faster order placement and execution than the Classic account.
- **Faster access to new features**: New products and capabilities are prioritized for release on UTA, so upgrading gets you earlier access to the latest features.

## How to Upgrade to the Unified Trading Account

There are two ways to upgrade to UTA:

- **Via the web**: see this [upgrade guide](https://www.bitget.com/support/articles/12560603830157) for step-by-step instructions.
- **Via the API**: call the [Upgrade Account](https://www.bitget.com/api-doc/classic/spot/account/Upgrade_Account) endpoint. The API supports the master account initiating the upgrade itself, as well as upgrading sub-accounts.

## Authentication and Signature

:::tip{title="No changes required"}
The signature mechanism is identical between v2 and v3.
:::

Every REST request still needs these headers:

- `ACCESS-KEY`
- `ACCESS-SIGN` (HMAC-SHA256, base64-encoded)
- `ACCESS-TIMESTAMP`
- `ACCESS-PASSPHRASE`
- `Content-Type: application/json`

:::tip{title="No changes required"}
Your existing v2 API Key automatically gains UTA access — there's no need to create a new key.
:::

## Interface and Parameter Mapping

### Place / Cancel / Modify Order

| Action | v2 (Classic) | v3 (UTA) |
|:---|:---|:---|
| Place order | `POST /api/v2/mix/order/place-order` (futures)<br/>`POST /api/v2/spot/trade/place-order` (spot) | `POST /api/v3/trade/place-order` (all products) |
| Cancel order | `POST /api/v2/mix/order/cancel-order`<br/>`POST /api/v2/spot/trade/cancel-order` | `POST /api/v3/trade/cancel-order` |
| Modify order | `POST /api/v2/mix/order/modify-order`<br/>`POST /api/v2/spot/trade/cancel-replace-order`<br/>No WebSocket support | `POST /api/v3/trade/modify-order`<br/>WebSocket modify **supported**, with new `autoCancel` parameter |

**Key parameter changes:**

| v2 Parameter | v3 Parameter | Note |
|:---|:---|:---|
| `productType` (e.g. `usdt-futures`) | `category` (e.g. `USDT-FUTURES`) | Same concept, renamed and uppercased in v3 |
| `marginCoin` | *(removed)* | Not required — UTA determines margin coin automatically from account mode |
| `marginMode` | *(removed from order request)* | Cross/isolated is set at the account/position level, not per order |
| — | `posSide` | New required field in v3 for specifying long/short in hedge mode |
| N/A (single order type per endpoint) | `category` covers `SPOT`, `MARGIN`, `USDT-FUTURES`, `USDC-FUTURES`, `COIN-FUTURES` in one endpoint | v3 unifies all product types under one place-order endpoint |

### Query Orders / Fills

| Action | v2 (Classic) | v3 (UTA) |
|:---|:---|:---|
| Unfilled orders | `GET /api/v2/spot/trade/unfilled-orders`<br/>`GET /api/v2/mix/order/orders-pending` | `GET /api/v3/trade/unfilled-orders` |
| Historical orders | `GET /api/v2/spot/trade/history-orders`<br/>`GET /api/v2/mix/order/orders-history` | `GET /api/v3/trade/history-orders` |
| Fill details | `GET /api/v2/spot/trade/fills`<br/>`GET /api/v2/mix/order/fills` | `GET /api/v3/trade/fills` |

**Pagination parameter change:**

| v2 Parameter | v3 Parameter | Note |
|:---|:---|:---|
| `idLessThan` | `cursor` | Same purpose (fetch older data), different parameter name |

### Account Assets

| Action | v2 (Classic) | v3 (UTA) |
|:---|:---|:---|
| Get account info | `GET /api/v2/spot/account/info` | `GET /api/v3/account/settings` |
| Get balance | `GET /api/v2/spot/account/assets` (spot)<br/>`GET /api/v2/mix/account/accounts` (futures) | `GET /api/v3/account/assets` (single endpoint for all products) |
| Get funding account | N/A (separate funding account concept) | `GET /api/v3/account/funding-assets` |
| Set leverage | `POST /api/v2/mix/account/set-leverage` | `POST /api/v3/account/set-leverage` |
| Set position mode | `POST /api/v2/mix/account/set-position-mode` | `POST /api/v3/account/set-hold-mode` |

### Market Data

| Action | v2 (Classic) | v3 (UTA) |
|:---|:---|:---|
| Get product configuration | `GET /api/v2/spot/public/symbols` (spot)<br/>`GET /api/v2/mix/market/contracts` (futures) | `GET /api/v3/market/instruments` (all products) |
| Get ticker | `GET /api/v2/spot/market/tickers` (spot)<br/>`GET /api/v2/mix/market/ticker` (futures) | `GET /api/v3/market/tickers` (all products) |
| Get order book (depth) | `GET /api/v2/spot/market/orderbook` (spot)<br/>`GET /api/v2/mix/market/merge-depth` (futures) | `GET /api/v3/market/orderbook` (all products) |
| Get candlestick data | `GET /api/v2/spot/market/candles` (spot)<br/>`GET /api/v2/mix/market/candles` (futures) | `GET /api/v3/market/candles` (all products) |
| Get recent trades | `GET /api/v2/spot/market/fills` (spot)<br/>`GET /api/v2/mix/market/fills` (futures) | `GET /api/v3/market/fills` (all products) |

### WebSocket Public Channels

| Channel | v2 (Classic) Subscription | v3 (UTA) Subscription |
|:---|:---|:---|
| Ticker | `{"instType": "SPOT", "channel": "ticker", "instId": "BTCUSDT"}` | `{"instType": "spot", "topic": "ticker", "symbol": "BTCUSDT"}` |
| Trades | `{"instType": "SPOT", "channel": "trade", "instId": "BTCUSDT"}` | `{"instType": "spot", "topic": "publicTrade", "symbol": "BTCUSDT"}` |
| Candlesticks | `{"instType": "SPOT", "channel": "candle1m", "instId": "BTCUSDT"}` | `{"instType": "spot", "topic": "kline", "symbol": "BTCUSDT", "interval": "1m"}` |
| Order book | `{"instType": "SPOT", "channel": "books5", "instId": "BTCUSDT"}` | `{"instType": "spot", "topic": "books5", "symbol": "BTCUSDT"}` |
| Liquidation | Not available in Classic | `{"instType": "usdt-futures", "topic": "liquidation"}` |

:::info{title="Key structural changes"}
- v2 encodes the candle interval into the channel name (e.g. `candle1m`, `candle5m`). v3 keeps `topic: "kline"` fixed and passes the interval as a separate `interval` field.
- v2's depth channel supports up to 15 levels (`books15`). v3 renames the deepest tier to `books50` (up to 50 levels) and adds a parallel `rpi-books*` channel for RPI depth — see [RPI Orderbook Channel](/docs/uta/websocket/public/RPI-OrderBook-Channel).
- The `liquidation` channel is new in UTA and has no v2 equivalent.
:::

### WebSocket Private Channels

| Channel | v2 (Classic) Subscription | v3 (UTA) Subscription |
|:---|:---|:---|
| Order updates | `{"instType": "USDT-FUTURES", "channel": "orders", "instId": "default"}` | `{"instType": "UTA", "topic": "order"}` |
| Account updates | `{"instType": "SPOT", "channel": "account", "coin": "default"}` | `{"instType": "UTA", "topic": "account"}` |
| Position updates | `{"instType": "USDT-FUTURES", "channel": "positions", "instId": "default"}` | `{"instType": "UTA", "topic": "position"}` |

:::info{title="Key structural change"}
v2 uses `channel` + `instType` + `instId`/`coin` to scope a subscription per product type. v3 simplifies this to a single `instType: "UTA"` + `topic`, since one UTA channel now covers all product types at once.
:::

## SDK V3 Version Notes

Bitget V3 will provide official SDKs in the following languages:

- ☕ **[Java](https://github.com/BitgetLimited/v3-bitget-api-sdk/tree/master/bitget-java-sdk-api)**
- 🐍 **[Python](https://github.com/BitgetLimited/v3-bitget-api-sdk/tree/master/bitget-python-sdk-api)**
- 🟩 **[Node.js](https://github.com/BitgetLimited/v3-bitget-api-sdk/tree/master/bitget-node-sdk-api)**
- 🐹 **[Golang](https://github.com/BitgetLimited/v3-bitget-api-sdk/tree/master/bitget-golang-sdk-api)**
- 🐘 **[PHP](https://github.com/BitgetLimited/v3-bitget-api-sdk/tree/master/bitget-php-sdk-api)**

## Migration Notes

:::warning{title="Note 1 — Forgetting to set `posSide` in Hedge Mode"}
If your account is in Hedge Mode, `posSide` (`long` or `short`) is required. Omitting it will cause the order to be rejected. In One-way Mode, `posSide` can be omitted.
:::

:::warning{title="Note 2 — Expecting order size to mean the same thing across product types"}
In v2, `size` means different things depending on order type and side (base coin vs. quote coin for market buy). In v3, the field is renamed to `qty`, but the same base-coin/quote-coin distinction for market orders still applies — check the [Place Order](/docs/catalog/trading/order-management) reference for the product you're trading.
:::

:::warning{title="Note 3 — Assuming error codes are unchanged"}
Error code values and meanings are **not guaranteed to be identical** between v2 and v3, even for conceptually similar failures. Always check the [UTA Error Code](/docs/uta/error-code/restapi) reference rather than reusing your v2 error-handling logic as-is.
:::

## Migration Checklist

- [ ] Switch the account mode to UTA via Web/API
- [ ] Update your base URL and endpoint paths from `/api/v2/...` to `/api/v3/...`
- [ ] Update order request payloads: remove `marginCoin`/`marginMode`, add `category` and `posSide`, rename `size` to `qty`
- [ ] Update pagination logic: rename `idLessThan` to `cursor`
- [ ] Update WebSocket subscriptions: switch from `channel`+`instType` to `instType: "UTA"` + `topic`
- [ ] Re-test order placement, modification, and cancellation end-to-end in demo trading first
- [ ] Update your error-handling logic against the UTA error code table
- [ ] Verify account/position WebSocket pushes match your expected field names (e.g. `createdTime`/`updatedTime` instead of `cTime`/`uTime`)

## Code Example: Place Order (v2 vs v3)

**v2 (Classic) — placing a USDT-margined futures order:**

```bash title="Request Example"
curl -X POST "https://api.bitget.com/api/v2/mix/order/place-order" \
   -H "ACCESS-KEY:*******" \
   -H "ACCESS-SIGN:*******" \
   -H "ACCESS-PASSPHRASE:*****" \
   -H "ACCESS-TIMESTAMP:1659076670000" \
   -H "locale:en-US" \
   -H "Content-Type: application/json" \
   -d '{
    "symbol": "BTCUSDT",
    "productType": "usdt-futures",
    "marginMode": "crossed",
    "marginCoin": "USDT",
    "clientOid": "testBTC0123",
    "side": "buy",
    "orderType": "limit",
    "price": "50000",
    "size": "0.1"
}'
```

```json title="Response Example"
{
  "code": "00000",
  "msg": "success",
  "data": {
    "clientOid": "testBTC0123",
    "orderId": "1234567890"
  }
}
```

**v3 (UTA) — placing the equivalent order:**

```bash title="Request Example"
curl -X POST "https://api.bitget.com/api/v3/trade/place-order" \
   -H "ACCESS-KEY:*******" \
   -H "ACCESS-SIGN:*******" \
   -H "ACCESS-PASSPHRASE:*****" \
   -H "ACCESS-TIMESTAMP:1659076670000" \
   -H "locale:en-US" \
   -H "Content-Type: application/json" \
   -d '{
    "category": "USDT-FUTURES",
    "symbol": "BTCUSDT",
    "clientOid": "testBTC0123",
    "side": "buy",
    "posSide": "long",
    "orderType": "limit",
    "price": "50000",
    "qty": "0.1",
    "timeInForce": "gtc"
}'
```

```json title="Response Example"
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695806875837,
  "data": {
    "clientOid": "testBTC0123",
    "orderId": "1234567890"
  }
}
```

:::info{title="Note"}
Notice the request body drops `productType`/`marginMode`/`marginCoin` in favor of `category`, and adds `posSide`. The response structure is otherwise the same.
:::

## Next Steps

Once your migration is complete, see the [Unified Trading Account Best Practices Guide](https://www.bitget.com/api-doc/uta/best-practices) for details on order lifecycle, WebSocket channel behavior, and self-trade prevention under UTA.

---

# 统一账户升级指南

这篇指南教你怎么把接入方式从经典账户 API（v2）换成统一账户 API（v3）。

## 为什么要升级到统一账户？

相比经典账户，[统一账户（UTA）](https://www.bitget.com/zh-CN/support/articles/12560603818930)有以下优势：

- **资金利用率更高**：可以在同一个账户中交易现货和各类衍生品，使用多币种资产作为共享保证金。你不再需要在现货、杠杆、合约等独立账户之间划转资金，不同产品间的盈亏还可以互相抵消。
- **下单延迟更低**：统一账户和撮合架构减少了跨账户、跨产品操作带来的处理开销，下单和成交速度比经典账户更快。
- **新功能更新更快**：新产品和新功能会优先在统一账户上线，升级后可以更早用上最新功能。

## 如何升级至统一账户

升级至统一账户有两种方式：

- **网页端升级**：参考[网页端升级介绍](https://www.bitget.com/zh-CN/support/articles/12560603830157)按步骤操作。
- **使用 API**：调用[升级账户](https://www.bitget.com/zh-CN/api-doc/classic/spot/account/Upgrade_Account)接口。接口支持母账户调用后自行升级，以及升级子账户。

## 认证与签名

:::tip{title="无需改动"}
v2 和 v3 的签名机制完全一致。
:::

每个 REST 请求仍然需要以下请求头：

- `ACCESS-KEY`
- `ACCESS-SIGN`（HMAC-SHA256，base64 编码）
- `ACCESS-TIMESTAMP`
- `ACCESS-PASSPHRASE`
- `Content-Type: application/json`

:::tip{title="无需改动"}
你现有的 v2 API Key 会自动获得 UTA 访问权限，无需创建新的 Key。
:::

## 接口与参数映射对照表

### 下单 / 撤单 / 改单

| 操作 | v2（经典账户） | v3（统一账户） |
|:---|:---|:---|
| 下单 | `POST /api/v2/mix/order/place-order`（合约）<br/>`POST /api/v2/spot/trade/place-order`（现货） | `POST /api/v3/trade/place-order`（所有产品统一） |
| 撤单 | `POST /api/v2/mix/order/cancel-order`<br/>`POST /api/v2/spot/trade/cancel-order` | `POST /api/v3/trade/cancel-order` |
| 改单 | `POST /api/v2/mix/order/modify-order`<br/>`POST /api/v2/spot/trade/cancel-replace-order`<br/>不支持 WebSocket 改单 | `POST /api/v3/trade/modify-order`<br/>**支持** WebSocket 改单，新增 `autoCancel` 参数 |

**关键参数变化：**

| v2 参数 | v3 参数 | 说明 |
|:---|:---|:---|
| `productType`（如 `usdt-futures`） | `category`（如 `USDT-FUTURES`） | 概念相同，v3 中重命名并改为大写 |
| `marginCoin` | *（已移除）* | 无需传入——UTA 根据账户模式自动确定保证金币种 |
| `marginMode` | *（从下单请求中移除）* | 全仓/逐仓在账户/仓位层面设置，不再按订单单独指定 |
| — | `posSide` | v3 新增必填字段，用于在双向持仓模式下指定多头/空头 |
| 无（每个产品类型对应独立接口） | `category` 一个接口即可覆盖 `SPOT`、`MARGIN`、`USDT-FUTURES`、`USDC-FUTURES`、`COIN-FUTURES` | v3 将所有产品类型统一到同一个下单接口 |

### 查询订单 / 成交记录

| 操作 | v2（经典账户） | v3（统一账户） |
|:---|:---|:---|
| 当前委托 | `GET /api/v2/spot/trade/unfilled-orders`<br/>`GET /api/v2/mix/order/orders-pending` | `GET /api/v3/trade/unfilled-orders` |
| 历史委托 | `GET /api/v2/spot/trade/history-orders`<br/>`GET /api/v2/mix/order/orders-history` | `GET /api/v3/trade/history-orders` |
| 成交明细 | `GET /api/v2/spot/trade/fills`<br/>`GET /api/v2/mix/order/fills` | `GET /api/v3/trade/fills` |

**分页参数变化：**

| v2 参数 | v3 参数 | 说明 |
|:---|:---|:---|
| `idLessThan` | `cursor` | 用途相同（获取更早的数据），参数名不同 |

### 账户资产查询

| 操作 | v2（经典账户） | v3（统一账户） |
|:---|:---|:---|
| 获取账户信息 | `GET /api/v2/spot/account/info` | `GET /api/v3/account/settings` |
| 获取余额 | `GET /api/v2/spot/account/assets`（现货）<br/>`GET /api/v2/mix/account/accounts`（合约） | `GET /api/v3/account/assets`（所有产品统一为一个接口） |
| 获取资金账户资产 | 无（v2 中资金账户是独立概念） | `GET /api/v3/account/funding-assets` |
| 设置杠杆 | `POST /api/v2/mix/account/set-leverage` | `POST /api/v3/account/set-leverage` |
| 设置持仓模式 | `POST /api/v2/mix/account/set-position-mode` | `POST /api/v3/account/set-hold-mode` |

### 行情接口

| 操作 | v2（经典账户） | v3（统一账户） |
|:---|:---|:---|
| 获取产品配置 | `GET /api/v2/spot/public/symbols`（现货）<br/>`GET /api/v2/mix/market/contracts`（合约） | `GET /api/v3/market/instruments`（所有产品统一） |
| 获取行情快照 | `GET /api/v2/spot/market/tickers`（现货）<br/>`GET /api/v2/mix/market/ticker`（合约） | `GET /api/v3/market/tickers`（所有产品统一） |
| 获取深度数据 | `GET /api/v2/spot/market/orderbook`（现货）<br/>`GET /api/v2/mix/market/merge-depth`（合约） | `GET /api/v3/market/orderbook`（所有产品统一） |
| 获取 K 线数据 | `GET /api/v2/spot/market/candles`（现货）<br/>`GET /api/v2/mix/market/candles`（合约） | `GET /api/v3/market/candles`（所有产品统一） |
| 获取最近成交记录 | `GET /api/v2/spot/market/fills`（现货）<br/>`GET /api/v2/mix/market/fills`（合约） | `GET /api/v3/market/fills`（所有产品统一） |

### WebSocket 公有频道

| 频道 | v2（经典账户）订阅方式 | v3（统一账户）订阅方式 |
|:---|:---|:---|
| 行情快照 | `{"instType": "SPOT", "channel": "ticker", "instId": "BTCUSDT"}` | `{"instType": "spot", "topic": "ticker", "symbol": "BTCUSDT"}` |
| 最新成交 | `{"instType": "SPOT", "channel": "trade", "instId": "BTCUSDT"}` | `{"instType": "spot", "topic": "publicTrade", "symbol": "BTCUSDT"}` |
| K 线 | `{"instType": "SPOT", "channel": "candle1m", "instId": "BTCUSDT"}` | `{"instType": "spot", "topic": "kline", "symbol": "BTCUSDT", "interval": "1m"}` |
| 深度 | `{"instType": "SPOT", "channel": "books5", "instId": "BTCUSDT"}` | `{"instType": "spot", "topic": "books5", "symbol": "BTCUSDT"}` |
| 强平信息 | 经典账户无对应频道 | `{"instType": "usdt-futures", "topic": "liquidation"}` |

:::info{title="关键结构变化"}
- v2 把 K 线的时间粒度编码进频道名（如 `candle1m`、`candle5m`）。v3 的 `topic` 固定为 `"kline"`，时间粒度通过独立的 `interval` 字段传入。
- v2 的深度频道最多支持 15 档（`books15`）。v3 将最深档位改名为 `books50`（最多支持 50 档），并新增了对应的 `rpi-books*` 频道用于 RPI 深度——详见[RPI 深度频道](/docs/uta/websocket/public/RPI-OrderBook-Channel)。
- `liquidation`（强平信息）频道是 UTA 新增的，经典账户没有对应频道。
:::

### WebSocket 私有频道

| 频道 | v2（经典账户）订阅方式 | v3（统一账户）订阅方式 |
|:---|:---|:---|
| 订单更新 | `{"instType": "USDT-FUTURES", "channel": "orders", "instId": "default"}` | `{"instType": "UTA", "topic": "order"}` |
| 账户更新 | `{"instType": "SPOT", "channel": "account", "coin": "default"}` | `{"instType": "UTA", "topic": "account"}` |
| 仓位更新 | `{"instType": "USDT-FUTURES", "channel": "positions", "instId": "default"}` | `{"instType": "UTA", "topic": "position"}` |

:::info{title="关键结构变化"}
v2 使用 `channel` + `instType` + `instId`/`coin` 按产品类型分别订阅。v3 简化为统一的 `instType: "UTA"` + `topic`，因为一个 UTA 频道现在能同时覆盖所有产品类型。
:::

## SDK V3 版本说明

Bitget V3 将提供以下语言的官方 SDK：

- ☕ **[Java](https://github.com/BitgetLimited/v3-bitget-api-sdk/tree/master/bitget-java-sdk-api)**
- 🐍 **[Python](https://github.com/BitgetLimited/v3-bitget-api-sdk/tree/master/bitget-python-sdk-api)**
- 🟩 **[Node.js](https://github.com/BitgetLimited/v3-bitget-api-sdk/tree/master/bitget-node-sdk-api)**
- 🐹 **[Golang](https://github.com/BitgetLimited/v3-bitget-api-sdk/tree/master/bitget-golang-sdk-api)**
- 🐘 **[PHP](https://github.com/BitgetLimited/v3-bitget-api-sdk/tree/master/bitget-php-sdk-api)**

## 迁移注意事项

:::warning{title="注意事项一 —— 双向持仓模式下忘记传 `posSide`"}
如果你的账户处于双向持仓模式，`posSide`（`long` 或 `short`）为必填字段。不传会导致订单被拒绝。单向持仓模式下 `posSide` 可以省略。
:::

:::warning{title="注意事项二 —— 以为下单数量字段在所有产品类型下含义相同"}
在 v2 中，`size` 的含义会因订单类型和方向而不同（市价买单是计价币数量，其余情况是基础币数量）。v3 中该字段重命名为 `qty`，但市价单基础币/计价币的区分规则依然存在——请查阅你所交易产品对应的[下单接口](/docs/catalog/trading/order-management)文档确认具体含义。
:::

:::warning{title="注意事项三 —— 以为错误码没有变化"}
v2 和 v3 之间的错误码取值和含义**不保证一致**，即使是概念上相似的失败场景也是如此。请始终查阅 [UTA 错误码](/docs/uta/error-code/restapi)文档，不要直接复用你原有的 v2 错误处理逻辑。
:::

## 完整迁移步骤清单

- [ ] 通过网页端/API 将账户模式切换为 UTA（统一账户）
- [ ] 将接口基础路径和路径从 `/api/v2/...` 更新为 `/api/v3/...`
- [ ] 更新下单请求参数：移除 `marginCoin`/`marginMode`，新增 `category` 和 `posSide`，将 `size` 重命名为 `qty`
- [ ] 更新分页逻辑：将 `idLessThan` 重命名为 `cursor`
- [ ] 更新 WebSocket 订阅方式：从 `channel`+`instType` 切换为 `instType: "UTA"` + `topic`
- [ ] 先在模拟盘完整测试下单、改单、撤单的全流程
- [ ] 按照 UTA 错误码表更新你的错误处理逻辑
- [ ] 核实账户/仓位 WebSocket 推送字段名是否符合预期（例如 `createdTime`/`updatedTime` 而非 `cTime`/`uTime`）

## 代码示例：下单接口 v2 与 v3 对比

**v2（经典账户）—— 下一笔 USDT 保证金合约订单：**

```bash title="请求示例"
curl -X POST "https://api.bitget.com/api/v2/mix/order/place-order" \
   -H "ACCESS-KEY:*******" \
   -H "ACCESS-SIGN:*******" \
   -H "ACCESS-PASSPHRASE:*****" \
   -H "ACCESS-TIMESTAMP:1659076670000" \
   -H "locale:en-US" \
   -H "Content-Type: application/json" \
   -d '{
    "symbol": "BTCUSDT",
    "productType": "usdt-futures",
    "marginMode": "crossed",
    "marginCoin": "USDT",
    "clientOid": "testBTC0123",
    "side": "buy",
    "orderType": "limit",
    "price": "50000",
    "size": "0.1"
}'
```

```json title="返回示例"
{
  "code": "00000",
  "msg": "success",
  "data": {
    "clientOid": "testBTC0123",
    "orderId": "1234567890"
  }
}
```

**v3（统一账户）—— 下同等效果的订单：**

```bash title="请求示例"
curl -X POST "https://api.bitget.com/api/v3/trade/place-order" \
   -H "ACCESS-KEY:*******" \
   -H "ACCESS-SIGN:*******" \
   -H "ACCESS-PASSPHRASE:*****" \
   -H "ACCESS-TIMESTAMP:1659076670000" \
   -H "locale:en-US" \
   -H "Content-Type: application/json" \
   -d '{
    "category": "USDT-FUTURES",
    "symbol": "BTCUSDT",
    "clientOid": "testBTC0123",
    "side": "buy",
    "posSide": "long",
    "orderType": "limit",
    "price": "50000",
    "qty": "0.1",
    "timeInForce": "gtc"
}'
```

```json title="返回示例"
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695806875837,
  "data": {
    "clientOid": "testBTC0123",
    "orderId": "1234567890"
  }
}
```

:::info{title="说明"}
可以看到，请求体中去掉了 `productType`/`marginMode`/`marginCoin`，改用 `category`，并新增了 `posSide`。返回结构基本保持一致。
:::

## 下一步

完成迁移后，请参阅[统一账户最佳实践指南](https://www.bitget.com/zh-CN/api-doc/uta/best-practices)，了解 UTA 下订单生命周期、WebSocket 频道行为以及自成交防护机制的详细说明。