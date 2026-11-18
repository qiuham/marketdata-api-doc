---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/agentic-wallet/reference/skills
api_type: Guide
updated_at: 2026-11-18 02:28:55.418437
---

# Skills Reference

The `binance-agentic-wallet` skill provides wallet management and on-chain trading through the `baw`
CLI.

**Supported chains:** BNB Smart Chain (BSC), Ethereum, Base, Solana

---

## Skill Documentation Structure

```
binance-agentic-wallet/
├── SKILL.md                      # Main doc: command routing, security policy, common token addresses
└── references/
    ├── preflight.md              # Preflight checks: skill version, CLI version
    ├── authentication.md         # Sign-in/sign-out flow
    ├── wallet-view.md            # Wallet queries: status, address, balance, history, etc.
    ├── wallet-setting.md         # Security settings (read-only)
    ├── send.md                   # Token transfer
    ├── market-order.md           # Market order (swap)
    ├── limit-order.md            # Limit order
    ├── prediction.md             # Prediction market trading
    ├── defi.md                   # DeFi data and transactions (deposit, redeem, LP, claim)
    └── security.md               # Pre-trade security check flow
```

---

## Key Features

### Wallet Management

Query wallet status, addresses, balances, transaction history, and security settings.

```
Is my wallet connected?
What's my wallet address?
How much BNB and USDT do I have?
Show me my recent transactions
How much of my daily limit is left?
```

### Token Transfer

Send tokens to addresses in your address book (Binance App → Wallet → Settings → Address Book).

```
Send 0.02 BNB to 0x1234...5678
Transfer 10 USDT to 0x1234...5678
```

### Market Swap

Get quotes or execute swaps at current market price. Supports custom slippage and MEV protection.

```
How much USDT would I get for 0.1 BNB? Quote only
Swap 0.1 BNB for USDT
Buy BNB with 50 USDT, max slippage 2%
```

### Limit Order

Set a target price — executes automatically when triggered.

> **Note:** Limit orders are only supported on BSC and Solana.

```
Buy BNB with 100 USDT when the price drops to $500
Sell 1 BNB for USDT when the price reaches $650
Show my open limit orders
Cancel my BNB limit order
```

### Prediction Market

Trade on prediction markets — browse markets, place bets on outcomes, track positions, and redeem
winnings.

```
Search the most popular market in the sport category
Buy "Up" in the most recent BTC 15m price market
What are my current prediction positions?
Show my prediction PnL
Redeem my winning predictions
Cancel my pending prediction order
```

### DeFi

Query DeFi protocols, investment products, and positions. Execute deposit / redeem / LP add / LP
remove / claim transactions on supported protocols.

```
What DeFi protocols are supported?
Show me earn options for USDT
What are my current DeFi positions?
Deposit 100 USDT to Venus
Add liquidity to the BNB/USDT pool on PancakeSwap
Claim my LP fee income from PancakeSwap
```

---

## Related

- [Install Agentic Wallet](../quickstart/install-agentic-wallet.md)
- [Use Cases Overview](../use-cases/overview.md)

---

# Skills 参考

`binance-agentic-wallet` Skill 通过 `baw` CLI 提供钱包管理和链上交易功能。

**支持链：** BNB Smart Chain (BSC)、Ethereum、Base、Solana

---

## Skill 文档结构

```
binance-agentic-wallet/
├── SKILL.md                      # 主文档：命令路由、安全策略、常用代币地址
└── references/
    ├── preflight.md              # 预检流程：Skill 版本检查、CLI 版本检查
    ├── authentication.md         # 登录/登出流程
    ├── wallet-view.md            # 钱包查询：状态、地址、余额、交易记录等
    ├── wallet-setting.md         # 安全设置（只读）
    ├── send.md                   # 代币转账
    ├── market-order.md           # 市价兑换
    ├── limit-order.md            # 限价单
    ├── prediction.md             # 预测市场交易
    ├── defi.md                   # DeFi 数据与交易（存入、赎回、流动性、领取）
    └── security.md               # 交易前安全预检流程
```

---

## 主要功能

### 钱包管理

查询钱包状态、地址、余额、交易记录、安全设置等。

```
我的钱包连接正常吗？
我的钱包地址是什么？
我有多少 BNB 和 USDT？
查一下我最近的交易记录
今天还剩多少可用额度？
```

### 代币转账

向通讯录地址转账代币。收款地址须在 Binance App 通讯录中。

```
发送 0.02 BNB 到 0x1234...5678
转 10 USDT 给 0x1234...5678
```

### 市价兑换

获取报价或以当前市价执行代币兑换。支持自定义滑点和 MEV 保护。

```
把 0.1 BNB 换成 USDT 大概能换多少？只看报价
把 0.1 BNB 换成 USDT
用 50 USDT 买 BNB，滑点控制在 2%
```

### 限价单

设定目标价格，价格到达时自动执行。

> **注意：** 限价单仅支持 BSC 和 Solana。

```
BNB 价格跌到 $500 时，用 100 USDT 买入
BNB 涨到 $650 时，卖出 1 BNB 换 USDT
查看我的挂单
取消我的 BNB 限价单
```

### 预测市场

在预测市场中交易 — 浏览市场、下注结果、跟踪持仓、赎回收益。

```
搜索体育类最热门的预测市场
在最近一期 BTC 15 分钟价格市场中买入"涨"
我当前的预测持仓有哪些？
查看我的预测盈亏
赎回我的预测收益
取消我的待处理预测订单
```

### DeFi

查询 DeFi 协议、投资产品和持仓。在支持的协议上执行存入 / 赎回 / 添加流动性 / 移除流动性 / 领取交易。

```
支持哪些 DeFi 协议？
给我看看 USDT 的理财选项
我当前的 DeFi 持仓有哪些？
存 100 USDT 到 Venus
在 PancakeSwap 的 BNB/USDT 池添加流动性
领取我在 PancakeSwap 的 LP 手续费收益
```

---

## 相关页面

- [安装 Agentic Wallet](../quickstart/install-agentic-wallet.md)
- [使用场景概览](../use-cases/overview.md)