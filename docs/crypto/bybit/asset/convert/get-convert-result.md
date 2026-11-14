---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/asset/convert/get-convert-result
api_type: REST
updated_at: 2026-11-13 19:21:34.362050
---

# Get Convert Status

You can query the exchange result by sending quoteTxId.

### HTTP Request

GET`/v5/asset/exchange/convert-result-query`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
quoteTxId| **true**|  string| Quote tx ID  
[accountType](/docs/v5/enum#convertaccounttype)| **true**|  string| Wallet type  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
result| object|   
> [accountType](/docs/v5/enum#convertaccounttype)| string| Wallet type  
> exchangeTxId| string| Exchange tx ID, same as quote tx ID  
> userId| string| User ID  
> fromCoin| string| From coin  
> fromCoinType| string| From coin type. `crypto`  
> toCoin| string| To coin  
> toCoinType| string| To coin type. `crypto`  
> fromAmount| string| From coin amount (amount to sell)  
> toAmount| string| To coin amount (amount to buy according to exchange rate)  
> exchangeStatus| string| Exchange status 

  * init
  * processing
  * success
  * failure

  
> extInfo| object| Reserved field, ignored for now  
> convertRate| string| Exchange rate  
> createdAt| string| Quote created time  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/asset/exchange/convert-result-query?quoteTxId=10100108106409343501030232064&accountType=eb_convert_funding HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1720073659847  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_convert_status(  
        accountType="eb_convert_funding",  
        quoteTxId="10100108106409343501030232064",  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getConvertStatus({  
        quoteTxId: 'quoteTransactionId',  
        accountType: 'eb_convert_funding',  
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
        "retMsg": "ok",  
        "result": {  
            "result": {  
                "accountType": "eb_convert_funding",  
                "exchangeTxId": "10100108106409343501030232064",  
                "userId": "XXXXX",  
                "fromCoin": "ETH",  
                "fromCoinType": "crypto",  
                "fromAmount": "0.1",  
                "toCoin": "BTC",  
                "toCoinType": "crypto",  
                "toAmount": "0.00534882723991",  
                "exchangeStatus": "success",  
                "extInfo": {},  
                "convertRate": "0.0534882723991",  
                "createdAt": "1720071899995"  
            }  
        },  
        "retExtInfo": {},  
        "time": 1720073660696  
    }

---

# 查詢報價單狀態

信息

  * 您可以通過quoteTxId指定查詢某筆被確認的報價單
  * 確保傳入匹配的錢包類型和報價單號, 否則會查不到



### HTTP 請求

GET`/v5/asset/exchange/convert-result-query`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
quoteTxId| **true**|  string| 報價單號  
[accountType](/docs/zh-TW/v5/enum#convertaccounttype)| **true**|  string| 錢包類型  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
result| object|   
> [accountType](/docs/zh-TW/v5/enum#convertaccounttype)| string| 錢包類型  
> exchangeTxId| string| 報價單ID, 和quoteTxId保持一致  
> userId| string| 用戶ID  
> fromCoin| string| 兌出幣種  
> fromCoinType| string| 兌出幣種類型. `crypto`  
> toCoin| string| 兌入幣種  
> toCoinType| string| 兌入幣種類型. `crypto`  
> fromAmount| string| 兌出幣種數量  
> toAmount| string| 兌入幣種數量  
> exchangeStatus| string| 兌換狀態 

  * init
  * processing
  * success
  * failure

  
> extInfo| object| 保留字段, 當前可忽略  
> convertRate| string| 兌換率  
> createdAt| string| 報價單創建時間  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/asset/exchange/convert-result-query?quoteTxId=10100108106409343501030232064&accountType=eb_convert_funding HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1720073659847  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_convert_status(  
        accountType="eb_convert_funding",  
        quoteTxId="10100108106409343501030232064",  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getConvertStatus({  
        quoteTxId: 'quoteTransactionId',  
        accountType: 'eb_convert_funding',  
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
        "retMsg": "ok",  
        "result": {  
            "result": {  
                "accountType": "eb_convert_funding",  
                "exchangeTxId": "10100108106409343501030232064",  
                "userId": "XXXXX",  
                "fromCoin": "ETH",  
                "fromCoinType": "crypto",  
                "fromAmount": "0.1",  
                "toCoin": "BTC",  
                "toCoinType": "crypto",  
                "toAmount": "0.00534882723991",  
                "exchangeStatus": "success",  
                "extInfo": {},  
                "convertRate": "0.0534882723991",  
                "createdAt": "1720071899995"  
            }  
        },  
        "retExtInfo": {},  
        "time": 1720073660696  
    }