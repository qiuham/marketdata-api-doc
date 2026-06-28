---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/pre-upgrade/settlement
api_type: REST
updated_at: 2026-06-28 19:13:50.083030
---

# Get Pre-upgrade Transaction Log

Query transaction logs which occurred in the USDC Derivatives wallet before the account was upgraded to a Unified account.

By category="linear", you can query USDC Perps transaction logs occurred during classic account By category="option", you can query Options transaction logs occurred during classic account

You can get USDC Perpetual, Option records.

info

USDC Perpeual & Option support the recent 6 months data. Please download older data via GUI

### HTTP Request

GET`/v5/pre-upgrade/account/transaction-log`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
[category](/docs/v5/enum#category)| **true**|  string| Product type `linear`, `option`  
baseCoin| false| string| BaseCoin, uppercase only. e.g., BTC of BTCPERP  
[type](/docs/v5/enum#type)| false| string| Types of transaction logs  
startTime| false| integer| The start timestamp (ms) 

  * startTime and endTime are not passed, return 7 days by default
  * Only startTime is passed, return range between startTime and startTime+7 days
  * Only endTime is passed, return range between endTime-7 days and endTime
  * If both are passed, the rule is endTime - startTime <= 7 days

  
endTime| false| integer| The end timestamp (ms)  
limit| false| integer| Limit for data size per page. [`1`, `50`]. Default: `20`  
cursor| false| string| Cursor. Used for pagination  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array| Object  
> symbol| string| Symbol name  
> category| string| Product type  
> side| string| Side. `Buy`,`Sell`,`None`  
> transactionTime| string| Transaction timestamp (ms)  
> [type](/docs/v5/enum#type)| string| Type  
> qty| string| Quantity  
> size| string| Size  
> currency| string| USDC、USDT、BTC、ETH  
> tradePrice| string| Trade price  
> funding| string| Funding fee 

  * Positive value means receiving funding fee
  * Negative value means deducting funding fee

  
> fee| string| Trading fee 

  * Positive fee value means expense
  * Negative fee value means rebates

  
> cashFlow| string| Cash flow  
> change| string| Change  
> cashBalance| string| Cash balance  
> feeRate| string| 

  * When type=`TRADE`, then it is trading fee rate
  * When type=`SETTLEMENT`, it means funding fee rate. For side=Buy, feeRate=market fee rate; For side=Sell, feeRate= - market fee rate

  
> bonusChange| string| The change of bonus  
> tradeId| string| Trade ID  
> orderId| string| Order ID  
> orderLinkId| string| User customised order ID  
nextPageCursor| string| Cursor. Used for pagination  
  
### Request Example

  * HTTP
  * Python


    
    
    GET /v5/pre-upgrade/account/transaction-log?category=option HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1686808288265  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "nextPageCursor": "21%3A0%2C21%3A0",  
            "list": [  
                {  
                    "symbol": "ETH-14JUN23-1750-C",  
                    "side": "Buy",  
                    "funding": "",  
                    "orderLinkId": "",  
                    "orderId": "",  
                    "fee": "0",  
                    "change": "0",  
                    "cashFlow": "0",  
                    "transactionTime": "1686729604507",  
                    "type": "DELIVERY",  
                    "feeRate": "0",  
                    "bonusChange": "",  
                    "size": "0",  
                    "qty": "0.5",  
                    "cashBalance": "1001.1438885",  
                    "currency": "USDC",  
                    "category": "option",  
                    "tradePrice": "1740.25036667",  
                    "tradeId": ""  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1686809006792  
    }

---

# 查詢升級前交易日誌

查詢升級到統一帳戶之前USDC合約帳戶裡的交易日誌

信息

  * USDC永續和期權僅支持查詢最近6個月的數據, 對於更老的數據, 請前往網頁端下載
  * 通過category=linear, 查詢到在經典帳戶期間產生的USDC永續交易日誌數據  

  * 通過category=option, 查詢到在經典帳戶期間產生的期權交易日誌數據



### HTTP 請求

GET`/v5/pre-upgrade/account/transaction-log`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
[category](/docs/zh-TW/v5/enum#category)| **true**|  string| 交易產品類型. `linear`: USDC永續, `option`: 期權  
baseCoin| false| string| 交易幣種. 例如： BTCUSDT 的 baseCoin 是 BTC  
[type](/docs/zh-TW/v5/enum#type)| false| string| 交易日誌的類型  
startTime| false| integer| 開始時間戳 (毫秒) 

  * startTime 和 endTime都不傳入, 則默認返回最近7天的數據
  * startTime 和 endTime都傳入的話, 則確保endTime - startTime <= 7天
  * 若只傳startTime，則查詢startTime和startTime+7天的數據
  * 若只傳endTime，則查詢endTime-7天和endTime的數據

  
endTime| false| integer| 結束時間戳 (毫秒)  
limit| false| integer| 每頁數量, 最大50. 默認每頁20條  
cursor| false| string| 游標，用於翻頁  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
list| array| Object  
> symbol| string| 合約名稱  
> category| string| 產品類型  
> side| string| 方向. `Buy`,`Sell`,`None`  
> transactionTime| string| 交易時間戳（毫秒）  
> [type](/docs/zh-TW/v5/enum#type)| string| 類型  
> qty| string| 數量  
> size| string| 倉位  
> currency| string| USDC、USDT、BTC、ETH  
> tradePrice| string| 交易價格  
> funding| string| 資金費用. 正數表示用戶收取xx資金費，負數表示用戶支出xx資金費  
> fee| string| 手續費，正數表示用戶付出xx手續費，負數表示返佣  
> cashFlow| string| 現金流  
> change| string| 變更  
> cashBalance| string| 餘額（當前幣種）  
> feeRate| string| 

  * 對於type=`TRADE`, 則表示交易手續費率
  * 對於type=`SETTLEMENT`, 則表示資金費率. 當side=Buy, feeRate=市場結算費率; 當side=Sell, feeRate=-市場結算費率

  
> bonusChange| string| 體驗金的變化  
> tradeId| string| 交易id  
> orderId| string| 訂單id  
> orderLinkId| string| 用戶自定義訂單id  
nextPageCursor| string| 游標，用於翻頁  
  
### 請求示例

  * HTTP
  * Python


    
    
    GET /v5/pre-upgrade/account/transaction-log?category=option HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1686808288265  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "nextPageCursor": "21%3A0%2C21%3A0",  
            "list": [  
                {  
                    "symbol": "ETH-14JUN23-1750-C",  
                    "side": "Buy",  
                    "funding": "",  
                    "orderLinkId": "",  
                    "orderId": "",  
                    "fee": "0",  
                    "change": "0",  
                    "cashFlow": "0",  
                    "transactionTime": "1686729604507",  
                    "type": "DELIVERY",  
                    "feeRate": "0",  
                    "bonusChange": "",  
                    "size": "0",  
                    "qty": "0.5",  
                    "cashBalance": "1001.1438885",  
                    "currency": "USDC",  
                    "category": "option",  
                    "tradePrice": "1740.25036667",  
                    "tradeId": ""  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1686809006792  
    }