---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#error-code-rest-api-funding
anchor_id: error-code-rest-api-funding
api_type: REST
updated_at: 2026-07-12 19:17:53.643606
---

# Funding

Error Code from 58000 to 58999  
  
Error Code | HTTP Status Code | Error Message  
---|---|---  
58002 | 200 | Please activate Savings Account first.  
58003 | 200 | Savings does not support this currency type  
58004 | 200 | Account blocked.  
58005 | 200 | The {behavior} amount must be equal to or less than {minNum}  
58006 | 200 | Service unavailable for token {0}.  
58007 | 200 | Assets interface is currently unavailable. Try again later  
58008 | 200 | You do not have assets in this currency.  
58009 | 200 | Crypto pair doesn't exist  
58010 | 200 | Chain {chain} isn't supported  
58011 | 200 | Due to local laws and regulations, our services are unavailable to unverified users in {region}. Please verify your account.  
58012 | 200 | Due to local laws and regulations, OKX does not support asset transfers to unverified users in {region}. Please make sure your recipient has a verified account.  
58013 | 200 | Withdrawals not supported yet, contact customer support for details  
58014 | 200 | Deposits not supported yet, contact customer support for details  
58015 | 200 | Transfers not supported yet, contact customer support for details  
58016 | 200 | The API can only be accessed and used by the trading team's main account  
58100 | 200 | The trading product triggers risk control, and the platform has suspended   
the fund transfer-out function with related users. Please wait patiently.  
58101 | 200 | Transfer suspended  
58102 | 429 | Rate limit reached. Please refer to API docs and throttle requests accordingly.  
58103 | 200 | This account transfer function is temporarily unavailable. Please contact customer service for details.  
58104 | 200 | Since your P2P transaction is abnormal, you are restricted from making  
fund transfers. Please contact customer support to remove the restriction.  
58105 | 200 | Since your P2P transaction is abnormal, you are restricted from making  
fund transfers. Please transfer funds on our website or app to complete  
identity verification.  
58106 | 200 | USD verification failed.  
58107 | 200 | Crypto verification failed.  
58110 | 200 | Transfers are suspended due to market risk control triggered by your {businessType} {instFamily} trades or positions. Please try again in a few minutes. Contact customer support if further assistance is needed.  
58111 | 200 | Fund transfers are unavailable while perpetual contracts are charging funding fees. Try again later.  
58112 | 200 | Transfer failed. Contact customer support for assistance  
58113 | 200 | Unable to transfer this crypto  
58114 | 400 | Transfer amount must be greater than 0  
58115 | 200 | Sub-account does not exist.  
58116 | 200 | Transfer exceeds the available amount.  
58117 | 200 | Transfer failed. Resolve any negative assets before transferring again  
58119 | 200 | {0} Sub-account has no permission to transfer out, please set first.  
58120 | 200 | Transfers are currently unavailable. Try again later  
58121 | 200 | This transfer will result in a high-risk level of your position, which may lead to forced liquidation. You need to re-adjust the transfer amount to make sure the position is at a safe level before proceeding with the transfer.  
58122 | 200 | A portion of your spot is being used for Delta offset between positions. If the transfer amount exceeds the available amount, it may affect current spot-derivatives risk offset structure, which will result in an increased Maintenance Margin Requirement (MMR) rate. Please be aware of your risk level.  
58123 | 200 | The From parameter cannot be the same as the To parameter.  
58124 | 200 | Your transfer is being processed, transfer id:{trId}. Please check the latest state of your transfer from the endpoint (GET /api/v5/asset/transfer-state)  
58125 | 200 | Non-tradable assets can only be transferred from sub-accounts to main accounts  
58126 | 200 | Non-tradable assets can only be transferred between funding accounts  
58127 | 200 | Main account API key does not support current transfer 'type' parameter. Please refer to the API documentation.  
58128 | 200 | Sub-account API key does not support current transfer 'type' parameter. Please refer to the API documentation.  
58129 | 200 | {param} is incorrect or {param} does not match with 'type'  
58131 | 200 | For compliance, we're unable to provide services to unverified users. Verify your identity to make a transfer.  
58132 | 200 | For compliance, we're unable to provide services to users with Basic verification (Level 1). Complete Advanced verification (Level 2) to make a transfer.  
58200 | 200 | Withdrawal from {0} to {1} is currently not supported for this currency.  
58201 | 200 | Withdrawal amount exceeds daily withdrawal limit.  
58202 | 200 | The minimum withdrawal amount for NEO is 1, and the amount must be an integer.  
58203 | 200 | Please add a withdrawal address.  
58204 | 200 | Withdrawal suspended due to your account activity triggering risk control. Please contact customer support for assistance.  
58205 | 200 | Withdrawal amount exceeds the upper limit.  
58206 | 200 | Withdrawal amount is less than the lower limit.  
58207 | 200 | Withdrawal address isn't on the verified address list. (The format for withdrawal addresses with a label is “address:label”.)  
58208 | 200 | Withdrawal failed. Please link your email.  
58209 | 200 | Sub-accounts don't support withdrawals or deposits. Please use your main account instead  
58210 | 200 | You can't proceed with withdrawal as we're unable to verify your identity. Please withdraw via our app or website instead.  
58212 | 200 | Withdrawal fee must be {0}% of the withdrawal amount  
58213 | 200 | The internal transfer address is illegal. It must be an email, phone number, or account name  
58214 | 200 | Withdrawals suspended due to {chainName} maintenance  
58215 | 200 | Withdrawal ID does not exist.  
58216 | 200 | Operation not allowed.  
58217 | 200 | Withdrawals are temporarily suspended for your account due to a risk detected in your withdrawal address. Contact customer support for assistance  
58218 | 200 | The internal withdrawal failed. Please check the parameters toAddr and areaCode.  
58219 | 200 | You cannot withdraw crypto within 24 hours after changing your mobile number, email address, or Google Authenticator.  
58220 | 200 | Withdrawal request already canceled.  
58221 | 200 | The toAddr parameter format is incorrect, withdrawal address needs labels. The format should be "address:label".  
58222 | 200 | Invalid withdrawal address  
58223 | 200 | This is a contract address with higher withdrawal fees  
58224 | 200 | This crypto currently doesn't support on-chain withdrawals to OKX addresses. Withdraw through internal transfers instead  
58225 | 200 | Asset transfers to unverified users in {region} are not supported due to local laws and regulations.  
58226 | 200 | {chainName} is delisted and not available for crypto withdrawal.  
58227 | 200 | Withdrawal of non-tradable assets can be withdrawn all at once only  
58228 | 200 | Withdrawal of non-tradable assets requires that the API key must be bound to an IP  
58229 | 200 | Insufficient funding account balance to pay fees {fee} USDT  
58230 | 200 | According to the OKX compliance policy, you will need to complete your identity verification (Level 1) in order to withdraw  
58231 | 200 | The recipient has not completed personal info verification (Level 1) and cannot receive your transfer  
58232 | 200 | You’ve reached the personal information verification (L1) withdrawal limit, complete photo verification (L2) to increase the withdrawal limit  
58233 | 200 | For compliance, we're unable to provide services to unverified users. Verify your identity to withdraw.  
58234 | 200 | For compliance, the recipient can't receive your transfer yet. They'll need to verify their identity to receive your transfer.  
58235 | 200 | For compliance, we're unable to provide services to users with Basic verification (Level 1). Complete Advanced verification (Level 2) to withdraw.  
58236 | 200 | For compliance, a recipient with Basic verification (Level 1) is unable to receive your transfer. They'll need to complete Advanced verification (Level 2) to receive it.  
58237 | 200 | According to local laws and regulations, please provide accurate recipient information (rcvrInfo). For the exchange address, please also provide exchange information and recipient identity information ({consientParameters}).  
58238 | 200 | Incomplete info. The info of the exchange and the recipient are required if you're withdrawing to an exchange platform.  
58239 | 200 | You can't withdraw to a private wallet via API. Please withdraw via our app or website instead.  
58240 | 200 | For security and compliance purposes, please complete the identity verification process to use our services. If you prefer not to verify, contact customer support for next steps. We're committed to ensuring a safe platform for users and appreciate your understanding.  
58241 | 200 | Due to local compliance requirements, internal withdrawal is unavailable  
58242 | 200 | The recipient can't receive your transfer due to their local compliance requirements  
58243 | 200 | Your recipient can't receive your transfer as they haven't made a cash deposit yet  
58244 | 200 | Make a cash deposit to proceed  
58248 | 200 | Due to local regulations, API withdrawal isn't allowed. Withdraw using OKX app or web.  
58249 | 200 | API withdrawal for this currency is currently unavailable. Try withdrawing via our app or website.  
58252 | 200 | Withdrawal is restricted for 48h after your first TRY transaction for asset security.  
58254 | 200 | Due to local compliance requirements, please complete the digital signature or satoshi test via our app or website first before withdrawing to a private wallet via API.  
58256 | 200 | You can withdraw stablecoins valued at up to {dailyLimit} {symbol} every 24 hours. You can still withdraw {quotaRemaining} {symbol}.  
58257 | 200 | You can withdraw stablecoins valued at up to {monthlyLimit} {symbol} every month. You can still withdraw {quotaRemaining} {symbol}.  
58258 | 200 | You can withdraw crypto valued at up to {dailyLimit} {symbol} every 24 hours. You can still withdraw {quotaRemaining} {symbol}.  
58300 | 200 | Deposit-address count exceeds the limit.  
58301 | 200 | Deposit-address not exist.  
58302 | 200 | Deposit-address needs tag.  
58303 | 200 | Deposit for chain {chain} is currently unavailable  
58304 | 200 | Failed to create invoice.  
58305 | 200 | Unable to retrieve deposit address, please complete identity verification and generate deposit address first.  
58306 | 200 | According to the OKX compliance policy, you will need to complete your identity verification (Level 1) in order to deposit  
58307 | 200 | You've reached the personal information verification (L1) deposit limit, the excess amount has been frozen, complete photo verification (L2) to increase the deposit limit  
58308 | 200 | For compliance, we're unable to provide services to unverified users. Verify your identity to deposit.  
58309 | 200 | For compliance, we're unable to provide services to users with Basic verification (Level 1). Complete Advanced verification (Level 2) to deposit.  
58310 | 200 | Unable to create new deposit address, try again later  
58350 | 200 | Insufficient balance.  
58351 | 200 | Invoice expired.  
58352 | 200 | Invalid invoice.  
58353 | 200 | Deposit amount must be within limits.  
58354 | 200 | You have reached the daily limit of 10,000 invoices.  
58355 | 200 | Permission denied. Please contact your account manager.  
58356 | 200 | The accounts of the same node do not support the Lightning network deposit or withdrawal.  
58358 | 200 | The fromCcy parameter cannot be the same as the toCcy parameter.  
58373 | 200 | The minimum {ccy} conversion amount is {amount}  
58381 | 200 | This feature is not currently supported.  
58382 | 200 | Unable to process unlock request. Please retry via the user interface.  
58383 | 200 | Deposit record not found. Unable to process unlock request.  
58384 | 200 | Per local regulations, please provide accurate sender information. For exchange addresses, please also provide the exchange information and sender identity details.  
58400 | 200 | Request Failed  
58401 | 200 | Payment method is not supported  
58402 | 200 | Invalid payment account  
58403 | 200 | Transaction cannot be canceled  
58404 | 200 | ClientId already exists  
58405 | 200 | Withdrawal suspended  
58406 | 200 | Channel is not supported  
58407 | 200 | API withdrawal isn't allowed for this payment method. Withdraw using OKX app or web

---

# 资金类

错误码从 58000 到 58999  
  
错误码 | HTTP 状态码 | 错误提示  
---|---|---  
58002 | 200 | 请先开通余币宝服务  
58003 | 200 | 余币宝不支持该币种  
58004 | 200 | 账户冻结  
58005 | 200 | 申购/赎回额度不可超过{0}  
58006 | 200 | 币种{0}不支持当前操作  
58007 | 200 | 资金接口服务异常，请稍后再试。  
58008 | 200 | 您没有该币种资产  
58009 | 200 | 币对不存在  
58010 | 200 | 该链{0}暂不支持  
58011 | 200 | 抱歉，由于当地法律法规，欧易无法为{region}未认证用户提供服务，请先认证身份以继续使用欧易  
58012 | 200 | 抱歉，由于当地法律法规，欧易无法为{region}未认证用户提供服务，所以您无法向该用户转账  
58013 | 200 | 暂不支持提币功能，请咨询客服了解详情  
58014 | 200 | 暂不支持充值功能，请咨询客服了解详情  
58015 | 200 | 暂不支持划转功能，请咨询客服了解详情  
58016 | 200 | 仅交易团队主账户有权限调用此接口  
58100 | 200 | 行权或结算中，暂无法转入或转出  
58101 | 200 | 划转冻结  
58102 | 429 | 已达到速率限制。请参考相应的 API 文档与节流请求  
58103 | 200 | 该账户划转功能暂不可用，详情请联系客服  
58104 | 200 | 您在法币区的交易异常，现已被限制划转功能，请您联系在线客服以解除限制  
58105 | 200 | 您在法币区的交易异常，现已被限制划转功能，请您在网页或APP进行法币划  
转操作以完成身份验证  
58106 | 200 | 美元可转校验未通过  
58107 | 200 | 币种可转校验未通过  
58110 | 200 | 您所交易过或者持仓的 {businessType} {instFamily} 产品触发市场风控，平台已暂停您的资金转出功能，请稍后重试。如需进一步的协助，请联系客服。  
58111 | 200 | 永续合约正在收取资金费，暂时无法做资金划转，请稍后重试  
58112 | 200 | 资金划转失败，请联系客服进行处理  
58113 | 200 | 该币种不支持划转  
58114 | 400 | 转账金额必须大于 0  
58115 | 200 | 子账户不存在  
58116 | 200 | 转出数量大于最大可转数量  
58117 | 200 | 账户划转失败，请先处理负资产后再划转  
58119 | 200 | {0} 子账户没有转出权限，请先设置  
58120 | 200 | 划转服务暂不可用，请稍后重试  
58121 | 200 | 此次划转将导致您的仓位风险水平较高，进而可能引起爆仓。您需要重新调整划转金额，确保仓位处于安全水平后，再进行划转操作。  
58122 | 200 | 您的一部分现货正用于仓位间的 Delta 对冲，若划转数量超过可用金额，可能会影响现有的现货对冲结构，进而导致维持保证金率增加，请留意您的风险水平。  
58123 | 200 | 参数from与参数to不可相同  
58124 | 200 | 资金划转中，划转id：{trId}，请通过接口(GET /api/v5/asset/transfer-state)获取最新状态  
58125 | 200 | 不可交易资产仅支持子账户转主账户  
58126 | 200 | 不可交易资产划转，只能在资金账户间互转  
58127 | 200 | 主账户 API key 不支持当前 type 划转类型参数，请参考 API 文档描述  
58128 | 200 | 子账户 API key 不支持当前 type 划转类型参数，请参考 API 文档描述  
58129 | 200 | {param}错误或{param}与type不匹配  
58131 | 200 | 根据当地法律法规，欧易无法为未认证用户提供服务，请先完成身份认证再继续划转  
58132 | 200 | 根据当地法律法规，我们无法为仅完成基本认证的用户提供服务，请先完成高级认证再继续划转  
58200 | 200 | 该币种暂不支持从{0}提现至{1}，敬请谅解  
58201 | 200 | 今日提现金额累计超过每日限额  
58202 | 200 | NEO最小提现数量为1，且提现数量必须为整数  
58203 | 200 | 请先添加提现地址  
58204 | 200 | 因您的账户活动触发风控，暂停提现。请联系客户支持寻求帮助。  
58205 | 200 | 提现金额大于单笔提现最大金额  
58206 | 200 | 提现金额小于单笔最小提现金额  
58207 | 200 | 提币地址不在认证地址列表内 (带标签的提币地址格式为 “address:label”)  
58208 | 200 | 提现失败，邮箱未绑定  
58209 | 200 | 子账户不能充值或提现，请在主账户中进行提现。  
58210 | 200 | 由于无法验证您的身份，提币操作未能成功。请通过欧易 App 或官网完成提币操作。  
58212 | 200 | 提现手续费应填写为提币数量的{0}%  
58213 | 200 | 内部转账地址不合法，必须是邮箱、手机号或者账户名  
58214 | 200 | {chainName}维护中，暂停提币  
58215 | 200 | 提币申请ID不存在  
58216 | 200 | 不允许执行该操作  
58217 | 200 | 您当前的提现地址存在风险，暂时不能提现，详情请联系客服  
58218 | 200 | 内部提现失败，请检查参数toAddr与areaCode  
58219 | 200 | 为保障您的资金安全，修改手机号/邮箱/谷歌验证后24小时之内将无法提现  
58220 | 200 | 提币请求已撤销  
58221 | 200 | toAddr参数格式有误，提币地址需要加上标签，格式应该为“地址:标签”  
58222 | 200 | 无效的提币地址  
58223 | 200 | 提币到此合约地址需要支付更高的手续费  
58224 | 200 | 该类型币种暂不支持链上提币到 OKX 地址，请通过内部转账进行提币  
58225 | 200 | 抱歉，由于当地法律法规，欧易无法为{region}未认证用户提供服务，所以您无法向该用户转账  
58226 | 200 | {chainName} 已下线，不支持提币  
58227 | 200 | 不可交易资产提币只能全部提出  
58228 | 200 | 不可交易资产提币要求 API key 必须绑定 IP  
58229 | 200 | 资金账户手续费不足 {fee} USDT  
58230 | 200 | 根据欧易的合规政策，您需要完成 Lv. 1 身份认证方可继续提币  
58231 | 200 | 由于您的收款人尚未完成 Lv. 1 身份认证，内部转账暂时无法完成  
58232 | 200 | 您已超出个人身份验证 (Lv.1) 的提币上限，请完成照片验证 (Lv. 2) ，即可提升提币限额  
58233 | 200 | 根据当地法律法规，欧易无法为未认证用户提供服务，请先完成身份认证再继续提币  
58234 | 200 | 根据当地法律法规，收款人必须完成身份认证方可收到您的转账  
58235 | 200 | 根据当地法律法规，欧易无法为仅完成基本认证的用户提供服务，请先完成高级认证再继续提币  
58236 | 200 | 根据当地法律法规，仅完成基础认证的收款人无法收取转账，您的收款人必须完成高级认证方可收到您的转账  
58237 | 200 | 根据当地法律法规，请提供准确的接收方信息 (rcvrInfo)。对于交易所地址，请一并提供交易所信息和接收人的身份信息({recipientParameters})。  
58238 | 200 | 提币到交易所地址需提供完整的接收方信息，包括交易所信息和接收人的身份信息  
58239 | 200 | 不支持 API 提币至私人钱包。请通过欧易 App 或官网完成提币操作。  
58240 | 200 | 根据当地法律法规，为保障用户安全，您需要完成身份认证方可继续使用我们的服务。若您不希望进行身份认证，请联系客服团队了解详情。我们致力于为用户提供一个安全的平台，感谢您的理解与支持。  
58241 | 200 | 根据当地法律法规，内部转账功能暂时无法使用  
58242 | 200 | 受收款人所在地法律法规限制，本次内部转账无法完成  
58243 | 200 | 由于您的收款人尚未完成法币入金，对方不能接收本次转账  
58244 | 200 | 请先完成法币入金，再进行您的操作  
58248 | 200 | 根据当地法律法规限制，提币API已被暂时禁用。请使用OKX网页或OKX手机APP进行提币操作。  
58249 | 200 | 该币种暂不支持 API 提币，请于欧易网页端或 App 端进行提币。  
58252 | 200 | 为保障您的资产安全，首次进行 TRY 交易后，提币将在 48 小时内受到限制。  
58254 | 200 | 由于您所在国家或地区的合规限制，API 提币至私人钱包之前，需要先通过欧易 App 或官网完成 digital signature 或者 satoshi test。  
58256 | 200 | 您每 24 小时最多可提取价值为 {dailyLimit} {symbol} 的稳定币，当前还可提取 {quotaRemaining} {symbol}。  
58257 | 200 | 您每月最多可提取价值为 {monthlyLimit} {symbol} 的稳定币，当前还可提取 {quotaRemaining} {symbol}。  
58258 | 200 | 您每 24 小时最多可提取价值为 {dailyLimit} {symbol} 的数字货币，当前还可提取 {quotaRemaining} {symbol}。  
58300 | 200 | 创建充值地址超过上限  
58301 | 200 | 充值地址不存在  
58302 | 200 | 充值地址需要标签  
58303 | 200 | 该链{chain}充值当前不可用  
58304 | 200 | 创建invoice失败  
58305 | 200 | 找不到充币地址，请完成身份认证并生成充币地址  
58306 | 200 | 根据欧易的合规政策，您需要完成 Lv. 1 身份认证方可继续充币  
58307 | 200 | 您已超出个人身份验证 (Lv.1) 的充币上限。超出充币上限的资产已被冻结，请完成照片验证 (Lv. 2) ，即可提升充币限额  
58308 | 200 | 根据当地法律法规，欧易无法为未认证用户提供服务，请先完成身份认证再继续充币  
58309 | 200 | 根据当地法律法规，欧易无法为仅完成基本认证的用户提供服务，请先完成高级认证再继续充币  
58310 | 200 | 无法创建新的充币地址，请稍后重试  
58350 | 200 | 您的余额不足  
58351 | 200 | invoice已经过期  
58352 | 200 | invoice无效  
58353 | 200 | 充币数量需要在限额范围内  
58354 | 200 | 单日达到生成invoice 10,000 个的上限  
58355 | 200 | 用户没有使用此API接口的权限，请联系您的客户经理  
58356 | 200 | 同节点账户不支持闪电网络充币或提币  
58358 | 200 | 参数fromCcy与参数toCcy不可相同  
58373 | 200 | {ccy} 最小兑换数量为 {amount}  
58381 | 200 | 该功能暂不支持  
58382 | 200 | 无法处理解锁请求，请通过用户界面重试  
58383 | 200 | 未找到充值记录，无法处理解锁请求  
58384 | 200 | 根据当地法规，请提供准确的发送方信息。对于交易所地址，请同时提供交易所信息和发送方身份详情