---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/asset/withdraw
api_type: REST
updated_at: 2026-07-04 19:03:59.558753
---

# Get available VASPs

This endpoint is used for query the available VASPs. This API distinguishes which compliance zone the user belongs to and the corresponding list of exchanges based on the user's UID.

### HTTP Request

GET`/v5/asset/withdraw/vasp/list`

### Request Parameters

None

### Response Parameters

Parameter| Type| Comments  
---|---|---  
vasp| array| Exchange entity info  
> vaspEntityId| string| Receiver platform id. When transfer to the exchanges that are not in the list, please use vaspEntityId='others'  
> vaspName| string| Receiver platform name  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/asset/withdraw/vasp/list HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1715067106163  
    X-BAPI-RECV-WINDOW: 5000  
    X-BAPI-SIGN: XXXXXX  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_exchange_entity_list())  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getExchangeEntities()  
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
            "vasp": [  
                {  
                    "vaspEntityId": "basic-finance",  
                    "vaspName": "Basic-finance"  
                },  
                {  
                    "vaspEntityId": "beeblock",  
                    "vaspName": "Beeblock"  
                },  
                {  
                    "vaspEntityId": "bithumb",  
                    "vaspName": "bithumb"  
                },  
                {  
                    "vaspEntityId": "cardo",  
                    "vaspName": "cardo"  
                },  
                {  
                    "vaspEntityId": "codevasp",  
                    "vaspName": "codevasp"  
                },  
                {  
                    "vaspEntityId": "codexchange-kor",  
                    "vaspName": "CODExchange-kor"  
                },  
                {  
                    "vaspEntityId": "coinone",  
                    "vaspName": "coinone"  
                },  
                {  
                    "vaspEntityId": "dummy",  
                    "vaspName": "Dummy"  
                },  
                {  
                    "vaspEntityId": "flata-exchange",  
                    "vaspName": "flataexchange"  
                },  
                {  
                    "vaspEntityId": "fobl",  
                    "vaspName": "Foblgate"  
                },  
                {  
                    "vaspEntityId": "hanbitco",  
                    "vaspName": "hanbitco"  
                },  
                {  
                    "vaspEntityId": "hexlant",  
                    "vaspName": "hexlant"  
                },  
                {  
                    "vaspEntityId": "inex",  
                    "vaspName": "INEX"  
                },  
                {  
                    "vaspEntityId": "infiniteblock-corp",  
                    "vaspName": "InfiniteBlock Corp"  
                },  
                {  
                    "vaspEntityId": "kdac",  
                    "vaspName": "kdac"  
                },  
                {  
                    "vaspEntityId": "korbit",  
                    "vaspName": "korbit"  
                },  
                {  
                    "vaspEntityId": "paycoin",  
                    "vaspName": "Paycoin"  
                },  
                {  
                    "vaspEntityId": "qbit",  
                    "vaspName": "Qbit"  
                },  
                {  
                    "vaspEntityId": "tennten",  
                    "vaspName": "TENNTEN"  
                },  
                {  
                    "vaspEntityId": "others",  
                    "vaspName": "Others (including Upbit)"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1715067106537  
    }

---

# 查詢交易所列表

該接口主要用于在提現時需要填寫接收方交易所信息，該 API 會根據用戶 UID 區分出用戶屬於哪個合規區以及對應的交易所列表。

### HTTP 請求

GET`/v5/asset/withdraw/vasp/list`

### 請求參數

無

### 響應參數

參數| 類型| 說明  
---|---|---  
vasp| array| 交易所實體信息  
> vaspEntityId| string| 接收方平台id. 當提現至交易所或者不在該列表內的平台時, 請使用vaspEntityId="others"  
> vaspName| string| 接收方平台名稱  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/asset/withdraw/vasp/list HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1715067106163  
    X-BAPI-RECV-WINDOW: 5000  
    X-BAPI-SIGN: XXXXXX  
    
    
    
      
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getExchangeEntities()  
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
            "vasp": [  
                {  
                    "vaspEntityId": "basic-finance",  
                    "vaspName": "Basic-finance"  
                },  
                {  
                    "vaspEntityId": "beeblock",  
                    "vaspName": "Beeblock"  
                },  
                {  
                    "vaspEntityId": "bithumb",  
                    "vaspName": "bithumb"  
                },  
                {  
                    "vaspEntityId": "cardo",  
                    "vaspName": "cardo"  
                },  
                {  
                    "vaspEntityId": "codevasp",  
                    "vaspName": "codevasp"  
                },  
                {  
                    "vaspEntityId": "codexchange-kor",  
                    "vaspName": "CODExchange-kor"  
                },  
                {  
                    "vaspEntityId": "coinone",  
                    "vaspName": "coinone"  
                },  
                {  
                    "vaspEntityId": "dummy",  
                    "vaspName": "Dummy"  
                },  
                {  
                    "vaspEntityId": "flata-exchange",  
                    "vaspName": "flataexchange"  
                },  
                {  
                    "vaspEntityId": "fobl",  
                    "vaspName": "Foblgate"  
                },  
                {  
                    "vaspEntityId": "hanbitco",  
                    "vaspName": "hanbitco"  
                },  
                {  
                    "vaspEntityId": "hexlant",  
                    "vaspName": "hexlant"  
                },  
                {  
                    "vaspEntityId": "inex",  
                    "vaspName": "INEX"  
                },  
                {  
                    "vaspEntityId": "infiniteblock-corp",  
                    "vaspName": "InfiniteBlock Corp"  
                },  
                {  
                    "vaspEntityId": "kdac",  
                    "vaspName": "kdac"  
                },  
                {  
                    "vaspEntityId": "korbit",  
                    "vaspName": "korbit"  
                },  
                {  
                    "vaspEntityId": "paycoin",  
                    "vaspName": "Paycoin"  
                },  
                {  
                    "vaspEntityId": "qbit",  
                    "vaspName": "Qbit"  
                },  
                {  
                    "vaspEntityId": "tennten",  
                    "vaspName": "TENNTEN"  
                },  
                {  
                    "vaspEntityId": "others",  
                    "vaspName": "Others (including Upbit)"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1715067106537  
    }