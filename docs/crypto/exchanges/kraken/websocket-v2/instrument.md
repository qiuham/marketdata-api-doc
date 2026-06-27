---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/websocket-v2/instrument
api_type: WebSocket
updated_at: 2026-05-27 20:12:23.873767
---

# Instruments

CHANNEL
**Endpoint:** `wss://ws.kraken.com/v2`
    instrument

The `instrument` channel provides a stream of reference data of all active assets and tradeable pairs.

It provides the symbol identifiers, precisions, trading parameters and rules.

## Subscribe Request

  * Subscribe Schema
  * Example: Subscribe
  * Subscribe Ack Schema
  * Example: Subscribe Ack

### MESSAGE BODY

**method** `string` *required*

**Value:** `subscribe`

**params** `object`

    ↳ **channel** `string` *required*

**Value:** `instrument`

    ↳ **execution_venue** `string`

**Possible values:**[`international`, `bitnomial-exchange`] 

**Default value:**`international`

The execution venue for the instrument channel. If not included, defaults to `international`.

    ↳ **include_tokenized_assets** `boolean`

**Possible values:**[`false`, `true`] 

**Default value:**`false`

If `true`, include xStocks in the response, otherwise include crypto spot pairs only.

    ↳ **snapshot** `boolean`

**Possible values:**[`true`, ` false`] 

**Default value:**`true`

Request a snapshot after subscribing.

**req_id** `integer`

Optional client originated request identifier sent as acknowledgment in the response.
    
    
    {  
        "method": "subscribe",  
        "params": {  
            "channel": "instrument"  
        },  
        "req_id": 79  
    }  
    

### MESSAGE BODY

**method** `string` *required*

**Value:** `subscribe`

**result** `object`

    ↳ **channel** `string` *required*

**Value:** `instrument`

    ↳ **snapshot** `boolean`

**Possible values:**[`true`, ` false`] 

Indicates if a snapshot is requested.

    ↳ **warnings** `array of strings`

An advisory message, highlighting deprecated fields or upcoming changes to the channel.

**success** `boolean`

**Possible values:**[`true`, ` false`] 

Indicates if the request was successfully processed by the engine.

**error** `string` *conditional*

**Condition:** If success is false. 

Error message.

**time_in** `string`

**Format:** RFC3339

**Example:** 2022-12-25T09:30:59.123456Z

The timestamp when the subscription was received on the wire, just prior to parsing data.

**time_out** `string`

**Format:** RFC3339

**Example:** 2022-12-25T09:30:59.123456Z

The timestamp when the acknowledgement was sent on the wire, just prior to transmitting data.

**req_id** `integer`

Optional client originated request identifier sent as acknowledgment in the response.
    
    
    {  
        "method": "subscribe",  
        "req_id": 79,  
        "result": {  
            "channel": "instrument",  
            "snapshot": true,  
            "warnings": [  
                "tick_size is deprecated, use price_increment"  
            ]  
        },  
        "success": true,  
        "time_in": "2023-09-26T16:49:20.962586Z",  
        "time_out": "2023-09-26T16:49:20.962630Z"  
    }  
    

## Snapshot / Update Responses

The snapshot and update responses share the same schema.

  * Snapshot / Update Schema
  * Example: Snapshot
  * Example: Update

### MESSAGE BODY

**channel** `string`

**Value:** `instrument`

**type** `string`

**Possible values:**[`snapshot`, ` update`] 

**data** `object`

    ↳ **assets** `array [`

A list of assets.

**[many] asset** object

        ↳ **borrowable** `boolean`

**Possible values:**[`true`, ` false`] 

Flag if asset is borrowable.

        ↳ **collateral_value** `float`

Valuation as margin collateral (if applicable).

        ↳ **id** `string`

Asset identifier.

        ↳ **margin_rate** `float`

Interest rate to borrow the asset.

        ↳ **precision** `integer`

Maximum precision for asset ledger, balances.

        ↳ **precision_display** `integer`

Recommended display precision.

        ↳ **multiplier** `float`

Multiplier of the tokenised asset. Fixed conversion rate of the token .

        ↳ **status** `string`

**Possible values:**[`depositonly`, ` disabled`, ` enabled`, ` fundingtemporarilydisabled`, ` withdrawalonly`, ` workinprogress`] 

Status of asset.

]

        ↳ **pairs** `array [`

A list of pairs.

**[many] pair** object

            ↳ **base** `string`

Asset identifier of the base currency.

            ↳ **quote** `string`

Asset identifier of the quote currency.

            ↳ **cost_min** `string`

Minimum cost (price * qty) for new orders.

            ↳ **cost_precision** `integer`

Maximum precision used for cost prices.

            ↳ **has_index** `boolean`

Whether the pair has an index available for example stop-loss triggers.

            ↳ **margin_initial** `float` *conditional*

**Condition:** On marginable pairs only 

Initial margin requirement (in percent).

            ↳ **marginable** `boolean`

**Possible values:**[`true`, ` false`] 

Whether the pair can be traded on margin.

            ↳ **position_limit_long** `integer` *conditional*

**Condition:** On marginable pairs only 

Limit for long positions.

            ↳ **position_limit_short** `integer` *conditional*

**Condition:** On marginable pairs only 

Limit for short positions.

            ↳ **price_increment** `float`

Minimum price increment for new orders.

            ↳ **price_precision** `integer`

Maximum precision used for order prices.

            ↳ **qty_increment** `float`

Minimum quantity increment for new orders.

            ↳ **qty_min** `float`

Minimum quantity (in base currency) for new orders.

            ↳ **qty_precision** `integer`

Maximum precision used for order quantities.

            ↳ **status** `string`

**Possible values:**[`cancel_only`, ` delisted`, ` limit_only`, ` maintenance`, ` online`, ` post_only`, ` reduce_only`, ` work_in_progress`] 

Status of pair.

            ↳ **symbol** `string`

**Example:** "BTC/USD"

The symbol of the currency pair.

            ↳ **tick_size** `float deprecated`

**Deprecated Usage:** Use 'price_increment'.

Minimum price increment for new orders.

]
    
    
    {  
        "channel": "instrument",  
        "type": "snapshot",  
        "data": {  
            "assets": [  
                {  
                    "id": "USD",  
                    "status": "enabled",  
                    "precision": 4,  
                    "precision_display": 2,  
                    "borrowable": true,  
                    "collateral_value": 1.0,  
                    "margin_rate": 0.015  
                },  
                {  
                    "id": "BTC",  
                    "status": "enabled",  
                    "precision": 10,  
                    "precision_display": 5,  
                    "borrowable": true,  
                    "collateral_value": 1.0,  
                    "margin_rate": 0.01  
                },  
                {  
                    "id": "XRP",  
                    "status": "enabled",  
                    "precision": 8,  
                    "precision_display": 5,  
                    "borrowable": true,  
                    "collateral_value": 0.0,  
                    "margin_rate": 0.02  
                }  
            ],  
            "pairs": [  
                {  
                    "symbol": "BTC/USD",  
                    "base": "BTC",  
                    "quote": "USD",  
                    "status": "online",  
                    "qty_precision": 8,  
                    "qty_increment": 1e-08,  
                    "price_precision": 1,  
                    "cost_precision": 5,  
                    "marginable": true,  
                    "has_index": true,  
                    "cost_min": 0.5,  
                    "margin_initial": 0.2,  
                    "position_limit_long": 250,  
                    "position_limit_short": 200,  
                    "tick_size": 0.1,  
                    "price_increment": 0.1,  
                    "qty_min": 0.0001  
                },  
                {  
                    "symbol": "MATIC/GBP",  
                    "base": "MATIC",  
                    "quote": "GBP",  
                    "status": "online",  
                    "qty_precision": 8,  
                    "qty_increment": 1e-08,  
                    "price_precision": 4,  
                    "cost_precision": 6,  
                    "marginable": false,  
                    "has_index": true,  
                    "cost_min": 0.43,  
                    "tick_size": 0.0001,  
                    "price_increment": 0.0001,  
                    "qty_min": 4.0  
                }  
            ]  
        }  
    }  
    
    
    
    {  
        "channel": "instrument",  
        "type": "update",  
        "data": {  
           "assets": [  
              {  
                 "id": "BTC",  
                 "status": "enabled",  
                 "precision": 10,  
                 "precision_display": 5,  
                 "borrowable": true,  
                 "collateral_value": 1.0,  
                 "margin_rate": 0.01  
              }  
           ],  
           "pairs": []  
        }  
     }  
    

## Unsubscribe Request

  * Unsubscribe Schema
  * Example: Unsubscribe
  * Unsubscribe Ack Schema
  * Example: Unsubscribe Ack

### MESSAGE BODY

**method** `string` *required*

**Value:** `unsubscribe`

**params** `object`

    ↳ **channel** `string` *required*

**Value:** `instrument`

**req_id** `integer`

Optional client originated request identifier sent as acknowledgment in the response.
    
    
    {  
        "method": "unsubscribe",  
        "params": {  
            "channel": "instrument"  
        },  
        "req_id": 79  
    }  
    

### MESSAGE BODY

**method** `string` *required*

**Value:** `subscribe`

**result** `object`

    ↳ **channel** `string` *required*

**Value:** `instrument`

    ↳ **warnings** `array of strings`

An advisory message, highlighting deprecated fields or upcoming changes to the channel.

**success** `boolean`

**Possible values:**[`true`, ` false`] 

Indicates if the request was successfully processed by the engine.

**error** `string` *conditional*

**Condition:** If success is false. 

Error message.

**time_in** `string`

**Format:** RFC3339

**Example:** 2022-12-25T09:30:59.123456Z

The timestamp when the subscription was received on the wire, just prior to parsing data.

**time_out** `string`

**Format:** RFC3339

**Example:** 2022-12-25T09:30:59.123456Z

The timestamp when the acknowledgement was sent on the wire, just prior to transmitting data.

**req_id** `integer`

Optional client originated request identifier sent as acknowledgment in the response.
    
    
    {  
        "method": "unsubscribe",  
        "req_id": 79,  
        "result": {  
            "channel": "instrument"  
        },  
        "success": true,  
        "time_in": "2023-09-26T16:49:20.962586Z",  
        "time_out": "2023-09-26T16:49:20.962630Z"  
    }