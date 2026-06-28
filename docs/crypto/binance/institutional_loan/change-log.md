---
exchange: binance
source_url: https://developers.binance.com/docs/institutional_loan/change-log
api_type: REST
updated_at: 2026-05-27 19:01:25.448074
---

# Error Codes

> The error JSON payload:
    
    
    {  
      "code":-1121,  
      "msg":"Invalid symbol."  
    }  
    

Errors consist of two parts: an error code and a message. Codes are universal, but messages can vary.

## 10xx - General Server or Network issues[​](/docs/institutional_loan/error-code#10xx---general-server-or-network-issues "Direct link to 10xx - General Server or Network issues")

### -1000 UNKNOWN[​](/docs/institutional_loan/error-code#-1000-unknown "Direct link to -1000 UNKNOWN")

  * An unknown error occurred while processing the request.
  * An unknown error occurred while processing the request.[%s]



### -1001 DISCONNECTED[​](/docs/institutional_loan/error-code#-1001-disconnected "Direct link to -1001 DISCONNECTED")

  * Internal error; unable to process your request. Please try again.



### -1002 UNAUTHORIZED[​](/docs/institutional_loan/error-code#-1002-unauthorized "Direct link to -1002 UNAUTHORIZED")

  * You are not authorized to execute this request.



### -1003 TOO_MANY_REQUESTS[​](/docs/institutional_loan/error-code#-1003-too_many_requests "Direct link to -1003 TOO_MANY_REQUESTS")

  * Too many requests queued.
  * Too much request weight used; current limit is %s request weight per %s. Please use WebSocket Streams for live updates to avoid polling the API.
  * Way too much request weight used; IP banned until %s. Please use WebSocket Streams for live updates to avoid bans.



### -1004 SERVER_BUSY[​](/docs/institutional_loan/error-code#-1004-server_busy "Direct link to -1004 SERVER_BUSY")

  * Server is busy, please wait and try again



### -1006 UNEXPECTED_RESP[​](/docs/institutional_loan/error-code#-1006-unexpected_resp "Direct link to -1006 UNEXPECTED_RESP")

  * An unexpected response was received from the message bus. Execution status unknown.



### -1007 TIMEOUT[​](/docs/institutional_loan/error-code#-1007-timeout "Direct link to -1007 TIMEOUT")

  * Timeout waiting for response from backend server. Send status unknown; execution status unknown.



### -1008 SERVER_BUSY[​](/docs/institutional_loan/error-code#-1008-server_busy "Direct link to -1008 SERVER_BUSY")

  * Spot server is currently overloaded with other requests. Please try again in a few minutes.



### -1014 UNKNOWN_ORDER_COMPOSITION[​](/docs/institutional_loan/error-code#-1014-unknown_order_composition "Direct link to -1014 UNKNOWN_ORDER_COMPOSITION")

  * Unsupported order combination.



### -1015 TOO_MANY_ORDERS[​](/docs/institutional_loan/error-code#-1015-too_many_orders "Direct link to -1015 TOO_MANY_ORDERS")

  * Too many new orders.
  * Too many new orders; current limit is %s orders per %s.



### -1016 SERVICE_SHUTTING_DOWN[​](/docs/institutional_loan/error-code#-1016-service_shutting_down "Direct link to -1016 SERVICE_SHUTTING_DOWN")

  * This service is no longer available.



### -1020 UNSUPPORTED_OPERATION[​](/docs/institutional_loan/error-code#-1020-unsupported_operation "Direct link to -1020 UNSUPPORTED_OPERATION")

  * This operation is not supported.



### -1021 INVALID_TIMESTAMP[​](/docs/institutional_loan/error-code#-1021-invalid_timestamp "Direct link to -1021 INVALID_TIMESTAMP")

  * Timestamp for this request is outside of the recvWindow.
  * Timestamp for this request was 1000ms ahead of the server's time.



### -1022 INVALID_SIGNATURE[​](/docs/institutional_loan/error-code#-1022-invalid_signature "Direct link to -1022 INVALID_SIGNATURE")

  * Signature for this request is not valid.



### -1099 Not found, authenticated, or authorized[​](/docs/institutional_loan/error-code#-1099-not-found-authenticated-or-authorized "Direct link to -1099 Not found, authenticated, or authorized")

  * This replaces error code -1999



## 11xx - 2xxx Request issues[​](/docs/institutional_loan/error-code#11xx---2xxx-request-issues "Direct link to 11xx - 2xxx Request issues")

### -1100 ILLEGAL_CHARS[​](/docs/institutional_loan/error-code#-1100-illegal_chars "Direct link to -1100 ILLEGAL_CHARS")

  * Illegal characters found in a parameter.
  * Illegal characters found in a parameter. %s
  * Illegal characters found in parameter `%s`; legal range is `%s`.



### -1101 TOO_MANY_PARAMETERS[​](/docs/institutional_loan/error-code#-1101-too_many_parameters "Direct link to -1101 TOO_MANY_PARAMETERS")

  * Too many parameters sent for this endpoint.
  * Too many parameters; expected `%s` and received `%s`.
  * Duplicate values for a parameter detected.



### -1102 MANDATORY_PARAM_EMPTY_OR_MALFORMED[​](/docs/institutional_loan/error-code#-1102-mandatory_param_empty_or_malformed "Direct link to -1102 MANDATORY_PARAM_EMPTY_OR_MALFORMED")

  * A mandatory parameter was not sent, was empty/null, or malformed.
  * Mandatory parameter `%s` was not sent, was empty/null, or malformed.
  * Param `%s` or `%s` must be sent, but both were empty/null!



### -1103 UNKNOWN_PARAM[​](/docs/institutional_loan/error-code#-1103-unknown_param "Direct link to -1103 UNKNOWN_PARAM")

  * An unknown parameter was sent.



### -1104 UNREAD_PARAMETERS[​](/docs/institutional_loan/error-code#-1104-unread_parameters "Direct link to -1104 UNREAD_PARAMETERS")

  * Not all sent parameters were read.
  * Not all sent parameters were read; read `%s` parameter(s) but was sent `%s`.



### -1105 PARAM_EMPTY[​](/docs/institutional_loan/error-code#-1105-param_empty "Direct link to -1105 PARAM_EMPTY")

  * A parameter was empty.
  * Parameter `%s` was empty.



### -1106 PARAM_NOT_REQUIRED[​](/docs/institutional_loan/error-code#-1106-param_not_required "Direct link to -1106 PARAM_NOT_REQUIRED")

  * A parameter was sent when not required.
  * Parameter `%s` sent when not required.



### -1111 BAD_PRECISION[​](/docs/institutional_loan/error-code#-1111-bad_precision "Direct link to -1111 BAD_PRECISION")

  * Precision is over the maximum defined for this asset.



### -1112 NO_DEPTH[​](/docs/institutional_loan/error-code#-1112-no_depth "Direct link to -1112 NO_DEPTH")

  * No orders on book for symbol.



### -1114 TIF_NOT_REQUIRED[​](/docs/institutional_loan/error-code#-1114-tif_not_required "Direct link to -1114 TIF_NOT_REQUIRED")

  * TimeInForce parameter sent when not required.



### -1115 INVALID_TIF[​](/docs/institutional_loan/error-code#-1115-invalid_tif "Direct link to -1115 INVALID_TIF")

  * Invalid timeInForce.



### -1116 INVALID_ORDER_TYPE[​](/docs/institutional_loan/error-code#-1116-invalid_order_type "Direct link to -1116 INVALID_ORDER_TYPE")

  * Invalid orderType.



### -1117 INVALID_SIDE[​](/docs/institutional_loan/error-code#-1117-invalid_side "Direct link to -1117 INVALID_SIDE")

  * Invalid side.



### -1118 EMPTY_NEW_CL_ORD_ID[​](/docs/institutional_loan/error-code#-1118-empty_new_cl_ord_id "Direct link to -1118 EMPTY_NEW_CL_ORD_ID")

  * New client order ID was empty.



### -1119 EMPTY_ORG_CL_ORD_ID[​](/docs/institutional_loan/error-code#-1119-empty_org_cl_ord_id "Direct link to -1119 EMPTY_ORG_CL_ORD_ID")

  * Original client order ID was empty.



### -1120 BAD_INTERVAL[​](/docs/institutional_loan/error-code#-1120-bad_interval "Direct link to -1120 BAD_INTERVAL")

  * Invalid interval.



### -1121 BAD_SYMBOL[​](/docs/institutional_loan/error-code#-1121-bad_symbol "Direct link to -1121 BAD_SYMBOL")

  * Invalid symbol.



### -1125 INVALID_LISTEN_KEY[​](/docs/institutional_loan/error-code#-1125-invalid_listen_key "Direct link to -1125 INVALID_LISTEN_KEY")

  * This listenKey does not exist.



### -1127 MORE_THAN_XX_HOURS[​](/docs/institutional_loan/error-code#-1127-more_than_xx_hours "Direct link to -1127 MORE_THAN_XX_HOURS")

  * Lookup interval is too big.
  * More than %s hours between startTime and endTime.



### -1128 OPTIONAL_PARAMS_BAD_COMBO[​](/docs/institutional_loan/error-code#-1128-optional_params_bad_combo "Direct link to -1128 OPTIONAL_PARAMS_BAD_COMBO")

  * Combination of optional parameters invalid.



### -1130 INVALID_PARAMETER[​](/docs/institutional_loan/error-code#-1130-invalid_parameter "Direct link to -1130 INVALID_PARAMETER")

  * Invalid data sent for a parameter.
  * Data sent for parameter `%s` is not valid.



### -1131 BAD_RECV_WINDOW[​](/docs/institutional_loan/error-code#-1131-bad_recv_window "Direct link to -1131 BAD_RECV_WINDOW")

  * recvWindow must be less than 60000



### -1134 BAD_STRATEGY_TYPE[​](/docs/institutional_loan/error-code#-1134-bad_strategy_type "Direct link to -1134 BAD_STRATEGY_TYPE")

  * `strategyType` was less than 1000000.



#### -1145 INVALID_CANCEL_RESTRICTIONS[​](/docs/institutional_loan/error-code#-1145-invalid_cancel_restrictions "Direct link to -1145 INVALID_CANCEL_RESTRICTIONS")

  * `cancelRestrictions` has to be either `ONLY_NEW` or `ONLY_PARTIALLY_FILLED`.



#### -1151 DUPLICATE_SYMBOLS[​](/docs/institutional_loan/error-code#-1151-duplicate_symbols "Direct link to -1151 DUPLICATE_SYMBOLS")

  * Symbol is present multiple times in the list.



### -2010 NEW_ORDER_REJECTED[​](/docs/institutional_loan/error-code#-2010-new_order_rejected "Direct link to -2010 NEW_ORDER_REJECTED")

  * NEW_ORDER_REJECTED



### -2011 CANCEL_REJECTED[​](/docs/institutional_loan/error-code#-2011-cancel_rejected "Direct link to -2011 CANCEL_REJECTED")

  * CANCEL_REJECTED



### -2013 NO_SUCH_ORDER[​](/docs/institutional_loan/error-code#-2013-no_such_order "Direct link to -2013 NO_SUCH_ORDER")

  * Order does not exist.



### -2014 BAD_API_KEY_FMT[​](/docs/institutional_loan/error-code#-2014-bad_api_key_fmt "Direct link to -2014 BAD_API_KEY_FMT")

  * API-key format invalid.



### -2015 REJECTED_MBX_KEY[​](/docs/institutional_loan/error-code#-2015-rejected_mbx_key "Direct link to -2015 REJECTED_MBX_KEY")

  * Invalid API-key, IP, or permissions for action.



### -2016 NO_TRADING_WINDOW[​](/docs/institutional_loan/error-code#-2016-no_trading_window "Direct link to -2016 NO_TRADING_WINDOW")

  * No trading window could be found for the symbol. Try ticker/24hrs instead.



#### -2026 ORDER_ARCHIVED[​](/docs/institutional_loan/error-code#-2026-order_archived "Direct link to -2026 ORDER_ARCHIVED")

  * Order was canceled or expired with no executed qty over 90 days ago and has been archived.



## 3xxx-5xxx SAPI-specific issues[​](/docs/institutional_loan/error-code#3xxx-5xxx-sapi-specific-issues "Direct link to 3xxx-5xxx SAPI-specific issues")

### -3000 INNER_FAILURE[​](/docs/institutional_loan/error-code#-3000-inner_failure "Direct link to -3000 INNER_FAILURE")

  * Internal server error.



### -3001 NEED_ENABLE_2FA[​](/docs/institutional_loan/error-code#-3001-need_enable_2fa "Direct link to -3001 NEED_ENABLE_2FA")

  * Please enable 2FA first.



### -3002 ASSET_DEFICIENCY[​](/docs/institutional_loan/error-code#-3002-asset_deficiency "Direct link to -3002 ASSET_DEFICIENCY")

  * We don't have this asset.



### -3003 NO_OPENED_MARGIN_ACCOUNT[​](/docs/institutional_loan/error-code#-3003-no_opened_margin_account "Direct link to -3003 NO_OPENED_MARGIN_ACCOUNT")

  * Margin account does not exist.



### -3004 TRADE_NOT_ALLOWED[​](/docs/institutional_loan/error-code#-3004-trade_not_allowed "Direct link to -3004 TRADE_NOT_ALLOWED")

  * Trade not allowed.



### -3005 TRANSFER_OUT_NOT_ALLOWED[​](/docs/institutional_loan/error-code#-3005-transfer_out_not_allowed "Direct link to -3005 TRANSFER_OUT_NOT_ALLOWED")

  * Transferring out not allowed.



### -3006 EXCEED_MAX_BORROWABLE[​](/docs/institutional_loan/error-code#-3006-exceed_max_borrowable "Direct link to -3006 EXCEED_MAX_BORROWABLE")

  * Your borrow amount has exceed maximum borrow amount.



### -3007 HAS_PENDING_TRANSACTION[​](/docs/institutional_loan/error-code#-3007-has_pending_transaction "Direct link to -3007 HAS_PENDING_TRANSACTION")

  * You have pending transaction, please try again later.



### -3008 BORROW_NOT_ALLOWED[​](/docs/institutional_loan/error-code#-3008-borrow_not_allowed "Direct link to -3008 BORROW_NOT_ALLOWED")

  * Borrow not allowed.



### -3009 ASSET_NOT_MORTGAGEABLE[​](/docs/institutional_loan/error-code#-3009-asset_not_mortgageable "Direct link to -3009 ASSET_NOT_MORTGAGEABLE")

  * This asset are not allowed to transfer into margin account currently.



### -3010 REPAY_NOT_ALLOWED[​](/docs/institutional_loan/error-code#-3010-repay_not_allowed "Direct link to -3010 REPAY_NOT_ALLOWED")

  * Repay not allowed.



### -3011 BAD_DATE_RANGE[​](/docs/institutional_loan/error-code#-3011-bad_date_range "Direct link to -3011 BAD_DATE_RANGE")

  * Your input date is invalid.



### -3012 ASSET_ADMIN_BAN_BORROW[​](/docs/institutional_loan/error-code#-3012-asset_admin_ban_borrow "Direct link to -3012 ASSET_ADMIN_BAN_BORROW")

  * Borrow is banned for this asset.



### -3013 LT_MIN_BORROWABLE[​](/docs/institutional_loan/error-code#-3013-lt_min_borrowable "Direct link to -3013 LT_MIN_BORROWABLE")

  * Borrow amount less than minimum borrow amount.



### -3014 ACCOUNT_BAN_BORROW[​](/docs/institutional_loan/error-code#-3014-account_ban_borrow "Direct link to -3014 ACCOUNT_BAN_BORROW")

  * Borrow is banned for this account.



### -3015 REPAY_EXCEED_LIABILITY[​](/docs/institutional_loan/error-code#-3015-repay_exceed_liability "Direct link to -3015 REPAY_EXCEED_LIABILITY")

  * Repay amount exceeds borrow amount.



### -3016 LT_MIN_REPAY[​](/docs/institutional_loan/error-code#-3016-lt_min_repay "Direct link to -3016 LT_MIN_REPAY")

  * Repay amount less than minimum repay amount.



### -3017 ASSET_ADMIN_BAN_MORTGAGE[​](/docs/institutional_loan/error-code#-3017-asset_admin_ban_mortgage "Direct link to -3017 ASSET_ADMIN_BAN_MORTGAGE")

  * This asset are not allowed to transfer into margin account currently.



### -3018 ACCOUNT_BAN_MORTGAGE[​](/docs/institutional_loan/error-code#-3018-account_ban_mortgage "Direct link to -3018 ACCOUNT_BAN_MORTGAGE")

  * Transferring in has been banned for this account.



### -3019 ACCOUNT_BAN_ROLLOUT[​](/docs/institutional_loan/error-code#-3019-account_ban_rollout "Direct link to -3019 ACCOUNT_BAN_ROLLOUT")

  * Transferring out has been banned for this account.



### -3020 EXCEED_MAX_ROLLOUT[​](/docs/institutional_loan/error-code#-3020-exceed_max_rollout "Direct link to -3020 EXCEED_MAX_ROLLOUT")

  * Transfer out amount exceeds max amount.



### -3021 PAIR_ADMIN_BAN_TRADE[​](/docs/institutional_loan/error-code#-3021-pair_admin_ban_trade "Direct link to -3021 PAIR_ADMIN_BAN_TRADE")

  * Margin account are not allowed to trade this trading pair.



### -3022 ACCOUNT_BAN_TRADE[​](/docs/institutional_loan/error-code#-3022-account_ban_trade "Direct link to -3022 ACCOUNT_BAN_TRADE")

  * You account's trading is banned.



### -3023 WARNING_MARGIN_LEVEL[​](/docs/institutional_loan/error-code#-3023-warning_margin_level "Direct link to -3023 WARNING_MARGIN_LEVEL")

  * You can't transfer out/place order under current margin level.



### -3024 FEW_LIABILITY_LEFT[​](/docs/institutional_loan/error-code#-3024-few_liability_left "Direct link to -3024 FEW_LIABILITY_LEFT")

  * The unpaid debt is too small after this repayment.



### -3025 INVALID_EFFECTIVE_TIME[​](/docs/institutional_loan/error-code#-3025-invalid_effective_time "Direct link to -3025 INVALID_EFFECTIVE_TIME")

  * Your input date is invalid.



### -3026 VALIDATION_FAILED[​](/docs/institutional_loan/error-code#-3026-validation_failed "Direct link to -3026 VALIDATION_FAILED")

  * Your input param is invalid.



### -3027 NOT_VALID_MARGIN_ASSET[​](/docs/institutional_loan/error-code#-3027-not_valid_margin_asset "Direct link to -3027 NOT_VALID_MARGIN_ASSET")

  * Not a valid margin asset.



### -3028 NOT_VALID_MARGIN_PAIR[​](/docs/institutional_loan/error-code#-3028-not_valid_margin_pair "Direct link to -3028 NOT_VALID_MARGIN_PAIR")

  * Not a valid margin pair.



### -3029 TRANSFER_FAILED[​](/docs/institutional_loan/error-code#-3029-transfer_failed "Direct link to -3029 TRANSFER_FAILED")

  * Transfer failed.



### -3036 ACCOUNT_BAN_REPAY[​](/docs/institutional_loan/error-code#-3036-account_ban_repay "Direct link to -3036 ACCOUNT_BAN_REPAY")

  * This account is not allowed to repay.



### -3037 PNL_CLEARING[​](/docs/institutional_loan/error-code#-3037-pnl_clearing "Direct link to -3037 PNL_CLEARING")

  * PNL is clearing. Wait a second.



### -3038 LISTEN_KEY_NOT_FOUND[​](/docs/institutional_loan/error-code#-3038-listen_key_not_found "Direct link to -3038 LISTEN_KEY_NOT_FOUND")

  * Listen key not found.



### -3041 BALANCE_NOT_CLEARED[​](/docs/institutional_loan/error-code#-3041-balance_not_cleared "Direct link to -3041 BALANCE_NOT_CLEARED")

  * Balance is not enough



### -3042 PRICE_INDEX_NOT_FOUND[​](/docs/institutional_loan/error-code#-3042-price_index_not_found "Direct link to -3042 PRICE_INDEX_NOT_FOUND")

  * PriceIndex not available for this margin pair.



### -3043 TRANSFER_IN_NOT_ALLOWED[​](/docs/institutional_loan/error-code#-3043-transfer_in_not_allowed "Direct link to -3043 TRANSFER_IN_NOT_ALLOWED")

  * Transferring in not allowed.



### -3044 SYSTEM_BUSY[​](/docs/institutional_loan/error-code#-3044-system_busy "Direct link to -3044 SYSTEM_BUSY")

  * System busy.



### -3045 SYSTEM[​](/docs/institutional_loan/error-code#-3045-system "Direct link to -3045 SYSTEM")

  * The system doesn't have enough asset now.



### -3999 NOT_WHITELIST_USER[​](/docs/institutional_loan/error-code#-3999-not_whitelist_user "Direct link to -3999 NOT_WHITELIST_USER")

  * This function is only available for invited users.



### -4001 CAPITAL_INVALID[​](/docs/institutional_loan/error-code#-4001-capital_invalid "Direct link to -4001 CAPITAL_INVALID")

  * Invalid operation.



### -4002 CAPITAL_IG[​](/docs/institutional_loan/error-code#-4002-capital_ig "Direct link to -4002 CAPITAL_IG")

  * Invalid get.



### -4003 CAPITAL_IEV[​](/docs/institutional_loan/error-code#-4003-capital_iev "Direct link to -4003 CAPITAL_IEV")

  * Your input email is invalid.



### -4004 CAPITAL_UA[​](/docs/institutional_loan/error-code#-4004-capital_ua "Direct link to -4004 CAPITAL_UA")

  * You don't login or auth.



### -4005 CAPAITAL_TOO_MANY_REQUEST[​](/docs/institutional_loan/error-code#-4005-capaital_too_many_request "Direct link to -4005 CAPAITAL_TOO_MANY_REQUEST")

  * Too many new requests.



### -4006 CAPITAL_ONLY_SUPPORT_PRIMARY_ACCOUNT[​](/docs/institutional_loan/error-code#-4006-capital_only_support_primary_account "Direct link to -4006 CAPITAL_ONLY_SUPPORT_PRIMARY_ACCOUNT")

  * Support main account only.



### -4007 CAPITAL_ADDRESS_VERIFICATION_NOT_PASS[​](/docs/institutional_loan/error-code#-4007-capital_address_verification_not_pass "Direct link to -4007 CAPITAL_ADDRESS_VERIFICATION_NOT_PASS")

  * Address validation is not passed.



### -4008 CAPITAL_ADDRESS_TAG_VERIFICATION_NOT_PASS[​](/docs/institutional_loan/error-code#-4008-capital_address_tag_verification_not_pass "Direct link to -4008 CAPITAL_ADDRESS_TAG_VERIFICATION_NOT_PASS")

  * Address tag validation is not passed.



### -4010 CAPITAL_WHITELIST_EMAIL_CONFIRM[​](/docs/institutional_loan/error-code#-4010-capital_whitelist_email_confirm "Direct link to -4010 CAPITAL_WHITELIST_EMAIL_CONFIRM")

  * White list mail has been confirmed.



### -4011 CAPITAL_WHITELIST_EMAIL_EXPIRED[​](/docs/institutional_loan/error-code#-4011-capital_whitelist_email_expired "Direct link to -4011 CAPITAL_WHITELIST_EMAIL_EXPIRED")

  * White list mail is invalid.



### -4012 CAPITAL_WHITELIST_CLOSE[​](/docs/institutional_loan/error-code#-4012-capital_whitelist_close "Direct link to -4012 CAPITAL_WHITELIST_CLOSE")

  * White list is not opened.



### -4013 CAPITAL_WITHDRAW_2FA_VERIFY[​](/docs/institutional_loan/error-code#-4013-capital_withdraw_2fa_verify "Direct link to -4013 CAPITAL_WITHDRAW_2FA_VERIFY")

  * 2FA is not opened.



### -4014 CAPITAL_WITHDRAW_LOGIN_DELAY[​](/docs/institutional_loan/error-code#-4014-capital_withdraw_login_delay "Direct link to -4014 CAPITAL_WITHDRAW_LOGIN_DELAY")

  * Withdraw is not allowed within 2 min login.



### -4015 CAPITAL_WITHDRAW_RESTRICTED_MINUTE[​](/docs/institutional_loan/error-code#-4015-capital_withdraw_restricted_minute "Direct link to -4015 CAPITAL_WITHDRAW_RESTRICTED_MINUTE")

  * Withdraw is limited.



### -4016 CAPITAL_WITHDRAW_RESTRICTED_PASSWORD[​](/docs/institutional_loan/error-code#-4016-capital_withdraw_restricted_password "Direct link to -4016 CAPITAL_WITHDRAW_RESTRICTED_PASSWORD")

  * Within 24 hours after password modification, withdrawal is prohibited.



### -4017 CAPITAL_WITHDRAW_RESTRICTED_UNBIND_2FA[​](/docs/institutional_loan/error-code#-4017-capital_withdraw_restricted_unbind_2fa "Direct link to -4017 CAPITAL_WITHDRAW_RESTRICTED_UNBIND_2FA")

  * Within 24 hours after the release of 2FA, withdrawal is prohibited.



### -4018 CAPITAL_WITHDRAW_ASSET_NOT_EXIST[​](/docs/institutional_loan/error-code#-4018-capital_withdraw_asset_not_exist "Direct link to -4018 CAPITAL_WITHDRAW_ASSET_NOT_EXIST")

  * We don't have this asset.



### -4019 CAPITAL_WITHDRAW_ASSET_PROHIBIT[​](/docs/institutional_loan/error-code#-4019-capital_withdraw_asset_prohibit "Direct link to -4019 CAPITAL_WITHDRAW_ASSET_PROHIBIT")

  * Current asset is not open for withdrawal.



### -4021 CAPITAL_WITHDRAW_AMOUNT_MULTIPLE[​](/docs/institutional_loan/error-code#-4021-capital_withdraw_amount_multiple "Direct link to -4021 CAPITAL_WITHDRAW_AMOUNT_MULTIPLE")

  * Asset withdrawal must be an %s multiple of %s.



### -4022 CAPITAL_WITHDRAW_MIN_AMOUNT[​](/docs/institutional_loan/error-code#-4022-capital_withdraw_min_amount "Direct link to -4022 CAPITAL_WITHDRAW_MIN_AMOUNT")

  * Not less than the minimum pick-up quantity %s.



### -4023 CAPITAL_WITHDRAW_MAX_AMOUNT[​](/docs/institutional_loan/error-code#-4023-capital_withdraw_max_amount "Direct link to -4023 CAPITAL_WITHDRAW_MAX_AMOUNT")

  * Within 24 hours, the withdrawal exceeds the maximum amount.



### -4024 CAPITAL_WITHDRAW_USER_NO_ASSET[​](/docs/institutional_loan/error-code#-4024-capital_withdraw_user_no_asset "Direct link to -4024 CAPITAL_WITHDRAW_USER_NO_ASSET")

  * You don't have this asset.



### -4025 CAPITAL_WITHDRAW_USER_ASSET_LESS_THAN_ZERO[​](/docs/institutional_loan/error-code#-4025-capital_withdraw_user_asset_less_than_zero "Direct link to -4025 CAPITAL_WITHDRAW_USER_ASSET_LESS_THAN_ZERO")

  * The number of hold asset is less than zero.



### -4026 CAPITAL_WITHDRAW_USER_ASSET_NOT_ENOUGH[​](/docs/institutional_loan/error-code#-4026-capital_withdraw_user_asset_not_enough "Direct link to -4026 CAPITAL_WITHDRAW_USER_ASSET_NOT_ENOUGH")

  * You have insufficient balance.



### -4027 CAPITAL_WITHDRAW_GET_TRAN_ID_FAILURE[​](/docs/institutional_loan/error-code#-4027-capital_withdraw_get_tran_id_failure "Direct link to -4027 CAPITAL_WITHDRAW_GET_TRAN_ID_FAILURE")

  * Failed to obtain tranId.



### -4028 CAPITAL_WITHDRAW_MORE_THAN_FEE[​](/docs/institutional_loan/error-code#-4028-capital_withdraw_more_than_fee "Direct link to -4028 CAPITAL_WITHDRAW_MORE_THAN_FEE")

  * The amount of withdrawal must be greater than the Commission.



### -4029 CAPITAL_WITHDRAW_NOT_EXIST[​](/docs/institutional_loan/error-code#-4029-capital_withdraw_not_exist "Direct link to -4029 CAPITAL_WITHDRAW_NOT_EXIST")

  * The withdrawal record does not exist.



### -4030 CAPITAL_WITHDRAW_CONFIRM_SUCCESS[​](/docs/institutional_loan/error-code#-4030-capital_withdraw_confirm_success "Direct link to -4030 CAPITAL_WITHDRAW_CONFIRM_SUCCESS")

  * Confirmation of successful asset withdrawal.



### -4031 CAPITAL_WITHDRAW_CANCEL_FAILURE[​](/docs/institutional_loan/error-code#-4031-capital_withdraw_cancel_failure "Direct link to -4031 CAPITAL_WITHDRAW_CANCEL_FAILURE")

  * Cancellation failed.



### -4032 CAPITAL_WITHDRAW_CHECKSUM_VERIFY_FAILURE[​](/docs/institutional_loan/error-code#-4032-capital_withdraw_checksum_verify_failure "Direct link to -4032 CAPITAL_WITHDRAW_CHECKSUM_VERIFY_FAILURE")

  * Withdraw verification exception.



### -4033 CAPITAL_WITHDRAW_ILLEGAL_ADDRESS[​](/docs/institutional_loan/error-code#-4033-capital_withdraw_illegal_address "Direct link to -4033 CAPITAL_WITHDRAW_ILLEGAL_ADDRESS")

  * Illegal address.



### -4034 CAPITAL_WITHDRAW_ADDRESS_CHEAT[​](/docs/institutional_loan/error-code#-4034-capital_withdraw_address_cheat "Direct link to -4034 CAPITAL_WITHDRAW_ADDRESS_CHEAT")

  * The address is suspected of fake.



### -4035 CAPITAL_WITHDRAW_NOT_WHITE_ADDRESS[​](/docs/institutional_loan/error-code#-4035-capital_withdraw_not_white_address "Direct link to -4035 CAPITAL_WITHDRAW_NOT_WHITE_ADDRESS")

  * This address is not on the whitelist. Please join and try again.



### -4036 CAPITAL_WITHDRAW_NEW_ADDRESS[​](/docs/institutional_loan/error-code#-4036-capital_withdraw_new_address "Direct link to -4036 CAPITAL_WITHDRAW_NEW_ADDRESS")

  * The new address needs to be withdrawn in {0} hours.



### -4037 CAPITAL_WITHDRAW_RESEND_EMAIL_FAIL[​](/docs/institutional_loan/error-code#-4037-capital_withdraw_resend_email_fail "Direct link to -4037 CAPITAL_WITHDRAW_RESEND_EMAIL_FAIL")

  * Re-sending Mail failed.



### -4038 CAPITAL_WITHDRAW_RESEND_EMAIL_TIME_OUT[​](/docs/institutional_loan/error-code#-4038-capital_withdraw_resend_email_time_out "Direct link to -4038 CAPITAL_WITHDRAW_RESEND_EMAIL_TIME_OUT")

  * Please try again in 5 minutes.



### -4039 CAPITAL_USER_EMPTY[​](/docs/institutional_loan/error-code#-4039-capital_user_empty "Direct link to -4039 CAPITAL_USER_EMPTY")

  * The user does not exist.



### -4040 CAPITAL_NO_CHARGE[​](/docs/institutional_loan/error-code#-4040-capital_no_charge "Direct link to -4040 CAPITAL_NO_CHARGE")

  * This address not charged.



### -4041 CAPITAL_MINUTE_TOO_SMALL[​](/docs/institutional_loan/error-code#-4041-capital_minute_too_small "Direct link to -4041 CAPITAL_MINUTE_TOO_SMALL")

  * Please try again in one minute.



### -4042 CAPITAL_CHARGE_NOT_RESET[​](/docs/institutional_loan/error-code#-4042-capital_charge_not_reset "Direct link to -4042 CAPITAL_CHARGE_NOT_RESET")

  * This asset cannot get deposit address again.



### -4043 CAPITAL_ADDRESS_TOO_MUCH[​](/docs/institutional_loan/error-code#-4043-capital_address_too_much "Direct link to -4043 CAPITAL_ADDRESS_TOO_MUCH")

  * More than 100 recharge addresses were used in 24 hours.



### -4044 CAPITAL_BLACKLIST_COUNTRY_GET_ADDRESS[​](/docs/institutional_loan/error-code#-4044-capital_blacklist_country_get_address "Direct link to -4044 CAPITAL_BLACKLIST_COUNTRY_GET_ADDRESS")

  * This is a blacklist country.



### -4045 CAPITAL_GET_ASSET_ERROR[​](/docs/institutional_loan/error-code#-4045-capital_get_asset_error "Direct link to -4045 CAPITAL_GET_ASSET_ERROR")

  * Failure to acquire assets.



### -4046 CAPITAL_AGREEMENT_NOT_CONFIRMED[​](/docs/institutional_loan/error-code#-4046-capital_agreement_not_confirmed "Direct link to -4046 CAPITAL_AGREEMENT_NOT_CONFIRMED")

  * Agreement not confirmed.



### -4047 CAPITAL_DATE_INTERVAL_LIMIT[​](/docs/institutional_loan/error-code#-4047-capital_date_interval_limit "Direct link to -4047 CAPITAL_DATE_INTERVAL_LIMIT")

  * Time interval must be within 0-90 days



### -4060 CAPITAL_WITHDRAW_USER_ASSET_LOCK_DEPOSIT[​](/docs/institutional_loan/error-code#-4060-capital_withdraw_user_asset_lock_deposit "Direct link to -4060 CAPITAL_WITHDRAW_USER_ASSET_LOCK_DEPOSIT")

  * As your deposit has not reached the required block confirmations, we have temporarily locked {0} asset



### -4106 TAG_NOT_SUPPORTED_FOR_NETWORK[​](/docs/institutional_loan/error-code#-4106-tag_not_supported_for_network "Direct link to -4106 TAG_NOT_SUPPORTED_FOR_NETWORK")

  * This network does not support memo/tag. Please remove the `addressTag` field and try again.



### -5001 ASSET_DRIBBLET_CONVERT_SWITCH_OFF[​](/docs/institutional_loan/error-code#-5001-asset_dribblet_convert_switch_off "Direct link to -5001 ASSET_DRIBBLET_CONVERT_SWITCH_OFF")

  * Don't allow transfer to micro assets.



### -5002 ASSET_ASSET_NOT_ENOUGH[​](/docs/institutional_loan/error-code#-5002-asset_asset_not_enough "Direct link to -5002 ASSET_ASSET_NOT_ENOUGH")

  * You have insufficient balance.



### -5003 ASSET_USER_HAVE_NO_ASSET[​](/docs/institutional_loan/error-code#-5003-asset_user_have_no_asset "Direct link to -5003 ASSET_USER_HAVE_NO_ASSET")

  * You don't have this asset.



### -5004 USER_OUT_OF_TRANSFER_FLOAT[​](/docs/institutional_loan/error-code#-5004-user_out_of_transfer_float "Direct link to -5004 USER_OUT_OF_TRANSFER_FLOAT")

  * The residual balances have exceeded 0.001BTC, Please re-choose.
  * The residual balances of %s have exceeded 0.001BTC, Please re-choose.



### -5005 USER_ASSET_AMOUNT_IS_TOO_LOW[​](/docs/institutional_loan/error-code#-5005-user_asset_amount_is_too_low "Direct link to -5005 USER_ASSET_AMOUNT_IS_TOO_LOW")

  * The residual balances of the BTC is too low
  * The residual balances of %s is too low, Please re-choose.



### -5006 USER_CAN_NOT_REQUEST_IN_24_HOURS[​](/docs/institutional_loan/error-code#-5006-user_can_not_request_in_24_hours "Direct link to -5006 USER_CAN_NOT_REQUEST_IN_24_HOURS")

  * Only transfer once in 24 hours.



### -5007 AMOUNT_OVER_ZERO[​](/docs/institutional_loan/error-code#-5007-amount_over_zero "Direct link to -5007 AMOUNT_OVER_ZERO")

  * Quantity must be greater than zero.



### -5008 ASSET_WITHDRAW_WITHDRAWING_NOT_ENOUGH[​](/docs/institutional_loan/error-code#-5008-asset_withdraw_withdrawing_not_enough "Direct link to -5008 ASSET_WITHDRAW_WITHDRAWING_NOT_ENOUGH")

  * Insufficient amount of returnable assets.



### -5009 PRODUCT_NOT_EXIST[​](/docs/institutional_loan/error-code#-5009-product_not_exist "Direct link to -5009 PRODUCT_NOT_EXIST")

  * Product does not exist.



### -5010 TRANSFER_FAIL[​](/docs/institutional_loan/error-code#-5010-transfer_fail "Direct link to -5010 TRANSFER_FAIL")

  * Asset transfer fail.



### -5011 FUTURE_ACCT_NOT_EXIST[​](/docs/institutional_loan/error-code#-5011-future_acct_not_exist "Direct link to -5011 FUTURE_ACCT_NOT_EXIST")

  * future account not exists.



### -5012 TRANSFER_PENDING[​](/docs/institutional_loan/error-code#-5012-transfer_pending "Direct link to -5012 TRANSFER_PENDING")

  * Asset transfer is in pending.



### -5021 PARENT_SUB_HAVE_NO_RELATION[​](/docs/institutional_loan/error-code#-5021-parent_sub_have_no_relation "Direct link to -5021 PARENT_SUB_HAVE_NO_RELATION")

  * This parent sub have no relation



### -5012 FUTURE_ACCT_OR_SUBRELATION_NOT_EXIST[​](/docs/institutional_loan/error-code#-5012-future_acct_or_subrelation_not_exist "Direct link to -5012 FUTURE_ACCT_OR_SUBRELATION_NOT_EXIST")

  * future account or sub relation not exists.



## 6XXX - Savings Issues[​](/docs/institutional_loan/error-code#6xxx---savings-issues "Direct link to 6XXX - Savings Issues")

### -6001 DAILY_PRODUCT_NOT_EXIST[​](/docs/institutional_loan/error-code#-6001-daily_product_not_exist "Direct link to -6001 DAILY_PRODUCT_NOT_EXIST")

  * Daily product not exists.



### -6003 DAILY_PRODUCT_NOT_ACCESSIBLE[​](/docs/institutional_loan/error-code#-6003-daily_product_not_accessible "Direct link to -6003 DAILY_PRODUCT_NOT_ACCESSIBLE")

  * Product not exist or you don't have permission



### -6004 DAILY_PRODUCT_NOT_PURCHASABLE[​](/docs/institutional_loan/error-code#-6004-daily_product_not_purchasable "Direct link to -6004 DAILY_PRODUCT_NOT_PURCHASABLE")

  * Product not in purchase status



### -6005 DAILY_LOWER_THAN_MIN_PURCHASE_LIMIT[​](/docs/institutional_loan/error-code#-6005-daily_lower_than_min_purchase_limit "Direct link to -6005 DAILY_LOWER_THAN_MIN_PURCHASE_LIMIT")

  * Smaller than min purchase limit



### -6006 DAILY_REDEEM_AMOUNT_ERROR[​](/docs/institutional_loan/error-code#-6006-daily_redeem_amount_error "Direct link to -6006 DAILY_REDEEM_AMOUNT_ERROR")

  * Redeem amount error



### -6007 DAILY_REDEEM_TIME_ERROR[​](/docs/institutional_loan/error-code#-6007-daily_redeem_time_error "Direct link to -6007 DAILY_REDEEM_TIME_ERROR")

  * Not in redeem time



### -6008 DAILY_PRODUCT_NOT_REDEEMABLE[​](/docs/institutional_loan/error-code#-6008-daily_product_not_redeemable "Direct link to -6008 DAILY_PRODUCT_NOT_REDEEMABLE")

  * Product not in redeem status



### -6009 REQUEST_FREQUENCY_TOO_HIGH[​](/docs/institutional_loan/error-code#-6009-request_frequency_too_high "Direct link to -6009 REQUEST_FREQUENCY_TOO_HIGH")

  * Request frequency too high



### -6011 EXCEEDED_USER_PURCHASE_LIMIT[​](/docs/institutional_loan/error-code#-6011-exceeded_user_purchase_limit "Direct link to -6011 EXCEEDED_USER_PURCHASE_LIMIT")

  * Exceeding the maximum num allowed to purchase per user



### -6012 BALANCE_NOT_ENOUGH[​](/docs/institutional_loan/error-code#-6012-balance_not_enough "Direct link to -6012 BALANCE_NOT_ENOUGH")

  * Balance not enough



### -6013 PURCHASING_FAILED[​](/docs/institutional_loan/error-code#-6013-purchasing_failed "Direct link to -6013 PURCHASING_FAILED")

  * Purchasing failed



### -6014 UPDATE_FAILED[​](/docs/institutional_loan/error-code#-6014-update_failed "Direct link to -6014 UPDATE_FAILED")

  * Exceed up-limit allowed to purchased



### -6015 EMPTY_REQUEST_BODY[​](/docs/institutional_loan/error-code#-6015-empty_request_body "Direct link to -6015 EMPTY_REQUEST_BODY")

  * Empty request body



### -6016 PARAMS_ERR[​](/docs/institutional_loan/error-code#-6016-params_err "Direct link to -6016 PARAMS_ERR")

  * Parameter err



### -6017 NOT_IN_WHITELIST[​](/docs/institutional_loan/error-code#-6017-not_in_whitelist "Direct link to -6017 NOT_IN_WHITELIST")

  * Not in whitelist



### -6018 ASSET_NOT_ENOUGH[​](/docs/institutional_loan/error-code#-6018-asset_not_enough "Direct link to -6018 ASSET_NOT_ENOUGH")

  * Asset not enough



### -6019 PENDING[​](/docs/institutional_loan/error-code#-6019-pending "Direct link to -6019 PENDING")

  * Need confirm



### -6020 PROJECT_NOT_EXISTS[​](/docs/institutional_loan/error-code#-6020-project_not_exists "Direct link to -6020 PROJECT_NOT_EXISTS")

  * Project not exists



## 70xx - Futures[​](/docs/institutional_loan/error-code#70xx---futures "Direct link to 70xx - Futures")

### -7001 FUTURES_BAD_DATE_RANGE[​](/docs/institutional_loan/error-code#-7001-futures_bad_date_range "Direct link to -7001 FUTURES_BAD_DATE_RANGE")

  * Date range is not supported.



### -7002 FUTURES_BAD_TYPE[​](/docs/institutional_loan/error-code#-7002-futures_bad_type "Direct link to -7002 FUTURES_BAD_TYPE")

  * Data request type is not supported.



## 20xxx - Futures/Spot Algo[​](/docs/institutional_loan/error-code#20xxx---futuresspot-algo "Direct link to 20xxx - Futures/Spot Algo")

### -20121[​](/docs/institutional_loan/error-code#-20121 "Direct link to -20121")

  * Invalid symbol.



### -20124[​](/docs/institutional_loan/error-code#-20124 "Direct link to -20124")

  * Invalid algo id or it has been completed.



### -20130[​](/docs/institutional_loan/error-code#-20130 "Direct link to -20130")

  * Invalid data sent for a parameter.



### -20132[​](/docs/institutional_loan/error-code#-20132 "Direct link to -20132")

  * The client algo id is duplicated.



### -20194[​](/docs/institutional_loan/error-code#-20194 "Direct link to -20194")

  * Duration is too short to execute all required quantity.



### -20195[​](/docs/institutional_loan/error-code#-20195 "Direct link to -20195")

  * The total size is too small.



### -20196[​](/docs/institutional_loan/error-code#-20196 "Direct link to -20196")

  * The total size is too large.



### -20198[​](/docs/institutional_loan/error-code#-20198 "Direct link to -20198")

  * Reach the max open orders allowed.



### -20204[​](/docs/institutional_loan/error-code#-20204 "Direct link to -20204")

  * The notional of USD is less or more than the limit.



## Filter failures[​](/docs/institutional_loan/error-code#filter-failures "Direct link to Filter failures")

Error message| Description  
---|---  
"Filter failure: PRICE_FILTER"| `price` is too high, too low, and/or not following the tick size rule for the symbol.  
"Filter failure: PERCENT_PRICE"| `price` is X% too high or X% too low from the average weighted price over the last Y minutes.  
"Filter failure: PERCENT_PRICE_BY_SIDE"| `price` is X% too high or Y% too low from the `lastPrice` on that side (i.e. BUY/SELL)  
"Filter failure: LOT_SIZE"| `quantity` is too high, too low, and/or not following the step size rule for the symbol.  
"Filter failure: MIN_NOTIONAL"| `price` * `quantity` is too low to be a valid order for the symbol.  
"Filter failure: ICEBERG_PARTS"| `ICEBERG` order would break into too many parts; icebergQty is too small.  
"Filter failure: MARKET_LOT_SIZE"| `MARKET` order's `quantity` is too high, too low, and/or not following the step size rule for the symbol.  
"Filter failure: MAX_POSITION"| The account's position has reached the maximum defined limit.   
  
This is composed of the sum of the balance of the base asset, and the sum of the quantity of all open `BUY`orders.  
"Filter failure: MAX_NUM_ORDERS"| Account has too many open orders on the symbol.  
"Filter failure: MAX_NUM_ALGO_ORDERS"| Account has too many open stop loss and/or take profit orders on the symbol.  
"Filter failure: MAX_NUM_ICEBERG_ORDERS"| Account has too many open iceberg orders on the symbol.  
"Filter failure: TRAILING_DELTA"| `trailingDelta` is not within the defined range of the filter for that order type.  
"Filter failure: EXCHANGE_MAX_NUM_ORDERS"| Account has too many open orders on the exchange.  
"Filter failure: EXCHANGE_MAX_NUM_ALGO_ORDERS"| Account has too many open stop loss and/or take profit orders on the exchange.  
  
## 10xxx - Crypto Loans[​](/docs/institutional_loan/error-code#10xxx---crypto-loans "Direct link to 10xxx - Crypto Loans")

### -10001 SYSTEM_MAINTENANCE[​](/docs/institutional_loan/error-code#-10001-system_maintenance "Direct link to -10001 SYSTEM_MAINTENANCE")

  * The system is under maintenance, please try again later.



### -10002 INVALID_INPUT[​](/docs/institutional_loan/error-code#-10002-invalid_input "Direct link to -10002 INVALID_INPUT")

  * Invalid input parameters.



### -10005 NO_RECORDS[​](/docs/institutional_loan/error-code#-10005-no_records "Direct link to -10005 NO_RECORDS")

  * No records found.



### -10007 COIN_NOT_LOANABLE[​](/docs/institutional_loan/error-code#-10007-coin_not_loanable "Direct link to -10007 COIN_NOT_LOANABLE")

  * This coin is not loanable.



### -10008 COIN_NOT_LOANABLE[​](/docs/institutional_loan/error-code#-10008-coin_not_loanable "Direct link to -10008 COIN_NOT_LOANABLE")

  * This coin is not loanable



### -10009 COIN_NOT_COLLATERAL[​](/docs/institutional_loan/error-code#-10009-coin_not_collateral "Direct link to -10009 COIN_NOT_COLLATERAL")

  * This coin can not be used as collateral.



### -10010 COIN_NOT_COLLATERAL[​](/docs/institutional_loan/error-code#-10010-coin_not_collateral "Direct link to -10010 COIN_NOT_COLLATERAL")

  * This coin can not be used as collateral.



### -10011 INSUFFICIENT_ASSET[​](/docs/institutional_loan/error-code#-10011-insufficient_asset "Direct link to -10011 INSUFFICIENT_ASSET")

  * Insufficient spot assets.



### -10012 INVALID_AMOUNT[​](/docs/institutional_loan/error-code#-10012-invalid_amount "Direct link to -10012 INVALID_AMOUNT")

  * Invalid repayment amount.



### -10013 INSUFFICIENT_AMOUNT[​](/docs/institutional_loan/error-code#-10013-insufficient_amount "Direct link to -10013 INSUFFICIENT_AMOUNT")

  * Insufficient collateral amount.



### -10015 DEDUCTION_FAILED[​](/docs/institutional_loan/error-code#-10015-deduction_failed "Direct link to -10015 DEDUCTION_FAILED")

  * Collateral deduction failed.



### -10016 LOAN_FAILED[​](/docs/institutional_loan/error-code#-10016-loan_failed "Direct link to -10016 LOAN_FAILED")

  * Failed to provide loan.



### -10017 REPAY_EXCEED_DEBT[​](/docs/institutional_loan/error-code#-10017-repay_exceed_debt "Direct link to -10017 REPAY_EXCEED_DEBT")

  * Repayment amount exceeds debt.



### -10018 INVALID_AMOUNT[​](/docs/institutional_loan/error-code#-10018-invalid_amount "Direct link to -10018 INVALID_AMOUNT")

  * Invalid repayment amount.



### -10019 CONFIG_NOT_EXIST[​](/docs/institutional_loan/error-code#-10019-config_not_exist "Direct link to -10019 CONFIG_NOT_EXIST")

  * Configuration does not exists.



### -10020 UID_NOT_EXIST[​](/docs/institutional_loan/error-code#-10020-uid_not_exist "Direct link to -10020 UID_NOT_EXIST")

  * User ID does not exist.



### -10021 ORDER_NOT_EXIST[​](/docs/institutional_loan/error-code#-10021-order_not_exist "Direct link to -10021 ORDER_NOT_EXIST")

  * Order does not exist.



### -10022 INVALID_AMOUNT[​](/docs/institutional_loan/error-code#-10022-invalid_amount "Direct link to -10022 INVALID_AMOUNT")

  * Invalid adjustment amount.



### -10023 ADJUST_LTV_FAILED[​](/docs/institutional_loan/error-code#-10023-adjust_ltv_failed "Direct link to -10023 ADJUST_LTV_FAILED")

  * Failed to adjust LTV.



### -10024 ADJUST_LTV_NOT_SUPPORTED[​](/docs/institutional_loan/error-code#-10024-adjust_ltv_not_supported "Direct link to -10024 ADJUST_LTV_NOT_SUPPORTED")

  * LTV adjustment not supported.



### -10025 REPAY_FAILED[​](/docs/institutional_loan/error-code#-10025-repay_failed "Direct link to -10025 REPAY_FAILED")

  * Repayment failed.



### -10026 INVALID_PARAMETER[​](/docs/institutional_loan/error-code#-10026-invalid_parameter "Direct link to -10026 INVALID_PARAMETER")

  * Invalid parameter.



### -10028 INVALID_PARAMETER[​](/docs/institutional_loan/error-code#-10028-invalid_parameter "Direct link to -10028 INVALID_PARAMETER")

  * Invalid parameter.



### -10029 AMOUNT_TOO_SMALL[​](/docs/institutional_loan/error-code#-10029-amount_too_small "Direct link to -10029 AMOUNT_TOO_SMALL")

  * Loan amount is too small.



### -10030 AMOUNT_TOO_LARGE[​](/docs/institutional_loan/error-code#-10030-amount_too_large "Direct link to -10030 AMOUNT_TOO_LARGE")

  * Loan amount is too much.



### -10031 QUOTA_REACHED[​](/docs/institutional_loan/error-code#-10031-quota_reached "Direct link to -10031 QUOTA_REACHED")

  * Individual loan quota reached.



### -10032 REPAY_NOT_AVAILABLE[​](/docs/institutional_loan/error-code#-10032-repay_not_available "Direct link to -10032 REPAY_NOT_AVAILABLE")

  * Repayment is temporarily unavailable.



### -10034 REPAY_NOT_AVAILABLE[​](/docs/institutional_loan/error-code#-10034-repay_not_available "Direct link to -10034 REPAY_NOT_AVAILABLE")

  * Repay with collateral is not available currently, please try to repay with borrowed coin.



### -10039 AMOUNT_TOO_SMALL[​](/docs/institutional_loan/error-code#-10039-amount_too_small "Direct link to -10039 AMOUNT_TOO_SMALL")

  * Repayment amount is too small.



### -10040 AMOUNT_TOO_LARGE[​](/docs/institutional_loan/error-code#-10040-amount_too_large "Direct link to -10040 AMOUNT_TOO_LARGE")

  * Repayment amount is too large.



### -10041 INSUFFICIENT_AMOUNT[​](/docs/institutional_loan/error-code#-10041-insufficient_amount "Direct link to -10041 INSUFFICIENT_AMOUNT")

  * Due to high demand, there are currently insufficient loanable assets for {0}. Please adjust your borrow amount or try again tomorrow.



### -10042 ASSET_NOT_SUPPORTED[​](/docs/institutional_loan/error-code#-10042-asset_not_supported "Direct link to -10042 ASSET_NOT_SUPPORTED")

  * asset %s is not supported



### -10043 ASSET_NOT_SUPPORTED[​](/docs/institutional_loan/error-code#-10043-asset_not_supported "Direct link to -10043 ASSET_NOT_SUPPORTED")

  * {0} borrowing is currently not supported.



### -10044 QUOTA_REACHED[​](/docs/institutional_loan/error-code#-10044-quota_reached "Direct link to -10044 QUOTA_REACHED")

  * Collateral amount has reached the limit. Please reduce your collateral amount or try with other collaterals.



### -10045 COLLTERAL_REPAY_NOT_SUPPORTED[​](/docs/institutional_loan/error-code#-10045-collteral_repay_not_supported "Direct link to -10045 COLLTERAL_REPAY_NOT_SUPPORTED")

  * The loan coin does not support collateral repayment. Please try again later.



### -10046 EXCEED_MAX_ADJUSTMENT[​](/docs/institutional_loan/error-code#-10046-exceed_max_adjustment "Direct link to -10046 EXCEED_MAX_ADJUSTMENT")

  * Collateral Adjustment exceeds the maximum limit. Please try again.



### -10047 REGION_NOT_SUPPORTED[​](/docs/institutional_loan/error-code#-10047-region_not_supported "Direct link to -10047 REGION_NOT_SUPPORTED")

  * This coin is currently not supported in your location due to local regulations.



## 13xxx - BLVT[​](/docs/institutional_loan/error-code#13xxx---blvt "Direct link to 13xxx - BLVT")

### -13000 BLVT_FORBID_REDEEM[​](/docs/institutional_loan/error-code#-13000-blvt_forbid_redeem "Direct link to -13000 BLVT_FORBID_REDEEM")

  * Redeption of the token is forbiden now



### -13001 BLVT_EXCEED_DAILY_LIMIT[​](/docs/institutional_loan/error-code#-13001-blvt_exceed_daily_limit "Direct link to -13001 BLVT_EXCEED_DAILY_LIMIT")

  * Exceeds individual 24h redemption limit of the token



### -13002 BLVT_EXCEED_TOKEN_DAILY_LIMIT[​](/docs/institutional_loan/error-code#-13002-blvt_exceed_token_daily_limit "Direct link to -13002 BLVT_EXCEED_TOKEN_DAILY_LIMIT")

  * Exceeds total 24h redemption limit of the token



### -13003 BLVT_FORBID_PURCHASE[​](/docs/institutional_loan/error-code#-13003-blvt_forbid_purchase "Direct link to -13003 BLVT_FORBID_PURCHASE")

  * Subscription of the token is forbiden now



### -13004 BLVT_EXCEED_DAILY_PURCHASE_LIMIT[​](/docs/institutional_loan/error-code#-13004-blvt_exceed_daily_purchase_limit "Direct link to -13004 BLVT_EXCEED_DAILY_PURCHASE_LIMIT")

  * Exceeds individual 24h subscription limit of the token



### -13005 BLVT_EXCEED_TOKEN_DAILY_PURCHASE_LIMIT[​](/docs/institutional_loan/error-code#-13005-blvt_exceed_token_daily_purchase_limit "Direct link to -13005 BLVT_EXCEED_TOKEN_DAILY_PURCHASE_LIMIT")

  * Exceeds total 24h subscription limit of the token



### -13006 BLVT_PURCHASE_LESS_MIN_AMOUNT[​](/docs/institutional_loan/error-code#-13006-blvt_purchase_less_min_amount "Direct link to -13006 BLVT_PURCHASE_LESS_MIN_AMOUNT")

  * Subscription amount is too small



### -13007 BLVT_PURCHASE_AGREEMENT_NOT_SIGN[​](/docs/institutional_loan/error-code#-13007-blvt_purchase_agreement_not_sign "Direct link to -13007 BLVT_PURCHASE_AGREEMENT_NOT_SIGN")

  * The Agreement is not signed



## 12xxx - Liquid Swap[​](/docs/institutional_loan/error-code#12xxx---liquid-swap "Direct link to 12xxx - Liquid Swap")

### -12014 TOO MANY REQUESTS[​](/docs/institutional_loan/error-code#-12014-too-many-requests "Direct link to -12014 TOO MANY REQUESTS")

  * More than 1 request in 2 seconds




## 18xxx - Binance Code[​](/docs/institutional_loan/error-code#18xxx---binance-code "Direct link to 18xxx - Binance Code")

### -18002[​](/docs/institutional_loan/error-code#-18002 "Direct link to -18002")

  * The total amount of codes you created has exceeded the 24-hour limit, please try again after UTC 0



### -18003[​](/docs/institutional_loan/error-code#-18003 "Direct link to -18003")

  * Too many codes created in 24 hours, please try again after UTC 0



### -18004[​](/docs/institutional_loan/error-code#-18004 "Direct link to -18004")

  * Too many invalid redeem attempts in 24 hours, please try again after UTC 0



### -18005[​](/docs/institutional_loan/error-code#-18005 "Direct link to -18005")

  * Too many invalid verify attempts, please try later



### -18006[​](/docs/institutional_loan/error-code#-18006 "Direct link to -18006")

  * The amount is too small, please re-enter



### -18007[​](/docs/institutional_loan/error-code#-18007 "Direct link to -18007")

  * This token is not currently supported, please re-enter



## 21xxx - Portfolio Margin Account[​](/docs/institutional_loan/error-code#21xxx---portfolio-margin-account "Direct link to 21xxx - Portfolio Margin Account")

### -21001 USER_IS_NOT_UNIACCOUNT[​](/docs/institutional_loan/error-code#-21001-user_is_not_uniaccount "Direct link to -21001 USER_IS_NOT_UNIACCOUNT")

  * Request ID is not a Portfolio Margin Account.



### -21002 UNI_ACCOUNT_CANT_TRANSFER_FUTURE[​](/docs/institutional_loan/error-code#-21002-uni_account_cant_transfer_future "Direct link to -21002 UNI_ACCOUNT_CANT_TRANSFER_FUTURE")

  * Portfolio Margin Account doesn't support transfer from margin to futures.



### -21003 NET_ASSET_MUST_LTE_RATIO[​](/docs/institutional_loan/error-code#-21003-net_asset_must_lte_ratio "Direct link to -21003 NET_ASSET_MUST_LTE_RATIO")

  * Fail to retrieve margin assets.



### -21004 USER_NO_LIABILITY[​](/docs/institutional_loan/error-code#-21004-user_no_liability "Direct link to -21004 USER_NO_LIABILITY")

  * User doesn’t have portfolio margin bankruptcy loan



### -21005 NO_ENOUGH_ASSET[​](/docs/institutional_loan/error-code#-21005-no_enough_asset "Direct link to -21005 NO_ENOUGH_ASSET")

  * User’s spot wallet doesn’t have enough BUSD to repay portfolio margin bankruptcy loan



### -21006 HAD_IN_PROCESS_REPAY[​](/docs/institutional_loan/error-code#-21006-had_in_process_repay "Direct link to -21006 HAD_IN_PROCESS_REPAY")

  * User had portfolio margin bankruptcy loan repayment in process



### -21007 IN_FORCE_LIQUIDATION[​](/docs/institutional_loan/error-code#-21007-in_force_liquidation "Direct link to -21007 IN_FORCE_LIQUIDATION")

  * User failed to repay portfolio margin bankruptcy loan since liquidation was in process




## Order Rejection Issues[​](/docs/institutional_loan/error-code#order-rejection-issues "Direct link to Order Rejection Issues")

Error messages like these are indicated when the error is coming specifically from the matching engine:

  * `-1010 ERROR_MSG_RECEIVED`
  * `-2010 NEW_ORDER_REJECTED`
  * `-2011 CANCEL_REJECTED`



The following messages which will indicate the specific error:

Error message| Description  
---|---  
"Unknown order sent."| The order (by either `orderId`, `clientOrderId`, `origClientOrderId`) could not be found.  
"Duplicate order sent."| The `clientOrderId` is already in use.  
"Market is closed."| The symbol is not trading.  
"Account has insufficient balance for requested action."| Not enough funds to complete the action.  
"Market orders are not supported for this symbol."| `MARKET` is not enabled on the symbol.  
"Iceberg orders are not supported for this symbol."| `icebergQty` is not enabled on the symbol  
"Stop loss orders are not supported for this symbol."| `STOP_LOSS` is not enabled on the symbol  
"Stop loss limit orders are not supported for this symbol."| `STOP_LOSS_LIMIT` is not enabled on the symbol  
"Take profit orders are not supported for this symbol."| `TAKE_PROFIT` is not enabled on the symbol  
"Take profit limit orders are not supported for this symbol."| `TAKE_PROFIT_LIMIT` is not enabled on the symbol  
"Price * QTY is zero or less."| `price` * `quantity` is too low  
"IcebergQty exceeds QTY."| `icebergQty` must be less than the order quantity  
"This action is disabled on this account."| Contact customer support; some actions have been disabled on the account.  
"This account may not place or cancel orders."| Contact customer support; the account has trading ability disabled.  
"Unsupported order combination"| The `orderType`, `timeInForce`, `stopPrice`, and/or `icebergQty` combination isn't allowed.  
"Order would trigger immediately."| The order's stop price is not valid when compared to the last traded price.  
"Cancel order is invalid. Check origClientOrderId and orderId."| No `origClientOrderId` or `orderId` was sent in.  
"Order would immediately match and take."| `LIMIT_MAKER` order type would immediately match and trade, and not be a pure maker order.  
"The relationship of the prices for the orders is not correct."| The prices set in the `OCO` is breaking the Price rules.   
  
The rules are:   
  
`SELL Orders`: Limit Price > Last Price > Stop Price   
  
`BUY Orders`: Limit Price < Last Price < Stop Price  
"OCO orders are not supported for this symbol"| `OCO` is not enabled on the symbol.  
"Quote order qty market orders are not support for this symbol."| `MARKET` orders using the parameter `quoteOrderQty` are not enabled on this symbol.  
"Trailing stop orders are not supported for this symbol."| Orders using `trailingDelta` are not enabled on the symbol.  
"Order cancel-replace is not supported for this symbol."| `POST /api/v3/order/cancelReplace` (REST API) or `order.cancelReplace` (WebSocket API) is on enabled the symbol.  
"This symbol is not permitted for this account."| Account and symbol do not have the same permissions. (e.g. `SPOT`, `MARGIN`, etc)  
"This symbol is restricted for this account."| Account is unable to trade on that symbol. (e.g. An `ISOLATED_MARGIN` account cannot place `SPOT` orders.)  
"Order was not canceled due to cancel restrictions."| Either `cancelRestrictions` was set to `ONLY_NEW` but the order status was not `NEW`   
or   
`cancelRestrictions` was set to `ONLY_PARTIALLY_FILLED` but the order status was not `PARTIALLY_FILLED`.  
  
## Errors regarding POST /api/v3/order/cancelReplace[​](/docs/institutional_loan/error-code#errors-regarding-post-apiv3ordercancelreplace "Direct link to Errors regarding POST /api/v3/order/cancelReplace")

### -2021 Order cancel-replace partially failed[​](/docs/institutional_loan/error-code#-2021-order-cancel-replace-partially-failed "Direct link to -2021 Order cancel-replace partially failed")

This code is sent when either the cancellation of the order failed or the new order placement failed but not both.

### -2022 Order cancel-replace failed.[​](/docs/institutional_loan/error-code#-2022-order-cancel-replace-failed "Direct link to -2022 Order cancel-replace failed.")

This code is sent when both the cancellation of the order failed and the new order placement failed.

---

# 错误代码

> 错误JSON格式:
    
    
    {  
      "code":-1121,  
      "msg":"Invalid symbol."  
    }  
    

错误由两部分组成：错误代码和消息。 代码是通用的，但是消息可能会有所不同。

## 10xx -常规服务器或网络问题[​](/docs/zh-CN/institutional_loan/error-code#10xx--常规服务器或网络问题 "10xx -常规服务器或网络问题的直接链接")

### -1000 UNKNOWN[​](/docs/zh-CN/institutional_loan/error-code#-1000-unknown "-1000 UNKNOWN的直接链接")

  * 处理请求时发生未知错误。
  * 处理请求时发生未知错误。[%s]



### -1001 DISCONNECTED[​](/docs/zh-CN/institutional_loan/error-code#-1001-disconnected "-1001 DISCONNECTED的直接链接")

  * 内部错误; 无法处理您的请求。 请再试一次.



### -1002 UNAUTHORIZED[​](/docs/zh-CN/institutional_loan/error-code#-1002-unauthorized "-1002 UNAUTHORIZED的直接链接")

  * 您无权执行此请求。



### -1003 TOO_MANY_REQUESTS[​](/docs/zh-CN/institutional_loan/error-code#-1003-too_many_requests "-1003 TOO_MANY_REQUESTS的直接链接")

  * 排队的请求过多。
  * 请求权重过多； 当前限制是 %s 每 %s 的请求权重。 请使用 Websocket Streams 进行实时更新，以避免轮询API。
  * 请求权重过多； IP被禁止，直到％s。 请使用 Websocket Streams 进行实时更新，以免被禁。



### -1004 SERVER_BUSY[​](/docs/zh-CN/institutional_loan/error-code#-1004-server_busy "-1004 SERVER_BUSY的直接链接")

  * 服务器正忙，请稍候再试。



### -1006 UNEXPECTED_RESP[​](/docs/zh-CN/institutional_loan/error-code#-1006-unexpected_resp "-1006 UNEXPECTED_RESP的直接链接")

  * 从消息总线收到意外的响应。 执行状态未知。



### -1007 TIMEOUT[​](/docs/zh-CN/institutional_loan/error-code#-1007-timeout "-1007 TIMEOUT的直接链接")

  * 等待后端服务器响应超时。 发送状态未知； 执行状态未知。



### -1008 SERVER_BUSY[​](/docs/zh-CN/institutional_loan/error-code#-1008-server_busy "-1008 SERVER_BUSY的直接链接")

  * 现货交易服务器当前因其他请求而过载。 请在几分钟后重试。



### -1014 UNKNOWN_ORDER_COMPOSITION[​](/docs/zh-CN/institutional_loan/error-code#-1014-unknown_order_composition "-1014 UNKNOWN_ORDER_COMPOSITION的直接链接")

  * 不支持的订单组合。



### -1015 TOO_MANY_ORDERS[​](/docs/zh-CN/institutional_loan/error-code#-1015-too_many_orders "-1015 TOO_MANY_ORDERS的直接链接")

  * 新订单太多。
  * 新订单太多； 当前限制为每％s ％s个订单。



### -1016 SERVICE_SHUTTING_DOWN[​](/docs/zh-CN/institutional_loan/error-code#-1016-service_shutting_down "-1016 SERVICE_SHUTTING_DOWN的直接链接")

  * 该服务不可用。



### -1020 UNSUPPORTED_OPERATION[​](/docs/zh-CN/institutional_loan/error-code#-1020-unsupported_operation "-1020 UNSUPPORTED_OPERATION的直接链接")

  * 不支持此操作。



### -1021 INVALID_TIMESTAMP[​](/docs/zh-CN/institutional_loan/error-code#-1021-invalid_timestamp "-1021 INVALID_TIMESTAMP的直接链接")

  * 此请求的时间戳在recvWindow之外。
  * 此请求的时间戳比服务器时间提前1000毫秒。



### -1022 INVALID_SIGNATURE[​](/docs/zh-CN/institutional_loan/error-code#-1022-invalid_signature "-1022 INVALID_SIGNATURE的直接链接")

  * 此请求的签名无效。



### -1099 Not found, authenticated, or authorized[​](/docs/zh-CN/institutional_loan/error-code#-1099-not-found-authenticated-or-authorized "-1099 Not found, authenticated, or authorized的直接链接")

  * 替换错误代码-1999



## 11xx - 2xxx Request issues[​](/docs/zh-CN/institutional_loan/error-code#11xx---2xxx-request-issues "11xx - 2xxx Request issues的直接链接")

### -1100 ILLEGAL_CHARS[​](/docs/zh-CN/institutional_loan/error-code#-1100-illegal_chars "-1100 ILLEGAL_CHARS的直接链接")

  * 在参数中发现非法字符。
  * 在参数中发现非法字符。`％s`
  * 在参数`％s`中发现非法字符； 合法范围是`％s`。



### -1101 TOO_MANY_PARAMETERS[​](/docs/zh-CN/institutional_loan/error-code#-1101-too_many_parameters "-1101 TOO_MANY_PARAMETERS的直接链接")

  * 为此端点发送的参数太多。
  * 参数太多； 预期为`％s`并收到了`％s`。
  * 检测到的参数值重复。



### -1102 MANDATORY_PARAM_EMPTY_OR_MALFORMED[​](/docs/zh-CN/institutional_loan/error-code#-1102-mandatory_param_empty_or_malformed "-1102 MANDATORY_PARAM_EMPTY_OR_MALFORMED的直接链接")

  * 未发送强制性参数，该参数为空/空或格式错误。
  * 强制参数`％s`未发送，为空/空或格式错误。
  * 必须发送参数`％s`或`％s`，但两者均为空！



### -1103 UNKNOWN_PARAM[​](/docs/zh-CN/institutional_loan/error-code#-1103-unknown_param "-1103 UNKNOWN_PARAM的直接链接")

  * 发送了未知参数。



### -1104 UNREAD_PARAMETERS[​](/docs/zh-CN/institutional_loan/error-code#-1104-unread_parameters "-1104 UNREAD_PARAMETERS的直接链接")

  * 并非所有发送的参数都被读取。
  * 并非所有发送的参数都被读取； 读取了`％s`参数，但被发送了`％s`。



### -1105 PARAM_EMPTY[​](/docs/zh-CN/institutional_loan/error-code#-1105-param_empty "-1105 PARAM_EMPTY的直接链接")

  * 参数为空。
  * 参数`％s`为空。



### -1106 PARAM_NOT_REQUIRED[​](/docs/zh-CN/institutional_loan/error-code#-1106-param_not_required "-1106 PARAM_NOT_REQUIRED的直接链接")

  * 不需要时已发送参数。
  * 不需要时发送参数`％s`。



### -1111 BAD_PRECISION[​](/docs/zh-CN/institutional_loan/error-code#-1111-bad_precision "-1111 BAD_PRECISION的直接链接")

  * 精度超过为此资产定义的最大值。



### -1112 NO_DEPTH[​](/docs/zh-CN/institutional_loan/error-code#-1112-no_depth "-1112 NO_DEPTH的直接链接")

  * 交易对没有挂单。



### -1114 TIF_NOT_REQUIRED[​](/docs/zh-CN/institutional_loan/error-code#-1114-tif_not_required "-1114 TIF_NOT_REQUIRED的直接链接")

  * 不需要时发送了TimeInForce参数。



### -1115 INVALID_TIF[​](/docs/zh-CN/institutional_loan/error-code#-1115-invalid_tif "-1115 INVALID_TIF的直接链接")

  * 无效 timeInForce.



### -1116 INVALID_ORDER_TYPE[​](/docs/zh-CN/institutional_loan/error-code#-1116-invalid_order_type "-1116 INVALID_ORDER_TYPE的直接链接")

  * 无效订单类型。



### -1117 INVALID_SIDE[​](/docs/zh-CN/institutional_loan/error-code#-1117-invalid_side "-1117 INVALID_SIDE的直接链接")

  * 无效买卖方向。



### -1118 EMPTY_NEW_CL_ORD_ID[​](/docs/zh-CN/institutional_loan/error-code#-1118-empty_new_cl_ord_id "-1118 EMPTY_NEW_CL_ORD_ID的直接链接")

  * 新的客户订单ID为空。



### -1119 EMPTY_ORG_CL_ORD_ID[​](/docs/zh-CN/institutional_loan/error-code#-1119-empty_org_cl_ord_id "-1119 EMPTY_ORG_CL_ORD_ID的直接链接")

  * 客户自定义的订单ID为空。



### -1120 BAD_INTERVAL[​](/docs/zh-CN/institutional_loan/error-code#-1120-bad_interval "-1120 BAD_INTERVAL的直接链接")

  * 无效时间间隔。



### -1121 BAD_SYMBOL[​](/docs/zh-CN/institutional_loan/error-code#-1121-bad_symbol "-1121 BAD_SYMBOL的直接链接")

  * 无效的交易对。



### -1125 INVALID_LISTEN_KEY[​](/docs/zh-CN/institutional_loan/error-code#-1125-invalid_listen_key "-1125 INVALID_LISTEN_KEY的直接链接")

  * 该listenKey不存在。



### -1127 MORE_THAN_XX_HOURS[​](/docs/zh-CN/institutional_loan/error-code#-1127-more_than_xx_hours "-1127 MORE_THAN_XX_HOURS的直接链接")

  * 查询间隔太大。
  * 从开始时间到结束时间之间超过％s小时。



### -1128 OPTIONAL_PARAMS_BAD_COMBO[​](/docs/zh-CN/institutional_loan/error-code#-1128-optional_params_bad_combo "-1128 OPTIONAL_PARAMS_BAD_COMBO的直接链接")

  * 可选参数组合无效。



### -1130 INVALID_PARAMETER[​](/docs/zh-CN/institutional_loan/error-code#-1130-invalid_parameter "-1130 INVALID_PARAMETER的直接链接")

  * 发送的参数为无效数据。
  * 发送参数`％s`的数据无效。



### -1131 BAD_RECV_WINDOW[​](/docs/zh-CN/institutional_loan/error-code#-1131-bad_recv_window "-1131 BAD_RECV_WINDOW的直接链接")

  * `recvWindow` 必须小于 60000



### -1134 BAD_STRATEGY_TYPE[​](/docs/zh-CN/institutional_loan/error-code#-1134-bad_strategy_type "-1134 BAD_STRATEGY_TYPE的直接链接")

  * `strategyType` 必须小于 1000000



#### -1145 INVALID_CANCEL_RESTRICTIONS[​](/docs/zh-CN/institutional_loan/error-code#-1145-invalid_cancel_restrictions "-1145 INVALID_CANCEL_RESTRICTIONS的直接链接")

  * `cancelRestrictions` 必须是 `ONLY_NEW` 或者 `ONLY_PARTIALLY_FILLED`。



#### -1151 重复的交易对[​](/docs/zh-CN/institutional_loan/error-code#-1151-重复的交易对 "-1151 重复的交易对的直接链接")

  * Symbol is present multiple times in the list.



### -2010 NEW_ORDER_REJECTED[​](/docs/zh-CN/institutional_loan/error-code#-2010-new_order_rejected "-2010 NEW_ORDER_REJECTED的直接链接")

  * 新订单被拒绝



### -2011 CANCEL_REJECTED[​](/docs/zh-CN/institutional_loan/error-code#-2011-cancel_rejected "-2011 CANCEL_REJECTED的直接链接")

  * 取消订单被拒绝



### -2013 NO_SUCH_ORDER[​](/docs/zh-CN/institutional_loan/error-code#-2013-no_such_order "-2013 NO_SUCH_ORDER的直接链接")

  * 订单不存在。



### -2014 BAD_API_KEY_FMT[​](/docs/zh-CN/institutional_loan/error-code#-2014-bad_api_key_fmt "-2014 BAD_API_KEY_FMT的直接链接")

  * API-key 格式无效。



### -2015 REJECTED_MBX_KEY[​](/docs/zh-CN/institutional_loan/error-code#-2015-rejected_mbx_key "-2015 REJECTED_MBX_KEY的直接链接")

  * 无效的API密钥，IP或操作权限。



### -2016 NO_TRADING_WINDOW[​](/docs/zh-CN/institutional_loan/error-code#-2016-no_trading_window "-2016 NO_TRADING_WINDOW的直接链接")

  * 找不到该交易对的交易窗口。 尝试改为24小时自动报价。



#### -2026 ORDER_ARCHIVED[​](/docs/zh-CN/institutional_loan/error-code#-2026-order_archived "-2026 ORDER_ARCHIVED的直接链接")

  * 订单已被存档因为此订单被取消或过期，无交易数量而最后的更新已超过 90 天前。



## 3xxx-5xxx SAPI 具体问题[​](/docs/zh-CN/institutional_loan/error-code#3xxx-5xxx-sapi-具体问题 "3xxx-5xxx SAPI 具体问题的直接链接")

### -3000 INNER_FAILURE[​](/docs/zh-CN/institutional_loan/error-code#-3000-inner_failure "-3000 INNER_FAILURE的直接链接")

  * 内部服务器错误。



### -3001 NEED_ENABLE_2FA[​](/docs/zh-CN/institutional_loan/error-code#-3001-need_enable_2fa "-3001 NEED_ENABLE_2FA的直接链接")

  * 请先启用2FA。



### -3002 ASSET_DEFICIENCY[​](/docs/zh-CN/institutional_loan/error-code#-3002-asset_deficiency "-3002 ASSET_DEFICIENCY的直接链接")

  * 此资产不存在。



### -3003 NO_OPENED_MARGIN_ACCOUNT[​](/docs/zh-CN/institutional_loan/error-code#-3003-no_opened_margin_account "-3003 NO_OPENED_MARGIN_ACCOUNT的直接链接")

  * 杠杆账户不存在。



### -3004 TRADE_NOT_ALLOWED[​](/docs/zh-CN/institutional_loan/error-code#-3004-trade_not_allowed "-3004 TRADE_NOT_ALLOWED的直接链接")

  * 禁止交易。



### -3005 TRANSFER_OUT_NOT_ALLOWED[​](/docs/zh-CN/institutional_loan/error-code#-3005-transfer_out_not_allowed "-3005 TRANSFER_OUT_NOT_ALLOWED的直接链接")

  * 不允许转账。



### -3006 EXCEED_MAX_BORROWABLE[​](/docs/zh-CN/institutional_loan/error-code#-3006-exceed_max_borrowable "-3006 EXCEED_MAX_BORROWABLE的直接链接")

  * 您的已借金额已超过最高可借金额。



### -3007 HAS_PENDING_TRANSACTION[​](/docs/zh-CN/institutional_loan/error-code#-3007-has_pending_transaction "-3007 HAS_PENDING_TRANSACTION的直接链接")

  * 您有待处理的交易，请稍后再试。



### -3008 BORROW_NOT_ALLOWED[​](/docs/zh-CN/institutional_loan/error-code#-3008-borrow_not_allowed "-3008 BORROW_NOT_ALLOWED的直接链接")

  * 不允许借款。



### -3009 ASSET_NOT_MORTGAGEABLE[​](/docs/zh-CN/institutional_loan/error-code#-3009-asset_not_mortgageable "-3009 ASSET_NOT_MORTGAGEABLE的直接链接")

  * 此资产目前不允许转入杠杆账户。



### -3010 REPAY_NOT_ALLOWED[​](/docs/zh-CN/institutional_loan/error-code#-3010-repay_not_allowed "-3010 REPAY_NOT_ALLOWED的直接链接")

  * 不允许还款。



### -3011 BAD_DATE_RANGE[​](/docs/zh-CN/institutional_loan/error-code#-3011-bad_date_range "-3011 BAD_DATE_RANGE的直接链接")

  * 您输入的日期无效。



### -3012 ASSET_ADMIN_BAN_BORROW[​](/docs/zh-CN/institutional_loan/error-code#-3012-asset_admin_ban_borrow "-3012 ASSET_ADMIN_BAN_BORROW的直接链接")

  * 此资产禁止借款。



### -3013 LT_MIN_BORROWABLE[​](/docs/zh-CN/institutional_loan/error-code#-3013-lt_min_borrowable "-3013 LT_MIN_BORROWABLE的直接链接")

  * 借入金额少于最低借入金额。



### -3014 ACCOUNT_BAN_BORROW[​](/docs/zh-CN/institutional_loan/error-code#-3014-account_ban_borrow "-3014 ACCOUNT_BAN_BORROW的直接链接")

  * 此帐户禁止借款。



### -3015 REPAY_EXCEED_LIABILITY[​](/docs/zh-CN/institutional_loan/error-code#-3015-repay_exceed_liability "-3015 REPAY_EXCEED_LIABILITY的直接链接")

  * 还款额超过借款额。



### -3016 LT_MIN_REPAY[​](/docs/zh-CN/institutional_loan/error-code#-3016-lt_min_repay "-3016 LT_MIN_REPAY的直接链接")

  * 还款额少于最低还款额。



### -3017 ASSET_ADMIN_BAN_MORTGAGE[​](/docs/zh-CN/institutional_loan/error-code#-3017-asset_admin_ban_mortgage "-3017 ASSET_ADMIN_BAN_MORTGAGE的直接链接")

  * 此资产目前不允许转入保证金账户。



### -3018 ACCOUNT_BAN_MORTGAGE[​](/docs/zh-CN/institutional_loan/error-code#-3018-account_ban_mortgage "-3018 ACCOUNT_BAN_MORTGAGE的直接链接")

  * 此帐户已禁止转入。



### -3019 ACCOUNT_BAN_ROLLOUT[​](/docs/zh-CN/institutional_loan/error-code#-3019-account_ban_rollout "-3019 ACCOUNT_BAN_ROLLOUT的直接链接")

  * 此帐户禁止转出。



### -3020 EXCEED_MAX_ROLLOUT[​](/docs/zh-CN/institutional_loan/error-code#-3020-exceed_max_rollout "-3020 EXCEED_MAX_ROLLOUT的直接链接")

  * 转出金额超过上限。



### -3021 PAIR_ADMIN_BAN_TRADE[​](/docs/zh-CN/institutional_loan/error-code#-3021-pair_admin_ban_trade "-3021 PAIR_ADMIN_BAN_TRADE的直接链接")

  * 杠杆账户无法交易此交易对。



### -3022 ACCOUNT_BAN_TRADE[​](/docs/zh-CN/institutional_loan/error-code#-3022-account_ban_trade "-3022 ACCOUNT_BAN_TRADE的直接链接")

  * 账号被禁止交易。



### -3023 WARNING_MARGIN_LEVEL[​](/docs/zh-CN/institutional_loan/error-code#-3023-warning_margin_level "-3023 WARNING_MARGIN_LEVEL的直接链接")

  * 无法在当前杠杆倍数下转出资金或者下单



### -3024 FEW_LIABILITY_LEFT[​](/docs/zh-CN/institutional_loan/error-code#-3024-few_liability_left "-3024 FEW_LIABILITY_LEFT的直接链接")

  * 付款之后未付款的债务太小



### -3025 INVALID_EFFECTIVE_TIME[​](/docs/zh-CN/institutional_loan/error-code#-3025-invalid_effective_time "-3025 INVALID_EFFECTIVE_TIME的直接链接")

  * 输入时间有误。



### -3026 VALIDATION_FAILED[​](/docs/zh-CN/institutional_loan/error-code#-3026-validation_failed "-3026 VALIDATION_FAILED的直接链接")

  * 输入参数有误。



### -3027 NOT_VALID_MARGIN_ASSET[​](/docs/zh-CN/institutional_loan/error-code#-3027-not_valid_margin_asset "-3027 NOT_VALID_MARGIN_ASSET的直接链接")

  * 无效的杠杆资产。



### -3028 NOT_VALID_MARGIN_PAIR[​](/docs/zh-CN/institutional_loan/error-code#-3028-not_valid_margin_pair "-3028 NOT_VALID_MARGIN_PAIR的直接链接")

  * 无效的杠杆交易对。



### -3029 TRANSFER_FAILED[​](/docs/zh-CN/institutional_loan/error-code#-3029-transfer_failed "-3029 TRANSFER_FAILED的直接链接")

  * 转账失败。



### -3036 ACCOUNT_BAN_REPAY[​](/docs/zh-CN/institutional_loan/error-code#-3036-account_ban_repay "-3036 ACCOUNT_BAN_REPAY的直接链接")

  * 此账号无法还款。



### -3037 PNL_CLEARING[​](/docs/zh-CN/institutional_loan/error-code#-3037-pnl_clearing "-3037 PNL_CLEARING的直接链接")

  * `PNL`正在清帐，请稍等。



### -3038 LISTEN_KEY_NOT_FOUND[​](/docs/zh-CN/institutional_loan/error-code#-3038-listen_key_not_found "-3038 LISTEN_KEY_NOT_FOUND的直接链接")

  * 找不到`Listen key`



### -3041 BALANCE_NOT_CLEARED[​](/docs/zh-CN/institutional_loan/error-code#-3041-balance_not_cleared "-3041 BALANCE_NOT_CLEARED的直接链接")

  * 余额不足



### -3042 PRICE_INDEX_NOT_FOUND[​](/docs/zh-CN/institutional_loan/error-code#-3042-price_index_not_found "-3042 PRICE_INDEX_NOT_FOUND的直接链接")

  * 该杠杆交易对无可用价格指数。



### -3043 TRANSFER_IN_NOT_ALLOWED[​](/docs/zh-CN/institutional_loan/error-code#-3043-transfer_in_not_allowed "-3043 TRANSFER_IN_NOT_ALLOWED的直接链接")

  * 不允许转入。



### -3044 SYSTEM_BUSY[​](/docs/zh-CN/institutional_loan/error-code#-3044-system_busy "-3044 SYSTEM_BUSY的直接链接")

  * 系统繁忙。



### -3045 SYSTEM[​](/docs/zh-CN/institutional_loan/error-code#-3045-system "-3045 SYSTEM的直接链接")

  * 系统目前没有足够可借的资产。



### -3999 NOT_WHITELIST_USER[​](/docs/zh-CN/institutional_loan/error-code#-3999-not_whitelist_user "-3999 NOT_WHITELIST_USER的直接链接")

  * 此功能只面向邀请的用户。



### -4001 CAPITAL_INVALID[​](/docs/zh-CN/institutional_loan/error-code#-4001-capital_invalid "-4001 CAPITAL_INVALID的直接链接")

  * 非法操作



### -4002 CAPITAL_IG[​](/docs/zh-CN/institutional_loan/error-code#-4002-capital_ig "-4002 CAPITAL_IG的直接链接")

  * 非法获取



### -4003 CAPITAL_IEV[​](/docs/zh-CN/institutional_loan/error-code#-4003-capital_iev "-4003 CAPITAL_IEV的直接链接")

  * 非法邮箱验证



### -4004 CAPITAL_UA[​](/docs/zh-CN/institutional_loan/error-code#-4004-capital_ua "-4004 CAPITAL_UA的直接链接")

  * 未登录或者认证。



### -4005 CAPAITAL_TOO_MANY_REQUEST[​](/docs/zh-CN/institutional_loan/error-code#-4005-capaital_too_many_request "-4005 CAPAITAL_TOO_MANY_REQUEST的直接链接")

  * 请求太频繁。



### -4006 CAPITAL_ONLY_SUPPORT_PRIMARY_ACCOUNT[​](/docs/zh-CN/institutional_loan/error-code#-4006-capital_only_support_primary_account "-4006 CAPITAL_ONLY_SUPPORT_PRIMARY_ACCOUNT的直接链接")

  * 只支持主账号。



### -4007 CAPITAL_ADDRESS_VERIFICATION_NOT_PASS[​](/docs/zh-CN/institutional_loan/error-code#-4007-capital_address_verification_not_pass "-4007 CAPITAL_ADDRESS_VERIFICATION_NOT_PASS的直接链接")

  * 地址的没有通过校验。



### -4008 CAPITAL_ADDRESS_TAG_VERIFICATION_NOT_PASS[​](/docs/zh-CN/institutional_loan/error-code#-4008-capital_address_tag_verification_not_pass "-4008 CAPITAL_ADDRESS_TAG_VERIFICATION_NOT_PASS的直接链接")

  * 地址的标记信息(`tag`)没有通过校验。



### -4010 CAPITAL_WHITELIST_EMAIL_CONFIRM[​](/docs/zh-CN/institutional_loan/error-code#-4010-capital_whitelist_email_confirm "-4010 CAPITAL_WHITELIST_EMAIL_CONFIRM的直接链接")

  * 确认电子邮件已经列入白名单。



### -4011 CAPITAL_WHITELIST_EMAIL_EXPIRED[​](/docs/zh-CN/institutional_loan/error-code#-4011-capital_whitelist_email_expired "-4011 CAPITAL_WHITELIST_EMAIL_EXPIRED的直接链接")

  * 列入白名单的电子邮件无效。



### -4012 CAPITAL_WHITELIST_CLOSE[​](/docs/zh-CN/institutional_loan/error-code#-4012-capital_whitelist_close "-4012 CAPITAL_WHITELIST_CLOSE的直接链接")

  * 白名单未打开。



### -4013 CAPITAL_WITHDRAW_2FA_VERIFY[​](/docs/zh-CN/institutional_loan/error-code#-4013-capital_withdraw_2fa_verify "-4013 CAPITAL_WITHDRAW_2FA_VERIFY的直接链接")

  * 2FA未打开。



### -4014 CAPITAL_WITHDRAW_LOGIN_DELAY[​](/docs/zh-CN/institutional_loan/error-code#-4014-capital_withdraw_login_delay "-4014 CAPITAL_WITHDRAW_LOGIN_DELAY的直接链接")

  * 在登录后的2分钟之内不允许提款。



### -4015 CAPITAL_WITHDRAW_RESTRICTED_MINUTE[​](/docs/zh-CN/institutional_loan/error-code#-4015-capital_withdraw_restricted_minute "-4015 CAPITAL_WITHDRAW_RESTRICTED_MINUTE的直接链接")

  * 暂停提款



### -4016 CAPITAL_WITHDRAW_RESTRICTED_PASSWORD[​](/docs/zh-CN/institutional_loan/error-code#-4016-capital_withdraw_restricted_password "-4016 CAPITAL_WITHDRAW_RESTRICTED_PASSWORD的直接链接")

  * 在密码修改后的24小时之内不允许提款。



### -4017 CAPITAL_WITHDRAW_RESTRICTED_UNBIND_2FA[​](/docs/zh-CN/institutional_loan/error-code#-4017-capital_withdraw_restricted_unbind_2fa "-4017 CAPITAL_WITHDRAW_RESTRICTED_UNBIND_2FA的直接链接")

  * 在2FA发行后的24小时之内不允许提款。



### -4018 CAPITAL_WITHDRAW_ASSET_NOT_EXIST[​](/docs/zh-CN/institutional_loan/error-code#-4018-capital_withdraw_asset_not_exist "-4018 CAPITAL_WITHDRAW_ASSET_NOT_EXIST的直接链接")

  * 此资产不存在。



### -4019 CAPITAL_WITHDRAW_ASSET_PROHIBIT[​](/docs/zh-CN/institutional_loan/error-code#-4019-capital_withdraw_asset_prohibit "-4019 CAPITAL_WITHDRAW_ASSET_PROHIBIT的直接链接")

  * 此资产不允许提款。



### -4021 CAPITAL_WITHDRAW_AMOUNT_MULTIPLE[​](/docs/zh-CN/institutional_loan/error-code#-4021-capital_withdraw_amount_multiple "-4021 CAPITAL_WITHDRAW_AMOUNT_MULTIPLE的直接链接")

  * 资产的提款数量必须是％s的％s倍。



### -4022 CAPITAL_WITHDRAW_MIN_AMOUNT[​](/docs/zh-CN/institutional_loan/error-code#-4022-capital_withdraw_min_amount "-4022 CAPITAL_WITHDRAW_MIN_AMOUNT的直接链接")

  * 不须少于最低的提款数量％s。



### -4023 CAPITAL_WITHDRAW_MAX_AMOUNT[​](/docs/zh-CN/institutional_loan/error-code#-4023-capital_withdraw_max_amount "-4023 CAPITAL_WITHDRAW_MAX_AMOUNT的直接链接")

  * 在24小时之内，不须超过最高的提款数量。



### -4024 CAPITAL_WITHDRAW_USER_NO_ASSET[​](/docs/zh-CN/institutional_loan/error-code#-4024-capital_withdraw_user_no_asset "-4024 CAPITAL_WITHDRAW_USER_NO_ASSET的直接链接")

  * 当前用户没有此资产。



### -4025 CAPITAL_WITHDRAW_USER_ASSET_LESS_THAN_ZERO[​](/docs/zh-CN/institutional_loan/error-code#-4025-capital_withdraw_user_asset_less_than_zero "-4025 CAPITAL_WITHDRAW_USER_ASSET_LESS_THAN_ZERO的直接链接")

  * 持有资产的数量小于零。



### -4026 CAPITAL_WITHDRAW_USER_ASSET_NOT_ENOUGH[​](/docs/zh-CN/institutional_loan/error-code#-4026-capital_withdraw_user_asset_not_enough "-4026 CAPITAL_WITHDRAW_USER_ASSET_NOT_ENOUGH的直接链接")

  * 此资产余额不足。



### -4027 CAPITAL_WITHDRAW_GET_TRAN_ID_FAILURE[​](/docs/zh-CN/institutional_loan/error-code#-4027-capital_withdraw_get_tran_id_failure "-4027 CAPITAL_WITHDRAW_GET_TRAN_ID_FAILURE的直接链接")

  * 无法获取tranId。



### -4028 CAPITAL_WITHDRAW_MORE_THAN_FEE[​](/docs/zh-CN/institutional_loan/error-code#-4028-capital_withdraw_more_than_fee "-4028 CAPITAL_WITHDRAW_MORE_THAN_FEE的直接链接")

  * 提款金额必须多于佣金额。



### -4029 CAPITAL_WITHDRAW_NOT_EXIST[​](/docs/zh-CN/institutional_loan/error-code#-4029-capital_withdraw_not_exist "-4029 CAPITAL_WITHDRAW_NOT_EXIST的直接链接")

  * 此提款记录不存在。



### -4030 CAPITAL_WITHDRAW_CONFIRM_SUCCESS[​](/docs/zh-CN/institutional_loan/error-code#-4030-capital_withdraw_confirm_success "-4030 CAPITAL_WITHDRAW_CONFIRM_SUCCESS的直接链接")

  * 提款资产成功。



### -4031 CAPITAL_WITHDRAW_CANCEL_FAILURE[​](/docs/zh-CN/institutional_loan/error-code#-4031-capital_withdraw_cancel_failure "-4031 CAPITAL_WITHDRAW_CANCEL_FAILURE的直接链接")

  * 取消提款失败。



### -4032 CAPITAL_WITHDRAW_CHECKSUM_VERIFY_FAILURE[​](/docs/zh-CN/institutional_loan/error-code#-4032-capital_withdraw_checksum_verify_failure "-4032 CAPITAL_WITHDRAW_CHECKSUM_VERIFY_FAILURE的直接链接")

  * 验证提款失败。



### -4033 CAPITAL_WITHDRAW_ILLEGAL_ADDRESS[​](/docs/zh-CN/institutional_loan/error-code#-4033-capital_withdraw_illegal_address "-4033 CAPITAL_WITHDRAW_ILLEGAL_ADDRESS的直接链接")

  * 提款地址不合法。



### -4034 CAPITAL_WITHDRAW_ADDRESS_CHEAT[​](/docs/zh-CN/institutional_loan/error-code#-4034-capital_withdraw_address_cheat "-4034 CAPITAL_WITHDRAW_ADDRESS_CHEAT的直接链接")

  * 当前地址有异常。



### -4035 CAPITAL_WITHDRAW_NOT_WHITE_ADDRESS[​](/docs/zh-CN/institutional_loan/error-code#-4035-capital_withdraw_not_white_address "-4035 CAPITAL_WITHDRAW_NOT_WHITE_ADDRESS的直接链接")

  * 此地址不在白名单上。请加入然后重试。



### -4036 CAPITAL_WITHDRAW_NEW_ADDRESS[​](/docs/zh-CN/institutional_loan/error-code#-4036-capital_withdraw_new_address "-4036 CAPITAL_WITHDRAW_NEW_ADDRESS的直接链接")

  * 新地址在{0}小时后才可以提款。



### -4037 CAPITAL_WITHDRAW_RESEND_EMAIL_FAIL[​](/docs/zh-CN/institutional_loan/error-code#-4037-capital_withdraw_resend_email_fail "-4037 CAPITAL_WITHDRAW_RESEND_EMAIL_FAIL的直接链接")

  * 重新发送邮件失败。



### -4038 CAPITAL_WITHDRAW_RESEND_EMAIL_TIME_OUT[​](/docs/zh-CN/institutional_loan/error-code#-4038-capital_withdraw_resend_email_time_out "-4038 CAPITAL_WITHDRAW_RESEND_EMAIL_TIME_OUT的直接链接")

  * 请5分钟后重试。



### -4039 CAPITAL_USER_EMPTY[​](/docs/zh-CN/institutional_loan/error-code#-4039-capital_user_empty "-4039 CAPITAL_USER_EMPTY的直接链接")

  * 用户不存在。



### -4041 CAPITAL_MINUTE_TOO_SMALL[​](/docs/zh-CN/institutional_loan/error-code#-4041-capital_minute_too_small "-4041 CAPITAL_MINUTE_TOO_SMALL的直接链接")

  * 请一分钟后重试。



### -4042 CAPITAL_CHARGE_NOT_RESET[​](/docs/zh-CN/institutional_loan/error-code#-4042-capital_charge_not_reset "-4042 CAPITAL_CHARGE_NOT_RESET的直接链接")

  * 资产无法重新获取存款地址。



### -4043 CAPITAL_ADDRESS_TOO_MUCH[​](/docs/zh-CN/institutional_loan/error-code#-4043-capital_address_too_much "-4043 CAPITAL_ADDRESS_TOO_MUCH的直接链接")

  * 在24小时之内充值超过100多个地址。



### -4044 CAPITAL_BLACKLIST_COUNTRY_GET_ADDRESS[​](/docs/zh-CN/institutional_loan/error-code#-4044-capital_blacklist_country_get_address "-4044 CAPITAL_BLACKLIST_COUNTRY_GET_ADDRESS的直接链接")

  * 此国家在黑名单上。



### -4045 CAPITAL_GET_ASSET_ERROR[​](/docs/zh-CN/institutional_loan/error-code#-4045-capital_get_asset_error "-4045 CAPITAL_GET_ASSET_ERROR的直接链接")

  * 获得资产失败。



### -4046 CAPITAL_AGREEMENT_NOT_CONFIRMED[​](/docs/zh-CN/institutional_loan/error-code#-4046-capital_agreement_not_confirmed "-4046 CAPITAL_AGREEMENT_NOT_CONFIRMED的直接链接")

  * 协议未确认。



### -4047 CAPITAL_DATE_INTERVAL_LIMIT[​](/docs/zh-CN/institutional_loan/error-code#-4047-capital_date_interval_limit "-4047 CAPITAL_DATE_INTERVAL_LIMIT的直接链接")

  * 时间间隔必须在0-90天之内



### -4060 CAPITAL_WITHDRAW_USER_ASSET_LOCK_DEPOSIT[​](/docs/zh-CN/institutional_loan/error-code#-4060-capital_withdraw_user_asset_lock_deposit "-4060 CAPITAL_WITHDRAW_USER_ASSET_LOCK_DEPOSIT的直接链接")

  * 体现仍在区块确认中，暂时锁定部分资产



### -4106 TAG_NOT_SUPPORTED_FOR_NETWORK[​](/docs/zh-CN/institutional_loan/error-code#-4106-tag_not_supported_for_network "-4106 TAG_NOT_SUPPORTED_FOR_NETWORK的直接链接")

  * 该网络不支持 memo/tag。请移除 `addressTag` 字段后重试。



### -5001 ASSET_DRIBBLET_CONVERT_SWITCH_OFF[​](/docs/zh-CN/institutional_loan/error-code#-5001-asset_dribblet_convert_switch_off "-5001 ASSET_DRIBBLET_CONVERT_SWITCH_OFF的直接链接")

  * 不允许转移到微型资产。



### -5002 ASSET_ASSET_NOT_ENOUGH[​](/docs/zh-CN/institutional_loan/error-code#-5002-asset_asset_not_enough "-5002 ASSET_ASSET_NOT_ENOUGH的直接链接")

  * 此余额不足。



### -5003 ASSET_USER_HAVE_NO_ASSET[​](/docs/zh-CN/institutional_loan/error-code#-5003-asset_user_have_no_asset "-5003 ASSET_USER_HAVE_NO_ASSET的直接链接")

  * 此资产不存在。



### -5004 USER_OUT_OF_TRANSFER_FLOAT[​](/docs/zh-CN/institutional_loan/error-code#-5004-user_out_of_transfer_float "-5004 USER_OUT_OF_TRANSFER_FLOAT的直接链接")

  * 剩余余额已超过0.001BTC，请重新选择。
  * ％s的剩余余额已超过0.001BTC，请重新选择。



### -5005 USER_ASSET_AMOUNT_IS_TOO_LOW[​](/docs/zh-CN/institutional_loan/error-code#-5005-user_asset_amount_is_too_low "-5005 USER_ASSET_AMOUNT_IS_TOO_LOW的直接链接")

  * BTC的剩余余额太低，请重新选择。
  * ％s的剩余余额太低，请重新选择。



### -5006 USER_CAN_NOT_REQUEST_IN_24_HOURS[​](/docs/zh-CN/institutional_loan/error-code#-5006-user_can_not_request_in_24_hours "-5006 USER_CAN_NOT_REQUEST_IN_24_HOURS的直接链接")

  * 24小时内只能转账一次。



### -5007 AMOUNT_OVER_ZERO[​](/docs/zh-CN/institutional_loan/error-code#-5007-amount_over_zero "-5007 AMOUNT_OVER_ZERO的直接链接")

  * 数量必须大于零。



### -5008 ASSET_WITHDRAW_WITHDRAWING_NOT_ENOUGH[​](/docs/zh-CN/institutional_loan/error-code#-5008-asset_withdraw_withdrawing_not_enough "-5008 ASSET_WITHDRAW_WITHDRAWING_NOT_ENOUGH的直接链接")

  * 可退回资产的金额不足。



### -5009 PRODUCT_NOT_EXIST[​](/docs/zh-CN/institutional_loan/error-code#-5009-product_not_exist "-5009 PRODUCT_NOT_EXIST的直接链接")

  * 产品不存在。



### -5010 TRANSFER_FAIL[​](/docs/zh-CN/institutional_loan/error-code#-5010-transfer_fail "-5010 TRANSFER_FAIL的直接链接")

  * 资产转移失败。



### -5011 FUTURE_ACCT_NOT_EXIST[​](/docs/zh-CN/institutional_loan/error-code#-5011-future_acct_not_exist "-5011 FUTURE_ACCT_NOT_EXIST的直接链接")

  * 合约帐户不存在。



### -5012 TRANSFER_PENDING[​](/docs/zh-CN/institutional_loan/error-code#-5012-transfer_pending "-5012 TRANSFER_PENDING的直接链接")

  * 资产转移正在进行中。



### -5021 PARENT_SUB_HAVE_NO_RELATION[​](/docs/zh-CN/institutional_loan/error-code#-5021-parent_sub_have_no_relation "-5021 PARENT_SUB_HAVE_NO_RELATION的直接链接")

  * 当前的子账户和母账户没有从属关系。



### -5012 FUTURE_ACCT_OR_SUBRELATION_NOT_EXIST[​](/docs/zh-CN/institutional_loan/error-code#-5012-future_acct_or_subrelation_not_exist "-5012 FUTURE_ACCT_OR_SUBRELATION_NOT_EXIST的直接链接")

  * 合约帐户或子账户关系不存在。



## 6XXX - 币安宝相关[​](/docs/zh-CN/institutional_loan/error-code#6xxx---币安宝相关 "6XXX - 币安宝相关的直接链接")

### -6001 DAILY_PRODUCT_NOT_EXIST[​](/docs/zh-CN/institutional_loan/error-code#-6001-daily_product_not_exist "-6001 DAILY_PRODUCT_NOT_EXIST的直接链接")

  * 理财产品不存在.



### -6003 DAILY_PRODUCT_NOT_ACCESSIBLE[​](/docs/zh-CN/institutional_loan/error-code#-6003-daily_product_not_accessible "-6003 DAILY_PRODUCT_NOT_ACCESSIBLE的直接链接")

  * 产品不存在或者没有权限。



### -6004 DAILY_PRODUCT_NOT_PURCHASABLE[​](/docs/zh-CN/institutional_loan/error-code#-6004-daily_product_not_purchasable "-6004 DAILY_PRODUCT_NOT_PURCHASABLE的直接链接")

  * 产品无法购买。



### -6005 DAILY_LOWER_THAN_MIN_PURCHASE_LIMIT[​](/docs/zh-CN/institutional_loan/error-code#-6005-daily_lower_than_min_purchase_limit "-6005 DAILY_LOWER_THAN_MIN_PURCHASE_LIMIT的直接链接")

  * 低于可以购买的最小限额。



### -6006 DAILY_REDEEM_AMOUNT_ERROR[​](/docs/zh-CN/institutional_loan/error-code#-6006-daily_redeem_amount_error "-6006 DAILY_REDEEM_AMOUNT_ERROR的直接链接")

  * 赎回额度有误。



### -6007 DAILY_REDEEM_TIME_ERROR[​](/docs/zh-CN/institutional_loan/error-code#-6007-daily_redeem_time_error "-6007 DAILY_REDEEM_TIME_ERROR的直接链接")

  * 不在赎回的时间内。



### -6008 DAILY_PRODUCT_NOT_REDEEMABLE[​](/docs/zh-CN/institutional_loan/error-code#-6008-daily_product_not_redeemable "-6008 DAILY_PRODUCT_NOT_REDEEMABLE的直接链接")

  * 产品暂时无法赎回。



### -6009 REQUEST_FREQUENCY_TOO_HIGH[​](/docs/zh-CN/institutional_loan/error-code#-6009-request_frequency_too_high "-6009 REQUEST_FREQUENCY_TOO_HIGH的直接链接")

  * 发送请求太频繁。



### -6011 EXCEEDED_USER_PURCHASE_LIMIT[​](/docs/zh-CN/institutional_loan/error-code#-6011-exceeded_user_purchase_limit "-6011 EXCEEDED_USER_PURCHASE_LIMIT的直接链接")

  * 超购每个月用户可以申购的最大次数。



### -6012 BALANCE_NOT_ENOUGH[​](/docs/zh-CN/institutional_loan/error-code#-6012-balance_not_enough "-6012 BALANCE_NOT_ENOUGH的直接链接")

  * 余额不足。



### -6013 PURCHASING_FAILED[​](/docs/zh-CN/institutional_loan/error-code#-6013-purchasing_failed "-6013 PURCHASING_FAILED的直接链接")

  * 申购失败。



### -6014 UPDATE_FAILED[​](/docs/zh-CN/institutional_loan/error-code#-6014-update_failed "-6014 UPDATE_FAILED的直接链接")

  * 超过可以申购的最大上限。



### -6015 EMPTY_REQUEST_BODY[​](/docs/zh-CN/institutional_loan/error-code#-6015-empty_request_body "-6015 EMPTY_REQUEST_BODY的直接链接")

  * 请求的`body`为空。



### -6016 PARAMS_ERR[​](/docs/zh-CN/institutional_loan/error-code#-6016-params_err "-6016 PARAMS_ERR的直接链接")

  * 请求的参数有误。



### -6017 NOT_IN_WHITELIST[​](/docs/zh-CN/institutional_loan/error-code#-6017-not_in_whitelist "-6017 NOT_IN_WHITELIST的直接链接")

  * 不在白名单里面。



### -6018 ASSET_NOT_ENOUGH[​](/docs/zh-CN/institutional_loan/error-code#-6018-asset_not_enough "-6018 ASSET_NOT_ENOUGH的直接链接")

  * 资产不足。



### -6019 PENDING[​](/docs/zh-CN/institutional_loan/error-code#-6019-pending "-6019 PENDING的直接链接")

  * 需要进一步确认。



### -6020 PROJECT_NOT_EXISTS[​](/docs/zh-CN/institutional_loan/error-code#-6020-project_not_exists "-6020 PROJECT_NOT_EXISTS的直接链接")

  * 此项目不存在。



## 70xx - 期货[​](/docs/zh-CN/institutional_loan/error-code#70xx---期货 "70xx - 期货的直接链接")

### -7001 FUTURES_BAD_DATE_RANGE[​](/docs/zh-CN/institutional_loan/error-code#-7001-futures_bad_date_range "-7001 FUTURES_BAD_DATE_RANGE的直接链接")

  * 此日期范围不支持。



### -7002 FUTURES_BAD_TYPE[​](/docs/zh-CN/institutional_loan/error-code#-7002-futures_bad_type "-7002 FUTURES_BAD_TYPE的直接链接")

  * 此数据请求类型不支持。



## 20xxx - 合约/现货策略交易[​](/docs/zh-CN/institutional_loan/error-code#20xxx---合约现货策略交易 "20xxx - 合约/现货策略交易的直接链接")

### -20121 Invalid symbol[​](/docs/zh-CN/institutional_loan/error-code#-20121-invalid-symbol "-20121 Invalid symbol的直接链接")

  * 无效交易对。



### -20124 Invalid algo id or it has been completed[​](/docs/zh-CN/institutional_loan/error-code#-20124-invalid-algo-id-or-it-has-been-completed "-20124 Invalid algo id or it has been completed的直接链接")

  * 无效的策略订单ID或者它已经被执行。



### -20130 Invalid data sent for a parameter[​](/docs/zh-CN/institutional_loan/error-code#-20130-invalid-data-sent-for-a-parameter "-20130 Invalid data sent for a parameter的直接链接")

  * 无效数据。



### -20132 The client algo id is duplicated[​](/docs/zh-CN/institutional_loan/error-code#-20132-the-client-algo-id-is-duplicated "-20132 The client algo id is duplicated的直接链接")

  * 用户自定义策略订单ID重复。



### -20194 Duration is too short to execute all required quantity[​](/docs/zh-CN/institutional_loan/error-code#-20194-duration-is-too-short-to-execute-all-required-quantity "-20194 Duration is too short to execute all required quantity的直接链接")

  * Duration 时间太短不足以执行用户选择的订单数量。



### -20195 The total size is too small[​](/docs/zh-CN/institutional_loan/error-code#-20195-the-total-size-is-too-small "-20195 The total size is too small的直接链接")

  * 下单数量太小。



### -20196 The total size is too large[​](/docs/zh-CN/institutional_loan/error-code#-20196-the-total-size-is-too-large "-20196 The total size is too large的直接链接")

  * 下单数量太大。



### -20198 Reach the max open orders allowed[​](/docs/zh-CN/institutional_loan/error-code#-20198-reach-the-max-open-orders-allowed "-20198 Reach the max open orders allowed的直接链接")

  * 达到了最大挂单上限。



### -20204 The notional of USD is less or more than the limit[​](/docs/zh-CN/institutional_loan/error-code#-20204-the-notional-of-usd-is-less-or-more-than-the-limit "-20204 The notional of USD is less or more than the limit的直接链��接")

  * 订单小于最小USD名义价值



## 过滤器故障[​](/docs/zh-CN/institutional_loan/error-code#过滤器故障 "过滤器故障的直接链接")

报错信息| 描述  
---|---  
"Filter failure: PRICE_FILTER"| "价格"过高，过低和/或不遵循交易对的最小价格规则。  
"Filter failure: PERCENT_PRICE"| "价格"比最近Y分钟的平均加权价格高X％或X％太低。  
"Filter failure: PERCENT_PRICE_BY_SIDE"| `price` 在当前方向上(`BUY`或者`SELL`)比`lastPrice`价格超过X%或者低于Y%。  
"Filter failure: LOT_SIZE"| "数量"太高，太低和/或不遵循该交易对的步长规则。  
"Filter failure: MIN_NOTIONAL"| 价格*数量太低，无法成为该交易对的有效订单。  
"Filter failure: ICEBERG_PARTS"| `ICEBERG` 订单会分成太多部分； icebergQty太小。  
"Filter failure: MARKET_LOT_SIZE"| "MARKET"订单的"数量"过高，过低和/或未遵循交易对的步长规则。  
"Filter failure: MAX_POSITION"| 达到账户的最大仓位限制。这包括了账户的余额总额，以及所有处于open的买单的数量总和。  
"Filter failure: MAX_NUM_ORDERS"| 客户在交易对上有太多挂单。  
"Filter failure: MAX_ALGO_ORDERS"| 账户有太多未平仓止损和/或在交易对上执行获利指令。  
"Filter failure: MAX_NUM_ICEBERG_ORDERS"| 客户在交易对上有太多 iceberg 挂单。  
"Filter failure: TRAILING_DELTA"| `trailingDelta` 值不在限定的范围内.  
"Filter failure: EXCHANGE_MAX_NUM_ORDERS"| 帐户上的交易所有太多挂单。  
"Filter failure: EXCHANGE_MAX_ALGO_ORDERS"| 帐户有太多止损挂单和/或在交易所收取获利指令。  
  
## 10xxx - 质押借币[​](/docs/zh-CN/institutional_loan/error-code#10xxx---质押借币 "10xxx - 质押借币的直接链接")

### -10001 SYSTEM_MAINTENANCE[​](/docs/zh-CN/institutional_loan/error-code#-10001-system_maintenance "-10001 SYSTEM_MAINTENANCE的直接链接")

  * 系统维护中，请稍后再试



### -10002 INVALID_INPUT[​](/docs/zh-CN/institutional_loan/error-code#-10002-invalid_input "-10002 INVALID_INPUT的直接链接")

  * 无效的输入参数



### -10005 NO_RECORDS[​](/docs/zh-CN/institutional_loan/error-code#-10005-no_records "-10005 NO_RECORDS的直接链接")

  * 暂无记录



### -10007 COIN_NOT_LOANABLE[​](/docs/zh-CN/institutional_loan/error-code#-10007-coin_not_loanable "-10007 COIN_NOT_LOANABLE的直接链接")

  * 该币种暂不支持借贷



### -10008 COIN_NOT_LOANABLE[​](/docs/zh-CN/institutional_loan/error-code#-10008-coin_not_loanable "-10008 COIN_NOT_LOANABLE的直接链接")

  * 该币种暂不支持借贷



### -10009 COIN_NOT_COLLATERAL[​](/docs/zh-CN/institutional_loan/error-code#-10009-coin_not_collateral "-10009 COIN_NOT_COLLATERAL的直接链接")

  * 该币种暂不支持抵押



### -10010 COIN_NOT_COLLATERAL[​](/docs/zh-CN/institutional_loan/error-code#-10010-coin_not_collateral "-10010 COIN_NOT_COLLATERAL的直接链接")

  * 该币种暂不支持抵押



### -10011 INSUFFICIENT_ASSET[​](/docs/zh-CN/institutional_loan/error-code#-10011-insufficient_asset "-10011 INSUFFICIENT_ASSET的直接链接")

  * 现货资产不足



### -10012 INVALID_AMOUNT[​](/docs/zh-CN/institutional_loan/error-code#-10012-invalid_amount "-10012 INVALID_AMOUNT的直接链接")

  * 无效的还款金额



### -10013 INSUFFICIENT_AMOUNT[​](/docs/zh-CN/institutional_loan/error-code#-10013-insufficient_amount "-10013 INSUFFICIENT_AMOUNT的直接链接")

  * 抵押资产不足



### -10015 DEDUCTION_FAILED[​](/docs/zh-CN/institutional_loan/error-code#-10015-deduction_failed "-10015 DEDUCTION_FAILED的直接链接")

  * 抵押资产扣款失败



### -10016 LOAN_FAILED[​](/docs/zh-CN/institutional_loan/error-code#-10016-loan_failed "-10016 LOAN_FAILED的直接链接")

  * 放贷失败



### -10017 REPAY_EXCEED_DEBT[​](/docs/zh-CN/institutional_loan/error-code#-10017-repay_exceed_debt "-10017 REPAY_EXCEED_DEBT的直接链接")

  * 还款金额超过负债金额



### -10018 INVALID_AMOUNT[​](/docs/zh-CN/institutional_loan/error-code#-10018-invalid_amount "-10018 INVALID_AMOUNT的直接链接")

  * 无效的还款金额



### -10019 CONFIG_NOT_EXIST[​](/docs/zh-CN/institutional_loan/error-code#-10019-config_not_exist "-10019 CONFIG_NOT_EXIST的直接链接")

  * 配置不存在



### -10020 UID_NOT_EXIST[​](/docs/zh-CN/institutional_loan/error-code#-10020-uid_not_exist "-10020 UID_NOT_EXIST的直接链接")

  * 用户ID不存在



### -10021 ORDER_NOT_EXIST[​](/docs/zh-CN/institutional_loan/error-code#-10021-order_not_exist "-10021 ORDER_NOT_EXIST的直接链接")

  * 订单不存在



### -10022 INVALID_AMOUNT[​](/docs/zh-CN/institutional_loan/error-code#-10022-invalid_amount "-10022 INVALID_AMOUNT的直接链接")

  * 无效的调整金额



### -10023 ADJUST_LTV_FAILED[​](/docs/zh-CN/institutional_loan/error-code#-10023-adjust_ltv_failed "-10023 ADJUST_LTV_FAILED的直接链接")

  * 调整质押率失败



### -10024 ADJUST_LTV_NOT_SUPPORTED[​](/docs/zh-CN/institutional_loan/error-code#-10024-adjust_ltv_not_supported "-10024 ADJUST_LTV_NOT_SUPPORTED的直接链接")

  * 暂不支持调整质押率



### -10025 REPAY_FAILED[​](/docs/zh-CN/institutional_loan/error-code#-10025-repay_failed "-10025 REPAY_FAILED的直接链接")

  * 还款失败



### -10026 INVALID_PARAMETER[​](/docs/zh-CN/institutional_loan/error-code#-10026-invalid_parameter "-10026 INVALID_PARAMETER的直接链接")

  * 无效的参数



### -10028 INVALID_PARAMETER[​](/docs/zh-CN/institutional_loan/error-code#-10028-invalid_parameter "-10028 INVALID_PARAMETER的直接链接")

  * 无效的参数



### -10029 AMOUNT_TOO_SMALL[​](/docs/zh-CN/institutional_loan/error-code#-10029-amount_too_small "-10029 AMOUNT_TOO_SMALL的直接链接")

  * 借贷金额过小



### -10030 AMOUNT_TOO_LARGE[​](/docs/zh-CN/institutional_loan/error-code#-10030-amount_too_large "-10030 AMOUNT_TOO_LARGE的直接链接")

  * 借贷金额过大



### -10031 QUOTA_REACHED[​](/docs/zh-CN/institutional_loan/error-code#-10031-quota_reached "-10031 QUOTA_REACHED的直接链接")

  * 已达到个人借贷限额



### -10032 REPAY_NOT_AVAILABLE[​](/docs/zh-CN/institutional_loan/error-code#-10032-repay_not_available "-10032 REPAY_NOT_AVAILABLE的直接链接")

  * 暂不支持换款



### -10034 REPAY_NOT_AVAILABLE[​](/docs/zh-CN/institutional_loan/error-code#-10034-repay_not_available "-10034 REPAY_NOT_AVAILABLE的直接链接")

  * 抵押物还款暂时不支持，请尝试用借贷币还款。



### -10039 AMOUNT_TOO_SMALL[​](/docs/zh-CN/institutional_loan/error-code#-10039-amount_too_small "-10039 AMOUNT_TOO_SMALL的直接链接")

  * 还款金额过小



### -10040 AMOUNT_TOO_LARGE[​](/docs/zh-CN/institutional_loan/error-code#-10040-amount_too_large "-10040 AMOUNT_TOO_LARGE的直接链接")

  * 还款金额过大



### -10041 INSUFFICIENT_AMOUNT[​](/docs/zh-CN/institutional_loan/error-code#-10041-insufficient_amount "-10041 INSUFFICIENT_AMOUNT的直接链接")

  * 由于借贷需求过多，系统剩余可借{0}额度不足。请调整借贷金额或明天再试。



### -10042 ASSET_NOT_SUPPORTED[​](/docs/zh-CN/institutional_loan/error-code#-10042-asset_not_supported "-10042 ASSET_NOT_SUPPORTED的直接链接")

  * 暂不支持%s币种



### -10043 ASSET_NOT_SUPPORTED[​](/docs/zh-CN/institutional_loan/error-code#-10043-asset_not_supported "-10043 ASSET_NOT_SUPPORTED的直接链接")

  * 暂不支持{0} 借贷



### -10044 QUOTA_REACHED[​](/docs/zh-CN/institutional_loan/error-code#-10044-quota_reached "-10044 QUOTA_REACHED的直接链接")

  * 抵押物数量已达到限额，请调整抵押金额或使用其他抵押资产。



### -10045 COLLTERAL_REPAY_NOT_SUPPORTED[​](/docs/zh-CN/institutional_loan/error-code#-10045-collteral_repay_not_supported "-10045 COLLTERAL_REPAY_NOT_SUPPORTED的直接链接")

  * 该借贷币种暂不支持抵押物还款，请稍后再试。



### -10046 EXCEED_MAX_ADJUSTMENT[​](/docs/zh-CN/institutional_loan/error-code#-10046-exceed_max_adjustment "-10046 EXCEED_MAX_ADJUSTMENT的直接链接")

  * 调整抵押物超过最大限额，请重试。



### -10047 REGION_NOT_SUPPORTED[​](/docs/zh-CN/institutional_loan/error-code#-10047-region_not_supported "-10047 REGION_NOT_SUPPORTED的直接链接")

  * 受当地法规管制，您所在地区暂不支持该币种。




## 13xxx - 杠杆代币[​](/docs/zh-CN/institutional_loan/error-code#13xxx---杠杆代币 "13xxx - 杠杆代币的直接链接")

### -13000 BLVT_FORBID_REDEEM[​](/docs/zh-CN/institutional_loan/error-code#-13000-blvt_forbid_redeem "-13000 BLVT_FORBID_REDEEM的直接链接")

  * 当前该杠杆代币关闭赎回



### -13001 BLVT_EXCEED_DAILY_LIMIT[​](/docs/zh-CN/institutional_loan/error-code#-13001-blvt_exceed_daily_limit "-13001 BLVT_EXCEED_DAILY_LIMIT的直接链接")

  * 超过该代币个人24小时赎回金额上限



### -13002 BLVT_EXCEED_TOKEN_DAILY_LIMIT[​](/docs/zh-CN/institutional_loan/error-code#-13002-blvt_exceed_token_daily_limit "-13002 BLVT_EXCEED_TOKEN_DAILY_LIMIT的直接链接")

  * 超过该代币全局24小时赎回金额上限



### -13003 BLVT_FORBID_PURCHASE[​](/docs/zh-CN/institutional_loan/error-code#-13003-blvt_forbid_purchase "-13003 BLVT_FORBID_PURCHASE的直接链接")

  * 当前该杠杆代币关闭申购



### -13004 BLVT_EXCEED_DAILY_PURCHASE_LIMIT[​](/docs/zh-CN/institutional_loan/error-code#-13004-blvt_exceed_daily_purchase_limit "-13004 BLVT_EXCEED_DAILY_PURCHASE_LIMIT的直接链接")

  * 超过该代币个人24小时申购金额上限



### -13005 BLVT_EXCEED_TOKEN_DAILY_PURCHASE_LIMIT[​](/docs/zh-CN/institutional_loan/error-code#-13005-blvt_exceed_token_daily_purchase_limit "-13005 BLVT_EXCEED_TOKEN_DAILY_PURCHASE_LIMIT的直接链接")

  * 超过该代币全局24小时申购金额上限



### -13006 BLVT_PURCHASE_LESS_MIN_AMOUNT[​](/docs/zh-CN/institutional_loan/error-code#-13006-blvt_purchase_less_min_amount "-13006 BLVT_PURCHASE_LESS_MIN_AMOUNT的直接链接")

  * 申购金额低于规定下限



### -13007 BLVT_PURCHASE_AGREEMENT_NOT_SIGN[​](/docs/zh-CN/institutional_loan/error-code#-13007-blvt_purchase_agreement_not_sign "-13007 BLVT_PURCHASE_AGREEMENT_NOT_SIGN的直接链接")

  * 没有签署开通交易协议



## 12xxx - 流动性挖矿[​](/docs/zh-CN/institutional_loan/error-code#12xxx---流动性挖矿 "12xxx - 流动性挖矿的直接链接")

### -12014 TOO MANY REQUESTS[​](/docs/zh-CN/institutional_loan/error-code#-12014-too-many-requests "-12014 TOO MANY REQUESTS的直接链接")

  * 2秒内接收的请求数量多于1条



## 18xxx - 币安码[​](/docs/zh-CN/institutional_loan/error-code#18xxx---币安码 "18xxx - 币安码的直接链接")

### -18002[​](/docs/zh-CN/institutional_loan/error-code#-18002 "-18002的直接链接")

  * The total amount of codes you created has exceeded the 24-hour limit, please try again after UTC 0
  * 24小时内制码总金额已超过限额，请UTC0点后再尝试



### -18003[​](/docs/zh-CN/institutional_loan/error-code#-18003 "-18003的直接链接")

  * Too many codes created in 24 hours, please try again after UTC 0
  * 24小时内制码总次数已超过限额，请UTC0点后再尝试



### -18004[​](/docs/zh-CN/institutional_loan/error-code#-18004 "-18004的直接链接")

  * Too many invalid redeem attempts in 24 hours, please try again after UTC 0
  * 24小时内兑现币安码输错次数已超过限额，请UTC0点后再尝试



### -18005[​](/docs/zh-CN/institutional_loan/error-code#-18005 "-18005的直接链接")

  * Too many invalid verify attempts, please try later
  * 参考号输错次数过多，请稍后再试



### -18006[​](/docs/zh-CN/institutional_loan/error-code#-18006 "-18006的直接链接")

  * The amount is too small, please re-enter
  * 金额过小，请重新输入



### -18007[​](/docs/zh-CN/institutional_loan/error-code#-18007 "-18007的直接链接")

  * This token is not currently supported, please re-enter
  * 尚未支持该币种，请重新输入



## 21xxx - 統一帳戶[​](/docs/zh-CN/institutional_loan/error-code#21xxx---統一帳戶 "21xxx - 統一帳戶的直接链接")

### -21001 USER_IS_NOT_UNIACCOUNT[​](/docs/zh-CN/institutional_loan/error-code#-21001-user_is_not_uniaccount "-21001 USER_IS_NOT_UNIACCOUNT的直接链接")

  * 尚未开通统一账户。



### -21002 UNI_ACCOUNT_CANT_TRANSFER_FUTURE[​](/docs/zh-CN/institutional_loan/error-code#-21002-uni_account_cant_transfer_future "-21002 UNI_ACCOUNT_CANT_TRANSFER_FUTURE的直接链接")

  * 统一账户禁用margin向futures转账。



### -21003 NET_ASSET_MUST_LTE_RATIO[​](/docs/zh-CN/institutional_loan/error-code#-21003-net_asset_must_lte_ratio "-21003 NET_ASSET_MUST_LTE_RATIO的直接链接")

  * margin资产更新失败。



### -21004 USER_NO_LIABILITY[​](/docs/zh-CN/institutional_loan/error-code#-21004-user_no_liability "-21004 USER_NO_LIABILITY的直接链接")

  * 用户不存在统一账户穿仓负债



### -21005 NO_ENOUGH_ASSET[​](/docs/zh-CN/institutional_loan/error-code#-21005-no_enough_asset "-21005 NO_ENOUGH_ASSET的直接链接")

  * 用户现货钱包BUSD资产不足以偿还统一账户穿仓负债



### -21006 HAD_IN_PROCESS_REPAY[​](/docs/zh-CN/institutional_loan/error-code#-21006-had_in_process_repay "-21006 HAD_IN_PROCESS_REPAY的直接链接")

  * 用户存在正在偿还的统一账户穿仓负债



### -21007 IN_FORCE_LIQUIDATION[​](/docs/zh-CN/institutional_loan/error-code#-21007-in_force_liquidation "-21007 IN_FORCE_LIQUIDATION的直接链接")

  * 强平进行中，用户偿还统一账户穿仓负债失败



## 订单拒绝错误[​](/docs/zh-CN/institutional_loan/error-code#订单拒绝错误 "订单拒绝错误的直接链接")

以下错误代码表示撮合引擎返回的订单相关错误:

  * `-1010 ERROR_MSG_RECEIVED`
  * `-2010 NEW_ORDER_REJECTED`
  * `-2011 CANCEL_REJECTED`



结合以下消息将指示特定的错误：

错误信息| 描述  
---|---  
"Unknown order sent."| 找不到订单(通过"orderId"，"clientOrderId"，"origClientOrderId")  
"Duplicate order sent."| `clientOrderId`已经被使用  
"Market is closed."| 该交易对不在交易范围  
"Account has insufficient balance for requested action."| 没有足够的资金来完成行动  
"Market orders are not supported for this symbol."| 交易对上未启用"MARKET"  
"Iceberg orders are not supported for this symbol."| 交易对上未启用`icebergQty`  
"Stop loss orders are not supported for this symbol."| 交易对上未启用 `STOP_LOSS`  
"Stop loss limit orders are not supported for this symbol."| 交易对上未启`STOP_LOSS_LIMIT`  
"Take profit orders are not supported for this symbol."| 交易对上未启用`TAKE_PROFIT`  
"Take profit limit orders are not supported for this symbol."| 交易对上未启用`TAKE_PROFIT_LIMIT`  
"Price * QTY is zero or less."| `price` * `quantity`太小  
"IcebergQty exceeds QTY."| `icebergQty` 必须少于订单数量  
"This action is disabled on this account."| 联系客户支持； 该账户已禁用了某些操作。  
"This account may not place or cancel orders."| 联系客户支持： 该账户已被禁用了交易操作。  
"Unsupported order combination"| 不允许组合`orderType`, `timeInForce`, `stopPrice`, 和/或 `icebergQty` 。  
"Order would trigger immediately."| 与最后交易价格相比，订单的止损价无效。  
"Cancel order is invalid. Check origClientOrderId and orderId."| 未发送`origClientOrderId` 或`orderId` 。  
"Order would immediately match and take."| `LIMIT_MAKER` 订单类型将立即匹配并进行交易，而不是纯粹的生成订单。  
"The relationship of the prices for the orders is not correct."| `OCO`订单中设置的价格不符合报价规则：  
  
The rules are:   
  
`SELL Orders`: Limit Price > Last Price > Stop Price   
  
`BUY Orders`: Limit Price < Last Price < Stop Price  
"OCO orders are not supported for this symbol"| `OCO`订单不支持该交易对  
"Quote order qty market orders are not support for this symbol."| 这个交易对，市价单不支持参数`quoteOrderQty`  
"Trailing stop orders are not supported for this symbol."| 此symbol不支持 `trailingDelta` ｜  
"Order cancel-replace is not supported for this symbol."| 此symbol不支持 `POST /api/v3/order/cancelReplace` 或者 `order.cancelReplace` (WebSocket API) ｜  
"This symbol is not permitted for this account."| 账户和交易对的权限不一致 (比如 `SPOT`, `MARGIN` 等)。｜  
"This symbol is restricted for this account."| 账户没有权限在此交易对交易 (比如账户只拥有 `ISOLATED_MARGIN`权限，则无法下`SPOT` 订单)。 ｜  
"Order was not canceled due to cancel restrictions."| `cancelRestrictions` 设置为 `ONLY_NEW` 但订单状态不是 `NEW`   
或   
`cancelRestrictions` 设置为 `ONLY_PARTIALLY_FILLED` 但订单状态不是 `PARTIALLY_FILLED`。 ｜  
  
## 关于 POST /api/v3/order/cancelReplace 的错误[​](/docs/zh-CN/institutional_loan/error-code#关于-post-apiv3ordercancelreplace-的错误 "关于 POST /api/v3/order/cancelReplace 的错误的直接链接")

### -2021 Order cancel-replace partially failed[​](/docs/zh-CN/institutional_loan/error-code#-2021-order-cancel-replace-partially-failed "-2021 Order cancel-replace partially failed的直接链接")

收到该错误码代表撤单**或者** 下单失败。

### -2022 Order cancel-replace failed.[​](/docs/zh-CN/institutional_loan/error-code#-2022-order-cancel-replace-failed "-2022 Order cancel-replace failed.的直接链接")

收到该错误码代表撤单**和** 下单都失败。