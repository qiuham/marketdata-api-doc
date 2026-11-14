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
source_url: 'https://docs.polymarket.com/cn/trading/positions/combinatorial'
updated_at: 2026-11-13
---

# 组合持仓

> 了解 Combos 使用的 PositionManager 持仓。

组合持仓将多个市场结果合并成一对 YES 和 NO 持仓。Polymarket 使用这些持仓表示 Combos。

## 持仓含义

只有每条腿都获得支付时，组合 YES 持仓才会获得支付。对于以下三腿 condition：

```text theme={null}
YES(Market A) and YES(Market B) and NO(Market C)
```

三个陈述全部为真时，YES 持仓获胜。对应的 NO 持仓获得互补支付。

| 持仓 | 支付 |
| - | - |
| YES | 各腿支付的乘积 |
| NO | 1 减去 YES 支付 |

如果每条腿都结算为 `0` 或 `1`，Combo 会得到二元结果。腿的分数支付会产生 Combo 的分数支付。

[结算为 50/50](https://docs.polymarket.com/cn/concepts/resolution.md) 的腿支付 `0.5`，并且仍保留在组合中，不会被移除。例如，一条腿结算为 50/50 且其余腿全部获胜时，YES 每个代币支付 \$0.50；两条腿结算为 50/50 时支付 \$0.25。腿所在事件被取消或延期时是否结算为 50/50，取决于该腿市场的规则。

## PositionManager 表示方式

组合持仓不是 Gnosis CTF 代币。PositionManager 管理余额，CombinatorialModule 使用模块 ID `3`。

每条腿都必须是来自 BinaryModule 或 NegRiskModule 的 Polymarket Protocol V2 Position ID。SDK 会对腿排序。模块会拒绝重复和相互矛盾的结果，然后为这组腿派生一个 condition ID。

> [!NOTE]
>
> 一个市场可以同时提供用于 CLOB 交易的 CTF 代币 ID 和用于 Combo 腿的 Position
> ID。构建 Combo 时，始终使用 Combo 市场目录中的 Position ID。

## 创建和移除完整持仓

拆分 pUSD 会创建数量相等的 Combo YES 和 NO 余额。合并相等余额会返还 pUSD。

```text theme={null}
1 pUSD ⇄ 1 Combo YES + 1 Combo NO
```

首次拆分前，CombinatorialModule 必须知道按顺序排列的腿集合。SDK 工作流会在需要时准备 condition。直接调用者应先用升序排列的 Position ID 调用 `prepareCondition()`，再在 Router 上调用 `split()` 或 `merge()`。

## 交易结构

Polymarket Protocol V2 Exchange 将每个 Combo 作为二元结构市场进行交易。订单使用派生的 YES 或 NO Position ID 作为订单资产。由于 `tokenId` 是已签名订单字段名，线上字段仍为 `tokenId`。

## 结算

CombinatorialModule 从每条腿已注册的模块读取其支付。最终支付可以确定时，持仓即可赎回。

部分腿结算后，尚未结算的持仓有时可以压缩。压缩会返还已经解锁的抵押品，并为尚未结算的敞口铸造一个更小的剩余持仓。支持的规划工作流请参阅[抵押品返还](https://docs.polymarket.com/trading/combos/collateral-return.md)。

## 相关页面

> [card] [持仓运作方式](https://docs.polymarket.com/cn/trading/positions/how-positions-work.md)
>
> 比较两种持仓账本。

> [card] [管理持仓](https://docs.polymarket.com/cn/trading/positions/manage.md)
>
> 拆分、合并和赎回持仓。

> [card] [Combos](https://docs.polymarket.com/cn/trading/combos/overview.md)
>
> 通过 RFQ 为组合持仓报价。


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
