---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/demo
api_type: REST
updated_at: 2026-10-23 18:45:13.075313
---

# Introduction

## Overview

Event Contract is a structured product offered by Bybit that allows users to trade on the outcome of market events with a defined payout structure.

## Access

caution

Only **market makers** are permitted to call the Event Contract OpenAPI endpoints. To apply for market maker access, please contact your **Relation Manager**. Public access may be considered in the future.

## WebSocket streams

  * Public: [Orderbook](/docs/v5/event/websocket/public/orderbook) and [Trade](/docs/v5/event/websocket/public/public-trade).
  * Private: [Position](/docs/v5/event/websocket/private/position), [Execution](/docs/v5/event/websocket/private/execution), and [Order](/docs/v5/event/websocket/private/order).



For account transaction records, see [Get Transaction Log](/docs/v5/account/transaction-log).

---

# 簡介

## 概述

Event Contract 是 Bybit 提供的結構化產品，允許用戶以固定賠付結構對市場事件的結果進行交易。

## 訪問權限

警告

僅**做市商** 可調用 Event Contract OpenAPI 接口。如需申請做市商資格，請聯繫您的 **Relation Manager** 。 未來可能考慮向公眾開放。

## WebSocket 推送

  * 公共頻道：[訂單簿](/docs/zh-TW/v5/event/websocket/public/orderbook)和[成交](/docs/zh-TW/v5/event/websocket/public/public-trade)。
  * 私有頻道：[持倉](/docs/zh-TW/v5/event/websocket/private/position)、[成交](/docs/zh-TW/v5/event/websocket/private/execution)和[訂單](/docs/zh-TW/v5/event/websocket/private/order)。



賬戶交易記錄請參閱[獲取交易日誌](/docs/zh-TW/v5/account/transaction-log)。