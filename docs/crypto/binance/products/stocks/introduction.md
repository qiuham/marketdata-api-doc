---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/stocks/introduction
api_type: Guide
updated_at: 2026-11-22 18:27:44.566978
---

# Introduction

**Stocks Trading** — trade Stocks and ETFs with crypto.

The Stocks Trading API lets you trade US-listed equities programmatically through the SAPI endpoint
family. All endpoints live under the `/sapi/v1/equity/*` prefix.

## Supported Instruments

- **Stocks** — common shares of US-listed companies (NYSE / NASDAQ).
- **ETFs** — exchange-traded funds listed on US venues.

Both are traded through the same endpoints. In request and response payloads, the `symbol` field is
always a plain ticker — for example `AAPL`, `NVDA`, `TSLA`, `SPY`, `QQQ` — with no prefix.

## What's Included

| Group             | Endpoints                                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------------------- |
| Market Data       | Exchange Info, Tokenized Assets, Latest Quote                                                                 |
| Trade             | Place Order, Cancel Order, Cancel All Orders, Current Open Orders, Order History, Order Detail, Trade History |
| Tokenized         | Mint, Redeem, Convert History, Convert Status                                                                 |
| Account           | Sign US Equity Disclaimer                                                                                     |
| User Data Streams | Listen Key, Order Report                                                                                      |
| WebSocket Streams | Price, Quote, Kline, Calendar, Trading Status, Tradability                                                    |

## Defaults and Conventions

- **Base URL**: same as other SAPI endpoints (see root
  [General Info](../common/sapi/general-info.md)).
- **URL prefix**: `/sapi/v1/equity/*`.
- **Symbol**: plain uppercase ticker (`AAPL`, not `EQ_AAPL`).
- **Quote asset**: default `USDC`; the server-side allow-set controls which quote assets are
  accepted.
- **Prices**: quoted in USD.
- **Timestamps**: milliseconds since Unix epoch.
- **Enum string values**: always **UPPERCASE** on both request and response (`BUY` / `SELL`,
  `MARKET` / `LIMIT`, `FILLED` / `CANCELED`, …).
- **Signing**: same HMAC / Ed25519 scheme as other SAPI endpoints.

---

# 概览

**股票交易** —— 使用加密货币交易股票和 ETF。

股票交易 API 提供了通过 SAPI 渠道交易美股的能力，所有接口挂在 `/sapi/v1/equity/*` 前缀下。

## 支持的交易品种

- **股票（Stocks）** — NYSE / NASDAQ 上市的美股普通股。
- **ETF（交易所交易基金）** — 在美股交易所挂牌的 ETF。

两者共用同一套接口。请求与响应中的 `symbol` 字段统一使用美股 ticker——例如
`AAPL`、`NVDA`、`TSLA`、`SPY`、`QQQ`——不加任何前缀。

## 接口分组

| 分组               | 接口                                                         |
| ------------------ | ------------------------------------------------------------ |
| 行情接口           | 交易规则与 Symbol 列表、代币化资产列表、获取最新报价         |
| 交易接口           | 下单、撤单、全部撤单、当前挂单、订单历史、订单详情、成交历史 |
| 代币化             | 铸造、赎回、转换历史、转换状态                               |
| 账户接口           | 签署美股免责声明                                             |
| 用户数据流         | Listen Key、订单回报                                         |
| WebSocket 行情推送 | 全量价格、报价、K 线、市场阶段日历、交易状态、可交易方向     |

## 默认值与约定

- **Base URL**：与其他 SAPI 接口相同（详见根目录 [General Info](../common/sapi/general-info.md)）。
- **URL 前缀**：`/sapi/v1/equity/*`。
- **Symbol**：纯大写美股 ticker（`AAPL`，不带前缀）。
- **计价资产**：默认 `USDC`；服务端维护允许集合。
- **价格**：以 USD 报价。
- **时间戳**：Unix 纪元毫秒数。
- **枚举字符串值**：请求与响应中均为**大写**（`BUY` / `SELL`、`MARKET` / `LIMIT`、`FILLED` /
  `CANCELED` 等）。
- **签名**：与其他 SAPI 接口相同的 HMAC / Ed25519 方案。