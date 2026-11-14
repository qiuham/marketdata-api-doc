---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/spot/testnet/user-data-stream
api_type: REST
updated_at: 2026-11-13 20:27:22.365021
---

# User Data Streams for Binance Spot TESTNET

## General information

  * Subscribe via the [WebSocket API](/en/docs/catalog/core-trading-spot-trading/api/ws-api/user-data-stream#user-data-stream-subscribe) using an API Key.
  * Both [SBE](/en/docs/products/spot/faqs/sbe_faq) and JSON output are supported.
  * Account events are pushed in **real-time**.
  * All timestamps in JSON payloads are in **milliseconds by default**.
  * Events may contain non-ASCII characters encoded in UTF-8 if you own or trade any assets or symbols whose names contain non-ASCII characters.
  * You can also filter specific events. Please see [User Data Stream Subscription Filters](/en/docs/products/spot/testnet/web-socket-api#user-data-stream-subscription-filters) for more information



## User Data Stream Events

### Account Update

`outboundAccountPosition` is sent any time an account balance has changed and contains the assets that were possibly changed by the event that generated the balance change.
    
    
    Code
    
    {
      "subscriptionId": 0,
      "event": {
        "e": "outboundAccountPosition", // Event type
        "E": 1564034571105,             // Event Time
        "u": 1564034571073,             // Time of last account update
        "B":                            // Balances Array
        [
          {
            "a": "ETH",                 // Asset
            "f": "10000.000000",        // Free
            "l": "0.000000"             // Locked
          }
        ]
      }
    }

### Balance Update

Balance Update occurs during the following:

  * Deposits or withdrawals from the account
  * Transfer of funds between accounts (e.g. Spot to Margin)



**Payload**
    
    
    Code
    
    {
      "subscriptionId": 0,
      "event": {
        "e": "balanceUpdate",         // Event Type
        "E": 1573200697110,           // Event Time
        "a": "BTC",                   // Asset
        "d": "100.00000000",          // Balance Delta
        "T": 1573200697068            // Clear Time
      }
    }

### Order Update

Orders are updated with the `executionReport` event.

**Payload:**
    
    
    Code
    
    {
      "subscriptionId": 0,
      "event": {
        "e": "executionReport",         // Event type
        "E": 1499405658658,             // Event time
        "s": "ETHBTC",                  // Symbol
        "c": "mUvoqJxFIILMdfAW5iGSOW",  // Client order ID
        "S": "BUY",                     // Side
        "o": "LIMIT",                   // Order type
        "f": "GTC",                     // Time in force
        "q": "1.00000000",              // Order quantity
        "p": "0.10264410",              // Order price
        "P": "0.00000000",              // Stop price
        "F": "0.00000000",              // Iceberg quantity
        "g": -1,                        // OrderListId
        "C": "",                        // Original client order ID; This is the ID of the order being canceled
        "x": "NEW",                     // Current execution type
        "X": "NEW",                     // Current order status
        "r": "NONE",                    // Order reject reason; Please see Order Reject Reason (below) for more information.
        "i": 4293153,                   // Order ID
        "l": "0.00000000",              // Last executed quantity
        "z": "0.00000000",              // Cumulative filled quantity
        "L": "0.00000000",              // Last executed price
        "n": "0",                       // Commission amount
        "N": null,                      // Commission asset
        "T": 1499405658657,             // Transaction time
        "t": -1,                        // Trade ID
        "v": 3,                         // Prevented Match Id; This is only visible if the order expired due to STP
        "I": 8641984,                   // Execution Id
        "w": true,                      // Is the order on the book?
        "m": false,                     // Is this trade the maker side?
        "M": false,                     // Ignore
        "O": 1499405658657,             // Order creation time
        "Z": "0.00000000",              // Cumulative quote asset transacted quantity
        "Y": "0.00000000",              // Last quote asset transacted quantity (i.e. lastPrice * lastQty)
        "Q": "0.00000000",              // Quote Order Quantity
        "W": 1499405658657,             // Working Time; This is only visible if the order has been placed on the book.
        "V": "NONE"                     // SelfTradePreventionMode
      }
    }

**Note:** Average price can be found by doing `Z` divided by `z`.

#### Conditional Fields in Execution Report

These are fields that appear in the payload only if certain conditions are met.

For additional information on these parameters, please refer to the [Spot Glossary](/en/docs/products/spot/faqs/spot_glossary).

#### Order Reject Reason

For additional details, look up the Error Message in the [Errors](/en/docs/products/spot/testnet/errors#messages-for--1010-error_msg_received--2010-new_order_rejected--2011-cancel_rejected-and--2038-order_amend_rejected) documentation.

Rejection Reason (`r`)| Error Message  
---|---  
`NONE`| N/A (i.e. The order was not rejected.)  
`INSUFFICIENT_BALANCES`| "Account has insufficient balance for requested action."  
`STOP_PRICE_WOULD_TRIGGER_IMMEDIATELY`| "Order would trigger immediately."  
`WOULD_MATCH_IMMEDIATELY`| "Order would immediately match and take."  
`OCO_BAD_PRICES`| "The relationship of the prices for the orders is not correct."  
  
If the order is an order list, an event named `ListStatus` will be sent in addition to the `executionReport` event.

**Payload**
    
    
    Code
    
    {
      "subscriptionId": 0,
      "event": {
        "e": "listStatus",                 // Event Type
        "E": 1564035303637,                // Event Time
        "s": "ETHBTC",                     // Symbol
        "g": 2,                            // OrderListId
        "c": "OCO",                        // Contingency Type
        "l": "EXEC_STARTED",               // List Status Type
        "L": "EXECUTING",                  // List Order Status
        "r": "NONE",                       // List Reject Reason
        "C": "F4QN4G8DlFATFlIUQ0cjdD",     // List Client Order ID
        "T": 1564035303625,                // Transaction Time
        "O":                               // An array of objects
        [
          {
            "s": "ETHBTC",                 // Symbol
            "i": 17,                       // OrderId
            "c": "AJYsMjErWJesZvqlJCTUgL"  // ClientOrderId
          },
          {
            "s": "ETHBTC",
            "i": 18,
            "c": "bfYPSQdLoqAJeNrOr9adzq"
          }
        ]
      }
    }

#### Execution types

See [Execution types](/en/docs/products/spot/testnet/enums#execution-types) on the Enums page for what each `x` / `X` value means.

#### Order Expiry Reason

See [Expiry Reasons](/en/docs/products/spot/testnet/enums#expiry-reasons) on the Enums page for what each `eR` value means.

Check the [Enums Documentation](/en/docs/products/spot/testnet/enums) for more relevant enum definitions.

### Event Stream Terminated

`eventStreamTerminated` is sent when:

  * [A listen token subscription](/en/docs/products/margin-trading/listen-token-data-stream#websocket-api-method--userdatastreamsubscribelistentoken) expires due to token expiration.
  * A [logon subscription](/en/docs/products/spot/testnet/web-socket-api#session-logon) ends after sending [`session.logout`](/en/docs/catalog/core-trading-spot-trading/api/ws-api/auth#session-logout) method.
  * The subscription is stopped via the [`userDataStream.unsubscribe`](/en/docs/catalog/core-trading-spot-trading/api/ws-api/user-data-stream#user-data-stream-unsubscribe) method.



**Payload:**
    
    
    Code
    
    {
      "subscriptionId": 0,
      "event": {
        "e": "eventStreamTerminated", // Event Type
        "E": 1728973001334            // Event Time
      }
    }

### External Lock Update

`externalLockUpdate` is sent when part of your spot wallet balance is locked/unlocked by an external system, for example when used as margin collateral.

**Payload:**
    
    
    Code
    
    {
      "subscriptionId": 0,
      "event": {
        "e": "externalLockUpdate",   // Event Type
        "E": 1581557507324,          // Event Time
        "a": "NEO",                  // Asset
        "d": "10.00000000",          // Delta
        "T": 1581557507268           // Transaction Time
      }
    }

Was this page helpful?

Last modified on November 12, 2026

[Terms of Use](/en/docs/products/spot/testnet/TESTNET-TERMS-OF-USE)[WebSocket API](/en/docs/products/spot/testnet/web-socket-api)

---

# User Data Streams for Binance Spot TESTNET

## General information

  * Subscribe via the [WebSocket API](/zh-CN/docs/catalog/core-trading-spot-trading/api/ws-api/user-data-stream#user-data-stream-subscribe) using an API Key.
  * Both [SBE](/zh-CN/docs/products/spot/faqs/sbe_faq) and JSON output are supported.
  * Account events are pushed in **real-time**.
  * All timestamps in JSON payloads are in **milliseconds by default**.
  * Events may contain non-ASCII characters encoded in UTF-8 if you own or trade any assets or symbols whose names contain non-ASCII characters.
  * You can also filter specific events. Please see [User Data Stream Subscription Filters](/zh-CN/docs/products/spot/testnet/web-socket-api#user-data-stream-subscription-filters) for more information



## User Data Stream Events

### Account Update

`outboundAccountPosition` is sent any time an account balance has changed and contains the assets that were possibly changed by the event that generated the balance change.
    
    
    Code
    
    {
      "subscriptionId": 0,
      "event": {
        "e": "outboundAccountPosition", // Event type
        "E": 1564034571105,             // Event Time
        "u": 1564034571073,             // Time of last account update
        "B":                            // Balances Array
        [
          {
            "a": "ETH",                 // Asset
            "f": "10000.000000",        // Free
            "l": "0.000000"             // Locked
          }
        ]
      }
    }

### Balance Update

Balance Update occurs during the following:

  * Deposits or withdrawals from the account
  * Transfer of funds between accounts (e.g. Spot to Margin)



**Payload**
    
    
    Code
    
    {
      "subscriptionId": 0,
      "event": {
        "e": "balanceUpdate",         // Event Type
        "E": 1573200697110,           // Event Time
        "a": "BTC",                   // Asset
        "d": "100.00000000",          // Balance Delta
        "T": 1573200697068            // Clear Time
      }
    }

### Order Update

Orders are updated with the `executionReport` event.

**Payload:**
    
    
    Code
    
    {
      "subscriptionId": 0,
      "event": {
        "e": "executionReport",         // Event type
        "E": 1499405658658,             // Event time
        "s": "ETHBTC",                  // Symbol
        "c": "mUvoqJxFIILMdfAW5iGSOW",  // Client order ID
        "S": "BUY",                     // Side
        "o": "LIMIT",                   // Order type
        "f": "GTC",                     // Time in force
        "q": "1.00000000",              // Order quantity
        "p": "0.10264410",              // Order price
        "P": "0.00000000",              // Stop price
        "F": "0.00000000",              // Iceberg quantity
        "g": -1,                        // OrderListId
        "C": "",                        // Original client order ID; This is the ID of the order being canceled
        "x": "NEW",                     // Current execution type
        "X": "NEW",                     // Current order status
        "r": "NONE",                    // Order reject reason; Please see Order Reject Reason (below) for more information.
        "i": 4293153,                   // Order ID
        "l": "0.00000000",              // Last executed quantity
        "z": "0.00000000",              // Cumulative filled quantity
        "L": "0.00000000",              // Last executed price
        "n": "0",                       // Commission amount
        "N": null,                      // Commission asset
        "T": 1499405658657,             // Transaction time
        "t": -1,                        // Trade ID
        "v": 3,                         // Prevented Match Id; This is only visible if the order expired due to STP
        "I": 8641984,                   // Execution Id
        "w": true,                      // Is the order on the book?
        "m": false,                     // Is this trade the maker side?
        "M": false,                     // Ignore
        "O": 1499405658657,             // Order creation time
        "Z": "0.00000000",              // Cumulative quote asset transacted quantity
        "Y": "0.00000000",              // Last quote asset transacted quantity (i.e. lastPrice * lastQty)
        "Q": "0.00000000",              // Quote Order Quantity
        "W": 1499405658657,             // Working Time; This is only visible if the order has been placed on the book.
        "V": "NONE"                     // SelfTradePreventionMode
      }
    }

**Note:** Average price can be found by doing `Z` divided by `z`.

#### Conditional Fields in Execution Report

These are fields that appear in the payload only if certain conditions are met.

For additional information on these parameters, please refer to the [Spot Glossary](/zh-CN/docs/products/spot/faqs/spot_glossary).

#### Order Reject Reason

For additional details, look up the Error Message in the [Errors](/zh-CN/docs/products/spot/testnet/errors#messages-for--1010-error_msg_received--2010-new_order_rejected--2011-cancel_rejected-and--2038-order_amend_rejected) documentation.

Rejection Reason (`r`)| Error Message  
---|---  
`NONE`| N/A (i.e. The order was not rejected.)  
`INSUFFICIENT_BALANCES`| "Account has insufficient balance for requested action."  
`STOP_PRICE_WOULD_TRIGGER_IMMEDIATELY`| "Order would trigger immediately."  
`WOULD_MATCH_IMMEDIATELY`| "Order would immediately match and take."  
`OCO_BAD_PRICES`| "The relationship of the prices for the orders is not correct."  
  
If the order is an order list, an event named `ListStatus` will be sent in addition to the `executionReport` event.

**Payload**
    
    
    Code
    
    {
      "subscriptionId": 0,
      "event": {
        "e": "listStatus",                 // Event Type
        "E": 1564035303637,                // Event Time
        "s": "ETHBTC",                     // Symbol
        "g": 2,                            // OrderListId
        "c": "OCO",                        // Contingency Type
        "l": "EXEC_STARTED",               // List Status Type
        "L": "EXECUTING",                  // List Order Status
        "r": "NONE",                       // List Reject Reason
        "C": "F4QN4G8DlFATFlIUQ0cjdD",     // List Client Order ID
        "T": 1564035303625,                // Transaction Time
        "O":                               // An array of objects
        [
          {
            "s": "ETHBTC",                 // Symbol
            "i": 17,                       // OrderId
            "c": "AJYsMjErWJesZvqlJCTUgL"  // ClientOrderId
          },
          {
            "s": "ETHBTC",
            "i": 18,
            "c": "bfYPSQdLoqAJeNrOr9adzq"
          }
        ]
      }
    }

#### Execution types

See [Execution types](/zh-CN/docs/products/spot/testnet/enums#execution-types) on the Enums page for what each `x` / `X` value means.

#### Order Expiry Reason

See [Expiry Reasons](/zh-CN/docs/products/spot/testnet/enums#expiry-reasons) on the Enums page for what each `eR` value means.

Check the [Enums Documentation](/zh-CN/docs/products/spot/testnet/enums) for more relevant enum definitions.

### Event Stream Terminated

`eventStreamTerminated` is sent when:

  * [A listen token subscription](/zh-CN/docs/products/margin-trading/listen-token-data-stream#websocket-api-method--userdatastreamsubscribelistentoken) expires due to token expiration.
  * A [logon subscription](/zh-CN/docs/products/spot/testnet/web-socket-api#session-logon) ends after sending [`session.logout`](/zh-CN/docs/catalog/core-trading-spot-trading/api/ws-api/auth#session-logout) method.
  * The subscription is stopped via the [`userDataStream.unsubscribe`](/zh-CN/docs/catalog/core-trading-spot-trading/api/ws-api/user-data-stream#user-data-stream-unsubscribe) method.



**Payload:**
    
    
    Code
    
    {
      "subscriptionId": 0,
      "event": {
        "e": "eventStreamTerminated", // Event Type
        "E": 1728973001334            // Event Time
      }
    }

### External Lock Update

`externalLockUpdate` is sent when part of your spot wallet balance is locked/unlocked by an external system, for example when used as margin collateral.

**Payload:**
    
    
    Code
    
    {
      "subscriptionId": 0,
      "event": {
        "e": "externalLockUpdate",   // Event Type
        "E": 1581557507324,          // Event Time
        "a": "NEO",                  // Asset
        "d": "10.00000000",          // Delta
        "T": 1581557507268           // Transaction Time
      }
    }

此页面是否有帮助？

Last modified on November 12, 2026

[Terms of Use](/zh-CN/docs/products/spot/testnet/TESTNET-TERMS-OF-USE)[WebSocket API](/zh-CN/docs/products/spot/testnet/web-socket-api)