---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#overview-market-maker-program-get-glp-c-history-performance
anchor_id: overview-market-maker-program-get-glp-c-history-performance
api_type: API
updated_at: 2026-11-25 18:59:29.212058
---

# GET / GLP-C history performance

Retrieve aggregated historical assessment results for registered GLP-C pairs.  
  
#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/users/glp/c/history/performance`

> Request Example
    
    
    GET /api/v5/users/glp/c/history/performance?instId=DOGE-USDT&begin=1732276800000&end=1732363200000
    

#### Request Parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
instId | String | No | Instrument ID  
instType | String | No | Instrument type filter  
`SPOT`  
`SWAP`  
begin | String | No | Filter with a begin timestamp `assessStartTime`. Unix timestamp in milliseconds  
end | String | No | Filter with an end timestamp `assessStartTime`. Unix timestamp in milliseconds  
after | String | No | Pagination of data to return records earlier than the requested `assessStartTime`, Unix timestamp format in milliseconds, e.g. `1597026383085`  
before | String | No | Pagination of data to return records newer than the requested `assessStartTime`, Unix timestamp format in milliseconds, e.g. `1597026383085`  
limit | String | No | Number of results per request. The maximum is `100`. The default is `100`.  
`assessStartTime` is not unique across pairs. When `instId` is omitted, several records can share the same `assessStartTime`, and `after`/`before` exclude every record at the requested `assessStartTime`, so records at a page boundary can be skipped. To reduce the chance of skipped records, specify `instId` when paginating. 

> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "instId": "DOGE-USDT",
                "instType": "SPOT",
                "assessStartTime": "1732276800000",
                "assessEndTime": "1732363200000",
                "qualifiedHours": "20",
                "totalHours": "24",
                "qualifiedRate": "0.8333"
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
assessStartTime | String | Assessment period start time. Unix timestamp in milliseconds  
assessEndTime | String | Assessment period end time. Unix timestamp in milliseconds  
qualifiedHours | String | Number of qualified hours in the period  
totalHours | String | Total assessment hours in the period  
qualifiedRate | String | Qualification rate. Decimal string, e.g. `0.8333` = 83.33%

---

# GET / 查询 GLP-C 历史考核结果

查询已注册 GLP-C 币对的历史聚合考核结果。  
  
#### 限速：5次/2s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/users/glp/c/history/performance`

> 请求示例
    
    
    GET /api/v5/users/glp/c/history/performance?instId=DOGE-USDT&begin=1732276800000&end=1732363200000
    

#### 请求参数

**参数名** | **类型** | **是否必须** | **描述**  
---|---|---|---  
instId | String | 否 | 产品ID  
instType | String | 否 | 产品类型过滤  
`SPOT`  
`SWAP`  
begin | String | 否 | 筛选的开始时间戳 `assessStartTime`。Unix 毫秒时间戳  
end | String | 否 | 筛选的结束时间戳 `assessStartTime`。Unix 毫秒时间戳  
after | String | 否 | 请求 `assessStartTime` 此时间戳之前（更旧的数据）的分页内容，Unix时间戳的毫秒数格式，如 `1597026383085`  
before | String | 否 | 请求 `assessStartTime` 此时间戳之后（更新的数据）的分页内容，Unix时间戳的毫秒数格式，如 `1597026383085`  
limit | String | 否 | 返回结果的数量，最大为100，默认100条  
`assessStartTime` 在不同币对之间不唯一。不传 `instId` 时，多条记录可能具有相同的 `assessStartTime`，而 `after`/`before` 会排除请求的 `assessStartTime` 上的所有记录，因此分页边界上的记录可能被跳过。分页时建议传入 `instId`，以减少记录被跳过的可能。 

> 返回示例
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "instId": "DOGE-USDT",
                "instType": "SPOT",
                "assessStartTime": "1732276800000",
                "assessEndTime": "1732363200000",
                "qualifiedHours": "20",
                "totalHours": "24",
                "qualifiedRate": "0.8333"
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
assessStartTime | String | 考核周期开始时间。Unix 毫秒时间戳  
assessEndTime | String | 考核周期结束时间。Unix 毫秒时间戳  
qualifiedHours | String | 周期内达标小时数  
totalHours | String | 周期内总考核小时数  
qualifiedRate | String | 达标率。小数字符串，如 `0.8333` 表示 83.33%