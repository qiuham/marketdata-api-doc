---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#error-code-rest-api-public
anchor_id: error-code-rest-api-public
api_type: REST
updated_at: 2026-07-20 19:37:52.821377
---

# Public

Error Code from 50000 to 53999  
  
  
  
There is a sub-code format used to further distinguish different scenarios within the same type of error. For example, 51008_1000, where 51008 is the error code and 1000 is the error sub-code.

#### General Class

Error Code | HTTP Status Code | Error Message  
---|---|---  
0 | 200 |   
1 | 200 | Operation failed.  
2 | 200 | Bulk operation partially succeeded.  
50000 | 400 | Body for POST request cannot be empty.  
50001 | 503 | Service temporarily unavailable. Please try again later.  
50002 | 400 | JSON syntax error  
50004 | 400 | API endpoint request timeout. (does not mean that the request was successful or failed, please check the request result).  
50005 | 410 | API endpoint is inactive or unavailable.  
50006 | 400 | Invalid Content-Type. Please use "application/JSON".  
50007 | 200 | User blocked.  
50008 | 200 | User doesn't exist.  
50009 | 200 | Account is frozen due to stop-out.  
50010 | 200 | User ID cannot be empty.  
50011 | 200 | Rate limit reached. Please refer to API documentation and throttle requests accordingly.  
50011 | 429 | Too Many Requests  
50012 | 200 | Account status invalid. Check account status  
50013 | 429 | Systems are busy. Please try again later.  
50014 | 400 | Parameter {param0} can not be empty.  
50015 | 400 | Either parameter {param0} or {param1} is required  
50016 | 400 | Parameter {param0} does not match parameter {param1}  
50017 | 200 | Position frozen and related operations restricted due to auto-deleveraging (ADL). Please try again later.  
50018 | 200 | Currency {param0} is frozen due to ADL. Operation restricted.  
50019 | 200 | Account frozen and related operations restricted due to auto-deleveraging (ADL). Please try again later.  
50020 | 200 | Position frozen and related operations restricted due to forced liquidation. Please try again later.  
50021 | 200 | Currency {param0} is frozen due to liquidation. Operation restricted.  
50022 | 200 | Account frozen and related operations restricted due to forced liquidation. Please try again later.  
50023 | 200 | Funding fees frozen and related operations are restricted. Please try again later.  
50024 | 200 | Parameter {param0} and {param1} can not exist at the same time.  
50025 | 200 | Parameter {param0} count exceeds the limit {param1}.  
50026 | 500 | System error. Try again later  
50027 | 200 | This account is restricted from trading. Please contact customer support for assistance.  
50028 | 200 | Unable to place the order. Please contact the customer service for details.  
50029 | 200 | Your account has triggered OKX risk control and is temporarily restricted from conducting transactions. Please check your email registered with OKX for contact from our customer support team.  
50030 | 200 | You don't have permission to use this API endpoint  
50032 | 200 | Your account has been set to prohibit transactions in this currency. Please confirm and try again  
50033 | 200 | Instrument blocked. Please verify trading this instrument is allowed under account settings and try again.  
50035 | 403 | This endpoint requires that APIKey must be bound to IP  
50036 | 200 | The expTime can't be earlier than the current system time. Please adjust the expTime and try again.  
50037 | 200 | Order expired.  
50038 | 200 | This feature is unavailable in demo trading  
50039 | 200 | Parameter "before" isn't supported for timestamp pagination  
50040 | 200 | Too frequent operations, please try again later  
50041 | 200 | Your user ID hasn’t been allowlisted. Please contact customer service for assistance.  
50042 | 200 | Repeated request  
50044 | 200 | Must select one broker type  
50045 | 200 | simPos should be empty because simulated positions cannot be counted when Position Builder is calculating under Spot-Derivatives risk offset mode  
50046 | 200 | This feature is temporarily unavailable while we make some improvements to it. Please try again later.  
50047 | 200 | {param0} has already settled. To check the relevant candlestick data, please use {param1}  
50048 | 200 | Switching risk unit may lead position risk increases and be forced liquidated. Please adjust position size, make sure margin is in a safe status.  
50049 | 200 | No information on the position tier. The current instrument doesn’t support margin trading.  
50050 | 200 | You’ve already activated options trading. Please don’t activate it again.  
50051 | 200 | Due to compliance restrictions in your country or region, you cannot use this feature.  
50052 | 200 | Due to local laws and regulations, you cannot trade with your chosen crypto.  
50053 | 200 | This feature is only available in demo trading.  
50055 | 200 | Reset unsuccessful. Assets can only be reset up to 5 times per day.  
50056 | 200 | You have pending orders or open positions with this currency. Please reset after canceling all the pending orders/closing all the open positions.  
50057 | 200 | Reset unsuccessful. Try again later.  
50058 | 200 | This crypto is not supported in an asset reset.  
50059 | 200 | Before you continue, you'll need to complete additional steps as required by your local regulators. Please visit the website or app for more details.  
50060 | 200 | For security and compliance purposes, please complete the identity verification process to continue using our services.  
50061 | 200 | You've reached the maximum order rate limit for this account.  
50062 | 200 | This feature is currently unavailable.  
50063 | 200 | You can't activate the credits as they might have expired or are already activated.  
50064 | 200 | The borrowing system is unavailable. Try again later.  
50067 | 200 | The API doesn't support cross site trading feature  
50069 | 200 | Margin ratio verification for this risk unit failed.  
50071 | 200 | {param} already exists  
e.g. clOrdId already exists  
50072 | 200 | Isolated margin mode is no longer supported in multi-currency margin mode and portfolio margin mode.  
50075 | 200 | The token is restricted in Islamic sub-account  
50076 | 200 | The time interval between the start date and end date cannot exceed {param0} days  
50077 | 200 | The time interval between the start date and end date cannot exceed {param0} months  
  
#### API Class

Error Code | HTTP Status Code | Error Message  
---|---|---  
50100 | 400 | API frozen, please contact customer service.  
50101 | 401 | APIKey does not match current environment.  
50102 | 401 | Timestamp request expired.  
50103 | 401 | Request header "OK-ACCESS-KEY" cannot be empty.  
50104 | 401 | Request header "OK-ACCESS-PASSPHRASE" cannot be empty.  
50105 | 401 | Request header "OK-ACCESS-PASSPHRASE" incorrect.  
50106 | 401 | Request header "OK-ACCESS-SIGN" cannot be empty.  
50107 | 401 | Request header "OK-ACCESS-TIMESTAMP" cannot be empty.  
50108 | 401 | Exchange ID does not exist.  
50109 | 401 | Exchange domain does not exist.  
50110 | 401 | Your IP {param0} is not included in your API key's IP whitelist.  
50111 | 401 | Invalid OK-ACCESS-KEY.  
50112 | 401 | Invalid OK-ACCESS-TIMESTAMP.  
50113 | 401 | Invalid signature.  
50114 | 401 | Invalid authorization.  
50115 | 405 | Invalid request method.  
50116 | 200 | Fast API is allowed to create only one API key  
50118 | 200 | To link the app using your API key, your broker needs to share their IP to be whitelisted  
50119 | 200 | API key doesn't exist  
50120 | 200 | This API key doesn't have permission to use this function  
50121 | 200 | You can't access our services through the IP address ({param0})  
50122 | 200 | Order amount must exceed minimum amount  
  
#### Trade Class

Error Code | HTTP Status code | Error Message  
---|---|---  
51000 | 400 | Parameter {param0} error  
51001 | 200 | Instrument ID, Instrument ID code or Spread ID doesn't exist.  
51002 | 200 | Instrument ID doesn't match underlying index.  
51003 | 200 | Either client order ID or order ID is required.  
51004_1101 | 200 | Order failed. For isolated long/short mode of {param0}, the sum of current order size, position quantity in the same direction, and pending orders in the same direction can’t be more than {param1}(contracts) which is the maximum position amount under current leverage. Please lower the leverage or use a new sub-account to place the order again (current leverage: {param2}×, current order size: {param3} contracts, position quantity in the same direction: {param4} contracts, pending orders in the same direction: {param5} contracts).  
51004_1102 | 200 | Order failed. For cross long/short mode of {param0}, the sum of current order size, position quantity in the long and short directions, and pending orders in the long and short directions can’t be more than {param1}(contracts) which is the maximum position amount under current leverage. Please lower the leverage or use a new sub-account to place the order again (current leverage: {param2}×, current order size: {param3} contracts, position quantity in the long and short directions: {param4} contracts, pending orders in the long and short directions: {param5} contracts).  
51004_1103 | 200 | Order failed. For cross buy/sell mode of {param0} and instFamily {param1}, the sum of current order size, current instId position quantity in the long and short directions, current instId pending orders in the long and short directions, and other contracts of the same instFamily can’t be more than {param2}(contracts) which is the maximum position amount under current leverage. Please lower the leverage or use a new sub-account to place the order again (current leverage: {param3}×, current order size: {param4} contracts, current instId position quantity in the long and short directions: {param5} contracts, current instId pending orders in the long and short directions: {param6} contracts, other contracts of the same instFamily: {param7} contracts).  
51004_1104 | 200 | Order failed. For buy/sell mode of {param0}, the sum of current buy order size, position quantity, and pending buy orders can’t be more than {param1}(contracts) which is the maximum position amount under current leverage. Please lower the leverage or use a new sub-account to place the order again (current leverage: {param2}×, current buy order size: {param3} contracts, position quantity: {param4} contracts, pending buy orders: {param5} contracts).  
51004_1105 | 200 | Order failed. For buy/sell mode of {param0}, the sum of current sell order size, position quantity, and pending sell orders can’t be more than {param1}(contracts) which is the maximum position amount under current leverage. Please lower the leverage or use a new sub-account to place the order again (current leverage: {param2}×, current sell order size: {param3} contracts, position quantity: {param4} contracts, pending sell orders: {param5} contracts).  
51004_1106 | 200 | Order failed. For cross buy/sell mode of {param0} and instFamily {param1}, the sum of current buy order size, current instId position quantity, current instId pending buy orders, and other contracts of the same instFamily can’t be more than {param2}(contracts) which is the maximum position amount under current leverage. Please lower the leverage or use a new sub-account to place the order again (current leverage: {param3}×, current buy order size: {param4} contracts, current instId position quantity: {param5} contracts, current instId pending buy orders: {param6} contracts, other contracts of the same instFamily: {param7} contracts).  
51004_1107 | 200 | Order failed. For cross buy/sell mode of {param0} and instFamily {param1}, the sum of current sell order size, current instId position quantity, current instId pending sell orders, and other contracts of the same instFamily can’t be more than {param2}(contracts) which is the maximum position amount under current leverage. Please lower the leverage or use a new sub-account to place the order again (current leverage: {param3}×, current sell order size: {param4} contracts, current instId position quantity: {param5} contracts, current instId pending sell orders: {param6} contracts, other contracts of the same instFamily: {param7} contracts).  
51004_1111 | 200 | Order amendment failed. For isolated long/short mode of {param0}, the sum of increment order size by amendment, position quantity in the same direction, and pending orders in the same direction can’t be more than {param1}(contracts) which is the maximum position amount under current leverage. Please lower the leverage or use a new sub-account to place the order again (current leverage: {param2}×, increment order size by amendment: {param3} contracts, position quantity in the same direction: {param4} contracts, pending orders in the same direction: {param5} contracts).  
51004_1112 | 200 | Order amendment failed. For cross long/short mode of {param0}, the sum of increment order size by amendment, position quantity in the long and short directions, and pending orders in the long and short directions can’t be more than {param1}(contracts) which is the maximum position amount under current leverage. Please lower the leverage or use a new sub-account to place the order again (current leverage: {param2}×, increment order size by amendment: {param3} contracts, position quantity in the long and short directions: {param4} contracts, pending orders in the same direction: {param5} contracts).  
51004_1113 | 200 | Order amendment failed. For cross buy/sell mode of {param0} and instFamily {param1}, the sum of increment order size by amendment, current instId position quantity in the long and short directions, current instId pending orders in the long and short directions, and other contracts of the same instFamily can’t be more than {param2}(contracts) which is the maximum position amount under current leverage. Please lower the leverage or use a new sub-account to place the order again (current leverage: {param3}×, increment order size by amendment: {param4} contracts, current instId position quantity in the long and short directions: {param5} contracts, current instId pending orders in the long and short directions: {param6} contracts, other contracts of the same instFamily: {param7} contracts).  
51004_1114 | 200 | Order amendment failed. For buy/sell mode of {param0}, the sum of increment order size by amending current buy order, position quantity, and pending buy orders can’t be more than {param1}(contracts) which is the maximum position amount under current leverage. Please lower the leverage or use a new sub-account to place the order again (current leverage: {param2}×, increment order size by amending current buy order: {param3} contracts, position quantity: {param4} contracts, pending buy orders: {param5} contracts).  
51004_1115 | 200 | Order amendment failed. For buy/sell mode of {param0}, the sum of increment order size by amending current sell order, position quantity, and pending sell orders can’t be more than {param1}(contracts) which is the maximum position amount under current leverage. Please lower the leverage or use a new sub-account to place the order again (current leverage: {param2}×, increment order size by amending current sell order: {param3} contracts, position quantity: {param4} contracts, pending sell orders: {param5} contracts).  
51004_1116 | 200 | Order amendment failed. For cross buy/sell mode of {param0} and instFamily {param1}, the sum of increment order size by amending current buy order, current instId position quantity, current instId pending buy orders, and other contracts of the same instFamily can’t be more than {param2}(contracts) which is the maximum position amount under current leverage. Please lower the leverage or use a new sub-account to place the order again (current leverage: {param3}×, increment order size by amending current buy order: {param4} contracts, current instId position quantity: {param5} contracts, current instId pending buy orders: {param6} contracts, other contracts of the same instFamily: {param7} contracts).  
51004_1117 | 200 | Order amendment failed. For cross buy/sell mode of {param0} and instFamily {param1}, the sum of increment order size by amending current sell order, current instId position quantity, current instId pending sell orders, and other contracts of the same instFamily can’t be more than {param2}(contracts) which is the maximum position amount under current leverage. Please lower the leverage or use a new sub-account to place the order again (current leverage: {param3}×, increment order size by amending current sell order: {param4} contracts, current instId position quantity: {param5} contracts, current instId pending sell orders: {param6} contracts, other contracts of the same instFamily: {param7} contracts).  
51005 | 200 | Your order amount exceeds the max order amount.  
51006 | 200 | Order price is not within the price limit (max buy price: {param0} , min sell price: {param1} )  
51007 | 200 | Order failed. Please place orders of at least 1 contract or more.  
51008_1000 | 200 | Order failed. Insufficient {param0} balance in account  
51008_1001 | 200 | Order failed. Insufficient {param0} margin in account  
51008_1002 | 200 | Order failed. Insufficient {param0} balance in account, and Auto Borrow is not enabled  
51008_1003 | 200 | Order failed. Insufficient {param0} margin in account and auto-borrow is not enabled (Portfolio margin mode can try IOC orders to lower the risks)  
51008_1004 | 200 | Insufficient {param0} available as your borrowing amount exceeds tier limit. Lower leverage appropriately. New and pending limit orders need borrowings {param1}, remaining quota {param2}, total limit {param3}, in use {param4}.  
51008_1005 | 200 | Order failed. Exceeds {param0} borrow limit (Limit of master account plus the allocated VIP quota for the current account) (Existing pending orders and the new order are required to borrow {param1}, Remaining limit {param2}, Limit {param3}, Limit used {param4})  
51008_1006 | 200 | Order failed. Insufficient {param0} borrowing quota results in an insufficient amount available to borrow.  
51008_1007 | 200 | Your order failed because it requires borrowing {param0}, and the platform’s loan quota is insufficient.  
51008_1009 | 200 | Order failed. Insufficient account balance, and the adjusted equity in `USD` is less than IMR (Portfolio margin mode can try IOC orders to lower the risks)  
51008_1010 | 200 | Order failed. The order didn't pass delta verification because if the order were to succeed, the change in adjEq would be smaller than the change in IMR. Increase adjEq or reduce IMR (Portfolio margin mode can try IOC orders to lower the risks)  
51008_1015 | 200 | Order failed. Your available balance is insufficient. It excludes crypto ({param0}) exceeding the platform's collateral limit.  
51008_1016 | 200 | Order failed. Your available {param0} balance is insufficient, and your available margin (in USD) is too low for borrowing. This margin excludes crypto ({param1}) exceeding the platform's collateral limit.  
51008_1017 | 200 | Your order failed because it requires a borrowing amount that exceeds your tier limit. The total borrowing required after placing your order is {param1} {param0}, and the limit for {param2}x borrowing leverage is {param3} {param0}. Try lowering your leverage before placing your order again.  
51008_1018 | 200 | Your order failed because it requires a borrowing amount that exceeds your tier limit. The total potential borrowing required after placing your order is {param1} {param0}, and the limit for {param2}x borrowing leverage is {param3} {param0}. Try lowering your leverage before placing your order again.  
51008_1019 | 200 | Order failed. Your main account's {param0} borrowing quota is insufficient.  
51008_1020 | 200 | Order failed. After the spot fee in quote currency is deducted, your {param0} balance is insufficient to complete the order. Please disable the spot fees in quote currency toggle and try again.  
51009 | 200 | Order blocked. Please contact customer support for assistance.  
51010 | 200 | Request unsupported under current account mode  
51011 | 200 | Order ID already exists.  
51012 | 200 | Token doesn't exist.  
51014 | 200 | Index doesn't exist.  
51015 | 200 | Instrument ID doesn't match instrument type.  
51016 | 200 | Client order ID already exists.  
51017 | 200 | Loan amount exceeds borrowing limit.  
51018 | 200 | Users with options accounts cannot hold net short positions.  
51019 | 200 | No net long positions can be held under cross margin mode in options.  
51020 | 200 | Your order should meet or exceed the minimum order amount.  
51021 | 200 | The pair or contract is not yet listed  
51022 | 200 | Contract suspended.  
51023 | 200 | Position doesn't exist.  
51024 | 200 | Trading account is blocked.  
51024 | 200 | In accordance with the terms of service, we regret to inform you that we cannot provide services for you. If you have any questions, please contact our customer support.  
51024 | 200 | According to your request, this account has been frozen. If you have any questions, please contact our customer support.  
51024 | 200 | Your account has recently changed some security settings. To protect the security of your funds, this action is not allowed for now. If you have any questions, please contact our customer support.  
51024 | 200 | You have withdrawn all assets in the account. To protect your personal information, the account has been permanently frozen. If you have any questions, please contact our customer support.  
51024 | 200 | Your identity could not be verified. To protect the security of your funds, this action is not allowed. Please contact our customer support.  
51024 | 200 | Your verified age doesn't meet the requirement. To protect the security of your funds, we cannot proceed with your request. Please contact our customer support.  
51024 | 200 | In accordance with the terms of service, trading is currently unavailable in your verified country or region. Close all open positions or contact customer support if you have any questions.  
51024 | 200 | In accordance with the terms of service, multiple account is not allowed. To protect the security of your funds, this action is not allowed. Please contact our customer support.  
51024 | 200 | Your account is in judicial freezing, and this action is not allowed for now. If you have any questions, please contact our customer support.  
51024 | 200 | Based on your previous requests, this action is not allowed for now. If you have any questions, please contact our customer support.  
51024 | 200 | Your account has disputed deposit orders. To protect the security of your funds, this action is not allowed for now. Please contact our customer support.  
51024 | 200 | Unable to proceed. Please resolve your existing P2P disputes first.  
51024 | 200 | Your account might have compliance risk. To protect the security of your funds, this action is not allowed for now. Please contact our customer support.  
51024 | 200 | Based on your trading requests, this action is not allowed for now. If you have any questions, please contact our customer support.  
51024 | 200 | Your account has triggered risk control. This action is not allowed for now. Please contact our customer support.  
51024 | 200 | This account is temporarily unavailable. Please contact our customer support.  
51024 | 200 | Withdrawal function of this account is temporarily unavailable. Please contact our customer support.  
51024 | 200 | Transfer function of this account is temporarily unavailable. Please contact our customer support.  
51024 | 200 | You violated the "Fiat Trading Rules" when you were doing fiat trade, so we'll no longer provide fiat trading-related services for you. The deposit and withdrawal of your account and other trading functions will not be affected.  
51024 | 200 | Please kindly check your mailbox and reply to emails from the verification team.  
51024 | 200 | According to your request, this account has been closed. If you have any questions, please contact our customer support.  
51024 | 200 | Your account might have security risk. To protect the security of your funds, this action is not allowed for now. Please contact our customer support.  
51024 | 200 | Your account might have security risk. Convert is now unavailable. Please contact our customer support.  
51024 | 200 | Unable to proceed due to account restrictions. We've sent an email to your OKX registered email address regarding this matter, or you can contact customer support via Chat with AI chatbot on our support center page.  
51024 | 200 | In accordance with the terms of service, trading is currently unavailable in your verified country or region. Cancel all orders or contact customer support if you have any questions.  
51024 | 200 | In accordance with the terms of service, trading is not available in your verified country. If you have any questions, please contact our customer support.  
51024 | 200 | This product isn’t available in your country or region due to local laws and regulations. If you don’t reside in this area, you may continue using OKX Exchange products with a valid government-issued ID.  
51024 | 200 | Please note that you may not be able to transfer or trade in the first 30 minutes after establishing custody trading sub-accounts. Please kindly wait and try again later.  
51024 | 200 | Feature unavailable. Complete Advanced verification to access this feature.  
51024 | 200 | You can't trade or deposit now. Update your personal info to restore full account access immediately.  
51024 | 200 | Sub-accounts exceeding the limit aren't allowed to open new positions and can only reduce or close existing ones. Please try again with a different account.  
51025 | 200 | Order count exceeds the limit.  
51026 | 200 | Instrument type doesn't match underlying index.  
51027 | 200 | Contract expired.  
51028 | 200 | Contract under delivery.  
51029 | 200 | Contract is being settled.  
51030 | 200 | Funding fee is being settled.  
51031 | 200 | This order price is not within the closing price range.  
51032 | 200 | Closing all the positions at the market price.  
51033 | 200 | The total amount per order for this pair has reached the upper limit.  
51034 | 200 | Fill rate exceeds the limit that you've set. Please reset the market maker protection to inactive for new trades.  
51035 | 200 | This account doesn't have permission to submit MM quote order.  
51036 | 200 | Only options instrument of the PM account supports MMP orders.  
51042 | 200 | Under the Portfolio margin account, users can only place market maker protection orders in cross margin mode in Options.  
51043 | 200 | This isolated position doesn't exist.  
59509 | 200 | Account does not have permission to reset MMP status  
51037 | 200 | This account only supports placing IOC orders to reduce account risk.  
51038 | 200 | IOC order already exists under the current risk module.  
51039 | 200 | Leverage cannot be adjusted for the cross positions of Expiry Futures and Perpetual Futures under the PM account.  
51040 | 200 | Cannot adjust margins for long isolated options positions  
51041 | 200 | Portfolio margin account only supports the Buy/Sell mode.  
51044 | 200 | The order type {param0}, {param1} is not allowed to set stop loss and take profit  
51046 | 200 | The take profit trigger price must be higher than the order price  
51047 | 200 | The stop loss trigger price must be lower than the order price  
51048 | 200 | The take profit trigger price must be lower than the order price  
51049 | 200 | The stop loss trigger price must be higher than the order price  
51050 | 200 | The take profit trigger price must be higher than the best ask price  
51051 | 200 | The stop loss trigger price must be lower than the best ask price  
51052 | 200 | The take profit trigger price must be lower than the best bid price  
51053 | 200 | The stop loss trigger price must be higher than the best bid price  
51054 | 500 | Request timed out. Please try again.  
51055 | 200 | Futures Grid is not available in Portfolio Margin mode  
51056 | 200 | Action not allowed  
51057 | 200 | This bot isn’t available in current account mode. Switch mode in Settings > Account mode to continue.  
51058 | 200 | No available position for this algo order  
51059 | 200 | Strategy for the current state does not support this operation  
51063 | 200 | OrdId does not exist  
51065 | 200 | algoClOrdId already exists.  
51066 | 200 | Market orders unavailable for options trading. Place a limit order to close position.  
51068 | 200 | {param0} already exists within algoClOrdId and attachAlgoClOrdId.  
51069 | 200 | The option contracts related to current {param0} do not exist  
51070 | 200 | You do not meet the requirements for switching to this account mode. Please upgrade the account mode on the OKX website or App  
51071 | 200 | You've reached the maximum limit for tag level cancel all after timers.  
51072 | 200 | As a spot lead trader, you need to set tdMode to spot_isolated when buying the configured lead trade pairs.  
51073 | 200 | As a spot lead trader, you need to use '/copytrading/close-subposition' for selling assets through lead trades  
51074 | 200 | Only the tdMode for lead trade pairs configured by spot lead traders can be set to 'spot_isolated'  
51075 | 200 | Order modification failed. You can only modify the price of sell orders in spot copy trading.  
51076 | 200 | TP/SL orders in Split TPs only support one-way TP/SL. You can't use slTriggerPx&slOrdPx and tpTriggerPx&tpOrdPx at the same time.  
51077 | 200 | Setting multiple TP and cost-price SL orders isn’t supported for spot and margin trading.  
51078 | 200 | You are a lead trader. Split TPs are not supported.  
51079 | 200 | The number of TP orders with Split TPs attached in a same order cannot exceed {param0}  
51080 | 200 | Take-profit trigger price types (tpTriggerPxType) must be the same in an order with Split TPs attached  
51081 | 200 | Take-profit trigger prices (tpTriggerPx) cannot be the same in an order with Split TPs attached  
51082 | 200 | TP trigger prices (tpOrdPx) in one order with multiple TPs must be market prices.  
51083 | 200 | The total size of TP orders with Split TPs attached in a same order should equal the size of this order  
51084 | 200 | The number of SL orders with Split TPs attached in a same order cannot exceed {param0}  
51085 | 200 | The number of TP orders cannot be less than 2 when cost-price SL is enabled (amendPxOnTriggerType set as 1) for Split TPs  
51086 | 200 | The number of orders with Split TPs attached in a same order cannot exceed {param0}  
51538 | 200 | You need to use attachAlgoOrds if you used attachAlgoOrds when placing an order. attachAlgoOrds is not supported if you did not use attachAlgoOrds when placing this order.  
51539 | 200 | attachAlgoId or attachAlgoClOrdId cannot be identical when modifying any TP/SL within your split TPs order  
51527 | 200 | Order modification failed. At least 1 of the attached TP/SL orders does not exist.  
51087 | 200 | Listing canceled for this crypto  
51088 | 200 | You can only place 1 TP/SL order to close an entire position  
51089 | 200 | The size of the TP order among split TPs attached cannot be empty  
51090 | 200 | You can't modify the amount of an SL order placed with a TP limit order.  
51091 | 200 | All TP orders in one order must be of the same type.  
51092 | 200 | TP order prices (tpOrdPx) in one order must be different.  
51093 | 200 | TP limit order prices (tpOrdPx) in one order can't be –1 (market price).  
51094 | 200 | You can't place TP limit orders in spot, margin, or options trading.  
51095 | 200 | To place TP limit orders at this endpoint, you must place an SL order at the same time.  
51096 | 200 | cxlOnClosePos needs to be true to place a TP limit order  
51098 | 200 | You can't add a new TP order to an SL order placed with a TP limit order.  
51099 | 200 | You can't place TP limit orders as a lead trader.  
51178 | 200 | tpTriggerPx&tpOrdPx or slTriggerPx&slOrdPx can't be empty when using attachAlgoClOrdId.  
51100 | 200 | Unable to place order. Take profit/Stop loss conditions cannot be added to reduce-only orders.  
51101 | 200 | Order failed, the sz of the current order can’t be more than {param0} (contracts).  
51102 | 200 | Order failed, the number of pending orders for this instId can’t be more than {param0} (orders)  
51103 | 200 | Order failed, the number of pending orders across all instIds under the {param0} current instFamily can’t be more than {param1} (orders)  
51104 | 200 | Order failed, the aggregated contract quantity for all pending orders across all instIds under the {param0} current instFamily can’t be more than {param1} (contracts)  
51105 | 200 | Order failed, the maximal sum of position quantity and pending orders quantity with the same direction for current instId can’t be more than {param0} (contracts)  
51106 | 200 | Order failed, the maximal sum of position quantity and pending orders quantity with the same direction across all instIds under the {param0} current instFamily can’t be more than {param1} (contracts)  
51107 | 200 | Order failed, the maximal sum of position quantity and pending orders quantity in both directions across all instIds under the {param0} current instFamily can’t be more than {param1} (contracts)  
51108 | 200 | Positions exceed the limit for closing out with the market price.  
51109 | 200 | No available offers.  
51110 | 200 | You can only place a limit order after Call Auction has started.  
51111 | 200 | Maximum {param0} orders can be placed in bulk.  
51112 | 200 | Close order size exceeds available size for this position.  
51113 | 429 | Market-price liquidation requests too frequent.  
51115 | 429 | Cancel all pending close-orders before liquidation.  
51116 | 200 | Order price or trigger price exceeds {param0}.  
51117 | 200 | Pending close-orders count exceeds limit.  
51120 | 200 | Order amount is less than {param0}, please try again.  
51121 | 200 | Order quantity must be a multiple of the lot size.  
51122 | 200 | Order price should higher than the min price {param0}  
51123 | 200 | Min price increment is null.  
51124 | 200 | You can only place limit orders during call auction.  
51125 | 200 | Currently there are pending reduce + reverse position orders in margin trading. Please cancel all pending reduce + reverse position orders and continue.  
51126 | 200 | Currently there are pending reduce only orders in margin trading. Please cancel all pending reduce only orders and continue.  
51127 | 200 | Available balance is 0.  
51128 | 200 | Multi-currency margin accounts cannot do cross-margin trading.  
51129 | 200 | The value of the position and buy order has reached the position limit. No further buying is allowed.  
51130 | 200 | Fixed margin currency error.  
51131 | 200 | Insufficient balance.  
51132 | 200 | Your position amount is negative and less than the minimum trading amount.  
51133 | 200 | Reduce-only feature is unavailable for spot transactions in multi-currency margin accounts.  
51134 | 200 | Closing failed. Please check your margin holdings and pending orders. Turn off the Reduce-only to continue.  
51135 | 200 | Your closing price has triggered the limit price, and the max buy price is {param0}.  
51136 | 200 | Your closing price has triggered the limit price, and the min sell price is {param0}.  
51137 | 200 | The highest price limit for buy orders is {param0}.  
51138 | 200 | The lowest price limit for sell orders is {param0}.  
51139 | 200 | Reduce-only feature is unavailable for the spot transactions by spot mode.  
51140 | 200 | Purchase failed due to insufficient sell orders, please try later.  
51142 | 200 | There is no valid quotation in the market, and the order cannot be filled in USDT mode, please try to switch to currency mode  
51143 | 200 | Insufficient conversion amount  
51144 | 200 | Please use {param0} for closing.  
51147 | 200 | To trade options, make sure you have more than 10,000 USD worth of assets in your trading account first, then activate options trading  
51148 | 200 | Failed to place order. The new order may execute an opposite trading direction of your existing reduce-only positions. Cancel or edit pending orders to continue order  
51149 | 500 | Order timed out. Please try again. (does not mean that the request was successful or failed, please check the request result)  
51150 | 200 | The precision of the number of trades or the price exceeds the limit.  
51152 | 200 | Unable to place an order that mixes automatic buy with automatic repayment or manual operation in Quick margin mode.  
51153 | 200 | Unable to borrow manually in Quick margin mode. The amount you entered exceeds the upper limit.  
51154 | 200 | Unable to repay manually in Quick margin mode. The amount you entered exceeds your available balance.  
51155 | 200 | Trading of this pair or contract is restricted due to local compliance requirements.  
51158 | 200 | Manual transfer unavailable. To proceed, please switch to Quick margin mode (isoMode = quick_margin)  
51164 | 200 | As lead trader, you can't switch to portfolio margin mode.  
51169 | 200 | Order failed because you don't have any positions in this direction for this contract to reduce or close.  
51170 | 200 | Failed to place order. A reduce-only order can’t be the same trading direction as your existing positions.  
51171 | 200 | Failed to edit order. The edited order may execute an opposite trading direction of your existing reduce-only positions. Cancel or edit pending orders to continue.  
51173 | 200 | Unable to close all at market price. Your current positions don't have any liabilities.  
51174 | 200 | Order failed, number of pending orders for {param0} exceed the limit of {param1}.  
51175 | 200 | Parameters {param0} {param1} and {param2} cannot be empty at the same time  
51176 | 200 | Only one parameter can be filled among Parameters {param0} {param1} and {param2}  
51177 | 200 | Unavailable to amend {param1} because the price type of the current options order is {param0}  
51179 | 200 | Unavailable to place options orders using {param0} in simple mode  
51180 | 200 | The range of {param0} should be ({param1}~{param2})  
51181 | 200 | ordType must be limit while placing {param0} orders  
51182 | 200 | The total number of pending orders under price types pxUsd and pxVol for the current account cannot exceed {param0}  
51185 | 200 | The maximum value allowed per order is {maxOrderValue} USD  
51186 | 200 | Order failed. The leverage for {param0} in your current margin mode is {param1}x, which exceeds the platform limit of {param2}x.  
51187 | 200 | Order failed. For {param0} {param1} in your current margin mode, the sum of your current order amount, position sizes, and open orders is {param2} contracts, which exceeds the platform limit of {param3} contracts. Reduce your order amount, cancel orders, or close positions.  
51192 | 200 | The {param0} price corresponding to the IV level you entered is lower than the minimum allowed selling price of {param1} {param2}. Enter a higher IV level.  
51193 | 200 | The {param0} price corresponding to the IV level you entered is higher than the maximum allowed buying price of {param1} {param2}. Enter a lower IV level.  
51194 | 200 | The {param0} price corresponding to the USD price you entered is lower than the minimum allowed selling price of {param1} {param2}. Enter a higher USD price.  
51195 | 200 | The {param0} price corresponding to the USD price you entered is higher than the maximum allowed buying price of {param1} {param2}. Enter a lower USD price.  
51196 | 200 | You can only place limit orders during the pre-quote phase.  
51197 | 200 | You can only place limit orders after the pre-quote phase begins.  
51201 | 200 | The value of a market order can't exceed {param0}.  
51202 | 200 | Market order amount exceeds the maximum amount.  
51203 | 200 | Order amount exceeds the limit {param0}.  
51204 | 200 | The price for the limit order cannot be empty.  
51205 | 200 | Reduce Only is not available.  
51206 | 200 | Please cancel the Reduce Only order before placing the current {param0} order to avoid opening a reverse position.  
51207 | 200 | Trading amount exceeds the limit, and can't be all closed at the market price. You can try closing the position manually in batches.  
51209 | 200 | Order failed because your current status only allows placing delta-reducing orders. Increase your account equity or place an order that would reduce delta when filled to proceed.  
51210 | 200 | Order failed because your current status only allows placing one order per underlying. Cancel other orders in the underlying to proceed.  
51211 | 200 | Order failed because your current status only allows placing delta-reducing orders. Increase your account equity or place an order that would reduce delta when filled to proceed.  
51212 | 200 | Order failed because your current status doesn’t support batch orders. Place a single order to proceed.  
51213 | 200 | Order failed because your current status only allows placing one order per underlying. Cancel other orders in the underlying to proceed.  
51214 | 200 | Failed to modify order because your current status only allows placing delta-reducing orders. Increase your account equity or place an order that would reduce delta when filled to proceed.  
51220 | 200 | Lead and follow bots only support “Sell” or “Close all positions” when bot stops  
51221 | 200 | The profit-sharing ratio must be between 0% and 30%  
51222 | 200 | Profit sharing isn’t supported for this type of bot  
51223 | 200 | Only lead bot creators can set profit-sharing ratio  
51224 | 200 | Profit sharing isn’t supported for this crypto pair  
51225 | 200 | Instant trigger isn’t available for follow bots  
51226 | 200 | Editing parameters isn’t available for follow bots  
51250 | 200 | Algo order price is out of the available range.  
51251 | 200 | Bot order type error occurred when placing iceberg order  
51252 | 200 | Algo order amount is out of the available range.  
51253 | 200 | Average amount exceeds the limit of per iceberg order.  
51254 | 200 | Iceberg average amount error occurred.  
51255 | 200 | Limit of per iceberg order: Total amount/1000 < x <= Total amount.  
51256 | 200 | Iceberg order price variance error.  
51257 | 200 | Trailing stop order callback rate error. The callback rate should be {min}< x<={max}%.  
51258 | 200 | Trailing stop order placement failed. The trigger price of a sell order must be higher than the last transaction price.  
51259 | 200 | Trailing stop order placement failed. The trigger price of a buy order must be lower than the last transaction price.  
51260 | 200 | Maximum of {param0} pending trailing stop orders can be held at the same time.  
51261 | 200 | Each user can hold up to {param0} pending stop orders at the same time.  
51262 | 200 | Maximum {param0} pending iceberg orders can be held at the same time.  
51263 | 200 | Maximum {param0} pending time-weighted orders can be held at the same time.  
51264 | 200 | Average amount exceeds the limit of per time-weighted order.  
51265 | 200 | Time-weighted order limit error.  
51267 | 200 | Time-weighted order strategy initiative rate error.  
51268 | 200 | Time-weighted order strategy initiative range error.  
51269 | 200 | Time-weighted order interval error. Interval must be {%min}<= x<={%max}.  
51270 | 200 | The limit of time-weighted order price variance is 0 < x <= 1%.  
51271 | 200 | Sweep ratio must be 0 < x <= 100%.  
51272 | 200 | Price variance must be 0 < x <= 1%.  
51273 | 200 | Total amount must be greater than {param0}.  
51274 | 200 | Total quantity of time-weighted order must be larger than single order limit.  
51275 | 200 | The amount of single stop-market order cannot exceed the upper limit.  
51276 | 200 | Prices cannot be specified for stop market orders.  
51277 | 200 | TP trigger price cannot be higher than the last price.  
51278 | 200 | SL trigger price cannot be lower than the last price.  
51279 | 200 | TP trigger price cannot be lower than the last price.  
51280 | 200 | SL trigger price cannot be higher than the last price.  
51281 | 200 | Trigger order do not support the tgtCcy parameter.  
51282 | 200 | The range of Price variance is {param0}~{param1}  
51283 | 200 | The range of Time interval is {param0}~{param1}  
51284 | 200 | The range of Average amount is {param0}~{param1}  
51285 | 200 | The range of Total amount is {param0}~{param1}  
51286 | 200 | The total amount should not be less than {param0}  
51287 | 200 | This bot doesn't support current instrument  
51288 | 200 | Bot is currently stopping. Do not make multiple attempts to stop.  
51289 | 200 | Bot configuration does not exist. Please try again later  
51290 | 200 | The Bot engine is being upgraded. Please try again later  
51291 | 200 | This Bot does not exist or has been stopped  
51292 | 200 | This Bot type does not exist  
51293 | 200 | This Bot does not exist  
51294 | 200 | This Bot cannot be created temporarily. Please try again later  
51295 | 200 | Portfolio margin account does not support ordType {param0} in Trading bot mode  
51298 | 200 | Trigger orders are not available in the net mode of Expiry Futures and Perpetual Futures  
51299 | 200 | Order did not go through. You can hold a maximum of {param0} orders of this type.  
51300 | 200 | TP trigger price cannot be higher than the mark price  
51302 | 200 | SL trigger price cannot be lower than the mark price  
51303 | 200 | TP trigger price cannot be lower than the mark price  
51304 | 200 | SL trigger price cannot be higher than the mark price  
51305 | 200 | TP trigger price cannot be higher than the index price  
51306 | 200 | SL trigger price cannot be lower than the index price  
51307 | 200 | TP trigger price cannot be lower than the index price  
51308 | 200 | SL trigger price cannot be higher than the index price  
51309 | 200 | Cannot create trading bot during call auction  
51310 | 200 | Strategic orders with Iceberg and TWAP order type are not supported when margins are self-transferred in isolated mode.  
51311 | 200 | Failed to place trailing stop order. Callback rate should be within {min}<x<={max}  
51312 | 200 | Failed to place trailing stop order. Order amount should be within {min}<x<={max}  
51313 | 200 | Manual transfer in isolated mode does not support bot trading  
51317 | 200 | Trigger orders are not available by margin  
51327 | 200 | closeFraction is only available for Expiry Futures and Perpetual Futures  
51328 | 200 | closeFraction is only available for reduceOnly orders  
51329 | 200 | closeFraction is only available in NET mode  
51330 | 200 | closeFraction is only available for stop market orders  
51331 | 200 | closeFraction is only available for close position orders  
51332 | 200 | closeFraction is not applicable to Portfolio Margin  
51333 | 200 | Close position order in hedge-mode or reduce-only order in one-way mode cannot attach TPSL  
51340 | 200 | Used margin must be greater than {0}{1}  
51341 | 200 | Position closing not allowed  
51342 | 200 | Closing order already exists. Please try again later  
51343 | 200 | TP price must be less than the lower price  
51344 | 200 | SL price must be greater than the upper price  
51345 | 200 | Policy type is not grid policy  
51346 | 200 | The highest price cannot be lower than the lowest price  
51347 | 200 | No profit available  
51348 | 200 | Stop loss price must be less than the lower price in the range.  
51349 | 200 | Take profit price must be greater than the highest price in the range.  
51350 | 200 | No recommended parameters  
51351 | 200 | Single income must be greater than 0  
51352 | 200 | You can have {0} to {1} trading pairs  
51353 | 200 | Trading pair {0} already exists  
51354 | 200 | The percentages of all trading pairs should add up to 100%  
51355 | 200 | Select a date within {0} - {1}  
51356 | 200 | Select a time within {0} - {1}  
51357 | 200 | Select a time zone within {0} - {1}  
51358 | 200 | The investment amount of each crypto must be greater than {amount}  
51359 | 200 | Recurring buy not supported for the selected crypto {0}  
51370 | 200 | The range of lever is {0}~{1}  
51380 | 200 | Market conditions do not meet the strategy running configuration. You can try again later or adjust your tp/sl configuration.  
51381 | 200 | Per grid profit ratio must be larger than 0.1% and less or equal to 10%  
51382 | 200 | Stop triggerAction is not supported by the current strategy  
51383 | 200 | The min_price is lower than the last price  
51384 | 200 | The trigger price must be greater than the min price  
51385 | 200 | The take profit price needs to be greater than the min price  
51386 | 200 | The min price needs to be greater than 1/2 of the last price  
51387 | 200 | Stop loss price must be less than the bottom price  
51388 | 200 | This Bot is in running status  
51389 | 200 | Trigger price should be lower than {0}  
51390 | 200 | Trigger price should be lower than the TP price  
51391 | 200 | Trigger price should be higher than the SL price  
51392 | 200 | TP price should be higher than the trigger price  
51393 | 200 | SL price should be lower than the trigger price  
51394 | 200 | Trigger price should be higher than the TP price  
51395 | 200 | Trigger price should be lower than the SL price  
51396 | 200 | TP price should be lower than the trigger price  
51397 | 200 | SL price should be higher than the trigger price  
51398 | 200 | Current market meets the stop condition. The bot cannot be created.  
51399 | 200 | Max margin under current leverage: {amountLimit} {quoteCurrency}. Enter a smaller amount and try again.  
51400 | 200 | Order cancellation failed as the order has been filled, canceled or does not exist.  
51400 | 200 | Cancellation failed as the order does not exist. (Only applicable to Nitro Spread)  
51401 | 200 | Cancellation failed as the order is already canceled. (Only applicable to Nitro Spread)  
51402 | 200 | Cancellation failed as the order is already completed. (Only applicable to Nitro Spread)  
51403 | 200 | Cancellation failed as the order type doesn't support cancellation.  
51404 | 200 | Order cancellation unavailable during the second phase of call auction.  
51405 | 200 | Cancellation failed as you don't have any pending orders.  
51406 | 400 | Canceled - order count exceeds the limit {param0}.  
51407 | 200 | Either order ID or client order ID is required.  
51408 | 200 | Pair ID or name doesn't match the order info.  
51409 | 200 | Either pair ID or pair name ID is required.  
51410 | 200 | Cancellation failed as the order is already in canceling status or pending settlement.  
51411 | 200 | Account does not have permission for mass cancellation.  
51412 | 200 | Cancellation timed out, please try again later.  
51412 | 200 | The order has been triggered and can't be canceled.  
51413 | 200 | Cancellation failed as the order type is not supported by endpoint.  
51415 | 200 | Unable to place order. Spot trading only supports using the last price as trigger price. Please select "Last" and try again.  
51416 | 200 | Order has been triggered and can't be canceled  
51500 | 200 | You must enter a price, quantity, or TP/SL  
51501 | 400 | Maximum {param0} orders can be modified.  
51502_1030 | 200 | Unable to edit order: insufficient balance or margin.  
51502_1031 | 200 | Order failed. Insufficient {param0} margin in account  
51502_1032 | 200 | Order failed. Insufficient {param0} balance in account and Auto Borrow is not enabled  
51502_1033 | 200 | Order failed. Insufficient {param0} margin in account and Auto Borrow is not enabled (Portfolio margin mode can try IOC orders to lower the risks)  
51502_1034 | 200 | Order failed. The requested borrowing amount is larger than the available {param0} borrowing amount of your position tier. Existing pending orders and the new order need to borrow {param1}, remaining quota {param2}, total quota {param3}, used {param4}  
51502_1035 | 200 | Order failed. The requested borrowing amount is larger than the available {param0} borrowing amount of your main account and the allocated VIP quota. Existing pending orders and the new order need to borrow {param1}, remaining quota {param2}, total quota {param3}, used {param4}  
51502_1036 | 200 | Order failed. Insufficient available borrowing amount in {param0} crypto pair  
51502_1037 | 200 | Failed to modify order because it requires borrowing {param0}, and the platform’s loan quota is insufficient.  
51502_1039 | 200 | Order failed. Insufficient account balance and the adjusted equity in USD is smaller than the IMR.  
51502_1040 | 200 | Order failed. The order didn't pass delta verification. If the order succeeded, the change in adjEq would be smaller than the change in IMR. Increase adjEq or reduce IMR (Portfolio margin mode can try IOC orders to lower the risks)  
51502_1049 | 200 | Order modification failed. Your main account’s {param0} borrowing quota is insufficient.  
51503 | 200 | Your order has already been filled or canceled.  
51503 | 200 | Order modification failed as the order does not exist. (Only applicable to Nitro Spread)  
51505 | 200 | {instId} is not in call auction  
51506 | 200 | Order modification unavailable for the order type.  
51507 | 200 | You can only place market orders for this crypto at least 5 minutes after its listing.  
51508 | 200 | Orders are not allowed to be modified during the call auction.  
51509 | 200 | Modification failed as the order has been canceled. (Only applicable to Nitro Spread)  
51510 | 200 | Modification failed as the order has been completed. (Only applicable to Nitro Spread)  
51511 | 200 | Modification failed as the order price did not meet the requirement for Post Only.  
51512 | 200 | Failed to amend orders in batches. You cannot have duplicate orders in the same amend-batch-orders request.  
51513 | 200 | Number of modification requests that are currently in progress for an order cannot exceed 3 times.  
51514 | 200 | Order modification failed. The price length must be 32 characters or shorter.  
51521 | 200 | Failed to edit. Unable to edit reduce-only order because you don't have any positions of this contract.  
51522 | 200 | Failed to edit. A reduce-only order can't be in the same trading direction as your existing positions.  
51523 | 200 | Unable to modify the order price of a stop order that closes an entire position. Please modify the trigger price instead.  
51524 | 200 | Unable to modify the order quantity of a stop order that closes an entire position. Please modify the trigger price instead.  
51525 | 200 | Stop order modification is not available for quick margin  
51526 | 200 | Order modification unsuccessful. Take profit/Stop loss conditions cannot be added to or removed from stop orders.  
51527 | 200 | Order modification unsuccessful. The stop order does not exist.  
51528 | 200 | Unable to modify trigger price type  
51529 | 200 | Order modification unsuccessful. Stop order modification only applies to Expiry Futures and Perpetual Futures.  
51530 | 200 | Order modification unsuccessful. Take profit/Stop loss conditions cannot be added to or removed from reduce-only orders.  
51531 | 200 | Order modification unsuccessful. The stop order must have either take profit or stop loss attached.  
51532 | 200 | Your TP/SL can't be modified because it was partially triggered  
51536 | 200 | Unable to modify the size of the options order if the price type is pxUsd or pxVol.  
51537 | 200 | pxUsd or pxVol are not supported by non-options instruments  
51543 | 200 | When modifying take-profit or stop-loss orders for spot or margin trading, you can only adjust the price and quantity. Cancel the order and place a new one for other actions.  
51600 | 200 | Status not found.  
51601 | 200 | Order status and order id cannot exist at the same time.  
51602 | 200 | Either order status or order ID is required.  
51603 | 200 | Order does not exist.  
51604 | 200 | Initiate a download request before obtaining the hyperlink  
51605 | 200 | You can only download transaction data from the past 2 years  
51606 | 200 | Transaction data for the current quarter is not available  
51607 | 200 | Your previous download request is still being processed  
51608 | 200 | No transaction data found for the current quarter  
51610 | 200 | You can't download billing statements for the current quarter.  
51611 | 200 | You can't download billing statements for the current quarter.  
51620 | 200 | Only affiliates can perform this action  
51621 | 200 | The user isn’t your invitee  
51625 | 200 | One-click repay requires auto-borrow to be enabled. Please enable auto-borrow, or repay the debt currency via Easy Convert or spot trading.  
51156 | 200 | You're leading trades in long/short mode and can't use this API endpoint to close positions  
51159 | 200 | You're leading trades in buy/sell mode. If you want to place orders using this API endpoint, the orders must be in the same direction as your existing positions and open orders.  
51162 | 200 | You have {instrument} open orders. Cancel these orders and try again  
51163 | 200 | You hold {instrument} positions. Close these positions and try again  
51165 | 200 | The number of {instrument} reduce-only orders reached the upper limit of {upLimit}. Cancel some orders to proceed.  
51166 | 200 | Currently, we don't support leading trades with this instrument  
51167 | 200 | Failed. You have block trading open order(s), please proceed after canceling existing order(s).  
51168 | 200 | Failed. You have reduce-only type of open order(s), please proceed after canceling existing order(s)  
51320 | 200 | The range of coin percentage is {0}%-{1}%  
51321 | 200 | You're leading trades. Currently, we don't support leading trades with arbitrage, iceberg, or TWAP bots  
51322 | 200 | You're leading trades that have been filled at market price. We've canceled your open stop orders to close your positions  
51323 | 200 | You're already leading trades with take profit or stop loss settings. Cancel your existing stop orders to proceed  
51324 | 200 | As a lead trader, you hold positions in {instrument}. To close your positions, place orders in the amount that equals the available amount for closing  
51325 | 200 | As a lead trader, you must use market price when placing stop orders  
51326 | 200 | As a lead trader, you must use market price when placing orders with take profit or stop loss settings  
51820 | 200 | Request failed  
51821 | 200 | The payment method is not supported  
51822 | 200 | Quote expired  
51823 | 200 | Parameter {param} of buy/sell trading is inconsistent with the quotation  
51824 | 200 | You must bind a phone number to your account before using this feature  
51825 | 200 | You must bind an email to your account before using this feature  
54000 | 200 | Margin trading is not supported.  
54001 | 200 | Only Multi-currency margin account can be set to borrow coins automatically.  
54004 | 200 | Order placement or modification failed because one of the orders in the batch failed.  
54005 | 200 | Switch to isolated margin mode to trade pre-market expiry futures.  
54006 | 200 | Pre-market expiry future position limit is {posLimit}. Please cancel order or close position  
54007 | 200 | Instrument {instId} is not supported  
54008 | 200 | This operation is disabled by the 'mass cancel order' endpoint. Please enable it using this endpoint.  
54009 | 200 | The range of {param0} should be [{param1}, {param2}].  
54011 | 200 | Pre-market trading contracts are only allowed to reduce the number of positions within 1 hour before delivery. Please modify or cancel the order.  
54012 | 200 | Due to insufficient order book depth, we are now taking measures to protect your positions. Currently, you can only cancel orders, add margin to your positions, and place post-only orders. Your positions will not be liquidated. Trade will resume once order book depth returns to a safe level.  
54018 | 200 | Buy limit of {param0} USD exceeded. Your remaining limit is {param1} USD. (During the call auction)  
54019 | 200 | Buy limit of {param0} USD exceeded. Your remaining limit is {param1} USD. (After the call auction)  
54024 | 200 | Your order failed because you must enable {ccy} as collateral to trade expiry futures, perpetual futures, and options in cross-margin mode.  
54025 | 200 | Your order failed because you must enable {ccy} as collateral to trade margin, expiry futures, perpetual futures, and options in isolated margin mode.  
54026 | 200 | Your order failed because you must enable {ccy} and {ccy1} as collateral to trade the margin pair in isolated margin mode.  
54027 | 200 | Your order failed because you must enable {ccy} as collateral to trade options.  
54028 | 200 | Your order failed because you must enable {ccy} as collateral to trade spot in isolated margin mode.  
54029 | 200 | {param0} doesn’t exist within {param1}.  
54030 | 200 | Order failed. Your total value of same-direction {param0} open positions and orders can't exceed {param1} USD or {param2} of the platform's open interest.  
54031 | 200 | Order failed. The open interest of {param0} has reached the platform open interest limit. Positions opening orders cannot be placed. Please try again later.  
54035 | 200 | Order failed. The platform has reached the collateral limit for this crypto, so you can only place reduce-only orders.  
54036 | 200 | You can't place fill or kill orders when self-trade prevention is set to both maker and taker orders.  
54036 | 200 | You can't place fill or kill orders when self-trade prevention is set to both maker and taker orders.  
54039 | 200 | ELP orders can't be reduce-only orders.  
54040 | 200 | ELP orders can't be used with TP/SL settings.  
54041 | 200 | ELP orders aren't supported for {param0}.  
54042 | 200 | You don't have permission to place ELP orders for {param0}.  
54043 | 200 | You can only place up to {param1} ELP orders for {param0}. Cancel some of your orders and try again.  
54044 | 200 | ELP is not enabled for {param0}. You can’t place orders that take ELP liquidity of it.  
54045 | 200 | OpenAPI users can only place IOC orders that take ELP liquidity.  
54046 | 200 | You can’t place orders to take ELP liquidity.  
54047 | 200 | You can’t amend this order because an order with the same order ID or client order ID is in speed bump.  
54048 | 200 | You can’t cancel the order because an order with the same order ID or client order ID is in speed bump.  
54049 | 200 | API users can’t place orders that take ELP liquidity now because system is busy. To proceed, set isElpTakerAccess:false.  
54070 | 200 | The current function is not supported. Please update to the latest app version if using the app, or use the attachAlgoOrds array to place orders via Open API.  
54071 | 200 | Due to the platform system upgrade, this order no longer supports modifications. It is recommended to cancel and place a new order.  
54072 | 200 | This contract is currently view-only and not tradable.  
54073 | 200 | Couldn’t place order, as {param0} is at risk of depegging. Switch settlement currencies and try again.  
54074 | 200 | Your settings failed as you have positions, bot or open orders for USD contracts.  
54075 | 200 | Cross-crypto contracts are currently not supported in this account mode.  
54078 | 200 | If the main order is a buy order, the TP ratio must be greater than 0, while the SL ratio must be between -1 and 0. If the main order is a sell order, the TP ratio must be between -1 and 0, and the SL ratio must be greater than 0. Additionally, the ratio must be multiples of 0.0001.  
54079 | 200 | Dynamic change is available only for futures trading in futures mode or multi-currency mode. Note that when selecting dynamic change, the trigger price can only be calculated using the last price.  
54092 | 200 | Action Required: Please accept the TradFi Perps disclaimer on Web or App by attempting to place a TradFi Perp trade via the frontend. Each account, including sub-accounts, must separately accept the disclaimer before API trading is enabled  
54094 | 200 | Order rejected. The cool-off period is active for the current instId.  
  
#### Data class

Error Code | HTTP Status Code | Error Message  
---|---|---  
52000 | 200 | No market data found.

---

# 公共

错误码从 50000 到 53999  
  
  
  
存在子码格式，用来细分同一类报错的不同场景，如 51008_1000，其中 51008 是错误码，1000 是错误码子码。

#### 通用类

错误码 | HTTP 状态码 | 错误提示  
---|---|---  
0 | 200 |   
1 | 200 | 操作全部失败  
2 | 200 | 批量操作部分成功  
50000 | 400 | POST请求的body不能为空  
50001 | 503 | 服务暂时不可用，请稍后重试  
50002 | 400 | JSON 语法错误  
50004 | 400 | 接口请求超时（不代表请求成功或者失败，请检查请求结果）  
50005 | 410 | 接口已下线或无法使用  
50006 | 400 | 无效的 Content-Type，请使用“application/JSON”格式  
50007 | 200 | 用户被冻结  
50008 | 200 | 用户不存在  
50009 | 200 | 用户处于爆仓冻结  
50010 | 200 | 用户ID为空  
50011 | 200 | 用户请求频率过快，超过该接口允许的限额。请参考 API 文档并限制请求  
50011 | 429 | 请求频率太高  
50012 | 200 | 账户状态无效，请检查帐户的状态  
50013 | 429 | 当前系统繁忙，请稍后重试  
50014 | 400 | 必填参数{param0}不能为空  
50015 | 400 | 参数{param0}和{param1}不能同时为空  
50016 | 400 | 参数{param0}和{param1}不匹配  
50017 | 200 | 当前仓位处于自动减仓 (ADL) 冻结中，无法进行相关操作，请稍后重试  
50018 | 200 | {param0} 处于自动减仓 (ADL) 冻结中，无法进行相关操作，请稍后重试  
50019 | 200 | 当前账户处于自动减仓 (ADL) 冻结中，无法进行相关操作，请稍后重试  
50020 | 200 | 当前仓位处于强平冻结中，无法进行相关操作，请稍后重试  
50021 | 200 | {param0} 处于强平冻结中，无法进行相关操作，请稍后重试  
50022 | 200 | 当前账户处于强平冻结中，无法进行相关操作，请稍后重试  
50023 | 200 | 资金费冻结，无法进行相关操作，请稍后重试  
50024 | 200 | 参数{param0}和{param1}不能同时存在  
50025 | 200 | 参数{param0}传值个数超过最大限制{param1}  
50026 | 500 | 系统错误，请稍后重试  
50027 | 200 | 当前账户已被限制交易，请联系客服处理  
50028 | 200 | 账户异常无法下单  
50029 | 200 | 你的账户已经触发风控体系，禁止交易该标的，请检查您在欧易注册的电子邮件以便我们的客服联系  
50030 | 200 | 您没有使用此 API 接口的权限  
50032 | 200 | 您的账户已设置禁止该币种交易，请确认后重试  
50033 | 200 | 您的账户已设置禁止该业务线交易，请确认后重试  
50035 | 403 | 该接口要求APIKey必须绑定IP  
50036 | 200 | expTime 不能早于当前系统时间，请调整 expTime 后重试  
50037 | 200 | 订单已过期  
50038 | 200 | 模拟交易不支持该功能  
50039 | 200 | 时间戳分页时，不支持使用before参数  
50040 | 200 | 操作频繁，请稍后重试  
50041 | 200 | 用户 ID 未被列入白名单列表，请联系客服  
50042 | 200 | 请求重复  
50044 | 200 | 必须指定一种broker类型  
50045 | 200 | simPos 应为空。投资组合计算器纳入真实现货仓位时，暂不支持添加模拟仓位。  
50046 | 200 | 该功能暂时无法使用，我们正在进行维护，请稍后重试  
50047 | 200 | {param0} 已经交割，对应的K线请使用{param1}查询  
50048 | 200 | 切换对冲单元可能导致仓位风险水平升高，引起强制平仓。请调整仓位，使保证金处于安全状态。  
50049 | 200 | 无仓位档位信息，该币种不支持杠杆交易  
50050 | 200 | 您已开通期权交易服务，请勿重复开通  
50051 | 200 | 由于您所在国家或地区的合规限制，您无法使用该功能  
50052 | 200 | 根据当地的法律法规，您无法交易您选择的币种  
50053 | 200 | 该功能只支持模拟盘  
50055 | 200 | 资产重置失败，超过每日设置5次资产上限  
50056 | 200 | 当前账户有交易挂单或持仓，请完成全部撤单/平仓后进行重置  
50057 | 200 | 资产重置失败，请稍后重试  
50058 | 200 | 该币种不支持资产重置  
50059 | 200 | 继续下一步之前，请按照当地监管机构的要求完成额外步骤。您可以前往欧易网页端或 App 端了解详情。  
50060 | 200 | 根据当地法律法规，您需要完成身份认证方可继续使用我们的服务。  
50061 | 200 | 订单请求频率过快，超过账户允许的最高限额  
50062 | 200 | 该功能暂不可用  
50063 | 200 | 激活失败，您的体验金可能已过期或已激活  
50064 | 200 | 借币系统暂不可用，请稍后再试  
50067 | 200 | 当前接口不支持跨站交易功能  
50069 | 200 | 风险单元保证金率校验失败  
50071 | 200 | {param} 已存在  
e.g. clOrdId 已存在  
50072 | 200 | 跨币种保证金和组合保证金模式不再支持进行逐仓杠杆交易  
50075 | 200 | 该币种在伊斯兰子账户不可用  
50076 | 200 | 起始日期和结束日期的时间间隔不能超过{param0}天  
50077 | 200 | 起始日期和结束日期的时间间隔不能超过{param0}月  
  
#### API 类

错误码 | HTTP 状态码 | 错误提示  
---|---|---  
50100 | 400 | Api 已被冻结，请联系客服处理  
50101 | 401 | APIKey 与当前环境不匹配  
50102 | 401 | 请求时间戳过期  
50103 | 401 | 请求头"OK-ACCESS-KEY"不能为空  
50104 | 401 | 请求头"OK-ACCESS-PASSPHRASE"不能为空  
50105 | 401 | 请求头"OK-ACCESS-PASSPHRASE"错误  
50106 | 401 | 请求头"OK-ACCESS-SIGN"不能为空  
50107 | 401 | 请求头"OK-ACCESS-TIMESTAMP"不能为空  
50108 | 401 | 券商ID不存在  
50109 | 401 | 券商域名不存在  
50110 | 401 | 您的IP{param0}不在APIKey绑定IP名单中 (您可以将您的IP加入到APIKey绑定白名单中)  
50111 | 401 | 无效的OK-ACCESS-KEY  
50112 | 401 | 无效的OK-ACCESS-TIMESTAMP  
50113 | 401 | 无效的签名  
50114 | 401 | 无效的授权  
50115 | 405 | 无效的请求类型  
50116 | 200 | Fast API 只能创建一个 API key  
50118 | 200 | 如需将 API key 绑定 App，经纪商需要提供 IP 才能加入白名单  
50119 | 200 | API key 不存在  
50120 | 200 | API key 权限不足  
50121 | 200 | 您无权通过该 IP 地址 ({param0}) 访问  
50122 | 200 | 下单金额必须超过最低金额限制  
  
#### 交易类

错误码 | HTTP 状态码 | 错误提示  
---|---|---  
51000 | 400 | {param0}参数错误  
51001 | 200 | Instrument ID、Instrument ID code 或 Spread ID 不存在  
51002 | 200 | 交易产品ID不匹配指数  
51003 | 200 | ordId或clOrdId至少填一个  
51004_1101 | 200 | 下单失败，您在{instId} 逐仓的开平仓模式下，当前下单张数、同方向持有仓位以及同方向挂单张数之和，不能超过当前杠杆倍数允许的持仓上限{tierLimitQuantity}(张)，请调低杠杆或者使用新的子账户重新下单(当前杠杆：{leverage}×，当前下单张数：{size}张，同方向持有仓位：{posNumber}张，同方向挂单张数：{pendingNumber}张)。  
51004_1102 | 200 | 下单失败，您在{instId}全仓的开平仓模式下，当前下单张数、多空持有仓位以及多空挂单张数之和，不能超过当前杠杆倍数允许的持仓上限{tierLimitQuantity}(张)，请调低杠杆或者使用新的子账户重新下单(当前杠杆：{leverage}×，当前下单张数：{size}张，多空持有仓位{posLongShortNumber}张，多空挂单张数：{pendingLongShortNumber}张)。  
51004_1103 | 200 | 下单失败，您在{businessType}和交易品种{instFamily}的全仓开平仓模式下，当前下单张数、当前合约多空持有仓位、当前合约多空挂单张数以及其他合约占用额度之和，不能超过当前杠杆倍数允许的持仓上限{tierLimitQuantity}(张)，请调低杠杆或者使用新的子账户重新下单(当前杠杆：{leverage}×，当前下单张数：{size}张，当前合约多空持有仓位：{posLongShortNumber}张，当前合约多空挂单张数：{pendingLongShortNumber}张，其他合约占用额度：{otherQuote}张)。  
51004_1104 | 200 | 下单失败，您在{instId}的买卖模式下，当前买入张数、持有仓位、以及买入挂单张数之和，不能超过当前杠杆倍数允许的持仓上限{tierLimitQuantity}(张)，请调低杠杆或者使用新的子账户重新下单(当前杠杆：{leverage}×，当前买入张数：{size}张，持有仓位：{posNumber}张，买入挂单张数：{pendingNumber}张)。  
51004_1105 | 200 | 下单失败，您在{instId}的买卖模式下，当前卖出张数、持有仓位以及卖出挂单张数之和，不能超过当前杠杆倍数允许的持仓上限{tierLimitQuantity}(张)，请调低杠杆或者使用新的子账户重新下单(当前杠杆：{leverage}×，当前卖出张数：{size}张，持有仓位：{posNumber}张，卖出挂单张数：{pendingNumber}张)。  
51004_1106 | 200 | 下单失败，您在{businessType}和交易品种{instFamily}的全仓买卖模式下，当前买入张数、当前合约持有仓位、当前合约买入挂单张数以及其他合约占用额度之和，不能超过当前杠杆倍数允许的持仓上限{tierLimitQuantity}(张)，请调低杠杆或者使用新的子账户重新下单(当前杠杆：{leverage}×，当前买入张数：{size}张，当前合约持有仓位：{posNumber}张，当前合约买入挂单张数：{pendingNumber}张，其他合约占用额度：{otherQuota}张)。  
51004_1107 | 200 | 下单失败，您在{businessType}和交易品种{instFamily}的全仓买卖模式下，当前卖出张数、当前合约持有仓位、当前合约卖出挂单张数以及其他合约占用额度之和，不能超过当前杠杆倍数允许的持仓上限{tierLimitQuantity}(张)，请调低杠杆或者使用新的子账户重新下单(当前杠杆：{leverage}×，当前卖出张数：{size}张，当前合约持有仓位：{posNumber}张，当前合约卖出挂单张数：{pendingNumber}张，其他合约占用额度：{otherQuota}张)。  
51004_1111 | 200 | 修改订单失败，您在{instId} 逐仓的开平仓模式下，当前改单新增张数、同方向持有仓位以及同方向挂单张数之和，不能超过当前杠杆倍数允许的持仓上限{tierLimitQuantity}(张)，请调低杠杆或者使用新的子账户重新下单(当前杠杆：{leverage}×，当前改单新增张数：{size}张，同方向持有仓位：{posNumber}张，同方向挂单张数：{pendingNumber}张)。  
51004_1112 | 200 | 修改订单失败，您在{instId}全仓的开平仓模式下，当前改单新增张数、多空持有仓位以及多空挂单张数之和，不能超过当前杠杆倍数允许的持仓上限{tierLimitQuantity}(张)，请调低杠杆或者使用新的子账户重新下单(当前杠杆：{leverage}×，当前改单新增张数：{size}张，多空持有仓位{posLongShortNumber}张，多空挂单张数：{pendingLongShortNumber}张)。  
51004_1113 | 200 | 修改订单失败，您在{businessType}和交易品种{instFamily}的全仓开平仓模式下，当前改单新增张数、当前合约多空持有仓位、当前合约多空挂单张数以及其他合约占用额度之和，不能超过当前杠杆倍数允许的持仓上限{tierLimitQuantity}(张)，请调低杠杆或者使用新的子账户重新下单(当前杠杆：{leverage}×，当前改单新增张数：{size}张，当前合约多空持有仓位：{posLongShortNumber}张，当前合约多空挂单张数：{pendingLongShortNumber}张，其他合约占用额度：{otherQuote}张)。  
51004_1114 | 200 | 修改订单失败，您在{instId}的买卖模式下，修改当前买单新增张数、持有仓位、以及买入挂单张数之和，不能超过当前杠杆倍数允许的持仓上限{tierLimitQuantity}(张)，请调低杠杆或者使用新的子账户重新下单(当前杠杆：{leverage}×，修改当前买单新增张数：{size}张，持有仓位：{posNumber}张，买入挂单张数：{pendingNumber}张)。  
51004_1115 | 200 | 修改订单失败，您在{instId}的买卖模式下，修改当前卖单新增张数、持有仓位以及卖出挂单张数之和，不能超过当前杠杆倍数允许的持仓上限{tierLimitQuantity}(张)，请调低杠杆或者使用新的子账户重新下单(当前杠杆：{leverage}×，修改当前卖单新增张数：{size}张，持有仓位：{posNumber}张，卖出挂单张数：{pendingNumber}张)。  
51004_1116 | 200 | 修改订单失败，您在{businessType}和交易品种{instFamily}的全仓买卖模式下，修改当前买单新增张数、当前合约持有仓位、当前合约买入挂单张数以及其他合约占用额度之和，不能超过当前杠杆倍数允许的持仓上限{tierLimitQuantity}(张)，请调低杠杆或者使用新的子账户重新下单(当前杠杆：{leverage}×，修改当前买单新增张数：{size}张，当前合约持有仓位：{posNumber}张，当前合约买入挂单张数：{pendingNumber}张，其他合约占用额度：{otherQuota}张)。  
51004_1117 | 200 | 修改订单失败，您在{businessType}和交易品种{instFamily}的全仓买卖模式下，修改当前卖单新增张数、当前合约持有仓位、当前合约卖出挂单张数以及其他合约占用额度之和，不能超过当前杠杆倍数允许的持仓上限{tierLimitQuantity}(张)，请调低杠杆或者使用新的子账户重新下单(当前杠杆：{leverage}×，修改当前卖单新增张数：{size}张，当前合约持有仓位：{posNumber}张，当前合约卖出挂单张数：{pendingNumber}张，其他合约占用额度：{otherQuota}张)。  
51005 | 200 | 委托数量大于单笔上限  
51006 | 200 | 委托价格不在限价范围内（最高买入价：{param0}，最低卖出价：{param1}）  
51007 | 200 | 委托失败，委托数量不可小于 1 张  
51008_1000 | 200 | 委托失败，{param0} 可用余额不足，该委托会产生借币，当前账户可用保证金过低无法借币  
51008_1001 | 200 | 委托失败，账户 {param0} 可用保证金不足  
51008_1002 | 200 | 委托失败，请先增加可用保证金，再进行借币交易  
51008_1003 | 200 | 委托失败，账户 {param0} 可用保证金不足，且未开启自动借币（PM模式也可以尝试IOC订单降低风险）  
51008_1004 | 200 | {param0} 可用不足。借币数量超过档位限制，请尝试降低杠杆倍数。限价挂单以及当前下单需借 {param1}，剩余额度 {param2}，限额 {param3}，已用额度 {param4}。  
51008_1005 | 200 | 委托失败，因为 {param0} 剩余的限额 (主账户限额 + 当前账户锁定的尊享借币额度) 不足，导致可借不足 (限价挂单以及当前下单需借 {param1}，剩余额度 {param2}，限额 {param3}，已用额度 {param4})  
51008_1006 | 200 | 委托失败，您的下单数量超过了 {param0} 剩余的可借额度  
51008_1007 | 200 | 委托失败，该委托需要借币 {param0}，但该币种的平台剩余借币额度已不足  
51008_1009 | 200 | 委托失败，账户可用保证金过低（PM模式也可以尝试IOC订单降低风险）  
51008_1010 | 200 | 委托失败，Delta 校验未通过，因为若成功下单，有效保证金 (adjEq) 的变化值将小于初始保证金 (IMR) 的变化值。建议增加 adjEq 或减少 IMR 占用。（PM模式也可以尝试IOC订单降低风险）  
51008_1015 | 200 | 委托失败，账户可用余额不足，其中不包含已触发平台质押限制的币种资产 {param0}  
51008_1016 | 200 | 委托失败，{param0} 可用余额不足，该委托会产生借币，当前账户可用保证金过低无法借币。账户可用保证金不包含已触发平台质押限制的币种资产 {param1}  
51008_1017 | 200 | 委托失败，该委托所需的借币数量已超过您的档位限制。下单后产生的总借币量为 {param1} {param0}，{param2}x 杠杆的借币上限为 {param3} {param0}。请降低杠杆倍数后再重新下单。  
51008_1018 | 200 | 委托失败，该委托所需的借币数量已超过您的档位限制。下单后产生的总潜在借币量为 {param1} {param0}，{param2}x 杠杆的借币上限为 {param3} {param0}。请降低杠杆倍数后再重新下单。  
51008_1019 | 200 | 委托失败，您主账户的 {param0} 借币额度不足  
51008_1020 | 200 | 委托失败，扣除计价货币手续费后，您的 {param0} 余额不足以完成该委托。请关闭使用计价货币支付现货手续费开关后重试。  
51009 | 200 | 下单功能被冻结，请联系客服进行处理  
51010 | 200 | 当前账户模式不支持此操作  
51011 | 200 | ordId重复  
51012 | 200 | 币种不存在  
51014 | 200 | 指数不存在  
51015 | 200 | instId和instType不匹配  
51016 | 200 | clOrdId重复  
51017 | 200 | 杠杆委托交易借币超出限额  
51018 | 200 | 期权交易账户不能有净开空持仓  
51019 | 200 | 期权全仓不能有净开多持仓  
51020 | 200 | 委托数量需大于或等于最小下单数量  
51021 | 200 | 币对或合约待上线  
51022 | 200 | 合约暂停中  
51023 | 200 | 仓位不存在  
51024 | 200 | 交易账户冻结  
51024 | 200 | 根据服务条款，我们很遗憾地通知您，我们无法为您提供服务。如果您有任何问题，请联系我们的客服。  
51024 | 200 | 根据您的要求，该账号已被冻结，如有问题请及时联系客服处理。  
51024 | 200 | 您的账户近期做了相关安全设置变更，为保证您的资金安全，暂无法进行此操作，如有问题请您及时联系客服处理。  
51024 | 200 | 您的账户已完成全部资产支取，为保证您的信息安全，该账户已永久冻结，若有问题，请您及时联系客服处理。  
51024 | 200 | 您的认证信息疑似存在安全风险，为保证您的资金安全，暂无法进行此操作，请您及时联系客服处理。  
51024 | 200 | 您的认证信息不符合年龄规定，为保证您的资金安全，暂无法进行此操作，请您及时联系客服处理。  
51024 | 200 | 根据合规要求，您的认证国家或地区已禁止交易，您可以平掉所有仓位。如有问题请及时联系客服处理。  
51024 | 200 | 您的认证信息疑似存在多次认证，为保证您的资金安全，暂无法进行此操作，请您及时联系客服处理。  
51024 | 200 | 您的账户已被司法冻结，暂无法进行此操作，如有问题请您及时联系客服处理。  
51024 | 200 | 无法进行此操作。请首先解决您现有的 C2C申诉。  
51024 | 200 | 您的账户疑似存在合规风险，为保证您的资金安全，暂无法进行此操作，请您及时联系客服处理。  
51024 | 200 | 根据您的交易需求，暂无法进行此操作，如有问题请及时联系客服处理。  
51024 | 200 | 由于您的账户触发平台风控，暂无法进行此操作，有疑问请您联系客服。  
51024 | 200 | 此账户暂无法使用，有任何疑问您可以联系客服。  
51024 | 200 | 此账户提币功能暂无法使用，有任何疑问您可以联系客服。  
51024 | 200 | 此账户资金账户划转功能暂无法使用，有任何疑问您可以联系客服。  
51024 | 200 | 因您进行法币交易时违反了《平台法币交易规则》，故不再为您提供法币交易功能的相关服务，您账户的充币提币以及其他交易功能不受影响。  
51024 | 200 | 请注意查收邮件内容，回复认证团队发送邮件，有任何问题，请联系认证团队。  
51024 | 200 | 根据您的要求，该账号已被关闭，如有问题请及时联系客服处理。  
51024 | 200 | 您的账户疑似存在安全风险，为保证您的资金安全，暂无法进行此操作，请您及时联系客服处理。  
51024 | 200 | 您的账户疑似存在安全风险，暂无法兑换，请您及时联系客服处理  
51024 | 200 | 您的账号已冻结，部分功能将被禁用，如您希望解除账号限制，请前往帮助中心联系平台客服。  
51024 | 200 | 根据合规要求，您的认证国家或地区已禁止交易，您可以撤销已有的订单。如有问题请及时联系客服处理。  
51024 | 200 | 您的认证国家为交易禁止国，根据合规要求，暂无法进行此操作，如有问题请您及时联系客服处理。  
51024 | 200 | 根据当地法律法规，您所在的国家或地区无法使用该产品。如果您的常居住地不是本国家或地区，并持有有效身份证件，您可继续使用欧易的交易所产品。  
51024 | 200 | 请注意您在建立托管交易子账户后的前30分钟内可能无法划转或进行交易，请耐心等待并稍后再试。  
51024 | 200 | 此功能暂不可用，完成高级身份认证后即可正常使用  
51024 | 200 | 由于您未能及时更新认证信息，您账户的充币与交易功能已受限。请尽快更新认证，以解除账户限制。  
51024 | 200 | 超出限制的子账户不能开仓，只能减仓或平仓，请尝试使用其他账户进行交易。  
51025 | 200 | 委托笔数超限  
51026 | 200 | 交易产品类型不匹配指数（instType和uly不匹配）  
51027 | 200 | 合约已到期  
51028 | 200 | 合约交割中  
51029 | 200 | 合约结算中  
51030 | 200 | 资金费结算中  
51031 | 200 | 委托价格不在平仓限价范围内  
51032 | 200 | 市价全平中  
51033 | 200 | 币对单笔交易已达限额  
51034 | 200 | 成交速率超出您所设置的上限，请将做市商保护状态重置为 inactive 以继续交易。  
51035 | 200 | 用户没有做市订单的下单权限  
51036 | 200 | 仅 PM 账户的期权业务线支持 MMP 类型订单  
51411 | 200 | 用户没有执行mass cancel的权限  
51042 | 200 | PM 账户模式下，期权仅支持持仓模式为全仓的 MMP 类型订单  
51043 | 200 | 该逐仓仓位不存在  
59509 | 200 | 用户没有重置做市商保护状态的权限  
51037 | 200 | 当前账户风险状态，仅支持降低账户风险方向的IOC订单  
51038 | 200 | 当前风险模块下已经存在降低账户风险方向的IOC类型订单  
51039 | 200 | PM账户下交割和永续的全仓不能调整杠杆倍数  
51040 | 200 | 期权逐仓的买方不能调整保证金  
51041 | 200 | PM账户仅支持买卖模式  
51044 | 200 | 当前订单类型{param0}， {param1}不支持设置止盈和止损  
51046 | 200 | 止盈触发价格应该大于委托价格  
51047 | 200 | 止损触发价格应该小于委托价格  
51048 | 200 | 止盈触发价格应该小于委托价格  
51049 | 200 | 止损触发价格应该大于委托价格  
51050 | 200 | 止盈触发价格应该大于卖一价  
51051 | 200 | 止损触发价格应该小于卖一价  
51052 | 200 | 止盈触发价格应该小于买一价  
51053 | 200 | 止损触发价格应该大于买一价  
51054 | 500 | 请求超时，请稍候重试  
51055 | 200 | 组合保证金模式暂不支持合约网格  
51056 | 200 | 当前策略不支持该操作  
51057 | 200 | 当前账户模式暂不支持此交易策略，请前往“交易设置 > 账户模式”进行切换  
51058 | 200 | 该策略无仓位  
51059 | 200 | 策略当前状态不支持此操作  
51065 | 200 | algoClOrdId 重复  
51066 | 200 | 期权交易不支持市价单，请用限价单平仓  
51068 | 200 | {param0} 已经在 algoClOrdId 和 attachAlgoClOrdId 中存在。  
51069 | 200 | 不存在该{param0}相关的期权合约  
51070 | 200 | 您当前尚未达到升级至该账户模式的要求，请先在官方网站或APP完成账户模式的升级。  
51071 | 200 | 当前维护的标签维度倒计时全部撤单达到数量上限  
51072 | 200 | 您当前身份为现货带单员，设置的带单币对买入时，tdMode 需要使用 spot_isolated  
51073 | 200 | 您当前身份为现货带单员，卖出带单资产需要使用'/copytrading/close-subposition'接口  
51074 | 200 | 仅现货带单员设置的带单币对支持使用 tdMode：spot_isolated  
51075 | 200 | 现货跟单平仓单只支持修改价格，不支持修改数量  
51076 | 200 | 分批止盈的每笔止盈止损订单仅支持单向止盈止损，slTriggerPx&slOrdPx 与 tpTriggerPx&tpOrdPx 只能填写一组  
51077 | 200 | 现货和杠杆暂不支持多笔止盈和成交价止损  
51078 | 200 | 您当前身份为带单交易员，不支持分批止盈  
51079 | 200 | 同一笔订单上附带分批止盈的止盈委托单不能超过 {param0} 笔  
51080 | 200 | 同一笔订单上附带分批止盈的止盈触发价类型 (tpTriggerPxType) 必须保持一致  
51081 | 200 | 同一笔订单上附带分批止盈的止盈触发价 (tpTriggerPx) 不能相等  
51082 | 200 | 同一笔订单上附带分批止盈，其中触发止盈的止盈委托价 (tpOrdPx) 只能是市价  
51083 | 200 | 同一笔订单上附带分批止盈的止盈数量之和需要等于订单的委托数量  
51084 | 200 | 同一笔订单上附带分批止盈的止损委托单不能超过 {param0} 笔  
51085 | 200 | 附带止盈止损开启'开仓价止损'时 (amendPxOnTriggerType 设置为 1)，该笔订单上的止盈委托单必须大于等于 2 笔  
51086 | 200 | 同一笔订单上附带止盈止损委托单不能超过 {param0} 笔  
51538 | 200 | 若下单时使用了 attachAlgoOrds 参数，也需要使用 attachAlgoOrds 参数改单；若下单时没有使用 attachAlgoOrds 参数，则不支持使用 attachAlgoOrds 参数改单。  
51539 | 200 | 修改同一笔订单上分批止盈中的止盈止损订单时，attachAlgoId 或者 attachAlgoClOrdId 的值不能重复  
51527 | 200 | 改单失败，其中至少有一个附带的止盈止损订单不存在  
51087 | 200 | 该币种取消上线，当前不支持交易  
51088 | 200 | 对于同一个仓位，仅支持一笔全部平仓的止盈止损挂单  
51089 | 200 | 在附带分批止盈时，止盈订单的数量不能为空  
51090 | 200 | 对于绑定了限价止盈的止损订单，不允许修改其委托数量  
51091 | 200 | 同一笔订单上附带分批止盈的止盈类型必须保持一致  
51092 | 200 | 同一笔订单上附带分批止盈的止盈委托价不能相等  
51093 | 200 | 同一笔订单上附带分批止盈，其中限价止盈的止盈委托价 (tpOrdPx) 不能为 –1 (市价)  
51094 | 200 | 币币、杠杆和期权交易不支持限价止盈  
51095 | 200 | 该接口下限价止盈订单时，也需要同时下一笔止损订单  
51096 | 200 | 限价止盈时 cxlOnClosePos 需要为 true  
51098 | 200 | 对于绑定了限价止盈的止损订单，不能添加新的止盈  
51099 | 200 | 您当前身份为带单交易员，不支持下单限价止盈  
51178 | 200 | 使用 attachAlgoClOrdId 时，tpTriggerPx&tpOrdPx 或者 slTriggerPx&slOrdPx 不能为空。  
51100 | 200 | 下单失败，只减仓订单不能附带止盈止损。  
51101 | 200 | 操作失败，单笔委托数量不能大于{maxSzPerOrder}(张)。  
51102 | 200 | 操作失败，当前合约的累计挂单数量不能大于{maxNumberPerInstrument}(单)。  
51103 | 200 | 操作失败，{businessType}的当前交易品种下，所有合约累计挂单数量不能大于{maxNumberPerInstFamily}(单)。  
51104 | 200 | 操作失败，{businessType}的当前交易品种下，所有合约累计挂单张数不能大于{maxSzPerInstFamily} (张)。  
51105 | 200 | 操作失败，当前合约的持仓张数和同方向挂单张数之和不能大于{maxPositionSzPerInstrument}(张)。  
51106 | 200 | 操作失败，{businessType}的当前交易品种下，所有合约累计持仓张数和同方向挂单张数之和不能大于{maxPostionSzPerInstFamily51106}(张)。  
51107 | 200 | 操作失败，{businessType}的当前交易品种下，所有合约累计持仓张数和双向挂单张数之和不能大于{maxPostionSzPerInstFamily51107}(张)。  
51108 | 200 | 持仓量超过市价全平最大限制  
51109 | 200 | 订单深度中无买一卖一价  
51110 | 200 | 集合竞价开始后方可下限价单  
51111 | 200 | 批量下单时，超过最大单数{param0}  
51112 | 200 | 平仓张数大于该仓位的可平张数  
51113 | 429 | 市价全平操作过于频繁  
51115 | 429 | 市价全平前请先撤销所有平仓单  
51116 | 200 | 委托价格或触发价格超过{param0}  
51117 | 200 | 平仓单挂单单数超过限制  
51120 | 200 | 下单数量不足{param0}张  
51121 | 200 | 下单张数应为一手张数的倍数  
51122 | 200 | 委托价格小于最小值{param0}  
51123 | 200 | 最小价格增量为空  
51124 | 200 | 价格发现期间您只可下限价单  
51125 | 200 | 当前杠杆存在非只减仓挂单，请撤销所有非只减仓挂单后进行只减仓挂单  
51126 | 200 | 当前杠杆存在只减仓挂单，请撤销所有只减仓挂单后进行非只减仓挂单  
51127 | 200 | 仓位可用余额为0  
51128 | 200 | 跨币种账户无法进行全仓杠杆交易  
51129 | 200 | 持仓及买入订单价值已达到持仓限额，不允许继续买入  
51130 | 200 | 逐仓杠杆保证金币种错误  
51131 | 200 | 仓位可用余额不足  
51132 | 200 | 仓位正资产小于最小交易单位  
51133 | 200 | 跨币种全仓币币不支持只减仓功能  
51134 | 200 | 平仓失败，您当前没有杠杆仓位，请关闭只减仓后继续  
51135 | 200 | 您的平仓价格已触发限价，最高买入价格为{param0}  
51136 | 200 | 您的平仓价格已触发限价，最低卖出价格为{param0}  
51137 | 200 | 买单最高价为 {param0}，请调低价格  
51138 | 200 | 卖单最低价为 {param0}，请调高价格  
51139 | 200 | 现货模式下币币不支持只减仓功能  
51140 | 200 | 由于盘口卖单不足，下单失败，请稍后重试  
51142 | 200 | 盘口无有效报价，用USDT模式下单无法成交，请尝试切换到币种模式  
51143 | 200 | 兑换数量不足  
51144 | 200 | 请使用 {param0} 进行下单  
51147 | 200 | 交易期权需要在交易账户资产总价值大于1万美元的前提下，开通期权交易服务  
51148 | 200 | 下单失败，当前订单若下单成功会造成只减仓订单反向开仓，请撤销或修改原有挂单再进行下单  
51149 | 500 | 下单超时，请稍候重试 (不代表请求成功或失败，请检查请求结果)  
51150 | 200 | 交易数量或价格的精度超过限制  
51152 | 200 | 一键借币模式下，不支持自动借币与自动还币和手动类型混合下单。  
51153 | 200 | 无法在一键借币模式下手动借币，您输入的金额已超过可借上限  
51154 | 200 | 无法手动归还一键借币模式下的借币，您输入的还币金额已超过该币种可用余额  
51155 | 200 | 由于您所在国家或地区的合规限制，您无法交易此币对或合约  
51158 | 200 | 自主划转已不支持，请切换至一键借币模式下单 (isoMode=quick_margin)  
51164 | 200 | 您当前身份为带单交易员，无法切换至组合保证金账户  
51169 | 200 | 下单失败，您没有当前合约对应方向的持仓，无法进行平仓或者减仓。  
51170 | 200 | 下单失败，只减仓下单方向不能与持仓方向相同  
51171 | 200 | 改单失败，当前订单若改单成功会造成只减仓订单反向开仓，请撤销或修改原有挂单再进行改单  
51173 | 200 | 无法市价全平，当前仓位暂无负债  
51174 | 200 | 操作失败，当前 {param0} 的累计挂单数量已达上限 {param1} (单)  
51175 | 200 | 参数 {param0}、{param1} 和 {param2} 不能同时为空  
51176 | 200 | 参数 {param0}、{param1} 和 {param2} 只能填写一个  
51177 | 200 | 当前期权订单的价格类型为{param0}，不支持修改{param1}  
51179 | 200 | 现货模式下，不支持使用{param0}进行期权下单。  
51180 | 200 | {param0}的范围应为({param1}, {param2})  
51181 | 200 | 使用{param0}下单，ordType 只能为限价单 (limit)  
51182 | 200 | 当前账户期权价格类型 pxUsd 和 pxVol 的挂单数量之和，不能超过 {param0} 个  
51185 | 200 | 单笔订单价值不能超过 {maxOrderValue} USD  
51186 | 200 | 下单失败。在当前保证金模式下，您针对 {param0} 的杠杠倍数设置为 {param1}x，大于平台允许的最大杠杠倍数 {param2}x，请调低杠杆。  
51187 | 200 | 下单失败，您在 {param0} {param1} 和当前保证金模式下，当前下单张数、持仓及挂单张数之和 {param2}，已超过平台上限 {param3} 张，请修改当前订单数量，或撤单、平仓。  
51192 | 200 | 输入IV值对应的 {param0} 期权价格超过最低卖价 {param1} {param2}，请重新输入合理的IV值。  
51193 | 200 | 输入IV值对应的 {param0} 期权价格超过最高买价 {param1} {param2}，请重新输入合理的IV值。  
51194 | 200 | 输入USD订单价格对应的 {param0} 期权价格超过最低卖价 {param1} {param2}，请重新输入合理的USD订单价格。  
51195 | 200 | 输入USD订单价格对应的 {param0} 期权价格超过最高买价 {param1} {param2}，请重新输入合理的USD订单价格。  
51196 | 200 | 在提前挂单期间，您只能下限价单。  
51197 | 200 | 在提前挂单开始后，您才能下限价单。  
51201 | 200 | 市价委托单笔价值不能超过 1,000,000 USDT  
51202 | 200 | 市价单下单数量超出最大值  
51203 | 200 | 普通委托数量超出最大限制{param0}  
51204 | 200 | 限价委托单价格不能为空  
51205 | 200 | 不支持只减仓操作  
51206 | 200 | 请先撤销当前下单产品{param0}的只减仓挂单，避免反向开仓  
51207 | 200 | 交易数量超过限制，无法市价全平，请手动下单分批平仓  
51209 | 200 | 下单失败。当前账户状态下，仅支持下降低 Delta 值的订单。请增加您的账户权益，或下一笔降低 Delta 值的订单，待该订单后成交后再继续操作  
51210 | 200 | 下单失败。当前账户状态下，基础货币相同的现货、永续和交割合约间仅能下一笔降低 Delta 值的订单，请撤销其他订单后再继续操作  
51211 | 200 | 下单失败。当前账户状态下，仅支持下降低 Delta 值的订单。请增加您的账户权益，或下一笔降低 Delta 值的订单，待该订单后成交后再继续操作  
51212 | 200 | 下单失败。当前不支持批量下单，请分开下单  
51213 | 200 | 下单失败。当前账户状态下，基础货币相同的现货、永续和交割合约间仅能下一笔降低 Delta 值的订单，请撤销其他订单后再继续操作  
51214 | 200 | 改单失败。当前账户状态下，仅支持下降低 Delta 值的订单。请增加您的账户权益，或下一笔降低 Delta 值的订单，待该订单后成交后再继续操作  
51220 | 200 | 分润策略仅支持策略停止时卖币或停止时全部平仓  
51221 | 200 | 请输入 0-30% 范围内的指定分润比例  
51222 | 200 | 该策略不支持分润  
51223 | 200 | 当前状态您不可以进行分润带单  
51224 | 200 | 该币对不支持分润  
51225 | 200 | 分润跟单策略不支持手动立即触发策略  
51226 | 200 | 分润跟单策略不支持修改策略参数  
51250 | 200 | 策略委托价格不在正确范围内  
51251 | 200 | 创建冰山委托时，策略委托类型错误  
51252 | 200 | 策略委托数量不在正确范围内  
51253 | 200 | 冰山委托单笔均值超限  
51254 | 200 | 冰山委托单笔均值错误  
51255 | 200 | 冰山委托单笔委托超限  
51256 | 200 | 冰山委托深度错误  
51257 | 200 | 跟踪委托回调服务错误，回调幅度限制为{min}<x<={max}%  
51258 | 200 | 跟踪委托失败，卖单激活价格需大于最新成交价格  
51259 | 200 | 跟踪委托失败，买单激活价格需小于最新成交价格  
51260 | 200 | 每个用户最多可同时持有{param0}笔未成交的跟踪委托  
51261 | 200 | 每个用户最多可同时持有{param0}笔未成交的止盈止损  
51262 | 200 | 每个用户最多可同时持有{param0}笔未成交的冰山委托  
51263 | 200 | 每个用户最多可同时持有{param0}笔未成交的时间加权单  
51264 | 200 | 时间加权单笔均值超限  
51265 | 200 | 时间加权单笔上限错误  
51267 | 200 | 时间加权扫单比例出错  
51268 | 200 | 时间加权扫单范围出错  
51269 | 200 | 时间加权委托间隔错误，应为{min}<=x<={max}  
51270 | 200 | 时间加权委托深度限制为 0<x<=1%  
51271 | 200 | 时间加权委托失败，扫单比例应该为 0<x<=100%  
51272 | 200 | 时间加权委托失败，扫单范围应该为 0<x<=1%  
51273 | 200 | 时间加权委托总量应为大于 0  
51274 | 200 | 时间加权委托总数量需大于单笔上限  
51275 | 200 | 止盈止损市价单笔委托数量不能超过最大限制  
51276 | 200 | 止盈止损市价单不能指定价格  
51277 | 200 | 止盈触发价格不能大于最新成交价  
51278 | 200 | 止损触发价格不能小于最新成交价  
51279 | 200 | 止盈触发价格不能小于最新成交价  
51280 | 200 | 止损触发价格不能大于最新成交价  
51281 | 200 | 计划委托不支持使用tgtCcy参数  
51282 | 200 | 吃单价优于盘口的比例范围  
51283 | 200 | 时间间隔的范围{param0}s~{param1}s  
51284 | 200 | 单笔数量的范围{param0}~{param1}  
51285 | 200 | 委托总量的范围{param0}~{param1}  
51286 | 200 | 下单金额需大于等于{param0}  
51287 | 200 | 当前策略不支持此交易品种  
51288 | 200 | 策略正在停止中，请勿重复点击  
51289 | 200 | 策略配置不存在，请稍后再试  
51290 | 200 | 策略引擎正在升级，请稍后重试  
51291 | 200 | 策略不存在或已停止  
51292 | 200 | 策略类型不存在  
51293 | 200 | 策略不存在  
51294 | 200 | 该策略暂不能创建，请稍后再试  
51295 | 200 | PM账户不支持ordType为{param0}的策略委托单  
51298 | 200 | 交割、永续合约的买卖模式下，不支持计划委托  
51299 | 200 | 策略委托失败，用户最多可持有{param0}笔该类型委托  
51300 | 200 | 止盈触发价格不能大于标记价格  
51302 | 200 | 止损触发价格不能小于标记价格  
51303 | 200 | 止盈触发价格不能小于标记价格  
51304 | 200 | 止损触发价格不能大于标记价格  
51305 | 200 | 止盈触发价格不能大于指数价格  
51306 | 200 | 止损触发价格不能小于指数价格  
51307 | 200 | 止盈触发价格不能小于指数价格  
51308 | 200 | 止损触发价格不能大于指数价格  
51309 | 200 | 集合竞价期间不能创建策略  
51310 | 200 | 逐仓自主划转保证金模式不支持ordType为iceberg、twap的策略委托单  
51311 | 200 | 移动止盈止损委托失败，回调幅度限制为{min}<x<={max}  
51312 | 200 | 移动止盈止损委托失败，委托数量范围{min}<x<={max}  
51313 | 200 | 逐仓自主划转模式不支持策略部分  
51317 | 200 | 币币杠杆不支持计划委托  
51327 | 200 | closeFraction 仅适用于交割合约和永续合约  
51328 | 200 | closeFraction 仅适用于只减仓订单  
51329 | 200 | closeFraction 仅适用于买卖模式  
51330 | 200 | closeFraction 仅适用于止盈止损市价订单  
51331 | 200 | closeFraction仅限于平仓单  
51332 | 200 | 组合保证金模式不支持closeFraction  
51333 | 200 | 开平模式下的平仓单或买卖模式下的只减仓单无法附带止盈止损  
51340 | 200 | 投入保证金需大于{0}{1}  
51341 | 200 | 当前策略状态下暂不支持平仓  
51342 | 200 | 已有平仓单，请稍后重试  
51343 | 200 | 止盈价格需小于区间最低价格  
51344 | 200 | 止损价格需大于区间最高价格  
51345 | 200 | 策略类型不是网格策略  
51346 | 200 | 最高价格不能低于最低价格  
51347 | 200 | 暂无可提取利润  
51348 | 200 | 止损价格需小于区间最低价格  
51349 | 200 | 止盈价格需大于区间最高价格  
51350 | 200 | 暂无可推荐参数  
51351 | 200 | 单格收益必须大于0  
51352 | 200 | 币对数量范围{pairNum1} - {pairNum2}  
51353 | 200 | 存在重复币对{existingPair}  
51354 | 200 | 币对比例总和需等于100%  
51355 | 200 | 定投日期范围{date1} - {date2}  
51356 | 200 | 定投时间范围{0}~{1}  
51357 | 200 | 时区范围 {timezone1} - {timezone2}  
51358 | 200 | 每个币种的投入金额需大于{amount}  
51359 | 200 | 暂不支持定投该币种{0}  
51370 | 200 | 杠杆倍数范围{0}~{1}  
51380 | 200 | 市场行情不符合策略配置  
51381 | 200 | 单网格利润率不在区间内  
51382 | 200 | 策略不支持停止信号触发  
51383 | 200 | 最小价格必须小于最新成交价  
51384 | 200 | 信号触发价格必须大于最小价格  
51385 | 200 | 止盈价必须大于最小价格  
51386 | 200 | 最小价格必须大于1/2最新成交价  
51387 | 200 | 止损价格应小于无限网格的区间最低价  
51388 | 200 | 策略已在运行中  
51389 | 200 | 触发价格需小于{0}  
51390 | 200 | 触发价格需小于止盈价格  
51391 | 200 | 触发价格需大于止损价格  
51392 | 200 | 止盈价格需大于触发价格  
51393 | 200 | 止损价格需小于触发价格  
51394 | 200 | 触发价格需大于止盈价格  
51395 | 200 | 触发价格需小于止损价格  
51396 | 200 | 止盈价格需小于触发价格  
51397 | 200 | 止损价格需大于触发价格  
51398 | 200 | 当前行情满足停止条件，无法创建策略  
51399 | 200 | 当前杠杆下最大可投入金额为 {amountLimit} {quoteCurrency}，请减少投入金额后再试。  
51400 | 200 | 由于订单已完成、已撤销或不存在，撤单失败  
51400 | 200 | 撤单失败，订单不存在（仅适用于价差速递）  
51401 | 200 | 撤单失败，订单已撤销（仅适用于价差速递）  
51402 | 200 | 撤单失败，订单已完成（仅适用于价差速递）  
51403 | 200 | 撤单失败，该委托类型无法进行撤单操作  
51404 | 200 | 价格发现第二阶段您不可撤单  
51405 | 200 | 撤单失败，您当前没有未成交的订单  
51406 | 400 | 撤单数量超过最大允许单数{param0}  
51407 | 200 | ordIds 和 clOrdIds 不能同时为空  
51408 | 200 | 币对 id 或币对名称与订单信息不匹配  
51409 | 200 | 币对 id 或币对名称不能同时为空  
51410 | 200 | 撤单失败，订单已处于撤销中或结算中  
51411 | 200 | 用户没有执行mass cancel的权限  
51412 | 200 | 撤单超时，请稍后重试  
51416 | 200 | 委托已触发，暂不支持撤单  
51413 | 200 | 撤单失败，接口不支持该委托类型的撤单  
51415 | 200 | 下单失败，现货交易仅支持设置最新价为触发价格，请更改触发价格并重试  
51416 | 200 | 委托已触发，暂不支持撤单  
51500 | 200 | 价格、数量、止盈/止损不能同时为空  
51501 | 400 | 修改订单超过最大允许单数{param0}  
51502_1030 | 200 | 修改失败，{param0} 可用余额不足，该委托会产生借币，当前账户可用保证金过低无法借币  
51502_1031 | 200 | 修改订单失败，账户 {param0} 可用保证金不足  
51502_1032 | 200 | 委托失败，请先增加可用保证金，再进行借币交易  
51502_1033 | 200 | 修改订单失败，账户 {param0} 可用保证金不足，且未开启自动借币（PM模式也可以尝试IOC订单降低风险）  
51502_1034 | 200 | {param0} 可用不足。借币数量超过档位限制，请尝试降低杠杆倍数。限价挂单以及当前下单需借 {param1}，剩余额度 {param2}，限额 {param3}，已用额度 {param4}。  
51502_1035 | 200 | 修改订单失败，因为 {param0} 剩余的限额 (主账户限额+当前账户锁定的尊享借币额度) 不足，导致可借不足。限价挂单以及当前下单需借 {param1}，剩余额度 {param2}，限额 {param3}，已用额度 {param4}。  
51502_1036 | 200 | 修改订单失败，因为 {param0} 剩余的币对限额不足，导致可借不足  
51502_1037 | 200 | 改单失败，该委托需要借币 {param0}，但该币种的平台剩余借币额度已不足  
51502_1039 | 200 | 修改订单失败，账户可用保证金过低（PM模式也可以尝试IOC订单降低风险）  
51502_1040 | 200 | 修改订单失败，Delta 校验未通过，因为若成功下单，adjEq 的变化值将小于 IMR 的变化值。建议增加 adjEq 或减少 IMR 占用。（PM模式也可以尝试IOC订单降低风险）  
51502_1049 | 200 | 修改订单失败，您主账户的 {param0} 借币额度不足  
51503 | 200 | 由于订单已完成、已撤销或不存在，改单失败  
51503 | 200 | 由于订单不存在，改单失败（仅适用于价差速递）  
51505 | 200 | {instId} 不处于集合竞价阶段  
51506 | 200 | 订单类型不支持改单  
51507 | 200 | 您仅能在币种上线至少 5 分钟后进行市价委托  
51508 | 200 | 集合竞价第一阶段和第二阶段不允许改单  
51509 | 200 | 修改订单失败,订单已撤销（仅适用于价差速递）  
51510 | 200 | 修改订单失败,订单已完成（仅适用于价差速递）  
51511 | 200 | 操作失败，订单价格不满足Post Only条件  
51512 | 200 | 批量修改订单失败。同一批量改单请求中不允许包含相同订单。  
51513 | 200 | 对于正在处理的同一订单，改单请求次数不得超过3次  
51514 | 200 | 修改订单失败，价格长度不能超过 32 个字符  
51521 | 200 | 改单失败，当前合约无持仓，无法修改只减仓订单  
51522 | 200 | 改单失败，只减仓订单方向不能与持仓反向相同  
51532 | 200 | 止盈止损已触发，无法改单  
51524 | 200 | 不允许在全部仓位止盈止损单上修改委托数量，请修改触发价格  
51525 | 200 | 一键借币止盈止损单不支持修改  
51526 | 200 | 改单失败，止盈止损单不支持增加或删除止盈/止损  
51527 | 200 | 改单失败，止盈止损订单不存在  
51528 | 200 | 止盈止损不支持修改触发类型  
51529 | 200 | 改单失败，只有交割、永续合约单可以修改止盈止损  
51530 | 200 | 改单失败，只减仓订单不能附带止盈止损  
51531 | 200 | 改单失败，止盈止损单修改必须保留一个方向  
51536 | 200 | 期权的 pxVol 或者 pxUsd 订单不支持修改订单数量  
51537 | 200 | 非期权产品不支持使用 pxUsd 或者 pxVol  
51543 | 200 | 修改现货或杠杆的止盈止损订单时，仅支持调整价格和数量。如需其他操作，请撤单后重新下单。  
51600 | 200 | 查询订单的状态不存在  
51601 | 200 | 订单状态和订单id不能同时存在  
51602 | 200 | 订单状态或订单id必须存在一个  
51603 | 200 | 查询订单不存在  
51604 | 200 | 若想获取文件链接，请先申请下载文件  
51605 | 200 | 只允许下载过去两年内的历史成交明细文件  
51606 | 200 | 无法下载当前季度的历史成交明细  
51607 | 200 | 您已申请下载文件，当前状态为进行中  
51608 | 200 | 当前季度无历史成交明细  
51610 | 200 | 只允许下载 2021 年第一季度以来的历史账单流水  
51611 | 200 | 无法下载当前季度的账单流水  
51620 | 200 | 您不是节点用户，没有相关权限  
51621 | 200 | 该用户不是您的直客  
51625 | 200 | 一键还债失败，请先开启自动借币，或通过闪兑、现货交易进行还债。  
51820 | 200 | 请求失败  
51821 | 200 | 该支付方式不支持  
51822 | 200 | 超过询价有效期  
51823 | 200 | 买卖交易参数 {param} 与报价不一致  
51156 | 200 | 您当前身份为带单交易员。在开平仓模式下，对于带单合约标的不支持使用该接口平仓  
51159 | 200 | 您当前身份为带单交易员，在买卖模式下，如需使用该接口下单，委托的方向必须与现有持仓和挂单保持一致  
51162 | 200 | 您当前有 {instrument} 挂单，请撤单后重试  
51163 | 200 | 您当前有 {instrument} 持仓，请平仓后重试  
51165 | 200 | {instrument}只减仓订单数量已达上限 {upLimit}，请撤销部分订单后重新下单。  
51166 | 200 | 当前产品不支持带单  
51167 | 200 | 下单失败，因为您存在大宗交易的委托订单，请撤销后重新下单  
51168 | 200 | 下单失败，因为您存在只减仓类型的委托订单，请撤销后重新下单  
51320 | 200 | 币种占比范围 {PercentNum1}%-{PercentNum2}%  
51321 | 200 | 您正在带单。暂不支持使用套利、冰山或时间加权 (TWAP) 策略带单  
51322 | 200 | 您当前身份为带单交易员。您的带单合约持仓已经市价全平，系统已撤销止盈止损委托并进行平仓  
51323 | 200 | 您当前身份为带单交易员。您的带单合约仓位已设置止盈止损，请先撤销原有止盈止损订单  
51324 | 200 | 您当前身份为带单交易员，并持有 {instrument} 仓位。平仓委托张数需要与可平张数一致  
51325 | 200 | 您当前身份为带单交易员。下止盈止损单时，请选择市价作为委托价格  
51326 | 200 | 您当前身份为带单交易员，下止盈止损单时，委托价格类型必须为市价  
51326 | 200 | 您当前身份为带单交易员，下止盈止损单时，委托价格类型必须为市价  
54000 | 200 | 暂不支持币币杠杆业务  
54001 | 200 | 只有跨币种全仓账户才能设置自动借币  
54004 | 200 | 下单或改单失败，因为批量订单中的一个订单失败了  
54005 | 200 | 盘前交割合约请使用逐仓进行交易  
54006 | 200 | 盘前交易合约用户持仓上限为{posLimit}张  
54007 | 200 | 不支持该产品 {instId}  
54008 | 200 | 该操作被“撤销 MMP 订单”接口限制。请通过该接口解除限制。  
54009 | 200 | {param0}的范围应为 [{param1}，{param2}]  
54011 | 200 | 盘前交易合约交割前 1 小时内仅允许减少仓位数量，请修改或撤销订单  
54018 | 200 | 超出 {param0} 美元的买入量限额，余下限额为 {param1} 美元。（集合竞价期间）  
54019 | 200 | 超出 {param0} 美元的买入量限额，余下限额为 {param1} 美元。（集合后）  
54024 | 200 | 下单失败，在全仓模式下交易交割、永续合约和期权时需开启 {ccy} 质押  
54025 | 200 | 下单失败，在逐仓模式下交易杠杆、交割、永续合约和期权时需开启 {ccy} 质押  
54026 | 200 | 下单失败，在逐仓模式下交易杠杆币对时需开启 {ccy} 和 {ccy1} 质押  
54027 | 200 | 下单失败，交易期权时需开启 {ccy} 质押  
54028 | 200 | 下单失败，在逐仓模式下交易现货需开启 {ccy} 质押  
54029 | 200 | {param0} 不存在于 {param1}  
54030 | 200 | 下单失败，您的 {param0} 相同交易方向的持仓和挂单总价值不可超过 {param1} 美元，或超过全平台总持仓量的 {param2}  
54031 | 200 | 下单失败，{param0}的平台持仓量已达到平台持仓限额，无法开仓，只能平仓。开仓请稍后再试。  
54035 | 200 | 下单失败，当前已达到该币种的全平台质押上限，仅支持只减仓订单  
54036 | 200 | STP mode 为 cancel both，不支持 FOK 订单  
54039 | 200 | ELP 订单不支持仅减仓设置  
54040 | 200 | ELP 订单无法与止盈止损设置同时使用  
54041 | 200 | {param0} 不支持下 ELP 订单  
54042 | 200 | 您无法为 {param0} 下 ELP 订单  
54043 | 200 | 您最多只能为 {param0} 下 {param1} 个 ELP 订单，请撤销部分订单后再试  
54044 | 200 | {param0} 不支持 ELP，你不能吃单 ELP 挂单  
54045 | 200 | OpenAPI 用户只能下 IOC 订单来吃单 ELP 挂单  
54046 | 200 | 你不能吃单 ELP 挂单  
54047 | 200 | 您无法修改此订单，因为存在订单 ID 或客户订单 ID 相同的订单处于延迟中  
54048 | 200 | 您无法取消此订单，因为存在订单 ID 或客户订单 ID 相同的订单处于延迟中  
54049 | 200 | 由于系统繁忙，API 用户目前无法吃单 ELP 挂单。请将 isElpTakerAccess 设置为 false 以继续操作  
54070 | 200 | 当前功能不可用。使用 App 请更新至最新版本；使用 Open API 请通过 attachAlgoOrds 数组下单。  
54071 | 200 | 由于平台系统已升级，此订单已不支持修改。建议撤销后再重新下单。  
54072 | 200 | 当前仅支持查看该合约，无法进行交易  
54073 | 200 | 下单失败，{param0} 存在脱钩风险，请切换结算币种后重试  
54074 | 200 | 设置失败，请撤销所有以 {param0} 作为结算币种的挂单、平掉相关仓位、停止策略  
54075 | 200 | 当前账户模式暂不支持币币合约交易。  
54078 | 200 | 当主单为买入订单时，止盈涨跌幅应高于 0，止损涨跌幅应处于 -1 ~ 0 之间；当主单为卖出订单时，止盈涨跌幅应处于 -1 ~ 0 之间，止损涨跌幅应高于 0。请注意，涨跌幅应为 0.0001 的整倍数。  
54079 | 200 | 仅支持合约模式和跨币种保证金模式下的合约交易设置动态涨跌幅。请注意，若设置为动态涨跌幅，触发价将以最新价为参考。  
54092 | 200 | 操作要求：请通过网页端或 App 前端尝试下单 TradFi 永续合约（TradFi Perps）交易，并完成免责声明确认。每个主账户及子账户都必须单独接受免责声明后，方可启用 API 交易功能。  
54094 | 200 | 下单失败，当前交易产品处于冷静期内，暂不支持下单。  
  
#### 数据类

错误码 | HTTP 状态码 | 错误提示  
---|---|---  
52000 | 200 | 没有最新行情信息