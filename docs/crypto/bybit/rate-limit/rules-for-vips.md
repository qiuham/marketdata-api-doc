---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/rate-limit/rules-for-vips
api_type: REST
updated_at: 2026-10-31 18:36:45.971289
---

# Get Referral Commission Records

Query referral commission records for the authenticated inviter.

info

  * Authentication is required. The inviter is identified from the API key; do not provide a user ID for the inviter in the request body.
  * `userId` in the response is a masked invitee ID.
  * An empty `userIdList` does not filter by invitee ID.
  * Time filters use `YYYY-MM-DD HH:mm:ss`. When either value cannot be parsed, an empty string is passed downstream; downstream handling is not established here. The endpoint does not apply a default past-week time range.
  * Request and response property names use the proto's explicit camelCase JSON names; actual gateway serialization has not been independently verified.



### HTTP Request

POST`/v5/referral/commission/records`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
userIdList| false| array| Invitee ID list. An empty list returns records without filtering by invitee ID.  
> userId| false| integer| Invitee ID  
startTime| false| string| Start time in `YYYY-MM-DD HH:mm:ss` format. An invalid value is passed downstream as an empty string; its handling is unverified.  
endTime| false| string| End time in `YYYY-MM-DD HH:mm:ss` format. An invalid value is passed downstream as an empty string; its handling is unverified.  
page| false| integer| One-based page number. `0` is treated as `1`.  
pageSize| false| integer| Number of records per page. `0` or a value greater than `200` is treated as `10`.  
productLine| false| integer| Product line: `0` unknown, `1` spot, `2` contracts, `3` options, `4` USDC perpetual, `6` TradeFi, `9` Alpha.  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
records| array| Referral commission records  
> userId| string| Masked invitee ID, in the format of first character + `***` \+ last character  
> paymentTime| integer| Commission payment time as a Unix timestamp in seconds  
> rate| string| Commission rate  
> businessUnit| integer| Product line: `0` unknown, `1` spot, `2` contracts, `3` options, `4` USDC perpetual, `6` TradeFi, `9` Alpha. Unrecognized values are returned as `0`.  
> commissionOriginCoin| string| Original commission currency  
> commissionOriginAmount| string| Commission amount in the original currency  
> commissionUsdtAmount| string| Commission value in USDT  
> commissionStatus| integer| Commission status: `0` unknown, `1` awaiting credit, `2` settled. Unrecognized values are returned as `0`.  
> isBoostM2| boolean| Whether the invitee associated with the commission is a Boost user. This field may not be present.  
total| integer| Total number of records  
  
### Request Example

  * HTTP


    
    
    POST /v5/referral/commission/records HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1753286400000  
    X-BAPI-RECV-WINDOW: 5000  
    X-BAPI-SIGN: XXXXX  
    Content-Type: application/json  
      
    {  
      "userIdList": [201, 202],  
      "startTime": "2025-03-01 10:20:30",  
      "endTime": "2025-03-08 11:22:33",  
      "page": 3,  
      "pageSize": 200,  
      "productLine": 1  
    }  
    

### Response Example

The following illustrates the field structure only; it is not a default ProtoJSON serialization or a gateway-validated response.
    
    
    {  
      "retCode": 0,  
      "retMsg": "",  
      "result": {  
        "records": [  
          {  
            "userId": "1***6",  
            "paymentTime": 1740916800,  
            "rate": "0.20",  
            "businessUnit": 1,  
            "commissionOriginCoin": "BTC",  
            "commissionOriginAmount": "1.25",  
            "commissionUsdtAmount": "250",  
            "commissionStatus": 2  
          }  
        ],  
        "total": 29  
      },  
      "retExtInfo": {},  
      "time": 1753286400000  
    }

---

# 查詢邀請返佣紀錄

查詢已驗證邀請人的邀請返佣紀錄。

信息

  * 需要鑑權。邀請人由 API Key 識別；請勿在請求體中傳入邀請人的使用者 ID。
  * 回應中的 `userId` 為已遮罩的受邀人 ID。
  * 空的 `userIdList` 不會按受邀人 ID 篩選。
  * 時間篩選使用 `YYYY-MM-DD HH:mm:ss`。任一值無法解析時，會將空字串傳至下游；下游如何處理尚未在此確認。此接口不會預設查詢過去一週。
  * 請求與回應的欄位名稱使用 Proto 明確定義的 camelCase JSON 名稱；實際閘道序列化尚未獨立驗證。



### HTTP請求

POST`/v5/referral/commission/records`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
userIdList| false| array| 受邀人 ID 列表。空列表不會按受邀人 ID 篩選。  
> userId| false| integer| 受邀人 ID  
startTime| false| string| 開始時間，格式為 `YYYY-MM-DD HH:mm:ss`。無效值會以空字串傳至下游；其處理方式尚未驗證。  
endTime| false| string| 結束時間，格式為 `YYYY-MM-DD HH:mm:ss`。無效值會以空字串傳至下游；其處理方式尚未驗證。  
page| false| integer| 頁碼，`0` 會視為 `1`。  
pageSize| false| integer| 每頁紀錄數。`0` 或大於 `200` 的值會視為 `10`。  
productLine| false| integer| 產品線：`0` 未知、`1` 現貨、`2` 合約、`3` 期權、`4` USDC 永續、`6` TradeFi、`9` Alpha。  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
records| array| 邀請返佣紀錄  
> userId| string| 已遮罩的受邀人 ID，格式為首字元 + `***` \+ 末字元  
> paymentTime| integer| 返佣支付時間，Unix 秒級時間戳  
> rate| string| 返佣比例  
> businessUnit| integer| 產品線：`0` 未知、`1` 現貨、`2` 合約、`3` 期權、`4` USDC 永續、`6` TradeFi、`9` Alpha。未識別值回傳 `0`。  
> commissionOriginCoin| string| 原始返佣幣種  
> commissionOriginAmount| string| 原始幣種的返佣金額  
> commissionUsdtAmount| string| 以 USDT 計價的返佣金額  
> commissionStatus| integer| 返佣狀態：`0` 未知、`1` 待入帳、`2` 已結算。未識別值回傳 `0`。  
> isBoostM2| boolean| 與該返佣關聯的受邀人是否為 Boost 使用者。此欄位可能不會出現。  
total| integer| 總紀錄數  
  
### 請求示例

  * HTTP


    
    
    POST /v5/referral/commission/records HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1753286400000  
    X-BAPI-RECV-WINDOW: 5000  
    X-BAPI-SIGN: XXXXX  
    Content-Type: application/json  
      
    {  
      "userIdList": [201, 202],  
      "startTime": "2025-03-01 10:20:30",  
      "endTime": "2025-03-08 11:22:33",  
      "page": 3,  
      "pageSize": 200,  
      "productLine": 1  
    }  
    

### 響應示例

以下僅示意欄位結構，並非預設 ProtoJSON 序列化結果，也未經閘道驗證。
    
    
    {  
      "retCode": 0,  
      "retMsg": "",  
      "result": {  
        "records": [{  
          "userId": "1***6",  
          "paymentTime": 1740916800,  
          "rate": "0.20",  
          "businessUnit": 1,  
          "commissionOriginCoin": "BTC",  
          "commissionOriginAmount": "1.25",  
          "commissionUsdtAmount": "250",  
          "commissionStatus": 2  
        }],  
        "total": 29  
      },  
      "retExtInfo": {},  
      "time": 1753286400000  
    }