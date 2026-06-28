---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/earn/easy-onchain/product-info
api_type: REST
updated_at: 2026-05-27 19:17:31.683450
---

# Get Order List

API ker permission: `Earn`  
API rate limit: 10 reqs / sec

info

  * Pass `orderId` alone to retrieve a single order. Omit to query the full order list with optional filters.
  * For `Stake` orders, `startTime`/`endTime` filters on order creation time. For `Redeem` orders, filters are applied on settlement time.
  * When `productId` is passed, `category` is required.



### HTTP Request

GET`/v5/earn/fixed-term/order`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
orderType| false| string| Filter by order type: `Stake`, `Redeem`, `Reinvest`. Returns all types if omitted  
productId| false| string| Filter by product ID. Requires `category` when passed  
category| false| string| Product sub-type: `FixedTermSaving`, `FundPool`, `FundPoolPremium`. Required when `productId` is passed  
orderId| false| string| System order ID for single order lookup  
startTime| false| integer| Start timestamp in ms  
endTime| false| integer| End timestamp in ms  
limit| false| integer| Number of items per page. Default: `20`, Max: `50`  
cursor| false| string| Pagination cursor. Use `nextPageCursor` from the previous response  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array| Order list  
> orderId| string| System-generated order ID  
> orderLinkId| string| User-customised idempotent ID  
> orderType| string| Order type: `Stake`, `Redeem`, `Reinvest`  
> status| string| Order status: `Processing`, `Active`, `Complete`, `Failed`  
> productId| string| Product ID  
> category| string| Product sub-type: `FixedTermSaving`, `FundPool`, `FundPoolPremium`  
> coin| string| Coin  
> amount| string| Order amount  
> duration| string| Fixed term duration, e.g. `1d`, `8h`, `2m`  
> accountType| string| Account type: `FUND`, `UNIFIED`. Redeem orders always show `FUND`  
> settlementTime| string| Settlement time, unix timestamp in ms  
> createdAt| string| Order creation time, unix timestamp in ms  
> yieldInfoList| array| Yield info list. Populated after settlement  
>> coin| string| Yield coin  
>> amount| string| Yield amount  
>> status| string| Yield status: `Pending`, `Distributed`, `Fail`, `ReinvestSuccess`  
>> createdAt| string| Yield record creation time, unix timestamp in ms  
>> apy| string| APY applied for this yield  
nextPageCursor| string| Cursor for the next page. Empty string means no more data  
  
* * *

### Request Example
    
    
    GET /v5/earn/fixed-term/order?productId=546&category=FixedTermSaving HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1741651200000  
    X-BAPI-RECV-WINDOW: 5000  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "list": [  
                {  
                    "orderId": "6f2530d6-46b9-41f9-880a-4addbd152398",  
                    "orderLinkId": "",  
                    "orderType": "Redeem",  
                    "status": "Complete",  
                    "productId": "546",  
                    "category": "FixedTermSaving",  
                    "coin": "USDT",  
                    "amount": "100.056",  
                    "duration": "1d",  
                    "accountType": "UNIFIED",  
                    "settlementTime": "1750811400000",  
                    "createdAt": "1750648976000",  
                    "yieldInfoList": [  
                        {  
                            "coin": "USDT",  
                            "amount": "0.0063",  
                            "status": "Distributed",  
                            "createdAt": "1750811401000",  
                            "apy": "2.33%"  
                        }  
                    ]  
                }  
            ],  
            "nextPageCursor": ""  
        },  
        "retExtInfo": {},  
        "time": 1776070828622  
    }

---

# 取得訂單列表

API key權限：`Earn`  
API 頻率限制：每秒10次

信息

  * 單獨傳入 `orderId` 可查詢單筆訂單；省略則搭配可選過濾條件查詢完整訂單列表。
  * `Stake` 訂單的 `startTime`/`endTime` 按訂單創建時間過濾；`Redeem` 訂單則按結算時間過濾。
  * 傳入 `productId` 時，`category` 為必填項。



### HTTP 請求

GET`/v5/earn/fixed-term/order`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
orderType| false| string| 依訂單類型篩選：`Stake`、`Redeem`、`Reinvest`。若省略則返回所有類型  
productId| false| string| 依產品ID篩選。傳入時需要 `category`  
category| false| string| 產品子類型：`FixedTermSaving`、`FundPool`、`FundPoolPremium`。傳入 `productId` 時必填  
orderId| false| string| 系統訂單ID，用於單筆訂單查詢  
startTime| false| integer| 開始時間戳（毫秒）  
endTime| false| integer| 結束時間戳（毫秒）  
limit| false| integer| 每頁數量。預設：`20`，最大：`50`  
cursor| false| string| 分頁游標。使用上次響應中的 `nextPageCursor`  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
list| array| 訂單列表  
> orderId| string| 系統生成的訂單ID  
> orderLinkId| string| 用戶自訂冪等ID  
> orderType| string| 訂單類型：`Stake`、`Redeem`、`Reinvest`  
> status| string| 訂單狀態：`Processing`、`Active`、`Complete`、`Failed`  
> productId| string| 產品ID  
> category| string| 產品子類型：`FixedTermSaving`、`FundPool`、`FundPoolPremium`  
> coin| string| 幣種  
> amount| string| 訂單金額  
> duration| string| 固定期限，例如 `1d`、`8h`、`2m`  
> accountType| string| 帳戶類型：`FUND`、`UNIFIED`。贖回訂單始終顯示 `FUND`  
> settlementTime| string| 結算時間，毫秒級unix時間戳  
> createdAt| string| 訂單創建時間，毫秒級unix時間戳  
> yieldInfoList| array| 收益資訊列表，結算後填充  
>> coin| string| 收益幣種  
>> amount| string| 收益金額  
>> status| string| 收益狀態：`Pending`、`Distributed`、`Fail`、`ReinvestSuccess`  
>> createdAt| string| 收益記錄創建時間，毫秒級unix時間戳  
>> apy| string| 此收益適用的APY  
nextPageCursor| string| 下一頁游標。空字符串表示無更多數據  
  
* * *

### 請求示例
    
    
    GET /v5/earn/fixed-term/order?productId=546&category=FixedTermSaving HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1741651200000  
    X-BAPI-RECV-WINDOW: 5000  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "list": [  
                {  
                    "orderId": "6f2530d6-46b9-41f9-880a-4addbd152398",  
                    "orderLinkId": "",  
                    "orderType": "Redeem",  
                    "status": "Complete",  
                    "productId": "546",  
                    "category": "FixedTermSaving",  
                    "coin": "USDT",  
                    "amount": "100.056",  
                    "duration": "1d",  
                    "accountType": "UNIFIED",  
                    "settlementTime": "1750811400000",  
                    "createdAt": "1750648976000",  
                    "yieldInfoList": [  
                        {  
                            "coin": "USDT",  
                            "amount": "0.0063",  
                            "status": "Distributed",  
                            "createdAt": "1750811401000",  
                            "apy": "2.33%"  
                        }  
                    ]  
                }  
            ],  
            "nextPageCursor": ""  
        },  
        "retExtInfo": {},  
        "time": 1776070828622  
    }