---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#overview-rate-limits-fill-ratio-based-sub-account-rate-limit
anchor_id: overview-rate-limits-fill-ratio-based-sub-account-rate-limit
api_type: API
updated_at: 2026-07-01 19:53:19.567005
---

# Fill ratio based sub-account rate limit

This is only applicable to >= VIP5 customers.   
As an incentive for more efficient trading, the exchange will offer a higher sub-account rate limit to clients with a high trade fill ratio.   
  
The exchange calculates two ratios based on the transaction data from the past 7 days at 00:00 UTC.

  1. Sub-account fill ratio: This ratio is determined by dividing (the trade volume in USDT of the sub-account) by (sum of (new and amendment request count per symbol * symbol multiplier) of the sub-account). Note that the master trading account itself is also considered as a sub-account in this context.
  2. Master account aggregated fill ratio: This ratio is calculated by dividing (the trade volume in USDT on the master account level) by (the sum (new and amendment count per symbol * symbol multiplier] of all sub-accounts).

  

The symbol multiplier allows for fine-tuning the weight of each symbol. A smaller symbol multiplier (<1) is used for smaller pairs that require more updates per trading volume. All instruments have a default symbol multiplier, and some instruments will have overridden symbol multipliers.

InstType | Override rule | Overridden symbol multiplier | Default symbol multiplier  
---|---|---|---  
Perpetual Futures | Per instrument ID | `1`   
Instrument ID:   
BTC-USDT-SWAP   
BTC-USD-SWAP   
ETH-USDT-SWAP   
ETH-USD-SWAP | `0.2`  
Expiry Futures | Per instrument Family | `0.3`   
Instrument Family:   
BTC-USDT   
BTC-USD   
ETH-USDT   
ETH-USD | `0.1`  
Spot | Per instrument ID | `0.5`   
Instrument ID:   
BTC-USDT   
ETH-USDT | `0.1`  
Options | Per instrument Family |  | `0.1`  
  
The fill ratio computation excludes block trading, spread trading, MMP and fiat orders for order count; and excludes block trading, spread trading for trade volume. Only successful order requests (sCode=0) are considered.

  
  

At 08:00 UTC, the system will use the maximum value between the sub-account fill ratio and the master account aggregated fill ratio based on the data snapshot at 00:00 UTC to determine the sub-account rate limit based on the table below. For broker (non-disclosed) clients, the system considers the sub-account fill ratio only.

| Fill ratio[x<=ratio<y) | Sub-account rate limit per 2 seconds(new and amendment)  
---|---|---  
Tier 1 | [0,1) | 1,000  
Tier 2 | [1,2) | 1,250  
Tier 3 | [2,3) | 1,500  
Tier 4 | [3,5) | 1,750  
Tier 5 | [5,10) | 2,000  
Tier 6 | [10,20) | 2,500  
Tier 7 | [20,50) | 3,000  
Tier 8 | >= 50 | 10,000  
  
If there is an improvement in the fill ratio and rate limit to be uplifted, the uplift will take effect immediately at 08:00 UTC. However, if the fill ratio decreases and the rate limit needs to be lowered, a one-day grace period will be granted, and the lowered rate limit will only be implemented on T+1 at 08:00 UTC. On T+1, if the fill ratio improves, the higher rate limit will be applied accordingly. In the event of client demotion to VIP4, their rate limit will be downgraded to Tier 1, accompanied by a one-day grace period.

  

If the 7-day trading volume of a sub-account is less than 1,000,000 USDT, the fill ratio of the master account will be applied to it.

  

For newly created sub-accounts, the Tier 1 rate limit will be applied at creation until T+1 8am UTC, at which the normal rules will be applied.

  

Block trading, spread trading, MMP and spot/margin orders are exempted from the sub-account rate limit.

  

The exchange offers [GET / Account rate limit](/docs-v5/en/#order-book-trading-trade-get-account-rate-limit) endpoint that provides ratio and rate limit data, which will be updated daily at 8am UTC. It will return the sub-account fill ratio, the master account aggregated fill ratio, current sub-account rate limit and sub-account rate limit on T+1 (applicable if the rate limit is going to be demoted).   
  
The fill ratio and rate limit calculation example is shown below. Client has 3 accounts, symbol multiplier for BTC-USDT-SWAP = 1 and XRP-USDT = 0.1.

  1. Account A (master account): 
     1. BTC-USDT-SWAP trade volume = 100 USDT, order count = 10;
     2. XRP-USDT trade volume = 20 USDT, order count = 15;
     3. Sub-account ratio = (100+20) / (10 * 1 + 15 * 0.1) = 10.4
  2. Account B (sub-account): 
     1. BTC-USDT-SWAP trade volume = 200 USDT, order count = 100;
     2. XRP-USDT trade volume = 20 USDT, order count = 30;
     3. Sub-account ratio = (200+20) / (100 * 1 + 30 * 0.1) = 2.13
  3. Account C (sub-account): 
     1. BTC-USDT-SWAP trade volume = 300 USDT, order count = 1000;
     2. XRP-USDT trade volume = 20 USDT, order count = 45;
     3. Sub-account ratio = (300+20) / (100 * 1 + 45 * 0.1) = 3.06
  4. Master account aggregated fill ratio = (100+20+200+20+300+20) / (10 * 1 + 15 * 0.1 + 100 * 1 + 30 * 0.1 + 100 * 1 + 45 * 0.1) = 3.01
  5. Rate limit of accounts 
     1. Account A = max(10.4, 3.01) = 10.4 -> 2500 order requests/2s
     2. Account B = max(2.13, 3.01) = 3.01 -> 1750 order requests/2s
     3. Account C = max(3.06, 3.01) = 3.06 -> 1750 order requests/2s

---

# 基于成交比率的子账户限速

仅适用于用户等级 >= VIP5的用户。   
为了激励更高效的交易，交易所将为交易成交比率高的用户提供更高的子账户限速。

交易所将在每天 00:00 UTC，根据过去七天的交易数据计算两个比率。

  1. 子账户成交比率：该比率为（子账户的USDT对应交易量）/（每个交易产品的新增和修改请求数 * 交易产品乘数之和）。请注意，在这种情况下，母账户自身也被视为一个“子账户”。
  2. 母账户合计成交比率：该比率为（母账户层面的USDT对应交易量）/（所有子账户各个交易产品的新增和修改请求数 * 交易产品乘数之和）。

交易产品乘数允许我们微调每个交易产品对成交比率的影响权重。较小的交易产品乘数（<1）适用于小币对及合约，在交易这些币对、合约时，为达到相同交易量往往需要更多的订单。所有的交易产品都有默认乘数，部分交易产品有独立的乘数。详情请见下表。

业务线 | 覆盖规则 | 独立乘数 | 默认乘数  
---|---|---|---  
永续 | 产品ID | `1`   
产品ID：   
BTC-USDT-SWAP   
BTC-USD-SWAP   
ETH-USDT-SWAP   
ETH-USD-SWAP | `0.2`  
交割 | 交易品种 | `0.3`   
交易品种：   
BTC-USDT   
BTC-USD   
ETH-USDT   
ETH-USD | `0.1`  
币币 | 产品ID | `0.5`   
产品ID：   
BTC-USDT   
ETH-USDT | `0.1`  
期权 | 交易品种 |  | `0.1`  
  
成交比率计算不包括大宗交易，价差交易，做市商保护（MMP），以及法币类型订单对应的订单数量；并且不包括大宗交易，价差交易对应的交易量。仅考虑 `sCode = 0` 的成功请求。  

每日 08:00 UTC，系统将根据UTC时间 00:00 的数据快照，选取子账户成交比率及母账户合计成交比率中的较大值决定子账户的未来限速。详情请见下表。对于独立经纪商，系统只会取子账户的成交比率。

| 成交比率[x<=比率<y) | 子账户每2秒限速(新订单及修改订单请求)  
---|---|---  
Tier 1 | [0,1) | 1,000  
Tier 2 | [1,2) | 1,250  
Tier 3 | [2,3) | 1,500  
Tier 4 | [3,5) | 1,750  
Tier 5 | [5,10) | 2,000  
Tier 6 | [10,20) | 2,500  
Tier 7 | [20,50) | 3,000  
Tier 8 | >= 50 | 10,000  
  
若成交比率和预期限速有所改善，则提升将于 08:00 (UTC) 立即生效。但若成交比率下降，需要降低未来限速，系统将给予一天的宽限期，降低后的速率限制将在 T+1 08:00 (UTC) 实施。在 T+1 时，若成交比率提高，则将立即授予更高的限速。若用户的交易手续费等级降级为 VIP4，其限速将降低为最低档位，并有一天的宽限期。

  

若子账户7日交易量低于1,000,000 USDT，则按照母账户的合计成交比率实施限速。

  

对于新创建的子账户，创建时将应用最低档位限速，在 T+1 08:00 (UTC)时，将开始应用上述限速规则。

  

大宗交易、价差交易、做市商保护（MMP）以及币币、币币杠杆订单不受子账户限速限制。

  

交易所提供 [GET / 获取账户限速](/docs-v5/zh/#order-book-trading-trade-get-account-rate-limit) 接口以便用户查询成交比率以及限速数据，数据将于每天 08:00 (UTC) 更新。该接口将返回子账户成交比率，母账户合计成交比率，子账户当前限速以及 T+1 时的预期子账户限速（适用于限速降级）。

  

成交比率、限速计算样例如下。用户有三个账户，交易产品 BTC-USDT-SWAP 及 XRP-USDT 的乘数分别为1，0.1。

  1. 账户 A（母账户）： 
     1. BTC-USDT-SWAP 交易量为100 USDT，订单数量为10;
     2. XRP-USDT 交易量为20 USDT，订单数量为15;
     3. 子账户成交比率 = (100+20) / (10 * 1 + 15 * 0.1) = 10.4
  2. 账户 B (子账户)： 
     1. BTC-USDT-SWAP 交易量为200 USDT，订单数量为100;
     2. XRP-USDT 交易量为20 USDT，订单数量为30;
     3. 子账户成交比率 = (200+20) / (100 * 1 + 30 * 0.1) = 2.13
  3. 账户 C (子账户)： 
     1. BTC-USDT-SWAP 交易量为300 USDT，订单数量为100;
     2. XRP-USDT 交易量为20 USDT，订单数量为45;
     3. 子账户成交比率 = (300+20) / (100 * 1 + 45 * 0.1) = 3.06
  4. 母账户合计成交比率 = (100+20+200+20+300+20) / (10 * 1 + 15 * 0.1 + 100 * 1 + 30 * 0.1 + 100 * 1 + 45 * 0.1) = 3.01
  5. 账户限速 
     1. 账户 A = max(10.4, 3.01) = 10.4 -> 2500订单请求/2秒
     2. 账户 B = max(2.13, 3.01) = 3.01 -> 1750订单请求/2秒
     3. 账户 C = max(3.06, 3.01) = 3.06 -> 1750订单请求/2秒