---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/order/execution
api_type: Trading
updated_at: 2026-08-17 18:45:13.232296
---

# Get Borrow Quota (Spot)

Query the available balance for Spot trading and Margin trading

info

  * During periods of extreme market volatility, this interface may experience increased latency or temporary delays in data delivery



### HTTP Request

GET`/v5/order/spot-borrow-check`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
[category](/docs/v5/enum#category)| **true**|  string| Product type `spot`  
symbol| **true**|  string| Symbol name  
side| **true**|  string| Transaction side. `Buy`,`Sell`  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
symbol| string| Symbol name, like `BTCUSDT`, uppercase only  
side| string| Side  
maxTradeQty| string| The maximum base coin qty can be traded

  * If spot margin trade on and symbol is margin trading pair, it returns available balance + max.borrowable quantity = min(The maximum quantity that a single user can borrow on the platform, The maximum quantity that can be borrowed calculated by IMR MMR of UTA account, The available quantity of the platform's capital pool) 
  * Otherwise, it returns actual available balance
  * up to 4 decimals

  
maxTradeAmount| string| The maximum quote coin amount can be traded

  * If spot margin trade on and symbol is margin trading pair, it returns available balance + max.borrowable amount = min(The maximum amount that a single user can borrow on the platform, The maximum amount that can be borrowed calculated by IMR MMR of UTA account, The available amount of the platform's capital pool) 
  * Otherwise, it returns actual available balance
  * up to 8 decimals

  
spotMaxTradeQty| string| No matter your Spot margin switch on or not, it always returns actual qty of base coin you can trade or you have (borrowable qty is not included), up to 4 decimals  
spotMaxTradeAmount| string| No matter your Spot margin switch on or not, it always returns actual amount of quote coin you can trade or you have (borrowable amount is not included), up to 8 decimals  
borrowCoin| string| Borrow coin  
[](/docs/api-explorer/v5/trade/query-spot-quota)

* * *

### Request Example

  * HTTP
  * Python
  * Java
  * Node.js


    
    
    GET /v5/order/spot-borrow-check?category=spot&symbol=BTCUSDT&side=Buy HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672228522214  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_borrow_quota(  
        category="spot",  
        symbol="BTCUSDT",  
        side="Buy",  
    ))  
    
    
    
    import com.bybit.api.client.config.BybitApiConfig;  
    import com.bybit.api.client.domain.trade.request.TradeOrderRequest;  
    import com.bybit.api.client.domain.*;  
    import com.bybit.api.client.domain.trade.*;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    var client = BybitApiClientFactory.newInstance("YOUR_API_KEY", "YOUR_API_SECRET", BybitApiConfig.TESTNET_DOMAIN).newTradeRestClient();  
    var getBorrowQuotaRequest = TradeOrderRequest.builder().category(CategoryType.SPOT).symbol("BTCUSDT").side(Side.BUY).build();  
    System.out.println(client.getBorrowQuota(getBorrowQuotaRequest));  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
        key: 'xxxxxxxxxxxxxxxxxx',  
        secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
        .getSpotBorrowCheck('BTCUSDT', 'Buy')  
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
            "symbol": "BTCUSDT",  
            "maxTradeQty": "6.6065",  
            "side": "Buy",  
            "spotMaxTradeAmount": "9004.75628594",  
            "maxTradeAmount": "218014.01330797",  
            "borrowCoin": "USDT",  
            "spotMaxTradeQty": "0.2728"  
        },  
        "retExtInfo": {},  
        "time": 1698895841534  
    }

---

# 查詢用戶可用額度 (現貨)

可以查詢現貨幣幣交易以及槓桿交易時, 可用對應幣種的實時餘額

信息

  * 在極端市場波動期間, 此介面可能會出現延遲增加或資料傳遞暫時延遲的情況



### HTTP請求

GET`/v5/order/spot-borrow-check`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
[category](/docs/zh-TW/v5/enum#category)| **true**|  string| 產品類型 `spot`  
symbol| **true**|  string| 交易對名稱  
side| **true**|  string| 交易方向. `Buy`,`Sell`  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
symbol| string| 交易對名稱  
side| string| 方向  
maxTradeQty| string| 最大可用於交易的交易幣種數量

  * 若啟用了全倉槓桿且是槓桿幣對, 則返回現貨可用+最大可借貸數量 = min(平台單一用戶可借貸上限，UTA帳戶IMR MMR反推出來的最大可借，平台資金池可用額度)
  * 否則, 僅代表現貨可用
  * 最多支持4位小數

  
maxTradeAmount| string| 最大可用於交易的報價幣種金額

  * 若啟用了全倉槓桿且是槓桿幣對, 則返回現貨可用+最大可借貸數量 = min(平台單一用戶可借貸上限，UTA帳戶IMR MMR反推出來的最大可借，平台資金池可用額度) 
  * 否則, 僅代表現貨可用
  * 最多支持8位小數

  
spotMaxTradeQty| string| 無論是否開啟了槓桿, 這個字段表示交易幣種在幣幣交易下的可交易數量或者餘額 (不包含可借貸數量), 最多支持4位小數  
spotMaxTradeAmount| string| 無論是否開啟了槓桿, 這個字段表示報價幣種在幣幣交易下的可交易數量或者餘額 (不包含可借貸數量), 最多支持8位小數  
borrowCoin| string| 借貸幣種  
[](/docs/zh-TW/api-explorer/v5/trade/query-spot-quota)

* * *

### 請求示例

  * HTTP
  * Python
  * Java
  * Node.js


    
    
    GET /v5/order/spot-borrow-check?category=spot&symbol=BTCUSDT&side=Buy HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672228522214  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_borrow_quota(  
        category="spot",  
        symbol="BTCUSDT",  
        side="Buy",  
    ))  
    
    
    
    import com.bybit.api.client.config.BybitApiConfig;  
    import com.bybit.api.client.domain.trade.request.TradeOrderRequest;  
    import com.bybit.api.client.domain.*;  
    import com.bybit.api.client.domain.trade.*;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    var client = BybitApiClientFactory.newInstance("YOUR_API_KEY", "YOUR_API_SECRET", BybitApiConfig.TESTNET_DOMAIN).newTradeRestClient();  
    var getBorrowQuotaRequest = TradeOrderRequest.builder().category(CategoryType.SPOT).symbol("BTCUSDT").side(Side.BUY).build();  
    System.out.println(client.getBorrowQuota(getBorrowQuotaRequest));  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
        key: 'xxxxxxxxxxxxxxxxxx',  
        secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
        .getSpotBorrowCheck('BTCUSDT', 'Buy')  
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
            "symbol": "BTCUSDT",  
            "maxTradeQty": "6.6065",  
            "side": "Buy",  
            "spotMaxTradeAmount": "9004.75628594",  
            "maxTradeAmount": "218014.01330797",  
            "borrowCoin": "USDT",  
            "spotMaxTradeQty": "0.2728"  
        },  
        "retExtInfo": {},  
        "time": 1698895841534  
    }