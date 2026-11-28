---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/agentic-wallet/use-cases/trading/stock-trading
api_type: Guide
updated_at: 2026-11-28 18:42:02.746808
---

# Stock Trading (Tokenized Securities)

## 🎯 Goal

Research and trade tokenized stocks (bStock and Ondo) by ticker or company name in plain language —
look up the on-chain price and trading status, then buy or sell the stock token, all through
conversation with your AI Agent.

## ✅ Prerequisites

- Agentic Wallet [installed](../../quickstart/install-agentic-wallet) and signed in.
- **Install the
  [`binance-tokenized-securities-info`](https://github.com/binance/binance-skills-hub/tree/main/skills/binance-web3)
  skill.** Agentic Wallet uses it to resolve a ticker/company name to its on-chain contract and to
  fetch price, fundamentals, and trading status. Without it, the Agent can't map "AAPL" to a
  tradable token.
- USDT to buy, plus native token for gas.

## How it works

A tokenized stock is an on-chain token backed by the underlying share. Trading it uses the same swap
flow as any token — the extra step is **resolving the ticker to a contract and checking the token's
trading status first**:

1. **Resolve** — the Agent maps the ticker or company name to its on-chain contract.
2. **Check status** — confirm the token is tradable (not paused / halted for a corporate action).
3. **Trade** — buy or sell the stock token.

## Research a stock

> "What tokenized stocks are available?"

The Agent lists the tradable bStock and Ondo tickers.

> "What's the on-chain price of AAPL, and its P/E and 52-week range?"

The Agent replies in plain language — for example: "AAPL is trading at about $228.5 on-chain. Its
P/E is 31.4, the dividend yield is 0.44%, and the 52-week range is $169.21–$260.10."

> "Show me TSLA's holders, circulating supply, and market cap"

The Agent summarizes the on-chain data for you conversationally.

## Check trading status before you trade

Tokenized stocks follow session states and corporate actions — a token can be paused or halted.

> "Is AAPL tradable right now?"

The Agent tells you the current state — for example: "AAPL is open and trading normally (regular
session), next close is 8:00 PM UTC." If a token is halted for a corporate action (earnings,
dividend, split, merger, or maintenance), the Agent explains why and holds off on trading.

## Buy a tokenized stock

> "How much AAPL would I get for 100 USDT? Quote only."

The Agent replies with the estimate — for example: "100 USDT would get you about 0.437 AAPL at the
current price, with 0.5% slippage. No order placed."

> "Buy AAPL with 100 USDT"

The Agent resolves the contract, checks status, shows you the quote, and on your confirmation
submits the swap — then confirms: "Done — your buy order for AAPL is submitted. Ask me to check its
status anytime."

## Sell a tokenized stock

> "Sell half my TSLA position for USDT"

> "Sell all my NVDA tokens"

The Agent confirms the amount and destination before executing, then reports back once the sell is
submitted.

## Check order status

> "Did my AAPL buy go through?"

The Agent looks up the order and answers in plain language — for example: "Yes — your AAPL buy
filled successfully. You spent 100 USDT and the transaction is confirmed on-chain."

## Automated strategies

Beyond one-off trades, you can hand the Agent a rule and let it watch a stock and act for you over
the long run.

### Example 1 — Earnings-reaction watcher

> "Watch NVDA on an ongoing basis. Around each earnings report, track how the price reacts: if it
> drops more than 8% from the pre-earnings level, buy 100 USDT as a dip; if I'm holding and it's up
> more than 10%, take profit on half. Keep this running across future earnings and message me on
> each action."

The Agent runs continuously, watches each earnings reaction as it comes, applies your dip-buy and
take-profit rules, executes when one triggers, and reports every move — staying active until you
stop it.

### Example 2 — News-driven sector strategy

Have the Agent continuously monitor market news, judge the impact on a sector you hold, and manage
the position or rotate into a new name.

> "Keep an eye on AI and semiconductor news — new model releases, chip export rules, key
> supply-chain moves. If clearly bullish news for AI/semis breaks and I hold NVDA or AMD, add 50
> USDT to the stronger one; if it names a tradable stock I don't hold yet (say a new AI winner), buy
> 50 USDT as a starter; if clearly bearish news breaks, trim my AI/semi exposure by 30%. Run this
> for 7 days and tell me each time, with the reason."

Over those 7 days the Agent keeps monitoring, judges each news item as bullish or bearish for
AI/semis and maps it to your holdings, decides whether to scale up, open a new position, or trim,
checks the token's on-chain trading status before acting, then executes and explains its reasoning.

> 💡 **Tip:** Agentic Wallet focuses on on-chain trading. Off-chain data such as earnings or news
> must be supplied via your own data source or a relevant Skill.

## ⚠️ Risk notice

Tokenized securities are not covered by securities insurance, may be restricted in your
jurisdiction, and can be halted for corporate actions. On-chain trading also carries slippage and
smart-contract risk. Do your own research (DYOR) — Skills provide information and execution
capability only, never investment advice.

---

# 代币化证券

## 🎯 目标

用自然语言按股票代码或公司名称研究并交易代币化股票（bStock 和 Ondo）—— 查询链上价格与交易状态，然后买入或卖出该股票代币，全程通过与 AI
Agent 对话完成。

## ✅ 前置条件

- Agentic Wallet 已[安装](../../quickstart/install-agentic-wallet)并登录。
- **安装
  [`binance-tokenized-securities-info`](https://github.com/binance/binance-skills-hub/tree/main/skills/binance-web3)
  skill。** Agentic
  Wallet 用它把股票代码/公司名称解析为链上合约，并获取价格、基本面和交易状态。没有它，AI 无法把 "AAPL" 映射到可交易的代币。
- 用于买入的 USDT，以及用于支付 gas 的原生代币（BNB）。

## 运作方式

代币化股票是由对应股份支撑的链上代币。交易它与交易其他代币的兑换流程相同 —— 额外的一步是**先把股票代码解析为合约、并检查该代币的交易状态**：

1. **解析** —— AI Agent 把股票代码或公司名称映射为其链上合约。
2. **查状态** —— 确认代币可交易（未因公司行为而暂停/停牌）。
3. **交易** —— 买入或卖出该股票代币。

## 研究一只股票

> “有哪些代币化股票可以交易？”

AI Agent 会列出可交易的 bStock 和 Ondo 股票代码。

> “AAPL 的链上价格、市盈率和 52 周区间是多少？”

AI
Agent 用自然语言回答 —— 例如：“AAPL 链上价格约为 $228.5，市盈率 31.4，股息率 0.44%，52 周区间为 $169.21–$260.10。”

> “看下 TSLA 的持有人、流通量和市值”

AI Agent 会以对话形式为你总结链上数据。

## 交易前先查交易状态

代币化股票遵循交易时段状态与公司行为 —— 代币可能被暂停或停牌。

> “AAPL 现在能交易吗？”

AI Agent 会告诉你当前状态 —— 例如：“AAPL 正常开盘交易中（regular 时段），下次收盘为 UTC
20:00。” 如果代币因公司行为（财报、分红、拆股、并购或维护）而停牌，AI Agent 会说明原因并暂缓交易。

## 买入代币化股票

> “100 USDT 能买到多少 AAPL？只报价。”

AI Agent 回复估算 —— 例如：“按当前价格，100 USDT 大约能买到 0.437 AAPL，滑点 0.5%。未下单。”

> “用 100 USDT 买入 AAPL”

AI
Agent 会解析合约、检查状态、向你展示报价，并在你确认后提交兑换 —— 然后确认：“完成 —— 你的 AAPL 买单已提交。随时可以让我查状态。”

## 卖出代币化股票

> “把我一半的 TSLA 持仓卖成 USDT”

> “卖掉我所有的 NVDA 代币”

AI Agent 会在执行前确认金额与去向，卖单提交后再向你汇报。

## 查询订单状态

> “我的 AAPL 买单成了吗？”

AI Agent 会查出订单并用自然语言回答 —— 例如：“成了 —— 你的 AAPL 买单已成功成交。你花了 100
USDT，交易已在链上确认。”

## 自动化策略

除了一次性交易，你还可以给 AI Agent 一条规则，让它替你长期盯盘并自动执行。

### 案例 1 —— 财报反应监控

> “持续盯着 NVDA。每次财报前后，跟踪它的价格反应：如果比财报前价格跌超 8%，就抄底买入 100
> USDT；如果我持有且它涨超 10%，就把一半仓位止盈。这个策略跨未来多个财报季一直跑，每次操作都告诉我。”

AI
Agent 会长期持续运行，逐次盯住每个财报的价格反应，套用你的抄底和止盈规则，触发时执行，并汇报每一步操作 —— 直到你停止该策略。

### 案例 2 —— 新闻驱动的板块策略

让 AI Agent 持续监控市场新闻，分析其对你所持板块的影响，进而管理仓位或轮动到新标的。

> “帮我盯着 AI 和半导体相关新闻 —— 新模型发布、芯片出口管制、重要供应链动态。如果出现明显利好 AI/半导体的消息、且我持有 NVDA 或 AMD，就给表现更强的那只加仓 50
> USDT；如果消息点名了某只我还没持有、且链上可交易的股票（比如某个新的 AI 赢家），就买入 50
> USDT 作为建仓；如果出现明显利空，就把我 AI/半导体的敞口减仓 30%。这个策略跑 7 天，每次操作都告诉我并说明理由。”

AI
Agent 会在这 7 天里持续监控，逐条判断新闻对 AI/半导体板块是利好还是利空，并映射到你的持仓上，决定加仓、建新仓还是减仓，执行前先检查代币的链上交易状态，然后执行并说明理由。

> 💡 **提示：** Agentic
> Wallet 专注于链上交易。策略所需的财报、新闻等链下数据需自行接入数据源或相应 Skill。

## ⚠️ 风险提示

代币化证券不受证券保险保护，在你所在的司法辖区可能受限，且可能因公司行为而停牌。链上交易还存在滑点和智能合约风险。请做好自己的研究（DYOR）——
Skills 仅提供信息和执行能力，不构成投资建议。