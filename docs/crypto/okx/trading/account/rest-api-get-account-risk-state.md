---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#trading-account-rest-api-get-account-risk-state
anchor_id: trading-account-rest-api-get-account-risk-state
api_type: REST
updated_at: 2026-07-17 19:15:50.781001
---

# Get account risk state

Only applicable to Portfolio margin account  
  
#### Rate Limit: 10 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/account/risk-state`

> Request Example
    
    
    GET /api/v5/account/risk-state
    
    
    
    import okx.Account as Account
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading:0 , demo trading:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # Get account risk state
    result = accountAPI.get_account_position_risk()
    print(result)
    

> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "atRisk": false,
                "atRiskIdx": [],
                "atRiskMgn": [],
                "ts": "1635745078794"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameters** | **Types** | **Description**  
---|---|---  
atRisk | Boolean | Account risk status in auto-borrow mode   
true: the account is currently in a specific risk state   
false: the account is currently not in a specific risk state  
atRiskIdx | Array of strings | derivatives risk unit list  
atRiskMgn | Array of strings | margin risk unit list  
ts | String | Unix timestamp format in milliseconds, e.g.`1597026383085`

---

# 查看账户特定风险状态

仅适用于PM账户  
  
#### 限速：10次/2s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/account/risk-state`

> 请求示例
    
    
    GET /api/v5/account/risk-state
    
    
    
    
    import okx.Account as Account
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # 查看账户持仓风险
    result = accountAPI.get_account_position_risk()
    print(result)
    

> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "atRisk": false,
                "atRiskIdx": [],
                "atRiskMgn": [],
                "ts": "1635745078794"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
atRisk | Boolean | 自动借币模式下的账户风险状态  
true： 当前账户为特定风险状态  
false： 当前不是特定风险状态  
atRiskIdx | Array of strings | 衍生品的risk unit列表  
atRiskMgn | Array of strings | 杠杆的risk unit列表  
ts | String | 接口数据返回时间 ，Unix时间戳的毫秒数格式，如 `1597026383085`  
当账户进入特定风险状态后，仅可以委托降低账户风险方向的IOC类型订单.