---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/account/pay-info
api_type: Account
updated_at: 2026-07-11 18:43:11.521102
---

# Get Pay Info

Query repayment collateral information for the account before repayment. This data is typically used prior to calling the [Repay](/docs/v5/account/repay) or [Repay Liability](/docs/v5/account/repay-liability) endpoints.

### HTTP Request

GET`/v5/account/pay-info`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
coin| false| string| Coin name, e.g. `USDT`, `BTC`. Must be a coin with outstanding liabilities, otherwise an error will be returned. If not passed, returns the aggregated total across all liabilities.  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
collateralInfo| object| Collateral info  
> collateralList| array<object>| Collateral list  
>> coin| string| Coin name  
>> availableSize| string| Available size  
>> availableValue| string| Available value (in USD)  
>> coinScale| integer| Coin precision  
>> borrowSize| string| Borrow size  
>> spotHedgeAmount| string| Spot hedge amount  
>> assetFrozen| string| Frozen asset  
borrowInfo| object| Borrow info for the queried coin.  
> coin| string| Coin name. Only returned when `coin` is passed in the request  
> borrowSize| string| Borrow size  
> borrowValue| string| Borrow value (in USD)  
> assetFrozen| string| Frozen asset  
> availableBalance| string| Available balance  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/account/pay-info?coin=SOL HTTP/1.1  
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
            "collateralInfo": {  
                "collateralList": [  
                    {  
                        "availableValue": "13038.369918809215134556464993",  
                        "coinScale": 4,  
                        "borrowSize": "0",  
                        "spotHedgeAmount": "0",  
                        "assetFrozen": "0",  
                        "availableSize": "13041.904274867704282417",  
                        "coin": "USDT"  
                    },  
                    {  
                        "availableValue": "4997.9120975285472554850",  
                        "coinScale": 6,  
                        "borrowSize": "0",  
                        "spotHedgeAmount": "0",  
                        "assetFrozen": "0",  
                        "availableSize": "4997.912097528547255485",  
                        "coin": "USDC"  
                    },  
                    {  
                        "availableValue": "0",  
                        "coinScale": 8,  
                        "borrowSize": "0.10006839",  
                        "spotHedgeAmount": "0",  
                        "assetFrozen": "0",  
                        "availableSize": "0",  
                        "coin": "SOL"  
                    },  
                    {  
                        "availableValue": "0",  
                        "coinScale": 9,  
                        "borrowSize": "0.001000068",  
                        "spotHedgeAmount": "-0.00100006728685180109293673123005419256514869630336761474609375",  
                        "assetFrozen": "0",  
                        "availableSize": "0",  
                        "coin": "BTC"  
                    },  
                    {  
                        "availableValue": "38488.319604591478793130841305",  
                        "coinScale": 8,  
                        "borrowSize": "0",  
                        "spotHedgeAmount": "0",  
                        "assetFrozen": "0",  
                        "availableSize": "17.867158854367695555",  
                        "coin": "ETH"  
                    }  
                ]  
            },  
            "borrowInfo": {  
                "borrowSize": "0.100068384926503532",  
                "assetFrozen": "0",  
                "borrowValue": "9.172497619169950215718876",  
                "coin": "SOL",  
                "availableBalance": "0"  
            }  
        },  
        "retExtInfo": {},  
        "time": 1774344990873  
    }

---

# 查詢還款信息

查詢帳戶的還款抵押品信息。該接口返回的數據通常在調用 [有損還款](/docs/zh-TW/v5/account/repay) 或 [還款負債](/docs/zh-TW/v5/account/repay-liability) 接口之前使用。

### HTTP 請求

GET`/v5/account/pay-info`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
coin| false| string| 幣種，如 `USDT`、`BTC`。必須傳入有負債的幣種，否則會報錯。不傳則返回所有負債的匯總總和  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
collateralInfo| object| 抵押品信息  
> collateralList| array<object>| 抵押品列表  
>> coin| string| 幣種  
>> availableSize| string| 可用數量  
>> availableValue| string| 可用價值（USD）  
>> coinScale| integer| 幣種精度  
>> borrowSize| string| 借貸數量  
>> spotHedgeAmount| string| 現貨對沖數量  
>> assetFrozen| string| 凍結資產  
borrowInfo| object| 查詢幣種的借貸信息。  
> coin| string| 幣種。僅在請求時傳入 `coin` 時返回  
> borrowSize| string| 借貸數量  
> borrowValue| string| 借貸價值（USD）  
> assetFrozen| string| 凍結資產  
> availableBalance| string| 可用餘額  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/account/pay-info?coin=SOL HTTP/1.1  
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
            "collateralInfo": {  
                "collateralList": [  
                    {  
                        "availableValue": "13038.369918809215134556464993",  
                        "coinScale": 4,  
                        "borrowSize": "0",  
                        "spotHedgeAmount": "0",  
                        "assetFrozen": "0",  
                        "availableSize": "13041.904274867704282417",  
                        "coin": "USDT"  
                    },  
                    {  
                        "availableValue": "4997.9120975285472554850",  
                        "coinScale": 6,  
                        "borrowSize": "0",  
                        "spotHedgeAmount": "0",  
                        "assetFrozen": "0",  
                        "availableSize": "4997.912097528547255485",  
                        "coin": "USDC"  
                    },  
                    {  
                        "availableValue": "0",  
                        "coinScale": 8,  
                        "borrowSize": "0.10006839",  
                        "spotHedgeAmount": "0",  
                        "assetFrozen": "0",  
                        "availableSize": "0",  
                        "coin": "SOL"  
                    },  
                    {  
                        "availableValue": "0",  
                        "coinScale": 9,  
                        "borrowSize": "0.001000068",  
                        "spotHedgeAmount": "-0.00100006728685180109293673123005419256514869630336761474609375",  
                        "assetFrozen": "0",  
                        "availableSize": "0",  
                        "coin": "BTC"  
                    },  
                    {  
                        "availableValue": "38488.319604591478793130841305",  
                        "coinScale": 8,  
                        "borrowSize": "0",  
                        "spotHedgeAmount": "0",  
                        "assetFrozen": "0",  
                        "availableSize": "17.867158854367695555",  
                        "coin": "ETH"  
                    }  
                ]  
            },  
            "borrowInfo": {  
                "borrowSize": "0.100068384926503532",  
                "assetFrozen": "0",  
                "borrowValue": "9.172497619169950215718876",  
                "coin": "SOL",  
                "availableBalance": "0"  
            }  
        },  
        "retExtInfo": {},  
        "time": 1774344990873  
    }