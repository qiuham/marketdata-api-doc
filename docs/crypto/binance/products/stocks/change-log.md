---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/stocks/change-log
api_type: Changelog
updated_at: 2026-11-24 18:28:42.644388
---

# Change Log

The latest update: 2026-11-24

## 2026-11-24

### New parameter `tokenizedAssetSettleWalletType`

- Added optional request parameter `tokenizedAssetSettleWalletType` (`MAIN` = Spot wallet, `CARD` =
  Funding wallet, default `CARD`) to choose the wallet the tokenized asset is settled in:
  - `POST /sapi/v1/equity/order/place` — wallet that receives the tokenized asset minted after the
    fill. Only applies when `side` = `BUY` and `tokenize` = `true`.
  - `POST /sapi/v1/equity/tokenized/mint` — wallet that receives the minted tokenized asset.
  - `POST /sapi/v1/equity/tokenized/redeem` — wallet the tokenized asset is deducted from.
- Added response field `tokenizedAssetSettleWalletType`, the settle wallet actually used, to:
  - `POST /sapi/v1/equity/tokenized/mint`
  - `POST /sapi/v1/equity/tokenized/redeem`
  - `GET /sapi/v1/equity/tokenized/history` (each element of `rows`)
  - `GET /sapi/v1/equity/tokenized/convert-status`

## 2026-11-18

### Order history price fields

- `GET /sapi/v1/equity/order/history` — `limitPrice` and `avgFilledPrice` are now both returned as
  reported by the broker, regardless of order type. Previously only one price field was populated
  per order type, so filled `LIMIT` orders had no `avgFilledPrice`, and stop-limit orders had
  neither price.

## 2026-11-12

### New fields for Price Stream

- `price` stream — added `lrc` (latest completed RTH close) and `prc` (previous RTH close relative
  to `lrc`) to `rates[]`. Clarified the descriptions of `pc` and `tc`.

## 2026-08-12

### Deprecated response fields removed

- `GET /sapi/v1/equity/trade/history` — removed `fee` from `rows`.
- `GET /sapi/v1/equity/order/detail` — removed `fee` from `trades`; top-level `fee` and
  `avgFilledPrice` are now documented as present only when the order has at least one fill.

## 2026-08-10

### New parameter for Equity Order Detail

- `GET /sapi/v1/equity/order/detail` — added `clientOrderId` as an alternative lookup key. Either
  `orderId` or `clientOrderId` must be provided. The response now includes `clientOrderId`.

## 2026-07-30

### Rate limit update

- `POST /sapi/v1/equity/tokenized/redeem` — UID rate limit increased from 50 to **200 requests /
  min**.

## 2026-07-20

### Initial release

Stocks Trading API (`/sapi/v1/equity/*`) goes live with 16 REST endpoints plus the user data and
market-data WebSocket streams.

**Market Data** (MARKET_DATA)

- `GET /sapi/v1/equity/market/exchangeInfo` — exchange trading rules and the list of tradable
  symbols; optional `symbol` filter.
- `GET /sapi/v1/equity/market/tokenized-assets` — list of tokenized assets with underlying equity
  symbol and multiplier.
- `GET /sapi/v1/equity/market/quote` — latest best bid / ask for a single ticker (5s server-side
  cache).

**Trade** (TRADE)

- `POST /sapi/v1/equity/order/place` — place a stock order. Supports all `LIMIT` / `MARKET` × `BUY`
  / `SELL` combinations, with `timeInForce` and `tradingSession`; optional `tokenize`. Rate limit
  200 requests / min (UID).
- `POST /sapi/v1/equity/order/cancel` — cancel a single order by `orderId`.
- `POST /sapi/v1/equity/order/cancel-all` — cancel all open orders for the caller.

**Trade** (USER_DATA)

- `GET /sapi/v1/equity/order/open-orders` — all unfinished (open) orders for the caller.
- `GET /sapi/v1/equity/order/history` — paged order history.
- `GET /sapi/v1/equity/order/detail` — single order + execution list.
- `GET /sapi/v1/equity/trade/history` — paged per-fill trade history.

**Tokenized** (TRADE)

- `POST /sapi/v1/equity/tokenized/mint` — mint a tokenized asset from underlying equity. Target
  tokenized asset is resolved server-side from `underlyingAsset`. Rate limit 50 requests / min
  (UID).
- `POST /sapi/v1/equity/tokenized/redeem` — redeem a tokenized asset back into the underlying.
  Target underlying is resolved server-side from `tokenizedAsset`. Rate limit 50 requests / min
  (UID).

**Tokenized** (USER_DATA)

- `GET /sapi/v1/equity/tokenized/history` — paged mint / redeem history (cursor pagination).
- `GET /sapi/v1/equity/tokenized/convert-status` — query a single mint / redeem request by
  `issuerRequestId`.

**Account** (TRADE)

- `POST /sapi/v1/equity/account/disclaimer` — sign / acknowledge the US equity disclaimer.

**User Data Streams** (USER_STREAM)

- `POST /sapi/v1/equity/listenKey` — create a new stock user-data-stream `listenKey`, or renew an
  existing one.
- WebSocket `{listenKey}@orderReport` — real-time push of the user's order state transitions
  (open-state updates and terminal notifications).

**WebSocket Streams** (public market data)

- WebSocket `price` — all-symbol latest-price snapshot, pushed every 3 seconds.
- WebSocket `{SYMBOL}@quote` — per-symbol best bid / ask, real-time with 200 ms per-symbol throttle.
- WebSocket `{SYMBOL}@kline_{interval}` — per-symbol candlesticks for `5m` / `1h` / `1d` / `1w` /
  `1M` intervals.
- WebSocket `calendar` — market-phase transitions (`PRE_MARKET` / `MARKET_OPEN` / `POST_MARKET` /
  `OVERNIGHT` / `MARKET_CLOSED`).
- WebSocket `{SYMBOL}@tradingStatus` — per-symbol trading-status events (halts, resumes, SSR, LULD).
- WebSocket `{SYMBOL}@tradability` — per-symbol tradable-direction changes.

---

# 更新日志

最新更新：2026-11-24

## 2026-11-24

### 新增参数 `tokenizedAssetSettleWalletType`

- 新增可选请求参数 `tokenizedAssetSettleWalletType`（`MAIN` = 现货钱包，`CARD` = 资金钱包，默认
  `CARD`），用于选择代币化资产的结算钱包：
  - `POST /sapi/v1/equity/order/place` — 订单成交后铸造的代币化资产所划入的钱包。仅在 `side` = `BUY`
    且 `tokenize` = `true` 时生效。
  - `POST /sapi/v1/equity/tokenized/mint` — 接收所铸造代币化资产的钱包。
  - `POST /sapi/v1/equity/tokenized/redeem` — 扣减代币化资产的钱包。
- 以下接口的响应新增字段 `tokenizedAssetSettleWalletType`，表示实际使用的结算钱包：
  - `POST /sapi/v1/equity/tokenized/mint`
  - `POST /sapi/v1/equity/tokenized/redeem`
  - `GET /sapi/v1/equity/tokenized/history`（`rows` 中的每个元素）
  - `GET /sapi/v1/equity/tokenized/convert-status`

## 2026-11-18

### 订单历史价格字段

- `GET /sapi/v1/equity/order/history` — `limitPrice` 与 `avgFilledPrice`
  均直接返回券商原值，不再区分订单类型。此前每种订单类型只返回其中一个价格字段，已成交的 `LIMIT`
  订单没有 `avgFilledPrice`，止损限价 / 止盈限价订单两个价格都没有。

## 2026-11-12

### 全量价格流新增字段

- `price` 流 — `rates[]` 新增 `lrc`（最近一个已完成 RTH 交易日收盘价）和 `prc`（`lrc`
  对应交易日的前一交易日收盘价）。同时修正 `pc`、`tc` 的字段说明。

## 2026-08-12

### 废弃响应字段移除

- `GET /sapi/v1/equity/trade/history` — 移除 `rows` 中的 `fee` 字段。
- `GET /sapi/v1/equity/order/detail` — 移除 `trades` 中的 `fee` 字段；顶层 `fee` 与 `avgFilledPrice`
  字段注明仅在订单至少有一笔成交时返回。

## 2026-08-10

### 订单详情接口新增参数

- `GET /sapi/v1/equity/order/detail` — 新增 `clientOrderId` 作为可选查询条件。`orderId` 与
  `clientOrderId` 必须提供其中一个。响应新增 `clientOrderId` 字段。

## 2026-07-30

### 频率限制更新

- `POST /sapi/v1/equity/tokenized/redeem` — UID 频率限制从 50 次/分钟提升至 **200 次/分钟**。

## 2026-07-20

### 首次发布

股票交易 API（`/sapi/v1/equity/*`）正式上线，首批 16 个 REST 接口，以及用户数据流与行情 WebSocket 推送。

**行情接口**（MARKET_DATA）

- `GET /sapi/v1/equity/market/exchangeInfo` — 交易规则与可交易 Symbol 列表；可选 `symbol` 过滤。
- `GET /sapi/v1/equity/market/tokenized-assets`
  — 全部代币化资产列表，包含标的美股 Symbol 与转换倍数。
- `GET /sapi/v1/equity/market/quote` — 查询单只美股最优买一 / 卖一实时报价（服务端 5 秒缓存）。

**交易接口**（TRADE）

- `POST /sapi/v1/equity/order/place` — 下一笔股票订单。支持 `LIMIT` / `MARKET` × `BUY` / `SELL`
  全组合，含 `timeInForce` 与 `tradingSession`；可选 `tokenize`。频率限制 200 次 / 分钟（UID）。
- `POST /sapi/v1/equity/order/cancel` — 按 `orderId` 撤销单笔订单。
- `POST /sapi/v1/equity/order/cancel-all` — 一键撤销调用方所有未成交订单。

**交易接口**（USER_DATA）

- `GET /sapi/v1/equity/order/open-orders` — 查询调用方全部未完成（挂单中）订单。
- `GET /sapi/v1/equity/order/history` — 分页订单历史。
- `GET /sapi/v1/equity/order/detail` — 单笔订单详情 + 成交明细。
- `GET /sapi/v1/equity/trade/history` — 分页逐笔成交历史。

**代币化接口**（TRADE）

- `POST /sapi/v1/equity/tokenized/mint` — 从标的股票铸造代币化资产，目标代币由服务端根据
  `underlyingAsset` 查找。频率限制 50 次 / 分钟（UID）。
- `POST /sapi/v1/equity/tokenized/redeem` — 赎回代币化资产换回标的股票，目标标的由服务端根据
  `tokenizedAsset` 查找。频率限制 50 次 / 分钟（UID）。

**代币化接口**（USER_DATA）

- `GET /sapi/v1/equity/tokenized/history` — 分页铸造 / 赎回转换历史。
- `GET /sapi/v1/equity/tokenized/convert-status` — 通过 `issuerRequestId` 查询铸造 / 赎回状态。

**账户接口**（TRADE）

- `POST /sapi/v1/equity/account/disclaimer` — 签署 / 确认美股免责声明。

**用户数据流**（USER_STREAM）

- `POST /sapi/v1/equity/listenKey` — 创建新的股票用户数据流 `listenKey`，或对已有 `listenKey` 续期。
- WebSocket `{listenKey}@orderReport` — 实时推送用户的订单状态变更（在途更新与终态通知）。

**WebSocket Streams**（公开行情）

- WebSocket `price` — 全量 symbol 最新价快照，固定每 3 秒推送。
- WebSocket `{SYMBOL}@quote` — 按 symbol 实时推送最优买一 / 卖一，内置 per-symbol 200 ms 限流。
- WebSocket `{SYMBOL}@kline_{interval}` — 按 symbol 推送 K 线，支持 `5m` / `1h` / `1d` / `1w` /
  `1M`。
- WebSocket `calendar` — 市场阶段切换通知（`PRE_MARKET` / `MARKET_OPEN` / `POST_MARKET` /
  `OVERNIGHT` / `MARKET_CLOSED`）。
- WebSocket `{SYMBOL}@tradingStatus` — 按 symbol 推送交易状态（停牌 / 恢复 / SSR / LULD）。
- WebSocket `{SYMBOL}@tradability` — 按 symbol 推送可交易方向变更。