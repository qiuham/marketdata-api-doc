---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/agentic-wallet/use-cases/trading/defi
api_type: Guide
updated_at: 2026-11-26 18:44:28.070042
---

# DeFi

## 🎯 Goal

Put your assets to work across DeFi protocols — check positions, deposit to earn, redeem, provide or
remove liquidity, and claim rewards, all through conversation.

## ✅ Prerequisites

- Agentic Wallet [installed](../../quickstart/install-agentic-wallet) and signed in.
- Enough balance of the asset you want to deposit or provide, plus native token for gas.

## Browse protocols & investment products

> "What DeFi protocols are supported?"

> "Show me earn options for USDT"

> "What's the APY for depositing BNB?"

> "List available LP pools"

The Agent walks you through the options in plain language — for example: "Supported protocols
include Venus, Lista DAO, and PancakeSwap. For USDT earn, Venus is offering around 4.2% APY, and
depositing BNB into Lista DAO earns roughly 3.8%. There are also several LP pools available, such as
BNB/USDT and ETH/USDT on PancakeSwap."

## Check DeFi positions

> "What are my current DeFi positions?"

> "How much am I earning?"

> "Show me my LP positions — are any out of range?"

> "Do I have any claimable rewards?"

The Agent summarizes your positions in plain language — for example: "You have 100 USDT supplied on
Venus earning ~4.2% APY, and a BNB/USDT LP position on PancakeSwap that's currently in range. You
have about 0.8 USDT of unclaimed rewards ready to collect."

## Deposit

> "Deposit 100 USDT to Venus"

> "Deposit 0.5 BNB into Lista DAO"

The Agent will show a transaction preview (balance changes, gas fee, contract address) before
execution. Confirm to proceed.

## Redeem

> "Redeem my USDT from Venus"

> "Redeem all my BNB from Lista DAO"

The Agent previews the redemption and confirms once it's done — for example: "I've redeemed your 100
USDT from Venus plus about 0.4 USDT of accrued interest. The funds are back in your wallet."

## Add liquidity

> "Add liquidity to the BNB/USDT pool on PancakeSwap"

> "Provide 500 USDT and equivalent BNB to PancakeSwap BNB/USDT"

For concentrated liquidity pools, the Agent will use the protocol's default price range unless you
specify otherwise. It previews the pairing and confirms once the position is open — for example:
"I've added 500 USDT and about 0.8 BNB to the PancakeSwap BNB/USDT pool. Your LP position is now
active and in range."

## Remove liquidity

> "Remove my liquidity from PancakeSwap BNB/USDT pool"

> "Remove 50% of my LP position on PancakeSwap"

The Agent confirms the withdrawal in plain language — for example: "I've removed 50% of your
BNB/USDT LP position. About 250 USDT and 0.4 BNB have been returned to your wallet, along with any
fees earned."

## Claim rewards / LP fee / redemption

> "Claim my LP fee income from PancakeSwap"

> "Claim my redemption assets of Lista DAO"

The Agent claims and confirms in plain language — for example: "I've claimed your accrued LP fees
from PancakeSwap — about 0.8 USDT and a small amount of BNB have been credited to your wallet."

## Transaction status

After submitting a DeFi transaction, you can check its status:

> "Has my deposit to Venus gone through?"

> "Check my recent DeFi transactions"

The Agent reports the status in plain language — for example: "Your 100 USDT deposit to Venus was
confirmed on-chain a moment ago and now shows in your positions. Your other recent DeFi transactions
have all completed successfully." Each transaction's status maps to one of the following:

| Status    | Description                                           |
| --------- | ----------------------------------------------------- |
| `PENDING` | Transaction broadcast, awaiting on-chain confirmation |
| `SUCCESS` | Executed successfully                                 |
| `FAILED`  | Transaction reverted on-chain                         |

## Post-trade verification

After every DeFi transaction, the Agent automatically verifies:

1. On-chain transaction receipt (success/revert)
2. Position balance change matches expected amount
3. Updated position reflected in portfolio
4. App push notification sent with result

## ⚠️ Risk notice

DeFi deposits and liquidity provision are not risk-free: protocols carry smart-contract risk
(undetected bugs, hacks), you may be exposed to impermanent loss and liquidation in leveraged or
borrowing positions, and APY/rewards are variable and not guaranteed. On-chain trading also involves
slippage, MEV attacks, and gas-price volatility. Always confirm the contract address the Agent
previews before approving, and base every decision on your own research (DYOR) — Skills provide
information and execution capability only, never investment advice.

## What's next

- [Market Order](./market-order) — Swap tokens to fund your DeFi positions.
- [Automated Strategies](../automated-strategies) — Combine DeFi with Skills for hands-off yield.

---

# DeFi

## 🎯 目标

让你的资产在各类 DeFi 协议中运转起来——查看持仓、存入生息、赎回、提供或移除流动性、领取奖励，全部通过对话完成。

## ✅ 前置条件

- 已[安装](../../quickstart/install-agentic-wallet) Agentic Wallet 并登录。
- 有足够的待存入或待提供资产余额，以及用于 gas 的原生代币。

## 浏览协议与投资产品

> "支持哪些 DeFi 协议？"

> "看看 USDT 的生息选项"

> "存入 BNB 的 APY 是多少？"

> "列出可用的 LP 池"

AI Agent 会用自然语言为你逐一介绍选项——例如："支持的协议包括 Venus、Lista
DAO 和 PancakeSwap。USDT 生息方面，Venus 目前提供约 4.2% APY，把 BNB 存入 Lista
DAO 约可获得 3.8%。还有若干 LP 池可用，比如 PancakeSwap 上的 BNB/USDT 和 ETH/USDT。"

## 查看 DeFi 持仓

> "我当前的 DeFi 持仓有哪些？"

> "我赚了多少？"

> "看一下我的 LP 持仓——有超出区间的吗？"

> "我有可领取的奖励吗？"

AI Agent 会用自然语言总结你的持仓——例如："你在 Venus 上供应了 100 USDT，赚取约 4.2%
APY，还有一笔 PancakeSwap 上的 BNB/USDT LP 持仓当前在区间内。你有约 0.8 USDT 未领取的奖励可以领取。"

## 存入

> "存 100 USDT 到 Venus"

> "把 0.5 BNB 存入 Lista DAO"

AI Agent 会在执行前展示交易预览（余额变化、gas 费、合约地址）。确认以继续。

## 赎回

> "从 Venus 赎回我的 USDT"

> "从 Lista DAO 赎回我所有的 BNB"

AI Agent 会预览赎回并在完成后确认——例如："我已从 Venus 赎回你的 100 USDT，外加约 0.4
USDT 的累计利息。资金已回到你的钱包。"

## 添加流动性

> "向 PancakeSwap 上的 BNB/USDT 池添加流动性"

> "向 PancakeSwap BNB/USDT 提供 500 USDT 及等值 BNB"

对于集中流动性池，除非你另行指定，AI
Agent 会使用协议的默认价格区间。它会预览配对并在持仓开立后确认——例如："我已向 PancakeSwap
BNB/USDT 池添加 500 USDT 和约 0.8 BNB。你的 LP 持仓现已激活并处于区间内。"

## 移除流动性

> "从 PancakeSwap BNB/USDT 池移除我的流动性"

> "移除我在 PancakeSwap 上 50% 的 LP 持仓"

AI Agent 会用自然语言确认提取——例如："我已移除你 50% 的 BNB/USDT LP 持仓。约 250 USDT 和 0.4
BNB 已返还到你的钱包，连同已赚取的手续费。"

## 领取奖励 / LP 手续费 / 赎回

> "领取我在 PancakeSwap 的 LP 手续费收益"

> "领取我在 Lista DAO 的赎回资产"

AI Agent 会领取并用自然语言确认——例如："我已领取你在 PancakeSwap 累计的 LP 手续费——约 0.8
USDT 和少量 BNB 已计入你的钱包。"

## 交易状态

提交 DeFi 交易后，你可以查看其状态：

> "我存到 Venus 的那笔到账了吗？"

> "查一下我最近的 DeFi 交易"

AI Agent 会用自然语言报告状态——例如："你存入 Venus 的 100
USDT 刚刚已在链上确认，现已显示在你的持仓中。你其他最近的 DeFi 交易也都已成功完成。"每笔交易的状态对应以下之一：

| 状态      | 说明                     |
| --------- | ------------------------ |
| `PENDING` | 交易已广播，等待链上确认 |
| `SUCCESS` | 已成功执行               |
| `FAILED`  | 交易在链上回滚           |

## 交易后核验

每笔 DeFi 交易后，AI Agent 会自动核验：

1. 链上交易回执（成功/回滚）
2. 持仓余额变化与预期金额一致
3. 更新后的持仓已反映在投资组合中
4. 已发送 App 推送通知告知结果

## ⚠️ 风险提示

DeFi 存入与提供流动性并非没有风险：协议存在智能合约风险（未被发现的漏洞、黑客攻击），在杠杆或借贷持仓中你可能面临无常损失和清算，且 APY/奖励是浮动的、不保证兑现。链上交易还涉及滑点、MEV 攻击和 gas 价格波动。请务必在批准前确认 AI
Agent 预览的合约地址，并基于你自己的研究（DYOR）做出每一个决定——Skill 只提供信息和执行能力，绝不构成投资建议。

## 下一步

- [市价单](./market-order) —— 兑换代币来为你的 DeFi 持仓提供资金。
- [自动化策略](../automated-strategies) —— 把 DeFi 与 Skill 结合，实现无需盯盘的收益。