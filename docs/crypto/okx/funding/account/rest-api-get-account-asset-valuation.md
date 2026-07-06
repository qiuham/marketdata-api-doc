---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#funding-account-rest-api-get-account-asset-valuation
anchor_id: funding-account-rest-api-get-account-asset-valuation
api_type: REST
updated_at: 2026-07-06 19:54:23.598561
---

# Get account asset valuation

View account asset valuation  
  
#### Rate Limit: 1 request per second

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/asset/asset-valuation`

> Request Example
    
    
    GET /api/v5/asset/asset-valuation
    
    
    
    import okx.Funding as Funding
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading: 0, Demo trading: 1
    
    fundingAPI = Funding.FundingAPI(apikey, secretkey, passphrase, False, flag)
    
    # Get account asset valuation
    result = fundingAPI.get_asset_valuation()
    print(result)
    

#### Request Parameters

**Parameters** | **Types** | **Required** | **Description**  
---|---|---|---  
ccy | String | No | Asset valuation calculation unit   
BTC, USDT  
USD, CNY, JP, KRW, RUB, EUR  
VND, IDR, INR, PHP, THB, TRY   
AUD, SGD, ARS, SAR, AED, IQD   
The default is the valuation in BTC.  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "details": {
                    "classic": "124.6",
                    "earn": "1122.73",
                    "funding": "0.09",
                    "trading": "2544.28"
                },
                "totalBal": "3790.09",
                "ts": "1637566660769"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
totalBal | String | Valuation of total account assets  
ts | String | Unix timestamp format in milliseconds, e.g.`1597026383085`  
details | Object | Asset valuation details for each account  
> funding | String | Funding account  
> trading | String | Trading account  
> classic | String | [Deprecated] Classic account  
> earn | String | Earn account

---

# 获取账户资产估值

查看账户资产估值  
  
#### 限速：1次/s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/asset/asset-valuation`

> 请求示例
    
    
    GET /api/v5/asset/asset-valuation
    
    
    
    import okx.Funding as Funding
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    fundingAPI = Funding.FundingAPI(apikey, secretkey, passphrase, False, flag)
    
    # 获取账户资产估值
    result = fundingAPI.get_asset_valuation()
    print(result)
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 否 | 资产估值对应的单位  
BTC 、USDT  
USD 、CNY 、JPY、KRW、RUB、EUR  
VND 、IDR 、INR、PHP、THB、TRY   
AUD 、SGD 、ARS、SAR、AED、IQD   
默认为`BTC`为单位的估值  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "details": {
                    "classic": "124.6",
                    "earn": "1122.73",
                    "funding": "0.09",
                    "trading": "2544.28"
                },
                "totalBal": "3790.09",
                "ts": "1637566660769"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
totalBal | String | 账户总资产估值  
ts | String | 数据更新时间，Unix时间戳的毫秒数格式，如 1597026383085  
details | Object | 各个账户的资产估值  
> funding | String | 资金账户  
> trading | String | 交易账户  
> classic | String | 经典账户 (已废弃)  
> earn | String | 金融账户