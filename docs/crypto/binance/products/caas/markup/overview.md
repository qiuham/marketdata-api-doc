---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/caas/markup/overview
api_type: Guide
updated_at: 2026-11-20 18:43:00.318047
---

# Markup

The standard CAAS model works on a revenue share system, described in
[this Binance announcement](https://www.binance.com/en/support/announcement/detail/c7154e8282b8499ea7983bd715ed8959).

Should a CAAS partner wish to have a markup model instead of the revenue share system, they may
apply through [link@binance.com](mailto:link@binance.com). Markups are approved on a case-by-case
basis only, and this model is available on the **spot order book only**.

The markup model lets a CAAS partner mark up their trades above 0.10% maker/taker (M/T) on spot and
take the excess.

**Example — revenue share at 40%**

The partner charges the end client 0.10% M/T. 0.04% is returned to the partner, and 0.06% goes to
Binance.

**Example — markup**

The partner marks up to 0.30% M/T. 0.10% goes to Binance, and 0.20% goes to the partner.

:::note

Revenue share and markup **cannot be combined**.

:::

## How it works

The Markup API lets a CAAS partner set the commission its end users pay above Binance's own fee, by
grouping members into fee groups, and to report on the markup earned.

| Area       | Endpoints                                                                 |
| ---------- | ------------------------------------------------------------------------- |
| Fee groups | Create, update, query, and delete fee groups; assign and unassign members |
| Reporting  | Query markup trade aggregations and markup trade details                  |

## Where to go next

| If you need                                             | Go to                                                                   |
| ------------------------------------------------------- | ----------------------------------------------------------------------- |
| Endpoints, signing, and rate limits                     | [Getting Started](/products/caas/markup/getting-started)                |
| The end-to-end integration flow                         | [Integration Guide](/products/caas/markup/integration-guide)            |
| The Markup endpoint reference                           | [Markup REST API](/catalog/vip-and-institutional-vip-caas/api/rest-api) |
| CAAS base endpoints, limits, and error payloads in full | [API basics](/products/caas/basics/1.base-urls)                         |
| Sub-account and API key setup                           | [Getting Started](/products/caas/getting-started)                       |
| Markup release history                                  | [Binance Link Change Log](/products/binance-link/change-log)            |

---

# 加点（Markup）

加点（Markup）API 允许 CAAS 合作方在币安自身费率之上设置其终端用户所支付的佣金，方式是将成员归入费率组，并对已赚取的加点进行报表查询。

| 功能   | 接口                                             |
| ------ | ------------------------------------------------ |
| 费率组 | 创建、更新、查询、删除费率组；分配与取消分配成员 |
| 报表   | 查询加点交易聚合数据与加点交易明细               |

## 接口地址、签名与访问限制

加点接口为 **https://api.binance.com** 上的 `/sapi/v1/vip/caas/commission/*`，因此遵循
[API basics](/products/caas/basics/1.base-urls)
中的主 API 规则——基础接口地址、请求签名、错误响应，以及 `/sapi/*` 的访问限制。

加点特有的两点：

- 所有加点接口的鉴权类型均为 **`TRADE`**，因此全部属于 `SIGNED`（签名）接口，需要提供有效的 API
  Key 以及 `signature` 与 `timestamp`。加点接口中没有公开（无需鉴权）的接口。
- API Key 必须属于您的**主账户**，而非子账户。

由于这些是 `/sapi/*` 接口，每个接口都有各自独立的访问限制，而非共享同一额度；超出限制时返回
`429`，且**不适用** `418` 的 IP 封禁升级机制。参见
[`/api/*` 与 `/sapi/*` 的差异](/products/caas/basics/4.rate-limits#api-and-sapi-differ--check-which-family-you-are-calling)。

## 后续参考

| 如果您需要                                   | 请前往                                                                |
| -------------------------------------------- | --------------------------------------------------------------------- |
| 加点接口参考文档                             | [加点 REST API](/catalog/vip-and-institutional-vip-caas/api/rest-api) |
| 完整的 CAAS 基础接口地址、访问限制与错误响应 | [API basics](/products/caas/basics/1.base-urls)                       |
| 子账户与 API Key 设置                        | [Getting Started](/products/caas/getting-started)                     |
| 加点更新日志                                 | [Binance Link 更新日志](/products/binance-link/change-log)            |