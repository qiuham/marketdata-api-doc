---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#trading-account-rest-api-get-borrow-repay-history
anchor_id: trading-account-rest-api-get-borrow-repay-history
api_type: REST
updated_at: 2026-07-07 19:41:27.814046
---

# Get borrow/repay history

Retrieve the borrow/repay history under `Spot mode`  
  
#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/account/spot-borrow-repay-history`

> Request Example
    
    
    GET /api/v5/account/spot-borrow-repay-history
    
    
    
    import okx.Account as Account
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"   # Production trading:0 , demo trading:1
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    result = accountAPI.spot_borrow_repay_history(ccy="USDT", type="auto_borrow")
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
ccy | String | No | Currency, e.g. `BTC`  
type | String | No | Event type  
`auto_borrow`  
`auto_repay`  
`manual_borrow`  
`manual_repay`  
after | String | No | Pagination of data to return records earlier than the requested `ts` (included), Unix timestamp format in milliseconds, e.g. `1597026383085`  
before | String | No | Pagination of data to return records newer than the requested `ts`(included), Unix timestamp format in milliseconds, e.g. `1597026383085`  
limit | String | No | Number of results per request. The maximum is 100. The default is 100.  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "accBorrowed": "0",
                "amt": "6764.802661157592",
                "ccy": "USDT",
                "ts": "1725330976644",
                "type": "auto_repay"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ccy | String | Currency, e.g. `BTC`  
type | String | Event type  
`auto_borrow`  
`auto_repay`  
`manual_borrow`  
`manual_repay`  
amt | String | Amount  
accBorrowed | String | Accumulated borrow amount  
ts | String | Timestamp for the event, Unix timestamp format in milliseconds, e.g. `1597026383085`

---

# 获取借/还币历史

获取`现货模式`下的借/还币历史。  
  
#### 限速：5次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/account/spot-borrow-repay-history`

> 请求示例
    
    
    GET /api/v5/account/spot-borrow-repay-history
    
    
    
    import okx.Account as Account
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘:1
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    result = accountAPI.spot_borrow_repay_history(ccy="USDT", type="auto_borrow")
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 否 | 币种，如 `BTC`  
type | String | 否 | 事件类型  
`auto_borrow`：自动借币  
`auto_repay`：自动还币  
`manual_borrow`：手动借币  
`manual_repay`：手动还币  
after | String | 否 | 请求发生时间`ts`之前（包含）的分页内容，Unix时间戳的毫秒数格式，如 `1597026383085`  
before | String | 否 | 请求发生时间`ts`之后（包含）的分页内容，Unix时间戳的毫秒数格式，如 `1597026383085`  
limit | String | 否 | 返回结果的数量，最大为100，默认100条  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "accBorrowed": "0",
                "amt": "6764.802661157592",
                "ccy": "USDT",
                "ts": "1725330976644",
                "type": "auto_repay"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ccy | String | 币种，如 `BTC`  
type | String | 事件类型  
`auto_borrow`：自动借币  
`auto_repay`：自动还币  
`manual_borrow`：手动借币  
`manual_repay`：手动还币  
amt | String | 数量  
accBorrowed | String | 累计借币数量  
ts | String | 事件发生时间，Unix时间戳的毫秒数格式，如 `1597026383085`