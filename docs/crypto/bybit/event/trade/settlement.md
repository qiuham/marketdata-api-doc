---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/event/trade/settlement
api_type: Trading
updated_at: 2026-11-13 19:22:36.086070
---

# Get Event Contract Settlement Records

Query Event Contract settlement records. Returns records in the past 2 years.

info

  * Only **Event Contract maker accounts** are allowed to access this endpoint.
  * Default query window: **7 days** if `startTime`/`endTime` are not specified.



### HTTP Request

GET`/v5/event/settlements`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
symbol| **true**|  string| Symbol name, e.g. `ETHUSDT-28AUG26-2450-2570-OUT`  
orderId| false| string| Order ID filter  
startTime| false| integer| Start time in milliseconds. Default: 7 days ago  
endTime| false| integer| End time in milliseconds. Default: now  
limit| false| integer| Number of items per page. Default: `50`, Range: [`1`, `100`]  
cursor| false| string| Pagination cursor  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array| Event Contract settlement record list  
> transId| string| Transaction ID  
> symbol| string| Symbol name  
> symbolId| string| Symbol ID  
> baseCoin| string| Base coin  
> settleCoin| string| Settle coin  
> side| string| Side: `Buy` or `Sell`  
> ecContractType| string| Event contract type: `UpDown`, `Target`, `Range`  
> ecDirection| string| Direction: `UP`/`DOWN` (UpDown type), `ABOVE`/`BELOW` (Target type), `RANGE_IN`/`RANGE_OUT` (Range type)  
> settlePrice| string| Settlement price  
> entryPrice| string| Entry price  
> grossPayoutRatio| string| Gross payout ratio  
> ecDurationWindow| string| Duration window in seconds  
> ecTargetPrice| string| Target price. Target type only.  
> ecLowerBound| string| Lower bound. Range type only.  
> ecUpperBound| string| Upper bound. Range type only.  
> transTime| string| Transaction time in milliseconds  
> crossSeq| string| Cross sequence number  
> execFee| string| Execution fee  
> execFeeRate| string| Execution fee rate  
> payout| string| Settlement payout amount  
> sessionRpl| string| Session realised PnL  
> orderId| string| Related order ID  
cursor| string| Cursor for next page pagination  
  
* * *

### Request Example
    
    
    GET /v5/event/settlements?symbol=ETHUSDT-28AUG26-2450-2570-OUT&limit=50 HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1694402559000  
    X-BAPI-RECV-WINDOW: 5000  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "list": [  
                {  
                    "transId": "tx-001",  
                    "symbol": "ETHUSDT-28AUG26-2450-2570-OUT",  
                    "symbolId": "100001",  
                    "baseCoin": "BTC",  
                    "settleCoin": "USDT",  
                    "side": "Buy",  
                    "ecContractType": "UpDown",  
                    "ecDirection": "UP",  
                    "settlePrice": "26500",  
                    "entryPrice": "26000.5",  
                    "grossPayoutRatio": "1.85",  
                    "ecDurationWindow": "300",  
                    "ecTargetPrice": "",  
                    "ecLowerBound": "",  
                    "ecUpperBound": "",  
                    "transTime": "1694515498753",  
                    "crossSeq": "31413030",  
                    "execFee": "0.5",  
                    "execFeeRate": "0.01",  
                    "payout": "92.5",  
                    "sessionRpl": "42.5",  
                    "orderId": "1234567890"  
                }  
            ],  
            "cursor": ""  
        },  
        "retExtInfo": {},  
        "time": 1694402560000  
    }

---

# 查詢Event Contract結算記錄

查詢 Event Contract 結算記錄，支持查詢過去 2 年內的數據。

信息

  * 僅 **Event Contract maker 帳戶** 可訪問此接口。
  * 若未指定 `startTime`/`endTime`，默認查詢窗口為 **7 天** 。



### HTTP 請求

GET`/v5/event/settlements`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
symbol| **true**|  string| 交易對名稱，如 `ETHUSDT-28AUG26-2450-2570-OUT`  
orderId| 否| string| 訂單 ID 篩選  
startTime| 否| integer| 開始時間（毫秒）。默認：7 天前  
endTime| 否| integer| 結束時間（毫秒）。默認：當前時間  
limit| 否| integer| 每頁數量。默認：`50`，範圍：[`1`, `100`]  
cursor| 否| string| 分頁游標  
  
### 返回參數

參數| 類型| 說明  
---|---|---  
list| array| Event Contract 結算記錄列表  
> transId| string| 交易 ID  
> symbol| string| 交易對名稱  
> symbolId| string| 交易對 ID  
> baseCoin| string| 標的幣種  
> settleCoin| string| 結算幣種  
> side| string| 方向：`Buy` 或 `Sell`  
> ecContractType| string| 事件合約類型：`UpDown`、`Target`、`Range`  
> ecDirection| string| 方向：`UP`/`DOWN`（UpDown 類型），`ABOVE`/`BELOW`（Target 類型），`RANGE_IN`/`RANGE_OUT`（Range 類型）  
> settlePrice| string| 結算價格  
> entryPrice| string| 入場價格  
> grossPayoutRatio| string| 毛賠付比率  
> ecDurationWindow| string| 持續時間窗口（秒）  
> ecTargetPrice| string| 目標價格，僅 Target 類型適用  
> ecLowerBound| string| 下限價格，僅 Range 類型適用  
> ecUpperBound| string| 上限價格，僅 Range 類型適用  
> transTime| string| 結算時間（毫秒）  
> crossSeq| string| 跨業務序號  
> execFee| string| 執行手續費  
> execFeeRate| string| 執行手續費率  
> payout| string| 結算賠付金額  
> sessionRpl| string| 本次持倉已結盈虧  
> orderId| string| 關聯訂單 ID  
cursor| string| 下一頁分頁游標  
  
* * *

### 請求示例
    
    
    GET /v5/event/settlements?symbol=ETHUSDT-28AUG26-2450-2570-OUT&limit=50 HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1694402559000  
    X-BAPI-RECV-WINDOW: 5000  
    

### 返回示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "list": [  
                {  
                    "transId": "tx-001",  
                    "symbol": "ETHUSDT-28AUG26-2450-2570-OUT",  
                    "symbolId": "100001",  
                    "baseCoin": "BTC",  
                    "settleCoin": "USDT",  
                    "side": "Buy",  
                    "ecContractType": "UpDown",  
                    "ecDirection": "UP",  
                    "settlePrice": "26500",  
                    "entryPrice": "26000.5",  
                    "grossPayoutRatio": "1.85",  
                    "ecDurationWindow": "300",  
                    "ecTargetPrice": "",  
                    "ecLowerBound": "",  
                    "ecUpperBound": "",  
                    "transTime": "1694515498753",  
                    "crossSeq": "31413030",  
                    "execFee": "0.5",  
                    "execFeeRate": "0.01",  
                    "payout": "92.5",  
                    "sessionRpl": "42.5",  
                    "orderId": "1234567890"  
                }  
            ],  
            "cursor": ""  
        },  
        "retExtInfo": {},  
        "time": 1694402560000  
    }