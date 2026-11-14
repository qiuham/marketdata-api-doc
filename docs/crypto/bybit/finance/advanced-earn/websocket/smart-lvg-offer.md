---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/advanced-earn/websocket/smart-lvg-offer
api_type: WebSocket
updated_at: 2026-11-13 19:23:05.984841
---

# Smart Leverage Offers

### WebSocket public URL

  * **Mainnet:**  
Earn: `wss://stream.bybit.com/v5/public/fp`  


  * **Testnet:**  
Earn: `wss://stream-testnet.bybit.com/v5/public/fp`  





### Desc

  * Real-time push when price or quota parameters change
  * Periodic push every 30 seconds, even without any updates



### Topic: `earn.smartleverage.offers`

### Response Parameters

Parameter| Type| Comments  
---|---|---  
topic| string| Topic name  
data| array| Object  
> p| string| Product ID  
> b| string| Breakeven price  
> e| string| Quote expiry time  
> m| string| Maximum single order amount at current quote  
> c| string| Current market price of the underlying asset  
  
### Subscribe Example
    
    
    {  
        "op": "subscribe",  
        "args": [  
            "earn.dualassets.offers"  
        ]  
    }  
    

### Stream Example
    
    
    {  
        "topic": "earn.smartleverage.offers",  
        "data": [  
            {  
                "p": "13010",  
                "b": "553.849143",  
                "e": "1775040711994",  
                "m": "784",  
                "c": "615.1"  
            }  
        ]  
    }

---

# 槓桿無憂報價

### WebSocket 公共頻道網址

  * **主網：**  
Earn: `wss://stream.bybit.com/v5/public/fp`  


  * **測試網：**  
Earn: `wss://stream-testnet.bybit.com/v5/public/fp`  





### 說明

  * 當價格或報價參數變化時即時推送
  * 即使無任何更新，每 30 秒定期推送



### 頻道：`earn.smartleverage.offers`

### 響應參數

參數| 類型| 說明  
---|---|---  
topic| string| 頻道名稱  
data| array| 列表  
> p| string| 產品 ID  
> b| string| 損益平衡價格  
> e| string| 報價到期時間  
> m| string| 當前報價下的最大單筆訂單金額  
> c| string| 標的資產的當前市場價格  
  
### 訂閱示例
    
    
    {  
        "op": "subscribe",  
        "args": [  
            "earn.dualassets.offers"  
        ]  
    }  
    

### 推送示例
    
    
    {  
        "topic": "earn.smartleverage.offers",  
        "data": [  
            {  
                "p": "13010",  
                "b": "553.849143",  
                "e": "1775040711994",  
                "m": "784",  
                "c": "615.1"  
            }  
        ]  
    }