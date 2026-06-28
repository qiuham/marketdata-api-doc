---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/position/trading-stop
api_type: Position
updated_at: 2026-05-27 19:21:16.258558
---

# Get Pre-upgrade Delivery Record

Query delivery records of Options before you upgraded the account to a Unified account, sorted by `deliveryTime` in descending order

info

  * By `category`="option", you can query Options delivery data occurred during classic account
  * Supports the recent 6 months Options delivery data. Please download older data via GUI



### HTTP Request

GET`/v5/pre-upgrade/asset/delivery-record`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
[category](/docs/v5/enum#category)| **true**|  string| Product type `option`  
symbol| false| string| Symbol name, uppercase only  
expDate| false| string| Expiry date. `25MAR22`. Default: return all  
limit| false| integer| Limit for data size per page. [`1`, `50`]. Default: `20`  
cursor| false| string| Cursor. Used for pagination  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
category| string| Product type  
list| array| Object  
> deliveryTime| number| Delivery time (ms)  
> symbol| string| Symbol name  
> side| string| `Buy`,`Sell`  
> position| string| Executed size  
> deliveryPrice| string| Delivery price  
> strike| string| Exercise price  
> fee| string| Trading fee  
> deliveryRpl| string| Realized PnL of the delivery  
nextPageCursor| string| Cursor. Used for pagination  
  
### Request Example

  * HTTP
  * Python


    
    
    GET /v5/pre-upgrade/asset/delivery-record?category=option HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1686809005774  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "nextPageCursor": "21%3A0%2C21%3A0",  
            "category": "option",  
            "list": [  
                {  
                    "symbol": "ETH-14JUN23-1750-C",  
                    "side": "Buy",  
                    "deliveryTime": 1686729604507,  
                    "strike": "1750",  
                    "fee": "0",  
                    "position": "0.5",  
                    "deliveryPrice": "1740.25036667",  
                    "deliveryRpl": "0.175"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1686796328492  
    }

---

# 查詢升級前期權交割紀錄

查詢升級到統一帳戶之前發生的期權的交割紀錄, 返回結果按照`deliveryTime`降序排列

信息

  * 僅支持查詢最近6個月的數據, 對於更老的數據, 請前往網頁端下載
  * 查詢到在經典帳戶期間產生的期權交割數據



### HTTP 請求

GET`/v5/pre-upgrade/asset/delivery-record`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
[category](/docs/zh-TW/v5/enum#category)| **true**|  string| 產品類型. `option`  
symbol| false| string| 合約名稱  
expDate| false| string| 過期日. 格式示例: `25MAR22`. 默認: 返回所有日期數據  
limit| false| integer| 每頁數量限制. [`1`, `50`]. 默認: `20`  
cursor| false| string| 游標，用於翻頁  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
category| string| 產品類型  
list| array| Object  
> deliveryTime| number| 交割時間戳 (毫秒)  
> symbol| string| 合約名稱  
> side| string| `Buy`,`Sell`  
> position| string| 交割數量  
> deliveryPrice| string| 交割價格  
> strike| string| 行權價  
> fee| string| 手續費，正數表支出，負數表收取  
> deliveryRpl| string| 交割已實現盈虧  
nextPageCursor| string| 游標，用於翻頁  
  
### 請求示例

  * HTTP
  * Python


    
    
    GET /v5/pre-upgrade/asset/delivery-record?category=option HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1686809005774  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "nextPageCursor": "21%3A0%2C21%3A0",  
            "category": "option",  
            "list": [  
                {  
                    "symbol": "ETH-14JUN23-1750-C",  
                    "side": "Buy",  
                    "deliveryTime": 1686729604507,  
                    "strike": "1750",  
                    "fee": "0",  
                    "position": "0.5",  
                    "deliveryPrice": "1740.25036667",  
                    "deliveryRpl": "0.175"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1686796328492  
    }