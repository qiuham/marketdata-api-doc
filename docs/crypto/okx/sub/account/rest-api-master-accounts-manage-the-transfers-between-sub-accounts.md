---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#sub-account-rest-api-master-accounts-manage-the-transfers-between-sub-accounts
anchor_id: sub-account-rest-api-master-accounts-manage-the-transfers-between-sub-accounts
api_type: REST
updated_at: 2026-07-14 19:20:55.417261
---

# Master accounts manage the transfers between sub-accounts

Applies to master accounts only.   
  
Only API keys with `Trade` privilege can call this endpoint.

#### Rate limit：1 request per second

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP request

`POST /api/v5/asset/subaccount/transfer`

> Request sample
    
    
    POST /api/v5/asset/subaccount/transfer
    body
    {
        "ccy":"USDT",
        "amt":"1.5",
        "from":"6",
        "to":"6",
        "fromSubAccount":"test-1",
        "toSubAccount":"test-2"
    }
    
    
    
    import okx.SubAccount as SubAccount
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading: 0, Demo trading: 1
    
    subAccountAPI = SubAccount.SubAccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # Master accounts manage the transfers between sub-accounts
    result = subAccountAPI.subAccount_transfer(
        ccy="USDT",
        amt="10",
        froms="6",
        to="6",
        fromSubAccount="test-1",
        toSubAccount="test-2"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
ccy | String | Yes | Currency  
amt | String | Yes | Transfer amount  
from | String | Yes | Account type of transfer from sub-account  
`6`: Funding Account  
`18`: Trading account  
to | String | Yes | Account type of transfer to sub-account  
`6`: Funding Account  
`18`: Trading account  
fromSubAccount | String | Yes | Sub-account name of the account that transfers funds out.  
toSubAccount | String | Yes | Sub-account name of the account that transfers funds in.  
loanTrans | Boolean | No | Whether or not borrowed coins can be transferred out under `Multi-currency margin`/`Portfolio margin`  
The default is `false`  
omitPosRisk | String | No | Ignore position risk  
Default is `false`  
Applicable to `Portfolio margin`  
  
> Returned results
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "transId":"12345",
            }
        ]
    }
    

#### Response parameters

**Parameter name** | **Type** | **Description**  
---|---|---  
transId | String | Transfer ID

---

# 子账户间资金划转

母账户控制子账户与子账户之间划转（仅适用于母账户）  
  
调用时，APIKey 需要有交易权限

#### 限速：1次/s

#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/asset/subaccount/transfer`

> 请求示例
    
    
    POST /api/v5/asset/subaccount/transfer
    body
    {
        "ccy":"USDT",
        "amt":"1.5",
        "from":"6",
        "to":"6",
        "fromSubAccount":"test-1",
        "toSubAccount":"test-2"
    }
    
    
    
    import okx.SubAccount as SubAccount
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘：1
    
    subAccountAPI = SubAccount.SubAccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # 子账户间资金划转
    result = subAccountAPI.subAccount_transfer(
        ccy="USDT",
        amt="10",
        froms="6",
        to="6",
        fromSubAccount="test-1",
        toSubAccount="test-2"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 是 | 币种  
amt | String | 是 | 划转数量  
from | String | 是 | 转出子账户类型  
`6`：资金账户  
`18`：交易账户  
to | String | 是 | 转入子账户类型  
`6`：资金账户  
`18`：交易账户  
fromSubAccount | String | 是 | 转出子账户的子账户名称  
toSubAccount | String | 是 | 转入子账户的子账户名称  
loanTrans | Boolean | 否 | 是否支持`跨币种保证金模式`或`组合保证金模式`下的借币转入/转出  
默认`false`  
omitPosRisk | String | 否 | 是否忽略仓位风险  
默认为`false`  
仅适用于`组合保证金模式`  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "transId":"12345",
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
transId | String | 划转ID