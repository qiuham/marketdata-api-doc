---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#error-code-rest-api-account
anchor_id: error-code-rest-api-account
api_type: REST
updated_at: 2026-07-22 19:21:30.149458
---

# Account

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

---

# 账户类

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