---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/rate-limit/rules-for-pros/introduction
api_type: REST
updated_at: 2026-11-11 18:29:40.485125
---

# Get Referral Campaign Rewards

Get the referral rules and configured campaign tasks and rewards for the current site. This endpoint returns static campaign configuration only; it does not return the user's task progress, reward claims, or payout records.

info

  * Authentication is required. The user and site are derived from the authenticated gateway context; do not provide a user ID or site selector in the request body.
  * The response envelope, `rebateRule`, and each embedded campaign JSON string use camelCase field names. Campaigns are returned in base, fiat, then earn order when active. Each `tasks` entry has `schemaVersion: 2`.
  * A reward-configuration lookup failure skips only that task. Other tasks and campaigns are retained.
  * `rebateRule` is site configuration and does not indicate the tier matched by the current user.



### HTTP Request

POST`/v5/referral/campaign/rewards`

### Request Parameters

No request parameters are required. Send an empty JSON object.

### Response Parameters

Parameter| Type| Comments  
---|---|---  
rebateRule| object| Referral rules configured for the site  
> depositAmount| integer| Deposit threshold. Currency and precision are not specified.  
> tradeAmount| integer| Trading threshold. Currency and precision are not specified.  
> rebateRatioRules| array| Tiered referral commission rules  
>> rebateRatio| integer| Referral commission rate, from 0 to 100  
>> referralCount| integer| Required number of qualified invitees  
>> hasTradeCondition| boolean| Whether the tier requires trading volume  
>> tradeAmountCondition| integer| Trading-volume threshold for the tier  
> rebateDurationDays| integer| Number of days that the referral commission lasts  
> tradefiDepositAmount| integer| Currently not populated; a default value of `0` does not confirm a threshold  
> tradefiTradeAmount| integer| Currently not populated; a default value of `0` does not confirm a threshold  
tasks| array| Campaign JSON strings, in base, fiat, then earn order. Parse each string to access the fields below.  
> schemaVersion| integer| Campaign JSON schema version. The current value is always `2`.  
> source| string| Campaign source: `base`, `fiat`, or `earn`  
> campaignId| string| Campaign configuration ID; not a user reward-record ID  
> tasks| array| Configured tasks and one-hop M1/M2 related tasks. May be empty if task details cannot be assembled.  
>> id| integer| Task ID  
>> awardType| integer| Task reward type. See [awardType](/docs/v5/enum#awardtype). Type `100` retrieves reward-packet details; reward details are not currently assembled for types `95` and `97`. This value does not mean that a reward has been claimed.  
>> ruleTitle| array | null| English title of each valid rule. `null` when there are no valid rules.  
>> ruleDescription| array | null| English description of each valid rule. Corresponds to `ruleTitle` by index.  
>> ruleParam| array | null| First parameter of each valid rule. Corresponds to `ruleTitle` by index.  
>> taskAwards| array| Rewards for completing the task  
>> m1Awards| array| M1 rewards with `UserRelateType=REFERRAL`  
>>> id| integer| Regular reward ID or reward packet ID  
>>> name| string| English reward name. Reward packets use `UP TO &lt;value_usd&gt;` or `EARN &lt;value_usd&gt;`.  
>>> type| string| English reward type. Always `Packet` for reward packets.  
>>> productLine| string| English product type. Empty for reward packets.  
>>> startTime| string| Start time in UTC RFC 3339 format. Empty when unavailable or for reward packets.  
>>> endTime| string| End time in UTC RFC 3339 format. Empty when unavailable.  
  
### Request Example

  * HTTP


    
    
    POST /v5/referral/campaign/rewards HTTP/1.1  
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
      "retMsg": "",  
      "result": {  
        "rebateRule": {  
          "depositAmount": 0,  
          "tradeAmount": 0,  
          "rebateRatioRules": [],  
          "rebateDurationDays": 30  
        },  
        "tasks": [  
          "{\"schemaVersion\":2,\"source\":\"base\",\"campaignId\":\"sample\",\"tasks\":[{\"id\":7,\"awardType\":100,\"ruleTitle\":[\"Deposit\"],\"ruleDescription\":[\"Deposit $100\"],\"ruleParam\":[\"100\"],\"taskAwards\":[{\"id\":92,\"name\":\"EARN 10\",\"type\":\"Packet\",\"productLine\":\"\",\"startTime\":\"\",\"endTime\":\"\"}],\"m1Awards\":[]}]}"  
        ]  
      },  
      "retExtInfo": {},  
      "time": 1753286400000  
    }

---

# 查詢邀請活動獎勵

查詢目前站點的邀請規則、已設定的活動任務與獎勵。本接口僅回傳靜態活動設定，不會回傳使用者任務進度、獎勵領取或支付紀錄。

信息

  * 需要鑑權。使用者與站點由已驗證的閘道上下文識別；請勿在請求體中傳入使用者 ID 或站點選擇器。
  * 響應封套、`rebateRule` 與每個內嵌活動 JSON 字串皆使用 camelCase 欄位名稱。若有啟用中的活動，會依 base、fiat、earn 順序回傳。每個 `tasks` 元素皆帶有 `schemaVersion: 2`。
  * 若某任務的獎勵設定查詢失敗，只會略過該任務；其他任務與活動仍會保留。
  * `rebateRule` 為站點設定，不代表目前使用者實際符合的層級。



### HTTP請求

POST`/v5/referral/campaign/rewards`

### 請求參數

無需請求參數。請傳送空的 JSON 物件。

### 響應參數

參數| 類型| 說明  
---|---|---  
rebateRule| object| 站點設定的邀請規則  
> depositAmount| integer| 入金門檻；幣種與精度未指定。  
> tradeAmount| integer| 交易門檻；幣種與精度未指定。  
> rebateRatioRules| array| 分層邀請返佣規則  
>> rebateRatio| integer| 邀請返佣比例，範圍為 0 至 100  
>> referralCount| integer| 所需符合資格的受邀人數  
>> hasTradeCondition| boolean| 該層級是否要求交易量  
>> tradeAmountCondition| integer| 該層級的交易量門檻  
> rebateDurationDays| integer| 邀請返佣持續天數  
> tradefiDepositAmount| integer| 目前未填入；預設值 `0` 不代表已確認門檻。  
> tradefiTradeAmount| integer| 目前未填入；預設值 `0` 不代表已確認門檻。  
tasks| array| 活動 JSON 字串，依 base、fiat、earn 順序排列。請解析每個字串以取得以下欄位。  
> schemaVersion| integer| 活動 JSON schema 版本；目前固定為 `2`。  
> source| string| 活動來源：`base`、`fiat` 或 `earn`  
> campaignId| string| 活動設定 ID，不是使用者獎勵紀錄 ID。  
> tasks| array| 已設定任務及一層 M1/M2 關聯任務。任務資訊無法組裝時可能為空。  
>> id| integer| 任務 ID  
>> awardType| integer| 任務獎勵類型。請參閱 [awardType](/docs/zh-TW/v5/enum#awardtype)。類型 `100` 會查詢獎勵包詳細資料；目前不會組裝類型 `95` 與 `97` 的獎勵詳細資料。此值不代表獎勵已被領取。  
>> ruleTitle| array | null| 每項有效規則的英文標題；沒有有效規則時為 `null`。  
>> ruleDescription| array | null| 每項有效規則的英文描述，索引與 `ruleTitle` 相對應。  
>> ruleParam| array | null| 每項有效規則的第一個參數，索引與 `ruleTitle` 相對應。  
>> taskAwards| array| 完成該任務的獎勵  
>> m1Awards| array| `UserRelateType=REFERRAL` 的 M1 獎勵  
>>> id| integer| 一般獎勵 ID 或獎勵包 ID  
>>> name| string| 英文獎勵名稱；獎勵包使用 `UP TO &lt;value_usd&gt;` 或 `EARN &lt;value_usd&gt;`。  
>>> type| string| 英文獎勵類型；獎勵包固定為 `Packet`。  
>>> productLine| string| 英文產品類型；獎勵包為空字串。  
>>> startTime| string| UTC RFC 3339 格式開始時間；沒有資料或獎勵包時為空字串。  
>>> endTime| string| UTC RFC 3339 格式結束時間；沒有資料時為空字串。  
  
### 請求示例

  * HTTP


    
    
    POST /v5/referral/campaign/rewards HTTP/1.1  
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
      "retMsg": "",  
      "result": {  
        "rebateRule": {  
          "depositAmount": 0,  
          "tradeAmount": 0,  
          "rebateRatioRules": [],  
          "rebateDurationDays": 30  
        },  
        "tasks": [  
          "{\"schemaVersion\":2,\"source\":\"base\",\"campaignId\":\"sample\",\"tasks\":[{\"id\":7,\"awardType\":100,\"ruleTitle\":[\"Deposit\"],\"ruleDescription\":[\"Deposit $100\"],\"ruleParam\":[\"100\"],\"taskAwards\":[{\"id\":92,\"name\":\"EARN 10\",\"type\":\"Packet\",\"productLine\":\"\",\"startTime\":\"\",\"endTime\":\"\"}],\"m1Awards\":[]}]}"  
        ]  
      },  
      "retExtInfo": {},  
      "time": 1753286400000  
    }