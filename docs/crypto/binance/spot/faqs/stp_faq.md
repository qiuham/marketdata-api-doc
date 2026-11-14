---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/spot/faqs/stp_faq
api_type: REST
updated_at: 2026-11-13 20:24:39.132027
---

# Self Trade Prevention (STP) FAQ

**Disclaimer:**

  * The commissions and prices used here are fictional and do not imply anything about the actual setup on the live exchange.



### What is Self Trade Prevention?

Self Trade Prevention (or STP) prevents orders of users, or the user's `tradeGroupId` to match against their own.

### What defines a self-trade?

A self-trade can occur in either scenario:

  * The order traded against the same account.
  * The order traded against an account with the same `tradeGroupId`.



### What happens when STP is triggered?

There are five possible modes for what the system does when an order would create a self-trade.

`NONE` \- This mode exempts the order from self-trade prevention. Accounts or Trade group IDs will not be compared, no orders will be expired, and the trade will occur.

`EXPIRE_TAKER` \- This mode prevents a trade by immediately expiring the taker order's remaining quantity.

`EXPIRE_MAKER` \- This mode prevents a trade by immediately expiring the potential maker order's remaining quantity.

`EXPIRE_BOTH` \- This mode prevents a trade by immediately expiring both the taker and the potential maker orders' remaining quantities.

`DECREMENT` \- This mode increases the `prevented quantity` of _both_ orders by the amount of the prevented match. The smaller of the two orders will expire, or both if they have the same quantity.

`TRANSFER` \- If orders are from the same account, then the behavior is the same as `DECREMENT`. If orders are from different accounts with the same `tradeGroupId`, then in addition to the behavior of `DECREMENT`, the `last prevented quantity` and its notional are transferred between the two accounts.

STP behavior is typically determined by the STP mode of the **taker order** only. The exception is that for STP `TRANSFER` to occur, both the maker and taker orders must specify STP mode `TRANSFER`. If the taker order specifies STP mode `TRANSFER`, but the maker order specifies a different STP mode, then the STP behavior is `DECREMENT`.

In summary:

Taker Order STP Mode| Maker Order STP Mode| Effective STP Mode  
---|---|---  
`TRANSFER`| `TRANSFER`| `TRANSFER`  
`TRANSFER`| `EXPIRE_MAKER`, `EXPIRE_TAKER`, `EXPIRE_BOTH`, `NONE`, `DECREMENT`| `DECREMENT`  
`EXPIRE_MAKER`, `EXPIRE_TAKER`, `EXPIRE_BOTH`, `NONE`, `DECREMENT`| ANY STP MODE| STP mode of the Taker Order  
  
### How is the Effective STP Mode reported?

The Effective STP Mode is reported back on prevented match execution reports and order responses whenever it differs from the STP mode the report's own order was placed with:

  * `FULL` order responses (REST and WebSocket API): `effectiveSelfTradePreventionMode` inside each entry of `preventedMatches[]`.
  * User Data Stream `executionReport`: `eV`.
  * FIX `ExecutionReport<8>`: tag `25058 EffectiveSelfTradePreventionMode`.



The field is only present when the applied STP mode differs from the mode specified on the report's own order. If the stated mode is applied as-is, the field is omitted. It is never reported as `NONE`.

Each report carries this field relative to its own order's mode, so a single prevented match can produce a taker report with the field absent and a maker report with the field set, or vice versa.

### What is a Trade Group Id?

Different accounts with the same `tradeGroupId` are considered part of the same "trade group". Orders submitted by members of a trade group are eligible for STP according to the taker-order's STP mode.

A user can confirm if their accounts are under the same `tradeGroupId` from the API either from `GET /api/v3/account` (REST API) or `account.status` (WebSocket API) for each account.

The field is also present in the response for `GET /api/v3/preventedMatches` (REST API) or `myPreventedMatches` (WebSocket API).

If the value is `-1`, then the `tradeGroupId` has not been set for that account, so the STP may only take place between orders of the same account.

### What is a Prevented Match?

When a self-trade is prevented, a prevented match is created. The orders in the prevented match have their prevented quantities increased and one or more orders expire.

This is not to be confused with a trade, as no orders will match.

This is a record of what orders could have self-traded.

This can be queried through the endpoint `GET /api/v3/preventedMatches` on the REST API or `myPreventedMatches` on the WebSocket API.

This is a sample of the output request for reference:
    
    
    Code
    
    [
      {
        symbol: "BTCDUSDT", // Symbol of the orders
        preventedMatchId: 8, // Identifies the prevented match of the expired order(s) for the symbol.
        takerOrderId: 12, // Order Id of the Taker Order
        makerOrderId: 10, // Order Id of the Maker Order
        tradeGroupId: 1, // Identifies the Trade Group Id. (If the account is not part of a trade group, this will be -1.)
        selfTradePreventionMode: "EXPIRE_BOTH", // STP mode that expired the order(s).
        price: "50.00000000", // Price at which the match occurred.
        takerPreventedQuantity: "1.00000000", // Taker's remaining quantity before the STP. Only appears if the STP mode is EXPIRE_TAKER, EXPIRE_BOTH or DECREMENT.
        makerPreventedQuantity: "10.00000000", // Maker's remaining quantity before the STP. Only appears if the STP mode is EXPIRE_MAKER, EXPIRE_BOTH, or DECREMENT.
        transactTime: 1663190634060, // Time the order(s) expired due to STP.
      },
    ];

### What is "prevented quantity?"

STP events expire quantity from open orders. The STP modes `EXPIRE_TAKER`, `EXPIRE_MAKER`, and `EXPIRE_BOTH` expire all remaining quantity on the affected orders, resulting in the entire open order being expired.

Prevented quantity is the amount of quantity that is expired due to STP events for a particular order. User stream execution reports for orders involved in STP may have these fields:
    
    
    Code
    
    {
        "A": "3.000000",     // Prevented Quantity
        "B": "3.000000"      // Last Prevented Quantity
    }

`B` is present for execution type `TRADE_PREVENTION`, and is the quantity expired due to that individual STP event.

`A` is the cumulative quantity expired due to STP over the lifetime of the order. For `EXPIRE_TAKER`, `EXPIRE_MAKER`, and `EXPIRE_BOTH` modes this will always be the same value as `B`.

API responses for orders which expired due to STP will also have a `preventedQuantity` field, indicating the cumulative quantity expired due to STP over the lifetime of the order.

While an order is open, the following equation holds true:
    
    
    Code
    
    original order quantity - executed quantity - prevented quantity = quantity available for further execution

When an order's available quantity goes to zero, the order will be removed from the order book and the status will be one of `EXPIRED_IN_MATCH`, `FILLED`, or `EXPIRED`.

### How do I know which symbol uses STP?

Symbols may be configured to allow different sets of STP modes and take different default STP modes.

`defaultSelfTradePreventionMode` \- Orders will use this STP mode if the user does not provide one on order placement.

`allowedSelfTradePreventionModes` \- Defines the allowed set of STP modes for order placement on that symbol.

For example, if a symbol has the following configuration:
    
    
    Code
    
    {
      "defaultSelfTradePreventionMode": "NONE",
      "allowedSelfTradePreventionModes": ["NONE", "EXPIRE_TAKER", "EXPIRE_BOTH"]
    }

Then that means if a user sends an order with no `selfTradePreventionMode` provided, then the order sent will have the value of `NONE`.

If a user wants to explicitly specify the mode they can pass the enum `NONE`, `EXPIRE_TAKER`, or `EXPIRE_BOTH`.

If a user tries to specify `EXPIRE_MAKER` for orders on this symbol, they will receive an error:
    
    
    Code
    
    {
      "code": -1013,
      "msg": "This symbol does not allow the specified self-trade prevention mode."
    }

### How do I know if an order expired due to STP?

The order will have the status `EXPIRED_IN_MATCH`.

### STP Examples

For all these cases, assume that all orders for these examples are made on the same account.

**Scenario A- A user sends a new order with selfTradePreventionMode:`NONE` that will match with another order of theirs that is already on the book.**
    
    
    Code
    
    Maker Order: symbol=BTCUSDT side=BUY  type=LIMIT quantity=1 price=1 selfTradePreventionMode=NONE
    Taker Order: symbol=BTCUSDT side=SELL type=LIMIT quantity=1 price=1 selfTradePreventionMode=NONE

**Result** : No STP is triggered and the orders will match.

Order Status of the Maker Order
    
    
    Code
    
    {
      "symbol": "BTCUSDT",
      "orderId": 2,
      "orderListId": -1,
      "clientOrderId": "FaDk4LPRxastaICEFE9YTf",
      "price": "1.000000",
      "origQty": "1.000000",
      "executedQty": "1.000000",
      "cummulativeQuoteQty": "1.000000",
      "status": "FILLED",
      "timeInForce": "GTC",
      "type": "LIMIT",
      "side": "BUY",
      "stopPrice": "0.000000",
      "icebergQty": "0.000000",
      "time": 1670217090310,
      "updateTime": 1670217090330,
      "isWorking": true,
      "workingTime": 1670217090310,
      "origQuoteOrderQty": "0.000000",
      "selfTradePreventionMode": "NONE"
    }

Order Status of the Taker Order
    
    
    Code
    
    {
      "symbol": "BTCUSDT",
      "orderId": 3,
      "orderListId": -1,
      "clientOrderId": "Ay48Vtpghnsvy6w8RPQEde",
      "transactTime": 1670207731263,
      "price": "1.000000",
      "origQty": "1.000000",
      "executedQty": "1.000000",
      "cummulativeQuoteQty": "1.000000",
      "status": "FILLED",
      "timeInForce": "GTC",
      "type": "LIMIT",
      "side": "SELL",
      "workingTime": 1670207731263,
      "fills": [
        {
          "price": "1.000000",
          "qty": "1.000000",
          "commission": "0.000000",
          "commissionAsset": "USDT",
          "tradeId": 1
        }
      ],
      "selfTradePreventionMode": "NONE"
    }

**Scenario B- A user sends an order with`EXPIRE_MAKER` that would match with their orders that are already on the book.**
    
    
    Code
    
    Maker Order 1: symbol=BTCUSDT side=BUY  type=LIMIT quantity=1.2 price=1.2 selfTradePreventionMode=NONE
    Maker Order 2: symbol=BTCUSDT side=BUY  type=LIMIT quantity=1.3 price=1.1 selfTradePreventionMode=NONE
    Maker Order 3: symbol=BTCUSDT side=BUY  type=LIMIT quantity=8.1 price=1   selfTradePreventionMode=NONE
    Taker Order 1: symbol=BTCUSDT side=SELL type=LIMIT quantity=3   price=1   selfTradePreventionMode=EXPIRE_MAKER

**Result** : The orders that were on the book will expire due to STP, and the taker order will go on the book.

Maker Order 1
    
    
    Code
    
    {
      "symbol": "BTCUSDT",
      "orderId": 2,
      "orderListId": -1,
      "clientOrderId": "wpNzhSclc16pV8g5THIOR3",
      "price": "1.200000",
      "origQty": "1.200000",
      "executedQty": "0.000000",
      "cummulativeQuoteQty": "0.000000",
      "status": "EXPIRED_IN_MATCH",
      "timeInForce": "GTC",
      "type": "LIMIT",
      "side": "BUY",
      "stopPrice": "0.000000",
      "icebergQty": "0.000000",
      "time": 1670217957437,
      "updateTime": 1670217957498,
      "isWorking": true,
      "workingTime": 1670217957437,
      "origQuoteOrderQty": "0.000000",
      "selfTradePreventionMode": "NONE",
      "preventedMatchId": 0,
      "preventedQuantity": "1.200000"
    }

Maker Order 2
    
    
    Code
    
    {
      "symbol": "BTCUSDT",
      "orderId": 3,
      "orderListId": -1,
      "clientOrderId": "ZT9emqia99V7x8B6FW0pFF",
      "price": "1.100000",
      "origQty": "1.300000",
      "executedQty": "0.000000",
      "cummulativeQuoteQty": "0.000000",
      "status": "EXPIRED_IN_MATCH",
      "timeInForce": "GTC",
      "type": "LIMIT",
      "side": "BUY",
      "stopPrice": "0.000000",
      "icebergQty": "0.000000",
      "time": 1670217957458,
      "updateTime": 1670217957498,
      "isWorking": true,
      "workingTime": 1670217957458,
      "origQuoteOrderQty": "0.000000",
      "selfTradePreventionMode": "NONE",
      "preventedMatchId": 1,
      "preventedQuantity": "1.300000"
    }

Maker Order 3
    
    
    Code
    
    {
      "symbol": "BTCUSDT",
      "orderId": 4,
      "orderListId": -1,
      "clientOrderId": "8QZ3taGcU4gND59TxHAcR0",
      "price": "1.000000",
      "origQty": "8.100000",
      "executedQty": "0.000000",
      "cummulativeQuoteQty": "0.000000",
      "status": "EXPIRED_IN_MATCH",
      "timeInForce": "GTC",
      "type": "LIMIT",
      "side": "BUY",
      "stopPrice": "0.000000",
      "icebergQty": "0.000000",
      "time": 1670217957478,
      "updateTime": 1670217957498,
      "isWorking": true,
      "workingTime": 1670217957478,
      "origQuoteOrderQty": "0.000000",
      "selfTradePreventionMode": "NONE",
      "preventedMatchId": 2,
      "preventedQuantity": "8.100000"
    }

Output of the Taker Order
    
    
    Code
    
    {
      "symbol": "BTCUSDT",
      "orderId": 5,
      "orderListId": -1,
      "clientOrderId": "WRzbhp257NhZsIJW4y2Nri",
      "transactTime": 1670217957498,
      "price": "1.000000",
      "origQty": "3.000000",
      "executedQty": "0.000000",
      "cummulativeQuoteQty": "0.000000",
      "status": "NEW",
      "timeInForce": "GTC",
      "type": "LIMIT",
      "side": "SELL",
      "workingTime": 1670217957498,
      "fills": [],
      "preventedMatches": [
        {
          "preventedMatchId": 0,
          "makerOrderId": 2,
          "price": "1.200000",
          "makerPreventedQuantity": "1.200000"
        },
        {
          "preventedMatchId": 1,
          "makerOrderId": 3,
          "price": "1.100000",
          "makerPreventedQuantity": "1.300000"
        },
        {
          "preventedMatchId": 2,
          "makerOrderId": 4,
          "price": "1.000000",
          "makerPreventedQuantity": "8.100000"
        }
      ],
      "selfTradePreventionMode": "EXPIRE_MAKER"
    }

**Scenario C - A user sends an order with`EXPIRE_TAKER` that would match with their orders already on the book.**
    
    
    Code
    
    Maker Order 1: symbol=BTCUSDT side=BUY  type=LIMIT quantity=1.2 price=1.2  selfTradePreventionMode=NONE
    Maker Order 2: symbol=BTCUSDT side=BUY  type=LIMIT quantity=1.3 price=1.1  selfTradePreventionMode=NONE
    Maker Order 3: symbol=BTCUSDT side=BUY  type=LIMIT quantity=8.1 price=1    selfTradePreventionMode=NONE
    Taker Order 1: symbol=BTCUSDT side=SELL type=LIMIT quantity=3   price=1    selfTradePreventionMode=EXPIRE_TAKER

**Result** : The orders already on the book will remain, while the taker order will expire.

Maker Order 1
    
    
    Code
    
    {
      "symbol": "BTCUSDT",
      "orderId": 2,
      "orderListId": -1,
      "clientOrderId": "NpwW2t0L4AGQnCDeNjHIga",
      "price": "1.200000",
      "origQty": "1.200000",
      "executedQty": "0.000000",
      "cummulativeQuoteQty": "0.000000",
      "status": "NEW",
      "timeInForce": "GTC",
      "type": "LIMIT",
      "side": "BUY",
      "stopPrice": "0.000000",
      "icebergQty": "0.000000",
      "time": 1670219811986,
      "updateTime": 1670219811986,
      "isWorking": true,
      "workingTime": 1670219811986,
      "origQuoteOrderQty": "0.000000",
      "selfTradePreventionMode": "NONE"
    }

Maker Order 2
    
    
    Code
    
    {
      "symbol": "BTCUSDT",
      "orderId": 3,
      "orderListId": -1,
      "clientOrderId": "TSAmJqGWk4YTB2yA9p04UO",
      "price": "1.100000",
      "origQty": "1.300000",
      "executedQty": "0.000000",
      "cummulativeQuoteQty": "0.000000",
      "status": "NEW",
      "timeInForce": "GTC",
      "type": "LIMIT",
      "side": "BUY",
      "stopPrice": "0.000000",
      "icebergQty": "0.000000",
      "time": 1670219812007,
      "updateTime": 1670219812007,
      "isWorking": true,
      "workingTime": 1670219812007,
      "origQuoteOrderQty": "0.000000",
      "selfTradePreventionMode": "NONE"
    }

Maker Order 3
    
    
    Code
    
    {
      "symbol": "BTCUSDT",
      "orderId": 4,
      "orderListId": -1,
      "clientOrderId": "L6FmpCJJP6q4hCNv4MuZDG",
      "price": "1.000000",
      "origQty": "8.100000",
      "executedQty": "0.000000",
      "cummulativeQuoteQty": "0.000000",
      "status": "NEW",
      "timeInForce": "GTC",
      "type": "LIMIT",
      "side": "BUY",
      "stopPrice": "0.000000",
      "icebergQty": "0.000000",
      "time": 1670219812026,
      "updateTime": 1670219812026,
      "isWorking": true,
      "workingTime": 1670219812026,
      "origQuoteOrderQty": "0.000000",
      "selfTradePreventionMode": "NONE"
    }

Output of the Taker order
    
    
    Code
    
    {
      "symbol": "BTCUSDT",
      "orderId": 5,
      "orderListId": -1,
      "clientOrderId": "kocvDAi4GNN2y1l1Ojg1Ri",
      "price": "1.000000",
      "origQty": "3.000000",
      "executedQty": "0.000000",
      "cummulativeQuoteQty": "0.000000",
      "status": "EXPIRED_IN_MATCH",
      "timeInForce": "GTC",
      "type": "LIMIT",
      "side": "SELL",
      "stopPrice": "0.000000",
      "icebergQty": "0.000000",
      "time": 1670219812046,
      "updateTime": 1670219812046,
      "isWorking": true,
      "workingTime": 1670219812046,
      "origQuoteOrderQty": "0.000000",
      "selfTradePreventionMode": "EXPIRE_TAKER",
      "preventedMatchId": 0,
      "preventedQuantity": "3.000000"
    }

**Scenario D- A user has an order on the book, and then sends an order with`EXPIRE_BOTH` that would match with the existing order.**
    
    
    Code
    
    Maker Order: symbol=BTCUSDT side=BUY  type=LIMIT quantity=1 price=1 selfTradePreventionMode=NONE
    Taker Order: symbol=BTCUSDT side=SELL type=LIMIT quantity=3 price=1 selfTradePreventionMode=EXPIRE_BOTH

**Result:** Both orders will expire.

Maker Order
    
    
    Code
    
    {
      "symbol": "BTCUSDT",
      "orderId": 2,
      "orderListId": -1,
      "clientOrderId": "2JPC8xjpLq6Q0665uYWAcs",
      "price": "1.000000",
      "origQty": "1.000000",
      "executedQty": "0.000000",
      "cummulativeQuoteQty": "0.000000",
      "status": "EXPIRED_IN_MATCH",
      "timeInForce": "GTC",
      "type": "LIMIT",
      "side": "BUY",
      "stopPrice": "0.000000",
      "icebergQty": "0.000000",
      "time": 1673842412831,
      "updateTime": 1673842413170,
      "isWorking": true,
      "workingTime": 1673842412831,
      "origQuoteOrderQty": "0.000000",
      "selfTradePreventionMode": "NONE",
      "preventedMatchId": 0,
      "preventedQuantity": "1.000000"
    }

Taker Order
    
    
    Code
    
    {
      "symbol": "BTCUSDT",
      "orderId": 5,
      "orderListId": -1,
      "clientOrderId": "qMaz8yrOXk2iUIz74cFkiZ",
      "transactTime": 1673842413170,
      "price": "1.000000",
      "origQty": "3.000000",
      "executedQty": "0.000000",
      "cummulativeQuoteQty": "0.000000",
      "status": "EXPIRED_IN_MATCH",
      "timeInForce": "GTC",
      "type": "LIMIT",
      "side": "SELL",
      "workingTime": 1673842413170,
      "fills": [],
      "preventedMatches": [
        {
          "preventedMatchId": 0,
          "makerOrderId": 2,
          "price": "1.000000",
          "takerPreventedQuantity": "3.000000",
          "makerPreventedQuantity": "1.000000"
        }
      ],
      "selfTradePreventionMode": "EXPIRE_BOTH",
      "tradeGroupId": 1,
      "preventedQuantity": "3.000000"
    }

**Scenario E - A user has an order on the book with`EXPIRE_MAKER`, and then sends a new order with `EXPIRE_TAKER` which would match with the existing order.**
    
    
    Code
    
    Maker Order: symbol=BTCUSDT side=BUY  type=LIMIT quantity=1 price=1 selfTradePreventionMode=EXPIRE_MAKER
    Taker Order: symbol=BTCUSDT side=SELL type=LIMIT quantity=1 price=1 selfTradePreventionMode=EXPIRE_TAKER

**Result** : The taker order's STP mode will be used, so the taker order will be expired.

Maker Order
    
    
    Code
    
    {
      "symbol": "BTCUSDT",
      "orderId": 0,
      "orderListId": -1,
      "clientOrderId": "jFUap8iFwwgqIpOfAL60GS",
      "price": "1.000000",
      "origQty": "1.000000",
      "executedQty": "0.000000",
      "cummulativeQuoteQty": "0.000000",
      "status": "NEW",
      "timeInForce": "GTC",
      "type": "LIMIT",
      "side": "BUY",
      "stopPrice": "0.000000",
      "icebergQty": "0.000000",
      "time": 1670220769261,
      "updateTime": 1670220769261,
      "isWorking": true,
      "workingTime": 1670220769261,
      "origQuoteOrderQty": "0.000000",
      "selfTradePreventionMode": "EXPIRE_MAKER"
    }

Taker Order
    
    
    Code
    
    {
      "symbol": "BTCUSDT",
      "orderId": 1,
      "orderListId": -1,
      "clientOrderId": "zxrvnNNm1RXC3rkPLUPrc1",
      "transactTime": 1670220800315,
      "price": "1.000000",
      "origQty": "1.000000",
      "executedQty": "0.000000",
      "cummulativeQuoteQty": "0.000000",
      "status": "EXPIRED_IN_MATCH",
      "timeInForce": "GTC",
      "type": "LIMIT",
      "side": "SELL",
      "workingTime": 1670220800315,
      "fills": [],
      "preventedMatches": [
        {
          "preventedMatchId": 0,
          "makerOrderId": 0,
          "price": "1.000000",
          "takerPreventedQuantity": "1.000000"
        }
      ],
      "selfTradePreventionMode": "EXPIRE_TAKER",
      "preventedQuantity": "1.000000"
    }

**Scenario F - A user sends a market order with`EXPIRE_MAKER` which would match with an existing order.**
    
    
    Code
    
    Maker Order: symbol=BTCUSDT side=BUY  type=LIMIT  quantity=1 price=1  selfTradePreventionMode=NONE
    Taker Order: symbol=BTCUSDT side=SELL type=MARKET quantity=1          selfTradePreventionMode=EXPIRE_MAKER

**Result** : The existing order expires with the status `EXPIRED_IN_MATCH`, due to STP. The new order also expires but with status `EXPIRED`, due to low liquidity on the order book.

Maker Order
    
    
    Code
    
    {
      "symbol": "BTCUSDT",
      "orderId": 2,
      "orderListId": -1,
      "clientOrderId": "7sgrQQInL69XDMQpiqMaG2",
      "price": "1.000000",
      "origQty": "1.000000",
      "executedQty": "0.000000",
      "cummulativeQuoteQty": "0.000000",
      "status": "EXPIRED_IN_MATCH",
      "timeInForce": "GTC",
      "type": "LIMIT",
      "side": "BUY",
      "stopPrice": "0.000000",
      "icebergQty": "0.000000",
      "time": 1670222557456,
      "updateTime": 1670222557478,
      "isWorking": true,
      "workingTime": 1670222557456,
      "origQuoteOrderQty": "0.000000",
      "selfTradePreventionMode": "NONE",
      "preventedMatchId": 0,
      "preventedQuantity": "1.000000"
    }

Taker Order
    
    
    Code
    
    {
      "symbol": "BTCUSDT",
      "orderId": 3,
      "orderListId": -1,
      "clientOrderId": "zqhsgGDEcdhxy2oza2Ljxd",
      "transactTime": 1670222557478,
      "price": "0.000000",
      "origQty": "1.000000",
      "executedQty": "0.000000",
      "cummulativeQuoteQty": "0.000000",
      "status": "EXPIRED",
      "timeInForce": "GTC",
      "type": "MARKET",
      "side": "SELL",
      "workingTime": 1670222557478,
      "fills": [],
      "preventedMatches": [
        {
          "preventedMatchId": 0,
          "makerOrderId": 2,
          "price": "1.000000",
          "makerPreventedQuantity": "1.000000"
        }
      ],
      "selfTradePreventionMode": "EXPIRE_MAKER"
    }

**Scenario G- A user sends a limit order with`DECREMENT` which would match with an existing order.**
    
    
    Code
    
    Maker Order: symbol=BTCUSDT side=BUY  type=LIMIT quantity=6 price=2  selfTradePreventionMode=NONE
    Taker Order: symbol=BTCUSDT side=SELL type=LIMIT quantity=2 price=2  selfTradePreventionMode=DECREMENT

**Result** : Both orders have a preventedQuantity of 2. Since this is the taker order’s full quantity, it expires due to STP.

Maker Order
    
    
    Code
    
    {
      "symbol": "BTCUSDT",
      "orderId": 23,
      "orderListId": -1,
      "clientOrderId": "Kxb4RpsBhfQrkK2r2YO2Z9",
      "price": "2.00000000",
      "origQty": "6.00000000",
      "executedQty": "0.00000000",
      "cummulativeQuoteQty": "0.00000000",
      "status": "NEW",
      "timeInForce": "GTC",
      "type": "LIMIT",
      "side": "BUY",
      "stopPrice": "0.00000000",
      "icebergQty": "0.00000000",
      "time": 1741682807892,
      "updateTime": 1741682816376,
      "isWorking": true,
      "workingTime": 1741682807892,
      "origQuoteOrderQty": "0.00000000",
      "selfTradePreventionMode": "DECREMENT",
      "preventedMatchId": 4,
      "preventedQuantity": "2.00000000"
    }

Taker Order
    
    
    Code
    
    {
      "symbol": "BTCUSDT",
      "orderId": 24,
      "orderListId": -1,
      "clientOrderId": "dwf3qOzD7GM9ysDn9XG9AS",
      "price": "2.00000000",
      "origQty": "2.00000000",
      "executedQty": "0.00000000",
      "cummulativeQuoteQty": "0.00000000",
      "status": "EXPIRED_IN_MATCH",
      "timeInForce": "GTC",
      "type": "LIMIT",
      "side": "SELL",
      "stopPrice": "0.00000000",
      "icebergQty": "0.00000000",
      "time": 1741682816376,
      "updateTime": 1741682816376,
      "isWorking": true,
      "workingTime": 1741682816376,
      "origQuoteOrderQty": "0.00000000",
      "selfTradePreventionMode": "DECREMENT",
      "preventedMatchId": 4,
      "preventedQuantity": "2.00000000"
    }

**Scenario H- A user sends a limit order with`TRANSFER` which would match with an existing order under the same tradeGroupId.**

Balances before order placement

Maker's Balances
    
    
    Code
    
    {
      "balances": [
        {
          "asset": "BTC",
          "free": "20000.00000000",
          "locked": "0.00000000"
        },
        {
          "asset": "USDT",
          "free": "20000.00000000",
          "locked": "0.00000000"
        }
      ]
    }

Taker's Balances
    
    
    Code
    
    {
      "balances": [
        {
          "asset": "BTC",
          "free": "20000.00000000",
          "locked": "0.00000000"
        },
        {
          "asset": "USDT",
          "free": "20000.00000000",
          "locked": "0.00000000"
        }
      ]
    }
    
    
    Code
    
    Maker Order: symbol=BTCUSDT side=BUY  type=LIMIT quantity=0.6 price=0.2  selfTradePreventionMode=TRANSFER tradeGroupId=1
    Taker Order: symbol=BTCUSDT side=SELL type=LIMIT quantity=0.2 price=0.2  selfTradePreventionMode=TRANSFER tradeGroupId=1

**Result:** Both orders have a preventedQuantity of 0.2. Since this is the taker’s full quantity, it expires due to STP.

Maker Order
    
    
    Code
    
    {
      "symbol": "BTCUSDT",
      "orderId": 12,
      "orderListId": -1,
      "clientOrderId": "zEyu9HGqiT5YUaXXhKr1MR",
      "price": "0.20000000",
      "origQty": "0.60000000",
      "executedQty": "0.00000000",
      "cummulativeQuoteQty": "0.00000000",
      "status": "NEW",
      "timeInForce": "GTC",
      "type": "LIMIT",
      "side": "BUY",
      "stopPrice": "0.00000000",
      "icebergQty": "0.00000000",
      "time": 1762852466582,
      "updateTime": 1762852522145,
      "isWorking": true,
      "workingTime": 1762852466582,
      "origQuoteOrderQty": "0.00000000",
      "selfTradePreventionMode": "TRANSFER",
      "preventedMatchId": 3,
      "preventedQuantity": "0.20000000"
    }

Taker Order
    
    
    Code
    
    {
      "symbol": "BTCUSDT",
      "orderId": 13,
      "orderListId": -1,
      "clientOrderId": "6T06cph3Et2yFNnGpHdejh",
      "transactTime": 1762852522145,
      "price": "0.20000000",
      "origQty": "0.20000000",
      "executedQty": "0.00000000",
      "origQuoteOrderQty": "0.00000000",
      "cummulativeQuoteQty": "0.00000000",
      "status": "EXPIRED_IN_MATCH",
      "timeInForce": "GTC",
      "type": "LIMIT",
      "side": "SELL",
      "workingTime": 1762852522145,
      "fills": [],
      "preventedMatches": [
        {
          "preventedMatchId": 3,
          "makerSymbol": "BTCUSDT",
          "makerOrderId": 12,
          "price": "0.20000000",
          "takerPreventedQuantity": "0.20000000",
          "makerPreventedQuantity": "0.20000000"
        }
      ],
      "selfTradePreventionMode": "TRANSFER",
      "tradeGroupId": 1,
      "preventedQuantity": "0.20000000"
    }

Balances after self-trade prevention:

Maker Balances
    
    
    Code
    
    {
      "balances": [
        {
          "asset": "BTC",
          "free": "20000.20000000",
          "locked": "0.00000000"
        },
        {
          "asset": "USDT",
          "free": "19999.88000000",
          "locked": "0.08000000"
        }
      ]
    }

Taker's Balances
    
    
    Code
    
    {
      "balances": [
        {
          "asset": "BTC",
          "free": "19999.80000000",
          "locked": "0.00000000"
        },
        {
          "asset": "USDT",
          "free": "20000.04000000",
          "locked": "0.00000000"
        }
      ]
    }

Was this page helpful?

Last modified on November 12, 2026

[SPOT API Glossary](/en/docs/products/spot/faqs/spot_glossary)[Trailing Stop Orders](/en/docs/products/spot/faqs/trailing-stop-faq)

---

# 自我交易预防 (Self Trade Prevention - STP) 常见问题

**免责声明:**

  * 此处使用的佣金和价格是虚构的，并不反映实际交易所的设置。



### 什么是 Self Trade Prevention - STP?

自我交易预防是指阻止订单与来自同一账户或者同一 `tradeGroupId` 账户的订单交易。

### 什么是自我交易（self-trade）?

在以下任一情况下都可能发生自我交易：

  * 属于同一账户的订单之间交易。
  * 属于相同 `tradeGroupId` 的账户的订单之间交易。



### STP 触发时会发生什么？

如果订单会触发自我交易，系统将执行五种可能的模式：

`NONE` \- 此模式使订单免于自我交易预防。

`EXPIRE_TAKER` \- 此模式通过立即使吃单者(taker)的剩余数量过期来预防交易。

`EXPIRE_MAKER` \- 此模式通过立即使潜在挂单者(maker)的剩余数量过期来预防交易。

`EXPIRE_BOTH` \- 此模式通过立即同时使吃单和挂单者的剩余数量过期来预防交易。

`DECREMENT` \- 此模式通过阻止匹配的数量来增加 _两种_ 订单的 `prevented quantity`。这将使可用数量较少的订单过期， 如果两个订单的可用数量相等，那么两个订单都将过期。

`TRANSFER` \- 如果订单来自同一账户，则行为与 `DECREMENT` 相同。如果订单来自不同账户且具有相同的 `tradeGroupId`，则除了 `DECREMENT` 的行为外，`最后被阻止的数量` 及其名义价值将在两个账户之间转移。

STP 行为通常仅由**吃单** 的 STP 模式决定。例外情况是，只有当挂单和吃单都指定 STP 模式为 `TRANSFER` 时，才会发生 STP `TRANSFER`。如果吃单指定 STP 模式为 `TRANSFER`，但挂单指定了不同的 STP 模式，则 STP 行为为 `DECREMENT`。

总结如下：

吃单 STP 模式| 挂单 STP 模式| 实际生效的 STP 模式  
---|---|---  
`TRANSFER`| `TRANSFER`| `TRANSFER`  
`TRANSFER`| `EXPIRE_MAKER`、`EXPIRE_TAKER`、`EXPIRE_BOTH`、`NONE`、`DECREMENT`| `DECREMENT`  
`EXPIRE_MAKER`、`EXPIRE_TAKER`、`EXPIRE_BOTH`、`NONE`、`DECREMENT`| 任意 STP 模式| 吃单的 STP 模式  
  
### 实际生效的 STP 模式如何返回？

当实际生效的 STP 模式与报告该订单下单时指定的模式不同时，该生效 STP 模式会在被阻止撮合（`prevented match`）的执行回报及订单响应中返回：

  * REST 和 WebSocket API 的 `FULL` 订单响应：`preventedMatches[]` 数组中每个条目内的 `effectiveSelfTradePreventionMode`。
  * 用户数据流 `executionReport`：`eV`。
  * FIX `ExecutionReport<8>`：标签 `25058 EffectiveSelfTradePreventionMode`。



该字段仅在实际生效的 STP 模式与报告所属订单指定的模式不同时才出现。如果订单所指定的模式即为实际生效的模式，则该字段省略。此字段永远不会被返回为 `NONE`。

每份报告都是针对其所属订单的模式进行比较，因此同一次被阻止的撮合可能产生吃单报告中无此字段、挂单报告中有此字段的情况，反之亦然。

### 什么是交易组 Id（Trade Group Id）?

属于同一 `tradeGroupId` 的账户被视为同一交易组。相同交易组成员提交的订单有 STP 资格。

每个账户可以从 `GET /api/v3/account`（REST API）或 `account.status`（WebSocket API）确认账户是否属于同一个 `tradeGroupId`。

`tradeGroupId` 也存在 `GET /api/v3/preventedMatches`（REST API）或 `myPreventedMatches`（WebSocket API）的响应中。

如果该值为 `-1`，这表示账户未设置 `tradeGroupId`，因此 STP 只能发生在同一账户的订单之间。

### 什么是 Prevented Match?

当一个或多个订单因 STP 而过期时，这会创建一个被阻止的撮合交易。

当一个自我交易被阻止时，将会创建一个被阻止的撮合交易。隶属于被阻止的撮合交易中的订单会增加其 `prevented quantity` 然后导致一个或多个订单过期。

通过 REST API 的 `GET /api/v3/preventedMatches` 或 WebSocket API 的 `myPreventedMatches` 可以查询到有哪些被阻止的撮合交易。

请求的响应示例：
    
    
    Code
    
    [
      {
        symbol: "BTCDUSDT", // 交易对
        preventedMatchId: 8, // 被阻止撮合交易的Id
        takerOrderId: 12, // 吃单者的订单Id
        makerOrderId: 10, // 挂单者的订单Id
        tradeGroupId: 1, // 交易组的Id。（如果账户不属于交易组，则为 -1）
        selfTradePreventionMode: "EXPIRE_BOTH", // 订单过期的 STP 模式。
        price: "50.00000000", // 撮合交易的价格。
        takerPreventedQuantity: "1.00000000", // 在STP 前， 吃单者的剩余数量。 仅在 STP 模式为 EXPIRE_TAKER 或 EXPIRE_BOTH 或 DECREMENT 时出现。
        makerPreventedQuantity: "10.00000000", // 在STP 前， 挂单者的剩余数量。 仅在 STP 模式为 EXPIRE_MAKER 或 EXPIRE_BOTH 或 DECREMENT 时出现。
        transactTime: 1663190634060, // 订单因 STP 而过期的时间。
      },
    ];

### 什么是 "prevented quantity"?

STP事件会导致挂单的数量失效； STP的模式 `EXPIRE_TAKER`， `EXPIRE_MAKER` 以及 `EXPIRE_BOTH` 会使挂单中剩余的数量全部失效，从而使整个订单失效。

`Prevented quantity` 表示订单中因为STP事件失效的数量， 用户WebSocket数据流中可能有如下两个字段：
    
    
    Code
    
    {
      "A":"3.000000", // Prevented Quantity
      "B":"3.000000"  // Last Prevented Quantity
    }

`B` 代表着 `TRADE_PREVENTION` 交易类型， 其值表示本次STP事件导致失效的订单数量。

`A` 代表着某订单因为STP事件导致的累计失效订单数量。 对于 `EXPIRE_TAKER`， `EXPIRE_MAKER` 以及 `EXPIRE_BOTH` 模式, 其值总是和 `B` 一样。

由于 STP 而过期的订单的 API 响应也将有一个 `preventedQuantity` 字段，指示在订单由于 STP 而过期的累计数量。

如果订单是处于挂单状态, 如下的公式成立:
    
    
    Code
    
    original order quantity - executed quantity - prevented quantity = quantity available for further execution
    原始的订单数量 - 执行的订单数量 - 被过期的数量 = 可用于未来执行的数量

当一个订单的可用数量归 0 时，该订单会被从订单簿中移除。 这个状态会是 `EXPIRED_IN_MATCH`，`FILLED`， 或 `EXPIRED` 模式中的一个。

### 如何知道有那些交易对支持 STP?

交易对可以配置为允许不同的 STP 模式集并采用不同的默认 STP 模式。

`defaultSelfTradePreventionMode` \- 如果用户在下单时不提供，订单将使用此 STP 模式。

`allowedSelfTradePreventionModes` \- 交易对允许的下单 STP 模式集。

例如，如果交易对有以下配置：
    
    
    Code
    
    "defaultSelfTradePreventionMode": "NONE",
    "allowedSelfTradePreventionModes": [
        "NONE",
        "EXPIRE_TAKER",
        "EXPIRE_BOTH"
      ]

这表示如果用户在没有提供 `selfTradePreventionMode` 的情况下发送订单，发送的订单有 `NONE` 的值。

如果用户想明确指定模式，可以传 `NONE`，`EXPIRE_TAKER`，或 `EXPIRE_BOTH`。

如果用户尝试为此交易对的订单指定 `EXPIRE_MAKER`，将会收到错误消息：
    
    
    Code
    
    {
      "code": -1013,
      "msg": "This symbol does not allow the specified self-trade prevention mode."
    }

### 如何知道订单因为 STP 而过期？

订单的状态会是 `EXPIRED_IN_MATCH`.

### STP 的一些示例

假设以下示例的所有订单都是在同一个账户下发送。

**情况 A - 用户发送一个带有 selfTradePreventionMode:`NONE` 的新订单，该订单将与订单簿上已有的另一个订单撮合。**
    
    
    Code
    
    Maker 订单: symbol=BTCUSDT side=BUY type=LIMIT quantity=1 price=1 selfTradePreventionMode=NONE
    Taker 订单: symbol=BTCUSDT side=SELL type=LIMIT quantity=1 price=1 selfTradePreventionMode=NONE

**结果:** : 没有 STP 被触发，订单会撮合。

Maker 订单的状态
    
    
    Code
    
    {
      "symbol": "BTCUSDT",
      "orderId": 2,
      "orderListId": -1,
      "clientOrderId": "FaDk4LPRxastaICEFE9YTf",
      "price": "1.000000",
      "origQty": "1.000000",
      "executedQty": "1.000000",
      "cummulativeQuoteQty": "1.000000",
      "status": "FILLED",
      "timeInForce": "GTC",
      "type": "LIMIT",
      "side": "BUY",
      "stopPrice": "0.000000",
      "icebergQty": "0.000000",
      "time": 1670217090310,
      "updateTime": 1670217090330,
      "isWorking": true,
      "workingTime": 1670217090310,
      "origQuoteOrderQty": "0.000000",
      "selfTradePreventionMode": "NONE"
    }

Taker 订单的状态
    
    
    Code
    
    {
      "symbol": "BTCUSDT",
      "orderId": 3,
      "orderListId": -1,
      "clientOrderId": "Ay48Vtpghnsvy6w8RPQEde",
      "transactTime": 1670207731263,
      "price": "1.000000",
      "origQty": "1.000000",
      "executedQty": "1.000000",
      "cummulativeQuoteQty": "1.000000",
      "status": "FILLED",
      "timeInForce": "GTC",
      "type": "LIMIT",
      "side": "SELL",
      "workingTime": 1670207731263,
      "fills": [
        {
          "price": "1.000000",
          "qty": "1.000000",
          "commission": "0.000000",
          "commissionAsset": "USDT",
          "tradeId": 1
        }
      ],
      "selfTradePreventionMode": "NONE"
    }

**情况 B - 用户发送带有`EXPIRE_MAKER` 的订单，该订单将与订单簿上已有的订单撮合。**
    
    
    Code
    
    Maker 订单 1: symbol=BTCUSDT side=BUY type=LIMIT quantity=1.2 price=1.2 selfTradePreventionMode=NONE
    Maker 订单 2: symbol=BTCUSDT side=BUY type=LIMIT quantity=1.3 price=1.1 selfTradePreventionMode=NONE
    Maker 订单 3: symbol=BTCUSDT side=BUY type=LIMIT quantity=8.1 price=1   selfTradePreventionMode=NONE
    Taker 订单 1: symbol=BTCUSDT side=SELL type=LIMIT quantity=3 price=1    selfTradePreventionMode=EXPIRE_MAKER

**结果:** : 由于 STP，订单簿上的订单将会过期，taker 订单将继续在订单簿。

Maker 订单 1
    
    
    Code
    
    {
      "symbol": "BTCUSDT",
      "orderId": 2,
      "orderListId": -1,
      "clientOrderId": "wpNzhSclc16pV8g5THIOR3",
      "price": "1.200000",
      "origQty": "1.200000",
      "executedQty": "0.000000",
      "cummulativeQuoteQty": "0.000000",
      "status": "EXPIRED_IN_MATCH",
      "timeInForce": "GTC",
      "type": "LIMIT",
      "side": "BUY",
      "stopPrice": "0.000000",
      "icebergQty": "0.000000",
      "time": 1670217957437,
      "updateTime": 1670217957498,
      "isWorking": true,
      "workingTime": 1670217957437,
      "origQuoteOrderQty": "0.000000",
      "selfTradePreventionMode": "NONE",
      "preventedMatchId": 0,
      "preventedQuantity": "1.200000"
    }

Maker 订单 2
    
    
    Code
    
    {
      "symbol": "BTCUSDT",
      "orderId": 3,
      "orderListId": -1,
      "clientOrderId": "ZT9emqia99V7x8B6FW0pFF",
      "price": "1.100000",
      "origQty": "1.300000",
      "executedQty": "0.000000",
      "cummulativeQuoteQty": "0.000000",
      "status": "EXPIRED_IN_MATCH",
      "timeInForce": "GTC",
      "type": "LIMIT",
      "side": "BUY",
      "stopPrice": "0.000000",
      "icebergQty": "0.000000",
      "time": 1670217957458,
      "updateTime": 1670217957498,
      "isWorking": true,
      "workingTime": 1670217957458,
      "origQuoteOrderQty": "0.000000",
      "selfTradePreventionMode": "NONE",
      "preventedMatchId": 1,
      "preventedQuantity": "1.300000"
    }

Maker 订单 3
    
    
    Code
    
    {
      "symbol": "BTCUSDT",
      "orderId": 4,
      "orderListId": -1,
      "clientOrderId": "8QZ3taGcU4gND59TxHAcR0",
      "price": "1.000000",
      "origQty": "8.100000",
      "executedQty": "0.000000",
      "cummulativeQuoteQty": "0.000000",
      "status": "EXPIRED_IN_MATCH",
      "timeInForce": "GTC",
      "type": "LIMIT",
      "side": "BUY",
      "stopPrice": "0.000000",
      "icebergQty": "0.000000",
      "time": 1670217957478,
      "updateTime": 1670217957498,
      "isWorking": true,
      "workingTime": 1670217957478,
      "origQuoteOrderQty": "0.000000",
      "selfTradePreventionMode": "NONE",
      "preventedMatchId": 2,
      "preventedQuantity": "8.100000"
    }

Taker 订单的响应
    
    
    Code
    
    {
      "symbol": "BTCUSDT",
      "orderId": 5,
      "orderListId": -1,
      "clientOrderId": "WRzbhp257NhZsIJW4y2Nri",
      "transactTime": 1670217957498,
      "price": "1.000000",
      "origQty": "3.000000",
      "executedQty": "0.000000",
      "cummulativeQuoteQty": "0.000000",
      "status": "NEW",
      "timeInForce": "GTC",
      "type": "LIMIT",
      "side": "SELL",
      "workingTime": 1670217957498,
      "fills": [],
      "preventedMatches": [
        {
          "preventedMatchId": 0,
          "makerOrderId": 2,
          "price": "1.200000",
          "makerPreventedQuantity": "1.200000"
        },
        {
          "preventedMatchId": 1,
          "makerOrderId": 3,
          "price": "1.100000",
          "makerPreventedQuantity": "1.300000"
        },
        {
          "preventedMatchId": 2,
          "makerOrderId": 4,
          "price": "1.000000",
          "makerPreventedQuantity": "8.100000"
        }
      ],
      "selfTradePreventionMode": "EXPIRE_MAKER"
    }

**情况 C - 用户发送带有`EXPIRE_TAKER` 的订单，该订单将与订单簿上已有的订单撮合。**
    
    
    Code
    
    Maker 订单 1: symbol=BTCUSDT side=BUY type=LIMIT quantity=1.2 price=1.2  selfTradePreventionMode=NONE
    Maker 订单 2: symbol=BTCUSDT side=BUY type=LIMIT quantity=1.3 price=1.1  selfTradePreventionMode=NONE
    Maker 订单 3: symbol=BTCUSDT side=BUY type=LIMIT quantity=8.1 price=1    selfTradePreventionMode=NONE
    Taker 订单 1: symbol=BTCUSDT side=SELL type=LIMIT quantity=3 price=1 selfTradePreventionMode=EXPIRE_TAKER

**结果:** : 已经在订单簿上的订单将保留，而taker订单将过期。

Maker 订单 1
    
    
    Code
    
    {
      "symbol": "BTCUSDT",
      "orderId": 2,
      "orderListId": -1,
      "clientOrderId": "NpwW2t0L4AGQnCDeNjHIga",
      "price": "1.200000",
      "origQty": "1.200000",
      "executedQty": "0.000000",
      "cummulativeQuoteQty": "0.000000",
      "status": "NEW",
      "timeInForce": "GTC",
      "type": "LIMIT",
      "side": "BUY",
      "stopPrice": "0.000000",
      "icebergQty": "0.000000",
      "time": 1670219811986,
      "updateTime": 1670219811986,
      "isWorking": true,
      "workingTime": 1670219811986,
      "origQuoteOrderQty": "0.000000",
      "selfTradePreventionMode": "NONE"
    }

Maker 订单 2
    
    
    Code
    
    {
      "symbol": "BTCUSDT",
      "orderId": 3,
      "orderListId": -1,
      "clientOrderId": "TSAmJqGWk4YTB2yA9p04UO",
      "price": "1.100000",
      "origQty": "1.300000",
      "executedQty": "0.000000",
      "cummulativeQuoteQty": "0.000000",
      "status": "NEW",
      "timeInForce": "GTC",
      "type": "LIMIT",
      "side": "BUY",
      "stopPrice": "0.000000",
      "icebergQty": "0.000000",
      "time": 1670219812007,
      "updateTime": 1670219812007,
      "isWorking": true,
      "workingTime": 1670219812007,
      "origQuoteOrderQty": "0.000000",
      "selfTradePreventionMode": "NONE"
    }

Maker 订单 3
    
    
    Code
    
    {
      "symbol": "BTCUSDT",
      "orderId": 4,
      "orderListId": -1,
      "clientOrderId": "L6FmpCJJP6q4hCNv4MuZDG",
      "price": "1.000000",
      "origQty": "8.100000",
      "executedQty": "0.000000",
      "cummulativeQuoteQty": "0.000000",
      "status": "NEW",
      "timeInForce": "GTC",
      "type": "LIMIT",
      "side": "BUY",
      "stopPrice": "0.000000",
      "icebergQty": "0.000000",
      "time": 1670219812026,
      "updateTime": 1670219812026,
      "isWorking": true,
      "workingTime": 1670219812026,
      "origQuoteOrderQty": "0.000000",
      "selfTradePreventionMode": "NONE"
    }

Taker 订单的状态
    
    
    Code
    
    {
      "symbol": "BTCUSDT",
      "orderId": 5,
      "orderListId": -1,
      "clientOrderId": "kocvDAi4GNN2y1l1Ojg1Ri",
      "price": "1.000000",
      "origQty": "3.000000",
      "executedQty": "0.000000",
      "cummulativeQuoteQty": "0.000000",
      "status": "EXPIRED_IN_MATCH",
      "timeInForce": "GTC",
      "type": "LIMIT",
      "side": "SELL",
      "stopPrice": "0.000000",
      "icebergQty": "0.000000",
      "time": 1670219812046,
      "updateTime": 1670219812046,
      "isWorking": true,
      "workingTime": 1670219812046,
      "origQuoteOrderQty": "0.000000",
      "selfTradePreventionMode": "EXPIRE_TAKER",
      "preventedMatchId": 0,
      "preventedQuantity": "3.000000"
    }

**情况 D - 用户发送带有`EXPIRE_BOTH` 的订单，该订单将与订单簿上已有的订单撮合。**
    
    
    Code
    
    Maker 订单: symbol=BTCUSDT side=BUY type=LIMIT quantity=1 price=1 selfTradePreventionMode=NONE
    Taker 订单: symbol=BTCUSDT side=SELL type=LIMIT quantity=3 price=1 selfTradePreventionMode=EXPIRE_BOTH

**结果:** 两个订单都将过期。

Maker 订单
    
    
    Code
    
    {
      "symbol": "BTCUSDT",
      "orderId": 2,
      "orderListId": -1,
      "clientOrderId": "2JPC8xjpLq6Q0665uYWAcs",
      "price": "1.000000",
      "origQty": "1.000000",
      "executedQty": "0.000000",
      "cummulativeQuoteQty": "0.000000",
      "status": "EXPIRED_IN_MATCH",
      "timeInForce": "GTC",
      "type": "LIMIT",
      "side": "BUY",
      "stopPrice": "0.000000",
      "icebergQty": "0.000000",
      "time": 1673842412831,
      "updateTime": 1673842413170,
      "isWorking": true,
      "workingTime": 1673842412831,
      "origQuoteOrderQty": "0.000000",
      "selfTradePreventionMode": "NONE",
      "preventedMatchId": 0,
      "preventedQuantity": "1.000000"
    }

Taker 订单
    
    
    Code
    
    {
      "symbol": "BTCUSDT",
      "orderId": 5,
      "orderListId": -1,
      "clientOrderId": "qMaz8yrOXk2iUIz74cFkiZ",
      "transactTime": 1673842413170,
      "price": "1.000000",
      "origQty": "3.000000",
      "executedQty": "0.000000",
      "cummulativeQuoteQty": "0.000000",
      "status": "EXPIRED_IN_MATCH",
      "timeInForce": "GTC",
      "type": "LIMIT",
      "side": "SELL",
      "workingTime": 1673842413170,
      "fills": [],
      "preventedMatches": [
        {
          "preventedMatchId": 0,
          "makerOrderId": 2,
          "price": "1.000000",
          "takerPreventedQuantity": "3.000000",
          "makerPreventedQuantity": "1.000000"
        }
      ],
      "selfTradePreventionMode": "EXPIRE_BOTH",
      "tradeGroupId": 1,
      "preventedQuantity": "3.000000"
    }

**情况 E - 用户在订单簿上有一个带有`EXPIRE_MAKER` 的订单，然后发送一个带有 `EXPIRE_TAKER` 的新订单，该订单将与订单簿上的订单撮合。**
    
    
    Code
    
    Maker 订单: symbol=BTCUSDT side=BUY type=LIMIT quantity=1 price=1 selfTradePreventionMode=EXPIRE_MAKER
    Taker 订单: symbol=BTCUSDT side=SELL type=LIMIT quantity=1 price=1 selfTradePreventionMode=EXPIRE_TAKER

**结果:** 将使用 taker 订单的 STP 模式，因此 taker 订单将过期。

Maker 订单
    
    
    Code
    
    {
      "symbol": "BTCUSDT",
      "orderId": 0,
      "orderListId": -1,
      "clientOrderId": "jFUap8iFwwgqIpOfAL60GS",
      "price": "1.000000",
      "origQty": "1.000000",
      "executedQty": "0.000000",
      "cummulativeQuoteQty": "0.000000",
      "status": "NEW",
      "timeInForce": "GTC",
      "type": "LIMIT",
      "side": "BUY",
      "stopPrice": "0.000000",
      "icebergQty": "0.000000",
      "time": 1670220769261,
      "updateTime": 1670220769261,
      "isWorking": true,
      "workingTime": 1670220769261,
      "origQuoteOrderQty": "0.000000",
      "selfTradePreventionMode": "EXPIRE_MAKER"
    }

Taker 订单
    
    
    Code
    
    {
      "symbol": "BTCUSDT",
      "orderId": 1,
      "orderListId": -1,
      "clientOrderId": "zxrvnNNm1RXC3rkPLUPrc1",
      "transactTime": 1670220800315,
      "price": "1.000000",
      "origQty": "1.000000",
      "executedQty": "0.000000",
      "cummulativeQuoteQty": "0.000000",
      "status": "EXPIRED_IN_MATCH",
      "timeInForce": "GTC",
      "type": "LIMIT",
      "side": "SELL",
      "workingTime": 1670220800315,
      "fills": [],
      "preventedMatches": [
        {
          "preventedMatchId": 0,
          "makerOrderId": 0,
          "price": "1.000000",
          "takerPreventedQuantity": "1.000000"
        }
      ],
      "selfTradePreventionMode": "EXPIRE_TAKER",
      "preventedQuantity": "1.000000"
    }

**情况 F - 用户发送带有`EXPIRE_MAKER` 的市价订单，该订单将与订单簿上已有的订单撮合。**
    
    
    Code
    
    Maker 订单: symbol=BTCUSDT side=BUY type=LIMIT quantity=1 price=1  selfTradePreventionMode=NONE
    Taker 订单: symbol=BTCUSDT side=SELL type=MARKET quantity=1 selfTradePreventionMode=EXPIRE_MAKER

**结果:** 由于 STP，订单簿上的订单会过期，状态为 `EXPIRED_IN_MATCH`。由于订单簿上的流动性低，新订单也已过期但状态为 `EXPIRED`。

Maker 订单
    
    
    Code
    
    {
      "symbol": "BTCUSDT",
      "orderId": 2,
      "orderListId": -1,
      "clientOrderId": "7sgrQQInL69XDMQpiqMaG2",
      "price": "1.000000",
      "origQty": "1.000000",
      "executedQty": "0.000000",
      "cummulativeQuoteQty": "0.000000",
      "status": "EXPIRED_IN_MATCH",
      "timeInForce": "GTC",
      "type": "LIMIT",
      "side": "BUY",
      "stopPrice": "0.000000",
      "icebergQty": "0.000000",
      "time": 1670222557456,
      "updateTime": 1670222557478,
      "isWorking": true,
      "workingTime": 1670222557456,
      "origQuoteOrderQty": "0.000000",
      "selfTradePreventionMode": "NONE",
      "preventedMatchId": 0,
      "preventedQuantity": "1.000000"
    }

Taker 订单
    
    
    Code
    
    {
      "symbol": "BTCUSDT",
      "orderId": 3,
      "orderListId": -1,
      "clientOrderId": "zqhsgGDEcdhxy2oza2Ljxd",
      "transactTime": 1670222557478,
      "price": "0.000000",
      "origQty": "1.000000",
      "executedQty": "0.000000",
      "cummulativeQuoteQty": "0.000000",
      "status": "EXPIRED",
      "timeInForce": "GTC",
      "type": "MARKET",
      "side": "SELL",
      "workingTime": 1670222557478,
      "fills": [],
      "preventedMatches": [
        {
          "preventedMatchId": 0,
          "makerOrderId": 2,
          "price": "1.000000",
          "makerPreventedQuantity": "1.000000"
        }
      ],
      "selfTradePreventionMode": "EXPIRE_MAKER"
    }

**情况 G - 用户发送带有`DECREMENT` 的限价订单，该订单将与订单簿上已有的订单撮合。**
    
    
    Code
    
    Maker 订单： symbol=BTCUSDT side=BUY  type=LIMIT quantity=6 price=2  selfTradePreventionMode=NONE
    Taker 订单： symbol=BTCUSDT side=SELL type=LIMIT quantity=2 price=2  selfTradePreventionMode=DECREMENT

**结果:** 两个订单的 preventedQuantity 均为 2。 由于这是 Taker 订单的所有可用数量，此订单会因为 STP 而过期。

Maker 订单
    
    
    Code
    
    {
      "symbol": "BTCUSDT",
      "orderId": 23,
      "orderListId": -1,
      "clientOrderId": "Kxb4RpsBhfQrkK2r2YO2Z9",
      "price": "2.00000000",
      "origQty": "6.00000000",
      "executedQty": "0.00000000",
      "cummulativeQuoteQty": "0.00000000",
      "status": "NEW",
      "timeInForce": "GTC",
      "type": "LIMIT",
      "side": "BUY",
      "stopPrice": "0.00000000",
      "icebergQty": "0.00000000",
      "time": 1741682807892,
      "updateTime": 1741682816376,
      "isWorking": true,
      "workingTime": 1741682807892,
      "origQuoteOrderQty": "0.00000000",
      "selfTradePreventionMode": "DECREMENT",
      "preventedMatchId": 4,
      "preventedQuantity": "2.00000000"
    }

Taker 订单
    
    
    Code
    
    {
      "symbol": "BTCUSDT",
      "orderId": 24,
      "orderListId": -1,
      "clientOrderId": "dwf3qOzD7GM9ysDn9XG9AS",
      "price": "2.00000000",
      "origQty": "2.00000000",
      "executedQty": "0.00000000",
      "cummulativeQuoteQty": "0.00000000",
      "status": "EXPIRED_IN_MATCH",
      "timeInForce": "GTC",
      "type": "LIMIT",
      "side": "SELL",
      "stopPrice": "0.00000000",
      "icebergQty": "0.00000000",
      "time": 1741682816376,
      "updateTime": 1741682816376,
      "isWorking": true,
      "workingTime": 1741682816376,
      "origQuoteOrderQty": "0.00000000",
      "selfTradePreventionMode": "DECREMENT",
      "preventedMatchId": 4,
      "preventedQuantity": "2.00000000"
    }

**场景 H - 用户发送一个带有`TRANSFER` 的限价订单，该订单将与同一 `tradeGroupId` 下的现有订单匹配。**

下单前余额

Maker 余额
    
    
    Code
    
    {
      "balances": [
        {
          "asset": "BTC",
          "free": "20000.00000000",
          "locked": "0.00000000"
        },
        {
          "asset": "USDT",
          "free": "20000.00000000",
          "locked": "0.00000000"
        }
      ]
    }

Taker 余额
    
    
    Code
    
    {
      "balances": [
        {
          "asset": "BTC",
          "free": "20000.00000000",
          "locked": "0.00000000"
        },
        {
          "asset": "USDT",
          "free": "20000.00000000",
          "locked": "0.00000000"
        }
      ]
    }
    
    
    Code
    
    Maker Order: symbol=BTCUSDT side=BUY  type=LIMIT quantity=0.6 price=0.2  selfTradePreventionMode=TRANSFER tradeGroupId=1
    Taker Order: symbol=BTCUSDT side=SELL type=LIMIT quantity=0.2 price=0.2  selfTradePreventionMode=TRANSFER tradeGroupId=1

**结果：** 两个订单的 preventedQuantity 都为 0.2。由于这是吃单方的全部数量，该订单因 STP 而过期。

Maker 订单
    
    
    Code
    
    {
      "symbol": "BTCUSDT",
      "orderId": 12,
      "orderListId": -1,
      "clientOrderId": "zEyu9HGqiT5YUaXXhKr1MR",
      "price": "0.20000000",
      "origQty": "0.60000000",
      "executedQty": "0.00000000",
      "cummulativeQuoteQty": "0.00000000",
      "status": "NEW",
      "timeInForce": "GTC",
      "type": "LIMIT",
      "side": "BUY",
      "stopPrice": "0.00000000",
      "icebergQty": "0.00000000",
      "time": 1762852466582,
      "updateTime": 1762852522145,
      "isWorking": true,
      "workingTime": 1762852466582,
      "origQuoteOrderQty": "0.00000000",
      "selfTradePreventionMode": "TRANSFER",
      "preventedMatchId": 3,
      "preventedQuantity": "0.20000000"
    }

Taker 订单
    
    
    Code
    
    {
      "symbol": "BTCUSDT",
      "orderId": 13,
      "orderListId": -1,
      "clientOrderId": "6T06cph3Et2yFNnGpHdejh",
      "transactTime": 1762852522145,
      "price": "0.20000000",
      "origQty": "0.20000000",
      "executedQty": "0.00000000",
      "origQuoteOrderQty": "0.00000000",
      "cummulativeQuoteQty": "0.00000000",
      "status": "EXPIRED_IN_MATCH",
      "timeInForce": "GTC",
      "type": "LIMIT",
      "side": "SELL",
      "workingTime": 1762852522145,
      "fills": [],
      "preventedMatches": [
        {
          "preventedMatchId": 3,
          "makerSymbol": "BTCUSDT",
          "makerOrderId": 12,
          "price": "0.20000000",
          "takerPreventedQuantity": "0.20000000",
          "makerPreventedQuantity": "0.20000000"
        }
      ],
      "selfTradePreventionMode": "TRANSFER",
      "tradeGroupId": 1,
      "preventedQuantity": "0.20000000"
    }

触发STP后的余额

Maker 余额
    
    
    Code
    
    {
      "balances": [
        {
          "asset": "BTC",
          "free": "20000.20000000",
          "locked": "0.00000000"
        },
        {
          "asset": "USDT",
          "free": "19999.88000000",
          "locked": "0.08000000"
        }
      ]
    }

Taker 余额
    
    
    Code
    
    {
      "balances": [
        {
          "asset": "BTC",
          "free": "19999.80000000",
          "locked": "0.00000000"
        },
        {
          "asset": "USDT",
          "free": "20000.04000000",
          "locked": "0.00000000"
        }
      ]
    }

此页面是否有帮助？

Last modified on November 12, 2026

[现货交易API术语表](/zh-CN/docs/products/spot/faqs/spot_glossary)[追踪止盈止损(Trailing Stop)订单](/zh-CN/docs/products/spot/faqs/trailing-stop-faq)