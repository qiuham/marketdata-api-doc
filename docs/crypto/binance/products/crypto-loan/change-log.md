---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/crypto-loan/change-log
api_type: Changelog
updated_at: 2026-11-23 18:32:34.816822
---

# Change Log

## 2026-10-16

- The following SAPI endpoints have been retired and now return HTTP 404. They were kept for
  order-history queries after the Stable Rate retirement on 2024-11-05 and the Flexible Rate v2
  upgrade on 2024-02-27. Their documentation has been removed:
  - Stable Rate:
    - `GET /sapi/v1/loan/income`
    - `GET /sapi/v1/loan/borrow/history`
    - `GET /sapi/v1/loan/repay/history`
    - `GET /sapi/v1/loan/ltv/adjustment/history`
  - Flexible Rate (v1):
    - `GET /sapi/v1/loan/flexible/borrow/history`
    - `GET /sapi/v1/loan/flexible/repay/history`
    - `GET /sapi/v1/loan/flexible/ltv/adjustment/history`
- Flexible Rate v2 endpoints are not affected.

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

## 2024-12-20

- New endpoints for Flexible Loan: Collateral repayment is now available for flexible loan

* `POST/sapi/v2/loan/flexible/repay/collateral`
* `GET /sapi/v2/loan/flexible/repay/rate`
* `GET /sapi/v2/loan/flexible/liquidation/history`

## 2024-11-05

- Following the latest upgrade on Binance Loans （Stable Rate Loan）, Binance Loans has retired its
  SAPI endpoints for Stable Rate Loan as below(Stable Rate orders on VIP Loan are not impacted by
  this service update):
  - `GET /sapi/v1/loan/loanable/data`
  - `GET /sapi/v1/loan/collateral/data`
  - `POST /sapi/v1/loan/borrow`
  - `POST /sapi/v1/loan/repay`
  - `POST /sapi/v1/loan/adjust/ltv`
  - `POST /sapi/v1/loan/customize/margin_call`
  - `GET /sapi/v1/loan/ongoing/orders`

- In the meantime, Binance Loans will continue to maintain the following SAPI endpoints for stable
  loan history query:
  - `GET /sapi/v1/loan/income`
  - `GET /sapi/v1/loan/borrow/history`
  - `GET /sapi/v1/loan/ltv/adjustment/history`
  - `GET /sapi/v1/loan/repay/history`

## 2024-02-27

- Following the latest
  [upgrade](https://www.binance.com/en/support/announcement/binance-upgrades-binance-loans-flexible-rate-2024-02-27-d35942110b53480581773fc62a3e6eae)
  on Binance Loans
  - Binance Loans has added the following /v2 SAPI endpoints at 2024-02-27 08:00 (UTC). Users may
    utilize v2 SAPI endpoints to place, repay, and manage new Binance Loans (Flexible Rate) orders
    created after 2024-02-27 08:00 (UTC).
    - `POST /sapi/v2/loan/flexible/borrow`
    - `GET /sapi/v2/loan/flexible/ongoing/orders`
    - `GET /sapi/v2/loan/flexible/borrow/history`
    - `POST /sapi/v2/loan/flexible/repay`
    - `GET /sapi/v2/loan/flexible/repay/history`
    - `POST /sapi/v2/loan/flexible/adjust/ltv`
    - `GET /sapi/v2/loan/flexible/ltv/adjustment/history`
    - `GET /sapi/v2/loan/flexible/loanable/data`
    - `GET /sapi/v2/loan/flexible/collateral/data`

  - In addition, Binance Loans will be retiring its /v1 SAPI endpoints at the following timings:
    - At 2024-02-27 08:00 (UTC):
      - `POST /sapi/v1/loan/flexible/borrow`
      - `GET /sapi/v1/loan/flexible/loanable/data`
      - `GET /sapi/v1/loan/flexible/collateral/data`
    - At 2024-04-24 03:00 (UTC):
      - `GET /sapi/v1/loan/flexible/ongoing/orders`
      - `POST /sapi/v1/loan/flexible/repay`
      - `POST /sapi/v1/loan/flexible/adjust/ltv`

  - Binance Loans will also continue to maintain the following /v1 SAPI endpoints for users to check
    their Binance Loans (Flexible Rate) order history before 2024-02-27 08:00 (UTC).
    - `GET /sapi/v1/loan/flexible/borrow/history`
    - `GET /sapi/v1/loan/flexible/repay/history`
    - `GET /sapi/v1/loan/flexible/ltv/adjustment/history`

---

## 2023-08-26

- New endpoint for Crypto Loans:
  - `POST /sapi/v1/loan/flexible/borrow`: flexible Loan borrow
  - `GET /sapi/v1/loan/flexible/ongoing/orders`: get flexible loan ongoing orders
  - `GET /sapi/v1/loan/flexible/borrow/history`: Get flexible loan borrow history
  - `POST /sapi/v1/loan/flexible/repay`: flexible loan repay
  - `POST /sapi/v1/loan/flexible/repay/history`: Get flexible loan repayment history
  - `POST /sapi/v1/loan/flexible/adjust/ltv`: adjust flexible Loan adjust LTV
  - `GET /sapi/v1/loan/flexible/ltv/adjustment/history`: Get Flexible loan LTV adjustment history
  - `GET /sapi/v1/loan/flexible/loanable/data`: Get flexible loan assets data
  - `GET /sapi/v1/loan/flexible/collateral/data`: Get flexible loan collateral assets data

---

## 2023-02-21

- Adjusted endpoints for Crypto Loan:
  - `POST /sapi/v1/loan/borrow`: paramater `loanTerm` is restricted to 7 or 30

---

## 2022-11-01

- New endpoints for Crypto Loan:
  - `GET /sapi/v1/loan/loanable/data`: Get interest rate and borrow limit of loanable assets. The
    borrow limit is shown in USD value.
  - `GET /sapi/v1/loan/collateral/data`: Get LTV information and collateral limit of collateral
    assets. The collateral limit is shown in USD value.
  - `GET /sapi/v1/loan/repay/collateral/rate`: Get the the rate of collateral coin / loan coin when
    using collateral repay, the rate will be valid within 8 second.
  - `POST /sapi/v1/loan/customize/margin_call`: Customize margin call for ongoing orders only.

---

## 2022-09-15

- New endpoints for Crypto Loan
  - `POST /sapi/v1/loan/borrow`: Borrow - Crypto Loan Borrow
  - `GET /sapi/v1/loan/borrow/history`: Borrow - Get Loan Borrow History
  - `GET/sapi/v1/loan/ongoing/orders`: Borrow - Get Loan Ongoing Orders
  - `POST/sapi/v1/loan/repay`: Repay - Crypto Loan Repay
  - `GET/sapi/v1/loan/repay/history`: Repay - Get Loan Repayment History
  - `POST/sapi/v1/loan/adjust/ltv`: Adjust LTV - Crypto Loan Adjust LTV
  - `GET/sapi/v1/loan/ltv/adjustment/history`: Adjust LTV - Get Loan LTV Adjustment History

---

## 2021-11-08

- New endpoint for Crypto Loans:
  - New endpoint`GET /sapi/v1/loan/income`to support user query crypto loans income history

---

# 更新日志

## 2026-10-16

- 以下 SAPI 接口已下线，调用将返回 HTTP
  404。这些接口在 2024-11-05 固定利率借币下线及 2024-02-27 浮动利率 v2 升级后保留用于历史订单查询，相关文档已移除：
  - 固定利率：
    - `GET /sapi/v1/loan/income`
    - `GET /sapi/v1/loan/borrow/history`
    - `GET /sapi/v1/loan/repay/history`
    - `GET /sapi/v1/loan/ltv/adjustment/history`
  - 浮动利率（v1）：
    - `GET /sapi/v1/loan/flexible/borrow/history`
    - `GET /sapi/v1/loan/flexible/repay/history`
    - `GET /sapi/v1/loan/flexible/ltv/adjustment/history`
- 浮动利率 v2 接口不受影响。

## 2025-12-26

### 时效性通知

- **以下有关于REST API变更将在 2026-01-15 07:00 UTC 发生:** <br>
  调用需要签名的接口时，请在计算签名之前对 payload 进行百分比编码（percent-encode）。不符合此顺序的请求将被拒绝，并返回错误代码
  [`-1022 签名不正确`](./error-code.md#-1022-invalid_signature)。请检查并相应地更新您代码中的签名逻辑部分。

### REST API

- 更新了 REST API 文档中有关于 [签名请求示例](./general-info.md#post-apiv3order-的签名示例) 的部分。

## 2024-12-20

- 活期借币新增接口：活期借币支持抵押物还款

* `POST/sapi/v2/loan/flexible/repay/collateral`
* `GET /sapi/v2/loan/flexible/repay/rate`
* `GET /sapi/v2/loan/flexible/liquidation/history`

## 2024-11-05

- 根据币安借币（固定利率）的最新升级，币安借币已经下架了如下固定利率借贷对应的SAPI接口(VIP借币定期利率订单不受本次服务更新影响 ):
  - `GET /sapi/v1/loan/loanable/data`
  - `GET /sapi/v1/loan/collateral/data`
  - `POST /sapi/v1/loan/borrow`
  - `POST /sapi/v1/loan/repay`
  - `POST /sapi/v1/loan/adjust/ltv`
  - `POST /sapi/v1/loan/customize/margin_call`
  - `GET /sapi/v1/loan/ongoing/orders`

- 于此同时，币安借币会继续维护如下固定利率借贷的历史订单查询SAPI接口:
  - `GET /sapi/v1/loan/income`
  - `GET /sapi/v1/loan/borrow/history`
  - `GET /sapi/v1/loan/ltv/adjustment/history`
  - `GET /sapi/v1/loan/repay/history`

## 2024-02-27

- 根据币安借币（浮动利率）的[最新升级](https://www.binance.com/zh-CN/support/announcement/%E5%B8%81%E5%AE%89%E5%8D%87%E7%BA%A7%E8%B4%A8%E6%8A%BC%E5%80%9F%E5%B8%81-%E6%B4%BB%E6%9C%9F%E5%88%A9%E7%8E%87-%E4%BA%A7%E5%93%81-2024-02-27-d35942110b53480581773fc62a3e6eae)
  ，
  - 币安借币已于 2024-02-27 08:00 (UTC) 添加以下 /v2 SAPI 接口。用户可以使用 v2
    SAPI 接口来下单、还款和管理 2024-02-27 08:00 (UTC) 之后创建的 币安借币（浮动利率 新版）订单。
    - `POST /sapi/v2/loan/flexible/borrow`
    - `GET /sapi/v2/loan/flexible/ongoing/orders`
    - `GET /sapi/v2/loan/flexible/borrow/history`
    - `POST /sapi/v2/loan/flexible/repay`
    - `GET /sapi/v2/loan/flexible/repay/history`
    - `POST /sapi/v2/loan/flexible/adjust/ltv`
    - `GET /sapi/v2/loan/flexible/ltv/adjustment/history`
    - `GET /sapi/v2/loan/flexible/loanable/data`
    - `GET /sapi/v2/loan/flexible/collateral/data`

  - 此外，币安借币将在以下时间停止维护 /v1 SAPI 接口：
    - 在 2024-02-27 08:00 (UTC):
      - `POST /sapi/v1/loan/flexible/borrow`
      - `GET /sapi/v1/loan/flexible/loanable/data`
      - `GET /sapi/v1/loan/flexible/collateral/data`
    - 在 2024-04-24 03:00 (UTC):
      - `GET /sapi/v1/loan/flexible/ongoing/orders`
      - `POST /sapi/v1/loan/flexible/repay`
      - `POST /sapi/v1/loan/flexible/adjust/ltv`

  - 币安借币还将继续维护以下 /v1 SAPI 接口，以便用户查看在 2024-02-27 08:00
    (UTC) 之前浮动利率的订单历史。
    - `GET /sapi/v1/loan/flexible/borrow/history`
    - `GET /sapi/v1/loan/flexible/repay/history`
    - `GET /sapi/v1/loan/flexible/ltv/adjustment/history`

---

## 2023-08-26

- 新增质押借币接口：
  - `POST /sapi/v1/loan/flexible/borrow`: 活期借币借贷
  - `GET /sapi/v1/loan/flexible/ongoing/orders`: 查询活期借款中订单列表
  - `GET /sapi/v1/loan/flexible/borrow/history`: 查询活期借币历史记录
  - `POST /sapi/v1/loan/flexible/repay`: 活期借币还款
  - `POST /sapi/v1/loan/flexible/repay/history`: 查询活期借币还款记录历史
  - `POST /sapi/v1/loan/flexible/adjust/ltv`: 调整活期借币质押率
  - `GET /sapi/v1/loan/flexible/ltv/adjustment/history`: 查询活期借币质押率调整历史
  - `GET /sapi/v1/loan/flexible/loanable/data`: 查询活期借币可借币种数据
  - `GET /sapi/v1/loan/flexible/collateral/data`: 查询活期借币抵押币种数据

---

## 2023-02-21

- 修改质押借币接口:
  - `POST /sapi/v1/loan/borrow`: 参数`loanTerm`仅可传 7 或 30

---

## 2022-11-01

- 添加质押借币接口：
  - `GET /sapi/v1/loan/loanable/data`： 获取可借币种的利率和借贷限额。借入限额以美元价值显示。
  - `GET /sapi/v1/loan/collateral/data`： 获取抵押币种质押率信息和质押限额。质押限额以美元价值显示。
  - `GET /sapi/v1/loan/repay/collateral/rate`： 获取抵押物还款时，抵押/借贷币种的汇率价格。汇率价格有效时间为 8 秒。
  - `POST /sapi/v1/loan/customize/margin_call`： 质押借币自定义补仓质押率，仅可针对进行中订单，自定义补仓质押率。

---

## 2022-09-15

- 添加质押借币接口：
  - `POST /sapi/v1/loan/borrow`：借币 - 质押借币借贷
  - `GET /sapi/v1/loan/borrow/history`：借币 - 查询质押借币历史记录
  - `GET/sapi/v1/loan/ongoing/orders`：借币 - 查询借款中订单列表
  - `POST/sapi/v1/loan/repay`：还款 - 质押借币还款
  - `GET/sapi/v1/loan/repay/history`：还款 - 查询还款记录历史
  - `POST/sapi/v1/loan/adjust/ltv`：调整质押率 - 质押借币调整质押率
  - `GET/sapi/v1/loan/ltv/adjustment/history`：调整质押率 - 查询质押率调整历史

---

## 2021-11-08

- 新增质押借币接口:
  - 新增查询质押借币资金流水接口`GET /sapi/v1/loan/income`以支持用户查询质押借币资金流水历史