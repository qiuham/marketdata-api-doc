---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#funding-account-rest-api-get-funds-transfer-state
anchor_id: funding-account-rest-api-get-funds-transfer-state
api_type: REST
updated_at: 2026-07-03 19:40:50.621231
---

# Get funds transfer state

Retrieve the transfer state data of the last 2 weeks.  
  
#### Rate Limit: 10 requests per second

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/asset/transfer-state`

> Request Example
    
    
    GET /api/v5/asset/transfer-state?transId=1&type=1
    
    
    
    import okx.Funding as Funding
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading: 0, Demo trading: 1
    
    fundingAPI = Funding.FundingAPI(apikey, secretkey, passphrase, False, flag)
    
    # Get funds transfer state
    result = fundingAPI.transfer_state(
        transId="248424899",
        type="0"
    )
    print(result)
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
transId | String | Conditional | Transfer ID  
Either transId or clientId is required. If both are passed, transId will be used.  
clientId | String | Conditional | Client-supplied ID  
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
type | String | No | Transfer type  
`0`: transfer within account   
`1`: master account to sub-account (Only applicable to API Key from master account)   
`2`: sub-account to master account (Only applicable to API Key from master account)  
`3`: sub-account to master account (Only applicable to APIKey from sub-account)  
`4`: sub-account to sub-account (Only applicable to APIKey from sub-account, and target account needs to be another sub-account which belongs to same master account)  
The default is `0`.  
For Custody accounts, can choose not to pass this parameter or pass `0`.  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "amt": "1.5",
                "ccy": "USDT",
                "clientId": "",
                "from": "18",
                "instId": "", //deprecated
                "state": "success",
                "subAcct": "test",
                "to": "6",
                "toInstId": "", //deprecated
                "transId": "1",
                "type": "1"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
transId | String | Transfer ID  
clientId | String | Client-supplied ID  
ccy | String | Currency, e.g. `USDT`  
amt | String | Amount to be transferred  
type | String | Transfer type  
`0`: transfer within account  
`1`: master account to sub-account (Only applicable to API Key from master account)   
`2`: sub-account to master account (Only applicable to APIKey from master account)  
`3`: sub-account to master account (Only applicable to APIKey from sub-account)  
`4`: sub-account to sub-account (Only applicable to APIKey from sub-account, and target account needs to be another sub-account which belongs to same master account)  
from | String | The remitting account  
`6`: Funding account  
`18`: Trading account  
to | String | The beneficiary account  
`6`: Funding account  
`18`: Trading account  
subAcct | String | Name of the sub-account  
instId | String | deprecated  
toInstId | String | deprecated  
state | String | Transfer state  
`success`  
`pending`  
`failed`

---

# 获取资金划转状态

获取最近2个星期内的资金划转状态数据  
  
#### 限速：10 次/s

#### 限速规则：User ID

#### 权限：读取

#### HTTP 请求

`GET /api/v5/asset/transfer-state`

> 请求示例
    
    
    GET /api/v5/asset/transfer-state?transId=1&type=1
    
    
    
    import okx.Funding as Funding
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘: 0, 模拟盘: 1
    
    fundingAPI = Funding.FundingAPI(apikey, secretkey, passphrase, False, flag)
    
    # 获取资金划转状态
    result = fundingAPI.transfer_state(
        transId="248424899",
        type="0"
    )
    print(result)
    
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
transId | String | 可选 | 划转ID  
transId和clientId必须传一个，若传两个，以transId为主  
clientId | String | 可选 | 客户自定义ID  
type | String | 否 | 划转类型  
`0`：账户内划转  
`1`：母账户转子账户(仅适用于母账户APIKey)  
`2`：子账户转母账户(仅适用于母账户APIKey)  
`3`：子账户转母账户(仅适用于子账户APIKey)  
`4`：子账户转子账户(仅适用于子账户APIKey，且目标账户需要是同一母账户下的其他子账户)  
默认是`0`  
对于Custody账户该参数可以不传或者传0。  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "amt": "1.5",
                "ccy": "USDT",
                "clientId": "",
                "from": "18",
                "instId": "", //已废弃
                "state": "success",
                "subAcct": "test",
                "to": "6",
                "toInstId": "", //已废弃
                "transId": "1",
                "type": "1"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
transId | String | 划转 ID  
clientId | String | 客户自定义 ID  
ccy | String | 划转币种  
amt | String | 划转量  
type | String | 划转类型  
`0`：账户内划转  
`1`：母账户转子账户(仅适用于母账户APIKey)  
`2`：子账户转母账户(仅适用于母账户APIKey)  
`3`：子账户转母账户(仅适用于子账户APIKey)  
`4`：子账户转子账户(仅适用于子账户APIKey，且目标账户需要是同一母账户下的其他子账户)  
from | String | 转出账户  
`6`：资金账户  
`18`：交易账户  
to | String | 转入账户  
`6`：资金账户  
`18`：交易账户  
subAcct | String | 子账户名称  
instId | String | 已废弃  
toInstId | String | 已废弃  
state | String | 转账状态  
`success`：成功  
`pending`：处理中  
`failed`：失败