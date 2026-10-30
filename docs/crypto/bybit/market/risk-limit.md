---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/market/risk-limit
api_type: Market Data
updated_at: 2026-10-30 18:36:35.040321
---

# Get Tickers

Query for the latest price snapshot, best bid/ask price, and trading volume in the last 24 hours.

> **Covers: Spot / USDT contract / USDC contract / Inverse contract / Option**

info

If category=_option_ , `symbol` or `baseCoin` must be passed.

### HTTP Request

GET`/v5/market/tickers`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
[category](/docs/v5/enum#category)| **true**|  string| Product type. `spot`,`linear`,`inverse`,`option`  
[symbol](/docs/v5/enum#symbol)| false| string| Symbol name, like `BTCUSDT`, uppercase only  
baseCoin| false| string| Base coin, uppercase only. Apply to `option` **only**  
expDate| false| string| Expiry date. e.g., 25DEC22. Apply to `option` **only**  
  
### Response Parameters

  * Linear/Inverse
  * Option
  * Spot



Parameter| Type| Comments  
---|---|---  
category| string| Product type  
list| array| Object  
> symbol| string| Symbol name   
> lastPrice| string| Last price   
> indexPrice| string| Index price   
> markPrice| string| Mark price   
> prevPrice24h| string| Market price 24 hours ago   
> price24hPcnt| string| Percentage change of market price relative to 24h   
> highPrice24h| string| The highest price in the last 24 hours   
> lowPrice24h| string| The lowest price in the last 24 hours   
> prevPrice1h| string| Market price an hour ago   
> openInterest| string| Open interest size (both sides)   
> openInterestValue| string| Open interest value (both sides)  
> singleOpenInterest| string| Open interest size (single side)  
> singleOpenInterestValue| string| Open interest value (single side)  
> turnover24h| string| Turnover for 24h   
> volume24h| string| Volume for 24h   
> fundingRate| string| Funding rate   
> nextFundingTime| string| Next funding time (ms)   
> predictedDeliveryPrice| string| Predicated delivery price. It has a value 30 mins before delivery   
> basisRate| string| Basis rate   
> basis| string| Basis   
> deliveryFeeRate| string| Delivery fee rate   
> deliveryTime| string| Delivery timestamp (ms), applicable to expiry futures only  
> ask1Size| string| Best ask size   
> bid1Price| string| Best bid price   
> ask1Price| string| Best ask price   
> bid1Size| string| Best bid size   
> preOpenPrice| string| Estimated pre-market contract open price 

  * Meaningless once the market opens

  
> preQty| string| Estimated pre-market contract open qty 

  * The value is meaningless once the market opens

  
> [curPreListingPhase](/docs/v5/enum#curauctionphase)| string| The current pre-market contract phase   
> fundingIntervalHour| string| Funding interval hour

  * This value currently only supports whole hours

  
> fundingCap| string| Funding rate upper and lower limits  
> basisRateYear| string| Annual basis rate

  * Only for Futures,For Perpetual,it will return ""

  
  
Parameter| Type| Comments  
---|---|---  
category| string| Product type  
list| array| Object  
> symbol| string| Symbol name   
> bid1Price| string| Best bid price   
> bid1Size| string| Best bid size   
> bid1Iv| string| Best bid iv   
> ask1Price| string| Best ask price   
> ask1Size| string| Best ask size   
> ask1Iv| string| Best ask iv   
> lastPrice| string| Last price   
> highPrice24h| string| The highest price in the last 24 hours   
> lowPrice24h| string| The lowest price in the last 24 hours   
> markPrice| string| Mark price   
> indexPrice| string| Index price   
> markIv| string| Mark price iv   
> underlyingPrice| string| Underlying price   
> openInterest| string| Open interest size   
> turnover24h| string| Turnover for 24h   
> volume24h| string| Volume for 24h   
> totalVolume| string| Total volume   
> totalTurnover| string| Total turnover   
> delta| string| Delta   
> gamma| string| Gamma   
> vega| string| Vega   
> theta| string| Theta   
> predictedDeliveryPrice| string| Predicated delivery price. It has a value 30 mins before delivery   
> change24h| string| The change in the last 24 hous   
  
Parameter| Type| Comments  
---|---|---  
category| string| Product type  
list| array| Object  
> symbol| string| Symbol name   
> bid1Price| string| Best bid price   
> bid1Size| string| Best bid size   
> ask1Price| string| Best ask price   
> ask1Size| string| Best ask size   
> lastPrice| string| Last price   
> prevPrice24h| string| Market price 24 hours ago   
> price24hPcnt| string| Percentage change of market price relative to 24h   
> highPrice24h| string| The highest price in the last 24 hours   
> lowPrice24h| string| The lowest price in the last 24 hours   
> turnover24h| string| Turnover for 24h   
> volume24h| string| Volume for 24h   
> usdIndexPrice| string| USD index price 

  * used to calculate USD value of the assets in Unified account
  * non-collateral margin coin returns ""
  * Only those trading pairs like "XXX/USDT" or "XXX/USDC" have the value

  
  
[](/docs/api-explorer/v5/market/tickers)

* * *

### Request Example

  * Inverse
  * Option
  * Spot



  * HTTP
  * Python
  * Go
  * Java
  * Node.js


    
    
    GET /v5/market/tickers?category=inverse&symbol=BTCUSD HTTP/1.1  
    Host: api-testnet.bybit.com  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(testnet=True)  
    print(session.get_tickers(  
        category="inverse",  
        symbol="BTCUSD",  
    ))  
    
    
    
    import (  
        "context"  
        "fmt"  
        bybit "github.com/bybit-exchange/bybit.go.api"  
    )  
    client := bybit.NewBybitHttpClient("", "", bybit.WithBaseURL(bybit.TESTNET))  
    params := map[string]interface{}{"category": "inverse", "symbol": "BTCUSD"}  
    client.NewUtaBybitServiceWithParams(params).GetMarketTickers(context.Background())  
    
    
    
    import com.bybit.api.client.domain.CategoryType;  
    import com.bybit.api.client.domain.market.*;  
    import com.bybit.api.client.domain.market.request.MarketDataRequest;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    var client = BybitApiClientFactory.newInstance().newAsyncMarketDataRestClient();  
    var tickerReueqt = MarketDataRequest.builder().category(CategoryType.INVERSE).symbol("BTCUSD").build();  
    client.getMarketTickers(tickerReueqt, System.out::println);  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
    });  
      
    client  
        .getTickers({  
            category: 'inverse',  
            symbol: 'BTCUSDT',  
        })  
        .then((response) => {  
            console.log(response);  
        })  
        .catch((error) => {  
            console.error(error);  
        });  
    

  * HTTP
  * Python
  * Go
  * Java
  * Node.js


    
    
    GET /v5/market/tickers?category=option&symbol=BTC-30DEC22-18000-C HTTP/1.1  
    Host: api-testnet.bybit.com  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(testnet=True)  
    print(session.get_tickers(  
        category="option",  
        symbol="BTC-30DEC22-18000-C",  
    ))  
    
    
    
    import (  
        "context"  
        "fmt"  
        bybit "github.com/bybit-exchange/bybit.go.api"  
    )  
    client := bybit.NewBybitHttpClient("", "", bybit.WithBaseURL(bybit.TESTNET))  
    params := map[string]interface{}{"category": "option", "symbol": "BTC-30DEC22-18000-C"}  
    client.NewUtaBybitServiceWithParams(params).GetMarketTickers(context.Background())  
    
    
    
    import com.bybit.api.client.domain.CategoryType;  
    import com.bybit.api.client.domain.market.*;  
    import com.bybit.api.client.domain.market.request.MarketDataRequest;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    var client = BybitApiClientFactory.newInstance().newAsyncMarketDataRestClient();  
    var tickerReueqt = MarketDataRequest.builder().category(CategoryType.OPTION).symbol("BTC-30DEC22-18000-C").build();  
    client.getMarketTickers(tickerReueqt, System.out::println);  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
    });  
      
    client  
      .getTickers({  
        category: 'option',  
        symbol: 'BTC-30DEC22-18000-C',  
      })  
      .then((response) => {  
        console.log(response);  
      })  
      .catch((error) => {  
        console.error(error);  
      });  
    

  * HTTP
  * Python
  * GO
  * Java
  * Node.js


    
    
    GET /v5/market/tickers?category=spot&symbol=BTCUSDT HTTP/1.1  
    Host: api-testnet.bybit.com  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(testnet=True)  
    print(session.get_tickers(  
        category="spot",  
        symbol="BTCUSDT",  
    ))  
    
    
    
    import (  
        "context"  
        "fmt"  
        bybit "github.com/bybit-exchange/bybit.go.api"  
    )  
    client := bybit.NewBybitHttpClient("", "", bybit.WithBaseURL(bybit.TESTNET))  
    params := map[string]interface{}{"category": "spot", "symbol": "BTCUSDT"}  
    client.NewUtaBybitServiceWithParams(params).GetMarketTickers(context.Background())  
    
    
    
    import com.bybit.api.client.domain.*;  
    import com.bybit.api.client.domain.market.*;  
    import com.bybit.api.client.domain.market.request.*;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    var client = BybitApiClientFactory.newInstance().newAsyncMarketDataRestClient();  
    var tickerReueqt = MarketDataRequest.builder().category(CategoryType.SPOT).symbol("BTCUSDT").build();  
    client.getMarketTickers(tickerReueqt, System.out::println);  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
    });  
      
    client  
      .getTickers({  
        category: 'spot',  
        symbol: 'BTCUSDT',  
      })  
      .then((response) => {  
        console.log(response);  
      })  
      .catch((error) => {  
        console.error(error);  
      });  
    

### Response Example

  * Inverse
  * Option
  * Spot


    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "category": "inverse",  
            "list": [  
                {  
                    "symbol": "BTCUSD",  
                    "lastPrice": "120635.50",  
                    "indexPrice": "114890.92",  
                    "markPrice": "114898.43",  
                    "prevPrice24h": "105595.90",  
                    "price24hPcnt": "0.142425",  
                    "highPrice24h": "131309.30",  
                    "lowPrice24h": "102007.60",  
                    "prevPrice1h": "119806.10",  
                    "openInterest": "240113967",  
                    "openInterestValue": "2089.79",  
                    "turnover24h": "115.6907",  
                    "volume24h": "13713832.0000",  
                    "fundingRate": "0.0001",  
                    "nextFundingTime": "1760371200000",  
                    "predictedDeliveryPrice": "",  
                    "basisRate": "",  
                    "deliveryFeeRate": "",  
                    "deliveryTime": "0",  
                    "ask1Size": "9854",  
                    "bid1Price": "103401.00",  
                    "ask1Price": "109152.80",  
                    "bid1Size": "1063",  
                    "basis": "",  
                    "preOpenPrice": "",  
                    "preQty": "",  
                    "curPreListingPhase": "",  
                    "fundingIntervalHour": "8",  
                    "basisRateYear": "",  
                    "fundingCap": "0.005"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1760352369814  
    }  
    
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "category": "option",  
            "list": [  
                {  
                    "symbol": "BTC-30DEC22-18000-C",  
                    "bid1Price": "0",  
                    "bid1Size": "0",  
                    "bid1Iv": "0",  
                    "ask1Price": "435",  
                    "ask1Size": "0.66",  
                    "ask1Iv": "5",  
                    "lastPrice": "435",  
                    "highPrice24h": "435",  
                    "lowPrice24h": "165",  
                    "markPrice": "0.00000009",  
                    "indexPrice": "16600.55",  
                    "markIv": "0.7567",  
                    "underlyingPrice": "16590.42",  
                    "openInterest": "6.3",  
                    "turnover24h": "2482.73",  
                    "volume24h": "0.15",  
                    "totalVolume": "99",  
                    "totalTurnover": "1967653",  
                    "delta": "0.00000001",  
                    "gamma": "0.00000001",  
                    "vega": "0.00000004",  
                    "theta": "-0.00000152",  
                    "predictedDeliveryPrice": "0",  
                    "change24h": "86"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1672376592395  
    }  
    
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "category": "spot",  
            "list": [  
                {  
                    "symbol": "BTCUSDT",  
                    "bid1Price": "20517.96",  
                    "bid1Size": "2",  
                    "ask1Price": "20527.77",  
                    "ask1Size": "1.862172",  
                    "lastPrice": "20533.13",  
                    "prevPrice24h": "20393.48",  
                    "price24hPcnt": "0.0068",  
                    "highPrice24h": "21128.12",  
                    "lowPrice24h": "20318.89",  
                    "turnover24h": "243765620.65899866",  
                    "volume24h": "11801.27771",  
                    "usdIndexPrice": "20784.12009279"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1673859087947  
    }

---

# 查詢最新行情信息

可獲取到快照的最新市場價格，最佳買賣價格，以及過去時間內的交易量等.

> **覆蓋範圍: 現貨 / USDT永續 / USDT交割 / USDC永續 / USDC交割 / 反向合約 / 期權**

### HTTP請求

GET`/v5/market/tickers`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
[category](/docs/zh-TW/v5/enum#category)| **true**|  string| 產品類型. `spot`,`linear`,`inverse`,`option`  
[symbol](/docs/zh-TW/v5/enum#symbol)| false| string| 合約名稱  
baseCoin| false| string| 交易幣種. 僅`option`有效, `baseCoin`和`symbol`必傳其中一個  
expDate| false| string| 到期日. 舉例, 25DEC22. 僅`option`有效  
  
### 響應參數

  * Linear/Inverse
  * Option
  * Spot



參數| 類型| 說明  
---|---|---  
category| string| 產品類型  
list| array| Object  
> symbol| string| 合約名稱   
> lastPrice| string| 最新市場成交價   
> indexPrice| string| 指數價格   
> markPrice| string| 標記價格   
> prevPrice24h| string| 24小時前的整點市價   
> price24hPcnt| string| 市場價格相對24h前變化的百分比   
> highPrice24h| string| 最近24小時的最高價   
> lowPrice24h| string| 最近24小時的最低價   
> prevPrice1h| string| 1小時前的整點市價   
> openInterest| string| 未平倉合約的數量（雙邊和）  
> openInterestValue| string| 未平倉合約的價值（雙邊和）  
> singleOpenInterest| string| 未平倉合約的數量（單邊）  
> singleOpenInterestValue| string| 未平倉合約的價值（單邊）  
> turnover24h| string| 最近24小時成交額   
> volume24h| string| 最近24小時成交量   
> fundingRate| string| 資金費率   
> nextFundingTime| string| 下次結算資金費用的時間 (毫秒)   
> predictedDeliveryPrice| string| 預計交割價格. 交割前30分鐘有值  
> basisRate| string| 交割合約基差率   
> basis| string| 交割合約基差   
> deliveryFeeRate| string| 交割費率   
> deliveryTime| string| 交割時間戳 (毫秒), 僅適用於交割合約  
> ask1Size| string| 買1價的數量   
> bid1Price| string| 買1價   
> ask1Price| string| 賣1價   
> bid1Size| string| 買1價的數量   
> preOpenPrice| string| 盤前合約預估開盤價格 

  * 在進入連續競價後, 該值無意義

  
> preQty| string| 盤前合約預估開盤數量 

  * 進入連續競價後, 該值無意義

  
> [curPreListingPhase](/docs/zh-TW/v5/enum#curauctionphase)| string| 當前盤前交易階段   
> fundingIntervalHour| string| 資金費率間隔（小時）

  * 此數值目前僅支援整數小時

  
> fundingCap| string| 資金費率上下限  
> basisRateYear| string| 年化基準利率

  * 僅適用於交割合約;若為永續合約,將返回""

  
  
參數| 類型| 說明  
---|---|---  
category| string| 產品類型  
list| array| Object  
> symbol| string| 合約名稱   
> bid1Price| string| 買1價   
> bid1Size| string| 買1價的數量   
> bid1Iv| string| 買1價對應的iv   
> ask1Price| string| 賣1價   
> ask1Size| string| 賣1價的數量   
> ask1Iv| string| 賣1價對應的iv   
> lastPrice| string| 最新市場成交價   
> highPrice24h| string| 最近24小時的最高價   
> lowPrice24h| string| 最近24小時的最低價   
> markPrice| string| 標記價格   
> indexPrice| string| 指數價格   
> markIv| string| 標記價格對應的iv   
> underlyingPrice| string| 底層資產的價格   
> openInterest| string| 未平倉合約的數量   
> turnover24h| string| 最近24小時成交額   
> volume24h| string| 最近24小時成交量   
> totalVolume| string| 總成交量   
> totalTurnover| string| 總成交額   
> delta| string| Delta   
> gamma| string| Gamma   
> vega| string| Vega   
> theta| string| Theta   
> predictedDeliveryPrice| string| 預估交割價. 交割前30分鐘有值   
> change24h| string| 過去24小時的變化   
  
參數| 類型| 說明  
---|---|---  
category| string| 產品類型  
list| array| Object  
> symbol| string| 合約名稱   
> bid1Price| string| 買1價   
> bid1Size| string| 買1價的數量   
> ask1Price| string| 賣1價   
> ask1Size| string| 賣1價的數量   
> lastPrice| string| 最新市場成交價   
> prevPrice24h| string| 24小時前的整點市價   
> price24hPcnt| string| 市場價格相對24h前變化的百分比   
> highPrice24h| string| 最近24小時的最高價   
> lowPrice24h| string| 最近24小時的最低價   
> turnover24h| string| 最近24小時成交額   
> volume24h| string| 最近24小時成交量   
> usdIndexPrice| string| USD指數價格 

  * 用於計算統一帳戶裡資產折算成USD價值的價格
  * 若幣種不屬於抵押品幣種, 則返回空字符串
  * 只有那些幣對名是"XXX/USDT"或者"XXX/USDC"有值

  
  
[](/docs/zh-TW/api-explorer/v5/market/tickers)

* * *

### 請求示例

  * Inverse
  * Option
  * Spot



  * HTTP
  * Python
  * GO
  * Java
  * Node.js


    
    
    GET /v5/market/tickers?category=inverse&symbol=BTCUSD HTTP/1.1  
    Host: api-testnet.bybit.com  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(testnet=True)  
    print(session.get_tickers(  
        category="inverse",  
        symbol="BTCUSD",  
    ))  
    
    
    
    import (  
        "context"  
        "fmt"  
        bybit "github.com/bybit-exchange/bybit.go.api"  
    )  
    client := bybit.NewBybitHttpClient("", "", bybit.WithBaseURL(bybit.TESTNET))  
    params := map[string]interface{}{"category": "inverse", "symbol": "BTCUSD"}  
    client.NewUtaBybitServiceWithParams(params).GetMarketTickers(context.Background())  
    
    
    
    import com.bybit.api.client.domain.CategoryType;  
    import com.bybit.api.client.domain.market.*;  
    import com.bybit.api.client.domain.market.request.MarketDataRequest;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    var client = BybitApiClientFactory.newInstance().newAsyncMarketDataRestClient();  
    var tickerReueqt = MarketDataRequest.builder().category(CategoryType.INVERSE).symbol("BTCUSD").build();  
    client.getMarketTickers(tickerReueqt, System.out::println);  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
    });  
      
    client  
        .getTickers({  
            category: 'inverse',  
            symbol: 'BTCUSDT',  
        })  
        .then((response) => {  
            console.log(response);  
        })  
        .catch((error) => {  
            console.error(error);  
        });  
    

  * HTTP
  * Python
  * GO
  * Java
  * Node.js


    
    
    GET /v5/market/tickers?category=option&symbol=BTC-30DEC22-18000-C HTTP/1.1  
    Host: api-testnet.bybit.com  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(testnet=True)  
    print(session.get_tickers(  
        category="option",  
        symbol="BTC-30DEC22-18000-C",  
    ))  
    
    
    
    import (  
        "context"  
        "fmt"  
        bybit "github.com/bybit-exchange/bybit.go.api"  
    )  
    client := bybit.NewBybitHttpClient("", "", bybit.WithBaseURL(bybit.TESTNET))  
    params := map[string]interface{}{"category": "option", "symbol": "BTC-30DEC22-18000-C"}  
    client.NewUtaBybitServiceWithParams(params).GetMarketTickers(context.Background())  
    
    
    
    import com.bybit.api.client.domain.CategoryType;  
    import com.bybit.api.client.domain.market.*;  
    import com.bybit.api.client.domain.market.request.MarketDataRequest;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    var client = BybitApiClientFactory.newInstance().newAsyncMarketDataRestClient();  
    var tickerReueqt = MarketDataRequest.builder().category(CategoryType.OPTION).symbol("BTC-30DEC22-18000-C").build();  
    client.getMarketTickers(tickerReueqt, System.out::println);  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
    });  
      
    client  
      .getTickers({  
        category: 'option',  
        symbol: 'BTC-30DEC22-18000-C',  
      })  
      .then((response) => {  
        console.log(response);  
      })  
      .catch((error) => {  
        console.error(error);  
      });  
    

  * HTTP
  * Python
  * GO
  * Java
  * Node.js


    
    
    GET /v5/market/tickers?category=spot&symbol=BTCUSDT HTTP/1.1  
    Host: api-testnet.bybit.com  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(testnet=True)  
    print(session.get_tickers(  
        category="spot",  
        symbol="BTCUSDT",  
    ))  
    
    
    
    import (  
        "context"  
        "fmt"  
        bybit "github.com/bybit-exchange/bybit.go.api"  
    )  
    client := bybit.NewBybitHttpClient("", "", bybit.WithBaseURL(bybit.TESTNET))  
    params := map[string]interface{}{"category": "spot", "symbol": "BTCUSDT"}  
    client.NewUtaBybitServiceWithParams(params).GetMarketTickers(context.Background())  
    
    
    
    import com.bybit.api.client.domain.*;  
    import com.bybit.api.client.domain.market.*;  
    import com.bybit.api.client.domain.market.request.*;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    var client = BybitApiClientFactory.newInstance().newAsyncMarketDataRestClient();  
    var tickerReueqt = MarketDataRequest.builder().category(CategoryType.SPOT).symbol("BTCUSDT").build();  
    client.getMarketTickers(tickerReueqt, System.out::println);  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
    });  
      
    client  
      .getTickers({  
        category: 'spot',  
        symbol: 'BTCUSDT',  
      })  
      .then((response) => {  
        console.log(response);  
      })  
      .catch((error) => {  
        console.error(error);  
      });  
    

### 響應示例

  * Inverse
  * Option
  * Spot


    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "category": "inverse",  
            "list": [  
                {  
                    "symbol": "BTCUSD",  
                    "lastPrice": "16597.00",  
                    "indexPrice": "16598.54",  
                    "markPrice": "16596.00",  
                    "prevPrice24h": "16464.50",  
                    "price24hPcnt": "0.008047",  
                    "highPrice24h": "30912.50",  
                    "lowPrice24h": "15700.00",  
                    "prevPrice1h": "16595.50",  
                    "openInterest": "373504107",  
                    "openInterestValue": "22505.67",  
                    "turnover24h": "2352.94950046",  
                    "volume24h": "49337318",  
                    "fundingRate": "-0.001034",  
                    "nextFundingTime": "1672387200000",  
                    "predictedDeliveryPrice": "",  
                    "basisRate": "",  
                    "deliveryFeeRate": "",  
                    "deliveryTime": "0",  
                    "ask1Size": "1",  
                    "bid1Price": "16596.00",  
                    "ask1Price": "16597.50",  
                    "bid1Size": "1",  
                    "basis": ""  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1672376496682  
    }  
    
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "category": "option",  
            "list": [  
                {  
                    "symbol": "BTC-30DEC22-18000-C",  
                    "bid1Price": "0",  
                    "bid1Size": "0",  
                    "bid1Iv": "0",  
                    "ask1Price": "435",  
                    "ask1Size": "0.66",  
                    "ask1Iv": "5",  
                    "lastPrice": "435",  
                    "highPrice24h": "435",  
                    "lowPrice24h": "165",  
                    "markPrice": "0.00000009",  
                    "indexPrice": "16600.55",  
                    "markIv": "0.7567",  
                    "underlyingPrice": "16590.42",  
                    "openInterest": "6.3",  
                    "turnover24h": "2482.73",  
                    "volume24h": "0.15",  
                    "totalVolume": "99",  
                    "totalTurnover": "1967653",  
                    "delta": "0.00000001",  
                    "gamma": "0.00000001",  
                    "vega": "0.00000004",  
                    "theta": "-0.00000152",  
                    "predictedDeliveryPrice": "0",  
                    "change24h": "86"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1672376592395  
    }  
    
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "category": "spot",  
            "list": [  
                {  
                    "symbol": "BTCUSDT",  
                    "bid1Price": "20517.96",  
                    "bid1Size": "2",  
                    "ask1Price": "20527.77",  
                    "ask1Size": "1.862172",  
                    "lastPrice": "20533.13",  
                    "prevPrice24h": "20393.48",  
                    "price24hPcnt": "0.0068",  
                    "highPrice24h": "21128.12",  
                    "lowPrice24h": "20318.89",  
                    "turnover24h": "243765620.65899866",  
                    "volume24h": "11801.27771",  
                    "usdIndexPrice": "20784.12009279"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1673859087947  
    }