---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/earn/byusdt/yield
api_type: REST
updated_at: 2026-11-13 18:27:38.192578
---

# Get APR History

info

Does not need authentication.

note

You can query up to 6 months of historical APR data.

### HTTP Request

GET`/v5/earn/apr-history`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
category| **true**|  string| `FlexibleSaving`,`OnChain`  
productId| **true**|  string| Product ID, from [GET /v5/earn/product](/docs/v5/finance/earn/easy-onchain/product-info)  
startTime| false| integer| Start timestamp (ms). If neither `startTime` nor `endTime` is provided, the last 7 days of data is returned by default  
endTime| false| integer| End timestamp (ms). The difference between `endTime` and `startTime` must be less than or equal to 182 days  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array| Object  
> timestamp| string| Unix timestamp (ms) at midnight of the corresponding date  
> apr| string| APR, decimal string, e.g., `"0.055"` represents 5.5%  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/earn/apr-history?productId=8&category=OnChain HTTP/1.1  
    Host: api-testnet.bybit.com  
    
    
    
      
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "list": [  
                {  
                    "timestamp": "1773705600000",  
                    "apr": "15%"  
                },  
                {  
                    "timestamp": "1773619200000",  
                    "apr": "15%"  
                },  
                {  
                    "timestamp": "1773532800000",  
                    "apr": "15%"  
                },  
                {  
                    "timestamp": "1773446400000",  
                    "apr": "15%"  
                },  
                {  
                    "timestamp": "1773360000000",  
                    "apr": "15%"  
                },  
                {  
                    "timestamp": "1773273600000",  
                    "apr": "15%"  
                },  
                {  
                    "timestamp": "1773187200000",  
                    "apr": "15%"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1773741812091  
    }

---

# 查詢歷史 APR

信息

不需要鑒權

備註

最多可查詢 6 個月的歷史 APR 數據。

### HTTP 請求

GET`/v5/earn/apr-history`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
category| **true**|  string| `FlexibleSaving`,`OnChain`  
productId| **true**|  string| 產品 ID，從 [GET /v5/earn/product](/docs/zh-TW/v5/finance/earn/easy-onchain/product-info) 獲取  
startTime| false| integer| 查詢開始時間戳 (ms)。若 `startTime` 和 `endTime` 均不傳，默認返回最近 7 天的數據  
endTime| false| integer| 查詢結束時間戳 (ms)，與 `startTime` 的間隔不超過 182 天  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
list| array| Object  
> timestamp| string| 該記錄對應日期零點的 Unix 毫秒時間戳  
> apr| string| APR，decimal 字符串，如 `"0.055"` 表示 5.5%  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/earn/apr-history?productId=8&category=OnChain HTTP/1.1  
    Host: api-testnet.bybit.com  
    
    
    
      
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "list": [  
                {  
                    "timestamp": "1773705600000",  
                    "apr": "15%"  
                },  
                {  
                    "timestamp": "1773619200000",  
                    "apr": "15%"  
                },  
                {  
                    "timestamp": "1773532800000",  
                    "apr": "15%"  
                },  
                {  
                    "timestamp": "1773446400000",  
                    "apr": "15%"  
                },  
                {  
                    "timestamp": "1773360000000",  
                    "apr": "15%"  
                },  
                {  
                    "timestamp": "1773273600000",  
                    "apr": "15%"  
                },  
                {  
                    "timestamp": "1773187200000",  
                    "apr": "15%"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1773741812091  
    }