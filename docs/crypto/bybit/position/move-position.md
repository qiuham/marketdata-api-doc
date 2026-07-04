---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/position/move-position
api_type: Position
updated_at: 2026-07-04 19:09:32.961891
---

# Switch Position Mode

It supports to switch the position mode for **USDT perpetual** and **Inverse futures**. If you are in one-way Mode, you can only open one position on Buy or Sell side. If you are in hedge mode, you can open both Buy and Sell side positions simultaneously.

tip

  * Priority for configuration to take effect: symbol > coin > system default
  * System default: one-way mode
  * If the request is by coin (settleCoin), then all symbols based on this setteCoin that do not have position and open order will be batch switched, and new listed symbol based on this settleCoin will be the same mode you set.



### Example

| System default| coin| symbol  
---|---|---|---  
Initial setting| one-way| never configured| never configured  
Result| All USDT perpetual trading pairs are one-way mode  
**Change 1**|  -| -| Set BTCUSDT to hedge-mode  
Result| BTCUSDT becomes hedge-mode, and all other symbols keep one-way mode  
list new symbol ETHUSDT| ETHUSDT is one-way mode (inherit default rules)   
**Change 2**|  -| Set USDT to hedge-mode| -  
Result| All current trading pairs with no positions or orders are hedge-mode, and no adjustments will be made for trading pairs with positions and orders  
list new symbol SOLUSDT| SOLUSDT is hedge-mode (Inherit coin rule)  
**Change 3**|  -| -| Set ASXUSDT to one-mode  
Take effect result| AXSUSDT is one-way mode, other trading pairs have no change  
list new symbol BITUSDT| BITUSDT is hedge-mode (Inherit coin rule)  
  
### The position-switch ability for each contract

| UTA2.0  
---|---  
USDT perpetual| **Support one-way & hedge-mode**  
USDT futures| Support one-way **only**  
USDC perpetual| Support one-way **only**  
Inverse perpetual| Support one-way **only**  
Inverse futures| Support one-way **only**  
  
### HTTP Request

POST`/v5/position/switch-mode`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
[category](/docs/v5/enum#category)| **true**|  string| Product type `linear`, USDT Contract  
symbol| false| string| Symbol name, like `BTCUSDT`, uppercase only. Either `symbol` or `coin` is **required**. `symbol` has a higher priority  
coin| false| string| Coin, uppercase only  
mode| **true**|  integer| Position mode. `0`: Merged Single. `3`: Both Sides  
[](/docs/api-explorer/v5/position/position-mode)

* * *

### Response Parameters

None

### Request Example

  * HTTP
  * Python
  * Java
  * Node.js


    
    
    POST /v5/position/switch-mode HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1675249072041  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 87  
      
    {  
        "category":"inverse",  
        "symbol":"BTCUSDH23",  
        "coin": null,  
        "mode": 0  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.switch_position_mode(  
        category="inverse",  
        symbol="BTCUSDH23",  
        mode=0,  
    ))  
    
    
    
    import com.bybit.api.client.domain.*;  
    import com.bybit.api.client.domain.position.*;  
    import com.bybit.api.client.domain.position.request.*;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    var client = BybitApiClientFactory.newInstance().newPositionRestClient();  
    var switchPositionMode = PositionDataRequest.builder().category(CategoryType.LINEAR).symbol("BTCUSDT").positionMode(PositionMode.BOTH_SIDES).build();  
    System.out.println(client.switchPositionMode(switchPositionMode));  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
        key: 'xxxxxxxxxxxxxxxxxx',  
        secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
        .switchPositionMode({  
            category: 'inverse',  
            symbol: 'BTCUSDH23',  
            mode: 0,  
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
        "time": 1675249072814  
    }

---

# 切換持倉模式

該接口支持切換USDT永續的持倉模式。如果處於單向持倉模式下，您只能要麼持有多頭要麼空頭倉位；如果處於雙向持倉模式下，您可以同時持倉多頭和空頭的倉位。

提示

  * 配置生效優先級: symbol > coin > 系統默認
  * 系統默認: 單向持倉
  * 如果請求是按幣種（settleCoin），則所有基於該settleCoin的交易品種沒有持倉和活動單的將被批量切換，並且基於該settleCoin的新上市交易品種將與您設置的模式相同。



### 示例

| 系統默認| coin| symbol  
---|---|---|---  
初始配置| 單向持倉| 未設置過| 未設置過  
生效結果| 所有USDT正向交易對都是單向持倉  
**變更 1**|  -| -| BTCUSDT 設置為雙向持倉模式  
生效結果| 當前交易對BTCUSDT為雙向持倉，其他交易對都是單向持倉（繼承系統默認規則  
新上線交易對 ETHUSDT| 新上線的ETHUSDT為單向持倉 （繼承系統默認規則）  
**變更 2**|  -| USDT 設置為雙向持倉| -  
生效結果| 當前所有未持倉未有訂單的交易對都是雙向持倉，有持倉和有委託單的交易對不做調整  
新上線交易對 SOLUSDT| 新上線的SOLUSDT為雙向持倉 (繼承coin規則)  
**變更 3**|  -| -| ASXUSDT 設置為單向持倉模式  
生效結果| AXSUSDT為單向持倉模式，其餘交易對不做任何變更（繼承coin規則）  
新上線交易對 BITUSDT| 新上線的BITUSDT為雙向持倉 (繼承coin規則)  
  
### 當前合約單雙向持倉切換能力

| 統一帳戶2.0  
---|---  
USDT 永續| **支持單雙向持倉**  
USDT 交割| 僅支持單向持倉  
USDC 永續| 僅支持單向持倉  
USDC 交割| 僅支持單向持倉  
反向永續| 僅支持單向持倉  
反向交割| 僅支持單向持倉  
  
### HTTP 请求

POST`/v5/position/switch-mode`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
[category](/docs/zh-TW/v5/enum#category)| **true**|  string| 產品類型 `linear`, USDT 永续  
symbol| false| string| 合約名稱. `symbol`和`coin`**必須** 傳其中一個. `symbol`有更高優先級  
coin| false| string| 結算幣種  
mode| **true**|  integer| 倉位模式. `0`: 單向持倉. `3`: 雙向持倉  
[](/docs/zh-TW/api-explorer/v5/position/position-mode)

* * *

### 響應參數

無

### 請求示例

  * HTTP
  * Python
  * Java
  * Node.js


    
    
    POST /v5/position/switch-mode HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1675249072041  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 87  
      
    {  
        "category":"inverse",  
        "symbol":"BTCUSDH23",  
        "coin": null,  
        "mode": 0  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.switch_position_mode(  
        category="inverse",  
        symbol="BTCUSDH23",  
        mode=0,  
    ))  
    
    
    
    import com.bybit.api.client.domain.*;  
    import com.bybit.api.client.domain.position.*;  
    import com.bybit.api.client.domain.position.request.*;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    var client = BybitApiClientFactory.newInstance().newPositionRestClient();  
    var switchPositionMode = PositionDataRequest.builder().category(CategoryType.LINEAR).symbol("BTCUSDT").positionMode(PositionMode.BOTH_SIDES).build();  
    System.out.println(client.switchPositionMode(switchPositionMode));  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
        key: 'xxxxxxxxxxxxxxxxxx',  
        secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
        .switchPositionMode({  
            category: 'inverse',  
            symbol: 'BTCUSDH23',  
            mode: 0,  
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
        "time": 1675249072814  
    }