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
source_url: 'https://docs.polymarket.com/cn/resources/onchain-position-data'
updated_at: 2026-11-13
---

# 链上持仓数据

> 索引两种持仓系统的余额、交易和结算

Polymarket 的结果余额存在于两个 ERC-1155 合约之一。使用 Gamma 返回的市场
`version` 选择下方的正确章节。字段是否存在不能可靠区分系统，因为 CTF 市场也可以
作为腿出现在 PositionManager 工作流中。

| Gamma `version` | 持仓系统 | 结果 ID | ERC-1155 账本 | Exchange 域版本 |
| - | - | - | - | - |
| `"v2"` | Polymarket V2 | 结果 `positionId` | PositionManager | `"3"` |
| `"v1"` | CTF | 结果 `tokenId` | Conditional Tokens | `"2"` |

发现工作流请参阅[发现市场](https://docs.polymarket.com/cn/market-data/discover-markets.md)，Polygon 地址请参阅
[合约](https://docs.polymarket.com/cn/resources/contracts.md)。

## CTF 合约

### 派生 CTF 标识符

Conditional Tokens 根据 condition 和抵押品路径派生每个标识符。尽可能使用已部署
合约的 helper。

| 标识符 | 派生方式 |
| - | - |
| Condition ID | `keccak256(abi.encodePacked(oracle, questionId, outcomeSlotCount))` |
| Collection ID | `getCollectionId(parentCollectionId, conditionId, indexSet)` |
| Position ID | `getPositionId(collateralToken, collectionId)` |

CTF 持仓可以通过 parent collection 包含多个 condition。`indexSet` 选择其表示的结果。
对于二元 condition，两个单一结果 collection 使用 index set `1` 和 `2`。

Conditional Tokens 不定义全平台 Event ID。负风险分组由 Neg Risk Adapter 维护。
Gamma 提供应用集成使用的事件和市场标识符。

### 索引 CTF 余额和生命周期事件

根据 Conditional Tokens 发出的 `TransferSingle` 和 `TransferBatch` 构建余额。
根据 `ApprovalForAll` 构建 operator 授权。

| 事件结构 | 索引操作 |
| - | - |
| `from` 是零地址 | 增加持有人余额和索引供应量 |
| `to` 是零地址 | 减少持有人余额和索引供应量 |
| 两个地址都不是零地址 | 在持有人之间移动余额 |
| `ApprovalForAll` | 更新 owner 与 operator 的授权关系 |

Conditional Tokens 没有为每个结果代币提供通用总供应量读取。如果索引器需要完整历史
余额或供应量，请从部署区块或其他经过验证的检查点开始。

使用以下生命周期事件补充 ERC-1155 余额变化的交易上下文：

| 工作流 | 事件 |
| - | - |
| 准备 | `ConditionPreparation` 和 `MarketPrepared` |
| 拆分 | `PositionSplit` |
| 合并 | `PositionsMerge` |
| 转换 | `PositionsConverted` |
| 赎回 | `PayoutRedemption` |
| 结算 | `OutcomeReported` 和 `ConditionResolution` |

ERC-1155 转移事件仍是余额、铸造、销毁和供应量的标准输入。不要将生命周期事件及其底层
转移重复计为两次余额变化。

### 归因 CTF Exchange 成交

CTF exchanges 会发出 `OrderFilled`、`OrdersMatched` 和 `FeeCharged`。已签名订单的
字段名为 `tokenId`，其中包含市场发现阶段选择的 CTF 结果代币 ID。

`OrderFilled` 包含已签名的 `builder` 值和 `metadata`。请为每个订单记录 Exchange
地址或 EIP-712 域版本 `"2"`。当两个系统使用相同订单结构时，这样可以将成交归因到
正确的持仓系统。

### 跟踪 CTF 结算和赎回

Conditional Tokens 存储 `payoutNumerators` 和 `payoutDenominator`。一个结果的支付
比例等于其 numerator 除以 condition denominator。

AutoRedeemer 使用以下事件之一标识自动 CTF 赎回的余额来源：

| 事件 | 余额来源 |
| - | - |
| `BinaryRedemption` | 二元 Conditional Tokens 持仓 |
| `NegRiskRedemption` | 负风险 Conditional Tokens 持仓 |

账本也会发出常规赎回、销毁和转移事件。使用 AutoRedeemer 事件归因自动操作，使用账本
事件更新余额和供应量。

## Polymarket Protocol V2

### 解码 Polymarket Protocol V2 Position ID

Polymarket Protocol V2 Position ID 编码模块、事件、condition 和结果。清除低位字段后，同一个
值可以转换为 Condition ID 或 Event ID。

```text theme={null}
[moduleId | baseHash | arity | reserved | resolutionChain | conditionIndex | outcomeIndex]
  8 bits    128 bits  16 bits   64 bits       16 bits          16 bits          8 bits
```

| 字段 | 位 | 用途 |
| - | - | - |
| `moduleId` | 248 到 255 | 将持仓路由到对应模块 |
| `baseHash` | 120 到 247 | 标识来源事件或问题数据 |
| `arity` | 104 到 119 | 存储负风险事件的真实 condition 数量 |
| `reserved` | 40 到 103 | 预留的事件标识位 |
| `resolutionChain` | 24 到 39 | 标识允许结算该 condition 的链 |
| `conditionIndex` | 8 到 23 | 选择事件中的 condition |
| `outcomeIndex` | 0 到 7 | 选择 condition 结果 |

当前模块 ID：

| 模块 ID | 模块 |
| - | - |
| `1` | BinaryModule |
| `2` | NegRiskModule |
| `3` | CombinatorialModule |

Polymarket Protocol V2 原生标识符 helper 按以下顺序派生标识符：

| 标识符 | 派生方式 |
| - | - |
| Base hash | `keccak256(abi.encode(moduleId, data))`，在编码 ID 中截取低 128 位 |
| Event ID | 编码模块 ID、base hash、arity 和 resolution chain，并保持低 24 位为零 |
| Condition ID | 在 Event ID 上加入 `conditionIndex`，并保持 outcome 字节为零 |
| Position ID | 在 Condition ID 上加入 `outcomeIndex` |

迁移使用预先计算的旧版标识符，而不是原生 base-hash 派生方式。二元迁移直接将旧版 CTF
Condition ID 作为 base-hash 输入。负风险迁移直接将旧版 Event ID 作为 Event ID 的
base-hash 输入，再按索引派生 Condition ID。不要再次哈希这两种旧版标识符。将
`MigrationConditionRegistered` 视为权威的 CTF 到 Polymarket Protocol V2 Condition ID 映射，
将 `EventPrepared` 视为权威的旧版到 Polymarket Protocol V2 Event ID 映射。

Polymarket Protocol V2 使用 `bytes31` 表示 Condition ID，使用 `bytes29` 表示 Event ID。接受或返回
`bytes32` 的兼容边界使用相同的值，并在右侧补零字节。解码带类型的 ABI 值时保留原生
宽度，仅在目标 ABI 要求 `bytes32` 时补齐。

二元 condition 的 arity 为 `0`，condition index 为 `0`，因此其 Condition ID 与
Event ID 在位表示上相同。

解码 Position ID 时可使用以下掩码：

```text theme={null}
moduleId       = positionId >> 248
outcomeIndex   = positionId & 0xff
conditionId    = positionId with bits 0 to 7 cleared
eventId        = positionId with bits 0 to 23 cleared
conditionIndex = (positionId >> 8) & 0xffff
arity          = (positionId >> 104) & 0xffff
```

将 `outcomeIndex` 替换为 YES 的 `0` 或 NO 的 `1`，即可派生另一个二元结果。标准
Condition ID 的 outcome 字节为零，标准 Event ID 的 condition 和 outcome 字段都为零。

### 索引 PositionManager 余额和生命周期事件

根据 PositionManager 发出的 `TransferSingle` 和 `TransferBatch` 构建余额。根据
`ApprovalForAll` 构建 operator 授权。

| 事件结构 | 索引操作 |
| - | - |
| `from` 是零地址 | 增加持有人余额和索引供应量 |
| `to` 是零地址 | 减少持有人余额和索引供应量 |
| 两个地址都不是零地址 | 在持有人之间移动余额 |
| `ApprovalForAll` | 更新 owner 与 operator 的授权关系 |

PositionManager 没有为每个结果持仓提供通用总供应量读取。如果索引器需要完整历史余额或
供应量，请从部署区块或其他经过验证的检查点开始。

使用以下生命周期事件补充 ERC-1155 余额变化的交易上下文：

| 工作流 | 模块范围 | 事件 |
| - | - | - |
| 准备 | NegRiskModule 迁移 | `EventPrepared` |
| 准备 | CombinatorialModule | `CombinatorialConditionPrepared` |
| 拆分 | BinaryModule、NegRiskModule 或 Combo | `PositionsSplit`、`HorizontalSplit` 或组合拆分事件 |
| 合并 | BinaryModule、NegRiskModule 或 Combo | `PositionsMerged`、`HorizontalMerge` 或组合合并事件 |
| 转换 | NegRiskModule | `PositionConverted` |
| 赎回 | BinaryModule、NegRiskModule 或 Combo | `PositionRedeemed` |
| 结算 | BinaryModule 或 NegRiskModule | `ResultReported` 和 `ConditionResolved` |
| 桥接 | BinaryModule 或 NegRiskModule | `BridgePositionMinted` 和 `BridgePositionsBurned` |

原生 BinaryModule 和 NegRiskModule 标识符没有准备事件。除上述汇总的事件外，
CombinatorialModule 还有自己的操作专用转换事件，并且 Combo 持仓不可桥接。

Router 也会为路由后的拆分、合并、转换、赎回和抵押品返还发出事件。需要时可将其保存为
调用上下文。不要把其中的数量再次应用为 ERC-1155 余额更新。

CombinatorialModule 会为 Combo 内部变化发出操作专用事件，包括拆分、合并、转换、
提取、注入、压缩和包装。需要重建这些变化时，请索引已部署模块的 ABI。

ERC-1155 转移事件仍是余额、铸造、销毁和供应量的标准输入。不要将生命周期事件及其
底层转移重复计为两次余额变化。

### 归因 Polymarket Protocol V2 Exchange 成交

Polymarket Protocol V2 Exchange 会发出 `OrderFilled`、`OrdersMatched` 和
`FeeCharged`。已签名订单的字段名为 `tokenId`，其中包含市场发现阶段选择的 Position ID。

`OrderFilled` 包含已签名的 `builder` 值和 `metadata`。请为每个订单记录 Exchange
地址或 EIP-712 域版本 `"3"`。当两个系统使用相同订单结构时，这样可以将成交归因到
正确的持仓系统。

### 跟踪 Polymarket Protocol V2 结算和赎回

BinaryModule 和 NegRiskModule 以百万分比存储结果向量。结果分母为 `1,000,000`。
`OracleAggregator` 事件说明 reporter 共识和争议。BinaryModule 或 NegRiskModule 的
`ConditionResolved` 事件记录控制赎回的结果。

CombinatorialModule 存储每个 Combo condition 的 BinaryModule 和 NegRiskModule 腿，
而不是单独的结果向量。根据存储的腿及其底层模块结果确定 Combo 持仓的支付。
CombinatorialModule 不会发出 `ConditionResolved`。

对于原生 Polymarket Protocol V2 负风险事件，并非每个结果都需要单独存储值：

* `RemainingConditionsDerivableAsNo` 表示一个 YES 结果达到完整分母后，剩余真实
  condition 可以推导为 NO。
* `SyntheticConditionDerivableAsYes` 表示所有真实 condition 都结算为 NO 后，合成
  Other condition 可以推导为 YES。

显示所有结果的索引器必须应用这些推导规则，而不能等待每个推导结果各自发出
`ConditionResolved`。

不要为已注册的负风险迁移 condition 推导同级 NO 结果。即使其事件发出了
`RemainingConditionsDerivableAsNo`，`NegRiskModule.getResult` 也会从该推导中排除已注册
的迁移 condition。请等待每个已迁移真实 condition 存储其由 CTF 支持的结果，该结果由
`ConditionResolved` 和 `MigrationResolved` 记录。合成 Other condition 没有 CTF 映射，
在所有真实 condition 都结算为 NO 后仍可推导。

AutoRedeemer 会为自动 PositionManager 赎回发出 `Redemption`。账本也会发出常规赎回、
销毁和转移事件。使用 AutoRedeemer 事件归因自动操作，使用账本事件更新余额和供应量。

### 跟踪从 CTF 迁移

迁移会将已注册的 CTF 余额移动到对应的 PositionManager 余额。请索引 BinaryModule 和
NegRiskModule 中的以下事件：

| 事件 | 含义 |
| - | - |
| `MigrationConditionRegistered` | 将 PositionManager Condition ID 关联到其 CTF condition ID |
| 带 `legacyEventId` 的 `EventPrepared` | 将负风险 Event ID 关联到其 CTF 事件 |
| `PositionMigrated` | 记录持有人、新 Condition ID、Position ID、结果索引和数量 |
| `MigrationResolved` | 记录 CTF 支付和标准化模块结果 |
| `LegacyCollateralSettled` | 记录 CTF 赎回或互补 YES/NO 合并释放的抵押品 |

已迁移 condition 根据注册的 CTF 支付结算。Polymarket Protocol V2 resolver 不能替换该
结果。桥接报告会先从 CTF 派生结果，并且必须与之匹配。负风险事件中的合成 Other condition
没有 CTF 映射，由 NegRiskModule 派生。

迁移还会发出 CTF 转移和 PositionManager 铸造事件。使用 ERC-1155 事件更新余额，再使用
`PositionMigrated` 关联旧标识符和新标识符。


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
