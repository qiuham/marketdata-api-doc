---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/rfq/trade/cancel-rfq
api_type: Trading
updated_at: 2026-10-22 18:48:53.171657
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

  
anonymous| false| boolean| Whether or not it is anonymous inquiry. The default value is `false`. When it is `true` the identity of the inquiring party will not be revealed even after the transaction is concluded. When `anonymous` is `true`, the `deskCode` field returned by [Get RFQ](/docs/v5/rfq/trade/rfq-list) will be an empty string  
strategyType| false| string| Strategy type, if it is a custom inquiry, strategyType is `custom`, if it is a product combination provided by the system, it is the combination type; the default is `custom`; non-custom combinations have rate optimization, currently 50%; the transaction rate between LPs is currently 30%  
list| **true**|  array of objects| Combination transaction list 

  * Use [Get RFQ Configuration](/docs/v5/rfq/trade/rfq-config) to confirm the maximum length of the combination (`maxLegs`)
  * The base coin and settle coin of all combinations must be the same
  * Symbols under the same category must be unique

  
> category| **true**|  string| Product type: Unified account: `spot`, `linear`,`option`  
> symbol| **true**|  string| Name of the transaction contract. No inquiries are allowed in the last 30 minutes before contract settlement  
> side| **true**|  string| Inquiry transaction direction: `Buy` , `Sell`  
> qty| **true**|  string| If the number of transactions exceeds the position size, the position will then open in the reverse direction  
hedge| false| array of objects| Delta Hedge leg object (single object, not an array). The entire `hedge` object is optional; if omitted, this RFQ has no hedge leg  
> category| **true**|  string| Product type. Only `linear` is supported initially (perpetual / linear delivery futures)  
> symbol| **true**|  string| Hedge contract name, e.g. `BTCUSDT` (perpetual) or `BTC-27JUN25` (linear delivery futures). The underlying asset must match the main strategy legs (`list`). Cross-asset hedging is not supported  
> side| **true**|  string| Inquiry transaction direction: `Buy`, `Sell`  
> qty| **true**|  string| Trade quantity. If it exceeds the position size, the position will open in the reverse direction  
> price| false| string| Taker's desired Delta Hedge execution price, passed to the market maker for reference only. The maker may override this price in `create-quote`. Price validation reuses the existing derivatives limit-price logic; out-of-range values are automatically corrected  
  
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
        "counterparties": ["SPMAKERTEST"],  
        "rfqLinkId": "V2-Integration-Test-RFQ",  
        "anonymous": false,  
        "strategyType": "custom",  
        "list": [  
            {  
                "category": "option",  
                "symbol": "BTC-25JUL25-100000-C",  
                "side": "Buy",  
                "qty": "100"  
            }  
        ],  
        "hedge": [  
            {  
                "category": "linear",  
                "symbol": "BTCUSDT",  
                "side": "Sell",  
                "qty": "46",  
                "price": "121500.0"  
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
        counterparties=["SPMAKERTEST"],  
        rfqLinkId="V2-Integration-Test-RFQ",  
        anonymous=False,  
        strategyType="custom",  
        list=[  
            {  
                "category": "option",  
                "symbol": "BTC-25JUL25-100000-C",  
                "side": "Buy",  
                "qty": "100"  
            }  
        ],  
        hedge=[  
            {  
                "category": "linear",  
                "symbol": "BTCUSDT",  
                "side": "Sell",  
                "qty": "46",  
                "price": "121500.0"  
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

  
anonymous| false| boolean| 是否為匿名詢價，`true` 表示匿名詢價，`false` 表示公開詢價，預設值為 `false` ，當為 `true` 時，即使交易執行後，身份也不會透露給報價方。當 `anonymous` 為 `true` 時，[獲取詢價單](/docs/zh-TW/v5/rfq/trade/rfq-list) 返回的 `deskCode` 為空字串  
strategyType| false| string| 策略類型，若為自定義詢價，strategyType 為 `custom`，若為系統提供的產品，則為組合類型；預設為 `custom`；非自定義組合具有費率優化，目前為 50%；LP 之間的交易費率目前為 30%  
list| true| array of objects| 組合交易清單 

  * 通過 [rfq配寘資訊](/docs/zh-TW/v5/rfq/trade/rfq-config) 確認所提供的最大腿數 (`maxLegs`)
  * 所有組合的 basecoin 和 settleCoin 必須相同
  * 同類型下的 symbol 必須唯一

  
> category| true| string| 產品類型：統一帳戶：`spot`, `linear`, `option`  
> symbol| true| string| 交易合約名稱，合約結算前 30 分鐘不允許詢價  
> side| true| string| 詢價交易方向：`Buy` , `Sell`  
> qty| true| string| 交易數量，超過倉位的Size，則反向開倉  
hedge| false| array of objects| Delta Hedge 腿對象（單個對象，非陣列）；整個 `hedge` 對象均為可選，不填則本筆 RFQ 無 hedge 腿  
> category| **true**|  string| 產品類型，初期僅支持 `linear`（永續合約 / 線性交割期貨）  
> symbol| **true**|  string| 對冲合約名稱，如 `BTCUSDT`（永續）或 `BTC-27JUN25`（線性交割期貨）。底層資產須與主策略腿（`list`）一致，不支持跨資產對冲  
> side| **true**|  string| 詢價單交易方向：`Buy`, `Sell`  
> qty| **true**|  string| 交易數量，超過倉位的 Size，則反向開倉  
> price| false| string| Taker 期望的 Delta Hedge 執行價格，僅作為參考透傳給做市商；Maker 可在 `create-quote` 中覆蓋此價格。價格校驗復用主網現有衍生品限價邏輯，超限自動修正  
  
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
        "counterparties": ["SPMAKERTEST"],  
        "rfqLinkId": "V2-Integration-Test-RFQ",  
        "anonymous": false,  
        "strategyType": "custom",  
        "list": [  
            {  
                "category": "option",  
                "symbol": "BTC-25JUL25-100000-C",  
                "side": "Buy",  
                "qty": "100"  
            }  
        ],  
        "hedge": [  
            {  
                "category": "linear",  
                "symbol": "BTCUSDT",  
                "side": "Sell",  
                "qty": "46",  
                "price": "121500.0"  
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