---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/oms/Fast-API/base-urls
api_type: Guide
updated_at: 2026-11-24 18:37:18.094236
---

# Environments and API base URLs

| Environment | Base URL                                  |
| ----------- | ----------------------------------------- |
| Production  | **https://www.binanceapis.com/oauth-api** |

Fast API does **not** use `X-MBX-APIKEY` or request signing. It authenticates over OAuth with a
Client ID and Client Secret.

## Remarks

1. When Link clients start to use oAuth, they will get their unique “Client ID” and “Client secret”.
2. When each User grants permission via oAuth, the Link client will get an unique “User’s open ID”
   and an "Access token".
3. Access token will be expired once the User’s API key is generated.
4. **Each user account** can only use the Fast API to connect with **Each Link client Once**.
5. Link client need to provide a public key for encrypting User’s API key, when requesting the API
   generation. Additionally, Link clients should be able to decrypt the API key package, and store
   it safely.
6. When Link client request to generate a user's API key, it should state clearly if this API key
   should have certain permission(s). In request params:

- enableTrade → whether to enable Spot & Margin Trading
- enableFutureTrade → whether to enable Futures Trading
- enableMargin → whether to enable Margin Loan, Repay and Transfer
- enableEuropeanOptions → whether to enable European Options Trading

7. To know if a user has a Futures account, Link client should use Oauth to check the user's
   status.and show the necessary Front end UI to allow the user to select. The standard Front end is
   provided as a SDK.

---

# Environments and API base URLs

| Environment | Base URL                                  |
| ----------- | ----------------------------------------- |
| Production  | **https://www.binanceapis.com/oauth-api** |

Fast API does **not** use `X-MBX-APIKEY` or request signing. It authenticates over OAuth with a
Client ID and Client Secret.

## Remarks

1. When Link clients start to use oAuth, they will get their unique “Client ID” and “Client secret”.
2. When each User grants permission via oAuth, the Link client will get an unique “User’s open ID”
   and an "Access token".
3. Access token will be expired once the User’s API key is generated.
4. **Each user account** can only use the Fast API to connect with **Each Link client Once**.
5. Link client need to provide a public key for encrypting User’s API key, when requesting the API
   generation. Additionally, Link clients should be able to decrypt the API key package, and store
   it safely.
6. When Link client request to generate a user's API key, it should state clearly if this API key
   should have certain permission(s). In request params:

- enableTrade → whether to enable Spot & Margin Trading
- enableFutureTrade → whether to enable Futures Trading
- enableMargin → whether to enable Margin Loan, Repay and Transfer
- enableEuropeanOptions → whether to enable European Options Trading

7. To know if a user has a Futures account, Link client should use Oauth to check the user's
   status.and show the necessary Front end UI to allow the user to select. The standard Front end is
   provided as a SDK.