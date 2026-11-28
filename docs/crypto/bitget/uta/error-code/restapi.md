---
exchange: bitget
source_url: https://www.bitget.com/docs/uta/error-code/restapi
api_type: Error Code
updated_at: 2026-11-28 18:59:47.302345
---

# REST API Error Code

| Error Code | Description                                                                                                                                                 |
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [429](./common-error-handling#err-429)        | Too Many Requests                                                                                                                                           |
| 25000      | System error, please try again later                                                                                                                        |
| 25001      | Operation timed out                                                                                                                                         |
| 25002      | Unsupported operation                                                                                                                                       |
| [25003](./common-error-handling#err-25003)      | Concurrent operation, please retry                                                                                                                          |
| [25004](./common-error-handling#err-25004)      | Operation too frequent, please try again later                                                                                                              |
| 25005      | User does not exist                                                                                                                                         |
| 25006      | Abnormal account status                                                                                                                                     |
| 25007      | Account in an irregular status                                                                                                                              |
| 25008      | Account is in forced liquidation status                                                                                                                     |
| 25009      | Unsupported account mode switch                                                                                                                             |
| 25010      | Unsupported position mode switch                                                                                                                            |
| 25011      | Transfer failed, account is in forced liquidation status                                                                                                    |
| 25012      | Account at risk, trading temporarily disabled                                                                                                               |
| 25013      | {0} not support API trade                                                                                                                                   |
| 25100      | Trading pair {0} does not exist                                                                                                                             |
| 25101      | Trading pair not open for trading                                                                                                                           |
| [25102](./common-error-handling#err-25102)      | Trading pair temporarily closed for maintenance                                                                                                             |
| 25104      | Contract delisted                                                                                                                                           |
| [25105](./common-error-handling#err-25105)      | This contract does not support opening positions                                                                                                            |
| 25107      | There is currently a position, please close the position                                                                                                    |
| 25108      | The contract is in the initialization state                                                                                                                 |
| [25110](./common-error-handling#err-25110)      | This coin is not supported for deposits into the unified account                                                                                            |
| 25113      | There are cancellation orders in progress.                                                                                                                  |
| 25114      | There are modification orders in progress.                                                                                                                  |
| 25116      | Exceeded the currency lending account limit                                                                                                                 |
| [25150](./common-error-handling#err-25150)      | The leverage for this contract cannot exceed {0}x. Please adjust your leverage.                                        |
| 25200      | {0} validation error                                                                                                                                        |
| 25201      | Currency does not exist                                                                                                                                     |
| 25202      | Insufficient balance                                                                                                                                        |
| 25203      | Insufficient margin                                                                                                                                         |
| 25204      | Order does not exist                                                                                                                                        |
| 25205      | {0} trading price cannot be below {1}%                                                                                                                      |
| 25206      | {0} trading price cannot exceed {1}%                                                                                                                        |
| 25207      | {0} trading quantity cannot be less than {1} units                                                                                                          |
| 25208      | {0} trading quantity cannot exceed {1} units                                                                                                                |
| 25209      | Insufficient market liquidity, please try again later                                                                                                       |
| 25210      | Large price fluctuation, placing the order entails higher risk, please reorder                                                                              |
| 25211      | Exceeds the limit of {0} maximum orders                                                                                                                     |
| [25212](./common-error-handling#err-25212)      | Duplicate clientOid                                                                                                                                         |
| 25213      | Exceeds {0} permanent net buy limit, you can currently buy up to {1} USD worth of {0}                                                                       |
| 25214      | Exceeds {0} permanent net sell limit, you can currently sell up to {1} USD worth of {0}                                                                     |
| 25215      | Exceeds {0} 24-hour net buy limit, you can currently buy up to {1} USD worth of {0}                                                                         |
| 25216      | Exceeds {0} 24-hour net sell limit, you can currently sell up to {1} USD worth of {0}                                                                       |
| 25217      | Exceeds maximum repayment limit                                                                                                                             |
| 25218      | High risk, usage may result in forced liquidation                                                                                                           |
| [25219](./common-error-handling#err-25219)      | Exceeds the maximum borrowable amount.                                                                                                                      |
| 25220      | RaiseImrTakeUp more than settleAvailable                                                                                                                    |
| 25221      | Level gradient does not exist                                                                                                                               |
| 25222      | Trade or fair mark price does not exist                                                                                                                     |
| 25223      | Exceeds Max. leverage                                                                                                                                       |
| 25224      | Take-profit or stop-loss triggered warning, please proceed with cancellation                                                                                |
| 25225      | Insufficient available quantity in position                                                                                                                 |
| 25226      | Insufficient total position quantity                                                                                                                        |
| 25227      | No position available to close                                                                                                                              |
| 25228      | Unable to update leverage for this position, insufficient margin!                                                                                           |
| [25229](./common-error-handling#err-25229)      | Total positions exceed the current limit of {0} positions                                                                                                   |
| 25230      | Order quantity exceeds the maximum open quantity                                                                                                            |
| 25231      | Close quantity cannot exceed the held position quantity                                                                                                     |
| [25232](./common-error-handling#err-25232)      | Reduce-only orders will only reduce your position; please cancel or modify existing orders before placing a new one                                         |
| 25233      | Order quantity cannot exceed the maximum for this level                                                                                                     |
| [25234](./common-error-handling#err-25234)      | Remaining quantity for regular orders is {0} {1}, and for post-only orders it is {2} {3}.                                                                   |
| 25235      | Due to risk control, the maximum open position currently allowed is {0} {1}. The risk control limit for a single user includes all primary and sub-accounts |
| 25236      | Incorrect position open type                                                                                                                                |
| 25237      | Close orders can only occur in bi-directional mode                                                                                                          |
| 25238      | {0} do not assign values at the same                                                                                                                        |
| 25239      | Closing failed, please try again later                                                                                                                      |
| 25240      | {0} does not support this operation                                                                                                                         |
| 25241      | Bulk orders cannot exceed the corresponding maximum order value.                                                                                            |
| 25242      | The maximum reducible amount is {0}{1}.                                                                                                                     |
| 25243      | You have exceeded the currency holding limit and cannot add more of this currency.                                                                          |
| 25244      | Price should be a multiple of {0}                                                                                                                           |
| 25245      | The account is not the unified account mode                                                                                                                 |
| 25559      | Not loan user                                                                                                                                               |
| 25560      | Subaccount the same with RiskUnit ID                                                                                                                        |
| 25561      | SubUid not in risk unit                                                                                                                                     |
| 25562      | The subacccount is the other's Risk Unit                                                                                                                    |
| 25563      | The UID you are unbinding has a non-zero balance and has unsettled or pending loan orders in its associated risk unit.                                      |
| 25564      | The number of sub-accounts under the risk unit has exceeded the limit.                                                                                      |
| 25565      | The sub-account UID you entered is already bound to another risk unit.                                                                                      |
| 25566      | The risk unit does not exist.                                                                                                                               |
| [25567](./common-error-handling#err-25567)      | Exceeded the maximum quantity of contract orders：{0} {1}                                                                                                    |
| [25568](./common-error-handling#err-25568)      | The order does not meet the modification requirements.                                                                                                      |
| 25569      | Exceeded the maximum limit for modifications.                                                                                                               |
| 25570      | There are pending orders for contract bidirectional closing or contract unidirectional opening/reducing positions.                                          |
| 25571      | The modification price and qty is the same as the original value. Please adjust and try again.                                                              |
| 25572      | Too many pending modification requests. Please try again later                                                                                              |
| 25573      | Skipped due to prior modification failure                                                                                                                   |
| [25574](./common-error-handling#err-25574)      | Reduce-only order protection                                                                                                                                |
| 25575      | Failed to stop the strategy because the corresponding strategy ID could not be found                                                                        |
| 25576      | Failed to stop the strategy because it is already stopping                                                                                                  |
| 25577      | Failed to stop the strategy because the corresponding strategy ID could not be found                                                                        |
| 25578      | No strategies available to stop                                                                                                                             |
| 25579      | For long position TP/SL (close long), the take-profit trigger price must be greater than the average entry price                                            |
| 25580      | For long position TP/SL (close long), the stop-loss trigger price must be less than the average entry price                                                 |
| 25581      | For short position TP/SL (close short), the take-profit trigger price must be less than the average entry price                                             |
| 25582      | For short position TP/SL (close short), the stop-loss trigger price must be greater than the average entry price                                            |
| 25583      | Take-profit price must be greater than 0                                                                                                                    |
| 25584      | Stop-loss price must be greater than 0                                                                                                                      |
| 25585      | For long position TP/SL (close long), the take-profit trigger price must be greater than the latest price                                                   |
| 25586      | For long position TP/SL (close long), the stop-loss trigger price must be less than the latest price                                                        |
| 25587      | For short position TP/SL (close short), the take-profit trigger price must be less than the latest price                                                    |
| 25588      | For short position TP/SL (close short), the stop-loss trigger price must be greater than the latest price                                                   |
| 25589      | For long position TP/SL (close long), the take-profit trigger price must be greater than the mark price                                                     |
| 25590      | For long position TP/SL (close long), the stop-loss trigger price must be less than the mark price                                                          |
| 25591      | For short position TP/SL (close short), the take-profit trigger price must be less than the mark price                                                      |
| 25592      | For short position TP/SL (close short), the stop-loss trigger price must be greater than the mark price                                                     |
| 25593      | The current trading type does not support TP/SL settings                                                                                                    |
| 25594      | Only one TP/SL can be set for all positions of the current symbol                                                                                           |
| 25595      | The total TP/SL quantity for partial positions exceeds the position amount                                                                                  |
| 25596      | Cannot modify strategy in triggered or error state                                                                                                          |
| 25597      | Strategy does not exist or has already been stopped                                                                                                         |
| 25598      | Current strategy status does not support modification                                                                                                       |
| 25599      | Maximum number of active TP/SL orders for this symbol is {0}; cannot add more                                                                               |
| 25600      | No changes made to the TP/SL order; please modify before submitting                                                                                         |
| 25601      | Position does not exist; cannot set TP/SL                                                                                                                   |
| 25602      | Take-profit trigger price must be greater than 0                                                                                                            |
| 25603      | Stop-loss trigger price must be greater than 0                                                                                                              |
| 25604      | Take-profit order price must be greater than 0                                                                                                              |
| 25605      | Stop-loss order price must be greater than 0                                                                                                                |
| 25606      | Take-profit trigger price does not meet precision requirements                                                                                              |
| 25607      | Stop-loss trigger price does not meet precision requirements                                                                                                |
| 25608      | Take-profit order price does not meet precision requirements                                                                                                |
| 25609      | Stop-loss order price does not meet precision requirements                                                                                                  |
| 25610      | Order amount does not meet precision requirements                                                                                                           |
| 25611      | Order quantity must be greater than the minimum order amount                                                                                                |
| 25612      | Only opening orders are allowed to have preset take-profit and stop-loss                                                                                    |
| 25620      | permission denied                                                                                                                                           |
| 25622      | The collateral setting for institutional loans sub-accounts must be in all-coins mode                                                                       |
| 25650      | For long positions, the stop-loss price must be lower than the current price: {0}                                                                           |
| 25651      | For short positions, the take-profit price must be lower than the current price: {0}                                                                        |
| 25652      | For long positions, the take-profit price must be greater than the current price: {0}                                                                       |
| 25653      | The order has been changed. Please try again later                                                                                                          |
| 25654      | {0} trading price cannot be greater than the bankruptcy price of {1} {2}                                                                                    |
| 25655      | {0} trading price cannot be lower than the bankruptcy price of {1} {2}                                                                                      |
| 25657      | Manual borrowing requires switching to manual repayment mode                                                                                                |
| 41124      | For a short position, the stop-loss price must be higher than the current price {0}.                                                                        |
| 40001      | ACCESS_KEY cannot be empty                                                                                                                                  |
| 40002      | SECRET_KEY cannot be empty                                                                                                                                  |
| 40003      | Signature cannot be empty                                                                                                                                   |
| [40006](./common-error-handling#err-40006)      | Invalid ACCESS_KEY                                                                                                                                          |
| [40008](./common-error-handling#err-40008)      | Request timestamp expired                                                                                                                                   |
| [40009](./common-error-handling#err-40009)      | sign signature error                                                                                                                                        |
| 40017      | Parameter verification failed {0}                                                                                                                           |
| [40034](./common-error-handling#err-40034)      | Parameter {0} does not exist                                                                                                                                |
| 40042      | The account is an ins loan sub-account and is subject to business restrictions. For more details, please contact customer service.                          |
| 40304      | clientOid or clientOrderId length cannot greater than 50                                                                                                    |
| 40500      | Order requests for the symbol are too frequent. Please try again later.
| [40725](./common-error-handling#err-40725)      | service return an error                                                                                                                                     |
| 43117      | Exceeded Max. transferable quantity                                                                                                                         |
| 95001      | The current user is undergoing forced liquidation.                                                                                                          |
| 95002      | The sub-account has contract positions and cannot be added.                                                                                                 |
| 95003      | he sub-account UID you entered does not exist.                                                                                                              |
| 95004      | The UID you unbound has a non-zero asset balance and is in a risk unit with unsettled or pending loan orders.                                               |
| 95005      | The LTV for ins loan has exceeded the limit, and opening contracts is prohibited                                                                            |
| 95006      | The LTV for ins loan has exceeded the limit, and spot buying is prohibited                                                                                  |
| 95007      | Ins loan is not support this spot trading pair.                                                                                                             |
| 95008      | Ins loan is not support futures trading.                                                                                                                    |
| 95009      | Ins loan is not support this margin trading pair.                                                                                                           |
| 95010      | Your entered subaccount UID is already bound to another risk unit.                                                                                          |
| 95011      | Parameter validation failed:{0}                                                                                                                             |
| 95012      | The leverage {1} of the sub-account contract position for {0} exceeds max leverage {2} for ins loan                                                         |
| 95013      | The leverage {1} of the sub-account contract order trading pair {0} exceeds max leverage {2} for ins loan.",                                                |
| 95014      | The sub-account has contract orders and cannot be added                                                                                                     |
| 95016      | Exceeds Ins loan max leverage                                                                                                                               |
| 95017      | Leverage exceeds the maximum allowed. Please decrease the leverage and try again                                                                            |
| 25626      | This account mode cannot be added to the risk unit.                                                                                                         |
| 25628      | This is the demo sub-account and cannot be added to the risk unit.                                                                                          |
| 25117      | This account does not support placing RPI orders for this symbol.                                                                                           |
| 25118      | The RPI order’s price exceeds the allowed price limit range for RPI orders.                                                                                 |
| 25119      | The symbol not support placing RPI orders                                                                                                                   |
| 60050      | Order not exist                                                                                                                                             |
| 60051      | The current merchant level is not supported.                                                                                                                |
| 60052      | This P2P ad price differs by less than {3}% from your existing ad price ({0} {1}/{2}). Please adjust the price and repost.                                  |
| 60053      | param error / Order status is not unpaid / Payment timed out / Requests are too frequent. Please try again later.                                           |
| 60054      | Only the buyer can confirm the payment.                                                                                                                     |
| 60055      | The order status is not pending release.                                                                                                                    |
| 60056      | Does not meet the fiat currency limit ({0}–{1}).                                                                                                            |
| 60057      | Does not meet the crypto currency limit ({0}–{1}).                                                                                                          |
| 60058      | The number of posted ads bound to payment methods not under your name exceeds the allowable limit.                                                          |
| 60059      | The number of ads posted has reached the limit.                                                                                                             |
| 60060      | Insufficient fiat margin for the merchant.                                                                                                                  |
| 60061      | User behavior restricted: OTC ad posting is limited. Withdrawal from the funding account is restricted (applicable only to sell ads).                       |
| 60062      | Dear merchant, due to risk control reasons, you are temporarily not allowed to post ads.                                                                    |
| 60063      | P2P merchant penalty triggered.                                                                                                                             |
| 60065      | Risk control triggered when posting ads.                                                                                                                    |
| 60066      | payTimeLimit error                                                                                                                                          |
| 60067      | The remarklength for the copy cannot exceed 800 characters.                                                                                                 |
| 60068      | The remark for the trading terms must not exceed 800 characters.                                                                                            |
| 60069      | Incorrect price input.                                                                                                                                      |
| 60070      | The query period cannot exceed 30 days.                                                                                                                     |
| 60071      | The maximum fiat amount cannot exceed {0}.                                                                                                                  |
| 60072      | Ad display failed. The available trading amount must be greater than the minimum limit set for the advertisement.                                           |

---

# REST API 错误码

| 错误码   | 描述                                                  | 
|:------|:----------------------------------------------------|
| [429](./common-error-handling#err-429)   | 请求次数过                                               |
| 40001 | ACCESS_KEY不能为空                                      |
| 40002 | SECRET_KEY不能为空                                      |
| 40003 | 签名不能为空                                              |
| [40006](./common-error-handling#err-40006) | 无效的ACCESS_KEY                                       |
| [40008](./common-error-handling#err-40008) | 请求时间戳过期                                             |
| [40009](./common-error-handling#err-40009) | sign签名错误                                            |
| 40017 | 参数校验失败 {0}                                          |
| [40034](./common-error-handling#err-40034) | 参数 {0} 不存在                                          |
| [40725](./common-error-handling#err-40725) | 返回无映射信息                                             |
| 25000 | 系统异常,请稍后重试                                          |
| 25001 | 操作超时                                                |
| 25002 | 不支持的操作                                              |
| [25003](./common-error-handling#err-25003) | 并发操作,请重试                                            |
| [25004](./common-error-handling#err-25004) | 操作过于频繁，请稍后再试                                        |
| 25005 | 用户不存在                                               |
| 25006 | 账号状态异常                                              |
| 25007 | 账户非正常状态                                             |
| 25008 | 账号处于强平状态                                            |
| 25009 | 不支持的切换账户模式                                          |
| 25010 | 不支持的切换持仓模式                                          |
| 25011 | 划转失败，账号处于强平状态                                       |
| 25012 | 账户有风险,暂时不能交易                                        |
| 25013 | {0}已停盘暂不支持该操作                                       |
| 25100 | 交易对不存在                                              |
| 25101 | 交易对未开放交易                                            |
| [25102](./common-error-handling#err-25102) | 交易对停止交易维护                                           |
| 25103 | 交易对即将开放                                             |
| 25104 | 该合约已下架                                              |
| [25105](./common-error-handling#err-25105) | 此合约暂不支持开仓操作                                         |
| 25106 | 因为结算或维护原因， 交易暂停                                     |
| 25107 | 当前存在仓位,请平掉仓位                                        |
| 25108 | 该合约处于初始化状态                                          |
| 25113 | 存在在途的取消订单                                           |
| 25114 | 存在在途的改单                                             |
| 25116 | 超出币种个人借贷限额                                          |
| 25200 | 参数校验异常{0}                                           |
| 25201 | 币种不存在                                               |
| 25202 | 余额不足                                                |
| 25203 | 保证金不足                                               |
| 25204 | 订单不存在                                               |
| 25205 | {0}交易价格不能低于{1}%                                     |
| 25206 | {0}交易价格不能高于{1}%                                     |
| 25207 | {0}交易数量不能低于{1}数量                                    |
| 25208 | {0}交易数量不能高于{1}数量                                    |
| 25209 | 盘口流动性不足，请稍后操作                                       |
| 25210 | 成交价波动过大，继续挂单风险较大，请重新下单                              |
| 25211 | 超过{0}最大委托单数量限制                                      |
| [25212](./common-error-handling#err-25212) | 重复的clientOid                                        |
| 25213 | 超出永久净买入限制，当前可买入价值{1}USD                             |
| 25214 | 超出永久净卖出限制，当前可卖出价值{1}USD                             |
| 25215 | 超出24小时净买入限制，当前可买入价值{1}USD                           |
| 25216 | 超出24小时净卖出限制，当前可卖出价值{1}USD                           |
| 25217 | 超过最大的还款限额                                           |
| 25218 | 当前风险较高，使用时可能有强平风险                                   |
| [25219](./common-error-handling#err-25219) | 超出最大可借金额                                            |
| 25220 | imr占用增加超过可用资产                                       |
| 25221 | 档位梯度不存在                                             |
| 25222 | 成交或合理标记价格不存在                                        |
| 25223 | 超过最大可设置杠杆倍数                                         |
| 25224 | 止盈止损触发警告，需要撤单操作且正在撤单，请继续尝试                          |
| 25225 | 仓位的可用数量不足                                           |
| 25226 | 仓位总量不足                                              |
| 25227 | 暂无仓位可平                                              |
| 25228 | 无法更新此仓位的杠杆系数，没有足够的保证金！                              |
| [25229](./common-error-handling#err-25229) | 总持仓超过了当前持仓条数限制{0}                                   |
| 25230 | 委托数量大于最大可开数量                                        |
| 25231 | 平仓数量不能超过持有仓位数量                                      |
| [25232](./common-error-handling#err-25232) | 只减仓只会减少您的仓位, 请先撤销或者修改原有挂单再进行下单                      |
| 25233 | 委托数量不能超过对应档位的最大量                                    |
| [25234](./common-error-handling#err-25234) | 您的普通下单的剩余数量为 {0} {1}，post only下单的数量为 {2} {3}。       |
| 25235 | 因风控限制，您当前最大可开仓 {0} {1}。单个用户风控比例限额是将所有主账户与子账户一起计算在内的 |
| 25236 | 开仓类型不正确                                             |
| 25237 | 平仓只能发生在双向持仓下                                        |
| 25238 | {0}请不要同时赋值                                          |
| 25239 | 平仓失败，请稍后重试                                          |
| 25240 | {0}不支持此操作                                           |
| 25241 | 批量下单不能超过对应的最大下单值                                    |
| 25242 | 最大可减少金额为{0}{1}                                      |
| 25243 | 超过币种持有上限，无法再增加更多币种数量                                |
| 25244 | price应该满足 {0} 的倍数                                   |
| 25245 | 账号不是统一账户模式                                          |
| 25559 | 不是机构借贷用户                                            |
| 25560 | 您输入的子账户UID 和辅账户UID相同                                |
| 25561 | 您输入的子账户UID不存在风险单元内                                  |
| 25562 | 您输入的子账户UID 是其他风险单元的辅账户                              |
| 25563 | 您解绑的UID 资产大于零且所在风险单元有未结算或在途借贷订单                     |
| 25564 | 风险单元子账户数量超过上限                                       |
| 25565 | 您输入的子账户UID 已绑定到其他风险单元                               |
| 25566 | 专属子账户风险单元不存在                                        |
| [25567](./common-error-handling#err-25567) | 超过最大下单合约数量:{0} {1}                                  |
| [25568](./common-error-handling#err-25568) | 订单不符合改单要求                                           |
| 25569 | 超过最大改单数量限制                                          |
| 25570 | 合约双向平仓、合约单向开仓/减仓 存在在途订单                             |
| 25571 | 改单价格和数量和原始值相同，请调整后重试                                |
| 25572 | 存在过多未完成的改单请求，请稍后重试                                  |
| 25573 | 因前序改单失败，本改单未执行                                      |
| [25574](./common-error-handling#err-25574) | 为保障现有只减仓订单，改单失败                                     |
| 25575 | 因无法找到对应策略id，停止策略失败                                  |
| 25576 | 因对应策略状态停止中，停止策略失败                                   |
| 25577 | 因无法找到对应策略id，停止策略失败                                  |
| 25578 | 无可停的策略，停止策略失败                                       |
| 25579 | 多头止盈止损(平多方向)，止盈触发价格需要大于开仓均价                         |
| 25580 | 多头止盈止损(平多方向)，止损触发价格需要小于开仓均价                         |
| 25581 | 空头止盈止损(平空方向)，止盈触发价格需要小于开仓均价                         |
| 25582 | 空头止盈止损(平空方向)，止损触发价格需要大于开仓均价                         |
| 25583 | 止盈价格请大于0                                            |
| 25584 | 止损价格请大于0                                            |
| 25585 | 多头止盈止损(平多方向)，止盈触发价格需要大于最新价格                         |
| 25586 | 多头止盈止损(平多方向)，止损触发价格需要小于最新价格                         |
| 25587 | 空头止盈止损(平空方向)，止盈触发价格需要小于最新价格                         |
| 25588 | 空头止盈止损(平空方向)，止损触发价格需要大于最新价格                         |
| 25589 | 多头止盈止损(平多方向)，止盈触发价格需要大于标记价格                         |
| 25590 | 多头止盈止损(平多方向)，止损触发价格需要小于标记价格                         |
| 25591 | 空头止盈止损(平空方向)，止盈触发价格需要小于标记价格                         |
| 25592 | 空头止盈止损(平空方向)，止损触发价格需要大于标记价格                         |
| 25593 | 当前交易种类无法设置止盈止损                                      |
| 25594 | 当前币对的全部仓位止盈止损最多只能有一个                                |
| 25595 | 当前币对的部分仓位止盈止损数量总和不能超过仓位数量                           |
| 25596 | 当前订单状态是已触发或报错中，无法修改策略                               |
| 25597 | 策略不存在或者已经停止                                         |
| 25598 | 策略当前状态不支持修改                                         |
| 25599 | 当前币对运行中的最大止盈止损订单数为{0}，不能继续添加止盈止损                    |
| 25600 | 未修改止盈止损订单，请修改后提交                                    |
| 25601 | 仓位不存在，无法设置止盈止损                                      |
| 25602 | 止盈触发价格需要大于0                                         |
| 25603 | 止损触发价格需要大于0                                         |
| 25604 | 止盈执行价格需要大于0                                         |
| 25605 | 止损执行价格需要大于0                                         |
| 25606 | 止盈触发价格不满足精度要求                                       |
| 25607 | 止损触发价格不满足精度要求                                       |
| 25608 | 止盈执行价格不满足精度要求                                       |
| 25609 | 止损执行价格不满足精度要求                                       |
| 25610 | 下单精度不满足精度要求                                         |
| 25611 | 下单数量需要大于最小下单量                                       |
| 25612 | 只有开仓单才允许预设止盈止损                                      |
| 25650 | 多头仓位止损价格请小于当前价格: {0}                                |
| 25651 | 空头仓位止盈价格请小于当前价格: {0}                                |
| 25652 | 多头仓位止盈价格请大于当前价格：{0}                                 |
| 25653 | 存在改单，请稍后重试                                          |
| 25654 | {0}交易价格不能高于爆仓价格{1}                                  |
| 25655 | {0}交易价格不能低于爆仓价格{1}                                  |
| 25657 | 手动借币需要切换至手动还币模式                                       |
| 41124 | 空头仓位止损价格请大于当前价格{0}                                                                |
| 25620 | 没有访问权限                                              |
| [25110](./common-error-handling#err-25110) | 该币种不支持转入统一账户                                        |
| 25622 | 机构借贷子账户抵押品设置必须为全部币种模式                               |
| 40042 | 账户为机构子账户，业务受限，详情请联系客服                               |
| 40304 | clientOid 或 clientOrderId 的长度不能大于 50 个字符                 |
| 40500 | 当前交易对下单请求过于集中，请稍后重试
| 43117 | 超过最大可转出数量                                           |
| 95001 | 当前用户强平中                                             |
| 95002 | 子账户有合约持仓，不支持添加                                      |
| 95003 | 您输入的子账户UID不存在                                       |
| 95004 | 您解绑的UID 资产大于零且所在风险单元有未结算或在途借贷订单                     |
| 95005 | 机构借贷风控审核不通过，LTV 超过限制合约开仓线                           |
| 95006 | 机构借贷风控审核不通过，LTV 超过限制现货买入线                           |
| 95007 | 机构借贷不支持该现货币对                                        |
| 95008 | 机构借贷不支持合约交易                                         |
| 95009 | 机构借贷不支持杠杆交易                                         |
| 95010 | 您输入的子账户UID 已绑定到其他风险单元                               |
| 95011 | 参数校验失败:{0}                                          |
| 95014 | 子账户有合约挂单，不支持添加                                      |
| 95012 | 子账户合约持仓交易对 {0} 杠杆 {1} 超过机构借贷最大开仓杠杆 {2}              |
| 95013 | 子账户合约挂单交易对 {0} 杠杆 {1} 超过机构借贷最大开仓杠杆 {2}              |
| 95016 | 超过机构借贷最大可设置杠杆倍数                                     |
| 95017 | 超过最大杠杆倍数,请调小杠杆再交易                                   |
| 25626 | 当前账户模式不支持添加至风险单元,请调小杠杆再交易                           |
| 25628 | 模拟子账户，不支持添加至风险单元                                    |
| 25117 | 该账号不支持委托该币对的RPI订单                                   |
| 25118 | RPI订单委托价超出RPI订单限价范围                                 |
| 25119 | 该币对不支持委托RPI订单                                       |
| 60050 | 订单不存在                                                |
| 60051 | 当前商家等级不支持                                            |
| 60052 | 此 P2P 广告的价格与您现有广告的价格（{0} {1}/{2}）相差不到 {3}%。请调整价格并重新发布  |
| 60053 | 参数错误 / 订单状态不是未付款 / 付款超时 / 请求频繁,稍后重试                  |
| 60054 | 只有买家可以确认付款                                           |
| 60055 | 订单状态不是待放币                                            |
| 60056 | 不满足法币限额{0}-{1}                                       |
| 60057 | 不满足数字币限额{0}-{1}                                      |
| 60058 | 发布的广告绑定非本人收款方式的数量大于可绑定数量                             |
| 60059 | 发布广告的数量达到阈值                                          |
| 60060 | 商家法币保证金不足                                            |
| 60061 | 用户行为限制：OTC发布广告。用户行为限制：限制资金账户出金(仅针对发布出售广告)            |
| 60062 | 尊敬的商家，由于风险原因，您暂时不可以发布广告                              |
| 60063 | 触发P2P商家惩罚                                            |
| 60065 | 发布广告触发风控                                             |
| 60066 | 付款时长参数不存在                                            |
| 60067 | 文案备注长度不能大于800                                        |
| 60068 | 交易条款备注长度不能大于 800                                     |
| 60069 | 价格输入错误                                               |
| 60070 | 查询区间不能超过30天                                          |
| 60071 | 法币最大值不能超过{0}                                         |
| 60072 | 广告显示失败，可交易金额需大于广告的最小限额                               |