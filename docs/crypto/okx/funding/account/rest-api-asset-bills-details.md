---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#funding-account-rest-api-asset-bills-details
anchor_id: funding-account-rest-api-asset-bills-details
api_type: REST
updated_at: 2026-07-05 19:35:15.041127
---

# Asset bills details

Query the billing record in the past month.  
  
#### Rate Limit: 6 Requests per second

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/asset/bills`

> Request Example
    
    
    GET /api/v5/asset/bills
    
    
    
    
    import okx.Funding as Funding
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading: 0, Demo trading: 1
    
    fundingAPI = Funding.FundingAPI(apikey, secretkey, passphrase, False, flag)
    
    # Get asset bills details
    result = fundingAPI.get_bills()
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
ccy | String | No | Currency  
type | String | No | Bill type  
`1`: Deposit  
`2`: Withdrawal  
`13`: Canceled withdrawal  
`20`: Transfer to sub account (for master account)  
`21`: Transfer from sub account (for master account)  
`22`: Transfer out from sub to master account (for sub-account)  
`23`: Transfer in from master to sub account (for sub-account)  
`28`: Manually claimed Airdrop  
`47`: System reversal  
`48`: Event Reward  
`49`: Event Giveaway  
`68`: Fee rebate (by rebate card)  
`72`: Token received  
`73`: Token given away  
`74`: Token refunded  
`75`: [Simple earn flexible] Subscription  
`76`: [Simple earn flexible] Redemption  
`77`: Jumpstart distribute  
`78`: Jumpstart lock up  
`80`: DEFI/Staking subscription  
`82`: DEFI/Staking redemption  
`83`: Staking yield  
`84`: Violation fee  
`89`: Deposit yield  
`116`: [Fiat] Place an order  
`117`: [Fiat] Fulfill an order  
`118`: [Fiat] Cancel an order  
`124`: Jumpstart unlocking  
`130`: Transferred from Trading account  
`131`: Transferred to Trading account  
`132`: [P2P] Frozen by customer service  
`133`: [P2P] Unfrozen by customer service  
`134`: [P2P] Transferred by customer service  
`135`: Cross chain exchange  
`137`: [ETH Staking] Subscription  
`138`: [ETH Staking] Swapping  
`139`: [ETH Staking] Earnings  
`146`: Customer feedback  
`150`: Affiliate commission  
`151`: Referral reward  
`152`: Broker reward  
`160`: Dual Investment subscribe  
`161`: Dual Investment collection  
`162`: Dual Investment profit  
`163`: Dual Investment refund  
`172`: [Affiliate] Sub-affiliate commission  
`173`: [Affiliate] Fee rebate (by trading fee)  
`174`: Jumpstart Pay  
`175`: Locked collateral  
`176`: Loan  
`177`: Added collateral  
`178`: Returned collateral  
`179`: Repayment  
`180`: Unlocked collateral  
`181`: Airdrop payment  
`185`: [Broker] Convert reward  
`187`: [Broker] Convert transfer  
`189`: Mystery box bonus  
`195`: Untradable asset withdrawal  
`196`: Untradable asset withdrawal revoked  
`197`: Untradable asset deposit  
`198`: Untradable asset collection reduce  
`199`: Untradable asset collection increase  
`200`: Buy  
`202`: Price Lock Subscribe  
`203`: Price Lock Collection  
`204`: Price Lock Profit  
`205`: Price Lock Refund  
`207`: Dual Investment Lite Subscribe  
`208`: Dual Investment Lite Collection  
`209`: Dual Investment Lite Profit  
`210`: Dual Investment Lite Refund  
`212`: [Flexible loan] Multi-collateral loan collateral locked  
`215`: [Flexible loan] Multi-collateral loan collateral released  
`217`: [Flexible loan] Multi-collateral loan borrowed  
`218`: [Flexible loan] Multi-collateral loan repaid  
`232`: [Flexible loan] Subsidized interest received  
`220`: Delisted crypto  
`221`: Blockchain's withdrawal fee  
`222`: Withdrawal fee refund  
`223`: SWAP lead trading profit share  
`225`: Shark Fin subscribe  
`226`: Shark Fin collection  
`227`: Shark Fin profit  
`228`: Shark Fin refund  
`229`: Airdrop  
`232`: Subsidized interest received  
`233`: Broker rebate compensation  
`240`: Snowball subscribe  
`241`: Snowball refund  
`242`: Snowball profit  
`243`: Snowball trading failed  
`249`: Seagull subscribe  
`250`: Seagull collection  
`251`: Seagull profit  
`252`: Seagull refund  
`263`: Strategy bots profit share  
`265`: Signal revenue  
`266`: SPOT lead trading profit share  
`270`: DCD broker transfer  
`271`: DCD broker rebate  
`272`: [Convert] Buy Crypto/Fiat  
`273`: [Convert] Sell Crypto/Fiat  
`284`: [Custody] Transfer out trading sub-account  
`285`: [Custody] Transfer in trading sub-account  
`286`: [Custody] Transfer out custody funding account  
`287`: [Custody] Transfer in custody funding account  
`288`: [Custody] Fund delegation   
`289`: [Custody] Fund undelegation  
`299`: Affiliate recommendation commission  
`300`: Fee discount rebate  
`303`: Snowball market maker transfer  
~~`304`: [Simple Earn Fixed] Order submission~~  
~~`305`: [Simple Earn Fixed] Order redemption~~  
~~`306`: [Simple Earn Fixed] Principal distribution~~  
~~`307`: [Simple Earn Fixed] Interest distribution (early termination compensation)~~  
~~`308`: [Simple Earn Fixed] Interest distribution~~  
~~`309`: [Simple Earn Fixed] Interest distribution (extension compensation) ~~  
`311`: Crypto dust auto-transfer in  
`313`: Sent by gift  
`314`: Received from gift  
`315`: Refunded from gift  
`328`: [SOL staking] Send Liquidity Staking Token reward  
`329`: [SOL staking] Subscribe Liquidity Staking Token staking  
`330`: [SOL staking] Mint Liquidity Staking Token  
`331`: [SOL staking] Redeem Liquidity Staking Token order  
`332`: [SOL staking] Settle Liquidity Staking Token order  
`333`: Trial fund reward  
`339`: [Simple Earn Fixed] Order submission  
`340`: [Simple Earn Fixed] Order failure refund  
`341`: [Simple Earn Fixed] Redemption  
`342`: [Simple Earn Fixed] Principal  
`343`: [Simple Earn Fixed] Interest  
`344`: [Simple Earn Fixed] Compensatory interest  
`345`: [Institutional Loan] Principal repayment  
`346`: [Institutional Loan] Interest repayment  
`347`: [Institutional Loan] Overdue penalty  
`348`: [BTC staking] Subscription  
`349`: [BTC staking] Redemption  
`350`: [BTC staking] Earnings  
`351`: [Institutional Loan] Loan disbursement  
`354`: Copy and bot rewards  
`361`: Deposit from closed sub-account  
`372`: Asset segregation  
`373`: Asset release  
`400`: Auto lend interest   
`408`: Auto earn USDG interest  
`476`: Transferred out to Cloud Exchange  
`477`: Transferred in from Cloud Exchange  
thirdPartyType | String | No | Third-party custody type. If not specified, defaults to `1` (for backward compatibility).  
`1`: Copper  
`2`: Komainu  
`5`: SCB  
When a master account is bound to multiple custody providers, use this parameter to filter bills by the specified custody provider. Applicable to bill types `284`–`289`.  
clientId | String | No | Client-supplied ID for transfer or withdrawal  
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
after | String | No | Pagination of data to return records earlier than the requested `ts`, Unix timestamp format in milliseconds, e.g. `1597026383085`  
before | String | No | Pagination of data to return records newer than the requested `ts`, Unix timestamp format in milliseconds, e.g. `1597026383085`  
limit | String | No | Number of results per request. The maximum is `100`. The default is `100`.  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
            "billId": "12344",
            "ccy": "BTC",
            "clientId": "",
            "balChg": "2",
            "bal": "12",
            "type": "1",
            "ts": "1597026383085",
            "notes": ""
        }]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
billId | String | Bill ID  
ccy | String | Account balance currency  
clientId | String | Client-supplied ID for transfer or withdrawal  
balChg | String | Change in balance at the account level  
bal | String | Balance at the account level  
type | String | Bill type  
notes | String | Notes  
ts | String | Creation time, Unix timestamp format in milliseconds, e.g.`1597026383085`

---

# 获取资金流水

查询最近一个月内资金账户账单流水  
  
#### 限速：6 次/s

#### 限速规则：User ID

#### 权限：读取

#### HTTP 请求

`GET /api/v5/asset/bills`

> 请求示例
    
    
    GET /api/v5/asset/bills
    
    GET /api/v5/asset/bills?type=1
    
    
    
    
    import okx.Funding as Funding
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    fundingAPI = Funding.FundingAPI(apikey, secretkey, passphrase, False, flag)
    
    # 获取资金流水
    result = fundingAPI.get_bills()
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 否 | 币种  
type | String | 否 | 账单类型  
`1`：充值  
`2`：提现  
`13`：撤销提现  
`20`：转出至子账户（主体是母账户）  
`21`：从子账户转入（主体是母账户）  
`22`：转出到母账户（主体是子账户）  
`23`：母账户转入（主体是子账户）  
`28`：领取  
`47`：系统冲正  
`48`：活动得到  
`49`：活动送出  
`68`：手续费返佣(通过返佣卡)  
`72`：收币  
`73`：送币  
`74`：送币退还  
`75`：[活期简单赚币] 申购  
`76`：[活期简单赚币] 赎回  
`77`：[Jumpstart] 派发  
`78`：[Jumpstart] 锁定  
`80`：[DEFI/锁仓挖矿] 产品申购  
`82`：[DEFI/锁仓挖矿] 产品赎回  
`83`：挖矿收益  
`84`：违约金  
`89`：存币收益  
`116`：法币创建订单  
`117`：法币完成订单  
`118`：法币取消订单  
`124`：[Jumpstart] 解锁  
`130`：从交易账户转入  
`131`：转出至交易账户  
`132`：[P2P] 客服冻结  
`133`：[P2P] 客服解冻  
`134`：[P2P] 客服转交  
`135`：跨链兑换  
`137`：[ETH质押] 申购  
`138`：[ETH质押] 兑换  
`139`：[ETH质押] 收益  
`146`：客户回馈  
`150`：节点返佣  
`151`：邀请奖励  
`152`：经纪商返佣  
`160`：双币赢申购  
`161`：双币赢回款  
`162`：双币赢收益  
`163`：双币赢退款  
`172`：[节点计划] 助力人返佣  
`173`：[节点计划] 手续费返现  
`174`：Jumpstart支付  
`175`：锁定质押物  
`176`：借款转入  
`177`：添加质押物  
`178`：减少质押物  
`179`：还款  
`180`：释放质押物  
`181`：偿还空投糖果  
`185`：[经纪商] 闪兑返佣  
`187`：[经纪商] 闪兑划转  
`189`：盲盒奖励  
`195`：不可交易资产提币  
`196`：不可交易资产提币撤销  
`197`：不可交易资产充值  
`198`：不可交易资产减少  
`199`：不可交易资产增加  
`200`：买入  
`202`：价格锁定申购  
`203`：价格锁定回款  
`204`：价格锁定收益  
`205`：价格锁定退款  
`207`：双币赢精简版申购  
`208`：双币赢精简版回款  
`209`：双币赢精简版收益  
`210`：双币赢精简版退款  
`212`：[活期借币] 多币种借贷锁定质押物  
`215`：[活期借币] 多币种借贷释放质押物  
`217`：[活期借币] 多币种借贷借款转入  
`218`：[活期借币] 多币种借贷还款  
`232`：[活期借币] 利息补贴转出  
`220`：已下架数字货币  
`221`：提币手续费支出  
`222`：提币手续费退款  
`223`：合约带单分润  
`225`：鲨鱼鳍申购  
`226`：鲨鱼鳍回款  
`227`：鲨鱼鳍收益  
`228`：鲨鱼鳍退款  
`229`：空投发放  
`232`：利息补贴入账  
`233`：经纪商佣金补偿  
`240`：雪球申購  
`241`：雪球回款  
`242`：雪球收益  
`243`：雪球交易失败  
`249`：海鸥申购  
`250`：海鸥回款  
`251`：海鸥收益  
`252`：海鸥退款  
`263`：策略分润  
`265`：信号收入  
`266`：现货带单分润  
`270`：DCD经纪商划转  
`271`：DCD经纪商返佣  
`272`：[闪兑] 买入数字货币/法币  
`273`：[闪兑] 卖出数字货币/法币  
`284`：[Custody] 转出交易子账户  
`285`：[Custody] 转入交易子账户  
`286`：[Custody] 转出托管资金账户  
`287`：[Custody] 转入托管资金账户  
`288`：[Custody] 托管资金入金  
`289`：[Custody] 托管资金出金  
`299`：推荐节点返佣  
`300`：手续费折扣返现  
`303`：雪球做市商转账  
~~`304`：[定期简单赚币] 订单提交~~  
~~`305`：[定期简单赚币] 订单赎回~~  
~~`306`：[定期简单赚币] 本金发放~~  
~~`307`：[定期简单赚币] 收益发放 (提前终止订单补偿) ~~  
~~`308`：[定期简单赚币] 收益发放~~  
~~`309`：[定期简单赚币] 补偿收益发放 (订单延期补偿)~~  
`311`：系统转入小额资产  
`313`：发送礼物  
`314`：收到礼物  
`315`：礼物退回  
`328`：[SOL质押] 流动性质押收益  
`329`：[SOL质押] 流动性质押申购  
`330`：[SOL质押] 流动性质押铸币  
`331`：[SOL质押] 流动性质押赎回  
`332`：[SOL质押] 流动性质押结算  
`333`：体验金收益  
`339`：[定期简单赚币] 订单提交  
`340`：[定期简单赚币] 订单失败退款  
`341`：[定期简单赚币] 订单赎回  
`342`：[定期简单赚币] 本金发放  
`343`：[定期简单赚币] 收益发放  
`344`：[定期简单赚币] 补偿收益发放  
`345`：[机构借贷] 本金还款  
`346`：[机构借贷] 利息还款  
`347`：[机构借贷] 逾期罚款  
`348`：[BTC质押] 申购  
`349`：[BTC质押] 赎回  
`350`：[BTC质押] 收益  
`351`：[机构借贷] 发放贷款  
`354`：策略奖励发放  
`361`：已关闭的子账户余额转入  
`372`：资产锁定  
`373`：解除资产锁定  
`400`：自动借币利息  
`408`：自动赚币（USDG赚币）利息  
`476`：云交易所转出  
`477`：云交易所转入  
thirdPartyType | String | 否 | 第三方托管类型。不填则默认为 `1`（向后兼容）。  
`1`：Copper  
`2`：Komainu  
`5`：SCB  
当母账户绑定多家托管商时，使用此参数可筛选指定托管商的账单。适用于账单类型 `284`–`289`。  
clientId | String | 否 | 转账或提币的客户自定义ID  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度要在1-32位之间。  
after | String | 否 | 查询在此之前的内容，值为时间戳，Unix 时间戳为毫秒数格式，如 `1597026383085`  
before | String | 否 | 查询在此之后的内容，值为时间戳，Unix 时间戳为毫秒数格式，如 `1597026383085`  
limit | String | 否 | 分页返回的结果集数量，最大为 100，不填默认返回 100 条  
  
> 返回结果
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
        {
          "billId": "12344",
          "ccy": "BTC",
          "clientId": "",
          "balChg": "2",
          "bal": "12",
          "type": "1",
          "ts": "1597026383085",
          "notes": ""
        }
      ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
billId | String | 账单 ID  
ccy | String | 账户余额币种  
clientId | String | 转账或提币的客户自定义ID  
balChg | String | 账户层面的余额变动数量  
bal | String | 账户层面的余额数量  
type | String | 账单类型  
notes | String | 备注  
ts | String | 账单创建时间，Unix 时间戳的毫秒数格式，如 `1597026383085`