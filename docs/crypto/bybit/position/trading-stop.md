---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/position/trading-stop
api_type: Position
updated_at: 2026-09-25 18:45:31.875416
---

# Get Pre-upgrade Trade History

Get users' execution records which occurred before you upgraded the account to a Unified account, sorted by `execTime` in descending order It supports to query USDT perpetual, USDC perpetual, Inverse perpetual, Inverse futures, Spot and Option.

By category="linear", you can query USDT Perps, USDC Perps data occurred during classic account  
By category="spot", you can query Spot data occurred during classic account  
By category="option", you can query Options data occurred during classic account  
By category="inverse", you can query Inverse Contract data occurred during **classic account or[UTA1.0](/docs/v5/acct-mode#uta-10)**

info

USDC Perpeual & Option support the recent 6 months data. Please download older data via GUI

deprecate plan

category=spot will be deprecated by the end of Aug, 2026.

### HTTP Request

GET`/v5/pre-upgrade/execution/list`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
[category](/docs/v5/enum#category)| **true**|  string| Product type `linear`, `inverse`, `option`, `spot`  
symbol| false| string| Symbol name, like `BTCUSDT`, uppercase only  
orderId| false| string| Order ID  
orderLinkId| false| string| User customised order ID  
baseCoin| false| string| Base coin, uppercase only. Used for `option`  
startTime| false| integer| The start timestamp (ms) 

  * startTime and endTime are not passed, return 7 days by default
  * Only startTime is passed, return range between startTime and startTime+7 days
  * Only endTime is passed, return range between endTime-7 days and endTime
  * If both are passed, the rule is endTime - startTime <= 7 days

  
endTime| false| integer| The end timestamp (ms)  
[execType](/docs/v5/enum#exectype)| false| string| Execution type  
limit| false| integer| Limit for data size per page. [`1`, `100`]. Default: `50`  
cursor| false| string| Cursor. Use the `nextPageCursor` token from the response to retrieve the next page of the result set  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
category| string| Product type  
list| array| Object  
> symbol| string| Symbol name  
> orderId| string| Order ID  
> orderLinkId| string| User customized order ID  
> side| string| Side. `Buy`,`Sell`  
> orderPrice| string| Order price  
> orderQty| string| Order qty  
> leavesQty| string| The remaining qty not executed  
> [orderType](/docs/v5/enum#ordertype)| string| Order type. `Market`,`Limit`  
> [stopOrderType](/docs/v5/enum#stopordertype)| string| Stop order type. If the order is not stop order, any type is not returned  
> execFee| string| Executed trading fee  
> execId| string| Execution ID  
> execPrice| string| Execution price  
> execQty| string| Execution qty  
> [execType](/docs/v5/enum#exectype)| string| Executed type  
> execValue| string| Executed order value  
> execTime| string| Executed timestamp (ms)  
> isMaker| boolean| Is maker order. `true`: maker, `false`: taker  
> feeRate| string| Trading fee rate  
> tradeIv| string| Implied volatility  
> markIv| string| Implied volatility of mark price  
> markPrice| string| The mark price of the symbol when executing  
> indexPrice| string| The index price of the symbol when executing  
> underlyingPrice| string| The underlying price of the symbol when executing  
> blockTradeId| string| Paradigm block trade ID  
> closedSize| string| Closed position size  
nextPageCursor| string| Refer to the `cursor` request parameter  
  
### Request Example
    
    
    GET /v5/pre-upgrade/execution/list?category=linear&limit=1&execType=Funding&symbol=BTCUSDT HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1682580752432  
    X-BAPI-RECV-WINDOW: 5000  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "list": [  
                {  
                    "symbol": "BTCUSDT",  
                    "orderId": "1682553600-BTCUSDT-592334-Sell",  
                    "orderLinkId": "",  
                    "side": "Sell",  
                    "orderPrice": "0.00",  
                    "orderQty": "0.000",  
                    "leavesQty": "0.000",  
                    "orderType": "UNKNOWN",  
                    "stopOrderType": "UNKNOWN",  
                    "execFee": "0.6364003",  
                    "execId": "11f1c4ed-ff20-4d73-acb7-96e43a917f25",  
                    "execPrice": "28399.90",  
                    "execQty": "0.011",  
                    "execType": "Funding",  
                    "execValue": "312.3989",  
                    "execTime": "1682553600000",  
                    "isMaker": false,  
                    "feeRate": "0.00203714",  
                    "tradeIv": "",  
                    "markIv": "",  
                    "markPrice": "28399.90",  
                    "indexPrice": "",  
                    "underlyingPrice": "",  
                    "blockTradeId": "",  
                    "closedSize": "0.000"  
                }  
            ],  
            "nextPageCursor": "page_token%3D96184191%26",  
            "category": "linear"  
        },  
        "retExtInfo": {},  
        "time": 1682580752717  
    }

---

# 查詢升級前成交紀錄

支持查詢升級到統一帳戶之前發生的USDT永續, USDC永續, 反向合約, 現貨和期權, 返回結果按`execTime`降序排列

信息

  * USDC永續和期權僅支持查詢最近6個月的數據, 對於更老的數據, 請前往網頁端下載
  * 通過category=linear, 查詢到在經典帳戶期間產生的USDT永續, USDC永續數據  

  * 通過category=spot, 查詢到在經典帳戶期間產生的現貨數據  

  * 通過category=option, 查詢到在經典帳戶期間產生的期權數據  

  * 通過category=inverse, 查詢到在**經典帳戶或者[統一帳戶1.0](/docs/zh-TW/v5/acct-mode#%E7%B5%B1%E4%B8%80%E5%B8%B3%E6%88%B610)**期間產生的反向合約數據



下線計畫

現貨查詢（category=spot） 將會於2026年8月底下線，請前往網頁端下載歷史數據

### HTTP 請求

GET `v5/pre-upgrade/execution/list`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
[category](/docs/zh-TW/v5/enum#category)| **true**|  string| 產品類型 `linear`, `inverse`, `option`, `spot`  
symbol| false| string| 合約名稱  
orderId| false| string| 訂單ID  
orderLinkId| false| string| 用戶自定義訂單ID  
baseCoin| false| string| 交易幣種. 僅期權使用  
startTime| false| integer| 開始時間戳 (毫秒) 

  * startTime 和 endTime都不傳入, 則默認返回最近7天的數據
  * startTime 和 endTime都傳入的話, 則確保endTime - startTime <= 7天
  * 若只傳startTime，則查詢startTime和startTime+7天的數據
  * 若只傳endTime，則查詢endTime-7天和endTime的數據

  
endTime| false| integer| 結束時間戳 (毫秒)  
[execType](/docs/zh-TW/v5/enum#exectype)| false| string| 執行類型  
limit| false| integer| 每頁數量限制. [`1`, `100`]. 默認: `50`  
cursor| false| string| 游標，用於翻頁  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
[category](/docs/zh-TW/v5/enum#category)| string| 產品類型  
list| array| Object  
> symbol| string| 合約名稱  
> orderId| string| 訂單Id  
> orderLinkId| string| 用戶自定義訂單id  
> side| string| 訂單方向.買： `Buy`,賣：`Sell`  
> orderPrice| string| 訂單價格  
> orderQty| string| 訂單數量  
> leavesQty| string| 剩餘委託未成交數量  
> [orderType](/docs/zh-TW/v5/enum#ordertype)| string| 訂單類型. 市價單：`Market`,限價單：`Limit`  
> [stopOrderType](/docs/zh-TW/v5/enum#stopordertype)| string| 条件单的订单类型。如果该订单不是条件单，则不会返回任何类型  
> execFee| string| 交易手續費  
> execId| string| 成交Id  
> execPrice| string| 成交價格  
> execQty| string| 成交數量  
> [execType](/docs/zh-TW/v5/enum#exectype)| string| 交易類型  
> execValue| string| 成交價值  
> execTime| string| 成交時間（毫秒）  
> isMaker| Bool| 是否是 Maker 訂單,`true` 為 maker 訂單，`false` 為 taker 訂單  
> feeRate| string| 手續費率  
> tradeIv| string| 隱含波動率，僅期權有效  
> markIv| string| 標記價格的隱含波動率，僅期權有效  
> markPrice| string| 成交執行時，該 symbol 當時的標記價格  
> indexPrice| string| 成交執行時，該 symbol 當時的指數價格，目前僅對期權業務有效  
> underlyingPrice| string| 成交執行時，該 symbol 當時的底層資產價格，僅期權有效  
> blockTradeId| string| 大宗交易的订单 ID ，使用 paradigm 进行大宗交易时生成的 ID  
> closedSize| string| 平倉數量  
nextPageCursor| string| 游標，用於翻頁  
  
### Request Example
    
    
    GET /v5/pre-upgrade/execution/list?category=linear&limit=1&execType=Funding&symbol=BTCUSDT HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1682580752432  
    X-BAPI-RECV-WINDOW: 5000  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "list": [  
                {  
                    "symbol": "BTCUSDT",  
                    "orderId": "1682553600-BTCUSDT-592334-Sell",  
                    "orderLinkId": "",  
                    "side": "Sell",  
                    "orderPrice": "0.00",  
                    "orderQty": "0.000",  
                    "leavesQty": "0.000",  
                    "orderType": "UNKNOWN",  
                    "stopOrderType": "UNKNOWN",  
                    "execFee": "0.6364003",  
                    "execId": "11f1c4ed-ff20-4d73-acb7-96e43a917f25",  
                    "execPrice": "28399.90",  
                    "execQty": "0.011",  
                    "execType": "Funding",  
                    "execValue": "312.3989",  
                    "execTime": "1682553600000",  
                    "isMaker": false,  
                    "feeRate": "0.00203714",  
                    "tradeIv": "",  
                    "markIv": "",  
                    "markPrice": "28399.90",  
                    "indexPrice": "",  
                    "underlyingPrice": "",  
                    "blockTradeId": "",  
                    "closedSize": "0.000"  
                }  
            ],  
            "nextPageCursor": "page_token%3D96184191%26",  
            "category": "linear"  
        },  
        "retExtInfo": {},  
        "time": 1682580752717  
    }