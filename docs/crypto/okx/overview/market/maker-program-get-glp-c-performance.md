---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#overview-market-maker-program-get-glp-c-performance
anchor_id: overview-market-maker-program-get-glp-c-performance
api_type: API
updated_at: 2026-11-25 18:59:29.201045
---

# GET / GLP-C performance

Retrieve hourly assessment performance data for registered GLP-C pairs.  
  
#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/users/glp/c/performance`

> Request Example
    
    
    GET /api/v5/users/glp/c/performance?instId=DOGE-USDT&limit=10
    

#### Request Parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
instId | String | No | Instrument ID. Returns all registered pairs if omitted  
instType | String | No | Instrument type filter  
`SPOT`  
`SWAP`  
begin | String | No | Start time. Unix timestamp in milliseconds, inclusive  
end | String | No | End time. Unix timestamp in milliseconds, inclusive  
after | String | No | Pagination of data to return records earlier than the requested `ts`, Unix timestamp format in milliseconds, e.g. `1597026383085`  
before | String | No | Pagination of data to return records newer than the requested `ts`, Unix timestamp format in milliseconds, e.g. `1597026383085`  
limit | String | No | Number of results per request. The maximum is `100`. The default is `100`.  
`ts` is not unique across pairs. When `instId` is omitted, several records can share the same `ts`, and `after`/`before` exclude every record at the requested `ts`, so records at a page boundary can be skipped. To paginate without missing records, specify `instId`. 

> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "instId": "DOGE-USDT",
                "instType": "SPOT",
                "ts": "1732363200000",
                "qualified": "true",
                "bidDepth": "50000",
                "askDepth": "48000",
                "reqDepth": "30000"
            },
            {
                "instId": "DOGE-USDT",
                "instType": "SPOT",
                "ts": "1732359600000",
                "qualified": "false",
                "bidDepth": "25000",
                "askDepth": "22000",
                "reqDepth": "30000"
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instId | String | Instrument ID  
instType | String | Instrument type  
`SPOT`  
`SWAP`  
ts | String | Assessment timestamp. Unix timestamp in milliseconds (on the hour)  
qualified | String | Whether the hourly assessment was met  
`true`  
`false`  
bidDepth | String | Bid-side depth in top 3 levels  
askDepth | String | Ask-side depth in top 3 levels  
reqDepth | String | Required depth threshold to qualify

---

# GET / 查询 GLP-C 考核表现

查询已注册 GLP-C 币对的每小时考核表现数据。  
  
#### 限速：5次/2s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/users/glp/c/performance`

> 请求示例
    
    
    GET /api/v5/users/glp/c/performance?instId=DOGE-USDT&limit=10
    

#### 请求参数

**参数名** | **类型** | **是否必须** | **描述**  
---|---|---|---  
instId | String | 否 | 产品ID。不传返回全部已注册币对  
instType | String | 否 | 产品类型过滤  
`SPOT`  
`SWAP`  
begin | String | 否 | 开始时间。Unix 毫秒时间戳，包含  
end | String | 否 | 结束时间。Unix 毫秒时间戳，包含  
after | String | 否 | 请求 `ts` 此时间戳之前（更旧的数据）的分页内容，Unix时间戳的毫秒数格式，如 `1597026383085`  
before | String | 否 | 请求 `ts` 此时间戳之后（更新的数据）的分页内容，Unix时间戳的毫秒数格式，如 `1597026383085`  
limit | String | 否 | 返回结果的数量，最大为100，默认100条  
`ts` 在不同币对之间不唯一。不传 `instId` 时，多条记录可能具有相同的 `ts`，而 `after`/`before` 会排除请求的 `ts` 上的所有记录，因此分页边界上的记录可能被跳过。如需分页且不遗漏记录，请传入 `instId`。 

> 返回示例
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "instId": "DOGE-USDT",
                "instType": "SPOT",
                "ts": "1732363200000",
                "qualified": "true",
                "bidDepth": "50000",
                "askDepth": "48000",
                "reqDepth": "30000"
            },
            {
                "instId": "DOGE-USDT",
                "instType": "SPOT",
                "ts": "1732359600000",
                "qualified": "false",
                "bidDepth": "25000",
                "askDepth": "22000",
                "reqDepth": "30000"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
instId | String | 产品ID  
instType | String | 产品类型  
`SPOT`  
`SWAP`  
ts | String | 考核时间点。Unix 毫秒时间戳（整点）  
qualified | String | 该小时是否达标  
`true`  
`false`  
bidDepth | String | 买方前三档挂单深度  
askDepth | String | 卖方前三档挂单深度  
reqDepth | String | 达标所需深度