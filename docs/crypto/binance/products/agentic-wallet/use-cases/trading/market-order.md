---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/agentic-wallet/use-cases/trading/market-order
api_type: Guide
updated_at: 2026-11-24 18:43:49.266627
---

# Market Order (Swap)

## 🎯 Goal

Swap one token for another at the current market price — get a quote first, then confirm to execute,
and track the order to completion.

## ✅ Prerequisites

- Agentic Wallet [installed](../../quickstart/install-agentic-wallet) and signed in.
- Enough balance of the token you're selling, plus native token for gas.

## Get a quote

> "How much USDT would I get for 0.1 BNB? Quote only, don't execute."

The Agent replies with the estimate in plain language — for example: "0.1 BNB is currently worth
about 61 USDT, with 0.5% slippage and a small gas fee. No transaction placed."

## Execute a market swap

> "Swap 0.1 BNB for USDT"

> "Buy BNB with 50 USDT, slippage max 2%"

The Agent shows the quote and waits for confirmation. Say "confirm" or "go ahead" to trigger the
swap.

## Check order status

> "Has my last swap completed?"

> "Show me my recent swap orders"

> "Any swaps still pending?"

The Agent summarizes your orders in plain language — for example: "Your last swap of 0.1 BNB for
about 61 USDT finished successfully a few minutes ago. You have no swaps still pending." The status
of each order maps to one of the following:

| Status     | Description           |
| ---------- | --------------------- |
| `PENDING`  | Processing on-chain   |
| `FINISHED` | Executed successfully |
| `FAILED`   | Execution failed      |

## ⚠️ Risk notice

Market swaps execute at the best available price, which means slippage can be significant on
illiquid or volatile pairs — the amount you receive may differ from the quote. On-chain trading also
carries MEV-attack and smart-contract risk. Always review the final quote the Agent shows before
confirming, and base every decision on your own research (DYOR) — Skills provide information and
execution capability only, never investment advice.

## What's next

- [Limit Order](./limit-order) — Set a target price and let the Agent execute automatically.
- [Automated Strategies](../automated-strategies) — Combine swaps with Skills for hands-off trading.

---

# 市价单（兑换）

## 🎯 目标

按当前市价把一种代币兑换成另一种——先获取报价，再确认执行，并跟踪订单直至完成。

## ✅ 前置条件

- 已[安装](../../quickstart/install-agentic-wallet) Agentic Wallet 并登录。
- 有足够的待卖出代币余额，以及用于 gas 的原生代币。

## 获取报价

> "0.1 BNB 能换多少 USDT？只报价，不要执行。"

AI Agent 会用自然语言给出估算——例如："0.1 BNB 目前约值 61
USDT，滑点 0.5%，另有一笔少量 gas 费。未提交任何交易。"

## 执行市价兑换

> "把 0.1 BNB 兑换成 USDT"

> "用 50 USDT 买 BNB，滑点上限 2%"

AI Agent 会展示报价并等待确认。说"确认"或"继续"即可触发兑换。

## 查看订单状态

> "我上一笔兑换完成了吗？"

> "看一下我最近的兑换订单"

> "还有兑换在待处理吗？"

AI Agent 会用自然语言总结你的订单——例如："你上一笔把 0.1 BNB 兑换成约 61
USDT 的订单几分钟前成功完成。没有仍在待处理的兑换。"每笔订单的状态对应以下之一：

| 状态       | 说明       |
| ---------- | ---------- |
| `PENDING`  | 链上处理中 |
| `FINISHED` | 已成功执行 |
| `FAILED`   | 执行失败   |

## ⚠️ 风险提示

市价兑换按当前最优价格执行，这意味着在流动性不足或波动剧烈的交易对上滑点可能很大——你实际收到的数量可能与报价有出入。链上交易还伴随 MEV 攻击和智能合约风险。请务必在确认前审核 AI
Agent 展示的最终报价，并基于你自己的研究（DYOR）做出每一个决定——Skill 只提供信息和执行能力，绝不构成投资建议。

## 下一步

- [限价单](./limit-order) —— 设定目标价格，让 AI Agent 自动执行。
- [自动化策略](../automated-strategies) —— 把兑换与 Skill 结合，实现无需盯盘的交易。