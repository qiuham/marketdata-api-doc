---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/new-crypto-loan/fixed/supply
api_type: REST
updated_at: 2026-05-27 19:18:54.951347
---

# Get Supply Contract Info

> Permission: "Spot trade"  
>  UID rate limit: 5 req / second

### HTTP Request

GET`/v5/crypto-loan-fixed/supply-contract-info`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
orderId| false| string| Supply order ID  
supplyId| false| string| Supply contract ID  
supplyCurrency| false| string| Supply coin name  
term| false| string| Fixed term `7`: 7 days; `14`: 14 days; `30`: 30 days; `90`: 90 days; `180`: 180 days  
limit| false| string| Limit for data size per page. [`1`, `100`]. Default: `10`  
cursor| false| string| Cursor. Use the `nextPageCursor` token from the response to retrieve the next page of the result set  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array| Object  
> annualRate| string| Annual rate for the supply  
> supplyCurrency| string| Supply coin  
> supplyTime| string| Supply timestamp  
> supplyAmount| string| Supply amount  
> interestPaid| string| Paid interest  
> supplyId| string| Supply contract ID  
> orderId| string| Supply order ID  
> redemptionTime| string| Planned time to redeem  
> penaltyInterest| string| Overdue interest  
> actualRedemptionTime| string| Actual time to redeem  
> status| integer| Supply contract status `1`: Supplying; `2`: Redeemed  
> term| string| Fixed term `7`: 7 days; `14`: 14 days; `30`: 30 days; `90`: 90 days; `180`: 180 days  
nextPageCursor| string| Refer to the `cursor` request parameter  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/crypto-loan-fixed/supply-contract-info?supplyCurrency=USDT HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1752654376532  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_lending_contract_info_fixed_crypto_loan(  
        supplyCurrency="USDT",  
    ))  
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "ok",  
        "result": {  
            "list": [  
                {  
                    "actualRedemptionTime": "1753087596082",  
                    "annualRate": "0.01",  
                    "interest": "0.13041095890410959",  
                    "orderId": "13564",  
                    "penaltyInterest": "0",  
                    "redemptionTime": "1753087596082",  
                    "status": 1,  
                    "supplyAmount": "800",  
                    "supplyCurrency": "USDT",  
                    "supplyId": "567",  
                    "supplyTime": "1752482796082",  
                    "term": "7"  
                }  
            ],  
            "nextPageCursor": "567"  
        },  
        "retExtInfo": {},  
        "time": 1752654377461  
    }

---

# 查詢存款合同

> 權限: "現貨"  
>  頻率: 5次/秒

### HTTP 請求

GET`/v5/crypto-loan-fixed/supply-contract-info`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
orderId| false| string| 存款訂單ID  
supplyId| false| string| 存款合同ID  
supplyCurrency| false| string| 存款幣種  
term| false| string| 存款期限 `7`: 7天; `14`: 14天; `30`: 30天; `90`: 90天; `180`: 180天  
limit| false| string| 每頁數量限制. [`1`, `100`]. 默認: `10`  
cursor| false| string| 游標，用於分頁  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
list| array| Object  
> annualRate| string| 出借年化利率  
> supplyCurrency| string| 出借幣種  
> supplyTime| string| 出借時間戳  
> supplyAmount| string| 出借金額  
> interestPaid| string| 已支付利息  
> supplyId| string| 出借合約 ID  
> orderId| string| 出借訂單 ID  
> redemptionTime| string| 預計贖回時間  
> penaltyInterest| string| 逾期利息  
> actualRedemptionTime| string| 實際贖回時間  
> status| integer| 出借合約狀態 `1`: 出借中；`2`: 已贖回  
> term| string| 固定期限 `7`: 7 天；`14`: 14 天；`30`: 30 天；`90`: 90 天；`180`: 180 天  
nextPageCursor| string| 下一頁游標  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/crypto-loan-fixed/supply-contract-info?supplyCurrency=USDT HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1752654376532  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_lending_contract_info_fixed_crypto_loan(  
        supplyCurrency="USDT",  
    ))  
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "ok",  
        "result": {  
            "list": [  
                {  
                    "actualRedemptionTime": "1753087596082",  
                    "annualRate": "0.01",  
                    "interest": "0.13041095890410959",  
                    "orderId": "13564",  
                    "penaltyInterest": "0",  
                    "redemptionTime": "1753087596082",  
                    "status": 1,  
                    "supplyAmount": "800",  
                    "supplyCurrency": "USDT",  
                    "supplyId": "567",  
                    "supplyTime": "1752482796082",  
                    "term": "7"  
                }  
            ],  
            "nextPageCursor": "567"  
        },  
        "retExtInfo": {},  
        "time": 1752654377461  
    }