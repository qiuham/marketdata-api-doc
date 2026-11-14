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
source_url: 'https://docs.polymarket.com/cn/trading/positions/how-positions-work'
updated_at: 2026-11-13
---

# 持仓运作方式

> 了解 Polymarket 的结果持仓、账本和标识符。

Polymarket 将可交易结果表示为 ERC-1155 余额。每个二元市场都有一个 YES 持仓和一个 NO 持仓，但管理这些余额的合约取决于市场的持仓系统。

## 持仓系统

| 持仓系统 | ERC-1155 账本 | 市场逻辑 | 结果标识符 |
| - | - | - | - |
| Polymarket V2 | PositionManager | BinaryModule、NegRiskModule 或 CombinatorialModule | Position ID |
| CTF | Conditional Tokens | 标准 CTF 或 Neg Risk Adapter | CTF 代币 ID |

不要将 CTF 代币 ID 传给 PositionManager，也不要将 Position ID 传给 Conditional Tokens。市场发现数据会提供每个工作流所需的标识符。

## 持仓生命周期

两种系统都提供相同的基本持仓生命周期。

> [card] [拆分](https://docs.polymarket.com/cn/trading/positions/manage.md#拆分持仓)
>
> 将 pUSD 转换为数量相同的 YES 和 NO 余额。

> [card] [合并](https://docs.polymarket.com/cn/trading/positions/manage.md#合并持仓)
>
> 将数量相同的 YES 和 NO 余额转换回 pUSD。

> [card] [赎回](https://docs.polymarket.com/cn/trading/positions/manage.md#赎回已结算持仓)
>
> 销毁已结算持仓并获得对应支付。

![pUSD 可以拆分为 YES 和 NO 持仓，这些持仓可以交易、合并，或在结算后赎回。](https://mintcdn.com/polymarket-292d1b1b/FOMte3ewbG-LVy3k/images/core-concepts/token-flow.png?fit=max\&auto=format\&n=FOMte3ewbG-LVy3k\&q=85\&s=36f5a57946ac2b83136e17b6c06b358c)

## CTF 合约

Conditional Tokens 管理结果余额。CTF 代币 ID 由抵押代币、condition ID 和结果 collection 派生。

| 市场类型 | 持仓操作 | 交易合约 |
| - | - | - |
| 标准二元市场 | `CtfCollateralAdapter` | CTF Exchange |
| 负风险市场 | `NegRiskCtfCollateralAdapter` | Negative Risk CTF Exchange |

对于二元 condition，index set `1` 标识 YES，index set `2` 标识 NO。市场数据会返回生成的代币 ID，因此大多数集成不需要自行派生。

## Polymarket Protocol V2

PositionManager 管理所有结果余额，并将每个 Position ID 路由到其注册模块。Position ID 中编码了模块 ID。

| 模块 ID | 模块 | 持仓结构 |
| - | - | - |
| `1` | BinaryModule | 一个 YES 持仓和一个 NO 持仓 |
| `2` | NegRiskModule | 事件中每个结果各有一个 YES 持仓和一个 NO 持仓 |
| `3` | CombinatorialModule | 一组腿对应的一个 YES 持仓和一个 NO 持仓 |

第一个字节标识模块，最后一个字节标识结果，其中 `0` 表示 YES，`1` 表示 NO。在应用代码中，请将完整 Position ID 视为不透明的十进制字符串。

Router 是拆分、合并、赎回和模块专用持仓操作的公开入口。拆分需要向 Router 授权 pUSD。合并或赎回需要向 Router 授权 PositionManager。

## 负风险与 Combos

负风险事件会关联多个结果，使一个 NO 持仓可以转换为互补的 YES 持仓。两种系统通过不同合约实现该行为。事件模型请参阅[负风险市场](https://docs.polymarket.com/cn/concepts/negative-risk.md)。

Combos 使用 PositionManager 和 CombinatorialModule。每条腿都是来自 BinaryModule 或 NegRiskModule 的 Polymarket Protocol V2 Position ID。生成的 Combo 仍是一对二元结构的 YES 和 NO 持仓，因此可以使用 Polymarket Protocol V2 Exchange。

Combo 持仓模型请参阅[组合持仓](https://docs.polymarket.com/cn/trading/positions/combinatorial.md)。

## 合约地址

当前 Polygon 地址请参阅[合约](https://docs.polymarket.com/cn/resources/contracts.md)。

## 后续步骤

> [card] [管理持仓](https://docs.polymarket.com/cn/trading/positions/manage.md)
>
> 拆分、合并、赎回或迁移持仓。

> [card] [Combos 运作方式](https://docs.polymarket.com/cn/trading/combos/overview.md)
>
> 完成 Combo RFQ 和持仓工作流。


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
