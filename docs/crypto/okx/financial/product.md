---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#financial-product
anchor_id: financial-product
api_type: API
updated_at: 2026-07-23 19:23:08.453905
---

# Financial Product

## On-chain earn  
  
Only the assets in the funding account can be used for purchase. [More details](/earn/onchain-earn)

### GET / Offers

#### Rate Limit: 3 requests per second

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/finance/staking-defi/offers`

> Request Example
    
    
    GET /api/v5/finance/staking-defi/offers
    
    
    
    
    import okx.Finance.StakingDefi as StakingDefi
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    StakingAPI = StakingDefi.StakingDefiAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StakingAPI.get_offers(ccy="USDT")
    print(result)
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
productId | String | No | Product ID  
protocolType | String | No | Protocol type  
`defi`: on-chain earn  
ccy | String | No | Investment currency, e.g. `BTC`  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "ccy": "DOT",
                "productId": "101",
                "protocol": "Polkadot",
                "protocolType": "defi",
                "term": "0",
                "apy": "0.1767",
                "earlyRedeem": false,
                "state": "purchasable",
                "investData": [
                    {
                        "bal": "0",
                        "ccy": "DOT",
                        "maxAmt": "0",
                        "minAmt": "2"
                    }
                ],
                "earningData": [
                    {
                        "ccy": "DOT",
                        "earningType": "0"
                    }
                ],
                "fastRedemptionDailyLimit": "",
                "redeemPeriod": [
                    "28D",
                    "28D"
                ]
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ccy | String | Currency type, e.g. `BTC`  
productId | String | Product ID  
protocol | String | Protocol  
protocolType | String | Protocol type  
`defi`: on-chain earn  
term | String | Protocol term  
It will return the days of fixed term and will return `0` for flexible product  
apy | String | Estimated annualization  
If the annualization is 7% , this field is 0.07  
earlyRedeem | Boolean | Whether the protocol supports early redemption  
investData | Array of objects | Current target currency information available for investment  
> ccy | String | Investment currency, e.g. `BTC`  
> bal | String | Available balance to invest  
> minAmt | String | Minimum subscription amount  
> maxAmt | String | Maximum available subscription amount  
earningData | Array of objects | Earning data  
> ccy | String | Earning currency, e.g. `BTC`  
> earningType | String | Earning type  
`0`: Estimated earning  
`1`: Cumulative earning  
state | String | Product state  
`purchasable`: Purchasable  
`sold_out`: Sold out  
`Stop`: Suspension of subscription  
redeemPeriod | Array of strings | Redemption Period, format in [min time,max time]  
`H`: Hour, `D`: Day  
e.g. ["1H","24H"] represents redemption period is between 1 Hour and 24 Hours.  
["14D","14D"] represents redemption period is 14 days.  
fastRedemptionDailyLimit | String | Fast redemption daily limit  
If fast redemption is not supported, it will return ''.  
  
### POST / Purchase

#### Rate Limit: 2 requests per second

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/finance/staking-defi/purchase`

> Request Example
    
    
    # Invest 100ZIL 30-day staking protocol
    POST /api/v5/finance/staking-defi/purchase
    body 
    {
        "productId":"1234",
        "investData":[
          {
            "ccy":"ZIL",
            "amt":"100"
          }
        ],
        "term":"30"
    }
    
    
    
    import okx.Finance.StakingDefi as StakingDefi
    
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    StakingAPI = StakingDefi.StakingDefiAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StakingAPI.purchase(
                productId = "4005", 
                investData = [{
                    "ccy":"USDT",
                    "amt":"100"
                }]
            )
    print(result)
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
productId | String | Yes | Product ID  
investData | Array of objects | Yes | Investment data  
> ccy | String | Yes | Investment currency, e.g. `BTC`  
> amt | String | Yes | Investment amount  
term | String | Conditional | Investment term  
Investment term must be specified for fixed-term product  
tag | String | No | Order tag  
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 16 characters.  
  
> Response Example
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
        {
          "ordId": "754147",
          "tag": ""
        }
      ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ordId | String | Order ID  
tag | String | Order tag  
  
### POST / Redeem

#### Rate Limit: 2 requests per second

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/finance/staking-defi/redeem`

> Request Example
    
    
    # Early redemption of investment
    POST /api/v5/finance/staking-defi/redeem
    body 
    {
        "ordId":"754147",
        "protocolType":"defi",
        "allowEarlyRedeem":true
    }
    
    
    
    import okx.Finance.StakingDefi as StakingDefi
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    StakingAPI = StakingDefi.StakingDefiAPI(apikey, secretkey, passphrase, False, flag)
    
    
    result = StakingAPI.redeem(
               ordId = "1234",
               protocolType = "defi"
            )
    print(result)
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
ordId | String | Yes | Order ID  
protocolType | String | Yes | Protocol type  
`defi`: on-chain earn  
allowEarlyRedeem | Boolean | No | Whether allows early redemption  
Default is `false`  
  
> Response Example
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
        {
          "ordId": "754147",
          "tag": ""
        }
      ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ordId | String | Order ID  
tag | String | Order tag  
  
### POST / Cancel purchases/redemptions

After cancelling, returning funds will go to the funding account. 

#### Rate Limit: 2 requests per second

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/finance/staking-defi/cancel`

> Request Example
    
    
    POST /api/v5/finance/staking-defi/cancel
    body 
    {
        "ordId":"754147",
        "protocolType":"defi"
    }
    
    
    
    import okx.Finance.StakingDefi as StakingDefi
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    StakingAPI = StakingDefi.StakingDefiAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StakingAPI.cancel(
               ordId = "1234",
               protocolType = "defi"
            )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
ordId | String | Yes | Order ID  
protocolType | String | Yes | Protocol type  
`defi`: on-chain earn  
  
> Response Example
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
        {
          "ordId": "754147",
          "tag": ""
        }
      ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ordId | String | Order ID  
tag | String | Order tag  
  
### GET / Active orders

#### Rate Limit: 3 requests per second

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/finance/staking-defi/orders-active`

> Request Example
    
    
    GET /api/v5/finance/staking-defi/orders-active
    
    
    
    
    import okx.Finance.StakingDefi as StakingDefi
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    StakingAPI = StakingDefi.StakingDefiAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StakingAPI.get_activity_orders()
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
productId | String | No | Product ID  
protocolType | String | No | Protocol type  
`defi`: on-chain earn  
ccy | String | No | Investment currency, e.g. `BTC`  
state | String | No | Order state  
`8`: Pending   
`13`: Cancelling   
`9`: Onchain   
`1`: Earning   
`2`: Redeeming  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "ordId": "2413499",
                "ccy": "DOT",
                "productId": "101",
                "state": "1",
                "protocol": "Polkadot",
                "protocolType": "defi",
                "term": "0",
                "apy": "0.1014",
                "investData": [
                    {
                        "ccy": "DOT",
                        "amt": "2"
                    }
                ],
                "earningData": [
                    {
                        "ccy": "DOT",
                        "earningType": "0",
                        "earnings": "0.10615025"
                    }
                ],
                "purchasedTime": "1729839328000",
                "tag": "",
                "estSettlementTime": "",
                "cancelRedemptionDeadline": "",
                "fastRedemptionData": []
            },
            {
                "ordId": "2213257",
                "ccy": "USDT",
                "productId": "4005",
                "state": "1",
                "protocol": "On-Chain Defi",
                "protocolType": "defi",
                "term": "0",
                "apy": "0.0323",
                "investData": [
                    {
                        "ccy": "USDT",
                        "amt": "1"
                    }
                ],
                "earningData": [
                    {
                        "ccy": "USDT",
                        "earningType": "0",
                        "earnings": "0.02886582"
                    },
                    {
                        "ccy": "COMP",
                        "earningType": "1",
                        "earnings": "0.0000627"
                    }
                ],
                "purchasedTime": "1725345790000",
                "tag": "",
                "estSettlementTime": "",
                "cancelRedemptionDeadline": "",
                "fastRedemptionData": []
            },
            {
                "ordId": "2210943",
                "ccy": "USDT",
                "productId": "4005",
                "state": "1",
                "protocol": "On-Chain Defi",
                "protocolType": "defi",
                "term": "0",
                "apy": "0.0323",
                "investData": [
                    {
                        "ccy": "USDT",
                        "amt": "1"
                    }
                ],
                "earningData": [
                    {
                        "ccy": "USDT",
                        "earningType": "0",
                        "earnings": "0.02891823"
                    },
                    {
                        "ccy": "COMP",
                        "earningType": "1",
                        "earnings": "0.0000632"
                    }
                ],
                "purchasedTime": "1725280801000",
                "tag": "",
                "estSettlementTime": "",
                "cancelRedemptionDeadline": "",
                "fastRedemptionData": []
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ccy | String | Currency, e.g. `BTC`  
ordId | String | Order ID  
productId | String | Product ID  
state | String | Order state  
`8`: Pending   
`13`: Cancelling   
`9`: Onchain   
`1`: Earning   
`2`: Redeeming  
protocol | String | Protocol  
protocolType | String | Protocol type  
`defi`: on-chain earn  
term | String | Protocol term  
It will return the days of fixed term and will return `0` for flexible product  
apy | String | Estimated APY  
If the estimated APY is 7% , this field is 0.07  
Retain to 4 decimal places (truncated)  
investData | Array of objects | Investment data  
> ccy | String | Investment currency, e.g. `BTC`  
> amt | String | Invested amount  
earningData | Array of objects | Earning data  
> ccy | String | Earning currency, e.g. `BTC`  
> earningType | String | Earning type  
`0`: Estimated earning  
`1`: Cumulative earning  
> earnings | String | Earning amount  
fastRedemptionData | Array of objects | Fast redemption data  
> ccy | String | Currency, e.g. `BTC`  
> redeemingAmt | String | Redeeming amount  
purchasedTime | String | Order purchased time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
estSettlementTime | String | Estimated redemption settlement time  
cancelRedemptionDeadline | String | Deadline for cancellation of redemption application  
tag | String | Order tag  
  
### GET / Order history

#### Rate Limit: 3 requests per second

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/finance/staking-defi/orders-history`

> Request Example
    
    
    GET /api/v5/finance/staking-defi/orders-history
    
    
    
    
    import okx.Finance.StakingDefi as StakingDefi
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    StakingAPI = StakingDefi.StakingDefiAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StakingAPI.get_orders_history()
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
productId | String | No | Product ID  
protocolType | String | No | Protocol type  
`defi`: on-chain earn  
ccy | String | No | Investment currency, e.g. `BTC`  
after | String | No | Pagination of data to return records earlier than the requested ID. The value passed is the corresponding `ordId`  
before | String | No | Pagination of data to return records newer than the requested ID. The value passed is the corresponding `ordId`  
limit | String | No | Number of results per request. The default is `100`. The maximum is `100`.  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
           {
                "ordId": "1579252",
                "ccy": "DOT",
                "productId": "101",
                "state": "3",
                "protocol": "Polkadot",
                "protocolType": "defi",
                "term": "0",
                "apy": "0.1704",
                "investData": [
                    {
                        "ccy": "DOT",
                        "amt": "2"
                    }
                ],
                "earningData": [
                    {
                        "ccy": "DOT",
                        "earningType": "0",
                        "realizedEarnings": "0"
                    }
                ],
                "purchasedTime": "1712908001000",
                "redeemedTime": "1712914294000",
                "tag": ""
           }
        ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ccy | String | Currency, e.g. `BTC`  
ordId | String | Order ID  
productId | String | Product ID  
state | String | Order state  
`3`: Completed (including canceled and redeemed)  
protocol | String | Protocol  
protocolType | String | Protocol type  
`defi`: on-chain earn  
term | String | Protocol term  
It will return the days of fixed term and will return `0` for flexible product  
apy | String | Estimated APY  
If the estimated APY is 7% , this field is `0.07`  
Retain to 4 decimal places (truncated)  
investData | Array of objects | Investment data  
> ccy | String | Investment currency, e.g. `BTC`  
> amt | String | Invested amount  
earningData | Array of objects | Earning data  
> ccy | String | Earning currency, e.g. `BTC`  
> earningType | String | Earning type  
`0`: Estimated earning  
`1`: Cumulative earning  
> realizedEarnings | String | Cumulative earning of redeemed orders  
This field is just valid when the order is in redemption state  
purchasedTime | String | Order purchased time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
redeemedTime | String | Order redeemed time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
tag | String | Order tag  
  
## ETH staking

ETH Staking, also known as Ethereum Staking, is the process of participating in the Ethereum blockchain's Proof-of-Stake (PoS) consensus mechanism.  
Stake to receive BETH for liquidity at 1:1 ratio and earn daily BETH rewards  
[Learn more about ETH Staking](https://www.okx.com/earn/ethereum-staking)

### GET / Product info

#### Rate Limit: 3 requests per second

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/finance/staking-defi/eth/product-info`

> Request Example
    
    
    GET /api/v5/finance/staking-defi/eth/product-info
    
    
    
    
    import okx.Finance.EthStaking as EthStaking
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    StackingAPI = EthStaking.EthStakingAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StackingAPI.eth_product_info()
    print(result)
    

> Response Example
    
    
    {
        "code": "0",
        "data": [
          {
            "fastRedemptionDailyLimit": "100",
            "rate": "2.23",
            "redemptDays": "8",
            "minAmt": "0.001"
          }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
fastRedemptionDailyLimit | String | Fast redemption daily limit  
The master account and sub-accounts share the same limit  
rate | String | Latest BETH APY  
redemptDays | String | Redemption days of BETH  
minAmt | String | Minimum subscription amount of BETH  
  
### POST / Purchase

Staking ETH for BETH  
Only the assets in the funding account can be used.  

#### Rate Limit: 2 requests per second

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/finance/staking-defi/eth/purchase`

> Request Example
    
    
    POST /api/v5/finance/staking-defi/eth/purchase
    body 
    {
        "amt":"100"
    }
    
    
    
    import okx.Finance.EthStaking as EthStaking
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    StackingAPI = EthStaking.EthStakingAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StackingAPI.eth_purchase(amt="1")
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
amt | String | Yes | Investment amount  
  
> Response Example
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
      ]
    }
    

#### Response Parameters

code = `0` means your request has been successfully handled.

### POST / Redeem

Only the assets in the funding account can be used. If your BETH is in your trading account, you can make funding transfer first.  

#### Rate Limit: 2 requests per second

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/finance/staking-defi/eth/redeem`

> Request Example
    
    
    POST /api/v5/finance/staking-defi/eth/redeem
    body 
    {
        "amt": "10"
    }
    
    
    
    import okx.Finance.EthStaking as EthStaking
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    StackingAPI = EthStaking.EthStakingAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StackingAPI.eth_redeem(amt="1")
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
amt | String | Yes | Redeeming amount  
  
> Response Example
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
      ]
    }
    

#### Response Parameters

code = `0` means your request has been successfully handled.

### POST / Cancel redeem

#### Rate Limit: 2 requests per second

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/finance/staking-defi/eth/cancel-redeem`

> Request Example
    
    
    POST /api/v5/finance/staking-defi/eth/cancel-redeem
    body
    {
        "ordId": "1234567890"
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
ordId | String | Yes | Order ID  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "ordId": "1234567890"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ordId | String | Order ID  
  
### GET / Balance

The balance represents the real-time total BETH holdings across the entire account, including assets in the trading account, funding account, and those currently in the redeeming process.

#### Rate Limit: 6 requests per second

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/finance/staking-defi/eth/balance`

> Request Example
    
    
    GET /api/v5/finance/staking-defi/eth/balance
    
    
    
    import okx.Finance.EthStaking as EthStaking
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    StackingAPI = EthStaking.EthStakingAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StackingAPI.eth_balance()
    print(result)
    

#### Request Parameters

None

> Response Example
    
    
    {
        "code": "0",
        "data": [
          {
            "amt": "0.63926191",
            "ccy": "BETH",
            "latestInterestAccrual": "0.00006549",
            "totalInterestAccrual": "0.01490596",
            "ts": "1699257600000"
          }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ccy | String | Currency, e.g. `BETH`  
amt | String | Currency amount  
latestInterestAccrual | String | Latest interest accrual  
totalInterestAccrual | String | Total interest accrual  
ts | String | Query data time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
### GET / Purchase&Redeem history

#### Rate Limit: 6 requests per second

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/finance/staking-defi/eth/purchase-redeem-history`

> Request Example
    
    
    GET /api/v5/finance/staking-defi/eth/purchase-redeem-history
    
    
    
    import okx.Finance.EthStaking as EthStaking
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    StackingAPI = EthStaking.EthStakingAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StackingAPI.eth_purchase_redeem_history()
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
type | String | No | Type  
`purchase`  
`redeem`  
status | String | No | Status  
`pending`  
`success`  
`failed`  
`cancelled`  
after | String | No | Pagination of data to return records earlier than the `requestTime`. The value passed is the corresponding `timestamp`  
before | String | No | Pagination of data to return records newer than the `requestTime`. The value passed is the corresponding `timestamp`  
limit | String | No | Number of results per request. The default is `100`. The maximum is `100`.  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "amt": "0.62666630",
                "completedTime": "1683413171000",
                "estCompletedTime": "",
                "redeemingAmt": "",
                "requestTime": "1683413171000",
                "status": "success",
                "type": "purchase"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
type | String | Type  
`purchase`  
`redeem`  
amt | String | Purchase/Redeem amount  
redeemingAmt | String | Redeeming amount  
status | String | Status  
`pending`  
`success`  
`failed`  
`cancelled`  
ordId | String | Order ID  
requestTime | String | Request time of make purchase/redeem, Unix timestamp format in milliseconds, e.g. `1597026383085`  
completedTime | String | Completed time of redeem settlement, Unix timestamp format in milliseconds, e.g. `1597026383085`  
estCompletedTime | String | Estimated completed time of redeem settlement, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
### GET / APY history (Public)

Public endpoints don't need authorization.

#### Rate Limit: 6 requests per second

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/finance/staking-defi/eth/apy-history`

> Request Example
    
    
    GET /api/v5/finance/staking-defi/eth/apy-history?days=2
    
    
    
    
    import okx.Finance.EthStaking as EthStaking
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    StackingAPI = EthStaking.EthStakingAPI(flag=flag)
    
    result = StackingAPI.eth_apy_history(days="7")
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
days | String | Yes | Get the days of APY(Annual percentage yield) history record in the past  
No more than 365 days  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "rate": "0.02690000",
                "ts": "1734195600000"
            },
            {
                "rate": "0.02840000",
                "ts": "1734109200000"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
rate | String | APY(Annual percentage yield), e.g. `0.01` represents `1%`  
ts | String | Data time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
## SOL staking

By staking SOL tokens and delegating them to validators on the Solana network, you can receive equivalent OKSOL and earn extra OKSOL rewards.  
Stake SOL on Solana to receive OKSOL at a 1:1 ratio for liquidity  
[Learn more about OKSOL Staking](/earn/solana-staking#from=finance_crypto)

### GET / Product info

#### Rate Limit: 3 requests per second

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/finance/staking-defi/sol/product-info`

> Request Example
    
    
    GET /api/v5/finance/staking-defi/sol/product-info
    
    
    
    
    

> Response Example
    
    
    {
        "code": "0",
        "data": {
            "fastRedemptionAvail": "240",
            "fastRedemptionDailyLimit": "240",
            "rate": "5.57",
            "redemptDays": "2",
            "minAmt": "0.01"
        },
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
fastRedemptionDailyLimit | String | Fast redemption daily limit  
The master account and sub-accounts share the same limit  
fastRedemptionAvail | String | Currently fast redemption max available amount  
rate | String | Latest OKSOL APY  
redemptDays | String | Redemption days of OKSOL  
minAmt | String | Minimum subscription amount of OKSOL  
  
### POST / Purchase

Staking SOL for OKSOL  
Only the assets in the funding account can be used.  

#### Rate Limit: 2 requests per second

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/finance/staking-defi/sol/purchase`

> Request Example
    
    
    POST /api/v5/finance/staking-defi/sol/purchase
    body 
    {
        "amt":"100"
    }
    
    
    
    import okx.Finance.SolStaking as SolStaking
    
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    StackingAPI = SolStaking.SolStakingAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StackingAPI.sol_purchase(amt="1")
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
amt | String | Yes | Investment amount  
  
> Response Example
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
      ]
    }
    

#### Response Parameters

code = `0` means your request has been successfully handled.

### POST / Redeem

Only the assets in the funding account can be used. If your OKSOL is in your trading account, you can make funding transfer first.  

#### Rate Limit: 2 requests per second

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/finance/staking-defi/sol/redeem`

> Request Example
    
    
    POST /api/v5/finance/staking-defi/sol/redeem
    body 
    {
        "amt": "10"
    }
    
    
    
    import okx.Finance.SolStaking as SolStaking
    
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    StackingAPI = SolStaking.SolStakingAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StackingAPI.sol_redeem(amt="1")
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
amt | String | Yes | Redeeming amount  
  
> Response Example
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
      ]
    }
    

#### Response Parameters

code = `0` means your request has been successfully handled.

### GET / Balance

The balance represents the real-time total OKSOL holdings across the entire account, including assets in the trading account, funding account, and those currently in the redeeming process.

#### Rate Limit: 6 requests per second

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/finance/staking-defi/sol/balance`

> Request Example
    
    
    GET /api/v5/finance/staking-defi/sol/balance
    
    
    
    import okx.Finance.SolStaking as SolStaking
    
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    StackingAPI = SolStaking.SolStakingAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StackingAPI.sol_balance()
    print(result)
    

#### Request Parameters

None

> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "amt": "0.01100012",
                "ccy": "OKSOL",
                "latestInterestAccrual": "0.00000012",
                "totalInterestAccrual": "0.00000012"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ccy | String | Currency, e.g. `OKSOL`  
amt | String | Currency amount  
latestInterestAccrual | String | Latest interest accrual  
totalInterestAccrual | String | Total interest accrual  
  
### GET / Purchase&Redeem history

#### Rate Limit: 6 requests per second

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/finance/staking-defi/sol/purchase-redeem-history`

> Request Example
    
    
    GET /api/v5/finance/staking-defi/sol/purchase-redeem-history
    
    
    
    import okx.Finance.SolStaking as SolStaking
    
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    StackingAPI = SolStaking.SolStakingAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StackingAPI.sol_purchase_redeem_history()
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
type | String | No | Type  
`purchase`  
`redeem`  
status | String | No | Status  
`pending`  
`success`  
`failed`  
after | String | No | Pagination of data to return records earlier than the `requestTime`. The value passed is the corresponding `timestamp`  
before | String | No | Pagination of data to return records newer than the `requestTime`. The value passed is the corresponding `timestamp`  
limit | String | No | Number of results per request. The default is `100`. The maximum is `100`.  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "amt": "0.62666630",
                "completedTime": "1683413171000",
                "estCompletedTime": "",
                "redeemingAmt": "",
                "requestTime": "1683413171000",
                "status": "success",
                "type": "purchase"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
type | String | Type  
`purchase`  
`redeem`  
amt | String | Purchase/Redeem amount  
redeemingAmt | String | Redeeming amount  
status | String | Status  
`pending`  
`success`  
`failed`  
requestTime | String | Request time of make purchase/redeem, Unix timestamp format in milliseconds, e.g. `1597026383085`  
completedTime | String | Completed time of redeem settlement, Unix timestamp format in milliseconds, e.g. `1597026383085`  
estCompletedTime | String | Estimated completed time of redeem settlement, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
### GET / APY history (Public)

Public endpoints don't need authorization.

#### Rate Limit: 6 requests per second

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/finance/staking-defi/sol/apy-history`

> Request Example
    
    
    GET /api/v5/finance/staking-defi/sol/apy-history?days=2
    
    
    
    
    import okx.Finance.SolStaking as SolStaking
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    StackingAPI = SolStaking.SolStakingAPI(flag=flag)
    
    result = StackingAPI.sol_apy_history(days="7")
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
days | String | Yes | Get the days of APY(Annual percentage yield) history record in the past  
No more than 365 days  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "rate": "0.11280000",
                "ts": "1734192000000"
            },
            {
                "rate": "0.11270000",
                "ts": "1734105600000"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
rate | String | APY(Annual percentage yield), e.g. `0.01` represents `1%`  
ts | String | Data time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
## Stable Rewards

OKX Stable Rewards automatically distributes daily rewards to holders of eligible stablecoins (e.g. `USDG`) without any action required once enrolled.  
Subscribe from the funding account; rewards and redemptions settle to the trading account by default.

> **Deprecation Notice**
> 
> `POST /api/v5/finance/stable-rewards/quote`, `POST /api/v5/finance/stable-rewards/trade`, and `GET /api/v5/finance/stable-rewards/subscribe-redeem-history` have been decommissioned. Please use the standard [order book trading APIs](/docs-v5/en/#order-book-trading) to trade USDG and other stablecoins.

### GET / Product info

Retrieve product-level information for the specified stablecoin, including all currencies eligible for subscription and redemption, applicable fee rates, amount limits, daily quotas, and current redemption availability.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/finance/stable-rewards/product-info`

> Request Example
    
    
    GET /api/v5/finance/stable-rewards/product-info?ccy=USDG
    

#### Request Parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
ccy | String | Yes | Stablecoin, e.g. `USDG`  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "details": [
                    {
                        "ccy": "USDG",
                        "settleCcy": "USDC",
                        "subFeeRate": "0.0003",
                        "redemptFeeRate": "0",
                        "minSubAmt": "1",
                        "minRedeemAmt": "0.0000001",
                        "remainingSubQuota": "1000000",
                        "remainingRedemptQuota": "500000",
                        "canRedeem": true
                    },
                    {
                        "ccy": "USDG",
                        "settleCcy": "USDT",
                        "subFeeRate": "0.0003",
                        "redemptFeeRate": "",
                        "minSubAmt": "1",
                        "minRedeemAmt": "",
                        "remainingSubQuota": "1000000",
                        "remainingRedemptQuota": "",
                        "canRedeem": false
                    }
                ],
                "ts": "1718035200000"
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
details | Array of objects | List of supported settlement currencies and their subscription/redemption details  
> ccy | String | Subscribable stablecoin, e.g. `USDG`  
> settleCcy | String | Settlement currency that can be used to subscribe to `ccy`, e.g. `USDC`, `USDT`  
> subFeeRate | String | Subscription fee rate, e.g. `0.01` represents `1%`  
> redemptFeeRate | String | Redemption fee rate, e.g. `0.01` represents `1%`  
Returns `""` if redemption to the given `settleCcy` is not available  
> minSubAmt | String | Minimum subscription amount, denominated in `settleCcy`  
> minRedeemAmt | String | Minimum redemption amount, denominated in `ccy`  
Returns `""` if redemption to the given `settleCcy` is not available  
> remainingSubQuota | String | Remaining daily subscription quota per master user ID  
Returns `-1` if unlimited  
> remainingRedemptQuota | String | Remaining daily redemption quota per master user ID  
Returns `-1` if unlimited  
Returns `""` if redemption to the given `settleCcy` is not available  
> canRedeem | Boolean | Whether redemption to the given `settleCcy` is currently available  
`true`: Available  
`false`: Unavailable  
ts | String | Data query time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
### GET / Balance

Retrieve the real-time Stable Rewards balance across the account (trading account, funding account, and in-progress redemptions combined), along with lifetime earnings and the current earning state for each stablecoin.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/finance/stable-rewards/balance`

> Request Example
    
    
    GET /api/v5/finance/stable-rewards/balance?ccy=USDG
    

#### Request Parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
ccy | String | No | Stablecoin, e.g. `USDG`  
Returns all supported stablecoins if not specified  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "details": [
                    {
                        "ccy": "USDG",
                        "amt": "100",
                        "totalEarnAccrual": "0.0003",
                        "state": "earning"
                    }
                ],
                "ts": "1718035200000"
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
details | Array of objects | Real-time balance details per stablecoin  
> ccy | String | Stablecoin, e.g. `USDG`  
> amt | String | Currency amount held across the entire account  
> totalEarnAccrual | String | Total interest accrued over the lifetime of the holding  
> state | String | Earning state  
`earning`: The balance is currently accruing rewards  
`pending`: The balance is not currently accruing (e.g. auto-earn is off, or the balance is below the activation threshold)  
ts | String | Query data time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
### GET / APY history

Retrieve the historical daily APY of the specified stablecoin. The returned rate reflects the user's current VIP level.

#### Rate Limit: 6 requests per second

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/finance/stable-rewards/apy-history`

> Request Example
    
    
    GET /api/v5/finance/stable-rewards/apy-history?ccy=USDG
    

#### Request Parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
ccy | String | Yes | Stablecoin, e.g. `USDG`  
days | String | No | Number of historical days to return. The default is `100`. The maximum is `100`  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "rate": "0.004",
                "ts": "1718035200000"
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
rate | String | Daily APY for the user's current VIP level, e.g. `0.041` represents `4.1%`  
ts | String | Snapshot time (UTC+0), Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
## OKUSD

OKUSD is OKX's stablecoin receipt issued at a 1:1 rate against USDT. Holders earn daily APR with no action required, and OKUSD can be used as trading margin to improve capital efficiency.  
Subscription and redemption operate on the funding account. Use the `/limits` endpoint to check your remaining daily quota before subscribing or redeeming.

### GET / OKUSD limits

Retrieve your remaining daily OKUSD subscription quota and both fast and standard redemption quotas. All limits are calculated at the master-account level and shared across sub-accounts.

#### Rate Limit: 2 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/finance/okusd/limits`

> Request Example
    
    
    GET /api/v5/finance/okusd/limits
    

#### Request Parameters

None

> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "subLimit": {
                    "maxSubAmt": "45000000",
                    "personalDailyLimit": "5000000",
                    "personalUsedAmt": "500000",
                    "platformDailyLimit": "50000000",
                    "platformUsedAmt": "5000000"
                },
                "fastRedeemLimit": {
                    "personalDailyLimit": "10000",
                    "personalUsedAmt": "0",
                    "platformDailyLimit": "5000000",
                    "platformUsedAmt": "1000000",
                    "feeRate": "0.001"
                },
                "stdRedeemLimit": {
                    "personalDailyLimit": "1000000",
                    "personalUsedAmt": "0",
                    "platformDailyLimit": "40000000",
                    "platformUsedAmt": "0",
                    "feeRate": "0.00025"
                },
                "ts": "1718500000000"
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
subLimit | Object | Subscription limit information  
> maxSubAmt | String | Maximum subscribable amount for today (USDT). Equal to `min(personalDailyLimit - personalUsedAmt, platformDailyLimit - platformUsedAmt)`. Minimum value is `"0"`  
> personalDailyLimit | String | Your daily subscription limit based on your VIP tier (USDT)  
> personalUsedAmt | String | Amount you have already subscribed today (USDT)  
> platformDailyLimit | String | Platform-wide daily subscription cap (USDT)  
> platformUsedAmt | String | Total amount subscribed across the platform today (USDT)  
fastRedeemLimit | Object | Fast redemption limit information (real-time settlement)  
> personalDailyLimit | String | Your daily fast redemption limit based on your VIP tier (OKUSD)  
> personalUsedAmt | String | Fast redemption amount you have already used today (OKUSD)  
> platformDailyLimit | String | Platform-wide daily fast redemption cap (OKUSD)  
> platformUsedAmt | String | Total fast redemption amount used across the platform today (OKUSD)  
> feeRate | String | Fee rate for fast redemption  
stdRedeemLimit | Object | Standard redemption limit information  
> personalDailyLimit | String | Your daily standard redemption limit based on your VIP tier (OKUSD)  
> personalUsedAmt | String | Standard redemption amount you have already used today (OKUSD)  
> platformDailyLimit | String | Platform-wide daily standard redemption cap (OKUSD)  
> platformUsedAmt | String | Total standard redemption amount used across the platform today (OKUSD)  
> feeRate | String | Fee rate for standard redemption  
ts | String | Server timestamp, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
### POST / Subscribe OKUSD

Subscribe USDT to receive OKUSD at a 1:1 rate with no subscription fee. OKUSD is credited immediately to your funding account. Pass a unique `clOrdId` per request; resubmitting the same `clOrdId` returns the original order without re-executing the subscription.

#### Rate Limit: 1 request per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/finance/okusd/subscribe`

> Request Example
    
    
    POST /api/v5/finance/okusd/subscribe
    body
    {
        "amt": "1000.00000000",
        "clOrdId": "my-sub-001"
    }
    

#### Request Parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
amt | String | Yes | Amount of USDT to subscribe. Minimum: `1`. Maximum 8 decimal places. Scientific notation is not supported  
clOrdId | String | Yes | Client-defined order ID. Maximum 32 characters (letters, digits, `-`, `_`). Must be unique per UID. Used for order tracking and idempotency  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "ordId": "680012345678901234",
                "clOrdId": "my-sub-001",
                "ccy": "USDT",
                "amt": "1000.00000000",
                "okusdAmt": "1000.00000000",
                "state": "success",
                "ts": "1718500000000"
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
ordId | String | System-generated order ID  
clOrdId | String | Client-defined order ID (echoed back)  
ccy | String | Subscription currency. Always `"USDT"`  
amt | String | Actual USDT amount subscribed  
okusdAmt | String | OKUSD amount credited to your funding account (equal to `amt` at 1:1 rate; no subscription fee)  
state | String | Order status: `"success"` / `"pending"` / `"failed"`  
ts | String | Order creation time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
### POST / Redeem OKUSD

Redeem OKUSD back to USDT. Choose between fast redemption (real-time settlement) or standard redemption (D+5 or D+6 calendar days, depending on submission time). Fee rates vary by redemption type — call `GET /limits` to get current rates. All fee amounts are truncated (floor) to 8 decimal places. Pass a unique `clOrdId` per request; resubmitting the same `clOrdId` returns the original order without re-executing the redemption.

#### Rate Limit: 1 request per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/finance/okusd/redeem`

> Request Example (Fast Redemption)
    
    
    POST /api/v5/finance/okusd/redeem
    body
    {
        "amt": "1000.00000000",
        "redeemType": "1",
        "clOrdId": "my-redeem-001"
    }
    

#### Request Parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
amt | String | Yes | Amount of OKUSD to redeem. Minimum: `1`. Maximum 8 decimal places. Scientific notation is not supported  
redeemType | String | Yes | Redemption type. `"1"`: Fast redemption (real-time settlement); `"2"`: Standard redemption (D+5 calendar days if submitted before UTC+8 16:00; D+6 calendar days if submitted at or after UTC+8 16:00). See the `feeRate` fields returned by `GET /limits` for current fee rates  
clOrdId | String | Yes | Client-defined order ID. Maximum 32 characters (letters, digits, `-`, `_`). Must be unique per UID. Used for order tracking and idempotency  
  
> Response Example (Fast Redemption)
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "ordId": "680012345678905678",
                "clOrdId": "my-redeem-001",
                "ccy": "OKUSD",
                "amt": "1000.00000000",
                "fee": "1.00000000",
                "usdtAmt": "999.00000000",
                "redeemType": "1",
                "state": "success",
                "estSettlementTime": "1718500010000",
                "ts": "1718500000000"
            }
        ]
    }
    

> Response Example (Standard Redemption)
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "ordId": "680012345678906789",
                "clOrdId": "my-redeem-002",
                "ccy": "OKUSD",
                "amt": "50000.00000000",
                "fee": "12.50000000",
                "usdtAmt": "49987.50000000",
                "redeemType": "2",
                "state": "processing",
                "estSettlementTime": "1718932800000",
                "ts": "1718500000000"
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
ordId | String | System-generated order ID  
clOrdId | String | Client-defined order ID (echoed back)  
ccy | String | Redemption currency. Always `"OKUSD"`  
amt | String | OKUSD amount redeemed  
fee | String | Fee charged in USDT, truncated (floor) to 8 decimal places  
usdtAmt | String | Net USDT amount credited to your funding account (`amt - fee`, truncated to 8 decimal places)  
redeemType | String | Redemption type: `"1"` (fast) or `"2"` (standard)  
state | String | Order status: `"processing"` / `"success"` / `"failed"` / `"cancelled"`  
estSettlementTime | String | Estimated settlement time, Unix timestamp format in milliseconds. Fast redemption: current time. Standard redemption: D+5 calendar days if submitted before UTC+8 16:00; D+6 calendar days if submitted at or after UTC+8 16:00  
ts | String | Order creation time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
### GET / Get OKUSD Account

Retrieve your current OKUSD balance and lifetime accrued yield. All balances are aggregated at the master-account level and shared across sub-accounts.

#### Rate Limit: 2 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/finance/okusd/account`

> Request Example
    
    
    GET /api/v5/finance/okusd/account
    

#### Request Parameters

None

> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "ccy": "OKUSD",
                "amt": "10000.00000000",
                "totalEarnAccrual": "123.45678900",
                "ts": "1718500000000"
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
ccy | String | Currency. Always `"OKUSD"`  
amt | String | Current OKUSD balance  
totalEarnAccrual | String | Cumulative yield accrued over the holding period, denominated in USDT  
ts | String | Server timestamp, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
### GET / Get Subscription History

Retrieve your OKUSD subscription order history. Results are returned in descending order by timestamp (newest first) and support time-range filtering.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/finance/okusd/subscribe/history`

> Request Example
    
    
    GET /api/v5/finance/okusd/subscribe/history?limit=2
    

#### Request Parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
limit | String | No | Number of results per page. Default `"100"`. Maximum `"100"`  
begin | String | No | Start time filter (order creation time `ts`, Unix ms, inclusive)  
end | String | No | End time filter (order creation time `ts`, Unix ms, inclusive)  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "ordId": "680012345678901234",
                "clOrdId": "my-sub-001",
                "ccy": "USDT",
                "amt": "1000.00000000",
                "settleCcy": "OKUSD",
                "settleCcyAmt": "1000.00000000",
                "status": "success",
                "ts": "1718500000000"
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
ordId | String | System-generated order ID  
clOrdId | String | Client-defined order ID (echoed back; empty string if not provided)  
ccy | String | Subscription currency. Always `"USDT"`  
amt | String | USDT amount subscribed  
settleCcy | String | Settlement currency. Always `"OKUSD"`  
settleCcyAmt | String | OKUSD amount credited (equal to `amt` at 1:1 rate)  
status | String | Terminal order status: `"success"` / `"failed"`  
ts | String | Order creation time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
### GET / Get Redemption History

Retrieve your OKUSD redemption order history. Results are returned in descending order by timestamp (newest first) and support time-range filtering and redemption-type filtering.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/finance/okusd/redeem/history`

> Request Example
    
    
    GET /api/v5/finance/okusd/redeem/history?type=fast
    

#### Request Parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
limit | String | No | Number of results per page. Default `"100"`. Maximum `"100"`  
begin | String | No | Start time filter (order creation time `ts`, Unix ms, inclusive)  
end | String | No | End time filter (order creation time `ts`, Unix ms, inclusive)  
type | String | No | Redemption type filter: `"fast"` for fast redemption only; `"standard"` for standard redemption only. Defaults to standard redemption if not specified  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "ordId": "680012345678905678",
                "clOrdId": "my-rdm-fast-001",
                "ccy": "OKUSD",
                "amt": "1000.00000000",
                "fee": "1.00000000",
                "settleCcy": "USDT",
                "settleCcyAmt": "999.00000000",
                "type": "fast",
                "status": "success",
                "estSettlementTime": "1718500010000",
                "ts": "1718500000000"
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
ordId | String | System-generated order ID  
clOrdId | String | Client-defined order ID (echoed back; empty string if not provided)  
ccy | String | Redemption currency. Always `"OKUSD"`  
amt | String | OKUSD amount redeemed  
fee | String | Fee charged in USDT, truncated (floor) to 8 decimal places  
settleCcy | String | Settlement currency. Always `"USDT"`  
settleCcyAmt | String | Net USDT amount credited (`amt - fee`, truncated to 8 decimal places)  
type | String | Redemption type: `"fast"` (real-time settlement) or `"standard"` (D+5/D+6 calendar days)  
status | String | Order status: `"pending"` / `"success"` / `"failed"` / `"canceled"`  
estSettlementTime | String | Estimated settlement time, Unix timestamp format in milliseconds. Empty string for settled fast redemption orders  
ts | String | Order creation time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
### GET / Get Rewards History

Retrieve your daily OKUSD yield distribution history. Results are returned in descending order by timestamp (newest first).

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/finance/okusd/rewards/history`

> Request Example
    
    
    GET /api/v5/finance/okusd/rewards/history?limit=7
    

#### Request Parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
limit | String | No | Number of results per page. Default `"30"`. Maximum `"100"`  
begin | String | No | Start time filter (`ts`, Unix ms, inclusive). Maximum query span is 6 months  
end | String | No | End time filter (`ts`, Unix ms, inclusive). Defaults to the current time if not provided  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "ccy": "USDT",
                "earnAmt": "1.14246575",
                "amt": "10000.00000000",
                "apr": "0.0418",
                "ts": "1718500000000"
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
ccy | String | Yield currency. Always `"USDT"`  
earnAmt | String | USDT yield distributed in this event  
amt | String | Your USDT principal balance at the time of distribution  
apr | String | APR applied for this distribution, e.g. `"0.0418"` represents 4.18%  
ts | String | Distribution timestamp, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
### GET / Get APR History

Retrieve the historical APR snapshots for OKUSD. Results are returned in descending order by timestamp (newest first). This endpoint requires API Key authentication even though the data is product-level and not user-specific.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/finance/okusd/rate/history`

> Request Example
    
    
    GET /api/v5/finance/okusd/rate/history?limit=10
    

#### Request Parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
limit | String | No | Number of results per page. Default `"30"`. Maximum `"100"`  
begin | String | No | Start time filter (`ts`, Unix ms, inclusive). Maximum query span is 6 months  
end | String | No | End time filter (`ts`, Unix ms, inclusive). Defaults to the current time if not provided  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            { "apr": "0.0418", "ts": "1718500000000" },
            { "apr": "0.0395", "ts": "1718413600000" }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
apr | String | OKUSD APR at this snapshot, e.g. `"0.0418"` represents 4.18%  
ts | String | Snapshot timestamp, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
## Simple earn flexible

Simple earn flexible (saving) is earned by lending to leveraged trading users in the lending market. [learn more](/earn/simple-earn)

### GET / Saving balance

#### Rate Limit: 6 requests per second

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/finance/savings/balance`

> Request Example
    
    
    GET /api/v5/finance/savings/balance?ccy=USDT
    
    
    
    
    import okx.Finance.Savings as Savings
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    SavingsAPI = Savings.SavingsAPI(apikey, secretkey, passphrase, False, flag)
    
    result = SavingsAPI.get_saving_balance(ccy="USDT")
    print(result)
    

#### Request Parameters

**Parameters** | **Types** | **Required** | **Description**  
---|---|---|---  
ccy | String | No | Currency, e.g. `BTC`  
  
> Response Example
    
    
    {
        "code": "0",
        "msg":"",
        "data": [
            {
                "earnings": "0.0010737388791526",
                "redemptAmt": "",
                "rate": "0.0100000000000000",
                "ccy": "USDT",
                "amt": "11.0010737453457821",
                "loanAmt": "11.0010630707982819",
                "pendingAmt": "0.0000106745475002"
            }
        ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ccy | String | Currency  
amt | String | Currency amount  
earnings | String | Currency earnings  
rate | String | Minimum annual lending rate configured by users  
loanAmt | String | Lending amount  
pendingAmt | String | Pending amount  
redemptAmt | String | ~~Redempting amount~~ (Deprecated)  
  
### POST / Savings purchase/redemption

Only the assets in the funding account can be used for saving.

#### Rate Limit: 6 requests per second

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/finance/savings/purchase-redempt`

> Request Example
    
    
    POST /api/v5/finance/savings/purchase-redempt
    body
    {
        "ccy":"BTC",
        "amt":"1",
        "side":"purchase",
        "rate":"0.01"
    }
    
    
    
    
    import okx.Finance.Savings as Savings
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    SavingsAPI = Savings.SavingsAPI(apikey, secretkey, passphrase, False, flag)
    
    result = SavingsAPI.savings_purchase_redemption(ccy='USDT',amt="0.1",side="purchase",rate="1")
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
ccy | String | Yes | Currency, e.g. `BTC`  
amt | String | Yes | Purchase/redemption amount  
side | String | Yes | Action type.   
`purchase`: purchase saving shares   
`redempt`: redeem saving shares  
rate | String | Conditional | Annual purchase rate, e.g. `0.1` represents `10%`  
Only applicable to purchase saving shares  
The interest rate of the new subscription will cover the interest rate of the last subscription  
The rate value range is between 1% and 365%  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "ccy":"BTC",
                "amt":"1",
                "side":"purchase",
                "rate": "0.01"
            }
        ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ccy | String | Currency  
amt | String | Purchase/Redemption amount  
side | String | Action type  
rate | String | Annual purchase rate, e.g. `0.1` represents `10%`  
  
### POST / Set lending rate

#### Rate Limit: 6 requests per second

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/finance/savings/set-lending-rate`

> Request Example
    
    
    POST /api/v5/finance/savings/set-lending-rate
    body
    {
        "ccy":"BTC",
        "rate":"0.02"
    }
    
    
    
    
    import okx.Finance.Savings as Savings
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    SavingsAPI = Savings.SavingsAPI(apikey, secretkey, passphrase, False, flag)
    
    result = SavingsAPI.set_lending_rate(ccy='USDT',rate="1")
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
ccy | String | Yes | Currency, e.g. `BTC`  
rate | String | Yes | Annual lending rate  
The rate value range is between 1% and 365%  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
            "ccy": "BTC",
            "rate": "0.02"
        }]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ccy | String | Currency, e.g. `BTC`  
rate | String | Annual lending rate  
  
### GET / Lending history

Return data in the past month.

#### Rate Limit: 6 requests per second

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/finance/savings/lending-history`

> Request Example
    
    
    GET /api/v5/finance/savings/lending-history
    
    
    
    
    import okx.Finance.Savings as Savings
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    SavingsAPI = Savings.SavingsAPI(apikey, secretkey, passphrase, False, flag)
    
    result = SavingsAPI.get_lending_history()
    print(result)
    

#### Request Parameters

**Parameters** | **Types** | **Required** | **Description**  
---|---|---|---  
ccy | String | No | Currency, e.g. `BTC`  
after | String | No | Pagination of data to return records earlier than the requested `ts`, Unix timestamp format in milliseconds, e.g. `1597026383085`  
before | String | No | Pagination of data to return records newer than the requested `ts`, Unix timestamp format in milliseconds, e.g. `1597026383085`  
limit | String | No | Number of results per request. The maximum is `100`. The default is `100`.  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
                "ccy": "BTC",
                "amt": "0.01",
                "earnings": "0.001",
                "rate": "0.01",
                "ts": "1597026383085"
            },
            {
                "ccy": "ETH",
                "amt": "0.2",
                "earnings": "0.001",
                "rate": "0.01",
                "ts": "1597026383085"
            }
        ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ccy | String | Currency, e.g. `BTC`  
amt | String | Lending amount  
earnings | String | Currency earnings  
rate | String | Lending annual interest rate  
ts | String | Lending time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
### GET / Public borrow info (public)

Authentication is not required for this public endpoint.

#### Rate Limit: 6 requests per second

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/finance/savings/lending-rate-summary`

> Request Example
    
    
    GET /api/v5/finance/savings/lending-rate-summary
    
    
    
    
    import okx.Finance.Savings as Savings
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    SavingsAPI = Savings.SavingsAPI(flag=flag)
    
    result = SavingsAPI.get_public_borrow_info()
    print(result)
    

#### Request Parameters

**Parameters** | **Types** | **Required** | **Description**  
---|---|---|---  
ccy | String | No | Currency, e.g. `BTC`  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
            "ccy": "BTC",
            "avgAmt": "10000",
            "avgAmtUsd": "10000000000",
            "avgRate": "0.03",
            "preRate": "0.02",
            "estRate": "0.01"
        }]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ccy | String | Currency, e.g. `BTC`  
avgAmt | String | ~~24H average borrowing amount~~(deprecated)  
avgAmtUsd | String | ~~24H average borrowing amount in`USD` value~~(deprecated)  
avgRate | String | 24-hours average annual borrowing rate  
preRate | String | Last annual borrowing interest rate  
estRate | String | Next estimate annual borrowing interest rate  
  
### GET / Public borrow history (public)

Authentication is not required for this public endpoint.  
Only returned records after December 14, 2021.

#### Rate Limit: 6 requests per second

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/finance/savings/lending-rate-history`

> Request Example
    
    
    GET /api/v5/finance/savings/lending-rate-history
    
    
    
    
    import okx.Finance.Savings as Savings
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    SavingsAPI = Savings.SavingsAPI(flag=flag)
    
    result = SavingsAPI.get_public_borrow_history()
    print(result)
    

#### Request Parameters

**Parameters** | **Types** | **Required** | **Description**  
---|---|---|---  
ccy | String | No | Currency, e.g. `BTC`  
after | String | No | Pagination of data to return records earlier than the requested `ts`, Unix timestamp format in milliseconds, e.g. `1597026383085`  
before | String | No | Pagination of data to return records newer than the requested `ts`, Unix timestamp format in milliseconds, e.g. `1597026383085`  
limit | String | No | Number of results per request. The maximum is `100`. The default is `100`.  
If `ccy` is not specified, all data under the same `ts` will be returned, not limited by `limit`  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
            "ccy": "BTC",
            "amt": "0.01",
            "rate": "0.001",
            "lendingRate": "0.001",
            "ts": "1597026383085"
        }]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ccy | String | Currency, e.g. `BTC`  
amt | String | ~~Lending amount~~(deprecated)  
rate | String | Annual borrowing interest rate  
lendingRate | String | Annual lending interest rate  
ts | String | Time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
## Flexible loan

OKX Flexible Loan is a high-end loan product that allows users to increase cash flow without selling off their crypto. [More details](/loan)

### GET / Borrowable currencies

Get borrowable currencies

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/finance/flexible-loan/borrow-currencies`

> Request Example
    
    
    GET /api/v5/finance/flexible-loan/borrow-currencies
    
    
    
    from okx.Finance import FlexibleLoan
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    flexibleLoanAPI = FlexibleLoan.FlexibleLoanAPI(apikey, secretkey, passphrase, False, flag)
    result = flexibleLoanAPI.borrow_currencies()
    print(result)
    

> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "borrowCcy": "USDT"
            },
            {
                "borrowCcy": "USDC"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
borrowCcy | String | Borrowable currency, e.g. `BTC`  
  
### GET / Collateral assets

Get collateral assets in funding account.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/finance/flexible-loan/collateral-assets`

> Request Example
    
    
    GET /api/v5/finance/flexible-loan/collateral-assets?ordId=12345
    
    
    
    from okx.Finance import FlexibleLoan
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    flexibleLoanAPI = FlexibleLoan.FlexibleLoanAPI(apikey, secretkey, passphrase, False, flag)
    result = flexibleLoanAPI.collateral_assets(ordId="12345")
    print(result)
    

#### Request Parameters

**Parameters** | **Types** | **Required** | **Description**  
---|---|---|---  
ccy | String | No | Collateral currency, e.g. `BTC`  
ordId | String. | No | Order ID of your flexible loan.  
If `ordId` is not passed, system will assume it is acting against the existing order with the earliest order start time.  
If there are no existing orders, system will return empty result data.  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "assets": [
                    {
                        "amt": "1.7921483143067599",
                        "ccy": "BTC",
                        "notionalUsd": "158292.621793314105231"
                    },
                    {
                        "amt": "1.9400755578876945",
                        "ccy": "ETH",
                        "notionalUsd": "6325.6652712507628946"
                    },
                    {
                        "amt": "63.9795959720319628",
                        "ccy": "USDT",
                        "notionalUsd": "64.3650372635940345"
                    }
                ]
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
assets | Array of objects | Collateral assets data  
> ccy | String | Currency, e.g. `BTC`  
> amt | String | Available amount  
> notionalUsd | String | Notional value in `USD`  
  
### POST / Maximum loan amount

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/finance/flexible-loan/max-loan`

> Request Example
    
    
    POST /api/v5/finance/flexible-loan/max-loan
    body
    {
        "ordId": "12345",
        "borrowCcy": "USDT"
    }
    
    
    
    
    from okx.Finance import FlexibleLoan
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    flexibleLoanAPI = FlexibleLoan.FlexibleLoanAPI(apikey, secretkey, passphrase, False, flag)
    result = flexibleLoanAPI.max_loan(ordId="12345", borrowCcy="USDT")
    print(result)
    

#### Request Parameters

**Parameters** | **Types** | **Required** | **Description**  
---|---|---|---  
borrowCcy | String | Yes | Currency to borrow, e.g. `USDT`  
ordId | String | No | Order ID of your flexible loan.  
If `ordId` is not passed, system will assume it is acting against the existing order with the earliest order start time.  
If there are no existing orders, system will return empty result data.  
supCollateral | Array of objects | No | Supplementary collateral assets  
> ccy | String | Yes | Currency, e.g. `BTC`  
> amt | String | Yes | Amount  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "borrowCcy": "USDT",
                "maxLoan": "0.01113",
                "notionalUsd": "0.01113356",
                "remainingQuota": "3395000"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
borrowCcy | String | Currency to borrow, e.g. `USDT`  
maxLoan | String | Maximum available loan  
notionalUsd | String | Maximum available loan notional value, unit in `USD`  
remainingQuota | String | Remaining quota, unit in `borrowCcy`  
  
### GET / Maximum collateral redeem amount

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/finance/flexible-loan/max-collateral-redeem-amount`

> Request Example
    
    
    GET /api/v5/finance/flexible-loan/max-collateral-redeem-amount?ccy=USDT&ordId=12345
    
    
    
    
    from okx.Finance import FlexibleLoan
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    flexibleLoanAPI = FlexibleLoan.FlexibleLoanAPI(apikey, secretkey, passphrase, False, flag)
    result = flexibleLoanAPI.max_collateral_redeem_amount(ordId="12345", ccy="USDT")
    print(result)
    

#### Request Parameters

**Parameters** | **Types** | **Required** | **Description**  
---|---|---|---  
ccy | String | Yes | Collateral currency, e.g. `USDT`  
ordId | String | No | Order ID of your flexible loan.  
If `ordId` is not passed, system will assume it is acting against the existing order with the earliest order start time.  
If there are no existing orders, system will return empty result data.  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "ccy": "USDT",
                "maxRedeemAmt": "1"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
ccy | String | Collateral currency, e.g. `USDT`  
maxRedeemAmt | String | Maximum collateral redeem amount  
  
### POST / Adjust collateral

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/finance/flexible-loan/adjust-collateral`

> Request Example
    
    
    POST /api/v5/finance/flexible-loan/adjust-collateral
    body
    {
        "type":"add",
        "ordId": "12345",
        "collateralCcy": "BTC",
        "collateralAmt": "0.1"
    }
    
    
    
    
    from okx.Finance import FlexibleLoan
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    flexibleLoanAPI = FlexibleLoan.FlexibleLoanAPI(apikey, secretkey, passphrase, False, flag)
    result = flexibleLoanAPI.adjust_collateral(type="add", ordId="12345", collateralCcy="USDT", collateralAmt="1")
    print(result)
    

#### Request Parameters

**Parameters** | **Types** | **Required** | **Description**  
---|---|---|---  
type | String | Yes | Operation type  
`add`: Add collateral  
`reduce`: Reduce collateral  
collateralCcy | String | Yes | Collateral currency, e.g. `BTC`  
collateralAmt | String | Yes | Collateral amount  
ordId | String | No | Order ID of your flexible loan.  
If `ordId` is not passed, system will assume it is acting against the existing order with the earliest order start time.  
If there are no existing orders, system will return error `51063`  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
        ],
        "msg": ""
    }
    

#### Response Parameters

code = `0` means your request has been accepted (It doesn't mean the request has been successfully handled.)

### GET / Loan info

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/finance/flexible-loan/loan-info`

> Request Example
    
    
    GET /api/v5/finance/flexible-loan/loan-info
    
    
    
    from okx.Finance import FlexibleLoan
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    flexibleLoanAPI = FlexibleLoan.FlexibleLoanAPI(apikey, secretkey, passphrase, False, flag)
    result = flexibleLoanAPI.loan_info()
    print(result)
    

#### Request Parameters

**Parameters** | **Types** | **Required** | **Description**  
---|---|---|---  
ordId | String | No | Order ID of your flexible loan.  
If `ordId` is not passed, system will return data of all existing orders  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "ordId": "12345",
                "collateralData": [
                    {
                        "amt": "0.0000097",
                        "ccy": "COMP"
                    },
                    {
                        "amt": "0.78",
                        "ccy": "STX"
                    },
                    {
                        "amt": "0.001",
                        "ccy": "DOT"
                    },
                    {
                        "amt": "0.05357864",
                        "ccy": "LUNA"
                    }
                ],
                "collateralNotionalUsd": "1.5078763",
                "curLTV": "0.5742",
                "liqLTV": "0.8374",
                "loanData": [
                    {
                        "amt": "0.86590608",
                        "ccy": "USDC"
                    }
                ],
                "loanNotionalUsd": "0.8661285",
                "marginCallLTV": "0.7374",
                "riskWarningData": {
                    "instId": "",
                    "liqPx": ""
                }
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
ordId | String | Order ID  
loanNotionalUsd | String | Loan value in `USD`  
loanData | Array of objects | Loan data  
> ccy | String | Loan currency, e.g. `USDT`  
> amt | String | Loan amount  
collateralNotionalUsd | String | Adjusted collateral value in `USD`  
collateralData | Array of objects | Collateral data  
> ccy | String | Collateral currency, e.g. `BTC`  
> amt | String | Collateral amount  
riskWarningData | Object | Risk warning data  
> instId | String | Liquidation instrument ID, e.g. `BTC-USDT`  
This field is only valid when there is only one type of collateral and one type of borrowed currency. In other cases, it returns "".  
> liqPx | String | Liquidation price  
The unit of the liquidation price is the quote currency of the instrument, e.g. `USDT` in `BTC-USDT`.  
This field is only valid when there is only one type of collateral and one type of borrowed currency. In other cases, it returns "".  
curLTV | String | Current LTV, e.g. `0.1` represents `10%`  
Note: LTV = Loan to Value  
marginCallLTV | String | Margin call LTV, e.g. `0.1` represents `10%`  
If your loan hits the margin call LTV, our system will automatically warn you that your loan is getting close to forced liquidation.  
liqLTV | String | Liquidation LTV, e.g. `0.1` represents `10%`  
If your loan reaches liquidation LTV, it'll trigger forced liquidation. When this happens, you'll lose access to your collateral and any repayments made.  
  
### GET / Loan history

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/finance/flexible-loan/loan-history`

> Request Example
    
    
    GET /api/v5/finance/flexible-loan/loan-history
    
    
    
    from okx.Finance import FlexibleLoan
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    flexibleLoanAPI = FlexibleLoan.FlexibleLoanAPI(apikey, secretkey, passphrase, False, flag)
    result = flexibleLoanAPI.loan_history()
    print(result)
    

#### Request Parameters

**Parameters** | **Types** | **Required** | **Description**  
---|---|---|---  
type | String | No | Action type  
`borrowed`  
`repaid`  
`collateral_locked`  
`collateral_released`  
`forced_repayment_buy`  
`forced_repayment_sell`  
`forced_liquidation`  
`partial_liquidation`  
`sell_collateral`  
`buy_transition_coin`  
`sell_transition_coin`  
`buy_borrowed_coin`  
after | String | No | Pagination of data to return records earlier than the requested `refId`(not include)  
before | String | No | Pagination of data to return records newer than the requested `refId`(not include)  
limit | String | No | Number of results per request. The maximum is `100`. The default is `100`.  
ordId | String | No | Order ID of your flexible loan.  
If `ordId` is not passed, system will return data of all orders  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "amt": "-0.001",
                "ccy": "DOT",
                "refId": "17316594851045086",
                "ts": "1731659485000",
                "type": "collateral_locked"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
refId | String | Reference ID  
type | String | Action type  
ccy | String | Currency, e.g. `BTC`  
amt | String | Amount  
ts | String | Timestamp for the action, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
### GET / Accrued interest

Retrieves the interest accrual history for flexible loans over the past 30 days.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/finance/flexible-loan/interest-accrued`

> Request Example
    
    
    GET /api/v5/finance/flexible-loan/interest-accrued
    
    
    
    from okx.Finance import FlexibleLoan
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    flexibleLoanAPI = FlexibleLoan.FlexibleLoanAPI(apikey, secretkey, passphrase, False, flag)
    result = flexibleLoanAPI.interest_accrued()
    print(result)
    

#### Request Parameters

**Parameters** | **Types** | **Required** | **Description**  
---|---|---|---  
ccy | String | No | Loan currency, e.g. `BTC`  
after | String | No | Pagination of data to return records earlier than the requested `refId`(not include)  
before | String | No | Pagination of data to return records newer than the requested `refId`(not include)  
limit | String | No | Number of results per request. The maximum is `100`. The default is `100`.  
ordId | String | No | Order ID of your flexible loan.  
If `ordId` is not passed, system will return data of all orders  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "ccy": "USDC",
                "interest": "0.00004054",
                "interestRate": "0.41",
                "loan": "0.86599309",
                "refId": "17319133035195744",
                "ts": "1731913200000"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
refId | String | Reference ID  
ccy | String | Loan currency, e.g. `BTC`  
loan | String | Loan when calculated interest  
interest | String | Interest  
interestRate | String | APY, e.g. `0.01` represents `1%`  
ts | String | Timestamp to calculated interest, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
## Dual investment

### GET / Currency pairs

Returns available dual investment currency pairs.

#### Rate Limit: 1 request per second

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/finance/sfp/dcd/currency-pair`

> Request Example
    
    
    GET /api/v5/finance/sfp/dcd/currency-pair
    

#### Request Parameters

None

> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "baseCcy": "BTC",
                "quoteCcy": "USDT",
                "optType": "C",
                "uly": "BTC-USD"
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
baseCcy | String | Base currency  
quoteCcy | String | Quote currency  
optType | String | Option type  
`C`: Call  
`P`: Put  
uly | String | Underlying  
  
### GET / Product info

Return dual investment product list.

#### Rate Limit: 1 request per second

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/finance/sfp/dcd/products`

> Request Example
    
    
    GET /api/v5/finance/sfp/dcd/products?baseCcy=BTC&quoteCcy=USDT&optType=C
    

#### Request Parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
baseCcy | String | Yes | Base currency  
quoteCcy | String | Yes | Quote currency  
optType | String | Yes | Option type  
`C`: Call  
`P`: Put  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "absYield": "0.00232413",
                "annualizedYield": "0.0541",
                "baseCcy": "BTC",
                "quoteCcy": "USDT",
                "expTime": "1774598400000",
                "interestAccrualTime": "1773244800000",
                "listTime": "1743150759000",
                "maxSize": "6000000",
                "minSize": "10",
                "notionalCcy": "USDT",
                "optType": "P",
                "productId": "BTC-USDT-260327-54500-P",
                "quoteTime": "1773243808703",
                "redeemEndTime": "1774594800000",
                "redeemStartTime": "1773244800000",
                "stepSz": "1",
                "tradeEndTime": "1774584000000",
                "strike": "54500",
                "uly": "BTC-USD"
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
absYield | String | Absolute yield  
annualizedYield | String | Annualized yield  
baseCcy | String | Base currency  
quoteCcy | String | Quote currency  
notionalCcy | String | Investment currency. If `C`, then baseCcy; if `P`, then quoteCcy.  
expTime | String | Expiry time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
interestAccrualTime | String | Interest accrual start time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
listTime | String | Product launch time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
minSize | String | Minimum trade size in notional currency  
maxSize | String | Maximum trade size in notional currency  
optType | String | Option type  
`C`: Call  
`P`: Put  
productId | String | Product ID  
quoteTime | String | When product was quoted, Unix timestamp format in milliseconds, e.g. `1597026383085`  
redeemStartTime | String | Earliest time to request early redemption, Unix timestamp format in milliseconds, e.g. `1597026383085`  
redeemEndTime | String | Latest time to request early redemption, Unix timestamp format in milliseconds, e.g. `1597026383085`  
stepSz | String | Trade step size in notional currency  
tradeEndTime | String | Trade end time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
uly | String | Underlying  
strike | String | Strike price  
  
### POST / Request for quote

Requests a real-time quote for a dual investment product. The quote has a TTL and must be used before expiry.

#### Rate Limit: 10 requests per 60 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/finance/sfp/dcd/quote`

> Request Example
    
    
    POST /api/v5/finance/sfp/dcd/quote
    body
    {
        "productId": "BTC-USDT-260327-77000-C",
        "notionalSz": "1.5",
        "notionalCcy": "BTC"
    }
    

#### Request Parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
productId | String | Yes | Product ID  
notionalSz | String | Yes | Investment size  
notionalCcy | String | Yes | Investment currency  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "absYield": "0.00135182",
                "annualizedYield": "69.65",
                "interestAccrualTime": "1773241200000",
                "notionalSz": "0.001",
                "notionalCcy": "BTC",
                "productId": "BTC-USDT-260312-72000-C",
                "quoteId": "qtbcDCD-QUOTE17732395560537636",
                "validUntil": "1774584000000",
                "idxPx": "69000"
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
absYield | String | Absolute yield  
annualizedYield | String | Annualized yield  
interestAccrualTime | String | Interest accrual start time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
notionalSz | String | Investment size  
notionalCcy | String | Investment currency  
productId | String | Product ID  
quoteId | String | Quote ID  
validUntil | String | Quote valid until, Unix timestamp format in milliseconds, e.g. `1597026383085`  
idxPx | String | Index price  
  
### POST / Trade

Places a dual investment order using a valid quote.

#### Rate Limit: 2 requests per 60 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/finance/sfp/dcd/trade`

> Request Example
    
    
    POST /api/v5/finance/sfp/dcd/trade
    body
    {
        "quoteId": "quoterbpDCD-QUOTE17732116652401234"
    }
    

#### Request Parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
quoteId | String | Yes | Quote ID  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "quoteId": "quoterbpDCD-QUOTE17732116652401234",
                "ordId": "987654321",
                "state": "live"
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
quoteId | String | Quote ID  
ordId | String | Order ID  
state | String | Order state  
`initial`: request has been received by system, will further process  
`pending_book`: trade received by liquidity provider, pending further processing  
`live`: trade is live  
`rejected`: trade has been rejected  
  
### POST / Request for redeem quote

Requests an early redemption quote for a live dual investment order. This is step 1 of the two-step early redemption flow; call POST / Redeem to confirm.

#### Rate Limit: 10 requests per 60 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/finance/sfp/dcd/redeem-quote`

> Request Example
    
    
    POST /api/v5/finance/sfp/dcd/redeem-quote
    body
    {
        "ordId": "987654321"
    }
    

#### Request Parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
ordId | String | Yes | Order ID  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "ordId": "987654321",
                "quoteId": "quoterbcDCD-REDEEM17732116652401234",
                "redeemCcy": "BTC",
                "redeemSz": "1.4856",
                "termRate": "-0.50",
                "validUntil": "1774598400000"
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
ordId | String | Order ID  
quoteId | String | Quote ID  
redeemSz | String | Redeem size  
redeemCcy | String | Redeem currency  
termRate | String | Term rate  
validUntil | String | Redeem quote valid until, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
### POST / Redeem

Confirms early redemption using a valid redeem quote. This is step 2 of the two-step early redemption flow.

#### Rate Limit: 2 requests per 60 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/finance/sfp/dcd/redeem`

> Request Example
    
    
    POST /api/v5/finance/sfp/dcd/redeem
    body
    {
        "ordId": "987654321",
        "quoteId": "quoterbcDCD-REDEEM17732116652401234"
    }
    

#### Request Parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
ordId | String | Yes | Order ID  
quoteId | String | Yes | Quote ID  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "ordId": "987654321",
                "state": "pending_redeem_booking"
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
ordId | String | Order ID  
state | String | order state  
`pending_redeem_booking`: redeem received, waiting for liquidity provider further processing  
`pending_redeem`: liquidity provider booked, waiting for transfer  
`redeeming`: redemption in progress  
`redeemed`: redemption completed  
  
### GET / Order state

Returns the current state of a dual investment order.

#### Rate Limit: 3 requests per second

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/finance/sfp/dcd/order-status`

> Request Example
    
    
    GET /api/v5/finance/sfp/dcd/order-status?ordId=987654321
    

#### Request Parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
ordId | String | Yes | Order ID  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "ordId": "987654321",
                "state": "live"
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
ordId | String | Order ID  
state | String | Order state  
`initial`  
`live`  
`pending_settle`  
`settled`  
`pending_redeem`  
`redeemed`  
`rejected`  
  
### GET / Order history

Return dual investment history orders

#### Rate Limit: 1 request per second

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/finance/sfp/dcd/order-history`

> Request Example
    
    
    GET /api/v5/finance/sfp/dcd/order-history
    

#### Request Parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
ordId | String | No | Order ID. When provided, returns that specific order directly (ignores other filters)  
productId | String | No | Product ID, e.g. `BTC-USDT-260327-77000-C`  
uly | String | No | Underlying index, e.g. `BTC-USD`  
state | String | No | Order state filter  
`initial`  
`live`  
`pending_settle`  
`settled`  
`pending_redeem`  
`redeemed`  
`rejected`  
beginId | String | No | Return records newer than this order ID  
endId | String | No | Return records earlier than this order ID  
begin | String | No | Begin timestamp filter, Unix timestamp format in milliseconds, e.g. `1597026383085`  
end | String | No | End timestamp filter, Unix timestamp format in milliseconds, e.g. `1597026383085`  
limit | String | No | Number of results per request, max 100  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "ordId": "987654321",
                "quoteId": "quoterbpDCD-QUOTE17732116652401234",
                "state": "settled",
                "productId": "BTC-USDT-260327-77000-C",
                "baseCcy": "BTC",
                "quoteCcy": "USDT",
                "uly": "BTC-USD",
                "strike": "77000",
                "notionalSz": "1.5",
                "notionalCcy": "BTC",
                "absYield": "0.00806038",
                "annualizedYield": "0.1834",
                "yieldSz": "0.01209057",
                "yieldCcy": "BTC",
                "settleSz": "1.51209057",
                "settleCcy": "BTC",
                "settlePx": "76500",
                "settleTime": "1774598400000",
                "expTime": "1774598400000",
                "redeemStartTime" : "1774598400000",
                "redeemEndime": "1774598400000",
                "cTime": "1773212400000",
                "uTime": "1773212400000"
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
ordId | String | Order ID  
quoteId | String | Quote ID  
state | String | Order state  
`initial`  
`live`  
`pending_settle`  
`settled`  
`pending_redeem`  
`redeemed`  
`rejected`  
productId | String | Product ID, e.g. `BTC-USDT-260327-77000-C`  
baseCcy | String | Base currency, e.g. `BTC`  
quoteCcy | String | Quote currency, e.g. `USDT`  
uly | String | Underlying index, e.g. `BTC-USD`  
strike | String | Strike price  
notionalSz | String | Notional size  
notionalCcy | String | Notional currency  
absYield | String | Absolute yield rate  
annualizedYield | String | Annual yield rate  
yieldSz | String | Yield size  
yieldCcy | String | Yield currency  
settleSz | String | Settlement size ("" if not yet settled)  
settleCcy | String | Settlement currency ("" if not yet settled)  
settlePx | String | Settlement price ("" if not yet settled)  
expTime | String | Product expiration time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
settleTime | String | Actual settled time, Unix timestamp format in milliseconds, e.g. `1597026383085` ("" if not yet settled)  
redeemStartTime | String | Earliest time to request early redemption, Unix timestamp format in milliseconds, e.g. `1597026383085`  
redeemEndTime | String | Latest time to request early redemption, Unix timestamp format in milliseconds, e.g. `1597026383085`  
cTime | String | Order creation time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
uTime | String | Last update time, Unix timestamp format in milliseconds, e.g. `1597026383085`

---

# 金融产品

## 链上赚币   
  
仅资金账户中的资产支持申购。[了解更多](/cn/earn/onchain-earn)

### GET / 查看项目 

#### 限速：3次/s

#### 限速规则：User ID

#### HTTP 请求

`GET /api/v5/finance/staking-defi/offers`

> 请求示例
    
    
    GET /api/v5/finance/staking-defi/offers
    
    
    
    
    import okx.Finance.StakingDefi as StakingDefi
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0" # 实盘:0 , 模拟盘:1
    
    StakingAPI = StakingDefi.StakingDefiAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StakingAPI.get_offers(ccy="USDT")
    print(result)
    
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
productId | String | 否 | 项目ID  
protocolType | String | 否 | 项目类型  
`defi`：链上赚币  
ccy | String | 否 | 投资币种，如 `BTC`  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "ccy": "DOT",
                "productId": "101",
                "protocol": "Polkadot",
                "protocolType": "defi",
                "term": "0",
                "apy": "0.1767",
                "earlyRedeem": false,
                "state": "purchasable",
                "investData": [
                    {
                        "bal": "0",
                        "ccy": "DOT",
                        "maxAmt": "0",
                        "minAmt": "2"
                    }
                ],
                "earningData": [
                    {
                        "ccy": "DOT",
                        "earningType": "0"
                    }
                ],
                "fastRedemptionDailyLimit": "",
                "redeemPeriod": [
                    "28D",
                    "28D"
                ]
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ccy | String | 币种名称，如 `BTC`  
productId | String | 项目ID  
protocol | String | 项目名称  
protocolType | String | 项目类型  
`defi`：链上赚币  
term | String | 项目期限  
活期为0，其他则显示定期天数  
apy | String | 预估年化  
如果年化为`7%` ，则该字段为`0.07`  
earlyRedeem | Boolean | 项目是否支持提前赎回  
investData | Array of objects | 目前用户可用来投资的目标币种信息  
> ccy | String | 投资币种，如`BTC`  
> bal | String | 可投数量  
> minAmt | String | 最小申购量  
> maxAmt | String | 最大可申购量  
earningData | Array of objects | 收益信息  
> ccy | String | 收益币种，如`BTC`  
> earningType | String | 收益类型  
`0`：预估收益  
`1`：累计发放收益  
state | String | 项目状态  
`purchasable`：可申购  
`sold_out`：售罄  
`stop`：暂停申购  
redeemPeriod | Array of strings | 赎回期，形式为 [最小赎回时间,最大赎回时间]  
`H`：小时，`D`：天  
例 ["1H","24H"] 表示赎回期时1小时到24小时。  
["14D","14D"] 表示赎回期为14天。  
fastRedemptionDailyLimit | String | 快速赎回每日最高限额  
如果不支持快速赎回，则返回""  
  

### POST / 申购项目 

#### 限速：2次/s

#### 限速规则：User ID

#### HTTP 请求

`POST /api/v5/finance/staking-defi/purchase`

> 请求示例
    
    
    # 投资100ZIL30天的锁仓挖矿项目
    POST /api/v5/finance/staking-defi/purchase
    body 
    {
        "productId":"1234",
        "investData":[
          {
            "ccy":"ZIL",
            "amt":"100"
          }
        ],
        "term":"30"
    }
    
    
    
    import okx.Finance.StakingDefi as StakingDefi
    
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0" # 实盘:0 , 模拟盘:1
    
    StakingAPI = StakingDefi.StakingDefiAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StakingAPI.purchase(
                productId = "4005", 
                investData = [{
                    "ccy":"USDT",
                    "amt":"100"
                }]
            )
    print(result)
    
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
productId | String | 是 | 项目ID  
investData | Array of objects | 是 | 投资信息  
> ccy | String | 是 | 投资币种，如 `BTC`  
> amt | String | 是 | 投资数量  
term | String | 可选 | 投资期限  
定期项目必须指定投资期限  
tag | String | 否 | 订单标签  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字，且长度在1-16位之间  
  
> 返回结果
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
        {
          "ordId": "754147",
          "tag": ""
        }
      ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ordId | String | 订单ID  
tag | String | 订单标签  
  
### POST / 赎回项目 

#### 限速：2次/s

#### 限速规则：User ID

#### HTTP 请求

`POST /api/v5/finance/staking-defi/redeem`

> 请求示例
    
    
    # 提前赎回项目投资
    POST /api/v5/finance/staking-defi/redeem
    body 
    {
        "ordId":"754147",
        "protocolType":"defi",
        "allowEarlyRedeem":true
    }
    
    
    
    import okx.Finance.StakingDefi as StakingDefi
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    StakingAPI = StakingDefi.StakingDefiAPI(apikey, secretkey, passphrase, False, flag)
    
    
    result = StakingAPI.redeem(
               ordId = "1234",
               protocolType = "defi"
            )
    print(result)
    
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
ordId | String | 是 | 订单ID  
protocolType | String | 是 | 项目类型  
`defi`：链上赚币  
allowEarlyRedeem | Boolean | 否 | 是否提前赎回  
默认为`false`  
  
> 返回结果
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
        {
          "ordId": "754147",
          "tag": ""
        }
      ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ordId | String | 订单ID  
tag | String | 订单标签  
  
### POST / 撤销项目申购/赎回 

撤销申购后的资金返回资金账户。 

#### 限速：2次/s

#### 限速规则：User ID

#### HTTP 请求

`POST /api/v5/finance/staking-defi/cancel`

> 请求示例
    
    
    POST /api/v5/finance/staking-defi/cancel
    body 
    {
        "ordId":"754147",
        "protocolType":"defi"
    }
    
    
    
    import okx.Finance.StakingDefi as StakingDefi
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘:0 , 模拟盘:1
    
    StakingAPI = StakingDefi.StakingDefiAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StakingAPI.cancel(
               ordId = "1234",
               protocolType = "defi"
            )
    print(result)
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
ordId | String | 是 | 订单ID  
protocolType | String | 是 | 项目类型  
`defi`：链上赚币  
  
> 返回结果
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
        {
          "ordId": "754147",
          "tag": ""
        }
      ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ordId | String | 订单ID  
tag | String | 订单标签  
  
### GET / 查看活跃订单 

#### 限速：3次/s

#### 限速规则：User ID

#### HTTP 请求

`GET /api/v5/finance/staking-defi/orders-active`

> 请求示例
    
    
    GET /api/v5/finance/staking-defi/orders-active
    
    
    
    
    import okx.Finance.StakingDefi as StakingDefi
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    StakingAPI = StakingDefi.StakingDefiAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StakingAPI.get_activity_orders()
    print(result)
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
productId | String | 否 | 项目ID  
protocolType | String | 否 | 项目类型  
`defi`：链上赚币  
ccy | String | 否 | 投资币种，如 `BTC`  
state | String | 否 | 订单状态  
`8`: 待上车（预约中）  
`13`: 订单取消中  
`9`: 上链中  
`1`: 收益中  
`2`: 赎回中  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "ordId": "2413499",
                "ccy": "DOT",
                "productId": "101",
                "state": "1",
                "protocol": "Polkadot",
                "protocolType": "defi",
                "term": "0",
                "apy": "0.1014",
                "investData": [
                    {
                        "ccy": "DOT",
                        "amt": "2"
                    }
                ],
                "earningData": [
                    {
                        "ccy": "DOT",
                        "earningType": "0",
                        "earnings": "0.10615025"
                    }
                ],
                "purchasedTime": "1729839328000",
                "tag": "",
                "estSettlementTime": "",
                "cancelRedemptionDeadline": "",
                "fastRedemptionData": []
            },
            {
                "ordId": "2213257",
                "ccy": "USDT",
                "productId": "4005",
                "state": "1",
                "protocol": "On-Chain Defi",
                "protocolType": "defi",
                "term": "0",
                "apy": "0.0323",
                "investData": [
                    {
                        "ccy": "USDT",
                        "amt": "1"
                    }
                ],
                "earningData": [
                    {
                        "ccy": "USDT",
                        "earningType": "0",
                        "earnings": "0.02886582"
                    },
                    {
                        "ccy": "COMP",
                        "earningType": "1",
                        "earnings": "0.0000627"
                    }
                ],
                "purchasedTime": "1725345790000",
                "tag": "",
                "estSettlementTime": "",
                "cancelRedemptionDeadline": "",
                "fastRedemptionData": []
            },
            {
                "ordId": "2210943",
                "ccy": "USDT",
                "productId": "4005",
                "state": "1",
                "protocol": "On-Chain Defi",
                "protocolType": "defi",
                "term": "0",
                "apy": "0.0323",
                "investData": [
                    {
                        "ccy": "USDT",
                        "amt": "1"
                    }
                ],
                "earningData": [
                    {
                        "ccy": "USDT",
                        "earningType": "0",
                        "earnings": "0.02891823"
                    },
                    {
                        "ccy": "COMP",
                        "earningType": "1",
                        "earnings": "0.0000632"
                    }
                ],
                "purchasedTime": "1725280801000",
                "tag": "",
                "estSettlementTime": "",
                "cancelRedemptionDeadline": "",
                "fastRedemptionData": []
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ccy | String | 币种名称，如 `BTC`  
ordId | String | 订单ID  
productId | String | 项目ID  
state | String | 订单状态  
`8`：待上车（预约中）  
`13`：订单取消中  
`9`：上链中  
`1`：收益中  
`2`：赎回中  
protocol | String | 项目名称  
protocolType | String | 项目类型  
`defi`：链上赚币  
term | String | 项目期限  
活期为0，其他则显示定期天数  
apy | String | 预估年化  
如果年化为7% ，则该字段为0.07  
保留到小数点后4位（截位）  
investData | Array of objects | 用户投资信息  
> ccy | String | 投资币种，如 `BTC`  
> amt | String | 已投资数量  
earningData | Array of objects | 收益信息  
> ccy | String | 收益币种，如 `BTC`  
> earningType | String | 收益类型  
`0`：预估收益  
`1`：实际到账收益  
> earnings | String | 收益数量  
fastRedemptionData | Array of objects | 快速赎回信息  
> ccy | String | 快速赎回币种，如 `BTC`  
> redeemingAmt | String | 赎回中的数量  
purchasedTime | String | 用户订单创建时间，值为时间戳，Unix时间戳为毫秒数格式，如 `1597026383085`  
estSettlementTime | String | 预估赎回到账时间  
cancelRedemptionDeadline | String | 撤销赎回申请截止时间  
tag | String | 订单标签  
  
### GET / 查看历史订单 

#### 限速：3次/s

#### 限速规则：User ID

#### HTTP 请求

`GET /api/v5/finance/staking-defi/orders-history`

> 请求示例
    
    
    GET /api/v5/finance/staking-defi/orders-history
    
    
    
    
    import okx.Finance.StakingDefi as StakingDefi
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    StakingAPI = StakingDefi.StakingDefiAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StakingAPI.get_orders_history()
    print(result)
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
productId | String | 否 | 项目ID  
protocolType | String | 否 | 项目类型  
`defi`：链上赚币  
ccy | String | 否 | 投资币种，如 `BTC`  
after | String | 否 | 请求此ID之前（更旧的数据）的分页内容，传的值为对应接口的`ordId`  
before | String | 否 | 请求此ID之后（更新的数据）的分页内容，传的值为对应接口的`ordId`  
limit | String | 否 | 返回结果的数量，默认100条，最大值为100条  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
           {
                "ordId": "1579252",
                "ccy": "DOT",
                "productId": "101",
                "state": "3",
                "protocol": "Polkadot",
                "protocolType": "defi",
                "term": "0",
                "apy": "0.1704",
                "investData": [
                    {
                        "ccy": "DOT",
                        "amt": "2"
                    }
                ],
                "earningData": [
                    {
                        "ccy": "DOT",
                        "earningType": "0",
                        "realizedEarnings": "0"
                    }
                ],
                "purchasedTime": "1712908001000",
                "redeemedTime": "1712914294000",
                "tag": ""
           }
        ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ccy | String | 币种名称，如 `BTC`  
ordId | String | 订单ID  
productId | String | 项目ID  
state | String | 订单状态  
3: 订单已完成（包含撤销和已赎回两种状态）  
protocol | String | 项目名称  
protocolType | String | 项目类型  
`defi`：链上赚币  
term | String | 项目期限  
活期为0，其他则显示定期天数  
apy | String | 预估年化  
如果年化为7% ，则该字段为0.07  
保留到小数点后4位（截位）  
investData | Array of objects | 用户投资信息  
> ccy | String | 投资币种，如`BTC`  
> amt | String | 已投资数量  
earningData | Array of objects | 收益信息  
> ccy | String | 收益币种，如`BTC`  
> earningType | String | 收益类型  
`0`：预估收益  
`1`：实际到账收益  
> realizedEarnings | String | 已赎回订单累计收益  
该字段仅在订单处于赎回状态时有效  
purchasedTime | String | 用户订单创建时间，值为时间戳，Unix时间戳为毫秒数格式，如 `1597026383085`  
redeemedTime | String | 用户订单赎回时间，值为时间戳，Unix时间戳为毫秒数格式，如 `1597026383085`  
tag | String | 订单标签  
  
## ETH质押 

ETH 质押，也称为以太坊质押，是参与以太坊区块链权益证明 (Proof of Stake, PoS) 共识机制的过程。  
质押 ETH 即获 1:1 BETH 并赚取每日奖励，享受更高流动性  
[了解更多](https://www.okx.com/zh-hans/earn/ethereum-staking)

### GET / 获取产品信息 

#### 限速：3 次/s

#### 限速规则：User ID

#### HTTP 请求

`GET /api/v5/finance/staking-defi/eth/product-info`

> 请求示例
    
    
    GET /api/v5/finance/staking-defi/eth/product-info
    
    
    
    
    import okx.Finance.EthStaking as EthStaking
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    StackingAPI = EthStaking.EthStakingAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StackingAPI.eth_product_info()
    print(result)
    

> 返回结果
    
    
    {
        "code": "0",
        "data": [
          {
            "fastRedemptionDailyLimit": "100",
            "rate": "2.23",
            "redemptDays": "8",
            "minAmt": "0.001"
          }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
fastRedemptionDailyLimit | String | 快速赎回每日最高份额  
母账户和子账户共享同一个限额  
rate | String | 最新 BETH 年化收益率  
redemptDays | String | BETH 赎回天数  
minAmt | String | BETH 最低申购数量  
  
### POST / 申购 

质押ETH获取BETH  
仅资金账户中的资产支持ETH质押。

#### 限速：2次/s

#### 限速规则：User ID

#### HTTP 请求

`POST /api/v5/finance/staking-defi/eth/purchase`

> 请求示例
    
    
    POST /api/v5/finance/staking-defi/eth/purchase
    body 
    {
        "amt":"100"
    }
    
    
    
    import okx.Finance.EthStaking as EthStaking
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    StackingAPI = EthStaking.EthStakingAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StackingAPI.eth_purchase(amt="1")
    print(result)
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
amt | String | 是 | 投资数量  
  
> 返回结果
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
      ]
    }
    

#### 返回参数

code = `0`代表请求已被成功处理

### POST / 赎回 

只能赎回资金账户中的 BETH 资产，交易账户中的 BETH 资产需要您先做资金划转到资金账户后赎回。

#### 限速：2次/s

#### 限速规则：User ID

#### HTTP 请求

`POST /api/v5/finance/staking-defi/eth/redeem`

> 请求示例
    
    
    POST /api/v5/finance/staking-defi/eth/redeem
    body 
    {
        "amt":"10"
    }
    
    
    
    import okx.Finance.EthStaking as EthStaking
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    StackingAPI = EthStaking.EthStakingAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StackingAPI.eth_redeem(amt="1")
    print(result)
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
amt | String | 是 | 赎回数量  
  
> 返回结果
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
      ]
    }
    

#### 返回参数

code = `0`代表请求已被成功处理

### POST / 撤销赎回 

#### 限速：2 次/s

#### 限速规则：User ID

#### HTTP 请求

`POST /api/v5/finance/staking-defi/eth/cancel-redeem`

> 请求示例
    
    
    POST /api/v5/finance/staking-defi/eth/cancel-redeem
    body
    {
        "ordId": "1234567890"
    }
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
ordId | String | 是 | 订单ID  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "ordId": "1234567890"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ordId | String | 订单ID  
  
### GET / 获取余额 

该余额表示账户内 BETH 的实时总持仓，包括交易账户、资金账户以及处于赎回过程中的资产。

#### 限速：6 次/s

#### 限速规则：User ID

#### HTTP 请求

`GET /api/v5/finance/staking-defi/eth/balance`

> 请求示例
    
    
    GET /api/v5/finance/staking-defi/eth/balance
    
    
    
    
    import okx.Finance.EthStaking as EthStaking
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    StackingAPI = EthStaking.EthStakingAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StackingAPI.eth_balance()
    print(result)
    

#### 请求参数

None

> 返回结果
    
    
    {
        "code": "0",
        "data": [
          {
            "amt": "0.63926191",
            "ccy": "BETH",
            "latestInterestAccrual": "0.00006549",
            "totalInterestAccrual": "0.01490596",
            "ts": "1699257600000"
          }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ccy | String | 币种名称，如 `BETH`  
amt | String | 币种数量  
latestInterestAccrual | String | 最近收益  
totalInterestAccrual | String | 历史总收益  
ts | String | 快照时间，值为时间戳，Unix时间戳为毫秒数格式，如 `1597026383085`  
  
### GET / 获取申购赎回记录 

#### 限速：6 次/s

#### 限速规则：User ID

#### HTTP 请求

`GET /api/v5/finance/staking-defi/eth/purchase-redeem-history`

> 请求示例
    
    
    GET /api/v5/finance/staking-defi/eth/purchase-redeem-history
    
    
    
    
    import okx.Finance.EthStaking as EthStaking
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    StackingAPI = EthStaking.EthStakingAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StackingAPI.eth_purchase_redeem_history()
    print(result)
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
type | String | 否 | 类型  
`purchase`：申购  
`redeem`：赎回  
status | String | 否 | 状态  
`pending`：处理中  
`success`：成功处理  
`failed`：处理失败  
`cancelled`：已取消  
after | String | 否 | 请求此`requestTime`之前（更旧的数据）的分页内容，值为时间戳，Unix 时间戳为毫秒数格式，如 `1597026383085`  
before | String | 否 | 请求此`requestTime`之后（更新的数据）的分页内容，值为时间戳，Unix 时间戳为毫秒数格式，如 `1597026383085`  
limit | String | 否 | 返回结果的数量，默认100条，最大值为100条  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "amt": "0.62666630",
                "completedTime": "1683413171000",
                "estCompletedTime": "",
                "redeemingAmt": "",
                "requestTime": "1683413171000",
                "status": "success",
                "type": "purchase"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
type | String | 类型  
`purchase`：申购  
`redeem`：赎回  
amt | String | 申购/赎回 的数量  
redeemingAmt | String | 赎回中的数量  
status | String | 状态  
`pending`：处理中  
`success`：成功处理  
`failed`：处理失败  
`cancelled`：已取消  
ordId | String | 订单ID  
requestTime | String | 发起 申购/赎回 请求的时间，值为时间戳，Unix时间戳为毫秒数格式，如 `1597026383085`  
completedTime | String | 赎回请求处理完成的时间，值为时间戳，Unix时间戳为毫秒数格式，如 `1597026383085`  
estCompletedTime | String | 预估完成赎回的时间，值为时间戳，Unix时间戳为毫秒数格式，如 `1597026383085`  
  
### GET / 获取历史收益率(公共) 

公共接口无须鉴权

#### 限速：6次/s

#### 限速规则：IP

#### HTTP 请求

`GET /api/v5/finance/staking-defi/eth/apy-history`

> 请求示例
    
    
    GET /api/v5/finance/staking-defi/eth/apy-history?days=2
    
    
    
    
    import okx.Finance.EthStaking as EthStaking
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    StackingAPI = EthStaking.EthStakingAPI(flag=flag)
    
    result = StackingAPI.eth_apy_history(days="7")
    print(result)
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
days | String | 是 | 查询最近多少天内的数据，不超过365天  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "rate": "0.02690000",
                "ts": "1734195600000"
            },
            {
                "rate": "0.02840000",
                "ts": "1734109200000"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
rate | String | 年化收益率，如 `0.01`代表`1%`  
ts | String | 时间，值为时间戳，Unix时间戳为毫秒数格式，如 `1597026383085`  
  
## SOL质押 

通过质押 SOL 代币并将其委托给 Solana 网络上的验证者，您可以收到等值的 OKSOL 并获得每日 OKSOL 奖励。  
在 Solana 上质押 SOL，即获 1:1 OKSOL，享受更高流动性  
[了解更多](/zh-hans/earn/solana-staking#from=finance_crypto)

### GET / 获取产品信息 

#### 限速：3 次/s

#### 限速规则：User ID

#### HTTP 请求

`GET /api/v5/finance/staking-defi/sol/product-info`

> 请求示例
    
    
    GET /api/v5/finance/staking-defi/sol/product-info
    
    
    
    
    

> 返回结果
    
    
    {
        "code": "0",
        "data": {
            "fastRedemptionAvail": "240",
            "fastRedemptionDailyLimit": "240",
            "rate": "5.57",
            "redemptDays": "2",
            "minAmt": "0.01"
        },
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
fastRedemptionDailyLimit | String | 快速赎回每日最高份额  
母账户和子账户共享同一个限额  
fastRedemptionAvail | String | 当前剩余最大可赎回数量  
rate | String | 最新 OKSOL 年化收益率  
redemptDays | String | OKSOL 赎回天数  
minAmt | String | OKSOL 最低申购数量  
  
### POST / 申购 

质押 SOL 获取 OKSOL  
仅资金账户中的资产支持 SOL 质押。

#### 限速：2次/s

#### 限速规则：User ID

#### HTTP 请求

`POST /api/v5/finance/staking-defi/sol/purchase`

> 请求示例
    
    
    POST /api/v5/finance/staking-defi/sol/purchase
    body 
    {
        "amt":"100"
    }
    
    
    
    import okx.Finance.SolStaking as SolStaking
    
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    StackingAPI = SolStaking.SolStakingAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StackingAPI.sol_purchase(amt="1")
    print(result)
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
amt | String | 是 | 投资数量  
  
> 返回结果
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
      ]
    }
    

#### 返回参数

code = `0`代表请求已被成功处理

### POST / 赎回 

只能赎回资金账户中的 OKSOL 资产，交易账户中的 OKSOL 资产需要您先做资金划转到资金账户后赎回。

#### 限速：2次/s

#### 限速规则：User ID

#### HTTP 请求

`POST /api/v5/finance/staking-defi/sol/redeem`

> 请求示例
    
    
    POST /api/v5/finance/staking-defi/sol/redeem
    body 
    {
        "amt":"10"
    }
    
    
    
    import okx.Finance.SolStaking as SolStaking
    
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    StackingAPI = SolStaking.SolStakingAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StackingAPI.sol_redeem(amt="1")
    print(result)
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
amt | String | 是 | 赎回数量  
  
> 返回结果
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
      ]
    }
    

#### 返回参数

code = `0`代表请求已被成功处理

### GET / 获取余额 

该余额表示账户内 OKSOL 的实时总持仓，包括交易账户、资金账户以及处于赎回过程中的资产。

#### 限速：6 次/s

#### 限速规则：User ID

#### HTTP 请求

`GET /api/v5/finance/staking-defi/sol/balance`

> 请求示例
    
    
    GET /api/v5/finance/staking-defi/sol/balance
    
    
    
    
    import okx.Finance.SolStaking as SolStaking
    
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    StackingAPI = SolStaking.SolStakingAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StackingAPI.sol_balance()
    print(result)
    

#### 请求参数

None

> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "amt": "0.01100012",
                "ccy": "OKSOL",
                "latestInterestAccrual": "0.00000012",
                "totalInterestAccrual": "0.00000012"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ccy | String | 币种名称，如 `OKSOL`  
amt | String | 币种数量  
latestInterestAccrual | String | 最近收益  
totalInterestAccrual | String | 历史总收益  
  
### GET / 获取申购赎回记录 

#### 限速：6 次/s

#### 限速规则：User ID

#### HTTP 请求

`GET /api/v5/finance/staking-defi/sol/purchase-redeem-history`

> 请求示例
    
    
    GET /api/v5/finance/staking-defi/sol/purchase-redeem-history
    
    
    
    
    import okx.Finance.SolStaking as SolStaking
    
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    StackingAPI = SolStaking.SolStakingAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StackingAPI.sol_purchase_redeem_history()
    print(result)
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
type | String | 否 | 类型  
`purchase`：申购  
`redeem`：赎回  
status | String | 否 | 状态  
`pending`：处理中  
`success`：成功处理  
`failed`：处理失败  
after | String | 否 | 请求此`requestTime`之前（更旧的数据）的分页内容，值为时间戳，Unix 时间戳为毫秒数格式，如 `1597026383085`  
before | String | 否 | 请求此`requestTime`之后（更新的数据）的分页内容，值为时间戳，Unix 时间戳为毫秒数格式，如 `1597026383085`  
limit | String | 否 | 返回结果的数量，默认100条，最大值为100条  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "amt": "0.62666630",
                "completedTime": "1683413171000",
                "estCompletedTime": "",
                "redeemingAmt": "",
                "requestTime": "1683413171000",
                "status": "success",
                "type": "purchase"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
type | String | 类型  
`purchase`：申购  
`redeem`：赎回  
amt | String | 申购/赎回 的数量  
redeemingAmt | String | 赎回中的数量  
status | String | 状态  
`pending`：处理中  
`success`：成功处理  
`failed`：处理失败  
requestTime | String | 发起 申购/赎回 请求的时间，值为时间戳，Unix时间戳为毫秒数格式，如 `1597026383085`  
completedTime | String | 赎回请求处理完成的时间，值为时间戳，Unix时间戳为毫秒数格式，如 `1597026383085`  
estCompletedTime | String | 预估完成赎回的时间，值为时间戳，Unix时间戳为毫秒数格式，如 `1597026383085`  
  
### GET / 获取历史收益率(公共) 

公共接口无须鉴权

#### 限速：6次/s

#### 限速规则：IP

#### HTTP 请求

`GET /api/v5/finance/staking-defi/sol/apy-history`

> 请求示例
    
    
    GET /api/v5/finance/staking-defi/sol/apy-history?days=2
    
    
    
    
    import okx.Finance.SolStaking as SolStaking
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    StackingAPI = SolStaking.SolStakingAPI(flag=flag)
    
    result = StackingAPI.sol_apy_history(days="7")
    print(result)
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
days | String | 是 | 查询最近多少天内的数据，不超过365天  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "rate": "0.11280000",
                "ts": "1734192000000"
            },
            {
                "rate": "0.11270000",
                "ts": "1734105600000"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
rate | String | 年化收益率，如 `0.01`代表`1%`  
ts | String | 时间，值为时间戳，Unix时间戳为毫秒数格式，如 `1597026383085`  
  
## Stable Rewards 

OKX Stable Rewards 自动为持有合格稳定币（如 `USDG`）的用户每日发放奖励，启用后无需任何操作即可持续赚取收益。  
订阅时从资金账户扣款；收益及赎回默认结算至交易账户。

> **下线说明**
> 
> `POST /api/v5/finance/stable-rewards/quote`、`POST /api/v5/finance/stable-rewards/trade` 及 `GET /api/v5/finance/stable-rewards/subscribe-redeem-history` 接口已停用。如需交易 USDG 等稳定币，请使用标准[订单簿交易 API](/docs-v5/zh/#order-book-trading)。

### GET / 获取产品信息 

获取指定稳定币的产品信息，包括支持订阅/赎回的结算币种、适用手续费率、申购/赎回金额限制、每日配额以及当前赎回可用状态。

#### 限速：5次/2s

#### 限速规则：User ID

#### HTTP 请求

`GET /api/v5/finance/stable-rewards/product-info`

> 请求示例
    
    
    GET /api/v5/finance/stable-rewards/product-info?ccy=USDG
    

#### 请求参数

**参数名** | **类型** | **是否必须** | **描述**  
---|---|---|---  
ccy | String | 是 | 稳定币，如 `USDG`  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "details": [
                    {
                        "ccy": "USDG",
                        "settleCcy": "USDC",
                        "subFeeRate": "0.0003",
                        "redemptFeeRate": "0",
                        "minSubAmt": "1",
                        "minRedeemAmt": "0.0000001",
                        "remainingSubQuota": "1000000",
                        "remainingRedemptQuota": "500000",
                        "canRedeem": true
                    },
                    {
                        "ccy": "USDG",
                        "settleCcy": "USDT",
                        "subFeeRate": "0.0003",
                        "redemptFeeRate": "",
                        "minSubAmt": "1",
                        "minRedeemAmt": "",
                        "remainingSubQuota": "1000000",
                        "remainingRedemptQuota": "",
                        "canRedeem": false
                    }
                ],
                "ts": "1718035200000"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
details | Array of objects | 当前稳定币支持的结算币种及其订阅/赎回信息列表  
> ccy | String | 可订阅的稳定币，如 `USDG`  
> settleCcy | String | 可用于订阅 `ccy` 的结算币种，如 `USDC`、`USDT`  
> subFeeRate | String | 订阅手续费率，如 `0.01` 代表 `1%`  
> redemptFeeRate | String | 赎回手续费率，如 `0.01` 代表 `1%`  
当前 `settleCcy` 不支持赎回时返回 `""`  
> minSubAmt | String | 最小订阅数量，以 `settleCcy` 计价  
> minRedeemAmt | String | 最小赎回数量，以 `ccy` 计价  
当前 `settleCcy` 不支持赎回时返回 `""`  
> remainingSubQuota | String | 每日剩余订阅额度，按母账户 ID 统计  
`-1` 代表无上限  
> remainingRedemptQuota | String | 每日剩余赎回额度，按母账户 ID 统计  
`-1` 代表无上限  
当前 `settleCcy` 不支持赎回时返回 `""`  
> canRedeem | Boolean | 当前 `settleCcy` 是否支持赎回  
`true`：可赎回  
`false`：不可赎回  
ts | String | 数据查询时间，Unix 时间戳，单位为毫秒，如 `1597026383085`  
  
### GET / 获取余额 

查询 Stable Rewards 的实时余额，余额涵盖交易账户、资金账户以及正在赎回中的资产合计，同时返回累计收益与当前收益状态。

#### 限速：5次/2s

#### 限速规则：User ID

#### HTTP 请求

`GET /api/v5/finance/stable-rewards/balance`

> 请求示例
    
    
    GET /api/v5/finance/stable-rewards/balance?ccy=USDG
    

#### 请求参数

**参数名** | **类型** | **是否必须** | **描述**  
---|---|---|---  
ccy | String | 否 | 稳定币，如 `USDG`  
不传则返回全部支持的稳定币  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "details": [
                    {
                        "ccy": "USDG",
                        "amt": "100",
                        "totalEarnAccrual": "0.0003",
                        "state": "earning"
                    }
                ],
                "ts": "1718035200000"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
details | Array of objects | 按稳定币返回的实时余额明细  
> ccy | String | 稳定币，如 `USDG`  
> amt | String | 整个账户范围内的持有数量  
> totalEarnAccrual | String | 持有期间的累计收益  
> state | String | 收益状态  
`earning`：正在产生收益  
`pending`：未在产生收益（如自动赚币已关闭，或余额低于起息门槛）  
ts | String | 数据查询时间，Unix 时间戳，单位为毫秒，如 `1597026383085`  
  
### GET / 获取历史收益率 

查询指定稳定币的历史每日年化收益率。返回值为用户当前 VIP 等级对应的收益率。

#### 限速：6次/s

#### 限速规则：IP

#### HTTP 请求

`GET /api/v5/finance/stable-rewards/apy-history`

> 请求示例
    
    
    GET /api/v5/finance/stable-rewards/apy-history?ccy=USDG
    

#### 请求参数

**参数名** | **类型** | **是否必须** | **描述**  
---|---|---|---  
ccy | String | 是 | 稳定币，如 `USDG`  
days | String | 否 | 查询最近多少天的历史数据。默认 `100`，最大 `100`  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "rate": "0.004",
                "ts": "1718035200000"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
rate | String | 用户当前 VIP 等级对应的日度年化收益率，如 `0.041` 代表 `4.1%`  
ts | String | 数据快照时间（UTC+0），Unix 时间戳，单位为毫秒，如 `1597026383085`  
  
## OKUSD 

OKUSD 是 OKX 以 1:1 汇率发行的稳定币凭证，用户以 USDT 申购后持有即可享受每日收益，同时可用作交易账户保证金以提升资本效率。  
申购与赎回均在资金账户中操作。申购或赎回前可调用 `/limits` 接口查询当日剩余限额。

### GET / 查询限额 

查询您当日 OKUSD 申购剩余限额及即时/标准赎回剩余限额。所有限额均以母账户维度计算，子账户共享。

#### 限速：2次/2s

#### 限速规则：User ID

#### HTTP 请求

`GET /api/v5/finance/okusd/limits`

> 请求示例
    
    
    GET /api/v5/finance/okusd/limits
    

#### 请求参数

无

> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "subLimit": {
                    "maxSubAmt": "45000000",
                    "personalDailyLimit": "5000000",
                    "personalUsedAmt": "500000",
                    "platformDailyLimit": "50000000",
                    "platformUsedAmt": "5000000"
                },
                "fastRedeemLimit": {
                    "personalDailyLimit": "10000",
                    "personalUsedAmt": "0",
                    "platformDailyLimit": "5000000",
                    "platformUsedAmt": "1000000",
                    "feeRate": "0.001"
                },
                "stdRedeemLimit": {
                    "personalDailyLimit": "1000000",
                    "personalUsedAmt": "0",
                    "platformDailyLimit": "40000000",
                    "platformUsedAmt": "0",
                    "feeRate": "0.00025"
                },
                "ts": "1718500000000"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
subLimit | Object | 申购限额信息  
> maxSubAmt | String | 当日最大可申购数量（USDT），= min(personalDailyLimit - personalUsedAmt, platformDailyLimit - platformUsedAmt)，最小值为 `"0"`  
> personalDailyLimit | String | 根据您的 VIP 等级对应的每日申购上限（USDT）  
> personalUsedAmt | String | 您当日已申购金额（USDT）  
> platformDailyLimit | String | 平台每日申购总上限（USDT）  
> platformUsedAmt | String | 平台当日已申购总金额（USDT）  
fastRedeemLimit | Object | 即时赎回限额信息（实时到账）  
> personalDailyLimit | String | 根据您的 VIP 等级对应的每日即时赎回上限（OKUSD）  
> personalUsedAmt | String | 您当日已使用的即时赎回额度（OKUSD）  
> platformDailyLimit | String | 平台每日即时赎回总上限（OKUSD）  
> platformUsedAmt | String | 平台当日已使用的即时赎回额度（OKUSD）  
> feeRate | String | 即时赎回手续费率  
stdRedeemLimit | Object | 标准赎回限额信息  
> personalDailyLimit | String | 根据您的 VIP 等级对应的每日标准赎回上限（OKUSD）  
> personalUsedAmt | String | 您当日已使用的标准赎回额度（OKUSD）  
> platformDailyLimit | String | 平台每日标准赎回总上限（OKUSD）  
> platformUsedAmt | String | 平台当日已使用的标准赎回额度（OKUSD）  
> feeRate | String | 标准赎回手续费率  
ts | String | 服务器时间戳，Unix 时间戳，单位为毫秒，如 `1597026383085`  
  
### POST / 申购 OKUSD 

以 1:1 汇率将 USDT 申购为 OKUSD，无申购手续费，OKUSD 即时到账至资金账户。每次请求需传入唯一的 `clOrdId`；重复提交相同 `clOrdId` 将直接返回原始订单，不重复执行申购。

#### 限速：1次/2s

#### 限速规则：User ID

#### HTTP 请求

`POST /api/v5/finance/okusd/subscribe`

> 请求示例
    
    
    POST /api/v5/finance/okusd/subscribe
    body
    {
        "amt": "1000.00000000",
        "clOrdId": "my-sub-001"
    }
    

#### 请求参数

**参数名** | **类型** | **是否必须** | **描述**  
---|---|---|---  
amt | String | 是 | 申购 USDT 数量。最小值：`1`。最多 8 位小数。不支持科学计数法  
clOrdId | String | 是 | 客户自定义订单 ID，最多 32 字符（字母、数字、`-`、`_`）。同一 UID 下不可重复，用于订单追踪与幂等标识  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "ordId": "680012345678901234",
                "clOrdId": "my-sub-001",
                "ccy": "USDT",
                "amt": "1000.00000000",
                "okusdAmt": "1000.00000000",
                "state": "success",
                "ts": "1718500000000"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
ordId | String | 系统订单 ID  
clOrdId | String | 客户自定义订单 ID（原样返回）  
ccy | String | 申购货币，固定为 `"USDT"`  
amt | String | 实际申购 USDT 数量  
okusdAmt | String | 到账 OKUSD 数量（= `amt`，汇率 1:1，无申购手续费），到账至资金账户  
state | String | 订单状态：`"success"` / `"pending"` / `"failed"`  
ts | String | 订单创建时间，Unix 时间戳，单位为毫秒，如 `1597026383085`  
  
### POST / 赎回 OKUSD 

将 OKUSD 赎回为 USDT。支持即时赎回（实时到账）和标准赎回（D+5 或 D+6 自然日，取决于提交时间）。各类型手续费率请调用 `GET /limits` 查询。所有手续费均向下截断（floor）至 8 位小数。每次请求需传入唯一的 `clOrdId`；重复提交相同 `clOrdId` 将直接返回原始订单，不重复执行赎回。

#### 限速：1次/2s

#### 限速规则：User ID

#### HTTP 请求

`POST /api/v5/finance/okusd/redeem`

> 请求示例（即时赎回）
    
    
    POST /api/v5/finance/okusd/redeem
    body
    {
        "amt": "1000.00000000",
        "redeemType": "1",
        "clOrdId": "my-redeem-001"
    }
    

#### 请求参数

**参数名** | **类型** | **是否必须** | **描述**  
---|---|---|---  
amt | String | 是 | 赎回 OKUSD 数量。最小值：`1`。最多 8 位小数。不支持科学计数法  
redeemType | String | 是 | 赎回类型。`"1"`：即时赎回（实时到账）；`"2"`：标准赎回（UTC+8 16:00 前提交加 5 自然日，16:00 后（含）提交加 6 自然日）。各类型手续费率请参考 `/limits` 接口返回的 `feeRate` 字段  
clOrdId | String | 是 | 客户自定义订单 ID，最多 32 字符（字母、数字、`-`、`_`）。同一 UID 下不可重复，用于订单追踪与幂等标识  
  
> 返回结果（即时赎回）
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "ordId": "680012345678905678",
                "clOrdId": "my-redeem-001",
                "ccy": "OKUSD",
                "amt": "1000.00000000",
                "fee": "1.00000000",
                "usdtAmt": "999.00000000",
                "redeemType": "1",
                "state": "success",
                "estSettlementTime": "1718500010000",
                "ts": "1718500000000"
            }
        ]
    }
    

> 返回结果（标准赎回）
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "ordId": "680012345678906789",
                "clOrdId": "my-redeem-002",
                "ccy": "OKUSD",
                "amt": "50000.00000000",
                "fee": "12.50000000",
                "usdtAmt": "49987.50000000",
                "redeemType": "2",
                "state": "processing",
                "estSettlementTime": "1718932800000",
                "ts": "1718500000000"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
ordId | String | 系统订单 ID  
clOrdId | String | 客户自定义订单 ID（原样返回）  
ccy | String | 赎回货币，固定为 `"OKUSD"`  
amt | String | 赎回 OKUSD 数量  
fee | String | 实收手续费（USDT），向下截断至 8 位小数  
usdtAmt | String | 实际到账 USDT 数量（`amt - fee`，向下截断至 8 位小数），到账至资金账户  
redeemType | String | 赎回类型：`"1"`（即时）或 `"2"`（标准）  
state | String | 订单状态：`"processing"` / `"success"` / `"failed"` / `"cancelled"`  
estSettlementTime | String | 预计到账时间，Unix 时间戳，单位为毫秒。即时赎回为当前时间；标准赎回：UTC+8 16:00 前提交加 5 自然日，16:00 后（含）提交加 6 自然日  
ts | String | 订单创建时间，Unix 时间戳，单位为毫秒，如 `1597026383085`  
  
### GET / 查询账户余额及累计收益 

查询您当前的 OKUSD 余额及持仓期间累计收益。所有余额均以母账户维度聚合，子账户共享。

#### 限速：2次/2s

#### 限速规则：User ID

#### Permission: Read

#### HTTP 请求

`GET /api/v5/finance/okusd/account`

> 请求示例
    
    
    GET /api/v5/finance/okusd/account
    

#### 请求参数

无

> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "ccy": "OKUSD",
                "amt": "10000.00000000",
                "totalEarnAccrual": "123.45678900",
                "ts": "1718500000000"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
ccy | String | 持仓货币，固定为 `"OKUSD"`  
amt | String | 当前 OKUSD 余额  
totalEarnAccrual | String | 持仓期间累计收益（USDT）  
ts | String | 服务器时间戳，Unix 时间戳，单位为毫秒，如 `1597026383085`  
  
### GET / 查询申购历史 

查询您的 OKUSD 申购历史订单。结果按时间戳倒序返回（最新优先），支持时间范围过滤。

#### 限速：5次/2s

#### 限速规则：User ID

#### Permission: Read

#### HTTP 请求

`GET /api/v5/finance/okusd/subscribe/history`

> 请求示例
    
    
    GET /api/v5/finance/okusd/subscribe/history?limit=2
    

#### 请求参数

**参数名** | **类型** | **是否必须** | **描述**  
---|---|---|---  
limit | String | 否 | 每页返回条数，默认 `"100"`，最大 `"100"`  
begin | String | 否 | 起始时间过滤（订单创建时间 `ts`，Unix ms，含）  
end | String | 否 | 结束时间过滤（订单创建时间 `ts`，Unix ms，含）  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "ordId": "680012345678901234",
                "clOrdId": "my-sub-001",
                "ccy": "USDT",
                "amt": "1000.00000000",
                "settleCcy": "OKUSD",
                "settleCcyAmt": "1000.00000000",
                "status": "success",
                "ts": "1718500000000"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
ordId | String | 系统订单 ID  
clOrdId | String | 客户自定义订单 ID（原样返回；未传则为空字符串）  
ccy | String | 申购货币，固定为 `"USDT"`  
amt | String | 申购 USDT 数量  
settleCcy | String | 到账货币，固定为 `"OKUSD"`  
settleCcyAmt | String | 到账 OKUSD 数量（= `amt`，汇率 1:1）  
status | String | 订单终态：`"success"` / `"failed"`  
ts | String | 订单创建时间，Unix 时间戳，单位为毫秒，如 `1597026383085`  
  
### GET / 查询赎回历史 

查询您的 OKUSD 赎回历史订单。结果按时间戳倒序返回（最新优先），支持时间范围过滤及赎回类型过滤。

#### 限速：5次/2s

#### 限速规则：User ID

#### Permission: Read

#### HTTP 请求

`GET /api/v5/finance/okusd/redeem/history`

> 请求示例
    
    
    GET /api/v5/finance/okusd/redeem/history?type=fast
    

#### 请求参数

**参数名** | **类型** | **是否必须** | **描述**  
---|---|---|---  
limit | String | 否 | 每页返回条数，默认 `"100"`，最大 `"100"`  
begin | String | 否 | 起始时间过滤（订单创建时间 `ts`，Unix ms，含）  
end | String | 否 | 结束时间过滤（订单创建时间 `ts`，Unix ms，含）  
type | String | 否 | 赎回类型过滤：`"fast"` 仅返回即时赎回；`"standard"` 仅返回标准赎回；不传默认返回标准赎回  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "ordId": "680012345678905678",
                "clOrdId": "my-rdm-fast-001",
                "ccy": "OKUSD",
                "amt": "1000.00000000",
                "fee": "1.00000000",
                "settleCcy": "USDT",
                "settleCcyAmt": "999.00000000",
                "type": "fast",
                "status": "success",
                "estSettlementTime": "1718500010000",
                "ts": "1718500000000"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
ordId | String | 系统订单 ID  
clOrdId | String | 客户自定义订单 ID（原样返回；未传则为空字符串）  
ccy | String | 赎回货币，固定为 `"OKUSD"`  
amt | String | 赎回 OKUSD 数量  
fee | String | 实收手续费（USDT），向下截断至 8 位小数  
settleCcy | String | 到账货币，固定为 `"USDT"`  
settleCcyAmt | String | 实际到账 USDT 数量（`amt - fee`，向下截断至 8 位小数）  
type | String | 赎回类型：`"fast"`（即时赎回）或 `"standard"`（标准赎回，D+5/D+6 自然日）  
status | String | 订单状态：`"pending"` / `"success"` / `"failed"` / `"canceled"`  
estSettlementTime | String | 预计到账时间，Unix 时间戳，单位为毫秒。已结算的即时赎回订单返回空字符串  
ts | String | 订单创建时间，Unix 时间戳，单位为毫秒，如 `1597026383085`  
  
### GET / 查询收益发放历史 

查询您的 OKUSD 每日收益发放历史。结果按时间戳倒序返回（最新优先）。

#### 限速：5次/2s

#### 限速规则：User ID

#### Permission: Read

#### HTTP 请求

`GET /api/v5/finance/okusd/rewards/history`

> 请求示例
    
    
    GET /api/v5/finance/okusd/rewards/history?limit=7
    

#### 请求参数

**参数名** | **类型** | **是否必须** | **描述**  
---|---|---|---  
limit | String | 否 | 每页返回条数，默认 `"30"`，最大 `"100"`  
begin | String | 否 | 起始时间过滤（`ts`，Unix ms，含），最大查询跨度 6 个月  
end | String | 否 | 结束时间过滤（`ts`，Unix ms，含），不传默认取当前时间  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "ccy": "USDT",
                "earnAmt": "1.14246575",
                "amt": "10000.00000000",
                "apr": "0.0418",
                "ts": "1718500000000"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
ccy | String | 收益货币，固定为 `"USDT"`  
earnAmt | String | 本次发放的 USDT 收益数量  
amt | String | 发放时点用户 USDT 本金余额  
apr | String | 本次发放适用的 APR，如 `"0.0418"` 表示 4.18%  
ts | String | 发放时间戳，Unix 时间戳，单位为毫秒，如 `1597026383085`  
  
### GET / 查询 APR 历史 

查询 OKUSD 历史 APR 快照。结果按时间戳倒序返回（最新优先）。虽然数据为产品级（非用户维度），本接口仍需 API Key 鉴权。

#### 限速：5次/2s

#### 限速规则：User ID

#### Permission: Read

#### HTTP 请求

`GET /api/v5/finance/okusd/rate/history`

> 请求示例
    
    
    GET /api/v5/finance/okusd/rate/history?limit=10
    

#### 请求参数

**参数名** | **类型** | **是否必须** | **描述**  
---|---|---|---  
limit | String | 否 | 每页返回条数，默认 `"30"`，最大 `"100"`  
begin | String | 否 | 起始时间过滤（`ts`，Unix ms，含），最大查询跨度 6 个月  
end | String | 否 | 结束时间过滤（`ts`，Unix ms，含），不传默认取当前时间  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            { "apr": "0.0418", "ts": "1718500000000" },
            { "apr": "0.0395", "ts": "1718413600000" }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
apr | String | 该快照时刻的 OKUSD APR，如 `"0.0418"` 表示 4.18%  
ts | String | 快照时间戳，Unix 时间戳，单位为毫秒，如 `1597026383085`  
  
## 活期简单赚币 

活期简单赚币通过在借贷市场出借给杠杆交易用户获取收益。[了解更多](/cn/earn/simple-earn)

### GET / 获取活期简单赚币余额 

#### 限速：6次/s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/finance/savings/balance`

> 请求示例
    
    
    GET /api/v5/finance/savings/balance?ccy=BTC
    
    
    
    
    import okx.Finance.Savings as Savings
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    SavingsAPI = Savings.SavingsAPI(apikey, secretkey, passphrase, False, flag)
    
    result = SavingsAPI.get_saving_balance(ccy="USDT")
    print(result)
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 否 | 币种，如 `BTC`  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg":"",
        "data": [
            {
                "earnings": "0.0010737388791526",
                "redemptAmt": "",
                "rate": "0.0100000000000000",
                "ccy": "USDT",
                "amt": "11.0010737453457821",
                "loanAmt": "11.0010630707982819",
                "pendingAmt": "0.0000106745475002"
            }
        ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ccy | String | 币种，如 `BTC`  
amt | String | 币种数量  
earnings | String | 币种持仓收益  
rate | String | 用户配置的最低年化出借利率  
loanAmt | String | 已出借数量  
pendingAmt | String | 未出借数量  
redemptAmt | String | ~~赎回中的数量~~ （已废弃）  
  
### POST / 活期简单赚币申购/赎回 

仅资金账户中的资产支持活期简单赚币申购。

#### 限速：6次/s

#### 限速规则：User ID

#### HTTP请求

`POST /api/v5/finance/savings/purchase-redempt`

> 请求示例
    
    
    POST /api/v5/finance/savings/purchase-redempt
    body
    {
        "ccy":"BTC",
        "amt":"1",
        "side":"purchase",
        "rate":"0.01"
    }
    
    
    
    
    import okx.Finance.Savings as Savings
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    SavingsAPI = Savings.SavingsAPI(apikey, secretkey, passphrase, False, flag)
    
    result = SavingsAPI.savings_purchase_redemption(ccy='USDT',amt="0.1",side="purchase",rate="1")
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 是 | 币种名称，如 `BTC`  
amt | String | 是 | 申购/赎回 数量  
side | String | 是 | 操作类型  
`purchase`：申购 `redempt`：赎回  
rate | String | 可选 | 申购年利率，如 `0.1`代表`10%`  
仅适用于申购，新申购的利率会覆盖上次申购的利率  
参数取值范围在1%到365%之间  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "ccy":"BTC",
                "amt":"1",
                "side":"purchase",
                "rate":"0.01"
            }
        ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ccy | String | 币种名称  
amt | String | 申购/赎回 数量  
side | String | 操作类型  
rate | String | 申购年利率，如 `0.1`代表`10%`  
  
### POST / 设置活期简单赚币借贷利率 

#### 限速：6次/s

#### 限速规则：User ID

#### HTTP请求

`POST /api/v5/finance/savings/set-lending-rate`

> 请求示例
    
    
    POST /api/v5/finance/savings/set-lending-rate
    body
    {
        "ccy":"BTC",
        "rate":"0.02"
    }
    
    
    
    
    import okx.Finance.Savings as Savings
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    SavingsAPI = Savings.SavingsAPI(apikey, secretkey, passphrase, False, flag)
    
    result = SavingsAPI.set_lending_rate(ccy='USDT',rate="1")
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 是 | 币种名称，如 `BTC`  
rate | String | 是 | 贷出年利率  
参数取值范围在1%到365%之间  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
            "ccy": "BTC",
            "rate": "0.02"
        }]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ccy | String | 币种名称，如 `BTC`  
rate | String | 贷出年利率  
  
### GET / 获取活期简单赚币出借明细 

返回最近一个月的数据

#### 限速：6次/s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/finance/savings/lending-history`

> 请求示例
    
    
    GET /api/v5/finance/savings/lending-history
    
    
    
    
    import okx.Finance.Savings as Savings
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    SavingsAPI = Savings.SavingsAPI(apikey, secretkey, passphrase, False, flag)
    
    result = SavingsAPI.get_lending_history()
    print(result)
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 否 | 币种，如 `BTC`  
after | String | 否 | 查询在此之前的内容，值为时间戳，Unix 时间戳为毫秒数格式，如 `1597026383085`  
before | String | 否 | 查询在此之后的内容，值为时间戳，Unix 时间戳为毫秒数格式，如 `1597026383085`  
limit | String | 否 | 分页返回的结果集数量，最大为 100，不填默认返回 100 条  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
                "ccy": "BTC",
                "amt": "0.01",
                "earnings": "0.001",
                "rate": "0.01",
                "ts": "1597026383085"
            },
            {
                "ccy": "ETH",
                "amt": "0.2",
                "earnings": "0.001",
                "rate": "0.01",
                "ts": "1597026383085"
            }
        ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ccy | String | 币种，如 `BTC`  
amt | String | 出借数量  
earnings | String | 已赚取利息  
rate | String | 出借年利率  
ts | String | 出借时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
  
### GET / 获取市场借贷信息（公共）

公共接口无须鉴权

#### 限速：6次/s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/finance/savings/lending-rate-summary`

> 请求示例
    
    
    GET /api/v5/finance/savings/lending-rate-summary
    
    
    
    
    import okx.Finance.Savings as Savings
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    SavingsAPI = Savings.SavingsAPI(flag=flag)
    
    result = SavingsAPI.get_public_borrow_info()
    print(result)
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 否 | 币种，如 `BTC`  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
            "ccy": "BTC",
            "avgAmt": "10000",
            "avgAmtUsd": "10000000000",
            "avgRate": "0.03",
            "preRate": "0.02",
            "estRate": "0.01"
        }]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ccy | String | 币种，如 `BTC`  
avgAmt | String | ~~过去24小时平均借贷量~~(已弃用)  
avgAmtUsd | String | ~~过去24小时平均借贷美元价值~~(已弃用)  
avgRate | String | 过去24小时平均借入年利率  
preRate | String | 上一次借入年利率  
estRate | String | 下一次预估借入年利率  
  
### GET / 获取市场借贷历史（公共） 

公共接口无须鉴权  
返回2021年12月14日后的记录  

#### 限速：6次/s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/finance/savings/lending-rate-history`

> 请求示例
    
    
    GET /api/v5/finance/savings/lending-rate-history
    
    
    
    
    import okx.Finance.Savings as Savings
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    SavingsAPI = Savings.SavingsAPI(flag=flag)
    
    result = SavingsAPI.get_public_borrow_history()
    print(result)
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 否 | 币种，如 `BTC`  
after | String | 否 | 查询在此之前的内容，值为时间戳，Unix 时间戳为毫秒数格式，如 `1597026383085`  
before | String | 否 | 查询在此之后的内容，值为时间戳，Unix 时间戳为毫秒数格式，如 `1597026383085`  
limit | String | 否 | 分页返回的结果集数量，最大为100，不填默认返回100条  
如果不指定`ccy`,会返回同一个`ts`下的全部数据，不受`limit`限制  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
            "ccy": "BTC",
            "amt": "0.01",
            "rate": "0.001",
            "lendingRate": "0.001",
            "ts": "1597026383085"
        }]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ccy | String | 币种，如 `BTC`  
amt | String | ~~市场总出借数量~~ （已弃用）  
rate | String | 出借年利率  
lendingRate | String | 年化出借利率  
ts | String | 时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
  
## 活期借币 

欧易活期借币是一款高端借贷产品，用户无需变卖数字货币即可增加现金流。[了解更多](/loan)

### GET / 可借币种列表 

获取可借币种列表

#### 限速：5次/2s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/finance/flexible-loan/borrow-currencies`

> 请求示例
    
    
    GET /api/v5/finance/flexible-loan/borrow-currencies
    
    
    
    from okx.Finance import FlexibleLoan
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    flexibleLoanAPI = FlexibleLoan.FlexibleLoanAPI(apikey, secretkey, passphrase, False, flag)
    result = flexibleLoanAPI.borrow_currencies()
    print(result)
    

> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "borrowCcy": "USDT"
            },
            {
                "borrowCcy": "USDC"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
borrowCcy | String | 可借币种，如 `BTC`  
  
### GET / 可抵押资产 

获取可抵押资产信息（仅支持资金账户中的资产）

#### 限速：5次/2s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/finance/flexible-loan/collateral-assets`

> 请求示例
    
    
    GET /api/v5/finance/flexible-loan/collateral-assets?ordId=12345
    
    
    
    from okx.Finance import FlexibleLoan
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    flexibleLoanAPI = FlexibleLoan.FlexibleLoanAPI(apikey, secretkey, passphrase, False, flag)
    result = flexibleLoanAPI.collateral_assets(ordId="12345")
    print(result)
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 否 | 币种，如 `BTC`  
ordId | String | 否 | 活期借币订单 ID。  
如果不传 `ordId`，系统将默认对起始时间最早的现存订单进行操作。  
如果没有现存订单，系统将返回空数据。  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "assets": [
                    {
                        "amt": "1.7921483143067599",
                        "ccy": "BTC",
                        "notionalUsd": "158292.621793314105231"
                    },
                    {
                        "amt": "1.9400755578876945",
                        "ccy": "ETH",
                        "notionalUsd": "6325.6652712507628946"
                    },
                    {
                        "amt": "63.9795959720319628",
                        "ccy": "USDT",
                        "notionalUsd": "64.3650372635940345"
                    }
                ]
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
assets | Array of objects | 可抵押资产信息  
> ccy | String | 币种，如 `BTC`  
> amt | String | 可用数量  
> notionalUsd | String | 可抵押资产的美金价值  
  
### POST / 最大可借 

#### 限速：5次/2s

#### 限速规则：User ID

#### HTTP请求

`POST /api/v5/finance/flexible-loan/max-loan`

> 请求示例
    
    
    POST /api/v5/finance/flexible-loan/max-loan
    body
    {
        "ordId": "12345",
        "borrowCcy": "USDT"
    }
    
    
    
    
    from okx.Finance import FlexibleLoan
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    flexibleLoanAPI = FlexibleLoan.FlexibleLoanAPI(apikey, secretkey, passphrase, False, flag)
    result = flexibleLoanAPI.max_loan(ordId="12345", borrowCcy="USDT")
    print(result)
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
borrowCcy | String | 是 | 借币币种，如 `USDT`  
ordId | String | 否 | 活期借币订单 ID。  
如果不传 `ordId`，系统将默认对起始时间最早的现存订单进行操作。  
如果没有现存订单，系统将返回空数据。  
supCollateral | Array of objects | 否 | 补充抵押资产信息  
> ccy | String | 是 | 币种，如 `BTC`  
> amt | String | 是 | 数量  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "borrowCcy": "USDT",
                "maxLoan": "0.01113",
                "notionalUsd": "0.01113356",
                "remainingQuota": "3395000"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
borrowCcy | String | 借币币种，如 `USDT`  
maxLoan | String | 最大可借数量  
notionalUsd | String | 最大可借美元价值  
remainingQuota | String | 剩余可借额度，单位为`borrowCcy`  
  
### GET / 抵押物最大可赎回数量 

#### 限速：5次/2s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/finance/flexible-loan/max-collateral-redeem-amount`

> 请求示例
    
    
    GET /api/v5/finance/flexible-loan/max-collateral-redeem-amount?ccy=USDT&ordId=12345
    
    
    
    
    from okx.Finance import FlexibleLoan
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    flexibleLoanAPI = FlexibleLoan.FlexibleLoanAPI(apikey, secretkey, passphrase, False, flag)
    result = flexibleLoanAPI.max_collateral_redeem_amount(ordId="12345", ccy="USDT")
    print(result)
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 是 | 抵押物币种，如 `USDT`  
ordId | String | 否 | 活期借币订单 ID。  
如果不传 `ordId`，系统将默认对起始时间最早的现存订单进行操作。  
如果没有现存订单，系统将返回空数据。  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "ccy": "USDT",
                "maxRedeemAmt": "1"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
ccy | String | 抵押物币种，如 `USDT`  
maxRedeemAmt | String | 抵押物最大可赎回数量  
  
### POST / 调整抵押物 

#### 限速：5次/2s

#### 限速规则：User ID

#### HTTP请求

`POST /api/v5/finance/flexible-loan/adjust-collateral`

> 请求示例
    
    
    POST /api/v5/finance/flexible-loan/adjust-collateral
    body
    {
        "type":"add",
        "ordId": "12345",
        "collateralCcy": "BTC",
        "collateralAmt": "0.1"
    }
    
    
    
    
    from okx.Finance import FlexibleLoan
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    flexibleLoanAPI = FlexibleLoan.FlexibleLoanAPI(apikey, secretkey, passphrase, False, flag)
    result = flexibleLoanAPI.adjust_collateral(type="add", ordId="12345", collateralCcy="USDT", collateralAmt="1")
    print(result)
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
type | String | 是 | 操作类型  
`add`：补充抵押物  
`reduce`：减少抵押物  
collateralCcy | String | 是 | 抵押物币种，如 `BTC`  
collateralAmt | String | 是 | 抵押物数量  
ordId | String | 否 | 活期借币订单 ID。  
如果不传 `ordId`，系统将默认对起始时间最早的现存订单进行操作。  
如果没有现存订单，系统将返回错误 `51063`  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
        ],
        "msg": ""
    }
    

#### 返回参数

code = `0` 代表请求已被接受(不代表处理成功)

### GET / 借贷信息 

#### 限速：5次/2s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/finance/flexible-loan/loan-info`

> 请求示例
    
    
    GET /api/v5/finance/flexible-loan/loan-info
    
    
    
    from okx.Finance import FlexibleLoan
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    flexibleLoanAPI = FlexibleLoan.FlexibleLoanAPI(apikey, secretkey, passphrase, False, flag)
    result = flexibleLoanAPI.loan_info()
    print(result)
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
ordId | String | 否 | 活期借币订单 ID。  
如果不传 `ordId`，系统将返回所有现存订单数据  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "ordId": "12345",
                "collateralData": [
                    {
                        "amt": "0.0000097",
                        "ccy": "COMP"
                    },
                    {
                        "amt": "0.78",
                        "ccy": "STX"
                    },
                    {
                        "amt": "0.001",
                        "ccy": "DOT"
                    },
                    {
                        "amt": "0.05357864",
                        "ccy": "LUNA"
                    }
                ],
                "collateralNotionalUsd": "1.5078763",
                "curLTV": "0.5742",
                "liqLTV": "0.8374",
                "loanData": [
                    {
                        "amt": "0.86590608",
                        "ccy": "USDC"
                    }
                ],
                "loanNotionalUsd": "0.8661285",
                "marginCallLTV": "0.7374",
                "riskWarningData": {
                    "instId": "",
                    "liqPx": ""
                }
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
ordId | String | 订单 ID  
loanNotionalUsd | String | 借币资产美金价值  
loanData | Array of objects | 借币数据  
> ccy | String | 借贷币种  
> amt | String | 借贷数量  
collateralNotionalUsd | String | 调整后的抵押物美金价值  
collateralData | Array of objects | 抵押资产数据  
> ccy | String | 抵押币种  
> amt | String | 抵押数量  
riskWarningData | Object | 风险预警信息  
> instId | String | 清算交易产品，如 `BTC-USDT`  
仅当质押物和借币都只有一种时，该字段有效。其他情况返回""。  
> liqPx | String | 清算价格  
清算价格的单位为交易产品的计价币，如 `BTC-USDT`中的`USDT`。  
仅当质押物和借币都只有一种时，该字段有效。其他情况返回""。  
curLTV | String | 当前质押率，如 `0.1`代表`10%`  
注：LTV(Loan-to-Value，贷款价值比)  
marginCallLTV | String | 预警质押率，如 `0.1`代表`10%`  
您的质押率达到预警质押率时，系统将会提示您当前质押率过高，即将触发强平。  
liqLTV | String | 强平质押率，如 `0.1`代表`10%`  
若您的借贷达到强平质押率并被强平，您将损失质押物及已完成的还款。  
  
### GET / 借贷历史 

#### 限速：5次/2s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/finance/flexible-loan/loan-history`

> 请求示例
    
    
    GET /api/v5/finance/flexible-loan/loan-history
    
    
    
    from okx.Finance import FlexibleLoan
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    flexibleLoanAPI = FlexibleLoan.FlexibleLoanAPI(apikey, secretkey, passphrase, False, flag)
    result = flexibleLoanAPI.loan_history()
    print(result)
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
type | String | 否 | 操作类型  
`borrowed`：借入  
`repaid`：还币  
`collateral_locked`：锁定质押物  
`collateral_released`：释放质押物  
`forced_repayment_buy`：自动换币买入  
`forced_repayment_sell`：自动换币卖出  
`forced_liquidation`：强制平仓  
`partial_liquidation`：强制减仓  
`sell_collateral`：卖出质押资产  
`buy_transition_coin`：购买中介币种  
`sell_transition_coin`：卖出中介币种  
`buy_borrowed_coin`：购买借币币种  
after | String | 否 | 请求此 ID 之前（更旧的数据）的分页内容，传的值为对应接口的`refId`（不包含）  
before | String | 否 | 请求此 ID 之后（更新的数据）的分页内容，传的值为对应接口的`refId`（不包含）  
limit | String | 否 | 返回结果的数量，最大为`100`，默认`100`条  
ordId | String | 否 | 活期借币订单 ID。  
如果不传 `ordId`，系统将返回所有订单数据  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "amt": "-0.001",
                "ccy": "DOT",
                "refId": "17316594851045086",
                "ts": "1731659485000",
                "type": "collateral_locked"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
refId | String | 对应记录ID  
type | String | 操作类型  
ccy | String | 币种，如 `BTC`  
amt | String | 数量  
ts | String | 操作发生时间，Unix 时间戳为毫秒数格式，如 `1597026383085`  
  
### GET / 计息记录 

获取最近30天的计息记录。

#### 限速：5次/2s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/finance/flexible-loan/interest-accrued`

> 请求示例
    
    
    GET /api/v5/finance/flexible-loan/interest-accrued
    
    
    
    from okx.Finance import FlexibleLoan
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    flexibleLoanAPI = FlexibleLoan.FlexibleLoanAPI(apikey, secretkey, passphrase, False, flag)
    result = flexibleLoanAPI.interest_accrued()
    print(result)
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 否 | 借贷币种，如 `BTC`  
after | String | 否 | 请求此 ID 之前（更旧的数据）的分页内容，传的值为对应接口的`refId`（不包含）  
before | String | 否 | 请求此 ID 之后（更新的数据）的分页内容，传的值为对应接口的`refId`（不包含）  
limit | String | 否 | 返回结果的数量，最大为`100`，默认`100`条  
ordId | String | 否 | 活期借币订单 ID。  
如果不传 `ordId`，系统将返回所有订单数据  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "ccy": "USDC",
                "interest": "0.00004054",
                "interestRate": "0.41",
                "loan": "0.86599309",
                "refId": "17319133035195744",
                "ts": "1731913200000"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
refId | String | 对应记录ID  
ccy | String | 币种，如 `BTC`  
loan | String | 计息时负债  
interest | String | 利息  
interestRate | String | 年化利率，如 `0.01`代表`1%`  
ts | String | 计息时间，Unix 时间戳为毫秒数格式，如 `1597026383085`  
  
## 双币赢 

### GET / 获取币对 

获取双币赢币对

#### 限速：1次/s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/finance/sfp/dcd/currency-pair`

> 请求示例
    
    
    GET /api/v5/finance/sfp/dcd/currency-pair
    

#### 请求参数

无

> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "baseCcy": "BTC",
                "quoteCcy": "USDT",
                "optType": "C",
                "uly": "BTC-USD"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
baseCcy | String | 基础币种  
quoteCcy | String | 报价币种  
optType | String | 期权类型  
`C`：看涨  
`P`：看跌  
uly | String | 标的  
  
### GET / 获取产品信息 

获取双币赢产品列表

#### 限速：1次/s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/finance/sfp/dcd/products`

> 请求示例
    
    
    GET /api/v5/finance/sfp/dcd/products?baseCcy=BTC&quoteCcy=USDT&optType=C
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
baseCcy | String | 是 | 基础币种  
quoteCcy | String | 是 | 报价币种  
optType | String | 是 | 期权类型  
`C`：看涨  
`P`：看跌  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "absYield": "0.00232413",
                "annualizedYield": "0.0541",
                "baseCcy": "BTC",
                "quoteCcy": "USDT",
                "expTime": "1774598400000",
                "interestAccrualTime": "1773244800000",
                "listTime": "1743150759000",
                "maxSize": "6000000",
                "minSize": "10",
                "notionalCcy": "USDT",
                "optType": "P",
                "productId": "BTC-USDT-260327-54500-P",
                "quoteTime": "1773243808703",
                "redeemEndTime": "1774594800000",
                "redeemStartTime": "1773244800000",
                "stepSz": "1",
                "tradeEndTime": "1774584000000",
                "strike": "54500",
                "uly": "BTC-USD"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
absYield | String | 绝对收益率  
annualizedYield | String | 年化收益率  
baseCcy | String | 基础币种  
quoteCcy | String | 报价币种  
notionalCcy | String | 投资币种。若 `C`，则为 baseCcy；若 `P`，则为 quoteCcy。  
expTime | String | 到期时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
interestAccrualTime | String | 利息开始计算时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
listTime | String | 产品上架时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
minSize | String | 最小交易规模（以投资币种计）  
maxSize | String | 最大交易规模（以投资币种计）  
optType | String | 期权类型  
`C`：看涨  
`P`：看跌  
productId | String | 产品ID  
quoteTime | String | 产品报价时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
redeemStartTime | String | 最早可申请提前赎回的时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
redeemEndTime | String | 最晚可申请提前赎回的时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
stepSz | String | 交易步长（以投资币种计）  
tradeEndTime | String | 交易截止时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
uly | String | 标的  
strike | String | 行权价  
  
### POST / 获取报价 

为双币赢产品请求实时报价。报价有有效期，须在到期前使用。

#### 限速：10次/60s

#### 限速规则：User ID

#### HTTP请求

`POST /api/v5/finance/sfp/dcd/quote`

> 请求示例
    
    
    POST /api/v5/finance/sfp/dcd/quote
    body
    {
        "productId": "BTC-USDT-260327-77000-C",
        "notionalSz": "1.5",
        "notionalCcy": "BTC"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
productId | String | 是 | 产品ID  
notionalSz | String | 是 | 投资数量  
notionalCcy | String | 是 | 投资币种  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "absYield": "0.00135182",
                "annualizedYield": "69.65",
                "interestAccrualTime": "1773241200000",
                "notionalSz": "0.001",
                "notionalCcy": "BTC",
                "productId": "BTC-USDT-260312-72000-C",
                "quoteId": "qtbcDCD-QUOTE17732395560537636",
                "validUntil": "1774584000000",
                "idxPx": "69000"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
absYield | String | 绝对收益率  
annualizedYield | String | 年化收益率  
interestAccrualTime | String | 利息开始计算时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
notionalSz | String | 投资数量  
notionalCcy | String | 投资币种  
productId | String | 产品ID  
quoteId | String | 报价ID  
validUntil | String | 报价有效期，Unix时间戳的毫秒数格式，如 `1597026383085`  
idxPx | String | 指数价格  
  
### POST / 下单 

使用有效报价下单双币赢。

#### 限速：2次/60s

#### 限速规则：User ID

#### HTTP请求

`POST /api/v5/finance/sfp/dcd/trade`

> 请求示例
    
    
    POST /api/v5/finance/sfp/dcd/trade
    body
    {
        "quoteId": "quoterbpDCD-QUOTE17732116652401234"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
quoteId | String | 是 | 报价ID  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "quoteId": "quoterbpDCD-QUOTE17732116652401234",
                "ordId": "987654321",
                "state": "live"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
quoteId | String | 报价ID  
ordId | String | 订单ID  
state | String | 订单状态  
`initial`：系统已接收请求，待处理  
`pending_book`：流动性提供商已接收请求，待处理  
`live`：交易已生效  
`rejected`：交易已拒绝  
  
### POST / 获取赎回报价 

为生效中的双币赢订单申请提前赎回报价。这是两步赎回流程的第一步，之后需调用 POST / 赎回 确认。

#### 限速：10次/60s

#### 限速规则：User ID

#### HTTP请求

`POST /api/v5/finance/sfp/dcd/redeem-quote`

> 请求示例
    
    
    POST /api/v5/finance/sfp/dcd/redeem-quote
    body
    {
        "ordId": "987654321"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
ordId | String | 是 | 订单ID  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "ordId": "987654321",
                "quoteId": "quoterbcDCD-REDEEM17732116652401234",
                "redeemCcy": "BTC",
                "redeemSz": "1.4856",
                "termRate": "-0.50",
                "validUntil": "1774598400000"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
ordId | String | 订单ID  
quoteId | String | 报价ID  
redeemSz | String | 赎回数量  
redeemCcy | String | 赎回币种  
termRate | String | 期限利率  
validUntil | String | 赎回报价有效期，Unix时间戳的毫秒数格式，如 `1597026383085`  
  
### POST / 赎回 

使用有效的赎回报价确认提前赎回。这是两步赎回流程的第二步。

#### 限速：2次/60s

#### 限速规则：User ID

#### HTTP请求

`POST /api/v5/finance/sfp/dcd/redeem`

> 请求示例
    
    
    POST /api/v5/finance/sfp/dcd/redeem
    body
    {
        "ordId": "987654321",
        "quoteId": "quoterbcDCD-REDEEM17732116652401234"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
ordId | String | 是 | 订单ID  
quoteId | String | 是 | 报价ID  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "ordId": "987654321",
                "state": "pending_redeem_booking"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
ordId | String | 订单ID  
state | String | 订单状态  
`pending_redeem_booking`：赎回请求已接收，等待流动性提供商确认  
`pending_redeem`：流动性提供商已确认，等待资金划转  
`redeeming`：赎回处理中  
`redeemed`：赎回完成  
  
### GET / 获取订单状态 

返回双币赢订单的当前状态。

#### 限速：3次/s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/finance/sfp/dcd/order-status`

> 请求示例
    
    
    GET /api/v5/finance/sfp/dcd/order-status?ordId=987654321
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
ordId | String | 是 | 订单ID  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "ordId": "987654321",
                "state": "live"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
ordId | String | 订单ID  
state | String | 订单状态  
`initial`  
`live`  
`pending_settle`  
`settled`  
`pending_redeem`  
`redeemed`  
`rejected`  
  
### GET / 获取历史订单 

返回双币赢历史订单列表

#### 限速：1次/s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/finance/sfp/dcd/order-history`

> 请求示例
    
    
    GET /api/v5/finance/sfp/dcd/order-history
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
ordId | String | 否 | 订单ID。传入时直接返回该订单（忽略其他筛选条件）  
productId | String | 否 | 产品ID，如 `BTC-USDT-260327-77000-C`  
uly | String | 否 | 标的指数，如 `BTC-USD`  
state | String | 否 | 订单状态筛选  
`initial`  
`live`  
`pending_settle`  
`settled`  
`pending_redeem`  
`redeemed`  
`rejected`  
beginId | String | 否 | 返回比该订单ID更新的记录  
endId | String | 否 | 返回比该订单ID更早的记录  
begin | String | 否 | 开始时间戳筛选，Unix时间戳的毫秒数格式，如 `1597026383085`  
end | String | 否 | 结束时间戳筛选，Unix时间戳的毫秒数格式，如 `1597026383085`  
limit | String | 否 | 每次请求返回的结果数量，最大100  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "ordId": "987654321",
                "quoteId": "quoterbpDCD-QUOTE17732116652401234",
                "state": "settled",
                "productId": "BTC-USDT-260327-77000-C",
                "baseCcy": "BTC",
                "quoteCcy": "USDT",
                "uly": "BTC-USD",
                "strike": "77000",
                "notionalSz": "1.5",
                "notionalCcy": "BTC",
                "absYield": "0.00806038",
                "annualizedYield": "0.1834",
                "yieldSz": "0.01209057",
                "yieldCcy": "BTC",
                "settleSz": "1.51209057",
                "settleCcy": "BTC",
                "settlePx": "76500",
                "settleTime": "1774598400000",
                "expTime": "1774598400000",
                "redeemStartTime" : "1774598400000",
                "redeemEndime": "1774598400000",
                "cTime": "1773212400000",
                "uTime": "1773212400000"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
ordId | String | 订单ID  
quoteId | String | 报价ID  
state | String | 订单状态  
`initial`  
`live`  
`pending_settle`  
`settled`  
`pending_redeem`  
`redeemed`  
`rejected`  
productId | String | 产品ID，如 `BTC-USDT-260327-77000-C`  
baseCcy | String | 基础币种，如 `BTC`  
quoteCcy | String | 计价币种，如 `USDT`  
uly | String | 标的指数，如 `BTC-USD`  
strike | String | 行权价  
notionalSz | String | 投资数量  
notionalCcy | String | 投资币种  
absYield | String | 绝对收益率  
annualizedYield | String | 年化收益率  
yieldSz | String | 收益金额  
yieldCcy | String | 收益币种  
settleSz | String | 结算金额（未结算时为""）  
settleCcy | String | 结算币种（未结算时为""）  
settlePx | String | 结算价格（未结算时为""）  
expTime | String | 产品到期时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
settleTime | String | 实际结算时间，Unix时间戳的毫秒数格式，如 `1597026383085`（未结算时为""）  
redeemStartTime | String | 最早可申请提前赎回的时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
redeemEndTime | String | 最晚可申请提前赎回的时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
cTime | String | 订单创建时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
uTime | String | 最后更新时间，Unix时间戳的毫秒数格式，如 `1597026383085`