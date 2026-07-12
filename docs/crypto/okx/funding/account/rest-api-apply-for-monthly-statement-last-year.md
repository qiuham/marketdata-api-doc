---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#funding-account-rest-api-apply-for-monthly-statement-last-year
anchor_id: funding-account-rest-api-apply-for-monthly-statement-last-year
api_type: REST
updated_at: 2026-07-12 19:17:15.076171
---

# Apply for monthly statement (last year)

Apply for monthly statement in the past year.  
  
#### Rate Limit: 20 requests per month

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`POST /api/v5/asset/monthly-statement`

> Request Example
    
    
    POST /api/v5/asset/monthly-statement
    body
    {
        "month":"Jan"
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
month | String | No | Month,last month by default. Valid value is `Jan`, `Feb`, `Mar`, `Apr`,`May`, `Jun`, `Jul`,`Aug`, `Sep`,`Oct`,`Nov`,`Dec`  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "ts": "1646892328000"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
ts | String | Download link generation time, Unix timestamp format in milliseconds, e.g. `1597026383085`

---

# 申请月结单 (近一年)

申请最近一年的月结单。  
  
#### 限速：20 次/月

#### 限速规则：User ID

#### 权限：读取

#### HTTP Request

`POST /api/v5/asset/monthly-statement`

> 请求示例
    
    
    POST /api/v5/asset/monthly-statement
    body
    {
        "month":"Jan"
    }
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
month | String | 否 | 月份,默认上一个月。有效值是`Jan`, `Feb`, `Mar`, `Apr`,`May`, `Jun`, `Jul`,`Aug`, `Sep`,`Oct`,`Nov`,`Dec`  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "ts": "1646892328000"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ts | String | 下载链接生成时间，Unix时间戳的毫秒数格式 ，如, `1597026383085`