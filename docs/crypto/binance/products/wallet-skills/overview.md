---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/wallet-skills/overview
api_type: Guide
updated_at: 2026-11-28 18:27:40.039360
---

# Binance Wallet Skills

Binance Wallet Skills are composable AI modules for developers. They expose Binance Web3's on-chain
capabilities in a form that any LLM Agent or application can call directly.

## What Are Skills

Traditional APIs require developers to manually parse intent, call endpoints, and handle errors.
Skills wrap all of that into modules an AI can understand and invoke directly:

- Triggered by **natural language intent** — no API calls to write
- Each Skill is a standalone module — integrate individually or combine
- Compatible with Claude, ChatGPT, Copilot, and major AI Agent environments

## Published Wallet Skills (binance-web3)

8 Skills are currently published on
[binance-skills-hub](https://github.com/binance/binance-skills-hub/tree/main/skills/binance-web3):

| Skill                                 | Type         | Core Capability                                                                      |
| ------------------------------------- | ------------ | ------------------------------------------------------------------------------------ |
| **binance-agentic-wallet**            | Read + Write | Wallet management, token transfers, market swaps, limit orders (BSC/ETH/Base/Solana) |
| **query-token-info**                  | Read         | Token search, metadata, live market data, candlestick charts                         |
| **query-token-audit**                 | Read         | Token security audit: risk scoring, honeypot detection, contract verification        |
| **query-address-info**                | Read         | Wallet address token holdings with prices and balances                               |
| **crypto-market-rank**                | Read         | Market rankings: social buzz, smart money inflow, Meme coins, trader PnL             |
| **meme-rush**                         | Read         | Meme token tracking (new/migrating/migrated) + AI narrative discovery                |
| **trading-signal**                    | Read         | On-chain smart money signals with signal status and peak gain data                   |
| **binance-tokenized-securities-info** | Read         | Tokenized securities (Ondo Finance) — live prices, market status, on-chain data      |

→ [View full Skills list](/products/wallet-skills/supported-skills)

---

# Binance Wallet Skills

Binance Wallet Skills 是面向开发者的可组合 AI 模块，将 Binance
Web3 的链上能力以 AI 可调用的形式暴露，供任意 LLM Agent 或应用集成。

## 什么是 Skills

传统 API 需要开发者手动解析意图、调用接口、处理错误。Skills 把这些封装为 AI 可直接理解的模块：

- 用**自然语言意图**触发，不需要写 API 调用
- 每个 Skill 是一个独立能力模块，可单独集成，也可组合使用
- 兼容 Claude、ChatGPT、Copilot 及主流 AI Agent 环境

## 已发布的 Wallet Skills（binance-web3）

当前在
[binance-skills-hub](https://github.com/binance/binance-skills-hub/tree/main/skills/binance-web3)
发布了 8 个 Skills：

| Skill                                 | 类别         | 核心能力                                                    |
| ------------------------------------- | ------------ | ----------------------------------------------------------- |
| **binance-agentic-wallet**            | Read + Write | 钱包管理、代币转账、市价兑换、限价单（BSC/ETH/Base/Solana） |
| **query-token-info**                  | Read         | 代币搜索、元数据、实时行情、K 线数据                        |
| **query-token-audit**                 | Read         | 代币安全审计：风险评分、蜜罐检测、合约验证                  |
| **query-address-info**                | Read         | 钱包地址持仓查询，含价格与余额                              |
| **crypto-market-rank**                | Read         | 市场排行：热度、智能钱包流入、Meme 币、交易者 PnL           |
| **meme-rush**                         | Read         | Meme 代币追踪（新发/即将迁移/已迁移）+ AI 叙事主题          |
| **trading-signal**                    | Read         | 链上聪明钱交易信号，含信号状态与历史最大涨幅                |
| **binance-tokenized-securities-info** | Read         | 代币化证券（Ondo Finance）行情、状态与链上数据              |

→ [查看完整 Skills 列表](/products/wallet-skills/supported-skills)