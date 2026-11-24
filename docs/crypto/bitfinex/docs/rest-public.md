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
source_url: 'https://docs.bitfinex.com/docs/rest-public'
updated_at: 2026-11-24
---

# Public Endpoints

Public endpoints should use the domain:
<https://api-pub.bitfinex.com/>

The following code template can be used for GET requests to our public endpoints. Endpoint documentation pages also offer dynamic code examples in multiple languages and using multiple libraries.

```javascript
const axios = require('axios') // Axios library for Node

const baseUrl = "https://api-pub.bitfinex.com/v2/"; // Domain
const pathParams = "tickers" // Change based on relevant path params listed in the documentation
const queryParams = "symbols=fUSD,tBTCUSD" // Change based on relevant query params listed in the documentation

axios.get(`${baseUrl}/${pathParams}?${queryParams}`)
    .then(response => {
        console.log(response.data); // Logs response data
    }, error => {
        console.log(error); // Catches and logs any error
    })
```

## Public Endpoints

* GET [Platform Status](https://docs.bitfinex.com/reference/rest-public-platform-status)
* GET [Tickers](https://docs.bitfinex.com/reference/rest-public-tickers)
* GET [Ticker](https://docs.bitfinex.com/reference/rest-public-ticker)
* GET [Tickers History](https://docs.bitfinex.com/reference/rest-public-tickers-history)
* GET [Trades](https://docs.bitfinex.com/reference/rest-public-trades)
* GET [Book](https://docs.bitfinex.com/reference/rest-public-book)
* GET [Stats](https://docs.bitfinex.com/reference/rest-public-stats)
* GET [Candles](https://docs.bitfinex.com/reference/rest-public-candles)
* GET [Configs](https://docs.bitfinex.com/reference/rest-public-conf)
* GET [Derivatives Status](https://docs.bitfinex.com/reference/rest-public-derivatives-status)
* GET [Derivatives Status History](https://docs.bitfinex.com/reference/rest-public-derivatives-status-history)
* GET [Liquidations](https://docs.bitfinex.com/reference/rest-public-liquidations)
* GET [Leaderboards](https://docs.bitfinex.com/reference/rest-public-rankings)
* GET [Funding Stats](https://docs.bitfinex.com/reference/rest-public-funding-stats)
* GET [Virtual Asset Service Providers](https://docs.bitfinex.com/reference/virtual-asset-service-providers)

## Calculation Endpoints

* POST [Market Average Price](https://docs.bitfinex.com/reference/rest-public-market-average-price)
* POST [Foreign Exchange Rate](https://docs.bitfinex.com/reference/rest-public-foreign-exchange-rate)
