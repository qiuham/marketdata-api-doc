---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#error-code-rest-api-block-trading-and-spread-orderbook
anchor_id: error-code-rest-api-block-trading-and-spread-orderbook
api_type: REST
updated_at: 2026-07-13 19:29:49.619741
---

# Block Trading and Spread Orderbook

Error Code from 70000  
  
Error Code | HTTP Status Code | Error Message  
---|---|---  
70000 | 200 | RFQ does not exist.  
70001 | 200 | Quote does not exist.  
70002 | 200 | Block trade does not exist.  
70003 | 200 | Public block trade does not exist.  
70004 | 200 | Invalid instrument {instId}  
70005 | 200 | The number of legs in RFQ cannot exceed maximum value.  
70006 | 200 | Does not meet the minimum asset requirement.  
70007 | 200 | Underlying index {instFamily} does not exist under instType {instType}.  
70008 | 200 | Operation failed under MMP status.  
70009 | 200 | Data must have at least 1 valid element.  
70010 | 200 | Timestamp parameters need to be in Unix timestamp format in milliseconds.  
70011 | 200 | Duplicate setting for instType {instType}.  
70012 | 200 | Duplicate setting for underlying/instId {instId} under the same instType {instType}.  
70013 | 200 | endTs needs to be bigger than or equal to beginTs.  
70014 | 200 | It's not allowed to have includeAll=True for all the instType.  
70015 | 200 | In order to trade this product, you need to complete advanced verification  
70016 | 200 | Please specify your instrument settings for at least one instType.  
70060 | 200 | The {account} doesn’t exist or the position side is incorrect. “To” and “from” accounts must be under the same main account.  
70061 | 200 | To move position, please enter a position that’s opposite to your current side and is smaller than or equal to your current size.  
70062 | 200 | {account} has reached the maximum number of position transfers allowed per day.  
70064 | 200 | Position does not exist.  
70065 | 200 | Couldn’t move position. Execution price cannot be determined.  
70066 | 200 | Moving positions isn't supported in spot mode. Switch to any other account mode and try again.  
70067 | 200 | Moving positions isn't supported in margin trading.  
70100 | 200 | Duplicate instruments in legs array.  
70101 | 200 | Duplicate clRfqId  
70102 | 200 | No counterparties specified  
70103 | 200 | Invalid counterparty  
70105 | 200 | The total value of non all-SPOT RFQs should be greater than the min notional value {nonSpotMinNotional}  
70106 | 200 | The trading amount does not meet the min tradable amount requirement  
70107 | 200 | The number of counterparties cannot exceed maximum value.  
70108 | 200 | The total value of all-spot RFQs should be greater than the min notional value {spotMinNotional}  
70109 | 200 | Counterparties for selected instruments are currently unavailable.  
70200 | 200 | The RFQ with {rfqState} status cannot be canceled  
70203 | 200 | Cancellation failed as rfq count exceeds the limit {rfqLimit}.  
70207 | 200 | Cancellation failed as you do not have any active RFQs.  
70208 | 200 | Cancellation failed as service is unavailable now, please try again later.  
70301 | 200 | Duplicate clQuoteId.  
70303 | 200 | The RFQ with {rfqState} status cannot be quoted.  
70304 | 200 | Price should be an integer multiple of the tick size.  
70305 | 200 | Bid price cannot be higher than offer price  
70306 | 200 | The legs of quote do not match the legs of {rfqId}  
70307 | 200 | Size should be in integral multiples of the lot size.  
70308 | 200 | Quote to your own RFQ is not allowed.  
70309 | 200 | Quote to the same RFQ with the same side is not allowed.  
70310 | 200 | Quoted price of instId {instId} cannot exceed your preset price limit.  
70400 | 200 | The Quote with {quoteState} status cannot be canceled  
70408 | 200 | Cancellation failed as quote count exceeds the limit {quoteLimit}.  
70409 | 200 | Cancellation failed as you do not have any active Quotes.  
70501 | 200 | RFQ {rfqId} is not quoted by {quoteId}  
70502 | 200 | The legs do not match the legs of {rfqId}  
70503 | 200 | Leg sizes specified are under the minimum block size required by Jupiter.  
70504 | 200 | Execution failed as the RFQ status is {rfqState}.  
70505 | 200 | Execution failed as the Quote status is {quoteState}.  
70506 | 200 | Leg sizes specified do not have the same ratios as the whole RFQ.  
70507 | 200 | Partial execution was attempted but allowPartialExecution of the RFQ is not enabled.  
70508 | 200 | No instrument settings available.  
70509 | 200 | Execution failed: counterparty error  
70510 | 200 | For error details, refer to the acctAlloc field.  
70511 | 200 | Execution is being processed  
70514 | 200 | For each symbol, the total size of RFQ legs in all accounts should be equal to its combined amount in the group RFQ.  
70515 | 200 | For each sub-account, the ratio of a leg’s size to the main account RFQ must be the same across all symbols.  
70516 | 200 | You can only select up to {param0} sub-accounts for group RFQ.  
70517 | 200 | {param0} doesn't exist or you don’t have permission to create group RFQ for it.  
70518 | 200 | Make sure you didn’t select the same account more than once for group RFQ.  
75001 | 200 | Trade ID does not exist  
75002 | 200 | {sprdId} : unable to place new orders or modify existing orders at the moment  
75003 | 200 | Invalid price  
56000 | 200 | Block trade does not exist.  
56001 | 200 | The number of multi-legs cannot exceed {legLimit}.  
56002 | 200 | The number of multi-legs does not match with the verified one.  
56003 | 200 | Duplicate clBlockTdId.  
56004 | 200 | Trade with yourself is not allowed.  
56005 | 200 | clBlockTdId should be the same as the verified one.  
56006 | 200 | The role should be different from the verified one.  
56007 | 200 | Leg no.{legNo} does not match with the verified one.  
56008 | 200 | Duplicate instruments in legs array.

---

# 大宗交易

错误码从 70000 开始  
  
错误码 | HTTP 状态码 | 错误提示  
---|---|---  
70000 | 200 | 询价单不存在  
70001 | 200 | 报价单不存在  
70002 | 200 | 大宗交易不存在  
70003 | 200 | 公共的大宗交易不存在  
70004 | 200 | 无效的产品ID {instId}  
70005 | 200 | 组合交易的数量不能超过最大值  
70006 | 200 | 不满足最小资产要求  
70007 | 200 | 该产品类型 {instFamily} 的标的指数 {instType} 不存在  
70008 | 200 | MMP状态下操作失败。  
70009 | 200 | Data数组必须至少含有一个有效元素  
70010 | 200 | 时间戳参数必须是Unix时间戳的毫秒格式  
70011 | 200 | 产品类型 {instType} 存在重复设置  
70012 | 200 | 同一个instType{instType}下的instFamily/instId{instId} 存在重复设置  
70013 | 200 | endTs必须大于等于beginTs  
70014 | 200 | 不允许对所有产品类别设置includeAll=True.  
70015 | 200 | 您在完成高级身份认证后才能交易此类产品  
70016 | 200 | 交易产品设置中需选择至少一个交易品种  
70060 | 200 | 账号 {account} 不存在或输入有误。仓位转移的两边帐号必须属于同一个主帐号。  
70061 | 200 | 您输入的仓位数量应小于您当前的持仓量，方向应与您当前的持仓方向相反。  
70062 | 200 | 账号 {account} 已达到每日仓位转移次数的上限  
70064 | 200 | 仓位不存在  
70065 | 200 | 未能转移仓位，因为无法确定成交价格  
70066 | 200 | 现货模式不支持仓位转移，请切换到其他账户模式后重试  
70067 | 200 | 杠杆交易暂不支持仓位转移  
70100 | 200 | 组合交易中的产品ID重复  
70101 | 200 | clRfqId重复  
70102 | 200 | 未指定对手方  
70103 | 200 | 无效的对手方  
70105 | 200 | 非全现货的RFQ总价值应该大于最小名义值{nonSpotMinNotional}  
70106 | 200 | 下单数量小于最小交易数量  
70107 | 200 | 对手方的数量不能超过最大值  
70108 | 200 | 全现货的RFQ总价值应该大于最小名义值{spotMinNotional}  
70109 | 200 | 所选产品无有效对手方  
70200 | 200 | 不能取消处于{rfqState}状态的询价单  
70203 | 200 | 取消失败，由于询价单数量超过限制数量{rfqLimit}  
70207 | 200 | 取消失败，由于您没有询价挂单  
70208 | 200 | 取消失败，由于服务暂时不可用，请稍后重试  
70301 | 200 | clQuoteId重复  
70303 | 200 | 不能对处于{rfqState}状态的询价单报价  
70304 | 200 | 价格应该是下单价格精度的整数倍  
70305 | 200 | 买入价格不能高于报价  
70306 | 200 | 报价的组合交易没有匹配{rfqId}的组合交易  
70307 | 200 | 数量应该是下单数量精度的整数倍  
70308 | 200 | 不允许对自己的询价单报价  
70309 | 200 | 不允许对相同询价单进行同一方向的报价  
70310 | 200 | instId {instId} 报价不可以超过你预设的价格限制  
70400 | 200 | 不能取消处于{quoteState}状态的报价单  
70408 | 200 | 取消失败，由于报价单数量超过限制数量{quoteLimit}  
70409 | 200 | 取消失败，由于您没有报价挂单  
70501 | 200 | 询价单{rfqId}没有被{quoteId}报价  
70502 | 200 | 组合交易没有匹配{rfqId}的组合交易  
70503 | 200 | 执行腿的价值总和小于大宗交易的最小名义值  
70504 | 200 | 执行失败，因为询价单的状态是{rfqState}  
70505 | 200 | 执行失败，因为报价单的状态是{quoteState}  
70506 | 200 | 腿的数量比例与原RFQ不一致  
70507 | 200 | 部分执行尝试失败。须设置allowPartialExecution为`true`  
70508 | 200 | 没有可用的产品设置。  
70509 | 200 | 交易执行失败：对手方相关错误  
70510 | 200 | 如需了解错误详情，请查看 acctAlloc 字段  
70511 | 200 | 正在执行报价  
70514 | 200 | 每个交易品种的各类账户腿的数量之和，需与组合询价单总量一致  
70515 | 200 | 各子账户的腿数量与组合询价单的比例需在所有交易品种中保持一致  
70516 | 200 | 您最多可为组合询价单选择 {param0} 个子账户  
70517 | 200 | {param0} 不存在，或您暂无权限创建组合询价单  
70518 | 200 | 请勿为组合询价单重复选择同一账户  
75001 | 200 | 交易 ID 不存在  
75002 | 200 | {sprdId} : 目前无法下新订单或修改现有订单  
75003 | 200 | 价格无效  
56000 | 200 | 大宗交易不存在  
56001 | 200 | 多腿的数量不能超过 {legLimit}  
56002 | 200 | 执行和验证的多腿数量不匹配  
56003 | 200 | 重复的clBlockTdId  
56004 | 200 | 不允许自成交  
56005 | 200 | 执行和验证的clBlockTdId 不匹配  
56006 | 200 | 执行和验证的角色不能相同  
56007 | 200 | 执行和验证的第{legNo}条腿不匹配  
56008 | 200 | 重复的产品名称