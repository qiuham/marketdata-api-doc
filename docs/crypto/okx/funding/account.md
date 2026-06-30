---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#funding-account
anchor_id: funding-account
api_type: API
updated_at: 2026-06-30 19:56:05.197028
---

# Funding Account

The API endpoints of `Funding Account` require authentication.

## REST API

### Get currencies

Retrieve a list of all currencies available which are related to the current account's KYC entity.

#### Rate Limit: 6 requests per second

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/asset/currencies`

> Request Example
    
    
    GET /api/v5/asset/currencies
    
    
    
    
    import okx.Funding as Funding
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading: 0, Demo trading: 1
    
    fundingAPI = Funding.FundingAPI(apikey, secretkey, passphrase, False, flag)
    
    # Get currencies
    result = fundingAPI.get_currencies()
    print(result)
    

#### Request Parameters

**Parameters** | **Types** | **Required** | **Description**  
---|---|---|---  
ccy | String | No | Single currency or multiple currencies separated with comma, e.g. `BTC` or `BTC,ETH`.  
  
> Response Example
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
        {
            "burningFeeRate": "",
            "canDep": true,
            "canInternal": true,
            "canWd": true,
            "ccy": "BTC",
            "chain": "BTC-Bitcoin",
            "ctAddr": "",
            "depEstOpenTime": "",
            "depQuotaFixed": "",
            "depQuoteDailyLayer2": "",
            "fee": "0.00005",
            "logoLink": "https://static.coinall.ltd/cdn/oksupport/asset/currency/icon/btc20230419112752.png",
            "mainNet": true,
            "maxFee": "0.00005",
            "maxFeeForCtAddr": "",
            "maxWd": "500",
            "minDep": "0.0005",
            "minDepArrivalConfirm": "1",
            "minFee": "0.00005",
            "minFeeForCtAddr": "",
            "minInternal": "0.0001",
            "minWd": "0.0005",
            "minWdUnlockConfirm": "2",
            "name": "Bitcoin",
            "needTag": false,
            "usedDepQuotaFixed": "",
            "usedWdQuota": "0",
            "wdEstOpenTime": "",
            "wdQuota": "10000000",
            "wdTickSz": "8"
        }
      ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ccy | String | Currency, e.g. `BTC`  
name | String | Name of currency. There is no related name when it is not shown.  
logoLink | String | The logo link of currency  
chain | String | Chain name, e.g. `USDT-ERC20`, `USDT-TRC20`  
ctAddr | String | Contract address  
canDep | Boolean | The availability to deposit from chain   
`false`: not available   
`true`: available  
canWd | Boolean | The availability to withdraw to chain   
`false`: not available   
`true`: available  
canInternal | Boolean | The availability to internal transfer   
`false`: not available   
`true`: available  
depEstOpenTime | String | Estimated opening time for deposit, Unix timestamp format in milliseconds, e.g. `1597026383085`  
if `canDep` is `true`, it returns `""`  
wdEstOpenTime | String | Estimated opening time for withdraw, Unix timestamp format in milliseconds, e.g. `1597026383085`  
if `canWd` is `true`, it returns `""`  
minDep | String | The minimum deposit amount of currency in a single transaction  
minWd | String | The minimum `on-chain withdrawal` amount of currency in a single transaction  
minInternal | String | The minimum `internal transfer` amount of currency in a single transaction  
No maximum `internal transfer` limit in a single transaction, subject to the withdrawal limit in the past 24 hours(`wdQuota`).  
maxWd | String | The maximum amount of currency `on-chain withdrawal` in a single transaction  
wdTickSz | String | The withdrawal precision, indicating the number of digits after the decimal point.  
The withdrawal fee precision kept the same as withdrawal precision.  
The accuracy of internal transfer withdrawal is 8 decimal places.  
wdQuota | String | The withdrawal limit in the past 24 hours (including `on-chain withdrawal` and `internal transfer`), unit in `USD`  
usedWdQuota | String | The amount of currency withdrawal used in the past 24 hours, unit in `USD`  
fee | String | The fixed withdrawal fee  
Apply to `on-chain withdrawal`  
minFee | String | ~~The minimum withdrawal fee for normal address  
Apply to `on-chain withdrawal`~~  
(Deprecated)  
maxFee | String | ~~The maximum withdrawal fee for normal address  
Apply to `on-chain withdrawal`~~  
(Deprecated)  
minFeeForCtAddr | String | ~~The minimum withdrawal fee for contract address  
Apply to `on-chain withdrawal`~~  
(Deprecated)  
maxFeeForCtAddr | String | ~~The maximum withdrawal fee for contract address  
Apply to `on-chain withdrawal`~~  
(Deprecated)  
burningFeeRate | String | Burning fee rate, e.g "0.05" represents "5%".  
Some currencies may charge combustion fees. The burning fee is deducted based on the withdrawal quantity (excluding gas fee) multiplied by the burning fee rate.  
Apply to `on-chain withdrawal`  
mainNet | Boolean | If current chain is main net, then it will return `true`, otherwise it will return `false`  
needTag | Boolean | Whether tag/memo information is required for withdrawal, e.g. `EOS` will return `true`  
minDepArrivalConfirm | String | The minimum number of blockchain confirmations to acknowledge fund deposit. The account is credited after that, but the deposit can not be withdrawn  
minWdUnlockConfirm | String | The minimum number of blockchain confirmations required for withdrawal of a deposit  
depQuotaFixed | String | The fixed deposit limit, unit in `USD`  
Return empty string if there is no deposit limit  
usedDepQuotaFixed | String | The used amount of fixed deposit quota, unit in `USD`  
Return empty string if there is no deposit limit  
depQuoteDailyLayer2 | String | The layer2 network daily deposit limit  
  
### Get balance

Retrieve the funding account balances of all the assets and the amount that is available or on hold.

Only asset information of a currency with a balance greater than 0 will be returned. 

#### Rate Limit: 6 requests per second

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/asset/balances`

> Request Example
    
    
    GET /api/v5/asset/balances
    
    
    
    
    import okx.Funding as Funding
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading: 0, Demo trading: 1
    
    fundingAPI = Funding.FundingAPI(apikey, secretkey, passphrase, False, flag)
    
    # Get balane
    result = fundingAPI.get_balances()
    print(result)
    

#### Request Parameters

**Parameters** | **Types** | **Required** | **Description**  
---|---|---|---  
ccy | String | No | Single currency or multiple currencies (no more than 20) separated with comma, e.g. `BTC` or `BTC,ETH`.  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "availBal": "37.11827078",
                "bal": "37.11827078",
                "ccy": "ETH",
                "frozenBal": "0"
            }
        ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ccy | String | Currency  
bal | String | Balance  
frozenBal | String | Frozen balance  
availBal | String | Available balance  
  
### Get non-tradable assets

Retrieve the funding account balances of all the assets and the amount that is available or on hold.

#### Rate Limit: 6 requests per second

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/asset/non-tradable-assets`

> Request Example
    
    
    GET /api/v5/asset/non-tradable-assets
    
    
    
    
    import okx.Funding as Funding
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading: 0, Demo trading: 1
    
    fundingAPI = Funding.FundingAPI(apikey, secretkey, passphrase, False, flag)
    
    result = fundingAPI.get_non_tradable_assets()
    print(result)
    

#### Request Parameters

**Parameters** | **Types** | **Required** | **Description**  
---|---|---|---  
ccy | String | No | Single currency or multiple currencies (no more than 20) separated with comma, e.g. `BTC` or `BTC,ETH`.  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "bal": "989.84719571",
                "burningFeeRate": "",
                "canWd": true,
                "ccy": "CELT",
                "chain": "CELT-OKTC",
                "ctAddr": "f403fb",
                "fee": "2",
                "feeCcy": "USDT",
                "logoLink": "https://static.coinall.ltd/cdn/assets/imgs/221/460DA8A592400393.png",
                "minWd": "0.1",
                "name": "",
                "needTag": false,
                "wdAll": false,
                "wdTickSz": "8"
            },
            {
                "bal": "0.001",
                "burningFeeRate": "",
                "canWd": true,
                "ccy": "MEME",
                "chain": "MEME-ERC20",
                "ctAddr": "09b760",
                "fee": "5",
                "feeCcy": "USDT",
                "logoLink": "https://static.coinall.ltd/cdn/assets/imgs/207/2E664E470103C613.png",
                "minWd": "0.001",
                "name": "MEME Inu",
                "needTag": false,
                "wdAll": false,
                "wdTickSz": "8"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ccy | String | Currency, e.g. `CELT`  
name | String | Chinese name of currency. There is no related name when it is not shown.  
logoLink | String | Logo link of currency  
bal | String | Withdrawable balance  
canWd | Boolean | Availability to withdraw to chain.   
`false`: not available `true`: available  
chain | String | Chain for withdrawal  
minWd | String | Minimum withdrawal amount of currency in a single transaction  
wdAll | Boolean | Whether all assets in this currency must be withdrawn at one time  
fee | String | Fixed withdrawal fee  
feeCcy | String | Fixed withdrawal fee unit, e.g. `USDT`  
burningFeeRate | String | Burning fee rate, e.g "0.05" represents "5%".  
Some currencies may charge combustion fees. The burning fee is deducted based on the withdrawal quantity (excluding gas fee) multiplied by the burning fee rate.  
ctAddr | String | Last 6 digits of contract address  
wdTickSz | String | Withdrawal precision, indicating the number of digits after the decimal point  
needTag | Boolean | Whether tag/memo information is required for withdrawal  
  
### Get account asset valuation

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
  
### Funds transfer

Only API keys with `Trade` privilege can call this endpoint.

This endpoint supports the transfer of funds between your funding account and trading account, and from the master account to sub-accounts.

Sub-account can transfer out to master account by default. Need to call [Set permission of transfer out](/docs-v5/en/#sub-account-rest-api-set-permission-of-transfer-out) to grant privilege first if you want sub-account transferring to another sub-account (sub-accounts need to belong to same master account.)

The success or failure of the request does not necessarily reflect the actual transfer result. Recommend checking the transfer status by calling "Get funds transfer state" to confirm the final result. 

#### Rate Limit: 2 requests per second

#### Rate limit rule: User ID + Currency

#### Permission: Trade

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
  
### Get funds transfer state

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
  
### Asset bills details

Query the billing record in the past month.

#### Rate Limit: 6 Requests per second

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/asset/bills`

> Request Example
    
    
    GET /api/v5/asset/bills
    
    
    
    
    import okx.Funding as Funding
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading: 0, Demo trading: 1
    
    fundingAPI = Funding.FundingAPI(apikey, secretkey, passphrase, False, flag)
    
    # Get asset bills details
    result = fundingAPI.get_bills()
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
ccy | String | No | Currency  
type | String | No | Bill type  
`1`: Deposit  
`2`: Withdrawal  
`13`: Canceled withdrawal  
`20`: Transfer to sub account (for master account)  
`21`: Transfer from sub account (for master account)  
`22`: Transfer out from sub to master account (for sub-account)  
`23`: Transfer in from master to sub account (for sub-account)  
`28`: Manually claimed Airdrop  
`47`: System reversal  
`48`: Event Reward  
`49`: Event Giveaway  
`68`: Fee rebate (by rebate card)  
`72`: Token received  
`73`: Token given away  
`74`: Token refunded  
`75`: [Simple earn flexible] Subscription  
`76`: [Simple earn flexible] Redemption  
`77`: Jumpstart distribute  
`78`: Jumpstart lock up  
`80`: DEFI/Staking subscription  
`82`: DEFI/Staking redemption  
`83`: Staking yield  
`84`: Violation fee  
`89`: Deposit yield  
`116`: [Fiat] Place an order  
`117`: [Fiat] Fulfill an order  
`118`: [Fiat] Cancel an order  
`124`: Jumpstart unlocking  
`130`: Transferred from Trading account  
`131`: Transferred to Trading account  
`132`: [P2P] Frozen by customer service  
`133`: [P2P] Unfrozen by customer service  
`134`: [P2P] Transferred by customer service  
`135`: Cross chain exchange  
`137`: [ETH Staking] Subscription  
`138`: [ETH Staking] Swapping  
`139`: [ETH Staking] Earnings  
`146`: Customer feedback  
`150`: Affiliate commission  
`151`: Referral reward  
`152`: Broker reward  
`160`: Dual Investment subscribe  
`161`: Dual Investment collection  
`162`: Dual Investment profit  
`163`: Dual Investment refund  
`172`: [Affiliate] Sub-affiliate commission  
`173`: [Affiliate] Fee rebate (by trading fee)  
`174`: Jumpstart Pay  
`175`: Locked collateral  
`176`: Loan  
`177`: Added collateral  
`178`: Returned collateral  
`179`: Repayment  
`180`: Unlocked collateral  
`181`: Airdrop payment  
`185`: [Broker] Convert reward  
`187`: [Broker] Convert transfer  
`189`: Mystery box bonus  
`195`: Untradable asset withdrawal  
`196`: Untradable asset withdrawal revoked  
`197`: Untradable asset deposit  
`198`: Untradable asset collection reduce  
`199`: Untradable asset collection increase  
`200`: Buy  
`202`: Price Lock Subscribe  
`203`: Price Lock Collection  
`204`: Price Lock Profit  
`205`: Price Lock Refund  
`207`: Dual Investment Lite Subscribe  
`208`: Dual Investment Lite Collection  
`209`: Dual Investment Lite Profit  
`210`: Dual Investment Lite Refund  
`212`: [Flexible loan] Multi-collateral loan collateral locked  
`215`: [Flexible loan] Multi-collateral loan collateral released  
`217`: [Flexible loan] Multi-collateral loan borrowed  
`218`: [Flexible loan] Multi-collateral loan repaid  
`232`: [Flexible loan] Subsidized interest received  
`220`: Delisted crypto  
`221`: Blockchain's withdrawal fee  
`222`: Withdrawal fee refund  
`223`: SWAP lead trading profit share  
`225`: Shark Fin subscribe  
`226`: Shark Fin collection  
`227`: Shark Fin profit  
`228`: Shark Fin refund  
`229`: Airdrop  
`232`: Subsidized interest received  
`233`: Broker rebate compensation  
`240`: Snowball subscribe  
`241`: Snowball refund  
`242`: Snowball profit  
`243`: Snowball trading failed  
`249`: Seagull subscribe  
`250`: Seagull collection  
`251`: Seagull profit  
`252`: Seagull refund  
`263`: Strategy bots profit share  
`265`: Signal revenue  
`266`: SPOT lead trading profit share  
`270`: DCD broker transfer  
`271`: DCD broker rebate  
`272`: [Convert] Buy Crypto/Fiat  
`273`: [Convert] Sell Crypto/Fiat  
`284`: [Custody] Transfer out trading sub-account  
`285`: [Custody] Transfer in trading sub-account  
`286`: [Custody] Transfer out custody funding account  
`287`: [Custody] Transfer in custody funding account  
`288`: [Custody] Fund delegation   
`289`: [Custody] Fund undelegation  
`299`: Affiliate recommendation commission  
`300`: Fee discount rebate  
`303`: Snowball market maker transfer  
~~`304`: [Simple Earn Fixed] Order submission~~  
~~`305`: [Simple Earn Fixed] Order redemption~~  
~~`306`: [Simple Earn Fixed] Principal distribution~~  
~~`307`: [Simple Earn Fixed] Interest distribution (early termination compensation)~~  
~~`308`: [Simple Earn Fixed] Interest distribution~~  
~~`309`: [Simple Earn Fixed] Interest distribution (extension compensation) ~~  
`311`: Crypto dust auto-transfer in  
`313`: Sent by gift  
`314`: Received from gift  
`315`: Refunded from gift  
`328`: [SOL staking] Send Liquidity Staking Token reward  
`329`: [SOL staking] Subscribe Liquidity Staking Token staking  
`330`: [SOL staking] Mint Liquidity Staking Token  
`331`: [SOL staking] Redeem Liquidity Staking Token order  
`332`: [SOL staking] Settle Liquidity Staking Token order  
`333`: Trial fund reward  
`339`: [Simple Earn Fixed] Order submission  
`340`: [Simple Earn Fixed] Order failure refund  
`341`: [Simple Earn Fixed] Redemption  
`342`: [Simple Earn Fixed] Principal  
`343`: [Simple Earn Fixed] Interest  
`344`: [Simple Earn Fixed] Compensatory interest  
`345`: [Institutional Loan] Principal repayment  
`346`: [Institutional Loan] Interest repayment  
`347`: [Institutional Loan] Overdue penalty  
`348`: [BTC staking] Subscription  
`349`: [BTC staking] Redemption  
`350`: [BTC staking] Earnings  
`351`: [Institutional Loan] Loan disbursement  
`354`: Copy and bot rewards  
`361`: Deposit from closed sub-account  
`372`: Asset segregation  
`373`: Asset release  
`400`: Auto lend interest   
`408`: Auto earn USDG interest  
`476`: Transferred out to Cloud Exchange  
`477`: Transferred in from Cloud Exchange  
thirdPartyType | String | No | Third-party custody type. If not specified, defaults to `1` (for backward compatibility).  
`1`: Copper  
`2`: Komainu  
`5`: SCB  
When a master account is bound to multiple custody providers, use this parameter to filter bills by the specified custody provider. Applicable to bill types `284`–`289`.  
clientId | String | No | Client-supplied ID for transfer or withdrawal  
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
after | String | No | Pagination of data to return records earlier than the requested `ts`, Unix timestamp format in milliseconds, e.g. `1597026383085`  
before | String | No | Pagination of data to return records newer than the requested `ts`, Unix timestamp format in milliseconds, e.g. `1597026383085`  
limit | String | No | Number of results per request. The maximum is `100`. The default is `100`.  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
            "billId": "12344",
            "ccy": "BTC",
            "clientId": "",
            "balChg": "2",
            "bal": "12",
            "type": "1",
            "ts": "1597026383085",
            "notes": ""
        }]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
billId | String | Bill ID  
ccy | String | Account balance currency  
clientId | String | Client-supplied ID for transfer or withdrawal  
balChg | String | Change in balance at the account level  
bal | String | Balance at the account level  
type | String | Bill type  
notes | String | Notes  
ts | String | Creation time, Unix timestamp format in milliseconds, e.g.`1597026383085`  
  
### Asset bills history

Query the billing records of all time since 1 February, 2021. 

⚠️ **IMPORTANT** : Data updates occur every 30 seconds. Update frequency may vary based on data volume - please be aware of potential delays during high-traffic periods. 

#### Rate Limit: 1 Requests per second

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/asset/bills-history`

> Request Example
    
    
    GET /api/v5/asset/bills-history
    
    
    
    
    import okx.Funding as Funding
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading: 0, Demo trading: 1
    
    fundingAPI = Funding.FundingAPI(apikey, secretkey, passphrase, False, flag)
    
    # Get asset bills details
    result = fundingAPI.get_bills_history()
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
ccy | String | No | Currency  
type | String | No | Bill type  
`1`: Deposit  
`2`: Withdrawal  
`13`: Canceled withdrawal  
`20`: Transfer to sub account (for master account)  
`21`: Transfer from sub account (for master account)  
`22`: Transfer out from sub to master account (for sub-account)  
`23`: Transfer in from master to sub account (for sub-account)  
`28`: Manually claimed Airdrop  
`47`: System reversal  
`48`: Event Reward  
`49`: Event Giveaway  
`68`: Fee rebate (by rebate card)  
`72`: Token received  
`73`: Token given away  
`74`: Token refunded  
`75`: [Simple earn flexible] Subscription  
`76`: [Simple earn flexible] Redemption  
`77`: Jumpstart distribute  
`78`: Jumpstart lock up  
`80`: DEFI/Staking subscription  
`82`: DEFI/Staking redemption  
`83`: Staking yield  
`84`: Violation fee  
`89`: Deposit yield  
`116`: [Fiat] Place an order  
`117`: [Fiat] Fulfill an order  
`118`: [Fiat] Cancel an order  
`124`: Jumpstart unlocking  
`130`: Transferred from Trading account  
`131`: Transferred to Trading account  
`132`: [P2P] Frozen by customer service  
`133`: [P2P] Unfrozen by customer service  
`134`: [P2P] Transferred by customer service  
`135`: Cross chain exchange  
`137`: [ETH Staking] Subscription  
`138`: [ETH Staking] Swapping  
`139`: [ETH Staking] Earnings  
`146`: Customer feedback  
`150`: Affiliate commission  
`151`: Referral reward  
`152`: Broker reward  
`160`: Dual Investment subscribe  
`161`: Dual Investment collection  
`162`: Dual Investment profit  
`163`: Dual Investment refund  
`172`: [Affiliate] Sub-affiliate commission  
`173`: [Affiliate] Fee rebate (by trading fee)  
`174`: Jumpstart Pay  
`175`: Locked collateral  
`176`: Loan  
`177`: Added collateral  
`178`: Returned collateral  
`179`: Repayment  
`180`: Unlocked collateral  
`181`: Airdrop payment  
`185`: [Broker] Convert reward  
`187`: [Broker] Convert transfer  
`189`: Mystery box bonus  
`195`: Untradable asset withdrawal  
`196`: Untradable asset withdrawal revoked  
`197`: Untradable asset deposit  
`198`: Untradable asset collection reduce  
`199`: Untradable asset collection increase  
`200`: Buy  
`202`: Price Lock Subscribe  
`203`: Price Lock Collection  
`204`: Price Lock Profit  
`205`: Price Lock Refund  
`207`: Dual Investment Lite Subscribe  
`208`: Dual Investment Lite Collection  
`209`: Dual Investment Lite Profit  
`210`: Dual Investment Lite Refund  
`212`: [Flexible loan] Multi-collateral loan collateral locked  
`215`: [Flexible loan] Multi-collateral loan collateral released  
`217`: [Flexible loan] Multi-collateral loan borrowed  
`218`: [Flexible loan] Multi-collateral loan repaid  
`232`: [Flexible loan] Subsidized interest received  
`220`: Delisted crypto  
`221`: Blockchain's withdrawal fee  
`222`: Withdrawal fee refund  
`223`: SWAP lead trading profit share  
`225`: Shark Fin subscribe  
`226`: Shark Fin collection  
`227`: Shark Fin profit  
`228`: Shark Fin refund  
`229`: Airdrop  
`232`: Subsidized interest received  
`233`: Broker rebate compensation  
`240`: Snowball subscribe  
`241`: Snowball refund  
`242`: Snowball profit  
`243`: Snowball trading failed  
`249`: Seagull subscribe  
`250`: Seagull collection  
`251`: Seagull profit  
`252`: Seagull refund  
`263`: Strategy bots profit share  
`265`: Signal revenue  
`266`: SPOT lead trading profit share  
`270`: DCD broker transfer  
`271`: DCD broker rebate  
`272`: [Convert] Buy Crypto/Fiat  
`273`: [Convert] Sell Crypto/Fiat  
`284`: [Custody] Transfer out trading sub-account  
`285`: [Custody] Transfer in trading sub-account  
`286`: [Custody] Transfer out custody funding account  
`287`: [Custody] Transfer in custody funding account  
`288`: [Custody] Fund delegation   
`289`: [Custody] Fund undelegation  
`299`: Affiliate recommendation commission  
`300`: Fee discount rebate  
`303`: Snowball market maker transfer  
~~`304`: [Simple Earn Fixed] Order submission~~  
~~`305`: [Simple Earn Fixed] Order redemption~~  
~~`306`: [Simple Earn Fixed] Principal distribution~~  
~~`307`: [Simple Earn Fixed] Interest distribution (early termination compensation)~~  
~~`308`: [Simple Earn Fixed] Interest distribution~~  
~~`309`: [Simple Earn Fixed] Interest distribution (extension compensation) ~~  
`311`: Crypto dust auto-transfer in  
`313`: Sent by gift  
`314`: Received from gift  
`315`: Refunded from gift  
`328`: [SOL staking] Send Liquidity Staking Token reward  
`329`: [SOL staking] Subscribe Liquidity Staking Token staking  
`330`: [SOL staking] Mint Liquidity Staking Token  
`331`: [SOL staking] Redeem Liquidity Staking Token order  
`332`: [SOL staking] Settle Liquidity Staking Token order  
`333`: Trial fund reward  
`339`: [Simple Earn Fixed] Order submission  
`340`: [Simple Earn Fixed] Order failure refund  
`341`: [Simple Earn Fixed] Redemption  
`342`: [Simple Earn Fixed] Principal  
`343`: [Simple Earn Fixed] Interest  
`344`: [Simple Earn Fixed] Compensatory interest  
`345`: [Institutional Loan] Principal repayment  
`346`: [Institutional Loan] Interest repayment  
`347`: [Institutional Loan] Overdue penalty  
`348`: [BTC staking] Subscription  
`349`: [BTC staking] Redemption  
`350`: [BTC staking] Earnings  
`351`: [Institutional Loan] Loan disbursement  
`354`: Copy and bot rewards  
`361`: Deposit from closed sub-account  
`372`: Asset segregation  
`373`: Asset release  
`400`: auto lend interest  
`408`: Auto earn interest (USDG earn)  
`476`: Transferred out to Cloud Exchange  
`477`: Transferred in from Cloud Exchange  
thirdPartyType | String | No | Third-party custody type. If not specified, defaults to `1` (for backward compatibility).  
`1`: Copper  
`2`: Komainu  
`5`: SCB  
When a master account is bound to multiple custody providers, use this parameter to filter bills by the specified custody provider. Applicable to bill types `284`–`289`.  
clientId | String | No | Client-supplied ID for transfer or withdrawal  
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
after | String | No | Pagination of data to return records earlier than the requested `ts` or `billId`, Unix timestamp format in milliseconds, e.g. `1597026383085`  
before | String | No | Pagination of data to return records newer than the requested `ts`, Unix timestamp format in milliseconds, e.g. `1597026383085`  
limit | String | No | Number of results per request. The maximum is `100`. The default is `100`.  
pagingType | String | No | PagingType  
`1`: Timestamp of the bill record  
`2`: Bill ID of the bill record  
The default is `1`  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
            "billId": "12344",
            "ccy": "BTC",
            "clientId": "",
            "balChg": "2",
            "bal": "12",
            "type": "1",
            "ts": "1597026383085",
            "notes": ""
        }]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
billId | String | Bill ID  
ccy | String | Account balance currency  
clientId | String | Client-supplied ID for transfer or withdrawal  
balChg | String | Change in balance at the account level  
bal | String | Balance at the account level  
type | String | Bill type  
notes | String | Notes  
ts | String | Creation time, Unix timestamp format in milliseconds, e.g.`1597026383085`  
  
### Get deposit address

Retrieve the deposit addresses of currencies, including previously-used addresses.

#### Rate Limit: 6 requests per second

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/asset/deposit-address`

> Request Example
    
    
    GET /api/v5/asset/deposit-address?ccy=BTC
    
    
    
    
    import okx.Funding as Funding
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading: 0, Demo trading: 1
    
    fundingAPI = Funding.FundingAPI(apikey, secretkey, passphrase, False, flag)
    
    # Get deposit address
    result = fundingAPI.get_deposit_address(
        ccy="USDT"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
ccy | String | Yes | Currency, e.g. `BTC`  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "chain": "BTC-Bitcoin",
                "ctAddr": "",
                "ccy": "BTC",
                "to": "6",
                "addr": "39XNxK1Ryqgg3Bsyn6HzoqV4Xji25pNkv6",
                "verifiedName":"John Corner",
                "selected": true
            },
            {
                "chain": "BTC-OKC",
                "ctAddr": "",
                "ccy": "BTC",
                "to": "6",
                "addr": "0x66d0edc2e63b6b992381ee668fbcb01f20ae0428",
                "verifiedName":"John Corner",
                "selected": true
            },
            {
                "chain": "BTC-ERC20",
                "ctAddr": "5807cf",
                "ccy": "BTC",
                "to": "6",
                "addr": "0x66d0edc2e63b6b992381ee668fbcb01f20ae0428",
                "verifiedName":"John Corner",
                "selected": true
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
addr | String | Deposit address  
tag | String | Deposit tag (This will not be returned if the currency does not require a tag for deposit)  
memo | String | Deposit memo (This will not be returned if the currency does not require a memo for deposit)  
pmtId | String | Deposit payment ID (This will not be returned if the currency does not require a payment_id for deposit)  
addrEx | Object | Deposit address attachment (This will not be returned if the currency does not require this)  
e.g. `TONCOIN` attached tag name is `comment`, the return will be `{'comment':'123456'}`  
ccy | String | Currency, e.g. `BTC`  
chain | String | Chain name, e.g. `USDT-ERC20`, `USDT-TRC20`  
to | String | The beneficiary account  
`6`: Funding account `18`: Trading account  
The users under some entity (e.g. Brazil) only support deposit to trading account.  
verifiedName | String | Verified name (for recipient)  
selected | Boolean | Return `true` if the current deposit address is selected by the website page  
ctAddr | String | Last 6 digits of contract address  
  
### Get deposit history

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

### Withdrawal

Only supported withdrawal of assets from funding account. Common sub-account does not support withdrawal. 

The API can only make withdrawal to verified addresses/account, and verified addresses can be set by WEB/APP.  About tag  
Some token deposits require a deposit address and a tag (e.g. Memo/Payment ID), which is a string that guarantees the uniqueness of your deposit address. Follow the deposit procedure carefully, or you may risk losing your assets.  
For currencies with labels, if it is a withdrawal between OKX users, please use internal transfer instead of online withdrawal  The following content only applies to users residing in the United Arab Emirates  
Due to local laws and regulations in your country or region, a certain ratio of user assets must be stored in cold wallets. We will perform cold-to-hot wallet asset transfers from time to time. However, if assets in hot wallets are not sufficient to meet user withdrawal demands, an extra step is needed to transfer cold wallet assets to the hot wallet. This may cause delays of up to 24 hours to receive withdrawals.  
Learn more (https://www.okx.com/help/what-is-a-segregated-wallet-and-why-is-my-withdrawal-delayed)  Users under certain entities need to provide additional information for withdrawal  
Bahamas entity users refer to https://www.okx.com/docs-v5/log_en/#2024-08-08-withdrawal-api-adjustment-for-bahama-entity-users 

#### Rate Limit: 6 requests per second

#### Rate limit rule: User ID

#### Permission: Withdraw

#### HTTP Request

`POST /api/v5/asset/withdrawal`

> Request Example
    
    
    # on-chain withdrawal
    POST /api/v5/asset/withdrawal
    body
    {
        "amt":"1",
        "dest":"4",
        "ccy":"BTC",
        "chain":"BTC-Bitcoin",
        "toAddr":"17DKe3kkkkiiiiTvAKKi2vMPbm1Bz3CMKw"
    }
    
    # internal withdrawal 
    POST /api/v5/asset/withdrawal
    body
    {
        "amt":"10",
        "dest":"3",
        "ccy":"USDT",
        "areaCode":"86",
        "toAddr":"15651000000"
    }
    
    # Specific entity users need to provide receiver's info
    POST /api/v5/asset/withdrawal
    body
    {
        "amt":"1",
        "dest":"4",
        "ccy":"BTC",
        "chain":"BTC-Bitcoin",
        "toAddr":"17DKe3kkkkiiiiTvAKKi2vMPbm1Bz3CMKw",
        "rcvrInfo":{
            "walletType":"exchange",
            "exchId":"did:ethr:0xfeb4f99829a9acdf52979abee87e83addf22a7e1",
            "rcvrFirstName":"Bruce",
            "rcvrLastName":"Wayne"
        }
    }
    
    
    
    import okx.Funding as Funding
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading: 0, Demo trading: 1
    
    fundingAPI = Funding.FundingAPI(apikey, secretkey, passphrase, False, flag)
    
    # Withdrawal
    result = fundingAPI.withdrawal(
        ccy="USDT",
        toAddr="TXtvfb7cdrn6VX9H49mgio8bUxZ3DGfvYF",
        amt="100",
        dest="4",
        chain="USDT-TRC20"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
ccy | String | Yes | Currency, e.g. `USDT`  
amt | String | Yes | Withdrawal amount  
Withdrawal fee is not included in withdrawal amount. Please reserve sufficient transaction fees when withdrawing.  
You can get fee amount by [Get currencies](/docs-v5/en/#funding-account-rest-api-get-currencies).  
For `internal transfer`, transaction fee is always `0`.  
dest | String | Yes | Withdrawal method  
`3`: internal transfer  
`4`: on-chain withdrawal  
toAddr | String | Yes | `toAddr` should be a trusted address/account.   
If your `dest` is `4`, some crypto currency addresses are formatted as `'address:tag'`, e.g. `'ARDOR-7JF3-8F2E-QUWZ-CAN7F:123456'`  
If your `dest` is `3`,`toAddr` should be a recipient address which can be UID, email, phone or login account name (account name is only for sub-account).  
toAddrType | String | No | Address type  
`1`: wallet address, email, phone, or login account name  
`2`: UID (applicable only when dest=`3`)  
chain | String | Conditional | Chain name  
There are multiple chains under some currencies, such as `USDT` has `USDT-ERC20`, `USDT-TRC20`  
If the parameter is not filled in, the default will be the main chain.  
When you withdrawal the non-tradable asset, if the parameter is not filled in, the default will be the unique withdrawal chain.  
Apply to `on-chain withdrawal`.  
You can get supported chain name by the endpoint of [Get currencies](/docs-v5/en/#funding-account-rest-api-get-currencies).  
areaCode | String | Conditional | Area code for the phone number, e.g. `86`  
If `toAddr` is a phone number, this parameter is required.  
Apply to `internal transfer`  
rcvrInfo | Object | Conditional | Recipient information  
For the specific entity users to do on-chain withdrawal/lightning withdrawal, this information is required.  
> walletType | String | Yes | Wallet Type  
`exchange`: Withdraw to exchange wallet  
`private`: Withdraw to private wallet  
For the wallet belongs to business recipient, `rcvrFirstName` may input the company name, `rcvrLastName` may input "N/A", location info may input the registered address of the company.  
> exchId | String | Conditional | Exchange ID  
You can query supported exchanges through the endpoint of [Get exchange list (public)](/docs-v5/en/#funding-account-rest-api-get-exchange-list-public)  
If the exchange is not in the exchange list, fill in '0' in this field.   
Apply to walletType = `exchange`  
> rcvrFirstName | String | Conditional | Receiver's first name, e.g. `Bruce`  
> rcvrLastName | String | Conditional | Receiver's last name, e.g. `Wayne`  
> rcvrCountry | String | Conditional | The recipient's country, e.g. `United States`  
You must enter an English country name or a two letter country code (ISO 3166-1). Please refer to the `Country Name` and `Country Code` in the country information table below.  
> rcvrCountrySubDivision | String | Conditional | State/Province of the recipient, e.g. `California`  
> rcvrTownName | String | Conditional | The town/city where the recipient is located, e.g. `San Jose`  
> rcvrStreetName | String | Conditional | Recipient's street address, e.g. `Clementi Avenue 1`  
clientId | String | No | Client-supplied ID  
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
            "amt": "0.1",
            "wdId": "67485",
            "ccy": "BTC",
            "clientId": "",
            "chain": "BTC-Bitcoin"
        }]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ccy | String | Currency  
chain | String | Chain name, e.g. `USDT-ERC20`, `USDT-TRC20`  
amt | String | Withdrawal amount  
wdId | String | Withdrawal ID  
clientId | String | Client-supplied ID  
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
  
#### Country information

Country name | Country code  
---|---  
Afghanistan | AF  
Albania | AL  
Algeria | DZ  
Andorra | AD  
Angola | AO  
Anguilla | AI  
Antigua and Barbuda | AG  
Argentina | AR  
Armenia | AM  
Australia | AU  
Austria | AT  
Azerbaijan | AZ  
Bahamas | BS  
Bahrain | BH  
Bangladesh | BD  
Barbados | BB  
Belarus | BY  
Belgium | BE  
Belize | BZ  
Benin | BJ  
Bermuda | BM  
Bhutan | BT  
Bolivia | BO  
Bosnia and Herzegovina | BA  
Botswana | BW  
Brazil | BR  
British Virgin Islands | VG  
Brunei | BN  
Bulgaria | BG  
Burkina Faso | BF  
Burundi | BI  
Cambodia | KH  
Cameroon | CM  
Canada | CA  
Cape Verde | CV  
Cayman Islands | KY  
Central African Republic | CF  
Chad | TD  
Chile | CL  
Colombia | CO  
Comoros | KM  
Congo (Republic) | CG  
Congo (Democratic Republic) | CD  
Costa Rica | CR  
Cote d´Ivoire (Ivory Coast) | CI  
Croatia | HR  
Cuba | CU  
Cyprus | CY  
Czech Republic | CZ  
Denmark | DK  
Djibouti | DJ  
Dominica | DM  
Dominican Republic | DO  
Ecuador | EC  
Egypt | EG  
El Salvador | SV  
Equatorial Guinea | GQ  
Eritrea | ER  
Estonia | EE  
Ethiopia | ET  
Fiji | FJ  
Finland | FI  
France | FR  
Gabon | GA  
Gambia | GM  
Georgia | GE  
Germany | DE  
Ghana | GH  
Greece | GR  
Grenada | GD  
Guatemala | GT  
Guinea | GN  
Guinea-Bissau | GW  
Guyana | GY  
Haiti | HT  
Honduras | HN  
Hong Kong | HK  
Hungary | HU  
Iceland | IS  
India | IN  
Indonesia | ID  
Iran | IR  
Iraq | IQ  
Ireland | IE  
Israel | IL  
Italy | IT  
Jamaica | JM  
Japan | JP  
Jordan | JO  
Kazakhstan | KZ  
Kenya | KE  
Kiribati | KI  
North Korea | KP  
South Korea | KR  
Kuwait | KW  
Kyrgyzstan | KG  
Laos | LA  
Latvia | LV  
Lebanon | LB  
Lesotho | LS  
Liberia | LR  
Libya | LY  
Liechtenstein | LI  
Lithuania | LT  
Luxembourg | LU  
Macau | MO  
Macedonia | MK  
Madagascar | MG  
Malawi | MW  
Malaysia | MY  
Maldives | MV  
Mali | ML  
Malta | MT  
Marshall Islands | MH  
Mauritania | MR  
Mauritius | MU  
Mexico | MX  
Micronesia | FM  
Moldova | MD  
Monaco | MC  
Mongolia | MN  
Montenegro | ME  
Morocco | MA  
Mozambique | MZ  
Myanmar (Burma) | MM  
Namibia | NA  
Nauru | NR  
Nepal | NP  
Netherlands | NL  
New Zealand | NZ  
Nicaragua | NI  
Niger | NE  
Nigeria | NG  
Norway | NO  
Oman | OM  
Pakistan | PK  
Palau | PW  
Panama | PA  
Papua New Guinea | PG  
Paraguay | PY  
Peru | PE  
Philippines | PH  
Poland | PL  
Portugal | PT  
Qatar | QA  
Romania | RO  
Russia | RU  
Rwanda | RW  
Saint Kitts and Nevis | KN  
Saint Lucia | LC  
Saint Vincent and the Grenadines | VC  
Samoa | WS  
San Marino | SM  
Sao Tome and Principe | ST  
Saudi Arabia | SA  
Senegal | SN  
Serbia | RS  
Seychelles | SC  
Sierra Leone | SL  
Singapore | SG  
Slovakia | SK  
Slovenia | SI  
Solomon Islands | SB  
Somalia | SO  
South Africa | ZA  
Spain | ES  
Sri Lanka | LK  
Sudan | SD  
Suriname | SR  
Swaziland | SZ  
Sweden | SE  
Switzerland | CH  
Syria | SY  
Taiwan | TW  
Tajikistan | TJ  
Tanzania | TZ  
Thailand | TH  
Timor-Leste (East Timor) | TL  
Togo | TG  
Tonga | TO  
Trinidad and Tobago | TT  
Tunisia | TN  
Turkey | TR  
Turkmenistan | TM  
Tuvalu | TV  
U.S. Virgin Islands | VI  
Uganda | UG  
Ukraine | UA  
United Arab Emirates | AE  
United Kingdom | GB  
United States | US  
Uruguay | UY  
Uzbekistan | UZ  
Vanuatu | VU  
Vatican City | VA  
Venezuela | VE  
Vietnam | VN  
Yemen | YE  
Zambia | ZM  
Zimbabwe | ZW  
Kosovo | XK  
South Sudan | SS  
China | CN  
Palestine | PS  
Curacao | CW  
Dominican Republic | DO  
Dominican Republic | DO  
Gibraltar | GI  
New Caledonia | NC  
Cook Islands | CK  
Reunion | RE  
Guernsey | GG  
Guadeloupe | GP  
Martinique | MQ  
French Polynesia | PF  
Faroe Islands | FO  
Greenland | GL  
Jersey | JE  
Aruba | AW  
Puerto Rico | PR  
Isle of Man | IM  
Guam | GU  
Sint Maarten | SX  
Turks and Caicos | TC  
Åland Islands | AX  
Caribbean Netherlands | BQ  
British Indian Ocean Territory | IO  
Christmas as Island | CX  
Cocos (Keeling) Islands | CC  
Falkland Islands (Islas Malvinas) | FK  
Mayotte | YT  
Niue | NU  
Norfolk Island | NF  
Northern Mariana Islands | MP  
Pitcairn Islands | PN  
Saint Helena, Ascension and Tristan da Cunha | SH  
Collectivity of Saint Martin | MF  
Saint Pierre and Miquelon | PM  
Tokelau | TK  
Wallis and Futuna | WF  
American Samoa | AS  
  
### Cancel withdrawal

You can cancel normal withdrawal requests, but you cannot cancel withdrawal requests on Lightning.

#### Rate Limit: 6 requests per second

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/asset/cancel-withdrawal`

> Request Example
    
    
    POST /api/v5/asset/cancel-withdrawal
    body {
       "wdId":"1123456"
    }
    
    
    
    
    import okx.Funding as Funding
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading: 0, Demo trading: 1
    
    fundingAPI = Funding.FundingAPI(apikey, secretkey, passphrase, False, flag)
    
    # Cancel withdrawal
    result = fundingAPI.cancel_withdrawal(
        wdId="123456"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
wdId | String | Yes | Withdrawal ID  
  
> Response Example
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
        {
          "wdId": "1123456"   
        }
      ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
wdId | String | Withdrawal ID  
If the code is equal to 0, it cannot be strictly considered that the withdrawal has been revoked. It only means that your request is accepted by the server. The actual result is subject to the status in the withdrawal history. 

### Get withdrawal history

Retrieve the withdrawal records according to the currency, withdrawal status, and time range in reverse chronological order. The 100 most recent records are returned by default.  
Websocket API is also available, refer to [Withdrawal info channel](/docs-v5/en/#funding-account-websocket-withdrawal-info-channel).

#### Rate Limit: 6 requests per second

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/asset/withdrawal-history`

> Request Example
    
    
    GET /api/v5/asset/withdrawal-history
    
    # Query withdrawal history from 2022-06-01 to 2022-07-01
    GET /api/v5/asset/withdrawal-history?ccy=BTC&after=1654041600000&before=1656633600000
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
ccy | String | No | Currency, e.g. `BTC`  
wdId | String | No | Withdrawal ID  
clientId | String | No | Client-supplied ID  
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
txId | String | No | Hash record of the deposit  
type | String | No | Withdrawal type  
`3`: Internal transfer  
`4`: On-chain withdrawal  
state | String | No | Status of withdrawal  
  

* Stage 1 : Pending withdrawal
`19`: insufficient balance in the hot wallet  
`17`: Pending response from Travel Rule vendor  
`10`: Waiting transfer  
`0`: Waiting withdrawal  
`4`/`5`/`6`/`8`/`9`/`12`: Waiting manual review  
`7`: Approved  
> `0`, `17`, `19` can be cancelled, other statuses cannot be cancelled  
  

* Stage 2 : Withdrawal in progress (Applicable to on-chain withdrawals, internal transfers do not have this stage)
`1`: Broadcasting your transaction to chain  
`15`: Pending transaction validation  
`16`: Due to local laws and regulations, your withdrawal may take up to 24 hours to arrive  
`-3`: Canceling   
  

* Final stage
`-2`: Canceled   
`-1`: Failed  
`2`: Success  
after | String | No | Pagination of data to return records earlier than the requested ts, Unix timestamp format in milliseconds, e.g. `1654041600000`  
before | String | No | Pagination of data to return records newer than the requested ts, Unix timestamp format in milliseconds, e.g. `1656633600000`  
limit | String | No | Number of results per request. The maximum is `100`; The default is `100`  
  
> Response Example
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
        {
          "note": "",
          "chain": "ETH-Ethereum",
          "fee": "0.007",
          "feeCcy": "ETH",
          "ccy": "ETH",
          "clientId": "",
          "toAddrType": "1",
          "amt": "0.029809",
          "txId": "0x35c******b360a174d",
          "from": "156****359",
          "areaCodeFrom": "86",
          "to": "0xa30d1fab********7CF18C7B6C579",
          "areaCodeTo": "",
          "state": "2",
          "ts": "1655251200000",
          "nonTradableAsset": false,
          "wdId": "15447421"
        }
      ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ccy | String | Currency  
chain | String | Chain name, e.g. `USDT-ERC20`, `USDT-TRC20`  
nonTradableAsset | Boolean | Whether it is a non-tradable asset or not  
`true`: non-tradable asset, `false`: tradable asset  
amt | String | Withdrawal amount  
ts | String | Time the withdrawal request was submitted, Unix timestamp format in milliseconds, e.g. `1655251200000`.  
from | String | Withdrawal account   
It can be `email`/`phone`/`sub-account name`  
areaCodeFrom | String | Area code for the phone number  
If `from` is a phone number, this parameter returns the area code for the phone number  
to | String | Receiving address  
areaCodeTo | String | Area code for the phone number  
If `to` is a phone number, this parameter returns the area code for the phone number  
toAddrType | String | Address type  
`1`: wallet address, email, phone, or login account name  
`2`: UID  
tag | String | Some currencies require a tag for withdrawals. This is not returned if not required.  
pmtId | String | Some currencies require a payment ID for withdrawals. This is not returned if not required.  
memo | String | Some currencies require this parameter for withdrawals. This is not returned if not required.  
addrEx | Object | Withdrawal address attachment (This will not be returned if the currency does not require this) e.g. TONCOIN attached tag name is comment, the return will be {'comment':'123456'}  
txId | String | Hash record of the withdrawal  
This parameter will return "" for internal transfers.  
fee | String | Withdrawal fee amount  
feeCcy | String | Withdrawal fee currency, e.g. `USDT`  
state | String | Status of withdrawal  
wdId | String | Withdrawal ID  
clientId | String | Client-supplied ID  
note | String | Withdrawal note  
  
### Get deposit withdraw status

Retrieve deposit's and withdrawal's detailed status and estimated complete time.

#### Rate Limit: 1 request per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/asset/deposit-withdraw-status`

> Request Example
    
    
    # For deposit
    GET /api/v5/asset/deposit-withdraw-status?txId=xxxxxx&to=1672734730284&ccy=USDT&chain=USDT-ERC20
    
    # For withdrawal
    GET /api/v5/asset/deposit-withdraw-status?wdId=200045249
    
    

#### Request Parameters

**Parameters** | **Types** | **Required** | **Description**  
---|---|---|---  
wdId | String | Conditional | Withdrawal ID, use to retrieve withdrawal status   
Required to input one and only one of `wdId` and `txId`  
txId | String | Conditional | Hash record of the deposit, use to retrieve deposit status   
Required to input one and only one of `wdId` and `txId`  
ccy | String | Conditional | Currency type, e.g. `USDT`   
Required when retrieving deposit status with `txId`  
to | String | Conditional | To address, the destination address in deposit   
Required when retrieving deposit status with `txId`  
chain | String | Conditional | Currency chain information, e.g. USDT-ERC20   
Required when retrieving deposit status with `txId`  
  
> Response Example
    
    
    {
        "code":"0",
        "data":[
            {
                "wdId": "200045249",
                "txId": "16f3638329xxxxxx42d988f97", 
                "state": "Pending withdrawal: Wallet is under maintenance, please wait.",
                "estCompleteTime": "01/09/2023, 8:10:48 PM"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
estCompleteTime | String | Estimated complete time  
The timezone is `UTC+8`. The format is MM/dd/yyyy, h:mm:ss AM/PM   
estCompleteTime is only an approximate estimated time, for reference only.  
state | String | The detailed stage and status of the deposit/withdrawal   
The message in front of the colon is the stage; the message after the colon is the ongoing status.  
txId | String | Hash record on-chain  
For withdrawal, if the `txId` has already been generated, it will return the value, otherwise, it will return "".  
wdId | String | Withdrawal ID  
When retrieving deposit status, wdId returns blank "".  
Stage References  
Deposit  
Stage 1: On-chain transaction detection   
Stage 2: Push deposit data to associated account   
Stage 3: Receiving account credit   
Final stage: Deposit complete  
Withdrawal  
Stage 1: Pending withdrawal   
Stage 2: Withdrawal in progress   
Final stage: Withdrawal complete / cancellation complete   

### Get exchange list (public)

Authentication is not required for this public endpoint.

#### Rate Limit: 6 requests per second

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/asset/exchange-list`

> Request Example
    
    
    GET /api/v5/asset/exchange-list
    
    
    
    
    

#### Request Parameters

None

> Response Example
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
        {
            "exchId": "did:ethr:0xfeb4f99829a9acdf52979abee87e83addf22a7e1",
            "exchName": "1xbet"
        }
      ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
exchName | String | Exchange name, e.g. `1xbet`  
exchId | String | Exchange ID, e.g. `did:ethr:0xfeb4f99829a9acdf52979abee87e83addf22a7e1`  
  
### Apply for monthly statement (last year)

Apply for monthly statement in the past year.

#### Rate Limit: 20 requests per month

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`POST /api/v5/asset/monthly-statement`

> Request Example
    
    
    POST /api/v5/asset/monthly-statement
    body
    {
        "month":"Jan"
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
month | String | No | Month,last month by default. Valid value is `Jan`, `Feb`, `Mar`, `Apr`,`May`, `Jun`, `Jul`,`Aug`, `Sep`,`Oct`,`Nov`,`Dec`  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "ts": "1646892328000"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
ts | String | Download link generation time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
### Get monthly statement (last year)

Retrieve monthly statement in the past year.

#### Rate Limit: 10 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/asset/monthly-statement`

> Request Example
    
    
    GET /api/v5/asset/monthly-statement?month=Jan
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
month | String | Yes | Month, valid value is `Jan`, `Feb`, `Mar`, `Apr`,`May`, `Jun`, `Jul`,`Aug`, `Sep`,`Oct`,`Nov`,`Dec`  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "fileHref": "http://xxx",
                "state": "finished",
                "ts": 1646892328000
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
fileHref | String | Download file link  
ts | Int | Download link generation time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
state | String | Download link status   
"finished" "ongoing"  
  
### Get convert currencies

#### Rate Limit: 6 requests per second

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/asset/convert/currencies`

> Request Example
    
    
    GET /api/v5/asset/convert/currencies
    
    

#### Response parameters

none

> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "min": "",  // Deprecated
                "max": "",  // Deprecated
                "ccy": "BTC"
            },
            {
                "min": "",
                "max": "",
                "ccy": "ETH"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ccy | String | Currency, e.g. BTC  
min | String | Minimum amount to convert ( Deprecated )  
max | String | Maximum amount to convert ( Deprecated )  
  
### Get convert currency pair

#### Rate Limit: 6 requests per second

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/asset/convert/currency-pair`

> Request Example
    
    
    GET /api/v5/asset/convert/currency-pair?fromCcy=USDT&toCcy=BTC
    
    

#### Response parameters

**Parameters** | **Types** | **Required** | **Description**  
---|---|---|---  
fromCcy | String | Yes | Currency to convert from, e.g. `USDT`  
toCcy | String | Yes | Currency to convert to, e.g. `BTC`  
convertMode | String | No | `0`: standard convert (default)   
`1`: large order convert for VIP  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "baseCcy": "BTC",
                "baseCcyMax": "0.5",
                "baseCcyMin": "0.0001",
                "instId": "BTC-USDT",
                "quoteCcy": "USDT",
                "quoteCcyMax": "10000",
                "quoteCcyMin": "1"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
instId | String | Currency pair, e.g. `BTC-USDT`  
baseCcy | String | Base currency, e.g. `BTC` in `BTC-USDT`  
baseCcyMax | String | Maximum amount of base currency  
baseCcyMin | String | Minimum amount of base currency  
quoteCcy | String | Quote currency, e.g. `USDT` in `BTC-USDT`  
quoteCcyMax | String | Maximum amount of quote currency  
quoteCcyMin | String | Minimum amount of quote currency  
  
### Estimate quote

#### Rate Limit: 10 requests per second

#### Rate limit rule: User ID

#### Rate Limit: 1 request per 5 seconds

#### Rate limit rule: Instrument ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/asset/convert/estimate-quote`

> Request Example
    
    
    POST /api/v5/asset/convert/estimate-quote
    body
    {
        "baseCcy": "ETH",
        "quoteCcy": "USDT",
        "side": "buy",
        "rfqSz": "30",
        "rfqSzCcy": "USDT"
    }
    

#### Request Parameters

**Parameters** | **Types** | **Required** | **Description**  
---|---|---|---  
baseCcy | String | Yes | Base currency, e.g. `BTC` in `BTC-USDT`  
quoteCcy | String | Yes | Quote currency, e.g. `USDT` in `BTC-USDT`  
side | String | Yes | Trade side based on `baseCcy`  
`buy` `sell`  
rfqSz | String | Yes | RFQ amount  
rfqSzCcy | String | Yes | RFQ currency  
clQReqId | String | No | Client Order ID as assigned by the client  
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
tag | String | No | Order tag  
Applicable to broker user  
convertMode | String | No | `0`: standard convert (default)   
`1`: large order convert for VIP  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "baseCcy": "ETH",
                "baseSz": "0.01023052",
                "clQReqId": "",
                "cnvtPx": "2932.40104429",
                "origRfqSz": "30",
                "quoteCcy": "USDT",
                "quoteId": "quoterETH-USDT16461885104612381",
                "quoteSz": "30",
                "quoteTime": "1646188510461",
                "rfqSz": "30",
                "rfqSzCcy": "USDT",
                "side": "buy",
                "ttlMs": "10000"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
quoteTime | String | Quotation generation time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
ttlMs | String | Validity period of quotation in milliseconds  
clQReqId | String | Client Order ID as assigned by the client  
quoteId | String | Quote ID  
baseCcy | String | Base currency, e.g. `BTC` in `BTC-USDT`  
quoteCcy | String | Quote currency, e.g. `USDT` in `BTC-USDT`  
side | String | Trade side based on `baseCcy`  
origRfqSz | String | Original RFQ amount  
rfqSz | String | Real RFQ amount  
rfqSzCcy | String | RFQ currency  
cnvtPx | String | Convert price based on quote currency  
baseSz | String | Convert amount of base currency  
quoteSz | String | Convert amount of quote currency  
  
### Convert trade

You should make [estimate quote](/docs-v5/en/#funding-account-rest-api-estimate-quote) before convert trade. 

Only assets in the trading account supported convert. 

#### Rate Limit: 10 requests per second

#### Rate limit rule: User ID

#### Permission: Trade

For the same side (buy/sell), there's a trading limit of 1 request per 5 seconds.

#### HTTP Request

`POST /api/v5/asset/convert/trade`

> Request Example
    
    
    POST /api/v5/asset/convert/trade
    body
    {
        "baseCcy": "ETH",
        "quoteCcy": "USDT",
        "side": "buy",
        "sz": "30",
        "szCcy": "USDT",
        "quoteId": "quoterETH-USDT16461885104612381"
    }
    

#### Request Parameters

**Parameters** | **Types** | **Required** | **Description**  
---|---|---|---  
quoteId | String | Yes | Quote ID  
baseCcy | String | Yes | Base currency, e.g. `BTC` in `BTC-USDT`  
quoteCcy | String | Yes | Quote currency, e.g. `USDT` in `BTC-USDT`  
side | String | Yes | Trade side based on `baseCcy`  
`buy` `sell`  
sz | String | Yes | Quote amount  
The quote amount should no more then RFQ amount  
szCcy | String | Yes | Quote currency  
clTReqId | String | No | Client Order ID as assigned by the client  
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
tag | String | No | Order tag  
Applicable to broker user  
convertMode | String | No | `0`: standard convert (default)   
`1`: large order convert for VIP  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "baseCcy": "ETH",
                "clTReqId": "",
                "fillBaseSz": "0.01023052",
                "fillPx": "2932.40104429",
                "fillQuoteSz": "30",
                "instId": "ETH-USDT",
                "quoteCcy": "USDT",
                "quoteId": "quoterETH-USDT16461885104612381",
                "side": "buy",
                "state": "fullyFilled",
                "tradeId": "trader16461885203381437",
                "ts": "1646188520338"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
tradeId | String | Trade ID  
quoteId | String | Quote ID  
clTReqId | String | Client Order ID as assigned by the client  
state | String | Trade state  
`fullyFilled`: success  
`rejected`: failed  
instId | String | Currency pair, e.g. `BTC-USDT`  
baseCcy | String | Base currency, e.g. `BTC` in `BTC-USDT`  
quoteCcy | String | Quote currency, e.g. `USDT` in `BTC-USDT`  
side | String | Trade side based on `baseCcy`  
`buy`  
`sell`  
fillPx | String | Filled price based on quote currency  
fillBaseSz | String | Filled amount for base currency  
fillQuoteSz | String | Filled amount for quote currency  
ts | String | Convert trade time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
### Get convert history

#### Rate Limit: 6 requests per second

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/asset/convert/history`

> Request Example
    
    
    GET /api/v5/asset/convert/history
    
    

#### Request Parameters

**Parameters** | **Types** | **Required** | **Description**  
---|---|---|---  
clTReqId | String | No | Client Order ID as assigned by the client  
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
after | String | No | Pagination of data to return records earlier than the requested `ts`, Unix timestamp format in milliseconds, e.g. `1597026383085`  
before | String | No | Pagination of data to return records newer than the requested `ts`, Unix timestamp format in milliseconds, e.g. `1597026383085`  
limit | String | No | Number of results per request. The maximum is `100`. The default is `100`.  
tag | String | No | Order tag  
Applicable to broker user  
If the convert trading used `tag`, this parameter is also required.  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "clTReqId": "",
                "instId": "ETH-USDT",
                "side": "buy",
                "fillPx": "2932.401044",
                "baseCcy": "ETH",
                "quoteCcy": "USDT",
                "fillBaseSz": "0.01023052",
                "state": "fullyFilled",
                "tradeId": "trader16461885203381437",
                "fillQuoteSz": "30",
                "ts": "1646188520000"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
tradeId | String | Trade ID  
clTReqId | String | Client Order ID as assigned by the client  
state | String | Trade state  
`fullyFilled` : success   
`rejected` : failed  
instId | String | Currency pair, e.g. `BTC-USDT`  
baseCcy | String | Base currency, e.g. `BTC` in `BTC-USDT`  
quoteCcy | String | Quote currency, e.g. `USDT` in `BTC-USDT`  
side | String | Trade side based on `baseCcy`  
`buy` `sell`  
fillPx | String | Filled price based on quote currency  
fillBaseSz | String | Filled amount for base currency  
fillQuoteSz | String | Filled amount for quote currency  
ts | String | Convert trade time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
### Get deposit payment methods

To display all the available fiat deposit payment methods

#### Rate Limit: 3 requests per second

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/fiat/deposit-payment-methods`

> Request Example
    
    
    GET /api/v5/fiat/deposit-payment-methods?ccy=TRY
    body
    {
      "ccy" : "TRY",
    }
    
    
    
    

#### Request Parameters

**Parameters** | **Types** | **Required** | **Description**  
---|---|---|---  
ccy | String | Yes | Fiat currency, ISO-4217 3 digit currency code, e.g. `TRY`  
  
> Response Example
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
        {
          "ccy": "TRY",
          "paymentMethod": "TR_BANKS",
          "feeRate": "0",
          "minFee": "0",
          "limits": {
            "dailyLimit": "2147483647",
            "dailyLimitRemaining": "2147483647",
            "weeklyLimit": "2147483647",
            "weeklyLimitRemaining": "2147483647",
            "monthlyLimit": "",
            "monthlyLimitRemaining": "",
            "maxAmt": "1000000",
            "minAmt": "1",
            "lifetimeLimit": "2147483647"
          },
          "accounts": [
              {
                "paymentAcctId": "1",
                "acctNum": "TR740001592093703829602611",
                "recipientName": "John Doe",
                "bankName": "VakıfBank",
                "bankCode": "TVBATR2AXXX",
                "state": "active"
              },
              {
                "paymentAcctId": "2",
                "acctNum": "TR740001592093703829602622",
                "recipientName": "John Doe",
                "bankName": "FBHLTRISXXX",
                "bankCode": "",
                "state": "active"
              }
          ]
        }
      ]
    }
    
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ccy | String | Fiat currency  
paymentMethod | String | The payment method associated with the currency  
`TR_BANKS`  
`PIX`  
`SEPA`  
`XPULSE`  
`NPP`  
`US_WIRE`  
feeRate | String | The fee rate for each deposit, expressed as a percentage  
e.g. `0.02` represents 2 percent fee for each transaction.  
minFee | String | The minimum fee for each deposit  
limits | Object | An object containing limits for various transaction intervals  
> dailyLimit | String | The daily transaction limit  
> dailyLimitRemaining | String | The remaining daily transaction limit  
> weeklyLimit | String | The weekly transaction limit  
> weeklyLimitRemaining | String | The remaining weekly transaction limit  
> monthlyLimit | String | The monthly transaction limit  
> monthlyLimitRemaining | String | The remaining monthly transaction limit  
> maxAmt | String | The maximum amount allowed per transaction  
> minAmt | String | The minimum amount allowed per transaction  
> lifetimeLimit | String | The lifetime transaction limit. Return the configured value, "" if not configured  
accounts | Array of Object | An array containing information about payment accounts associated with the currency and method.  
> paymentAcctId | String | The account ID for withdrawal  
> acctNum | String | The account number, which can be an IBAN or other bank account number.  
> recipientName | String | The name of the recipient  
> bankName | String | The name of the bank associated with the account  
> bankCode | String | The SWIFT code / BIC / bank code associated with the account  
> state | String | The state of the account  
`active`  
  
### Get withdrawal payment methods

To display all the available fiat withdrawal payment methods

#### Rate Limit: 3 requests per second

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/fiat/withdrawal-payment-methods`

> Request Example
    
    
     GET /api/v5/fiat/withdrawal-payment-methods?ccy=TRY
    
    
    
    
    

#### Request Parameters

**Parameters** | **Types** | **Required** | **Description**  
---|---|---|---  
ccy | String | Yes | Fiat currency, ISO-4217 3 digit currency code. e.g. `TRY`  
  
> Response Example
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
        {
          "ccy": "TRY",
          "paymentMethod": "TR_BANKS",
          "feeRate": "0.02",
          "minFee": "1",
          "limits": {
            "dailyLimit": "",
            "dailyLimitRemaining": "",
            "weeklyLimit": "",
            "weeklyLimitRemaining": "",
            "monthlyLimit": "",
            "monthlyLimitRemaining": "",
            "maxAmt": "",
            "minAmt": "",
            "lifetimeLimit": ""
          },
          "accounts": [
              {
                "paymentAcctId": "1",
                "acctNum": "TR740001592093703829602668",
                "recipientName": "John Doe",
                "bankName": "VakıfBank",
                "bankCode": "TVBATR2AXXX",
                "state": "active"
              },
              {
                "paymentAcctId": "2",
                "acctNum": "TR740001592093703829603024",
                "recipientName": "John Doe",
                "bankName": "Şekerbank",
                "bankCode": "SEKETR2AXXX",
                "state": "active"
              }
          ]
        }
      ]
    }
    
    
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ccy | String | Fiat currency  
paymentMethod | String | The payment method associated with the currency  
`TR_BANKS`  
`PIX`  
`SEPA`  
`XPULSE`  
`NPP`  
`US_WIRE`  
`SG_FAST`  
feeRate | String | The fee rate for each deposit, expressed as a percentage   
e.g. `0.02` represents 2 percent fee for each transaction.  
minFee | String | The minimum fee for each deposit  
limits | Object | An object containing limits for various transaction intervals  
> dailyLimit | String | The daily transaction limit  
> dailyLimitRemaining | String | The remaining daily transaction limit  
> weeklyLimit | String | The weekly transaction limit  
> weeklyLimitRemaining | String | The remaining weekly transaction limit  
> monthlyLimit | String | The monthly transaction limit  
> monthlyLimitRemaining | String | The remaining monthly transaction limit  
> minAmt | String | The minimum amount allowed per transaction  
> maxAmt | String | The maximum amount allowed per transaction  
> lifetimeLimit | String | The lifetime transaction limit. Return the configured value, "" if not configured  
accounts | Array of Object | An array containing information about payment accounts associated with the currency and method.  
> paymentAcctId | String | The account ID for withdrawal  
> acctNum | String | The account number, which can be an IBAN or other bank account number.  
> recipientName | String | The name of the recipient  
> bankName | String | The name of the bank associated with the account  
> bankCode | String | The SWIFT code / BIC / bank code associated with the account  
> state | String | The state of the account  
`active`  
  
### Create withdrawal order

Initiate a fiat withdrawal request (Authenticated endpoint, Only for API keys with "Withdrawal" access)  
Only supported withdrawal of assets from funding account.

#### Rate Limit: 3 requests per second

#### Rate limit rule: User ID

#### Permission: Withdraw

#### HTTP Request

`POST /api/v5/fiat/create-withdrawal`

> Request Example
    
    
     POST /api/v5/fiat/create-withdrawal
     body
     {
        "paymentAcctId": "412323",
        "ccy": "TRY",
        "amt": "10000",
        "paymentMethod": "TR_BANKS",
        "clientId": "194a6975e98246538faeb0fab0d502df"
     }
    
    
    
    

#### Request Parameters

**Parameters** | **Type** | **Required** | **Description**  
---|---|---|---  
paymentAcctId | String | Yes | Payment account id to withdraw to, retrieved from get withdrawal payment methods API  
ccy | String | Yes | Currency for withdrawal, must match currency allowed for paymentMethod  
amt | String | Yes | Requested withdrawal amount before fees. Has to be less than or equal to 2 decimal points double  
paymentMethod | String | Yes | Payment method to use for withdrawal  
`TR_BANKS`  
`PIX`  
`SEPA`  
`XPULSE`  
`NPP`  
`US_WIRE`  
`SG_FAST`  
clientId | String | Yes | Client-supplied ID, A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters   
e.g. `194a6975e98246538faeb0fab0d502df`  
  
> Response Example
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
        {
            "cTime": "1707429385000",
            "uTime": "1707429385000",
            "ordId": "124041201450544699",
            "paymentMethod": "TR_BANKS",
            "paymentAcctId": "20",
            "fee": "0",
            "amt": "100",
            "ccy": "TRY",
            "state": "completed",
            "clientId": "194a6975e98246538faeb0fab0d502df"
        }
      ]
    }
    
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ordId | String | The unique order Id  
clientId | String | The client ID associated with the transaction  
amt | String | The requested amount for the transaction  
ccy | String | The currency of the transaction  
fee | String | The transaction fee  
paymentAcctId | String | The Id of the payment account used  
paymentMethod | String | Payment Method  
`TR_BANKS`  
`PIX`  
`SEPA`  
state | String | The State of the transaction  
`processing`  
`completed`  
cTime | String | The creation time of the transaction, Unix timestamp format in milliseconds, e.g. `1597026383085`  
uTime | String | The update time of the transaction, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
### Cancel withdrawal order

Cancel a pending fiat withdrawal order, currently only applicable to TRY

#### Rate Limit: 3 requests per second

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/fiat/cancel-withdrawal`

> Request Example
    
    
     POST /api/v5/fiat/cancel-withdrawal
     body
     {
        "ordId": "124041201450544699"
     }
    
    
    
    

#### Request Parameters

**Parameters** | **Types** | **Required** | **Description**  
---|---|---|---  
ordId | String | Yes | Payment Order Id  
  
> Response Example
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
        {
            "ordId": "124041201450544699",
            "state": "canceled"
        }
      ]
    }
    
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ordId | String | Payment Order ID  
state | String | The state of the transaction, e.g.`canceled`  
  
### Get withdrawal order history

Get fiat withdrawal order history

#### Rate Limit: 3 requests per second

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/fiat/withdrawal-order-history`

> Request Example
    
    
     GET /api/v5/fiat/withdrawal-order-history
    
    
    
    
    

#### Request Parameters

**Parameters** | **Types** | **Required** | **Description**  
---|---|---|---  
ccy | String | No | Fiat currency, ISO-4217 3 digit currency code, e.g. `TRY`  
paymentMethod | String | No | Payment Method  
`TR_BANKS`  
`PIX`  
`SEPA`  
`XPULSE`  
`NPP`  
`US_WIRE`  
`SG_FAST`  
state | String | No | State of the order  
`completed`  
`failed`  
`pending`  
`canceled`  
`inqueue`  
`processing`  
after | String | No | Filter with a begin timestamp. Unix timestamp format in milliseconds (inclusive), e.g. `1597026383085`  
before | String | No | Filter with an end timestamp. Unix timestamp format in milliseconds (inclusive), e.g. `1597026383085`  
limit | String | No | Number of results per request. Maximum and default is `100`  
  
> Response Example
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
        {
            "cTime": "1707429385000",
            "uTime": "1707429385000",
            "ordId": "124041201450544699",
            "paymentMethod": "TR_BANKS",
            "paymentAcctId": "20",
            "amt": "10000",
            "fee": "0",
            "ccy": "TRY",
            "state": "completed",
            "clientId": "194a6975e98246538faeb0fab0d502df"
        },
        {
            "cTime": "1707429385000",
            "uTime": "1707429385000",
            "ordId": "124041201450544690",
            "paymentMethod": "TR_BANKS",
            "paymentAcctId": "20",
            "amt": "5000",
            "fee": "0",
            "ccy": "TRY",
            "state": "completed",
            "clientId": "164a6975e48946538faeb0fab0d414fg"
        }
      ]
    }
    
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ordId | String | Unique Order Id  
clientId | String | Client Id of the transaction  
amt | String | Final amount of the transaction  
ccy | String | Currency of the transaction  
fee | String | Transaction fee  
paymentAcctId | String | ID of the payment account used  
paymentMethod | String | Payment method type  
state | String | State of the transaction  
`completed`  
`failed`  
`pending`  
`canceled`  
`inqueue`  
`processing`  
cTime | String | Creation time of the transaction, Unix timestamp format in milliseconds, e.g. `1597026383085`  
uTime | String | Update time of the transaction, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
### Get withdrawal order detail

Get fiat withdraw order detail

#### Rate Limit: 3 requests per second

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/fiat/withdrawal`

> Request Example
    
    
     GET /api/v5/fiat/withdrawal?ordId=024041201450544699
     body
     {
        "ordId": "024041201450544699"
     }
    
    
    
    

#### Request Parameters

**Parameters** | **Types** | **Required** | **Description**  
---|---|---|---  
ordId | String | Yes | Order ID  
  
> Response Example
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
        {
            "cTime": "1707429385000",
            "uTime": "1707429385000",
            "ordId": "024041201450544699",
            "paymentMethod": "TR_BANKS",
            "paymentAcctId": "20",
            "amt": "100",
            "fee": "0",
            "ccy": "TRY",
            "state": "completed",
            "clientId": "194a6975e98246538faeb0fab0d502df"
        }
      ]
    }
    
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ordId | String | Order ID  
clientId | String | The original request ID associated with the transaction  
ccy | String | The currency of the transaction  
amt | String | Amount of the transaction  
fee | String | The transaction fee  
paymentAcctId | String | The ID of the payment account used  
paymentMethod | String | Payment method, e.g. `TR_BANKS`  
`PIX`  
`SEPA`  
`XPULSE`  
`NPP`  
`US_WIRE`  
`SG_FAST`  
state | String | The state of the transaction  
`completed`  
`failed`  
`pending`  
`canceled`  
`inqueue`  
`processing`  
cTime | String | The creation time of the transaction, Unix timestamp format in milliseconds, e.g. `1597026383085`  
uTime | String | The update time of the transaction, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
### Get deposit order history

Get fiat deposit order history

#### Rate Limit: 3 requests per second

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/fiat/deposit-order-history`

> Request Example
    
    
     GET /api/v5/fiat/deposit-order-history
    
    
    
    
    

#### Request Parameters

**Parameters** | **Types** | **Required** | **Description**  
---|---|---|---  
ccy | String | No | ISO-4217 3 digit currency code  
paymentMethod | String | No | Payment Method  
`TR_BANKS`  
`PIX`  
`SEPA`  
`XPULSE`  
`NPP`  
`US_WIRE`  
state | String | No | State of the order  
`completed`  
`failed`  
`pending`  
`canceled`  
`inqueue`  
`processing`  
after | String | No | Filter with a begin timestamp. Unix timestamp format in milliseconds (inclusive), e.g. `1597026383085`  
before | String | No | Filter with an end timestamp. Unix timestamp format in milliseconds (inclusive), e.g. `1597026383085`  
limit | String | No | Number of results per request. Maximum and default is 100  
  
> Response Example
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
        {
            "cTime": "1707429385000",
            "uTime": "1707429385000",
            "ordId": "024041201450544699",
            "paymentMethod": "TR_BANKS",
            "paymentAcctId": "20",
            "amt": "10000",
            "fee": "0",
            "ccy": "TRY",
            "state": "completed",
            "clientId": ""
        },
        {
            "cTime": "1707429385000",
            "uTime": "1707429385000",
            "ordId": "024041201450544690",
            "paymentMethod": "TR_BANKS",
            "paymentAcctId": "20",
            "amt": "50000",
            "fee": "0",
            "ccy": "TRY",
            "state": "completed",
            "clientId": ""
        }
      ]
    }
    
    
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ordId | String | Unique Order ID  
clientId | String | Client Id of the transaction  
ccy | String | Currency of the transaction  
amt | String | Final amount of the transaction  
fee | String | Transaction fee  
paymentAcctId | String | ID of the payment account used  
paymentMethod | String | Payment Method, e.g. `TR_BANKS`  
state | String | State of the transaction  
`completed`  
`failed`  
`pending`  
`canceled`  
`inqueue`  
cTime | String | Creation time of the transaction, Unix timestamp format in milliseconds, e.g. `1597026383085`  
uTime | String | Update time of the transaction, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
### Get deposit order detail

Get fiat deposit order detail

#### Rate Limit: 3 requests per second

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/fiat/deposit`

> Request Example
    
    
    GET /api/v5/fiat/deposit?ordId=024041201450544699
    body
    {
        "ordId": "024041201450544699",
    }
    
    
    
    

#### Request Parameters

**Parameters** | **Types** | **Required** | **Description**  
---|---|---|---  
ordId | String | Yes | Order ID  
  
> Response Example
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
        {
            "cTime": "1707429385000",
            "uTime": "1707429385000",
            "ordId": "024041201450544699",
            "paymentMethod": "TR_BANKS",
            "paymentAcctId": "20",
            "amt": "100",
            "fee": "0",
            "ccy": "TRY",
            "state": "completed",
            "clientId": ""
        }
      ]
    }
    
    
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ordId | String | Order ID  
clientId | String | The original request ID associated with the transaction. If it's a deposit, it's most likely an empty string ("").  
amt | String | Amount of the transaction  
ccy | String | The currency of the transaction  
fee | String | The transaction fee  
paymentAcctId | String | The ID of the payment account used  
paymentMethod | String | Payment method, e.g.`TR_BANKS`  
`PIX`  
`SEPA`  
`XPULSE`  
`NPP`  
`US_WIRE`  
state | String | The state of the transaction  
`completed`  
`failed`  
`pending`  
`canceled`  
`inqueue`  
`processing`  
cTime | String | The creation time of the transaction, Unix timestamp format in milliseconds, e.g. `1597026383085`  
uTime | String | The update time of the transaction, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
### Get buy/sell currencies

#### Rate Limit: 6 requests per second

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/fiat/buy-sell/currencies`

> Request Example
    
    
    GET /api/v5/fiat/buy-sell/currencies
    

> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
               "fiatCcyList":[
                    {
                        "ccy": "USD"
                    },
                    {
                        "ccy": "EUR"
                    },
                    ...
                ],
                "cryptoCcyList":[
                    {
                        "ccy": "BTC"
                    },
                    ...
                ],
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
fiatCcyList | Array of objects | Fiat currency list  
>ccy | String | Currency, e.g. `BTC`  
cryptoCcyList | Array of objects | Crypto currency list  
>ccy | String | Currency, e.g. `USD`  
  
This feature is only available to Bahamas institutional users at the moment. 

### Get buy/sell currency pair

#### Rate Limit: 6 requests per second

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/fiat/buy-sell/currency-pair`

> Request Example
    
    
    GET /api/v5/fiat/buy-sell/currency-pair?fromCcy=USD&toCcy=BTC
    

#### Request Parameters

Parameters | Types | Required | Description  
---|---|---|---  
fromCcy | String | Yes | Currency to sell, e.g. `USD`  
toCcy | String | Yes | Currency to buy, e.g. `BTC`  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "side": "buy",
                "fromCcy": "USD",
                "toCcy": "BTC",
                "singleTradeMax": "1",
                "singleTradeMin": "0.01",
                "fixedPxRemainingDailyQuota": "", 
                "fixedPxDailyLimit": "", 
                "paymentMethods":["balance"]
            }
        ],
        "msg": ""
    }
    
    
    
    {
        "code": "0",
        "data": [
            {
                "side": "sell",
                "fromCcy": "BTC",
                "toCcy": "USD",
                "singleTradeMax": "1",
                "singleTradeMin": "0.01",
                "fixedPxRemainingDailyQuota": "", 
                "fixedPxDailyLimit": "", 
                "paymentMethods":["balance"]
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
side | String | Side  
`buy`: Fiat to crypto  
`sell`: Crypto to fiat  
May support both sides in the future, separated with a comma, e.g. `buy,sell`.  
fromCcy | String | Currency to sell, e.g. `USD`  
toCcy | String | Currency to buy, e.g. `BTC`  
singleTradeMax | String | The maximum amount of currency for a single trade, unit in `fromCcy`  
singleTradeMin | String | The minimum amount of currency for a single trade, unit in `fromCcy`  
fixedPxDailyLimit | String | Fixed price daily limit  
Applicable to Fiat to Fiat trade, else return ''.  
If `side` = `buy`, unit in `fromCcy`  
If `side` = `sell`, unit in `toCcy`  
fixedPxRemainingDailyQuota | String | Fixed price remaining daily quota  
Applicable to Fiat to Fiat trade, else return ''.  
If `side` = `buy`, unit in `fromCcy`  
If `side` = `sell`, unit in `toCcy`  
paymentMethods | Array of strings | Supported payment methods  
`balance`  
e.g. ["balance"]  
  
This feature is only available to Bahamas institutional users at the moment. 

### Get buy/sell quote

#### Rate Limit: 10 requests per second

#### Rate limit rule: User ID

#### Rate Limit: 1 request per 5 seconds

#### Rate limit rule: Instrument ID

#### Permission: Read

#### HTTP Request

`POST /api/v5/fiat/buy-sell/quote`

> Request Example
    
    
    # Sell USD to buy 0.1 BTC
    POST /api/v5/fiat/buy-sell/quote
    body
    {
        "side":"buy",
        "fromCcy": "USD",
        "toCcy": "BTC",
        "rfqAmt": "0.1",
        "rfqCcy": "BTC"
    }
    
    # Sell 30 USD to buy BTC
    POST /api/v5/fiat/buy-sell/quote
    body
    {
        "side":"buy",
        "fromCcy": "USD",
        "toCcy": "BTC",
        "rfqAmt": "30",
        "rfqCcy": "USD"
    }
    
    # Sell BTC to buy 30 USD
    POST /api/v5/fiat/buy-sell/quote
    body
    {
        "side":"sell",
        "fromCcy": "BTC",
        "toCcy": "USD",
        "rfqAmt": "30",
        "rfqCcy": "USD"
    }
    
    # Sell 0.1 BTC to buy USD
    POST /api/v5/fiat/buy-sell/quote
    body
    {
        "side":"sell",
        "fromCcy": "BTC",
        "toCcy": "USD",
        "rfqAmt": "0.1",
        "rfqCcy": "BTC"
    }
    

#### Request Parameters

Parameters | Types | Required | Description  
---|---|---|---  
side | String | Yes | Side   
`buy`: Buy Crypto / Fiat with Fiat   
`sell`: Sell Crypto to Crypto / Fiat  
fromCcy | String | Yes | Currency to sell  
toCcy | String | Yes | Currency to buy  
rfqAmt | String | Yes | RFQ amount  
rfqCcy | String | Yes | RFQ currency  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "quoteId": "quoterBTC-USD16461885104612381",
                "fromCcy": "USD",
                "toCcy": "BTC",
                "rfqAmt": "30",
                "rfqCcy": "USD",
                "quotePx": "2932.40104429",
                "quoteCcy": "USD",
                "quoteFromAmt": "30",
                "quoteToAmt": "30",
                "quoteTime": "1646188510461",
                "ttlMs": "10000"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
quoteId | String | Quote ID  
side | String | Side   
`buy`: Buy Crypto / Fiat with Fiat   
`sell`: Sell Crypto to Crypto / Fiat  
fromCcy | String | Currency to sell, e.g. `USD`  
toCcy | String | Currency to buy, e.g. `BTC`  
rfqAmt | String | RFQ amount  
rfqCcy | String | RFQ currency  
quotePx | String | Quote price  
quoteCcy | String | Quote price unit   
e.g. `USD`  
quoteFromAmt | String | Quote amount, unit in `fromCcy`  
quoteToAmt | String | Quote amount, unit in `toCcy`  
quoteTime | String | Quotation generation time, Unix timestamp format in milliseconds, e.g. 1597026383085  
ttlMs | String | The validity period of quotation in milliseconds   
e.g. `10000` represents the quotation only valid for 10 seconds  
  
This feature is only available to Bahamas institutional users at the moment. 

### Buy/sell trade

#### Rate Limit: 1 request per 5 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/fiat/buy-sell/trade`

> Request Example
    
    
    # Sell 30 USD to buy BTC
    POST /api/v5/fiat/buy-sell/trade
    body
    {
        "clOrdId":"123456",
        "side":"sell",
        "fromCcy": "USD",
        "toCcy": "BTC",
        "rfqAmt": "30",
        "rfqCcy": "USD",
        "paymentMethod":"balance",
        "quoteId": "quoterETH-USDT16461885104612381"
    }
    

#### Request Parameters

Parameters | Types | Required | Description  
---|---|---|---  
quoteId | String | Yes | Quote ID  
Get from Buy/Sell quote API  
side | String | Yes | Side   
`buy`: Buy Crypto / Fiat with Fiat   
`sell`: Sell Crypto to Crypto / Fiat   
Should be the same as the Quote request  
fromCcy | String | Yes | Currency to sell   
Should be the same as the Quote request  
toCcy | String | Yes | Currency to buy   
Should be the same as the Quote request  
rfqAmt | String | Yes | RFQ amount   
Should be the same as the Quote request  
rfqCcy | String | Yes | RFQ currency   
Should be the same as the Quote request  
paymentMethod | String | Yes | paymentMethod   
`balance`  
clOrdId | String | Yes | Client Order ID as assigned by the client   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "ordId": "1234",
                "clOrdId": "",
                "quoteId": "quoterBTC-USD16461885104612381",
                "side":"buy",
                "fromCcy": "USD",
                "toCcy": "BTC",
                "rfqAmt": "30",
                "rfqCcy": "USD",
                "fillPx": "2932.40104429",
                "fillQuoteCcy": "USD",
                "fillFromAmt": "30",
                "fillToAmt": "0.01",
                "cTime": "1646188510461"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ordId | String | Order ID  
clOrdId | String | Client Order ID as assigned by the client  
quoteId | String | Quote ID  
state | String | Trade state   
`processing`   
`completed`   
`failed`  
side | String | Side   
`buy`: Buy Crypto / Fiat with Fiat   
`sell`: Sell Crypto to Crypto / Fiat  
fromCcy | String | Currency to sell  
toCcy | String | Currency to buy  
rfqAmt | String | RFQ amount  
rfqCcy | String | RFQ currency  
fillPx | String | Filled price based on quote currency  
fillQuoteCcy | String | Filled price quote currency   
e.g. `USD`  
fillFromAmt | String | Sold amount, unit in `fromCcy`  
fillToAmt | String | Bought amount, unit in `toCcy`  
cTime | String | Request time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
This feature is only available to Bahamas institutional users at the moment. 

### Get buy/sell trade history

#### Rate Limit: 6 requests per second

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/fiat/buy-sell/history`

> Request Example
    
    
    GET /api/v5/fiat/buy-sell/history
    

#### Request Parameters

Parameters | Types | Required | Description  
---|---|---|---  
ordId | String | No | Order ID  
clOrdId | String | No | Client Order ID as assigned by the client   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
state | String | No | Trade state   
`processing`   
`completed`   
`failed`  
begin | String | No | Filter with a begin timestamp. Unix timestamp format in milliseconds, e.g. `1597026383085`  
end | String | No | Filter with an end timestamp. Unix timestamp format in milliseconds, e.g. `1597026383085`  
limit | String | No | Number of results per request. The maximum is 100. The default is 100.  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "ordId": "1234",
                "clOrdId": "",
                "quoteId": "quoterBTC-USD16461885104612381",
                "state":"completed",
                "side":"buy",
                "fromCcy": "USD",
                "toCcy": "BTC",
                "rfqAmt": "30",
                "rfqCcy": "USD",
                "fillPx": "2932.40104429",
                "fillQuoteCcy": "USD",
                "fillFromAmt": "30",
                "fillToAmt": "0.01",
                "cTime": "1646188510461",
                "uTime": "1646188510461"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ordId | String | Order ID  
clOrdId | String | Client Order ID as assigned by the client  
quoteId | String | Quote ID  
state | String | Trade state   
`processing`   
`completed`   
`failed`  
fromCcy | String | Currency to sell  
toCcy | String | Currency to buy  
rfqAmt | String | RFQ amount  
rfqCcy | String | RFQ currency  
fillPx | String | Filled price based on quote currency  
fillQuoteCcy | String | Filled price quote currency   
e.g. `USD`  
fillFromAmt | String | Filled amount unit in fromCcy  
fillToAmt | String | Filled amount unit in toCcy  
cTime | String | Request time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
uTime | String | Updated time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
This feature is only available to Bahamas institutional users at the moment. 

## WebSocket

### Deposit info channel

A push notification is triggered when a deposit is initiated or the deposit status changes.  
Supports subscriptions for accounts  

  * If it is a master account subscription, you can receive the push of the deposit info of both the master account and the sub-account.
  * If it is a sub-account subscription, only the push of sub-account deposit info you can receive.

#### URL Path

/ws/v5/business (required login)

> Request Example
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [
            {
                "channel": "deposit-info"
            }
        ]
    }
    
    
    
    import asyncio
    from okx.websocket.WsPrivateAsync import WsPrivateAsync
    
    def callbackFunc(message):
        print(message)
    
    async def main():
        ws = WsPrivateAsync(
            apiKey = "YOUR_API_KEY",
            passphrase = "YOUR_PASSPHRASE",
            secretKey = "YOUR_SECRET_KEY",
            url = "wss://ws.okx.com:8443/ws/v5/business",
            useServerTime=False
        )
        await ws.start()
        args = [
            {
                "channel": "deposit-info"
            }
        ]
        await ws.subscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
        await ws.unsubscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
    
    asyncio.run(main())
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
id | String | No | Unique identifier of the message   
Provided by client. It will be returned in response message for identifying the corresponding request.   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
op | String | Yes | Operation  
`subscribe`  
`unsubscribe`  
  
args | Array of objects | Yes | List of subscribed channels  
> channel | String | Yes | Channel name  
`deposit-info`  
> ccy | String | No | Currency, e.g. `BTC`  
  
> Successful Response Example
    
    
    {
        "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "deposit-info"
        },
        "connId": "a4d3ae55"
    }
    

> Failure Response Example
    
    
    {
        "id": "1512",
        "event": "error",
        "code": "60012",
        "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"deposit-info\""}]}",
        "connId": "a4d3ae55"
    }
    

#### Response parameters

Parameter | Type | Required | Description  
---|---|---|---  
id | String | No | Unique identifier of the message  
event | String | Yes | Operation  
`subscribe`  
`unsubscribe`  
`error`  
arg | Object | No | Subscribed channel  
> channel | String | Yes | Channel name  
`deposit-info`  
> ccy | String | No | Currency, e.g. `BTC`  
code | String | No | Error code  
msg | String | No | Error message  
connId | String | Yes | WebSocket connection ID  
  
> Push Data Example
    
    
    {
        "arg": {
            "channel": "deposit-info",
            "uid": "289320****60975104"
        },
        "data": [{
            "actualDepBlkConfirm": "0",
            "amt": "1",
            "areaCodeFrom": "",
            "ccy": "USDT",
            "chain": "USDT-TRC20",
            "depId": "88165462",
            "from": "",
            "fromWdId": "",
            "pTime": "1674103661147",
            "state": "0",
            "subAcct": "test",
            "to": "TEhFAqpuHa3LY*****8ByNoGnrmexeGMw",
            "ts": "1674103661123",
            "txId": "bc5376817*****************dbb0d729f6b",
            "uid": "289320****60975104"
        }]
    }
    

#### Push data parameters

**Parameters** | **Types** | **Description**  
---|---|---  
arg | Object | Successfully subscribed channel  
> channel | String | Channel name  
`deposit-info`  
> uid | String | User Identifier  
> ccy | String | Currency, e.g. `BTC`  
data | Array of objects | Subscribed data  
> uid | String | User Identifier of the message producer  
> subAcct | String | Sub-account name  
If the message producer is master account, the parameter will return ""  
> pTime | String | Push time, the millisecond format of the Unix timestamp, e.g. `1597026383085`  
> ccy | String | Currency  
> chain | String | Chain name  
> amt | String | Deposit amount  
> from | String | Deposit account  
Only the internal OKX account (masked mobile phone number or email address) is returned, not the address on the blockchain.  
> areaCodeFrom | String | If `from` is a phone number, this parameter return area code of the phone number  
> to | String | Deposit address  
> txId | String | Hash record of the deposit  
> ts | String | Time of deposit record is created, Unix timestamp format in milliseconds, e.g. `1655251200000`  
> state | String | Status of deposit  
`0`: waiting for confirmation  
`1`: deposit credited   
`2`: deposit successful   
`8`: pending due to temporary deposit suspension on this crypto currency  
`11`: match the address blacklist  
`12`: account or deposit is frozen  
`13`: sub-account deposit interception  
`14`: KYC limit  
> depId | String | Deposit ID  
> fromWdId | String | Internal transfer initiator's withdrawal ID  
If the deposit comes from internal transfer, this field displays the withdrawal ID of the internal transfer initiator, and will return "" in other cases  
> actualDepBlkConfirm | String | The actual amount of blockchain confirmed in a single deposit  
  
### Withdrawal info channel

A push notification is triggered when a withdrawal is initiated or the withdrawal status changes.  
Supports subscriptions for accounts  

  * If it is a master account subscription, you can receive the push of the withdrawal info of both the master account and the sub-account.
  * If it is a sub-account subscription, only the push of sub-account withdrawal info you can receive.

#### URL Path

/ws/v5/business (required login)

> Request Example
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [
            {
                "channel": "withdrawal-info"
            }
        ]
    }
    
    
    
    import asyncio
    from okx.websocket.WsPrivateAsync import WsPrivateAsync
    
    def callbackFunc(message):
        print(message)
    
    async def main():
        ws = WsPrivateAsync(
            apiKey = "YOUR_API_KEY",
            passphrase = "YOUR_PASSPHRASE",
            secretKey = "YOUR_SECRET_KEY",
            url = "wss://ws.okx.com:8443/ws/v5/business",
            useServerTime=False
        )
        await ws.start()
        args = [
            {
                "channel": "withdrawal-info"
            }
        ]
    
        await ws.subscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
        await ws.unsubscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
    
    asyncio.run(main())
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
id | String | No | Unique identifier of the message   
Provided by client. It will be returned in response message for identifying the corresponding request.   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
op | String | Yes | Operation  
`subscribe`  
`unsubscribe`  
  
args | Array of objects | Yes | List of subscribed channels  
> channel | String | Yes | Channel name  
`withdrawal-info`  
> ccy | String | No | Currency, e.g. `BTC`  
  
> Successful Response Example
    
    
    {
        "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "withdrawal-info"
        },
        "connId": "a4d3ae55"
    }
    

> Failure Response Example
    
    
    {
        "id": "1512",
        "event": "error",
        "code": "60012",
        "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"withdrawal-info\"}]}",
        "connId": "a4d3ae55"
    }
    

#### Response parameters

Parameter | Type | Required | Description  
---|---|---|---  
id | String | No | Unique identifier of the message  
event | String | Yes | Operation  
`subscribe`  
`unsubscribe`  
`error`  
arg | Object | No | Subscribed channel  
> channel | String | Yes | Channel name  
`withdrawal-info`  
> ccy | String | No | Currency, e.g. `BTC`  
code | String | No | Error code  
msg | String | No | Error message  
connId | String | Yes | WebSocket connection ID  
  
> Push Data Example
    
    
    {
        "arg": {
            "channel": "withdrawal-info",
            "uid": "289320*****0975104"
        },
        "data": [{
            "addrEx": null,
            "amt": "2",
            "areaCodeFrom": "",
            "areaCodeTo": "",
            "ccy": "USDT",
            "chain": "USDT-TRC20",
            "clientId": "",
            "fee": "0.8",
            "feeCcy": "USDT",
            "from": "",
            "memo": "",
            "nonTradableAsset": false,
            "note": "",
            "pTime": "1674103268578",
            "pmtId": "",
            "state": "0",
            "subAcct": "test",
            "tag": "",
            "to": "TN8CKTQMnpWfT******8KipbJ24ErguhF",
            "toAddrType": "1",
            "ts": "1674103268472",
            "txId": "",
            "uid": "289333*****1101696",
            "wdId": "63754560"
        }]
    }
    

#### Push data parameters

**Parameters** | **Types** | **Description**  
---|---|---  
arg | Object | Successfully subscribed channel  
> channel | String | Channel name  
> uid | String | User Identifier  
> ccy | String | Currency, e.g. `BTC`  
data | Array of objects | Subscribed data  
> uid | String | User Identifier of the message producer  
> subAcct | String | Sub-account name  
If the message producer is master account, the parameter will return ""  
> pTime | String | Push time, the millisecond format of the Unix timestamp, e.g. `1597026383085`  
> ccy | String | Currency  
> chain | String | Chain name, e.g. `USDT-ERC20`, `USDT-TRC20`  
> nonTradableAsset | String | Whether it is a non-tradable asset or not  
`true`: non-tradable asset, `false`: tradable asset  
> amt | String | Withdrawal amount  
> ts | String | Time the withdrawal request was submitted, Unix timestamp format in milliseconds, e.g. `1655251200000`.  
> from | String | Withdrawal account  
It can be `email`/`phone`/`sub-account name`  
> areaCodeFrom | String | Area code for the phone number  
If `from` is a phone number, this parameter returns the area code for the phone number  
> to | String | Receiving address  
> areaCodeTo | String | Area code for the phone number  
If `to` is a phone number, this parameter returns the area code for the phone number  
> toAddrType | String | Address type  
`1`: wallet address, email, phone, or login account name  
`2`: UID  
> tag | String | Some currencies require a tag for withdrawals  
> pmtId | String | Some currencies require a payment ID for withdrawals  
> memo | String | Some currencies require this parameter for withdrawals  
> addrEx | Object | Withdrawal address attachment, e.g. `TONCOIN` attached tag name is comment, the return will be {'comment':'123456'}  
> txId | String | Hash record of the withdrawal   
This parameter will return "" for internal transfers.  
> fee | String | Withdrawal fee amount  
> feeCcy | String | Withdrawal fee currency, e.g. `USDT`  
> state | String | Status of withdrawal  
  

* Stage 1 : Pending withdrawal
`17`: Pending response from Travel Rule vendor  
`10`: Waiting transfer  
`0`: Waiting withdrawal  
`4`/`5`/`6`/`8`/`9`/`12`: Waiting manual review  
`7`: Approved  
  

* Stage 2 : Withdrawal in progress (Applicable to on-chain withdrawals, internal transfers do not have this stage)
`1`: Broadcasting your transaction to chain  
`15`: Pending transaction validation  
`16`: Due to local laws and regulations, your withdrawal may take up to 24 hours to arrive  
`-3`: Canceling   
  

* Final stage
`-2`: Canceled   
`-1`: Failed  
`2`: Success  
> wdId | String | Withdrawal ID  
> clientId | String | Client-supplied ID  
> note | String | Withdrawal note

---

# 资金账户

`资金`功能模块下的API接口需要身份验证。

## REST API 

### 获取币种列表 

获取当前用户KYC实体支持的币种列表。

#### 限速：6 次/s

#### 限速规则：User ID

#### 权限：读取

#### HTTP 请求

`GET /api/v5/asset/currencies`

> 请求示例
    
    
    GET /api/v5/asset/currencies
    
    
    
    
    import okx.Funding as Funding
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    fundingAPI = Funding.FundingAPI(apikey, secretkey, passphrase, False, flag)
    
    # 获取币种列表
    result = fundingAPI.get_currencies()
    print(result)
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 否 | 币种，如 `BTC`  
支持多币种查询，币种之间半角逗号分隔  
  
> 返回结果
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
        {
            "burningFeeRate": "",
            "canDep": true,
            "canInternal": true,
            "canWd": true,
            "ccy": "BTC",
            "chain": "BTC-Bitcoin",
            "ctAddr": "",
            "depEstOpenTime": "",
            "depQuotaFixed": "",
            "depQuoteDailyLayer2": "",
            "fee": "0.00005",
            "logoLink": "https://static.coinall.ltd/cdn/oksupport/asset/currency/icon/btc20230419112752.png",
            "mainNet": true,
            "maxFee": "0.00005",
            "maxFeeForCtAddr": "",
            "maxWd": "500",
            "minDep": "0.0005",
            "minDepArrivalConfirm": "1",
            "minFee": "0.00005",
            "minFeeForCtAddr": "",
            "minInternal": "0.0001",
            "minWd": "0.0005",
            "minWdUnlockConfirm": "2",
            "name": "Bitcoin",
            "needTag": false,
            "usedDepQuotaFixed": "",
            "usedWdQuota": "0",
            "wdEstOpenTime": "",
            "wdQuota": "10000000",
            "wdTickSz": "8"
        }
      ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ccy | String | 币种名称，如 `BTC`  
name | String | 币种名称，不显示则无对应名称  
logoLink | String | 币种Logo链接  
chain | String | 币种链信息  
有的币种下有多个链，必须要做区分，如`USDT`下有`USDT-ERC20`，`USDT-TRC20`多个链  
ctAddr | String | 合约地址  
canDep | Boolean | 当前是否可充值  
`false`：不可链上充值  
`true`：可以链上充值  
canWd | Boolean | 当前是否可提币  
`false`：不可链上提币  
`true`：可以链上提币  
canInternal | Boolean | 当前是否可内部转账  
`false`：不可内部转账  
`true`：可以内部转账  
depEstOpenTime | String | 充值预期开放时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
如果 `canDep` 为 `true`，则返回 `""`  
wdEstOpenTime | String | 提币预期开放时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
如果 `canWd` 为 `true`，则返回 `""`  
minDep | String | 币种单笔最小充值量  
minWd | String | 币种单笔最小`链上提币`量  
minInternal | String | 币种单笔最小`内部转账`量  
无单笔最大`内部转账`量限制，受24小时内提币额度(`wdQuota`)限制  
maxWd | String | 币种单笔最大`链上提币`量  
wdTickSz | String | 提币精度,表示小数点后的位数。提币手续费精度与提币精度保持一致。  
内部转账提币精度为小数点后8位。  
wdQuota | String | 过去24小时内提币额度（包含`链上提币`和`内部转账`），单位为`USD`  
usedWdQuota | String | 过去24小时内已用提币额度，单位为`USD`  
fee | String | 固定的提币手续费数量  
适用于`链上提币`  
minFee | String | ~~普通地址最小提币手续费数量  
适用于`链上提币`~~  
该字段已废弃  
maxFee | String | ~~普通地址最大提币手续费数量  
适用于`链上提币`~~  
该字段已废弃  
minFeeForCtAddr | String | ~~合约地址最小提币手续费数量  
适用于`链上提币`~~  
该字段已废弃  
maxFeeForCtAddr | String | ~~合约地址最大提币手续费数量  
适用于`链上提币`~~  
该字段已废弃  
burningFeeRate | String | 燃烧费率，如 `0.05` 代表 `5%`。  
部分币种会收取燃烧费用。燃烧费用按照提币数量（不含gas fee） 乘以 燃烧费率，在提币数量基础上扣除。  
适用于`链上提币`  
mainNet | Boolean | 当前链是否为主链  
needTag | Boolean | 当前链提币是否需要标签（tag/memo）信息，如 `EOS`该字段为`true`  
minDepArrivalConfirm | String | 充值到账最小网络确认数。币已到账但不可提。  
minWdUnlockConfirm | String | 提现解锁最小网络确认数  
depQuotaFixed | String | 充币固定限额，单位为`USD`  
没有充币限制则返回""  
usedDepQuotaFixed | String | 已用充币固定额度，单位为`USD`  
没有充币限制则返回""  
depQuoteDailyLayer2 | String | Layer2网络每日充值上限  
  
### 获取资金账户余额 

获取资金账户所有资产列表，查询各币种的余额、冻结和可用等信息。

只返回余额大于0的币资产信息。 

#### 限速：6次/s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/asset/balances`

> 请求示例
    
    
    GET /api/v5/asset/balances
    
    
    
    
    import okx.Funding as Funding
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    fundingAPI = Funding.FundingAPI(apikey, secretkey, passphrase, False, flag)
    
    # 获取资金账户余额
    result = fundingAPI.get_balances()
    print(result)
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
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
frozenBal | String | 冻结余额  
availBal | String | 可用余额  
  
### 获取不可交易资产 

获取当前用户 KYC 实体支持的不可交易资产列表。

#### 限速：6 次/s

#### 限速规则：User ID

#### 权限：读取

#### HTTP 请求

`GET /api/v5/asset/non-tradable-assets`

> 请求示例
    
    
    GET /api/v5/asset/non-tradable-assets
    
    
    
    
    import okx.Funding as Funding
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘: 0, 模拟盘: 1
    
    fundingAPI = Funding.FundingAPI(apikey, secretkey, passphrase, False, flag)
    
    result = fundingAPI.get_non_tradable_assets()
    print(result)
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 否 | 币种，如 `BTC`  
支持多币种查询（不超过20个），币种之间半角逗号分隔  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "bal": "989.84719571",
                "burningFeeRate": "",
                "canWd": true,
                "ccy": "CELT",
                "chain": "CELT-OKTC",
                "ctAddr": "f403fb",
                "fee": "2",
                "feeCcy": "USDT",
                "logoLink": "https://static.coinall.ltd/cdn/assets/imgs/221/460DA8A592400393.png",
                "minWd": "0.1",
                "name": "",
                "needTag": false,
                "wdAll": false,
                "wdTickSz": "8"
            },
            {
                "bal": "0.001",
                "burningFeeRate": "",
                "canWd": true,
                "ccy": "MEME",
                "chain": "MEME-ERC20",
                "ctAddr": "09b760",
                "fee": "5",
                "feeCcy": "USDT",
                "logoLink": "https://static.coinall.ltd/cdn/assets/imgs/207/2E664E470103C613.png",
                "minWd": "0.001",
                "name": "MEME Inu",
                "needTag": false,
                "wdAll": false,
                "wdTickSz": "8"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ccy | String | 币种名称，如 `CELT`  
name | String | 币种中文名称，不显示则无对应名称  
logoLink | String | 币种Logo链接  
bal | String | 可提余额  
canWd | Boolean | 是否可提  
`false`: 不可提 `true`: 可提  
chain | String | 支持提币的链  
minWd | String | 币种单笔最小提币量  
wdAll | Boolean | 该币种资产是否必须一次性全部提取  
fee | String | 提币固定手续费。提币手续费精度为小数点后8位。  
feeCcy | String | 提币固定手续费单位  
burningFeeRate | String | 燃烧费率，如 `0.05` 代表 `5%`。  
部分币种会收取燃烧费用。燃烧费用按照提币数量（不含gas fee） 乘以 燃烧费率，在提币数量基础上扣除。  
ctAddr | String | 合约地址后6位  
wdTickSz | String | 提币精度,表示小数点后的位数  
needTag | Boolean | 提币的链是否需要标签（tag/memo）信息  
  
### 获取账户资产估值 

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
  
### 资金划转 

调用时，API Key 需要有交易权限。

支持母账户的资金账户划转到交易账户，母账户到子账户的资金账户和交易账户划转。

子账户默认可转出至母账户，划转到同一母账户下的其他子账户，需要先调用 [设置子账户主动转出权限](/docs-v5/zh/#sub-account-rest-api-set-permission-of-transfer-out) 接口进行授权。

请求的成功或失败不一定反映实际的划转结果，建议通过调用"获取资金划转状态"接口来确认最终结果。 

#### 限速：2 次/s

#### 限速规则：User ID + Currency

#### 权限：交易

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
  
### 获取资金划转状态 

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
  
### 获取资金流水 

查询最近一个月内资金账户账单流水

#### 限速：6 次/s

#### 限速规则：User ID

#### 权限：读取

#### HTTP 请求

`GET /api/v5/asset/bills`

> 请求示例
    
    
    GET /api/v5/asset/bills
    
    GET /api/v5/asset/bills?type=1
    
    
    
    
    import okx.Funding as Funding
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    fundingAPI = Funding.FundingAPI(apikey, secretkey, passphrase, False, flag)
    
    # 获取资金流水
    result = fundingAPI.get_bills()
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 否 | 币种  
type | String | 否 | 账单类型  
`1`：充值  
`2`：提现  
`13`：撤销提现  
`20`：转出至子账户（主体是母账户）  
`21`：从子账户转入（主体是母账户）  
`22`：转出到母账户（主体是子账户）  
`23`：母账户转入（主体是子账户）  
`28`：领取  
`47`：系统冲正  
`48`：活动得到  
`49`：活动送出  
`68`：手续费返佣(通过返佣卡)  
`72`：收币  
`73`：送币  
`74`：送币退还  
`75`：[活期简单赚币] 申购  
`76`：[活期简单赚币] 赎回  
`77`：[Jumpstart] 派发  
`78`：[Jumpstart] 锁定  
`80`：[DEFI/锁仓挖矿] 产品申购  
`82`：[DEFI/锁仓挖矿] 产品赎回  
`83`：挖矿收益  
`84`：违约金  
`89`：存币收益  
`116`：法币创建订单  
`117`：法币完成订单  
`118`：法币取消订单  
`124`：[Jumpstart] 解锁  
`130`：从交易账户转入  
`131`：转出至交易账户  
`132`：[P2P] 客服冻结  
`133`：[P2P] 客服解冻  
`134`：[P2P] 客服转交  
`135`：跨链兑换  
`137`：[ETH质押] 申购  
`138`：[ETH质押] 兑换  
`139`：[ETH质押] 收益  
`146`：客户回馈  
`150`：节点返佣  
`151`：邀请奖励  
`152`：经纪商返佣  
`160`：双币赢申购  
`161`：双币赢回款  
`162`：双币赢收益  
`163`：双币赢退款  
`172`：[节点计划] 助力人返佣  
`173`：[节点计划] 手续费返现  
`174`：Jumpstart支付  
`175`：锁定质押物  
`176`：借款转入  
`177`：添加质押物  
`178`：减少质押物  
`179`：还款  
`180`：释放质押物  
`181`：偿还空投糖果  
`185`：[经纪商] 闪兑返佣  
`187`：[经纪商] 闪兑划转  
`189`：盲盒奖励  
`195`：不可交易资产提币  
`196`：不可交易资产提币撤销  
`197`：不可交易资产充值  
`198`：不可交易资产减少  
`199`：不可交易资产增加  
`200`：买入  
`202`：价格锁定申购  
`203`：价格锁定回款  
`204`：价格锁定收益  
`205`：价格锁定退款  
`207`：双币赢精简版申购  
`208`：双币赢精简版回款  
`209`：双币赢精简版收益  
`210`：双币赢精简版退款  
`212`：[活期借币] 多币种借贷锁定质押物  
`215`：[活期借币] 多币种借贷释放质押物  
`217`：[活期借币] 多币种借贷借款转入  
`218`：[活期借币] 多币种借贷还款  
`232`：[活期借币] 利息补贴转出  
`220`：已下架数字货币  
`221`：提币手续费支出  
`222`：提币手续费退款  
`223`：合约带单分润  
`225`：鲨鱼鳍申购  
`226`：鲨鱼鳍回款  
`227`：鲨鱼鳍收益  
`228`：鲨鱼鳍退款  
`229`：空投发放  
`232`：利息补贴入账  
`233`：经纪商佣金补偿  
`240`：雪球申購  
`241`：雪球回款  
`242`：雪球收益  
`243`：雪球交易失败  
`249`：海鸥申购  
`250`：海鸥回款  
`251`：海鸥收益  
`252`：海鸥退款  
`263`：策略分润  
`265`：信号收入  
`266`：现货带单分润  
`270`：DCD经纪商划转  
`271`：DCD经纪商返佣  
`272`：[闪兑] 买入数字货币/法币  
`273`：[闪兑] 卖出数字货币/法币  
`284`：[Custody] 转出交易子账户  
`285`：[Custody] 转入交易子账户  
`286`：[Custody] 转出托管资金账户  
`287`：[Custody] 转入托管资金账户  
`288`：[Custody] 托管资金入金  
`289`：[Custody] 托管资金出金  
`299`：推荐节点返佣  
`300`：手续费折扣返现  
`303`：雪球做市商转账  
~~`304`：[定期简单赚币] 订单提交~~  
~~`305`：[定期简单赚币] 订单赎回~~  
~~`306`：[定期简单赚币] 本金发放~~  
~~`307`：[定期简单赚币] 收益发放 (提前终止订单补偿) ~~  
~~`308`：[定期简单赚币] 收益发放~~  
~~`309`：[定期简单赚币] 补偿收益发放 (订单延期补偿)~~  
`311`：系统转入小额资产  
`313`：发送礼物  
`314`：收到礼物  
`315`：礼物退回  
`328`：[SOL质押] 流动性质押收益  
`329`：[SOL质押] 流动性质押申购  
`330`：[SOL质押] 流动性质押铸币  
`331`：[SOL质押] 流动性质押赎回  
`332`：[SOL质押] 流动性质押结算  
`333`：体验金收益  
`339`：[定期简单赚币] 订单提交  
`340`：[定期简单赚币] 订单失败退款  
`341`：[定期简单赚币] 订单赎回  
`342`：[定期简单赚币] 本金发放  
`343`：[定期简单赚币] 收益发放  
`344`：[定期简单赚币] 补偿收益发放  
`345`：[机构借贷] 本金还款  
`346`：[机构借贷] 利息还款  
`347`：[机构借贷] 逾期罚款  
`348`：[BTC质押] 申购  
`349`：[BTC质押] 赎回  
`350`：[BTC质押] 收益  
`351`：[机构借贷] 发放贷款  
`354`：策略奖励发放  
`361`：已关闭的子账户余额转入  
`372`：资产锁定  
`373`：解除资产锁定  
`400`：自动借币利息  
`408`：自动赚币（USDG赚币）利息  
`476`：云交易所转出  
`477`：云交易所转入  
thirdPartyType | String | 否 | 第三方托管类型。不填则默认为 `1`（向后兼容）。  
`1`：Copper  
`2`：Komainu  
`5`：SCB  
当母账户绑定多家托管商时，使用此参数可筛选指定托管商的账单。适用于账单类型 `284`–`289`。  
clientId | String | 否 | 转账或提币的客户自定义ID  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度要在1-32位之间。  
after | String | 否 | 查询在此之前的内容，值为时间戳，Unix 时间戳为毫秒数格式，如 `1597026383085`  
before | String | 否 | 查询在此之后的内容，值为时间戳，Unix 时间戳为毫秒数格式，如 `1597026383085`  
limit | String | 否 | 分页返回的结果集数量，最大为 100，不填默认返回 100 条  
  
> 返回结果
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
        {
          "billId": "12344",
          "ccy": "BTC",
          "clientId": "",
          "balChg": "2",
          "bal": "12",
          "type": "1",
          "ts": "1597026383085",
          "notes": ""
        }
      ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
billId | String | 账单 ID  
ccy | String | 账户余额币种  
clientId | String | 转账或提币的客户自定义ID  
balChg | String | 账户层面的余额变动数量  
bal | String | 账户层面的余额数量  
type | String | 账单类型  
notes | String | 备注  
ts | String | 账单创建时间，Unix 时间戳的毫秒数格式，如 `1597026383085`  
  
### 获取资金流水全历史 

查询资金账户的所有历史账单流水记录，可追溯至2021年2月1日。 

⚠️ **重要提示** ：数据每30秒更新一次。更新频率可能因数据量而异 - 请注意在高流量期间可能出现延迟。 

#### 限速：1 次/s

#### 限速规则：User ID

#### 权限：读取

#### HTTP 请求

`GET /api/v5/asset/bills-history`

> 请求示例
    
    
    GET /api/v5/asset/bills-history
    
    GET /api/v5/asset/bills-history?type=1
    
    
    
    
    import okx.Funding as Funding
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    fundingAPI = Funding.FundingAPI(apikey, secretkey, passphrase, False, flag)
    
    # 获取资金流水
    result = fundingAPI.get_bills_history()
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 否 | 币种  
type | String | 否 | 账单类型  
`1`：充值  
`2`：提现  
`13`：撤销提现  
`20`：转出至子账户（主体是母账户）  
`21`：从子账户转入（主体是母账户）  
`22`：转出到母账户（主体是子账户）  
`23`：母账户转入（主体是子账户）  
`28`：领取  
`47`：系统冲正  
`48`：活动得到  
`49`：活动送出  
`68`：手续费返佣(通过返佣卡)  
`72`：收币  
`73`：送币  
`74`：送币退还  
`75`：[活期简单赚币] 申购  
`76`：[活期简单赚币] 赎回  
`77`：[Jumpstart] 派发  
`78`：[Jumpstart] 锁定  
`80`：[DEFI/锁仓挖矿] 产品申购  
`82`：[DEFI/锁仓挖矿] 产品赎回  
`83`：挖矿收益  
`84`：违约金  
`89`：存币收益  
`116`：法币创建订单  
`117`：法币完成订单  
`118`：法币取消订单  
`124`：[Jumpstart] 解锁  
`130`：从交易账户转入  
`131`：转出至交易账户  
`132`：[P2P] 客服冻结  
`133`：[P2P] 客服解冻  
`134`：[P2P] 客服转交  
`135`：跨链兑换  
`137`：[ETH质押] 申购  
`138`：[ETH质押] 兑换  
`139`：[ETH质押] 收益  
`146`：客户回馈  
`150`：节点返佣  
`151`：邀请奖励  
`152`：经纪商返佣  
`160`：双币赢申购  
`161`：双币赢回款  
`162`：双币赢收益  
`163`：双币赢退款  
`172`：[节点计划] 助力人返佣  
`173`：[节点计划] 手续费返现  
`174`：Jumpstart支付  
`175`：锁定质押物  
`176`：借款转入  
`177`：添加质押物  
`178`：减少质押物  
`179`：还款  
`180`：释放质押物  
`181`：偿还空投糖果  
`185`：[经纪商] 闪兑返佣  
`187`：[经纪商] 闪兑划转  
`189`：盲盒奖励  
`195`：不可交易资产提币  
`196`：不可交易资产提币撤销  
`197`：不可交易资产充值  
`198`：不可交易资产减少  
`199`：不可交易资产增加  
`200`：买入  
`202`：价格锁定申购  
`203`：价格锁定回款  
`204`：价格锁定收益  
`205`：价格锁定退款  
`207`：双币赢精简版申购  
`208`：双币赢精简版回款  
`209`：双币赢精简版收益  
`210`：双币赢精简版退款  
`212`：[活期借币] 多币种借贷锁定质押物  
`215`：[活期借币] 多币种借贷释放质押物  
`217`：[活期借币] 多币种借贷借款转入  
`218`：[活期借币] 多币种借贷还款  
`232`：[活期借币] 利息补贴转出  
`220`：已下架数字货币  
`221`：提币手续费支出  
`222`：提币手续费退款  
`223`：合约带单分润  
`225`：鲨鱼鳍申购  
`226`：鲨鱼鳍回款  
`227`：鲨鱼鳍收益  
`228`：鲨鱼鳍退款  
`229`：空投发放  
`232`：利息补贴入账  
`233`：经纪商佣金补偿  
`240`：雪球申購  
`241`：雪球回款  
`242`：雪球收益  
`243`：雪球交易失败  
`249`：海鸥申购  
`250`：海鸥回款  
`251`：海鸥收益  
`252`：海鸥退款  
`263`：策略分润  
`265`：信号收入  
`266`：现货带单分润  
`270`：DCD经纪商划转  
`271`：DCD经纪商返佣  
`272`：[闪兑] 买入数字货币/法币  
`273`：[闪兑] 卖出数字货币/法币  
`284`：[Custody] 转出交易子账户  
`285`：[Custody] 转入交易子账户  
`286`：[Custody] 转出托管资金账户  
`287`：[Custody] 转入托管资金账户  
`288`：[Custody] 托管资金入金  
`289`：[Custody] 托管资金出金  
`299`：推荐节点返佣  
`300`：手续费折扣返现  
`303`：雪球做市商转账  
~~`304`：[定期简单赚币] 订单提交~~  
~~`305`：[定期简单赚币] 订单赎回~~  
~~`306`：[定期简单赚币] 本金发放~~  
~~`307`：[定期简单赚币] 收益发放 (提前终止订单补偿) ~~  
~~`308`：[定期简单赚币] 收益发放~~  
~~`309`：[定期简单赚币] 补偿收益发放 (订单延期补偿)~~  
`311`：系统转入小额资产  
`313`：发送礼物  
`314`：收到礼物  
`315`：礼物退回  
`328`：[SOL质押] 流动性质押收益  
`329`：[SOL质押] 流动性质押申购  
`330`：[SOL质押] 流动性质押铸币  
`331`：[SOL质押] 流动性质押赎回  
`332`：[SOL质押] 流动性质押结算  
`333`：体验金收益  
`339`：[定期简单赚币] 订单提交  
`340`：[定期简单赚币] 订单失败退款  
`341`：[定期简单赚币] 订单赎回  
`342`：[定期简单赚币] 本金发放  
`343`：[定期简单赚币] 收益发放  
`344`：[定期简单赚币] 补偿收益发放  
`345`：[机构借贷] 本金还款  
`346`：[机构借贷] 利息还款  
`347`：[机构借贷] 逾期罚款  
`348`：[BTC质押] 申购  
`349`：[BTC质押] 赎回  
`350`：[BTC质押] 收益  
`351`：[机构借贷] 发放贷款  
`354`：策略奖励发放  
`361`：已关闭的子账户余额转入  
`372`：资产锁定  
`373`：解除资产锁定  
`400`：自动借币利息  
`408`：自动赚币（USDG赚币）利息  
`476`：云交易所转出  
`477`：云交易所转入  
thirdPartyType | String | 否 | 第三方托管类型。不填则默认为 `1`（向后兼容）。  
`1`：Copper  
`2`：Komainu  
`5`：SCB  
当母账户绑定多家托管商时，使用此参数可筛选指定托管商的账单。适用于账单类型 `284`–`289`。  
clientId | String | 否 | 转账或提币的客户自定义ID  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度要在1-32位之间。  
after | String | 否 | 查询在此之前的内容，值为时间戳或账单记录ID，Unix 时间戳为毫秒数格式，如 `1597026383085`  
before | String | 否 | 查询在此之后的内容，值为时间戳，Unix 时间戳为毫秒数格式，如 `1597026383085`  
limit | String | 否 | 分页返回的结果集数量，最大为 100，不填默认返回 100 条  
pagingType | String | 否 | 分页类型  
`1`：按账单记录时间戳分页  
`2`：按账单记录ID分页  
默认值为`1`  
  
> 返回结果
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
        {
          "billId": "12344",
          "ccy": "BTC",
          "clientId": "",
          "balChg": "2",
          "bal": "12",
          "type": "1",
          "ts": "1597026383085",
          "notes": ""
        }
      ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
billId | String | 账单 ID  
ccy | String | 账户余额币种  
clientId | String | 转账或提币的客户自定义ID  
balChg | String | 账户层面的余额变动数量  
bal | String | 账户层面的余额数量  
type | String | 账单类型  
notes | String | 备注  
ts | String | 账单创建时间，Unix 时间戳的毫秒数格式，如 `1597026383085`  
  
### 获取充值地址信息 

获取各个币种的充值地址，包括曾使用过的老地址。

#### 限速：6次/s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/asset/deposit-address`

> 请求示例
    
    
    GET /api/v5/asset/deposit-address?ccy=BTC
    
    
    
    
    import okx.Funding as Funding
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    fundingAPI = Funding.FundingAPI(apikey, secretkey, passphrase, False, flag)
    
    # 获取充值地址信息
    result = fundingAPI.get_deposit_address(
        ccy="USDT"
    )
    print(result)
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 是 | 币种，如`BTC`  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "chain": "BTC-Bitcoin",
                "ctAddr": "",
                "ccy": "BTC",
                "to": "6",
                "addr": "39XNxK1Ryqgg3Bsyn6HzoqV4Xji25pNkv6",
                "verifiedName":"John Corner",
                "selected": true
            },
            {
                "chain": "BTC-OKC",
                "ctAddr": "",
                "ccy": "BTC",
                "to": "6",
                "addr": "0x66d0edc2e63b6b992381ee668fbcb01f20ae0428",
                "verifiedName":"John Corner",
                "selected": true
            },
            {
                "chain": "BTC-ERC20",
                "ctAddr": "5807cf",
                "ccy": "BTC",
                "to": "6",
                "addr": "0x66d0edc2e63b6b992381ee668fbcb01f20ae0428",
                "verifiedName":"John Corner",
                "selected": true
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
addr | String | 充值地址  
tag | String | 部分币种充值需要标签，若不需要则不返回此字段  
memo | String | 部分币种充值需要 memo，若不需要则不返回此字段  
pmtId | String | 部分币种充值需要此字段（payment_id），若不需要则不返回此字段  
addrEx | Object | 充值地址备注，部分币种充值需要，若不需要则不返回此字段  
如币种`TONCOIN`的充值地址备注标签名为`comment`,则该字段返回：{'comment':'123456'}  
ccy | String | 币种，如`BTC`  
chain | String | 币种链信息  
有的币种下有多个链，必须要做区分，如`USDT`下有`USDT-ERC20`，`USDT-TRC20`多个链  
to | String | 转入账户  
`6`：资金账户 `18`：交易账户  
某些主体用户(如巴西)只支持充值到交易账户  
verifiedName | String | (接受方)已验证姓名  
selected | Boolean | 该地址是否为页面选中的地址  
ctAddr | String | 合约地址后6位  
  
### 获取充值记录 

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

### 提币 

支持资金账户资产提币。普通子账户不支持提币。

API只能提币到免认证地址/账户上，通过 WEB/APP 可以设置免认证地址。  关于标签  
某些币种如XRP充币时同时需要一个充值地址和标签（又名memo/payment_id），标签是一种保证您的充币地址唯一性的数字串，与充币地址成对出现并一一对应。请您务必遵守正确的充值步骤，在提币时输入完整信息，否则将面临丢失币的风险！  
对于有标签的币种，如果是OKX用户间的提币，请走内部转账不要走链上提币。  下列内容仅适用于居住地为阿拉伯联合酋长国的用户  
根据您所在国家或地区的法律法规，一定比例的用户资产必须存储在冷钱包中。我们会不定期进行冷热钱包资产转移，但如果热钱包中的资产不足以满足用户提币需求，我们将需要进行额外步骤将冷钱包资产转移到热钱包，这可能会导致提币延迟最多24小时。  
更多详情参考(https://www.okx.com/zh-hans/help/what-is-a-segregated-wallet-and-why-is-my-withdrawal-delayed)  部分主体下的用户提币需要传入附加信息  
巴哈马主体参考： https://www.okx.com/docs-v5/log_en/#2024-08-08-withdrawal-api-adjustment-for-bahama-entity-users 

#### 限速：6次/s

#### 限速规则：User ID

#### 权限：提币

#### HTTP请求

`POST /api/v5/asset/withdrawal`

> 请求示例
    
    
    # 链上提币
    POST /api/v5/asset/withdrawal
    body
    {
        "amt":"1",
        "dest":"4",
        "ccy":"BTC",
        "chain":"BTC-Bitcoin",
        "toAddr":"17DKe3kkkkiiiiTvAKKi2vMPbm1Bz3CMKw"
    }
    
    # 内部转账
    POST /api/v5/asset/withdrawal
    body
    {
        "amt":"10",
        "dest":"3",
        "ccy":"USDT",
        "areaCode":"86",
        "toAddr":"15651000000"
    }
    
    # 特定主体用户需要提供接收方信息
    POST /api/v5/asset/withdrawal
    body
    {
        "amt":"1",
        "dest":"4",
        "ccy":"BTC",
        "chain":"BTC-Bitcoin",
        "toAddr":"17DKe3kkkkiiiiTvAKKi2vMPbm1Bz3CMKw",
        "rcvrInfo":{
            "walletType":"exchange",
            "exchId":"did:ethr:0xfeb4f99829a9acdf52979abee87e83addf22a7e1",
            "rcvrFirstName":"Bruce",
            "rcvrLastName":"Wayne"
        }
    }
    
    
    
    import okx.Funding as Funding
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    fundingAPI = Funding.FundingAPI(apikey, secretkey, passphrase, False, flag)
    
    # 提币
    result = fundingAPI.withdrawal(
        ccy="USDT",
        toAddr="TXtvfb7cdrn6VX9H49mgio8bUxZ3DGfvYF",
        amt="100",
        dest="4",
        chain="USDT-TRC20"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 是 | 币种，如 `USDT`  
amt | String | 是 | 提币数量  
该数量不包含手续费。提币时需预留足够的手续费。  
链上提币所需网络手续费可以通过接口 [获取币种列表](/docs-v5/zh/#funding-account-rest-api-get-currencies) 获取  
内部转账无需手续费  
dest | String | 是 | 提币方式  
`3`：内部转账   
`4`：链上提币  
toAddr | String | 是 | `toAddr`必须是认证过的地址/账户。如果选择链上提币，某些数字货币地址格式为`地址:标签`，如 `ARDOR-7JF3-8F2E-QUWZ-CAN7F:123456`  
如果选择内部转账，`toAddr`必须是接收方地址，可以是UID（仅白名单用户）、邮箱、手机或者账户名（只有子账户才有账户名）。  
toAddrType | String | 否 | 地址类型  
`1`: 钱包地址、邮箱、手机号、登录账户名  
`2`: UID（仅适用于 dest=`3`）  
chain | String | 可选 | 币种链信息  
如`USDT`下有`USDT-ERC20`，`USDT-TRC20`多个链  
如果不填此参数，则默认为主链  
对于无效资产提币，不填此参数，则默认为唯一的提币链  
适用于`链上提币`，链信息可以通过接口 [获取币种列表](/docs-v5/zh/#funding-account-rest-api-get-currencies) 获取  
areaCode | String | 可选 | 手机区号，如 `86`  
当`toAddr`为手机号时，该参数必填  
适用于`内部转账`  
rcvrInfo | Object | 可选 | 接收方信息  
特定主体用户做`链上提币`/`闪电网络提币` 需要提供此信息  
> walletType | String | 是 | 钱包类型  
`exchange`：提币到交易所钱包  
`private`：提币到私人钱包  
对于钱包接收方为公司的，`rcvrFirstName`可以填公司名称，`rcvrLastName`可以填"N/A"，地址信息可以填写公司注册地址。  
> exchId | String | 可选 | 交易所 ID  
可以通过 [获取交易所列表（公共）](/docs-v5/zh/#funding-account-rest-api-get-exchange-list-public) 接口查询支持的交易所  
如果交易所不在支持的交易所列表中，该字段填`0`  
适用于walletType=`exchange`  
> rcvrFirstName | String | 可选 | 接收方名字，如 `Bruce`  
> rcvrLastName | String | 可选 | 接收方姓氏，如 `Wayne`  
> rcvrCountry | String | 可选 | 接收方所在国家，如 `United States`  
必须输入英文国家名称，或者两字母国家代码(ISO 3166-1)。输入内容参考下方国家信息表中`国家名称(英)`，`国家代码`  
> rcvrCountrySubDivision | String | 可选 | 接收方所在州/省，如 `California`  
> rcvrTownName | String | 可选 | 接收方所在城镇，如 `San Jose`  
> rcvrStreetName | String | 可选 | 接收方所在街道地址，如 `Clementi Avenue 1`  
clientId | String | 否 | 客户自定义ID  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度要在1-32位之间。  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
            "amt": "0.1",
            "wdId": "67485",
            "ccy": "BTC",
            "clientId": "",
            "chain": "BTC-Bitcoin"
        }]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ccy | String | 提币币种  
chain | String | 币种链信息  
有的币种下有多个链，必须要做区分，如`USDT`下有`USDT-ERC20`，`USDT-TRC20`多个链  
amt | String | 提币数量  
wdId | String | 提币申请ID  
clientId | String | 客户自定义ID  
  
#### 国家信息表

国家名称(英) | 国家名称(中) | 国家代码  
---|---|---  
Afghanistan | 阿富汗 | AF  
Albania | 阿尔巴尼亚 | AL  
Algeria | 阿尔及利亚 | DZ  
Andorra | 安道尔 | AD  
Angola | 安哥拉 | AO  
Anguilla | 安圭拉 | AI  
Antigua and Barbuda | 安提瓜和巴布达 | AG  
Argentina | 阿根廷 | AR  
Armenia | 亚美尼亚 | AM  
Australia | 澳大利亚 | AU  
Austria | 奥地利 | AT  
Azerbaijan | 阿塞拜疆 | AZ  
Bahamas | 巴哈马 | BS  
Bahrain | 巴林 | BH  
Bangladesh | 孟加拉国 | BD  
Barbados | 巴巴多斯 | BB  
Belarus | 白俄罗斯 | BY  
Belgium | 比利时 | BE  
Belize | 伯利兹 | BZ  
Benin | 贝宁 | BJ  
Bermuda | 百慕大 | BM  
Bhutan | 不丹 | BT  
Bolivia | 玻利维亚 | BO  
Bosnia and Herzegovina | 波斯尼亚和黑塞哥维那 (波黑) | BA  
Botswana | 博茨瓦纳 | BW  
Brazil | 巴西 | BR  
British Virgin Islands | 英属维尔京群岛 | VG  
Brunei | 文莱 | BN  
Bulgaria | 保加利亚 | BG  
Burkina Faso | 布基纳法索 | BF  
Burundi | 布隆迪 | BI  
Cambodia | 柬埔寨 | KH  
Cameroon | 喀麦隆 | CM  
Canada | 加拿大 | CA  
Cape Verde | 佛得角 | CV  
Cayman Islands | 开曼群岛 | KY  
Central African Republic | 中非共和国 | CF  
Chad | 乍得 | TD  
Chile | 智利 | CL  
Colombia | 哥伦比亚 | CO  
Comoros | 科摩罗 | KM  
Congo (Republic) | 刚果共和国 | CG  
Congo (Democratic Republic) | 刚果民主共和国 | CD  
Costa Rica | 哥斯达黎加 | CR  
Cote d´Ivoire (Ivory Coast) | 象牙海岸 | CI  
Croatia | 克罗地亚 | HR  
Cuba | 古巴 | CU  
Cyprus | 塞浦路斯 | CY  
Czech Republic | 捷克共和国 | CZ  
Denmark | 丹麦 | DK  
Djibouti | 吉布提 | DJ  
Dominica | 多米尼克 | DM  
Dominican Republic | 多明尼加共和国 | DO  
Ecuador | 厄瓜多尔 | EC  
Egypt | 埃及 | EG  
El Salvador | 萨尔瓦多 | SV  
Equatorial Guinea | 赤道几内亚 | GQ  
Eritrea | 厄立特里亚 | ER  
Estonia | 爱沙尼亚 | EE  
Ethiopia | 埃塞俄比亚 | ET  
Fiji | 斐济 | FJ  
Finland | 芬兰 | FI  
France | 法国 | FR  
Gabon | 加蓬 | GA  
Gambia | 冈比亚 | GM  
Georgia | 格鲁吉亚 | GE  
Germany | 德国 | DE  
Ghana | 加纳 | GH  
Greece | 希腊 | GR  
Grenada | 格林纳达 | GD  
Guatemala | 危地马拉 | GT  
Guinea | 几内亚 | GN  
Guinea-Bissau | 几内亚比绍 | GW  
Guyana | 圭亚那 | GY  
Haiti | 海地 | HT  
Honduras | 洪都拉斯 | HN  
Hong Kong | 香港 | HK  
Hungary | 匈牙利 | HU  
Iceland | 冰岛 | IS  
India | 印度 | IN  
Indonesia | 印度尼西亚 | ID  
Iran | 伊朗 | IR  
Iraq | 伊拉克 | IQ  
Ireland | 爱尔兰 | IE  
Israel | 以色列 | IL  
Italy | 意大利 | IT  
Jamaica | 牙买加 | JM  
Japan | 日本 | JP  
Jordan | 约旦 | JO  
Kazakhstan | 哈萨克斯坦 | KZ  
Kenya | 肯尼亚 | KE  
Kiribati | 基里巴斯 | KI  
North Korea | 朝鲜 | KP  
South Korea | 韩国 | KR  
Kuwait | 科威特 | KW  
Kyrgyzstan | 吉尔吉斯斯坦 | KG  
Laos | 老挝 | LA  
Latvia | 拉脱维亚 | LV  
Lebanon | 黎巴嫩 | LB  
Lesotho | 莱索托 | LS  
Liberia | 利比里亚 | LR  
Libya | 利比亚 | LY  
Liechtenstein | 列支敦士登 | LI  
Lithuania | 立陶宛 | LT  
Luxembourg | 卢森堡 | LU  
Macau | 澳门 | MO  
Macedonia | 马其顿 | MK  
Madagascar | 马达加斯加 | MG  
Malawi | 马拉维 | MW  
Malaysia | 马来西亚 | MY  
Maldives | 马尔代夫 | MV  
Mali | 马里 | ML  
Malta | 马耳他 | MT  
Marshall Islands | 马绍尔群岛 | MH  
Mauritania | 毛里塔尼亚 | MR  
Mauritius | 毛里求斯 | MU  
Mexico | 墨西哥 | MX  
Micronesia | 密克罗尼西亚 | FM  
Moldova | 摩尔多瓦 | MD  
Monaco | 摩纳哥 | MC  
Mongolia | 蒙古 | MN  
Montenegro | 黑山 | ME  
Morocco | 摩洛哥 | MA  
Mozambique | 莫桑比克 | MZ  
Myanmar (Burma) | 缅甸 | MM  
Namibia | 纳米比亚 | NA  
Nauru | 瑙鲁 | NR  
Nepal | 尼泊尔 | NP  
Netherlands | 荷兰 | NL  
New Zealand | 新西兰 | NZ  
Nicaragua | 尼加拉瓜 | NI  
Niger | 尼日尔 | NE  
Nigeria | 尼日利亚 | NG  
Norway | 挪威 | NO  
Oman | 阿曼 | OM  
Pakistan | 巴基斯坦 | PK  
Palau | 帕劳 | PW  
Panama | 巴拿马 | PA  
Papua New Guinea | 巴布亚新几内亚 | PG  
Paraguay | 巴拉圭 | PY  
Peru | 秘鲁 | PE  
Philippines | 菲律宾 | PH  
Poland | 波兰 | PL  
Portugal | 葡萄牙 | PT  
Qatar | 卡塔尔 | QA  
Romania | 罗马尼亚 | RO  
Russia | 俄国 | RU  
Rwanda | 卢旺达 | RW  
Saint Kitts and Nevis | 圣基茨和尼维斯 | KN  
Saint Lucia | 圣卢西亚 | LC  
Saint Vincent and the Grenadines | 圣文森特和格林纳丁斯 | VC  
Samoa | 萨摩亚 | WS  
San Marino | 圣马力诺 | SM  
Sao Tome and Principe | 圣多美和普林西比 | ST  
Saudi Arabia | 沙特阿拉伯 | SA  
Senegal | 塞内加尔 | SN  
Serbia | 塞尔维亚 | RS  
Seychelles | 塞舌尔 | SC  
Sierra Leone | 塞拉利昂 | SL  
Singapore | 新加坡 | SG  
Slovakia | 斯洛伐克 | SK  
Slovenia | 斯洛文尼亚 | SI  
Solomon Islands | 所罗门群岛 | SB  
Somalia | 索马里 | SO  
South Africa | 南非 | ZA  
Spain | 西班牙 | ES  
Sri Lanka | 斯里兰卡 | LK  
Sudan | 苏丹 | SD  
Suriname | 苏里南 | SR  
Swaziland | 斯威士兰 | SZ  
Sweden | 瑞典 | SE  
Switzerland | 瑞士 | CH  
Syria | 叙利亚 | SY  
Taiwan | 台湾 | TW  
Tajikistan | 塔吉克斯坦 | TJ  
Tanzania | 坦桑尼亚 | TZ  
Thailand | 泰国 | TH  
Timor-Leste (East Timor) | 东帝汶 | TL  
Togo | 多哥 | TG  
Tonga | 汤加 | TO  
Trinidad and Tobago | 特里尼达和多巴哥 | TT  
Tunisia | 突尼斯 | TN  
Turkey | 土耳其 | TR  
Turkmenistan | 土库曼斯坦 | TM  
Tuvalu | 图瓦卢 | TV  
U.S. Virgin Islands | 美属维尔京群岛 | VI  
Uganda | 乌干达 | UG  
Ukraine | 乌克兰 | UA  
United Arab Emirates | 阿拉伯联合酋长国 | AE  
United Kingdom | 英国 | GB  
United States | 美国 | US  
Uruguay | 乌拉圭 | UY  
Uzbekistan | 乌兹别克斯坦 | UZ  
Vanuatu | 瓦努阿图 | VU  
Vatican City | 梵蒂冈城 | VA  
Venezuela | 委内瑞拉 | VE  
Vietnam | 越南 | VN  
Yemen | 也门 | YE  
Zambia | 赞比亚 | ZM  
Zimbabwe | 津巴布韦 | ZW  
Kosovo | 科索沃 | XK  
South Sudan | 南苏丹 | SS  
China | 中国 | CN  
Palestine | 巴勒斯坦 | PS  
Curacao | 库拉索 | CW  
Dominican Republic | 多明尼加共和国 | DO  
Dominican Republic | 多明尼加共和国 | DO  
Gibraltar | 英属直布罗陀 | GI  
New Caledonia | 新喀里多尼亚 | NC  
Cook Islands | 库克群岛 | CK  
Reunion | 留尼旺 | RE  
Guernsey | 根西岛 | GG  
Guadeloupe | 瓜德罗普 | GP  
Martinique | 马提尼克 | MQ  
French Polynesia | 法属波利尼西亚 | PF  
Faroe Islands | 法罗群岛 | FO  
Greenland | 格陵兰岛 | GL  
Jersey | 泽西岛 | JE  
Aruba | 阿鲁巴 | AW  
Puerto Rico | 波多黎各 | PR  
Isle of Man | 曼岛 | IM  
Guam | 关岛 | GU  
Sint Maarten | 荷属圣马丁 | SX  
Turks and Caicos | 特克斯和凯科斯群岛 | TC  
Åland Islands | 奥兰群岛 | AX  
Caribbean Netherlands | 荷属加勒比 | BQ  
British Indian Ocean Territory | 英属印度洋领地 | IO  
Christmas as Island | 圣诞岛 | CX  
Cocos (Keeling) Islands | 科科斯 (基林) 群岛 | CC  
Falkland Islands (Islas Malvinas) | 福克兰群岛 (马尔维纳斯群岛) | FK  
Mayotte | 马约特 | YT  
Niue | 纽埃 | NU  
Norfolk Island | 诺福克岛 | NF  
Northern Mariana Islands | 北马里亚纳群岛 | MP  
Pitcairn Islands | 皮特凯恩群岛 | PN  
Saint Helena, Ascension and Tristan da Cunha | 圣赫勒拿、阿森松岛和特里斯坦-达库尼亚 | SH  
Collectivity of Saint Martin | 法属圣马丁 | MF  
Saint Pierre and Miquelon | 圣皮埃尔和密克隆 | PM  
Tokelau | 托克劳 | TK  
Wallis and Futuna | 瓦利斯和富图纳 | WF  
American Samoa | 美属萨摩亚 | AS  
  
### 撤销提币 

可以撤销普通提币，但不支持撤销闪电网络上的提币。

#### 限速：6次/s

#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/asset/cancel-withdrawal`

> 请求示例
    
    
    POST /api/v5/asset/cancel-withdrawal
    body {
       "wdId":"1123456"
    }
    
    
    
    import okx.Funding as Funding
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    fundingAPI = Funding.FundingAPI(apikey, secretkey, passphrase, False, flag)
    
    # 撤销提币
    result = fundingAPI.cancel_withdrawal(
        wdId="123456"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
wdId | String | 是 | 提币申请ID  
  
> 返回结果
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
        {
          "wdId": "1123456"   
        }
      ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
wdId | String | 提币申请ID  
接口返回code等于0不能严格认为提币已经被撤销，只表示您的请求被系统服务器所接受，实际结果以获取提币记录中的状态为准。 

### 获取提币记录 

根据币种，提币状态，时间范围获取提币记录，按照时间倒序排列，默认返回100条数据。  
支持Websocket订阅，参考 [提币信息频道](/docs-v5/zh/#funding-account-websocket-withdrawal-info-channel)。

#### 限速：6 次/s

#### 限速规则：User ID

#### 权限：读取

#### HTTP 请求

`GET /api/v5/asset/withdrawal-history`

> 请求示例
    
    
    # 查询最近的提币记录
    GET /api/v5/asset/withdrawal-history
    
    # 查询从2022年06月01日到2022年07月01日之间的BTC的提币记录
    GET /api/v5/asset/withdrawal-history?ccy=BTC&after=1654041600000&before=1656633600000
    
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 否 | 币种名称，如 `BTC`  
wdId | String | 否 | 提币申请ID  
clientId | String | 否 | 客户自定义ID  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度要在1-32位之间。  
txId | String | 否 | 区块转账哈希记录  
type | String | 否 | 提币方式  
`3`：内部转账  
`4`：链上提币  
state | String | 否 | 提币状态  
  

* 阶段1：等待提币
`19`：热钱包余额不足  
`17`：钱包地址正等待国际转账规则认证  
`10`：等待划转  
`0`：等待提币  
`4`/`5`/`6`/`8`/`9`/`12`：等待客服审核  
`7`：审核通过  
>`0`, `17`, `19` 可撤销，其他状态不可撤销  
  

* 阶段2：提币处理中（适用于链上提币，内部转账无此阶段）
`1`：正在将您的交易广播到链上  
`15`：交易待确认  
`16`：根据当地法律法规，您的提币最多可能需要 24 小时才能到账  
`-3`：撤销中  
  

* 最终阶段
`-2`：已撤销  
`-1`：失败  
`2`：提币成功  
after | String | 否 | 查询在此之前的内容，值为时间戳，Unix 时间戳为毫秒数格式，如 `1654041600000`  
before | String | 否 | 查询在此之后的内容，值为时间戳，Unix 时间戳为毫秒数格式，如 `1656633600000`  
limit | string | 否 | 返回的结果集数量，默认为100，最大为100，不填默认返回100条  
  
> 返回结果
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
        {
          "note": "",
          "chain": "ETH-Ethereum",
          "fee": "0.007",
          "feeCcy": "ETH",
          "ccy": "ETH",
          "clientId": "",
          "toAddrType": "1",
          "amt": "0.029809",
          "txId": "0x35c******b360a174d",
          "from": "156****359",
          "areaCodeFrom": "86",
          "to": "0xa30d1fab********7CF18C7B6C579",
          "areaCodeTo": "",
          "state": "2",
          "ts": "1655251200000",
          "nonTradableAsset": false,
          "wdId": "15447421"
        }
      ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ccy | String | 币种  
chain | String | 币种链信息  
有的币种下有多个链，必须要做区分，如`USDT`下有`USDT-ERC20`，`USDT-TRC20`多个链  
nonTradableAsset | Boolean | 是否为不可交易资产  
`true`：不可交易资产，`false`：可交易资产  
amt | String | 数量  
ts | String | 提币申请时间，Unix 时间戳的毫秒数格式，如 `1655251200000`  
from | String | 提币账户  
可以是`邮箱`/`手机号`/`子账户名`  
areaCodeFrom | String | 如果`from`为手机号，该字段为该手机号的区号  
to | String | 收币地址  
areaCodeTo | String | 如果`to`为手机号，该字段为该手机号的区号  
toAddrType | String | 地址类型  
`1`: 钱包地址、邮箱、手机号、登录账户名  
`2`: UID  
tag | String | 部分币种提币需要标签，若不需要则不返回此字段  
pmtId | String | 部分币种提币需要此字段（payment_id），若不需要则不返回此字段  
memo | String | 部分币种提币需要此字段，若不需要则不返回此字段  
addrEx | Object | 提币地址备注，部分币种提币需要，若不需要则不返回此字段。如币种TONCOIN的提币地址备注标签名为comment,则该字段返回：{'comment':'123456'}  
txId | String | 提币哈希记录  
内部转账该字段返回""  
fee | String | 提币手续费数量  
feeCcy | String | 提币手续费币种，如 `USDT`  
state | String | 提币状态  
wdId | String | 提币申请ID  
clientId | String | 客户自定义ID  
note | String | 备注信息  
  
### 获取充值/提现的详细状态

获取充值与提现的详细状态信息与预估完成时间。

#### 限速：1次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/asset/deposit-withdraw-status`

> 请求示例
    
    
    # 查询充值
    GET /api/v5/asset/deposit-withdraw-status?txId=xxxxxx&to=1672734730284&ccy=USDT&chain=USDT-ERC20
    
    # 查询提现
    GET /api/v5/asset/deposit-withdraw-status?wdId=200045249
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
wdId | String | 可选 | 提币申请ID，用于查询资金提现  
`wdId`与`txId`必传其一也仅可传其一  
txId | String | 可选 | 区块转账哈希记录ID，用于查询资金充值  
`wdId`与`txId`必传其一也仅可传其一  
ccy | String | 可选 | 币种，如`USDT`  
查询充值时必填，需要与`txId`一并提供  
to | String | 可选 | 资金充值到账账户地址   
查询充值时必填，需要与`txId`一并提供  
chain | String | 可选 | 币种链信息，如 USDT-ERC20   
查询充值时必填，需要与`txId`一并提供  
  
> 返回结果
    
    
    {
        "code":"0",
        "data":[
            {
                "wdId": "200045249",
                "txId": "16f3638329xxxxxx42d988f97", 
                "state": "Pending withdrawal: Wallet is under maintenance, please wait.",
                "estCompleteTime": "01/09/2023, 8:10:48 PM"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
estCompleteTime | String | 预估完成时间  
时区为 UTC+8；格式为 MM/dd/yyyy, h:mm:ss AM/PM   
estCompleteTime仅为预估完成时间，仅供参考  
state | String | 充值/提现的现处于的详细阶段提示  
冒号前面代表阶段，后面代表状态  
txId | String | 区块转账哈希记录  
提币如果`txId`已经生成，则返回，否则返回""  
wdId | String | 提币申请ID  
如查询的是充值，该字段返回""  
阶段参考  
充值  
阶段一：监测链上交易  
阶段二：推送充值数据到入账环节  
阶段三：进行入账  
终态：充值已完成  
提现  
阶段一：等待提现  
阶段二：提现中  
终态：提现已完成 / 撤销已完成  

### 获取交易所列表（公共）

公共接口无须鉴权

#### 限速：6次/s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/asset/exchange-list`

> 请求示例
    
    
    GET /api/v5/asset/exchange-list
    
    
    
    

#### 请求参数

无

> 返回结果
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
        {
            "exchId": "did:ethr:0xfeb4f99829a9acdf52979abee87e83addf22a7e1",
            "exchName": "1xbet"
        }
      ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
exchName | String | 交易所名称，如 `1xbet`  
exchId | String | 交易所 ID，如 `did:ethr:0xfeb4f99829a9acdf52979abee87e83addf22a7e1`  
  
### 申请月结单 (近一年)

申请最近一年的月结单。

#### 限速：20 次/月

#### 限速规则：User ID

#### 权限：读取

#### HTTP Request

`POST /api/v5/asset/monthly-statement`

> 请求示例
    
    
    POST /api/v5/asset/monthly-statement
    body
    {
        "month":"Jan"
    }
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
month | String | 否 | 月份,默认上一个月。有效值是`Jan`, `Feb`, `Mar`, `Apr`,`May`, `Jun`, `Jul`,`Aug`, `Sep`,`Oct`,`Nov`,`Dec`  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "ts": "1646892328000"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ts | String | 下载链接生成时间，Unix时间戳的毫秒数格式 ，如, `1597026383085`  
  
### 获取月结单 (近一年)

获取近一年的月结单

#### 限速：10 次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP Request

`GET /api/v5/asset/monthly-statement`

> 请求示例
    
    
    GET /api/v5/asset/monthly-statement?month=Jan
    
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
month | String | 是 | 月份, 有效值是`Jan`, `Feb`, `Mar`, `Apr`,`May`, `Jun`, `Jul`,`Aug`, `Sep`, `Oct`, `Nov`, `Dec`  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "fileHref": "http://xxx",
                "state": "finished",
                "ts": 1646892328000
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
fileHref | String | 文件链接  
ts | Int | 下载链接生成时间，Unix时间戳的毫秒数格式 ，如 1597026383085  
state | String | 下载链接状态   
`finished`：已生成  
`ongoing`：进行中  
  
### 获取闪兑币种列表 

#### 限速：6次/s

#### 限速规则：User ID

#### 权限：读取

#### HTTP 请求

`GET /api/v5/asset/convert/currencies`

> 请求示例
    
    
    GET /api/v5/asset/convert/currencies
    
    

#### 请求参数

无

> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "min": "",  // 已废弃
                "max": "",  // 已废弃
                "ccy": "BTC"
            },
            {
                "min": "",
                "max": "",
                "ccy": "ETH"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ccy | String | 币种名称，如 `BTC`  
min | String | ~~支持闪兑的最小值~~(已废弃)  
max | String | ~~支持闪兑的最大值~~(已废弃)  
  
### 获取闪兑币对信息 

#### 限速：6次/s

#### 限速规则：User ID

#### 权限：读取

#### HTTP 请求

`GET /api/v5/asset/convert/currency-pair`

> 请求示例
    
    
    GET /api/v5/asset/convert/currency-pair?fromCcy=USDT&toCcy=BTC
    
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
fromCcy | String | 是 | 消耗币种，如 `USDT`  
toCcy | String | 是 | 获取币种，如 `BTC`  
convertMode | String | 否 | `0`：标准闪兑（默认）  
`1`：VIP大额闪兑  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "baseCcy": "BTC",
                "baseCcyMax": "0.5",
                "baseCcyMin": "0.0001",
                "instId": "BTC-USDT",
                "quoteCcy": "USDT",
                "quoteCcyMax": "10000",
                "quoteCcyMin": "1"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
instId | String | 币对，如 `BTC-USDT`  
baseCcy | String | 交易货币币种，如 `BTC-USDT`中的`BTC`  
baseCcyMax | String | 交易货币支持闪兑的最大值  
baseCcyMin | String | 交易货币支持闪兑的最小值  
quoteCcy | String | 计价货币币种，如 `BTC-USDT`中的`USDT`  
quoteCcyMax | String | 计价货币支持闪兑的最大值  
quoteCcyMin | String | 计价货币支持闪兑的最小值  
  
### 闪兑预估询价 

#### 限速：10次/s

#### 限速规则：User ID

#### 限速：1次/5s

#### 限速规则：Instrument ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/asset/convert/estimate-quote`

> 请求示例
    
    
    POST /api/v5/asset/convert/estimate-quote
    body
    {
        "baseCcy": "ETH",
        "quoteCcy": "USDT",
        "side": "buy",
        "rfqSz": "30",
        "rfqSzCcy": "USDT"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
baseCcy | String | 是 | 交易货币币种，如 `BTC-USDT`中的`BTC`  
quoteCcy | String | 是 | 计价货币币种，如 `BTC-USDT`中的`USDT`  
side | String | 是 | 交易方向  
买：`buy` 卖：`sell`  
描述的是对于baseCcy的交易方向  
rfqSz | String | 是 | 询价数量  
rfqSzCcy | String | 是 | 询价币种  
clQReqId | String | 否 | 客户端自定义的订单标识  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度要在1-32位之间。  
tag | String | 否 | 订单标签  
适用于broker用户  
convertMode | String | 否 | `0`：标准闪兑（默认）  
`1`：VIP大额闪兑  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "baseCcy": "ETH",
                "baseSz": "0.01023052",
                "clQReqId": "",
                "cnvtPx": "2932.40104429",
                "origRfqSz": "30",
                "quoteCcy": "USDT",
                "quoteId": "quoterETH-USDT16461885104612381",
                "quoteSz": "30",
                "quoteTime": "1646188510461",
                "rfqSz": "30",
                "rfqSzCcy": "USDT",
                "side": "buy",
                "ttlMs": "10000"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
quoteTime | String | 生成报价时间，Unix时间戳的毫秒数格式  
ttlMs | String | 报价有效期，单位为毫秒  
clQReqId | String | 客户端自定义的订单标识  
quoteId | String | 报价ID  
baseCcy | String | 交易货币币种，如 BTC-USDT 中BTC  
quoteCcy | String | 计价货币币种，如 BTC-USDT 中USDT  
side | String | 交易方向  
买：`buy` 卖：`sell`  
origRfqSz | String | 原始报价的数量  
rfqSz | String | 实际报价的数量  
rfqSzCcy | String | 报价的币种  
cnvtPx | String | 闪兑价格，单位为计价币  
baseSz | String | 闪兑交易币数量  
quoteSz | String | 闪兑计价币数量  
  
### 闪兑交易 

闪兑交易前需要先 [询价](/docs-v5/zh/#funding-account-rest-api-estimate-quote)。

闪兑只能使用交易账户中的资产 

#### 限速：10次/s

#### 限速规则：User ID

#### 权限：交易

同一方向(buy/sell) 1次/5s 交易限制

#### HTTP请求

`POST /api/v5/asset/convert/trade`

> 请求示例
    
    
    POST /api/v5/asset/convert/trade
    body
    {
        "baseCcy": "ETH",
        "quoteCcy": "USDT",
        "side": "buy",
        "sz": "30",
        "szCcy": "USDT",
        "quoteId": "quoterETH-USDT16461885104612381"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
quoteId | String | 是 | 报价ID  
baseCcy | String | 是 | 交易货币币种，如 `BTC-USDT`中的`BTC`  
quoteCcy | String | 是 | 计价货币币种，如 `BTC-USDT`中的`USDT`  
side | String | 是 | 交易方向  
`buy`：买  
`sell`：卖  
描述的是对于`baseCcy`的交易方向  
sz | String | 是 | 用户报价数量  
报价数量应不大于预估询价中的询价数量  
szCcy | String | 是 | 用户报价币种  
clTReqId | String | 否 | 用户自定义的订单标识  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度要在1-32位之间。  
tag | String | 否 | 订单标签  
适用于broker用户  
convertMode | String | 否 | `0`：标准闪兑（默认）  
`1`：VIP大额闪兑  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "baseCcy": "ETH",
                "clTReqId": "",
                "fillBaseSz": "0.01023052",
                "fillPx": "2932.40104429",
                "fillQuoteSz": "30",
                "instId": "ETH-USDT",
                "quoteCcy": "USDT",
                "quoteId": "quoterETH-USDT16461885104612381",
                "side": "buy",
                "state": "fullyFilled",
                "tradeId": "trader16461885203381437",
                "ts": "1646188520338"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
tradeId | String | 成交ID  
quoteId | String | 报价ID  
clTReqId | String | 用户自定义的订单标识  
state | String | 状态  
`fullyFilled`：交易成功  
`rejected`：交易失败  
instId | String | 币对，如 `BTC-USDT`  
baseCcy | String | 交易货币币种，如 `BTC-USDT`中`BTC`  
quoteCcy | String | 计价货币币种，如 `BTC-USDT`中`USDT`  
side | String | 交易方向  
买：`buy` 卖：`sell`  
fillPx | String | 成交价格，单位为计价币  
fillBaseSz | String | 成交的交易币数量  
fillQuoteSz | String | 成交的计价币数量  
ts | String | 闪兑交易时间，值为时间戳，Unix时间戳为毫秒数格式，如 `1597026383085`  
  
### 获取闪兑交易历史 

#### 限速：6次/s

#### 限速规则：User ID

#### 权限：读取

#### HTTP 请求

`GET /api/v5/asset/convert/history`

> 请求示例
    
    
    GET /api/v5/asset/convert/history
    
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
clTReqId | String | 否 | 用户自定义的订单标识  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度要在1-32位之间。  
after | String | 否 | 查询在此之前的内容，值为时间戳，Unix时间戳为毫秒数格式，如 `1597026383085`  
before | String | 否 | 查询在此之后的内容，值为时间戳，Unix时间戳为毫秒数格式，如 `1597026383085`  
limit | String | 否 | 返回的结果集数量，默认为100，最大为100  
tag | String | 否 | 订单标签  
适用于broker用户  
如果闪兑交易带上了`tag`,查询时必须也带上此参数  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "clTReqId": "",
                "instId": "ETH-USDT",
                "side": "buy",
                "fillPx": "2932.401044",
                "baseCcy": "ETH",
                "quoteCcy": "USDT",
                "fillBaseSz": "0.01023052",
                "state": "fullyFilled",
                "tradeId": "trader16461885203381437",
                "fillQuoteSz": "30",
                "ts": "1646188520000"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
tradeId | String | 成交ID  
clTReqId | String | 用户自定义的订单标识  
state | String | `fullyFilled`：交易成功  
`rejected`：交易失败  
instId | String | 币对，如 `BTC-USDT`  
baseCcy | String | 交易货币币种，如 `BTC-USDT`中的`BTC`  
quoteCcy | String | 计价货币币种，如 `BTC-USDT`中的`USDT`  
side | String | 交易方向  
买：`buy` 卖：`sell`  
fillPx | String | 成交价格，单位为计价币  
fillBaseSz | String | 成交的交易币数量  
fillQuoteSz | String | 成交的计价币数量  
ts | String | 闪兑交易时间，值为时间戳，Unix时间戳为毫秒数格式，如 `1597026383085`  
  
### 获取买卖交易币种 

#### 限速：6次/s

#### 限速规则：User ID

#### 权限：读取

#### HTTP 请求

`GET /api/v5/fiat/buy-sell/currencies`

> 请求示例
    
    
    GET /api/v5/fiat/buy-sell/currencies
    

> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
               "fiatCcyList":[
                    {
                        "ccy": "USD"
                    },
                    {
                        "ccy": "EUR"
                    },
                    ...
                ],
                "cryptoCcyList":[
                    {
                        "ccy": "BTC"
                    },
                    ...
                ],
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
fiatCcyList | Array of objects | 法币列表  
>ccy | String | 币种，如 `BTC`  
cryptoCcyList | Array of objects | 加密货币列表  
>ccy | String | 币种，如 `USD`  
此功能目前仅对巴哈马机构用户开放。 

### 获取买卖交易币对 

#### 限速：6次/s

#### 限速规则：User ID

#### 权限：读取

#### HTTP 请求

`GET /api/v5/fiat/buy-sell/currency-pair`

> 请求示例
    
    
    GET /api/v5/fiat/buy-sell/currency-pair?fromCcy=USD&toCcy=BTC
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
fromCcy | String | 是 | 卖出币种，如 `USD`  
toCcy | String | 是 | 买入币种，如 `BTC`  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "side": "buy",
                "fromCcy": "USD",
                "toCcy": "BTC",
                "singleTradeMax": "1",
                "singleTradeMin": "0.01",
                "fixedPxRemainingDailyQuota": "", 
                "fixedPxDailyLimit": "", 
                "paymentMethods":["balance"]
            }
        ],
        "msg": ""
    }
    
    {
        "code": "0",
        "data": [
            {
                "side": "sell",
                "fromCcy": "BTC",
                "toCcy": "USD",
                "singleTradeMax": "1",
                "singleTradeMin": "0.01",
                "fixedPxRemainingDailyQuota": "", 
                "fixedPxDailyLimit": "", 
                "paymentMethods":["balance"]
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
side | String | 交易方向  
`buy`: 使用法币购买加密货币/法币  
`sell`: 将加密货币出售为加密货币/法币  
未来可能同时支持双向交易，以逗号分隔，如 `buy,sell`  
fromCcy | String | 卖出币种，如 `USD`  
toCcy | String | 买入币种，如 `BTC`  
singleTradeMax | String | 单笔交易最大数量，单位为 `fromCcy`  
singleTradeMin | String | 单笔交易最小数量，单位为 `fromCcy`  
fixedPxDailyLimit | String | 固定价格每日限额  
仅适用于法币间交易，否则返回空字符串  
当`side` = `buy`时，单位为 `fromCcy`  
当`side` = `sell`时，单位为 `toCcy`  
fixedPxRemainingDailyQuota | String | 固定价格剩余每日限额  
仅适用于法币间交易，否则返回空字符串  
当`side` = `buy`时，单位为 `fromCcy`  
当`side` = `sell`时，单位为 `toCcy`  
paymentMethods | Array of strings | 支持的支付方式  
`balance`  
例如：["balance"]  
此功能目前仅对巴哈马机构用户开放。 

### 获取买卖交易报价 

#### 限速：10次/s

#### 限速规则：User ID

#### 限速：1次/5s

#### 限速规则：Instrument ID

#### 权限：读取

#### HTTP 请求

`POST /api/v5/fiat/buy-sell/quote`

> 请求示例
    
    
    # 卖出USD买入0.1 BTC
    POST /api/v5/fiat/buy-sell/quote
    body
    {
        "side":"buy",
        "fromCcy": "USD",
        "toCcy": "BTC",
        "rfqAmt": "0.1",
        "rfqCcy": "BTC"
    }
    
    # 卖出30 USD买入BTC
    POST /api/v5/fiat/buy-sell/quote
    body
    {
        "side":"buy",
        "fromCcy": "USD",
        "toCcy": "BTC",
        "rfqAmt": "30",
        "rfqCcy": "USD"
    }
    
    # 卖出BTC买入30 USD
    POST /api/v5/fiat/buy-sell/quote
    body
    {
        "side":"sell",
        "fromCcy": "BTC",
        "toCcy": "USD",
        "rfqAmt": "30",
        "rfqCcy": "USD"
    }
    
    # 卖出0.1 BTC买入USD
    POST /api/v5/fiat/buy-sell/quote
    body
    {
        "side":"sell",
        "fromCcy": "BTC",
        "toCcy": "USD",
        "rfqAmt": "0.1",
        "rfqCcy": "BTC"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
side | String | 是 | 交易方向  
`buy`: 法币买入加密货币  
`sell`: 加密货币卖出法币  
fromCcy | String | 是 | 卖出币种  
toCcy | String | 是 | 买入币种  
rfqAmt | String | 是 | 询价数量  
rfqCcy | String | 是 | 询价币种  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "quoteId": "quoterBTC-USD16461885104612381",
                "fromCcy": "USD",
                "toCcy": "BTC",
                "rfqAmt": "30",
                "rfqCcy": "USD",
                "quotePx": "2932.40104429",
                "quoteCcy": "USD",
                "quoteFromAmt": "30",
                "quoteToAmt": "30",
                "quoteTime": "1646188510461",
                "ttlMs": "10000"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
quoteId | String | 报价ID  
side | String | 交易方向  
`buy`: 使用法币购买加密货币/法币  
`sell`: 将加密货币出售为加密货币/法币  
fromCcy | String | 卖出币种，如 `USD`  
toCcy | String | 买入币种，如 `BTC`  
rfqAmt | String | 询价数量  
rfqCcy | String | 询价币种  
quotePx | String | 报价价格  
quoteCcy | String | 报价价格单位  
如 `USD`  
quoteFromAmt | String | 报价数量，单位为 `fromCcy`  
quoteToAmt | String | 报价数量，单位为 `toCcy`  
quoteTime | String | 报价生成时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
ttlMs | String | 报价有效期，单位为毫秒  
如 `10000` 表示报价仅10秒内有效  
此功能目前仅对巴哈马机构用户开放。 

### 买卖交易 

#### 限速：1次/5s

#### 限速规则：User ID

#### 权限：交易

#### HTTP 请求

`POST /api/v5/fiat/buy-sell/trade`

> 请求示例
    
    
    # 卖出30 USD买入BTC
    POST /api/v5/fiat/buy-sell/trade
    body
    {
        "clOrdId":"123456",
        "side":"sell",
        "fromCcy": "USD",
        "toCcy": "BTC",
        "rfqAmt": "30",
        "rfqCcy": "USD",
        "paymentMethod":"balance",
        "quoteId": "quoterETH-USDT16461885104612381"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
quoteId | String | 是 | 报价ID  
从获取买卖交易报价API获取  
side | String | 是 | 交易方向  
`buy`: 使用法币购买加密货币/法币  
`sell`: 将加密货币出售为加密货币/法币  
必须与报价请求一致  
fromCcy | String | 是 | 卖出币种  
必须与报价请求一致  
toCcy | String | 是 | 买入币种  
必须与报价请求一致  
rfqAmt | String | 是 | 询价数量  
必须与报价请求一致  
rfqCcy | String | 是 | 询价币种  
必须与报价请求一致  
paymentMethod | String | 是 | 支付方式  
`balance`  
clOrdId | String | 是 | 用户自定义的订单标识  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度要在1-32位之间  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "ordId": "1234",
                "clOrdId": "",
                "quoteId": "quoterBTC-USD16461885104612381",
                "side":"buy",
                "fromCcy": "USD",
                "toCcy": "BTC",
                "rfqAmt": "30",
                "rfqCcy": "USD",
                "fillPx": "2932.40104429",
                "fillQuoteCcy": "USD",
                "fillFromAmt": "30",
                "fillToAmt": "0.01",
                "cTime": "1646188510461"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ordId | String | 订单ID  
clOrdId | String | 用户自定义的订单标识  
quoteId | String | 报价ID  
state | String | 交易状态  
`processing`：处理中  
`completed`：已完成  
`failed`：失败  
side | String | 交易方向  
`buy`: 使用法币购买加密货币/法币  
`sell`: 将加密货币出售为加密货币/法币  
fromCcy | String | 卖出币种  
toCcy | String | 买入币种  
rfqAmt | String | 询价数量  
rfqCcy | String | 询价币种  
fillPx | String | 成交价格，单位为报价币种  
fillQuoteCcy | String | 成交价格报价币种  
如 `USD`  
fillFromAmt | String | 卖出数量，单位为 `fromCcy`  
fillToAmt | String | 买入数量，单位为 `toCcy`  
cTime | String | 请求时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
此功能目前仅对巴哈马机构用户开放。 

### 获取买卖交易历史 

#### 限速：6次/s

#### 限速规则：User ID

#### 权限：读取

#### HTTP 请求

`GET /api/v5/fiat/buy-sell/history`

> 请求示例
    
    
    GET /api/v5/fiat/buy-sell/history
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
ordId | String | 否 | 订单ID  
clOrdId | String | 否 | 用户自定义的订单标识  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度要在1-32位之间  
state | String | 否 | 交易状态  
`processing`：处理中  
`completed`：已完成  
`failed`：失败  
begin | String | 否 | 开始时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
end | String | 否 | 结束时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
limit | String | 否 | 返回的结果集数量，默认为100，最大为100  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "ordId": "1234",
                "clOrdId": "",
                "quoteId": "quoterBTC-USD16461885104612381",
                "state":"completed",
                "side":"buy",
                "fromCcy": "USD",
                "toCcy": "BTC",
                "rfqAmt": "30",
                "rfqCcy": "USD",
                "fillPx": "2932.40104429",
                "fillQuoteCcy": "USD",
                "fillFromAmt": "30",
                "fillToAmt": "0.01",
                "cTime": "1646188510461",
                "uTime": "1646188510461"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ordId | String | 订单ID  
clOrdId | String | 用户自定义的订单标识  
quoteId | String | 报价ID  
state | String | 交易状态  
`processing`：处理中  
`completed`：已完成  
`failed`：失败  
fromCcy | String | 卖出币种  
toCcy | String | 买入币种  
rfqAmt | String | 询价数量  
rfqCcy | String | 询价币种  
fillPx | String | 成交价格，单位为报价币种  
fillQuoteCcy | String | 成交价格报价币种  
如 `USD`  
fillFromAmt | String | 成交数量，单位为 `fromCcy`  
fillToAmt | String | 成交数量，单位为 `toCcy`  
cTime | String | 请求时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
uTime | String | 更新时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
此功能目前仅对巴哈马机构用户开放。 

## WebSocket 

### 充值信息频道 

当发起充值或者充值状态发生变化时会触发消息推送。  
支持母账户或者子账户的订阅   

  * 如果是母账户订阅，可以同时接受母账户与子账户的充值信息的推送  

  * 如果是子账户订阅，则仅支持子账户充值信息的推送  

#### 服务地址

/ws/v5/business (需要登录)

> 请求示例
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [
            {
                "channel": "deposit-info"
            }
        ]
    }
    
    
    
    import asyncio
    from okx.websocket.WsPrivateAsync import WsPrivateAsync
    
    def callbackFunc(message):
        print(message)
    
    async def main():
        ws = WsPrivateAsync(
            apiKey = "YOUR_API_KEY",
            passphrase = "YOUR_PASSPHRASE",
            secretKey = "YOUR_SECRET_KEY",
            url = "wss://ws.okx.com:8443/ws/v5/business",
            useServerTime=False
        )
        await ws.start()
        args = [
            {
                "channel": "deposit-info"
            }
        ]
        await ws.subscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
        await ws.unsubscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
    
    asyncio.run(main())
    
    

#### 请求参数

参数名 | 类型 | 是否必填 | 描述  
---|---|---|---  
id | String | 否 | 消息的唯一标识。  
用户提供，返回参数中会返回以便于找到相应的请求。  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度必须要在1-32位之间。  
op | String | 是 | 操作  
`subscribe`  
`unsubscribe`  
  
args | Array of objects | 是 | 请求订阅的频道列表  
> channel | String | 是 | 频道名  
`deposit-info`  
> ccy | String | 否 | 币种名称，如 `BTC`  
  
> 成功返回示例
    
    
    {
        "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "deposit-info"
        },
        "connId": "a4d3ae55"
    }
    

> 失败返回示例
    
    
    {
        "id": "1512",
        "event": "error",
        "code": "60012",
        "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"deposit-info\""}]}",
        "connId": "a4d3ae55"
    }
    

#### 返回参数

参数名 | 类型 | 是否必填 | 描述  
---|---|---|---  
id | String | 否 | 消息的唯一标识  
event | String | 是 | 操作  
`subscribe`  
`unsubscribe`  
`error`  
arg | Object | 否 | 订阅的频道  
> channel | String | 是 | 频道名  
`deposit-info`  
> ccy | String | 否 | 币种名称，如 `BTC`  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID  
  
> 推送示例
    
    
    {
        "arg": {
            "channel": "deposit-info",
            "uid": "289320****60975104"
        },
        "data": [{
            "actualDepBlkConfirm": "0",
            "amt": "1",
            "areaCodeFrom": "",
            "ccy": "USDT",
            "chain": "USDT-TRC20",
            "depId": "88165462",
            "from": "",
            "fromWdId": "",
            "pTime": "1674103661147",
            "state": "0",
            "subAcct": "test",
            "to": "TEhFAqpuHa3LY*****8ByNoGnrmexeGMw",
            "ts": "1674103661123",
            "txId": "bc5376817*****************dbb0d729f6b",
            "uid": "289320****60975104"
        }]
    }
    

#### 推送数据参数

**参数名** | **类型** | **描述**  
---|---|---  
arg | Object | 订阅成功的频道  
> channel | String | 频道名  
`deposit-info`  
> uid | String | 用户标识  
> ccy | String | 币种名称，如 `BTC`  
data | Array of objects | 订阅的数据  
> uid | String | (产生数据者的）用户标识  
> subAcct | String | 子账户名称  
如果是母账户产生的数据，该字段返回""  
> pTime | String | 推送时间，Unix时间戳的毫秒数格式，如 1597026383085  
> ccy | String | 币种名称，如 `BTC`  
> chain | String | 币种链信息  
有的币种下有多个链，必须要做区分，如`USDT`下有`USDT-ERC20`，`USDT-TRC20`多个链  
> amt | String | 充值数量  
> from | String | 充值账户，仅展示内部账户的转账地址（手机号和邮箱将做脱敏处理），不展示区块链充值地址  
> areaCodeFrom | String | 如果`from`为手机号，该字段为该手机号的区号  
> to | String | 到账地址  
> txId | String | 区块转账哈希记录  
> ts | String | 充值记录创建时间，Unix 时间戳的毫秒数格式，如 `1655251200000`  
> state | String | 充值状态  
`0`：等待确认   
`1`：确认到账   
`2`：充值成功   
`8`：因该币种暂停充值而未到账，恢复充值后自动到账  
`11`：命中地址黑名单  
`12`：账户或充值被冻结  
`13`：子账户充值拦截  
`14`：KYC限额  
> depId | String | 充值记录 ID  
> fromWdId | String | 内部转账发起者提币申请 ID  
如果该笔充值来自于内部转账，则该字段展示内部转账发起者的提币申请 ID，其他情况返回""  
> actualDepBlkConfirm | String | 最新的充币网络确认数  
  
### 提币信息频道 

当发起提币或者提币状态发生变化时会触发消息推送。  
支持母账户或者子账户的订阅  

  * 如果是母账户订阅，可以同时接受母账户与子账户的提币信息的推送  

  * 如果是子账户订阅，则仅支持子账户提币信息的推送  

#### 服务地址

/ws/v5/business (需要登录)

> 请求示例
    
    
    {
      "id": "1512",
        "op": "subscribe",
        "args": [
            {
                "channel": "withdrawal-info"
            }
        ]
    }
    
    
    
    import asyncio
    from okx.websocket.WsPrivateAsync import WsPrivateAsync
    
    def callbackFunc(message):
        print(message)
    
    async def main():
        ws = WsPrivateAsync(
            apiKey = "YOUR_API_KEY",
            passphrase = "YOUR_PASSPHRASE",
            secretKey = "YOUR_SECRET_KEY",
            url = "wss://ws.okx.com:8443/ws/v5/business",
            useServerTime=False
        )
        await ws.start()
        args = [
            {
                "channel": "withdrawal-info"
            }
        ]
    
        await ws.subscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
        await ws.unsubscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
    
    asyncio.run(main())
    
    

#### 请求参数

参数名 | 类型 | 是否必填 | 描述  
---|---|---|---  
id | String | 否 | 消息的唯一标识。  
用户提供，返回参数中会返回以便于找到相应的请求。  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度必须要在1-32位之间。  
op | String | 是 | 操作  
`subscribe`  
`unsubscribe`  
  
args | Array of objects | 是 | 请求订阅的频道列表  
> channel | String | 是 | 频道名  
`withdrawal-info`  
> ccy | String | 否 | 币种名称，如 `BTC`  
  
> 成功返回示例
    
    
    {
        "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "withdrawal-info"
        },
        "connId": "a4d3ae55"
    }
    

> 失败返回示例
    
    
    {
        "id": "1512",
        "event": "error",
        "code": "60012",
        "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"withdrawal-info\"}]}",
        "connId": "a4d3ae55"
    }
    

#### 返回参数

参数名 | 类型 | 是否必填 | 描述  
---|---|---|---  
id | String | 否 | 消息的唯一标识  
event | String | 是 | 操作  
`subscribe`  
`unsubscribe`  
`error`  
arg | Object | 否 | 订阅的频道  
> channel | String | 是 | 频道名  
`withdrawal-info`  
> ccy | String | 否 | 币种名称，如 `BTC`  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID  
  
> 推送示例
    
    
    {
        "arg": {
            "channel": "withdrawal-info",
            "uid": "289320*****0975104"
        },
        "data": [{
            "addrEx": null,
            "amt": "2",
            "areaCodeFrom": "",
            "areaCodeTo": "",
            "ccy": "USDT",
            "chain": "USDT-TRC20",
            "clientId": "",
            "fee": "0.8",
            "feeCcy": "USDT",
            "from": "",
            "memo": "",
            "nonTradableAsset": false,
            "note": "",
            "pTime": "1674103268578",
            "pmtId": "",
            "state": "0",
            "subAcct": "test",
            "tag": "",
            "to": "TN8CKTQMnpWfT******8KipbJ24ErguhF",
            "toAddrType": "1",
            "ts": "1674103268472",
            "txId": "",
            "uid": "289333*****1101696",
            "wdId": "63754560"
        }]
    }
    

#### 推送数据参数

**参数名** | **类型** | **描述**  
---|---|---  
arg | Object | 订阅成功的频道  
> channel | String | 频道名  
> uid | String | 用户标识  
> ccy | String | 币种名称，如 `BTC`  
data | Array of objects | 订阅的数据  
> uid | String | (产生数据者的）用户标识  
> subAcct | String | 子账户名称  
如果是母账户产生的数据，该字段返回""  
> pTime | String | 推送时间，Unix时间戳的毫秒数格式，如 1597026383085  
> ccy | String | 币种  
> chain | String | 币种链信息  
有的币种下有多个链，必须要做区分，如`USDT`下有`USDT-ERC20`，`USDT-TRC20`多个链  
> nonTradableAsset | String | 是否为不可交易资产  
`true`：不可交易资产，`false`：可交易资产  
> amt | String | 数量  
> ts | String | 提币申请时间，Unix 时间戳的毫秒数格式，如 `1655251200000`  
> from | String | 提币账户  
可以是`邮箱`/`手机号`/`子账户名`  
> areaCodeFrom | String | 如果`from`为手机号，该字段为该手机号的区号  
> to | String | 收币地址  
> areaCodeTo | String | 如果`to`为手机号，该字段为该手机号的区号  
> toAddrType | String | 地址类型  
`1`: 钱包地址、邮箱、手机号、登录账户名  
`2`: UID  
> tag | String | 部分币种提币需要标签  
> pmtId | String | 部分币种提币需要此字段（payment_id）  
> memo | String | 部分币种提币需要此字段  
> addrEx | Object | 提币地址备注。如币种TONCOIN的提币地址备注标签名为comment,则该字段返回：{'comment':'123456'}  
> txId | String | 提币哈希记录  
内部转账该字段返回""  
> fee | String | 提币手续费数量  
> feeCcy | String | 提币手续费币种，如 `USDT`  
> state | String | 提币状态  
  

* 阶段1：等待提币
`17`：钱包地址正等待国际转账规则认证  
`10`：等待划转  
`0`：等待提币  
`4`/`5`/`6`/`8`/`9`/`12`：等待客服审核  
`7`：审核通过  
  

* 阶段2：提币处理中（适用于链上提币，内部转账无此阶段）
`1`：正在将您的交易广播到链上  
`15`：交易待确认  
`16`：根据当地法律法规，您的提币最多可能需要 24 小时才能到账  
`-3`：撤销中  
  

* 最终阶段
`-2`：已撤销  
`-1`：失败  
`2`：提币成功  
> wdId | String | 提币申请ID  
> clientId | String | 客户自定义ID  
> note | String | 备注信息