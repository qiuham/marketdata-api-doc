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
source_url: 'https://docs.polymarket.com/cn/trading/overview'
updated_at: 2026-11-13
---

# 概览

> 了解 Polymarket 中订单、结算和持仓如何协同运作。

交易将 CLOB 上的已签名订单与 Polygon 上的结算连接起来。你需要选择一个结果，使用签名者授权订单，然后将其提交到订单簿。订单撮合后，结算过程会在交易账户之间转移 pUSD 和结果持仓。

## 交易流程

先完成一次账户设置，然后为每笔订单重复其余步骤。

**1. 设置账户**

将签名者连接到账户钱包，为钱包充值，并授予所需的交易授权。

**2. 选择结果**

选择要买入或卖出的结果，并查看当前的市场限制。

**3. 下单**

选择价格和数量，签署订单，然后将其提交到 CLOB。

**4. 管理订单**

监控成交情况，并取消剩余的未成交数量。已撮合的交易会在 Polygon
上结算，并更新你的余额和持仓。

> [!NOTE]
>
> Exchange
> 运营方可以撮合订单并执行订单排序，但不能设定价格，也不能执行未经用户授权的交易。

## 开始交易

> [card] [完成第一笔订单](https://docs.polymarket.com/cn/trading/quickstart.md)
>
> 完成首个需要身份验证的交易流程。

> [card] [钱包与身份验证](https://docs.polymarket.com/cn/trading/wallets-auth.md)
>
> 将签名者连接到持有资金和持仓的账户钱包。

> [card] [订单生命周期](https://docs.polymarket.com/cn/concepts/order-lifecycle.md)
>
> 了解订单从提交到成交、取消或到期的完整过程。


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
