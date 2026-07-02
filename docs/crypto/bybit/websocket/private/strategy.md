---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/websocket/private/strategy
api_type: WebSocket
updated_at: 2026-07-02 19:22:34.682838
---

# Full Orderbook

Subscribe to the full orderbook stream. Delivers **delta-only** updates for deep, full-depth market data.

> **Covers: Spot / USDT contract / USDC contract / Inverse contract**

info

  * [Retail Price Improvement (RPI)](https://www.bybit.com/en/help-center/article/Retail-Price-Improvement-RPI-Order) orders will not be included in the messages.
  * This stream pushes **delta updates only** — there is no initial snapshot message. You must initialize your local order book via the [REST full orderbook snapshot](/docs/v5/market/full-ob) before applying deltas.



## Release Schedule

Product| Testnet| Mainnet  
---|---|---  
Spot| July 6, 2026| July 16, 2026  
Futures (linear & inverse)| Est.July 13, 2026| not determined  
  
### Push frequency

**Linear, inverse & spot:**  
Full depth data, push frequency: **200ms**  


**Topic:**  
`orderbook.full.{symbol}` e.g., `orderbook.full.BTCUSDT`

Reset scenarios (`u=1`)

Scenario| WS payload| REST snapshot| Client action  
---|---|---|---  
Service restart| `u=1`| `u` may also reset to `1`| Overwrite local book with snapshot  
Symbol delist| `u=1`, `b=[]`, `a=[]`| Returns empty| Clear local book, mark as **unavailable**  
Before pre-market auction| `u=1`, delta empty| May return empty| Keep book empty, treat as **NO_BOOK**  
Auction → continuous trading| `u=1`, delta empty| Returns valid snapshot| Pull snapshot, then continue with deltas  
Lot / tick configuration change| `u=1`, delta can be empty| Snapshot ready when applicable| Clear and re-sync local book  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
topic| string| Topic name  
type| string| Data type. Always `delta`  
ts| number| The timestamp (ms) that the system generates the data  
data| object| Object  
> s| string| Symbol name  
> b| array| Bid delta entries. Sorted by price in descending order  
>> b[0]| string| Bid price  
>> b[1]| string| Bid size. `0` means this price level should be deleted  
> a| array| Ask delta entries. Sorted by price in ascending order  
>> a[0]| string| Ask price  
>> a[1]| string| Ask size. `0` means this price level should be deleted  
> u| integer| Update ID

  * Always incremental within a session
  * When `u=1`, it is a re-initialization signal — overwrite your local order book with a fresh [REST snapshot](/docs/v5/market/full-ob)

  
> seq| integer| Cross sequence. Use this to compare across different orderbook levels — a smaller `seq` means the data was generated earlier  
cts| number| The timestamp from the matching engine when this orderbook data is produced. It can be correlated with `T` from [public trade channel](/docs/v5/websocket/public/trade)  
  
### Subscribe Example
    
    
      
    

### Response Example
    
    
      
    

### Full Order Book Synchronization Procedure

Use the REST endpoint to fetch an Order Book (OB) snapshot, then subscribe to OB delta updates via WebSocket to maintain a complete local order book. Both the OB snapshot and OB delta messages include two fields — `seq` and `u` — for data matching and sequencing.

  * `seq`: The matching engine version number. It is monotonically increasing but not guaranteed to be consecutive — adjacent delta packets for the same symbol may have non-contiguous `seq` values.
  * `u`: The update ID. It is consecutive — the `u` value of each delta packet increments by one from the previous (`u+1`). However, when the system restarts or the tick size is adjusted, `u` resets to `1` and delta numbering starts over.


  1. Open a market data WebSocket connection and subscribe to the full-depth order book channel.
  2. Buffer all deltas received from the stream, recording the `seq` and `u` values of the first delta.


  * If a discontinuity in `u` is detected, clear the buffer and restart buffering.
  * If `seq` is detected to have decreased, discard that delta packet.


  3. Fetch the [full-depth order book snapshot](/docs/v5/market/full-ob) from the REST endpoint.
  4. Compare the snapshot's `seq` and `u` against the buffered deltas:


  * If the snapshot's `seq` is strictly less than the first buffered delta's `seq`, repeat step 3 until a sufficiently recent snapshot is obtained.
  * In the buffered deltas, discard all deltas whose `seq` is less than the snapshot's `seq`.
  * If the snapshot's `seq` equals the delta's `seq` but their `u` values differ, repeat step 3 until a sufficiently recent snapshot is obtained.


  5. Once the snapshot's `seq` and `u` both match the delta's `seq` and `u`, initialize the local order book with the snapshot. Set the local order book version to the snapshot's `u` value.
  6. Apply all remaining buffered deltas to the local order book as described below, then continue processing subsequent real-time deltas.



#### Order Book Update Procedure

For each incoming delta event:

  1. Validate Event Continuity


  * If the event's `u` is less than the local order book's `u`, ignore the event.
  * If the event's `u` is greater than the local order book's `u` \+ 1, one or more events have been missed. In this case:
    * Discard the local order book.
    * Restart the synchronization process from the beginning.
  * Under normal circumstances, the next event's u should equal the previous event's u + 1.
  * If the event's `u` = 1, then restart the sync procedure


  2. Apply Price Level Updates



For every price level in bids (b) and asks (a):

  * If the price level does not exist in the local order book, insert it with the specified quantity.
  * If the quantity is zero, remove the price level from the local order book.
  * Otherwise, update the quantity of the existing price level.



info

The REST snapshot endpoint returns a maximum of 10,000 price levels per side. As a result, price levels outside the initial snapshot range are unknown unless they subsequently appear in delta updates.

Therefore, quantities for levels beyond the snapshot depth may not represent the complete state of the order book. For most trading and market analysis use cases, however, the available depth (typically more than 10,000 levels per side) is sufficient to provide an accurate view of market liquidity and trading conditions.

---

# 全深度訂單簿

訂閱全深度訂單簿推送。僅推送**增量（delta）** 數據，提供深度全量行情。

> **覆蓋範圍: 現貨 / USDT永續 / USDC永續 / 反向合約**

信息

  * 零售價格優化（RPI）訂單不會包含在推送消息中。
  * 此頻道**僅推送增量數據** ，不會推送初始全量快照。請先通過 [REST 全深度訂單簿接口](/docs/zh-TW/v5/market/full-ob) 初始化本地訂單簿，再應用增量更新。



## 上線時間表

產品| 測試網| 主網  
---|---|---  
現貨| 2026年7月6日| 2026年7月16日  
期貨（線性 & 反向）| 預計2026年7月13日| 未定  
  
### 推送頻率

**USDT合約、反向合約 & 現貨:**  
全深度數據，推送頻率: **200ms**  


**Topic:**  
`orderbook.full.{symbol}` 例如, `orderbook.full.BTCUSDT`

重置場景 (`u=1`)

場景| WebSocket 推送| REST 快照| 客戶端處理  
---|---|---|---  
服務重啟| `u=1`| `u` 也可能重置為 `1`| 以 REST 快照覆蓋本地訂單簿  
合約下架| `u=1`, `b=[]`, `a=[]`| 返回空數據| 清空本地訂單簿，標記為**不可用**  
盤前競價期間（無訂單簿）| `u=1`，delta 為空| 可能返回空| 保持本地訂單簿為空，標記為 **NO_BOOK**  
競價 → 連續競價| `u=1`，delta 為空| 返回有效快照| 拉取 REST 快照後繼續應用增量  
精度等配置變更| `u=1`，delta 可為空| 就緒後返回快照| 清空並重新同步本地訂單簿  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
topic| string| Topic名  
type| string| 數據類型. 固定為 `delta`  
ts| number| 行情服務生成數據的時間戳（毫秒）  
data| object| Object  
> s| string| 合約名稱  
> b| array| Bid 增量, 買方. 按照價格從大到小  
>> b[0]| string| 買方報價  
>> b[1]| string| 買方數量. `0` 表示該價位應被刪除  
> a| array| Ask 增量, 賣方. 按照價格從小到大  
>> a[0]| string| 賣方報價  
>> a[1]| string| 賣方數量. `0` 表示該價位應被刪除  
> u| integer| 更新id 

  * 在同一會話內始終遞增
  * 當 `u=1` 時，為重置信號——請立即拉取 [REST 快照](/docs/zh-TW/v5/market/full-ob) 並覆蓋本地訂單簿

  
> seq| integer| 撮合版本號. 可用於關聯不同檔位的 orderbook，值越小說明數據生成越早  
cts| number| 產生此訂單簿數據時來自撮合引擎的時間戳. 可用於與[平台成交](/docs/zh-TW/v5/websocket/public/trade)頻道中的`T`進行關聯  
  
### 訂閱示例
    
    
      
    

### 響應示例
    
    
      
    

### 全深度訂單簿同步流程

提供了 REST 請求查詢 Order Book（OB）快照，並透過 WebSocket 訂閱 Order Book 增量資料，以維護完整的 Order Book。於 OB 快照與 OB 增量資料中，均提供 seq 與 u 兩個欄位，用於資料匹配與定位。

  * seq：撮合版本號，具備單調遞增特性，但不保證連續性。也就是說，同一交易對的相鄰增量資料包，其 seq 值可能不連續。
  * u：更新 ID，具備連續性，相鄰增量資料包的 u 值會依序遞增（u+1）。但當系統重啟或調整 Tick Size 時，u 會重置為 1，並重新對增量資料進行編號。


  1. 開啟行情 WebSocket 連接並訂閱全深度訂單簿頻道。
  2. 緩存從串流中接收到的所有增量，記錄第一個增量的 `seq` 与 `u` 值。


  * 若偵測到 `u` 不連續，清空緩存區並重新開始緩存。
  * 若偵測到 `seq` 变小，丢弃该增量包。


  3. 從Rest接口獲取[全深度訂單簿快照](/docs/zh-TW/v5/market/full-ob)
  4. 將快照的 `seq`，`u` 與緩存增量進行比對：


  * 若快照的 `seq` 嚴格小於第一個緩存增量的 seq，重複步驟 3，直到獲得足夠新的快照。
  * 在緩存增量中，丟棄所有 `seq` 小於快照 `seq` 的增量。
  * 若快照的seq与增量的seq相等，但u不相等，重複步驟 3，直到獲得足夠新的快照。


  5. 直到获取快照的seq，u与增量的seq，u都相同时，使用快照初始化本地訂單簿，本地訂單簿版本應設定為快照的u值。
  6. 按照以下的說明將所有剩餘的緩存增量應用至本地訂單簿，然後繼續處理後續到來的即時增量。



#### 訂單簿更新流程

針對每個收到的增量（delta）事件：

  1. 驗證增量連續性


  * 若增量的 `u` 小於本地訂單簿的 `u`，忽略該增量。
  * 若增量的 `u` 大於本地訂單簿的 `u` \+ 1，表示遺漏了一個或多個增量，此時：
    * 丟棄本地訂單簿。
    * 從頭重新啟動同步流程。
  * 正常情況下，下一個增量的 u 應等於上一個增量的 u + 1。
  * 若增量的 `u` 變成1，則重新啟動同步流程。


  2. 應用價位更新



對買方（b）和賣方（a）中的每個價位：

  * 若該價位不存在於本地訂單簿中，以指定數量插入該價位。
  * 若數量為零，從本地訂單簿中移除該價位。
  * 否則，更新現有價位的數量。



信息

REST 快照接口每側最多返回 10,000 個價位。因此，超出初始快照範圍的價位在增量更新中出現之前，其狀態是未知的。

這意味著超出快照深度的價位數量，可能無法完整反映訂單簿的實際狀態。不過，對於大多數交易和市場分析場景而言，可用深度（每側通常超過 10,000 個價位）已足以提供準確的市場流動性與交易狀況視圖。