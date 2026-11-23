---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/wallet-skills/supported-skills
api_type: Guide
updated_at: 2026-11-23 18:27:51.158493
---

# Supported Skills

Binance Wallet Skills are published on
[binance-skills-hub](https://github.com/binance/binance-skills-hub/tree/main/skills/binance-web3),
including 7 read-only **Wallet Skills** and the **Agentic Wallet Skill** for on-chain trading.

## Overview

### Published Wallet Skills

| Skill                                 | Type | Status  | Wallet Required |
| ------------------------------------- | ---- | ------- | --------------- |
| **query-token-info**                  | Read | ✅ Live | No              |
| **query-token-audit**                 | Read | ✅ Live | No              |
| **query-address-info**                | Read | ✅ Live | No              |
| **crypto-market-rank**                | Read | ✅ Live | No              |
| **meme-rush**                         | Read | ✅ Live | No              |
| **trading-signal**                    | Read | ✅ Live | No              |
| **binance-tokenized-securities-info** | Read | ✅ Live | No              |

### Agentic Wallet Skills

| Skill                      | Type         | Status  | Wallet Required |
| -------------------------- | ------------ | ------- | --------------- |
| **binance-agentic-wallet** | Read + Write | ✅ Live | Yes (write ops) |

---

## Published Wallet Skills

### query-token-info

Comprehensive token research — from discovery to deep analysis in one place.

**Supported operations**

| Operation          | Description                                                                        |
| ------------------ | ---------------------------------------------------------------------------------- |
| Token search       | Search by name, symbol, or contract address — returns price, market cap, liquidity |
| Metadata           | Description, creator, audit status, social links                                   |
| Live market data   | Price changes across timeframes (5m/1h/4h/24h), buy/sell volume, holder analytics  |
| Candlestick charts | OHLCV data from 1s to 1-month intervals                                            |

**Supported chains:** BSC, Base, Solana

```
What's the price of BNB?
Show me the holder distribution for this token
Give me SOL's 4-hour candlestick data
```

---

### query-token-audit

Pre-trade security audit to identify risky contracts and malicious tokens.

**Supported operations**

| Operation             | Description                                                       |
| --------------------- | ----------------------------------------------------------------- |
| Risk scoring          | Returns LOW / MEDIUM / HIGH risk level (scale 1–5)                |
| Honeypot detection    | Identifies contracts that can be bought but not sold              |
| Tax analysis          | Returns buy/sell tax rates — flags anything above 10% as critical |
| Contract verification | Checks whether source code is publicly verified                   |

**Supported chains:** Ethereum, BSC, Base, Solana

> ⚠️ Audit results are for reference only. LOW risk is not a safety guarantee. Always do your own
> research.

```
Is this contract address safe?
Does this token have honeypot risk?
```

---

### query-address-info

Query all tokens held by a wallet address, with balances and valuations.

**Supported operations**

| Operation      | Description                                                    |
| -------------- | -------------------------------------------------------------- |
| Holdings query | Returns all token balances, quantities, and contract addresses |
| Price data     | Current USD price and 24h change for each token                |
| Pagination     | Use offset parameter to page through large portfolios          |

**Supported chains:** BSC, Base, Solana

```
What tokens does this address hold?
What positions does 0xABC... have on BSC?
```

---

### crypto-market-rank

Multi-dimensional crypto market rankings covering social buzz, fund flows, Meme coins, and trader
performance.

**Supported operations**

| Operation           | Description                                                                                |
| ------------------- | ------------------------------------------------------------------------------------------ |
| Social buzz ranking | Ranked by community discussion volume, with sentiment analysis (positive/negative/neutral) |
| Unified rankings    | Trending tokens, top searched, Binance Alpha picks, tokenized stocks                       |
| Smart money inflow  | Top tokens by net buying from tracked smart wallets                                        |
| Meme token rank     | Top 100 Meme tokens from Pulse launchpad, scored by breakout potential                     |
| Trader PnL ranking  | Address-level realized P&L over 7d/30d/90d                                                 |

**Supported chains:** BSC, Base, Solana

```
Which tokens have the highest social buzz right now?
What are smart money wallets buying lately?
Show me the Binance Alpha picks ranking
```

---

### meme-rush

Real-time Meme token tracking + AI hot topic discovery, built for fast-paced Meme trading. Includes
two core features:

**Meme Rush — Launchpad token lifecycle tracking**

| Operation       | Description                                                                  |
| --------------- | ---------------------------------------------------------------------------- |
| New tokens      | Tracks newly launched tokens on the bonding curve                            |
| Migrating soon  | Monitors tokens near the end of the bonding curve, about to migrate to DEX   |
| Migrated tokens | Tokens that just completed migration — capture early liquidity opportunities |

**Topic Rush — AI hot topic discovery**

| Operation     | Description                                              |
| ------------- | -------------------------------------------------------- |
| Latest topics | Discover newest market hot topics with associated tokens |
| Rising topics | Topics gaining momentum (all-time high inflow $1k–$20k)  |

Each topic returns: topic name, AI summary, net inflow (total/1h), associated token list (with
market cap, liquidity, net inflow, holder count, etc.).

**Supported chains:** Solana (Pump.fun, Raydium, etc.), BSC (Four.meme, Flap, etc.)

```
What new Meme tokens launched on Solana recently?
Which Meme tokens are about to migrate to DEX?
What topics are trending right now?
What are the rising hot topics?
```

---

### trading-signal

Monitors on-chain smart money trading activity and outputs structured buy/sell signals for
reference.

**Supported operations**

| Operation        | Description                                                                                                |
| ---------------- | ---------------------------------------------------------------------------------------------------------- |
| Signal feed      | Buy/sell signals from smart money wallets on Solana and BSC                                                |
| Price comparison | Signal trigger price vs current price — gauge whether entry is still relevant                              |
| Signal quality   | Returns peak gain (maxGain) and smart money exit rate (exitRate)                                           |
| Token tags       | Labels tokens with Social Events, Launch Platform (e.g., Pumpfun), Sensitive Events (e.g., whale buy/sell) |
| Signal status    | Classifies signals as `active` / `timeout` / `completed`                                                   |

**Supported chains:** Solana, BSC

```
What are the latest smart money buy signals?
Are there any new on-chain signals on BNB Chain?
What was the peak gain after this signal triggered?
```

---

### binance-tokenized-securities-info

Query real-time on-chain data and status for Ondo Finance tokenized US stocks.

**Supported operations**

| Operation          | Description                                                                                       |
| ------------------ | ------------------------------------------------------------------------------------------------- |
| Asset list         | All supported tokenized stocks with contract addresses                                            |
| Company info       | CEO, industry, concept tags, attestation report links                                             |
| Market status      | Whether the Ondo market is open/paused, and next open/close times                                 |
| Corporate actions  | Per-token halt status (splits, dividends, mergers, etc.)                                          |
| Live on-chain data | Token price, 24h change, holder count, supply, market cap, and fundamentals (P/E, dividend yield) |
| Candlestick data   | OHLC data from 1-minute to 1-day intervals                                                        |

**Supported chains:** Ethereum, BSC

> Note: Each token represents `multiplier` shares, not 1 share. To compare with the reference price:
> `referencePrice = tokenPrice ÷ sharesMultiplier`.

```
Is the Ondo market open right now?
What's the current price of the AAPL tokenized stock?
Which tokenized stocks are halted due to corporate actions?
```

---

## Agentic Wallet Skill

`binance-agentic-wallet` provides wallet management, token transfers, market swaps, limit orders,
prediction market trading, and DeFi.

→ See [Agentic Wallet Documentation](/products/agentic-wallet/welcome) for details.

---

## Related

- [Binance Wallet Skills Overview](/products/wallet-skills/overview)

---

# 支持的 Skills

Binance Wallet Skills 已在
[binance-skills-hub](https://github.com/binance/binance-skills-hub/tree/main/skills/binance-web3)
发布，包括 7 个只读 **Wallet Skills** 和用于链上交易的 **Agentic Wallet Skill**。

## 总览

### 已发布 Wallet Skills

| Skill                                 | 类别 | 状态    | 需要钱包连接 |
| ------------------------------------- | ---- | ------- | ------------ |
| **query-token-info**                  | Read | ✅ Live | 否           |
| **query-token-audit**                 | Read | ✅ Live | 否           |
| **query-address-info**                | Read | ✅ Live | 否           |
| **crypto-market-rank**                | Read | ✅ Live | 否           |
| **meme-rush**                         | Read | ✅ Live | 否           |
| **trading-signal**                    | Read | ✅ Live | 否           |
| **binance-tokenized-securities-info** | Read | ✅ Live | 否           |

### Agentic Wallet Skills

| Skill                      | 类别         | 状态    | 需要钱包连接 |
| -------------------------- | ------------ | ------- | ------------ |
| **binance-agentic-wallet** | Read + Write | ✅ Live | 是（写操作） |

---

## 已发布 Wallet Skills

### query-token-info

代币全面信息查询，从发现到深度分析一站解决。

**支持操作**

| 操作       | 说明                                                  |
| ---------- | ----------------------------------------------------- |
| 代币搜索   | 按名称、Symbol 或合约地址搜索，返回价格、市值、流动性 |
| 元数据查询 | 描述、创建者、审计状态、社交链接等静态信息            |
| 实时行情   | 多时间维度价格变化（5m/1h/4h/24h）、买卖量、持币分析  |
| K 线数据   | OHLCV K 线，支持 1s 到 1 月多种时间粒度               |

**支持链：** BSC、Base、Solana

```
BNB 现在多少钱？
查一下这个代币的持币分布
给我 SOL 过去 4 小时的 K 线数据
```

---

### query-token-audit

交易前安全审计，帮助识别风险合约和恶意代币。

**支持操作**

| 操作     | 说明                                        |
| -------- | ------------------------------------------- |
| 风险评分 | 输出 LOW / MEDIUM / HIGH 风险等级（1–5 分） |
| 蜜罐检测 | 识别能买不能卖的欺诈合约                    |
| 税率分析 | 返回买入/卖出税率，超过 10% 标记为高危      |
| 合约验证 | 检查源码是否已公开验证                      |

**支持链：** Ethereum、BSC、Base、Solana

> ⚠️ 审计结果仅供参考，LOW 风险不等于安全背书，请自行做好研究。

```
帮我审计一下这个合约地址是否安全
这个代币有没有蜜罐风险？
```

---

### query-address-info

查询指定钱包地址在链上持有的全部代币及估值。

**支持操作**

| 操作     | 说明                                 |
| -------- | ------------------------------------ |
| 持仓查询 | 返回地址所有代币余额、数量、合约地址 |
| 价格数据 | 每个代币当前 USD 价格及 24h 涨跌幅   |
| 分页支持 | 通过 offset 参数翻页查看大量持仓     |

**支持链：** BSC、Base、Solana

```
查一下这个地址持有哪些代币
0xABC... 在 BSC 上有什么仓位？
```

---

### crypto-market-rank

多维度加密货币市场排行榜，覆盖热度、资金流向、Meme 排名与交易者收益。

**支持操作**

| 操作           | 说明                                                         |
| -------------- | ------------------------------------------------------------ |
| 社交热度榜     | 按社区讨论量排名，含情绪分析（正/负/中性）                   |
| 综合排行榜     | 支持趋势币、搜索热榜、Binance Alpha 精选、代币化股票等多类型 |
| 智能钱包流入榜 | 聪明钱净买入最多的代币 TOP 榜                                |
| Meme 币榜      | Pulse 发射台前 100 Meme 代币，按爆发潜力评分                 |
| 交易者 PnL 榜  | 地址级别 7d/30d/90d 已实现盈亏排行                           |

**支持链：** BSC、Base、Solana

```
最近哪些代币社交热度最高？
聪明钱最近在买什么？
给我看 Binance Alpha 精选代币榜单
```

---

### meme-rush

Meme 代币实时追踪 + AI 热门话题发现，适合快节奏 Meme 交易场景。包含两大核心功能：

**Meme Rush — 发射台代币生命周期追踪**

| 操作       | 说明                                               |
| ---------- | -------------------------------------------------- |
| 新发代币   | 追踪处于 Bonding Curve 阶段的新上线代币            |
| 即将迁移   | 监控 Bonding Curve 接近完成、即将迁移到 DEX 的代币 |
| 已迁移代币 | 刚完成迁移的代币列表，捕捉早期流动性机会           |

**Topic Rush — AI 热门话题发现**

| 操作     | 说明                                    |
| -------- | --------------------------------------- |
| 最新话题 | 发现最新的市场热门话题及关联代币        |
| 上升话题 | 正在崛起的话题（历史最高流入 $1k–$20k） |

每个话题返回：话题名称、AI 摘要、净流入金额（总计/1h）、关联代币列表（含市值、流动性、净流入、持币人数等）。

**支持链：** Solana（Pump.fun、Raydium 等）、BSC（Four.meme、Flap 等）

```
Solana 上最新上线的 Meme 有哪些？
有哪些 Meme 快要迁移到 DEX 了？
现在什么话题最火？
有哪些正在崛起的热门话题？
```

---

### trading-signal

监控链上聪明钱交易行为，输出结构化买卖信号供参考。

**支持操作**

| 操作     | 说明                                                         |
| -------- | ------------------------------------------------------------ |
| 信号获取 | 聪明钱地址在 Solana / BSC 上的买卖信号                       |
| 价格比对 | 信号触发价 vs 当前价，判断是否已错过入场时机                 |
| 信号质量 | 返回历史最大涨幅（maxGain）和聪明钱退出比例（exitRate）      |
| 代币标签 | 标注社交事件、发射平台（Pumpfun 等）、敏感事件（巨鲸买卖等） |
| 信号状态 | 区分 active / timeout / completed，聚焦仍有效信号            |

**支持链：** Solana、BSC

```
最近有哪些聪明钱买入信号？
BNB Chain 上有没有新的链上信号？
这个信号自触发后最高涨了多少？
```

---

### binance-tokenized-securities-info

查询 Ondo Finance 代币化美股在链上的实时数据与状态。

**支持操作**

| 操作         | 说明                                                             |
| ------------ | ---------------------------------------------------------------- |
| 资产列表     | 所有支持的代币化股票及合约地址                                   |
| 公司信息     | CEO、行业、概念标签、证明报告链接                                |
| 市场状态     | Ondo 市场是否开放/暂停，下次开收盘时间                           |
| 企业行动     | 每只代币的停牌状态（分拆、派息、并购等）                         |
| 实时链上行情 | 代币价格、24h 涨跌、持有人数、流通量、市值，及 PE/股息率等基本面 |
| K 线数据     | OHLC 数据，支持 1 分钟到 1 天多种粒度                            |

**支持链：** Ethereum、BSC

> 注意：每个代币代表 `multiplier` 股而非 1 股，价格换算需除以 sharesMultiplier。

```
当前 Ondo 市场开放了吗？
查一下 AAPL 代币化股票的当前价格
有哪些代币化股票因企业行动停牌了？
```

---

## Agentic Wallet Skill

`binance-agentic-wallet` 提供钱包管理、代币转账、市价兑换、限价单、预测市场交易和 DeFi 功能。

→ 详见 [Agentic Wallet 文档](/products/agentic-wallet/welcome)

---

## 相关页面

- [Binance Wallet Skills 概览](/products/wallet-skills/overview)