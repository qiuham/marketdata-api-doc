---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/tax/batch-create
api_type: REST
updated_at: 2026-11-13 19:25:33.372945
---

# Batch Request Export Reports

Request to export multiple types of tax reports in a batch. Reports are generated asynchronously. Use the returned `batchId` to [query task status and download URLs](/docs/v5/tax/batch-query).

**Batch workflow:**

  1. Call BatchCreate to submit multiple tax report export items and obtain `batchId`.
  2. Poll [BatchQuery](/docs/v5/tax/batch-query) with `batchId` until every child task reaches a terminal status (`2` or `-1`).
  3. Use the `url` returned for child tasks whose status is `2`.



info

  * API key permission: **Exchange History (read/write)**.
  * Rate limit: **5 requests per second** , per UID and endpoint.
  * `items` must contain at least one item.
  * `startTime` must be earlier than `endTime`. The time range must not exceed **12 months**.
  * A new batch cannot be submitted while an unfinished batch exists. The API returns error code `400004` in this case.



### HTTP Request

POST `/v5/fht/compliance/tax/private/batch_create`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
startTime| **true**|  integer (int64)| Report start time. UNIX timestamp in seconds.  
endTime| **true**|  integer (int64)| Report end time. UNIX timestamp in seconds. Must be later than `startTime`, with a time range of at most 12 months.  
items| **true**|  array| List of report objects to export. At least one item is required.  
> type| **true**|  string| Report type. Use `ALL` to export all supported report types for the current site. See supported report types.  
> number| **true**|  string| Report subcategory number, used together with `type`. The field is still required when `type=ALL`, but its value is ignored; pass an empty string (`""`). See supported report types.  
sourceInstitution| false| string| Identifier of the institution making the request.  
exportFileType| false| string| Export file format: `orc` for ORC columnar format (default), or `csv` for CSV text format.  
  
#### Report Types

The supported `type` and `number` combinations depend on the site. `bybit` refers to Bybit; `eu` refers to Bybit EU.

type| number| Report| Supported sites  
---|---|---|---  
`ALL`| Ignored; use `""`| All supported reports for the current site| `bybit`, `eu`  
`TRADE`| `1`| Spot trading| `bybit`, `eu`  
`TRADE`| `2`| Contract trading| `bybit`  
`TRADE`| `3`| USDC Options trading| `bybit`  
`TRADE`| `4`| NFT trading| `bybit`  
`TRADE`| `5`| Convert| `bybit`, `eu`  
`TRADE`| `6`| One-Click Buy| `bybit`, `eu`  
`P&L`| `1`| Closed PnL| `bybit`  
`EARN`| `1`| Staking| `bybit`, `eu`  
`EARN`| `2`| Liquidity Mining - Liquidity| `bybit`  
`EARN`| `3`| Liquidity Mining - Yield| `bybit`  
`EARN`| `4`| Liquidity Mining - Swap| `bybit`  
`EARN`| `5`| Dual Asset| `bybit`  
`EARN`| `6`| DeFi Mining| `bybit`  
`EARN`| `7`| Launchpool| `bybit`, `eu`  
`EARN`| `8`| Shark Fin| `bybit`  
`EARN`| `9`| On-Chain Earn| `bybit`, `eu`  
`EARN`| `11`| Double Win orders| `bybit`, `eu`  
`EARN`| `12`| Discount Buy orders| `bybit`, `eu`  
`EARN`| `13`| Smart Leverage| `bybit`, `eu`  
`DEPOSIT&WITHDRAWAL`| `1`| Crypto deposits| `bybit`, `eu`  
`DEPOSIT&WITHDRAWAL`| `2`| P2P| `bybit`  
`DEPOSIT&WITHDRAWAL`| `3`| Fiat deposits and withdrawals| `bybit`, `eu`  
`DEPOSIT&WITHDRAWAL`| `4`| Express orders| `bybit`, `eu`  
`DEPOSIT&WITHDRAWAL`| `5`| Third-party deposits| `bybit`  
`DEPOSIT&WITHDRAWAL`| `6`| Withdrawals| `bybit`, `eu`  
`DEPOSIT&WITHDRAWAL`| `7`| NFT deposits and withdrawals| `bybit`  
`BONUS`| `1`| Coupons| `bybit`, `eu`  
`BONUS`| `2`| Bonuses| `bybit`, `eu`  
`AIRDROP`| `1`| Airdrops| `bybit`, `eu`  
`CARD`| `1`| Bybit Card transactions| `bybit`, `eu`  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
batchId| string| Unique batch ID in UUID format. Use it to query the batch's task status and download URLs.  
  
### Request Example
    
    
    POST /v5/fht/compliance/tax/private/batch_create HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN-TYPE: 2  
    X-BAPI-SIGN: xxxxxxxxxxxxxx  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1790035200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "startTime": 1756684800,  
        "endTime": 1788220800,  
        "items": [  
            { "type": "TRADE", "number": "1" },  
            { "type": "EARN", "number": "1" },  
            { "type": "DEPOSIT&WITHDRAWAL", "number": "1" }  
        ],  
        "sourceInstitution": "INST_A",  
        "exportFileType": "csv"  
    }  
    

#### Export All Report Types

To export all report types supported by the current site, use the following request body. `number` is required but its value is ignored when `type=ALL`.
    
    
    {  
        "startTime": 1756684800,  
        "endTime": 1788220800,  
        "items": [  
            { "type": "ALL", "number": "" }  
        ],  
        "exportFileType": "csv"  
    }  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "ok",  
        "result": {  
            "batchId": "b5f4a3e2-1c8d-4f96-9a03-2e7b8c6d4f10"  
        }  
    }  
    

### Error Codes

See [Tax Error Codes](/docs/v5/error#tax).

---

# 批量創建導出報告請求

一次請求批量導出多種類型的報稅報告。報告以異步方式生成，可使用返回的 `batchId` [查詢任務狀態及下載地址](/docs/zh-TW/v5/tax/batch-query)。

**批量導出流程：**

  1. 調用 BatchCreate 提交多個報稅報告導出條目，並獲取 `batchId`。
  2. 使用 `batchId` 輪詢 [BatchQuery](/docs/zh-TW/v5/tax/batch-query)，直到所有子任務均達到終態（`2` 或 `-1`）。
  3. 使用狀態為 `2` 的子任務返回的 `url` 下載報告。



信息

  * API Key 權限：**Exchange History（讀寫權限）** 。
  * 限流：每個 UID 每個接口 **5 次/秒** 。
  * `items` 至少包含一個條目。
  * `startTime` 必須在最近 **18 個月** 內，且早於 `endTime`。時間跨度不得超過 **12 個月** 。
  * 存在未完成批次時，不可提交新批次，否則接口返回錯誤碼 `400004`。



### HTTP 請求

POST `/v5/fht/compliance/tax/private/batch_create`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
startTime| **true**|  integer (int64)| 報告開始時間，UNIX 時間戳，單位為秒。必須在最近 18 個月內。  
endTime| **true**|  integer (int64)| 報告結束時間，UNIX 時間戳，單位為秒。必須晚於 `startTime`，且時間跨度不得超過 12 個月。  
items| **true**|  array| 待導出報告的對象列表，至少包含一個條目。  
> type| **true**|  string| 報告類型。傳入 `ALL` 可導出當前站點支持的所有報告類型，參見支持的報告類型。  
> number| **true**|  string| 報告子類編號，與 `type` 組合使用。`type=ALL` 時仍須傳入此字段，但其值會被忽略，可傳入空字符串（`""`）。參見支持的報告類型。  
sourceInstitution| false| string| 調用機構標識。  
exportFileType| false| string| 導出文件格式：`orc` 為 ORC 列式格式（默認），`csv` 為 CSV 文本格式。  
  
#### 報告類型

支持的 `type` 和 `number` 組合取決於站點。`bybit` 表示 Bybit，`eu` 表示 Bybit EU。

type| number| 報告| 支持站點  
---|---|---|---  
`ALL`| 忽略此值，可傳入 `""`| 當前站點支持的所有報告| `bybit`, `eu`  
`TRADE`| `1`| 現貨交易| `bybit`, `eu`  
`TRADE`| `2`| 合約交易| `bybit`  
`TRADE`| `3`| USDC 期權交易| `bybit`  
`TRADE`| `4`| NFT 交易| `bybit`  
`TRADE`| `5`| 閃兌| `bybit`, `eu`  
`TRADE`| `6`| 一鍵買幣| `bybit`, `eu`  
`P&L`| `1`| 已平倉盈虧| `bybit`  
`EARN`| `1`| 質押| `bybit`, `eu`  
`EARN`| `2`| 流動性挖礦 - 流動性| `bybit`  
`EARN`| `3`| 流動性挖礦 - 收益| `bybit`  
`EARN`| `4`| 流動性挖礦 - 兌換| `bybit`  
`EARN`| `5`| 雙幣投資| `bybit`  
`EARN`| `6`| DeFi 挖礦| `bybit`  
`EARN`| `7`| Launchpool| `bybit`, `eu`  
`EARN`| `8`| 鯊魚鰭| `bybit`  
`EARN`| `9`| 鏈上賺幣| `bybit`, `eu`  
`EARN`| `11`| 雙贏訂單| `bybit`, `eu`  
`EARN`| `12`| 折扣買幣訂單| `bybit`, `eu`  
`EARN`| `13`| 智能槓桿| `bybit`, `eu`  
`DEPOSIT&WITHDRAWAL`| `1`| 加密貨幣充值| `bybit`, `eu`  
`DEPOSIT&WITHDRAWAL`| `2`| P2P| `bybit`  
`DEPOSIT&WITHDRAWAL`| `3`| 法幣充值及提現| `bybit`, `eu`  
`DEPOSIT&WITHDRAWAL`| `4`| 快捷訂單| `bybit`, `eu`  
`DEPOSIT&WITHDRAWAL`| `5`| 第三方充值| `bybit`  
`DEPOSIT&WITHDRAWAL`| `6`| 提現| `bybit`, `eu`  
`DEPOSIT&WITHDRAWAL`| `7`| NFT 充值及提現| `bybit`  
`BONUS`| `1`| 優惠券| `bybit`, `eu`  
`BONUS`| `2`| 獎勵金| `bybit`, `eu`  
`AIRDROP`| `1`| 空投| `bybit`, `eu`  
`CARD`| `1`| Bybit Card 交易| `bybit`, `eu`  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
batchId| string| UUID 格式的批次唯一 ID，用於查詢批次內的任務狀態及下載地址。  
  
### 請求示例
    
    
    POST /v5/fht/compliance/tax/private/batch_create HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN-TYPE: 2  
    X-BAPI-SIGN: xxxxxxxxxxxxxx  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1790035200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "startTime": 1756684800,  
        "endTime": 1788220800,  
        "items": [  
            { "type": "TRADE", "number": "1" },  
            { "type": "EARN", "number": "1" },  
            { "type": "DEPOSIT&WITHDRAWAL", "number": "1" }  
        ],  
        "sourceInstitution": "INST_A",  
        "exportFileType": "csv"  
    }  
    

#### 導出所有報告類型

如需導出當前站點支持的所有報告類型，可使用以下請求體。`type=ALL` 時，`number` 字段仍為必填，但其值會被忽略。
    
    
    {  
        "startTime": 1756684800,  
        "endTime": 1788220800,  
        "items": [  
            { "type": "ALL", "number": "" }  
        ],  
        "exportFileType": "csv"  
    }  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "ok",  
        "result": {  
            "batchId": "b5f4a3e2-1c8d-4f96-9a03-2e7b8c6d4f10"  
        }  
    }  
    

### 錯誤碼

參見[報稅錯誤碼](/docs/zh-TW/v5/error#%E5%A0%B1%E7%A8%85)。