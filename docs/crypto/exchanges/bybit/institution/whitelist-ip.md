---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/institution/whitelist-ip
api_type: REST
updated_at: 2026-05-27 19:18:12.846538
---

# Get Delivery Price

Get the delivery price.

> **Covers: USDT futures / USDC futures / Inverse futures / Option**

info

  * Option: only returns those symbols which are `DELIVERING` (UTC 8 - UTC 12) when `symbol` is not specified.
  * During periods of extreme market volatility, this interface may experience increased latency or temporary delays in data delivery



### HTTP Request

GET`/v5/market/delivery-price`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
[category](/docs/v5/enum#category)| **true**|  string| Product type. `linear`, `inverse`, `option`  
symbol| false| string| Symbol name, like `BTCUSDT`, uppercase only  
baseCoin| false| string| Base coin, uppercase only. Default: `BTC`. _Valid for`option` only_  
settleCoin| false| string| Settle coin, uppercase only. Default: `USDC`.  
limit| false| integer| Limit for data size per page. [`1`, `200`]. Default: `50`  
cursor| false| string| Cursor. Use the `nextPageCursor` token from the response to retrieve the next page of the result set  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
category| string| Product type  
list| array| Object  
> symbol| string| Symbol name  
> deliveryPrice| string| Delivery price  
> deliveryTime| string| Delivery timestamp (ms)  
nextPageCursor| string| Refer to the `cursor` request parameter  
[](/docs/api-explorer/v5/market/delivery-price)

* * *

### Request Example

  * HTTP
  * Python
  * GO
  * Java
  * Node.js


    
    
    GET /v5/market/delivery-price?category=option&symbol=ETH-26DEC22-1400-C HTTP/1.1  
    Host: api-testnet.bybit.com  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP()  
    print(session.get_option_delivery_price(  
        category="option",  
        symbol="ETH-26DEC22-1400-C",  
    ))  
    
    
    
    import (  
        "context"  
        "fmt"  
        bybit "github.com/bybit-exchange/bybit.go.api"  
    )  
    client := bybit.NewBybitHttpClient("", "", bybit.WithBaseURL(bybit.TESTNET))  
    params := map[string]interface{}{"category": "linear", "symbol": "ETH-26DEC22-1400-C"}  
    client.NewUtaBybitServiceWithParams(params).GetDeliveryPrice(context.Background())  
    
    
    
    import com.bybit.api.client.domain.CategoryType;  
    import com.bybit.api.client.domain.market.request.MarketDataRequest;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    var client = BybitApiClientFactory.newInstance().newAsyncMarketDataRestClient();  
    var deliveryPriceRequest = MarketDataRequest.builder().category(CategoryType.OPTION).baseCoin("BTC").limit(10).build();  
    client.getDeliveryPrice(deliveryPriceRequest, System.out::println);  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
    });  
      
    client  
        .getDeliveryPrice({ category: 'option', symbol: 'ETH-26DEC22-1400-C' })  
        .then((response) => {  
            console.log(response);  
        })  
        .catch((error) => {  
            console.error(error);  
        });  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "category": "option",  
            "nextPageCursor": "",  
            "list": [  
                {  
                    "symbol": "ETH-26DEC22-1400-C",  
                    "deliveryPrice": "1220.728594450",  
                    "deliveryTime": "1672041600000"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1672055336993  
    }

---

# 查詢交割價格

查詢平台交割產品的交割價格，支持反向交割, USDT/USDC交割, 和期權

> **覆蓋範圍: USDC交割 / 反向交割 / 期權**

信息

  * 期權: 當不指定symbol時, 僅返回處於交割中狀態的(UTC8~UTC12)的數據
  * 在極端市場波動期間, 此介面可能會出現延遲增加或資料傳遞暫時延遲的情況



### HTTP請求

GET`/v5/market/delivery-price`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
[category](/docs/zh-TW/v5/enum#category)| **true**|  string| 產品類型. `linear`, `inverse`, `option`  
symbol| false| string| 合約名稱  
baseCoin| false| string| 交易貨幣. 默認: `BTC`. 僅支持`option`  
settleCoin| false| string| 結算貨幣，僅限大寫。默認：`USDC`。  
limit| false| integer| 每頁數量限制. [`1`, `200`]. 默認: `50`  
cursor| false| string| 游標，用於分頁  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
category| string| 產品類型  
list| array| Object  
> symbol| string| 合約名稱  
> deliveryPrice| string| 交割價格  
> deliveryTime| string| 交割時間戳 (毫秒)  
nextPageCursor| string| 游標，用於分頁  
[](/docs/zh-TW/api-explorer/v5/market/delivery-price)

* * *

### 請求示例

  * HTTP
  * Python
  * GO
  * Java
  * Node.js


    
    
    GET /v5/market/delivery-price?category=option&symbol=ETH-26DEC22-1400-C HTTP/1.1  
    Host: api-testnet.bybit.com  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP()  
    print(session.get_option_delivery_price(  
        category="option",  
        symbol="ETH-26DEC22-1400-C",  
    ))  
    
    
    
    import (  
        "context"  
        "fmt"  
        bybit "github.com/bybit-exchange/bybit.go.api"  
    )  
    client := bybit.NewBybitHttpClient("", "", bybit.WithBaseURL(bybit.TESTNET))  
    params := map[string]interface{}{"category": "linear", "symbol": "ETH-26DEC22-1400-C"}  
    client.NewUtaBybitServiceWithParams(params).GetDeliveryPrice(context.Background())  
    
    
    
    import com.bybit.api.client.domain.CategoryType;  
    import com.bybit.api.client.domain.market.request.MarketDataRequest;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    var client = BybitApiClientFactory.newInstance().newAsyncMarketDataRestClient();  
    var deliveryPriceRequest = MarketDataRequest.builder().category(CategoryType.OPTION).baseCoin("BTC").limit(10).build();  
    client.getDeliveryPrice(deliveryPriceRequest, System.out::println);  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
    });  
      
    client  
        .getDeliveryPrice({ category: 'option', symbol: 'ETH-26DEC22-1400-C' })  
        .then((response) => {  
            console.log(response);  
        })  
        .catch((error) => {  
            console.error(error);  
        });  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "category": "option",  
            "nextPageCursor": "",  
            "list": [  
                {  
                    "symbol": "ETH-26DEC22-1400-C",  
                    "deliveryPrice": "1220.728594450",  
                    "deliveryTime": "1672041600000"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1672055336993  
    }