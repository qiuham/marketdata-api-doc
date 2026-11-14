---
api_type: reference
source_type: llms_txt
version: ''
scope: crypto
asset_class: prediction_market
domain: exchanges
provider: polymarket
provider_name: Polymarket
product: api
product_id: polymarket
source_url: 'https://docs.polymarket.com/cn/polymarket-101'
updated_at: 2026-11-13
---

# Polymarket 101

> Polymarket 简介——全球最大的预测市场

Polymarket 是一个预测市场平台，用户可以在这里交易现实世界事件的结果。你并非与庄家对赌，而是在开放的点对点市场中与其他用户交易份额。价格反映了市场对某一事件发生概率的集体判断。

平台采用非托管模式，你始终掌控自己的资金。所有交易通过区块链上的智能合约结算，确保操作透明且无需信任第三方。

## 自托管

Polymarket 采用非托管模式，你始终对自己的资金拥有完全控制权。

* 资产存放在你的钱包中，由你的私钥保护。
* 交易通过经过审计的智能合约自动执行。
* Polymarket 永远不会占有你的资金。
* 所有交易和持仓均记录在链上，可公开验证。
* 结算根据市场判定结果自动完成。

> [!WARNING]
>
> 请妥善保管你的私钥，切勿与任何人分享。如果丢失私钥，你将无法访问资金。如果你是通过
> Magic Link 注册的或拥有代理钱包，可以通过
> [recovery.polymarket.com](https://recovery.polymarket.com) 尝试恢复。

## Polymarket 运作机制

![Polymarket Overview](https://mintcdn.com/polymarket-292d1b1b/FOMte3ewbG-LVy3k/images/core-concepts/polymarket-101.png?fit=max\&auto=format\&n=FOMte3ewbG-LVy3k\&q=85\&s=059e9831d1c51b99996d9747c0139d49)

### 价格即概率

Polymarket 上每个份额的价格在 `$0.00` 到 `$1.00` 之间。价格代表市场对该结果发生概率的判断。

例如，如果某事件的 "Yes" 份额交易价格为 `$0.65`，意味着市场认为该事件发生的概率约为 `65%`。

### 抵押品与代币

Polymarket 使用 pUSD（Polymarket USD）作为抵押品。每一对 Yes/No 份额都有完全的资金支撑：

* `$1 pUSD` 可铸造一份 Yes 份额和一份 No 份额
* 获胜份额可兑换 `$1.00`
* 失败份额价值 `$0.00`

份额是 Polygon 上的 ERC-1155 代币余额。使用哪个账本取决于市场的持仓系统：

* **Polymarket Protocol V2**：PositionManager 将每个结果记录为持仓余额
* **CTF 合约**：Gnosis Conditional Tokens 将每个结果记录为 CTF 代币余额

两套系统都表示相同的 Yes 和 No 份额。区别在于集成所用的标识符和链上路径，不会改变交易者对 Yes 和 No 价格的理解。

### 交易

Polymarket 使用点对点订单簿（CLOB）进行交易。你直接与其他用户交易，而非与庄家对赌。

* **买入份额** — 当你认为市场低估了某一结果的概率
* **卖出份额** — 当你认为市场高估了某一结果的概率
* **随时退出** — 在判定结果公布前卖出持仓，锁定利润或止损

| 操作 | 适用场景 | 盈利条件 |
| - | - | - |
| 买入 Yes | 你认为概率被市场低估了 | 事件发生 |
| 买入 No | 你认为概率被市场高估了 | 事件未发生 |
| 卖出 | 锁定收益或控制亏损 | 价格朝有利方向变动 |

### 判定

事件结束后，市场规则决定最终赔付。CTF 市场和 Polymarket Protocol V2 市场使用不同的链上判定路径。赔付结果确定后，获胜结果代币或持仓可兑换为 pUSD。

有关两条路径如何得出最终赔付，请参阅[判定](https://docs.polymarket.com/cn/concepts/resolution.md)。

## 为什么选择区块链

Polymarket 构建在 **Polygon** 区块链网络上，主要基于以下原因：

* **全球可访问** — 任何有互联网连接的人都可以参与
* **非托管** — 资金由你掌控，而非中心化机构
* **透明** — 所有活动均可在链上公开验证
* **快速且低成本** — Polygon 提供快速、低费用的交易体验
* **价值稳定** — pUSD 是由 USDC 背书的标准 ERC-20 代币，背书由智能合约在链上强制执行 — 避免加密货币的价格波动

## 智能钱包

Polymarket 使用智能钱包，使用户无需手动提交每一笔链上交易即可交易。新的 API 用户使用存款钱包；现有 Safe 和 Proxy 用户可以继续使用当前钱包。

存款钱包在 Polygon 上持有用户的 pUSD 和结果代币，并通过 ERC-1271 验证订单。现有用户和集成仍可使用 Safe 和 Proxy 钱包。

智能钱包让 Polymarket 能够提供更好的用户体验：多步骤交易可以原子化执行，交易也可以由 Polymarket 的中继器转发。如果你是希望以编程方式访问现有 Polymarket 账户持仓的开发者，请继续使用该账户当前的智能钱包类型。

### 部署地址

每位智能钱包用户都有自己的钱包地址。有关 Polygon 上所有已部署的工厂和交易合约地址，请参阅[合约](https://docs.polymarket.com/cn/resources/contracts.md)。

***

## 开始使用

准备好开始交易了吗？

> [card] [交易快速入门](https://docs.polymarket.com/cn/trading/quickstart.md)
>
> 设置账户并完成第一笔交易。

> [card] [浏览市场](https://polymarket.com)
>
> 在 Polymarket 上浏览活跃的预测市场。


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
