---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/rfq/trade/create-quote
api_type: Trading
updated_at: 2026-06-29 19:32:04.556817
---

# Create RFQ

Create RFQ. **Up to 50 requests** per second.

info

  * Only supports UTA2.0 accounts
  * Only supports full position and combined margin mode
  * Not supported by demo users
  * Cannot choose oneself as the bidder



### HTTP Request

POST`/v5/rfq/create-rfq`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
counterparties| **true**|  array| Spread combination symbol name  
rfqLinkId| false| string| Custom RFQ ID

  * The length should be between 1-32 bits 
  * Combination of letters (case sensitive) and numbers
  * An rfqLinkId expires after three months – after which it can be reused
  * Open orders must have a unique ID whereas orders that have reached a final/terminated status do not have to be unique. 

  
anonymous| false| boolean| Whether or not it is anonymous inquiry. The default value is `false`. When it is `true` the identity of the inquiring party will not be revealed even after the transaction is concluded.  
strategyType| false| string| Strategy type, if it is a custom inquiry, strategyType is `custom`, if it is a product combination provided by the system, it is the combination type; the default is `custom`; non-custom combinations have rate optimization, currently 50%; the transaction rate between LPs is currently 30%  
list| **true**|  array of objects| Combination transaction list 

  * Use [Get RFQ Configuration](/docs/v5/rfq/trade/rfq-config) to confirm the maximum length of the combination (`maxLegs`)
  * The base coin and settle coin of all combinations must be the same
  * Symbols under the same category must be unique

  
> category| **true**|  string| Product type: Unified account: `spot`, `linear`,`option`  
> symbol| **true**|  string| Name of the transaction contract. No inquiries are allowed in the last 30 minutes before contract settlement  
> side| **true**|  string| Inquiry transaction direction: `Buy` , `Sell`  
> qty| **true**|  string| If the number of transactions exceeds the position size, the position will then open in the reverse direction  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
result| array| Order ID  
list| array of objects|   
> rfqId| string| Inquiry ID  
> rfqLinkId| string| Custom inquiry ID  
> status| string| Status of the RFQ: `Active` `Canceled` `Filled` `Expired` `Failed`  
> expiresAt| string| The inquiry's expiration time (ms)  
> deskCode| string| Inquiring party's unique identification code  
  
### Request Example

  * HTTP
  * Python


    
    
    POST /v5/rfq/create-rfq HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1744083949347  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 115  
      
    {  
        "counterparties": ["LP4","LP5"],  
        "rfqLinkId":"rfq00993",  
        "anonymous": false,  
        "strategyType": "custom",  
        "list": [  
            {  
                "category": "linear",  
                "symbol": "BTCUSDT",  
                "side":"buy",  
                "qty":"2"  
            },  
            {  
                "category": "spot",  
                "symbol": "BTCUSDT",  
                "side":"buy",  
                "qty":"2"  
            },  
            {  
                "category": "option",  
                "symbol": "BTCUSDT",  
                "side":"sell",  
                "qty":"2"  
            }  
        ]  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.create_rfq(  
        counterparties=["LP4", "LP5"],  
        rfqLinkId="rfq00993",  
        anonymous=False,  
        strategyType="custom",  
        list=[  
            {  
                "category": "linear",  
                "symbol": "BTCUSDT",  
                "side": "Buy",  
                "qty": "2"  
            },  
            {  
                "category": "spot",  
                "symbol": "BTCUSDT",  
                "side": "Buy",  
                "qty": "2"  
            },  
            {  
                "category": "option",  
                "symbol": "BTCUSDT",  
                "side": "Sell",  
                "qty": "2"  
            }  
        ]  
    ))  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "rfqId": "17526315514105706281",  
            "rfqLinkId": "rfq00993",  
            "status": "Active",  
            "expiresAt": "1752632151414",  
            "deskCode": "LP2"  
        },  
        "retExtInfo": {},  
        "time": 1752631551419  
    }

---

# 詢價

創建詢價單 **每秒最多 50 次請求**

信息

  * 僅支持 UTA2.0 帳戶
  * 僅支持全倉與組合保證金模式
  * 不支持模擬用戶 
  * 不能選擇自己作為報價方



### HTTP 請求

POST`/v5/rfq/create-rfq`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
counterparties| **true**|  Array of deskCode| 希望接收詢價的報價方列表,可透過 `/v5/rfq/config`獲取  
rfqLinkId| false| string| 自定義詢價單 ID： 

  * 長度應介於 1-32 位 
  * 字母（區分大小寫）與數字的組合，可以是純字母或純數字 
  * 指定 rfqLinkId 僅檢查最近 3 個月的資料 
  * 非終端狀態僅能保證在 24 小時內的唯一性，而終端狀態不保證唯一性 

  
anonymous| false| boolean| 是否為匿名詢價，`true` 表示匿名詢價，`false` 表示公開詢價，預設值為 `false` ，當為 `true` 時，即使交易執行後，身份也不會透露給報價方。  
strategyType| false| string| 策略類型，若為自定義詢價，strategyType 為 `custom`，若為系統提供的產品，則為組合類型；預設為 `custom`；非自定義組合具有費率優化，目前為 50%；LP 之間的交易費率目前為 30%  
list| true| array of objects| 組合交易清單 

  * 通過 [rfq配寘資訊](/docs/zh-TW/v5/rfq/trade/rfq-config) 確認所提供的最大腿數 (`maxLegs`)
  * 所有組合的 basecoin 和 settleCoin 必須相同
  * 同類型下的 symbol 必須唯一

  
> category| true| string| 產品類型：統一帳戶：`spot`, `linear`, `option`  
> symbol| true| string| 交易合約名稱，合約結算前 30 分鐘不允許詢價  
> side| true| string| 詢價交易方向：`Buy` , `Sell`  
> qty| true| string| 交易數量，超過倉位的Size，則反向開倉  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
result| array| 訂單 ID  
list| array<object>|   
> rfqId| string| 詢價單 ID  
> rfqLinkId| string| 自定義詢價單 ID  
> status| string| 詢價單狀態： `Active` `Canceled` `Filled` `Expired` `Failed`  
> expiresAt| string| 詢價單的到期時間，為 Unix 時間戳的毫秒格式  
> deskCode| string| 詢價方唯一識別碼  
  
### 請求示例
    
    
    POST /v5/rfq/create-rfq HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1744083949347  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 115  
      
    {  
        "counterparties": ["LP4","LP5"],  
        "rfqLinkId":"rfq00993",  
        "anonymous": false,  
        "strategyType": "custom",  
        "list": [  
            {  
                "category": "linear",  
                "symbol": "BTCUSDT",  
                "side":"buy",  
                "qty":"2"  
            },  
            {  
                "category": "spot",  
                "symbol": "BTCUSDT",  
                "side":"buy",  
                "qty":"2"  
            },  
            {  
                "category": "option",  
                "symbol": "BTCUSDT",  
                "side":"sell",  
                "qty":"2"  
            }  
        ]  
    }  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "rfqId": "17526315514105706281",  
            "rfqLinkId": "rfq00993",  
            "status": "Active",  
            "expiresAt": "1752632151414",  
            "deskCode": "LP2"  
        },  
        "retExtInfo": {},  
        "time": 1752631551419  
    }