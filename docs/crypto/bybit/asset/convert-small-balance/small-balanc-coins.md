---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/asset/convert-small-balance/small-balanc-coins
api_type: REST
updated_at: 2026-05-27 19:14:51.270895
---

# Request a Quote

### HTTP Request

POST`/v5/asset/exchange/quote-apply`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
[accountType](/docs/v5/enum#convertaccounttype)| **true**|  string| Wallet type  
fromCoin| **true**|  string| Convert from coin (coin to sell)  
toCoin| **true**|  string| Convert to coin (coin to buy)  
requestCoin| **true**|  string| Request coin, same as fromCoin 

  * In the future, we may support requestCoin=toCoin

  
requestAmount| **true**|  string| request coin amount (the amount you want to sell)  
fromCoinType| false| string| `crypto`  
toCoinType| false| string| `crypto`  
paramType| false| string| `opFrom`, mainly used for API broker user  
paramValue| false| string| Broker ID, mainly used for API broker user  
requestId| false| string| Customised request ID 

  * a maximum length of 36
  * Generally it is useless, but it is convenient to track the quote request internally if you fill this field

  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
quoteTxId| string| Quote transaction ID. It is system generated, and it is used to confirm quote and query the result of transaction  
exchangeRate| string| Exchange rate  
fromCoin| string| From coin  
fromCoinType| string| From coin type. `crypto`  
toCoin| string| To coin  
toCoinType| string| To coin type. `crypto`  
fromAmount| string| From coin amount (amount to sell)  
toAmount| string| To coin amount (amount to buy according to exchange rate)  
expiredTime| string| The expiry time for this quote (15 seconds)  
requestId| string| Customised request ID  
extTaxAndFee| array| Compliance-related field. Currently returns an empty array, which may be used in the future  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/asset/exchange/quote-apply HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1720071077014  
    X-BAPI-RECV-WINDOW: 5000  
    X-BAPI-SIGN: XXXXXX  
    Content-Type: application/json  
    Content-Length: 172  
      
    {  
        "requestId": "test-00002",  
        "fromCoin": "ETH",  
        "toCoin": "BTC",  
        "accountType": "eb_convert_funding",  
        "requestCoin": "ETH",  
        "requestAmount": "0.1",  
        "paramType": "opFrom",  
        "paramValue": "broker-id-001"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.request_a_quote(  
        requestId="test-00002",  
        fromCoin="ETH",  
        toCoin="BTC",  
        accountType="eb_convert_funding",  
        requestCoin="ETH",  
        requestAmount="0.1",  
        paramType="opFrom",  
        paramValue="broker-id-001",  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .requestConvertQuote({  
        requestId: 'test-00002',  
        fromCoin: 'ETH',  
        toCoin: 'BTC',  
        accountType: 'eb_convert_funding',  
        requestCoin: 'ETH',  
        requestAmount: '0.1',  
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
            "quoteTxId": "10100108106409340067234418688",  
            "exchangeRate": "0.053517914861880000",  
            "fromCoin": "ETH",  
            "fromCoinType": "crypto",  
            "toCoin": "BTC",  
            "toCoinType": "crypto",  
            "fromAmount": "0.1",  
            "toAmount": "0.005351791486188000",  
            "expiredTime": "1720071092225",  
            "requestId": "test-00002",  
            "extTaxAndFee":[]  
        },  
        "retExtInfo": {},  
        "time": 1720071077265  
    }

---

# 申請報價

### HTTP 請求

POST`/v5/asset/exchange/quote-apply`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
[accountType](/docs/zh-TW/v5/enum#convertaccounttype)| **true**|  string| 帳戶類型  
fromCoin| **true**|  string| 兌出幣種  
toCoin| **true**|  string| 兌入幣種  
requestCoin| **true**|  string| 請求報價幣種, 和兌出幣種保持一致 

  * 未來, 可能會支援requestCoin=兌入幣種

  
requestAmount| **true**|  string| 請求報價幣種數量  
fromCoinType| false| string| `crypto`  
toCoinType| false| string| `crypto`  
paramType| false| string| `opFrom`, 主要用於API broker  
paramValue| false| string| Broker ID, 主要用於API broker  
requestId| false| string| 自定義的請求ID 

  * 最長不超過36位的字符串
  * 一般來說該字段無用, 可用於內部追蹤這次報價請求

  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
quoteTxId| string| 報價單號. 由系統生成, 用於後面的確認報價和查詢  
exchangeRate| string| 兌換率  
fromCoin| string| 兌出幣種  
fromCoinType| string| 兌出幣種類型. `crypto`  
toCoin| string| 兌入幣種  
toCoinType| string| 兌入幣種類型. `crypto`  
fromAmount| string| 兌出幣種數量  
toAmount| string| 兌入幣種數量  
expiredTime| string| 報價單過期的時間戳(有效期為15秒)  
requestId| string| 自定義請求ID  
extTaxAndFee| array| 合規相關字段. 目前返回一個空數組，將來可能會用到  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/asset/exchange/quote-apply HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1720071077014  
    X-BAPI-RECV-WINDOW: 5000  
    X-BAPI-SIGN: XXXXXX  
    Content-Type: application/json  
    Content-Length: 172  
      
    {  
        "requestId": "test-00002",  
        "fromCoin": "ETH",  
        "toCoin": "BTC",  
        "accountType": "eb_convert_funding",  
        "requestCoin": "ETH",  
        "requestAmount": "0.1",  
        "paramType": "opFrom",  
        "paramValue": "broker-id-001"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.request_a_quote(  
        requestId="test-00002",  
        fromCoin="ETH",  
        toCoin="BTC",  
        accountType="eb_convert_funding",  
        requestCoin="ETH",  
        requestAmount="0.1",  
        paramType="opFrom",  
        paramValue="broker-id-001",  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .requestConvertQuote({  
        requestId: 'test-00002',  
        fromCoin: 'ETH',  
        toCoin: 'BTC',  
        accountType: 'eb_convert_funding',  
        requestCoin: 'ETH',  
        requestAmount: '0.1',  
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
            "quoteTxId": "10100108106409340067234418688",  
            "exchangeRate": "0.053517914861880000",  
            "fromCoin": "ETH",  
            "fromCoinType": "crypto",  
            "toCoin": "BTC",  
            "toCoinType": "crypto",  
            "fromAmount": "0.1",  
            "toAmount": "0.005351791486188000",  
            "expiredTime": "1720071092225",  
            "requestId": "test-00002",  
            "extTaxAndFee":[]  
        },  
        "retExtInfo": {},  
        "time": 1720071077265  
    }