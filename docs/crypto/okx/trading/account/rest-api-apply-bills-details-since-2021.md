---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#trading-account-rest-api-apply-bills-details-since-2021
anchor_id: trading-account-rest-api-apply-bills-details-since-2021
api_type: REST
updated_at: 2026-07-22 19:18:43.841050
---

# Apply bills details (since 2021)

Apply for bill data since 1 February, 2021 except for the current quarter.

#### Rate Limit: 1 request per 10 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/account/bills-history-archive`

> Request Example
    
    
    POST /api/v5/account/bills-history-archive
    body
    {
        "year":"2023",
        "quarter":"Q1"
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
year | String | Yes | 4 digits year  
quarter | String | Yes | Quarter, valid value is `Q1`, `Q2`, `Q3`, `Q4`  
type | String | No | Bill type. Multiple values are supported, separated by commas, e.g. `1,2,3`. If not specified, all types are returned.  
Please refer to [Get bill types](/docs-v5/en/#trading-account-rest-api-get-bill-types) for the list of available types.  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "result": "true",
                "ts": "1646892328000"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
result | String | Whether there is already a download link for this section   
`true`: Existed, can check from "Get bills details (since 2021)".   
`false`: Does not exist and is generating, can check the download link after 2 hours  
The data of file is in reverse chronological order using `billId`.  
ts | String | The first request time when the server receives. Unix timestamp format in milliseconds, e.g. `1597026383085`  
The rule introduction, only applicable to the file generated after 11 October, 2024  
1\. Taking 2024 Q2 as an example. The date range are [2024-07-01, 2024-10-01). The begin date is included, The end date is excluded.  
2\. The data of file is in reverse chronological order using `billId`  Check the file link from the "Get bills details (since 2021)" endpoint in 2 hours to allow for data generation.   
During peak demand, data generation may take longer. If the file link is still unavailable after 3 hours, reach out to customer support for assistance.  It is only applicable to the data from the unified account.

---

# 申请账单流水（自 2021 年）

申请自 2021 年 2 月 1 日以来的账单数据，不包括当前季度。

#### 限速：1次/10s

#### 限速规则：User ID

#### HTTP 请求

`POST /api/v5/account/bills-history-archive`

> 请求示例
    
    
    POST /api/v5/account/bills-history-archive
    body
    {
        "year":"2023",
        "quarter":"Q1"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
year | String | 是 | 4位数字的年份，如 `2023`  
quarter | String | 是 | 季度，有效值 `Q1` `Q2` `Q3` `Q4`  
type | String | 否 | 账单类型，支持多个，用英文逗号分隔，如 `1,2,3`；不填则返回所有类型。  
枚举值请通过 [获取账单类型](/docs-v5/zh/#trading-account-rest-api-get-bill-types) 接口查询。  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "result": "true",
                "ts": "1646892328000"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
result | String | 是否已经存在该区间的下载链接  
`true`：已存在，可以通过"获取账单流水（自 2021 年）"接口获取  
`false`：不存在，正在生成，请 2 个小时后查看下载链接  
ts | String | 服务端首次收到请求的时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
规则说明，仅适用于 2024 年 10 月 11 日之后新生成的文件： 1\. 以查询 2024 年第 3 季度的数据为例，实际查询的起止日期范围是 [2024-07-01, 2024-10-01)，包含开始日期，不包含结束日期。  
2\. 文件中的数据以 `billId` 倒序排列  平台需求量较多的情况下，生成数据所需要的时间会有所延长，如果超过 3 小时，请联系客服进行反馈。  仅适用于来自统一账户的数据