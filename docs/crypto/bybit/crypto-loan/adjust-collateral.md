---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/crypto-loan/adjust-collateral
api_type: REST
updated_at: 2026-06-28 19:10:03.652261
---

# Get Loan LTV Adjustment History

Query for your LTV adjustment history.

> Permission: "Spot trade"

info

  * Support querying last 6 months adjustment transactions
  * Only the ltv adjustment transactions launched by the user can be queried



### HTTP Request

GET`/v5/crypto-loan/adjustment-history`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
orderId| false| string| Loan order ID  
adjustId| false| string| Collateral adjustment transaction ID  
collateralCurrency| false| string| Collateral coin name  
limit| false| string| Limit for data size per page. [`1`, `100`]. Default: `10`  
cursor| false| string| Cursor. Use the `nextPageCursor` token from the response to retrieve the next page of the result set  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array| Object  
> collateralCurrency| string| Collateral coin  
> orderId| string| Loan order ID  
> adjustId| string| Collateral adjustment transaction ID  
> adjustTime| string| Adjust timestamp  
> preLTV| string| LTV before the adjustment  
> afterLTV| string| LTV after the adjustment  
> direction| integer| The direction of adjustment, `0`: add collateral; `1`: reduce collateral  
nextPageCursor| string| Refer to the `cursor` request parameter  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/crypto-loan/adjustment-history?adjustId=1794318409405331968 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1728635871668  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_crypto_loan_ltv_adjustment_history(  
        adjustId="1794318409405331968",  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getLoanLTVAdjustmentHistory({ adjustId: '1794271131730737664' })  
      .then((response) => {  
        console.log(response);  
      })  
      .catch((error) => {  
        console.error(error);  
      });  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "request.success",  
        "result": {  
            "list": [  
                {  
                    "adjustId": "1794318409405331968",  
                    "adjustTime": "1728635422814",  
                    "afterLTV": "0.7164",  
                    "amount": "0.001",  
                    "collateralCurrency": "BTC",  
                    "direction": 1,  
                    "orderId": "1794267532472646144",  
                    "preLTV": "0.6546"  
                }  
            ],  
            "nextPageCursor": "1844656778923966466"  
        },  
        "retExtInfo": {},  
        "time": 1728635873329  
    }

---

# 查詢質押金調整歷史

查詢增減質押金的操作歷史

> 權限: "現貨交易"

信息

  * 支持查詢過去6個月的操作紀錄
  * 僅返回由用戶主動發起的質押金操作紀錄



### HTTP 請求

GET`/v5/crypto-loan/adjustment-history`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
orderId| false| string| 借貸訂單ID  
adjustId| false| string| 質押金調整操作ID  
collateralCurrency| false| string| 質押幣種  
limit| false| string| 每頁數量限制. [`1`, `100`]. 默認: `10`  
cursor| false| string| 游標，用於分頁  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
list| array| Object  
> collateralCurrency| string| 質押幣種  
> orderId| string| 借貸訂單ID  
> adjustId| string| 質押金調整操作ID  
> adjustTime| string| 調整時間戳  
> preLTV| string| 调整前LTV  
> afterLTV| string| 調整後LTV  
> direction| integer| 調整方向, `0`: 增加; `1`: 減少  
nextPageCursor| string| 下一頁游標  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/crypto-loan/adjustment-history?adjustId=1794318409405331968 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1728635871668  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_crypto_loan_ltv_adjustment_history(  
        adjustId="1794318409405331968",  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getLoanLTVAdjustmentHistory({ adjustId: '1794271131730737664' })  
      .then((response) => {  
        console.log(response);  
      })  
      .catch((error) => {  
        console.error(error);  
      });  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "request.success",  
        "result": {  
            "list": [  
                {  
                    "adjustId": "1794318409405331968",  
                    "adjustTime": "1728635422814",  
                    "afterLTV": "0.7164",  
                    "amount": "0.001",  
                    "collateralCurrency": "BTC",  
                    "direction": 1,  
                    "orderId": "1794267532472646144",  
                    "preLTV": "0.6546"  
                }  
            ],  
            "nextPageCursor": "1844656778923966466"  
        },  
        "retExtInfo": {},  
        "time": 1728635873329  
    }