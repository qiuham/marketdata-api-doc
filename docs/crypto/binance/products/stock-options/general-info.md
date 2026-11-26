---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/stock-options/general-info
api_type: Guide
updated_at: 2026-11-26 18:29:29.779499
---

# General Info

This module documents the Stock Option Trading REST API. Base URL, HMAC / Ed25519 signing,
timestamps, `recvWindow`, and the SAPI error envelope are identical to other SAPI endpoint families
— see the root [General Info](../common/sapi/general-info.md) for those.

This page lists only what is specific to the Stock Option Trading module.

## Enabling Options

There is no API for account opening. Enable option trading in the Binance App first; orders and
exercise requests from an account without options enabled are rejected with `497203`.

## Rate Limits

In addition to the shared SAPI weight / IP limits, the following endpoint carries a per-UID
request-rate cap:

| Endpoint            | Limit                    |
| ------------------- | ------------------------ |
| `POST /order/place` | 200 requests / min (UID) |

Other endpoints (market data, queries, cancel, cancel-all, exercise, listenKey) have no separate
per-UID cap.

When the per-UID cap is exceeded, HTTP `429` is returned:

```json
{ "code": -1003, "msg": "Too many requests; current request has limited." }
```

The limit is counted per minute and resets in the next window.

Stock option and stock endpoints also share a global upstream broker limit. When it is reached,
Place Option Order and Submit Option Exercise return `497301`. For orders, retry with the **same**
`clientOrderId` (see [Error Code](./error-code.md)).

## Request Security

| Security type | Endpoints                                                                                 |
| ------------- | ----------------------------------------------------------------------------------------- |
| `MARKET_DATA` | Option Expirations, Option Contracts, Option Exchange Info                                |
| `TRADE`       | Place Option Order, Cancel Option Order, Cancel All Option Orders, Submit Option Exercise |
| `USER_DATA`   | Order, trade, position, exercise and settlement event queries                             |
| `USER_STREAM` | Create / Renew Listen Key                                                                 |

`MARKET_DATA` endpoints only require the `X-MBX-APIKEY` header; no signature, `timestamp` or
`recvWindow` is needed.

Submit Option Exercise requires `TRADE` rather than `USER_DATA`, because exercising changes
positions and balances.

## URL Prefix

All endpoints in this module share the prefix:

```
/sapi/v1/equity/option/
```

There is no `/sapi/v1/bstocks/option/` alias.

## Numbers and Timestamps

- **Decimal fields are returned as strings** in REST responses, with trailing zeros removed: `1.50`
  is returned as `"1.5"`, `148.00` as `"148"`. Parse them as decimal strings; do not convert to
  floating point before comparing. Integer fields (e.g. `contractSize`, `tranId`, the paging
  `total`, timestamps) are JSON numbers. The user data stream pushes JSON numbers instead (see
  [WebSocket Streams General Info](./websocket-streams-general-info.md)).
- **Empty fields are omitted** rather than returned as `null`. Fields documented as "not returned
  when ..." or "returned only when ..." follow this rule.
- **Time fields** (`*Time`, `*At`, `settlementDate`) are millisecond timestamps (integers).
- **`expirationDate`**: Option Expirations and Option Contracts return a `YYYY-MM-DD` string. All
  other endpoints, including the `ed` field of the user data stream, return the **millisecond
  timestamp of 12:00 ET on the expiration day**. Convert it in the `America/New_York` time zone and
  take the date part. Converting in UTC gives the same date, but time zones at UTC+8 or further east
  (during US daylight saving time) / UTC+7 or further east (during US standard time) read it as the
  next day. It is not the expiration moment; the expiration moment is the market close (see
  `optionsLateClose` in Option Exchange Info).

## Quote Asset

- Prices are in USD. USDC:USD is 1:1, and orders are paid in `USDC` only.
- `quoteAsset` defaults to `USDC`; other values are rejected with `497104`.

## No Market Data

No option market data is provided, including but not limited to last price, previous close, best bid
/ ask and size, mark price, volume, open interest, implied volatility, Greeks (delta / gamma / theta
/ vega) and break-even price. The Market Data endpoints return contract reference data only.

## Order Constraints

- **Limit orders only**: there is no `orderType` parameter; every order is `LIMIT`. Query endpoints
  may return orders with `orderType` = `MARKET`: these are automatic liquidations by the broker on
  the expiration date, executed as market orders (`autoLiquidation` = `true` in Option Order History
  / Option Order Detail).
- **`timeInForce` is `DAY` only.**
- **Whole contracts only**: fractional contracts are not supported.
- **Fees are calculated by the server**: the premium and all fees are calculated and locked at
  placement. Callers do not and cannot pass payment details.
- **Price checks**: a limit price must be a multiple of `tickSize`; the order notional (`price` ×
  `quantity` × `multiplier`, excluding fees) must fall within `[minNotional, maxNotional]`
  (inclusive) from Option Exchange Info; the limit price of a `SELL` put order must not exceed the
  strike price.

---

# 基本信息

本模块说明股票期权交易 REST API。Base URL、HMAC / Ed25519 签名、时间戳、`recvWindow`
以及 SAPI 错误返回格式与其他 SAPI 接口相同，见根目录 [基本信息](../common/sapi/general-info.md)。

本页只列出股票期权交易模块特有的内容。

## 开通期权

SAPI 不提供开户接口。请先在 Binance App 内开通期权交易；未开通期权的账户下单或提交行权会返回
`497203`。

## 频率限制

除 SAPI 通用的权重 / IP 限制外，以下接口有单用户（UID）频率上限：

| 接口                | 限制                 |
| ------------------- | -------------------- |
| `POST /order/place` | 200 次 / 分钟（UID） |

其他接口（合约数据、查询、撤单、全部撤单、行权、listenKey）不单独限制。

单用户超过限频时返回 HTTP `429`：

```json
{ "code": -1003, "msg": "Too many requests; current request has limited." }
```

按分钟窗口计数，下一个窗口自动恢复。

期权与美股接口还共享上游券商的全局上限。该上限触发时，下单与提交行权返回
`497301`。下单请用**同一个** `clientOrderId` 重试（见[错误代码](./error-code.md)）。

## 请求鉴权类型

| 鉴权类型      | 接口                                       |
| ------------- | ------------------------------------------ |
| `MARKET_DATA` | 到期日列表、合约列表、合约交易规则         |
| `TRADE`       | 下单、撤单、全部撤单、提交行权             |
| `USER_DATA`   | 订单、成交、持仓、行权与结算事件相关的查询 |
| `USER_STREAM` | 创建 / 续期 Listen Key                     |

`MARKET_DATA` 接口只需在 Header 中携带 `X-MBX-APIKEY`，无需签名，也无需 `timestamp` / `recvWindow`。

提交行权需要 `TRADE` 权限而不是 `USER_DATA`，因为行权会真实改变持仓与资金。

## URL 前缀

本模块所有接口共享前缀：

```
/sapi/v1/equity/option/
```

没有 `/sapi/v1/bstocks/option/` 别名。

## 数值与时间格式

- **REST 响应中的小数字段（DECIMAL）一律以字符串返回**，并去掉末尾多余的 0：`1.50` 返回
  `"1.5"`，`148.00` 返回 `"148"`。请按十进制字符串解析，不要转成浮点数再比较。整数字段（如
  `contractSize`、`tranId`、分页 `total`、时间戳）为 JSON number。用户数据流推送的是 JSON
  number（见[WebSocket 流基本信息](./websocket-streams-general-info.md)）。
- **值为空的字段不返回**，而不是返回
  `null`。文档中标注「……时不返回」「仅……时返回」的字段都属于这种情况。
- **时间字段**（`*Time`、`*At`、`settlementDate`）为毫秒时间戳，整数。
- **`expirationDate`**：「到期日列表」「合约列表」返回 `YYYY-MM-DD` 字符串；其余接口（含用户数据流的
  `ed`）均为**到期日当天 12:00
  ET 的毫秒时间戳**。请按美东时区（`America/New_York`）转换后取日期部分：按 UTC 转换也落在同一天，但 UTC+8（夏令时期间）/
  UTC+7（冬令时期间）及以东的时区会读成次日。它不是到期时刻，到期时刻是收盘时间（见「合约交易规则」的
  `optionsLateClose`）。

## 计价资产

- 价格以 USD 计。USDC:USD 为 1:1，下单只接受 `USDC` 支付。
- `quoteAsset` 默认 `USDC`，传其他值返回 `497104`。

## 不提供行情

不提供任何期权行情，包括但不限于：最新价、昨收、买一 / 卖一价格及挂单量、mark 价、成交量、持仓量、隐含波动率、Greeks（delta
/ gamma / theta / vega）、盈亏平衡价。合约数据接口只返回合约参考数据。

## 下单限制

- **只支持限价单**：没有 `orderType` 参数，全部按 `LIMIT` 处理。查询接口中可能出现 `orderType` =
  `MARKET` 的订单：那是到期日券商自动强平，以市价单执行（「订单历史」「订单详情」中
  `autoLiquidation` = `true`）。
- **`timeInForce` 只支持 `DAY`。**
- **张数必须是整数**：不支持碎张。
- **手续费由服务端计算**：下单时自动算出权利金与各项费用并一并冻结，调用方不需要也不能传支付明细。
- **价格校验**：限价需符合「合约交易规则」的 `tickSize` 步进；订单名义金额（`price` × `quantity` ×
  `multiplier`，不含手续费）需落在 `[minNotional, maxNotional]` 闭区间内；卖出 put（`SELL`
  方向）的限价不得高于行权价。