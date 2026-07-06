---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/payment-methods/get-payment-method
api_type: REST
updated_at: 2026-07-06 19:41:48.345079
---

# Get Payment Method

**Endpoint:** `GET https://api.coinbase.com/api/v3/brokerage/payment_methods/{payment_method_id}`


Get information about a payment method for the current user.
    
    
    curl --request GET \
      --url https://api.coinbase.com/api/v3/brokerage/payment_methods/{payment_method_id} \
      --header 'Authorization: Bearer <token>'
    
    
    {
      "payment_method": {
        "id": "8bfc20d7-f7c6-4422-bf07-8243ca4169fe",
        "type": "ACH",
        "name": "ALLY BANK ******1234",
        "currency": "USD",
        "verified": true,
        "allow_buy": true,
        "allow_sell": true,
        "allow_deposit": true,
        "allow_withdraw": true,
        "created_at": "2021-05-31T09:59:59.000Z",
        "updated_at": "2021-05-31T09:59:59.000Z"
      }
    }

#### Authorizations

Authorization

string

header

required

A JWT signed using your CDP API Key Secret, encoded in base64. Refer to the [Creating API Keys](/coinbase-app/authentication-authorization/api-key-authentication) section of our Coinbase App Authentication docs for information on how to generate your Bearer Token.

#### Path Parameters

payment_method_id

string

required

The ID of the payment method. Refer to [List Payment Methods](https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_getpaymentmethods/) for the list of all available payment methods and their corresponding IDs.

#### Response

A successful response.

payment_method

object