---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/spot-margin-uta/fixedborrow-order-info
api_type: REST
updated_at: 2026-06-30 19:30:48.810966
---

# Get Fixed-Rate Borrow Order Quote

### HTTP Request

GET`/v5/spot-margin-trade/fixedborrow-order-quote`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
orderCurrency| **true**|  string| Coin name  
term| false| string| Fixed term. `7`: 7 days; `14`: 14 days; `30`: 30 days; `90`: 90 days; `180`: 180 days  
orderBy| false| string| Sort field. `apy`: annual rate; `term`: term; `quantity`: quantity  
sort| false| integer| Sort direction. `0`: ascending (default); `1`: descending  
limit| false| integer| Limit for data size per page. [1, 100]. Default: `10`  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array| Object  
> orderCurrency| string| Coin name  
> term| integer| Fixed term. `7`: 7 days; `14`: 14 days; `30`: 30 days; `90`: 90 days; `180`: 180 days  
> annualRate| string| Annual rate  
> qty| string| Quantity  
  
* * *

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/spot-margin-trade/fixedborrow-order-quote?orderCurrency=ETH&orderBy=apy&limit=10 HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1692696840996  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.spot_margin_trade_get_fixed_borrow_order_quote(  
        orderCurrency="ETH",  
        orderBy="apy",  
        limit=10  
    ))  
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "list": [  
                {  
                    "orderCurrency": "ETH",  
                    "term": 30,  
                    "annualRate": "0.026",  
                    "qty": "0.1"  
                },  
                {  
                    "orderCurrency": "ETH",  
                    "term": 60,  
                    "annualRate": "0.033",  
                    "qty": "0.1"  
                },  
                {  
                    "orderCurrency": "ETH",  
                    "term": 90,  
                    "annualRate": "0.038",  
                    "qty": "0.1"  
                },  
                {  
                    "orderCurrency": "ETH",  
                    "term": 30,  
                    "annualRate": "0.1",  
                    "qty": "0.6"  
                },  
                {  
                    "orderCurrency": "ETH",  
                    "term": 60,  
                    "annualRate": "0.1",  
                    "qty": "0.1"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1775617874744  
    }

---

# 查詢固定利率借款掛單報價

### HTTP 請求

GET`/v5/spot-margin-trade/fixedborrow-order-quote`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
orderCurrency| **true**|  string| 幣種名稱  
term| false| string| 借款期限。`7`：7天；`14`：14天；`30`：30天；`90`：90天；`180`：180天  
orderBy| false| string| 排序字段。`apy`：年化利率；`term`：期限；`quantity`：數量  
sort| false| integer| 排序方向。`0`：升序（默認）；`1`：降序  
limit| false| integer| 每頁返回數量，[1, 100]，默認：`10`  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
list| array| Object  
> orderCurrency| string| 幣種名稱  
> term| integer| 借款期限。`7`：7天；`14`：14天；`30`：30天；`90`：90天；`180`：180天  
> annualRate| string| 年化利率  
> qty| string| 數量  
  
* * *

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/spot-margin-trade/fixedborrow-order-quote?orderCurrency=ETH&orderBy=apy&limit=10 HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1692696840996  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
      
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "list": [  
                {  
                    "orderCurrency": "ETH",  
                    "term": 30,  
                    "annualRate": "0.026",  
                    "qty": "0.1"  
                },  
                {  
                    "orderCurrency": "ETH",  
                    "term": 60,  
                    "annualRate": "0.033",  
                    "qty": "0.1"  
                },  
                {  
                    "orderCurrency": "ETH",  
                    "term": 90,  
                    "annualRate": "0.038",  
                    "qty": "0.1"  
                },  
                {  
                    "orderCurrency": "ETH",  
                    "term": 30,  
                    "annualRate": "0.1",  
                    "qty": "0.6"  
                },  
                {  
                    "orderCurrency": "ETH",  
                    "term": 60,  
                    "annualRate": "0.1",  
                    "qty": "0.1"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1775617874744  
    }