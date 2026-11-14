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
source_url: 'https://docs.kraken.com/exchange/api-reference/futures-websocket/balances'
updated_at: 2026-11-13
---

# Balances

> Subscribe to balance information for holding, single collateral, and multi-collateral wallets

WSS
futures.kraken.com/ws/v1
balances

> [!WARNING]
>
> **Derivatives WebSocket is being deprecated.** For new integrations, use the
> [Unified WebSocket](https://docs.kraken.com/exchange/api-reference/unified-websocket), which streams
> Spot and Derivatives over a single connection. Existing integrations continue
> to work until **1 March 2027**, when the Derivatives WebSocket will no
> longer be available. Migrate to the Unified WebSocket before then.
>
> To use private channels or trade on the Unified WebSocket, you need a
> Kraken API key, not a Derivatives API key. Use it to get a token from
> [`GetWebSocketsToken`](https://docs.kraken.com/api-reference/trading/get-websockets-token). See
> [Unified WebSocket authentication](https://docs.kraken.com/exchange/api-reference/unified-websocket#authentication).

This feed returns balance information for holding wallets, single collateral wallets and multi-collateral wallets.

***

## Request

**event** `string` *required*

`subscribe` or `unsubscribe`

**feed** `string` *required*

The requested subscription feed. Value: `balances`

**api\_key** `string` *required*

The user API key.

**original\_challenge** `string` *required*

The message that is received from a challenge request.

**signed\_challenge** `string` *required*

The signed challenge message with user API secret.

```json Example theme={null}
{
  "event": "subscribe",
  "feed": "balances",
  "api_key": "drUfSSmBbDpcIpwpqK0OBTcGLdAYZJU+NlPIsHaKspu/8feT2YSKl+Jw",
  "original_challenge": "c094497e-9b5f-40da-a122-3751c39b107f",
  "signed_challenge": "Ds0wtsHaXlAby/Vnoil59Q+yJIrJwZGUlgECD3+qEvFcTFfacJi2LrSRzAoqwBAeZk4pGXSmyyIW0uDymZ3olw=="
}
```

***

## Response Success

**event** `string`

One of: `subscribed`, `subscribed_failed`, `unsubscribed`, `unsubscribed_failed`

The result.

**feed** `string`

The requested subscription feed. Value: `balances`

**api\_key** `string`

The user API key.

**original\_challenge** `string`

The message that is received from a challenge request.

**signed\_challenge** `string`

The signed challenge message with user API secret.

```json Example theme={null}
{
  "event": "subscribed",
  "feed": "balances"
}
```

***

## Balances Snapshot

**feed** `string`

The subscribed feed.

**account** `string`

The user account.

**timestamp** `positive integer`

The unix timestamp of the balance state in milliseconds.

**seq** `positive integer`

The subscription message sequence number.

**holding** `map of floats`

A map from currency names to balance quantity.

**properties**

**name** `string`

The name of the account.

**pair** `string`

The wallet currency pair.

**unit** `string`

The wallet settlement unit.

**portfolio\_value** `float`

The current balance with haircuts and any unrealized margin from open positions in settlement units.

**balance** `float`

The current balance in settlement units.

**maintenance\_margin** `positive float`

The maintenance margin for open positions.

**initial\_margin** `float`

The initial margin for open positions and open orders.

**available** `float`

The current portfolio value minus initial margin.

**unrealized\_funding** `positive float`

The total unrealized funding for open positions.

**pnl** `positive float`

The total profit and loss for open positions.

**cash\_value** `float`

The cash value of the single collateral wallet in USD.

**futures** `map of structures`

A map from single collateral wallet names to collateral wallet structure.

**properties**

**name** `string`

The name of the account.

**pair** `string`

The wallet currency pair.

**unit** `string`

The wallet settlement unit.

**portfolio\_value** `float`

The current balance with haircuts and any unrealized margin from open positions in settlement units.

**balance** `float`

The current balance in settlement units.

**maintenance\_margin** `positive float`

The maintenance margin for open positions.

**initial\_margin** `float`

The initial margin for open positions and open orders.

**available** `float`

The current portfolio value minus initial margin.

**unrealized\_funding** `positive float`

The total unrealized funding for open positions.

**pnl** `positive float`

The total profit and loss for open positions.

**cash\_value** `float`

The cash value of the single collateral wallet in USD.

**flex\_futures** `structure`

The multi-collateral wallet structure.

**properties**

**balance\_value** `float`

The current USD balance of the account.

**portfolio\_value** `float`

The current collateral value with unrealized margin from any open positions.

**collateral\_value** `float`

The current USD balance with haircuts.

**initial\_margin** `float`

The total initial margin for open positions and open orders.

**initial\_margin\_without\_orders** `float`

The total initial margin for open positions.

**maintenance\_margin** `float`

The total maintenance margin for open positions.

**pnl** `float`

The total profit and loss for open positions.

**unrealized\_funding** `float`

The total unrealized funding for open positions.

**total\_unrealized** `float`

The total unrealized funding and pnl.

**total\_unrealized\_as\_margin** `float`

The total unrealized in USD.

**margin\_equity** `float`

The current collateral value and unrealized margin.

**available\_margin** `float`

The margin equity minus initial margin.

**total\_position\_size** `float`

Sum of all position sizes in USD.

**unified\_balances** `boolean`

True if the user has unified balances enabled, false if not.

**currencies** `map of structures`

A map from collateral wallet names to collateral wallet structure.

**properties**

**quantity** `float`

The currency quantity.

**value** `float`

The USD value of the currency balance.

**collateral\_value** `float`

The current USD balance with haircuts.

**available** `float`

The total available margin valued in the wallet currency.

**haircut** `float`

The rate of reduction in the value of a collateral asset that may be used as margin.

**conversion\_spread** `float`

The conversion spread is used to calculate conversion fee for multi-collateral wallets.

**isolated** `map of structures`

A map from collateral wallet names to collateral wallet structure.

**properties**

**initial\_margin** `float`

Initial margin for any position plus open orders.

**initial\_margin\_without\_orders** `float`

Initial margin for any position.

**maintenance\_margin** `float`

Maintenance margin for any position.

**pnl** `float`

Total profit and loss for any position.

**unrealized\_funding** `float`

Unrealized funding for any position.

**total\_unrealized** `float`

Unrealized funding plus pnl.

**total\_unrealized\_as\_margin** `float`

Total unrealized as USD.

**cross** `map of structures`

The current margin information for cross position(s).

**properties**

**initial\_margin** `float`

Initial margin for all positions plus open orders.

**initial\_margin\_without\_orders** `float`

Initial margin for all positions.

**maintenance\_margin** `float`

Maintenance margin for all positions.

**pnl** `float`

Total profit and loss for all positions.

**unrealized\_funding** `float`

Unrealized funding for all positions.

**total\_unrealized** `float`

Unrealized funding plus pnl.

**total\_unrealized\_as\_margin** `float`

Total unrealized as USD.

**balance\_value** `float`

Total USD balance minus initial margin of isolated positions.

**collateral\_value** `float`

USD balance, but with haircuts applied.

**portfolio\_value** `float`

USD balance plus total unrealized.

**margin\_equity** `float`

Collateral value plus total unrealized.

**available\_margin** `float`

Margin equity minus initial margin of cross and isolated positions.

**effective\_leverage** `float`

Ratio of position size to margin equity.

**total\_position\_size** `float`

Sum of all cross position sizes in USD.

**portfolio\_margin\_breakdown** `map of structures`

A breakdown of the portfolio margin calculation components.

**properties**

**market\_risk** `float`

Non-delta market risk of the portfolio.

**abs\_options\_delta** `float`

Absolute options delta of the portfolio.

**net\_position\_delta** `float`

Net position delta of the portfolio.

**futures\_maintenance\_margin** `float`

Total maintenance margin of all futures positions in the portfolio.

**futures\_cash\_value** `float`

Cash value sum total of the single collateral wallets in USD.

**futures\_upnl\_cash\_value** `float`

Cash value sum total with unrealized pnl of the single collateral wallets in USD.

```json Example theme={null}
{
  "feed": "balances_snapshot",
  "account": "4a012c31-df95-484a-9473-d51e4a0c4ae7",
  "holding": {
    "USDT": 4997.5012493753,
    "XBT": 0.1285407184,
    "ETH": 1.8714395862,
    "LTC": 47.6462740614,
    "GBP": 3733.488646461,
    "USDC": 5001.00020004,
    "USD": 5000.0,
    "BCH": 16.8924625832,
    "EUR": 4459.070194683,
    "XRP": 7065.5399485629
  },
  "futures": {
    "F-ETH:EUR": {
      "name": "F-ETH:EUR",
      "pair": "ETH/EUR",
      "unit": "EUR",
      "portfolio_value": 0.0,
      "balance": 0.0,
      "maintenance_margin": 0.0,
      "initial_margin": 0.0,
      "available": 0.0,
      "unrealized_funding": 0.0,
      "pnl": 0.0
    },
    "F-XBT:USD": {
      "name": "F-XBT:USD",
      "pair": "XBT/USD",
      "unit": "XBT",
      "portfolio_value": 0.0,
      "balance": 0.0,
      "maintenance_margin": 0.0,
      "initial_margin": 0.0,
      "available": 0.0,
      "unrealized_funding": 0.0,
      "pnl": 0.0
    }
  },
  "flex_futures": {
    "currencies": {
      "USDT": {
        "quantity": 0.0,
        "value": 0.0,
        "collateral_value": 0.0,
        "available": 0.0,
        "haircut": 0.0,
        "conversion_spread": 0.0
      },
      "USD": {
        "quantity": 0.0,
        "value": 0.0,
        "collateral_value": 0.0,
        "available": 0.0,
        "haircut": 0.0,
        "conversion_spread": 0.0
      }
    },
    "balance_value": 0.0,
    "portfolio_value": 0.0,
    "collateral_value": 0.0,
    "initial_margin": 0.0,
    "initial_margin_without_orders": 0.0,
    "maintenance_margin": 0.0,
    "pnl": 0.0,
    "unrealized_funding": 0.0,
    "total_unrealized": 0.0,
    "total_unrealized_as_margin": 0.0,
    "margin_equity": 0.0,
    "available_margin": 0.0,
    "isolated": {
      "PF_ETHUSD": {
        "initial_margin": 0.0,
        "initial_margin_without_orders": 0.0,
        "maintenance_margin": 0.0,
        "pnl": 0.0,
        "unrealized_funding": 0.0,
        "total_unrealized": 0.0,
        "total_unrealized_as_margin": 0.0
      }
    },
    "cross": {
      "balance_value": 9963.66,
      "portfolio_value": 9963.66,
      "collateral_value": 9963.66,
      "initial_margin": 0.0,
      "initial_margin_without_orders": 0.0,
      "maintenance_margin": 0.0,
      "pnl": 0.0,
      "unrealized_funding": 0.0,
      "total_unrealized": 0.0,
      "total_unrealized_as_margin": 0.0,
      "margin_equity": 9963.66,
      "available_margin": 9963.66,
      "effective_leverage": 0.0
    }
  },
  "timestamp": 1640995200000,
  "seq": 0
}
```

***

## Balances Delta

**feed** `string`

The subscribed feed.

**account** `string`

The user account.

**timestamp** `positive integer`

The unix timestamp of the balance state in milliseconds.

**seq** `positive integer`

The subscription message sequence number.

**holding** `optional map of floats`

A map from currency names to balance quantity.

**properties**

**name** `string`

The name of the account.

**pair** `string`

The wallet currency pair.

**unit** `string`

The wallet settlement unit.

**portfolio\_value** `float`

The current balance with haircuts and any unrealized margin from open positions in settlement units.

**balance** `float`

The current balance in settlement units.

**maintenance\_margin** `positive float`

The maintenance margin for open positions.

**initial\_margin** `float`

The initial margin for open positions and open orders.

**available** `float`

The current portfolio value minus initial margin.

**unrealized\_funding** `positive float`

The total unrealized funding for open positions.

**pnl** `positive float`

The total profit and loss for open positions.

**futures** `optional map of structures`

A map from single collateral wallet names to collateral wallet structure.

**properties**

**name** `string`

The name of the account.

**pair** `string`

The wallet currency pair.

**unit** `string`

The wallet settlement unit.

**portfolio\_value** `float`

The current balance with haircuts and any unrealized margin from open positions in settlement units.

**balance** `float`

The current balance in settlement units.

**maintenance\_margin** `positive float`

The maintenance margin for open positions.

**initial\_margin** `float`

The initial margin for open positions and open orders.

**available** `float`

The current portfolio value minus initial margin.

**unrealized\_funding** `positive float`

The total unrealized funding for open positions.

**pnl** `positive float`

The total profit and loss for open positions.

**flex\_futures** `optional structure`

The multi-collateral wallet structure.

**properties**

**balance\_value** `float`

The current USD balance of the account.

**portfolio\_value** `float`

The current collateral value with unrealized margin from any open positions.

**collateral\_value** `float`

The current USD balance with haircuts.

**initial\_margin** `float`

The total initial margin for open positions and open orders.

**initial\_margin\_without\_orders** `float`

The total initial margin for open positions.

**maintenance\_margin** `float`

The total maintenance margin for open positions.

**pnl** `float`

The total profit and loss for open positions.

**unrealized\_funding** `float`

The total unrealized funding for open positions.

**total\_unrealized** `float`

The total unrealized funding and pnl.

**total\_unrealized\_as\_margin** `float`

The total unrealized in USD.

**margin\_equity** `float`

The current collateral value and unrealized margin.

**available\_margin** `float`

The margin equity minus initial margin.

**total\_position\_size** `float`

Sum of all position sizes in USD.

**unified\_balances** `boolean`

True if the user has unified balances enabled, false if not.

**currencies** `map of structures`

A map from collateral wallet names to collateral wallet structure.

**properties**

**quantity** `float`

The currency quantity.

**value** `float`

The USD value of the currency balance.

**collateral\_value** `float`

The current USD balance with haircuts.

**available** `float`

The total available margin valued in the wallet currency.

**haircut** `float`

The rate of reduction in the value of a collateral asset that may be used as margin.

**conversion\_spread** `float`

The conversion spread is used to calculate conversion fee for multi-collateral wallets.

**isolated** `map of structures`

A map from collateral wallet names to collateral wallet structure.

**properties**

**initial\_margin** `float`

Initial margin for any position plus open orders.

**initial\_margin\_without\_orders** `float`

Initial margin for any position.

**maintenance\_margin** `float`

Maintenance margin for any position.

**pnl** `float`

Total profit and loss for any position.

**unrealized\_funding** `float`

Unrealized funding for any position.

**total\_unrealized** `float`

Unrealized funding plus pnl.

**total\_unrealized\_as\_margin** `float`

Total unrealized as USD.

**cross** `map of structures`

The current margin information for cross position(s).

**properties**

**initial\_margin** `float`

Initial margin for all positions plus open orders.

**initial\_margin\_without\_orders** `float`

Initial margin for all positions.

**maintenance\_margin** `float`

Maintenance margin for all positions.

**pnl** `float`

Total profit and loss for all positions.

**unrealized\_funding** `float`

Unrealized funding for all positions.

**total\_unrealized** `float`

Unrealized funding plus pnl.

**total\_unrealized\_as\_margin** `float`

Total unrealized as USD.

**balance\_value** `float`

Total USD balance minus initial margin of isolated positions.

**collateral\_value** `float`

USD balance, but with haircuts applied.

**portfolio\_value** `float`

USD balance plus total unrealized.

**margin\_equity** `float`

Collateral value plus total unrealized.

**available\_margin** `float`

Margin equity minus initial margin of cross and isolated positions.

**effective\_leverage** `float`

Ratio of position size to margin equity.

**total\_position\_size** `float`

Sum of all cross position sizes in USD.

```json Example: Holding Wallet Delta theme={null}
{
  "feed": "balances",
  "account": "7a641082-55c7-4411-a85f-930ec2e09617",
  "holding": {
    "USD": 5000.0
  },
  "futures": {},
  "timestamp": 1640995200000,
  "seq": 83
}
```

```json Example: Multi-Collateral Delta theme={null}
{
  "feed": "balances",
  "account": "7a641082-55c7-4411-a85f-930ec2e09617",
  "flex_futures": {
    "currencies": {
      "USD": { "quantity": 5000.0, "value": 5000.0, "collateral_value": 5000.0, "available": 5000.0, "haircut": 0.0, "conversion_spread": 0.0 }
    },
    "balance_value": 5000.0,
    "portfolio_value": 5000.0,
    "collateral_value": 5000.0,
    "initial_margin": 0.0,
    "initial_margin_without_orders": 0.0,
    "maintenance_margin": 0.0,
    "pnl": 0.0,
    "unrealized_funding": 0.0,
    "total_unrealized": 0.0,
    "total_unrealized_as_margin": 0.0,
    "margin_equity": 5000.0,
    "available_margin": 5000.0,
    "isolated": {},
    "cross": {
      "balance": 0.0,
      "portfolio_value": 0.0,
      "collateral_value": 0.0,
      "initial_margin": 0.0,
      "initial_margin_without_orders": 0.0,
      "maintenance_margin": 0.0,
      "pnl": 0.0,
      "unrealized_funding": 0,
      "total_unrealized": 0.0,
      "total_unrealized_as_margin": 0.0,
      "margin_equity": 0.0,
      "available_margin": 0.0,
      "effective_leverage": 0.0
    }
  },
  "timestamp": 1640995200000,
  "seq": 1
}
```

```json Example: Single-Collateral Delta theme={null}
{
  "feed": "balances",
  "account": "7a641082-55c7-4411-a85f-930ec2e09617",
  "holding": {},
  "futures": {
    "F-XBT:USD": {
      "name": "F-XBT:USD",
      "pair": "XBT/USD",
      "unit": "XBT",
      "portfolio_value": 0.1219368845,
      "balance": 0.1219368845,
      "maintenance_margin": 0.0,
      "initial_margin": 0.0,
      "available": 0.1219368845,
      "unrealized_funding": 0.0,
      "pnl": 0.0
    }
  },
  "timestamp": 1640995200000,
  "seq": 2
}
```

***

## Response Error

**event** `string`

Value: `error`

**message** `string`

One of: `Invalid feed`, `Json Error`

An error message.

```json Example theme={null}
{
  "event": "error",
  "message": "Invalid feed"
}
```
