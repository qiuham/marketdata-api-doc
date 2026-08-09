---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/position/move-position
api_type: Position
updated_at: 2026-08-09 18:46:02.047283
---

# Set Trading Stop

Set the take profit, stop loss or trailing stop for the position.

tip

Passing these parameters will create conditional orders by the system internally. The system will cancel these orders if the position is closed, and adjust the qty according to the size of the open position.

info

New version of TP/SL function supports both holding entire position TP/SL orders and holding partial position TP/SL orders.

  * Full position TP/SL orders: This API can be used to modify the parameters of existing TP/SL orders.
  * Partial position TP/SL orders: This API can only add partial position TP/SL orders.



note

Under the new version of TP/SL function, when calling this API to perform one-sided take profit or stop loss modification on existing TP/SL orders on the holding position, it will cause the paired tp/sl orders to lose binding relationship. This means that when calling the cancel API through the tp/sl order ID, it will only cancel the corresponding one-sided take profit or stop loss order ID.

### HTTP Request

POST`/v5/position/trading-stop`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
[category](/docs/v5/enum#category)| **true**|  string| Product type `linear`, `inverse`, `option`  
symbol| **true**|  string| Symbol name, like `BTCUSDT`, uppercase only  
tpslMode| **true**|  string| TP/SL mode

  * `Full`: entire position TP/SL, option supports "tpslMode"=`Full` only
  * `Partial`: partial position TP/SL

  
[positionIdx](/docs/v5/enum#positionidx)| true| integer| Used to identify positions in different position modes. 

  * `0`: one-way mode
  * `1`: hedge-mode Buy side
  * `2`: hedge-mode Sell side

  
takeProfit| false| string| Cannot be less than 0, 0 means cancel TP  
stopLoss| false| string| Cannot be less than 0, 0 means cancel SL  
trailingStop| false| string| Trailing stop by price distance. Cannot be less than 0, 0 means cancel TS  
[tpTriggerBy](/docs/v5/enum#triggerby)| false| string| Take profit trigger price type  
[slTriggerBy](/docs/v5/enum#triggerby)| false| string| Stop loss trigger price type  
activePrice| false| string| Trailing stop trigger price. Trailing stop will be triggered when this price is reached **only**  
tpSize| false| string| Take profit size  
valid for TP/SL partial mode, note: the value of tpSize and slSize must equal  
slSize| false| string| Stop loss size  
valid for TP/SL partial mode, note: the value of tpSize and slSize must equal  
tpLimitPrice| false| string| The limit order price when take profit price is triggered. Only works when tpslMode=Partial and tpOrderType=Limit  
slLimitPrice| false| string| The limit order price when stop loss price is triggered. Only works when tpslMode=Partial and slOrderType=Limit  
tpOrderType| false| string| The order type when take profit is triggered. `Market`(default), `Limit`  
For tpslMode=Full, it only supports tpOrderType="Market"  
slOrderType| false| string| The order type when stop loss is triggered. `Market`(default), `Limit`  
For tpslMode=Full, it only supports slOrderType="Market"  
  
### Response Parameters

None

[](/docs/api-explorer/v5/position/trading-stop)

* * *

### Request Example

  * HTTP
  * Python
  * Java
  * Node.js


    
    
    POST /v5/position/trading-stop HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672283124270  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "category":"linear",  
        "symbol": "XRPUSDT",  
        "takeProfit": "0.6",  
        "stopLoss": "0.2",  
        "tpTriggerBy": "MarkPrice",  
        "slTriggerBy": "IndexPrice",  
        "tpslMode": "Partial",  
        "tpOrderType": "Limit",  
        "slOrderType": "Limit",  
        "tpSize": "50",  
        "slSize": "50",  
        "tpLimitPrice": "0.57",  
        "slLimitPrice": "0.21",  
        "positionIdx": 0  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.set_trading_stop(  
        category="linear",  
        symbol="XRPUSDT",  
        takeProfit="0.6",  
        stopLoss="0.2",  
        tpTriggerBy="MarkPrice",  
        slTriggerB="IndexPrice",  
        tpslMode="Partial",  
        tpOrderType="Limit",  
        slOrderType="Limit",  
        tpSize="50",  
        slSize="50",  
        tpLimitPrice="0.57",  
        slLimitPrice="0.21",  
        positionIdx=0,  
    ))  
    
    
    
    import com.bybit.api.client.domain.*;  
    import com.bybit.api.client.domain.position.*;  
    import com.bybit.api.client.domain.position.request.*;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    var client = BybitApiClientFactory.newInstance().newAsyncPositionRestClient();  
    var setTradingStopRequest = PositionDataRequest.builder().category(CategoryType.LINEAR).symbol("XRPUSDT").takeProfit("0.6").stopLoss("0.2").tpTriggerBy(TriggerBy.MARK_PRICE).slTriggerBy(TriggerBy.LAST_PRICE)  
                    .tpslMode(TpslMode.PARTIAL).tpOrderType(TradeOrderType.LIMIT).slOrderType(TradeOrderType.LIMIT).tpSize("50").slSize("50").tpLimitPrice("0.57").slLimitPrice("0.21").build();  
    client.setTradingStop(setTradingStopRequest, System.out::println);  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
        key: 'xxxxxxxxxxxxxxxxxx',  
        secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
        .setTradingStop({  
            category: 'linear',  
            symbol: 'XRPUSDT',  
            takeProfit: '0.6',  
            stopLoss: '0.2',  
            tpTriggerBy: 'MarkPrice',  
            slTriggerBy: 'IndexPrice',  
            tpslMode: 'Partial',  
            tpOrderType: 'Limit',  
            slOrderType: 'Limit',  
            tpSize: '50',  
            slSize: '50',  
            tpLimitPrice: '0.57',  
            slLimitPrice: '0.21',  
            positionIdx: 0,  
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
        "result": {},  
        "retExtInfo": {},  
        "time": 1672283125359  
    }

---

# 設置止盈止損

該接口可以設置止盈、止損和追蹤止損

提示

在提交請求後，系統內部將會自動創建對應類型的條件單。若倉位被平，系統將會調整相關條件訂單數量或者取消這些條件單。

信息

新版止盈止損, 支持既持有全部止盈止損單, 也可以持有部分止盈止損單

  * 全部倉位止盈止損單: 該接口可用於修改該類型的止盈止損單的參數
  * 部分倉位止盈止損單: 該接口僅能新增部分倉位止盈止損單



備註

新版止盈止損下, 調用該接口對持倉上的已有的止盈止損進行單邊止盈或者止損修改時, 會導致成對的tp/sl訂單失去綁定關係, 這意味著當通過tp/sl訂單ID調用 取消接口時, 只會取消對應訂單ID的單邊止盈或止損.

### HTTP 請求

POST`/v5/position/trading-stop`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
[category](/docs/zh-TW/v5/enum#category)| **true**|  string| 產品類型 `linear`, `inverse`, `option`  
symbol| **true**|  string| 合約名稱  
tpslMode| **true**|  string| 止盈止損模式. `Full`: 全部倉位止盈止損, 期權僅支持`Full` `Partial`: 部分倉位止盈止損  
[positionIdx](/docs/zh-TW/v5/enum#positionidx)| true| integer| 倉位標識，用戶識別倉位. 

  * `0`: 單向持倉
  * `1`: 買側雙向持倉
  * `2`: 賣側雙向持倉

  
takeProfit| false| string| 止盈價格. 等於0表示取消止盈，若不修改，則不要傳遞該參數  
stopLoss| false| string| 止損價格. 等於0表示取消止損，若不修改，則不要傳遞該參數  
trailingStop| false| string| 追蹤止損, 僅支持按價差設置. 等於0表示取消追蹤止損，若不修改，則不要傳遞該參數  
[tpTriggerBy](/docs/zh-TW/v5/enum#triggerby)| false| string| 止盈價格類型  
[slTriggerBy](/docs/zh-TW/v5/enum#triggerby)| false| string| 止損價格類型  
activePrice| false| string| 追蹤止損激活價格. 追蹤止損會在到達該價格時觸發  
tpSize| false| string| 止盈倉位數量. 僅部分止盈止損時有效. 注意: tpSize和slSize的數值必須相等  
slSize| false| string| 止損倉位數量. 僅部分止盈止損時有效. 注意: tpSize和slSize的數值必須相等  
tpLimitPrice| false| string| 觸發止盈後轉換為限價單的價格  
僅tpslMode=Partial且tpOrderType=Limit時有效  
slLimitPrice| false| string| 觸發止損後轉換為限價單的價格  
僅tpslMode=Partial且slOrderType=Limit時有效  
tpOrderType| false| string| 止盈觸發後的訂單類型. `Market`(默認), `Limit`  
對於tpslMode=Full時, 僅支持tpOrderType=Market  
slOrderType| false| string| 止損觸發後的訂單類型. `Market`(默認), `Limit`  
對於tpslMode=Full時, 僅支持slOrderType=Market  
[](/docs/zh-TW/api-explorer/v5/position/trading-stop)

* * *

### 響應參數

無

### 請求示例

  * HTTP
  * Python
  * Java
  * Node.js


    
    
    POST /v5/position/trading-stop HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672283124270  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "category":"linear",  
        "symbol": "XRPUSDT",  
        "takeProfit": "0.6",  
        "stopLoss": "0.2",  
        "tpTriggerBy": "MarkPrice",  
        "slTriggerBy": "IndexPrice",  
        "tpslMode": "Partial",  
        "tpOrderType": "Limit",  
        "slOrderType": "Limit",  
        "tpSize": "50",  
        "tpLimitPrice": "0.57",  
        "slLimitPrice": "0.21",  
        "positionIdx": 0  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.set_trading_stop(  
        category="linear",  
        symbol="XRPUSDT",  
        takeProfit="0.6",  
        stopLoss="0.2",  
        tpTriggerBy="MarkPrice",  
        slTriggerB="IndexPrice",  
        tpslMode="Partial",  
        tpOrderType="Limit",  
        slOrderType="Limit",  
        tpSize="50",  
        slSize="50",  
        tpLimitPrice="0.57",  
        slLimitPrice="0.21",  
        positionIdx=0,  
    ))  
    
    
    
    import com.bybit.api.client.domain.*;  
    import com.bybit.api.client.domain.position.*;  
    import com.bybit.api.client.domain.position.request.*;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    var client = BybitApiClientFactory.newInstance().newAsyncPositionRestClient();  
    var setTradingStopRequest = PositionDataRequest.builder().category(CategoryType.LINEAR).symbol("XRPUSDT").takeProfit("0.6").stopLoss("0.2").tpTriggerBy(TriggerBy.MARK_PRICE).slTriggerBy(TriggerBy.LAST_PRICE)  
                    .tpslMode(TpslMode.PARTIAL).tpOrderType(TradeOrderType.LIMIT).slOrderType(TradeOrderType.LIMIT).tpSize("50").slSize("50").tpLimitPrice("0.57").slLimitPrice("0.21").build();  
    client.setTradingStop(setTradingStopRequest, System.out::println);  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
        key: 'xxxxxxxxxxxxxxxxxx',  
        secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
        .setTradingStop({  
            category: 'linear',  
            symbol: 'XRPUSDT',  
            takeProfit: '0.6',  
            stopLoss: '0.2',  
            tpTriggerBy: 'MarkPrice',  
            slTriggerBy: 'IndexPrice',  
            tpslMode: 'Partial',  
            tpOrderType: 'Limit',  
            slOrderType: 'Limit',  
            tpSize: '50',  
            slSize: '50',  
            tpLimitPrice: '0.57',  
            slLimitPrice: '0.21',  
            positionIdx: 0,  
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
        "result": {},  
        "retExtInfo": {},  
        "time": 1672283125359  
    }