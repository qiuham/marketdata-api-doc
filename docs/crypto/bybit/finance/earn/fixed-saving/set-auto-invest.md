---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/earn/fixed-saving/set-auto-invest
api_type: REST
updated_at: 2026-11-11 18:28:59.151832
---

# Get/Set Auto Savings Settings

Query or update Flexible Saving auto savings settings.

note

  * `GET` queries the auto savings switch, position limit, and APR.
  * `POST` enables or disables auto savings.



info

  * API key permission: `Earn`
  * Get Auto Savings Settings: 10 requests per second per UID
  * Set Auto Savings Settings: 5 requests per second per UID



## Get Auto Savings Settings

Query the user's Flexible Saving auto savings settings and current APR by coin. Omit `coins` to return all supported coins. You can specify up to 50 coins.

### HTTP Request

GET`/v5/earn/flexible-saving/auto-savings`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
coins| false| array| Coin names to query. Pass repeated query parameters, for example `coins=BTC&coins=ETH`. Omit to query all supported coins. Maximum: `50`  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
selectedAll| boolean| Whether auto savings is enabled globally  
coins| array| Supported or requested coins and their auto savings settings  
> coin| string| Coin name  
> isSelected| boolean| Whether auto savings is enabled for this coin  
> maxStakingAmount| string| Maximum auto savings position amount, expressed in this coin  
> apr| string| Current APR as a decimal rate. For example, `0.05` means 5%  
  
* * *

### Request Example
    
    
    GET /v5/earn/flexible-saving/auto-savings?coins=BTC&coins=ETH HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672211918471  
    X-BAPI-RECV-WINDOW: 5000  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "selectedAll": false,  
            "coins": [  
                {  
                    "coin": "BTC",  
                    "isSelected": true,  
                    "maxStakingAmount": "10",  
                    "apr": "0.05"  
                },  
                {  
                    "coin": "ETH",  
                    "isSelected": false,  
                    "maxStakingAmount": "100",  
                    "apr": "0.04"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1672211918471  
    }  
    

## Set Auto Savings Settings

Enable or disable Flexible Saving auto savings for one coin or all supported coins. Omit `coin` or pass an empty string to update the global setting.

When enabling, set `purchaseImmediately` to `true` to asynchronously subscribe the available Funding Account balance. When it is `false` or omitted, only the setting is updated. This parameter is ignored when disabling auto savings.

### HTTP Request

POST`/v5/earn/flexible-saving/auto-savings`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
coin| false| string| Coin to update. Omit or pass an empty string to update the global setting  
isSelected| **true**|  boolean| Whether to enable auto savings  
purchaseImmediately| false| boolean| When enabling, asynchronously subscribe the available Funding Account balance. Default: `false`. Ignored when disabling  
  
### Response Parameters

None

* * *

### Request Example
    
    
    POST /v5/earn/flexible-saving/auto-savings HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672211918471  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "coin": "BTC",  
        "isSelected": true,  
        "purchaseImmediately": false  
    }  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {},  
        "retExtInfo": {},  
        "time": 1672211918471  
    }

---

# 查詢/設定自動儲蓄設定

查詢或設定活期理財自動儲蓄。

備註

  * `GET` 查詢自動儲蓄開關、持倉上限及 APR。
  * `POST` 開啟或關閉自動儲蓄。



信息

  * API key 權限：`Earn`
  * 查詢自動儲蓄設定：每個 UID 每秒 10 次請求
  * 設定自動儲蓄設定：每個 UID 每秒 5 次請求



## 查詢自動儲蓄設定

查詢使用者的活期理財自動儲蓄設定及各幣種目前 APR。省略 `coins` 可回傳所有支援的幣種；最多可指定 50 個幣種。

### HTTP 請求

GET`/v5/earn/flexible-saving/auto-savings`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
coins| false| array| 欲查詢的幣種。以重複的查詢參數傳入，例如 `coins=BTC&coins=ETH`。省略時查詢所有支援的幣種。最多 `50` 個  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
selectedAll| boolean| 是否已全域啟用自動儲蓄  
coins| array| 支援或指定幣種的自動儲蓄設定  
> coin| string| 幣種名稱  
> isSelected| boolean| 是否已為此幣種啟用自動儲蓄  
> maxStakingAmount| string| 此幣種可進行自動儲蓄的最大持倉數量  
> apr| string| 目前 APR，以小數利率表示。例如 `0.05` 代表 5%  
  
* * *

### 請求示例
    
    
    GET /v5/earn/flexible-saving/auto-savings?coins=BTC&coins=ETH HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672211918471  
    X-BAPI-RECV-WINDOW: 5000  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "selectedAll": false,  
            "coins": [  
                {  
                    "coin": "BTC",  
                    "isSelected": true,  
                    "maxStakingAmount": "10",  
                    "apr": "0.05"  
                },  
                {  
                    "coin": "ETH",  
                    "isSelected": false,  
                    "maxStakingAmount": "100",  
                    "apr": "0.04"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1672211918471  
    }  
    

## 設定自動儲蓄設定

為單一幣種或所有支援的幣種啟用或停用活期理財自動儲蓄。省略 `coin` 或傳入空字串可更新全域設定。

啟用時，將 `purchaseImmediately` 設為 `true` 可非同步申購資金帳戶中的可用餘額。設定為 `false` 或省略時，僅會更新設定。停用自動儲蓄時，此參數會被忽略。

### HTTP 請求

POST`/v5/earn/flexible-saving/auto-savings`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
coin| false| string| 要更新的幣種。省略或傳入空字串可更新全域設定  
isSelected| **true**|  boolean| 是否啟用自動儲蓄  
purchaseImmediately| false| boolean| 啟用時，非同步申購資金帳戶中的可用餘額。預設：`false`。停用時會被忽略  
  
### 響應參數

無

* * *

### 請求示例
    
    
    POST /v5/earn/flexible-saving/auto-savings HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672211918471  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "coin": "BTC",  
        "isSelected": true,  
        "purchaseImmediately": false  
    }  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {},  
        "retExtInfo": {},  
        "time": 1672211918471  
    }