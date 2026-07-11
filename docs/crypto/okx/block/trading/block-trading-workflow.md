---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#block-trading-block-trading-workflow
anchor_id: block-trading-block-trading-workflow
api_type: API
updated_at: 2026-07-11 19:13:22.118162
---

# Block Trading Workflow

A block trade is a **large sized, privately negotiated** transaction that allows traders to execute spot, perpetuals, futures, options and a combination of instruments (multi leg) which are traded **outside the order book** and at a **mutually agreed price** between the counter-parties. Once the transaction economics have been agreed upon, it will be submitted to OKX to be seamlessly margined, cleared and executed.  
  
**Basic Concepts**

  1. **RFQs** \- Request for Quote sent by the Taker to Maker(s). It captures the quantity, instrument or multi instrument strategy that a Taker wants to trade.
  2. **Quotes** \- Quotes are created by the _Maker_  in response to a requested RFQ.
  3. **Trades** \- Trades occur when the _Taker_ successfully _executes_ upon a makers quote to an RFQ.

**High Level Workflow**

To trade as either Taker or Maker, users need to deposit at least 100,000 USD into their trading account. In addition, to become a Maker, [Please complete the form to access block trading](https://share.hsforms.com/1mYdfKtJJR3CC03IyCeC6hg3a1fq).

  1. Taker creates an RFQ and selects which counterparties to broadcast the RFQ to.
  2. Multiple Maker(s) send a two way quote as a response to the RFQ.
  3. Taker chooses to execute upon the best quote and the trade is sent to OKX for clearing & settlement.
  4. Taker & Maker receive confirmation of the trade's execution. 
  5. Trade economics are published to market feed. (minus counterparty info) 

**Self-trade Prevention** Users cannot send RFQ requests to themselves.

**Taker's Perspective**

  1. Taker creates an RFQ using `POST /api/v5/rfq/create-rfq`. Taker can pull available instruments via `GET /api/v5/public/instruments` and available counterparties from `GET /api/v5/rfq/counterparties`.
  2. Taker can cancel an RFQ anytime until it becomes inactive with `POST /api/v5/rfq/cancel-rfq`.
  3. Maker, who is a requested counterparty to the RFQ, and is notified over the `rfqs` WebSocket channel, can provide a Quote to the RFQ.
  4. Taker, who will be notified of quotes from the `quotes` WebSocket channel, can execute upon the best Quote with `POST /api/v5/rfq/execute-quote`.
  5. Taker will receive confirmation of the trade's successful execution on the `struc-block-trades` and `rfqs` WebSocket channel.
  6. Taker will also receive confirmation of the trade being completed on the `public-struc-block-trades` WebSocket channel as well as all other block trades on OKX.

**Maker's Perspective**

  1. Maker is notified about a new RFQ who they are a counterparty to, on the `rfqs` WebSocket channel.
  2. Maker can create a one way or two way Quote using `POST /api/v5/rfq/create-quote`.
  3. Maker can cancel an existing quote anytime until it becomes inactive with `POST /api/v5/rfq/cancel-quote`.
  4. Taker chooses to execute upon an available Quote.
  5. Maker will receive updates of their Quote from the `quotes` WebSocket channel.
  6. Maker will receive confirmation of the successful execution of their Quote from the `struc-block-trades` and `quotes` WebSocket channel.
  7. Maker will receive confirmation of the trade being completed on the `public-struc-block-trades` WebSocket channel as well as all other block trades on OKX.

---

# 大宗交易工作流程

大宗交易时指在非公开市场进行的、私下议定的、满足规定最小交易手数的期货、期权、交割、永续或混合产品的大单交易。 交易细节一经确认，此笔交易会被提交到OKX以进行保证金计算，清算和执行。  
  
**基本概念**

  1. **询价单（RFQs） -** 询价单，由询价方发给报价方. 询价单包括询价方希望交易的一种或多种产品及其数量。
  2. **报价单 -** 报价单，由报价方发给询价方对询价单的报价。
  3. **交易** \- 当询价方接受并执行报价方的报价单，一笔交易就由此产生。

**基本工作流程**

要以询价方或报价方身份进行交易，用户需要在交易账户中存入至少100,000美元。 此外，要成为报价方[请填写表格以访问大宗交易](https://share.hsforms.com/1mYdfKtJJR3CC03IyCeC6hg3a1fq).

  1. 询价方创建一个询价单（RFQ），并选择希望收到此询价单的报价方。 
  2. 不同报价方发送报价单回应此询价单。
  3. 询价方选择执行最好的报价单产生交易。OKX收到此笔交易并做结算。
  4. 询价方和报价方收到交易执行的确认。
  5. 交易详情发布在公共市场数据频道上（不包含交易方信息）。

**询价方角度**

  1. 询价方使用`POST /api/v5/rfq/create-rfq`创建询价单。询价方可通过`GET /api/v5/public/instruments`查询可询价产品信息，并通过`GET /api/v5/rfq/counterparties`查询可选择报价方信息。
  2. 询价方可以在询价单有效的任何时候通过`POST /api/v5/rfq/cancel-rfq`取消询价单。
  3. 报价方，如果是询价方选择的报价方之一，会在`rfqs`推送频道收到询价单信息，并可作出相应报价。
  4. 询价方，在`quotes`推送频道收到报价信息后，可以选择最优报价并通过`POST /api/v5/rfq/execute-quote`执行。
  5. 询价方会在`struc-block-trades`和`rfqs`推送频道收到交易成功执行确认。
  6. 询价方也会在`public-struc-block-trades`推送频道收到此笔交易以及其他OKX大宗交易的确认信息。

**报价方角度**

  1. 当有一个新的询价单发出，并且报价方是被选择的报价方之一时，报价方会在rfqs推送频道接收到此询价单信息。
  2. 报价方创建一个单向或者双向的报价单并通过`POST /api/v5/rfq/create-quote`发出。
  3. 报价方可以通过`POST /api/v5/rfq/cancel-quote`任意取消一个有效的报价单。
  4. 询价方选择执行最优报价单。
  5. 报价方通过`quotes`推送频道接收他们报价单的状态更新。
  6. 报价方会在`struc-block-trades`和`quotes`推送频道收到他们报价单的交易成功执行确认。
  7. 报价方也会在`public-struc-block-trades`推送频道收到此笔交易以及其他OKX大宗交易的确认信息。