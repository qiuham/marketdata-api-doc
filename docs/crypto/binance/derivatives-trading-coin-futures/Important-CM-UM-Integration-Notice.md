---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/derivatives-trading-coin-futures/Important-CM-UM-Integration-Notice
api_type: REST
updated_at: 2026-11-13 20:27:44.621037
---

# Important Notice — COIN-M / USDⓈ-M Architecture Integration

## Background

COIN-M Futures (CM / DAPI) is being integrated into the unified architecture shared with USDⓈ-M Futures (UM / FAPI). After the migration, several COIN-M REST endpoints, WebSocket streams, and account-level behaviors are aligned with the existing USDⓈ-M conventions. This page summarizes every user-facing change so you can adjust client logic accordingly.

> **Document published:** 2026-06-10 **Effective date:** Progressively rolled out since 2026-06-24, fully effective by 2026-06-30

> **Note:** The changes described in this document will be rolled out progressively — not all changes will take effect simultaneously. Individual changes may be enabled at different times after the initial effective date.

* * *

## A. Account-level changes

### A.1 `dualSidePosition` is unified across UM and CM

  * After the migration, UM and CM share the **same** `dualSidePosition` setting.
  * Calling `POST /fapi/v1/positionSide/dual` or `POST /dapi/v1/positionSide/dual` will flip the value for **both** UM and CM at once.
  * If either side has any open order or open position, switching is rejected with:
    * `-4067` — _"Position side cannot be changed if there exists open orders."_
    * `-4068` — _"Position side cannot be changed if there exists position."_
  * **Action required:** before flipping `dualSidePosition`, ensure both UM and CM have no open orders and no open positions.



### A.2 STP setting follows UM

  * Self-Trade Prevention configuration is taken from the UM side. The CM-side standalone STP setting is no longer effective.



### A.3 UM and CM share the same rate-limit pools

  * **IP request weight (2400 / min)** : UM and CM share a single 2400 weight budget per IP per minute. Requests on either `fapi` or `dapi` count against the same `X-MBX-USED-WEIGHT-1M` counter.
  * **Account order rate limit** : UM and CM share a single order budget — **1200 / minute** (`X-MBX-ORDER-COUNT-1M`) and **300 / 10 seconds** (`X-MBX-ORDER-COUNT-10S`). Order placements on either `fapi` or `dapi` consume from the same counters.
  * Plan client traffic accordingly: previously isolated weight / order quotas across UM and CM are now merged into one.



* * *

## B. Maintenance window behavior (during the cutover only)

During the maintenance window:

  * **UM`dualSidePosition` cannot be changed.** Requests to `POST /fapi/v1/positionSide/dual` or `POST /dapi/v1/positionSide/dual` return error `-1016`.
  * **CM`lastPrice` is frozen** (unchanged). `indexPrice` and `markPrice` continue to update.
  * **Strategy products (Arbitrage / Grid)** on CM are paused:
    * Cannot create new CM Arbitrage bots; existing CM Arbitrage bots cannot reduce size.
    * All CM Grid actions are blocked: create / add margin / withdraw margin / close / cancel.
    * For CM Grid configured with `markPrice` trigger, even if `markPrice` crosses the trigger price during the window the grid will **not** fire — it will trigger after the window ends if the threshold is still crossed.
  * **Portfolio Margin (PM)** during the window:
    * **When a PM account triggers liquidation during the window:**
      * If the user has **no** CM balance/position, liquidation is processed normally.
      * If the user **has** CM balance/position, the UM positions will be settled and assets may be processed, while the CM portion is **liquidated after the window ends**. As a result, single-leg liquidation may occur (in particular, an arbitrage position may be left with one leg liquidated) — the resulting risk is borne by the user.
    * PM **account opening / closing / auto-exchange / close-position** are paused during the window.
  * **Error codes returned during the window** may include any of:
    * `{"code":-1016,"msg":"This service is no longer available."}`
    * `{"code":-1016,"msg":"Service is under maintenance."}`
    * `{"239999": "The system is under maintenance, please try again later."}`
    * `{"code":-1109,"msg":"Invalid account."}`



* * *

## C. REST API changes

### C.1 `avgPrice` / `cumQuote` / `cumBase` removed from order placement responses

The immediate response of order placement / modification / cancellation no longer carries `avgPrice` and the cumulative quote/base value. These fields were always `0` in the placement ack (fills happen asynchronously); the actual fill price is still available via the order query / userTrades endpoints.

**Affected (CM / DAPI —`cumBase` removed):**

  * `POST /dapi/v1/order`
  * `POST /dapi/v1/batchOrders`
  * `PUT /dapi/v1/order`
  * `PUT /dapi/v1/batchOrders`
  * `DELETE /dapi/v1/order`
  * `DELETE /dapi/v1/batchOrders`



**Affected (UM / FAPI —`cumQuote` removed):**

  * `POST /fapi/v1/order`
  * `POST /fapi/v1/batchOrders`
  * `PUT /fapi/v1/order`
  * `PUT /fapi/v1/batchOrders`
  * `DELETE /fapi/v1/order`
  * `DELETE /fapi/v1/batchOrders`



> Read endpoints (`GET /fapi/v1/order`, `/allOrders`, `/userTrades`, etc.) are **not** affected — they still return `avgPrice` and `cumQuote` / `cumBase`.

### C.2 `PUT /dapi/v1/order` and `PUT /dapi/v1/batchOrders` — `price` and `quantity` are both required

After the migration, these PUT endpoints require **both** `price` **and** `quantity`. Sending only one returns `-1102`. For batch, missing field on any element yields element-level `-1102`.

### C.3 The following endpoints can now accept both UM and CM symbols

  * `GET /fapi/v1/klines`
  * `GET /fapi/v1/continuousKlines`
  * `GET /fapi/v1/indexPriceKlines`
  * `GET /fapi/v1/markPriceKlines`
  * `GET /fapi/v1/premiumIndexKlines`
  * `GET /dapi/v1/klines`
  * `GET /dapi/v1/continuousKlines`
  * `GET /dapi/v1/indexPriceKlines`
  * `GET /dapi/v1/markPriceKlines`
  * `GET /dapi/v1/premiumIndexKlines`



### C.4 `GET /fapi/v1/assetIndex` renamed to _Asset Index_ and now includes CM settlement-asset price index

  * The display name is changed from _Multi-Assets Mode Asset Index_ to **Asset Index**.
  * The HTTP path `/fapi/v1/assetIndex` is **unchanged** ; no client code change is required for the call itself.
  * The response now additionally includes COIN-M settlement-asset price index entries — e.g. `BTCUSD`, `ETHUSD`, `BNBUSD`, `SOLUSD`. Existing UM-side entries remain.



### C.5 New CM Algo Order endpoints

COIN-M now exposes the same algo-order surface as UM:

  * `POST /dapi/v1/algoOrder` — place a CONDITIONAL algo (STOP / TAKE_PROFIT / STOP_MARKET / TAKE_PROFIT_MARKET / TRAILING_STOP_MARKET)
  * `GET /dapi/v1/openAlgoOrders` — list open algo orders
  * `DELETE /dapi/v1/algoOrder` — cancel an algo order (by `algoId` or `clientAlgoId`)



### C.6 Plain `place` order endpoints no longer accept stop-type orders

After a delayed effective period following the migration (the exact effective time will be announced separately), the following endpoints will reject stop-type `type` values (`STOP_MARKET` / `TAKE_PROFIT_MARKET` / `STOP` / `TAKE_PROFIT` / `TRAILING_STOP_MARKET`) with:
    
    
    Code
    
    {
      "code": -4120,
      "msg": "Order type not supported for this endpoint. Please use the Algo Order API endpoints instead."
    }

**Affected:**

  * `POST /dapi/v1/order` (single)
  * `POST /dapi/v1/batchOrders` (per element)
  * WebSocket API: `order.place` on the COIN-M ws-dapi endpoint



**Action required:** route stop-type orders through the new `/dapi/v1/algoOrder` endpoint described in C.5.

### C.7 DAPI error code changes

Endpoint| Scenario| Before| After  
---|---|---|---  
`GET /dapi/v1/openOrders`| Invalid `symbol`| `200` (silently)| `-1121`  
  
### C.8 DAPI request weight changes

Endpoint| Before| After  
---|---|---  
`GET /dapi/v2/leverageBracket`| `1` (flat)| `1` with `symbol` / `2` without `symbol`  
`GET /dapi/v1/allOrders`| `20` / `40`| `5` (flat)  
`GET /dapi/v1/userTrades`| `20` / `40`| `5` (flat)  
`GET /dapi/v1/forceOrders`| `20` (flat)| `20` with `symbol` / `50` without `symbol`  
  
* * *

## D. WebSocket changes

### D.1 WebSocket API — `order.place` / `order.modify` / `order.cancel` immediate response no longer returns `avgPrice` / `cumQuote` (UM) / `cumBase` (CM)

Same rationale as C.1 — the immediate response is a placement acknowledgement, fills are asynchronous.

### D.2 WebSocket API — `order.modify` requires both `price` and `quantity`

Sending only one returns `-1102`.

### D.3 `!assetIndex@arr` stream renamed to _Asset Index_ and additionally pushes COIN-M settlement-asset price index

  * Display name changed from _Multi-Assets Mode Asset Index_ to **Asset Index**.
  * Stream key (`!assetIndex@arr`) is **unchanged** on the wire; existing subscriptions continue to work without code changes.
  * The stream now additionally pushes COIN-M settlement-asset entries (e.g., `BTCUSD`, `ETHUSD`, `BNBUSD`, `SOLUSD`).



### D.4 Streams that gain a new `st` field on each payload

`st` distinguishes the symbol type: `1` = UM, `2` = CM.

  * `!miniTicker@arr`
  * `!ticker@arr`
  * `!bookTicker`
  * `!forceOrder@arr`
  * `!contractInfo`
  * `<symbol>@depth<levels>` (incl. `@500ms` / `@100ms`)
  * `<symbol>@aggTrade`
  * `<symbol>@ticker`
  * `<symbol>@bookTicker`
  * `<symbol>@miniTicker`
  * `<symbol>@rpiDepth`



For the all-market arrays (`!*@arr`, `!bookTicker`, `!contractInfo`), both `fstream` and `dstream` deliver the same merged UM + CM content.

### D.5 UM-side single-symbol streams add a `ps` (pair symbol) field, aligning with the CM payload shape

Affected:

  * `!miniTicker@arr`
  * `<symbol>@miniTicker`
  * `!ticker@arr`
  * `!forceOrder@arr`
  * `<symbol>@depth<levels>` (incl. `@500ms` / `@100ms`)
  * `!bookTicker`
  * `<symbol>@bookTicker`
  * `<symbol>@rpiDepth@500ms`



### D.6 markPrice / kline stream family — cross-host subscription

Both `fstream` and `dstream` may subscribe to the streams below.

**markPrice streams** — payload gains a new `st` field (`1` = UM, `2` = CM):

  * `<symbol>@markPrice`, `<symbol>@markPrice@1s`
  * `<pair>@markPrice`, `<pair>@markPrice@1s`
  * `!markPrice@arr`, `!markPrice@arr@1s`



> CM-side `!markPrice@arr` / `!markPrice@arr@1s` standalone doc pages will be added in a future release.

**UM-side kline streams** — cross-host subscription enabled:

  * `<symbol>@kline_<interval>`
  * `<pair>_<contractType>@continuousKline_<interval>`



**CM-side kline streams** — cross-host subscription enabled:

  * `<symbol>@kline_<interval>`
  * `<pair>_<contractType>@continuousKline_<interval>`
  * `<pair>@indexPriceKline_<interval>`
  * `<symbol>@markPriceKline_<interval>`



* * *

## Action Required

  1. **Account-level**

     * Verify your `dualSidePosition` setting after the migration; flip on either side affects both.
     * Make sure both UM and CM are clean (no open orders, no open positions) before changing `dualSidePosition`.
  2. **REST**

     * Adjust client code that reads `avgPrice` / `cumQuote` / `cumBase` from order placement / modify / cancel responses — fetch fill data via `GET /{f,d}api/v1/order` or `userTrades` instead.
     * When calling `PUT /dapi/v1/order` or `PUT /dapi/v1/batchOrders`, always supply both `price` and `quantity`.
     * Update DAPI error handling — `GET /dapi/v1/openOrders` with an invalid `symbol` now returns `-1121` (was a silent `200`).
     * Migrate stop-type orders on COIN-M from `POST /dapi/v1/order` / `batchOrders` / `ws-dapi order.place` to the new `/dapi/v1/algoOrder` endpoint.
  3. **WebSocket**

     * On streams listed in D.4 / D.5 / D.6, expect new fields `st` and/or `ps` in the payload. Add tolerance for these new fields in your parser.
     * Plan for the merged universe on `!ticker@arr` / `!miniTicker@arr` / `!bookTicker` / `!forceOrder@arr` / `!contractInfo` — both UM and CM symbols will be received.
  4. **Maintenance window**

     * Pause CM strategy / PM operations during the announced window. Expect `-1016` / `239999` / `-1109` errors during the window.



Was this page helpful?

Last modified on November 12, 2026

[Change Log](/en/docs/products/derivatives-trading-coin-futures/change-log)[General Info](/en/docs/products/derivatives-trading-coin-futures/general-info)

---

# 币本位 / U本位 架构整合迁移公告（重要变更）

## 变更背景

币本位合约 (CM / DAPI) 正在迁移到与 U本位合约 (UM / FAPI) 共享的统一架构。迁移完成后,部分 CM REST 接口、WebSocket Stream 与账户级行为将与 UM 已有规则对齐。本页面汇总所有面向用户的改动,请相应调整客户端逻辑。

> **文档发布日期:** 2026-06-10 **生效日期:** 自 2026-06-24 起逐步上线，2026-06-30 前全部生效

> **注意:** 本文档所述变更将分阶段逐步上线,并非所有变更都会同时生效。各项变更可能在初始生效日期之后的不同时间启用。

* * *

## 一、账户层变更

### 1\. `dualSidePosition` 在 UM 与 CM 之间打通

  * 迁移完成后,UM 与 CM 共用**同一个** `dualSidePosition` 设置。
  * 调用 `POST /fapi/v1/positionSide/dual` 或 `POST /dapi/v1/positionSide/dual` 都会**同时翻转 UM 和 CM** 的设置。
  * 任意一侧存在 open order 或 open position 时,切换会被拒绝:
    * `-4067` — _"Position side cannot be changed if there exists open orders."_
    * `-4068` — _"Position side cannot be changed if there exists position."_
  * **行动项:** 切换 `dualSidePosition` 之前,请确保 UM 和 CM 都没有挂单也没有持仓。



### 2\. STP 设置以 UM 为准

  * 自成交防止 (STP) 设置以 UM 侧为准。CM 侧的独立 STP 设置不再生效。



### 3\. UM 与 CM 共用同一套 rate-limit 池

  * **IP 请求权重(2400 / 分钟)** : UM 与 CM 共用同一个 2400 权重池(每分钟,每 IP)。`fapi` 与 `dapi` 上的请求都计入同一个 `X-MBX-USED-WEIGHT-1M` 预算。
  * **账户下单频率限制** : UM 与 CM 共用同一套下单预算 — **1200 / 分钟**(`X-MBX-ORDER-COUNT-1M`)与 **300 / 10 秒**(`X-MBX-ORDER-COUNT-10S`)。`fapi` 或 `dapi` 上的下单请求都计入同一个计数器。
  * 请相应调整客户端流量预算:此前 UM 与 CM 分别独立的权重 / 下单额度现在已合并为一个。



* * *

## 二、停机维护期间的行为(仅迁移当天生效)

停机维护期间:

  * **UM`dualSidePosition` 无法修改。** `POST /fapi/v1/positionSide/dual` 或 `POST /dapi/v1/positionSide/dual` 都会返回 `-1016`。
  * **CM`lastPrice` 冻结**(不变化),`indexPrice` 与 `markPrice` 仍持续更新。
  * **CM 策略产品(套利 / 网格)暂停:**
    * 不可新开 CM 套利 bot;已有 CM 套利 bot 不可减仓。
    * 所有 CM 网格操作被禁止:新建 / 补保证金 / 提取保证金 / 关闭 / 取消。
    * CM 网格若使用 `markPrice` 触发,即便 `markPrice` 在窗口内触及触发价,网格也**不会** 触发,需等开机后若仍越过阈值才会触发。
  * **统一账户 (PM) 期间:**
    * **当 PM 账户在窗口期内触发强平时:**
      * 不存在 CM 余额 / 持仓的用户:强平正常处理。
      * 存在 CM 余额 / 持仓的用户: UM 仓位会被结算,资产可能会被处理;CM 部分**等开机后** 再进行清算。由此**单腿可能会被平仓**(特别是套利仓位可能出现单腿爆仓),对此产生的风险需由用户自行承担。
    * PM 期间**开户 / 关户 / auto-exchange / close-position** 暂停。
  * **窗口期可能返回的错误码:**
    * `{"code":-1016,"msg":"This service is no longer available."}`
    * `{"code":-1016,"msg":"Service is under maintenance."}`
    * `{"239999": "The system is under maintenance, please try again later."}`
    * `{"code":-1109,"msg":"Invalid account."}`



* * *

## 三、REST API 变更

### 1\. 下单 / 改单 / 撤单接口的即时响应不再返回 `avgPrice` / `cumQuote` / `cumBase`

下单 / 改单 / 撤单的即时响应是"挂单确认",成交是异步发生的 — 这些字段在挂单 ack 中本来就是 `0`。实际成交价仍可通过订单查询接口与 userTrades 接口获取。

**受影响接口(CM / DAPI — 移除`cumBase`):**

  * `POST /dapi/v1/order`
  * `POST /dapi/v1/batchOrders`
  * `PUT /dapi/v1/order`
  * `PUT /dapi/v1/batchOrders`
  * `DELETE /dapi/v1/order`
  * `DELETE /dapi/v1/batchOrders`



**受影响接口(UM / FAPI — 移除`cumQuote`):**

  * `POST /fapi/v1/order`
  * `POST /fapi/v1/batchOrders`
  * `PUT /fapi/v1/order`
  * `PUT /fapi/v1/batchOrders`
  * `DELETE /fapi/v1/order`
  * `DELETE /fapi/v1/batchOrders`



> 查询类接口(`GET /fapi/v1/order`、`/allOrders`、`/userTrades` 等)**不受影响** ,仍会返回 `avgPrice` 与 `cumQuote` / `cumBase`。

### 2\. `PUT /dapi/v1/order` 与 `PUT /dapi/v1/batchOrders` — `price` 与 `quantity` 必须同时传

迁移后,这两个 PUT 接口要求同时传 `price` **和** `quantity`。只传其中一个返回 `-1102`。批量接口任一元素缺字段则该元素返回 `-1102`。

### 3\. 以下接口入参均可传入 UM 与 CM 的 symbol

  * `GET /fapi/v1/klines`
  * `GET /fapi/v1/continuousKlines`
  * `GET /fapi/v1/indexPriceKlines`
  * `GET /fapi/v1/markPriceKlines`
  * `GET /fapi/v1/premiumIndexKlines`
  * `GET /dapi/v1/klines`
  * `GET /dapi/v1/continuousKlines`
  * `GET /dapi/v1/indexPriceKlines`
  * `GET /dapi/v1/markPriceKlines`
  * `GET /dapi/v1/premiumIndexKlines`



### 4\. `GET /fapi/v1/assetIndex` 接口名变更为"资产汇率指数",响应额外推送 CM 结算资产价格指数

  * 显示名由"**多资产模式资产汇率指数** "变更为"**资产汇率指数** "。
  * HTTP 路径 `/fapi/v1/assetIndex` **保持不变** ,客户端调用代码无需修改。
  * 响应中**额外** 包含币本位结算资产的价格指数条目 — 如 `BTCUSD`、`ETHUSD`、`BNBUSD`、`SOLUSD`。原有 UM 端条目仍然保留。



### 5\. CM 新增 algo order 接口

COIN-M 现在提供与 UM 同样的 algo-order 接口集合:

  * `POST /dapi/v1/algoOrder` — 新建 CONDITIONAL algo 订单(STOP / TAKE_PROFIT / STOP_MARKET / TAKE_PROFIT_MARKET / TRAILING_STOP_MARKET)
  * `GET /dapi/v1/openAlgoOrders` — 列出当前 open 的 algo 订单
  * `DELETE /dapi/v1/algoOrder` — 撤销 algo 订单(通过 `algoId` 或 `clientAlgoId`)



### 6\. 普通下单接口不再支持 stop 类型订单

迁移后经过一段延迟生效期(具体生效时间另行通知),以下入口对 stop 类型 (`STOP_MARKET` / `TAKE_PROFIT_MARKET` / `STOP` / `TAKE_PROFIT` / `TRAILING_STOP_MARKET`) 的 `type` 值会被拒绝:
    
    
    Code
    
    {
      "code": -4120,
      "msg": "Order type not supported for this endpoint. Please use the Algo Order API endpoints instead."
    }

**受影响接口:**

  * `POST /dapi/v1/order` (单笔)
  * `POST /dapi/v1/batchOrders` (按元素拒绝)
  * WebSocket API: COIN-M ws-dapi 端的 `order.place`



**行动项:** 把 stop 类型订单切换到第 5 点的新接口 `/dapi/v1/algoOrder`。

### 7\. DAPI 错误码变更

接口| 场景| 迁移前| 迁移后  
---|---|---|---  
`GET /dapi/v1/openOrders`| 非法 `symbol`| `200`(静默)| `-1121`  
  
### 8\. DAPI 请求权重变更

接口| 迁移前| 迁移后  
---|---|---  
`GET /dapi/v2/leverageBracket`| `1`(固定)| 带 `symbol` `1` / 不带 `symbol` `2`  
`GET /dapi/v1/allOrders`| `20` / `40`| `5`(固定)  
`GET /dapi/v1/userTrades`| `20` / `40`| `5`(固定)  
`GET /dapi/v1/forceOrders`| `20`(固定)| 带 `symbol` `20` / 不带 `symbol` `50`  
  
* * *

## 四、WebSocket 变更

### 1\. WebSocket API — `order.place` / `order.modify` / `order.cancel` 即时响应不再返回 `avgPrice` / `cumQuote` (UM) / `cumBase` (CM)

原理同三、1 — 即时响应是挂单 ack,成交异步。

### 2\. WebSocket API — `order.modify` 必须同时传 `price` 和 `quantity`

只传其中一个返回 `-1102`。

### 3\. `!assetIndex@arr` Stream 改名为"资产汇率指数",额外推送 CM 结算资产价格指数

  * 显示名由"**多资产模式资产汇率指数** "变更为"**资产汇率指数** "。
  * 订阅键 (`!assetIndex@arr`) **保持不变** ,已有订阅无需修改代码即可继续使用。
  * Stream 现在**额外** 推送币本位结算资产条目(如 `BTCUSD` / `ETHUSD` / `BNBUSD` / `SOLUSD`)。



### 4\. 以下 Stream payload 新增 `st` 字段

`st` 区分 symbol 类型:`1` = UM,`2` = CM。

  * `!miniTicker@arr`
  * `!ticker@arr`
  * `!bookTicker`
  * `!forceOrder@arr`
  * `!contractInfo`
  * `<symbol>@depth<levels>`(包括 `@500ms` / `@100ms`)
  * `<symbol>@aggTrade`
  * `<symbol>@ticker`
  * `<symbol>@bookTicker`
  * `<symbol>@miniTicker`
  * `<symbol>@rpiDepth`



全市场数组类(`!*@arr` / `!bookTicker` / `!contractInfo`),`fstream` 与 `dstream` 推送相同的合并 UM + CM 内容。

### 5\. UM 端单 symbol 订阅新增 `ps` (pair symbol) 字段,与 CM payload 形态对齐

受影响 stream:

  * `!miniTicker@arr`
  * `<symbol>@miniTicker`
  * `!ticker@arr`
  * `!forceOrder@arr`
  * `<symbol>@depth<levels>`(包括 `@500ms` / `@100ms`)
  * `!bookTicker`
  * `<symbol>@bookTicker`
  * `<symbol>@rpiDepth@500ms`



### 6\. markPrice / kline 系列 stream — fstream 和 dstream 跨域订阅

`fstream` 与 `dstream` 均可订阅以下 stream。

**markPrice 系列** — payload 新增 `st` 字段(`1` = UM,`2` = CM):

  * `<symbol>@markPrice`,`<symbol>@markPrice@1s`
  * `<pair>@markPrice`,`<pair>@markPrice@1s`
  * `!markPrice@arr`,`!markPrice@arr@1s`



> CM 端 `!markPrice@arr` / `!markPrice@arr@1s` 暂未提供独立文档页,后续发布。

**UM 端 kline 系列** — `fstream` 与 `dstream` 均可订阅:

  * `<symbol>@kline_<interval>`
  * `<pair>_<contractType>@continuousKline_<interval>`



**CM 端 kline 系列** — `fstream` 与 `dstream` 均可订阅:

  * `<symbol>@kline_<interval>`
  * `<pair>_<contractType>@continuousKline_<interval>`
  * `<pair>@indexPriceKline_<interval>`
  * `<symbol>@markPriceKline_<interval>`



* * *

## 行动项汇总

  1. **账户层**

     * 迁移后请重新核对 `dualSidePosition` 设置,任一侧调整都会同步另一侧。
     * 调整 `dualSidePosition` 之前,请确保 UM 和 CM 都无挂单且无持仓。
  2. **REST**

     * 调整客户端代码 — 不要再从下单 / 改单 / 撤单的响应里读 `avgPrice` / `cumQuote` / `cumBase`,改用 `GET /{f,d}api/v1/order` 或 `userTrades` 取实际成交数据。
     * 调用 `PUT /dapi/v1/order` 或 `PUT /dapi/v1/batchOrders` 时,必须同时传 `price` 和 `quantity`。
     * 更新 DAPI 错误码处理:`GET /dapi/v1/openOrders` 传非法 `symbol` 现在返回 `-1121`(此前为静默 `200`)。
     * 把 COIN-M 的 stop 类订单从 `POST /dapi/v1/order` / `batchOrders` / `ws-dapi order.place` 切换到新接口 `/dapi/v1/algoOrder`。
  3. **WebSocket**

     * 对第四节 4 / 5 / 6 列出的 stream,准备好接收新增的 `st` 与 `ps` 字段,parser 应允许新字段而不报错。
     * 准备好接收 `!ticker@arr` / `!miniTicker@arr` / `!bookTicker` / `!forceOrder@arr` / `!contractInfo` 上合并后的 UM + CM 全量 universe。
  4. **维护窗口**

     * 在公告窗口内暂停 CM 策略 / PM 相关操作,期间可能收到 `-1016` / `239999` / `-1109` 错误。



此页面是否有帮助？

Last modified on November 12, 2026

[更新日志](/zh-CN/docs/products/derivatives-trading-coin-futures/change-log)[基本信息](/zh-CN/docs/products/derivatives-trading-coin-futures/general-info)