---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#sub-account-rest-api-get-sub-account-trading-balance
anchor_id: sub-account-rest-api-get-sub-account-trading-balance
api_type: REST
updated_at: 2026-05-27 19:36:42.901628
---

# Get sub-account trading balance

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

---

# 获取子账户交易账户余额

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