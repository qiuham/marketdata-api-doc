---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/order/cancel-order
api_type: Trading
updated_at: 2026-09-02 18:45:40.557877
---

# Set Disconnect Cancel All

info

## What is Disconnection Protect (DCP)?

Based on the websocket private connection and heartbeat mechanism, Bybit provides disconnection protection function. The timing starts from the first disconnection. If the Bybit server does not receive the reconnection from the client for more than 10 (default) seconds and resumes the heartbeat "ping", then the client is in the state of "disconnection protect", all active **futures / spot / option** orders of the client will be cancelled automatically. If within 10 seconds, the client reconnects and resumes the heartbeat "ping", the timing will be reset and restarted at the next disconnection.

## How to enable DCP

  * If you need to turn it on/off, you can contact your client manager for consultation and application. The default time window is 10 seconds.
  * DCP feature is only available for Ins clients. VIP clients cannot access this feature



## Applicable

Effective for **Inverse Perp / Inverse Futures / USDT Perp / USDT Futures / USDC Perp / USDC Futures / Spot / options**

tip

After the request is successfully sent, the system needs a certain time to take effect. It is recommended to query or set again after 10 seconds

  * You can use [this endpoint](/docs/v5/account/dcp-info) to get your current DCP configuration.
  * Your private websocket connection **must** subscribe ["dcp" topic](/docs/v5/websocket/private/dcp) in order to trigger DCP successfully



### HTTP Request

POST`/v5/order/disconnected-cancel-all`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
product| false| string| `OPTIONS`(default), `DERIVATIVES`, `SPOT`  
timeWindow| **true**|  integer| Disconnection timing window time. [`3`, `300`], unit: second  
  
### Response Parameters

None

### Request Example

  * HTTP
  * Python
  * Java
  * Node.js


    
    
    POST v5/order/disconnected-cancel-all HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1675852742375  
    X-BAPI-RECV-WINDOW: 50000  
    Content-Type: application/json  
      
    {  
      "timeWindow": 40  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.set_dcp(  
        timeWindow=40,  
    ))  
    
    
    
    import com.bybit.api.client.config.BybitApiConfig;  
    import com.bybit.api.client.domain.trade.request.TradeOrderRequest;  
    import com.bybit.api.client.domain.*;  
    import com.bybit.api.client.domain.trade.*;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    var client = BybitApiClientFactory.newInstance("YOUR_API_KEY", "YOUR_API_SECRET", BybitApiConfig.TESTNET_DOMAIN).newTradeRestClient();  
    var setDcpOptionsRequest = TradeOrderRequest.builder().timeWindow(40).build();  
    System.out.println(client.setDisconnectCancelAllTime(setDcpOptionsRequest));  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
        key: 'xxxxxxxxxxxxxxxxxx',  
        secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
        .setDisconnectCancelAllWindow('option', 40)  
        .then((response) => {  
            console.log(response);  
        })  
        .catch((error) => {  
            console.error(error);  
        });  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "success"  
    }

---

# 設置斷線保護時間

信息

## 什麼是斷線保護 (Disconnection Protect)?

Bybit基於websocket私有連接和心跳機制，提供斷線保護功能。這計時從第一次斷開開始。如果Bybit服務器在一段時間內沒有收到客戶端的重連超過10秒（默認）並 恢復心跳“ping”，則客戶端處於“斷線保護”狀態，客戶所有活躍的**合約 / 現貨 / 期權** 訂單將自動取消。如果在 10 秒內，客戶端重新連接並恢復心跳“ping”，計時會在下次斷線 時重置並重新開始。

## 如何啟用斷線保護

  * 若您需要開啟/關閉斷線保護功能, 您可以諮詢客戶經理. 開啟後，默認的斷線保護時間為10秒。
  * DCP 功能僅適用於 Ins 用戶，VIP 用戶無法使用此功能。



## 適用對象

作用於**幣本位合約 / U本位合約 / 現貨 / 期權**

提示

API請求發送成功後，系統需要一定的時間才能生效。建議10秒後再查詢或設置。

  * 您可以使用該[接口](/docs/zh-TW/v5/account/dcp-info)來查詢當前DCP配置
  * 您的私有連接**必須** 訂閱[斷線保護](/docs/zh-TW/v5/websocket/private/dcp), 才能確保DCP功能被觸發



### HTTP請求

POST`/v5/order/disconnected-cancel-all`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
product| false| string| `OPTIONS`(默認), `DERIVATIVES`, `SPOT`  
timeWindow| **true**|  integer| 斷線保護時間窗口. [`3`, `300`], 單位: 秒  
  
### 響應參數

無

### 請求示例

  * HTTP
  * Python
  * Java
  * Node.js


    
    
    POST v5/order/disconnected-cancel-all HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1675852742375  
    X-BAPI-RECV-WINDOW: 50000  
    Content-Type: application/json  
      
    {  
      "timeWindow": 40  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.set_dcp(  
        timeWindow=40,  
    ))  
    
    
    
    import com.bybit.api.client.config.BybitApiConfig;  
    import com.bybit.api.client.domain.trade.request.TradeOrderRequest;  
    import com.bybit.api.client.domain.*;  
    import com.bybit.api.client.domain.trade.*;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    var client = BybitApiClientFactory.newInstance("YOUR_API_KEY", "YOUR_API_SECRET", BybitApiConfig.TESTNET_DOMAIN).newTradeRestClient();  
    var setDcpOptionsRequest = TradeOrderRequest.builder().timeWindow(40).build();  
    System.out.println(client.setDisconnectCancelAllTime(setDcpOptionsRequest));  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
        key: 'xxxxxxxxxxxxxxxxxx',  
        secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
        .setDisconnectCancelAllWindow('option', 40)  
        .then((response) => {  
            console.log(response);  
        })  
        .catch((error) => {  
            console.error(error);  
        });  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "success"  
    }