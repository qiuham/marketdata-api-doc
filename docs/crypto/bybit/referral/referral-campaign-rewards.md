---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/referral/referral-campaign-rewards
api_type: REST
updated_at: 2026-10-26 18:59:14.651350
---

# Get Referral User Identity Profile

Get the authenticated user's referral identity, relationship indicators, and available commission information.

info

  * Authentication is required. The user ID is derived from the API key; do not provide a user ID in the request body.
  * If the user is an affiliate, `isAffiliate` is `true` and M1 inviter status is not queried.
  * `inviterAffiliateUserId` and `inviterUserId` are relationship indicators: `1` when the respective record exists and `0` otherwise; they are not user IDs. The relationships are queried independently, and missing records are not errors.
  * `commissionInfo` is returned only when an M1 inviter record's user ID matches the authenticated user and the commission query succeeds. It uses this endpoint's dedicated commission-info payload; its fields copy the source commission result and may therefore be `0` when the source value is `0`.
  * Request and response property names use the proto's explicit camelCase JSON names. Actual gateway serialization, including int64 and enum representation, has not been independently verified.



### HTTP Request

POST`/v5/referral/user/identity-profile`

### Request Parameters

No request parameters are required. Send an empty JSON object.

### Response Parameters

Parameter| Type| Comments  
---|---|---  
isAffiliate| boolean| Whether the current user is an affiliate  
isM1| boolean| Whether the current user is an M1 inviter. This is checked only when the user is not an affiliate.  
inviterAffiliateId| integer| Affiliate ID from the affiliate direct-customer relationship. `0` if no relationship is found.  
inviterAffiliateUserId| integer| Affiliate direct-customer relationship indicator: `1` when a record exists, otherwise `0`. This is not the affiliate user's actual ID.  
inviterUserId| integer| Invitation relationship indicator: `1` when a record exists for the current user as invitee, otherwise `0`. This is not the inviter's actual ID.  
commissionInfo| object| Commission information for this endpoint. Returned only when a matching M1 inviter record and commission data are available.  
> totalCommission| string| Total accumulated commission amount  
> yesterdayCommission| string| Commission amount earned yesterday  
> totalFriends| integer| Total number of invited friends  
> qualifiedFriends| integer| Number of invitees eligible for commission  
> walletBalance| string| Commission wallet balance  
> qualifiedFriendsQuarterTotalTradeVolume| string| Current-quarter trading volume of qualified invitees  
> curQuarterActiveFriendsCount| integer| Number of active invitees in the current quarter. Copied from the source commission result and may be `0` when the source value is `0`.  
> hasOldReferral| integer| Legacy referral-commission programme indicator  
> degradeType| integer| Commission downgrade status: `0` unknown or not downgraded, `1` downgraded due to active invitee count, `2` downgraded due to invitee trading volume.  
> commissionRate| string| Current commission rate  
> upgradeUnifiedAccount| integer| Unified Trading Account status: `0` unknown, `1` upgraded, `2` upgrading, `3` not upgraded.  
> withdrawalSwitch| integer| Commission withdrawal switch: `1` enabled, `2` disabled. Copied from the source commission result and may be `0` when the source value is `0`.  
> lastQuarterQualifiedFriendsCount| integer| Number of qualified invitees in the previous quarter. Copied from the source commission result and may be `0` when the source value is `0`.  
  
### Request Example

  * HTTP


    
    
    POST /v5/referral/user/identity-profile HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1753286400000  
    X-BAPI-RECV-WINDOW: 5000  
    X-BAPI-SIGN: XXXXX  
    Content-Type: application/json  
      
    {}  
    

### Response Example
    
    
    {  
      "retCode": 0,  
      "retMsg": "OK",  
      "result": {  
        "isAffiliate": false,  
        "isM1": false,  
        "inviterAffiliateId": 0,  
        "inviterAffiliateUserId": 0,  
        "inviterUserId": 0  
      },  
      "retExtInfo": {},  
      "time": 1672211918471  
    }

---

# 查詢邀請使用者身分資料

查詢已驗證使用者的邀請身分、關係標識與可用返佣資訊。

信息

  * 需要鑑權。使用者 ID 由 API Key 識別；請勿在請求體中傳入使用者 ID。
  * 若使用者為代理商，`isAffiliate` 為 `true`，且不會查詢 M1 邀請人狀態。
  * `inviterAffiliateUserId` 與 `inviterUserId` 為關係標識：存在相應紀錄時為 `1`，否則為 `0`；它們不是使用者 ID。兩種關係會分別查詢，找不到紀錄不視為錯誤。
  * 僅在 M1 邀請人紀錄的使用者 ID 與已驗證使用者相符，且返佣查詢成功時，才會回傳 `commissionInfo`。它使用本接口專用的返佣資訊負載；欄位複製自來源返佣結果，因此來源值為 `0` 時也可能為 `0`。
  * 請求與回應的欄位名稱使用 Proto 明確定義的 camelCase JSON 名稱；實際閘道序列化（包括 int64 與列舉值的表示）尚未獨立驗證。



### HTTP請求

POST`/v5/referral/user/identity-profile`

### 請求參數

無需請求參數。請傳送空的 JSON 物件。

### 響應參數

參數| 類型| 說明  
---|---|---  
isAffiliate| boolean| 目前使用者是否為代理商  
isM1| boolean| 目前使用者是否為 M1 邀請人。僅在使用者不是代理商時查詢。  
inviterAffiliateId| integer| 代理商直客關係中的代理商 ID。找不到關係時為 `0`。  
inviterAffiliateUserId| integer| 代理商直客關係標識：存在紀錄時為 `1`，否則為 `0`。這不是代理商使用者的實際 ID。  
inviterUserId| integer| 邀請關係標識：目前使用者作為受邀人時若存在紀錄則為 `1`，否則為 `0`。這不是邀請人的實際 ID。  
commissionInfo| object| 本接口的返佣資訊。僅在可取得相符的 M1 邀請人紀錄及返佣資料時回傳。  
> totalCommission| string| 累計返佣金額  
> yesterdayCommission| string| 昨日取得的返佣金額  
> totalFriends| integer| 累計受邀好友數  
> qualifiedFriends| integer| 符合返佣資格的受邀人數  
> walletBalance| string| 返佣錢包餘額  
> qualifiedFriendsQuarterTotalTradeVolume| string| 本季符合資格受邀人的交易量  
> curQuarterActiveFriendsCount| integer| 本季活躍受邀人數。複製自來源返佣結果，來源值為 `0` 時可能為 `0`。  
> hasOldReferral| integer| 舊版邀請返佣計畫標識  
> degradeType| integer| 返佣降級狀態：`0` 未知或未降級、`1` 因活躍受邀人數降級、`2` 因受邀人交易量降級。  
> commissionRate| string| 目前返佣比例  
> upgradeUnifiedAccount| integer| 統一交易帳戶狀態：`0` 未知、`1` 已升級、`2` 升級中、`3` 未升級。  
> withdrawalSwitch| integer| 返佣提現開關：`1` 開啟、`2` 關閉。複製自來源返佣結果，來源值為 `0` 時可能為 `0`。  
> lastQuarterQualifiedFriendsCount| integer| 上季符合資格的受邀人數。複製自來源返佣結果，來源值為 `0` 時可能為 `0`。  
  
### 請求示例

  * HTTP


    
    
    POST /v5/referral/user/identity-profile HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1753286400000  
    X-BAPI-RECV-WINDOW: 5000  
    X-BAPI-SIGN: XXXXX  
    Content-Type: application/json  
      
    {}  
    

### 響應示例
    
    
    {  
      "retCode": 0,  
      "retMsg": "OK",  
      "result": {  
        "isAffiliate": false,  
        "isM1": false,  
        "inviterAffiliateId": 0,  
        "inviterAffiliateUserId": 0,  
        "inviterUserId": 0  
      },  
      "retExtInfo": {},  
      "time": 1672211918471  
    }