---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/c2c/change-log
api_type: Changelog
updated_at: 2026-11-27 18:33:29.987907
---

# Change Log

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

## 2021-08-05

- New endpoint for C2C:
  - `GET /sapi/v1/c2c/orderMatch/listUserOrderHistory` to query user C2C trade history

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

## 2021-08-05

- 新增C2C接口:
  - `GET /sapi/v1/c2c/orderMatch/listUserOrderHistory` 以查询用户C2C交易历史记录