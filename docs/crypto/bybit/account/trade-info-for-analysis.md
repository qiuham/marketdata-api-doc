---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/account/trade-info-for-analysis
api_type: Account
updated_at: 2026-11-13 19:20:57.892718
---

# Get Trade Info For Analysis

Query aggregated **spot trade** analysis data for a symbol, including execution values, quantities, fees, and daily breakdown.

### HTTP Request

GET`/v5/account/trade-info-for-analysis`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
symbol| **true**|  string| Symbol name, e.g. `BTCUSDT`, `ETHUSDT`  
startTime| false| long| Query start time (ms)  
endTime| false| long| Query end time (ms)  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
symbolRnl| string| Symbol realised P&L  
netExecQty| string| Net execution quantity  
sumExecValue| string| Total execution value  
sumExecQty| string| Total execution quantity  
avgBuyExecPrice| string| Average buy execution price  
sumBuyExecValue| string| Total buy execution value  
sumBuyExecQty| string| Total buy execution quantity  
sumBuyExecFee| string| Total buy execution fee  
sumBuyOrderQty| string| Total buy order quantity  
avgSellExecPrice| string| Average sell execution price  
sumSellExecValue| string| Total sell execution value  
sumSellExecQty| string| Total sell execution quantity  
sumSellExecFee| string| Total sell execution fee  
sumSellOrderQty| string| Total sell order quantity  
maxMarginVersion| integer| Max margin version number  
baseCoin| string| Base coin  
settleCoin| string| Settle coin  
sumPriceList| array<object>| Daily aggregated price list  
> day| string| Date  
> sumBuyExecValue| string| Daily total buy execution value  
> sumSellExecValue| string| Daily total sell execution value  
> sumExecValue| string| Daily total execution value  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/account/trade-info-for-analysis?symbol=ETHUSDT HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1773230920000  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
      
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "Success",  
        "result": {  
            "symbolRnl": "0",  
            "sumBuyExecValue": "0",  
            "sumBuyExecQty": "0",  
            "sumSellExecFee": "0",  
            "netExecQty": "0",  
            "sumExecQty": "0",  
            "settleCoin": "USDT",  
            "sumExecValue": "0",  
            "sumSellExecValue": "0",  
            "sumBuyOrderQty": "0",  
            "sumSellOrderQty": "0",  
            "maxMarginVersion": 0,  
            "avgSellExecPrice": "0",  
            "avgBuyExecPrice": "0",  
            "sumBuyExecFee": "0",  
            "sumSellExecQty": "0",  
            "baseCoin": "ETH"  
        },  
        "retExtInfo": {},  
        "time": 1773230927308  
    }

---

# 查詢交易分析信息

查詢指定交易對的**現貨交易** 分析數據，包括成交金額、數量、手續費及每日明細。

### HTTP 請求

GET`/v5/account/trade-info-for-analysis`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
symbol| **true**|  string| 交易對，如 `BTCUSDT`、`ETHUSDT`  
startTime| false| long| 查詢開始時間（毫秒時間戳）  
endTime| false| long| 查詢結束時間（毫秒時間戳）  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
symbolRnl| string| 交易對已實現盈虧  
netExecQty| string| 淨成交數量  
sumExecValue| string| 總成交金額  
sumExecQty| string| 總成交數量  
avgBuyExecPrice| string| 平均買入成交價  
sumBuyExecValue| string| 買入總成交金額  
sumBuyExecQty| string| 買入總成交數量  
sumBuyExecFee| string| 買入總手續費  
sumBuyOrderQty| string| 買入總委託數量  
avgSellExecPrice| string| 平均賣出成交價  
sumSellExecValue| string| 賣出總成交金額  
sumSellExecQty| string| 賣出總成交數量  
sumSellExecFee| string| 賣出總手續費  
sumSellOrderQty| string| 賣出總委託數量  
maxMarginVersion| integer| 最大保證金版本號  
baseCoin| string| 基礎幣種  
settleCoin| string| 結算幣種  
sumPriceList| array<object>| 每日匯總價格列表  
> day| string| 日期  
> sumBuyExecValue| string| 當日買入總成交金額  
> sumSellExecValue| string| 當日賣出總成交金額  
> sumExecValue| string| 當日總成交金額  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/account/trade-info-for-analysis?symbol=ETHUSDT HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1773230920000  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
      
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "Success",  
        "result": {  
            "symbolRnl": "0",  
            "sumBuyExecValue": "0",  
            "sumBuyExecQty": "0",  
            "sumSellExecFee": "0",  
            "netExecQty": "0",  
            "sumExecQty": "0",  
            "settleCoin": "USDT",  
            "sumExecValue": "0",  
            "sumSellExecValue": "0",  
            "sumBuyOrderQty": "0",  
            "sumSellOrderQty": "0",  
            "maxMarginVersion": 0,  
            "avgSellExecPrice": "0",  
            "avgBuyExecPrice": "0",  
            "sumBuyExecFee": "0",  
            "sumSellExecQty": "0",  
            "baseCoin": "ETH"  
        },  
        "retExtInfo": {},  
        "time": 1773230927308  
    }