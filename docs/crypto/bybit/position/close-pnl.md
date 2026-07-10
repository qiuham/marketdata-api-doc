---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/position/close-pnl
api_type: Position
updated_at: 2026-07-10 19:04:36.972425
---

# Confirm New Risk Limit

It is only applicable when the user is marked as only reducing positions (please see the isReduceOnly field in the [Get Position Info](/docs/v5/position) interface). After the user actively adjusts the risk level, this interface is called to try to calculate the adjusted risk level, and if it passes (retCode=0), the system will remove the position reduceOnly mark. You are recommended to call [Get Position Info](/docs/v5/position) to check `isReduceOnly` field.

### HTTP Request

POST`/v5/position/confirm-pending-mmr`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
[category](/docs/v5/enum#category)| **true**|  string| Product type `linear`, `inverse`  
symbol| **true**|  string| Symbol name  
  
### Response Parameters

None

### Request Example

  * HTTP
  * Python
  * Java
  * Node.js


    
    
    POST /v5/position/confirm-pending-mmr HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1698051123673  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 53  
      
    {  
        "category": "linear",  
        "symbol": "BTCUSDT"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.confirm_new_risk_limit(  
        category="linear",  
        symbol="BTCUSDT"  
    ))  
    
    
    
    import com.bybit.api.client.domain.*;  
    import com.bybit.api.client.domain.position.*;  
    import com.bybit.api.client.domain.position.request.*;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    var client = BybitApiClientFactory.newInstance().newAsyncPositionRestClient();  
    var confirmNewRiskRequest = PositionDataRequest.builder().category(CategoryType.LINEAR).symbol("BTCUSDT").build();  
    client.confirmPositionRiskLimit(confirmNewRiskRequest, System.out::println);  
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {},  
        "retExtInfo": {},  
        "time": 1698051124588  
    }

---

# 確認新的風險限額

僅適用於當用戶被標記為僅減倉 (請看[持倉](/docs/zh-TW/v5/position)接口中的isReduceOnly字段) 時, 在用戶主動調整風險水位後, 調用該接口來試算調整後的風 險水平, 若通過(retCode=0), 則系統會移除僅減倉標記, 推薦自行再調用下倉位接口確認`isReduceOnly`字段是否變成false

### HTTP 請求

POST`/v5/position/confirm-pending-mmr`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
[category](/docs/zh-TW/v5/enum#category)| **true**|  string| 產品類型 `linear`, `inverse`  
symbol| **true**|  string| 合約名稱  
  
### 響應參數

無

### 請求示例

  * HTTP
  * Python
  * Java
  * Node.js


    
    
    POST /v5/position/confirm-pending-mmr HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1698051123673  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 53  
      
    {  
        "category": "linear",  
        "symbol": "BTCUSDT"  
    }  
    
    
    
      
    
    
    
    import com.bybit.api.client.domain.*;  
    import com.bybit.api.client.domain.position.*;  
    import com.bybit.api.client.domain.position.request.*;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    var client = BybitApiClientFactory.newInstance().newAsyncPositionRestClient();  
    var confirmNewRiskRequest = PositionDataRequest.builder().category(CategoryType.LINEAR).symbol("BTCUSDT").build();  
    client.confirmPositionRiskLimit(confirmNewRiskRequest, System.out::println);  
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {},  
        "retExtInfo": {},  
        "time": 1698051124588  
    }