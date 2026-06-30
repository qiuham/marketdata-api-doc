---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/asset/deposit/set-deposit-acct
api_type: REST
updated_at: 2026-06-30 19:23:38.410447
---

# Submit Deposit Originator Info

Submit the originator's compliance information when a deposit triggers a Travel Rule review. After submission, the vendor completes the review and returns the resulting status.

info

Call this endpoint when a deposit record hits the Travel Rule compliance policy and the current `travel_rule_status` is `1` (pending counterparty info submission).

### HTTP Request

POST`/v5/asset/travel-rule/deposit/submit`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
depositId| **true**|  integer| Deposit record ID obtained from the deposit query API  
subAccountId| false| integer| Broker scenario: target sub-account UID. Pass `0` or omit to use the current account  
questionnaire| **true**|  string| Travel Rule questionnaire info as a JSON string. Max 16384 bytes. Structure varies by compliance zone. See [Questionnaire](/docs/v5/asset/withdraw/questionnaire)  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
travelRuleStatus| integer| Travel Rule review status 

  * `0`: Approved — review passed, proceed with subsequent flow
  * `1`: CollectInfo — counterparty info required, re-submit questionnaire
  * `2`: Pending — under review, poll the deposit query endpoint
  * `3`: Rejected — rejected or failed (including cancelled)

  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/asset/travel-rule/deposit/submit HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672197227732  
    X-BAPI-RECV-WINDOW: 5000  
    X-BAPI-SIGN: XXXXX  
    Content-Type: application/json  
      
    {  
        "deposit_id": 1234567890,  
        "sub_account_id": 0,  
        "questionnaire": "{\"walletType\":0,\"vaspCode\":\"BINANCEUS_VASP\",\"legalType\":\"individual\",\"firstName\":\"John\",\"lastName\":\"Smith\",\"transactionPurpose\":\"Personal investment in long-term holdings\"}"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.submit_deposit_originator_info(  
        deposit_id=1234567890,  
        sub_account_id=0,  
        questionnaire='{"walletType":0,"vaspCode":"BINANCEUS_VASP","legalType":"individual","firstName":"John","lastName":"Smith","transactionPurpose":"Personal investment in long-term holdings"}',  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .submitDepositOriginatorInfo({  
        deposit_id: 1234567890,  
        sub_account_id: 0,  
        questionnaire: '{"walletType":0,"vaspCode":"BINANCEUS_VASP","legalType":"individual","firstName":"John","lastName":"Smith","transactionPurpose":"Personal investment in long-term holdings"}',  
      })  
      .then((response) => {  
        console.log(response);  
      })  
      .catch((error) => {  
        console.error(error);  
      });  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "travel_rule_status": 2  
        },  
        "retExtInfo": {},  
        "time": 1672197228408  
    }

---

# 提交入金發起人信息

當入金記錄觸發 Travel Rule 審核時，由用戶提交發起人（Originator）合規信息，供應商完成審核後返回結果狀態。

信息

當入金記錄命中合規策略且當前 `travel_rule_status` 為 `1`（待提交對手方信息）時調用本接口。

### HTTP 請求

POST`/v5/asset/travel-rule/deposit/submit`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
depositId| **true**|  integer| 入金記錄 ID，從入金查詢接口獲得，必須大於 `0`  
subAccountId| false| integer| Broker 場景：目標子帳號 UID。傳 `0` 或不傳表示當前帳號本人  
questionnaire| **true**|  string| Travel Rule 問卷信息，JSON 字符串，最大 16384 字節。不同合規區結構不同，詳見[問卷說明](/docs/zh-TW/v5/asset/withdraw/questionnaire)  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
travelRuleStatus| integer| Travel Rule 審核狀態 

  * `0`: Approved — 已通過，可繼續後續流程
  * `1`: CollectInfo — 需補充對手方信息，請重新提交問卷
  * `2`: Pending — 審核中，請輪詢入金查詢接口
  * `3`: Rejected — 已拒絕或失敗（含取消）

  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/asset/travel-rule/deposit/submit HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672197227732  
    X-BAPI-RECV-WINDOW: 5000  
    X-BAPI-SIGN: XXXXX  
    Content-Type: application/json  
      
    {  
        "depositId": 1234567890,  
        "subAccountId": 0,  
        "questionnaire": "{\"walletType\":0,\"vaspCode\":\"BINANCEUS_VASP\",\"legalType\":\"individual\",\"firstName\":\"John\",\"lastName\":\"Smith\",\"transactionPurpose\":\"Personal investment in long-term holdings\"}"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.submit_deposit_originator_info(  
        depositId=1234567890,  
        subAccountId=0,  
        questionnaire='{"walletType":0,"vaspCode":"BINANCEUS_VASP","legalType":"individual","firstName":"John","lastName":"Smith","transactionPurpose":"Personal investment in long-term holdings"}',  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .submitDepositOriginatorInfo({  
        depositId: 1234567890,  
        subAccountId: 0,  
        questionnaire: '{"walletType":0,"vaspCode":"BINANCEUS_VASP","legalType":"individual","firstName":"John","lastName":"Smith","transactionPurpose":"Personal investment in long-term holdings"}',  
      })  
      .then((response) => {  
        console.log(response);  
      })  
      .catch((error) => {  
        console.error(error);  
      });  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "travelRuleStatus": 2  
        },  
        "retExtInfo": {},  
        "time": 1672197228408  
    }