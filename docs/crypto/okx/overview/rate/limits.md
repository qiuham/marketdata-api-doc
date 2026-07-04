---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#overview-rate-limits
anchor_id: overview-rate-limits
api_type: API
updated_at: 2026-07-04 19:37:03.423334
---

# Rate Limits

Our REST and WebSocket APIs use rate limits to protect our APIs against malicious usage so our trading platform can operate reliably and fairly.  
When a request is rejected by our system due to rate limits, the system returns error code 50011 (Rate limit reached. Please refer to API documentation and throttle requests accordingly).  
The rate limit is different for each endpoint. You can find the limit for each endpoint from the endpoint details. Rate limit definitions are detailed below:

  * WebSocket login and subscription rate limits are based on connection.

  * Public unauthenticated REST rate limits are based on IP address.

  * Private REST rate limits are based on User ID (sub-accounts have individual User IDs).

  * WebSocket order management rate limits are based on User ID (sub-accounts have individual User IDs).

### Trading-related APIs

For Trading-related APIs (place order, cancel order, and amend order) the following conditions apply:

  * Rate limits are shared across the REST and WebSocket channels. 

  * Rate limits for placing orders, amending orders, and cancelling orders are independent from each other. 

  * Rate limits are defined on the Instrument ID level (except Options)

  * Rate limits for Options are defined based on the Instrument Family level. Refer to the [Get instruments](/docs-v5/en/#public-data-rest-api-get-instruments) endpoint to view Instrument Family information.

  * Rate limits for a multiple order endpoint and a single order endpoint are also independent, with the exception being when there is only one order sent to a multiple order endpoint, the order will be counted as a single order and adopt the single order rate limit. 

### Sub-account rate limit

At the sub-account level, we allow a maximum of 1000 order requests per 2 seconds. Only new order requests and amendment order requests will be counted towards this limit. The limit encompasses all requests from the endpoints below. For batch order requests consisting of multiple orders, each order will be counted individually. Error code 50061 is returned when the sub-account rate limit is exceeded. The existing rate limit rule per instrument ID remains unchanged and the existing rate limit and sub-account rate limit will operate in parallel. If clients require a higher rate limit, clients can trade via multiple sub-accounts.

  * [POST / Place order](/docs-v5/en/#order-book-trading-trade-post-place-order)
  * [POST / Place multiple orders](/docs-v5/en/#order-book-trading-trade-post-place-multiple-orders)
  * [POST / Amend order](/docs-v5/en/#order-book-trading-trade-post-amend-order)
  * [POST / Amend multiple orders](/docs-v5/en/#order-book-trading-trade-post-amend-multiple-orders)

  * [WS / Place order](/docs-v5/en/#order-book-trading-trade-ws-place-order)

  * [WS / Place multiple orders](/docs-v5/en/#order-book-trading-trade-ws-place-multiple-orders)

  * [WS / Amend order](/docs-v5/en/#order-book-trading-trade-ws-amend-order)

  * [WS / Amend multiple orders](/docs-v5/en/#order-book-trading-trade-ws-amend-multiple-orders)   

### Fill ratio based sub-account rate limit

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

### Best practices

If you require a higher request rate than our rate limit, you can set up different sub-accounts to batch request rate limits. We recommend this method for throttling or spacing out requests in order to maximize each accounts' rate limit and avoid disconnections or rejections.

---

# 限速

我们的 REST 和 WebSocket API 使用限速来保护我们的 API 免受恶意使用，因此我们的交易平台可以可靠和公平地运行。  
当请求因限速而被我们的系统拒绝时，系统会返回错误代码 50011（用户请求频率过快，超过该接口允许的限额。请参考 API 文档并限制请求）。  
每个接口的限速都不同。 您可以从接口详细信息中找到每个接口的限制。 限速定义详述如下：

  * WebSocket 登录和订阅限速基于连接。

  * 公共未经身份验证的 REST 限速基于 IP 地址。

  * 私有 REST 限速基于 User ID（子帐户具有单独的 User ID）。

  * WebSocket 订单管理限速基于 User ID（子账户具有单独的 User ID）。

### 交易相关API 

对于与交易相关的 API（下订单、取消订单和修改订单），以下条件适用：

  * 限速在 REST 和 WebSocket 通道之间共享。

  * 下单、修改订单、取消订单的限速相互独立。

  * 限速在 Instrument ID 级别定义（期权除外）

  * 期权的限速是根据 Instrument Family 级别定义的。 请参阅 [获取交易产品基础信息](/docs-v5/zh/#public-data-rest-api-get-instruments) 接口以查看交易品种信息。

  * 批量订单接口和单订单接口的限速也是独立的，除了只有一个订单发送到批量订单接口时，该订单将被视为一个订单并采用单订单限速。

### 子账户限速 

子账户维度，每2秒最多允许1000个订单相关请求。仅有新订单及修改订单请求会被计入此限制。此限制涵盖以下所列的所有接口。对于包含多个订单的批量请求，每个订单将被单独计数。如果请求频率超过限制，系统会返回50061错误码。产品ID维度的限速规则保持不变，现有的限速规则与新增的子账户维度限速将并行运行。若用户需要更高的速率限制，可以通过多个子账户进行交易。

  * [POST / 下单](/docs-v5/zh/#order-book-trading-trade-post-place-order)
  * [POST / 批量下单](/docs-v5/zh/#order-book-trading-trade-post-place-multiple-orders)
  * [POST / 修改订单](/docs-v5/zh/#order-book-trading-trade-post-amend-order)
  * [POST / 批量修改订单](/docs-v5/zh/#order-book-trading-trade-post-amend-multiple-orders)

  * [WS / 下单](/docs-v5/zh/#order-book-trading-trade-ws-place-order)

  * [WS / 批量下单](/docs-v5/zh/#order-book-trading-trade-ws-place-multiple-orders)

  * [WS / 改单](/docs-v5/zh/#order-book-trading-trade-ws-amend-order)

  * [WS / 批量改单](/docs-v5/zh/#order-book-trading-trade-ws-amend-multiple-orders)

### 基于成交比率的子账户限速 

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

### 最佳实践 

如果您需要的请求速率高于我们的限速，您可以设置不同的子账户来批量请求限速。 我们建议使用此方法来限制或间隔请求，以最大化每个帐户的限速并避免断开连接或拒绝请求。