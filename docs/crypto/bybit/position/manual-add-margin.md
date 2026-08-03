---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/position/manual-add-margin
api_type: Position
updated_at: 2026-08-03 19:08:19.212479
---

# Move Position

You can move positions between sub-master, master-sub, or sub-sub UIDs when necessary

info

  * The endpoint can only be called by master UID api key
  * UIDs must be the same master-sub account relationship
  * The trades generated from move-position endpoint will not be displayed in the Recent Trade (Rest API & Websocket)
  * There is no trading fee
  * `fromUid` and `toUid` both should be Unified trading accounts, and they need to be one-way mode when moving the positions
  * Please note that once executed, you will get execType=`MovePosition` entry from [Get Trade History](/docs/v5/order/execution), [Get Closed Pnl](/docs/v5/position/close-pnl), and stream from [Execution](/docs/v5/websocket/private/execution).
  * Not available for TradFi perpetual contracts, including forex, stock, and commodities



### HTTP Request

POST`/v5/position/move-positions`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
fromUid| **true**|  string| From UID 

  * Must be UTA
  * Must be in one-way mode for Futures

  
toUid| **true**|  string| To UID 

  * Must be UTA
  * Must be in one-way mode for Futures

  
list| **true**|  array| Object. Up to 25 legs per request  
> [category](/docs/v5/enum#category)| **true**|  string| Product type `linear`, `spot`, `option`,`inverse`  
> symbol| **true**|  string| Symbol name, like `BTCUSDT`, uppercase only  
> price| **true**|  string| Trade price 

  * `linear`&`inverse`: the price needs to be between [95% of mark price, 105% of mark price]
  * `spot`&`option`: the price needs to follow the price rule from [Instruments Info](/docs/v5/market/instrument)

  
> side| **true**|  string| Trading side of `fromUid`

  * For example, `fromUid` has a long position, when side=`Sell`, then once executed, the position of `fromUid` will be reduced or open a short position depending on `qty` input

  
> qty| **true**|  string| Executed qty 

  * The value must satisfy the qty rule from [Instruments Info](/docs/v5/market/instrument), in particular, category=`linear` is able to input `maxOrderQty` * 5

  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
retCode| integer| Result code. `0` means request is successfully accepted  
retMsg| string| Result message  
result| map| Object  
> blockTradeId| string| Block trade ID  
> status| string| Status. `Processing`, `Rejected`  
> rejectParty| string| 

  * `""` means initial validation is passed, please check the order status via [Get Move Position History](/docs/v5/position/move-position-history)
  * `Taker`, `Maker` when status=`Rejected`
  * `bybit` means error is occurred on the Bybit side

  
  
### Request Example

  * HTTP
  * Python
  * Java
  * Node.js


    
    
    POST /v5/position/move-positions HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1697447928051  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "fromUid": "100307601",  
        "toUid": "592324",  
        "list": [  
            {  
                "category": "spot",  
                "symbol": "BTCUSDT",  
                "price": "100",  
                "side": "Sell",  
                "qty": "0.01"  
            }  
        ]  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.move_position(  
        fromUid="100307601",  
        toUid="592324",  
        list=[  
            {  
                "category": "spot",  
                "symbol": "BTCUSDT",  
                "price": "100",  
                "side": "Sell",  
                "qty": "0.01",  
            }  
        ]  
    ))  
    
    
    
    import com.bybit.api.client.domain.*;  
    import com.bybit.api.client.domain.position.*;  
    import com.bybit.api.client.domain.position.request.*;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    var client = BybitApiClientFactory.newInstance().newAsyncPositionRestClient();  
    var movePositionsRequest = Arrays.asList(MovePositionDetailsRequest.builder().category(CategoryType.SPOT.getCategoryTypeId()).symbol("BTCUSDT").side(Side.SELL.getTransactionSide()).price("100").qty("0.01").build(),  
                    MovePositionDetailsRequest.builder().category(CategoryType.SPOT.getCategoryTypeId()).symbol("ETHUSDT").side(Side.SELL.getTransactionSide()).price("100").qty("0.01").build());  
    var batchMovePositionsRequest = BatchMovePositionRequest.builder().fromUid("123456").toUid("456789").list(movePositionsRequest).build();  
    System.out.println(client.batchMovePositions(batchMovePositionsRequest));  
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "blockTradeId": "e9bb926c95f54cf1ba3e315a58b8597b",  
            "status": "Processing",  
            "rejectParty": ""  
        }  
    }

---

# 移倉

您可以在同一個母子帳戶體系下移動期貨、期權的倉位, 以及現貨的幣幣交易

信息

  * 該接口僅支持母帳戶的api key訪問
  * 移倉間的UID和調用者的UID必須是同一個母子帳戶體系
  * 該移倉生成的交易將不會出現在公有行情的成交中(包括Rest API和Websocket)
  * 該操作不會產生手續費
  * `fromUid` 和 `toUid`都必須是統一交易帳戶, 並且對於期貨而言, 倉位需要處於單向模式下
  * 請注意一旦成交, [查詢成交紀錄](/docs/zh-TW/v5/order/execution), [查詢平倉盈虧](/docs/zh-TW/v5/position/close-pnl), 以及私有推送[成交](/docs/zh-TW/v5/websocket/private/execution)會返回execType=`MovePosition`的數據
  * 不支持 TradFi 永續合約，包括外匯、股票及大宗商品



### HTTP 請求

POST`/v5/position/move-positions`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
fromUid| **true**|  string| 原UID 

  * 必須是統一交易帳戶
  * 期貨倉位必須有處於單向持倉模式

  
toUid| **true**|  string| 目標UID 

  * 必須是統一交易帳戶
  * 期貨倉位必須有處於單向持倉模式

  
list| **true**|  array| Object. 單次請求最多支持25腿  
> [category](/docs/zh-TW/v5/enum#category)| **true**|  string| 產品類型 `linear`, `spot`, `option`,`inverse`  
> symbol| **true**|  string| 合約名稱/幣對名  
> price| **true**|  string| 訂單價格 

  * `linear`和`inverse`: 價格需要位於[95% _標記價格, 105%_ 標記價格]之間
  * `spot`和`option`: 價格需要遵循[查詢可交易產品的規格信息](/docs/zh-TW/v5/market/instrument)的價格上下限和精度

  
> side| **true**|  string| 是`fromUid`的交易方向 

  * 例如, `fromUid`持有多倉, 如果選擇side=`Sell`, 則執行後, `fromUid`的多倉會被減倉或者開了空倉取決於`qty`的大小

  
> qty| **true**|  string| 交易數量

  * 該數字需要滿足[查詢可交易產品的規格信息](/docs/zh-TW/v5/market/instrument)的qty規則, 特別的, 對於linear, 可以支持5倍的`maxOrderQty`

  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
retCode| integer| 響應碼. `0`表示請求被成功接受  
retMsg| string| 響應信息  
result| map| Object  
> blockTradeId| string| 大宗交易訂單ID  
> status| string| 訂單狀態. `Processing`, `Rejected`  
> rejectParty| string| 

  * `""`表示初始校驗通過, 需要進一步通過[查詢移倉歷史](/docs/zh-TW/v5/position/move-position-history)接口來確認最終狀態
  * `Taker`, `Maker`: 當status=`Rejected`返回
  * `bybit`表示處理過程中的錯誤發生在Bybit側

  
  
### 請求示例

  * HTTP
  * Python
  * Java
  * Node.js


    
    
    POST /v5/position/move-positions HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1697447928051  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "fromUid": "100307601",  
        "toUid": "592324",  
        "list": [  
            {  
                "category": "spot",  
                "symbol": "BTCUSDT",  
                "price": "100",  
                "side": "Sell",  
                "qty": "0.01"  
            }  
        ]  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.move_position(  
        fromUid="100307601",  
        toUid="592324",  
        list=[  
            {  
                "category": "spot",  
                "symbol": "BTCUSDT",  
                "price": "100",  
                "side": "Sell",  
                "qty": "0.01",  
            }  
        ]  
    ))  
    
    
    
    import com.bybit.api.client.domain.*;  
    import com.bybit.api.client.domain.position.*;  
    import com.bybit.api.client.domain.position.request.*;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    var client = BybitApiClientFactory.newInstance().newAsyncPositionRestClient();  
    var movePositionsRequest = Arrays.asList(MovePositionDetailsRequest.builder().category(CategoryType.SPOT.getCategoryTypeId()).symbol("BTCUSDT").side(Side.SELL.getTransactionSide()).price("100").qty("0.01").build(),  
                    MovePositionDetailsRequest.builder().category(CategoryType.SPOT.getCategoryTypeId()).symbol("ETHUSDT").side(Side.SELL.getTransactionSide()).price("100").qty("0.01").build());  
    var batchMovePositionsRequest = BatchMovePositionRequest.builder().fromUid("123456").toUid("456789").list(movePositionsRequest).build();  
    System.out.println(client.batchMovePositions(batchMovePositionsRequest));  
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "blockTradeId": "e9bb926c95f54cf1ba3e315a58b8597b",  
            "status": "Processing",  
            "rejectParty": ""  
        }  
    }