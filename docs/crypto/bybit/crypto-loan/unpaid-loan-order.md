---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/crypto-loan/unpaid-loan-order
api_type: REST
updated_at: 2026-05-27 19:16:30.565870
---

# Enums Definitions

### locale

  * `de-DE`
  * `en-US`
  * `es-AR`
  * `es-ES`
  * `es-MX`
  * `fr-FR`
  * `kk-KZ`
  * `id-ID`
  * `uk-UA`
  * `ja-JP`
  * `ru-RU`
  * `th-TH`
  * `pt-BR`
  * `tr-TR`
  * `vi-VN`
  * `zh-TW`
  * `ar-SA`
  * `hi-IN`
  * `fil-PH`



### announcementType

  * `new_crypto`
  * `latest_bybit_news`
  * `delistings`
  * `latest_activities`
  * `product_updates`
  * `maintenance_updates`
  * `new_fiat_listings`
  * `other`



### announcementTag

  * `Spot`
  * `Derivatives`
  * `Spot Listings`
  * `BTC`
  * `ETH`
  * `Trading Bots`
  * `USDC`
  * `Leveraged Tokens`
  * `USDT`
  * `Margin Trading`
  * `Partnerships`
  * `Launchpad`
  * `Upgrades`
  * `ByVotes`
  * `Delistings`
  * `VIP`
  * `Futures`
  * `Institutions`
  * `Options`
  * `WEB3`
  * `Copy Trading`
  * `Earn`
  * `Bybit Savings`
  * `Dual Asset`
  * `Liquidity Mining`
  * `Shark Fin`
  * `Launchpool`
  * `NFT GrabPic`
  * `Buy Crypto`
  * `P2P Trading`
  * `Fiat Deposit`
  * `Crypto Deposit`
  * `Спот`
  * `Спот лістинги`
  * `Торгові боти`
  * `Токени з кредитним плечем`
  * `Маржинальна торгівля`
  * `Партнерство`
  * `Оновлення`
  * `Делістинги`
  * `Ф'ючерси`
  * `Опціони`
  * `Копітрейдинг`
  * `Bybit Накопичення`
  * `Бівалютні інвестиції`
  * `Майнінг ліквідності`
  * `Купівля криптовалюти`
  * `P2P торгівля`
  * `Фіатні депозити`
  * `Криптодепозити`
  * `Копитрейдинг`
  * `Торговые боты`
  * `Деривативы`
  * `P2P`
  * `Спот листинги`
  * `Деривативи`
  * `MT4`
  * `Lucky Draw`
  * `Unified Trading Account`
  * `Єдиний торговий акаунт`
  * `Единый торговый аккаунт`
  * `Институциональный трейдинг`
  * `Інституціональний трейдинг`
  * `Делистинг`



### category

  * `spot`
  * `linear` USDT perpetual, USDT Futures and USDC contract, including USDC perp, USDC futures
  * `inverse` Inverse contract, including Inverse perp, Inverse futures
  * `option`



### orderStatus

 _open status_

  * `New` order has been placed successfully
  * `PartiallyFilled`
  * `Untriggered` Conditional orders are created



 _closed status_

  * `Rejected`
  * `PartiallyFilledCanceled` Only spot has this order status
  * `Filled`
  * `Cancelled` In derivatives, orders with this status may have an executed qty
  * `Triggered` instantaneous state for conditional orders from Untriggered to New
  * `Deactivated` UTA: Spot tp/sl order, conditional order, OCO order are cancelled before they are triggered



### timeInForce

  * `GTC` GoodTillCancel
  * `IOC` ImmediateOrCancel
  * `FOK` FillOrKill
  * [PostOnly](https://www.bybit.com/en/help-center/article/Post-Only-Order)
  * [RPI](https://www.bybit.com/en/help-center/article/Retail-Price-Improvement-RPI-Order) features:
    * **Exclusive Matching** : Only match non-algorithmic users; no execution against orders from Open API.
    * **Post-Only Mechanism** : Act as maker orders, adding liquidity
    * **Lower Priority** : Execute after non-RPI orders at the same price level.
    * **Limited Access** : Initially for select market makers across multiple pairs.
    * **Order Book Updates** : Excluded from API but displayed on the GUI.



### createType

  * `CreateByUser`
  * `CreateByFutureSpread` Spread order
  * `CreateByAdminClosing`
  * `CreateBySettle` USDC Futures delivery; position closed as a result of the delisting of a contract. This is recorded as a [trade](/docs/v5/order/execution) but not an [order](/docs/v5/order/order-list).
  * `CreateByStopOrder` Futures conditional order
  * `CreateByTakeProfit` Futures take profit order
  * `CreateByPartialTakeProfit` Futures partial take profit order
  * `CreateByStopLoss` Futures stop loss order
  * `CreateByPartialStopLoss` Futures partial stop loss order
  * `CreateByTrailingStop` Futures trailing stop order
  * `CreateByTrailingProfit` Futures trailing take profit order
  * `CreateByLiq` Laddered liquidation to reduce the required maintenance margin
  * `CreateByTakeOver_PassThrough`If the position is still subject to liquidation (i.e., does not meet the required maintenance margin level), the position shall be taken over by the liquidation engine and closed at the bankruptcy price.
  * `CreateByAdl_PassThrough` [Auto-Deleveraging(ADL)](https://www.bybit.com/en/help-center/article/Auto-Deleveraging-ADL)
  * `CreateByBlock_PassThrough` Order placed via Paradigm
  * `CreateByBlockTradeMovePosition_PassThrough` Order created by move position
  * `CreateByChaseOrder` Chase limit order
  * `CreateByFGridBot` Order created via grid bot
  * `CloseByFGridBot` Order closed via grid bot
  * `CreateByTWAP` Order created by TWAP
  * `CreateByMartingaleBot` Order created by Martingale bot
  * `CloseByMartingaleBot` Order closed by Martingale bot
  * `CreateByIceBerg` Order created by Ice berg strategy
  * `CreateByBboOrder` BBO order
  * `CreateByClosing` The close order placed via web or app position area - web/app
  * `CreateByTVSignal` Order created by TV webhook - web/app
  * `CreateByMmRateClose` Order created by Mm rate close function - web/app
  * `CreateByArbitrage` Order created by arbitrage - web/app
  * `CreateByDdh` Option dynamic delta hedge order - web/app



### execType

  * `Trade`
  * `AdlTrade` [Auto-Deleveraging](https://www.bybit.com/en/help-center/article/Auto-Deleveraging-ADL)
  * `Funding` [Funding fee](https://www.bybit.com/en/help-center/article/Introduction-to-Funding-Rate)
  * `BustTrade` Takeover liquidation
  * `Delivery` USDT futures delivery; Position closed due to delisting
  * `Settle` Inverse futures settlement
  * `BlockTrade`
  * `MovePosition`
  * `FutureSpread` Spread leg execution
  * `UNKNOWN` May be returned by a classic account. Cannot query by this type



### orderType

  * `Market`
  * `Limit`
  * `UNKNOWN` is not a valid request parameter value. Is only used in some responses. Mainly, it is used when `execType` is `Funding`.



### stopOrderType

  * `TakeProfit`
  * `StopLoss`
  * `TrailingStop`
  * `Stop`
  * `PartialTakeProfit`
  * `PartialStopLoss`
  * `tpslOrder` spot TP/SL order
  * `OcoOrder` spot Oco order
  * `MmRateClose` On web or app can set MMR to close position
  * `BidirectionalTpslOrder` Spot bidirectional tpsl order



### tickDirection

  * `PlusTick` price rise
  * `ZeroPlusTick` trade occurs at the same price as the previous trade, which occurred at a price higher than that for the trade preceding it
  * `MinusTick` price drop
  * `ZeroMinusTick` trade occurs at the same price as the previous trade, which occurred at a price lower than that for the trade preceding it



### interval

  * `1` `3` `5` `15` `30` `60` `120` `240` `360` `720` minute
  * `D` day
  * `W` week
  * `M` month



### intervalTime

  * `5min` `15min` `30min` minute
  * `1h` `4h` hour
  * `1d` day



### positionIdx

  * `0` one-way mode position
  * `1` Buy side of hedge-mode position
  * `2` Sell side of hedge-mode position



### positionStatus

  * `Normal`
  * `Liq` in the liquidation progress
  * `Adl` in the auto-deleverage progress



### rejectReason

  * `EC_NoError`
  * `EC_Others`
  * `EC_UnknownMessageType`
  * `EC_MissingClOrdID`
  * `EC_MissingOrigClOrdID`
  * `EC_ClOrdIDOrigClOrdIDAreTheSame`
  * `EC_DuplicatedClOrdID`
  * `EC_OrigClOrdIDDoesNotExist`
  * `EC_TooLateToCancel`
  * `EC_UnknownOrderType`
  * `EC_UnknownSide`
  * `EC_UnknownTimeInForce`
  * `EC_WronglyRouted`
  * `EC_MarketOrderPriceIsNotZero`
  * `EC_LimitOrderInvalidPrice`
  * `EC_NoEnoughQtyToFill`
  * `EC_NoImmediateQtyToFill` a maker could not be found to fill your order
  * `EC_PerCancelRequest`
  * `EC_MarketOrderCannotBePostOnly`
  * `EC_PostOnlyWillTakeLiquidity` your post only order would have executed as a taker, and so was rejected
  * `EC_CancelReplaceOrder`
  * `EC_InvalidSymbolStatus`
  * `EC_CancelForNoFullFill`
  * `EC_BySelfMatch`
  * `EC_InCallAuctionStatus` used for pre-market order operation, e.g., during 2nd phase of call auction, cancel order is not allowed, when the cancel request is failed to be rejected by trading server, the request will be rejected by matching box finally
  * `EC_QtyCannotBeZero`
  * `EC_MarketOrderNoSupportTIF`
  * `EC_ReachMaxTradeNum`
  * `EC_InvalidPriceScale`
  * `EC_BitIndexInvalid`
  * `EC_StopBySelfMatch`
  * `EC_InvalidSmpType`
  * `EC_CancelByMMP`
  * `EC_InvalidUserType`
  * `EC_InvalidMirrorOid`
  * `EC_InvalidMirrorUid`
  * `EC_EcInvalidQty`
  * `EC_InvalidAmount`
  * `EC_LoadOrderCancel`
  * `EC_MarketQuoteNoSuppSell`
  * `EC_DisorderOrderID`
  * `EC_InvalidBaseValue`
  * `EC_LoadOrderCanMatch`
  * `EC_SecurityStatusFail`
  * `EC_ReachRiskPriceLimit`
  * `EC_OrderNotExist`
  * `EC_CancelByOrderValueZero` order cancelled as its remaining value is zero
  * `EC_CancelByMatchValueZero` order cancelled as the order it matched with has a remaining value of zero
  * `EC_ReachMarketPriceLimit`



### accountType

  * `UNIFIED` Unified Trading Account
  * `FUND` Funding Account



### assetCategory

  * `Easy Earn` Earn account sub-category
  * `Futures Grid Bot` Trading Bot account sub-category
  * `Futures Combo Bot` Trading Bot account sub-category
  * `Futures Martingale Bot` Trading Bot account sub-category
  * `Copy Trading Classic` Copy Trading account sub-category
  * `Copy Trading TradFi` Copy Trading account sub-category
  * `Copy Trading Pro` Copy Trading account sub-category
  * `trade` Alpha account sub-category — spot alpha token holdings
  * `farm` Alpha account sub-category — spot alpha farming positions



### assetAccountType

  * `FundingAccount` Funding Account
  * `UnifiedTradingAccount` Unified Trading Account
  * `Earn` Earn Account
  * `TradingBot` Trading Bot Account
  * `CopyTrading` Copy Trading Account
  * `CryptoLoans` Crypto Loans Account
  * `CryptoLoans_legacy` Crypto Loans Account (Legacy)
  * `PayLater` Bybit Pay Later Account
  * `Launchpool` Launchpool Account
  * `TradFi` TradFi Account
  * `MarginStakedSOL` Margin Staked SOL Account
  * `Alpha` Alpha Account



### transferStatus

  * `SUCCESS`
  * `PENDING`
  * `FAILED`



### depositStatus

  * `0` unknown
  * `1` toBeConfirmed
  * `2` processing
  * `3` success (finalised status of a success deposit)
  * `4` deposit failed
  * `10011` pending to be credited to funding pool
  * `10012` Credited to funding pool successfully



### withdrawStatus

  * `SecurityCheck`
  * `Pending`
  * `success`
  * `CancelByUser`
  * `Reject`
  * `Fail`
  * `BlockchainConfirmed`
  * `MoreInformationRequired`
  * `Unknown` a rare status



### triggerBy

  * `LastPrice`
  * `IndexPrice`
  * `MarkPrice`



### cancelType

  * `CancelByUser`
  * `CancelByReduceOnly` cancelled by [reduceOnly](https://bybit-exchange.github.io/docs/v5/order/create-order)
  * `CancelByPrepareLiq` `CancelAllBeforeLiq` cancelled in order to attempt [liquidation prevention](https://www.bybit.com/en/help-center/article/Liquidation-Process-Derivatives-Standard-Account) by freeing up margin
  * `CancelByPrepareAdl` `CancelAllBeforeAdl` cancelled due to [ADL](https://www.bybit.com/en/help-center/article/Auto-Deleveraging-ADL)
  * `CancelByAdmin`
  * `CancelBySettle` cancelled due to delisting contract
  * `CancelByTpSlTsClear` TP/SL order cancelled when the position is cleared
  * `CancelBySmp` cancelled by [SMP](https://bybit-exchange.github.io/docs/v5/smp)
  * `CancelByDCP` cancelled by DCP triggering
  * `CancelByRebalance` Spread trading: the order price of a single leg order is outside the limit price range.
  * `CancelByOCOTpCanceledBySlTriggered` The take profit order was canceled due to the triggering of the stop loss
  * `CancelByOCOSlCanceledByTpTriggered` The stop loss order was canceled due to the triggering of the take profit



 _Options:_

  * `CancelByUser`
  * `CancelByReduceOnly`
  * `CancelAllBeforeLiq` cancelled due to liquidation
  * `CancelAllBeforeAdl` cancelled due to ADL
  * `CancelBySettle`
  * `CancelByCannotAffordOrderCost`
  * `CancelByPmTrialMmOverEquity`
  * `CancelByAccountBlocking`
  * `CancelByDelivery`
  * `CancelByMmpTriggered`
  * `CancelByCrossSelfMuch`
  * `CancelByCrossReachMaxTradeNum`
  * `CancelByDCP`
  * `CancelBySmp`



### optionPeriod

  * BTC: `7`,`14`,`21`,`30`,`60`,`90`,`180`,`270`days
  * ETH: `7`,`14`,`21`,`30`,`60`,`90`,`180`,`270`days
  * SOL: `7`,`14`,`21`,`30`,`60`,`90`days



### dataRecordingPeriod

  * `5min` `15min` `30min` minute
  * `1h` `4h` hour
  * `4d` day



### contractType

  * `InversePerpetual`
  * `LinearPerpetual`
  * `LinearFutures` USDT/USDC Futures
  * `InverseFutures`



### status

  * `PreLaunch`
  * `Trading`
  * `Delivering`
  * `Closed`



### symbolType

  * `innovation` linear
  * `adventure` spot
  * `xstocks` spot
  * `commodity` linear
  * `stock` linear
  * `forex` linear Foreign exchange



### curAuctionPhase

  * `NotStarted` Pre-market trading is not started
  * `Finished` Pre-market trading is finished
    * After the auction, if the pre-market contract fails to enter continues trading phase, it will be delisted and phase="Finished"
    * After the continuous trading, if the pre-market contract fails to be converted to official contract, it will be delisted and phase="Finished"
  * `CallAuction` Auction phase of pre-market trading
    * only timeInForce=GTC, orderType=Limit order is allowed to submit
    * TP/SL are not supported; Conditional orders are not supported
    * cannot **modify** the order at this stage
    * order price range: [[preOpenPrice](/docs/v5/market/tickers) x 0.5, [maxPrice](/docs/v5/market/instrument)]
  * `CallAuctionNoCancel` Auction no cancel phase of pre-market trading
    * only timeInForce=GTC, orderType=Limit order is allowed to submit
    * TP/SL are not supported; Conditional orders are not supported
    * cannot **modify and cancel** the order at this stage
    * order price range: Buy [[lastPrice](/docs/v5/market/tickers) x 0.5, [markPrice](/docs/v5/market/tickers) x 1.1], Sell [[markPrice](/docs/v5/market/tickers) x 0.9, [maxPrice](/docs/v5/market/instrument)]
  * `CrossMatching` cross matching phase
    * cannot **create, modify and cancel** the order at this stage
    * Candle data is released from this stage
  * `ContinuousTrading` Continuous trading phase
    * There is no restriction to create, amend, cancel orders
    * orderbook, public trade data is released from this stage



### marginTrading

  * `none` Regardless of normal account or UTA account, this trading pair does not support margin trading
  * `both` For both normal account and UTA account, this trading pair supports margin trading
  * `utaOnly` Only for UTA account,this trading pair supports margin trading
  * `normalSpotOnly` Only for normal account, this trading pair supports margin trading



### copyTrading

  * `none` Regardless of normal account or UTA account, this trading pair does not support copy trading
  * `both` For both normal account and UTA account, this trading pair supports copy trading
  * `utaOnly` Only for UTA account,this trading pair supports copy trading
  * `normalOnly` Only for normal account, this trading pair supports copy trading



### type(uta-translog)

  * `TRANSFER_IN` Assets that transferred into Unified wallet
  * `TRANSFER_OUT` Assets that transferred out from Unified wallet
  * `TRADE`
  * `SETTLEMENT` USDT Perp funding settlement, and USDC Perp funding settlement + USDC 8-hour session settlement
  * `DELIVERY` USDC Futures, Option delivery
  * `LIQUIDATION`
  * `ADL` Auto-Deleveraging
  * `AIRDROP`
  * `BONUS` Bonus claimed
  * `BONUS_RECOLLECT` Bonus expired
  * `FEE_REFUND` Trading fee refunded
  * `INTEREST` Interest occurred due to borrowing
  * `CURRENCY_BUY` Currency convert, and the liquidation for borrowing asset(UTA loan)
  * `CURRENCY_SELL` Currency convert, and the liquidation for borrowing asset(UTA loan)
  * `BORROWED_AMOUNT_INS_LOAN`
  * `PRINCIPLE_REPAYMENT_INS_LOAN`
  * `INTEREST_REPAYMENT_INS_LOAN`
  * `AUTO_SOLD_COLLATERAL_INS_LOAN` the liquidation for borrowing asset(INS loan)
  * `AUTO_BUY_LIABILITY_INS_LOAN` the liquidation for borrowing asset(INS loan)
  * `AUTO_PRINCIPLE_REPAYMENT_INS_LOAN`
  * `AUTO_INTEREST_REPAYMENT_INS_LOAN`
  * `TRANSFER_IN_INS_LOAN` Transfer In when in the liquidation of OTC loan
  * `TRANSFER_OUT_INS_LOAN` Transfer Out when in the liquidation of OTC loan
  * `SPOT_REPAYMENT_SELL` One-click repayment currency sell
  * `SPOT_REPAYMENT_BUY` One-click repayment currency buy
  * `TOKENS_SUBSCRIPTION` Spot leverage token subscription
  * `TOKENS_REDEMPTION` Spot leverage token redemption
  * `AUTO_DEDUCTION` Asset auto deducted by system (roll back)
  * `FLEXIBLE_STAKING_SUBSCRIPTION` Byfi flexible stake subscription
  * `FLEXIBLE_STAKING_REDEMPTION` Byfi flexible stake redemption
  * `FIXED_STAKING_SUBSCRIPTION` Byfi fixed stake subscription
  * `FLEXIBLE_STAKING_REFUND` Byfi flexiable stake refund
  * `FIXED_STAKING_REFUND` Byfi fixed stake refund
  * `PREMARKET_TRANSFER_OUT`
  * `PREMARKET_DELIVERY_SELL_NEW_COIN`
  * `PREMARKET_DELIVERY_BUY_NEW_COIN`
  * `PREMARKET_DELIVERY_PLEDGE_PAY_SELLER`
  * `PREMARKET_DELIVERY_PLEDGE_BACK`
  * `PREMARKET_ROLLBACK_PLEDGE_BACK`
  * `PREMARKET_ROLLBACK_PLEDGE_PENALTY_TO_BUYER`
  * `CUSTODY_NETWORK_FEE` fireblocks business
  * `CUSTODY_SETTLE_FEE` fireblocks business
  * `CUSTODY_LOCK` fireblocks / copper business
  * `CUSTODY_UNLOCK` fireblocks business
  * `CUSTODY_UNLOCK_REFUND` fireblocks business
  * `LOANS_BORROW_FUNDS` crypto loan
  * `LOANS_PLEDGE_ASSET` crypto loan repayment
  * `BONUS_TRANSFER_IN`
  * `BONUS_TRANSFER_OUT`
  * `PEF_TRANSFER_IN`
  * `PEF_TRANSFER_OUT`
  * `PEF_PROFIT_SHARE`
  * `ONCHAINEARN_SUBSCRIPTION` tranfer out for on chain earn
  * `ONCHAINEARN_REDEMPTION` tranfer in for on chain earn
  * `ONCHAINEARN_REFUND` tranfer in for on chain earn failed
  * `STRUCTURE_PRODUCT_SUBSCRIPTION` tranfer out for structure product
  * `STRUCTURE_PRODUCT_REFUND` tranfer in for structure product
  * `CLASSIC_WEALTH_MANAGEMENT_SUBSCRIPTION` tranfer out for classic wealth management
  * `PREMIMUM_WEALTH_MANAGEMENT_SUBSCRIPTION` tranfer in for classic wealth management
  * `PREMIMUM_WEALTH_MANAGEMENT_REFUND` tranfer in for classic wealth management refund
  * `LIQUIDITY_MINING_SUBSCRIPTION` tranfer out for liquidity mining
  * `LIQUIDITY_MINING_REFUND` tranfer in for liquidity mining
  * `PWM_SUBSCRIPTION` tranfer out for PWM
  * `PWM_REFUND` tranfer in for PWM
  * `DEFI_INVESTMENT_SUBSCRIPTION` tranfer out for DEFI subscription
  * `DEFI_INVESTMENT_REFUND` transfer in for DEFI refund
  * `DEFI_INVESTMENT_REDEMPTION` tranfer in for DEFI redemption
  * `INSTITUTION_LOAN_IN` Borrowed Amount (INS Loan)
  * `INSTITUTION_PAYBACK_PRINCIPAL_OUT` Principal repayment (INS Loan)
  * `INSTITUTION_PAYBACK_INTEREST_OUT` Interest repayment (INS Loan) 
  * `INSTITUTION_EXCHANGE_SELL` Auto sold collateral (INS Loan)
  * `INSTITUTION_EXCHANGE_BUY` Auto buy liability (INS Loan)
  * `INSTITUTION_LIQ_PRINCIPAL_OUT` Forced principal repayment, i.e. liquidation (INS Loan)
  * `INSTITUTION_LIQ_INTEREST_OUT` Forced interest repayment, i.e. liquidation (INS Loan)
  * `INSTITUTION_LOAN_TRANSFER_IN` Transfer in (INS Loan)
  * `INSTITUTION_LOAN_TRANSFER_OUT` Transfer out (INS Loan)
  * `INSTITUTION_LOAN_WITHOUT_WITHDRAW` Transfer out (INS Loan)
  * `INSTITUTION_LOAN_RESERVE_IN` Reserve fund in (INS Loan)
  * `INSTITUTION_LOAN_RESERVE_OUT` Reserve fund out (INS Loan)
  * `SPREAD_FEE_OUT` Spread fee for EU Broker
  * `PLATFORM_TOKEN_MNT_LIQRECALLEDMMNT` Recall MNT
  * `PLATFORM_TOKEN_MNT_LIQRETURNEDMNT` Return MNT
  * `BORROW` Manual loan borrow and auto loan borrow
  * `REPAY` Manual loan repay and auto loan repay
  * `CONVERT` Currency convert repayment
  * `BROKER_ABACCOUNT_FEE` Borker AB fee deduction
  * `EARNING_REDEMPTION_SELL`
  * `EARNING_REDEMPTION_BUY`
  * `DBS_CASH_OUT`
  * `DBS_CASH_IN`
  * `DBS_CASH_OUT_TR`
  * `DBS_CASH_IN_TR`
  * `CUSTODY_CASH_RECOVER_TR`
  * `ALPHA_SMALL_TOKEN_REFUND`
  * `TWAP_BUDGET_AIRDROP`
  * `TWAP_BUDGET_RECALL`
  * `FLOATING_TO_FIXED_BORROW`
  * `FLOATING_TO_FIXED_REPAY`
  * `IDN_CONVERT_IN`
  * `IDN_CONVERT_OUT`



### type(contract-translog)

  * `TRANSFER_IN` Assets that transferred into (inverse) derivatives wallet
  * `TRANSFER_OUT` Assets that transferred out from (inverse) derivatives wallet
  * `TRADE`
  * `SETTLEMENT` USDT / Inverse Perp funding settlement
  * `DELIVERY` Inverse Futures delivery
  * `LIQUIDATION`
  * `ADL` Auto-Deleveraging
  * `AIRDROP`
  * `BONUS` Bonus claimed
  * `BONUS_RECOLLECT` Bonus expired
  * `FEE_REFUND` Trading fee refunded
  * `CURRENCY_BUY` Currency convert
  * `CURRENCY_SELL` Currency convert
  * `AUTO_DEDUCTION` Asset auto deducted by system (roll back)
  * `Others`



### unifiedMarginStatus

  * `1` Classic account
  * `3` Unified trading account 1.0
  * `4` Unified trading account 1.0 (pro version)
  * `5` Unified trading account 2.0
  * `6` Unified trading account 2.0 (pro version)



### convertAccountType

  * `eb_convert_uta` Unified Trading Account
  * `eb_convert_funding` Funding Account



### symbol

 _USDT Perpetual_ :

  * `BTCUSDT`
  * `ETHUSDT`



 _USDT Futures_ :

  * `BTCUSDT-21FEB25`
  * `ETHUSDT-14FEB25`  
The types of USDT Futures contracts offered by Bybit include: Weekly, Bi-Weekly, Tri-Weekly, Monthly, Bi-Monthly, Quarterly, Bi-Quarterly, Tri-Quarterly



 _USDC Perpetual_ :

  * `BTCPERP`
  * `ETHPERP`



 _USDC Futures_ :

  * `BTC-24MAR23`



 _Inverse Perpetual_ :

  * `BTCUSD`
  * `ETHUSD`



 _Inverse Futures_ :

  * `BTCUSDH23` H: First quarter; 23: 2023
  * `BTCUSDM23` M: Second quarter; 23: 2023
  * `BTCUSDU23` U: Third quarter; 23: 2023
  * `BTCUSDZ23` Z: Fourth quarter; 23: 2023



 _Spot_ :

  * `BTCUSDT`
  * `ETHUSDC`



 _Option_ :

  * `BTC-13FEB25-89000-P-USDT` USDT Option
  * `ETH-28FEB25-2800-C` USDC Option



### vipLevel

  * No VIP
  * VIP-1
  * VIP-2
  * VIP-3
  * VIP-4
  * VIP-5
  * VIP-Supreme
  * PRO-1
  * PRO-2
  * PRO-3
  * PRO-4
  * PRO-5
  * PRO-6



### adlRankIndicator

  * `0` default value of empty position
  * `1`
  * `2`
  * `3`
  * `4`
  * `5`



### smpType

  * default: `None`
  * `CancelMaker`
  * `CancelTaker`
  * `CancelBoth`



### extraFees.feeType

  * `UNKNOWN`
  * `TAX` Government tax. Only for Indonesian site
  * `CFX` Indonesian foreign exchange tax. Only for Indonesian site
  * `WHT` EU withholding tax. Only for EU site
  * `GST` Indian GST tax. Only for kyc=Indian users
  * `VAT` ARE VAT tax. Only for kyc=ARE users



### extraFees.subFeeType

  * `UNKNOWN`
  * `TAX_PNN` Tax fee, fiat currency to digital currency. Only for Indonesian site
  * `TAX_PPH` Tax fee, digital currency to fiat currency. Only for Indonesian site
  * `CFX_FIEE` CFX fee, fiat currency to digital currency. Only for Indonesian site
  * `AUT_WITHHOLDING_TAX` EU site withholding tax. Only for EU site
  * `IND_GST` Indian GST tax. Only for kyc=Indian users
  * `ARE_VAT` ARE VAT tax. Only for kyc=ARE users



### state

  * `scheduled`
  * `ongoing`
  * `completed`
  * `canceled`



### serviceTypes

  * `1` Trading service
  * `2` Trading service via http request
  * `3` Trading service via websocket
  * `4` Private websocket stream
  * `5` Market data service



### product

  * `1` Futures
  * `2` Spot
  * `3` Option
  * `4` Spread



### maintainType

  * `1` Planned maintenance
  * `2` Temporary maintenance
  * `3` Incident



### env

  * `1` Production
  * `2` Production Demo service



### bizType

  * `SPOT`
  * `DERIVATIVES`
  * `OPTIONS`



### msg

  * `API limit updated successfully`
  * `Requested limit exceeds maximum allowed per user`
  * `No permission to operate these UIDs`
  * `API cap configuration not found`
  * `API cap configuration not found for bizType`
  * `Requested limit would exceed institutional quota`



### groupId

  * `1` Major Coins
  * `2` High Growth
  * `3` Mid-Tier Liquidity
  * `4` Mid-Tier Activation
  * `5` Long Tail
  * `6` Innovation Zone
  * `7` Pre-Listing
  * `8` USDC contracts



### groupName

  * `G1(Major Coins)` Major Coins
  * `G2(High Growth)` High Growth
  * `G3(Mid-Tier Liquidity)` Mid-Tier Liquidity
  * `G4(Mid-Tier Activation)` Mid-Tier Activation
  * `G5(Long Tail)` Long Tail
  * `Innovation-Zone` Innovation Zone
  * `Pre-listing` Pre-listing
  * `USDC` USDC group



### Spot Fee Currency Instruction

with the example of BTCUSDT:

  * Is makerFeeRate positive?
    * TRUE
      * Side = Buy -> base currency (BTC)
      * Side = Sell -> quote currency (USDT)
    * FALSE
      * IsMakerOrder = TRUE
        * Side = Buy -> quote currency (USDT)
        * Side = Sell -> base currency (BTC)
      * IsMakerOrder = FALSE
        * Side = Buy -> base currency (BTC)
        * Side = Sell -> quote currency (USDT)



### sbe-orderStatus

  * `5` Rejected
  * `6` New
  * `7` Cancelled
  * `8` PartiallyFilled
  * `9` Filled
  * `0` Others



### sbe-rejectReason

  * `0` EC_NoError 
  * `1` EC_Others 
  * `2` EC_UnknownMessageType 
  * `3` EC_MissingClOrdID 
  * `4` EC_OrderNotExist 
  * `5` EC_MissingOrigClOrdID 
  * `6` EC_ClOrdIDOrigClOrdIDAreTheSame 
  * `7` EC_OrigClOrdIDDoesNotExist 
  * `8` EC_TooLateToCancel 
  * `9` EC_UnknownOrderType 
  * `10` EC_UnknownSide 
  * `11` EC_UnknownTimeInForce 
  * `12` EC_WronglyRouted 
  * `13` EC_MarketOrderPriceIsNotZero 
  * `14` EC_LimitOrderInvalidPrice 
  * `15` EC_NoEnoughQtyToFill 
  * `16` EC_NoImmediateQtyToFill 
  * `17` EC_QtyCannotBeZero 
  * `18` EC_PerCancelRequest 
  * `19` EC_MarketOrderCannotBePostOnly 
  * `20` EC_PostOnlyWillTakeLiquidity 
  * `21` EC_CancelReplaceOrder 
  * `22` EC_InvalidSymbolStatus 
  * `23` EC_MarketOrderNoSupportTIF 
  * `24` EC_ReachMaxTradeNum 
  * `25` EC_InvalidPriceScale 
  * `28` EC_BySelfMatch 
  * `29` EC_InvalidSmpType 
  * `30` EC_CancelByMMP 
  * `31` EC_InCallAuctionStatus 
  * `34` EC_InvalidUserType 
  * `35` EC_InvalidMirrorOid 
  * `36` EC_InvalidMirrorUid 
  * `100` EC_EcInvalidQty 
  * `101` EC_InvalidAmount 
  * `102` EC_LoadOrderCancel 
  * `103` EC_CancelForNoFullFill 
  * `104` EC_MarketQuoteNoSuppSell 
  * `105` EC_DisorderOrderID 
  * `106` EC_InvalidBaseValue 
  * `107` EC_LoadOrderCanMatch 
  * `108` EC_SecurityStatusFail 
  * `110` EC_ReachRiskPriceLimit 
  * `111` EC_CancelByOrderValueZero 
  * `112` EC_CancelByMatchValueZero 
  * `113` EC_CancelByMatchValueZero 
  * `200` EC_ReachMarketPriceLimit



### Advanced-Earn-category

  * `DualAssets`



### Advanced-Earn-Product-Status

  * `Available`
  * `NotAvailable`



### Advanced-Earn-Position-Status

  * `Active`
  * `Redeeming`



### Advanced-Earn-Order-Status

  * `Pending`
  * `Success`
  * `Settled`
  * `Fail`

---

# 枚舉定義

### locale

  * `de-DE`
  * `en-US`
  * `es-AR`
  * `es-ES`
  * `es-MX`
  * `fr-FR`
  * `kk-KZ`
  * `id-ID`
  * `uk-UA`
  * `ja-JP`
  * `ru-RU`
  * `th-TH`
  * `pt-BR`
  * `tr-TR`
  * `vi-VN`
  * `zh-TW`
  * `ar-SA`
  * `hi-IN`
  * `fil-PH`



### announcementType

  * `new_crypto`
  * `latest_bybit_news`
  * `delistings`
  * `latest_activities`
  * `product_updates`
  * `maintenance_updates`
  * `new_fiat_listings`
  * `other`



### announcementTag

  * `Spot`
  * `Derivatives`
  * `Spot Listings`
  * `BTC`
  * `ETH`
  * `Trading Bots`
  * `USDC`
  * `Leveraged Tokens`
  * `USDT`
  * `Margin Trading`
  * `Partnerships`
  * `Launchpad`
  * `Upgrades`
  * `ByVotes`
  * `Delistings`
  * `VIP`
  * `Futures`
  * `Institutions`
  * `Options`
  * `WEB3`
  * `Copy Trading`
  * `Earn`
  * `Bybit Savings`
  * `Dual Asset`
  * `Liquidity Mining`
  * `Shark Fin`
  * `Launchpool`
  * `NFT GrabPic`
  * `Buy Crypto`
  * `P2P Trading`
  * `Fiat Deposit`
  * `Crypto Deposit`
  * `Спот`
  * `Спот лістинги`
  * `Торгові боти`
  * `Токени з кредитним плечем`
  * `Маржинальна торгівля`
  * `Партнерство`
  * `Оновлення`
  * `Делістинги`
  * `Ф'ючерси`
  * `Опціони`
  * `Копітрейдинг`
  * `Bybit Накопичення`
  * `Бівалютні інвестиції`
  * `Майнінг ліквідності`
  * `Купівля криптовалюти`
  * `P2P торгівля`
  * `Фіатні депозити`
  * `Криптодепозити`
  * `Копитрейдинг`
  * `Торговые боты`
  * `Деривативы`
  * `P2P`
  * `Спот листинги`
  * `Деривативи`
  * `MT4`
  * `Lucky Draw`
  * `Unified Trading Account`
  * `Єдиний торговий акаунт`
  * `Единый торговый аккаунт`
  * `Институциональный трейдинг`
  * `Інституціональний трейдинг`
  * `Делистинг`



### category

  * `spot` 現貨
  * `linear` USDT永續, USDT交割, USDC永續, USDC交割
  * `inverse` 反向合約，包含反向永續, 反向交割
  * `option` 期權



### orderStatus

 _活動態_

  * `New` 訂單成功下達
  * `PartiallyFilled` 部分成交
  * `Untriggered` 條件單未觸發



 _終態_

  * `Rejected` 訂單被拒絕
  * `PartiallyFilledCanceled` 僅現貨存在該枚舉值, 訂單部分成交且已取消
  * `Filled` 完全成交
  * `Cancelled` 期貨交易，當訂單是該狀態時，是可能存在部分成交的; 經典帳戶的現貨盈止損單、條件單、OCO訂單觸發前取消
  * `Triggered` 已觸發, 條件單從未觸發到變成New的一個中間態
  * `Deactivated` 統一帳戶下期貨、現貨的盈止損單、條件單、OCO訂單觸發前取消



### timeInForce

  * `GTC` 一直有效至取消
  * `IOC` 立即成交或取消
  * `FOK` 完全成交或取消
  * [PostOnly](https://www.bybit.com/zh-TW/help-center/bybitHC_Article?language=zh_TW&id=000001051) 被動委託
  * [RPI(Retail Price Improvement)](https://www.bybit.com/en/help-center/article/Retail-Price-Improvement-RPI-Order) 特性:
    * **獨家匹配** : 僅匹配非演算法用戶；不執行來自 Open API 的訂單.
      * **Post-Only 機制** : 充當掛單，增加流動性
      * **較低優先順序** : 在相同價格水準的非 RPI 訂單之後執行
      * **有限訪問** : 最初僅針對部分幣對的選定做市商.
      * **訂單簿更新** : 從 API 中排除，但顯示在 GUI 上.



### createType

  * `CreateByUser`
  * `CreateByAdminClosing`
  * `CreateBySettle` USDC期貨交割; 因合約下架導致的平倉
  * `CreateByStopOrder` 期貨條件單
  * `CreateByTakeProfit` 期貨止盈單
  * `CreateByPartialTakeProfit` 期貨部分止盈單
  * `CreateByStopLoss` 期貨止損單
  * `CreateByPartialStopLoss` 期貨部分止損單
  * `CreateByTrailingStop` 期貨追蹤出場單
  * `CreateByTrailingProfit` 期貨追蹤止盈單
  * `CreateByLiq` 階梯強平
  * `CreateByTakeOver_PassThrough`強平觸發倉位被系統接管
  * `CreateByAdl_PassThrough` [自動減倉](https://www.bybit.com/en/help-center/article/Auto-Deleveraging-ADL)
  * `CreateByBlock_PassThrough` 從Paradigm下的大宗交易
  * `CreateByBlockTradeMovePosition_PassThrough` 移倉觸發的訂單
  * `CreateByClosing` 在持倉區進行平倉 - web/app
  * `CreateByFGridBot` 網格機器人創建訂單
  * `CloseByFGridBot` 網格機器人平倉
  * `CreateByTWAP` TWAP創建訂單
  * `CreateByTVSignal` TradingView webhook觸發訂單 - web/app
  * `CreateByMmRateClose` 通過設置mmrate觸發的訂單 - web/app
  * `CreateByMartingaleBot` 馬丁格爾訂單
  * `CloseByMartingaleBot` 馬丁格爾平倉
  * `CreateByIceBerg` 冰山策略訂
  * `CreateByArbitrage` 套利策略下單 - web/app
  * `CreateByDdh` 期權動態Delta對衝訂單 - web/app
  * `CreateByBboOrder` BBO 訂單
  * `CreateByChaseOrder` 追逐限價訂單



### execType

  * `Trade`
  * `AdlTrade` [自動減倉](https://www.bybit.com/zh-TW/help-center/bybitHC_Article?language=zh_TW&id=000001124)
  * `Funding` [資金費率](https://www.bybit.com/zh-TW/help-center/HelpCenterKnowledge/bybitHC_Article?id=000001123&language=zh_TW)
  * `BustTrade` 強平
  * `Delivery` USDT到期交割; 下架合約到期平倉
  * `Settle` 反向合約到期交割;
  * `BlockTrade`
  * `MovePosition`



### stopOrderType

  * `TakeProfit` 止盈單
  * `StopLoss` 止損單
  * `TrailingStop` 追蹤止損單
  * `Stop` 條件單
  * `PartialTakeProfit` 部分止盈單
  * `PartialStopLoss` 部分止損單
  * `tpslOrder` 現貨止盈止損單
  * `OcoOrder` 現貨OCO訂單
  * `MmRateClose` 在web或者app端, 當倉位上設置了當達到某個MMR水平時, 自動平倉
  * `BidirectionalTpslOrder` 現貨雙向止盈止損單



### tickDirection

  * `PlusTick` 價格上漲
  * `ZeroPlusTick` 交易的價格與前一筆交易的價格相同，前一筆交易的價格高於前一筆交易的價格
  * `MinusTick` 價格下跌
  * `ZeroMinusTick` 交易的價格與前一筆交易的價格相同，前一筆交易的價格低於前一筆交易的價格



### interval

  * `1` `3` `5` `15` `30` `60` `120` `240` `360` `720` 分鐘
  * `D` 天
  * `W` 週
  * `M` 月



### intervalTime

  * `5min` `15min` `30min` 分鐘
  * `1h` `4h` 小時
  * `1d` 天



### positionIdx

  * `0` 單向持倉
  * `1` 買側的雙向持倉
  * `2` 賣側的雙向持倉



### positionStatus

  * `Normal`
  * `Liq` 強平中
  * `Adl` 自動減倉中



### rejectReason

  * `EC_NoError`
  * `EC_Others`
  * `EC_UnknownMessageType`
  * `EC_MissingClOrdID`
  * `EC_MissingOrigClOrdID`
  * `EC_ClOrdIDOrigClOrdIDAreTheSame`
  * `EC_DuplicatedClOrdID`
  * `EC_OrigClOrdIDDoesNotExist`
  * `EC_TooLateToCancel`
  * `EC_UnknownOrderType`
  * `EC_UnknownSide`
  * `EC_UnknownTimeInForce`
  * `EC_WronglyRouted`
  * `EC_MarketOrderPriceIsNotZero`
  * `EC_LimitOrderInvalidPrice`
  * `EC_NoEnoughQtyToFill`
  * `EC_NoImmediateQtyToFill`
  * `EC_PerCancelRequest`
  * `EC_MarketOrderCannotBePostOnly`
  * `EC_PostOnlyWillTakeLiquidity`
  * `EC_CancelReplaceOrder`
  * `EC_InvalidSymbolStatus`
  * `EC_CancelForNoFullFill`
  * `EC_BySelfMatch`
  * `EC_InCallAuctionStatus` 用於市前訂單操作，例如集合競價第二階段不允許撤單，當交易服務沒有成功攔截撤單請求時，該請求最終會被撮合服務拒絕
  * `EC_QtyCannotBeZero`
  * `EC_MarketOrderNoSupportTIF`
  * `EC_ReachMaxTradeNum`
  * `EC_InvalidPriceScale`
  * `EC_BitIndexInvalid`
  * `EC_StopBySelfMatch`
  * `EC_InvalidSmpType`
  * `EC_CancelByMMP`
  * `EC_InvalidUserType`
  * `EC_InvalidMirrorOid`
  * `EC_InvalidMirrorUid`
  * `EC_EcInvalidQty`
  * `EC_InvalidAmount`
  * `EC_LoadOrderCancel`
  * `EC_MarketQuoteNoSuppSell`
  * `EC_DisorderOrderID`
  * `EC_InvalidBaseValue`
  * `EC_LoadOrderCanMatch`
  * `EC_SecurityStatusFail`
  * `EC_ReachRiskPriceLimit`
  * `EC_OrderNotExist`
  * `EC_CancelByOrderValueZero`
  * `EC_CancelByMatchValueZero`
  * `EC_ReachMarketPriceLimit`



### accountType

  * `UNIFIED` 統一帳戶
  * `FUND` 資金帳戶



### assetCategory

  * `Easy Earn` 理財帳戶子分類
  * `Futures Grid Bot` 交易機器人帳戶子分類
  * `Futures Combo Bot` 交易機器人帳戶子分類
  * `Futures Martingale Bot` 交易機器人帳戶子分類
  * `Copy Trading Classic` 跟單交易帳戶子分類
  * `Copy Trading TradFi` 跟單交易帳戶子分類
  * `Copy Trading Pro` 跟單交易帳戶子分類
  * `trade` Alpha 帳戶子分類 — 現貨Alpha代幣持倉
  * `farm` Alpha 帳戶子分類 — 現貨Alpha挖礦倉位



### assetAccountType

  * `FundingAccount` 資金帳戶
  * `UnifiedTradingAccount` 統一交易帳戶
  * `Earn` 理財帳戶
  * `TradingBot` 交易機器人帳戶
  * `CopyTrading` 跟單交易帳戶
  * `CryptoLoans` 加密借貸帳戶
  * `CryptoLoans_legacy` 加密借貸帳戶（舊版）
  * `PayLater` 先享後付帳戶
  * `Launchpool` Launchpool 帳戶
  * `TradFi` 傳統金融帳戶
  * `MarginStakedSOL` SOL 質押保證金帳戶
  * `Alpha` Alpha 帳戶



### transferStatus

  * `SUCCESS`
  * `PENDING`
  * `FAILED`



### depositStatus

  * `0` 未知
  * `1` 等待確認
  * `2` 處理中
  * `3` 成功 (這是一筆入金成功的終態)
  * `4` 儲值失敗
  * `10011` 等待加錢到資金池
  * `10012` 成功加錢到資金池



### withdrawStatus

  * `SecurityCheck`
  * `Pending`
  * `success`
  * `CancelByUser`
  * `Reject`
  * `Fail`
  * `BlockchainConfirmed`
  * `MoreInformationRequired`
  * `Unknown` 兜底狀態, 一般不會出現



### triggerBy

  * `LastPrice`
  * `IndexPrice`
  * `MarkPrice`



### cancelType

  * `CancelByUser`
  * `CancelByReduceOnly`
  * `CancelByPrepareLiq` `CancelAllBeforeLiq` 由於強平而取消
  * `CancelByPrepareAdl` `CancelAllBeforeAdl` 由於自動減倉而取消
  * `CancelByAdmin`
  * `CancelBySettle` 由於合約下架而取消訂單
  * `CancelByTpSlTsClear` 止盈止損訂單因倉位被平而取消
  * `CancelBySmp`
  * `CancelByDCP`
  * `CancelByRebalance` 價差交易特有
  * `CancelByOCOTpCanceledBySlTriggered` 止盈訂單因止損觸發而被取消
  * `CancelByOCOSlCanceledByTpTriggered` 止損訂單因止盈觸發而被取消



 _期權:_

  * `CancelByUser`
  * `CancelByReduceOnly`
  * `CancelAllBeforeLiq` 由於強平而取消
  * `CancelAllBeforeAdl` 由於自動減倉而取消
  * `CancelBySettle`
  * `CancelByCannotAffordOrderCost`
  * `CancelByPmTrialMmOverEquity`
  * `CancelByAccountBlocking`
  * `CancelByDelivery`
  * `CancelByMmpTriggered`
  * `CancelByCrossSelfMuch`
  * `CancelByCrossReachMaxTradeNum`
  * `CancelByDCP`
  * `CancelBySmp`



### optionPeriod

  * BTC: `7`,`14`,`21`,`30`,`60`,`90`,`180`,`270`天
  * ETH: `7`,`14`,`21`,`30`,`60`,`90`,`180`,`270`天
  * SOL: `7`,`14`,`21`,`30`,`60`,`90`天



### dataRecordingPeriod

  * `5min` `15min` `30min` 分鐘
  * `1h` `4h` 小時
  * `4d` 天



### contractType

  * `InversePerpetual` 反向永續
  * `LinearPerpetual` 正向永續: USDT永續和USDC永續
  * `LinearFutures` USDT/USDC交割
  * `InverseFutures` 反向交割



### status

  * `PreLaunch` 預上線
  * `Trading` 線上可交易
  * `Delivering` 交割中
  * `Closed` 已下架



### symbolType

  * `innovation` 合約
  * `adventure` 現貨
  * `xstocks` 現貨
  * `commodity` 合約
  * `stock` 合約 股票
  * `forex` 合約 外匯



### curAuctionPhase

  * `NotStarted` 盤前交易未開始
  * `Finished` 盤前交易已結束
    * 當盤前合約最終無法轉為正式合約, 它將會被下架且phase="Finished"
  * `CallAuction` 集合競價第一階段
    * 僅支持timeInForce=GTC, orderType=Limit的訂單
    * 不支持設置止盈止損; 不支持掛條件單
    * 該階段不支持改單
    * 訂單價格區間: [[preOpenPrice](/docs/zh-TW/v5/market/tickers) x 0.5, [maxPrice](/docs/zh-TW/v5/market/instrument)]
  * `CallAuctionNoCancel` 集合競價第二階段
    * 僅支持timeInForce=GTC, orderType=Limit的訂單
    * 不支持設置止盈止損; 不支持掛條件單
    * 該階段不支持改單和撤單
    * 訂單價格區間: 買單 [[lastPrice](/docs/zh-TW/v5/market/tickers) x 0.5, [markPrice](/docs/zh-TW/v5/market/tickers) x 1.1], 賣單 [[markPrice](/docs/zh-TW/v5/market/tickers) x 0.9, [maxPrice](/docs/zh-TW/v5/market/instrument)]
  * `CrossMatching` 集合競價第三階段 - 撮合盤前交易
    * 該階段不支持掛單, 改單和撤單
    * 該階段會產生k線數據
  * `ContinuousTrading` 連續競價階段
    * 該階段對訂單行為沒有限制
    * 該階段會產生訂單簿、最近成交數據



### marginTrading

  * `none` 不管是經典帳戶還是統一帳戶, 該交易對都不支持槓桿交易
  * `both` 對於經典帳戶和統一帳戶, 該交易對都支持槓桿交易
  * `utaOnly` 僅對於統一帳戶, 該交易對支持槓桿交易
  * `normalSpotOnly` 僅對於經典帳戶, 該交易對支持槓桿交易



### copyTrading

  * `none` 不管是經典帳戶還是統一帳戶, 該交易對都不支持帶單交易
  * `both` 對於經典帳戶和統一帳戶, 該交易對都支持帶單交易
  * `utaOnly` 僅對於統一帳戶, 該交易對支持帶單交易
  * `normalOnly` 僅對於經典帳戶, 該交易對支持帶單交易



### type(uta-translog)

  * `TRANSFER_IN` 從其他錢包轉入到統一錢包
  * `TRANSFER_OUT` 從統一錢包轉出到別的錢包
  * `TRADE`
  * `SETTLEMENT` USDT永續的資金費結算; USDC永續的資金費結算以及USDC合約的8小時倉位結算
  * `DELIVERY` USDC交割合約和期權到期交割
  * `LIQUIDATION`
  * `ADL` 自動減倉
  * `AIRDROP`
  * `BONUS` 體驗金發放
  * `BONUS_RECOLLECT` 體驗金過期
  * `FEE_REFUND` 手續費返還
  * `INTEREST` 借貸產生的利息
  * `CURRENCY_BUY` 閃兌, 以及系統對借款的清算(統一帳戶借貸)
  * `CURRENCY_SELL` 閃兌, 以及系統對借款的清算(統一帳戶借貸)
  * `BORROWED_AMOUNT_INS_LOAN` OTC放款
  * `PRINCIPLE_REPAYMENT_INS_LOAN` 主動償還本金
  * `INTEREST_REPAYMENT_INS_LOAN` 主動償還利息
  * `AUTO_SOLD_COLLATERAL_INS_LOAN` OTC強平賣出抵押品(機構借貸)
  * `AUTO_BUY_LIABILITY_INS_LOAN` OTC強平買入借款資產(機構借貸)
  * `AUTO_PRINCIPLE_REPAYMENT_INS_LOAN` 被動償還本金
  * `AUTO_INTEREST_REPAYMENT_INS_LOAN` 被動償還利息
  * `TRANSFER_IN_INS_LOAN` 機構借貸強平時自動劃入
  * `TRANSFER_OUT_INS_LOAN` 機構借貸強平時自動劃出
  * `SPOT_REPAYMENT_SELL` 一鍵還款時的賣出
  * `SPOT_REPAYMENT_BUY` 一鍵還款時的買入
  * `TOKENS_SUBSCRIPTION` 槓桿代幣申購
  * `TOKENS_REDEMPTION` 槓桿代幣贖回
  * `AUTO_DEDUCTION` 資金自動轉出 (鏈回滾)
  * `FLEXIBLE_STAKING_SUBSCRIPTION` Byfi靈活質押申購
  * `FLEXIBLE_STAKING_REDEMPTION` Byfi靈活質押贖回
  * `FIXED_STAKING_SUBSCRIPTION` Byfi固定質押申購
  * `FLEXIBLE_STAKING_REFUND` Byfi靈活質押退款
  * `FIXED_STAKING_REFUND` Byfi固定質押退款
  * `PREMARKET_TRANSFER_OUT` 盤前交易質押金上帳
  * `PREMARKET_DELIVERY_SELL_NEW_COIN` 盤前交易交割新幣
  * `PREMARKET_DELIVERY_BUY_NEW_COIN` 盤前交易新幣種劃給買家
  * `PREMARKET_DELIVERY_PLEDGE_PAY_SELLER` 交割履約-質押款交付
  * `PREMARKET_DELIVERY_PLEDGE_BACK` 交割履約-退回賣家質押幣
  * `PREMARKET_ROLLBACK_PLEDGE_BACK` 交割違約-退還買家質押款
  * `PREMARKET_ROLLBACK_PLEDGE_PENALTY_TO_BUYER` 交割違約-違約金劃給買家
  * `CUSTODY_NETWORK_FEE` fireblocks業務
  * `CUSTODY_SETTLE_FEE` fireblocks業務
  * `CUSTODY_LOCK` fireblocks / copper 業務
  * `CUSTODY_UNLOCK` fireblocks / copper 業務
  * `CUSTODY_UNLOCK_REFUND` fireblocks / copper 業務
  * `LOANS_BORROW_FUNDS` 質押借貸放款
  * `LOANS_PLEDGE_ASSET` 質押借貸還款
  * `BONUS_TRANSFER_IN` 卡券金額轉入
  * `BONUS_TRANSFER_OUT` 卡券金額轉出
  * `PEF_TRANSFER_IN` 私募基金申購
  * `PEF_TRANSFER_OUT` 私募基金贖回
  * `PEF_PROFIT_SHARE` 私募基金分潤
  * `ONCHAINEARN_SUBSCRIPTION` 鏈上賺幣申購
  * `ONCHAINEARN_REDEMPTION` 鏈上賺幣贖回
  * `ONCHAINEARN_REFUND` 鏈上賺幣退款
  * `STRUCTURE_PRODUCT_SUBSCRIPTION` 結構化產品申購
  * `STRUCTURE_PRODUCT_REFUND` 結構化產品退款
  * `CLASSIC_WEALTH_MANAGEMENT_SUBSCRIPTION` 經典財富管理申購
  * `PREMIMUM_WEALTH_MANAGEMENT_SUBSCRIPTION` 高級財富管理申購
  * `PREMIMUM_WEALTH_MANAGEMENT_REFUND` 高級財富管理退款
  * `LIQUIDITY_MINING_SUBSCRIPTION` 流動性挖礦申購
  * `LIQUIDITY_MINING_REFUND` 流動性挖礦退款
  * `PWM_SUBSCRIPTION` 私人財富管理申購
  * `PWM_REFUND` 私人財富管理退款
  * `DEFI_INVESTMENT_SUBSCRIPTION` DEFI申購
  * `DEFI_INVESTMENT_REFUND` DEFI退款
  * `DEFI_INVESTMENT_REDEMPTION` DEFI贖回
  * `INSTITUTION_LOAN_IN` 借款放款（INS借款）
  * `INSTITUTION_PAYBACK_PRINCIPAL_OUT` 還本金（INS借款）
  * `INSTITUTION_PAYBACK_INTEREST_OUT` 還利息（INS借款）
  * `INSTITUTION_EXCHANGE_SELL` 強平兌換兌換（INS借款）
  * `INSTITUTION_EXCHANGE_BUY` 強平兌換兌入（INS借款）
  * `INSTITUTION_LIQ_PRINCIPAL_OUT` 被動還款本金（INS借款）
  * `INSTITUTION_LIQ_INTEREST_OUT` 被動還利息（INS借款）
  * `INSTITUTION_LOAN_TRANSFER_IN` 機構借貸強平轉入
  * `INSTITUTION_LOAN_TRANSFER_OUT` 機構借貸強平轉出
  * `INSTITUTION_LOAN_WITHOUT_WITHDRAW` 機構借貸本金轉出
  * `INSTITUTION_LOAN_RESERVE_IN` 機構借貸借款轉入
  * `INSTITUTION_LOAN_RESERVE_OUT` 機構借貸還款
  * `SPREAD_FEE_OUT` EU Broker點差收入
  * `PLATFORM_TOKEN_MNT_LIQRECALLEDMMNT` MNT回收
  * `PLATFORM_TOKEN_MNT_LIQRETURNEDMNT` MNT返回
  * `BORROW` 手工借幣和自動借幣
  * `REPAY` 手工還幣和自動還幣
  * `CONVERT` 貨幣兌換還款
  * `INTEREST_REFUND` 固定利率利息
  * `EU_FIAT_HEDGE_TRADING_TRADER_IN` 歐盟站法貨幣對沖交易流入
  * `EU_FIAT_HEDGE_TRADING_TRADER_OUT` 歐盟站法貨幣對沖交易資金流出
  * `BYUSDT_MINT` BYUSDT 活期儲蓄代幣
  * `BYUSDT_REDEMPTION` BYUSDT 活期儲蓄贖回
  * `BYUSDT_INTEREST` BYUSDT 活期儲蓄利息
  * `EARNING_REDEMPTION_SELL` 理財作為保證金強平流水(賣)
  * `EARNING_REDEMPTION_BUY` 理財作為保證金強平流水(買)
  * `BROKER_ABACCOUNT_FEE`
  * `DBS_CASH_OUT`
  * `DBS_CASH_IN`
  * `DBS_CASH_OUT_TR`
  * `DBS_CASH_IN_TR`
  * `CUSTODY_CASH_RECOVER_TR`
  * `ALPHA_SMALL_TOKEN_REFUND`
  * `TWAP_BUDGET_AIRDROP`
  * `TWAP_BUDGET_RECALL`
  * `FLOATING_TO_FIXED_BORROW`
  * `FLOATING_TO_FIXED_REPAY`
  * `IDN_CONVERT_IN`
  * `IDN_CONVERT_OUT`



### type(contract-translog)

  * `TRANSFER_IN` 從其他錢包轉入到(反向)合約錢包
  * `TRANSFER_OUT` 從(反向)合約錢包轉出到別的錢包
  * `TRADE`
  * `SETTLEMENT` USDT永續/反向永續的資金費結算
  * `DELIVERY` 反向期貨合約的交割
  * `LIQUIDATION`
  * `ADL` 自動減倉
  * `AIRDROP`
  * `BONUS` 體驗金發放
  * `BONUS_RECOLLECT` 體驗金過期
  * `FEE_REFUND` 手續費返還
  * `CURRENCY_BUY` 閃兌
  * `CURRENCY_SELL` 閃兌
  * `AUTO_DEDUCTION` 資金自動轉出 (鏈回滾)
  * `Others`



### unifiedMarginStatus

  * `1` 經典帳戶
  * `3` [統一帳戶1.0](/docs/zh-TW/v5/acct-mode#%E7%B5%B1%E4%B8%80%E5%B8%B3%E6%88%B610)
  * `4` [統一帳戶1.0](/docs/zh-TW/v5/acct-mode#%E7%B5%B1%E4%B8%80%E5%B8%B3%E6%88%B610) (pro版本)
  * `5` [統一帳戶2.0](/docs/zh-TW/v5/acct-mode#%E7%B5%B1%E4%B8%80%E5%B8%B3%E6%88%B620)
  * `6` [統一帳戶2.0](/docs/zh-TW/v5/acct-mode#%E7%B5%B1%E4%B8%80%E5%B8%B3%E6%88%B620) (pro版本)



### ltStatus

  * `1` 槓桿代幣支持申贖
  * `2` 槓桿代幣支持申購，但無法贖回
  * `3` 槓桿代幣支持贖回，但是無法申購
  * `4` 槓桿代幣無法申贖
  * `5` 調倉中



### convertAccountType

  * `eb_convert_uta` 統一帳戶錢包
  * `eb_convert_funding` 資金錢包



### symbol

 _USDT永續_ :

  * `BTCUSDT`
  * `ETHUSDT`



_USDT交割:

  * `BTCUSDT-21FEB25`
  * `ETHUSDT-14FEB25`  
Bybit提供的USDC交割合約類型包括: 週報、雙週報、三週報、月報、雙月報、季報、雙季報、三季報。



 _USDC永續_ :

  * `BTCPERP`
  * `ETHPERP`



 _USDC交割_ :

  * `BTC-24MAR23`



 _反向永續_ :

  * `BTCUSD`
  * `ETHUSD`



 _反向交割_ :

  * `BTCUSDH23` H: 第一季度; 23: 2023
  * `BTCUSDM23` M: 第二季度; 23: 2023
  * `BTCUSDU23` U: 第三季度; 23: 2023
  * `BTCUSDZ23` Z: 第四季度; 23: 2023



 _現貨_ :

  * `BTCUSDT`
  * `ETHUSDC`



 _期權_ :

  * `BTC-13FEB25-89000-P-USDT` USDT期權
  * `ETH-28FEB25-2800-C` USDC期權



### adlRankIndicator

  * `0` 空倉時默認值
  * `1`
  * `2`
  * `3`
  * `4`
  * `5`



### vipLevel

  * No VIP
  * VIP-1
  * VIP-2
  * VIP-3
  * VIP-4
  * VIP-5
  * VIP-Supreme
  * PRO-1
  * PRO-2
  * PRO-3
  * PRO-4
  * PRO-5



### smpType

  * 默認: `None`
  * `CancelMaker`
  * `CancelTaker`
  * `CancelBoth`



### extraFees.feeType

  * `UNKNOWN`
  * `TAX` 政府稅。僅適用於印尼站
  * `CFX` 印尼外匯稅。僅適用於印尼站
  * `WHT` 歐盟預扣稅。僅適用於歐盟站
  * `GST` 印度商品及服務稅。僅適用於 kyc=印度用戶
  * `VAT` 阿聯酋增值税。僅適用於 kyc=阿聯酋用戶



### extraFees.subFeeType

  * `UNKNOWN`
  * `TAX_PNN` 稅費，法定貨幣轉數位貨幣。僅適用於印尼站
  * `TAX_PPH` 稅費，數位貨幣轉法定貨幣。僅適用於印尼站
  * `CFX_FIEE` 印尼外匯稅，法定貨幣轉換數位貨幣。僅適用於印尼站
  * `AUT_WITHHOLDING_TAX` EU 網站預扣稅。僅適用於歐盟站
  * `IND_GST` 印度商品及服務稅。僅適用於 kyc=印度用戶
  * `ARE_VAT` 阿聯酋增值税。僅適用於 kyc=阿聯酋用戶



### state

  * `scheduled`
  * `ongoing`
  * `completed`
  * `canceled`



### serviceTypes

  * `1` 交易服務
  * `2` 交易服務-http
  * `3` 交易服務-ws下單
  * `4` 私有推送
  * `5` 行情



### product

  * `1` 期貨
  * `2` 現貨
  * `3` 期權
  * `4` 價差交易



### maintainType

  * `1` 計畫維護
  * `2` 臨時維護
  * `3` 系統故障



### env

  * `1` 實盤
  * `2` 模擬交易



### bizType

  * `SPOT`
  * `DERIVATIVES`
  * `OPTIONS`



### msg

  * `API limit updated successfully` API limit更新成功
  * `Requested limit exceeds maximum allowed per user` 請求設定limit超出單一用戶最大限制
  * `No permission to operate these UIDs` 針對這些uid沒有操作權限
  * `API cap configuration not found` 未找到 API 上限配置
  * `API cap configuration not found for bizType` 未找到 bizType 的 API 上限配置
  * `Requested limit would exceed institutional quota` 設定超出機構最大限頻值



### groupId

  * `1` 主流交易對
  * `2` 高增長率交易對
  * `3` 中等流動性交易對
  * `4` 中等啟動區交易對
  * `5` 長尾資產交易對
  * `6` 創新區交易對
  * `7` 盤前交易對
  * `8` USDC合約



### groupName

  * `G1(Major Coins)` G1, 主流交易對
  * `G2(High Growth)` G2, 高增長率交易對
  * `G3(Mid-Tier Liquidity)` G3, 中等流動性交易對
  * `G4(Mid-Tier Activation)` G4, 中等啟動區交易對
  * `G5(Long Tail)` G5, 長尾資產交易對
  * `Innovation-Zone` 創新區交易對
  * `Pre-listing` 盤前交易對
  * `USDC` USDC合約組



### 現貨交易手續費幣種說明

以BTCUSDT為例:

  * maker費率是否為正?
    * TRUE
      * 方向 = Buy -> 交易幣種 (BTC)
      * 方向 = Sell -> 報價幣種 (USDT)
    * FALSE
      * 是否是maker單 = TRUE
        * 方向 = Buy -> 報價幣種 (USDT)
        * 方向 = Sell -> 交易幣種 (BTC)
      * 是否是maker單 = FALSE
        * 方向 = Buy -> 交易幣種 (BTC)
        * 方向 = Sell -> 報價幣種 (USDT)



### sbe-orderStatus

  * `5` Rejected
  * `6` New
  * `7` Cancelled
  * `8` PartiallyFilled
  * `9` Filled
  * `0` Others



### sbe-rejectReason

  * `0` EC_NoError 
  * `1` EC_Others 
  * `2` EC_UnknownMessageType 
  * `3` EC_MissingClOrdID 
  * `4` EC_OrderNotExist 
  * `5` EC_MissingOrigClOrdID 
  * `6` EC_ClOrdIDOrigClOrdIDAreTheSame 
  * `7` EC_OrigClOrdIDDoesNotExist 
  * `8` EC_TooLateToCancel 
  * `9` EC_UnknownOrderType 
  * `10` EC_UnknownSide 
  * `11` EC_UnknownTimeInForce 
  * `12` EC_WronglyRouted 
  * `13` EC_MarketOrderPriceIsNotZero 
  * `14` EC_LimitOrderInvalidPrice 
  * `15` EC_NoEnoughQtyToFill 
  * `16` EC_NoImmediateQtyToFill 
  * `17` EC_QtyCannotBeZero 
  * `18` EC_PerCancelRequest 
  * `19` EC_MarketOrderCannotBePostOnly 
  * `20` EC_PostOnlyWillTakeLiquidity 
  * `21` EC_CancelReplaceOrder 
  * `22` EC_InvalidSymbolStatus 
  * `23` EC_MarketOrderNoSupportTIF 
  * `24` EC_ReachMaxTradeNum 
  * `25` EC_InvalidPriceScale 
  * `28` EC_BySelfMatch 
  * `29` EC_InvalidSmpType 
  * `30` EC_CancelByMMP 
  * `31` EC_InCallAuctionStatus 
  * `34` EC_InvalidUserType 
  * `35` EC_InvalidMirrorOid 
  * `36` EC_InvalidMirrorUid 
  * `100` EC_EcInvalidQty 
  * `101` EC_InvalidAmount 
  * `102` EC_LoadOrderCancel 
  * `103` EC_CancelForNoFullFill 
  * `104` EC_MarketQuoteNoSuppSell 
  * `105` EC_DisorderOrderID 
  * `106` EC_InvalidBaseValue 
  * `107` EC_LoadOrderCanMatch 
  * `108` EC_SecurityStatusFail 
  * `110` EC_ReachRiskPriceLimit 
  * `111` EC_CancelByOrderValueZero 
  * `112` EC_CancelByMatchValueZero 
  * `113` EC_CancelByMatchValueZero 
  * `200` EC_ReachMarketPriceLimit



### Advanced-Earn-category

  * `DualAssets`



### Advanced-Earn-Product-Status

  * `Available`
  * `NotAvailable`



### Advanced-Earn-Position-Status

  * `Active`
  * `Redeeming`



### Advanced-Earn-Order-Status

  * `Pending`
  * `Success`
  * `Settled`
  * `Fail`