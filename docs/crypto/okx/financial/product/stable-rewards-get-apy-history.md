---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#financial-product-stable-rewards-get-apy-history
anchor_id: financial-product-stable-rewards-get-apy-history
api_type: API
updated_at: 2026-07-10 19:32:42.153631
---

# GET / APY history

Retrieve the historical daily APY of the specified stablecoin. The returned rate reflects the user's current VIP level.  
  
#### Rate Limit: 6 requests per second

#### Rate limit rule: IP

#### Permission: Read

#### HTTP Request

`GET /api/v5/finance/stable-rewards/apy-history`

> Request Example
    
    
    GET /api/v5/finance/stable-rewards/apy-history?ccy=USDG
    

#### Request Parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
ccy | String | Yes | Stablecoin, e.g. `USDG`  
days | String | No | Number of historical days to return. The default is `100`. The maximum is `100`  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "rate": "0.004",
                "ts": "1718035200000"
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
rate | String | Daily APY for the user's current VIP level, e.g. `0.041` represents `4.1%`  
ts | String | Snapshot time (UTC+0), Unix timestamp format in milliseconds, e.g. `1597026383085`

---

# GET / 获取历史收益率

查询指定稳定币的历史每日年化收益率。返回值为用户当前 VIP 等级对应的收益率。  
  
#### 限速：6次/s

#### 限速规则：IP

#### 权限：读取

#### HTTP 请求

`GET /api/v5/finance/stable-rewards/apy-history`

> 请求示例
    
    
    GET /api/v5/finance/stable-rewards/apy-history?ccy=USDG
    

#### 请求参数

**参数名** | **类型** | **是否必须** | **描述**  
---|---|---|---  
ccy | String | 是 | 稳定币，如 `USDG`  
days | String | 否 | 查询最近多少天的历史数据。默认 `100`，最大 `100`  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "rate": "0.004",
                "ts": "1718035200000"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
rate | String | 用户当前 VIP 等级对应的日度年化收益率，如 `0.041` 代表 `4.1%`  
ts | String | 数据快照时间（UTC+0），Unix 时间戳，单位为毫秒，如 `1597026383085`