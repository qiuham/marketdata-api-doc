---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/market/open-interest
api_type: Market Data
updated_at: 2026-10-31 18:34:54.086125
---

# Get Orderbook

Query for orderbook depth data.

> **Covers: Spot / USDT contract / USDC contract / Inverse contract / Option**

  * Contract: 1000-level of orderbook data
  * Spot: 1000-level of orderbook data
  * Option: 25-level of orderbook data



info

  * The response is in the snapshot format.
  * [Retail Price Improvement (RPI)](https://www.bybit.com/en/help-center/article/Retail-Price-Improvement-RPI-Order) orders will not be included in the response message and will not be visible over API.



### HTTP Request

GET`/v5/market/orderbook`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
[category](/docs/v5/enum#category)| **true**|  string| Product type. `spot`, `linear`, `inverse`, `option`  
symbol| **true**|  string| Symbol name, like `BTCUSDT`, uppercase only  
limit| false| integer| Limit size for each bid and ask

  * `spot`: [`1`, `1000`]. Default: `1`.
  * `linear`&`inverse`: [`1`, `1000`]. Default: `25`.
  * `option`: [`1`, `25`]. Default: `1`.

  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
s| string| Symbol name  
b| array| Bid, buyer. Sorted by price in descending order  
> b[0]| string| Bid price  
> b[1]| string| Bid size  
a| array| Ask, seller. Sorted by price in ascending order  
> a[0]| string| Ask price  
> a[1]| string| Ask size  
ts| integer| The timestamp (ms) that the system generates the data  
u| integer| Update ID, is always in sequence

  * For contract, corresponds to `u` in the 1000-level [WebSocket orderbook stream](https://bybit-exchange.github.io/docs/v5/websocket/public/orderbook)
  * For spot, corresponds to `u` in the 1000-level [WebSocket orderbook stream](https://bybit-exchange.github.io/docs/v5/websocket/public/orderbook)

  
seq| integer| Cross sequence 

  * You can use this field to compare different levels orderbook data, and for the smaller seq, then it means the data is generated earlier. 

  
cts| integer| The timestamp from the matching engine when this orderbook data is produced. It can be correlated with `T` from [public trade channel](/docs/v5/websocket/public/trade)  
[](/docs/api-explorer/v5/market/orderbook)

* * *

### Request Example

  * HTTP
  * Python
  * Go
  * Java
  * Node.js


    
    
    GET /v5/market/orderbook?category=spot&symbol=BTCUSDT HTTP/1.1  
    Host: api-testnet.bybit.com  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(testnet=True)  
    print(session.get_orderbook(  
        category="linear",  
        symbol="BTCUSDT",  
    ))  
    
    
    
    import (  
        "context"  
        "fmt"  
        bybit "github.com/bybit-exchange/bybit.go.api"  
    )  
    client := bybit.NewBybitHttpClient("", "", bybit.WithBaseURL(bybit.TESTNET))  
    params := map[string]interface{}{"category": "spot", "symbol": "BTCUSDT"}  
    client.NewUtaBybitServiceWithParams(params).GetOrderBookInfo(context.Background())  
    
    
    
    import com.bybit.api.client.domain.CategoryType;  
    import com.bybit.api.client.domain.market.*;  
    import com.bybit.api.client.domain.market.request.MarketDataRequest;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    var client = BybitApiClientFactory.newInstance().newAsyncMarketDataRestClient();  
    var orderbookRequest = MarketDataRequest.builder().category(CategoryType.SPOT).symbol("BTCUSDT").build();  
    client.getMarketOrderBook(orderbookRequest,System.out::println);  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
    });  
      
    client  
        .getOrderbook({  
            category: 'linear',  
            symbol: 'BTCUSDT',  
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
            "s": "BTCUSDT",  
            "a": [  
                [  
                    "65557.7",  
                    "16.606555"  
                ]  
            ],  
            "b": [  
                [  
                    "65485.47",  
                    "47.081829"  
                ]  
            ],  
            "ts": 1716863719031,  
            "u": 230704,  
            "seq": 1432604333,  
            "cts": 1716863718905  
        },  
        "retExtInfo": {},  
        "time": 1716863719382  
    }

---

# Order Book (深度)

獲取深度數據

> **覆蓋範圍: 現貨 / USDT永續 / USDT交割 / USDC永續 / USDC交割 / 反向合約 / 期權**

  * 期貨: 最多返回1000檔的數據.
  * 現貨: 最多返回1000檔的數據.
  * 期權: 僅返回25檔的數據.



提示

響應是當前時間的切片數據

### HTTP請求

GET`/v5/market/orderbook`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
[category](/docs/zh-TW/v5/enum#category)| **true**|  string| 產品類型. `spot`, `linear`, `inverse`, `option`  
[symbol](/docs/zh-TW/v5/enum#symbol)| **true**|  string| 合約名稱  
limit| false| integer| 深度限制.

  * `spot`: [`1`, `1000`], 默認: `1`.
  * `linear`&`inverse`: [`1`, `1000`],默認: `25`.
  * `option`: [`1`, `25`],默認: `1`.

  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
s| string| 合約名稱  
b| array| Bid, 買方. 按照價格從大到小  
> b[0]| string| 買方報價  
> b[1]| string| 買方數量  
a| array| Ask, 賣方. 按照價格從小到大  
> a[0]| string| 賣方報價  
> a[1]| string| 賣方數量  
ts| integer| 行情服務生成數據時間戳（毫秒）  
u| integer| 表示數據連續性的id. 

  * 對於期貨, 它和wss推送裡的1000檔的`u`對齊
  * 對於現貨, 它和wss推送裡的1000檔的`u`對齊

  
seq| integer| 撮合版本號 

  * 該字段可以用於關聯不同檔位的orderbook, 如果值越小, 則說明數據生成越早

  
cts| number| 產生此訂單簿數據時來自撮合引擎的時間戳. 可用於與[平台成交](/docs/zh-TW/v5/websocket/public/trade)頻道中的`T`進行關聯  
[](/docs/zh-TW/api-explorer/v5/market/orderbook)

* * *

### 請求示例

  * HTTP
  * Python
  * Go
  * Java
  * Node.js


    
    
    GET /v5/market/orderbook?category=spot&symbol=BTCUSDT HTTP/1.1  
    Host: api-testnet.bybit.com  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(testnet=True)  
    print(session.get_orderbook(  
        category="linear",  
        symbol="BTCUSDT",  
    ))  
    
    
    
    import (  
        "context"  
        "fmt"  
        bybit "github.com/bybit-exchange/bybit.go.api"  
    )  
    client := bybit.NewBybitHttpClient("", "", bybit.WithBaseURL(bybit.TESTNET))  
    params := map[string]interface{}{"category": "spot", "symbol": "BTCUSDT"}  
    client.NewUtaBybitServiceWithParams(params).GetOrderBookInfo(context.Background())  
    
    
    
    import com.bybit.api.client.domain.CategoryType;  
    import com.bybit.api.client.domain.market.*;  
    import com.bybit.api.client.domain.market.request.MarketDataRequest;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    var client = BybitApiClientFactory.newInstance().newAsyncMarketDataRestClient();  
    var orderbookRequest = MarketDataRequest.builder().category(CategoryType.SPOT).symbol("BTCUSDT").build();  
    client.getMarketOrderBook(orderbookRequest,System.out::println);  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
    });  
      
    client  
        .getOrderbook({  
            category: 'linear',  
            symbol: 'BTCUSDT',  
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
            "s": "BTCUSDT",  
            "a": [  
                [  
                    "65557.7",  
                    "16.606555"  
                ]  
            ],  
            "b": [  
                [  
                    "65485.47",  
                    "47.081829"  
                ]  
            ],  
            "ts": 1716863719031,  
            "u": 230704,  
            "seq": 1432604333,  
            "cts": 1716863718905  
        },  
        "retExtInfo": {},  
        "time": 1716863719382  
    }