---
exchange: deribit
source_url: https://docs.deribit.com/articles/block-trading-api
api_type: Guide
updated_at: 2026-11-26 19:02:01.585407
---

# Block Trading

> Negotiate and execute Deribit Block Trades between two counterparties via API, including quote verification, approval, and settlement workflows.

This section explains how to execute Deribit Block Trades between two parties using the API. Block Trades allow for large trades to be executed off the order book at negotiated prices. Before calling any private method you must authenticate.

> [!NOTE]
>
> Please refer to [API Authentication Guide](https://docs.deribit.com/articles/authentication.md) for more information regarding authentication.

## Overview

Block trading on Deribit enables two parties to execute large trades directly with each other, bypassing the public order book. This is particularly useful for:

* Large institutional trades that might impact market prices
* Negotiated trades between known counterparties
* Complex multi-leg trades

Block Trades and Block RFQ trades can be distinguished from other trades in the API via the `block_trade_id` field, which can be seen in endpoints such as `get_last_trades_by_currency`.

## Prerequisites

* Both parties must have Deribit accounts
* API keys with `block_trade:read` scope (for verification) or `block_trade:read_write` scope (for execution)
* Agreement on trade parameters (instruments, prices, amounts, direction)
* Shared timestamp and nonce between parties

## Block Trade Workflow

Block Trades involve a two-party process:

1. **First party** calls [`private/verify_block_trade`](https://docs.deribit.com/api-reference/block-trade/private-verify_block_trade) to generate a signature
2. **Second party** calls [`private/execute_block_trade`](https://docs.deribit.com/api-reference/block-trade/private-execute_block_trade) with the signature to execute the trade

### Step 1: Verify Block Trade (First Party)

The initial party initiates the Block Trade by calling [`private/verify_block_trade`](https://docs.deribit.com/api-reference/block-trade/private-verify_block_trade) to generate a Block Trade signature based on provided parameters.

### Example Request

```json theme={null}
{
  "jsonrpc": "2.0",
  "method": "private/verify_block_trade",
  "params": {
    "timestamp": 1590485535899,
    "nonce": "bszyprbq",
    "role": "taker",
    "trades": [
      {
        "instrument_name": "BTC-PERPETUAL",
        "direction": "buy",
        "price": 8900.0,
        "amount": 200000
      },
      {
        "instrument_name": "BTC-28MAY20-9000-C",
        "direction": "buy",
        "amount": 5.0,
        "price": 0.0133
      }
    ]
  },
  "id": 1
}
```

### Parameters

* `timestamp` (required): Timestamp in milliseconds since the UNIX epoch, shared with the other party
* `nonce` (required): A unique nonce shared with the other party
* `role` (required): Either `"maker"` or `"taker"` - describes which role you want to be in the trade
* `trades` (required): Array of trade objects, each containing:
  * `instrument_name` (required): The instrument name
  * `direction` (required): `"buy"` or `"sell"` - **Note: direction is always from the maker's perspective**
  * `price` (required): The trade price
  * `amount` (required): The trade amount

> [!WARNING]
>
> **Important:** In the API, the `direction` field is always expressed from the maker's perspective. This means that when you accept a Block Trade as a taker, the direction shown in the API represents the opposite side of your trade. For example, if you are buying puts as a taker, the API will show the operation as a "sell put" (maker's perspective), and you will be verifying and accepting a "sell put" Block Trade.

### Response

```json theme={null}
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "signature": "1590485595899.1Mn52L_Q.lNyNBzXXo-_QBT_wDuMgnhA7uS9tBqdQ5TLN6rxbuoAiQhyaJYGJrm5IV_9enp9niY_x8D60AJLm3yEKPUY1Dv3T0TW0n5-ADPpJF7Fpj0eVDZpZ6QCdX8snBWrSJ0TtqevnO64RCBlN1dIm2T70PP9dlhiqPDAUYI4fpB1vLYI"
  }
}
```

The response contains a `signature` that must be shared with the second party.

### Step 2: Execute Block Trade (Second Party)

After receiving the signature, the second party is required to call [`private/execute_block_trade`](https://docs.deribit.com/api-reference/block-trade/private-execute_block_trade) with the same parameters as the first party in [`private/verify_block_trade`](https://docs.deribit.com/api-reference/block-trade/private-verify_block_trade) (only the `role` field should be set as the opposite of the first party).

### Example Request

```json theme={null}
{
  "jsonrpc": "2.0",
  "method": "private/execute_block_trade",
  "params": {
    "timestamp": 1590485535899,
    "nonce": "bszyprbq",
    "role": "maker",
    "trades": [
      {
        "instrument_name": "BTC-PERPETUAL",
        "direction": "sell",
        "price": 8900.0,
        "amount": 200000
      },
      {
        "instrument_name": "BTC-28MAY20-9000-C",
        "direction": "sell",
        "amount": 5.0,
        "price": 0.0133
      }
    ],
    "counterparty_signature": "1590485595899.1Mn52L_Q.lNyNBzXXo-_QBT_wDuMgnhA7uS9tBqdQ5TLN6rxbuoAiQhyaJYGJrm5IV_9enp9niY_x8D60AJLm3yEKPUY1Dv3T0TW0n5-ADPpJF7Fpj0eVDZpZ6QCdX8snBWrSJ0TtqevnO64RCBlN1dIm2T70PP9dlhiqPDAUYI4fpB1vLYI"
  },
  "id": 2
}
```

### Parameters

* `timestamp` (required): Must match the timestamp used in `verify_block_trade`
* `nonce` (required): Must match the nonce used in `verify_block_trade`
* `role` (required): Must be the opposite role of the first party (if first party was `"taker"`, second party must be `"maker"`)
* `trades` (required): Must match the trades array from `verify_block_trade`, but with opposite directions
* `counterparty_signature` (required): The signature received from the first party

After the call, the Block Trade is executed.

## Simulating Block Trades

Before executing a Block Trade, you can simulate it to check if it can be executed using [`private/simulate_block_trade`](https://docs.deribit.com/api-reference/block-trade/private-simulate_block_trade):

### Example Request

```json theme={null}
{
  "jsonrpc": "2.0",
  "method": "private/simulate_block_trade",
  "params": {
    "role": "maker",
    "trades": [
      {
        "instrument_name": "BTC-PERPETUAL",
        "direction": "buy",
        "price": 11624,
        "amount": 40
      },
      {
        "instrument_name": "BTC-9AUG19-10250-P",
        "direction": "buy",
        "amount": 1.2,
        "price": 0.0707
      }
    ]
  },
  "id": 3
}
```

This method checks if a Block Trade can be executed without actually executing it.

## Block Trade Approval Feature

Block Trade approval introduces an additional layer to the Block Trade verification process. When activated, it necessitates an additional approval from the user from a different API key before a Block Trade can be executed.

### Setting Up Block Trade Approval

To use the Block Trade approval feature, an additional API key setting feature called `enabled_feature: block_trade_approval` is required. This key has to be given to the broker/registered partner who performs the trades.

### Approval Workflow

When a trade is executed by a Registered Partner on behalf of any of the two clients (Client A and Client B), multiple things happen to clients with Block Trade approval enabled:

1. **Timer starts**: A 5-minute timer starts. If those 5 minutes pass without required approvals, the Block Trade will be rejected
2. **Email notification**: An email with a link pointing to a Block Trade approval window is sent
3. **Announcement**: An announcement about pending approval is displayed on top of their screen
4. **WebSocket event**: An event is transmitted on a `block_trade_confirmation` channel informing about a new pending trade
5. **Pop-up window**: A pop-up window emerges in the user interface displaying the structure of the trade, providing options to 'Approve' or 'Reject'

### Monitoring Pending Approvals

Clients can use the `block_trade_confirmation` channel to monitor their pending confirmations.

### Approving Block Trades via API

To approve a Block Trade, use [`private/approve_block_trade`](https://docs.deribit.com/api-reference/block-trade/private-approve_block_trade). To reject, use [`private/reject_block_trade`](https://docs.deribit.com/api-reference/block-trade/private-reject_block_trade). Timestamp, nonce, and role are required to select a Block Trade.

### Example Request - Approve Block Trade

```json theme={null}
{
  "jsonrpc": "2.0",
  "method": "private/approve_block_trade",
  "params": {
    "timestamp": 1590485535899,
    "nonce": "bszyprbq",
    "role": "taker"
  },
  "id": 5
}
```

### Example Request - Reject Block Trade

```json theme={null}
{
  "jsonrpc": "2.0",
  "method": "private/reject_block_trade",
  "params": {
    "timestamp": 1590485535899,
    "nonce": "bszyprbq",
    "role": "taker"
  },
  "id": 6
}
```

> [!WARNING]
>
> If any of the clients reject the trade, the Block Trade will be rejected. The approval must be done within 5 minutes, otherwise the trade will be automatically rejected.

## Invalidating Block Trade Signatures

If needed, you can invalidate a Block Trade signature using [`private/invalidate_block_trade_signature`](https://docs.deribit.com/api-reference/block-trade/private-invalidate_block_trade_signature):

```json theme={null}
{
  "jsonrpc": "2.0",
  "method": "private/invalidate_block_trade_signature",
  "params": {
    "timestamp": 1590485535899,
    "nonce": "bszyprbq"
  },
  "id": 10
}
```

## Restricted Block Trades Feature

The Restricted Block Trades feature limits the `block_trade:read` scope of the API key to block trades that have been made using this specific API key. This method can be employed to restrict the visibility of user private block trades with third parties to whom the user has provided their API key.

## Best Practices

* **Coordinate parameters**: Ensure both parties agree on timestamp, nonce, and all trade parameters before starting
* **Use unique nonces**: Generate unique nonces for each Block Trade to prevent replay attacks
* **Verify before executing**: Use `simulate_block_trade` to verify trades can be executed before the actual execution
* **Monitor pending approvals**: If using Block Trade approval, monitor the `block_trade_confirmation` channel for pending approvals
* **Handle timeouts**: Be aware of the 5-minute timeout for Block Trade approvals
* **Secure signature sharing**: Share signatures securely between parties
* **Check direction carefully**: Remember that direction is always from the maker's perspective

## Common Errors

* **Invalid signature**: The signature doesn't match the trade parameters
* **Mismatched parameters**: Timestamp, nonce, or trades don't match between parties
* **Wrong role**: The role specified doesn't match the expected role (must be opposite of counterparty)
* **Insufficient balance**: One party doesn't have sufficient balance or margin
* **Approval timeout**: Block Trade approval was not completed within 5 minutes
* **Invalid nonce**: The nonce has already been used or is invalid

## Related Methods

* [`private/simulate_block_trade`](https://docs.deribit.com/api-reference/block-trade/private-simulate_block_trade) - Check if a Block Trade can be executed
* [`private/get_block_trade`](https://docs.deribit.com/api-reference/block-trade/private-get_block_trade) - Get information about a specific Block Trade or Block RFQ trade
* [`private/get_block_trades`](https://docs.deribit.com/api-reference/block-trade/private-get_block_trades) - List Block Trades and Block RFQ trades
* [`private/approve_block_trade`](https://docs.deribit.com/api-reference/block-trade/private-approve_block_trade) - Approve a pending Block Trade
* [`private/reject_block_trade`](https://docs.deribit.com/api-reference/block-trade/private-reject_block_trade) - Reject a pending Block Trade
* [`private/invalidate_block_trade_signature`](https://docs.deribit.com/api-reference/block-trade/private-invalidate_block_trade_signature) - Invalidate a Block Trade signature


## Related topics

- [Access Scope](https://docs.deribit.com/articles/access-scope.md)
- [block_trade_confirmations ](https://docs.deribit.com/subscriptions/block-trade/block_trade_confirmations.md)
- [Voice Broker Trading API](https://docs.deribit.com/articles/voice-broker-trading-api.md)
- [block_trade_confirmations.(currency) ](https://docs.deribit.com/subscriptions/block-trade/block_trade_confirmationscurrency.md)
- [private/get_block_trade](https://docs.deribit.com/api-reference/block-trade/private-get_block_trade.md)