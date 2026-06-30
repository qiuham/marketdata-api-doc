---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#spread-trading-introduction
anchor_id: spread-trading-introduction
api_type: API
updated_at: 2026-06-30 19:55:29.604725
---

# Introduction

### Basic Concepts

  1. **Spread -** Entering a trade where the trader is long one instrument and short an offsetting quantity of a related instrument, forming a trade with two risk offsetting legs.
  2. **Order-book -** A collection of offers to trade an instrument or basket. Each offer contains a defined instrument or group of instruments, relevant quantity, and the price at which the offerer is willing to transact. Takers can then immediately consume these offers up to the full amount of quantity listed at the offered price. The pending order limit of spread trading is 500 across all spreads.

### High Level Workflow

Nitro Spreads is centered around the familiar concept of a Central Limit Order Book (**CLOB**).

  * Spreads consist of instruments sourced from OKX where they are cleared and settled.
  * Anyone can act as a "Taker," who consumes an existing resting order, or a "Maker," whose order is consumed.
  * Trades take place when orders are crossed. Trades are then sent for clearing and settlement on OKX.

At a high level, the Nitro Spreads workflow is as follows:

  1. _Maker_ rests a Limit Order upon a Spread's Order Book.
  2. _Taker_ consumes a resting Order via a Limit Order.
  3. The crossed orders are sent for clearing and settlement.
  4. The _Taker_ and _Maker_ receive confirmation of the success or rejection of the Trade.
  5. All users are notified of successfully settled & cleared Trades, minus the counterparties or sides (`buy` / `sell`) involved.

Key aspects of Nitro Spreads:

  * All Spreads have **publicly accessible** Central Limit Order Books **(CLOB)**.
  * The availability of trading Spreads is determined by OKX. Typically, these Spreads encompass all possible combinations of delta one derivatives (Expiry Futures and Perpetual Futures) and SPOT within a specific instrument family (e.g. "BTC/USDT" or "ETH/USDC").
  * **Partial fills** and multiple orders can be consumed as part of a single trade.
  * **Counterparties** are **NOT** selected. All Spread Order Books can be engaged by anyone, effectively trading against the broader market.
  * Anonymity is maintained throughout the process, with all orders and trades conducted on an **anonymous basis**.
  * Users have the flexibility to place multiple orders on both the bid and ask sides of the Order Book, allowing for a **ladder-style** configuration.

---

# 介绍

### 基本概念 

  1. 价差（**Spread） -** 做多一种产品并同时做空数量等价的另一种相关产品，形成具有两条风险互相抵消的腿的交易
  2. 订单簿（**Order-book） -** 一种或一组交易产品的报价集合。每个报价都包含一个或一组定义的产品、相关数量以及 _Maker_(报价者)愿意交易的价格。然后， _Taker_(接受者)可以立即消耗这些报价，直至订单簿上列出的全部数量。价差交易挂单限额为所有价差挂单合计不超过500个。

### 基本工作流程 

Nitro Spreads 以熟悉的**中央限价订单簿 (CLOB)** 概念为中心：

  * Spreads里包含的产品来自OKX交易所，交易之后也在OKX交易所进行清算和结算。
  * 任何人都可以充当“Taker”，消耗现有的剩余订单，或“Maker”，其订单被消耗。
  * 交易在订单被匹配时发生，之后它们被发送到 OKX 进行清算和结算。

简单来说，Nitro Spreads 工作流程是

  1. _Maker 在 Spread 的订单簿上设置限价订单。_
  2. _Taker通过限价单消耗一个resting Order。_
  3. 被匹配的订单被发送去清算和结算。
  4. Taker和Maker收到交易成功或拒绝的确认
  5. 所有用户都会收到成功结算和清算交易的通知，除去涉及的交易双方以交易方向 (买入或卖出) 等信息。

Nitro Spreads 的主要方面：

  * 所有价差都有**可公开访问** 的中央限价订单簿 (**CLOB**)。
  * Spreads的可用性由OKX决定。通常，这些Spreads包括同一标的下（如“BTC/USDT”或“ETH/USDC”）中 delta one 衍生品（交割和永续）和现货的所有可能组合。
  * **部分成交** 和多个订单可以作为单笔交易的一部分。
  * 交易对手方**不是** 任由用户选择的。任何人都可以参与所有Spread的订单簿，有效地与更广泛的市场进行交易。
  * 整个过程保持匿名，所有订单和交易均在**匿名** 的基础上进行。
  * 用户可以灵活地在订单簿的买卖双方下多个订单，从而实现阶梯式配置。