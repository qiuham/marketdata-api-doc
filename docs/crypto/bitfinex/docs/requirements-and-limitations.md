---
api_type: reference
source_type: llms_txt
version: ''
scope: crypto
asset_class: digital_asset
domain: exchanges
provider: bitfinex
provider_name: Bitfinex
product: api
product_id: bitfinex
source_url: 'https://docs.bitfinex.com/docs/requirements-and-limitations'
updated_at: 2026-11-21
---

# Requirements and Limitations

Depending on the intended use, the Bitfinex API is subject to a number of requirements and limitations that will be outlined here.

## Requirements

First and foremost, any use of our API needs to be in compliance with our [API Terms of Service](https://www.bitfinex.com/legal/general/api-terms/).

### Public API

Access to our public API only requires a device with an active internet connection. Access to our public API does not require a Bitfinex account.

REST public endpoints can be called by running code, but can also be retrieved in the browser using a cURL. For example, the following cURL retrieves the most recent data from the BTC/USD ticker:

<https://api-pub.bitfinex.com/v2/ticker/tBTCUSD>

To learn more about building a cURL, please look [here](https://docs.bitfinex.com/docs/rest-reading-the-api-documentation#query-parameters-in-the-curl).

To retrieve data from Public Websocket channels, you will need to run some code. For both REST and WebSocket, example code can be found in our API documentation. The documentation will also include information to interpret the data that is returned to you. As an alternative, you can also use one of our Open Source Libraries or custom code to retrieve data from our API.

### Authenticated API

Our Authenticated API allows you to connect to and use your Bitfinex account on our platform. The Authenticated API allows you to retrieve account data and also enables you to place, adjust, or cancel any trading orders or funding offers. To do this, a Bitfinex Account and a set of Bitfinex API keys are required.

To create an API key, log in to your account and navigate to the [API key management page](https://setting.bitfinex.com/api#new-key). On this page, you can create new keys and revoke existing ones.

To create a key, press the "Create Key" button and select the desired permissions. If you only want to use your keys to view account data, selecting the "read" permissions will suffice. If you also wish to use your API key to trade on your account or to request deposits and withdrawals, you will also need to check the appropriate "write" permissions. After selecting the desired permissions, click on "Generate API Key" to generate your key. You may be prompted to enter a 2FA code if this feature is enabled on your account. Once this is done, an email will be sent to you with a link to confirm your API key creation. Click the link in the email to confirm and you will be directed to a page where your API key and API key secret will be shown. You will need both keys to connect to our authenticated APIs. This is the only time you will be able to view these keys in full, but you can always generate new keys as long as you have access to your Bitfinex and email accounts.

Instructions on how to authenticate your connection using these keys can be found on these pages:\
[Authenticated Endpoints (REST)](https://docs.bitfinex.com/docs/rest-auth)\
[Authenticated Channels (WS)](https://docs.bitfinex.com/docs/ws-auth)

> 🚧 Important
>
> Should you believe one of your API keys to be compromised, you should always immediately revoke it. Depending on the permission settings, compromised keys can provide full access to your account and can result in a loss of funds.

### Nonce and Multiple Connections

Authenticated requests through the Bitfinex API require a nonce. The nonce is used for your security and is used to guard against replay attacks. The server will reject any request that comes with an incorrect nonce.

The only requirement for the nonce is that it needs to be strictly increasing. Nonce generation is often achieved by using the current UNIX timestamp. Examples of this can be found in the authentication example code which have been linked to earlier in this article.

> 🚧 Nonce MAX\_SAFE\_INTEGER
>
> The nonce provided must be strictly increasing but should not exceed the MAX\_SAFE\_INTEGER constant value of 9007199254740991.

> 📘 Multiple Connections
>
> If you wish to use multiple HTTP or WebSocket connections to send authenticated requests, you will need to generate separate API keys for each client so as to avoid requests being rejected on account of an incorrect nonce. Each API key has its own nonce requirements, so no errors will occur if you send the same nonce using different keys.

## Limitations

Use of the Bitfinex API is subject to certain limitations to protect our servers against DDOS attacks. REST and WebSocket have different limitations.

### REST Rate Limits

Bitfinex API access is rate limited. For the REST API, an IP address can be rate limited if it has sent too many requests per minute. The current rate limit is between 10 and 90 requests per minute, depending on the specific REST API endpoint (i.e. /ticker). If an IP address is rate limited, the IP is blocked for 60 seconds and cannot make any requests during that time. If your IP address is rate limited, the API will return the JSON response \{“error”: “ERR\_RATE\_LIMIT”}”.

### WebSocket Rate Limits

For Websocket, you cannot open more than 5 (authenticated) connections per 15 seconds using the wss\://api.bitfinex.com domain and no more than 20 connections per minute using the wss\://api-pub.bitfinex.com/ domain. Aside from that, you can subscribe to up to 25 channels at the same time per connection. If your WS connection is dropped, please make sure to not make multiple reconnects in short succession. If you exceed the stated limitations, you will be rate-limited for 15 seconds on api.bitfinex.com and 60 seconds on api-pub.bitfinex.com.
