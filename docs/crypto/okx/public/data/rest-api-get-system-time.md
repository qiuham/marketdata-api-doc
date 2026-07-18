---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#public-data-rest-api-get-system-time
anchor_id: public-data-rest-api-get-system-time
api_type: REST
updated_at: 2026-07-18 20:04:37.995799
---

# Get system time

Retrieve API server time.  
  
#### Rate Limit: 10 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/public/time`

> Request Example
    
    
    GET /api/v5/public/time
    
    
    
    import okx.PublicData as PublicData
    
    flag = "0"  # Production trading: 0, Demo trading: 1
    
    publicDataAPI = PublicData.PublicAPI(flag=flag)
    
    # Retrieve API server time
    result = publicDataAPI.get_system_time()
    print(result)
    

> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
        {
            "ts":"1597026383085"
        }
      ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
ts | String | System time, Unix timestamp format in milliseconds, e.g. `1597026383085`

---

# 获取系统时间

获取系统时间  
  
#### 限速：10次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/public/time`

> 请求示例
    
    
    GET /api/v5/public/time
    
    
    
    import okx.PublicData as PublicData
    
    flag = "0"  # 实盘:0 , 模拟盘：1
    
    publicDataAPI = PublicData.PublicAPI(flag=flag)
    
    # 获取系统时间
    result = publicDataAPI.get_system_time()
    print(result)
    

> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
        {
            "ts":"1597026383085"
        }
      ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
ts | String | 系统时间，Unix时间戳的毫秒数格式，如 `1597026383085`