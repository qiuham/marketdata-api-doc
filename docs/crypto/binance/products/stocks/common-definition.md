---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/stocks/common-definition
api_type: Guide
updated_at: 2026-11-18 01:55:25.394347
---

# Common Definition

This page lists every enum value accepted or returned by Stocks Trading endpoints.

**Global rule:** all enum string values are **UPPERCASE** on both request and response.

## side

Used on `/order/place` (request), `/order/history` filter (request), and on every order / trade row
(response).

| Value  | Description |
| ------ | ----------- |
| `BUY`  | Buy side    |
| `SELL` | Sell side   |

## orderType

Used on `/order/place` (request), `/order/history` filter (request), and on every order / trade row
(response).

| Value    | Description  |
| -------- | ------------ |
| `MARKET` | Market order |
| `LIMIT`  | Limit order  |

## timeInForce

Used on `/order/place` (request). Optional; defaults to `DAY`.

| Value | Description                                                                                                                           |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------- |
| `DAY` | Good until end of the trading day (default)                                                                                           |
| `GTC` | Good-til-cancelled. Only supported on `LIMIT` orders. Fractional GTC orders must be placed with `tradingSession = EXTENDED` or `24H`. |

## tradingSession / session

Used on `/order/place` (request) as `tradingSession`; returned on order / trade rows as `session`.
Required for `LIMIT`, forbidden for `MARKET`.

| Value      | Description                                                            |
| ---------- | ---------------------------------------------------------------------- |
| `RTH`      | Regular Trading Hours (09:30–16:00 ET) only                            |
| `EXTENDED` | Pre-Market + RTH + Post-Market (04:00–20:00 ET)                        |
| `24H`      | Overnight + Pre-Market + RTH + Post-Market (20:00 → next-day 20:00 ET) |

## walletType

Used on `/order/place` (request, BUY side only). Optional; defaults to `CARD`. SELL orders always
settle against `CARD` regardless of what is passed.

| Value  | Description              |
| ------ | ------------------------ |
| `CARD` | Funding wallet (default) |
| `MAIN` | Spot wallet              |

## orderStatus (filter)

Used on `/order/history` as a comma-separated multi-value filter. Accepts only these terminal-status
values; in-flight statuses (`NEW`, `ACCEPTED`) are not valid filter inputs.

| Value              | Description      |
| ------------------ | ---------------- |
| `FILLED`           | Fully filled     |
| `PARTIALLY_FILLED` | Partially filled |
| `CANCELED`         | Canceled         |
| `EXPIRED`          | Expired          |
| `REJECTED`         | Rejected         |

## status (order / trade response)

Returned on each order / trade row. Covers both in-flight and terminal states.

| Value              | Description                                        |
| ------------------ | -------------------------------------------------- |
| `NEW`              | Accepted locally, pending upstream acknowledgement |
| `ACCEPTED`         | Accepted by upstream broker                        |
| `PARTIALLY_FILLED` | Partially filled                                   |
| `FILLED`           | Fully filled                                       |
| `CANCELED`         | Canceled                                           |
| `EXPIRED`          | Expired (end-of-day close for `DAY` orders, etc.)  |
| `REJECTED`         | Rejected                                           |

> **Note:** The `status` field on the **Place Order** response (`/order/place`) and on the **Cancel
> Order** response (`/order/cancel`) is a separate acknowledgement code, not an order lifecycle
> status. It only carries `S` (accepted) or `F` (failed).

## tradability (exchange info)

Returned on `/market/exchangeInfo` → `symbols[].tradability`. Indicates which trading direction is
currently allowed for a symbol.

| Value      | Description                                       |
| ---------- | ------------------------------------------------- |
| `BUY_SELL` | Both buying and selling are allowed.              |
| `BUY`      | Only buying is allowed (new long positions only). |
| `SELL`     | Only selling is allowed (close-only).             |
| `NONE`     | No trading allowed (halted / suspended).          |

## convertType (tokenized)

Used on `/tokenized/convert-status` (request) and returned in `/tokenized/history` and
`/tokenized/convert-status` responses.

| Value    | Description                                             |
| -------- | ------------------------------------------------------- |
| `MINT`   | Mint tokenized asset from an underlying equity holding. |
| `REDEEM` | Redeem tokenized asset back into the underlying equity. |

## status (tokenized convert response)

Returned on `/tokenized/mint`, `/tokenized/redeem`, `/tokenized/convert-status`, and each row of
`/tokenized/history`. This is a **separate status code from the order lifecycle `status`** — mint /
redeem is an async convert flow with its own three-state machine.

| Value | Description                   |
| ----- | ----------------------------- |
| `P`   | Processing (async in flight). |
| `S`   | Success (convert completed).  |
| `F`   | Failed.                       |

---

# 通用枚举定义

本页列出股票交易模块所有接口使用的枚举值。

**全局约定：** 所有枚举字符串值在请求与响应中**一律 UPPERCASE**。

## side

用于 `/order/place` 请求、`/order/history` 过滤参数，以及每条订单 / 成交响应记录。

| 值     | 说明 |
| ------ | ---- |
| `BUY`  | 买入 |
| `SELL` | 卖出 |

## orderType

用于 `/order/place` 请求、`/order/history` 过滤参数，以及每条订单 / 成交响应记录。

| 值       | 说明   |
| -------- | ------ |
| `MARKET` | 市价单 |
| `LIMIT`  | 限价单 |

## timeInForce

用于 `/order/place` 请求；可选，默认 `DAY`。

| 值    | 说明                                                                                                |
| ----- | --------------------------------------------------------------------------------------------------- |
| `DAY` | 当日有效（默认），收盘时自动失效                                                                    |
| `GTC` | 一直有效直至撤销。仅支持 `LIMIT` 订单；分数股 GTC 必须同时设置 `tradingSession = EXTENDED` 或 `24H` |

## tradingSession / session

请求端在 `/order/place` 里叫 `tradingSession`，响应端在订单 / 成交记录里叫 `session`。`LIMIT`
必填；`MARKET` 禁传。

| 值         | 说明                                              |
| ---------- | ------------------------------------------------- |
| `RTH`      | 常规交易时段（09:30–16:00 ET）                    |
| `EXTENDED` | 盘前 + RTH + 盘后（04:00–20:00 ET）               |
| `24H`      | 夜盘 + 盘前 + RTH + 盘后（20:00 → 次日 20:00 ET） |

## walletType

用于 `/order/place` 请求（仅 BUY 方向）；可选，默认 `CARD`。SELL 方向始终使用 `CARD`，忽略传入值。

| 值     | 说明             |
| ------ | ---------------- |
| `CARD` | 资金钱包（默认） |
| `MAIN` | 现货钱包         |

## orderStatus（过滤器）

用于 `/order/history`
的逗号分隔多值过滤参数。仅接受以下终态值；进行中状态（`NEW`、`ACCEPTED`）不是有效过滤输入。

| 值                 | 说明     |
| ------------------ | -------- |
| `FILLED`           | 全部成交 |
| `PARTIALLY_FILLED` | 部分成交 |
| `CANCELED`         | 已撤销   |
| `EXPIRED`          | 已过期   |
| `REJECTED`         | 已拒绝   |

## status（订单 / 成交响应）

每条订单 / 成交记录的生命周期状态，涵盖进行中与终态。

| 值                 | 说明                                   |
| ------------------ | -------------------------------------- |
| `NEW`              | 本地已接受，待上游确认                 |
| `ACCEPTED`         | 上游券商已接受                         |
| `PARTIALLY_FILLED` | 部分成交                               |
| `FILLED`           | 全部成交                               |
| `CANCELED`         | 已撤销                                 |
| `EXPIRED`          | 已过期（`DAY` 订单收盘自动撤销等场景） |
| `REJECTED`         | 已拒绝                                 |

> **注意：** 下单响应（`/order/place`）和撤单响应（`/order/cancel`）中的 `status`
> 字段是独立的请求确认码，不是订单生命周期状态，仅携带 `S`（已接受）或 `F`（失败）。

## tradability（交易规则）

由 `/market/exchangeInfo` → `symbols[].tradability` 返回，表示当前 symbol 允许的交易方向。

| 值         | 说明                        |
| ---------- | --------------------------- |
| `BUY_SELL` | 买卖双向均允许              |
| `BUY`      | 仅允许买入（仅可建新多仓）  |
| `SELL`     | 仅允许卖出（仅可平仓）      |
| `NONE`     | 禁止交易（已停牌 / 已暂停） |

## convertType（代币化）

用于 `/tokenized/convert-status` 请求，以及 `/tokenized/history` 和 `/tokenized/convert-status`
响应中返回。

| 值       | 说明                       |
| -------- | -------------------------- |
| `MINT`   | 从标的股票铸造代币化资产   |
| `REDEEM` | 将代币化资产赎回为标的股票 |

## status（代币化转换响应）

由 `/tokenized/mint`、`/tokenized/redeem`、`/tokenized/convert-status` 以及 `/tokenized/history`
每行返回。此状态码**独立于订单生命周期 `status`**——铸造 / 赎回是异步流程，有自己的三态机。

| 值  | 说明               |
| --- | ------------------ |
| `P` | 处理中（异步进行） |
| `S` | 成功               |
| `F` | 失败               |