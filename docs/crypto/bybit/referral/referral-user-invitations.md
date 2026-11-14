---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/referral/referral-user-invitations
api_type: REST
updated_at: 2026-11-13 19:24:46.949797
---

# Get Referral User Invitations

Query invitation records for the authenticated referral user.

info

  * Authentication is required. The caller is identified from the API key; do not provide the caller's user ID in the request body.
  * An empty `userIdList` does not filter by invitee ID.
  * Time values use `YYYY-MM-DD HH:mm:ss`. Invalid or empty values are passed downstream as `0`; do not infer the final search window from this endpoint layer alone.
  * Request and response property names use the proto's explicit camelCase JSON names. Invitation records use this endpoint's dedicated payload; final gateway serialization, HTTP error behavior, and integer/enum representation remain unverified.



### HTTP Request

POST`/v5/referral/user/invitations`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
userIdList| false| array| Invitee ID list. An empty list does not apply an invitee-ID filter.  
> userId| false| integer| Invitee ID  
startTime| false| string| Query start time in `YYYY-MM-DD HH:mm:ss` format. Invalid or empty values are passed downstream as `0`.  
endTime| false| string| Query end time in `YYYY-MM-DD HH:mm:ss` format. Invalid or empty values are passed downstream as `0`.  
page| false| integer| Page number. `0` is treated as `1`.  
pageSize| false| integer| Number of records per page. `0` or a value greater than `200` is treated as `10`.  
friendStatus| false| integer| Invitee status. See [friendStatus](/docs/v5/enum#friendstatus).  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
records| array| Invitation records  
> userIdMask| string| Masked invitee ID  
> signTime| integer| Invitee registration timestamp  
> userStatus| integer| Invitee status. See [friendStatus](/docs/v5/enum#friendstatus).  
> totalCommission| string| Total commission amount, formatted to at most eight decimal places. Invalid source values cause an error.  
> userId| string| The invitee's unencrypted decimal user ID. `userIdMask` is supplied separately; confirm that exposing this value is intended.  
> taskProgress| string| Task completion progress  
> notShowCommission| boolean| `true` for some new EU-site invitees and non-Boost JPN-site invitees; the Boost path leaves the default `false`.  
> totalBaseRewards| string| Not populated by the current endpoint; remains the default empty string. Whether it appears in gateway JSON is unverified.  
total| integer| Total number of records  
  
### Request Example

  * HTTP


    
    
    POST /v5/referral/user/invitations HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1753286400000  
    X-BAPI-RECV-WINDOW: 5000  
    X-BAPI-SIGN: XXXXX  
    Content-Type: application/json  
      
    {  
      "userIdList": [],  
      "startTime": "2026-01-01 00:00:00",  
      "endTime": "2026-01-31 23:59:59",  
      "page": 1,  
      "pageSize": 10,  
      "friendStatus": 0  
    }  
    

### Response Example

The following illustrates the field structure only; it is not a default ProtoJSON serialization or a gateway-validated response.
    
    
    {  
      "retCode": 0,  
      "retMsg": "",  
      "result": {  
        "records": [],  
        "total": 0  
      }  
    }

---

# 查詢邀請使用者紀錄

查詢已驗證邀請使用者的邀請紀錄。

信息

  * 需要鑑權。呼叫者由 API Key 識別；請勿在請求體中傳入呼叫者的使用者 ID。
  * 空的 `userIdList` 不會按受邀人 ID 篩選。
  * 時間使用 `YYYY-MM-DD HH:mm:ss`。無效或空的值會以 `0` 傳至下游；請勿只根據此接口層推斷最終查詢時間範圍。
  * 請求與回應的欄位名稱使用 Proto 明確定義的 camelCase JSON 名稱。邀請紀錄使用本接口專用負載；最終閘道序列化、HTTP 錯誤行為及整數／列舉值的表示方式尚未驗證。



### HTTP請求

POST`/v5/referral/user/invitations`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
userIdList| false| array| 受邀人 ID 列表。空列表不會按受邀人 ID 篩選。  
> userId| false| integer| 受邀人 ID  
startTime| false| string| 開始時間，格式為 `YYYY-MM-DD HH:mm:ss`。無效或空值會以 `0` 傳至下游。  
endTime| false| string| 結束時間，格式為 `YYYY-MM-DD HH:mm:ss`。無效或空值會以 `0` 傳至下游。  
page| false| integer| 頁碼。`0` 會視為 `1`。  
pageSize| false| integer| 每頁紀錄數。`0` 或大於 `200` 的值會視為 `10`。  
friendStatus| false| integer| 受邀人狀態。請參閱 [friendStatus](/docs/zh-TW/v5/enum#friendstatus)。  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
records| array| 邀請紀錄  
> userIdMask| string| 已遮罩的受邀人 ID  
> signTime| integer| 受邀人註冊時間戳  
> userStatus| integer| 受邀人狀態。請參閱 [friendStatus](/docs/zh-TW/v5/enum#friendstatus)。  
> totalCommission| string| 累計返佣金額，最多保留八位小數。來源值無效時會發生錯誤。  
> userId| string| 受邀人未加密的十進位使用者 ID。另有 `userIdMask`；請確認是否應公開此值。  
> taskProgress| string| 任務完成進度  
> notShowCommission| boolean| 部分新 EU 站受邀人及非 Boost 的 JPN 站受邀人為 `true`；Boost 流程保留預設 `false`。  
> totalBaseRewards| string| 目前接口不會填入此欄位，維持預設空字串。其是否出現在閘道 JSON 中尚未驗證。  
total| integer| 總紀錄數  
  
### 請求示例

  * HTTP


    
    
    POST /v5/referral/user/invitations HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1753286400000  
    X-BAPI-RECV-WINDOW: 5000  
    X-BAPI-SIGN: XXXXX  
    Content-Type: application/json  
      
    {  
      "userIdList": [],  
      "startTime": "2026-01-01 00:00:00",  
      "endTime": "2026-01-31 23:59:59",  
      "page": 1,  
      "pageSize": 10,  
      "friendStatus": 0  
    }  
    

### 響應示例

以下僅示意欄位結構，並非預設 ProtoJSON 序列化結果，也未經閘道驗證。
    
    
    {  
      "retCode": 0,  
      "retMsg": "",  
      "result": {"records": [], "total": 0}  
    }