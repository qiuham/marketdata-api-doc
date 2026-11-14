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
source_url: 'https://docs.polymarket.com/cn/programs/builders/overview'
updated_at: 2026-11-13
---

# 概览

> 构建通过 Polymarket 路由订单的应用

**Builder** 是将用户订单路由到 Polymarket 的个人、团体或组织。如果你创建的平台允许用户通过你的系统在 Polymarket 上交易，则可以加入此计划。

## 计划权益

> [card] 免 Gas 交易
>
> 通过 relayer 执行支持的链上操作，无需支付 Gas

> [card] 订单归因
>
> 在 Builder 排行榜上获得已撮合订单的归因

### 你将获得

| 权益 | 说明 |
| - | - |
| **Relayer 访问权限** | 免费执行支持的钱包部署、授权和持仓操作 |
| **交易量追踪** | 将所有订单归因到你的 Builder 资料 |
| **排行榜** | 在 [builders.polymarket.com](https://builders.polymarket.com) 上公开展示 |
| **支持** | Telegram 频道和工程支持（Verified+） |

## 工作原理

**1. 用户下单**

用户通过你的应用下单。

**2. 附加 Builder Code**

应用为每个订单添加你的 Builder Code。

**3. 提交到 CLOB**

应用将已签名订单提交到 Polymarket CLOB。已签名订单包含 Builder Code。

**4. 执行交易**

Polymarket 撮合订单。支持的 relayer 操作仍由 Builder 免费使用。

**5. 交易量归因**

对于每笔附有你的 Builder Code 的已撮合交易，其交易量都会计入你的 Builder
账户。

## 开始使用

**1. 创建 Builder 资料**

在 Polymarket 设置中打开 [Builders](https://polymarket.com/settings?tab=builder)，然后复制你的 Builder Code。

**2. 附加 Builder Code**

为提交的每个订单附加 Builder Code。请参阅 [Builder
归因](https://docs.polymarket.com/cn/trading/place-orders.md#构建者归因)。

**3. 启用免 Gas 交易**

使用 Polymarket relayer 部署钱包并[执行免 Gas
交易](https://docs.polymarket.com/cn/trading/wallets-auth.md#执行免-gas-交易)。

**4. 追踪表现**

在 [Builder 排行榜](https://builders.polymarket.com)上监控交易量。

已撮合交易量最多可能需要 **24 小时**才会显示在排行榜上。

***

## 后续步骤

> [card] [创建新账户](https://docs.polymarket.com/cn/trading/wallets-auth.md#创建新账户)
>
> 创建 Builder 账户，以及用于为用户配置账户的凭据。

> [card] [了解等级](https://docs.polymarket.com/cn/programs/builders/tiers.md)
>
> 了解速率限制和升级方式。

> [card] [订单归因](https://docs.polymarket.com/cn/trading/place-orders.md#构建者归因)
>
> 配置客户端，将交易归因到你的账户。

> [card] [执行免 Gas 交易](https://docs.polymarket.com/cn/trading/wallets-auth.md#执行免-gas-交易)
>
> 无需支付 Gas 即可授权 token、转移资金和管理仓位。


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
