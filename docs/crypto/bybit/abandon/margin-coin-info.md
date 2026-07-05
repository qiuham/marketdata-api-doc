---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/abandon/margin-coin-info
api_type: REST
updated_at: 2026-07-05 19:04:19.434498
---

# Set Risk Limit

**Since bybit has launched auto risk limit on 12 March 2024, please click[here](https://announcements.bybit.com/en/article/risk-limit-update-transitioning-from-manual-to-auto-adjustment-bltf0fa535064561d9d/) to learn more, so it will not take effect even you set it successfully.**

### HTTP Request

POST`/v5/position/set-risk-limit`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
[category](/docs/v5/enum#category)| **true**|  string| Product type 

  * Unified account: `linear`, `inverse`
  * Classic account: `linear`, `inverse`. _Please note that`category` is **not** involved with business logic_

  
symbol| **true**|  string| Symbol name, like `BTCUSDT`, uppercase only  
riskId| **true**|  integer| Risk limit ID  
[positionIdx](/docs/v5/enum#positionidx)| false| integer| Used to identify positions in different position modes. For hedge mode, it is **required**

  * `0`: one-way mode
  * `1`: hedge-mode Buy side
  * `2`: hedge-mode Sell side

  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
category| string| Product type  
riskId| integer| Risk limit ID  
riskLimitValue| string| The position limit value corresponding to this risk ID  
[](/docs/api-explorer/v5/position/set-risk-limit)

* * *

### Request Example

  * HTTP
  * Python
  * Java
  * Node.js


    
    
    POST /v5/position/set-risk-limit HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672282269774  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "category": "linear",  
        "symbol": "BTCUSDT",  
        "riskId": 4,  
        "positionIdx": null  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.set_risk_limit(  
        category="linear",  
        symbol="BTCUSDT",  
        riskId=4,  
    ))  
    
    
    
    import com.bybit.api.client.domain.*;  
    import com.bybit.api.client.domain.position.*;  
    import com.bybit.api.client.domain.position.request.*;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    var client = BybitApiClientFactory.newInstance().newAsyncPositionRestClient();  
    var setRiskLimitRequest = PositionDataRequest.builder().category(CategoryType.LINEAR).symbol("BTCUSDT").riskId(4).build();  
    client.setRiskLimit(setRiskLimitRequest, System.out::println);  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
        key: 'xxxxxxxxxxxxxxxxxx',  
        secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
        .setRiskLimit({  
            category: 'linear',  
            symbol: 'BTCUSDT',  
            riskId: 4,  
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
            "riskId": 4,  
            "riskLimitValue": "8000000",  
            "category": "linear"  
        },  
        "retExtInfo": {},  
        "time": 1672282270571  
    }

---

# 設置風險限額

**由於Bybit在2024年3月12日上線了自動調整risk limit功能, 詳情請見[這裡](https://announcements.bybit.com/zh-TW/article/risk-limit-update-transitioning-from-manual-to-auto-adjustment-bltf0fa535064561d9d/), 因此儘管接口能調通, 但是沒有任何意義**

### HTTP 請求

POST`/v5/position/set-risk-limit`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
[category](/docs/zh-TW/v5/enum#category)| **true**|  string| 產品類型 

  * 統一帳戶: `linear`, `inverse`
  * 經典帳戶: `linear`, `inverse`. 這裡`category`字段不參與業務邏輯，僅做路由使用

  
symbol| **true**|  string| 合約名稱  
riskId| **true**|  integer| 風險限額Id  
[positionIdx](/docs/zh-TW/v5/enum#positionidx)| false| integer| 倉位標識，用於標識不同倉位, 雙向持倉模式下，該字段**必傳**

  * `0`: 單向持倉模式
  * `1`: 買側雙向持倉模式
  * `2`: 賣側雙向持倉模式

  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
category| string| 產品類型  
riskId| integer| 風險限額Id  
riskLimitValue| string| 風險限額Id對應的風險限額  
[](/docs/zh-TW/api-explorer/v5/position/set-risk-limit)

* * *

### 請求示例

  * HTTP
  * Python
  * Java
  * Node.js


    
    
    POST /v5/position/set-risk-limit HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672282269774  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "category": "linear",  
        "symbol": "BTCUSDT",  
        "riskId": 4,  
        "positionIdx": null  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.set_risk_limit(  
        category="linear",  
        symbol="BTCUSDT",  
        riskId=4,  
    ))  
    
    
    
    import com.bybit.api.client.domain.*;  
    import com.bybit.api.client.domain.position.*;  
    import com.bybit.api.client.domain.position.request.*;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    var client = BybitApiClientFactory.newInstance().newAsyncPositionRestClient();  
    var setRiskLimitRequest = PositionDataRequest.builder().category(CategoryType.LINEAR).symbol("BTCUSDT").riskId(4).build();  
    client.setRiskLimit(setRiskLimitRequest, System.out::println);  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
        key: 'xxxxxxxxxxxxxxxxxx',  
        secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
        .setRiskLimit({  
            category: 'linear',  
            symbol: 'BTCUSDT',  
            riskId: 4,  
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
            "riskId": 4,  
            "riskLimitValue": "8000000",  
            "category": "linear"  
        },  
        "retExtInfo": {},  
        "time": 1672282270571  
    }