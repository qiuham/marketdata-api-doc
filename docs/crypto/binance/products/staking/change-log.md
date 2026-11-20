---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/staking/change-log
api_type: Changelog
updated_at: 2026-11-20 18:30:18.244301
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

## 2025-10-27

- Update endpoint for ETH Staking:
  - `GET /sapi/v1/eth-staking/eth/quota` to inquire about the minimum amount and redeem period.

## 2025-09-09

- Added new endpoints related to Soft Staking.

## 2025-07-01

- Added new endpoints related to On-Chain Yields Locked Staking.

## 2024-12-3

- New endpoints for SOL Staking:
  - `GET /sapi/v1/sol-staking/sol/history/boostRewardsHistory` to inquire about SOL Staking Boost
    APR Airdrop Rewards history records.
  - `GET /sapi/v1/sol-staking/sol/history/unclaimedRewards` to inquire about SOL Staking unclaimed
    Boost APR Airdrop Rewards.
  - `POST /sapi/v1/sol-staking/sol/claim` to claim SOL Staking Boost APR Airdrop Rewards.
- Upgraded endpoints for SOL Staking:
  - `GET /sapi/v1/sol-staking/sol/history/rateHistory` to inquire about SOL Staking Boost APR rate
    history.

## 2024-10-15

- New endpoints for Staking:
  - `POST /sapi/v1/sol-staking/sol/stake` to stake SOL and get BNSOL.
  - `POST /sapi/v1/sol-staking/sol/redeem` to redeem BNSOL and get SOL.
  - `GET /sapi/v1/sol-staking/sol/history/stakingHistory` to inquire about SOL Staking subscription
    history records.
  - `GET /sapi/v1/sol-staking/sol/history/redemptionHistory` to inquire about SOL Staking redemption
    history records.
  - `GET /sapi/v1/sol-staking/sol/history/bnsolRewardsHistory` to inquire about SOL Staking rewards
    history records.
  - `GET /sapi/v1/sol-staking/sol/history/rateHistory` to inquire about SOL Staking exchange rate
    history.
  - `GET /sapi/v1/sol-staking/account` to get the total BNSOL account details.
  - `GET /sapi/v1/sol-staking/sol/quota` to inquire about product quota and details.

---

## 2023-12-22

- Binance will disable the following Staking SAPI endpoints at 2024-03-31 04:00:
  - `GET /sapi/v1/eth-staking/eth/history/wbethRewardsHistory`: add new endpoint to query WBETH
    income record
  - `POST /sapi/v2/eth-staking/eth/stake`: add new endpoint to stake ETH to get WBETH. Current v1
    endpoint `POST /sapi/v1/eth-staking/eth/stake` will be deprecated in the future, with the exact
    timing to be determined.
  - `GET /sapi/v2/eth-staking/account`: add new endpoint to query positions and 30-day earnings of
    staked ETH. Current v1 endpoint `GET /sapi/v1/eth-staking/account` will be deprecated in the
    future, with the exact timing to be determined.
  - `POST /sapi/v1/eth-staking/wbeth/unwrap`: delete this endpoint,
    `POST /sapi/v1/eth-staking/eth/redeem` is able to achieve same functionality
  - `POST /sapi/v1/eth-staking/eth/redeem`: Add new parameter `asset`, add new response
    fields`ethAmount`, `conversionRatio`
  - `GET /sapi/v1/eth-staking/eth/history/stakingHistory`: add new response fields
    `distributeAsset`, `distributeAmount`, `conversionRatio`
  - `GET /sapi/v1/eth-staking/eth/history/redemptionHistory` add new response fields `asset`,
    `distributeAsset`, `distributeAmount`, `conversionRatio`
  - `POST /sapi/v1/eth-staking/wbeth/wrap`: add new response fields `wbethAmount`, `exchangeRate`

---

## 2023-06-29

- Added multiple new endpoints related to ETH Staking in Staking.

---

## 2022-04-28

- New endpoints for Staking:
  - `GET /sapi/v1/staking/productList` to get Staking product list
  - `POST /sapi/v1/staking/purchase` to stake product
  - `POST /sapi/v1/staking/redeem` to redeem product
  - `GET /sapi/v1/staking/position` to get Staking product holding position
  - `GET /sapi/v1/staking/stakingRecord` to inquiry Staking history records
  - `POST /sapi/v1/staking/setAutoStaking` to set Auto Staking function
  - `GET /sapi/v1/staking/personalLeftQuota` to inquiry Staking left quota

---

# 更新日志

## 2025-12-26

### 时效性通知

- **以下有关于REST API变更将在 2026-01-15 07:00 UTC 发生:** <br>
  调用需要签名的接口时，请在计算签名之前对 payload 进行百分比编码（percent-encode）。不符合此顺序的请求将被拒绝，并返回错误代码
  [`-1022 签名不正确`](./error-code.md#-1022-invalid_signature)。请检查并相应地更新您代码中的签名逻辑部分。

### REST API

- 更新了 REST API 文档中有关于 [签名请求示例](./general-info.md#post-apiv3order-的签名示例) 的部分。

## 2025-10-27

- 更新 ETH Staking 的接口:
  - `GET /sapi/v1/eth-staking/eth/quota` 查询ETH质押的赎回周期和最小数量限制等参数。

## 2025-09-09

- 新增持币生息相关接口。

## 2025-07-01

- 新增链上赚币定期相关接口。

## 2024-12-3

- 新增 SOL Staking 的接口:
  - `GET /sapi/v1/sol-staking/sol/history/boostRewardsHistory` 查询 SOL质押Boost空投奖励历史记录。
  - `GET /sapi/v1/sol-staking/sol/history/unclaimedRewards` 查询 SOL质押未领取的Boost空投奖励。
  - `POST /sapi/v1/sol-staking/sol/claim` 领取 Boost空投奖励。
- 更新 SOL Staking 的接口:
  - `GET /sapi/v1/sol-staking/sol/history/rateHistory` 查询 SOL质押Boost空投奖励年利率。

## 2024-10-15

- 新增 Staking 接口:
  - `POST /sapi/v1/sol-staking/sol/stake`: 质押SOL并获得BNSOL。
  - `POST /sapi/v1/sol-staking/sol/redeem`: 赎回BNSOL并获得 SOL。
  - `GET /sapi/v1/sol-staking/sol/history/stakingHistory`: 查询SOL质押的申购历史记录。
  - `GET /sapi/v1/sol-staking/sol/history/redemptionHistory`: 查询SOL质押的赎回历史记录。
  - `GET /sapi/v1/sol-staking/sol/history/bnsolRewardsHistory`: 查询SOL质押的奖励历史记录。
  - `GET /sapi/v1/sol-staking/sol/history/rateHistory`: 查询SOL质押的汇率历史记录。
  - `GET /sapi/v1/sol-staking/account`: 获取BNSOL账户详情。
  - `GET /sapi/v1/sol-staking/sol/quota`: 查询产品配额和详细信息。

---

## 2023-12-22

- 更新 staking 接口:
  - `GET /sapi/v1/eth-staking/eth/history/wbethRewardsHistory`: 新增接口以查询 WBETH 收益记录
  - `POST /sapi/v2/eth-staking/eth/stake`: 新增接口质押 ETH 获得 WBETH。 现有 v1 接口`POST /sapi/v1/eth-staking/eth/stake`
    将被弃用, 具体时间待定
  - `GET /sapi/v2/eth-staking/account`: 新增接口查询已质押 ETH 的对应持仓和 30 天收益。现有 v1 接口`GET /sapi/v1/eth-staking/account`
    将被弃用, 具体时间待定
  - `POST /sapi/v1/eth-staking/wbeth/unwrap`: 移除本接口。`POST /sapi/v1/eth-staking/eth/redeem`已经支持相同功能
  - `POST /sapi/v1/eth-staking/eth/redeem`: 新增入参`asset`, 新增返回字段`ethAmount`,
    `conversionRatio`。
  - `GET /sapi/v1/eth-staking/eth/history/stakingHistory`: 新增返回字段 `distributeAsset`,
    `distributeAmount`, `conversionRatio`
  - `GET /sapi/v1/eth-staking/eth/history/redemptionHistory` 新增返回字段`asset`, `distributeAsset`,
    `distributeAmount`, `conversionRatio`
  - `POST /sapi/v1/eth-staking/wbeth/wrap`: 新增返回字段`wbethAmount`, `exchangeRate`

---

## 2023-06-29

- Staking 接口中新增一系列 ETH Staking 相关接口
- 新增杠杆接口：
  - `GET /sapi/v1/margin/dust`: 获取可以转换成 BNB 的小额资产列表
  - `POST /sapi/v1/margin/dust`: 把小额资产转换成 BNB
- 新增 VIP 借币接口(2023-06-30 生效)：
  - `POST /sapi/v1/loan/vip/borrow`: VIP 借币借款
  - `GET /sapi/v1/loan/vip/loanable/data`: 查询 VIP 借币可借币种数据
  - `GET /sapi/v1/loan/vip/collateral/data`: 查询 VIP 借币抵押币种数据
  - `GET /sapi/v1/loan/vip/request/data`: 查询申请状态

---

## 2022-04-28

- 新增 Staking 接口:
  - `GET /sapi/v1/staking/productList` 以查询 Staking 可锁仓产品列表
  - `POST /sapi/v1/staking/purchase` 以锁仓 Staking 产品
  - `POST /sapi/v1/staking/redeem` 以赎回 Staking 产品
  - `GET /sapi/v1/staking/position` 以查询 Staking 产品的持仓
  - `GET /sapi/v1/staking/stakingRecord`以查询锁仓产品的历史记录
  - `POST /sapi/v1/staking/setAutoStaking` 以设置 Staking 产品的自动续期
  - `GET /sapi/v1/staking/personalLeftQuota` 以查询个人锁仓限额