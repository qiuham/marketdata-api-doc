---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/How-to-manage-a-local-order-book-correctly
api_type: WebSocket
updated_at: 2026-01-15T23:48:00.931119
---

# How to manage a local order book correctly

1. Open a stream to **wss://fstream.binance.com/stream?streams=btcusdt@depth**.
  2. Buffer the events you receive from the stream. For same price, latest received update covers the previous one.
  3. Get a depth snapshot from **[https://fapi.binance.com/fapi/v1/depth?symbol=BTCUSDT&limit=1000](https://fapi.binance.com/fapi/v1/depth?symbol=BTCUSDT&limit=1000)** .
  4. Drop any event where `u` is < `lastUpdateId` in the snapshot.
  5. The first processed event should have `U` `<= ``lastUpdateId` **AND** `u` >`= ``lastUpdateId`


  * U = firstUpdateId (the first update ID) from the WebSocket stream.
  * u = finalUpdateId (the last update ID) from the WebSocket stream.
  * lastUpdateId = the update ID you got from the REST depth snapshot.


  6. While listening to the stream, each new event's `pu` should be equal to the previous event's `u`, otherwise initialize the process from step 3.ß
  7. The data in each event is the **absolute** quantity for a price level.
  8. If the quantity is 0, **remove** the price level.
  9. Receiving an event that removes a price level that is not in your local order book can happen and is normal.

---

# 如何正确在本地维护一个orderbook副本

1. 订阅 **wss://fstream.binance.com/stream?streams=btcusdt@depth**
  2. 开始缓存收到的更新。同一个价位，后收到的更新覆盖前面的。
  3. 访问Rest接口 **[https://fapi.binance.com/fapi/v1/depth?symbol=BTCUSDT&limit=1000**获得一个1000档的深度快照](https://fapi.binance.com/fapi/v1/depth?symbol=BTCUSDT&limit=1000**%E8%8E%B7%E5%BE%97%E4%B8%80%E4%B8%AA1000%E6%A1%A3%E7%9A%84%E6%B7%B1%E5%BA%A6%E5%BF%AB%E7%85%A7)
  4. 将目前缓存到的信息中`u`< 步骤3中获取到的快照中的`lastUpdateId`的部分丢弃(丢弃更早的信息，已经过期)。
  5. 将深度快照中的内容更新到本地orderbook副本中，并从websocket接收到的第一个`U` `<= ``lastUpdateId` **且** `u` >`= ``lastUpdateId` 的event开始继续更新本地副本。


  * U = 来自 WebSocket 流的 firstUpdateId（第一个更新 ID）。
  * u = 来自 WebSocket 流的 finalUpdateId（最后一个更新 ID）。
  * lastUpdateId = 你从 REST 深度快照中获取的 更新 ID。


  6. 每一个新event的`pu`应该等于上一个event的`u`，否则可能出现了丢包，请从step3重新进行初始化。
  7. 每一个event中的挂单量代表这个价格目前的挂单量**绝对值** ，而不是相对变化。
  8. 如果某个价格对应的挂单量为0，表示该价位的挂单已经撤单或者被吃，应该移除这个价位。