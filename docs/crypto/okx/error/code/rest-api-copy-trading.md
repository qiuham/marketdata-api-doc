---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#error-code-rest-api-copy-trading
anchor_id: error-code-rest-api-copy-trading
api_type: REST
updated_at: 2026-07-15 19:21:00.732896
---

# Copy trading

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

---

# 跟单交易

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