---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#funding-account-rest-api-funds-transfer
anchor_id: funding-account-rest-api-funds-transfer
api_type: REST
updated_at: 2026-07-19 19:16:42.022147
---

# Funds transfer

Only API keys with `Trade` privilege can call this endpoint.  
  
This endpoint supports the transfer of funds between your funding account and trading account, and from the master account to sub-accounts.

Sub-account can transfer out to master account by default. Need to call [Set permission of transfer out](/docs-v5/en/#sub-account-rest-api-set-permission-of-transfer-out) to grant privilege first if you want sub-account transferring to another sub-account (sub-accounts need to belong to same master account.)

The success or failure of the request does not necessarily reflect the actual transfer result. Recommend checking the transfer status by calling "Get funds transfer state" to confirm the final result. 

#### Rate Limit: 2 requests per second

#### Rate limit rule: User ID + Currency

#### HTTP Request

`POST /api/v5/asset/transfer`

> Request Example
    
    
    # Transfer 1.5 USDT from funding account to Trading account when current account is master-account
    POST /api/v5/asset/transfer
    body
    {
        "ccy":"USDT",
        "amt":"1.5",
        "from":"6",
        "to":"18"
    }
    
    # Transfer 1.5 USDT from funding account to subAccount when current account is master-account
    POST /api/v5/asset/transfer
    body
    {
        "ccy":"USDT",
        "type":"1",
        "amt":"1.5",
        "from":"6",
        "to":"6",
        "subAcct":"mini"
    }
    
    # Transfer 1.5 USDT from funding account to subAccount when current account is sub-account
    POST /api/v5/asset/transfer
    body 
    {
        "ccy":"USDT",
        "type":"4",
        "amt":"1.5",
        "from":"6",
        "to":"6",
        "subAcct":"mini"
    }
    
    
    
    import okx.Funding as Funding
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading: 0, Demo trading: 1
    
    fundingAPI = Funding.FundingAPI(apikey, secretkey, passphrase, False, flag)
    
    # Funds transfer
    result = fundingAPI.funds_transfer(
        ccy="USDT",
        amt="1.5",
        from_="6",
        to="18"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
type | String | No | Transfer type  
`0`: transfer within account  
`1`: master account to sub-account (Only applicable to API Key from master account)  
`2`: sub-account to master account (Only applicable to API Key from master account)  
`3`: sub-account to master account (Only applicable to APIKey from sub-account)  
`4`: sub-account to sub-account (Only applicable to APIKey from sub-account, and target account needs to be another sub-account which belongs to same master account. Sub-account directly transfer out permission is disabled by default, set permission please refer to [Set permission of transfer out](/docs-v5/en/#sub-account-rest-api-set-permission-of-transfer-out))  
The default is `0`.  
If you want to make transfer between sub-accounts by master account API key, refer to [Master accounts manage the transfers between sub-accounts](/docs-v5/en/#sub-account-rest-api-master-accounts-manage-the-transfers-between-sub-accounts)  
ccy | String | Yes | Transfer currency, e.g. `USDT`  
amt | String | Yes | Amount to be transferred  
from | String | Yes | The remitting account  
`6`: Funding account  
`18`: Trading account  
to | String | Yes | The beneficiary account  
`6`: Funding account  
`18`: Trading account  
subAcct | String | Conditional | Name of the sub-account  
When `type` is `1`/`2`/`4`, this parameter is required.  
loanTrans | Boolean | No | Whether or not borrowed coins can be transferred out under `Spot mode`/`Multi-currency margin`/`Portfolio margin`  
`true`: borrowed coins can be transferred out  
`false`: borrowed coins cannot be transferred out  
the default is `false`  
omitPosRisk | String | No | Ignore position risk  
Default is `false`  
Applicable to `Portfolio margin`  
clientId | String | No | Client-supplied ID  
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
  
> Response Example
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
        {
          "transId": "754147",
          "ccy": "USDT",
          "clientId": "",
          "from": "6",
          "amt": "0.1",
          "to": "18"
        }
      ]
    }
    

#### Response Parameters

> Response Example

Parameter | Type | Description  
---|---|---  
transId | String | Transfer ID  
clientId | String | Client-supplied ID  
ccy | String | Currency  
from | String | The remitting account  
amt | String | Transfer amount  
to | String | The beneficiary account

---

# 资金划转

调用时，API Key 需要有交易权限。  
  
支持母账户的资金账户划转到交易账户，母账户到子账户的资金账户和交易账户划转。

子账户默认可转出至母账户，划转到同一母账户下的其他子账户，需要先调用 [设置子账户主动转出权限](/docs-v5/zh/#sub-account-rest-api-set-permission-of-transfer-out) 接口进行授权。

请求的成功或失败不一定反映实际的划转结果，建议通过调用"获取资金划转状态"接口来确认最终结果。 

#### 限速：2 次/s

#### 限速规则：User ID + Currency

#### HTTP 请求

`POST /api/v5/asset/transfer`

> 请求示例
    
    
    # 母账户USDT从资金账户划转1.5USDT到交易账户
    POST /api/v5/asset/transfer
    body 
    {
        "ccy":"USDT",
        "amt":"1.5",
        "from":"6",
        "to":"18"
    }
    
    # 母账户从资金账户划转1.5USDT到子账户的资金账户
    POST /api/v5/asset/transfer
    body 
    {
        "ccy":"USDT",
        "type":"1",
        "amt":"1.5",
        "from":"6",
        "to":"6",
        "subAcct":"mini"
    }
    
    # 子账户从资金账户划转1.5USDT到另一子账户的资金账户
    POST /api/v5/asset/transfer
    body 
    {
        "ccy":"USDT",
        "type":"4",
        "amt":"1.5",
        "from":"6",
        "to":"6",
        "subAcct":"mini"
    }
    
    
    
    import okx.Funding as Funding
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    fundingAPI = Funding.FundingAPI(apikey, secretkey, passphrase, False, flag)
    
    # 资金划转
    result = fundingAPI.funds_transfer(
        ccy="USDT",
        amt="1.5",
        from_="6",
        to="18"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
type | String | 否 | 划转类型  
`0`：账户内划转  
`1`：母账户转子账户(仅适用于母账户APIKey)  
`2`：子账户转母账户(仅适用于母账户APIKey)  
`3`：子账户转母账户(仅适用于子账户APIKey)  
`4`：子账户转子账户(仅适用于子账户APIKey，且目标账户需要是同一母账户下的其他子账户。子账户主动转出权限默认是关闭的，权限调整参考 [设置子账户主动转出权限](/docs-v5/zh/#sub-account-rest-api-set-permission-of-transfer-out)。)  
默认是`0`  
如果您希望通过母账户API Key控制子账户之间的划转，参考接口 [子账户间资金划转](/docs-v5/zh/#sub-account-rest-api-master-accounts-manage-the-transfers-between-sub-accounts)  
ccy | String | 是 | 划转币种，如 `USDT`  
amt | String | 是 | 划转数量  
from | String | 是 | 转出账户  
`6`：资金账户  
`18`：交易账户  
to | String | 是 | 转入账户  
`6`：资金账户  
`18`：交易账户  
subAcct | String | 可选 | 子账户名称  
当`type`为`1`/`2`/`4`时，该字段必填  
loanTrans | Boolean | 否 | 是否支持`现货模式`/`跨币种保证金模式`/`组合保证金模式`下的借币转出  
`true`：支持借币转出  
`false`：不支持借币转出  
默认为`false`  
omitPosRisk | String | 否 | 是否忽略仓位风险  
默认为`false`  
仅适用于`组合保证金模式`  
clientId | String | 否 | 客户自定义ID  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度要在1-32位之间。  
  
> 返回结果
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
        {
          "transId": "754147",
          "ccy": "USDT",
          "clientId": "",
          "from": "6",
          "amt": "0.1",
          "to": "18"
        }
      ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
transId | String | 划转 ID  
ccy | String | 划转币种  
from | String | 转出账户  
amt | String | 划转量  
to | String | 转入账户  
clientId | String | 客户自定义ID