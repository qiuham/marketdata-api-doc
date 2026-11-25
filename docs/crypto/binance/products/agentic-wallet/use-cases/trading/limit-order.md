---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/agentic-wallet/use-cases/trading/limit-order
api_type: Guide
updated_at: 2026-11-25 18:43:52.814718
---

# Limit Order

## 🎯 Goal

Set a target price once and let the Agent execute the trade automatically when the market hits it —
no need to watch the charts.

## ✅ Prerequisites

- Agentic Wallet [installed](../../quickstart/install-agentic-wallet) and signed in.
- **Chain support:** limit orders are only available on **BSC and Solana**.
- **Token rules:** buy orders — `fromToken` must be USDT, USDC, USD1, U or native token; sell orders
  — `toToken` must be USDT, USDC, USD1, U or native token.

## Place a limit buy

> "Buy BNB with 100 USDT when the price drops to $500"

> "When WETH drops to $2800, buy some with 200 USDT on BSC"

The Agent creates the conditional order and returns a strategy ID. It executes automatically when
the price is hit.

## Place a limit sell

> "Sell 1 BNB for USDT when the price reaches $650"

> "Sell 0.5 WETH on BSC when it hits $3500"

The Agent sets up the sell order and confirms in plain language — for example: "I've placed a limit
sell for 1 BNB at $650 (strategy ID 9876543210). It will execute automatically once the price is
reached."

## Check limit orders

> "What limit orders do I have open?"

> "Show me limit orders still waiting to trigger"

> "Check the status of limit order 9876543210"

The Agent summarizes your open orders in plain language — for example: "You have one open order: a
limit sell of 1 BNB at $650, still waiting for the trigger price." Each order's status maps to one
of the following:

| Status      | Description               |
| ----------- | ------------------------- |
| `WORKING`   | Waiting for trigger price |
| `TRIGGERED` | Price hit, executing      |
| `PENDING`   | Processing on-chain       |
| `FINISHED`  | Executed successfully     |
| `FAILED`    | Execution failed          |
| `EXPIRED`   | Order expired             |
| `CANCELED`  | Order canceled            |

## Cancel a limit order

> "Cancel my BNB limit buy order"

> "Cancel all my open orders"

The Agent confirms the cancellation in plain language — for example: "Done — your BNB limit buy
order has been canceled and is no longer resting on the book."

## ⚠️ Risk notice

Limit orders rest on the book until the trigger price is hit — they are **not** guaranteed to fill,
and a resting sell does not protect against a price gap that blows through your trigger. On-chain
trading also involves slippage, MEV attacks, and smart-contract risk. Every decision should be based
on your own research (DYOR) — Skills provide information and execution capability only, never
investment advice.

## What's next

- [Market Order](./market-order) — Swap immediately at market price instead.
- [Automated Strategies](../automated-strategies) — Use limit sells as automated stop-losses.

---

# 限价单

## 🎯 目标

只需设定一次目标价格，当市场触及时让 AI Agent 自动执行交易——无需盯盘看图。

## ✅ 前置条件

- 已[安装](../../quickstart/install-agentic-wallet) Agentic Wallet 并登录。
- **链支持：** 限价单仅在 **BSC 和 Solana** 上可用。
- **代币规则：** 买单——`fromToken` 必须是 USDT、USDC、USD1、U 或原生代币；卖单——`toToken`
  必须是 USDT、USDC、USD1、U 或原生代币。

## 下达限价买单

> "当价格跌到 $500 时，用 100 USDT 买 BNB"

> "当 WETH 跌到 $2800 时，在 BSC 上用 200 USDT 买一些"

AI Agent 会创建条件订单并返回一个策略 ID。当价格触及时，它会自动执行。

## 下达限价卖单

> "当价格涨到 $650 时，把 1 BNB 卖成 USDT"

> "当 WETH 在 BSC 上涨到 $3500 时卖出 0.5 个"

AI Agent 会设置卖单并用自然语言确认——例如："我已下达一笔限价卖单，在 $650 卖出 1 BNB（策略 ID
9876543210）。一旦价格触及，它会自动执行。"

## 查看限价单

> "我有哪些未成交的限价单？"

> "看一下还在等待触发的限价单"

> "查一下限价单 9876543210 的状态"

AI Agent 会用自然语言总结你的未成交订单——例如："你有一笔未成交订单：在 $650 限价卖出 1
BNB，仍在等待触发价格。" 每笔订单的状态对应以下之一：

| 状态        | 说明             |
| ----------- | ---------------- |
| `WORKING`   | 等待触发价格     |
| `TRIGGERED` | 价格触及，执行中 |
| `PENDING`   | 链上处理中       |
| `FINISHED`  | 已成功执行       |
| `FAILED`    | 执行失败         |
| `EXPIRED`   | 订单已过期       |
| `CANCELED`  | 订单已取消       |

## 取消限价单

> "取消我的 BNB 限价买单"

> "取消我所有未成交的订单"

AI Agent 会用自然语言确认取消——例如："已完成——你的 BNB 限价买单已取消，不再挂在盘口上。"

## ⚠️ 风险提示

限价单会挂在盘口上直到触发价格被触及——它们**不**保证成交，且一笔挂着的卖单无法防范跳空穿透触发价的行情。链上交易同样涉及滑点、MEV 攻击和智能合约风险。每一个决定都应基于你自己的研究（DYOR）——Skill 只提供信息和执行能力，绝不构成投资建议。

## 下一步

- [市价单](./market-order) —— 改为按市价立即兑换。
- [自动化策略](../automated-strategies) —— 把限价卖单用作自动止损。