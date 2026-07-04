---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#trading-account-rest-api-get-balance
anchor_id: trading-account-rest-api-get-balance
api_type: REST
updated_at: 2026-07-04 19:37:07.595197
---

# Get balance

Retrieve a list of assets (with non-zero balance), remaining balance, and available amount in the trading account.

Interest-free quota and discount rates are public data and not displayed on the account interface. 

#### Rate Limit: 10 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/account/balance`

> Request Example
    
    
    # Get the balance of all assets in the account
    GET /api/v5/account/balance
    
    # Get the balance of BTC and ETH assets in the account
    GET /api/v5/account/balance?ccy=BTC,ETH
    
    
    
    
    import okx.Account as Account
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading:0 , demo trading:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # Get account balance
    result = accountAPI.get_account_balance()
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
                "adjEq": "55415.624719833286",
                "availEq": "55415.624719833286",
                "borrowFroz": "0",
                "delta": "0",
                "deltaLever": "0",
                "deltaNeutralStatus": "0",
                "details": [
                    {
                        "autoLendStatus": "off",
                        "autoLendMtAmt": "0",
                        "availBal": "4834.317093622894",
                        "availEq": "4834.3170936228935",
                        "borrowFroz": "0",
                        "cashBal": "4850.435693622894",
                        "ccy": "USDT",
                        "crossLiab": "0",
                        "colRes": "0",
                        "collateralEnabled": false,
                        "collateralRestrict": false,
                        "colBorrAutoConversion": "0",
                        "disEq": "4991.542013297616",
                        "eq": "4992.890093622894",
                        "eqUsd": "4991.542013297616",
                        "smtSyncEq": "0",
                        "spotCopyTradingEq": "0",
                        "fixedBal": "0",
                        "frozenBal": "158.573",
                        "frpType": "0",
                        "imr": "",
                        "interest": "0",
                        "isoEq": "0",
                        "isoLiab": "0",
                        "isoUpl": "0",
                        "liab": "0",
                        "maxLoan": "0",
                        "mgnRatio": "",
                        "mmr": "",
                        "notionalLever": "",
                        "ordFrozen": "0",
                        "rewardBal": "0",
                        "spotInUseAmt": "",
                        "clSpotInUseAmt": "",
                        "maxSpotInUse": "",
                        "spotIsoBal": "0",
                        "stgyEq": "150",
                        "twap": "0",
                        "uTime": "1705449605015",
                        "upl": "-7.545600000000006",
                        "uplLiab": "0",
                        "spotBal": "",
                        "openAvgPx": "",
                        "accAvgPx": "",
                        "spotUpl": "",
                        "spotUplRatio": "",
                        "totalPnl": "",
                        "totalPnlRatio": ""
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
                "ordFroz": "",
                "totalEq": "55837.43556134779",
                "uTime": "1705474164160",
                "upl": "0"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameters** | **Types** | **Description**  
---|---|---  
uTime | String | Update time of account information, millisecond format of Unix timestamp, e.g. `1597026383085`  
totalEq | String | Total account assets denominated in `USD`  
isoEq | String | Isolated margin equity in `USD`  
Applicable to `Futures mode`/`Multi-currency margin`/`Portfolio margin`  
adjEq | String | Adjusted equity in `USD`: `totalEq` minus haircut discounts applied to non-stablecoin collateral assets. This is the operative value used in the margin ratio calculation (`mgnRatio` = `adjEq` / `mmr`).   
The net fiat value of the assets in the account that can provide margins for spot, expiry futures, perpetual futures and options under the cross-margin mode.   
In multi-ccy or PM mode, the asset and margin requirement will all be converted to USD value to process the order check or liquidation.   
Due to the volatility of each currency market, our platform calculates the actual USD value of each currency based on discount rates to balance market risks.   
Applicable to `Spot mode`/`Multi-currency margin` and `Portfolio margin`  
availEq | String | Account level available equity, excluding currencies that are restricted due to the collateralized borrowing limit.  
Applicable to `Multi-currency margin`/`Portfolio margin`  
ordFroz | String | Cross margin frozen for pending orders in `USD`   
Only applicable to `Spot mode`/`Multi-currency margin`/`Portfolio margin`  
imr | String | Initial Margin Requirement (IMR) in `USD`: equity locked across all open cross-margin positions. The sum of initial margins of all open positions and pending orders under cross-margin mode. Formula per position: position size × markPx × initial margin rate (= 1/lever). Returns empty string in Simple mode.   
Applicable to `Spot mode`/`Multi-currency margin`/`Portfolio margin`  
mmr | String | Maintenance Margin Requirement (MMR) in `USD`: the minimum equity required to avoid forced liquidation. The sum of maintenance margins of all open positions and pending orders under cross-margin mode. When `adjEq` ≤ `mmr` (equivalently, `mgnRatio` ≤ 1.0), the system begins forced liquidation of positions. Subscribe to the position-risk-warning WebSocket channel for proactive alerts.   
Applicable to `Spot mode`/`Multi-currency margin`/`Portfolio margin`  
borrowFroz | String | Potential borrowing IMR of the account in `USD`   
Only applicable to `Spot mode`/`Multi-currency margin`/`Portfolio margin`. It is "" for other margin modes.  
mgnRatio | String | Account-level margin ratio = `adjEq` / `mmr`. Values at or below 1.0 indicate the account is at or past the liquidation boundary. Monitor this field or subscribe to the position-risk-warning WebSocket channel for proactive alerts.   
Applicable to `Spot mode`/`Multi-currency margin`/`Portfolio margin`  
notionalUsd | String | Gross notional value of all open derivative positions converted to USD. Linear contracts: sz × ctVal × markPx. Inverse contracts: sz × ctVal (USD-denominated face value). Gross = long and short are not netted.   
Applicable to `Spot mode`/`Multi-currency margin`/`Portfolio margin`  
notionalUsdForBorrow | String | Notional value for `Borrow` in USD  
Applicable to `Spot mode`/`Multi-currency margin`/`Portfolio margin`  
notionalUsdForSwap | String | Notional value of positions for `Perpetual Futures` in USD  
Applicable to `Multi-currency margin`/`Portfolio margin`  
notionalUsdForFutures | String | Notional value of positions for `Expiry Futures` in USD  
Applicable to `Multi-currency margin`/`Portfolio margin`  
notionalUsdForOption | String | Notional value of positions for `Option` in USD  
Applicable to `Spot mode`/`Multi-currency margin`/`Portfolio margin`  
upl | String | Unrealized PnL across all open cross-margin positions at the account level, in `USD`. Calculated using mark price (not last trade price). Positive = unrealized gain; negative = unrealized loss. Returns empty string in Simple mode and Single-currency margin mode.  
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
Applicable to `Spot mode`(enabled spot borrow)/`Multi-currency margin`/`Portfolio margin`  
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
> mgnRatio | String | Cross maintenance margin ratio of currency   
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
> maxLoan | String | Maximum borrowable amount for the currency under the current account conditions. Affects the amount available for margin borrowing and transfers.  
Applicable to `cross` of `Spot mode`/`Multi-currency margin`/`Portfolio margin`  
> eqUsd | String | Equity in `USD` of currency  
> borrowFroz | String | Potential borrowing IMR of currency in `USD`   
Applicable to `Multi-currency margin`/`Portfolio margin`. It is "" for other margin modes.  
> notionalLever | String | Leverage of currency  
Applicable to `Futures mode`  
> stgyEq | String | Total equity allocated to trading bots for the currency. Covers Spot Grid, Futures Grid, Signal Bot, Futures Martingale, Spot Martingale, Infinite Grid, and Recurring Buy strategies.  
> isoUpl | String | Isolated unrealized profit and loss of currency  
Applicable to `Futures mode`/`Multi-currency margin`/`Portfolio margin`  
> spotInUseAmt | String | Actual spot hedging amount in use for the currency.   
Applicable to `Portfolio margin`  
> clSpotInUseAmt | String | User-defined spot hedging amount for the currency. Applicable to `Portfolio margin`  
> maxSpotInUse | String | System-calculated maximum possible spot hedging amount for the currency.  
Applicable to `Portfolio margin`  
> spotIsoBal | String | Balance acquired through spot copy trading (as a follower or lead trader), including amounts currently frozen by open orders. For example, if 1 BTC was purchased via copy trading and 0.4 BTC is frozen in an open sell order, `spotIsoBal` returns `1`, not `0.6`.  
Applicable to copy trading. Applicable to `Spot mode`/`Futures mode`.  
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
  
  * Regarding more parameter details, you can refer to product documentations below:  
[Futures mode: cross margin trading](https://www.okx.com/help/iii-single-currency-margin-cross-margin-trading)   
[Multi-currency margin mode: cross margin trading](https://www.okx.com/help/iv-multi-currency-margin-mode-cross-margin-trading)   
[Multi-currency margin mode vs. Portfolio margin mode](https://www.okx.com/help/vi-multi-currency-margin-mode-vs-portfolio-margin-mode)   

"" will be returned for inapplicable fields under the current account level.  The currency details will not be returned when cashBal and eq is both 0. 

Distribution of applicable fields under each account level are as follows:

**Parameters** | **Spot mode** | **Futures mode** | **Multi-currency margin mode** | **Portfolio margin mode**  
---|---|---|---|---  
uTime | Yes | Yes | Yes | Yes  
totalEq | Yes | Yes | Yes | Yes  
isoEq |  | Yes | Yes | Yes  
adjEq | Yes |  | Yes | Yes  
availEq |  |  | Yes | Yes  
ordFroz | Yes |  | Yes | Yes  
imr | Yes |  | Yes | Yes  
mmr | Yes |  | Yes | Yes  
borrowFroz | Yes |  | Yes | Yes  
mgnRatio | Yes |  | Yes | Yes  
notionalUsd | Yes |  | Yes | Yes  
notionalUsdForSwap |  |  | Yes | Yes  
notionalUsdForFutures |  |  | Yes | Yes  
notionalUsdForOption | Yes |  | Yes | Yes  
notionalUsdForBorrow | Yes |  | Yes | Yes  
upl |  |  | Yes | Yes  
details | Yes | Yes | Yes | Yes  
> ccy | Yes | Yes | Yes | Yes  
> eq | Yes | Yes | Yes | Yes  
> cashBal | Yes | Yes | Yes | Yes  
> uTime | Yes | Yes | Yes | Yes  
> isoEq |  | Yes | Yes | Yes  
> availEq |  | Yes | Yes | Yes  
> disEq | Yes |  | Yes | Yes  
> availBal | Yes | Yes | Yes | Yes  
> frozenBal | Yes | Yes | Yes | Yes  
> ordFrozen | Yes | Yes | Yes | Yes  
> liab | Yes |  | Yes | Yes  
> upl |  | Yes | Yes | Yes  
> uplLiab |  |  | Yes | Yes  
> crossLiab | Yes |  | Yes | Yes  
> isoLiab |  |  | Yes | Yes  
> mgnRatio |  | Yes |  |   
> interest | Yes |  | Yes | Yes  
> twap | Yes |  | Yes | Yes  
> maxLoan | Yes |  | Yes | Yes  
> eqUsd | Yes | Yes | Yes | Yes  
> borrowFroz | Yes |  | Yes | Yes  
> notionalLever |  | Yes |  |   
> stgyEq | Yes | Yes | Yes | Yes  
> isoUpl |  | Yes | Yes | Yes  
> spotInUseAmt |  |  |  | Yes  
> clSpotInUseAmt |  |  |  | Yes  
> maxSpotInUse |  |  |  | Yes  
> spotIsoBal | Yes | Yes |  |   
> imr |  | Yes |  |   
> mmr |  | Yes |  |   
> smtSyncEq | Yes | Yes | Yes | Yes  
> spotCopyTradingEq | Yes | Yes | Yes | Yes  
> spotBal | Yes | Yes | Yes | Yes  
> openAvgPx | Yes | Yes | Yes | Yes  
> accAvgPx | Yes | Yes | Yes | Yes  
> spotUpl | Yes | Yes | Yes | Yes  
> spotUplRatio | Yes | Yes | Yes | Yes  
> totalPnl | Yes | Yes | Yes | Yes  
> totalPnlRatio | Yes | Yes | Yes | Yes  
> collateralEnabled |  |  | Yes |

---

# 查看账户余额

获取交易账户中资金余额信息。

免息额度和折算率都是公共数据，不在账户接口内展示 

#### 限速：10次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/account/balance`

> 请求示例
    
    
    # 获取账户中所有资产余额
    GET /api/v5/account/balance
    
    # 获取账户中BTC、ETH两种资产余额
    GET /api/v5/account/balance?ccy=BTC,ETH
    
    
    
    
    import okx.Account as Account
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # 查看账户余额
    result = accountAPI.get_account_balance()
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 否 | 币种，如 `BTC`  
支持多币种查询（不超过20个），币种之间半角逗号分隔  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "adjEq": "55415.624719833286",
                "availEq": "",
                "borrowFroz": "0",
                "delta": "0",
                "deltaLever": "0",
                "deltaNeutralStatus": "0",
                "details": [
                    {
                        "autoLendStatus": "off",
                        "autoLendMtAmt": "0",
                        "availBal": "4834.317093622894",
                        "availEq": "4834.3170936228935",
                        "borrowFroz": "0",
                        "cashBal": "4850.435693622894",
                        "ccy": "USDT",
                        "crossLiab": "0",
                        "colRes": "0",
                        "collateralEnabled": false,
                        "collateralRestrict": false,
                        "colBorrAutoConversion": "0",
                        "disEq": "4991.542013297616",
                        "eq": "4992.890093622894",
                        "eqUsd": "4991.542013297616",
                        "smtSyncEq": "0",
                        "spotCopyTradingEq": "0",
                        "fixedBal": "0",
                        "frozenBal": "158.573",
                        "frpType": "0",
                        "imr": "",
                        "interest": "0",
                        "isoEq": "0",
                        "isoLiab": "0",
                        "isoUpl": "0",
                        "liab": "0",
                        "maxLoan": "0",
                        "mgnRatio": "",
                        "mmr": "",
                        "notionalLever": "",
                        "ordFrozen": "0",
                        "rewardBal": "0",
                        "spotInUseAmt": "",
                        "clSpotInUseAmt": "",
                        "maxSpotInUse": "",
                        "spotIsoBal": "0",
                        "stgyEq": "150",
                        "twap": "0",
                        "uTime": "1705449605015",
                        "upl": "-7.545600000000006",
                        "uplLiab": "0",
                        "spotBal": "",
                        "openAvgPx": "",
                        "accAvgPx": "",
                        "spotUpl": "",
                        "spotUplRatio": "",
                        "totalPnl": "",
                        "totalPnlRatio": ""
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
                "ordFroz": "",
                "totalEq": "55837.43556134779",
                "uTime": "1705474164160",
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
adjEq | String | 调整后权益（USD）：`totalEq` 减去非稳定币抵押资产的折价扣减。是保证金率计算中的分子（`mgnRatio` = `adjEq` / `mmr`）。美金层面有效保证金  
适用于`现货模式`/`跨币种保证金模式`/`组合保证金模式`  
availEq | String | 账户美金层面可用保证金，排除因总质押借币上限而被限制的币种  
适用于`跨币种保证金模式/组合保证金模式`  
ordFroz | String | 美金层面全仓挂单占用保证金  
仅适用于`现货模式`/`跨币种保证金模式`/`组合保证金模式`  
imr | String | 初始保证金要求（IMR），以 `USD` 计价：账户所有全仓持仓及挂单的初始保证金之和。公式：仓位数量 × 标记价格 × 初始保证金率（= 1/杠杆）。简单交易模式下返回空字符串。  
适用于 `现货模式`/`跨币种保证金模式`/`组合保证金模式`  
mmr | String | 维持保证金要求（MMR），以 `USD` 计价：避免强制平仓所需的最低权益。当 `adjEq` ≤ `mmr`（即 `mgnRatio` ≤ 1.0）时，系统开始强制平仓。可订阅持仓风险预警WebSocket频道获取主动告警。  
适用于 `现货模式`/`跨币种保证金模式`/`组合保证金模式`  
borrowFroz | String | 账户美金层面潜在借币占用保证金  
仅适用于`现货模式`/`跨币种保证金模式`/`组合保证金模式`。在其他账户模式下为""。  
mgnRatio | String | 账户层面保证金率 = `adjEq` / `mmr`。数值 ≤ 1.0 表示账户已达到或超过强平边界。建议监控此字段，或订阅持仓风险预警WebSocket频道进行主动预警。  
适用于 `现货模式`/`跨币种保证金模式`/`组合保证金模式`  
notionalUsd | String | 所有衍生品持仓折算为USD的名义价值总和（多头+空头，不轧差）。线性合约：数量 × `ctVal` × 标记价格；反向合约：数量 × `ctVal`（USD面值固定）。  
适用于 `现货模式`/`跨币种保证金模式`/`组合保证金模式`  
notionalUsdForBorrow | String | 借币金额（美元价值）  
适用于`现货模式`/`跨币种保证金模式`/`组合保证金模式`  
notionalUsdForSwap | String | 永续合约持仓美元价值  
适用于`跨币种保证金模式`/`组合保证金模式`  
notionalUsdForFutures | String | 交割合约持仓美元价值  
适用于`跨币种保证金模式`/`组合保证金模式`  
notionalUsdForOption | String | 期权持仓美元价值  
适用于`现货模式`/`跨币种保证金模式`/`组合保证金模式`  
upl | String | 账户层面所有多头/空头持仓未实现盈亏之和，以 `USD` 计价。按标记价格计算（非最新成交价）。正数代表未实现盈利；负数代表未实现亏损。适用于 `跨币种保证金模式`/`组合保证金模式`，其他模式返回空字符串。  
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
适用于`现货模式`(开通了借币功能)/`跨币种保证金模式`/`组合保证金模式`  
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
> autoLendStatus | String | 自动借出状态  
`unsupported`：该币种不支持自动借出  
`off`：自动借出功能关闭  
`pending`：自动借出功能开启但未匹配  
`active`：自动借出功能开启且已匹配  
> autoLendMtAmt | String | 自动借出已匹配量  
当 autoLendStatus 为 `unsupported/off/pending` 时返回 0  
当 autoLendStatus 为 `active` 时返回已匹配量  
  
  * 更多字段详情，请参考以下产品文档：  
[合约账户全仓交易规则](https://www.okx.com/zh-hans/help/iii-single-currency-margin-cross-margin-trading)  
[跨币种保证金账户全仓交易规则](https://www.okx.com/zh-hans/help/iv-multi-currency-margin-mode-cross-margin-trading)  
[跨币种保证金模式和组合保证金模式对比](https://www.okx.com/zh-hans/help/vi-multi-currency-margin-mode-vs-portfolio-margin-mode)

当前账户等级下无效字段返回""  cashBal 和 eq 同时为 0 的币种过滤不返回 

各账户等级下有效字段分布

参数 | 现货模式 | 合约模式 | 跨币种保证金模式 | 组合保证金模式  
---|---|---|---|---  
uTime | 是 | 是 | 是 | 是  
totalEq | 是 | 是 | 是 | 是  
isoEq |  | 是 | 是 | 是  
adjEq | 是 |  | 是 | 是  
availEq |  |  | 是 | 是  
ordFroz | 是 |  | 是 | 是  
imr | 是 |  | 是 | 是  
mmr | 是 |  | 是 | 是  
borrowFroz | 是 |  | 是 | 是  
mgnRatio | 是 |  | 是 | 是  
notionalUsd | 是 |  | 是 | 是  
notionalUsdForSwap |  |  | 是 | 是  
notionalUsdForFutures |  |  | 是 | 是  
notionalUsdForOption | 是 |  | 是 | 是  
notionalUsdForBorrow | 是 |  | 是 | 是  
upl |  |  | 是 | 是  
details |  |  |  |   
> ccy | 是 | 是 | 是 | 是  
> eq | 是 | 是 | 是 | 是  
> cashBal | 是 | 是 | 是 | 是  
> uTime | 是 | 是 | 是 | 是  
> isoEq |  | 是 | 是 | 是  
> availEq |  | 是 | 是 | 是  
> disEq | 是 |  | 是 | 是  
> availBal | 是 | 是 | 是 | 是  
> frozenBal | 是 | 是 | 是 | 是  
> ordFrozen | 是 | 是 | 是 | 是  
> liab | 是 |  | 是 | 是  
> upl |  | 是 | 是 | 是  
> uplLiab |  |  | 是 | 是  
> crossLiab | 是 |  | 是 | 是  
> isoLiab |  |  | 是 | 是  
> mgnRatio |  | 是 |  |   
> interest | 是 |  | 是 | 是  
> twap | 是 |  | 是 | 是  
> maxLoan | 是 |  | 是 | 是  
> eqUsd | 是 | 是 | 是 | 是  
> borrowFroz | 是 |  | 是 | 是  
> notionalLever |  | 是 |  |   
> stgyEq | 是 | 是 | 是 | 是  
> isoUpl |  | 是 | 是 | 是  
> spotInUseAmt |  |  |  | 是  
> clSpotInUseAmt |  |  |  | 是  
> maxSpotInUse |  |  |  | 是  
> spotIsoBal | 是 | 是 |  |   
> imr |  | 是 |  |   
> mmr |  | 是 |  |   
> smtSyncEq | 是 | 是 | 是 | 是  
> spotCopyTradingEq | 是 | 是 | 是 | 是  
> spotBal | 是 | 是 | 是 | 是  
> openAvgPx | 是 | 是 | 是 | 是  
> accAvgPx | 是 | 是 | 是 | 是  
> spotUpl | 是 | 是 | 是 | 是  
> spotUplRatio | 是 | 是 | 是 | 是  
> totalPnl | 是 | 是 | 是 | 是  
> totalPnlRatio | 是 | 是 | 是 | 是  
> collateralEnabled |  |  | 是 |