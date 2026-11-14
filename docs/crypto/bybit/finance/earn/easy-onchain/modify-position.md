---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/earn/easy-onchain/modify-position
api_type: REST
updated_at: 2026-11-13 19:23:12.801960
---

# Modify Position

info

API key needs "Earn" permission

note

Only positions with `duration` = `Fixed` support setting auto-reinvestment. You can get the `duration` value from the response of [GET /v5/earn/product?category=OnChain](/docs/v5/finance/earn/easy-onchain/product-info).

### HTTP Request

POST`/v5/earn/position/modify`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
category| **true**|  string| Product category. Fixed value: `OnChain`  
productId| **true**|  integer| Product ID. Obtained from [GET /v5/earn/product](/docs/v5/finance/earn/easy-onchain/product-info)  
positionId| **true**|  integer| Position ID. Obtained from [GET /v5/earn/position](/docs/v5/finance/earn/easy-onchain/position)  
autoReinvest| **true**|  integer| Auto-reinvestment switch. `0`: Off, `1`: On  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
retCode| integer| Return code. `0` means success  
retMsg| string| Return message. Empty string `""` on success  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/earn/position/modify HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1773732693000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "category": "OnChain",  
        "productId": 8,  
        "positionId": 326,  
        "autoReinvest": 1  
    }  
    
    
    
      
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {},  
        "retExtInfo": {},  
        "time": 1773732693032  
    }

---

# 修改持倉設置

信息

API key 需要「理財」權限

備註

僅 `duration` = `Fixed` 的持倉支持設置自動複投。您可以從 [GET /v5/earn/product?category=OnChain](/docs/zh-TW/v5/finance/earn/easy-onchain/product-info) 的響應參數中獲取 `duration` 的值。

### HTTP 請求

POST`/v5/earn/position/modify`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
category| **true**|  string| 產品類別，固定傳 `OnChain`  
productId| **true**|  integer| 產品 ID，從 [GET /v5/earn/product](/docs/zh-TW/v5/finance/earn/easy-onchain/product-info) 獲取  
positionId| **true**|  integer| 持倉 ID，從 [GET /v5/earn/position](/docs/zh-TW/v5/finance/earn/easy-onchain/position) 獲取  
autoReinvest| **true**|  integer| 自動續期開關。`0`：關閉，`1`：開啟  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
retCode| integer| 返回碼，`0` 表示成功  
retMsg| string| 返回信息，成功時為 `""`  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/earn/position/modify HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1773732693000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "category": "OnChain",  
        "productId": 8,  
        "positionId": 326,  
        "autoReinvest": 1  
    }  
    
    
    
      
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {},  
        "retExtInfo": {},  
        "time": 1773732693032  
    }