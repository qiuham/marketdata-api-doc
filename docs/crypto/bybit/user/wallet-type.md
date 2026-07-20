---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/user/wallet-type
api_type: REST
updated_at: 2026-07-20 19:14:37.250592
---

# Greek

Subscribe to the greeks stream to see changes to your greeks data in **real-time**. `option` only.

**Topic:** `greeks`

### Response Parameters

Parameter| Type| Comments  
---|---|---  
id| string| Message ID  
topic| string| Topic name  
creationTime| number| Data created timestamp (ms)  
data| array| Object  
> baseCoin| string| Base coin  
> totalDelta| string| Delta value  
> totalGamma| string| Gamma value  
> totalVega| string| Vega value  
> totalTheta| string| Theta value  
  
### Subscribe Example
    
    
    {  
        "op": "subscribe",  
        "args": [  
            "greeks"  
        ]  
    }  
    
    
    
    from pybit.unified_trading import WebSocket  
    from time import sleep  
    ws = WebSocket(  
        testnet=True,  
        channel_type="private",  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    def handle_message(message):  
        print(message)  
    ws.greek_stream(callback=handle_message)  
    while True:  
        sleep(1)  
    

### Stream Example
    
    
    {  
        "id": "592324fa945a30-2603-49a5-b865-21668c29f2a6",  
        "topic": "greeks",  
        "creationTime": 1672364262482,  
        "data": [  
            {  
                "baseCoin": "ETH",  
                "totalDelta": "0.06999986",  
                "totalGamma": "-0.00000001",  
                "totalVega": "-0.00000024",  
                "totalTheta": "0.00001314"  
            }  
        ]  
    }

---

# 用戶希臘字母信息 (期權)

訂閱用戶希臘字母數據推送

**Topic:** `greeks`

### 響應參數

參數| 類型| 說明  
---|---|---  
id| string| 消息id  
topic| string| Topic名  
creationTime| number| 消息數據創建時間  
data| array| Object  
> baseCoin| string| 交易幣種  
> totalDelta| string| Delta值  
> totalGamma| string| Gamma值  
> totalVega| string| Vega值  
> totalTheta| string| Theta值  
  
### 訂閱示例
    
    
    {  
        "op": "subscribe",  
        "args": [  
            "greeks"  
        ]  
    }  
    
    
    
    from pybit.unified_trading import WebSocket  
    from time import sleep  
    ws = WebSocket(  
        testnet=True,  
        channel_type="private",  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    def handle_message(message):  
        print(message)  
    ws.greek_stream(callback=handle_message)  
    while True:  
        sleep(1)  
    

### 推送示例
    
    
    {  
        "id": "592324fa945a30-2603-49a5-b865-21668c29f2a6",  
        "topic": "greeks",  
        "creationTime": 1672364262482,  
        "data": [  
            {  
                "baseCoin": "ETH",  
                "totalDelta": "0.06999986",  
                "totalGamma": "-0.00000001",  
                "totalVega": "-0.00000024",  
                "totalTheta": "0.00001314"  
            }  
        ]  
    }