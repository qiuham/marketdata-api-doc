---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/account/dcp-info
api_type: Account
updated_at: 2026-11-13 19:20:45.470605
---

# Get DCP Info

Query the DCP configuration of the account. Before calling the interface, please make sure you have applied for the UTA account DCP configuration with your account manager

  * Only the configured main / sub account can query information from this API. Calling this API by an account always returns empty.

  * If you only request to activate Spot trading for DCP, the contract and options data will not be returned.




info

  * Support USDT Perpetuals, USDT Futures, USDC Perpetuals, USDC Futures, Inverse Perpetuals, Inverse Futures [DERIVATIVES]  
Spot [SPOT]  
Options [OPTIONS]



### HTTP Request

GET`/v5/account/query-dcp-info`

### Request Parameters

None

### Response Parameters

Parameter| Type| Comments  
---|---|---  
dcpInfos| array<object>| DCP config for each product  
> product| string| `SPOT`, `DERIVATIVES`, `OPTIONS`  
> dcpStatus| string| [Disconnected-CancelAll-Prevention](/docs/v5/order/dcp) status: `ON`  
> timeWindow| string| DCP trigger time window which user pre-set. Between [3, 300] seconds, default: 10 sec  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/account/query-dcp-info HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1717065530867  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.query_dcp_info())  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getDCPInfo()  
      .then((response) => {  
        console.log(response);  
      })  
      .catch((error) => {  
        console.error(error);  
      });  
    

### Response Example
    
    
    // it means my account enables Spot and Deriviatvies on the backend  
    // Options is not enabled with DCP  
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "dcpInfos": [  
                {  
                    "product": "SPOT",  
                    "dcpStatus": "ON",  
                    "timeWindow": "10"  
                },  
                {  
                    "product": "DERIVATIVES",  
                    "dcpStatus": "ON",  
                    "timeWindow": "10"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1717065531697  
    }

---

# 查詢DCP配置

查詢帳戶的期貨 / 現貨 / 期權的dcp配置. 在調用接口前, 請確保已經和客戶經理申請了帳戶DCP開通

  * 只有配置了的母子帳戶能夠從該接口查詢到信息, 沒有配置的母帳戶或者子帳戶調用該接口總是返回空
  * 在配置時, 若只申請部分業務線, 比如只申請開通期貨, 則現貨和期權是不會返回數據的



### HTTP 請求

GET`/v5/account/query-dcp-info`

### 請求參數

無

### 響應參數

參數| 類型| 說明  
---|---|---  
dcpInfos| array<object>|   
> product| string| `SPOT`, `DERIVATIVES`, `OPTIONS`  
> dcpStatus| string| [設置斷線保護時間](/docs/zh-TW/v5/order/dcp) 開關狀態: `ON`  
> timeWindow| string| 設置的DCP觸發時間窗口. 範圍為[3, 300] 秒, 默認: 10 秒  
  
### 請求示例

  * HTTP
  * Node.js


    
    
    GET /v5/account/query-dcp-info HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1717065530867  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getDCPInfo()  
      .then((response) => {  
        console.log(response);  
      })  
      .catch((error) => {  
        console.error(error);  
      });  
    

### 響應示例
    
    
    // 下面這個實例意味著帳戶只配置了現貨和期貨的dcp功能  
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "dcpInfos": [  
                {  
                    "product": "SPOT",  
                    "dcpStatus": "ON",  
                    "timeWindow": "10"  
                },  
                {  
                    "product": "DERIVATIVES",  
                    "dcpStatus": "ON",  
                    "timeWindow": "10"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1717065531697  
    }