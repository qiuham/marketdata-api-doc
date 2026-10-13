---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/abandon/enable-unitransfer-subuid
api_type: REST
updated_at: 2026-10-13 18:45:05.655928
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

# Unicorn! · GitHub