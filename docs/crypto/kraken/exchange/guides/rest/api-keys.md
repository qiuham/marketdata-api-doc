---
api_type: reference
source_type: llms_txt
version: ''
scope: crypto
asset_class: digital_asset
domain: exchanges
provider: kraken
provider_name: Kraken
product: api
product_id: kraken
source_url: 'https://docs.kraken.com/exchange/guides/rest/api-keys'
updated_at: 2026-11-13
---

# API key permissions

> Which API key permissions to enable for each use case

When creating an API key at [Settings → API](https://www.kraken.com/u/security/api), Kraken asks you to select permissions. Granting too few causes `EGeneral:Permission denied` errors. Granting too many exposes you to unnecessary risk if the key is compromised.

## Permissions by use case

| Use case | Required permissions |
| :- | :- |
| Market data only (public endpoints) | None — public endpoints require no key |
| Read account balances | Query Funds |
| Read order history and positions | Query Open Orders & Trades, Query Closed Orders & Trades |
| Algorithmic spot trading | Query Funds, Query Open Orders & Trades, Create & Modify Orders, Cancel/Close Orders |
| Market making | Query Funds, Query Open Orders & Trades, Create & Modify Orders, Cancel/Close Orders, **Get WebSocket Token** |
| Funding operations (deposits/withdrawals) | Query Funds, Deposit Funds, Withdraw Funds |
| Full institutional access | All of the above |
| Read-only monitoring dashboard | Query Funds, Query Open Orders & Trades, Query Closed Orders & Trades |
| Sub-account management | Query Funds, Create & Modify Orders, Cancel/Close Orders |
| Affiliate daily activity | Query affiliate participants |

## Permission descriptions

| Permission | What it enables |
| :- | :- |
| Query Funds | `Balance`, `BalanceEx`, `TradeBalance` |
| Query Open Orders & Trades | `OpenOrders`, `QueryOrders`, `TradesHistory`, `QueryTrades`, `OpenPositions` |
| Query Closed Orders & Trades | `ClosedOrders`, `QueryOrders`, `TradesHistory`, `QueryTrades` |
| Create & Modify Orders | `AddOrder`, `EditOrder`, `AmendOrder`, `AddOrderBatch` |
| Cancel/Close Orders | `CancelOrder`, `CancelAll`, `CancelAllOrdersAfter`, `CancelOrderBatch` |
| Query Ledger Entries | `Ledgers`, `QueryLedgers` |
| Export Data | `AddExport`, `ExportStatus`, `RetrieveExport`, `RemoveExport` |
| Access WebSocket API | `GetWebSocketsToken` — required for authenticated WebSocket subscriptions |
| Deposit Funds | `DepositMethods`, `DepositAddresses`, `DepositStatus` |
| Withdraw Funds | `WithdrawMethods`, `WithdrawAddresses`, `WithdrawInfo`, `Withdraw`, `WithdrawStatus`, `WithdrawCancel` |
| Earn | `Earn/Strategies`, `Earn/Allocations`, `Earn/Allocate`, `Earn/Deallocate` |
| Query affiliate participants | `GetDailyActivity` |

## Security best practices

**Use IP whitelisting.** Lock your API key to the IP addresses your trading system runs from. This single measure prevents almost all key misuse even if the key is leaked.

**Use separate keys per purpose.** Give your market data service a read-only key. Give your order management system a trading key. Give your accounting system a ledger query key. If one is compromised, the blast radius is contained.

**Never embed keys in source code.** Use environment variables or a secrets manager. Rotate keys periodically.

**Set the minimum permissions required.** A key used only for placing orders does not need `Withdraw Funds`.

> [!WARNING]
>
> Withdrawal permissions should only be enabled on keys that genuinely need to move funds, and those keys should have strict IP whitelisting. A compromised key with withdrawal permissions is a direct financial risk.

## WebSocket authentication

WebSocket private channels (executions, balances, open orders) require a short-lived token rather than your API key directly. Obtain it via the REST endpoint before opening your WebSocket connection:

```bash theme={null}
POST /0/private/GetWebSocketsToken
```

The token is valid for 15 minutes. Your API key must have the **Access WebSocket API** permission enabled.

```json theme={null}
{
  "error": [],
  "result": {
    "token": "WW91ciBhdXRoZW50aWNhdGlvbiB0b2tlbiBnb2VzIGhlcmUu",
    "expires": 900
  }
}
```

Use this token in your WebSocket subscription messages — never send your API key directly over WebSocket.

## Related guides

> [card] [Authentication](https://docs.kraken.com/exchange/guides/rest/authentication.md)
>
> HMAC-SHA512 signature generation and nonce management

> [card] [Sub-accounts](https://docs.kraken.com/exchange/guides/general/subaccounts.md)
>
> Issue independent API keys per sub-account for strategy isolation

> [card] [WebSocket authentication](https://docs.kraken.com/exchange/guides/websockets/authentication.md)
>
> How to use your WebSocket token in subscription messages
