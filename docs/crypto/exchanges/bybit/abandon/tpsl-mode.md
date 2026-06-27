---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/abandon/tpsl-mode
api_type: REST
updated_at: 2026-05-27 19:13:52.009303
---

# Batch Set Collateral Coin

### HTTP Request

POST`/v5/account/set-collateral-switch-batch`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
request| **true**|  array| Object  
> coin| **true**|  string| Coin name, uppercase only 

  * You can get collateral coin from [here](/docs/v5/account/collateral-info)
  * USDT, USDC cannot be set

  
> collateralSwitch| **true**|  string| `ON`: switch on collateral, `OFF`: switch off collateral  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
result| Object|   
> list| array| Object  
>> coin| string| Coin name  
>> collateralSwitch| string| `ON`: switch on collateral, `OFF`: switch off collateral  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/account/set-collateral-switch-batch HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1704782042755  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 371  
      
    {  
        "request": [  
            {  
                "coin": "MATIC",  
                "collateralSwitch": "OFF"  
            },  
            {  
                "coin": "BTC",  
                "collateralSwitch": "OFF"  
            },  
            {  
                "coin": "ETH",  
                "collateralSwitch": "OFF"  
            },  
            {  
                "coin": "SOL",  
                "collateralSwitch": "OFF"  
            }  
        ]  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.batch_set_collateral_coin(  
      request=[  
        {  
          "coin": "BTC",  
          "collateralSwitch": "ON",  
        },  
        {  
          "coin": "ETH",  
          "collateralSwitch": "ON",  
        }  
      ]  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .batchSetCollateralCoin({  
        request: [  
          {  
            coin: 'BTC',  
            collateralSwitch: 'ON',  
          },  
          {  
            coin: 'ETH',  
            collateralSwitch: 'OFF',  
          },  
        ],  
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
        "retMsg": "SUCCESS",  
        "result": {  
            "list": [  
                {  
                    "coin": "MATIC",  
                    "collateralSwitch": "OFF"  
                },  
                {  
                    "coin": "BTC",  
                    "collateralSwitch": "OFF"  
                },  
                {  
                    "coin": "ETH",  
                    "collateralSwitch": "OFF"  
                },  
                {  
                    "coin": "SOL",  
                    "collateralSwitch": "OFF"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1704782042913  
    }

---

# 批量設置抵押品幣種

用戶可以批量開啟或關閉統一帳戶中幣種抵押屬性，默認都是**關閉** 的

### HTTP 請求

POST`/v5/account/set-collateral-switch-batch`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
request| **true**|  array| Object  
> coin| **true**|  string| 幣種名稱 

  * 您可以從[這裡](/docs/zh-TW/v5/account/collateral-info)獲取抵押品幣種
  * USDT, USDC不支持設置

  
> collateralSwitch| **true**|  string| `ON`: 開啟抵押, `OFF`: 關閉抵押  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
result| Object|   
> list| array| Object  
>> coin| string| 幣種名稱  
>> collateralSwitch| string| `ON`: 開啟抵押, `OFF`: 關閉抵押  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/account/set-collateral-switch-batch HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1704782042755  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 371  
      
    {  
        "request": [  
            {  
                "coin": "MATIC",  
                "collateralSwitch": "OFF"  
            },  
            {  
                "coin": "BTC",  
                "collateralSwitch": "OFF"  
            },  
            {  
                "coin": "ETH",  
                "collateralSwitch": "OFF"  
            },  
            {  
                "coin": "SOL",  
                "collateralSwitch": "OFF"  
            }  
        ]  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.batch_set_collateral_coin(  
      request=[  
        {  
          "coin": "BTC",  
          "collateralSwitch": "ON",  
        },  
        {  
          "coin": "ETH",  
          "collateralSwitch": "ON",  
        }  
      ]  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .batchSetCollateralCoin({  
        request: [  
          {  
            coin: 'BTC',  
            collateralSwitch: 'ON',  
          },  
          {  
            coin: 'ETH',  
            collateralSwitch: 'OFF',  
          },  
        ],  
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
        "retMsg": "SUCCESS",  
        "result": {  
            "list": [  
                {  
                    "coin": "MATIC",  
                    "collateralSwitch": "OFF"  
                },  
                {  
                    "coin": "BTC",  
                    "collateralSwitch": "OFF"  
                },  
                {  
                    "coin": "ETH",  
                    "collateralSwitch": "OFF"  
                },  
                {  
                    "coin": "SOL",  
                    "collateralSwitch": "OFF"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1704782042913  
    }