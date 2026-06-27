---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/rfq/trade/create-quote
api_type: Trading
updated_at: 2026-05-27 19:21:37.922947
---

# Create Quote

Create a quote. **Up to 50 requests** per second. The quoting party sends a quote in response to the inquirier.

info

  * Only support UTA2.0 accounts
  * Cannot quote for your own inquiry
  * One request reports in two directions
  * You must pass at least one quoteBuyList and quoteSellList
  * If you would like to quote a spot quote, please ensure the corresponding collateral asset is enabled using [Set Collateral Coin](/docs/v5/account/set-collateral) or [Batch Set Collateral Coin](/docs/v5/account/batch-set-collateral)



### HTTP Request

POST`/v5/rfq/create-quote`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
rfqId| **true**|  string| Inquiry ID  
quoteLinkId| false| string| Custom quote ID: 

  * The length should be between 1-32 bits 
  * Combination of letters (case sensitive) and numbers
  * An rfqLinkId expires after three months – after which it can be reused
  * Open orders must have a unique ID whereas orders that have reached a final/terminated status do not have to be unique. 

  
anonymous| false| boolean| Whether or not it is anonymous quote. The default value is `false`. When it is `true` the identity of the quoting party will not be revealed even after the transaction is concluded.  
expireIn| false| integer| Duration of the quote (in secs). [`10`, `120`]. Default: `60`  
quoteBuyList| false| array of objects| Quote direction 

  * In the `Buy` direction, for the maker (the quoting party), the execution direction is the same as the direction of the legs
  * For the taker (the inquiring party) it is opposite direction

  
> category| **true**|  string| Product type: Unified account: `spot`, `linear`,`option`  
> symbol| **true**|  string| Name of the trading contract  
> price| **true**|  string| Quote price  
quoteSellList| false| array of objects| Ask direction 

  * In the `Sell` direction, for the maker (the quoting party), the execution direction is opposite to the direction of the legs
  * For the taker (the inquiring party) it is the same direction

  
> category| **true**|  string| Product type: Unified account: `spot`, `linear`,`option`  
> symbol| **true**|  string| Name of the trading contract  
> price| **true**|  string| Quote price  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
result| object|   
> rfqId| string| Inquiry ID  
> quoteId| string| Quote ID  
> quoteLinkId| string| Custom quote ID  
> expiresAt| string| The quote's expiration time (ms)  
> deskCode| string| Quoter's unique identification code  
> status| string| Status of quotation: `Active` `Canceled` `Filled` `Expired` `Failed`  
  
### Request Example

  * HTTP
  * Python


    
    
    POST /v5/rfq/create-quote HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1744083949347  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 115  
      
    {  
      "rfqId":"1754364447601610516653123084412812",   
      "quoteBuyList": [  
            {  
                "category": "linear",  
                "symbol": "BTCUSDT",  
                "price": "106000"  
            }  
        ],  
        "quoteSellList":[  
            {  
                "category": "linear",  
                "symbol": "BTCUSDT",  
                "price": "126500"  
            }  
        ]  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.create_quote(  
        rfqId="1754364447601610516653123084412812",  
        quoteBuyList=[  
            {  
                "category": "linear",  
                "symbol": "BTCUSDT",  
                "price": "106000"  
            }  
        ],  
        quoteSellList=[  
            {  
                "category": "linear",  
                "symbol": "BTCUSDT",  
                "price": "126500"  
            }  
        ]  
    ))  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "rfqId": "175740578143743543930777169307022",  
            "quoteId": "1757405933130044334361923221559805",  
            "quoteLinkId": "",  
            "expiresAt": "1757405993126",  
            "deskCode": "test0904",  
            "status": "Active"  
        },  
        "retExtInfo": {},  
        "time": 1757405933132  
    }

---

# 報價

建立報價。**每秒最多 50 次請求**

信息

  * 僅支持 UTA2.0 帳戶
  * 無法對自己提出的詢價進行報價
  * 一個請求報價包含兩個方向
  * 至少需傳遞 quoteBuyList 或 quoteSellList
  * 若需進行現貨報價，請先通過 [設置抵押品幣種](/docs/zh-TW/v5/account/set-collateral) 或 [批量設置抵押品幣種](/docs/zh-TW/v5/account/batch-set-collateral) 啟用相應的抵押幣種



### HTTP 請求

POST`/v5/rfq/create-quote`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
rfqId| **true**|  string| 詢價單 ID  
quoteLinkId| false| string| 報價自定義 ID： 

  * 長度應介於 1-32 位 
  * 字母（區分大小寫）與數字的組合，可以是純字母或純數字 
  * 指定 quoteLinkId 僅檢查最近 3 個月的資料 
  * 非終端狀態僅能保證在 24 小時內的唯一性，而終端狀態不保證唯一性 

  
anonymous| false| boolean| 是否為匿名報價，`true` 表示匿名報價，`false` 表示公開報價，預設值為 `false` ，當為 `true` 時，即使交易執行後，身份也不會透露給詢價方。  
expireIn| false| integer| 報價的有效持續時間（以秒為單位）. [`10`, `120`]. 默認: `60`  
quoteBuyList| false| array of objects| 買入方向，報價方向為 `Buy`，對於 maker（報價方），執行方向與 legs 中的方向一致，對於 taker（詢價方）則相反  
> category| true| string| 產品類型：統一帳戶：`spot`, `linear`, `option`  
> symbol| true| string| 交易合約名稱  
> price| true| string| 報價價格  
quoteSellList| false| array of objects| 賣出方向，報價方向為 `Sell`，對於 maker（報價方），執行方向與 legs 中的方向相反，對於 taker（詢價方）則一致  
> category| true| string| 產品類型：統一帳戶：`spot`, `linear`, `option`  
> symbol| true| string| 交易合約名稱  
> price| true| string| 報價價格  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
result| object|   
> rfqId| string| 詢價單 ID  
> quoteId| string| 報價單 ID  
> quoteLinkId| string| 報價自定義 ID  
> expiresAt| string| 報價單的到期時間，為 Unix 時間戳的毫秒格式  
> deskCode| string| 報價方唯一識別碼  
> status| string| 報價單狀態：`Active` `Canceled` `Filled` `Expired` `Failed`  
  
### 請求示例
    
    
    POST /v5/rfq/create-quote HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1744083949347  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 115  
      
    {  
      "rfqId":"1754364447601610516653123084412812",   
      "quoteBuyList": [  
            {  
                "category": "linear",  
                "symbol": "BTCUSDT",  
                "price": "106000"  
            }  
        ],  
        "quoteSellList":[  
            {  
                "category": "linear",  
                "symbol": "BTCUSDT",  
                "price": "126500"  
            }  
        ]  
    }  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "rfqId": "175740578143743543930777169307022",  
            "quoteId": "1757405933130044334361923221559805",  
            "quoteLinkId": "",  
            "expiresAt": "1757405993126",  
            "deskCode": "test0904",  
            "status": "Active"  
        },  
        "retExtInfo": {},  
        "time": 1757405933132  
    }