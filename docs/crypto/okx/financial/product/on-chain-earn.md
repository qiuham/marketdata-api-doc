---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#financial-product-on-chain-earn
anchor_id: financial-product-on-chain-earn
api_type: API
updated_at: 2026-07-22 19:21:03.784313
---

# On-chain earn

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

---

# 链上赚币

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