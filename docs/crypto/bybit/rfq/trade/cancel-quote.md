---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/rfq/trade/cancel-quote
api_type: Trading
updated_at: 2026-08-02 18:53:06.944230
---

# Execute Quote

Execute quote – only for the creator of the RFQ. **Up to 50 requests** per second.

info

This endpoint is asynchronous. You must check the [Get Trade History](/docs/v5/rfq/trade/trade-list) endpoint or listen to the [Execution](/docs/v5/rfq/websocket/private/transaction) WebSocket topic to confirm if the execution was successful.

### HTTP Request

POST`/v5/rfq/execute-quote`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
rfqId| **true**|  string| Inquiry ID  
quoteId| **true**|  string| Quote ID  
quoteSide| **true**|  string| The direction of the quote is `Buy` or `Sell` . When the direction of the quote is `Buy` , for the maker, the execution direction is the same as the direction in legs, and for the taker, it is opposite. Conversely, the same applies  
isHedge| false| boolean| Whether to simultaneously execute the hedge leg in the RFQ. The execution direction is determined by `quoteSide`. Default: `false`  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
result| object|   
> rfqId| string| Inquiry ID  
>rfqLinkId| string|   
> quoteId| string| Quote ID  
> status| string| Order status: 

  * `PendingFill`: Order has been sent to the matching engine but not yet filled.
  * `Failed`: Order failed

  
  
### Request Example

  * HTTP
  * Python


    
    
    POST /v5/rfq/execute-quote HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1744083949347  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 115  
      
     {  
      "rfqId":"1754364447601610516653123084412812",  
      "quoteId": "111",  
      "quoteSide":"Buy"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.execute_quote(  
        rfqId="1754364447601610516653123084412812",  
        quoteId="111",  
        quoteSide="Buy"  
    ))  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "rfqId": "175740700350925204128457980089654",  
            "rfqLinkId": "",  
            "quoteId": "1757407015586174663206671159484665",  
            "status": "PendingFill"  
        },  
        "retExtInfo": {},  
        "time": 1757407058177  
    }

---

# 執行報價

執行報價，僅限詢價單的創建者使用。**每秒最多 50 次請求**

信息

  * 執行成功，只是已經發送撮合，並不能說明訂單已經成交，用戶需要通過査詢介面/v5/rfq/trade-list或監聽toipic:rfq.open.trades來獲取執行結果



### HTTP 請求

POST`/v5/rfq/execute-quote`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
rfqId| **true**|  string| 詢價單 ID  
quoteId| **true**|  string| 報價單 ID  
quoteSide| **true**|  string| 報價方向，`Buy` 或 `Sell` 。當報價方向為 `Buy` 時，對於 maker，執行方向與 legs 中的方向一致，對於 taker 則相反；反之亦然  
isHedge| false| boolean| 是否同時執行詢價單中的 hedge 腿，執行方向取決於 `quoteSide`；預設為 `false`  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
result| object|   
> rfqId| string| 詢價單 ID  
> rfqLinkId| string| 自定義詢價單 ID  
> quoteId| string| 報價單 ID  
> status| string| 訂單狀態： 

  * `PendingFill`：已經發送撮合，待執行，執行結果需要通過査詢/v5/rfq/trade-list獲取或者監聽rfq.open.trades獲取
  * `Failed`：驗證失敗

  
  
### 請求示例
    
    
    POST /v5/rfq/execute-quote HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1744083949347  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 115  
      
     {  
      "rfqId":"1754364447601610516653123084412812",  
      "quoteId": "111",  
      "quoteSide":"Buy"  
    }  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "rfqId": "175740700350925204128457980089654",  
            "rfqLinkId": "",  
            "quoteId": "1757407015586174663206671159484665",  
            "status": "PendingFill"  
        },  
        "retExtInfo": {},  
        "time": 1757407058177  
    }