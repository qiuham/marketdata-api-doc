---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/websocket/public/insurance-pool
api_type: WebSocket
updated_at: 2026-10-10 18:50:34.630961
---

# Insurance Pool

Subscribe to get the update of insurance pool balance 

Push frequency: **1s**

**Topic:**  
USDT contracts: `insurance.USDT`  
USDC contracts: `insurance.USDC` (**note** : all USDC Perpetuals, USDC Futures have their own shared insurance pools)  
Inverse contracts: `insurance.inverse`

info

  * Shared insurance pool data is **not** pushed, please refer to Rest API [Get Insurance](/docs/v5/market/insurance) to understand which symbols belong to isolated or shared insurance pools.
  * No event will be published if the balances of all insurance pools remain unchanged.



### Response Parameters

Parameter| Type| Comments  
---|---|---  
topic| string| Topic name  
type| string| Data type. `snapshot`, `delta`  
ts| number| The timestamp (ms) that the system generates the data  
data| Object|   
> coin| string| Insurance pool coin  
> symbols| string| Symbol name  
> balance| string| Balance  
> updateTime| string| Data updated timestamp (ms)  
  
### Subscribe Example

  * JSON
  * Python


    
    
    {  
        "op": "subscribe",  
        "args": [  
            "insurance.USDT",  
            "insurance.USDC"  
        ]  
    }  
    
    
    
    from pybit.unified_trading import WebSocket  
    from time import sleep  
    ws = WebSocket(  
        testnet=True,  
        channel_type="linear",  
    )  
    def handle_message(message):  
        print(message)  
    ws.insurance_pool_stream(  
        contract_group=["USDT", "USDC"],  
        callback=handle_message  
    )  
    while True:  
        sleep(1)  
    

### Response Example
    
    
    {  
        "topic": "insurance.USDT",  
        "type": "delta",  
        "ts": 1747722930000,  
        "data": [  
            {  
                "coin": "USDT",  
                "symbols": "GRIFFAINUSDT",  
                "balance": "25614.92972633",  
                "updateTime": "1747722930000"  
            },  
            {  
                "coin": "USDT",  
                "symbols": "CGPTUSDT",  
                "balance": "100000.27064825",  
                "updateTime": "1747722930000"  
            },  
            {  
                "coin": "USDT",  
                "symbols": "GOATUSDT",  
                "balance": "20352.32665441",  
                "updateTime": "1747722930000"  
            },  
            {  
                "coin": "USDT",  
                "symbols": "XTERUSDT",  
                "balance": "19998.81533291",  
                "updateTime": "1747722930000"  
            }  
        ]  
    }

---

# 保險池餘額

訂閱來獲取保險池的餘額變動

推送頻率: **1秒**

**Topic:**  
USDT合約: `insurance.USDT`  
USDC合約: `insurance.USDC` (**注意** : 目前所有的USDC永續, USDC交割有各自的共享保險池  
反向合約: `insurance.inverse`

信息

  * 共享保險池的餘額數據不推送, 可以調用[查詢保險基金](/docs/zh-TW/v5/market/insurance)接口獲取到每個合約屬於共享還是獨立保險池
  * 如果1秒內沒有任何保險池子的餘額發生變化, 將不會有消息下發



### 響應參數

參數| 類型| 說明  
---|---|---  
topic| string| Topic名  
type| string| 數據類型. `snapshot`, `delta`  
ts| number| 行情服務生成數據的時間戳 (毫秒)  
data| Object|   
> coin| string| 保險池幣種  
> symbols| string| 合約名稱  
> balance| string| 保險基金的幣種餘額  
> updateTime| string| 餘額更新時間戳  
  
### 訂閱示例

  * JSON
  * Python


    
    
    {  
        "op": "subscribe",  
        "args": [  
            "insurance.USDT",  
            "insurance.USDC"  
        ]  
    }  
    
    
    
    from pybit.unified_trading import WebSocket  
    from time import sleep  
    ws = WebSocket(  
        testnet=True,  
        channel_type="linear",  
    )  
    def handle_message(message):  
        print(message)  
    ws.insurance_pool_stream(  
        contract_group=["USDT", "USDC"],  
        callback=handle_message  
    )  
    while True:  
        sleep(1)  
    

### 消息示例
    
    
    {  
        "topic": "insurance.USDT",  
        "type": "delta",  
        "ts": 1747722930000,  
        "data": [  
            {  
                "coin": "USDT",  
                "symbols": "GRIFFAINUSDT",  
                "balance": "25614.92972633",  
                "updateTime": "1747722930000"  
            },  
            {  
                "coin": "USDT",  
                "symbols": "CGPTUSDT",  
                "balance": "100000.27064825",  
                "updateTime": "1747722930000"  
            },  
            {  
                "coin": "USDT",  
                "symbols": "GOATUSDT",  
                "balance": "20352.32665441",  
                "updateTime": "1747722930000"  
            },  
            {  
                "coin": "USDT",  
                "symbols": "XTERUSDT",  
                "balance": "19998.81533291",  
                "updateTime": "1747722930000"  
            }  
        ]  
    }