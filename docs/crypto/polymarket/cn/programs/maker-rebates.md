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
source_url: 'https://docs.polymarket.com/cn/programs/maker-rebates'
updated_at: 2026-11-23
---

# Maker 返利计划

> 通过在 Polymarket 提供流动性赚取每日 pUSD 返利

Polymarket 在多个市场类别收取 taker 费用。费用由协议在撮合时确定,并用于资助 **Maker 返利**计划,向流动性提供者支付每日 pUSD 返利。

***

## 为什么要有 Maker 返利

更深的流动性意味着更紧的价差、更低的价格影响、更可靠的成交以及在波动期间更强的韧性。Maker 返利激励**持续的、有竞争力的报价**，让每个人都能获得更好的交易体验。

***

## Maker 返利如何运作

* **每日以 pUSD 支付:** 返利每天计算和分配。
* **基于表现:** Maker 等级决定你从符合条件成交产生的 Taker 费用中获得的返利比例。

### 资格

下达为订单簿增加流动性并被成交的订单(即,你的流动性被其他交易者成交)。标准返利要求过去 30 天的 Maker 加权成交量至少达到 \$200,000。

> [!NOTE]
>
> Combo 和免费交易（包括费用假期内的交易）不赚取 Maker 加权成交量或返利。

### 支付

返利每日以 pUSD 支付,直接到你的钱包。

***

## 资金来源

Maker 返利由符合条件的市场中收取的 taker 费用资助。这些费用的一定百分比重新分配给保持市场流动性的 maker。返利百分比取决于过去 30 天的 Maker 加权成交量。

| 等级 | 30 天 Maker 加权成交量 | 成交产生的 Taker 费用的返利比例 |
| - | - | - |
| 无 | 低于 \$200,000 | 0% |
| Tier 1 | \$200,000 至低于 \$1,000,000 | 3% |
| Tier 2 | \$1,000,000 至低于 \$4,000,000 | 7% |
| Tier 3 | \$4,000,000 至低于 \$10,000,000 | 10% |
| Tier 4 | \$10,000,000 及以上 | 15% |

以上为标准等级比例。适用的 Maker 返利活动可替代标准比例。

你可以查询最多 100 个 Maker 地址的等级、返利比例及 30 天加权成交量，无需身份验证。请参阅[获取地址的 Maker 等级](https://docs.polymarket.com/cn/api-reference/rebates/get-maker-tiers-for-addresses.md)。

> [!NOTE]
>
> Polymarket 在所有启用费用的市场类别中收取 taker 费用。返利百分比由 Polymarket
> 全权决定,可能会随时间变化。

***

## Maker 等级返利

Maker 等级取决于过去 30 天符合条件的 Maker 加权成交量：

```text theme={null}
wV = C × p × (1 - p)
```

其中 **C** 为已成交份额数量，**p** 为以美元表示的成交价格。
各符合条件市场的成交量合并计算，包括 BTC 5 分钟和 15 分钟市场，等级每日更新。
仅计入已成交部分，不使用类别乘数。Maker 成交和 Taker 成交分别计入各自的等级。

对于每个成交的 maker 订单:

```text theme={null}
fee_equivalent = C × feeRate × p × (1 - p)
```

其中 **C** = 交易的份额数量,**p** = 份额价格。费用参数因市场类型而异:

| 类别 | Taker Fee Rate | Maker Fee Rate |
| - | - | - |
| 加密货币 — BTC 5 分钟和 15 分钟涨跌市场 | 0.05 | 0 |
| 加密货币 — 其他所有市场 | 0.01 | 0 |
| 体育，包括 NFL 和大学橄榄球 | 0.05 | 0 |
| 金融 | 0.05 | 0 |
| 科技 | 0.05 | 0 |
| 政治 — 选举 | 0.05 | 0 |
| 政治 — 不含选举和地缘政治 | 0.01 | 0 |
| 经济 | 0.01 | 0 |
| 文化 | 0.01 | 0 |
| 天气 | 0.01 | 0 |
| Mentions | 0.01 | 0 |
| 地缘政治 | 0 | 0 |
| Combo | 0.05 | 0 |
| 其他 / 通用 | 0.05 | 0 |

每笔符合条件成交的返利:

```text theme={null}
rebate = fee_equivalent × maker_tier_rebate_rate
```

每笔符合条件的成交以扣除任何 Taker 等级返利前的 Taker 费用为基数。Maker 返利取决于你的 Maker 等级，不受你自己或交易对手的 Taker 等级影响。例如，Tier 4 Maker 的符合条件成交产生 \$100 Taker 费用时，可赚取 \$15 返利。

***

## Taker 费用结构

Taker 费用以 pUSD 计算,并根据份额价格变化。费用金额（以 pUSD 计）关于 50% 概率对称 — 30¢ 的交易与 70¢ 的交易产生相同的美元费用。

### 费用表 - 100 份额

有关每个市场类别的详细费用表,请参阅[费用](https://docs.polymarket.com/cn/trading/fees.md)页面。

### 费用精度

费用四舍五入到小数点后 5 位。收取的最小费用为 0.00001 pUSD。任何更小的费用都会四舍五入为零,因此接近极端的非常小的交易可能根本不产生费用。

***

## 哪些市场符合条件

以下市场类别已启用 taker 费用,符合 maker 返利条件:加密货币、体育、金融、政治、经济、文化、天气、科技、Mentions 和其他 / 通用。仅产生 Taker 费用的成交符合条件，且不包括 Combo。Maker 返利与[流动性奖励](https://docs.polymarket.com/cn/programs/liquidity-rewards.md)是独立计划；市场无需分配流动性奖励，其符合条件的成交也可以计入。

要确认某个市场是否收取费用，请参阅“市场详情”中的[交易费用](https://docs.polymarket.com/cn/market-data/market-details.md#交易费用)。

***

## 常见问题

> [accordion] 如何获得 maker 返利资格
>
> 下达为订单簿增加流动性并被成交的订单(即,你的流动性被其他交易者成交)。标准返利要求过去 30 天的 Maker 加权成交量至少达到 \$200,000。

> [accordion] 返利何时支付
>
> 每日,以 pUSD 支付。

> [accordion] 返利如何计算
>
> 返利按你的 Maker 等级比例计算，基数是符合条件成交产生且扣除 Taker 等级返利前的
> Taker 费用。你自己和交易对手的 Taker 等级均不影响 Maker 返利。

> [accordion] Maker 返利从哪里来
>
> Maker 返利由符合条件市场收取的 Taker
> 费用支持，按你自己的符合条件成交计算，并每日分配。

> [accordion] 哪些市场启用了费用
>
> 加密货币、体育、金融、政治、经济、文化、天气、科技、Mentions、其他 / 通用和
> Combo 市场。Combo 收取费用，但不赚取 Maker 返利。


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
