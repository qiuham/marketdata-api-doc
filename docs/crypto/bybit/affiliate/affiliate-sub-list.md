---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/affiliate/affiliate-sub-list
api_type: REST
updated_at: 2026-11-13 19:21:00.905528
---

# Get Affiliate Sub-Affiliate List

To use this endpoint, you should have an affiliate account and only tick "affiliate" permission while creating the API key.  
Affiliate site: <https://affiliates.bybit.com>

tip

  * Use master UID only
  * The api key can only have "Affiliate" permission



### HTTP Request

GET`/v5/affiliate/affiliate-sub-list`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
cursor| false| string| Cursor. Use the `nextPageCursor` token from the response to retrieve the next page of the result set  
size| false| integer| Limit for data size per page. [`0`, `100`]. Default: `0`  
startDate| false| string| Start date of the query period, format `YYYY-MM-DD`. The range between "startDate" and "endTime" cannot exceed 3 months  
endDate| false| string| End date of the query period, format `YYYY-MM-DD`. "startDate" and "endDate" must either both be provided or both be omitted. If both are omitted, it returns T-1 data by default  
subAffId| false| integer| Sub-affiliate ID for exact lookup. Pass `0` or omit to return all sub-affiliates without filtering  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array| Object  
> subAffId| string| Sub-affiliate ID  
> userId| string| Sub-affiliate UID  
> name| string| Sub-affiliate account nickname  
> email| string| Sub-affiliate email address (partially masked)  
> commissionsVol| json| Commission amount per currency for the queried date range (fixed five currencies: BTC / ETH / MNT / USDC / USDT)  
> commissionsForUsdt| string| Total commission converted to USDT for the queried date range  
> becameAffTime| string| Time when this user became a sub-affiliate, format `YYYY-MM-DD HH:mm:ss` (UTC)  
> startDate| string| Query start time echoed from the request parameters, format `YYYY-MM-DD HH:mm:ss`  
> endDate| string| Query end time echoed from the request parameters, format `YYYY-MM-DD HH:mm:ss`  
nextPageCursor| string| Refer to the `cursor` request parameter  
  
* * *

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/affiliate/affiliate-sub-list?cursor=&size=100&startDate=2024-01-01&endDate=2024-01-31 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1706745600000  
    X-BAPI-RECV-WINDOW: 5000  
    X-BAPI-SIGN: xxxxxx  
    Content-Type: application/json  
    
    
    
      
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "list": [  
                {  
                    "subAffId": "10001",  
                    "userId": "123456789",  
                    "name": "sub_affiliate_nick",  
                    "email": "sub***@example.com",  
                    "commissionsVol": {  
                        "BTC": "0.005",  
                        "ETH": "0.2",  
                        "MNT": "40.0",  
                        "USDC": "100.0",  
                        "USDT": "400.0"  
                    },  
                    "commissionsForUsdt": "550.00",  
                    "becameAffTime": "2023-06-01 10:00:00",  
                    "startDate": "2024-01-01 00:00:00",  
                    "endDate": "2024-01-31 23:59:59"  
                }  
            ],  
            "nextPageCursor": "eyJsYXN0SWQiOiIxMDAwMSJ9"  
        },  
        "retExtInfo": {},  
        "time": 1706745600000  
    }

---

# 查詢子代理列表

要使用此接口，您应该有一个代理商账户，并且在创建 API 密钥时仅勾选"代理商"权限。  
代理商網站: <https://affiliates.bybit.com>

提示

  * 僅支持使用母帳戶uid
  * 若要查詢該接口, api key僅能擁有代理商權限, 若擁有任何其他權限想, 請移除



### HTTP 請求

GET`/v5/affiliate/affiliate-sub-list`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
cursor| false| string| 游標，用於翻頁  
size| false| integer| 每頁數量限制. [`0`, `100`]. 默認: `0`  
startDate| false| string| 查詢時段開始日期，格式為 `YYYY-MM-DD`，開始時間和結束時間跨度最大為3個月  
endDate| false| string| 查詢時段結束日期，格式為 `YYYY-MM-DD`，開始時間和結束時間要麼同時傳入要麼都不傳，當都不傳時，默認返回T-1的數據  
subAffId| false| integer| 子代理 ID，用於精確查詢。傳入 `0` 或不傳則返回所有子代理  
  
### 返回參數

參數| 類型| 說明  
---|---|---  
list| array| Object  
> subAffId| string| 子代理 ID  
> userId| string| 子代理帳戶 uid  
> name| string| 子代理帳戶暱稱  
> email| string| 子代理電子郵件地址（部分遮蔽）  
> commissionsVol| json| 查詢時段內各幣種佣金金額（固定五種幣種：BTC / ETH / MNT / USDC / USDT）  
> commissionsForUsdt| string| 查詢時段內佣金總額折算為 USDT  
> becameAffTime| string| 該用戶成為子代理的時間，格式為 `YYYY-MM-DD HH:mm:ss`（UTC）  
> startDate| string| 從請求參數回傳的查詢起始時間，格式為 `YYYY-MM-DD HH:mm:ss`  
> endDate| string| 從請求參數回傳的查詢結束時間，格式為 `YYYY-MM-DD HH:mm:ss`  
nextPageCursor| string| 游標，用於翻頁  
  
* * *

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/affiliate/affiliate-sub-list?cursor=&size=100&startDate=2024-01-01&endDate=2024-01-31 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1706745600000  
    X-BAPI-RECV-WINDOW: 5000  
    X-BAPI-SIGN: xxxxxx  
    Content-Type: application/json  
    
    
    
      
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "list": [  
                {  
                    "subAffId": "10001",  
                    "userId": "123456789",  
                    "name": "sub_affiliate_nick",  
                    "email": "sub***@example.com",  
                    "commissionsVol": {  
                        "BTC": "0.005",  
                        "ETH": "0.2",  
                        "MNT": "40.0",  
                        "USDC": "100.0",  
                        "USDT": "400.0"  
                    },  
                    "commissionsForUsdt": "550.00",  
                    "becameAffTime": "2023-06-01 10:00:00",  
                    "startDate": "2024-01-01 00:00:00",  
                    "endDate": "2024-01-31 23:59:59"  
                }  
            ],  
            "nextPageCursor": "eyJsYXN0SWQiOiIxMDAwMSJ9"  
        },  
        "retExtInfo": {},  
        "time": 1706745600000  
    }