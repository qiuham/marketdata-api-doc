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
source_url: 'https://docs.kraken.com/institutional/api-reference/prime-fix/sl'
updated_at: 2026-11-13
---

# Security List

> FIX response message returning the list of securities matching a Security List Request.

The Security List message is used to return a list of securities that matches the criteria specified in the Security List Request.

> [tab] FIX Specification
>
> **header** *required*
>
> MsgType `y`
>
> **320 - SecurityReqID** `string` *required*
>
> Unique ID to identify this request.
>
> **322 - SecurityResponseID** `string` *required*
>
> Identifier for the SecurityList message.
>
> **560 - SecurityRequestResult** `integer` *required*
>
> Result of the Security Request Identified by the SecurityReqID.
>
> <ul>
>   \*\*Possible values: \*\*
>   <li>`0` : Valid Request</li>
>   <li>`1` : Invalid or Unsupported Request</li>
>   <li>`2` : No instruments found that match the selection criteria</li>
>   <li>`3` : Not authorized to retrieve instrument data</li>
>   <li>`4` : Instrument data temporarily unavailable</li>
>   <li>`5` : Request for instrument data not supported</li>
> </ul>
>
> **393 - TotalNoRelatedSym** `integer`
>
> Used to indicate the total number of securities being returned for this request. Used in the event that message fragmentation is required.
>
> **893 - LastFragment** `boolean`
>
> Indicates whether this is the last fragment in a sequence of message fragments. Only required where message has been fragmented.
>
> **146 - NoRelatedSym** `integer`
>
> Number of related symbols. Component Block \<Instrument> required if 560=0.
>
> **55 - Symbol** `string` *required*
>
> Common "human understood" representation of the security.
>
> **48 - SecurityID** `string` *required*
>
> Internal Customer ID for Security - for information only.
>
> **561 - RoundLot** `integer` *required*
>
> The trading lot size of a security.
>
> **562 - MinTradeVol** `float` *required*
>
> Minimum Trading Volume for a security.
>
> **969 - MinPriceIncrement** `float` *required*
>
> The smallest difference between quoted prices for this instrument.
>
> **1140 - MaxTradeVol** `float` *required*
>
> Maximum Size for an order on this security.
>
> **trailer** *required*

> [tab] Example
>
> ```text theme={null}
> 8=FIX.4.4|9=243|35=y|34=3|49={{ Customer }}|52=20220930-13:28:16.514|56=CUSTOMER|146=2|55=ETH-USD|48=2|561=0.00000001|562=0.00000001|969=0.00001|1140=1000.00|55=BTC-USD|48=24|561=0.00000001|562=0|969=0.01|1140=1000.00|320=id-220929160342682-27|322=1BQM22QR01G00|560=0|10=153|
> ```
