---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/websocket/private/position
api_type: WebSocket
updated_at: 2026-10-06 18:55:25.217771
---

# Strategy

Subscribe to the strategy stream to get the strategy (twap / iceberg / ChaseOrder) feeds.

**Topic:** `strategy`  


### Response Parameters

Parameter| Type| Comments  
---|---|---  
id| string| Message ID  
topic| string| Topic name  
creationTime| number| Data created timestamp (ms)  
data| array| Object  
> strategyId| string| Strategy ID  
> strategyType| string| Strategy type. `twap`, `chaseOrder`, `iceberg`, `pov`  
> category| string| Product type. `UTA_USDT`, `UTA_USDC`, `UTA_USDC_FUTURE`, `UTA_SPOT`, `UTA_INVERSE`, `UTA_INVERSE_FUTURE`, `UTA_USDT_FUTURE`  
> symbol| string| Symbol name  
> size| string| Total strategy quantity  
> side| string| `Buy`, `Sell`  
> duration| integer| Execution duration in seconds. TWAP strategy only  
> status| integer| Strategy status. `2`: running, `3`: terminated, `4`: terminated but orders are not filled, `5`: paused, `6`: not yet triggered  
> terminateType| integer| Termination type. `0`: not terminated, `1`: user stopped, `2`: completed normally, `3`: insufficient balance. Refer to terminateType enum  
> terminateRemark| string| Termination reason description  
> executedDuration| integer| Elapsed execution duration  
> executedSize| string| Executed quantity  
> executedAvgPrice| string| Average execution price  
> executedStartTimeE3| integer| Execution start time (ms)  
> executedEndTimeE3| integer| Execution end time (ms). `0` means not yet ended  
> createdTimeE3| integer| Strategy creation time (ms)  
> updatedTimeE3| integer| Strategy last updated time (ms)  
> isRandom| boolean| Whether to randomize order quantity. TWAP strategy only  
> reduceOnly| boolean| Reduce-only  
> limitPrice| string| Fixed limit price  
> triggerCount| integer| Trigger count (number of times strategy executed)  
> tradingCount| integer| Trading count (number of orders placed)  
> chaseDistance| string| Chase distance (absolute value). Chase / Iceberg strategy  
> ChasePercentE4| integer| Chase percentage in basis points. e.g. `100` = 1%. Chase / Iceberg strategy  
> maxChasePrice| string| Max chase price protection. Chase / Iceberg strategy  
> chaseOrderPrice| string| Current chase order price. Chase strategy only  
> strategyPrefer| string| Strategy preference. `limit`: fixed price, `priceSpeedBalance`: balanced, `fastestExecution`: fastest execution, `quickExecution`: quick execution  
> interval| integer| Order interval in seconds. TWAP strategy only  
> leverageType| integer| Leverage type. `0`: normal, `1`: margin (spot only)  
> postOnly| integer| Post-only. `0`: non-post-only, `1`: post-only. Iceberg strategy only  
> triggerPrice| string| Trigger price. Strategy starts executing when this price is reached  
> isTriggered| boolean| Whether the strategy has been triggered  
> strategyTp| string| Strategy take-profit price  
> strategySl| string| Strategy stop-loss price  
> orderType| string| Order type. `1`: market order, `2`: limit order  
> orderPriceOffset| string| Limit order price offset percentage  
> positionValue| string| Total strategy value. Returned for value-based orders, otherwise empty string  
> filledPositionValue| string| Filled position value  
  
### Subscribe Example
    
    
    {  
        "op": "subscribe",  
        "args": [  
            "strategy"  
        ]  
    }  
    
    
    
      
    

### Stream Example
    
    
    {  
        "id": "62f79ebea4794f767cad0bd937f7ad01",  
        "topic": "strategy",  
        "creationTime": 1776734985598,  
        "data": [  
            {  
                "strategyId": "cf7303ae-29c0-480a-8f3d-eaa9330054bc",  
                "strategyType": "iceberg",  
                "category": "UTA_USDT",  
                "symbol": "BTCUSDT",  
                "size": "0.36",  
                "side": "Buy",  
                "duration": 0,  
                "status": 3,  
                "terminateType": 2,  
                "terminateRemark": "RunningStop",  
                "executedDuration": 268,  
                "executedSize": "0.36",  
                "executedAvgPrice": "134301.53",  
                "executedStartTimeE3": 1776734716717,  
                "executedEndTimeE3": 1776734985592,  
                "createdTimeE3": 1776734716717,  
                "updatedTimeE3": 1776734985592,  
                "isRandom": false,  
                "reduceOnly": false,  
                "limitPrice": "",  
                "triggerCount": 0,  
                "tradingCount": 0,  
                "chaseDistance": "0",  
                "ChasePercentE4": 0,  
                "maxChasePrice": "198000",  
                "chaseOrderPrice": "135682.4",  
                "strategyPrefer": "quickExecution",  
                "interval": 30,  
                "leverageType": 0,  
                "postOnly": 0,  
                "triggerPrice": "",  
                "isTriggered": false,  
                "strategyTp": "",  
                "strategySl": "",  
                "orderType": "UNKNOWN",  
                "orderPriceOffset": "",  
                "positionValue": "",  
                "filledPositionValue": ""  
            }  
        ]  
    }

---

# 策略

訂閱策略推送，以獲取策略（TWAP / Iceberg / ChaseOrder）的即時數據更新。

**Topic:** `strategy`  


### 響應參數

參數| 類型| 說明  
---|---|---  
id| string| 消息id  
topic| string| Topic名  
creationTime| number| 消息數據創建時間  
data| array| 物件  
> strategyId| string| 策略 ID  
> strategyType| string| 策略類型。`twap`、`chaseOrder`、`iceberg`、`pov`  
> category| string| 產品類型。`UTA_USDT`、`UTA_USDC`、`UTA_USDC_FUTURE`、`UTA_SPOT`、`UTA_INVERSE`、`UTA_INVERSE_FUTURE`、`UTA_USDT_FUTURE`  
> symbol| string| 交易對名稱  
> size| string| 總下單數量  
> side| string| `Buy`、`Sell`  
> duration| integer| 計劃總執行時間（秒）。 _僅 TWAP_  
> status| integer| 策略狀態。`2`：執行中，`3`：已終止，`4`：已終止但訂單還未成交，`5`：已暫停，`6`：待觸發  
> terminateType| integer| 終止原因代碼。`0`：未知，`1`：使用者停止，`2`：正常完成，`3`：餘額不足。詳見 terminateType 枚舉  
> terminateRemark| string| 終止原因說明  
> executedDuration| integer| 實際已執行時間（秒）  
> executedSize| string| 已成交數量  
> executedAvgPrice| string| 平均成交價格  
> executedStartTimeE3| integer| 執行開始時間（毫秒）  
> executedEndTimeE3| integer| 執行結束時間（毫秒）。`0` 表示尚未結束  
> createdTimeE3| integer| 策略創建時間（毫秒）  
> updatedTimeE3| integer| 策略最後更新時間（毫秒）  
> isRandom| boolean| 是否啟用子訂單數量隨機化。 _僅 TWAP_  
> reduceOnly| boolean| 是否為只減倉訂單  
> limitPrice| string| 固定限價。訂單不會在此價格以外掛出  
> triggerCount| integer| 觸發嘗試次數  
> tradingCount| integer| 實際下單筆數  
> chaseDistance| string| 追蹤價格距離（絕對值）。 _Chase / Iceberg_  
> ChasePercentE4| integer| 追蹤價格偏移（基點，1/10000）。例如 `100` = 1%。 _Chase / Iceberg_  
> maxChasePrice| string| 最大追蹤價格保護。 _Chase / Iceberg_  
> chaseOrderPrice| string| 當前追蹤委託價格（實時）。 _僅 Chase_  
> strategyPrefer| string| 執行偏好。`limit`：固定價格，`priceSpeedBalance`：均衡，`fastestExecution`：最快成交，`quickExecution`：快速成交  
> interval| integer| 子訂單掛出間隔（秒）。 _僅 TWAP_  
> leverageType| integer| 槓桿類型。`0`：普通，`1`：借貸（僅現貨）  
> postOnly| integer| 掛單模式。`0`：允許吃單，`1`：僅掛單。 _僅 Iceberg_  
> triggerPrice| string| 觸發價格。達到此價格後策略開始執行  
> isTriggered| boolean| 策略是否已被觸發  
> strategyTp| string| 策略止盈價格  
> strategySl| string| 策略止損價格  
> orderType| string| 訂單類型。`1`：市價單，`2`：限價單  
> orderPriceOffset| string| 限價單價格偏移百分比  
> positionValue| string| 策略總價值。按價值下單時返回，否則為空字串  
> filledPositionValue| string| 已成交持倉價值  
  
### 訂閱示例
    
    
    {  
        "op": "subscribe",  
        "args": [  
            "strategy"  
        ]  
    }  
    
    
    
      
    

### 推送示例
    
    
    {  
        "id": "62f79ebea4794f767cad0bd937f7ad01",  
        "topic": "strategy",  
        "creationTime": 1776734985598,  
        "data": [  
            {  
                "strategyId": "cf7303ae-29c0-480a-8f3d-eaa9330054bc",  
                "strategyType": "iceberg",  
                "category": "UTA_USDT",  
                "symbol": "BTCUSDT",  
                "size": "0.36",  
                "side": "Buy",  
                "duration": 0,  
                "status": 3,  
                "terminateType": 2,  
                "terminateRemark": "RunningStop",  
                "executedDuration": 268,  
                "executedSize": "0.36",  
                "executedAvgPrice": "134301.53",  
                "executedStartTimeE3": 1776734716717,  
                "executedEndTimeE3": 1776734985592,  
                "createdTimeE3": 1776734716717,  
                "updatedTimeE3": 1776734985592,  
                "isRandom": false,  
                "reduceOnly": false,  
                "limitPrice": "",  
                "triggerCount": 0,  
                "tradingCount": 0,  
                "chaseDistance": "0",  
                "ChasePercentE4": 0,  
                "maxChasePrice": "198000",  
                "chaseOrderPrice": "135682.4",  
                "strategyPrefer": "quickExecution",  
                "interval": 30,  
                "leverageType": 0,  
                "postOnly": 0,  
                "triggerPrice": "",  
                "isTriggered": false,  
                "strategyTp": "",  
                "strategySl": "",  
                "orderType": "UNKNOWN",  
                "orderPriceOffset": "",  
                "positionValue": "",  
                "filledPositionValue": ""  
            }  
        ]  
    }