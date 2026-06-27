---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/futures-api/history/account-history
api_type: REST
updated_at: 2026-05-27 19:45:44.386651
---

# Account History

Account History provides account-specific data, including account logs ( history of all balance and position changes) and history for executions, orders, and triggers.

  * The `/account-log` endpoint provides a paginated JSON response, with access to all account log history specified by ranges of timestamp or ID.
  * The `/accountlogcsv` endpoint provides a CSV formatted response of 500,000 rows of most recent account logs. See also the websocket feed of account log snapshots
  * The `/executions` endpoint provides a paginated JSON response, with access to all private execution history specified by ranges of timestamp or ID
  * The `/orders` endpoint provides a paginated JSON response, with access to all private order history specified by ranges of timestamp or ID
  * The `/triggers` endpoint provides a paginated JSON response, with access to all private trigger history specified by ranges of timestamp or ID

## [📄️ Get execution eventsLists executions/trades for authenticated account.](/api/docs/futures-api/history/get-execution-events)## [📄️ Get order eventsLists order events for authenticated account.](/api/docs/futures-api/history/get-order-events)## [📄️ Get trigger eventsLists trigger events for authenticated account.](/api/docs/futures-api/history/get-trigger-events)## [📄️ Get position update eventsLists position events for authenticated account.](/api/docs/futures-api/history/get-position-events)## [📄️ Get account logLists account log entries, paged by timestamp or by ID.](/api/docs/futures-api/history/account-log)## [📄️ Account log (CSV)Lists recent account log entries in CSV format.](/api/docs/futures-api/history/account-log-csv)