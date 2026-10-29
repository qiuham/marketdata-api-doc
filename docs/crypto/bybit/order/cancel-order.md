---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/order/cancel-order
api_type: Trading
updated_at: 2026-10-29 18:40:17.847103
---

# Get Trade History

Query users' execution records, sorted by `execTime` in descending order.

tip

  * Response items will have sorting issues when 'execTime' is the same, it is recommended to sort according to `execId+OrderId+leavesQty`. If you want to receive real-time execution information, Use the [websocket stream](/docs/v5/websocket/private/execution) (recommended).
  * You may have multiple executions in a single order.
  * You can query by symbol, baseCoin, orderId and orderLinkId, and if you pass multiple params, the system will process them according to this priority: orderId > orderLinkId > symbol > baseCoin. orderId and orderLinkId have a higher priority and as long as these two parameters are in the input parameters, other input parameters will be ignored.



### HTTP Request

GET`/v5/execution/list`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
[category](/docs/v5/enum#category)| **true**|  string| Product type `linear`, `inverse`, `spot`, `option`  
symbol| false| string| Symbol name, like `BTCUSDT`, uppercase only  
orderId| false| string| Order ID  
orderLinkId| false| string| User customised order ID  
baseCoin| false| string| Base coin, uppercase only. For type `option`, default value is BTC  
settleCoin| false| string| Settle coin, uppercase only. Only for `linear`, `inverse`,`option`  
startTime| false| integer| The start timestamp (ms) 

  * startTime and endTime are not passed, return 7 days by default
  * Only startTime is passed, return range between startTime and startTime+7 days
  * Only endTime is passed, return range between endTime-7 days and endTime  
If both are passed, the rule is endTime - startTime <= 7 days

  
endTime| false| integer| The end timestamp (ms)  
[execType](/docs/v5/enum#exectype)| false| string| Execution type  
limit| false| integer| Limit for data size per page. [`1`, `100`]. Default: `50`  
cursor| false| string| Cursor. Use the `nextPageCursor` token from the response to retrieve the next page of the result set  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
[category](/docs/v5/enum#category)| string| Product type  
list| array| Object  
> symbol| string| Symbol name  
> orderId| string| Order ID  
> orderLinkId| string| User customized order ID  
> side| string| Side. `Buy`,`Sell`  
> orderPrice| string| Order price  
> orderQty| string| Order qty  
> leavesQty| string| The remaining qty not executed  
> [createType](/docs/v5/enum#createtype)| string| Order create type 
* Spot does not have this key  
> [orderType](/docs/v5/enum#ordertype)| string| Order type. `Market`,`Limit`  
> [stopOrderType](/docs/v5/enum#stopordertype)| string| Stop order type. If the order is not stop order, it either returns `UNKNOWN` or `""`  
> execFee| string| Executed trading fee. You can get spot fee currency instruction [here](/docs/v5/enum#spot-fee-currency-instruction)  
> execFeeV2| string| Spot leg transaction fee, only works for execType=`FutureSpread`  
> execId| string| Execution ID  
> execPrice| string| Execution price  
> execQty| string| Execution qty  
> [execType](/docs/v5/enum#exectype)| string| Executed type  
> execValue| string| Executed order value  
> execTime| string| Executed timestamp (ms)  
> feeCurrency| string| Trading fee currency  
> isMaker| boolean| Is maker order. `true`: maker, `false`: taker  
> feeRate| string| Trading fee rate  
> tradeIv| string| Implied volatility. _Valid for`option`_  
> markIv| string| Implied volatility of mark price. _Valid for`option`_  
> markPrice| string| The mark price of the symbol when executing  
> indexPrice| string| The index price of the symbol when executing. _Valid for`option` only_  
> underlyingPrice| string| The underlying price of the symbol when executing. _Valid for`option`_  
> blockTradeId| string| Paradigm block trade ID  
> closedSize| string| Closed position size  
> seq| long| Cross sequence, used to associate each fill and each position update

  * The seq will be the same when conclude multiple transactions at the same time
  * Different symbols may have the same seq, please use seq + symbol to check unique

  
> extraFees| string| Trading fee rate information. Currently, this data is returned only for kyc=Indian user or spot orders placed on the Indonesian site or spot fiat currency orders placed on the EU site. In other cases, an empty string is returned. Enum: [feeType](/docs/v5/enum#extrafeesfeetype), [subFeeType](/docs/v5/enum#extrafeessubfeetype)  
nextPageCursor| string| Refer to the `cursor` request parameter  
[](/docs/api-explorer/v5/position/execution)

* * *

### Request Example

  * HTTP
  * Python
  * Java
  * Node.js


    
    
    GET /v5/execution/list?category=linear&limit=1 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672283754132  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_executions(  
        category="linear",  
        limit=1,  
    ))  
    
    
    
    import com.bybit.api.client.config.BybitApiConfig;  
    import com.bybit.api.client.domain.trade.request.TradeOrderRequest;  
    import com.bybit.api.client.domain.*;  
    import com.bybit.api.client.domain.trade.*;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    var client = BybitApiClientFactory.newInstance("YOUR_API_KEY", "YOUR_API_SECRET", BybitApiConfig.TESTNET_DOMAIN).newTradeRestClient();  
    var tradeHistoryRequest = TradeOrderRequest.builder().category(CategoryType.LINEAR).symbol("BTCUSDT").execType(ExecType.Trade).limit(100).build();  
    System.out.println(client.getTradeHistory(tradeHistoryRequest));  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
        key: 'xxxxxxxxxxxxxxxxxx',  
        secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
        .getExecutionList({  
            category: 'linear',  
            symbol: 'BTCUSDT',  
            margin: '10',  
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
            "nextPageCursor": "132766%3A2%2C132766%3A2",  
            "category": "linear",  
            "list": [  
                {  
                    "symbol": "ETHPERP",  
                    "orderType": "Market",  
                    "underlyingPrice": "",  
                    "orderLinkId": "",  
                    "side": "Buy",  
                    "indexPrice": "",  
                    "orderId": "8c065341-7b52-4ca9-ac2c-37e31ac55c94",  
                    "stopOrderType": "UNKNOWN",  
                    "leavesQty": "0",  
                    "execTime": "1672282722429",  
                    "feeCurrency": "",  
                    "isMaker": false,  
                    "execFee": "0.071409",  
                    "feeRate": "0.0006",  
                    "execId": "e0cbe81d-0f18-5866-9415-cf319b5dab3b",  
                    "tradeIv": "",  
                    "blockTradeId": "",  
                    "markPrice": "1183.54",  
                    "execPrice": "1190.15",  
                    "markIv": "",  
                    "orderQty": "0.1",  
                    "orderPrice": "1236.9",  
                    "execValue": "119.015",  
                    "execType": "Trade",  
                    "execQty": "0.1",  
                    "closedSize": "",  
                    "extraFees": "",  
                    "seq": 4688002127  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1672283754510  
    }

---

# 查詢成交紀錄

獲取用戶成交紀錄，返回結果按`execTime`降序排列

提示

  * 儅execTime相同時,返回會有排序問題，此問題已在優化中, 目前建議依照`execId+OrderId+leavesQty`進行排序, 如果您想獲取實時成交信息建議使用[websocket stream](/docs/zh-TW/v5/websocket/private/execution).
  * 單筆訂單可能會有多次成交.
  * 您可以通過指定symbol, baseCoin, orderId 和 orderLinkId字段來查詢。如果您使用多字段組合，系統的查詢優先級如下: orderId > orderLinkId > symbol > baseCoin. orderId 和 orderLinkId 優先權較高，只要輸入參數中有這兩個參數，其他輸入參數將被忽略。



### HTTP 請求

GET`/v5/execution/list`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
[category](/docs/zh-TW/v5/enum#category)| **true**|  string| 產品類型 `spot`, `linear`, `inverse`, `option`  
symbol| false| string| 合約名稱  
orderId| false| string| 訂單Id  
orderLinkId| false| string| 用戶自定義訂單id  
baseCoin| false| string| 交易幣種. 對於期權來說，默认是BTC  
settleCoin| false| string| 结算幣種. 只支持 `linear`, `inverse`,`option`  
startTime| false| integer| 開始時間戳 (毫秒) 

  * startTime 和 endTime都不傳入, 則默認返回最近7天的數據
  * startTime 和 endTime都傳入的話, 則確保endTime - startTime ≤ 7天
  * 若只傳startTime, 則查詢startTime和startTime+7天的數據
  * 若只傳endTime, 則查詢endTime-7天和endTime的數據

  
endTime| false| integer| 結束時間戳 (毫秒)  
[execType](/docs/zh-TW/v5/enum#exectype)| false| string| 執行類型  
limit| false| integer| 每頁數量限制. [`1`, `100`]. 默認: `50`  
cursor| false| string| 游標，用於翻頁  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
[category](/docs/zh-TW/v5/enum#category)| string| 產品類型  
list| array| Object  
> symbol| string| 合約名稱  
> orderId| string| 訂單Id  
> orderLinkId| string| 用戶自定義訂單id  
> side| string| 訂單方向.買： `Buy`,賣：`Sell`  
> orderPrice| string| 訂單價格  
> orderQty| string| 訂單數量  
> leavesQty| string| 剩餘委託未成交數量  
> [createType](/docs/zh-TW/v5/enum#createtype)| string| 訂單創建類型
* 現貨不返回該字段  
> [orderType](/docs/zh-TW/v5/enum#ordertype)| string| 訂單類型. 市價單：`Market`,限價單：`Limit`  
> [stopOrderType](/docs/zh-TW/v5/enum#stopordertype)| string| 条件单的订单类型。如果该订单不是条件单，则可能返回`""`或者`UNKNOWN`.  
> execFee| string| 交易手續費. 您可以從[這裡](/docs/zh-TW/v5/enum#%E7%8F%BE%E8%B2%A8%E4%BA%A4%E6%98%93%E6%89%8B%E7%BA%8C%E8%B2%BB%E5%B9%A3%E7%A8%AE%E8%AA%AA%E6%98%8E)了解現貨手續費幣種信息  
> execFeeV2| string| 價差交易下現貨單腿的交易手續費  
> execId| string| 成交Id  
> execPrice| string| 成交價格  
> execQty| string| 成交數量  
> [execType](/docs/zh-TW/v5/enum#exectype)| string| 交易類型  
> execValue| string| 成交價值.  
> execTime| string| 成交時間（毫秒）  
> feeCurrency| string| 手續費幣種  
> isMaker| Bool| 是否是 Maker 訂單,`true` 為 maker 訂單，`false` 為 taker 訂單  
> feeRate| string| 手續費率  
> tradeIv| string| 隱含波動率，僅期權有效  
> markIv| string| 標記價格的隱含波動率，僅期權有效  
> markPrice| string| 成交執行時，該 symbol 當時的標記價格  
> indexPrice| string| 成交執行時，該 symbol 當時的指數價格   
僅期權業務有效  
> underlyingPrice| string| 成交執行時，該 symbol 當時的底層資產價格  
僅期權有效  
> blockTradeId| string| 大宗交易的订单 ID ，使用 paradigm 进行大宗交易时生成的 ID  
> closedSize| string| 平倉數量  
> seq| long| 序列號, 用於關聯成交和倉位的更新

  * 同一時間有多筆成交, seq相同
  * 不同的幣對會存在相同seq, 可以使用seq + symbol來做唯一性識別

  
> extraFees| string| 交易費率。目前，僅針對kyc=Indian用戶或在印尼網站的現貨訂單或在歐盟站的現貨法定貨幣訂單返回此數據。在其他情況下，傳回空字串。字段枚舉: [feeType](/docs/zh-TW/v5/enum#extrafeesfeetype), [subFeeType](/docs/zh-TW/v5/enum#extrafeessubfeetype)  
nextPageCursor| string| 游標，用於翻頁  
[](/docs/zh-TW/api-explorer/v5/position/execution)

* * *

### 請求示例

  * HTTP
  * Python
  * Java
  * Node.js


    
    
    GET /v5/execution/list?category=linear&limit=1 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672283754132  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_executions(  
        category="linear",  
        limit=1,  
    ))  
    
    
    
    import com.bybit.api.client.config.BybitApiConfig;  
    import com.bybit.api.client.domain.trade.request.TradeOrderRequest;  
    import com.bybit.api.client.domain.*;  
    import com.bybit.api.client.domain.trade.*;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    var client = BybitApiClientFactory.newInstance("YOUR_API_KEY", "YOUR_API_SECRET", BybitApiConfig.TESTNET_DOMAIN).newTradeRestClient();  
    var tradeHistoryRequest = TradeOrderRequest.builder().category(CategoryType.LINEAR).symbol("BTCUSDT").execType(ExecType.Trade).limit(100).build();  
    System.out.println(client.getTradeHistory(tradeHistoryRequest));  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
        key: 'xxxxxxxxxxxxxxxxxx',  
        secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
        .getExecutionList({  
            category: 'linear',  
            symbol: 'BTCUSDT',  
            margin: '10',  
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
            "nextPageCursor": "132766%3A2%2C132766%3A2",  
            "category": "linear",  
            "list": [  
                {  
                    "symbol": "ETHPERP",  
                    "orderType": "Market",  
                    "underlyingPrice": "",  
                    "orderLinkId": "",  
                    "side": "Buy",  
                    "indexPrice": "",  
                    "orderId": "8c065341-7b52-4ca9-ac2c-37e31ac55c94",  
                    "stopOrderType": "UNKNOWN",  
                    "leavesQty": "0",  
                    "execTime": "1672282722429",  
                    "feeCurrency": "",  
                    "isMaker": false,  
                    "execFee": "0.071409",  
                    "feeRate": "0.0006",  
                    "execId": "e0cbe81d-0f18-5866-9415-cf319b5dab3b",  
                    "tradeIv": "",  
                    "blockTradeId": "",  
                    "markPrice": "1183.54",  
                    "execPrice": "1190.15",  
                    "markIv": "",  
                    "orderQty": "0.1",  
                    "orderPrice": "1236.9",  
                    "execValue": "119.015",  
                    "execType": "Trade",  
                    "execQty": "0.1",  
                    "closedSize": "0.1",  
                    "seq": 4688002127,  
                    "extraFees":""  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1672283754510  
    }