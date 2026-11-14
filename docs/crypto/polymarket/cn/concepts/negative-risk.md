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
source_url: 'https://docs.polymarket.com/cn/concepts/negative-risk'
updated_at: 2026-11-13
---

# 负风险市场

> 多结果事件的资金高效交易方式

**负风险**会关联同一事件中只有一个结果可以获胜的多个市场。**转换**会把一个市场的 No 持仓换成其他市场的 Yes 持仓。

## 运作方式

在普通的多结果事件中，每个市场相互独立。在负风险事件中：

* 一个市场的 **No 持仓**代表对其他所有结果的敞口
* 转换会把该 No 持仓换成互补的 Yes 持仓

### 示例

假设事件是“谁会赢得 2024 年美国总统选举？”，并包含三个结果：

| 结果 | 你的持仓 |
| - | - |
| Trump | 无 |
| Harris | 无 |
| Other | 1 No |

通过负风险转换，“Other”的 1 个 No 持仓可以转换为：

| 结果 | 转换后的持仓 |
| - | - |
| Trump | 1 Yes |
| Harris | 1 Yes |
| Other | 无 |

这个 No 持仓代表与其他所有结果的 Yes 持仓相同的敞口。

## 实现方式

CTF 合约通过 Neg Risk Adapter 关联独立的二元市场。部分事件会预留占位市场，并设置明确的 Other 市场，以便在交易开始后命名新结果。

Polymarket Protocol V2 通过 Router 调用 NegRiskModule 处理负风险。同一模块支持已命名结果、占位结果和 Other，不存在单独的 augmented mode。增强型负风险同时适用于 CTF 和 Polymarket Protocol V2 市场。

合约地址请参阅[合约](https://docs.polymarket.com/cn/resources/contracts.md)。

> [!WARNING]
>
> 只交易**已命名结果**。占位结果命名前不要交易。Polymarket UI 会隐藏未命名结果。

如果获胜结果没有分配给已命名的 condition，则 Other 获胜。

## 转换示例

转换操作是原子操作，两种系统的转换结果相同：

1. 你持有结果 A 的 1 个 No 持仓
2. 通过该市场的负风险路径转换持仓
3. 你会获得事件中其他每个结果的 1 个 Yes 持仓

准确的授权、合约目标和调用请参阅[持仓工作流](https://docs.polymarket.com/cn/trading/positions/how-positions-work.md)。

## 后续步骤

> [card] [市场与事件](https://docs.polymarket.com/cn/concepts/markets-events.md)
>
> 了解多市场事件的结构。

> [card] [持仓与代币](https://docs.polymarket.com/cn/concepts/positions-tokens.md)
>
> 了解拆分、合并和赎回等持仓操作。


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
