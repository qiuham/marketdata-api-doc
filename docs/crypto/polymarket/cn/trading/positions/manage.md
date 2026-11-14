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
source_url: 'https://docs.polymarket.com/cn/trading/positions/manage'
updated_at: 2026-11-13
---

# 管理持仓

> 拆分抵押品、合并完整持仓，以及赎回已结算持仓。

在订单簿之外管理持仓。你可以将 pUSD 拆分为完整持仓，将完整持仓合并回 pUSD，或在结算后赎回持仓。

| 操作 | 结果 |
| - | - |
| 拆分 | pUSD 变为数量相等的 YES 和 NO 余额 |
| 合并 | 数量相等的 YES 和 NO 余额变为 pUSD |
| 赎回 | 已结算持仓按支付比例返还 pUSD |

## 持仓路径

持仓系统决定代币账本、调用目标和授权。SDK 工作流会根据市场 condition 选择路径。直接调用者必须根据市场响应选择路径。

| 持仓系统 | ERC-1155 账本 | 持仓调用目标 | 所需授权 |
| - | - | - | - |
| Polymarket V2 | PositionManager | Router | 拆分时授权 pUSD，合并和赎回时授权 PositionManager |
| CTF | Conditional Tokens | 标准或负风险抵押品适配器 | 拆分时授权 pUSD，合并和赎回时授权 Conditional Tokens |

SDK 示例所需的授权设置请参阅[钱包与身份验证](https://docs.polymarket.com/cn/trading/wallets-auth.md#设置交易授权)。

> [tab] TypeScript
>
> 示例使用已经配置的 `SecureClient`。客户端设置请参阅[连接账户](https://docs.polymarket.com/cn/trading/wallets-auth.md#连接你的账户)。

> [tab] Python
>
> 示例使用已经配置的 `AsyncSecureClient`。同步 `SecureClient`
> 提供相同的持仓方法。客户端设置请参阅[连接账户](https://docs.polymarket.com/cn/trading/wallets-auth.md#连接你的账户)。

> [tab] API
>
> 示例构建可以直接提交或放入 Deposit Wallet 调用批次的合约调用。完整签名和提交工作流请参阅[执行免 Gas 交易](https://docs.polymarket.com/cn/trading/wallets-auth.md#执行免-gas-交易)。

## 拆分持仓

拆分 1 pUSD 会创建 1 个 YES 持仓和 1 个 NO 持仓。数量使用六位小数，因此 `1_000_000` 表示 1 pUSD 和每个结果的 1 份持仓。

> [tab] TypeScript
>
> 使用市场 condition ID 调用 `splitPosition()`。客户端会选择正确路径。
>
> ```ts theme={null}
> const transaction = await client.splitPosition({
>   conditionId: "<condition_id>",
>   amount: 1_000_000n,
> });
>
> const outcome = await transaction.wait();
>
> // outcome.transactionHash: TxHash
> // outcome.transactionId: TransactionId | null
> ```

> [tab] Python
>
> 使用市场 condition ID 调用 `split_position()`。客户端会选择正确路径。
>
> ```python theme={null}
> transaction = await client.split_position(
>     condition_id="<condition_id>",
>     amount=1_000_000,
> )
>
> outcome = await transaction.wait()
>
> # outcome.transaction_hash: TransactionHash
> # outcome.transaction_id: str | None
> ```

> [tab] API
>
> 使用 Gamma 市场响应中的 `version` 和 `negRisk` 选择目标，并授权该目标使用要拆分的 pUSD 数量。
>
> | `version` | `negRisk` | 目标 | 地址 |
> | - | - | - | - |
> | `"v1"` | `false` | `CtfCollateralAdapter` | `0xAdA100Db00Ca00073811820692005400218FcE1f` |
> | `"v1"` | `true` | `NegRiskCtfCollateralAdapter` | `0xadA2005600Dec949baf300f4C6120000bDB6eAab` |
> | `"v2"` | 忽略 | Router | `0x12121212006e4CD160D18e3f00711DA5c3372600` |
>
> ```solidity theme={null}
> function approve(address spender, uint256 amount) returns (bool);
> ```
>
> 为选定路径编码对应函数。
>
> ```solidity Polymarket V2 theme={null}
> function split(bytes31 conditionId, uint256 amount);
> ```
>
> ```solidity CTF theme={null}
> function splitPosition(
>     address collateralToken,
>     bytes32 parentCollectionId,
>     bytes32 conditionId,
>     uint256[] partition,
>     uint256 amount
> );
> ```
>
> Gnosis CTF 路径使用 pUSD 地址 `0xC011a7E12a19f7B1f670d46F03B03f3342E82DFB`、零值 `parentCollectionId` 和 partition `[1, 2]`。Polymarket Protocol V2 使用 Gamma 返回的 31 字节 condition ID。
>
> ```json theme={null}
> {
>   "target": "<selected_target_address>",
>   "value": "0",
>   "data": "<encoded_split_calldata>"
> }
> ```

## 合并持仓

合并数量相等的 YES 和 NO 余额，会返还相同数量的 pUSD。直接调用者不能合并超过较小一边余额的数量。

> [tab] TypeScript
>
> 调用 `mergePositions()`。传入 `"max"` 可合并账户中最大的完整持仓。
>
> ```ts theme={null}
> const transaction = await client.mergePositions({
>   conditionId: "<condition_id>",
>   amount: "max",
> });
>
> const outcome = await transaction.wait();
> ```

> [tab] Python
>
> 调用 `merge_positions()`。传入 `"max"` 可合并账户中最大的完整持仓。
>
> ```python theme={null}
> transaction = await client.merge_positions(
>     condition_id="<condition_id>",
>     amount="max",
> )
>
> outcome = await transaction.wait()
> ```
>
> `merge_multiple_positions()` 会在一个钱包交易中提交多个市场合并。每个市场独立选择路径。不要在同一批次中混合市场和 Combo 请求。
>
> ```python theme={null}
> transaction = await client.merge_multiple_positions(
>     positions=[
>         {"condition_id": "<first_condition_id>", "amount": 1_000_000},
>         {"condition_id": "<second_condition_id>", "amount": "max"},
>     ],
> )
>
> outcome = await transaction.wait()
> ```

> [tab] API
>
> 使用 Gamma 市场响应中的 `version` 和 `negRisk` 选择目标。
>
> | `version` | `negRisk` | 目标 | 地址 |
> | - | - | - | - |
> | `"v1"` | `false` | `CtfCollateralAdapter` | `0xAdA100Db00Ca00073811820692005400218FcE1f` |
> | `"v1"` | `true` | `NegRiskCtfCollateralAdapter` | `0xadA2005600Dec949baf300f4C6120000bDB6eAab` |
> | `"v2"` | 忽略 | Router | `0x12121212006e4CD160D18e3f00711DA5c3372600` |
>
> 对于 CTF，在 Conditional Tokens 上通过 `setApprovalForAll()` 授权选定适配器。对于 Polymarket Protocol V2，在 PositionManager 上通过 `setApprovalForAll()` 授权 Router。
>
> | 合约 | 地址 |
> | - | - |
> | Conditional Tokens | `0x4D97DCd97eC945f40cF65F87097ACe5EA0476045` |
> | PositionManager | `0x006F54F7f9A22e0000CC2AB60031000000ae9fEF` |
>
> ```solidity theme={null}
> function setApprovalForAll(address operator, bool approved);
> ```
>
> ```solidity Polymarket V2 theme={null}
> function merge(bytes31 conditionId, uint256 amount);
> ```
>
> ```solidity CTF theme={null}
> function mergePositions(
>     address collateralToken,
>     bytes32 parentCollectionId,
>     bytes32 conditionId,
>     uint256[] partition,
>     uint256 amount
> );
> ```
>
> Gnosis CTF 路径使用零值 `parentCollectionId` 和 partition `[1, 2]`。对于两条路径，`amount` 都表示每个待合并结果持仓的基础单位数量。
>
> ```json theme={null}
> {
>   "target": "<selected_target_address>",
>   "value": "0",
>   "data": "<encoded_merge_calldata>"
> }
> ```

## 赎回已结算持仓

赎回会销毁已结算持仓，并按支付比例返还 pUSD。赎回没有截止日期。

> [tab] TypeScript
>
> 使用 condition ID 或市场 ID 调用 `redeemPositions()`。对于 Gnosis CTF 持仓，客户端会赎回两个结果余额。对于 Polymarket Protocol V2 持仓，客户端会为每个非零结果余额提交一次 Router 调用。
>
> ```ts theme={null}
> const transaction = await client.redeemPositions({
>   conditionId: "<condition_id>",
> });
>
> const outcome = await transaction.wait();
> ```

> [tab] Python
>
> 使用 condition ID 或市场 ID 调用 `redeem_positions()`。客户端会赎回该市场的所有非零余额。
>
> ```python theme={null}
> transaction = await client.redeem_positions(
>     condition_id="<condition_id>",
> )
>
> outcome = await transaction.wait()
> ```

> [tab] API
>
> 使用 Gamma 市场响应中的 `version` 和 `negRisk` 选择目标。
>
> | `version` | `negRisk` | 目标 | 地址 |
> | - | - | - | - |
> | `"v1"` | `false` | `CtfCollateralAdapter` | `0xAdA100Db00Ca00073811820692005400218FcE1f` |
> | `"v1"` | `true` | `NegRiskCtfCollateralAdapter` | `0xadA2005600Dec949baf300f4C6120000bDB6eAab` |
> | `"v2"` | 忽略 | Router | `0x12121212006e4CD160D18e3f00711DA5c3372600` |
>
> Gnosis CTF 路径使用选定的抵押品适配器并赎回两个 index set。Polymarket Protocol V2 路径使用 Router，并要求为每个要赎回的结果余额分别调用。赎回前，请授权合并工作流中说明的同一 ERC-1155 operator。
>
> ```solidity Polymarket V2 theme={null}
> function redeem(bytes31 conditionId, uint256 outcomeIndex, uint256 amount);
> ```
>
> ```solidity CTF theme={null}
> function redeemPositions(
>     address collateralToken,
>     bytes32 parentCollectionId,
>     bytes32 conditionId,
>     uint256[] indexSets
> );
> ```
>
> Gnosis CTF 调用使用零值 `parentCollectionId` 和 index set `[1, 2]`。Polymarket Protocol V2 使用结果索引 `0` 表示 YES，`1` 表示 NO。`amount` 必须明确指定，且不能超过对应的 PositionManager 余额。
>
> ```json theme={null}
> {
>   "target": "<selected_target_address>",
>   "value": "0",
>   "data": "<encoded_redeem_calldata>"
> }
> ```

## 自动赎回

AutoRedeemer 可以代表已授权账户赎回已结算持仓。operator 提交赎回，用户只需授予 ERC-1155 授权。

| 持仓系统 | 授权代币 | Operator |
| - | - | - |
| Polymarket V2 | PositionManager | AutoRedeemer |
| CTF | Conditional Tokens | AutoRedeemer |

AutoRedeemer 支持标准 CTF 持仓、负风险 CTF 持仓，以及来自所有已注册模块的 PositionManager 持仓。标准交易授权设置包含这两项授权。

| 合约 | 地址 |
| - | - |
| AutoRedeemer | `0xa1200000d0002264C9a1698e001292D00E1b00af` |
| Conditional Tokens | `0x4D97DCd97eC945f40cF65F87097ACe5EA0476045` |
| PositionManager | `0x006F54F7f9A22e0000CC2AB60031000000ae9fEF` |

## 迁移已注册 CTF 持仓

迁移是可选操作。它会将符合条件的 Gnosis CTF 持仓移动到等价的 PositionManager 持仓。正常交易、拆分、合并或赎回不需要迁移。

> [!WARNING]
>
> 只能迁移 Polymarket 已注册的 condition 或事件。未注册的迁移调用会回滚。

该路径使用直接合约调用。先在 Conditional Tokens 上通过 `setApprovalForAll()` 授权目标模块，再使用已排序的旧 condition ID 调用该模块。

| 旧持仓类型 | 目标模块 | 地址 |
| - | - | - |
| Binary CTF | BinaryModule | `0x1000008dD9001B968442c1000017eaE6E0dA00Ba` |
| 负风险 CTF | NegRiskModule | `0x200000900045e3B6259600682756002200028933` |

```solidity theme={null}
function migratePositions(
    bytes32[] legacyConditionIds,
    uint256[] outcomeIndices,
    uint256[] amounts
);
```

三个数组的长度必须相同。每个结果索引使用 `0` 表示 YES，`1` 表示 NO。按旧 condition ID 升序排列条目。模块会转移已授权的 CTF 余额，并在 PositionManager 中铸造相同数量。

## 后续步骤

> [card] [持仓运作方式](https://docs.polymarket.com/cn/trading/positions/how-positions-work.md)
>
> 比较两种持仓账本和标识符。

> [card] [组合持仓](https://docs.polymarket.com/cn/trading/positions/combinatorial.md)
>
> 了解 Combo 持仓如何使用 CombinatorialModule。


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
