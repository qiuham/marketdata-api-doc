---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/stocks/error-code
api_type: Guide
updated_at: 2026-11-27 18:29:06.784262
---

# Error Code

Errors on Stocks Trading endpoints come from two layers, and **the pre-check layer takes
precedence**:

1. **Pre-check — standard SAPI errors** (`10xx` / `11xx–2xxx` / `3xxx–5xxx`, negative codes). SAPI
   validates signature, timestamp, parameters and format **before** the request reaches the equity
   service. If any of these fail you receive the SAPI code (e.g. `-1102`), **not** a `486xxx`.
2. **Post-check — module business errors** (`486xxx`, positive codes). Returned only after the
   request passes pre-check and then violates an equity business rule.

All errors use the standard SAPI error envelope: the code is in the `code` field and a
human-readable message in `msg`.

## 10xx - General Server or Network issues

### -1000 UNKNOWN

- An unknown error occurred while processing the request.
- An unknown error occurred while processing the request.[%s]

### -1001 DISCONNECTED

- Internal error; unable to process your request. Please try again.

### -1002 UNAUTHORIZED

- You are not authorized to execute this request.

### -1003 TOO_MANY_REQUESTS

- Too many requests queued.
- Too much request weight used; current limit is %s request weight per %s. Please use WebSocket
  Streams for live updates to avoid polling the API.
- Way too much request weight used; IP banned until %s. Please use WebSocket Streams for live
  updates to avoid bans.

### -1004 SERVER_BUSY

- Server is busy, please wait and try again

### -1006 UNEXPECTED_RESP

- An unexpected response was received from the message bus. Execution status unknown.

### -1007 TIMEOUT

- Timeout waiting for response from backend server. Send status unknown; execution status unknown.

### -1008 SERVER_BUSY

- Spot server is currently overloaded with other requests. Please try again in a few minutes.

### -1014 UNKNOWN_ORDER_COMPOSITION

- Unsupported order combination.

### -1015 TOO_MANY_ORDERS

- Too many new orders.
- Too many new orders; current limit is %s orders per %s.

### -1016 SERVICE_SHUTTING_DOWN

- This service is no longer available.

### -1020 UNSUPPORTED_OPERATION

- This operation is not supported.

### -1021 INVALID_TIMESTAMP

- Timestamp for this request is outside of the recvWindow.
- Timestamp for this request was 1000ms ahead of the server's time.

### -1022 INVALID_SIGNATURE

- Signature for this request is not valid.

### -1099 Not found, authenticated, or authorized

- This replaces error code -1999

## 11xx - 2xxx Request issues

### -1100 ILLEGAL_CHARS

- Illegal characters found in a parameter.
- Illegal characters found in a parameter. %s
- Illegal characters found in parameter `%s`; legal range is `%s`.

### -1101 TOO_MANY_PARAMETERS

- Too many parameters sent for this endpoint.
- Too many parameters; expected `%s` and received `%s`.
- Duplicate values for a parameter detected.

### -1102 MANDATORY_PARAM_EMPTY_OR_MALFORMED

- A mandatory parameter was not sent, was empty/null, or malformed.
- Mandatory parameter `%s` was not sent, was empty/null, or malformed.
- Param `%s` or `%s` must be sent, but both were empty/null!

> Standard SAPI codes (`10xx`–`5xxx`) mirror the SPOT API. For the authoritative, always-current
> message list, see the
> [SPOT API error reference](https://developers.binance.com/en/docs/products/spot/errors#-1102-mandatory_param_empty_or_malformed).

### -1103 UNKNOWN_PARAM

- An unknown parameter was sent.

### -1104 UNREAD_PARAMETERS

- Not all sent parameters were read.
- Not all sent parameters were read; read `%s` parameter(s) but was sent `%s`.

### -1105 PARAM_EMPTY

- A parameter was empty.
- Parameter `%s` was empty.

### -1106 PARAM_NOT_REQUIRED

- A parameter was sent when not required.
- Parameter `%s` sent when not required.

### -1111 BAD_PRECISION

- Precision is over the maximum defined for this asset.

### -1112 NO_DEPTH

- No orders on book for symbol.

### -1114 TIF_NOT_REQUIRED

- TimeInForce parameter sent when not required.

### -1115 INVALID_TIF

- Invalid timeInForce.

### -1116 INVALID_ORDER_TYPE

- Invalid orderType.

### -1117 INVALID_SIDE

- Invalid side.

### -1118 EMPTY_NEW_CL_ORD_ID

- New client order ID was empty.

### -1119 EMPTY_ORG_CL_ORD_ID

- Original client order ID was empty.

### -1120 BAD_INTERVAL

- Invalid interval.

### -1121 BAD_SYMBOL

- Invalid symbol.

### -1125 INVALID_LISTEN_KEY

- This listenKey does not exist.

### -1127 MORE_THAN_XX_HOURS

- Lookup interval is too big.
- More than %s hours between startTime and endTime.

### -1128 OPTIONAL_PARAMS_BAD_COMBO

- Combination of optional parameters invalid.

### -1130 INVALID_PARAMETER

- Invalid data sent for a parameter.
- Data sent for parameter `%s` is not valid.

### -1131 BAD_RECV_WINDOW

- recvWindow must be less than 60000

### -1134 BAD_STRATEGY_TYPE

- `strategyType` was less than 1000000.

#### -1145 INVALID_CANCEL_RESTRICTIONS

- `cancelRestrictions` has to be either `ONLY_NEW` or `ONLY_PARTIALLY_FILLED`.

#### -1151 DUPLICATE_SYMBOLS

- Symbol is present multiple times in the list.

### -2010 NEW_ORDER_REJECTED

- NEW_ORDER_REJECTED

### -2011 CANCEL_REJECTED

- CANCEL_REJECTED

### -2013 NO_SUCH_ORDER

- Order does not exist.

### -2014 BAD_API_KEY_FMT

- API-key format invalid.

### -2015 REJECTED_MBX_KEY

- Invalid API-key, IP, or permissions for action.

### -2016 NO_TRADING_WINDOW

- No trading window could be found for the symbol. Try ticker/24hrs instead.

#### -2026 ORDER_ARCHIVED

- Order was canceled or expired with no executed qty over 90 days ago and has been archived.

## 3xxx-5xxx SAPI-specific issues

### -3000 INNER_FAILURE

- Internal server error.

### -3001 NEED_ENABLE_2FA

- Please enable 2FA first.

### -3002 ASSET_DEFICIENCY

- We don't have this asset.

### -3003 NO_OPENED_MARGIN_ACCOUNT

- Margin account does not exist.

### -3004 TRADE_NOT_ALLOWED

- Trade not allowed.

### -3005 TRANSFER_OUT_NOT_ALLOWED

- Transferring out not allowed.

### -3006 EXCEED_MAX_BORROWABLE

- Your borrow amount has exceed maximum borrow amount.

### -3007 HAS_PENDING_TRANSACTION

- You have pending transaction, please try again later.

### -3008 BORROW_NOT_ALLOWED

- Borrow not allowed.

### -3009 ASSET_NOT_MORTGAGEABLE

- This asset are not allowed to transfer into margin account currently.

### -3010 REPAY_NOT_ALLOWED

- Repay not allowed.

### -3011 BAD_DATE_RANGE

- Your input date is invalid.

### -3012 ASSET_ADMIN_BAN_BORROW

- Borrow is banned for this asset.

### -3013 LT_MIN_BORROWABLE

- Borrow amount less than minimum borrow amount.

### -3014 ACCOUNT_BAN_BORROW

- Borrow is banned for this account.

### -3015 REPAY_EXCEED_LIABILITY

- Repay amount exceeds borrow amount.

### -3016 LT_MIN_REPAY

- Repay amount less than minimum repay amount.

### -3017 ASSET_ADMIN_BAN_MORTGAGE

- This asset are not allowed to transfer into margin account currently.

### -3018 ACCOUNT_BAN_MORTGAGE

- Transferring in has been banned for this account.

### -3019 ACCOUNT_BAN_ROLLOUT

- Transferring out has been banned for this account.

### -3020 EXCEED_MAX_ROLLOUT

- Transfer out amount exceeds max amount.

### -3021 PAIR_ADMIN_BAN_TRADE

- Margin account are not allowed to trade this trading pair.

### -3022 ACCOUNT_BAN_TRADE

- You account's trading is banned.

### -3023 WARNING_MARGIN_LEVEL

- You can't transfer out/place order under current margin level.

### -3024 FEW_LIABILITY_LEFT

- The unpaid debt is too small after this repayment.

### -3025 INVALID_EFFECTIVE_TIME

- Your input date is invalid.

### -3026 VALIDATION_FAILED

- Your input param is invalid.

### -3027 NOT_VALID_MARGIN_ASSET

- Not a valid margin asset.

### -3028 NOT_VALID_MARGIN_PAIR

- Not a valid margin pair.

### -3029 TRANSFER_FAILED

- Transfer failed.

### -3036 ACCOUNT_BAN_REPAY

- This account is not allowed to repay.

### -3037 PNL_CLEARING

- PNL is clearing. Wait a second.

### -3038 LISTEN_KEY_NOT_FOUND

- Listen key not found.

### -3041 BALANCE_NOT_CLEARED

- Balance is not enough

### -3042 PRICE_INDEX_NOT_FOUND

- PriceIndex not available for this margin pair.

### -3043 TRANSFER_IN_NOT_ALLOWED

- Transferring in not allowed.

### -3044 SYSTEM_BUSY

- System busy.

### -3045 SYSTEM

- The system doesn't have enough asset now.

### -3999 NOT_WHITELIST_USER

- This function is only available for invited users.

### -4001 CAPITAL_INVALID

- Invalid operation.

### -4002 CAPITAL_IG

- Invalid get.

### -4003 CAPITAL_IEV

- Your input email is invalid.

### -4004 CAPITAL_UA

- You don't login or auth.

### -4005 CAPAITAL_TOO_MANY_REQUEST

- Too many new requests.

### -4006 CAPITAL_ONLY_SUPPORT_PRIMARY_ACCOUNT

- Support main account only.

### -4007 CAPITAL_ADDRESS_VERIFICATION_NOT_PASS

- Address validation is not passed.

### -4008 CAPITAL_ADDRESS_TAG_VERIFICATION_NOT_PASS

- Address tag validation is not passed.

### -4010 CAPITAL_WHITELIST_EMAIL_CONFIRM

- White list mail has been confirmed.

### -4011 CAPITAL_WHITELIST_EMAIL_EXPIRED

- White list mail is invalid.

### -4012 CAPITAL_WHITELIST_CLOSE

- White list is not opened.

### -4013 CAPITAL_WITHDRAW_2FA_VERIFY

- 2FA is not opened.

### -4014 CAPITAL_WITHDRAW_LOGIN_DELAY

- Withdraw is not allowed within 2 min login.

### -4015 CAPITAL_WITHDRAW_RESTRICTED_MINUTE

- Withdraw is limited.

### -4016 CAPITAL_WITHDRAW_RESTRICTED_PASSWORD

- Within 24 hours after password modification, withdrawal is prohibited.

### -4017 CAPITAL_WITHDRAW_RESTRICTED_UNBIND_2FA

- Within 24 hours after the release of 2FA, withdrawal is prohibited.

### -4018 CAPITAL_WITHDRAW_ASSET_NOT_EXIST

- We don't have this asset.

### -4019 CAPITAL_WITHDRAW_ASSET_PROHIBIT

- Current asset is not open for withdrawal.

### -4021 CAPITAL_WITHDRAW_AMOUNT_MULTIPLE

- Asset withdrawal must be an %s multiple of %s.

### -4022 CAPITAL_WITHDRAW_MIN_AMOUNT

- Not less than the minimum pick-up quantity %s.

### -4023 CAPITAL_WITHDRAW_MAX_AMOUNT

- Within 24 hours, the withdrawal exceeds the maximum amount.

### -4024 CAPITAL_WITHDRAW_USER_NO_ASSET

- You don't have this asset.

### -4025 CAPITAL_WITHDRAW_USER_ASSET_LESS_THAN_ZERO

- The number of hold asset is less than zero.

### -4026 CAPITAL_WITHDRAW_USER_ASSET_NOT_ENOUGH

- You have insufficient balance.

### -4027 CAPITAL_WITHDRAW_GET_TRAN_ID_FAILURE

- Failed to obtain tranId.

### -4028 CAPITAL_WITHDRAW_MORE_THAN_FEE

- The amount of withdrawal must be greater than the Commission.

### -4029 CAPITAL_WITHDRAW_NOT_EXIST

- The withdrawal record does not exist.

### -4030 CAPITAL_WITHDRAW_CONFIRM_SUCCESS

- Confirmation of successful asset withdrawal.

### -4031 CAPITAL_WITHDRAW_CANCEL_FAILURE

- Cancellation failed.

### -4032 CAPITAL_WITHDRAW_CHECKSUM_VERIFY_FAILURE

- Withdraw verification exception.

### -4033 CAPITAL_WITHDRAW_ILLEGAL_ADDRESS

- Illegal address.

### -4034 CAPITAL_WITHDRAW_ADDRESS_CHEAT

- The address is suspected of fake.

### -4035 CAPITAL_WITHDRAW_NOT_WHITE_ADDRESS

- This address is not on the whitelist. Please join and try again.

### -4036 CAPITAL_WITHDRAW_NEW_ADDRESS

- The new address needs to be withdrawn in {0} hours.

### -4037 CAPITAL_WITHDRAW_RESEND_EMAIL_FAIL

- Re-sending Mail failed.

### -4038 CAPITAL_WITHDRAW_RESEND_EMAIL_TIME_OUT

- Please try again in 5 minutes.

### -4039 CAPITAL_USER_EMPTY

- The user does not exist.

### -4040 CAPITAL_NO_CHARGE

- This address not charged.

### -4041 CAPITAL_MINUTE_TOO_SMALL

- Please try again in one minute.

### -4042 CAPITAL_CHARGE_NOT_RESET

- This asset cannot get deposit address again.

### -4043 CAPITAL_ADDRESS_TOO_MUCH

- More than 100 recharge addresses were used in 24 hours.

### -4044 CAPITAL_BLACKLIST_COUNTRY_GET_ADDRESS

- This is a blacklist country.

### -4045 CAPITAL_GET_ASSET_ERROR

- Failure to acquire assets.

### -4046 CAPITAL_AGREEMENT_NOT_CONFIRMED

- Agreement not confirmed.

### -4047 CAPITAL_DATE_INTERVAL_LIMIT

- Time interval must be within 0-90 days

### -4060 CAPITAL_WITHDRAW_USER_ASSET_LOCK_DEPOSIT

- As your deposit has not reached the required block confirmations, we have temporarily locked {0}
  asset

### -4106 TAG_NOT_SUPPORTED_FOR_NETWORK

- This network does not support memo/tag. Please remove the `addressTag` field and try again.

### -5001 ASSET_DRIBBLET_CONVERT_SWITCH_OFF

- Don't allow transfer to micro assets.

### -5002 ASSET_ASSET_NOT_ENOUGH

- You have insufficient balance.

### -5003 ASSET_USER_HAVE_NO_ASSET

- You don't have this asset.

### -5004 USER_OUT_OF_TRANSFER_FLOAT

- The residual balances have exceeded 0.001BTC, Please re-choose.
- The residual balances of %s have exceeded 0.001BTC, Please re-choose.

### -5005 USER_ASSET_AMOUNT_IS_TOO_LOW

- The residual balances of the BTC is too low
- The residual balances of %s is too low, Please re-choose.

### -5006 USER_CAN_NOT_REQUEST_IN_24_HOURS

- Only transfer once in 24 hours.

### -5007 AMOUNT_OVER_ZERO

- Quantity must be greater than zero.

### -5008 ASSET_WITHDRAW_WITHDRAWING_NOT_ENOUGH

- Insufficient amount of returnable assets.

### -5009 PRODUCT_NOT_EXIST

- Product does not exist.

### -5010 TRANSFER_FAIL

- Asset transfer fail.

### -5011 FUTURE_ACCT_NOT_EXIST

- future account not exists.

### -5012 TRANSFER_PENDING

- Asset transfer is in pending.

### -5021 PARENT_SUB_HAVE_NO_RELATION

- This parent sub have no relation

### -5012 FUTURE_ACCT_OR_SUBRELATION_NOT_EXIST

- future account or sub relation not exists.

## Equity-specific pre-check errors

These codes come from the equity pre-check layer (before the business layer) and are **not** part of
the standard SAPI ranges above. They take precedence over the `486xxx` codes below.

### -26004

Symbol does not exist. Returned by `POST /order/place` and `POST /tokenized/mint` when the supplied
`symbol` / `underlyingAsset` is not a listed ticker. The doc's `SYMBOL_NOT_EXISTS` wording maps to
this code in practice.

## 486xxx - Stocks Trading Business Errors

Returned by the equity service after a request passes pre-check. **Note:** several
parameter-validation codes (`486217`, `486431`, `486432`, `486433`) are surfaced only in the UI
layer; for API callers these conditions return the pre-check code `-1102` instead — see the
precedence note at the top.

### Account & Symbol

| Code     | Message                                                        |
| -------- | -------------------------------------------------------------- |
| `486003` | The system is temporarily unavailable. Please try again later. |
| `486105` | Account not found.                                             |
| `486201` | This quote asset is not supported.                             |
| `486203` | Invalid stock symbol.                                          |
| `486207` | This stock is currently unavailable for trading.               |
| `486208` | This stock is not yet listed for trading.                      |
| `486209` | This stock has been delisted.                                  |
| `486212` | Unable to create the account. Please try again later.          |
| `486213` | Stock trading account not found.                               |
| `486214` | The system is temporarily unavailable. Please try again later. |
| `486215` | Your account is not active. Please contact support.            |
| `486216` | Your sub-account does not support stock trading.               |
| `486217` | Either orderId or clientOrderId is required.                   |
| `486218` | Order not found.                                               |

### Market Data

| Code     | Message                                                        |
| -------- | -------------------------------------------------------------- |
| `486301` | The system is temporarily unavailable. Please try again later. |
| `486302` | Unable to retrieve the market price. Please try again later.   |

### Order Placement & Cancellation

| Code     | Message                                                                                                                                                     |
| -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `486401` | This wallet type is not supported.                                                                                                                          |
| `486402` | You have reached your trading limit.                                                                                                                        |
| `486403` | You have reached your daily trading limit for this stock.                                                                                                   |
| `486404` | The system is temporarily unavailable. Please try again later.                                                                                              |
| `486405` | Insufficient balance. Please deposit and try again.                                                                                                         |
| `486406` | The system is temporarily unavailable. Please try again later.                                                                                              |
| `486407` | Overnight trading is halted for this stock.                                                                                                                 |
| `486408` | This stock does not support fractional trading.                                                                                                             |
| `486409` | This stock does not support fractional trading during extended hours.                                                                                       |
| `486410` | Please sign the trading disclaimer before placing an order.                                                                                                 |
| `486411` | Unable to cancel the order. Please try again later.                                                                                                         |
| `486412` | This order cannot be canceled.                                                                                                                              |
| `486413` | Market orders are temporarily unavailable for newly listed IPO stocks. Please use limit order.                                                              |
| `486414` | Extended session trading is not available for this stock.                                                                                                   |
| `486416` | Order quantity is below the minimum.                                                                                                                        |
| `486417` | Order quantity exceeds the maximum.                                                                                                                         |
| `486418` | Order quantity must be a multiple of the minimum lot size.                                                                                                  |
| `486419` | Order amount is below the minimum.                                                                                                                          |
| `486420` | Order amount exceeds the maximum.                                                                                                                           |
| `486421` | Limit price is above the allowed range.                                                                                                                     |
| `486422` | Limit price is below the allowed range.                                                                                                                     |
| `486423` | You have reached the maximum number of open orders.                                                                                                         |
| `486424` | Order amount is too small after fees. Please increase your order amount.                                                                                    |
| `486425` | The system is temporarily unavailable. Please try again later.                                                                                              |
| `486426` | Buy orders are not allowed for this stock.                                                                                                                  |
| `486427` | Sell orders are not allowed for this stock.                                                                                                                 |
| `486428` | Trading is currently suspended for this stock.                                                                                                              |
| `486429` | Unable to process trading for this stock. Please try again later.                                                                                           |
| `486430` | The system is temporarily unavailable. Please try again later.                                                                                              |
| `486431` | Please enter a valid quantity or amount.                                                                                                                    |
| `486432` | Please input a valid limit price.                                                                                                                           |
| `486433` | Order value must be greater than 0.                                                                                                                         |
| `486434` | Minimum order value is $1.                                                                                                                                  |
| `486435` | Stock not found. Please check the symbol.                                                                                                                   |
| `486436` | This stock is currently unavailable for trading.                                                                                                            |
| `486437` | Insufficient shares available. Please check your holdings.                                                                                                  |
| `486438` | Your account is not authorized for trading.                                                                                                                 |
| `486439` | Your account is currently restricted to sell-only. Please contact support for assistance.                                                                   |
| `486440` | Trade denied: Pattern Day Trading protection triggered. See Help Center for details.                                                                        |
| `486441` | Only limit orders are available during extended hours.                                                                                                      |
| `486442` | Fractional shares can only be traded with market orders.                                                                                                    |
| `486443` | This order type is not available for fractional shares.                                                                                                     |
| `486444` | Order not found or already filled. Unable to cancel.                                                                                                        |
| `486445` | No position found for this stock.                                                                                                                           |
| `486446` | Cancellation in progress. Your order may still be filled before completion. Funds will remain frozen until final confirmation.                              |
| `486447` | Some orders are cancelled. The rest are still being processed and may be filled before cancellation. Funds will stay frozen until all orders are confirmed. |
| `486449` | Duplicate clientOrderId. Please use a new clientOrderId and try again.                                                                                      |
| `486450` | Failed to redeem from Earn. Please try again later.                                                                                                         |
| `486451` | Earn redemption is processing. Please try again later.                                                                                                      |

### Tokenized Conversion

| Code     | Message                                                                                           |
| -------- | ------------------------------------------------------------------------------------------------- |
| `486601` | The system is temporarily unavailable. Please try again later.                                    |
| `486602` | The system is temporarily unavailable. Please try again later.                                    |
| `486603` | The system is temporarily unavailable. Please try again later.                                    |
| `486604` | The system is temporarily unavailable. Please try again later.                                    |
| `486702` | Insufficient balance for conversion. Please check your balance and try again.                     |
| `486706` | Conversion could not be processed at this time. Please try again in a few minutes.                |
| `486717` | You've reached the conversion limit for this period. Please try again later or reduce the amount. |
| `486718` | Token conversion is temporarily unavailable. Please try again later.                              |
| `486719` | Token conversion is temporarily unavailable. Please try again later.                              |

## Reporting an Unknown Code

If you encounter a `486xxx` code that is not listed above, please open an issue with the full error
envelope and request / response timestamps.

---

# 错误代码

股票交易接口的错误来自两个层次,**前置层优先**:

1. **前置 —— 标准 SAPI 错误**(`10xx` / `11xx–2xxx` /
   `3xxx–5xxx`,负数码)。SAPI 在请求到达 equity 服务**之前**先校验签名、时间戳、参数与格式。任一不过,返回的是 SAPI 码(如
   `-1102`),**而不是** `486xxx`。
2. **后置 —— 本模块业务错误**(`486xxx`,正数码)。仅当请求通过前置校验、再违反 equity 业务规则时返回。

所有错误均使用标准 SAPI 错误包络:业务码在 `code` 字段,人类可读信息在 `msg` 字段。

## 10xx -常规服务器或网络问题

### -1000 UNKNOWN

- 处理请求时发生未知错误。
- 处理请求时发生未知错误。[%s]

### -1001 DISCONNECTED

- 内部错误; 无法处理您的请求。 请再试一次.

### -1002 UNAUTHORIZED

- 您无权执行此请求。

### -1003 TOO_MANY_REQUESTS

- 排队的请求过多。
- 请求权重过多； 当前限制是 %s 每 %s 的请求权重。 请使用 Websocket
  Streams 进行实时更新，以避免轮询API。
- 请求权重过多； IP被禁止，直到％s。 请使用 Websocket Streams 进行实时更新，以免被禁。

### -1004 SERVER_BUSY

- 服务器正忙，请稍候再试。

### -1006 UNEXPECTED_RESP

- 从消息总线收到意外的响应。 执行状态未知。

### -1007 TIMEOUT

- 等待后端服务器响应超时。 发送状态未知； 执行状态未知。

### -1008 SERVER_BUSY

- 现货交易服务器当前因其他请求而过载。 请在几分钟后重试。

### -1014 UNKNOWN_ORDER_COMPOSITION

- 不支持的订单组合。

### -1015 TOO_MANY_ORDERS

- 新订单太多。
- 新订单太多； 当前限制为每％s ％s个订单。

### -1016 SERVICE_SHUTTING_DOWN

- 该服务不可用。

### -1020 UNSUPPORTED_OPERATION

- 不支持此操作。

### -1021 INVALID_TIMESTAMP

- 此请求的时间戳在recvWindow之外。
- 此请求的时间戳比服务器时间提前1000毫秒。

### -1022 INVALID_SIGNATURE

- 此请求的签名无效。

### -1099 Not found, authenticated, or authorized

- 替换错误代码-1999

## 11xx - 2xxx Request issues

### -1100 ILLEGAL_CHARS

- 在参数中发现非法字符。
- 在参数中发现非法字符。`％s`
- 在参数`％s`中发现非法字符； 合法范围是`％s`。

### -1101 TOO_MANY_PARAMETERS

- 为此端点发送的参数太多。
- 参数太多； 预期为`％s`并收到了`％s`。
- 检测到的参数值重复。

### -1102 MANDATORY_PARAM_EMPTY_OR_MALFORMED

- 未发送强制性参数，该参数为空/空或格式错误。
- 强制参数`％s`未发送，为空/空或格式错误。
- 必须发送参数`％s`或`％s`，但两者均为空！

> 标准 SAPI 码（`10xx`–`5xxx`）与 SPOT API 一致。权威、始终最新的完整信息列表请参见
> [SPOT API 错误码参考](https://developers.binance.com/en/docs/products/spot/errors#-1102-mandatory_param_empty_or_malformed)。

### -1103 UNKNOWN_PARAM

- 发送了未知参数。

### -1104 UNREAD_PARAMETERS

- 并非所有发送的参数都被读取。
- 并非所有发送的参数都被读取； 读取了`％s`参数，但被发送了`％s`。

### -1105 PARAM_EMPTY

- 参数为空。
- 参数`％s`为空。

### -1106 PARAM_NOT_REQUIRED

- 不需要时已发送参数。
- 不需要时发送参数`％s`。

### -1111 BAD_PRECISION

- 精度超过为此资产定义的最大值。

### -1112 NO_DEPTH

- 交易对没有挂单。

### -1114 TIF_NOT_REQUIRED

- 不需要时发送了TimeInForce参数。

### -1115 INVALID_TIF

- 无效 timeInForce.

### -1116 INVALID_ORDER_TYPE

- 无效订单类型。

### -1117 INVALID_SIDE

- 无效买卖方向。

### -1118 EMPTY_NEW_CL_ORD_ID

- 新的客户订单ID为空。

### -1119 EMPTY_ORG_CL_ORD_ID

- 客户自定义的订单ID为空。

### -1120 BAD_INTERVAL

- 无效时间间隔。

### -1121 BAD_SYMBOL

- 无效的交易对。

### -1125 INVALID_LISTEN_KEY

- 该listenKey不存在。

### -1127 MORE_THAN_XX_HOURS

- 查询间隔太大。
- 从开始时间到结束时间之间超过％s小时。

### -1128 OPTIONAL_PARAMS_BAD_COMBO

- 可选参数组合无效。

### -1130 INVALID_PARAMETER

- 发送的参数为无效数据。
- 发送参数`％s`的数据无效。

### -1131 BAD_RECV_WINDOW

- `recvWindow` 必须小于 60000

### -1134 BAD_STRATEGY_TYPE

- `strategyType` 必须小于 1000000

#### -1145 INVALID_CANCEL_RESTRICTIONS

- `cancelRestrictions` 必须是 `ONLY_NEW` 或者 `ONLY_PARTIALLY_FILLED`。

#### -1151 重复的交易对

- Symbol is present multiple times in the list.

### -2010 NEW_ORDER_REJECTED

- 新订单被拒绝

### -2011 CANCEL_REJECTED

- 取消订单被拒绝

### -2013 NO_SUCH_ORDER

- 订单不存在。

### -2014 BAD_API_KEY_FMT

- API-key 格式无效。

### -2015 REJECTED_MBX_KEY

- 无效的API密钥，IP或操作权限。

### -2016 NO_TRADING_WINDOW

- 找不到该交易对的交易窗口。 尝试改为24小时自动报价。

#### -2026 ORDER_ARCHIVED

- 订单已被存档因为此订单被取消或过期，无交易数量而最后的更新已超过 90 天前。

## 3xxx-5xxx SAPI 具体问题

### -3000 INNER_FAILURE

- 内部服务器错误。

### -3001 NEED_ENABLE_2FA

- 请先启用2FA。

### -3002 ASSET_DEFICIENCY

- 此资产不存在。

### -3003 NO_OPENED_MARGIN_ACCOUNT

- 杠杆账户不存在。

### -3004 TRADE_NOT_ALLOWED

- 禁止交易。

### -3005 TRANSFER_OUT_NOT_ALLOWED

- 不允许转账。

### -3006 EXCEED_MAX_BORROWABLE

- 您的已借金额已超过最高可借金额。

### -3007 HAS_PENDING_TRANSACTION

- 您有待处理的交易，请稍后再试。

### -3008 BORROW_NOT_ALLOWED

- 不允许借款。

### -3009 ASSET_NOT_MORTGAGEABLE

- 此资产目前不允许转入杠杆账户。

### -3010 REPAY_NOT_ALLOWED

- 不允许还款。

### -3011 BAD_DATE_RANGE

- 您输入的日期无效。

### -3012 ASSET_ADMIN_BAN_BORROW

- 此资产禁止借款。

### -3013 LT_MIN_BORROWABLE

- 借入金额少于最低借入金额。

### -3014 ACCOUNT_BAN_BORROW

- 此帐户禁止借款。

### -3015 REPAY_EXCEED_LIABILITY

- 还款额超过借款额。

### -3016 LT_MIN_REPAY

- 还款额少于最低还款额。

### -3017 ASSET_ADMIN_BAN_MORTGAGE

- 此资产目前不允许转入保证金账户。

### -3018 ACCOUNT_BAN_MORTGAGE

- 此帐户已禁止转入。

### -3019 ACCOUNT_BAN_ROLLOUT

- 此帐户禁止转出。

### -3020 EXCEED_MAX_ROLLOUT

- 转出金额超过上限。

### -3021 PAIR_ADMIN_BAN_TRADE

- 杠杆账户无法交易此交易对。

### -3022 ACCOUNT_BAN_TRADE

- 账号被禁止交易。

### -3023 WARNING_MARGIN_LEVEL

- 无法在当前杠杆倍数下转出资金或者下单

### -3024 FEW_LIABILITY_LEFT

- 付款之后未付款的债务太小

### -3025 INVALID_EFFECTIVE_TIME

- 输入时间有误。

### -3026 VALIDATION_FAILED

- 输入参数有误。

### -3027 NOT_VALID_MARGIN_ASSET

- 无效的杠杆资产。

### -3028 NOT_VALID_MARGIN_PAIR

- 无效的杠杆交易对。

### -3029 TRANSFER_FAILED

- 转账失败。

### -3036 ACCOUNT_BAN_REPAY

- 此账号无法还款。

### -3037 PNL_CLEARING

- `PNL`正在清帐，请稍等。

### -3038 LISTEN_KEY_NOT_FOUND

- 找不到`Listen key`

### -3041 BALANCE_NOT_CLEARED

- 余额不足

### -3042 PRICE_INDEX_NOT_FOUND

- 该杠杆交易对无可用价格指数。

### -3043 TRANSFER_IN_NOT_ALLOWED

- 不允许转入。

### -3044 SYSTEM_BUSY

- 系统繁忙。

### -3045 SYSTEM

- 系统目前没有足够可借的资产。

### -3999 NOT_WHITELIST_USER

- 此功能只面向邀请的用户。

### -4001 CAPITAL_INVALID

- 非法操作

### -4002 CAPITAL_IG

- 非法获取

### -4003 CAPITAL_IEV

- 非法邮箱验证

### -4004 CAPITAL_UA

- 未登录或者认证。

### -4005 CAPAITAL_TOO_MANY_REQUEST

- 请求太频繁。

### -4006 CAPITAL_ONLY_SUPPORT_PRIMARY_ACCOUNT

- 只支持主账号。

### -4007 CAPITAL_ADDRESS_VERIFICATION_NOT_PASS

- 地址的没有通过校验。

### -4008 CAPITAL_ADDRESS_TAG_VERIFICATION_NOT_PASS

- 地址的标记信息(`tag`)没有通过校验。

### -4010 CAPITAL_WHITELIST_EMAIL_CONFIRM

- 确认电子邮件已经列入白名单。

### -4011 CAPITAL_WHITELIST_EMAIL_EXPIRED

- 列入白名单的电子邮件无效。

### -4012 CAPITAL_WHITELIST_CLOSE

- 白名单未打开。

### -4013 CAPITAL_WITHDRAW_2FA_VERIFY

- 2FA未打开。

### -4014 CAPITAL_WITHDRAW_LOGIN_DELAY

- 在登录后的2分钟之内不允许提款。

### -4015 CAPITAL_WITHDRAW_RESTRICTED_MINUTE

- 暂停提款

### -4016 CAPITAL_WITHDRAW_RESTRICTED_PASSWORD

- 在密码修改后的24小时之内不允许提款。

### -4017 CAPITAL_WITHDRAW_RESTRICTED_UNBIND_2FA

- 在2FA发行后的24小时之内不允许提款。

### -4018 CAPITAL_WITHDRAW_ASSET_NOT_EXIST

- 此资产不存在。

### -4019 CAPITAL_WITHDRAW_ASSET_PROHIBIT

- 此资产不允许提款。

### -4021 CAPITAL_WITHDRAW_AMOUNT_MULTIPLE

- 资产的提款数量必须是％s的％s倍。

### -4022 CAPITAL_WITHDRAW_MIN_AMOUNT

- 不须少于最低的提款数量％s。

### -4023 CAPITAL_WITHDRAW_MAX_AMOUNT

- 在24小时之内，不须超过最高的提款数量。

### -4024 CAPITAL_WITHDRAW_USER_NO_ASSET

- 当前用户没有此资产。

### -4025 CAPITAL_WITHDRAW_USER_ASSET_LESS_THAN_ZERO

- 持有资产的数量小于零。

### -4026 CAPITAL_WITHDRAW_USER_ASSET_NOT_ENOUGH

- 此资产余额不足。

### -4027 CAPITAL_WITHDRAW_GET_TRAN_ID_FAILURE

- 无法获取tranId。

### -4028 CAPITAL_WITHDRAW_MORE_THAN_FEE

- 提款金额必须多于佣金额。

### -4029 CAPITAL_WITHDRAW_NOT_EXIST

- 此提款记录不存在。

### -4030 CAPITAL_WITHDRAW_CONFIRM_SUCCESS

- 提款资产成功。

### -4031 CAPITAL_WITHDRAW_CANCEL_FAILURE

- 取消提款失败。

### -4032 CAPITAL_WITHDRAW_CHECKSUM_VERIFY_FAILURE

- 验证提款失败。

### -4033 CAPITAL_WITHDRAW_ILLEGAL_ADDRESS

- 提款地址不合法。

### -4034 CAPITAL_WITHDRAW_ADDRESS_CHEAT

- 当前地址有异常。

### -4035 CAPITAL_WITHDRAW_NOT_WHITE_ADDRESS

- 此地址不在白名单上。请加入然后重试。

### -4036 CAPITAL_WITHDRAW_NEW_ADDRESS

- 新地址在{0}小时后才可以提款。

### -4037 CAPITAL_WITHDRAW_RESEND_EMAIL_FAIL

- 重新发送邮件失败。

### -4038 CAPITAL_WITHDRAW_RESEND_EMAIL_TIME_OUT

- 请5分钟后重试。

### -4039 CAPITAL_USER_EMPTY

- 用户不存在。

### -4041 CAPITAL_MINUTE_TOO_SMALL

- 请一分钟后重试。

### -4042 CAPITAL_CHARGE_NOT_RESET

- 资产无法重新获取存款地址。

### -4043 CAPITAL_ADDRESS_TOO_MUCH

- 在24小时之内充值超过100多个地址。

### -4044 CAPITAL_BLACKLIST_COUNTRY_GET_ADDRESS

- 此国家在黑名单上。

### -4045 CAPITAL_GET_ASSET_ERROR

- 获得资产失败。

### -4046 CAPITAL_AGREEMENT_NOT_CONFIRMED

- 协议未确认。

### -4047 CAPITAL_DATE_INTERVAL_LIMIT

- 时间间隔必须在0-90天之内

### -4060 CAPITAL_WITHDRAW_USER_ASSET_LOCK_DEPOSIT

- 体现仍在区块确认中，暂时锁定部分资产

### -4106 TAG_NOT_SUPPORTED_FOR_NETWORK

- 该网络不支持 memo/tag。请移除 `addressTag` 字段后重试。

### -5001 ASSET_DRIBBLET_CONVERT_SWITCH_OFF

- 不允许转移到微型资产。

### -5002 ASSET_ASSET_NOT_ENOUGH

- 此余额不足。

### -5003 ASSET_USER_HAVE_NO_ASSET

- 此资产不存在。

### -5004 USER_OUT_OF_TRANSFER_FLOAT

- 剩余余额已超过0.001BTC，请重新选择。
- ％s的剩余余额已超过0.001BTC，请重新选择。

### -5005 USER_ASSET_AMOUNT_IS_TOO_LOW

- BTC的剩余余额太低，请重新选择。
- ％s的剩余余额太低，请重新选择。

### -5006 USER_CAN_NOT_REQUEST_IN_24_HOURS

- 24小时内只能转账一次。

### -5007 AMOUNT_OVER_ZERO

- 数量必须大于零。

### -5008 ASSET_WITHDRAW_WITHDRAWING_NOT_ENOUGH

- 可退回资产的金额不足。

### -5009 PRODUCT_NOT_EXIST

- 产品不存在。

### -5010 TRANSFER_FAIL

- 资产转移失败。

### -5011 FUTURE_ACCT_NOT_EXIST

- 合约帐户不存在。

### -5012 TRANSFER_PENDING

- 资产转移正在进行中。

### -5021 PARENT_SUB_HAVE_NO_RELATION

- 当前的子账户和母账户没有从属关系。

### -5012 FUTURE_ACCT_OR_SUBRELATION_NOT_EXIST

- 合约帐户或子账户关系不存在。

## Equity 专属前置错误码

以下码来自 equity 前置校验层(在业务层之前),**不属于**上面的标准 SAPI 区间,且优先于下面的 `486xxx`。

### -26004

Symbol 不存在。当 `symbol` / `underlyingAsset` 不是上架 ticker 时,`POST /order/place` 与
`POST /tokenized/mint` 返回此码。文档中 `SYMBOL_NOT_EXISTS` 的说法实际对应此码。

## 486xxx - 股票交易业务错误

请求通过前置校验后,由 equity 服务返回。**注意:**
部分参数校验码(`486217`、`486431`、`486432`、`486433`)仅在 UI 层出现;对 API 调用方,这些场景实际返回前置码
`-1102`——详见顶部的优先级说明。

### 账户与 Symbol

| Code     | 信息                                      |
| -------- | ----------------------------------------- |
| `486003` | 系统暂时不可用，请稍后重试。              |
| `486105` | 未找到账户。                              |
| `486201` | 不支持该计价资产。                        |
| `486203` | 无效的股票 symbol。                       |
| `486207` | 该股票当前不可交易。                      |
| `486208` | 该股票尚未上市交易。                      |
| `486209` | 该股票已退市。                            |
| `486212` | 无法创建账户，请稍后重试。                |
| `486213` | 未找到股票交易账户。                      |
| `486214` | 系统暂时不可用，请稍后重试。              |
| `486215` | 您的账户未激活，请联系客服。              |
| `486216` | 您的子账户不支持股票交易。                |
| `486217` | orderId 或 clientOrderId 至少需提供一个。 |
| `486218` | 未找到订单。                              |

### 行情

| Code     | 信息                           |
| -------- | ------------------------------ |
| `486301` | 系统暂时不可用，请稍后重试。   |
| `486302` | 无法获取市场价格，请稍后重试。 |

### 下单与撤单

| Code     | 信息                                                                                     |
| -------- | ---------------------------------------------------------------------------------------- |
| `486401` | 不支持该钱包类型。                                                                       |
| `486402` | 您已达到交易限额。                                                                       |
| `486403` | 您已达到该股票的每日交易限额。                                                           |
| `486404` | 系统暂时不可用，请稍后重试。                                                             |
| `486405` | 余额不足，请充值后重试。                                                                 |
| `486406` | 系统暂时不可用，请稍后重试。                                                             |
| `486407` | 该股票的夜盘交易已暂停。                                                                 |
| `486408` | 该股票不支持碎股交易。                                                                   |
| `486409` | 该股票在盘前盘后不支持碎股交易。                                                         |
| `486410` | 下单前请先签署交易免责声明。                                                             |
| `486411` | 无法撤销订单，请稍后重试。                                                               |
| `486412` | 该订单无法撤销。                                                                         |
| `486413` | 新上市 IPO 股票暂不支持市价单，请使用限价单。                                            |
| `486414` | 该股票不支持盘前盘后交易。                                                               |
| `486416` | 订单数量低于最小值。                                                                     |
| `486417` | 订单数量超过最大值。                                                                     |
| `486418` | 订单数量必须是最小交易单位的整数倍。                                                     |
| `486419` | 订单金额低于最小值。                                                                     |
| `486420` | 订单金额超过最大值。                                                                     |
| `486421` | 限价高于允许范围。                                                                       |
| `486422` | 限价低于允许范围。                                                                       |
| `486423` | 您已达到最大挂单数量。                                                                   |
| `486424` | 扣除手续费后订单金额过小，请提高订单金额。                                               |
| `486425` | 系统暂时不可用，请稍后重试。                                                             |
| `486426` | 该股票不允许买入。                                                                       |
| `486427` | 该股票不允许卖出。                                                                       |
| `486428` | 该股票当前暂停交易。                                                                     |
| `486429` | 无法处理该股票的交易，请稍后重试。                                                       |
| `486430` | 系统暂时不可用，请稍后重试。                                                             |
| `486431` | 请输入有效的数量或金额。                                                                 |
| `486432` | 请输入有效的限价。                                                                       |
| `486433` | 订单价值必须大于 0。                                                                     |
| `486434` | 最小订单价值为 $1。                                                                      |
| `486435` | 未找到该股票，请检查 symbol。                                                            |
| `486436` | 该股票当前不可交易。                                                                     |
| `486437` | 可用股数不足，请检查您的持仓。                                                           |
| `486438` | 您的账户未获授权交易。                                                                   |
| `486439` | 您的账户当前仅限卖出，请联系客服协助。                                                   |
| `486440` | 交易被拒：触发日内交易（Pattern Day Trading）保护，详见帮助中心。                        |
| `486441` | 盘前盘后仅支持限价单。                                                                   |
| `486442` | 碎股仅支持市价单交易。                                                                   |
| `486443` | 该订单类型不支持碎股。                                                                   |
| `486444` | 未找到订单或订单已成交，无法撤销。                                                       |
| `486445` | 未找到该股票的持仓。                                                                     |
| `486446` | 撤单处理中。您的订单在完成前仍可能成交。资金将保持冻结，直至最终确认。                   |
| `486447` | 部分订单已撤销，其余仍在处理中，撤销前仍可能成交。资金将保持冻结，直至所有订单确认完成。 |
| `486449` | clientOrderId 重复，请使用新的 clientOrderId 重试。                                      |
| `486450` | 从赚币赎回失败，请稍后重试。                                                             |
| `486451` | 赚币赎回处理中，请稍后重试。                                                             |

### 代币化转换

| Code     | 信息                                           |
| -------- | ---------------------------------------------- |
| `486601` | 系统暂时不可用，请稍后重试。                   |
| `486602` | 系统暂时不可用，请稍后重试。                   |
| `486603` | 系统暂时不可用，请稍后重试。                   |
| `486604` | 系统暂时不可用，请稍后重试。                   |
| `486702` | 转换余额不足，请检查余额后重试。               |
| `486706` | 当前无法处理转换，请几分钟后重试。             |
| `486717` | 您已达到本期的转换限额，请稍后重试或减少数量。 |
| `486718` | 代币转换暂时不可用，请稍后重试。               |
| `486719` | 代币转换暂时不可用，请稍后重试。               |

## 遇到未列出的 Code

如果你遇到上表之外的 `486xxx` 码,请将完整错误包络 + 请求 / 响应时间戳作为 issue 反馈给我们。