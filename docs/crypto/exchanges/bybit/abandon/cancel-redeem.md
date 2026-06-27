---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/abandon/cancel-redeem
api_type: REST
updated_at: 2026-05-27 19:13:38.515882
---

# Get Transaction Log

Query transaction logs in the derivatives wallet (classic account), and inverse derivatives account (upgraded to UTA)

> **Permission** : "Contract - Position"  
>  **Apply to** : classic account, [UTA1.0](/docs/v5/acct-mode#uta-10)(inverse)

### HTTP Request

GET`/v5/account/contract-transaction-log`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
currency| false| string| Currency, uppercase only  
baseCoin| false| string| BaseCoin, uppercase only. e.g., BTC of BTCPERP  
[type](/docs/v5/enum#typecontract-translog)| false| string| Types of transaction logs  
startTime| false| integer| The start timestamp (ms) 

  * startTime and endTime are not passed, return 7 days by default
  * Only startTime is passed, return range between startTime and startTime+7 days
  * Only endTime is passed, return range between endTime-7 days and endTime
  * If both are passed, the rule is endTime - startTime <= 7 days

  
endTime| false| integer| The end timestamp (ms)  
limit| false| integer| Limit for data size per page. [`1`, `50`]. Default: `20`  
cursor| false| string| Cursor. Use the `nextPageCursor` token from the response to retrieve the next page of the result set  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array| Object  
> id| string| Unique id  
> symbol| string| Symbol name  
> category| string| Product type  
> side| string| Side. `Buy`,`Sell`,`None`  
> transactionTime| string| Transaction timestamp (ms)  
> [type](/docs/v5/enum#type)| string| Type  
> qty| string| Quantity 

  * Perps & Futures: it is the quantity for each trade entry and it does not have direction

  
> size| string| Size. The rest position size after the trade is executed, and it has direction, i.e., short with "-"  
> currency| string| currency  
> tradePrice| string| Trade price  
> funding| string| Funding fee 

  * Positive value means deducting funding fee
  * Negative value means receiving funding fee

  
> fee| string| Trading fee 

  * Positive fee value means expense
  * Negative fee value means rebates

  
> cashFlow| string| Cash flow, e.g., (1) close the position, and unRPL converts to RPL, (2) transfer in or transfer out. This does not include trading fee, funding fee  
> change| string| Change = cashFlow - funding - fee  
> cashBalance| string| Cash balance. This is the wallet balance after a cash change  
> feeRate| string| 

  * When type=`TRADE`, then it is trading fee rate
  * When type=`SETTLEMENT`, it means funding fee rate. For side=Buy, feeRate=market fee rate; For side=Sell, feeRate= - market fee rate

  
> bonusChange| string| The change of bonus  
> tradeId| string| Trade ID  
> orderId| string| Order ID  
> orderLinkId| string| User customised order ID  
nextPageCursor| string| Refer to the `cursor` request parameter  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/account/contract-transaction-log?limit=1&symbol=BTCUSD HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1714035117255  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
      
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getClassicTransactionLogs({  
        limit: 1,  
        symbol: 'BTCUSD',  
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
        "retMsg": "OK",  
        "result": {  
            "list": [  
                {  
                    "id": "467153",  
                    "symbol": "BTCUSD",  
                    "category": "inverse",  
                    "side": "Sell",  
                    "transactionTime": "1714032000000",  
                    "type": "SETTLEMENT",  
                    "qty": "1000",  
                    "size": "-1000",  
                    "currency": "BTC",  
                    "tradePrice": "63974.88",  
                    "funding": "-0.00000156",  
                    "fee": "",  
                    "cashFlow": "0.00000000",  
                    "change": "0.00000156",  
                    "cashBalance": "1.1311",  
                    "feeRate": "-0.00010000",  
                    "bonusChange": "",  
                    "tradeId": "423a565c-f1b6-4c81-bc62-760cd7dd89e7",  
                    "orderId": "",  
                    "orderLinkId": ""  
                }  
            ],  
            "nextPageCursor": "cursor_id%3D467153%26"  
        },  
        "retExtInfo": {},  
        "time": 1714035117258  
    }

---

# 交易日誌

支持查詢經典帳戶下合約錢包, 以及統一帳戶下反向合約錢包裡的交易日誌

> API key權限: "合約 - 倉位"  
>  適用於: 經典帳戶, [統一帳戶1.0](/docs/zh-TW/v5/acct-mode#%E7%B5%B1%E4%B8%80%E5%B8%B3%E6%88%B610)(反向合約)

### HTTP 請求

GET`/v5/account/contract-transaction-log`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
currency| false| string| 貨幣  
baseCoin| false| string| 交易幣種. 例如： BTCUSDT 的 baseCoin 是 BTC  
[type](/docs/zh-TW/v5/enum#typecontract-translog)| false| string| 交易日誌的類型  
startTime| false| integer| 開始時間戳 (毫秒) 

  * startTime 和 endTime都不傳入, 則默認返回最近7天的數據
  * startTime 和 endTime都傳入的話, 則確保endTime - startTime ≤ 7天
  * 若只傳startTime，則查詢startTime和startTime+7天的數據
  * 若只傳endTime，則查詢endTime-7天和endTime的數據

  
endTime| false| integer| 結束時間戳 (毫秒)  
limit| false| integer| 每頁數量, 最大50. 默認每頁20條  
cursor| false| string| 游標，用於翻頁  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
list| array| Object  
> id| string| 唯一id  
> symbol| string| 合約名稱  
> category| string| 產品類型  
> side| string| 方向. `Buy`,`Sell`,`None`  
> transactionTime| string| 交易時間戳（毫秒）  
> [type](/docs/zh-TW/v5/enum#type)| string| 類型  
> qty| string| 數量. 

  * 期貨: 對於成交的流水來說, 這裡的qty表示每筆成交的數量, 不帶方向

  
> size| string| 倉位. 特別地, 對於成交的流水來說, 這裡的size表示成交後的倉位大小, 帶有方向, 比如空倉, 則有"-"  
> currency| string| 幣種  
> tradePrice| string| 交易價格  
> funding| string| 資金費用. 正數表示用戶支出xx資金費，負數表示用戶收取xx資金費  
> fee| string| 手續費，正數表示用戶付出xx手續費，負數表示返佣  
> cashFlow| string| 現金流, 比如平倉時的未平盈虧結算, 以及劃入劃出等. 該值不包含任何手續費或者資金費  
> change| string| 變更 = cashFlow + funding - fee  
> cashBalance| string| 餘額（當前幣種）, 資金流發生後的該幣種的錢包餘額  
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
  * Node.js


    
    
    GET /v5/account/contract-transaction-log?limit=1&symbol=BTCUSD HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1714035117255  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
      
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getClassicTransactionLogs({  
        limit: 1,  
        symbol: 'BTCUSD',  
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
        "retMsg": "OK",  
        "result": {  
            "list": [  
                {  
                    "id": "467153",  
                    "symbol": "BTCUSD",  
                    "category": "inverse",  
                    "side": "Sell",  
                    "transactionTime": "1714032000000",  
                    "type": "SETTLEMENT",  
                    "qty": "1000",  
                    "size": "-1000",  
                    "currency": "BTC",  
                    "tradePrice": "63974.88",  
                    "funding": "-0.00000156",  
                    "fee": "",  
                    "cashFlow": "0.00000000",  
                    "change": "0.00000156",  
                    "cashBalance": "1.1311",  
                    "feeRate": "-0.00010000",  
                    "bonusChange": "",  
                    "tradeId": "423a565c-f1b6-4c81-bc62-760cd7dd89e7",  
                    "orderId": "",  
                    "orderLinkId": ""  
                }  
            ],  
            "nextPageCursor": "cursor_id%3D467153%26"  
        },  
        "retExtInfo": {},  
        "time": 1714035117258  
    }