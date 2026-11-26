---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/simple-earn/change-log
api_type: Changelog
updated_at: 2026-11-26 18:30:11.818228
---

# Change Log

## 2026-05-27

- Add new Yield Arena endpoint:
  - `GET /sapi/v1/earn/arena/activities` - Returns the list of Earn Yield Arena activities currently
    available to the user (`AIRDROP`, `LEADERBOARD`, `EVENT`). Supports an optional `lang` request
    header for localized `title` and `description`.

## 2026-03-09

- Changes to BFUSD endpoints:
  - `GET /sapi/v1/bfusd/quota` - New `subscriptionQuota` object in response with `leftQuota` field.

## 2025-12-26

### Time-sensitive Notice

- **The following change to REST API will occur at approximately 2026-01-15 07:00 UTC:** <br>When
  calling endpoints that require signatures, percent-encode payloads before computing signatures.
  Requests that do not follow this order will be rejected with
  [`-1022 INVALID_SIGNATURE`](error-code.md#-1022-invalid_signature). Please review and update your
  signing logic accordingly.

### REST API

- Updated documentation for REST API regarding
  [Signed Endpoints examples for placing an order](general-info.md#signed-endpoint-examples-for-post-apiv3order).

## 2025-10-27

- Increase BFUSD endpoints

## 2025-09-05

- Increase RWUSD endpoints

## 2025-09-02

- Update the file paths for Flexible and Locked products

## 2025-03-18

- Changes to Simple Earn endpoints:
  - `GET /sapi/v1/simple-earn/locked/subscriptionPreview` new fields in response `boostRewardAsset`,
    `estDailyRewardAmt`
  - `GET /sapi/v1/simple-earn/locked/list` new fields in response `boostRewardAsset`,`boostApr`,
    `boostEndTime`
  - `GET /sapi/v1/simple-earn/locked/position` new fields in response `boostRewardAsset`,`boostApr`,
    `totalBoostRewardAmt`
  - `GET /sapi/v1/simple-earn/locked/history/rewardsRecord` new fields in response `type`

## 2024-07-04

- Changes to Simple Earn endpoints:
  - `POST /sapi/v1/simple-earn/locked/subscribe` new parameter:`redeemTo`
  - `GET /sapi/v1/simple-earn/locked/position` new fields in response:`redeemTo`
  - `GET /sapi/v1/simple-earn/flexible/history/subscriptionRecord` new fields in
    response:`productId`
  - `GET /sapi/v1/simple-earn/locked/history/subscriptionRecord` new fields in response:`projectId`
  - `GET /sapi/v1/simple-earn/locked/history/redemptionRecord` new fields in
    response:`originalAmount`, `lossAmount`, `isComplete`, `rewardAsset`, `rewardAmt`,
    `extraRewardAsset`, `estExtraRewardAmt`
- Add New endpoint in Simple Earn：
  - `POST /sapi/v1/simple-earn/locked/setRedeemOption` Set the redeem option of Locked products to
    Flexible product or Spot wallet

## 2023-08-26

- Changes to Simple Earn endpoints:
  - `GET /sapi/v1/simple-earn/flexible/history/subscriptionRecord`: new fields in response:
    `sourceAccount`,`amtFromSpot`,`amtFromFunding`
  - `GET /sapi/v1/simple-earn/locked/history/subscriptionRecord`: new fields in response:
    `sourceAccount`，`amtFromSpot`,`amtFromFunding`
  - `GET /sapi/v1/simple-earn/flexible/history/redemptionRecord`: new fields in response
    `destAccount`
  - `POST /sapi/v1/simple-earn/flexible/subscribe`: new parameter `sourceAccount`
  - `POST /sapi/v1/simple-earn/locked/subscribe`: new parameter `sourceAccount`
  - `POST /sapi/v1/simple-earn/flexible/redeem`: new parameter `destAccount`

---

# 更新日志

## 2026-05-27

- 新增收益竞技场接口：
  - `GET /sapi/v1/earn/arena/activities` - 返回该用户当前可参与的理财收益竞技场活动列表（`AIRDROP`、`LEADERBOARD`、`EVENT`）。支持可选请求头
    `lang` 用于返回对应语言的 `title` 和 `description`。

## 2026-03-09

- 更新BFUSD接口:
  - `GET /sapi/v1/bfusd/quota` - 响应新增 `subscriptionQuota` 对象，包含 `leftQuota` 字段。

## 2025-12-26

### 时效性通知

- **以下有关于REST API变更将在 2026-01-15 07:00 UTC 发生:** <br>
  调用需要签名的接口时，请在计算签名之前对 payload 进行百分比编码（percent-encode）。不符合此顺序的请求将被拒绝，并返回错误代码
  [`-1022 签名不正确`](error-code_zh-CN.md#-1022-invalid_signature)。请检查并相应地更新您代码中的签名逻辑部分。

### REST API

- 更新了 REST API 文档中有关于 [签名请求示例](general-info_zh-CN.md#post-apiv3order-的签名示例)
  的部分。

## 2025-10-27

- 增加BFUSD接口

## 2025-09-05

- 增加RWUSD接口

## 2025-09-02

- 更新赚币活期和定期产品的接口文档路径

## 2025-03-18

- 更新赚币接口:
  - `GET /sapi/v1/simple-earn/locked/subscriptionPreview` 新增响应字段 `boostRewardAsset`,
    `estDailyRewardAmt`
  - `GET /sapi/v1/simple-earn/locked/list` 新增响应字段 `boostRewardAsset`,`boostApr`,
    `boostEndTime`
  - `GET /sapi/v1/simple-earn/locked/position` 新增响应字段 `boostRewardAsset`,`boostApr`,
    `totalBoostRewardAmt`
  - `GET /sapi/v1/simple-earn/locked/history/rewardsRecord` 新增响应字段 `type`

## 2024-07-04

- 更新赚币接口:
  - `POST /sapi/v1/simple-earn/locked/subscribe` 新增字段`redeemTo`
  - `GET /sapi/v1/simple-earn/locked/position` 新增响应字段`redeemTo`
  - `GET /sapi/v1/simple-earn/flexible/history/subscriptionRecord` 新增响应字段`productId`
  - `GET /sapi/v1/simple-earn/locked/history/subscriptionRecord` 新增响应字段`projectId`
  - `GET /sapi/v1/simple-earn/locked/history/redemptionRecord` 新增响应字段`originalAmount`,
    `lossAmount`, `isComplete`, `rewardAsset`, `rewardAmt`, `extraRewardAsset`, `estExtraRewardAmt`
- 新增赚币接口：
  - `POST /sapi/v1/simple-earn/locked/setRedeemOption` 设置定期产品到期赎回至活期产品或现货钱包

## 2023-08-26

- 更新赚币接口：
  - `GET /sapi/v1/simple-earn/flexible/history/subscriptionRecord`: 在响应中增加字段：`sourceAccount`，`amtFromSpot`，`amtFromFunding`
  - `GET /sapi/v1/simple-earn/locked/history/subscriptionRecord`:在响应中增加字段：`sourceAccount`，`amtFromSpot`，`amtFromFunding`
  - `GET /sapi/v1/simple-earn/flexible/history/redemptionRecord`:在响应中增加字段：`destAccount`
  - `POST /sapi/v1/simple-earn/flexible/subscribe`: 新增参数`sourceAccount`
  - `POST /sapi/v1/simple-earn/locked/subscribe`: 新增参数`sourceAccount`
  - `POST /sapi/v1/simple-earn/flexible/redeem`: 新增参数`destAccount`