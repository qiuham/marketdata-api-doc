---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/futures-api/websocket/balances
api_type: WebSocket
updated_at: 2026-05-27 19:54:59.452389
---

# Balances

CHANNEL
**Endpoint:** `wss://futures.kraken.com/ws/v1`
    balances

This feed returns balance information for holding wallets, single collateral wallets and multi-collateral wallets.

## Request

  * Request Fields
  * Example

### MESSAGE BODY

**event** `string` *required*

`subscribe` or `unsubscribe`

**feed** `string` *required*

The requested subscription feed `balances`

**api_key** `string` *required*

The user api key

**original_challenge** `string` *required*

The message that is received from a challenge request

**signed_challenge** `string` *required*

The signed challenge message with user api secret
    
    
    {  
      "event": "subscribe",  
      "feed": "balances",  
      "api_key": "drUfSSmBbDpcIpwpqK0OBTcGLdAYZJU+NlPIsHaKspu/8feT2YSKl+Jw",  
      "original_challenge": "c094497e-9b5f-40da-a122-3751c39b107f",  
      "signed_challenge": "Ds0wtsHaXlAby/Vnoil59Q+yJIrJwZGUlgECD3+qEvFcTFfacJi2LrSRzAoqwBAeZk4pGXSmyyIW0uDymZ3olw=="  
    }  
    

## Response Success

  * Response Fields
  * Successful

### MESSAGE BODY

**event** `string`

The result, `subscribed` or `subscribed_failed` or `unsubscribed` or `unsubscribed_failed`

**feed** `string`

The requested subscription feed `balances`

**api_key** `string`

The user api key

**original_challenge** `string`

The message that is received from a challenge request

**signed_challenge** `string`

The signed challenge message with user api secret
    
    
    {  
      "event": "subscribed",  
      "feed": "balances"  
    }  
    

## Balances Snapshot

  * Response Fields
  * Subscription Snapshot Data

### MESSAGE BODY

**feed** `string`

The subscribed feed

**account** `string`

The user account

**timestamp** `positive integer`

The unix timestamp of the balance state in milliseconds.

**seq** `positive integer`

The subscription message sequence number.

**holding** `map of floats`

A map from currency names to balance quantity 

**name** `string`

The name of the account.

**pair** `string`

The wallet currency pair.

**unit** `string`

The wallet settlement unit.

**portfolio_value** `float`

The current balance with haircuts and any unrealized margin from open positions in settlement units.

**balance** `float`

The current balance in settlement units.

**maintenance_margin** `positive float`

The maintenance margin for open positions.

**initial_margin** `float`

The initial margin for open positions and open orders.

**available** `float`

The current portfolio value minus initial margin.

**unrealized_funding** `positive float`

The total unrealized funding for open positions.

**pnl** `positive float`

The total profit and loss for open positions.

**cash_value** `float`

The cash value of the single collateral wallet in USD.

**futures** `map of structures`

A map from single collateral wallet names to collateral wallet structure 

**name** `string`

The name of the account.

**pair** `string`

The wallet currency pair.

**unit** `string`

The wallet settlement unit.

**portfolio_value** `float`

The current balance with haircuts and any unrealized margin from open positions in settlement units.

**balance** `float`

The current balance in settlement units.

**maintenance_margin** `positive float`

The maintenance margin for open positions.

**initial_margin** `float`

The initial margin for open positions and open orders.

**available** `float`

The current portfolio value minus initial margin.

**unrealized_funding** `positive float`

The total unrealized funding for open positions.

**pnl** `positive float`

The total profit and loss for open positions.

**cash_value** `float`

The cash value of the single collateral wallet in USD.

**flex_futures** `structure`

The multi-collateral wallet structure 

**balance_value** `float`

The current USD balance of the account.

**portfolio_value** `float`

The current collateral value with unrealized margin from any open positions.

**collateral_value** `float`

The current USD balance with haircuts.

**initial_margin** `float`

The total initial margin for open positions and open orders.

**initial_margin_without_orders** `float`

The total initial margin for open positions.

**maintenance_margin** `float`

The total maintenance margin for open positions.

**pnl** `float`

The total profit and loss for open positions.

**unrealized_funding** `float`

The total unrealized funding for open positions.

**total_unrealized** `float`

The total unrealized funding and pnl.

**total_unrealized_as_margin** `float`

The total unrealized in USD.

**margin_equity** `float`

The current collateral value and unrealized margin.

**available_margin** `float`

The margin equity minus initial margin.

**total_position_size** `float`

Sum of all position sizes in USD.

**unified_balances** `boolean`

True if the user has unified balances enabled, false if not.

**currencies** `map of structures`

A map from collateral wallet names to collateral wallet structure 

**quantity** `float`

The currency quantity.

**value** `float`

The USD value of the currency balance.

**collateral_value** `float`

The current USD balance with haircuts.

**available** `float`

The total available margin valued in the wallet currency.

**haircut** `float`

The rate of reduction in the value of a collateral asset that may be used as margin.

**conversion_spread** `float`

The conversion spread is used to calculate conversion fee for multi-collateral wallets.

**isolated** `map of structures`

A map from collateral wallet names to collateral wallet structure 

**initial_margin** `float`

Initial margin for any position plus open orders.

**initial_margin_without_orders** `float`

Initial margin for any position.

**maintenance_margin** `float`

Maintenance margin for any position.

**pnl** `float`

Total profit and loss for any position.

**unrealized_funding** `float`

Unrealized funding for any position.

**total_unrealized** `float`

Unrealized funding plus pnl.

**total_unrealized_as_margin** `float`

Total unrealized as USD.

**cross** `map of structures`

The current margin information for cross position(s) 

**initial_margin** `float`

Initial margin for all positions plus open orders.

**initial_margin_without_orders** `float`

Initial margin for all position.

**maintenance_margin** `float`

Maintenance margin for all position.

**pnl** `float`

Total profit and loss for all position.

**unrealized_funding** `float`

Unrealized funding for all position.

**total_unrealized** `float`

Unrealized funding plus pnl.

**total_unrealized_as_margin** `float`

Total unrealized as USD.

**balance_value** `float`

Total USD balance minus initial margin of isolated positions.

**collateral_value** `float`

USD balance, but with haircuts applied.

**portfolio_value** `float`

USD balance plus total unrealized.

**margin_equity** `float`

Collateral value plus total unrealized.

**available_margin** `float`

Margin equity minus initial margin of cross and isolated positions.

**effective_leverage** `float`

Ratio of position size to margin equity.

**total_position_size** `float`

Sum of all cross position sizes in USD.

**portfolio_margin_breakdown** `map of structures`

A breakdown of the portfolio margin calculation components 

**market_risk** `float`

Non-delta market risk of the portfolio..

**abs_options_delta** `float`

Absolute options delta of the portfolio.

**net_position_delta** `float`

Net position delta of the portfolio.

**futures_maintenance_margin** `float`

Total maintenance margin of all futures positions in the portfolio.

**futures_cash_value** `float`

Cash value sum total of the single collateral wallets in USD.

**futures_upnl_cash_value** `float`

Cash value sum total with unrealized pnl of the single collateral wallets in USD.
    
    
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
          "GBP": {  
            "quantity": 0.0,  
            "value": 0.0,  
            "collateral_value": 0.0,  
            "available": 0.0,  
            "haircut": 0.0,  
            "conversion_spread": 0.0  
          },  
          "USDC": {  
            "quantity": 0.0,  
            "value": 0.0,  
            "collateral_value": 0.0,  
            "available": 0.0,  
            "haircut": 0.0,  
            "conversion_spread": 0.0  
          },  
          "XBT": {  
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
          },  
          "EUR": {  
            "quantity": 0.0,  
            "value": 0.0,  
            "collateral_value": 0.0,  
            "available": 0.0,  
            "haircut": 0.0,  
            "conversion_spread": 0.0  
          },  
          "ETH": {  
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
    

## Balances Delta

  * Response Fields
  * Holding Wallet Balance Delta
  * Multi-Collateral Balance Delta
  * Single-Collateral Balance Delta

### MESSAGE BODY

**feed** `string`

The subscribed feed

**account** `string`

The user account

**timestamp** `positive integer`

The unix timestamp of the balance state in milliseconds.

**seq** `positive integer`

The subscription message sequence number.

**holding** `optional map of float`

A map from currency names to balance quantity 

**name** `string`

The name of the account.

**pair** `string`

The wallet currency pair.

**unit** `string`

The wallet settlement unit.

**portfolio_value** `float`

The current balance with haircuts and any unrealized margin from open positions in settlement units.

**balance** `float`

The current balance in settlement units.

**maintenance_margin** `positive float`

The maintenance margin for open positions.

**initial_margin** `float`

The initial margin for open positions and open orders.

**available** `float`

The current portfolio value minus initial margin.

**unrealized_funding** `positive float`

The total unrealized funding for open positions.

**pnl** `positive float`

The total profit and loss for open positions.

**futures** `optional map of structures`

A map from single collateral wallet names to collateral wallet structure 

**name** `string`

The name of the account.

**pair** `string`

The wallet currency pair.

**unit** `string`

The wallet settlement unit.

**portfolio_value** `float`

The current balance with haircuts and any unrealized margin from open positions in settlement units.

**balance** `float`

The current balance in settlement units.

**maintenance_margin** `positive float`

The maintenance margin for open positions.

**initial_margin** `float`

The initial margin for open positions and open orders.

**available** `float`

The current portfolio value minus initial margin.

**unrealized_funding** `positive float`

The total unrealized funding for open positions.

**pnl** `positive float`

The total profit and loss for open positions.

**flex_futures** `optional structure`

The multi-collateral wallet structure 

**balance_value** `float`

The current USD balance of the account.

**portfolio_value** `float`

The current collateral value with unrealized margin from any open positions.

**collateral_value** `float`

The current USD balance with haircuts.

**initial_margin** `float`

The total initial margin for open positions and open orders.

**initial_margin_without_orders** `float`

The total initial margin for open positions.

**maintenance_margin** `float`

The total maintenance margin for open positions.

**pnl** `float`

The total profit and loss for open positions.

**unrealized_funding** `float`

The total unrealized funding for open positions.

**total_unrealized** `float`

The total unrealized funding and pnl.

**total_unrealized_as_margin** `float`

The total unrealized in USD.

**margin_equity** `float`

The current collateral value and unrealized margin.

**available_margin** `float`

The margin equity minus initial margin.

**total_position_size** `float`

Sum of all position sizes in USD.

**unified_balances** `boolean`

True if the user has unified balances enabled, false if not.

**currencies** `map of structures`

A map from collateral wallet names to collateral wallet structure 

**quantity** `float`

The currency quantity.

**value** `float`

The USD value of the currency balance.

**collateral_value** `float`

The current USD balance with haircuts.

**available** `float`

The total available margin valued in the wallet currency.

**haircut** `float`

The rate of reduction in the value of a collateral asset that may be used as margin.

**conversion_spread** `float`

The conversion spread is used to calculate conversion fee for multi-collateral wallets.

**isolated** `map of structures`

A map from collateral wallet names to collateral wallet structure 

**initial_margin** `float`

Initial margin for any position plus open orders.

**initial_margin_without_orders** `float`

Initial margin for any position.

**maintenance_margin** `float`

Maintenance margin for any position.

**pnl** `float`

Total profit and loss for any position.

**unrealized_funding** `float`

Unrealized funding for any position.

**total_unrealized** `float`

Unrealized funding plus pnl.

**total_unrealized_as_margin** `float`

Total unrealized as USD.

**cross** `map of structures`

The current margin information for cross position(s) 

**initial_margin** `float`

Initial margin for all positions plus open orders.

**initial_margin_without_orders** `float`

Initial margin for all position.

**maintenance_margin** `float`

Maintenance margin for all position.

**pnl** `float`

Total profit and loss for all position.

**unrealized_funding** `float`

Unrealized funding for all position.

**total_unrealized** `float`

Unrealized funding plus pnl.

**total_unrealized_as_margin** `float`

Total unrealized as USD.

**balance_value** `float`

Total USD balance minus initial margin of isolated positions.

**collateral_value** `float`

USD balance, but with haircuts applied.

**portfolio_value** `float`

USD balance plus total unrealized.

**margin_equity** `float`

Collateral value plus total unrealized.

**available_margin** `float`

Margin equity minus initial margin of cross and isolated positions.

**effective_leverage** `float`

Ratio of position size to margin equity.

**total_position_size** `float`

Sum of all cross position sizes in USD.
    
    
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
    
    
    
    {  
      "feed": "balances",  
      "account": "7a641082-55c7-4411-a85f-930ec2e09617",  
      "flex_futures": {  
        "currencies": {  
          "USDT": { "quantity": 0.0, "value": 0.0, "collateral_value": 0.0, "available": 0.0, "haircut": 0.0, "conversion_spread": 0.0 },  
          "GBP": { "quantity": 0.0, "value": 0.0, "collateral_value": 0.0, "available": 0.0, "haircut": 0.0, "conversion_spread": 0.0 },  
          "USDC": { "quantity": 0.0, "value": 0.0, "collateral_value": 0.0, "available": 0.0, "haircut": 0.0, "conversion_spread": 0.0 },  
          "XBT": { "quantity": 0.0, "value": 0.0, "collateral_value": 0.0, "available": 0.0, "haircut": 0.0, "conversion_spread": 0.0 },  
          "USD": { "quantity": 5000.0, "value": 5000.0, "collateral_value": 5000.0, "available": 5000.0, "haircut": 0.0, "conversion_spread": 0.0 },  
          "EUR": { "quantity": 0.0, "value": 0.0, "collateral_value": 0.0, "available": 0.0, "haircut": 0.0, "conversion_spread": 0.0 },  
          "ETH": { "quantity": 0.0, "value": 0.0, "collateral_value": 0.0, "available": 0.0, "haircut": 0.0, "conversion_spread": 0.0 }  
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
    

## Response Error

  * Response Fields
  * Example Error

### MESSAGE BODY

**event** `string`

Always error

**message** `string`

An error message out of:  
`Invalid feed`  
`Json Error`
    
    
    {  
      "event": "error",  
      "message": "Invalid feed"  
    }