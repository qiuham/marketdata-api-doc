---
exchange: deribit
source_url: https://docs.deribit.com/articles/deribit-quickstart
api_type: Guide
updated_at: 2026-11-24 18:59:41.383881
---

# Quickstart Guide

> Set up the Deribit API environment, send your first authenticated JSON-RPC request, and use the key endpoints to place an order in minutes.

Deribit provides three different interfaces to access the API:

* **JSON-RPC over WebSocket** (recommended) - Real-time, bidirectional communication
* **JSON-RPC over HTTP** - Simple REST-like interface
* **FIX API** - Financial Information eXchange protocol for institutional trading

> [!NOTE]
>
> All examples in this documentation use the **test environment** (`test.deribit.com`). To use production, change the URLs to `www.deribit.com`. Test and production environments are separate and require different accounts and API keys.

**1. Get API Credentials**

<ol>
  <li>Log in to your Deribit account at [www.deribit.com](https://www.deribit.com) or [test.deribit.com](https://test.deribit.com) for testing</li>
  <li>Navigate to **Account** → **API**</li>
  <li>Create a new API key with appropriate permissions</li>
  <li>Save your **Client ID** and **Client Secret** securely</li>
</ol>

> [!WARNING]
>
> Never share your API credentials or commit them to version control. The client secret is only shown once and cannot be retrieved later.

> [card] [Creating API Keys](https://docs.deribit.com/articles/creating-api-key.md)
>
> Step-by-step guide to creating API keys

> [card] [Asymmetric API Keys](https://docs.deribit.com/articles/asymmetric-api-keys.md)
>
> Using Ed25519 or RSA key pairs for enhanced security

**2. Choose Your Interface**

**3. Authenticate**

For private methods, you need to authenticate. Deribit supports multiple authentication methods:

<ul>
  <li>**Client Credentials** - Standard OAuth 2.0 flow</li>
  <li>**Client Signature** - User generated signature</li>
  <li>**Refresh Token** - Token renewal</li>
</ul>

> [tab] HTTP Authentication
>
> ```bash theme={null}
> # Get access token using Client Credentials
> curl -X GET "https://test.deribit.com/api/v2/public/auth" \
>   -d "grant_type=client_credentials" \
>   -d "client_id=YOUR_CLIENT_ID" \
>   -d "client_secret=YOUR_CLIENT_SECRET"
> ```
>
> Response:
>
> ```json theme={null}
> {
>   "jsonrpc": "2.0",
>   "result": {
>     "access_token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
>     "expires_in": 31536000,
>     "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
>     "scope": "account:read trade:read",
>     "token_type": "bearer"
>   }
> }
> ```

> [tab] WebSocket Authentication
>
> ```javascript theme={null}
> const WebSocket = require('ws');
> const ws = new WebSocket('wss://test.deribit.com/ws/api/v2');
>
> ws.on('open', function open() {
>   // Authenticate
>   ws.send(JSON.stringify({
>     "jsonrpc": "2.0",
>     "method": "public/auth",
>     "params": {
>       "grant_type": "client_credentials",
>       "client_id": "YOUR_CLIENT_ID",
>       "client_secret": "YOUR_CLIENT_SECRET"
>     },
>     "id": 1
>   }));
> });
>
> ws.on('message', function incoming(data) {
>   const response = JSON.parse(data);
>   if (response.result && response.result.access_token) {
>     console.log('Authenticated! Access token:', response.result.access_token);
>     // Now you can make private method calls
>   }
> });
> ```

> [card] [Access Scopes](https://docs.deribit.com/articles/access-scope.md)
>
> Learn more about API permissions and access scopes

**4. Make Your First Requests**

> [tab] Public Data (No Auth)
>
> **Get Market Data**
>
> ```bash theme={null}
> # Get all BTC futures
> curl -X GET "https://test.deribit.com/api/v2/public/get_instruments?currency=BTC&kind=future"
>
> # Get ticker for BTC-PERPETUAL
> curl -X GET "https://test.deribit.com/api/v2/public/ticker?instrument_name=BTC-PERPETUAL"
>
> # Get order book
> curl -X GET "https://test.deribit.com/api/v2/public/get_order_book?instrument_name=BTC-PERPETUAL&depth=5"
> ```

> [tab] Private Data (Auth Required)
>
> **Get Account Information**
>
> ```bash theme={null}
> # Get account summary
> curl -X GET "https://test.deribit.com/api/v2/private/get_account_summary?currency=BTC" \
>   -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
>
> # Get open orders
> curl -X GET "https://test.deribit.com/api/v2/private/get_open_orders?currency=BTC" \
>   -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
> ```

> [tab] WebSocket Subscriptions
>
> **Subscribe to Real-Time Data**
>
> ```javascript theme={null}
> const WebSocket = require('ws');
> const ws = new WebSocket('wss://test.deribit.com/ws/api/v2');
>
> ws.on('open', function open() {
>   // Subscribe to multiple channels
>   ws.send(JSON.stringify({
>     "jsonrpc": "2.0",
>     "method": "public/subscribe",
>     "params": {
>       "channels": [
>         "book.BTC-PERPETUAL.100ms",
>         "ticker.BTC-PERPETUAL.100ms",
>         "trades.BTC-PERPETUAL.100ms"
>       ]
>     },
>     "id": 1
>   }));
> });
>
> ws.on('message', function incoming(data) {
>   const message = JSON.parse(data);
>   if (message.method === 'subscription') {
>     console.log('Update:', message.params.channel, message.params.data);
>   }
> });
> ```

**5. Place a Test Order (Testnet Only)**

> [!WARNING]
>
> Only use test.deribit.com for testing. Never test with real funds on production.

> [tab] HTTP
>
> ```bash theme={null}
> # Place a limit buy order (testnet)
> curl -X GET "https://test.deribit.com/api/v2/private/buy" \
>   -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
>   -d "instrument_name=BTC-PERPETUAL" \
>   -d "amount=10" \
>   -d "type=limit" \
>   -d "price=50000"
> ```

> [tab] WebSocket
>
> ```javascript theme={null}
> ws.send(JSON.stringify({
>   "jsonrpc": "2.0",
>   "method": "private/buy",
>   "params": {
>     "instrument_name": "BTC-PERPETUAL",
>     "amount": 10,
>     "type": "limit",
>     "price": 50000,
>     "access_token": "YOUR_ACCESS_TOKEN"
>   },
>   "id": 2
> }));
> ```


## Related topics

- [Welcome to Deribit API](https://docs.deribit.com/index.md)
- [Multicast Subscription Guide](https://docs.deribit.com/starbase/multicast-subscription-guide.md)
- [Starbase Connectivity Quickstart](https://docs.deribit.com/starbase/quickstart.md)
- [Liquidity Support Program (LSP) API Guide](https://docs.deribit.com/articles/lsp-api-guide.md)
- [Managing Subaccounts](https://docs.deribit.com/articles/managing-subaccounts-api.md)