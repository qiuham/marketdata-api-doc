---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/bybit-card/asset-records
api_type: REST
updated_at: 2026-11-13 19:22:19.532174
---

# Query Asset Records

Query card transaction history. Supports filtering by status, last digits of card number, merchant name, transaction type, time range, etc. Results are paginated.

tip

`type` is required when neither `txnId` nor `orderNo` is provided. This restriction does not apply when either `txnId` or `orderNo` is present.

### HTTP Request

POST`/v5/card/transaction/query-asset-records`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
statusCode| false| string| Transaction status code. `0`: Pending, `1`: Cleared, `2`: Declined  
limit| false| integer| Number of items per page. Default: `100`. Range: [`1`, `500`]  
page| false| integer| Page number. Default: `1`. Min: `1`  
pan4| false| string| Last 2/4 digits of card number, used to filter transactions of a specific card  
createBeginTime| false| integer| Start time of transaction (Unix ms timestamp)  
createEndTime| false| integer| End time of transaction (Unix ms timestamp)  
merchName| false| string| Merchant name. Supports fuzzy search  
type| false| string| Query type.  
`SIDE_QUERY_AUTH`: Authorization  
`SIDE_QUERY_FINANCIAL`: Clearing. Requires `txnId` and `orderNo`.  
`SIDE_QUERY_REFUND`: Refund. Requires `txnId` and `orderNo`.  
The following query types are available to all users:  
`SIDE_QUERY_AUTH_ALL`: All authorization transactions  
`SIDE_QUERY_AUTH_REVERSAL`: Authorization reversals  
`SIDE_QUERY_FINANCIAL_ALL`: All clearing transactions  
`SIDE_QUERY_FINANCIAL_REFUND`: Clearing refunds  
txnId| false| string| Transaction ID. Exact match  
cardToken| false| string| Card token, used to identify a specific card  
orderNo| false| string| Order number. Exact match  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
retCode| integer| Business return code. `0`: success; non-zero: failure  
retMsg| string| Return message  
result| object|   
> pageSize| integer| Number of items per page  
> pageNo| integer| Current page number  
> totalCount| integer| Total number of records  
> data| array| Transaction record list  
>> pan4| string| Last 4 digits of card number  
>> pan6| string| First 6 digits of card number (BIN)  
>> tradeStatus| string| Trade status. `0`: In_Progress, `1`: Completed, `2`: Declined, `3`: Reversal  
>> side| string| Transaction type. `1`: Authorization, `2`: Authorization Reversal, `3`: Transaction, `4`: Refund (unDeduct), `5`: Refund, `6`: Chargeback, `7`: Transaction (Direct), `8`: Refund Reversal, `9`: Chargeback Reversal, `10`: Refund Request, `11`: Refund Reversal Request, `12`: Chargeback Fee, `13`: ATM Withdrawal  
>> basicAmount| string| Total amount  
>> basicCurrency| string| Total amount currency code  
>> transactionAmount| string| Amount before tax  
>> transactionCurrency| string| Amount before tax currency code  
>> txnCreate| integer| Transaction creation time (Unix ms timestamp)  
>> merchCountry| string| Merchant country  
>> merchCity| string| Merchant city  
>> merchName| string| Merchant name  
>> txnId| string| Transaction ID  
>> declinedReason| string| Declined reason. Only populated when transaction is declined  
>> totalFees| string| Total fees  
>> uid| integer| User ID  
>> transactionCurrencyAmount| string| Fiat transaction amount  
>> fxPad| string| Fee  
>> interchangeFee| string| Interchange fee (non-cumulative, unrelated to users, card network related)  
>> billAmount| string| Bill amount  
>> paidAmount| string| Transaction currency amount  
>> paidCurrency| string| Paid currency code  
>> bonusAmount| string| Trial bonus  
>> foreignTransactionFee| string| Foreign transaction fee  
>> totalTax| string| Total tax  
>> paidFiat| string| Fiat paid amount  
>> withdrawalFee| string| Withdrawal fee  
>> status| string| Transaction status. `-1`: Init, `0`: Pending, `1`: Success, `2`: Fail  
>> orderNo| string| Order number  
>> mccCode| string| Merchant Category Code (MCC)  
>> merchCategoryDesc| string| Merchant category description  
  
* * *

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/card/transaction/query-asset-records?limit=10&page=1 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672211918471  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    import requests  
      
    url = "https://api-testnet.bybit.com/v5/card/transaction/query-asset-records"  
    headers = {  
        "X-BAPI-API-KEY": "xxxxxxxxxxxxxxxxxx",  
        "X-BAPI-SIGN": "XXXXX",  
        "X-BAPI-TIMESTAMP": "1672211918471",  
        "X-BAPI-RECV-WINDOW": "5000"  
    }  
    params = {  
        "limit": 10,  
        "page": 1  
    }  
    response = requests.post(url, headers=headers, params=params)  
    print(response.json())  
    
    
    
    const axios = require('axios');  
      
    const url = 'https://api-testnet.bybit.com/v5/card/transaction/query-asset-records';  
    const headers = {  
      'X-BAPI-API-KEY': 'xxxxxxxxxxxxxxxxxx',  
      'X-BAPI-SIGN': 'XXXXX',  
      'X-BAPI-TIMESTAMP': '1672211918471',  
      'X-BAPI-RECV-WINDOW': '5000'  
    };  
    const params = { limit: 10, page: 1 };  
      
    axios.post(url, {}, { headers, params })  
      .then(response => console.log(response.data))  
      .catch(error => console.error(error));  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "pageSize": 100,  
            "pageNo": 1,  
            "totalCount": 2,  
            "data": [  
                {  
                    "pan4": "1234",  
                    "pan6": "456789",  
                    "tradeStatus": "1",  
                    "side": "3",  
                    "basicAmount": "101.50",  
                    "basicCurrency": "USD",  
                    "transactionAmount": "100.00",  
                    "transactionCurrency": "USD",  
                    "txnCreate": 1672211918471,  
                    "merchCountry": "US",  
                    "merchCity": "New York",  
                    "merchName": "Amazon",  
                    "txnId": "TXN20230101001",  
                    "declinedReason": "",  
                    "totalFees": "1.50",  
                    "uid": 100001,  
                    "transactionCurrencyAmount": "100.00",  
                    "fxPad": "",  
                    "interchangeFee": "0.50",  
                    "billAmount": "101.50",  
                    "paidAmount": "101.50",  
                    "paidCurrency": "USDT",  
                    "bonusAmount": "0",  
                    "foreignTransactionFee": "0",  
                    "totalTax": "1.50",  
                    "paidFiat": "0",  
                    "withdrawalFee": "0",  
                    "status": "1",  
                    "orderNo": "ORD20230101001",  
                    "mccCode": "5411",  
                    "merchCategoryDesc": "Grocery Stores"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1672211918471  
    }

---

# 查詢資產記錄

查詢卡交易歷史記錄，支持按狀態、卡號後幾位、商戶名、交易類型、時間範圍等條件篩選，返回分頁結果。

提示

若入參未傳 `txnId` 也未傳 `orderNo`，則 `type` 為必填項。傳入 `txnId` 或 `orderNo` 時不受此限制。

### HTTP 請求

POST`/v5/card/transaction/query-asset-records`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
statusCode| false| string| 交易狀態碼。`0`: 待處理, `1`: 已清算, `2`: 已拒絕  
limit| false| integer| 每頁條目數，默認 `100`，範圍：[`1`, `500`]  
page| false| integer| 頁碼，默認 `1`，最小值 `1`  
pan4| false| string| 卡後 2/4 位，用於篩選特定卡片的交易  
createBeginTime| false| integer| 交易開始時間（Unix 毫秒時間戳）  
createEndTime| false| integer| 交易截止時間（Unix 毫秒時間戳）  
merchName| false| string| 商戶名稱，支持模糊搜索  
type| false| string| 查詢類型。  
`SIDE_QUERY_AUTH`: 授權交易  
`SIDE_QUERY_FINANCIAL`: 清算交易。須傳入 `txnId` 和 `orderNo`。  
`SIDE_QUERY_REFUND`: 退款交易。須傳入 `txnId` 和 `orderNo`。  
以下查詢類型適用於所有用戶：  
`SIDE_QUERY_AUTH_ALL`: 所有授權交易  
`SIDE_QUERY_AUTH_REVERSAL`: 授權撤銷交易  
`SIDE_QUERY_FINANCIAL_ALL`: 所有清算交易  
`SIDE_QUERY_FINANCIAL_REFUND`: 清算退款交易  
txnId| false| string| 交易 ID，精確匹配  
cardToken| false| string| 卡 Token，用於標識特定卡片  
orderNo| false| string| 訂單號，精確匹配  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
retCode| integer| 業務返回碼。`0`: 成功；非零: 失敗  
retMsg| string| 返回消息  
result| object|   
> pageSize| integer| 每頁條數  
> pageNo| integer| 當前頁碼  
> totalCount| integer| 總記錄數  
> data| array| 交易記錄列表  
>> pan4| string| 卡後 4 位  
>> pan6| string| 卡前 6 位（BIN 號）  
>> tradeStatus| string| 交易狀態。`0`: 處理中, `1`: 已完成, `2`: 已拒絕, `3`: 已撤銷  
>> side| string| 交易類型。`1`: 授權, `2`: 授權撤銷, `3`: 扣款, `4`: 退款（unDeduct）, `5`: 退款, `6`: 拒付, `7`: 直接扣款, `8`: 退款撤銷, `9`: 拒付撤銷, `10`: 退款請求, `11`: 退款撤銷請求, `12`: 拒付費, `13`: ATM 取款  
>> basicAmount| string| 總金額  
>> basicCurrency| string| 總金額幣種代碼  
>> transactionAmount| string| 不含稅金額  
>> transactionCurrency| string| 不含稅金額幣種代碼  
>> txnCreate| integer| 交易創建時間（Unix 毫秒時間戳）  
>> merchCountry| string| 商戶所在國家  
>> merchCity| string| 商戶所在城市  
>> merchName| string| 商戶名稱  
>> txnId| string| 交易 ID  
>> declinedReason| string| 拒絕原因，僅當交易被拒絕時有值  
>> totalFees| string| 總費用  
>> uid| integer| 用戶 ID  
>> transactionCurrencyAmount| string| 法幣交易金額  
>> fxPad| string| 手續費  
>> interchangeFee| string| 交換費（不叠加，與用戶無關，卡組相關）  
>> billAmount| string| 賬單金額  
>> paidAmount| string| 交易幣種金額  
>> paidCurrency| string| 實付貨幣代碼  
>> bonusAmount| string| 體驗金  
>> foreignTransactionFee| string| 外幣交易手續費  
>> totalTax| string| 總稅費  
>> paidFiat| string| 法幣支付金額  
>> withdrawalFee| string| 提現手續費  
>> status| string| 交易狀態。`-1`: 初始化, `0`: 待處理, `1`: 成功, `2`: 失敗  
>> orderNo| string| 訂單號  
>> mccCode| string| 商戶類別代碼（MCC Code）  
>> merchCategoryDesc| string| 商戶類別描述  
  
* * *

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/card/transaction/query-asset-records?limit=10&page=1 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672211918471  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    import requests  
      
    url = "https://api-testnet.bybit.com/v5/card/transaction/query-asset-records"  
    headers = {  
        "X-BAPI-API-KEY": "xxxxxxxxxxxxxxxxxx",  
        "X-BAPI-SIGN": "XXXXX",  
        "X-BAPI-TIMESTAMP": "1672211918471",  
        "X-BAPI-RECV-WINDOW": "5000"  
    }  
    params = {  
        "limit": 10,  
        "page": 1  
    }  
    response = requests.post(url, headers=headers, params=params)  
    print(response.json())  
    
    
    
    const axios = require('axios');  
      
    const url = 'https://api-testnet.bybit.com/v5/card/transaction/query-asset-records';  
    const headers = {  
      'X-BAPI-API-KEY': 'xxxxxxxxxxxxxxxxxx',  
      'X-BAPI-SIGN': 'XXXXX',  
      'X-BAPI-TIMESTAMP': '1672211918471',  
      'X-BAPI-RECV-WINDOW': '5000'  
    };  
    const params = { limit: 10, page: 1 };  
      
    axios.post(url, {}, { headers, params })  
      .then(response => console.log(response.data))  
      .catch(error => console.error(error));  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "pageSize": 100,  
            "pageNo": 1,  
            "totalCount": 2,  
            "data": [  
                {  
                    "pan4": "1234",  
                    "pan6": "456789",  
                    "tradeStatus": "1",  
                    "side": "3",  
                    "basicAmount": "101.50",  
                    "basicCurrency": "USD",  
                    "transactionAmount": "100.00",  
                    "transactionCurrency": "USD",  
                    "txnCreate": 1672211918471,  
                    "merchCountry": "US",  
                    "merchCity": "New York",  
                    "merchName": "Amazon",  
                    "txnId": "TXN20230101001",  
                    "declinedReason": "",  
                    "totalFees": "1.50",  
                    "uid": 100001,  
                    "transactionCurrencyAmount": "100.00",  
                    "fxPad": "",  
                    "interchangeFee": "0.50",  
                    "billAmount": "101.50",  
                    "paidAmount": "101.50",  
                    "paidCurrency": "USDT",  
                    "bonusAmount": "0",  
                    "foreignTransactionFee": "0",  
                    "totalTax": "1.50",  
                    "paidFiat": "0",  
                    "withdrawalFee": "0",  
                    "status": "1",  
                    "orderNo": "ORD20230101001",  
                    "mccCode": "5411",  
                    "merchCategoryDesc": "Grocery Stores"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1672211918471  
    }