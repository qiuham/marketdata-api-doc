---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/market/corporate-action
api_type: Market Data
updated_at: 2026-11-13 19:23:47.411780
---

# Query Corporate Action

Query current corporate actions for TradFi options, including forward splits, reverse splits, and dividends.

Corporate actions are retained for 14 days and are returned in descending order of `effectiveTime`.

> **Covers: TradFi Options**

### HTTP Request

GET`/v5/market/corporate-action`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
category| false| string| Product category. `option`  
baseCoin| false| string| Underlying asset ticker, such as `AAPL`  
actionType| false| string| Corporate action type. `ForwardSplit`, `ReverseSplit`, or `Dividend`  
limit| false| integer| Limit for data size per page  
cursor| false| string| Cursor. Use the `nextPageCursor` token from the response to retrieve the next page of results  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
nextPageCursor| string| Cursor for the next page  
list| array| List of corporate action records  
> category| string| Product category  
> symbol| string| Symbol name, such as `NVDAUSDT`  
> baseCoin| string| Underlying asset ticker, such as `NVDA`  
> actionType| string| Corporate action type. `ForwardSplit`, `ReverseSplit`, or `Dividend`  
> status| string| Corporate action status  
> effectiveTime| integer| Effective timestamp (ms)  
> details| object| Corporate-action-specific details. See the applicable action type below  
>> splitFactor| string| Split factor. Only returned for forward or reverse splits  
>> splitType| string| Split direction: `FORWARD` or `REVERSE`. Only returned for splits  
>> dividendAmountPerShare| string| Dividend amount per share. Only returned for dividends  
>> dividendCurrency| string| Currency of `dividendAmountPerShare`. Only returned for dividends  
>> installmentCount| integer| Number of dividend installments. Only returned for dividends  
>> installmentAmountPerShare| string| Dividend amount per share in each installment. Only returned for dividends  
>> installmentCoin| string| Settlement coin for the installment. Only returned for dividends  
>> firstSettlementTimeUtc| integer| First dividend installment settlement timestamp (ms). Only returned for dividends  
>> installments| array| Dividend installment details. Only returned for dividends  
>>> installmentNo| integer| Installment sequence number  
>>> settlementTimeUtc| integer| Installment settlement timestamp (ms)  
>>> status| string| Installment status  
  
For forward and reverse splits in `PROCESSING` status, `effectiveTime` is `limitStartTime`. For dividends in `PROCESSING` status, it is `firstSettlementTimeUtc`.

* * *

### Request Example

  * HTTP
  * Python


    
    
    GET /v5/market/corporate-action?category=option&baseCoin=AAPL HTTP/1.1  
    Host: api-testnet.bybit.com  
    
    
    
    from pybit.unified_trading import HTTP  
      
    session = HTTP(testnet=True)  
    print(session.get_corporate_action(  
        category="option",  
        baseCoin="AAPL",  
    ))  
    

### Response Example

**Forward split or reverse split**
    
    
    {  
      "retCode": 0,  
      "retMsg": "OK",  
      "result": {  
        "list": [  
          {  
            "category": "option",  
            "symbol": "AAPLUSDT",  
            "baseCoin": "AAPL",  
            "actionType": "ForwardSplit",  
            "status": "Completed",  
            "effectiveTime": 1788278400000,  
            "details": {  
              "splitFactor": "4",  
              "splitType": "FORWARD"  
            }  
          }  
        ],  
        "nextPageCursor": ""  
      },  
      "retExtInfo": {},  
      "time": 1788300000000  
    }  
    

**Dividend**
    
    
    {  
      "retCode": 0,  
      "retMsg": "OK",  
      "result": {  
        "list": [  
          {  
            "symbol": "AAPLUSDT",  
            "baseCoin": "AAPL",  
            "actionType": "Dividend",  
            "status": "Announced",  
            "effectiveTime": 1788278400000,  
            "details": {  
              "dividendAmountPerShare": "0.25",  
              "dividendCurrency": "USD",  
              "installmentCount": 4,  
              "installmentAmountPerShare": "5.00000",  
              "installmentCoin": "USDT",  
              "firstSettlementTimeUtc": 1788134400000,  
              "installments": [  
                {  
                  "installmentNo": 1,  
                  "settlementTimeUtc": 1788134400000,  
                  "status": "SUCCESS"  
                },  
                {  
                  "installmentNo": 2,  
                  "settlementTimeUtc": 1788138000000,  
                  "status": "WAITING"  
                },  
                {  
                  "installmentNo": 3,  
                  "settlementTimeUtc": 1788141600000,  
                  "status": "WAITING"  
                },  
                {  
                  "installmentNo": 4,  
                  "settlementTimeUtc": 1788145200000,  
                  "status": "WAITING"  
                }  
              ]  
            }  
          }  
        ],  
        "nextPageCursor": ""  
      },  
      "retExtInfo": {},  
      "time": 1788300000000  
    }

---

# 查詢公司行動

查詢 TradFi 期權目前的公司行動，包含正向拆股、反向拆股及股息。

公司行動資料保留 14 天，並依 `effectiveTime` 由新到舊排序返回。

> **覆蓋範圍: TradFi 期權**

### HTTP 請求

GET`/v5/market/corporate-action`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
category| false| string| 產品類型。`option`  
baseCoin| false| string| 標的資產代碼，例如 `AAPL`  
actionType| false| string| 公司行動類型：`ForwardSplit`、`ReverseSplit` 或 `Dividend`  
limit| false| integer| 每頁返回的資料筆數限制  
cursor| false| string| 遊標。使用響應中的 `nextPageCursor` 取得下一頁資料  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
nextPageCursor| string| 下一頁遊標  
list| array| 公司行動記錄列表  
> category| string| 產品類型  
> symbol| string| 交易對名稱，例如 `NVDAUSDT`  
> baseCoin| string| 標的資產代碼，例如 `NVDA`  
> actionType| string| 公司行動類型：`ForwardSplit`、`ReverseSplit` 或 `Dividend`  
> status| string| 公司行動狀態  
> effectiveTime| integer| 生效時間戳（毫秒）  
> details| object| 公司行動專屬詳情。請參閱下方各行動類型欄位  
>> splitFactor| string| 拆股比例。僅拆股或合股時返回  
>> splitType| string| 拆股方向：`FORWARD` 或 `REVERSE`。僅拆股或合股時返回  
>> dividendAmountPerShare| string| 每股股息金額。僅股息時返回  
>> dividendCurrency| string| `dividendAmountPerShare` 的幣種。僅股息時返回  
>> installmentCount| integer| 股息分期數。僅股息時返回  
>> installmentAmountPerShare| string| 每期每股股息金額。僅股息時返回  
>> installmentCoin| string| 分期結算幣種。僅股息時返回  
>> firstSettlementTimeUtc| integer| 首期股息結算時間戳（毫秒）。僅股息時返回  
>> installments| array| 股息分期詳情。僅股息時返回  
>>> installmentNo| integer| 分期序號  
>>> settlementTimeUtc| integer| 分期結算時間戳（毫秒）  
>>> status| string| 分期狀態  
  
當拆股或合股的狀態為 `PROCESSING` 時，`effectiveTime` 取 `limitStartTime`。當股息的狀態為 `PROCESSING` 時，`effectiveTime` 取 `firstSettlementTimeUtc`。

* * *

### 請求示例

  * HTTP


    
    
    GET /v5/market/corporate-action?category=option&baseCoin=AAPL HTTP/1.1  
    Host: api-testnet.bybit.com  
    

### 響應示例

**正向拆股或反向拆股**
    
    
    {  
      "retCode": 0,  
      "retMsg": "OK",  
      "result": {  
        "list": [  
          {  
            "category": "option",  
            "symbol": "AAPLUSDT",  
            "baseCoin": "AAPL",  
            "actionType": "ForwardSplit",  
            "status": "Completed",  
            "effectiveTime": 1788278400000,  
            "details": {  
              "splitFactor": "4",  
              "splitType": "FORWARD"  
            }  
          }  
        ],  
        "nextPageCursor": ""  
      },  
      "retExtInfo": {},  
      "time": 1788300000000  
    }  
    

**股息**
    
    
    {  
      "retCode": 0,  
      "retMsg": "OK",  
      "result": {  
        "list": [  
          {  
            "symbol": "AAPLUSDT",  
            "baseCoin": "AAPL",  
            "actionType": "Dividend",  
            "status": "Announced",  
            "effectiveTime": 1788278400000,  
            "details": {  
              "dividendAmountPerShare": "0.25",  
              "dividendCurrency": "USD",  
              "installmentCount": 4,  
              "installmentAmountPerShare": "5.00000",  
              "installmentCoin": "USDT",  
              "firstSettlementTimeUtc": 1788134400000,  
              "installments": [  
                {  
                  "installmentNo": 1,  
                  "settlementTimeUtc": 1788134400000,  
                  "status": "SUCCESS"  
                },  
                {  
                  "installmentNo": 2,  
                  "settlementTimeUtc": 1788138000000,  
                  "status": "WAITING"  
                },  
                {  
                  "installmentNo": 3,  
                  "settlementTimeUtc": 1788141600000,  
                  "status": "WAITING"  
                },  
                {  
                  "installmentNo": 4,  
                  "settlementTimeUtc": 1788145200000,  
                  "status": "WAITING"  
                }  
              ]  
            }  
          }  
        ],  
        "nextPageCursor": ""  
      },  
      "retExtInfo": {},  
      "time": 1788300000000  
    }