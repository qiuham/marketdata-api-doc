---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/portfolio-account/change-log
api_type: Changelog
updated_at: 2026-11-28 18:29:18.429167
---

# Change Log

## 2026-11-26

- Renamed Fund Account to Portfolio Account across the documentation. The documentation moved from
  `/products/fund-account` to `/products/portfolio-account`, and the API Reference moved from
  `vip-and-institutional-fund-account` to `vip-and-institutional-portfolio-account`. Old URLs
  redirect to the new pages.
- Rewrote the Introduction and split it into pages: Introduction, Account Structure, Getting
  Started, Core Concepts, Basics, and Integration Guides for trading teams, Capital Connect listing
  and investors. Added an Error Codes page.
- Decommissioned the v1 endpoints, which are replaced by their v2 versions:
  - `GET /sapi/v1/vip/fund-info/fund-info-basic-info`
  - `GET /sapi/v1/vip/fund-info/fund-nav-info`
  - `GET /sapi/v1/vip/fund-info/fund-investor-his-info`
  - `GET /sapi/v1/capital-connect/redemption/calendar`
- Added new endpoints:
  - `POST /sapi/v2/portfolio-account/trading-team/change-api-sharing-switch`: Change API Sharing
    Switch
  - `GET /sapi/v2/portfolio-account/trading-team/api-sharing-status`: Query API Sharing Status
  - `GET /sapi/v1/portfolio-account/investor/portfolio-history-info`: Query Investor Portfolio
    History Info
  - `GET /sapi/v1/portfolio-account/investor/portfolio-realtime-asset-value`: Query Investor
    Portfolio Realtime Asset Value
- Updated request weights of the following endpoints: Query Portfolio Basic Info for Trading Team V2
  (1), Query Portfolio NAV History for Trading Team V2 (1), Query Investor Operation History for
  Trading Team V2 (1), Query Portfolio NAV History for Investor (600).

---

## 2026-08-28

- Added v2 Portfolio Account endpoints as breaking replacements for the v1 fund-info endpoints:
  Query Portfolio Basic Info for Trading Team V2, Query Portfolio NAV History for Trading Team V2,
  Query Investor Operation History for Trading Team V2, Redemption Calendar V2. The v1 endpoints
  remain callable and will be decommissioned in a future release.
- Added a new investor-facing endpoint, Query Portfolio NAV History for Investor.

---

## 2025-09-04

- Upload to API doc

---

---

# 更新日志

## 2026-11-26

- 在文档中将资金账户（Fund Account）统一更名为投资组合账户（Portfolio Account）。文档路径由
  `/products/fund-account` 迁移至 `/products/portfolio-account`，API 参考由
  `vip-and-institutional-fund-account` 迁移至
  `vip-and-institutional-portfolio-account`。旧链接会跳转到新页面。
- 重写概述页并拆分为多个页面：概述、账户结构、快速开始、核心概念、基础信息，以及面向交易团队、Capital
  Connect 上架和投资人的集成指南。新增错误码页面。
- 下线 v1 接口，由对应的 v2 接口替代：
  - `GET /sapi/v1/vip/fund-info/fund-info-basic-info`
  - `GET /sapi/v1/vip/fund-info/fund-nav-info`
  - `GET /sapi/v1/vip/fund-info/fund-investor-his-info`
  - `GET /sapi/v1/capital-connect/redemption/calendar`
- 新增接口：
  - `POST /sapi/v2/portfolio-account/trading-team/change-api-sharing-switch`：修改 API 数据共享开关
  - `GET /sapi/v2/portfolio-account/trading-team/api-sharing-status`：查询 API 数据共享状态
  - `GET /sapi/v1/portfolio-account/investor/portfolio-history-info`：查询投资组合操作历史（适用于投资人）
  - `GET /sapi/v1/portfolio-account/investor/portfolio-realtime-asset-value`：查询投资组合实时资产价值（适用于投资人）
- 更新以下接口的请求权重：查询投资组合基本信息（适用于交易团队）V2（1）、查询投资组合净值历史（适用于交易团队）V2（1）、查询投资人操作历史（适用于交易团队）V2（1）、查询投资组合净值历史（适用于投资人）（600）。

---

## 2026-08-28

- 新增 v2 版投资组合账户接口，作为 v1
  fund-info 系列接口的破坏性替代版本：查询投资组合基本信息（适用于交易团队）V2、查询投资组合净值历史（适用于交易团队）V2、查询投资人操作历史（适用于交易团队）V2、赎回日历V2。v1 接口目前仍可正常调用，将在后续版本中下线。
- 新增投资人专属接口 查询投资组合净值历史（适用于投资人）。

---

## 2025-09-04

- 上传至文档

---