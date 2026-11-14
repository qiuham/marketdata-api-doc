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
source_url: 'https://docs.polymarket.com/cn/concepts/pusd'
updated_at: 2026-11-13
---

# Polymarket USD

> pUSD — Polymarket 上用于所有交易的抵押代币

**pUSD**（Polymarket USD）是 Polymarket 上用于所有交易的抵押代币。它是 Polygon 上的标准 ERC-20 代币，由 USDC 背书。背书由支持提现功能的智能合约在链上强制执行。无算法锚定，无部分准备金。

> [!NOTE]
>
> **日常使用没有变化。** 你充值、查看余额、交易、提现。pUSD
> 是你熟悉的同一体验下的技术结算层。

***

## 为什么是 pUSD

Polymarket 使用 pUSD 结算交易，为不同市场系统提供一致的抵押资产。

pUSD 是一个代表 USDC 债权的标准 ERC-20 包装代币。包装与解包通过 `CollateralOnramp` 和 `CollateralOfframp` 合约在链上强制执行。

***

## 基本信息

| | |
| - | - |
| 代币标准 | ERC-20 |
| 网络 | Polygon 主网 |
| 小数位 | 6 |
| 背书 | USDC（链上强制执行） |
| 可转账 | 可以 — 标准 ERC-20 |

pUSD 的设计目的是在 Polymarket 内部使用。目前没有在外部交易所上架的计划。

所有抵押品相关的合约地址详见[合约](https://docs.polymarket.com/cn/resources/contracts.md)页面。

***

## 持仓背书

CTF 合约与 Polymarket Protocol V2 使用不同的持仓背书记账方式。

| 系统 | 持仓背书 |
| - | - |
| **Polymarket V2** | 创建 PositionManager 持仓时，市场模块销毁 pUSD。合并或赎回这些持仓时，市场模块铸造 pUSD |
| **CTF** | 抵押品适配器先将 pUSD 解包为 USDC.e，再创建 CTF 持仓。合并或赎回持仓时，释放的 USDC.e 会重新包装为 pUSD |

两种系统中的未平仓持仓都代表未计入 pUSD 总供应量的价值。进行系统级记账时，应将 pUSD 总供应量与未偿持仓权益合并计算。CTF 权益应与对应持仓的底层抵押品对账，Polymarket Protocol V2 权益应与 PositionManager 余额和模块支付记账对账。

***

## 包装 — USDC.e → pUSD

使用 **CollateralOnramp** 将 USDC.e 包装为 pUSD。

```solidity theme={null}
function wrap(address _asset, address _to, uint256 _amount) external
```

**参数**

* `_asset` — 要包装的资产地址。必须是 USDC.e。
* `_to` — 铸造的 pUSD 的接收者。不必是 `msg.sender`。
* `_amount` — 包装数量，使用 USDC.e 的最小单位（6 小数位）。

**要求**

* 调用方必须先授权 **CollateralOnramp** 合约（而不是 pUSD 代币）转移 USDC.e。
* 如果管理员暂停了 USDC.e，调用会以 `OnlyUnpaused()` 回滚。

### 示例

```typescript TypeScript theme={null}
import {
  createWalletClient,
  createPublicClient,
  http,
  parseAbi,
  parseUnits,
} from "viem";
import { polygon } from "viem/chains";
import { privateKeyToAccount } from "viem/accounts";

const account = privateKeyToAccount(process.env.PRIVATE_KEY as `0x${string}`);
const walletClient = createWalletClient({
  account,
  chain: polygon,
  transport: http(),
});
const publicClient = createPublicClient({ chain: polygon, transport: http() });

const ONRAMP = "0x93070a847efEf7F70739046A929D47a521F5B8ee" as const;
const USDCE = "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174" as const; // USDC.e on Polygon

const amount = parseUnits("100", 6); // 100 USDC.e

// 1. Approve the Onramp to spend your USDC.e
const approveHash = await walletClient.writeContract({
  address: USDCE,
  abi: parseAbi([
    "function approve(address spender, uint256 amount) returns (bool)",
  ]),
  functionName: "approve",
  args: [ONRAMP, amount],
});
await publicClient.waitForTransactionReceipt({ hash: approveHash });

// 2. Wrap USDC.e → pUSD
const wrapHash = await walletClient.writeContract({
  address: ONRAMP,
  abi: parseAbi([
    "function wrap(address _asset, address _to, uint256 _amount)",
  ]),
  functionName: "wrap",
  args: [USDCE, account.address, amount],
});
await publicClient.waitForTransactionReceipt({ hash: wrapHash });
```

```python Python theme={null}
from web3 import Web3

ONRAMP = "0x93070a847efEf7F70739046A929D47a521F5B8ee"
USDCE = "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174"

amount = 100 * 10**6  # 100 USDC.e

# 1. Approve the Onramp to spend your USDC.e
usdce = w3.eth.contract(address=USDCE, abi=[{
    "name": "approve", "type": "function",
    "inputs": [{"name": "spender", "type": "address"},
               {"name": "amount", "type": "uint256"}],
    "outputs": [{"type": "bool"}],
}])
usdce.functions.approve(ONRAMP, amount).transact({"from": address})

# 2. Wrap USDC.e → pUSD
onramp = w3.eth.contract(address=ONRAMP, abi=[{
    "name": "wrap", "type": "function",
    "inputs": [{"name": "_asset", "type": "address"},
               {"name": "_to", "type": "address"},
               {"name": "_amount", "type": "uint256"}],
    "outputs": [],
}])
onramp.functions.wrap(USDCE, address, amount).transact({"from": address})
```

***

## 解包 — pUSD → USDC.e

使用 **CollateralOfframp** 将 pUSD 解包回 USDC.e。

```solidity theme={null}
function unwrap(address _asset, address _to, uint256 _amount) external
```

**参数**

* `_asset` — 你希望接收的资产。必须是 USDC.e。
* `_to` — 底层资产的接收者。
* `_amount` — 要解包的 pUSD 数量（6 小数位）。

**要求**

* 调用方必须先授权 **CollateralOfframp** 合约转移其 pUSD。
* 与 Onramp 使用相同的暂停机制。

***

## 下一步

> [card] [合约](https://docs.polymarket.com/cn/resources/contracts.md)
>
> 所有 Polymarket 合约地址和审计

> [card] [Bridge](https://docs.polymarket.com/cn/trading/bridge/deposit.md)
>
> 从其他链充值 — 自动包装为 pUSD


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
