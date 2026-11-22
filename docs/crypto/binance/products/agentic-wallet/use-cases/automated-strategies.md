---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/agentic-wallet/use-cases/automated-strategies
api_type: Guide
updated_at: 2026-11-22 18:39:44.751902
---

# Automated Trading Strategies

## 🎯 Goal

Combine Agentic Wallet with published Wallet Skills to build end-to-end automated trading strategies
— discover opportunities, run security checks, and execute trades from a single conversation.

## ✅ Prerequisites

- Agentic Wallet [installed](../quickstart/install-agentic-wallet) and signed in.
- **The strategies below require the corresponding Skills to be installed.** Get them from
  [binance-skills-hub](https://github.com/binance/binance-skills-hub/tree/main/skills/binance-web3):
  - Strategy 1 (Meme Sniping): `meme-rush`, `query-token-audit`
  - Strategy 2 (Smart Money): `trading-signal`, `query-token-audit`
  - Strategy 3 (Narrative Capture): `meme-rush`, `query-token-info`

## Strategy 1: Meme Token Sniping

Use `meme-rush` to monitor newly launched or migrating Meme tokens, run security pre-checks with
`query-token-audit`, and execute trades when safe.

**Example conversation:**

> "What new Meme tokens launched on Solana recently?"

The Agent uses `meme-rush` to return tokens on the bonding curve.

> "Audit the security of token XXX for me"

The Agent uses `query-token-audit` to return risk score, honeypot detection, tax analysis, etc.

> "Looks safe enough. Buy with 50 USDT"

The Agent confirms and executes a market swap via Agentic Wallet.

## Strategy 2: Smart Money Following

Use `trading-signal` to monitor smart money buy signals in real-time, auto-check security, and
follow trades.

**Basic usage:**

> "What are the latest smart money buy signals?"

The Agent uses `trading-signal` to return active signals with token, trigger price, current price,
max gain, etc.

> "Is the token from this signal safe? Check it for me"

The Agent calls `query-token-audit` to return the security audit.

> "Looks good, buy with 50 USDT"

The Agent executes the trade via Agentic Wallet.

**Advanced usage — automated following:**

> "Check smart money signals every 5 minutes. When a new signal appears, auto-audit it. If risk
> level is LOW, buy with 50 USDT"

The AI Agent will set up a scheduled task to automatically: fetch signals → security audit → execute
trade if safe. The specific implementation is planned by the Agent based on your instructions.

## Strategy 3: Narrative Trend Capture

Use `meme-rush`'s AI narrative detection to discover market hot spots and position early.

**Example conversation:**

> "What narratives are trending right now? Which themes have the most capital inflow?"

The Agent uses `meme-rush` to return narrative themes ranked by net capital inflow.

> "What are the representative tokens for this narrative?"

The Agent returns related tokens with market data.

> "Check the holder distribution and liquidity for XXX"

The Agent uses `query-token-info` to return token details, holder analytics, and liquidity data.

> "Liquidity looks deep. Set a limit sell order for 50% when it reaches $1.2"

The Agent creates a limit sell order via Agentic Wallet.

## Best Practices

| Principle               | Description                                                                 |
| ----------------------- | --------------------------------------------------------------------------- |
| **Audit before buying** | For any non-mainstream token, audit with `query-token-audit` before trading |
| **Start small**         | Test new strategies with small amounts before scaling up                    |
| **Set stop-losses**     | Use limit sell orders to define exit points and avoid being stuck           |
| **Diversify**           | Don't put all funds into a single token or narrative                        |
| **Monitor regularly**   | Check limit order status and portfolio changes periodically                 |

> ⚠️ **Risk Warning:** On-chain trading involves slippage, MEV attacks, and contract risks. All
> trading decisions should be based on your own research (DYOR). Skills provide information and
> execution capabilities only — they do not constitute investment advice.

## What's next

- [Skills Reference](../reference/skills) — Full capability reference for all Skills modules.
- [Supported Skills](../../wallet-skills/supported-skills) — View all available Wallet Skills.

---

# 自动化交易策略

## 🎯 目标

将 Agentic Wallet 与已发布的 Wallet
Skills 结合，构建端到端自动化交易策略 —— 从发现机会、运行安全检查到执行交易，全部在一段对话中完成。

## ✅ 前置条件

- Agentic Wallet 已[安装](../quickstart/install-agentic-wallet)并登录。
- **以下策略需安装对应的 Skills。** 从
  [binance-skills-hub](https://github.com/binance/binance-skills-hub/tree/main/skills/binance-web3)
  获取：
  - 策略 1（Meme 打新）：`meme-rush`、`query-token-audit`
  - 策略 2（聪明钱）：`trading-signal`、`query-token-audit`
  - 策略 3（叙事捕捉）：`meme-rush`、`query-token-info`

## 策略 1：Meme 代币打新

使用 `meme-rush` 监控新发行或正在迁移的 Meme 代币，用 `query-token-audit`
运行安全预检，安全时执行交易。

**示例对话：**

> "最近在 Solana 上发行了哪些新 Meme 代币？"

AI 使用 `meme-rush` 返回处于 bonding curve 阶段的代币。

> "帮我审计 XXX 代币的安全性"

AI 使用 `query-token-audit` 返回风险评分、蜜罐检测、税率分析等。

> "看起来够安全。用 50 USDT 买入"

AI 通过 Agentic Wallet 确认并执行市价兑换。

## 策略 2：聪明钱跟随

使用 `trading-signal` 实时监控聪明钱买入信号，自动进行安全检查，跟随交易。

**基本用法：**

> "最新的聪明钱买入信号有哪些？"

AI 使用 `trading-signal` 返回活跃信号，包含代币、触发价、当前价、最大涨幅等。

> "这个信号里的代币安全吗？帮我查一下"

AI 调用 `query-token-audit` 返回安全审计。

> "看起来不错，用 50 USDT 买入"

AI 通过 Agentic Wallet 执行交易。

**进阶用法 —— 自动跟随：**

> "每 5 分钟检查聪明钱信号。出现新信号时自动审计。如果风险等级为 LOW，用 50 USDT 买入"

AI
Agent 会创建一个定时任务，自动执行：获取信号 → 安全审计 → 安全时执行交易。具体实现由 Agent 根据你的指令规划。

## 策略 3：叙事趋势捕捉

使用 `meme-rush` 的 AI 叙事检测发现市场热点并提前布局。

**示例对话：**

> "当前哪些叙事在流行？哪些主题有最多的资金流入？"

AI 使用 `meme-rush` 返回按净资金流入排序的叙事主题。

> "这个叙事有哪些代表性代币？"

AI 返回相关代币及其行情数据。

> "查一下 XXX 的持有人分布和流动性"

AI 使用 `query-token-info` 返回代币详情、持有人分析和流动性数据。

> "流动性看起来很充足。到 $1.2 时设置 50% 的限价卖出"

AI 通过 Agentic Wallet 创建限价卖出订单。

## 最佳实践

| 原则           | 说明                                              |
| -------------- | ------------------------------------------------- |
| **买入前审计** | 任何非主流代币交易前都用 `query-token-audit` 审计 |
| **小仓位起步** | 用小额测试新策略后再放大                          |
| **设置止损**   | 用限价卖出订单定义出场点，避免被套                |
| **分散投资**   | 不要把所有资金押在单一代币或叙事上                |
| **定期监控**   | 定期检查限价订单状态和持仓变化                    |

> ⚠️ **风险提示：**
> 链上交易涉及滑点、MEV 攻击和合约风险。所有交易决策应基于你自己的研究（DYOR）。Skills 仅提供信息和执行能力，不构成投资建议。

## 下一步

- [Skills 参考](../reference/skills) —— 所有 Skills 模块的完整能力参考。
- [支持的 Skills](../../wallet-skills/supported-skills) —— 查看所有可用的 Wallet Skills。