---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#spread-trading-comprehensive-api-workflow-spread-states
anchor_id: spread-trading-comprehensive-api-workflow-spread-states
api_type: API
updated_at: 2026-07-17 19:17:13.275723
---

# Spread States

There are three different states during a Spread's life cycle: `live`, `suspend`, and `expired` as detailed below:

  1. `live`: Spreads that are actively traded on Nitro Spreads
  2. `suspend`: Spreads in which at least one of the legs is suspended and the other one is active or suspended on the OKX orderbook exchange; or spreads in which the underlying instruments are still live on the OKX orderbook exchange, but removed from Nitro Spreads
  3. `expired`: Spreads in which at least one of the underlying instruments is expired on the OKX orderbook exchange

Please refer to the following table for all possible scenarios given the state of the underlying instruments and the resulting state of the spread on Nitro Spreads (except for the case that the spread is delisted on Nitro Spreads):

Instrument A | Instrument B | Spread State  
---|---|---  
Live | Live | Live  
Suspend | Live | Suspend  
Live | Suspend | Suspend  
Suspend | Suspend | Suspend  
Expired | Live | Expired  
Live | Expired | Expired  
Suspend | Expired | Expired  
Expired | Suspend | Expired  
Expired | Expired | Expired

---

# Spread状态

Spread 的生命周期中存在三种不同的状态：`live`，`suspend`，和 `expired`:

  1. `live`: 在 Nitro Spread 上活跃交易的Spreads
  2. `suspend`：其中至少一条腿被暂停，另一条在 OKX 订单簿交易所处于活跃或暂停状态的价差；或标的工具仍在 OKX 订单簿交易所中存在但已从 Nitro Spread 中移除的Spread
  3. `expired`：至少一条腿在 OKX 订单簿交易所到期的Spread

给定每条腿的状态以及 Nitro Spreads 上的Spread状态（除了在 Nitro Spread上退市的情况），所有可能Spread状态的情况请参考下表：

交易产品A | 交易产品B | Spread状态  
---|---|---  
Live | Live | Live  
Suspend | Live | Suspend  
Live | Suspend | Suspend  
Suspend | Suspend | Suspend  
Expired | Live | Expired  
Live | Expired | Expired  
Suspend | Expired | Expired  
Expired | Suspend | Expired  
Expired | Expired | Expired