---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/agentic-wallet/welcome
api_type: Guide
updated_at: 2026-11-18 02:11:45.397815
---

# Binance Agentic Wallet

## What is Binance Agentic Wallet

On-chain operations are getting more complex by the day — limit orders, multi-chain asset
management… every step demands manual action, constant monitoring, and the risk of missing the right
moment.

**Binance Agentic Wallet changes all of that.**

Just tell your AI what you want in plain language. The AI understands your intent, finds the optimal
path, and executes on-chain within the safety rules you define. No contract addresses to memorize.
No parameters to type. No screen to watch.

### Why Binance Agentic Wallet

**MPC Keyless Security** Built on the same MPC Keyless technology as Binance Wallet. Your private
key is never fully reconstructed on any single device or server. The AI Agent cannot directly hold
or transfer your keys. Every operation is logged and auditable on-chain.

**You Set the Rules — the AI Stays Within Them** Set your daily limit, tradable token scope, and
high-risk transaction handling in the Binance App. These rules constrain the Agent at the API level.
Any action outside your rules is automatically rejected or requires a second confirmation from you.

**Natural Language as the Interface** Swap, transfer, place orders, check balances — all through
conversation. Install the Skills and connect to Claude, ChatGPT, Copilot, or any major AI Agent.
Agentic Wallet is ready immediately.

---

## Core Capabilities

| Capability            | Description                                                                    |
| --------------------- | ------------------------------------------------------------------------------ |
| **Authentication**    | QR code sign-in, session management, sign-out                                  |
| **Wallet**            | Status, address, balances, transaction history, daily quota, security settings |
| **Market Order**      | Market swap, quote, order tracking                                             |
| **Limit Order**       | Limit buy/sell, order management, cancel                                       |
| **Prediction Market** | Browse markets, place predictions, manage positions, redeem winnings           |

> More features coming soon.

### Security: MPC Keyless

- Private key is never fully reconstructed on any single device or server
- All Agent operations are logged and auditable at any time
- The Agent is constrained at the API level and cannot exceed user-defined rules

### You Define the Rules

- Set daily limits and tradable token scope in the Binance App
- Sign out of Agentic Wallet anytime to revoke the Agent's access
- High-risk transactions can be auto-rejected or sent for App confirmation

---

## Key Use Cases

**Check your assets**

> "What's my wallet address? How much USDT do I have? How much of my daily limit is left?"

**Market swap**

> "Swap 0.1 BNB for USDT" — the AI fetches a quote, confirms with you, then executes.

**Limit order**

> "Buy 100 USDT worth of BNB when the price drops to $500" — the order waits for the trigger
> automatically.

**Token transfer**

> "Send 10 USDT to 0x123" — the AI confirms with you before executing, address has to be in
> addressbook

**Prediction market**

> "Bet 10 USDT on YES for BTC 5-min price up" — the AI shows current odds, confirms your bet, then
> places the prediction.

---

## Install

Run the following command to install Skills. The CLI will be set up automatically:

```bash
npx skills add binance/binance-skills-hub/skills/binance-web3/binance-agentic-wallet
```

See [Install Agentic Wallet](./quickstart/install-agentic-wallet.md) for the full setup guide.

---

## Chain Support

Current version supports 4 major networks, with more chains coming soon.

| Network               | Chain ID | Status         |
| --------------------- | -------- | -------------- |
| BNB Smart Chain (BSC) | 56       | ✅ Supported   |
| Ethereum              | 1        | ✅ Supported   |
| Base                  | 8453     | ✅ Supported   |
| Solana                | CT_501   | ✅ Supported   |
| More networks         | —        | 🔜 Coming Soon |

---

## Documentation

- [Install Agentic Wallet](./quickstart/install-agentic-wallet.md)
- [Use Cases Overview](./use-cases/overview.md)
- [Skills Reference](./reference/skills.md)

---

# Binance Agentic Wallet

## 什么是 Binance Agentic Wallet

链上操作正在变得越来越复杂：限价挂单、多链资产管理……每一步都需要用户手动操作，随时盯盘，一不小心就错过最佳时机。

**Binance Agentic Wallet 改变了这一切。**

它让你可以用自然语言告诉 AI 你想做什么——AI 负责理解你的意图、选择最优路径，并在你设定的安全规则范围内自动执行链上操作。你不需要懂合约地址，不需要手动输参数，不需要守在屏幕前。

### 为什么选择 Binance Agentic Wallet

**MPC Keyless 安全机制** 与 Binance Wallet 采用完全相同的 MPC
Keyless 技术：私钥永远不会在任何单一设备或服务器上被完整重建，AI
Agent 无法直接持有或转移你的私钥，所有操作均有链上日志可审计。

**你制定规则，AI 在规则内执行** 在 Binance
App 中设定每日限额、可交易代币范围和异常交易处理方式。这些规则在 API 层面约束 Agent 的行为，任何超出规则的操作都会被自动拒绝或发起二次确认。

**自然语言即操作界面**
兑换、转账、挂单、查余额——全部通过对话完成。安装 Skills 后，接入 Claude、ChatGPT、Copilot 等主流 AI
Agent，Agentic Wallet 即刻可用。

---

## 核心能力

| 能力                  | 说明                                               |
| --------------------- | -------------------------------------------------- |
| **Authentication**    | QR 码扫码登录、会话管理、登出                      |
| **Wallet**            | 状态查询、地址、余额、交易记录、每日限额、安全设置 |
| **Market Order**      | 市价兑换（Swap）、报价查询、订单查询               |
| **Limit Order**       | 限价挂单（买/卖）、订单管理、取消                  |
| **Prediction Market** | 浏览市场、下注预测、管理持仓、赎回收益             |

> 更多功能持续开发中，敬请期待。

### Security: MPC Keyless

- 私钥永远不会在任何单一设备或服务器上被完整重建
- 所有 Agent 操作均有日志记录，可随时审计
- Agent 在 API 层面受约束，无法突破用户设置的规则

### 你制定规则

- 在 Binance App 中设置每日限额和可交易代币范围
- 可随时在 App 里登出 Agentic Wallet，取消 Agent 的操作权限
- 异常交易支持自动拒绝或 App 二次确认两种处理模式

---

## 典型场景

**查询资产状态**

> "我的钱包地址是什么？ USDT 余额还有多少？ 今天还能操作多少额度？"

**市价兑换**

> "把 0.1 BNB 换成 USDT" — AI 自动获取报价， 确认后执行链上兑换。

**限价挂单**

> "BNB 价格跌到 $500 时， 用 100 USDT 买入 BNB" — 条件单自动等待触发， 无需守盘。

**代币转账**

> "把 10 USDT 转到 Ox123 的地址" — 收款地址须在通讯录中， AI 请求确认后执行。

**预测市场交易**

> "押注 10 USDT 赌 BTC 5分钟内上涨" — AI 展示当前赔率，确认下注后执行预测。

---

## 安装

运行以下命令安装 Skills，CLI 会在安装过程中自动完成：

```bash
npx skills add binance/binance-skills-hub/skills/binance-web3/binance-agentic-wallet
```

详见 [安装 Agentic Wallet](./quickstart/install-agentic-wallet.md)。

---

## 支持链

当前版本支持 4 条主流网络，更多链即将推出。

| 网络                  | Chain ID | 状态        |
| --------------------- | -------- | ----------- |
| BNB Smart Chain (BSC) | 56       | ✅ 支持     |
| Ethereum              | 1        | ✅ 支持     |
| Base                  | 8453     | ✅ 支持     |
| Solana                | CT_501   | ✅ 支持     |
| 更多网络              | —        | 🔜 即将推出 |

---

## 文档导航

- [安装 Agentic Wallet](./quickstart/install-agentic-wallet.md)
- [使用场景概览](./use-cases/overview.md)
- [Skills 参考](./reference/skills.md)