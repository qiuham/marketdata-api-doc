---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/stock-options/common-definition
api_type: Guide
updated_at: 2026-11-28 18:28:36.327213
---

# Common Definition

This page lists the contract conventions and enum values used by Stock Option Trading endpoints.

**Global rule:** REST enum string values are **UPPERCASE** on both request and response, except the
settlement event `status`, which is always `Completed`. `eventType` filter values are
case-insensitive. The user data stream uses lowercase values (see
[WebSocket Streams General Info](./websocket-streams-general-info.md)).

## Contract Symbol

`symbol` is always the OCC option contract symbol, formatted as
`{root}{yymmdd}{C|P}{strike × 1000, zero-padded to 8 digits}`. For example, `NVDA260930C00100000` is
an NVDA call expiring on 2026-09-30 with a strike of 100.

**Do not parse the OCC symbol to derive the underlying.** After a corporate action, the root of an
adjusted contract carries a suffix (`GOOG1` is not `GOOG`), so parsing would return the wrong stock.
Read `underlyingSymbol`, `expirationDate`, `contractType`, `strikePrice` and `multiplier` from the
response instead.

## Contract Discovery

Browse contracts of an underlying in two steps:

1. `GET /market/expirations` — list the expiration dates of the underlying.
2. `GET /market/contracts` — list all calls and puts of the underlying for one expiration date.

The `expirationDate` returned by step 1 can be passed **as-is** to step 2 (both use `YYYY-MM-DD`).
The returned `symbol` can then be used for order placement and Option Exchange Info.

When standard and corporate-action-adjusted contracts share an expiration date, step 1 returns
**multiple** rows with the same `expirationDate` and different `rootSymbol`. To list the adjusted
set, pass that `rootSymbol` to step 2; without it, only standard contracts are returned.

## status

Contract trading status, returned by Option Contracts and Option Exchange Info. The values match the
ones used by server-side order validation.

| Value        | Description                                   | Allowed `positionIntent`                                          |
| ------------ | --------------------------------------------- | ----------------------------------------------------------------- |
| `OPEN_CLOSE` | Opening and closing allowed                   | `BUY_TO_OPEN` / `SELL_TO_CLOSE` / `SELL_TO_OPEN` / `BUY_TO_CLOSE` |
| `CLOSE_ONLY` | Only reducing or closing existing positions   | `SELL_TO_CLOSE` / `BUY_TO_CLOSE`                                  |
| `NONE`       | No new orders allowed (delisted or suspended) | None                                                              |

- `status` is a **snapshot at query time**. The server-side validation at order placement is final.
- **Known deviation**: `status` does not take the expiration-day time window into account. After the
  close on the expiration day, and during roughly the last 45 minutes before that close, `status`
  may still be `OPEN_CLOSE` while the order is rejected. The deviation is always on the optimistic
  side: a contract shown as not tradable is never actually tradable.
- `status` reflects the **contract** only. Account-level restrictions (insufficient options level,
  restricted account, etc.) are returned as order error codes.
- `status` applies to orders, not to exercise. Use Exercisable Options to check whether an exercise
  can be submitted.
- Mapping to order errors: with `status` = `NONE`, orders return `497426` or `497425`; with `status`
  = `CLOSE_ONLY`, opening orders return `497427`; with `status` = `OPEN_CLOSE`, opening orders in
  roughly the last 45 minutes of the expiration day still return `497423`; for a contract with any
  `status`, orders placed after the close on the expiration day return `497425`.

## positionIntent

| Value           | Description                                    | Position side |
| --------------- | ---------------------------------------------- | ------------- |
| `BUY_TO_OPEN`   | Buy to open                                    | Long          |
| `SELL_TO_CLOSE` | Sell to close                                  | Long          |
| `SELL_TO_OPEN`  | Sell to open (covered call / cash-secured put) | Short         |
| `BUY_TO_CLOSE`  | Buy to close                                   | Short         |

- **`positionIntent` may be omitted**; the server derives it from `side`: `BUY` → `BUY_TO_OPEN`,
  `SELL` → `SELL_TO_CLOSE`. The order is rejected (parameter error) if it is omitted when:
  - `side` = `BUY` and the account holds a **short** position in the contract (it may be meant as
    `BUY_TO_CLOSE`);
  - `side` = `SELL` and the account holds **no long** position in the contract (it can only be
    `SELL_TO_OPEN`).
- Therefore **always pass the short side (`SELL_TO_OPEN` / `BUY_TO_CLOSE`) explicitly.** An explicit
  value must match `side` (`BUY_*` with `BUY`, `SELL_*` with `SELL`); otherwise the order is
  rejected.

## side

| Value  | Description |
| ------ | ----------- |
| `BUY`  | Buy         |
| `SELL` | Sell        |

## timeInForce

| Value | Description                                                     |
| ----- | --------------------------------------------------------------- |
| `DAY` | Good until the end of the trading day. The only value supported |

## walletType

Used on Place Option Order. Optional; defaults to `CARD`.

| Value  | Description              |
| ------ | ------------------------ |
| `CARD` | Funding wallet (default) |
| `MAIN` | Spot wallet              |

## Position side

Returned as `side` by Option Positions.

| Value   | Description    |
| ------- | -------------- |
| `LONG`  | Long position  |
| `SHORT` | Short position |

## Exercise status

| Value        | Description            |
| ------------ | ---------------------- |
| `PROCESSING` | Submitted, in progress |
| `SUCCESS`    | Exercise completed     |
| `FAILED`     | Exercise failed        |

## eventType

Used by the settlement event endpoints.

| Value        | Description                       |
| ------------ | --------------------------------- |
| `EXERCISE`   | Exercise of a long position       |
| `ASSIGNMENT` | Assignment of a short position    |
| `EXPIRY`     | Contract expired without exercise |

## settlementKind

| Value      | Description            |
| ---------- | ---------------------- |
| `PHYSICAL` | Physical delivery      |
| `CASH`     | Cash settlement        |
| `MIXED`    | Both physical and cash |

## cashDirection

| Value    | Description   |
| -------- | ------------- |
| `DEBIT`  | Cash debited  |
| `CREDIT` | Cash credited |

## Deliverable type

In Option Exchange Info and Exercisable Options, `deliverables[].type` is:

| Value    | Description                                                 |
| -------- | ----------------------------------------------------------- |
| `EQUITY` | Shares; `symbol` is the ticker, `amount` is the share count |
| `CASH`   | Cash; `symbol` is the currency, `amount` is the cash amount |

In the settlement event endpoints, the share leg of `deliverables` has no `type`, and the cash leg
has one of:

| Value   | Description     |
| ------- | --------------- |
| `OPEXC` | Exercise cash   |
| `OPASN` | Assignment cash |
| `OPCSH` | Cash settlement |

---

# 通用枚举定义

本页列出股票期权交易接口使用的合约约定与枚举取值。

**全局规则：** REST 接口的枚举字符串在请求与响应中一律为**大写**（结算事件的 `status` 例外，恒为
`Completed`；`eventType` 过滤值大小写不敏感）。用户数据流使用小写取值（见
[WebSocket 流基本信息](./websocket-streams-general-info.md)）。

## 合约代码

`symbol` 一律是 OCC 合约代码，格式为 `{root}{yymmdd}{C|P}{strike × 1000 补零至 8 位}`。例如
`NVDA260930C00100000` 表示 NVDA、2026-09-30 到期、看涨、行权价 100。

**不要自行解析 OCC 字符串反推标的。** 公司行动调整后的合约 root 会带序号（`GOOG1` 不等于
`GOOG`），自行解析会拿到错的正股。请直接读响应里的
`underlyingSymbol`、`expirationDate`、`contractType`、`strikePrice`、`multiplier`。

## 合约发现

按标的浏览合约分两步：

1. `GET /market/expirations` —— 按标的拿到期日列表。
2. `GET /market/contracts` —— 按标的 + 到期日拿该到期日下的全部合约（Call + Put）。

第 1 步返回的 `expirationDate` 可**原样**作为第 2 步的入参（两边都是 `YYYY-MM-DD`）。拿到 `symbol`
后即可用于下单与「合约交易规则」。

同一到期日下若同时存在标准合约与公司行动调整后的合约，第 1 步会返回**多条**记录，`expirationDate`
相同、`rootSymbol` 不同。要查调整后的那一组，需把对应的 `rootSymbol`
传给第 2 步；不传则只返回标准合约。

## status

合约交易状态，由「合约列表」与「合约交易规则」返回，取值与服务端下单校验使用的枚举一致。

| 取值         | 含义                                | 允许的 `positionIntent`                                           |
| ------------ | ----------------------------------- | ----------------------------------------------------------------- |
| `OPEN_CLOSE` | 允许开仓和平仓                      | `BUY_TO_OPEN` / `SELL_TO_CLOSE` / `SELL_TO_OPEN` / `BUY_TO_CLOSE` |
| `CLOSE_ONLY` | 只允许减少或关闭已有持仓            | `SELL_TO_CLOSE` / `BUY_TO_CLOSE`                                  |
| `NONE`       | 不允许创建新订单（下架 / 暂停交易） | 无                                                                |

- `status` 是**查询时刻的快照**，最终以下单时服务端的校验结果为准。
- **已知偏差**：`status`
  不含到期日时间窗口的判定。在到期日收盘之后、以及到期日收盘前最后约 45 分钟，`status` 可能仍返回
  `OPEN_CLOSE`，而实际下单会被拒。偏差方向恒为偏乐观，不会出现显示不可交易但实际可交易的情况。
- `status`
  只表示**合约维度**的状态，不包含账户维度的限制（期权等级不足、账户受限等），这类限制通过下单错误码返回。
- `status` 只约束下单，不约束行权。行权是否可提交，以「可行权合约」为准。
- 与下单错误码的对应：`status` = `NONE` 时下单返回 `497426` 或 `497425`；`status` = `CLOSE_ONLY`
  时开仓返回 `497427`；`status` = `OPEN_CLOSE` 的合约在到期日最后约 45 分钟内开仓仍会返回
  `497423`；任何 `status` 的合约在到期日收盘后下单均返回 `497425`。

## positionIntent

| 取值            | 含义                                        | 持仓方向 |
| --------------- | ------------------------------------------- | -------- |
| `BUY_TO_OPEN`   | 买入开仓                                    | 多头     |
| `SELL_TO_CLOSE` | 卖出平仓                                    | 多头     |
| `SELL_TO_OPEN`  | 卖出开仓（covered call / cash-secured put） | 空头     |
| `BUY_TO_CLOSE`  | 买入平仓                                    | 空头     |

- **`positionIntent` 可以不传**，此时服务端按 `side` 推导：`BUY` → `BUY_TO_OPEN`，`SELL` →
  `SELL_TO_CLOSE`。以下两种情况不传会被拒单（参数错误）：
  - `BUY`，且该合约当前持有**空头**（可能是要买入平仓 `BUY_TO_CLOSE`）；
  - `SELL`，且该合约当前**没有多头**（只可能是卖出开仓 `SELL_TO_OPEN`）。
- 因此**空头侧（`SELL_TO_OPEN` / `BUY_TO_CLOSE`）请始终显式传**。显式传入时必须与 `side`
  同向（`BUY_*` 配 `BUY`，`SELL_*` 配 `SELL`），否则拒单。

## side

| 取值   | 含义 |
| ------ | ---- |
| `BUY`  | 买入 |
| `SELL` | 卖出 |

## timeInForce

| 取值  | 含义                       |
| ----- | -------------------------- |
| `DAY` | 当日有效，也是唯一支持的值 |

## walletType

用于「下单」，可选，默认 `CARD`。

| 取值   | 含义             |
| ------ | ---------------- |
| `CARD` | 资金账户（默认） |
| `MAIN` | 现货账户         |

## 持仓方向

「持仓查询」返回的 `side`。

| 取值    | 含义 |
| ------- | ---- |
| `LONG`  | 多头 |
| `SHORT` | 空头 |

## 行权状态

| 取值         | 含义           |
| ------------ | -------------- |
| `PROCESSING` | 已提交，处理中 |
| `SUCCESS`    | 行权完成       |
| `FAILED`     | 行权失败       |

## eventType

用于结算事件相关接口。

| 取值         | 含义         |
| ------------ | ------------ |
| `EXERCISE`   | 多头行权     |
| `ASSIGNMENT` | 空头被指派   |
| `EXPIRY`     | 合约到期作废 |

## settlementKind

| 取值       | 含义     |
| ---------- | -------- |
| `PHYSICAL` | 实物交割 |
| `CASH`     | 现金结算 |
| `MIXED`    | 两者兼有 |

## cashDirection

| 取值     | 含义 |
| -------- | ---- |
| `DEBIT`  | 扣款 |
| `CREDIT` | 入账 |

## 交割物类型

「合约交易规则」与「可行权合约」中 `deliverables[].type` 的取值：

| 取值     | 含义                                      |
| -------- | ----------------------------------------- |
| `EQUITY` | 正股，`symbol` 为 ticker，`amount` 为股数 |
| `CASH`   | 现金，`symbol` 为币种，`amount` 为金额    |

结算事件相关接口中，`deliverables` 的正股腿不带 `type`，现金腿的 `type` 取值为：

| 取值    | 含义       |
| ------- | ---------- |
| `OPEXC` | 行权现金   |
| `OPASN` | 被指派现金 |
| `OPCSH` | 现金结算   |