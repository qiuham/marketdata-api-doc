---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/position/leverage
api_type: Position
updated_at: 2026-09-24 18:47:25.073806
---

# Get Move Position History

You can query moved position data by master UID api key

### HTTP Request

GET`/v5/position/move-history`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
[category](/docs/v5/enum#category)| false| string| Product type `linear`, `inverse`, `spot`, `option`  
symbol| false| string| Symbol name, like `BTCUSDT`, uppercase only  
startTime| false| number| The order creation start timestamp. The interval is 7 days  
endTime| false| number| The order creation end timestamp. The interval is 7 days  
status| false| string| Order status. `Processing`, `Filled`, `Rejected`  
blockTradeId| false| string| Block trade ID  
limit| false| string| Limit for data size per page. [`1`, `200`]. Default: `20`  
cursor| false| string| Cursor. Use the `nextPageCursor` token from the response to retrieve the next page of the result set  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array| Object  
> blockTradeId| string| Block trade ID  
> [category](/docs/v5/enum#category)| string| Product type. `linear`, `spot`, `option`  
> orderId| string| Bybit order ID  
> userId| integer| User ID  
> symbol| string| Symbol name  
> side| string| Order side from taker's perspective. `Buy`, `Sell`  
> price| string| Order price  
> qty| string| Order quantity  
> execFee| string| The fee for taker or maker in the base currency paid to the Exchange executing the block trade  
> status| string| Block trade status. `Processing`, `Filled`, `Rejected`  
> execId| string| The unique trade ID from the exchange  
> resultCode| integer| The result code of the order. `0` means success  
> resultMessage| string| The error message. `""` when resultCode=0  
> createdAt| number| The timestamp (ms) when the order is created  
> updatedAt| number| The timestamp (ms) when the order is updated  
> rejectParty| string| 

  * `""` means the status=`Filled`
  * `Taker`, `Maker` when status=`Rejected`
  * `bybit` means error is occurred on the Bybit side

  
nextPageCursor| string| Used to get the next page data  
  
### Request Example

  * HTTP
  * Python
  * Java
  * Node.js


    
    
    GET /v5/position/move-history?limit=1&status=Filled HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1697523024244  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_move_position_history(  
        limit="1",  
        status="Filled",  
    ))  
    
    
    
    import com.bybit.api.client.domain.*;  
    import com.bybit.api.client.domain.position.*;  
    import com.bybit.api.client.domain.position.request.*;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    var client = BybitApiClientFactory.newInstance().newAsyncPositionRestClient();  
    var movePositionsHistoryRequest = PositionDataRequest.builder().category(CategoryType.LINEAR).symbol("BTCUSDT").status(MovePositionStatus.Processing).build();  
    System.out.println(client.getMovePositionHistory(movePositionsHistoryRequest));  
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "list": [  
                {  
                    "blockTradeId": "1a82e5801af74b67b7ad71ba00a7391a",  
                    "category": "option",  
                    "orderId": "8e09c5b8-f651-4cec-968d-52764cac11ec",  
                    "userId": 592324,  
                    "symbol": "BTC-14OCT23-27000-C",  
                    "side": "Buy",  
                    "price": "6",  
                    "qty": "0.99",  
                    "execFee": "0",  
                    "status": "Filled",  
                    "execId": "677ad344-6bb4-4ace-baca-128fcffcaca7",  
                    "resultCode": 0,  
                    "resultMessage": "",  
                    "createdAt": 1697186522865,  
                    "updatedAt": 1697186523289,  
                    "rejectParty": ""  
                }  
            ],  
            "nextPageCursor": "page_token%3D1241742%26"  
        },  
        "retExtInfo": {},  
        "time": 1697523024386  
    }

---

# 查詢移倉歷史

您可以通過使用母帳戶的api key查詢過去的移倉歷史紀錄

### HTTP 請求

GET`/v5/position/move-history`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
[category](/docs/zh-TW/v5/enum#category)| false| string| 產品類型 `linear`, `spot`, `option`, `inverse`  
symbol| false| string| 合約名稱/幣對名  
startTime| false| number| 創建訂單的開始時間戳 (毫秒), `startTime`和`endTime`的時間範圍是7天  
endTime| false| number| 創建訂單的結束時間戳 (毫秒), `startTime`和`endTime`的時間範圍是7天  
status| false| string| Order status. `Processing`, `Filled`, `Rejected`  
blockTradeId| false| string| 大宗交易訂單ID  
limit| false| string| 每頁數量限制. [`1`, `200`]. 默認: `20`  
cursor| false| string| 游標，用於翻頁. 請使用響應中的`nextPageCursor`的獲得下一頁  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
list| array| Object  
> blockTradeId| string| 大宗交易ID  
> [category](/docs/zh-TW/v5/enum#category)| string| 產品類型

  * [統一帳戶2.0](/docs/zh-TW/v5/acct-mode#%E7%B5%B1%E4%B8%80%E5%B8%B3%E6%88%B620), [統一帳戶1.0](/docs/zh-TW/v5/acct-mode#%E7%B5%B1%E4%B8%80%E5%B8%B3%E6%88%B610): `linear`, `spot`, `option`

  
> orderId| string| Bybit側的訂單ID  
> userId| integer| 用戶ID  
> symbol| string| 合約名稱  
> side| string| 從taker角度看的訂單方向. `Buy`, `Sell`  
> price| string| 訂單價格  
> qty| string| 訂單數量  
> execFee| string| 成交費用  
> status| string| 大宗交易訂單狀態. `Processing`, `Filled`, `Rejected`  
> execId| string| 交易所側的成交ID  
> resultCode| integer| 錯誤碼. `0`表示成功  
> resultMessage| string| 錯誤信息. 當resultCode=0時, 則返回`""`  
> createdAt| number| 訂單創建時間戳 (毫秒)  
> updatedAt| number| 訂單更新時間戳 (毫秒)  
> rejectParty| string| 

  * `""`表示初始校驗通過, 需要進一步通過[查詢移倉歷史](/docs/zh-TW/v5/position/move-position-history)接口來確認最終狀態
  * `Taker`, `Maker`: 當status=`Rejected`返回
  * `bybit`表示處理過程中的錯誤發生在Bybit側

  
nextPageCursor| string| 游標, 用於翻下一頁  
  
### 請求示例

  * HTTP
  * Python
  * Java
  * Node.js


    
    
    GET /v5/position/move-history?limit=1&status=Filled HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1697523024244  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_move_position_history(  
        limit="1",  
        status="Filled",  
    ))  
    
    
    
    import com.bybit.api.client.domain.*;  
    import com.bybit.api.client.domain.position.*;  
    import com.bybit.api.client.domain.position.request.*;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    var client = BybitApiClientFactory.newInstance().newAsyncPositionRestClient();  
    var movePositionsHistoryRequest = PositionDataRequest.builder().category(CategoryType.LINEAR).symbol("BTCUSDT").status(MovePositionStatus.Processing).build();  
    System.out.println(client.getMovePositionHistory(movePositionsHistoryRequest));  
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "list": [  
                {  
                    "blockTradeId": "1a82e5801af74b67b7ad71ba00a7391a",  
                    "category": "option",  
                    "orderId": "8e09c5b8-f651-4cec-968d-52764cac11ec",  
                    "userId": 592324,  
                    "symbol": "BTC-14OCT23-27000-C",  
                    "side": "Buy",  
                    "price": "6",  
                    "qty": "0.99",  
                    "execFee": "0",  
                    "status": "Filled",  
                    "execId": "677ad344-6bb4-4ace-baca-128fcffcaca7",  
                    "resultCode": 0,  
                    "resultMessage": "",  
                    "createdAt": 1697186522865,  
                    "updatedAt": 1697186523289,  
                    "rejectParty": ""  
                }  
            ],  
            "nextPageCursor": "page_token%3D1241742%26"  
        },  
        "retExtInfo": {},  
        "time": 1697523024386  
    }