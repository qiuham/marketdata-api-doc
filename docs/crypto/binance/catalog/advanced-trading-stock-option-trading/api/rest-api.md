---
exchange: binance
source_url: https://developers.binance.com/en/docs/catalog/advanced-trading-stock-option-trading/api/rest-api
api_type: REST
updated_at: 2026-11-27 18:48:03.288417
---

# Stock Option Trading REST API

Schema: https://developers.binance.com/en/docs/catalog/advanced-trading-stock-option-trading/api/rest-api/1.0.0/schema.yaml

REST APIs for Binance Stock Option Trading (US-listed equity options). All endpoints under `/sapi/v1/equity/option/*`.

Binance 股票期权交易（美股期权）REST API。所有接口位于 `/sapi/v1/equity/option/*`。

版本: 1.0.0

## 服务地址

- `https://api.binance.com`

## 接口列表

- `GET /sapi/v1/equity/option/market/expirations` — Option Expirations (MARKET_DATA)
- `GET /sapi/v1/equity/option/market/contracts` — Option Contracts (MARKET_DATA)
- `GET /sapi/v1/equity/option/market/exchangeInfo` — Option Exchange Info (MARKET_DATA)
- `POST /sapi/v1/equity/option/order/place` — Place Option Order (TRADE)
- `POST /sapi/v1/equity/option/order/cancel` — Cancel Option Order (TRADE)
- `POST /sapi/v1/equity/option/order/cancel-all` — Cancel All Option Orders (TRADE)
- `POST /sapi/v1/equity/option/exercise/submit` — Submit Option Exercise (TRADE)
- `GET /sapi/v1/equity/option/order/open-orders` — Current Open Option Orders (USER_DATA)
- `GET /sapi/v1/equity/option/order/history` — Option Order History (USER_DATA)
- `GET /sapi/v1/equity/option/order/detail` — Option Order Detail (USER_DATA)
- `GET /sapi/v1/equity/option/trade/history` — Option Trade History (USER_DATA)
- `GET /sapi/v1/equity/option/position` — Option Positions (USER_DATA)
- `GET /sapi/v1/equity/option/exercise/exercisable` — Exercisable Options (USER_DATA)
- `GET /sapi/v1/equity/option/exercise/detail` — Option Exercise Detail (USER_DATA)
- `GET /sapi/v1/equity/option/exercise/history` — Option Exercise History (USER_DATA)
- `GET /sapi/v1/equity/option/event/history` — Option Settlement Event History (USER_DATA)
- `GET /sapi/v1/equity/option/event/detail` — Option Settlement Event Detail (USER_DATA)
- `POST /sapi/v1/equity/option/listenKey` — Create / Renew Listen Key (USER_STREAM)

## Option Expirations (MARKET_DATA)（到期日列表 (MARKET_DATA)）

`GET /sapi/v1/equity/option/market/expirations`

Returns every expiration date currently tradable for an underlying, in ascending `expirationDate` order.

When standard and corporate-action-adjusted contracts share an expiration date, **multiple** rows are returned with the same `expirationDate` and different `rootSymbol`. To list the adjusted set, pass that `rootSymbol` to Option Contracts.

Reference data only — no market data.

An unknown underlying, or one without listed options, returns `-1121 Invalid symbol.` An empty array is never returned.

Only the `X-MBX-APIKEY` header is required; this endpoint is **not signed** and takes no `timestamp` / `recvWindow`.

返回某个标的当前可交易的全部期权到期日，按 `expirationDate` 升序。

同一到期日下若同时存在标准合约与公司行动调整后的合约，会返回**多条**记录：`expirationDate` 相同、`rootSymbol` 不同。要查调整后的那一组，需把 `rootSymbol` 传给「合约列表」。

只含参考数据，不含任何行情。

`underlyingSymbol` 不存在或该标的不支持期权时返回 `-1121 Invalid symbol.`，不会返回空数组。

本接口只需在 Header 中携带 `X-MBX-APIKEY`，**无需签名**，也无需 `timestamp` / `recvWindow`。

权重: 1

Operation ID: `optionExpirations`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| underlyingSymbol | query | string | 是 | Underlying US-equity ticker, e.g. `NVDA`.<br>标的美股 ticker，如 `NVDA`。<br>例: `NVDA` |

### 响应 200：Option Expirations / 到期日列表

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].expirationDate | string |  | Expiration date in `YYYY-MM-DD`, US Eastern (ET) calendar day. Can be passed as-is to Option Contracts.<br>到期日，格式 `YYYY-MM-DD`，美东（ET）日历日。可原样作为「合约列表」的入参。<br>例: `2026-09-30` |
| [].rootSymbol | string |  | OCC root symbol. Differs from `underlyingSymbol` for contracts adjusted by a corporate action (e.g. `GOOG1`).<br>OCC root。公司行动调整后的合约与 `underlyingSymbol` 不同（如 `GOOG1`）。<br>例: `NVDA` |

## Option Contracts (MARKET_DATA)（合约列表 (MARKET_DATA)）

`GET /sapi/v1/equity/option/market/contracts`

Returns every option contract (calls and puts) of an underlying for one expiration date. Reference data only — no market data.

Sorted by `strikePrice` ascending; for the same strike, `CALL` comes before `PUT`. Not paginated.

If there is no contract for the `(underlying, root, expiration)` combination, an empty array is returned.

Only the `X-MBX-APIKEY` header is required; this endpoint is **not signed** and takes no `timestamp` / `recvWindow`.

返回某个标的在指定到期日下的全部期权合约（Call + Put），只含合约参考数据，不含任何行情。

按 `strikePrice` 升序，同一行权价下 `CALL` 在前、`PUT` 在后。不分页。

`(标的, root, 到期日)` 组合下没有合约时返回空数组，不报错。

本接口只需在 Header 中携带 `X-MBX-APIKEY`，**无需签名**，也无需 `timestamp` / `recvWindow`。

权重: 1

Operation ID: `optionContracts`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| underlyingSymbol | query | string | 是 | Underlying US-equity ticker, e.g. `NVDA`.<br>标的美股 ticker，如 `NVDA`。<br>例: `NVDA` |
| expirationDate | query | string | 是 | Expiration date in `YYYY-MM-DD`, taken from Option Expirations. Other formats (e.g. `2026-9-30`, `2026/09/30`) are rejected.<br>到期日，格式 `YYYY-MM-DD`，取值来自「到期日列表」。其他格式（如 `2026-9-30`、`2026/09/30`）直接拒绝。<br>例: `2026-09-30` |
| rootSymbol | query | string |  | OCC root. If omitted, only **standard** contracts are returned. To list corporate-action-adjusted contracts (e.g. `GOOG1`), pass the `rootSymbol` from Option Expirations.<br>OCC root。不传则**只返回标准合约**；要查公司行动调整后的合约（如 `GOOG1`），需传「到期日列表」返回的 `rootSymbol`。<br>例: `NVDA` |

### 响应 200：Option Contracts / 合约列表

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].symbol | string |  | OCC contract symbol; usable for order placement and Option Exchange Info.<br>OCC 合约代码，可直接用于下单、「合约交易规则」等接口。<br>例: `NVDA260930C00100000` |
| [].contractType | string |  | `CALL` / `PUT`.<br>`CALL` / `PUT`。<br>例: `CALL` |
| [].strikePrice | string |  | Strike price.<br>行权价。<br>例: `100` |
| [].multiplier | string |  | Premium multiplier. Order cost = price × quantity × multiplier.<br>权利金乘数，订单成本 = price × quantity × multiplier。<br>例: `100` |
| [].contractSize | integer |  | Shares delivered per contract. Equals `multiplier` for standard contracts; may differ after a corporate action.<br>每张合约交割的正股股数。标准合约等于 `multiplier`，公司行动调整后可能不等。<br>例: `100` |
| [].expirationDate | string |  | Expiration date in `YYYY-MM-DD`, US Eastern (ET) calendar day.<br>到期日，格式 `YYYY-MM-DD`，美东（ET）日历日。<br>例: `2026-09-30` |
| [].status | string |  | Contract trading status: `OPEN_CLOSE` / `CLOSE_ONLY` / `NONE`. Omitted when the status of a contract is temporarily unavailable. See [Common Definition](/products/stock-options/common-definition#status).<br>合约交易状态：`OPEN_CLOSE` / `CLOSE_ONLY` / `NONE`，见[通用枚举定义](/products/stock-options/common-definition#status)。个别合约暂时取不到状态时不返回。<br>枚举: `OPEN_CLOSE`, `CLOSE_ONLY`, `NONE`<br>例: `OPEN_CLOSE` |

## Option Exchange Info (MARKET_DATA)（合约交易规则 (MARKET_DATA)）

`GET /sapi/v1/equity/option/market/exchangeInfo`

Returns the trading rules of a single option contract, combining contract-level data (type, strike, expiration, multiplier, deliverables) with underlying-level configuration (price / quantity increments and limits).

`symbol` is **required**. Unlike the stock `exchangeInfo`, listing all contracts is not supported. To browse contracts, use Option Expirations and Option Contracts.

**Price constraints**: a limit price must be a multiple of `tickSize`, and the order notional (`price` × `quantity` × `multiplier`, excluding fees) must fall within the closed interval `[minNotional, maxNotional]`. For a put `SELL` order, the limit price cannot exceed the strike price. All of these values are returned by this endpoint, so you can validate an order before placing it.

**`multiplier` vs `contractSize`**: `multiplier` is used to calculate cost, `contractSize` is the number of shares delivered. Both are 100 for standard contracts and may differ for contracts adjusted by a corporate action (split, merger, special dividend). Always estimate cost with `multiplier`.

Only the `X-MBX-APIKEY` header is required; this endpoint is **not signed** and takes no `timestamp` / `recvWindow`.

返回单个期权合约的交易规则，合并了合约维度（类型、行权价、到期日、乘数、交割物）与标的维度（价格 / 数量档位与上下限）的配置。

`symbol` **必填**。与美股 `exchangeInfo` 不同，不支持全量拉取。按标的浏览合约请使用「到期日列表」与「合约列表」。

**价格约束**：限价需符合 `tickSize` 步进，订单名义金额（`price` × `quantity` × `multiplier`，不含手续费）需落在 `[minNotional, maxNotional]` 闭区间内；卖出 put（`SELL` 方向）的限价不得高于行权价。以上取值本接口都返回，下单前可自行校验。

**`multiplier` 与 `contractSize` 的区别**：前者是算钱用的乘数，后者是交割股数。标准合约两者都是 100；公司行动（拆股 / 并购 / 特别股息）调整后的合约可能不等。估算成本一律用 `multiplier`。

本接口只需在 Header 中携带 `X-MBX-APIKEY`，**无需签名**，也无需 `timestamp` / `recvWindow`。

权重: 1

Operation ID: `optionExchangeInfo`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | OCC contract symbol, e.g. `NVDA260930C00100000`.<br>OCC 合约代码，如 `NVDA260930C00100000`。<br>例: `NVDA260930C00100000` |

### 响应 200：Option Exchange Info / 合约交易规则

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| timezone | string |  | Always `UTC`.<br>时区，固定为 `UTC`。<br>例: `UTC` |
| symbols | object[] |  | Matched contract.<br>匹配到的合约。 |
| symbols[].symbol | string |  | OCC option contract symbol.<br>OCC 合约代码。<br>例: `NVDA260930C00100000` |
| symbols[].underlyingSymbol | string |  | Underlying US-equity ticker.<br>标的美股 ticker。<br>例: `NVDA` |
| symbols[].rootSymbol | string |  | OCC root symbol. Differs from `underlyingSymbol` for contracts adjusted by a corporate action (e.g. `GOOG1`).<br>OCC root。公司行动调整后的合约与 `underlyingSymbol` 不同（如 `GOOG1`）。<br>例: `NVDA` |
| symbols[].contractType | string |  | `CALL` / `PUT`.<br>`CALL` / `PUT`。<br>例: `CALL` |
| symbols[].status | string |  | Contract trading status: `OPEN_CLOSE` / `CLOSE_ONLY` / `NONE`. Omitted when the status of a contract is temporarily unavailable. See [Common Definition](/products/stock-options/common-definition#status).<br>合约交易状态：`OPEN_CLOSE` / `CLOSE_ONLY` / `NONE`，见[通用枚举定义](/products/stock-options/common-definition#status)。个别合约暂时取不到状态时不返回。<br>枚举: `OPEN_CLOSE`, `CLOSE_ONLY`, `NONE`<br>例: `OPEN_CLOSE` |
| symbols[].strikePrice | string |  | Strike price.<br>行权价。<br>例: `100` |
| symbols[].expirationDate | integer (int64) |  | Expiration date as the millisecond timestamp of 12:00 ET on the expiration day. Convert in `America/New_York` and take the date part (see [General Info](/products/stock-options/general-info#numbers-and-timestamps)).<br>到期日当天 12:00 ET 的毫秒时间戳，请按美东时区取日期部分（见[基本信息](/products/stock-options/general-info#数值与时间格式)）。<br>例: `1790784000000` |
| symbols[].multiplier | string |  | Premium multiplier. Order cost = price × quantity × multiplier. `100` for standard contracts.<br>权利金乘数，订单成本 = price × quantity × multiplier。标准合约为 `100`。<br>例: `100` |
| symbols[].contractSize | integer |  | Shares delivered per contract. Equals `multiplier` for standard contracts; may differ after a corporate action.<br>每张交割的正股股数。标准合约等于 `multiplier`，公司行动调整后可能不等。<br>例: `100` |
| symbols[].tickSize | string |  | Minimum price increment.<br>最小价格变动单位。<br>例: `0.01` |
| symbols[].stepSize | string |  | Quantity increment (contracts).<br>张数变动单位。<br>例: `1` |
| symbols[].minQty | string |  | Minimum order quantity (contracts).<br>最小委托张数。<br>例: `1` |
| symbols[].maxQty | string |  | Maximum order quantity (contracts).<br>最大委托张数。<br>例: `100000` |
| symbols[].minNotional | string |  | Minimum order notional (`price` × `quantity` × `multiplier`), excluding fees.<br>最小名义金额（不含手续费）。<br>例: `1` |
| symbols[].maxNotional | string |  | Maximum order notional (`price` × `quantity` × `multiplier`), excluding fees.<br>最大名义金额（不含手续费）。<br>例: `500000` |
| symbols[].optionsLateClose | boolean |  | Whether options on this underlying close 15 minutes later: `true` means 16:15 ET, otherwise 16:00 ET (both move earlier accordingly on early-close days).<br>该标的期权是否延后 15 分钟收盘：`true` 为 16:15 ET，否则 16:00 ET（提前收盘日相应提前）。<br>例: `False` |
| symbols[].pennyProgram | boolean |  | Penny Program indicator. Omitted when unknown.<br>Penny Program 标识；未知时不返回。<br>例: `True` |
| symbols[].deliverables | object[] |  | What one contract delivers on exercise / assignment.<br>每张合约行权 / 被指派时交割的内容。 |
| symbols[].deliverables[].type | string |  | `EQUITY` (shares; `symbol` is the ticker and `amount` is the number of shares) / `CASH` (`symbol` is the currency and `amount` is the cash amount).<br>`EQUITY`（正股，`symbol` 为 ticker，`amount` 为股数）/ `CASH`（现金，`symbol` 为币种，`amount` 为金额）。<br>枚举: `EQUITY`, `CASH`<br>例: `EQUITY` |
| symbols[].deliverables[].symbol | string |  | Ticker or currency.<br>ticker 或币种。<br>例: `NVDA` |
| symbols[].deliverables[].amount | string |  | Number of shares or cash amount.<br>股数或现金金额。<br>例: `100` |

## Place Option Order (TRADE)（下单 (TRADE)）

`POST /sapi/v1/equity/option/order/place`

Place an option limit order.

The server calculates the amount to lock based on `positionIntent` and the contract type: buy to open locks the premium plus fees; sell to open locks the underlying shares for a covered call, or the strike-equivalent cash for a cash-secured put. Fees are calculated by the server; callers do not pass payment details.

**`positionIntent`**: may be omitted, in which case it is derived from `side`: `BUY` → `BUY_TO_OPEN`, `SELL` → `SELL_TO_CLOSE`. The derivation is unreliable in two cases, and an order without `positionIntent` is rejected (parameter error): a `BUY` while you hold a **short** position in the contract (it may be meant as `BUY_TO_CLOSE`), and a `SELL` while you hold **no long** position in the contract (it can only be `SELL_TO_OPEN`). Therefore always pass it for the short side (`SELL_TO_OPEN` / `BUY_TO_CLOSE`). When passed, it must match `side` (`BUY_*` with `BUY`, `SELL_*` with `SELL`), otherwise the order is rejected.

Only `LIMIT` orders with `timeInForce = DAY` are supported, and `quantity` must be a whole number of contracts.

Resubmitting with the **same** `clientOrderId` is idempotent: if the original order was accepted or is still processing, the original order is returned (`S` / `P`); if the original order failed, `497401` is returned.

If the request returns `497001`, `497301` or a broker-rejection error code after the order has already been submitted to the broker, the order may still be processing. Retry with the **same** `clientOrderId` (a replay then returns `P`) or query Option Order Detail by `clientOrderId` for the final status. Do not retry with a new `clientOrderId`.

Rate limit: 200 requests / min (UID).

下一笔期权限价单。

服务端会根据 `positionIntent` 与合约类型自动计算需要冻结的金额：买入开仓冻结权利金加手续费；卖出开仓时，covered call 冻结对应张数的正股，cash-secured put 冻结行权价对应的现金。手续费由服务端计算，调用方不需要传支付明细。

**`positionIntent`**：可以不传，此时服务端按 `side` 推导：`BUY` → `BUY_TO_OPEN`，`SELL` → `SELL_TO_CLOSE`。以下两种情况推导不可靠，不传会被拒单（参数错误）：`BUY` 且该合约当前持有**空头**（可能是要买入平仓 `BUY_TO_CLOSE`）；`SELL` 且该合约当前**没有多头**（只可能是卖出开仓 `SELL_TO_OPEN`）。因此空头侧（`SELL_TO_OPEN` / `BUY_TO_CLOSE`）请始终显式传。显式传入时必须与 `side` 同向（`BUY_*` 配 `BUY`，`SELL_*` 配 `SELL`），否则拒单。

仅支持 `LIMIT` 订单与 `timeInForce = DAY`，`quantity` 必须为整数张。

用**同一个** `clientOrderId` 重复下单是幂等的：原订单已受理或处理中时，直接返回原订单（`S` / `P`）；原订单已失败时返回 `497401`。

下单返回 `497001`、`497301` 或券商拒单类错误码时，若错误发生在订单已提交券商之后，订单可能仍在处理中：请用**同一个** `clientOrderId` 重试（此时返回 `P`），或按 `clientOrderId` 调用「订单详情」查询最终状态，不要换新的 `clientOrderId` 重下。

频率限制：200 次 / 分钟（UID）。

权重: 1

Operation ID: `placeOptionOrder`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | OCC contract symbol.<br>OCC 合约代码。<br>例: `NVDA260930C00100000` |
| quoteAsset | query | string |  | Quote asset. Only `USDC` (default) is supported; other values return `497104`.<br>报价资产，仅支持 `USDC`（默认）；传其他值返回 `497104`。<br>例: `USDC` |
| side | query | string | 是 | `BUY` / `SELL`.<br>`BUY` / `SELL`。<br>枚举: `BUY`, `SELL`<br>例: `BUY` |
| positionIntent | query | string |  | May be omitted and derived from `side` (`BUY` → `BUY_TO_OPEN`, `SELL` → `SELL_TO_CLOSE`); always pass it for the short side (`SELL_TO_OPEN` / `BUY_TO_CLOSE`). Must match `side` when passed.<br>可省略，由 `side` 推导（`BUY` → `BUY_TO_OPEN`，`SELL` → `SELL_TO_CLOSE`）；空头侧（`SELL_TO_OPEN` / `BUY_TO_CLOSE`）请始终显式传。显式传入时必须与 `side` 同向。<br>枚举: `BUY_TO_OPEN`, `SELL_TO_CLOSE`, `SELL_TO_OPEN`, `BUY_TO_CLOSE`<br>例: `BUY_TO_OPEN` |
| quantity | query | string | 是 | Number of contracts. Must be a whole number, minimum `1`.<br>合约张数，必须为整数，最小 `1`。<br>例: `1` |
| price | query | string | 是 | Limit price (premium) per share, minimum `0.01`, must be a multiple of `tickSize`. For a put `SELL` order it cannot exceed the strike price (`497438`).<br>每股权利金限价，最小 `0.01`，需符合 `tickSize`。卖出 put 时不得高于行权价（`497438`）。<br>例: `1.5` |
| timeInForce | query | string |  | Only `DAY` (default) is supported. Other values return a parameter error.<br>仅支持 `DAY`（默认），传其他值返回参数错误。<br>枚举: `DAY`<br>例: `DAY` |
| walletType | query | string |  | Payment wallet: `CARD` (default) / `MAIN`.<br>付款钱包：`CARD`（默认）/ `MAIN`。<br>枚举: `CARD`, `MAIN`<br>例: `CARD` |
| clientOrderId | query | string |  | Client order ID. Format `^[a-zA-Z0-9-_]{32,36}$`. Generated by the server when omitted.<br>客户端订单 ID，格式 `^[a-zA-Z0-9-_]{32,36}$`；省略时由服务端生成。<br>例: `web_2c9c92b74f1e4a7c8f3b9e1a2d3c4b5a` |
| recvWindow | query | integer (int64) |  | The value cannot be greater than `60000`.<br>赋值不能大于 `60000`。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Timestamp in milliseconds.<br>时间戳（毫秒）。<br>例: `1770736694138` |

### 响应 200：Place Option Order / 下单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| status | string |  | `S` = accepted; `P` = processing. A failed order is always returned as an error code (see [Error Code](/products/stock-options/error-code)); a successful response never carries a failed status.<br>`S` = 已受理；`P` = 处理中。下单失败一律以错误码返回（见[错误代码](/products/stock-options/error-code)），正常响应中不会出现失败状态。<br>例: `S` |
| orderId | string |  | Option order ID. Omitted when `status` = `P`; query Option Order Detail by `clientOrderId` instead.<br>期权订单 ID。`status` = `P` 时不返回，请用「订单详情」按 `clientOrderId` 查询。<br>例: `c3c58f49-7b0d-4b9e-a2db-1a2f9a3b8c71` |
| clientOrderId | string |  | Echoes the supplied or server-generated client order ID.<br>回显提交的或服务端生成的客户端订单 ID。<br>例: `web_2c9c92b74f1e4a7c8f3b9e1a2d3c4b5a` |

## Cancel Option Order (TRADE)（撤单 (TRADE)）

`POST /sapi/v1/equity/option/order/cancel`

Cancel an open order by `orderId`.

Cancellation applies to the caller's own brokerage account and is not restricted by asset class: passing the `orderId` of a stock order also cancels it, and `/sapi/v1/equity/order/cancel` can likewise cancel option orders. Only the caller's own orders can be canceled.

Errors on this endpoint use the Stocks Trading error codes (`486xxx`). See [Stocks Trading Error Code](/products/stocks/error-code).

按 `orderId` 撤销一笔未完结的订单。

撤单作用于调用方自己的券商账户，与资产类别无关：传入一笔美股股票订单的 `orderId` 同样会撤单成功，美股的 `/sapi/v1/equity/order/cancel` 也能撤期权订单。只能撤自己的单。

本接口的错误使用股票交易的错误码（`486xxx`），见[股票交易错误代码](/products/stocks/error-code)。

权重: 1

Operation ID: `cancelOptionOrder`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| orderId | query | string | 是 | Option order ID.<br>期权订单 ID。<br>例: `c3c58f49-7b0d-4b9e-a2db-1a2f9a3b8c71` |
| recvWindow | query | integer (int64) |  | The value cannot be greater than `60000`.<br>赋值不能大于 `60000`。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Timestamp in milliseconds.<br>时间戳（毫秒）。<br>例: `1770736694138` |

### 响应 200：Cancel Option Order / 撤单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderId | string |  | Echoes the order ID in the request.<br>回显请求中的订单 ID。<br>例: `c3c58f49-7b0d-4b9e-a2db-1a2f9a3b8c71` |
| status | string |  | Always `S`, meaning the cancel request was accepted upstream. A failed cancellation (e.g. order not found or already filled) is returned as an error code (`486xxx`).<br>固定为 `S`，表示上游已接受撤单请求。撤单失败（如订单不存在、已成交）以错误码返回（`486xxx`）。<br>例: `S` |

## Cancel All Option Orders (TRADE)（全部撤单 (TRADE)）

`POST /sapi/v1/equity/option/order/cancel-all`

Cancel all of the caller's open orders.

**This also cancels open stock orders.** Cancel-all is account-level at the broker and does not distinguish asset classes; it is the same operation as `/sapi/v1/equity/order/cancel-all`.

To cancel option orders only, fetch them with Current Open Option Orders and cancel each one with Cancel Option Order.

Errors on this endpoint use the Stocks Trading error codes (`486xxx`). See [Stocks Trading Error Code](/products/stocks/error-code).

撤销调用方所有未完结订单。

**本接口会连同美股股票挂单一起撤掉。** 券商侧的全撤是账户级的，不区分资产类别，与美股的 `/sapi/v1/equity/order/cancel-all` 是同一个操作。

如果只想撤期权挂单，请先用「当前挂单」取出列表，再逐个调用「撤单」。

本接口的错误使用股票交易的错误码（`486xxx`），见[股票交易错误代码](/products/stocks/error-code)。

权重: 1

Operation ID: `cancelAllOptionOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | The value cannot be greater than `60000`.<br>赋值不能大于 `60000`。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Timestamp in milliseconds.<br>时间戳（毫秒）。<br>例: `1770736694138` |

### 响应 200：Cancel All Option Orders / 全部撤单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| success | boolean |  | `true` if the cancel-all request was accepted upstream. Individual orders may still fail to cancel (e.g. already filled); check with Current Open Option Orders.<br>`true` 表示全撤请求已被上游受理；个别订单可能撤单失败（如已成交），请用「当前挂单」复核。<br>例: `True` |

## Submit Option Exercise (TRADE)（提交行权 (TRADE)）

`POST /sapi/v1/equity/option/exercise/submit`

Submit an exercise request for a long option position.

Requires the `TRADE` permission, because exercising changes positions and balances.

**Exercise is asynchronous.** The request returns `PROCESSING`; delivery is handled by the broker. Poll Option Exercise Detail for the final status.

`quantity` cannot exceed `availableQty` from Exercisable Options.

Resubmitting with the **same** `clientOrderId` is idempotent: if the original exercise was accepted or is still processing, it is returned with its current status; if it failed, `497401` is returned. If the request returns `497001`, `497301` or a broker-rejection error code, the exercise **may still be processing**: retry with the same `clientOrderId` or query Option Exercise Detail by `clientOrderId`. Do not resubmit with a new `clientOrderId`.

对多头期权持仓提交行权申请。

需要 `TRADE` 权限，因为行权会真实改变持仓与资金。

**行权是异步的。** 提交后返回 `PROCESSING`，交割由券商处理，请用「行权详情」轮询终态。

`quantity` 不能超过「可行权合约」返回的 `availableQty`。

用**同一个** `clientOrderId` 重复提交是幂等的：原行权单已受理或处理中时返回原行权单及其当前状态；原行权单已失败时返回 `497401`。提交返回 `497001`、`497301` 或券商拒绝类错误码时，行权**可能仍在处理中**：请用同一个 `clientOrderId` 重试，或用「行权详情」按 `clientOrderId` 查询，不要换新的 `clientOrderId` 重提。

权重: 1

Operation ID: `submitOptionExercise`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| symbol | query | string | 是 | OCC contract symbol to exercise.<br>要行权的 OCC 合约代码。<br>例: `NVDA260930C00100000` |
| quantity | query | string | 是 | Number of contracts to exercise. Whole number, minimum `1`, up to `availableQty`.<br>行权张数，必须为整数，最小 `1`，不超过 `availableQty`。<br>例: `1` |
| quoteAsset | query | string |  | Quote asset. Only `USDC` (default) is supported; other values return `497104`.<br>报价资产，仅支持 `USDC`（默认）；传其他值返回 `497104`。<br>例: `USDC` |
| clientOrderId | query | string |  | Client ID. Format `^[a-zA-Z0-9-_]{32,36}$`. Generated by the server when omitted.<br>客户端 ID，格式 `^[a-zA-Z0-9-_]{32,36}$`；省略时由服务端生成。<br>例: `web_2c9c92b74f1e4a7c8f3b9e1a2d3c4b5a` |
| recvWindow | query | integer (int64) |  | The value cannot be greater than `60000`.<br>赋值不能大于 `60000`。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Timestamp in milliseconds.<br>时间戳（毫秒）。<br>例: `1770736694138` |

### 响应 200：Submit Option Exercise / 提交行权

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| tranId | integer (int64) |  | Exercise transaction ID; use it to query Option Exercise Detail.<br>行权流水 ID，用于查询「行权详情」。<br>例: `1234567890` |
| clientOrderId | string |  | Echoes the supplied or server-generated client ID.<br>回显提交的或服务端生成的客户端 ID。<br>例: `web_2c9c92b74f1e4a7c8f3b9e1a2d3c4b5a` |
| status | string |  | `PROCESSING` on a first successful submission. When replayed with the same `clientOrderId`, the current status of the original exercise (`PROCESSING` / `SUCCESS`) is returned.<br>首次提交成功恒为 `PROCESSING`；用同一 `clientOrderId` 重放时返回原行权单当前状态（`PROCESSING` / `SUCCESS`）。<br>例: `PROCESSING` |

## Current Open Option Orders (USER_DATA)（当前挂单 (USER_DATA)）

`GET /sapi/v1/equity/option/order/open-orders`

Query all of the caller's open **option** orders, including the remaining quantity of partially filled orders. Stock orders are not included.

查询调用方当前所有未完结的**期权**订单，包含部分成交后的剩余委托。不含股票挂单。

权重: 1

Operation ID: `currentOpenOptionOrders`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | The value cannot be greater than `60000`.<br>赋值不能大于 `60000`。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Timestamp in milliseconds.<br>时间戳（毫秒）。<br>例: `1770736694138` |

### 响应 200：Current Open Option Orders / 当前挂单

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].orderId | string |  | Option order ID.<br>期权订单 ID。<br>例: `c3c58f49-7b0d-4b9e-a2db-1a2f9a3b8c71` |
| [].clientOrderId | string |  | Client order ID.<br>客户端订单 ID。<br>例: `web_2c9c92b74f1e4a7c8f3b9e1a2d3c4b5a` |
| [].symbol | string |  | OCC option contract symbol.<br>OCC 合约代码。<br>例: `NVDA260930C00100000` |
| [].underlyingSymbol | string |  | Underlying US-equity ticker.<br>标的美股 ticker。<br>例: `NVDA` |
| [].rootSymbol | string |  | OCC root symbol. Differs from `underlyingSymbol` for contracts adjusted by a corporate action (e.g. `GOOG1`).<br>OCC root。公司行动调整后的合约与 `underlyingSymbol` 不同（如 `GOOG1`）。<br>例: `NVDA` |
| [].contractType | string |  | `CALL` / `PUT`.<br>`CALL` / `PUT`。<br>例: `CALL` |
| [].strikePrice | string |  | Strike price.<br>行权价。<br>例: `100` |
| [].expirationDate | integer (int64) |  | Expiration date as the millisecond timestamp of 12:00 ET on the expiration day. Convert in `America/New_York` and take the date part (see [General Info](/products/stock-options/general-info#numbers-and-timestamps)).<br>到期日当天 12:00 ET 的毫秒时间戳，请按美东时区取日期部分（见[基本信息](/products/stock-options/general-info#数值与时间格式)）。<br>例: `1790784000000` |
| [].multiplier | string |  | Premium multiplier. Order cost = price × quantity × multiplier.<br>权利金乘数，订单成本 = price × quantity × multiplier。<br>例: `100` |
| [].positionIntent | string |  | Position intent: `BUY_TO_OPEN` / `SELL_TO_CLOSE` / `SELL_TO_OPEN` / `BUY_TO_CLOSE`.<br>持仓意图：`BUY_TO_OPEN` / `SELL_TO_CLOSE` / `SELL_TO_OPEN` / `BUY_TO_CLOSE`。<br>例: `BUY_TO_OPEN` |
| [].quoteAsset | string |  | Quote asset.<br>报价资产。<br>例: `USDC` |
| [].side | string |  | `BUY` / `SELL`.<br>`BUY` / `SELL`。<br>例: `BUY` |
| [].orderType | string |  | Order type: `LIMIT`; `MARKET` for orders placed by the broker's automatic liquidation on the expiration date.<br>订单类型：`LIMIT`；到期日券商自动强平单为 `MARKET`。<br>例: `LIMIT` |
| [].limitPrice | string |  | Limit price (premium per share).<br>每股权利金限价。<br>例: `1.5` |
| [].qty | string |  | Order quantity (contracts).<br>委托张数。<br>例: `1` |
| [].filledQty | string |  | Cumulative filled quantity (contracts).<br>累计成交张数。<br>例: `0` |
| [].filledNotional | string |  | Cumulative filled amount.<br>累计成交金额。<br>例: `0` |
| [].totalCost | string |  | Amount locked from the wallet when the order was placed (a snapshot, not updated after fills or cancellation): premium plus fees for buy-to-open and for buy-to-close of a covered call; for buy-to-close of a cash-secured put, only the shortfall remaining after the released collateral (usually `0`); the collateral for sell-to-open (number of shares for a covered call, cash for a cash-secured put); `0` for sell-to-close. Not returned for broker automatic liquidation orders.<br>下单时从钱包锁定的金额（快照，成交与撤单后不更新）：买入开仓、买入平仓 covered call 为权利金加手续费；买入平仓 cash-secured put 只锁释放抵押后仍不足的差额（通常为 `0`）；卖出开仓为抵押品（covered call 为正股股数，cash-secured put 为现金）；卖出平仓为 `0`；券商自动强平单不返回。<br>例: `150.65` |
| [].filledPercent | string |  | Fill progress percentage (0–100).<br>成交进度百分比（0–100）。<br>例: `0` |
| [].status | string |  | Order status: `NEW` / `PENDING_NEW` / `ACCEPTED` / `PARTIALLY_FILLED` / `PENDING_CANCEL` / `PENDING_REPLACE`.<br>订单状态：`NEW` / `PENDING_NEW` / `ACCEPTED` / `PARTIALLY_FILLED` / `PENDING_CANCEL` / `PENDING_REPLACE`。<br>例: `NEW` |
| [].createdAt | integer (int64) |  | Creation time (ms).<br>创建时间（毫秒）。<br>例: `1790173800000` |
| [].updatedAt | integer (int64) |  | Last update time (ms).<br>最后更新时间（毫秒）。<br>例: `1790173800000` |

## Option Order History (USER_DATA)（订单历史 (USER_DATA)）

`GET /sapi/v1/equity/option/order/history`

Paged option order history, sorted by creation time in descending order. Only option orders are returned; stock orders are not included.

分页查询期权订单历史，按创建时间倒序。只返回期权订单，不会混入股票订单。

权重: 1

Operation ID: `optionOrderHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| underlyingSymbol | query | string |  | Underlying US-equity ticker filter, e.g. `NVDA`, case-insensitive. Matches orders on **all** contracts of that underlying, not a single OCC contract. An unlisted or delisted ticker returns `-26004`.<br>标的美股 ticker 过滤，如 `NVDA`，大小写不敏感。命中该标的下**所有**合约的订单，不是按单个 OCC 合约筛选。传入未上架 / 已下架的 ticker 返回 `-26004`。<br>例: `NVDA` |
| side | query | string |  | `BUY` / `SELL`.<br>`BUY` / `SELL`。<br>枚举: `BUY`, `SELL`<br>例: `BUY` |
| orderStatus | query | string |  | Comma-separated status filter, without spaces: `FILLED` / `PARTIALLY_FILLED` / `CANCELED` / `EXPIRED` / `REJECTED`. If omitted, all statuses are returned except open orders with no fills (`NEW` / `ACCEPTED`, etc.).<br>逗号分隔的状态过滤（不要带空格）：`FILLED` / `PARTIALLY_FILLED` / `CANCELED` / `EXPIRED` / `REJECTED`。不传时返回除未成交挂单（`NEW` / `ACCEPTED` 等）以外的全部状态。<br>例: `FILLED,CANCELED` |
| startTime | query | integer (int64) | 是 | Start of the order creation time (`createdAt`) filter (ms). If the span to `endTime` exceeds 180 days, it is truncated to 180 days before `endTime`.<br>按订单创建时间（`createdAt`）过滤的开始时间（毫秒）。与 `endTime` 跨度超过 180 天时，自动截为 `endTime` 前 180 天。<br>例: `1790100000000` |
| endTime | query | integer (int64) | 是 | End of the order creation time (`createdAt`) filter (ms).<br>按订单创建时间（`createdAt`）过滤的结束时间（毫秒）。<br>例: `1790200000000` |
| current | query | integer |  | Page number. Default `1`.<br>页码，默认 `1`。<br>例: `1` |
| size | query | integer |  | Page size. Default `20`, max `100`.<br>每页大小，默认 `20`，最大 `100`。<br>例: `20` |
| recvWindow | query | integer (int64) |  | The value cannot be greater than `60000`.<br>赋值不能大于 `60000`。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Timestamp in milliseconds.<br>时间戳（毫秒）。<br>例: `1770736694138` |

### 响应 200：Option Order History / 订单历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| total | integer (int64) |  | Total number of records.<br>记录总数。<br>例: `1` |
| page | integer |  | Current page number.<br>当前页码。<br>例: `1` |
| size | integer |  | Current page size.<br>当前页大小。<br>例: `20` |
| rows | object[] |  | Order records.<br>订单记录。 |
| rows[].orderId | string |  | Option order ID.<br>期权订单 ID。<br>例: `c3c58f49-7b0d-4b9e-a2db-1a2f9a3b8c71` |
| rows[].clientOrderId | string |  | Client order ID.<br>客户端订单 ID。<br>例: `web_2c9c92b74f1e4a7c8f3b9e1a2d3c4b5a` |
| rows[].symbol | string |  | OCC option contract symbol.<br>OCC 合约代码。<br>例: `NVDA260930C00100000` |
| rows[].underlyingSymbol | string |  | Underlying US-equity ticker.<br>标的美股 ticker。<br>例: `NVDA` |
| rows[].rootSymbol | string |  | OCC root symbol. Differs from `underlyingSymbol` for contracts adjusted by a corporate action (e.g. `GOOG1`).<br>OCC root。公司行动调整后的合约与 `underlyingSymbol` 不同（如 `GOOG1`）。<br>例: `NVDA` |
| rows[].contractType | string |  | `CALL` / `PUT`.<br>`CALL` / `PUT`。<br>例: `CALL` |
| rows[].strikePrice | string |  | Strike price.<br>行权价。<br>例: `100` |
| rows[].expirationDate | integer (int64) |  | Expiration date as the millisecond timestamp of 12:00 ET on the expiration day. Convert in `America/New_York` and take the date part (see [General Info](/products/stock-options/general-info#numbers-and-timestamps)).<br>到期日当天 12:00 ET 的毫秒时间戳，请按美东时区取日期部分（见[基本信息](/products/stock-options/general-info#数值与时间格式)）。<br>例: `1790784000000` |
| rows[].multiplier | string |  | Premium multiplier. Order cost = price × quantity × multiplier.<br>权利金乘数，订单成本 = price × quantity × multiplier。<br>例: `100` |
| rows[].positionIntent | string |  | Position intent: `BUY_TO_OPEN` / `SELL_TO_CLOSE` / `SELL_TO_OPEN` / `BUY_TO_CLOSE`.<br>持仓意图：`BUY_TO_OPEN` / `SELL_TO_CLOSE` / `SELL_TO_OPEN` / `BUY_TO_CLOSE`。<br>例: `BUY_TO_OPEN` |
| rows[].autoLiquidation | boolean |  | `true` if the order was initiated by the broker's automatic liquidation rather than by the user.<br>`true` 表示该单由券商自动强平发起，非用户主动下单。<br>例: `False` |
| rows[].quote | string |  | Quote asset (named `quoteAsset` in Current Open Option Orders).<br>报价资产（「当前挂单」中字段名为 `quoteAsset`）。<br>例: `USDC` |
| rows[].side | string |  | `BUY` / `SELL`.<br>`BUY` / `SELL`。<br>例: `BUY` |
| rows[].orderType | string |  | Order type: `LIMIT`; `MARKET` for orders placed by the broker's automatic liquidation on the expiration date.<br>订单类型：`LIMIT`；到期日券商自动强平单为 `MARKET`。<br>例: `LIMIT` |
| rows[].limitPrice | string |  | Limit price (premium per share). Returned as reported by the broker regardless of order type; not returned for `MARKET` orders, which have no limit price.<br>每股权利金限价。直接返回券商原值，不区分订单类型；`MARKET` 单没有限价，不返回。<br>例: `1.5` |
| rows[].avgFilledPrice | string |  | Average fill price (premium per share) as reported by the broker, returned for all order types. Not returned if the order has no fills.<br>每股平均成交价（券商回报），所有订单类型都返回；未成交时不返回。<br>例: `1.48` |
| rows[].qty | string |  | Order quantity (contracts).<br>委托张数。<br>例: `1` |
| rows[].filledQty | string |  | Cumulative filled quantity (contracts).<br>累计成交张数。<br>例: `1` |
| rows[].filledTotal | string |  | Cumulative filled amount.<br>累计成交金额。<br>例: `148` |
| rows[].fee | string |  | Cumulative fees = `commission` + `sec` + `taf` + `cat` + `orf` + `occ` (excluding `platformFee`). Fees are returned at the order level only; individual fills carry no fee.<br>累计手续费 = `commission` + `sec` + `taf` + `cat` + `orf` + `occ`（不含 `platformFee`）。订单维度返回，单笔成交不单独返回手续费。<br>例: `0.65` |
| rows[].status | string |  | Order status, e.g. `FILLED` / `PARTIALLY_FILLED` / `CANCELED` / `EXPIRED` / `REJECTED`.<br>订单状态，如 `FILLED` / `PARTIALLY_FILLED` / `CANCELED` / `EXPIRED` / `REJECTED`。<br>例: `FILLED` |
| rows[].createdAt | integer (int64) |  | Creation time (ms).<br>创建时间（毫秒）。<br>例: `1790173800000` |
| rows[].updatedAt | integer (int64) |  | Last update time (ms).<br>最后更新时间（毫秒）。<br>例: `1790173802000` |

## Option Order Detail (USER_DATA)（订单详情 (USER_DATA)）

`GET /sapi/v1/equity/option/order/detail`

Query a single option order with its fills and an itemized fee breakdown.

Provide at least one of `orderId` and `clientOrderId`; omitting both returns `-1102`. If both are provided, the order is looked up by `orderId`, and `clientOrderId` must belong to the same order, otherwise `486218 Order not found` is returned.

Only option orders are accepted: the `orderId` / `clientOrderId` of a stock order returns `-2013 Order does not exist.`; an unknown order ID returns `486218 Order not found`.

Example: a fully filled buy-to-open order — `filledTotal` = `total` = 1.48 × 1 × 100 = 148 (excluding fees); total fees `fee` = 0.65 (`commission` + `cat` + `orf` + `occ`). `sec` / `taf` are `0` for buy orders. For an order still in progress with no fills, `fee` and the itemized fees are not returned (`platformFee` is always `"0"`); for an order canceled or expired without any fill, each fee item is `"0"`. `canceledAt` / `expiredAt` are returned only in the corresponding status; `settlementDate` is not returned for buy orders.

查询单笔期权订单及其成交明细，并给出手续费的分项拆解。

`orderId` 与 `clientOrderId` 至少提供一个（都不传返回 `-1102`）。两者都传时以 `orderId` 查询，且 `clientOrderId` 必须与该订单一致，否则返回 `486218 Order not found`。

本接口只认期权订单：传入美股股票订单的 `orderId` / `clientOrderId` 返回 `-2013 Order does not exist.`；订单号不存在返回 `486218 Order not found`。

示例为一笔已全部成交的买入开仓单：`filledTotal` = `total` = 1.48 × 1 × 100 = 148（不含手续费），手续费合计 `fee` = 0.65（`commission` + `cat` + `orf` + `occ`）。买单的 `sec` / `taf` 为 `0`；仍在途且尚无成交的订单不返回 `fee` 及各分项（`platformFee` 恒为 `"0"`）；无成交即撤单 / 失效的订单各项返回 `"0"`。`canceledAt` / `expiredAt` 只在对应状态下返回；买单不返回 `settlementDate`。

权重: 1

Operation ID: `optionOrderDetail`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| orderId | query | string |  | Option order ID. Provide at least one of `orderId` and `clientOrderId`.<br>期权订单 ID。与 `clientOrderId` 至少提供一个。<br>例: `c3c58f49-7b0d-4b9e-a2db-1a2f9a3b8c71` |
| clientOrderId | query | string |  | Client order ID. Provide at least one of `orderId` and `clientOrderId`.<br>客户端订单 ID。与 `orderId` 至少提供一个。<br>例: `web_2c9c92b74f1e4a7c8f3b9e1a2d3c4b5a` |
| recvWindow | query | integer (int64) |  | The value cannot be greater than `60000`.<br>赋值不能大于 `60000`。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Timestamp in milliseconds.<br>时间戳（毫秒）。<br>例: `1770736694138` |

### 响应 200：Option Order Detail / 订单详情

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| orderId | string |  | Option order ID.<br>期权订单 ID。<br>例: `c3c58f49-7b0d-4b9e-a2db-1a2f9a3b8c71` |
| clientOrderId | string |  | Client order ID.<br>客户端订单 ID。<br>例: `web_2c9c92b74f1e4a7c8f3b9e1a2d3c4b5a` |
| symbol | string |  | OCC option contract symbol.<br>OCC 合约代码。<br>例: `NVDA260930C00100000` |
| underlyingSymbol | string |  | Underlying US-equity ticker.<br>标的美股 ticker。<br>例: `NVDA` |
| rootSymbol | string |  | OCC root symbol. Differs from `underlyingSymbol` for contracts adjusted by a corporate action (e.g. `GOOG1`).<br>OCC root。公司行动调整后的合约与 `underlyingSymbol` 不同（如 `GOOG1`）。<br>例: `NVDA` |
| contractType | string |  | `CALL` / `PUT`.<br>`CALL` / `PUT`。<br>例: `CALL` |
| strikePrice | string |  | Strike price.<br>行权价。<br>例: `100` |
| expirationDate | integer (int64) |  | Expiration date as the millisecond timestamp of 12:00 ET on the expiration day. Convert in `America/New_York` and take the date part (see [General Info](/products/stock-options/general-info#numbers-and-timestamps)).<br>到期日当天 12:00 ET 的毫秒时间戳，请按美东时区取日期部分（见[基本信息](/products/stock-options/general-info#数值与时间格式)）。<br>例: `1790784000000` |
| multiplier | string |  | Premium multiplier. Order cost = price × quantity × multiplier.<br>权利金乘数，订单成本 = price × quantity × multiplier。<br>例: `100` |
| positionIntent | string |  | Position intent: `BUY_TO_OPEN` / `SELL_TO_CLOSE` / `SELL_TO_OPEN` / `BUY_TO_CLOSE`.<br>持仓意图：`BUY_TO_OPEN` / `SELL_TO_CLOSE` / `SELL_TO_OPEN` / `BUY_TO_CLOSE`。<br>例: `BUY_TO_OPEN` |
| autoLiquidation | boolean |  | `true` if the order was initiated by the broker's automatic liquidation rather than by the user.<br>`true` 表示该单由券商自动强平发起，非用户主动下单。<br>例: `False` |
| quote | string |  | Quote asset (named `quoteAsset` in Current Open Option Orders).<br>报价资产（「当前挂单」中字段名为 `quoteAsset`）。<br>例: `USDC` |
| side | string |  | `BUY` / `SELL`.<br>`BUY` / `SELL`。<br>例: `BUY` |
| orderType | string |  | Order type: `LIMIT`; `MARKET` for orders placed by the broker's automatic liquidation on the expiration date.<br>订单类型：`LIMIT`；到期日券商自动强平单为 `MARKET`。<br>例: `LIMIT` |
| limitPrice | string |  | Limit price (premium per share). Returned as reported by the broker regardless of order type; not returned for `MARKET` orders, which have no limit price.<br>每股权利金限价。直接返回券商原值，不区分订单类型；`MARKET` 单没有限价，不返回。<br>例: `1.5` |
| avgFilledPrice | string |  | Average fill price (premium per share) as reported by the broker, returned for all order types. Not returned if the order has no fills.<br>每股平均成交价（券商回报），所有订单类型都返回；未成交时不返回。<br>例: `1.48` |
| qty | string |  | Order quantity (contracts).<br>委托张数。<br>例: `1` |
| filledQty | string |  | Cumulative filled quantity (contracts).<br>累计成交张数。<br>例: `1` |
| filledTotal | string |  | Cumulative filled amount.<br>累计成交金额。<br>例: `148` |
| fee | string |  | Cumulative fees = `commission` + `sec` + `taf` + `cat` + `orf` + `occ` (excluding `platformFee`). Fees are returned at the order level only; individual fills carry no fee.<br>累计手续费 = `commission` + `sec` + `taf` + `cat` + `orf` + `occ`（不含 `platformFee`）。订单维度返回，单笔成交不单独返回手续费。<br>例: `0.65` |
| status | string |  | Order status, e.g. `FILLED` / `PARTIALLY_FILLED` / `CANCELED` / `EXPIRED` / `REJECTED`.<br>订单状态，如 `FILLED` / `PARTIALLY_FILLED` / `CANCELED` / `EXPIRED` / `REJECTED`。<br>例: `FILLED` |
| createdAt | integer (int64) |  | Creation time (ms).<br>创建时间（毫秒）。<br>例: `1790173800000` |
| updatedAt | integer (int64) |  | Last update time (ms).<br>最后更新时间（毫秒）。<br>例: `1790173802000` |
| timeInForce | string |  | Time in force. Always `DAY`.<br>有效期，恒为 `DAY`。<br>例: `DAY` |
| commission | string |  | Commission.<br>佣金。<br>例: `0.6` |
| platformFee | string |  | Platform fee.<br>平台费。<br>例: `0` |
| sec | string |  | SEC fee. Charged on sell orders only; `0` for buy orders.<br>SEC 费（仅卖出方向收取，买单为 `0`）。<br>例: `0` |
| taf | string |  | FINRA TAF. Charged on sell orders only; `0` for buy orders.<br>FINRA TAF（仅卖出方向收取，买单为 `0`）。<br>例: `0` |
| cat | string |  | FINRA CAT fee.<br>FINRA CAT 费。<br>例: `0.01` |
| orf | string |  | Options Regulatory Fee (ORF).<br>期权监管费（ORF）。<br>例: `0.02` |
| occ | string |  | OCC clearing fee.<br>OCC 清算费。<br>例: `0.02` |
| total | string |  | Cumulative filled amount, same as `filledTotal` (average fill price × filled quantity × multiplier), excluding fees.<br>累计成交金额，与 `filledTotal` 相同（成交均价 × 成交张数 × 乘数，不含手续费）。<br>例: `148` |
| filledAt | integer (int64) |  | Fully filled time (ms).<br>完全成交时间（毫秒）。<br>例: `1790173802000` |
| canceledAt | integer (int64) |  | Cancel time (ms). Returned only for canceled orders.<br>撤单时间（毫秒），仅已撤销订单返回。<br>例: `1790173802000` |
| expiredAt | integer (int64) |  | Expiry time (ms). Returned only for expired orders.<br>失效时间（毫秒），仅已失效订单返回。<br>例: `1790173802000` |
| settlementDate | integer (int64) |  | Millisecond timestamp of 14:00 ET on the settlement date. Returned only for sell orders with fills.<br>结算日当天 14:00 ET 的毫秒时间戳。仅卖出方向且有成交时返回。<br>例: `1790272800000` |
| trades | object[] |  | Fills of this order, sorted by execution time in descending order. Individual fills carry no fee; see the order-level `fee` and itemized fees.<br>成交明细，按成交时间倒序。单笔成交不返回手续费，手续费见订单上的 `fee` 及分项。 |
| trades[].executionId | string |  | Execution ID.<br>成交 ID。<br>例: `8f2d0c1e-5b7a-4e3c-9d61-2a4b6c8e0f13` |
| trades[].executionAt | integer (int64) |  | Execution time (ms).<br>成交时间（毫秒）。<br>例: `1790173802000` |
| trades[].price | string |  | Fill price (premium per share).<br>每股成交价。<br>例: `1.48` |
| trades[].qty | string |  | Fill quantity (contracts).<br>成交张数。<br>例: `1` |

```json
{
  "orderId": "c3c58f49-7b0d-4b9e-a2db-1a2f9a3b8c71",
  "clientOrderId": "web_2c9c92b74f1e4a7c8f3b9e1a2d3c4b5a",
  "symbol": "NVDA260930C00100000",
  "underlyingSymbol": "NVDA",
  "rootSymbol": "NVDA",
  "contractType": "CALL",
  "strikePrice": "100",
  "expirationDate": 1790784000000,
  "multiplier": "100",
  "positionIntent": "BUY_TO_OPEN",
  "autoLiquidation": false,
  "quote": "USDC",
  "side": "BUY",
  "orderType": "LIMIT",
  "limitPrice": "1.5",
  "avgFilledPrice": "1.48",
  "qty": "1",
  "filledQty": "1",
  "filledTotal": "148",
  "fee": "0.65",
  "status": "FILLED",
  "createdAt": 1790173800000,
  "updatedAt": 1790173802000,
  "timeInForce": "DAY",
  "commission": "0.6",
  "platformFee": "0",
  "sec": "0",
  "taf": "0",
  "cat": "0.01",
  "orf": "0.02",
  "occ": "0.02",
  "total": "148",
  "filledAt": 1790173802000,
  "trades": [
    {
      "executionId": "8f2d0c1e-5b7a-4e3c-9d61-2a4b6c8e0f13",
      "executionAt": 1790173802000,
      "price": "1.48",
      "qty": "1"
    }
  ]
}
```

## Option Trade History (USER_DATA)（成交历史 (USER_DATA)）

`GET /sapi/v1/equity/option/trade/history`

Paged per-fill option trade history. Only option fills are returned. Option fees are charged per order, so individual fills carry no fee; see `fee` in Option Order History / Option Order Detail.

分页查询期权逐笔成交历史。只返回期权成交。期权手续费按订单收取，单笔成交不返回手续费，请查「订单历史」/「订单详情」的 `fee`。

权重: 1

Operation ID: `optionTradeHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| underlyingSymbol | query | string |  | Underlying US-equity ticker filter, e.g. `NVDA`, case-insensitive. Matches fills on **all** contracts of that underlying, not a single OCC contract. An unlisted or delisted ticker returns `-26004`.<br>标的美股 ticker 过滤，如 `NVDA`，大小写不敏感。命中该标的下**所有**合约的成交，不是按单个 OCC 合约筛选。传入未上架 / 已下架的 ticker 返回 `-26004`。<br>例: `NVDA` |
| side | query | string |  | `BUY` / `SELL`.<br>`BUY` / `SELL`。<br>枚举: `BUY`, `SELL`<br>例: `BUY` |
| orderId | query | string |  | Return fills of this order only.<br>仅返回指定订单的成交记录。<br>例: `c3c58f49-7b0d-4b9e-a2db-1a2f9a3b8c71` |
| startTime | query | integer (int64) | 是 | Start of the execution time (`executionAt`) filter (ms).<br>按成交时间（`executionAt`）过滤的开始时间（毫秒）。<br>例: `1790100000000` |
| endTime | query | integer (int64) | 是 | End of the execution time (`executionAt`) filter (ms).<br>按成交时间（`executionAt`）过滤的结束时间（毫秒）。<br>例: `1790200000000` |
| current | query | integer |  | Page number. Default `1`.<br>页码，默认 `1`。<br>例: `1` |
| size | query | integer |  | Page size. Default `20`, max `100`.<br>每页大小，默认 `20`，最大 `100`。<br>例: `20` |
| recvWindow | query | integer (int64) |  | The value cannot be greater than `60000`.<br>赋值不能大于 `60000`。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Timestamp in milliseconds.<br>时间戳（毫秒）。<br>例: `1770736694138` |

### 响应 200：Option Trade History / 成交历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| total | integer (int64) |  | Total number of records.<br>记录总数。<br>例: `1` |
| page | integer |  | Current page number.<br>当前页码。<br>例: `1` |
| size | integer |  | Current page size.<br>当前页大小。<br>例: `20` |
| rows | object[] |  | Fill records.<br>成交记录。 |
| rows[].executionId | string |  | Execution ID.<br>成交 ID。<br>例: `8f2d0c1e-5b7a-4e3c-9d61-2a4b6c8e0f13` |
| rows[].orderId | string |  | Option order ID.<br>期权订单 ID。<br>例: `c3c58f49-7b0d-4b9e-a2db-1a2f9a3b8c71` |
| rows[].clientOrderId | string |  | Client order ID.<br>客户端订单 ID。<br>例: `web_2c9c92b74f1e4a7c8f3b9e1a2d3c4b5a` |
| rows[].symbol | string |  | OCC option contract symbol.<br>OCC 合约代码。<br>例: `NVDA260930C00100000` |
| rows[].underlyingSymbol | string |  | Underlying US-equity ticker.<br>标的美股 ticker。<br>例: `NVDA` |
| rows[].rootSymbol | string |  | OCC root symbol. Differs from `underlyingSymbol` for contracts adjusted by a corporate action (e.g. `GOOG1`).<br>OCC root。公司行动调整后的合约与 `underlyingSymbol` 不同（如 `GOOG1`）。<br>例: `NVDA` |
| rows[].contractType | string |  | `CALL` / `PUT`.<br>`CALL` / `PUT`。<br>例: `CALL` |
| rows[].strikePrice | string |  | Strike price.<br>行权价。<br>例: `100` |
| rows[].expirationDate | integer (int64) |  | Expiration date as the millisecond timestamp of 12:00 ET on the expiration day. Convert in `America/New_York` and take the date part (see [General Info](/products/stock-options/general-info#numbers-and-timestamps)).<br>到期日当天 12:00 ET 的毫秒时间戳，请按美东时区取日期部分（见[基本信息](/products/stock-options/general-info#数值与时间格式)）。<br>例: `1790784000000` |
| rows[].multiplier | string |  | Premium multiplier. Order cost = price × quantity × multiplier.<br>权利金乘数，订单成本 = price × quantity × multiplier。<br>例: `100` |
| rows[].positionIntent | string |  | Position intent: `BUY_TO_OPEN` / `SELL_TO_CLOSE` / `SELL_TO_OPEN` / `BUY_TO_CLOSE`.<br>持仓意图：`BUY_TO_OPEN` / `SELL_TO_CLOSE` / `SELL_TO_OPEN` / `BUY_TO_CLOSE`。<br>例: `BUY_TO_OPEN` |
| rows[].autoLiquidation | boolean |  | `true` if the order was initiated by the broker's automatic liquidation rather than by the user.<br>`true` 表示该单由券商自动强平发起，非用户主动下单。<br>例: `False` |
| rows[].quote | string |  | Quote asset.<br>报价资产。<br>例: `USDC` |
| rows[].side | string |  | `BUY` / `SELL`.<br>`BUY` / `SELL`。<br>例: `BUY` |
| rows[].orderType | string |  | Order type: `LIMIT`; `MARKET` for orders placed by the broker's automatic liquidation on the expiration date.<br>订单类型：`LIMIT`；到期日券商自动强平单为 `MARKET`。<br>例: `LIMIT` |
| rows[].price | string |  | Fill price (premium per share).<br>每股成交价。<br>例: `1.48` |
| rows[].qty | string |  | Fill quantity (contracts).<br>成交张数。<br>例: `1` |
| rows[].total | string |  | Fill amount (price × qty × multiplier), excluding fees.<br>成交金额（price × qty × multiplier，不含手续费）。<br>例: `148` |
| rows[].executionAt | integer (int64) |  | Execution time (ms).<br>成交时间（毫秒）。<br>例: `1790173802000` |
| rows[].updatedAt | integer (int64) |  | Update time (ms).<br>更新时间（毫秒）。<br>例: `1790173802000` |
| rows[].settlementDate | integer (int64) |  | Millisecond timestamp of 14:00 ET on the settlement date. Returned for sell fills only.<br>结算日当天 14:00 ET 的毫秒时间戳。仅卖出方向返回。<br>例: `1790272800000` |

```json
{
  "total": 1,
  "page": 1,
  "size": 20,
  "rows": [
    {
      "executionId": "8f2d0c1e-5b7a-4e3c-9d61-2a4b6c8e0f13",
      "orderId": "c3c58f49-7b0d-4b9e-a2db-1a2f9a3b8c71",
      "clientOrderId": "web_2c9c92b74f1e4a7c8f3b9e1a2d3c4b5a",
      "symbol": "NVDA260930C00100000",
      "underlyingSymbol": "NVDA",
      "rootSymbol": "NVDA",
      "contractType": "CALL",
      "strikePrice": "100",
      "expirationDate": 1790784000000,
      "multiplier": "100",
      "positionIntent": "BUY_TO_OPEN",
      "autoLiquidation": false,
      "quote": "USDC",
      "side": "BUY",
      "orderType": "LIMIT",
      "price": "1.48",
      "qty": "1",
      "total": "148",
      "executionAt": 1790173802000,
      "updatedAt": 1790173802000
    }
  ]
}
```

## Option Positions (USER_DATA)（持仓查询 (USER_DATA)）

`GET /sapi/v1/equity/option/position`

Returns all current option positions.

One record per contract; see `side` for the direction.

**`free` / `locked` are signed: negative for short positions.** For example, with 3 short contracts of which 1 is reserved by an open order, `free` = `"-2"` and `locked` = `"-1"`. When closing (`SELL_TO_CLOSE` / `BUY_TO_CLOSE`), the quantity you can order is the **absolute value** of `free`.

Positions past the last trading time and awaiting settlement are not returned.

返回当前全部期权持仓。

每张合约一条记录，方向见 `side`。

**`free` / `locked` 带符号：空头为负数。** 例如持有 3 张空头、其中 1 张被挂单占用时，`free` = `"-2"`、`locked` = `"-1"`。平仓（`SELL_TO_CLOSE` / `BUY_TO_CLOSE`）时可下单的张数是 `free` 的**绝对值**。

已过最后交易时刻、等待结算的持仓不返回。

权重: 1

Operation ID: `optionPositions`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | The value cannot be greater than `60000`.<br>赋值不能大于 `60000`。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Timestamp in milliseconds.<br>时间戳（毫秒）。<br>例: `1770736694138` |

### 响应 200：Option Positions / 持仓查询

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].symbol | string |  | OCC option contract symbol.<br>OCC 合约代码。<br>例: `NVDA260930C00100000` |
| [].underlyingSymbol | string |  | Underlying US-equity ticker.<br>标的美股 ticker。<br>例: `NVDA` |
| [].contractType | string |  | `CALL` / `PUT`.<br>`CALL` / `PUT`。<br>例: `CALL` |
| [].side | string |  | Position side: `LONG` / `SHORT`.<br>持仓方向：`LONG` / `SHORT`。<br>例: `LONG` |
| [].free | string |  | Contracts available to close, signed (negative for short positions).<br>可平仓张数，带符号（空头为负）。<br>例: `2` |
| [].locked | string |  | Contracts reserved by open orders or submitted exercises, signed (negative for short positions).<br>被挂单或已提交的行权占用的张数，带符号（空头为负）。<br>例: `1` |
| [].strikePrice | string |  | Strike price.<br>行权价。<br>例: `100` |
| [].expirationDate | integer (int64) |  | Expiration date as the millisecond timestamp of 12:00 ET on the expiration day. Convert in `America/New_York` and take the date part (see [General Info](/products/stock-options/general-info#numbers-and-timestamps)).<br>到期日当天 12:00 ET 的毫秒时间戳，请按美东时区取日期部分（见[基本信息](/products/stock-options/general-info#数值与时间格式)）。<br>例: `1790784000000` |
| [].multiplier | string |  | Premium multiplier. Order cost = price × quantity × multiplier.<br>权利金乘数，订单成本 = price × quantity × multiplier。<br>例: `100` |

## Exercisable Options (USER_DATA)（可行权合约 (USER_DATA)）

`GET /sapi/v1/equity/option/exercise/exercisable`

Returns the contracts that can currently be exercised. Only **long** positions are exercisable; the short side is the assigned party and has no exercise right.

`availableQty` is the maximum quantity for Submit Option Exercise.

返回当前可以行权的合约。只有**多头**持仓可行权，空头是被指派方，没有行权选择权。

`availableQty` 是提交行权时的张数上限。

权重: 1

Operation ID: `exercisableOptions`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | The value cannot be greater than `60000`.<br>赋值不能大于 `60000`。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Timestamp in milliseconds.<br>时间戳（毫秒）。<br>例: `1770736694138` |

### 响应 200：Exercisable Options / 可行权合约

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| [].symbol | string |  | OCC option contract symbol.<br>OCC 合约代码。<br>例: `NVDA260930C00100000` |
| [].underlyingSymbol | string |  | Underlying US-equity ticker.<br>标的美股 ticker。<br>例: `NVDA` |
| [].rootSymbol | string |  | OCC root symbol. Differs from `underlyingSymbol` for contracts adjusted by a corporate action (e.g. `GOOG1`).<br>OCC root。公司行动调整后的合约与 `underlyingSymbol` 不同（如 `GOOG1`）。<br>例: `NVDA` |
| [].contractType | string |  | `CALL` / `PUT`.<br>`CALL` / `PUT`。<br>例: `CALL` |
| [].strikePrice | string |  | Strike price.<br>行权价。<br>例: `100` |
| [].expirationDate | integer (int64) |  | Expiration date as the millisecond timestamp of 12:00 ET on the expiration day. Convert in `America/New_York` and take the date part (see [General Info](/products/stock-options/general-info#numbers-and-timestamps)).<br>到期日当天 12:00 ET 的毫秒时间戳，请按美东时区取日期部分（见[基本信息](/products/stock-options/general-info#数值与时间格式)）。<br>例: `1790784000000` |
| [].multiplier | string |  | Premium multiplier. Order cost = price × quantity × multiplier.<br>权利金乘数，订单成本 = price × quantity × multiplier。<br>例: `100` |
| [].positionQty | string |  | Total contracts held.<br>持有总张数。<br>例: `2` |
| [].availableQty | string |  | Contracts available to exercise; the upper limit for Submit Option Exercise.<br>可行权张数，提交行权时的上限。<br>例: `2` |
| [].deliverables | object[] |  | What one contract delivers on exercise / assignment.<br>每张合约行权 / 被指派时交割的内容。 |
| [].deliverables[].type | string |  | `EQUITY` (shares; `symbol` is the ticker and `amount` is the number of shares) / `CASH` (`symbol` is the currency and `amount` is the cash amount).<br>`EQUITY`（正股，`symbol` 为 ticker，`amount` 为股数）/ `CASH`（现金，`symbol` 为币种，`amount` 为金额）。<br>枚举: `EQUITY`, `CASH`<br>例: `EQUITY` |
| [].deliverables[].symbol | string |  | Ticker or currency.<br>ticker 或币种。<br>例: `NVDA` |
| [].deliverables[].amount | string |  | Number of shares or cash amount.<br>股数或现金金额。<br>例: `100` |

## Option Exercise Detail (USER_DATA)（行权详情 (USER_DATA)）

`GET /sapi/v1/equity/option/exercise/detail`

Query the result of a single exercise request. Provide at least one of `tranId` and `clientOrderId`; omitting both returns `-1102`. If both are provided, the lookup uses `clientOrderId` and `tranId` is ignored (the opposite of Option Order Detail).

Returns `497402 Order not found.` if no record is found or the record does not belong to the caller.

`errorCode` is returned only when `status` is `FAILED`.

查询单笔行权的处理结果。`tranId` 与 `clientOrderId` 至少提供一个（都不传返回 `-1102`）；两者都传时按 `clientOrderId` 查询，忽略 `tranId`（与「订单详情」相反）。

查不到、或该行权不属于调用方时返回 `497402 Order not found.`。

`errorCode` 仅在 `status` 为 `FAILED` 时返回。

权重: 1

Operation ID: `optionExerciseDetail`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| tranId | query | integer (int64) |  | Exercise transaction ID returned by Submit Option Exercise.<br>提交行权时返回的行权流水 ID。<br>例: `1234567890` |
| clientOrderId | query | string |  | Client ID used at submission.<br>提交时使用的客户端 ID。<br>例: `web_2c9c92b74f1e4a7c8f3b9e1a2d3c4b5a` |
| recvWindow | query | integer (int64) |  | The value cannot be greater than `60000`.<br>赋值不能大于 `60000`。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Timestamp in milliseconds.<br>时间戳（毫秒）。<br>例: `1770736694138` |

### 响应 200：Option Exercise Detail / 行权详情

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| tranId | integer (int64) |  | Exercise transaction ID.<br>行权流水 ID。<br>例: `1234567890` |
| clientOrderId | string |  | Client ID.<br>客户端 ID。<br>例: `web_2c9c92b74f1e4a7c8f3b9e1a2d3c4b5a` |
| symbol | string |  | OCC option contract symbol.<br>OCC 合约代码。<br>例: `NVDA260930C00100000` |
| underlyingSymbol | string |  | Underlying US-equity ticker.<br>标的美股 ticker。<br>例: `NVDA` |
| rootSymbol | string |  | OCC root symbol. Differs from `underlyingSymbol` for contracts adjusted by a corporate action (e.g. `GOOG1`).<br>OCC root。公司行动调整后的合约与 `underlyingSymbol` 不同（如 `GOOG1`）。<br>例: `NVDA` |
| contractType | string |  | `CALL` / `PUT`.<br>`CALL` / `PUT`。<br>例: `CALL` |
| strikePrice | string |  | Strike price.<br>行权价。<br>例: `100` |
| expirationDate | integer (int64) |  | Expiration date as the millisecond timestamp of 12:00 ET on the expiration day. Convert in `America/New_York` and take the date part (see [General Info](/products/stock-options/general-info#numbers-and-timestamps)).<br>到期日当天 12:00 ET 的毫秒时间戳，请按美东时区取日期部分（见[基本信息](/products/stock-options/general-info#数值与时间格式)）。<br>例: `1790784000000` |
| requestedQty | string |  | Requested number of contracts.<br>申请行权张数。<br>例: `2` |
| status | string |  | `PROCESSING` / `SUCCESS` / `FAILED`.<br>`PROCESSING` / `SUCCESS` / `FAILED`。<br>例: `SUCCESS` |
| requestedTime | integer (int64) |  | Submission time (ms).<br>提交时间（毫秒）。<br>例: `1790704800000` |
| updateTime | integer (int64) |  | Last update time (ms).<br>最后更新时间（毫秒）。<br>例: `1790766761000` |
| optionEventId | string |  | Settlement event ID of the option leg; can be used with Option Settlement Event Detail.<br>期权腿的结算事件 ID，可用于查询「结算事件详情」。<br>例: `a7f3c2e1-4b5d-4e8f-9c0a-1b2c3d4e5f60` |
| underlyingEventId | string |  | Settlement event ID of the underlying-share leg.<br>正股腿的结算事件 ID。<br>例: `c9d8e7f6-a5b4-4c3d-8e2f-1a0b9c8d7e6f` |
| multiplier | string |  | Premium multiplier. Order cost = price × quantity × multiplier.<br>权利金乘数，订单成本 = price × quantity × multiplier。<br>例: `100` |
| errorCode | string |  | Error code on failure; one of the option business error codes in [Error Code](/products/stock-options/error-code). Returned only when `status` is `FAILED`.<br>失败时的错误码，取值见[错误代码](/products/stock-options/error-code)中的期权业务码。仅 `status` 为 `FAILED` 时返回。<br>例: `497505` |

```json
{
  "tranId": 1234567890,
  "clientOrderId": "web_2c9c92b74f1e4a7c8f3b9e1a2d3c4b5a",
  "symbol": "NVDA260930C00100000",
  "underlyingSymbol": "NVDA",
  "rootSymbol": "NVDA",
  "contractType": "CALL",
  "strikePrice": "100",
  "expirationDate": 1790784000000,
  "requestedQty": "2",
  "status": "SUCCESS",
  "requestedTime": 1790704800000,
  "updateTime": 1790766761000,
  "optionEventId": "a7f3c2e1-4b5d-4e8f-9c0a-1b2c3d4e5f60",
  "underlyingEventId": "c9d8e7f6-a5b4-4c3d-8e2f-1a0b9c8d7e6f",
  "multiplier": "100"
}
```

## Option Exercise History (USER_DATA)（行权历史 (USER_DATA)）

`GET /sapi/v1/equity/option/exercise/history`

Paged exercise history.

分页查询行权历史。

权重: 1

Operation ID: `optionExerciseHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| status | query | string |  | Comma-separated status filter: `PROCESSING` / `SUCCESS` / `FAILED`.<br>逗号分隔的状态过滤：`PROCESSING` / `SUCCESS` / `FAILED`。<br>例: `SUCCESS,FAILED` |
| startTime | query | integer (int64) |  | Start time (ms).<br>开始时间（毫秒）。<br>例: `1790600000000` |
| endTime | query | integer (int64) |  | End time (ms).<br>结束时间（毫秒）。<br>例: `1790800000000` |
| current | query | integer |  | Page number. Default `1`.<br>页码，默认 `1`。<br>例: `1` |
| size | query | integer |  | Page size. Default `20`, max `100`.<br>每页大小，默认 `20`，最大 `100`。<br>例: `20` |
| recvWindow | query | integer (int64) |  | The value cannot be greater than `60000`.<br>赋值不能大于 `60000`。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Timestamp in milliseconds.<br>时间戳（毫秒）。<br>例: `1770736694138` |

### 响应 200：Option Exercise History / 行权历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| total | integer (int64) |  | Total number of records.<br>记录总数。<br>例: `1` |
| page | integer |  | Current page number.<br>当前页码。<br>例: `1` |
| size | integer |  | Current page size.<br>当前页大小。<br>例: `20` |
| rows | object[] |  | Exercise records.<br>行权记录。 |
| rows[].tranId | integer (int64) |  | Exercise transaction ID.<br>行权流水 ID。<br>例: `1234567890` |
| rows[].clientOrderId | string |  | Client ID.<br>客户端 ID。<br>例: `web_2c9c92b74f1e4a7c8f3b9e1a2d3c4b5a` |
| rows[].symbol | string |  | OCC option contract symbol.<br>OCC 合约代码。<br>例: `NVDA260930C00100000` |
| rows[].underlyingSymbol | string |  | Underlying US-equity ticker.<br>标的美股 ticker。<br>例: `NVDA` |
| rows[].rootSymbol | string |  | OCC root symbol. Differs from `underlyingSymbol` for contracts adjusted by a corporate action (e.g. `GOOG1`).<br>OCC root。公司行动调整后的合约与 `underlyingSymbol` 不同（如 `GOOG1`）。<br>例: `NVDA` |
| rows[].contractType | string |  | `CALL` / `PUT`.<br>`CALL` / `PUT`。<br>例: `CALL` |
| rows[].strikePrice | string |  | Strike price.<br>行权价。<br>例: `100` |
| rows[].expirationDate | integer (int64) |  | Expiration date as the millisecond timestamp of 12:00 ET on the expiration day. Convert in `America/New_York` and take the date part (see [General Info](/products/stock-options/general-info#numbers-and-timestamps)).<br>到期日当天 12:00 ET 的毫秒时间戳，请按美东时区取日期部分（见[基本信息](/products/stock-options/general-info#数值与时间格式)）。<br>例: `1790784000000` |
| rows[].requestedQty | string |  | Requested number of contracts.<br>申请行权张数。<br>例: `2` |
| rows[].status | string |  | `PROCESSING` / `SUCCESS` / `FAILED`.<br>`PROCESSING` / `SUCCESS` / `FAILED`。<br>例: `SUCCESS` |
| rows[].requestedTime | integer (int64) |  | Submission time (ms).<br>提交时间（毫秒）。<br>例: `1790704800000` |

## Option Settlement Event History (USER_DATA)（结算事件历史 (USER_DATA)）

`GET /sapi/v1/equity/option/event/history`

Query option settlement events — the settlement outcome of a contract: exercise, assignment or expiry (expired worthless), along with the shares / cash delivered and the collateral released. Sorted by event time in descending order.

These records are on a settlement basis, separate from orders and trades.

**Cursor pagination.** Omit `lastId` on the first page, then pass the `nextLastId` from the previous page until `hasMore` is `false`.

查询期权结算事件，记录合约的结算结果：行权、被指派、到期作废，以及随之交割的股票 / 现金与释放的抵押品。按事件时间倒序。

这是结算口径的流水，与订单、成交是不同的记录。

**游标分页。** 首页不传 `lastId`，之后传上一页返回的 `nextLastId`，直到 `hasMore` 为 `false`。

权重: 1

Operation ID: `optionSettlementEventHistory`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| underlyingSymbol | query | string |  | Underlying US-equity ticker filter.<br>标的美股 ticker 过滤。<br>例: `NVDA` |
| symbol | query | string |  | OCC contract symbol filter. If both `symbol` and `underlyingSymbol` are sent, `symbol` takes precedence.<br>OCC 合约代码过滤；与 `underlyingSymbol` 同时传时以 `symbol` 为准。<br>例: `NVDA260930C00100000` |
| eventType | query | string |  | Comma-separated event type filter: `EXERCISE` / `ASSIGNMENT` / `EXPIRY`, case-insensitive.<br>逗号分隔的事件类型过滤：`EXERCISE` / `ASSIGNMENT` / `EXPIRY`，大小写不敏感。<br>例: `EXERCISE,ASSIGNMENT` |
| startTime | query | integer (int64) |  | Start of the event time (`eventTime`) filter (ms).<br>按事件时间（`eventTime`）过滤的开始时间（毫秒）。<br>例: `1790700000000` |
| endTime | query | integer (int64) |  | End of the event time (`eventTime`) filter (ms).<br>按事件时间（`eventTime`）过滤的结束时间（毫秒）。<br>例: `1790900000000` |
| lastId | query | integer (int64) |  | Cursor returned by the previous page. Omit on the first page.<br>上一页返回的游标，首页不传。<br>例: `10086` |
| size | query | integer |  | Page size. Default `20`, max `100`.<br>每页大小，默认 `20`，最大 `100`。<br>例: `20` |
| recvWindow | query | integer (int64) |  | The value cannot be greater than `60000`.<br>赋值不能大于 `60000`。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Timestamp in milliseconds.<br>时间戳（毫秒）。<br>例: `1770736694138` |

### 响应 200：Option Settlement Event History / 结算事件历史

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| rows | object[] |  | Event records.<br>事件记录。 |
| rows[].eventId | string |  | Event ID; use it with Option Settlement Event Detail.<br>事件 ID，用于查询「结算事件详情」。<br>例: `a7f3c2e1-4b5d-4e8f-9c0a-1b2c3d4e5f60` |
| rows[].eventType | string |  | `EXERCISE` / `ASSIGNMENT` / `EXPIRY`.<br>`EXERCISE`（行权）/ `ASSIGNMENT`（被指派）/ `EXPIRY`（到期作废）。<br>枚举: `EXERCISE`, `ASSIGNMENT`, `EXPIRY`<br>例: `EXERCISE` |
| rows[].status | string |  | Event status. Only settled events are returned, so the value is always `Completed`.<br>事件状态。只返回已完成结算的事件，取值恒为 `Completed`。<br>例: `Completed` |
| rows[].symbol | string |  | OCC option contract symbol.<br>OCC 合约代码。<br>例: `NVDA260930C00100000` |
| rows[].underlyingSymbol | string |  | Underlying US-equity ticker.<br>标的美股 ticker。<br>例: `NVDA` |
| rows[].contractType | string |  | `CALL` / `PUT`.<br>`CALL` / `PUT`。<br>例: `CALL` |
| rows[].contracts | string |  | Number of contracts, **signed**: positive for long, negative for short. (Option Settlement Event Detail returns the absolute value.)<br>涉及张数，**带符号**：多头为正、空头为负（结算事件详情返回绝对值）。<br>例: `2` |
| rows[].expirationDate | integer (int64) |  | Expiration date as the millisecond timestamp of 12:00 ET on the expiration day. Convert in `America/New_York` and take the date part (see [General Info](/products/stock-options/general-info#numbers-and-timestamps)).<br>到期日当天 12:00 ET 的毫秒时间戳，请按美东时区取日期部分（见[基本信息](/products/stock-options/general-info#数值与时间格式)）。<br>例: `1790784000000` |
| rows[].strikePrice | string |  | Strike price.<br>行权价。<br>例: `100` |
| rows[].shareDelta | string |  | Net change in underlying shares (signed). Not returned for `EXPIRY` events, or for events on adjusted contracts that deliver more than one stock (see `deliverables`).<br>正股股数净变动（带符号）；`EXPIRY` 事件、或交割多只股票的调整合约事件不返回（见 `deliverables`）。<br>例: `200` |
| rows[].deliverables | object[] |  | Assets actually delivered. Empty array when nothing is delivered.<br>实际交割的资产。无交割时为空数组。 |
| rows[].deliverables[].type | string |  | Present on cash legs only: `OPEXC` (exercise cash) / `OPASN` (assignment cash) / `OPCSH` (cash settlement).<br>仅现金腿返回：`OPEXC`（行权现金）/ `OPASN`（被指派现金）/ `OPCSH`（现金结算）。<br>枚举: `OPEXC`, `OPASN`, `OPCSH`<br>例: `OPEXC` |
| rows[].deliverables[].symbol | string |  | Ticker for the share leg, currency for the cash leg.<br>正股腿为 ticker，现金腿为币种。<br>例: `USDC` |
| rows[].deliverables[].amount | string |  | Signed amount: positive = received, negative = paid. Number of shares for the share leg.<br>带符号的数量：收入为正、付出为负。正股腿为股数。<br>例: `-20000` |
| rows[].eventTime | integer (int64) |  | Event time (ms).<br>事件时间（毫秒）。<br>例: `1790766760000` |
| hasMore | boolean |  | Whether there is a next page.<br>是否还有下一页。<br>例: `False` |
| nextLastId | integer (int64) |  | Cursor for the next page.<br>下一页游标。<br>例: `10086` |

```json
{
  "rows": [
    {
      "eventId": "b8e4d3f2-6c5a-4b9e-8d7c-2f1e0a9b8c7d",
      "eventType": "EXPIRY",
      "status": "Completed",
      "symbol": "NVDA260930P00090000",
      "underlyingSymbol": "NVDA",
      "contractType": "PUT",
      "contracts": "-1",
      "expirationDate": 1790784000000,
      "strikePrice": "90",
      "deliverables": [],
      "eventTime": 1790852710000
    },
    {
      "eventId": "a7f3c2e1-4b5d-4e8f-9c0a-1b2c3d4e5f60",
      "eventType": "EXERCISE",
      "status": "Completed",
      "symbol": "NVDA260930C00100000",
      "underlyingSymbol": "NVDA",
      "contractType": "CALL",
      "contracts": "2",
      "expirationDate": 1790784000000,
      "strikePrice": "100",
      "shareDelta": "200",
      "deliverables": [
        {
          "symbol": "NVDA",
          "amount": "200"
        },
        {
          "type": "OPEXC",
          "symbol": "USDC",
          "amount": "-20000"
        }
      ],
      "eventTime": 1790766760000
    }
  ],
  "hasMore": false,
  "nextLastId": 10086
}
```

## Option Settlement Event Detail (USER_DATA)（结算事件详情 (USER_DATA)）

`GET /sapi/v1/equity/option/event/detail`

Full detail of a single settlement event, including the settlement basis and collateral release. Returns `-1102` if `eventId` does not exist or does not belong to the caller.

All fields of the history endpoint are included, with two differences: `contracts` is an absolute value, and `eventTime` is the time the settlement record was created.

For an `EXPIRY` event, `settlementKind`, `cashDirection`, `amount` and `shareDelta` are not returned. For an `EXPIRY` event on a short position (covered call / cash-secured put), `collateralRelease` lists the collateral released.

单条结算事件的完整明细，含结算口径与抵押品释放。`eventId` 不存在或不属于调用方时返回 `-1102`。

包含历史接口的全部字段，两处口径不同：`contracts` 为绝对值；`eventTime` 为结算记录的生成时间。

`EXPIRY` 事件不返回 `settlementKind`、`cashDirection`、`amount`、`shareDelta`；空头（covered call / cash-secured put）的 `EXPIRY` 事件通过 `collateralRelease` 返回释放的抵押品。

权重: 1

Operation ID: `optionSettlementEventDetail`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| eventId | query | string | 是 | Event ID from Option Settlement Event History.<br>事件 ID，来自「结算事件历史」。<br>例: `a7f3c2e1-4b5d-4e8f-9c0a-1b2c3d4e5f60` |
| recvWindow | query | integer (int64) |  | The value cannot be greater than `60000`.<br>赋值不能大于 `60000`。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Timestamp in milliseconds.<br>时间戳（毫秒）。<br>例: `1770736694138` |

### 响应 200：Option Settlement Event Detail / 结算事件详情

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| eventId | string |  | Event ID; use it with Option Settlement Event Detail.<br>事件 ID，用于查询「结算事件详情」。<br>例: `a7f3c2e1-4b5d-4e8f-9c0a-1b2c3d4e5f60` |
| eventType | string |  | `EXERCISE` / `ASSIGNMENT` / `EXPIRY`.<br>`EXERCISE`（行权）/ `ASSIGNMENT`（被指派）/ `EXPIRY`（到期作废）。<br>枚举: `EXERCISE`, `ASSIGNMENT`, `EXPIRY`<br>例: `EXERCISE` |
| status | string |  | Event status. Only settled events are returned, so the value is always `Completed`.<br>事件状态。只返回已完成结算的事件，取值恒为 `Completed`。<br>例: `Completed` |
| symbol | string |  | OCC option contract symbol.<br>OCC 合约代码。<br>例: `NVDA260930C00100000` |
| underlyingSymbol | string |  | Underlying US-equity ticker.<br>标的美股 ticker。<br>例: `NVDA` |
| contractType | string |  | `CALL` / `PUT`.<br>`CALL` / `PUT`。<br>例: `CALL` |
| contracts | string |  | Number of contracts, **absolute value** (unsigned), unlike the history endpoint.<br>涉及张数，**绝对值**（不带符号），与历史接口不同。<br>例: `2` |
| expirationDate | integer (int64) |  | Expiration date as the millisecond timestamp of 12:00 ET on the expiration day. Convert in `America/New_York` and take the date part (see [General Info](/products/stock-options/general-info#numbers-and-timestamps)).<br>到期日当天 12:00 ET 的毫秒时间戳，请按美东时区取日期部分（见[基本信息](/products/stock-options/general-info#数值与时间格式)）。<br>例: `1790784000000` |
| strikePrice | string |  | Strike price.<br>行权价。<br>例: `100` |
| shareDelta | string |  | Net change in underlying shares (signed). Not returned for `EXPIRY` events, or for events on adjusted contracts that deliver more than one stock (see `deliverables`).<br>正股股数净变动（带符号）；`EXPIRY` 事件、或交割多只股票的调整合约事件不返回（见 `deliverables`）。<br>例: `200` |
| deliverables | object[] |  | Assets actually delivered. Empty array when nothing is delivered.<br>实际交割的资产。无交割时为空数组。 |
| deliverables[].type | string |  | Present on cash legs only: `OPEXC` (exercise cash) / `OPASN` (assignment cash) / `OPCSH` (cash settlement).<br>仅现金腿返回：`OPEXC`（行权现金）/ `OPASN`（被指派现金）/ `OPCSH`（现金结算）。<br>枚举: `OPEXC`, `OPASN`, `OPCSH`<br>例: `OPEXC` |
| deliverables[].symbol | string |  | Ticker for the share leg, currency for the cash leg.<br>正股腿为 ticker，现金腿为币种。<br>例: `USDC` |
| deliverables[].amount | string |  | Signed amount: positive = received, negative = paid. Number of shares for the share leg.<br>带符号的数量：收入为正、付出为负。正股腿为股数。<br>例: `-20000` |
| eventTime | integer (int64) |  | Time the settlement record was created (ms).<br>结算记录的生成时间（毫秒）。<br>例: `1790766761000` |
| settlementKind | string |  | Settlement method: `PHYSICAL` (physical delivery) / `CASH` (cash settlement) / `MIXED` (both). Not returned for `EXPIRY` events.<br>结算方式：`PHYSICAL`（实物交割）/ `CASH`（现金结算）/ `MIXED`（两者兼有）。`EXPIRY` 事件不返回。<br>枚举: `PHYSICAL`, `CASH`, `MIXED`<br>例: `PHYSICAL` |
| underlyingPrice | string |  | Reference price of the underlying when the event was generated, for display only; it is not used in the settlement calculation. Not returned if unavailable.<br>事件生成时的正股参考价，仅供展示，不参与结算计算；取不到时不返回。<br>例: `123.45` |
| cashDirection | string |  | Cash direction: `DEBIT` / `CREDIT`. Not returned for `EXPIRY` events.<br>现金方向：`DEBIT`（扣款）/ `CREDIT`（入账）。`EXPIRY` 事件不返回。<br>枚举: `DEBIT`, `CREDIT`<br>例: `DEBIT` |
| amount | string |  | Net cash amount (absolute value); see `cashDirection` for the direction. Not returned for `EXPIRY` events.<br>现金净额（绝对值），方向见 `cashDirection`。`EXPIRY` 事件不返回。<br>例: `20000` |
| collateralRelease | object[] |  | Only for `EXPIRY` events on short positions (covered call / cash-secured put): collateral released back to the user, e.g. the cash of a cash-secured put (strike × contracts × multiplier).<br>仅空头（covered call / cash-secured put）的 `EXPIRY` 事件：到期作废时释放回用户的抵押品，如 cash-secured put 的抵押现金（行权价 × 张数 × 乘数）。 |
| collateralRelease[].symbol | string |  | Asset released.<br>释放的资产。<br>例: `USDC` |
| collateralRelease[].amount | string |  | Amount released.<br>释放数量。<br>例: `9000` |
| updatedTime | integer (int64) |  | Last update time (ms).<br>最后更新时间（毫秒）。<br>例: `1790766761000` |

```json
{
  "eventId": "a7f3c2e1-4b5d-4e8f-9c0a-1b2c3d4e5f60",
  "eventType": "EXERCISE",
  "status": "Completed",
  "symbol": "NVDA260930C00100000",
  "underlyingSymbol": "NVDA",
  "contractType": "CALL",
  "contracts": "2",
  "expirationDate": 1790784000000,
  "strikePrice": "100",
  "shareDelta": "200",
  "deliverables": [
    {
      "symbol": "NVDA",
      "amount": "200"
    },
    {
      "type": "OPEXC",
      "symbol": "USDC",
      "amount": "-20000"
    }
  ],
  "eventTime": 1790766761000,
  "settlementKind": "PHYSICAL",
  "underlyingPrice": "123.45",
  "cashDirection": "DEBIT",
  "amount": "20000",
  "updatedTime": 1790766761000
}
```

## Create / Renew Listen Key (USER_STREAM)（创建 / 续期 Listen Key (USER_STREAM)）

`POST /sapi/v1/equity/option/listenKey`

Create or renew the user data stream `listenKey`.

- **Valid for 1 hour.** Calling again renews it (resets to 1 hour) and returns the **same** key; renewing every 30 minutes is recommended. After expiry, a new key is issued and you must resubscribe with it.
- **Options and stocks share one key.** The key is issued per user, not per asset class. This endpoint and `/sapi/v1/equity/listenKey` return the same key; calling either is enough.
- Use the key to subscribe to the [Order Report V2 Stream](/catalog/advanced-trading-stock-option-trading/api/ws-streams/user-streams).

创建或续期用户数据流 `listenKey`。

- **有效期 1 小时。** 重复调用即续期（重置为 1 小时），返回**同一个** key；建议每 30 分钟调用一次。过期后再调用会签发新 key，需用新 key 重新订阅。
- **期权与美股共用同一个 key。** 按用户签发，不分品类。本接口与 `/sapi/v1/equity/listenKey` 返回的是同一个 key，任调其一即可。
- 拿到 key 后订阅[订单回报 V2 流](/catalog/advanced-trading-stock-option-trading/api/ws-streams/user-streams)。

权重: 1

Operation ID: `createRenewListenKey`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| X-MBX-APIKEY | header | string | 是 | An API Key is required to access this endpoint and must be included in the request headers. To create an API Key, refer to: [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).<br>访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。<br>例: `API_KEY` |
| recvWindow | query | integer (int64) |  | The value cannot be greater than `60000`.<br>赋值不能大于 `60000`。<br>例: `5000` |
| timestamp | query | integer (int64) | 是 | Timestamp in milliseconds.<br>时间戳（毫秒）。<br>例: `1770736694138` |

### 响应 200：Create / Renew Listen Key / 创建 / 续期 Listen Key

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| listenKey | string |  | User data stream session identifier.<br>用户数据流会话标识。<br>例: `3f9a1c2e-7b4d-4e8a-9c61-0d2f5b7e8a13` |