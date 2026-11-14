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
source_url: 'https://docs.polymarket.com/cn/concepts/markets-events'
updated_at: 2026-11-13
---

# 市场与事件

> 了解 Polymarket 的基本构成要素

Polymarket 上的每个预测都围绕一个**事件**、一个或多个 **condition**，以及每个 condition 对应的**持仓**构建。理解这一层级关系是在平台上进行开发的基础。

![](https://mintcdn.com/polymarket-292d1b1b/FOMte3ewbG-LVy3k/images/core-concepts/event-market.png?fit=max\&auto=format\&n=FOMte3ewbG-LVy3k\&q=85\&s=4c62bd08a405868307cdd6799b368ca5)

## 市场

**市场**是 Polymarket 上最基本的可交易单元。每个市场代表一个包含 Yes 和 No 结果、可以结算的 condition。

![](https://mintcdn.com/polymarket-292d1b1b/FOMte3ewbG-LVy3k/images/core-concepts/event.png?fit=max\&auto=format\&n=FOMte3ewbG-LVy3k\&q=85\&s=0c9a264aec9a22ce5a20c4cc7980806d)

每个市场都有标识其 condition 和可交易结果持仓的值：

| 概念 | Polymarket V2 | CTF |
| - | - | - |
| **Condition 标识** | 协议专用的 condition ID | CTF condition ID |
| **结果标识符** | 每个结果对应一个 Polymarket V2 Position ID | 每个结果对应一个 CTF 代币 ID |

请将这些标识符视为不透明值。两种系统的格式和派生规则不同，不要用一种系统的规则派生另一种系统的标识符。

> [!NOTE]
>
> 只有当 `enableOrderBook` 为 `true` 时，市场才可以通过 CLOB
> 进行交易。部分市场可能存在于链上，但不支持订单簿交易。

### 市场示例

一个简单的市场可能是：

> **"比特币能否在 2026 年 12 月前达到 \$150,000？"**

这会产生两个结果：

* **Yes 持仓**：如果比特币达到 $150k，可兑换 `$1\`
* **No 持仓**：如果比特币未达到 $150k，可兑换 `$1\`

## 事件

**事件**是将一个或多个相关市场组合在一起的容器。事件提供组织结构，并支持多结果预测。

### 单市场事件

当事件只包含一个市场时，形成一个简单的市场对。事件和市场实质上是等价的。

```
Event: Will Bitcoin reach $100,000 by December 2024?
└── Market: Will Bitcoin reach $100,000 by December 2024? (Yes/No)
```

### 多市场事件

当事件包含两个或更多市场时，会在一个事件下组合相关的二元问题。部分多市场事件表示互斥的结果。

Polymarket 会将这些互斥市场关联为一个[负风险组](https://docs.polymarket.com/cn/concepts/negative-risk.md)。组内只会有一个市场判定为 Yes，其余市场都会判定为 No。

```
Event: Who will win the 2024 Presidential Election?
├── Market: Donald Trump? (Yes/No)
├── Market: Joe Biden? (Yes/No)
├── Market: Kamala Harris? (Yes/No)
└── Market: Other? (Yes/No)
```

## 市场标识

每个市场和事件都有一个唯一的 **slug**，出现在 Polymarket 的 URL 中：

```
https://polymarket.com/event/fed-decision-in-october
                              └── slug: fed-decision-in-october
```

你可以使用 slug 从 API 获取特定的市场或事件：

```bash theme={null}
# Fetch event by slug
curl "https://gamma-api.polymarket.com/events?slug=fed-decision-in-october"
```

## 体育市场

对于体育市场，未成交的限价单会在比赛开始时**自动取消**，在官方开赛时间清空订单簿。但比赛开始时间可能会变动——如果比赛提前开始，订单可能来不及清除。请在临近开赛时密切关注你的订单。

***

## 下一步

> [card] [价格与订单簿](https://docs.polymarket.com/cn/concepts/prices-orderbook.md)
>
> 了解价格如何形成以及订单簿的运作方式。

> [card] [获取市场数据](https://docs.polymarket.com/cn/market-data/overview.md)
>
> 开始通过 API 查询市场和事件。


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
