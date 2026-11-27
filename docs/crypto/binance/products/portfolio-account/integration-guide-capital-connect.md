---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/portfolio-account/integration-guide-capital-connect
api_type: Guide
updated_at: 2026-11-27 18:30:07.235661
---

# Integration Guide — Capital Connect Listing

Capital Connect is the distribution layer on top of Portfolio Account. It lists portfolios to
KYB-verified institutional investors using performance data calculated by Binance. The listing flow
is a business process with no API integration.

**Step 1 — Meet the eligibility requirements.**

- KYB-verified entity.
- Valid license or exemption. An asset management or portfolio management license, or a recognised
  exemption, issued by a regulatory authority in the team's jurisdiction. Teams without a license
  may enter EIO mode.
- 30 active trading days.

**Step 2 — Define the portfolio terms.** Strategy description, fees, lock-up period, settlement
window, minimum investment, currency. These are disclosed in the Key Fact Sheet before investors
subscribe, and become locked for existing investors once they subscribe.

**Step 3 — Accumulate the track record.** Trade the portfolio and let the NAV series build. Binance
calculates all performance data — cumulative returns, NAV history, risk metrics — from NAV history.
Trading teams cannot self-report or edit historical performance data at any stage.

**Step 4 — Submit the Open Offering application.** All portfolios are private by default. To list
publicly, contact your account manager to submit an Open Offering application for Binance review.
Binance may request additional strategy information. The review ensures information presented to
investors is factual and complete; it does not endorse or favour any trading team or portfolio.

**Step 5 — Go live and operate.** Once approved, the portfolio is listed as active and investors can
subscribe through Capital Connect. The daily operating loop is the same as the trading-team path.

---

# 集成指南 — Capital Connect 上架

Capital
Connect 是建立在投资组合账户之上的分发层，使用币安计算的业绩数据，向通过 KYB 认证的机构投资人展示投资组合。上架流程是一个业务流程，没有 API 对接。

**第 1 步 — 满足资格要求。**

- 已通过 KYB 认证的实体。
- 有效的牌照或豁免。由交易团队所在司法辖区监管机构颁发的资产管理或投资组合管理牌照，或公认的豁免。没有牌照的团队可以进入 EIO 模式。
- 30 个有效交易日。

**第 2 步 — 确定投资组合条款。**
策略说明、费用、锁定期、结算窗口、最低投资额、币种。这些条款会在投资人申购前通过 Key Fact
Sheet 披露，并在投资人申购后对现有投资人锁定。

**第 3 步 — 积累业绩记录。**
交易该投资组合并让净值序列逐步形成。币安基于净值历史计算所有业绩数据 — 累计收益、净值历史、风险指标。交易团队在任何阶段都无法自行上报或修改历史业绩数据。

**第 4 步 — 提交公开募集（Open Offering）申请。**
所有投资组合默认私有。如需公开上架，请联系您的客户经理，提交 Open
Offering 申请供币安审核。币安可能要求补充策略信息。审核的目的是确保向投资人展示的信息真实完整，并不代表对任何交易团队或投资组合的背书或偏向。

**第 5 步 — 上线与运营。** 获批后，投资组合以活跃状态上架，投资人可以通过 Capital
Connect 申购。日常运营流程与交易团队路径相同。