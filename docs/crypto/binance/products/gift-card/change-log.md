---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/gift-card/change-log
api_type: Changelog
updated_at: 2026-11-27 18:31:35.720180
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

## 2024-09-09

- The gift card limit is updated to:
  - Monthly creation volume: 4,200,000 USDC / month / account
  - Monthly creation quantity: 6,000 Gift Cards / month / account

---

## 2024-04-08

- Update Gift Card Endpoint:
  - `POST /sapi/v1/giftcard/createCode`: add response field `expiredTime`
  - `POST /sapi/v1/giftcard/buyCode`: add response field `expiredTime`

---

## 2023-08-02

- Effective from 21 Aug 2023, a 1% transaction fee will apply when you buy or create gift cards in
  Binance directly. The following endpoints are impacted:
  - `POST /sapi/v1/giftcard/createCode`
  - `POST /sapi/v1/giftcard/buyCode`

---

## 2023-07-20

- As per
  [the announcement](https://www.binance.com/en/support/announcement/updates-on-the-creation-of-gift-cards-transferring-of-crypto-via-gift-cards-16b0d3ad544b464889d37d2cfdc2a692),
  effective from 20 July 2023, creating gift cards is limited only to entity accounts which have
  passed KYB verification. The following endpoints are impacted:
  - `POST /sapi/v1/giftcard/createCode`
  - `POST /sapi/v1/giftcard/buyCode`

---

## 2022-10-15

- New endpoints for Binance Code:
  - `POST /sapi/v1/giftcard/buyCode`: For buying a fixed-value Binance Code.
  - `GET /sapi/v1/giftcard/buyCode/token-limit`: To verify which tokens are available for you to
    purchase fixed-value gift cards as mentioned in section 2 and its’ limitation.

---

## 2022-05-05

- New endpoint for Binance Code:
  - `GET /sapi/v1/giftcard/cryptography/rsa-public-key` to fetch RSA public key.
- Update endpoint for Binance Code:
  - `POST /sapi/v1/giftcard/redeemCode`: new optional parameter `externalUid`. Each external unique
    ID represents a unique user on the partner platform. The function helps you to identify the
    redemption behavior of different users.

---

## 2022-1-21

- New endpoints for Binance Code:
  - `POST /sapi/v1/giftcard/createCode` to create a Binance Code.
  - `POST /sapi/v1/giftcard/redeemCode` to redeem a Binance Code.
  - `GET /sapi/v1/giftcard/verify` to verify a Binance Code.

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

## 2024-09-09

- 礼品卡额度更新为：
  - 每月制卡金额上限：4,200,000 USDC / 月 / 账户
  - 每月制卡数量上限：6,000 张 / 月 / 账户

---

## 2024-04-08

- 更新礼品卡接口:
  - `POST /sapi/v1/giftcard/createCode`: 增加返回字段`expiredTime`
  - `POST /sapi/v1/giftcard/buyCode`: 增加返回字段`expiredTime`

---

## 2023-08-02

- 自 2023 年 8 月 21 日起，创建礼品卡将增收 1% 的服务费。下列接口受影响：
  - `POST /sapi/v1/giftcard/createCode`
  - `POST /sapi/v1/giftcard/buyCode`

---

## 2023-07-20

- 根据此[公告](https://www.binance.com/zh-TC/support/announcement/%E9%97%9C%E6%96%BC%E5%89%B5%E5%BB%BA%E7%A6%AE%E5%93%81%E5%8D%A1%E5%92%8C%E8%BD%89%E5%B8%B3%E5%8A%A0%E5%AF%86%E8%B2%A8%E5%B9%A3%E7%9A%84%E6%9B%B4%E6%96%B0-16b0d3ad544b464889d37d2cfdc2a692)，自 2023 年 7 月 20 日起，创建功能仅允许已通过 KYB 的企业帐户使用。下列接口受影响：
  - `POST /sapi/v1/giftcard/createCode`
  - `POST /sapi/v1/giftcard/buyCode`

---

## 2022-10-15

- 添加币安码接口：
  - `POST /sapi/v1/giftcard/buyCode`：用于购买一个币安码
  - `GET /sapi/v1/giftcard/buyCode/token-limit`：用来查看你所支付的数字货币，可以购买的面额与数量限制

---

## 2022-05-05

- 新增 Binance Code 接口:
  - `GET /sapi/v1/giftcard/cryptography/rsa-public-key`，以查询 RSA public key。
- 更新 Binance Code 接口:
  - `POST /sapi/v1/giftcard/redeemCode`: 新增参数
    `externalUid`。每个外部用户 ID 代表合作伙伴平台上的某个用户。该功能帮助您识别不同用户的兑现行为。

## 2022-1-21

---

- 新增币安码接口:
  - `POST /sapi/v1/giftcard/createCode` 以支持创建币安码
  - `POST /sapi/v1/giftcard/redeemCode` 以支持兑现币安码
  - `GET /sapi/v1/giftcard/verify` 以支持验证币安码