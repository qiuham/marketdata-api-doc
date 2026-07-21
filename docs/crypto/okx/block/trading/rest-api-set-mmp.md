---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#block-trading-rest-api-set-mmp
anchor_id: block-trading-rest-api-set-mmp
api_type: REST
updated_at: 2026-07-21 19:26:32.949539
---

# Set MMP

This endpoint is used to set MMP configure and only applicable to block trading makers  
  
  
#### Rate Limit: 1 request per 10 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/rfq/mmp-config`

> Request Example
    
    
    POST /api/v5/rfq/mmp-config
    body
    {
        "timeInterval":"5000",
        "frozenInterval":"2000",
        "countLimit": "100"
    }
    
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
timeInterval | String | Yes | Time window (ms). MMP interval where monitoring is done.  
"0" means disable MMP. Maximum time interval is 600,000.  
frozenInterval | String | Yes | Frozen period (ms).   
"0" means the trade will remain frozen until you request "Reset MMP Status" to unfrozen.  
countLimit | String | Yes | Limit in number of execution attempts.  
  
> Response Example
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
        {
            "frozenInterval":"2000",
            "countLimit": "100",
            "timeInterval":"5000"
        }
      ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
timeInterval | String | Time window (ms). MMP interval where monitoring is done  
frozenInterval | String | Frozen period (ms).  
countLimit | String | Limit in number of execution attempts  
Group RFQ introduction  
  
For RFQ makers, the execution attempt of group RFQ will only count once towards MMP regardless of how many account allocations involved.

---

# 设置 MMP

该接口用于设置 MMP 的配置，仅适用于大宗交易中的maker。  
  
#### 限速：1次/10s

#### 限速规则：User ID

#### HTTP请求

`POST /api/v5/rfq/mmp-config`

> 请求示例
    
    
    POST /api/v5/rfq/mmp-config
    body
    {
        "timeInterval":"5000",
        "frozenInterval":"2000",
        "countLimit": "100"
    }
    
    
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
timeInterval | String | 是 | 时间窗口 (毫秒)。  
"0" 代表不使用 MMP。最大为 600,000。  
frozenInterval | String | 是 | 冻结时间长度 (毫秒)。  
"0" 代表一直冻结，直到调用 "重置 MMP 状态" 接口解冻  
countLimit | String | 是 | 尝试执行次数限制  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "frozenInterval": "2000",
                "countLimit": "100",
                "timeInterval": "5000"
            }
        ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
timeInterval | String | 时间窗口 (毫秒)  
frozenInterval | String | 冻结时间长度 (毫秒)  
countLimit | String | 尝试执行次数限制  
组合询价单介绍  
  
对于 Maker，组合询价单的执行尝试将只计入一次 MMP，无论涉及多少账户分配。