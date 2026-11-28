---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/binance-pay-merchant/introduction
api_type: Guide
updated_at: 2026-11-28 18:33:01.931722
---

# Merchant API References | Binance Pay

# What is the Binance Pay

Binance Pay is a contactless, borderless and secure cryptocurrency payment technology designed by
Binance. Binance Pay allows Binance customer to pay and get paid in crypto from your friends and
family worldwide.

# Scenarios

## Merchant Acquiring (C2B) - Payment by QR code

In this scenario, users are able to make payments by scanning QR Codes provided by Binance and shown
by merchants.

1. Merchants cooperate with Binance to get different QR Codes for different products. Merchants
   display QR Codes for users to scan.
2. Users open Binance APP and scan QR Codes.
3. Users confirm payments by entering passcode or by clicking “confirm” button
4. Binance notify Merchants and users the status of payments.

![img](/img/payment-api/BinancePay-Pay-QRCodeV2.png)

## Transfer or Send Cryptos (C2C)

In this scenario, users are able to request crypto from others which called "Collection" in 3rd
party application.

1. Binance user grants a 3rd party application the permission to initiate transfer with his/her
   Binance Pay
2. Binance user makes collection request from others in 3rd party application.
3. Users(Payer) open Binance APP and confirm the collection.
4. Binance notifies 3rd party application the status of the collection.

![img](/img/payment-api/BinancePay-Collection-Flow.png)

> - 3rd party application uses oauth authentication to initiate the collection request, please
>   contact Binance Merchant Operation (https://merchant.binance.com/en/help) to set up proper
>   permissions of oauth client and refer to
>   [Binance OAuth2 Integration](/docs/products/login/web-integration) for oauth integration.
> - Please refer to [Webhook Common Rules](webhook-common) for authentication of collection result
>   notification.
> - In case 3rd party application needs to query the collection result, please contact Binance
>   Merchant Operation (https://merchant.binance.com/en/help) to set up authentication credential
>   and refer to [API Common Rules](api-common) for usage of API identity key and secret key.

---

# Merchant API References | Binance Pay

# What is the Binance Pay

Binance Pay is a contactless, borderless and secure cryptocurrency payment technology designed by
Binance. Binance Pay allows Binance customer to pay and get paid in crypto from your friends and
family worldwide.

# Scenarios

## Merchant Acquiring (C2B) - Payment by QR code

In this scenario, users are able to make payments by scanning QR Codes provided by Binance and shown
by merchants.

1. Merchants cooperate with Binance to get different QR Codes for different products. Merchants
   display QR Codes for users to scan.
2. Users open Binance APP and scan QR Codes.
3. Users confirm payments by entering passcode or by clicking “confirm” button
4. Binance notify Merchants and users the status of payments.

![img](/img/payment-api/BinancePay-Pay-QRCodeV2.png)

## Transfer or Send Cryptos (C2C)

In this scenario, users are able to request crypto from others which called "Collection" in 3rd
party application.

1. Binance user grants a 3rd party application the permission to initiate transfer with his/her
   Binance Pay
2. Binance user makes collection request from others in 3rd party application.
3. Users(Payer) open Binance APP and confirm the collection.
4. Binance notifies 3rd party application the status of the collection.

![img](/img/payment-api/BinancePay-Collection-Flow.png)

> - 3rd party application uses oauth authentication to initiate the collection request, please
>   contact Binance Merchant Operation (https://merchant.binance.com/en/help) to set up proper
>   permissions of oauth client and refer to
>   [Binance OAuth2 Integration](/docs/products/login/web-integration) for oauth integration.
> - Please refer to [Webhook Common Rules](webhook-common) for authentication of collection result
>   notification.
> - In case 3rd party application needs to query the collection result, please contact Binance
>   Merchant Operation (https://merchant.binance.com/en/help) to set up authentication credential
>   and refer to [API Common Rules](api-common) for usage of API identity key and secret key.