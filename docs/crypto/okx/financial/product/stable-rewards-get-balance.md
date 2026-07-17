---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#financial-product-stable-rewards-get-balance
anchor_id: financial-product-stable-rewards-get-balance
api_type: API
updated_at: 2026-07-17 19:18:12.321874
---

# GET / Balance

Retrieve the real-time Stable Rewards balance across the account (trading account, funding account, and in-progress redemptions combined), along with lifetime earnings and the current earning state for each stablecoin.  
  
#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/finance/stable-rewards/balance`

> Request Example
    
    
    GET /api/v5/finance/stable-rewards/balance?ccy=USDG
    

#### Request Parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
ccy | String | No | Stablecoin, e.g. `USDG`  
Returns all supported stablecoins if not specified  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "details": [
                    {
                        "ccy": "USDG",
                        "amt": "100",
                        "totalEarnAccrual": "0.0003",
                        "state": "earning"
                    }
                ],
                "ts": "1718035200000"
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
details | Array of objects | Real-time balance details per stablecoin  
> ccy | String | Stablecoin, e.g. `USDG`  
> amt | String | Currency amount held across the entire account  
> totalEarnAccrual | String | Total interest accrued over the lifetime of the holding  
> state | String | Earning state  
`earning`: The balance is currently accruing rewards  
`pending`: The balance is not currently accruing (e.g. auto-earn is off, or the balance is below the activation threshold)  
ts | String | Query data time, Unix timestamp format in milliseconds, e.g. `1597026383085`

---

# GET / 获取余额

查询 Stable Rewards 的实时余额，余额涵盖交易账户、资金账户以及正在赎回中的资产合计，同时返回累计收益与当前收益状态。  
  
#### 限速：5次/2s

#### 限速规则：User ID

#### HTTP 请求

`GET /api/v5/finance/stable-rewards/balance`

> 请求示例
    
    
    GET /api/v5/finance/stable-rewards/balance?ccy=USDG
    

#### 请求参数

**参数名** | **类型** | **是否必须** | **描述**  
---|---|---|---  
ccy | String | 否 | 稳定币，如 `USDG`  
不传则返回全部支持的稳定币  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "details": [
                    {
                        "ccy": "USDG",
                        "amt": "100",
                        "totalEarnAccrual": "0.0003",
                        "state": "earning"
                    }
                ],
                "ts": "1718035200000"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
details | Array of objects | 按稳定币返回的实时余额明细  
> ccy | String | 稳定币，如 `USDG`  
> amt | String | 整个账户范围内的持有数量  
> totalEarnAccrual | String | 持有期间的累计收益  
> state | String | 收益状态  
`earning`：正在产生收益  
`pending`：未在产生收益（如自动赚币已关闭，或余额低于起息门槛）  
ts | String | 数据查询时间，Unix 时间戳，单位为毫秒，如 `1597026383085`