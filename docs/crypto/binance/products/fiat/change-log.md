---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/fiat/change-log
api_type: Changelog
updated_at: 2026-11-20 18:32:42.365820
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

## 2025-11-06

- New endpoint for Fiat:
  - `POST /sapi/v1/fiat/deposit`： Fiat deposit
  - `POST /sapi/v2/fiat/withdraw`: Fiat withdraw
  - `GET /sapi/v1/fiat/get-order-detail` Fiat order detail

---

## 2022-05-31

- Update endpoint for Fiat:
  - `GET /sapi/v1/fiat/orders`: Weight changes from UID(3000) to UID(90000)

---

## 2022-05-26

- Update endpoint for Fiat:
  - `GET /sapi/v1/fiat/orders`: Weight changes from IP(1) to UID(3000)

---

## 2021-07-27

- New endpoint for Fiat:
  - `GET /sapi/v1/fiat/orders` to query user fiat deposit and withdraw history
  - `GET /sapi/v1/fiat/payments` to query user fiat payments history

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

## 2025-11-06

- 新增法币接口:
  - `POST /sapi/v1/fiat/deposit`： 法币充值
  - `POST /sapi/v2/fiat/withdraw`: 法币提现
  - `GET /sapi/v1/fiat/get-order-detail` 获取订单详情

---

## 2022-05-31

- 更新法币接口：
  - `GET /sapi/v1/fiat/orders`： 权重自 UID(3000) 改至 UID(90000)

---

## 2022-05-26

- 更新法币接口：
  - `GET /sapi/v1/fiat/orders`： 权重自 IP(1) 改至 UID(3000)

---

## 2021-07-27

- 新增法币接口:
  - `GET /sapi/v1/fiat/orders` 以查询用户法币充值和提币历史记录
  - `GET /sapi/v1/fiat/payments` 以查询用户法币支付（买卖）历史记录