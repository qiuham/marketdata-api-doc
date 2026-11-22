---
exchange: bitget
source_url: https://www.bitget.com/docs/uta/error-code/common-error-handling
api_type: Error Code
updated_at: 2026-11-22 19:00:28.757452
---

# Common Error Handling

This page explains common errors, why they occur, and how to resolve them. For the full list of error codes, see [REST API Error Code](./restapi) or [WebSocket Error Code](./websocket).

## WebSocket Errors

<a id="err-30002"></a>
### 30002 — Unrecognized request

The request message format is invalid. Check that the subscription or request payload is valid JSON and matches the expected schema.

<a id="err-30004"></a>
### 30004 — User not logged in / User must be logged in

A subscription message was sent before the login response was received. Always wait for a successful login response before sending subscription messages.

## Authentication Errors

<a id="err-40006"></a>
### 40006 — Invalid ACCESS\_KEY

Check that the `ACCESS-KEY` in your request header is correct.

<a id="err-40008"></a>
### 40008 — Request timestamp expired

The timestamp in your request deviates too far from the server time. Sync your local clock using [Get Server Time](/docs/uta/public/get-server-time).

<a id="err-40009"></a>
### 40009 — sign signature error

Common causes and fixes:

- **Signature algorithm error** → follow the [Signature Guide](/docs/uta/guide/signature)
- **Query string or body was URL-encoded before signing** (breaks when coin names contain non-ASCII characters) → do **not** URL-encode the query string or body before signing

## Rate Limit Errors

<a id="err-429"></a>
### 429 — Too Many Requests

The API rate limit has been exceeded. Reduce your request frequency and comply with the rate limits for each endpoint.

<a id="err-40725"></a>
### 40725 — service return an error

Usually caused by a server deployment. Retry after receiving the error response.

## Order Errors

<a id="err-25003"></a>
### 25003 — Concurrent operation, please retry

In one-way position mode, if the total quantity of all reduce-only orders exceeds the current position size, the system will cancel existing orders before placing new ones. In cancel-then-place scenarios, the new order can arrive before the cancellation is processed by the matching engine. No special action is needed — retry after a short delay.

<a id="err-25102"></a>
### 25102 — Trading pair temporarily closed for maintenance

The trading pair may not yet support UTA orders, may not be launched on v3, or may be under maintenance.

> `25101` = short-term maintenance or not open yet; `25102` = longer maintenance or near-delisting; `40309` = already delisted.

<a id="err-25105"></a>
### 25105 — This contract does not support opening positions

The trading pair does not support opening positions, or it has been delisted. Check whether the unified contract is live or refer to delisting announcements.

<a id="err-25110"></a>
### 25110 — This coin is not supported for deposits into the unified account

This coin cannot be transferred into the unified account. No workaround is available.

<a id="err-25150"></a>
### 25150 — The leverage for this contract cannot exceed \{0\}x

Sub-accounts belonging to a newly registered user are capped at 5x maximum leverage for the first 7 days after registration. The restriction is lifted automatically once the 7-day period ends — no action is required.

<a id="err-25212"></a>
### 25212 — Duplicate clientOid

Idempotency is checked against the current order status: `clientOid` cannot be reused while an order is open; it can be reused after the order is filled or cancelled.

<a id="err-25219"></a>
### 25219 — Exceeds the maximum borrowable amount

The lending pool has insufficient funds, so the requested amount cannot be borrowed. Reduce the borrow amount or try again later once more funds are available in the pool.

<a id="err-25229"></a>
### 25229 — Total positions exceed the current limit of \{0\} positions

The maximum position count of 200 has been reached. Keep position count below 200, or distribute positions across sub-accounts.

<a id="err-25232"></a>
### 25232 — Reduce-only orders will only reduce your position

This occurs when non-reduce-only orders exist and the combined quantity of both order types exceeds the position size, while the non-reduce-only order price is more favorable. Cancel or modify existing non-reduce-only orders before placing a reduce-only order.

<a id="err-25234"></a>
### 25234 — Remaining quantity for regular orders is 0

An IO position limit was triggered. Adjust your order size and retry. [Learn more](https://www.bitget.com/zh-CN/trade-info/oi_limit)

<a id="err-25567"></a>
### 25567 — Exceeded the maximum quantity of contract orders

The order size exceeds the single-order quantity limit. Check `maxMarketOrderQty` (max market order size) and `maxOrderQty` (max limit order size) from the [Get Instruments](/docs/uta/public/get-instruments) endpoint.

<a id="err-25568"></a>
### 25568 — The order does not meet the modification requirements

Preset TP/SL orders and market orders cannot be modified. Do not attempt to modify these order types.

<a id="err-25574"></a>
### 25574 — Reduce-only order protection

When non-reduce-only orders exist, the modified price cannot be more favorable than the existing reduce-only order price. Adjust the modified price so it does not take priority over the reduce-only order.

<a id="err-45110"></a>
### 45110 — Less than the minimum order amount

Order value is below the minimum (5 USDT for futures, 1 USDT for spot). Note that in unified accounts, the backend resets the effective order quantity to match the trading pair's precision — this can silently reduce the order value below the minimum (e.g., SYRUPUSDT with a step of 10: placing 16 × 0.4484 → effective qty 10 × 0.4484 = 4.484 USDT, rejected). Ensure the final effective order value clears the minimum threshold.

<a id="err-45116"></a>
### 45116 — The count of positions held by the account exceeds the maximum count

The maximum position count (200) has been exceeded. Keep positions below 200, or distribute across sub-accounts.

<a id="err-45119"></a>
### 45119 — This symbol does not support position opening operation

The trading pair's `status` has been restricted or the pair has been delisted. Use [Get Instruments](/docs/uta/public/get-instruments) to check the trading pair status, or refer to delisting announcements.

<a id="err-45121"></a>
### 45121 — The reasonable mark price deviates too much from the market

The reasonable mark price has deviated too far from the market price, making the current leveraged position high-risk. See the [Bitget support article](https://www.bitget.com/support/articles/12560603775538) for details.

<a id="err-45001"></a>
### 45001 — Unknown error

Usually caused by a server deployment. Retry after receiving the error response.

<a id="err-40908"></a>
### 40908 — Concurrent operation failed

Occurs when position processing takes longer than usual (accounts with many positions), or when a close order arrives before a prior cancellation is fully processed. Wait for the previous operation to complete before sending a new request.

<a id="err-40710"></a>
### 40710 — Abnormal account status

Account status is abnormal. Contact customer support.

<a id="err-40760"></a>
### 40760 — Unable to place order due to ongoing liquidation

The account is currently being liquidated — trading and transfers are blocked until the process completes. Wait for the liquidation to finish before retrying.

<a id="err-40022"></a>
### 40022 — The business of this account has been restricted

Two common causes:

- **Sub-account trading permission is not enabled** → enable trading permission for the sub-account
- **Account under risk control** → contact customer support to verify the account's risk control status

<a id="err-40715"></a>
### 40715 — Exceeded the maximum open count

The maximum openable quantity has been reached. Use [Get Max Open Available](/docs/uta/trade/get-max-open-available) to check the current limit.

<a id="err-40034"></a>
### 40034 — Parameter does not exist

One or more request parameters are incorrect. Verify all parameters against the API documentation.

<a id="err-40763"></a>
### 40763 — Exceeds position tier limit

The position size exceeds the current position tier limit. See [Position Tier](https://www.bitget.com/futures/introduction/position-tier) for the applicable limits.

<a id="err-40774"></a>
### 40774 — The order type for unilateral position must also be the unilateral position type

Order parameters do not match the current position mode (`tradeSide` / `posSide` mismatch). Use the correct combination for your account's position mode:

| Mode | Action | Parameters |
|---|---|---|
| Hedge | Open long | `side=buy&posSide=long` |
| Hedge | Open short | `side=sell&posSide=short` |
| Hedge | Close long | `side=sell&posSide=long` |
| Hedge | Close short | `side=buy&posSide=short` |
| One-way | Open long | `side=buy` |
| One-way | Open short | `side=sell` |
| One-way | Close long | `side=sell&reduceOnly=yes` |
| One-way | Close short | `side=buy&reduceOnly=yes` |

<a id="err-40815"></a>
### 40815 — The order price is higher than the highest bid price

The buy order price exceeds the current highest bid. Adjust the price downward.

<a id="err-40816"></a>
### 40816 — The order price is lower than the lowest selling price

The sell order price is below the current lowest ask. Adjust the price upward.

<a id="err-40922"></a>
### 40922 — Only work order modifications are allowed

The order cannot be modified because it is fully filled, cancelled, or rejected. Only unfilled or partially-filled orders can be modified.

<a id="err-41117"></a>
### 41117 — Selling price cannot be lower than the limit

The order price is outside the allowed buy/sell spread range (`buyLimitPriceRatio` / `sellLimitPriceRatio`). Check these values from [Get Instruments](/docs/uta/public/get-instruments) and place orders within the allowed range.

<a id="err-43027"></a>
### 43027 — The minimum order value is not met

When placing a buy order, the system uses the lower of the mark price and the order price. If the mark price is below the order price, an order priced at exactly 5 USDT may still be rejected. Avoid placing orders at the exact boundary — leave a small margin above the minimum.

<a id="err-45118"></a>
### 45118 — Reached the upper limit of orders

The pending order count has reached the platform limit. Limits by account type:

- **Futures:** 200 unfilled orders per symbol, 400 per business line (UID-level)
- **Max position count:** 200 per business line (UID-level)
- **Spot margin:** 100 open orders per trading pair per UID, 1,000 total
- **Spot:** 200 open orders per trading pair per UID, 1,000 total

Reduce the number of pending orders to proceed.

<a id="err-22046"></a>
### 22046 — The order price exceeds the minimum price limit

The order price is below the minimum allowed. Adjust the price upward to meet the minimum limit.

<a id="err-22047"></a>
### 22047 — The order price exceeds the maximum price limit

The order price exceeds the maximum allowed. Adjust the price downward to stay within the limit.

<a id="err-22048"></a>
### 22048 — Exceeded personal limit, unable to delegate

The user's borrowable quantity has reached the personal limit. Check the current limit from [Get Max Open Available](/docs/uta/trade/get-max-open-available).

<a id="err-22067"></a>
### 22067 — ADL processing, forbid operate the symbol

The symbol is temporarily blocked due to ADL (Auto-Deleveraging) processing. Wait for the ADL process to complete before retrying.

<a id="err-12001"></a>
### 12001 — \{0\} can be used at most

Insufficient account balance. Top up the account and retry.

<a id="err-13008"></a>
### 13008 — Traders minimum place orderSize is \{0\}

The order size is below the trader's minimum requirement. Increase the order size to meet the minimum.

<a id="err-31008"></a>
### 31008 — No position found for this symbol; cannot place a TP/SL order

When placing a strategy order for take-profit/stop-loss (`type=tpsl`), `marginMode` defaults to cross margin (`crossed`) if not provided. If the actual position on this symbol is isolated margin (`isolated`), the request fails because no matching cross-margin position exists. Pass `marginMode` explicitly to match your actual position type (`crossed` or `isolated`) and retry.

---

# 常见错误码处理方法

本页说明常见错误码的触发场景及处理方式。完整错误码列表请参见 [REST API 错误码](./restapi) 或 [WebSocket 错误码](./websocket)。

## WebSocket 错误

<a id="err-30002"></a>
### 30002 — 不合法的请求

请求报文格式有误。检查订阅/请求报文是否为合法 JSON，且字段结构与文档一致。

<a id="err-30004"></a>
### 30004 — 用户需要登录

订阅报文在登录成功返回之前就已发送。务必等到收到登录成功的响应后，再发送订阅消息。


## 认证错误

<a id="err-40006"></a>
### 40006 — 无效的 ACCESS\_KEY

检查请求头中的`ACCESS-KEY`是否正确。

<a id="err-40008"></a>
### 40008 — 请求时间戳过期

请求中的时间戳与服务器时间偏差过大。调用[获取服务器时间](/zh-CN/docs/catalog/classic-common-public/classic-common#get-server-time)同步本地时钟。

<a id="err-40009"></a>
### 40009 — sign 签名错误

常见原因及处理方式：

- **签名算法错误**→ 参考[签名文档](/zh-CN/docs/classic/rest-api#签名)
- **签名前对 queryString 或 body 做了 URL 编码**（当币对名称含中文时会触发）→ 签名时不要对参数做 URL 编码

## 频率限制错误

<a id="err-429"></a>
### 429 — 请求次数过多

超过接口频率限制。降低请求频率，遵守各接口的频率限制规则。

<a id="err-40725"></a>
### 40725 — 返回无映射信息

通常由服务器发布导致，用户在收到报错响应后重试即可


## 订单错误

<a id="err-25003"></a>
### 25003 — 并发操作，请重试

单向持仓模式下，若全部只减仓单数量超过当前仓位数量时，系统会触发先撤后下，撮合引擎还未处理完撤单，新下单请求已到达。无需特殊操作，系统会阻止重复平仓，稍后重试即可。


<a id="err-25102"></a>
### 25102 — 交易对停止交易维护

该交易对可能尚未支持 UTA 下单、未上线 v3，或正在维护中。

> `25101` = 短期维护或未开放；`25102` = 较长维护期或即将下架；`40309` = 已完成下架。

<a id="err-25105"></a>
### 25105 — 此合约暂不支持开仓操作

该交易对不支持开仓，或已下架。查看统一合约是否上线，或查阅下架公告。

<a id="err-25110"></a>
### 25110 — 该币种不支持转入统一账户

该币种不支持转入统一账户，无法操作。

<a id="err-25150"></a>
### 25150 — 您在该合约上的杠杆不能超过\{0\}x，请调整杠杆

新注册用户的子账户在注册后 7 天内，最大杠杆会被限制为 5 倍；7 天后该限制会自动解除，无需手动操作。

<a id="err-25212"></a>
### 25212 — 重复的 clientOid

重复使用了同一个 `clientOid`。幂等会基于当前委托单的状态进行判断，即订单挂单期间clientOid不允许重复，成交或撤销后clientOid允许重复。

<a id="err-25219"></a>
### 25219 — 超出最大可借金额

借贷池资金不足，无法借出申请的金额。请减少借款金额，或等待借贷池资金充足后重试。

<a id="err-25229"></a>
### 25229 — 总持仓超过了当前持仓条数限制

已达到最大仓位数量（200 条）。将仓位数量控制在 200 条以下，或创建子账户分散仓位。

<a id="err-25232"></a>
### 25232 — 只减仓只会减少您的仓位

当存在非只减仓单，且两类委托数量之和超过仓位数量，同时非减仓单价格更优时会触发此错误。撤销或修改已有的非只减仓单后再下只减仓单。

<a id="err-25234"></a>
### 25234 — 普通下单剩余数量为 0

触发了 IO 限仓。调整下单仓位后重试。[查看详情](https://www.bitget.com/zh-CN/trade-info/oi_limit)


<a id="err-25567"></a>
### 25567 — 超过最大下单合约数量

下单数量超过单笔下单量限制。参考[获取交易产品信息](/zh-CN/docs/catalog/market/market-data#get-instruments)中的 `maxMarketOrderQty`（市价单上限）和 `maxOrderQty`（限价单上限）。

<a id="err-25568"></a>
### 25568 — 订单不符合改单要求

预设止盈止损订单和市价单不允许修改，不要对这两类订单执行改单操作。

<a id="err-25574"></a>
### 25574 — 为保障现有只减仓订单，改单失败

存在同向的非只减仓单时，修改后的价格不允许比只减仓单的价格更优先成交。调整修改后的价格，使其不超过只减仓单的价格优先级。

<a id="err-45110"></a>
### 45110 — 触发最小下单价值限制

下单价值低于最低限额（合约 5 USDT，现货 1 USDT）。注意统一账户中，后端会按交易对精度重设有效数量，可能静默压低实际价值（例如 SYRUPUSDT 步长为 10，下单 16 × 0.4484 → 有效数量 10 × 0.4484 = 4.484 USDT，会被拦截）。确保最终有效下单价值高于最低限额。

<a id="err-45116"></a>
### 45116 — 当前账号持仓条数超过最大数量

已达到最大仓位数量（200 条）。将仓位数量控制在 200 条以下，或创建子账户分散仓位。

<a id="err-45119"></a>
### 45119 — 此合约暂不支持开仓操作

交易对 `status` 已被限制或已下架。调用[获取交易产品信息](/zh-CN/docs/catalog/market/market-data#get-instruments)查看状态，或参考下架公告。

<a id="err-45121"></a>
### 45121 — 合理标记价格偏离盘口过大，当前杠杆开仓风险较高

合理标记价格偏离市场价格过大，当前杠杆开仓风险较高。详见 [Bitget 支持文章](https://www.bitget.com/zh-CN/support/articles/12560603775538)。

<a id="err-45001"></a>
### 45001 — 未知错误

通常由服务器发布导致，用户在收到报错响应后重试即可

<a id="err-40908"></a>
### 40908 — 并发操作失败

仓位较多时处理耗时超过平均水平，或先撤后挂场景下平仓单在撤单处理完成前到达。需等待上一笔操作完成后再发起新请求。

<a id="err-40710"></a>
### 40710 — 账户状态异常

账户状态异常，联系客服处理。

<a id="err-40760"></a>
### 40760 — 账户处于强平状态，无法下单

账户正在强平中，强平期间禁止交易和划转。等待强平处理完成后再操作。

<a id="err-40022"></a>
### 40022 — 此账号该业务已被限制

两种常见原因：

- **子账户交易权限未开启** → 开启子账户交易权限
- **账户被风控限制** → 联系客服核实账户风控状态

<a id="err-40715"></a>
### 40715 — 委托数量大于最大可开数量

已达到最大可开数量。调用[获取最大可开可用](/zh-CN/docs/catalog/trading/position-management#get-max-open-available)查询当前限额。

<a id="err-40034"></a>
### 40034 — 参数不存在

请求参数有误。对照 API 文档逐一核查入参。

<a id="err-40763"></a>
### 40763 — 委托数量不能超过对应档位的最大量

仓位超过当前档位限制。参考[仓位档位规则](https://www.bitget.com/zh-CN/trade-info/position-gear?symbolId=BTCUSDT_UMCBL)，调整仓位后重试。

<a id="err-40774"></a>
### 40774 — 单边持仓时委托类型也必须是单边持仓类型

下单参数与当前持仓模式不匹配（`tradeSide` / `posSide` 错误）。按当前模式使用正确参数组合：

| 模式 | 操作 | 参数 |
|---|---|---|
| 双向持仓 | 开多 | `side=buy&posSide=long` |
| 双向持仓 | 开空 | `side=sell&posSide=short` |
| 双向持仓 | 平多 | `side=sell&posSide=long` |
| 双向持仓 | 平空 | `side=buy&posSide=short` |
| 单向持仓 | 开多 | `side=buy` |
| 单向持仓 | 开空 | `side=sell` |
| 单向持仓 | 平多 | `side=sell&reduceOnly=yes` |
| 单向持仓 | 平空 | `side=buy&reduceOnly=yes` |


<a id="err-40815"></a>
### 40815 — 委托价格高于最高买价

买单价格超过当前最高买入价。下调委托价格后重试。

<a id="err-40816"></a>
### 40816 — 委托价格低于最低卖价

卖单价格低于当前最低卖出价。上调委托价格后重试。

<a id="err-40922"></a>
### 40922 — 只允许修改未成交的限价单

订单已完全成交、撤销或被拒绝，无法修改。只能对未成交或部分成交（有剩余数量）的订单进行改单。

<a id="err-41117"></a>
### 41117 — 卖出价格不能低于限制价格

价格超出了交易对允许的买卖价差范围（`buyLimitPriceRatio` / `sellLimitPriceRatio`）。参考[获取交易对信息](/zh-CN/docs/catalog/market/market-data#get-instruments)中的对应字段值，在允许范围内下单。

<a id="err-43027"></a>
### 43027 — 不满足最小下单价值

买单时系统取标记价格与委托价格的较小值计算实际价值，若标记价格低于委托价格，即使委托价格恰好为 5 USDT 也可能被拦截。不要使用边界值下单，留出一定余量。

<a id="err-45118"></a>
### 45118 — 达到委托总笔数上限

当前挂单数量已达到平台限制。各账户类型限制如下：

- **合约：** 每个交易对最多 200 笔未成交委托，每条业务线最多 400 笔（基于 UID 限制）
- **最大仓位条数：** 每条业务线 200 条（基于 UID 限制）
- **现货杠杆：** 每个交易对/UID 最多 100 笔，总计最多 1,000 笔
- **现货：** 每个交易对/UID 最多 200 笔，总计最多 1,000 笔

减少挂单数量后重试。

<a id="err-22046"></a>
### 22046 — 下单价格超过最小价格限制

订单价格低于最小价格限制。上调价格至高于最小限制后重试。

<a id="err-22047"></a>
### 22047 — 下单价格超过最大价格限制

订单价格超出最大价格限制。下调价格至最大限制范围内后重试。

<a id="err-22048"></a>
### 22048 — 超过个人限额，无法委托

可借币数量已达到个人限额。调用[获取最大可开可用](/zh-CN/docs/catalog/trading/position-management#get-max-open-available)查询当前最大可开。

<a id="err-22067"></a>
### 22067 — ADL 处理中，禁止操作该币对

该币对正在进行 ADL（自动减仓）处理，期间禁止操作。等待 ADL 处理完成后再重试。

<a id="err-12001"></a>
### 12001 — 当前最多可使用 \{0\}

账户余额不足。充值后重试。

<a id="err-13008"></a>
### 13008 — 交易员最小交易量为 \{0\}

下单数量低于交易员最小下单量要求。增加下单数量至满足最小要求后重试。

<a id="err-31008"></a>
### 31008 — 该仓位暂无持仓，不能进行止盈止损委托

创建策略单下止盈止损（`type=tpsl`）时，`marginMode` 未传则默认按全仓（`crossed`）处理；若该交易对实际持有的是逐仓（`isolated`）仓位，就会因为找不到匹配的全仓仓位而报此错误。下单时显式传入与实际仓位一致的 `marginMode`（`crossed` 或 `isolated`）后重试。