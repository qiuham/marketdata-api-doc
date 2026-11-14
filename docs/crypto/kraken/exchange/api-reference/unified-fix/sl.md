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
source_url: 'https://docs.kraken.com/exchange/api-reference/unified-fix/sl'
updated_at: 2026-11-13
---

# Instrument List

> Instrument parameters and status response via FIX

FIX
session: market-data
35=y

This message provides the different parameters of each instrument that can be traded on Kraken as well as their status at the time of the request.

***

**header** *required*

35=`y`

**146 - NoRelatedSym** `integer`

Repeating Group describing all the Symbols available on Kraken exchange.

**repeating group**

**55 - Symbol** `string` *required*

Asset Pair listed on Kraken exchange.

**562 - minTradeVol** `float` *required*

Minimum order quantity increment on an asset pair.

**5010 - QtyPrecision** `float` *required*

Specifies the quantity decimal precision of the asset pair and currency.

**5011 - QtyMin** `float` *required*

Minimum order quantity allowed on asset pair.

**5012 - QtyMax** `float`

Maximum order quantity allowed on asset pair.

**5013 - MinimumCost** `float`

Minimum cost (price × qty) for new orders.

**2349 - PricePrecision** `float` *required*

Specifies the price decimal precision of the asset pair.

**5052 - MDPricePrecision** `integer` *required*

Specifies the price decimal precision used on market data feeds. May be greater than `2349 - PricePrecision` for rebased xStocks pairs, where market data prices are published at full internal precision. Currently applies to order book and trade market data entries;

**5022 - TickSize** `float` *required*

Specifies the price increment allowed on the asset pair.

**5032 - AssetPairStatus** `integer` *required*

**Possible values:**

* `0` : Hidden
* `1` : Online
* `2` : Maintenance
* `3` : CancelOnly
* `4` : PostOnly
* `5` : LimitOnly
* `6` : Delisted
* `7` : ReduceOnly

**320 - InstrumentReqID** `string` *required*

Unique request identifier.

**393 - TotNoRelatedSym** `integer`

Total number of securities. Only seen when fragmentation occurs.

**893 - LastFragment** `boolean`

Indicates whether this message is the last in a sequence of messages when the Security List was delivered in multiple SecurityList messages. Only seen when fragmentation occurs.

**322 - InstrumentResponseID** `string` *required*

Unique response identifier.

**560 - InstrumentRequestResult** `integer` *required*

**Possible values:**

* `0` : Valid request
* `1` : Invalid or unsupported request
* `2` : No Instruments found that match criteria
* `4` : Instrument data temporarily unavailable

**58 - Text** `string`

Full description for rejection.

**trailer** *required*

```text Instrument List Response (2 instruments) theme={null}
8=FIX.4.4|9=254|35=y|34=4|49=KRAKEN-MD|56=CLIENT|52=20260407-14:32:01.000|320=SLREQ1|322=SLRESP1|560=0|146=2|55=BTC/USD|562=0.00001|5010=5|5011=0.0001|5013=0.5|2349=1|5052=1|5022=0.1|5032=1|55=ETH/USD|562=0.0001|5010=4|5011=0.001|5013=0.5|2349=2|5052=2|5022=0.01|5032=1|10=227|
```
