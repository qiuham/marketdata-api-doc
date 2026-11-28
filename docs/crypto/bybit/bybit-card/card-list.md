---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/bybit-card/card-list
api_type: REST
updated_at: 2026-11-28 18:48:33.236487
---

# Query Card List

Query the authenticated user's virtual and physical cards. By default, only non-final cards and cards being processed are returned.

tip

Only cards belonging to the authenticated user are returned.

The request body can be omitted or set to `{}`. Pagination parameters are not accepted.

### HTTP Request

POST`/v5/card/list`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
includeFinalCards| false| boolean| Whether to include cancelled and invalid cards. `true`: include final cards. Omitted, `false`, or `null`: use the default filtering  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
retCode| integer| Business return code. `0`: success; non-zero: failure  
retMsg| string| Return message  
result| object| Query result. `null` on failure  
> pageNo| integer| Current page number. Fixed at `1`  
> pageSize| integer| Number of cards returned  
> totalPage| integer| Total number of pages. Fixed at `1`  
> totalCount| integer| Total number of matching cards  
> data| array| Card list. Empty array when no cards match  
>> cardId| string| Card ID  
>> cardProductCode| integer| Card product code. Identifies the product together with `productId`  
>> productId| integer| Card product ID  
>> cardHolderName| string| Cardholder name printed on the card  
>> cardType| integer| Card type. `1`: Virtual card, `2`: Physical card  
>> maskedCardNumber| string| Masked card number  
>> pan6| string| Card number prefix, usually the first 6 digits  
>> pan4| string| Card number suffix, usually the last 4 digits  
>> cardExpireDate| string| Card expiry date, in `MM/yy` format  
>> cardCurrency| string| Card currency code  
>> status| integer| Card status. `0`: Undefined, `1`: Inactive, `2`: Active, `3`: Frozen, `4`: Banned, `5`: Cancelled, `6`: Invalid, `7`: Created  
>> subStatus| integer| Card sub-status code. Examples: `200`: Active, `300`: Regular freeze, `501`: Cancelled by user, `601`: Expired  
>> countryAlpha3| string| Country Alpha-3 code, e.g. `AUS`  
>> cardActivateTime| integer| Card activation time (Unix ms timestamp)  
>> createTime| integer| Card creation time (Unix ms timestamp)  
>> allowOnlineTransaction| boolean| Whether online transactions are allowed  
>> allowAtmWithdrawal| boolean| Whether ATM withdrawals are allowed  
>> supportedCurrencyList| array| List of supported currency codes. Entries can be `null`  
>> shippingInfo| object| Physical card shipping information. `null` for virtual cards  
>>> delvProvider| string| Delivery provider  
>>> trackingNo| string| Tracking number  
>>> shipmentTime| integer| Shipment time (Unix ms timestamp)  
>>> shippingStatus| string| Shipping status  
>>> shippingStatusDetail| string| Detailed shipping status  
>>> trackingUrl| string| Tracking URL  
>>> allowToChangeAddress| boolean| Whether the shipping address can be changed  
>>> deliverReminderCode| string| Delivery reminder code  
>> isGooglePayAvailable| boolean| Whether the product supports Google Pay. `false` when the configuration is missing  
>> isApplePayAvailable| boolean| Whether the product supports Apple Pay. `false` when the configuration is missing  
retExtInfo| object| Extended information. Defaults to `{}`  
time| integer| Response time (Unix ms timestamp)  
  
Card detail fields can be `null`, except `isGooglePayAvailable` and `isApplePayAvailable`, which are always returned as booleans. Shipping fields can be `null`; shipping addresses are not returned. Some physical cards without shipping records still return an object with empty fields.

### Error Codes

retCode| retMsg| Comments  
---|---|---  
913100000| SYSTEM ERROR| Request binding failure or system error  
  
Global error responses may omit `retExtInfo` and `time`.

* * *

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/card/list HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672211918471  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "includeFinalCards": true  
    }  
    
    
    
    import requests  
      
    url = "https://api-testnet.bybit.com/v5/card/list"  
    headers = {  
        "X-BAPI-API-KEY": "xxxxxxxxxxxxxxxxxx",  
        "X-BAPI-SIGN": "XXXXX",  
        "X-BAPI-TIMESTAMP": "1672211918471",  
        "X-BAPI-RECV-WINDOW": "5000"  
    }  
    body = {  
        "includeFinalCards": True  
    }  
    response = requests.post(url, headers=headers, json=body)  
    print(response.json())  
    
    
    
    const axios = require('axios');  
      
    const url = 'https://api-testnet.bybit.com/v5/card/list';  
    const headers = {  
      'X-BAPI-API-KEY': 'xxxxxxxxxxxxxxxxxx',  
      'X-BAPI-SIGN': 'XXXXX',  
      'X-BAPI-TIMESTAMP': '1672211918471',  
      'X-BAPI-RECV-WINDOW': '5000'  
    };  
    const body = { includeFinalCards: true };  
      
    axios.post(url, body, { headers })  
      .then(response => console.log(response.data))  
      .catch(error => console.error(error));  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "pageNo": 1,  
            "pageSize": 1,  
            "totalPage": 1,  
            "totalCount": 1,  
            "data": [  
                {  
                    "cardId": "180585395564494848",  
                    "cardProductCode": 1,  
                    "productId": 4,  
                    "cardHolderName": "TEST HOLDER",  
                    "cardType": 1,  
                    "maskedCardNumber": "539900******5497",  
                    "pan6": "539900",  
                    "pan4": "5497",  
                    "cardExpireDate": "12/29",  
                    "cardCurrency": "USD",  
                    "status": 2,  
                    "subStatus": 200,  
                    "countryAlpha3": "AUS",  
                    "cardActivateTime": 1672211918471,  
                    "createTime": 1672211918471,  
                    "allowOnlineTransaction": true,  
                    "allowAtmWithdrawal": true,  
                    "supportedCurrencyList": ["USD"],  
                    "shippingInfo": null,  
                    "isGooglePayAvailable": false,  
                    "isApplePayAvailable": false  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1672211918471  
    }

---

# 查詢卡片列表

查詢已認證用戶的虛擬卡與實體卡，一次返回全部符合條件的卡片。默認僅返回非終態卡及處理中的卡片。

提示

僅返回屬於已認證用戶本人的卡片

請求體可以省略或設為 `{}`，不接受分頁參數。

### HTTP 請求

POST`/v5/card/list`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
includeFinalCards| false| boolean| 是否包含已註銷及已失效的卡片。`true`: 包含終態卡；省略、`false` 或 `null`: 使用默認篩選條件  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
retCode| integer| 業務返回碼。`0`: 成功；非零: 失敗  
retMsg| string| 返回消息  
result| object| 查詢結果，失敗時為 `null`  
> pageNo| integer| 當前頁碼，固定為 `1`  
> pageSize| integer| 本次返回的卡片數量  
> totalPage| integer| 總頁數，固定為 `1`  
> totalCount| integer| 符合條件的卡片總數  
> data| array| 卡片列表，無符合條件的卡片時為空數組  
>> cardId| string| 卡片 ID  
>> cardProductCode| integer| 卡產品代碼，與 `productId` 共同標識產品  
>> productId| integer| 卡產品 ID  
>> cardHolderName| string| 卡面持卡人姓名  
>> cardType| integer| 卡片類型。`1`: 虛擬卡, `2`: 實體卡  
>> maskedCardNumber| string| 掩碼卡號  
>> pan6| string| 卡號前綴，通常為前 6 位  
>> pan4| string| 卡號後綴，通常為後 4 位  
>> cardExpireDate| string| 卡片有效期，格式為 `MM/yy`  
>> cardCurrency| string| 卡片幣種代碼  
>> status| integer| 卡主狀態。`0`: 未定義, `1`: 未激活, `2`: 已激活, `3`: 已凍結, `4`: 已封禁, `5`: 已註銷, `6`: 已失效, `7`: 已創建  
>> subStatus| integer| 卡子狀態碼。例如：`200`: 已激活, `300`: 常規凍結, `501`: 用戶註銷, `601`: 過期失效  
>> countryAlpha3| string| 國家 Alpha-3 代碼，例如 `AUS`  
>> cardActivateTime| integer| 卡片激活時間（Unix 毫秒時間戳）  
>> createTime| integer| 卡片創建時間（Unix 毫秒時間戳）  
>> allowOnlineTransaction| boolean| 是否允許線上交易  
>> allowAtmWithdrawal| boolean| 是否允許 ATM 取款  
>> supportedCurrencyList| array| 支持的幣種代碼列表，列表元素可以為 `null`  
>> shippingInfo| object| 實體卡配送信息，虛擬卡為 `null`  
>>> delvProvider| string| 配送服務商  
>>> trackingNo| string| 追蹤單號  
>>> shipmentTime| integer| 發貨時間（Unix 毫秒時間戳）  
>>> shippingStatus| string| 配送狀態  
>>> shippingStatusDetail| string| 配送詳細狀態  
>>> trackingUrl| string| 追蹤鏈接  
>>> allowToChangeAddress| boolean| 是否允許修改配送地址  
>>> deliverReminderCode| string| 配送提醒代碼  
>> isGooglePayAvailable| boolean| 產品是否支持 Google Pay，配置缺失時為 `false`  
>> isApplePayAvailable| boolean| 產品是否支持 Apple Pay，配置缺失時為 `false`  
retExtInfo| object| 擴展信息，默認為 `{}`  
time| integer| 響應時間（Unix 毫秒時間戳）  
  
卡片詳情字段可以為 `null`，但 `isGooglePayAvailable` 和 `isApplePayAvailable` 始終返回布爾值。配送字段可以為 `null`，不返回配送地址。部分實體卡無配送記錄時，仍返回字段為空的對象。

### 錯誤碼

retCode| retMsg| 說明  
---|---|---  
913100000| SYSTEM ERROR| 請求參數綁定失敗或系統異常  
  
全局異常響應可以缺少 `retExtInfo` 和 `time`。

* * *

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/card/list HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672211918471  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "includeFinalCards": true  
    }  
    
    
    
    import requests  
      
    url = "https://api-testnet.bybit.com/v5/card/list"  
    headers = {  
        "X-BAPI-API-KEY": "xxxxxxxxxxxxxxxxxx",  
        "X-BAPI-SIGN": "XXXXX",  
        "X-BAPI-TIMESTAMP": "1672211918471",  
        "X-BAPI-RECV-WINDOW": "5000"  
    }  
    body = {  
        "includeFinalCards": True  
    }  
    response = requests.post(url, headers=headers, json=body)  
    print(response.json())  
    
    
    
    const axios = require('axios');  
      
    const url = 'https://api-testnet.bybit.com/v5/card/list';  
    const headers = {  
      'X-BAPI-API-KEY': 'xxxxxxxxxxxxxxxxxx',  
      'X-BAPI-SIGN': 'XXXXX',  
      'X-BAPI-TIMESTAMP': '1672211918471',  
      'X-BAPI-RECV-WINDOW': '5000'  
    };  
    const body = { includeFinalCards: true };  
      
    axios.post(url, body, { headers })  
      .then(response => console.log(response.data))  
      .catch(error => console.error(error));  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "pageNo": 1,  
            "pageSize": 1,  
            "totalPage": 1,  
            "totalCount": 1,  
            "data": [  
                {  
                    "cardId": "180585395564494848",  
                    "cardProductCode": 1,  
                    "productId": 4,  
                    "cardHolderName": "TEST HOLDER",  
                    "cardType": 1,  
                    "maskedCardNumber": "539900******5497",  
                    "pan6": "539900",  
                    "pan4": "5497",  
                    "cardExpireDate": "12/29",  
                    "cardCurrency": "USD",  
                    "status": 2,  
                    "subStatus": 200,  
                    "countryAlpha3": "AUS",  
                    "cardActivateTime": 1672211918471,  
                    "createTime": 1672211918471,  
                    "allowOnlineTransaction": true,  
                    "allowAtmWithdrawal": true,  
                    "supportedCurrencyList": ["USD"],  
                    "shippingInfo": null,  
                    "isGooglePayAvailable": false,  
                    "isApplePayAvailable": false  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1672211918471  
    }