---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#spread-trading-comprehensive-api-workflow-all-trades
anchor_id: spread-trading-comprehensive-api-workflow-all-trades
api_type: API
updated_at: 2026-07-11 19:13:37.039670
---

# All Trades

All users have the ability to receive updates on all trades that take place through the OKX Nitro Spreads product.

It's important to note that OKX Nitro Spreads does not disclose information about the counterparties involved in the trades or the individual `side` (`buy` or `sell`) of the composite legs that were traded.

  1. By subscribing to the `sprd-public-trades`WebSocket channel, WebSocket messages are sent exclusively for trades that have been successfully cleared and settled.

---

# 所有交易

所有用户都能够接收通过 OKX Nitro Spread 产品发生的所有交易的更新。 请务必注意，OKX Nitro Spreads 不会披露有关交易双方及交易方向（买入或卖出）的信息。

  1. 用户可以订阅`sprd-public-trades`频道来获取所有已成功结算的交易。