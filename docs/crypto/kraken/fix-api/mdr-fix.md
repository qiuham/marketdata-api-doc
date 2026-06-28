---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/fix-api/mdr-fix
api_type: Market Data
updated_at: 2026-05-27 19:42:45.098014
---

# Market Data Request

The MarketDataRequest message is used by the client system to request a market data stream for the order book and/or trades.

In response, the FIX Server will begin sending out a [MarketDataSnapshot](/api/docs/fix-api/mdsfr-fix) if it is a valid request. Otherwise, the FIX Server will send out a [MarketDataRequestReject](/api/docs/fix-api/mdrr-fix) with the Text tag containing the reason for the rejection.

Each subscription request needs to have a unique identifier set via tag MDReqID, which will be used to refer back to the client. It is also used to unsubscribe from market data.

Market data updates are sent to clients using a [MarketDataSnapshotFullRefresh](/api/docs/fix-api/mdsfr-fix) message and then [MarketDataIncrementalRefresh](/api/docs/fix-api/mdir-fix) message. A full empty market data snapshot may be sent in case no more prices are received. These prices will stream continuously until the client requests to unsubscribe using a MarketDataRequest with the SubscriptionRequestType set to Unsubscribe (263=2).

For the OrderBook, the client can request Level 2 or Level 3 depending on the value of Tag

In case of a disconnection, the subscription will be cancelled. The Client will need to subscribe again after the reconnection.

  * FIX Specification
  * Spot Example
  * Futures L2 Example
  * Futures L3 Example

### MESSAGE BODY

**header** `` *required*

MsgType `V`

**262 - MDReqID** string required

Unique request identifier. 

**263 - SubscriptionRequestType** integer required

**Possible values:**
  * `1` : Snapshot + Updates
  * `2` : Disable previous snapshot + Update request

**264 - MarketDepth** integer required

**Possible values:**
  * `0` : Full depth of book (limited to 1000 for Level 2)
  * `1` : Top of Book
  * `10`, `25`, `100`, `500` and `1000`

**265 - MDUpdateType** integer

**Possible values:**
  * `1`=Incremental Refresh.

Only incremental Refresh is supported

**266 - AggregatedBook** boolean

Specify if the request is for Level 2 or Level 3.

**Possible values:**
  * `Y` : one book entry per side per price. Aka Level 2.
  * `N` : Multiple entries per side per price allowed. Aka Level 3. Only Available for Derivatives
**Default value:`Y`**

Level 3 is only available for MDEntryType BID and OFFER. Request will get rejected if used with MDEntryType TRADE.

**267 - NoMDEntryTypes** integer required

Repeating Group. Number of MDEntryTypes.

**269 - MDEntryType** integer required

Client can subscribe to bid/offer and/or trades. It s not possible to subscribe to only bid or only offer.

**Possible values:**
  * `0` : Bid
  * `1` : Offer
  * `2` : Trade 

**146 - NoRelatedSym** integer required

Number of Pair that are going to be Subscribe: 

**55 - Symbol** string required

Asset Pair listed on the exchange. 

**trailer** `` *required*
    
    
    8=FIX.4.4|9=123|35=V|34=3|49=MYCOMPID|52=20230707-13:42:21.000|56=KRAKEN-MD|146=1|55=BTC/USD|262=1|263=1|264=0|265=1|267=3|269=0|269=1|269=2|10=019|  
    
    
    
    8=FIX.4.4|9=133|35=V|34=2|49=damien_DRV|52=20250303-17:59:37.042|56=KRAKEN-DRV-MD|146=1|55=PF_ETHUSD|262=1|263=1|264=0|265=1|267=3|269=0|269=1|269=2|10=088|  
    
    
    
    8=FIX.4.4|9=133|35=V|34=2|49=damien_DRV|52=20250303-18:00:21.589|56=KRAKEN-DRV-MD|146=1|55=PF_ETHUSD|262=1|263=1|264=0|265=1|266=N|267=2|269=0|269=1|10=108|