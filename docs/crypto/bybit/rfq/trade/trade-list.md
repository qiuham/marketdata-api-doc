---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/rfq/trade/trade-list
api_type: Trading
updated_at: 2026-06-29 19:32:17.346058
---

# Quote

Obtain the quote information sent or received by the user themselves. Whenever the user sends or receives a quote themselves, the data will be pushed.

**Topic:** `rfq.open.quotes`

### Response Parameters

Parameter| Type| Comments  
---|---|---  
id| string| Message ID  
topic| string| Topic name  
creationTime| int| Data created timestamp (ms)  
data| array| Object  
> rfqId| string| Inquiry ID  
> rfqLinkId| string| The unique identification code of the inquiring party, which is not visible when anonymous was set to `true` when the RFQ was created  
> quoteId| string| Quote ID  
> quoteLinkId| string| The unique identification code of the inquiring party, which is not visible when anonymous was set to `true` when the quote was created  
> expiresAt| string| The quote's expiration time (ms)  
> deskCode| string| The unique identification code of the quote party, which is not visible when anonymous is set to `true` during quotation  
> status| string| Status of quote: `Active`, `Canceled`, `PendingFill`, `Filled`, `Expired`, `Failed`  
>execQuoteSide| string| Execute the quote direction, `buy` or `sell`. When the quote direction is 'buy', for maker, the execution direction is the same as the direction in legs, and opposite for taker. Conversely, the same applies  
> createdAt| string| Time (ms) when the trade is created in epoch, such as 1650380963  
> updatedAt| string| Time (ms) when the trade is updated in epoch, such as 1650380964  
> quoteBuyList| array of objects| Quote buy direction  
>> category| string| Product type: `spot`, `linear`, `option`  
>> symbol| string| symbol name  
>> price| string| Quote price  
>> qty| string| Quantity  
> quoteSellList| array of objects| Quote sell direction  
>> category| string| Product type: `spot`, `linear`, `option`  
>> symbol| string| symbol name  
>> price| string| Quote price  
>> qty| string| Quantity  
  
### Subscribe Example
    
    
    {  
        "op": "subscribe",  
        "args": [  
            "rfq.open.quotes"  
        ]  
    }  
    

### Stream Example
    
    
    {  
      "topic": "rfq.open.quotes",  
      "creationTime": 1757578449562,  
      "data": [  
        {  
          "rfqLinkId": "",  
          "rfqId": "1757578410512325974246073709371267",  
          "quoteId": "1757578449553042047579782748460520",  
          "quoteLinkId": "",  
          "expiresAt": "1757578509556",  
          "status": "Active",  
          "deskCode": "test0904",  
          "execQuoteSide": "",  
          "quoteBuyList": [  
            {  
              "category": "linear",  
              "symbol": "BTCUSDT",  
              "price": "95800",  
              "qty": "1"  
            }  
          ],  
          "quoteSellList": [  
            {  
              "category": "linear",  
              "symbol": "BTCUSDT",  
              "price": "95000",  
              "qty": "1"  
            }  
          ],  
          "createdAt": "1757578449556",  
          "updatedAt": "1757578449556"  
        }  
      ]  
    }

---

# 報價頻道

獲取用戶自己發送或接收的報價信息。每當用戶自己發送或接收報價時，數據將被推送。

**主題：** `rfq.open.quotes`

### 響應參數

參數| 類型| 說明  
---|---|---  
id| string| 消息 ID  
topic| string| 主題名稱  
creationTime| int| 數據創建時間戳（毫秒）  
data| array| Object  
> rfqId| string| 詢價單 ID  
> rfqLinkId| string| 詢價單的自定義 ID，客戶的敏感信息，不會向報價方披露，返回 ""。  
> quoteId| string| 報價單 ID  
> quoteLinkId| string| 報價單自定義 ID，客戶的敏感信息，不會向詢價方披露，返回 ""。  
> expiresAt| string| 報價單到期時間，Unix 時間戳的毫秒格式  
> deskCode| string| 報價方的唯一識別碼，如果在報價期間設置為匿名，則不可見  
> status| string| 報價單狀態：`Active`（活躍）、`Canceled`（已取消）、`PendingFill`（待成交）、`Filled`（已成交）、`Expired`（已過期）、`Failed`（失敗）  
>execQuoteSide| string| 執行報價方向，`Buy`（買入） 或 `Sell`（賣出）。當報價方向為 "buy" 時，對於 maker（做市方），執行方向與 legs 中的方向一致；對於 taker（接單方），執行方向相反。反之亦然。  
> createdAt| string| 交易創建的時間（毫秒），例如 1650380963  
> updatedAt| string| 交易更新的時間（毫秒），例如 1650380964  
> quoteBuyList| array of objects| 報價買入方向  
>> category| string| 產品類型：`spot`（現貨）、`linear`（線性）、`option`（期權）  
>> symbol| string| 交易對名稱  
>> price| string| 報價價格  
>> qty| string| 數量  
> quoteSellList| array of objects| 報價賣出方向  
>> category| string| 產品類型：`spot`（現貨）、`linear`（線性）、`option`（期權）  
>> symbol| string| 交易對名稱  
>> price| string| 報價價格  
>> qty| string| 數量  
  
### 訂閱示例
    
    
    {  
        "op": "subscribe",  
        "args": [  
            "rfq.open.quotes"  
        ]  
    }  
    

### 資料流示例
    
    
    {  
      "topic": "rfq.open.quotes",  
      "creationTime": 1757578449562,  
      "data": [  
        {  
          "rfqLinkId": "",  
          "rfqId": "1757578410512325974246073709371267",  
          "quoteId": "1757578449553042047579782748460520",  
          "quoteLinkId": "",  
          "expiresAt": "1757578509556",  
          "status": "Active",  
          "deskCode": "test0904",  
          "execQuoteSide": "",  
          "quoteBuyList": [  
            {  
              "category": "linear",  
              "symbol": "BTCUSDT",  
              "price": "95800",  
              "qty": "1"  
            }  
          ],  
          "quoteSellList": [  
            {  
              "category": "linear",  
              "symbol": "BTCUSDT",  
              "price": "95000",  
              "qty": "1"  
            }  
          ],  
          "createdAt": "1757578449556",  
          "updatedAt": "1757578449556"  
        }  
      ]  
    }