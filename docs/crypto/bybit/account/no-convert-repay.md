---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/account/no-convert-repay
api_type: Account
updated_at: 2026-11-13 19:20:49.306900
---

# Manual Repay Without Asset Conversion

info

  * When `coin` is provided and `amount` is provided, the following validation applies based on `repaymentType`:
    * `ALL`: request is rejected if `amount` exceeds total liability
    * `FIXED`: request is rejected if `amount` exceeds fixed-rate liability
    * `FLEXIBLE`: request is rejected if `amount` exceeds floating-rate liability
  * When `coin` is provided and `amount` is not, repayment uses the spot available balance of that coin:
    * `FLEXIBLE`: repays floating-rate liability of that coin only
    * `FIXED`: repays fixed-rate liability of that coin only
    * `ALL`: repays all liabilities of that coin (floating-rate first, then fixed-rate)



important

  1. When repaying, system will only use the spot available balance of the debt currency. Users can perform a manual repay without converting their other assets.
  2. To check the spot available amount to repay, you can call this API: [Get Available Amount to Repay](/docs/v5/spot-margin-uta/repayment-available-amount)
  3. Repayment is prohibited between 04:00 and 05:30 per hour. Interest is calculated based on the BorrowAmount at 05:00 per hour.
  4. System repays floating-rate liabilities first, followed by fixed-rate
  5. Starting Mar 17, 2026 (gradual rollout, fully released on Mar 24, 2026), BYUSDT can be used for repayment.
  6. API response behavior based on `repaymentType`: `FIXED`: asynchronous; `FLEXIBLE`: synchronous; `ALL`: asynchronous



### HTTP Request

POST`/v5/account/no-convert-repay`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
coin| **true**|  string| coin name, uppercase only  
amount| false| string| Repay amount. If `coin` is not passed in input parameter, `amount` can not be passed in input parameter  
repaymentType| false| string| Repayment type. `ALL`: repay both fixed-rate and floating-rate liabilities, repaying floating-rate first; `FIXED`: repay fixed-rate liabilities only; `FLEXIBLE`: repay floating-rate liabilities only. Default: `FLEXIBLE`  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
result| array| Object  
> resultStatus| string| 

  * `P`: Processing
  * `SU`: Success
  * `FA`: Failed

  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/account/no-convert-repay HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1675842997277  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "coin":"BTC",  
        "amount":"0.01"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.set_no_convert_repay(  
        coin="BTC",  
        amount="0.01"  
    ))  
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "resultStatus": "P"  
        },  
        "retExtInfo": {},  
        "time": 1756295680801  
    }

---

# 無損手工還款

信息

  * 當傳入 `coin` 和 `amount` 時，根據 `repaymentType` 進行以下校驗：
    * `ALL`：若 `amount` 超過總負債，則拒絕請求
    * `FIXED`：若 `amount` 超過定期負債，則拒絕請求
    * `FLEXIBLE`：若 `amount` 超過活期負債，則拒絕請求
  * 當傳入 `coin` 但未傳入 `amount` 時，使用該幣種的現貨可用餘額進行還款：
    * `FLEXIBLE`：僅償還該幣種的活期負債
    * `FIXED`：僅償還該幣種的定期負債
    * `ALL`：償還該幣種的所有負債（先活期，再定期）



重要

  1. 還款時，只使用負債幣種的現貨可用餘額. 用戶不會轉換其他資產進行手動還款。
  2. 若要查看可用於還款的現貨可用餘額，您可以調用此 API：[查詢負債幣種可還款金額](/docs/zh-TW/v5/spot-margin-uta/repayment-available-amount)
  3. 每小時04分-05分30秒，禁止還款。計息是按每小時05分那一刻的borrowAmount來進行計息。
  4. 系統先償還浮動利率債務，然後償還固定利率債務。
  5. 自2026年3月17日起開始灰度，2026年3月24日全量發布，BYUSDT 可用於還款
  6. 接口結果說明（根據 `repaymentType`）：`FIXED`：異步；`FLEXIBLE`：同步；`ALL`：異步



### HTTP 請求

POST`/v5/account/no-convert-repay`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
coin| **true**|  string| 幣名稱，僅限大寫  
amount| false| string| 還款金額，若未使用 `coin` 作為輸入參數，則 `amount` 不作為輸入參數  
repaymentType| false| string| 還款類型。`ALL`：同時償還定期和活期負債，先還活期再還定期；`FIXED`：僅償還定期負債；`FLEXIBLE`：僅償還活期負債。默認值：`FLEXIBLE`  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
result| array| Object  
> resultStatus| string| 

  * `P`: 處理中
  * `SU`: 成功
  * `FA`: 失敗

  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/account/no-convert-repay HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1675842997277  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "coin":"BTC",  
        "amount":"0.01"  
    }  
    
    
    
      
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "resultStatus": "P"  
        },  
        "retExtInfo": {},  
        "time": 1756295680801  
    }