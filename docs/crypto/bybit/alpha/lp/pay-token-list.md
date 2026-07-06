---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/alpha/lp/pay-token-list
api_type: REST
updated_at: 2026-07-06 19:23:35.554675
---

# Get LP Pay Token List

Query the list of supported payment tokens for LP staking, including user's available balance for each.

info

  * Call this before staking to verify which tokens are available and check balances
  * **Rate Limit:** 5 req/s (per user), 5000 req/s (global)



### HTTP Request

POST`/v5/alpha/lp/pay-token-list`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
chainCode| false| string| Filter by blockchain identifier  
tokenAddress| false| string| Filter by token contract address  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
tokens| array| Payment token list  
> tokenCode| string| Token identifier, e.g. `CEX_1`  
> tokenSymbol| string| Token symbol, e.g. `USDT`  
> chainCode| string| Blockchain identifier  
> chainIconUrl| string| Blockchain icon URL  
> decimals| integer| Token decimal precision  
> availableBalance| string| User's available balance for this token  
> tokenIconUrlDay| string| Token icon URL (light mode)  
> tokenIconUrlNight| string| Token icon URL (dark mode)  
> minStakeAmount| string| Minimum stake amount for this token  
> maxStakeAmount| string| Maximum stake amount for this token  
  
* * *

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/alpha/lp/pay-token-list HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1704067200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {}  
    
    
    
      
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "tokens": [  
                {  
                    "tokenCode": "CEX_1",  
                    "tokenSymbol": "USDT",  
                    "chainCode": "ETH",  
                    "chainIconUrl": "",  
                    "decimals": 6,  
                    "availableBalance": "1000",  
                    "tokenIconUrlDay": "",  
                    "tokenIconUrlNight": "",  
                    "minStakeAmount": "",  
                    "maxStakeAmount": ""  
                },  
                {  
                    "tokenCode": "CEX_2",  
                    "tokenSymbol": "USDC",  
                    "chainCode": "ETH",  
                    "chainIconUrl": "",  
                    "decimals": 6,  
                    "availableBalance": "500",  
                    "tokenIconUrlDay": "",  
                    "tokenIconUrlNight": "",  
                    "minStakeAmount": "",  
                    "maxStakeAmount": ""  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1704067200000  
    }

---

# 查詢 LP 支付代幣列表

查詢 LP 質押所支持的支付代幣列表，包含每種代幣的用戶可用餘額。

信息

  * 質押前調用本接口，確認可用代幣種類及餘額
  * **頻率限制：** 5 次/秒（用戶），5000 次/秒（全局）



### HTTP 請求

POST`/v5/alpha/lp/pay-token-list`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
chainCode| false| string| 按區塊鏈標識符過濾  
tokenAddress| false| string| 按代幣合約地址過濾  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
tokens| array| 支付代幣列表  
> tokenCode| string| 代幣標識符，如 `CEX_1`  
> tokenSymbol| string| 代幣符號，如 `USDT`  
> chainCode| string| 區塊鏈標識符  
> chainIconUrl| string| 區塊鏈圖標 URL  
> decimals| integer| 代幣小數精度  
> availableBalance| string| 用戶該代幣的可用餘額  
> tokenIconUrlDay| string| 代幣圖標 URL（亮色模式）  
> tokenIconUrlNight| string| 代幣圖標 URL（暗色模式）  
> minStakeAmount| string| 該代幣最小質押數量  
> maxStakeAmount| string| 該代幣最大質押數量  
  
* * *

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/alpha/lp/pay-token-list HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1704067200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {}  
    
    
    
      
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "tokens": [  
                {  
                    "tokenCode": "CEX_1",  
                    "tokenSymbol": "USDT",  
                    "chainCode": "ETH",  
                    "chainIconUrl": "",  
                    "decimals": 6,  
                    "availableBalance": "1000",  
                    "tokenIconUrlDay": "",  
                    "tokenIconUrlNight": "",  
                    "minStakeAmount": "",  
                    "maxStakeAmount": ""  
                },  
                {  
                    "tokenCode": "CEX_2",  
                    "tokenSymbol": "USDC",  
                    "chainCode": "ETH",  
                    "chainIconUrl": "",  
                    "decimals": 6,  
                    "availableBalance": "500",  
                    "tokenIconUrlDay": "",  
                    "tokenIconUrlNight": "",  
                    "minStakeAmount": "",  
                    "maxStakeAmount": ""  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1704067200000  
    }