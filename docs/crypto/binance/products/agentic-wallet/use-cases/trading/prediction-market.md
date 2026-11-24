---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/agentic-wallet/use-cases/trading/prediction-market
api_type: Guide
updated_at: 2026-11-24 18:43:47.599204
---

# Prediction Market

## 🎯 Goal

Trade prediction markets end-to-end in natural language — discover markets, place market or limit
bets on outcomes, track positions and PnL, redeem winnings after a market resolves, and even hand
the whole loop to an automated strategy.

## ✅ Prerequisites

- Agentic Wallet [installed](../../quickstart/install-agentic-wallet) and signed in.
- BSC USDT balance to fund bets (prediction trades are quoted and settled in USDT).

## Browse & discover markets

Explore what's tradable by category, popularity, or keyword.

> "What prediction market categories are available?"

The Agent lists the categories — for example: crypto, sports, politics, economy, and culture.

> "Show me the most popular markets in the crypto category"

> "List crypto markets sorted by volume"

> "Search prediction markets about the next Fed rate decision"

The Agent returns the matching markets with their current odds and volume, and can sort by
recommended, volume, participants, newest, or soonest-to-resolve.

## Inspect a market before betting

> "Show me the full detail of this market"

> "What are the current odds for the 'Yes' outcome?"

> "What was the last traded price on this market?"

The Agent summarizes the market — the question, resolution date, each outcome's implied probability,
and recent activity. Prices sit between 0 and 1 USDT and read as the market's implied probability,
so a "Yes" at 0.62 means the market prices that outcome at ~62%.

> **Note:** the last-traded price is a historical fill, not a live quote — it can be stale. The
> Agent always pulls a fresh quote before placing an order.

## Place a bet

Prediction trading always quotes first, then places on your confirmation.

> "Buy 'Up' in the most recent BTC 15m price market with 5 USDT"

The Agent replies with the quote in plain language — for example: "5 USDT buys about 8.1 shares of
'Up' at an average price of 0.61, with a 1.2% price impact and a 0.02 USDT fee. Confirm to place?"
On your confirmation it places the order and reports back.

Both **market** and **limit** orders are supported:

> "Place a limit buy for 'Yes' at 0.60 USDT with 20 USDT"

> "Sell 10 shares of my 'Up' position at market"

A **buy** amount is the USDT you spend; a **sell** amount is the number of shares you sell.

## Check positions & PnL

> "What are my current prediction positions?"

> "Show my prediction portfolio and unrealized PnL"

> "Show my settled positions — only the ones I won"

The Agent groups your positions into ongoing, ended, and ready-to-claim, and summarizes your PnL —
for example: "You hold 3 ongoing positions worth ~42 USDT, up 11% unrealized. One resolved position
is ready to claim."

## Track & cancel orders

> "Show my prediction order history"

> "Which of my prediction orders are still open?"

> "Cancel my pending prediction order"

The Agent lists your orders with their status and can cancel any that are still resting. Placing an
order isn't the same as it filling — market orders usually fill quickly, while limit orders rest
until the price is hit, so the Agent always verifies status before reporting a bet as complete.

## Redeem winnings

Once a market resolves in your favor, claim the payout:

> "Do I have any winning predictions ready to claim?"

> "Redeem my winning prediction positions"

The Agent finds your ready-to-claim positions and triggers the redemption on-chain, then confirms
the payout landed in your wallet.

## Automated strategies

Beyond manual bets, you can hand the whole loop to the Agent and let it watch, judge, and bet on the
BTC 5-minute "Up / Down" market for you over the long run.

### Example — Price-trend-based Up/Down betting

> "Keep tracking BTC's price action and pull the settlement results of the last few 5-minute Up/Down
> rounds. Before each round settles, run a technical read on that price data — say short-term
> moving-average direction and recent momentum — to judge whether the next 5 minutes is more likely
> to settle Up or Down, then bet 10 USDT on the side you favor. Keep my total open exposure in the
> BTC 5-minute Up/Down market under 50 USDT, take profit once the overall position is up +30% and
> cut losses at −20%, and tell me the direction and reasoning on every bet."

The Agent keeps tracking price action and each round's outcome, runs a technical read before every
round to form a directional view, bets on that side within your 50 USDT exposure cap, and watches
overall PnL to apply the +30% take-profit and −20% stop-loss — reporting the direction and reason on
each action, until you stop it.

> 💡 **Tip:** Agentic Wallet focuses on prediction-market trading. BTC price data must be supplied
> via your own data source or a relevant Skill.

## ⚠️ Risk notice

Prediction outcomes are binary — a position can go to zero if the market resolves against you, and
outcome-token liquidity can be thin. Resolution depends on the market's oracle. Do your own research
(DYOR) — Skills provide information and execution capability only, never investment advice.

## What's next

- [Stock Trading](./stock-trading) — Trade tokenized stocks (bStock and Ondo).
- [DeFi](./defi) — Earn yield, provide liquidity, and manage protocol positions.
- [Automated Strategies](../automated-strategies) — Automate discovery and trading with Skills.

---

# 预测市场

## 🎯 目标

用自然语言端到端交易预测市场 —— 发现市场、对结果下市价单或限价单、跟踪持仓与 PnL、在市场结算后领取收益，甚至把整个流程交给自动化策略。

## ✅ 前置条件

- Agentic Wallet 已[安装](../../quickstart/install-agentic-wallet)并登录。
- 用于下注的 BSC USDT 余额（预测交易以 USDT 报价和结算）。

## 浏览与发现市场

按类别、热度或关键词探索可交易的市场。

> “有哪些预测市场类别？”

AI Agent 会列出类别 —— 例如：加密、体育、政治、经济和文化。

> “看下加密类别里最热门的市场”

> “按成交量列出加密类市场”

> “搜一下关于下次美联储利率决议的预测市场”

AI Agent 会返回匹配的市场及其当前赔率和成交量，并可按推荐、成交量、参与人数、最新或最快结算排序。

## 下注前先审视市场

> “把这个市场的完整详情给我看看”

> “‘Yes’ 结果现在的赔率是多少？”

> “这个市场最后成交价是多少？”

AI Agent 会为你总结该市场 —— 问题、结算日期、每个结果的隐含概率以及近期活跃度。价格在 0 到 1
USDT 之间，可理解为市场的隐含概率，所以 “Yes” 为 0.62 表示市场对该结果定价约 62%。

> **注意：** 最后成交价是历史成交，不是实时报价 —— 可能已过时。AI Agent 在下单前总会拉取一份新报价。

## 下注

预测交易总是先报价、在你确认后再下单。

> “用 5 USDT 买最近这个 BTC 15 分钟价格市场的 ‘Up’”

AI Agent 用自然语言回复报价 —— 例如：“5
USDT 大约能买到 8.1 份 ‘Up’，均价 0.61，价格冲击 1.2%，手续费 0.02
USDT。确认下单吗？” 你确认后它会下单并向你汇报。

同时支持**市价单**和**限价单**：

> “以 0.60 USDT 挂一个 ‘Yes’ 的限价买单，用 20 USDT”

> “把我 ‘Up’ 持仓里的 10 份按市价卖掉”

**买入**金额是你花的 USDT；**卖出**金额是你卖出的份数。

## 查询持仓与 PnL

> “我当前有哪些预测持仓？”

> “看下我的预测组合和未实现 PnL”

> “只看我赢了的已结算持仓”

AI Agent 会把你的持仓分成进行中、已结束和可领取，并总结你的 PnL
—— 例如：“你有 3 个进行中持仓，价值约 42 USDT，未实现盈利 11%。有 1 个已结算持仓可领取。”

## 跟踪与取消订单

> “看下我的预测订单历史”

> “我还有哪些预测订单没成交？”

> “取消我那个待处理的预测订单”

AI
Agent 会列出你的订单及其状态，并可取消仍在挂单中的订单。下单不等于成交 —— 市价单通常很快成交，而限价单会在盘中挂单，直到价格触及，所以 AI
Agent 在把下注报告为完成前总会核对状态。

## 领取收益

一旦市场结算且对你有利，就领取收益：

> “我有可以领取的获胜预测吗？”

> “领取我获胜的预测持仓”

AI Agent 会找出可领取的持仓并在链上触发赎回，然后确认收益已到账。

## 自动化策略

除了手动下注，你还可以把整个流程交给 AI Agent，让它在 BTC 5 分钟 “Up /
Down” 市场上长期替你盯盘、判断并下注。

### 案例 —— 基于价格趋势的 Up/Down 下注

> “持续跟踪 BTC 的价格走势，并拉取近期几轮 5 分钟 Up/Down 的结算结果。每一轮结算前，用这些价格数据做一次技术分析（比如短期均线方向、近几轮的涨跌动能），判断下一个 5 分钟大概率结算成 Up 还是 Down，然后在你更看好的一侧下注 10
> USDT。把我在 BTC 5 分钟 Up/Down 市场的总未平仓敞口控制在 50
> USDT 以内，整体仓位盈利到 +30% 就止盈离场、亏损到 −20% 就止损，每次下注都告诉我方向和依据。”

AI
Agent 会持续跟踪价格走势和每一轮的结算结果，在每轮结算前做一次技术研判、形成对下一轮的方向判断，在你设定的 50
USDT 敞口上限内下注对应一侧，并盯着整体盈亏执行 +30% 止盈、−20% 止损 —— 每次操作都汇报方向和理由，直到你停止该策略。

> 💡 **提示：** Agentic
> Wallet 专注于预测市场交易。策略所需的 BTC 价格数据需自行接入数据源或相应 Skill。

## ⚠️ 风险提示

预测结果是二元的 —— 如果市场结算与你相反，持仓可能归零，且结果代币的流动性可能很薄。结算依赖该市场的预言机（oracle）。请做好自己的研究（DYOR）——
Skills 仅提供信息和执行能力，不构成投资建议。

## 下一步

- [代币化证券](./stock-trading) —— 交易代币化股票（bStock 和 Ondo）。
- [DeFi](./defi) —— 赚取收益、提供流动性、管理协议持仓。
- [自动化策略](../automated-strategies) —— 用 Skills 自动完成市场发现与交易。