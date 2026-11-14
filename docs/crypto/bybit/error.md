---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/error
api_type: REST
updated_at: 2026-11-13 19:22:29.387875
---

# Error Codes

## HTTP Code

Code| Description  
---|---  
400| Bad request. Need to send the request with **GET** / **POST** (must be capitalized)  
[401](/docs/pilot-feature#normal-account-is-supported-by-v5-api)| Invalid request. 1. Need to use the correct key to access; 2. Need to put authentication params in the request header  
403| Forbidden request. Possible causes: 1. IP rate limit breached; 2. You send GET request with an empty json body; 3. You are using U.S IP  
[404](/docs/pilot-feature#normal-account-is-supported-by-v5-api)| Cannot find path. Possible causes: 1. Wrong path; 2. Category value does not match account mode  
429| System level frequency protection. Please retry when encounter this  
  
## WS OE General code

Code| Description  
---|---  
10404| 1\. op type is not found; 2. `category` is not correct/supported  
10429| System level frequency protection  
10003| Too many sessions under the same UID  
10016| 1\. internal server error; 2. Service is restarting  
10019| ws trade service is restarting, do not accept new request, but the request in the process is not affected. You can build new connection to be routed to normal service  
20003| Too frequent requests under the same session  
20006| reqId is duplicated  
  
## UTA

Code| Description  
---|---  
0| OK  
-1| request expired: o@0, now[] diff[]  
429| The trading service is experiencing a high server load. Please retry if you encounter this issue.  
-2015| (Spot) Your api key has expired  
33004| (Derivatives) Your api key has expired  
10000| Server Timeout  
10001| Request parameter error  
10002| The request time exceeds the time window range.  
10003| API key is invalid. Check whether the key and domain are matched, there are 4 env: mainnet, testnet, mainnet-demo, testnet-demo  
10004| Error sign, please check your signature generation algorithm.  
10005| Permission denied, please check your API key permissions.  
10006| Too many visits. Exceeded the API Rate Limit.  
10007| User authentication failed.  
10008| Common banned, please check your account mode  
10009| Service Restricted: Access is currently unavailable for your region. Please contact our support team for further assistance  
10010| Unmatched IP, please check your API key's bound IP addresses.  
10014| Invalid duplicate request.  
10016| Server error.  
10017| Route not found.  
~~10018~~| ~~Exceeded the IP Rate Limit.~~  
10024| Compliance rules triggered  
10027| Transactions are banned.  
10029| The requested symbol is invalid, please check symbol whitelist  
10028| The API can only be accessed by unified account users.  
30035| Option: Too fast to cancel, Try it later  
30133| OTC loan: The symbol you select for USDT Perpetual is not allowed by Institutional Lending  
30134| OTC loan: The symbol you select for USDC Contract is not allowed by Institutional Lending  
30135| The leverage you select for USDT Perpetual trading cannot exceed the maximum leverage allowed by Institutional Lending.  
30136| The leverage you select for USDC Perpetual or Futures trading cannot exceed the maximum leverage allowed by Institutional Lending.  
30208| Failed to submit order(s). The order price is higher than the maximum buying price  
30209| Failed to submit order(s). The order price is lower than the minimum selling price.  
30228| No new positions during delisting  
30256| Margin limit exceeded. The maintenance margin required for this order exceeds the available risk margin under current LTV constraints (Spot)  
40004| the order is modified during the process of replacing , please check the order status again  
100028| The API cannot be accessed by unified account users.  
110001| Order does not exist  
110003| Order price exceeds the [allowable range](https://www.bybithelp.com/en-US/s/article/Contract-Price-Limits).  
110004| Wallet balance is insufficient  
110005| position status error  
110006| The assets are estimated to be unable to cover the position margin  
110007| Available balance is insufficient  
110008| The order has been completed or cancelled.  
110009| The number of stop orders exceeds the maximum allowable limit  
110010| The order has been cancelled  
110011| Liquidation will be triggered immediately by this adjustment  
110012| Insufficient available balance.  
110013| Cannot set leverage due to risk limit level.  
110014| Insufficient available balance to add additional margin.  
110015| The position is in cross margin mode.  
~~110016~~| ~~The quantity of contracts requested exceeds the risk limit, please adjust your risk limit level before trying again~~  
110017| orderQty will be truncated to zero  
110018| User ID is illegal.  
110019| Order ID is illegal.  
110020| Not allowed to have more than 500 active orders.  
110021| Not allowed to exceeded position limits due to Open Interest.  
110022| Quantity has been restricted and orders cannot be modified to increase the quantity.  
110023| Currently you can only reduce your position on this contract. please check our announcement or contact customer service for details.  
110024| You have an existing position, so the position mode cannot be switched.  
110025| Position mode has not been modified.  
110026| Cross/isolated margin mode has not been modified.  
110027| Margin has not been modified.  
110028| You have existing open orders, so the position mode cannot be switched.  
110029| Hedge mode is not supported for this symbol.  
~~110030~~| ~~Duplicate orderId~~  
110031| Non-existing risk limit info, please check the risk limit rules.  
110032| Order is illegal  
110033| You can't set margin without an open position  
110034| There is no net position  
110035| Cancellation of orders was not completed before liquidation  
110036| You are not allowed to change leverage due to cross margin mode.  
110037| User setting list does not have this symbol  
110038| You are not allowed to change leverage due to portfolio margin mode.  
110039| Maintenance margin rate is too high. This may trigger liquidation.  
110040| The order will trigger a forced liquidation, please re-submit the order.  
110041| Skip liquidation is not allowed when a position or maker order exists  
110042| Currently,due to pre-delivery status, you can only reduce your position on this contract.  
110043| Set leverage has not been modified.  
110044| Available margin is insufficient.  
110045| Wallet balance is insufficient.  
110046| Liquidation will be triggered immediately by this adjustment.  
110047| Risk limit cannot be adjusted due to insufficient available margin.  
110048| Risk limit cannot be adjusted as the current/expected position value exceeds the revised risk limit.  
110049| Tick notes can only be numbers  
110050| Invalid coin  
110051| The user's available balance cannot cover the lowest price of the current market  
110052| Your available balance is insufficient to set the price  
110053| The user's available balance cannot cover the current market price and upper limit price  
110054| This position has at least one take profit link order, so the take profit and stop loss mode cannot be switched  
110055| This position has at least one stop loss link order, so the take profit and stop loss mode cannot be switched  
110056| This position has at least one trailing stop link order, so the take profit and stop loss mode cannot be switched  
110057| Conditional order or limit order contains TP/SL related params  
110058| You can't set take profit and stop loss due to insufficient size of remaining position size.  
110059| Not allowed to modify the TP/SL of a partially filled open order  
110060| Under full TP/SL mode, it is not allowed to modify TP/SL  
110061| Not allowed to have more than 20 TP/SLs under Partial tpSlMode  
110062| There is no MMP information of the institution found.  
110063| Settlement in progress! {{key0}} not available for trading.  
110064| The modified contract quantity cannot be less than or equal to the filled quantity.  
110065| MMP hasn't yet been enabled for your account. Please contact your BD manager.  
110066| Trading is currently not allowed.  
110067| Unified account is not supported.  
110068| Leveraged trading is not allowed.  
110069| Ins lending customer is not allowed to trade.  
110070| ETP symbols cannot be traded.  
110071| Sorry, we're revamping the Unified Margin Account! Currently, new upgrades are not supported. If you have any questions, please contact our 24/7 customer support.  
110072| OrderLinkedID is duplicate  
110073| Set margin mode failed  
110074| This contract is not live  
~~110075~~| ~~RiskId not modified~~  
110076| Only isolated mode can set auto-add-margin  
110077| Pm mode cannot support  
110078| Added margin more than max can reduce margin  
110079| The order is processing and can not be operated, please try again later  
110080| Operations Restriction: The current LTV ratio of your Institutional Lending has hit the liquidation threshold. Assets in your account are being liquidated (trade/risk limit/leverage)  
110082| You cannot lift Reduce-Only restrictions, as no Reduce-Only restrictions are applied to your position  
110083| Reduce-Only restrictions must be lifted for both Long and Short positions at the same time  
110085| The risk limit and margin ratio for this contract has been updated, please select a supported risk limit and place your order again  
110086| Current order leverage exceeds the maximum available for your current Risk Limit tier. Please lower leverage before placing an order  
110087| Leverage for Perpetual or Futures contracts cannot exceed the maximum allowed for your Institutional loan  
110088| Please Upgrade to UTA to trade  
110089| Exceeds the maximum risk limit level  
110090| Order placement failed as your position may exceed the max limit. Please adjust your leverage to {{leverage}} or below to increase the max. position limit  
110092| expect Rising, but trigger_price[XXXXX] <= current[XXXXX]??laste  
110093| expect Falling, but trigger_price[XXXXX] >= current[XXXXX]??last  
110094| Order notional value below the lower limit  
110095| You cannot create, modify or cancel Pre-Market Perpetual orders during the Call Auction.  
110096| Pre-Market Perpetual Trading does not support Portfolio Margin mode.  
110097| Non-UTA users cannot access Pre-Market Perpetual Trading. To place, modify or cancel Pre-Market Perpetual orders, please upgrade your Standard Account to UTA.  
110098| Only Good-Till-Canceled (GTC) orders are supported during Call Auction.  
110099| You cannot create TP/SL orders during the Call Auction for Pre-Market Perpetuals.  
110100| You cannot place, modify, or cancel Pre-Market Perpetual orders when you are in Demo Trading.  
110101| Trading inverse contracts under Cross and Portfolio modes requires enabling the settlement asset as collateral.  
110102| The user does not support trading Inverse contracts - copy trading pro, Ins loan account are not supported  
110103| Only Post-Only orders are available at this stage  
110104| The LTV for ins Loan has exceeded the limit, and opening inverse contracts is prohibited  
110105| The LTV for ins Loan has exceeded the limit, and trading inverse contracts is prohibited  
110106| Restrictions on Ins Loan; inverse contracts are not on the whitelist and are not allowed for trading  
110107| Restrictions on ins Loan; leverage exceeding the limit for inverse contracts is not allowed.  
110108| Allowable range: 1 to 10000 tick size  
110109| Allowable range: 0.01% to 10%  
110110| Spread trading is not available in isolated margin trading mode  
110111| To access spread trading, upgrade to the latest version of UTA  
110112| Spread trading is not available for Copy Trading  
110113| Spread trading is not available in hedge mode  
110114| You have a Spread trading order in progress. Please try again later  
110115| The cancellation of a combo single-leg order can only be done by canceling the combo order  
110116| The entry price of a single leg, derived from the combo order price, exceeds the limit price  
110117| The modification of a combo single-leg order can only be done by modifying the combo order  
110118| Unable to retrieve a pruce of the market order due to low liquidity  
110119| Order failed. RPI orders are restricted to approved market makers only  
110120| Order price cannot be smaller than xxxx, the price limitation  
110121| Order price cannot be higher than xxxx, the price limitation  
110123| You must agree to the Trading Terms  
110124| Trading is temporarily restricted due to an active cooling-off period.  
110125| You must agree to the Trading Terms before trading this contract  
110131| Margin limit exceeded. The maintenance margin required for this order exceeds the available risk margin under current LTV constraints (Perps)  
110132| Product not available in your region  
110134| Trading on this symbol is suspended. Please try again later  
110135| You currently hold a position in an Event Futures contract. Order placement and modification are not supported under Portfolio Margin (PM) mode. Please close the relevant positions before proceeding.  
110136| Event Futures are currently available for trading via OpenAPI to whitelisted accounts only. Your account does not have the required access at this time.  
110137| This Event Futures contract has entered the reduce-only window before settlement. New orders and order modifications are temporarily suspended.  
170346| Settle coin is not a collateral coin, cannot trade  
170360| symbol[XXXX] cannot trade. Used for spread trading in particular when collateral is not turned on  
181017| OrderStatus must be final status  
182100| Compulsory closing of positions, no repayment allowed  
182101| Failed repayment, insufficient collateral balance  
182102| Failed repayment, there are no liabilities in the current currency  
182103| Institutional lending users are not supported  
182108| Switching failed, margin verification failed, please re-adjust the currency status  
182110| Failed to switch  
182111| The requested currency has a non guaranteed gold currency or does not support switching status currencies  
182112| Duplicate currency, please re-adjust  
182011| The {{coin}} collateral amount has reached the platform limit. Enable collateral for another asset, or transfer another supported asset to your account as collateral.  
182012| Due to regulatory requirements, collateral services are currently unavailable in your region.  
3100101| xxx_coin does not exist  
3100181| UID can not be null  
3100197| Temporary banned due to the upgrade to UTA  
3200306| Failed to place an order with the contract! Your maintenance margin utilization has exceeded the upper limit.  
3200316| USDC Options Trading Restriction: The current LTV ratio for your Institutional Lending has reached the maximum allowable amount for USDC Options trading.  
3200317| USDC Options Open Position Restriction: The current LTV ratio for your Institutional Lending has reached the maximum allowable amount for opening USDC Options positions.  
3100326| BaseCoin is required  
3200403| isolated margin can not create order  
3200419| Unable to switch to Portfolio margin due to active pre-market Perpetual orders and positions  
3200425| You currently hold a position in an Event Futures contract. Switching to Portfolio Margin (PM) mode is not allowed. Please close the relevant positions before switching.  
3200320| Operations Restriction: The current LTV ratio of your Institutional Lending has hit the liquidation threshold. Assets in your account are being liquidated. (margin mode or spot leverage)  
3200641| {{coin}} collateral has reached the platform limit. Disable {{coin}} collateral before switching margin mode.  
3400208| You have unclosed hedge mode or isolated mode USDT perpetual positions  
3400209| You have USDT perpetual positions, so upgrading is prohibited for 10 minutes before and after the hour every hour  
3400210| The risk rate of your Derivatives account is too high  
3400211| Once upgraded, the estimated risk rate will be too high  
3400212| You have USDC perpetual positions or Options positions, so upgrading is prohibited for 10 minutes before and after the hour every hour  
3400213| The risk rate of your USDC Derivatives account is too high  
3400052| You have uncancelled USDC perpetual orders  
3400053| You have uncancelled Options orders  
3400054| You have uncancelled USDT perpetual orders  
3400214| Server error, please try again later  
3400071| The net asset is not satisfied  
3401010| Cannot switch to PM mode (for copy trading master trader)  
3400139| The total value of your positions and orders has exceeded the risk limit for a Perpetual or Futures contract  
34040| Not modified. Indicates you already set this TP/SL value or you didn't pass a required parameter  
500010| The subaccount specified does not belong to the parent account  
500011| The Uid 592334 provided is not associated with a Unified Trading Account  
  
## Spot Trade

Code| Description  
---|---  
170001| Internal error.  
170005| Too many new orders; current limit is %s orders per %s.  
170007| Timeout waiting for response from backend server.  
170010| Purchase failed: Exceed the maximum position limit of leveraged tokens, the current available limit is %s USDT  
170011| "Purchase failed: Exceed the maximum position limit of innovation tokens,  
170019| the current available limit is ''{{.replaceKey0}}'' USDT"  
170031| The feature has been suspended  
170032| Network error. Please try again later  
170033| margin Insufficient account balance  
170034| Liability over flow in spot leverage trade!  
170035| Submitted to the system for processing!  
170036| You haven't enabled Cross Margin Trading yet. To do so, please head to the PC trading site or the Bybit app  
170037| Cross Margin Trading not yet supported by the selected coin  
170105| Parameter '%s' was empty.  
170115| Invalid timeInForce.  
170116| Invalid orderType.  
170117| Invalid side.  
170121| Invalid symbol.  
170124| Order amount too large.  
170130| Data sent for paramter '%s' is not valid.  
170131| Balance insufficient  
170132| Order price too high.  
170133| Order price lower than the minimum.  
170134| Order price decimal too long.  
170371| Order price cannot be lower than {}, the price limitation  
170372| Order price cannot be higher than 0, the price limitation  
170381| Order quantity too large.  
170382| Order quantity too large.  
170136| Order quantity lower than the minimum.  
170137| Order volume decimal too long  
170139| Order has been filled.  
170140| Order value exceeded lower limit  
170141| Duplicate clientOrderId  
170142| Order has been cancelled  
170143| Cannot be found on order book  
170144| Order has been locked  
170145| This order type does not support cancellation  
170146| Order creation timeout  
170147| Order cancellation timeout  
170148| Market order amount decimal too long  
170149| Create order failed  
170150| Cancel order failed  
170151| The trading pair is not open yet  
170157| The trading pair is not available for api trading  
170159| Market Order is not supported within the first %s minutes of newly launched pairs due to risk control.  
170190| Cancel order has been finished  
170191| Can not cancel order, please try again later  
170192| Order price cannot be higher than %s .  
170193| Buy order price cannot be higher than %s.  
170194| Sell order price cannot be lower than %s.  
170195| Please note that your order may not be filled. ETP buy order price deviates from risk control  
170196| Please note that your order may not be filled. ETP sell order price deviates from risk control  
170197| Your order quantity to buy is too large. The filled price may deviate significantly from the market price. Please try again  
170198| Your order quantity to sell is too large. The filled price may deviate significantly from the market price. Please try again  
170199| Your order quantity to buy is too large. The filled price may deviate significantly from the nav. Please try again.  
170200| Your order quantity to sell is too large. The filled price may deviate significantly from the nav. Please try again.  
170201| Invalid orderFilter parameter  
170202| Please enter the TP/SL price.  
170203| trigger price cannot be higher than 110% price.  
170204| trigger price cannot be lower than 90% of qty.  
170206| Stop_limit Order is not supported within the first 5 minutes of newly launched pairs  
170207| The loan amount of the platform is not enough.  
170209| This trading pair is only available to the xxx, yyyy,etc region.  
170210| New order rejected.  
170212| Cancel order request processing  
170213| Order does not exist.  
170215| Spot Trading (Buy) Restriction: The current LTV ratio of your institutional lending has reached the maximum allowable amount for buy orders  
170216| The leverage you select for Spot Trading cannot exceed the maximum leverage allowed by Institutional Lending  
170217| Only LIMIT-MAKER order is supported for the current pair.  
170218| The LIMIT-MAKER order is rejected due to invalid price.  
170219| UID {{xxx}} is not available to this feature  
170220| Spot Trading Restriction: The current LTV ratio of your institutional lending has reached the maximum allowable amount for Spot trading  
170221| This coin does not exist.  
170222| Too many requests in this time frame.  
170223| Your Spot Account with Institutional Lending triggers an alert or liquidation.  
170224| You're not a user of the Innovation Zone.  
170226| Your Spot Account for Margin Trading is being liquidated.  
170227| This feature is not supported.  
170228| The purchase amount of each order exceeds the estimated maximum purchase amount.  
170229| The sell quantity per order exceeds the estimated maximum sell quantity.  
170230| Operations Restriction: Due to the deactivation of Margin Trading for institutional loan  
170234| System Error  
170241| To proceed with trading, users must read through and confirm that they fully understand the project's risk disclosure document. For App users, please update your Bybit App to version 4.16.0 to process.  
170310| Order modification timeout  
170311| Order modification failed  
170312| The current order does not support modification  
170313| The modified contract quantity cannot be less than to the filled quantity  
170341| Request order quantity exceeds maximum limit  
170344| Symbol is not supported on Margin Trading  
170348| Please go to (<https://www.bybit-tr.com>) to proceed.  
170355| RPI orders are restricted to approved market makers only  
170358| The current site does not support ETP  
170359| TThe current site does not support leveraged trading  
170709| OTC loan: The select trading pair is not in the whitelist pair  
170810| Cannot exceed maximum of 500 conditional, TP/SL and active orders.  
  
## Spot Margin Trade

Code| Description  
---|---  
176002| Query user account info error. Confirm that if you have completed quiz in GUI  
176003| Query user loan history error  
176004| Query order history start time exceeds end time  
176005| Failed to borrow  
176006| Repayment Failed  
176007| User not found  
176008| You haven't enabled Cross Margin Trading yet. To do so, please head to the PC trading site  
176009| You haven't enabled Cross Margin Trading yet. Confirm that if you have turned on margin trade  
176010| Failed to locate the coins to borrow  
176011| Cross Margin Trading not yet supported by the selected coin  
176012| Pair not available  
176013| Cross Margin Trading not yet supported by the selected pair  
176014| Repeated repayment requests  
176015| Insufficient available balance  
176016| No repayment required  
176017| Repayment amount has exceeded the total liability  
176018| Settlement in progress  
176019| Liquidation in progress  
176020| Failed to locate repayment history  
176021| Repeated borrowing requests  
176022| Coins to borrow not generally available yet  
176023| Pair to borrow not generally available yet  
176024| Invalid user status  
176025| Amount to borrow cannot be lower than the min. amount to borrow (per transaction)  
176026| Amount to borrow cannot be larger than the max. amount to borrow (per transaction)  
176027| Amount to borrow cannot be higher than the max. amount to borrow per user  
176028| Amount to borrow has exceeded Bybit's max. amount to borrow  
176029| Amount to borrow has exceeded the user's estimated max. amount to borrow  
176030| Query user loan info error  
176031| Number of decimals for borrow amount has exceeded the maximum precision  
176034| The leverage ratio is out of range  
176035| Failed to close the leverage switch during liquidation  
176036| Failed to adjust leverage switch during forced liquidation  
176037| For non-unified transaction users, the operation failed  
176038| The spot leverage is closed and the current operation is not allowed  
176039| Borrowing, current operation is not allowed  
176040| There is a spot leverage order, and the adjustment of the leverage switch failed!  
176132| Number of decimals for repay amount has exceeded the maximum precision  
176133| Liquidation may be triggered! Please adjust your transaction amount and try again  
176134| Account has been upgraded (upgrading) to UTA  
176135| Failed to get bond data  
176136| Failed to get borrow data  
176137| Failed to switch user status  
176138| You need to repay all your debts before closing your disabling cross margin account  
176139| Sorry, you are not eligible to enable cross margin, as you have already enabled OTC lending  
176201| Account exception. Check if the UID is bound to an institutional loan  
182021| Cannot enable spot margin while in isolated margin mode. Please switch to cross margin mode or portfolio margin mode to trade spot with margin.  
182104| This action could not be completed as your Unified Margin Account's IM/MM utilization rate has exceeded the threshold  
182105| Adjustment failed, user is upgrading  
182106| Adjustment failed, user forced liquidation in progress.  
182107| Adjustment failed, Maintenance Margin Rate too high  
  
## Asset

Code| Description  
---|---  
131001| openapi svc error  
131002| Parameter error  
131002| Withdraw address chain or destination tag are not equal  
131003| Internal error  
131004| KYC needed  
131065| Your KYC information is incomplete, please go to the KYC information page of the web or app to complete the information. kyc=India client may encounter this  
131066| This address does not support withdrawals for the time being. Please switch to another address for withdrawing  
131067| Travel rule verification failed, please contact the target exchange. Travel rule for KR user  
131068| Travel rule information is insufficient, please provide additional details. Travel rule for KR user  
131069| Unable to withdraw to the receipt, please contact the target the exchange. Travel rule for KR user  
131070| The recipient's name is mismatched with the targeted exchange. Travel rule for KR user  
131071| The recipient has not undergone KYC verification. Travel rule for KR user  
131072| Your withdrawal currency is not supported by the target exchange. Travel rule for KR user  
131073| Your withdrawal address has not been included in the target exchange. Travel rule for KR user  
131074| Beneficiary info is required, please refer to the latest api document. Travel rule for KR user  
131075| InternalAddressCannotBeYourself  
131076| internal transfer not support subaccounts  
131077| receive user not exist  
131078| receive user deposit has been banned  
131079| receive user need kyc  
131080| User left retry times is zero  
131081| Do not input memo/tag,please.  
131082| Do not repeat the request  
131083| Withdraw only allowed from address book  
131084| Withdraw failed because of Uta Upgrading  
131085| Withdrawal amount is greater than your availale balance (the deplayed withdrawal is triggered)  
131086| Withdrawal amount exceeds risk limit (the risk limit of margin trade is triggered)  
131087| your current account spot risk level is too high, withdrawal is prohibited, please adjust and try again  
131088| The withdrawal amount exceeds the remaining withdrawal limit of your identity verification level. The current available amount for withdrawal : %s  
131089| User sensitive operation, withdrawal is prohibited within 24 hours  
131090| User withdraw has been banned  
131091| Blocked login status does not allow withdrawals  
131092| User status is abnormal  
131093| The withdrawal address is not in the whitelist  
131094| UserId is not in the whitelist  
131095| Withdrawl amount exceeds the 24 hour platform limit  
131096| Withdraw amount does not satify the lower limit or upper limit  
131097| Withdrawal of this currency has been closed  
131098| Withdrawal currently is not availble from new address  
131099| Hot wallet status can cancel the withdraw  
131200| Service error  
131201| Internal error  
131202| Invalid memberId  
131203| Request parameter error  
131204| Account info error  
131205| Query transfer error  
131206| cannot be transfer  
131207| Account not exist  
131208| Forbid transfer  
131209| Get subMember relation error  
131210| Amount accuracy error  
131211| fromAccountType can't be the same as toAccountType  
131212| Insufficient balance  
131213| TransferLTV check error  
131214| TransferId exist  
131215| Amount error  
131216| Query balance error  
131217| Risk check error  
131226| Due to security reasons, we are unable to proceed with the current action. Should you have any enquiries, please reach out to our Customer Support  
131227| subaccount do not have universal transfer permission  
131228| your balance is not enough. Please check transfer safe amount  
131229| Due to compliance requirements, the current currency is not allowed to transfer  
131230| The system is busy, please try again later  
131231| Transfers into this account are not supported  
131232| Transfers out this account are not supported  
131233| can not transfer the coin that not supported for islamic account  
131239| The collateral amount has exceeded the platform limit. Please disable the collateral for this asset, or transfer in another supported asset as collateral.  
140001| Switching the PM spot hedging switch is not allowed in non PM mode  
~~140002~~| ~~Institutional lending users do not support PM spot hedging~~  
140003| You have position(s) being liquidated, please try again later.  
140004| Operations Restriction: The current LTV ratio of your Institutional Loan has hit the liquidation threshold. Assets in your account are being liquidated.  
140005| Risk level after switching modes exceeds threshold  
141004| sub member is not normal  
141019| To add or update the IP whitelist, go to API management and select Edit  
141020| To change read and write permissions for sensitive actions, go to API management and select Edit  
141025| This subaccount has assets and cannot be deleted  
141027| Sub account cannot accept agreement  
181000| category is null  
181001| category only support linear or option or spot.  
181002| symbol is null.  
181003| side is null.  
181004| side only support Buy or Sell.  
181005| orderStatus is wrong  
181006| startTime is not number  
181007| endTime is not number  
181008| Parameter startTime and endTime are both needed  
181009| Parameter startTime needs to be smaller than endTime  
181010| The time range between startTime and endTime cannot exceed 7 days  
181011| limit is not a number  
181012| symbol not exist  
181013| Only support settleCoin: usdc  
181014| Classic account is not supported  
181018| Invalid expDate.  
181019| Parameter expDate can't be earlier than 2 years  
182000| symbol related quote price is null  
182200| Please upgrade UTA first.  
182201| You must enter 2 time parameters.  
182202| The start time must be less than the end time  
182203| Please enter valid characters  
182204| Coin does not exist  
182205| User level does not exist  
700000| accountType/quoteTxId cannot be null  
700001| quote fail:no dealer can used  
700004| order does not exist  
700007| Large Amount Limit  
700012| UTA upgrading, don't allow to apply for quote  
  
### Fiat Convert

Code| Description  
---|---  
400000| invalid request.  
400001| broker not found.  
400002| broker invalid.  
400003| broker quotation invalid.  
400004| sub-account doesn't exist.  
400005| request amount out of quota limit.  
400006| funding account not sufficient funds.  
400007| sub-account funding account not sufficient funds.  
500000| bybit internal error.  
  
### Convert Small Balances

Code| Description  
---|---  
790000| system error. please try again later  
790001| sign verification failed  
700000| params error  
700001| quote fail:no dealer can used  
700002| quote fail:not support quote type  
700004| order not exist  
700005| Your Available Balance is insufficient or your wallet not exist  
700006| Low amount limit  
700007| Large amount limit  
700008| quote fail: price time out  
700009| quoteTxId has already been used  
700010| loan user can not perform conversion  
700011| illegal operation  
700012| uta upgrading, convert unavailable.  
700013| the current coin does not support convert  
700016| rate is less than current rate  
700021| exist processing exchange order, please try again later  
700022| This operation is not currently supported  
  
## Crypto Loan (New)

Code| Description  
---|---  
148001| This currency is not supported for flexible savings.  
148002| The entered amount is below the minimum borrowable amount.  
148003| Exceeds the allowed decimal precision for this currency.  
148004| This currency cannot be used as collateral.  
148005| Exceeds the allowed decimal precision for this collateral currency.  
148006| The amount of collateral exceeds the upper limit of the platform.  
148007| Borrow amount cannot be negative.  
148008| Collateral amount cannot be negative.  
148009| LTV exceeds the risk threshold.  
148010| Insufficient available quota.  
148011| Insufficient balance in the funding pool .  
148012| Insufficient collateral amount.  
148013| Non-borrowing users cannot adjust collateral.  
148014| This currency is not supported.  
148015| Loan term exceeds the allowed range.  
148016| The specified lending rate is not supported.  
148017| The interest rate exceeds the allowed decimal precision.  
148018| Exceeded the maximum number of open orders.  
148019| The system is busy, please try again later.  
148020| Insufficient platform lending quota.  
148021| Operation conflict detected. Please try again later.  
148022| Insufficient assets for lending.  
148023| Loan order not found.  
148024| Loan cancellation failed: the order may have been completed or has an invalid amount.  
148025| Lending order cancellation failed: the order may have been completed or has an invalid amount.  
148026| Failed to create repayment. Please try again later.  
148027| No active loan found for this account. Operation not allowed.  
148028| Repayment amount exceeds the supported precision for the currency.  
148029| Insufficient balance in the repayment account.  
148030| Deposit order not found.  
148031| Operation not allowed during liquidation.  
148032| No outstanding debt. Repayment is not allowed.  
148033| This loan order cannot be repaid.  
148034| Please wait and try again later.  
148035| Please wait and try again later.  
148036| Failed to adjust collateral amount. Please try again later.  
148037| Insufficient assets or adjustment amount exceeds the maximum allowed.  
148038| Repayment amount cannot exceed the debt amount of the position.  
148039| Duplicate collateral assets detected. Please review and resubmit.  
148040| Pledge token is error.  
148041| Repay order is exist.  
148042| Exceeds the allowed decimal precision for this currency.  
148047| The request collateral amount exceeds the maximum allowed. upper limit (initial limit: 300,000 USD-equivalent per repayment)  
148048| The collateral amount has exceeded the platform limit. Please transfer in other supported assets as collateral.  
148049| kyc region is not supported  
  
## Crypto Loan (legacy)

Code| Description  
---|---  
177002| Server is busy, please wait and try again  
177003| Illegal characters found in a parameter  
177004| Precision is over the maximum defined for this asset  
177005| Order does not exist  
177006| We don't have this asset  
177007| Your borrow amount has exceed maximum borrow amount  
177008| Borrow is banned for this asset  
177009| Borrow amount is less than minimum borrow amount  
177010| Repay amount exceeds borrow amount  
177011| Balance is not enough  
177012| The system doesn't have enough asset now  
177013| adjustment amount exceeds minimum collateral amount  
177014| Individual loan quota reached  
177015| Collateral amount has reached the limit. Please reduce your collateral amount or try with other collaterals  
177016| Minimum collateral amount is not enough  
177017| This coin cannot be used as collateral  
177018| duplicate request  
177019| Your input param is invalid  
177020| The account does not support the asset  
177021| Repayment failed  
  
## Institutional Loan

Code| Description  
---|---  
3777002| UID cannot be bound repeatedly.  
3777003| UID cannot be unbound because the UID has not been bound to a risk unit.  
3777004| The main UID of the risk unit cannot be unbound.  
3777005| You have unsettled lending or borrowing orders. Please try again later.  
3777006| UID cannot be bound, please try again with a different UID."  
3777007| UID cannot be bound, please upgrade to UTA Pro."  
3777012| Your request is currently being processed. Please wait and try again later  
3777027| UID cannot be bound, leveraged trading closure failed.  
3777029| You currently have orders for pre-market trading that can’t be bind UIDs  
3777030| This account has activated copyPro and cannot bind uid  
3777039| The repayment amount exceeds the outstanding debt, or there is no outstanding liability.  
3777040| Insufficient balance.  
3777042| The uid is invalid  
3777043| There is a repayment order currently being processed. Please try again later.  
3777045| Account exception: the account is not an institutional lending account.  
  
## Exchange Broker

Code| Description  
---|---  
3500402| Parameter verification failed for 'limit'.  
3500403| Only available to exchange broker main-account  
3500404| Invalid Cursor  
~~3500405~~|  Parameter "startTime" and "endTime" need to be input in pairs.  
3500406| Out of query time range.  
3500407| Parameter begin and end need to be input in pairs.  
3500415| Sub-accounts are not permitted to perform this action.  
  
### Reward

Code| Description  
---|---  
400001| invalid parameter  
400101| The voucher was recycled  
400102| The voucher has exceeded the redemption date (expired)  
400103| The voucher is not available for redemption  
400105| Budget exceeded  
403001| Account rejected, check if the input accountId valid, account banned, or kyc issue  
404001| resource not found  
404011| Insufficient inventory  
409011| VIP level limit  
500001| Internal server error  
  
## Earn

Code| Description  
---|---  
180001| Invalid parameter  
180002| Invalid coin  
180003| User banned  
180004| Site not allowed. Only users from Bybit global site can access  
180005| Compliance wallet not reach  
180006| Validation failed  
180007| Product not available  
180008| Invalid Product  
180009| product is forbidden  
180010| User not allowed  
180011| User not VIP  
180012| Purchase share is invalid  
180013| Stake over maximum share  
180014| Redeem share invlaid  
180015| Products share not enough  
180016| Balance not enough  
180017| Invalid risk user  
180018| internal error  
180019| empty order link id  
180020| Position not found  
180021| Invalid select price  
180022| Kyc level not reached  
180023| Service maintenance  
180024| Child member forbidden  
180025| Order already exists  
180026| Apr lowered  
180027| Tax forbidden  
180028| Reinvest validation failed  
180029| Redeem not allowed  
180030| Slippage fail  
180031| Duplicate order  
  
## User

Code| Description  
---|---  
81007| Bybit Europe is not supported create API Key  
20096| need KYC authentication  
  
## Set API rate limit

Code| Description  
---|---  
3500002| Current user is not an institutional user  
3500153| No permission to operate these UIDs  
3500153| You do not have permission to query other UIDs  
  
## RFQ

Code| Description  
---|---  
110300| The RFQ order does not exist  
110301| The Quote order does not exist  
110302| Demo user is prohibited  
110303| RFQ value is less than the min limit  
110304| Cannot be self-executed  
110305| Quote UID is not in counterparties  
110306| Quote legs do not match  
110307| Quote order already exists for this RFQ  
110308| RFQ strategy legs size is not correct  
110309| RFQ strategy side is not correct  
110310| RFQ strategy qty is not correct  
110311| RFQ strategy symbol is not correct  
110312| No permission to execute quote  
110313| RFQ only supports one-way position mode  
110314| Order amount is less than min trade amount  
110315| Order qty exceeds the upper limit  
110316| RFQ is not available for Copy Trading  
110317| Counterparty cannot be self  
110318| There are too many counterparties to choose from  
110319| Order amount is greater than max trade amount  
110320| Symbols that have not enabled manual loan are not supported  
110321| Symbol is not supported  
110323| Quotations cannot be made by non-ByBit registration institutions  
111008| The spot asset is not be enabled as collateral asset  
  
## Manual Loan

Code| Description  
---|---  
34022001| System error. Please try again later.  
34022003| System error. Please try again later.  
34022027| Invalid request parameters.  
34022030| Borrowing demand is high, and the fund pool is currently low. Please wait a moment.  
34022031| Risk rate limit exceeded. Please reduce your borrow amount in the Unified Trading Account.  
34022033| Borrowing precision must be an integer multiple.  
34022034| The minimum repayment amount must be an integer multiple.  
34022035| You cannot repay while interest is being calculated.  
34022036| Please enable Margin Trading to continue.  
34022038| Repayment is in progress. Please do not repeat the operation.  
34022010| The borrowed asset does not exist.  
34022041| Currently, your account has no borrowed coins. No repayments are needed.  
34022044| Repayment unsuccessful.  
34022045| Borrowing unsuccessful.  
34022011| Amount must be at least.  
34022014| Decimal precision cannot exceed 18 digits.  
34022047| CopyTrade not supported.  
34022048| Borrowing is not allowed during liquidation.  
34022049| Insufficient collateral balance.  
34022050| Repayment failed. You currently have spot hedging liabilities. Please close your derivatives positions before repayment.  
34022051| Institutional loan in progress.  
34022052| Institutional loan transactions banned.  
35000011| You have existing pending loan orders. Please try again later.  
34022053| Please contact the sales to enable the manual borrowing feature.  
34022094| This coin does not support repayment through coin exchange.  
34022107| To use this feature, your net liability value must be below %s USD. Otherwise, please repay through spot trading or deposit funds first. (For all coin repayment)  
34022108| To use this feature, your net liability value must be below %s USD. Otherwise, please repay through spot trading or deposit funds first. (For single coin repayment)  
  
## Tax

Code| Description  
---|---  
10001| Invalid request parameters, including invalid timestamps, an invalid time range, no valid `type`/`number` items, or a batch ID that does not exist or is not accessible to the current user.  
10007| User is not logged in.  
20000| Batch not found for the authenticated user.  
20001| Database write or query failed.  
400004| An unfinished batch exists. A new batch cannot be submitted.  
  
## Strategy

Code| Description  
---|---  
60061| Strategy creation failed / webhook strategy name is empty  
60062| Strategy has been terminated / Can't stop sub strategy  
60063| user running symbol strategy count limited  
60064| user running strategy count limited  
60065| Strategy not found  
60066| size should more than {minSize} / sub size should more than {minSize}  
60067| too large size / size should less than {maxSize} / sub size should less than {maxSize}  
60068| Order cancelled  
60069| hit blacklist rule  
60070| Blocked by unified margin limit  
60071| Get conn err / Trading service unavailable  
60072| Strategy status modify failed  
60073| Webhook order creation failed  
60074| strategy has been stopped  
60075| Webhook positionidx is not supported  
60076| Signal latency too high  
60077| strategy userId invalid / strategy json invalid / strategy StrategyID invalid  
60078| strategy symbol not supported  
60079| User position limit exceeded  
60080| Order retry failed  
60081| can't create same sides order  
60082| iceberg not support usdc / chase order not support usdc  
60083| strategy symbol not supported  
60084| Invalid post only parameter  
60085| Quantity is less than minimum order quantity  
60086| Position percentage does not match side  
60087| Quantity exceeds allowed range  
60088| POV invalid mode  
60089| POV participation rate over the range or over 1 decimal  
60090| POV lack of required param at the different modes  
60091| POV lack of size and duration when interval > 0  
60092| POV pre-checked failed due to calculated sub size over [minQty, maxQty]  
60093| POV max duration over the range  
60094| POV pre-checked sub order size over the one order size  
60095| POV interval over the max duration  
61000| Signal symbol not tradable  
61001| Signal name exceeds limit  
61002| Signal leverage exceeds maximum risk limit  
61003| Signal entry price invalid  
61004| Signal TP should be better than worst price  
61005| Signal SL should be worse than best price  
61006| Signal expiration time invalid  
61007| Signal description exceeds limit  
61008| SL is worse than liquidation price  
61009| Signal not found  
61010| User does not have permission to create signal  
60200| the qty of twap inverse step position value is less than minOrderQty / the qty of iceberg inverse sub position value is less than minOrderQty / the qty of chase inverse position value is less than minOrderQty / strategy stepPositionValue less than minNationValue / iceberg sub position value is less than minNationValue / chase position value is less than minNationValue  
60201| the qty of twap inverse step position value exceeds maxOrderQty / the qty of iceberg inverse sub position value exceeds maxOrderQty / the qty of chase inverse position value exceeds maxOrderQty / the qty of iceberg inverse total position value exceeds maxTotalQty / iceberg sub position value exceeds max value / iceberg total position value exceeds maxTotalValue / twap step position value exceeds max value / chase position value exceeds max value  
  
## Prediction

Code| Description  
---|---  
180000| Internal server error  
180001| Invalid request parameter  
700001| Prediction market not found or closed  
700002| Insufficient liquidity for FOK order  
700003| Prediction engine unavailable  
700010| Insufficient USDC balance  
700011| Insufficient token position

---

# 錯誤碼

## HTTP 響應碼

響應碼| 描述  
---|---  
400| Bad request. 請檢查您的請求方式是否為**GET** / **POST** (必需大寫)  
[401](/docs/zh-TW/pilot-feature#v5%E6%8E%A5%E5%8F%A3%E6%94%AF%E6%8C%81%E7%B6%93%E5%85%B8%E5%B8%B3%E6%88%B6)| 無效請求. 1. 請檢查是否為正確的API密鑰; 2. 請檢查是否將鑒權參數放在了請求頭裡  
403| Forbidden request. 可能原因: 1. 違反了IP請求速率; 2. 您的GET請求裡帶了空的json體; 3. 您的請求發送自美國IP  
[404](/docs/zh-TW/pilot-feature#v5%E6%8E%A5%E5%8F%A3%E6%94%AF%E6%8C%81%E7%B6%93%E5%85%B8%E5%B8%B3%E6%88%B6)| 無法找到路由. 可能原因: 1. 請檢查您的路由; 2. 帳戶模式不支持請求的category值  
429| 觸發系統層面的頻率保護, 請嘗試重試  
  
## WS下單通用錯誤碼

響應碼| 描述  
---|---  
10404| 1\. op類型未找到; 2. `category`不支持/未找到  
10429| 觸發系統級別的頻率保護  
10003| 同一個uid上構建了過多會話  
10016| 1.內部錯誤; 2. 服務重啟  
10019| ws下單服務正在重啟, 拒絕新的請求, 正在處理中的請求不受影響. 您可以重新/新建連接, 會分配到正常的服務上  
20003| Too frequent requests under the same session  
20006| `reqId`重複  
  
## 統一帳戶

錯誤碼| 描述  
---|---  
0| OK  
429| 交易服務負載過高, 遇到後可以發起重試  
-2015| (現貨) Your api key has expired API key已經過期  
33004| (衍生品) Your api key has expired API key已經過期  
10000| 服務超時  
10001| 請求參數錯誤。  
10002| 請求時間超出了時間視窗範圍。  
10003| API金鑰無效。檢查使用的key是否與域名匹配, 共有4類環境: 主網mainnet, 測試網testnet, 主網模擬盤, 測試網模擬盤  
10004| 錯誤簽名，請檢查簽名生成算灋。  
10005| 許可權被拒絕，請檢查您的API金鑰許可權。  
10006| 訪問次數太多。 超過API速率限制。  
10007| 用戶身份驗證失敗。  
10008| 當前帳戶模式無法訪問，請檢查您的帳戶模式  
10009| Service Restricted: Access is currently unavailable for your region. Please contact our support team for further assistance 您的IP屬於限制地區  
10010| IP不匹配，請檢查API金鑰的綁定IP地址。  
10014| 無效的重複請求。  
10016| 系統錯誤。  
10017| 未找到路由。  
~~10018~~| ~~超過IP速率限制。~~  
10024| 合規牆攔截。  
10027| 禁止交易。  
10028| API只能由統一帳戶用戶訪問。  
10029| 交易對白名單限制，請求的交易對無效。  
100028| 統一帳戶用戶無法訪問API。  
30035| Options: Too fast to cancel, Try it later  
30133| OTC loan: The symbol you select for USDT Perpetual is not allowed by Institutional Lending 下單交易對不在機構借貸白名單內  
30134| OTC loan: The symbol you select for USDC Contract is not allowed by Institutional Lending 下單交易對不在機構借貸白名單內  
30135| The leverage you select for USDT Perpetual trading cannot exceed the maximum leverage allowed by Institutional Lending. 可設置的槓桿倍數不能超過機構借貸的上限  
30136| The leverage you select for USDC Perpetual or Futures trading cannot exceed the maximum leverage allowed by Institutional Lending. 可設置的槓桿倍數不能超過機構借貸的上限  
30208| Failed to submit order(s). The order price is higher than the maximum buying price 提交訂單失敗，訂單價格高於最高買入價  
30209| Failed to submit order(s). The order price is lower than the minimum selling price.提交訂單失敗，訂單價格高於最高賣出價  
30228| No new positions during delisting 下架期間不能開倉  
30256| Margin limit exceeded. The maintenance margin required for this order exceeds the available risk margin under current LTV constraints (現貨)  
40004| the order is modified during the process of replacing 訂單已經到達終態, 無法修改  
110001| 訂單不存在  
110003| 訂單價格超出[允許範圍](https://www.bybithelp.com/zh-MY/s/article/Contract-Price-Limits)。  
110004| 錢包餘額不足  
110005| 倉位狀態  
110006| 估計資產無法彌補頭寸差額  
110007| 可用餘額不足  
110008| 訂單已完成或取消。  
110009| 停止訂單的數量超過了允許的最大限制。 您可以從我們的OpenAPI檔案中找到參攷。  
110010| 訂單已取消  
110011| 此調整將立即觸發清算  
110012| 可用餘額不足。  
110013| 由於風險限制級別，無法設定杠杆。  
110014| 可用餘額不足，無法添加額外保證金。  
110015| 該倉位處於全倉保證金模式。  
~~110016~~| ~~請求的合約數量超過了風險限額，請在重試之前調整風險限額級別~~  
110017| 不滿足ReduceOnly規則。  
110018| 用戶id非法。  
110019| 訂單id非法。  
110020| 不允許有超過500個活動訂單。  
110021| 由於未平倉，不允許超過持倉限額。  
110022| 數量已受到限制，無法修改訂單以新增數量。  
110023| 現時你只能减少你在這份合約上的頭寸。 請查看我們的公告或聯系客服瞭解詳情。  
110024| 您有一個持倉，因此無法切換位置模式。  
110025| 倉位模式尚未修改。  
110026| 全倉/逐倉模式尚未修改。  
110027| 保證金尚未修改。  
110028| 您已有未結訂單，因此無法切換倉位模式。  
110029| 此符號不支持對沖模式。  
~~110030~~| ~~訂單ID重複~~  
110031| 不存在風險限額資訊，請檢查風險限額規則。  
110032| 訂單不合法  
110033| 沒有未平倉頭寸，您無法設定保證金  
110034| 沒有淨頭寸  
110035| 清算前未完成訂單取消  
110036| 由於交叉保證金模式，您不允許更改杠杆。  
110037| 用戶設置清單沒有此交易對  
110038| 由於投資組合保證金模式，您不允許更改杠杆率。  
110039| 維護保證金率過高。 這可能引發清算。  
110040| 訂單將觸發強制清算，請重新提交訂單。  
110041| 當存在倉位或maker訂單時，不允許跳過清算  
110042| 現時，由於預交割狀態，您只能减少您在本合約中的頭寸。  
110043| 設定杠杆尚未修改。  
110044| 可用保證金不足。  
110045| 錢包餘額不足。  
110046| 此調整將立即觸發清算。  
110047| 由於可用保證金不足，無法調整風險限額。  
110048| 由於當前/預期頭寸值超過修訂後的風險限額，因此無法調整風險限額。  
110049| tick note只能是數位  
110050| 無效的幣種  
110051| 用戶的可用餘額不能覆蓋當前市場的最低價格  
110052| 您的可用餘額不足以設定價格  
110053| 用戶可用餘額不能覆蓋當前市場價格和上限價格  
110054| 此倉位至少有一個獲利連結訂單，因此無法切換獲利和止損模式  
110055| 此倉位至少有一個止損連結訂單，因此無法切換獲利和止損模式  
110056| 此倉位至少有一個尾隨止損連結訂單，因此無法切換獲利和止損模式  
110057| 條件訂單或限制訂單包含TP/SL相關參數  
110058| 由於剩餘倉位大小不足，您無法設定獲利和止損。  
110059| 不允許修改部分填寫的未結訂單的TP/SL  
110060| 在完全TP/SL模式下，不允許修改TP/SL  
110061| 部分tpSlMode下不允許有超過20個TP/SL  
110062| 未找到該機构的MMP資訊。  
110063| 結算正在進行中！ ｛｛key0｝｝不可用於交易。  
110064| 修改後的契约數量不能小於或等於成交的數量。  
110065| 尚未為您的帳戶啟用MMP。 請聯系您的BD經理。  
110066| 現時不允許交易。  
110067| 不支持統一帳戶。  
110068| 不允許杠杆交易。  
110069| 機構借貸客戶不得交易。  
110070| ETP合約不能交易。  
110071| 抱歉，我們正在修改統一保證金帳戶！ 現時，不支持新的升級。 如果您有任何問題，請聯繫我們的24/7客戶支援。  
110072| OrderLinkedID 不能重複  
110073| 設置保證金模式失敗. 請檢查響應裡的具體原因內容  
110074| This contract is not live 合約已經下架  
~~110075~~| ~~RiskId沒有修改~~  
110076| 僅逐倉保證金下支持自動添加保證金  
110077| 組合保證金模式不支持此操作  
110078| 無法減少過多的保證金  
110079| 訂單正在處理中, 請稍後再試  
110080| Operations Restriction: The current LTV ratio of your Institutional Lending has hit the liquidation threshold. Assets in your account are being liquidated. 目前機構借貸帳戶的LTV達到強平閾值 (交易/杠杆/风险限额等操作)  
110082| You cannot lift Reduce-Only restrictions, as no Reduce-Only restrictions are applied to your position 您的倉位沒有受到Reduce-Only限制, 無需解禁  
110083| Reduce-Only restrictions must be lifted for both Long and Short positions at the same time 對於多空倉位, Reduce-Only 限制需要同時解除  
110085| The risk limit and margin ratio for this contract has been updated, please select a supported risk limit and place your order again 該合約的風險限額和保證金率已經更新, 請使用支持的風險限額並重新下單  
110086| Current order leverage exceeds the maximum available for your current Risk Limit tier. Please lower leverage before placing an order 當前槓桿超過您當前風險限額等級的最大槓桿. 請降低槓桿後再重新下單  
110087| Leverage for Perpetual or Futures contracts cannot exceed the maximum allowed for your Institutional loan 期貨的槓桿不能超過場外借貸產品規定的最大槓桿倍數  
110088| Please Upgrade to UTA to trade 請升級到UTA後再進行交易  
110089| Exceeds the maximum risk limit level 超過了最大風險限額等級  
110090| Order placement failed as your position may exceed the max limit. Please adjust your leverage to {{leverage}} or below to increase the max. position limit 超過了當前風險限額等級支持的最大槓桿  
110092| expect Rising, but trigger_price[XXXXX] <= current[XXXXX]??laste 期望趨勢上行觸發, 但是觸發價格小於當前的市場價格  
110093| expect Falling, but trigger_price[XXXXX] >= current[XXXXX]??last 期望趨勢下行觸發, 但是觸發價格大於當前的市場價格  
110094| Order notional value below the lower limit 訂單最小下單金額小於名義價值金額  
110095| You cannot create, modify or cancel Pre-Market Perpetual orders during the Call Auction. 集合競價每個階段都有不同訂單操作要求  
110096| Pre-Market Perpetual Trading does not support Portfolio Margin mode. 組合保證金模式不支持盤前交易  
110097| Non-UTA users cannot access Pre-Market Perpetual Trading. To place, modify or cancel Pre-Market Perpetual orders, please upgrade your Standard Account to UTA. 經典帳戶不支持盤前交易  
110098| Only Good-Till-Canceled (GTC) orders are supported during Call Auction. 集合競價階段僅支持GTC訂單  
110099| You cannot create TP/SL orders during the Call Auction for Pre-Market Perpetuals. 集合競價階段不支持止盈止損、條件單  
110100| You cannot place, modify, or cancel Pre-Market Perpetual orders when you are in Demo Trading. 模擬交易不支持盤前交易  
110101| Trading inverse contracts under Cross and Portfolio modes requires enabling the settlement asset as collateral. 統一帳戶2.0的全倉/組合保證金模式, 交易反向合約需要預先打開對應幣種的抵押開關  
110102| The user does not support trading Inverse contracts - 帶單交易pro, 機構借貸帳戶暫不支持uta2.0的反向合約交易  
110103| Only Post-Only orders are available at this stage  
110104| The LTV for ins Loan has exceeded the limit, and opening inverse contracts is prohibited 不允許開倉  
110105| The LTV for ins Loan has exceeded the limit, and trading inverse contracts is prohibited 不允許交易  
110106| Restrictions on Ins Loan; inverse contracts are not on the whitelist and are not allowed for trading 合約不在名單內, 無法交易  
110107| Restrictions on ins Loan; leverage exceeding the limit for inverse contracts is not allowed 槓桿超過限定  
110108| Allowable range: 1 to 10000 tick size  
110109| Allowable range: 0.01% to 10%  
110110| Spread trading is not available in isolated margin trading mode 價差交易不支持逐倉模式  
110111| To access spread trading, upgrade to the latest version of UTA 價差交易僅支持UTA2.0  
110112| Spread trading is not available for Copy Trading 帶單不支持價差交易  
110113| Spread trading is not available in hedge mode 價差交易不支持雙向持倉模式  
110114| You have a Spread trading order in progress. Please try again later 不能操作在途狀態的組合訂單  
110115| The cancellation of a combo single-leg order can only be done by canceling the combo order 組合單腿訂單只能被組合訂單撤銷  
110116| The entry price of a single leg, derived from the combo order price, exceeds the limit price 組合單腿訂單價格超過單腿業務訂單價格區間  
110117| The modification of a combo single-leg order can only be done by modifying the combo order 組合單腿訂單只能組合訂單修改  
110118| Unable to retrieve a pruce of the market order due to low liquidity 組合合約沒有盤口，無法定市價  
110119| Order failed. RPI orders are restricted to approved market makers only  
110120| Order price cannot be smaller than xxxx, the price limitation  
110121| Order price cannot be higher than xxxx, the price limitation  
110123| You must agree to the Trading Terms  
110124| Trading is temporarily restricted due to an active cooling-off period. 冷靜期不能開倉  
110125| You must agree to the Trading Terms before trading this contract  
110131| Margin limit exceeded. The maintenance margin required for this order exceeds the available risk margin under current LTV constraints (合約)  
110132| Product not available in your region 韓國kyc/kyb無法交易韓股合約, 英國kyb帳戶僅能交易合規合約  
110134| Trading on this symbol is suspended. Please try again later 交易暫停  
110135| You currently hold a position in an Event Futures contract. Order placement and modification are not supported under Portfolio Margin (PM) mode. Please close the relevant positions before proceeding.  
110136| Event Futures are currently available for trading via OpenAPI to whitelisted accounts only. Your account does not have the required access at this time.  
110137| This Event Futures contract has entered the reduce-only window before settlement. New orders and order modifications are temporarily suspended.  
170346| Settle coin is not a collateral coin, cannot trade settleCoin不是抵押品, 无法交易  
170360| symbol[XXXX] cannot trade 價差交易需要幣種打開抵押品  
3100101| xxx_coin does not exist  
3100181| uid can not be null uid 不能為空  
3100197| 由於升級UTA中, 用戶暫時被封禁  
3200306| 合約下單失敗！您的維持保證金佔用率已超過上限。  
3200316| USDC Options Trading Restriction: The current LTV ratio for your Institutional Lending has reached the maximum allowable amount for USDC Options trading. 目前機構借貸風險水平無法進行期權交易  
3200317| USDC Options Open Position Restriction: The current LTV ratio for your Institutional Lending has reached the maximum allowable amount for opening USDC Options positions.目前機構借貸風險水平無法進行期權買入  
3100326| BaseCoin is required baseCoin必須傳  
3200403| 逐倉保證金模式下無法進行此產品交易  
3200419| Unable to switch to Portfolio margin due to active pre-market Perpetual orders and positions 在有盤前永續訂單和倉位的情況下, 無法切換到PM模式  
3200425| You currently hold a position in an Event Futures contract. Switching to Portfolio Margin (PM) mode is not allowed. Please close the relevant positions before switching. 您目前持有事件合約倉位，無法切換至組合保證金（PM）模式，請先平倉後再切換。  
3200320| Operations Restriction: The current LTV ratio of your Institutional Lending has hit the liquidation threshold. Assets in your account are being liquidated. 目前機構借貸帳戶的LTV達到強平閾值 (修改保证金模式或者现货杠杆时)  
3200641| {{coin}} collateral has reached the platform limit. Disable {{coin}} collateral before switching margin mode. {{coin}} 抵押品已達到平台上限。請先關閉 {{coin}} 的抵押開關，再切換保證金模式。  
3400208| 您有未關閉的雙向持倉或逐倉模式下的USDT永續倉位  
3400209| 有USDT永續倉位時，小時整點的前後10分鐘禁止升級  
3400210| 您合約帳戶當前風險率過高  
3400211| 升級後，帳戶風險率過高  
3400212| 有USDC永續倉位或者期權倉位時，小時整點的前後10分鐘禁止升級  
3400213| 您USDC合約帳戶當前風險率過高  
3400052| 您有未取消的USDC永續掛單  
3400053| 您有未取消的期權掛單  
3400054| 您有未取消的USDT永續掛單  
3400214| 系統處理異常，請稍候再試  
3400071| 您未達到帳戶升級的資產要求，無法完成升級  
3401010| Cannot switch to PM mode 無法切換到PM模式(帶單帳戶嘗試切換到PM模式)  
3400139| The total value of your positions and orders has exceeded the risk limit for a Perpetual or Futures contract 當前PM模式下的倉位超過了全倉或者逐倉的最大允許風險限額  
181017| OrderStatus must be final status 僅支持查詢終態  
182100| Compulsory closing of positions, no repayment allowed 強平清算中, 不支持還款  
182101| Failed repayment, insufficient collateral balance 試算抵押品餘額不足, 還款失敗  
182102| Failed repayment, there are no liabilities in the current currency 該幣種不存在任何負債  
182103| Institutional lending users are not supported 機構借貸用戶不支持一鍵還款  
182108| Switching failed, margin verification failed, please re-adjust the currency status 保證金校驗失敗, 請檢查對應幣種的狀態  
182110| Failed to switch 無法切換  
182111| The requested currency has a non guaranteed gold currency or does not support switching status currencies 請求的幣種是非保證金幣種  
182112| Duplicate currency, please re-adjust 重複的幣種, 請調整後重試  
182011| The {{coin}} collateral amount has reached the platform limit. Enable collateral for another asset, or transfer another supported asset to your account as collateral. {{coin}} 的抵押品金額已達到平台上限。請為其他資產開啟抵押，或將其他支援的資產轉入帳戶作為抵押品。  
182012| Due to regulatory requirements, collateral services are currently unavailable in your region. 由於監管要求，抵押品服務目前在您所在地區不可用。  
  
## 現貨交易

錯誤碼| 描述  
---|---  
170001| openapi內部异常、及調用下游异常會拋出次异常  
170005| 限頻報錯  
170007| 調用下游超時  
170010| 杠杆代幣申購：超出持倉限額  
170011| 下單失敗，當前下單金額已超過該幣種可用額度  
170019| 黑名單用戶  
170031| 該功能已暫停  
170032| 下游熔斷錯誤碼  
170033| 保證金可用額度不足  
170034| 超出限額  
170035| 已提交系統處理（服務超時）  
170036| 未開通全倉杠杆  
170037| 所選幣種未開啟借貸  
170105| 參數為空  
170115| 無效的timeInForce  
170116| 無效的訂單類型  
170117| 無效的買賣方向  
170121| 下游返回的無效幣對  
170124| 訂單金額太大  
170130| 無效入参  
170131| 餘額不足  
170132| 下單價格太高  
170133| 下單價格太小  
170134| 訂單價格精度太大  
170371| Order price cannot be lower than {}, the price limitation 买单价格低于最低价格限制  
170372| Order price cannot be higher than 0, the price limitation 卖单价格高于最高价格限制  
170381| 下單數量太大  
170382| 下單數量太大  
170136| 下單數量太小  
170137| 下單數量精度太大  
170139| 訂單已經成交  
170140| 訂單金額太小  
170141| 重複的clientOrderId  
170142| 訂單已經取消  
170143| 訂單取消時撮合不存在  
170144| 訂單被鎖定  
170145| 訂單類型不能取消  
170146| 下單超時  
170147| 取消訂單超時  
170148| 下單金額精度太大  
170149| 創建訂單失敗（下游發生未知异常）  
170150| 取消訂單失敗（下游發生未知异常）  
170151| 幣對未開放交易  
170157| 幣對不允許openapi交易  
170159| 開盤前五分鐘不允許下普通市價單  
170190| 取消訂單時訂單已經完成  
170191| 取消訂單時訂單狀態  
170192| 盤面風控（開盤後30分鐘）  
170193| 盤面風控限價單買入風控（開盤後前30分鐘）  
170194| 盤面風控片價單賣出風控（開盤後前X分鐘）  
170195| ETP限價單買入偏離值風控  
170196| ETP限價單賣出偏離值風控  
170197| 市價單買入偏離值風控  
170198| 市價單賣出偏離值風控  
170199| ETP市價單買入偏離值風控  
170200| ETP市價單賣出偏離值風控  
170201| 訂單種類錯誤  
170202| 請輸入觸發價格  
170203| 觸發價格大於110%  
170204| 觸發價格小於90%  
170206| 開倉前5分鐘不允許下條件單  
170207| 平台借貸池額度不足  
170209| This trading pair is only available to the xxx, yyyy,etc region. 該交易對僅對限制區域開放  
170210| 下單被拒絕  
170212| Cancel order request processing 正在處理撤單請求  
170213| 訂單不存在  
170215| Spot Trading (Buy) Restriction: The current LTV ratio of your institutional lending has reached the maximum allowable amount for buy orders 限制現貨買入交易, 因您當前機構借貸的LTV已觸發限制現貨買入風控線  
170216| The leverage you select for Spot Trading cannot exceed the maximum leverage allowed by Institutional Lending OTC現貨切換槓桿超過機構借貸允許的槓桿上線  
170217| openapi禁止成交  
170218| limit-maker訂單被拒  
170219| UID {{xxx}} is not available to this feature  
170220| Spot Trading Restriction: The current LTV ratio of your institutional lending has reached the maximum allowable amount for Spot trading 限制現貨交易, 因您當前機構借貸的LTV已觸發限制現貨交易風控線  
170221| 幣種不存在  
170222| 請求過快  
170223| 場外借貸帳戶觸發告警或爆倉  
170224| 非創新區用戶  
170226| 全倉用戶帳戶爆倉中  
170227| 功能未開放  
170228| 買入額度超過預估最大買入額  
170229| 賣出數量超過預估最大賣出量  
170230| Operations Restriction: Due to the deactivation of Margin Trading for institutional loan 機構借貸產品不支持現貨槓桿交易, 因此無法調用開關接口  
170234| 系統錯誤  
170241| To proceed with trading, users must read through and confirm that they fully understand the project's risk disclosure document. For App users, please update your Bybit App to version 4.16.0 to process. 請先去前端頁面完成協議簽署  
170310| Order modification timeout 改單超時  
170311| Order modification failed 改單失敗  
170312| The current order does not support modification 該訂單類型不支持修改  
170313| The modified contract quantity cannot be less than to the filled quantity 修改後訂單數量小於當前已成交數量  
170341| Request order quantity exceeds maximum limit 單次請求的訂單數量超過上限  
170344| Symbol is not supported on Margin Trading 該交易對不支持槓桿交易  
170355| RPI orders are restricted to approved market makers only RPI訂單僅適用於指定做市商  
170358| The current site does not support ETP  
170359| TThe current site does not support leveraged trading  
170709| OTC loan: The select trading pair is not in the whitelist pair 該交易對不在機構借貸現貨交易白名單內  
170810| Cannot exceed maximum of 500 conditional, TP/SL and active orders. 現貨交易,單帳戶單交易對支持最多500個活動單  
  
## 槓桿交易

錯誤碼| 描述  
---|---  
176002| 獲取用戶帳戶信息失敗, 檢查是否已經在web端完成quiz  
176003| 獲取用戶借款紀錄失敗  
176004| 獲取歷史紀錄的startTime大於endTime  
176005| 借款失敗  
176006| 還款失敗  
176007| 未找到借貸帳戶  
176008| 借貸帳戶未開通全倉槓桿,請先在web端完成練習  
176009| 借貸帳戶未打开全倉槓桿, 請先開啟全倉槓桿  
176010| 未找到借貸幣種  
176011| 幣種未開啟借貸  
176012| 未找到交易幣對  
176013| 交易比對未開啟借貸  
176014| 還款請求重複  
176015| 還款帳戶餘額不足  
176016| 無欠款,無需還款  
176017| 還款金額超過欠款金額  
176018| 用戶幣種已在還款中  
176019| 用戶還款計息強平衝突  
176020| 查詢不到還款紀錄  
176021| 借貸請求重複  
176022| 借貸幣種全量未開放  
176023| 交易對全量未開放  
176024| 借貸用戶狀態非正常  
176025| 借貸數量不能小於單詞最小借貸量  
176026| 借貸數量不能大於單次最大借貸量  
176027| 借貸數量不能大於平臺允許的單用戶最大借貸量  
176028| 借貸申請數量超過平臺最大借貸量  
176029| 借款申請數量超過用戶預估最大可借貸量  
176030| 獲取用戶借貸信息失敗  
176031| 借貸精度超過設置精度  
176034| 杠杆倍數超出範圍  
176035| 清算中，關閉杠杆開關失敗  
176036| 强平中，調整杠杆開關失敗  
176037| 非統一交易用戶，操作失敗  
176038| 現貨杠杆為關閉狀態，不允許當前操作  
176039| 借貸中，不允許當前操作  
176040| 存在現貨杠杆訂單，調整杠杆開關失敗！  
176132| 還款精度過高  
176133| 可能觸發爆倉！ 請調整您的交易金額後重試  
176134| 帳戶已經陞級（upgrading）到UTA  
176135| 獲取保證金幣種失敗，請稍後重試  
176136| 獲取借貸幣種失敗，請稍後重試  
176137| 切換全倉狀態失敗，請稍後重試  
176138| 在關閉禁用的全倉保證金帳戶之前，您需要償還所有債務  
176139| 抱歉，您沒有資格啟用全倉保證金，因為您已經啟用了場外借貸  
176201| Account exception. 確認是否是綁定了機構借貸的帳戶  
182021| 逐倉保證金模式下無法啟用槓桿交易. 請切換至全倉保證金或者組合保證金後再使用  
182104| This action could not be completed as your Unified Margin Account's IM/MM utilization rate has exceeded the threshold  
182105| Adjustment failed, user is upgrading  
182106| Adjustment failed, user forced liquidation in progress.  
182107| Adjustment failed, Maintenance Margin Rate too high  
  
## 資產服務

錯誤碼| 描述  
---|---  
131001| openapi svc error 內部服務錯誤  
131002| 參數錯誤  
131002| Withdraw address chain or destination tag are not equal 需要檢查提幣地址是否添加到網頁端的地址簿中, 以及是否存在tag  
131003| 內部錯誤  
131004| 需要KYC認證  
131065| Your KYC information is incomplete, please go to the KYC information page of the web or app to complete the information. kyc=India client may encounter this  
131066| This address does not support withdrawals for the time being. Please switch to another address for withdrawing 目標地址被列入黑名單, 請使用其他地址  
131067| Travel rule verification failed, please contact the target exchange. Travel rule for KR user  
131068| Travel rule information is insufficient, please provide additional details. Travel rule for KR user  
131069| Unable to withdraw to the receipt, please contact the target the exchange. Travel rule for KR user  
131070| The recipient's name is mismatched with the targeted exchange. Travel rule for KR user  
131071| The recipient has not undergone KYC verification. Travel rule for KR user  
131072| Your withdrawal currency is not supported by the target exchange. Travel rule for KR user  
131073| Your withdrawal address has not been included in the target exchange. Travel rule for KR user  
131074| Beneficiary info is required, please refer to the latest api document. Travel rule for KR user  
131075| Internal address cannot be yourself 內部提現時目標UID不能是自身  
131076| internal transfer not support sub-accounts 內部提現不支持提幣到子帳戶  
131077| receive user not exist 接收方UID不再村  
131078| receive user deposit has been banned 接收方被禁止入金  
131079| receive user need kyc 接收方需要做KYC  
131080| User left retry times is zero 所剩的重試次數為0  
131081| Do not input memo/tag,please. 不要輸入memo/tag  
131082| Do not repeat the request 不要重複發送請求  
131083| Withdraw only allowed from address book 僅能提幣到地址簿中的地址  
131084| uta upgrading, and withdraw is prohibited UTA升級中, 無法提現  
131085| 提幣金額大於可用餘額，觸發延遲提幣  
131086| 提幣金額超過風控限制，觸發全倉槓桿限制  
131087| your current account spot risk level is too high, withdrawal is prohibited, please adjust and try again  
131088| 提幣金額超過當前KYC限額，您目前的可提限額是: %s  
131089| 用戶24小時內進行過銘感操作，提現被禁  
131090| 用戶提現封禁  
131091| 用戶登陸封禁，無法提幣  
131092| 用戶狀態異常  
131093| 提幣地址不在白名單內  
131094| 用戶ID不在白名單內  
131095| 提幣金額超過平台24小時限額  
131096| 檢查提幣金額是否滿足最小最大可提金額  
131097| 系統暫停提幣  
131098| 當前時間禁止從新地址提幣  
131099| 當前狀態不支持取消提幣請求  
131200| 服務不可用  
131201| 業務異常  
131202| 用戶ID無效  
131203| 請求參數錯誤  
131204| 帳戶異常  
131205| 查詢劃轉失敗  
131206| 劃轉失敗  
131207| 帳戶不存在  
131208| 劃轉封禁  
131209| 查詢子帳戶關係失敗  
131210| 金額精度錯誤  
131211| 轉入賬戶類型不能作為轉出賬戶類型  
131212| 可用餘額不足  
131213| 當前劃轉能力受到LTV風險率限制  
131214| 劃轉ID已存在  
131215| 金額錯誤  
131216| 查詢余額錯誤  
131217| 風險檢查失敗  
131226| Due to security reasons, we are unable to proceed with the current action. Should you have any enquiries, please reach out to our Customer Support 帳戶有封禁項  
131227| 子帳戶未配置萬能劃轉能力  
131228| 可劃轉餘額不足. 請確認延遲提幣安全限額  
131229| Due to compliance requirements, the current currency is not allowed to transfer 根據合規要求, 該資產不允許劃轉  
131230| The system is busy, please try again later 系統繁忙, 請重試  
131231| Transfers into this account are not supported 限制劃入這個帳戶  
131232| Transfers out this account are not supported 限制劃出這個帳戶  
131233| can not transfer the coin that not supported for islamic account 伊斯蘭帳戶有限制的可劃幣種  
131239| The collateral amount has exceeded the platform limit. Please disable the collateral for this asset, or transfer in another supported asset as collateral. 抵押品金額已超出平台上限。請關閉該資產的抵押，或轉入其他支援的資產作為抵押品。  
140001| Switching the PM spot hedging switch is not allowed in non PM mode 僅支持在組合保證金模式下開啟現貨對衝  
~~140002~~| ~~Institutional lending users do not support PM spot hedging 機構借貸帳戶不支持現貨对冲~~  
140003| You have position(s) being liquidated, please try again later. 您的倉位正在被清算, 請稍候再試  
140004| Operations Restriction: The current LTV ratio of your Institutional Loan has hit the liquidation threshold. Assets in your account are being liquidated.  
140005| Risk level after switching modes exceeds threshold 在啟用或關閉現貨對衝後, 風險水位超出警戒線  
141004| sub member is not normal 可能是帳戶的母子關係不正確  
141019| To add or update the IP whitelist, go to API management and select Edit  
141020| To change read and write permissions for sensitive actions, go to API management and select Edit  
141025| This sub-account has assets and cannot be deleted 該子帳戶存在資產, 無法刪除  
141027| Sub account cannot accept agreement  
181000| category不能為空  
181001| 類別僅支持正向合約，期權或現貨  
181002| symbol不能為空.  
181003| side不能為空.  
181004| side僅支持Buy或者Sell  
181005| orderStatus所填的枚舉值不正確  
181006| startTime所傳入的不是一個數字類型  
181007| endTime所傳入的不是一個數字類型  
181008| 入參startTime和endTime都需要  
181009| 入參startTime應當小於結束時間  
181010| startTime和endTime的間隔不能超過7天  
181011| limit所傳入的不是一個數字類型  
181012| 該交易對名不存在  
181013| 結算幣種僅支持USDC  
181014| Classic account is not supported 經典帳戶不支持  
181018| Invalid expDate. 參數expDate輸入值無效  
181019| Parameter expDate can't be earlier than 2 years 參數expDate不能早於2年  
182000| 交易品種相關報價不能為空  
182200| Please upgrade UTA first 请升级到统一账户  
182201| You must enter 2 time parameters 时间入参必须成对出现  
182202| The start time must be less than the end time 开始时间必须小于结束时间  
182203| Please enter valid characters  
182204| Coin does not exist  
182205| User level does not exist vip等级不存在  
700000| accountType/quoteTxId cannot be null  
700001| quote fail:no dealer can used報價失敗  
700004| order does not exist訂單不存在  
700007| Large Amount Limit大額限制  
700012| UTA升級中, 禁止申請報價  
  
## 法幣閃兌

Code| Description  
---|---  
400000| invalid request. 請求不合法  
400001| broker not found. 未找到 broker  
400002| broker invalid. broker 不合法  
400003| broker quotation invalid. broker 報價不合法  
400004| sub-account doesn't exist. 子帳戶不存在  
400005| request amount out of quota limit. 請求金額超出配額限制  
400006| funding account not sufficient funds. 資金帳戶餘額不足  
400007| sub-account funding account not sufficient funds. 子帳戶資金帳戶餘額不足  
500000| bybit internal error. Bybit 內部錯誤  
  
### 小額兌換

Code| Description  
---|---  
790000| system error. please try again later. 系統錯誤，請稍後再試  
790001| sign verification failed. 簽名驗證失敗  
700000| params error. 參數錯誤  
700001| quote fail: no dealer can used. 報價失敗：無可用的交易商  
700002| quote fail: not support quote type. 報價失敗：不支持的報價類型  
700004| order not exist. 訂單不存在  
700005| Your Available Balance is insufficient or your wallet not exist. 您的可用餘額不足或您的錢包不存在  
700006| Low amount limit. 金額低於最低限制  
700007| Large amount limit. 金額超過最高限制  
700008| quote fail: price time out. 報價失敗：報價超時  
700009| quoteTxId has already been used. quoteTxId 已被使用  
700010| loan user can not perform conversion. 借貸用戶無法執行兌換操作  
700011| illegal operation. 非法操作  
700012| uta upgrading, convert unavailable. 統一錢包正在升級中，暫時無法兌換  
700013| the current coin does not support convert. 當前幣種不支持兌換  
700016| rate is less than current rate. 匯率低於當前匯率  
700021| exist processing exchange order, please try again later. 存在處理中的兌換訂單，請稍後再試  
700022| This operation is not currently supported. 當前暫不支持該操作  
  
## 質押借貸 (新版)

錯誤碼| 描述  
---|---  
148001| This currency is not supported for flexible savings. 此幣種不支援彈性儲蓄。  
148002| The entered amount is below the minimum borrowable amount. 輸入金額低於最低可借金額。  
148003| Exceeds the allowed decimal precision for this currency. 超出該幣種允許的小數精度。  
148004| This currency cannot be used as collateral. 該幣種無法用作抵押品。  
148005| Exceeds the allowed decimal precision for this collateral currency. 超出該抵押幣種允許的小數精度。  
148006| The amount of collateral exceeds the upper limit of the platform. 抵押金額超過平台上限。  
148007| Borrow amount cannot be negative. 借款金額不能為負數。  
148008| Collateral amount cannot be negative. 抵押金額不能為負數。  
148009| LTV exceeds the risk threshold. 質押率（LTV）超過風險閾值。  
148010| Insufficient available quota. 可用額度不足。  
148011| Insufficient balance in the funding pool . 資金池餘額不足。  
148012| Insufficient collateral amount. 抵押金額不足。  
148013| Non-borrowing users cannot adjust collateral. 非借款用戶無法調整抵押品。  
148014| This currency is not supported. 該幣種不被支援。  
148015| Loan term exceeds the allowed range. 借款期限超出允許範圍。  
148016| The specified lending rate is not supported. 指定的出借利率不被支援。  
148017| The interest rate exceeds the allowed decimal precision. 利率超出允許的小數精度。  
148018| Exceeded the maximum number of open orders. 超出最大未完成訂單數量。  
148019| The system is busy, please try again later. 系統忙碌，請稍後重試。  
148020| Insufficient platform lending quota. 平台出借額度不足。  
148021| Operation conflict detected. Please try again later. 操作衝突，請稍後重試。  
148022| Insufficient assets for lending. 出借資產不足。  
148023| Loan order not found. 找不到借款訂單。  
148024| Loan cancellation failed: the order may have been completed or has an invalid amount. 借款訂單取消失敗：訂單可能已完成或金額無效。  
148025| Lending order cancellation failed: the order may have been completed or has an invalid amount. 出借訂單取消失敗：訂單可能已完成或金額無效。  
148026| Failed to create repayment. Please try again later. 創建還款失敗，請稍後重試。  
148027| No active loan found for this account. Operation not allowed. 該帳戶無有效借款，操作不允許。  
148028| Repayment amount exceeds the supported precision for the currency. 還款金額超出該幣種支持的精度。  
148029| Insufficient balance in the repayment account. 還款帳戶餘額不足。  
148030| Deposit order not found. 找不到存款訂單。  
148031| Operation not allowed during liquidation. 清算期間不允許操作。  
148032| No outstanding debt. Repayment is not allowed. 無未償還債務，不允許還款。  
148033| This loan order cannot be repaid. 該借款訂單無法還款。  
148034| Please wait and try again later. 請稍候並重試。  
148035| Please wait and try again later. 請稍候並重試。  
148036| Failed to adjust collateral amount. Please try again later. 調整抵押金額失敗，請稍後重試。  
148037| Insufficient assets or adjustment amount exceeds the maximum allowed. 資產不足或調整金額超過最大允許值。  
148038| Repayment amount cannot exceed the debt amount of the position. 還款金額不可超過該持倉的債務金額。  
148039| Duplicate collateral assets detected. Please review and resubmit. 發現重複的抵押資產，請檢查後重新提交。  
148040| Pledge token is error.質押權杖錯誤。  
148041| Repay order is exist.還款單已存在。  
148042| Exceeds the allowed decimal precision for this currency.超出該幣種允許的小數精度。  
148047| The request collateral amount exceeds the maximum allowed. upper limit (初始限額: 每筆還款額度為 30 萬美元等值金額)  
148048| The collateral amount has exceeded the platform limit. Please transfer in other supported assets as collateral. 抵押品金額已超出平台上限，請轉入其他支援的資產作為抵押品。  
148049| kyc region is not supported kyc地區受限制  
  
## 質押借貸 (舊版)

Code| Description  
---|---  
177002| Server is busy, please wait and try again  
177003| Illegal characters found in a parameter  
177004| Precision is over the maximum defined for this asset  
177005| Order does not exist  
177006| We don't have this asset  
177007| Your borrow amount has exceed maximum borrow amount  
177008| Borrow is banned for this asset  
177009| Borrow amount is less than minimum borrow amount  
177010| Repay amount exceeds borrow amount  
177011| Balance is not enough  
177012| The system doesn't have enough asset now  
177013| adjustment amount exceeds minimum collateral amount  
177014| Individual loan quota reached  
177015| Collateral amount has reached the limit. Please reduce your collateral amount or try with other collaterals  
177016| Minimum collateral amount is not enough  
177017| This coin cannot be used as collateral  
177018| duplicate request  
177019| Your input param is invalid  
177020| The account does not support the asset  
177021| Repayment failed  
  
## 機構借貸

錯誤碼| 描述  
---|---  
3777002| UID cannot be bound repeatedly. UID不能重複綁定  
3777003| UID cannot be unbound because the UID has not been bound to a risk unit. 無法解綁, 因為UID還沒有在風險單元內  
3777004| The main UID of the risk unit cannot be unbound. 風險單元主UID不允許解綁  
3777006| UID cannot be bound, please try again with a different UID." 導致的原因: 1. 請求接口的UID不是風險單元內的UID; 2. 請求接口的UID與被操作的UID不存在母子或子子關係  
3777005| You have unsettled lending or borrowing orders. Please try again later.存在未結算的借出或借入訂單，請稍後重試  
3777007| UID cannot be bound, please upgrade to UTA Pro." UID無法綁定, 請先將該UID升級到統一帳戶  
3777012| Your request is currently being processed. Please wait and try again later 已經提交請求請稍後重試  
3777027| UID cannot be bound, leveraged trading closure failed. UID無法綁定, 因為無法自動關閉槓桿交易  
3777029| You currently have orders for pre-market trading that can’t be bind UIDs 由於當前存在盤前交易訂單，所以無法綁定UID  
3777030| This account has activated copyPro and cannot bind uid 該帳戶已經激活了copy pro, 無法綁定到機構借貸  
3777039| The repayment amount exceeds the outstanding debt, or there is no outstanding liability. 還款金額大於負債或沒有負債  
3777040| Insufficient balance. 餘額不足  
3777042| The uid is invalid 使用的UID非法  
3777043| There is a repayment order currently being processed. Please try again later. 有在途還款單, 請稍候重試  
3777045| Account exception: the account is not an institutional lending account. 帳戶異常：非機構借貸帳戶  
  
## 經紀商

錯誤碼| 描述  
---|---  
3500402| `limit`值校驗失敗. 請檢查是否在支持範圍內  
3500403| 僅適用於經紀商的主帳戶  
3500404| 無效的cursor  
~~3500405~~| `startTime`和`endTime`必須同時傳入  
3500406| Out of query time range. 超過了支持的時間範圍  
3500407| Parameter begin and end need to be input in pairs.  
3500415| Sub-accounts are not permitted to perform this action.  
  
### 卡券

錯誤碼| 描述  
---|---  
400001| invalid parameter 無效入參  
400101| The voucher was recycled 卡券已經被回收  
400102| The voucher has exceeded the redemption date (expired) 卡券已經過期  
400103| The voucher is not available for redemption 卡券還未開始  
400105| Budget exceeded 超出預算  
403001| Account rejected, check if the input accountId valid, account banned, or kyc issue 輸入帳戶無效/被禁/kyc問題  
404001| resource not found  
404011| Insufficient inventory 庫存不足  
409011| VIP level limit VIP等級限制  
500001| Internal server error 系統錯誤  
  
## 理財

Code| Description  
---|---  
180001| Invalid parameter 參數錯誤  
180002| Invalid coin 幣種不存在  
180003| User banned 用戶被封禁  
180004| Site not allowed 本地站用戶不允許購買  
180005| Compliance wallet not reach 用戶不合規  
180006| Validation failed 驗證失敗  
180007| Product not available 產品已下線  
180008| Invalid Product 產品不存在  
180009| product is forbidden 產品被封禁  
180010| User not allowed 用戶驗證失敗  
180011| User not VIP 非VIP用戶不允許購買VIP標籤產品  
180012| Purchase share is invalid 購買份額不符合要求  
180013| Stake over maximum share 購買份額超過最大允許數量  
180014| Redeem share invalid 贖回份額大於持倉數量  
180015| Products share not enough 產品可質押庫存不足  
180016| Balance not enough 餘額不足  
180017| Invalid risk user 非法用戶操作(風控)  
180018| internal error 內部錯誤  
180019| empty order link id orderLinkID不能為空  
180020| Position not found 持倉不存在  
180021| Invalid select price 報價已過期或不在有效報價列表中  
180022| Kyc level not reached KYC等級不滿足產品要求  
180023| Service maintenance 系統維護中  
180024| Child member forbidden 子帳戶禁止操作  
180025| Order already exists 訂單ID已存在  
180026| Apr lowered APR已被調低，低於用戶預期  
180027| Tax forbidden 稅務身份封禁  
180028| Reinvest validation failed 複投失敗  
180029| Redeem not allowed 不允許贖回  
180030| Slippage fail 滑點失敗  
180031| Duplicate order 重複訂單  
  
## 用戶

Code| Description  
---|---  
81007| Bybit Europe is not supported create API Key Bybit歐洲站不支持創建API Key  
20096| need KYC authentication 創建apikey前需要完成KYC或KYB  
  
## 設置API頻率

Code| Description  
---|---  
3500002| Current user is not an institutional user 當前用戶不是機構用戶  
3500153| No permission to operate these UIDs 無權操作這些UID  
3500153| You do not have permission to query other UIDs 您無權查詢其他UID  
  
## RFQ

錯誤碼| 錯誤信息  
---|---  
110300| 該詢價單不存在  
110301| 該報價單不存在  
110302| 禁止使用模擬賬戶  
110303| 詢價金額低於最低限制  
110304| 無法自我成交  
110305| 報價 UID 不在交易對手列表中  
110306| 報價明細不匹配  
110307| 該詢價單已存在相應的報價  
110308| 詢價策略的明細數量不正確  
110309| 詢價策略的方向不正確  
110310| 詢價策略的數量不正確  
110311| 詢價策略的交易對不正確  
110312| 無權執行報價  
110313| 詢價僅支持單向持倉模式  
110314| 訂單金額低於最低交易金額  
110315| 訂單數量超過上限  
110316| 詢價不支持跟單交易  
110317| 交易對手不能為自己  
110318| 可選的交易對手過多  
110319| 訂單金額超過最大交易金額  
110320| 未啟用手動借貸功能的交易對不支持  
110321| 該交易對不支持  
110323| 非 Bybit 註冊機構不得進行報價  
111008| 該現貨未設置為抵押資產  
  
## 手動借貸

錯誤碼| 錯誤信息  
---|---  
34022001| System error. Please try again later. 系統異常  
34022003| System error. Please try again later. 系統異常  
34022027| Invalid request parameters. 請求參數不合法  
34022030| Borrowing demand is high, and the fund pool is currently low. Please wait a moment. 資金池可用餘額不足  
34022031| Risk rate limit exceeded. Please reduce your borrow amount in the Unified Trading Account. 交易校驗不通過  
34022033| Borrowing precision must be an integer multiple. 下單數量精度必須是整數倍  
34022034| The minimum repayment amount must be an integer multiple. 還款數量必須是整數倍  
34022035| You cannot repay while interest is being calculated. 計息中不允許還款  
34022036| Please enable Margin Trading to continue. 現貨槓桿未開啟  
34022038| Repayment is in progress. Please do not repeat the operation. 借還款處理中訂單  
34022010| The borrowed asset does not exist. 不支援的幣種  
34022041| Currently, your account has no borrowed coins. No repayments are needed. 用戶無負債無需還款  
34022044| Repayment unsuccessful. 還款失敗  
34022045| Borrowing unsuccessful. 借款失敗  
34022011| Amount must be at least. 借款數量不能小於最小下單數量  
34022014| Decimal precision cannot exceed 18 digits. 小數精度不能超過18位  
34022047| CopyTrade not supported. copyTrade用戶不允許申請借幣  
34022048| Borrowing is not allowed during liquidation. 強平中  
34022049| Insufficient collateral balance. 試算抵押品餘額不足：還款失敗，抵押品餘額不足  
34022050| Repayment failed. You currently have spot hedging liabilities. Please close your derivatives positions before repayment. 輸入幣種錯誤：“當前幣種不存在負債”  
34022051| Institutional loan in progress. 機構借貸處理中  
34022052| Institutional loan transactions banned. 機構借貸交易封鎖  
35000011| You have existing pending loan orders. Please try again later. 存在撮合中的借款訂單  
34022053| Please contact the sales to enable the manual borrowing feature. 黑名單攔截  
34022094| This coin does not support repayment through coin exchange. 這幣種不支持還有其他coin負債  
34022107| To use this feature, your net liability value must be below %s USD. Otherwise, please repay through spot trading or deposit funds first. 全部還款需兌幣負債超過門檻，無法使用全部還款  
34022108| To use this feature, your net liability value must be below %s USD. Otherwise, please repay through spot trading or deposit funds first. 單幣種還款需兌幣負債超過門檻，無法使用單幣種還款  
  
## 報稅

錯誤碼| 描述  
---|---  
10001| 請求參數無效，包括時間戳無效、時間範圍無效、不存在有效的 `type`/`number` 條目，或批次 ID 不存在或當前用戶無權訪問該批次。  
10007| 用戶未登錄。  
20000| 未找到屬於當前已認證用戶的批次。  
20001| 數據庫寫入或查詢失敗。  
400004| 存在未完成批次，不可提交新批次。  
  
## 策略下單

錯誤碼| 描述  
---|---  
60061| Strategy creation failed / webhook strategy name is empty  
60062| Strategy has been terminated / Can't stop sub strategy  
60063| user running symbol strategy count limited  
60064| user running strategy count limited  
60065| Strategy not found  
60066| size should more than {minSize} / sub size should more than {minSize}  
60067| too large size / size should less than {maxSize} / sub size should less than {maxSize}  
60068| Order cancelled  
60069| hit blacklist rule  
60070| Blocked by unified margin limit  
60071| Get conn err / Trading service unavailable  
60072| Strategy status modify failed  
60073| Webhook order creation failed  
60074| strategy has been stopped  
60075| Webhook positionidx is not supported  
60076| Signal latency too high  
60077| strategy userId invalid / strategy json invalid / strategy StrategyID invalid  
60078| strategy symbol not supported  
60079| User position limit exceeded  
60080| Order retry failed  
60081| can't create same sides order  
60082| iceberg not support usdc / chase order not support usdc  
60083| strategy symbol not supported  
60084| Invalid post only parameter  
60085| Quantity is less than minimum order quantity  
60086| Position percentage does not match side  
60087| Quantity exceeds allowed range  
60088| POV invalid mode  
60089| POV participation rate over the range or over 1 decimal  
60090| POV lack of required param at the different modes  
60091| POV lack of size and duration when interval > 0  
60092| POV pre-checked failed due to calculated sub size over [minQty, maxQty]  
60093| POV max duration over the range  
60094| POV pre-checked sub order size over the one order size  
60095| POV interval over the max duration  
61000| Signal symbol not tradable  
61001| Signal name exceeds limit  
61002| Signal leverage exceeds maximum risk limit  
61003| Signal entry price invalid  
61004| Signal TP should be better than worst price  
61005| Signal SL should be worse than best price  
61006| Signal expiration time invalid  
61007| Signal description exceeds limit  
61008| SL is worse than liquidation price  
61009| Signal not found  
61010| User does not have permission to create signal  
60200| the qty of twap inverse step position value is less than minOrderQty / the qty of iceberg inverse sub position value is less than minOrderQty / the qty of chase inverse position value is less than minOrderQty / strategy stepPositionValue less than minNationValue / iceberg sub position value is less than minNationValue / chase position value is less than minNationValue  
60201| the qty of twap inverse step position value exceeds maxOrderQty / the qty of iceberg inverse sub position value exceeds maxOrderQty / the qty of chase inverse position value exceeds maxOrderQty / the qty of iceberg inverse total position value exceeds maxTotalQty / iceberg sub position value exceeds max value / iceberg total position value exceeds maxTotalValue / twap step position value exceeds max value / chase position value exceeds max value  
  
## Alpha - 預測市場

Code| Description  
---|---  
180000| Internal server error  
180001| Invalid request parameter  
700001| Prediction market not found or closed  
700002| Insufficient liquidity for FOK order  
700003| Prediction engine unavailable  
700010| Insufficient USDC balance  
700011| Insufficient token position  
  
## TM-Onchain

Code| Description| 建議處理  
---|---|---  
390110000| 服務內部異常| 可退避重試  
390110001| 參數錯誤| 檢查請求參數  
390120000| 工單不存在| 確認 `appealId` 是否正確  
390120001| 工單審核中（COMMITTED 狀態）| 無需操作，等待推送通知  
390120002| 工單已過期| 工單無法再提交  
390120003| 工單已完結| 工單處於終態，無需操作