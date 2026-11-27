---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/portfolio-account/integration-guide-investor
api_type: Guide
updated_at: 2026-11-27 18:30:05.725418
---

# Integration Guide — Investor

An investor is a KYB-verified institutional user that subscribes to a portfolio, monitors
performance, and redeems allocations. Investor endpoints use API keys issued on the investor's own
account, not the trading team's.

**Step 1 — Get bound to a Portfolio Account.** An investor joins by invitation from the trading
team. The invitation arrives by email and must be accepted within 7 days. Once accepted you are
bound to the Portfolio Account and can subscribe and redeem. If you decline, the trading team cannot
re-invite you to the same portfolio for 30 days.

**Step 2 — Browse and subscribe.** If the portfolio is listed on Capital Connect you can discover it
on the marketplace and compare portfolios by performance, strategy type, risk metrics and terms.
Private portfolios are visible only to their invited investors.

To subscribe, submit a subscription for an amount at or above the portfolio minimum disclosed in the
Key Fact Sheet. Funds are frozen in your account until the trading team approves or declines. After
approval, funds transfer to the Portfolio Account within approximately 1 hour, priced at the
applicable NAV, and your allocations are issued. A brand-new portfolio must complete its first daily
NAV calculation before subscriptions can be processed.

**Step 3 — Monitor your position.** Call Investor Portfolio NAV Info to retrieve the NAV per
allocation series. NAV is struck daily between 00:00 and 04:00 UTC, so the latest value is for the
previous day.

For intraday monitoring, call Investor Portfolio Realtime Asset Value, which returns the current NAV
per allocation and your current equity.

Realtime values are for monitoring only. Subscriptions and redemptions are priced using the daily
NAV strike, not the realtime value.

**Step 4 — Reconcile your records.** Call Investor Portfolio History Info to retrieve your own
subscription and redemption records.

**Step 5 — Redeem.** Redemption does not require trading team approval. Submit the number of
allocations to redeem and a redemption time expressed as T+N days from the request date, where T+N
falls within the portfolio's settlement window.

After approval the system attempts the transfer daily from T+1 up to your selected date. Completed
redemptions return funds to your master account spot wallet.

- **Lock-up:** during the lock-up period disclosed in the Key Fact Sheet, redemption is unavailable.
- **Failed settlement:** if the transfer cannot complete by the deadline, the request fails. Your
  allocations remain in the portfolio; submit a new request.

**Step 6 — Performance data.** Capital Connect displays cumulative returns for 7D, 30D, 90D and
since inception, plus risk metrics including Sharpe ratio, Sortino ratio, maximum drawdown and
volatility. All performance figures are calculated by Binance from NAV history and cannot be
self-reported by trading teams.

Note on history: the API exposes a trailing NAV window only. If you need since-inception series for
your own reporting, persist each day's NAV from the start of your integration.

**Step 7 — Data availability.** Portfolio-level data access through the API is controlled by the
trading team. If sharing is disabled, portfolio-level endpoints return an error indicating the
trading team has not enabled data sharing. Contact the trading team or your account manager.

---

# 集成指南 — 投资人

投资人是通过 KYB 认证的机构用户，申购投资组合、监控业绩并赎回份额。投资人接口使用签发在投资人自己账户上的 API
Key，而不是交易团队的 Key。

**第 1 步 — 绑定投资组合账户。**
投资人通过交易团队的邀请加入。邀请通过邮件送达，必须在 7 天内接受。接受后即被绑定到该投资组合账户，可以申购和赎回。如果拒绝邀请，交易团队 30 天内不能再次邀请您加入同一个投资组合。

**第 2 步 — 浏览与申购。** 如果投资组合已在 Capital
Connect 上架，您可以在市场中发现它，并按业绩、策略类型、风险指标和条款对比不同投资组合。私有投资组合仅对受邀投资人可见。

申购时，提交不低于 Key Fact
Sheet 中披露的最低投资额的金额。资金在您的账户中被冻结，直到交易团队批准或拒绝。批准后，资金约 1 小时内划转到投资组合账户，按适用净值定价，并发行份额。全新的投资组合必须完成首次每日净值计算后，才能处理申购。

**第 3 步 — 监控持仓。** 调用投资人投资组合净值信息接口获取每份净值序列。净值每天在 UTC
00:00 至 04:00 之间结算，因此最新值是前一天的。

如需日内监控，请调用投资人投资组合实时资产价值接口，它返回当前每份净值和您当前的权益。

实时数值仅用于监控。申购和赎回按每日净值结算定价，而不是实时数值。

**第 4 步 — 核对记录。** 调用投资人投资组合历史信息接口获取您自己的申购和赎回记录。

**第 5 步 — 赎回。**
赎回无需交易团队审批。提交要赎回的份额数量，以及以申请日起算的 T+N 天表示的赎回时间，T+N 须在投资组合的结算窗口之内。

获批后，系统每日尝试划转，从 T+1 开始直到您选择的日期。赎回完成后，资金返回到您主账户的现货钱包。

- **锁定期：** 在 Key Fact Sheet 披露的锁定期内，不可赎回。
- **结算失败：** 如果截止日前划转无法完成，请求失败。您的份额仍保留在投资组合中，请重新提交请求。

**第 6 步 — 业绩数据。** Capital
Connect 展示 7 日、30 日、90 日及成立以来的累计收益，以及夏普比率、索提诺比率、最大回撤和波动率等风险指标。所有业绩数据均由币安基于净值历史计算，交易团队无法自行上报。

关于历史数据的说明：API 仅开放滚动净值窗口。如果您需要成立以来的序列用于自己的报告，请从对接开始起每天保存当日净值。

**第 7 步 — 数据可用性。**
通过 API 访问投资组合层面的数据由交易团队控制。如果共享被关闭，投资组合层面的接口会返回错误，提示交易团队未开启数据共享。请联系交易团队或您的客户经理。