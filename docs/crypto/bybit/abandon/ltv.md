---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/abandon/ltv
api_type: REST
updated_at: 2026-05-27 19:13:45.913119
---

# Get Margin Coin Info

### HTTP Request

GET`/v5/ins-loan/ensure-tokens`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
productId| false| string| ProductId. If not passed, then return all product margin coin. For spot, it returns coin that convertRation greater than 0.  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
marginToken| array| Object  
> productId| string| Product Id  
> spotToken| array| Spot margin coin  
>> token| string| Margin coin  
>> convertRatio| string| Margin coin convert ratio  
> contractToken| array| Contract margin coin  
>> token| string| Margin coin  
>> convertRatio| string| Margin coin convert ratio  
  
### Request Example
    
    
    GET /v5/ins-loan/ensure-tokens?productId=70 HTTP/1.1  
    Host: api-testnet.bybit.com  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "marginToken": [  
                {  
                    "productId": "70",  
                    "spotToken": [  
                        {  
                            "token": "BTC",  
                            "convertRatio": "1.00000000"  
                        },  
                        {  
                            "token": "ETH",  
                            "convertRatio": "1.00000000"  
                        },  
                        {  
                            "token": "USDT",  
                            "convertRatio": "1"  
                        }  
                    ],  
                    "contractToken": [  
                        {  
                            "token": "USDT",  
                            "convertRatio": "1"  
                        }  
                    ]  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1669363954802  
    }

---

# 查詢保證金幣種信息

提示

這是公共接口，無需鑒權。

### HTTP 請求

GET`/v5/ins-loan/ensure-tokens`

### 請求參數

參數| 是否必須| 類型| 說明  
---|---|---|---  
productId| false| string| 產品ID. 若不傳，則返回所有產品的保證金幣種信息. 現貨返回折算率大於0的幣種.  
  
### 返回參數

參數| 類型| 說明  
---|---|---  
marginToken| array| Object  
> productId| string| 產品ID  
> spotToken| array| 現貨保證金幣種信息  
>> token| string| 保證金幣種  
>> convertRatio| string| 保證金幣種折算率  
> contractToken| array| 合約保證金幣種信息  
>> token| string| 保證金幣種  
>> convertRatio| string| 保證金幣種折算率  
  
### 請求示例
    
    
    GET /v5/ins-loan/ensure-tokens?productId=70 HTTP/1.1  
    Host: api-testnet.bybit.com  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "marginToken": [  
                {  
                    "productId": "70",  
                    "spotToken": [  
                        {  
                            "token": "BTC",  
                            "convertRatio": "1.00000000"  
                        },  
                        {  
                            "token": "ETH",  
                            "convertRatio": "1.00000000"  
                        },  
                        {  
                            "token": "USDT",  
                            "convertRatio": "1"  
                        }  
                    ],  
                    "contractToken": [  
                        {  
                            "token": "USDT",  
                            "convertRatio": "1"  
                        }  
                    ]  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1669363954802  
    }