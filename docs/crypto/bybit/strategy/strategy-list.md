---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/strategy/strategy-list
api_type: REST
updated_at: 2026-05-27 19:22:48.252678
---

# Get Strategy List

Query the strategy list. Supports filtering by strategy ID, symbol, status, category, and strategy type.  
You can also subscribe [strategy](/docs/v5/websocket/private/strategy) stream to receive the feed.

### HTTP Request

GET`/v5/strategy/list`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
strategyId| false| string| Strategy ID (exact match)  
symbol| false| string| Symbol name, e.g. `BTCUSDT`  
status| false| string| Strategy status. `2`: running, `3`: terminated, `4`: terminated but orders are not filled, `5`: paused, `6`: untriggered  
category| false| string| Product type. `UTA_USDT`, `UTA_USDC`, `UTA_USDC_FUTURE`, `UTA_SPOT`, `UTA_INVERSE`, `UTA_INVERSE_FUTURE`, `UTA_USDT_FUTURE`  
strategyType| false| string| Strategy type. `twap`, `chaseOrder`, `iceberg`, `pov`  
beginTimeE0| false| int64| Start time in seconds (Unix timestamp)  
endTimeE0| false| int64| End time in seconds (Unix timestamp)  
pageSize| false| integer| Limit for data size per page. Default: `20`, max: `50`  
cursor| false| string| Cursor for pagination, returned from the previous response  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array| Object  
> strategyId| string| Strategy ID (UUID format)  
> category| string| Product type  
> symbol| string| Symbol name  
> side| string| `Buy`, `Sell`  
> size| string| Total order quantity  
> strategyType| string| Strategy type. `twap`, `chaseOrder`, `iceberg`, `pov`  
> status| integer| Strategy status. `2`: running, `3`: terminated, `4`: terminated but orders are not filled, `5`: paused, `6`: untriggered  
> executedSize| string| Executed quantity  
> executedAvgPrice| string| Average executed price  
> executedStartTimeE3| int64| Execution start time (ms)  
> executedEndTimeE3| int64| Execution end time (ms). `0` means not yet ended  
> createdTimeE3| int64| Strategy creation time (ms)  
> updatedTimeE3| int64| Strategy last updated time (ms)  
> reduceOnly| boolean| Whether it is a reduce-only order  
> triggerPrice| string| Trigger price  
> isTriggered| boolean| Whether the strategy has been triggered  
> leverageType| integer| Leverage type. `0`: normal, `1`: margin  
> terminateType| integer| Termination reason code. `0`: unknown, `1`: user stop, `2`: completed normally, `3`: insufficient balance, `4`: position mode changed, `5`: uid blocked, `6`: would trigger liquidation, `7`: no position for reduce-only, `8`: upgrade to UTA, `9`: OI limited, `10`: user trading banned, `11`: risk limit exceeded, `12`: symbol delivery stopped, `13`: symbol delisted, `14`: consecutive order failures, `15`: missing template param, `16`: signal latency, `17`: symbol mismatch, `18`: beyond max chase price, `19`: max sub-order count exceeded, `20`: order already cancelled, `21`: max risk limit value exceeded, `22`: risk limit max leverage exceeded, `23`: coin not collateral, `24`: reached limit price, `25`: reduce-only state with pending UTA upgrade, `26`: user in cooling-off period  
> terminateRemark| string| Termination reason description  
> triggerCount| integer| Number of trigger attempts  
> tradingCount| integer| Number of actual orders placed  
> realizedPnl| string| Realized PnL (futures only)  
> strategyName| string| Strategy custom name  
> strategyPrefer| string| Execution preference. `limit`, `priceSpeedBalance`, `fastestExecution`, `quickExecution`  
> duration| integer| Total planned execution duration in seconds. _TWAP/POV only_  
> executedDuration| integer| Actual executed duration in seconds. _TWAP/POV only_  
> isRandom| boolean| Whether sub-order quantity randomization is enabled. _TWAP only_  
> interval| integer| Sub-order placement interval in seconds. _TWAP/POV only_  
> limitPrice| string| Fixed limit price. Orders will not be placed beyond this price  
> chasePercentE4| int64| Chase price offset in basis points (1/10000). _Chase / Iceberg_  
> chaseDistance| string| Chase price distance (absolute value). _Chase / Iceberg_  
> maxChasePrice| string| Maximum chase price protection. _Chase / Iceberg_  
> chaseOrderPrice| string| Current chase order price (real-time). _Chase only_  
> chasePrice| string| Reference price side for chase orders, e.g. `Bid1`, `Ask1`. _Chase / Iceberg_  
> postOnly| integer| Maker-only mode. `0`: taker allowed, `1`: post-only. _Iceberg only_  
> isRebalance| boolean| Whether rebalance is enabled  
> orderType| integer| Order type. `1`: market order, `2`: limit order  
> orderPriceOffset| string| Limit order price offset percentage. _TWAP only_  
> strategySl| string| Strategy stop-loss price  
> strategyTp| string| Strategy take-profit price  
> arbitrageOrders| array| List of associated arbitrage orders  
> positionValue| string| Total position value  
> filledPositionValue| string| Filled position value  
> mode| string| Execution modes, `TradeVolume` `OppositeSideLiquidity` `SameSideLiquidity`, _POV only_  
> participationRate| string| Participation rate, _POV only_  
> referenceWindow| string| Reference window for historical trading volume, _POV only_  
> depthReference| string| Reference depths, _POV only_  
nextCursor| string| Cursor for the next page. Empty string means no more data  
prevCursor| string| Cursor for the previous page  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/strategy/list?strategyId=119b6211-2611-461b-be5e-5ac557099e82 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1773718018000  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
      
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "list": [  
                {  
                    "strategyId": "119b6211-2611-461b-be5e-5ac557099e82",  
                    "category": "UTA_USDT",  
                    "symbol": "BTCUSDT",  
                    "side": "Buy",  
                    "size": "0.05",  
                    "duration": 1560,  
                    "status": 3,  
                    "executedDuration": 1608,  
                    "executedSize": "0.046",  
                    "executedAvgPrice": "76695.48",  
                    "executedStartTimeE3": "1773711467045",  
                    "executedEndTimeE3": "1773713075628",  
                    "createdTimeE3": "1773711467045",  
                    "updatedTimeE3": "1773713075628",  
                    "isRandom": false,  
                    "limitPrice": "",  
                    "reduceOnly": false,  
                    "terminateType": 2,  
                    "terminateRemark": "RunningStop",  
                    "strategyName": "",  
                    "triggerCount": "26",  
                    "tradingCount": "0",  
                    "realizedPnl": "0",  
                    "strategyType": "twap",  
                    "chasePrice": "Bid1",  
                    "chasePercentE4": "0",  
                    "chaseDistance": "0",  
                    "maxChasePrice": "",  
                    "chaseOrderPrice": "",  
                    "arbitrageOrders": [],  
                    "strategyPrefer": "quickExecution",  
                    "isRebalance": false,  
                    "interval": 60,  
                    "leverageType": 0,  
                    "postOnly": 0,  
                    "triggerPrice": "0",  
                    "isTriggered": false,  
                    "strategyTp": "",  
                    "strategySl": "",  
                    "orderType": "UNKNOWN",  
                    "orderPriceOffset": "",  
                    "positionValue": "",  
                    "filledPositionValue": ""  
                }  
            ],  
            "nextCursor": "",  
            "prevCursor": ""  
        },  
        "retExtInfo": {},  
        "time": 1774583153599  
    }

---

# 查詢策略列表

查詢策略列表。支援依策略 ID、交易對、狀態、產品類型及策略類型進行篩選。您也可以通過訂閱[strategy](/docs/zh-TW/v5/websocket/private/strategy)流獲得實時更新

### HTTP 請求

GET`/v5/strategy/list`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
strategyId| false| string| 策略 ID（精確匹配）  
symbol| false| string| 交易對名稱，例如 `BTCUSDT`  
status| false| string| 策略狀態。`2`：執行中，`3`：已終止，`4`：已終止但訂單還未成交, `5`：已暫停，`6`：待觸發  
category| false| string| 產品類型。`UTA_USDT`、`UTA_USDC`、`UTA_USDC_FUTURE`、`UTA_SPOT`、`UTA_INVERSE`、`UTA_INVERSE_FUTURE`、`UTA_USDT_FUTURE`  
strategyType| false| string| 策略類型。`twap`、`chaseOrder`、`iceberg`、`pov`  
beginTimeE0| false| int64| 起始時間（Unix 時間戳，秒）  
endTimeE0| false| int64| 結束時間（Unix 時間戳，秒）  
pageSize| false| integer| 每頁資料筆數。默認：`20`，最大：`50`  
cursor| false| string| 分頁游標，從上一次響應中返回  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
list| array| 物件  
> strategyId| string| 策略 ID（UUID 格式）  
> category| string| 產品類型  
> symbol| string| 交易對名稱  
> side| string| `Buy`、`Sell`  
> size| string| 總下單數量  
> strategyType| string| 策略類型。`twap`、`chaseOrder`、`iceberg`、`pov`  
> status| integer| 策略狀態。`2`：執行中，`3`：已終止，`4`：已終止但訂單還未成交，`5`：已暫停，`6`：待觸發  
> executedSize| string| 已成交數量  
> executedAvgPrice| string| 平均成交價格  
> executedStartTimeE3| int64| 執行開始時間（毫秒）  
> executedEndTimeE3| int64| 執行結束時間（毫秒）。`0` 表示尚未結束  
> createdTimeE3| int64| 策略創建時間（毫秒）  
> updatedTimeE3| int64| 策略最後更新時間（毫秒）  
> reduceOnly| boolean| 是否為只減倉訂單  
> triggerPrice| string| 觸發價格  
> isTriggered| boolean| 策略是否已被觸發  
> leverageType| integer| 槓桿類型。`0`：普通，`1`：借貸  
> terminateType| integer| 終止原因代碼。`0`：未知，`1`：使用者停止，`2`：正常完成，`3`：餘額不足，`4`：持倉模式變更，`5`：UID 被封禁，`6`：觸發強平，`7`：只減倉但無持倉，`8`：升級至 UTA，`9`：OI 超限，`10`：用戶交易被禁，`11`：超過風險限額，`12`：交易對交割停止，`13`：交易對下架，`14`：連續下單失敗，`15`：缺少模板參數，`16`：信號延遲，`17`：交易對不匹配，`18`：超出最大追蹤價格，`19`：子訂單數量超限，`20`：訂單已取消，`21`：超出最大風險限額，`22`：風險限額最大槓桿超限，`23`：幣種非抵押品，`24`：達到限價，`25`：只減倉狀態下有待處理的 UTA 升級，`26`：用戶處於冷靜期  
> terminateRemark| string| 終止原因說明  
> triggerCount| integer| 觸發嘗試次數  
> tradingCount| integer| 實際下單筆數  
> realizedPnl| string| 已實現盈虧（僅合約）  
> strategyName| string| 策略自訂名稱  
> strategyPrefer| string| 執行偏好。`limit`、`priceSpeedBalance`、`fastestExecution`、`quickExecution`  
> duration| integer| 計劃總執行時間（秒）。 _僅 TWAP/POV_  
> executedDuration| integer| 實際已執行時間（秒）。 _僅 TWAP/POV_  
> isRandom| boolean| 是否啟用子訂單數量隨機化。 _僅 TWAP_  
> interval| integer| 子訂單掛出間隔（秒）。 _僅 TWAP/POV_  
> limitPrice| string| 固定限價。訂單不會在此價格以外掛出  
> chasePercentE4| int64| 追蹤價格偏移（基點，1/10000）。 _Chase / Iceberg_  
> chaseDistance| string| 追蹤價格距離（絕對值）。 _Chase / Iceberg_  
> maxChasePrice| string| 最大追蹤價格保護。 _Chase / Iceberg_  
> chaseOrderPrice| string| 當前追蹤委託價格（實時）。 _僅 Chase_  
> chasePrice| string| 追蹤委託的參考價格方向，例如 `Bid1`、`Ask1`。 _Chase / Iceberg_  
> postOnly| integer| 掛單模式。`0`：允許吃單，`1`：僅掛單。 _僅 Iceberg_  
> isRebalance| boolean| 是否啟用再平衡  
> orderType| integer| 訂單類型。`1`：市價單，`2`：限價單  
> orderPriceOffset| string| 限價單價格偏移百分比。 _僅 TWAP_  
> strategySl| string| 策略止損價格  
> strategyTp| string| 策略止盈價格  
> arbitrageOrders| array| 關聯套利訂單列表  
> positionValue| string| 總持倉價值  
> filledPositionValue| string| 已成交持倉價值  
> mode| string| 執行模式, `TradeVolume` `OppositeSideLiquidity` `SameSideLiquidity`, _僅 POV_  
> participationRate| string| 參與率, _僅 POV_  
> referenceWindow| string| 歷史成交量的參考窗口, _僅 POV_  
> depthReference| string| 參考深度, _僅 POV_  
nextCursor| string| 下一頁游標。空字串表示無更多資料  
prevCursor| string| 上一頁游標  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/strategy/list?strategyId=119b6211-2611-461b-be5e-5ac557099e82 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1773718018000  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
      
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "list": [  
                {  
                    "strategyId": "119b6211-2611-461b-be5e-5ac557099e82",  
                    "category": "UTA_USDT",  
                    "symbol": "BTCUSDT",  
                    "side": "Buy",  
                    "size": "0.05",  
                    "duration": 1560,  
                    "status": 3,  
                    "executedDuration": 1608,  
                    "executedSize": "0.046",  
                    "executedAvgPrice": "76695.48",  
                    "executedStartTimeE3": "1773711467045",  
                    "executedEndTimeE3": "1773713075628",  
                    "createdTimeE3": "1773711467045",  
                    "updatedTimeE3": "1773713075628",  
                    "isRandom": false,  
                    "limitPrice": "",  
                    "reduceOnly": false,  
                    "terminateType": 2,  
                    "terminateRemark": "RunningStop",  
                    "strategyName": "",  
                    "triggerCount": "26",  
                    "tradingCount": "0",  
                    "realizedPnl": "0",  
                    "strategyType": "twap",  
                    "chasePrice": "Bid1",  
                    "chasePercentE4": "0",  
                    "chaseDistance": "0",  
                    "maxChasePrice": "",  
                    "chaseOrderPrice": "",  
                    "arbitrageOrders": [],  
                    "strategyPrefer": "quickExecution",  
                    "isRebalance": false,  
                    "interval": 60,  
                    "leverageType": 0,  
                    "postOnly": 0,  
                    "triggerPrice": "0",  
                    "isTriggered": false,  
                    "strategyTp": "",  
                    "strategySl": "",  
                    "orderType": "UNKNOWN",  
                    "orderPriceOffset": "",  
                    "positionValue": "",  
                    "filledPositionValue": ""  
                }  
            ],  
            "nextCursor": "",  
            "prevCursor": ""  
        },  
        "retExtInfo": {},  
        "time": 1774583153599  
    }