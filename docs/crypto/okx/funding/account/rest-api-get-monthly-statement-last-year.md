---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#funding-account-rest-api-get-monthly-statement-last-year
anchor_id: funding-account-rest-api-get-monthly-statement-last-year
api_type: REST
updated_at: 2026-07-22 19:20:51.212708
---

# Get monthly statement (last year)

Retrieve monthly statement in the past year.  
  
#### Rate Limit: 10 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/asset/monthly-statement`

> Request Example
    
    
    GET /api/v5/asset/monthly-statement?month=Jan
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
month | String | Yes | Month, valid value is `Jan`, `Feb`, `Mar`, `Apr`,`May`, `Jun`, `Jul`,`Aug`, `Sep`,`Oct`,`Nov`,`Dec`  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "fileHref": "http://xxx",
                "state": "finished",
                "ts": 1646892328000
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
fileHref | String | Download file link  
ts | Int | Download link generation time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
state | String | Download link status   
"finished" "ongoing"

---

# 获取月结单 (近一年)

获取近一年的月结单  
  
#### 限速：10 次/2s

#### 限速规则：User ID

#### HTTP Request

`GET /api/v5/asset/monthly-statement`

> 请求示例
    
    
    GET /api/v5/asset/monthly-statement?month=Jan
    
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
month | String | 是 | 月份, 有效值是`Jan`, `Feb`, `Mar`, `Apr`,`May`, `Jun`, `Jul`,`Aug`, `Sep`, `Oct`, `Nov`, `Dec`  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "fileHref": "http://xxx",
                "state": "finished",
                "ts": 1646892328000
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
fileHref | String | 文件链接  
ts | Int | 下载链接生成时间，Unix时间戳的毫秒数格式 ，如 1597026383085  
state | String | 下载链接状态   
`finished`：已生成  
`ongoing`：进行中