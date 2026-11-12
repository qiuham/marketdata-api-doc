---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/event/trade/cancel-all
api_type: Trading
updated_at: 2026-11-12 18:28:58.111095
---

# Get Event Contract Trade History

Query Event Contract trade (execution) records. Returns records in the past 2 years.

info

  * Only **Event Contract maker accounts** are allowed to access this endpoint.
  * Default query window: **7 days** if `startTime`/`endTime` are not specified.



### HTTP Request

GET`/v5/event/trades`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
symbol| **true**|  string| Symbol name, e.g. `ETHUSDT-28AUG26-2450-2570-OUT`  
orderId| false| string| Order ID filter  
orderLinkId| false| string| User-defined order ID  
startTime| false| integer| Start time in milliseconds. Default: 7 days ago  
endTime| false| integer| End time in milliseconds. Default: now  
limit| false| integer| Number of items per page. Default: `50`, Range: [`1`, `100`]  
cursor| false| string| Pagination cursor  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array| Event Contract trade record list  
> orderId| string| Order ID  
> orderLinkId| string| User-defined order ID  
> execId| string| Execution ID  
> symbol| string| Symbol name  
> baseCoin| string| Base coin  
> settleCoin| string| Settle coin  
> side| string| Side: `Buy` or `Sell`  
> [execType](/docs/v5/enum#exectype)| string| Execution type: `Trade`, `Settle`  
> execPrice| string| Execution price (payout ratio)  
> execValue| string| Execution value  
> execFee| string| Execution fee  
> execFeeRate| string| Execution fee rate  
> orderPrice| string| Order price  
> feeCoin| string| Fee coin  
> transTime| string| Transaction time in milliseconds  
> [timeInForce](/docs/v5/enum#timeinforce)| string| Time in force, e.g. `GTC`, `IOC`, `FOK`  
> crossSeq| string| Cross sequence number  
> ecPayout| string| Event Contract payout (settlement payout for this execution)  
> ecDurationWindow| string| Duration window in seconds  
> settleTimeMs| string| Settlement time in milliseconds  
> ecOrderValue| string| Event Contract order value  
> ecContractType| string| Event contract type: `UpDown`, `Target`, `Range`  
> ecDirection| string| Direction: `UP`/`DOWN` (UpDown type), `ABOVE`/`BELOW` (Target type), `RANGE_IN`/`RANGE_OUT` (Range type)  
> ecTargetPrice| string| Target price. Target type only.  
> ecLowerBound| string| Lower bound. Range type only.  
> ecUpperBound| string| Upper bound. Range type only.  
> extraFees| string| Extra fees (JSON string if applicable)  
cursor| string| Cursor for next page pagination  
  
* * *

### Request Example
    
    
    GET /v5/event/trades?symbol=ETHUSDT-28AUG26-2450-2570-OUT&limit=50 HTTP/1.1  
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
                    "orderId": "1234567890",  
                    "orderLinkId": "my-order-001",  
                    "execId": "exec-001",  
                    "symbol": "ETHUSDT-28AUG26-2450-2570-OUT",  
                    "baseCoin": "BTC",  
                    "settleCoin": "USDT",  
                    "side": "Buy",  
                    "execType": "Trade",  
                    "execPrice": "1.95",  
                    "execValue": "50",  
                    "execFee": "0.5",  
                    "execFeeRate": "0.01",  
                    "orderPrice": "1.95",  
                    "feeCoin": "USDT",  
                    "transTime": "1694402559843",  
                    "timeInForce": "GTC",  
                    "crossSeq": "31413030",  
                    "ecPayout": "0",  
                    "ecDurationWindow": "300",  
                    "settleTimeMs": "1694515498753",  
                    "ecOrderValue": "50",  
                    "ecContractType": "UpDown",  
                    "ecDirection": "UP",  
                    "ecTargetPrice": "",  
                    "ecLowerBound": "",  
                    "ecUpperBound": "",  
                    "extraFees": ""  
                }  
            ],  
            "cursor": ""  
        },  
        "retExtInfo": {},  
        "time": 1694402560000  
    }

---

# 查詢Event Contract成交記錄

查詢 Event Contract 成交（執行）記錄，支持查詢過去 2 年內的數據。

信息

  * 僅 **Event Contract maker 帳戶** 可訪問此接口。
  * 若未指定 `startTime`/`endTime`，默認查詢窗口為 **7 天** 。



### HTTP 請求

GET`/v5/event/trades`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
symbol| **true**|  string| 交易對名稱，如 `ETHUSDT-28AUG26-2450-2570-OUT`  
orderId| 否| string| 訂單 ID 篩選  
orderLinkId| 否| string| 用戶自定義訂單 ID  
startTime| 否| integer| 開始時間（毫秒）。默認：7 天前  
endTime| 否| integer| 結束時間（毫秒）。默認：當前時間  
limit| 否| integer| 每頁數量。默認：`50`，範圍：[`1`, `100`]  
cursor| 否| string| 分頁游標  
  
### 返回參數

參數| 類型| 說明  
---|---|---  
list| array| Event Contract 成交記錄列表  
> orderId| string| 訂單 ID  
> orderLinkId| string| 用戶自定義訂單 ID  
> execId| string| 成交 ID  
> symbol| string| 交易對名稱  
> baseCoin| string| 標的幣種  
> settleCoin| string| 結算幣種  
> side| string| 方向：`Buy` 或 `Sell`  
> [execType](/docs/zh-TW/v5/enum#exectype)| string| 成交類型：`Trade`、`Settle`  
> execPrice| string| 成交價格（賠付比率）  
> execValue| string| 成交金額  
> execFee| string| 成交手續費  
> execFeeRate| string| 成交手續費率  
> orderPrice| string| 訂單價格  
> feeCoin| string| 手續費幣種  
> transTime| string| 成交時間（毫秒）  
> [timeInForce](/docs/zh-TW/v5/enum#timeinforce)| string| 訂單有效期，如 `GTC`、`IOC`、`FOK`  
> crossSeq| string| 跨業務序號  
> ecPayout| string| Event Contract 賠付金額（本次成交的結算賠付）  
> ecDurationWindow| string| 持續時間窗口（秒）  
> settleTimeMs| string| 結算時間（毫秒）  
> ecOrderValue| string| Event Contract 訂單金額  
> ecContractType| string| 事件合約類型：`UpDown`、`Target`、`Range`  
> ecDirection| string| 方向：`UP`/`DOWN`（UpDown 類型），`ABOVE`/`BELOW`（Target 類型），`RANGE_IN`/`RANGE_OUT`（Range 類型）  
> ecTargetPrice| string| 目標價格，僅 Target 類型適用  
> ecLowerBound| string| 下限價格，僅 Range 類型適用  
> ecUpperBound| string| 上限價格，僅 Range 類型適用  
> extraFees| string| 額外費用（適用時為 JSON 字符串）  
cursor| string| 下一頁分頁游標  
  
* * *

### 請求示例
    
    
    GET /v5/event/trades?symbol=ETHUSDT-28AUG26-2450-2570-OUT&limit=50 HTTP/1.1  
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
                    "orderId": "1234567890",  
                    "orderLinkId": "my-order-001",  
                    "execId": "exec-001",  
                    "symbol": "ETHUSDT-28AUG26-2450-2570-OUT",  
                    "baseCoin": "BTC",  
                    "settleCoin": "USDT",  
                    "side": "Buy",  
                    "execType": "Trade",  
                    "execPrice": "1.95",  
                    "execValue": "50",  
                    "execFee": "0.5",  
                    "execFeeRate": "0.01",  
                    "orderPrice": "1.95",  
                    "feeCoin": "USDT",  
                    "transTime": "1694402559843",  
                    "timeInForce": "GTC",  
                    "crossSeq": "31413030",  
                    "ecPayout": "0",  
                    "ecDurationWindow": "300",  
                    "settleTimeMs": "1694515498753",  
                    "ecOrderValue": "50",  
                    "ecContractType": "UpDown",  
                    "ecDirection": "UP",  
                    "ecTargetPrice": "",  
                    "ecLowerBound": "",  
                    "ecUpperBound": "",  
                    "extraFees": ""  
                }  
            ],  
            "cursor": ""  
        },  
        "retExtInfo": {},  
        "time": 1694402560000  
    }