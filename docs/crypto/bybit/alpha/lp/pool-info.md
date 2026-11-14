---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/alpha/lp/pool-info
api_type: REST
updated_at: 2026-11-13 19:21:04.172678
---

# Get LP Pool Info

Query detailed information for a specific liquidity pool, including APY, fees, token reserves, and price range.

info

  * Call this before staking to show users complete pool details
  * `poolAddress` must be obtained from the pool list
  * **Rate Limit:** 5 req/s (per user), 5000 req/s (global)



### HTTP Request

POST`/v5/alpha/lp/pool-info`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
poolAddress| **true**|  string| Pool contract address  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
poolAddress| string| Pool contract address  
poolName| string| Pool name  
apy| string| Annual percentage yield  
tvl| string| Total value locked  
feeRate| string| Pool fee rate, e.g. `"0.003"` = 0.3%  
token0Symbol| string| Token0 symbol  
token0Reserve| string| Token0 reserve amount  
token1Symbol| string| Token1 symbol  
token1Reserve| string| Token1 reserve amount  
priceRangeLower| string| Price range lower bound  
priceRangeUpper| string| Price range upper bound  
currentPrice| string| Current pool price  
  
* * *

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/alpha/lp/pool-info HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1704067200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "poolAddress": "0x1234567890abcdef"  
    }  
    
    
    
      
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "poolAddress": "0x1234567890abcdef",  
            "poolName": "ETH-USDC Pool",  
            "apy": "12.5",  
            "tvl": "1000000",  
            "feeRate": "0.003",  
            "token0Symbol": "ETH",  
            "token0Reserve": "500",  
            "token1Symbol": "USDC",  
            "token1Reserve": "1000000",  
            "priceRangeLower": "",  
            "priceRangeUpper": "",  
            "currentPrice": ""  
        },  
        "retExtInfo": {},  
        "time": 1704067200000  
    }

---

# 查詢 LP 礦池詳情

查詢指定流動性礦池的詳細信息，包括 APY、手續費率、代幣儲備及價格區間。

信息

  * 質押前調用本接口，向用戶展示完整的礦池詳情
  * `poolAddress` 需從礦池列表接口獲取
  * **頻率限制：** 5 次/秒（用戶），5000 次/秒（全局）



### HTTP 請求

POST`/v5/alpha/lp/pool-info`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
poolAddress| **true**|  string| 礦池合約地址  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
poolAddress| string| 礦池合約地址  
poolName| string| 礦池名稱  
apy| string| 年化收益率  
tvl| string| 總鎖倉價值  
feeRate| string| 礦池手續費率，如 `"0.003"` = 0.3%  
token0Symbol| string| Token0 符號  
token0Reserve| string| Token0 儲備量  
token1Symbol| string| Token1 符號  
token1Reserve| string| Token1 儲備量  
priceRangeLower| string| 價格區間下限  
priceRangeUpper| string| 價格區間上限  
currentPrice| string| 當前礦池價格  
  
* * *

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/alpha/lp/pool-info HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1704067200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "poolAddress": "0x1234567890abcdef"  
    }  
    
    
    
      
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "poolAddress": "0x1234567890abcdef",  
            "poolName": "ETH-USDC Pool",  
            "apy": "12.5",  
            "tvl": "1000000",  
            "feeRate": "0.003",  
            "token0Symbol": "ETH",  
            "token0Reserve": "500",  
            "token1Symbol": "USDC",  
            "token1Reserve": "1000000",  
            "priceRangeLower": "",  
            "priceRangeUpper": "",  
            "currentPrice": ""  
        },  
        "retExtInfo": {},  
        "time": 1704067200000  
    }