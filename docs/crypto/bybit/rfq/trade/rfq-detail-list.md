---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/rfq/trade/rfq-detail-list
api_type: Trading
updated_at: 2026-10-31 18:37:08.854681
---

# RFQ

Obtain the inquiries (requests for quotes) information sent or received by the user themselves. Whenever the user sends or receives an inquiry themselves, the data will be pushed.

**Topic:** `rfq.open.rfqs`

### Response Parameters

Parameter| Type| Comments  
---|---|---  
id| string| Message ID  
topic| string| Topic name  
creationTime| int| Data created timestamp (ms)  
data| array of objects| RFQ data: Return and obtain real-time inquiry information Open consistent  
> rfqId| string| Inquiry ID  
> rfqLinkId| string| The unique identification code of the inquiring party, which is not visible when anonymous was set to `true` when the RFQ was created  
>counterparties| Array of strings| List of bidders  
> expiresAt| string| The quote's expiration time (ms)  
> strategyType| string| Inquiry label  
> status| string| Status of the inquiry form: `Active`, `Canceled`, `PendingFill`, `Filled`, `Expired`, `Failed`  
> acceptOtherQuoteStatus| string| Whether to accept non-LP quotes. The default value is `false`: `false`: Default value, do not accept non-LP quotes. `true`: Accept non-LP quotes  
> deskCode| string| The unique identification code of the inquiring party, which is not visible when anonymous was set to `true` when the RFQ was created  
> createdAt| string| Time (ms) when the trade is created in epoch, such as 1650380963  
> updatedAt| string| Time (ms) when the trade is updated in epoch, such as 1650380964  
> legs| array of objects| Combination transaction  
>> category| string| Category. Valid values include: `linear`, `option` and `spot`  
>> symbol| string| symbol name  
>> side| string| Inquiry direction. Valid values are `buy` and `sell`  
>> qty| string| Order quantity of the instrument  
  
### Subscribe Example
    
    
    {  
        "op": "subscribe",  
        "args": [  
            "rfq.open.rfqs"  
        ]  
    }  
    

### Stream Example
    
    
    {  
      "topic": "rfq.open.rfqs",  
      "creationTime": 1757482013792,  
      "data": [  
        {  
          "rfqLinkId": "",  
          "rfqId": "1757482013783362721227613524547439",  
          "counterparties": [  
            "test0904"  
          ],  
          "strategyType": "custom",  
          "expiresAt": "1757482613784",  
          "status": "Active",  
          "acceptOtherQuoteStatus":"false",  
          "deskCode": "1nu9d1",  
          "createdAt": "1757482013784",  
          "updatedAt": "1757482013784",  
          "legs": [  
            {  
              "category": "linear",  
              "symbol": "BTCUSDT",  
              "side": "Buy",  
              "qty": "5"  
            }  
          ]  
        }  
      ]  
    }

---

# 詢價頻道

獲取用戶自己發送或接收的詢價信息。每當用戶自己發送或接收詢價時，數據將被推送。

**主題：** `rfq.open.rfqs`

### 響應參數

參數| 類型| 說明  
---|---|---  
id| string| 消息 ID  
topic| string| 主題名稱  
creationTime| int| 數據創建時間戳（毫秒）  
data| array<object>| 詢價數據：返回並獲取實時詢價信息，與打開的詢價保持一致  
> rfqId| string| 詢價單 ID  
> rfqLinkId| string| 詢價單的自定義 ID，客戶的敏感信息，不會向報價方披露，返回 ""。  
>counterparties| Array of strings| 投標方列表  
> expiresAt| string| 詢價單到期時間，Unix 時間戳的毫秒格式  
> strategyType| string| 詢價標籤  
> status| string| 詢價單狀態：`Active`（活躍）、`Canceled`（已取消）、`PendingFill`（待成交）、`Filled`（已成交）、`Expired`（已過期）、`Failed`（失敗）  
> acceptOtherQuoteStatus| string| 是否接受非 LP 報價. 預設值是 `false`.`false`: 不接受非 LP 報價. `true`: 接受非 LP 報價  
> deskCode| string| 詢價方的唯一識別碼，如果在詢價期間設置為匿名，則不可見  
> createdAt| string| 交易創建的時間（毫秒），例如 1650380963  
> updatedAt| string| 交易更新的時間（毫秒），例如 1650380964  
> legs| Array of objects| 組合交易  
>> category| string| 類別。有效值包括：`linear`（線性）、`option`（期權） 和 `spot`（現貨）  
>> symbol| string| 交易對名稱  
>> side| string| 詢價方向。有效值為 `buy`（買入） 和 `sell`（賣出）  
>> qty| string| 合約的訂單數量  
  
### 訂閱示例
    
    
    {  
        "op": "subscribe",  
        "args": [  
            "rfq.open.rfqs"  
        ]  
    }  
    

### 資料流示例
    
    
    {  
      "topic": "rfq.open.rfqs",  
      "creationTime": 1757482013792,  
      "data": [  
        {  
          "rfqLinkId": "",  
          "rfqId": "1757482013783362721227613524547439",  
          "counterparties": [  
            "test0904"  
          ],  
          "strategyType": "custom",  
          "expiresAt": "1757482613784",  
          "status": "Active",  
          "acceptOtherQuoteStatus":"false",  
          "deskCode": "1nu9d1",  
          "createdAt": "1757482013784",  
          "updatedAt": "1757482013784",  
          "legs": [  
            {  
              "category": "linear",  
              "symbol": "BTCUSDT",  
              "side": "Buy",  
              "qty": "5"  
            }  
          ]  
        }  
      ]  
    }