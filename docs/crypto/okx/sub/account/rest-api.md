---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#sub-account-rest-api
anchor_id: sub-account-rest-api
api_type: REST
updated_at: 2026-07-10 19:32:28.391796
---

# REST API

### Get sub-account list  
  
Applies to master accounts only

#### Rate limit：20 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

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
  
### Create sub-account

Applies to master accounts only and master accounts API Key must be linked to IP addresses.

#### Rate limit：1 request per second

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP request

`POST /api/v5/users/subaccount/create-subaccount`

> Request sample
    
    
    POST /api/v5/users/subaccount/create-subaccount
    body
    {
        "subAcct": "subAccount002",
        "type": "1",
        "label": "123456"
    }
    
    
    
    import okx.SubAccount as SubAccount
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading: 0, Demo trading: 1
    
    subAccountAPI = SubAccount.SubAccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # Reset the API Key of a sub-account
    result = subAccountAPI.reset_subaccount_apikey(
        subAcct="hahawang1",
        apiKey="",
        ip=""
    )
    print(result)
    

#### Request Parameters

Parameter name | Type | Required | Description  
---|---|---|---  
subAcct | String | Yes | Sub-account name  
type | String | Yes | Sub-account type   
`1`: Standard sub-account   
`5`: Custody trading sub-account - Copper  
`12`: Custody trading sub-account - Komainu  
label | String | No | Sub-account notes. 6-32 letters (case sensitive), numbers or special characters like *.  
pwd | String | Conditional | Sub-account login password, it is required for KYB users only.  
Your password must contain:  
8 - 32 characters long.  
1 lowercase character (a-z).  
1 uppercase character (A-Z).  
1 number.  
1 special character e.g. ! @ # $ %  
  
> Returned results
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "label": "123456 ",
                "subAcct": "subAccount002",
                "ts": "1744875304520",
                "uid": "698827017768230914"
            }
        ]
    }
    

#### Response parameters

**Parameter name** | **Type** | **Description**  
---|---|---  
subAcct | String | Sub-account name  
label | String | Sub-account notes  
uid | String | Sub-account ID  
ts | String | Creation time  
  
### Create an API Key for a sub-account

Applies to master accounts only and master accounts API Key must be linked to IP addresses.

#### Rate limit：1 request per second

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP request

`POST /api/v5/users/subaccount/apikey`

> Request sample
    
    
    POST /api/v5/users/subaccount/apikey
    body
    {
        "subAcct":"panpanBroker2",
        "label":"broker3",
        "passphrase": "******",
        "perm":"trade"
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
subAcct | String | Yes | Sub-account name, supports 6 to 20 characters that include numbers and letters (case sensitive, space symbol is not supported).  
label | String | Yes | API Key note  
passphrase | String | Yes | API Key password, supports 8 to 32 alphanumeric characters containing at least 1 number, 1 uppercase letter, 1 lowercase letter and 1 special character.  
perm | String | No | API Key permissions   
`read_only`: Read only   
`trade`: Trade  
ip | String | No | Link IP addresses, separate with commas if more than one. Support up to 20 addresses.  
**For security reasons, it is recommended to bind IP addresses.**  
**API keys with trading or withdrawal permissions that are not bound to IPs will expire after 14 days of inactivity. (API keys in demo trading will not be deleted.)**  
  
> Returned result
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
            "subAcct": "test-1",
            "label": "v5",
            "apiKey": "******",
            "secretKey": "******",
            "passphrase": "******",
            "perm": "read_only,trade",
            "ip": "1.1.1.1,2.2.2.2",
            "ts": "1597026383085"
        }]
    }
    

#### Response parameters

**Parameter name** | **Type** | **Description**  
---|---|---  
subAcct | String | Sub-account name  
label | String | API Key note  
apiKey | String | API public key  
secretKey | String | API private key  
passphrase | String | API Key password  
perm | String | API Key access   
`read_only` : Read only `trade` : Trade  
ip | String | IP address that linked with API Key  
ts | String | Creation time  
  
### Query the API Key of a sub-account

Applies to master accounts only

#### Rate limit：20 request per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP request

`GET /api/v5/users/subaccount/apikey`

> Request sample
    
    
    GET /api/v5/users/subaccount/apikey?subAcct=panpanBroker2
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
subAcct | String | Yes | Sub-account name  
apiKey | String | No | API public key  
  
> Returned results
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "label": "v5",
                "apiKey": "******",
                "perm": "read_only,trade",
                "ip": "1.1.1.1,2.2.2.2",
                "ts": "1597026383085"
            },
            {
                "label": "v5.1",
                "apiKey": "******",
                "perm": "read_only",
                "ip": "1.1.1.1,2.2.2.2",
                "ts": "1597026383085"
            }
        ]
    }
    

#### Response parameters

**Parameter name** | **Type** | **Description**  
---|---|---  
label | String | API Key note  
apiKey | String | API public key  
perm | String | API Key access   
read_only: Read only; trade: Trade  
ip | String | IP address that linked with API Key  
ts | String | Creation time  
  
### Reset the API Key of a sub-account

Applies to master accounts only and master accounts API Key must be linked to IP addresses.

#### Rate limit：1 request per second

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP request

`POST /api/v5/users/subaccount/modify-apikey`

> Request sample
    
    
    POST /api/v5/users/subaccount/modify-apikey
    body
    {
        "subAcct":"yongxu",
        "apiKey":"******"
        "ip":"1.1.1.1"
    }
    
    
    
    import okx.SubAccount as SubAccount
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading: 0, Demo trading: 1
    
    subAccountAPI = SubAccount.SubAccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # Reset the API Key of a sub-account
    result = subAccountAPI.reset_subaccount_apikey(
        subAcct="hahawang1",
        apiKey="",
        ip=""
    )
    print(result)
    

#### Request Parameters

Parameter name | Type | Required | Description  
---|---|---|---  
subAcct | String | Yes | Sub-account name  
apiKey | String | Yes | Sub-account APIKey  
label | String | No | Sub-account API Key label. The label will be reset if this is passed through.  
perm | String | No | Sub-account API Key permissions  
`read_only`: Read  
`trade`: Trade  
Separate with commas if more than one.   
The permission will be reset if this is passed through.  
ip | String | No | Sub-account API Key linked IP addresses, separate with commas if more than one. Support up to 20 IP addresses.  
The IP will be reset if this is passed through.  
If `ip` is set to "", then no IP addresses is linked to the APIKey.  
  
> Returned results
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
            "subAcct": "yongxu",
            "label": "v5",
            "apiKey": "******",
            "perm": "read,trade",
            "ip": "1.1.1.1",
            "ts": "1597026383085"
        }]
    }
    

#### Response parameters

**Parameter name** | **Type** | **Description**  
---|---|---  
subAcct | String | Sub-account name  
apiKey | String | Sub-accountAPI public key  
label | String | Sub-account API Key label  
perm | String | Sub-account API Key permissions  
`read_only`: Read  
`trade`: Trade  
ip | String | Sub-account API Key IP addresses that linked with API Key  
ts | String | Creation time  
  
### Delete the API Key of sub-accounts

Applies to master accounts only and master accounts API Key must be linked to IP addresses.

#### Rate limit：1 request per second

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP request

`POST /api/v5/users/subaccount/delete-apikey`

> Request sample
    
    
    POST /api/v5/users/subaccount/delete-apikey
    body
    {
        "subAcct":"test00001",
        "apiKey":"******"
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
subAcct | String | Yes | Sub-account name  
apiKey | String | Yes | API public key  
  
> Returned results
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
            "subAcct": "test00001"
        }]
    }
    

#### Response parameters

**Parameter name** | **Type** | **Description**  
---|---|---  
subAcct | String | Sub-account name  
  
### Get sub-account trading balance

Query detailed balance info of Trading Account of a sub-account via the master account (applies to master accounts only)

#### Rate limit：6 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP request

`GET /api/v5/account/subaccount/balances`

> Request sample
    
    
    GET /api/v5/account/subaccount/balances?subAcct=test1
    
    
    
    
    import okx.SubAccount as SubAccount
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading: 0, Demo trading: 1
    
    subAccountAPI = SubAccount.SubAccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # Get sub-account trading balance
    result = subAccountAPI.get_account_balance(
        subAcct="hahawang1"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
subAcct | String | Yes | Sub-account name  
  
> Returned result
    
    
    {
        "code": "0",
        "data": [
            {
                "adjEq": "101.46752000000001",
                "availEq": "624719833286",
                "borrowFroz": "0",
                "delta": "0",
                "deltaLever": "0",
                "deltaNeutralStatus": "0",
                "details": [
                    {
                        "autoLendStatus": "off",
                        "autoLendMtAmt": "0",
                        "accAvgPx": "",
                        "availBal": "101.5",
                        "availEq": "101.5",
                        "borrowFroz": "0",
                        "cashBal": "101.5",
                        "ccy": "USDT",
                        "clSpotInUseAmt": "",
                        "crossLiab": "0",
                        "colRes": "0",
                        "collateralEnabled": false,
                        "collateralRestrict": false,
                        "colBorrAutoConversion": "0",
                        "disEq": "101.46752000000001",
                        "eq": "101.5",
                        "eqUsd": "101.46752000000001",
                        "fixedBal": "0",
                        "frozenBal": "0",
                        "frpType": "0",
                        "imr": "",
                        "interest": "0",
                        "isoEq": "0",
                        "isoLiab": "0",
                        "isoUpl": "0",
                        "liab": "0",
                        "maxLoan": "1015.0000000000001",
                        "maxSpotInUse": "",
                        "mgnRatio": "",
                        "mmr": "",
                        "notionalLever": "",
                        "openAvgPx": "",
                        "ordFrozen": "0",
                        "rewardBal": "",
                        "smtSyncEq": "0",
                        "spotBal": "",
                        "spotCopyTradingEq": "0",
                        "spotInUseAmt": "",
                        "spotIsoBal": "0",
                        "spotUpl": "",
                        "spotUplRatio": "",
                        "stgyEq": "0",
                        "totalPnl": "",
                        "totalPnlRatio": "",
                        "twap": "0",
                        "uTime": "1663854334734",
                        "upl": "0",
                        "uplLiab": "0"
                    }
                ],
                "imr": "0",
                "isoEq": "0",
                "mgnRatio": "",
                "mmr": "0",
                "notionalUsd": "0",
                "notionalUsdForBorrow": "0",
                "notionalUsdForFutures": "0",
                "notionalUsdForOption": "0",
                "notionalUsdForSwap": "0",
                "ordFroz": "0",
                "totalEq": "101.46752000000001",
                "uTime": "1739332269934",
                "upl": "0"
            }
        ],
        "msg": ""
    }
    

#### Response parameters

**Parameters** | **Types** | **Description**  
---|---|---  
uTime | String | Update time of account information, millisecond format of Unix timestamp, e.g. `1597026383085`  
totalEq | String | The total amount of equity in `USD`  
isoEq | String | Isolated margin equity in `USD`  
Applicable to `Futures mode`/`Multi-currency margin`/`Portfolio margin`  
adjEq | String | Adjusted / Effective equity in `USD`   
The net fiat value of the assets in the account that can provide margins for spot, expiry futures, perpetual futures and options under the cross-margin mode.   
In multi-ccy or PM mode, the asset and margin requirement will all be converted to USD value to process the order check or liquidation.   
Due to the volatility of each currency market, our platform calculates the actual USD value of each currency based on discount rates to balance market risks.   
Applicable to `Spot mode`/`Multi-currency margin` and `Portfolio margin`  
availEq | String | Account level available equity, excluding currencies that are restricted due to the collateralized borrowing limit.  
Applicable to `Multi-currency margin`/`Portfolio margin`  
ordFroz | String | Cross margin frozen for pending orders in `USD`   
Only applicable to `Spot mode`/`Multi-currency margin`/`Portfolio margin`  
imr | String | Initial margin requirement in `USD`   
The sum of initial margins of all open positions and pending orders under cross-margin mode in `USD`.   
Applicable to `Spot mode`/`Multi-currency margin`/`Portfolio margin`  
mmr | String | Maintenance margin requirement in `USD`   
The sum of maintenance margins of all open positions and pending orders under cross-margin mode in `USD`.   
Applicable to `Spot mode`/`Multi-currency margin`/`Portfolio margin`  
borrowFroz | String | Potential borrowing IMR of the account in `USD`   
Only applicable to `Spot mode`/`Multi-currency margin`/`Portfolio margin`. It is "" for other margin modes.  
mgnRatio | String | Maintenance margin ratio in `USD`   
Applicable to `Spot mode`/`Multi-currency margin`/`Portfolio margin`  
notionalUsd | String | Notional value of positions in `USD`   
Applicable to `Spot mode`/`Multi-currency margin`/`Portfolio margin`  
notionalUsdForBorrow | String | Notional value for `Borrow` in USD  
Applicable to `Spot mode`/`Multi-currency margin`/`Portfolio margin`  
notionalUsdForSwap | String | Notional value of positions for `Perpetual Futures` in USD  
Applicable to `Multi-currency margin`/`Portfolio margin`  
notionalUsdForFutures | String | Notional value of positions for `Expiry Futures` in USD  
Applicable to `Multi-currency margin`/`Portfolio margin`  
notionalUsdForOption | String | Notional value of positions for `Option` in USD  
Applicable to `Spot mode`/`Multi-currency margin`/`Portfolio margin`  
upl | String | Cross-margin info of unrealized profit and loss at the account level in `USD`  
Applicable to `Multi-currency margin`/`Portfolio margin`  
delta | String | Delta (USD)  
deltaLever | String | Delta neutral strategy account level delta leverage  
deltaLever = delta / totalEq  
deltaNeutralStatus | String | Delta risk status  
`0`: normal  
`1`: transfer restricted  
`2`: delta reducing - cancel all pending orders if delta is greater than 5000 USD, only one delta reducing order allowed per index (spot, futures, swap)  
details | Array of objects | Detailed asset information in all currencies  
> ccy | String | Currency  
> eq | String | Equity of currency  
> cashBal | String | Cash balance  
> uTime | String | Update time of currency balance information, Unix timestamp format in milliseconds, e.g. `1597026383085`  
> isoEq | String | Isolated margin equity of currency  
Applicable to `Futures mode`/`Multi-currency margin`/`Portfolio margin`  
> availEq | String | Available equity of currency  
Applicable to `Futures mode`/`Multi-currency margin`/`Portfolio margin`  
> disEq | String | Discount equity of currency in `USD`.  
> fixedBal | String | Frozen balance for `Dip Sniper` and `Peak Sniper`  
> availBal | String | Available balance of currency  
> frozenBal | String | Frozen balance of currency  
> ordFrozen | String | Margin frozen for open orders   
Applicable to `Spot mode`/`Futures mode`/`Multi-currency margin`  
> liab | String | Liabilities of currency  
It is a positive value, e.g. `21625.64`  
Applicable to `Spot mode`/`Multi-currency margin`/`Portfolio margin`  
> upl | String | The sum of the unrealized profit & loss of all margin and derivatives positions of currency.   
Applicable to `Futures mode`/`Multi-currency margin`/`Portfolio margin`  
> uplLiab | String | Liabilities due to Unrealized loss of currency  
Applicable to `Multi-currency margin`/`Portfolio margin`  
> crossLiab | String | Cross liabilities of currency  
Applicable to `Spot mode`/`Multi-currency margin`/`Portfolio margin`  
> rewardBal | String | Trial fund balance  
> isoLiab | String | Isolated liabilities of currency  
Applicable to `Multi-currency margin`/`Portfolio margin`  
> mgnRatio | String | Cross Maintenance margin ratio of currency   
The index for measuring the risk of a certain asset in the account.   
Applicable to `Futures mode` and when there is cross position  
> imr | String | Cross initial margin requirement at the currency level  
Applicable to `Futures mode` and when there is cross position  
> mmr | String | Cross maintenance margin requirement at the currency level  
Applicable to `Futures mode` and when there is cross position  
> interest | String | Accrued interest of currency  
It is a positive value, e.g. `9.01`  
Applicable to `Spot mode`/`Multi-currency margin`/`Portfolio margin`  
> twap | String | Risk indicator of forced repayment  
Divided into multiple levels from 0 to 5, the larger the number, the more likely the forced repayment will be triggered.   
Applicable to `Spot mode`/`Multi-currency margin`/`Portfolio margin`  
> frpType | String | Forced repayment (FRP) type  
`0`: no FRP  
`1`: user based FRP  
`2`: platform based FRP  
  
Return `1`/`2` when twap is >= 1, applicable to `Spot mode`/`Multi-currency margin`/`Portfolio margin`  
> maxLoan | String | Max loan of currency  
Applicable to `cross` of `Spot mode`/`Multi-currency margin`/`Portfolio margin`  
> eqUsd | String | Equity in `USD` of currency  
> borrowFroz | String | Potential borrowing IMR of currency in `USD`   
Applicable to `Multi-currency margin`/`Portfolio margin`. It is "" for other margin modes.  
> notionalLever | String | Leverage of currency  
Applicable to `Futures mode`  
> stgyEq | String | Strategy equity  
> isoUpl | String | Isolated unrealized profit and loss of currency  
Applicable to `Futures mode`/`Multi-currency margin`/`Portfolio margin`  
> spotInUseAmt | String | Spot in use amount  
Applicable to `Portfolio margin`  
> clSpotInUseAmt | String | User-defined spot risk offset amount  
Applicable to `Portfolio margin`  
> maxSpotInUse | String | Max possible spot risk offset amount  
Applicable to `Portfolio margin`  
> spotIsoBal | String | Spot isolated balance  
Applicable to copy trading  
Applicable to `Spot mode`/`Futures mode`.  
> smtSyncEq | String | Smart sync equity  
The default is "0", only applicable to copy trader.  
> spotCopyTradingEq | String | Spot smart sync equity.   
The default is "0", only applicable to copy trader.  
> spotBal | String | Spot balance. The unit is currency, e.g. BTC. [More details](https://www.okx.com/help/i-introduction-of-spot)  
> openAvgPx | String | Spot average cost price. The unit is USD. [More details](https://www.okx.com/help/i-introduction-of-spot)  
> accAvgPx | String | Spot accumulated cost price. The unit is USD. [More details](https://www.okx.com/help/i-introduction-of-spot)  
> spotUpl | String | Spot unrealized profit and loss. The unit is USD. [More details](https://www.okx.com/help/i-introduction-of-spot)  
> spotUplRatio | String | Spot unrealized profit and loss ratio. [More details](https://www.okx.com/help/i-introduction-of-spot)  
> totalPnl | String | Spot accumulated profit and loss. The unit is USD. [More details](https://www.okx.com/help/i-introduction-of-spot)  
> totalPnlRatio | String | Spot accumulated profit and loss ratio. [More details](https://www.okx.com/help/i-introduction-of-spot)  
> colRes | String | Platform level collateral restriction status  
`0`: The restriction is not enabled.  
`1`: The restriction is not enabled. But the crypto is close to the platform's collateral limit.  
`2`: The restriction is enabled. This crypto can't be used as margin for your new orders. This may result in failed orders. But it will still be included in the account's adjusted equity and doesn't impact margin ratio.  
Refer to [Introduction to the platform collateralized borrowing limit](https://www.okx.com/help/introduction-to-the-platforms-collateralized-borrowing-limit-mechanism) for more details.  
> colBorrAutoConversion | String | Risk indicator of auto conversion. Divided into multiple levels from 1-5, the larger the number, the more likely the repayment will be triggered. The default will be 0, indicating there is no risk currently. 5 means this user is undergoing auto conversion now, 4 means this user will undergo auto conversion soon whereas 1/2/3 indicates there is a risk for auto conversion.  
Applicable to `Spot mode`/`Futures mode`/`Multi-currency margin`/`Portfolio margin`  
When the total liability for each crypto set as collateral exceeds a certain percentage of the platform's total limit, the auto-conversion mechanism may be triggered. This may result in the automatic sale of excess collateral crypto if you've set this crypto as collateral and have large borrowings. To lower this risk, consider reducing your use of the crypto as collateral or reducing your liabilities.  
Refer to [Introduction to the platform collateralized borrowing limit](https://www.okx.com/help/introduction-to-the-platforms-collateralized-borrowing-limit-mechanism) for more details.  
> collateralRestrict | Boolean | ~~Platform level collateralized borrow restriction  
`true`  
`false`~~(deprecated, use colRes instead)  
> collateralEnabled | Boolean | `true`: Collateral enabled  
`false`: Collateral disabled  
Applicable to `Multi-currency margin`  
> autoLendStatus | String | Auto lend status  
`unsupported`: auto lend is not supported by this currency  
`off`: auto lend is supported but turned off  
`pending`: auto lend is turned on but pending matching  
`active`: auto lend is turned on and matched  
> autoLendMtAmt | String | Auto lend currency matched amount  
Return "0" when autoLendStatus is `unsupported/off/pending`. Return matched amount when autoLendStatus is `active`  
"" will be returned for inapplicable fields with the current account level. 

### Get sub-account funding balance

Query detailed balance info of Funding Account of a sub-account via the master account (applies to master accounts only)

#### Rate limit：6 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP request

`GET /api/v5/asset/subaccount/balances`

> Request sample
    
    
    GET /api/v5/asset/subaccount/balances?subAcct=test1
    
    
    
    
    import okx.SubAccount as SubAccount
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading: 0, Demo trading: 1
    
    subAccountAPI = SubAccount.SubAccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # Get sub-account funding balance
    result = subAccountAPI.get_funding_balance(
        subAcct="hahawang1"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
subAcct | String | Yes | Sub-account name  
ccy | String | No | Single currency or multiple currencies (no more than 20) separated with comma, e.g. `BTC` or `BTC,ETH`.  
  
> Returned result
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
                "availBal": "37.11827078",
                "bal": "37.11827078",
                "ccy": "ETH",
                "frozenBal": "0"
            }
        ]
    }
    

#### Response parameters

Parameter | Type | Description  
---|---|---  
ccy | String | Currency  
bal | String | Balance  
frozenBal | String | Frozen balance  
availBal | String | Available balance  
  
### Get sub-account maximum withdrawals

Retrieve the maximum withdrawal information of a sub-account via the master account (applies to master accounts only). If no currency is specified, the transferable amount of all owned currencies will be returned.

#### Rate limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP request

`GET /api/v5/account/subaccount/max-withdrawal`

> Request Example
    
    
    GET /api/v5/account/subaccount/max-withdrawal?subAcct=test1
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
subAcct | String | Yes | Sub-account name  
ccy | String | No | Single currency or multiple currencies (no more than 20) separated with comma, e.g. `BTC` or `BTC,ETH`.  
  
> Response Example
    
    
    {
       "code":"0",
       "data":[
          {
             "ccy":"BTC",
             "maxWd":"3",
             "maxWdEx":"",
             "spotOffsetMaxWd":"3",
             "spotOffsetMaxWdEx":""
          },
          {
             "ccy":"ETH",
             "maxWd":"15",
             "maxWdEx":"",
             "spotOffsetMaxWd":"15",
             "spotOffsetMaxWdEx":""
          },
          {
             "ccy":"USDT",
             "maxWd":"10600",
             "maxWdEx":"",
             "spotOffsetMaxWd":"10600",
             "spotOffsetMaxWdEx":""
          }
       ],
       "msg":""
    }
    

#### Response parameters

Parameter | Type | Description  
---|---|---  
ccy | String | Currency  
maxWd | String | Max withdrawal (excluding borrowed assets under `Multi-currency margin`)  
maxWdEx | String | Max withdrawal (including borrowed assets under `Multi-currency margin`)  
spotOffsetMaxWd | String | Max withdrawal under Spot-Derivatives risk offset mode (excluding borrowed assets under `Portfolio margin`)   
Applicable to `Portfolio margin`  
spotOffsetMaxWdEx | String | Max withdrawal under Spot-Derivatives risk offset mode (including borrowed assets under `Portfolio margin`)   
Applicable to `Portfolio margin`  
  
### Get history of sub-account transfer

This endpoint is only available for master accounts. Transfer records are available from September 28, 2022 onwards.

#### Rate limit：6 requests per second

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP request

`GET /api/v5/asset/subaccount/bills`

> Request sample
    
    
    GET /api/v5/asset/subaccount/bills
    
    
    
    import okx.SubAccount as SubAccount
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading: 0, Demo trading: 1
    
    subAccountAPI = SubAccount.SubAccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # Get history of sub-account transfer
    result = subAccountAPI.bills()
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
ccy | String | No | Currency, such as BTC  
type | String | No | Transfer type  
`0`: Transfers from master account to sub-account  
`1` : Transfers from sub-account to master account.  
subAcct | String | No | Sub-account name  
after | String | No | Query the data prior to the requested bill ID creation time (exclude), the value should be a Unix timestamp in millisecond format. e.g. `1597026383085`  
before | String | No | Query the data after the requested bill ID creation time (exclude), the value should be a Unix timestamp in millisecond format. e.g. `1597026383085`  
limit | String | No | Number of results per request. The maximum is 100. The default is 100.  
  
> Returned results
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
          {
            "amt": "1.1",
            "billId": "89887685",
            "ccy": "USDT", 
            "subAcct": "hahatest1",
            "ts": "1712560959000",
            "type": "0"
          }
        ]
    }
    

#### Response parameters

**Parameter name** | **Type** | **Description**  
---|---|---  
billId | String | Bill ID  
ccy | String | Transfer currency  
amt | String | Transfer amount  
type | String | Bill type  
subAcct | String | Sub-account name  
ts | String | Bill ID creation time, Unix timestamp in millisecond format, e.g. `1597026383085`  
  
### Get history of managed sub-account transfer

Only applicable to the trading team's master account to getting transfer records of managed sub accounts entrusted to oneself.

#### Rate limit：6 requests per second

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP request

`GET /api/v5/asset/subaccount/managed-subaccount-bills`

> Request sample
    
    
    GET /api/v5/asset/subaccount/managed-subaccount-bills
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
ccy | String | No | Currency, e.g `BTC`  
type | String | No | Transfer type  
`0`: Transfers from master account to sub-account  
`1`: Transfers from sub-account to master account  
subAcct | String | No | Sub-account name  
subUid | String | No | Sub-account UID  
after | String | No | Query the data prior to the requested bill ID creation time (exclude), Unix timestamp in millisecond format, e.g. `1597026383085`  
before | String | No | Query the data after the requested bill ID creation time (exclude), Unix timestamp in millisecond format, e.g. `1597026383085`  
limit | String | No | Number of results per request. The maximum is 100. The default is 100.  
  
> Returned results
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
            "billId": "12344",
            "type": "1",
            "ccy": "BTC",
            "amt": "2",
            "subAcct": "test-1",
            "subUid": "xxxxxx",
            "ts": "1597026383085"
        }]
    }
    

#### Response parameters

**Parameter name** | **Type** | **Description**  
---|---|---  
billId | String | Bill ID  
ccy | String | Transfer currency  
amt | String | Transfer amount  
type | String | Bill type  
subAcct | String | Sub-account name  
subUid | String | Sub-account UID  
ts | String | Bill ID creation time, Unix timestamp in millisecond format, e.g. `1597026383085`  
  
### Master accounts manage the transfers between sub-accounts

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
  
### Set permission of transfer out

Set permission of transfer out for sub-account (only applicable to master account API key). Sub-account can transfer out to master account by default.

#### Rate Limit: 1 request per second

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/users/subaccount/set-transfer-out`

> Request Example
    
    
    POST /api/v5/users/subaccount/set-transfer-out
    body
    {
        "subAcct": "Test001,Test002",
        "canTransOut": true
    }
    
    
    
    import okx.SubAccount as SubAccount
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading: 0, Demo trading: 1
    
    subAccountAPI = SubAccount.SubAccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # Set permission of transfer out for sub-account
    result = subAccountAPI.set_permission_transfer_out(
        subAcct="hahawang1",
        canTransOut=False
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
subAcct | String | Yes | Name of the sub-account. Single sub-account or multiple sub-account (no more than 20) separated with comma.  
canTransOut | Boolean | No | Whether the sub-account has the right to transfer out. The default is `true`.  
`false`: cannot transfer out   
`true`: can transfer out  
  
> Returned result
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "subAcct": "Test001",
                "canTransOut": true
            },
            {
                "subAcct": "Test002",
                "canTransOut": true
            }
        ]
    }
    
    

#### Response parameters

**Parameter** | **Type** | **Description**  
---|---|---  
subAcct | String | Name of the sub-account  
canTransOut | Boolean | Whether the sub-account has the right to transfer out.   
`false`: cannot transfer out   
`true`: can transfer out  
  
### Get custody trading sub-account list

The trading team uses this interface to view the list of sub-accounts currently under escrow

#### Rate limit：1 request per second

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP request

`GET /api/v5/users/entrust-subaccount-list`

> Request sample
    
    
    GET /api/v5/users/entrust-subaccount-list
    
    
    
    
    import okx.SubAccount as SubAccount
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading: 0, Demo trading: 1
    
    subAccountAPI = SubAccount.SubAccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # Get custody trading sub-account list
    result = subAccountAPI.get_entrust_subaccount_list()
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
subAcct | String | No | Sub-account name  
  
> Returned results
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
           {
              "subAcct":"test-1"
           },
           {
              "subAcct":"test-2"
           }
        ]
    }
    

#### Response parameters

**Parameter name** | **Type** | **Description**  
---|---|---  
subAcct | String | Sub-account name

---

# REST API

### 查看子账户列表   
  
仅适用于母账户

#### 限速：20次/2s

#### 限速规则：User ID

#### 权限：读取

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
  
### 创建子账户 

仅适用于母账户，且母账户APIKey必须绑定IP。

#### 限速：1次/s

#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/users/subaccount/create-subaccount`

> 请求示例
    
    
    POST /api/v5/users/subaccount/create-subaccount
    body
    {
        "subAcct": "subAccount002",
        "type": "1",
        "label": "123456"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
subAcct | String | 是 | 子账户名称，支持6-20位字母和数字组合（区分大小写，不支持空格符号）  
type | String | 是 | 子账户类型   
`1`：普通子账户   
`5`：托管交易子账户 - Copper  
`12`：托管交易子账户 - Komainu  
label | String | 是 | API Key的备注，支持6-32位字母（区分大小写），数字，或者特殊字符如: *  
pwd | String | 可选 | 子账户登录密码，仅 KYB 账户必填  
您的密码必须满足以下条件：  
长度为 8 ~ 32 个字符。  
1 个小写字母 (a-z)   
1 个大写字母 (A-Z)   
1 个数字   
1 个符号，如：！@ # $ %  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "label": "123456",
                "subAcct": "subAccount002",
                "ts": "1744875304520",
                "uid": "698827017768230914"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
subAcct | String | 子账户名称  
label | String | 子账户的备注  
uid | String | 子账户 ID  
ts | String | 创建时间  
  
### 创建子账户的API Key 

仅适用于母账户，且母账户APIKey必须绑定IP。

#### 限速：1次/s

#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/users/subaccount/apikey`

> 请求示例
    
    
    POST /api/v5/users/subaccount/apikey
    body
    {
        "subAcct":"panpanBroker2",
        "label":"broker3",
        "passphrase": "******",
        "perm":"trade"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
subAcct | String | 是 | 子账户名称，支持6-20位字母和数字组合（区分大小写，不支持空格符号）  
label | String | 是 | API Key的备注  
passphrase | String | 是 | API Key密码，8-32位字母数字组合，至少包含一个数字、一个大写字母、一个小写字母、一个特殊字符  
perm | String | 否 | API Key权限  
`read_only`：读取  
`trade`：交易  
ip | String | 否 | 绑定ip地址，多个ip用半角逗号隔开，最多支持20个ip  
**安全性考虑，推荐绑定IP**   
**未绑定IP且拥有交易或提币权限的API key，将在闲置14天之后自动删除。(模拟盘的API key不会被删除)**  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
            "subAcct": "test-1",
            "label": "v5",
            "apiKey": "******",
            "secretKey": "******",
            "passphrase": "******",
            "perm": "read_only,trade",
            "ip": "1.1.1.1,2.2.2.2",
            "ts": "1597026383085"
        }]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
subAcct | String | 子账户名称  
label | String | APIKey的备注  
apiKey | String | API公钥  
secretKey | String | API的私钥  
passphrase | String | APIKey的密码  
perm | String | APIKey权限  
ip | String | APIKey绑定的ip地址  
ts | String | 创建时间  
  
### 查询子账户的API Key 

仅适用于母账户 

#### 限速：20次/2秒

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/users/subaccount/apikey`

> 请求示例
    
    
    GET /api/v5/users/subaccount/apikey?subAcct=panpanBroker2
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
subAcct | String | 是 | 子账户名称  
apiKey | String | 否 | API的公钥  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "label":"v5",
                "apiKey":"arg13sdfgs",
                "perm":"read_only,trade",
                "ip":"1.1.1.1,2.2.2.2",
                "ts":"1597026383085"
            },
            {
                "label":"v5.1",
                "apiKey":"arg13sdfgs",
                "perm":"read_only",
                "ip":"1.1.1.1,2.2.2.2",
                "ts":"1597026383085"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
label | String | API Key的备注  
apiKey | String | API Key公钥  
perm | String | API Key权限  
read_only：读取  
trade ：交易  
ip | String | API Key绑定的ip地址  
ts | String | 创建时间  
  
### 重置子账户的APIKey 

仅适用于母账户，且母账户APIKey必须绑定IP。

#### 限速：1次/s

#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/users/subaccount/modify-apikey`

> 请求示例
    
    
    POST /api/v5/users/subaccount/modify-apikey
    body
    {
        "subAcct":"yongxu",
        "apiKey":"******"
        "ip":"1.1.1.1"
    }
    
    
    
    import okx.SubAccount as SubAccount
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘：1
    
    subAccountAPI = SubAccount.SubAccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # 重置子账户的APIKey
    result = subAccountAPI.reset_subaccount_apikey(
        subAcct="hahawang1",
        apiKey="",
        ip=""
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
subAcct | String | 是 | 子账户名称  
apiKey | String | 是 | 子账户API的公钥  
label | String | 否 | 子账户APIKey的备注，如果填写该字段，则该字段会被重置  
perm | String | 否 | 子账户APIKey权限  
`read_only`：读取  
`trade`：交易  
多个权限用半角逗号隔开。  
如果填写该字段，则该字段会被重置。  
ip | String | 否 | 子账户APIKey绑定ip地址，多个ip用半角逗号隔开，最多支持20个ip。  
如果填写该字段，那该字段会被重置。  
如果ip传""，则表示解除IP绑定。  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
            "subAcct": "yongxu",
            "label": "v5",
            "apiKey": "******",
            "perm": "read,trade",
            "ip": "1.1.1.1",
            "ts": "1597026383085"
        }]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
subAcct | String | 子账户名称  
label | String | APIKey的备注  
apiKey | String | API公钥  
perm | String | APIKey权限  
ip | String | APIKey绑定的ip地址  
ts | String | 创建时间  
  
### 删除子账户的API Key 

仅适用于母账户，且母账户APIKey必须绑定IP。

#### 限速：1次/s

#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/users/subaccount/delete-apikey`

> 请求示例
    
    
    POST /api/v5/users/subaccount/delete-apikey
    body
    {
        "subAcct":"test00001",
        "apiKey":"******"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
subAcct | String | 是 | 子账户名称  
apiKey | String | 是 | API的公钥  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
            "subAcct": "test00001"
        }]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
subAcct | String | 子账户名称  
  
### 获取子账户交易账户余额 

获取子账户交易账户余额（适用于母账户）

#### 限速：6次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/account/subaccount/balances`

> 请求示例
    
    
    GET /api/v5/account/subaccount/balances?subAcct=test1
    
    
    
    
    import okx.SubAccount as SubAccount
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘：1
    
    subAccountAPI = SubAccount.SubAccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # 获取子账户交易账户余额
    result = subAccountAPI.get_account_balance(
        subAcct="hahawang1"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
subAcct | String | 是 | 子账户名称  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "adjEq": "101.46752000000001",
                "availEq": "",
                "borrowFroz": "0",
                "delta": "0",
                "deltaLever": "0",
                "deltaNeutralStatus": "0",
                "details": [
                    {
                        "autoLendStatus": "off",
                        "autoLendMtAmt": "0",
                        "accAvgPx": "",
                        "availBal": "101.5",
                        "availEq": "101.5",
                        "borrowFroz": "0",
                        "cashBal": "101.5",
                        "ccy": "USDT",
                        "clSpotInUseAmt": "",
                        "crossLiab": "0",
                        "colRes": "0",
                        "collateralEnabled": false,
                        "collateralRestrict": false,
                        "colBorrAutoConversion": "0",
                        "disEq": "101.46752000000001",
                        "eq": "101.5",
                        "eqUsd": "101.46752000000001",
                        "fixedBal": "0",
                        "frozenBal": "0",
                        "frpType": "0",
                        "imr": "",
                        "interest": "0",
                        "isoEq": "0",
                        "isoLiab": "0",
                        "isoUpl": "0",
                        "liab": "0",
                        "maxLoan": "1015.0000000000001",
                        "maxSpotInUse": "",
                        "mgnRatio": "",
                        "mmr": "",
                        "notionalLever": "",
                        "openAvgPx": "",
                        "ordFrozen": "0",
                        "rewardBal": "",
                        "smtSyncEq": "0",
                        "spotBal": "",
                        "spotCopyTradingEq": "0",
                        "spotInUseAmt": "",
                        "spotIsoBal": "0",
                        "spotUpl": "",
                        "spotUplRatio": "",
                        "stgyEq": "0",
                        "totalPnl": "",
                        "totalPnlRatio": "",
                        "twap": "0",
                        "uTime": "1663854334734",
                        "upl": "0",
                        "uplLiab": "0"
                    }
                ],
                "imr": "0",
                "isoEq": "0",
                "mgnRatio": "",
                "mmr": "0",
                "notionalUsd": "0",
                "notionalUsdForBorrow": "0",
                "notionalUsdForFutures": "0",
                "notionalUsdForOption": "0",
                "notionalUsdForSwap": "0",
                "ordFroz": "0",
                "totalEq": "101.46752000000001",
                "uTime": "1739332269934",
                "upl": "0"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
uTime | String | 账户信息的更新时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
totalEq | String | 美金层面权益  
isoEq | String | 美金层面逐仓仓位权益  
适用于`合约模式`/`跨币种保证金模式`/`组合保证金模式`  
adjEq | String | 美金层面有效保证金  
适用于`现货模式`/`跨币种保证金模式`/`组合保证金模式`  
availEq | String | 账户美金层面可用保证金，排除因总质押借币上限而被限制的币种  
适用于`跨币种保证金模式/组合保证金模式`  
ordFroz | String | 美金层面全仓挂单占用保证金  
仅适用于`现货模式`/`跨币种保证金模式`/`组合保证金模式`  
imr | String | 美金层面占用保证金  
适用于`现货模式`/`跨币种保证金模式`/`组合保证金模式`  
mmr | String | 美金层面维持保证金  
适用于`现货模式`/`跨币种保证金模式`/`组合保证金模式`  
borrowFroz | String | 账户美金层面潜在借币占用保证金  
仅适用于`现货模式`/`跨币种保证金模式`/`组合保证金模式`。在其他账户模式下为""。  
mgnRatio | String | 美金层面维持保证金率  
适用于`现货模式`/`跨币种保证金模式`/`组合保证金模式`  
notionalUsd | String | 以美金价值为单位的持仓数量，即仓位美金价值  
适用于`现货模式`/`跨币种保证金模式`/`组合保证金模式`  
notionalUsdForBorrow | String | 借币金额（美元价值）  
适用于`现货模式`/`跨币种保证金模式`/`组合保证金模式`  
notionalUsdForSwap | String | 永续合约持仓美元价值  
适用于`跨币种保证金模式`/`组合保证金模式`  
notionalUsdForFutures | String | 交割合约持仓美元价值  
适用于`跨币种保证金模式`/`组合保证金模式`  
notionalUsdForOption | String | 期权持仓美元价值  
适用于`现货模式`/`跨币种保证金模式`/`组合保证金模式`  
upl | String | 账户层面全仓未实现盈亏（美元单位）  
适用于`跨币种保证金模式`/`组合保证金模式`  
delta | String | Delta (USD)  
deltaLever | String | Delta权益比率  
deltaLever = delta/totalEq  
deltaNeutralStatus | String | Delta 风险状态  
`0`: 普通  
`1`: 限制划转  
`2`: 仅支持降低 Delta - 相同基础货币的现货、交割和永续合约视为同一标的资产。同一标的资产内，仅能新下一笔降低 Delta 值的订单，且下单时不应存在其他挂单。如果触发此限制，且您的账户 Delta 大于 500,000 USD，您的所有限价、市价、高级限价单挂单将被撤销。  
details | Array of objects | 各币种资产详细信息  
> ccy | String | 币种  
> eq | String | 币种总权益  
> cashBal | String | 币种余额  
> uTime | String | 币种余额信息的更新时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
> isoEq | String | 币种逐仓仓位权益  
适用于`合约模式`/`跨币种保证金模式`/`组合保证金模式`  
> availEq | String | 可用保证金  
适用于`合约模式`/`跨币种保证金模式`/`组合保证金模式`  
> disEq | String | 美金层面币种折算权益  
> fixedBal | String | 抄底宝、逃顶宝功能的币种冻结金额  
> availBal | String | 可用余额  
> frozenBal | String | 币种占用金额  
> ordFrozen | String | 挂单冻结数量   
适用于`现货模式`/`合约模式`/`跨币种保证金模式`  
> liab | String | 币种负债额  
值为正数，如 "21625.64"  
适用于`现货模式`/`跨币种保证金模式`/`组合保证金模式`  
> upl | String | 未实现盈亏  
适用于`合约模式`/`跨币种保证金模式`/`组合保证金模式`  
> uplLiab | String | 由于仓位未实现亏损导致的负债  
适用于`跨币种保证金模式`/`组合保证金模式`  
> crossLiab | String | 币种全仓负债额  
适用于`现货模式`/`跨币种保证金模式`/`组合保证金模式`  
> isoLiab | String | 币种逐仓负债额  
适用于`跨币种保证金模式`/`组合保证金模式`  
> rewardBal | String | 体验金余额  
> mgnRatio | String | 币种全仓维持保证金率，衡量账户内某项资产风险的指标  
适用于`合约模式`且有全仓仓位时  
> imr | String | 币种维度全仓占用保证金  
适用于`合约模式`且有全仓仓位时  
> mmr | String | 币种维度全仓维持保证金  
适用于`合约模式`且有全仓仓位时  
> interest | String | 计息，应扣未扣利息  
值为正数，如 `9.01`  
适用于`现货模式`/`跨币种保证金模式`/`组合保证金模式`  
> twap | String | 当前负债币种触发自动换币的风险  
0、1、2、3、4、5其中之一，数字越大代表您的负债币种触发自动换币概率越高  
适用于`现货模式`/`跨币种保证金模式`/`组合保证金模式`  
> frpType | String | 自动换币类型  
`0`：未发生自动换币  
`1`：基于用户的自动换币  
`2`：基于平台借币限额的自动换币  
  
当twap>=1时返回1或2代表自动换币风险类型，适用于`现货模式`/`跨币种保证金模式`/`组合保证金模式`  
> maxLoan | String | 币种最大可借  
适用于`现货模式`/`跨币种保证金模式`/`组合保证金模式` 的全仓  
> eqUsd | String | 币种权益美金价值  
> borrowFroz | String | 币种美金层面潜在借币占用保证金  
仅适用于`现货模式`/`跨币种保证金模式`/`组合保证金模式`。在其他账户模式下为""。  
> notionalLever | String | 币种杠杆倍数  
适用于`合约模式`  
> stgyEq | String | 策略权益  
> isoUpl | String | 逐仓未实现盈亏  
适用于`合约模式`/`跨币种保证金模式`/`组合保证金模式`  
> spotInUseAmt | String | 现货对冲占用数量  
适用于`组合保证金模式`  
> clSpotInUseAmt | String | 用户自定义现货占用数量  
适用于`组合保证金模式`  
> maxSpotInUse | String | 系统计算得到的最大可能现货占用数量  
适用于`组合保证金模式`  
> spotIsoBal | String | 现货逐仓余额  
仅适用于现货带单/跟单  
适用于`现货模式`/`合约模式`  
> smtSyncEq | String | 合约智能跟单权益  
默认为0，仅适用于跟单人。  
> spotCopyTradingEq | String | 现货智能跟单权益  
默认为0，仅适用于跟单人。  
> spotBal | String | 现货余额 ，单位为 币种，比如 BTC。[详情](https://www.okx.com/zh-hans/help/i-introduction-of-spot)  
> openAvgPx | String | 现货开仓成本价 单位 USD。 [详情](https://www.okx.com/zh-hans/help/i-introduction-of-spot)  
> accAvgPx | String | 现货累计成本价 单位 USD。 [详情](https://www.okx.com/zh-hans/help/i-introduction-of-spot)  
> spotUpl | String | 现货未实现收益，单位 USD。 [详情](https://www.okx.com/zh-hans/help/i-introduction-of-spot)  
> spotUplRatio | String | 现货未实现收益率。[详情](https://www.okx.com/zh-hans/help/i-introduction-of-spot)  
> totalPnl | String | 现货累计收益，单位 USD。 [详情](https://www.okx.com/zh-hans/help/i-introduction-of-spot)  
> totalPnlRatio | String | 现货累计收益率。[详情](https://www.okx.com/zh-hans/help/i-introduction-of-spot)  
> colRes | String | 平台维度质押限制状态  
`0`：限制未触发  
`1`：限制未触发，但该币种接近平台质押上限  
`2`：限制已触发。该币种不可用作新订单的保证金，这可能会导致下单失败。但它仍会被计入账户有效保证金，保证金率不会收到影响。  
更多详情，请参阅[平台总质押借币上限说明](https://www.okx.com/zh-hans/help/introduction-to-the-platforms-collateralized-borrowing-limit-mechanism)。  
> colBorrAutoConversion | String | 基于平台质押借币限额的自动换币风险指标。分为1-5多个等级，数字越大，触发自动换币的可能性越大。默认值为0，表示当前无风险。5表示该用户正在进行自动换币，4代表该用户即将被进行自动换币，1/2/3表示存在自动换币风险。  
适用于`现货模式`/`合约模式`/`跨币种保证金模式`/`组合保证金模式`  
当某币种的全平台质押借币量超出平台总上限一定比例时，对于质押该币种且借币量较大的用户，平台将通过自动换币降低质押借币风险。请减少该币种的质押数量或偿还负债，以降低风险。  
更多详情，请参阅[平台总质押借币上限说明](https://www.okx.com/zh-hans/help/introduction-to-the-platforms-collateralized-borrowing-limit-mechanism)。  
> collateralRestrict | Boolean | ~~平台维度的质押借币限制  
`true`  
`false`~~（已弃用，请使用colRes）  
> collateralEnabled | Boolean | `true`：质押币  
`false`：非质押币  
适用于`跨币种保证金模式  
> colBorrAutoConversion | String | 表示当某个币种的抵押借贷达到平台限制且用户交易账户持有该币种时，强制还款的指标  
分为5档，从1到5，数字越小代表强制还款强度越弱。默认为0，表示当前无强制还款风险；5代表用户当前正经历强制还款。  
适用于`现货模式`/`合约模式`/`跨币种保证金模式`/`组合保证金模式`  
> autoLendStatus | String | 自动借出状态  
`unsupported`：该币种不支持自动借出  
`off`：自动借出功能关闭  
`pending`：自动借出功能开启但未匹配  
`active`：自动借出功能开启且已匹配  
> autoLendMtAmt | String | 自动借出已匹配量  
当 autoLendStatus 为 `unsupported/off/pending` 时返回 0  
当 autoLendStatus 为 `active` 时返回已匹配量  
当前账户等级下无效字段返回"" 

### 获取子账户资金账户余额 

获取子账户资金账户余额（适用于母账户）

#### 限速：6次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/asset/subaccount/balances`

> 请求示例
    
    
    GET /api/v5/asset/subaccount/balances?subAcct=test1
    
    
    
    
    import okx.SubAccount as SubAccount
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘：1
    
    subAccountAPI = SubAccount.SubAccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # 获取子账户资金账户余额
    result = subAccountAPI.get_funding_balance(
        subAcct="hahawang1"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
subAcct | String | 是 | 子账户名称  
ccy | String | 否 | 币种，如 `BTC`  
支持多币种查询（不超过20个），币种之间半角逗号分隔  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
                "availBal": "37.11827078",
                "bal": "37.11827078",
                "ccy": "ETH",
                "frozenBal": "0"
            }
        ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ccy | String | 币种，如 `BTC`  
bal | String | 余额  
frozenBal | String | 冻结余额（不可用）  
availBal | String | 可用余额  
  
### 获取子账户最大可转余额 

获取子账户最大可转余额（适用于母账户）。不指定币种会返回所有拥有的币种资产可划转数量。

#### 限速：20次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/account/subaccount/max-withdrawal`

> 请求示例
    
    
    GET /api/v5/account/subaccount/max-withdrawal?subAcct=test1
    
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
subAcct | String | 是 | 子账户名称  
ccy | String | 否 | 币种，如 `BTC`   
支持多币种查询（不超过20个），币种之间半角逗号分隔  
  
> 返回结果
    
    
    {
       "code":"0",
       "data":[
          {
             "ccy":"BTC",
             "maxWd":"3",
             "maxWdEx":"",
             "spotOffsetMaxWd":"3",
             "spotOffsetMaxWdEx":""
          },
          {
             "ccy":"ETH",
             "maxWd":"15",
             "maxWdEx":"",
             "spotOffsetMaxWd":"15",
             "spotOffsetMaxWdEx":""
          },
          {
             "ccy":"USDT",
             "maxWd":"10600",
             "maxWdEx":"",
             "spotOffsetMaxWd":"10600",
             "spotOffsetMaxWdEx":""
          }
       ],
       "msg":""
    }
    

#### Response Parameters

参数名 | 类型 | 描述  
---|---|---  
ccy | String | 币种  
maxWd | String | 最大可划转数量（不包含`跨币种保证金模式`借币金额）  
maxWdEx | String | 最大可划转数量（包含`跨币种保证金模式`借币金额）  
spotOffsetMaxWd | String | 现货对冲不支持借币最大可转数量   
仅适用于`组合保证金模式`  
spotOffsetMaxWdEx | String | 现货对冲支持借币的最大可转数量   
仅适用于`组合保证金模式`  
  
### 查询子账户转账记录 

仅适用于母账户。转账记录可追溯至2022年9月28日。

#### 限速：6次/s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/asset/subaccount/bills`

> 请求示例
    
    
    GET /api/v5/asset/subaccount/bills
    
    
    
    import okx.SubAccount as SubAccount
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘：1
    
    subAccountAPI = SubAccount.SubAccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # 查询子账户转账记录
    result = subAccountAPI.bills()
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 否 | 币种，如 BTC  
type | String | 否 | 划转类型  
`0`：母账户转子账户  
`1`：子账户转母账户  
subAcct | String | 否 | 子账户名称  
after | String | 否 | 查询在billId创建时间之前(不包含)的内容，值为时间戳，Unix时间戳的毫秒数格式，如 `1597026383085`  
before | String | 否 | 查询在billId创建时间之后(不包含)的内容，值为时间戳，Unix时间戳的毫秒数格式，如 `1597026383085`  
limit | String | 否 | 分页返回的结果集数量，最大为100，不填默认返回100条  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
          {
            "amt": "1.1",
            "billId": "89887685",
            "ccy": "USDT",
            "subAcct": "hahatest1",
            "ts": "1712560959000",
            "type": "0"
          }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
billId | String | 账单ID  
ccy | String | 划转币种  
amt | String | 划转金额  
type | String | 账单类型  
subAcct | String | 子账户名称  
ts | String | 账单ID创建时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
  
### 查询托管子账户转账记录 

仅适用于交易团队母账户查看托管给自己的托管子账户转账记录

#### 限速：6次/s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/asset/subaccount/managed-subaccount-bills`

> 请求示例
    
    
    GET /api/v5/asset/subaccount/managed-subaccount-bills
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 否 | 币种，如 `BTC`  
type | String | 否 | 划转类型  
`0`：母账户转子账户  
`1`：子账户转母账户  
subAcct | String | 否 | 子账户名称  
subUid | String | 否 | 子账户UID  
after | String | 否 | 查询在billId创建时间之前(不包含)的内容，值为时间戳，Unix时间戳的毫秒数格式，如 `1597026383085`  
before | String | 否 | 查询在billId创建时间之后(不包含)的内容，值为时间戳，Unix时间戳的毫秒数格式，如 `1597026383085`  
limit | String | 否 | 分页返回的结果集数量，最大为100，默认返回100条  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
            "billId": "12344",
            "type": "1",
            "ccy": "BTC",
            "amt": "2",
            "subAcct": "test-1",
            "subUid": "xxxxxx",
            "ts": "1597026383085"
        }]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
billId | String | 账单ID  
ccy | String | 划转币种  
amt | String | 划转金额  
type | String | 账单类型  
subAcct | String | 子账户名称  
subUid | String | 子账户UID  
ts | String | 账单ID创建时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
  
### 子账户间资金划转 

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
  
### 设置子账户主动转出权限 

设置子账户转出权限（仅适用于母账户），默认可转出至母账户。

#### 限速：1次/s

#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/users/subaccount/set-transfer-out`

> 请求示例
    
    
    POST /api/v5/users/subaccount/set-transfer-out
    body
    {
        "subAcct": "Test001,Test002",
        "canTransOut": true
    }
    
    
    
    import okx.SubAccount as SubAccount
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘：1
    
    subAccountAPI = SubAccount.SubAccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # 设置子账户主动转出权限
    result = subAccountAPI.set_permission_transfer_out(
        subAcct="hahawang1",
        canTransOut=False
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
subAcct | String | 是 | 子账户名称，支持设置多个（不超过20个），子账户名称之间半角逗号分隔  
canTransOut | Boolean | 否 | 是否可以主动转出，默认为`true`  
`false`：不可转出  
`true`：可以转出  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "subAcct": "Test001",
                "canTransOut": true
            },
            {
                "subAcct": "Test002",
                "canTransOut": true
            }
        ]
    }
    
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
subAcct | String | 子账户名称  
canTransOut | Boolean | 是否可以主动转出   
`false`：不可转出  
`true`：可以转出  
  
### 查看被托管的子账户列表 

交易团队使用该接口查看当前托管中的子账户列表

#### 限速：1次/s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/users/entrust-subaccount-list`

> 请求示例
    
    
    GET /api/v5/users/entrust-subaccount-list
    
    
    
    
    import okx.SubAccount as SubAccount
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘：1
    
    subAccountAPI = SubAccount.SubAccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # 查看被托管的子账户列表
    result = subAccountAPI.get_entrust_subaccount_list()
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
subAcct | String | 否 | 子账户名称  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
           {
              "subAcct":"test-1"
           },
           {
              "subAcct":"test-2"
           }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
subAcct | String | 子账户名称