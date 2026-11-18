---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/spot-block-matching/change-log
api_type: Changelog
updated_at: 2026-11-18 18:28:03.389272
---

# Changelog

## 2025-12-26

### Time-sensitive Notice

- **The following change to REST API will occur at approximately 2026-01-15 07:00 UTC:** <br>When
  calling endpoints that require signatures, percent-encode payloads before computing signatures.
  Requests that do not follow this order will be rejected with
  [`-1022 INVALID_SIGNATURE`](./error-code.md#-1022-invalid_signature). Please review and update
  your signing logic accordingly.

### REST API

- Updated documentation for REST API regarding
  [Signed Endpoints examples for placing an order](./general-info.md#signed-endpoint-examples-for-post-apiv3order).

---

## 2025-06-27

- New endpoint for Spot Block Matching:
  - `POST /sapi/v1/block-match/order/cancel` Order Cancel
  - `POST /sapi/v1/block-match/order/extend` Extend Order Validity Period by Adding 30 Minutes to
    the Current Time
  - `POST /sapi/v1/block-match/order/place` Spot block match Place order, The order is valid for 30
    minutes and will automatically expire if not executed.
  - `POST /sapi/v1/block-match/order/take` Accept order, Complete Transaction
  - `POST /sapi/v1/block-match/order/query-open-order` Query User's Open Orders
  - `POST /sapi/v1/block-match/order/query-order-history` Query User's Order History
  - `POST /sapi/v1/block-match/symbols` Return Trading Symbols Supported by Block Match

---

# 更新日志

## 2025-12-26

### 时效性通知

- **以下有关于REST API变更将在 2026-01-15 07:00 UTC 发生:** <br>
  调用需要签名的接口时，请在计算签名之前对 payload 进行百分比编码（percent-encode）。不符合此顺序的请求将被拒绝，并返回错误代码
  [`-1022 签名不正确`](./error-code.md#-1022-invalid_signature)。请检查并相应地更新您代码中的签名逻辑部分。

### REST API

- 更新了 REST API 文档中有关于 [签名请求示例](./general-info.md#post-apiv3order-的签名示例) 的部分。

---

## 2025-06-27

- New endpoint for Spot Block Matching:
  - `POST /sapi/v1/block-match/order/cancel` 取消订单
  - `POST /sapi/v1/block-match/order/extend` 在当前时间基础上增加 30 分钟，延长订单有效期
  - `POST /sapi/v1/block-match/order/place` 现货匹配下单，订单有效期为 30 分钟，如不执行将自动失效
  - `POST /sapi/v1/block-match/order/take` 接受订单，完成交易
  - `POST /sapi/v1/block-match/order/query-open-order` 查询用户的未结订单
  - `POST /sapi/v1/block-match/order/query-order-history` 查询用户的订单历史记录
  - `POST /sapi/v1/block-match/symbols` 返回支持的交易对