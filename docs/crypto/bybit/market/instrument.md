---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/market/instrument
api_type: Market Data
updated_at: 2026-07-03 19:14:10.425143
---

# Get Instruments Info

Query for the instrument specification of online trading pairs.

> **Covers: Spot / USDT contract / USDC contract / Inverse contract / Option**

info

  * Spot does not support pagination, so `limit`, `cursor` are invalid.
  * When querying by `baseCoin`, regardless of if category=`linear` or `inverse`, the result will contain USDT contract, USDC contract and Inverse contract symbols.



caution

  * This endpoint returns 500 entries by default. There are now more than 500 `linear` symbols on the platform. As a result, you will need to use `cursor` for pagination or `limit` to get all entries.
  * During periods of extreme market volatility, this interface may experience increased latency or temporary delays in data delivery
  * The fields `maxLimitOrderQty`, `maxMarketOrderQty`, and `postOnlyMaxLimitOrderSize` are adjusted bi-monthly (3rd and 17th, 08:00 UTC+8). Developers should not assume these values remain constant.



### HTTP Request

GET`/v5/market/instruments-info`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
[category](/docs/v5/enum#category)| **true**|  string| Product type. `spot`,`linear`,`inverse`,`option`  
[symbol](/docs/v5/enum#symbol)| false| string| Symbol name, like `BTCUSDT`, uppercase only  
[symbolType](/docs/v5/enum#symboltype)| false| string| SymbolType:The region to which the trading pair belongs,only for`linear`,`inverse`,`spot`  
[status](/docs/v5/enum#status)| false| string| Symbol status filter 

  * `linear` & `inverse` & `spot `By default returns only `Trading` symbols
  * `option` By default returns `PreLaunch`, `Trading`, and `Delivering`
  * Spot has `Trading` only
  * `linear` & `inverse`: when status=PreLaunch, it returns [Pre-Market contracts](https://www.bybit.com/help-center/article/Introduction-to-Pre-Market-Perpetual)

  
baseCoin| false| string| Base coin, uppercase only 

  * Applies to `linear`,`inverse`,`option` **only**
  * `option`: returns BTC by default

  
limit| false| integer| Limit for data size per page. [`1`, `1000`]. Default: `500`  
cursor| false| string| Cursor. Use the `nextPageCursor` token from the response to retrieve the next page of the result set  
  
### Response Parameters

  * Linear/Inverse
  * Option
  * Spot



Parameter| Type| Comments  
---|---|---  
category| string| Product type  
nextPageCursor| string| Cursor. Used to pagination  
list| array| Object  
> symbol| string| Symbol name   
> symbolId| integer| The ID of symbol name   
> [contractType](/docs/v5/enum#contracttype)| string| Contract type  
> [status](/docs/v5/enum#status)| string| Instrument status   
> baseCoin| string| Base coin   
> quoteCoin| string| Quote coin   
> [symbolType](/docs/v5/enum#symboltype)| string| the region to which the trading pair belongs  
> launchTime| string| Launch timestamp (ms)   
> deliveryTime| string| Delivery timestamp (ms) 

  * Expired futures delivery time
  * Perpetual delisting time

  
> deliveryFeeRate| string| Delivery fee rate  
> priceScale| string| Price scale   
> leverageFilter| Object| Leverage attributes   
>> minLeverage| string| Minimum leverage   
>> maxLeverage| string| Maximum leverage   
>> leverageStep| string| The step to increase/reduce leverage   
> priceFilter| Object| Price attributes   
>> minPrice| string| Minimum order price   
>> maxPrice| string| Maximum order price   
>> tickSize| string| The step to increase/reduce order price   
> lotSizeFilter| Object| Size attributes   
>> minNotionalValue| string| Minimum notional value  
>> maxOrderQty| string| Maximum quantity for Limit and PostOnly order   
>> maxMktOrderQty| string| Maximum quantity for Market order   
>> minOrderQty| string| Minimum order quantity   
>> qtyStep| string| The step to increase/reduce order quantity   
>> postOnlyMaxOrderQty| string| deprecated, please use `maxOrderQty`  
> unifiedMarginTrade| boolean| Whether to support unified margin trade   
> fundingInterval| integer| Funding interval (minute)   
> settleCoin| string| Settle coin   
> [copyTrading](/docs/v5/enum#copytrading)| string| Copy trade symbol or not   
> upperFundingRate| string| Upper limit of funding date  
> lowerFundingRate| string| Lower limit of funding date  
> displayName| string| The USDC futures & perpetual name displayed in the Web or App  
> forbidUplWithdrawal| boolean| Whether to prohibit unrealised profit withdrawal  
> riskParameters| object| Risk parameters for limit order price. Note that the [formula changed](https://announcements.bybit.com/en/article/update-contract-price-limit-enhancement-bltf9ebdcebe3089641/) in May 2026  
>> priceLimitRatioX| string| Ratio X  
>> priceLimitRatioY| string| Ratio Y  
> isPreListing| boolean| 

  * Whether the contract is a pre-market contract
  * When the pre-market contract is converted to official contract, it will be false

  
> preListingInfo| object| 

  * If isPreListing=false, preListingInfo=null
  * If isPreListing=true, preListingInfo is an object

  
>> [curAuctionPhase](/docs/v5/enum#curauctionphase)| string| The current auction phase  
>> phases| array<object>| Each phase time info  
>>> [phase](/docs/v5/enum#curauctionphase)| string| pre-market trading phase  
>>> startTime| string| The start time of the phase, timestamp(ms)  
>>> endTime| string| The end time of the phase, timestamp(ms)  
>> auctionFeeInfo| object| Action fee info  
>>> auctionFeeRate| string| The trading fee rate during auction phase 

  * There is no trading fee until entering continues trading phase

  
>>> takerFeeRate| string| The taker fee rate during continues trading phase   
>>> makerFeeRate| string| The maker fee rate during continues trading phase  
>> skipCallAuction| boolean| `false`, `true` Whether the pre-market contract skips the call auction phase  
  
Parameter| Type| Comments  
---|---|---  
category| string| Product type  
nextPageCursor| string| Cursor. Used to pagination  
list| array| Object  
> symbol| string| Symbol name   
> symbolId| integer| The ID of symbol name   
> optionsType| string| Option type. `Call`, `Put`  
> [status](/docs/v5/enum#status)| string| Instrument status   
> baseCoin| string| Base coin   
> quoteCoin| string| Quote coin   
> settleCoin| string| Settle coin   
> launchTime| string| Launch timestamp (ms)   
> deliveryTime| string| Delivery timestamp (ms)   
> deliveryFeeRate| string| Delivery fee rate   
> priceFilter| Object| Price attributes   
>> minPrice| string| Minimum order price   
>> maxPrice| string| Maximum order price   
>> tickSize| string| The step to increase/reduce order price   
> lotSizeFilter| Object| Size attributes   
>> maxOrderQty| string| Maximum order quantity   
>> minOrderQty| string| Minimum order quantity   
>> qtyStep| string| The step to increase/reduce order quantity   
> displayName| string| The option name displayed in the Web or App   
  
Parameter| Type| Comments  
---|---|---  
category| string| Product type  
list| array| Object  
> symbolId| integer| The ID of symbol name   
> symbol| string| Symbol name   
> baseCoin| string| Base coin   
> quoteCoin| string| Quote coin   
> innovation| string| deprecated, please use `symbolType`  
> [symbolType](/docs/v5/enum#symboltype)| string| the region to which the trading pair belongs  
> xstockMultiplier| string| Xstock mutiplier 
* It only applies to those "symbolType"=`xstocks` trading pairs  
relationship: stock_price = token_price / mutiplier; stock_qty = token_qty * mutiplier
* default value: "1"  
> [status](/docs/v5/enum#status)| string| Instrument status   
> [marginTrading](/docs/v5/enum#margintrading)| string| Whether or not this symbol supports margin trading

  * This is to identify if the symbol supports margin trading under different account modes
  * You may find some symbols do not support margin buy or margin sell, so you need to go to [Collateral Info (UTA)](/docs/v5/account/collateral-info) to check if that coin is borrowable
  * When the lending pool has insufficient balance to lend out funds (can happen during big market movements) then this will switch to `none` until there is sufficient balance to re-enable margin trading

  
> stTag| string| Whether or not it has an [special treatment label](https://www.bybit.com/en/help-center/article/Bybit-Special-Treatment-ST-Label-Management-Rules). `0`: false, `1`: true   
> lotSizeFilter| Object| Size attributes   
>> basePrecision| string| The precision of base coin   
>> quotePrecision| string| The precision of quote coin   
>> minOrderQty| string| Minimum order quantity, deprecated, no longer check `minOrderQty`, check `minOrderAmt` instead  
>> maxOrderQty| string| Maximum order quantity, deprecated, please refer to `maxLimitOrderQty`, `maxMarketOrderQty` based on order type   
>> minOrderAmt| string| Minimum order amount   
>> maxOrderAmt| string| Maximum order amount, deprecated, no longer check `maxOrderAmt`, check `maxLimitOrderQty` and `maxMarketOrderQty` instead  
>> maxLimitOrderQty| string| Maximum Limit order quantity 

  * For post-only and retail price improvement (RPI) orders, the maximum limit order quantity is 5x `maxLimitOrderQty`

  
>> maxMarketOrderQty| string| Maximum Market order quantity   
>> postOnlyMaxLimitOrderSize | string| Maximum limit order size for Post-only and RPI orders   
> priceFilter| Object| Price attributes   
>> tickSize| string| The step to increase/reduce order price   
> riskParameters| Object| Risk parameters for limit order price, refer to [announcement](https://announcements.bybit.com/en/article/title-adjustments-to-bybit-s-spot-trading-limit-order-mechanism-blt786c0c5abf865983/)  
>> priceLimitRatioX| string| Ratio X  
>> priceLimitRatioY| string| Ratio Y  
  
[](/docs/api-explorer/v5/market/instrument)

* * *

### Request Example

  * Linear
  * Option
  * Spot



  * HTTP
  * Python
  * Go
  * Java
  * Node.js


    
    
    GET /v5/market/instruments-info?category=linear&symbol=BTCUSDT HTTP/1.1  
    Host: api-testnet.bybit.com  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(testnet=True)  
    print(session.get_instruments_info(  
        category="linear",  
        symbol="BTCUSDT",  
    ))  
    
    
    
    import (  
        "context"  
        "fmt"  
        bybit "github.com/bybit-exchange/bybit.go.api"  
    )  
    client := bybit.NewBybitHttpClient("", "", bybit.WithBaseURL(bybit.TESTNET))  
    params := map[string]interface{}{"category": "linear", "symbol": "BTCUSDT"}  
    client.NewUtaBybitServiceWithParams(params).GetInstrumentInfo(context.Background())  
    
    
    
    import com.bybit.api.client.domain.CategoryType;  
    import com.bybit.api.client.domain.market.*;  
    import com.bybit.api.client.domain.market.request.MarketDataRequest;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    var client = BybitApiClientFactory.newInstance().newAsyncMarketDataRestClient();  
    var instrumentInfoRequest = MarketDataRequest.builder().category(CategoryType.LINEAR).symbol("BTCUSDT").instrumentStatus(InstrumentStatus.TRADING).limit(500).build();  
    client.getInstrumentsInfo(instrumentInfoRequest,System.out::println);  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
    });  
      
    client  
        .getInstrumentsInfo({  
            category: 'linear',  
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


    
    
    GET /v5/market/instruments-info?category=option&symbol=ETH-3JAN23-1250-P HTTP/1.1  
    Host: api-testnet.bybit.com  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(testnet=True)  
    print(session.get_instruments_info(  
        category="option",  
        symbol="ETH-3JAN23-1250-P",  
    ))  
    
    
    
    import (  
        "context"  
        "fmt"  
        bybit "github.com/bybit-exchange/bybit.go.api"  
    )  
    client := bybit.NewBybitHttpClient("", "", bybit.WithBaseURL(bybit.TESTNET))  
    params := map[string]interface{}{"category": "option", "symbol": "ETH-3JAN23-1250-P"}  
    client.NewUtaBybitServiceWithParams(params).GetInstrumentInfo(context.Background())  
    
    
    
    import com.bybit.api.client.domain.CategoryType;  
    import com.bybit.api.client.domain.market.*;  
    import com.bybit.api.client.domain.market.request.MarketDataRequest;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    var client = BybitApiClientFactory.newInstance().newAsyncMarketDataRestClient();  
    var instrumentInfoRequest = MarketDataRequest.builder().category(CategoryType.OPTION).symbol("ETH-3JAN23-1250-P").instrumentStatus(InstrumentStatus.TRADING).limit(500).build();  
    client.getInstrumentsInfo(instrumentInfoRequest,System.out::println);  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
    });  
      
    client  
      .getInstrumentsInfo({  
        category: 'option',  
        symbol: 'ETH-3JAN23-1250-P',  
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


    
    
    GET /v5/market/instruments-info?category=spot&symbol=BTCUSDT HTTP/1.1  
    Host: api-testnet.bybit.com  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(testnet=True)  
    print(session.get_instruments_info(  
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
    client.NewUtaBybitServiceWithParams(params).GetInstrumentInfo(context.Background())  
    
    
    
    import com.bybit.api.client.domain.*;  
    import com.bybit.api.client.domain.market.*;  
    import com.bybit.api.client.domain.market.request.*;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    var client = BybitApiClientFactory.newInstance().newAsyncMarketDataRestClient();  
    var instrumentInfoRequest = MarketDataRequest.builder().category(CategoryType.SPOT).symbol("BTCUSDT").instrumentStatus(InstrumentStatus.TRADING).limit(500).build();  
    client.getInstrumentsInfo(instrumentInfoRequest,System.out::println);  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
    });  
      
    client  
      .getInstrumentsInfo({  
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

  * Linear
  * Option
  * Spot


    
    
    // official USDT Perpetual instrument structure  
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "category": "linear",  
            "list": [  
                {  
                    "symbol": "BTCUSDT",  
                    "symbolId": 5,  
                    "contractType": "LinearPerpetual",  
                    "status": "Trading",  
                    "baseCoin": "BTC",  
                    "quoteCoin": "USDT",  
                    "launchTime": "1585526400000",  
                    "deliveryTime": "0",  
                    "deliveryFeeRate": "",  
                    "priceScale": "2",  
                    "leverageFilter": {  
                        "minLeverage": "1",  
                        "maxLeverage": "100.00",  
                        "leverageStep": "0.01"  
                    },  
                    "priceFilter": {  
                        "minPrice": "0.10",  
                        "maxPrice": "1999999.80",  
                        "tickSize": "0.10"  
                    },  
                    "lotSizeFilter": {  
                        "maxOrderQty": "1190.000",  
                        "minOrderQty": "0.001",  
                        "qtyStep": "0.001",  
                        "postOnlyMaxOrderQty": "1190.000",  
                        "maxMktOrderQty": "500.000",  
                        "minNotionalValue": "5"  
                    },  
                    "unifiedMarginTrade": true,  
                    "fundingInterval": 480,  
                    "settleCoin": "USDT",  
                    "copyTrading": "both",  
                    "upperFundingRate": "0.00375",  
                    "lowerFundingRate": "-0.00375",  
                    "isPreListing": false,  
                    "preListingInfo": null,  
                    "riskParameters": {  
                        "priceLimitRatioX": "0.01",  
                        "priceLimitRatioY": "0.02"  
                    },  
                    "symbolType": ""  
                }  
            ],  
            "nextPageCursor": ""  
        },  
        "retExtInfo": {},  
        "time": 1735809771618  
    }  
      
    // Pre-market Perpetual instrument structure  
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "category": "linear",  
            "list": [  
                {  
                    "symbol": "BIOUSDT",  
                    "contractType": "LinearPerpetual",  
                    "status": "PreLaunch",  
                    "baseCoin": "BIO",  
                    "quoteCoin": "USDT",  
                    "launchTime": "1735032510000",  
                    "deliveryTime": "0",  
                    "deliveryFeeRate": "",  
                    "priceScale": "4",  
                    "leverageFilter": {  
                        "minLeverage": "1",  
                        "maxLeverage": "5.00",  
                        "leverageStep": "0.01"  
                    },  
                    "priceFilter": {  
                        "minPrice": "0.0001",  
                        "maxPrice": "1999.9998",  
                        "tickSize": "0.0001"  
                    },  
                    "lotSizeFilter": {  
                        "maxOrderQty": "70000",  
                        "minOrderQty": "1",  
                        "qtyStep": "1",  
                        "postOnlyMaxOrderQty": "70000",  
                        "maxMktOrderQty": "14000",  
                        "minNotionalValue": "5"  
                    },  
                    "unifiedMarginTrade": true,  
                    "fundingInterval": 480,  
                    "settleCoin": "USDT",  
                    "copyTrading": "none",  
                    "upperFundingRate": "0.05",  
                    "lowerFundingRate": "-0.05",  
                    "isPreListing": true,  
                    "preListingInfo": {  
                        "curAuctionPhase": "ContinuousTrading",  
                        "phases": [  
                            {  
                                "phase": "CallAuction",  
                                "startTime": "1735113600000",  
                                "endTime": "1735116600000"  
                            },  
                            {  
                                "phase": "CallAuctionNoCancel",  
                                "startTime": "1735116600000",  
                                "endTime": "1735116900000"  
                            },  
                            {  
                                "phase": "CrossMatching",  
                                "startTime": "1735116900000",  
                                "endTime": "1735117200000"  
                            },  
                            {  
                                "phase": "ContinuousTrading",  
                                "startTime": "1735117200000",  
                                "endTime": ""  
                            }  
                        ],  
                        "auctionFeeInfo": {  
                            "auctionFeeRate": "0",  
                            "takerFeeRate": "0.001",  
                            "makerFeeRate": "0.0004"  
                        }  
                    },  
                    "riskParameters": {  
                        "priceLimitRatioX": "0.05",  
                        "priceLimitRatioY": "0.1"  
                    },  
                    "symbolType": ""  
                }  
            ],  
            "nextPageCursor": "first%3DBIOUSDT%26last%3DBIOUSDT"  
        },  
        "retExtInfo": {},  
        "time": 1735810114435  
    }  
    
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "category": "option",  
            "nextPageCursor": "",  
            "list": [  
                {  
                    "symbol": "BTC-27MAR26-70000-P-USDT",  
                    "status": "Trading",  
                    "baseCoin": "BTC",  
                    "quoteCoin": "USDT",  
                    "settleCoin": "USDT",  
                    "optionsType": "Put",  
                    "launchTime": "1743669649256",  
                    "deliveryTime": "1774598400000",  
                    "deliveryFeeRate": "0.00015",  
                    "priceFilter": {  
                        "minPrice": "5",  
                        "maxPrice": "1110000",  
                        "tickSize": "5"  
                    },  
                    "lotSizeFilter": {  
                        "maxOrderQty": "500",  
                        "minOrderQty": "0.01",  
                        "qtyStep": "0.01"  
                    },  
                    "displayName": "BTCUSDT-27MAR26-70000-P"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1672712537130  
    }  
    
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "category": "spot",  
            "list": [  
                {  
                    "symbolId": 9,  
                    "symbol": "BTCUSDT",  
                    "baseCoin": "BTC",  
                    "quoteCoin": "USDT",  
                    "innovation": "0",  
                    "status": "Trading",  
                    "marginTrading": "utaOnly",  
                    "stTag": "0",  
                    "lotSizeFilter": {  
                        "basePrecision": "0.000001",  
                        "quotePrecision": "0.0000001",  
                        "minOrderQty": "0.000011",  
                        "maxOrderQty": "83",  
                        "minOrderAmt": "5",  
                        "maxOrderAmt": "8000000",  
                        "maxLimitOrderQty": "83",  
                        "maxMarketOrderQty": "41.5",  
                        "postOnlyMaxLimitOrderSize":"60000"  
      
                    },  
                    "priceFilter": {  
                        "tickSize": "0.1"  
                    },  
                    "riskParameters": {  
                        "priceLimitRatioX": "0.005",  
                        "priceLimitRatioY": "0.01"  
                    },  
                    "symbolType": ""  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1760027412300  
    }

---

# 查詢可交易產品的規格信息

查詢全站可交易產品的基礎配置規則信息

> **覆蓋範圍: 現貨 / USDT永續 / USDT交割 / USDC永續 / USDC交割 / 反向合約 / 期權**

警告

  * 現貨不支持翻頁，因此`limit`, `cusor`無效.
  * 當通過`baseCoin`查詢時, 不管category=`linear`或`inverse`, 返回結果中都會包含USDT永續, USDT交割, USDC永續, USDC交割和反向合約的交易對.
  * 在極端市場波動期間, 此介面可能會出現延遲增加或資料傳遞暫時延遲的情況
  * `maxLimitOrderQty`, `maxMarketOrderQty`, `postOnlyMaxLimitOrderSize` 欄位會於每月 3 日與 17 日（UTC+8 08:00）進行定期調整。請開發者勿假設上述欄位數值為固定不變，並應於系統設計時預留動態更新與重新讀取機制。



### HTTP請求

GET`/v5/market/instruments-info`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
[category](/docs/zh-TW/v5/enum#category)| **true**|  string| 產品類型. `spot`,`linear`,`inverse`,`option`  
symbol| false| string| 合約名稱  
[symbolType](/docs/zh-TW/v5/enum#symboltype)| false| string| 交易對所屬區域:僅对`linear`,`inverse`,`spot`有效  
[status](/docs/zh-TW/v5/enum#status)| false| string| 交易對狀態篩選 

  * `linear` & `inverse` & `spot ` 默認返回`Trading`狀態的交易對
  * `option` 默認返回 `PreLaunch`, `Trading`, `Delivering`狀態的交易對
  * 現貨 僅有`Trading`狀態
  * `linear` & `inverse`: status=PreLaunch可以查詢到盤前交易的合約

  
baseCoin| false| string| 交易貨幣. 僅對期貨/期權有效 

  * 對於期權, 默認返回baseCoin為BTC的

  
limit| false| integer| 每頁數量限制. [`1`, `1000`]. 默認: `500`  
cursor| false| string| 游標，用於翻頁  
  
### 響應參數

  * Linear/Inverse
  * Option
  * Spot



參數| 類型| 說明  
---|---|---  
category| string| 產品類型  
nextPageCursor| string| 游標，用於翻頁  
list| array| Object  
> symbol| string| 合約名稱   
> symbolId| integer| 合約symbol ID   
> [contractType](/docs/zh-TW/v5/enum#contracttype)| string| 合約類型  
> [status](/docs/zh-TW/v5/enum#status)| string| 合約狀態   
> baseCoin| string| 交易幣種   
> quoteCoin| string| 報價幣種   
> [symbolType](/docs/zh-TW/v5/enum#symboltype)| string|  交易對所屬區域  
> launchTime| string| 發佈時間 (ms)   
> deliveryTime| string| 交割時間 (ms)

  * 交割合約交割時間
  * 永續合約下架時間

  
> deliveryFeeRate| string| 交割費率. 僅對交割合約有效  
> priceScale| string| 價格精度   
> leverageFilter| Object| 槓桿屬性   
>> minLeverage| string| 最小槓桿   
>> maxLeverage| string| 最大槓桿   
>> leverageStep| string| 修改槓桿的步長   
> priceFilter| Object| 價格屬性   
>> minPrice| string| 訂單最小價格   
>> maxPrice| string| 訂單最大價格   
>> tickSize| string| 修改價格的步長   
> lotSizeFilter| Object| 訂單數量屬性   
>> maxOrderQty| string| 單筆限價或PostOnly單最大下單量   
>> maxMktOrderQty| string| 單筆市價單最大下單量   
>> minOrderQty| string| 單筆訂單最小下單量   
>> qtyStep| string| 修改下單量的步長   
>> postOnlyMaxOrderQty| string| 已廢棄, 請參照`maxOrderQty`  
>> minNotionalValue| string| 訂單最小名義價值  
> unifiedMarginTrade| boolean| 是否支持統一保證金交易   
> fundingInterval| integer| 資金費率結算週期 (分鐘)   
> settleCoin| string| 結算幣種   
> [copyTrading](/docs/zh-TW/v5/enum#copytrading)| string| 當前交易對是否支持帶單交易   
> upperFundingRate| string| 資金費率上限   
> lowerFundingRate| string| 資金費率下限   
> displayName| string| 網頁或APP端展示的USDC永續和交割合約的名稱  
> forbidUplWithdrawal| boolean| 是否禁止浮盈提現  
> riskParameters| object| 限價單價格風控參數, 參讀該[公告內容](https://announcements.bybit.com/en/article/update-contract-price-limit-enhancement-bltf9ebdcebe3089641/)（2026年5月更新）  
>> priceLimitRatioX| string| 參數X  
>> priceLimitRatioY| string| 參數Y  
> isPreListing| boolean| 

  * 該合約是否為盤前合約
  * 當盤前合約轉為正式合約後, 值將變成false

  
> preListingInfo| object| 

  * 如果isPreListing=false, preListingInfo=null
  * 如果isPreListing=true, preListingInfo是object

  
>> [curAuctionPhase](/docs/zh-TW/v5/enum#curauctionphase)| string| 當前的盤前階段  
>> phases| array<object>| 每個階段的時間信息  
>>> [phase](/docs/zh-TW/v5/enum#curauctionphase)| string| 盤前交易階段  
>>> startTime| string| 該階段的開始時間戳(毫秒)  
>>> endTime| string| 該階段的結束時間戳(毫秒)  
>> auctionFeeInfo| object| 盤前交易手續費率信息  
>>> auctionFeeRate| string| 集合競價期間的手續費率 

  * 目前, 僅在連續競價期間才會產生手續費

  
>>> takerFeeRate| string| 連續競價期間的吃單成交手續費率  
>>> makerFeeRate| string| 連續競價期間的掛單成交手續費率  
>> skipCallAuction| boolean| `false`, `true` 是否跳過集合競價階段  
  
參數| 類型| 說明  
---|---|---  
category| string| 產品類型  
nextPageCursor| string| 游標，用於翻頁  
list| array| Object  
> symbol| string| 合約名稱   
> symbolId| integer| 期權symbol ID   
> optionsType| string| 期權類型. `Call`,`Put`  
> [status](/docs/zh-TW/v5/enum#status)| string| 合約狀態   
> baseCoin| string| 交易幣種   
> quoteCoin| string| 報價幣種   
> settleCoin| string| 結算幣種   
> launchTime| string| 發佈時間 (ms)   
> deliveryTime| string| 交割時間 (ms)   
> deliveryFeeRate| string| 交割費率   
> priceFilter| Object| 價格屬性   
>> minPrice| string| 最小訂單價格   
>> maxPrice| string| 最大訂單價格   
>> tickSize| string| 修改訂單價格的步長   
> lotSizeFilter| Object| 訂單量屬性   
>> maxOrderQty| string| 單筆訂單最大下單量   
>> minOrderQty| string| 單筆訂單最小下單量   
>> qtyStep| string| 修改下單量的步長   
> displayName| Object| 網頁或APP端展示的期權名稱   
  
參數| 類型| 說明  
---|---|---  
category| string| 產品類型  
list| array| Object  
> symbolId| integer| 現貨交易對ID   
> symbol| string| 現貨交易對名稱   
> baseCoin| string| 交易幣種   
> quoteCoin| string| 報價幣種   
> innovation| string| 已廢棄, 請參照`symbolType`  
> [symbolType](/docs/zh-TW/v5/enum#symboltype)| string|  交易對所屬區域  
> xstockMultiplier| string| 股票代幣係數
* 僅適用於"symbolType"=`xstocks`交易對  
關係: 股票價格 = 代幣價格 / 係數; 股票數量 = 代幣數量 * 係數
* 默認值: "1"  
> [status](/docs/zh-TW/v5/enum#status)| string| 合約狀態   
> [marginTrading](/docs/zh-TW/v5/enum#margintrading)| string| 該幣對是否支持槓桿交易 

  * 該字段僅用於說明不同帳戶類型下某個幣對是否支持槓桿交易
  * 您可能會遇到某個幣對支持槓桿交易, 但是不支持單邊買入或者賣出, 這種情況下您需要前往[查詢抵押品信息 (UTA)](/docs/zh-TW/v5/account/collateral-info)確認目標幣種是否可借貸

  
> stTag| string| 幣對是否存在[特殊處理(ST)標籤](https://www.bybit.com/en/help-center/article/Bybit-Special-Treatment-ST-Label-Management-Rules). `0`: 否, `1`: 是   
> lotSizeFilter| Object| 數量屬性   
>> basePrecision| string| 交易幣種精度   
>> quotePrecision| string| 報價幣種精度   
>> minOrderQty| string| 單筆訂單最小下單量, 已廢棄, 不再檢查`minOrderQty`，而是檢查`minOrderAmt`  
>> maxOrderQty| string| 單筆訂單最大下單量, 已廢棄, 請基於訂單類型參考`maxLimitOrderQty`, `maxMarketOrderQty`  
>> minOrderAmt| string| 單筆訂單最小訂單額   
>> maxOrderAmt| string| 單筆訂單最大訂單額, 已廢棄, 不再檢查 `maxOrderAmt`，而是檢查 `maxLimitOrderQty` 和 `maxMarketOrderQty`  
>> maxLimitOrderQty| string| 單筆限價訂單最大下單量 

  * 被動委託(Post-Only)與零售價格優化(RPI)的最大限價訂單下單量為5x `maxLimitOrderQty`

  
>> maxMarketOrderQty| string| 單筆市價訂單最大下單量   
>> postOnlyMaxLimitOrderSize | string| 被動委託(Post-Only)與零售價格優化(RPI)的最大限價單規模  
> priceFilter| Object| 價格屬性   
>> tickSize| string| 修改訂單的步長   
> riskParameters| Object| 限價單價格風控參數, 參讀該[公告內容](https://announcements.bybit.com/zh-TW/article/title-adjustments-to-bybit-s-spot-trading-limit-order-mechanism-blt786c0c5abf865983/)  
>> priceLimitRatioX| string| 參數 X  
>> priceLimitRatioY| string| 參數 Y  
  
[](/docs/zh-TW/api-explorer/v5/market/instrument)

* * *

### 請求示例

  * Linear
  * Option
  * Spot



  * HTTP
  * Python
  * Go
  * Java
  * Node.js


    
    
    GET /v5/market/instruments-info?category=linear&symbol=BTCUSDT HTTP/1.1  
    Host: api-testnet.bybit.com  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(testnet=True)  
    print(session.get_instruments_info(  
        category="linear",  
        symbol="BTCUSDT",  
    ))  
    
    
    
    import (  
        "context"  
        "fmt"  
        bybit "github.com/bybit-exchange/bybit.go.api"  
    )  
    client := bybit.NewBybitHttpClient("", "", bybit.WithBaseURL(bybit.TESTNET))  
    params := map[string]interface{}{"category": "linear", "symbol": "BTCUSDT"}  
    client.NewUtaBybitServiceWithParams(params).GetInstrumentInfo(context.Background())  
    
    
    
    import com.bybit.api.client.domain.CategoryType;  
    import com.bybit.api.client.domain.market.*;  
    import com.bybit.api.client.domain.market.request.MarketDataRequest;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    var client = BybitApiClientFactory.newInstance().newAsyncMarketDataRestClient();  
    var instrumentInfoRequest = MarketDataRequest.builder().category(CategoryType.LINEAR).symbol("BTCUSDT").instrumentStatus(InstrumentStatus.TRADING).limit(500).build();  
    client.getInstrumentsInfo(instrumentInfoRequest,System.out::println);  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
    });  
      
    client  
        .getInstrumentsInfo({  
            category: 'linear',  
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


    
    
    GET /v5/market/instruments-info?category=option&symbol=ETH-3JAN23-1250-P HTTP/1.1  
    Host: api-testnet.bybit.com  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(testnet=True)  
    print(session.get_instruments_info(  
        category="option",  
        symbol="ETH-3JAN23-1250-P",  
    ))  
    
    
    
    import (  
        "context"  
        "fmt"  
        bybit "github.com/bybit-exchange/bybit.go.api"  
    )  
    client := bybit.NewBybitHttpClient("", "", bybit.WithBaseURL(bybit.TESTNET))  
    params := map[string]interface{}{"category": "option", "symbol": "ETH-3JAN23-1250-P"}  
    client.NewUtaBybitServiceWithParams(params).GetInstrumentInfo(context.Background())  
    
    
    
    import com.bybit.api.client.domain.CategoryType;  
    import com.bybit.api.client.domain.market.*;  
    import com.bybit.api.client.domain.market.request.MarketDataRequest;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    var client = BybitApiClientFactory.newInstance().newAsyncMarketDataRestClient();  
    var instrumentInfoRequest = MarketDataRequest.builder().category(CategoryType.OPTION).symbol("ETH-3JAN23-1250-P").instrumentStatus(InstrumentStatus.TRADING).limit(500).build();  
    client.getInstrumentsInfo(instrumentInfoRequest,System.out::println);  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
    });  
      
    client  
      .getInstrumentsInfo({  
        category: 'option',  
        symbol: 'ETH-3JAN23-1250-P',  
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


    
    
    GET /v5/market/instruments-info?category=spot&symbol=BTCUSDT HTTP/1.1  
    Host: api-testnet.bybit.com  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(testnet=True)  
    print(session.get_instruments_info(  
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
    client.NewUtaBybitServiceWithParams(params).GetInstrumentInfo(context.Background())  
    
    
    
    import com.bybit.api.client.domain.*;  
    import com.bybit.api.client.domain.market.*;  
    import com.bybit.api.client.domain.market.request.*;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    var client = BybitApiClientFactory.newInstance().newAsyncMarketDataRestClient();  
    var instrumentInfoRequest = MarketDataRequest.builder().category(CategoryType.SPOT).symbol("BTCUSDT").instrumentStatus(InstrumentStatus.TRADING).limit(500).build();  
    client.getInstrumentsInfo(instrumentInfoRequest,System.out::println);  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
    });  
      
    client  
      .getInstrumentsInfo({  
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

  * Linear
  * Option
  * Spot


    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "category": "linear",  
            "list": [  
                {  
                    "symbol": "BTCUSDT",  
                    "symbolId": 5,  
                    "contractType": "LinearPerpetual",  
                    "status": "Trading",  
                    "baseCoin": "BTC",  
                    "quoteCoin": "USDT",  
                    "launchTime": "1585526400000",  
                    "deliveryTime": "0",  
                    "deliveryFeeRate": "",  
                    "priceScale": "2",  
                    "leverageFilter": {  
                        "minLeverage": "1",  
                        "maxLeverage": "100.00",  
                        "leverageStep": "0.01"  
                    },  
                    "priceFilter": {  
                        "minPrice": "0.10",  
                        "maxPrice": "1999999.80",  
                        "tickSize": "0.10"  
                    },  
                    "lotSizeFilter": {  
                        "maxOrderQty": "1190.000",  
                        "minOrderQty": "0.001",  
                        "qtyStep": "0.001",  
                        "postOnlyMaxOrderQty": "1190.000",  
                        "maxMktOrderQty": "500.000",  
                        "minNotionalValue": "5"  
                    },  
                    "unifiedMarginTrade": true,  
                    "fundingInterval": 480,  
                    "settleCoin": "USDT",  
                    "copyTrading": "both",  
                    "upperFundingRate": "0.00375",  
                    "lowerFundingRate": "-0.00375",  
                    "isPreListing": false,  
                    "preListingInfo": null,  
                    "riskParameters": {  
                        "priceLimitRatioX": "0.01",  
                        "priceLimitRatioY": "0.02"  
                    },  
                    "symbolType": ""  
                }  
            ],  
            "nextPageCursor": ""  
        },  
        "retExtInfo": {},  
        "time": 1735809771618  
    }  
      
    // 盤前永續合約的響應  
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "category": "linear",  
            "list": [  
                {  
                    "symbol": "BIOUSDT",  
                    "contractType": "LinearPerpetual",  
                    "status": "PreLaunch",  
                    "baseCoin": "BIO",  
                    "quoteCoin": "USDT",  
                    "launchTime": "1735032510000",  
                    "deliveryTime": "0",  
                    "deliveryFeeRate": "",  
                    "priceScale": "4",  
                    "leverageFilter": {  
                        "minLeverage": "1",  
                        "maxLeverage": "5.00",  
                        "leverageStep": "0.01"  
                    },  
                    "priceFilter": {  
                        "minPrice": "0.0001",  
                        "maxPrice": "1999.9998",  
                        "tickSize": "0.0001"  
                    },  
                    "lotSizeFilter": {  
                        "maxOrderQty": "70000",  
                        "minOrderQty": "1",  
                        "qtyStep": "1",  
                        "postOnlyMaxOrderQty": "70000",  
                        "maxMktOrderQty": "14000",  
                        "minNotionalValue": "5"  
                    },  
                    "unifiedMarginTrade": true,  
                    "fundingInterval": 480,  
                    "settleCoin": "USDT",  
                    "copyTrading": "none",  
                    "upperFundingRate": "0.05",  
                    "lowerFundingRate": "-0.05",  
                    "isPreListing": true,  
                    "preListingInfo": {  
                        "curAuctionPhase": "ContinuousTrading",  
                        "phases": [  
                            {  
                                "phase": "CallAuction",  
                                "startTime": "1735113600000",  
                                "endTime": "1735116600000"  
                            },  
                            {  
                                "phase": "CallAuctionNoCancel",  
                                "startTime": "1735116600000",  
                                "endTime": "1735116900000"  
                            },  
                            {  
                                "phase": "CrossMatching",  
                                "startTime": "1735116900000",  
                                "endTime": "1735117200000"  
                            },  
                            {  
                                "phase": "ContinuousTrading",  
                                "startTime": "1735117200000",  
                                "endTime": ""  
                            }  
                        ],  
                        "auctionFeeInfo": {  
                            "auctionFeeRate": "0",  
                            "takerFeeRate": "0.001",  
                            "makerFeeRate": "0.0004"  
                        }  
                    },  
                    "riskParameters": {  
                        "priceLimitRatioX": "0.05",  
                        "priceLimitRatioY": "0.1"  
                    },  
                    "symbolType": ""  
                }  
            ],  
            "nextPageCursor": "first%3DBIOUSDT%26last%3DBIOUSDT"  
        },  
        "retExtInfo": {},  
        "time": 1735810114435  
    }  
    
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "category": "option",  
            "nextPageCursor": "",  
            "list": [  
                {  
                    "symbol": "BTC-27MAR26-70000-P-USDT",  
                    "status": "Trading",  
                    "baseCoin": "BTC",  
                    "quoteCoin": "USDT",  
                    "settleCoin": "USDT",  
                    "optionsType": "Put",  
                    "launchTime": "1743669649256",  
                    "deliveryTime": "1774598400000",  
                    "deliveryFeeRate": "0.00015",  
                    "priceFilter": {  
                        "minPrice": "5",  
                        "maxPrice": "1110000",  
                        "tickSize": "5"  
                    },  
                    "lotSizeFilter": {  
                        "maxOrderQty": "500",  
                        "minOrderQty": "0.01",  
                        "qtyStep": "0.01"  
                    },  
                    "displayName": "BTCUSDT-27MAR26-70000-P"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1672712537130  
    }  
    
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "category": "spot",  
            "list": [  
                {  
                    "symbolId": 9,  
                    "symbol": "BTCUSDT",  
                    "baseCoin": "BTC",  
                    "quoteCoin": "USDT",  
                    "innovation": "0",  
                    "status": "Trading",  
                    "marginTrading": "utaOnly",  
                    "stTag": "0",  
                    "lotSizeFilter": {  
                        "basePrecision": "0.000001",  
                        "quotePrecision": "0.0000001",  
                        "minOrderQty": "0.000011",  
                        "maxOrderQty": "83",  
                        "minOrderAmt": "5",  
                        "maxOrderAmt": "8000000",  
                        "maxLimitOrderQty": "83",  
                        "maxMarketOrderQty": "41.5",  
                        "postOnlyMaxLimitOrderSize":"60000"  
                    },  
                    "priceFilter": {  
                        "tickSize": "0.1"  
                    },  
                    "riskParameters": {  
                        "priceLimitRatioX": "0.005",  
                        "priceLimitRatioY": "0.01"  
                    },  
                    "symbolType": ""  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1760027412300  
    }