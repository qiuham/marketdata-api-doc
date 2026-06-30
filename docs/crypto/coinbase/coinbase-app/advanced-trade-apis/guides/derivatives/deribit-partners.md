---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/coinbase-app/advanced-trade-apis/guides/derivatives/deribit-partners
api_type: Guide
updated_at: 2026-06-30 19:43:29.204827
---

# Deribit Registered Partners — Migration Guide

This is the migration guide for existing registered Deribit partners.

## Summary

Coinbase is integrating Deribit, with cutover on **September 9, 2026**. Your existing Deribit users are unaffected. They keep their Deribit accounts and credentials, and you keep receiving rebates from them. What changes is your new users — after cutover they arrive with Coinbase credentials. Therefore, you will need to cover a mix — existing users on Deribit credentials, new users on Coinbase credentials. This will require some integration work: route each user to the correct endpoint, and add the auth path for new (Coinbase) users.

## What changes — and what doesn’t

Cohort| What happens at cutover  
---|---  
**Your existing Deribit users**|  Unaffected. They keep their Deribit accounts, credentials, and UX. No migration. You keep receiving rebates from them.  
**Your new users (after cutover)**|  Can no longer self-serve at `deribit.com`. They onboard through Coinbase and arrive with Coinbase credentials.  
  
## Route per user

Existing and new users hold different credentials, so your integration selects the base URL and auth model per user, based on how they onboarded.

End-user cohort| Account type| Base URL (REST / WebSocket)| Auth model  
---|---|---|---  
**Existing users**|  Deribit-native| `https://www.deribit.com/api/v2` · `wss://www.deribit.com/ws/api/v2`| Deribit OAuth / Deribit API key  
**New users**|  Coinbase| `https://drb.coinbase.com/api/v2` · `wss://drb.coinbase.com/ws/api/v2`| Coinbase CDP key or OAuth2 via token exchange  
  
## Authentication

  * **Existing users** keep their native Deribit authentication (Deribit OAuth or Deribit API key) — unchanged from today.
  * **New users** authenticate with Coinbase credentials — either a CDP API key or OAuth2 — by calling `public/auth` to obtain a Deribit access token (HTTP) or an authenticated session (WebSocket).

**Tokens** — the following tokens are used in the authentication flows:

Token| What it is| Issued by| Lifetime| Reference  
---|---|---|---|---  
`cdp jwt`| short-lived JWT signed with the user’s CDP API key| you, signed locally| ~120s| [API key auth](/coinbase-app/authentication-authorization/api-key-authentication)  
`oauth2 access token`| the user’s Coinbase OAuth2 access token| `POST login.coinbase.com/oauth2/token`| 1 hour| [Access & refresh tokens](/coinbase-app/oauth2-integration/access-and-refresh-tokens)  
`deribit access token`| Deribit bearer token from `public/auth`, HTTP only; on WebSocket the socket itself is authenticated (no token)| Deribit `public/auth`| ~15m (HTTP) · ~50m session (WS)| [Deribit API docs](https://docs.deribit.com)  
  
**Authenticate over the transport you will use:** an HTTP token cannot authenticate a WebSocket, and vice versa.

### API Keys - Private Access Sequence

  * HTTP

  * WebSocket

![CDP API key HTTP authentication flow](https://mintcdn.com/coinbase-prod/A5C6GnUDQYs1tVJd/coinbase-app/advanced-trade-apis/guides/derivatives/images/auth-cdp-http.svg?fit=max&auto=format&n=A5C6GnUDQYs1tVJd&q=85&s=01dacfc9f9bf1082f63630ce381d7a00)

  * You create a JWT, no round-trip to Coinbase. See [creating a JWT](/coinbase-app/authentication-authorization/api-key-authentication#generating-a-jwt).
  * It lasts only ~120s, use a fresh JWT for every `public/auth` call.
  * You need to provide the Deribit access token on each private method call.
  * Refresh the Deribit access token every 15 minutes.

![CDP API key WebSocket authentication flow](https://mintcdn.com/coinbase-prod/A5C6GnUDQYs1tVJd/coinbase-app/advanced-trade-apis/guides/derivatives/images/auth-cdp-ws.svg?fit=max&auto=format&n=A5C6GnUDQYs1tVJd&q=85&s=da205794e4b2fb96d27d53a5c55fb828)

  * You create a JWT, no round-trip to Coinbase. See [creating a JWT](/coinbase-app/authentication-authorization/api-key-authentication#generating-a-jwt).
  * It lasts only ~120s, use a fresh JWT for every `public/auth` call.
  * When you call `public/auth` that authorizes the websocket session, no return token is needed to access private methods.
  * Refresh the websockets authentication before it expires (~50 minutes).

### OAuth2 - Private Access Sequence

  * HTTP

  * WebSocket

![OAuth2 HTTP authentication flow](https://mintcdn.com/coinbase-prod/A5C6GnUDQYs1tVJd/coinbase-app/advanced-trade-apis/guides/derivatives/images/auth-oauth2-http.svg?fit=max&auto=format&n=A5C6GnUDQYs1tVJd&q=85&s=edeeecd9516b905490e8e17475a23642)

  * Retrieve an OAuth2 access token from `POST login.coinbase.com/oauth2/token`.
  * It expires in 60 mins, use an unexpired OAuth2 access token with every `public/auth` call.
  * You need to provide the Deribit access token on each private method call.

For OAuth there are 2 separate refresh cycles:

  * Refresh the Deribit access token every 15 minutes.
  * Refresh the OAuth2 access token every 1 hour. `POST login.coinbase.com/oauth2/token` with `grant_type=refresh_token` and your refresh token; you get back a new access _and_ refresh token.

![OAuth2 WebSocket authentication flow](https://mintcdn.com/coinbase-prod/A5C6GnUDQYs1tVJd/coinbase-app/advanced-trade-apis/guides/derivatives/images/auth-oauth2-ws.svg?fit=max&auto=format&n=A5C6GnUDQYs1tVJd&q=85&s=051d7746684e34ffb42517e5548e2588)

  * Retrieve an OAuth2 access token from `POST login.coinbase.com/oauth2/token`.
  * It expires in 60 mins, use an unexpired OAuth2 access token with every `public/auth` call.
  * When you call `public/auth` that authorizes the websocket session, no return token is needed to access private methods.

For OAuth there are 2 separate refresh cycles:

  * Refresh the websockets authentication before it expires (~50 minutes).
  * Refresh the OAuth2 access token every 1 hour. `POST login.coinbase.com/oauth2/token` with `grant_type=refresh_token` and your refresh token; you get back a new access _and_ refresh token.

### Notes

  * **On WebSocket, the connection is the credential.** `public/auth` returns no token — private method calls are authorized by the authenticated socket itself. Re-send `public/auth` on the same socket to extend. If the socket drops, you’ll need to re-authenticate from scratch.
  * **Request`offline_access` to get a refresh token (OAuth2).** Coinbase only issues a refresh token if the `offline_access` scope was in your authorize request. Without it, the 1-hour access token cannot be refreshed and the user must re-authorize. See [OAuth2 scopes](/coinbase-app/oauth2-integration/scopes) and [access & refresh tokens](/coinbase-app/oauth2-integration/access-and-refresh-tokens).
  * **CDP keys can use Ed25519 or ECDSA algorithms.** Ed25519 is recommended and works with direct API calls. ECDSA keys are only required for legacy / third party SDKs.
  * **Send`public/auth` as a `POST` so credentials stay out of the URL.** Deribit accepts `public/auth` over both `GET` and `POST`; use `POST` so the CDP JWT or OAuth2 access token travels in the request body, not the query string — keeping it out of URLs, browser history, and access logs. See [OAuth2 security best practices](/coinbase-app/oauth2-integration/security-best-practices).

## Migration Checklist

1

Keep your existing Deribit integration as-is

Existing users are unaffected and rebates continue.

2

Add a per-user routing branch

Existing Deribit users → native Deribit; new Coinbase users → new Coinbase endpoints.

3

Implement the Coinbase auth path for new users

CDP key or OAuth2 via `public/auth` token exchange.

4

Validate the new path

Before onboarding live Coinbase-credentialed users.

5

Deribit Advanced Trading gateway is live

New Coinbase users can trade from **September 9, 2026**.

## Help

  * Further assistance and timing — your Coinbase account manager.
  * Method-level API detail — the [Advanced Trade API reference](/api-reference/advanced-trade-api/rest-api/introduction).
  * Best practices and detailed guides — [Deribit’s documentation](https://docs.deribit.com/articles/order-management-best-practices).