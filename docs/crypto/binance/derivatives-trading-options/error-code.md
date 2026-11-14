---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/derivatives-trading-options/error-code
api_type: REST
updated_at: 2026-11-13 20:27:57.327456
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

  * An unknown error occurred while processing the request.



### -1001 DISCONNECTED

  * Internal error; unable to process your request. Please try again.



### -1002 UNAUTHORIZED

  * You are not authorized to execute this request.



### -1008 TOO_MANY_REQUESTS

  * Too many requests queued.
  * Too much request weight used; please use the websocket for live updates to avoid polling the API.
  * Too much request weight used; current limit is %s request weight per %s %s. Please use the websocket for live updates to avoid polling the API.
  * Way too much request weight used; IP banned until %s. Please use the websocket for live updates to avoid bans.



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



## 11xx - 2xxx Request issues

### -1100 ILLEGAL_CHARS

  * Illegal characters found in a parameter.
  * Illegal characters found in a parameter. %s
  * Illegal characters found in parameter `%s`; legal range is `%s`.



### -1101 TOO_MANY_PARAMETERS

  * Too many parameters sent for this endpoint.
  * Too many parameters; expected `%s` and received `%s`.
  * Duplicate values for a parameter detected.



### -1102 MANDATORY_PARAM_EMPTY_OR_MALFORMED

  * A mandatory parameter was not sent, was empty/null, or malformed.
  * Mandatory parameter `%s` was not sent, was empty/null, or malformed.
  * Param `%s` or `%s` must be sent, but both were empty/null!



### -1103 UNKNOWN_PARAM

  * An unknown parameter was sent.



### -1104 UNREAD_PARAMETERS

  * Not all sent parameters were read.
  * Not all sent parameters were read; read `%s` parameter(s) but was sent `%s`.



### -1105 PARAM_EMPTY

  * A parameter was empty.
  * Parameter `%s` was empty.



### -1106 PARAM_NOT_REQUIRED

  * A parameter was sent when not required.
  * Parameter `%s` sent when not required.



### -1111 BAD_PRECISION

  * Precision is over the maximum defined for this asset.



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

  * This listenKey does not exist.



### -1127 MORE_THAN_XX_HOURS

  * Lookup interval is too big.
  * More than %s hours between startTime and endTime.



### -1128 BAD_CONTRACT

  * Invalid underlying



### -1129 BAD_CURRENCY

  * Invalid asset。



### -1130 INVALID_PARAMETER

  * Invalid data sent for a parameter.
  * Data sent for paramter `%s` is not valid.



### -1131 BAD_RECV_WINDOW

  * recvWindow must be less than 60000



### -2010 NEW_ORDER_REJECTED

  * NEW_ORDER_REJECTED



### -2013 NO_SUCH_ORDER

  * Order does not exist.



### -2014 BAD_API_KEY_FMT

  * API-key format invalid.



### -2015 INVALID_API_KEY

  * Invalid API-key, IP, or permissions for action.



### -2018 BALANCE_NOT_SUFFICIENT

  * Balance is insufficient.



### -2027 OPTION_MARGIN_NOT_SUFFICIENT

  * Option margin is insufficient.



## 3xxx-5xxx Filters and other issues

### -3029 TRANSFER_FAILED

  * Asset transfer fail.



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



### -4013 PRICE_LESS_THAN_MIN_PRICE

  * Price less than min price.



### -4029 INVALID_TICK_SIZE_PRECISION

  * Tick size precision is invalid.



### -4030 INVALID_QTY_PRECISION

  * Step size precision is invalid.



### -4055 AMOUNT_MUST_BE_POSITIVE

  * Amount must be positive.



### -4056 INVALID_AMOUNT

  * Amount is invalid.



### -4078 OPTIONS_COMMON_ERROR

  * options internal error



### -5001 USER_EXIST

  * Option user already exist



### -5002 USER_NOT_ACCESS

  * Option user not access



### -5003 BAD_INVITE_CODE

  * Invalid invite code



### -5004 USED_INVITE_CODE

  * Invite code has bean used



### -5005 BLACK_COUNTRY

  * Black country



### -5006 ITEMS_EXIST

  * Items '%s' already exist



### -5007 USER_API_EXIST

  * User api already exist



### -5008 KYC_NOT_PASS

  * User kyc not pass



### -5009 IP_COUNTRY_BLACK

  * Restricted jurisdiction ip address



### -5010 NOT_ENOUGH_POSITION

  * User doesn't have enough position to sell



### -6001 INVALID_MMP_WINDOW_TIME_LIMIT

  * Invalid mmp window time limit



### -6002 INVALID_MMP_FROZEN_TIME_LIMIT

  * Invalid mmp frozen time limit



### -6003 INVALID_UNDERLYING

  * Invalid underlying



### -6004 MMP_UNDERLYING_NOT_FOUND

  * Underlying not found



### -6005 IS_NOT_MARKET_MAKER

  * It is not market maker



### -6006 MMP_RULES_NOT_EXISTING

  * Mmp rules are not existing



### -6007 MMP_ERROR_UNKNOWN

  * Mmp unknown error



### -6008 INVALID_LIMIT

  * parameter 'limit' is invalid.



### -6009 INVALID_COUNTDOWN_TIME

  * countdownTime must be no less than 5000 or equal to 0



### -6010 OPEN_INTEREST_ERR_DATA

  * open interest error data.



### -6011 EXCEED_MAXIMUM_BATCH_ORDERS

  * Maximum 10 orders in one batchOrder request.



### -6012 EXCEED_MAXIMUM_BLOCK_ORDER_LEGS

  * Exceed maximum number of legs in one block order request.



### -6013 BLOCK_ORDER_LEGS_WITH_DUPLICATE_SYMBOL

  * Duplicate symbol in one block order request.



### -6014 GRFQ_INVALID_LEGS

  * Invalid legs



### -6015 GRFQ_QTY_IS_NOT_MULTIPLE_OF_MINIMUM_QTY

  * Quantity is not multiple of minimum quantity



### -6016 GRFQ_QUOTE_NOT_FOUND

  * Quote is not found



### -6017 GRFQ_QUOTE_NOT_ENOUGH_QTY_LEFT

  * Not enough quantity left



### -6018 GRFQ_QUOTE_REQUEST_NOT_FOUND

  * Quote request is not found



### -6019 GRFQ_QUOTE_INVALID_EXPIRE_TIME

  * Invalid quote expire time



### -6020 GRFQ_QUOTE_EXPIRED

  * Quote expired



### -6021 GRFQ_INVALID_SIDE

  * Invalid side



### -6022 GRFQ_INVALID_USER

  * Not Global RFQ user



### -6023 SELF_TRADE_PREVENTION

  * Self trade prevention



### -6024 CHANGE_USER_FLAG_FAILED

  * Change user flag failed



### -6025 GRFQ_INVALID_QUOTE_PRICE

  * Invalid quote price



### -6026 INVALID_QTY

  * Invalid qty



### -6027 INVALID_PRICE

  * Invalid price



### -6028 ORDER_IS_FINAL

  * Order is in final state



### -6029 PARAMETER_IS_REQUIRED

  * %s is required



### -6030 INVALID_TIME_INTERVAL

  * Invalid time interval.



### -6031 START_TIME_GREATER_THAN_END_TIME

  * Start time is greater than end time.



### -6032 HAS_OPEN_ORDER

  * Has open order.



### -6033 HAS_NEGATIVE_BALANCE

  * Has negative balance.



### -6034 HAS_POSITION

  * Has position.



### -6035 NO_NEED_TO_CHANGE

  * No need to change.



### -6036 NO_PERMISSION_TO_CHANGE

  * no permission to change.



### -6037 NO_RECORDS_FOUND

  * No records found.



### -6038 SCALE_NOT_MATCH

  * scale not match.



### -6039 INVALID_STEP_SIZE_PRECISION

  * Step size precision is invalid.



### -6040 INVALID_QTYLIMIT_DELTALIMIT

  * Invalid qtyLimit or deltaLimit.



### -6041 START_TRADING_MUST_SLOWLY

  * Start Trading Must Slowly..



### -6042 INDEX_COMMISSION_NOT_MATCH

  * Index Commission Not Match..



### -6043 INDEX_RISKPARAMETER_NOT_MATCH

  * Index RiskParameter Not Match..



### -6044 CLI_ORD_ID_ERROR

  * clientOrderId is duplicated



### -6045 REDUCE_ONLY_REJECT

  * Reduce-only order rejected. The new reduce-only order conflicts with existing open orders. Please cancel the conflicting orders and resubmit.



### -6046 FOK_ORDER_REJECT

  * Due to the order could not be filled immediately, the FOK order has been rejected.



### -6047 GTX_ORDER_REJECT

  * Due to the order could not be executed as maker, the Post Only order will be rejected.



### -6048 INVALID_BLOCK_ORDER

  * Block order parameter is invalid



### -6049 SYMBOL_NOT_TRADING

  * this symbol is not in trading status



### -6050 MAX_OPEN_ORDERS_ON_SYMBOL_EXCEEDED

  * Maximum open orders reached for this symbol. Please cancel existing orders and try again.



### -6051 MAX_OPEN_ORDERS_ON_INDEX_EXCEEDED

  * Maximum open orders reached for this underlying. Please cancel existing orders and try again.



### -6052 MAX_SHORT_POSITION_ON_SYMBOL_EXCEEDED

  * Maximum short position size reached for this symbol



### -6053 MAX_SHORT_POSITION_ON_INDEX_EXCEEDED

  * Maximum short position size reached for this underlying



### -6054 MAX_QUANTITY_ON_SINGLE_ORDER_EXCEEDED

  * Quantity greater than max quantity



### -6055 USER_LIQUIDATING

  * User is in liquidation process



### -6056 REDUCE_ONLY_MARGIN_CHECK_FAILED

  * Reduce-only order failed. Your new reduce-only order, when combined with existing same-side open orders, would flip your position and cause insufficient margin. Please cancel those open orders and try again.



### -6057 WRITER_CANT_NAKED_SELL

  * The current symbol is not eligible for option writing.



### -6058 MMP_TRIGGERED

  * MMP triggered. Please reset MMP config



### -6059 USER_IN_LIQUIDATION

  * User is in liquidation process



### -6060 LOCKED_BALANCE_NOT_FOUND

  * OTC order fail due to unable to lock balance



### -6061 LOCKED_OTC_ORDER_NOT_FOUNT

  * OTC order fail due to unable to lock order



### -6062 INVALID_USER_STATUS

  * Operation is not supported for current user status



### -6063 CANCEL_REJECTED

  * Cancel rejected by system



### -6073 SEARCH_WINDOW_RESTRICTED

  * Search window is restricted to recent 90 days only.



Was this page helpful?

Last modified on November 12, 2026

[Public Endpoints Info](/en/docs/products/derivatives-trading-options/common-definition)[Connect](/en/docs/products/derivatives-trading-options/websocket-market-streams/Connect)

---

# 错误代码

> error JSON payload:
    
    
    Code
    
    {
      "code":-1121,
      "msg":"Invalid symbol."
    }

错误由两部分组成：错误代码和消息。 代码是通用的，但是消息可能会有所不同。

## 10xx -常规服务器或网络问题

### -1000 UNKNOWN

  * 处理请求时发生未知错误。



### -1001 DISCONNECTED

  * 内部错误; 无法处理您的请求。 请再试一次.



### -1002 UNAUTHORIZED

  * 您无权执行此请求。



### -1008 TOO_MANY_REQUESTS

  * 排队的请求过多。
  * 请求权重过多； 请使用websocket获取实时更新。
  * 请求权重过多； 当前限制为每分钟％s请求权重。 请使用websocket进行实时更新，以避免轮询API。
  * 请求权重过多； IP被禁止，直到％s。 请使用websocket进行实时更新，以免被禁。



### -1014 UNKNOWN_ORDER_COMPOSITION

  * 不支持的订单组合。



### -1015 TOO_MANY_ORDERS

  * 新订单太多。
  * 新订单太多； 当前限制为每％s ％s个订单。



### -1016 SERVICE_SHUTTING_DOWN

  * 该服务不可用。



### -1020 UNSUPPORTED_OPERATION

  * 不支持此操作。



### -1021 INVALID_TIMESTAMP

  * 此请求的时间戳在recvWindow之外。
  * 此请求的时间戳比服务器时间提前1000毫秒。



### -1022 INVALID_SIGNATURE

  * 此请求的签名无效。



## 11xx - 2xxx Request issues

### -1100 ILLEGAL_CHARS

  * 在参数中发现非法字符。
  * 在参数中发现非法字符。`％s`
  * 在参数`％s`中发现非法字符； 合法范围是`％s`。



### -1101 TOO_MANY_PARAMETERS

  * 为此端点发送的参数太多。
  * 参数太多； 预期为`％s`并收到了`％s`。
  * 检测到的参数值重复。



### -1102 MANDATORY_PARAM_EMPTY_OR_MALFORMED

  * 未发送强制性参数，该参数为空/空或格式错误。
  * 强制参数`％s`未发送，为空/空或格式错误。
  * 必须发送参数`％s`或`％s`，但两者均为空！



### -1103 UNKNOWN_PARAM

  * 发送了未知参数。



### -1104 UNREAD_PARAMETERS

  * 并非所有发送的参数都被读取。
  * 并非所有发送的参数都被读取； 读取了`％s`参数，但被发送了`％s`。



### -1105 PARAM_EMPTY

  * 参数为空。
  * 参数`％s`为空。



### -1106 PARAM_NOT_REQUIRED

  * 不需要时已发送参数。
  * 不需要时发送参数`％s`。



### -1111 BAD_PRECISION

  * 精度超过为此资产定义的最大值。



### -1115 INVALID_TIF

  * 无效 timeInForce.



### -1116 INVALID_ORDER_TYPE

  * 无效订单类型。



### -1117 INVALID_SIDE

  * 无效买卖方向。



### -1118 EMPTY_NEW_CL_ORD_ID

  * 新的客户订单ID为空。



### -1119 EMPTY_ORG_CL_ORD_ID

  * 客户自定义的订单ID为空。



### -1120 BAD_INTERVAL

  * 无效时间间隔。



### -1121 BAD_SYMBOL

  * 无效的交易对。



### -1125 INVALID_LISTEN_KEY

  * 该listenKey不存在。



### -1127 MORE_THAN_XX_HOURS

  * 查询间隔太大。
  * 从开始时间到结束时间之间超过％s小时。



### -1128 BAD_CONTRACT

  * 无效的期权合约标的。



### -1129 BAD_CURRENCY

  * 无效的资产类型。



### -1130 INVALID_PARAMETER

  * 发送的参数为无效数据。
  * 发送参数`％s`的数据无效。



### -1131 BAD_RECV_WINDOW

  * `recvWindow` 必须小于 60000



### -2010 NEW_ORDER_REJECTED

  * 新订单被拒绝



### -2013 NO_SUCH_ORDER

  * 订单不存在。



### -2014 BAD_API_KEY_FMT

  * API-key 格式无效。



### -2015 INVALID_API_KEY

  * 无效的API密钥，IP或操作权限。



### -2018 BALANCE_NOT_SUFFICIENT

  * 余额不足。



### -2027 OPTION_MARGIN_NOT_SUFFICIENT

  * 期权可用余额不足。



## 3xxx-5xxx Filters and other issues

### -3029 TRANSFER_FAILED

  * 资金划转失败。



### -4001 PRICE_LESS_THAN_ZERO

  * 价格小于0。



### -4002 PRICE_GREATER_THAN_MAX_PRICE

  * 价格超过最大值。



### -4003 QTY_LESS_THAN_ZERO

  * 数量小于0。



### -4004 QTY_LESS_THAN_MIN_QTY

  * 数量小于最小值。



### -4005 QTY_GREATER_THAN_MAX_QTY

  * 数量大于最大值。



### -4013 PRICE_LESS_THAN_MIN_PRICE

  * 价格小于最小价格。



### -4029 INVALID_TICK_SIZE_PRECISION

  * 价格精度小数点位数不正确。



### -4030 INVALID_QTY_PRECISION

  * 数量精度小数点位数不正确。



### -4055 AMOUNT_MUST_BE_POSITIVE

  * 金额必须大于零。



### -4056 INVALID_AMOUNT

  * 金额无效。



### -4078 OPTIONS_COMMON_ERROR

  * 期权内部错误。



### -5001 USER_EXIST

  * Option 用户已存在。



### -5002 USER_NOT_ACCESS

  * Option 用户无权限访问。



### -5003 BAD_INVITE_CODE

  * 邀请码无效。



### -5004 USED_INVITE_CODE

  * 邀请码已被使用。



### -5005 BLACK_COUNTRY

  * 黑名单国家/地区限制。



### -5006 ITEMS_EXIST

  * 项目 '%s' 已存在。



### -5007 USER_API_EXIST

  * 用户 API 已存在。



### -5008 KYC_NOT_PASS

  * 用户 KYC 未通过。



### -5009 IP_COUNTRY_BLACK

  * 所在 IP 属于受限司法辖区。



### -5010 NOT_ENOUGH_POSITION

  * 用户没有足够的仓位卖出。



### -6001 INVALID_MMP_WINDOW_TIME_LIMIT

  * MMP 窗口时间限制无效。



### -6002 INVALID_MMP_FROZEN_TIME_LIMIT

  * MMP 冻结时间限制无效。



### -6003 INVALID_UNDERLYING

  * 标的物无效。



### -6004 MMP_UNDERLYING_NOT_FOUND

  * 未找到标的物。



### -6005 IS_NOT_MARKET_MAKER

  * 该用户不是做市商。



### -6006 MMP_RULES_NOT_EXISTING

  * MMP 规则不存在。



### -6007 MMP_ERROR_UNKNOWN

  * MMP 未知错误。



### -6008 INVALID_LIMIT

  * 参数 'limit' 无效。



### -6009 INVALID_COUNTDOWN_TIME

  * countdownTime 必须大于等于 5000 或等于 0。



### -6010 OPEN_INTEREST_ERR_DATA

  * 持仓量数据异常。



### -6011 EXCEED_MAXIMUM_BATCH_ORDERS

  * 每次 batchOrder 最多允许下 10 单。



### -6012 EXCEED_MAXIMUM_BLOCK_ORDER_LEGS

  * Block order 的腿数超过最大限制。



### -6013 BLOCK_ORDER_LEGS_WITH_DUPLICATE_SYMBOL

  * Block order 中包含重复的 symbol。



### -6014 GRFQ_INVALID_LEGS

  * Legs 参数无效。



### -6015 GRFQ_QTY_IS_NOT_MULTIPLE_OF_MINIMUM_QTY

  * 数量不是最小数量的整数倍。



### -6016 GRFQ_QUOTE_NOT_FOUND

  * 报价未找到。



### -6017 GRFQ_QUOTE_NOT_ENOUGH_QTY_LEFT

  * 剩余数量不足。



### -6018 GRFQ_QUOTE_REQUEST_NOT_FOUND

  * 报价请求未找到。



### -6019 GRFQ_QUOTE_INVALID_EXPIRE_TIME

  * 报价过期时间无效。



### -6020 GRFQ_QUOTE_EXPIRED

  * 报价已过期。



### -6021 GRFQ_INVALID_SIDE

  * Side 参数无效。



### -6022 GRFQ_INVALID_USER

  * 非 Global RFQ 用户。



### -6023 SELF_TRADE_PREVENTION

  * 触发自成交保护。



### -6024 CHANGE_USER_FLAG_FAILED

  * 修改用户标志失败。



### -6025 GRFQ_INVALID_QUOTE_PRICE

  * 报价价格无效。



### -6026 INVALID_QTY

  * 数量无效。



### -6027 INVALID_PRICE

  * 价格无效。



### -6028 ORDER_IS_FINAL

  * 订单已经处于最终状态。



### -6029 PARAMETER_IS_REQUIRED

  * %s 为必填参数。



### -6030 INVALID_TIME_INTERVAL

  * 时间区间无效。



### -6031 START_TIME_GREATER_THAN_END_TIME

  * 开始时间大于结束时间。



### -6032 HAS_OPEN_ORDER

  * 存在未完成订单。



### -6033 HAS_NEGATIVE_BALANCE

  * 存在负余额。



### -6034 HAS_POSITION

  * 用户存在持仓。



### -6035 NO_NEED_TO_CHANGE

  * 无需变更。



### -6036 NO_PERMISSION_TO_CHANGE

  * 无权限变更。



### -6037 NO_RECORDS_FOUND

  * 未找到记录。



### -6038 SCALE_NOT_MATCH

  * 精度不匹配。



### -6039 INVALID_STEP_SIZE_PRECISION

  * 步长精度无效。



### -6040 INVALID_QTYLIMIT_DELTALIMIT

  * qtyLimit 或 deltaLimit 无效。



### -6041 START_TRADING_MUST_SLOWLY

  * 开始交易需逐步进行。



### -6042 INDEX_COMMISSION_NOT_MATCH

  * 指数手续费不匹配。



### -6043 INDEX_RISKPARAMETER_NOT_MATCH

  * 指数风险参数不匹配。



### -6044 CLI_ORD_ID_ERROR

  * clientOrderId 已被使用。



### -6045 REDUCE_ONLY_REJECT

  * Reduce-Only 订单被拒绝。新的 Reduce-Only 订单与现有同向挂单冲突。请取消冲突订单后重试。



### -6046 FOK_ORDER_REJECT

  * 因无法立即完全成交，FOK 订单被拒绝。



### -6047 GTX_ORDER_REJECT

  * 因无法作为 maker 执行，Post Only（GTX）订单被拒绝。



### -6048 INVALID_BLOCK_ORDER

  * Block order 参数无效。



### -6049 SYMBOL_NOT_TRADING

  * 当前交易对不在交易状态。



### -6050 MAX_OPEN_ORDERS_ON_SYMBOL_EXCEEDED

  * 当前交易对已达最大挂单数量，请取消部分订单后重试。



### -6051 MAX_OPEN_ORDERS_ON_INDEX_EXCEEDED

  * 当前标的已达最大挂单数量，请取消部分订单后重试。



### -6052 MAX_SHORT_POSITION_ON_SYMBOL_EXCEEDED

  * 当前交易对的最大可开空头仓位已达到上限。



### -6053 MAX_SHORT_POSITION_ON_INDEX_EXCEEDED

  * 当前标的的最大可开空头仓位已达到上限。



### -6054 MAX_QUANTITY_ON_SINGLE_ORDER_EXCEEDED

  * 下单数量超过最大限制。



### -6055 USER_LIQUIDATING

  * 用户正在爆仓处理中。



### -6056 REDUCE_ONLY_MARGIN_CHECK_FAILED

  * Reduce-Only 下单失败。新下单与现有同方向挂单叠加会导致反向持仓并造成保证金不足，请取消相关挂单后重试。



### -6057 WRITER_CANT_NAKED_SELL

  * 当前交易对不支持裸卖（Option Writing）。



### -6058 MMP_TRIGGERED

  * MMP 已触发，请重置 MMP 配置。



### -6059 USER_IN_LIQUIDATION

  * 用户正在爆仓处理中。



### -6060 LOCKED_BALANCE_NOT_FOUND

  * OTC 下单失败：无法锁定余额。



### -6061 LOCKED_OTC_ORDER_NOT_FOUNT

  * OTC 下单失败：无法锁定订单。



### -6062 INVALID_USER_STATUS

  * 当前用户状态不支持此操作。



### -6063 CANCEL_REJECTED

  * 系统拒绝取消订单。



### -6073 SEARCH_WINDOW_RESTRICTED

  * 查询时间范围仅限最近90天。



此页面是否有帮助？

Last modified on November 12, 2026

[公开API参数](/zh-CN/docs/products/derivatives-trading-options/common-definition)[连接](/zh-CN/docs/products/derivatives-trading-options/websocket-market-streams/Connect)