---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#trading-account-rest-api-get-account-configuration
anchor_id: trading-account-rest-api-get-account-configuration
api_type: REST
updated_at: 2026-07-20 19:35:08.342675
---

# Get account configuration

Retrieve current account configuration.  
  
#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/account/config`

> Request Example
    
    
    GET /api/v5/account/config
    
    
    
    
    import okx.Account as Account
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading:0 , demo trading:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # Retrieve current account configuration
    result = accountAPI.get_account_config()
    print(result)
    

#### Request Parameters

none

> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "acctLv": "2",
                "acctStpMode": "cancel_maker",
                "autoLoan": false,
                "ctIsoMode": "automatic",
                "enableSpotBorrow": false,
                "greeksType": "PA",
                "feeType": "0",
                "ip": "",
                "type": "0",
                "kycLv": "3",
                "label": "v5 test",
                "level": "Lv1",
                "levelTmp": "",
                "liquidationGear": "-1",
                "mainUid": "44705892343619584",
                "mgnIsoMode": "automatic",
                "opAuth": "1",
                "perm": "read_only,withdraw,trade",
                "posMode": "long_short_mode",
                "roleType": "0",
                "spotBorrowAutoRepay": false,
                "spotOffsetType": "",
                "spotRoleType": "0",
                "spotTraderInsts": [],
                "stgyType": "0",
                "traderInsts": [],
                "uid": "44705892343619584",
                "settleCcy": "USDC",
                "settleCcyList": ["USD", "USDC", "USDG"]
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
uid | String | Account ID of current request.  
mainUid | String | Main Account ID of current request.   
The current request account is main account if uid = mainUid.  
The current request account is sub-account if uid != mainUid.  
acctLv | String | Account mode   
`1`: Spot mode  
`2`: Futures mode  
`3`: Multi-currency margin  
`4`: Portfolio margin  
acctStpMode | String | Account self-trade prevention mode   
`cancel_maker`   
`cancel_taker`   
`cancel_both`   
The default value is `cancel_maker`. Users can log in to the webpage through the master account to modify this configuration  
posMode | String | Position mode  
`long_short_mode`: long/short, only applicable to `FUTURES`/`SWAP`  
`net_mode`: net  
autoLoan | Boolean | Whether to borrow coins automatically  
`true`: borrow coins automatically  
`false`: not borrow coins automatically  
greeksType | String | Current display type of Greeks  
`PA`: Greeks in coins  
`BS`: Black-Scholes Greeks in dollars  
feeType | String | Fee type  
`0`: fee is charged in the currency you receive from the trade  
`1`: fee is always charged in the quote currency of the trading pair  
level | String | The user level of the current real trading volume on the platform, e.g `Lv1`, which means regular user level.  
levelTmp | String | Temporary experience user level of special users, e.g `Lv1`  
ctIsoMode | String | Contract isolated margin trading settings  
`automatic`: Auto transfers  
`autonomy`: Manual transfers  
mgnIsoMode | String | Margin isolated margin trading settings  
`auto_transfers_ccy`: New auto transfers, enabling both base and quote currency as the margin for isolated margin trading  
`automatic`: Auto transfers  
`quick_margin`: Quick Margin Mode (For new accounts, including subaccounts, some defaults will be `automatic`, and others will be `quick_margin`)  
spotOffsetType | String | ~~Risk offset type  
`1`: Spot-Derivatives(USDT) to be offsetted  
`2`: Spot-Derivatives(Coin) to be offsetted  
`3`: Only derivatives to be offsetted  
Only applicable to `Portfolio margin`~~  
(Deprecated)  
stgyType | String | Strategy type  
`0`: general strategy  
`1`: delta neutral strategy  
roleType | String | Role type  
`0`: General user  
`1`: Leading trader  
`2`: Copy trader  
traderInsts | Array of strings | Leading trade instruments, only applicable to Leading trader  
spotRoleType | String | SPOT copy trading role type.  
`0`: General user；`1`: Leading trader；`2`: Copy trader  
spotTraderInsts | Array of strings | Spot lead trading instruments, only applicable to lead trader  
opAuth | String | Whether the optional trading was activated  
`0`: not activate  
`1`: activated  
kycLv | String | Main account KYC level  
`0`: No verification  
`1`: level 1 completed  
`2`: level 2 completed  
`3`: level 3 completed  
If the request originates from a subaccount, kycLv is the KYC level of the main account.   
If the request originates from the main account, kycLv is the KYC level of the current account.  
label | String | API key note of current request API key. No more than 50 letters (case sensitive) or numbers, which can be pure letters or pure numbers.  
ip | String | IP addresses that linked with current API key, separate with commas if more than one, e.g. `117.37.203.58,117.37.203.57`. It is an empty string "" if there is no IP bonded.  
perm | String | The permission of the current requesting API key or Access token  
`read_only`: Read  
`trade`: Trade  
`withdraw`: Withdraw  
liquidationGear | String | The maintenance margin ratio level of liquidation alert  
`3` and `-1` means that you will get hourly liquidation alerts on app and channel "Position risk warning" when your margin level drops to or below 300%. `-1` is the initial value which has the same effect as `-3`   
`0` means that there is not alert  
enableSpotBorrow | Boolean | Whether borrow is allowed or not in `Spot mode`  
`true`: Enabled  
`false`: Disabled  
spotBorrowAutoRepay | Boolean | Whether auto-repay is allowed or not in `Spot mode`  
`true`: Enabled  
`false`: Disabled  
type | String | Account type   
`0`: Main account   
`1`: Standard sub-account   
`2`: Managed trading sub-account   
`5`: Custody trading sub-account - Copper  
`9`: Managed trading sub-account - Copper  
`12`: Custody trading sub-account - Komainu  
settleCcy | String | Current account's USD-margined contract settle currency  
settleCcyList | String | Current account's USD-margined contract settle currency list, like ["USD", "USDC", "USDG"].

---

# 查看账户配置

查看当前账户的配置信息。   
  
#### 限速：5次/2s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/account/config`

> 请求示例
    
    
    GET /api/v5/account/config
    
    
    
    
    import okx.Account as Account
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # 查看账户配置
    result = accountAPI.get_account_config()
    print(result)
    

#### 请求参数

无

> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "acctLv": "2",
                "acctStpMode": "cancel_maker",
                "autoLoan": false,
                "ctIsoMode": "automatic",
                "enableSpotBorrow": false,
                "greeksType": "PA",
                "feeType": "0",
                "ip": "",
                "type": "0",
                "kycLv": "3",
                "label": "v5 test",
                "level": "Lv1",
                "levelTmp": "",
                "liquidationGear": "-1",
                "mainUid": "44705892343619584",
                "mgnIsoMode": "automatic",
                "opAuth": "1",
                "perm": "read_only,withdraw,trade",
                "posMode": "long_short_mode",
                "roleType": "0",
                "spotBorrowAutoRepay": false,
                "spotOffsetType": "",
                "spotRoleType": "0",
                "spotTraderInsts": [],
                "stgyType": "0",
                "traderInsts": [],
                "uid": "44705892343619584",
                "settleCcy": "USDC",
                "settleCcyList": ["USD", "USDC", "USDG"]
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
uid | String | 当前请求的账户ID，账户uid和app上的一致  
mainUid | String | 当前请求的母账户ID  
如果 uid = mainUid，代表当前账号为母账户；如果 uid != mainUid，代表当前账户为子账户。  
acctLv | String | 账户模式  
`1`：现货模式  
`2`：合约模式  
`3`：跨币种保证金模式  
`4`：组合保证金模式  
acctStpMode | String | 账户自成交保护模式   
`cancel_maker`：撤销挂单   
`cancel_taker`：撤销吃单   
`cancel_both`：撤销挂单和吃单   
默认为`cancel_maker`，用户可通过母账户登录网页修改该配置  
posMode | String | 持仓方式  
`long_short_mode`：开平仓模式  
`net_mode`：买卖模式  
仅适用`交割/永续`  
autoLoan | Boolean | 是否自动借币  
`true`：自动借币 `false`：非自动借币  
greeksType | String | 当前希腊字母展示方式  
`PA`：币本位 `BS`：美元本位  
feeType | String | 手续费类型  
`0`：手续费以获取币种收取  
`1`：手续费以计价币种收取  
level | String | 当前在平台上真实交易量的用户等级，如 `Lv1`，代表普通用户等级。  
levelTmp | String | 特约用户的临时体验用户等级，如 `Lv1`  
ctIsoMode | String | 衍生品的逐仓保证金划转模式  
`automatic`：开仓划转  
`autonomy`：自主划转  
mgnIsoMode | String | 币币杠杆的逐仓保证金划转模式  
`automatic`：开仓划转  
`autonomy`：自主划转  
spotOffsetType | String | ~~现货对冲类型  
`1`：现货对冲模式U模式  
`2`：现货对冲模式币模式  
`3`：非现货对冲模式  
适用于`组合保证金模式`~~  
已废弃  
stgyType | String | 策略类型  
`0`：普通策略模式  
`1`：delta 中性策略模式  
roleType | String | 用户角色  
`0`：普通用户  
`1`：带单者  
`2`：跟单者  
traderInsts | Array of strings | 当前账号已经设置的带单合约，仅适用于带单者  
spotRoleType | String | 现货跟单角色。  
`0`：普通用户；`1`：带单者；`2`：跟单者  
spotTraderInsts | Array of strings | 当前账号已经设置的带单币对，仅适用于带单者  
opAuth | String | 是否开通期权交易  
`0`：未开通  
`1`：已经开通  
kycLv | String | 母账户KYC等级  
`0`: 未认证  
`1`: 已完成 level 1 认证  
`2`: 已完成 level 2 认证  
`3`: 已完成 level 3认证  
如果请求来自子账户, kycLv 为其母账户的等级  
如果请求来自母账户, kycLv 为当前请求的母账户等级  
label | String | 当前请求API key的备注名，不超过50位字母（区分大小写）或数字，可以是纯字母或纯数字。  
ip | String | 当前请求API key绑定的ip地址，多个ip用半角逗号隔开，如：`117.37.203.58,117.37.203.57`。  
如果没有绑定ip，会返回空字符串""  
perm | String | 当前请求的 API key 或 Access token 的权限  
`read_only`：读取  
`trade`：交易  
`withdraw`：提币  
liquidationGear | String | 强平提醒的维持保证金率水平  
`3` 和 `-1` 代表维持保证金率达到 300% 时，每隔 1 小时 app 和 ”爆仓风险预警推送频道“会推送通知。`-1` 是初始值，与`-3`有着同样效果  
`0` 代表不提醒  
enableSpotBorrow | Boolean | `现货模式`下是否支持借币  
`true`：支持  
`false`：不支持  
spotBorrowAutoRepay | Boolean | `现货模式`下是否支持自动还币  
`true`：支持  
`false`：不支持  
type | String | 账户类型   
`0`：母账户   
`1`：普通子账户   
`2`：资管子账户   
`5`：托管交易子账户 - Copper  
`9`：资管交易子账户 - Copper  
`12`：托管交易子账户 - Komainu  
settleCcy | String | 当前账户的 USD 本位合约结算币种  
settleCcyList | String | 当前账户的 USD 本位合约结算币种列表，如 ["USD", "USDC", "USDG"]。