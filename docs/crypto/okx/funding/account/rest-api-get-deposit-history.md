---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#funding-account-rest-api-get-deposit-history
anchor_id: funding-account-rest-api-get-deposit-history
api_type: REST
updated_at: 2026-06-29 19:57:36.499912
---

# Get deposit history

Retrieve the deposit records according to the currency, deposit status, and time range in reverse chronological order. The 100 most recent records are returned by default.  
Websocket API is also available, refer to [Deposit info channel](/docs-v5/en/#funding-account-websocket-deposit-info-channel).  
  
#### Rate Limit: 6 requests per second

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/asset/deposit-history`

> Request Example
    
    
    GET /api/v5/asset/deposit-history
    
    # Query deposit history from 2022-06-01 to 2022-07-01
    GET /api/v5/asset/deposit-history?ccy=BTC&after=1654041600000&before=1656633600000
    
    
    
    
    import okx.Funding as Funding
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading: 0, Demo trading: 1
    
    fundingAPI = Funding.FundingAPI(apikey, secretkey, passphrase, False, flag)
    
    # Get deposit history
    result = fundingAPI.get_deposit_history()
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
ccy | String | No | Currency, e.g. `BTC`  
depId | String | No | Deposit ID  
fromWdId | String | No | Internal transfer initiator's withdrawal ID  
If the deposit comes from internal transfer, this field displays the withdrawal ID of the internal transfer initiator  
txId | String | No | Hash record of the deposit  
type | String | No | Deposit Type  
`3`: internal transfer  
`4`: deposit from chain  
state | String | No | Status of deposit   
`0`: waiting for confirmation  
`1`: deposit credited   
`2`: deposit successful   
`8`: pending due to temporary deposit suspension on this crypto currency  
`11`: match the address blacklist  
`12`: account or deposit is frozen  
`13`: sub-account deposit interception  
`14`: KYC limit  
`17`: Pending response from Travel Rule vendor  
after | String | No | Pagination of data to return records earlier than the requested ts, Unix timestamp format in milliseconds, e.g. `1654041600000`  
before | String | No | Pagination of data to return records newer than the requested ts, Unix timestamp format in milliseconds, e.g. `1656633600000`  
limit | string | No | Number of results per request. The maximum is `100`; The default is `100`  
  
> Response Example
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
        {
            "actualDepBlkConfirm": "2",
            "amt": "1",
            "areaCodeFrom": "",
            "ccy": "USDT",
            "chain": "USDT-TRC20",
            "depId": "88****33",
            "from": "",
            "fromWdId": "",
            "state": "2",
            "to": "TN4hGjVXMzy*********9b4N1aGizqs",
            "ts": "1674038705000",
            "txId": "fee235b3e812********857d36bb0426917f0df1802"
        }
      ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ccy | String | Currency  
chain | String | Chain name  
amt | String | Deposit amount  
from | String | Deposit account  
If the deposit comes from an internal transfer, this field displays the account information of the internal transfer initiator, which can be a mobile phone number or email address (masked), and will return "" in other cases  
areaCodeFrom | String | If `from` is a phone number, this parameter return area code of the phone number  
to | String | Deposit address  
If the deposit comes from the on-chain, this field displays the on-chain address, and will return "" in other cases  
txId | String | Hash record of the deposit  
ts | String | The timestamp that the deposit record is created, Unix timestamp format in milliseconds, e.g. `1655251200000`  
state | String | Status of deposit  
`0`: Waiting for confirmation  
`1`: Deposit credited   
`2`: Deposit successful   
`8`: Pending due to temporary deposit suspension on this crypto currency  
`11`: Match the address blacklist  
`12`: Account or deposit is frozen  
`13`: Sub-account deposit interception  
`14`: KYC limit  
depId | String | Deposit ID  
fromWdId | String | Internal transfer initiator's withdrawal ID  
If the deposit comes from internal transfer, this field displays the withdrawal ID of the internal transfer initiator, and will return "" in other cases  
actualDepBlkConfirm | String | The actual amount of blockchain confirmed in a single deposit  
About deposit state  
**Waiting for confirmation** is that the required number of blockchain confirmations has not been reached.   
**Deposit credited** is that there is sufficient number of blockchain confirmations for the currency to be credited to the account, but it cannot be withdrawn yet.   
**Deposit successful** means the crypto has been credited to the account and it can be withdrawn.

---

# 获取充值记录

根据币种，充值状态，时间范围获取充值记录，按照时间倒序排列，默认返回 100 条数据。  
支持Websocket订阅，参考 [充值信息频道](/docs-v5/zh/#funding-account-websocket-deposit-info-channel)。  
  
#### 限速：6次/s

#### 限速规则：User ID

#### 权限：读取

#### HTTP 请求

`GET /api/v5/asset/deposit-history`

> 请求示例
    
    
    # 查询最近的充值记录
    GET /api/v5/asset/deposit-history
    
    # 查询从2022年06月01日到2022年07月01日之间的BTC的充值记录
    GET /api/v5/asset/deposit-history?ccy=BTC&after=1654041600000&before=1656633600000
    
    
    
    
    import okx.Funding as Funding
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    fundingAPI = Funding.FundingAPI(apikey, secretkey, passphrase, False, flag)
    
    # 获取充值记录
    result = fundingAPI.get_deposit_history()
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 否 | 币种名称，如 `BTC`  
depId | String | 否 | 充值记录 ID  
fromWdId | String | 否 | 内部转账发起者提币申请 ID  
如果该笔充值来自于内部转账，则该字段展示内部转账发起者的提币申请 ID  
txId | String | 否 | 区块转账哈希记录  
type | String | 否 | 充值方式  
`3`：内部转账  
`4`：链上充值  
state | String | 否 | 充值状态  
`0`：等待确认  
`1`：确认到账  
`2`：充值成功  
`8`：因该币种暂停充值而未到账，恢复充值后自动到账  
`11`：命中地址黑名单  
`12`：账户或充值被冻结  
`13`：子账户充值拦截  
`14`：KYC限额  
`17`：钱包地址正等待国际转账规则认证  
after | String | 否 | 查询在此之前的内容，值为时间戳，Unix 时间戳为毫秒数格式，如 `1654041600000`  
before | String | 否 | 查询在此之后的内容，值为时间戳，Unix 时间戳为毫秒数格式，如 `1656633600000`  
limit | string | 否 | 返回的结果集数量，默认为100，最大为100，不填默认返回100条  
  
> 返回结果
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
        {
            "actualDepBlkConfirm": "2",
            "amt": "1",
            "areaCodeFrom": "",
            "ccy": "USDT",
            "chain": "USDT-TRC20",
            "depId": "88****33",
            "from": "",
            "fromWdId": "",
            "state": "2",
            "to": "TN4hGjVXMzy*********9b4N1aGizqs",
            "ts": "1674038705000",
            "txId": "fee235b3e812********857d36bb0426917f0df1802"
        }
      ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ccy | String | 币种名称，如 `BTC`  
chain | String | 币种链信息  
有的币种下有多个链，必须要做区分，如`USDT`下有`USDT-ERC20`，`USDT-TRC20`多个链  
amt | String | 充值数量  
from | String | 充值账户  
如果该笔充值来自于内部转账，则该字段展示内部转账发起者的账户信息，可以是手机号或邮箱（脱敏），其他情况返回""  
areaCodeFrom | String | 如果`from`为手机号，该字段为该手机号的区号  
to | String | 到账地址  
如果该笔充值来自于链上充值，则该字段展示链上地址，其他情况返回""  
txId | String | 区块转账哈希记录  
ts | String | 充值记录创建时间，Unix 时间戳的毫秒数格式，如 `1655251200000`  
state | String | 充值状态  
`0`：等待确认   
`1`：确认到账   
`2`：充值成功   
`8`：因该币种暂停充值而未到账，恢复充值后自动到账  
`11`：命中地址黑名单  
`12`：账户或充值被冻结  
`13`：子账户充值拦截  
`14`：KYC限额  
depId | String | 充值记录 ID  
fromWdId | String | 内部转账发起者提币申请 ID  
如果该笔充值来自于内部转账，则该字段展示内部转账发起者的提币申请 ID，其他情况返回""  
actualDepBlkConfirm | String | 最新的充币网络确认数  
关于充值状态  
**等待确认** 是没有达到充币确认数。  
**确认到账** 是够充币确认数，且币已经到账户中，但是不可提。  
**充值成功** 是当前账户完成到提币确认，可以提出。