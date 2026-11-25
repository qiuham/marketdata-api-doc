---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#overview-market-maker-program
anchor_id: overview-market-maker-program
api_type: API
updated_at: 2026-11-25 18:59:29.169198
---

# Market Maker Program

High-caliber trading teams are welcomed to work with OKX as market makers in providing a liquid, fair, and orderly platform to all users. OKX market makers could enjoy favourable fees in return for meeting the market making obligations.  

Prerequisites (Satisfy any condition): 

  * VIP 2 or above on fee schedule  

  * Qualified Market Maker on other exchange  

Interested parties can reach out to us at `Institutional@okx.com`  

Remarks:

Market making obligations and trading fees will be shared to successful parties only.

OKX reserves the right of final decision and interpretation for the content hereinabove.  In fairness to all users, market makers will be ineligible for other VIP-related and volume-related promotions or rebates. 

### POST / Register GLP-C pairs

Register one or more instruments for the GLP-C (Global Liquidity Program — Category C) market maker program. GLP-C assesses market maker order book depth on tail-end trading pairs on an hourly basis. Supports batch registration; each instrument returns an individual result code.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/users/glp/c/register-pairs`

> Request Example
    
    
    POST /api/v5/users/glp/c/register-pairs
    body
    {
        "instIds": ["DOGE-USDT", "SHIB-USDT", "PEPE-USDT-SWAP"]
    }
    

#### Request Parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
instIds | Array of strings | Yes | List of instrument IDs to register for GLP-C  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "instId": "DOGE-USDT",
                "sCode": "0",
                "sMsg": ""
            },
            {
                "instId": "SHIB-USDT",
                "sCode": "0",
                "sMsg": ""
            },
            {
                "instId": "PEPE-USDT-SWAP",
                "sCode": "0",
                "sMsg": ""
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instId | String | Instrument ID  
sCode | String | Result code for this instrument. `0` means success  
sMsg | String | Result message for this instrument  
  
### GET / GLP-C registered pairs

Retrieve the list of instruments that the account has registered for GLP-C.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/users/glp/c/registered-pairs`

> Request Example
    
    
    GET /api/v5/users/glp/c/registered-pairs?instType=SPOT
    

#### Request Parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
instType | String | No | Instrument type filter  
`SPOT`  
`SWAP`  
Returns all if omitted  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "instId": "DOGE-USDT",
                "instType": "SPOT",
                "registerTime": "1732300800000"
            },
            {
                "instId": "PEPE-USDT-SWAP",
                "instType": "SWAP",
                "registerTime": "1732300800000"
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
registerTime | String | Registration time. Unix timestamp in milliseconds  
  
### GET / GLP-C performance

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
  
### GET / GLP-C history performance

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

# 做市商申请

满足以下任意条件的用户即可申请加入欧易做市商计划：

  * 交易等级VIP2及以上  

  * 其他交易所达标做市商（需审核）  

感兴趣的各方可以通过邮箱联系我们：`Institutional@okx.com`  

为鼓励做市商为平台提供更好的流动性，可以享受更优的交易手续费，同时也承担相应的做市责任。具体做市责任及手续费申请成功后提供相关资料。

欧易保留对做市商项目的最终解释权  做市商项目不支持VIP、交易量相关活动以及任何形式的返佣活动 

### POST / 注册 GLP-C 币对 

为 GLP-C（全球流动性计划 — C 类）做市商激励项目注册一个或多个交易产品。GLP-C 以每小时为周期，考核做市商在长尾币对上的订单簿挂单深度。支持批量注册，每个产品独立返回结果码。

#### 限速：5次/2s

#### 限速规则：User ID

#### HTTP请求

`POST /api/v5/users/glp/c/register-pairs`

> 请求示例
    
    
    POST /api/v5/users/glp/c/register-pairs
    body
    {
        "instIds": ["DOGE-USDT", "SHIB-USDT", "PEPE-USDT-SWAP"]
    }
    

#### 请求参数

**参数名** | **类型** | **是否必须** | **描述**  
---|---|---|---  
instIds | Array of strings | 是 | 要注册 GLP-C 的产品ID列表  
  
> 返回示例
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "instId": "DOGE-USDT",
                "sCode": "0",
                "sMsg": ""
            },
            {
                "instId": "SHIB-USDT",
                "sCode": "0",
                "sMsg": ""
            },
            {
                "instId": "PEPE-USDT-SWAP",
                "sCode": "0",
                "sMsg": ""
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
instId | String | 产品ID  
sCode | String | 该产品的结果码。`0` 表示成功  
sMsg | String | 该产品的结果消息  
  
### GET / 查询已注册 GLP-C 币对 

查询账户已注册 GLP-C 的交易产品列表。

#### 限速：5次/2s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/users/glp/c/registered-pairs`

> 请求示例
    
    
    GET /api/v5/users/glp/c/registered-pairs?instType=SPOT
    

#### 请求参数

**参数名** | **类型** | **是否必须** | **描述**  
---|---|---|---  
instType | String | 否 | 产品类型过滤  
`SPOT`  
`SWAP`  
不传返回全部  
  
> 返回示例
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "instId": "DOGE-USDT",
                "instType": "SPOT",
                "registerTime": "1732300800000"
            },
            {
                "instId": "PEPE-USDT-SWAP",
                "instType": "SWAP",
                "registerTime": "1732300800000"
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
registerTime | String | 注册时间。Unix 毫秒时间戳  
  
### GET / 查询 GLP-C 考核表现 

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
  
### GET / 查询 GLP-C 历史考核结果 

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