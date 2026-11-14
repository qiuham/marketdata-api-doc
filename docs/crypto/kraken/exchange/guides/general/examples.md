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
source_url: 'https://docs.kraken.com/exchange/guides/general/examples'
updated_at: 2026-11-13
---

# Spot Example Clients

> Community and official API client libraries for Spot REST and WebSocket in Python, Go, Java, and more

## Official and community clients

In order to achieve maximum performance, security and flexibility for your particular needs, Kraken strongly encourage the implementation of this API with your own code, and to minimise reliance on third party software.

That being said, in order to aid with rapid development and prototyping, we're in the process of producing 'official' API clients in Python and Golang that will be actively maintained, coincident with the release of newer versions of both our Websockets and REST APIs. In the meantime, our Client Engagement team has compiled a number of [code snippets, examples and Postman collections](https://support.kraken.com/hc/en-us/sections/360003946512-Example-API-Code) that many find useful.

### Third Party Software

The following are some third party API client code libraries that may be useful when writing your own API client.

| Language | Link |
| - | :- |
| C++ | [https://github.com/voidloop/krakenapi](https://github.com/voidloop/krakenapi) |
| Golang | [https://github.com/Beldur/kraken-go-api-client](https://github.com/Beldur/kraken-go-api-client) |
| Python 3 | [https://github.com/veox/python3-krakenex](https://github.com/veox/python3-krakenex) |
| Python 3 | [https://github.com/btschwertfeger/python-kraken-sdk](https://github.com/btschwertfeger/python-kraken-sdk) |
| Julia | [https://github.com/btschwertfeger/KrakenEx.jl](https://github.com/btschwertfeger/KrakenEx.jl) |

The following is some third party sample code that can be referenced when writing your own API client.

| Language | Type of Example | Link |
| - | - | :- |
| Python 3 | WebSocket order book feed | [https://github.com/voidloop/krakenapi](https://github.com/voidloop/krakenapi) |
| Golang | WebSocket client | [https://github.com/Beldur/kraken-go-api-client](https://github.com/Beldur/kraken-go-api-client) |

Please keep in mind that neither Payward nor the third party authors are responsible for losses due to bugs or improper use of the APIs.

Payward has performed an initial review of the safety of the third party code before listing them, but cannot vouch for any changes added since then, or for those that may be stale.

Please [contact our API support team](https://support.kraken.com/hc/en-us/forms/360000104043) if you have any concerns/questions.
