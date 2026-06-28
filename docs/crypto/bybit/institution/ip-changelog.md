---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/institution/ip-changelog
api_type: REST
updated_at: 2026-05-27 19:18:10.657943
---

# Get Institution IP Change Log

info

This endpoint must be requested with a main account API key.

### HTTP Request

GET`/v5/ins/ip/changelog`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
startTime| false| string| Filter start time, Unix timestamp in milliseconds  
endTime| false| string| Filter end time, Unix timestamp in milliseconds  
limit| false| integer| Records per page. Range: [1, 50]. Default: 20  
cursor| false| string| Pagination cursor. Use the `nextPageCursor` value from the previous response  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array| Array of IP change records  
> operationType| string| Action type: `ADD`, `REMOVE`, `ENABLE`, or `DISABLE`  
> ipAddress| string| The IP address affected by the operation  
> domainType| string| Connection protocol. `GW` for HTTP hostname, `WS` for WebSocket hostname  
> operator| string| Internal team member who performed the operation  
> createdAt| string| Operation timestamp in UTC+0, ISO 8601 format  
nextPageCursor| string| Opaque token for retrieving the next page of results  
  
### Request Example

  * HTTP


    
    
    GET /v5/ins/ip/changelog?limit=3 HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1779362662315  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "list": [  
                {  
                    "operationType": "DISABLE",  
                    "ipAddress": "193.118.167.247",  
                    "domainType": "WS",  
                    "operator": "wood.liang1",  
                    "createdAt": "2026-05-21T06:02:36Z"  
                },  
                {  
                    "operationType": "DISABLE",  
                    "ipAddress": "18.99.43.128/25",  
                    "domainType": "WS",  
                    "operator": "wood.liang1",  
                    "createdAt": "2026-05-21T06:02:36Z"  
                }  
            ],  
            "nextPageCursor": "eyJpZCI6NDE0LCJjcmVhdGVkQXQiOiIyMDI2LTA1LTIxVDA2OjAyOjM2In0="  
        },  
        "time": 1779362027705  
    }

---

# 查詢機構 IP 變更記錄

信息

此接口必須使用主帳戶 API key 請求。

### HTTP 請求

GET`/v5/ins/ip/changelog`

### 請求參數

參數| 是否必填| 類型| 說明  
---|---|---|---  
startTime| false| string| 篩選起始時間，Unix 毫秒時間戳  
endTime| false| string| 篩選結束時間，Unix 毫秒時間戳  
limit| false| integer| 每頁記錄數。範圍: [1, 50]。預設: 20  
cursor| false| string| 分頁游標。使用上一頁響應中的 `nextPageCursor` 值  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
list| array| IP 變更記錄列表  
> operationType| string| 操作類型: `ADD`, `REMOVE`, `ENABLE`, 或 `DISABLE`  
> ipAddress| string| 受該操作影響的 IP 位址  
> domainType| string| 連接協議。`GW` 表示 HTTP hostname，`WS` 表示 WebSocket hostname  
> operator| string| 執行該操作的內部團隊成員  
> createdAt| string| 操作時間戳，UTC+0，ISO 8601 格式  
nextPageCursor| string| 用於查詢下一頁的不透明 token  
  
### 請求示例

  * HTTP


    
    
    GET /v5/ins/ip/changelog?limit=3 HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1779362662315  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "list": [  
                {  
                    "operationType": "DISABLE",  
                    "ipAddress": "193.118.167.247",  
                    "domainType": "WS",  
                    "operator": "wood.liang1",  
                    "createdAt": "2026-05-21T06:02:36Z"  
                },  
                {  
                    "operationType": "DISABLE",  
                    "ipAddress": "18.99.43.128/25",  
                    "domainType": "WS",  
                    "operator": "wood.liang1",  
                    "createdAt": "2026-05-21T06:02:36Z"  
                }  
            ],  
            "nextPageCursor": "eyJpZCI6NDE0LCJjcmVhdGVkQXQiOiIyMDI2LTA1LTIxVDA2OjAyOjM2In0="  
        },  
        "time": 1779362027705  
    }