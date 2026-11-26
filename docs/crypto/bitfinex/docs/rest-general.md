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
source_url: 'https://docs.bitfinex.com/docs/rest-general'
updated_at: 2026-11-26
---

# General

### URL

Public endpoints should use the domain:\
[https://api-pub.bitfinex.com\
](https://api-pub.bitfinex.com)\
Authenticated endpoints should use the domain:\
<https://api.bitfinex.com>

### Parameters:

To build a request, use the following structure to append parameters:

```html
Public:

https://api-pub.bitfinex.com/v2/<endpoint>?parameter=value&parameter=value&....

Authenticated:

https://api.bitfinex.com/v2/<endpoint>?parameter=value&parameter=value&....
```

Please note that Path Parameters are appended after the endpoint. In the documentation, Path Parameters will be listed below the example code and will also be shown in the URL above the example code. The structure is as follows:

```html
Public:

https://api-pub.bitfinex.com/v2/<endpoint>/<pathParam>?queryParam=value&queryParam=value&....

Authenticated:

https://api.bitfinex.com/v2/<endpoint>/<pathParam>?queryParam=value&queryParam=value&....
```

When adding timestamp parameters the value needs to be expressed in UTC and in milliseconds.

For a more detailed overview of the structure of the documentation, please look the [Reading the Documentation (REST)](https://docs.bitfinex.com/docs/rest-reading-the-api-documentation) page.\
For further information regarding authentication, please look to the [Authenticated Endpoints](https://docs.bitfinex.com/docs/rest-auth) page.

### Supported Pairs

All pairs available in the platform are supported. A symbol can be a trading pair or a margin currency. All symbols are in uppercase (i.e. btcusd is invalid, BTCUSD is valid).

Trading pairs are prepended by a “t” before the pair (e.g. tBTCUSD, tETHUSD, ...).\
Margin currencies are prepended by an “f” before the currency (e.g. fUSD, fBTC, …).

Lists of available currencies and pairs can be retrieved through the [Configs endpoint](https://docs.bitfinex.com/reference#rest-public-conf).

For a list of all currencies on the platform, look to:\
<https://api-pub.bitfinex.com/v2/conf/pub:list:currency>\
For a list of all trading pairs on the platform, look to:\
<https://api-pub.bitfinex.com/v2/conf/pub:list:pair:exchange>\
For a list of all margin trading pairs on the platform, look to:\
<https://api-pub.bitfinex.com/v2/conf/pub:list:pair:margin>

> 🚧 Rate Limits
>
> In order to offer the best service possible, there is a rate limit to the number of REST requests that can be made in the span of a minute. Our rate limit policy varies per endpoint and lies in the range of 10 to 90 requests per minute. For more information regarding the requirements and limitations of our API, please look to our [Requirements and Limitations](https://docs.bitfinex.com/docs/requirements-and-limitations) page.

> 🚧 Maintenance Error
>
> When in maintenance, a few API endpoints (eg. books) will return a maintenance error to prevent you from using potentially inconsistent data. The error will appear as follows:\
> \["error", 20060, "maintenance"]
