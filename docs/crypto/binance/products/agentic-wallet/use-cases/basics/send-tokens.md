---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/agentic-wallet/use-cases/basics/send-tokens
api_type: Guide
updated_at: 2026-11-21 18:43:17.344621
---

# Send Tokens

## 🎯 Goal

Transfer native or ERC-20 tokens to a trusted address, with the Agent confirming amount and
destination before it executes.

## ✅ Prerequisites

- Agentic Wallet [installed](../../quickstart/install-agentic-wallet) and signed in.
- **The recipient address must be added to the Address Book in the Binance App** (Wallet → Settings
  → Address Book). Transfers can only go to whitelisted addresses.

## Send native token

> "Send 0.02 BNB to 0x1234...5678"

The Agent confirms the details before executing — for example: "You're about to send 0.02 BNB to
0x1234...5678, with a small gas fee. Confirm to proceed." Once you approve, it submits the transfer
and reports back with the transaction hash.

## Send ERC-20 token

> "Transfer 10 USDT to 0x1234...5678"

The Agent will show you the amount and destination address before executing. After success, it
returns a transaction hash. You can follow up:

> "Has that transfer been confirmed on-chain?"

The Agent checks and answers in plain language — for example: "Yes, your 10 USDT transfer to
0x1234...5678 was confirmed on-chain a few moments ago."

## What's next

- [Wallet Operations](./wallet-operations) — Check the transfer status and history.
- [Market Order](../trading/market-order) — Swap tokens at market price.

---

# 发送代币

## 🎯 目标

向可信地址转账原生代币或 ERC-20 代币，AI Agent 会在执行前确认金额和目标地址。

## ✅ 前置条件

- 已[安装](../../quickstart/install-agentic-wallet) Agentic Wallet 并登录。
- **收款地址必须已在币安 App 中添加到地址簿** （钱包 → 设置 → 地址簿）。转账只能发往白名单地址。

## 发送原生代币

> "转 0.02 BNB 到 0x1234...5678"

AI Agent 会在执行前确认细节——例如："你即将向 0x1234...5678 发送 0.02
BNB，另需一笔少量 gas 费。确认以继续。" 一旦你批准，它会提交转账并返回交易哈希。

## 发送 ERC-20 代币

> "转 10 USDT 到 0x1234...5678"

AI Agent 会在执行前向你展示金额和目标地址。成功后，它会返回交易哈希。你可以追问：

> "那笔转账在链上确认了吗？"

AI Agent 会检查并用自然语言回答——例如："是的，你向 0x1234...5678 转的 10 USDT 刚刚已在链上确认。"

## 下一步

- [钱包操作](./wallet-operations) —— 查看转账状态和记录。
- [市价单](../trading/market-order) —— 按市价兑换代币。