---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/coinbase-app/advanced-trade-apis/guides/derivatives/intx-partners
api_type: Guide
updated_at: 2026-07-12 19:04:37.770643
---

# INTX Retail API Partners — Migration Guide

This is the migration guide for existing Coinbase INTX partners.

## Summary

Coinbase is moving international derivatives off INTX onto Deribit-backed endpoints, with cutover on **September 9, 2026**. INTX trading ends at cutover — migrate your integration before then to keep trading. You already authenticate with Coinbase CDP API keys or OAuth2, and those credentials carry over unchanged — no new keys to issue, no new end-user consent. To migrate, repoint to the new endpoints and add a single `public/auth` token-exchange call. The protocol moves from INTX REST to JSON-RPC 2.0 over HTTP and WebSocket. The [Technical Migration Guide](/coinbase-app/advanced-trade-apis/guides/derivatives/technical) is the full reference — protocol, base URLs, symbology, order types, and endpoint mapping. This guide covers what’s specific to you as an INTX partner.

## What changes

Area| Today (INTX)| After cutover  
---|---|---  
**Where you trade**|  Coinbase INTX| New Coinbase Deribit-backed endpoints  
**Protocol**|  REST| JSON-RPC 2.0 (over HTTP and WebSocket)  
**Auth credentials**|  CDP API key (JWT) or Coinbase OAuth2| Same credentials, preserved via a token-exchange step  
**WebSocket**|  Market data only| Full order lifecycle over WebSocket  
  
### Endpoints and URLs

The new surface speaks JSON-RPC 2.0 over both HTTP and WebSocket. WebSocket is the recommended transport for trading.

Surface| INTX (current)| Coinbase Deribit-backed  
---|---|---  
**REST**| `https://api.coinbase.com/api/v3/brokerage/intx/`| `https://drb.coinbase.com/api/v2`  
**WebSocket**| `wss://advanced-trade-ws.coinbase.com` (market data only)| `wss://drb.coinbase.com/ws/api/v2`  
  
One endpoint serves both trading and market data on the new surface, unlike INTX where market data is a separate socket.

## Authentication

Your users authenticate with their existing Coinbase credentials — either a CDP API key or OAuth2 — by calling `public/auth` to obtain a Deribit access token (HTTP) or an authenticated session (WebSocket). No new credentials, no new end-user consent. **Tokens** — the following tokens are used in the authentication flows:

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

The INTX to Deribit migration steps:

1

Repoint base URLs

`https://drb.coinbase.com/api/v2` (REST) and `wss://drb.coinbase.com/ws/api/v2` (WebSocket).

2

Add the token-exchange call

`public/auth` with the `coinbase_cdp` or `coinbase_oauth2` grant (see Authentication).

3

Restructure to JSON-RPC 2.0

`{jsonrpc, method, params, id}` envelope.

4

Re-map your endpoints

Replace each INTX REST path with its Deribit equivalent (see the [endpoint mapping](/coinbase-app/advanced-trade-apis/guides/derivatives/technical#endpoint-mapping) in the Technical Migration Guide).

5

Update symbology

`{BASE}-PERP-INTX` → `{BASE}_USDC-PERPETUAL` (discover exact names via `public/get_instruments`).

6

Deribit Advanced Trading gateway is live

Cut over on **September 9, 2026** , no parallel run. Repoint production traffic.

## Help

  * Further assistance and timing — your Coinbase account manager.
  * Method-level API detail — the [Advanced Trade API reference](/api-reference/advanced-trade-api/rest-api/introduction).
  * Best practices and detailed guides — [Deribit’s documentation](https://docs.deribit.com/articles/order-management-best-practices).