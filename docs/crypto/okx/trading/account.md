---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#trading-account
anchor_id: trading-account
api_type: API
updated_at: 2026-07-16 19:19:18.108744
---

# Trading Account

The API endpoints of `Account` require authentication.

## REST API

### Get instruments

Retrieve available instruments info of current account.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID + Instrument Type

#### HTTP Request

`GET /api/v5/account/instruments`

> Request Example
    
    
    GET /api/v5/account/instruments?instType=SPOT
    
    
    
    import okx.Account as Account
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1" # Production trading: 0, Demo trading: 1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    result = accountAPI.get_instruments(instType="SPOT")
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | Yes | Instrument type  
`SPOT`: Spot  
`MARGIN`: Margin  
`SWAP`: Perpetual Futures  
`FUTURES`: Expiry Futures  
`OPTION`: Option  
`EVENTS`: Event Contracts  
seriesId | String | Conditional | Series ID, e.g. `BTC-ABOVE-DAILY`. Required when instType is `EVENTS`  
instFamily | String | Conditional | Instrument family  
Only applicable to `FUTURES`/`SWAP`/`OPTION`. If instType is `OPTION`, `instFamily` is required.  
instId | String | No | Instrument ID  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "auctionEndTime": "",
                "baseCcy": "BTC",
                "ctMult": "",
                "ctType": "",
                "ctVal": "",
                "ctValCcy": "",
                "contTdSwTime": "1704876947000",
                "elp": "0",
                "expTime": "",
                "futureSettlement": false,
                "groupId": "4",
                "instFamily": "",
                "instId": "BTC-EUR",
                "instType": "SPOT",
                "lever": "",
                "listTime": "1704876947000",
                "lotSz": "0.00000001",
                "maxIcebergSz": "9999999999.0000000000000000",
                "maxLmtAmt": "1000000",
                "maxLmtSz": "9999999999",
                "maxMktAmt": "1000000",
                "maxMktSz": "1000000",
                "maxPlatOILmt": "1000000000",
                "maxPlatOICoinLmt": "",
                "maxStopSz": "1000000",
                "maxTriggerSz": "9999999999.0000000000000000",
                "maxTwapSz": "9999999999.0000000000000000",
                "minSz": "0.00001",
                "optType": "",
                "openType": "call_auction",
                "preMktSwTime": "",
                "posLmtPct": "30",
                "posLmtAmt": "2500000",
                "quoteCcy": "EUR",
                "tradeQuoteCcyList": [
                    "EUR"
                ],
                "settleCcy": "",
                "state": "live",
                "ruleType": "normal",
                "stk": "",
                "tickSz": "1",
                "uly": "",
                "instIdCode": 1000000000,   
                "instCategory": "1",
                "initPxLmtPct": "0.05",
                "floatPxLmtPct": "0.03",
                "maxPxLmtPct": "0.15",
                "upcChg": [
                    {
                        "param": "tickSz",
                        "newValue": "0.0001",
                        "effTime": "1704876947000"
                    }
                ]
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instType | String | Instrument type  
seriesId | String | Series ID, e.g. `BTC-ABOVE-DAILY`. Only applicable to `EVENTS`  
instId | String | Instrument ID, e.g. `BTC-USD-SWAP`  
uly | String | Underlying, e.g. `BTC-USD`   
Only applicable to `MARGIN/FUTURES`/`SWAP`/`OPTION`  
groupId | String | Instrument trading fee group ID  
Spot:  
`3`: Spot TRY  
`5`: Spot BRL  
`7`: Spot AED  
`8`: Spot AUD  
`10`: Spot SGD  
`11`: Spot zero  
`12`: Spot group one  
`13`: Spot group two  
`14`: Spot group three  
`15`: Spot special rule  
`17`: Spot stablecoin  
  
Expiry futures:  
`5`: Expiry futures group one  
`6`: Expiry futures group two  
`8`: XPERP group two  
`10`: XPERP RWA group two  
  
Perpetual futures:  
`4`: Perpetual futures group one  
`5`: Perpetual futures group two  
`6`: SWAP RWA group one  
`7`: SWAP RWA group two  
  
Options:  
`1`: Options crypto-margined  
  
**instType and groupId should be used together to determine a trading fee group. Users should use this endpoint together with[fee rates endpoint](/docs-v5/en/#trading-account-rest-api-get-fee-rates) to get the trading fee of a specific symbol.**   
  
**Some enum values may not apply to you; the actual return values shall prevail.**  
instFamily | String | Instrument family, e.g. `BTC-USD`   
Only applicable to `MARGIN/FUTURES`/`SWAP`/`OPTION`  
baseCcy | String | Base currency, e.g. `BTC` in`BTC-USDT`   
Only applicable to `SPOT`/`MARGIN`  
quoteCcy | String | Quote currency, e.g. `USDT` in `BTC-USDT`   
Only applicable to `SPOT`/`MARGIN`  
settleCcy | String | Settlement and margin currency, e.g. `BTC`   
Only applicable to `FUTURES`/`SWAP`/`OPTION`  
ctVal | String | Contract value   
Only applicable to `FUTURES`/`SWAP`/`OPTION`  
ctMult | String | Contract multiplier   
Only applicable to `FUTURES`/`SWAP`/`OPTION`  
ctValCcy | String | Contract value currency   
Only applicable to `FUTURES`/`SWAP`/`OPTION`  
optType | String | Option type, `C`: Call `P`: put   
Only applicable to `OPTION`  
stk | String | Strike price   
Only applicable to `OPTION`  
listTime | String | Listing time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
auctionEndTime | String | ~~The end time of call auction, Unix timestamp format in milliseconds, e.g.`1597026383085`   
Only applicable to `SPOT` that are listed through call auctions, return "" in other cases (deprecated, use contTdSwTime)~~  
contTdSwTime | String | Continuous trading switch time. The switch time from call auction, prequote to continuous trading, Unix timestamp format in milliseconds. e.g. `1597026383085`.  
Only applicable to `SPOT`/`MARGIN` that are listed through call auction or prequote, return "" in other cases.  
preMktSwTime | String | The time a pre-market instrument switched to normal trading, Unix timestamp format in milliseconds, e.g. `1597026383085`.   
Only applicable to pre-market `SWAP` and pre-market X-Perp `FUTURES`. Populated when a pre-market X-Perp converts to a normal X-Perp  
openType | String | Open type  
`fix_price`: fix price opening  
`pre_quote`: pre-quote  
`call_auction`: call auction   
Only applicable to `SPOT`/`MARGIN`, return "" for all other business lines  
elp | String | ELP maker permission  
`0`: ELP is not enabled for this symbol  
`1`: ELP is enabled for this symbol, but current users don't have permission to place ELP orders for it.   
`2`: ELP is enabled for this symbol, and current users have permission to place ELP orders for it.   
  
It doesn't mean there will be ELP liquidity when elp is `1/2`.  
expTime | String | Expiry time   
Applicable to `SPOT`/`MARGIN`/`FUTURES`/`SWAP`/`OPTION`. For `FUTURES`/`OPTION`, it is natural delivery/exercise time. It is the instrument offline time when there is `SPOT/MARGIN/FUTURES/SWAP/` manual offline. Update once change.  
lever | String | Max Leverage,   
Not applicable to `SPOT`, `OPTION`  
tickSz | String | Tick size, e.g. `0.0001`.  
For `OPTION`/`EVENTS`, it is the minimum tickSz among tick band. Use "Get instrument tick bands" endpoint with the corresponding `instType` for accurate tickSz per price range.  
lotSz | String | Lot size  
If it is a derivatives contract, the value is the number of contracts.  
If it is `SPOT`/`MARGIN`, the value is the quantity in `base currency`.  
minSz | String | Minimum order size  
If it is a derivatives contract, the value is the number of contracts.  
If it is `SPOT`/`MARGIN`, the value is the quantity in `base currency`.  
ctType | String | Contract type  
`linear`: linear contract  
`inverse`: inverse contract   
Only applicable to `FUTURES`/`SWAP`  
state | String | Instrument status  
`live`   
`suspend`  
`rebase`: can't be traded during rebasing, only applicable to `SWAP`  
`post_only`: only post-only orders are accepted; existing post-only orders can be amended and cancelled. Other order types (market, IOC, FOK, normal limit) are rejected. Only applicable to `SWAP`  
`preopen` e.g. Futures and options contracts rollover from generation to trading start; certain symbols before they go live  
`test`: Test pairs, can't be traded  
`settling`: Settling, only applicable to `EVENTS`  
ruleType | String | Trading rule types  
`normal`: normal trading  
`pre_market`: pre-market trading, including pre-market X-Perp `FUTURES`  
`rebase_contract`: pre-market rebase contract  
`xperp`: perpetual-style futures, only applicable to certain `FUTURES` contracts. A pre-market X-Perp changes from `pre_market` to `xperp` after it converts to a normal X-Perp  
posLmtAmt | String | Maximum position value (USD) for this instrument at the user level (shared across master and sub-accounts), based on the notional value of all same-direction open positions and resting orders. The effective user limit is max(posLmtAmt, oiUSD × posLmtPct). Applicable to `SWAP`/`FUTURES`.  
posLmtPct | String | Maximum position ratio (e.g., 30 for 30%) a user (shared across master and sub-accounts) may hold relative to the platform's current total position value. The effective user limit is max(posLmtAmt, oiUSD × posLmtPct). Applicable to `SWAP`/`FUTURES`.  
maxPlatOILmt | String | Platform-wide maximum position value (USD) for this instrument. If the platform total open interest (USD) reaches or exceeds this value, all users’ new opening orders for this instrument are rejected; otherwise, orders pass.  
Applicable to `SWAP`/`FUTURES`  
maxPlatOICoinLmt | String | Platform-wide maximum position value (coins) for this instrument. If the platform total open interest (coins) reaches or exceeds this value, all users’ new opening orders for this instrument are rejected; otherwise, orders pass.  
Applicable to `SWAP`/`FUTURES`  
longPosRemainingQuota | String | The remaining long position value (USD) the user is permitted to open, netting all existing long positions and resting buy orders. The quota is shared across the master account and all subaccounts.  
shortPosRemainingQuota | String | The remaining short position value (USD) the user is permitted to open, netting all existing short positions and resting sell orders. The quota is shared across the master account and all subaccounts.  
maxLmtSz | String | The maximum order quantity of a single limit order.  
If it is a derivatives contract, the value is the number of contracts.  
If it is `SPOT`/`MARGIN`, the value is the quantity in `base currency`.  
maxMktSz | String | The maximum order quantity of a single market order.  
If it is a derivatives contract, the value is the number of contracts.  
If it is `SPOT`/`MARGIN`, the value is the quantity in `USDT`.  
maxLmtAmt | String | Max USD amount for a single limit order  
maxMktAmt | String | Max USD amount for a single market order   
Only applicable to `SPOT`/`MARGIN`  
maxTwapSz | String | The maximum order quantity of a single TWAP order.  
If it is a derivatives contract, the value is the number of contracts.  
If it is `SPOT`/`MARGIN`, the value is the quantity in `base currency`.   
The minimum order quantity of a single TWAP order is minSz*2  
maxIcebergSz | String | The maximum order quantity of a single iceBerg order.  
If it is a derivatives contract, the value is the number of contracts.  
If it is `SPOT`/`MARGIN`, the value is the quantity in `base currency`.  
maxTriggerSz | String | The maximum order quantity of a single trigger order.  
If it is a derivatives contract, the value is the number of contracts.  
If it is `SPOT`/`MARGIN`, the value is the quantity in `base currency`.  
maxStopSz | String | The maximum order quantity of a single stop market order.  
If it is a derivatives contract, the value is the number of contracts.  
If it is `SPOT`/`MARGIN`, the value is the quantity in `USDT`.  
futureSettlement | Boolean | Whether daily settlement for expiry feature is enabled  
Applicable to `FUTURES` `cross`  
tradeQuoteCcyList | Array of strings | List of quote currencies available for trading, e.g. ["USD", "USDC"].  
instIdCode | Integer | Instrument ID code.   
For simple binary encoding, you must use `instIdCode` instead of `instId`.  
For the same `instId`, it's value may be different between production and demo trading.   
It is `null` when the value is not generated.  
instCategory | String | The asset category of the instrument’s base asset (the first segment of the instrument ID). For example, for `BTC-USDT-SWAP`, the `instCategory` represents the asset category of `BTC`.   
`1`: Crypto   
`3`: Stocks   
`4`: Commodities   
`5`: Forex   
`6`: Bonds   
`""`: Not available  
initPxLmtPct | String | Initial price-limit band applied during the first 10 minutes after contract listing, e.g. `0.05` represents 5%. Use GET /api/v5/public/price-limit for the computed price limits.  
Only applicable to `SPOT`/`MARGIN`/`SWAP`/`FUTURES`, returns `""` for `OPTION` and `EVENTS`.  
floatPxLmtPct | String | Floating price-limit band during normal trading, e.g. `0.03` represents 3%. Use GET /api/v5/public/price-limit for the computed price limits.  
Only applicable to `SPOT`/`MARGIN`/`SWAP`/`FUTURES`, returns `""` for `OPTION` and `EVENTS`.  
maxPxLmtPct | String | Maximum price-limit cap (hard ceiling on order-price deviation from the index price), e.g. `0.15` represents 15%. Use GET /api/v5/public/price-limit for the computed price limits.  
Only applicable to `SPOT`/`MARGIN`/`SWAP`/`FUTURES`, returns `""` for `OPTION` and `EVENTS`.  
upcChg | Array of objects | Upcoming changes. It is [] when there is no upcoming change.  
> param | String | The parameter name to be updated.   
`tickSz`  
`minSz`: For `FUTURES`/`SWAP`, `lotSz` will be modified synchronously.  
`maxMktSz`  
> newValue | String | The parameter value that will replace the current one.  
> effTime | String | Effective time. Unix timestamp format in milliseconds, e.g. `1597026383085`  
listTime and contTdSwTime  
For spot symbols listed through a call auction or pre-open, listTime represents the start time of the auction or pre-open, and contTdSwTime indicates the end of the auction or pre-open and the start of continuous trading. For other scenarios, listTime will mark the beginning of continuous trading, and contTdSwTime will return an empty value "".  state  
For `SPOT`, `MARGIN`, `SWAP`, and `FUTURES`, the state changes from `preopen` to `live` when the `listTime` is reached. For `OPTION` contracts, the state may change to `live` slightly after `listTime` due to internal processing. It is recommended to verify that `state` is `live` before placing orders.  
When a product is going to be delisted (e.g. when a FUTURES contract is settled or OPTION contract is exercised), the instrument will not be available. 

### Get balance

Retrieve a list of assets (with non-zero balance), remaining balance, and available amount in the trading account.

Interest-free quota and discount rates are public data and not displayed on the account interface. 

#### Rate Limit: 10 requests per 2 seconds

#### Rate limit rule: User ID

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
  
### Get positions

Retrieve information on your positions. When the account is in `net` mode, `net` positions will be displayed, and when the account is in `long/short` mode, `long` or `short` positions will be displayed. Return in reverse chronological order using ctime.

#### Rate Limit: 10 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/account/positions`

> Request Example
    
    
    # Query BTC-USDT position information
    GET /api/v5/account/positions?instId=BTC-USDT
    
    
    
    
    import okx.Account as Account
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading:0 , demo trading:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # Get positions information
    result = accountAPI.get_positions()
    print(result)
    

#### Request Parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
instType | String | No | Instrument type  
`MARGIN`  
`SWAP`  
`FUTURES`  
`OPTION`  
`EVENTS`  
`instId` will be checked against `instType` when both parameters are passed.  
instId | String | No | Instrument ID, e.g. `BTC-USDT-SWAP`. Single instrument ID or multiple instrument IDs (no more than 10) separated with comma  
posId | String | No | Single position ID or multiple position IDs (no more than 20) separated with comma.   
There is attribute expiration, the posId and position information will be cleared if it is more than 30 days after the last full close position.  
instId  
If the instrument ever had position and its open interest is 0, it will return the position information with specific instId. It will not return the position information with specific instId if there is no valid posId; it will not return the position information without specific instId.  In the isolated margin trading settings, if it is set to the manual transfers mode, after the position is transferred to the margin, a position with a position of 0 will be generated 

> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "adl": "1",
                "availPos": "0.00190433573",
                "avgPx": "62961.4",
                "baseBal": "",
                "baseBorrowed": "",
                "baseInterest": "",
                "bePx": "",
                "bizRefId": "",
                "bizRefType": "",
                "cTime": "1724740225685",
                "ccy": "BTC",
                "clSpotInUseAmt": "",
                "closeOrderAlgo": [],
                "deltaBS": "",
                "deltaPA": "",
                "fee": "",
                "fundingFee": "",
                "gammaBS": "",
                "gammaPA": "",
                "hedgedPos": "",
                "idxPx": "62890.5",
                "imr": "",
                "instId": "BTC-USDT",
                "instType": "MARGIN",
                "interest": "0",
                "last": "62892.9",
                "lever": "5",
                "liab": "-99.9998177776581948",
                "liabCcy": "USDT",
                "liqPenalty": "",
                "liqPx": "53615.448336593756",
                "margin": "0.000317654",
                "markPx": "62891.9",
                "maxSpotInUseAmt": "",
                "mgnMode": "isolated",
                "mgnRatio": "9.404143929947395",
                "mmr": "0.0000318005395854",
                "notionalUsd": "119.756628017499",
                "optVal": "",
                "pendingCloseOrdLiabVal": "0",
                "pnl": "",
                "pos": "0.00190433573",
                "posCcy": "BTC",
                "posId": "1752810569801498626",
                "posSide": "net",
                "quoteBal": "",
                "quoteBorrowed": "",
                "quoteInterest": "",
                "realizedPnl": "",
                "spotInUseAmt": "",
                "spotInUseCcy": "",
                "thetaBS": "",
                "thetaPA": "",
                "tradeId": "785524470",
                "uTime": "1724742632153",
                "upl": "-0.0000033452492717",
                "uplLastPx": "-0.0000033199677697",
                "uplRatio": "-0.0105311101755551",
                "uplRatioLastPx": "-0.0104515220008934",
                "usdPx": "",
                "vegaBS": "",
                "vegaPA": "",
                "nonSettleAvgPx":"",
                "settledPnl":""
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instType | String | Instrument type  
`MARGIN`  
`SWAP`  
`FUTURES`  
`OPTION`  
`EVENTS`  
mgnMode | String | Margin mode  
`cross`   
`isolated`  
posId | String | Position ID  
posSide | String | Position side  
`long`, `pos` is positive   
`short`, `pos` is positive   
`net` (`FUTURES`/`SWAP`/`OPTION`: positive `pos` means long position and negative `pos` means short position. For `MARGIN`, `pos` is always positive, `posCcy` being base currency means long position, `posCcy` being quote currency means short position.)  
pos | String | Position quantity. Unit: number of contracts for SWAP/FUTURES/OPTIONS; base currency amount for MARGIN. Sign (net mode): positive = long, negative = short. In long/short mode, separate records are returned per side — check `posSide`. In the isolated margin mode, when doing manual transfers, a position with pos of `0` will be generated after the deposit is transferred (represents a funded-but-empty position record created after a margin deposit).  
hedgedPos | String | Hedged position size  
Only return for accounts in delta neutral strategy, stgyType:1. Return "" for accounts in general strategy.  
baseBal | String | ~~Base currency balance, only applicable to`MARGIN`（Quick Margin Mode）~~(Deprecated)  
quoteBal | String | ~~Quote currency balance, only applicable to`MARGIN`（Quick Margin Mode）~~(Deprecated)  
baseBorrowed | String | ~~Base currency amount already borrowed, only applicable to MARGIN(Quick Margin Mode）~~(Deprecated)  
baseInterest | String | ~~Base Interest, undeducted interest that has been incurred, only applicable to MARGIN(Quick Margin Mode）~~(Deprecated)  
quoteBorrowed | String | ~~Quote currency amount already borrowed, only applicable to MARGIN(Quick Margin Mode）~~(Deprecated)  
quoteInterest | String | ~~Quote Interest, undeducted interest that has been incurred, only applicable to MARGIN(Quick Margin Mode）~~(Deprecated)  
posCcy | String | Position currency, only applicable to `MARGIN` positions.  
availPos | String | Position that can be closed   
Only applicable to `MARGIN` and `OPTION`.  
For `MARGIN` position, the rest of sz will be `SPOT` trading after the liability is repaid while closing the position. Please get the available reduce-only amount from "Get maximum available tradable amount" if you want to reduce the amount of `SPOT` trading as much as possible.  
avgPx | String | Volume-weighted average entry price of the current open position. Denominated in quote currency for linear contracts (e.g., USDT for BTC-USDT-SWAP) and in USD for inverse contracts (e.g., BTC-USD-SWAP). Recalculated after each fill that changes position size.  
Under cross-margin mode, the entry price of expiry futures will update at settlement to the last settlement price, and when the position is opened or increased.  
nonSettleAvgPx | String | Non-settlement entry price  
The non-settlement entry price only reflects the average price at which the position is opened or increased.  
Applicable to `cross` `FUTURES` positions.  
markPx | String | Latest Mark price  
upl | String | Unrealized PnL for this position, denominated in the instrument's settlement currency (see `ccy`). Formula: (markPx − avgPx) × pos × ctVal for linear; (1/avgPx − 1/markPx) × pos × ctVal for inverse. For account-level USD total, see `upl` in GET /api/v5/account/balance.  
uplRatio | String | Unrealized profit and loss ratio calculated by mark price.  
uplLastPx | String | Unrealized profit and loss calculated by last price. Main usage is showing, actual value is upl.  
uplRatioLastPx | String | Unrealized profit and loss ratio calculated by last price.  
instId | String | Instrument ID, e.g. `BTC-USDT-SWAP`  
lever | String | Leverage  
Not applicable to `OPTION` and positions of cross margin mode under `Portfolio margin`  
liqPx | String | Estimated mark price at which this position would be forcibly liquidated. This is an estimate based on current equity and margin rates — the actual liquidation price can change quickly due to funding rate accrual, other position changes, or rapid market moves.   
Not applicable to `OPTION`  
imr | String | Initial margin requirement for this specific cross-margin position, in USD. Formula: position size × markPx × initial margin rate (1/lever). For total account IMR, see `imr` in GET /api/v5/account/balance. Empty string for isolated positions. Only applicable to `cross`.  
margin | String | Margin, can be added or reduced. Only applicable to `isolated`.  
mgnRatio | String | Maintenance margin ratio  
mmr | String | Maintenance margin requirement  
liab | String | Liabilities, only applicable to `MARGIN`.  
liabCcy | String | Liabilities currency, only applicable to `MARGIN`.  
interest | String | Interest. Undeducted interest that has been incurred.  
tradeId | String | Last trade ID  
optVal | String | Option Value, only applicable to `OPTION`.  
pendingCloseOrdLiabVal | String | The amount of close orders of isolated margin liability.  
notionalUsd | String | Notional value of positions in `USD`  
adl | String | Auto-Deleveraging (ADL) indicator. Range: 0–5, where 0 = lowest ADL priority (least likely to be forcibly deleveraged) and 5 = highest priority (first in queue if the insurance fund is depleted). Priority increases with higher unrealized profit and higher leverage.   
Only applicable to `FUTURES/SWAP/OPTION`  
ccy | String | Currency used for margin  
last | String | Latest traded price  
idxPx | String | Latest underlying index price  
usdPx | String | Latest USD price of the `ccy` on the market, only applicable to `FUTURES`/`SWAP`/`OPTION`  
bePx | String | Breakeven price  
deltaBS | String | delta: Black-Scholes Greeks in dollars, only applicable to `OPTION`  
deltaPA | String | delta: Greeks in coins, only applicable to `OPTION`  
gammaBS | String | gamma: Black-Scholes Greeks in dollars, only applicable to `OPTION`  
gammaPA | String | gamma: Greeks in coins, only applicable to `OPTION`  
thetaBS | String | theta：Black-Scholes Greeks in dollars, only applicable to `OPTION`  
thetaPA | String | theta：Greeks in coins, only applicable to `OPTION`  
vegaBS | String | vega：Black-Scholes Greeks in dollars, only applicable to `OPTION`  
vegaPA | String | vega：Greeks in coins, only applicable to `OPTION`  
spotInUseAmt | String | Spot in use amount  
Applicable to `Portfolio margin`  
spotInUseCcy | String | Spot in use unit, e.g. `BTC`  
Applicable to `Portfolio margin`  
clSpotInUseAmt | String | User-defined spot risk offset amount  
Applicable to `Portfolio margin`  
maxSpotInUseAmt | String | Max possible spot risk offset amount  
Applicable to `Portfolio margin`  
bizRefId | String | External business id, e.g. experience coupon id  
bizRefType | String | External business type  
realizedPnl | String | Realized profit and loss  
Only applicable to `FUTURES`/`SWAP`/`OPTION`  
`realizedPnl`=`pnl`+`fee`+`fundingFee`+`liqPenalty`+`settledPnl`  
settledPnl | String | Accumulated settled profit and loss (calculated by settlement price)  
Only applicable to `cross` `FUTURES`  
pnl | String | Accumulated pnl of closing order(s) (excluding the fee).  
fee | String | Accumulated fee since the current position was opened. Resets to 0 when the position is fully closed. For per-fill fees, use GET /api/v5/trade/fills.  
Negative number represents the user transaction fee charged by the platform. Positive number represents rebate.  
fundingFee | String | Accumulated funding fee  
liqPenalty | String | Accumulated liquidation penalty. It is negative when there is a value.  
closeOrderAlgo | Array of objects | Close position algo orders attached to the position. This array will have values only after you request "Place algo order" with `closeFraction`=1.  
> algoId | String | Algo ID  
> slTriggerPx | String | Stop-loss trigger price.  
> slTriggerPxType | String | Stop-loss trigger price type.   
`last`: last price  
`index`: index price  
`mark`: mark price  
> tpTriggerPx | String | Take-profit trigger price.  
> tpTriggerPxType | String | Take-profit trigger price type.   
`last`: last price  
`index`: index price  
`mark`: mark price  
> closeFraction | String | Fraction of position to be closed when the algo order is triggered.  
cTime | String | Creation time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
uTime | String | Latest time position was adjusted, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
As for portfolio margin account, the IMR and MMR of the position are calculated in risk unit granularity, thus their values of the same risk unit cross positions are the same. 

### Get positions history

Retrieve the updated position data for the last 3 months. Return in reverse chronological order using utime. Getting positions history is supported under Portfolio margin mode since **04:00 AM (UTC) on November 11, 2024**.

#### Rate Limit: 10 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/account/positions-history`

> Request Example
    
    
    GET /api/v5/account/positions-history
    
    
    
    import okx.Account as Account
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading:0 , demo trading:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # Get positions history
    result = accountAPI.get_positions_history()
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | No | Instrument type  
`MARGIN`  
`SWAP`  
`FUTURES`  
`OPTION`  
`EVENTS`  
instId | String | No | Instrument ID, e.g. `BTC-USD-SWAP`  
mgnMode | String | No | Margin mode  
`cross` `isolated`  
type | String | No | The type of latest close position  
`1`: Close position partially;`2`：Close all;`3`：Liquidation;`4`：Partial liquidation; `5`：ADL - position not fully closed; `6`：ADL - position fully closed  
It is the latest type if there are several types for the same position.  
posId | String | No | Position ID. There is attribute expiration. The posId will be expired if it is more than 30 days after the last full close position, then position will use new posId.  
after | String | No | Pagination of data to return records earlier than the requested `uTime`, Unix timestamp format in milliseconds, e.g. `1597026383085`  
before | String | No | Pagination of data to return records newer than the requested `uTime`, Unix timestamp format in milliseconds, e.g. `1597026383085`  
limit | String | No | Number of results per request. The maximum is 100. The default is 100. All records that have the same `uTime` will be returned at the current request  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "cTime": "1654177169995",
                "ccy": "BTC",
                "closeAvgPx": "29786.5999999789081085",
                "closeTotalPos": "1",
                "instId": "BTC-USD-SWAP",
                "instType": "SWAP",
                "lever": "10.0",
                "mgnMode": "cross",
                "openAvgPx": "29783.8999999995535393",
                "openMaxPos": "1",
                "realizedPnl": "0.001",
                "fee": "-0.0001",
                "fundingFee": "0",
                "liqPenalty": "0",
                "pnl": "0.0011",
                "pnlRatio": "0.000906447858888",
                "posId": "452587086133239818",
                "posSide": "long",
                "direction": "long",
                "triggerPx": "",
                "type": "1",
                "uTime": "1654177174419",
                "uly": "BTC-USD",
                "nonSettleAvgPx":"",
                "settledPnl":""
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
instType | String | Instrument type  
`MARGIN`  
`SWAP`  
`FUTURES`  
`OPTION`  
`EVENTS`  
instId | String | Instrument ID  
mgnMode | String | Margin mode  
`cross` `isolated`  
type | String | The type of latest close position  
`1`：Close position partially;`2`：Close all;`3`：Liquidation;`4`：Partial liquidation; `5`：ADL;   
It is the latest type if there are several types for the same position.  
cTime | String | Created time of position  
uTime | String | Updated time of position  
openAvgPx | String | Average price of opening position  
Under cross-margin mode, the entry price of expiry futures will update at settlement to the last settlement price, and when the position is opened or increased.  
nonSettleAvgPx | String | Non-settlement entry price  
The non-settlement entry price only reflects the average price at which the position is opened or increased.  
Only applicable to `cross` `FUTURES`  
closeAvgPx | String | Average price of closing position  
posId | String | Position ID  
openMaxPos | String | Max quantity of position  
closeTotalPos | String | Position's cumulative closed volume  
realizedPnl | String | Realized profit and loss  
Only applicable to `FUTURES`/`SWAP`/`OPTION`  
`realizedPnl`=`pnl`+`fee`+`fundingFee`+`liqPenalty`+`settledPnl`  
settledPnl | String | Accumulated settled profit and loss (calculated by settlement price)  
Only applicable to `cross` `FUTURES`  
pnlRatio | String | Realized P&L ratio  
fee | String | Accumulated fee  
Negative number represents the user transaction fee charged by the platform.Positive number represents rebate.  
fundingFee | String | Accumulated funding fee  
liqPenalty | String | Accumulated liquidation penalty. It is negative when there is a value.  
pnl | String | Profit and loss (excluding the fee).  
posSide | String | Position mode side  
`long`: Hedge mode long  
`short`: Hedge mode short  
`net`: Net mode  
lever | String | Leverage  
direction | String | Direction: `long` `short`  
Only applicable to `MARGIN/FUTURES/SWAP/OPTION`  
triggerPx | String | trigger mark price. There is value when `type` is equal to `3`, `4` or `5`. It is "" when `type` is equal to `1` or `2`  
uly | String | Underlying  
ccy | String | Currency used for margin  
  
### Get account and position risk

Get account and position risk

Obtain basic information about accounts and positions on the same time snapshot 

#### Rate Limit: 10 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/account/account-position-risk`

> Request Example
    
    
    GET /api/v5/account/account-position-risk
    
    
    
    
    import okx.Account as Account
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading:0 , demo trading:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # Get account and position risk
    result = accountAPI.get_account_position_risk()
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | No | Instrument type  
`MARGIN`  
`SWAP`  
`FUTURES`  
`OPTION`  
  
> Response Example
    
    
    {
        "code":"0",
        "data":[
            {
                "adjEq":"174238.6793649711331679",
                "balData":[
                    {
                        "ccy":"BTC",
                        "disEq":"78846.7803721021362242",
                        "eq":"1.3863533369419636"
                    },
                    {
                        "ccy":"USDT",
                        "disEq":"73417.2495112863300127",
                        "eq":"73323.395564963177146"
                    }
                ],
                "posData":[
                    {
                        "baseBal": "0.4",
                        "ccy": "",
                        "instId": "BTC-USDT",
                        "instType": "MARGIN",
                        "mgnMode": "isolated",
                        "notionalCcy": "0",
                        "notionalUsd": "0",
                        "pos": "0",
                        "posCcy": "",
                        "posId": "310388685292318723",
                        "posSide": "net",
                        "quoteBal": "0"
                    }
                ],
                "ts":"1620282889345"
            }
        ],
        "msg":""
    }
    

#### Response Parameters

**Parameters** | **Types** | **Description**  
---|---|---  
ts | String | Update time of account information, millisecond format of Unix timestamp, e.g. `1597026383085`  
adjEq | String | Adjusted / Effective equity in `USD`  
Applicable to `Multi-currency margin` and `Portfolio margin`  
balData | Array of objects | Detailed asset information in all currencies  
> ccy | String | Currency  
> eq | String | Equity of currency  
> disEq | String | Discount equity of currency in `USD`.  
posData | Array of objects | Detailed position information in all currencies  
> instType | String | Instrument type  
> mgnMode | String | Margin mode  
`cross`   
`isolated`  
> posId | String | Position ID  
> instId | String | Instrument ID, e.g. `BTC-USDT-SWAP`  
> pos | String | Quantity of positions `contract`. In the isolated margin mode, when doing manual transfers, a position with pos of `0` will be generated after the deposit is transferred  
> baseBal | String | ~~Base currency balance, only applicable to`MARGIN`（Quick Margin Mode）~~(Deprecated)  
> quoteBal | String | ~~Quote currency balance, only applicable to`MARGIN`（Quick Margin Mode）~~(Deprecated)  
> posSide | String | Position side  
`long`   
`short`   
`net` (`FUTURES`/`SWAP`/`OPTION`: positive `pos` means long position and negative `pos` means short position. `MARGIN`: `posCcy` being base currency means long position, `posCcy` being quote currency means short position.)  
> posCcy | String | Position currency, only applicable to `MARGIN` positions.  
> ccy | String | Currency used for margin  
> notionalCcy | String | Notional value of positions in `coin`  
> notionalUsd | String | Notional value of positions in `USD`  
  
### Get bills details (last 7 days)

Retrieve the bills of the account. The bill refers to all transaction records that result in changing the balance of an account. Pagination is supported, and the response is sorted with the most recent first. This endpoint can retrieve data from the last 7 days.

#### Rate Limit: 5 requests per second

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/account/bills`

> Request Example
    
    
    GET /api/v5/account/bills
    
    GET /api/v5/account/bills?instType=MARGIN
    
    
    
    
    import okx.Account as Account
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading:0 , demo trading:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # Get bills details (last 7 days)
    result = accountAPI.get_account_bills()
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | No | Instrument type  
`SPOT`  
`MARGIN`  
`SWAP`  
`FUTURES`  
`OPTION`  
`EVENTS`  
instId | String | No | Instrument ID, e.g. `BTC-USDT`  
ccy | String | No | Bill currency  
mgnMode | String | No | Margin mode  
`isolated`  
`cross`  
ctType | String | No | Contract type  
`linear`  
`inverse`  
Only applicable to `FUTURES`/`SWAP`  
type | String | No | Bill type  
Please refer to [Get bill types](/docs-v5/en/#trading-account-rest-api-get-bill-types) for the list of available types.  
subType | String | No | Bill subtype  
Please refer to [Get bill types](/docs-v5/en/#trading-account-rest-api-get-bill-types) for the list of available types.  
after | String | No | Pagination of data to return records earlier than the requested bill ID.  
before | String | No | Pagination of data to return records newer than the requested bill ID.  
begin | String | No | Filter with a begin timestamp `ts`. Unix timestamp format in milliseconds, e.g. `1597026383085`  
end | String | No | Filter with an end timestamp `ts`. Unix timestamp format in milliseconds, e.g. `1597026383085`  
limit | String | No | Number of results per request. The maximum is `100`. The default is `100`.  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
            "bal": "8694.2179403378290202",
            "balChg": "0.0219338232210000",
            "billId": "623950854533513219",
            "ccy": "USDT",
            "clOrdId": "",
            "earnAmt": "",
            "earnApr": "",
            "execType": "T",
            "fee": "-0.000021955779",
            "fillFwdPx": "",
            "fillIdxPx": "27104.1",
            "fillMarkPx": "",
            "fillMarkVol": "",
            "fillPxUsd": "",
            "fillPxVol": "",
            "fillTime": "1695033476166",
            "from": "",
            "instId": "BTC-USDT",
            "instType": "SPOT",
            "interest": "0",
            "mgnMode": "isolated",
            "notes": "",
            "ordId": "623950854525124608",
            "pnl": "0",
            "posBal": "0",
            "posBalChg": "0",
            "px": "27105.9",
            "subType": "1",
            "sz": "0.021955779",
            "tag": "",
            "to": "",
            "tradeId": "586760148",
            "ts": "1695033476167",
            "type": "2"
        }]
    } 
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
instType | String | Instrument type  
billId | String | Bill ID  
type | String | Bill type  
subType | String | Bill subtype  
ts | String | The time when the balance complete update, Unix timestamp format in milliseconds, e.g.`1597026383085`  
balChg | String | Signed change in account balance for this event, in the currency specified by the `ccy` field. Positive: balance increased (e.g., received funding fee rebate, closed profitable trade). Negative: balance decreased (e.g., paid trading fee, settled a loss).  
posBalChg | String | Change in balance amount at the position level  
bal | String | Balance at the account level  
posBal | String | Balance at the position level  
sz | String | Quantity  
For `FUTURES`/`SWAP`/`OPTION`, it is fill quantity or position quantity, the unit is contract. The value is always positive.  
For other scenarios. the unit is account balance currency(`ccy`).  
px | String | Price which related to subType  

* Trade filled price for
`1`: Buy `2`: Sell `3`: Open long `4`: Open short `5`: Close long `6`: Close short `204`: block trade buy `205`: block trade sell `206`: block trade open long `207`: block trade open short `208`: block trade close long `209`: block trade close short `114`: Forced repayment buy `115`: Forced repayment sell  

* Liquidation Price for
`100`: Partial liquidation close long `101`: Partial liquidation close short `102`: Partial liquidation buy `103`: Partial liquidation sell `104`: Liquidation long `105`: Liquidation short `106`: Liquidation buy `107`: Liquidation sell `16`: Repay forcibly `17`: Repay interest by borrowing forcibly `110`: Liquidation transfer in `111`: Liquidation transfer out  

* Delivery price for
`112`: Delivery long `113`: Delivery short  

* Exercise price for
`170`: Exercised `171`: Counterparty exercised `172`: Expired OTM  

* Mark price for
`173`: Funding fee expense `174`: Funding fee income  
ccy | String | Account balance currency  
pnl | String | Profit and loss  
fee | String | Fee  
Negative number represents the user transaction fee charged by the platform.  
Positive number represents rebate.  
[Trading fee rule](/en/fees)  
earnAmt | String | Auto earn amount  
Only applicable when type is 381  
earnApr | String | Auto earn APR  
Only applicable when type is 381  
mgnMode | String | Margin mode  
`isolated` `cross` `cash`  
When bills are not generated by trading, the field returns ""  
instId | String | Instrument ID, e.g. `BTC-USDT`  
ordId | String | Order ID  
Return order ID when the type is `2`/`5`/`9`  
Return "" when there is no order.  
execType | String | Liquidity taker or maker  
`T`: taker  
`M`: maker  
from | String | The remitting account  
`6`: Funding account  
`18`: Trading account  
Only applicable to `transfer`. When bill type is not `transfer`, the field returns "".  
to | String | The beneficiary account  
`6`: Funding account  
`18`: Trading account  
Only applicable to `transfer`. When bill type is not `transfer`, the field returns "".  
notes | String | Notes  
interest | String | Interest  
tag | String | Order tag  
fillTime | String | Last filled time  
tradeId | String | Last traded ID  
clOrdId | String | Client Order ID as assigned by the client  
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
fillIdxPx | String | Index price at the moment of trade execution  
For cross currency spot pairs, it returns baseCcy-USDT index price. For example, for LTC-ETH, this field returns the index price of LTC-USDT.  
fillMarkPx | String | Mark price when filled  
Applicable to FUTURES/SWAP/OPTIONS, return "" for other instrument types  
fillPxVol | String | Implied volatility when filled  
Only applicable to options; return "" for other instrument types  
fillPxUsd | String | Options price when filled, in the unit of USD  
Only applicable to options; return "" for other instrument types  
fillMarkVol | String | Mark volatility when filled  
Only applicable to options; return "" for other instrument types  
fillFwdPx | String | Forward price when filled  
Only applicable to options; return "" for other instrument types  
**Funding Fee expense (subType = 173)**  
You may refer to "pnl" for the fee payment 

### Get bills details (last 3 months)

Retrieve the account’s bills. The bill refers to all transaction records that result in changing the balance of an account. Pagination is supported, and the response is sorted with most recent first. This endpoint can retrieve data from the last 3 months.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/account/bills-archive`

> Request Example
    
    
    GET /api/v5/account/bills-archive
    
    GET /api/v5/account/bills-archive?instType=MARGIN
    
    
    
    
    import okx.Account as Account
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading:0 , demo trading:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # Get bills details (last 3 months)
    result = accountAPI.get_account_bills_archive()
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | No | Instrument type  
`SPOT`  
`MARGIN`  
`SWAP`  
`FUTURES`  
`OPTION`  
`EVENTS`  
instId | String | No | Instrument ID, e.g. `BTC-USDT`  
ccy | String | No | Bill currency  
mgnMode | String | No | Margin mode  
`isolated`  
`cross`  
ctType | String | No | Contract type  
`linear`  
`inverse`  
Only applicable to `FUTURES`/`SWAP`  
type | String | No | Bill type  
Please refer to [Get bill types](/docs-v5/en/#trading-account-rest-api-get-bill-types) for the list of available types.  
subType | String | No | Bill subtype  
Please refer to [Get bill types](/docs-v5/en/#trading-account-rest-api-get-bill-types) for the list of available types.  
after | String | No | Pagination of data to return records earlier than the requested bill ID.  
before | String | No | Pagination of data to return records newer than the requested bill ID.  
begin | String | No | Filter with a begin timestamp `ts`. Unix timestamp format in milliseconds, e.g. `1597026383085`  
end | String | No | Filter with an end timestamp `ts`. Unix timestamp format in milliseconds, e.g. `1597026383085`  
limit | String | No | Number of results per request. The maximum is `100`. The default is `100`.  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
            "bal": "8694.2179403378290202",
            "balChg": "0.0219338232210000",
            "billId": "623950854533513219",
            "ccy": "USDT",
            "clOrdId": "",
            "earnAmt": "",
            "earnApr": "",
            "execType": "T",
            "fee": "-0.000021955779",
            "fillFwdPx": "",
            "fillIdxPx": "27104.1",
            "fillMarkPx": "",
            "fillMarkVol": "",
            "fillPxUsd": "",
            "fillPxVol": "",
            "fillTime": "1695033476166",
            "from": "",
            "instId": "BTC-USDT",
            "instType": "SPOT",
            "interest": "0",
            "mgnMode": "isolated",
            "notes": "",
            "ordId": "623950854525124608",
            "pnl": "0",
            "posBal": "0",
            "posBalChg": "0",
            "px": "27105.9",
            "subType": "1",
            "sz": "0.021955779",
            "tag": "",
            "to": "",
            "tradeId": "586760148",
            "ts": "1695033476167",
            "type": "2"
        }]
    } 
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
instType | String | Instrument type  
billId | String | Bill ID  
type | String | Bill type  
subType | String | Bill subtype  
ts | String | The time when the balance complete update, Unix timestamp format in milliseconds, e.g.`1597026383085`  
balChg | String | Change in balance amount at the account level  
posBalChg | String | Change in balance amount at the position level  
bal | String | Balance at the account level  
posBal | String | Balance at the position level  
sz | String | Quantity  
For `FUTURES`/`SWAP`/`OPTION`, it is fill quantity or position quantity, the unit is contract. The value is always positive.  
For other scenarios. the unit is account balance currency(`ccy`).  
px | String | Price which related to subType  

* Trade filled price for
`1`: Buy `2`: Sell `3`: Open long `4`: Open short `5`: Close long `6`: Close short `204`: block trade buy `205`: block trade sell `206`: block trade open long `207`: block trade open short `208`: block trade close long `209`: block trade close short `114`: Forced repayment buy `115`: Forced repayment sell  

* Liquidation Price for
`100`: Partial liquidation close long `101`: Partial liquidation close short `102`: Partial liquidation buy `103`: Partial liquidation sell `104`: Liquidation long `105`: Liquidation short `106`: Liquidation buy `107`: Liquidation sell `16`: Repay forcibly `17`: Repay interest by borrowing forcibly `110`: Liquidation transfer in `111`: Liquidation transfer out  

* Delivery price for
`112`: Delivery long `113`: Delivery short  

* Exercise price for
`170`: Exercised `171`: Counterparty exercised `172`: Expired OTM  

* Mark price for
`173`: Funding fee expense `174`: Funding fee income  
ccy | String | Account balance currency  
pnl | String | Profit and loss  
fee | String | Fee  
Negative number represents the user transaction fee charged by the platform.   
Positive number represents rebate.  
[Trading fee rule](/en/fees)  
earnAmt | String | Auto earn amount  
Only applicable when type is 381  
earnApr | String | Auto earn APR  
Only applicable when type is 381  
mgnMode | String | Margin mode  
`isolated` `cross` `cash`  
When bills are not generated by trading, the field returns ""  
instId | String | Instrument ID, e.g. `BTC-USDT`  
ordId | String | Order ID  
Return order ID when the type is `2`/`5`/`9`  
Return "" when there is no order.  
execType | String | Liquidity taker or maker  
`T`: taker `M`: maker  
from | String | The remitting account  
`6`: Funding account  
`18`: Trading account  
Only applicable to `transfer`. When bill type is not `transfer`, the field returns "".  
to | String | The beneficiary account  
`6`: Funding account  
`18`: Trading account  
Only applicable to `transfer`. When bill type is not `transfer`, the field returns "".  
notes | String | Notes  
interest | String | Interest  
tag | String | Order tag  
fillTime | String | Last filled time  
tradeId | String | Last traded ID  
clOrdId | String | Client Order ID as assigned by the client   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
fillIdxPx | String | Index price at the moment of trade execution   
For cross currency spot pairs, it returns baseCcy-USDT index price. For example, for LTC-ETH, this field returns the index price of LTC-USDT.  
fillMarkPx | String | Mark price when filled   
Applicable to FUTURES/SWAP/OPTIONS, return "" for other instrument types  
fillPxVol | String | Implied volatility when filled   
Only applicable to options; return "" for other instrument types  
fillPxUsd | String | Options price when filled, in the unit of USD   
Only applicable to options; return "" for other instrument types  
fillMarkVol | String | Mark volatility when filled   
Only applicable to options; return "" for other instrument types  
fillFwdPx | String | Forward price when filled   
Only applicable to options; return "" for other instrument types  
**Funding Fee expense (subType = 173)**  
You may refer to "pnl" for the fee payment 

### Apply bills details (since 2021)

Apply for bill data since 1 February, 2021 except for the current quarter.

#### Rate Limit: 1 request per 10 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/account/bills-history-archive`

> Request Example
    
    
    POST /api/v5/account/bills-history-archive
    body
    {
        "year":"2023",
        "quarter":"Q1"
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
year | String | Yes | 4 digits year  
quarter | String | Yes | Quarter, valid value is `Q1`, `Q2`, `Q3`, `Q4`  
type | String | No | Bill type. Multiple values are supported, separated by commas, e.g. `1,2,3`. If not specified, all types are returned.  
Please refer to [Get bill types](/docs-v5/en/#trading-account-rest-api-get-bill-types) for the list of available types.  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "result": "true",
                "ts": "1646892328000"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
result | String | Whether there is already a download link for this section   
`true`: Existed, can check from "Get bills details (since 2021)".   
`false`: Does not exist and is generating, can check the download link after 2 hours  
The data of file is in reverse chronological order using `billId`.  
ts | String | The first request time when the server receives. Unix timestamp format in milliseconds, e.g. `1597026383085`  
The rule introduction, only applicable to the file generated after 11 October, 2024  
1\. Taking 2024 Q2 as an example. The date range are [2024-07-01, 2024-10-01). The begin date is included, The end date is excluded.  
2\. The data of file is in reverse chronological order using `billId`  Check the file link from the "Get bills details (since 2021)" endpoint in 2 hours to allow for data generation.   
During peak demand, data generation may take longer. If the file link is still unavailable after 3 hours, reach out to customer support for assistance.  It is only applicable to the data from the unified account. 

### Get bills details (since 2021)

Apply for bill data since 1 February, 2021 except for the current quarter.

#### Rate Limit: 10 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/account/bills-history-archive`

> Response Example
    
    
    GET /api/v5/account/bills-history-archive?year=2023&quarter=Q4
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
year | String | Yes | 4 digits year  
quarter | String | Yes | Quarter, valid value is `Q1`, `Q2`, `Q3`, `Q4`  
type | String | No | Bill type. Multiple values are supported, separated by commas, e.g. `1,2,3`. If not specified, all types are returned.  
Please refer to [Get bill types](/docs-v5/en/#trading-account-rest-api-get-bill-types) for the list of available types.  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "fileHref": "http://xxx",
                "state": "finished",
                "ts": "1646892328000"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
fileHref | String | Download file link.   
The expiration of every link is 5 and a half hours. If you already apply the files for the same quarter, then it don’t need to apply again within 30 days.  
ts | String | The first request time when the server receives. Unix timestamp format in milliseconds, e.g. `1597026383085`  
state | String | Download link status   
"finished" "ongoing" "failed": Failed, please apply again  
It is only applicable to the data from the unified account. 

#### Field descriptions in the decompressed CSV file

**Parameter** | **Type** | **Description**  
---|---|---  
instType | String | Instrument type  
billId | String | Bill ID  
subType | String | Bill subtype  
ts | String | The time when the balance complete update, Unix timestamp format in milliseconds, e.g.`1597026383085`  
balChg | String | Change in balance amount at the account level  
posBalChg | String | Change in balance amount at the position level  
bal | String | Balance at the account level  
posBal | String | Balance at the position level  
sz | String | Quantity  
px | String | Price which related to subType  

* Trade filled price for
`1`: Buy `2`: Sell `3`: Open long `4`: Open short `5`: Close long `6`: Close short `204`: block trade buy `205`: block trade sell `206`: block trade open long `207`: block trade open short `208`: block trade close long `209`: block trade close short `114`: Forced repayment buy `115`: Forced repayment sell  

* Liquidation Price for
`100`: Partial liquidation close long `101`: Partial liquidation close short `102`: Partial liquidation buy `103`: Partial liquidation sell `104`: Liquidation long `105`: Liquidation short `106`: Liquidation buy `107`: Liquidation sell `16`: Repay forcibly `17`: Repay interest by borrowing forcibly `110`: Liquidation transfer in `111`: Liquidation transfer out  

* Delivery price for
`112`: Delivery long `113`: Delivery short  

* Exercise price for
`170`: Exercised `171`: Counterparty exercised `172`: Expired OTM  

* Mark price for
`173`: Funding fee expense `174`: Funding fee income  
ccy | String | Account balance currency  
pnl | String | Profit and loss  
fee | String | Fee  
Negative number represents the user transaction fee charged by the platform.   
Positive number represents rebate.  
[Trading fee rule](/en/fees)  
mgnMode | String | Margin mode  
`isolated` `cross` `cash`  
When bills are not generated by trading, the field returns ""  
instId | String | Instrument ID, e.g. `BTC-USDT`  
ordId | String | Order ID  
Return order ID when the type is `2`/`5`/`9`  
Return "" when there is no order.  
execType | String | Liquidity taker or maker  
`T`: taker `M`: maker  
interest | String | Interest  
tag | String | Order tag  
fillTime | String | Last filled time  
tradeId | String | Last traded ID  
clOrdId | String | Client Order ID as assigned by the client   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
fillIdxPx | String | Index price at the moment of trade execution   
For cross currency spot pairs, it returns baseCcy-USDT index price. For example, for LTC-ETH, this field returns the index price of LTC-USDT.  
fillMarkPx | String | Mark price when filled   
Applicable to FUTURES/SWAP/OPTIONS, return "" for other instrument types  
fillPxVol | String | Implied volatility when filled   
Only applicable to options; return "" for other instrument types  
fillPxUsd | String | Options price when filled, in the unit of USD   
Only applicable to options; return "" for other instrument types  
fillMarkVol | String | Mark volatility when filled   
Only applicable to options; return "" for other instrument types  
fillFwdPx | String | Forward price when filled   
Only applicable to options; return "" for other instrument types  
  
### Get bill types

Get all bill types, and the mapping of bill type and subType.

#### Rate limit: 20 requests per 2 seconds

#### Rate limit rule: UserId

#### HTTP request

`GET /api/v5/account/subtypes`

> Request example
    
    
    GET /api/v5/account/subtypes
    

#### Request parameters

Parameter | Type | Required | Description  
---|---|---|---  
type | String | No | Bill type. Multiple values are supported, separated by commas, e.g. `1,2,3`. If not specified, all types are returned.  
  
> Response example
    
    
    {
        "code": "0",
        "data": [
            {
                "type": "1",
                "typeDesc": "Transfer",
                "subTypeDetails": [
                    {
                        "subType": "11",
                        "subTypeDesc": "Transfer in"
                    },
                    {
                        "subType": "12",
                        "subTypeDesc": "Transfer out"
                    }
                ]
            }
        ],
        "msg": ""
    }
    

#### Response parameters

Parameter | Type | Description  
---|---|---  
type | String | Bill type  
typeDesc | String | Bill type description, "" means the type is not enabled.  
subTypeDetails | Array of objects | Sub-type details  
> subType | String | Sub-type  
> subTypeDesc | String | Sub-type description, "" means the type is not enabled.  
  
### Get account configuration

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
  
### Set position mode

Futures mode and Multi-currency mode: `FUTURES` and `SWAP` support both `long/short` mode and `net` mode. In `net` mode, users can only have positions in one direction; In `long/short` mode, users can hold positions in long and short directions.  
Portfolio margin mode: `FUTURES` and `SWAP` only support `net` mode

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/account/set-position-mode`

> Request Example
    
    
    POST /api/v5/account/set-position-mode
    body 
    {
        "posMode":"long_short_mode"
    }
    
    
    
    
    import okx.Account as Account
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading:0 , demo trading:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # Set position mode
    result = accountAPI.set_position_mode(
        posMode="long_short_mode"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
posMode | String | Yes | Position mode  
`long_short_mode`: long/short, only applicable to `FUTURES`/`SWAP`  
`net_mode`: net  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
            "posMode": "long_short_mode"
        }]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
posMode | String | Position mode  
  
Portfolio margin account only supports net mode 

### Set leverage

  
There are 10 different scenarios for leverage setting:   
  
1\. Set leverage for `MARGIN` instruments under `isolated-margin` trade mode at pairs level.   
2\. Set leverage for `MARGIN` instruments under `cross-margin` trade mode and Spot mode (enabled borrow) at currency level.   
3\. Set leverage for `MARGIN` instruments under `cross-margin` trade mode and Futures mode account mode at pairs level.   
4\. Set leverage for `MARGIN` instruments under `cross-margin` trade mode and Multi-currency margin at currency level.   
5\. Set leverage for `MARGIN` instruments under `cross-margin` trade mode and Portfolio margin at currency level.   
6\. Set leverage for `FUTURES` instruments under `cross-margin` trade mode at underlying level.   
7\. Set leverage for `FUTURES` instruments under `isolated-margin` trade mode and buy/sell position mode at contract level.   
8\. Set leverage for `FUTURES` instruments under `isolated-margin` trade mode and long/short position mode at contract and position side level.   
9\. Set leverage for `SWAP` instruments under `cross-margin` trade at contract level.   
10\. Set leverage for `SWAP` instruments under `isolated-margin` trade mode and buy/sell position mode at contract level.   
11\. Set leverage for `SWAP` instruments under `isolated-margin` trade mode and long/short position mode at contract and position side level.   
  

Note that the request parameter `posSide` is only required when margin mode is isolated in long/short position mode for FUTURES/SWAP instruments (see scenario 8 and 11 above).   
Please refer to the request examples on the right for each case.   

#### Rate limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/account/set-leverage`

> Request Example
    
    
    # 1. Set leverage for `MARGIN` instruments under `isolated-margin` trade mode at pairs level.
    POST /api/v5/account/set-leverage
    body
    {
        "instId":"BTC-USDT",
        "lever":"5",
        "mgnMode":"isolated"
    }
    
    # 2. Set leverage for `MARGIN` instruments under `cross-margin` trade mode and Spot mode (enabled borrow) at currency level.
    POST /api/v5/account/set-leverage
    body
    {
        "ccy":"BTC",
        "lever":"5",
        "mgnMode":"cross"
    }
    
    # 3. Set leverage for `MARGIN` instruments under `cross-margin` trade mode and Futures mode account mode at pairs level.
    POST /api/v5/account/set-leverage
    body
    {
        "instId":"BTC-USDT",
        "lever":"5",
        "mgnMode":"cross"
    }
    
    # 4. Set leverage for `MARGIN` instruments under `cross-margin` trade mode and Multi-currency margin at currency level.
    POST /api/v5/account/set-leverage
    body
    {
        "ccy":"BTC",
        "lever":"5",
        "mgnMode":"cross"
    }
    
    # 5. Set leverage for `MARGIN` instruments under `cross-margin` trade mode and Portfolio margin at currency level.
    POST /api/v5/account/set-leverage
    body
    {
        "ccy":"BTC",
        "lever":"5",
        "mgnMode":"cross"
    }
    
    # 6. Set leverage for `FUTURES` instruments under `cross-margin` trade mode at underlying level.
    POST /api/v5/account/set-leverage
    body
    {
        "instId":"BTC-USDT-200802",
        "lever":"5",
        "mgnMode":"cross"
    }
    
    # 7. Set leverage for `FUTURES` instruments under `isolated-margin` trade mode and buy/sell order placement mode at contract level.
    POST /api/v5/account/set-leverage
    body
    {
        "instId":"BTC-USDT-200802",
        "lever":"5",
        "mgnMode":"isolated"
    }
    
    # 8. Set leverage for `FUTURES` instruments under `isolated-margin` trade mode and long/short order placement mode at contract and position side level.
    POST /api/v5/account/set-leverage
    body
    {
        "instId":"BTC-USDT-200802",
        "lever":"5",
        "posSide":"long",
        "mgnMode":"isolated"
    }
    
    # 9. Set leverage for `SWAP` instruments under `cross-margin` trade at contract level.
    POST /api/v5/account/set-leverage
    body
    {
        "instId":"BTC-USDT-SWAP",
        "lever":"5",
        "mgnMode":"cross"
    }
    
    # 10. Set leverage for `SWAP` instruments under `isolated-margin` trade mode and buy/sell order placement mode at contract level.
    POST /api/v5/account/set-leverage
    body
    {
        "instId":"BTC-USDT-SWAP",
        "lever":"5",
        "mgnMode":"isolated"
    }
    
    # 11. Set leverage for `SWAP` instruments under `isolated-margin` trade mode and long/short order placement mode at contract and position side level.
    POST /api/v5/account/set-leverage
    body
    {
        "instId":"BTC-USDT-SWAP",
        "lever":"5",
        "posSide":"long",
        "mgnMode":"isolated"
    }
    
    
    
    import okx.Account as Account
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading:0 , demo trading:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # Set leverage for MARGIN instruments under isolated-margin trade mode at pairs level.
    result = accountAPI.set_leverage(
        instId="BTC-USDT",
        lever="5",
        mgnMode="isolated"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instId | String | Conditional | Instrument ID  
Only applicable to `cross` `FUTURES` `SWAP` of `Spot mode`/`Multi-currency margin`/`Portfolio margin`, `cross` `MARGIN``FUTURES``SWAP` and `isolated` position.  
And required in applicable scenarios.  
ccy | String | Conditional | Currency used for margin, used for the leverage setting for the currency in auto borrow.  
Only applicable to `cross` `MARGIN` of `Spot mode`/`Multi-currency margin`/`Portfolio margin`.  
And required in applicable scenarios.  
lever | String | Yes | Leverage  
mgnMode | String | Yes | Margin mode  
`isolated` `cross`   
Can only be `cross` if `ccy` is passed.  
posSide | String | Conditional | Position side  
`long` `short`  
Only required when margin mode is `isolated` in `long/short` mode for `FUTURES`/`SWAP`.  
  
> Response Example
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
        {
          "lever": "30",
          "mgnMode": "isolated",
          "instId": "BTC-USDT-SWAP",
          "posSide": "long"
        }
      ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
lever | String | Leverage  
mgnMode | String | Margin mode  
`cross` `isolated`  
instId | String | Instrument ID  
posSide | String | Position side  
When setting leverage for `cross` `FUTURES`/`SWAP` at the underlying level, pass in any instId and mgnMode(`cross`).  Leverage cannot be adjusted for the cross positions of Expiry Futures and Perpetual Futures under the portfolio margin account. 

### Get maximum order quantity

The maximum quantity to buy or sell. It corresponds to the "sz" from placement.

Under the Portfolio Margin account, the calculation of the maximum buy/sell amount or open amount is not supported under the cross mode of derivatives. 

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/account/max-size`

> Request Example
    
    
    GET /api/v5/account/max-size?instId=BTC-USDT&tdMode=isolated
    
    
    
    
    import okx.Account as Account
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading:0 , demo trading:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # Get maximum buy/sell amount or open amount
    result = accountAPI.get_max_order_size(
        instId="BTC-USDT",
        tdMode="isolated"
    )
    print(result)
    

#### Request Parameters

**Parameter** | **Type** | Required | Description  
---|---|---|---  
instId | String | Yes | Single instrument or multiple instruments (no more than 5) in the same instrument type separated with comma, e.g. `BTC-USDT,ETH-USDT`  
tdMode | String | Yes | Trade mode  
`cross`  
`isolated`  
`cash`  
`spot_isolated`: only applicable to `Futures mode`.  
ccy | String | Conditional | Currency used for margin   
Applicable to `isolated` `MARGIN` and `cross` `MARGIN` orders in `Futures mode`.  
px | String | No | Price  
When the price is not specified, it will be calculated according to the current limit price for `FUTURES` and `SWAP`, the last traded price for other instrument types.  
The parameter will be ignored when multiple instruments are specified.  
leverage | String | No | Leverage for instrument  
The default is current leverage  
Only applicable to `MARGIN/FUTURES/SWAP`  
tradeQuoteCcy | String | No | The quote currency used for trading. Only applicable to `SPOT`.   
The default value is the quote currency of the `instId`, for example: for `BTC-USD`, the default is `USD`.  
outcome | String | No | Market outcome to trade on.  
`yes`  
`no`  
Only applicable and optional for `EVENTS`, the default value is `yes`  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
            "ccy": "BTC",
            "instId": "BTC-USDT",
            "maxBuy": "0.0500695098559788",
            "maxSell": "64.4798671570072269"
      }]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instId | String | Instrument ID  
ccy | String | Currency used for margin  
maxBuy | String | `SPOT`/`MARGIN`: The maximum quantity in base currency that you can buy  
The cross-margin order under `Futures mode` mode, quantity of coins is based on base currency.  
`FUTURES`/`SWAP`/`OPTIONS`: The maximum quantity of contracts that you can buy  
maxSell | String | `SPOT`/`MARGIN`: The maximum quantity in quote currency that you can sell  
The cross-margin order under `Futures mode` mode, quantity of coins is based on base currency.  
`FUTURES`/`SWAP`/`OPTIONS`: The maximum quantity of contracts that you can sell  
  
### Get maximum available balance/equity

Available balance for isolated margin positions and SPOT, available equity for cross margin positions.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/account/max-avail-size`

> Request Example
    
    
    # Query maximum available transaction amount when cross MARGIN BTC-USDT use BTC as margin
    GET /api/v5/account/max-avail-size?instId=BTC-USDT&tdMode=cross&ccy=BTC
    
    # Query maximum available transaction amount for SPOT BTC-USDT
    GET /api/v5/account/max-avail-size?instId=BTC-USDT&tdMode=cash
    
    
    
    
    import okx.Account as Account
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading:0 , demo trading:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # Get maximum available transaction amount for SPOT BTC-USDT
    result = accountAPI.get_max_avail_size(
        instId="BTC-USDT",
        tdMode="cash"
    )
    print(result)
    

#### Request Parameters

**Parameter** | **Type** | Required | Description  
---|---|---|---  
instId | String | Yes | Single instrument or multiple instruments (no more than 5) separated with comma, e.g. `BTC-USDT,ETH-USDT`  
ccy | String | Conditional | Currency used for margin  
Applicable to `isolated` `MARGIN` and `cross` `MARGIN` in `Futures mode`.  
tdMode | String | Yes | Trade mode  
`cross`  
`isolated`  
`cash`  
`spot_isolated`: only applicable to `Futures mode`  
reduceOnly | Boolean | No | Whether to reduce position only   
Only applicable to `MARGIN`  
px | String | No | The price of closing position.   
Only applicable to reduceOnly `MARGIN`.  
tradeQuoteCcy | String | No | The quote currency used for trading. Only applicable to `SPOT`.   
The default value is the quote currency of the `instId`, for example: for `BTC-USD`, the default is `USD`.  
  
> Response Example
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
        {
          "instId": "BTC-USDT",
          "availBuy": "100",
          "availSell": "1"
        }
      ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instId | String | Instrument ID  
availBuy | String | Maximum available balance/equity to buy  
availSell | String | Maximum available balance/equity to sell  
In the case of SPOT/MARGIN, availBuy is in the quote currency, and availSell is in the base currency.  
In the case of MARGIN with cross tdMode, both availBuy and availSell are in the currency passed in **ccy**. 

### Increase/decrease margin

Increase or decrease the margin of the isolated position. Margin reduction may result in the change of the actual leverage.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/account/position/margin-balance`

> Request Example
    
    
    POST /api/v5/account/position/margin-balance 
    body
    {
        "instId":"BTC-USDT-200626",
        "posSide":"short",
        "type":"add",
        "amt":"1"
    }
    
    
    
    
    import okx.Account as Account
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading:0 , demo trading:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # Increase margin
    result = accountAPI.adjustment_margin(
        instId="BTC-USDT-SWAP",
        posSide="short",
        type= "add",
        amt="1"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instId | String | Yes | Instrument ID  
posSide | String | Yes | Position side, the default is `net`  
`long`   
`short`   
`net`  
type | String | Yes | `add`: add margin   
`reduce`: reduce margin  
amt | String | Yes | Amount to be increased or decreased.  
ccy | String | Conditional | Currency   
Applicable to `isolated` `MARGIN` orders  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
                "amt": "0.3",
                "ccy": "BTC",
                "instId": "BTC-USDT",
                "leverage": "",
                "posSide": "net",
                "type": "add"
            }]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instId | String | Instrument ID  
posSide | String | Position side, `long` `short`  
amt | String | Amount to be increase or decrease  
type | String | `add`: add margin  
`reduce`: reduce margin  
leverage | String | Real leverage after the margin adjustment  
ccy | String | Currency  
Manual transfer mode  
The value of the margin initially assigned to the isolated position must be greater than or equal to 10,000 USDT, and a position will be created on the account. 

### Get leverage

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/account/leverage-info`

> Request Example
    
    
    GET /api/v5/account/leverage-info?instId=BTC-USDT-SWAP&mgnMode=cross
    
    
    
    
    import okx.Account as Account
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading:0 , demo trading:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # Get leverage
    result = accountAPI.get_leverage(
        instId="BTC-USDT-SWAP",
        mgnMode="cross"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instId | String | Conditional | Instrument ID  
Single instrument ID or multiple instrument IDs (no more than 20) separated with comma  
ccy | String | Conditional | Currency，used for getting leverage of currency level.  
Applicable to `cross` `MARGIN` of `Spot mode`/`Multi-currency margin`/`Portfolio margin`.  
Supported single currency or multiple currencies (no more than 20) separated with comma.  
mgnMode | String | Yes | Margin mode  
`cross` `isolated`  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
            "ccy":"",
            "instId": "BTC-USDT-SWAP",
            "mgnMode": "cross",
            "posSide": "long",
            "lever": "10"
        },{
            "ccy":"",
            "instId": "BTC-USDT-SWAP",
            "mgnMode": "cross",
            "posSide": "short",
            "lever": "10"
        }]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instId | String | Instrument ID  
ccy | String | Currency，used for getting leverage of currency level.  
Applicable to `cross` `MARGIN` of `Spot mode`/`Multi-currency margin`/`Portfolio margin`.  
mgnMode | String | Margin mode  
posSide | String | Position side  
`long`   
`short`   
`net`  
In `long/short` mode, the leverage in both directions `long`/`short` will be returned.  
lever | String | Leverage  
Leverage cannot be enquired for the cross positions of Expiry Futures and Perpetual Futures under the portfolio margin account. 

### Get leverage estimated info

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/account/adjust-leverage-info`

> Request Example
    
    
    GET /api/v5/account/adjust-leverage-info?instType=MARGIN&mgnMode=isolated&lever=3&instId=BTC-USDT
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | Yes | Instrument type  
`MARGIN`  
`SWAP`  
`FUTURES`  
mgnMode | String | Yes | Margin mode  
`isolated`  
`cross`  
lever | String | Yes | Leverage  
instId | String | Conditional | Instrument ID, e.g. BTC-USDT  
It is required for these scenarioes: `SWAP` and `FUTURES`, Margin isolation, Margin cross in `Futures mode`.  
ccy | String | Conditional | Currency used for margin, e.g. BTC  
It is required for isolated margin and cross margin in `Futures mode`, `Multi-currency margin` and `Portfolio margin`  
posSide | String | No | posSide  
`net`: The default value  
`long`  
`short`  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "estAvailQuoteTrans": "",
                "estAvailTrans": "1.1398040558348279",
                "estLiqPx": "",
                "estMaxAmt": "10.6095865868904898",
                "estMgn": "0.0701959441651721",
                "estQuoteMaxAmt": "176889.6871254563042714",
                "estQuoteMgn": "",
                "existOrd": false,
                "maxLever": "10",
                "minLever": "0.01"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
estAvailQuoteTrans | String | The estimated margin(in quote currency) can be transferred out under the corresponding leverage  
For cross, it is the maximum quantity that can be transferred from the trading account.  
For isolated, it is the maximum quantity that can be transferred from the isolated position  
Only applicable to `MARGIN`  
estAvailTrans | String | The estimated margin can be transferred out under the corresponding leverage.  
For cross, it is the maximum quantity that can be transferred from the trading account.  
For isolated, it is the maximum quantity that can be transferred from the isolated position  
The unit is base currency for `MARGIN`  
It is not applicable to the scenario when increasing leverage for isolated position under `FUTURES` and `SWAP`  
estLiqPx | String | The estimated liquidation price under the corresponding leverage. Only return when there is a position.  
estMgn | String | The estimated margin needed by position under the corresponding leverage.  
For the `MARGIN` position, it is margin in base currency  
estQuoteMgn | String | The estimated margin (in quote currency) needed by position under the corresponding leverage  
estMaxAmt | String | For `MARGIN`, it is the estimated maximum loan in base currency under the corresponding leverage  
For `SWAP` and `FUTURES`, it is the estimated maximum quantity of contracts that can be opened under the corresponding leverage  
estQuoteMaxAmt | String | The `MARGIN` estimated maximum loan in quote currency under the corresponding leverage.  
existOrd | Boolean | Whether there is pending orders   
`true`  
`false`  
maxLever | String | Maximum leverage  
minLever | String | Minimum leverage  
  
### Get the maximum loan of instrument

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/account/max-loan`

> Request Example
    
    
    # Max loan of cross `MARGIN` for currencies of trading pair in `Spot mode` (enabled borrowing)
    GET  /api/v5/account/max-loan?instId=BTC-USDT&mgnMode=cross
    
    # Max loan for currency in `Spot mode` (enabled borrowing)
    GET  /api/v5/account/max-loan?ccy=USDT&mgnMode=cross
    
    # Max loan of isolated `MARGIN` in `Futures mode`
    GET  /api/v5/account/max-loan?instId=BTC-USDT&mgnMode=isolated
    
    # Max loan of cross `MARGIN` in `Futures mode` (Margin Currency is BTC)
    GET  /api/v5/account/max-loan?instId=BTC-USDT&mgnMode=cross&mgnCcy=BTC
    
    # Max loan of cross `MARGIN` in `Multi-currency margin`
    GET  /api/v5/account/max-loan?instId=BTC-USDT&mgnMode=cross
    
    
    
    
    import okx.Account as Account
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading:0 , demo trading:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # Max loan of cross MARGIN in Futures mode (Margin Currency is BTC)
    result = accountAPI.get_max_loan(
        instId="BTC-USDT",
        mgnMode="cross",
        mgnCcy="BTC"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
mgnMode | String | Yes | Margin mode  
`isolated` `cross`  
instId | String | Conditional | Single instrument or multiple instruments (no more than 5) separated with comma, e.g. `BTC-USDT,ETH-USDT`  
ccy | String | Conditional | Currency  
Applicable to get Max loan of manual borrow for the currency in `Spot mode` (enabled borrowing)  
mgnCcy | String | Conditional | Margin currency  
Applicable to `isolated` `MARGIN` and `cross` `MARGIN` in `Futures mode`.  
tradeQuoteCcy | String | No | The quote currency for trading. Only applicable to `SPOT`.  
The default value is the quote currency of `instId`, e.g. `USD` for `BTC-USD`.  
  
> Response Example
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
        {
          "instId": "BTC-USDT",
          "mgnMode": "isolated",
          "mgnCcy": "",
          "maxLoan": "0.1",
          "ccy": "BTC",
          "side": "sell"
        },
        {
          "instId": "BTC-USDT",
          "mgnMode": "isolated",
          "mgnCcy": "",
          "maxLoan": "0.2",
          "ccy": "USDT",
          "side": "buy"
        }
      ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instId | String | Instrument ID  
mgnMode | String | Margin mode  
mgnCcy | String | Margin currency  
maxLoan | String | Max loan  
ccy | String | Currency  
side | String | Order side  
`buy` `sell`  
  
### Get fee rates

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/account/trade-fee`

> Request Example
    
    
    # Query trade fee rate of SPOT BTC-USDT
    GET /api/v5/account/trade-fee?instType=SPOT&instId=BTC-USDT
    
    
    
    import okx.Account as Account
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading:0 , demo trading:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # Get trading fee rates of current account
    result = accountAPI.get_fee_rates(
        instType="SPOT",
        instId="BTC-USDT"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | Yes | Instrument type  
`SPOT`  
`MARGIN`  
`SWAP`  
`FUTURES`  
`OPTION`  
`EVENTS`  
instId | String | No | Instrument ID, e.g. `BTC-USDT`  
Applicable to `SPOT`/`MARGIN`  
Specifying this parameter returns the correct applicable fee rates (e.g., market maker rates for users in incentive programs).  
instFamily | String | No | Instrument family, e.g. `BTC-USD`  
Applicable to `FUTURES`/`SWAP`/`OPTION`  
groupId | String | No | Instrument trading fee group ID  
Only one of groupId and instId/instFamily can be passed in  
  
Users can use instruments endpoint to fetch the mapping of an instrument ID and its trading fee group ID  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "category": "1",
                "delivery": "",
                "exercise": "",
                "feeGroup": [
                    {
                        "elpMaker": "-0.0008",
                        "groupId": "1",
                        "maker": "-0.0008",
                        "taker": "-0.001"
                    }
                ],
                "fiat": [],
                "instType": "SPOT",
                "level": "Lv1",
                "maker": "-0.0008",
                "makerU": "",
                "makerUSDC": "",
                "ruleType": "normal",
                "taker": "-0.001",
                "takerU": "",
                "takerUSDC": "",
                "ts": "1763979985847"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
level | String | Fee rate Level  
feeGroup | Array of objects | Fee groups.   
Applicable to `SPOT/MARGIN/SWAP/FUTURES/OPTION/EVENTS`  
> taker | String | Taker fee  
K1 parameter for `EVENTS` taker fee formula: `K1 × C × (P × (1-P))` (C = number of contracts, P = price)  
> maker | String | Maker fee  
K2 parameter for `EVENTS` maker fee formula: `K2 × C × (P × (1-P))` (C = number of contracts, P = price)  
> groupId | String | Instrument trading fee group ID  
  
**instType and groupId should be used together to determine a trading fee group. Users should use this endpoint together with[instruments endpoint](/docs-v5/en/#trading-account-rest-api-get-instruments) to get the trading fee of a specific symbol.**  
> elpMaker | String | ELP Maker effective fee rate. Returns `""` if ELP is not applicable to the instrument.  
delivery | String | Delivery fee rate  
exercise | String | Fee rate for exercising the option  
instType | String | Instrument type  
ts | String | Data return time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
taker | String | ~~For`SPOT`/`MARGIN`, it is taker fee rate of the USDT trading pairs.   
For `FUTURES`/`SWAP`/`OPTION`, it is the fee rate of crypto-margined contracts~~(deprecated)  
maker | String | ~~For`SPOT`/`MARGIN`, it is maker fee rate of the USDT trading pairs.   
For `FUTURES`/`SWAP`/`OPTION`, it is the fee rate of crypto-margined contracts~~(deprecated)  
takerU | String | ~~Taker fee rate of USDT-margined contracts, only applicable to`FUTURES`/`SWAP`~~(deprecated)  
makerU | String | ~~Maker fee rate of USDT-margined contracts, only applicable to`FUTURES`/`SWAP`~~(deprecated)  
takerUSDC | String | ~~For`SPOT`/`MARGIN`, it is taker fee rate of the USDⓈ&Crypto trading pairs.  
For `FUTURES`/`SWAP`, it is the fee rate of USDC-margined contracts~~(deprecated)  
makerUSDC | String | ~~For`SPOT`/`MARGIN`, it is maker fee rate of the USDⓈ&Crypto trading pairs.  
For `FUTURES`/`SWAP`, it is the fee rate of USDC-margined contracts~~(deprecated)  
ruleType | String | ~~Trading rule types  
`normal`: normal trading  
`pre_market`: pre-market trading~~(deprecated)  
category | String | ~~Currency category.~~(deprecated)  
fiat | Array of objects | ~~Details of fiat fee rate~~(deprecated)  
> ccy | String | Fiat currency.  
> taker | String | Taker fee rate  
> maker | String | Maker fee rate  
settle | String | Settlement fee rate for users whose positions match the event contract settlement result. Users holding the opposite positions will not be charged during settlement. Only applicable to `EVENTS`  
Remarks:   
The fee rate like maker and taker: positive number, which means the rate of rebate; negative number, which means the rate of commission.  
Exception: The values for delivery and exercise are positive numbers, representing the commission rate.  USDⓈ represent the stablecoin besides USDT  The Open API will not reflect zero-fee trading. For zero-fee pairs, please refer to [https://www.okx.com/fees ](https://www.okx.com/fees).  For users in market maker incentive programs: specifying `instId` (for `SPOT`/`MARGIN`) or `instFamily` (for `FUTURES`/`SWAP`/`OPTION`) returns the correct applicable fee rates. Without these parameters, the response reflects the organic base fee rates. 

### Get interest accrued data

Get the interest accrued data for the past year

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/account/interest-accrued`

> Request Example
    
    
    GET /api/v5/account/interest-accrued
    
    
    
    
    import okx.Account as Account
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading:0 , demo trading:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # Get interest accrued data
    result = accountAPI.get_interest_accrued()
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
type | String | No | Loan type  
`2`: Market loans  
Default is `2`  
ccy | String | No | Loan currency, e.g. `BTC`  
Only applicable to `Market loans`  
Only applicable to`MARGIN`  
instId | String | No | Instrument ID, e.g. `BTC-USDT`  
Only applicable to `Market loans`  
mgnMode | String | No | Margin mode  
`cross`   
`isolated`  
Only applicable to `Market loans`  
after | String | No | Pagination of data to return records earlier than the requested timestamp, Unix timestamp format in milliseconds, e.g. `1597026383085`  
before | String | No | Pagination of data to return records newer than the requested, Unix timestamp format in milliseconds, e.g. `1597026383085`  
limit | String | No | Number of results per request. The maximum is `100`. The default is `100`.  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "ccy": "USDT",
                "instId": "",
                "interest": "0.0003960833333334",
                "interestRate": "0.0000040833333333",
                "liab": "97",
                "totalLiab": "",
                "interestFreeLiab": "",
                "mgnMode": "",
                "ts": "1637312400000",
                "type": "1"
            },
            {
                "ccy": "USDT",
                "instId": "",
                "interest": "0.0004083333333334",
                "interestRate": "0.0000040833333333",
                "liab": "100",
                "mgnMode": "",
                "ts": "1637049600000",
                "type": "1"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
type | String | Loan type  
`2`: Market loans  
ccy | String | Loan currency, e.g. `BTC`  
instId | String | Instrument ID, e.g. `BTC-USDT`  
Only applicable to `Market loans`  
mgnMode | String | Margin mode  
`cross`   
`isolated`  
interest | String | Interest accrued  
interestRate | String | Hourly borrowing interest rate  
liab | String | Liability  
totalLiab | String | Total liability for current account  
interestFreeLiab | String | Interest-free liability for current account  
ts | String | Timestamp for interest accrued, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
### Get interest rate

Get the user's current leveraged currency borrowing market interest rate

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/account/interest-rate`

> Request Example
    
    
    GET /api/v5/account/interest-rate
    
    
    
    import okx.Account as Account
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading:0 , demo trading:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # Get the user's current leveraged currency borrowing interest rate
    result = accountAPI.get_interest_rate()
    print(result)
    

#### Request Parameters

**Parameters** | **Types** | **Required** | **Description**  
---|---|---|---  
ccy | String | No | Currency, e.g. `BTC`  
      
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "ccy":"BTC",
                "interestRate":"0.0001"
            },
            {
                "ccy":"LTC",
                "interestRate":"0.0003"
            }
        ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
interestRate | String | Hourly borrowing interest rate  
ccy | String | Currency  
  
### Set fee type

Set the fee type. 

fee type selection is only effective for Spot. 

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/account/set-fee-type`

> Request Example
    
    
    POST /api/v5/account/set-fee-type 
    body
    {
        "feeType":"0"
    }
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
feeType | String | Yes | Fee type  
`0`: fee is charged in the currency you receive from the trade (default)  
`1`: fee is always charged in the quote currency of the trading pair (only effective for Spot)  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "feeType": "0"
            }
        ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
feeType | String | Fee type  
`0`: fee is charged in the currency you receive from the trade  
`1`: fee is always charged in the quote currency of the trading pair  
  
### Set greeks (PA/BS)

Set the display type of Greeks.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/account/set-greeks`

> Request Example
    
    
    POST /api/v5/account/set-greeks 
    body
    {
        "greeksType":"PA"
    }
    
    
    
    
    import okx.Account as Account
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading:0 , demo trading:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # Set greeks (PA/BS)
    result = accountAPI.set_greeks(greeksType="PA")
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
greeksType | String | Yes | Display type of Greeks.  
`PA`: Greeks in coins   
`BS`: Black-Scholes Greeks in dollars  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
            "greeksType": "PA"
        }]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
greeksType | String | Display type of Greeks.  
  
### Isolated margin trading settings

You can set the currency margin and futures/perpetual Isolated margin trading mode

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/account/set-isolated-mode`

> Request Example
    
    
    POST /api/v5/account/set-isolated-mode
    body
    {
        "isoMode":"automatic",
        "type":"MARGIN"
    }
    
    
    
    import okx.Account as Account
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading:0 , demo trading:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # Isolated margin trading settings
    result = accountAPI.set_isolated_mode(
        isoMode="automatic",
        type="MARGIN"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
isoMode | String | Yes | Isolated margin trading settings  
`auto_transfers_ccy`: New auto transfers, enabling both base and quote currency as the margin for isolated margin trading. Only applicable to `MARGIN`.  
`automatic`: Auto transfers  
type | String | Yes | Instrument type  
`MARGIN`  
`CONTRACTS`  
When there are positions and pending orders in the current account, the margin transfer mode from position to position cannot be adjusted. 

> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "isoMode": "automatic"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
isoMode | String | Isolated margin trading settings  
`automatic`: Auto transfers  
CONTRACTS  
Auto transfers: Automatically occupy and release the margin when opening and closing positions  MARGIN  
Auto transfers: Automatically borrow and return coins when opening and closing positions 

### Get maximum withdrawals

Retrieve the maximum transferable amount from trading account to funding account. If no currency is specified, the transferable amount of all owned currencies will be returned.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/account/max-withdrawal`

> Request Example
    
    
    GET /api/v5/account/max-withdrawal
    
    
    
    
    import okx.Account as Account
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading:0 , demo trading:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # Get maximum withdrawals
    result = accountAPI.get_max_withdrawal()
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
ccy | String | No | Single currency or multiple currencies (no more than 20) separated with comma, e.g. `BTC` or `BTC,ETH`.  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
                "ccy": "BTC",
                "maxWd": "124",
                "maxWdEx": "125",
                "spotOffsetMaxWd": "",
                "spotOffsetMaxWdEx": ""
            },
            {
                "ccy": "ETH",
                "maxWd": "10",
                "maxWdEx": "12",
                "spotOffsetMaxWd": "",
                "spotOffsetMaxWdEx": ""
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
ccy | String | Currency  
maxWd | String | Max withdrawal (excluding borrowed assets under `Spot mode`/`Multi-currency margin`/`Portfolio margin`)  
maxWdEx | String | Max withdrawal (including borrowed assets under `Spot mode`/`Multi-currency margin`/`Portfolio margin`)  
spotOffsetMaxWd | String | Max withdrawal under Spot-Derivatives risk offset mode (excluding borrowed assets under `Portfolio margin`)  
Applicable to `Portfolio margin`  
spotOffsetMaxWdEx | String | Max withdrawal under Spot-Derivatives risk offset mode (including borrowed assets under `Portfolio margin`)  
Applicable to `Portfolio margin`  
  
### Get account risk state

Only applicable to Portfolio margin account

#### Rate Limit: 10 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/account/risk-state`

> Request Example
    
    
    GET /api/v5/account/risk-state
    
    
    
    import okx.Account as Account
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading:0 , demo trading:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # Get account risk state
    result = accountAPI.get_account_position_risk()
    print(result)
    

> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "atRisk": false,
                "atRiskIdx": [],
                "atRiskMgn": [],
                "ts": "1635745078794"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameters** | **Types** | **Description**  
---|---|---  
atRisk | Boolean | Account risk status in auto-borrow mode   
true: the account is currently in a specific risk state   
false: the account is currently not in a specific risk state  
atRiskIdx | Array of strings | derivatives risk unit list  
atRiskMgn | Array of strings | margin risk unit list  
ts | String | Unix timestamp format in milliseconds, e.g.`1597026383085`  
  
### Get borrow interest and limit

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/account/interest-limits`

> Request Example
    
    
    GET /api/v5/account/interest-limits?ccy=BTC
    
    
    
    
    import okx.Account as Account
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading:0 , demo trading:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # Get borrow interest and limit
    result = accountAPI.get_interest_limits(
        ccy="BTC"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
type | String | No | Loan type  
`2`: Market loans  
Default is `2`  
ccy | String | No | Loan currency, e.g. `BTC`  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "debt": "0.85893159114900247077000000000000",
                "interest": "0.00000000000000000000000000000000",
                "loanAlloc": "",
                "nextDiscountTime": "1729490400000",
                "nextInterestTime": "1729490400000",
                "records": [
                    {
                        "availLoan": "",
                        "avgRate": "",
                        "ccy": "BTC",
                        "interest": "0",
                        "loanQuota": "175.00000000",
                        "posLoan": "",
                        "rate": "0.0000276",
                        "surplusLmt": "175.00000000",
                        "surplusLmtDetails": {},
                        "usedLmt": "0.00000000",
                        "usedLoan": "",
                        "interestFreeLiab": "",
                        "potentialBorrowingAmt": ""
                    }
                ]
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
debt | String | Current debt in `USD`  
interest | String | Current interest in `USD`, the unit is `USD`  
Only applicable to `Market loans`  
nextDiscountTime | String | Next deduct time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
nextInterestTime | String | Next accrual time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
loanAlloc | String | VIP Loan allocation for the current trading account  
1\. The unit is percent(%). Range is [0, 100]. Precision is 0.01%  
2\. If master account did not assign anything, then "0"  
3\. "" if shared between master and sub-account  
records | Array of objects | Details for currencies  
> ccy | String | Loan currency, e.g. `BTC`  
> rate | String | Current daily borrowing rate  
> loanQuota | String | Borrow limit of master account  
If loan allocation has been assigned, then it is the borrow limit of the current trading account  
> surplusLmt | String | Available amount across all sub-accounts  
If loan allocation has been assigned, then it is the available amount to borrow by the current trading account  
> usedLmt | String | Borrowed amount for current account  
If loan allocation has been assigned, then it is the borrowed amount by the current trading account  
> interest | String | Interest to be deducted  
Only applicable to `Market loans`  
> interestFreeLiab | String | Interest-free liability for current account  
> potentialBorrowingAmt | String | Potential borrowing amount for current account  
> surplusLmtDetails | Object | ~~The details of available amount across all sub-accounts  
The value of `surplusLmt` is the minimum value within this array. It can help you judge the reason that `surplusLmt` is not enough.  
Only applicable to `VIP loans`~~Deprecated  
>> allAcctRemainingQuota | String | ~~Total remaining quota for master account and sub-accounts~~ Deprecated  
>> curAcctRemainingQuota | String | ~~The remaining quota for the current account.  
Only applicable to the case in which the sub-account is assigned the loan allocation~~Deprecated  
>> platRemainingQuota | String | ~~Remaining quota for the platform.  
The format like "600" will be returned when it is more than `curAcctRemainingQuota` or `allAcctRemainingQuota`~~Deprecated  
> posLoan | String | ~~Frozen amount for current account (Within the locked quota)  
Only applicable to `VIP loans`~~Deprecated  
> availLoan | String | ~~Available amount for current account (Within the locked quota)  
Only applicable to `VIP loans`~~Deprecated  
> usedLoan | String | ~~Borrowed amount for current account  
Only applicable to `VIP loans`~~Deprecated  
> avgRate | String | ~~Average hourly interest of borrowed coin  
only applicable to `VIP loans`~~Deprecated  
  
### Manual borrow / repay

Only applicable to `Spot mode` (enabled borrowing)

#### Rate Limit: 1 request per 3 seconds

#### Rate limit rule: Master Account User ID

#### HTTP Request

`POST /api/v5/account/spot-manual-borrow-repay`

> Request Example
    
    
    POST /api/v5/account/spot-manual-borrow-repay 
    body
    {
        "ccy":"USDT",
        "side":"borrow",
        "amt":"100"
    }
    
    
    
    import okx.Account as Account
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading:0 , demo trading:1
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    result = accountAPI.spot_manual_borrow_repay(ccy="USDT", side="borrow", amt= "1")
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
ccy | String | Yes | Currency, e.g. `BTC`  
side | String | Yes | Side  
`borrow`  
`repay`  
amt | String | Yes | Amount  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "ccy":"USDT",
                "side":"borrow",
                "amt":"100"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ccy | String | Currency, e.g. `BTC`  
side | String | Side  
`borrow`  
`repay`  
amt | String | Actual amount  
  
### Set auto repay

Only applicable to `Spot mode` (enabled borrowing)

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/account/set-auto-repay`

> Request Example
    
    
    POST /api/v5/account/set-auto-repay
    body
    {
        "autoRepay": true
    }
    
    
    
    import okx.Account as Account
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading:0 , demo trading:1
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    result = accountAPI.set_auto_repay(autoRepay=True)
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
autoRepay | Boolean | Yes | Whether auto repay is allowed or not under `Spot mode`  
`true`: Enable auto repay  
`false`: Disable auto repay  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "autoRepay": true
            }
        ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
autoRepay | Boolean | Whether auto repay is allowed or not under `Spot mode`  
`true`: Enable auto repay  
`false`: Disable auto repay  
  
### Get borrow/repay history

Retrieve the borrow/repay history under `Spot mode`

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/account/spot-borrow-repay-history`

> Request Example
    
    
    GET /api/v5/account/spot-borrow-repay-history
    
    
    
    import okx.Account as Account
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"   # Production trading:0 , demo trading:1
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    result = accountAPI.spot_borrow_repay_history(ccy="USDT", type="auto_borrow")
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
ccy | String | No | Currency, e.g. `BTC`  
type | String | No | Event type  
`auto_borrow`  
`auto_repay`  
`manual_borrow`  
`manual_repay`  
after | String | No | Pagination of data to return records earlier than the requested `ts` (included), Unix timestamp format in milliseconds, e.g. `1597026383085`  
before | String | No | Pagination of data to return records newer than the requested `ts`(included), Unix timestamp format in milliseconds, e.g. `1597026383085`  
limit | String | No | Number of results per request. The maximum is 100. The default is 100.  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "accBorrowed": "0",
                "amt": "6764.802661157592",
                "ccy": "USDT",
                "ts": "1725330976644",
                "type": "auto_repay"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ccy | String | Currency, e.g. `BTC`  
type | String | Event type  
`auto_borrow`  
`auto_repay`  
`manual_borrow`  
`manual_repay`  
amt | String | Amount  
accBorrowed | String | Accumulated borrow amount  
ts | String | Timestamp for the event, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
### Position builder (new)

Calculates portfolio margin information for virtual position/assets or current position of the user.  
You can add up to 200 virtual positions and 200 virtual assets in one request.

#### Rate Limit: 2 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/account/position-builder`

> Request Example
    
    
    # Both real and virtual positions and assets are calculated 
    POST /api/v5/account/position-builder
    body
    {
        "inclRealPosAndEq": false,
        "simPos":[
             {
                "pos":"-10",
                "instId":"BTC-USDT-SWAP",
                "avgPx":"100000"
             },
             {
                "pos":"10",
                "instId":"LTC-USDT-SWAP",
                "avgPx":"8000"
             }
        ],
        "simAsset":[
            {
                "ccy": "USDT",
                "amt": "100"
            }
        ],
        "greeksType":"CASH"
    }
    
    
    # Only existing real positions are calculated
    POST /api/v5/account/position-builder
    body
    {
       "inclRealPosAndEq":true
    }
    
    
    # Only virtual positions are calculated
    POST /api/v5/account/position-builder
    body
    {
        "acctLv": "4",
        "inclRealPosAndEq": false,
        "simPos":[
            {
                "pos":"10",
                "instId":"BTC-USDT-SWAP",
                "avgPx":"100000"
            },
            {
                "pos":"10",
                "instId":"LTC-USDT-SWAP",
                "avgPx":"8000"
            }
        ]
    }
    
    # Switch to Multi-currency margin mode
    POST /api/v5/account/position-builder
    body
    {
        "acctLv": "3",
        "lever":"10",
        "simPos":[
            {
                "pos":"10",
                "instId":"BTC-USDT-SWAP",
                "avgPx":"100000",
                "lever":"5"
            },
            {
                "pos":"10",
                "instId":"LTC-USDT-SWAP",
                "avgPx":"8000"
            }
        ]
    }
    
    
    
    import okx.Account as Account
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading:0 , demo trading:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    result = accountAPI.position_builder(
        inclRealPosAndEq=True,
        simPos=[
            {
                "pos": "10",
                "instId": "BTC-USDT-SWAP"
            },
            {
                "pos": "10",
                "instId": "LTC-USDT-SWAP"
            }
        ]
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
acctLv | String | No | Switch to account mode  
`3`: Multi-currency margin  
`4`: Portfolio margin  
The default is `4`  
inclRealPosAndEq | Boolean | No | Whether import existing positions and assets  
The default is `true`  
lever | String | No | Cross margin leverage in Multi-currency margin mode, the default is `1`.  
If the allowed leverage is exceeded, set according to the maximum leverage.  
Only applicable to `Multi-currency margin`  
simPos | Array of objects | No | List of simulated positions  
> instId | String | Yes | Instrument ID, e.g. `BTC-USDT-SWAP`  
Applicable to `SWAP`/`FUTURES`/`OPTION`  
> pos | String | Yes | Quantity of positions  
> avgPx | String | Yes | Average open price  
> lever | String | No | leverage  
Only applicable to `Multi-currency margin`  
The default is `1`  
If the allowed leverage is exceeded, set according to the maximum leverage.  
simAsset | Array of objects | No | List of simulated assets  
When `inclRealPosAndEq` is `true`, only real assets are considered and virtual assets are ignored  
> ccy | String | Yes | Currency, e.g. `BTC`  
> amt | String | Yes | Currency amount  
greeksType | String | No | Greeks type  
`BS`: Black-Scholes Model Greeks  
`PA`: Crypto Greeks  
`CASH`: Empirical Greeks  
The default is `BS`  
idxVol | String | No | Price volatility percentage, indicating what this price change means towards each of the values. In decimal form, range -0.99 ~ 1, in 0.01 increment.  
Default 0  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "acctLever": "-0.1364949794742562",
                "assets": [
                    {
                        "availEq": "0",
                        "borrowImr": "0",
                        "borrowMmr": "",
                        "ccy": "BTC",
                        "spotInUse": "0"
                    },
                    {
                        "availEq": "0",
                        "borrowImr": "0",
                        "borrowMmr": "",
                        "ccy": "LTC",
                        "spotInUse": "0"
                    },
                    {
                        "availEq": "0",
                        "borrowImr": "0",
                        "borrowMmr": "",
                        "ccy": "USDC",
                        "spotInUse": "0"
                    },
                    {
                        "availEq": "-78589.37",
                        "borrowImr": "7855.32188898",
                        "borrowMmr": "",
                        "ccy": "USDT",
                        "spotInUse": "0"
                    }
                ],
                "borrowMmr": "1571.064377796",
                "derivMmr": "1375.4837063088003",
                "eq": "-78553.21888979999",
                "marginRatio": "-25.95365779811705",
                "positions": [],
                "riskUnitData": [
                    {
                        "delta": "-9704.903689800001",
                        "gamma": "0",
                        "imrBf": "",
                        "imr": "1538.9669514070802",
                        "mmrBf": "",
                        "mmr": "1183.8207318516002",
                        "mr1": "1164.4109244719994",
                        "mr1FinalResult": {
                            "pnl": "-1164.4109244719994",
                            "spotShock": "0.12",
                            "volShock": "up"
                        },
                        "mr1Scenarios": {
                            "volSame": {
                                "0": "0",
                                "0.08": "-776.2739496480004",
                                "-0.08": "776.2739496480004",
                                "0.04": "-388.1369748240002",
                                "0.12": "-1164.4109244719994",
                                "-0.12": "1164.4109244719994",
                                "-0.04": "388.1369748240002"
                            },
                            "volShockDown": {
                                "0": "0",
                                "0.08": "-776.2739496480004",
                                "-0.08": "776.2739496480004",
                                "0.04": "-388.1369748240002",
                                "0.12": "-1164.4109244719994",
                                "-0.12": "1164.4109244719994",
                                "-0.04": "388.1369748240002"
                            },
                            "volShockUp": {
                                "0": "0",
                                "0.08": "-776.2739496480004",
                                "-0.08": "776.2739496480004",
                                "0.04": "-388.1369748240002",
                                "0.12": "-1164.4109244719994",
                                "-0.12": "1164.4109244719994",
                                "-0.04": "388.1369748240002"
                            }
                        },
                        "mr2": "0",
                        "mr3": "0",
                        "mr4": "19.4098073796",
                        "mr5": "0",
                        "mr6": "1164.4109244720003",
                        "mr6FinalResult": {
                            "pnl": "-2328.8218489440005",
                            "spotShock": "0.24"
                        },
                        "mr7": "43.67206660410001",
                        "mr8": "1571.064377796",
                        "mr9": "0",
                        "portfolios": [
                            {
                                "amt": "-10",
                                "avgPx": "100000",
                                "delta": "-9704.903689800001",
                                "floatPnl": "290.6300000000003",
                                "gamma": "0",
                                "instId": "BTC-USDT-SWAP",
                                "instType": "SWAP",
                                "isRealPos": false,
                                "markPxBf": "",
                                "markPx": "97093.7",
                                "notionalUsd": "9703.22",
                                "posSide": "net",
                                "theta": "0",
                                "vega": "0"
                            }
                        ],
                        "riskUnit": "BTC",
                        "theta": "0",
                        "upl": "290.49631020000027",
                        "vega": "0"
                    },
                    {
                        "delta": "1019.5308",
                        "gamma": "0",
                        "imrBf": "",
                        "imr": "249.16186679436",
                        "mmrBf": "",
                        "mmr": "191.6629744572",
                        "mr1": "183.50672805719995",
                        "mr1FinalResult": {
                            "pnl": "-183.50672805719995",
                            "spotShock": "-0.18",
                            "volShock": "up"
                        },
                        "mr1Scenarios": {
                            "volSame": {
                                "0": "0",
                                "-0.06": "-61.168909352399936",
                                "0.06": "61.168909352399936",
                                "-0.18": "-183.50672805719995",
                                "0.18": "183.50672805719995",
                                "0.12": "122.33781870480001",
                                "-0.12": "-122.33781870480001"
                            },
                            "volShockDown": {
                                "0": "0",
                                "-0.06": "-61.168909352399936",
                                "0.06": "61.168909352399936",
                                "-0.18": "-183.50672805719995",
                                "0.18": "183.50672805719995",
                                "0.12": "122.33781870480001",
                                "-0.12": "-122.33781870480001"
                            },
                            "volShockUp": {
                                "0": "0",
                                "-0.06": "-61.168909352399936",
                                "0.06": "61.168909352399936",
                                "-0.18": "-183.50672805719995",
                                "0.18": "183.50672805719995",
                                "0.12": "122.33781870480001",
                                "-0.12": "-122.33781870480001"
                            }
                        },
                        "mr2": "0",
                        "mr3": "0",
                        "mr4": "8.1562464",
                        "mr5": "0",
                        "mr6": "183.5067280572",
                        "mr6FinalResult": {
                            "pnl": "-367.0134561144",
                            "spotShock": "-0.36"
                        },
                        "mr7": "7.1367156",
                        "mr8": "1571.064377796",
                        "mr9": "0",
                        "portfolios": [
                            {
                                "amt": "10",
                                "avgPx": "8000",
                                "delta": "1019.5308",
                                "floatPnl": "-78980",
                                "gamma": "0",
                                "instId": "LTC-USDT-SWAP",
                                "instType": "SWAP",
                                "isRealPos": false,
                                "markPxBf": "",
                                "markPx": "102",
                                "notionalUsd": "1018.9",
                                "posSide": "net",
                                "theta": "0",
                                "vega": "0"
                            }
                        ],
                        "riskUnit": "LTC",
                        "theta": "0",
                        "upl": "-78943.6692",
                        "vega": "0"
                    }
                ],
                "totalImr": "9643.45070718144",
                "totalMmr": "2946.5480841048",
                "ts": "1736936801642",
                "upl": "-78653.1728898"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameters** | **Types** | **Description**  
---|---|---  
eq | String | Adjusted equity (`USD`) for the account  
totalMmr | String | Total MMR (`USD`) for the account  
totalImr | String | Total IMR (`USD`) for the account  
borrowMmr | String | Borrow MMR (`USD`) for the account  
derivMmr | String | Derivatives MMR (`USD`) for the account  
marginRatio | String | Cross maintenance margin ratio for the account  
upl | String | UPL for the account  
acctLever | String | Leverage of the account  
ts | String | Update time for the account, Unix timestamp format in milliseconds, e.g. `1597026383085`  
assets | Array of objects | Asset info  
> ccy | String | Currency, e.g. `BTC`  
> availEq | String | Currency equity  
> spotInUse | String | Spot in use  
> borrowMmr | String | ~~Borrowing MMR (`USD`)~~(Deprecated)  
> borrowImr | String | Borrowing IMR (`USD`)  
riskUnitData | Array of objects | Risk unit info  
> riskUnit | String | Risk unit, e.g. `BTC`  
> mmrBf | String | Risk unit MMR before volatility (`USD`)  
Return "" if users don't pass in idxVol  
> mmr | String | Risk unit MMR (`USD`)  
> imrBf | String | Risk unit IMR before volatility (`USD`)  
Return "" if users don't pass in idxVol  
> imr | String | Risk unit IMR (`USD`)  
> upl | String | Risk unit UPL (`USD`)  
> mr1 | String | Stress testing value of spot and volatility (all derivatives, and spot trading in spot-derivatives risk offset mode)  
> mr2 | String | Stress testing value of time value of money (TVM) (for options)  
> mr3 | String | Stress testing value of volatility span (for options)  
> mr4 | String | Stress testing value of basis (for all derivatives)  
> mr5 | String | Stress testing value of interest rate risk (for options)  
> mr6 | String | Stress testing value of extremely volatile markets (for all derivatives, and spot trading in spot-derivatives risk offset mode)  
> mr7 | String | Stress testing value of position reduction cost (for all derivatives)  
> mr8 | String | Borrowing MMR/IMR  
> mr9 | String | USDT-USDC-USD hedge risk  
> mr1Scenarios | Object | MR1 scenario analysis  
>> volShockDown | Object | When volatility shocks down, the P&L of stress tests under different price volatility ratios, format in {`change`: `value`,...}  
`change`: price volatility ratio (in percentage), e.g. `0.01` representing `1%`  
`value`: P&L under stress tests, measured in `USD`  
e.g. {"-0.15":"-2333.23", ...}  
>> volSame | Object | When volatility keeps the same, the P&L of stress tests under different price volatility ratios, format in {`change`: `value`,...}  
`change`: price volatility ratio (in percentage), e.g. `0.01` representing `1%`  
`value`: P&L under stress tests, measured in `USD`  
e.g. {"-0.15":"-2333.23", ...}  
>> volShockUp | Object | When volatility shocks up, the P&L of stress tests under different price volatility ratios, format in {`change`: `value`,...}  
`change`: price volatility ratio (in percentage), e.g. `0.01` representing `1%`  
`value`: P&L under stress tests, measured in `USD`  
e.g. {"-0.15":"-2333.23", ...}  
> mr1FinalResult | Object | MR1 worst-case scenario  
>> pnl | String | MR1 stress P&L (`USD`)  
>> spotShock | String | MR1 worst-case scenario spot shock (in percentage), e.g. `0.01` representing `1%`  
>> volShock | String | MR1 worst-case scenario volatility shock  
`down`: volatility shock down  
`unchange`: volatility unchanged  
`up`: volatility shock up  
> mr6FinalResult | Object | MR6 scenario analysis  
>> pnl | String | MR6 stress P&L (`USD`)  
>> spotShock | String | MR6 worst-case scenario spot shock (in percentage), e.g. `0.01` representing `1%`  
> delta | String | (Risk unit) The rate of change in the contract’s price with respect to changes in the underlying asset’s price.   
When the price of the underlying changes by x, the option’s price changes by delta multiplied by x.  
> gamma | String | (Risk unit) The rate of change in the delta with respect to changes in the underlying price.   
When the price of the underlying changes by x%, the option’s delta changes by gamma multiplied by x%.  
> theta | String | (Risk unit) The change in contract price each day closer to expiry.  
> vega | String | (Risk unit) The change of the option price when underlying volatility increases by 1%.  
> portfolios | Array of objects | Portfolios info  
Only applicable to `Portfolio margin`  
>> instId | String | Instrument ID, e.g. `BTC-USDT-SWAP`  
>> instType | String | Instrument type  
`SPOT`  
`SWAP`  
`FUTURES`  
`OPTION`  
>> amt | String | When `instType` is `SPOT`, it represents spot in use.  
When `instType` is `SWAP`/`FUTURES`/`OPTION`, it represents position amount.  
>> posSide | String | Position side  
`long`  
`short`  
`net`  
>> avgPx | String | Average open price  
>> markPxBf | String | Mark price before price volatility  
Return "" if users don't pass in idxVol  
>> markPx | String | Mark price  
>> floatPnl | String | Float P&L  
>> notionalUsd | String | Notional in `USD`  
>> delta | String | When `instType` is `SPOT`, it represents asset amount.  
When `instType` is `SWAP`/`FUTURES`/`OPTION`, it represents the rate of change in the contract’s price with respect to changes in the underlying asset’s price (by Instrument ID).  
>> gamma | String | The rate of change in the delta with respect to changes in the underlying price (by Instrument ID).   
When `instType` is `SPOT`, it will return "".  
>> theta | String | The change in contract price each day closer to expiry (by Instrument ID).  
When `instType` is `SPOT`, it will return "".  
>> vega | String | The change of the option price when underlying volatility increases by 1% (by Instrument ID).  
When `instType` is `SPOT`, it will return "".  
>> isRealPos | Boolean | Whether it is a real position  
If `instType` is `SWAP`/`FUTURES`/`OPTION`, it is a valid parameter, else it will return `false`  
positions | Array of objects | Position info  
Only applicable to `Multi-currency margin`  
> instId | String | Instrument ID, e.g. `BTC-USDT-SWAP`  
> instType | String | Instrument type  
`SPOT`  
`SWAP`  
`FUTURES`  
`OPTION`  
> amt | String | When `instType` is `SPOT`, it represents spot in use.  
When `instType` is `SWAP`/`FUTURES`/`OPTION`, it represents position amount.  
> posSide | String | Position side  
`long`  
`short`  
`net`  
> avgPx | String | Average open price  
> markPxBf | String | Mark price before price volatility  
Return "" if users don't pass in idxVol  
> markPx | String | Mark price  
> floatPnl | String | Float P&L  
> imrBf | String | IMR before price volatility  
> imr | String | IMR  
> mgnRatio | String | Maintenance margin ratio  
> lever | String | Leverage  
> notionalUsd | String | Notional in `USD`  
> isRealPos | Boolean | Whether it is a real position  
If `instType` is `SWAP`/`FUTURES`/`OPTION`, it is a valid parameter, else it will return `false`  
  
### Position builder trend graph

#### Rate limit: 1 request per 5 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/account/position-builder-graph`

> Request Example
    
    
    {
       "inclRealPosAndEq":false,
       "simPos":[
          {
             "pos":"-10",
             "instId":"BTC-USDT-SWAP",
             "avgPx":"100000"
          },
          {
             "pos":"10",
             "instId":"LTC-USDT-SWAP",
             "avgPx":"8000"
          }
       ],
       "simAsset":[
          {
             "ccy":"USDT",
             "amt":"100"
          }
       ],
       "greeksType":"CASH",
       "type":"mmr",
       "mmrConfig":{
          "acctLv":"3",
          "lever":"1"
       }
    }
    

#### Request Parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
inclRealPosAndEq | Boolean | No | Whether to import existing positions and assets  
The default is `true`  
simPos | Array of objects | No | List of simulated positions  
> instId | String | Yes | Instrument ID, e.g. `BTC-USDT-SWAP`  
Applicable to `SWAP`/`FUTURES`/`OPTION`  
> pos | String | Yes | Quantity of positions  
> avgPx | String | Yes | Average open price  
> lever | String | No | leverage  
Only applicable to `Multi-currency margin`  
The default is `1`  
If the allowed leverage is exceeded, set according to the maximum leverage.  
simAsset | Array of objects | No | List of simulated assets  
When `inclRealPosAndEq` is `true`, only real assets are considered and virtual assets are ignored  
> ccy | String | Yes | Currency, e.g. `BTC`  
> amt | String | Yes | Currency amount  
type | String | Yes | Trending graph type  
`mmr`  
mmrConfig | Object | Yes | MMR configuration  
> acctLv | String | No | Switch to account mode  
`3`: Multi-currency margin  
`4`: Portfolio margin  
> lever | String | No | Cross margin leverage in Multi-currency margin mode, the default is `1`.  
If the allowed leverage is exceeded, set according to the maximum leverage.  
Only applicable to `Multi-currency margin`  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
             {
                "type": "mmr",
                "mmrData": [
                   ......
                   {
                         "mmr": "1415.0254039225917",
                         "mmrRatio": "-47.45603627655477",
                         "shockFactor": "-0.94"
                   },
                   {
                         "mmr": "1417.732491243024",
                         "mmrRatio": "-47.436684685735386",
                         "shockFactor": "-0.93"
                   }
                   ......
                ]
             }
        ],
        "msg": ""
    }
    
    

#### Response Parameters

**Parameters** | **Types** | **Description**  
---|---|---  
type | String | Graph type  
`mmr`  
mmrData | Array | Array of mmrData  
Return data in shockFactor ascending order  
> shockFactor | String | Price change ratio, data range -1 to 1.  
> mmr | String | Mmr at specific price  
> mmrRatio | String | Maintenance margin ratio at specific price  
  
### Set risk offset amount

Set risk offset amount. This does not represent the actual spot risk offset amount. Only applicable to Portfolio Margin Mode.

#### Rate Limit: 10 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/account/set-riskOffset-amt`

> Request Example
    
    
    # Set spot risk offset amount
    POST /api/v5/account/set-riskOffset-amt
    body
    {
       "ccy": "BTC",
       "clSpotInUseAmt": "0.5"
    }
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
ccy | String | Yes | Currency  
clSpotInUseAmt | String | Yes | Spot risk offset amount defined by users  
  
> Response Example
    
    
    {
       "code": "0",
       "msg": "",
       "data": [
          {
             "ccy": "BTC",
             "clSpotInUseAmt": "0.5"
          }
       ]
    }
    

#### Response Parameters

Parameters | Types | Description  
---|---|---  
ccy | String | Currency  
clSpotInUseAmt | String | Spot risk offset amount defined by users  
  
### Get Greeks

Retrieve a greeks list of all assets in the account.

#### Rate Limit: 10 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/account/greeks`

> Request Example
    
    
    # Get the greeks of all assets in the account
    GET /api/v5/account/greeks
    
    # Get the greeks of BTC assets in the account
    GET /api/v5/account/greeks?ccy=BTC
    
    
    
    
    import okx.Account as Account
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading:0 , demo trading:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # Retrieve a greeks list of all assets in the account
    result = accountAPI.get_greeks()
    print(result)
    

#### Request Parameters

**Parameters** | **Types** | **Required** | **Description**  
---|---|---|---  
ccy | String | No | Single currency, e.g. `BTC`.  
  
> Response Example
    
    
    {
        "code":"0",
        "data":[
            {            
               "thetaBS": "",
               "thetaPA":"",
               "deltaBS":"",
               "deltaPA":"",
               "gammaBS":"",
               "gammaPA":"",
               "vegaBS":"",    
               "vegaPA":"",
               "ccy":"BTC",
               "ts":"1620282889345"
            }
        ],
        "msg":""
    }
    

#### Response Parameters

**Parameters** | **Types** | **Description**  
---|---|---  
deltaBS | String | delta: Black-Scholes Greeks in dollars  
deltaPA | String | delta: Greeks in coins  
gammaBS | String | gamma: Black-Scholes Greeks in dollars, only applicable to OPTION  
gammaPA | String | gamma: Greeks in coins, only applicable to OPTION  
thetaBS | String | theta: Black-Scholes Greeks in dollars, only applicable to `OPTION`  
thetaPA | String | theta: Greeks in coins, only applicable to `OPTION`  
vegaBS | String | vega: Black-Scholes Greeks in dollars, only applicable to `OPTION`  
vegaPA | String | vega：Greeks in coins, only applicable to `OPTION`  
ccy | String | Currency  
ts | String | Time of getting Greeks, Unix timestamp format in milliseconds, e.g. 1597026383085  
  
### Get PM position limitation

Retrieve cross position limitation of SWAP/FUTURES/OPTION under Portfolio margin mode.

#### Rate Limit: 10 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/account/position-tiers`

> Request Example
    
    
    # Query limitation of BTC-USDT
    GET /api/v5/account/position-tiers?instType=SWAP&uly=BTC-USDT
    
    
    
    
    import okx.Account as Account
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading:0 , demo trading:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # Get PM position limitation
    result = accountAPI.get_account_position_tiers(
        instType="SWAP",
        uly="BTC-USDT"
    )
    print(result)
    

#### Request Parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
instType | String | Yes | Instrument type  
`SWAP`  
`FUTURES`  
`OPTION`  
instFamily | String | Yes | Single instrument family or instrument families (no more than 5) separated with comma.  
  
> Response Example
    
    
    {
      "code": "0",
      "data": [
        {
          "instFamily": "BTC-USDT",
          "maxSz": "10000",
          "posType": "",
          "uly": "BTC-USDT"
        }
      ],
      "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
uly | String | Underlying  
Applicable to `FUTURES`/`SWAP`/`OPTION`  
instFamily | String | Instrument family  
Applicable to `FUTURES`/`SWAP`/`OPTION`  
maxSz | String | Max number of positions  
posType | String | Limitation of position type, only applicable to cross `OPTION` under portfolio margin mode   
`1`: Contracts of pending orders and open positions for all derivatives instruments. `2`: Contracts of pending orders for all derivatives instruments. `3`: Pending orders for all derivatives instruments. `4`: Contracts of pending orders and open positions for all derivatives instruments on the same side. `5`: Pending orders for one derivatives instrument. `6`: Contracts of pending orders and open positions for one derivatives instrument. `7`: Contracts of one pending order.  
  
### Activate option

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/account/activate-option`

> Request Example
    
    
    POST /api/v5/account/activate-option
    
    

#### Request Parameters

None

> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
            "ts": "1600000000000"
        }]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ts | String | Activation time  
  
### Set auto loan

Only applicable to `Multi-currency margin` and `Portfolio margin`

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/account/set-auto-loan`

> Request Example
    
    
    POST /api/v5/account/set-auto-loan
    body
    {
        "autoLoan":true,
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
autoLoan | Boolean | No | Whether to automatically make loans   
Valid values are `true`, `false`   
The default is `true`  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
            "autoLoan": true
        }]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
autoLoan | Boolean | Whether to automatically make loans  
  
### Preset account mode switch

Pre-set the required information for account mode switching. When switching from `Portfolio margin mode` back to `Futures mode` / `Multi-currency margin mode`, and if there are existing cross-margin contract positions, it is mandatory to pre-set leverage.

If the user does not follow the required settings, they will receive an error message during the pre-check or when setting the account mode.

#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/account/account-level-switch-preset`

> Request example
    
    
    # 1. Futures mode -> Multi-currency margin mode
    POST /api/v5/account/account-level-switch-preset
    {
        "acctLv": "3"
    }
    
    # 2. Multi-currency margin mode -> Futures mode
    POST /api/v5/account/account-level-switch-preset
    {
        "acctLv": "2"
    }
    
    # 3. Portfolio margin mode -> Futures mode/Multi-currency margin mode, the user have cross-margin contract position and lever is required
    POST /api/v5/account/account-level-switch-preset
    {
        "acctLv": "2",
        "lever": "10"
    }
    
    # 4. Portfolio margin mode -> Futures mode/Multi-currency margin mode, the user doesn't have cross-margin contract position and lever is not required
    POST /api/v5/account/account-level-switch-preset
    {
        "acctLv": "3"
    }
    
    

#### Request parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
acctLv | String | Yes | Account mode  
`2`: Futures mode  
`3`: Multi-currency margin code  
`4`: Portfolio margin mode  
lever | String | Optional | Leverage  
Required when switching from Portfolio margin mode to `Futures mode` or `Multi-currency margin mode`, and the user holds cross-margin positions.  
riskOffsetType | String | Optional | ~~Risk offset type  
`1`: Spot-derivatives (USDT) risk offset  
`2`: Spot-derivatives (Crypto) risk offset  
`3`: Derivatives only mode  
`4`: Spot-derivatives (USDC) risk offset  
Applicable when switching from Futures mode or Multi-currency margin mode to Portfolio margin mode.~~(Deprecated)  
  
> Response example 1. Futures mode -> Multi-currency margin mode
    
    
    {
        "acctLv": "3",
        "curAcctLv": "2",
        "lever": "",
        "riskOffsetType": ""
    }
    

> Response example 2. Multi-currency margin mode -> Futures mode
    
    
    {
        "acctLv": "2",
        "curAcctLv": "3",
        "lever": "",
        "riskOffsetType": ""
    }
    

> Response example 3. Portfolio margin mode -> Futures mode/Multi-currency margin mode
    
    
    {
        "acctLv": "2",
        "curAcctLv": "4",
        "lever": "10",
        "riskOffsetType": ""
    }
    

> Response example 4. Portfolio margin mode -> Futures mode/Multi-currency margin mode
    
    
    {
        "acctLv": "3",
        "curAcctLv": "4",
        "lever": "",
        "riskOffsetType": ""
    }
    

#### Response parameters

**Parameter** | **Type** | **Description**  
---|---|---  
curAcctLv | String | Current account mode  
acctLv | String | Account mode after switch  
lever | String | The leverage user preset for cross-margin positions  
riskOffsetType | String | ~~The risk offset type user preset~~(Deprecated)  
  
lever: When switching from Portfolio margin mode to Futures mode or Multi-currency margin mode, if the user holds cross-margin positions, this parameter must be provided; otherwise, error code 50014 will occur. The maximum allowable value for this parameter is determined by the smallest maximum leverage based on current position sizes under the target mode. For example, if a user in PM mode holds three cross-margin positions, with maximum allowable leverage of 20x, 50x, and 100x respectively, the maximum leverage it can set is 20x. 

### Precheck account mode switch

Retrieve precheck information for account mode switching.

#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/account/set-account-switch-precheck`

> Request example
    
    
    GET /api/v5/account/set-account-switch-precheck?acctLv=3
    
    

#### Request parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
acctLv | String | Yes | Account mode  
`1`: Spot mode  
`2`: Futures mode  
`3`: Multi-currency margin code  
`4`: Portfolio margin mode  
  
> Response example. Futures mode->Portfolio margin mode, need to finish the Q&A on web or mobile first
    
    
    {
        "code": "51070",
        "data": [],
        "msg": "You do not meet the requirements for switching to this account mode. Please upgrade the account mode on the OKX website or App"
    }
    

> Response example. Futures mode->Portfolio margin mode, unmatched information. sCode 1
    
    
    {
        "code": "0",
        "data": [
            {
                "acctLv": "3",
                "curAcctLv": "1",
                "mgnAft": null,
                "mgnBf": null,
                "posList": [],
                "posTierCheck": [],
                "riskOffsetType": "",
                "sCode": "1",
                "unmatchedInfoCheck": [
                    {
                        "posList": [],
                        "totalAsset": "",
                        "type": "repay_borrowings"
                    }
                ]
            }
        ],
        "msg": ""
    }
    

> Response example. Portfolio margin mode->Multi-currency margin code, the user has cross-margin positions but doesn't preset leverage. sCode 3 
    
    
    {
        "code": "0",
        "data": [
            {
                "acctLv": "3",
                "curAcctLv": "4",
                "mgnAft": null,
                "mgnBf": null,
                "posList": [
                    {
                        "lever": "50",
                        "posId": "2005456500916518912"
                    },
                    {
                        "lever": "10",
                        "posId": "2005456108363218944"
                    },
                    {
                        "lever": "100",
                        "posId": "2005456332909477888"
                    },
                    {
                        "lever": "1",
                        "posId": "2005456415990251520"
                    }
                ],
                "posTierCheck": [],
                "riskOffsetType": "",
                "sCode": "3",
                "unmatchedInfoCheck": []
            }
        ],
        "msg": ""
    }
    

> Response example. Portfolio margin mode->Multi-currency margin code, the user finishes the leverage setting to 10, and passes the position tier an margin check. sCode 0. 
    
    
    {
        "code": "0",
        "data": [
            {
                "acctLv": "3",
                "curAcctLv": "4",
                "mgnAft": {
                    "acctAvailEq": "106002.2061970689",
                    "details": [],
                    "mgnRatio": "148.1652396878421"
                },
                "mgnBf": {
                    "acctAvailEq": "77308.89735228613",
                    "details": [],
                    "mgnRatio": "4.460069474634038"
                },
                "posList": [
                    {
                        "lever": "50",
                        "posId": "2005456500916518912"
                    },
                    {
                        "lever": "50",
                        "posId": "2005456108363218944"
                    },
                    {
                        "lever": "50",
                        "posId": "2005456332909477888"
                    },
                    {
                        "lever": "50",
                        "posId": "2005456415990251520"
                    }
                ],
                "posTierCheck": [],
                "riskOffsetType": "",
                "sCode": "0",
                "unmatchedInfoCheck": []
            }
        ],
        "msg": ""
    }
    
    

#### Response parameters

**Parameter** | **Type** | **Description**  
---|---|---  
sCode | String | Check code  
`0`: pass all checks  
`1`: unmatched information  
`3`: leverage setting is not finished  
`4`: position tier or margin check is not passed  
curAcctLv | String | Account mode  
`1`: Spot mode  
`2`: Futures mode  
`3`: Multi-currency margin code  
`4`: Portfolio margin mode  
Applicable to all scenarios  
acctLv | String | Account mode  
`1`: Spot mode  
`2`: Futures mode  
`3`: Multi-currency margin code  
`4`: Portfolio margin mode  
Applicable to all scenarios  
riskOffsetType | String | ~~Risk offset type  
`1`: Spot-derivatives (USDT) risk offset  
`2`: Spot-derivatives (Crypto) risk offset  
`3`: Derivatives only mode  
`4`: Spot-derivatives (USDC) risk offset  
Applicable when acctLv is `4`, return "" for other scenarios  
If the user preset before, it will use the user's specified value; if not, the default value `3` will be applied~~(Deprecated)  
unmatchedInfoCheck | Array of objects | Unmatched information list  
Applicable when sCode is `1`, indicating there is unmatched information; return [] for other scenarios  
>> type | String | Unmatched information type  
`asset_validation`: asset validation  
`pending_orders`: order book pending orders  
`pending_algos`: pending algo orders and trading bots, such as iceberg, recurring buy and twap  
`isolated_margin`: isolated margin (quick margin and manual transfers)  
`isolated_contract`: isolated contract (manual transfers)  
`contract_long_short`: contract positions in hedge mode  
`cross_margin`: cross margin positions  
`cross_option_buyer`: cross options buyer  
`isolated_option`: isolated options (only applicable to spot mode)  
`growth_fund`: positions with trial funds  
`all_positions`: all positions  
`spot_lead_copy_only_simple_single`: copy trader and customize lead trader can only use spot mode or Futures mode  
`stop_spot_custom`: spot customize copy trading  
`stop_futures_custom`: contract customize copy trading  
`lead_portfolio`: lead trader can not switch to portfolio margin mode  
`futures_smart_sync`: you can not switch to spot mode when having smart contract sync  
`vip_fixed_loan`: vip loan  
`repay_borrowings`: borrowings  
`compliance_restriction`: due to compliance restrictions, margin trading services are unavailable  
`compliance_kyc2`: Due to compliance restrictions, margin trading services are unavailable. If you are not a resident of this region, please complete kyc2 identity verification.  
>> totalAsset | String | Total assets  
Only applicable when type is `asset_validation`, return "" for other scenarios  
>> posList | Array of strings | Unmatched position list (posId)  
Applicable when type is related to positions, return [] for other scenarios  
posList | Array of objects | Cross margin contract position list  
Applicable when curAcctLv is `4`, acctLv is `2/3` and user has cross margin contract positions  
Applicable when sCode is `0/3/4`  
> posId | String | Position ID  
> lever | String | Leverage of cross margin contract positions after switch  
posTierCheck | Array of objects | Cross margin contract positions that don't pass the position tier check  
Only applicable when sCode is `4`  
> instFamily | String | Instrument family  
> instType | String | Instrument type  
`SWAP`  
`FUTURES`  
`OPTION`  
> pos | String | Quantity of position  
> lever | String | Leverage  
> maxSz | String | If acctLv is `2/3`, it refers to the maximum position size allowed at the current leverage. If acctLv is `4`, it refers to the maximum position limit for cross-margin positions under the PM mode.  
mgnBf | Object | The margin related information before switching account mode  
Applicable when sCode is `0/4`, return null for other scenarios  
> acctAvailEq | String | Account available equity in USD  
Applicable when curAcctLv is `3/4`, return "" for other scenarios  
> mgnRatio | String | Maintenance Margin ratio in USD  
Applicable when curAcctLv is `3/4`, return "" for other scenarios  
> details | Array of objects | Detailed information  
Only applicable when curAcctLv is `2`, return "" for other scenarios  
>> ccy | String | Currency  
>> availEq | String | Available equity of currency  
>> mgnRatio | String | Maintenance margin ratio of currency  
mgnAft | Object | The margin related information after switching account mode  
Applicable when sCode is `0/4`, return null for other scenarios  
> acctAvailEq | String | Account available equity in USD  
Applicable when acctLv is `3/4`, return "" for other scenarios  
> mgnRatio | String | Maintenance margin ratio in USD  
Applicable when acctLv is `3/4`, return "" for other scenarios  
> details | Array of objects | Detailed information  
Only applicable when acctLv is `2`, return "" for other scenarios  
>> ccy | String | Currency  
>> availEq | String | Available equity of currency  
>> mgnRatio | String | Maintenance margin ratio of currency  
  
### Set account mode

You need to set on the Web/App for the first set of every account mode. If users plan to switch account modes while holding positions, they should first call the preset endpoint to conduct necessary settings, then call the precheck endpoint to get unmatched information, margin check, and other related information, and finally call the account mode switch endpoint to switch account modes.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/account/set-account-level`

> Request Example
    
    
    POST /api/v5/account/set-account-level
    body
    {
        "acctLv":"1"
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
acctLv | String | Yes | Account mode  
`1`: Spot mode  
`2`: Futures mode   
`3`: Multi-currency margin code   
`4`: Portfolio margin mode  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "acctLv": "1"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
acctLv | String | Account mode  
  
### Set collateral assets

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/account/set-collateral-assets`

> Request Example
    
    
    # Set all assets to be collateral
    POST /api/v5/account/set-collateral-assets
    body
    {
        "type":"all",
        "collateralEnabled":true
    }
    
    
    # Set custom assets to be non-collateral
    POST /api/v5/account/set-collateral-assets
    body
    {
        "type":"custom",
        "ccyList":["BTC","ETH"],
        "collateralEnabled":false
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
type | String | true | Type  
`all`  
`custom`  
collateralEnabled | Boolean | true | Whether or not set the assets to be collateral  
`true`: Set to be collateral  
`false`: Set to be non-collateral  
ccyList | Array of strings | conditional | Currency list, e.g. ["BTC","ETH"]  
If type=`custom`, the parameter is required.  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data" :[
          {
            "type":"all",
            "ccyList":["BTC","ETH"],
            "collateralEnabled":false
          }
        ]  
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
type | String | Type  
`all`  
`custom`  
collateralEnabled | Boolean | Whether or not set the assets to be collateral  
`true`: Set to be collateral  
`false`: Set to be non-collateral  
ccyList | Array of strings | Currency list, e.g. ["BTC","ETH"]  
  
### Get collateral assets

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/account/collateral-assets`

> Request Example
    
    
    GET /api/v5/account/collateral-assets
    

#### Request Parameters

**Parameters** | **Types** | **Required** | **Description**  
---|---|---|---  
ccy | String | No | Single currency or multiple currencies (no more than 20) separated with comma, e.g. "BTC" or "BTC,ETH".  
collateralEnabled | Boolean | No | Whether or not to be a collateral asset  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data" :[
              {
                "ccy":"BTC",
                "collateralEnabled": true
              },
              {
                "ccy":"ETH",
                "collateralEnabled": false
              }
        ]  
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
ccy | String | Currency, e.g. `BTC`  
collateralEnabled | Boolean | Whether or not to be a collateral asset  
  
### Reset MMP Status

You can unfreeze by this endpoint once MMP is triggered.  

Only applicable to Option in Portfolio Margin mode, and MMP privilege is required.

In the demo trading environment, MMP configurations may be periodically reset by the system. If your MMP status is unexpectedly reset in demo trading, please contact your BD manager or reach out to institutional@okx.com. 

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/account/mmp-reset`

> Request Example
    
    
    POST /api/v5/account/mmp-reset
    body
    {
        "instType":"OPTION",
        "instFamily":"BTC-USD"
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | No | Instrument type  
`OPTION`  
The default is `OPTION  
instFamily | String | Yes | Instrument family  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "result":true
            }
        ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
result | Boolean | Result of the request `true`, `false`  
  
### Set MMP

This endpoint is used to set MMP configure  

Only applicable to Option in Portfolio Margin mode, and MMP privilege is required.

  
What is MMP?  
Market Maker Protection (MMP) is an automated mechanism for market makers to pull their quotes when their executions exceed a certain threshold(`qtyLimit`) within a certain time frame(`timeInterval`). Once mmp is triggered, any pre-existing mmp pending orders(`mmp` and `mmp_and_post_only` orders) will be automatically canceled, and new orders tagged as MMP will be rejected for a specific duration(`frozenInterval`), or until manual reset by makers.  
  
How to enable MMP?  
Please send an email to institutional@okx.com or contact your business development (BD) manager to apply for MMP. The initial threshold will be upon your request.  MMP is configured individually per instrument family (`instFamily`). Enabling MMP for one instrument family does **not** automatically extend to others. For example, setting up MMP for `BTC-USD` does not cover `ETH-USD` or `SOL-USD` — each must be configured separately via this endpoint. 

#### Rate Limit: 2 requests per 10 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/account/mmp-config`

> Request Example
    
    
    POST /api/v5/account/mmp-config
    body
    {
        "instFamily":"BTC-USD",
        "timeInterval":"5000",
        "frozenInterval":"2000",
        "qtyLimit": "100"
    }
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instFamily | String | Yes | Instrument family  
timeInterval | String | Yes | Time window (ms). MMP interval where monitoring is done  
"0" means disable MMP  
frozenInterval | String | Yes | Frozen period (ms).   
"0" means the trade will remain frozen until you request "Reset MMP Status" to unfrozen  
qtyLimit | String | Yes | Trade qty limit in number of contracts  
Must be > 0  
  
> Response Example
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
        {
            "frozenInterval":"2000",
            "instFamily":"BTC-USD",
            "qtyLimit": "100",
            "timeInterval":"5000"
        }
      ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
instFamily | String | Instrument family  
timeInterval | String | Time window (ms). MMP interval where monitoring is done  
frozenInterval | String | Frozen period (ms).  
qtyLimit | String | Trade qty limit in number of contracts  
  
### GET MMP Config

This endpoint is used to get MMP configure information  

Only applicable to Option in Portfolio Margin mode, and MMP privilege is required.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/account/mmp-config`

> Request Example
    
    
    GET /api/v5/account/mmp-config?instFamily=BTC-USD
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instFamily | String | No | Instrument Family  
  
> Response Example
    
    
    {
      "code": "0",
      "data": [
        {
          "frozenInterval": "2000",
          "instFamily": "ETH-USD",
          "mmpFrozen": true,
          "mmpFrozenUntil": "1000",
          "qtyLimit": "10",
          "timeInterval": "5000"
        }
      ],
      "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instFamily | String | Instrument Family  
mmpFrozen | Boolean | Whether MMP is currently triggered. `true` or `false`  
mmpFrozenUntil | String | If frozenInterval is configured and mmpFrozen = True, it is the time interval (in ms) when MMP is no longer triggered, otherwise "".  
timeInterval | String | Time window (ms). MMP interval where monitoring is done  
frozenInterval | String | Frozen period (ms). If it is "0", the trade will remain frozen until manually reset and `mmpFrozenUntil` will be "".  
qtyLimit | String | Trade qty limit in number of contracts  
  
### Move positions

Only applicable to users with a trading level greater than or equal to VIP6, and can only be called through the API Key of the master account. Users can check their trading level through the fee details table on the [My trading fees](https://www.okx.com/balance/fee) page.  

To move positions between different accounts under the same master account. Each source account can trigger up to fifteen move position requests every 24 hours. There is no limitation to the destination account to receive positions. Refer to the "Things to note" part for more details.

#### Rate limit: 1 request per second

#### Rate limit rule: Master account User ID

#### HTTP Request

`POST /api/v5/account/move-positions`

> Request example
    
    
    {
       "fromAcct":"0",
       "toAcct":"test",
       "legs":[
          {
             "from":{
                "posId":"2065471111340792832",
                "side":"sell",
                "sz":"1"
             },
             "to":{
                "posSide":"net",
                "tdMode":"cross"
             }
          },
          {
             "from":{
                "posId":"2063111180412153856",
                "side":"sell",
                "sz":"1"
             },
             "to":{
                "posSide":"net",
                "tdMode":"cross"
             }
          }
       ],
       "clientId":"test"
    }
    

#### Request parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
fromAcct | String | Yes | Source account name. If it's a master account, it should be "0"  
toAcct | String | Yes | Destination account name. If it's a master account, it should be "0"  
legs | Array of Objects | Yes | An array of objects containing details of each position to be moved  
> from | Object | yes | Details of the position in the source account  
>> posId | String | Yes | Position ID in the source account  
>> sz | String | Yes | Number of contracts.  
>> side | String | Yes | Trade side from the perspective of source account  
`buy`  
`sell`  
> to | Object | Yes | Details of the configuration of the destination account  
>> tdMode | String | No | Trading mode in the destination account.  
`cross`  
`isolated`  
If not provided, tdMode will take the default values as shown below:  
Buy options in `Futures mode`/`Multi-currency margin mode`: `isolated`  
Other cases: `cross`  
>> posSide | String | No | Position side  
`net`  
`long`  
`short`  
This parameter is not mandatory if the destination sub-account is in **net** mode. If you pass it through, the only valid value is `net`.It can only be `long` or `short` if the destination sub-account is in long/short mode. If not specified, destination account in long/short mode always open new positions.  
>> ccy | String | No | Margin currency in destination accountOnly applicable to cross margin positions in `Futures mode`.  
clientId | String | Yes | Client-supplied ID. A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
  
> Response example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "clientId": "test",
                "blockTdId": "2065832911119076864",
                "state": "filled",
                "ts": "1734069018526",
                "fromAcct": "0",
                "toAcct": "test",
                "legs": [
                    {
                        "from": {
                            "posId": "2065471111340792832",
                            "instId": "BTC-USD-SWAP",
                            "px": "100042.7",
                            "side": "sell",
                            "sz": "1",
                            "sCode": "0",
                            "sMsg": ""
                        },
                        "to": {
                            "instId": "BTC-USD-SWAP",
                            "px": "100042.7",
                            "side": "buy",
                            "sz": "1",
                            "tdMode": "cross",
                            "posSide": "net",
                            "ccy": "",
                            "sCode": "0",
                            "sMsg": ""
                        }
                    },
                    {
                        "from": {
                            "posId": "2063111180412153856",
                            "instId": "BTC-USDT-SWAP",
                            "px": "100008.1",
                            "side": "sell",
                            "sz": "1",
                            "sCode": "0",
                            "sMsg": ""
                        },
                        "to": {
                            "instId": "BTC-USDT-SWAP",
                            "px": "100008.1",
                            "side": "buy",
                            "sz": "1",
                            "tdMode": "cross",
                            "posSide": "net",
                            "ccy": "",
                            "sCode": "0",
                            "sMsg": ""
                        }
                    }
                ]
            }
        ]
    }
    
    

> Response example:failure
    
    
    // The destination account position mode (net/longShort) is not matched with the posSide field
    {
        "code": "51000",
        "msg": "Incorrect type of posSide (leg with Instrument Id [BTC-USD-SWAP])",
        "data": []
    }
    
    // The BTC amount in the destination account is not enough to open the position.
    {
        "code": "51008",
        "msg": "Order failed. Insufficient BTC margin in account",
        "data": []
    }
    
    // TradeFi positions are not supported.
    {
        "code": "70004",
        "msg": "Invalid instrument ID XAG-USDT-SWAP",
        "data": []
    }
    
    

#### Response parameters

**Parameter** | **Type** | **Description**  
---|---|---  
code | String | The result code, `0` means success  
msg | String | The error message, empty if the code is 0  
blockTdId | String | Block trade ID  
clientId | String | Client-supplied ID  
state | String | Status of the order `filled`, `failed`  
fromAcct | String | Source account name  
toAcct | String | Destination account name  
legs | Array | An array of objects containing details of each position to be moved  
> from | Object | Object describing the "from" leg  
>> instId | String | Instrument ID  
>> posId | String | Position ID  
>> px | String | Transfer price, typically a 60-minute TWAP of the mark price  
>> side | String | Direction of the leg in the source account  
`buy`  
`sell`  
>> sz | String | Number of Contracts  
>> sCode | String | The code of the event execution result, 0 means success  
>> sMsg | String | Rejection message if the request is unsuccessful  
> to | Object | Object describing the "to" leg  
>> instId | String | Instrument ID  
>> side | String | Trade side of the trade in the destination account  
>> posSide | String | Position side of the trade in the destination account  
>> tdMode | String | Trade mode  
>> px | String | Transfer price, typically a 60-minute TWAP of the mark price  
>> ccy | String | Margin currency  
>> sCode | String | The code of the event execution result, 0 means success  
>> sMsg | String | Rejection message if the request is unsuccessful  
ts | String | Unix timestamp in milliseconds indicating when the transfer request was processed  
  
#### Things to note

  1. Only applicable to users with a trading level greater than or equal to VIP6, and can only be called through the API Key of the master account.
  2. The source and destination accounts for move positions must be accounts under the same master account and they must be different.
  3. For source account, a maximum of fifteen move position requests can be triggered within a 24-hour period. There is no limitation to the destination account to receive positions. Only successful requests are counted toward this limit.
  4. The maximum number of legs per move position request is 30.
  5. No move position fee will be charged at this time.
  6. Moving positions is not supported in margin trading now.
  7. TradeFi positions are not supported.
  8. The move position price is determined by the TWAP (Time-Weighted Average Price) of the mark price over the past 60 minutes, using the closing mark price per minute. If the symbol is newly listed and a 60-minute TWAP is unavailable, the move position will be rejected with error code 70065
  9. The move position will share the same price limit as those in the order book. The move position will fail if the 60-minute mark price TWAP is outside of the price limit.
  10. For the source account, move positions must be conducted in a reduce-only manner. You must choose the opposite side of your current position and specify a size equal to or smaller than your existing position size. The system will also process move position requests in a best-effort reduce-only manner.
  11. The side field of source account leg (from) should be `sell` if you are holding a long position while the side of destination account leg (to) should be `buy`, vice versa for a short position.
  12. The posSide field of destination account (to) should be `net` if it's in one-way mode; `long`/`short` if it's in hedge mode. If in hedge mode, you need to specify `long`/`short` to decide whether to close current positions or open reverse positions. Otherwise, it will always open new positions. 
     1. Open long: buy and open long (side: buy; posSide: long)
     2. Open short: sell and open short (side: sell; posSide: short)
     3. Close long: sell and close long (side: sell; posSide: long)
     4. Close short: buy and close short (side: buy; posSide: short)
  13. Historical records of move positions can be fetched from the _Get move positions history_ endpoint but only for pending or successful requests.
  14. Move positions operation counting example.

Transfer done within the day | Account A count (total) | Account B count (total) | Account C count (total) | Account D count (total)  
---|---|---|---|---  
Account A to Account B | 1 | 0 | 0 | 0  
Account B to Account C | 1 | 1 | 0 | 0  
Account B to Account D | 1 | 2 | 0 | 0  
  
### Get move positions history

Only applicable to users with a trading level greater than or equal to VIP6, and can only be called through the API Key of the master account. Users can check their trading level through the fee details table on the [My trading fees](https://www.okx.com/balance/fee) page.  

Retrieve move position details in the last 3 days.

#### Rate limit: 2 requests per 2 seconds

#### Rate limit rule: Master account UserID

#### HTTP Request

`GET /api/v5/account/move-positions-history`

> Request example
    
    
    Get /api/v5/account/move-positions-history
    
    

#### Request parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
blockTdId | String | No | BlockTdId generated by the system  
clientId | String | No | Client-supplied ID. A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
beginTs | String | No | Filter with a begin timestamp. Unix timestamp format in milliseconds (inclusive)  
endTs | String | No | Filter with an end timestamp. Unix timestamp format in milliseconds (inclusive)  
limit | String | No | Number of results per request. The maximum and default are both `100`  
state | String | No | Positions transfer state, `filled` `pending`  
  
> Response example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "clientId": "test",
                "blockTdId": "2066393411110139648",
                "state": "filled",
                "ts": "1734085725000",
                "fromAcct": "0",
                "toAcct": "test",
                "legs": [
                    {
                        "from": {
                            "posId": "2065477911110792832",
                            "instId": "BTC-USD-SWAP",
                            "px": "100123.8",
                            "side": "sell",
                            "sz": "1"
                        },
                        "to": {
                            "instId": "BTC-USD-SWAP",
                            "px": "100123.8",
                            "side": "buy",
                            "sz": "1",
                            "tdMode": "cross",
                            "posSide": "net",
                            "ccy": ""
                        }
                    },
                    {
                        "from": {
                            "posId": "2063533111112153856",
                            "instId": "BTC-USDT-SWAP",
                            "px": "100078.7",
                            "side": "sell",
                            "sz": "1"
                        },
                        "to": {
                            "instId": "BTC-USDT-SWAP",
                            "px": "100078.7",
                            "side": "buy",
                            "sz": "1",
                            "tdMode": "cross",
                            "posSide": "net",
                            "ccy": ""
                        }
                    }
                ]
            }
       ]
    }
    
    

#### Response parameters

**Parameter** | **Type** | **Description**  
---|---|---  
clientId | String | Client-supplied ID. A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
blockTdId | String | Block trade ID.  
state | String | Position transfer state, `filled` `pending`  
ts | String | Unix timestamp in milliseconds indicating when the transfer request was processed  
fromAcct | String | Source account name  
toAcct | String | Destination account name  
legs | Array | An array of objects containing details of each position to be moved  
> from | Object | Object describing the "from" leg  
>> instId | String | Instrument ID  
>> posId | String | Position ID  
>> px | String | Transfer price, typically a 60-minute TWAP of the mark price  
>> side | String | Direction of the leg in the source account  
`buy`  
`sell`  
>> sz | String | Number of Contracts  
> to | Object | Object describing the "to" leg  
>> instId | String | Instrument ID  
>> px | String | Transfer price, typically a 60-minute TWAP of the mark price  
>> side | String | Trade side from the perspective of destination account  
`buy`  
`sell`  
>> sz | String | Number of contracts.  
>> tdMode | String | Trading mode in the destination account  
`cross`  
`isolated`  
>> posSide | String | Position side  
`net`  
`long`  
`short`  
>> ccy | String | Margin currency in destination account  
Only applicable to cross margin positions in `Futures mode`.  
  
### Set auto earn

Turn on/off auto earn.

#### Rate limit: 2 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/account/set-auto-earn`

> Request example
    
    
    // turn on auto lend
    {
       "earnType": "0",
       "ccy":"BTC",
       "action":"turn_on"
    }
    
    

#### Request parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
earnType | String | No | Auto earn type  
`0`: auto earn (auto lend, auto staking)   
`1`: auto earn (USDG earn)  
The default value is `0`  
ccy | String | Yes | Currency  
action | String | Yes | Auto earn operation action  
`turn_on`: turn on auto earn  
`turn_off`: turn off auto earn  
~~`amend`: amend minimum lending APR, applicable only to earnType `0`~~ (Deprecated)  
apr | String | Optional | ~~Minimum lending APR. Users must pass in this field when earnType is`0` and action is `turn_on/amend`.  
0.01 means 1%, available range 0.01-3.65, increment 0.01~~ (Deprecated)  
  
> Response example
    
    
    {
       "code":"0",
       "msg":"",
       "data":[
          {
             "earnType": "0",
             "ccy":"BTC",
             "action":"turn_on",
             "apr":"0.01"
          }
       ]
    }
    
    

#### Response parameters

**Parameter** | **Type** | **Description**  
---|---|---  
earnType | String | Auto earn type  
`0`: auto earn (auto lend, auto staking)   
`1`: auto earn (USDG earn)  
ccy | String | Currency  
action | String | Auto earn operation action  
`turn_on`  
`turn_off`  
~~`amend`~~ (Deprecated)  
apr | String | ~~Minimum lending APR~~ (Deprecated)  
  
### Set settle currency

Only applicable to USD-margined contract.

#### Rate limit: 20 times per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/account/set-settle-currency`

> Request Example
    
    
    POST /api/v5/account/set-settle-currency
    body
    {
        "settleCcy": "USDC"
    }
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
settleCcy | String | Yes | USD-margined contract settle currency  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data" :[
              {
                "settleCcy":"USDC"
              }
        ]  
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
settleCcy | String | USD-margined contract settle currency  
  
### Set trading config

#### Rate limit: 1 request per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/account/set-trading-config`

> Request example
    
    
    POST /api/v5/account/set-trading-config
    body
    {
        "type": "stgyType",
        "stgyType":"1"
    }
    
    

#### Request parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
type | String | Yes | Trading config type  
`stgyType`  
stgyType | String | No | Strategy type  
`0`: general strategy  
`1`: delta neutral strategy  
Only applicable when type is `stgyType`  
  
> Response example
    
    
    {
       "code":"0",
       "msg":"",
       "data":[
          {
                "type": "stgyType",
                "stgyType":"1"
          }
       ]
    }
    
    

#### Response parameters

**Parameter** | **Type** | **Description**  
---|---|---  
type | String | Trading config type  
stgyType | String | Strategy type  
  
### Precheck set delta neutral

#### Rate limit: 1 request per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/account/precheck-set-delta-neutral`

> Request example
    
    
    GET /api/v5/account/precheck-set-delta-neutral?stgyType=1
    
    

#### Request parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
stgyType | String | Yes | Strategy type  
`0`: general strategy  
`1`: delta neutral strategy  
  
> Response example
    
    
    {
        "code": "0",
        "data": [
            {
                "unmatchedInfoCheck": [
                    {
                        "posList": [],
                        "ordList": [],
                        "deltaLever": "",
                        "type": "spot_mode"
                    },
                   {
                        "posList": ["123","123","123"],
                        "ordList": [],
                        "deltaLever": "",
                        "type": "isolated_margin"
                    }
                ]
            }
        ],
        "msg": ""
    }
    
    

#### Response parameters

**Parameter** | **Type** | **Description**  
---|---|---  
unmatchedInfoCheck | Array of objects | Unmatched information list  
> type | String | Unmatched information type  
`spot_mode`: DNA is not supported under spot mode  
`futures_mode`: DNA is not supported under futures mode  
`isolated_margin`: Isolated margin position is not supported in DNA  
`isolated_contract`: Isolated contract position is not supported in DNA  
`positions_options`: Options are not supported in DNA  
`isolated_pending_orders`: Isolated pending orders are not supported in DNA  
`pending_orders_options`: Pending options orders are not supported in DNA  
`trading_bot`: Trading bot is not supported in DNA  
`repay_borrowings`: borrowing in the targeted strategy will exceed the main account borrowing limit after the switch. Repay liabilities and try again.  
`loan`: Flexible loan and DNA cannot be used at the same time   
`delta_risk`: delta risk check failed, lower delta and try again  
`collateral_all`: all coins must be set as collateral in DNA  
`risk_unit_type`: The account is part of a delta neutral risk unit and cannot be switched to general mode. Remove it from the risk unit before switching strategies.  
> deltaLever | String | Delta leverage  
Applicable when type is `delta_risk`  
> ordList | Array of strings | Unmatched order list, order ID  
Applicable when type is `isolated_pending_orders`/`pending_orders_options`  
> posList | Array of strings | Unmatched position list, position ID  
Applicable when type is `isolated_margin`/`isolated_contract`/`positions_options`  
  
### Adjust demo account balance

**This endpoint is only applicable to the demo trading environment.**

Allows users to increase or reduce balances for specific currencies (BTC, ETH, USDT, OKB) in a demo account, enabling flexible testing of trading strategies under different capital scenarios.

All-or-nothing: if any currency in the request fails validation, the entire request is rejected and no balances are modified.

#### Rate Limit: Increase — 3 requests per user per day (resets at UTC 0:00). Reduce — no limit.

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/account/demo-adjust-balance`

> Request Example
    
    
    POST /api/v5/account/demo-adjust-balance
    body
    {
        "type": "increase",
        "adjustments": [
            { "ccy": "BTC", "amt": "0.5" },
            { "ccy": "USDT", "amt": "3000" }
        ]
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
type | String | Yes | Direction of adjustment.  
`increase`: add to balance  
`reduce`: deduct from balance  
One direction per request; increase and reduce cannot be mixed.  
adjustments | Array | Yes | List of currency adjustments. At least one item required. Duplicate currencies are not allowed.  
> ccy | String | Yes | Currency. Supported values: `BTC` `ETH` `USDT` `OKB`  
> amt | String | Yes | Adjustment amount. Must be non-negative. Decimal places must not exceed the precision defined for the currency.  
Increase limits per request: BTC: 1, ETH: 1, USDT: 5000, OKB: 100.  
Reduce has no per-request amount limit — only constrained by available balance ≥ 0.  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
            "remainCnt": "2",
            "totalCnt": "3",
            "details": [
                { "ccy": "BTC", "amt": "0.5", "bal": "1.5" },
                { "ccy": "USDT", "amt": "3000", "bal": "13000" }
            ]
        }]
    }
    

> Failure Example
    
    
    {
        "code": "59693",
        "msg": "USDT transferable balance insufficient. Some funds are occupied by open orders or positions. Please cancel orders or close positions and try again",
        "data": []
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
remainCnt | String | Remaining daily increase quota. Also returned for reduce requests, but reduce does not consume quota.  
totalCnt | String | Total daily increase quota (default: 3).  
details | Array | Per-currency operation details.  
> ccy | String | Currency.  
> amt | String | Adjustment amount applied.  
> bal | String | Post-operation balance for this currency.  
  
## WebSocket

### Account channel

Retrieve account information. Data will be pushed when triggered by events such as placing order, canceling order, transaction execution, etc. It will also be pushed in regular interval according to subscription granularity.  

Concurrent connection to this channel will be restricted by the following rules: [WebSocket connection count limit](/docs-v5/en/#overview-websocket-connection-count-limit).

#### URL Path

/ws/v5/private (required login)

> Request Example : single
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "account",
          "ccy": "BTC"
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
            url = "wss://ws.okx.com:8443/ws/v5/private",
            useServerTime=False
        )
        await ws.start()
        args = [
            {
              "channel": "account",
              "ccy": "BTC"
            }
        ]
    
        await ws.subscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
        await ws.unsubscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
    
    asyncio.run(main())
    

> Request Example
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "account",
          "extraParams": "
            {
              \"updateInterval\": \"0\"
            }
          "
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
            url = "wss://ws.okx.com:8443/ws/v5/private",
            useServerTime=False
        )
        await ws.start()
        args = [
            {
              "channel": "account",
              "extraParams": "{\"updateInterval\": \"0\"}"
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
`account`  
> ccy | String | No | Currency  
> extraParams | String | No | Additional configuration  
>> updateInterval | int | No | `0`: only push due to account events   
The data will be pushed both by events and regularly if this field is omitted or set to other values than 0.   
The following format should be strictly obeyed when using this field.   
"extraParams": "  
{  
\"updateInterval\": \"0\"  
}  
"  
  
> Successful Response Example : single
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "account",
        "ccy": "BTC"
      },
      "connId": "a4d3ae55"
    }
    

> Successful Response Example
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "account"
      },
      "connId": "a4d3ae55"
    }
    

> Failure Response Example
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"account\", \"ccy\" : \"BTC\"}]}",
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
`account`  
> ccy | String | No | Currency  
code | String | No | Error code  
msg | String | No | Error message  
connId | String | Yes | WebSocket connection ID  
  
> Push Data Example
    
    
    {
        "arg": {
            "channel": "account",
            "uid": "44*********584"
        },
        "eventType": "snapshot",
        "curPage": 1,
        "lastPage": true,
        "data": [{
            "adjEq": "55444.12216906034",
        "availEq": "55444.12216906034",
            "borrowFroz": "0",
        "delta": "0",
        "deltaLever": "0",
        "deltaNeutralStatus": "0",
            "details": [{
            "availBal": "4734.371190691436",
            "availEq": "4734.371190691435",
            "borrowFroz": "0",
            "cashBal": "4750.426970691436",
            "ccy": "USDT",
            "coinUsdPrice": "0.99927",
            "crossLiab": "0",
            "colRes": "0",
            "collateralEnabled": false,
            "collateralRestrict": false, // Deprecated, use colRes instead
            "colBorrAutoConversion": "0",
            "disEq": "4889.379316336831",
            "eq": "4892.951170691435",
            "eqUsd": "4889.379316336831",
            "smtSyncEq": "0",
            "spotCopyTradingEq": "0",
            "fixedBal": "0",
            "frozenBal": "158.57998",
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
            "maxSpotInUseAmt": "",          
            "spotIsoBal": "0",
            "stgyEq": "150",
            "twap": "0",
            "uTime": "1705564213903",
            "upl": "-7.475800000000003",
            "uplLiab": "0",
            "spotBal": "",
            "openAvgPx": "",
            "accAvgPx": "",
            "spotUpl": "",
            "spotUplRatio": "",
            "totalPnl": "",
            "totalPnlRatio": ""
            }],
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
            "totalEq": "55868.06403501676",
            "uTime": "1705564223311",
            "upl": "0"
        }]
    }
    

#### Push data parameters

**Parameters** | **Types** | **Description**  
---|---|---  
arg | Object | Successfully subscribed channel  
> channel | String | Channel name  
> uid | String | User Identifier  
eventType | String | Event type:   
`snapshot`: Initial and regular snapshot push   
`event_update`: Event-driven update push  
curPage | Integer | Current page number.   
Only applicable for `snapshot` events. Not included in `event_update` events.  
lastPage | Boolean | Whether this is the last page of pagination:  
`true`  
`false`  
Only applicable for `snapshot` events. Not included in `event_update` events.  
data | Array of objects | Subscribed data  
> uTime | String | The latest time to get account information, millisecond format of Unix timestamp, e.g. `1597026383085`  
> totalEq | String | The total amount of equity in `USD`  
> isoEq | String | Isolated margin equity in `USD`  
Applicable to `Futures mode`/`Multi-currency margin`/`Portfolio margin`  
> adjEq | String | Adjusted / Effective equity in `USD`   
The net fiat value of the assets in the account that can provide margins for spot, expiry futures, perpetual futures and options under the cross-margin mode.   
In multi-ccy or PM mode, the asset and margin requirement will all be converted to USD value to process the order check or liquidation.   
Due to the volatility of each currency market, our platform calculates the actual USD value of each currency based on discount rates to balance market risks.   
Applicable to `Spot mode`/`Multi-currency margin`/`Portfolio margin`  
> availEq | String | Account level available equity, excluding currencies that are restricted due to the collateralized borrowing limit.  
Applicable to `Multi-currency margin`/`Portfolio margin`  
> ordFroz | String | Margin frozen for pending cross orders in `USD`   
Only applicable to `Spot mode`/`Multi-currency margin`/`Portfolio margin`  
> imr | String | Initial margin requirement in `USD`   
The sum of initial margins of all open positions and pending orders under cross-margin mode in `USD`.   
Applicable to `Spot mode`/`Multi-currency margin`/`Portfolio margin`  
> mmr | String | Maintenance margin requirement in `USD`   
The sum of maintenance margins of all open positions and pending orders under cross-margin mode in `USD`.   
Applicable to `Spot mode`/`Multi-currency margin`/`Portfolio margin`  
> borrowFroz | String | Potential borrowing IMR of the account in `USD`   
Only applicable to `Spot mode`/`Multi-currency margin`/`Portfolio margin`. It is "" for other margin modes.  
> mgnRatio | String | Maintenance margin ratio in `USD`.   
Applicable to `Spot mode`/`Multi-currency margin`/`Portfolio margin`  
> notionalUsd | String | Notional value of positions in `USD`   
Applicable to `Spot mode`/`Multi-currency margin`/`Portfolio margin`  
> notionalUsdForBorrow | String | Notional value for `Borrow` in USD  
Applicable to `Spot mode`/`Multi-currency margin`/`Portfolio margin`  
> notionalUsdForSwap | String | Notional value of positions for `Perpetual Futures` in USD  
Applicable to `Multi-currency margin`/`Portfolio margin`  
> notionalUsdForFutures | String | Notional value of positions for `Expiry Futures` in USD  
Applicable to `Multi-currency margin`/`Portfolio margin`  
> notionalUsdForOption | String | Notional value of positions for `Option` in USD  
Applicable to `Spot mode`/`Multi-currency margin`/`Portfolio margin`  
> upl | String | Cross-margin info of unrealized profit and loss at the account level in `USD`  
Applicable to `Multi-currency margin`/`Portfolio margin`  
> delta | String | Delta (USD)  
> deltaLever | String | Delta neutral strategy account level delta leverage  
deltaLever = delta / totalEq  
> deltaNeutralStatus | String | Delta risk status  
`0`: normal  
`1`: transfer restricted  
`2`: delta reducing - cancel all pending orders if delta is greater than 5000 USD, only one delta reducing order allowed per index (spot, futures, swap)  
> details | Array of objects | Detailed asset information in all currencies  
>> ccy | String | Currency  
>> eq | String | Equity of currency  
>> cashBal | String | Cash balance  
>> uTime | String | Update time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
>> isoEq | String | Isolated margin equity of currency  
Applicable to `Futures mode`/`Multi-currency margin`/`Portfolio margin`  
>> availEq | String | Available equity of currency  
Applicable to `Futures mode`/`Multi-currency margin`/`Portfolio margin`  
>> disEq | String | Discount equity of currency in `USD`.  
Applicable to `Spot mode`(enabled spot borrow)/`Multi-currency margin`/`Portfolio margin`  
>> fixedBal | String | Frozen balance for `Dip Sniper` and `Peak Sniper`  
>> availBal | String | Available balance of currency  
>> frozenBal | String | Frozen balance of currency  
>> ordFrozen | String | Margin frozen for open orders   
Applicable to `Spot mode`/`Futures mode`/`Multi-currency margin`  
>> liab | String | Liabilities of currency  
It is a positive value, e.g. `21625.64`.   
Applicable to `Spot mode`/`Multi-currency margin`/`Portfolio margin`  
>> upl | String | The sum of the unrealized profit & loss of all margin and derivatives positions of currency.   
Applicable to `Futures mode`/`Multi-currency margin`/`Portfolio margin`  
>> uplLiab | String | Liabilities due to Unrealized loss of currency  
Applicable to `Multi-currency margin`/`Portfolio margin`  
>> crossLiab | String | Cross liabilities of currency  
Applicable to `Spot mode`/`Multi-currency margin`/`Portfolio margin`  
>> isoLiab | String | Isolated liabilities of currency  
Applicable to `Multi-currency margin`/`Portfolio margin`  
>> rewardBal | String | Trial fund balance  
>> mgnRatio | String | Cross maintenance margin ratio of currency   
The index for measuring the risk of a certain asset in the account.   
Applicable to `Futures mode` and when there is cross position  
>> imr | String | Cross initial margin requirement at the currency level  
Applicable to `Futures mode` and when there is cross position  
>> mmr | String | Cross maintenance margin requirement at the currency level  
Applicable to `Futures mode` and when there is cross position  
>> interest | String | Interest of currency  
It is a positive value, e.g."9.01". Applicable to `Spot mode`/`Multi-currency margin`/`Portfolio margin`  
>> twap | String | Risk indicator of forced repayment  
Divided into multiple levels from 0 to 5, the larger the number, the more likely the forced repayment will be triggered.   
Applicable to `Spot mode`/`Multi-currency margin`/`Portfolio margin`  
>> frpType | String | Forced repayment (FRP) type  
`0`: no FRP  
`1`: user based FRP  
`2`: platform based FRP  
  
Return `1`/`2` when twap is >= 1, applicable to `Spot mode`/`Multi-currency margin`/`Portfolio margin`  
>> maxLoan | String | Maximum borrowable amount for the currency under the current account conditions. Affects the amount available for margin borrowing and transfers.  
Applicable to `cross` of `Spot mode`/`Multi-currency margin`/`Portfolio margin`  
>> eqUsd | String | Equity `USD` of currency  
>> borrowFroz | String | Potential borrowing IMR of currency in `USD`   
Only applicable to `Spot mode`/`Multi-currency margin`/`Portfolio margin`. It is "" for other margin modes.  
>> notionalLever | String | Leverage of currency  
Applicable to `Futures mode`  
>> coinUsdPrice | String | Price index `USD` of currency  
>> stgyEq | String | Total equity allocated to trading bots for the currency. Covers Spot Grid, Futures Grid, Signal Bot, Futures Martingale, Spot Martingale, Infinite Grid, and Recurring Buy strategies.  
>> isoUpl | String | Isolated unrealized profit and loss of currency  
Applicable to `Futures mode`/`Multi-currency margin`/`Portfolio margin`  
>> spotInUseAmt | String | Actual spot hedging amount in use for the currency.  
Applicable to `Portfolio margin`  
>> clSpotInUseAmt | String | User-defined spot hedging amount for the currency.  
Applicable to `Portfolio margin`  
>> maxSpotInUseAmt | String | System-calculated maximum possible spot hedging amount for the currency.  
Applicable to `Portfolio margin`  
>> spotIsoBal | String | Balance acquired through spot copy trading (as a follower or lead trader), including amounts currently frozen by open orders. For example, if 1 BTC was purchased via copy trading and 0.4 BTC is frozen in an open sell order, `spotIsoBal` returns `1`, not `0.6`.  
Applicable to copy trading. Applicable to `Spot mode`/`Futures mode`.  
>> smtSyncEq | String | Smart sync equity  
The default is "0", only applicable to copy trader.  
>> spotCopyTradingEq | String | Spot smart sync equity.   
The default is "0", only applicable to copy trader.  
>> spotBal | String | Spot balance. The unit is currency, e.g. BTC. [More details](https://www.okx.com/help/i-introduction-of-spot)  
>> openAvgPx | String | Spot average cost price. The unit is USD. [More details](https://www.okx.com/help/i-introduction-of-spot)  
>> accAvgPx | String | Spot accumulated cost price. The unit is USD. [More details](https://www.okx.com/help/i-introduction-of-spot)  
>> spotUpl | String | Spot unrealized profit and loss. The unit is USD. [More details](https://www.okx.com/help/i-introduction-of-spot)  
>> spotUplRatio | String | Spot unrealized profit and loss ratio. [More details](https://www.okx.com/help/i-introduction-of-spot)  
>> totalPnl | String | Spot accumulated profit and loss. The unit is USD. [More details](https://www.okx.com/help/i-introduction-of-spot)  
>> totalPnlRatio | String | Spot accumulated profit and loss ratio. [More details](https://www.okx.com/help/i-introduction-of-spot)  
>> colRes | String | Platform level collateral restriction status  
`0`: The restriction is not enabled.  
`1`: The restriction is not enabled. But the crypto is close to the platform's collateral limit.  
`2`: The restriction is enabled. This crypto can't be used as margin for your new orders. This may result in failed orders. But it will still be included in the account's adjusted equity and doesn't impact margin ratio.  
Refer to [Introduction to the platform collateralized borrowing limit](https://www.okx.com/help/introduction-to-the-platforms-collateralized-borrowing-limit-mechanism) for more details.  
>> colBorrAutoConversion | String | Risk indicator of auto conversion. Divided into multiple levels from 1-5, the larger the number, the more likely the repayment will be triggered. The default will be 0, indicating there is no risk currently. 5 means this user is undergoing auto conversion now, 4 means this user will undergo auto conversion soon whereas 1/2/3 indicates there is a risk for auto conversion.  
Applicable to `Spot mode`/`Futures mode`/`Multi-currency margin`/`Portfolio margin`  
When the total liability for each crypto set as collateral exceeds a certain percentage of the platform's total limit, the auto-conversion mechanism may be triggered. This may result in the automatic sale of excess collateral crypto if you've set this crypto as collateral and have large borrowings. To lower this risk, consider reducing your use of the crypto as collateral or reducing your liabilities.  
Refer to [Introduction to the platform collateralized borrowing limit](https://www.okx.com/help/introduction-to-the-platforms-collateralized-borrowing-limit-mechanism) for more details.  
>> collateralRestrict | Boolean | ~~Platform level collateralized borrow restriction  
`true`  
`false`~~(deprecated, use colRes instead)  
>> collateralEnabled | Boolean | `true`: Collateral enabled  
`false`: Collateral disabled  
Applicable to `Multi-currency margin`  
>> autoLendStatus | String | Auto lend status  
`unsupported`: auto lend is not supported by this currency  
`off`: auto lend is supported but turned off  
`pending`: auto lend is turned on but pending matching  
`active`: auto lend is turned on and matched  
>> autoLendMtAmt | String | Auto lend currency matched amount  
Return "0" when autoLendStatus is `unsupported/off/pending`. Return matched amount when autoLendStatus is `active`  
"" will be returned for inapplicable fields under the current account level.    
\- The account data is sent on event basis and regular basis.   
\- The event push is not pushed in real-time. It is aggregated and pushed at a fixed time interval, around 50ms. For example, if multiple events occur within a fixed time interval, the system will aggregate them into a single message and push it at the end of the fixed time interval. If the data volume is too large, it may be split into multiple messages.   
\- The regular push sends updates regardless of whether there are activities in the trading account or not.    
\- Only currencies with non-zero balance will be pushed. Definition of non-zero balance: any value of eq, availEq, availBal parameters is not 0. If the data is too large to be sent in a single push message, it will be split into multiple messages.   
\- For example, when subscribing to account channel without specifying ccy and there are 5 currencies are with non-zero balance, all 5 currencies data will be pushed in initial snapshot and in regular update. Subsequently when there is change in balance or equity of an token, only the incremental data of that currency will be pushed triggered by this change. 

### Positions channel

Retrieve position information. Initial snapshot will be pushed according to subscription granularity. Data will be pushed when triggered by events such as placing/canceling order, and will also be pushed in regular interval according to subscription granularity.  

Concurrent connection to this channel will be restricted by the following rules: [WebSocket connection count limit](/docs-v5/en/#overview-websocket-connection-count-limit).

#### URL Path

/ws/v5/private (required login)

> Request Example : single
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "positions",
          "instType": "FUTURES",
          "instFamily": "BTC-USD"
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
            url = "wss://ws.okx.com:8443/ws/v5/private",
            useServerTime=False
        )
        await ws.start()
        args = [
            {
              "channel": "positions",
              "instType": "FUTURES",
              "instFamily": "BTC-USD"
            }
        ]
    
        await ws.subscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
        await ws.unsubscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
    
    asyncio.run(main())
    

> Request Example
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "positions",
          "instType": "ANY",
          "extraParams": "
            {
              \"updateInterval\": \"0\"
            }
          "
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
            url = "wss://ws.okx.com:8443/ws/v5/private",
            useServerTime=False
        )
        await ws.start()
        args = [
            {
                "channel": "positions",
                "instType": "ANY",
                "extraParams": "{\"updateInterval\": \"0\"}"
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
`positions`  
> instType | String | Yes | Instrument type  
`MARGIN`  
`SWAP`  
`FUTURES`  
`OPTION`   
`EVENTS`  
`ANY`  
> instFamily | String | No | Instrument family  
Applicable to `FUTURES`/`SWAP`/`OPTION`  
> instId | String | No | Instrument ID  
If instId and instFamily are both passed, instId will be used  
> extraParams | String | No | Additional configuration  
>> updateInterval | int | No | `0`: only push due to positions events   
`2000, 3000, 4000`: push by events and regularly according to the time interval setting (ms)   
  
The data will be pushed both by events and around per 5 seconds regularly if this field is omitted or set to other values than the valid values above.   
  
The following format should be strictly followed when using this field.   
"extraParams": "   
{   
\"updateInterval\": \"0\"   
}  
"  
  
> Successful Response Example : single
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "positions",
        "instType": "FUTURES",
        "instFamily": "BTC-USD"
      },
      "connId": "a4d3ae55"
    }
    

> Successful Response Example
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "positions",
        "instType": "ANY"
      },
      "connId": "a4d3ae55"
    }
    

> Failure Response Example
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"positions\", \"instType\" : \"FUTURES\"}]}",
      "connId": "a4d3ae55"
    }
    

#### Response parameters

Parameter | Type | Required | Description  
---|---|---|---  
id | String | No | Unique identifier of the message  
event | String | Yes | Event  
`subscribe`  
`unsubscribe`  
`error`  
arg | Object | No | Subscribed channel  
> channel | String | Yes | Channel name  
> instType | String | Yes | Instrument type  
`MARGIN`  
`FUTURES`  
`SWAP`  
`OPTION`  
`EVENTS`  
`ANY`  
> instFamily | String | No | Instrument family  
> instId | String | No | Instrument ID  
code | String | No | Error code  
msg | String | No | Error message  
connId | String | Yes | WebSocket connection ID  
  
> Push Data Example: single
    
    
    {
      "arg":{
          "channel":"positions",
          "uid": "77982378738415879",
          "instType":"FUTURES"
      },
      "eventType": "snapshot",
      "curPage": 1,
      "lastPage": true,
      "data":[
        {
          "adl":"1",
          "availPos":"1",
          "avgPx":"2566.31",
          "cTime":"1619507758793",
          "ccy":"ETH",
          "deltaBS":"",
          "deltaPA":"",
          "gammaBS":"",
          "gammaPA":"",
          "hedgedPos":"",
          "imr":"",
          "instId":"ETH-USD-210430",
          "instType":"FUTURES",
          "interest":"0",
          "idxPx":"2566.13",
          "last":"2566.22",
          "lever":"10",
          "liab":"",
          "liabCcy":"",
          "liqPx":"2352.8496681818233",
          "markPx":"2353.849",
          "margin":"0.0003896645377994",
          "mgnMode":"isolated",
          "mgnRatio":"11.731726509588816",
          "mmr":"0.0000311811092368",
          "notionalUsd":"2276.2546609009605",
          "optVal":"",
          "pTime":"1619507761462",
          "pendingCloseOrdLiabVal":"0.1",
          "pos":"1",
          "baseBorrowed": "",
          "baseInterest": "",
          "quoteBorrowed": "",
          "quoteInterest": "",
          "posCcy":"",
          "posId":"307173036051017730",
          "posSide":"long",
          "spotInUseAmt": "",
          "clSpotInUseAmt": "",
          "maxSpotInUseAmt": "",
          "bizRefId": "",
          "bizRefType": "",
          "spotInUseCcy": "",
          "thetaBS":"",
          "thetaPA":"",
          "tradeId":"109844",
          "uTime":"1619507761462",
          "upl":"-0.0000009932766034",
          "uplLastPx":"-0.0000009932766034",
          "uplRatio":"-0.0025490556801078",
          "uplRatioLastPx":"-0.0025490556801078",
          "vegaBS":"",
          "vegaPA":"",
          "realizedPnl":"0.001",
          "pnl":"0.0011",
          "fee":"-0.0001",
          "fundingFee":"0",
          "liqPenalty":"0",
          "nonSettleAvgPx":"", 
          "settledPnl":"",
          "closeOrderAlgo":[
              {
                  "algoId":"123",
                  "slTriggerPx":"123",
                  "slTriggerPxType":"mark",
                  "tpTriggerPx":"123",
                  "tpTriggerPxType":"mark",
                  "closeFraction":"0.6"
              },
              {
                  "algoId":"123",
                  "slTriggerPx":"123",
                  "slTriggerPxType":"mark",
                  "tpTriggerPx":"123",
                  "tpTriggerPxType":"mark",
                  "closeFraction":"0.4"
              }
          ]
        }
      ]
    }
    

> Push Data Example
    
    
    {
      "arg":{
          "channel":"positions",
          "uid": "77982378738415879",
          "instType":"ANY"
      },
      "eventType": "snapshot",
      "curPage": 1,
      "lastPage": true,
      "data":[
        {
          "adl":"1",
          "availPos":"1",
          "avgPx":"2566.31",
          "cTime":"1619507758793",
          "ccy":"ETH",
          "deltaBS":"",
          "deltaPA":"",
          "gammaBS":"",
          "gammaPA":"",
          "hedgedPos":"",
          "imr":"",
          "instId":"ETH-USD-210430",
          "instType":"FUTURES",
          "interest":"0",
          "idxPx":"2566.13",
          "last":"2566.22",
          "usdPx":"",
          "bePx":"2353.949",
          "lever":"10",
          "liab":"",
          "liabCcy":"",
          "liqPx":"2352.8496681818233",
          "markPx":"2353.849",
          "margin":"0.0003896645377994",
          "mgnMode":"isolated",
          "mgnRatio":"11.731726509588816",
          "mmr":"0.0000311811092368",
          "notionalUsd":"2276.2546609009605",
          "optVal":"",
          "pTime":"1619507761462",
          "pendingCloseOrdLiabVal":"0.1",
          "pos":"1",
          "baseBorrowed": "",
          "baseInterest": "",
          "quoteBorrowed": "",
          "quoteInterest": "",
          "posCcy":"",
          "posId":"307173036051017730",
          "posSide":"long",
          "spotInUseAmt": "",
          "clSpotInUseAmt": "",
          "maxSpotInUseAmt": "",
          "spotInUseCcy": "",
          "bizRefId": "",
          "bizRefType": "",
          "thetaBS":"",
          "thetaPA":"",
          "tradeId":"109844",
          "uTime":"1619507761462",
          "upl":"-0.0000009932766034",
          "uplLastPx":"-0.0000009932766034",
          "uplRatio":"-0.0025490556801078",
          "uplRatioLastPx":"-0.0025490556801078",
          "vegaBS":"",
          "vegaPA":"",
          "realizedPnl":"0.001",
          "pnl":"0.0011",
          "fee":"-0.0001",
          "fundingFee":"0",
          "liqPenalty":"0",
          "nonSettleAvgPx":"", 
          "settledPnl":"",
          "closeOrderAlgo":[
              {
                  "algoId":"123",
                  "slTriggerPx":"123",
                  "slTriggerPxType":"mark",
                  "tpTriggerPx":"123",
                  "tpTriggerPxType":"mark",
                  "closeFraction":"0.6"
              },
              {
                  "algoId":"123",
                  "slTriggerPx":"123",
                  "slTriggerPxType":"mark",
                  "tpTriggerPx":"123",
                  "tpTriggerPxType":"mark",
                  "closeFraction":"0.4"
              }
          ]
        }, {
          "adl":"1",
          "availPos":"1",
          "avgPx":"2566.31",
          "cTime":"1619507758793",
          "ccy":"ETH",
          "deltaBS":"",
          "deltaPA":"",
          "gammaBS":"",
          "gammaPA":"",
          "hedgedPos":"",
          "imr":"",
          "instId":"ETH-USD-SWAP",
          "instType":"SWAP",
          "interest":"0",
          "idxPx":"2566.13",
          "last":"2566.22",
          "usdPx":"",
          "bePx":"2353.949",
          "lever":"10",
          "liab":"",
          "liabCcy":"",
          "liqPx":"2352.8496681818233",
          "markPx":"2353.849",
          "margin":"0.0003896645377994",
          "mgnMode":"isolated",
          "mgnRatio":"11.731726509588816",
          "mmr":"0.0000311811092368",
          "notionalUsd":"2276.2546609009605",
          "optVal":"",
          "pTime":"1619507761462",
          "pendingCloseOrdLiabVal":"0.1",
          "pos":"1",
          "baseBorrowed": "",
          "baseInterest": "",
          "quoteBorrowed": "",
          "quoteInterest": "",
          "posCcy":"",
          "posId":"307173036051017730",
          "posSide":"long",
          "spotInUseAmt": "",
          "clSpotInUseAmt": "",
          "maxSpotInUseAmt": "",
          "spotInUseCcy": "",
          "bizRefId": "",
          "bizRefType": "",
          "thetaBS":"",
          "thetaPA":"",
          "tradeId":"109844",
          "uTime":"1619507761462",
          "upl":"-0.0000009932766034",
          "uplLastPx":"-0.0000009932766034",
          "uplRatio":"-0.0025490556801078",
          "uplRatioLastPx":"-0.0025490556801078",
          "vegaBS":"",
          "vegaPA":"",
          "realizedPnl":"0.001",
          "pnl":"0.0011",
          "fee":"-0.0001",
          "fundingFee":"0",
          "liqPenalty":"0",
          "nonSettleAvgPx":"", 
          "settledPnl":"",
          "closeOrderAlgo":[
              {
                  "algoId":"123",
                  "slTriggerPx":"123",
                  "slTriggerPxType":"mark",
                  "tpTriggerPx":"123",
                  "tpTriggerPxType":"mark",
                  "closeFraction":"0.6"
              },
              {
                  "algoId":"123",
                  "slTriggerPx":"123",
                  "slTriggerPxType":"mark",
                  "tpTriggerPx":"123",
                  "tpTriggerPxType":"mark",
                  "closeFraction":"0.4"
              }
          ]
        }
      ]
    }
    

#### Push data parameters

Parameter | Type | Description  
---|---|---  
arg | Object | Successfully subscribed channel  
> channel | String | Channel name  
> uid | String | User Identifier  
> instType | String | Instrument type  
`MARGIN`  
`SWAP`  
`FUTURES`  
`OPTION`  
`EVENTS`  
> instFamily | String | Instrument family  
> instId | String | Instrument ID  
eventType | String | Event type:   
`snapshot`: Initial and regular snapshot push   
`event_update`: Event-driven update push  
curPage | Integer | Current page number.   
Only applicable for `snapshot` events. Not included in `event_update` events.  
lastPage | Boolean | Whether this is the last page of pagination:  
`true`  
`false`  
Only applicable for `snapshot` events. Not included in `event_update` events.  
data | Array of objects | Subscribed data  
> instType | String | Instrument type  
`MARGIN`  
`SWAP`  
`FUTURES`  
`OPTION`  
`EVENTS`  
> mgnMode | String | Margin mode, `cross` `isolated`  
> posId | String | Position ID  
> posSide | String | Position side  
`long`   
`short`   
`net` (`FUTURES`/`SWAP`/`OPTION`: positive `pos` means long position and negative `pos` means short position. `MARGIN`: `posCcy` being base currency means long position, `posCcy` being quote currency means short position.)  
> pos | String | Quantity of positions. In the isolated margin mode, when doing manual transfers, a position with pos of `0` will be generated after the deposit is transferred  
> hedgedPos | String | Hedged position size  
Only return for accounts in delta neutral strategy, stgyType:1. Return "" for accounts in general strategy.  
> baseBal | String | ~~Base currency balance, only applicable to`MARGIN`（Quick Margin Mode）~~(Deprecated)  
> quoteBal | String | ~~Quote currency balance, only applicable to`MARGIN`（Quick Margin Mode）~~(Deprecated)  
> baseBorrowed | String | ~~Base currency amount already borrowed, only applicable to MARGIN(Quick Margin Mode）~~(Deprecated)  
> baseInterest | String | ~~Base Interest, undeducted interest that has been incurred, only applicable to MARGIN(Quick Margin Mode）~~(Deprecated)  
> quoteBorrowed | String | ~~Quote currency amount already borrowed, only applicable to MARGIN(Quick Margin Mode）~~(Deprecated)  
> quoteInterest | String | ~~Quote Interest, undeducted interest that has been incurred, only applicable to MARGIN(Quick Margin Mode）~~(Deprecated)  
> posCcy | String | Position currency, only applicable to `MARGIN` positions  
> availPos | String | Position that can be closed   
Only applicable to `MARGIN` and `OPTION`.   
For `Margin` position, the rest of sz will be `SPOT` trading after the liability is repaid while closing the position. Please get the available reduce-only amount from "Get maximum available tradable amount" if you want to reduce the amount of `SPOT` trading as much as possible.  
> avgPx | String | Average open price  
> upl | String | Unrealized profit and loss calculated by mark price.  
> uplRatio | String | Unrealized profit and loss ratio calculated by mark price.  
> uplLastPx | String | Unrealized profit and loss calculated by last price. Main usage is showing, actual value is upl.  
> uplRatioLastPx | String | Unrealized profit and loss ratio calculated by last price.  
> instId | String | Instrument ID, e.g. `BTC-USDT-SWAP`  
> lever | String | Leverage, not applicable to `OPTION` seller  
> liqPx | String | Estimated liquidation price   
Not applicable to `OPTION`  
> markPx | String | Latest Mark price  
> imr | String | Initial margin requirement, only applicable to `cross`  
> margin | String | Margin, can be added or reduced. Only applicable to `isolated` `Margin`.  
> mgnRatio | String | Maintenance margin ratio  
> mmr | String | Maintenance margin requirement  
> liab | String | Liabilities, only applicable to `MARGIN`.  
> liabCcy | String | Liabilities currency, only applicable to `MARGIN`.  
> interest | String | Interest accrued that has not been settled.  
> tradeId | String | Last trade ID  
> notionalUsd | String | Notional value of positions in `USD`  
> optVal | String | Option Value, only applicable to `OPTION`.  
> pendingCloseOrdLiabVal | String | The amount of close orders of isolated margin liability.  
> adl | String | Automatic-Deleveraging, signal area  
Divided into 6 levels, from 0 to 5, the smaller the number, the weaker the adl intensity.   
Only applicable to `FUTURES/SWAP/OPTION`  
> bizRefId | String | External business id, e.g. experience coupon id  
> bizRefType | String | External business type  
> ccy | String | Currency used for margin  
> last | String | Latest traded price  
> idxPx | String | Latest underlying index price  
> usdPx | String | Latest USD price of the `ccy` on the market, only applicable to `FUTURES`/`SWAP`/`OPTION`  
> bePx | String | Breakeven price  
> deltaBS | String | delta: Black-Scholes Greeks in dollars, only applicable to `OPTION`  
> deltaPA | String | delta: Greeks in coins, only applicable to `OPTION`  
> gammaBS | String | gamma: Black-Scholes Greeks in dollars, only applicable to `OPTION`  
> gammaPA | String | gamma: Greeks in coins, only applicable to `OPTION`  
> thetaBS | String | theta: Black-Scholes Greeks in dollars, only applicable to `OPTION`  
> thetaPA | String | theta: Greeks in coins, only applicable to `OPTION`  
> vegaBS | String | vega: Black-Scholes Greeks in dollars, only applicable to `OPTION`  
> vegaPA | String | vega: Greeks in coins, only applicable to `OPTION`  
> spotInUseAmt | String | Spot in use amount  
Applicable to `Portfolio margin`  
> spotInUseCcy | String | Spot in use unit, e.g. `BTC`  
Applicable to `Portfolio margin`  
> clSpotInUseAmt | String | User-defined spot risk offset amount  
Applicable to `Portfolio margin`  
> maxSpotInUseAmt | String | Max possible spot risk offset amount  
Applicable to `Portfolio margin`  
> realizedPnl | String | Realized profit and loss  
Only applicable to `FUTURES`/`SWAP`/`OPTION`  
realizedPnl=pnl+fee+fundingFee+liqPenalty+settledPnl  
> pnl | String | Accumulated pnl of closing order(s) (excluding the fee).  
> fee | String | Accumulated fee  
Negative number represents the user transaction fee charged by the platform.Positive number represents rebate.  
> fundingFee | String | Accumulated funding fee  
> liqPenalty | String | Accumulated liquidation penalty. It is negative when there is a value.  
> closeOrderAlgo | Array of objects | Close position algo orders attached to the position. This array will have values only after you request "Place algo order" with `closeFraction`=1.  
>> algoId | String | Algo ID  
>> slTriggerPx | String | Stop-loss trigger price.  
>> slTriggerPxType | String | Stop-loss trigger price type.   
`last`: last price  
`index`: index price  
`mark`: mark price  
>> tpTriggerPx | String | Take-profit trigger price.  
>> tpTriggerPxType | String | Take-profit trigger price type.   
`last`: last price  
`index`: index price  
`mark`: mark price  
>> closeFraction | String | Fraction of position to be closed when the algo order is triggered.  
> cTime | String | Creation time, Unix timestamp format in milliseconds, e.g. `1597026383085`.  
> uTime | String | Latest time position was adjusted, Unix timestamp format in milliseconds, e.g. `1597026383085`.  
> pTime | String | Push time of positions information, Unix timestamp format in milliseconds, e.g. `1597026383085`.  
> nonSettleAvgPx | String | Non-Settlement entry price  
The non-settlement entry price only reflects the average price at which the position is opened or increased.  
Applicable to `FUTURES` `cross`  
> settledPnl | String | Accumulated settled P&L (calculated by settlement price)  
Applicable to `FUTURES` `cross`  
  
\- The position data is sent on event basis and regular basis   
\- The event push is not pushed in real-time. It is aggregated and pushed at a fixed time interval, around 50ms. For example, if multiple events occur within a fixed time interval, the system will aggregate them into a single message and push it at the end of the fixed time interval. If the data volume is too large, it may be split into multiple messages.   
\- The regular push sends updates regardless of whether there are position activities or not.   
\- If an event push and a regular push happen at the same time, the system will send the event push first, followed by the regular push.  As for portfolio margin account, the IMR and MMR of the position are calculated in risk unit granularity, thus their values of the same risk unit cross positions are the same.  In the position-by-position trading setting, it is an autonomous transfer mode. After the margin is transferred, positions with a position of 0 will be pushed    
\- Only position with non-zero position quantity will be pushed. Definition of non-zero quantity: value of pos parameter is not 0. If the data is too large to be sent in a single push message, it will be split into multiple messages.   
\- For example, when subscribing to positions channel specifying an underlying and there are 20 positions are with non-zero quantity, all 20 positions data will be pushed in initial snapshot and in regular push. Subsequently when there is change in pos of a position, only the data of that position will be pushed triggered by this change.  Unlike futures contracts, option positions are automatically exercised or expire at maturity. The rights then terminate and no closing orders are generated. Therefore, this channel will not push any updates for expired option positions. 

### Balance and position channel

Retrieve account balance and position information. Data will be pushed when triggered by events such as filled order, funding transfer.  
This channel applies to getting the account cash balance and the change of position asset ASAP.   
Concurrent connection to this channel will be restricted by the following rules: [WebSocket connection count limit](/docs-v5/en/#overview-websocket-connection-count-limit).

#### URL Path

/ws/v5/private (required login)

> Request Example 
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [{
            "channel": "balance_and_position"
        }]
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
            url = "wss://ws.okx.com:8443/ws/v5/private",
            useServerTime=False
        )
        await ws.start()
        args = [{
            "channel": "balance_and_position"
        }]
    
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
`balance_and_position`  
  
> Response Example 
    
    
    {
        "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "balance_and_position"
        },
        "connId": "a4d3ae55"
    }
    

> Failure Response Example
    
    
    {
        "id": "1512",
        "event": "error",
        "code": "60012",
        "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"balance_and_position\"}]}",
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
arg | Object | No | List of subscribed channels  
> channel | String | Yes | Channel name  
`balance_and_position`  
code | String | No | Error code  
msg | String | No | Error message  
connId | String | Yes | WebSocket connection ID  
  
> Push Data Example
    
    
    {
        "arg": {
            "channel": "balance_and_position",
            "uid": "77982378738415879"
        },
        "data": [{
            "pTime": "1597026383085",
            "eventType": "snapshot",
            "balData": [{
                "ccy": "BTC",
                "cashBal": "1",
                "uTime": "1597026383085"
            }],
            "posData": [{
                "posId": "1111111111",
                "tradeId": "2",
                "instId": "BTC-USD-191018",
                "instType": "FUTURES",
                "mgnMode": "cross",
                "posSide": "long",
                "pos": "10",
                "ccy": "BTC",
                "posCcy": "",
                "avgPx": "3320",
                "nonSettleAvgPx": "",
                "settledPnl": "",
                "uTime": "1597026383085"
            }],
            "trades": [{
                "instId": "BTC-USD-191018",
                "tradeId": "2",
            }]
        }]
    }
    

#### Push data parameters

**Parameter** | **Type** | **Description**  
---|---|---  
arg | Object | Channel to subscribe to  
> channel | String | Channel name  
> uid | String | User Identifier  
data | Array of objects | Subscribed data  
> pTime | String | Push time of both balance and position information, millisecond format of Unix timestamp, e.g. `1597026383085`  
> eventType | String | Event Type  
`snapshot`  
`delivered`  
`exercised`  
`transferred`  
`filled`  
`liquidation`  
`claw_back`  
`adl`  
`funding_fee`  
`adjust_margin`  
`set_leverage`  
`interest_deduction`  
`settlement`  
> balData | Array of objects | Balance data  
>> ccy | String | Currency  
>> cashBal | String | Cash Balance  
>> uTime | String | Update time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
> posData | Array of objects | Position data  
>> posId | String | Position ID  
>> tradeId | String | Last trade ID  
>> instId | String | Instrument ID, e.g `BTC-USD-180213`  
>> instType | String | Instrument type  
>> mgnMode | String | Margin mode  
`isolated`, `cross`  
>> avgPx | String | Average open price  
>> ccy | String | Currency used for margin  
>> posSide | String | Position side  
`long`, `short`, `net`  
>> pos | String | Quantity of positions. In the isolated margin mode, when doing manual transfers, a position with pos of `0` will be generated after the deposit is transferred  
>> baseBal | String | ~~Base currency balance, only applicable to`MARGIN`（Quick Margin Mode）~~(Deprecated)  
>> quoteBal | String | ~~Quote currency balance, only applicable to`MARGIN`（Quick Margin Mode）~~(Deprecated)  
>> posCcy | String | Position currency, only applicable to MARGIN positions.  
>> nonSettleAvgPx | String | Non-Settlement entry price  
The non-settlement entry price only reflects the average price at which the position is opened or increased.  
Applicable to `FUTURES` `cross`  
>> settledPnl | String | Accumulated settled P&L (calculated by settlement price)  
Applicable to `FUTURES` `cross`  
>> uTime | String | Update time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
> trades | Array of objects | Details of trade  
>> instId | String | Instrument ID, e.g. `BTC-USDT`  
>> tradeId | String | Trade ID  
Only balData will be pushed if only the account balance changes; only posData will be pushed if only the position changes.    
\- Initial snapshot: Only either position with non-zero position quantity or cash balance with non-zero quantity will be pushed. If the data is too large to be sent in a single push message, it will be split into multiple messages.   
\- For example, if you subscribe according to all currencies and the user has 5 currency balances that are not 0 and 20 positions, all 20 positions data and 5 currency balances data will be pushed in initial snapshot; Subsequently when there is change in pos of a position, only the data of that position will be pushed triggered by this change. 

### Position risk warning

This push channel is only used as a risk warning, and is not recommended as a risk judgment for strategic trading   
In the case that the market is volatile, there may be the possibility that the position has been liquidated at the same time that this message is pushed.  
The warning is sent when a position is at risk of liquidation for isolated margin positions. The warning is sent when all the positions are at risk of liquidation for cross-margin positions.  
Concurrent connection to this channel will be restricted by the following rules: [WebSocket connection count limit](/docs-v5/en/#overview-websocket-connection-count-limit).

#### URL Path

/ws/v5/private (required login)

> Request Example
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "liquidation-warning",
          "instType": "ANY"
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
            url = "wss://ws.okx.com:8443/ws/v5/private",
            useServerTime=False
        )
        await ws.start()
        args = [
            {
              "channel": "liquidation-warning",
              "instType": "ANY"
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
`liquidation-warning`  
> instType | String | Yes | Instrument type  
`MARGIN`  
`SWAP`  
`FUTURES`  
`OPTION`   
`ANY`  
> instFamily | String | No | Instrument family  
Applicable to `FUTURES`/`SWAP`/`OPTION`  
> instId | String | No | Instrument ID  
  
> Successful Response Example
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "liquidation-warning",
        "instType": "ANY"
      },
      "connId": "a4d3ae55"
    }
    

> Failure Response Example
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"liquidation-warning\", \"instType\" : \"FUTURES\"}]}",
      "connId": "a4d3ae55"
    }
    

#### Response parameters

Parameter | Type | Required | Description  
---|---|---|---  
id | String | No | Unique identifier of the message  
event | String | Yes | Event  
`subscribe`  
`unsubscribe`  
`error`  
arg | Object | No | Subscribed channel  
> channel | String | Yes | Channel name  
`liquidation-warning`  
> instType | String | Yes | Instrument type  
`OPTION`  
`FUTURES`  
`SWAP`  
`MARGIN`   
`ANY`  
> instFamily | String | No | Instrument family  
> instId | String | No | Instrument ID  
code | String | No | Error code  
msg | String | No | Error message  
connId | String | Yes | WebSocket connection ID  
  
> Push Data Example
    
    
    {
        "arg":{
            "channel":"liquidation-warning",
            "uid": "77982378738415879",
            "instType":"FUTURES"
        },
        "data":[
            {
                "cTime":"1619507758793",
                "ccy":"ETH",
                "instId":"ETH-USD-210430",
                "instType":"FUTURES",
                "lever":"10",
                "markPx":"2353.849",
                "mgnMode":"isolated",
                "mgnRatio":"11.731726509588816",
                "pTime":"1619507761462",
                "pos":"1",
                "posCcy":"",
                "posId":"307173036051017730",
                "posSide":"long",
                "uTime":"1619507761462",
            }
        ]
    }
    

#### Push data parameters

Parameter | Type | Description  
---|---|---  
arg | Object | Successfully subscribed channel  
> channel | String | Channel name  
> uid | String | User Identifier  
> instType | String | Instrument type  
> instFamily | String | Instrument family  
> instId | String | Instrument ID  
data | Array of objects | Subscribed data  
> instType | String | Instrument type  
> mgnMode | String | Margin mode, `cross` `isolated`  
> posId | String | Position ID  
> posSide | String | Position side  
`long`   
`short`   
`net` (`FUTURES`/`SWAP`/`OPTION`: positive `pos` means long position and negative `pos` means short position. `MARGIN`: `posCcy` being base currency means long position, `posCcy` being quote currency means short position.)  
> pos | String | Quantity of positions  
> posCcy | String | Position currency, only applicable to `MARGIN` positions  
> instId | String | Instrument ID, e.g. `BTC-USDT-SWAP`  
> lever | String | Leverage, not applicable to `OPTION` seller  
> markPx | String | Mark price  
> mgnRatio | String | Maintenance margin ratio  
> ccy | String | Currency used for margin  
> cTime | String | Creation time, Unix timestamp format in milliseconds, e.g. `1597026383085`.  
> uTime | String | Latest time position was adjusted, Unix timestamp format in milliseconds, e.g. `1597026383085`.  
> pTime | String | Push time of positions information, Unix timestamp format in milliseconds, e.g. `1597026383085`.  
Trigger push logic: the trigger logic of the liquidation warning and the liquidation message is the same 

### Account greeks channel

Retrieve account greeks information. Data will be pushed when triggered by events such as increase/decrease positions or cash balance in account, and will also be pushed in regular interval according to subscription granularity.  
Concurrent connection to this channel will be restricted by the following rules: [WebSocket connection count limit](/docs-v5/en/#overview-websocket-connection-count-limit).

#### URL Path

/ws/v5/private (required login)

> Request Example
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [{
            "channel": "account-greeks"
        }]
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
            url = "wss://ws.okx.com:8443/ws/v5/private",
            useServerTime=False
        )
        await ws.start()
        args = [{
            "channel": "account-greeks"
        }]
    
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
`subscribe` `unsubscribe`  
args | Array of objects | Yes | List of subscribed channels  
> channel | String | Yes | Channel name  
`account-greeks`  
> ccy | String | No | Settlement currency  
When the user specifies a settlement currency, event push will only be triggered when the position of the same settlement currency changes. For example, when ccy=BTC, if the position of `BTC-USDT-SWAP` changes, no event push will be triggered.  
  
> Successful Response Example
    
    
    {
        "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "account-greeks"
        },
      "connId": "a4d3ae55"
    }
    

> Failure Response Example
    
    
    {
        "id": "1512",
        "event": "error",
        "code": "60012",
        "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"account-greeks\", \"ccy\" : \"BTC\"}]}",
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
> channel | String | Yes | Channel name,`account-greeks`  
> ccy | String | No | Settlement currency  
code | String | No | Error code  
msg | String | No | Error message  
connId | String | Yes | WebSocket connection ID  
  
> Push Data Example: single
    
    
    {
        "arg": {
            "channel": "account-greeks",
            "ccy": "BTC",
            "uid": "614488474791936"
        },
        "data": [
            {
                "ccy": "BTC",
                "deltaBS": "1.1246665401944310",
                "deltaPA": "-0.0074076183688949",
                "gammaBS": "0.0000000000000000",
                "gammaPA": "0.0148152367377899",
                "thetaBS": "2.0356991946421226",
                "thetaPA": "-0.0000000200174309",
                "ts": "1729179082006",
                "vegaBS": "0.0000000000000000",
                "vegaPA": "0.0000000000000000"
            }
        ]
    }
    

> Push Data Example
    
    
    {
        "arg": {
            "channel": "account-greeks",
            "uid": "614488474791936"
        },
        "data": [
            {
                "ccy": "BTC",
                "deltaBS": "1.1246665403011684",
                "deltaPA": "-0.0074021163991037",
                "gammaBS": "0.0000000000000000",
                "gammaPA": "0.0148042327982075",
                "thetaBS": "2.1342098201092528",
                "thetaPA": "-0.0000000200876441",
                "ts": "1729179001692",
                "vegaBS": "0.0000000000000000",
                "vegaPA": "0.0000000000000000"
            },
            {
                "ccy": "ETH",
                "deltaBS": "0.3810670161698570",
                "deltaPA": "-0.0688347042402955",
                "gammaBS": "-0.0000000000230396",
                "gammaPA": "0.1376693483440320",
                "thetaBS": "0.3314776517141782",
                "thetaPA": "0.0000000001316008",
                "ts": "1729179001692",
                "vegaBS": "-0.0000000045069794",
                "vegaPA": "-0.0000000000017267"
            }
        ]
    }
    

#### Push data parameters

**Parameters** | **Types** | **Description**  
---|---|---  
arg | Object | Successfully subscribed channel  
> channel | String | Channel name  
> uid | String | User Identifier  
data | Array of objects | Subscribed data  
> deltaBS | String | delta: Black-Scholes Greeks in dollars  
> deltaPA | String | delta: Greeks in coins  
> gammaBS | String | gamma: Black-Scholes Greeks in dollars, only applicable to OPTION cross  
> gammaPA | String | gamma: Greeks in coins, only applicable to OPTION cross  
> thetaBS | String | theta: Black-Scholes Greeks in dollars, only applicable to OPTION cross  
> thetaPA | String | theta: Greeks in coins, only applicable to OPTION cross  
> vegaBS | String | vega: Black-Scholes Greeks in dollars, only applicable to OPTION cross  
> vegaPA | String | vega: Greeks in coins, only applicable to OPTION cross  
> ccy | String | Currency  
> ts | String | Push time of account greeks, Unix timestamp format in milliseconds, e.g. 1597026383085  
The account greeks data is sent on event basis and regular basis   
\- The event push is not pushed in real-time. It is aggregated and pushed at a fixed time interval, around 50ms. For example, if multiple events occur within a fixed time interval, the system will aggregate them into a single message and push it at the end of the fixed time interval. If the data volume is too large, it may be split into multiple messages.   
\- When the user specifies a settlement currency in the subscribe request, event push will only be triggered when the position of the same settlement currency changes. For example, when subscribe `ccy`=BTC, if the position of `BTC-USDT-SWAP` changes, no event push will be triggered.   
\- The regular push sends updates regardless of whether there are activities or not.    
\- Only currencies in the account will be pushed. If the data is too large to be sent in a single push message, it will be split into multiple messages.   
\- For example, when subscribing to account-greeks channel without specifying ccy and there are 5 currencies are with non-zero balance, all 5 currencies data will be pushed in initial snapshot and in regular interval. Subsequently when there is change in balance or equity of an token, only the incremental data of that currency will be pushed triggered by this change.

---

# 交易账户

`账户`功能模块下的API接口需要身份验证。

## REST API 

### 获取交易产品基础信息 

获取当前账户可交易产品的信息列表。

#### 限速：20次/2s

#### 限速规则：User ID + Instrument Type

#### HTTP请求

`GET /api/v5/account/instruments`

> 请求示例
    
    
    GET /api/v5/account/instruments?instType=SPOT
    
    
    
    import okx.Account as Account
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    result = accountAPI.get_instruments(instType="SPOT")
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 是 | 产品类型  
`SPOT`：币币  
`MARGIN`：币币杠杆  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`OPTION`：期权  
`EVENTS`：事件合约  
seriesId | String | 可选 | 系列 ID，如 `BTC-ABOVE-DAILY`。当 instType 为 `EVENTS` 时必填  
instFamily | String | 可选 | 交易品种，仅适用于`交割`/`永续`/`期权`，期权必填  
instId | String | 否 | 产品ID  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "auctionEndTime": "",
                "baseCcy": "BTC",
                "ctMult": "",
                "ctType": "",
                "ctVal": "",
                "ctValCcy": "",
                "contTdSwTime": "1704876947000",
                "elp": "0",
                "expTime": "",
                "futureSettlement": false,
                "groupId": "4",
                "instFamily": "",
                "instId": "BTC-EUR",
                "instType": "SPOT",
                "lever": "",
                "listTime": "1704876947000",
                "lotSz": "0.00000001",
                "maxIcebergSz": "9999999999.0000000000000000",
                "maxLmtAmt": "1000000",
                "maxLmtSz": "9999999999",
                "maxMktAmt": "1000000",
                "maxMktSz": "1000000",
                "maxPlatOILmt": "1000000000",
                "maxPlatOICoinLmt": "",
                "maxStopSz": "1000000",
                "maxTriggerSz": "9999999999.0000000000000000",
                "maxTwapSz": "9999999999.0000000000000000",
                "minSz": "0.00001",
                "optType": "",
                "openType": "call_auction",
                "preMktSwTime": "",
                "posLmtPct": "30",
                "posLmtAmt": "2500000",
                "quoteCcy": "EUR",
                "tradeQuoteCcyList": [
                    "EUR"
                ],
                "settleCcy": "",
                "state": "live",
                "ruleType": "normal",
                "stk": "",
                "tickSz": "1",
                "uly": "",
                "instIdCode": 1000000000,
                "instCategory": "1",
                "initPxLmtPct": "0.05",
                "floatPxLmtPct": "0.03",
                "maxPxLmtPct": "0.15",
                "upcChg": [
                    {
                        "param": "tickSz",
                        "newValue": "0.0001",
                        "effTime": "1704876947000"
                    }
                ]
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
instType | String | 产品类型  
seriesId | String | 系列 ID，如 `BTC-ABOVE-DAILY`。仅适用于 `EVENTS`  
instId | String | 产品id， 如 `BTC-USDT`  
uly | String | 标的指数，如 `BTC-USD`，仅适用于`杠杆/交割/永续/期权`  
groupId | String | 交易产品手续费分组ID  
现货：  
`3`：TRY现货  
`5`：BRL现货  
`7`：AED现货  
`8`：AUD现货  
`10`：SGD现货  
`11`：零手续费现货  
`12`：现货分组一  
`13`：现货分组二  
`14`：现货分组三  
`15`: 现货特别分组  
`17`：现货稳定币分组  
  
交割合约：  
`5`：交割合约分组一  
`6`：交割合约分组二  
`8`：XPERP分组二  
`10`：XPERP RWA分组二  
  
永续合约：  
`4`：永续合约分组一  
`5`：永续合约分组二  
`6`：SWAP RWA分组一  
`7`：SWAP RWA分组二  
  
期权：  
`1`：币本位期权  
  
**用户需要同时使用instType和groupId来确定一个交易产品的交易手续费分组；用户应该将此接口和[获取当前账户交易手续费费率](/docs-v5/zh/#trading-account-rest-api-get-fee-rates)一起使用，以获取特定交易产品的手续费率**   
  
**部分枚举值可能不适用于您，以实际返回为准**  
instFamily | String | 交易品种，如 `BTC-USD`，仅适用于`杠杆/交割/永续/期权`  
baseCcy | String | 交易货币币种，如 `BTC-USDT` 中的 `BTC` ，仅适用于`币币/币币杠杆`  
quoteCcy | String | 计价货币币种，如 `BTC-USDT` 中的`USDT` ，仅适用于`币币/币币杠杆`  
settleCcy | String | 盈亏结算和保证金币种，如 `BTC` 仅适用于`交割`/`永续`/`期权`  
ctVal | String | 合约面值，仅适用于`交割`/`永续`/`期权`  
ctMult | String | 合约乘数，仅适用于`交割`/`永续`/`期权`  
ctValCcy | String | 合约面值计价币种，仅适用于`交割`/`永续`/`期权`  
optType | String | 期权类型，`C`或`P` 仅适用于`期权`  
stk | String | 行权价格，仅适用于`期权`  
listTime | String | 上线时间   
Unix时间戳的毫秒数格式，如 `1597026383085`  
auctionEndTime | String | ~~集合竞价结束时间，Unix时间戳的毫秒数格式，如`1597026383085`   
仅适用于通过集合竞价方式上线的`币币`，其余情况返回""（已废弃，请使用contTdSwTime）~~  
contTdSwTime | String | 连续交易开始时间，从集合竞价、提前挂单切换到连续交易的时间，Unix时间戳格式，单位为毫秒。e.g. `1597026383085`。  
仅适用于通过集合竞价或提前挂单上线的`SPOT`/`MARGIN`，在其他情况下返回""。  
preMktSwTime | String | 盘前交易产品切换为正常交易的时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
仅适用于盘前`SWAP` 与盘前 X-Perp `FUTURES`。当盘前 X-Perp 转换为正常 X-Perp 时填充  
openType | String | 开盘类型  
`fix_price`: 定价开盘  
`pre_quote`: 提前挂单  
`call_auction`: 集合竞价   
只适用于`SPOT`/`MARGIN`，其他业务线返回""  
elp | String | ELP 下单权限  
`0`：该币对不支持 ELP  
`1`：该币对支持 ELP 但用户没有权限为其下 ELP 订单  
`2`：该币对支持 ELP 且用户有权限为其下 ELP 订单  
  
`1/2`不代表深度中一定有 ELP 挂单  
expTime | String | 产品下线时间  
适用于`币币/杠杆/交割/永续/期权`，对于 `交割/期权`，为交割/行权日期；亦可以为产品下线时间，有变动就会推送。  
lever | String | 该`instId`支持的最大杠杆倍数，不适用于`币币`、`期权`  
tickSz | String | 下单价格精度，如 `0.0001`。  
对于 `OPTION`/`EVENTS`，该值为 tick band 中的最小 tickSz。如需获取各价格区间的精确 tickSz，请使用"获取期权价格梯度"接口并传入对应的 `instType` 参数。  
lotSz | String | 下单数量精度  
合约的数量单位是`张`，现货的数量单位是`交易货币`  
minSz | String | 最小下单数量  
合约的数量单位是`张`，现货的数量单位是`交易货币`  
ctType | String | 合约类型  
`linear`：正向合约  
`inverse`：反向合约  
仅适用于`交割/永续`  
state | String | 产品状态  
`live`：交易中   
`suspend`：暂停中  
`rebase`：合约在变基中，不可交易，仅适用于`SWAP`  
`post_only`：仅接受 post-only 订单；已有 post-only 订单可改单和撤单。其他订单类型（市价单、IOC、FOK、普通限价单）将被拒绝。仅适用于 `SWAP`  
`preopen`：预上线，交割和期权合约轮转生成到开始交易；部分交易产品上线前  
`test`：测试中（测试产品，不可交易）  
`settling`：结算中，仅适用于 `EVENTS`  
ruleType | String | 交易规则类型  
`normal`：普通交易  
`pre_market`：盘前交易，含盘前 X-Perp `FUTURES`  
`rebase_contract`：盘前变基合约  
`xperp`：永续合约风格的交割合约，仅适用于部分 `FUTURES` 合约。盘前 X-Perp 转换为正常 X-Perp 后，由 `pre_market` 变为 `xperp`  
posLmtAmt | String | 单一用户（母子账户共享）层面的该产品最大持仓名义价值（USD），按同方向已持仓与挂单的美元名义价值计算。单用户有效上限为 max(posLmtAmt, oiUSD × posLmtPct)。适用于 `SWAP`/`FUTURES`。  
posLmtPct | String | 单一用户（母子账户共享）相对于平台当前总持仓名义价值可持有的最大比例（如 30 表示 30%）。单用户有效上限为 max(posLmtAmt, oiUSD × posLmtPct)。适用于 `SWAP`/`FUTURES`。  
maxPlatOILmt | String | 该产品的全平台最大持仓名义价值（USD）。当平台总持仓量（USD）达到或超过该值时，系统将拒绝所有用户对该产品的新开仓委托；否则订单通过校验。  
适用于 `SWAP`/`FUTURES`  
maxPlatOICoinLmt | String | 该产品的全平台最大持仓名义价值（币量）。当平台总持仓量（币量）达到或超过该值时，系统将拒绝所有用户对该产品的新开仓委托；否则订单通过校验。  
适用于 `SWAP`/`FUTURES`  
longPosRemainingQuota | String | 单一用户维度（母子账户共享），在该产品下扣除已有多头仓位及挂单中的买入订单后，仍可开立的多头仓位剩余额度（以 USD 计）。  
shortPosRemainingQuota | String | 单一用户维度（母子账户共享），在该产品下扣除已有空头仓位及挂单中的卖出订单后，仍可开立的空头仓位剩余额度（以 USD 计）。  
maxLmtSz | String | 限价单的单笔最大委托数量  
合约的数量单位是`张`，现货的数量单位是`交易货币`  
maxMktSz | String | 市价单的单笔最大委托数量  
合约的数量单位是`张`，现货的数量单位是`USDT`  
maxLmtAmt | String | 限价单的单笔最大美元价值  
maxMktAmt | String | 市价单的单笔最大美元价值  
仅适用于`币币/币币杠杆`  
maxTwapSz | String | 时间加权单的单笔最大委托数量  
合约的数量单位是`张`，现货的数量单位是`交易货币`   
单笔最小委托数量为 minSz*2  
maxIcebergSz | String | 冰山委托的单笔最大委托数量  
合约的数量单位是`张`，现货的数量单位是`交易货币`  
maxTriggerSz | String | 计划委托委托的单笔最大委托数量  
合约的数量单位是`张`，现货的数量单位是`交易货币`  
maxStopSz | String | 止盈止损市价委托的单笔最大委托数量  
合约的数量单位是`张`，现货的数量单位是`USDT`  
futureSettlement | Boolean | 交割合约是否支持每日结算  
适用于`全仓``交割`  
tradeQuoteCcyList | Array of strings | 可用于交易的计价币种列表，如 ["USD", "USDC"].  
instIdCode | Integer | 产品唯一标识代码。  
对于简单二进制编码，您必须使用 `instIdCode` 而不是 `instId`。  
对于同一`instId`，实盘和模拟盘的值可能会不一样。   
当值还未生成时，返回 `null`。  
instCategory | String | 标的资产类别（产品ID的第一部分）。例如：对于 `BTC-USDT-SWAP`，instCategory 表示 `BTC` 所属的资产类别。  
`1`: 加密货币   
`3`: 股票类资产   
`4`: 大宗商品   
`5`: 外汇   
`6`: 债券   
`""` 当值不可用时返回空字符串  
initPxLmtPct | String | 合约上线后前 10 分钟内的初始价格限制区间，小数百分比，例如 `0.05` 代表 5%。通过 GET /api/v5/public/price-limit 可获取对应价格限制。  
适用于 `SPOT`/`MARGIN`/`SWAP`/`FUTURES`；`OPTION` 和 `EVENTS` 返回 `""`。  
floatPxLmtPct | String | 常规交易期间的浮动价格限制区间，小数百分比，例如 `0.03` 代表 3%。通过 GET /api/v5/public/price-limit 可获取对应价格限制。  
适用于 `SPOT`/`MARGIN`/`SWAP`/`FUTURES`；`OPTION` 和 `EVENTS` 返回 `""`。  
maxPxLmtPct | String | 最大价格限制上限（下单价格相对指数价格偏离的硬性上限），小数百分比，例如 `0.15` 代表 15%。通过 GET /api/v5/public/price-limit 可获取对应价格限制。  
适用于 `SPOT`/`MARGIN`/`SWAP`/`FUTURES`；`OPTION` 和 `EVENTS` 返回 `""`。  
upcChg | Array of objects | 即将变更的参数列表。当没有即将变更的参数时，返回空数组 []  
> param | String | 即将变更的参数名称。  
`tickSz`  
`minSz`：若为交割/永续合约（`FUTURES`/`SWAP`），`lotSz` 会同步变更。  
`maxMktSz`  
> newValue | String | 即将变更的参数值。  
> effTime | String | 生效时间。Unix 时间戳格式，例如 `1597026383085`  
listTime以及contTdSwTime  
对于通过集合竞价/提前挂单方式上线的币币，listTime为集合竞价/提前挂单的开始时间，contTdSwTime为集合竞价/提前挂单的结束时间、连续交易的开始时间；对于其他情况及业务线，listTime即为连续交易开始时间，contTdSwTime将返回""  state  
对于`币币`、`杠杆`、`永续`和`交割`，状态state在时间到达listTime时由`preopen`转变为`live`。对于`期权`合约，由于内部处理原因，状态可能在`listTime`之后短暂延迟变为`live`。建议在下单前确认`state`为`live`。  
当产品下线的时候（如交割合约被交割的时候，期权合约被行权的时候），查询不到该产品 

### 查看账户余额 

获取交易账户中资金余额信息。

免息额度和折算率都是公共数据，不在账户接口内展示 

#### 限速：10次/2s

#### 限速规则：User ID

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
  
### 查看持仓信息 

获取该账户下拥有实际持仓的信息。账户为买卖模式会显示净持仓（`net`），账户为开平仓模式下会分别返回开多（`long`）或开空（`short`）的仓位。按照仓位创建时间倒序排列。

#### 限速：10次/2s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/account/positions`

> 请求示例
    
    
    # 查看BTC-USDT的持仓信息
    GET /api/v5/account/positions?instId=BTC-USDT
    
    
    
    
    import okx.Account as Account
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # 查看持仓信息
    result = accountAPI.get_positions()
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 否 | 产品类型  
`MARGIN`：币币杠杆  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`OPTION`：期权  
`EVENTS`：事件合约  
`instType`和`instId`同时传入的时候会校验`instId`与`instType`是否一致。  
instId | String | 否 | 交易产品ID，如：`BTC-USDT-SWAP`  
支持多个`instId`查询（不超过10个），半角逗号分隔  
posId | String | 否 | 持仓ID  
支持多个`posId`查询（不超过20个）。  
存在有效期的属性，自最近一次完全平仓算起，满30天 posId 以及整个仓位会被清除。  
如果该 instId 拥有过仓位且当前持仓量为0，传 instId 时，如果当前存在有效的posId，会返回仓位信息，如果当前不存在有效的 posId 时，不会返回仓位信息；不传 instId 时，仓位信息不返回。  逐仓交易设置中，如果设置为自主划转模式，逐仓转入保证金后，会生成一个持仓量为0的仓位 

> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "adl": "1",
                "availPos": "0.00190433573",
                "avgPx": "62961.4",
                "baseBal": "",
                "baseBorrowed": "",
                "baseInterest": "",
                "bePx": "",
                "bizRefId": "",
                "bizRefType": "",
                "cTime": "1724740225685",
                "ccy": "BTC",
                "clSpotInUseAmt": "",
                "closeOrderAlgo": [],
                "deltaBS": "",
                "deltaPA": "",
                "fee": "",
                "fundingFee": "",
                "gammaBS": "",
                "gammaPA": "",
                "hedgedPos": "",
                "idxPx": "62890.5",
                "imr": "",
                "instId": "BTC-USDT",
                "instType": "MARGIN",
                "interest": "0",
                "last": "62892.9",
                "lever": "5",
                "liab": "-99.9998177776581948",
                "liabCcy": "USDT",
                "liqPenalty": "",
                "liqPx": "53615.448336593756",
                "margin": "0.000317654",
                "markPx": "62891.9",
                "maxSpotInUseAmt": "",
                "mgnMode": "isolated",
                "mgnRatio": "9.404143929947395",
                "mmr": "0.0000318005395854",
                "notionalUsd": "119.756628017499",
                "optVal": "",
                "pendingCloseOrdLiabVal": "0",
                "pnl": "",
                "pos": "0.00190433573",
                "posCcy": "BTC",
                "posId": "1752810569801498626",
                "posSide": "net",
                "quoteBal": "",
                "quoteBorrowed": "",
                "quoteInterest": "",
                "realizedPnl": "",
                "spotInUseAmt": "",
                "spotInUseCcy": "",
                "thetaBS": "",
                "thetaPA": "",
                "tradeId": "785524470",
                "uTime": "1724742632153",
                "upl": "-0.0000033452492717",
                "uplLastPx": "-0.0000033199677697",
                "uplRatio": "-0.0105311101755551",
                "uplRatioLastPx": "-0.0104515220008934",
                "usdPx": "",
                "vegaBS": "",
                "vegaPA": "",
                "nonSettleAvgPx":"",
                "settledPnl":""
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
instType | String | 产品类型  
`MARGIN`：币币杠杆  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`OPTION`：期权  
`EVENTS`：事件合约  
mgnMode | String | 保证金模式  
`cross`：全仓  
`isolated`：逐仓  
posId | String | 持仓ID  
posSide | String | 持仓方向  
`long`：开平仓模式开多，`pos`为正   
`short`：开平仓模式开空，`pos`为正  
`net`：买卖模式（`交割`/`永续`/`期权`：`pos`为正代表开多，`pos`为负代表开空。`币币杠杆`时，`pos`均为正，`posCcy`为交易货币时，代表开多；`posCcy`为计价货币时，代表开空。）  
pos | String | 持仓量。单位：SWAP/FUTURES/OPTIONS为合约张数；MARGIN为标的币数量。符号（net模式）：正数=多头，负数=空头。long/short模式下按方向分开返回，请结合 `posSide` 判断。逐仓模式下手动划转保证金后，会生成一条 pos 为 `0` 的仓位记录（表示已划入资金但尚无持仓的状态）。  
hedgedPos | String | 对冲持仓数量  
仅在delta 中性策略模式的账户返回stgyType:1，对普通策略模式的账户返回""  
baseBal | String | ~~交易币余额，适用于`币币杠杆`（逐仓一键借币模式）~~（已弃用）  
quoteBal | String | ~~计价币余额 ，适用于`币币杠杆`（逐仓一键借币模式）~~（已弃用）  
baseBorrowed | String | ~~交易币已借，适用于`币币杠杆`（逐仓一键借币模式）~~（已弃用）  
baseInterest | String | ~~交易币计息，适用于`币币杠杆`（逐仓一键借币模式）~~（已弃用）  
quoteBorrowed | String | ~~计价币已借，适用于`币币杠杆`（逐仓一键借币模式）~~（已弃用）  
quoteInterest | String | ~~计价币计息，适用于`币币杠杆`（逐仓一键借币模式）~~（已弃用）  
posCcy | String | 仓位资产币种，仅适用于`币币杠杆`仓位  
availPos | String | 可平仓数量，适用于 `币币杠杆`，`期权`  
对于杠杆仓位，平仓时，杠杆还清负债后，余下的部分会视为币币交易，如果想要减少币币交易的数量，可通过"获取最大可用数量"接口获取只减仓的可用数量。  
avgPx | String | 当前持仓的成交量加权平均开仓价格。线性合约以计价货币计价（如BTC-USDT-SWAP以USDT计），反向合约以USD计价（如BTC-USD-SWAP以USD计）。每次影响仓位大小的成交后重新计算。开仓均价  
会随结算周期变化，特别是在交割合约全仓模式下，结算时开仓均价会更新为结算价格，同时新增头寸也会改变开仓均价。  
nonSettleAvgPx | String | 未结算均价  
不受结算影响的加权开仓价格，仅在新增头寸时更新，和开仓均价的主要区别在于是否受到结算影响。  
仅适用于`全仓``交割`  
upl | String | 当前持仓按标记价格计算的未实现盈亏，以该合约的结算货币（见 `ccy`）计价。公式：线性 = (标记价格 − 开仓均价) × 持仓量 × `ctVal`；反向 = (1/开仓均价 − 1/标记价格) × 持仓量 × `ctVal`。账户层面USD总计见 GET /api/v5/account/balance 中的 `upl`。  
uplRatio | String | 未实现收益率（以标记价格计算  
uplLastPx | String | 以最新成交价格计算的未实现收益，主要做展示使用，实际值还是 upl  
uplRatioLastPx | String | 以最新成交价格计算的未实现收益率  
instId | String | 产品ID，如 `BTC-USDT-SWAP`  
lever | String | 杠杆倍数，不适用于`期权`以及`组合保证金模式`下的全仓仓位  
liqPx | String | 预估强平价格。这是基于当前权益和保证金率的估算值，实际强平价格可能因资金费率累计、其他仓位变动或市场剧烈波动而迅速变化。  
不适用于 `OPTION`  
markPx | String | 最新标记价格  
imr | String | 该全仓持仓的初始保证金要求，以USD计价。公式：仓位数量 × 标记价格 × 初始保证金率（1/杠杆）。账户级别IMR请见 GET /api/v5/account/balance 中的 `imr`。逐仓持仓返回空字符串。仅适用于 `全仓`。  
margin | String | 保证金余额，可增减，仅适用于`逐仓`  
mgnRatio | String | 维持保证金率  
mmr | String | 维持保证金  
liab | String | 负债额，仅适用于`币币杠杆`  
liabCcy | String | 负债币种，仅适用于`币币杠杆`  
interest | String | 利息，已经生成的未扣利息  
tradeId | String | 最新成交ID  
optVal | String | 期权市值，仅适用于`期权`  
pendingCloseOrdLiabVal | String | 逐仓杠杆负债对应平仓挂单的数量  
notionalUsd | String | 以美金价值为单位的持仓数量  
adl | String | 自动减仓（ADL）指标。范围：0–5，0 = ADL优先级最低（最不可能被强制减仓），5 = 优先级最高（保险基金耗尽时最先被减仓）。优先级随未实现盈利增大和杠杆倍数增加而升高。  
仅适用于 `FUTURES/SWAP/OPTION`  
ccy | String | 占用保证金的币种  
last | String | 最新成交价  
idxPx | String | 最新指数价格  
usdPx | String | 保证金币种的市场最新美金价格 仅适用于`交割`/`永续`/`期权`  
bePx | String | 盈亏平衡价  
deltaBS | String | 美金本位持仓仓位delta，仅适用于`期权`  
deltaPA | String | 币本位持仓仓位delta，仅适用于`期权`  
gammaBS | String | 美金本位持仓仓位gamma，仅适用于`期权`  
gammaPA | String | 币本位持仓仓位gamma，仅适用于`期权`  
thetaBS | String | 美金本位持仓仓位theta，仅适用于`期权`  
thetaPA | String | 币本位持仓仓位theta，仅适用于`期权`  
vegaBS | String | 美金本位持仓仓位vega，仅适用于`期权`  
vegaPA | String | 币本位持仓仓位vega，仅适用于`期权`  
spotInUseAmt | String | 现货对冲占用数量  
适用于`组合保证金模式`  
spotInUseCcy | String | 现货对冲占用币种，如 `BTC`  
适用于`组合保证金模式`  
clSpotInUseAmt | String | 用户自定义现货占用数量  
适用于`组合保证金模式`  
maxSpotInUseAmt | String | 系统计算得到的最大可能现货占用数量  
适用于`组合保证金模式`  
realizedPnl | String | 已实现收益  
仅适用于`交割`/`永续`/`期权`  
`realizedPnl`=`pnl`+`fee`+`fundingFee`+`liqPenalty`+`settledPnl`  
settledPnl | String | 已结算收益  
仅适用于`全仓``交割`  
pnl | String | 平仓订单累计收益额(不包括手续费)  
fee | String | 自当前仓位开仓起累计手续费，仓位完全平仓后重置为0。逐笔手续费详情请使用 GET /api/v5/trade/fills。累计手续费金额，正数代表平台返佣 ，负数代表平台扣除  
fundingFee | String | 累计资金费用  
liqPenalty | String | 累计爆仓罚金，有值时为负数。  
closeOrderAlgo | Array of objects | 平仓策略委托订单。调用策略委托下单，且`closeFraction`=1 时，该数组才会有值。  
> algoId | String | 策略委托单ID  
> slTriggerPx | String | 止损触发价  
> slTriggerPxType | String | 止损触发价类型  
`last`：最新价格  
`index`：指数价格  
`mark`：标记价格  
> tpTriggerPx | String | 止盈触发价  
> tpTriggerPxType | String | 止盈触发价类型  
`last`：最新价格  
`index`：指数价格  
`mark`：标记价格  
> closeFraction | String | 策略委托触发时，平仓的百分比。1 代表100%  
cTime | String | 持仓创建时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
uTime | String | 最近一次持仓更新时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
bizRefId | String | 外部业务id，如 体验券id  
bizRefType | String | 外部业务类型  
PM账户下，持仓的 IMR MMR的数据是后端服务以ristUnit为最小粒度重新计算，相同riskUnit全仓仓位的imr和mmr返回值相同。 

### 查看历史持仓信息 

获取最近3个月有更新的仓位信息，按照仓位更新时间倒序排列。于**2024年11月11日中午12:00（UTC+8）** 开始支持组合保证金账户模式下的历史持仓。

#### 限速：10次/2s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/account/positions-history`

> 请求示例
    
    
    GET /api/v5/account/positions-history
    
    
    
    import okx.Account as Account
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # 查看历史持仓信息
    result = accountAPI.get_positions_history()
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 否 | 产品类型  
`MARGIN`：币币杠杆  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`OPTION`：期权  
`EVENTS`：事件合约  
instId | String | 否 | 交易产品ID，如：`BTC-USD-SWAP`  
mgnMode | String | 否 | 保证金模式  
`cross`：全仓，`isolated`：逐仓  
type | String | 否 | 最近一次平仓的类型  
`1`：部分平仓;`2`：完全平仓;`3`：强平;`4`：强减; `5`：ADL自动减仓 - 仓位未完全平仓; `6`：ADL自动减仓 - 仓位完全平仓  
状态叠加时，以最新的平仓类型为准状态为准。  
posId | String | 否 | 持仓ID。存在有效期的属性，自最近一次完全平仓算起，满30天 posId 会失效，之后的仓位，会使用新的 posId。  
after | String | 否 | 查询仓位更新 (uTime) 之前的内容，值为时间戳，Unix 时间戳为毫秒数格式，如 `1597026383085`  
before | String | 否 | 查询仓位更新 (uTime) 之后的内容，值为时间戳，Unix 时间戳为毫秒数格式，如 `1597026383085`  
limit | String | 否 | 分页返回结果的数量，最大为100，默认100条，uTime 相同的记录均会在当前请求中全部返回  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "cTime": "1654177169995",
                "ccy": "BTC",
                "closeAvgPx": "29786.5999999789081085",
                "closeTotalPos": "1",
                "instId": "BTC-USD-SWAP",
                "instType": "SWAP",
                "lever": "10.0",
                "mgnMode": "cross",
                "openAvgPx": "29783.8999999995535393",
                "openMaxPos": "1",
                "realizedPnl": "0.001",
                "fee": "-0.0001",
                "fundingFee": "0",
                "liqPenalty": "0",
                "pnl": "0.0011",
                "pnlRatio": "0.000906447858888",
                "posId": "452587086133239818",
                "posSide": "long",
                "direction": "long",
                "triggerPx": "",
                "type": "1",
                "uTime": "1654177174419",
                "uly": "BTC-USD",
                "nonSettleAvgPx":"",
                "settledPnl":""
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
instType | String | 产品类型  
`MARGIN`：币币杠杆  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`OPTION`：期权  
`EVENTS`：事件合约  
instId | String | 交易产品ID  
mgnMode | String | 保证金模式  
`cross`：全仓  
`isolated`：逐仓  
type | String | 最近一次平仓的类型  
`1`：部分平仓  
`2`：完全平仓  
`3`：强平  
`4`：强减  
`5`：ADL自动减仓  
状态叠加时，以最新的平仓类型为准状态为准。  
cTime | String | 仓位创建时间  
uTime | String | 仓位更新时间  
openAvgPx | String | 开仓均价  
会随结算周期变化，特别是在交割合约全仓模式下，结算时开仓均价会更新为结算价格，同时新增头寸也会改变开仓均价。  
nonSettleAvgPx | String | 未结算均价  
不受结算影响的加权开仓价格，仅在新增头寸时更新，和开仓均价的主要区别在于是否受到结算影响。  
仅适用于`全仓``交割`  
closeAvgPx | String | 平仓均价  
posId | String | 仓位ID  
openMaxPos | String | 最大持仓量  
closeTotalPos | String | 累计平仓量  
realizedPnl | String | 已实现收益  
仅适用于`交割`/`永续`/`期权`  
`realizedPnl`=`pnl`+`fee`+`fundingFee`+`liqPenalty`+`settledPnl`  
settledPnl | String | 已实现收益  
仅适用于`全仓``交割`  
pnlRatio | String | 已实现收益率  
fee | String | 累计手续费金额  
正数代表平台返佣，负数代表平台扣除。  
fundingFee | String | 累计资金费用  
liqPenalty | String | 累计爆仓罚金，有值时为负数。  
pnl | String | 已实现收益(不包括手续费)  
posSide | String | 持仓模式方向  
`long`：开平仓模式开多  
`short`：开平仓模式开空  
`net`：买卖模式  
lever | String | 杠杆倍数  
direction | String | 持仓方向  
`long`：多  
`short`：空  
仅适用于 `杠杆`/`交割`/`永续`/`期权`  
triggerPx | String | 触发标记价格  
`type` 为`3`,`4`,`5`时有值；为`1`, `2` 时为空  
uly | String | 标的指数  
ccy | String | 占用保证金的币种  
  
### 查看账户持仓风险 

查看账户整体风险。

获取同一时间切片上的账户和持仓的基础信息 

#### 限速：10次/2s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/account/account-position-risk`

> 请求示例
    
    
    GET /api/v5/account/account-position-risk
    
    
    
    
    import okx.Account as Account
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # 查看账户特定风险状态
    result = accountAPI.get_account_position_risk()
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 否 | 产品类型  
`MARGIN`：币币杠杆  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`OPTION`：期权   
  
  
> 返回结果
    
    
    {
        "code":"0",
        "data":[
            {
                "adjEq":"174238.6793649711331679",
                "balData":[
                    {
                        "ccy":"BTC",
                        "disEq":"78846.7803721021362242",
                        "eq":"1.3863533369419636"
                    },
                    {
                        "ccy":"USDT",
                        "disEq":"73417.2495112863300127",
                        "eq":"73323.395564963177146"
                    }
                ],
                "posData":[
                    {
                        "baseBal": "0.4",
                        "ccy": "",
                        "instId": "BTC-USDT",
                        "instType": "MARGIN",
                        "mgnMode": "isolated",
                        "notionalCcy": "0",
                        "notionalUsd": "0",
                        "pos": "0",
                        "posCcy": "",
                        "posId": "310388685292318723",
                        "posSide": "net",
                        "quoteBal": "0"
                    }
                ],
                "ts":"1620282889345"
            }
        ],
        "msg":""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
ts | String | 获取账户信息数据的时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
adjEq | String | 美金层面有效保证金  
适用于`跨币种保证金模式` 和`组合保证金模式`  
balData | Array of objects | 币种资产信息  
> ccy | String | 币种  
> eq | String | 币种总权益  
> disEq | String | 美金层面币种折算权益  
posData | Array of objects | 持仓详细信息  
> instType | String | 产品类型  
> mgnMode | String | 保证金模式  
`cross`：全仓  
`isolated`：逐仓  
> posId | String | 持仓ID  
> instId | String | 产品ID，如 `BTC-USDT-SWAP`  
> pos | String | 以`张`为单位的持仓数量，逐仓自主划转模式下，转入保证金后会产生pos为`0`的仓位  
> baseBal | String | ~~交易币余额，适用于`币币杠杆`（逐仓一键借币模式）~~（已弃用）  
> quoteBal | String | ~~计价币余额 ，适用于`币币杠杆`（逐仓一键借币模式）~~（已弃用）  
> posSide | String | 持仓方向  
`long`：开平仓模式开多  
`short`：开平仓模式开空  
`net`：买卖模式（`交割`/`永续`/`期权`：`pos`为正代表开多，`pos`为负代表开空。`币币杠杆`：`posCcy`为交易货币时，代表开多；`posCcy`为计价货币时，代表开空。）  
> posCcy | String | 仓位资产币种，仅适用于`币币杠杆`仓位  
> ccy | String | 占用保证金的币种  
> notionalCcy | String | 以`币`为单位的持仓数量  
> notionalUsd | String | 以`美金价值`为单位的持仓数量  
  
### 账单流水查询（近七天）

帐户资产流水是指导致帐户余额增加或减少的行为。本接口可以查询最近7天的账单数据。

#### 限速：5次/s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/account/bills`

> 请求示例
    
    
    GET /api/v5/account/bills
    
    GET /api/v5/account/bills?instType=MARGIN
    
    
    
    
    import okx.Account as Account
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘：0 , 模拟盘：1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # 查看账户账单详情 （近七日内）
    result = accountAPI.get_account_bills()
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 否 | 产品类型  
`SPOT`：币币  
`MARGIN`：币币杠杆  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`OPTION`：期权  
`EVENTS`：事件合约  
instId | String | 否 | 产品ID，如 `BTC-USDT`  
ccy | String | 否 | 账单币种  
mgnMode | String | 否 | 仓位类型  
`isolated`：逐仓  
`cross`：全仓  
ctType | String | 否 | 合约类型  
`linear`：正向合约  
`inverse`：反向合约  
仅`交割/永续`有效  
type | String | 否 | 账单类型  
枚举值请通过 [获取账单类型](/docs-v5/zh/#trading-account-rest-api-get-bill-types) 接口查询。  
subType | String | 否 | 账单子类型  
枚举值请通过 [获取账单类型](/docs-v5/zh/#trading-account-rest-api-get-bill-types) 接口查询。  
after | String | 否 | 请求此id之前（更旧的数据）的分页内容，传的值为对应接口的`billId`  
before | String | 否 | 请求此id之后（更新的数据）的分页内容，传的值为对应接口的`billId`  
begin | String | 否 | 筛选的开始时间戳 `ts`，Unix 时间戳为毫秒数格式，如 1597026383085  
end | String | 否 | 筛选的结束时间戳 `ts`，Unix 时间戳为毫秒数格式，如 1597027383085  
limit | String | 否 | 分页返回的结果集数量，最大为100，不填默认返回100条  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
            "bal":  "8694.2179403378290202",
            "balChg":  "0.0219338232210000",
            "billId":  "623950854533513219",
            "ccy":  "USDT",
            "clOrdId":  "",
            "earnAmt": "",
            "earnApr": "",
            "execType":  "T",
            "fee":  "-0.000021955779",
            "fillFwdPx":  "",
            "fillIdxPx":  "27104.1",
            "fillMarkPx":  "",
            "fillMarkVol":  "",
            "fillPxUsd":  "",
            "fillPxVol":  "",
            "fillTime":  "1695033476166",
            "from":  "",
            "instId":  "BTC-USDT",
            "instType":  "SPOT",
            "interest":  "0",
            "mgnMode":  "isolated",
            "notes":  "",
            "ordId":  "623950854525124608",
            "pnl":  "0",
            "posBal":  "0",
            "posBalChg":  "0",
            "px":  "27105.9",
            "subType":  "1",
            "sz":  "0.021955779",
            "tag":  "",
            "to":  "",
            "tradeId":  "586760148",
            "ts":  "1695033476167",
            "type":  "2"
        }]
    } 
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
instType | String | 产品类型  
billId | String | 账单ID  
type | String | 账单类型  
subType | String | 账单子类型  
ts | String | 余额更新完成的时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
balChg | String | 本次事件导致的账户余额变动量，以 `ccy` 字段指定的货币计价。正值表示余额增加（如收到资金费返佣、平仓盈利）；负值表示余额减少（如支付手续费、结算亏损）。  
posBalChg | String | 仓位层面的余额变动数量  
bal | String | 账户层面的余额数量  
posBal | String | 仓位层面的余额数量  
sz | String | 数量  
对于交割、永续以及期权，为成交或者持仓的数量，单位为张，总为正数。  
其他情况下，单位为账户余额币种（`ccy`）。  
px | String | 价格，与 subType 相关  

* 为成交价格时有
`1`：买入 `2`：卖出 `3`：开多 `4`：开空 `5`：平多 `6`：平空 `204`：大宗交易买 `205`：大宗交易卖 `206`：大宗交易开多 `207`：大宗交易开空 `208`：大宗交易平多 `209`：大宗交易平空 `114`：自动换币买入 `115`：自动换币卖出  

* 为强平价格时有
`100`：强减平多 `101`：强减平空 `102`：强减买入 `103`：强减卖出 `104`：强平平多 `105`：强平平空 `106`：强平买入 `107`：强平卖出 `16`：强制还币 `17`：强制借币还息 `110`：强平换币转入 `111`：强平换币转出  

* 为交割价格时有
`112`：交割平多 `113`：交割平空  

* 为行权价格时有
`170`：到期行权 `171`：到期被行权 `172`：到期作废  

* 为标记价格时有
`173`：资金费支出 `174`：资金费收入  
ccy | String | 账户余额币种  
pnl | String | 收益  
fee | String | 手续费  
正数代表平台返佣 ，负数代表平台扣除  
[手续费规则](/cn/fees)  
earnAmt | String | 自动赚币数量  
仅适用于type 381  
earnApr | String | 自动赚币实际年利率   
仅适用于type 381  
mgnMode | String | 保证金模式  
`isolated`：逐仓  
`cross`：全仓  
`cash`：非保证金  
如果账单不是由交易产生的，该字段返回 ""  
instId | String | 产品ID，如 `BTC-USDT`  
ordId | String | 订单ID  
当type为`2`/`5`/`9`时，返回相应订单id  
无订单时，该字段返回 ""  
execType | String | 流动性方向  
`T`：taker  
`M`：maker  
from | String | 转出账户  
`6`：资金账户  
`18`：交易账户  
仅适用于`资金划转`，不是`资金划转`时，返回 ""  
to | String | 转入账户  
`6`：资金账户  
`18`：交易账户  
仅适用于`资金划转`，不是`资金划转`时，返回 ""  
notes | String | 备注  
interest | String | 利息  
tag | String | 订单标签   
字母（区分大小写）与数字的组合，可以是纯字母、纯数字，且长度在1-16位之间。  
fillTime | String | 最新成交时间  
tradeId | String | 最新成交ID  
clOrdId | String | 客户自定义订单ID  
fillIdxPx | String | 交易执行时的指数价格 d  
对于交叉现货币对，返回 baseCcy-USDT 的指数价格。 例如 LTC-ETH，该字段返回 LTC-USDT 的指数价格。  
fillMarkPx | String | 成交时的标记价格，仅适用于 `交割`/`永续`/`期权`  
fillPxVol | String | 成交时的隐含波动率，仅适用于 `期权`，其他业务线返回空字符串""  
fillPxUsd | String | 成交时的期权价格，以USD为单位，仅适用于期权，其他业务线返回空字符串""  
fillMarkVol | String | 成交时的标记波动率，仅适用于期权，其他业务线返回空字符串""  
fillFwdPx | String | 成交时的远期价格，仅适用于期权，其他业务线返回空字符串""  
**资金费支出(subType = 173)**  
可以用"pnl"查询资金费的支出总额 

### 账单流水查询（近三个月）

帐户资产流水是指导致帐户余额增加或减少的行为。本接口可以查询最近 3 个月的账单数据。

#### 限速：5次/2s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/account/bills-archive`

> 请求示例
    
    
    GET /api/v5/account/bills-archive
    
    GET /api/v5/account/bills-archive?instType=MARGIN
    
    
    
    
    import okx.Account as Account
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # 查看账户账单详情 （近三个月内）
    result = accountAPI.get_account_bills_archive()
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 否 | 产品类型  
`SPOT`：币币  
`MARGIN`：币币杠杆  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`OPTION`：期权  
`EVENTS`：事件合约  
instId | String | 否 | 产品ID，如 `BTC-USDT`  
ccy | String | 否 | 账单币种  
mgnMode | String | 否 | 仓位类型  
`isolated`：逐仓  
`cross`：全仓  
ctType | String | 否 | 合约类型  
`linear`：正向合约  
`inverse`：反向合约  
仅`交割/永续`有效  
type | String | 否 | 账单类型  
枚举值请通过 [获取账单类型](/docs-v5/zh/#trading-account-rest-api-get-bill-types) 接口查询。  
subType | String | 否 | 账单子类型  
枚举值请通过 [获取账单类型](/docs-v5/zh/#trading-account-rest-api-get-bill-types) 接口查询。  
after | String | 否 | 请求此id之前（更旧的数据）的分页内容，传的值为对应接口的`billId`  
before | String | 否 | 请求此id之后（更新的数据）的分页内容，传的值为对应接口的`billId`  
begin | String | 否 | 筛选的开始时间戳 `ts`，Unix 时间戳为毫秒数格式，如 `1597026383085`  
end | String | 否 | 筛选的结束时间戳 `ts`，Unix 时间戳为毫秒数格式，如 `1597027383085`  
limit | String | 否 | 分页返回的结果集数量，最大为100，不填默认返回100条  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
            "bal": "8694.2179403378290202",
            "balChg": "0.0219338232210000",
            "billId": "623950854533513219",
            "ccy": "USDT",
            "clOrdId": "",
            "earnAmt": "",
            "earnApr": "",
            "execType": "T",
            "fee": "-0.000021955779",
            "fillFwdPx": "",
            "fillIdxPx": "27104.1",
            "fillMarkPx": "",
            "fillMarkVol": "",
            "fillPxUsd": "",
            "fillPxVol": "",
            "fillTime": "1695033476166",
            "from": "",
            "instId": "BTC-USDT",
            "instType": "SPOT",
            "interest": "0",
            "mgnMode": "isolated",
            "notes": "",
            "ordId": "623950854525124608",
            "pnl": "0",
            "posBal": "0",
            "posBalChg": "0",
            "px": "27105.9",
            "subType": "1",
            "sz": "0.021955779",
            "tag": "",
            "to": "",
            "tradeId": "586760148",
            "ts": "1695033476167",
            "type": "2"
        }]
    } 
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
instType | String | 产品类型  
billId | String | 账单ID  
type | String | 账单类型  
subType | String | 账单子类型  
ts | String | 余额更新完成的时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
balChg | String | 账户层面的余额变动数量  
posBalChg | String | 仓位层面的余额变动数量  
bal | String | 账户层面的余额数量  
posBal | String | 仓位层面的余额数量  
sz | String | 数量  
对于交割、永续以及期权，为成交或者持仓的数量，单位为张，总为正数。  
其他情况下，单位为账户余额币种（`ccy`）。  
px | String | 价格，与 subType 相关  

* 为成交价格时有
`1`：买入  
`2`：卖出  
`3`：开多  
`4`：开空  
`5`：平多  
`6`：平空  
`204`：大宗交易买  
`205`：大宗交易卖  
`206`：大宗交易开多  
`207`：大宗交易开空  
`208`：大宗交易平多  
`209`：大宗交易平空  
`114`：自动换币买入  
`115`：自动换币卖出  

* 为强平价格时有
`100`：强减平多 `101`：强减平空 `102`：强减买入 `103`：强减卖出 `104`：强平平多 `105`：强平平空 `106`：强平买入 `107`：强平卖出 `16`：强制还币 `17`：强制借币还息 `110`：强平换币转入 `111`：强平换币转出  

* 为交割价格时有
`112`：交割平多 `113`：交割平空  

* 为行权价格时有
`170`：到期行权 `171`：到期被行权 `172`：到期作废  

* 为标记价格时有
`173`：资金费支出 `174`：资金费收入  
ccy | String | 账户余额币种  
pnl | String | 收益  
fee | String | 手续费  
正数代表平台返佣 ，负数代表平台扣除  
[手续费规则](/cn/fees)  
earnAmt | String | 自动赚币数量  
仅适用于type 381  
earnApr | String | 自动赚币实际年利率   
仅适用于type 381  
mgnMode | String | 保证金模式  
`isolated`：逐仓  
`cross`：全仓  
`cash`：非保证金  
如果账单不是由交易产生的，该字段返回 ""  
instId | String | 产品ID，如 `BTC-USDT`  
ordId | String | 订单ID  
当type为`2`/`5`/`9`时，返回相应订单id  
无订单时，该字段返回 ""  
execType | String | 流动性方向  
`T`：taker  
`M`：maker  
from | String | 转出账户  
`6`：资金账户  
`18`：交易账户  
仅适用于`资金划转`，不是`资金划转`时，返回 ""  
to | String | 转入账户  
`6`：资金账户  
`18`：交易账户  
仅适用于`资金划转`，不是`资金划转`时，返回 ""  
notes | String | 备注  
interest | String | 利息  
tag | String | 订单标签  
fillTime | String | 最新成交时间  
tradeId | String | 最新成交ID  
clOrdId | String | 客户自定义订单ID  
fillIdxPx | String | 交易执行时的指数价格   
对于交叉现货币对，返回 baseCcy-USDT 的指数价格。 例 LTC-ETH，该字段返回 LTC-USDT 的指数价格。  
fillMarkPx | String | 成交时的标记价格，仅适用于 `交割`/`永续`/`期权`  
fillPxVol | String | 成交时的隐含波动率，仅适用于 `期权`，其他业务线返回空字符串""  
fillPxUsd | String | 成交时的期权价格，以USD为单位，仅适用于 `期权`，其他业务线返回空字符串""  
fillMarkVol | String | 成交时的标记波动率，仅适用于 `期权`，其他业务线返回空字符串""  
fillFwdPx | String | 成交时的远期价格，仅适用于 `期权`，其他业务线返回空字符串""  
**资金费支出(subType = 173)**  
可以用"pnl"查询资金费的支出总额 

### 申请账单流水（自 2021 年） 

申请自 2021 年 2 月 1 日以来的账单数据，不包括当前季度。

#### 限速：1次/10s

#### 限速规则：User ID

#### HTTP 请求

`POST /api/v5/account/bills-history-archive`

> 请求示例
    
    
    POST /api/v5/account/bills-history-archive
    body
    {
        "year":"2023",
        "quarter":"Q1"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
year | String | 是 | 4位数字的年份，如 `2023`  
quarter | String | 是 | 季度，有效值 `Q1` `Q2` `Q3` `Q4`  
type | String | 否 | 账单类型，支持多个，用英文逗号分隔，如 `1,2,3`；不填则返回所有类型。  
枚举值请通过 [获取账单类型](/docs-v5/zh/#trading-account-rest-api-get-bill-types) 接口查询。  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "result": "true",
                "ts": "1646892328000"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
result | String | 是否已经存在该区间的下载链接  
`true`：已存在，可以通过"获取账单流水（自 2021 年）"接口获取  
`false`：不存在，正在生成，请 2 个小时后查看下载链接  
ts | String | 服务端首次收到请求的时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
规则说明，仅适用于 2024 年 10 月 11 日之后新生成的文件： 1\. 以查询 2024 年第 3 季度的数据为例，实际查询的起止日期范围是 [2024-07-01, 2024-10-01)，包含开始日期，不包含结束日期。  
2\. 文件中的数据以 `billId` 倒序排列  平台需求量较多的情况下，生成数据所需要的时间会有所延长，如果超过 3 小时，请联系客服进行反馈。  仅适用于来自统一账户的数据 

### 获取账单流水（自 2021 年） 

获取自 2021 年 2 月 1 日以来的账单数据

#### 限速：10 次/2s

#### 限速规则：User ID

#### HTTP 请求

`GET /api/v5/account/bills-history-archive`

> 请求示例
    
    
    GET /api/v5/account/bills-history-archive?year=2023&quarter=Q4
    
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
year | String | 是 | 4位数字的年份，如 `2023`  
quarter | String | 是 | 季度，有效值 `Q1` `Q2` `Q3` `Q4`  
type | String | 否 | 账单类型，支持多个，用英文逗号分隔，如 `1,2,3`；不填则返回所有类型。  
枚举值请通过 [获取账单类型](/docs-v5/zh/#trading-account-rest-api-get-bill-types) 接口查询。  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "fileHref": "http://xxx",
                "state": "finished",
                "ts": "1646892328000"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
fileHref | String | 文件链接。  
每个链接的有效期为 5 个半小时，如果已经申请过同一季度的数据，则30天内无需再次申请。  
ts | String | 服务端首次收到请求的时间，Unix时间戳的毫秒数格式 ，如 `1597026383085`  
state | String | 下载链接状态  
`finished`：已生成  
`ongoing`：进行中  
`failed`：生成失败，请重新生成  
  
#### 解压后CSV里的字段说明

**参数名** | **类型** | **描述**  
---|---|---  
instType | String | 产品类型  
billId | String | 账单ID  
subType | String | 账单子类型  
ts | String | 余额更新完成的时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
balChg | String | 账户层面的余额变动数量  
posBalChg | String | 仓位层面的余额变动数量  
bal | String | 账户层面的余额数量  
posBal | String | 仓位层面的余额数量  
sz | String | 数量  
px | String | 价格，与 subType 相关  

* 为成交价格时有
`1`：买入  
`2`：卖出  
`3`：开多  
`4`：开空  
`5`：平多  
`6`：平空  
`204`：大宗交易买  
`205`：大宗交易卖  
`206`：大宗交易开多  
`207`：大宗交易开空  
`208`：大宗交易平多  
`209`：大宗交易平空  
`114`：自动换币买入  
`115`：自动换币卖出  

* 为强平价格时有
`100`：强减平多 `101`：强减平空 `102`：强减买入 `103`：强减卖出 `104`：强平平多 `105`：强平平空 `106`：强平买入 `107`：强平卖出 `16`：强制还币 `17`：强制借币还息 `110`：强平换币转入 `111`：强平换币转出  

* 为交割价格时有
`112`：交割平多 `113`：交割平空  

* 为行权价格时有
`170`：到期行权 `171`：到期被行权 `172`：到期作废  

* 为标记价格时有
`173`：资金费支出 `174`：资金费收入  
ccy | String | 账户余额币种  
pnl | String | 收益  
fee | String | 手续费  
正数代表平台返佣 ，负数代表平台扣除  
[手续费规则](/cn/fees)  
mgnMode | String | 保证金模式  
`isolated`：逐仓  
`cross`：全仓  
`cash`：非保证金  
如果账单不是由交易产生的，该字段返回 ""  
instId | String | 产品ID，如 `BTC-USDT`  
ordId | String | 订单ID  
无订单时，该字段返回 ""  
execType | String | 流动性方向  
`T`：taker  
`M`：maker  
interest | String | 利息  
tag | String | 订单标签  
fillTime | String | 最新成交时间  
tradeId | String | 最新成交ID  
clOrdId | String | 客户自定义订单ID  
fillIdxPx | String | 交易执行时的指数价格   
对于交叉现货币对，返回 baseCcy-USDT 的指数价格。 例 LTC-ETH，该字段返回 LTC-USDT 的指数价格。  
fillMarkPx | String | 成交时的标记价格，仅适用于 `交割`/`永续`/`期权`  
fillPxVol | String | 成交时的隐含波动率，仅适用于 `期权`，其他业务线返回空字符串""  
fillPxUsd | String | 成交时的期权价格，以USD为单位，仅适用于 `期权`，其他业务线返回空字符串""  
fillMarkVol | String | 成交时的标记波动率，仅适用于 `期权`，其他业务线返回空字符串""  
fillFwdPx | String | 成交时的远期价格，仅适用于 `期权`，其他业务线返回空字符串""  
  
### 获取账单类型 

获取所有账单类型，以及账单类型（type）与子类型（subType）的映射关系。

#### 限速：20次/2s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/account/subtypes`

> 请求示例
    
    
    GET /api/v5/account/subtypes
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
type | String | 否 | 账单类型，支持多个，用英文逗号分隔，如 `1,2,3`；不填则返回所有类型。  
  
> 返回示例
    
    
    {
        "code": "0",
        "data": [
            {
                "type": "1",
                "typeDesc": "Transfer",
                "subTypeDetails": [
                    {
                        "subType": "11",
                        "subTypeDesc": "Transfer in"
                    },
                    {
                        "subType": "12",
                        "subTypeDesc": "Transfer out"
                    }
                ]
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
type | String | 账单类型  
typeDesc | String | 账单类型描述，为 "" 代表该类型还未启用  
subTypeDetails | Array of objects | 子类型详情列表  
> subType | String | 子类型  
> subTypeDesc | String | 子类型描述，为 "" 代表该类型还未启用  
  
### 查看账户配置 

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
  
### 设置持仓模式 

`合约模式`和`跨币种保证金模式`：交割和永续合约支持开平仓模式和买卖模式。买卖模式只会有一个方向的仓位；开平仓模式可以分别持有多、空2个方向的仓位。  
`组合保证金模式`：交割和永续仅支持买卖模式

#### 限速：5次/2s

#### 限速规则：User ID

#### HTTP请求

`POST /api/v5/account/set-position-mode`

> 请求示例
    
    
    POST /api/v5/account/set-position-mode
    body 
    {
        "posMode":"long_short_mode"
    }
    
    
    
    
    import okx.Account as Account
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # 设置持仓模式
    result = accountAPI.set_position_mode(
        posMode="long_short_mode"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
posMode | String | 是 | 持仓方式  
`long_short_mode`：开平仓模式 `net_mode`：买卖模式  
仅适用`交割/永续`  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
            "posMode": "long_short_mode"
        }]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
posMode | String | 持仓方式  
  
### 设置杠杆倍数 

  
一个产品可以有如下10种杠杆倍数的设置场景：  
  

  1. 在`逐仓`交易模式下，设置`币币杠杆`的杠杆倍数（币对层面）；  

  2. `现货模式`账户已开通借币功能，在`全仓`交易模式下，设置`币币杠杆`的杠杆倍数（币种层面）；  

  3. `合约模式`账户在`全仓`交易模式下，设置`币币杠杆`的杠杆倍数（币对层面）；  

  4. `跨币种保证金模式`账户在`全仓`交易模式下，设置`币币杠杆`的杠杆倍数（币种层面）；  

  5. `组合保证金模式`账户在`全仓`交易模式下，设置`币币杠杆`的杠杆倍数（币种层面）；  

  6. 在`全仓`交易模式下，设置`交割`的杠杆倍数（指数层面）；  

  7. 在`逐仓`交易模式、`买卖`持仓模式下，设置`交割`的杠杆倍数（合约层面）；  

  8. 在`逐仓`交易模式、`开平仓`持仓模式下，设置`交割`的杠杆倍数（合约与持仓方向层面）；  

  9. 在`全仓`交易模式下，设置`永续`的杠杆倍数（合约层面）；  

  10. 在`逐仓`交易模式、`买卖`持仓模式下，设置`永续`的杠杆倍数（合约层面）；  

  11. 在`逐仓`交易模式、`开平仓`持仓模式下，设置`永续`的杠杆倍数（合约与持仓方向层面）；  

注意请求参数 posSide 仅在`交割/永续`的`开平仓`持仓模式下才需要填写（参见场景8和11）。  
请参阅右侧对应的每个案例的请求示例。  

#### 限速：20次/2s

#### 限速规则：User ID

#### HTTP请求

`POST /api/v5/account/set-leverage`

> 请求示例
    
    
    # 1.在`逐仓`交易模式下，设置`币币杠杆`的杠杆倍数（币对层面）
    POST /api/v5/account/set-leverage
    body
    {
        "instId":"BTC-USDT",
        "lever":"5",
        "mgnMode":"isolated"
    }
    
    # 2.`现货模式`账户已开通借币功能，在`全仓`交易模式下，设置`币币杠杆`的杠杆倍数（币种层面）
    POST /api/v5/account/set-leverage
    body
    {
        "ccy":"BTC",
        "lever":"5",
        "mgnMode":"cross"
    }
    
    
    # 3.`合约模式`账户在`全仓`交易模式下，设置`币币杠杆`的杠杆倍数（币对层面）
    POST /api/v5/account/set-leverage
    body
    {
        "instId":"BTC-USDT",
        "lever":"5",
        "mgnMode":"cross"
    }
    
    # 4.`跨币种保证金模式`账户在`全仓`交易模式下，设置`币币杠杆`的杠杆倍数（币种层面）
    POST /api/v5/account/set-leverage
    body
    {
        "ccy":"BTC",
        "lever":"5",
        "mgnMode":"cross"
    }
    
    # 5. `组合保证金模式`账户在`全仓`交易模式下，设置`币币杠杆`的杠杆倍数（币种层面）
    POST /api/v5/account/set-leverage
    body
    {
        "ccy":"BTC",
        "lever":"5",
        "mgnMode":"cross"
    }
    
    # 6.在`全仓`交易模式下，设置`交割`的杠杆倍数（指数层面）
    POST /api/v5/account/set-leverage
    body
    {
        "instId":"BTC-USDT-200802",
        "lever":"5",
        "mgnMode":"cross"
    }
    
    # 7.在`逐仓`交易模式、`买卖`持仓模式下，设置`交割`的杠杆倍数（合约层面）
    POST /api/v5/account/set-leverage
    body
    {
        "instId":"BTC-USDT-200802",
        "lever":"5",
        "mgnMode":"isolated"
    }
    
    # 8.在`逐仓`交易模式、`开平仓`持仓模式下，设置`交割`的杠杆倍数（合约与头寸层面）
    POST /api/v5/account/set-leverage
    body
    {
        "instId":"BTC-USDT-200802",
        "lever":"5",
        "posSide":"long",
        "mgnMode":"isolated"
    }
    
    # 9.在`全仓`交易模式下，设置`永续`的杠杆倍数（合约层面）
    POST /api/v5/account/set-leverage
    body
    {
        "instId":"BTC-USDT-SWAP",
        "lever":"5",
        "mgnMode":"cross"
    }
    
    # 10.在`逐仓`交易模式、`买卖`持仓模式下，设置`永续`的杠杆倍数（合约层面）
    POST /api/v5/account/set-leverage
    body
    {
        "instId":"BTC-USDT-SWAP",
        "lever":"5",
        "mgnMode":"isolated"
    }
    
    # 11.在`逐仓`交易模式、`开平仓`持仓模式下，设置`永续`的杠杆倍数（合约与头寸层面）
    POST /api/v5/account/set-leverage
    body
    {
        "instId":"BTC-USDT-SWAP",
        "lever":"5",
        "posSide":"long",
        "mgnMode":"isolated"
    }
    
    
    
    import okx.Account as Account
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # 在逐仓交易模式下，设置币币杠杆的杠杆倍数（币对层面）
    result = accountAPI.set_leverage(
        instId="BTC-USDT",
        lever="5",
        mgnMode="isolated"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instId | String | 可选 | 产品ID：币对、合约  
仅适用于`现货模式`/`跨币种保证金模式`/`组合保证金模式`的`全仓``交割``永续`，`合约模式`的`全仓``币币杠杆``交割``永续` 以及`逐仓`。  
且在适用场景下必填。  
ccy | String | 可选 | 保证金币种，用于设置开启自动借币模式下币种维度的杠杆。  
仅适用于`现货模式`/`跨币种保证金模式`/`组合保证金模式`的`全仓``币币杠杆`。  
且在适用场景下必填。  
lever | String | 是 | 杠杆倍数  
mgnMode | String | 是 | 保证金模式  
`isolated`：逐仓  
`cross`：全仓  
如果`ccy`有效传值，该参数值只能为`cross`。  
posSide | String | 可选 | 持仓方向  
`long`：开平仓模式开多  
`short`：开平仓模式开空  
仅适用于逐仓`交割`/`永续`  
在开平仓模式且保证金模式为逐仓条件下必填  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
            "lever": "30",
            "mgnMode": "isolated",
            "instId": "BTC-USDT-SWAP",
            "posSide": "long"
        }]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
lever | String | 杠杆倍数  
mgnMode | String | 保证金模式  
`isolated`：逐仓  
`cross`：全仓  
instId | String | 产品ID  
posSide | String | 持仓方向  
当希望在指数层面设置交割/永续的全仓杠杆倍数时，传入任意产品ID 和保证金模式（全仓）即可。  组合保证金账户下交割和永续的全仓不能调整杠杆倍数。 

### 获取最大可下单数量 

获取最大可下单数量，可对应下单时的 "sz" 字段

Portfolio Margin 账户下，衍生品的全仓模式不支持最大可买卖/开仓数量的计算。 

#### 限速：20次/2s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/account/max-size`

> 请求示例
    
    
    GET /api/v5/account/max-size?instId=BTC-USDT&tdMode=isolated
    
    
    
    
    import okx.Account as Account
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # 获取最大可买卖/开仓数量
    result = accountAPI.get_max_order_size(
        instId="BTC-USDT",
        tdMode="isolated"
    )
    print(result)
    

#### 请求参数

**参数名** | **类型** | **是否必须** | **描述**  
---|---|---|---  
instId | String | 是 | 产品ID，如 `BTC-USDT`  
支持同一业务线下的多产品ID查询（不超过5个），半角逗号分隔  
tdMode | String | 是 | 交易模式  
`cross`：全仓  
`isolated`：逐仓  
`cash`：非保证金  
`spot_isolated`：现货逐仓，仅适用于`合约模式`  
ccy | String | 可选 | 保证金币种，适用于`逐仓杠杆`及`合约模式`下的`全仓杠杆`订单  
px | String | 否 | 委托价格  
当不填委托价时，交割和永续会取当前限价计算，其他业务线会按当前最新成交价计算  
当指定多个产品ID查询时，忽略该参数，当未填写处理  
leverage | String | 否 | 开仓杠杆倍数  
默认为当前杠杆倍数  
仅适用于`币币杠杆/交割/永续`  
tradeQuoteCcy | String | 否 | 用于交易的计价币种。仅适用于`币币`。  
默认值为 `instId` 的计价币种，比如：对于 `BTC-USD`，默认取 `USD`。  
outcome | String | 可选 | 交易的市场结果方向。  
`yes`  
`no`  
仅适用于 `EVENTS`，选填，默认值为`yes`  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
            "ccy": "BTC",
            "instId": "BTC-USDT",
            "maxBuy": "0.0500695098559788",
            "maxSell": "64.4798671570072269"
        }]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
instId | String | 产品ID  
ccy | String | 保证金币种  
maxBuy | String | `币币/币币杠杆`：最大可买的交易币数量  
`合约模式`下的全仓杠杆订单，为交易币数量  
`交割`/`永续`/`期权`：最大可开多的合约张数  
maxSell | String | `币币/币币杠杆`：最大可卖的计价币数量  
`合约模式`下的全仓杠杆订单，为交易币数量  
`交割`/`永续`/`期权`：最大可开空的合约张数  
  
### 获取最大可用余额/保证金 

币币和逐仓时为可用余额，全仓时为可用保证金

#### 限速：20次/2s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/account/max-avail-size`

> 请求示例
    
    
    # 获取BTC-USDT全仓币币杠杆指定BTC作为保证金最大可用数量
    GET /api/v5/account/max-avail-size?instId=BTC-USDT&tdMode=cross&ccy=BTC
    
    # 获取BTC-USDT币币最大可用数量
    GET /api/v5/account/max-avail-size?instId=BTC-USDT&tdMode=cash
    
    
    
    
    import okx.Account as Account
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # 获取BTC-USDT币币最大可用数量
    result = accountAPI.get_max_avail_size(
        instId="BTC-USDT",
        tdMode="cash"
    )
    print(result)
    

#### 请求参数

**参数名** | **类型** | 是否必须 | 描述  
---|---|---|---  
instId | String | 是 | 产品ID，如 `BTC-USDT`  
支持多产品ID查询（不超过5个），半角逗号分隔  
tdMode | String | 是 | 交易模式  
`cross`：全仓  
`isolated`：逐仓  
`cash`：非保证金  
`spot_isolated`：现货逐仓，仅适用于`合约模式`  
ccy | String | 可选 | 保证金币种，适用于`逐仓杠杆`及`合约模式`下的`全仓杠杆`  
reduceOnly | Boolean | 否 | 是否为只减仓模式，仅适用于`币币杠杆`  
px | String | 否 | 平仓价格，默认为市价。  
仅适用于杠杆只减仓  
tradeQuoteCcy | String | 否 | 用于交易的计价币种。仅适用于`币币`。  
默认值为 `instId` 的计价币种，比如：对于 `BTC-USD`，默认取 `USD`。  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
            "instId": "BTC-USDT",
            "availBuy": "100",
            "availSell": "1"
        }]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
instId | String | 产品ID  
availBuy | String | 最大买入可用余额/保证金  
availSell | String | 最大卖出可用余额/保证金  
币币/币币杠杆时availBuy为计价货币，availSell为交易货币。  
全仓币币杠杆时，availBuy和availSell均为指定保证金的币种。 

### 调整保证金 

增加或者减少逐仓保证金。减少保证金可能会导致实际杠杆倍数发生变化。

#### 限速：20次/2s

#### 限速规则：User ID

#### HTTP请求

`POST /api/v5/account/position/margin-balance`

> 请求示例
    
    
    POST /api/v5/account/position/margin-balance 
    body
    {
        "instId":"BTC-USDT-SWAP",
        "posSide":"short",
        "type":"add",
        "amt":"1"
    }
    
    
    
    
    import okx.Account as Account
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # 调整保证金
    result = accountAPI.adjustment_margin(
        instId="BTC-USDT-SWAP",
        posSide="short",
        type= "add",
        amt="1"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instId | String | 是 | 产品ID  
posSide | String | 是 | 持仓方向，默认值是`net`  
`long`：开平仓模式开多  
`short`：开平仓模式开空  
`net`：买卖模式  
type | String | 是 | 增加/减少保证金  
`add`：增加   
`reduce`：减少  
amt | String | 是 | 增加或减少的保证金数量  
ccy | String | 可选 | 增加或减少的保证金的币种，  
适用于`逐仓杠杆`仓位  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "amt": "0.3",
                "ccy": "BTC",
                "instId": "BTC-USDT",
                "leverage": "",
                "posSide": "net",
                "type": "add"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
instId | String | 产品ID  
posSide | String | 持仓方向  
amt | String | 已增加/减少的保证金数量  
type | String | 增加/减少保证金  
leverage | String | 调整保证金后的实际杠杆倍数  
ccy | String | 增加或减少的保证金的币种  
自主划转模式  
初始划入逐仓仓位的保证金价值必须大于等于1万USDT,账户上会产生一个仓位。 

### 获取杠杆倍数 

#### 限速：20次/2s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/account/leverage-info`

> 请求示例
    
    
    GET /api/v5/account/leverage-info?instId=BTC-USDT-SWAP&mgnMode=cross
    
    
    
    
    import okx.Account as Account
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # 获取杠杆倍数
    result = accountAPI.get_leverage(
        instId="BTC-USDT-SWAP",
        mgnMode="cross"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instId | String | 可选 | 产品ID  
支持多个instId查询，半角逗号分隔。instId个数不超过20个。  
ccy | String | 可选 | 币种，用于币种维度的杠杆。  
仅适用于`现货模式`/`跨币种保证金模式`/`组合保证金模式`的全仓币币杠杆。  
支持多ccy查询，半角逗号分隔。ccy个数不超过20个。  
mgnMode | String | 是 | 保证金模式  
`isolated`：逐仓  
`cross`：全仓  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
            "ccy":"",
            "instId": "BTC-USDT-SWAP",
            "mgnMode": "cross",
            "posSide": "long",
            "lever": "10"
        },{
            "ccy":"",
            "instId": "BTC-USDT-SWAP",
            "mgnMode": "cross",
            "posSide": "short",
            "lever": "10"
        }]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
instId | String | 产品ID  
ccy | String | 币种，用于币种维度的杠杆。  
仅适用于`现货模式`/`跨币种保证金模式`/`组合保证金模式`的全仓币币杠杆。  
mgnMode | String | 保证金模式  
posSide | String | 持仓方向  
`long`：开平仓模式开多  
`short`：开平仓模式开空  
`net`：买卖模式  
开平仓模式下会返回两个方向的杠杆倍数  
lever | String | 杠杆倍数  
组合保证金账户下交割和永续的全仓不能获取杠杆倍数。 

### 获取杠杆倍数预估信息 

获取指定杠杆倍数下，相关的预估信息。

#### 限速：5次/2s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/account/adjust-leverage-info`

> 请求示例
    
    
    GET /api/v5/account/adjust-leverage-info?instType=MARGIN&mgnMode=isolated&lever=3&instId=BTC-USDT
    
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 是 | 产品类型  
`MARGIN`：币币杠杆  
`SWAP`：永续合约  
`FUTURES`：交割合约  
mgnMode | String | 是 | 保证金模式  
`isolated`：逐仓  
`cross`：全仓  
lever | String | 是 | 杠杆倍数  
instId | String | 可选 | 产品ID，如 `BTC-USDT`  
必填的场景有：交割永续，逐仓杠杆，以及`合约模式`下全仓杠杆。  
ccy | String | 可选 | 保证金币种，如 `BTC`  
逐仓杠杆及`合约模式`/`跨币种保证金模式`/`组合保证金模式`的全仓杠杆时必填。  
posSide | String | 否 | 持仓方向  
`net`: 默认值，代表买卖模式  
`long`: 开平模式下的多仓  
`short`：开平模式下的空仓  
适用于`交割`/`永续`。  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "estAvailQuoteTrans": "",
                "estAvailTrans": "1.1398040558348279",
                "estLiqPx": "",
                "estMaxAmt": "10.6095865868904898",
                "estMgn": "0.0701959441651721",
                "estQuoteMaxAmt": "176889.6871254563042714",
                "estQuoteMgn": "",
                "existOrd": false,
                "maxLever": "10",
                "minLever": "0.01"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
estAvailQuoteTrans | String | 对应杠杆倍数下，计价货币预估可转出的保证金数量  
全仓时，为交易账户最大可转出  
逐仓时，为逐仓仓位可减少的保证金。  
仅适用于`杠杆`  
estAvailTrans | String | 对应杠杆倍数下，预估可转出的保证金数量  
全仓时，为交易账户最大可转出  
逐仓时，为逐仓仓位可减少的保证金  
对于`杠杆`，单位为交易货币  
不适用于`交割`, `永续`的逐仓，调大杠杆的场景  
estLiqPx | String | 对应杠杆倍数下的预估强平价，仅在有仓位时有值  
estMgn | String | 对应杠杆倍数下，仓位预估所需的保证金数量  
对于杠杆仓位，为所需交易货币保证金  
对于交割或永续仓位，为仓位所需保证金  
estQuoteMgn | String | 对应杠杆倍数下，仓位预估所需的计价货币保证金数量  
estMaxAmt | String | 对于杠杆，为对应杠杆倍数下，交易货币预估最大可借  
对于交割和永续，为对应杠杆倍数下，预估的最大可开张数  
estQuoteMaxAmt | String | 对应杠杆倍数下，杠杆计价货币预估最大可借  
existOrd | Boolean | 当前是否存在挂单   
`true`：存在挂单  
`false`：不存在挂单  
maxLever | String | 最大杠杆倍数  
minLever | String | 最小杠杆倍数  
  
### 获取交易产品最大可借 

#### 限速：20 次/2s

#### 限速规则：User ID

#### HTTP 请求

`GET /api/v5/account/max-loan`

> 请求示例
    
    
    # 现货模式用户已经开通了借币情况下币对币种最大可借
    GET  /api/v5/account/max-loan?instId=BTC-USDT&mgnMode=cross
    
    # 现货模式用户已经开通了借币情况下币种最大可借
    GET  /api/v5/account/max-loan?ccy=USDT&mgnMode=cross
    
    # 合约模式逐仓账户获取币币杠杆最大可借
    GET  /api/v5/account/max-loan?instId=BTC-USDT&mgnMode=isolated
    
    # 合约模式全仓账户获取币币杠杆最大可借（指定保证金为BTC）
    GET  /api/v5/account/max-loan?instId=BTC-USDT&mgnMode=cross&mgnCcy=BTC
    
    # 跨币种全仓账户获取币币杠杠最大可借
    GET  /api/v5/account/max-loan?instId=BTC-USDT&mgnMode=cross
    
    
    
    
    import okx.Account as Account
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # 合约模式全仓账户获取币币杠杆最大可借（指定保证金为BTC）
    result = accountAPI.get_max_loan(
        instId="BTC-USDT",
        mgnMode="cross",
        mgnCcy="BTC"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
mgnMode | String | 是 | 仓位类型  
`isolated`：逐仓  
`cross`：全仓  
instId | String | 可选 | 产品 ID，如 `BTC-USDT`  
支持多产品ID查询（不超过5个），半角逗号分隔  
ccy | String | 可选 | 币种  
仅适用于`现货模式`下手动借币币种最大可借  
mgnCcy | String | 可选 | 保证金币种，如 `BTC`  
适用于`逐仓杠杆`及`合约模式`下的`全仓杠杆`  
tradeQuoteCcy | String | 否 | 用于交易的计价币种。仅适用于`币币`。  
默认值为 `instId` 的计价币种，比如：对于 `BTC-USD`，默认取 `USD`。  
  
> 返回结果
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
        {
          "instId": "BTC-USDT",
          "mgnMode": "isolated",
          "mgnCcy": "",
          "maxLoan": "0.1",
          "ccy": "BTC",
          "side": "sell"
        },
        {
          "instId": "BTC-USDT",
          "mgnMode": "isolated",
          "mgnCcy": "",
          "maxLoan": "0.2",
          "ccy": "USDT",
          "side": "buy"
        }
      ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
instId | String | 产品 ID  
mgnMode | String | 仓位类型  
mgnCcy | String | 保证金币种  
maxLoan | String | 最大可借  
ccy | String | 币种  
side | String | 订单方向  
  
### 获取当前账户交易手续费费率 

#### 限速：5次/2s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/account/trade-fee`

> 请求示例
    
    
    # 获取币币BTC-USDT交易手续费率  
    GET /api/v5/account/trade-fee?instType=SPOT&instId=BTC-USDT
    
    
    
    import okx.Account as Account
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # 获取当前账户交易手续费费率
    result = accountAPI.get_fee_rates(
        instType="SPOT",
        instId="BTC-USDT"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 是 | 产品类型  
`SPOT`：币币  
`MARGIN`：币币杠杆  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`OPTION`：期权  
`EVENTS`：事件合约  
instId | String | 否 | 产品ID，如 `BTC-USDT`  
仅适用于instType为`币币/币币杠杆`  
指定此参数将返回正确的适用手续费率（如：参与做市激励计划用户的做市商费率）。  
instFamily | String | 否 | 交易品种  
适用于`交割`/`永续`/`期权`，如 `BTC-USD`  
groupId | String | 否 | 交易产品手续费分组ID  
groupId 和 instId/instFamily 只能传入其一  
  
用户可以使用交易产品基础信息接口获取产品ID及其手续费分组ID的对应关系  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "category": "1",
                "delivery": "",
                "exercise": "",
                "feeGroup": [
                    {
                        "elpMaker": "-0.0008",
                        "groupId": "1",
                        "maker": "-0.0008",
                        "taker": "-0.001"
                    }
                ],
                "fiat": [],
                "instType": "SPOT",
                "level": "Lv1",
                "maker": "-0.0008",
                "makerU": "",
                "makerUSDC": "",
                "ruleType": "normal",
                "taker": "-0.001",
                "takerU": "",
                "takerUSDC": "",
                "ts": "1763979985847"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
level | String | 手续费等级  
feeGroup | Array of objects | 手续费分组   
适用于`SPOT/MARGIN/SWAP/FUTURES/OPTION/EVENTS`  
> taker | String | 吃单手续费  
`EVENTS` 吃单手续费公式的 K1 参数：`K1 × C × (P × (1-P))`（C = 合约张数，P = 价格）  
> maker | String | 挂单手续费  
`EVENTS` 挂单手续费公式的 K2 参数：`K2 × C × (P × (1-P))`（C = 合约张数，P = 价格）  
> groupId | String | 交易产品手续费分组ID  
  
**用户需要同时使用instType和groupId来确定一个交易产品的交易手续费分组；用户应该将此接口和[获取交易产品基础信息](/docs-v5/zh/#trading-account-rest-api-get-instruments)一起使用，以获取特定交易产品的手续费率**  
> elpMaker | String | ELP Maker 有效费率。若 ELP 不适用于该交易产品，则返回 `""`。  
delivery | String | 交割手续费率  
exercise | String | 行权手续费率  
instType | String | 产品类型  
ts | String | 数据返回时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
taker | String | ~~对于币币/杠杆，为 USDT 交易区的吃单手续费率；  
对于永续，交割和期权合约，为币本位合约费率~~（已废弃）  
maker | String | ~~对于币币/杠杆，为 USDT 交易区的挂单手续费率；  
对于永续，交割和期权合约，为币本位合约费率~~（已废弃）  
takerU | String | ~~USDT 合约吃单手续费率，仅适用于`交割/永续`~~（已废弃）  
makerU | String | ~~USDT 合约挂单手续费率，仅适用于`交割/永续`~~（已废弃）  
takerUSDC | String | ~~对于币币/杠杆，为 USDⓈ &Crypto 交易区的吃单手续费率；  
对于永续和交割合约，为 USDC 合约费率~~（已废弃）  
makerUSDC | String | ~~对于币币/杠杆，为 USDⓈ &Crypto 交易区的挂单手续费率；  
对于永续和交割合约，为 USDC 合约费率~~（已废弃）  
ruleType | String | ~~交易规则类型  
`normal`：普通交易  
`pre_market`：盘前交易~~（已废弃）  
category | String | ~~币种类别~~ （已废弃）  
fiat | Array of objects | ~~法币费率~~ （已废弃）  
> ccy | String | 法币币种  
> taker | String | 吃单手续费率  
> maker | String | 挂单手续费率  
settle | String | 结算手续费率，适用于持仓方向与事件合约结算结果一致的用户。持反向仓位的用户结算时不收取手续费。仅适用于 `EVENTS`  
备注：  
手续费率的值（如 maker/taker）：正数，代表是返佣的费率；负数，代表平台扣除的费率。  
例外：delivery 和 exercise 为正数，代表平台扣除的费率。  USDⓈ 代表除 USDT 之外的稳定币。  接口不会体现零手续费，零手续费交易对请参考<https://www.okx.com/zh-hans/fees> 对于参与做市激励计划的用户：指定 `instId`（适用于 `SPOT`/`MARGIN`）或 `instFamily`（适用于 `FUTURES`/`SWAP`/`OPTION`）将返回正确的适用手续费率；若不指定上述参数，则返回基础档位手续费率。 

### 获取计息记录 

获取过去一年的计息记录

#### 限速：5次/2s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/account/interest-accrued`

> 请求示例
    
    
    GET /api/v5/account/interest-accrued
    
    
    
    
    import okx.Account as Account
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # 获取计息记录
    result = accountAPI.get_interest_accrued()
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
type | String | 否 | 借币类型  
`2`：市场借币  
默认为`2`  
ccy | String | 否 | 借贷币种，如 `BTC`  
仅适用于`市场借币`  
仅适用于`币币杠杆`  
instId | String | 否 | 产品ID，如 `BTC-USDT`  
仅适用于`市场借币`  
mgnMode | String | 否 | 保证金模式  
`cross`：全仓  
`isolated`：逐仓  
仅适用于`市场借币`  
after | String | 否 | 请求此时间戳之前（更旧的数据）的分页内容，Unix时间戳的毫秒数格式，如 `1597026383085`  
before | String | 否 | 请求此时间戳之后（更新的数据）的分页内容，Unix时间戳的毫秒数格式，如 `1597026383085`  
limit | String | 否 | 分页返回的结果集数量，最大为100，不填默认返回100条  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "ccy": "USDT",
                "instId": "",
                "interest": "0.0003960833333334",
                "interestRate": "0.0000040833333333",
                "liab": "97",
                "totalLiab": "",
                "interestFreeLiab": "",
                "mgnMode": "",
                "ts": "1637312400000",
                "type": "1"
            },
            {
                "ccy": "USDT",
                "instId": "",
                "interest": "0.0004083333333334",
                "interestRate": "0.0000040833333333",
                "liab": "100",
                "totalLiab": "",
                "interestFreeLiab": "",
                "mgnMode": "",
                "ts": "1637049600000",
                "type": "1"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
type | String | 类型  
`2`：市场借币  
ccy | String | 借贷币种，如 `BTC`  
instId | String | 产品ID，如 `BTC-USDT`  
仅适用于`市场借币`  
mgnMode | String | 保证金模式  
`cross`：全仓  
`isolated`：逐仓  
interest | String | 利息累计  
interestRate | String | 借款计息利率(小时)  
liab | String | 计息负债  
totalLiab | String | 当前账户总负债量  
interestFreeLiab | String | 当前账户免息负债量  
ts | String | 计息时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
  
### 获取用户当前市场借币利率 

#### 限速：5次/2s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/account/interest-rate`

> 请求示例
    
    
    GET /api/v5/account/interest-rate
    
    
    
    
    import okx.Account as Account
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # 获取用户当前市场借币利率
    result = accountAPI.get_interest_rate()
    print(result)
    

#### 请求参数

**参数名** | **类型** | 是否必须 | 描述  
---|---|---|---  
ccy | String | 否 | 币种  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "ccy":"BTC",
                "interestRate":"0.0001"
            },
            {
                "ccy":"LTC",
                "interestRate":"0.0003"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
interestRate | String | 每小时借币利率  
ccy | String | 币种  
  
### 设置手续费计价方式 

设置手续费计价方式。

手續費計價方式選擇對現貨生效。 

#### 限速：5次/2s

#### 限速规则：User ID

#### HTTP 请求

`POST /api/v5/account/set-fee-type`

> 请求示例
    
    
    POST /api/v5/account/set-fee-type 
    body
    {
        "feeType": "0"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
feeType | String | 是 | 手续费计价方式  
`0`: 按交易获得的币种收取手续费（默认）  
`1`: 始终按交易对的计价币种收取手续费（仅适用于现货）  
  
> 返回示例
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "feeType": "0"
            }
        ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
feeType | String | 手续费计价方式  
`0`: 按交易获得的币种收取手续费  
`1`: 始终按交易对的计价币种收取手续费  
  
### 期权greeks的PA/BS切换 

设置greeks的展示方式。

#### 限速：5次/2s

#### 限速规则：User ID

#### HTTP请求

`POST /api/v5/account/set-greeks`

> 请求示例
    
    
    POST /api/v5/account/set-greeks 
    body
    {
        "greeksType":"PA"
    }
    
    
    
    
    import okx.Account as Account
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # 期权greeks的PA/BS切换
    result = accountAPI.set_greeks(greeksType="PA")
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
greeksType | String | 是 | 希腊字母展示方式  
`PA`：币本位，`BS`：美元本位  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
            "greeksType": "PA"
        }]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
greeksType | String | 当前希腊字母展示方式  
  
### 逐仓交易设置 

可以通过该接口设置币币杠杆和交割、永续的逐仓仓位保证金的划转模式

#### 限速：5次/2s

#### 限速规则：User ID

#### HTTP请求

`POST /api/v5/account/set-isolated-mode`

> 请求示例
    
    
    POST /api/v5/account/set-isolated-mode
    body
    {
        "isoMode":"automatic",
        "type":"MARGIN"
    }
    
    
    
    import okx.Account as Account
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # 逐仓交易设置
    result = accountAPI.set_isolated_mode(
        isoMode="automatic",
        type="MARGIN"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
isoMode | String | 是 | 逐仓保证金划转模式  
`auto_transfers_ccy`：新版开仓自动划转，支持交易货币及计价货币作为保证金，仅适用于`币币杠杆`  
`automatic`：开仓自动划转  
type | String | 是 | 业务线类型  
`MARGIN`：币币杠杆  
`CONTRACTS`：合约  
当前账户内有持仓和挂单时，不能调整逐仓保证金划转模式。 

> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "isoMode": "automatic"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
isoMode | String | 逐仓保证金划转模式  
`auto_transfers_ccy`：新版开仓自动划转  
`automatic`：开仓自动划转  
衍生品  
开仓划转：在开仓和平仓时自动占用和释放保证金  杠杆  
开仓划转：在开仓和平仓时自动借币和还币 

### 查看账户最大可转余额 

当指定币种时会返回该币种的交易账户到资金账户的最大可划转数量，不指定币种会返回所有拥有的币种资产可划转数量。

#### 限速：20次/2s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/account/max-withdrawal`

> 请求示例
    
    
    GET /api/v5/account/max-withdrawal
    
    
    
    
    import okx.Account as Account
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # 查看账户最大可转余额
    result = accountAPI.get_max_withdrawal()
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 否 | 币种，如 `BTC`  
支持多币种查询（不超过20个），币种之间半角逗号分隔  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
                "ccy": "BTC",
                "maxWd": "124",
                "maxWdEx": "125",
                "spotOffsetMaxWd": "",
                "spotOffsetMaxWdEx": ""
            },
            {
                "ccy": "ETH",
                "maxWd": "10",
                "maxWdEx": "12",
                "spotOffsetMaxWd": "",
                "spotOffsetMaxWdEx": ""
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
ccy | String | 币种  
maxWd | String | 最大可划转数量（不包含 `跨币种保证金模式`/`组合保证金模式` 借币金额）  
maxWdEx | String | 最大可划转数量（包含 `跨币种保证金模式`/`组合保证金模式` 借币金额）  
spotOffsetMaxWd | String | 现货对冲不支持借币最大可转数量  
仅适用于`组合保证金模式`  
spotOffsetMaxWdEx | String | 现货对冲支持借币的最大可转数量  
仅适用于`组合保证金模式`  
  
### 查看账户特定风险状态 

仅适用于PM账户

#### 限速：10次/2s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/account/risk-state`

> 请求示例
    
    
    GET /api/v5/account/risk-state
    
    
    
    
    import okx.Account as Account
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # 查看账户持仓风险
    result = accountAPI.get_account_position_risk()
    print(result)
    

> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "atRisk": false,
                "atRiskIdx": [],
                "atRiskMgn": [],
                "ts": "1635745078794"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
atRisk | Boolean | 自动借币模式下的账户风险状态  
true： 当前账户为特定风险状态  
false： 当前不是特定风险状态  
atRiskIdx | Array of strings | 衍生品的risk unit列表  
atRiskMgn | Array of strings | 杠杆的risk unit列表  
ts | String | 接口数据返回时间 ，Unix时间戳的毫秒数格式，如 `1597026383085`  
当账户进入特定风险状态后，仅可以委托降低账户风险方向的IOC类型订单. 

### 获取借币利率与限额 

#### 限速：5次/2s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/account/interest-limits`

> 请求示例
    
    
    GET /api/v5/account/interest-limits?ccy=BTC
    
    
    
    
    import okx.Account as Account
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # 获取借币利率与限额
    result = accountAPI.get_interest_limits(
        ccy="BTC"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
type | String | 否 | 借币类型  
`2`：市场借币  
默认为`2`  
ccy | String | 否 | 借贷币种，如 `BTC`  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "debt": "0.85893159114900247077000000000000",
                "interest": "0.00000000000000000000000000000000",
                "loanAlloc": "",
                "nextDiscountTime": "1729490400000",
                "nextInterestTime": "1729490400000",
                "records": [
                    {
                        "availLoan": "",
                        "avgRate": "",
                        "ccy": "BTC",
                        "interest": "0",
                        "loanQuota": "175.00000000",
                        "posLoan": "",
                        "rate": "0.0000276",
                        "surplusLmt": "175.00000000",
                        "surplusLmtDetails": {},
                        "usedLmt": "0.00000000",
                        "usedLoan": "",
                        "interestFreeLiab": "",
                        "potentialBorrowingAmt": ""
                    }
                ]
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
debt | String | 当前负债，单位为`USD`  
interest | String | 当前记息，单位为`USD`  
仅适用于`市场借币`  
nextDiscountTime | String | 下次扣息时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
nextInterestTime | String | 下次计息时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
loanAlloc | String | ~~当前交易账户尊享借币可用额度的比率（百分比）  
1\. 范围为[0, 100]. 精度为 0.01% (2位小数)  
2\. 0 代表母账户没有为子账户分配；  
3\. "" 代表母子账户共享~~  
已废弃  
records | Array of objects | 各币种详细信息  
> ccy | String | 借贷币种，如 `BTC`  
> rate | String | 当前日借币利率  
> loanQuota | String | 母账户维度借币限额  
如果已配置可用额度，该字段代表当前交易账户的借币限额  
> usedLmt | String | 当前账户已借额度  
如果已配置可用额度，该字段代表当前交易账户的已借额度  
> interest | String | 已计未扣利息  
仅适用于`市场借币`  
> interestFreeLiab | String | 当前账户免息负债  
> potentialBorrowingAmt | String | 当前账户潜在借币量  
> surplusLmt | String | 母子账户剩余可借  
如果已配置可用额度，该字段代表当前交易账户的剩余可借  
> surplusLmtDetails | Object | ~~母子账户剩余可借额度详情，母子账户剩余可借额度的值取该数组中的最小值，可以用来判断是什么原因导致可借额度不足  
仅适用于`尊享借币`~~  
已废弃  
>> allAcctRemainingQuota | String | 母子账户剩余额度  
>> curAcctRemainingQuota | String | 当前账户剩余额度  
仅适用于为子账户分配限额的场景  
>> platRemainingQuota | String | 平台剩余额度，当平台剩余额度大于`curAcctRemainingQuota`或者`allAcctRemainingQuota`时，会显示大于某个值，如">1000"  
> posLoan | String | ~~当前账户负债占用（锁定额度内）  
仅适用于`尊享借币`~~  
已废弃  
> availLoan | String | ~~当前账户剩余可用（锁定额度内）  
仅适用于`尊享借币`~~  
已废弃  
> usedLoan | String | ~~当前账户已借额度  
仅适用于`尊享借币`~~  
已废弃  
> avgRate | String | ~~已借币种平均每小时利率，仅适用于`尊享借币`~~  
已废弃  
  
### 手动借/还币 

仅适用于`现货模式`已开通借币的情况。

#### 限速：1次/3s

#### 限速规则：Master Account User ID

#### HTTP请求

`POST /api/v5/account/spot-manual-borrow-repay`

> 请求示例
    
    
    POST /api/v5/account/spot-manual-borrow-repay 
    body
    {
        "ccy": "USDT",
        "side": "borrow",
        "amt": "100"
    }
    
    
    
    import okx.Account as Account
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘:1
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    result = accountAPI.spot_manual_borrow_repay(ccy="USDT", side="borrow", amt= "1")
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 是 | 币种，如 `BTC`  
side | String | 是 | 方向  
`borrow`：借币  
`repay`：还币  
amt | String | 是 | 数量  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "ccy":"USDT",
                "side":"borrow",
                "amt":"100"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ccy | String | 币种，如 `BTC`  
side | String | 方向  
`borrow`：借币  
`repay`：还币  
amt | String | 实际数量  
  
### 设置自动还币 

仅适用于`现货模式`已开通借币的情况。

#### 限速：5次/2s

#### 限速规则：User ID

#### HTTP请求

`POST /api/v5/account/set-auto-repay`

> 请求示例
    
    
    POST /api/v5/account/set-auto-repay
    body
    {
        "autoRepay": true
    }
    
    
    
    import okx.Account as Account
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘:1
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    result = accountAPI.set_auto_repay(autoRepay=True)
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
autoRepay | Boolean | 是 | 是否支持`现货模式`下自动还币  
`true`：支持  
`false`：不支持  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "autoRepay": true
            }
        ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
autoRepay | Boolean | 是否支持`现货模式`下自动还币  
`true`：支持  
`false`：不支持  
  
### 获取借/还币历史 

获取`现货模式`下的借/还币历史。

#### 限速：5次/2s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/account/spot-borrow-repay-history`

> 请求示例
    
    
    GET /api/v5/account/spot-borrow-repay-history
    
    
    
    import okx.Account as Account
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘:1
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    result = accountAPI.spot_borrow_repay_history(ccy="USDT", type="auto_borrow")
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 否 | 币种，如 `BTC`  
type | String | 否 | 事件类型  
`auto_borrow`：自动借币  
`auto_repay`：自动还币  
`manual_borrow`：手动借币  
`manual_repay`：手动还币  
after | String | 否 | 请求发生时间`ts`之前（包含）的分页内容，Unix时间戳的毫秒数格式，如 `1597026383085`  
before | String | 否 | 请求发生时间`ts`之后（包含）的分页内容，Unix时间戳的毫秒数格式，如 `1597026383085`  
limit | String | 否 | 返回结果的数量，最大为100，默认100条  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "accBorrowed": "0",
                "amt": "6764.802661157592",
                "ccy": "USDT",
                "ts": "1725330976644",
                "type": "auto_repay"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ccy | String | 币种，如 `BTC`  
type | String | 事件类型  
`auto_borrow`：自动借币  
`auto_repay`：自动还币  
`manual_borrow`：手动借币  
`manual_repay`：手动还币  
amt | String | 数量  
accBorrowed | String | 累计借币数量  
ts | String | 事件发生时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
  
### 仓位创建器 

计算用户的模拟头寸或当前头寸的投资组合保证金信息，一次请求最多可添加200个虚拟仓位和200个虚拟虚拟资产

#### 限速：2次/2s

#### 限速规则：User ID

#### HTTP请求

`POST /api/v5/account/position-builder`

> 请求示例
    
    
    # 真实与虚拟的仓位与资产一起计算
    POST /api/v5/account/position-builder
    body
    {
        "inclRealPosAndEq": false,
        "simPos":[
             {
                "pos":"-10",
                "instId":"BTC-USDT-SWAP",
                "avgPx":"100000"
             },
             {
                "pos":"10",
                "instId":"LTC-USDT-SWAP",
                "avgPx":"8000"
             }
        ],
        "simAsset":[
            {
                "ccy": "USDT",
                "amt": "100"
            }
        ],
        "greeksType":"CASH"
    }
    
    
    # 只计算已有真实仓位
    POST /api/v5/account/position-builder
    body
    {
       "inclRealPosAndEq": true
    }
    
    
    # 只计算虚拟仓位
    POST /api/v5/account/position-builder
    body
    {
        "acctLv": "4",
        "inclRealPosAndEq": false,
        "simPos":[
            {
                "pos":"10",
                "instId":"BTC-USDT-SWAP",
                "avgPx":"100000"
            },
            {
                "pos":"10",
                "instId":"LTC-USDT-SWAP",
                "avgPx":"8000"
            }
        ]
    }
    
    # 切换到跨币种
    POST /api/v5/account/position-builder
    body
    {
        "acctLv": "3",
        "lever":"10",
        "simPos":[
            {
                "pos":"10",
                "instId":"BTC-USDT-SWAP",
                "avgPx":"100000",
                "lever":"5"
            },
            {
                "pos":"10",
                "instId":"LTC-USDT-SWAP",
                "avgPx":"8000"
            }
        ]
    }
    
    
    
    import okx.Account as Account
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘: 0, 模拟盘: 1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    result = accountAPI.position_builder(
        inclRealPosAndEq=True,
        simPos=[
            {
                "pos": "10",
                "instId": "BTC-USDT-SWAP",
                "avgPx":"100000"
            },
            {
                "pos": "10",
                "instId": "LTC-USDT-SWAP",
                "avgPx":"100000"
            }
        ]
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
acctLv | String | 否 | 切换至账户模式  
`3`：跨币种保证金模式  
`4`：组合保证金模式  
inclRealPosAndEq | Boolean | 否 | 是否代入已有仓位和资产  
默认为`true`  
lever | String | 否 | 跨币种下整体的全仓合约杠杆数量，默认为`1`。  
如果超过允许的杠杆倍数，按照最大的杠杆设置。  
适用于`跨币种保证金模式`  
simPos | Array of objects | 否 | 模拟仓位列表  
> instId | String | 是 | 交易产品ID，如 `BTC-USDT-SWAP`  
适用于 `SWAP`/`FUTURES`/`OPTION`  
> pos | String | 是 | 持仓量  
> avgPx | String | 是 | 平均开仓价格  
> lever | String | 否 | 杠杆  
仅适用于在跨币种保证金模式下指定交易产品的杠杆。如果用户不传，则选择默认杠杆为`1`。  
simAsset | Array of objects | 否 | 模拟资产  
当`inclRealPosAndEq`为`true`，只考虑真实资产，会忽略虚拟资产  
> ccy | String | 是 | 币种，如 `BTC`  
> amt | String | 是 | 币种数量  
可以为负，代表减少币种资产  
greeksType | String | 否 | 希腊值类型  
`BS`：BS模型  
`PA`：币本位  
`CASH`：美元现金等价  
默认是`BS`  
idxVol | String | 否 | 价格变动百分比。小数形式，范围 -0.99 ~ 1，以 0.01 为增量。  
默认值为 0  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "acctLever": "-0.1364949794742562",
                "assets": [
                    {
                        "availEq": "0",
                        "borrowImr": "0",
                        "borrowMmr": "",
                        "ccy": "BTC",
                        "spotInUse": "0"
                    },
                    {
                        "availEq": "0",
                        "borrowImr": "0",
                        "borrowMmr": "",
                        "ccy": "LTC",
                        "spotInUse": "0"
                    },
                    {
                        "availEq": "0",
                        "borrowImr": "0",
                        "borrowMmr": "",
                        "ccy": "USDC",
                        "spotInUse": "0"
                    },
                    {
                        "availEq": "-78589.37",
                        "borrowImr": "7855.32188898",
                        "borrowMmr": "",
                        "ccy": "USDT",
                        "spotInUse": "0"
                    }
                ],
                "borrowMmr": "1571.064377796",
                "derivMmr": "1375.4837063088003",
                "eq": "-78553.21888979999",
                "marginRatio": "-25.95365779811705",
                "positions": [],
                "riskUnitData": [
                    {
                        "delta": "-9704.903689800001",
                        "gamma": "0",
                        "imrBf": "",
                        "imr": "1538.9669514070802",
                        "mmrBf": "",
                        "mmr": "1183.8207318516002",
                        "mr1": "1164.4109244719994",
                        "mr1FinalResult": {
                            "pnl": "-1164.4109244719994",
                            "spotShock": "0.12",
                            "volShock": "up"
                        },
                        "mr1Scenarios": {
                            "volSame": {
                                "0": "0",
                                "0.08": "-776.2739496480004",
                                "-0.08": "776.2739496480004",
                                "0.04": "-388.1369748240002",
                                "0.12": "-1164.4109244719994",
                                "-0.12": "1164.4109244719994",
                                "-0.04": "388.1369748240002"
                            },
                            "volShockDown": {
                                "0": "0",
                                "0.08": "-776.2739496480004",
                                "-0.08": "776.2739496480004",
                                "0.04": "-388.1369748240002",
                                "0.12": "-1164.4109244719994",
                                "-0.12": "1164.4109244719994",
                                "-0.04": "388.1369748240002"
                            },
                            "volShockUp": {
                                "0": "0",
                                "0.08": "-776.2739496480004",
                                "-0.08": "776.2739496480004",
                                "0.04": "-388.1369748240002",
                                "0.12": "-1164.4109244719994",
                                "-0.12": "1164.4109244719994",
                                "-0.04": "388.1369748240002"
                            }
                        },
                        "mr2": "0",
                        "mr3": "0",
                        "mr4": "19.4098073796",
                        "mr5": "0",
                        "mr6": "1164.4109244720003",
                        "mr6FinalResult": {
                            "pnl": "-2328.8218489440005",
                            "spotShock": "0.24"
                        },
                        "mr7": "43.67206660410001",
                        "mr8": "1571.064377796",
                        "mr9": "0",
                        "portfolios": [
                            {
                                "amt": "-10",
                                "avgPx": "100000",
                                "delta": "-9704.903689800001",
                                "floatPnl": "290.6300000000003",
                                "gamma": "0",
                                "instId": "BTC-USDT-SWAP",
                                "instType": "SWAP",
                                "isRealPos": false,
                                "markPxBf": "",
                                "markPx": "97093.7",
                                "notionalUsd": "9703.22",
                                "posSide": "net",
                                "theta": "0",
                                "vega": "0"
                            }
                        ],
                        "riskUnit": "BTC",
                        "theta": "0",
                        "upl": "290.49631020000027",
                        "vega": "0"
                    },
                    {
                        "delta": "1019.5308",
                        "gamma": "0",
                        "imrBf": "",
                        "imr": "249.16186679436",
                        "mmrBf": "",
                        "mmr": "191.6629744572",
                        "mr1": "183.50672805719995",
                        "mr1FinalResult": {
                            "pnl": "-183.50672805719995",
                            "spotShock": "-0.18",
                            "volShock": "up"
                        },
                        "mr1Scenarios": {
                            "volSame": {
                                "0": "0",
                                "-0.06": "-61.168909352399936",
                                "0.06": "61.168909352399936",
                                "-0.18": "-183.50672805719995",
                                "0.18": "183.50672805719995",
                                "0.12": "122.33781870480001",
                                "-0.12": "-122.33781870480001"
                            },
                            "volShockDown": {
                                "0": "0",
                                "-0.06": "-61.168909352399936",
                                "0.06": "61.168909352399936",
                                "-0.18": "-183.50672805719995",
                                "0.18": "183.50672805719995",
                                "0.12": "122.33781870480001",
                                "-0.12": "-122.33781870480001"
                            },
                            "volShockUp": {
                                "0": "0",
                                "-0.06": "-61.168909352399936",
                                "0.06": "61.168909352399936",
                                "-0.18": "-183.50672805719995",
                                "0.18": "183.50672805719995",
                                "0.12": "122.33781870480001",
                                "-0.12": "-122.33781870480001"
                            }
                        },
                        "mr2": "0",
                        "mr3": "0",
                        "mr4": "8.1562464",
                        "mr5": "0",
                        "mr6": "183.5067280572",
                        "mr6FinalResult": {
                            "pnl": "-367.0134561144",
                            "spotShock": "-0.36"
                        },
                        "mr7": "7.1367156",
                        "mr8": "1571.064377796",
                        "mr9": "0",
                        "portfolios": [
                            {
                                "amt": "10",
                                "avgPx": "8000",
                                "delta": "1019.5308",
                                "floatPnl": "-78980",
                                "gamma": "0",
                                "instId": "LTC-USDT-SWAP",
                                "instType": "SWAP",
                                "isRealPos": false,
                                "markPxBf": "",
                                "markPx": "102",
                                "notionalUsd": "1018.9",
                                "posSide": "net",
                                "theta": "0",
                                "vega": "0"
                            }
                        ],
                        "riskUnit": "LTC",
                        "theta": "0",
                        "upl": "-78943.6692",
                        "vega": "0"
                    }
                ],
                "totalImr": "9643.45070718144",
                "totalMmr": "2946.5480841048",
                "ts": "1736936801642",
                "upl": "-78653.1728898"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
eq | String | 账户有效保证金  
totalMmr | String | 账户维持保证金，单位为`USD`  
totalImr | String | 账户初始保证金占用，单位为`USD`  
borrowMmr | String | 账户借币维持保证金，单位为`USD`  
derivMmr | String | 账户衍生品维持保证金，单位为`USD`  
marginRatio | String | 账户全仓维持保证金率  
upl | String | 账户浮动盈亏  
acctLever | String | 账户全仓杠杆  
ts | String | 账户信息的更新时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
assets | Array of objects | 资产信息  
> ccy | String | 币种，如 `BTC`  
> availEq | String | 币种权益  
> spotInUse | String | 现货对冲占用  
> borrowMmr | String | ~~借币维持保证金，单位为`USD`~~字段已废弃  
> borrowImr | String | 借币初始保证金，单位为`USD`  
riskUnitData | Array of objects | Risk unit 相关信息  
适用于`组合保证金模式`  
> riskUnit | String | 账户内的 risk unit，如 `BTC`  
> mmrBf | String | 价格变动前 Risk unit 维度的维持保证金，单位为`USD`  
若用户没有传入idxVol，则返回 ""  
> mmr | String | Risk unit 维度的维持保证金，单位为`USD`  
> imrBf | String | 价格变动前 Risk unit 维度的初始保证金，单位为`USD`  
若用户没有传入idxVol，则返回 ""  
> imr | String | Risk unit 维度的初始保证金，单位为`USD`  
> upl | String | Risk unit 维度的浮动盈亏，单位为`USD`  
> mr1 | String | 现货和波动率变化风险 (适用于所有衍生品，以及在现货对冲模式下的现货)  
> mr2 | String | 时间价值风险 (仅适用于期权)  
> mr3 | String | 波动率跨期风险 (仅适用于期权)  
> mr4 | String | 基差风险 (适用于所有衍生品)  
> mr5 | String | 利率风险 (仅适用于期权)  
> mr6 | String | 极端市场波动风险 (适用于所有衍生品，以及在现货对冲模式下的现货)  
> mr7 | String | 减仓成本 (适用于所有衍生品)  
> mr8 | String | 借币维持保证金/初始保证金  
> mr9 | String | USDT-USDC-USD 对冲风险  
> mr1Scenarios | Object of objects | MR1 的压力测试场景分析  
>> volShockDown | Object | 波动率向下时，不同价格波动比率下的压力测试盈亏  
值为 {`change`: `value`, ...}   
`change`：价格波动比率（百分比），如 `0.01` 代表 `1%`  
`value`：压力测试下的盈亏，单位为`USD`  
如 {"-0.15":"-2333.23", ...}  
>> volSame | Object | 波动率不变时，不同价格波动比率下的压力测试盈亏  
值为 {`change`: `value`, ...}   
`change`：价格波动比率（百分比），如 `0.01` 代表 `1%`  
`value`：压力测试下的盈亏，单位为`USD`  
如 {"-0.15":"-2333.23", ...}  
>> volShockUp | Object | 波动率向上时，不同价格波动比率下的压力测试盈亏  
值为 {`change`: `value`, ...}   
`change`：价格波动比率（百分比），如 `0.01` 代表 `1%`  
`value`：压力测试下的盈亏，单位为`USD`  
如 {"-0.15":"-2333.23", ...}  
> mr1FinalResult | Object | MR1 最大亏损场景  
>> pnl | String | MR1 最大亏损压测盈亏，单位为 `USD`  
>> spotShock | String | MR1 最大亏损的价格波动（百分比），如 `0.01` 代表 `1%`  
>> volShock | String | MR1 最大亏损波动率趋势  
`down`：波动率向下  
`unchange`：波动率不变  
`up`：波动率向上  
> mr6FinalResult | Object | MR6 最大亏损场景  
>> pnl | String | MR6 最大亏损压测盈亏，单位为 `USD`  
>> spotShock | String | MR6 最大亏损的价格波动（百分比），如 `0.01` 代表 `1%`  
> delta | String | (Risk unit 维度) 合约价格随标的价格变动的比例  
当标的价格变动 x 时，合约价格变动约为此 Delta 数值乘以 x  
> gamma | String | (Risk unit 维度) 标的价格对 Delta 值的影响程度  
当标的价格变动 x% 时，期权 Delta 值的变动约为此 Gamma 数值乘以 x%  
> theta | String | (Risk unit 维度) 距离到期日时间缩短 1 天，该合约价格的变化量  
> vega | String | (Risk unit 维度) 标的波动率增加 1%，该合约价格的变化量  
> portfolios | Array of objects | 资产组合  
>> instId | String | 产品ID，如 `BTC-USDT-SWAP`  
>> instType | String | 产品类型  
`SPOT`：现货  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`OPTION`：期权  
>> amt | String | `instType`为`SPOT`，代表现货对冲占用  
`instType`为`SWAP`/`FUTURES`/`OPTION`，代表仓位数量。  
>> posSide | String | 持仓方向  
`long`：开平仓模式开多  
`short`：开平仓模式开空  
`net`：买卖模式  
>> avgPx | String | 平均开仓价格  
>> markPxBf | String | 价格变动前标记价格  
若用户没有传入idxVol，则返回 ""  
>> markPx | String | 标记价格  
>> floatPnl | String | 浮动盈亏  
>> notionalUsd | String | 美金价值  
>> delta | String | `instType`为`SPOT`，代表资产数量。  
`instType`为`SWAP`/`FUTURES`/`OPTION`，代表(产品层面) 合约价格随标的价格变动的比例。  
>> gamma | String | (产品层面) 标的价格对 Delta 值的影响程度  
`instType`为`SPOT`，返回""  
>> theta | String | (产品层面) 距离到期日时间缩短 1 天，该合约价格的变化量  
`instType`为`SPOT`，返回""  
>> vega | String | (产品层面) 标的波动率增加 1%，该合约价格的变化量  
`instType`为`SPOT`，返回""  
>> isRealPos | Boolean | 是否为真实仓位  
`instType`为`SWAP`/`FUTURES`/`OPTION`，该字段有效，其他都默认返回`false`  
positions | Array of objects | 仓位信息  
适用于`跨币种保证金模式`  
> instId | String | 产品ID，如 `BTC-USDT-SWAP`  
> instType | String | 产品类型  
`SPOT`：现货  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`OPTION`：期权  
> amt | String | `instType`为`SPOT`，代表现货对冲占用  
`instType`为`SWAP`/`FUTURES`/`OPTION`，代表仓位数量。  
> posSide | String | 持仓方向  
`long`：开平仓模式开多  
`short`：开平仓模式开空  
`net`：买卖模式  
> avgPx | String | 平均开仓价格  
> markPxBf | String | 价格变动前标记价格  
若用户没有传入idxVol，则返回 ""  
> markPx | String | 标记价格  
> floatPnl | String | 浮动盈亏  
> imrBf | String | 价格变动前初始保证金  
> imr | String | 初始保证金，仅适用于全仓  
> mgnRatio | String | 维持保证金率  
> lever | String | 杠杆倍数  
> notionalUsd | String | 美金价值  
> isRealPos | Boolean | 是否为真实仓位  
`instType`为`SWAP`/`FUTURES`/`OPTION`，该字段有效，其他都默认返回`false`  
  
### 仓位创建器趋势图 

#### 限速：1次/5s

#### 限速规则：User ID

#### HTTP请求

`POST /api/v5/account/position-builder-graph`

> 请求示例
    
    
    {
       "inclRealPosAndEq":false,
       "simPos":[
          {
             "pos":"-10",
             "instId":"BTC-USDT-SWAP",
             "avgPx":"100000"
          },
          {
             "pos":"10",
             "instId":"LTC-USDT-SWAP",
             "avgPx":"8000"
          }
       ],
       "simAsset":[
          {
             "ccy":"USDT",
             "amt":"100"
          }
       ],
       "greeksType":"CASH",
       "type":"mmr",
       "mmrConfig":{
          "acctLv":"3",
          "lever":"1"
       }
    }
    

#### 请求参数

**参数名** | **类型** | **是否必须** | **描述**  
---|---|---|---  
inclRealPosAndEq | Boolean | 否 | 是否代入已有仓位和资产  
默认为`true`  
simPos | Array of objects | 否 | 模拟仓位列表  
> instId | String | 是 | 交易产品ID，如 `BTC-USDT-SWAP`  
适用于 `SWAP`/`FUTURES`/`OPTION`  
> pos | String | 是 | 持仓量  
> avgPx | String | 是 | 平均开仓价格  
> lever | String | 否 | 杠杆  
仅适用于在跨币种保证金模式下指定交易产品的杠杆。如果用户不传，则选择默认杠杆为`1`。  
simAsset | Array of objects | 否 | 模拟资产  
当`inclRealPosAndEq`为`true`，只考虑真实资产，会忽略虚拟资产  
> ccy | String | 是 | 币种，如 `BTC`  
> amt | String | 是 | 币种数量  
可以为负，代表减少币种资产  
type | String | 是 | 趋势图类型  
`mmr`  
mmrConfig | Object | 是 | MMR配置  
> acctLv | String | 否 | 切换至账户模式  
`3`：跨币种保证金模式  
`4`：组合保证金模式  
> lever | String | 否 | 跨币种下整体的全仓合约杠杆数量，默认为`1`。  
如果超过允许的杠杆倍数，按照最大的杠杆设置。  
适用于`跨币种保证金模式`  
  
> 返回示例
    
    
    {
        "code": "0",
        "data": [
             {
                "type": "mmr",
                "mmrData": [
                   ......
                   {
                         "mmr": "1415.0254039225917",
                         "mmrRatio": "-47.45603627655477",
                         "shockFactor": "-0.94"
                   },
                   {
                         "mmr": "1417.732491243024",
                         "mmrRatio": "-47.436684685735386",
                         "shockFactor": "-0.93"
                   }
                   ......
                ]
             }
        ],
        "msg": ""
    }
    
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
type | String | 趋势图类型  
`mmr`  
mmrData | Array | MMR数据  
以shockFactor升序返回  
> shockFactor | String | 价格变动比例，数据范围 -1 到 1.  
> mmr | String | 维持保证金  
> mmrRatio | String | 维持保证金率  
  
### 设置现货对冲占用 

用户自定义现货对冲占用数量，不代表实际现货对冲占用数量。仅适用于组合保证金模式。

#### 限速：10次/2s

#### 限速规则：User ID

#### HTTP请求

`POST /api/v5/account/set-riskOffset-amt`

> 请求示例
    
    
    # 设置现货对冲占用
    POST /api/v5/account/set-riskOffset-amt
    {
       "ccy": "BTC",
       "clSpotInUseAmt": "0.5"
    }
    
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 是 | 币种，如 `BTC`  
clSpotInUseAmt | String | 是 | 用户自定义现货对冲数量  
  
> 返回示例
    
    
    {
       "code": "0",
       "msg": "",
       "data": [
          {
             "ccy": "BTC",
             "clSpotInUseAmt": "0.5"
          }
       ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ccy | String | 币种，如 `BTC`  
clSpotInUseAmt | String | 用户自定义现货对冲数量  
  
### 查看账户Greeks 

获取账户资产的greeks信息。

#### 限速：10次/2s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/account/greeks`

> 请求示例
    
    
    # 获取账户中所有资产的greeks
    GET /api/v5/account/greeks
    
    # 获取账户中BTC的greeks
    GET /api/v5/account/greeks?ccy=BTC
    
    
    
    
    import okx.Account as Account
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # 查看账户Greeks
    result = accountAPI.get_greeks()
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 否 | 币种，如 `BTC`  
  
> 返回结果
    
    
    {
        "code":"0",
        "data":[
            {            
               "thetaBS": "",
               "thetaPA":"",
               "deltaBS":"",
               "deltaPA":"",
               "gammaBS":"",
               "gammaPA":"",
               "vegaBS":"",    
               "vegaPA":"",
               "ccy":"BTC",
               "ts":"1620282889345"
            }
        ],
        "msg":""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
deltaBS | String | 美金本位账户资产delta  
deltaPA | String | 币本位账户资产delta  
gammaBS | String | 美金本位账户资产gamma，仅适用于`期权`  
gammaPA | String | 币本位账户资产gamma，仅适用于`期权`  
thetaBS | String | 美金本位账户资产theta，仅适用于`期权`  
thetaPA | String | 币本位账户资产theta，仅适用于`期权`  
vegaBS | String | 美金本位账户资产vega，仅适用于`期权`  
vegaPA | String | 币本位账户资产vega，仅适用于`期权`  
ccy | String | 币种  
ts | String | 获取greeks的时间，Unix时间戳的毫秒数格式，如 1597026383085  
  
### 获取组合保证金模式仓位限制 

仅支持获取组合保证金模式下，交割、永续和期权的全仓仓位限制。

#### 限速：10次/2s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/account/position-tiers`

> 请求示例
    
    
    # 查看BTC-USDT在组合保证金模式下的全仓限制
    GET /api/v5/account/position-tiers?instType=SWAP&uly=BTC-USDT
    
    
    
    
    import okx.Account as Account
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # 获取组合保证金模式仓位限制
    result = accountAPI.get_account_position_tiers(
        instType="SWAP",
        uly="BTC-USDT"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 是 | 产品类型  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`OPTION`：期权  
  
instFamily | String | 是 | 交易品种，如 `BTC-USDT`，支持多个查询（不超过5个），`instFamily`之间半角逗号分隔  
  
> 返回结果
    
    
    {
      "code": "0",
      "data": [
        {
          "instFamily": "BTC-USD",
          "maxSz": "10000",
          "posType": "",
          "uly": "BTC-USDT"
        }
      ],
      "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
uly | String | 标的指数  
适用于`交割`/`永续`/`期权`  
instFamily | String | 交易品种  
适用于`交割`/`永续`/`期权`  
maxSz | String | 最大持仓量  
posType | String | 限仓类型，仅适用于组合保证金模式下的期权全仓。  
`1`：所有合约挂单 + 持仓张数，`2`：所有合约总挂单张数，`3`：所有合约总挂单单数，`4`：同方向合约挂单 + 持仓张数，`5`：单一合约总挂单单数，`6`：单一合约挂单 + 持仓张数，`7`：单笔挂单张数"  
  
### 开通期权交易 

#### 限速：5次/2s

#### 限速规则：User ID

#### HTTP请求

`POST /api/v5/account/activate-option`

> 请求示例
    
    
    POST /api/v5/account/activate-option
    
    

#### 请求参数

无

> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
            "ts": "1600000000000"
        }]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ts | String | 开通时间  
  
### 设置自动借币 

仅适用于跨币种保证金模式和组合保证金模式

#### 限速：5次/2s

#### 限速规则：User ID

#### HTTP请求

`POST /api/v5/account/set-auto-loan`

> 请求示例
    
    
    POST /api/v5/account/set-auto-loan
    body
    {
        "autoLoan":true,
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
autoLoan | Boolean | 否 | 是否自动借币   
有效值为`true`, `false`  
默认为 `true`  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
            "autoLoan": true
        }]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
autoLoan | Boolean | 是否自动借币  
  
### 预设置账户模式切换 

预设置账户模式切换的必要信息，若由`组合保证金模式`切换到`合约模式`/`跨币种保证金模式`，且存在全仓交割、永续仓位，则必须预设置lever，令所有仓位具有相同杠杆倍数。

若用户未按照规定进行设置，在预检查或设置账户模式时将接收到报错或提示信息。

#### 限速：5次/2s

#### 限速规则：User ID

#### HTTP请求

`POST /api/v5/account/account-level-switch-preset`

> 请求示例
    
    
    # 1. 合约模式 -> 跨币种
    POST /api/v5/account/account-level-switch-preset
    body
    {
        "acctLv": "3"
    }
    
    # 2. 跨币种 -> 合约模式
    POST /api/v5/account/account-level-switch-preset
    body
    {
        "acctLv": "2"
    }
    
    # 3. 组合保证金 -> 合约模式/跨币种，且有全仓合约仓位，则必须传入lever
    POST /api/v5/account/account-level-switch-preset
    body
    {
        "acctLv": "2",
        "lever": "10"
    }
    
    # 4. 组合保证金 -> 合约模式/跨币种，没有全仓合约仓位，则不需传入lever，不进行校验
    POST /api/v5/account/account-level-switch-preset
    body
    {
        "acctLv": "3"
    }
    
    

#### 请求参数

**参数名** | **类型** | **是否必须** | **描述**  
---|---|---|---  
acctLv | String | 是 | 账户模式  
`2`: 合约模式  
`3`: 跨币种保证金模式  
`4`: 组合保证金模式  
lever | String | 可选 | 在`组合保证金模式`向`合约模式/跨币种保证金模式`切换，且用户有全仓仓位时，必须传入  
riskOffsetType | String | 可选 | ~~风险对冲模式  
`1`：现货对冲(USDT)  
`2`：现货对冲(币)  
`3`：衍生品对冲（未开启现货对冲）  
`4`：现货对冲(USDC)  
适用于`合约模式/跨币种保证金模式`向`组合保证金模式`切换~~（已弃用）  
  
> 返回结果 1. 合约模式 -> 跨币种
    
    
    {
        "acctLv": "3",
        "curAcctLv": "2",
        "lever": "",
        "riskOffsetType": ""
    }
    

> 返回结果 2. 跨币种 -> 合约模式
    
    
    {
        "acctLv": "2",
        "curAcctLv": "3",
        "lever": "",
        "riskOffsetType": ""
    }
    

> 返回结果 3. 组合保证金 -> 合约模式/跨币种
    
    
    {
        "acctLv": "2",
        "curAcctLv": "4",
        "lever": "10",
        "riskOffsetType": ""
    }
    

> 返回结果 4. 组合保证金 -> 合约模式/跨币种，没有全仓合约仓位，则不需传入lever，不进行校验
    
    
    {
        "acctLv": "3",
        "curAcctLv": "4",
        "lever": "",
        "riskOffsetType": ""
    }
    
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
curAcctLv | String | 当前账户类型  
acctLv | String | 切换后的账户类型  
lever | String | 用户预设置的全仓合约仓位杠杆倍数  
riskOffsetType | String | ~~用户预设置的风险对冲模式~~ （已弃用）  
  
lever：`保证金模式`向`合约模式`/`跨币种保证金模式`切换，且用户有全仓合约仓位，则必须传入此参数，不传则报错50014。传此参数，允许设置的最大值为各个合约的仓位大小对应合约模式/跨币种账户模式下最大杠杆倍数的最小值。例如，用户在PM模式下，有三个全仓仓位，当前仓位大小对应目标账户模式下最大杠杆倍数分别为20x/50x/100x，那么用户能够设置的最大杠杆倍数为20x。 

### 预检查账户模式切换 

获取账户模式切换预检查相关信息

#### 限速：5次/2s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/account/set-account-switch-precheck`

> 请求示例
    
    
    GET /api/v5/account/set-account-switch-precheck?acctLv=3
    
    

#### 请求参数

**参数名** | **类型** | **是否必须** | **描述**  
---|---|---|---  
acctLv | String | 是 | 账户模式  
`1`: 现货模式  
`2`: 合约模式  
`3`: 跨币种保证金模式  
`4`: 组合保证金模式  
  
> 返回结果: 合约模式->跨币种，需要现在网页或移动端完成答题
    
    
    {
        "code": "51070",
        "data": [],
        "msg": "您当前尚未达到升级至该账户模式的要求，请先在官方网站或APP完成账户模式的升级。"
    }
    

> 返回结果: 合约模式->跨币种，有不兼容信息。sCode 1
    
    
    {
        "code": "0",
        "data": [
            {
                "acctLv": "3",
                "curAcctLv": "1",
                "mgnAft": null,
                "mgnBf": null,
                "posList": [],
                "posTierCheck": [],
                "riskOffsetType": "",
                "sCode": "1",
                "unmatchedInfoCheck": [
                    {
                        "posList": [],
                        "totalAsset": "",
                        "type": "repay_borrowings"
                    }
                ]
            }
        ],
        "msg": ""
    }
    

> 返回结果: 组合保证金->跨币种，未进行杠杆设置，展示用户全部合约全仓仓位。sCode 3
    
    
    {
        "code": "0",
        "data": [
            {
                "acctLv": "3",
                "curAcctLv": "4",
                "mgnAft": null,
                "mgnBf": null,
                "posList": [
                    {
                        "lever": "50",
                        "posId": "2005456500916518912"
                    },
                    {
                        "lever": "10",
                        "posId": "2005456108363218944"
                    },
                    {
                        "lever": "100",
                        "posId": "2005456332909477888"
                    },
                    {
                        "lever": "1",
                        "posId": "2005456415990251520"
                    }
                ],
                "posTierCheck": [],
                "riskOffsetType": "",
                "sCode": "3",
                "unmatchedInfoCheck": []
            }
        ],
        "msg": ""
    }
    

> 返回结果: 组合保证金->跨币种，已进行杠杆设置，将全部杠杆倍数设置为50，通过梯度档位及保证金校验。sCode 0
    
    
    {
        "code": "0",
        "data": [
            {
                "acctLv": "3",
                "curAcctLv": "4",
                "mgnAft": {
                    "acctAvailEq": "106002.2061970689",
                    "details": [],
                    "mgnRatio": "148.1652396878421"
                },
                "mgnBf": {
                    "acctAvailEq": "77308.89735228613",
                    "details": [],
                    "mgnRatio": "4.460069474634038"
                },
                "posList": [
                    {
                        "lever": "50",
                        "posId": "2005456500916518912"
                    },
                    {
                        "lever": "50",
                        "posId": "2005456108363218944"
                    },
                    {
                        "lever": "50",
                        "posId": "2005456332909477888"
                    },
                    {
                        "lever": "50",
                        "posId": "2005456415990251520"
                    }
                ],
                "posTierCheck": [],
                "riskOffsetType": "",
                "sCode": "0",
                "unmatchedInfoCheck": []
            }
        ],
        "msg": ""
    }
    
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
sCode | String | 校验码  
`0`：通过所有验证  
`1`：有不兼容信息  
`3`：未进行杠杆设置  
`4`：梯度档位或保证金校验未通过  
curAcctLv | String | 当前账户模式  
`1`: 现货模式  
`2`: 合约模式  
`3`: 跨币种保证金模式  
`4`: 组合保证金模式  
所有情况下均返回  
acctLv | String | 新账户模式  
`1`: 现货模式  
`2`: 合约模式  
`3`: 跨币种保证金模式  
`4`: 组合保证金模式  
所有情况下均返回  
riskOffsetType | String | ~~风险对冲模式  
`1`：现货对冲(USDT)  
`2`：现货对冲(币)  
`3`：衍生品对冲  
`4`：现货对冲(USDC)  
acctLv为`4`时返回，其余情况下返回""  
若用户有设置，则为用户的设置值；若没有设置，则为默认值~~（已弃用）  
unmatchedInfoCheck | Array of objects | 包含不匹配信息对象的列表  
仅在sCode为`1`，有不兼容信息时返回，其他情况返回[]  
>> type | String | 不匹配信息类型  
`asset_validation`：资产校验  
`pending_orders`：撮合挂单  
`pending_algos`：策略挂单，冰山、时间加权、定投等  
`isolated_margin`：杠杆逐仓一键借币及自主划转  
`isolated_contract`：合约逐仓自主划转  
`contract_long_short`：合约开平模式  
`cross_margin`：杠杆全仓开仓划转  
`cross_option_buyer`：期权全仓买方  
`isolated_option`：期权逐仓 （仅适用于简单账户）  
`growth_fund`：体验金仓位  
`all_positions`：所有仓位  
`spot_lead_copy_only_simple_single`：带单和自定义跟单员只能使用现货或合约模式  
`stop_spot_custom`：停止现货自定义跟单  
`stop_futures_custom`：停止合约自定义跟单  
`lead_portfolio`：身为带单员，您不能切换到组合保证金账户模式  
`futures_smart_sync`：您存在合约智能跟单，无法切换到现货模式  
`repay_borrowings`：存在借币  
`compliance_restriction`：合规，无法使用保证金交易相关服务  
`compliance_kyc2`：合规，无法使用保证金交易相关服务，如果您不是该地区居民，请进行KYC2身份认证  
>> totalAsset | String | 总资产  
仅在type为`asset_validation`时返回，其他情况都为""  
>> posList | Array of strings | 不匹配仓位列表，返回持仓ID  
在type为仓位相关枚举值时返回，其他情况都为[]  
posList | Array of objects | 合约全仓仓位列表  
适用于curAcctLv为`4`，acctLv为`2/3`，且用户具有全仓合约仓位的情况  
在sCode为`0/3/4`的情况下返回  
> posId | String | 持仓ID  
> lever | String | 切换后的全仓仓位杠杆倍数  
posTierCheck | Array of objects | 未满足梯度档位校验全仓仓位的列表  
仅在sCode为`4`时返回  
> instFamily | String | 交易品种  
> instType | String | 产品类型  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`OPTION`：期权  
> pos | String | 持仓量  
> lever | String | 杠杆倍数  
> maxSz | String | 若acctLv为`2/3`，目标账户模式为合约、跨币种，则为当前杠杆倍数下的最大持仓张数；若acctLv为`4`，目标账户模式为组合保证金，则为PM全仓最大持仓量上限  
mgnBf | Object | 切换账户模式前的保证金相关信息  
在sCode为`0/4`时返回，其他时候为null  
> acctAvailEq | String | 美金层面可用保证金  
在curAcctLv为`3/4`时返回，其他情况返回""  
> mgnRatio | String | 美金层面维持保证金率  
在curAcctLv为`3/4`时返回，其他情况返回""  
> details | Array of objects | 各币种资产详细信息  
仅在curAcctLv为`2`时返回，其他情况返回[]  
>> ccy | String | 币种  
>> availEq | String | 币种维度可用保证金  
>> mgnRatio | String | 币种维度全仓维持保证金率  
mgnAft | Object | 切换账户模式后的保证金相关信息  
在sCode为`0/4`时返回，其他时候为null  
> acctAvailEq | String | 美金层面可用保证金  
在acctLv为`3/4`时返回，其他情况返回""  
> mgnRatio | String | 美金层面维持保证金率  
在acctLv为`3/4`时返回，其他情况返回""  
> details | Array of objects | 各币种资产详细信息  
仅在acctLv为`2`时返回，其他情况返回""  
>> ccy | String | 币种  
>> availEq | String | 币种维度可用保证金  
>> mgnRatio | String | 币种维度全仓维持保证金率  
  
### 设置账户模式 

账户模式的首次设置，需要在网页或手机app上进行。若用户计划在持有仓位的情况下切换账户模式，应该先调用预设置接口进行必要的预设置，再调用预检查接口获取不匹配信息、保证金校验等相关信息，最后调用账户模式切换接口进行账户模式切换。

#### 限速：5次/2s

#### 限速规则：User ID

#### HTTP请求

`POST /api/v5/account/set-account-level`

> 请求示例
    
    
    POST /api/v5/account/set-account-level
    body
    {
        "acctLv":"1"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
acctLv | String | 是 | 账户模式  
`1`: 现货模式  
`2`: 合约模式   
`3`: 跨币种保证金模式   
`4`: 组合保证金模式  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data" :[
              {
                "acctLv":"1"
              }
        ]  
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
acctLv | String | 账户模式  
  
### 设置质押币种 

#### 限速：5次/2s

#### 限速规则：User ID

#### HTTP请求

`POST /api/v5/account/set-collateral-assets`

> 请求示例
    
    
    # 设置全部币种为可质押资产
    POST /api/v5/account/set-collateral-assets
    body
    {
        "type":"all",
        "collateralEnabled":true
    }
    
    
    # 设置自定义不可质押资产
    POST /api/v5/account/set-collateral-assets
    body
    {
        "type":"custom",
        "ccyList":["BTC","ETH"],
        "collateralEnabled":false
    }
    
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
type | String | 是 | 设置币种类型  
`all`：全部  
`custom`：自定义  
collateralEnabled | Boolean | 是 | 是否设置为质押币种  
`true`：设置为质押币  
`false`：取消质押币的设置  
ccyList | Array of strings | 可选 | 币种列表，如 ["BTC","ETH"]  
当type=`custom`,该字段必传。  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data" :[
          {
            "type":"all",
            "ccyList":["BTC","ETH"],
            "collateralEnabled":false
          }
        ]  
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
type | String | 设置币种类型  
`all`：全部  
`custom`：自定义  
collateralEnabled | Boolean | 是否已设置为质押币种  
`true`：设置为质押币  
`false`：取消质押币的设置  
ccyList | Array of strings | 币种列表，如 ["BTC","ETH"]  
  
### 查看质押币种 

#### 限速：5次/2s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/account/collateral-assets`

> 请求示例
    
    
    GET /api/v5/account/collateral-assets
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 否 | 币种  
支持多币种查询（不超过20个），币种之间半角逗号分隔，如 "BTC,ETH"  
collateralEnabled | Boolean | 否 | 是否为质押币  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data" :[
              {
                "ccy":"BTC",
                "collateralEnabled": true
              },
              {
                "ccy":"ETH",
                "collateralEnabled": false
              }
        ]  
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
ccy | String | 币种，如 `BTC`  
collateralEnabled | Boolean | 是否为质押币  
  
### 重置 MMP 状态 

一旦 MMP 被触发，可以使用该接口解冻。  
仅适用于组合保证金账户模式下的期权订单，且有 MMP 权限。

在模拟盘环境中，MMP 配置可能会被系统定期重置。若您的模拟盘 MMP 状态被意外重置，请联系您的客户经理或发邮件至 institutional@okx.com。 

#### 限速：5次/2s

#### 限速规则：User ID

#### HTTP请求

`POST /api/v5/account/mmp-reset`

> 请求示例
    
    
    POST /api/v5/account/mmp-reset
    body
    {
        "instType":"OPTION",
        "instFamily":"BTC-USD"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 否 | 交易产品类型  
`OPTION`:期权  
默认为期权  
instFamily | String | 是 | 交易品种  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "result":true
            }
        ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
result | Boolean | 重置结果  
`true`:将做市商保护状态重置为了 inactive 状态  
false：重置失败  
  
### 设置 MMP 

可以使用该接口进行 MMP 的配置。  
仅适用于组合保证金账户模式下的期权订单，且有 MMP 权限。

  
什么是MMP?  
做市商保护(MMP)机制保护做市商在一定时间内成交过多。当做市商保护触发时，即做市商在一定时间内(`timeInterval`)成交超过某阈值(`qtyLimit`)，系统会自动撤销所有MMP挂单(`mmp`和`mmp_and_post_only`挂单)，拒绝任何新的MMP订单直到某个时间(MMP最近一次触发时间+`frozenInterval`)或做市商主动重置。  
  
如何申请MMP?  
请发邮件至 institutional@okx.com 或者联系您的客户经理进行申请。  MMP 按交易品种（`instFamily`）单独配置。为某一交易品种启用 MMP **不会** 自动延伸至其他品种。例如，为 `BTC-USD` 配置 MMP 并不涵盖 `ETH-USD` 或 `SOL-USD`，需分别调用此接口为每个品种单独设置。 

#### 限速：2次/10s

#### 限速规则：User ID

#### HTTP请求

`POST /api/v5/account/mmp-config`

> 请求示例
    
    
    POST /api/v5/account/mmp-config
    body
    {
        "instFamily":"BTC-USD",
        "timeInterval":"5000",
        "frozenInterval":"2000",
        "qtyLimit": "100"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instFamily | String | 是 | 交易品种  
timeInterval | String | 是 | 时间窗口 (毫秒)。  
"0" 代表停用 MMP  
frozenInterval | String | 是 | 冻结时间长度 (毫秒)。   
"0" 代表一直冻结，直到调用 "重置 MMP 状态" 接口解冻  
qtyLimit | String | 是 | 成交数量的上限  
需大于 0  
  
> 返回结果
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
        {
            "frozenInterval":"2000",
            "instFamily":"BTC-USD",
            "qtyLimit": "100",
            "timeInterval":"5000"
        }
      ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
instFamily | String | 交易品种  
timeInterval | String | 时间窗口 (毫秒)  
frozenInterval | String | 冻结时间长度 (毫秒)  
qtyLimit | String | 成交张数的上限  
  
### 查看 MMP 配置 

可以使用该接口获取 MMP 的配置信息。  
仅适用于组合保证金账户模式下的期权订单，且有 MMP 权限。

#### 限速：5次/2s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/account/mmp-config`

> 请求示例
    
    
    GET /api/v5/account/mmp-config?instFamily=BTC-USD
    
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instFamily | String | 否 | 交易品种  
  
> 返回结果
    
    
    {
      "code": "0",
      "data": [
        {
          "frozenInterval": "2000",
          "instFamily": "ETH-USD",
          "mmpFrozen": true,
          "mmpFrozenUntil": "1000",
          "qtyLimit": "10",
          "timeInterval": "5000"
        }
      ],
      "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
instFamily | String | 交易品种  
mmpFrozen | Boolean | 是否 MMP 被触发. `true` 或者 `false`  
mmpFrozenUntil | String | 如果配置了frozenInterval且mmpFrozen = true，则为不再触发MMP时的时间窗口（单位为ms），否则为“”  
timeInterval | String | 时间窗口 (毫秒)  
frozenInterval | String | 冻结时间长度 (毫秒)。   
如果为"0"，代表一直冻结，直到调用 "重置 MMP 状态" 接口解冻，且`mmpFrozenUntil`为 ""。  
qtyLimit | String | 成交张数的上限  
  
### 移仓 

仅适用于交易等级大于等于VIP6的用户，仅能通过母账户的API Key调用。用户可通过[我的手续费](https://www.okx.com/balance/fee)页面的手续费详情表格查看自己的交易等级。  

支持同一母账户下的子账户间仓位划转。每个源账户每24小时最多可触发15次移仓请求，目标账户接受移仓不受次数限制。参考下文“注意事项”部分，以获取详情。

#### 限速：1次/1s

#### 限速规则：母账户 User ID

#### HTTP请求

`POST /api/v5/account/move-positions`

> 请求示例
    
    
    {
       "fromAcct":"0",
       "toAcct":"test",
       "legs":[
          {
             "from":{
                "posId":"2065471111340792832",
                "side":"sell",
                "sz":"1"
             },
             "to":{
                "posSide":"net",
                "tdMode":"cross"
             }
          },
          {
             "from":{
                "posId":"2063111180412153856",
                "side":"sell",
                "sz":"1"
             },
             "to":{
                "posSide":"net",
                "tdMode":"cross"
             }
          }
       ],
       "clientId":"test"
    }
    
    

#### 请求参数

**参数名** | **类型** | **是否必须** | **描述**  
---|---|---|---  
fromAcct | String | 是 | 源账户名，使用"0"代表母账户  
toAcct | String | 是 | 目标账户名，使用"0"代表母账户  
legs | Array of Objects | 是 | 移仓仓位列表，每次最多支持30个仓位  
> from | Object | 是 | 源账户仓位  
>> posId | String | 是 | 源账户持仓ID  
>> sz | String | 是 | 合约数量  
>> side | String | 是 | 源账户的交易方向  
`buy`  
`sell`  
> to | Object | 是 | 目标账户移仓配置  
>> tdMode | String | 否 | 目标账户的交易模式  
`cross`：全仓  
`isolated`：逐仓  
若未提供，tdMode会采用以下默认值：  
在合约模式或跨币种保证金模式下买入期权：`isolated`  
其他情况：`cross`  
>> posSide | String | 否 | 持仓方向  
`long`：开平仓模式开多  
`short`：开平仓模式开空  
`net`：买卖模式  
当目标账户处于买卖模式时，用户不需传入该参数，若传入，唯一有效值为`net`；当处于开平仓模式时，有效值为`long`，`short`，若未指定，目标账户将总是开仓  
>> ccy | String | 否 | 目标账户保证金币种  
仅适用于`合约模式`下的全仓杠杆仓位  
clientId | String | 是 | 客户自定义ID，字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度要在1-32位之间  
  
> 返回示例
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "clientId": "test",
                "blockTdId": "2065832911119076864",
                "state": "filled",
                "ts": "1734069018526",
                "fromAcct": "0",
                "toAcct": "test",
                "legs": [
                    {
                        "from": {
                            "posId": "2065471111340792832",
                            "instId": "BTC-USD-SWAP",
                            "px": "100042.7",
                            "side": "sell",
                            "sz": "1",
                            "sCode": "0",
                            "sMsg": ""
                        },
                        "to": {
                            "instId": "BTC-USD-SWAP",
                            "px": "100042.7",
                            "side": "buy",
                            "sz": "1",
                            "tdMode": "cross",
                            "posSide": "net",
                            "ccy": "",
                            "sCode": "0",
                            "sMsg": ""
                        }
                    },
                    {
                        "from": {
                            "posId": "2063111180412153856",
                            "instId": "BTC-USDT-SWAP",
                            "px": "100008.1",
                            "side": "sell",
                            "sz": "1",
                            "sCode": "0",
                            "sMsg": ""
                        },
                        "to": {
                            "instId": "BTC-USDT-SWAP",
                            "px": "100008.1",
                            "side": "buy",
                            "sz": "1",
                            "tdMode": "cross",
                            "posSide": "net",
                            "ccy": "",
                            "sCode": "0",
                            "sMsg": ""
                        }
                    }
                ]
            }
        ]
    }
    
    

> 返回示例:失败
    
    
    // 目标账户处于开平仓模式，传入posSide:net不匹配
    {
        "code": "51000",
        "msg": "Incorrect type of posSide (leg with Instrument Id [BTC-USD-SWAP])",
        "data": []
    }
    
    // 目标账户的BTC余额不足以开新仓位
    {
        "code": "51008",
        "msg": "Order failed. Insufficient BTC margin in account",
        "data": []
    }
    
    // TradeFi仓位不支持移仓
    {
        "code": "70004",
        "msg": "Invalid instrument ID XAG-USDT-SWAP",
        "data": []
    }
    
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
code | String | 结果代码，`0`表示成功  
msg | String | 错误信息，代码为0时，该字段为空  
blockTdId | String | 大宗交易ID  
clientId | String | 客户自定义ID  
state | String | 移仓状态，`filled` `failed`  
fromAcct | String | 源账户名  
toAcct | String | 目标账户名  
legs | Array | 移仓仓位列表  
> from | Object | 源账户仓位  
>> instId | String | 产品ID  
>> posId | String | 持仓ID  
>> px | String | 移仓价格，过去60分钟的标记价格TWAP  
>> side | String | 源账户的交易方向  
`buy`  
`sell`  
>> sz | String | 合约数量  
>> sCode | String | 事件执行结果的code，0代表成功  
>> sMsg | String | 事件执行失败或成功时的msg  
> to | Object | 目标账户移仓配置  
>> instId | String | 产品ID  
>> side | String | 目标账户交易方向  
>> posSide | String | 目标账户持仓方向  
>> tdMode | String | 目标账户的交易模式  
>> px | String | 移仓价格，过去60分钟的标记价格TWAP  
>> ccy | String | 保证金币种  
>> sCode | String | 事件执行结果的code，0代表成功  
>> sMsg | String | 事件执行失败或成功时的msg  
ts | String | 移仓请求处理时间戳，Unix时间戳的毫秒数格式，如`1597026383085`  
  
#### 注意事项

  1. 仅适用于交易等级大于等于VIP6的用户，仅能通过母账户的API Key调用
  2. 移仓的源账户和目标账户必须是统一主账户下的子账户，且两者不能相同
  3. 对于源账户，24小时内最多可触发15次移仓请求，目标账户接收仓位没有次数限制，只有成功的请求才会计入该限制
  4. 每个移仓请求最多支持30个仓位
  5. 目前暂不收取移仓手续费
  6. 目前币币杠杆交易产生的仓位不支持移仓
  7. TradeFi仓位不支持移仓
  8. 移仓价格采用过去60分钟内每分钟标记价格收盘价的TWAP（时间加权平均价格），若交易对为新上币且无法获取60分钟TWAP，移仓将被拒绝并返回错误码70065
  9. 移仓适用于订单簿相同的限价，若标记价格TWAP超出限价范围，移仓将失败
  10. 对源账户而言，移仓必须以只减仓模式进行；必须选择当前持仓的相反方向，且划转数量需小于或等于现有持仓量；系统将以尽力而为的方式按只减仓原则处理移仓请求
  11. 当持有多仓时，源账户的side字段应为sell，目标账户则应为buy；空仓时，方向相反
  12. 目标账户若为买卖模式，posSide应为net；若为开平仓模式，则需指定posSide为long/short以决定平仓或反向开仓，未指定时默认开新仓： 
     1. 开多：买入开多（side: buy; posSide: long）
     2. 开空：卖出开空（side: sell; posSide: short）
     3. 平多：卖出平多（side: sell; posSide: long）
     4. 平空：买入平空（side: buy; posSide: short
  13. 移仓历史可通过”获取移仓历史”接口查询，该接口仅包含处理中或成功的请求
  14. 移仓操作计数示例

移仓操作 | 账户A总计次数 | 账户B总计次数 | 账户C总计次数 | 账户D总计次数  
---|---|---|---|---  
账户A到账户B | 1 | 0 | 0 | 0  
账户B到账户C | 1 | 1 | 0 | 0  
账户B到账户D | 1 | 2 | 0 | 0  
  
### 获取移仓历史 

仅适用于交易等级大于等于VIP6的用户，仅能通过母账户的API Key调用。用户可通过[我的手续费](https://www.okx.com/balance/fee)页面的手续费详情表格查看自己的交易等级。  

获取过去三天的移仓明细。

#### 限速：2次/2s

#### 限速规则：母账户 User ID

#### HTTP请求

`GET /api/v5/account/move-positions-history`

> 请求示例
    
    
    Get /api/v5/account/move-positions-history
    
    

#### 请求参数

**参数名** | **类型** | **是否必须** | **描述**  
---|---|---|---  
blockTdId | String | 否 | 大宗交易ID  
clientId | String | 否 | 客户自定义ID字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度要在1-32位之间  
beginTs | String | 否 | 用开始时间戳筛选执行时间，Unix时间戳的毫秒数格式，如`1597026383085`  
endTs | String | 否 | 用结束时间戳筛选执行时间，Unix时间戳的毫秒数格式，如`1597026383085`  
limit | String | 否 | 返回结果的数量，最大为100，默认100条  
state | String | 否 | 移仓状态，`filled` `pending`  
  
> 返回示例
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "clientId": "test",
                "blockTdId": "2066393411110139648",
                "state": "filled",
                "ts": "1734085725000",
                "fromAcct": "0",
                "toAcct": "test",
                "legs": [
                    {
                        "from": {
                            "posId": "2065477911110792832",
                            "instId": "BTC-USD-SWAP",
                            "px": "100123.8",
                            "side": "sell",
                            "sz": "1"
                        },
                        "to": {
                            "instId": "BTC-USD-SWAP",
                            "px": "100123.8",
                            "side": "buy",
                            "sz": "1",
                            "tdMode": "cross",
                            "posSide": "net",
                            "ccy": ""
                        }
                    },
                    {
                        "from": {
                            "posId": "2063533111112153856",
                            "instId": "BTC-USDT-SWAP",
                            "px": "100078.7",
                            "side": "sell",
                            "sz": "1"
                        },
                        "to": {
                            "instId": "BTC-USDT-SWAP",
                            "px": "100078.7",
                            "side": "buy",
                            "sz": "1",
                            "tdMode": "cross",
                            "posSide": "net",
                            "ccy": ""
                        }
                    }
                ]
            }
       ]
    }
    
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
clientId | String | 客户自定义ID  
blockTdId | String | 大宗交易ID  
state | String | 移仓状态，`filled` `failed`  
ts | String | 移仓请求处理时间戳，Unix时间戳的毫秒数格式，如`1597026383085`  
fromAcct | String | 源账户名  
toAcct | String | 目标账户名  
legs | Array | 移仓仓位列表  
> from | Object | 源账户仓位  
>> instId | String | 产品ID  
>> posId | String | 持仓ID  
>> px | String | 移仓价格，过去60分钟的标记价格TWAP  
>> side | String | 源账户的交易方向  
`buy`  
`sell`  
>> sz | String | 合约数量  
> to | Object | 目标账户移仓配置  
>> instId | String | 产品ID  
>> px | String | 移仓价格，过去60分钟的标记价格TWAP  
>> side | String | 目标账户交易方向  
>> sz | String | 合约数量  
>> tdMode | String | 目标账户的交易模式  
>> posSide | String | 目标账户持仓方向  
>> ccy | String | 保证金币种  
  
### 设置自动赚币 

开启/关闭自动赚币

#### 限速：2次/2s

#### 限速规则：User ID

#### HTTP请求

`POST /api/v5/account/set-auto-earn`

> 请求示例
    
    
    // 开启自动赚币
    {
       "earnType": "0",
       "ccy":"BTC",
       "action":"turn_on"
    }
    
    

#### 请求参数

**参数名** | **类型** | **是否必须** | **描述**  
---|---|---|---  
earnType | String | 否 | 自动赚币类型  
`0`: 自动赚币 (自动出借、自动质押)   
`1`: 自动赚币（USDG 赚币）  
默认值为 `0`  
ccy | String | 是 | 币种  
action | String | 是 | 自动赚币操作类型  
`turn_on`: 开启自动赚币  
`turn_off`: 关闭自动赚币  
~~`amend`: 修改最低年化收益率，仅适用于 earnType `0`~~（已弃用）  
apr | String | 可选 | ~~最低年化收益率~~ （已弃用）  
  
> 返回结果
    
    
    {
       "code":"0",
       "msg":"",
       "data":[
          {
             "earnType": "0",
             "ccy":"BTC",
             "action":"turn_on",
             "apr":"0.01"
          }
       ]
    }
    
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
earnType | String | 自动赚币类型  
`0`: 自动赚币 (自动出借、自动质押)   
`1`: 自动赚币（USDG 赚币）  
ccy | String | 币种  
action | Boolean | 自动赚币操作类型  
`turn_on`  
`turn_off`  
~~`amend`~~ （已弃用）  
apr | String | ~~最低年化收益率~~ （已弃用）  
  
### 设置结算币种 

仅适用于 USD 本位合约。

#### 限速：20 次/2 秒

#### 限速规则：User ID

#### HTTP 请求

`POST /api/v5/account/set-settle-currency`

> 请求示例
    
    
    POST /api/v5/account/set-settle-currency
    body
    {
        "settleCcy": "USDC"
    }
    
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
settleCcy | String | 是 | USD 本位合约结算币种  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data" :[
              {
                "settleCcy":"USDC"
              }
        ]  
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
settleCcy | String | USD 本位合约结算币种  
  
### 设置交易配置 

#### **限速：1次/2s**

#### **限速规则：User ID**

#### **HTTP请求**

`POST /api/v5/account/set-trading-config`

> 请求示例
    
    
    POST /api/v5/account/set-trading-config
    body
    {
        "type": "stgyType",
        "stgyType":"1"
    }
    
    

#### 请求参数

**参数名** | **类型** | **是否必须** | **描述**  
---|---|---|---  
type | String | Yes | 交易配置类型  
`stgyType`  
stgyType | String | No | 账号策略类型  
`0`：普通策略模式  
`1`：delta 中性策略模式  
仅适用于type为`stgyType`  
  
> 返回示例
    
    
    {
       "code":"0",
       "msg":"",
       "data":[
          {
                "type": "stgyType",
                "stgyType":"1"
          }
       ]
    }
    
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
type | String | 交易配置类型  
stgyType | String | 账号策略类型  
  
### 设置Delta中性预检查 

#### **限速：1次/2s**

#### **限速规则：User ID**

#### **HTTP请求**

`GET /api/v5/account/precheck-set-delta-neutral`

> 请求示例
    
    
    GET /api/v5/account/precheck-set-delta-neutral?stgyType=1
    
    

#### 请求参数

**参数名** | **类型** | **是否必须** | **描述**  
---|---|---|---  
stgyType | String | Yes | 策略类型  
`0`：普通策略模式  
`1`：delta 中性策略模式  
  
> 返回示例
    
    
    {
        "code": "0",
        "data": [
            {
                "unmatchedInfoCheck": [
                    {
                        "posList": [],
                        "ordList": [],
                        "deltaLever": "",
                        "type": "spot_mode"
                    },
                   {
                        "posList": ["123","123","123"],
                        "ordList": [],
                        "deltaLever": "",
                        "type": "isolated_margin"
                    }
                ]
            }
        ],
        "msg": ""
    }
    
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
unmatchedInfoCheck | Array of objects | 包含不匹配信息对象的列表  
> type | String | 不匹配信息类型  
`spot_mode`：delta 中性策略模式不支持现货模式  
`futures_mode`：delta 中性策略模式不支持合约模式  
`isolated_margin`：delta 中性策略模式不支持逐仓杠杆仓位  
`isolated_contract`：delta 中性策略模式不支持逐仓合约仓位  
`positions_options`：delta 中性策略模式不支持期权仓位  
`isolated_pending_orders`：delta 中性策略模式不支持逐仓挂单  
`pending_orders_options`：delta 中性策略模式不支持期权挂单  
`trading_bot`：delta 中性策略模式不支持策略交易  
`repay_borrowings`：在转换后，在目前策略下的负债量超过母账户维度借币限额，请偿还负债后重试  
`loan`：不支持delta 中性策略模式使用活期借币  
`delta_risk`：Delta风险检查失败，降低delta后重试  
`collateral_all`：delta 中性策略模式下，所有币种必要被设置为质押币  
`risk_unit_type`：该账户在Delta中性风险单元内，无法切换至通用模式。请在切换策略前将其从风险单元中移除。  
> deltaLever | String | Delta权益比率  
仅适用于type为`delta_risk`  
> ordList | Array of strings | 不匹配订单列表，返回订单ID  
在type为`isolated_pending_orders`/`pending_orders_options`时适用  
> posList | Array of strings | 不匹配仓位列表，返回仓位ID  
在type为`isolated_margin`/`isolated_contract`/`positions_options`时适用  
  
### 调整模拟盘余额 

**此接口仅适用于模拟交易环境。**

允许用户对模拟账户中特定币种（BTC、ETH、USDT、OKB）的余额进行增加或减少，以便在不同资金情况下灵活测试交易策略。

原子性操作：若请求中任意币种未通过业务校验，整个请求将被拒绝，所有币种余额均不做修改。

#### 限速：增加 — 每用户每天 3 次（UTC 0:00 重置）；减少 — 无限制

#### 限速规则：User ID

#### HTTP请求

`POST /api/v5/account/demo-adjust-balance`

> 请求示例
    
    
    POST /api/v5/account/demo-adjust-balance
    body
    {
        "type": "increase",
        "adjustments": [
            { "ccy": "BTC", "amt": "0.5" },
            { "ccy": "USDT", "amt": "3000" }
        ]
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
type | String | 是 | 调整方向。  
`increase`：增加余额  
`reduce`：减少余额  
每次请求只能选择一个方向，不可同时包含增加和减少。  
adjustments | Array | 是 | 币种调整列表，至少包含一项，不允许重复币种。  
> ccy | String | 是 | 币种。支持：`BTC` `ETH` `USDT` `OKB`  
> amt | String | 是 | 调整数量。必须为非负数，小数位数不超过该币种精度。  
单次增加上限：BTC：1，ETH：1，USDT：5000，OKB：100。  
减少操作无单次数量限制，仅受可用余额 ≥ 0 约束。  
  
> 返回示例
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
            "remainCnt": "2",
            "totalCnt": "3",
            "details": [
                { "ccy": "BTC", "amt": "0.5", "bal": "1.5" },
                { "ccy": "USDT", "amt": "3000", "bal": "13000" }
            ]
        }]
    }
    

> 失败示例
    
    
    {
        "code": "59693",
        "msg": "USDT transferable balance insufficient. Some funds are occupied by open orders or positions. Please cancel orders or close positions and try again",
        "data": []
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
remainCnt | String | 当日剩余增加余额次数。减少操作也会返回该字段，但减少操作不消耗次数。  
totalCnt | String | 每日增加余额总次数（默认为 3）。  
details | Array | 各币种操作详情。  
> ccy | String | 币种。  
> amt | String | 实际调整数量。  
> bal | String | 操作后该币种的余额。  
  
## WebSocket 

### 账户频道 

获取账户信息，首次订阅按照订阅维度推送数据，此外，当下单、撤单、成交等事件触发时，推送数据以及按照订阅维度定时推送数据  

该频道的并发连接受到如下规则限制：[WebSocket 连接限制](/docs-v5/zh/#overview-websocket-connection-count-limit)

#### 服务地址

/ws/v5/private (需要登录)

> 请求示例：单个
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [{
            "channel": "account",
            "ccy": "BTC"
        }]
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
            url = "wss://ws.okx.com:8443/ws/v5/private",
            useServerTime=False
        )
        await ws.start()
        args = [{
            "channel": "account",
            "ccy": "BTC"
        }]
    
        await ws.subscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
        await ws.unsubscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
    asyncio.run(main())
    

> 请求示例
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [
        {
          "channel": "account",
          "extraParams": "
            {
              \"updateInterval\": \"0\"
            }
          "
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
            url = "wss://ws.okx.com:8443/ws/v5/private",
            useServerTime=False
        )
        await ws.start()
        args = [
            {
              "channel": "account",
              "extraParams": "{\"updateInterval\": \"0\"}"
            }
        ]
    
        await ws.subscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
        await ws.unsubscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
    
    asyncio.run(main())
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
id | String | 否 | 消息的唯一标识。  
用户提供，返回参数中会返回以便于找到相应的请求。  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度必须要在1-32位之间。  
op | String | 是 | 操作  
`subscribe`  
`unsubscribe`  
args | Array of objects | 是 | 请求订阅的频道列表  
> channel | String | 是 | 频道名  
`account`  
> ccy | String | 否 | 币种  
> extraParams | String | 否 | 额外配置  
>> updateInterval | int | 否 | `0`: 仅根据账户事件推送数据   
若不添加该字段或将其设置为除0外的其他值，数据将根据事件推送并定时推送。   
使用该字段需严格遵守以下格式。   
"extraParams": "  
{  
\"updateInterval\": \"0\"  
}  
"  
  
> 成功返回示例：单个
    
    
    {
        "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "account",
            "ccy": "BTC"
        },
      "connId": "a4d3ae55"
    }
    
    
    
    import asyncio
    
    from okx.websocket.WsPrivateAsync import WsPrivateAsync
    
    
    def privateCallback(message):
        print(message)
    
    async def main():
        ws = WsPrivateAsync(
            apiKey = "YOUR_API_KEY",
            passphrase = "YOUR_PASSPHRASE",
            secretKey = "YOUR_SECRET_KEY",
            url = "wss://ws.okx.com:8443/ws/v5/private",
            useServerTime=False
        )
        await ws.start()
        args = [{"channel": "account"}]
    
        await ws.subscribe(args, callback=privateCallback)
        await asyncio.sleep(10)
    
        await ws.unsubscribe(args, callback=privateCallback)
        await asyncio.sleep(10)
    
    asyncio.run(main())
    
    

> 成功返回示例
    
    
    {
        "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "account"
        },
      "connId": "a4d3ae55"
    }
    

> 失败返回示例
    
    
    {
        "id": "1512",
        "event": "error",
        "code": "60012",
        "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"account\", \"ccy\" : \"BTC\"}]}",
      "connId": "a4d3ae55"
    }
    

#### 返回参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
id | String | 否 | 消息的唯一标识  
event | String | 是 | 事件  
`subscribe`  
`unsubscribe`  
`error`  
arg | Object | 否 | 订阅的频道  
> channel | String | 是 | 频道名  
`account`  
> ccy | String | 否 | 币种  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID  
  
> 推送示例
    
    
    {
        "arg": {
            "channel": "account",
            "uid": "44*********584"
        },
        "eventType": "snapshot",
        "curPage": 1,
        "lastPage": true,
        "data": [{
            "adjEq": "55444.12216906034",
            "availEq": "55444.12216906034",
            "borrowFroz": "0",
            "delta": "0",
            "deltaLever": "0",
            "deltaNeutralStatus": "0",
            "details": [{
                "availBal": "4734.371190691436",
                "availEq": "4734.371190691435",
                "borrowFroz": "0",
                "cashBal": "4750.426970691436",
                "ccy": "USDT",
                "coinUsdPrice": "0.99927",
                "crossLiab": "0",
                "colRes": "0",
                "collateralEnabled": false,
                "collateralRestrict": false, // 已弃用，请使用colRes
                "colBorrAutoConversion": "0",
                "disEq": "4889.379316336831",
                "eq": "4892.951170691435",
                "eqUsd": "4889.379316336831",
                "smtSyncEq": "0",
                "spotCopyTradingEq": "0",
                "fixedBal": "0",
                "frozenBal": "158.57998",
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
                "maxSpotInUseAmt": "",          
                "spotIsoBal": "0",
                "stgyEq": "150",
                "twap": "0",
                "uTime": "1705564213903",
                "upl": "-7.475800000000003",
                "uplLiab": "0",
                "spotBal": "",
                "openAvgPx": "",
                "accAvgPx": "",
                "spotUpl": "",
                "spotUplRatio": "",
                "totalPnl": "",
                "totalPnlRatio": ""
            }],
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
            "totalEq": "55868.06403501676",
            "uTime": "1705564223311",
            "upl": "0"
        }]
    }
    

#### 推送数据参数

**参数名** | **类型** | **描述**  
---|---|---  
arg | Object | 请求订阅的频道  
> channel | String | 频道名  
> uid | String | 用户标识  
eventType | String | 事件类型：  
`snapshot`: 首推及定时快照推送   
`event_update`：事件推送  
curPage | Integer | 当前消息分页页数   
仅适用于`snapshot`事件类型，`event_update`时不返回。  
lastPage | Boolean | 当前消息是否为最后一页：  
`true`  
`false`  
仅适用于`snapshot`事件类型，`event_update`时不返回.  
data | Array of objects | 订阅的数据  
> uTime | String | 获取账户信息的最新时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
> totalEq | String | 美金层面权益  
> isoEq | String | 美金层面逐仓仓位权益  
适用于`合约模式`/`跨币种保证金模式`/`组合保证金模式`  
> adjEq | String | 美金层面有效保证金  
适用于`现货模式`/`跨币种保证金模式`/`组合保证金模式`  
> availEq | String | 账户美金层面可用保证金，排除因总质押借币上限而被限制的币种  
适用于`跨币种保证金模式/组合保证金模式`  
> ordFroz | String | 美金层面全仓挂单占用保证金  
仅适用于`现货模式`/`跨币种保证金模式`  
> imr | String | 美金层面占用保证金  
适用于`现货模式`/`跨币种保证金模式`/`组合保证金模式`  
> mmr | String | 美金层面维持保证金  
适用于`现货模式`/`跨币种保证金模式`/`组合保证金模式`  
> borrowFroz | String | 账户美金层面潜在借币占用保证金  
仅适用于`现货模式`/`跨币种保证金模式`/`组合保证金模式`。在其他账户模式下为""。  
> mgnRatio | String | 美金层面维持保证金率  
适用于`现货模式`/`跨币种保证金模式`/`组合保证金模式`  
> notionalUsd | String | 以美金价值为单位的持仓数量，即仓位美金价值  
适用于`现货模式`/`跨币种保证金模式`/`组合保证金模式`  
> notionalUsdForBorrow | String | 借币金额（美元价值）  
适用于`现货模式`/`跨币种保证金模式`/`组合保证金模式`  
> notionalUsdForSwap | String | 永续合约持仓美元价值  
适用于`跨币种保证金模式`/`组合保证金模式`  
> notionalUsdForFutures | String | 交割合约持仓美元价值  
适用于`跨币种保证金模式`/`组合保证金模式`  
> notionalUsdForOption | String | 期权持仓美元价值  
适用于`现货模式`/`跨币种保证金模式`/`组合保证金模式`  
> upl | String | 账户层面全仓未实现盈亏（美元单位）  
适用于`跨币种保证金模式`/`组合保证金模式`  
> delta | String | Delta (USD)  
> deltaLever | String | Delta权益比率  
deltaLever = delta/totalEq  
> deltaNeutralStatus | String | Delta 风险状态  
`0`: 普通  
`1`: 限制划转  
`2`: 仅支持降低 Delta - 相同基础货币的现货、交割和永续合约视为同一标的资产。同一标的资产内，仅能新下一笔降低 Delta 值的订单，且下单时不应存在其他挂单。如果触发此限制，且您的账户 Delta 大于 500,000 USD，您的所有限价、市价、高级限价单挂单将被撤销。  
> details | Array | 各币种资产详细信息  
>> ccy | String | 币种  
>> eq | String | 币种总权益  
>> cashBal | String | 币种余额  
>> uTime | String | 币种余额信息的更新时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
>> isoEq | String | 币种逐仓仓位权益  
适用于`合约模式`/`跨币种保证金模式`/`组合保证金模式`  
>> availEq | String | 可用保证金  
适用于`合约模式`/`跨币种保证金模式`/`组合保证金模式`  
>> disEq | String | 美金层面币种折算权益  
>> fixedBal | String | 抄底宝、逃顶宝功能的币种冻结金额  
>> availBal | String | 可用余额  
>> frozenBal | String | 币种占用金额  
>> ordFrozen | String | 挂单冻结数量  
适用于`现货模式`/`合约模式`/`跨币种保证金模式`  
>> liab | String | 币种负债额  
值为正数，如 `21625.64`  
适用于`现货模式`/`跨币种保证金模式`/`组合保证金模式`  
>> upl | String | 未实现盈亏  
适用于`合约模式`/`跨币种保证金模式`/`组合保证金模式`  
>> uplLiab | String | 由于仓位未实现亏损导致的负债  
适用于`跨币种保证金模式`/`组合保证金模式`  
>> crossLiab | String | 币种全仓负债额  
适用于`现货模式`/`跨币种保证金模式`/`组合保证金模式`  
>> isoLiab | String | 币种逐仓负债额  
适用于`跨币种保证金模式`/`组合保证金模式`  
>> rewardBal | String | 体验金余额  
>> mgnRatio | String | 币种全仓维持保证金率，衡量账户内某项资产风险的指标  
适用于`合约模式`且有全仓仓位时  
>> imr | String | 币种维度全仓占用保证金  
适用于`合约模式`且有全仓仓位时  
>> mmr | String | 币种维度全仓维持保证金  
适用于`合约模式`且有全仓仓位时  
>> interest | String | 计息  
值为正数，如 `9.01`  
适用于`现货模式`/`跨币种保证金模式`/`组合保证金模式`  
>> twap | String | 当前负债币种触发自动换币的风险  
0、1、2、3、4、5其中之一，数字越大代表您的负债币种触发自动换币概率越高  
适用于`现货模式`/`跨币种保证金模式`/`组合保证金模式`  
>> frpType | String | 自动换币类型  
`0`：未发生自动换币  
`1`：基于用户的自动换币  
`2`：基于平台借币限额的自动换币  
  
当twap>=1时返回1或2代表自动换币风险类型，适用于`现货模式`/`跨币种保证金模式`/`组合保证金模式`  
>> maxLoan | String | 币种最大可借  
适用于`现货模式`/`跨币种保证金模式`/`组合保证金模式` 的全仓  
>> eqUsd | String | 币种权益美金价值  
>> notionalLever | String | 币种杠杆倍数  
适用于`合约模式`  
>> coinUsdPrice | String | 币种美元指数  
>> stgyEq | String | 策略权益  
>> isoUpl | String | 逐仓未实现盈亏  
适用于`合约模式`/`跨币种保证金模式`/`组合保证金模式`  
>> borrowFroz | String | 币种美金层面潜在借币占用保证金  
仅适用于`现货模式`/`跨币种保证金模式`/`组合保证金模式`。在其他账户模式下为""。  
>> spotInUseAmt | String | 现货对冲占用数量  
适用于`组合保证金模式`  
>> clSpotInUseAmt | String | 用户自定义现货占用数量  
适用于`组合保证金模式`  
>> maxSpotInUseAmt | String | 系统计算得到的最大可能现货占用数量  
适用于`组合保证金模式`  
>> spotIsoBal | String | 现货逐仓余额  
仅适用于现货带单/跟单  
适用于`现货模式`/`合约模式`  
>> smtSyncEq | String | 合约智能跟单权益  
默认为0，仅适用于跟单人。  
>> spotCopyTradingEq | String | 现货智能跟单权益  
默认为0，仅适用于跟单人。  
>> spotBal | String | 现货余额 ，单位为 币种，比如 BTC。[详情](https://www.okx.com/zh-hans/help/i-introduction-of-spot)  
>> openAvgPx | String | 现货开仓成本价 单位 USD。 [详情](https://www.okx.com/zh-hans/help/i-introduction-of-spot)  
>> accAvgPx | String | 现货累计成本价 单位 USD。 [详情](https://www.okx.com/zh-hans/help/i-introduction-of-spot)  
>> spotUpl | String | 现货未实现收益，单位 USD。 [详情](https://www.okx.com/zh-hans/help/i-introduction-of-spot)  
>> spotUplRatio | String | 现货未实现收益率。[详情](https://www.okx.com/zh-hans/help/i-introduction-of-spot)  
>> totalPnl | String | 现货累计收益，单位 USD。 [详情](https://www.okx.com/zh-hans/help/i-introduction-of-spot)  
>> totalPnlRatio | String | 现货累计收益率。[详情](https://www.okx.com/zh-hans/help/i-introduction-of-spot)  
>> colRes | String | 平台维度质押限制状态  
`0`：限制未触发  
`1`：限制未触发，但该币种接近平台质押上限  
`2`：限制已触发。该币种不可用作新订单的保证金，这可能会导致下单失败。但它仍会被计入账户有效保证金，保证金率不会收到影响。  
更多详情，请参阅[平台总质押借币上限说明](https://www.okx.com/zh-hans/help/introduction-to-the-platforms-collateralized-borrowing-limit-mechanism)。  
>> colBorrAutoConversion | String | 基于平台质押借币限额的自动换币风险指标。分为1-5多个等级，数字越大，触发自动换币的可能性越大。默认值为0，表示当前无风险。5表示该用户正在进行自动换币，4代表该用户即将被进行自动换币，1/2/3表示存在自动换币风险。  
适用于`现货模式`/`合约模式`/`跨币种保证金模式`/`组合保证金模式`  
当某币种的全平台质押借币量超出平台总上限一定比例时，对于质押该币种且借币量较大的用户，平台将通过自动换币降低质押借币风险。请减少该币种的质押数量或偿还负债，以降低风险。  
更多详情，请参阅[平台总质押借币上限说明](https://www.okx.com/zh-hans/help/introduction-to-the-platforms-collateralized-borrowing-limit-mechanism)。  
>> collateralRestrict | Boolean | ~~平台维度的质押借币限制  
`true`  
`false`~~（已弃用，请使用colRes）  
>> collateralEnabled | Boolean | `true`：质押币  
`false`：非质押币  
适用于`跨币种保证金模式  
  
\- 账户频道基于事件推送，并进行定时推送   
\- 账户频道的事件推送并非在事件发生时实时进行，而是按照大约50毫秒的固定时间窗口进行聚合推送。例如，在固定时间窗口内发生多个事件，系统将尽量聚合为一条消息并在固定时间窗口结束时进行推送。在数据量过大的情况下可能拆分为多条消息。   
\- 无论是否有账户维度的变化，定时推送都会发送更新    
\- 只推用户币种层面资产不为0的账户信息。币种层面资产不为0的定义：eq、availEq、availBal 中任意一个字段不为0，即币种层面资产不为0。如果数据太大无法在单个推送消息中发送，它将被分成多个消息发送。   
\- 例：按照所有币种订阅且有5个币种的余额或者权益都不为0，首次和定时推全部5个；账户下有一个币种余额或者权益改变，那么账户变更的触发只推这一个。 

### 持仓频道 

获取持仓信息，首次订阅按照订阅维度推送数据，此外，当下单、撤单等事件触发时，推送数据以及按照订阅维度定时推送数据  
该频道的并发连接受到如下规则限制：[WebSocket 连接限制](/docs-v5/zh/#overview-websocket-connection-count-limit)

#### 服务地址

/ws/v5/private (需要登录)

> 请求示例：单个
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [{
            "channel": "positions",
            "instType": "FUTURES",
            "instFamily": "BTC-USD"
        }]
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
            url = "wss://ws.okx.com:8443/ws/v5/private",
            useServerTime=False
        )
        await ws.start()
        args = [
            {
              "channel": "positions",
              "instType": "FUTURES",
              "instFamily": "BTC-USD"
            }
        ]
    
        await ws.subscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
        await ws.unsubscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
    
    asyncio.run(main())
    

> 请求示例
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [
            {
                "channel": "positions",
                "instType": "ANY",
                "extraParams": "
                    {
                        \"updateInterval\": \"0\"
                    }
                "
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
            url = "wss://ws.okx.com:8443/ws/v5/private",
            useServerTime=False
        )
        await ws.start()
        args = [
            {
                "channel": "positions",
                "instType": "ANY",
                "extraParams": "{\"updateInterval\": \"0\"}"
            }
        ]
    
        await ws.subscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
        await ws.unsubscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
    
    asyncio.run(main())
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
id | String | 否 | 消息的唯一标识。  
用户提供，返回参数中会返回以便于找到相应的请求。  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度必须要在1-32位之间。  
op | String | 是 | 操作  
`subscribe`  
`unsubscribe`  
args | Array of objects | 是 | 请求订阅的频道列表  
> channel | String | 是 | 频道名  
`positions`  
> instType | String | 是 | 产品类型  
`MARGIN`：币币杠杆  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`OPTION`：期权  
`EVENTS`：事件合约  
`ANY`：全部  
> instFamily | String | 否 | 交易品种  
适用于`交割`/`永续`/`期权`  
> instId | String | 否 | 产品ID  
如果同时传了 instId 和 instFamily，instId 将被使用  
> extraParams | String | 否 | 额外配置  
>> updateInterval | int | 否 | `0`: 仅根据持仓事件推送数据  
`2000, 3000, 4000`: 根据持仓事件推送，且根据设置的时间间隔定时推送（ms）  
  
若不添加该字段或将其设置为上述合法值以外的其他值，数据将根据事件推送并大约每 5 秒定期推送一次。  
  
使用该字段需严格遵守以下格式。  
"extraParams": "  
{  
\"updateInterval\": \"0\"  
}  
"  
  
> 成功返回示例：单个
    
    
    {
        "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "positions",
            "instType": "FUTURES",
            "instFamily": "BTC-USD"
        },
        "connId": "a4d3ae55"
    }
    

> 成功返回示例
    
    
    {
        "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "positions",
            "instType": "ANY"
        },
        "connId": "a4d3ae55"
    }
    

> 失败返回示例
    
    
    {
        "id": "1512",
        "event": "error",
        "code": "60012",
        "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"positions\", \"instType\" : \"FUTURES\"}]}",
        "connId": "a4d3ae55"
    }
    

#### 返回参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
id | String | 否 | 消息的唯一标识  
event | String | 是 | 事件  
`subscribe`  
`unsubscribe`  
`error`  
arg | Object | 否 | 订阅的频道  
> channel | String | 是 | 频道名  
> instType | String | 是 | 产品类型  
`MARGIN`：币币杠杆  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`OPTION`：期权  
`EVENTS`：事件合约  
`ANY`：全部  
> instFamily | String | 否 | 交易品种  
适用于`交割`/`永续`/`期权`  
> instId | String | 否 | 产品ID  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID  
  
> 推送示例：单个
    
    
    {
        "arg":{
            "channel":"positions",
            "uid": "77982378738415879",
            "instType":"FUTURES"
        },
        "eventType": "snapshot",
        "curPage": 1,
        "lastPage": true,
        "data":[
            {
                "adl":"1",
                "availPos":"1",
                "avgPx":"2566.31",
                "cTime":"1619507758793",
                "ccy":"ETH",
                "deltaBS":"",
                "deltaPA":"",
                "gammaBS":"",
                "gammaPA":"",
                "hedgedPos": "",
                "imr":"",
                "instId":"ETH-USD-210430",
                "instType":"FUTURES",
                "interest":"0",
                "idxPx":"2566.13",
                "last":"2566.22",
                "lever":"10",
                "liab":"",
                "liabCcy":"",
                "liqPx":"2352.8496681818233",
                "markPx":"2353.849",
                "margin":"0.0003896645377994",
                "mgnMode":"isolated",
                "mgnRatio":"11.731726509588816",
                "mmr":"0.0000311811092368",
                "notionalUsd":"2276.2546609009605",
                "optVal":"",
                "pTime":"1619507761462",
                "pendingCloseOrdLiabVal":"0.1",
                "pos":"1",
                "baseBorrowed": "",
                "baseInterest": "",
                "quoteBorrowed": "",
                "quoteInterest": "",
                "posCcy":"",
                "posId":"307173036051017730",
                "posSide":"long",
                "spotInUseAmt": "",
                "clSpotInUseAmt": "",
                "maxSpotInUseAmt": "",
                "spotInUseCcy": "",
                "bizRefId": "",
                "bizRefType": "",
                "thetaBS":"",
                "thetaPA":"",
                "tradeId":"109844",
                "uTime":"1619507761462",
                "upl":"-0.0000009932766034",
                "uplLastPx":"-0.0000009932766034",
                "uplRatio":"-0.0025490556801078",
                "uplRatioLastPx":"-0.0025490556801078",
                "vegaBS":"",
                "vegaPA":"",
                "realizedPnl":"0.001",
                "pnl":"0.0011",
                "fee":"-0.0001",
                "fundingFee":"0",
                "liqPenalty":"0",
                "nonSettleAvgPx":"",
                "settledPnl":"",
                "closeOrderAlgo":[
                    {
                        "algoId":"123",
                        "slTriggerPx":"123",
                        "slTriggerPxType":"mark",
                        "tpTriggerPx":"123",
                        "tpTriggerPxType":"mark",
                        "closeFraction":"0.6"
                    },
                    {
                        "algoId":"123",
                        "slTriggerPx":"123",
                        "slTriggerPxType":"mark",
                        "tpTriggerPx":"123",
                        "tpTriggerPxType":"mark",
                        "closeFraction":"0.4"
                    }
                ]
            }
        ]
    }
    

> 推送示例
    
    
    {
        "arg": {
            "channel": "positions",
            "uid": "77982378738415879",
            "instType": "ANY"
        },
        "eventType": "snapshot",
        "curPage": 1,
        "lastPage": true,
        "data": [{
            "adl": "1",
            "availPos": "1",
            "avgPx": "2566.31",
            "cTime": "1619507758793",
            "ccy": "ETH",
            "deltaBS": "",
            "deltaPA": "",
            "gammaBS": "",
            "gammaPA": "",
            "hedgedPos": "",
            "imr": "",
            "instId": "ETH-USD-210430",
            "instType": "FUTURES",
            "interest": "0",
            "idxPx": "2566.13",
            "last": "2566.22",
            "usdPx": "",
            "bePx": "2353.949",
            "lever": "10",
            "liab": "",
            "liabCcy": "",
            "liqPx": "2352.8496681818233",
            "markPx": "2353.849",
            "margin": "0.0003896645377994",
            "mgnMode": "isolated",
            "mgnRatio": "11.731726509588816",
            "mmr": "0.0000311811092368",
            "notionalUsd": "2276.2546609009605",
            "optVal": "",
            "pendingCloseOrdLiabVal": "0.1",
            "pTime": "1619507761462",
            "pos": "1",
            "baseBorrowed": "",
            "baseInterest": "",
            "quoteBorrowed": "",
            "quoteInterest": "",
            "posCcy": "",
            "posId": "307173036051017730",
            "posSide": "long",
            "spotInUseAmt": "",
            "clSpotInUseAmt": "",
            "maxSpotInUseAmt": "",
            "spotInUseCcy": "",
            "bizRefId": "",
            "bizRefType": "",
            "thetaBS": "",
            "thetaPA": "",
            "tradeId": "109844",
            "uTime": "1619507761462",
            "upl": "-0.0000009932766034",
            "uplLastPx": "-0.0000009932766034",
            "uplRatio": "-0.0025490556801078",
            "uplRatioLastPx": "-0.0025490556801078",
            "vegaBS": "",
            "vegaPA": "",
            "realizedPnl": "0.001",
            "pnl": "0.0011",
            "fee": "-0.0001",
            "fundingFee": "0",
            "liqPenalty": "0",
            "nonSettleAvgPx": "",
            "settledPnl": "",
            "closeOrderAlgo": [{
                    "algoId": "123",
                    "slTriggerPx": "123",
                    "slTriggerPxType": "mark",
                    "tpTriggerPx": "123",
                    "tpTriggerPxType": "mark",
                    "closeFraction": "0.6"
                },
                {
                    "algoId": "123",
                    "slTriggerPx": "123",
                    "slTriggerPxType": "mark",
                    "tpTriggerPx": "123",
                    "tpTriggerPxType": "mark",
                    "closeFraction": "0.4"
                }
            ]
        }, {
            "adl": "1",
            "availPos": "1",
            "avgPx": "2566.31",
            "cTime": "1619507758793",
            "ccy": "ETH",
            "deltaBS": "",
            "deltaPA": "",
            "gammaBS": "",
            "gammaPA": "",
            "imr": "",
            "hedgedPos": "",
            "instId": "ETH-USD-SWAP",
            "instType": "SWAP",
            "interest": "0",
            "idxPx": "2566.13",
            "last": "2566.22",
            "usdPx": "",
            "bePx": "2353.949",
            "lever": "10",
            "liab": "",
            "liabCcy": "",
            "liqPx": "2352.8496681818233",
            "markPx": "2353.849",
            "margin": "0.0003896645377994",
            "mgnMode": "isolated",
            "mgnRatio": "11.731726509588816",
            "mmr": "0.0000311811092368",
            "notionalUsd": "2276.2546609009605",
            "optVal": "",
            "pendingCloseOrdLiabVal": "0.1",
            "pTime": "1619507761462",
            "pos": "1",
            "baseBorrowed": "",
            "baseInterest": "",
            "quoteBorrowed": "",
            "quoteInterest": "",
            "posCcy": "",
            "posId": "307173036051017730",
            "posSide": "long",
            "spotInUseAmt": "",
            "clSpotInUseAmt": "",
            "maxSpotInUseAmt": "",
            "spotInUseCcy": "",
            "bizRefId": "",
            "bizRefType": "",
            "thetaBS": "",
            "thetaPA": "",
            "tradeId": "109844",
            "uTime": "1619507761462",
            "upl": "-0.0000009932766034",
            "uplLastPx": "-0.0000009932766034",
            "uplRatio": "-0.0025490556801078",
            "uplRatioLastPx": "-0.0025490556801078",
            "vegaBS": "",
            "vegaPA": "",
            "realizedPnl": "0.001",
            "pnl": "0.0011",
            "fee": "-0.0001",
            "fundingFee": "0",
            "liqPenalty": "0",
            "nonSettleAvgPx": "",
            "settledPnl": "",
            "closeOrderAlgo": [{
                    "algoId": "123",
                    "slTriggerPx": "123",
                    "slTriggerPxType": "mark",
                    "tpTriggerPx": "123",
                    "tpTriggerPxType": "mark",
                    "closeFraction": "0.6"
                },
                {
                    "algoId": "123",
                    "slTriggerPx": "123",
                    "slTriggerPxType": "mark",
                    "tpTriggerPx": "123",
                    "tpTriggerPxType": "mark",
                    "closeFraction": "0.4"
                }
            ]
        }]
    }
    

#### 推送数据参数

参数名 | 类型 | 描述  
---|---|---  
arg | Object | 订阅成功的频道  
> channel | String | 频道名  
> uid | String | 用户标识  
> instType | String | 产品类型  
`MARGIN`：币币杠杆  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`OPTION`：期权  
`EVENTS`：事件合约  
> instFamily | String | 交易品种  
> instId | String | 产品ID  
eventType | String | 事件类型：  
`snapshot`: 首推及定时快照推送   
`event_update`：事件推送  
curPage | Integer | 当前消息分页页数   
仅适用于`snapshot`事件类型，`event_update`时不返回。  
lastPage | Boolean | 当前消息是否为最后一页：  
`true`  
`false`  
仅适用于`snapshot`事件类型，`event_update`时不返回.  
data | Array of objects | 订阅的数据  
> instType | String | 产品类型  
`MARGIN`：币币杠杆  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`OPTION`：期权  
`EVENTS`：事件合约  
> mgnMode | String | 保证金模式， `cross`：全仓 `isolated`：逐仓  
> posId | String | 持仓ID  
> posSide | String | 持仓方向  
`long`：开平仓模式开多  
`short`：开平仓模式开空  
`net`：买卖模式（`交割`/`永续`/`期权`：`pos`为正代表开多，`pos`为负代表开空。`币币杠杆`：`posCcy`为交易货币时，代表开多；`posCcy`为计价货币时，代表开空。）  
> pos | String | 持仓数量，逐仓自主划转模式下，转入保证金后会产生pos为`0`的仓位  
> hedgedPos | String | 对冲持仓数量  
仅在delta 中性策略模式的账户返回stgyType:1，对普通策略模式的账户返回""  
> baseBal | String | ~~交易币余额，适用于`币币杠杆`（逐仓一键借币模式）~~（已弃用）  
> quoteBal | String | ~~计价币余额 ，适用于`币币杠杆`（逐仓一键借币模式）~~（已弃用）  
> baseBorrowed | String | ~~交易币已借，适用于`币币杠杆`（逐仓一键借币模式）~~（已弃用）  
> baseInterest | String | ~~交易币计息，适用于`币币杠杆`（逐仓一键借币模式）~~（已弃用）  
> quoteBorrowed | String | ~~计价币已借，适用于`币币杠杆`（逐仓一键借币模式）~~（已弃用）  
> quoteInterest | String | ~~计价币计息，适用于`币币杠杆`（逐仓一键借币模式）~~（已弃用）  
> posCcy | String | 持仓数量币种，仅适用于`币币杠杆`  
> availPos | String | 可平仓数量，适用于 `币币杠杆`,`期权`  
对于杠杆仓位，平仓时，杠杆还清负债后，余下的部分会视为币币交易，如果想要减少币币交易的数量，可通过"获取最大可用数量"接口获取只减仓的可用数量。  
> avgPx | String | 开仓平均价  
> upl | String | 未实现收益（以标记价格计算）  
> uplRatio | String | 未实现收益率（以标记价格计算  
> uplLastPx | String | 以最新成交价格计算的未实现收益，主要做展示使用，实际值还是 upl  
> uplRatioLastPx | String | 以最新成交价格计算的未实现收益率  
> instId | String | 产品ID，如 `BTC-USDT-SWAP`  
> lever | String | 杠杆倍数，不适用于`期权卖方`  
> liqPx | String | 预估强平价  
不适用于`期权`  
> markPx | String | 最新标记价格  
> imr | String | 初始保证金，仅适用于`全仓`  
> margin | String | 保证金余额，仅适用于`逐仓`，可增减  
> mgnRatio | String | 维持保证金率  
> mmr | String | 维持保证金  
> liab | String | 负债额，仅适用于`币币杠杆`  
> liabCcy | String | 负债币种，仅适用于`币币杠杆`  
> interest | String | 利息，已经生成未扣利息  
> tradeId | String | 最新成交ID  
> notionalUsd | String | 以美金价值为单位的持仓数量  
> optVal | String | 期权价值，仅适用于`期权`  
> pendingCloseOrdLiabVal | String | 逐仓杠杆负债对应平仓挂单的数量  
> adl | String | 自动减仓信号区，分为6档，从0到5，数字越小代表adl强度越弱  
仅适用于`交割/永续/期权`  
> bizRefId | String | 外部业务id，如 体验券id  
> bizRefType | String | 外部业务类型  
> ccy | String | 占用保证金的币种  
> last | String | 最新成交价  
> idxPx | String | 最新指数价格  
> usdPx | String | 保证金币种的市场最新美金价格 仅适用于`交割`/`永续`/`期权`  
> bePx | String | 盈亏平衡价  
> deltaBS | String | 美金本位持仓仓位delta，仅适用于`期权`  
> deltaPA | String | 币本位持仓仓位delta，仅适用于`期权`  
> gammaBS | String | 美金本位持仓仓位gamma，仅适用于`期权`  
> gammaPA | String | 币本位持仓仓位gamma，仅适用于`期权`  
> thetaBS | String | 美金本位持仓仓位theta，仅适用于`期权`  
> thetaPA | String | 币本位持仓仓位theta，仅适用于`期权`  
> vegaBS | String | 美金本位持仓仓位vega，仅适用于`期权`  
> vegaPA | String | 币本位持仓仓位vega，仅适用于`期权`  
> spotInUseAmt | String | 现货对冲占用数量  
适用于`组合保证金模式`  
> clSpotInUseAmt | String | 用户自定义现货占用数量  
适用于`组合保证金模式`  
> maxSpotInUseAmt | String | 系统计算得到的最大可能现货占用数量  
适用于`组合保证金模式`  
> spotInUseCcy | String | 现货对冲占用币种，如 `BTC`  
适用于`组合保证金模式`  
> realizedPnl | String | 已实现收益  
仅适用于`交割`/`永续`/`期权`  
realizedPnl=pnl+fee+fundingFee+liqPenalty+settledPnl  
> pnl | String | 平仓订单累计收益额(不包括手续费)  
> fee | String | 累计手续费金额，正数代表平台返佣 ，负数代表平台扣除  
> fundingFee | String | 累计资金费用  
> liqPenalty | String | 累计爆仓罚金，有值时为负数。  
> closeOrderAlgo | Array of objects | 平仓策略委托订单。调用策略委托下单，且`closeFraction`=1 时，该数组才会有值。  
>> algoId | String | 策略委托单ID  
>> slTriggerPx | String | 止损触发价  
>> slTriggerPxType | String | 止损触发价类型  
`last`：最新价格  
`index`：指数价格  
`mark`：标记价格  
>> tpTriggerPx | String | 止盈委托价  
>> tpTriggerPxType | String | 止盈触发价类型  
`last`：最新价格  
`index`：指数价格  
`mark`：标记价格  
>> closeFraction | String | 策略委托触发时，平仓的百分比。1 代表100%  
> cTime | String | 持仓创建时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
> uTime | String | 最近一次持仓更新时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
> pTime | String | 持仓信息的推送时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
> nonSettleAvgPx | String | 未结算均价  
不受结算影响的加权开仓价格，仅在新增头寸时更新，和开仓均价的主要区别在于是否受到结算影响。  
适用于`全仓``交割`  
> settledPnl | String | 累计已结算收益（以结算价格计算）  
适用于`全仓``交割`  
  
\- 持仓频道基于事件推送，并进行定时推送。   
\- 持仓频道的事件推送并非在事件发生时实时进行，而是按照大约50毫秒的固定时间窗口进行聚合推送。例如，在固定时间窗口内发生多个事件，系统将尽量聚合为一条消息并在固定时间窗口结束时进行推送。在数据量过大的情况下可能拆分为多条消息。   
\- 无论是否有仓位的变化，定时推送都会发送更新。   
\- 若事件推送和定时推送同时发生，系统将在发送一次事件推送消息后再发送一次定时推送消息。  Portfolio Margin 账户下，持仓的 IMR MMR的数据是后端服务以ristUnit为最小粒度重新计算，相同riskUnit全仓仓位的imr和mmr返回值相同。  逐仓交易设置里是自主划转模式，转入保证金后会推送持仓量为0的仓位。    
\- 只推用户持有的仓位。用户持仓仓位定义：持逐仓自主划转模式下的逐仓仓位pos=0，pos>0或者pos<0都认为持有仓位。如果数据太大无法在单个推送消息中发送，它将被分成多个消息发送。   
\- 例：按underlying订阅且该underlying下有20个持仓，首次和定时推全部20个；持仓下有一个成交改变其中的一个持仓，那么持仓变更只推这一个。  与交割合约不同，期权持仓到期之后，期权持仓在到期后会自动行权或作废，持仓本身随即消失，因此，该频道不会推送期权到期的信息。 

### 账户余额和持仓频道 

获取账户余额和持仓信息，首次订阅按照订阅维度推送数据，此外，当成交、资金划转等事件触发时，推送数据。  

该频道适用于尽快获取账户现金余额和仓位资产变化的信息。  
该频道的并发连接受到如下规则限制：[WebSocket 连接限制](/docs-v5/zh/#overview-websocket-connection-count-limit)

#### 服务地址

/ws/v5/private (需要登录)

> 请求示例
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [{
            "channel": "balance_and_position"
        }]
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
            url = "wss://ws.okx.com:8443/ws/v5/private",
            useServerTime=False
        )
        await ws.start()
        args = [{
            "channel": "balance_and_position"
        }]
    
        await ws.subscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
        await ws.unsubscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
    
    asyncio.run(main())
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
id | String | 否 | 消息的唯一标识。  
用户提供，返回参数中会返回以便于找到相应的请求。  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度必须要在1-32位之间。  
op | String | 是 | 操作  
`subscribe`  
`unsubscribe`  
args | Array of objects | 是 | 请求订阅的频道列表  
> channel | String | 是 | 频道名  
`balance_and_position`  
  
> 成功返回示例
    
    
    {
        "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "balance_and_position"
        },
        "connId": "a4d3ae55"
    }
    

> 失败返回示例
    
    
    {
        "id": "1512",
        "event": "error",
        "code": "60012",
        "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"balance_and_position\"}]}",
        "connId": "a4d3ae55"
    }
    

#### 返回参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
id | String | 否 | 消息的唯一标识  
event | String | 是 | 事件  
`subscribe`  
`unsubscribe`  
`error`  
arg | Object | 否 | 订阅的频道  
> channel | String | 是 | 频道名  
`balance_and_position`  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID  
  
> 推送示例
    
    
    {
        "arg": {
            "channel": "balance_and_position",
            "uid": "77982378738415879"
        },
        "data": [{
            "pTime": "1597026383085",
            "eventType": "snapshot",
            "balData": [{
                "ccy": "BTC",
                "cashBal": "1",
                "uTime": "1597026383085"
            }],
            "posData": [{
                "posId": "1111111111",
                "tradeId": "2",
                "instId": "BTC-USD-191018",
                "instType": "FUTURES",
                "mgnMode": "cross",
                "posSide": "long",
                "pos": "10",
                "ccy": "BTC",
                "posCcy": "",
                "avgPx": "3320",
                "nonSettleAvgPx": "",
                "settledPnl": "",
                "uTime": "1597026383085"
            }],
            "trades": [{
                "instId": "BTC-USD-191018",
                "tradeId": "2",
            }]
        }]
    }
    

#### 推送数据参数

**参数名** | **类型** | **描述**  
---|---|---  
arg | Object | 请求订阅的频道  
> channel | String | 频道名  
> uid | String | 用户标识  
data | Array of objects | 订阅的数据  
> pTime | String | 推送时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
> eventType | String | 事件类型  
`snapshot`：首推快照  
`delivered`：交割  
`exercised`：行权  
`transferred`：划转  
`filled`：成交  
`liquidation`：强平  
`claw_back`：穿仓补偿  
`adl`：ADL自动减仓  
`funding_fee`：资金费  
`adjust_margin`：调整保证金  
`set_leverage`：设置杠杆  
`interest_deduction`：扣息  
`settlement`：交割结算  
> balData | String | 余额数据  
>> ccy | String | 币种  
>> cashBal | String | 币种余额  
>> uTime | String | 币种余额信息的更新时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
> posData | String | 持仓数据  
>> posId | String | 持仓ID  
>> tradeId | String | 最新成交ID  
>> instId | String | 交易产品ID，如 `BTC-USD-180213`  
>> instType | String | 交易产品类型  
`MARGIN`：币币杠杆  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`OPTION`：期权  
>> mgnMode | String | 保证金模式  
`isolated`, `cross`  
>> avgPx | String | 开仓平均价  
>> ccy | String | 占用保证金的币种  
>> posSide | String | 持仓方向  
`long`，`short`，`net`  
>> pos | String | 持仓数量，逐仓自主划转模式下，转入保证金后会产生pos为`0`的仓位  
>> baseBal | String | ~~交易币余额  
适用于 `币币杠杆`（逐仓一键借币模式）~~（已弃用）  
>> quoteBal | String | ~~计价币余额  
适用于 `币币杠杆`（逐仓一键借币模式）~~（已弃用）  
>> posCcy | String | 持仓数量币种  
只适用于币币杠杆仓位。当是交割、永续、期权持仓时，该字段返回“”  
>> nonSettleAvgPx | String | 未结算均价  
不受结算影响的加权开仓价格，仅在新增头寸时更新，和开仓均价的主要区别在于是否受到结算影响。  
适用于`全仓``交割`  
>> settledPnl | String | 累计已结算收益（以结算价格计算）  
适用于`全仓``交割`  
>> uTime | String | 仓位信息的更新时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
> trades | Array of objects | 成交数据  
>> instId | String | 产品ID，如 `BTC-USDT`  
>> tradeId | String | 最新成交ID  
只有账户余额变化，只推balData；只有持仓余额发生变化，只推posData。    
\- 首次推送，只推用户持有的仓位和币种余额不为0的信息。如果数据太大无法在单个推送消息中发送，它将被分成多个消息发送。   
\- 例：比如按照所有币种订阅且用户有5个币种余额不为0 和20个仓位，那么首推全部5个币种余额列表和20个持仓信息列表；某个订单成交后，那么只推一个币种余额和对应的持仓信息。 

### 爆仓风险预警推送频道 

此推送频道仅作为风险提示，不建议作为策略交易的风险判断。  
在行情剧烈波动的情况下，可能会出现此消息推送的同时仓位已经被强平的可能性。  
预警会在某一个逐仓仓位有风险时推送。预警会在所有全仓仓位有风险时推送。  
该频道的并发连接受到如下规则限制：[WebSocket 连接限制](/docs-v5/zh/#overview-websocket-connection-count-limit)

#### 服务地址

/ws/v5/private (需要登录)

> 请求示例
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [{
            "channel": "liquidation-warning",
            "instType": "ANY"
        }]
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
            url = "wss://ws.okx.com:8443/ws/v5/private",
            useServerTime=False
        )
        await ws.start()
        args = [
            {
              "channel": "liquidation-warning",
              "instType": "ANY"
            }
        ]
    
        await ws.subscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
        await ws.unsubscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
    
    asyncio.run(main())
    
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
id | String | 否 | 消息的唯一标识。  
用户提供，返回参数中会返回以便于找到相应的请求。  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度必须要在1-32位之间。  
op | String | 是 | 操作  
`subscribe`  
`unsubscribe`  
args | Array of objects | 是 | 请求订阅的频道列表  
> channel | String | 是 | 频道名  
`liquidation-warning`  
> instType | String | 是 | 产品类型  
`MARGIN`：币币杠杆  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`OPTION`：期权  
`ANY`：全部  
> instFamily | String | 否 | 交易品种  
适用于`交割`/`永续`/`期权`  
> instId | String | 否 | 产品ID  
  
> 成功返回示例
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "liquidation-warning",
        "instType": "ANY"
      },
      "connId": "a4d3ae55"
    }
    

> 失败返回示例
    
    
    {
        "id": "1512",
        "event": "error",
        "code": "60012",
        "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"liquidation-warning\", \"instType\" : \"FUTURES\"}]}",
        "connId": "a4d3ae55"
    }
    

#### 返回参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
id | String | 否 | 消息的唯一标识  
event | String | 是 | 事件  
`subscribe`  
`unsubscribe`  
`error`  
arg | Object | 否 | 订阅的频道  
> channel | String | 是 | 频道名 ，`liquidation-warning`  
> instType | String | 是 | 产品类型  
`MARGIN`：币币杠杆  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`OPTION`：期权   
`ANY`：全部  
> instFamily | String | 否 | 交易品种  
适用于`交割`/`永续`/`期权`  
> instId | String | 否 | 产品ID  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID  
  
> 推送示例：单个
    
    
    {
        "arg":{
            "channel":"liquidation-warning",
            "uid": "77982378738415879",
            "instType":"FUTURES"
        },
        "data":[
            {
                "cTime":"1619507758793",
                "ccy":"ETH",
                "instId":"ETH-USD-210430",
                "instType":"FUTURES",
                "lever":"10",
                "markPx":"2353.849",
                "mgnMode":"isolated",
                "mgnRatio":"11.731726509588816",
                "pTime":"1619507761462",
                "pos":"1",
                "posCcy":"",
                "posId":"307173036051017730",
                "posSide":"long",
                "uTime":"1619507761462",
            }
        ]
    }
    

#### 推送数据参数

参数名 | 类型 | 描述  
---|---|---  
arg | Object | 订阅成功的频道  
> channel | String | 频道名  
> uid | String | 用户标识  
> instType | String | 产品类型  
> instFamily | String | 交易品种  
> instId | String | 产品ID  
data | Array of objects | 订阅的数据  
> instType | String | 产品类型  
> mgnMode | String | 保证金模式， `cross`：全仓 `isolated`：逐仓  
> posId | String | 持仓ID  
> posSide | String | 持仓方向  
`long`：开平仓模式开多  
`short`：开平仓模式开空  
`net`：买卖模式（`交割`/`永续`/`期权`：`pos`为正代表开多，`pos`为负代表开空。`币币杠杆`：`posCcy`为交易货币时，代表开多；`posCcy`为计价货币时，代表开空。）  
> pos | String | 持仓数量  
> posCcy | String | 持仓数量币种，仅适用于`币币杠杆`  
> instId | String | 产品ID，如 `BTC-USDT-SWAP`  
> lever | String | 杠杆倍数，不适用于`期权卖方`  
> markPx | String | 标记价格  
> mgnRatio | String | 维持保证金率  
> ccy | String | 占用保证金的币种  
> cTime | String | 持仓创建时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
> uTime | String | 最近一次持仓更新时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
> pTime | String | 持仓信息的推送时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
触发推送逻辑：爆仓预警和爆仓短信的触发逻辑一致 

### 账户greeks频道 

获取账户资产的greeks信息。当增加或者减少币种余额、持仓数量等会触发事件推送，周期性的也会有定时推送。  
该频道的并发连接受到如下规则限制：[WebSocket 连接限制](/docs-v5/zh/#overview-websocket-connection-count-limit)

#### 服务地址

/ws/v5/private (需要登录)

> 请求示例
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [{
            "channel": "account-greeks"
        }]
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
            url = "wss://ws.okx.com:8443/ws/v5/private",
            useServerTime=False
        )
        await ws.start()
        args = [{
            "channel": "account-greeks"
        }]
    
        await ws.subscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
        await ws.unsubscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
    
    asyncio.run(main())
    
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
id | String | 否 | 消息的唯一标识。  
用户提供，返回参数中会返回以便于找到相应的请求。  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度必须要在1-32位之间。  
op | String | 是 | 操作  
`subscribe`  
`unsubscribe`  
args | Array of objects | 是 | 请求订阅的频道列表  
> channel | String | 是 | 频道名  
`account-greeks`  
> ccy | String | 否 | 保证金币种  
当用户指定了保证金，只有作为保证金的仓位发生变化的时候，才会触发事件推送。例如当指定了ccy = `BTC`，如果 `BTC-USDT-SWAP` 仓位发生变化，不会触发事件推送。  
  
> 成功返回示例
    
    
    {
        "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "account-greeks"
        },
      "connId": "a4d3ae55"
    }
    

> 失败返回示例
    
    
    {
        "id": "1512",
        "event": "error",
        "code": "60012",
        "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"account-greeks\", \"ccy\" : \"BTC\"}]}",
      "connId": "a4d3ae55"
    }
    

#### 返回参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
id | String | 否 | 消息的唯一标识  
event | String | 是 | 事件  
`subscribe`  
`unsubscribe`  
`error`  
arg | Object | 否 | 订阅的频道  
> channel | String | 是 | 频道名  
`account-greeks`  
> ccy | String | 否 | 保证金币种  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID  
  
> 推送示例：单个
    
    
    {
        "arg": {
            "channel": "account-greeks",
            "ccy": "BTC",
            "uid": "614488474791936"
        },
        "data": [
            {
                "ccy": "BTC",
                "deltaBS": "1.1246665401944310",
                "deltaPA": "-0.0074076183688949",
                "gammaBS": "0.0000000000000000",
                "gammaPA": "0.0148152367377899",
                "thetaBS": "2.0356991946421226",
                "thetaPA": "-0.0000000200174309",
                "ts": "1729179082006",
                "vegaBS": "0.0000000000000000",
                "vegaPA": "0.0000000000000000"
            }
        ]
    }
    

> 推送示例
    
    
    {
        "arg": {
            "channel": "account-greeks",
            "uid": "614488474791936"
        },
        "data": [
            {
                "ccy": "BTC",
                "deltaBS": "1.1246665403011684",
                "deltaPA": "-0.0074021163991037",
                "gammaBS": "0.0000000000000000",
                "gammaPA": "0.0148042327982075",
                "thetaBS": "2.1342098201092528",
                "thetaPA": "-0.0000000200876441",
                "ts": "1729179001692",
                "vegaBS": "0.0000000000000000",
                "vegaPA": "0.0000000000000000"
            },
            {
                "ccy": "ETH",
                "deltaBS": "0.3810670161698570",
                "deltaPA": "-0.0688347042402955",
                "gammaBS": "-0.0000000000230396",
                "gammaPA": "0.1376693483440320",
                "thetaBS": "0.3314776517141782",
                "thetaPA": "0.0000000001316008",
                "ts": "1729179001692",
                "vegaBS": "-0.0000000045069794",
                "vegaPA": "-0.0000000000017267"
            }
        ]
    }
    

#### 推送数据参数

**参数名** | **类型** | **描述**  
---|---|---  
arg | Object | 请求订阅的频道  
> channel | String | 频道名  
> uid | String | 用户标识  
data | Array of objects | 订阅的数据  
> deltaBS | String | 美金本位账户资产delta  
> deltaPA | String | 币本位账户资产delta  
> gammaBS | String | 美金本位账户资产gamma，仅适用于期权全仓  
> gammaPA | String | 币本位账户资产gamma，仅适用于期权全仓  
> thetaBS | String | 美金本位账户资产theta，仅适用于期权全仓  
> thetaPA | String | 币本位账户资产theta，仅适用于期权全仓  
> vegaBS | String | 美金本位账户资产vega，仅适用于期权全仓  
> vegaPA | String | 币本位账户资产vega，仅适用于期权全仓  
> ccy | String | 币种  
> ts | String | 获取greeks的时间，Unix时间戳的毫秒数格式，如 1597026383085  
账户greeks频道基于事件推送，并进行定时推送  
\- greeks频道的事件推送并非在事件发生时实时进行，而是按照大约50毫秒的固定时间窗口进行聚合推送。例如，在固定时间窗口内发生多个事件，系统将尽量聚合为一条消息并在固定时间窗口结束时进行推送。在数据量过大的情况下可能拆分为多条消息。   
\- 当用户订阅时指定了保证金币种(ccy)，只有作为保证金的仓位发生变化的时候，才会触发事件推送。例如订阅时指定了ccy=`BTC`，如果`BTC-USDT-SWAP`仓位发生变化，不会触发事件推送。   
\- 无论是否有greeks数据的变化，定时推送都会发送更新。    
\- 只推账户资产不为0的greeks数据。如果数据太大无法在单个推送消息中发送，它将被分成多个消息发送。   
\- 例：按照所有币种订阅且有5个币种资产都不为0，首次和定时推全部5个；账户的某个币种资产改变，那么账户greeks变更的触发只推这一个。