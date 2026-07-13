---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#error-code-rest-api
anchor_id: error-code-rest-api
api_type: REST
updated_at: 2026-07-13 19:29:46.732416
---

# REST API

REST API Error Code is from 50000 to 59999.

### Public

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
  
### Finance

Error Code from 51700 to 51799

Error Code | HTTP Status Code | Error Message  
---|---|---  
51720 | 200 | Redeem error  
51721 | 200 | Cancel redeem error  
51722 | 200 | Redeem already complete  
51723 | 200 | Early redemption is not supported  
51724 | 200 | Redemption is currently not supported  
51725 | 200 | Cancellation is currently not supported  
51726 | 200 | Cancellation of subscriptions/redemptions is not supported  
51727 | 200 | The minimum subscription amount is {minUnit} {ccy}  
51728 | 200 | The subscription quantity is above the maximum limit  
51729 | 200 | This project has not reached the redemption date  
51730 | 200 | Sold out  
51731 | 200 | Product is currently suspended for purchase  
51732 | 200 | Required user KYC level not met  
51733 | 200 | User is under risk control  
51734 | 200 | User KYC Country is not supported  
51735 | 200 | Sub-account is not supported  
51736 | 200 | Insufficient {ccy} balance  
51737 | 200 | For security and compliance purposes, please complete the identity verification process to continue using our services.  
51738 | 200 | Your funding account is frozen.  
51739 | 200 | This function is unavailable temporarily  
51750 | 200 | The collateral cannot contain assets in the currency of the loan  
51751 | 200 | The currency {ccy} does not support borrowing  
51752 | 200 | The currency {ccy} does not support collateralization  
51753 | 200 | The collateral does not include this asset  
51754 | 200 | There is currently no debt, no need to increase collateral  
51755 | 200 | The currency {ccy} operation is restricted  
51756 | 200 | Exceeding the maximum redeemable quantity  
51757 | 200 | The collateral amount should not be less than {minAmt}  
51758 | 200 | You can redeem at most {maxRedemptionAmount} {crypto}.  
51759 | 200 | You've exceed the temporary limit. Try again later.  
51760 | 200 | Flexible Loan isn’t available to accounts using delta neutral strategy.  
51761 | 200 | Failed to verify sub-account strategy type.  
51762 | 200 | Redemption partially processed and can't be cancelled  
51763 | 200 | Your account does not meet the VIP tier requirement for this product  
51764 | 200 | Insufficient balance  
51765 | 200 | Exceed your remaining daily quota of {x} USDT  
51766 | 200 | Platform daily subscription limit reached  
51767 | 200 | System maintenance, please retry  
51768 | 200 | Exceed your remaining fast redemption quota of {x} OKUSD  
51769 | 200 | Platform fast redemption limit reached  
51770 | 200 | Exceed your remaining standard redemption quota of {x} OKUSD  
51771 | 200 | Platform standard redemption limit reached  
51772 | 200 | Instant redemption pool insufficient  
51773 | 200 | Feature not available in your region  
51774 | 200 | OKUSD API is under maintenance  
  
### Convert

Error Code from 52900 to 52999

Error Code | HTTP Status Code | Error Message  
---|---|---  
52900 | 200 | General invalid request  
52901 | 200 | Invalid base asset  
52902 | 200 | Invalid quote asset  
52903 | 200 | Invalid quote amount  
52904 | 200 | Invalid quote side  
52905 | 200 | Invalid quote price  
52907 | 200 | Order not found  
52908 | 200 | Invalid order ID  
52909 | 200 | Duplicate Client Order Id  
52910 | 500 | Service unavailable, please try again later  
52911 | 500 | RFQ service unavailable, please try again later  
52912 | 500 | Server timeout  
52913 | 200 | Trade rejected  
52914 | 200 | Insufficient available balance in trading account  
52915 | 200 | Cannot quote due to large amounts of RFQ and insufficient liquidity, please try again later  
52916 | 200 | Insufficient balance in funding account  
52917 | 200 | RFQ quantity cannot be less than the lower limit  
52918 | 200 | RFQ quantity cannot be greater than the upper limit  
52919 | 200 | Parameter {param} of convert trading is inconsistent with the quotation  
52920 | 200 | Quantity of convert trading cannot exceed the quotation quantity  
52921 | 200 | Quote traded, please ask for quote again  
52922 | 200 | Quote expired, please ask for quote again  
52923 | 200 | Service unavailable. Try again later.  
52924 | 200 | Too many orders. Try again later.  
52925 | 200 | Duplicate client request ID  
52926 | 200 | {param0} has already expired  
52927 | 200 | No quote  
52928 | 200 | Quantity must be a multiple of the step size  
52929 | 200 | Disable Pay trading fees in quote currency, then try converting again.  
  
### Futures

Error Code from 55000 to 55999

Error Code | HTTP Status Code | Error Message  
---|---|---  
55000 | 200 | Cannot be transferred out within 30 minutes after delivery.  
  
### Swap

No

### Option

No

### Funding

Error Code from 58000 to 58999

Error Code | HTTP Status Code | Error Message  
---|---|---  
58002 | 200 | Please activate Savings Account first.  
58003 | 200 | Savings does not support this currency type  
58004 | 200 | Account blocked.  
58005 | 200 | The {behavior} amount must be equal to or less than {minNum}  
58006 | 200 | Service unavailable for token {0}.  
58007 | 200 | Assets interface is currently unavailable. Try again later  
58008 | 200 | You do not have assets in this currency.  
58009 | 200 | Crypto pair doesn't exist  
58010 | 200 | Chain {chain} isn't supported  
58011 | 200 | Due to local laws and regulations, our services are unavailable to unverified users in {region}. Please verify your account.  
58012 | 200 | Due to local laws and regulations, OKX does not support asset transfers to unverified users in {region}. Please make sure your recipient has a verified account.  
58013 | 200 | Withdrawals not supported yet, contact customer support for details  
58014 | 200 | Deposits not supported yet, contact customer support for details  
58015 | 200 | Transfers not supported yet, contact customer support for details  
58016 | 200 | The API can only be accessed and used by the trading team's main account  
58100 | 200 | The trading product triggers risk control, and the platform has suspended   
the fund transfer-out function with related users. Please wait patiently.  
58101 | 200 | Transfer suspended  
58102 | 429 | Rate limit reached. Please refer to API docs and throttle requests accordingly.  
58103 | 200 | This account transfer function is temporarily unavailable. Please contact customer service for details.  
58104 | 200 | Since your P2P transaction is abnormal, you are restricted from making  
fund transfers. Please contact customer support to remove the restriction.  
58105 | 200 | Since your P2P transaction is abnormal, you are restricted from making  
fund transfers. Please transfer funds on our website or app to complete  
identity verification.  
58106 | 200 | USD verification failed.  
58107 | 200 | Crypto verification failed.  
58110 | 200 | Transfers are suspended due to market risk control triggered by your {businessType} {instFamily} trades or positions. Please try again in a few minutes. Contact customer support if further assistance is needed.  
58111 | 200 | Fund transfers are unavailable while perpetual contracts are charging funding fees. Try again later.  
58112 | 200 | Transfer failed. Contact customer support for assistance  
58113 | 200 | Unable to transfer this crypto  
58114 | 400 | Transfer amount must be greater than 0  
58115 | 200 | Sub-account does not exist.  
58116 | 200 | Transfer exceeds the available amount.  
58117 | 200 | Transfer failed. Resolve any negative assets before transferring again  
58119 | 200 | {0} Sub-account has no permission to transfer out, please set first.  
58120 | 200 | Transfers are currently unavailable. Try again later  
58121 | 200 | This transfer will result in a high-risk level of your position, which may lead to forced liquidation. You need to re-adjust the transfer amount to make sure the position is at a safe level before proceeding with the transfer.  
58122 | 200 | A portion of your spot is being used for Delta offset between positions. If the transfer amount exceeds the available amount, it may affect current spot-derivatives risk offset structure, which will result in an increased Maintenance Margin Requirement (MMR) rate. Please be aware of your risk level.  
58123 | 200 | The From parameter cannot be the same as the To parameter.  
58124 | 200 | Your transfer is being processed, transfer id:{trId}. Please check the latest state of your transfer from the endpoint (GET /api/v5/asset/transfer-state)  
58125 | 200 | Non-tradable assets can only be transferred from sub-accounts to main accounts  
58126 | 200 | Non-tradable assets can only be transferred between funding accounts  
58127 | 200 | Main account API key does not support current transfer 'type' parameter. Please refer to the API documentation.  
58128 | 200 | Sub-account API key does not support current transfer 'type' parameter. Please refer to the API documentation.  
58129 | 200 | {param} is incorrect or {param} does not match with 'type'  
58131 | 200 | For compliance, we're unable to provide services to unverified users. Verify your identity to make a transfer.  
58132 | 200 | For compliance, we're unable to provide services to users with Basic verification (Level 1). Complete Advanced verification (Level 2) to make a transfer.  
58200 | 200 | Withdrawal from {0} to {1} is currently not supported for this currency.  
58201 | 200 | Withdrawal amount exceeds daily withdrawal limit.  
58202 | 200 | The minimum withdrawal amount for NEO is 1, and the amount must be an integer.  
58203 | 200 | Please add a withdrawal address.  
58204 | 200 | Withdrawal suspended due to your account activity triggering risk control. Please contact customer support for assistance.  
58205 | 200 | Withdrawal amount exceeds the upper limit.  
58206 | 200 | Withdrawal amount is less than the lower limit.  
58207 | 200 | Withdrawal address isn't on the verified address list. (The format for withdrawal addresses with a label is “address:label”.)  
58208 | 200 | Withdrawal failed. Please link your email.  
58209 | 200 | Sub-accounts don't support withdrawals or deposits. Please use your main account instead  
58210 | 200 | You can't proceed with withdrawal as we're unable to verify your identity. Please withdraw via our app or website instead.  
58212 | 200 | Withdrawal fee must be {0}% of the withdrawal amount  
58213 | 200 | The internal transfer address is illegal. It must be an email, phone number, or account name  
58214 | 200 | Withdrawals suspended due to {chainName} maintenance  
58215 | 200 | Withdrawal ID does not exist.  
58216 | 200 | Operation not allowed.  
58217 | 200 | Withdrawals are temporarily suspended for your account due to a risk detected in your withdrawal address. Contact customer support for assistance  
58218 | 200 | The internal withdrawal failed. Please check the parameters toAddr and areaCode.  
58219 | 200 | You cannot withdraw crypto within 24 hours after changing your mobile number, email address, or Google Authenticator.  
58220 | 200 | Withdrawal request already canceled.  
58221 | 200 | The toAddr parameter format is incorrect, withdrawal address needs labels. The format should be "address:label".  
58222 | 200 | Invalid withdrawal address  
58223 | 200 | This is a contract address with higher withdrawal fees  
58224 | 200 | This crypto currently doesn't support on-chain withdrawals to OKX addresses. Withdraw through internal transfers instead  
58225 | 200 | Asset transfers to unverified users in {region} are not supported due to local laws and regulations.  
58226 | 200 | {chainName} is delisted and not available for crypto withdrawal.  
58227 | 200 | Withdrawal of non-tradable assets can be withdrawn all at once only  
58228 | 200 | Withdrawal of non-tradable assets requires that the API key must be bound to an IP  
58229 | 200 | Insufficient funding account balance to pay fees {fee} USDT  
58230 | 200 | According to the OKX compliance policy, you will need to complete your identity verification (Level 1) in order to withdraw  
58231 | 200 | The recipient has not completed personal info verification (Level 1) and cannot receive your transfer  
58232 | 200 | You’ve reached the personal information verification (L1) withdrawal limit, complete photo verification (L2) to increase the withdrawal limit  
58233 | 200 | For compliance, we're unable to provide services to unverified users. Verify your identity to withdraw.  
58234 | 200 | For compliance, the recipient can't receive your transfer yet. They'll need to verify their identity to receive your transfer.  
58235 | 200 | For compliance, we're unable to provide services to users with Basic verification (Level 1). Complete Advanced verification (Level 2) to withdraw.  
58236 | 200 | For compliance, a recipient with Basic verification (Level 1) is unable to receive your transfer. They'll need to complete Advanced verification (Level 2) to receive it.  
58237 | 200 | According to local laws and regulations, please provide accurate recipient information (rcvrInfo). For the exchange address, please also provide exchange information and recipient identity information ({consientParameters}).  
58238 | 200 | Incomplete info. The info of the exchange and the recipient are required if you're withdrawing to an exchange platform.  
58239 | 200 | You can't withdraw to a private wallet via API. Please withdraw via our app or website instead.  
58240 | 200 | For security and compliance purposes, please complete the identity verification process to use our services. If you prefer not to verify, contact customer support for next steps. We're committed to ensuring a safe platform for users and appreciate your understanding.  
58241 | 200 | Due to local compliance requirements, internal withdrawal is unavailable  
58242 | 200 | The recipient can't receive your transfer due to their local compliance requirements  
58243 | 200 | Your recipient can't receive your transfer as they haven't made a cash deposit yet  
58244 | 200 | Make a cash deposit to proceed  
58248 | 200 | Due to local regulations, API withdrawal isn't allowed. Withdraw using OKX app or web.  
58249 | 200 | API withdrawal for this currency is currently unavailable. Try withdrawing via our app or website.  
58252 | 200 | Withdrawal is restricted for 48h after your first TRY transaction for asset security.  
58254 | 200 | Due to local compliance requirements, please complete the digital signature or satoshi test via our app or website first before withdrawing to a private wallet via API.  
58256 | 200 | You can withdraw stablecoins valued at up to {dailyLimit} {symbol} every 24 hours. You can still withdraw {quotaRemaining} {symbol}.  
58257 | 200 | You can withdraw stablecoins valued at up to {monthlyLimit} {symbol} every month. You can still withdraw {quotaRemaining} {symbol}.  
58258 | 200 | You can withdraw crypto valued at up to {dailyLimit} {symbol} every 24 hours. You can still withdraw {quotaRemaining} {symbol}.  
58300 | 200 | Deposit-address count exceeds the limit.  
58301 | 200 | Deposit-address not exist.  
58302 | 200 | Deposit-address needs tag.  
58303 | 200 | Deposit for chain {chain} is currently unavailable  
58304 | 200 | Failed to create invoice.  
58305 | 200 | Unable to retrieve deposit address, please complete identity verification and generate deposit address first.  
58306 | 200 | According to the OKX compliance policy, you will need to complete your identity verification (Level 1) in order to deposit  
58307 | 200 | You've reached the personal information verification (L1) deposit limit, the excess amount has been frozen, complete photo verification (L2) to increase the deposit limit  
58308 | 200 | For compliance, we're unable to provide services to unverified users. Verify your identity to deposit.  
58309 | 200 | For compliance, we're unable to provide services to users with Basic verification (Level 1). Complete Advanced verification (Level 2) to deposit.  
58310 | 200 | Unable to create new deposit address, try again later  
58350 | 200 | Insufficient balance.  
58351 | 200 | Invoice expired.  
58352 | 200 | Invalid invoice.  
58353 | 200 | Deposit amount must be within limits.  
58354 | 200 | You have reached the daily limit of 10,000 invoices.  
58355 | 200 | Permission denied. Please contact your account manager.  
58356 | 200 | The accounts of the same node do not support the Lightning network deposit or withdrawal.  
58358 | 200 | The fromCcy parameter cannot be the same as the toCcy parameter.  
58373 | 200 | The minimum {ccy} conversion amount is {amount}  
58381 | 200 | This feature is not currently supported.  
58382 | 200 | Unable to process unlock request. Please retry via the user interface.  
58383 | 200 | Deposit record not found. Unable to process unlock request.  
58384 | 200 | Per local regulations, please provide accurate sender information. For exchange addresses, please also provide the exchange information and sender identity details.  
58400 | 200 | Request Failed  
58401 | 200 | Payment method is not supported  
58402 | 200 | Invalid payment account  
58403 | 200 | Transaction cannot be canceled  
58404 | 200 | ClientId already exists  
58405 | 200 | Withdrawal suspended  
58406 | 200 | Channel is not supported  
58407 | 200 | API withdrawal isn't allowed for this payment method. Withdraw using OKX app or web  
  
### Account

Error Code from 59000 to 59999

Error Code | HTTP Status Code | Error Message  
---|---|---  
59000 | 200 | Settings failed. Close any open positions or orders before modifying settings.  
59001 | 200 | Switching unavailable as you have borrowings.  
59002 | 200 | Sub-account settings failed. Close any open positions, orders, or trading bots before modifying settings.  
59004 | 200 | Only IDs with the same instrument type are supported  
59005 | 200 | When margin is manually transferred in isolated mode, the value of the asset intially allocated to the position must be greater than 10,000 USDT.  
59006 | 200 | This feature is unavailable and will go offline soon.  
59101 | 200 | Leverage can't be modified. Please cancel all pending isolated margin orders before adjusting the leverage.  
59102 | 200 | Leverage exceeds the maximum limit. Please lower the leverage.  
59103 | 200 | Account margin is insufficient and leverage is too low. Please increase the leverage.  
59104 | 200 | The borrowed position has exceeded the maximum position of this leverage. Please lower the leverage.  
59105 | 400 | Leverage can't be less than {0}. Please increase the leverage.  
59106 | 200 | The max available margin corresponding to your order tier is {param0}. Please adjust your margin and place a new order.  
59107 | 200 | Leverage can't be modified. Please cancel all pending cross-margin orders before adjusting the leverage.  
59108 | 200 | Your account leverage is too low and has insufficient margins. Please increase the leverage.  
59109 | 200 | Account equity less than the required margin amount after adjustment. Please adjust the leverage.  
59110 | 200 | The instrument corresponding to this {param0} does not support the tgtCcy parameter.  
59111 | 200 | Leverage query isn't supported in portfolio margin account mode  
59112 | 200 | You have isolated/cross pending orders. Please cancel them before adjusting your leverage  
59113 | 200 | According to local laws and regulations, margin trading service is not available in your region. If your citizenship is at a different region, please complete KYC2 verification.  
59114 | 200 | According to local laws and regulations, margin trading services are not available in your region.  
59117 | 200 | Cannot select more than {param0} crypto types  
59118 | 200 | Amount placed should greater than {param0}  
59119 | 200 | One-click repay is temporarily unavailable. Try again later.  
59120 | 200 | One-click convert is temporarily unavailable. Try again later.  
59121 | 200 | This batch is still under processing, please wait patiently.  
59122 | 200 | This batch has been processed  
59123 | 200 | {param0} order amount must be greater than {param1}  
59124 | 200 | The order amount of {param0} must be less than {param1}.  
59125 | 200 | {param0} doesn't support the current operation.  
59132 | 200 | Unable to switch. Please close or cancel all open orders and refer to the pre-check endpoint to stop any incompatible bots.  
59133 | 200 | Unable to switch due to insufficient assets for the chosen account mode.  
59134 | 200 | Unable to switch. Refer to the pre-check endpoint and close any incompatible positions.  
59135 | 200 | Unable to switch. Refer to the pre-check endpoint and adjust your trades from copy trading.  
59136 | 200 | Unable to switch. Pre-set leverage for all cross margin contract positions then try again.  
59137 | 200 | Lower leverage to {param0} or below for all cross margin contract positions and try again.  
59138 | 200 | Unable to switch due to a position tier check failure.  
59139 | 200 | Unable to switch due to a margin check failure.  
59140 | 200 | You can only repay with your collateral crypto.  
59141 | 200 | The minimum repayment amount is {param0}. Select more available crypto or increase your trading account balance.  
59142 | 200 | Instant repay failed. You can only repay borrowable crypto.  
59200 | 200 | Insufficient account balance.  
59201 | 200 | Negative account balance.  
59202 | 200 | No access to max opening amount in cross positions for PM accounts.  
59300 | 200 | Margin call failed. Position does not exist.  
59301 | 200 | Margin adjustment failed for exceeding the max limit.  
59302 | 200 | Margin adjustment failed due to pending close order. Please cancel any pending close orders.  
59303 | 200 | Insufficient available margin, add margin or reduce the borrowing amount  
59304 | 200 | Insufficient equity for borrowing. Keep enough funds to pay interest for at least one day.  
59305 | 200 | Use VIP loan first to set the VIP loan priority  
59306 | 200 | Your borrowing amount exceeds the max limit  
59307 | 200 | You are not eligible for VIP loans  
59308 | 200 | Unable to repay VIP loan due to insufficient borrow limit  
59309 | 200 | Unable to repay an amount that exceeds the borrowed amount  
59310 | 200 | Your account does not support VIP loan  
59311 | 200 | Setup cannot continue. An outstanding VIP loan exists.  
59312 | 200 | {currency} does not support VIP loans  
59313 | 200 | Unable to repay. You haven't borrowed any ${ccy} (${ccyPair}) in Quick margin mode.  
59314 | 200 | The current user is not allowed to return the money because the order is not borrowed  
59315 | 200 | viploan is upgrade now. Wait for 10 minutes and try again  
59316 | 200 | The current user is not allowed to borrow coins because the currency is in the order in the currency borrowing application.  
59317 | 200 | The number of pending orders that are using VIP loan for a single currency cannot be more than {maxNumber} (orders)  
59319 | 200 | You can’t repay your loan order because your funds are in use. Make them available for full repayment.  
59401 | 200 | Holdings limit reached.  
59402 | 200 | No passed instIDs are in a live state. Please verify instIDs separately.  
59410 | 200 | You can only borrow this crypto if it supports borrowing and borrowing is enabled.  
59411 | 200 | Manual borrowing failed. Your account's free margin is insufficient.  
59412 | 200 | Manual borrowing failed. The amount exceeds your borrowing limit.  
59413 | 200 | You didn't borrow this crypto. No repayment needed.  
59414 | 200 | Manual borrowing failed. The minimum borrowing limit is {param0}.  
59417 | 200 | Manual Simple Borrow for {TOKEN} is temporarily disabled due to high utilization. Please retry later.  
59500 | 200 | Only the API key of the main account has permission.  
59501 | 200 | Each account can create up to 50 API keys  
59502 | 200 | This note name already exists. Enter a unique API key note name  
59503 | 200 | Each API key can bind up to 20 IP addresses  
59504 | 200 | Sub-accounts don't support withdrawals. Please use your main account for withdrawals.  
59505 | 200 | The passphrase format is incorrect.  
59506 | 200 | API key doesn't exist.  
59507 | 200 | The two accounts involved in a transfer must be 2 different sub-accounts under the same main account.  
59508 | 200 | The sub account of {param0} is suspended.  
59509 | 200 | Account doesn't have permission to reset market maker protection (MMP) status.  
59510 | 200 | Sub-account does not exist  
59512 | 200 | Unable to set up permissions for ND broker subaccounts. By default, all ND subaccounts can transfer funds out.  
59515 | 200 | You are currently not on the custody whitelist. Please contact customer service for assistance.  
59516 | 200 | Please create the Copper custody funding account first.  
59517 | 200 | Please create the Komainu custody funding account first.  
59518 | 200 | You can’t create a sub-account using the API; please use the app or web.  
59519 | 200 | You can’t use this function/feature while it's frozen, due to: {freezereason}  
59518 | 200 | This account isn’t eligible for delta neutral strategy.  
59519 | 200 | You must be VIP 1 or above to use delta netural strategy.  
59520 | 200 | You can’t use delta neutral strategy in spot or futures mode.  
59521 | 200 | Flexible Loan and delta neutral strategy can't be in use at the same time.  
59522 | 200 | You can’t borrow and transfer or withdraw when using delta neutral strategy.  
59523 | 200 | You can’t place orders or open positions in isolated mode and use delta neutral strategy at the same time.  
59524 | 200 | You can’t trade options or open option positions and use delta neutral strategy at the same time.  
59525 | 200 | Some bots and copy trades can’t be used at the same time as delta neutral strategy.  
59526 | 200 | Failed to switch strategy because your delta-to-equity ratio will exceed the threshold and trigger the transfer-out restriction after the switch. Lower your delta and try again.  
59527 | 200 | You must set all currencies as collateral when using delta neutral strategy.  
59528 | 200 | Failed to switch strategy because your account’s {param0} borrowing in the targeted strategy will exceed the main account borrowing limit after the switch. Repay your liabilities and try again.  
59529 | 200 | Failed to switch strategy. This account is part of a delta neutral risk unit. Remove it from the risk unit before switching strategies.  
59550 | 200 | Complete identity verification (Lv2) to access this feature.  
59601 | 200 | Subaccount name already exists.  
59603 | 200 | Maximum number of subaccounts reached.  
59604 | 200 | Only the API key of the main account can access this API.  
59606 | 200 | Failed to delete sub-account. Transfer all sub-account funds to your main account before deleting your sub-account.  
59608 | 200 | Only Broker accounts have permission to access this API.  
59609 | 200 | Broker already exists  
59610 | 200 | Broker does not exist  
59611 | 200 | Broker unverified  
59612 | 200 | Cannot convert time format  
59613 | 200 | No escrow relationship established with the subaccount.  
59614 | 200 | Managed subaccount does not support this operation.  
59615 | 200 | The time interval between the Begin Date and End Date cannot be greater than 180 days.  
59616 | 200 | The Begin Date cannot be later than the End Date.  
59617 | 200 | Sub-account created. Account level setup failed.  
59618 | 200 | Failed to create sub-account.  
59619 | 200 | This endpoint does not support ND sub accounts. Please use the dedicated endpoint supported for ND brokers.  
59622 | 200 | You're creating a sub-account for a non-existing or incorrect sub-account. Create a sub-account under the ND broker first or use the correct sub-account code.  
59623 | 200 | Couldn't delete the sub-account under the ND broker as the sub-account has one or more sub-accounts, which must be deleted first.  
59648 | 200 | Your modified spot-in-use amount is insufficient, which may lead to liquidation. Adjust the amount.  
59649 | 200 | Disabling spot-derivatives risk offset mode may increase the risk of liquidation. Adjust the size of your positions and ensure your maintenance maintenance margin ratio is safe.  
59650 | 200 | Switching your offset unit may increase the risk of liquidation. Adjust the size of your positions and ensure your maintenance maintenance margin ratio is safe.  
59651 | 200 | Enable spot-derivatives risk offset mode to set your spot-in-use amount.  
59652 | 200 | You can only set a spot-in-use amount for crypto that can be used as margin.  
59658 | 200 | {ccy} isn’t supported as collateral.  
59658 | 200 | {ccy} and {ccy1} aren’t supported as collateral.  
59658 | 200 | {ccy}, {ccy1}, and {ccy2} aren’t supported as collateral.  
59658 | 200 | {ccy}, {ccy1}, {ccy2}, and {number} other crypto aren’t supported as collateral.  
59659 | 200 | Failed to apply settings because you must also enable {ccy} to enable {ccy1} as collateral.  
59660 | 200 | Failed to apply settings because you must also disable {ccy} to disable {ccy1} as collateral.  
59661 | 200 | Failed to apply settings because you can’t disable {ccy} as collateral.  
59662 | 200 | Failed to apply settings because of open orders or positions requiring {ccy} as collateral.  
59662 | 200 | Failed to apply settings because of open orders or positions requiring {ccy} and {ccy1} as collateral.  
59662 | 200 | Failed to apply settings because of open orders or positions requiring {ccy}, {ccy1}, and {ccy2} as collateral.  
59662 | 200 | Failed to apply settings because of open orders or positions requiring {ccy}, {ccy1}, {ccy2}, and {number} other crypto as collateral.  
59664 | 200 | Failed to apply settings because you have borrowings in {ccy}.  
59664 | 200 | Failed to apply settings because you have borrowings in {ccy} and {ccy1}.  
59664 | 200 | Failed to apply settings because you have borrowings in {ccy}, {ccy1}, and {ccy2}.  
59664 | 200 | Failed to apply settings because you have borrowings in {ccy}, {ccy1}, {ccy2}, and {number} other crypto.  
59665 | 200 | Failed to apply settings. Enable other cryptocurrencies as collateral to meet the position’s margin requirements.  
59666 | 200 | Failed to apply settings because you can’t enable and disable a crypto as collateral at the same time.  
59668 | 200 | Cancel isolated margin TP/SL, trailing, trigger, and chase orders or stop bots before adjusting your leverage.  
59669 | 200 | Cancel cross-margin TP/SL, trailing, trigger, and chase orders or stop bots before adjusting your leverage.  
59670 | 200 | You have more than {param0} open orders for this trading pair. Cancel to reduce your orders to {param1} or fewer before adjusting your leverage.  
59671 | 200 | Auto-earn currently doesn’t support {param0}.  
59672 | 200 | You can’t modify your minimmum lending APR when Auto-earn is off.  
59673 | 200 | You can’t turn off Auto-earn within 24 hours of turning it on. Try again at {param0}.  
59674 | 200 | You can’t borrow to transfer or withdraw when Auto-earn is on for this cryptocurrency.  
59675 | 200 | You’ve already turned on Auto-earn for {param0}.  
59676 | 200 | You can only use Auto-earn if your trading fee tier is {param0} or higher.  
59678 | 200 | Switch failed. Please cancel all existing spot orders and try again.  
59679 | 200 | Switch failed. Your account does not currently support this fee currency.  
59683 | 200 | Set this crypto as your collateral crypto before selecting it as your settlement currency.  
59684 | 200 | Borrowing isn’t supported for this currency.  
59686 | 200 | This crypto can’t be set as a settlement currency.  
59689 | 200 | Convert failed. The {param0} converted to {param1} is too small to process.  
59691 | 200 | Daily increase limit reached {param0}. Please retry after UTC 0:00 or reset your demo account.  
59692 | 200 | Insufficient {param0} balance. Balance cannot go below zero after operation.  
59693 | 200 | {param0} transferable balance insufficient. Some funds are occupied by open orders or positions. Please cancel orders or close positions and try again.  
  
### Block Trading and Spread Orderbook

Error Code from 70000

Error Code | HTTP Status Code | Error Message  
---|---|---  
70000 | 200 | RFQ does not exist.  
70001 | 200 | Quote does not exist.  
70002 | 200 | Block trade does not exist.  
70003 | 200 | Public block trade does not exist.  
70004 | 200 | Invalid instrument {instId}  
70005 | 200 | The number of legs in RFQ cannot exceed maximum value.  
70006 | 200 | Does not meet the minimum asset requirement.  
70007 | 200 | Underlying index {instFamily} does not exist under instType {instType}.  
70008 | 200 | Operation failed under MMP status.  
70009 | 200 | Data must have at least 1 valid element.  
70010 | 200 | Timestamp parameters need to be in Unix timestamp format in milliseconds.  
70011 | 200 | Duplicate setting for instType {instType}.  
70012 | 200 | Duplicate setting for underlying/instId {instId} under the same instType {instType}.  
70013 | 200 | endTs needs to be bigger than or equal to beginTs.  
70014 | 200 | It's not allowed to have includeAll=True for all the instType.  
70015 | 200 | In order to trade this product, you need to complete advanced verification  
70016 | 200 | Please specify your instrument settings for at least one instType.  
70060 | 200 | The {account} doesn’t exist or the position side is incorrect. “To” and “from” accounts must be under the same main account.  
70061 | 200 | To move position, please enter a position that’s opposite to your current side and is smaller than or equal to your current size.  
70062 | 200 | {account} has reached the maximum number of position transfers allowed per day.  
70064 | 200 | Position does not exist.  
70065 | 200 | Couldn’t move position. Execution price cannot be determined.  
70066 | 200 | Moving positions isn't supported in spot mode. Switch to any other account mode and try again.  
70067 | 200 | Moving positions isn't supported in margin trading.  
70100 | 200 | Duplicate instruments in legs array.  
70101 | 200 | Duplicate clRfqId  
70102 | 200 | No counterparties specified  
70103 | 200 | Invalid counterparty  
70105 | 200 | The total value of non all-SPOT RFQs should be greater than the min notional value {nonSpotMinNotional}  
70106 | 200 | The trading amount does not meet the min tradable amount requirement  
70107 | 200 | The number of counterparties cannot exceed maximum value.  
70108 | 200 | The total value of all-spot RFQs should be greater than the min notional value {spotMinNotional}  
70109 | 200 | Counterparties for selected instruments are currently unavailable.  
70200 | 200 | The RFQ with {rfqState} status cannot be canceled  
70203 | 200 | Cancellation failed as rfq count exceeds the limit {rfqLimit}.  
70207 | 200 | Cancellation failed as you do not have any active RFQs.  
70208 | 200 | Cancellation failed as service is unavailable now, please try again later.  
70301 | 200 | Duplicate clQuoteId.  
70303 | 200 | The RFQ with {rfqState} status cannot be quoted.  
70304 | 200 | Price should be an integer multiple of the tick size.  
70305 | 200 | Bid price cannot be higher than offer price  
70306 | 200 | The legs of quote do not match the legs of {rfqId}  
70307 | 200 | Size should be in integral multiples of the lot size.  
70308 | 200 | Quote to your own RFQ is not allowed.  
70309 | 200 | Quote to the same RFQ with the same side is not allowed.  
70310 | 200 | Quoted price of instId {instId} cannot exceed your preset price limit.  
70400 | 200 | The Quote with {quoteState} status cannot be canceled  
70408 | 200 | Cancellation failed as quote count exceeds the limit {quoteLimit}.  
70409 | 200 | Cancellation failed as you do not have any active Quotes.  
70501 | 200 | RFQ {rfqId} is not quoted by {quoteId}  
70502 | 200 | The legs do not match the legs of {rfqId}  
70503 | 200 | Leg sizes specified are under the minimum block size required by Jupiter.  
70504 | 200 | Execution failed as the RFQ status is {rfqState}.  
70505 | 200 | Execution failed as the Quote status is {quoteState}.  
70506 | 200 | Leg sizes specified do not have the same ratios as the whole RFQ.  
70507 | 200 | Partial execution was attempted but allowPartialExecution of the RFQ is not enabled.  
70508 | 200 | No instrument settings available.  
70509 | 200 | Execution failed: counterparty error  
70510 | 200 | For error details, refer to the acctAlloc field.  
70511 | 200 | Execution is being processed  
70514 | 200 | For each symbol, the total size of RFQ legs in all accounts should be equal to its combined amount in the group RFQ.  
70515 | 200 | For each sub-account, the ratio of a leg’s size to the main account RFQ must be the same across all symbols.  
70516 | 200 | You can only select up to {param0} sub-accounts for group RFQ.  
70517 | 200 | {param0} doesn't exist or you don’t have permission to create group RFQ for it.  
70518 | 200 | Make sure you didn’t select the same account more than once for group RFQ.  
75001 | 200 | Trade ID does not exist  
75002 | 200 | {sprdId} : unable to place new orders or modify existing orders at the moment  
75003 | 200 | Invalid price  
56000 | 200 | Block trade does not exist.  
56001 | 200 | The number of multi-legs cannot exceed {legLimit}.  
56002 | 200 | The number of multi-legs does not match with the verified one.  
56003 | 200 | Duplicate clBlockTdId.  
56004 | 200 | Trade with yourself is not allowed.  
56005 | 200 | clBlockTdId should be the same as the verified one.  
56006 | 200 | The role should be different from the verified one.  
56007 | 200 | Leg no.{legNo} does not match with the verified one.  
56008 | 200 | Duplicate instruments in legs array.  
  
### Copy trading

Error Code from 59200 to 59300

Error Code | HTTP Status Code | Error Message  
---|---|---  
59128 | 200 | As a lead trader, you can't lead trades in {instrument} with leverage higher than {num}×  
59129 | 200 | The first crypto you use to repay must be {param0}.  
59130 | 200 | If an asset’s balance is < 1 USD, it can only repay borrowings of the same crypto.  
59206 | 200 | The lead trader doesn't have any more vacancies for copy traders  
59216 | 200 | The position doesn't exist. Please try again  
59218 | 200 | Closing all positions at market price...  
59256 | 200 | To switch to One-way mode, lower the number of traders you copy to 1  
59247 | 200 | High leverage causes current position to exceed the maximum position size limit under this leverage. Adjust the leverage.  
59260 | 200 | You are not a spot lead trader yet. Complete the application on our website or app first.  
59262 | 200 | You aren't a contract lead trader yet. Complete the application first.  
59641 | 200 | Can't switch account mode as you have fixed loan borrowings.  
59642 | 200 | Lead and copy traders can only use spot or futures modes  
59643 | 200 | Couldn’t switch account modes as you’re currently copying spot trades  
59245 | 200 | As a lead trader, number of {param0} contract per order must be no greater than {param1}  
59263 | 200 | Only traders on the allowlist can use copy trading. ND brokers can reach out to BD for help.  
59264 | 200 | Spot copy trading isn't supported  
59267 | 200 | Cancellation failed as you aren't copying this trader  
59268 | 200 | You can't copy trades with instId that hasn't been selected by the lead trader  
59269 | 200 | This contract lead trader doesn't exist  
59270 | 200 | Maximum total amount (copyTotalAmt) can't be lower than amount per order (copyAmt) when using fixed amount  
59273 | 200 | You aren't a contract copy trader yet. Start by coping a contract trader.  
59274 | 200 | Copying your own trade isn't allowed  
59275 | 200 | You can't copy trade as you're applying to become a lead trader  
59276 | 200 | You can't copy this lead trader as they've applied to stop leading trades  
59277 | 200 | You can't copy this lead trader as they don't have any copy trader vacancies  
59278 | 200 | Your request to stop copy trading is being processed. Try again later.  
59279 | 200 | You've already copied this trader  
59280 | 200 | You can't modify copy trade settings as you aren't copying this trader  
59282 | 200 | Only ND sub-accounts under ND brokers whose main accounts are on the allowlist support this endpoint. Reach out to BD for help.  
59283 | 200 | Your account isn't currently using futures mode  
59284 | 200 | You've reached the monthly limit of {param0} ratio edits  
59286 | 200 | You can't become a futures lead trader when using spot mode  
59287 | 200 | Profit sharing ratio should be between {param0} and {param1}  
59288 | 200 | You're leading trades but your account is in portfolio margin mode. Switch to futures mode or multiple-currency margin mode and try again.  
59130 | 200 | The highest take profit level is {num}%. Enter a smaller number and try again.  
59258 | 200 | Action not supported for lead traders  
59259 | 200 | Enter a multiplier value that's within the valid range  
59285 | 200 | You haven't led or copied any trades yet  
59292 | 200 | This lead trader only supports smart sync mode.  
  
### Trading bot

Error Code from 55100 to 55999

Error Code | HTTP Status Code | Error Message  
---|---|---  
55100 | 200 | Take profit % should be within the range of {parameter1}-{parameter2}  
55101 | 200 | Stop loss % should be within the range of {parameter1}-{parameter2}  
55102 | 200 | Take profit % should be greater than the current bot’s PnL%  
55103 | 200 | Stop loss % should be less than the current bot’s PnL%  
55104 | 200 | Only futures grid supports take profit or stop loss based on profit percentage  
55105 | 200 | Increasing positions is not allowed under current status  
55106 | 200 | Increased amount should be within the range of {parameter1} - {parameter2}  
55111 | 200 | This signal name is in use, please try a new name  
55112 | 200 | This signal does not exist  
55113 | 200 | Create signal strategies with leverage greater than the maximum leverage of the instruments  
55116 | 200 | You can only place one chase order for each trading pair.

---

# REST API

REST API 错误码从 50000 到 59999

### 公共 

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
  
### 金融 

错误码从 51700 到 51799

错误码 | HTTP 状态码 | 错误提示  
---|---|---  
51720 | 200 | 赎回失败  
51721 | 200 | 取消赎回失败  
51722 | 200 | 赎回已到账  
51723 | 200 | 不支持提前赎回  
51724 | 200 | 当前状态不支持赎回  
51725 | 200 | 当前状态不支持取消  
51726 | 200 | 该项目不支持撤销申购/赎回  
51727 | 200 | 最小申购数量为 {minUnit} {ccy}  
51728 | 200 | 申购数量超过最大值  
51729 | 200 | 该项目尚未到期  
51730 | 200 | 该项目已售罄  
51731 | 200 | 产品现在暂停申购  
51732 | 200 | 用户KYC等级不符合要求  
51733 | 200 | 用户被风险管理中  
51734 | 200 | 不支持用户所属KYC国家  
51735 | 200 | 不支持子帐户  
51736 | 200 | {ccy} 余额不足  
51737 | 200 | 根据当地法律法规，您需要完成身份认证方可继续使用我们的服务。  
51738 | 200 | 您的资金账户被冻结  
51739 | 200 | 该功能暂不可用  
51750 | 200 | 抵押物不能包含借贷币种资产  
51751 | 200 | 币种 {ccy} 不支持借币  
51752 | 200 | 币种 {ccy} 不支持抵押  
51753 | 200 | 抵押物中不包含此资产  
51754 | 200 | 当前没有负债，无需增加抵押物  
51755 | 200 | 币种 {ccy} 被限制操作  
51756 | 200 | 超过最大可赎回数量  
51757 | 200 | 质押物数量不应低于 {minAmt}  
51758 | 200 | 您最多可赎回 {maxRedemptionAmount} {crypto}。  
51759 | 200 | 已超出临时限额，请稍后再试。  
51760 | 200 | 使用中性套利策略的账户无法开通活期借币  
51761 | 200 | 无法验证子账户的策略类型  
51762 | 200 | 已部分赎回的订单无法取消  
51763 | 200 | 您的账户不满足该产品的 VIP 等级准入要求  
51764 | 200 | 余额不足  
51765 | 200 | 超出您当日剩余配额 {x} USDT  
51766 | 200 | 平台当日申购限额已达上限  
51767 | 200 | 系统维护中，请稍后重试  
51768 | 200 | 超出您当日剩余即时赎回配额 {x} OKUSD  
51769 | 200 | 平台即时赎回限额已达上限  
51770 | 200 | 超出您当日剩余标准赎回配额 {x} OKUSD  
51771 | 200 | 平台标准赎回限额已达上限  
51772 | 200 | 即时赎回池余额不足  
51773 | 200 | 该功能在您所在地区暂不可用  
51774 | 200 | OKUSD API 正在维护中  
  
### 闪兑 

错误码从 52900 到 52999

错误码 | HTTP 状态码 | 错误提示  
---|---|---  
52900 | 200 | 无效请求  
52901 | 200 | 无效基准货币  
52902 | 200 | 无效标价货币  
52903 | 200 | 无效的报价数量  
52904 | 200 | 无效的报价方向  
52905 | 200 | 无效的报价  
52907 | 200 | 订单找不到  
52908 | 200 | 无效的订单ID  
52909 | 200 | 客户自定义ID重复使用  
52910 | 500 | 服务端暂时不可用，请稍后重试  
52911 | 500 | 询价服务不可用，请稍后重试  
52912 | 500 | 服务端超时  
52913 | 200 | 拒绝交易  
52914 | 200 | 交易账户可用资产不足  
52915 | 200 | 询价量太大，流动性不足导致无法报价，请稍后重试  
52916 | 200 | 资金账户余额不足  
52917 | 200 | 询价数量不能低于下限  
52918 | 200 | 询价数量不能超过上限  
52919 | 200 | 闪兑交易参数{param}与报价不一致  
52920 | 200 | 闪兑交易数量不能超过报价数量  
52921 | 200 | 报价已交易，请重新询价  
52922 | 200 | 报价已过期，请重新询价  
52923 | 200 | 服务异常，请稍后重试  
52924 | 200 | 下单过于频繁，请稍后重试  
52925 | 200 | 客户自定义请求ID重复使用  
52926 | 200 | {param0}已过期  
52927 | 200 | 没有报价  
52928 | 200 | 数量应为下单数量精度的倍数  
52929 | 200 | 切换手续费支付为所得币后再闪兑  
  
### 交割合约类 

错误码从 55000 到 55999

错误码 | HTTP 状态码 | 错误提示  
---|---|---  
55000 | 200 | 交割后30分钟内不能转出  
  
### 永续合约类 

暂无

### 期权合约类 

暂无

### 资金类 

错误码从 58000 到 58999

错误码 | HTTP 状态码 | 错误提示  
---|---|---  
58002 | 200 | 请先开通余币宝服务  
58003 | 200 | 余币宝不支持该币种  
58004 | 200 | 账户冻结  
58005 | 200 | 申购/赎回额度不可超过{0}  
58006 | 200 | 币种{0}不支持当前操作  
58007 | 200 | 资金接口服务异常，请稍后再试。  
58008 | 200 | 您没有该币种资产  
58009 | 200 | 币对不存在  
58010 | 200 | 该链{0}暂不支持  
58011 | 200 | 抱歉，由于当地法律法规，欧易无法为{region}未认证用户提供服务，请先认证身份以继续使用欧易  
58012 | 200 | 抱歉，由于当地法律法规，欧易无法为{region}未认证用户提供服务，所以您无法向该用户转账  
58013 | 200 | 暂不支持提币功能，请咨询客服了解详情  
58014 | 200 | 暂不支持充值功能，请咨询客服了解详情  
58015 | 200 | 暂不支持划转功能，请咨询客服了解详情  
58016 | 200 | 仅交易团队主账户有权限调用此接口  
58100 | 200 | 行权或结算中，暂无法转入或转出  
58101 | 200 | 划转冻结  
58102 | 429 | 已达到速率限制。请参考相应的 API 文档与节流请求  
58103 | 200 | 该账户划转功能暂不可用，详情请联系客服  
58104 | 200 | 您在法币区的交易异常，现已被限制划转功能，请您联系在线客服以解除限制  
58105 | 200 | 您在法币区的交易异常，现已被限制划转功能，请您在网页或APP进行法币划  
转操作以完成身份验证  
58106 | 200 | 美元可转校验未通过  
58107 | 200 | 币种可转校验未通过  
58110 | 200 | 您所交易过或者持仓的 {businessType} {instFamily} 产品触发市场风控，平台已暂停您的资金转出功能，请稍后重试。如需进一步的协助，请联系客服。  
58111 | 200 | 永续合约正在收取资金费，暂时无法做资金划转，请稍后重试  
58112 | 200 | 资金划转失败，请联系客服进行处理  
58113 | 200 | 该币种不支持划转  
58114 | 400 | 转账金额必须大于 0  
58115 | 200 | 子账户不存在  
58116 | 200 | 转出数量大于最大可转数量  
58117 | 200 | 账户划转失败，请先处理负资产后再划转  
58119 | 200 | {0} 子账户没有转出权限，请先设置  
58120 | 200 | 划转服务暂不可用，请稍后重试  
58121 | 200 | 此次划转将导致您的仓位风险水平较高，进而可能引起爆仓。您需要重新调整划转金额，确保仓位处于安全水平后，再进行划转操作。  
58122 | 200 | 您的一部分现货正用于仓位间的 Delta 对冲，若划转数量超过可用金额，可能会影响现有的现货对冲结构，进而导致维持保证金率增加，请留意您的风险水平。  
58123 | 200 | 参数from与参数to不可相同  
58124 | 200 | 资金划转中，划转id：{trId}，请通过接口(GET /api/v5/asset/transfer-state)获取最新状态  
58125 | 200 | 不可交易资产仅支持子账户转主账户  
58126 | 200 | 不可交易资产划转，只能在资金账户间互转  
58127 | 200 | 主账户 API key 不支持当前 type 划转类型参数，请参考 API 文档描述  
58128 | 200 | 子账户 API key 不支持当前 type 划转类型参数，请参考 API 文档描述  
58129 | 200 | {param}错误或{param}与type不匹配  
58131 | 200 | 根据当地法律法规，欧易无法为未认证用户提供服务，请先完成身份认证再继续划转  
58132 | 200 | 根据当地法律法规，我们无法为仅完成基本认证的用户提供服务，请先完成高级认证再继续划转  
58200 | 200 | 该币种暂不支持从{0}提现至{1}，敬请谅解  
58201 | 200 | 今日提现金额累计超过每日限额  
58202 | 200 | NEO最小提现数量为1，且提现数量必须为整数  
58203 | 200 | 请先添加提现地址  
58204 | 200 | 因您的账户活动触发风控，暂停提现。请联系客户支持寻求帮助。  
58205 | 200 | 提现金额大于单笔提现最大金额  
58206 | 200 | 提现金额小于单笔最小提现金额  
58207 | 200 | 提币地址不在认证地址列表内 (带标签的提币地址格式为 “address:label”)  
58208 | 200 | 提现失败，邮箱未绑定  
58209 | 200 | 子账户不能充值或提现，请在主账户中进行提现。  
58210 | 200 | 由于无法验证您的身份，提币操作未能成功。请通过欧易 App 或官网完成提币操作。  
58212 | 200 | 提现手续费应填写为提币数量的{0}%  
58213 | 200 | 内部转账地址不合法，必须是邮箱、手机号或者账户名  
58214 | 200 | {chainName}维护中，暂停提币  
58215 | 200 | 提币申请ID不存在  
58216 | 200 | 不允许执行该操作  
58217 | 200 | 您当前的提现地址存在风险，暂时不能提现，详情请联系客服  
58218 | 200 | 内部提现失败，请检查参数toAddr与areaCode  
58219 | 200 | 为保障您的资金安全，修改手机号/邮箱/谷歌验证后24小时之内将无法提现  
58220 | 200 | 提币请求已撤销  
58221 | 200 | toAddr参数格式有误，提币地址需要加上标签，格式应该为“地址:标签”  
58222 | 200 | 无效的提币地址  
58223 | 200 | 提币到此合约地址需要支付更高的手续费  
58224 | 200 | 该类型币种暂不支持链上提币到 OKX 地址，请通过内部转账进行提币  
58225 | 200 | 抱歉，由于当地法律法规，欧易无法为{region}未认证用户提供服务，所以您无法向该用户转账  
58226 | 200 | {chainName} 已下线，不支持提币  
58227 | 200 | 不可交易资产提币只能全部提出  
58228 | 200 | 不可交易资产提币要求 API key 必须绑定 IP  
58229 | 200 | 资金账户手续费不足 {fee} USDT  
58230 | 200 | 根据欧易的合规政策，您需要完成 Lv. 1 身份认证方可继续提币  
58231 | 200 | 由于您的收款人尚未完成 Lv. 1 身份认证，内部转账暂时无法完成  
58232 | 200 | 您已超出个人身份验证 (Lv.1) 的提币上限，请完成照片验证 (Lv. 2) ，即可提升提币限额  
58233 | 200 | 根据当地法律法规，欧易无法为未认证用户提供服务，请先完成身份认证再继续提币  
58234 | 200 | 根据当地法律法规，收款人必须完成身份认证方可收到您的转账  
58235 | 200 | 根据当地法律法规，欧易无法为仅完成基本认证的用户提供服务，请先完成高级认证再继续提币  
58236 | 200 | 根据当地法律法规，仅完成基础认证的收款人无法收取转账，您的收款人必须完成高级认证方可收到您的转账  
58237 | 200 | 根据当地法律法规，请提供准确的接收方信息 (rcvrInfo)。对于交易所地址，请一并提供交易所信息和接收人的身份信息({recipientParameters})。  
58238 | 200 | 提币到交易所地址需提供完整的接收方信息，包括交易所信息和接收人的身份信息  
58239 | 200 | 不支持 API 提币至私人钱包。请通过欧易 App 或官网完成提币操作。  
58240 | 200 | 根据当地法律法规，为保障用户安全，您需要完成身份认证方可继续使用我们的服务。若您不希望进行身份认证，请联系客服团队了解详情。我们致力于为用户提供一个安全的平台，感谢您的理解与支持。  
58241 | 200 | 根据当地法律法规，内部转账功能暂时无法使用  
58242 | 200 | 受收款人所在地法律法规限制，本次内部转账无法完成  
58243 | 200 | 由于您的收款人尚未完成法币入金，对方不能接收本次转账  
58244 | 200 | 请先完成法币入金，再进行您的操作  
58248 | 200 | 根据当地法律法规限制，提币API已被暂时禁用。请使用OKX网页或OKX手机APP进行提币操作。  
58249 | 200 | 该币种暂不支持 API 提币，请于欧易网页端或 App 端进行提币。  
58252 | 200 | 为保障您的资产安全，首次进行 TRY 交易后，提币将在 48 小时内受到限制。  
58254 | 200 | 由于您所在国家或地区的合规限制，API 提币至私人钱包之前，需要先通过欧易 App 或官网完成 digital signature 或者 satoshi test。  
58256 | 200 | 您每 24 小时最多可提取价值为 {dailyLimit} {symbol} 的稳定币，当前还可提取 {quotaRemaining} {symbol}。  
58257 | 200 | 您每月最多可提取价值为 {monthlyLimit} {symbol} 的稳定币，当前还可提取 {quotaRemaining} {symbol}。  
58258 | 200 | 您每 24 小时最多可提取价值为 {dailyLimit} {symbol} 的数字货币，当前还可提取 {quotaRemaining} {symbol}。  
58300 | 200 | 创建充值地址超过上限  
58301 | 200 | 充值地址不存在  
58302 | 200 | 充值地址需要标签  
58303 | 200 | 该链{chain}充值当前不可用  
58304 | 200 | 创建invoice失败  
58305 | 200 | 找不到充币地址，请完成身份认证并生成充币地址  
58306 | 200 | 根据欧易的合规政策，您需要完成 Lv. 1 身份认证方可继续充币  
58307 | 200 | 您已超出个人身份验证 (Lv.1) 的充币上限。超出充币上限的资产已被冻结，请完成照片验证 (Lv. 2) ，即可提升充币限额  
58308 | 200 | 根据当地法律法规，欧易无法为未认证用户提供服务，请先完成身份认证再继续充币  
58309 | 200 | 根据当地法律法规，欧易无法为仅完成基本认证的用户提供服务，请先完成高级认证再继续充币  
58310 | 200 | 无法创建新的充币地址，请稍后重试  
58350 | 200 | 您的余额不足  
58351 | 200 | invoice已经过期  
58352 | 200 | invoice无效  
58353 | 200 | 充币数量需要在限额范围内  
58354 | 200 | 单日达到生成invoice 10,000 个的上限  
58355 | 200 | 用户没有使用此API接口的权限，请联系您的客户经理  
58356 | 200 | 同节点账户不支持闪电网络充币或提币  
58358 | 200 | 参数fromCcy与参数toCcy不可相同  
58373 | 200 | {ccy} 最小兑换数量为 {amount}  
58381 | 200 | 该功能暂不支持  
58382 | 200 | 无法处理解锁请求，请通过用户界面重试  
58383 | 200 | 未找到充值记录，无法处理解锁请求  
58384 | 200 | 根据当地法规，请提供准确的发送方信息。对于交易所地址，请同时提供交易所信息和发送方身份详情  
  
### 账户类 

错误码从 59000 到 59999

错误码 | HTTP 状态码 | 错误提示  
---|---|---  
59000 | 200 | 设置失败，请在设置前关闭任何挂单或持仓  
59001 | 200 | 当前存在借币，暂不可切换  
59002 | 200 | 子账户设置失败，请在设置前关闭任何子账户挂单、持仓或策略  
59004 | 200 | 只支持同一业务线下交易产品ID  
59005 | 200 | 逐仓自主划转保证金模式，初次划入仓位的资产价值需大于 10,000 USDT  
59006 | 200 | 此功能即将下线，无法切换到此模式  
59101 | 200 | 杠杆倍数无法修改，请撤销所有逐仓挂单后进行杠杆倍数修改  
59102 | 200 | 杠杆倍数超过最大杠杆倍数，请降低杠杆倍数  
59103 | 200 | 杠杆倍数过低，账户中没有足够的可用保证金可以追加，请提高杠杆倍数  
59104 | 200 | 杠杆倍数过高，借币仓位已超过该杠杆倍数的最大仓位，请降低杠杆倍数  
59105 | 400 | 杠杆倍数设置不能小于{0}，请提高杠杆倍数  
59106 | 200 | 您下单后仓位总张数所处档位的最高可用杠杆为{0}，请重新调整  
59107 | 200 | 杠杆倍数无法修改，请撤销所有全仓挂单后修改杠杆倍数  
59108 | 200 | 杠杆倍数过低，账户中保证金不足，请提高杠杆倍数  
59109 | 200 | 调整后，账户权益小于所需保证金，请重新调整杠杆倍数  
59110 | 200 | 该{0}对应的产品业务线不支持使用tgtCcy参数  
59111 | 200 | PM账户下衍生品全仓不支持杠杆查询  
59112 | 200 | 当前存在逐仓/全仓挂单，请撤销所有逐仓挂单后进行杠杆倍数修改  
59113 | 200 | 根据当地法律法规，您所在的地区无法使用保证金交易相关服务，如果您不是该地区居民，请进行KYC2身份认证  
59114 | 200 | 根据当地法律法规，您所在的地区无法使用保证金交易相关服务  
59117 | 200 | 所选币种数量不能超过 {param0} 个  
59118 | 200 | 下单金额需大于 {param0}  
59119 | 200 | 一键还债功能暂时关闭，请稍后重试  
59120 | 200 | 一键兑换主流币功能暂时关闭，请稍后重试  
59121 | 200 | 该批次正在处理中，请等待处理完  
59122 | 200 | 该批次已经处理完  
59123 | 200 | {param0}币种下单金额需大于 {param1}  
59124 | 200 | {param0} 币种下单金额需小于 {param1}  
59125 | 200 | {param0} 不支持当前操作  
59132 | 200 | 无法切换，请先撤销所有挂单，参考预检查接口并停止不兼容策略  
59133 | 200 | 无法切换，资产未达目标账户模式的要求  
59134 | 200 | 无法切换，请参考预检查接口并平掉不兼容的仓位  
59135 | 200 | 无法切换，请参考预检查接口并调整带跟单关系  
59136 | 200 | 无法切换，请预先设置全仓合约仓位的杠杆倍数  
59137 | 200 | 设置失败，请为所有全仓合约仓位降低杠杆倍数到 {param0} 或以下  
59138 | 200 | 无法切换，梯度档位校验失败  
59139 | 200 | 无法切换，保证金校验失败  
59140 | 200 | 请使用质押币种进行还币  
59141 | 200 | 最小还币数量为 {param0}，请增加还币币种数量或增加交易账户币种余额  
59142 | 200 | 还币失败，仅支持偿还可借币种  
59200 | 200 | 账户余额不足  
59201 | 200 | 账户余额是负数  
59202 | 200 | PM 账户下衍生品全仓不支持最大可开仓数量的查询  
59300 | 200 | 追加保证金失败，指定仓位不存在  
59301 | 200 | 调整保证金超过当前最大可调整数量  
59302 | 200 | 当前仓位存在平仓挂单，请撤销平仓挂单后进行保证金修改  
59303 | 200 | 可用保证金不足，请尝试增加保证金或减少借币数量  
59304 | 200 | 借币币种权益不足，请至少留有一天的利息  
59305 | 200 | 您当前没有进行尊享借币，无法设置尊享借币优先  
59306 | 200 | 借币数量超过总额度，不可继续借币  
59307 | 200 | 当前用户不满足尊享借币条件  
59308 | 200 | 市场化借币额度不足，VIP还币失败  
59309 | 200 | 还币数量超出已借数量，还币失败  
59310 | 200 | 当前账户不支持尊享借币  
59311 | 200 | 存在尊享借币，无法设置  
59312 | 200 | {币种}不支持尊享借币  
59313 | 200 | 无法还币。在一键借币模式下，您目前没有 ${ccy} 借币（币对：${ccyPair}）  
59314 | 200 | 当前用户该订单不是借币中，不允许还币  
59315 | 200 | VIP借币功能正在升级中,稍等10分钟之后再次操作  
59316 | 200 | 当前用户该币种存在借币申请中的订单，不允许借币  
59317 | 200 | 您当前币种 VIP 借币中的订单数量不能大于{maxNumber}(单)  
59319 | 200 | 由于您的资金已被占用，您暂时无法偿还借贷，请解除占用状态再进行还币  
59320 | 200 | 超出借贷限额  
59401 | 200 | 持仓价值达到持仓限制  
59402 | 200 | 查询条件中的instId的交易产品当前不是可交易状态，请填写单个instid逐个查询状态详情  
59410 | 200 | 只有当借币交易启用且该币种支持借币交易时，您才可以进行借币  
59411 | 200 | 无法手动借币，账户可用保证金不足  
59412 | 200 | 无法手动借币，您输入的数量已超过借币限额  
59413 | 200 | 该币种没有负债，无需还币  
59414 | 200 | 无法手动借币，您输入的数量应大于或等于最小借币数量 {param0}  
59417 | 200 | 由於利用率偏高，{TOKEN} 的手動簡單借幣已暫停，請稍後重試。  
59500 | 200 | 仅主账户有操作权限  
59501 | 200 | 每个账户最多可创建 50 个 API key  
59502 | 200 | 此备注名已存在。 请输入唯一的 API key 备注名称  
59503 | 200 | 每个 API key 最多可以绑定 20 个 IP 地址  
59504 | 200 | 子账户不支持提币功能，请在主账户中进行提币  
59505 | 200 | passphrase 格式不正确，支持6-32位字母和数字组合  
（区分大小写，不支持空格符号）  
59506 | 200 | API key 不存在  
59507 | 200 | 转出账户和转入账户必须是同一个母账户下的2个不同的子账户  
59508 | 200 | {0}该子账户被冻结  
59509 | 200 | 用户没有重置做市商保护状态的权限  
59510 | 200 | 子账户不存在  
59512 | 200 | 不支持为独立经纪商子账号设置主动转出权限，所有独立经纪商子账户默认有主动转出权限  
59515 | 200 | 您当前不在托管账户白名单上。请联系客服寻求帮助。  
59516 | 200 | 请先创建 Copper 托管资金账户  
59517 | 200 | 请先创建 Komainu 托管资金账户  
59518 | 200 | 您当前无法使用 API 创建子账户。请在网页端或 App 端创建。  
59519 | 200 | 此功能已冻结，暂时无法使用，冻结原因：{freezereason}  
59518 | 200 | 此账户无法使用 delta 中性策略模式  
59519 | 200 | 仅支持 VIP 1 及以上的用户使用 delta 中性策略模式  
59520 | 200 | 现货模式和合约模式不支持使用 delta 中性策略模式  
59521 | 200 | 不支持在 delta 中性策略模式模式，进行活期借币  
59522 | 200 | 不支持在 delta 中性策略模式模式，进行借币划转或借币提币  
59523 | 200 | 不支持在 delta 中性策略模式模式，进行逐仓下单或逐仓开仓  
59524 | 200 | 不支持在 delta 中性策略模式模式，进行期权交易或开期权仓位  
59525 | 200 | 部分策略交易和跟单交易，无法在 delta 中性策略模式模式下使用  
59526 | 200 | 策略模式设置失败。设置后，您账户的 Delta 权益比率将超过限制，触发“账户限制转出”状态，请降低 Delta 值后重试  
59527 | 200 | 使用 delta 中性策略模式，需开启全部币种的质押  
59528 | 200 | 策略模式设置失败。设置后，您账户在对应策略模式下的 {param0} 借币将超过主账户借币限额，请偿还借币后重试  
59529 | 200 | 策略模式设置失败。该账户属于 Delta 中性策略风险单元，设置策略模式前，请先将该账户移出风险单元  
59550 | 200 | 完成2级身份认证方可使用此功能。  
59601 | 200 | 子账户名称已存在  
59603 | 200 | 创建的子账户数量已达到上限  
59604 | 200 | 仅母账APIkey有操作此接口的权限  
59606 | 200 | 删除失败，请将子账户中的余额划转到母账户  
59608 | 200 | 仅Broker账户有操作此接口的权限  
59609 | 200 | 经纪商已经存在  
59610 | 200 | 经纪商不存在  
59611 | 200 | 经纪商状态是未审核  
59612 | 200 | 时间参数格式转换失败  
59613 | 200 | 当前未与子账户建立托管关系  
59614 | 200 | 托管子账户不支持此操作  
59615 | 200 | 起始日期和结束日期的时间间隔不能超过180天。  
59616 | 200 | 起始日期不能大于结束日期  
59617 | 200 | 子账户创建成功，账户等级设置失败  
59618 | 200 | 创建子账户失败  
59619 | 200 | 该接口不支持独立经纪商子账户，请使用为独立经纪商提供的专有接口。  
59622 | 200 | 您正在创建独立经纪商 2 级子账号。该 1 级子账号不存在或有误，请先创建 1 级子账号或使用正确的 1 级子账号。  
59623 | 200 | 独立经纪商 1 级子账号下存在 2 级子账号，请删除 2 级子账号后重试。  
59648 | 200 | 调整后实际现货对冲占用数量不足，有潜在爆仓风险，请调整现货对冲占用数量  
59649 | 200 | 关闭现货对冲占用模式可能会增加强制平仓的风险。请调整仓位，使保证金率处于安全状态。  
59650 | 200 | 切换对冲单位可能会增加强制平仓的风险。请调整仓位，使保证金率处于安全状态。  
59651 | 200 | 未开启现货对冲占用，无法设置现货对冲数量  
59652 | 200 | 不支持为非杠杆币种设置现货对冲占用数量  
59658 | 200 | 以下币种不支持开启质押：{ccy}  
59658 | 200 | 以下币种不支持开启质押：{ccy} 和 {ccy1}  
59658 | 200 | 以下币种不支持开启质押：{ccy}，{ccy1} 和 {ccy2}  
59658 | 200 | 以下币种不支持开启质押：{ccy}，{ccy1}，{ccy2} 以及其他 {number} 种  
59659 | 200 | 设置失败，需同时开启 {ccy} 和 {ccy1} 质押  
59660 | 200 | 设置失败，需同时关闭 {ccy} 和 {ccy1} 质押  
59661 | 200 | 设置失败，无法关闭 {ccy} 质押  
59662 | 200 | 设置失败，当前存在质押 {ccy} 为保证金的仓位或挂单  
59662 | 200 | 设置失败，当前存在质押 {ccy} 和 {ccy1} 为保证金的仓位或挂单  
59662 | 200 | 设置失败，当前存在质押 {ccy}，{ccy1} 和 {ccy2} 为保证金的仓位或挂单  
59662 | 200 | 设置失败，当前存在质押 {ccy}，{ccy1},{ccy2} 和其他 {number} 种币种为保证金的仓位或挂单  
59664 | 200 | 设置失败，当前存在 {ccy} 借币  
59664 | 200 | 设置失败，当前存在 {ccy} 和 {ccy1} 借币  
59664 | 200 | 设置失败，当前存在 {ccy}，{ccy1} 和{ccy2} 借币  
59664 | 200 | 设置失败，当前存在 {ccy}，{ccy1}，{ccy2} 和其他 {number} 种币种借币  
59665 | 200 | 设置失败，保证金不足。请增加质押币数量，以达到仓位保证金要求。  
59666 | 200 | 设置失败，无法同时开启和关闭币种质押。  
59667 | 200 | 设置失败，虚拟账户不支持开启质押币  
59668 | 200 | 调整杠杆倍数前，请先撤销逐仓止盈止损委托、移动止盈止损委托、计划委托，取消追逐限价委托并停止正在运行的策略  
59669 | 200 | 调整杠杆倍数前，请先撤销全仓止盈止损委托、移动止盈止损委托、计划委托和追逐限价委托，并停止正在运行的策略  
59670 | 200 | 当前该交易币对的订单数量超过 {param0} 个，调整杠杆倍数前请先撤销挂单或减少订单数量，订单数量低于或等于 {param1} 个后再进行操作  
59671 | 200 | {param0} 不支持自动赚币  
59672 | 200 | 关闭自动赚币后，不支持调整最低出借年化  
59673 | 200 | 开启自动赚币的 24 小时内，无法进行关闭，请在 {param0} 重试  
59674 | 200 | 该币种开启自动赚币后，不支持借币进行划转或提取  
59675 | 200 | {param0} 已开启自动赚币  
59676 | 200 | 当手续费等级等于或高于 {param0} 时，才可以开启自动赚币  
59678 | 200 | 切换失败。请撤销全部现货挂单后再次尝试。  
59679 | 200 | 切换失败，您当前的账户不支持切换手续费币种。  
59683 | 200 | 请先开启该币种的质押，再将其设置为结算币种  
59684 | 200 | 该币种不支持进行借币交易  
59686 | 200 | 不支持该币种作为结算币种  
59689 | 200 | 兑换失败。{param0} 兑换至 {param1} 的金额过低，无法执行  
59691 | 200 | 每日增加余额次数已达上限{param0}，请于 UTC 0:00 后重试或重置模拟盘  
59692 | 200 | {param0} 余额不足，操作后余额不可小于零  
59693 | 200 | {param0} 可转余额不足，部分资金被挂单或持仓占用，请取消订单或平仓后重试  
  
### 大宗交易 

错误码从 70000 开始

错误码 | HTTP 状态码 | 错误提示  
---|---|---  
70000 | 200 | 询价单不存在  
70001 | 200 | 报价单不存在  
70002 | 200 | 大宗交易不存在  
70003 | 200 | 公共的大宗交易不存在  
70004 | 200 | 无效的产品ID {instId}  
70005 | 200 | 组合交易的数量不能超过最大值  
70006 | 200 | 不满足最小资产要求  
70007 | 200 | 该产品类型 {instFamily} 的标的指数 {instType} 不存在  
70008 | 200 | MMP状态下操作失败。  
70009 | 200 | Data数组必须至少含有一个有效元素  
70010 | 200 | 时间戳参数必须是Unix时间戳的毫秒格式  
70011 | 200 | 产品类型 {instType} 存在重复设置  
70012 | 200 | 同一个instType{instType}下的instFamily/instId{instId} 存在重复设置  
70013 | 200 | endTs必须大于等于beginTs  
70014 | 200 | 不允许对所有产品类别设置includeAll=True.  
70015 | 200 | 您在完成高级身份认证后才能交易此类产品  
70016 | 200 | 交易产品设置中需选择至少一个交易品种  
70060 | 200 | 账号 {account} 不存在或输入有误。仓位转移的两边帐号必须属于同一个主帐号。  
70061 | 200 | 您输入的仓位数量应小于您当前的持仓量，方向应与您当前的持仓方向相反。  
70062 | 200 | 账号 {account} 已达到每日仓位转移次数的上限  
70064 | 200 | 仓位不存在  
70065 | 200 | 未能转移仓位，因为无法确定成交价格  
70066 | 200 | 现货模式不支持仓位转移，请切换到其他账户模式后重试  
70067 | 200 | 杠杆交易暂不支持仓位转移  
70100 | 200 | 组合交易中的产品ID重复  
70101 | 200 | clRfqId重复  
70102 | 200 | 未指定对手方  
70103 | 200 | 无效的对手方  
70105 | 200 | 非全现货的RFQ总价值应该大于最小名义值{nonSpotMinNotional}  
70106 | 200 | 下单数量小于最小交易数量  
70107 | 200 | 对手方的数量不能超过最大值  
70108 | 200 | 全现货的RFQ总价值应该大于最小名义值{spotMinNotional}  
70109 | 200 | 所选产品无有效对手方  
70200 | 200 | 不能取消处于{rfqState}状态的询价单  
70203 | 200 | 取消失败，由于询价单数量超过限制数量{rfqLimit}  
70207 | 200 | 取消失败，由于您没有询价挂单  
70208 | 200 | 取消失败，由于服务暂时不可用，请稍后重试  
70301 | 200 | clQuoteId重复  
70303 | 200 | 不能对处于{rfqState}状态的询价单报价  
70304 | 200 | 价格应该是下单价格精度的整数倍  
70305 | 200 | 买入价格不能高于报价  
70306 | 200 | 报价的组合交易没有匹配{rfqId}的组合交易  
70307 | 200 | 数量应该是下单数量精度的整数倍  
70308 | 200 | 不允许对自己的询价单报价  
70309 | 200 | 不允许对相同询价单进行同一方向的报价  
70310 | 200 | instId {instId} 报价不可以超过你预设的价格限制  
70400 | 200 | 不能取消处于{quoteState}状态的报价单  
70408 | 200 | 取消失败，由于报价单数量超过限制数量{quoteLimit}  
70409 | 200 | 取消失败，由于您没有报价挂单  
70501 | 200 | 询价单{rfqId}没有被{quoteId}报价  
70502 | 200 | 组合交易没有匹配{rfqId}的组合交易  
70503 | 200 | 执行腿的价值总和小于大宗交易的最小名义值  
70504 | 200 | 执行失败，因为询价单的状态是{rfqState}  
70505 | 200 | 执行失败，因为报价单的状态是{quoteState}  
70506 | 200 | 腿的数量比例与原RFQ不一致  
70507 | 200 | 部分执行尝试失败。须设置allowPartialExecution为`true`  
70508 | 200 | 没有可用的产品设置。  
70509 | 200 | 交易执行失败：对手方相关错误  
70510 | 200 | 如需了解错误详情，请查看 acctAlloc 字段  
70511 | 200 | 正在执行报价  
70514 | 200 | 每个交易品种的各类账户腿的数量之和，需与组合询价单总量一致  
70515 | 200 | 各子账户的腿数量与组合询价单的比例需在所有交易品种中保持一致  
70516 | 200 | 您最多可为组合询价单选择 {param0} 个子账户  
70517 | 200 | {param0} 不存在，或您暂无权限创建组合询价单  
70518 | 200 | 请勿为组合询价单重复选择同一账户  
75001 | 200 | 交易 ID 不存在  
75002 | 200 | {sprdId} : 目前无法下新订单或修改现有订单  
75003 | 200 | 价格无效  
56000 | 200 | 大宗交易不存在  
56001 | 200 | 多腿的数量不能超过 {legLimit}  
56002 | 200 | 执行和验证的多腿数量不匹配  
56003 | 200 | 重复的clBlockTdId  
56004 | 200 | 不允许自成交  
56005 | 200 | 执行和验证的clBlockTdId 不匹配  
56006 | 200 | 执行和验证的角色不能相同  
56007 | 200 | 执行和验证的第{legNo}条腿不匹配  
56008 | 200 | 重复的产品名称  
  
### 跟单交易 

错误码从 59200 到 59300

错误码 | HTTP 状态码 | 错误提示  
---|---|---  
59128 | 200 | 您当前身份为带单交易员。您设置的带单合约 {instrument} 杠杆倍数不能超过 {num}×  
59129 | 200 | 需优先使用 {param0} 进行还币  
59130 | 200 | 当资产 < 1 USD 时，仅支持用于偿还相同币种的借币  
59206 | 200 | 该带单交易员已无更多跟单空位  
59216 | 200 | 仓位不存在，请稍后重试  
59218 | 200 | 市价全平中...  
59256 | 200 | 无法切换为买卖模式，请降低跟单人数至1人  
59245 | 200 | 作为带单交易员，{param0} 单次下单张数应小于或等于 {param1}  
59247 | 200 | 杠杆倍数过高，当前仓位已超过该杠杆倍数的最大仓位，请重新调整杠杆倍数  
59260 | 200 | 您还不是现货带单交易员，请先在网页端/移动端完成申请  
59262 | 200 | 您还不是合约带单交易员，请先完成申请  
59641 | 200 | 由于您当前有定期借币，无法切换账户模式  
59642 | 200 | 跟单和带单员只能使用现货或合约模式  
59643 | 200 | 当前存在现货跟单，暂不可切换  
59263 | 200 | 仅白名单用户支持使用跟单功能，独立经纪商请联系 BD 进行处理  
59264 | 200 | 不支持现货跟单  
59267 | 200 | 取消失败，跟单关系不存在  
59268 | 200 | 存在交易员未带单的产品  
59269 | 200 | 该合约交易员不存在  
59270 | 200 | 固定金额跟单时，最大跟单金额 (copyTotalAmt) 需要大于等于单笔跟单金额 (copyAmt)  
59273 | 200 | 您还不是合约跟单用户，请先开始跟单  
59274 | 200 | 无法跟自己带的单  
59275 | 200 | 操作失败，您正在申请成为交易员，无法跟单  
59276 | 200 | 交易员正在退出，当前无法跟单  
59277 | 200 | 到达跟单人数上限，不允许继续跟单  
59278 | 200 | 正在处理您的停止跟单请求，请稍后再试  
59279 | 200 | 您已设置跟单，请勿重复设置  
59280 | 200 | 跟单关系不存在，请先进行首次设置  
59282 | 200 | 仅主账号在白名单中的独立经纪商 ND 子账户支持使用该接口，请联系 BD 进行处理  
59283 | 200 | 当前账户不在合约模式  
59284 | 200 | 超过本月 {param0} 次调整上限  
59286 | 200 | 当前账户模式为现货模式，无法成为合约带单人  
59287 | 200 | 请使用 {param0}-{param1} 范围内的分润比例  
59288 | 200 | 您当前身份为带单交易员。您的账户正处于组合保证金模式，请切换至合约或跨币种模式后重试。  
59130 | 200 | 最高止盈比例为 {num}%，请重新输入  
59258 | 200 | 您当前身份为带单交易员，暂不支持该操作  
59259 | 200 | 请输入在有效范围内的跟单比例  
59285 | 200 | 您尚未进行过带单或跟单操作  
59292 | 200 | 该带单交易员未开启自定义跟单模式  
  
### 策略交易 

错误码从 55100 到 55999

错误码 | HTTP 状态码 | 错误提示  
---|---|---  
55100 | 200 | 止盈百分比应在 {parameter1} ~ {parameter2} 的范围内  
55101 | 200 | 止损百分比应在 {parameter1} ~ {parameter2} 的范围内  
55102 | 200 | 止盈百分比需大于当前策略收益率  
55103 | 200 | 止损百分比需小于当前策略收益率  
55104 | 200 | 仅合约网格支持按收益率百分比止盈止损  
55105 | 200 | 当前状态不支持加仓操作  
55106 | 200 | 加仓金额应在 {parameter1} ~ {parameter2} 的范围内  
55111 | 200 | 此信号名称正在使用中，请尝试新名称  
55112 | 200 | 此信号不存在  
55113 | 200 | 创建信号策略的杠杆倍数大于交易产品列的最大杠杆倍数  
55116 | 200 | 每个交易对只能进行一笔追逐限价委托