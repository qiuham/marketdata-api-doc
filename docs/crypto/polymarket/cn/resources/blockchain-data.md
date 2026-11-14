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
source_url: 'https://docs.polymarket.com/cn/resources/blockchain-data'
updated_at: 2026-11-13
---

# 区块链数据

> 查询 Polymarket 链上交易、余额、持仓和赎回

Polymarket 在 Polygon 上的活动包括交易、ERC-1155 余额、持仓操作和赎回。以下服务通过 SQL 或流式管道提供这些数据。

持仓数据分布在 Conditional Tokens 和 PositionManager 中。构建查询前，请先使用[链上持仓数据](https://docs.polymarket.com/cn/resources/onchain-position-data.md)选择正确的合约、标识符和事件。

> [!NOTE]
>
> 第三方 schema
> 可能落后于合约升级。请将其索引的合约地址与当前[合约](https://docs.polymarket.com/cn/resources/contracts.md)页面核对。

## 数据提供商

### Goldsky

[Goldsky](https://docs.goldsky.com/chains/polymarket) 提供 Polymarket 链上活动的实时数据管道，可将交易、余额、持仓和其他合约数据传输到你的数据库或数据仓库。

Goldsky 还与 [ClickHouse](https://clickhouse.com) 合作创建了 [CryptoHouse](https://crypto.clickhouse.com)，你可以使用 SQL 查询 Polymarket 链上数据。

### Dune

[Dune](https://dune.com) 提供 Polymarket 合约索引数据的 SQL 访问，并支持自定义仪表板。

以下查询可以帮助你快速开始：

| 查询 | 说明 | 链接 |
| - | - | - |
| 交易量 | 名义交易量以及 Maker 和 Taker USDC 交易量 | [查看 Dune 查询](https://dune.com/queries/6545441) |
| TVL | 锁定在 Polymarket 智能合约中的 USDC | [查看 Dune 查询](https://dune.com/queries/6588784) |
| 未平仓量 | 市场当前及历史预估未平仓量 | [查看 Dune 查询](https://dune.com/queries/6555478) |

### Allium

[Allium](https://docs.allium.so/historical-data/predictions) 提供 Polymarket 历史活动的 SQL 访问，并支持自定义仪表板。

\--

## 仪表板

以下第三方区块链分析平台汇总并可视化 Polymarket 数据：

> [card] [Blockworks](https://blockworks.com/analytics/polymarket)

> [card] [Artemis](https://app.artemisanalytics.com/asset/polymarket?from=assets)

> [card] [Dune](https://dune.com/discover/content/popular?q=polymarket\&resource-type=dashboards)

> [card] [DeFiLlama](https://defillama.com/protocol/polymarket)

> [card] [The Block](https://www.theblock.co/data/decentralized-finance/prediction-markets-and-betting)

> [card] [Token Terminal](https://tokenterminal.com/explorer/projects/polymarket)

> [card] [Allium](https://predictions.allium.so)

### 社区仪表板

由社区创建的 Polymarket 链上分析 Dune 仪表板：

| 仪表板 | 创建者 | 链接 |
| - | - | - |
| Polymarket Overview | [@datadashboards](https://x.com/datadashboards) | [查看仪表板](https://dune.com/datadashboards/polymarket-overview) |
| Polymarket Volume, OI, Markets, Addresses and TVL | [@hildobby](https://x.com/hildobby) | [查看仪表板](https://dune.com/hildobby/polymarket) |
| Polymarket Historical Accuracy | [@alexmccullaaa](https://x.com/alexmccullaaa) | [查看仪表板](https://dune.com/alexmccullough/how-accurate-is-polymarket) |
| Polymarket Builders Dashboard | [@defioasis](https://x.com/defioasis) | [查看仪表板](https://dune.com/gateresearch/pmbuilders) |


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
