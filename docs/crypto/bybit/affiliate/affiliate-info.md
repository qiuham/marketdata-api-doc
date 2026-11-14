---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/affiliate/affiliate-info
api_type: REST
updated_at: 2026-11-13 19:21:00.878836
---

# Get Affiliate User Info

To use this endpoint, you should have an affiliate account and only tick "affiliate" permission while creating the API key.  
Affiliate site: <https://affiliates.bybit.com>

tip

  * Use master UID only
  * The api key can only have "Affiliate" permission
  * The transaction volume and deposit amount are the total amount of the user done on Bybit, and have nothing to do with commission settlement. Any transaction volume data related to commission settlement is subject to the Affiliate Portal.



### HTTP Request

GET`/v5/user/aff-customer-info`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
uid| **true**|  string| The master account UID of affiliate's client  
coin| false| string| Coin type for filtering, e.g., `USDT`  
business| false| string| Business line filter. `1`: Derivatives, `2`: Spot, `3`: ByFi, `4`: USDC, `5`: Options  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
uid| string| UID  
vipLevel| string| VIP tier. Common values: `0` (No VIP), `1`, `2`, `3`, `4`, `99` (VVIP)  
takerVol30Day| string| Taker volume in last 30 days (USDT). All volume fields below include Derivatives, Options, and Spot volume  
makerVol30Day| string| Maker volume in last 30 days (USDT)  
tradeVol30Day| string| Total trading volume in last 30 days (USDT)  
depositAmount30Day| string| Deposit amount in last 30 days (USDT), updated every 5 mins  
takerVol365Day| string| Lifetime taker volume since becoming affiliate's client (USDT)  
makerVol365Day| string| Lifetime maker volume since becoming affiliate's client (USDT)  
tradeVol365Day| string| Lifetime total trading volume since becoming affiliate's client (USDT)  
depositAmount365Day| string| Lifetime total deposit amount since becoming affiliate's client (USDT). Includes all deposit types regardless of account or business  
totalWalletBalance| string| Wallet balance range 

  * `1`: less than 100 USDT
  * `2`: [100, 250) USDT
  * `3`: [250, 500) USDT
  * `4`: >= 500 USDT

  
depositUpdateTime| string| UTC timestamp (ms) of the latest deposit data update  
volUpdateTime| string| UTC timestamp (ms) of the latest trading volume data update  
KycLevel| integer| KYC level. `0`: No KYC, `1`: KYC Level 1, `2`: KYC Level 2  
tradfiTradeVol30Day| string| TradFi trade volume in last 30 days (USDT)  
tradfiTradeVol365Day| string| TradFi trade volume in last 365 days (USDT)  
commissions30Day| object| Commission breakdown by coin for the last 30 days (e.g., BTC, ETH, USDT)  
commissions365Day| object| Commission breakdown by coin for the last 365 days (e.g., BTC, ETH, USDT)  
paySendAmount30Day| string| Payment amount in the last 30 days  
payFtt| string| Pay first transaction amount  
cardFtt| string| Card first-time transaction amount  
[](/docs/api-explorer/v5/user/affiliate-info)

* * *

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/user/aff-customer-info?uid=1513500 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1685596324209  
    X-BAPI-RECV-WINDOW: 5000  
    X-BAPI-SIGN: xxxxxx  
    Content-Type: application/json  
    
    
    
      
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getAffiliateUserInfo({ uid: '1513500' })  
      .then((response) => {  
        console.log(response);  
      })  
      .catch((error) => {  
        console.error(error);  
      });  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "uid": "1087997",  
            "takerVol30Day": "17061.64983",  
            "makerVol30Day": "10756.454142",  
            "tradeVol30Day": "27818.103972",  
            "depositAmount30Day": "0",  
            "takerVol365Day": "1183752.53919162",  
            "makerVol365Day": "44349.42819772",  
            "tradeVol365Day": "1228101.96738934",  
            "depositAmount365Day": "0",  
            "totalWalletBalance": "4",  
            "depositUpdateTime": "2026-02-04 00:00:00",  
            "vipLevel": "5",  
            "volUpdateTime": "2026-02-04 00:00:00",  
            "KycLevel": 0,  
            "tradfiTradeVol30Day": "1828890.6352",  
            "tradfiTradeVol365Day": "1828890.6352",  
            "commissions30Day": {  
                "BTC": "",  
                "ETH": "",  
                "MNT": "2.14012088",  
                "USDC": "",  
                "USDT": "17.0461748"  
            },  
            "commissions365Day": {  
                "BTC": "0.00012928",  
                "ETH": "0.00099384",  
                "MNT": "95.72886531",  
                "USDC": "2.81382591",  
                "USDT": "130.48078429"  
            },  
            "paySendAmount30Day": "1000.00",  
            "payFtt": "100.00",  
            "cardFtt": "50.00"  
        },  
        "retExtInfo": {},  
        "time": 1770197061282  
    }

---

# 查詢代理用戶信息

要使用此接口，您应该有一个代理商账户，并且在创建 API 密钥时仅勾选“代理商”权限。  
代理商网站: <https://affiliates.bybit.com>

提示

  * 僅支持使用母帳戶uid
  * 若要查詢該接口, api key僅能擁有代理商權限, 若擁有任何其他權限項, 請移除
  * 交易量和入金金額為用戶在Bybit上的總量，與結傭無關，任何結傭相關的交易量數據，以Affiliate Portal為準。



### HTTP 請求

GET`/v5/user/aff-customer-info`

### 請求參數

參數| 是否必須| 類型| 說明  
---|---|---|---  
uid| **true**|  string| 被代理用戶的母帳戶uid  
coin| false| string| 幣種篩選，如 `USDT`  
business| false| string| 業務線篩選。`1`: 衍生品，`2`: 現貨，`3`: ByFi，`4`: USDC，`5`: 期權  
  
### 返回參數

參數| 類型| 說明  
---|---|---  
uid| string| 帳戶uid  
vipLevel| string| VIP等級。常見值：`0`（無VIP）、`1`、`2`、`3`、`4`、`99`（VVIP）  
takerVol30Day| string| 過去30天的吃單交易量（USDT）。以下所有交易量字段均包含期貨、期權和現貨交易量  
makerVol30Day| string| 過去30天的掛單交易量（USDT）  
tradeVol30Day| string| 過去30天的總交易量（USDT）  
depositAmount30Day| string| 過去30天的入金金額（USDT），5分鐘內更新  
takerVol365Day| string| 成為代理直客以來的累計吃單交易量（USDT）  
makerVol365Day| string| 成為代理直客以來的累計掛單交易量（USDT）  
tradeVol365Day| string| 成為代理直客以來的累計總交易量（USDT）  
depositAmount365Day| string| 成為代理直客以來的累計入金總額（USDT），包含所有帳戶及業務類型的入金  
totalWalletBalance| string| 資產餘額區間

  * `1`: 少於100 USDT
  * `2`: 100(含) ~ 250 USDT
  * `3`: 250(含) ~ 500 USDT
  * `4`: >= 500 USDT

  
depositUpdateTime| string| 入金數據最新更新時間（UTC毫秒時間戳）  
volUpdateTime| string| 交易量數據最新更新時間（UTC毫秒時間戳）  
KycLevel| integer| KYC等級。`0`: 未認證，`1`: KYC Level 1，`2`: KYC Level 2  
tradfiTradeVol30Day| string| 過去30天的TradFi交易量（USDT）  
tradfiTradeVol365Day| string| 過去365天的TradFi交易量（USDT）  
commissions30Day| object| 過去30天按幣種劃分的佣金明細（如BTC、ETH、USDT等）  
commissions365Day| object| 過去365天按幣種劃分的佣金明細（如BTC、ETH、USDT等）  
paySendAmount30Day| string| 最近30天的支付金額  
payFtt| string| Pay首次交易金額  
cardFtt| string| Card首次交易金額  
[](/docs/zh-TW/api-explorer/v5/user/affiliate-info)

* * *

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/user/aff-customer-info?uid=1513500 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1685596324209  
    X-BAPI-RECV-WINDOW: 5000  
    X-BAPI-SIGN: xxxxxx  
    Content-Type: application/json  
    
    
    
      
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getAffiliateUserInfo({ uid: '1513500' })  
      .then((response) => {  
        console.log(response);  
      })  
      .catch((error) => {  
        console.error(error);  
      });  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "uid": "1087997",  
            "takerVol30Day": "17061.64983",  
            "makerVol30Day": "10756.454142",  
            "tradeVol30Day": "27818.103972",  
            "depositAmount30Day": "0",  
            "takerVol365Day": "1183752.53919162",  
            "makerVol365Day": "44349.42819772",  
            "tradeVol365Day": "1228101.96738934",  
            "depositAmount365Day": "0",  
            "totalWalletBalance": "4",  
            "depositUpdateTime": "2026-02-04 00:00:00",  
            "vipLevel": "5",  
            "volUpdateTime": "2026-02-04 00:00:00",  
            "KycLevel": 0,  
            "tradfiTradeVol30Day": "1828890.6352",  
            "tradfiTradeVol365Day": "1828890.6352",  
            "commissions30Day": {  
                "BTC": "",  
                "ETH": "",  
                "MNT": "2.14012088",  
                "USDC": "",  
                "USDT": "17.0461748"  
            },  
            "commissions365Day": {  
                "BTC": "0.00012928",  
                "ETH": "0.00099384",  
                "MNT": "95.72886531",  
                "USDC": "2.81382591",  
                "USDT": "130.48078429"  
            },  
            "paySendAmount30Day": "1000.00",  
            "payFtt": "100.00",  
            "cardFtt": "50.00"  
        },  
        "retExtInfo": {},  
        "time": 1770197061282  
    }