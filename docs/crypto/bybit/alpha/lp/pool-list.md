---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/alpha/lp/pool-list
api_type: REST
updated_at: 2026-11-13 19:21:04.198733
---

# Get LP Pool List

Query available liquidity pools with optional filtering by token symbol.

info

  * Use this to help users discover and compare available LP pools
  * Filter by `tokenSymbol` to find pools containing a specific token
  * **Rate Limit:** 5 req/s (per user), 5000 req/s (global)



### HTTP Request

POST`/v5/alpha/lp/pool-list`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
tokenSymbol| false| string| Search pools containing this token symbol, e.g. `ETH`, `USDC`  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
pools| array| Pool list  
> poolAddress| string| Pool contract address  
> poolName| string| Pool name  
> poolTag| string| Pool category tag  
> apy| string| Annual percentage yield  
> tvl| string| Total value locked (USD)  
> token0Symbol| string| First token symbol  
> token0IconUrlDay| string| First token icon URL (light mode)  
> token0IconUrlNight| string| First token icon URL (dark mode)  
> token1Symbol| string| Second token symbol  
> token1IconUrlDay| string| Second token icon URL (light mode)  
> token1IconUrlNight| string| Second token icon URL (dark mode)  
> chainCode| string| Blockchain identifier  
> chainIconUrl| string| Blockchain icon URL  
  
* * *

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/alpha/lp/pool-list HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1704067200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "tokenSymbol": "ETH"  
    }  
    
    
    
      
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "pools": [  
                {  
                    "poolAddress": "0x1234567890abcdef",  
                    "poolName": "ETH-USDC Pool",  
                    "poolTag": "Trending",  
                    "apy": "12.5",  
                    "tvl": "1000000",  
                    "token0Symbol": "ETH",  
                    "token0IconUrlDay": "",  
                    "token0IconUrlNight": "",  
                    "token1Symbol": "USDC",  
                    "token1IconUrlDay": "",  
                    "token1IconUrlNight": "",  
                    "chainCode": "",  
                    "chainIconUrl": ""  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1704067200000  
    }

---

# 查詢 LP 礦池列表

查詢可用的流動性礦池列表，支持按代幣符號過濾。

信息

  * 可用本接口幫助用戶發現和比較可用的 LP 礦池
  * 傳入 `tokenSymbol` 可篩選包含指定代幣的礦池
  * **頻率限制：** 5 次/秒（用戶），5000 次/秒（全局）



### HTTP 請求

POST`/v5/alpha/lp/pool-list`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
tokenSymbol| false| string| 按代幣符號搜索包含該代幣的礦池，如 `ETH`、`USDC`  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
pools| array| 礦池列表  
> poolAddress| string| 礦池合約地址  
> poolName| string| 礦池名稱  
> poolTag| string| 礦池分類標籤  
> apy| string| 年化收益率  
> tvl| string| 總鎖倉價值（USD）  
> token0Symbol| string| 第一個代幣符號  
> token0IconUrlDay| string| 第一個代幣圖標 URL（亮色模式）  
> token0IconUrlNight| string| 第一個代幣圖標 URL（暗色模式）  
> token1Symbol| string| 第二個代幣符號  
> token1IconUrlDay| string| 第二個代幣圖標 URL（亮色模式）  
> token1IconUrlNight| string| 第二個代幣圖標 URL（暗色模式）  
> chainCode| string| 區塊鏈標識符  
> chainIconUrl| string| 區塊鏈圖標 URL  
  
* * *

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/alpha/lp/pool-list HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1704067200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "tokenSymbol": "ETH"  
    }  
    
    
    
      
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "pools": [  
                {  
                    "poolAddress": "0x1234567890abcdef",  
                    "poolName": "ETH-USDC Pool",  
                    "poolTag": "Trending",  
                    "apy": "12.5",  
                    "tvl": "1000000",  
                    "token0Symbol": "ETH",  
                    "token0IconUrlDay": "",  
                    "token0IconUrlNight": "",  
                    "token1Symbol": "USDC",  
                    "token1IconUrlDay": "",  
                    "token1IconUrlNight": "",  
                    "chainCode": "",  
                    "chainIconUrl": ""  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1704067200000  
    }