---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/market/history-fund-rate
api_type: Market Data
updated_at: 2026-10-29 18:39:14.646041
---

# Get Instrument Summary

Query summary information and trading increments for linear and option instruments.

### HTTP Request

GET`/v5/market/instrument-summary`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
[category](/docs/v5/enum#category)| **true**|  string| Product type. `linear`, `option`  
symbol| false| string| Symbol name  
[symbolType](/docs/v5/enum#symboltype)| false| string| Instrument type  
marketRegion| false| string| Market region: `HK`, `US`, `CN`, `KR`, etc.  
baseCoin| false| string| Base coin, e.g. `NVDA`, `TSLA`  
limit| false| integer| Limit for data size per page. [`1`, `1000`]. Default: `500`  
cursor| false| string| Cursor. Use the `nextPageCursor` token from the response to retrieve the next page of the result set  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
category| string| Product type  
nextPageCursor| string| Cursor for the next page  
list| array| Object  
> symbol| string| Symbol name  
> symbolType| string| Instrument type  
> displayName| string| Display name shown in the UI  
> baseCoin| string| Base coin  
> settleCoin| string| Settlement coin  
> fullName| string| Full name. Returns an empty string for `option`  
> marketRegion| string| Market region of the underlying asset, used to determine its trading calendar and market hours. `US`: United States; `CN`: Mainland China; `HK`: Hong Kong; `KR`: South Korea. Returns an empty string for `option` or when not applicable  
> underlyingTicker| string| Stock ticker, security code, or asset symbol in the underlying asset's native market. Returns an empty string for `option`  
> priceIndex| string| The corresponding TradFi perpetual symbol used as the price index; for example, NVDA options use `NVDAUSDT`. Returns an empty string for `linear`  
> qtyStep| string| Quantity step  
> tickSize| string| Price tick size  
> deliveryTime| string| Delivery timestamp (ms). Returns `0` for `linear`  
  
### Request Example

  * HTTP


    
    
    GET /v5/market/instrument-summary?category=linear HTTP/1.1  
    Host: api.bybit.com  
    

### Response Example
    
    
    {  
      "retCode": 0,  
      "retMsg": "OK",  
      "result": {  
        "category": "linear",  
        "list": [  
          {  
            "symbol": "0GUSDT",  
            "symbolType": "",  
            "displayName": "0GUSDT",  
            "baseCoin": "0G",  
            "settleCoin": "USDT",  
            "fullName": "0G",  
            "marketRegion": "",  
            "underlyingTicker": "",  
            "qtyStep": "0.1",  
            "tickSize": "0.0001",  
            "priceIndex": "",  
            "deliveryTime": "0"  
          }  
        ],  
        "nextPageCursor": "first%3D0GUSDT%26last%3DMYXUSDT"  
      },  
      "retExtInfo": {},  
      "time": 1791944863432  
    }

---

# 查詢交易對摘要

查詢線性合約與期權交易對的摘要資訊及交易精度。

### HTTP 請求

GET`/v5/market/instrument-summary`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
[category](/docs/zh-TW/v5/enum#category)| **true**|  string| 產品類型：`linear`、`option`  
symbol| false| string| 交易對名稱  
[symbolType](/docs/zh-TW/v5/enum#symboltype)| false| string| 交易對類型  
marketRegion| false| string| 市場區域：`HK`、`US`、`CN`、`KR` 等  
baseCoin| false| string| 基礎幣種，例如 `NVDA`、`TSLA`  
limit| false| integer| 每頁資料筆數。[`1`, `1000`]。預設：`500`  
cursor| false| string| 游標。使用響應中的 `nextPageCursor` 取得下一頁  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
category| string| 產品類型  
nextPageCursor| string| 下一頁游標  
list| array| 物件  
> symbol| string| 交易對名稱  
> symbolType| string| 交易對類型  
> displayName| string| 與 UI 一致的顯示名稱  
> baseCoin| string| 基礎幣種  
> settleCoin| string| 結算幣種  
> fullName| string| 完整名稱。`option` 時返回空字串  
> marketRegion| string| 標的資產所屬的市場區域，用於判斷其交易日曆與市場交易時段。`US`：美國市場；`CN`：中國大陸市場；`HK`：香港市場；`KR`：韓國市場。`option` 或不適用時返回空字串  
> underlyingTicker| string| 標的資產在其原生市場中的股票代號、證券代碼或資產符號。`option` 時返回空字串  
> priceIndex| string| 對應的 TradFi 永續合約價格指數；例如 NVDA 期權對應 `NVDAUSDT`。`linear` 時返回空字串  
> qtyStep| string| 數量步長  
> tickSize| string| 價格最小變動單位  
> deliveryTime| string| 交割時間戳（毫秒）。`linear` 時返回 `0`  
  
### 請求示例

  * HTTP


    
    
    GET /v5/market/instrument-summary?category=linear HTTP/1.1  
    Host: api.bybit.com  
    

### 響應示例
    
    
    {  
      "retCode": 0,  
      "retMsg": "OK",  
      "result": {  
        "category": "linear",  
        "list": [  
          {  
            "symbol": "0GUSDT",  
            "symbolType": "",  
            "displayName": "0GUSDT",  
            "baseCoin": "0G",  
            "settleCoin": "USDT",  
            "fullName": "0G",  
            "marketRegion": "",  
            "underlyingTicker": "",  
            "qtyStep": "0.1",  
            "tickSize": "0.0001",  
            "priceIndex": "",  
            "deliveryTime": "0"  
          }  
        ],  
        "nextPageCursor": "first%3D0GUSDT%26last%3DMYXUSDT"  
      },  
      "retExtInfo": {},  
      "time": 1791944863432  
    }