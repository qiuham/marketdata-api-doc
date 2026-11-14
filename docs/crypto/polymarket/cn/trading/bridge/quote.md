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
source_url: 'https://docs.polymarket.com/cn/trading/bridge/quote'
updated_at: 2026-11-13
---

# 报价

> 预览存款和提款的费用及预计输出

在执行存款或提款前获取预估报价。报价包括预计输出金额、完成时间和详细的
费用明细。

## 获取报价

```bash theme={null}
curl -X POST https://bridge.polymarket.com/quote \
  -H "Content-Type: application/json" \
  -d '{
    "fromAmountBaseUnit": "10000000",
    "fromChainId": "137",
    "fromTokenAddress": "0x3c499c542cEF5E3811e1192ce70d8cC03d5c3359",
    "recipientAddress": "0x17eC161f126e82A8ba337f4022d574DBEaFef575",
    "toChainId": "137",
    "toTokenAddress": "0xC011a7E12a19f7B1f670d46F03B03f3342E82DFB"
  }'
```

### 请求参数

| 参数 | 类型 | 描述 |
| - | - | - |
| `fromAmountBaseUnit` | string | 以最小单位表示的发送金额（例如，10 USDC 为 `"10000000"`） |
| `fromChainId` | string | 源链 ID（例如，Polygon 为 `"137"`） |
| `fromTokenAddress` | string | 代币在源链上的合约地址 |
| `recipientAddress` | string | 接收资金的目标钱包地址 |
| `toChainId` | string | 目标链 ID |
| `toTokenAddress` | string | 代币在目标链上的合约地址 |

### 响应

报价响应包括预计输出金额、费用明细，以及一个可记录在自有系统中的 `quoteId`。
转账开始后，如需跟踪转账本身，请使用跨链桥地址轮询
[`/status`](https://docs.polymarket.com/cn/trading/bridge/status)。

```json theme={null}
{
  "estCheckoutTimeMs": 45000,
  "estInputUsd": 10,
  "estOutputUsd": 9.94,
  "estToTokenBaseUnit": "9940000",
  "quoteId": "0x00c34ba467184b0146406d62b0e60aaa24ed52460bd456222b6155a0d9de0ad5",
  "estFeeBreakdown": {
    "gasUsd": 0.02,
    "appFeeLabel": "Bridge fee",
    "appFeePercent": 0.3,
    "appFeeUsd": 0.03,
    "fillCostPercent": 0.1,
    "fillCostUsd": 0.01,
    "maxSlippage": 0.5,
    "minReceived": 9.89,
    "swapImpact": 0.05,
    "swapImpactUsd": 0.005,
    "totalImpact": 0.6,
    "totalImpactUsd": 0.06
  }
}
```

| 字段 | 类型 | 描述 |
| - | - | - |
| `estCheckoutTimeMs` | number | 预计完成时间（毫秒） |
| `estInputUsd` | number | 预计输入美元价值 |
| `estOutputUsd` | number | 预计输出美元价值 |
| `estToTokenBaseUnit` | string | 以最小单位表示的预计输出金额 |
| `quoteId` | string | 此报价的唯一标识符 |
| `estFeeBreakdown` | object | 详细费用明细（见下文） |

### 费用明细

`estFeeBreakdown` 对象包含：

**gasUsd** `number`

以美元计价的 Gas 费

**appFeeLabel** `string`

应用费用标签

**appFeePercent** `number`

应用费用占总金额的百分比

**appFeeUsd** `number`

以美元计价的应用费用

**fillCostPercent** `number`

成交成本占总金额的百分比

**fillCostUsd** `number`

以美元计价的成交成本

**maxSlippage** `number`

最大潜在滑点百分比

**minReceived** `number`

计入滑点后的最低接收金额

**swapImpact** `number`

兑换影响占总金额的百分比

**swapImpactUsd** `number`

以美元计价的兑换影响

**totalImpact** `number`

总影响占总金额的百分比

**totalImpactUsd** `number`

以美元计价的总影响成本

> [!NOTE]
>
> 报价为估算值。实际金额可能因市场状况而略有不同。

## 后续步骤

> [card] [创建存款](https://docs.polymarket.com/cn/trading/bridge/deposit.md)
>
> 向 Polymarket 执行存款。

> [card] [提款](https://docs.polymarket.com/cn/trading/bridge/withdraw.md)
>
> 从 Polymarket 提款到另一条链。


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
