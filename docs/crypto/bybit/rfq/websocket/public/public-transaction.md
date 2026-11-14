---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/rfq/websocket/public/public-transaction
api_type: WebSocket
updated_at: 2026-11-13 19:25:00.504251
---

# Trade

Latest block trade information. All legs in the same block trade are included in the same update. Data will be pushed whenever there is a block trade.

**Topic:** `rfq.open.public.trades`

### Response Parameters

Parameter| Type| Comments  
---|---|---  
id| string| Message ID  
topic| string| Topic name  
creationTime| int| Data created timestamp (ms)  
data| array| Object  
> rfqId| string| Inquiry ID  
>strategyType| string| Policy type  
> createdAt| string| Time (ms) when the trade is created in epoch, such as 1650380963  
> updatedAt| string| Time (ms) when the trade is updated in epoch, such as 1650380964  
> legs| array of objects| Combination transaction  
>> category| string| Product type: `spot`, `linear`, `option`  
>> symbol| string| symbol name  
>> side| string| Inquiry direction: Valid values are `buy` and `sell`  
>> price| string| Execution price  
>> qty| string| Number of executions  
>> markPrice| string| The markPrice (contract) at the time of transaction, and the spot price is indexPrice  
  
### Subscribe Example
    
    
    {  
        "op": "subscribe",  
        "args": [  
            "rfq.open.public.trades"  
        ]  
    }  
    

### Stream Example
    
    
    {  
      "topic": "rfq.open.public.trades",  
      "creationTime": 1757579314358,  
      "data": [  
        {  
          "rfqId": "1757579281847749169219132657134900",  
          "strategyType": "custom",  
          "legs": [  
            {  
              "category": "linear",  
              "symbol": "BTCUSDT",  
              "side": "Sell",  
              "price": "91600",  
              "qty": "1",  
              "markPrice": "90216.29"  
            }  
          ],  
          "createdAt": "1757579314213",  
          "updatedAt": "1757579314347"  
        }  
      ]  
    }

---

# 公共交易頻道

最新的大宗交易資訊。所有屬於同一大宗交易的明細都會包含在同一次更新中。每當發生大宗交易時，數據將被推送。

**主題:** `rfq.open.public.trades`

### 響應參數

參數| 類型| 說明  
---|---|---  
id| string| 消息 ID  
topic| string| 主題名稱  
creationTime| int| 數據創建時間戳（毫秒）  
data| array| 對象  
> rfqId| string| 詢價單 ID  
> strategyType| string| 策略類型  
> createdAt| string| 交易創建時間（毫秒），例如 1650380963  
> updatedAt| string| 交易更新時間（毫秒），例如 1650380964  
> legs| array of objects| 組合交易明細  
>> category| string| 產品類型：`spot`（現貨）、`linear`（線性合約）、`option`（期權）  
>> symbol| string| 交易對名稱  
>> side| string| 詢價方向：有效值為 `buy`（買入）和 `sell`（賣出）  
>> price| string| 成交價格  
>> qty| string| 成交數量  
>> markPrice| string| 成交時的標記價格（合約）；對於現貨，為指數價格  
  
### 訂閱示例
    
    
    {  
        "op": "subscribe",  
        "args": [  
            "rfq.open.public.trades"  
        ]  
    }  
    

### 響應示例
    
    
    {  
      "topic": "rfq.open.public.trades",  
      "creationTime": 1757579314358,  
      "data": [  
        {  
          "rfqId": "1757579281847749169219132657134900",  
          "strategyType": "custom",  
          "legs": [  
            {  
              "category": "linear",  
              "symbol": "BTCUSDT",  
              "side": "Sell",  
              "price": "91600",  
              "qty": "1",  
              "markPrice": "90216.29"  
            }  
          ],  
          "createdAt": "1757579314213",  
          "updatedAt": "1757579314347"  
        }  
      ]  
    }