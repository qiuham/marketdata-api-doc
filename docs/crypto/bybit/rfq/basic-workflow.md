---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/rfq/basic-workflow
api_type: REST
updated_at: 2026-07-03 19:16:00.159355
---

# Basic Workflow

**Basic concepts**

  1. Request for Quote (RFQ) – an inquiry sent by the inquiring party to the quoting party. The request for a quote includes one or more products and quantities that the inquiring party wishes to trade.
  2. Quote – provided in response to the inquiry. Sent by the quoting party to the inquiring party.
  3. Transaction – when the inquirer accepts and executes the quote.



**Basic workflow**

  1. The inquirier creates an RFQ and sends it to the quoters of their choice.
  2. Different quoting parties send quotes in response to this inquiry.
  3. The inquiring party chooses to execute the best quote to generate the transaction. The transaction executes and is settled.
  4. The inquiring party and the quoting party receive confirmation of the execution.
  5. The transaction details are published on the public market data channel (excluding party information).



**Creating an RFQ from the inquirer's perspective**

  1. The inquirer uses [/v5/rfq/create-rfq](/docs/v5/rfq/trade/create-rfq) to create an inquiry. The inquirer can query the information of the products with [/v5/market/instruments-info](/docs/v5/market/instrument), and the quoter information can be queried with [/v5/rfq/config query](/docs/v5/rfq/trade/rfq-config).
  2. The inquirer may cancel the inquiry with [/v5/rfq/cancel-rfq](/docs/v5/rfq/trade/cancel-rfq) at any time while the inquiry is in force.
  3. The inquirer can use the endpoint [/v5/rfq/accept-other-quote](/docs/v5/rfq/trade/accept-other-quote) to accept non-LP OTC quotes, thereby expanding the sources of quotations.
  4. The quoting party, if it is one of the quoting parties selected by the inquiry party, will receive the inquiry information in the [rfq.open.rfqs](/docs/v5/rfq/websocket/private/inquiry) WebSocket topic and can make the corresponding quote.
  5. The inquirer, after receiving the offer information in the [rfq.open.quotes](/docs/v5/rfq/websocket/private/quote) WebSocket topic, can choose the best offer and execute it through the [/v5/rfq/execute-quote](/docs/v5/rfq/trade/execute-quote).
  6. Inquirers will receive confirmation of successful trade execution in the [rfq.open.trades](/docs/v5/rfq/websocket/private/transaction) and [rfq.open.rfqs](/docs/v5/rfq/websocket/private/inquiry) WebSocket topics.
  7. Inquirers will also receive confirmation of this and other block trades [rfq.open.public.trades](/docs/v5/rfq/websocket/public/public-transaction) WebSocket topic.



**Creating a quote from the quoter's perspective**

  1. When a new request for a quote is issued and the quoting party is one of the selected quoting parties, the quoting party will receive this request information in the [rfq.open.rfqs](/docs/v5/rfq/websocket/private/inquiry) WebSocket topic.
  2. The quoting party creates a quote and sends it via [/v5/rfq/create-quote](/docs/v5/rfq/trade/create-quote) .
  3. Quoters can cancel a valid quote at will with [/v5/rfq/cancel-quote](/docs/v5/rfq/trade/cancel-quote) .
  4. The inquiring party chooses to execute the optimal quote.
  5. Quoters receive status updates on their quotes via the [rfq.open.quotes](/docs/v5/rfq/websocket/private/quote) WebSocket topic.
  6. Quoters will receive confirmation of the successful execution of their quote on the [rfq.open.trades](/docs/v5/rfq/websocket/private/transaction) and [rfq.open.quotes](/docs/v5/rfq/websocket/private/quote) WebSocket topics.
  7. The quoting party will also receive confirmation of this transaction and other block trades in the [rfq.open.public.trades](/docs/v5/rfq/websocket/public/public-transaction) WebSocket topic.

---

# 基本工作流程

**基本概念**

  1. **報價請求（RFQs）** \- 報價請求是由詢價方發送給報價方的文件，包含一個或多個產品及其數量，詢價方希望進行交易。
  2. **報價單** \- 報價單是報價方針對詢價單所提供的報價。
  3. **交易** \- 當詢價方接受並執行報價方的報價時，交易即完成。



**基本工作流程**

  1. 詢價方創建報價請求（RFQ），並選擇希望接收RFQ的報價方。
  2. 不同的報價方針對此詢價發送報價。
  3. 詢價方選擇執行最佳報價以生成交易。Blocktrade接收交易並進行結算。
  4. 詢價方和報價方收到交易執行確認。
  5. 交易詳情會發布在公開市場數據頻道（不包含交易方信息）。



**詢價方視角（OpenAPI）**

  1. 詢價方使用 [/v5/rfq/create-rfq](/docs/zh-TW/v5/rfq/trade/create-rfq) 創建詢價。詢價方可以通過 [/v5/market/instruments-info](/docs/zh-TW/v5/market/instrument) 查詢可詢價的產品信息，並通過 [/v5/rfq/config query](/docs/zh-TW/v5/rfq/trade/rfq-config) 選擇報價方信息。
  2. 詢價方可以隨時通過 [/v5/rfq/cancel-rfq](/docs/zh-TW/v5/rfq/trade/cancel-rfq) 取消有效的詢價。
  3. 詢價方可以通過 [/v5/rfq/accept-other-quote](/docs/zh-TW/v5/rfq/trade/accept-other-quote) 接受非 LP 的場外報價，以擴大報價來源。
  4. 報價方（若為詢價方選定的報價方之一）將在 [rfq.open.rfqs](/docs/zh-TW/v5/rfq/websocket/private/inquiry) 推送頻道接收到詢價信息，並可進行相應報價。
  5. 詢價方在 [rfq.open.quotes](/docs/zh-TW/v5/rfq/websocket/private/quote) 推送頻道接收到報價信息後，可以選擇最佳報價並通過 [/v5/rfq/execute-quote](/docs/zh-TW/v5/rfq/trade/execute-quote) 執行報價。
  6. 詢價方將在 [rfq.open.trades](/docs/zh-TW/v5/rfq/websocket/private/transaction) 和 [rfq.open.rfqs](/docs/zh-TW/v5/rfq/websocket/private/inquiry) 推送頻道收到交易成功執行的確認。
  7. 詢價方也會在 [rfq.open.public.trades](/docs/zh-TW/v5/rfq/websocket/public/public-transaction) 推送頻道收到此及其他大宗交易的確認。



**報價方視角（OpenAPI）**

  1. 當新的報價請求發出且報價方為選定的報價方之一時，報價方將在 [rfq.open.rfqs](/docs/zh-TW/v5/rfq/websocket/private/inquiry) 推送頻道收到此請求信息。
  2. 報價方創建報價並通過 [/v5/rfq/create-quote](/docs/zh-TW/v5/rfq/trade/create-quote) 發送。
  3. 報價方可以隨時通過 [/v5/rfq/cancel-quote](/docs/zh-TW/v5/rfq/trade/cancel-quote) 取消有效的報價。
  4. 詢價方選擇執行最佳報價。
  5. 報價方通過 [rfq.open.quotes](/docs/zh-TW/v5/rfq/websocket/private/quote) 推送頻道接收其報價的狀態更新。
  6. 報價方將在 [rfq.open.trades](/docs/zh-TW/v5/rfq/websocket/private/transaction) 和 [rfq.open.quotes](/docs/zh-TW/v5/rfq/websocket/private/quote) 推送頻道收到其報價成功執行的確認。
  7. 報價方也會在 [rfq.open.public.trades](/docs/zh-TW/v5/rfq/websocket/public/public-transaction) 推送頻道收到此交易及其他大宗交易的確認。