---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/new-crypto-loan/ltv-adjust-history
api_type: REST
updated_at: 2026-08-15 18:44:25.456756
---

# Get Collateral Adjustment History

Query for your LTV adjustment history.

> Permission: "Spot trade"  
>  UID rate limit: 5 req / second

### HTTP Request

GET`/v5/crypto-loan-common/adjustment-history`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
adjustId| false| string| Collateral adjustment transaction ID  
collateralCurrency| false| string| Collateral coin name  
limit| false| string| Limit for data size per page. [`1`, `100`]. Default: `10`  
cursor| false| string| Cursor. Use the `nextPageCursor` token from the response to retrieve the next page of the result set  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array| Object  
> collateralCurrency| string| Collateral coin  
> amount| string| amount  
> adjustId| long| Collateral adjustment transaction ID  
> adjustTime| long| Adjust timestamp  
> preLTV| string| LTV before the adjustment  
> afterLTV| string| LTV after the adjustment  
> direction| integer| The direction of adjustment, `0`: add collateral; `1`: reduce collateral  
> status| integer| The status of adjustment, `1`: success; `2`: processing; `3`: fail  
nextPageCursor| string| Refer to the `cursor` request parameter  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/crypto-loan-common/adjustment-history?limit=2&collateralCurrency=BTC HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1752628288472  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_ltv_adjustment_history_new_crypto_loan(  
        limit="2",  
        collateralCurrency="BTC",  
    ))  
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "ok",  
        "result": {  
            "list": [  
                {  
                    "adjustId": 27511,  
                    "adjustTime": 1752627997907,  
                    "afterLTV": "0.813743",  
                    "amount": "0.08",  
                    "collateralCurrency": "BTC",  
                    "direction": 1,  
                    "preLTV": "0.524602",  
                    "status": 1  
                },  
                {  
                    "adjustId": 27491,  
                    "adjustTime": 1752218558913,  
                    "afterLTV": "0.41983",  
                    "amount": "0.03",  
                    "collateralCurrency": "BTC",  
                    "direction": 1,  
                    "preLTV": "0.372314",  
                    "status": 1  
                }  
            ],  
            "nextPageCursor": "27491"  
        },  
        "retExtInfo": {},  
        "time": 1752628288732  
    }

---

# 查詢質押金調整歷史

查詢增減質押金的操作歷史

> 權限: "現貨"  
>  頻率: 5次/秒

### HTTP 請求

GET`/v5/crypto-loan-common/adjustment-history`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
adjustId| false| string| 質押金調整操作ID  
collateralCurrency| false| string| 質押幣種  
limit| false| string| 每頁數量限制. [`1`, `100`]. 默認: `10`  
cursor| false| string| 游標，用於分頁  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
list| array| Object  
> collateralCurrency| string| 抵押幣種  
> amount| string| 金額  
> adjustId| long| 抵押調整交易 ID  
> adjustTime| long| 調整時間戳  
> preLTV| string| 調整前質押率（LTV）  
> afterLTV| string| 調整後質押率（LTV）  
> direction| integer| 調整方向，`0`: 增加抵押；`1`: 減少抵押  
> status| integer| 調整狀態，`1`: 成功；`2`: 處理中；`3`: 失敗  
nextPageCursor| string| 下一頁游標  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/crypto-loan-common/adjustment-history?limit=2&collateralCurrency=BTC HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1752628288472  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_ltv_adjustment_history_new_crypto_loan(  
        limit="2",  
        collateralCurrency="BTC",  
    ))  
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "ok",  
        "result": {  
            "list": [  
                {  
                    "adjustId": 27511,  
                    "adjustTime": 1752627997907,  
                    "afterLTV": "0.813743",  
                    "amount": "0.08",  
                    "collateralCurrency": "BTC",  
                    "direction": 1,  
                    "preLTV": "0.524602",  
                    "status": 1  
                },  
                {  
                    "adjustId": 27491,  
                    "adjustTime": 1752218558913,  
                    "afterLTV": "0.41983",  
                    "amount": "0.03",  
                    "collateralCurrency": "BTC",  
                    "direction": 1,  
                    "preLTV": "0.372314",  
                    "status": 1  
                }  
            ],  
            "nextPageCursor": "27491"  
        },  
        "retExtInfo": {},  
        "time": 1752628288732  
    }