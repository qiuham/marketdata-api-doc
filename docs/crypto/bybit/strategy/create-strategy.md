---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/strategy/create-strategy
api_type: REST
updated_at: 2026-07-15 18:56:24.030643
---

# Create Strategy Order

Create a strategy order. Supported strategy types: `chaseOrder`, `twap`, `iceberg`, `pov`.

## Strategy Types

### TWAP (Time-Weighted Average Price)

Splits a large order into equal-sized sub-orders executed at fixed time intervals, minimizing market impact and achieving a price close to the time-weighted average.

**Execution logic:** `Number of sub-orders = Running Time (seconds) ÷ Frequency`. Sub-orders that fail to fill are retried once; if unsuccessful, they are canceled and the strategy continues.

Please refer to [Introduction to TWAP Strategy](https://www.bybit.com/en/help-center/article/Introduction-to-TWAP-Strategy?category=5f2fb74e9c8b771130) to get more details.

Parameter| Constraint  
---|---  
Total quantity (`size`)| Must be ≥ Max(MinNotional × subOrders ÷ LastPrice × 1.1, MinSize × subOrders)  
Running time (`duration`)| 5 minutes – 24 hours  
Sub-order interval (`interval`)| 5 – 120 seconds  
Sub-order quantity| ≤ 50% of the exchange's maximum single order size (Perpetual/Futures)  
Random quantity variance| ±20% if `isRandom` is enabled  
  
* * *

### Chase Order (Chase Limit Order)

Continuously places and adjusts a limit order at the best bid/ask price to track market movements until the order is fully filled, canceled, or reaches the maximum chase distance.

**Execution logic:** The order price updates every second. All Chase Limit Orders are **Post Only** by default (maker execution). If the order is rejected by the Post Only condition 5 consecutive times, the strategy is canceled.

Please refer to [Chase Limit Order](https://www.bybit.com/en/help-center/article/Chase-Order?category=5f2fb74e9c8b771130) to get more details.

* * *

### Iceberg Order

Splits a large order into multiple smaller sub-orders that are placed sequentially, revealing only a small portion of the total order size to the market at any one time.

**Execution logic:** Each sub-order enters the order book → upon fill, the next sub-order is automatically placed → repeats until the full quantity is executed.

Please refer to [Iceberg Order](https://www.bybit.com/en/help-center/article/Iceberg-Order?category=5f2fb74e9c8b771130) to get more details.

**Order preferences:**

Preference| Execution behavior  
---|---  
`Chase Limit (Taker)`| Buy at Ask1 / Sell at Bid1; prioritizes speed  
`Chase Limit`| Buy at Bid1 / Sell at Ask1; maker execution  
`Chase Limit (offset)`| Fixed distance from Ask1/Bid1; balances speed and cost  
`Fixed Prices`| All sub-orders placed at a single fixed price  
  
* * *

### POV Order (Percentage of Volume)

Participates in market volume at a fixed rate, dynamically sizing each sub-order as a percentage of observed trading activity or order book depth to minimize market impact.

**Execution logic:** At each `interval`, the strategy samples market activity based on the selected mode → calculates sub-order quantity using `participationRate` → places the order → repeats until `maxQty` (`size`) is reached or `maxDuration` (`duration`) expires. Setting `interval` to `0` executes once immediately (OneTime mode).

**Note:** POV supports Perpetuals only (`UTA_USDT`, `UTA_USDC`, `UTA_INVERSE`, `UTA_INVERSE_FUTURE`, `UTA_USDT_FUTURE`). Spot is not supported. When `interval` > `0`, at least one of `size` or `duration` must be provided.

**Execution modes (`povParams.mode`):**

Mode| Order type| Volume reference  
---|---|---  
`TradedVolume`| Market order| Historical traded volume over `referenceWindow` seconds; range: [60, 14400]  
`OppositeSideLiquidity`| Taker limit at best bid/ask| Opposite-side book depth; Top-N levels via `depthReference` [1, 10]  
`SameSideLiquidity`| Post-Only limit at best bid/ask| Same-side book depth; Top-N levels via `depthReference` [1, 10]; maker execution only  
  
* * *

### HTTP Request

POST`/v5/strategy/create`

### Request Parameters

  * TWAP
  * Chase Order
  * Iceberg
  * POV



Parameter| Required| Type| Comments  
---|---|---|---  
category| **true**|  string| Product type. `UTA_USDT`(USDT Perpetual), `UTA_USDC`(USDC Perpetual), `UTA_SPOT`(Spot), `UTA_INVERSE`(Inverse Perpetual), `UTA_INVERSE_FUTURE`(Inverse Futures), `UTA_USDT_FUTURE`(USDT Futures)  
symbol| **true**|  string| Symbol name, e.g. `BTCUSDT`  
side| **true**|  string| `Buy`, `Sell`  
size| false| string| Total order quantity (coin). Either "size" or "positionValue" is **needed**  
positionValue| false| string| Total order quantity (value). Either "size" or "positionValue" is **needed**  
strategyType| **true**|  string| Strategy type. `twap`  
duration| **true**|  integer| Total execution duration in seconds. Range: [300, 86400]. Must be divisible by `interval`  
reduceOnly| false| boolean| Reduce-only order, must set `true` when reducing the position. `true`, `false`  
positionIdx| false| integer| Position index. `0`: one-way mode, `1`: buy side of hedge mode, `2`: sell side of hedge mode. **Required** for hedge mode  
leverageType| false| integer| Spot leverage type. `0`: normal, `1`: borrow to trade (`UTA_SPOT` only)  
interval| false| integer| Sub-order placement interval in seconds. `5`, `10`, `15`, `30`(default), `60`, `120`  
isRandom| false| boolean| Whether to randomize each sub-order quantity by ±20%  
triggerPrice| false| string| Advanced settings (Trigger price): Strategy activates when the market price reaches this value  
maxChasePrice| false| string| Advanced settings (Stop Price): Strategy terminates when the last traded price reaches this value  
chaseDistance| false| string| Advanced settings - ordertype=Limit (default: market): Price distance from best bid/ask (absolute value), e.g. `"0.5"`. Mutually exclusive with `chasePercentE4`; `chaseDistance` takes priority if both are set  
chasePercentE4| false| integer| Advanced settings - ordertype=Limit (default: market): Price offset from best bid/ask in basis points (1/10000), e.g. `100` = 1%. Mutually exclusive with `chaseDistance`  
  
Parameter| Required| Type| Comments  
---|---|---|---  
category| **true**|  string| Product type. `UTA_USDT`(USDT Perpetual), `UTA_USDC`(USDC Perpetual), `UTA_SPOT`(Spot), `UTA_INVERSE`(Inverse Perpetual), `UTA_INVERSE_FUTURE`(Inverse Futures), `UTA_USDT_FUTURE`(USDT Futures)  
symbol| **true**|  string| Symbol name, e.g. `BTCUSDT`  
side| **true**|  string| `Buy`, `Sell`  
size| false| string| Total order quantity (coin). Either "size" or "positionValue" is **needed**  
positionValue| false| string| Total order quantity (value). Either "size" or "positionValue" is **needed**  
strategyType| **true**|  string| Strategy type. `chaseOrder`  
reduceOnly| false| boolean| Reduce-only order, must set `true` when reducing the position. `true`, `false`  
positionIdx| false| integer| Position index. `0`: one-way mode, `1`: buy side of hedge mode, `2`: sell side of hedge mode. **Required** for hedge mode  
leverageType| false| integer| Spot leverage type. `0`: normal, `1`: borrow to trade (`UTA_SPOT` only)  
chaseDistance| false| string| Price distance from best bid/ask (absolute value), e.g. `"0.5"`. Mutually exclusive with `chasePercentE4`; `chaseDistance` takes priority if both are set  
chasePercentE4| false| integer| Price offset from best bid/ask in basis points (1/10000), e.g. `100` = 1%, range: [0, 500]. Mutually exclusive with `chaseDistance`  
triggerPrice| false| string| Advanced setting (Trigger price): Strategy activates when the market price reaches this value  
maxChasePrice| false| string| Advanced setting (Max chase price): Stop chasing when the last traded price reaches this value  
  
Parameter| Required| Type| Comments  
---|---|---|---  
category| **true**|  string| Product type. `UTA_USDT`(USDT Perpetual), `UTA_USDC`(USDC Perpetual), `UTA_SPOT`(Spot), `UTA_INVERSE`(Inverse Perpetual), `UTA_INVERSE_FUTURE`(Inverse Futures), `UTA_USDT_FUTURE`(USDT Futures)  
symbol| **true**|  string| Symbol name, e.g. `BTCUSDT`  
side| **true**|  string| `Buy`, `Sell`  
size| false| string| Total order quantity (coin). Either "size" or "positionValue" is **needed**  
positionValue| false| string| Total order quantity (value). Either "size" or "positionValue" is **needed**  
strategyType| **true**|  string| Strategy type. `iceberg`  
reduceOnly| false| boolean| Reduce-only order, must set `true` when reducing the position. `true`, `false`  
positionIdx| false| integer| Position index. `0`: one-way mode, `1`: buy side of hedge mode, `2`: sell side of hedge mode. **Required** for hedge mode  
leverageType| false| integer| Spot leverage type. `0`: normal, `1`: borrow to trade (`UTA_SPOT` only)  
subSize| false| string| Quantity per sub-order. Mutually exclusive with `orderCount`; `subSize` takes priority if both are set  
orderCount| false| integer| Number of sub-orders. Mutually exclusive with `subSize` or `subPositionValue`  
subPositionValue| false| string| Order value per sub-order. Mutually exclusive with `orderCount`; `subPositionValue` takes priority if both are set  
postOnly| false| integer| Maker-only mode. `0`: post-only (maker only), `1`: taker allowed  
maxChasePrice| false| string| Price limit parameter. Buy orders are only placed when the price is at or below this limit and pause if the price rises above it. Sell orders are only placed when the price is at or above this limit and pause if the price falls below it  
limitPrice| false| string| **Order preferences: Limit Price** , limit price applied to all sub-orders  
chaseDistance| false| string| **Order preferences: Chase Limit (offset)** , Price distance from best bid/ask (absolute value), e.g. `"0.5"`. Mutually exclusive with `chasePercentE4`; `chaseDistance` takes priority if both are set.   
**Order preferences: Chase Limit (Taker)** , `"-1"` means immediate fill at counterparty price  
chasePercentE4| false| integer| **Order preferences: Chase Limit (offset)** , Price offset from best bid/ask in basis points (1/10000), e.g. `100` = 1%, range: [0, 100]. Mutually exclusive with `chaseDistance`  
  
Parameter| Required| Type| Comments  
---|---|---|---  
category| **true**|  string| Product type. `UTA_USDT`(USDT Perpetual), `UTA_USDC`(USDC Perpetual), `UTA_INVERSE`(Inverse Perpetual), `UTA_INVERSE_FUTURE`(Inverse Futures), `UTA_USDT_FUTURE`(USDT Futures)  
strategyType| **true**|  string| Strategy type. `pov`  
symbol| **true**|  string| Symbol name, e.g. `BTCUSDT`  
side| **true**|  string| `Buy`, `Sell`  
size| false| string| Total order quantity (coin). **Required** either "size" or "duration"  
duration| false| integer| Total execution duration in seconds. Range: [900, 86400]. **Required** either "size" or "duration"  
interval| false| integer| Sub-order placement interval in seconds. "0": one time execution, otherwise, range: [5, 3600]  
reduceOnly| false| boolean| Reduce-only order, must set `true` when reducing the position. `true`, `false`  
positionIdx| false| integer| Position index. `0`: one-way mode, `1`: buy side of hedge mode, `2`: sell side of hedge mode. **Required** for hedge mode  
povParams| **true**|  object| Param object  
> mode| **true**|  string| Execution modes, `TradedVolume`: places a market order based on historical volume  
`OppositeSideLiquidity`: places a taker limit at BBO based on the counterparty depth, `SameSideLiquidity`: places a post-only order at BBO based on the order side  
> participationRate| **true**|  string| Participation rate, range: [1, 100], support 1 decimal. e.g, `"25.1"`=25.1%  
> referenceWindow| false| string| **Required** when "mode"=`TradedVolume`, reference window for historical trading volume, range: [60, 14400]  
> depthReference| false| integer| **Required** when "mode"=`OppositeSideLiquidity` or `SameSideLiquidity`, reference depths, range: [1, 10]  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
strategyId| string| Strategy ID (UUID format)  
result| string| Execution result. `null` if creation succeeded  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/strategy/create HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1773711467000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "side": "Buy",  
        "symbol": "BTCUSDT",  
        "reduceOnly": false,  
        "category": "UTA_USDT",  
        "size": "0.1",  
        "positionIdx": 1,  
        "strategyType": "chaseOrder",  
        "chasePrice": "75967.7",  
        "maxChasePrice": "83564.5",  
        "triggerPrice": "75000.0"  
    }  
    
    
    
      
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "strategyId": "119b6211-2611-461b-be5e-5ac557099e82",  
            "result": null  
        },  
        "retExtInfo": {},  
        "time": 1773711467052  
    }

---

# 創建策略訂單

創建策略訂單。支援的策略類型：`chaseOrder`、`twap`、`iceberg`, `pov`。

## 策略類型

### TWAP（時間加權平均價格）

將大額訂單拆分為等量子訂單，按固定時間間隔執行，降低市場衝擊並使成交均價接近時間加權平均值。

**執行邏輯：** `子訂單數量 = 執行時間（秒）÷ 頻率`。未成交子訂單將重試一次；若仍未成功，則取消並繼續執行後續子訂單。

請參閱 [TWAP 策略介紹](https://www.bybit.com/en/help-center/article/Introduction-to-TWAP-Strategy?category=5f2fb74e9c8b771130) 了解更多細節。

參數| 限制條件  
---|---  
總數量（`size`）| 必須 ≥ Max(最小名義價值 × 子訂單數 ÷ 最新價格 × 1.1, 最小數量 × 子訂單數)  
執行時間（`duration`）| 5 分鐘 – 24 小時  
子訂單間隔（`interval`）| 5 – 120 秒  
子訂單數量| ≤ 交易所單筆最大下單量的 50%（永續/交割）  
隨機數量波動| 若啟用 `isRandom`，波動範圍 ±20%  
  
* * *

### 追蹤委託（Chase Limit Order）

持續在最優買一/賣一價格掛出並調整限價單，跟蹤市場行情直至訂單完全成交、取消或達到最大追蹤距離。

**執行邏輯：** 訂單價格每秒更新一次。所有追蹤委託默認為 **Post Only** （僅掛單成交）。若連續 5 次被 Post Only 條件拒絕，策略將取消。

請參閱 [追蹤委託](https://www.bybit.com/en/help-center/article/Chase-Order?category=5f2fb74e9c8b771130) 了解更多細節。

* * *

### 冰山委託（Iceberg Order）

將大額訂單拆分為多個較小子訂單並依序掛出，每次僅向市場展示一小部分訂單量。

**執行邏輯：** 每筆子訂單進入訂單簿 → 成交後自動掛出下一筆子訂單 → 重複直至全部數量成交。

請參閱 [冰山委託](https://www.bybit.com/en/help-center/article/Iceberg-Order?category=5f2fb74e9c8b771130) 了解更多細節。

**訂單偏好：**

偏好| 執行行為  
---|---  
`追逐限價單 (Taker)`| 買入掛賣一價 / 賣出掛買一價；優先速度  
`追逐限價單`| 買入掛買一價 / 賣出掛賣一價；掛單成交  
`追逐限價單 (跟價差)`| 與賣一/買一保持固定距離；兼顧速度與成本  
`固定價格`| 所有子訂單以固定單一價格掛出  
  
* * *

### POV 委託（Percentage of Volume）

以固定比例參與市場成交量，依據觀測到的市場交易活動或盤口深度動態計算每筆子訂單量，有效降低市場衝擊。

**執行邏輯：** 每隔 `interval` 秒，策略依照所選模式對市場活動進行取樣 → 依據 `participationRate` 計算子訂單數量 → 下單 → 重複直至達到 `maxQty`（`size`）或 `maxDuration`（`duration`）到期為止。將 `interval` 設為 `0` 時，策略僅執行一次即終止（OneTime 模式）。

**注意：** POV 僅支援永續合約（`UTA_USDT`、`UTA_USDC`、`UTA_INVERSE`、`UTA_INVERSE_FUTURE`、`UTA_USDT_FUTURE`），不支援現貨。`interval` > `0` 時，`size` 與 `duration` 至少須填寫一項。

**執行模式（`povParams.mode`）：**

模式| 訂單類型| 成交量參考依據  
---|---|---  
`TradedVolume`| 市價單| `referenceWindow` 秒內的歷史成交量，範圍：[60, 14400]  
`OppositeSideLiquidity`| 以最優買一／賣一價掛吃單限價單| 對手方盤口深度；`depthReference` Top-N 檔，範圍：[1, 10]  
`SameSideLiquidity`| 以最優買一／賣一價掛 Post-Only 限價單| 同側盤口深度；`depthReference` Top-N 檔，範圍：[1, 10]；僅掛單成交  
  
* * *

### HTTP 請求

POST`/v5/strategy/create`

### 請求參數

  * TWAP
  * 追逐限價單
  * 冰山委託
  * POV



參數| 是否必需| 類型| 說明  
---|---|---|---  
category| **true**|  string| 產品類型。`UTA_USDT`（USDT 永續）、`UTA_USDC`（USDC 永續）、`UTA_SPOT`（現貨）、`UTA_INVERSE`（反向永續）、`UTA_INVERSE_FUTURE`（反向交割）、`UTA_USDT_FUTURE`（USDT 交割）  
symbol| **true**|  string| 交易對名稱，例如 `BTCUSDT`  
side| **true**|  string| `Buy`、`Sell`  
size| false| string| 總下單數量，"size" 和 "positionValue" **二選一**  
positionValue| false| string| 總下單價值，"size" 和 "positionValue" **二選一**  
strategyType| **true**|  string| 策略類型。`twap`  
duration| **true**|  integer| 總執行時間（秒）。範圍：[300, 86400]，必須能被 `interval` 整除  
reduceOnly| false| boolean| 是否為只減倉訂單，減倉時需設為 `true`。`true`、`false`  
positionIdx| false| integer| 持倉方向索引。`0`：單向持倉，`1`：雙向持倉多頭，`2`：雙向持倉空頭。雙向持倉模式下**必填**  
leverageType| false| integer| 現貨槓桿類型。`0`：普通，`1`：槓桿交易（僅 `UTA_SPOT`）  
interval| false| integer| 子訂單掛出間隔（秒）。`5`、`10`、`15`、`30`（默認）、`60`、`120`  
isRandom| false| boolean| 隨機訂單: 是否對每筆子訂單數量進行 ±20% 隨機化  
triggerPrice| false| string| 高級設置（觸發價格）: 市場價格達到此值時策略啟動  
maxChasePrice| false| string| 高級設置（停止價格）: 達到此值時策略終止  
chaseDistance| false| string| 高級設置 - 訂單類型設置為限價（默認市價）: 與最優買一/賣一的價格距離（絕對值），例如 `"0.5"`。與 `chasePercentE4` 互斥；若兩者均設置，`chaseDistance` 優先  
chasePercentE4| false| integer| 高級設置 - 訂單類型設置為限價（默認市價）: 與最優買一/賣一的價格偏移（基點，1/10000），例如 `100` = 1%。與 `chaseDistance` 互斥  
  
參數| 是否必需| 類型| 說明  
---|---|---|---  
category| **true**|  string| 產品類型。`UTA_USDT`（USDT 永續）、`UTA_USDC`（USDC 永續）、`UTA_SPOT`（現貨）、`UTA_INVERSE`（反向永續）、`UTA_INVERSE_FUTURE`（反向交割）、`UTA_USDT_FUTURE`（USDT 交割）  
symbol| **true**|  string| 交易對名稱，例如 `BTCUSDT`  
side| **true**|  string| `Buy`、`Sell`  
size| false| string| 總下單數量，"size" 和 "positionValue" **二選一**  
positionValue| false| string| 總下單價值，"size" 和 "positionValue" **二選一**  
strategyType| **true**|  string| 策略類型。`chaseOrder`  
reduceOnly| false| boolean| 是否為只減倉訂單，減倉時需設為 `true`。`true`、`false`  
positionIdx| false| integer| 持倉方向索引。`0`：單向持倉，`1`：雙向持倉多頭，`2`：雙向持倉空頭。雙向持倉模式下**必填**  
chaseDistance| false| string| 追逐價格方式（默認追逐買一賣一價）：與最優買一/賣一的價格距離（絕對值），例如 `"0.5"`。與 `chasePercentE4` 互斥；若兩者均設置，`chaseDistance` 優先  
chasePercentE4| false| integer| 追逐價格方式（默認追逐買一賣一價）：與最優買一/賣一的價格偏移（基點，1/10000），例如 `100` = 1%, 範圍: [0, 500]。與 `chaseDistance` 互斥  
leverageType| false| integer| 現貨槓桿類型。`0`：普通，`1`：槓桿交易（僅 `UTA_SPOT`）  
triggerPrice| false| string| 高級設置（觸發價格）。市場價格達到此值時策略啟動  
maxChasePrice| false| string| 高級設置（最大追逐價格） - 最新成交價達到此值時停止追蹤  
  
參數| 是否必需| 類型| 說明  
---|---|---|---  
category| **true**|  string| 產品類型。`UTA_USDT`（USDT 永續）、`UTA_USDC`（USDC 永續）、`UTA_SPOT`（現貨）、`UTA_INVERSE`（反向永續）、`UTA_INVERSE_FUTURE`（反向交割）、`UTA_USDT_FUTURE`（USDT 交割）  
symbol| **true**|  string| 交易對名稱，例如 `BTCUSDT`  
side| **true**|  string| `Buy`、`Sell`  
size| false| string| 總下單數量，"size" 和 "positionValue" **二選一**  
positionValue| false| string| 總下單價值，"size" 和 "positionValue" **二選一**  
strategyType| **true**|  string| 策略類型。`iceberg`  
reduceOnly| false| boolean| 是否為只減倉訂單，減倉時需設為 `true`。`true`、`false`  
positionIdx| false| integer| 持倉方向索引。`0`：單向持倉，`1`：雙向持倉多頭，`2`：雙向持倉空頭。雙向持倉模式下**必填**  
leverageType| false| integer| 現貨槓桿類型。`0`：普通，`1`：槓桿交易（僅 `UTA_SPOT`）  
subSize| false| string| 每筆子訂單數量。與 `orderCount` 互斥；若兩者均設置，`subSize` 優先  
orderCount| false| integer| 子訂單筆數。與 `subSize`或者`subPositionValue` 互斥  
subPositionValue| false| string| 每筆子訂單價值。與 `orderCount` 互斥；若兩者均設置，`subPositionValue` 優先  
postOnly| false| integer| 掛單模式。`0`：Post Only（僅掛單），`1`：允許吃單  
maxChasePrice| false| string| 作為價格限制參數，買入訂單僅在價格低於或等於此限制時掛出，價格高於此限制時暫停；賣出訂單僅在價格高於或等於此限制時掛出，價格低於此限制時暫停  
limitPrice| false| string| **掛單偏好: 固定價格** ，應用於所有子訂單的固定限價  
chaseDistance| false| string| **掛單偏好: 追逐限價單（跟價差）參數，按價差** , 與最優買一/賣一的價格距離（絕對值），例如 `"0.5"`。與 `chasePercentE4` 互斥；若兩者均設置，`chaseDistance` 優先。  
**掛單偏好: 追逐限價單（Taker）參數**`"-1"` 表示以對手方價格立即成交  
chasePercentE4| false| integer| **掛單偏好: 追逐限價單（跟價差）參數，按比例** , 與最優買一/賣一的價格偏移（基點，1/10000），例如 `100` = 1%，範圍: [0, 100]。與 `chaseDistance` 互斥  
  
參數| 是否必需| 類型| 說明  
---|---|---|---  
category| **true**|  string| 產品類型。`UTA_USDT`（USDT 永續）、`UTA_USDC`（USDC 永續）、`UTA_INVERSE`（反向永續）、`UTA_INVERSE_FUTURE`（反向交割）、`UTA_USDT_FUTURE`（USDT 交割）  
strategyType| **true**|  string| 策略類型。`pov`  
symbol| **true**|  string| 交易對名稱，例如 `BTCUSDT`  
side| **true**|  string| `Buy`、`Sell`  
size| false| string| 總下單數量（幣）。"size" 和 "duration" **二選一**  
duration| false| integer| 總執行時間（秒）。範圍：[900, 86400]。"size" 和 "duration" **二選一**  
interval| false| integer| 子訂單掛出間隔（秒）。`"0"`：單次執行；否則範圍：[5, 3600]  
reduceOnly| false| boolean| 是否為只減倉訂單，減倉時需設為 `true`。`true`、`false`  
positionIdx| false| integer| 持倉方向索引。`0`：單向持倉，`1`：雙向持倉多頭，`2`：雙向持倉空頭。雙向持倉模式下**必填**  
povParams| **true**|  object| 參數物件  
> mode| **true**|  string| 執行模式。`TradedVolume`：根據歷史成交量下市價單；  
`OppositeSideLiquidity`：根據對手方深度在最優買賣價以吃單限價掛出；`SameSideLiquidity`：根據訂單方向在最優買賣價以 Post Only 限價掛出  
> participationRate| **true**|  string| 參與率，範圍：[1, 100]，支援 1 位小數。例如 `"25.1"`=25.1%  
> referenceWindow| false| string| 當 "mode"=`TradedVolume` 時**必填** ，歷史成交量的參考時間窗口（秒），範圍：[60, 14400]  
> depthReference| false| integer| 當 "mode"=`OppositeSideLiquidity` 或 `SameSideLiquidity` 時**必填** ，參考深度檔位，範圍：[1, 10]  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
strategyId| string| 策略 ID（UUID 格式）  
result| string| 執行結果。創建成功時為 `null`  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/strategy/create HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1773711467000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "side": "Buy",  
        "symbol": "BTCUSDT",  
        "reduceOnly": false,  
        "category": "UTA_USDT",  
        "size": "0.1",  
        "positionIdx": 1,  
        "strategyType": "chaseOrder",  
        "chasePrice": "75967.7",  
        "maxChasePrice": "83564.5",  
        "triggerPrice": "75000.0"  
    }  
    
    
    
      
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "strategyId": "119b6211-2611-461b-be5e-5ac557099e82",  
            "result": null  
        },  
        "retExtInfo": {},  
        "time": 1773711467052  
    }