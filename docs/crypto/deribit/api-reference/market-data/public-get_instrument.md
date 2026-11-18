---
exchange: deribit
source_url: https://docs.deribit.com/api-reference/market-data/public-get_instrument
api_type: JSON-RPC
updated_at: 2026-11-18 05:09:04.998972
---

# public/get_instrument

> Retrieves detailed information about a specific instrument, including instrument specifications, contract details, tick size, settlement currency, expiration date (for futures and options), strike price (for options), underlying type, and other instrument parameters.

Looks up by `instrument_name`, including combo IDs and expired or archivized instruments that `public/get_instruments` no longer lists. Unknown names fail with `instrument not found`. For live combo legs and combo-book state, use `public/get_combo_details` / `public/get_combos` instead of this method.

`is_active` is true while the order book is visible (`open`, `settlement`, `locked`, or `halted`). It is not the same as tradable: only `state` `open` accepts new orders. After delivery the book becomes `delivered` (`is_active` false) and is later archivized.

Spot instruments omit `settlement_currency` and `settlement_period`. Spot routed to Coinbase Exchange also omit block-trade fields and include `is_cbe_routed` / `is_csr` (present only when `true`). Futures include `max_leverage` and `max_non_default_leverage`. Some USDC spot pairs that support margin loans also include `max_leverage`. Perpetuals still have `expiration_timestamp`.

**📖 Related Article:** [Spot Trading: Deribit and Coinbase-Routed Instruments](https://docs.deribit.com/articles/spot-trading-venues)

[Try in API console](https://test.deribit.com/api_console?method=%2Fpublic%2Fget_instrument)


## OpenAPI

````yaml /specifications/deribit_openapi.json get /public/get_instrument
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
  /public/get_instrument:
    get:
      tags:
        - Market Data
        - Public
      description: >+
        Retrieves detailed information about a specific instrument, including
        instrument specifications, contract details, tick size, settlement
        currency, expiration date (for futures and options), strike price (for
        options), underlying type, and other instrument parameters.


        Looks up by `instrument_name`, including combo IDs and expired or
        archivized instruments that `public/get_instruments` no longer lists.
        Unknown names fail with `instrument not found`. For live combo legs and
        combo-book state, use `public/get_combo_details` / `public/get_combos`
        instead of this method.


        `is_active` is true while the order book is visible (`open`,
        `settlement`, `locked`, or `halted`). It is not the same as tradable:
        only `state` `open` accepts new orders. After delivery the book becomes
        `delivered` (`is_active` false) and is later archivized.


        Spot instruments omit `settlement_currency` and `settlement_period`.
        Spot routed to Coinbase Exchange also omit block-trade fields and
        include `is_cbe_routed` / `is_csr` (present only when `true`). Futures
        include `max_leverage` and `max_non_default_leverage`. Some USDC spot
        pairs that support margin loans also include `max_leverage`. Perpetuals
        still have `expiration_timestamp`.


        **📖 Related Article:** [Spot Trading: Deribit and Coinbase-Routed
        Instruments](https://docs.deribit.com/articles/spot-trading-venues)


        [Try in API
        console](https://test.deribit.com/api_console?method=%2Fpublic%2Fget_instrument)

      parameters:
        - name: instrument_name
          required: true
          in: query
          schema:
            $ref: '#/components/schemas/instrument_name'
          description: Instrument name
      requestBody:
        content:
          application/json:
            examples:
              request:
                summary: JSON-RPC Request Example
                value:
                  jsonrpc: '2.0'
                  id: 2
                  method: public/get_instrument
                  params:
                    instrument_name: BTC-13JAN23-16000-P
        description: JSON-RPC request body
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PublicGetInstrumentResponse'
              examples:
                response:
                  summary: Response example
                  value:
                    jsonrpc: '2.0'
                    id: 2
                    result:
                      tick_size: 0.0005
                      tick_size_steps:
                        - above_price: 120
                          tick_size: 0.001
                        - above_price: 200
                          tick_size: 0.003
                      taker_commission: 0.0003
                      strike: 16000
                      settlement_period: week
                      settlement_currency: BTC
                      quote_currency: BTC
                      price_index: btc_usd
                      option_type: put
                      min_trade_amount: 0.1
                      maker_commission: 0.0003
                      kind: option
                      is_active: true
                      instrument_name: BTC-13JAN23-16000-P
                      instrument_id: 144613
                      expiration_timestamp: 1673596800000
                      creation_timestamp: 1671696002000
                      counter_currency: USD
                      contract_size: 1
                      lot_size: 1
                      block_trade_tick_size: 0.0001
                      block_trade_min_trade_amount: 25
                      block_trade_commission: 0.00015
                      base_currency: BTC
                      state: open
                      index_id: 1000033
                      product_group: BTC
                      underlying_type: crypto
          description: Success response
      x-codeSamples:
        - lang: bash
          label: cURL
          source: |-
            curl --request POST \
              --url https://test.deribit.com/api/v2/public/get_instrument \
              --header 'Content-Type: application/json' \
              --data '{
              "jsonrpc": "2.0",
              "id": 2,
              "method": "public/get_instrument",
              "params": {
                "instrument_name": "BTC-13JAN23-16000-P"
              }
            }'
components:
  schemas:
    instrument_name:
      example: BTC-PERPETUAL
      type: string
      description: Unique instrument identifier
    PublicGetInstrumentResponse:
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
          $ref: '#/components/schemas/instrument'
      required:
        - result
        - jsonrpc
      type: object
    instrument:
      properties:
        kind:
          $ref: '#/components/schemas/kind'
        settlement_currency:
          type: string
          description: >-
            Optional (omitted for spot). Settlement currency for the instrument.
            For inverse (reversed) contracts this is the base coin (e.g. BTC);
            for linear contracts it is typically the quote currency (e.g. USDC).
        counter_currency:
          type: string
          description: >-
            Counter currency of the instrument's currency pair (e.g. USD or
            USDC).
        base_currency:
          type: string
          description: >-
            The underlying currency being traded. Not limited to BTC/ETH —
            altcoins, RWAs, and other listed bases are returned as their
            currency symbol.
        quote_currency:
          type: string
          description: >-
            The currency in which the instrument prices are quoted. Inverse
            options and futures are typically quoted in USD; linear and spot
            instruments are typically quoted in USDC or the quote coin.
        min_trade_amount:
          type: number
          example: 0.1
          description: >
            Minimum amount for trading and the quantity increment (step size)
            for order amounts. For perpetual and inverse futures the amount is
            in USD units. For options and linear futures it is the underlying
            base currency coin.


            This is the JSON-RPC name for the Starbase quantity increment
            (`qty_tick_size` on Starbase REST, SBE `minOrderQuantity ×
            10^quantityExponent`). JSON-RPC does not return a `qty_tick_size`
            field. Distinct from `contract_size`; do not assume the two values
            are equal.
        instrument_name:
          $ref: '#/components/schemas/instrument_name'
        instrument_id:
          $ref: '#/components/schemas/instrument_id'
        is_active:
          type: boolean
          description: >
            `true` while the order book is visible (`open`, `settlement`,
            `locked`, or `halted`). `false` for `delivered`, `inactive`, and
            `archivized`.


            This is not the same as tradable. Only `state` `open` accepts new
            orders; `locked` allows cancels only, and `settlement` / `halted`
            reject new orders even when `is_active` is `true`.
        settlement_period:
          type: string
          enum:
            - minute
            - hour
            - day
            - week
            - month
            - perpetual
          description: >-
            Optional (omitted for spot). Calendar unit of the instrument's
            settlement/expiration period (`minute`, `hour`, `day`, `week`,
            `month`, or `perpetual`). Biweekly contracts still report `week`.
        creation_timestamp:
          type: integer
          example: 1536569522277
          description: >-
            The time when the instrument was first created (milliseconds since
            the UNIX epoch).
        tick_size:
          type: number
          example: 0.0001
          description: >-
            Specifies minimal price change and, as follows, the number of
            decimal places for instrument prices.
        tick_size_steps:
          $ref: '#/components/schemas/tick_size_step'
        expiration_timestamp:
          type: integer
          description: >-
            The time when the instrument will expire (milliseconds since the
            UNIX epoch). Present for perpetuals as well (a far-future
            timestamp); do not treat a non-zero value as proof the instrument is
            dated.
        strike:
          type: number
          description: The strike value (only for options).
        option_type:
          type: string
          enum:
            - call
            - put
          description: The option type (only for options).
        future_type:
          type: string
          enum:
            - linear
            - reversed
          description: >-
            Future type (only for futures)(field is deprecated and will be
            removed in the future, `instrument_type` should be used instead).
        instrument_type:
          type: string
          description: >-
            Type of the instrument. `linear` or `reversed`. Present for options
            and spots as well as futures; do not assume it is futures-only.
        contract_size:
          type: number
          example: 1
          description: >
            Contract size for the instrument, expressed in the same unit as the
            order amount. For inverse (reversed) futures and perpetuals this is
            USD — BTC-PERPETUAL has a contract size of 10 USD. For options,
            spots, and for linear futures and perpetuals it is the base currency
            coin — BTC_USDC-PERPETUAL has a contract size of 0.0001 BTC. Note
            that on an inverse instrument `base_currency` identifies the
            underlying and settlement coin and does not indicate the unit of
            `contract_size`.


            Distinct from `min_trade_amount`. `contract_size` converts between
            `amount` and `contracts`. Starbase matching uses the quantity
            increment, which JSON-RPC exposes as `min_trade_amount` (Starbase
            REST name: `qty_tick_size`). The two values may currently coincide
            on some instruments, but that is not a guarantee.
        lot_size:
          type: number
          example: 1
          description: >-
            Lot size for instrument, used as the unit for fee lot counting.
            Omitted when the instrument has no configured lot size.
        maker_commission:
          type: number
          example: 0.0001
          description: Maker commission for instrument.
        taker_commission:
          type: number
          example: 0.0005
          description: Taker commission for instrument.
        max_liquidation_commission:
          type: number
          example: 0.001
          description: >-
            Maximal liquidation trade commission for instrument (only for
            futures).
        maker_max_commission:
          type: number
          description: >-
            Optional. Maximum maker commission. Returned only when
            `extended=true` on `public/get_instruments`.
        taker_max_commission:
          type: number
          description: >-
            Optional. Maximum taker commission. Returned only when
            `extended=true` on `public/get_instruments`.
        liquidation_max_commission:
          type: number
          description: >-
            Optional. Maximum liquidation commission. Returned only when
            `extended=true` on `public/get_instruments`. Distinct from
            `max_liquidation_commission`, which is present on futures without
            `extended`.
        settlement_max_commission:
          type: number
          description: >-
            Optional. Maximum settlement commission. Returned only when
            `extended=true` on `public/get_instruments`.
        trading_bandwidth_fraction:
          type: number
          description: >-
            Optional (futures only). Trading bandwidth fraction used in
            mark-price logic. Returned only when `extended=true` on
            `public/get_instruments`.
        perpetual_dempener:
          type: number
          description: >-
            Optional (perpetual futures only). Perpetual funding dampener.
            Returned only when `extended=true` on `public/get_instruments`. The
            JSON field name is spelled `dempener`.
        perpetual_max_funding:
          type: number
          description: >-
            Optional (perpetual futures only). Maximum funding rate. Returned
            only when `extended=true` on `public/get_instruments`.
        block_trade_commission:
          type: number
          example: 0.0005
          description: >-
            Block Trade commission for instrument. Omitted for spot routed to
            Coinbase Exchange (CSR), which does not support block trades.
        block_trade_tick_size:
          type: number
          example: 0.01
          description: Specifies minimal price change for block trading.
        block_trade_min_trade_amount:
          type: number
          example: 25
          description: Minimum amount for block trading.
        max_leverage:
          type: integer
          example: 100
          description: >
            Maximal leverage for the default risk profile (futures). For spot,
            present only on cross pairs when spot margin loans are enabled:
            derived from the loan initial-margin rate for borrowable USDC-quoted
            pairs, otherwise 1. Omitted on other spots and options.
        max_non_default_leverage:
          type: integer
          description: >-
            Maximal leverage for the non-default risk profile (futures only).
            Omitted on options and spots.
        price_index:
          $ref: '#/components/schemas/price_index'
        underlying_type:
          type: string
          enum:
            - crypto
            - equity
            - commodity
            - preipo
            - equity_etf
            - crypto_index
            - adr
            - foreign_equity
            - equity_index
            - commodity_index
            - commodity_etf
            - otc
          description: The type of the underlying asset.
        state:
          $ref: '#/components/schemas/book_state'
        base_currency_uuid:
          type: string
          example: 5b71fc48-3dd3-540c-809b-f8c94d0e68b5
          description: >-
            Internal identifier for the base currency. Absent if the base
            currency does not have an assigned identifier.
        quote_currency_uuid:
          type: string
          example: 2b92315d-eab7-5bef-84fa-089a131333f5
          description: >-
            Internal identifier for the quote currency. Absent if the quote
            currency does not have an assigned identifier.
        index_id:
          type: integer
          example: 1000004
          description: >-
            Numeric identifier of the price index used by this instrument.
            Derived from the index currency pair, so all instruments sharing the
            same `price_index` also share the same `index_id`.
        product_group:
          type: string
          enum:
            - BTC
            - ETH
            - TIER_2
            - TIER_3
            - RWA
          example: BTC
          description: >-
            Product group classification of the instrument's base currency.
            Determines gateway and multicast channel assignment — see
            [Underlying
            Tiers](https://docs.deribit.com/starbase/underlying-tiers).
        is_csr:
          type: boolean
          description: >-
            Optional (only for spot routed to Coinbase Exchange). When present
            it is always `true`, meaning orders on this instrument are routed to
            Coinbase Exchange (CBE) for matching instead of the native Deribit
            matching engine. The field is omitted for every other instrument, so
            test for its presence rather than for a `false` value.
        is_cbe_routed:
          type: boolean
          description: >-
            Optional (only for spot routed to Coinbase Exchange). Alias of
            `is_csr` added by `public/get_instrument` and
            `public/get_instruments`; other surfaces that return instrument
            metadata, such as the `instrument.creation.{kind}.{currency}`
            notification, carry `is_csr` only. When present it is always `true`
            and is omitted for every other instrument, so test for its presence
            rather than for a `false` value.
      required:
        - kind
        - base_currency
        - quote_currency
        - min_trade_amount
        - instrument_name
        - is_active
        - creation_timestamp
        - tick_size
        - expiration_timestamp
        - contract_size
        - price_index
        - index_id
        - product_group
        - underlying_type
      type: object
    kind:
      enum:
        - future
        - option
        - spot
        - future_combo
        - option_combo
      type: string
      description: >-
        Instrument kind: `"future"`, `"option"`, `"spot"`, `"future_combo"`,
        `"option_combo"`
    instrument_id:
      type: integer
      description: Instrument ID
    tick_size_step:
      properties:
        above_price:
          type: number
          description: The price from which the increased tick size applies
        tick_size:
          type: number
          description: >-
            Tick size to be used above the price. It must be multiple of the
            minimum tick size.
      type: object
    price_index:
      example: btc_usdc
      type: string
      description: Name of price index that is used for this instrument
    book_state:
      enum:
        - open
        - settlement
        - delivered
        - inactive
        - locked
        - halted
        - archivized
      type: string
      description: >
        The state of the order book. Represents the current lifecycle stage of
        the instrument.


        **State Lifecycle and Meanings:**


        - `open`: Default state for running books. In this state book is
        accepting new orders, edits, cancels; prices should be updated, trading
        is live.

        - `settlement`: Books enters to this state during settlement/delivery.
        New orders, edits, cancels are not accepted. After this state normally
        next state should be `open` if it was settlement, or `delivered` if it
        was delivery. On enter to this state good till day orders in book are
        canceled.

        - `delivered`: Final state of book that has been delivered. New orders,
        edits, cancels are not accepted. After some time book process will be
        terminated and, instrument moved to `expired_instruments` and its
        `instrument_state` will become archivized. On enter to this all open
        orders in book are canceled.

        - `inactive`: After a book is deactivated, this state is set on book.
        New orders, edits, cancels are not accepted. On enter to this all open
        orders in book are canceled. Book in this state is not considered as
        open. This can be also final state for book.

        - `locked`: New orders, edits, are not accepted, only cancels ARE
        accepted. In some cases when configured books can start as locked or it
        may become locked on admin request. Settlement is possible on locked
        books.

        - `halted`: The state that books enter as a result of an error.
        Settlement is not possible when there is at least one book in this
        state.

        - `archivized`: Set when instrument is moved to `expired_instruments`
        table, final state.

````

## Related topics

- [public/get_instruments](https://docs.deribit.com/api-reference/market-data/public-get_instruments.md)
- [public/get_combos](https://docs.deribit.com/api-reference/combo-books/public-get_combos.md)
- [public/get_contract_size](https://docs.deribit.com/api-reference/market-data/public-get_contract_size.md)
- [public/get_combo_details](https://docs.deribit.com/api-reference/combo-books/public-get_combo_details.md)
- [List Instruments](https://docs.deribit.com/api-reference/market-data/list-instruments.md)