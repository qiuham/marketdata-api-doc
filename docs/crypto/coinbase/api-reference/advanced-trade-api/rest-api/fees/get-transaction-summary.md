---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/fees/get-transaction-summary
api_type: REST
updated_at: 2026-06-29 19:44:46.327887
---

# Get Transaction Summary

**Endpoint:** `GET https://api.coinbase.com/api/v3/brokerage/transaction_summary`


Get a summary of transactions with fee tiers, total volume, and fees.
    
    
    curl --request GET \
      --url https://api.coinbase.com/api/v3/brokerage/transaction_summary \
      --header 'Authorization: Bearer <token>'
    
    
    {
      "total_fees": 25,
      "fee_tier": {
        "pricing_tier": "<$10k",
        "taker_fee_rate": "0.0010",
        "maker_fee_rate": "0.0020",
        "aop_from": "0",
        "aop_to": "10000",
        "volume_types_and_range": [
          {
            "volume_types": [
              "VOLUME_TYPE_SPOT",
              "VOLUME_TYPE_US_DERIVATIVES"
            ],
            "vol_from": "0",
            "vol_to": "50000"
          }
        ]
      },
      "margin_rate": 0.5,
      "goods_and_services_tax": {
        "rate": "<string>",
        "type": "INCLUSIVE"
      },
      "advanced_trade_only_volume": 1000,
      "advanced_trade_only_fees": 25,
      "coinbase_pro_volume": 1000,
      "coinbase_pro_fees": 25,
      "total_balance": "1000",
      "volume_breakdown": [
        {
          "volume_type": "VOLUME_TYPE_SPOT",
          "volume": 1000
        }
      ],
      "has_cost_plus_commission": false
    }

#### Authorizations

Authorization

string

header

required

A JWT signed using your CDP API Key Secret, encoded in base64. Refer to the [Creating API Keys](/coinbase-app/authentication-authorization/api-key-authentication) section of our Coinbase App Authentication docs for information on how to generate your Bearer Token.

#### Query Parameters

product_type

enum<string>

default:UNKNOWN_PRODUCT_TYPE

Only returns the orders matching this product type. By default, returns all product types.

Available options:

`UNKNOWN_PRODUCT_TYPE`,

`SPOT`,

`FUTURE`

contract_expiry_type

enum<string>

default:UNKNOWN_CONTRACT_EXPIRY_TYPE

Only returns the orders matching this contract expiry type. Only applicable if product_type is set to FUTURE.

Available options:

`UNKNOWN_CONTRACT_EXPIRY_TYPE`,

`EXPIRING`,

`PERPETUAL`

product_venue

enum<string>

default:UNKNOWN_VENUE_TYPE

Venue for product

Available options:

`UNKNOWN_VENUE_TYPE`,

`CBE`,

`FCM`,

`INTX`

#### Response

A successful response.

total_fees

number<double>

required

Total fees across assets, denoted in USD.

Example:

`25`

fee_tier

object

required

Description of maker and taker rates across all applicable fee tiers.

margin_rate

object

Margin rate, only applicable to product_type `FUTURE`.

Example:

`0.5`

goods_and_services_tax

object

advanced_trade_only_volume

number<double>

Advanced Trade volume (non-inclusive of Pro) across assets, denoted in USD.

Example:

`1000`

advanced_trade_only_fees

number<double>

Advanced Trade fees (non-inclusive of Pro) across assets, denoted in USD.

Example:

`25`

coinbase_pro_volume

number<double>

Coinbase Pro volume across assets, denoted in USD.

Example:

`1000`

coinbase_pro_fees

number<double>

Coinbase Pro fees across assets, denoted in USD.

Example:

`25`

total_balance

string

Total balance across assets and products, which is comprised of the sum of spot, intx, and fcm, and denoted in USD.

Example:

`"1000"`

volume_breakdown

object[]

Breakdown of volumes that contributed to the fee tier calculation.

Example:
    
    
    [  
      {  
        "volume_type": "VOLUME_TYPE_SPOT",  
        "volume": 1000  
      }  
    ]

has_cost_plus_commission

boolean

Indicates whether the user uses cost plus commission pricing model.

Example:

`false`