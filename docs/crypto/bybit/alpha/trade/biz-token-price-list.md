---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/alpha/trade/biz-token-price-list
api_type: Trading
updated_at: 2026-11-13 19:21:20.975062
---

# Get Token Price List

Batch query on-chain token prices, 24h change, volume, market cap, and other market data.

info

  * Supports querying multiple tokens in a single request (max 20)
  * Tokens are identified by `chainCode` \+ `tokenAddress` pairs — get these from [Get Biz Token List](/docs/v5/alpha/trade/biz-token-list) or [Get Asset List](/docs/v5/alpha/trade/asset-list)
  * To discover new tokens, use [Get Biz Token List](/docs/v5/alpha/trade/biz-token-list) instead



### HTTP Request

POST`/v5/alpha/trade/biz-token-price-list`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
tokenAddressInfo| **true**|  array| List of token identifiers to query. Maximum 20 items per request  
> chainCode| **true**|  string| Blockchain code, e.g. `ETH`, `SOL`, `BSC`  
> tokenAddress| **true**|  string| Token contract address on the specified chain  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
tokenPriceInfoList| array| Token price info list  
> chainCode| string| Blockchain code  
> tokenAddress| string| Token contract address  
> price| string| Current price in USD  
> change24h| string| 24-hour price change as decimal, e.g. `0.15` = +15%  
> vol24h| string| 24-hour trading volume in USD  
> marketCap| string| Market capitalization in USD  
> liquidity| string| Total liquidity in USD  
> holders| string| Number of token holders  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/alpha/trade/biz-token-price-list HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1704067200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "tokenAddressInfo": [  
            {  
                "chainCode": "ETH",  
                "tokenAddress": "0x6982508145454ce325ddbe47a25d4ec3d2311933"  
            },  
            {  
                "chainCode": "SOL",  
                "tokenAddress": "DezXAZ8z7PnrnRJjz3wXBoRgixCa6xjnB7YaB1pPB263"  
            }  
        ]  
    }  
    
    
    
      
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "tokenPriceInfoList": [  
                {  
                    "chainCode": "ETH",  
                    "tokenAddress": "0x6982508145454ce325ddbe47a25d4ec3d2311933",  
                    "price": "0.00001",  
                    "change24h": "0.15",  
                    "vol24h": "125000000",  
                    "marketCap": "4200000000",  
                    "liquidity": "50000000",  
                    "holders": "250000"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1704067200000  
    }

---

# 獲取代幣價格列表

批量查詢鏈上代幣的價格、24 小時漲跌幅、成交量、市值等行情數據。

信息

  * 單次請求最多查詢 20 個代幣
  * 代幣通過 `chainCode` \+ `tokenAddress` 組合識別 — 可從 [獲取業務代幣列表](/docs/zh-TW/v5/alpha/trade/biz-token-list) 或 [查詢資產列表](/docs/zh-TW/v5/alpha/trade/asset-list) 獲取
  * 若需發現新代幣，請使用 [獲取業務代幣列表](/docs/zh-TW/v5/alpha/trade/biz-token-list)



### HTTP 請求

POST`/v5/alpha/trade/biz-token-price-list`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
tokenAddressInfo| **true**|  array| 代幣標識列表，單次最多 20 個  
> chainCode| **true**|  string| 區塊鏈代碼，如 `ETH`、`SOL`、`BSC`  
> tokenAddress| **true**|  string| 指定鏈上的代幣合約地址  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
tokenPriceInfoList| array| 代幣價格信息列表  
> chainCode| string| 區塊鏈代碼  
> tokenAddress| string| 代幣合約地址  
> price| string| 當前價格（USD）  
> change24h| string| 24 小時漲跌幅（小數），如 `0.15` = +15%  
> vol24h| string| 24 小時交易量（USD）  
> marketCap| string| 市值（USD）  
> liquidity| string| 總流動性（USD）  
> holders| string| 持幣地址數  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/alpha/trade/biz-token-price-list HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1704067200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "tokenAddressInfo": [  
            {  
                "chainCode": "ETH",  
                "tokenAddress": "0x6982508145454ce325ddbe47a25d4ec3d2311933"  
            },  
            {  
                "chainCode": "SOL",  
                "tokenAddress": "DezXAZ8z7PnrnRJjz3wXBoRgixCa6xjnB7YaB1pPB263"  
            }  
        ]  
    }  
    
    
    
      
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "tokenPriceInfoList": [  
                {  
                    "chainCode": "ETH",  
                    "tokenAddress": "0x6982508145454ce325ddbe47a25d4ec3d2311933",  
                    "price": "0.00001",  
                    "change24h": "0.15",  
                    "vol24h": "125000000",  
                    "marketCap": "4200000000",  
                    "liquidity": "50000000",  
                    "holders": "250000"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1704067200000  
    }