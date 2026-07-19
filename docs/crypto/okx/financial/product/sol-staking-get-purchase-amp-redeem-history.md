---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#financial-product-sol-staking-get-purchase-amp-redeem-history
anchor_id: financial-product-sol-staking-get-purchase-amp-redeem-history
api_type: API
updated_at: 2026-07-19 19:17:04.580845
---

# GET / Purchase&Redeem history

#### Rate Limit: 6 requests per second  
  
#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/finance/staking-defi/sol/purchase-redeem-history`

> Request Example
    
    
    GET /api/v5/finance/staking-defi/sol/purchase-redeem-history
    
    
    
    import okx.Finance.SolStaking as SolStaking
    
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    StackingAPI = SolStaking.SolStakingAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StackingAPI.sol_purchase_redeem_history()
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
type | String | No | Type  
`purchase`  
`redeem`  
status | String | No | Status  
`pending`  
`success`  
`failed`  
after | String | No | Pagination of data to return records earlier than the `requestTime`. The value passed is the corresponding `timestamp`  
before | String | No | Pagination of data to return records newer than the `requestTime`. The value passed is the corresponding `timestamp`  
limit | String | No | Number of results per request. The default is `100`. The maximum is `100`.  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "amt": "0.62666630",
                "completedTime": "1683413171000",
                "estCompletedTime": "",
                "redeemingAmt": "",
                "requestTime": "1683413171000",
                "status": "success",
                "type": "purchase"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
type | String | Type  
`purchase`  
`redeem`  
amt | String | Purchase/Redeem amount  
redeemingAmt | String | Redeeming amount  
status | String | Status  
`pending`  
`success`  
`failed`  
requestTime | String | Request time of make purchase/redeem, Unix timestamp format in milliseconds, e.g. `1597026383085`  
completedTime | String | Completed time of redeem settlement, Unix timestamp format in milliseconds, e.g. `1597026383085`  
estCompletedTime | String | Estimated completed time of redeem settlement, Unix timestamp format in milliseconds, e.g. `1597026383085`

---

# GET / 获取申购赎回记录

#### 限速：6 次/s  
  
#### 限速规则：User ID

#### HTTP 请求

`GET /api/v5/finance/staking-defi/sol/purchase-redeem-history`

> 请求示例
    
    
    GET /api/v5/finance/staking-defi/sol/purchase-redeem-history
    
    
    
    
    import okx.Finance.SolStaking as SolStaking
    
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    StackingAPI = SolStaking.SolStakingAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StackingAPI.sol_purchase_redeem_history()
    print(result)
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
type | String | 否 | 类型  
`purchase`：申购  
`redeem`：赎回  
status | String | 否 | 状态  
`pending`：处理中  
`success`：成功处理  
`failed`：处理失败  
after | String | 否 | 请求此`requestTime`之前（更旧的数据）的分页内容，值为时间戳，Unix 时间戳为毫秒数格式，如 `1597026383085`  
before | String | 否 | 请求此`requestTime`之后（更新的数据）的分页内容，值为时间戳，Unix 时间戳为毫秒数格式，如 `1597026383085`  
limit | String | 否 | 返回结果的数量，默认100条，最大值为100条  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "amt": "0.62666630",
                "completedTime": "1683413171000",
                "estCompletedTime": "",
                "redeemingAmt": "",
                "requestTime": "1683413171000",
                "status": "success",
                "type": "purchase"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
type | String | 类型  
`purchase`：申购  
`redeem`：赎回  
amt | String | 申购/赎回 的数量  
redeemingAmt | String | 赎回中的数量  
status | String | 状态  
`pending`：处理中  
`success`：成功处理  
`failed`：处理失败  
requestTime | String | 发起 申购/赎回 请求的时间，值为时间戳，Unix时间戳为毫秒数格式，如 `1597026383085`  
completedTime | String | 赎回请求处理完成的时间，值为时间戳，Unix时间戳为毫秒数格式，如 `1597026383085`  
estCompletedTime | String | 预估完成赎回的时间，值为时间戳，Unix时间戳为毫秒数格式，如 `1597026383085`