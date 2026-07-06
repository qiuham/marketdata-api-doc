---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/abandon/contract-transaction-log
api_type: REST
updated_at: 2026-07-06 19:22:46.416982
---

# Enable Universal Transfer for Sub UID

info

You no longer need to configure transferable sub UIDs. Now, all sub UIDs are automatically enabled for universal transfer.

Transfer between sub-sub or main-sub

Use this endpoint to enable a subaccount to take part in a universal transfer. It is a one-time switch which, once thrown, enables a subaccount permanently. If not set, your subaccount cannot use universal transfers.

caution

Can query by the master UID's api key **only**

### HTTP Request

POST`/v5/asset/transfer/save-transfer-sub-member`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
subMemberIds| **true**|  array| This list has a **single item**. Separate multiple UIDs by comma, e.g., `"uid1,uid2,uid3"`  
  
### Response Parameters

None

### Request Example

  * HTTP
  * Python


    
    
    POST /v5/asset/transfer/save-transfer-sub-member HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672147595971  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "subMemberIds": ["554117,592324,592334"]  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.enable_universal_transfer_for_sub_uid(  
        subMemberIds=["554117,592324,592334"],  
    ))  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {},  
        "retExtInfo": {},  
        "time": 1672147593188  
    }

---

# 配置互相劃轉的子帳號

信息

無需再配置可劃轉的子帳號, 該限制已移除, 默認任意子帳號之間可以劃轉

該接口用於配置開啟萬能劃轉的子帳號列表。沒有進行配置的子帳號是無法進行萬能劃轉的。

提示

萬能劃轉是允許您將資金直接從一個子帳號劃轉到另一個子帳號，同樣允許母子帳號間的劃轉。

警告

僅支持母帳號API key

### HTTP 請求

POST`/v5/asset/transfer/save-transfer-sub-member`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
subMemberIds| **true**|  array<string>| 子帳號. 支持輸入多個子帳號，用逗號隔開, 比如, "uid1,uid2,uid3"  
  
### 響應參數

無

### 請求示例

  * HTTP
  * Python


    
    
    POST /v5/asset/transfer/save-transfer-sub-member HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672147595971  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "subMemberIds": ["554117,592324,592334"]  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.enable_universal_transfer_for_sub_uid(  
        subMemberIds=["554117,592324,592334"],  
    ))  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {},  
        "retExtInfo": {},  
        "time": 1672147593188  
    }