---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/tax/batch-create
api_type: REST
updated_at: 2026-10-18 18:45:55.345660
---

# Get Batch Export Report Status

Query the status and download URL of every task in a batch using the `batchId` returned by [Batch Request Export Reports](/docs/v5/tax/batch-create).

info

  * Rate limit: **20 requests per second** , per UID and endpoint.
  * The recommended polling interval is **30 seconds**.
  * The batch must be accessible to the authenticated user.
  * When a task's `status` is `2`, its `url` contains a JSON-encoded string with `Basepath` and `Files`. For all other statuses, `url` is an empty string.
  * The batch has finished processing when every task has status `2` (succeeded) or `-1` (failed). Check each task's status to determine whether its report was generated successfully.



### HTTP Request

GET `/v5/fht/compliance/tax/private/batch_query`

### Request Parameters

Pass the parameter in the query string.

Parameter| Required| Type| Comments  
---|---|---|---  
batchId| **true**|  string| Batch ID in UUID format, returned by [Batch Request Export Reports](/docs/v5/tax/batch-create).  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
items| array| List of task objects in the batch.  
> type| string| Report type. See [supported report types](/docs/v5/tax/batch-create#report-types).  
> number| string| Report subcategory number, used together with `type`.  
> status| integer (int32)| 

  * `0`: Queued
  * `1`: Processing
  * `2`: Succeeded
  * `-1`: Failed

  
> url| string| Download URL. Populated when `status` is `2`; otherwise, an empty string. URL of files (Basepath + Files). To shorten the time it takes to generate the report, it could generate multiple files. _Do take note of this and combine the several files using the same base path when requesting the data export_  
> queryId| string| Report generation query ID for the task. Populated while the task is processing or after completion.  
  
### Request Example
    
    
    GET /v5/fht/compliance/tax/private/batch_query?batchId=b5f4a3e2-1c8d-4f96-9a03-2e7b8c6d4f10 HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN-TYPE: 2  
    X-BAPI-SIGN: xxxxxxxxxxxxxx  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1790035230000  
    X-BAPI-RECV-WINDOW: 5000  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "items": [  
                {  
                    "type": "TRADE",  
                    "number": "1",  
                    "status": 2,  
                    "url": "{\"Basepath\":\"https://prod-bybit-tax-api-1705-rz.s3.ap-southeast-1.amazonaws.com/\",\"Files\":[\"20260929/6b1b3341-6940-47a7-b112-5949e496736f/_SUCCESS\",\"20260929/6b1b3341-6940-47a7-b112-5949e496736f/part-00000-92859919-c8bf-47ce-b349-9cdcf44e8045-c000.csv\",\"20260929/6b1b3341-6940-47a7-b112-5949e496736f/part-00997-92859919-c8bf-47ce-b349-9cdcf44e8045-c000.csv\"]}",  
                    "queryId": "2104839833489960960"  
                },  
                {  
                    "type": "EARN",  
                    "number": "1",  
                    "status": 2,  
                    "url": "{\"Basepath\":\"https://prod-bybit-tax-api-1705-rz.s3.ap-southeast-1.amazonaws.com/\",\"Files\":[\"20260929/d64081bf-955b-4a96-b2f9-aa2f49760611/_SUCCESS\",\"20260929/d64081bf-955b-4a96-b2f9-aa2f49760611/part-00000-0f0a3b1a-cdd3-43d0-8afa-1159893220a8-c000.csv\",\"20260929/d64081bf-955b-4a96-b2f9-aa2f49760611/part-00001-0f0a3b1a-cdd3-43d0-8afa-1159893220a8-c000.csv\"]}",  
                    "queryId": "2104839833871642624"  
                },  
                {  
                    "type": "DEPOSIT&WITHDRAWAL",  
                    "number": "1",  
                    "status": 2,  
                    "url": "{\"Basepath\":\"https://prod-bybit-tax-api-1705-rz.s3.ap-southeast-1.amazonaws.com/\",\"Files\":[\"20260929/db47d025-ba66-4dee-98b8-8860d891fdb9/_SUCCESS\",\"20260929/db47d025-ba66-4dee-98b8-8860d891fdb9/part-00000-a8f75a9b-637f-4865-af11-5e4609e4a415-c000.csv\"]}",  
                    "queryId": "2104839834236547072"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1790669270665  
    }  
    

### Error Codes

See [Tax Error Codes](/docs/v5/error#tax).

---

# 查詢批量報告導出狀態

使用[批量創建導出報告請求](/docs/zh-TW/v5/tax/batch-create)返回的 `batchId`，查詢該批次內所有子任務的狀態及下載地址。

信息

  * 限流：每個 UID 每個接口 **20 次/秒** 。
  * 建議每 **30 秒** 輪詢一次。
  * 當前已認證用戶必須有權訪問該批次。
  * 子任務的 `status` 為 `2` 時，`url` 返回包含 `Basepath` 和 `Files` 的 JSON 字符串；其他狀態下，`url` 為空字符串。
  * 所有子任務的狀態均為 `2`（成功）或 `-1`（失敗）時，該批次處理完成。請逐項檢查狀態，確認報告是否成功生成。



### HTTP 請求

GET `/v5/fht/compliance/tax/private/batch_query`

### 請求參數

通過 URL 查詢字符串傳入參數。

參數| 是否必需| 類型| 說明  
---|---|---|---  
batchId| **true**|  string| [批量創建導出報告請求](/docs/zh-TW/v5/tax/batch-create)返回的批次 ID，格式為 UUID。  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
items| array| 批次內的子任務對象列表。  
> type| string| 報告類型，參見[支持的報告類型](/docs/zh-TW/v5/tax/batch-create#%E5%A0%B1%E5%91%8A%E9%A1%9E%E5%9E%8B)。  
> number| string| 報告子類編號，與 `type` 組合使用。  
> status| integer (int32)| 

  * `0`：隊列中
  * `1`：生成中
  * `2`：成功
  * `-1`：失敗

  
> url| string| 下載地址。`status` 為 `2` 時有值，其他狀態下為空字符串。 文件的URL網址 (Basepath+Files)。為了縮短生成報告所需的時間，它可以生成多個文件。 _請注意這一點，並在請求數據導出時使用相同的基本路徑組合多個文件_  
> queryId| string| 該子任務的報告生成查詢 ID，在任務處理中或完成後有值。  
  
### 請求示例
    
    
    GET /v5/fht/compliance/tax/private/batch_query?batchId=b5f4a3e2-1c8d-4f96-9a03-2e7b8c6d4f10 HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN-TYPE: 2  
    X-BAPI-SIGN: xxxxxxxxxxxxxx  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1790035230000  
    X-BAPI-RECV-WINDOW: 5000  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "items": [  
                {  
                    "type": "TRADE",  
                    "number": "1",  
                    "status": 2,  
                    "url": "{\"Basepath\":\"https://prod-bybit-tax-api-1705-rz.s3.ap-southeast-1.amazonaws.com/\",\"Files\":[\"20260929/6b1b3341-6940-47a7-b112-5949e496736f/_SUCCESS\",\"20260929/6b1b3341-6940-47a7-b112-5949e496736f/part-00000-92859919-c8bf-47ce-b349-9cdcf44e8045-c000.csv\",\"20260929/6b1b3341-6940-47a7-b112-5949e496736f/part-00997-92859919-c8bf-47ce-b349-9cdcf44e8045-c000.csv\"]}",  
                    "queryId": "2104839833489960960"  
                },  
                {  
                    "type": "EARN",  
                    "number": "1",  
                    "status": 2,  
                    "url": "{\"Basepath\":\"https://prod-bybit-tax-api-1705-rz.s3.ap-southeast-1.amazonaws.com/\",\"Files\":[\"20260929/d64081bf-955b-4a96-b2f9-aa2f49760611/_SUCCESS\",\"20260929/d64081bf-955b-4a96-b2f9-aa2f49760611/part-00000-0f0a3b1a-cdd3-43d0-8afa-1159893220a8-c000.csv\",\"20260929/d64081bf-955b-4a96-b2f9-aa2f49760611/part-00001-0f0a3b1a-cdd3-43d0-8afa-1159893220a8-c000.csv\"]}",  
                    "queryId": "2104839833871642624"  
                },  
                {  
                    "type": "DEPOSIT&WITHDRAWAL",  
                    "number": "1",  
                    "status": 2,  
                    "url": "{\"Basepath\":\"https://prod-bybit-tax-api-1705-rz.s3.ap-southeast-1.amazonaws.com/\",\"Files\":[\"20260929/db47d025-ba66-4dee-98b8-8860d891fdb9/_SUCCESS\",\"20260929/db47d025-ba66-4dee-98b8-8860d891fdb9/part-00000-a8f75a9b-637f-4865-af11-5e4609e4a415-c000.csv\"]}",  
                    "queryId": "2104839834236547072"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1790669270665  
    }  
    

### 錯誤碼

參見[報稅錯誤碼](/docs/zh-TW/v5/error#%E5%A0%B1%E7%A8%85)。