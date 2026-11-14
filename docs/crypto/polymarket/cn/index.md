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
source_url: 'https://docs.polymarket.com/cn/index'
updated_at: 2026-11-13
---

# 概览

> 基于全球最大的预测市场进行构建。通过 Polymarket API 进行交易、集成并访问实时市场数据。

🇺🇸

正在查找&#x20;

Polymarket US

&#x20;

文档？

访问美国站文档 →

[Open](https://docs.polymarket.us)

# Polymarket 开发文档

基于全球最大的预测市场进行构建。为预测市场开发者提供 API、SDK 和工具。

## 开发者快速入门

几分钟内发出第一个 API 请求。了解 Polymarket 平台的基础知识、获取市场数据、下单并赎回获胜持仓。

[下第一笔订单 →](https://docs.polymarket.com/cn/trading/quickstart.md)

```typescript TypeScript theme={null}
import { createPublicClient } from "@polymarket/client";

const client = createPublicClient();

const pages = client.listMarkets({ closed: false });
const { items: markets } = await pages.firstPage();
```

```python Python theme={null}
from polymarket import AsyncPublicClient

async with AsyncPublicClient() as client:
    markets = client.list_markets(closed=False)

    async for market in markets.iter_items():
        print(market.question)
```

```bash API theme={null}
curl -G "https://gamma-api.polymarket.com/markets/keyset" \
  --data-urlencode "closed=false" \
  --data-urlencode "limit=5"
```

## 熟悉 Polymarket

了解 Polymarket 的运作方式，探索市场和交易背后的概念，或选择集成方式。

> [card] [Polymarket 101](https://docs.polymarket.com/cn/polymarket-101.md)
>
> 了解预测市场如何运作以及如何使用 Polymarket。

> [card] [核心概念](https://docs.polymarket.com/cn/concepts/markets-events.md)
>
> 了解市场与事件、价格与订单簿、持仓、订单和判定。

> [card] [SDK 与 API](https://docs.polymarket.com/cn/getting-started/sdks-apis)
>
> 选择最适合应用的集成方式。

[![Banner](https://mintcdn.com/polymarket-292d1b1b/FOMte3ewbG-LVy3k/images/banner.png?fit=max\&auto=format\&n=FOMte3ewbG-LVy3k\&q=85\&s=d83f2f21e8474e998d8ba0f45810d978)](https://builders.polymarket.com)

![](https://docs.polymarket.com/images/icons/medal.svg)

### [构建者计划](https://builders.polymarket.com)

在 Polymarket 上构建应用，并通过推动交易量获得奖励

![](https://docs.polymarket.com/images/icons/quiz.svg)

### [帮助中心](https://help.polymarket.com)

获取支持、报告问题并查找常见问题的答案

![](https://docs.polymarket.com/images/icons/sensor.svg)

### [服务状态](https://status.polymarket.com)

查看 API 运行时间、服务健康状况和故障报告


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
