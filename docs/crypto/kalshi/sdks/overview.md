---
api_type: reference
source_type: llms_txt
version: ''
scope: crypto
asset_class: prediction_market
domain: exchanges
provider: kalshi
provider_name: Kalshi
product: api
product_id: kalshi
source_url: 'https://docs.kalshi.com/sdks/overview'
updated_at: 2026-11-20
---

# Kalshi SDKs

> Official Python and TypeScript SDKs for the Kalshi API

Kalshi publishes Python and TypeScript SDKs to help you get started quickly.

> [!WARNING]
>
> SDKs are updated periodically and may lag the API. Active traders should treat the REST [OpenAPI specification](https://docs.kalshi.com/openapi.yaml) and WebSocket [AsyncAPI specification](https://docs.kalshi.com/asyncapi.yaml) as the source of truth. For production, we recommend generating your own client from those specs — or integrating directly — for full control over your implementation.

## Packages

> [card] [Python (sync)](https://pypi.org/project/kalshi_python_sync/)
>
> `pip install kalshi_python_sync`

> [card] [Python (async)](https://pypi.org/project/kalshi_python_async/)
>
> `pip install kalshi_python_async`

> [card] [TypeScript](https://www.npmjs.com/package/kalshi-typescript)
>
> `npm install kalshi-typescript`

> [!NOTE]
>
> The old `kalshi-python` package is deprecated — use `kalshi_python_sync` or `kalshi_python_async`.

SDK releases track the [OpenAPI specification](https://docs.kalshi.com/openapi.yaml) and are generally published Tuesday–Wednesday each week, ahead of the corresponding API changes; check the package pages and the [API Changelog](https://docs.kalshi.com/changelog.md) for updates. All SDKs authenticate with an API key and signed requests: RSA keys work with every SDK version,
Ed25519 keys need SDK 3.31.0 or later — see [API Keys](https://docs.kalshi.com/getting_started/api_keys.md) for setup.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
