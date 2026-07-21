---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#trading-account-rest-api-get-interest-accrued-data
anchor_id: trading-account-rest-api-get-interest-accrued-data
api_type: REST
updated_at: 2026-07-21 19:25:18.334447
---

# Get interest accrued data

Get the interest accrued data for the past year

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/account/interest-accrued`

> Request Example
    
    
    GET /api/v5/account/interest-accrued
    
    
    
    
    import okx.Account as Account
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading:0 , demo trading:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # Get interest accrued data
    result = accountAPI.get_interest_accrued()
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
type | String | No | Loan type  
`2`: Market loans  
Default is `2`  
ccy | String | No | Loan currency, e.g. `BTC`  
Only applicable to `Market loans`  
Only applicable to`MARGIN`  
instId | String | No | Instrument ID, e.g. `BTC-USDT`  
Only applicable to `Market loans`  
mgnMode | String | No | Margin mode  
`cross`   
`isolated`  
Only applicable to `Market loans`  
after | String | No | Pagination of data to return records earlier than the requested timestamp, Unix timestamp format in milliseconds, e.g. `1597026383085`  
before | String | No | Pagination of data to return records newer than the requested, Unix timestamp format in milliseconds, e.g. `1597026383085`  
limit | String | No | Number of results per request. The maximum is `100`. The default is `100`.  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "ccy": "USDT",
                "instId": "",
                "interest": "0.0003960833333334",
                "interestRate": "0.0000040833333333",
                "liab": "97",
                "totalLiab": "",
                "interestFreeLiab": "",
                "mgnMode": "",
                "ts": "1637312400000",
                "type": "1"
            },
            {
                "ccy": "USDT",
                "instId": "",
                "interest": "0.0004083333333334",
                "interestRate": "0.0000040833333333",
                "liab": "100",
                "mgnMode": "",
                "ts": "1637049600000",
                "type": "1"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
type | String | Loan type  
`2`: Market loans  
ccy | String | Loan currency, e.g. `BTC`  
instId | String | Instrument ID, e.g. `BTC-USDT`  
Only applicable to `Market loans`  
mgnMode | String | Margin mode  
`cross`   
`isolated`  
interest | String | Interest accrued  
interestRate | String | Hourly borrowing interest rate  
liab | String | Liability  
totalLiab | String | Total liability for current account  
interestFreeLiab | String | Interest-free liability for current account  
ts | String | Timestamp for interest accrued, Unix timestamp format in milliseconds, e.g. `1597026383085`

---

# 获取计息记录

获取过去一年的计息记录

#### 限速：5次/2s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/account/interest-accrued`

> 请求示例
    
    
    GET /api/v5/account/interest-accrued
    
    
    
    
    import okx.Account as Account
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # 获取计息记录
    result = accountAPI.get_interest_accrued()
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
type | String | 否 | 借币类型  
`2`：市场借币  
默认为`2`  
ccy | String | 否 | 借贷币种，如 `BTC`  
仅适用于`市场借币`  
仅适用于`币币杠杆`  
instId | String | 否 | 产品ID，如 `BTC-USDT`  
仅适用于`市场借币`  
mgnMode | String | 否 | 保证金模式  
`cross`：全仓  
`isolated`：逐仓  
仅适用于`市场借币`  
after | String | 否 | 请求此时间戳之前（更旧的数据）的分页内容，Unix时间戳的毫秒数格式，如 `1597026383085`  
before | String | 否 | 请求此时间戳之后（更新的数据）的分页内容，Unix时间戳的毫秒数格式，如 `1597026383085`  
limit | String | 否 | 分页返回的结果集数量，最大为100，不填默认返回100条  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "ccy": "USDT",
                "instId": "",
                "interest": "0.0003960833333334",
                "interestRate": "0.0000040833333333",
                "liab": "97",
                "totalLiab": "",
                "interestFreeLiab": "",
                "mgnMode": "",
                "ts": "1637312400000",
                "type": "1"
            },
            {
                "ccy": "USDT",
                "instId": "",
                "interest": "0.0004083333333334",
                "interestRate": "0.0000040833333333",
                "liab": "100",
                "totalLiab": "",
                "interestFreeLiab": "",
                "mgnMode": "",
                "ts": "1637049600000",
                "type": "1"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
type | String | 类型  
`2`：市场借币  
ccy | String | 借贷币种，如 `BTC`  
instId | String | 产品ID，如 `BTC-USDT`  
仅适用于`市场借币`  
mgnMode | String | 保证金模式  
`cross`：全仓  
`isolated`：逐仓  
interest | String | 利息累计  
interestRate | String | 借款计息利率(小时)  
liab | String | 计息负债  
totalLiab | String | 当前账户总负债量  
interestFreeLiab | String | 当前账户免息负债量  
ts | String | 计息时间，Unix时间戳的毫秒数格式，如 `1597026383085`