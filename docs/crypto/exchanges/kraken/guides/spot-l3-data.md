---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/guides/spot-l3-data
api_type: Market Data
updated_at: 2026-05-27 19:58:37.710865
---

# Spot Level 3 Market Data

Level 3 (L3) market data provides visibility of individual orders in the order book. This insight enables determination of queue priorities, resting times, fill probabilities, and many other analytics to help make better informed trading decisions.

## Market Data Levels Overview

Using the Kraken API channels as a reference:

Level| Description| Channel  
---|---|---  
**L1**|  Top of the book (best bid/offer) and recent trade data| `ticker`  
**L2**|  Individual price levels with aggregated order quantities at each level| `book`  
**L3**|  Individual orders in the book with order IDs and timestamps| `level3`  
  
## Order Visibility

The Level 3 feed shows orders **resting** in the visible order book. The book will never be crossed (i.e. no overlapping buy and sell orders). Therefore, this feed excludes:

  * In-flight orders
  * Unmatched market orders
  * Untriggered stop-loss and take-profit orders
  * Hidden quantity of `iceberg` orders

## Use Cases

Level 3 data enables advanced trading analytics:

  * **Queue Priority Analysis** : Understand your position in the order queue at each price level
  * **Resting Time Metrics** : Track how long orders have been in the book
  * **Fill Probability Estimation** : Estimate likelihood of order execution based on queue depth
  * **Market Microstructure Analysis** : Study order flow patterns and participant behavior
  * **Liquidity Analysis** : Assess true market depth beyond aggregated views

## REST API

The `/private/Level3` endpoint provides a snapshot of the Level 3 order book.

### Example Request
    
    
    {  
        "nonce": 1695828490,  
        "pair": "BTC/USD",  
        "depth": 10  
    }  
    

### Example Response
    
    
    {  
        "error": [],  
        "result": {  
            "pair": "BTC/USD",  
            "bids": [  
                {  
                    "price": "90509.00000",  
                    "qty": "0.04902300",  
                    "order_id": "ONLALL-67PF5-3CAQCL",  
                    "timestamp": 1765628335242269554  
                },  
                {  
                    "price": "90509.00000",  
                    "qty": "0.00010000",  
                    "order_id": "OZMMNG-E5B3K-4DCURI",  
                    "timestamp": 1765628346024196738  
                },  
                {  
                    "price": "90509.00000",  
                    "qty": "0.14670600",  
                    "order_id": "OGXZBL-RDLER-I45MMN",  
                    "timestamp": 1765628373027400852  
                },  
                {  
                    "price": "90506.80000",  
                    "qty": "1.65733300",  
                    "order_id": "O3YQDB-56ZLD-PYJJCD",  
                    "timestamp": 1765628373581704382  
                }  
            ],  
            "asks": [  
                {  
                    "price": "90509.10000",  
                    "qty": "0.00110900",  
                    "order_id": "OVT3GM-4OLSW-L4PPLG",  
                    "timestamp": 1765628340224297666  
                },  
                {  
                    "price": "90509.10000",  
                    "qty": "0.02771600",  
                    "order_id": "OBT7YM-NK4AM-3Z6CZR",  
                    "timestamp": 1765628349238326760  
                },  
                {  
                    "price": "90509.10000",  
                    "qty": "0.88510000",  
                    "order_id": "OPFXIF-2BHGV-3NJJTE",  
                    "timestamp": 1765628369865693932  
                },  
                {  
                    "price": "90509.50000",  
                    "qty": "0.34119400",  
                    "order_id": "OWMYX7-E63XJ-RHV64F",  
                    "timestamp": 1765628363316840374  
                }  
            ]  
        }  
    }  
    

## Websockets

For real-time Level 3 data, use the `level3` channel on the authenticated websockets connection. The channel provides:

  * Initial snapshot of the order book
  * Real-time updates as orders are added, modified, or removed
  * Sequence numbers for synchronization

### Building the Book

The `level3` channel synchronizes the initial snapshot and subsequent stream of updates in a similar mechanism to the `book` feed. Only a single subscription request is required to build the book—the channel handles snapshot and update synchronization automatically.

### Checksum Verification

Optional checksum verification provides an additional check that the client version of the book has been constructed correctly and is synchronized to the exchange.

The checksum can be verified in production on every update or periodically depending on requirements. Some clients generate the checksum in the development environment only when building their book models.

See the [Level3 Checksum Guide](/api/docs/guides/spot-ws-l3-v2) for detailed checksum calculation instructions.

## Performance Considerations

The latency differences between the `level3` and `book` feeds will be negligible compared to the transport time. However, here are some performance considerations:

  * **Direct Stream** : `level3` is a direct stream of order events from the matching engine. The `book` feed contains cumulative data which is aggregated extremely efficiently in the engine. Consider both channels as streams from the matching engine with a thin API layer.

  * **Payload Size** : `level3` data payload is larger than `book`. It takes more time to encode, transmit over the wire, and decode since it describes all orders in the book, not just cumulative quantity at a price level.

  * **Channel Load** : The channels are hosted on different market data stacks. `level3` uses an authenticated channel while `book` uses a public channel. Typically, the authenticated channel has less load than the public channel (but this may not always be the case).

  * **Checksum Computation** : `level3` checksum takes longer to compute than `book` checksum since it also verifies the sequence of orders in a price level.

  * **Latency Metrics** : The timestamps in both feeds enable clients to create latency metrics for detailed performance tracking.
* Market Data Levels Overview
  * Order Visibility
  * Use Cases
  * REST API
* Example Request
* Example Response
  * Websockets
* Building the Book
* Checksum Verification
  * Performance Considerations