---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/asset/convert/confirm-quote
api_type: REST
updated_at: 2026-06-29 19:25:38.671696
---

# Get Convert History

Returns all confirmed quotes.

info

Starting from September 10, 2025, converts executed on the webpage can also be queried via this API.

### HTTP Request

GET`/v5/asset/exchange/query-convert-history`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
[accountType](/docs/v5/enum#convertaccounttype)| false| string| Wallet type   
`eb_convert_funding`: funding wallet convert records via API  
`eb_convert_uta`: uta wallet convert records via API  
`funding`: normal crypto convert via web/app  
`funding_fiat`: fiat crypto convert via web/app  
`funding_fbtc_convert`: FBTC to BTC convert via web/app  
`funding_block_trade`: block trade convert via web/app 

  * Supports passing multiple types, separated by comma e.g., `eb_convert_funding,eb_convert_uta`
  * Return all wallet types data if not passed

  
index| false| integer| Page number 
* started from 1
* 1st page by default  
limit| false| integer| Page size 
* 20 records by default
* up to 100 records, return 100 when exceeds 100  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array<object>| Array of quotes  
> [accountType](/docs/v5/enum#convertaccounttype)| string| Wallet type  
`eb_convert_funding`: funding wallet convert records via API  
`eb_convert_uta`: uta wallet convert records via API  
`funding`: normal crypto convert via web/app  
`funding_fiat`: fiat crypto convert via web/app  
`funding_fbtc_convert`: FBTC to BTC convert via web/app  
`funding_block_trade`: block trade convert via web/app  
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

  
> extInfo| object|   
>> paramType| string| This field is published when you send it in the [Request a Quote ](/docs/v5/asset/convert/apply-quote)  
>> paramValue| string| This field is published when you send it in the [Request a Quote ](/docs/v5/asset/convert/apply-quote)  
> convertRate| string| Exchange rate  
> createdAt| string| Quote created time  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/asset/exchange/query-convert-history?accountType=eb_convert_uta,eb_convert_funding HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1720074159814  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_convert_history(  
        accountType="eb_convert_uta,eb_convert_funding",  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getConvertHistory()  
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
            "list": [  
                {  
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
                    "extInfo": {  
                        "paramType": "opFrom",  
                        "paramValue": "broker-id-001"  
                    },  
                    "convertRate": "0.0534882723991",  
                    "createdAt": "1720071899995"  
                },  
                {  
                    "accountType": "eb_convert_uta",  
                    "exchangeTxId": "23070eb_convert_uta408933875189391360",  
                    "userId": "XXXXX",  
                    "fromCoin": "BTC",  
                    "fromCoinType": "crypto",  
                    "fromAmount": "0.1",  
                    "toCoin": "ETH",  
                    "toCoinType": "crypto",  
                    "toAmount": "1.773938248611074",  
                    "exchangeStatus": "success",  
                    "extInfo": {},  
                    "convertRate": "17.73938248611074",  
                    "createdAt": "1719974243256"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1720074457715  
    }

---

# 查詢兌換歷史

那些被確認的報價單, 不管最終狀態如何, 該接口都會返回

信息

自 2025 年 9 月 10 日起，前端進行的閃兌也可以在此介面中查詢到

### HTTP 請求

GET`/v5/asset/exchange/query-convert-history`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
[accountType](/docs/zh-TW/v5/enum#convertaccounttype)| false| string| 錢包類型   
`eb_convert_funding`: 資金錢包閃兌紀錄(API)  
`eb_convert_uta`: uta錢包閃兌紀錄(API)  
`funding`: 資金錢包普通幣幣兌換(網頁/APP)  
`funding_fiat`: 資金錢包數法兌換(網頁/APP)  
`funding_fbtc_convert`: 資金錢包FBTC兌換成BTC(網頁/APP)  
`funding_block_trade`: 大宗兌換兌換(網頁/APP)

  * 支持傳遞多個, 用逗號分開 比如, `eb_convert_funding,eb_convert_uta`
  * 當不傳時, 默認返回所有錢包

  
index| false| integer| 頁碼 

  * 從1開始
  * 不傳時, 默認返回第一頁

  
limit| false| integer| 每頁數量 

  * 默認20條
  * 最多支持100條, 大於100, 按照100返回

  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
list| array<object>| 報價單列表  
> [accountType](/docs/zh-TW/v5/enum#convertaccounttype)| string| `eb_convert_funding`: 資金錢包閃兌紀錄(API)  
`eb_convert_uta`: uta錢包閃兌紀錄(API)  
`funding`: 資金錢包普通幣幣兌換(網頁/APP)  
`funding_fiat`: 資金錢包數法兌換(網頁/APP)  
`funding_fbtc_convert`: 資金錢包FBTC兌換成BTC(網頁/APP)  
`funding_block_trade`: 大宗兌換兌換(網頁/APP)  
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

  
> extInfo| object|   
>> paramType| string| 如果您在[申請報價](/docs/zh-TW/v5/asset/convert/apply-quote)接口中中有發送該字段, 則這裡會釋出該字段  
>> paramValue| string| 如果您在[申請報價](/docs/zh-TW/v5/asset/convert/apply-quote)接口中中有發送該字段, 則這裡會釋出該字段  
> convertRate| string| 兌換率  
> createdAt| string| 報價單創建時間  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/asset/exchange/query-convert-history?accountType=eb_convert_uta,eb_convert_funding HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1720074159814  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_convert_history(  
        accountType="eb_convert_uta,eb_convert_funding",  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getConvertHistory()  
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
            "list": [  
                {  
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
                    "extInfo": {  
                        "paramType": "opFrom",  
                        "paramValue": "broker-id-001"  
                    },  
                    "convertRate": "0.0534882723991",  
                    "createdAt": "1720071899995"  
                },  
                {  
                    "accountType": "eb_convert_uta",  
                    "exchangeTxId": "23070eb_convert_uta408933875189391360",  
                    "userId": "XXXXX",  
                    "fromCoin": "BTC",  
                    "fromCoinType": "crypto",  
                    "fromAmount": "0.1",  
                    "toCoin": "ETH",  
                    "toCoinType": "crypto",  
                    "toAmount": "1.773938248611074",  
                    "exchangeStatus": "success",  
                    "extInfo": {},  
                    "convertRate": "17.73938248611074",  
                    "createdAt": "1719974243256"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1720074457715  
    }