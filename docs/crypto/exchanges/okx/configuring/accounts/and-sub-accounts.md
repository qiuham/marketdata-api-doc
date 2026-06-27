---
exchange: okx
source_url: https://www.okx.com/docs-v5/trick_en/#configuring-accounts-and-sub-accounts
anchor_id: configuring-accounts-and-sub-accounts
api_type: API
updated_at: 2026-01-15T17:46:44.130749
---

# Configuring accounts and sub-accounts

After creating sub-accounts and their API Keys, users can configure the master account and sub-accounts via the API before trading.

## Account config

The account config of each account/sub-account can be retrieved via the REST API as follows:

[`GET /api/v5/account/config`](/docs-v5/en/#trading-account-rest-api-get-account-configuration).

The API returns account mode, position mode, auto-borrow setting, and the Greeks type option, among additional account-related information.

## Account mode

In the Trading account trading system, 4 account modes are supported: Spot mode, Futures mode, Multi-currency margin mode, and Portfolio margin mode.

Users can only change these modes via the web or mobile app interface.

## Position 

There are 2 position modes as detailed below.

`net` mode: Positions can be held on one side only. Exchange will open/close the position automatically depending on the position (positive/negative) specified.

`long` and `short` mode: Positions can be held on both sides at the same time.

To change the position mode, users can invoke the following REST API:

[`POST /api/v5/account/set-position-mode`](/docs-v5/en/#trading-account-rest-api-set-position-mode)

Note: All positions must be closed with no pending orders to perform the switch.

## Auto-borrow

Auto-borrowing is only applicable in Multi-currency margin mode and Portfolio margin mode and can only be enabled or disabled via the web UI.

Exchange may automatically convert from the available balance in other currencies to repay the liability. The risk indicator can be found from the `twap` field in [`GET /api/v5/account/balance`](/docs-v5/en/#trading-account-rest-api-get-balance) and WS [`account`](/docs-v5/en/#trading-account-websocket-account-channel) endpoints.

## Option Greeks type

Users can set the option Greeks type via the endpoint below:

[`POST /api/v5/account/set-greeks`](/docs-v5/en/#trading-account-rest-api-set-greeks-pa-bs)