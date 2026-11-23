---
exchange: bitget
source_url: https://www.bitget.com/docs/uta/enum
api_type: Guide
updated_at: 2026-11-23 19:01:46.236439
---

# Enumeration

## category
- `SPOT` Spot
- `MARGIN` Spot Margin
- `USDT-FUTURES` USDT Futures
- `COIN-FUTURES` Coin-M Futures
- `USDC-FUTURES` USDC Futures


## side
- `buy` Buy
- `sell` Sell


## orderType
- `limit` Limit
- `market` Market


## posSide
- `long` Long
- `short` Short


## timeInForce
- `gtc` Good 'til canceled. _It remains active until it is either filled or manually canceled._
- `post_only` Post only. _It will only be added to the order book as a maker._
- `fok` Fill or Kill. _It must be fully executed immediately, or it is canceled entirely._
- `ioc` Immediate or cancel. _It must be executed immediately, with any unfilled portion canceled_
- `rpi` Retail Price Improvement. _A limit order that matches against retail counterparts at a better price than the current best bid/ask._


## holdMode
- `one_way_mode` One_way mode. _Only single direction supported._
- `hedge_mode` Hedge mode. _Both directions supported._


## marginMode
- `crossed` Crossed margin mode
- `isolated` Isolated margin mode


## reduceOnly
- `yes` Only position reduction supported.
- `no` Both reduction and increase are supported.


## execType
- `normal` Normal
- `offset` Offset
- `reduce` Forced reduction
- `liquidation` Liquidation
- `delivery` Delivery


## orderStatus
- `live` Live
- `new`  Order matching
- `partially_filled` Partially filled
- `filled` Fully filled
- `cancelled` Cancelled


## tradeScope
- `taker` Taker, who executes an existing order, removing liquidity.
- `maker` Maker, who places a new order, adding liquidity.


## assetMode
-  `union` union-margin mode


## type (financial records)
- `TRANSFER_IN` Transfer in
- `TRANSFER_OUT` Transfer out
- `CONVERSION_UPON_DELISTING` Auto borrow - system debit
- `ORDER_DEALT_FROZEN_OUT` Order dealt fund out
- `ORDER_DEALT_IN` Order dealt fund in
- `ORDER_PLF_FEE_OUT` Trading fee deduction
- `EXCHANGE_SOURCE_TOKEN_USER_OUT` Repayment exchange out
- `EXCHANGE_TARGET_TOKEN_USER_IN` Repayment exchange in
- `OPEN_LONG` Open long position
- `OPEN_SHORT` Open short position
- `BUY_DEAL` Single-sided buy
- `SELL_DEAL` Single-sided sell
- `CLOSE_LONG` Close long
- `CLOSE_SHORT` Close short
- `FORCE_CLOSE_LONG` Forced reduction of long position
- `FORCE_CLOSE_SHORT` Forced reduction of short position
- `BURST_CLOSE_LONG` Liquidate long position
- `BURST_CLOSE_SHORT` Liquidate short position
- `OFFSET_REDUCE_CLOSE_LONG` Offset close long
- `OFFSET_REDUCE_CLOSE_SHORT` Offset close short
- `FORCE_BUY_SSM` Forced buy
- `FORCE_SELL_SSM` Forced sell
- `BURST_BUY_SSM` Liquidation buy
- `BURST_SELL_SSM` Liquidation sell
- `RISK_LIQ_USER_IN` Risk control - liability liquidation, user credit
- `INTEREST_SETTLEMENT_OUT` Interest deduction
- `CONTRACT_MAIN_SETTLE_FEE_USER_IN` Cross-margin funding fee in
- `CONTRACT_MAIN_SETTLE_FEE_USER_OUT` Cross-margin funding fee out
- `RISK_LIQ_USER_OUT` Risk control - liability liquidation, user debit
- `BORROW` Ins Loan borrow
- `RESERVE_TRANSFER_IN` Reserve transfer in
- `RESERVE_TRANSFER_OUT` Reserve transfer out
- `REPAYMENT` Ins Loan repayment
- `INTEREST_REPAYMENT` Interest repayment
- `LIQ_FUND_OUT` Liquidation fund out
- `LIQ_CONVERT_USER_OUT` Liquidation convert - user out
- `LIQ_CONVERT_SYS_IN` Liquidation convert - system in
- `LIQ_CONVERT_SYS_OUT` Liquidation convert - system out
- `LIQ_CONVERT_USER_IN` Liquidation convert - user in
- `LIQ_TRANSFER_IN` Liquidation transfer in
- `LIQ_TRANSFER_OUT` Liquidation transfer out
- `LIQ_FUND_IN` Liquidation fund in
- `LIQ_FEE` Liquidation fee
- `LIQ_REPAYMENT` Liquidation repayment
- `DELIST_MARGIN_TOKEN_SOURCE_USER_OUT` Margin token delist - exchange out, user debit
- `DELIST_MARGIN_TOKEN_SOURCE_SYS_IN` Margin token delist - exchange in, system credit
- `DELIST_MARGIN_TOKEN_TARGET_SYS_OUT` Margin token delist - exchange out, system debit
- `DELIST_MARGIN_TOKEN_TARGET_USER_IN` Margin token delist - exchange in, user credit
- `CONFISCATE_TOKEN_USER_OUT` Asset confiscation - user debit
- `CONFISCATE_TOKEN_SYS_IN` Asset confiscation - system credit
- `DELIST_SMALL_BALANCE_USER_OUT` Margin token delist - small balance, user out
- `DELIST_SMALL_BALANCE_SYS_IN` Margin token delist - small balance, system in
- `DELIST_SMALL_LIABILITY_SYS_OUT` Margin token delist - small liability, system out
- `DELIST_SMALL_LIABILITY_USER_IN` Margin token delist - small liability, user in
- `SMALL_ASSET_SOURCE_TOKEN_USER_OUT` Small asset conversion - source token, user out
- `SMALL_ASSET_SOURCE_TOKEN_SYS_IN` Small asset conversion - source token, system in
- `SMALL_ASSET_TARGET_TOKEN_SYS_OUT` Small asset conversion - target token, system out
- `SMALL_ASSET_TARGET_TOKEN_USER_IN` Small asset conversion - target token, user in
- `SMALL_ASSET_FEE_SYS_IN` Small asset conversion - fee, system in
- `TRACE_SHARE_BENEFIT_USER_OUT` Copy trading profit sharing - user out
- `TRACE_SHARE_BENEFIT_SYSTEM_IN` Copy trading profit sharing - system in
- `TRACE_SHARE_BENEFIT_SYSTEM_OUT` Copy trading profit sharing - system out
- `TRACE_SHARE_BENEFIT_USER_IN` Copy trading profit sharing - user in
- `MARGIN_OPEN_LONG` Isolated open long
- `MARGIN_OPEN_SHORT` Isolated open short
- `MARIN_BUY_DEAL` Isolated single-sided buy
- `MARIN_SELL_DEAL` Isolated single-sided sell
- `MARGIN_BACK` Isolated position refund
- `INCREASE_MARGIN` Add isolated margin
- `REDUCE_MARGIN` Reduce isolated margin
- `MARGIN_SETTLE_FEE_USER_IN` Isolated funding fee in
- `MARGIN_SETTLE_FEE_USER_OUT` Isolated funding fee out
- `MARGIN_LEVER_ORDER_REFROZEN` Isolated leverage adjustment - order unfreeze
- `MARGIN_LEVER_ORDER_FROZEN` Isolated leverage adjustment - order freeze
- `MARGIN_LEVER_POS_IN` Isolated leverage adjustment - position margin add
- `MARGIN_OFFSET_IN_SSM_LONG` Isolated single-sided long reduce-only
- `MARGIN_OFFSET_IN_SSM_SHORT` Isolated single-sided short reduce-only
- `FIXED_OFFSET_IN_SSM_LONG` Isolated reduce long
- `FIXED_OFFSET_IN_SSM_SHORT` Isolated reduce short
- `FIXED_CLOSE_LONG` Isolated close long
- `FIXED_CLOSE_SHORT` Isolated close short
- `FIXED_FORCE_CLOSE_LONG` Isolated forced reduction of long
- `FIXED_FORCE_CLOSE_SHORT` Isolated forced reduction of short
- `FIXED_BURST_CLOSE_LONG` Isolated liquidate long
- `FIXED_BURST_CLOSE_SHORT` Isolated liquidate short
- `FIXED_ADL_CLOSE_LONG` Isolated ADL close long
- `FIXED_ADL_CLOSE_SHORT` Isolated ADL close short
- `FIXED_RISK_LIQ_USER_IN` Isolated risk control - liability liquidation, user credit
- `FIXED_RISK_LIQ_USER_OUT` Isolated risk control - liability liquidation, user debit
- `FIXED_FORCE_BUY_SSM` Isolated forced buy
- `FIXED_FORCE_SELL_SSM` Isolated forced sell
- `FIXED_BURST_BUY_SSM` Isolated liquidation buy
- `FIXED_BURST_SELL_SSM` Isolated liquidation sell
- `ON_CHAIN_TRANSFER_REFUND` On-chain transfer - user in
- `ON_CHAIN_TRANSFER_OUT` On-chain transfer - user out
- `MT5_TRANSFER_IN` Transfer in from MT5
- `MT5_REFUND_IN` MT5 transfer out refund
- `MT5_TRANSFER_OUT` Transfer out to MT5
- `TRACE_LOCK_USER_OUT` Copy trading freeze - user out
- `TRACE_LOCK_USER_IN` Copy trading freeze - user in
- `TRACE_TRANSFER_USER_OUT` Copy trading - from UTA to funding account
- `TRACE_TRANSFER_USER_IN` Copy trading - from funding account to UTA sub-account
- `TRACE_TRANSFER_REFUND_IN` Copy trading - funding account refund to UTA
- `FINANCIAL_TRANSFER_OUT` Earn transfer out
- `FINANCIAL_TRANSFER_IN` Earn transfer in
- `CONVERT_TRANSFER_IN` Convert - transfer in
- `CONVERT_TRANSFER_OUT` Convert - transfer out
- `BGPAY_TRANSFER_OUT` BG Pay - transfer out
- `BGPAY_REFUND_IN` BG Pay - refund in
- `RWA_FIXED_SETTLE_FEE_USER_IN` RWA cash dividend isolated margin funding fee - user credit
- `RWA_FIXED_SETTLE_FEE_USER_OUT` RWA cash dividend isolated margin funding fee - user debit
- `RWA_CONTRACT_MAIN_SETTLE_FEE_SYSTEM_IN` RWA cash dividend cross margin funding fee - aggregation account credit
- `RWA_CONTRACT_MAIN_SETTLE_FEE_SYSTEM_OUT` RWA cash dividend cross margin funding fee - aggregation account debit
- `RWA_CONTRACT_MAIN_SETTLE_FEE_SYSTEM_KEEP_IN` RWA cash dividend cross margin funding fee - reserve account credit
- `RWA_CONTRACT_MAIN_SETTLE_FEE_SYSTEM_KEEP_OUT` RWA cash dividend cross margin funding fee - reserve account debit
- `RWA_CONTRACT_MAIN_SETTLE_FEE_USER_IN` RWA cash dividend cross margin funding fee - user credit
- `RWA_CONTRACT_MAIN_SETTLE_FEE_USER_OUT` RWA cash dividend cross margin funding fee - user debit
- `RWA_CONTRACT_REBASE_USER_OPEN_LONG` RWA contract rebase - open long
- `RWA_CONTRACT_REBASE_USER_OPEN_SHORT` RWA contract rebase - open short
- `RWA_CONTRACT_REBASE_USER_CLOSE_LONG` RWA contract rebase - close long
- `RWA_CONTRACT_REBASE_USER_CLOSE_SHORT` RWA contract rebase - close short
- `RWA_CONTRACT_REBASE_USER_BUY_IN_SSM` RWA contract rebase - buy in single side mode
- `RWA_CONTRACT_REBASE_USER_SELL_IN_SSM` RWA contract rebase - sell in single side mode
- `RISK_LIQ_DEFAULT_USER_IN` Risk control - debt liquidation user in
- `FIXED_RISK_LIQ_DEFAULT_USER_IN` Isolated risk control - debt liquidation user in
- `BONUS_GRANT_USER_IN` Bonus - user credit
- `BONUS_EXPIRE_USER_OUT` Bonus expiry - user debit
- `BONUS_TRANSFER_USER_OUT` Bonus transfer expiry - user debit
- `WITHDRAW_TRANSFER_OUT` Withdrawal - transfer out
- `WITHDRAW_TRANSFER_IN` Withdrawal - refund in
- `DELIVERY_LONG` Long delivery
- `DELIVERY_SHORT` Short delivery
- `FIXED_DELIVERY_LONG` Isolated long delivery
- `FIXED_DELIVERY_SHORT` Isolated short delivery
- `REBASE_COIN_SPLIT_OUT` Split/merge shares - split out
- `REBASE_COIN_SPLIT_IN` Split/merge shares - split in
- `REBASE_COIN_MERGE_OUT` Split/merge shares - merge out
- `REBASE_COIN_MERGE_IN` Split/merge shares - merge in


## groupType (funding financial records)
- `transaction` Transaction
- `deposit` Deposit
- `withdraw` Withdraw
- `transfer` Transfer
- `other` Other
- `financial` Financial
- `strategy` Strategy
- `trace` Copy trading
- `loan` Loan
- `fait` Fiat
- `convert` Convert
- `ipo_prime` IPO Prime
- `pre_c2c` Pre-market trading
- `paptrading` Paper trading
- `on_chain` On-chain transaction
- `debit` Debit
- `cfd` CFD
- `pay` Payment
- `compliance_wall` Compliance wall
- `live` Live streaming
- `broker` Broker
- `rwa` RWA
- `stock` Securities


## type (funding financial records)
- `buy` Buy
- `sell` Sell
- `deduction_handling_fee` Fee deduction
- `withholding_tax` Withholding tax
- `deposit` Deposit
- `inner_transfer_recharge` Internal transfer recharge
- `inner_chain_recharge` Internal chain recharge
- `recharge_receive` Recharge receive
- `withdraw` Withdraw
- `inner_withdraw` Internal withdraw
- `inner_addr_withdraw` Internal address withdraw
- `withdraw_transfer` Withdraw transfer
- `transfer_in` Transfer in
- `transfer_out` Transfer out
- `robot_close` Robot close
- `strategy_open` Strategy open
- `robot_account_transfer_in` Robot account transfer in
- `robot_account_transfer_out` Robot account transfer out
- `cross_site_transfer_out` Cross-site transfer out
- `cross_site_transfer_in` Cross-site transfer in
- `on_chain_trade_transfer_in` On-chain trade transfer in
- `pay` Pay
- `pay_refund` Pay refund
- `dual_invest_subscribe` Dual invest subscribe
- `interest` Interest
- `discount_subscribe` Discount subscribe
- `discount_allocate` Discount allocate
- `savings_flexible_subscribe` Simple Earn flexible subscribe
- `savings_flexible_redeem` Simple Earn flexible redeem
- `savings_flexible_profit` Simple Earn flexible profit
- `savings_fixed_subscribe` Simple Earn fixed subscribe
- `savings_fixed_redeem` Simple Earn fixed redeem
- `trend_subscribe` Trend subscribe
- `trend_settle` Trend settle
- `range_subscribe` Range subscribe
- `range_settle` Range settle
- `on_chain_earn_stake` On-chain earn stake
- `on_chain_earn_redeem` On-chain earn redeem
- `bgb_stake` BGB stake
- `bgb_redeem` BGB redeem
- `snowball_subscribe` Snowball subscribe
- `snowball_settle` Snowball settle
- `wealth_subscribe` Wealth subscribe
- `wealth_redeem` Wealth redeem
- `spot_dca_subscribe` Spot DCA subscribe
- `spot_dca_redeem` Spot DCA redeem
- `flexible_interest` Flexible interest
- `robot_buy_expense` Robot buy expense
- `robot_subscribe_expense` Robot subscribe expense
- `robot_refund` Robot refund
- `robot_subscribe_refund` Robot subscribe refund
- `robot_expert_income` Robot expert income
- `robot_trace_profit_income` Robot copy trading profit income
- `trace_profit_expense` Copy trading profit expense
- `trace_profit_income` Copy trading profit income
- `trace_profit_return` Copy trading profit return
- `pledge_deduct` Pledge deduct
- `pledge_return` Pledge return
- `loan_disburse` Loan disburse
- `loan_repay` Loan repay
- `liquidation_return` Liquidation return
- `collateral_repay_loan_return` Collateral repay loan return
- `supplement_pledge_deduct` Supplement pledge deduct
- `release_pledge` Release pledge
- `collateral_repay_pledge_return` Collateral repay pledge return
- `liquidation_loan_return` Liquidation loan return
- `liquidation_pledge_return` Liquidation pledge return
- `pledge_rollback` Pledge rollback
- `convert_consume` Convert consume
- `convert_gain` Convert gain
- `ipo_prime_trade_in` IPO Prime trade in
- `ipo_prime_trade_pay` IPO Prime trade pay
- `ipo_prime_subscribe_expense` IPO Prime subscribe expense
- `ipo_prime_subscribe_income` IPO Prime subscribe income
- `pre_delivery_in` Pre-market delivery in
- `pre_delivery_deduct` Pre-market delivery deduct
- `pre_margin_compensate_in` Pre-market margin compensate in
- `pre_margin_compensate_deduct` Pre-market margin compensate deduct
- `pre_fee_deduct` Pre-market fee deduct
- `pre_fee_return` Pre-market fee return
- `fee` Fee
- `rebate_rewards` Rebate rewards
- `channel_invite_reward` Channel invite reward
- `airdrop_rewards` Airdrop rewards
- `exchange_increase` Exchange increase
- `exchange_decrease` Exchange decrease
- `activity_grant` Activity grant
- `exchange_expense` Exchange expense
- `exchange_income` Exchange income
- `red_packet_expense` Red packet expense
- `red_packet_income` Red packet income
- `fee_return` Fee return
- `coupon_return` Coupon return
- `pre_recharge` Pre-recharge
- `cs_lock` Customer service lock
- `cs_unlock` Customer service unlock
- `hodler_yield` Hodler yield
- `finance_recycle` Finance recycle
- `contract_gift_expense` Contract gift expense
- `contract_gift_expire_income` Contract gift expire income
- `contract_gift_freeze_income` Contract gift freeze income
- `vip_airdrop_reward` VIP airdrop reward
- `cfd_trade_rebate` CFD trade rebate
- `dividend` Dividend
- `rebase_in` Rebase in
- `rebase_out` Rebase out
- `depth_quote_subscribe` Depth quote subscribe
- `on_chain_buy` On-chain buy
- `on_chain_sell` On-chain sell
- `on_chain_network_fee` On-chain network fee
- `on_chain_trade_fee` On-chain trade fee
- `on_chain_buy_freeze` On-chain buy freeze
- `on_chain_buy_freeze_return` On-chain buy freeze return
- `on_chain_withdraw_fee` On-chain withdraw fee
- `cfd_transfer_out` CFD transfer out
- `cfd_transfer_out_fail_refund` CFD transfer out fail refund
- `cfd_transfer_in` CFD transfer in
- `stock_deposit` Stock deposit
- `stock_deposit_fail_return` Stock deposit fail return
- `stock_withdraw` Stock withdraw

## symbolType
- `perpetual` Perpetual contract
- `delivery` Delivery contract

## status (instruments)
- `listed` Listed (not yet open)
- `online` Normal
- `limit_open` Order placement restricted
- `offline` Delisted / Under maintenance
- `restrictedAPI` API restricted


## deliveryStatus

- `delivery_config_period` Delivery configuration period
- `delivery_normal` Normal delivery period
- `delivery_before` Before delivery. No position opening is allowed 10 minutes
- `delivery_period` Delivery period. Opening, closing, and canceling orders is prohibited


## granularity
- `1m` (1 minute)
- `3m` (3 minutes)
- `5m` (5 minutes)
- `15m` (15 minutes)
- `30m` (30 minutes)
- `1H` (1 hour)
- `4H` (4 hours)
- `6H` (6 hours)
- `12H` (12 hours)
- `1D` (1 day)
- `3D` (3 days)
- `1W` (1 week)
- `1M` (1 month)
- `6Hutc` (zero time zone 6-hour line)
- `12Hutc` (zero time zone 12-hour line)
- `1Dutc` (zero time zone 1-day line)
- `3Dutc` (zero time zone 3-day line)
- `1Wutc` (zero time zone 1-week line)
- `1Mutc` (zero time zone 1-month line)


## kLineType
- `MARK` mark price K line
- `INDEX` index price K line
- `MARKET` Market price K line

## cancelReason

- `normal_cancel`   Normal cancellation
- `trade_too_many_times_cancel`   Trading user restriction, only for special users
- `trade_count_too_small`   Order cancelled due to too small tradable quantity
- `trade_too_many_times_cancel`   Your order has been matched too many times and cannot continue to be filled
- `fok_not_full_cancel`   FOK order not fully filled
- `ioc_not_full_cancel`    IOC order not fully filled
- `post_only_fill_cancel`   Post-only order filled immediately upon placement
- `self_trade_cancel`   Self-trade cancellation
- `trade_max_deal_size_cancel`  Your order has been filled too many times and cannot continue to be filled
- `tpsl_plan_cancel`  Cancelled by conditional trigger
- `back_contract_cancel`  Reverse position cancellation
- `delegated_risk_order_cancel`  Risk control cancellation of delegated orders
- `trader_order_cancel`  Copy trading order cancellation
- `delivery_order_cancel`  Delivery cancellation
- `modify_limit_order`  Limit order modification cancellation
- `slippage_cancel`  Cancelled due to slippage ratio
- `adl_cancel`  ADL cancellation
- `penetrate_cancel`  Liquidation risk control
- `stp_cancel`  Self-trade prevention cancellation
- `call_auction_cancel`  Order cancelled due to call auction failure
- `limit_price_exceed_cancel`  Order price exceeds limit range
- `burst_cancel`  All your orders are automatically cancelled as your account enters liquidation/reduction state
- `cancel_receiveWindow`  Order cancelled because the valid window period (receiveWindow) has expired

## tradeSide
- `open` Open
- `close` Close
- `open_long` Open long
- `close_long` Close long
- `open_short` Open Short
- `close_short` Close short
- `reduce_close_long`: Liquidate partial long positions for hedge position mode
- `reduce_close_short`：Liquidate partial short positions for hedge position mode
- `burst_close_long`：Liquidate long positions for hedge position mode
- `burst_close_short`：Liquidate short positions for hedge position mode
- `offset_close_long`：Liquidate partial long positions for netting for hedge position mode
- `offset_close_short`：Liquidate partial short positions for netting for hedge position mode
- `delivery_close_long`：Delivery long positions for hedge position mode
- `delivery_close_short`：Delivery short positions for hedge position mode
- `dte_sys_adl_close_long`：ADL close long position for hedge position mode
- `dte_sys_adl_close_short`：ADL close short position for hedge position mode
- `buy_single`：Buy, one way postion mode
- `sell_single`：Sell, one way postion mode
- `reduce_buy_single`：Liquidate partial positions, buy, one way position mode
- `reduce_sell_single`：Liquidate partial positions, sell, one way position mode
- `burst_buy_single`：Liquidate short positions, buy, one way postion mode
- `burst_sell_single`：Liquidate partial positions, sell, one way position mode
- `delivery_sell_single`：Delivery sell, one way position mode
- `delivery_buy_single`：Delivery buy, one way position mode
- `dte_sys_adl_buy_in_single_side_mode`：ADL close position, buy, one way position mode
- `dte_sys_adl_sell_in_single_side_mode`：ADL close position, sell, one way position mode
- `dte_migrate_position_open_long`：Migrate position, open long, hedge position mode
- `dte_migrate_position_open_short`：Migrate position, open short, hedge position mode
- `dte_migrate_position_close_long`：Migrate position, close long, hedge position mode
- `dte_migrate_position_close_short`：Migrate position, close short, hedge position mode
- `dte_migrate_position_buy_in_single_side_mode`：Migrate position, buy, one way position mode
- `dte_migrate_position_sell_in_single_side_mode`：Migrate position, sell, one way position mode
- `dte_rebase_open_long`：Split/merge shares, open long, hedge position mode
- `dte_rebase_open_short`：Split/merge shares, open short, hedge position mode
- `dte_rebase_close_long`：Split/merge shares, close long, hedge position mode
- `dte_rebase_close_short`：Split/merge shares, close short, hedge position mode
- `dte_rebase_buy_in_single_side_mode`：Split/merge shares, buy, one way position mode
- `dte_rebase_sell_in_single_side_mode`：Split/merge shares, sell, one way position mode

## Tax type

- `TRANSFER_IN` Transfer In
- `TRANSFER_OUT` Transfer Out
- `ORDER_DEALT_FROZEN_OUT` Order Dealt Deduction - User Out
- `ORDER_DEALT_IN` Order Dealt In - User In
- `ORDER_PLF_FEE_OUT` Exchange Token Fee Deduction - User Out
- `REPAY_SOURCE_USER_OUT` Repayment Out - User Out
- `REPAY_TARGET_USER_IN` Repayment In - User In
- `OPEN_LONG` Open Long Position Successfully
- `OPEN_SHORT` Open Short Position Successfully
- `BUY_DEAL` Buy Executed in Single-Side Mode
- `SELL_DEAL` Sell Executed in Single-Side Mode
- `CLOSE_LONG` Close Long
- `CLOSE_SHORT` Close Short
- `FORCE_CLOSE_LONG` Forced Reduce Long
- `FORCE_CLOSE_SHORT` Forced Reduce Short
- `BURST_CLOSE_LONG` Liquidation Close Long
- `BURST_CLOSE_SHORT` Liquidation Close Short
- `OFFSET_REDUCE_CLOSE_LONG` Net-Off Forced Reduce Long
- `OFFSET_REDUCE_CLOSE_SHORT` Net-Off Forced Reduce Short
- `FORCE_BUY_SSM` Forced Buy
- `FORCE_SELL_SSM` Forced Sell
- `BURST_BUY_SSM` Liquidation Buy
- `BURST_SELL_SSM` Liquidation Sell
- `RISK_LIQ_USER_IN` Risk Control - Debt Liquidation User In
- `RISK_LIQ_USER_OUT` Risk Control - Debt Liquidation User Out
- `INTEREST_SETTLEMENT_OUT` Interest Deduction - User Out
- `CONTRACT_MAIN_SETTLE_FEE_USER_IN` Cross Margin Funding Fee - User In
- `CONTRACT_MAIN_SETTLE_FEE_USER_OUT` Cross Margin Funding Fee - User Out
- `PAPTRADING_USER_IN` Demo Fund In - User In
- `PAPTRADING_USER_OUT` Demo Fund Out - User Out
- `RISK_TARGET_USER_IN` Forced Liquidation In - User In
- `RISK_SOURCE_USER_OUT` Forced Liquidation Out - User Out
- `ADL_CLOSE_LONG` ADL Close Long
- `ADL_CLOSE_SHORT` ADL Close Short
- `ADL_BUY_IN_SINGLE_SIDE_MODE` ADL Buy (Single-Side Mode)
- `ADL_SELL_IN_SINGLE_SIDE_MODE` ADL Sell (Single-Side Mode)
- `INS_LOAN_DISBURSE_USER_IN` Institutional Loan Disbursement - User In
- `INS_LOAN_DISBURSE_RESERVE_USER_OUT` Institutional Loan Disbursement to Reserve - User Out
- `INS_LOAN_REPAY_POOL_USER_OUT` Institutional Loan Repayment to Pool - User Out
- `INS_LOAN_REPAY_INTEREST_USER_OUT` Institutional Loan Repayment to Interest - User Out
- `INS_LOAN_REPAY_RESERVE_USER_IN` Institutional Loan Repayment to Reserve - User In
- `INS_LOAN_REPAY_FUND_USER_IN` Institutional Loan Repayment to Risk Fund - User In
- `INS_LOAN_EXCHANGE_USER_IN` Institutional Loan - Forced Liquidation Swap - User In
- `INS_LOAN_EXCHANGE_USER_OUT` Institutional Loan - Forced Liquidation Swap - User Out
- `INS_LOAN_TRANSFER_USER_IN` Institutional Loan - Forced Liquidation Transfer - User In
- `INS_LOAN_TRANSFER_USER_OUT` Institutional Loan - Forced Liquidation Transfer - User Out
- `INS_LOAN_REPAY_FEE_USER_OUT` Institutional Loan Repayment - Forced Liquidation Fee - User Out
- `INS_LOAN_REPAY_NON_MARGIN_USER_OUT` Institutional Loan Repayment - Forced Liquidation Recovery - User Out
- `DELIST_MARGIN_TOKEN_TARGET_USER_IN` Margin Delisted Token Redeem In - User In
- `DELIST_MARGIN_TOKEN_SOURCE_USER_OUT` Margin Delisted Token Redeem Out - User Out
- `SYSTEM_TRANSFER_OUT` System Transfer Out
- `SYSTEM_TRANSFER_IN` System Transfer In
- `SMALL_ASSET_SOURCE_TOKEN_USER_OUT` Small Asset Conversion - Source Token Out - User Out
- `SMALL_ASSET_TARGET_TOKEN_USER_IN` Small Asset Conversion - Target Token In - User In
- `FIXED_OPEN_LONG` Isolated Margin Open Long Position Successfully
- `FIXED_OPEN_SHORT` Isolated Margin Open Short Position Successfully
- `FIXED_BUY_DEAL` Isolated Margin Open Buy Executed (Single-Side)
- `FIXED_SELL_DEAL` Isolated Margin Open Sell Executed (Single-Side)
- `FIXED_BACK` Isolated Margin Return
- `FIXED_INCREASE_MARGIN` Increase Isolated Margin
- `FIXED_REDUCE_MARGIN` Decrease Isolated Margin
- `FIXED_SETTLE_FEE_USER_IN` Isolated Margin Funding Fee - User In
- `FIXED_SETTLE_FEE_USER_OUT` Isolated Margin Funding Fee - User Out
- `FIXED_LEVER_POS_IN` Isolated Margin Leverage Adjustment - Increase Margin
- `FIXED_REDUCE_ONLY_OFFSET_IN_SSM_LONG` Isolated Margin Single-Side Mode Long Reduce Only
- `FIXED_REDUCE_ONLY_OFFSET_IN_SSM_SHORT` Isolated Margin Single-Side Mode Short Reduce Only
- `FIXED_OFFSET_IN_SSM_LONG` Isolated Margin Reduce Long
- `FIXED_OFFSET_IN_SSM_SHORT` Isolated Margin Reduce Short
- `FIXED_ORDER_PLACE_FROZEN` Isolated Margin Order Placed Frozen
- `FIXED_ORDER_FROZEN_RETURN` Isolated Margin Unfreeze Return
- `FIXED_CLOSE_LONG` Isolated Margin Close Long
- `FIXED_CLOSE_SHORT` Isolated Margin Close Short
- `FIXED_FORCE_CLOSE_LONG` Isolated Margin Forced Reduce Long
- `FIXED_FORCE_CLOSE_SHORT` Isolated Margin Forced Reduce Short
- `FIXED_BURST_CLOSE_LONG` Isolated Margin Liquidation Close Long
- `FIXED_BURST_CLOSE_SHORT` Isolated Margin Liquidation Close Short
- `FIXED_ADL_CLOSE_LONG` Isolated Margin ADL Close Long
- `FIXED_ADL_CLOSE_SHORT` Isolated Margin ADL Close Short
- `FIXED_RISK_LIQ_USER_IN` Isolated Margin Risk Control - Debt Liquidation User In
- `FIXED_RISK_LIQ_USER_OUT` Isolated Margin Risk Control - Debt Liquidation User Out
- `FIXED_FORCE_BUY_SSM` Isolated Margin Forced Buy
- `FIXED_FORCE_SELL_SSM` Isolated Margin Forced Sell
- `FIXED_BURST_BUY_SSM` Isolated Margin Liquidation Buy
- `FIXED_BURST_SELL_SSM` Isolated Margin Liquidation Sell

---

# 枚举


## category

- `SPOT`  现货
- `MARGIN`  现货杠杆
- `USDT-FUTURES`  U本位合约
- `COIN-FUTURES`  币本位合约
- `USDC-FUTURES`  USDC合约

## side

- `buy` 买
- `sell` 卖

## orderType

- `limit` 限价单
- `market` 市价单

## posSide

- `long` 多仓
- `short` 空仓

## timeInForce

- `gtc` Good 'til canceled. _普通订单, 订单将持续有效直到完全成交或被交易者手动取消。_
- `post_only` Post only. _订单不会立刻在市场成交，保证用户始终为 Maker。如果委托会立即与已有委托成交，那么该委托会被取消。_
- `fok` Fill or Kill. _订单必须立即以委托价或更优的价格成交，否则将被完全取消。不允许部分成交。_
- `ioc` Immediate or cancel. _订单必须立即以限价或更优的价格成交。如果订单无法立即成交，未成交的部分将被取消。_
- `rpi` Retail Price Improvement. _零售价格改善订单，以优于当前最优买卖价的价格与零售对手方撮合的限价单。_

## holdMode

- `one_way_mode`  单向持仓
- `hedge_mode`  双向持仓

## marginMode

- `crossed`  全仓模式
- `isolated`  逐仓模式

## reduceOnly

- `yes` 是只减仓单
- `no`  不是只减仓

## execType

- `normal`  常规订单
- `offset`  轧差订单(系统单)
- `reduce`  强制减仓订单(系统单)
- `liquidation`  爆仓订单(系统单)
- `delivery`  交割订单(系统单)

## orderStatus

- `live`  等待成交订单
- `new`  订单已进入撮合
- `partially_filled`  部分成交订单
- `filled`  已成交订单
- `cancelled`  已撤销订单

## tradeScope

- `taker`  主动吃单方
- `maker`  主动铺单方,提供流动性

## assetMode

- `union`  多币种保证金模式

## type (financial-record)

- `TRANSFER_IN` 转入
- `TRANSFER_OUT` 转出
- `CONVERSION_UPON_DELISTING` 自动借款-系统出账
- `ORDER_DEALT_FROZEN_OUT` 成交扣除-用户出账
- `ORDER_DEALT_IN` 成交入账-用户入账
- `ORDER_PLF_FEE_OUT` 交易平台币手续费抵扣-用户出账
- `EXCHANGE_SOURCE_TOKEN_USER_OUT` 还款兑出-用户出账
- `EXCHANGE_TARGET_TOKEN_USER_IN` 还款兑入-用户入账
- `OPEN_LONG` 开多仓位成功
- `OPEN_SHORT` 开空仓位成功
- `BUY_DEAL` 单边持仓时买成交
- `SELL_DEAL` 单边持仓时卖成交
- `CLOSE_LONG` 平多
- `CLOSE_SHORT` 平空
- `FORCE_CLOSE_LONG` 强制减多
- `FORCE_CLOSE_SHORT` 强制减空
- `BURST_CLOSE_LONG` 爆仓平多
- `BURST_CLOSE_SHORT` 爆仓平空
- `OFFSET_REDUCE_CLOSE_LONG` 扎差强制减多
- `OFFSET_REDUCE_CLOSE_SHORT` 扎差强制减空
- `FORCE_BUY_SSM` 强制买
- `FORCE_SELL_SSM` 强制卖
- `BURST_BUY_SSM` 爆仓买
- `BURST_SELL_SSM` 爆仓卖
- `RISK_LIQ_USER_IN` 风控-负债清算用户划入
- `INTEREST_SETTLEMENT_OUT` 扣息-用户出账
- `CONTRACT_MAIN_SETTLE_FEE_USER_IN` 全仓资金费用普通用户转入
- `CONTRACT_MAIN_SETTLE_FEE_USER_OUT` 全仓资金费用普通用户转出
- `RISK_LIQ_USER_OUT` 风控-负债清算用户转出
- `BORROW` 机构借贷放款-用户入
- `RESERVE_TRANSFER_IN` 机构借贷还款-备付金-用户入
- `RESERVE_TRANSFER_OUT` 机构借贷放款备付金-用户出
- `REPAYMENT` 机构借贷-还款到借贷池-用户出
- `INTEREST_REPAYMENT` 机构借贷-还款到利息-用户出
- `LIQ_FUND_OUT` 机构借贷还款-风险基金-系统出
- `LIQ_CONVERT_USER_OUT` 机构借贷-强平兑换-用户出
- `LIQ_CONVERT_SYS_IN` 机构借贷-强平兑换-系统入
- `LIQ_CONVERT_SYS_OUT` 机构借贷-强平兑换-系统出
- `LIQ_CONVERT_USER_IN` 机构借贷-强平兑换-用户入
- `LIQ_TRANSFER_IN` 机构借贷-强平划转-用户入
- `LIQ_TRANSFER_OUT` 机构借贷-强平划转-用户出
- `LIQ_FUND_IN` 机构借贷还款-风险基金-用户入
- `LIQ_FEE` 机构借贷还款-强平手续费-用户出
- `LIQ_REPAYMENT` 机构借贷还款-强平回收-用户出
- `DELIST_MARGIN_TOKEN_SOURCE_USER_OUT` 保证金币种下架兑出-用户出账
- `DELIST_MARGIN_TOKEN_SOURCE_SYS_IN` 保证金币种下架兑入-系统入账
- `DELIST_MARGIN_TOKEN_TARGET_SYS_OUT` 保证金币种下架兑出-系统出账
- `DELIST_MARGIN_TOKEN_TARGET_USER_IN` 保证金币种下架兑入-用户入账
- `CONFISCATE_TOKEN_USER_OUT` 没收资产-用户出账
- `CONFISCATE_TOKEN_SYS_IN` 没收资产-系统入账
- `DELIST_SMALL_BALANCE_USER_OUT` 保证金币种下架-小额资产-用户出
- `DELIST_SMALL_BALANCE_SYS_IN` 保证金币种下架-小额资产-系统入
- `DELIST_SMALL_LIABILITY_SYS_OUT` 保证金币种下架-小额负债-系统出
- `DELIST_SMALL_LIABILITY_USER_IN` 保证金币种下架-小额负债-用户入
- `SMALL_ASSET_SOURCE_TOKEN_USER_OUT` 小额兑换-源币种-用户出
- `SMALL_ASSET_SOURCE_TOKEN_SYS_IN` 小额兑换-源币种-系统入
- `SMALL_ASSET_TARGET_TOKEN_SYS_OUT` 小额兑换-目标币种-系统出
- `SMALL_ASSET_TARGET_TOKEN_USER_IN` 小额兑换-目标币种-用户入
- `SMALL_ASSET_FEE_SYS_IN` 小额兑换-手续费-系统入
- `TRACE_SHARE_BENEFIT_USER_OUT` 跟单分润-用户出
- `TRACE_SHARE_BENEFIT_SYSTEM_IN` 跟单分润-系统入
- `TRACE_SHARE_BENEFIT_SYSTEM_OUT` 跟单分润-系统出
- `TRACE_SHARE_BENEFIT_USER_IN` 跟单分润-用户入
- `MARGIN_OPEN_LONG` 逐仓开多仓位成功
- `MARGIN_OPEN_SHORT` 逐仓开空仓位成功
- `MARIN_BUY_DEAL` 逐仓单边持仓时开仓买成交
- `MARIN_SELL_DEAL` 逐仓单边持仓时开仓卖成交
- `MARGIN_BACK` 逐仓返还
- `INCREASE_MARGIN` 增加逐仓保证金
- `REDUCE_MARGIN` 减少逐仓保证金
- `MARGIN_SETTLE_FEE_USER_IN` 逐仓资金费用普通用户转入
- `MARGIN_SETTLE_FEE_USER_OUT` 逐仓资金费用普通用户转出
- `MARGIN_LEVER_ORDER_REFROZEN` 逐仓调整杠杆订单释放冻结
- `MARGIN_LEVER_ORDER_FROZEN` 逐仓调整杠杆订单增加冻结
- `MARGIN_LEVER_POS_IN` 逐仓调整杠杆仓位增加保证金
- `MARGIN_OFFSET_IN_SSM_LONG` 逐仓单边持仓时多头只减仓
- `MARGIN_OFFSET_IN_SSM_SHORT` 逐仓单边持仓时空头只减仓
- `FIXED_OFFSET_IN_SSM_LONG` 逐仓减多
- `FIXED_OFFSET_IN_SSM_SHORT` 逐仓减空
- `FIXED_CLOSE_LONG` 逐仓平多
- `FIXED_CLOSE_SHORT` 逐仓平空
- `FIXED_FORCE_CLOSE_LONG` 逐仓强制减多
- `FIXED_FORCE_CLOSE_SHORT` 逐仓强制减空
- `FIXED_BURST_CLOSE_LONG` 逐仓爆仓平多
- `FIXED_BURST_CLOSE_SHORT` 逐仓爆仓平空
- `FIXED_ADL_CLOSE_LONG` 逐仓ADL平多
- `FIXED_ADL_CLOSE_SHORT` 逐仓ADL平空
- `FIXED_RISK_LIQ_USER_IN` 逐仓风控-负债清算用户划入
- `FIXED_RISK_LIQ_USER_OUT` 逐仓风控-负债清算用户转出
- `FIXED_FORCE_BUY_SSM` 逐仓强制买
- `FIXED_FORCE_SELL_SSM` 逐仓强制卖
- `FIXED_BURST_BUY_SSM` 逐仓爆仓买
- `FIXED_BURST_SELL_SSM` 逐仓爆仓卖
- `ON_CHAIN_TRANSFER_REFUND` 链上交易-用户入
- `ON_CHAIN_TRANSFER_OUT` 链上交易-用户出
- `MT5_TRANSFER_IN` 从MT5转入
- `MT5_REFUND_IN` MT5转出退回
- `MT5_TRANSFER_OUT` 转出到MT5
- `TRACE_LOCK_USER_OUT` 跟单冻结-用户出
- `TRACE_LOCK_USER_IN` 跟单冻结-用户入
- `TRACE_TRANSFER_USER_OUT` 跟单-从UTA到资金账户
- `TRACE_TRANSFER_USER_IN` 跟单-资金账户到UTA子账户
- `TRACE_TRANSFER_REFUND_IN` 跟单-资金账户退回UTA
- `FINANCIAL_TRANSFER_OUT` 理财划转-用户出
- `FINANCIAL_TRANSFER_IN` 理财划入-用户入
- `CONVERT_TRANSFER_IN` 闪兑-转入
- `CONVERT_TRANSFER_OUT` 闪兑-转出
- `BGPAY_TRANSFER_OUT` BG支付-转出
- `BGPAY_REFUND_IN` BG支付-退回
- `RWA_FIXED_SETTLE_FEE_USER_IN` RWA派息逐仓资金费用普通用户转入
- `RWA_FIXED_SETTLE_FEE_USER_OUT` RWA派息逐仓资金费用普通用户转出
- `RWA_CONTRACT_MAIN_SETTLE_FEE_SYSTEM_IN` RWA派息全仓资金费用归集账户转入
- `RWA_CONTRACT_MAIN_SETTLE_FEE_SYSTEM_OUT` RWA派息全仓资金费用归集账户转出
- `RWA_CONTRACT_MAIN_SETTLE_FEE_SYSTEM_KEEP_IN` RWA派息全仓资金费用留存账户转入
- `RWA_CONTRACT_MAIN_SETTLE_FEE_SYSTEM_KEEP_OUT` RWA派息全仓资金费用留存账户转出
- `RWA_CONTRACT_MAIN_SETTLE_FEE_USER_IN` RWA派息全仓资金费用普通用户转入
- `RWA_CONTRACT_MAIN_SETTLE_FEE_USER_OUT` RWA派息全仓资金费用普通用户转出
- `RWA_CONTRACT_REBASE_USER_OPEN_LONG` RWA合约拆合股开多
- `RWA_CONTRACT_REBASE_USER_OPEN_SHORT` RWA合约拆合股开空
- `RWA_CONTRACT_REBASE_USER_CLOSE_LONG` RWA合约拆合股平多
- `RWA_CONTRACT_REBASE_USER_CLOSE_SHORT` RWA合约拆合股平空
- `RWA_CONTRACT_REBASE_USER_BUY_IN_SSM` RWA合约拆合股单向持仓买入
- `RWA_CONTRACT_REBASE_USER_SELL_IN_SSM` RWA合约拆合股单向持仓卖出
- `RISK_LIQ_DEFAULT_USER_IN` 风控-负债清算用户划入
- `FIXED_RISK_LIQ_DEFAULT_USER_IN` 逐仓风控-负债清算用户划入
- `BONUS_GRANT_USER_IN` 体验金-用户入账
- `BONUS_EXPIRE_USER_OUT` 体验金过期-用户出账
- `BONUS_TRANSFER_USER_OUT` 体验金划转过期-用户出账
- `WITHDRAW_TRANSFER_OUT` 提币-转出
- `WITHDRAW_TRANSFER_IN` 提币-退回
- `DELIVERY_LONG` 多头交割
- `DELIVERY_SHORT` 空头交割
- `FIXED_DELIVERY_LONG` 逐仓多头交割
- `FIXED_DELIVERY_SHORT` 逐仓空头交割
- `REBASE_COIN_SPLIT_OUT` 拆合股-拆股出账
- `REBASE_COIN_SPLIT_IN` 拆合股-拆股入账
- `REBASE_COIN_MERGE_OUT` 拆合股-合股出账
- `REBASE_COIN_MERGE_IN` 拆合股-合股入账


## groupType (funding financial records)
- `transaction` 交易
- `deposit` 充值
- `withdraw` 提现
- `transfer` 划转
- `other` 其他
- `financial` 理财
- `strategy` 策略
- `trace` 跟单
- `loan` 质押借贷
- `fait` 法币
- `convert` 闪兑
- `ipo_prime` IPO Prime
- `pre_c2c` 盘前交易
- `paptrading` 模拟资金变动
- `on_chain` 链上交易
- `debit` 借贷中台
- `cfd` CFD
- `pay` 支付
- `compliance_wall` 合规墙
- `live` 直播打赏
- `broker` 代理商
- `rwa` RWA公司行动
- `stock` 证券


## type (funding financial records)
- `buy` 买入
- `sell` 卖出
- `deduction_handling_fee` 手续费抵扣
- `withholding_tax` 代收税款
- `deposit` 链上充值
- `inner_transfer_recharge` 内部转账
- `inner_chain_recharge` 内部链充值
- `recharge_receive` 充值-收款
- `withdraw` 提现
- `inner_withdraw` 内部提现
- `inner_addr_withdraw` 内部地址提现
- `withdraw_transfer` 提现-转账
- `transfer_in` 转入
- `transfer_out` 转出
- `robot_close` 机器人交易平仓
- `strategy_open` 策略交易开仓
- `robot_account_transfer_in` 由交易机器人账户转入
- `robot_account_transfer_out` 转出到交易机器人账户
- `cross_site_transfer_out` 跨站点资金转出
- `cross_site_transfer_in` 跨站点资金转入
- `on_chain_trade_transfer_in` 链上交易转入
- `pay` 支付
- `pay_refund` 退款
- `dual_invest_subscribe` 双币投资申购
- `interest` 利息
- `discount_subscribe` 打折认购申购
- `discount_allocate` 打折认购分配
- `savings_flexible_subscribe` 简单赚币活期申购
- `savings_flexible_redeem` 简单赚币活期赎回
- `savings_flexible_profit` 简单赚币活期收益
- `savings_fixed_subscribe` 简单赚币定期申购
- `savings_fixed_redeem` 简单赚币定期赎回
- `trend_subscribe` 趋势智盈申购
- `trend_settle` 趋势智盈结算
- `range_subscribe` 区间猎手申购
- `range_settle` 区间猎手结算
- `on_chain_earn_stake` 链上赚币质押
- `on_chain_earn_redeem` 链上赚币赎回
- `bgb_stake` 质押 BGB 质押
- `bgb_redeem` 质押 BGB 赎回
- `snowball_subscribe` 雪球申购
- `snowball_settle` 雪球结算
- `wealth_subscribe` 财富管理申购
- `wealth_redeem` 财富管理赎回
- `spot_dca_subscribe` 现货定投+申购
- `spot_dca_redeem` 现货定投+赎回
- `flexible_interest` 活期利息
- `robot_buy_expense` 交易机器人购买支出
- `robot_subscribe_expense` 订阅交易机器人专家支出
- `robot_refund` 交易机器人退款
- `robot_subscribe_refund` 订阅交易机器人专家退款
- `robot_expert_income` 交易机器人专家收入
- `robot_trace_profit_income` 交易机器人带单分润收入
- `trace_profit_expense` 跟单-分润支出
- `trace_profit_income` 带单-分润收入
- `trace_profit_return` 跟单-分润返还
- `pledge_deduct` 质押扣减
- `pledge_return` 质押退还
- `loan_disburse` 借贷放款
- `loan_repay` 借贷还款
- `liquidation_return` 强平返还
- `collateral_repay_loan_return` 抵押品还款–借贷退还
- `supplement_pledge_deduct` 补充质押扣减
- `release_pledge` 释放质押
- `collateral_repay_pledge_return` 抵押品还款–质押退还
- `liquidation_loan_return` 强平–借贷退还
- `liquidation_pledge_return` 强平–质押退还
- `pledge_rollback` 质押回退
- `convert_consume` 闪兑消耗
- `convert_gain` 闪兑获得
- `ipo_prime_trade_in` IPO Prime 交易入账
- `ipo_prime_trade_pay` IPO Prime 交易支付
- `ipo_prime_subscribe_expense` IPO Prime 认购支出
- `ipo_prime_subscribe_income` IPO Prime 认购收入
- `pre_delivery_in` 交割入账
- `pre_delivery_deduct` 交割扣除
- `pre_margin_compensate_in` 保证金赔付入账
- `pre_margin_compensate_deduct` 保证金赔付扣除
- `pre_fee_deduct` 手续费扣除
- `pre_fee_return` 手续费退还
- `fee` 手续费
- `rebate_rewards` 返佣奖励
- `channel_invite_reward` 渠道拉新奖励
- `airdrop_rewards` 空投奖励
- `exchange_increase` 兑换增加
- `exchange_decrease` 兑换减少
- `activity_grant` 活动发放
- `exchange_expense` 兑换支出
- `exchange_income` 兑换收入
- `red_packet_expense` 红包支出
- `red_packet_income` 红包收入
- `fee_return` 手续费返还
- `coupon_return` 卡券返还
- `pre_recharge` 预充值
- `cs_lock` 客服锁仓
- `cs_unlock` 客服锁仓解锁
- `hodler_yield` HodlerYield
- `finance_recycle` 财务回收
- `contract_gift_expense` 合约礼盒支出
- `contract_gift_expire_income` 合约礼盒过期收入
- `contract_gift_freeze_income` 合约礼盒冻结收入
- `vip_airdrop_reward` VIP 空投奖励
- `cfd_trade_rebate` CFD 交易返佣
- `dividend` 派息
- `rebase_in` Rebase 入账
- `rebase_out` Rebase 出账
- `depth_quote_subscribe` 深度行情权益订阅
- `on_chain_buy` 买入
- `on_chain_sell` 卖出
- `on_chain_network_fee` 网络费
- `on_chain_trade_fee` 交易手续费
- `on_chain_buy_freeze` 购买资金冻结
- `on_chain_buy_freeze_return` 购买资金冻结返还
- `on_chain_withdraw_fee` 提现手续费
- `cfd_transfer_out` 转出到 CFD 账户
- `cfd_transfer_out_fail_refund` 转出到 CFD 失败退款
- `cfd_transfer_in` 由 CFD 账户转入
- `stock_deposit` 证券入金
- `stock_deposit_fail_return` 证券入金失败退回
- `stock_withdraw` 证券出金


## symbolType

- `perpetual` 永续合约
- `delivery` 交割合约

## status(/instruments)

- `listed`  上架（未开盘）
- `online`  正常交易
- `limit_open`  限制交易(只允许平仓)
- `offline`    下线/维护
- `restrictedAPI`  限制API交易

## deliveryStatus

- `delivery_config_period` 新上币对配置中
- `delivery_normal` 正常交易
- `delivery_before` 交割前10分钟，禁止开仓
- `delivery_period` 交割中，禁止开平仓、撤单

## granularity

- `1m`  (1分钟)
- `3m`  (3分钟)
- `5m`  (5分钟)
- `15m`  (15分钟)
- `30m`  (30分钟)
- `1H`   (1小时)
- `4H`   (4小时)
- `6H`   (6小时)
- `12H`   (12小时)
- `1D`   (1天)
- `3D`   (3天)
- ``1W``   (1周)
- `1M`   (月线)
- `6Hutc`    (零时区 6小时线)
- `12Hutc`   (零时区12小时线)
- `1Dutc`    (零时区 1日线)
- `3Dutc`    (零时区 3日线)
- `1Wutc`    (零时区 周线)
- `1Mutc`    (零时区 月线)

## kLineType

- `MARK`   标记价格K线
- `INDEX`  指数价格K线
- `MARKET`  平台成交价格K线

## cancelReason

- `normal_cancel`   普通取消
- `trade_too_many_times_cancel`   成交用户限制，只有特殊用户才会有
- `trade_count_too_small`   可以成交的数量过小导致撤单
- `trade_too_many_times_cancel`   您的该委托，撮合次数过多，不能继续成交
- `fok_not_full_cancel`   FOK订单未完全成交
- `ioc_not_full_cancel`   IOC订单未完全成交
- `post_only_fill_cancel`   postOnly订单下单即成交
- `self_trade_cancel`   selfTrade撤销
- `trade_max_deal_size_cancel`  您的该委托，成交次数过多，不能继续成交
- `tpsl_plan_cancel`  条件触发撤销
- `back_contract_cancel`  反手撤销
- `delegated_risk_order_cancel`  委托风控撤单
- `trader_order_cancel`  带单撤销
- `delivery_order_cancel`  交割撤单
- `modify_limit_order`  限价修改撤销
- `slippage_cancel`  因滑点比例撤销
- `adl_cancel`  ADL 撤销
- `penetrate_cancel`  穿仓风控
- `stp_cancel`  自成交预防取消
- `call_auction_cancel`  集合竞价失败，订单撤销
- `limit_price_exceed_cancel`  订单价格超出限价范围
- `burst_cancel`  您的账户进入爆仓/减仓状态，自动撤销所有委托单
- `cancel_receiveWindow`  有效窗口期过期撤单

## tradeSide
- `open` 开
- `close` 平
- `open_long` 开多
- `close_long` 平多
- `open_short` 开空
- `close_short` 平空
- `reduce_close_long` 双向持仓强制减多
- `reduce_close_short` 双向持仓强制减空
- `offset_close_long` 双向持仓轧差强制减多
- `offset_close_short` 双向持仓轧差强制减空
- `burst_close_long` 双向持仓爆仓平多
- `burst_close_short` 双向持仓爆仓平空
- `delivery_close_long` 双向持仓多头交割
- `delivery_close_short` 双向持仓空头交割
- `dte_sys_adl_close_long` 双向持仓ADL减多仓
- `dte_sys_adl_close_short` 双向持仓ADL减空仓
- `buy_single` 单向持仓买
- `sell_single` 单向持仓卖
- `reduce_buy_single` 单向持仓强制减仓买
- `reduce_sell_single` 单向持仓强制减仓卖
- `burst_buy_single` 单向持仓爆仓买
- `burst_sell_single` 单向持仓爆仓卖
- `delivery_sell_single` 单向持仓交割卖
- `delivery_buy_single` 单向持仓交割买
- `dte_sys_adl_buy_in_single_side_mode` 单向持仓ADL减仓买
- `dte_sys_adl_sell_in_single_side_mode` 单向持仓ADL减仓卖
- `dte_migrate_position_open_long` 移仓开多
- `dte_migrate_position_open_short` 移仓开空
- `dte_migrate_position_close_long` 移仓平多
- `dte_migrate_position_close_short` 移仓平空
- `dte_migrate_position_buy_in_single_side_mode` 单向持仓移仓买
- `dte_migrate_position_sell_in_single_side_mode` 单向持仓移仓卖
- `dte_rebase_open_long` 拆合股开多
- `dte_rebase_open_short` 拆合股开空
- `dte_rebase_close_long` 拆合股平多
- `dte_rebase_close_short` 拆合股平空
- `dte_rebase_buy_in_single_side_mode` 拆合股买入
- `dte_rebase_sell_in_single_side_mode` 拆合股卖出

## Tax type

- `TRANSFER_IN` 转入
- `TRANSFER_OUT` 转出
- `ORDER_DEALT_FROZEN_OUT` 成交扣除-用户出账
- `ORDER_DEALT_IN` 成交入帐-用户入账
- `ORDER_PLF_FEE_OUT` 交易平台币手续费抵扣-用户出账
- `REPAY_SOURCE_USER_OUT` 还款兑出-用户出账
- `REPAY_TARGET_USER_IN` 还款兑入-用户入账
- `OPEN_LONG` 开多仓位成功
- `OPEN_SHORT` 开空仓位成功
- `BUY_DEAL` 单边持仓时买成交
- `SELL_DEAL` 单边持仓时卖成交
- `CLOSE_LONG` 平多
- `CLOSE_SHORT` 平空
- `FORCE_CLOSE_LONG` 强制减多
- `FORCE_CLOSE_SHORT` 强制减空
- `BURST_CLOSE_LONG` 爆仓平多
- `BURST_CLOSE_SHORT` 爆仓平空
- `OFFSET_REDUCE_CLOSE_LONG` 扎差强制减多
- `OFFSET_REDUCE_CLOSE_SHORT` 扎差强制减空
- `FORCE_BUY_SSM` 强制买
- `FORCE_SELL_SSM` 强制卖
- `BURST_BUY_SSM` 爆仓买
- `BURST_SELL_SSM` 爆仓卖
- `RISK_LIQ_USER_IN` 风控-负债清算用户划入
- `RISK_LIQ_USER_OUT` 风控-负债清算用户转出
- `INTEREST_SETTLEMENT_OUT` 扣息-用户出账
- `CONTRACT_MAIN_SETTLE_FEE_USER_IN` 全仓资金费用普通用户转入
- `CONTRACT_MAIN_SETTLE_FEE_USER_OUT` 全仓资金费用普通用户转出
- `PAPTRADING_USER_IN` 模拟金-用户入账
- `PAPTRADING_USER_OUT` 模拟金-用户出账
- `RISK_TARGET_USER_IN` 强平兑入-用户入账
- `RISK_SOURCE_USER_OUT` 强平兑出-用户出账
- `ADL_CLOSE_LONG` ADL平多
- `ADL_CLOSE_SHORT` ADL平空
- `ADL_BUY_IN_SINGLE_SIDE_MODE` ADL买入
- `ADL_SELL_IN_SINGLE_SIDE_MODE` ADL卖出
- `INS_LOAN_DISBURSE_USER_IN` 机构借贷放款-用户入
- `INS_LOAN_DISBURSE_RESERVE_USER_OUT` 机构借贷放款-备付金-用户出
- `INS_LOAN_REPAY_POOL_USER_OUT` 机构借贷-还款到借贷池-用户出
- `INS_LOAN_REPAY_INTEREST_USER_OUT` 机构借贷-还款到利息-用户出
- `INS_LOAN_REPAY_RESERVE_USER_IN` 机构借贷还款-备付金-用户入
- `INS_LOAN_REPAY_FUND_USER_IN` 机构借贷还款-风险基金-用户入
- `INS_LOAN_EXCHANGE_USER_IN` 机构借贷-强平兑换-用户入
- `INS_LOAN_EXCHANGE_USER_OUT` 机构借贷-强平兑换-用户出
- `INS_LOAN_TRANSFER_USER_IN` 机构借贷-强平划转-用户入
- `INS_LOAN_TRANSFER_USER_OUT` 机构借贷-强平划转-用户出
- `INS_LOAN_REPAY_FEE_USER_OUT` 机构借贷还款-强平手续费-用户出
- `INS_LOAN_REPAY_NON_MARGIN_USER_OUT` 机构借贷还款-强平回收-用户出
- `DELIST_MARGIN_TOKEN_TARGET_USER_IN` 保证金币种下架兑入-用户入账
- `DELIST_MARGIN_TOKEN_SOURCE_USER_OUT` 保证金币种下架兑出-用户出账
- `SYSTEM_TRANSFER_OUT` 系统转出
- `SYSTEM_TRANSFER_IN` 系统转入
- `SMALL_ASSET_SOURCE_TOKEN_USER_OUT` 小额兑换-源币种-用户出
- `SMALL_ASSET_TARGET_TOKEN_USER_IN` 小额兑换-目标币种-用户入
- `FIXED_OPEN_LONG` 逐仓开多仓位成功
- `FIXED_OPEN_SHORT` 逐仓开空仓位成功
- `FIXED_BUY_DEAL` 逐仓单边持仓时开仓买成交
- `FIXED_SELL_DEAL` 逐仓单边持仓时开仓卖成交
- `FIXED_BACK` 逐仓返还
- `FIXED_INCREASE_MARGIN` 增加逐仓保证金
- `FIXED_REDUCE_MARGIN` 减少逐仓保证金
- `FIXED_SETTLE_FEE_USER_IN` 逐仓资金费用普通用户转入
- `FIXED_SETTLE_FEE_USER_OUT` 逐仓资金费用普通用户转出
- `FIXED_LEVER_POS_IN` 逐仓调整杠杆仓位增加保证金
- `FIXED_REDUCE_ONLY_OFFSET_IN_SSM_LONG` 逐仓单边持仓时多头只减仓
- `FIXED_REDUCE_ONLY_OFFSET_IN_SSM_SHORT` 逐仓单边持仓时空头只减仓
- `FIXED_OFFSET_IN_SSM_LONG` 逐仓减多
- `FIXED_OFFSET_IN_SSM_SHORT` 逐仓减空
- `FIXED_ORDER_PLACE_FROZEN` 逐仓挂单冻结
- `FIXED_ORDER_FROZEN_RETURN` 交易冻结返还
- `FIXED_CLOSE_LONG` 逐仓平多
- `FIXED_CLOSE_SHORT` 逐仓平空
- `FIXED_FORCE_CLOSE_LONG` 逐仓强制减多
- `FIXED_FORCE_CLOSE_SHORT` 逐仓强制减空
- `FIXED_BURST_CLOSE_LONG` 逐仓爆仓平多
- `FIXED_BURST_CLOSE_SHORT` 逐仓爆仓平空
- `FIXED_ADL_CLOSE_LONG` 逐仓ADL平多
- `FIXED_ADL_CLOSE_SHORT` 逐仓ADL平空
- `FIXED_RISK_LIQ_USER_IN` 逐仓风控-负债清算用户划入
- `FIXED_RISK_LIQ_USER_OUT` 逐仓风控-负债清算用户转出
- `FIXED_FORCE_BUY_SSM` 逐仓强制买
- `FIXED_FORCE_SELL_SSM` 逐仓强制卖
- `FIXED_BURST_BUY_SSM` 逐仓爆仓买
- `FIXED_BURST_SELL_SSM` 逐仓爆仓卖