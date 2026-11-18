---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/agentic-wallet/use-cases/minimal-tutorial
api_type: Guide
updated_at: 2026-11-18 18:41:03.835408
---

# Minimal Tutorial

## 🎯 Goal

Complete your first end-to-end swap in four steps — the shortest path from "is my wallet working" to
"the swap is on-chain".

## ✅ Prerequisites

- Agentic Wallet [installed](../quickstart/install-agentic-wallet) and signed in.
- A small BNB balance for gas and the swap.

## Walkthrough

The minimal workflow: check status → get a quote → confirm and swap.

**1. Check wallet connection**

> "Is my wallet connected? What's my address?"

The Agent returns your connection status and wallet address.

**2. Check balances**

> "How much BNB and USDT do I have?"

The Agent returns all non-zero balances with USD valuation.

**3. Get a swap quote (no execution)**

> "How much USDT would I get for 0.01 BNB? Don't execute."

The Agent returns the estimated output, slippage, and gas estimate — no on-chain transaction is
triggered.

**4. Execute the swap**

> "Go ahead and execute."

The Agent requests your confirmation, then submits the on-chain swap and returns an order ID for
tracking.

## What's next

- Dive into [Wallet Operations](./basics/wallet-operations) for the full set of status and balance
  queries.
- Learn [Market Order](./trading/market-order) and [Limit Order](./trading/limit-order) trading in
  depth.

---

# 最小教程

## 🎯 目标

用四个步骤完成你的第一笔端到端兑换——从"我的钱包能用吗"到"兑换已上链"的最短路径。

## ✅ 前置条件

- 已[安装](../quickstart/install-agentic-wallet) Agentic Wallet 并登录。
- 有一小笔用于 gas 和兑换的 BNB 余额。

## 操作流程

最小工作流：查看状态 → 获取报价 → 确认并兑换。

**1. 查看钱包连接**

> "我的钱包连接上了吗？我的地址是什么？"

AI Agent 会返回你的连接状态和钱包地址。

**2. 查看余额**

> "我有多少 BNB 和 USDT？"

AI Agent 会返回所有非零余额及其美元估值。

**3. 获取兑换报价（不执行）**

> "0.01 BNB 能换多少 USDT？不要执行。"

AI Agent 会返回预估产出、滑点和 gas 估算——不触发任何链上交易。

**4. 执行兑换**

> "继续，执行吧。"

AI Agent 会请求你确认，然后提交链上兑换并返回一个用于跟踪的订单 ID。

## 下一步

- 深入了解[钱包操作](./basics/wallet-operations)，掌握全套状态和余额查询。
- 深入学习[市价单](./trading/market-order)和[限价单](./trading/limit-order)交易。