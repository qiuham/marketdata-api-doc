---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/rfq/trade/rfq-list
api_type: Trading
updated_at: 2026-07-20 19:13:09.106912
---

# Get Trade History

Obtain transaction information. **Up to 50 requests per second**

info

  * Field query priority: rfqId > rfqLinkId quoteId > quoteLinkId



### HTTP Request

GET`/v5/rfq/trade-list`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
rfqId| false| string| Inquiry ID  
rfqLinkId| false| string| Custom ID for RFQ; specify rfqLinkId to only check the last 3 months  
quoteId| false| string| Quote ID  
quoteLinkId| false| string| quote custom ID; specifying quoteLinkId can only check the last 3 months  
traderType| false| string| Trader type, `quote` , `request` , default `quote`  
status| false| string| Status : `Filled` `Failed`  
limit| false| integer| Return the number of items. [`1`, `100`]. Default: `50`  
cursor| false| string| Cursor. Use the `nextPageCursor` token from the response to retrieve the next page of the result set  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
result| Object|   
> cursor| string| Refer to the `cursor` request parameter  
> list| array| An array of RFQs  
>> rfqId| string| Inquiry ID  
>> rfqLinkId| string| Custom RFQ ID. Not publicly disclosed.  
>> quoteId| string| Return the completed RFQ and the executed quote id.  
>> quoteLinkId| string| Custom quote ID. Not publicly disclosed.  
>> quoteSide| string| Return of completed inquiry, execution of quote direction, `Buy` or `Sell`  
>> strategyType| string| Inquiry label  
>>status| string| Status : `Filled` `Failed`  
>> rfqDeskCode| string| The unique identification code of the inquiring party, which is not visible when anonymous was set to `true` when the RFQ was created  
>> quoteDeskCode| string| The unique identification code of the quoting party, which is not visible when anonymous is set to `true` during quotation  
>> createdAt| string| Time (ms) when the trade is created in epoch, such as 1650380963  
>> updatedAt| string| Time (ms) when the trade is updated in epoch, such as 1650380964  
>> legs| array of objects| Combination transaction  
>>> category| string| category. Valid values include: `linear`, `option` and `spot`  
>>> orderId| string| bybit order id  
>>> symbol| string| The unique instrument ID  
>>> side| string| Direction, valid values are `Buy` and `Sell`  
>>> price| string| Execution price  
>>> qty| string| Number of executions  
>>> markPrice| string| The futures markPrice at the time of transaction, the spot is indexPrice, and the option is the markPrice of the underlying Price.  
>>> execFee| string| The fee for taker or maker in the base currency paid to the Exchange executing the Block Trade.  
>>> execId| string| The unique exec(trade) ID from the exchange  
>>> resultCode| integer| The status code of the this order. "0" means success  
>>> resultMessage| string| Error message about resultCode. If resultCode is "0", resultMessage is "".  
>>> rejectParty| string| Empty if status is `Filled`. Valid values: `Taker` or `Maker` if status is `Rejected`, "rejectParty='bybit'" to indicate errors that occur on the Bybit side.  
  
### Request Example

  * HTTP
  * Python


    
    
    GET /v5/rfq/trade-list HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1676430842094  
    X-BAPI-RECV-WINDOW: 5000  
    X-BAPI-SIGN: XXXXXX  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_trade_list())  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "cursor": "",  
            "list": [  
                {  
                    "rfqId": "1755159541420049734454484077021786",  
                    "quoteId": "175515955714692291558309160384918",  
                    "quoteSide": "Buy",  
                    "strategyType": "PerpBasis",  
                    "status": "Failed",  
                    "rfqDeskCode": "1nu9d1",  
                    "quoteDeskCode": "lines100412673",  
                    "legs": [  
                        {  
                            "category": "linear",  
                            "symbol": "BTCUSDT-15AUG25",  
                            "side": "Sell",  
                            "price": "108887",  
                            "qty": "1",  
                            "orderId": "db852bcd-052e-49b7-ba10-059622e1219b",  
                            "markPrice": "",  
                            "execFee": "0",  
                            "execId": "",  
                            "resultCode": 111002,  
                            "resultMessage": "Rejected caused by another legs",  
                            "rejectParty": ""  
                        },  
                        {  
                            "category": "linear",  
                            "symbol": "BTCUSDT",  
                            "side": "Buy",  
                            "price": "132038",  
                            "qty": "1",  
                            "orderId": "69667acb-7048-48d7-90b9-ccbdfd423130",  
                            "markPrice": "",  
                            "execFee": "0",  
                            "execId": "",  
                            "resultCode": 110007,  
                            "resultMessage": "Insufficient available balance",  
                            "rejectParty": "taker"  
                        }  
                    ],  
                    "createdAt": "1755159541421",  
                    "updatedAt": "1755159654501"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1756891941267  
    }

---

# 獲取交易資訊

獲取交易資訊。**每秒最多 50 次請求**

信息

  * 字段查詢優先級：rfqId > rfqLinkId > quoteId > quoteLinkId



### HTTP 請求

GET`/v5/rfq/trade-list`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
rfqId| **false**|  string| 詢價單 ID  
rfqLinkId| **false**|  string| 自定義詢價單 ID；指定 rfqLinkId 僅能查詢最近 3 個月的數據  
quoteId| **false**|  string| 報價單 ID  
quoteLinkId| **false**|  string| 自定義報價單 ID；指定 quoteLinkId 僅能查詢最近 3 個月的數據  
traderType| **false**|  string| 交易者類型，`quote` 或 `request`，默認為 `quote`

  * `Request`：詢價方，查詢自己詢價單的成功交易
  * `Quote`：報價方，查詢自己報價單的成功交易

  
status| false| string| 狀態：`Filled` 或 `Failed`  
limit| **false**|  integer| 返回的項目數量，最多 100 項，默認 50 項  
cursor| **false**|  string| 分頁標記，請使用返回的 cursor，簽名時使用返回的原始數據，發送請求時進行 URLEncode  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
result| Object|   
> cursor| string| 分頁標記  
> list| Array| 詢價單數據陣列  
>> rfqId| string| 詢價單 ID  
>> rfqLinkId| string| 自定義詢價單 ID，客戶敏感資訊不會公開，僅返回給報價方。  
>> quoteId| string| 返回已完成的詢價單及執行的報價單 ID  
>> quoteLinkId| string| 自定義報價單 ID，客戶敏感資訊不會公開，僅返回給詢價方。  
>> quoteSide| string| 返回已完成詢價單的執行方向，`Buy` 或 `Sell`  
>> strategyType| string| 詢價標籤  
>> status| string| 狀態：`Filled` 或 `Failed`  
>> rfqDeskCode| string| 詢價方的唯一識別代碼，若詢價時設置匿名為 `true` 則不可見  
>> quoteDeskCode| string| 報價方的唯一識別代碼，若報價時設置匿名為 `true` 則不可見  
>> createdAt| string| 交易創建的時間（毫秒），例如 1650380963  
>> updatedAt| string| 交易更新的時間（毫秒），例如 1650380964  
>> legs| Array of objects| 組合交易  
>>> category| string| 類型，有效值包括：`linear`、`option` 和 `spot`  
>>> orderId| string| Bybit 訂單 ID  
>>> symbol| string| 唯一的交易品種 ID  
>>> side| string| 方向，有效值包括 `Buy` 和 `Sell`  
>>> price| string| 執行價格  
>>> qty| string| 執行數量  
>>> markPrice| string| 交易時的期貨標記價格，現貨為指數價格，期權為標的價格的標記價格  
>>> execFee| string| 支付給執行該交易的交易所的基礎貨幣的 taker 或 maker 費用  
>>> execId| string| 交易所唯一的執行交易 ID  
>>> resultCode| integer| 該訂單的狀態碼，"0" 表示成功  
>>> resultMessage| string| 關於 resultCode 的錯誤信息。如果 resultCode 為 "0"，則 resultMessage 為空字符串  
>>> rejectParty| string| 若狀態為 `Filled` 則為空。若狀態為 `Rejected`，有效值包括 `Taker` 或 `Maker`，"rejectParty='bybit'" 表示錯誤發生在 Bybit 端。  
  
### 請求示例
    
    
    GET /v5/rfq/trade-list HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1676430842094  
    X-BAPI-RECV-WINDOW: 5000  
    X-BAPI-SIGN: XXXXXX  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "cursor": "",  
            "list": [  
                {  
                    "rfqId": "1755159541420049734454484077021786",  
                    "quoteId": "175515955714692291558309160384918",  
                    "quoteSide": "Buy",  
                    "strategyType": "PerpBasis",  
                    "status": "Failed",  
                    "rfqDeskCode": "1nu9d1",  
                    "quoteDeskCode": "lines100412673",  
                    "legs": [  
                        {  
                            "category": "linear",  
                            "symbol": "BTCUSDT-15AUG25",  
                            "side": "Sell",  
                            "price": "108887",  
                            "qty": "1",  
                            "orderId": "db852bcd-052e-49b7-ba10-059622e1219b",  
                            "markPrice": "",  
                            "execFee": "0",  
                            "execId": "",  
                            "resultCode": 111002,  
                            "resultMessage": "Rejected caused by another legs",  
                            "rejectParty": ""  
                        },  
                        {  
                            "category": "linear",  
                            "symbol": "BTCUSDT",  
                            "side": "Buy",  
                            "price": "132038",  
                            "qty": "1",  
                            "orderId": "69667acb-7048-48d7-90b9-ccbdfd423130",  
                            "markPrice": "",  
                            "execFee": "0",  
                            "execId": "",  
                            "resultCode": 110007,  
                            "resultMessage": "Insufficient available balance",  
                            "rejectParty": "taker"  
                        }  
                    ],  
                    "createdAt": "1755159541421",  
                    "updatedAt": "1755159654501"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1756891941267  
    }