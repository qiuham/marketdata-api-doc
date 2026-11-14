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
source_url: 'https://docs.kraken.com/home/sdks/go'
updated_at: 2026-11-13
---

# Go

> api-go — the official Go module for the Spot and Derivatives APIs

[api-go](https://github.com/krakenfx/api-go) is the official Go module for building integrations against the Spot and Derivatives APIs.

## Install

```bash theme={null} theme={null}
go get github.com/krakenfx/api-go/v2/...
```

## What it covers

* Spot and Derivatives REST (public and authenticated endpoints)
* Spot and Derivatives WebSocket (public data streams and private channels)
* Order operations: add, amend, cancel
* Real-time order book construction with CRC32 checksum validation
* Instrument and asset lookups, account data retrieval

## Example

```go theme={null} theme={null}
client := krakenapi.New(apiKey, apiSecret)
resp, err := client.AddOrder(krakenapi.AddOrderOptions{
    Pair:      "XBTUSD",
    Type:      "buy",
    OrderType: "limit",
    Price:     "60000",
    Volume:    "0.01",
})
```
