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
source_url: 'https://docs.polymarket.com/cn/programs/builders/fees'
updated_at: 2026-11-13
---

# Builder 费用

> 从通过你的应用路由的订单中赚取费用

Builder 费用允许 Builder 从通过其应用路由的已撮合订单中获得收入。在签署订单前附加你的 **Builder Code**，即可在适用的平台费用之外收取配置的费用。

Builder 费用是交易名义价值的固定百分比。如果平台费用也适用，两者会叠加收取。

> [!NOTE]
>
> 第一次使用 Builder 计划？请先阅读 [Builder
> 计划](https://docs.polymarket.com/cn/programs/builders/overview.md)。本页专门介绍费用层。

***

## 工作原理

![](https://mintcdn.com/polymarket-292d1b1b/lWwKl4XdsXxYugaA/images/core-concepts/builder-fee.png?fit=max\&auto=format\&n=lWwKl4XdsXxYugaA\&q=85\&s=9287dc95f24f07bcb9f33c4d7d6ed0f2)

Builder 费用与平台费用相互独立。用户实际支付的费用取决于市场配置，以及订单是否附有 Builder Code：

| 市场 | 附有 Builder Code | 用户支付 |
| - | - | - |
| 无平台费用 | 否 | 无费用 |
| 无平台费用 | 是 | 仅 Builder 费用 |
| 已启用平台费用 | 否 | 仅平台费用 |
| 已启用平台费用 | 是 | 平台费用 + Builder 费用 |

Builder 费用绝不会取代平台费用，而是始终叠加收取。

> [!WARNING]
>
> Polymarket 保留自行决定撤销你收取 Builder
> 费用权限的权利，无论是否说明理由，包括但不限于费用被认定为通过欺诈、欺骗、误导、自动化、自我推荐或其他非真实交易活动收取的情况。

***

## 注册

通过你的 Polymarket 账户注册 Builder Code。

**1. 创建 Builder 资料**

打开 polymarket.com → Settings →
[Builders](https://polymarket.com/settings?tab=builder)，然后设置你的
Builder 资料。

**2. 设置费率**

在资料中配置两种费率： - **Taker Fee Rate** — 对通过你的应用路由的 Taker
订单收取 - **Maker Fee Rate** — 对通过你的应用路由的 Maker 订单收取

**3. 复制 Builder Code**

系统会为你的资料分配一个 `bytes32` Builder Code。[将其附加到你提交的每个订单
上](https://docs.polymarket.com/cn/trading/place-orders.md#构建者归因)。

### 费率限制

| 参数 | 默认值 | 最大值 |
| - | - | - |
| Taker 费率 | 0 bps (0%) | 100 bps (1%) |
| Maker 费率 | 0 bps (0%) | 50 bps (0.5%) |
| 最小调整幅度 | — | 1 bp (0.01%) |

### 费率变更政策

费率变更受到以下限制，以便用户提前知晓：

* \*\*冷却期。\*\*每 7 天只能变更一次费率。
* \*\*提前通知。\*\*变更在安排后的 3 天生效。
* \*\*一次只能有一项待处理变更。\*\*不能将多项变更排队；必须等待当前变更生效（或将其取消），才能安排下一项。

***

## 费用计算

### 平台费用

平台费用使用按市场动态计算的公式：

```
platform_fee = C × feeRate × p × (1 - p)
```

其中，`C` 是交易规模，`p` 是订单价格，`feeRate` 是按市场设置的参数。目前仅向 Taker 收取平台费用，Builder 无法配置该费用。

### Builder 费用

Builder 费用是名义价值的固定百分比：

```
builder_fee = notional × builder_fee_rate_bps / 10000
```

\*\*示例。\*\*一笔通过某 Builder 路由的 1,000 pUSD Taker 买单，该 Builder 的 Taker 费率为 100 bps (1%)：

```
builder_fee = 1000 × 100 / 10000 = 10 pUSD
```

一笔交易的 Maker 和 Taker 两侧可以使用不同的 Builder Code 和不同的费率。如果 Builder A（Maker 费率 0.3%）提交挂单，而 Builder B（Taker 费率 0.8%）提交与之撮合的订单，则双方分别从各自一侧赚取相应费用。

### 余额检查

账户必须有足够的 pUSD 支付交易以及所有适用的平台费用和 Builder 费用。对于市价买单，请[设置包含费用的支出上限](https://docs.polymarket.com/cn/trading/place-orders.md#限制市价买单支出)，以便在签名前根据费用调整订单金额。

***

## 链上归因

Builder 归因是已签名订单的一部分，适用于 CTF 合约和 Polymarket Protocol V2。

### 选择签名域

手动签名时，请使用 Gamma 市场的 `version`。两个签名域使用相同的订单字段。

| Gamma `version` | EIP-712 domain version | 结算合约 |
| - | - | - |
| `"v2"` | `"3"` | Polymarket V2 Exchange |
| `"v1"` | `"2"` | 根据 `negRisk` 选择 CTF Exchange 或 Neg Risk CTF Exchange |

SDK 会根据结果 ID 选择签名域。完整签名工作流请参阅[下限价单](https://docs.polymarket.com/cn/trading/place-orders.md#下限价单)。

### 已签名订单结构

```
salt, maker, signer, tokenId, makerAmount, takerAmount,
side, signatureType, timestamp, metadata, builder
```

`builder` 字段是与你已注册 Builder Code 匹配的 `bytes32`。`tokenId` 字段包含结果 ID，可以是 CTF 代币 ID 或 Polymarket Protocol V2 Position ID。

每个结算合约都会发出包含已签名 `builder` 值的 `OrderFilled`。跨两种持仓系统对账时，请索引 CTF Exchange、Neg Risk CTF Exchange 和 Polymarket Protocol V2 Exchange 的事件。

***

## 费用处理和支付

当用户下单并附加你的 `builderCode` 时：

1. CLOB 验证订单和 Builder Code。
2. 撮合时，系统分别计算交易两侧的平台费用和 Builder 费用。
3. 交易通过市场选定的 exchange 结算，并发出 `OrderFilled` 事件。
4. 系统使用已撮合的 Builder Code 将收入计入对应的 Builder 资料。

收取的 Builder 费用会分发到与你的 Builder 资料关联的钱包。

### 支付时间

Builder 费用每天支付一次。每次支付涵盖前一个 UTC 日内赚取的 Builder 费用。

最低 Builder 费用支付金额为 **\$0.10**。如果你在某个 UTC 日的 Builder 费用总额低于该金额，则当天不会发放支付。

***

## 计划政策

### 已停用的 Code

Polymarket 可随时因违反 Builder 计划条款、滥用费率或平台完整性问题而停用 Builder Code。携带已停用 Code 的订单会被 CLOB 拒绝。

### 公开可见性

Builder 资料和费率可供公开查询。这一设计让用户和第三方可以在使用 Builder 应用前了解其收费标准。


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
