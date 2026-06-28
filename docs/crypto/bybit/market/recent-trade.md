---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/market/recent-trade
api_type: Market Data
updated_at: 2026-06-28 19:12:27.429952
---

# Get Risk Limit

Query for the [risk limit](https://www.bybit.com/en/help-center/article/Risk-Limit-Perpetual-and-Futures) margin parameters. This information is also displayed on the website [here](https://www.bybit.com/en/announcement-info/margin-parameters/).

> **Covers: USDT contract / USDC contract / Inverse contract**

info

  * category=`linear` returns a data set of 15 symbols in each response. Please use the `cursor` param to get the next data set.
  * `symbol` support `Trading` status and `PreLaunch` [Pre-Market contracts](https://www.bybit.com/en/help-center/article/Introduction-to-Pre-Market-Perpetual) status trading pairs.
  * During periods of extreme market volatility, this interface may experience increased latency or temporary delays in data delivery



### HTTP Request

GET`/v5/market/risk-limit`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
[category](/docs/v5/enum#category)| **true**|  string| Product type. `linear`,`inverse`  
symbol| false| string| Symbol name, like `BTCUSDT`, uppercase only  
cursor| false| string| Cursor. Use the `nextPageCursor` token from the response to retrieve the next page of the data set  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
category| string| Product type  
list| array| Object  
> id| integer| Risk ID  
> symbol| string| Symbol name  
> riskLimitValue| string| Position limit  
> maintenanceMargin| number| Maintain margin rate  
> initialMargin| number| Initial margin rate  
> isLowestRisk| integer| `1`: true, `0`: false  
> maxLeverage| string| Allowed max leverage  
> mmDeduction| string| The maintenance margin deduction value when risk limit tier changed  
nextPageCursor| string| Refer to the `cursor` request parameter  
[](/docs/api-explorer/v5/market/risk-limit)

* * *

### Request Example

  * HTTP
  * Python
  * GO
  * Java
  * Node.js


    
    
    GET /v5/market/risk-limit?category=inverse&symbol=BTCUSD HTTP/1.1  
    Host: api-testnet.bybit.com  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(testnet=True)  
    print(session.get_risk_limit(  
        category="inverse",  
        symbol="BTCUSD",  
    ))  
    
    
    
    import (  
        "context"  
        "fmt"  
        bybit "github.com/bybit-exchange/bybit.go.api"  
    )  
    client := bybit.NewBybitHttpClient("", "", bybit.WithBaseURL(bybit.TESTNET))  
    params := map[string]interface{}{"category": "linear", "symbol": "BTCUSDT"}  
    client.NewUtaBybitServiceWithParams(params).GetMarketRiskLimits(context.Background())  
    
    
    
    import com.bybit.api.client.domain.CategoryType;  
    import com.bybit.api.client.domain.market.request.MarketDataRequest;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    var client = BybitApiClientFactory.newInstance().newAsyncMarketDataRestClient();  
    var riskMimitRequest = MarketDataRequest.builder().category(CategoryType.INVERSE).symbol("ADAUSD").build();  
    client.getRiskLimit(riskMimitRequest, System.out::println);  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
    });  
      
    client  
        .getRiskLimit({  
            category: 'inverse',  
            symbol: 'BTCUSD',  
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
            "category": "inverse",  
            "list": [  
                {  
                    "id": 1,  
                    "symbol": "BTCUSD",  
                    "riskLimitValue": "150",  
                    "maintenanceMargin": "0.5",  
                    "initialMargin": "1",  
                    "isLowestRisk": 1,  
                    "maxLeverage": "100.00",  
                    "mmDeduction": ""  
                },  
            ....  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1672054488010  
    }

---

# 查詢合約風險限額

查詢期貨合約的風險限額表

> **覆蓋範圍: USDT永續 / USDT交割 / USDC永續 / USDC交割 / 反向合約**

提示

什麼是風險限額？[風險限額(USDT合約)](https://www.bybit.com/en-US/help-center/bybitHC_Article?language=en_US&id=000001164)

信息

  * 當category=`linear`, 每次請求返回15個symbol的風險限額數據, 請通過cursor來實現翻頁查詢下一組15個symbol的數據。
  * `symbol`支持`Trading`線上可交易狀態，及`PreLaunch`[盤前交易](https://www.bybit.com/en/help-center/article/Introduction-to-Pre-Market-Perpetual)狀態的交易對。
  * 在極端市場波動期間, 此介面可能會出現延遲增加或資料傳遞暫時延遲的情況



### HTTP請求

GET`/v5/market/risk-limit`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
[category](/docs/zh-TW/v5/enum#category)| **true**|  string| 產品類型. `linear`,`inverse`  
symbol| false| string| 合約名稱  
cursor| false| string| 游標，用於翻頁  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
category| string| 產品類型  
list| array| Object  
> id| integer| 風險限額id  
> symbol| string| 合約名稱  
> riskLimitValue| string| 風險限制額度  
> maintenanceMargin| number| 維持保證金率  
> initialMargin| number| 初始保證金率  
> isLowestRisk| integer| 是否是最低風險限額. `1`: true, `0`: false  
> maxLeverage| string| 該風險限額允許的最大槓桿  
> mmDeduction| string| 維持保證金扣減額  
nextPageCursor| string| 下一頁游標, 配合`cursor`使用  
[](/docs/zh-TW/api-explorer/v5/market/risk-limit)

* * *

### 請求示例

  * HTTP
  * Python
  * GO
  * Java
  * Node.js


    
    
    GET /v5/market/risk-limit?category=inverse&symbol=BTCUSD HTTP/1.1  
    Host: api-testnet.bybit.com  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(testnet=True)  
    print(session.get_risk_limit(  
        category="inverse",  
        symbol="BTCUSD",  
    ))  
    
    
    
    import (  
        "context"  
        "fmt"  
        bybit "github.com/bybit-exchange/bybit.go.api"  
    )  
    client := bybit.NewBybitHttpClient("", "", bybit.WithBaseURL(bybit.TESTNET))  
    params := map[string]interface{}{"category": "linear", "symbol": "BTCUSDT"}  
    client.NewUtaBybitServiceWithParams(params).GetMarketRiskLimits(context.Background())  
    
    
    
    import com.bybit.api.client.domain.CategoryType;  
    import com.bybit.api.client.domain.market.request.MarketDataRequest;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    var client = BybitApiClientFactory.newInstance().newAsyncMarketDataRestClient();  
    var riskMimitRequest = MarketDataRequest.builder().category(CategoryType.INVERSE).symbol("ADAUSD").build();  
    client.getRiskLimit(riskMimitRequest, System.out::println);  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
    });  
      
    client  
        .getRiskLimit({  
            category: 'inverse',  
            symbol: 'BTCUSD',  
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
            "category": "inverse",  
            "list": [  
                {  
                    "id": 1,  
                    "symbol": "BTCUSD",  
                    "riskLimitValue": "150",  
                    "maintenanceMargin": "0.5",  
                    "initialMargin": "1",  
                    "isLowestRisk": 1,  
                    "maxLeverage": "100.00",  
                    "mmDeduction": ""  
                },  
            ....  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1672054488010  
    }