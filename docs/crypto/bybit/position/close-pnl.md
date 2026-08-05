---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/position/close-pnl
api_type: Position
updated_at: 2026-08-05 19:06:27.249976
---

# Get Closed PnL

Query user's closed profit and loss records

### HTTP Request

GET`/v5/position/closed-pnl`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
[category](/docs/v5/enum#category)| **true**|  string| Product type `linear`(USDT Contract, USDC Contract), `inverse`  
symbol| false| string| Symbol name, like `BTCUSDT`, uppercase only  
startTime| false| integer| The start timestamp (ms) 

  * startTime and endTime are not passed, return 7 days by default
  * Only startTime is passed, return range between startTime and startTime+7 days
  * Only endTime is passed, return range between endTime-7 days and endTime
  * If both are passed, the rule is endTime - startTime <= 7 days

  
endTime| false| integer| The end timestamp (ms)  
limit| false| integer| Limit for data size per page. [`1`, `100`]. Default: `50`  
cursor| false| string| Cursor. Use the `nextPageCursor` token from the response to retrieve the next page of the result set  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
[category](/docs/v5/enum#category)| string| Product type  
list| array| Object  
> symbol| string| Symbol name  
> orderId| string| Order ID  
> side| string| `Buy`, `Sell`  
> qty| string| Order qty  
> orderPrice| string| Order price  
> [orderType](/docs/v5/enum#ordertype)| string| Order type. `Market`,`Limit`  
> execType| string| Exec type  
`Trade`, `BustTrade`  
`SessionSettlePnL`  
`Settle`, `MovePosition`  
`CorporateAction`  
> closedSize| string| Closed size  
> cumEntryValue| string| Cumulated Position value  
> avgEntryPrice| string| Average entry price  
> cumExitValue| string| Cumulated exit position value  
> avgExitPrice| string| Average exit price  
> closedPnl| string| Closed PnL  
> fillCount| string| The number of fills in a single order  
> leverage| string| leverage  
> openFee| string| Open position trading fee  
> closeFee| string| Close position trading fee  
> createdTime| string| The created time (ms)  
> updatedTime| string| The updated time (ms)  
nextPageCursor| string| Refer to the `cursor` request parameter  
[](/docs/api-explorer/v5/position/close-pnl)

* * *

### Request Example

  * HTTP
  * Python
  * Java
  * Node.js


    
    
    GET /v5/position/closed-pnl?category=linear&limit=1 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672284128523  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_closed_pnl(  
        category="linear",  
        limit=1,  
    ))  
    
    
    
    import com.bybit.api.client.domain.*;  
    import com.bybit.api.client.domain.position.*;  
    import com.bybit.api.client.domain.position.request.*;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    var client = BybitApiClientFactory.newInstance().newAsyncPositionRestClient();  
    var closPnlRequest = PositionDataRequest.builder().category(CategoryType.LINEAR).build();  
    client.getClosePnlList(closPnlRequest, System.out::println);  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
        key: 'xxxxxxxxxxxxxxxxxx',  
        secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
        .getClosedPnL({  
            category: 'linear',  
            limit: 1,  
        })  
        .then((response) => {  
            console.log(response);  
        })  
        .catch((error) => {  
            console.error(error);  
        });  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "nextPageCursor": "5a373bfe-188d-4913-9c81-d57ab5be8068%3A1672214887231423699%2C5a373bfe-188d-4913-9c81-d57ab5be8068%3A1672214887231423699",  
            "category": "linear",  
            "list": [  
                {  
                    "symbol": "ETHPERP",  
                    "orderType": "Market",  
                    "leverage": "3",  
                    "updatedTime": "1672214887236",  
                    "side": "Sell",  
                    "orderId": "5a373bfe-188d-4913-9c81-d57ab5be8068",  
                    "closedPnl": "-47.4065323",  
                    "avgEntryPrice": "1194.97516667",  
                    "qty": "3",  
                    "cumEntryValue": "3584.9255",  
                    "createdTime": "1672214887231",  
                    "orderPrice": "1122.95",  
                    "closedSize": "3",  
                    "avgExitPrice": "1180.59833333",  
                    "execType": "Trade",  
                    "fillCount": "4",  
                    "cumExitValue": "3541.795"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1672284129153  
    }

---

# 查詢平倉盈虧

獲取當前用戶的所有平倉盈虧數據，返回結果按照`createdTime`降序排列.

信息

  * 支持查詢過去730天的平倉盈虧紀錄



### HTTP 請求

GET`/v5/position/closed-pnl`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
[category](/docs/zh-TW/v5/enum#category)| **true**|  string| 產品類型 `linear`, `inverse`  
symbol| false| string| 合約名稱  
startTime| false| integer| 開始時間戳 (毫秒) 

  * startTime 和 endTime都不傳入, 則默認返回最近7天的數據
  * startTime 和 endTime都傳入的話, 則確保endTime - startTime <= 7天
  * 若只傳startTime，則查詢startTime和startTime+7天的數據
  * 若只傳endTime，則查詢endTime-7天和endTime的數據

  
endTime| false| integer| 結束時間戳 (毫秒)  
limit| false| integer| 每頁數量限制. [`1`, `100`]. 默認: `50`  
cursor| false| string| 游標，用於翻頁  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
[category](/docs/zh-TW/v5/enum#category)| string| 產品類型  
list| array| Object  
> symbol| string| 合約名稱  
> orderId| string| 訂單Id  
> side| string| 買賣方向 `Buy`, `Side`  
> qty| string| 訂單數量  
> orderPrice| string| 訂單價格  
> [orderType](/docs/zh-TW/v5/enum#ordertype)| string| 訂單類型. `Market`,`Limit`  
> execType| string| 執行類型. `Trade`, `BustTrade`, `SessionSettlePnL`, `Settle`, `MovePosition`, `CorporateAction`  
> closedSize| string| 平倉數量  
> cumEntryValue| string| 被平倉位的累計入場價值  
> avgEntryPrice| string| 平均入場價格  
> cumExitValue| string| 被平倉位的累計出場價值  
> avgExitPrice| string| 平均出場價格  
> closedPnl| string| 被平倉位的盈虧  
> fillCount| string| 成交筆數  
> leverage| string| 持倉槓桿  
> openFee| string| 開倉手續費(平攤)  
> closeFee| string| 平倉手續費(平攤)  
> createdTime| string| 創建時間 (毫秒)  
> updatedTime| string| 更新時間 (毫秒)  
nextPageCursor| string| 游標，用於翻頁  
[](/docs/zh-TW/api-explorer/v5/position/close-pnl)

* * *

### 請求示例

  * HTTP
  * Python
  * Java
  * Node.js


    
    
    GET /v5/position/closed-pnl?category=linear&limit=1 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672284128523  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_closed_pnl(  
        category="linear",  
        limit=1,  
    ))  
    
    
    
    import com.bybit.api.client.domain.*;  
    import com.bybit.api.client.domain.position.*;  
    import com.bybit.api.client.domain.position.request.*;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    var client = BybitApiClientFactory.newInstance().newAsyncPositionRestClient();  
    var closPnlRequest = PositionDataRequest.builder().category(CategoryType.LINEAR).build();  
    client.getClosePnlList(closPnlRequest, System.out::println);  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
        key: 'xxxxxxxxxxxxxxxxxx',  
        secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
        .getClosedPnL({  
            category: 'linear',  
            limit: 1,  
        })  
        .then((response) => {  
            console.log(response);  
        })  
        .catch((error) => {  
            console.error(error);  
        });  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "nextPageCursor": "5a373bfe-188d-4913-9c81-d57ab5be8068%3A1672214887231423699%2C5a373bfe-188d-4913-9c81-d57ab5be8068%3A1672214887231423699",  
            "category": "linear",  
            "list": [  
                {  
                    "symbol": "ETHPERP",  
                    "orderType": "Market",  
                    "leverage": "3",  
                    "updatedTime": "1672214887236",  
                    "side": "Sell",  
                    "orderId": "5a373bfe-188d-4913-9c81-d57ab5be8068",  
                    "closedPnl": "-47.4065323",  
                    "avgEntryPrice": "1194.97516667",  
                    "qty": "3",  
                    "cumEntryValue": "3584.9255",  
                    "createdTime": "1672214887231",  
                    "orderPrice": "1122.95",  
                    "closedSize": "3",  
                    "avgExitPrice": "1180.59833333",  
                    "execType": "Trade",  
                    "fillCount": "4",  
                    "cumExitValue": "3541.795"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1672284129153  
    }