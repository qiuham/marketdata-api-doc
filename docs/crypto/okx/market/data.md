---
exchange: okx
source_url: https://www.okx.com/docs-v5/trick_en/#market-data
anchor_id: market-data
api_type: API
updated_at: 2026-01-15T17:46:44.101975
---

# Market data

Users can receive real time market data updates from websocket channels.

`bbo-tbt` and `books5` are depth snapshots that are published every 10ms and 100ms. New snapshots are not sent when there is no change in the orderbook.

`books`, `books-l2-tbt`, and `books50-l2-tbt` are incremental order book channels. `books` publishs the changes in the order book every 100ms. `books-l2-tbt` and `books50-l2-tbt` push changes every 10ms. In order to use `books-l2-tbt` and `books50-l2-tbt`, users must login before subscribing and are limited to VIP levels 5 and 4, respectively.

Order book data is created once every 10ms internally and relevant data is sent out depending on the subscribed channel. Users receive the same order book image from all websocket connections and channels.

No update is sent if the depth changes from A -> B -> A during the interval. If there are no updates to the depth for an extended period, the system resends the current depth for snapshot channels, a message with no depth updates for incremental channels, to inform users that the connection is still active.