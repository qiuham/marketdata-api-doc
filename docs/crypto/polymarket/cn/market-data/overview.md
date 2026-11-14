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
source_url: 'https://docs.polymarket.com/cn/market-data/overview'
updated_at: 2026-11-13
---

# 概览

> 了解 Polymarket 如何组织市场数据，以及应从何处开始。

使用市场数据的第一步，是确定应用关注的事件、市场或结果。本节将从这一选择出发，引导你获取应用所需的数据。

## 了解数据模型

在 Polymarket 中，一个事件包含一个或多个市场。每个市场都是一个可交易的问题，包含 YES 和 NO 两种结果，每种结果都有自己的资产 ID。读取某个结果的价格或订单簿时，请使用该结果的资产 ID。

![](https://mintcdn.com/polymarket-292d1b1b/FOMte3ewbG-LVy3k/images/core-concepts/event.png?fit=max\&auto=format\&n=FOMte3ewbG-LVy3k\&q=85\&s=0c9a264aec9a22ce5a20c4cc7980806d)

**1. 发现事件**

浏览活跃事件、按主题搜索，或通过 Polymarket URL 直接获取事件。

**2. 选择市场**

查看事件中的市场，并选择应用关注的具体问题。

**3. 选择结果**

选择 YES 或 NO 并保存其资产 ID。你将使用它读取价格、访问订单簿和下单。

**4. 读取或流式接收数据**

使用已收集的标识符，获取或流式接收应用所需的市场数据。

## 选择工作流

如果你刚开始使用 Polymarket 市场数据，请先阅读[发现市场](https://docs.polymarket.com/cn/market-data/discover-markets.md)。

> [card] [发现市场](https://docs.polymarket.com/cn/market-data/discover-markets.md)
>
> 查找应用关注的事件和市场。

> [card] [市场详情](https://docs.polymarket.com/cn/market-data/market-details.md)
>
> 了解市场的结果、状态、交易约束、费用及其他属性。

> [card] [价格和订单簿](https://docs.polymarket.com/cn/market-data/prices-order-books.md)
>
> 了解当前价格和流动性，或查看价格如何变化。

> [card] [分析](https://docs.polymarket.com/cn/market-data/public-analytics.md)
>
> 分析市场活动，并比较交易者和 Builder 的表现。

> [card] [实时数据](https://docs.polymarket.com/cn/market-data/realtime-data.md)
>
> 随市场及相关数据的变化，让应用保持最新状态。

> [card] [Chainlink TWAP 价格](https://docs.polymarket.com/cn/market-data/realtime-data.md#twap-价格)
>
> 流式接收 Chainlink 计算的 60 秒时间加权加密货币价格。


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
