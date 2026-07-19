---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#sub-account-rest-api-get-sub-account-list
anchor_id: sub-account-rest-api-get-sub-account-list
api_type: REST
updated_at: 2026-07-19 19:16:53.443544
---

# Get sub-account list

Applies to master accounts only  
  
#### Rate limit：20 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP request

`GET /api/v5/users/subaccount/list`

> Request sample
    
    
    GET /api/v5/users/subaccount/list
    
    
    
    
    import okx.SubAccount as SubAccount
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading: 0, Demo trading: 1
    
    subAccountAPI = SubAccount.SubAccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # Get sub-account list
    result = subAccountAPI.get_subaccount_list()
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
enable | String | No | Sub-account status   
`true`: Normal `false`: Frozen  
subAcct | String | No | Sub-account name  
after | String | No | Query the data earlier than the requested subaccount creation timestamp, the value should be a Unix timestamp in millisecond format. e.g. `1597026383085`  
before | String | No | Query the data newer than the requested subaccount creation timestamp, the value should be a Unix timestamp in millisecond format. e.g. `1597026383085`  
limit | String | No | Number of results per request. The maximum is 100. The default is 100.  
  
> Returned results
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "canTransOut": false,
                "enable": true,
                "frozenFunc": [
                ],
                "gAuth": false,
                "label": "D456DDDLx",
                "mobile": "",
                "subAcct": "D456DDDL",
                "ts": "1659334756000",
                "type": "1",
                "uid": "3400***********7413",
                "subAcctLv": "1",
                "firstLvSubAcct": "D456DDDL",
                "ifDma": false
            }
        ]
    }
    

#### Response parameters

**Parameter name** | **Type** | **Description**  
---|---|---  
type | String | Sub-account type   
`1`: Standard sub-account   
`2`: Managed trading sub-account   
`5`: Custody trading sub-account - Copper  
`9`: Managed trading sub-account - Copper  
`12`: Custody trading sub-account - Komainu  
enable | Boolean | Sub-account status  
`true`: Normal  
`false`: Frozen (global)  
subAcct | String | Sub-account name  
uid | String | Sub-account uid  
label | String | Sub-account note  
mobile | String | Mobile number that linked with the sub-account.  
gAuth | Boolean | If the sub-account switches on the Google Authenticator for login authentication.   
`true`: On `false`: Off  
frozenFunc | Array of strings | Frozen functions  
`trading`  
`convert`  
`transfer`  
`withdrawal`  
`deposit`  
`flexible_loan`  
canTransOut | Boolean | Whether the sub-account has the right to transfer out.   
`true`: can transfer out   
`false`: cannot transfer out  
ts | String | Sub-account creation time, Unix timestamp in millisecond format. e.g. `1597026383085`  
subAcctLv | String | Sub-account level   
`1`: First level sub-account  
`2`: Second level sub-account.  
firstLvSubAcct | String | The first level sub-account.   
For subAcctLv: 1, firstLvSubAcct is equal to subAcct  
For subAcctLv: 2, subAcct belongs to firstLvSubAcct.  
ifDma | Boolean | Whether it is dma broker sub-account.   
`true`: Dma broker sub-account  
`false`: It is not dma broker sub-account.

---

# 查看子账户列表

仅适用于母账户  
  
#### 限速：20次/2s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/users/subaccount/list`

> 请求示例
    
    
    GET /api/v5/users/subaccount/list
    
    
    
    
    import okx.SubAccount as SubAccount
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘：1
    
    subAccountAPI = SubAccount.SubAccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # 查看子账户列表
    result = subAccountAPI.get_subaccount_list()
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
enable | String | 否 | 子账户状态   
`true`: 正常使用 `false`: 冻结  
subAcct | String | 否 | 子账户名称  
after | String | 否 | 查询在此之前的内容，值为子账户创建时间戳，Unix时间戳为毫秒数格式  
before | String | 否 | 查询在此之后的内容，值为子账户创建时间戳，Unix时间戳为毫秒数格式  
limit | String | 否 | 分页返回的结果集数量，最大为100，不填默认返回100条  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "canTransOut": false,
                "enable": true,
                "frozenFunc": [
                ],
                "gAuth": false,
                "label": "D456DDDLx",
                "mobile": "",
                "subAcct": "D456DDDL",
                "ts": "1659334756000",
                "type": "1",
                "uid": "3400***********7413",
                "subAcctLv": "1",
                "firstLvSubAcct": "D456DDDL",
                "ifDma": false
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
type | String | 子账户类型   
`1`：普通子账户   
`2`：资管子账户   
`5`：托管交易子账户 - Copper  
`9`：资管交易子账户 - Copper  
`12`：托管交易子账户 - Komainu  
enable | Boolean | 子账户状态   
`true`：正常使用 `false`：冻结（全局）  
subAcct | String | 子账户名称  
uid | String | 子账户UID  
label | String | 子账户备注  
mobile | String | 子账户绑定手机号  
gAuth | Boolean | 子账户是否开启的登录时的谷歌验证  
`true`：已开启  
`false`：未开启  
frozenFunc | Array of strings | 被冻结的功能  
`trading`：交易  
`convert`：闪兑  
`transfer`：母子账户间资金划转  
`withdrawal`：提币  
`deposit`：充值  
`flexible_loan`：活期借币  
canTransOut | Boolean | 是否可以主动转出  
`true`：可以转出   
`false`：不可转出  
ts | String | 子账户创建时间，Unix时间戳的毫秒数格式 ，如 `1597026383085`  
subAcctLv | String | 子账户层级   
`1`: 一级子账号  
`2`: 二级子账户  
firstLvSubAcct | String | 一级子账号   
对于 subAcctLv: 1, firstLvSubAcct 与 subAcct 相等。  
对于 subAcctLv: 2, subAcct 属于 firstLvSubAcct。  
ifDma | Boolean | 是否为 DMA 经济商子账号。   
`true`: DMA 经济商子账号。  
`false`: 非 DMA 经济商子账号。