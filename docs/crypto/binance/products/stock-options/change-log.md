---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/stock-options/change-log
api_type: Changelog
updated_at: 2026-11-25 18:28:40.714321
---

# Change Log

The latest update: 2026-11-18

## 2026-11-18

### Initial release

- Stock Option Trading API launched under `/sapi/v1/equity/option/*`, with 18 REST endpoints:
  - Market Data: Option Expirations, Option Contracts, Option Exchange Info.
  - Trade: Place Option Order, Cancel Option Order, Cancel All Option Orders, Submit Option
    Exercise.
  - User Data: Current Open Option Orders, Option Order History, Option Order Detail, Option Trade
    History, Option Positions, Exercisable Options, Option Exercise Detail, Option Exercise History,
    Option Settlement Event History, Option Settlement Event Detail.
  - User Data Streams: Create / Renew Listen Key.
- Option order updates are pushed on the `<listenKey>@orderReportV2` user data stream.

---

# 更新日志

最新更新：2026-11-18

## 2026-11-18

### 首次发布

- 股票期权交易 API 上线，位于 `/sapi/v1/equity/option/*`，共 18 个 REST 接口：
  - 合约数据：到期日列表、合约列表、合约交易规则。
  - 交易：下单、撤单、全部撤单、提交行权。
  - 用户数据：当前挂单、订单历史、订单详情、成交历史、持仓查询、可行权合约、行权详情、行权历史、结算事件历史、结算事件详情。
  - 用户数据流：创建 / 续期 Listen Key。
- 期权订单更新通过 `<listenKey>@orderReportV2` 用户数据流推送。