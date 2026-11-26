---
exchange: deribit
source_url: https://docs.deribit.com/api-reference/market-data/public-get_expirations
api_type: JSON-RPC
updated_at: 2026-11-26 19:02:05.286905
---

# public/get_expirations

> Retrieves expiration **labels** for listed futures and options. Values are instrument-style date strings such as `21SEP24`, or `PERPETUAL` for perpetuals — not Unix timestamps. Daily 08:00 UTC expirations are date-only; other expiration times include hour and minute.

Spots and combos are not included, even when `kind` is omitted or `"any"`.

`currency` is a settlement currency, `"any"`, or `"grouped"`:
- `"any"` — a flat map keyed by `future` / `option` (dates merged across currencies). This is the shape in the example.
- a named currency — `{ "<currency>": { "future": [...], "option": [...] } }` with a lowercase currency key (for example `btc`).
- `"grouped"` — the same nested shape for every tradable settlement currency.

If `currency` is omitted, `currency_pair` is used (default: all pairs). When `currency` is set, `currency_pair` is ignored. `kind` defaults to `"any"` (`future` and `option`); `"spot"`, `"future_combo"`, and `"option_combo"` are not useful filters here.

**📖 Related Article:** [Using the currency Parameter](https://docs.deribit.com/articles/currency-parameter)

[Try in API console](https://test.deribit.com/api_console?method=%2Fpublic%2Fget_expirations)


## OpenAPI

````yaml /specifications/deribit_openapi.json get /public/get_expirations
openapi: 3.0.0
info:
  title: Deribit API
  version: 2.1.1
servers:
  - url: https://test.deribit.com/api/v2
security: []
tags:
  - name: WebSocket Only
    description: Can only be used over websockets.
  - name: Public
    description: Public methods can be used without authentication.
  - name: Private
    description: >-
      <p>Private methods require authentication. All requests must include a
      valid OAuth2 token.</p>

      <p>A token can be requested using the <a
      href="#public-auth">/public/auth</a> method.</p>

      <p>When using the websockets protocol, the token must be included as a
      parameter <code>access_token</code> in the message. When using REST (HTTP
      GET), the token may also be passed in the <code>Authorization</code>
      header.</p>
  - name: Authentication
  - name: Session Management
  - name: Subscription Management
    description: >-
      Subscription works as [notifications](#notifications), so users will
      automatically (after subscribing) receive messages from the server.
      Overview for each channel response format is described in
      [subscriptions](#subscriptions) section.
  - name: Account Management
  - name: Trading
  - name: Market Data
  - name: Wallet
  - name: Chat
  - name: lsp
    description: >-
      Methods and notifications for the Liquidity Support Program (LSP), the
      mechanism that assigns risk from liquidated positions to designated LSP
      participant subaccounts before falling back to auto-deleveraging (ADL).
paths:
  /public/get_expirations:
    get:
      tags:
        - Market Data
        - Public
      description: >+
        Retrieves expiration **labels** for listed futures and options. Values
        are instrument-style date strings such as `21SEP24`, or `PERPETUAL` for
        perpetuals — not Unix timestamps. Daily 08:00 UTC expirations are
        date-only; other expiration times include hour and minute.


        Spots and combos are not included, even when `kind` is omitted or
        `"any"`.


        `currency` is a settlement currency, `"any"`, or `"grouped"`:

        - `"any"` — a flat map keyed by `future` / `option` (dates merged across
        currencies). This is the shape in the example.

        - a named currency — `{ "<currency>": { "future": [...], "option": [...]
        } }` with a lowercase currency key (for example `btc`).

        - `"grouped"` — the same nested shape for every tradable settlement
        currency.


        If `currency` is omitted, `currency_pair` is used (default: all pairs).
        When `currency` is set, `currency_pair` is ignored. `kind` defaults to
        `"any"` (`future` and `option`); `"spot"`, `"future_combo"`, and
        `"option_combo"` are not useful filters here.


        **📖 Related Article:** [Using the currency
        Parameter](https://docs.deribit.com/articles/currency-parameter)


        [Try in API
        console](https://test.deribit.com/api_console?method=%2Fpublic%2Fget_expirations)

      parameters:
        - name: currency
          required: false
          in: query
          schema:
            $ref: '#/components/schemas/settlement_currency_with_any_and_grouped'
          description: >
            The currency symbol or `"any"` for all or `"grouped"` for all
            grouped by currency. Optional; if omitted, `currency_pair` is used
            (default: all pairs).


            **📖 Related Article:** [Using the currency
            Parameter](https://docs.deribit.com/articles/currency-parameter)
        - name: kind
          required: false
          in: query
          schema:
            $ref: '#/components/schemas/kind_future_or_option_with_any'
          description: >-
            Instrument kind, `"future"` or `"option"` or `"any"` for both. If
            omitted, `"any"` is used. Spots and combos are not returned.
        - name: currency_pair
          required: false
          in: query
          schema:
            $ref: '#/components/schemas/index_name'
          description: The currency pair symbol
      requestBody:
        content:
          application/json:
            examples:
              request:
                summary: JSON-RPC Request Example
                value:
                  jsonrpc: '2.0'
                  id: 1
                  method: public/get_expirations
                  params:
                    currency: any
                    kind: any
        description: JSON-RPC request body
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PublicGetExpirationsResponse'
              examples:
                response:
                  summary: Response example
                  value:
                    jsonrpc: '2.0'
                    result:
                      future:
                        - 21SEP24
                        - 22SEP24
                        - PERPETUAL
                      option:
                        - 21SEP24
                        - 22SEP24
                        - 23SEP24
          description: Success response
      x-codeSamples:
        - lang: bash
          label: cURL
          source: |-
            curl --request POST \
              --url https://test.deribit.com/api/v2/public/get_expirations \
              --header 'Content-Type: application/json' \
              --data '{
              "jsonrpc": "2.0",
              "id": 1,
              "method": "public/get_expirations",
              "params": {
                "currency": "any",
                "kind": "any"
              }
            }'
components:
  schemas:
    settlement_currency_with_any_and_grouped:
      enum:
        - BTC
        - ETH
        - USDC
        - USDT
        - any
        - grouped
      type: string
      description: >-
        Currency name or `"any"` if don't care or `"grouped"` if grouped by
        currencies
    kind_future_or_option_with_any:
      enum:
        - future
        - option
        - any
      type: string
      description: 'Instrument kind: `"future"`, `"option"` or `"any"` for all'
    index_name:
      enum:
        - btc_usd
        - eth_usd
        - ada_usdc
        - algo_usdc
        - avax_usdc
        - bch_usdc
        - bnb_usdc
        - btc_usdc
        - btcdvol_usdc
        - buidl_usdc
        - doge_usdc
        - dot_usdc
        - eurr_usdc
        - eth_usdc
        - ethdvol_usdc
        - hype_usdc
        - link_usdc
        - ltc_usdc
        - near_usdc
        - paxg_usdc
        - shib_usdc
        - sol_usdc
        - steth_usdc
        - ton_usdc
        - trump_usdc
        - trx_usdc
        - uni_usdc
        - usde_usdc
        - usyc_usdc
        - xrp_usdc
        - btc_usdt
        - eth_usdt
        - eurr_usdt
        - sol_usdt
        - steth_usdt
        - usdc_usdt
        - usde_usdt
        - btc_eurr
        - btc_usde
        - btc_usyc
        - eth_btc
        - eth_eurr
        - eth_usde
        - eth_usyc
        - steth_eth
        - paxg_btc
        - drbfix-btc_usdc
        - drbfix-eth_usdc
      type: string
      description: Index identifier, matches (base) cryptocurrency with quote currency
    PublicGetExpirationsResponse:
      properties:
        jsonrpc:
          type: string
          enum:
            - '2.0'
          description: The JSON-RPC version (2.0)
        id:
          type: integer
          description: The id that was sent in the request
        result:
          $ref: '#/components/schemas/expirations'
      required:
        - result
        - jsonrpc
      type: object
    expirations:
      additionalProperties:
        oneOf:
          - items:
              type: string
            type: array
            description: Expiration labels when `currency=any`.
          - additionalProperties:
              items:
                type: string
              type: array
            type: object
            description: Kind → labels when grouping by currency.
      type: object
      description: >
        Expiration labels for futures and options. Not Unix timestamps. Each
        value is a string such as `21SEP24` or `PERPETUAL`.


        Shape depends on `currency`:

        - `"any"`: keys are `future` and/or `option`; values are lists of labels
        (merged across currencies).

        - a named settlement currency or `"grouped"`: keys are lowercase
        currency symbols (or a pair symbol when `currency_pair` was used);
        values are maps of kind → list of labels.

````

## Related topics

- [JSON-RPC API Changelog](https://docs.deribit.com/changelogs/jsonrpc.md)
- [Using the currency Parameter](https://docs.deribit.com/articles/currency-parameter.md)
- [Market Data Collection](https://docs.deribit.com/articles/market-data-collection-best-practices.md)
- [public/get_instrument](https://docs.deribit.com/api-reference/market-data/public-get_instrument.md)
- [public/get_instruments](https://docs.deribit.com/api-reference/market-data/public-get_instruments.md)