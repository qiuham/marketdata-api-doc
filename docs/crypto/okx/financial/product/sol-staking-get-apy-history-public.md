---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#financial-product-sol-staking-get-apy-history-public
anchor_id: financial-product-sol-staking-get-apy-history-public
api_type: API
updated_at: 2026-07-23 19:23:15.303215
---

# GET / APY history (Public)

Public endpoints don't need authorization.  
  
#### Rate Limit: 6 requests per second

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/finance/staking-defi/sol/apy-history`

> Request Example
    
    
    GET /api/v5/finance/staking-defi/sol/apy-history?days=2
    
    
    
    
    import okx.Finance.SolStaking as SolStaking
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    StackingAPI = SolStaking.SolStakingAPI(flag=flag)
    
    result = StackingAPI.sol_apy_history(days="7")
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
days | String | Yes | Get the days of APY(Annual percentage yield) history record in the past  
No more than 365 days  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "rate": "0.11280000",
                "ts": "1734192000000"
            },
            {
                "rate": "0.11270000",
                "ts": "1734105600000"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
rate | String | APY(Annual percentage yield), e.g. `0.01` represents `1%`  
ts | String | Data time, Unix timestamp format in milliseconds, e.g. `1597026383085`

---

# GET / 获取历史收益率(公共)

公共接口无须鉴权  
  
#### 限速：6次/s

#### 限速规则：IP

#### HTTP 请求

`GET /api/v5/finance/staking-defi/sol/apy-history`

> 请求示例
    
    
    GET /api/v5/finance/staking-defi/sol/apy-history?days=2
    
    
    
    
    import okx.Finance.SolStaking as SolStaking
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    StackingAPI = SolStaking.SolStakingAPI(flag=flag)
    
    result = StackingAPI.sol_apy_history(days="7")
    print(result)
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
days | String | 是 | 查询最近多少天内的数据，不超过365天  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "rate": "0.11280000",
                "ts": "1734192000000"
            },
            {
                "rate": "0.11270000",
                "ts": "1734105600000"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
rate | String | 年化收益率，如 `0.01`代表`1%`  
ts | String | 时间，值为时间戳，Unix时间戳为毫秒数格式，如 `1597026383085`