---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/derivatives-trading-portfolio-margin/error-code
api_type: REST
updated_at: 2026-11-13 20:28:10.218180
---

# Error Codes

> Here is the error JSON payload:
    
    
    Code
    
    {
      "code":-1121,
      "msg":"Invalid symbol."
    }

Errors consist of two parts: an error code and a message.  
Codes are universal,but messages can vary.

## 10xx - General Server or Network issues

### -1000 UNKNOWN

  * An unknown error occured while processing the request.



### -1001 DISCONNECTED

  * Internal error; unable to process your request. Please try again.



### -1002 UNAUTHORIZED

  * You are not authorized to execute this request.



### -1003 TOO_MANY_REQUESTS

  * Too many requests; current limit is %s requests per minute. Please use the websocket for live updates to avoid polling the API.
  * Way too many requests; IP banned until %s. Please use the websocket for live updates to avoid bans.



### -1004 DUPLICATE_IP

  * This IP is already on the white list



### -1005 NO_SUCH_IP

  * No such IP has been white listed



### -1006 UNEXPECTED_RESP

  * An unexpected response was received from the message bus. Execution status unknown.



### -1007 TIMEOUT

  * Timeout waiting for response from backend server. Send status unknown; execution status unknown.



### -1008 Request Throttled

  * Request throttled by system-level protection. Reduce-only/close-position orders are exempt. Please try again.



### -1010 ERROR_MSG_RECEIVED

  * ERROR_MSG_RECEIVED.



### -1011 NON_WHITE_LIST

  * This IP cannot access this route.



### -1013 FILTER_FAILURE

  * Filter failure: `{filter}`



### -1014 UNKNOWN_ORDER_COMPOSITION

  * Unsupported order combination.



### -1015 TOO_MANY_ORDERS

  * Too many new orders.
  * Too many new orders; current limit is %s orders per %s.



### -1016 SERVICE_SHUTTING_DOWN

  * This service is no longer available.



### -1020 UNSUPPORTED_OPERATION

  * This operation is not supported.



### -1021 INVALID_TIMESTAMP

  * Timestamp for this request is outside of the recvWindow.
  * Timestamp for this request was 1000ms ahead of the server's time.



### -1022 INVALID_SIGNATURE

  * Signature for this request is not valid.



### -1023 START_TIME_GREATER_THAN_END_TIME

  * Start time is greater than end time.



## 11xx - Request issues

### -1100 ILLEGAL_CHARS

  * Illegal characters found in a parameter.
  * Illegal characters found in parameter '%s'; legal range is '%s'.



### -1101 TOO_MANY_PARAMETERS

  * Too many parameters sent for this endpoint.
  * Too many parameters; expected '%s' and received '%s'.
  * Duplicate values for a parameter detected.



### -1102 MANDATORY_PARAM_EMPTY_OR_MALFORMED

  * A mandatory parameter was not sent, was empty/null, or malformed.
  * Mandatory parameter '%s' was not sent, was empty/null, or malformed.
  * Param '%s' or '%s' must be sent, but both were empty/null!



### -1103 UNKNOWN_PARAM

  * An unknown parameter was sent.



### -1104 UNREAD_PARAMETERS

  * Not all sent parameters were read.
  * Not all sent parameters were read; read '%s' parameter(s) but was sent '%s'.



### -1105 PARAM_EMPTY

  * A parameter was empty.
  * Parameter '%s' was empty.



### -1106 PARAM_NOT_REQUIRED

  * A parameter was sent when not required.
  * Parameter '%s' sent when not required.



### -1108 BAD_ASSET

  * Invalid asset.



### -1109 BAD_ACCOUNT

  * Invalid account.



### -1110 BAD_INSTRUMENT_TYPE

  * Invalid symbolType.



### -1111 BAD_PRECISION

  * Precision is over the maximum defined for this asset.



### -1112 NO_DEPTH

  * No orders on book for symbol.



### -1113 WITHDRAW_NOT_NEGATIVE

  * Withdrawal amount must be negative.



### -1114 TIF_NOT_REQUIRED

  * TimeInForce parameter sent when not required.



### -1115 INVALID_TIF

  * Invalid timeInForce.



### -1116 INVALID_ORDER_TYPE

  * Invalid orderType.



### -1117 INVALID_SIDE

  * Invalid side.



### -1118 EMPTY_NEW_CL_ORD_ID

  * New client order ID was empty.



### -1119 EMPTY_ORG_CL_ORD_ID

  * Original client order ID was empty.



### -1120 BAD_INTERVAL

  * Invalid interval.



### -1121 BAD_SYMBOL

  * Invalid symbol.



### -1125 INVALID_LISTEN_KEY

  * This listenKey does not exist. Please use `POST /papi/v1/listenKey` to recreate `listenKey`



### -1127 MORE_THAN_XX_HOURS

  * Lookup interval is too big.
  * More than %s hours between startTime and endTime.



### -1128 OPTIONAL_PARAMS_BAD_COMBO

  * Combination of optional parameters invalid.



### -1130 INVALID_PARAMETER

  * Invalid data sent for a parameter.
  * Data sent for parameter '%s' is not valid.



### -1136 INVALID_NEW_ORDER_RESP_TYPE

  * Invalid newOrderRespType.



## 20xx - Processing Issues

### -2010 NEW_ORDER_REJECTED

  * NEW_ORDER_REJECTED
  * The new order was rejected. See the returned msg for the specific reason, for example "Account has insufficient balance for requested action."



### -2011 CANCEL_REJECTED

  * CANCEL_REJECTED



### -2013 NO_SUCH_ORDER

  * Order does not exist.



### -2014 BAD_API_KEY_FMT

  * API-key format invalid.



### -2015 REJECTED_MBX_KEY

  * Invalid API-key, IP, or permissions for action.



### -2016 NO_TRADING_WINDOW

  * No trading window could be found for the symbol. Try ticker/24hrs instead.



### -2018 BALANCE_NOT_SUFFICIENT

  * Balance is insufficient.



### -2019 MARGIN_NOT_SUFFICIEN

  * Margin is insufficient.



### -2020 UNABLE_TO_FILL

  * Unable to fill.



### -2021 ORDER_WOULD_IMMEDIATELY_TRIGGER

  * Order would immediately trigger.



### -2022 REDUCE_ONLY_REJECT

  * ReduceOnly Order is rejected.
  * This indicates the new reduce-only order conflicts with existing open orders; cancel the existing order and resubmit the reduce-only order.



### -2023 USER_IN_LIQUIDATION

  * User in liquidation mode now.



### -2024 POSITION_NOT_SUFFICIENT

  * Position is not sufficient.



### -2025 MAX_OPEN_ORDER_EXCEEDED

  * Reach max open order limit.



### -2026 REDUCE_ONLY_ORDER_TYPE_NOT_SUPPORTED

  * This OrderType is not supported when reduceOnly.



### -2027 MAX_LEVERAGE_RATIO

  * Exceeded the maximum allowable position at current leverage.



### -2028 MIN_LEVERAGE_RATIO

  * Leverage is smaller than permitted: insufficient margin balance.



## 40xx - Filters and other Issues

### -4000 INVALID_ORDER_STATUS

  * Invalid order status.



### -4001 PRICE_LESS_THAN_ZERO

  * Price less than 0.



### -4002 PRICE_GREATER_THAN_MAX_PRICE

  * Price greater than max price.



### -4003 QTY_LESS_THAN_ZERO

  * Quantity less than zero.



### -4004 QTY_LESS_THAN_MIN_QTY

  * Quantity less than min quantity.



### -4005 QTY_GREATER_THAN_MAX_QTY

  * Quantity greater than max quantity.



### -4006 STOP_PRICE_LESS_THAN_ZERO

  * Stop price less than zero.



### -4007 STOP_PRICE_GREATER_THAN_MAX_PRICE

  * Stop price greater than max price.



### -4008 TICK_SIZE_LESS_THAN_ZERO

  * Tick size less than zero.



### -4009 MAX_PRICE_LESS_THAN_MIN_PRICE

  * Max price less than min price.



### -4010 MAX_QTY_LESS_THAN_MIN_QTY

  * Max qty less than min qty.



### -4011 STEP_SIZE_LESS_THAN_ZERO

  * Step size less than zero.



### -4012 MAX_NUM_ORDERS_LESS_THAN_ZERO

  * Max mum orders less than zero.



### -4013 PRICE_LESS_THAN_MIN_PRICE

  * Price less than min price.



### -4014 PRICE_NOT_INCREASED_BY_TICK_SIZE

  * Price not increased by tick size.



### -4015 INVALID_CL_ORD_ID_LEN

  * Client order id is not valid.
  * Client order id length should not be more than 36 chars



### -4016 PRICE_HIGHTER_THAN_MULTIPLIER_UP

  * Price is higher than mark price multiplier cap.



### -4017 MULTIPLIER_UP_LESS_THAN_ZERO

  * Multiplier up less than zero.



### -4018 MULTIPLIER_DOWN_LESS_THAN_ZERO

  * Multiplier down less than zero.



### -4019 COMPOSITE_SCALE_OVERFLOW

  * Composite scale too large.



### -4020 TARGET_STRATEGY_INVALID

  * Target strategy invalid for orderType '%s',reduceOnly '%b'.



### -4021 INVALID_DEPTH_LIMIT

  * Invalid depth limit.
  * '%s' is not valid depth limit.



### -4022 WRONG_MARKET_STATUS

  * market status sent is not valid.



### -4023 QTY_NOT_INCREASED_BY_STEP_SIZE

  * Qty not increased by step size.



### -4024 PRICE_LOWER_THAN_MULTIPLIER_DOWN

  * Price is lower than mark price multiplier floor.



### -4025 MULTIPLIER_DECIMAL_LESS_THAN_ZERO

  * Multiplier decimal less than zero.



### -4026 COMMISSION_INVALID

  * Commission invalid.
  * `%s` less than zero.
  * `%s` absolute value greater than `%s`



### -4027 INVALID_ACCOUNT_TYPE

  * Invalid account type.



### -4028 INVALID_LEVERAGE

  * Invalid leverage
  * Leverage `%s` is not valid
  * Leverage `%s` already exist with `%s`



### -4029 INVALID_TICK_SIZE_PRECISION

  * Tick size precision is invalid.



### -4030 INVALID_STEP_SIZE_PRECISION

  * Step size precision is invalid.



### -4031 INVALID_WORKING_TYPE

  * Invalid parameter working type
  * Invalid parameter working type: `%s`



### -4032 EXCEED_MAX_CANCEL_ORDER_SIZE

  * Exceed maximum cancel order size.
  * Invalid parameter working type: `%s`



### -4033 INSURANCE_ACCOUNT_NOT_FOUND

  * Insurance account not found.



### -4044 INVALID_BALANCE_TYPE

  * Balance Type is invalid.



### -4045 MAX_STOP_ORDER_EXCEEDED

  * Reach max stop order limit.



### -4046 NO_NEED_TO_CHANGE_MARGIN_TYPE

  * No need to change margin type.



### -4047 THERE_EXISTS_OPEN_ORDERS

  * Margin type cannot be changed if there exists open orders.



### -4048 THERE_EXISTS_QUANTITY

  * Margin type cannot be changed if there exists position.



### -4049 ADD_ISOLATED_MARGIN_REJECT

  * Add margin only support for isolated position.



### -4050 CROSS_BALANCE_INSUFFICIENT

  * Cross balance insufficient.



### -4051 ISOLATED_BALANCE_INSUFFICIENT

  * Isolated balance insufficient.



### -4052 NO_NEED_TO_CHANGE_AUTO_ADD_MARGIN

  * No need to change auto add margin.



### -4053 AUTO_ADD_CROSSED_MARGIN_REJECT

  * Auto add margin only support for isolated position.



### -4054 ADD_ISOLATED_MARGIN_NO_POSITION_REJECT

  * Cannot add position margin: position is 0.



### -4055 AMOUNT_MUST_BE_POSITIVE

  * Amount must be positive.



### -4056 INVALID_API_KEY_TYPE

  * Invalid api key type.



### -4057 INVALID_RSA_PUBLIC_KEY

  * Invalid api public key



### -4058 MAX_PRICE_TOO_LARGE

  * maxPrice and priceDecimal too large,please check.



### -4059 NO_NEED_TO_CHANGE_POSITION_SIDE

  * No need to change position side.



### -4060 INVALID_POSITION_SIDE

  * Invalid position side.



### -4061 POSITION_SIDE_NOT_MATCH

  * Order's position side does not match user's setting.



### -4062 REDUCE_ONLY_CONFLICT

  * Invalid or improper reduceOnly value.



### -4063 INVALID_OPTIONS_REQUEST_TYPE

  * Invalid options request type



### -4064 INVALID_OPTIONS_TIME_FRAME

  * Invalid options time frame



### -4065 INVALID_OPTIONS_AMOUNT

  * Invalid options amount



### -4066 INVALID_OPTIONS_EVENT_TYPE

  * Invalid options event type



### -4067 POSITION_SIDE_CHANGE_EXISTS_OPEN_ORDERS

  * Position side cannot be changed if there exists open orders.



### -4068 POSITION_SIDE_CHANGE_EXISTS_QUANTITY

  * Position side cannot be changed if there exists position.



### -4069 INVALID_OPTIONS_PREMIUM_FEE

  * Invalid options premium fee



### -4070 INVALID_CL_OPTIONS_ID_LEN

  * Client options id is not valid.
  * Client options id length should be less than 32 chars



### -4071 INVALID_OPTIONS_DIRECTION

  * Invalid options direction



### -4072 OPTIONS_PREMIUM_NOT_UPDATE

  * premium fee is not updated, reject order



### -4073 OPTIONS_PREMIUM_INPUT_LESS_THAN_ZERO

  * input premium fee is less than 0, reject order



### -4074 OPTIONS_AMOUNT_BIGGER_THAN_UPPER

  * Order amount is bigger than upper boundary or less than 0, reject order



### -4075 OPTIONS_PREMIUM_OUTPUT_ZERO

  * output premium fee is less than 0, reject order



### -4076 OPTIONS_PREMIUM_TOO_DIFF

  * original fee is too much higher than last fee



### -4077 OPTIONS_PREMIUM_REACH_LIMIT

  * place order amount has reached to limit, reject order



### -4078 OPTIONS_COMMON_ERROR

  * options internal error



### -4079 INVALID_OPTIONS_ID

  * invalid options id
  * invalid options id: %s
  * duplicate options id %d for user %d



### -4080 OPTIONS_USER_NOT_FOUND

  * user not found
  * user not found with id: %s



### -4081 OPTIONS_NOT_FOUND

  * options not found
  * options not found with id: %s



### -4082 INVALID_BATCH_PLACE_ORDER_SIZE

  * Invalid number of batch place orders.
  * Invalid number of batch place orders: %s



### -4083 PLACE_BATCH_ORDERS_FAIL

  * Fail to place batch orders.



### -4084 UPCOMING_METHOD

  * Method is not allowed currently. Upcoming soon.



### -4085 INVALID_NOTIONAL_LIMIT_COEF

  * Invalid notional limit coefficient



### -4086 INVALID_PRICE_SPREAD_THRESHOLD

  * Invalid price spread threshold



### -4087 REDUCE_ONLY_ORDER_PERMISSION

  * User can only place reduce only order



### -4088 NO_PLACE_ORDER_PERMISSION

  * User can not place order currently



### -4104 INVALID_CONTRACT_TYPE

  * Invalid contract type



### -4114 INVALID_CLIENT_TRAN_ID_LEN

  * clientTranId is not valid
  * Client tran id length should be less than 64 chars



### -4115 DUPLICATED_CLIENT_TRAN_ID

  * clientTranId is duplicated
  * Client tran id should be unique within 7 days



### -4118 REDUCE_ONLY_MARGIN_CHECK_FAILED

  * ReduceOnly Order Failed. Please check your existing position and open orders
  * This indicates the new reduce-only order conflicts with existing open orders; cancel the existing order and resubmit the reduce-only order.



### -4131 MARKET_ORDER_REJECT

  * The counterparty's best price does not meet the PERCENT_PRICE filter limit



### -4135 INVALID_ACTIVATION_PRICE

  * Invalid activation price



### -4137 QUANTITY_EXISTS_WITH_CLOSE_POSITION

  * Quantity must be zero with closePosition equals true



### -4138 REDUCE_ONLY_MUST_BE_TRUE

  * Reduce only must be true with closePosition equals true



### -4139 ORDER_TYPE_CANNOT_BE_MKT

  * Order type can not be market if it's unable to cancel



### -4140 INVALID_OPENING_POSITION_STATUS

  * Invalid symbol status for opening position



### -4141 SYMBOL_ALREADY_CLOSED

  * Symbol is closed



### -4142 STRATEGY_INVALID_TRIGGER_PRICE

  * REJECT: take profit or stop order will be triggered immediately



### -4144 INVALID_PAIR

  * Invalid pair



### -4161 ISOLATED_LEVERAGE_REJECT_WITH_POSITION

  * Leverage reduction is not supported in Isolated Margin Mode with open positions



### -4164 MIN_NOTIONAL

  * Order's notional must be no smaller than 5.0 (unless you choose reduce only)
  * Order's notional must be no smaller than %s (unless you choose reduce only)



### -4165 INVALID_TIME_INTERVAL

  * Invalid time interval
  * Maximum time interval is %s days



### -4183 PRICE_HIGHTER_THAN_STOP_MULTIPLIER_UP

  * Price is higher than stop price multiplier cap.
  * Limit price can't be higher than %s.



### -4184 PRICE_LOWER_THAN_STOP_MULTIPLIER_DOWN

  * Price is lower than stop price multiplier floor.
  * Limit price can't be lower than %s.



### -4220 CANNOT_CHANGE_DUAL_SIDE

  * The operation is rejected because the CM dual-side is not allowed to be different from UM dual-side.



### -4405 UM_REDUCE_ONLY_ONLY

  * Only reduceOnly order is allowed, please try again later.



### -4407 ACCOUNT_REDUCE_ONLY

  * Restricted account permission: can only place reduceOnly order on the symbol.



### -4415 CM_REDUCE_ONLY_ONLY

  * Only reduceOnly order is allowed, please try again later.



### -4517 SYMBOL_REDUCE_ONLY

  * Symbol is under position risk control, only reduce-only order is allowed.



### -4518 SYMBOL_REDUCE_ONLY_BUY

  * Symbol is under position risk control, buy order can only works with reduce-only.



### -4519 SYMBOL_REDUCE_ONLY_SELL

  * Symbol is under position risk control, sell order can only works with reduce-only.



## 50xx/51xxx - Order Execution Issues

### -5021 FOK_ORDER_REJECT

  * Due to the order could not be filled immediately, the FOK order has been rejected.



### -5022 GTX_ORDER_REJECT

  * Due to the order could not be executed as maker, the Post Only order will be rejected.



### -5028 ME_RECVWINDOW_REJECT

  * The requested timestamp is outside the recvWindow of the matching engine



### -5041 TOO_MANY_REQUESTS_IN_QUEUE

  * Time out for too many requests from this account queueing at the same time.



### 51006 EXCEED_MAX_BORROWABLE

  * Your borrow amount has exceed maximum borrow amount.



### 51007 HAS_PENDING_TRANSACTION

  * You have pending borrow or repayment, please try again later.



### 51013 EMPTY_ASSET_ADMIN

  * Not a valid margin asset.



### 51014 ASSET_ADMIN_BAN_BORROW

  * This asset is currently not available for borrowing.



### 51017 REPAY_EXCEED_LIABILITY

  * Repay amount exceeds borrow amount.



### 51018 LT_MIN_REPAY

  * Repay amount less than minimum repay amount.



### 51022 EXCEED_MAX_ROLLOUT

  * Transfer out amount exceeds max amount.



### 51026 INVALID_INPUT_PARAM

  * Invalid input parameter.



### 51038 LISTEN_KEY_NOT_FOUND

  * Listen key not found.



### 51042 FREQUENT_OPERATION

  * Operation performed too frequently.



### 51061 BORROW_BALANCE_NOT_CLEARED_AND_ASSET

  * The platform's lendable token is temporarily insufficient. Please try again later.



### 51068 LIQUIDATION_IN_PROGRESS

  * Unable to trade. Your margin account is currently in liquidation. Please try again once liquidation is processed.



### 51078 NET_ASSET_MUST_LTE_RATIO

  * Fail to retrieve margin assets.



### 51113 TRADE_NOT_ALLOWED_LOSS_LIMIT

  * The limit price needs to be within (`{range}`) of current index price for this margin trading pair.
  * For OTO/OTOCO order types, the trigger price of the secondary order must be within (`{range}`) of primary order price. This rule applies to sell at a lower limit price and buy at a higher limit price.



### 51122 PM_FUNCTION_NOT_SUPPORTED

  * Portfolio Margin account users cannot use this function.



### 51169 PLATFORM_MAX_TRANSFER_IN_EXCEEDED

  * The amount of token exceeds the platform limit. You can transfer in or buy at most `{num}`.



### 51238 BSTOCK_TRADE_NOT_ELIGIBLE

  * bStocks related margin features are currently unavailable. Please complete the Suitability Assessment Questionnaire first.



### 51998 SYSTEM_BUSY

  * System is busy. Please try again later.



### 51999 UNKNOWN

  * System abnormality.
  * An unknown error occurred while processing the request.



### 331020 INSUFFICIENT_SPOT_AVAILABLE_BALANCE

  * The available spot balance is insufficient for this transfer.



Was this page helpful?

Last modified on November 12, 2026

[User Data Streams](/en/docs/products/derivatives-trading-portfolio-margin/user-data-streams)[Public API Definitions](/en/docs/products/derivatives-trading-portfolio-margin/common-definition)

---

# 错误代码

> error JSON payload:
    
    
    Code
    
    {
      "code":-1121,
      "msg":"Invalid symbol."
    }

错误由两部分组成：错误代码和消息。 代码是通用的，但是消息可能会有所不同。

## 10xx - 常规服务器或网络问题

### -1000 UNKNOWN

  * An unknown error occured while processing the request.
  * 处理请求时发生未知错误。



### -1001 DISCONNECTED

  * Internal error; unable to process your request. Please try again.
  * 内部错误; 无法处理您的请求。 请再试一次.



### -1002 UNAUTHORIZED

  * You are not authorized to execute this request.
  * 您无权执行此请求。



### -1003 TOO_MANY_REQUESTS

  * Too many requests; current limit is %s requests per minute. Please use the websocket for live updates to avoid polling the API.
  * 请求权重过多； 当前限制为每分钟％s请求权重。 请使用websocket进行实时更新，以避免轮询API。
  * Way too many requests; IP banned until %s. Please use the websocket for live updates to avoid bans.
  * 请求权重过多； IP被禁止，直到％s。 请使用websocket进行实时更新，以免被禁。



### -1004 DUPLICATE_IP

  * This IP is already on the white list
  * IP地址已经在白名单



### -1005 NO_SUCH_IP

  * No such IP has been white listed
  * 白名单上没有此IP地址



### -1006 UNEXPECTED_RESP

  * An unexpected 响应 was received from the message bus. Execution status unknown.
  * 从消息总线收到意外的响应。执行状态未知。



### -1007 TIMEOUT

  * Timeout waiting for 响应 from backend server. Send status unknown; execution status unknown.
  * 等待后端服务器响应超时。 发送状态未知； 执行状态未知。



### -1008 Request Throttled

  * Request throttled by system-level protection. Reduce-only/close-position orders are exempt. Please try again.
  * 等待后端服务器响应超时。 发送状态未知； 执行状态未知。



### -1014 UNKNOWN_ORDER_COMPOSITION

  * Unsupported order combination.
  * 不支持当前的下单参数组合



### -1015 TOO_MANY_ORDERS

  * Too many new orders.
  * 新订单太多。
  * Too many new orders; current limit is %s orders per %s.
  * 新订单太多； 当前限制为每％s ％s个订单。



### -1016 SERVICE_SHUTTING_DOWN

  * This service is no longer available.
  * 该服务不可用。



### -1020 UNSUPPORTED_OPERATION

  * This operation is not supported.
  * 不支持此操作。



### -1021 INVALID_TIMESTAMP

  * Timestamp for this request is outside of the recvWindow.
  * 此请求的时间戳在recvWindow之外。
  * Timestamp for this request was 1000ms ahead of the server's time.
  * 此请求的时间戳比服务器时间提前1000毫秒。



### -1022 INVALID_SIGNATURE

  * Signature for this request is not valid.
  * 此请求的签名无效。



### -1023 START_TIME_GREATER_THAN_END_TIME

  * Start time is greater than end time.
  * 参数里面的开始时间在结束时间之后



## 11xx - Request issues

### -1100 ILLEGAL_CHARS

  * Illegal characters found in a parameter.
  * 在参数中发现非法字符。
  * Illegal characters found in parameter '%s'; legal range is '%s'.
  * 在参数`％s`中发现非法字符； 合法范围是`％s`。



### -1101 TOO _MANY_ 参数

  * Too many 参数 sent for this endpoint.
  * 为此端点发送的参数太多。
  * Too many 参数; expected '%s' and received '%s'.
  * 参数太多；预期为`％s`并收到了`％s`。
  * Duplicate values for a parameter detected.
  * 检测到的参数值重复。



### -1102 MANDATORY_PARAM_EMPTY_OR_MALFORMED

  * A mandatory parameter was not sent, was empty/null, or malformed.
  * 未发送强制性参数，该参数为空/空或格式错误。
  * Mandatory parameter '%s' was not sent, was empty/null, or malformed.
  * 强制参数`％s`未发送，为空/空或格式错误。
  * Param '%s' or '%s' must be sent, but both were empty/null!
  * 必须发送参数`％s`或`％s`，但两者均为空！



### -1103 UNKNOWN_PARAM

  * An unknown parameter was sent.
  * 发送了未知参数。



### -1104 UNREAD_参数

  * Not all sent 参数 were read.
  * 并非所有发送的参数都被读取。
  * Not all sent 参数 were read; read '%s' parameter(s) but was sent '%s'.
  * 并非所有发送的参数都被读取； 读取了`％s`参数，但被发送了`％s`。



### -1105 PARAM_EMPTY

  * A parameter was empty.
  * 参数为空。
  * Parameter '%s' was empty.
  * 参数`％s`为空。



### -1106 PARAM_NOT_REQUIRED

  * A parameter was sent when not required.
  * 发送了不需要的参数。
  * Parameter '%s' sent when not required.
  * 发送了不需要参数`％s`。



### -1111 BAD_PRECISION

  * Precision is over the maximum defined for this asset.
  * 精度超过为此资产定义的最大值。



### -1112 NO_DEPTH

  * No orders on book for symbol.
  * 交易对没有挂单。



### -1114 TIF_NOT_REQUIRED

  * TimeInForce parameter sent when not required.
  * 发送的`TimeInForce`参数不需要。



### -1115 INVALID_TIF

  * Invalid timeInForce.
  * 无效的`timeInForce`



### -1116 INVALID_ORDER_TYPE

  * Invalid orderType.
  * 无效订单类型。



### -1117 INVALID_SIDE

  * Invalid side.
  * 无效买卖方向。



### -1118 EMPTY_NEW_CL_ORD_ID

  * New client order ID was empty.
  * 新的客户订单ID为空。



### -1119 EMPTY_ORG_CL_ORD_ID

  * Original client order ID was empty.
  * 客户自定义的订单ID为空。



### -1120 BAD_INTERVAL

  * Invalid interval.
  * 无效时间间隔。



### -1121 BAD_SYMBOL

  * Invalid symbol.
  * 无效的交易对。



### -1125 INVALID_LISTEN_KEY

  * This listenKey does not exist.
  * 此`listenKey`不存在。建议重新使用`POST /fapi/v1/listenKey`生成`listenKey`



### -1127 MORE_THAN_XX_HOURS

  * Lookup interval is too big.
  * 查询间隔太大。
  * More than %s hours between startTime and endTime.
  * 从开始时间到结束时间之间超过`％s`小时。



### -1128 OPTIONAL_PARAMS_BAD_COMBO

  * Combination of optional 参数 invalid.
  * 可选参数组合无效。



### -1130 INVALID_PARAMETER

  * Invalid data sent for a parameter.
  * 发送的参数为无效数据。
  * Data sent for parameter '%s' is not valid.
  * 发送参数`％s`的数据无效。



### -1136 INVALID_NEW_ORDER_RESP_TYPE

  * Invalid newOrderRespType.
  * 无效的 newOrderRespType。



## 20xx - Processing Issues

### -2010 NEW_ORDER_REJECTED

  * NEW_ORDER_REJECTED
  * 新订单被拒绝。具体原因见返回的 msg，例如 "Account has insufficient balance for requested action."（账户余额不足）。



### -2011 CANCEL_REJECTED

  * CANCEL_REJECTED
  * 取消订单被拒绝



### -2013 NO_SUCH_ORDER

  * Order does not exist.
  * 订单不存在。



### -2014 BAD_API_KEY_FMT

  * API-key format invalid.
  * API-key 格式无效。



### -2015 REJECTED_MBX_KEY

  * Invalid API-key, IP, or permissions for action.
  * 无效的API密钥，IP或操作权限。



### -2016 NO_TRADING_WINDOW

  * No trading window could be found for the symbol. Try ticker/24hrs instead.
  * 找不到该交易对的交易窗口。 尝试改为24小时自动报价。



### -2018 BALANCE_NOT_SUFFICIENT

  * Balance is insufficient.
  * 余额不足



### -2019 MARGIN_NOT_SUFFICIEN

  * Margin is insufficient.
  * 杠杆账户余额不足



### -2020 UNABLE_TO_FILL

  * Unable to fill.
  * 无法成交



### -2021 ORDER_WOULD_IMMEDIATELY_TRIGGER

  * Order would immediately trigger.
  * 订单可能被立刻触发



### -2022 REDUCE_ONLY_REJECT

  * ReduceOnly Order is rejected.
  * `ReduceOnly`订单被拒绝
  * 这表示新的「仅减仓（reduce-only）」订单与当前未成交同向订单存在冲突；请先取消现有订单，然后重新提交仅减仓订单。



### -2023 USER_IN_LIQUIDATION

  * User in liquidation mode now.
  * 用户正处于被强平模式



### -2024 POSITION_NOT_SUFFICIENT

  * Position is not sufficient.
  * 持仓不足



### -2025 MAX_OPEN_ORDER_EXCEEDED

  * Reach max open order limit.
  * 挂单量达到上限



### -2026 REDUCE_ONLY_ORDER_TYPE_NOT_SUPPORTED

  * This OrderType is not supported when reduceOnly.
  * 当前订单类型不支持`reduceOnly`



### -2027 MAX_LEVERAGE_RATIO

  * Exceeded the maximum allowable position at current leverage.
  * 挂单或持仓超出当前初始杠杆下的最大值



### -2028 MIN_LEVERAGE_RATIO

  * Leverage is smaller than permitted: insufficient margin balance.
  * 调整初始杠杆过低，导致可用余额不足



## 40xx - Filters and other Issues

### -4000 INVALID_ORDER_STATUS

  * Invalid order status.
  * 订单状态不正确



### -4001 PRICE_LESS_THAN_ZERO

  * Price less than 0.
  * 价格小于0



### -4002 PRICE_GREATER_THAN_MAX_PRICE

  * Price greater than max price.
  * 价格超过最大值



### -4003 QTY_LESS_THAN_ZERO

  * Quantity less than zero.
  * 数量小于0



### -4004 QTY_LESS_THAN_MIN_QTY

  * Quantity less than min quantity.
  * 数量小于最小值



### -4005 QTY_GREATER_THAN_MAX_QTY

  * Quantity greater than max quantity.
  * 数量大于最大值



### -4006 STOP_PRICE_LESS_THAN_ZERO

  * Stop price less than zero.
  * 触发价小于最小值



### -4007 STOP_PRICE_GREATER_THAN_MAX_PRICE

  * Stop price greater than max price.
  * 触发价大于最大值



### -4008 TICK_SIZE_LESS_THAN_ZERO

  * Tick size less than zero.
  * 价格精度小于0



### -4009 MAX_PRICE_LESS_THAN_MIN_PRICE

  * Max price less than min price.
  * 最大价格小于最小价格



### -4010 MAX_QTY_LESS_THAN_MIN_QTY

  * Max qty less than min qty.
  * 最大数量小于最小数量



### -4011 STEP_SIZE_LESS_THAN_ZERO

  * Step size less than zero.
  * 步进值小于0



### -4012 MAX_NUM_ORDERS_LESS_THAN_ZERO

  * Max num orders less than zero.
  * 最大订单量小于0



### -4013 PRICE_LESS_THAN_MIN_PRICE

  * Price less than min price.
  * 价格小于最小价格



### -4014 PRICE_NOT_INCREASED_BY_TICK_SIZE

  * Price not increased by tick size.
  * 价格增量不是价格精度的倍数。



### -4015 INVALID_CL_ORD_ID_LEN

  * Client order id is not valid.
  * 客户订单ID有误。
  * Client order id length should not be more than 36 chars
  * 客户订单ID长度应该不多于36字符



### -4016 PRICE_HIGHTER_THAN_MULTIPLIER_UP

  * Price is higher than mark price multiplier cap.



### -4017 MULTIPLIER_UP_LESS_THAN_ZERO

  * Multiplier up less than zero.
  * 价格上限小于0



### -4018 MULTIPLIER_DOWN_LESS_THAN_ZERO

  * Multiplier down less than zero.
  * 价格下限小于0



### -4019 COMPOSITE_SCALE_OVERFLOW

  * Composite scale too large.



### -4020 TARGET_STRATEGY_INVALID

  * Target strategy invalid for orderType '%s',reduceOnly '%b'.
  * 目标策略值不适合`%s`订单状态, 只减仓`%b`。



### -4021 INVALID_DEPTH_LIMIT

  * Invalid depth limit.
  * 深度信息的`limit`值不正确。
  * '%s' is not valid depth limit.
  * `%s`不是合理的深度信息的`limit`值。



### -4022 WRONG_MARKET_STATUS

  * market status sent is not valid.
  * 发送的市场状态不正确。



### -4023 QTY_NOT_INCREASED_BY_STEP_SIZE

  * Qty not increased by step size.
  * 数量的递增值不是步进值的倍数。



### -4024 PRICE_LOWER_THAN_MULTIPLIER_DOWN

  * Price is lower than mark price multiplier floor.



### -4025 MULTIPLIER_DECIMAL_LESS_THAN_ZERO

  * Multiplier decimal less than zero.



### -4026 COMMISSION_INVALID

  * Commission invalid.
  * 收益值不正确
  * `%s` less than zero.
  * `%s`少于0
  * `%s` absolute value greater than `%s`
  * `%s`绝对值大于`%s`



### -4027 INVALID_ACCOUNT_TYPE

  * Invalid account type.
  * 账户类型不正确。



### -4028 INVALID_LEVERAGE

  * Invalid leverage
  * 杠杆倍数不正确
  * Leverage `%s` is not valid
  * 杠杆`%s`不正确
  * Leverage `%s` already exist with `%s`
  * 杠杆`%s`已经存在于`%s`



### -4029 INVALID_TICK_SIZE_PRECISION

  * Tick size precision is invalid.
  * 价格精度小数点位数不正确。



### -4030 INVALID_STEP_SIZE_PRECISION

  * Step size precision is invalid.
  * 步进值小数点位数不正确。



### -4031 INVALID_WORKING_TYPE

  * Invalid parameter working type
  * 不正确的参数类型
  * Invalid parameter working type: `%s`
  * 不正确的参数类型: `%s`



### -4032 EXCEED_MAX_CANCEL_ORDER_SIZE

  * Exceed maximum cancel order size.
  * 超过可以取消的最大订单量。
  * Invalid parameter working type: `%s`
  * 不正确的参数类型: `%s`



### -4033 INSURANCE_ACCOUNT_NOT_FOUND

  * Insurance account not found.
  * 风险保障基金账号没找到。



### -4044 INVALID_BALANCE_TYPE

  * Balance Type is invalid.
  * 余额类型不正确。



### -4045 MAX_STOP_ORDER_EXCEEDED

  * Reach max stop order limit.
  * 达到止损单的上限。



### -4046 NO_NEED_TO_CHANGE_MARGIN_TYPE

  * No need to change margin type.
  * 不需要切换仓位模式。



### -4047 THERE_EXISTS_OPEN_ORDERS

  * Margin type cannot be changed if there exists open orders.
  * 如果有挂单，仓位模式不能切换。



### -4048 THERE_EXISTS_QUANTITY

  * Margin type cannot be changed if there exists position.
  * 如果有仓位，仓位模式不能切换。



### -4049 ADD_ISOLATED_MARGIN_REJECT

  * Add margin only support for isolated position.



### -4050 CROSS_BALANCE_INSUFFICIENT

  * Cross balance insufficient.
  * 全仓余额不足。



### -4051 ISOLATED_BALANCE_INSUFFICIENT

  * Isolated balance insufficient.
  * 逐仓余额不足。



### -4052 NO_NEED_TO_CHANGE_AUTO_ADD_MARGIN

  * No need to change auto add margin.



### -4053 AUTO_ADD_CROSSED_MARGIN_REJECT

  * Auto add margin only support for isolated position.
  * 自动增加保证金只适用于逐仓。



### -4054 ADD_ISOLATED_MARGIN_NO_POSITION_REJECT

  * Cannot add position margin: position is 0.
  * 不能增加逐仓保证金: 持仓为0



### -4055 AMOUNT_MUST_BE_POSITIVE

  * Amount must be positive.
  * 数量必须是正整数



### -4056 INVALID_API_KEY_TYPE

  * Invalid api key type.
  * API key的类型不正确



### -4057 INVALID_RSA_PUBLIC_KEY

  * Invalid api public key
  * API key不正确



### -4058 MAX_PRICE_TOO_LARGE

  * maxPrice and priceDecimal too large,please check.
  * maxPrice和priceDecimal太大，请检查。



### -4059 NO_NEED_TO_CHANGE_POSITION_SIDE

  * No need to change position side.
  * 无需变更仓位方向



### -4060 INVALID_POSITION_SIDE

  * Invalid position side.
  * 仓位方向不正确。



### -4061 POSITION_SIDE_NOT_MATCH

  * Order's position side does not match user's setting.
  * 订单的持仓方向和用户设置不一致。



### -4062 REDUCE_ONLY_CONFLICT

  * Invalid or improper reduceOnly value.
  * 仅减仓的设置不正确。



### -4063 INVALID_OPTIONS_REQUEST_TYPE

  * Invalid options request type
  * 无效的期权请求类型



### -4064 INVALID_OPTIONS_TIME_FRAME

  * Invalid options time frame
  * 无效的期权时间窗口



### -4065 INVALID_OPTIONS_AMOUNT

  * Invalid options amount
  * 无效的期权数量



### -4066 INVALID_OPTIONS_EVENT_TYPE

  * Invalid options event type
  * 无效的期权事件类型



### -4067 POSITION_SIDE_CHANGE_EXISTS_OPEN_ORDERS

  * Position side cannot be changed if there exists open orders.
  * 如果有挂单，无法修改仓位方向。



### -4068 POSITION_SIDE_CHANGE_EXISTS_QUANTITY

  * Position side cannot be changed if there exists position.
  * 如果有仓位, 无法修改仓位方向。



### -4069 INVALID_OPTIONS_PREMIUM_FEE

  * Invalid options premium fee
  * 无效的期权费



### -4070 INVALID_CL_OPTIONS_ID_LEN

  * Client options id is not valid.
  * 客户的期权ID不合法
  * Client options id length should be less than 32 chars
  * 客户的期权ID长度应该小于32个字符



### -4071 INVALID_OPTIONS_DIRECTION

  * Invalid options direction
  * 期权的方向无效



### -4072 OPTIONS_PREMIUM_NOT_UPDATE

  * premium fee is not updated, reject order
  * 期权费没有更新



### -4073 OPTIONS_PREMIUM_INPUT_LESS_THAN_ZERO

  * input premium fee is less than 0, reject order
  * 输入的期权费小于0



### -4074 OPTIONS_AMOUNT_BIGGER_THAN_UPPER

  * Order amount is bigger than upper boundary or less than 0, reject order



### -4075 OPTIONS_PREMIUM_OUTPUT_ZERO

  * output premium fee is less than 0, reject order



### -4076 OPTIONS_PREMIUM_TOO_DIFF

  * original fee is too much higher than last fee
  * 期权的费用比之前的费用高



### -4077 OPTIONS_PREMIUM_REACH_LIMIT

  * place order amount has reached to limit, reject order
  * 下单的数量达到上限



### -4078 OPTIONS_COMMON_ERROR

  * options internal error
  * 期权内部系统错误



### -4079 INVALID_OPTIONS_ID

  * invalid options id
  * invalid options id: %s
  * duplicate options id %d for user %d
  * 期权ID无效



### -4080 OPTIONS_USER_NOT_FOUND

  * user not found
  * user not found with id: %s
  * 用户找不到



### -4081 OPTIONS_NOT_FOUND

  * options not found
  * options not found with id: %s
  * 期权找不到



### -4082 INVALID_BATCH_PLACE_ORDER_SIZE

  * Invalid number of batch place orders.
  * Invalid number of batch place orders: %s
  * 批量下单的数量不正确



### -4083 PLACE_BATCH_ORDERS_FAIL

  * Fail to place batch orders.
  * 无法批量下单



### -4084 UPCOMING_METHOD

  * Method is not allowed currently. Upcoming soon.
  * 方法不支持



### -4085 INVALID_NOTIONAL_LIMIT_COEF

  * Invalid notional limit coefficient
  * 期权的有限系数不正确



### -4086 INVALID_PRICE_SPREAD_THRESHOLD

  * Invalid price spread threshold
  * 无效的价差阀值



### -4087 REDUCE_ONLY_ORDER_PERMISSION

  * User can only place reduce only order
  * 用户只能下仅减仓订单



### -4088 NO_PLACE_ORDER_PERMISSION

  * User can not place order currently
  * 用户当前不能下单



### -4104 INVALID_CONTRACT_TYPE

  * Invalid contract type
  * 无效的合约类型



### -4114 INVALID_CLIENT_TRAN_ID_LEN

  * clientTranId is not valid
  * clientTranId不正确
  * Client tran id length should be less than 64 chars
  * 客户的tranId长度应该小于64个字符



### -4115 DUPLICATED_CLIENT_TRAN_ID

  * clientTranId is duplicated
  * clientTranId重复
  * Client tran id should be unique within 7 days
  * 客户的tranId应在7天内唯一



### -4118 REDUCE_ONLY_MARGIN_CHECK_FAILED

  * ReduceOnly Order Failed. Please check your existing position and open orders
  * 仅减仓订单失败。请检查现有的持仓和挂单
  * 这表示新的「仅减仓（reduce-only）」订单与同方向的未成交订单叠加后，会形成反向持仓并导致保证金不足；请先取消该未成交订单后再重试



### -4131 MARKET_ORDER_REJECT

  * The counterparty's best price does not meet the PERCENT_PRICE filter limit
  * 交易对手的最高价格未达到PERCENT_PRICE过滤器限制



### -4135 INVALID_ACTIVATION_PRICE

  * Invalid activation price
  * 无效的激活价格



### -4137 QUANTITY_EXISTS_WITH_CLOSE_POSITION

  * Quantity must be zero with closePosition equals true
  * 数量必须为0，当closePosition为true时



### -4138 REDUCE_ONLY_MUST_BE_TRUE

  * Reduce only must be true with closePosition equals true
  * Reduce only 必须为true，当closePosition为true时



### -4139 ORDER_TYPE_CANNOT_BE_MKT

  * Order type can not be market if it's unable to cancel
  * 订单类型不能为市价单如果不能取消



### -4140 INVALID_OPENING_POSITION_STATUS

  * Invalid symbol status for opening position
  * 无效的交易对状态



### -4141 SYMBOL_ALREADY_CLOSED

  * Symbol is closed
  * 交易对已下架



### -4142 STRATEGY_INVALID_TRIGGER_PRICE

  * REJECT: take profit or stop order will be triggered immediately
  * 拒绝：止盈止损单将立即被触发



### -4144 INVALID_PAIR

  * Invalid pair
  * 无效的pair



### -4161 ISOLATED_LEVERAGE_REJECT_WITH_POSITION

  * Leverage reduction is not supported in Isolated Margin Mode with open positions
  * 逐仓仓位模式下无法降低杠杆



### -4164 MIN_NOTIONAL

  * Order's notional must be no smaller than 5.0 (unless you choose reduce only)
  * 订单的名义价值不可以小于5，除了使用reduce only
  * Order's notional must be no smaller than %s (unless you choose reduce only)
  * 订单的名义价值不可以小于`%s`，除了使用reduce only



### -4165 INVALID_TIME_INTERVAL

  * Invalid time interval
  * 无效的间隔
  * Maximum time interval is %s days
  * 最大的时间间隔为 `%s` 天



### -4183 PRICE_HIGHTER_THAN_STOP_MULTIPLIER_UP

  * Price is higher than stop price multiplier cap.
  * 止盈止损订单价格不应高于触发价与报价乘数上限的乘积
  * Limit price can't be higher than %s.
  * 止盈止损订单价格不应高于 `%s`



### -4184 PRICE_LOWER_THAN_STOP_MULTIPLIER_DOWN

  * Price is lower than stop price multiplier floor.
  * 止盈止损订单价格不应低于触发价与报价乘数下限的乘积
  * Limit price can't be lower than %s.
  * 止盈止损订单价格不应低于 `%s`f



### -4220 CANNOT_CHANGE_DUAL_SIDE

  * The operation is rejected because the CM dual-side is not allowed to be different from UM dual-side.
  * 操作被拒绝，CM的持仓模式不允许与UM的持仓模式不同。



### -4405 UM_REDUCE_ONLY_ONLY

  * Only reduceOnly order is allowed, please try again later.
  * 仅允许仅减仓订单，请稍后再试。



### -4407 ACCOUNT_REDUCE_ONLY

  * Restricted account permission: can only place reduceOnly order on the symbol.
  * 账户权限受限：该交易对仅允许下仅减仓订单。



### -4415 CM_REDUCE_ONLY_ONLY

  * Only reduceOnly order is allowed, please try again later.
  * 仅允许仅减仓订单，请稍后再试。



### -4517 SYMBOL_REDUCE_ONLY

  * Symbol is under position risk control, only reduce-only order is allowed.
  * 该交易对处于持仓风控状态，仅允许仅减仓订单。



### -4518 SYMBOL_REDUCE_ONLY_BUY

  * Symbol is under position risk control, buy order can only works with reduce-only.
  * 该交易对处于持仓风控状态，买单仅允许仅减仓。



### -4519 SYMBOL_REDUCE_ONLY_SELL

  * Symbol is under position risk control, sell order can only works with reduce-only.
  * 该交易对处于持仓风控状态，卖单仅允许仅减仓。



## 50xx/51xxx - Order Execution Issues

### -5021 FOK_ORDER_REJECT

  * 订单无法完全成交，FOK订单被拒绝



### -5022 GTX_ORDER_REJECT

  * 订单无法仅做maker单， Post Only订单被拒绝



### -5028 ME_RECVWINDOW_REJECT

  * 请求的时间戳在撮合的recvWindow之外



### -5041 TOO_MANY_REQUESTS_IN_QUEUE

  * 此帐户同时排队的请求订单过多而超时



### 51006 EXCEED_MAX_BORROWABLE

  * Your borrow amount has exceed maximum borrow amount.
  * 借款数量超过最大可借数量。



### 51007 HAS_PENDING_TRANSACTION

  * You have pending borrow or repayment, please try again later.
  * 您有待处理的借贷或还款，请稍后再试。



### 51013 EMPTY_ASSET_ADMIN

  * Not a valid margin asset.
  * 不是有效的杠杆资产。



### 51014 ASSET_ADMIN_BAN_BORROW

  * This asset is currently not available for borrowing.
  * 该资产目前不可借。



### 51017 REPAY_EXCEED_LIABILITY

  * Repay amount exceeds borrow amount.
  * 还款数量超过借款数量。



### 51018 LT_MIN_REPAY

  * Repay amount less than minimum repay amount.
  * 还款数量小于最小还款数量。



### 51022 EXCEED_MAX_ROLLOUT

  * Transfer out amount exceeds max amount.
  * 转出数量超过最大可转出数量。



### 51026 INVALID_INPUT_PARAM

  * Invalid input parameter.
  * 输入参数不合法。



### 51038 LISTEN_KEY_NOT_FOUND

  * Listen key not found.
  * 未找到 listenKey。



### 51042 FREQUENT_OPERATION

  * Operation performed too frequently.
  * 操作过于频繁，请稍后重试。



### 51061 BORROW_BALANCE_NOT_CLEARED_AND_ASSET

  * The platform's lendable token is temporarily insufficient. Please try again later.
  * 平台可借币暂时不足，请稍后重试。



### 51068 LIQUIDATION_IN_PROGRESS

  * Unable to trade. Your margin account is currently in liquidation. Please try again once liquidation is processed.
  * 无法交易。您的保证金账户正在清算中，请在清算完成后重试。



### 51078 NET_ASSET_MUST_LTE_RATIO

  * Fail to retrieve margin assets.
  * margin资产更新失败



### 51113 TRADE_NOT_ALLOWED_LOSS_LIMIT

  * The limit price needs to be within (`{range}`) of current index price for this margin trading pair.
  * For OTO/OTOCO order types, the trigger price of the secondary order must be within (`{range}`) of primary order price. This rule applies to sell at a lower limit price and buy at a higher limit price.
  * 限价需在该杠杆交易对当前指数价格的范围内。OTO/OTOCO 订单的从单触发价需在主单价格的范围内。该规则仅限制低于指数价的卖单和高于指数价的买单。



### 51122 PM_FUNCTION_NOT_SUPPORTED

  * Portfolio Margin account users cannot use this function.
  * 统一账户用户无法使用此功能。



### 51169 PLATFORM_MAX_TRANSFER_IN_EXCEEDED

  * The amount of token exceeds the platform limit. You can transfer in or buy at most `{num}`.
  * 转入币的数量超过平台限额，最多可转入或买入 `{num}`。



### 51238 BSTOCK_TRADE_NOT_ELIGIBLE

  * bStocks related margin features are currently unavailable. Please complete the Suitability Assessment Questionnaire first.
  * bStocks 相关杠杆功能当前不可用，请先完成适当性评估问卷。



### 51998 SYSTEM_BUSY

  * System is busy. Please try again later.
  * 系统繁忙，请稍后再试。



### 51999 UNKNOWN

  * System abnormality.
  * 系统异常。
  * An unknown error occurred while processing the request.
  * 处理请求时发生未知错误。



### 331020 INSUFFICIENT_SPOT_AVAILABLE_BALANCE

  * The available spot balance is insufficient for this transfer.
  * 现货可用余额不足，无法划转。



此页面是否有帮助？

Last modified on November 12, 2026

[账户信息流](/zh-CN/docs/products/derivatives-trading-portfolio-margin/user-data-streams)[公开API参数](/zh-CN/docs/products/derivatives-trading-portfolio-margin/common-definition)