---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/rfq/trade/create-rfq
api_type: Trading
updated_at: 2026-07-17 18:52:47.349953
---

# Get Quotes

Obtain historical quote information. **Up to 50 requests per second**

info

  * Obtain historical quotes. This data is not real-time. Please see Get RFQs (real-time).
  * If both quoteId and quoteLinkId are passed, only both is considered.
  * If both rfqId and rfqLinkId are passed, only rfqId is considered.
  * Sorted in descending order by createdAt.



### HTTP Request

GET`/v5/rfq/quote-list`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
rfqId|  _false_|  string| Inquiry ID  
quoteId|  _false_|  string| Quote ID  
quoteLinkId|  _false_|  string| Custom quote ID. If traderType is `request` this field is invalid  
traderType| false| string| Trader type, `quote` , `request`. Default: `quote`  
status| false| string| Status of the RFQ: `Active` `Canceled` `PendingFill` `Filled` `Expired` `Failed`  
limit| false| integer| Return the number of items. [`1`, `100`]. Default: `50`  
cursor| false| string| Cursor. Use the `nextPageCursor` token from the response to retrieve the next page of the result set  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
result| Object|   
> cursor| string| Refer to the `cursor` request parameter  
> list| array| An array of quotes  
>> rfqId| string| Inquiry ID  
>> rfqLinkId| string| Custom RFQ ID. Not publicly disclosed.  
>> quoteId| string| Quote ID  
>> quoteLinkId| string| Custom quote ID. Not publicly disclosed.  
>> expiresAt| string| The quote's expiration time (ms)  
>> deskCode| string| The unique identification code of the inquiring party, which is not visible when anonymous was set to `true` when the quote was created  
>> status| string| Status of the RFQ: `Active` `PendingFill` `Canceled` `Filled` `Expired` `Failed`  
>> execQuoteSide| string| Execute the quote direction, `Buy` or `Sell` . When the quote direction is `Buy` , for maker, the execution direction is the same as the direction in legs, and opposite for taker. Conversely, the same applies  
>> createdAt| string| Time (ms) when the trade is created in epoch, such as 1650380963  
>> updatedAt| string| Time (ms) when the trade is updated in epoch, such as 1650380964  
>> quoteBuyList| array of objects| Quote `Buy` Direction  
>>> category| string| Product type: `spot`,`linear`,`option`  
>>> symbol| string| The unique instrument ID  
>>> price| string| Order price in the quote currency of the instrument.  
>>> qty| string| Order quantity of the instrument.  
>> quoteSellList| array of objects| Quote `Sell` Direction  
>>> category| string| Product type: `spot`,`linear`,`option`  
>>> symbol| string| The unique instrument ID  
>>> price| string| Order price in the quote currency of the instrument.  
>>> qty| string| Order quantity of the instrument.  
  
### Request Example

  * HTTP
  * Python


    
    
    GET /v5/rfq/quote-list HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1676430842094  
    X-BAPI-RECV-WINDOW: 5000  
    X-BAPI-SIGN: XXXXXX  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_quote_list())  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "cursor": "",  
            "list": [  
                {  
                    "rfqLinkId": "",  
                    "rfqId": "175740578143743543930777169307022",  
                    "quoteId": "1757405933130044334361923221559805",  
                    "quoteLinkId": "",  
                    "expiresAt": "1757405993126",  
                    "status": "Expired",  
                    "deskCode": "test0904",  
                    "execQuoteSide": "",  
                    "quoteBuyList": [  
                        {  
                            "category": "linear",  
                            "symbol": "BTCUSDT",  
                            "price": "113790",  
                            "qty": "0.5"  
                        }  
                    ],  
                    "quoteSellList": [  
                        {  
                            "category": "linear",  
                            "symbol": "BTCUSDT",  
                            "price": "110500",  
                            "qty": "0.5"  
                        }  
                    ],  
                    "createdAt": "1757405933126",  
                    "updatedAt": "1757405999156"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1757406548275  
    }

---

# 獲取歷史報價

獲取歷史報價資訊。**每秒最多 50 次請求**

信息

  * 獲取使用者發送或接收的報價資訊，從資料庫查詢，有延遲
  * 同時傳遞 quoteId 和 quoteLinkId 時，以 quoteId 為準
  * 同時傳遞 rfqId 和 rfqLinkId 時，以 rfqId 為準
  * 根據報價的創建時間倒序排列



### HTTP 請求

GET`/v5/rfq/quote-list`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
rfqId| **false**|  string| 詢價單 ID  
quoteId| **false**|  string| 報價單 ID  
quoteLinkId| **false**|  string| 報價單自定義 ID；當 traderType 為 `request` 時，此字段無效  
traderType| **false**|  string| 交易者類型，`quote` 或 `request`，默認為 `quote`

  * `Request`：詢價方，查詢自己接收到的報價
  * `Quote`：報價方，查詢自己發布的報價

  
status| false| string| 詢價單狀態：`Active`、`Canceled`、`PendingFill`、`Filled`、`Expired`、`Failed`  
limit| **false**|  integer| 返回的項目數量，最多 100 項，默認 50 項  
cursor| **false**|  string| 翻頁標記，請使用返回的 cursor；簽名時使用返回的原始資料，發送請求時進行 URLEncode  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
result| Object|   
> cursor| string| 翻頁標記  
> list| Array| 報價數據陣列  
>> rfqId| string| 詢價單 ID  
>> rfqLinkId| string| 自定義詢價單 ID，客戶敏感資訊不會公開，僅返回給報價方  
>> quoteId| string| 報價單 ID  
>> quoteLinkId| string| 自定義報價單 ID，客戶敏感資訊不會公開，僅返回給詢價方  
>> expiresAt| string| 詢價單的過期時間，Unix 時間戳的毫秒格式  
>> deskCode| string| 詢價方的唯一識別代碼，若詢價時設置匿名為 `true` 則不可見  
>> status| string| 詢價單狀態：`Active`、`PendingFill`、`Canceled`、`Filled`、`Expired`、`Failed`  
>> execQuoteSide| string| 執行報價方向，`Buy` 或 `Sell` 。當報價方向為 `Buy` 時，對於 maker，執行方向與 legs 中的方向一致，對於 taker 則相反；反之亦然  
>> createdAt| string| 交易創建的時間（毫秒），例如 1650380963  
>> updatedAt| string| 交易更新的時間（毫秒），例如 1650380964  
>> quoteBuyList| array of objects| 報價 `Buy` 方向  
>>> category| string| 產品類型：`spot`、`linear`、`option`  
>>> symbol| string| 唯一的交易品種 ID  
>>> price| string| 報價貨幣中的訂單價格  
>>> qty| string| 交易品種的訂單數量  
>> quoteSellList| array of objects| 報價 `Sell` 方向  
>>> category| string| 產品類型：`spot`、`linear`、`option`  
>>> symbol| string| 唯一的交易品種 ID  
>>> price| string| 報價貨幣中的訂單價格  
>>> qty| string| 交易品種的訂單數量  
  
### 請求示例
    
    
    GET /v5/rfq/quote-list HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1676430842094  
    X-BAPI-RECV-WINDOW: 5000  
    X-BAPI-SIGN: XXXXXX  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "cursor": "",  
            "list": [  
                {  
                    "rfqLinkId": "",  
                    "rfqId": "175740578143743543930777169307022",  
                    "quoteId": "1757405933130044334361923221559805",  
                    "quoteLinkId": "",  
                    "expiresAt": "1757405993126",  
                    "status": "Expired",  
                    "deskCode": "test0904",  
                    "execQuoteSide": "",  
                    "quoteBuyList": [  
                        {  
                            "category": "linear",  
                            "symbol": "BTCUSDT",  
                            "price": "113790",  
                            "qty": "0.5"  
                        }  
                    ],  
                    "quoteSellList": [  
                        {  
                            "category": "linear",  
                            "symbol": "BTCUSDT",  
                            "price": "110500",  
                            "qty": "0.5"  
                        }  
                    ],  
                    "createdAt": "1757405933126",  
                    "updatedAt": "1757405999156"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1757406548275  
    }