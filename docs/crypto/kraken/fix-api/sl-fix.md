---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/fix-api/sl-fix
api_type: REST
updated_at: 2026-05-27 19:44:10.892317
---

# Instrument List

This message provides the different parameters of each instrument that can be traded on Kraken as well as their status at the time of the request.

  * FIX Specification

### MESSAGE BODY

**header** `` *required*

MsgType `y`

**146 - NoRelatedSym**

Repeating Group describing all the Symbols available on Kraken exchange. 

**55 - Symbol** string required

Asset Pair listed on Kraken exchange. 

**562 - minTradeVol** float required

Minimum order quantity increment on an asset pair. 

**5010 - QtyPrecision** float required

Specifies the quantity decimal precision of the asset pair and currency. 

**5011 - QtyMin** float required

Minimum order quantity allowed on asset pair. 

**5012 - QtyMax** float

Maximum order quantity allowed on asset pair. 

**5013 - MinimumCost** float

Minimum cost (price * qty) for new orders. 

**2349 - PricePrecision** float required

Specifies the price decimal precision of the asset pair. 

**5022 - TickSize** float required

Specifies the price increment allowed on the asset pair. 

**5032 - AssetPairStatus** integer required

**Possible values:**
  * `0` : Hidden
  * `1` : Online
  * `2` : Maintenance
  * `3` : CancelOnly
  * `4` : PostOnly
  * `5` : LimitOnly
  * `6` : Delisted
  * `7` : ReduceOnly

**320 - InstrumentReqID** string required

Unique request identifier. 

**393 - TotNoRelatedSym** Integer

Total number of securities. Only seen when fragmentation occurs. 

**893 - LastFragment** Boolean

Indicates whether this message is the last in a sequence of messages when the Security List was delivered in multiple SecurityList messages. Only seen when fragmentation occurs. 

**322 - InstrumentResponseID** string required

Unique response identifier. 

**560 - InstrumentRequestResult** integer required

**Possible values:**
  * `0` : Valid request
  * `1` : Invalid or unsupported request
  * `2` : No Instruments found that match criteria
  * `4` : Instrument data temporarily unavailable

**58 - Text** string

Full description for rejection. 

**trailer** `` *required*