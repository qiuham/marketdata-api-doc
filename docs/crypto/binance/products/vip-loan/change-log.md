---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/vip-loan/change-log
api_type: Changelog
updated_at: 2026-11-23 18:28:27.405482
---

# Change Log

## 2026-10-15

- Updated VIP Loan rate limits (already in effect). All limits are per account:
  - `POST /sapi/v1/loan/vip/borrow`: 1 request per second.
  - `POST /sapi/v1/loan/vip/repay`: 1 request per second.
  - `GET /sapi/v1/loan/vip/repay/history`: 1 request per second, shared with repayment history
    queries on the Binance website.
  - `GET /sapi/v1/loan/vip/interestRateHistory`: 1 request per second.
  - `GET /sapi/v1/loan/vip/request/data`: changed from 5 to 1 request per second.
  - `GET /sapi/v1/loan/vip/request/interestRate`: changed from 5 to 1 request per second.

---

## 2026-10-08

- Updated `GET /sapi/v1/loan/vip/repay/history`:
  - Added `repayPrincipal` and `repayInterest` fields to the response to provide principal/interest
    breakdown per repayment record.

---

## 2026-10-07

- VIP Loan now supports Simple Earn Flexible assets as collateral:
  - `POST /sapi/v1/loan/vip/borrow` and `POST /sapi/v1/loan/vip/fixed/borrow` - `collateralCoin`
    accepts `<ASSET>-Earn` (e.g. `USDT-Earn`), which must be sent together with its Spot asset (e.g.
    `USDT,USDT-Earn`). Sending `<ASSET>-Earn` without its Spot asset returns `-10213`.
  - `GET /sapi/v1/loan/vip/ongoing/orders` and `GET /sapi/v1/loan/vip/request/data` -
    `collateralCoin` in the response may include `<ASSET>-Earn` entries.

---

## 2026-06-15

- New endpoints for VIP Loans:
  - `GET /sapi/v1/loan/vip/fixed/market` - Query VIP Loan Fixed Rate Market.
  - `POST /sapi/v1/loan/vip/fixed/borrow` - VIP Loan Fixed Rate Borrow.

---

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

## 2024-11-27

- New endpoints for VIP Loans
  - `GET /sapi/v1/loan/vip/interestRateHistory`: Check VIP Loan Interest Rate History
  - `GET /sapi/v1/loan/vip/accruedInterest`: Check VIP Loan interest record

---

## 2023-10-11

- New endpoint for VIP Loans:
  - `GET /sapi/v1/loan/vip/request/interestRate`: Get Borrow Interest Rate

---

## 2023-09-22

- Changes to VIP loan Endpoint:
  - `GET /sapi/v1/loan/vip/loanable/data`: add new response fields
    `_flexibleDailyInterestRate`,`_flexibleYearlyInterestRate`
  - `GET /sapi/v1/loan/vip/ongoing/orders`: add new response fields
    `loanDate`，`loanRate`，`loanTerm`，`expirationTime`

---

## 2023-09-18

- Changes to Margin Endpoint `GET /sapi/v1/margin/isolated/transfer`:
  - Add request field `type`
  - Delete request field `transFrom`,`transTo`

---

## 2023-08-18

- Update endpoints for VIP Loan:
  - `POST /sapi/v1/loan/vip/borrow`: add field `isFlexibleRate` to borrow using flexible rate loan

---

## 2023-07-14

- New endpoints for VIP Loan:
  - `POST /sapi/v1/loan/vip/renew`: VIP Loan Renew

---

## 2023-04-20

- Update endpoints for VIP Loans:
  - `GET /sapi/v1/loan/vip/ongoing/orders`: add fields `totalCollateralValueAfterHaircut` and
    `lockedCollateralValue`

---

## 2022-11-29

- New endpoint for VIP Loan:
  - `GET /sapi/v1/loan/vip/collateral/account`: Check Locked Value of VIP Collateral Account

---

## 2022-11-14

- New endpoints for VIP Loan:
  - `GET /sapi/v1/loan/vip/ongoing/orders`: Get VIP Loan Ongoing Orders
  - `POST /sapi/v1/loan/vip/repay`: VIP Loan Repay
  - `GET /sapi/v1/loan/vip/repay/history`: Get VIP Loan Repayment History

---

# 更新日志

## 2026-10-15

- 更新 VIP 借币接口频率限制（已生效），以下均为每账户限制：
  - `POST /sapi/v1/loan/vip/borrow`：每秒 1 次。
  - `POST /sapi/v1/loan/vip/repay`：每秒 1 次。
  - `GET /sapi/v1/loan/vip/repay/history`：每秒 1 次，与币安网页端的还款记录查询共用额度。
  - `GET /sapi/v1/loan/vip/interestRateHistory`：每秒 1 次。
  - `GET /sapi/v1/loan/vip/request/data`：由每秒 5 次调整为每秒 1 次。
  - `GET /sapi/v1/loan/vip/request/interestRate`：由每秒 5 次调整为每秒 1 次。

---

## 2026-10-08

- 更新 `GET /sapi/v1/loan/vip/repay/history`：
  - 响应中新增 `repayPrincipal` 和 `repayInterest` 字段，提供每笔还款的本金/利息明细。

---

## 2026-10-07

- VIP 借币支持使用活期理财（Simple Earn Flexible）资产作为抵押：
  - `POST /sapi/v1/loan/vip/borrow` 和 `POST /sapi/v1/loan/vip/fixed/borrow` - `collateralCoin`
    支持传入 `<ASSET>-Earn`（如 `USDT-Earn`），且必须同时传入对应的现货币种（如
    `USDT,USDT-Earn`）。仅传入 `<ASSET>-Earn` 而未传入对应现货币种时，返回 `-10213`。
  - `GET /sapi/v1/loan/vip/ongoing/orders` 和 `GET /sapi/v1/loan/vip/request/data` - 响应中的
    `collateralCoin` 可能包含 `<ASSET>-Earn`。

---

## 2026-06-15

- 新增 VIP 借币接口：
  - `GET /sapi/v1/loan/vip/fixed/market` - 查询 VIP 借币固定利率市场。
  - `POST /sapi/v1/loan/vip/fixed/borrow` - VIP 借币固定利率借款。

---

## 2025-12-26

### 时效性通知

- **以下有关于REST API变更将在 2026-01-15 07:00 UTC 发生:** <br>
  调用需要签名的接口时，请在计算签名之前对 payload 进行百分比编码（percent-encode）。不符合此顺序的请求将被拒绝，并返回错误代码
  [`-1022 签名不正确`](./error-code.md#-1022-invalid_signature)。请检查并相应地更新您代码中的签名逻辑部分。

### REST API

- 更新了 REST API 文档中有关于 [签名请求示例](./general-info.md#post-apiv3order-的签名示例) 的部分。

---

## 2024-11-27

- 新增 VIP 借币接口:
  - `GET /sapi/v1/loan/vip/interestRateHistory`: 查询借币利率
  - `GET /sapi/v1/loan/vip/accruedInterest`: 查询利息记录

---

## 2023-10-11

- 新增 VIP 借币:
  - `GET /sapi/v1/loan/vip/request/interestRate`: 查询借币利率

---

## 2023-09-22

- VIP 借币接口改动：
  - `GET /sapi/v1/loan/vip/loanable/data`: 新增返回字段`_flexibleDailyInterestRate`，`_flexibleYearlyInterestRate`
  - `GET /sapi/v1/loan/vip/ongoing/orders`: 新增返回字段`loanDate`，`loanRate`，`loanTerm`，`expirationTime`

---

## 2023-09-18

- VIP 借币接口改动：
  - 新增入参`type`
  - 移除入参`transFrom`，`transTo`

---

## 2023-08-18

- 更新 VIP 借币接口：
  - `POST /sapi/v1/loan/vip/borrow`: 增加参数`isFlexibleRate`以支持浮动利率借贷

---

## 2023-07-14

- 新增 VIP 借币接口：
  - `POST /sapi/v1/loan/vip/renew`: VIP 借币续期

---

## 2023-04-20

- 更新 VIP 借币接口：
  - `GET /sapi/v1/loan/vip/ongoing/orders`：增加字段`totalCollateralValueAfterHaircut` 和
    `lockedCollateralValue`

---

## 2022-11-29

- 添加 VIP 借币接口：
  - `GET /sapi/v1/loan/vip/collateral/account`: 查询 VIP 子账户冻结抵押物金额

---

## 2022-11-14

- 添加 VIP 借币接口：
  - `GET /sapi/v1/loan/vip/ongoing/orders`：查询 VIP 借币借款中订单
  - `POST /sapi/v1/loan/vip/repay`：VIP 借币还款
  - `GET /sapi/v1/loan/vip/repay/history`：查询 VIP 借币还款记录历史