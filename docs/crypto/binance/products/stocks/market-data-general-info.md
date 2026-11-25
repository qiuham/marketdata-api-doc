---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/stocks/market-data-general-info
api_type: Guide
updated_at: 2026-11-25 18:28:22.451774
---

# Market Data — General Info

Market-data endpoints for the Stocks Trading module sit under:

```
/sapi/v1/equity/market/
```

All endpoints in this group are `MARKET_DATA` endpoints — they return real-time quote data and
market-phase information for US-listed equities. No signature is required.

- **Symbol** — plain uppercase US ticker (e.g. `AAPL`, `TSLA`), resolved against the active-symbol
  list. See the module [General Info](./general-info.md#symbol-format).
- **Prices** — quoted in USD.
- **Quote freshness** — values returned by `/market/quote` are at most ~5 seconds stale.

See each endpoint page for parameters and response shape.

---

# 行情接口基本信息

股票交易模块的行情类接口挂在：

```
/sapi/v1/equity/market/
```

本组接口均为 `MARKET_DATA` 接口——返回美股实时报价与市场阶段信息，不需要签名。

- **Symbol** — 大写美股 ticker（如 `AAPL`、`TSLA`），在上架 symbol 列表中解析。详见模块
  [基本信息](./general-info_zh-CN.md#symbol-格式)。
- **价格** — USD 计价。
- **报价时效性** — `/market/quote` 返回的数据最多延迟约 5 秒。

各接口参数与响应结构详见对应的接口页面。