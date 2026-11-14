---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/enum
api_type: REST
updated_at: 2026-11-13 19:22:29.341727
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
  * `ForwardSplitSettle` Forward stock split settlement and closure of the entire existing position, followed by opening a new position
  * `ForwardSplitOpen` Forward stock split position opening after the existing position is settled and closed
  * `ReverseSplitSettle` Reverse stock split settlement and closure of the entire existing position, followed by opening a new position
  * `ReverseSplitOpen` Reverse stock split position opening after the existing position is settled and closed
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
  * `Predication` Predication account sub-category



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
  * `3` success (this is final status reflected by the finalized deposit status. If a blockchain rollback occurs, the deposit will be assigned a 7XXXX status, which represents the finalized outcome of that rollback case.)
  * `4` deposit failed
  * `7` **Rollback processing** : A blockchain rollback occurred after the deposit had already been credited.
  * `70011` **Deposit rolled back** : A blockchain rollback occurred, and the deposit has been reversed. The credited funds have been deducted, and no final credit remains.
  * `70012` **Deposit remains successful after rollback review** : Although a blockchain rollback occurred, the deposit remains valid. After review, it was determined that no clawback or deduction is required.
  * `70013` **Deposit rollback faill** : The deposit was initially credited, but the backend system failed to process the blockchain rollback automatically. The case is pending manual review.
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



#### extra status for Bybit Turkey

  * `HighValueReviewPending`
  * `HighValueReviewEDDSubmission`
  * `HighValueReviewRejected`
  * `HighValueReviewRejectedRfunding`
  * `HighValueReviewRejectedRefunded`



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

  * `PreLaunch` linear: pre-market contract
  * `PendingOpen` Futures only: a contract that is not yet open for trading
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
  * `ETF` linear ETF
  * `mstocks` spot



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
  * `DELIVERY` USDC Futures, Option delivery, Event Contract settlement
  * `LIQUIDATION`
  * `ADL` Auto-Deleveraging
  * `AIRDROP`
  * `BONUS` Bonus claimed
  * `BONUS_RECOLLECT` Bonus expired
  * `BONUS_TRANSFER_IN`
  * `BONUS_TRANSFER_OUT`
  * `FEE_REFUND` Trading fee refunded
  * `INTEREST` Interest occurred due to borrowing
  * `CURRENCY_BUY` Currency convert, and the liquidation for borrowing asset(UTA loan)
  * `CURRENCY_SELL` Currency convert, and the liquidation for borrowing asset(UTA loan)
  * `SPOT_REPAYMENT_SELL` One-click repayment currency sell
  * `SPOT_REPAYMENT_BUY` One-click repayment currency buy
  * `FORWARD_SPLIT_SETTLE` Forward stock split fractional share settlement
  * `FORWARD_SPLIT_OPEN` Forward stock split position opening
  * `REVERSE_SPLIT_SETTLE` Reverse stock split fractional share settlement
  * `REVERSE_SPLIT_OPEN` Reverse stock split position opening
  * `BORROW` Manual loan borrow and auto loan borrow
  * `REPAY` Manual loan repay and auto loan repay
  * `CONVERT` Currency convert repayment
  * `EARNING_REDEMPTION_SELL` force sell when liquidation
  * `EARNING_REDEMPTION_BUY` force buy when liquidation
  * `FLOATING_TO_FIXED_BORROW`
  * `FLOATING_TO_FIXED_REPAY`
  * `CUSTODY_NETWORK_FEE` fireblocks business
  * `CUSTODY_SETTLE_FEE` fireblocks business
  * `CUSTODY_LOCK` fireblocks / copper business
  * `CUSTODY_UNLOCK` fireblocks business
  * `CUSTODY_UNLOCK_REFUND` fireblocks business
  * `LOANS_BORROW_FUNDS` crypto loan
  * `LOANS_PLEDGE_ASSET` crypto loan repayment
  * `FIXED_SAVING_PRINCIPAL_REDEMPTION` Bycustody fixed saving redemption



#### Earn Related

  * `FLEXIBLE_STAKING_SUBSCRIPTION` Byfi flexible stake subscription
  * `FLEXIBLE_STAKING_REDEMPTION` Byfi flexible stake redemption
  * `FIXED_STAKING_SUBSCRIPTION` Byfi fixed stake subscription
  * `FLEXIBLE_STAKING_REFUND` Byfi flexiable stake refund
  * `FIXED_STAKING_REFUND` Byfi fixed stake refund
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
  * `BYUSDT_MINT` BYUSDT mint
  * `BYUSDT_REDEMPTION` BYUSDT redemption
  * `BYUSDT_INTEREST` BYUSDT interest



#### Institution Loan Related

  * `PRINCIPAL_REPAYMENT_INS_LOAN` Repay the principal of the institution loan
  * `INSTITUTION_LOAN_TRANSFER_OUT` Repay with currency convert (liquidation)
  * `INSTITUTION_LOAN_WITHOUT_WITHDRAW` Repay without currency convert (liquidation)



#### RWA Direct Stocks

  * `STOCK_TRADE_BUY`
  * `STOCK_TRADE_REFUND`
  * `STOCK_TRADE_SELL`
  * `STOCK_CORPORATE_ACTION_DIVIDEND`
  * `STOCK_ADR_FEE`



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



### predictionSide (Prediction Market — Trade Direction)

  * `1` YES / BUY — buy outcome token shares
  * `2` NO / SELL — sell outcome token shares



### predictionOrderType (Prediction Market — Order Type)

  * `1` FOK (Fill-or-Kill) — must be fully filled or entirely cancelled. Phase 1 only



### predictionOrderStatus (Prediction Market — Order Status)

  * `1` PENDING
  * `2` FILLED
  * `3` PARTIALLY_FILLED
  * `4` CANCELLED
  * `5` REJECTED



### predictionPositionResult (Prediction Market — Position Result)

  * `1` WIN — event resolved in favour of this token
  * `2` LOSE — event resolved against this token
  * `3` MANUAL_CLOSE — position closed by user before resolution



### predictionMatchStatus (Prediction Market — Match Status)

  * `1` Live — match is in progress
  * `2` Upcoming — match has not yet started
  * `3` Ended — match has concluded



### predictionMarketType (Prediction Market — Market Type)

  * `1` YES/NO binary market — two outcome tokens (YES and NO)
  * `2` Multi-outcome market — more than two outcome tokens



### predictionSortBy (Prediction Market — Sort Field)

  * `volume` Sort by 24-hour trading volume descending
  * `liquidity` Sort by available liquidity descending
  * `endDate` Sort by resolution date ascending



### predictionPriceInterval (Prediction Market — Price Interval)

  * `1H` 1 hour
  * `6H` 6 hours
  * `1D` 1 day
  * `1W` 1 week
  * `1M` 1 month
  * `ALL` Full history



### predictionStageCode (Prediction Market — Stage Code)

  * `Groups` Group stage
  * `R32` Round of 32
  * `R16` Round of 16
  * `QF` Quarter-Finals
  * `SF` Semi-Finals
  * `Final` Final



### predictionEventType (Prediction Market — Event Type)

  * `1` FIFA_2026 — 2026 FIFA World Cup



### predictionTimelineStatus (Prediction Market — Timeline Status)

  * `1` Done — stage has completed
  * `2` Active — stage is currently in progress
  * `3` Upcoming — stage has not yet started



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
  * `5` Altcoin
  * `6` Innovation Zone
  * `7` Pre-Listing
  * `9` TradeFi Perps



### groupName

  * `G1(Major Coins)` Major Coins
  * `Altcoin` Altcoin
  * `G9(Stock & Commodity Tradfi Perp)` TradeFi Perps
  * `Innovation-Zone` Innovation Zone
  * `Pre-listing` Pre-listing



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



### stocks

### stocks-side

  * `BUY` Buy
  * `SELL` Sell



### stocks-type

  * `MARKET` Market order. Uses `notional` (USDC amount) when `BUY`; uses `qty` (shares) when `SELL`
  * `LIMIT` Limit order. Requires `qty` and `limitPrice`
  * `STOP` Stop order. Requires `qty` and `stopPrice`. Executes as market after the trigger
  * `STOP_LIMIT` Stop-limit order. Requires `qty`, `stopPrice` and `limitPrice`. Places a limit order after the trigger



### stocks-timeInForce

  * `DAY` Day order. Auto-cancelled at the main US market close
  * `GTC` Good Till Cancelled
  * `IOC` Immediate or Cancel. Any unfilled portion is cancelled immediately



**Note:** `SELL` only supports `DAY` and `GTC`. `IOC` is supported but constrained to `LIMIT` \+ whole-share + `RTH`.

### stocks-tradingSession

  * `RTH` Regular Trading Hours (default)
  * `24H` 24-hour session, including pre-market, post-market and overnight. Non-`RTH` sessions accept `LIMIT` orders only



### stocks-orderStatus

  * `PENDING` Order accepted and queued for execution. Returned as the initial status by Place Order
  * `queued` Queued — order submitted, waiting for market open to execute
  * `active` Active — order is live and waiting for fill conditions
  * `filled` Filled — order fully filled
  * `partial_filled` Cancelled after partial fill — order was cancelled/failed with some prior fills
  * `cancelled` Cancelled — order was cancelled/failed with no fills



### stocks-convertType

  * `MINT` Underlying → mStocks Token
  * `REDEEM` mStocks Token → Underlying



### stocks-convertStatus

  * `PENDING` Processing
  * `SUCCESS` Completed
  * `FAILED` Failed



### stocks-accountType

  * `all` Auto-select account (default)
  * `uta` Route into the Unified Trading Account (UTA)
  * `fund` Route into the Funding Account



### stocks-flow

  * `CEX` Centralized exchange flow. Both Mint and Burn are processed through the Bybit main site
  * `DEX` Decentralized flow. Mint to the specified contract address; Burn flow depends on `burnScene`



### stocks-burnScene

  * `DEP` Burn through the Bybit main site (Deposit)
  * `NDP` Burn without going through the main site (Non-Deposit)



### stocks-symbolType

  * `US_STOCK` US stock. Currently the only supported instrument type



### stocks-statusCode

  * `1` Pre-market (04:00–09:30 ET, XNYS/XNAS only)
  * `2` Regular hours (09:30–16:00 ET, XNYS/XNAS)
  * `3` Post-market (16:00–20:00 ET, XNYS/XNAS only)
  * `4` Overnight session (20:00 ET–next day 04:00 ET, OCEA)
  * `5` Closed (weekends, holidays, off-hours)



### stocks-tradingHolidayType

  * `HOLIDAY` Statutory holiday. Market closed all day
  * `EARLY_CLOSE` Early close. `endTime` is the actual close time of that day



### tm-onchain-appealType

  * `TM_Onchain` On-chain transaction monitoring appeal
  * `TM_Onchain_KYB` On-chain transaction monitoring KYB appeal



### tm-onchain-resultStatus

  * `PENDING` Materials pending submission (non-terminal)
  * `COMMITTED` Submitted, under review (non-terminal)
  * `REJECTED` Materials rejected, need to resubmit (non-terminal)
  * `PASS` Approved (terminal)
  * `REFUSE` Rejected (terminal)
  * `DISUSED` Appeal disused (terminal)



### tm-onchain-triggerType

  * `Auto-approve`
  * `Auto-create-Initial`
  * `Manual`



### tm-onchain-direction

  * `deposit`
  * `withdraw`



### tm-onchain-fundStatus

  * Empty string No fund action
  * `Deposit Intercepted`
  * `Refund`
  * `Guilty`
  * `Recharge`



### tm-onchain-styleBox

  * `UPLOAD` Upload image (jpg/png) or PDF. Submit via `itemsData[].resources[]`
  * `MIXUPLOAD` Upload media (image / audio / video / PDF). Submit via `itemsData[].resources[]`
  * `INPUT` Multi-line text. Submit via `itemsData[].content`
  * `SINGLEINPUT` Single-line text. Submit via `itemsData[].content`
  * `SELECT` Single-select dropdown. Submit via `itemsData[].content` (option value)
  * `RADIO` Radio button group. Submit via `itemsData[].content` (option value)
  * `CHECKBOX` Multi-select. Submit via `itemsData[].mulContent[]` (list of option values)
  * `COUNTRYNAME` Country dropdown. Submit via `itemsData[].content` (English full name, e.g. `Australia`)
  * `DATEPICKER` Date picker. Submit via `itemsData[].content` (date string)
  * `COMMENT` Display-only, no submission



### tm-onchain-banDescription

Values that may appear in `accountRestriction.ban` / `unban`, mapped from the backend `ban_tag_value`:

ban_tag_value| description  
---|---  
`login`| `Account Ban`  
`all_withdraw`| `Withdraw Ban`  
`non-principal`| `Withdraw Ban (Allow to Withdraw Deposited)`  
`all_trade`| `Trading Ban (All)`  
`lighten_up`| `Trading Ban (Allow to Close Position)`  
`transfer_service_user`| `Transfer Ban (User)`  
`bybitcard_service`| `Bybit Card Ban (All)`  
`fiat_service`| `Fiat Ban (All)`  
`card_service_buy`| `Fiat Bank Card Ban (Buy)`  
`fiat_exchange`| `Fiat Deposit and Withdrawal Ban`  
`fiat_exchange_recharge`| `Fiat Deposit Ban`  
`fiat_exchange_extract`| `Fiat Withdrawal Ban`  
`p2p_service`| `P2P Ban (All)`  
  
### tm-onchain-fileType

  * `fiat-image` Image (jpg / png)
  * `fiat-pdf` PDF
  * `fiat-video` Video (mp4, etc.)



### awardType

  * `0` UNKNOWN
  * `1` CASH_CARD (trial funds card)
  * `2` SERVICE_CASH_CARD (trading-fee deduction card)
  * `3` TRADING_FEE_DISCOUNT_CARD
  * `4` TASK
  * `5` BYFI_INTEREST
  * `6` SPOT_AIR_DROP
  * `7` VIP_EXPERIENCE_CARD
  * `8` VOTES_CARD
  * `9` TRADING_VOUCHER
  * `10` REWARD
  * `11` NFT_AIR_DROP
  * `12` LOSS_COVER_VOUCHER
  * `13` POSITION_AIR_DROP
  * `14` APR_BOOSTER
  * `15` NFT_FREE_MINT_CARD
  * `16` COUPON_CODE
  * `17` CREDIT
  * `18` CARD_SKIN
  * `19` CASH_VOUCHER
  * `95` BENEFIT_PKG
  * `96` EMPTY_PACK
  * `97` POINTS
  * `98` TRIGGER
  * `99` OTHERS
  * `100` REWARD_PACKET



### friendStatus

  * `0` Unknown
  * `1` Signed up
  * `2` Has first deposit
  * `3` Has first trade
  * `4` Qualified
  * `5` Not qualified
  * `6` Historical invitation
  * `7` Boost in progress
  * `8` Boost qualified
  * `9` Boost failed
  * `10` Boost user signed up

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
  * `ForwardSplitSettle` 拆股時結算並平掉整個現有倉位，隨後開設新倉位
  * `ForwardSplitOpen` 拆股後開設新倉位
  * `ReverseSplitSettle` 合股時結算並平掉整個現有倉位，隨後開設新倉位
  * `ReverseSplitOpen` 合股後開設新倉位



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
  * `Predication` Predication 帳戶子分類



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
  * `3` 成功 (這是一筆入金成功的終態；如果有回滚，则7XXXX这种是终态)
  * `4` 儲值失敗
  * `7` **區塊鏈回滾處理中** ：入金完成入帳後發生區塊鏈回滾，目前正在處理中。
  * `70011` **入金已回滾** ：發生區塊鏈回滾，該筆入金已被撤銷。先前已入帳的資金已扣回，最終不會完成入帳。
  * `70012` **回滾審核後入金仍然有效** ：雖然發生了區塊鏈回滾，但該筆入金仍被認定為有效。經審核後，確認無需追回或扣除已入帳資金。
  * `70013` **回滾处理失败** ：該筆入金已初步完成入帳，但後端系統未能自動處理區塊鏈回滾，等待人工審核。
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



#### Bybit Turkey額外提幣狀態

  * `HighValueReviewPending`
  * `HighValueReviewEDDSubmission`
  * `HighValueReviewRejected`
  * `HighValueReviewRejectedRfunding`
  * `HighValueReviewRejectedRefunded`



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

  * `PreLaunch` 期貨：盤前合約；期权：預上線
  * `PendingOpen` 期貨：預上線（該狀態僅支持期貨），在變為`Trading`狀態前是無法交易的
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
  * `ETF` 合約 ETF
  * `mstocks` 現貨



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
  * `DELIVERY` USDC交割合約和期權到期交割、事件合約結算
  * `LIQUIDATION`
  * `ADL` 自動減倉
  * `AIRDROP`
  * `BONUS` 體驗金發放
  * `BONUS_RECOLLECT` 體驗金過期
  * `BONUS_TRANSFER_IN` 卡券金額轉入
  * `BONUS_TRANSFER_OUT` 卡券金額轉出
  * `FEE_REFUND` 手續費返還
  * `INTEREST` 借貸產生的利息
  * `CURRENCY_BUY` 閃兌, 以及系統對借款的清算(統一帳戶借貸)
  * `CURRENCY_SELL` 閃兌, 以及系統對借款的清算(統一帳戶借貸)
  * `SPOT_REPAYMENT_SELL` 一鍵還款時的賣出
  * `SPOT_REPAYMENT_BUY` 一鍵還款時的買入
  * `FORWARD_SPLIT_SETTLE` 拆股尾差結算
  * `FORWARD_SPLIT_OPEN` 拆股後開設倉位
  * `REVERSE_SPLIT_SETTLE` 合股尾差結算
  * `REVERSE_SPLIT_OPEN` 合股後開設倉位
  * `BORROW` 手工借幣和自動借幣
  * `REPAY` 手工還幣和自動還幣
  * `CONVERT` 貨幣兌換還款
  * `EARNING_REDEMPTION_SELL` 理財作為保證金強平流水(賣)
  * `EARNING_REDEMPTION_BUY` 理財作為保證金強平流水(買)
  * `FLOATING_TO_FIXED_BORROW`
  * `FLOATING_TO_FIXED_REPAY`
  * `CUSTODY_NETWORK_FEE` fireblocks業務
  * `CUSTODY_SETTLE_FEE` fireblocks業務
  * `CUSTODY_LOCK` fireblocks / copper 業務
  * `CUSTODY_UNLOCK` fireblocks / copper 業務
  * `CUSTODY_UNLOCK_REFUND` fireblocks / copper 業務
  * `LOANS_BORROW_FUNDS` 質押借貸放款
  * `LOANS_PLEDGE_ASSET` 質押借貸還款
  * `FIXED_SAVING_PRINCIPAL_REDEMPTION` Bycustody固定存款贖回



#### 理財相關

  * `FLEXIBLE_STAKING_SUBSCRIPTION` Byfi靈活質押申購
  * `FLEXIBLE_STAKING_REDEMPTION` Byfi靈活質押贖回
  * `FIXED_STAKING_SUBSCRIPTION` Byfi固定質押申購
  * `FLEXIBLE_STAKING_REFUND` Byfi靈活質押退款
  * `FIXED_STAKING_REFUND` Byfi固定質押退款
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
  * `BYUSDT_MINT` BYUSDT 活期儲蓄代幣
  * `BYUSDT_REDEMPTION` BYUSDT 活期儲蓄贖回
  * `BYUSDT_INTEREST` BYUSDT 活期儲蓄利息



#### 機構借貸相關

  * `PRINCIPAL_REPAYMENT_INS_LOAN` 機構借貸還款
  * `INSTITUTION_LOAN_TRANSFER_OUT` 機構借貸有損還款（強平）
  * `INSTITUTION_LOAN_WITHOUT_WITHDRAW` 機構借貸無損還款（強平）



#### RWA股票交易

  * `STOCK_TRADE_BUY`
  * `STOCK_TRADE_REFUND`
  * `STOCK_TRADE_SELL`
  * `STOCK_CORPORATE_ACTION_DIVIDEND`
  * `STOCK_ADR_FEE`



### unifiedMarginStatus

  * `1` 經典帳戶
  * `3` [統一帳戶1.0](/docs/zh-TW/v5/acct-mode#%E7%B5%B1%E4%B8%80%E5%B8%B3%E6%88%B610)
  * `4` [統一帳戶1.0](/docs/zh-TW/v5/acct-mode#%E7%B5%B1%E4%B8%80%E5%B8%B3%E6%88%B610) (pro版本)
  * `5` [統一帳戶2.0](/docs/zh-TW/v5/acct-mode#%E7%B5%B1%E4%B8%80%E5%B8%B3%E6%88%B620)
  * `6` [統一帳戶2.0](/docs/zh-TW/v5/acct-mode#%E7%B5%B1%E4%B8%80%E5%B8%B3%E6%88%B620) (pro版本)



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



### predictionSide (Prediction Market — Trade Direction)

  * `1` YES / BUY — buy outcome token shares
  * `2` NO / SELL — sell outcome token shares



### predictionOrderType (Prediction Market — Order Type)

  * `1` FOK (Fill-or-Kill) — must be fully filled or entirely cancelled. Phase 1 only



### predictionOrderStatus (Prediction Market — Order Status)

  * `1` PENDING
  * `2` FILLED
  * `3` PARTIALLY_FILLED
  * `4` CANCELLED
  * `5` REJECTED



### predictionPositionResult (Prediction Market — Position Result)

  * `1` WIN — event resolved in favour of this token
  * `2` LOSE — event resolved against this token
  * `3` MANUAL_CLOSE — position closed by user before resolution



### predictionMatchStatus (Prediction Market — Match Status)

  * `1` Live — match is in progress
  * `2` Upcoming — match has not yet started
  * `3` Ended — match has concluded



### predictionMarketType (Prediction Market — Market Type)

  * `1` YES/NO binary market — two outcome tokens (YES and NO)
  * `2` Multi-outcome market — more than two outcome tokens



### predictionSortBy (Prediction Market — Sort Field)

  * `volume` Sort by 24-hour trading volume descending
  * `liquidity` Sort by available liquidity descending
  * `endDate` Sort by resolution date ascending



### predictionPriceInterval (Prediction Market — Price Interval)

  * `1H` 1 hour
  * `6H` 6 hours
  * `1D` 1 day
  * `1W` 1 week
  * `1M` 1 month
  * `ALL` Full history



### predictionStageCode (Prediction Market — Stage Code)

  * `Groups` Group stage
  * `R32` Round of 32
  * `R16` Round of 16
  * `QF` Quarter-Finals
  * `SF` Semi-Finals
  * `Final` Final



### predictionEventType (Prediction Market — Event Type)

  * `1` FIFA_2026 — 2026 FIFA World Cup



### predictionTimelineStatus (Prediction Market — Timeline Status)

  * `1` Done — stage has completed
  * `2` Active — stage is currently in progress
  * `3` Upcoming — stage has not yet started



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
  * `5` 非主流幣
  * `6` 創新區交易對
  * `7` 盤前交易對
  * `9` 傳統金融合約



### groupName

  * `G1(Major Coins)` G1, 主流交易對
  * `Altcoin` 非主流幣
  * `G9(Stock & Commodity Tradfi Perp)` G9, 傳統金融合約
  * `Innovation-Zone` 創新區交易對
  * `Pre-listing` 盤前交易對



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



### stocks

### stocks-side

  * `BUY` 買入
  * `SELL` 賣出



### stocks-type

  * `MARKET` 市價單。`BUY` 時以 `notional`（USDC 金額）計；`SELL` 時以 `qty`（股數）計
  * `LIMIT` 限價單。需填 `qty` 和 `limitPrice`
  * `STOP` 止損單。需填 `qty` 和 `stopPrice`；觸發後以市價成交
  * `STOP_LIMIT` 止損限價單。需填 `qty`、`stopPrice` 和 `limitPrice`；觸發後以限價委託



### stocks-timeInForce

  * `DAY` 當日有效，北美主市場收盤時自動撤單
  * `GTC` 撤銷前持續有效（Good Till Cancelled）
  * `IOC` 立即成交，未成交部分立即取消



**注意：** `SELL` 方向僅支持 `DAY` 和 `GTC`。`IOC` 支持但有約束（`LIMIT` \+ 整股 + `RTH`）。

### stocks-tradingSession

  * `RTH` Regular Trading Hours，正常交易時段（默認值）
  * `24H` 全天候交易時段，包含盤前 / 盤後 / 夜盤。非 `RTH` 時段只允許 `LIMIT` 單



### stocks-orderStatus

  * `PENDING` 訂單已接收，排隊等待執行。下單接口返回的初始狀態
  * `queued` 排隊中——訂單已提交，等待市場開盤後執行
  * `active` 掛單中——訂單已生效，正在等待成交條件觸發
  * `filled` 已成交——訂單全部成交完成
  * `partial_filled` 部分成交後撤單——訂單被取消 / 失敗，但撤單前已有部分成交
  * `cancelled` 已撤銷——訂單被取消 / 失敗，且無任何成交



### stocks-convertType

  * `MINT` 正股 → mStocks Token
  * `REDEEM` mStocks Token → 正股



### stocks-convertStatus

  * `PENDING` 處理中
  * `SUCCESS` 處理完成
  * `FAILED` 處理失敗



### stocks-accountType

  * `all` 自動選擇賬戶（默認值）
  * `uta` 指定劃入統一交易賬戶（UTA）
  * `fund` 指定劃入資金賬戶



### stocks-flow

  * `CEX` 中心化交易所鏈路，Mint / Burn 均通過 Bybit 主站處理
  * `DEX` 去中心化鏈路，Mint 到指定合約地址；Burn 流程見 `burnScene`



### stocks-burnScene

  * `DEP` Bybit 主站（Deposit）Burn
  * `NDP` 不經主站（Non-Deposit）Burn



### stocks-symbolType

  * `US_STOCK` 美股。當前業務僅支持這一種



### stocks-statusCode

  * `1` 盤前（04:00–09:30 ET，僅 XNYS/XNAS）
  * `2` 盤中（09:30–16:00 ET，XNYS/XNAS）
  * `3` 盤後（16:00–20:00 ET，僅 XNYS/XNAS）
  * `4` 夜盤（20:00 ET–次日 04:00 ET，OCEA）
  * `5` 休市（週末 / 假日 / 時段外）



### stocks-tradingHolidayType

  * `HOLIDAY` 法定假日，全天休市
  * `EARLY_CLOSE` 提前收盤，`endTime` 為當日實際收盤時間



### tm-onchain-appealType

  * `TM_Onchain` 鏈上交易監控工單
  * `TM_Onchain_KYB` 鏈上交易監控 KYB 工單



### tm-onchain-resultStatus

  * `PENDING` 待提交材料（非終態）
  * `COMMITTED` 已提交，審核中（非終態）
  * `REJECTED` 材料駁回，需重新提交（非終態）
  * `PASS` 審核通過（終態）
  * `REFUSE` 審核拒絕（終態）
  * `DISUSED` 工單廢棄（終態）



### tm-onchain-triggerType

  * `Auto-approve` 自動通過
  * `Auto-create-Initial` 自動創建（初始）
  * `Manual` 人工創建



### tm-onchain-direction

  * `deposit` 充幣
  * `withdraw` 提幣



### tm-onchain-fundStatus

  * 空字符串 無資金處置
  * `Deposit Intercepted` 充幣被攔截
  * `Refund` 退還資金
  * `Guilty` 沒收
  * `Recharge` 重新上帳



### tm-onchain-styleBox

  * `UPLOAD` 上傳圖片（jpg/png）或 PDF。
  * `MIXUPLOAD` 上傳媒體文件（圖片 / 音頻 / 視頻 / PDF）。
  * `INPUT` 多行文本。
  * `SINGLEINPUT` 單行文本。
  * `SELECT` 單選下拉。
  * `RADIO` 單選按鈕組。
  * `CHECKBOX` 多選框。
  * `COUNTRYNAME` 國家下拉列表。
  * `DATEPICKER` 日期選擇器。
  * `COMMENT` 純展示提示



### tm-onchain-banDescription

`accountRestriction.ban` / `unban` 中的值為以下描述之一 ：

ban_tag_value| description  
---|---  
`login`| `Account Ban`  
`all_withdraw`| `Withdraw Ban`  
`non-principal`| `Withdraw Ban (Allow to Withdraw Deposited)`  
`all_trade`| `Trading Ban (All)`  
`lighten_up`| `Trading Ban (Allow to Close Position)`  
`transfer_service_user`| `Transfer Ban (User)`  
`bybitcard_service`| `Bybit Card Ban (All)`  
`fiat_service`| `Fiat Ban (All)`  
`card_service_buy`| `Fiat Bank Card Ban (Buy)`  
`fiat_exchange`| `Fiat Deposit and Withdrawal Ban`  
`fiat_exchange_recharge`| `Fiat Deposit Ban`  
`fiat_exchange_extract`| `Fiat Withdrawal Ban`  
`p2p_service`| `P2P Ban (All)`  
  
### tm-onchain-fileType

  * `fiat-image` 圖片（jpg / png）
  * `fiat-pdf` PDF
  * `fiat-video` 視頻（mp4 等）



### awardType

  * `0` UNKNOWN
  * `1` CASH_CARD（試用金卡）
  * `2` SERVICE_CASH_CARD（交易手續費抵扣卡）
  * `3` TRADING_FEE_DISCOUNT_CARD
  * `4` TASK
  * `5` BYFI_INTEREST
  * `6` SPOT_AIR_DROP
  * `7` VIP_EXPERIENCE_CARD
  * `8` VOTES_CARD
  * `9` TRADING_VOUCHER
  * `10` REWARD
  * `11` NFT_AIR_DROP
  * `12` LOSS_COVER_VOUCHER
  * `13` POSITION_AIR_DROP
  * `14` APR_BOOSTER
  * `15` NFT_FREE_MINT_CARD
  * `16` COUPON_CODE
  * `17` CREDIT
  * `18` CARD_SKIN
  * `19` CASH_VOUCHER
  * `95` BENEFIT_PKG
  * `96` EMPTY_PACK
  * `97` POINTS
  * `98` TRIGGER
  * `99` OTHERS
  * `100` REWARD_PACKET



### friendStatus

  * `0` 未知
  * `1` 已註冊
  * `2` 已首次入金
  * `3` 已首次交易
  * `4` 符合資格
  * `5` 不符合資格
  * `6` 歷史邀請
  * `7` Boost 進行中
  * `8` Boost 符合資格
  * `9` Boost 失敗
  * `10` Boost 使用者已註冊