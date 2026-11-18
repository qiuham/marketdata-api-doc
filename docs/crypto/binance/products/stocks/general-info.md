---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/stocks/general-info
api_type: Guide
updated_at: 2026-11-18 01:55:17.574286
---

# General Info

This module documents the Stocks Trading REST API. Base URL, HMAC / Ed25519 signing, timestamps,
`recvWindow`, rate limits, and the sapi error envelope are identical to other SAPI endpoint families
— see the root [General Info](../common/sapi/general-info.md) for those.

This page lists only what is specific to the Stocks Trading module.

## Disclaimer Prerequisite

Before placing orders, the account must accept the US equity disclaimer via
`POST /account/disclaimer`. Orders placed before acceptance are rejected with `486410` (_Please sign
the trading disclaimer before placing an order_).

## Rate Limits

In addition to the shared SAPI weight / IP limits, the following endpoints carry a per-UID
request-rate cap:

| Endpoint                 | Limit                    |
| ------------------------ | ------------------------ |
| `POST /order/place`      | 200 requests / min (UID) |
| `POST /tokenized/mint`   | 50 requests / min (UID)  |
| `POST /tokenized/redeem` | 50 requests / min (UID)  |

## URL Prefix

All endpoints in this module share the prefix:

```
/sapi/v1/equity/
```

## Symbol Format

- `symbol` is always a plain US-equity ticker, UPPERCASE.
- Valid: `AAPL`, `NVDA`, `TSLA`, `SPY`, `QQQ`.
- Invalid: `EQ_AAPL`, `AAPLUSDT`, `aapl`.
- Tickers are resolved against the active-symbol list. Unknown-ticker behavior is endpoint-specific:
  `/order/place` and `/tokenized/mint` return `-26004`; `/market/exchangeInfo` returns an empty
  `symbols` array; `/market/quote` returns an empty response body.

## Quote Asset

- Default is `USDC` when `quoteAsset` is omitted in a `/order/place` request.
- The service enforces a server-side allow-set; values outside the allow-set are rejected.

## Prices

- All price fields are quoted in **USD** implicitly.
- Limit prices are capped at **2 decimal places**; orders with deeper precision are rejected at
  validation.

## Timestamps

- All timestamp fields in requests and responses use **milliseconds since Unix epoch**.
- `timestamp` in each signed request is the caller's current time; `recvWindow` applies the same as
  other SAPI endpoints (default 5000 ms, max 60000 ms).

## Enum Contract

- All enum string values are **UPPERCASE** on both request and response (`BUY` / `SELL`, `MARKET` /
  `LIMIT`, `FILLED` / `CANCELED`, `RTH` / `EXTENDED` / `24H`).
- See [Common Definition](./common-definition.md) for the full enum sets.

## Fees

- For LIMIT BUY orders, the service automatically computes the commission fee and includes it in the
  funds locked at placement time. Callers submit `price` and `quantity` only — no `fee` field is
  exposed on the request surface.
- Realized commission fees are reflected in the `fee` field of the order / trade history and order
  detail responses.

---

# 基本信息

本模块 REST API 的 Base URL、HMAC /
Ed25519 签名、时间戳、`recvWindow`、限频、SAPI 错误包络等与其他 SAPI 接口族完全一致，详见根级
[基本信息](../common/sapi/general-info_zh-CN.md)。

本页仅列出股票交易模块特有的约定。

## 免责声明前置条件

下单前，账户必须通过 `POST /account/disclaimer` 接受美股免责声明。未接受前下单会被拒绝，返回
`486410`（_下单前请先签署交易免责声明_）。

## 频率限制

除共享的 SAPI 权重 / IP 限制外，以下接口另有 per-UID 的请求频率上限：

| 接口                     | 限额                 |
| ------------------------ | -------------------- |
| `POST /order/place`      | 200 次 / 分钟（UID） |
| `POST /tokenized/mint`   | 50 次 / 分钟（UID）  |
| `POST /tokenized/redeem` | 50 次 / 分钟（UID）  |

## URL 前缀

本模块所有接口共享前缀：

```
/sapi/v1/equity/
```

## Symbol 格式

- `symbol` 一律为**大写美股 ticker**。
- 合法示例：`AAPL`、`NVDA`、`TSLA`、`SPY`、`QQQ`。
- 非法示例：`EQ_AAPL`、`AAPLUSDT`、`aapl`。
- 服务端维护上架 symbol 列表。未知 ticker 的行为因端点而异：`/order/place`、`/tokenized/mint` 返回
  `-26004`；`/market/exchangeInfo` 返回空 `symbols` 数组；`/market/quote` 返回空响应体。

## 报价资产（Quote Asset）

- `/order/place` 中 `quoteAsset` 省略时默认为 `USDC`。
- 服务端维护允许集合，提交不在集合内的值会被拒绝。

## 价格

- 所有价格字段**隐式以 USD 计价**。
- 限价单 `price` 最多 **2 位小数**，精度超出会在校验阶段被拒。

## 时间戳

- 请求与响应中所有时间戳字段均为 **Unix epoch 毫秒数**。
- 签名请求中的 `timestamp` 为客户端当前时间；`recvWindow` 与其他 SAPI 接口一致（默认 5000
  ms，最大 60000 ms）。

## 枚举契约

- 所有枚举字符串值在请求与响应中**一律 UPPERCASE**（`BUY` / `SELL`、`MARKET` / `LIMIT`、`FILLED` /
  `CANCELED`、`RTH` / `EXTENDED` / `24H`）。
- 完整枚举值集合参见 [通用枚举定义](./common-definition_zh-CN.md)。

## 手续费

- LIMIT BUY 下单时，服务端自动计算手续费并在下单时一并冻结；请求仅需提交 `price` +
  `quantity`，**无需**传入 `fee` 字段。
- 实际结算手续费在订单历史、订单详情、成交历史响应的 `fee` 字段中返回。