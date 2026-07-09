---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/asset/settlement
api_type: REST
updated_at: 2026-07-09 19:05:28.850229
---

# Get Sub UID

Query the sub UIDs under a main UID. It returns up to 2000 sub accounts, if you need more, please call this [endpoint](/docs/v5/user/page-subuid).

info

Query by the master UID's api key **only**

### HTTP Request

GET`/v5/asset/transfer/query-sub-member-list`

### Request Parameters

None

### Response Parameters

Parameter| Type| Comments  
---|---|---  
subMemberIds| array<string>| All sub UIDs under the main UID  
transferableSubMemberIds| array<string>| All sub UIDs that have universal transfer enabled  
[](/docs/api-explorer/v5/asset/sub-uid-list)

* * *

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/asset/transfer/query-sub-member-list HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672147239931  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_sub_uid())  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getSubUID()  
      .then((response) => {  
        console.log(response);  
      })  
      .catch((error) => {  
        console.error(error);  
      });  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "subMemberIds": [  
                "554117",  
                "592324",  
                "592334",  
                "1055262",  
                "1072055",  
                "1119352"  
            ],  
            "transferableSubMemberIds": [  
                "554117",  
                "592324"  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1672147241320  
    }

---

# 查詢子帳號列表

查詢某個母帳戶的子帳號列表, 返回至多2000個子帳戶, 如果您有更多, 可以調用這個[接口](/docs/zh-TW/v5/user/page-subuid).

信息

僅支持母帳號API key

### HTTP 請求

GET`/v5/asset/transfer/query-sub-member-list`

### 請求參數

無

### 響應參數

參數| 類型| 說明  
---|---|---  
subMemberIds| array<string>| 所有子帳號  
transferableSubMemberIds| array<string>| 已經開啟了萬能劃轉的子帳號  
[](/docs/zh-TW/api-explorer/v5/asset/sub-uid-list)

* * *

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/asset/transfer/query-sub-member-list HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672147239931  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_sub_uid())  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getSubUID()  
      .then((response) => {  
        console.log(response);  
      })  
      .catch((error) => {  
        console.error(error);  
      });  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "subMemberIds": [  
                "554117",  
                "592324",  
                "592334",  
                "1055262",  
                "1072055",  
                "1119352"  
            ],  
            "transferableSubMemberIds": [  
                "554117",  
                "592324"  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1672147241320  
    }