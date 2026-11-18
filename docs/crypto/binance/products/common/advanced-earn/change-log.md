---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/common/advanced-earn/change-log
api_type: Changelog
updated_at: 2026-11-18 18:40:44.750342
---

# Change Log

## 2026-08-31

- Dual Investment
  - Removed `POST /sapi/v1/dci/product/auto_compound/edit-status` (Change Auto-Compound status).
    This endpoint is retired; the auto-compound setting can no longer be toggled via API and must be
    managed in the Binance Web UI.
  - Removed the `autoCompoundPlan` request parameter from `POST /sapi/v1/dci/product/subscribe`
    (Subscribe Dual Investment products). The auto-compound setting is no longer configurable at
    subscription time via API.

---

## 2026-03-23

- Dual Investment
  - `GET /sapi/v1/dci/product/positions` - Added `subscriptionTime` field in the response.

---

## 2025-12-26

### Time-sensitive Notice

- **The following change to REST API will occur at approximately 2026-01-15 07:00 UTC:** <br>When
  calling endpoints that require signatures, percent-encode payloads before computing signatures.
  Requests that do not follow this order will be rejected with
  [`-1022 INVALID_SIGNATURE`](/products/advanced-earn/error-code#-1022-invalid_signature). Please
  review and update your signing logic accordingly.

### REST API

- Updated documentation for REST API regarding
  [Signed Endpoints examples for placing an order](/products/advanced-earn/general-info#signed-endpoint-examples-for-post-apiv3order).

---

## 2025-12-02

- New Endpoints for Discount Buy

---

## 2024-02-23

- New Endpoints for Dual-Investment:
  - `GET /sapi/v1/dci/product/list`: Get Dual Investment product list
  - `POST /sapi/v1/dci/product/subscribe`: Subscribe Dual Investment products
  - `GET /sapi/v1/dci/product/positions`: Get Dual Investment positions (batch)
  - `GET /sapi/v1/dci/product/accounts`: Check Dual Investment accounts
  - `POST /sapi/v1/dci/product/auto_compound/edit-status`: Change Auto-Compound status

---

# 更新日志

## 2026-08-31

- 双币投资
  - 移除
    `POST /sapi/v1/dci/product/auto_compound/edit-status`（改变自动复投状态）。该接口已下线，用户无法再通过 API 切换自动复投状态，需在 Binance 网页端手动设置。
  - 移除 `POST /sapi/v1/dci/product/subscribe`（申购双币产品）请求参数中的
    `autoCompoundPlan`。申购时不再支持通过 API 设置自动复投。

---

## 2026-03-23

- 双币投资
  - `GET /sapi/v1/dci/product/positions` - 在响应中新增 `subscriptionTime` 字段。

---

## 2025-12-26

### 时效性通知

- **以下有关于REST API变更将在 2026-01-15 07:00 UTC 发生:** <br>
  调用需要签名的接口时，请在计算签名之前对 payload 进行百分比编码（percent-encode）。不符合此顺序的请求将被拒绝，并返回错误代码
  [`-1022 签名不正确`](/products/advanced-earn/error-code#-1022-invalid_signature)。请检查并相应地更新您代码中的签名逻辑部分。

### REST API

- 更新了 REST API 文档中有关于
  [签名请求示例](/products/advanced-earn/general-info#signed-endpoint-examples-for-post-apiv3order)
  的部分。

---

## 2025-12-02

- 新增折价买币接口

---

## 2024-02-23

- 新增双币投资接口:
  - `GET /sapi/v1/dci/product/list`: 获得双币产品列表
  - `POST /sapi/v1/dci/product/subscribe`: 申购双币产品
  - `GET /sapi/v1/dci/product/positions`: 获得双币产品持仓状态
  - `GET /sapi/v1/dci/product/accounts`: 查询双币产品账户
  - `POST /sapi/v1/dci/product/auto_compound/edit-status`: 改变自动复投状态