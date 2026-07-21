---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/websocket/public/trade
api_type: WebSocket
updated_at: 2026-07-21 19:02:35.048676
---

# System Status

Listen to the system status when there is a platform maintenance or service incident.

info

Please note currently system maintenance that may result in short interruption (lasting less than 10 seconds) or websocket disconnection (users can immediately reconnect) will not be announced.

## URL

  * **Mainnet:**  
`wss://stream.bybit.com/v5/public/misc/status`



info

  * EU users registered from "[www.bybit.eu"](http://www.bybit.eu%22), please use `wss://stream.bybit.eu/v5/public/misc/status`



**Topic:**  
`system.status`

### Response Parameters

Parameter| Type| Comments  
---|---|---  
topic| string| Topic name  
ts| number| The timestamp (ms) that the system generates the data  
data| array| Object  
> id| string| Id. Unique identifier  
> title| string| Title of system maintenance  
> [state](/docs/v5/enum#state)| string| System state  
> begin| string| Start time of system maintenance, timestamp in milliseconds  
> end| string| End time of system maintenance, timestamp in milliseconds. Before maintenance is completed, it is the expected end time; After maintenance is completed, it will be changed to the actual end time.  
> href| string| Hyperlink to system maintenance details. Default value is empty string  
> [serviceTypes](/docs/v5/enum#servicetypes)| array<int>| Service Type  
> [product](/docs/v5/enum#product)| array<int>| Product  
> uidSuffix| array<int>| Affected UID tail number  
> [maintainType](/docs/v5/enum#maintaintype)| string| Maintenance type  
> [env](/docs/v5/enum#env)| string| Environment  
  
### Subscribe Example

  * JSON
  * Python


    
    
    {  
        "op": "subscribe",  
        "args": [  
            "system.status"  
        ]  
    }  
    
    
    
    from pybit.unified_trading import WebSocket  
    from time import sleep  
    ws = WebSocket(  
        testnet=True,  
        channel_type="misc/status",  
    )  
    def handle_message(message):  
        print(message)  
    ws.system_status_stream(  
        callback=handle_message  
    )  
    while True:  
        sleep(1)  
    

### Response Example
    
    
    {  
        "topic": "system.status",  
        "ts": 1751858399649,  
        "data": [  
            {  
                "id": "4d95b2a0-587f-11f0-bcc9-56f28c94d6ea",  
                "title": "t06",  
                "state": "completed",  
                "begin": "1751596902000",  
                "end": "1751597011000",  
                "href": "",  
                "serviceTypes": [  
                    2,  
                    3,  
                    4,  
                    5  
                ],  
                "product": [  
                    1,  
                    2  
                ],  
                "uidSuffix": [],  
                "maintainType": 1,  
                "env": 1  
            }  
        ]  
    }

---

# Websocket取得系統狀態

監聽大型平台維護或服務故障時取得系統狀態

信息

請注意，目前有些情況下, 服務發佈導致短暫停頓（持續時間少於 10 秒）或 WebSocket 中斷（使用者可立即重連），此類情況不會在此通知。

## 路徑

  * **主網:**  
`wss://stream.bybit.com/v5/public/misc/status`



信息

  * 從"[www.bybit.eu"註冊的歐盟用戶，請使用](http://www.bybit.eu%22%E8%A8%BB%E5%86%8A%E7%9A%84%E6%AD%90%E7%9B%9F%E7%94%A8%E6%88%B6%EF%BC%8C%E8%AB%8B%E4%BD%BF%E7%94%A8) `wss://stream.bybit.eu/v5/public/misc/status`



**Topic:**  
`system.status`

### 響應參數

參數| 類型| 說明  
---|---|---  
topic| string| 主題名稱  
ts| number| 系統產生的時間戳記（毫秒）  
data| array| Object  
> id| string| Id, 唯一標識  
> title| string| 系統維​​護說明的標題  
> [state](/docs/zh-TW/v5/enum#state)| string| 系統的狀態  
> begin| string| 系統維​​護的開始時間，Unix時間戳記的毫秒數格式  
> end| string| 交易全面開放的時間，Unix時間戳記的毫秒數格式。在維護完成前，是預期結束時間；維護完成後，會變更為實際結束時間  
> href| string| 系統維​​護詳情的超級連結,若無回傳值，預設值為空  
> [serviceTypes](/docs/zh-TW/v5/enum#servicetypes)| array<int>| 服務類型  
> [product](/docs/zh-TW/v5/enum#product)| array<int>| 產品  
> uidSuffix| array<int>| 維護期間受影響的UID尾號  
> [maintainType](/docs/zh-TW/v5/enum#maintaintype)| string| 維護類型  
> [env](/docs/zh-TW/v5/enum#env)| string| 環境  
  
### 訂閱範例

  * JSON
  * Python


    
    
    {  
        "op": "subscribe",  
        "args": [  
            "system.status"  
        ]  
    }  
    
    
    
    from pybit.unified_trading import WebSocket  
    from time import sleep  
    ws = WebSocket(  
        testnet=True,  
        channel_type="misc/status",  
    )  
    def handle_message(message):  
        print(message)  
    ws.system_status_stream(  
        callback=handle_message  
    )  
    while True:  
        sleep(1)  
    

### 響應示例
    
    
    {  
        "topic": "system.status",  
        "ts": 1751858399649,  
        "data": [  
            {  
                "id": "4d95b2a0-587f-11f0-bcc9-56f28c94d6ea",  
                "title": "t06",  
                "state": "completed",  
                "begin": "1751596902000",  
                "end": "1751597011000",  
                "href": "",  
                "serviceTypes": [  
                    2,  
                    3,  
                    4,  
                    5  
                ],  
                "product": [  
                    1,  
                    2  
                ],  
                "uidSuffix": [],  
                "maintainType": 1,  
                "env": 1  
            }  
        ]  
    }