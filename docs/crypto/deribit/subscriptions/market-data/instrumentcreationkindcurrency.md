---
exchange: deribit
source_url: https://docs.deribit.com/subscriptions/market-data/instrumentcreationkindcurrency
api_type: WebSocket
updated_at: 2026-11-24 18:59:42.774603
---

# instrument.creation.(kind).(currency)

> Notification published once when an instrument is created, carrying full instrument data in the same format as `public/get_instruments`.

The notification fires exactly once at creation time, regardless of the instrument's initial state.

**Subscription examples:**

| Channel | Description |
|---|---|
| `instrument.creation.any.any` | All instruments |
| `instrument.creation.future.BTC` | BTC futures only |
| `instrument.creation.option.any` | All options |

**📖 Related Article:** [Options Data Collection Best Practices](https://docs.deribit.com/articles/options-data-collection-best-practices)


## AsyncAPI

````yaml specifications/deribit_asyncapi.json instrument.creation.(kind).(currency)
id: instrument.creation.(kind).(currency)
title: 'instrument.creation.(kind).(currency) '
description: >
  Notification published once when an instrument is created, carrying full
  instrument data in the same format as `public/get_instruments`.


  The notification fires exactly once at creation time, regardless of the
  instrument's initial state.


  **Subscription examples:**


  | Channel | Description |

  |---|---|

  | `instrument.creation.any.any` | All instruments |

  | `instrument.creation.future.BTC` | BTC futures only |

  | `instrument.creation.option.any` | All options |


  **📖 Related Article:** [Options Data Collection Best
  Practices](https://docs.deribit.com/articles/options-data-collection-best-practices)
servers:
  - id: production
    protocol: wss
    host: deribit.com/ws/api/v2
    bindings: []
    variables: []
  - id: testnet
    protocol: wss
    host: test.deribit.com/ws/api/v2
    bindings: []
    variables: []
address: instrument.creation.(kind).(currency)
parameters:
  - id: kind
    jsonSchema:
      type: string
      description: Instrument kind or `"any"` for all
      enum:
        - future
        - option
        - spot
        - future_combo
        - option_combo
        - any
    description: Instrument kind or `"any"` for all
    type: string
    required: true
    deprecated: false
  - id: currency
    jsonSchema:
      type: string
      description: >
        The currency symbol or `"any"` for all.


        **📖 Related Article:** [Using the currency
        Parameter](https://docs.deribit.com/articles/currency-parameter)
      enum:
        - BTC
        - ETH
        - USDC
        - USDT
        - EURR
        - any
    description: >
      The currency symbol or `"any"` for all.


      **📖 Related Article:** [Using the currency
      Parameter](https://docs.deribit.com/articles/currency-parameter)
    type: string
    required: true
    deprecated: false
bindings: []
operations:
  - &ref_2
    id: send_subscribe_instrument_creation_kind_currency
    title: Send subscribe request for instrument
    description: Client sends subscription request for instrument updates
    type: send
    messages:
      - &ref_4
        id: subscription_message
        contentType: application/json
        payload:
          - name: Subscription Notification Data
            description: Server sends subscription notification data
            type: object
            properties:
              - name: data
                type: object
                required: true
                properties:
                  - name: kind
                    type: string
                    description: >-
                      Instrument kind: `"future"`, `"option"`, `"spot"`,
                      `"future_combo"`, `"option_combo"`
                    enumValues:
                      - future
                      - option
                      - spot
                      - future_combo
                      - option_combo
                    required: true
                  - name: settlement_currency
                    type: string
                    description: >-
                      Optional (omitted for spot). Settlement currency for the
                      instrument. For inverse (reversed) contracts this is the
                      base coin (e.g. BTC); for linear contracts it is typically
                      the quote currency (e.g. USDC).
                    required: false
                  - name: counter_currency
                    type: string
                    description: >-
                      Counter currency of the instrument's currency pair (e.g.
                      USD or USDC).
                    required: false
                  - name: base_currency
                    type: string
                    description: >-
                      The underlying currency being traded. Not limited to
                      BTC/ETH — altcoins, RWAs, and other listed bases are
                      returned as their currency symbol.
                    required: true
                  - name: quote_currency
                    type: string
                    description: >-
                      The currency in which the instrument prices are quoted.
                      Inverse options and futures are typically quoted in USD;
                      linear and spot instruments are typically quoted in USDC
                      or the quote coin.
                    required: true
                  - name: min_trade_amount
                    type: number
                    description: >
                      Minimum amount for trading and the quantity increment
                      (step size) for order amounts. For perpetual and inverse
                      futures the amount is in USD units. For options and linear
                      futures it is the underlying base currency coin.


                      This is the JSON-RPC name for the Starbase quantity
                      increment (`qty_tick_size` on Starbase REST, SBE
                      `minOrderQuantity × 10^quantityExponent`). JSON-RPC does
                      not return a `qty_tick_size` field. Distinct from
                      `contract_size`; do not assume the two values are equal.
                    required: true
                  - name: instrument_name
                    type: string
                    description: Unique instrument identifier
                    required: true
                  - name: instrument_id
                    type: integer
                    description: Instrument ID
                    required: false
                  - name: is_active
                    type: boolean
                    description: >
                      `true` while the order book is visible (`open`,
                      `settlement`, `locked`, or `halted`). `false` for
                      `delivered`, `inactive`, and `archivized`.


                      This is not the same as tradable. Only `state` `open`
                      accepts new orders; `locked` allows cancels only, and
                      `settlement` / `halted` reject new orders even when
                      `is_active` is `true`.
                    required: true
                  - name: settlement_period
                    type: string
                    description: >-
                      Optional (omitted for spot). Calendar unit of the
                      instrument's settlement/expiration period (`minute`,
                      `hour`, `day`, `week`, `month`, or `perpetual`). Biweekly
                      contracts still report `week`.
                    enumValues:
                      - minute
                      - hour
                      - day
                      - week
                      - month
                      - perpetual
                    required: false
                  - name: creation_timestamp
                    type: integer
                    description: >-
                      The time when the instrument was first created
                      (milliseconds since the UNIX epoch).
                    required: true
                  - name: tick_size
                    type: number
                    description: >-
                      Specifies minimal price change and, as follows, the number
                      of decimal places for instrument prices.
                    required: true
                  - name: tick_size_steps
                    type: object
                    required: false
                    properties:
                      - name: above_price
                        type: number
                        description: The price from which the increased tick size applies
                        required: false
                      - name: tick_size
                        type: number
                        description: >-
                          Tick size to be used above the price. It must be
                          multiple of the minimum tick size.
                        required: false
                  - name: expiration_timestamp
                    type: integer
                    description: >-
                      The time when the instrument will expire (milliseconds
                      since the UNIX epoch). Present for perpetuals as well (a
                      far-future timestamp); do not treat a non-zero value as
                      proof the instrument is dated.
                    required: true
                  - name: strike
                    type: number
                    description: The strike value (only for options).
                    required: false
                  - name: option_type
                    type: string
                    description: The option type (only for options).
                    enumValues:
                      - call
                      - put
                    required: false
                  - name: future_type
                    type: string
                    description: >-
                      Future type (only for futures)(field is deprecated and
                      will be removed in the future, `instrument_type` should be
                      used instead).
                    enumValues:
                      - linear
                      - reversed
                    required: false
                  - name: instrument_type
                    type: string
                    description: >-
                      Type of the instrument. `linear` or `reversed`. Present
                      for options and spots as well as futures; do not assume it
                      is futures-only.
                    required: false
                  - name: contract_size
                    type: number
                    description: >
                      Contract size for the instrument, expressed in the same
                      unit as the order amount. For inverse (reversed) futures
                      and perpetuals this is USD — BTC-PERPETUAL has a contract
                      size of 10 USD. For options, spots, and for linear futures
                      and perpetuals it is the base currency coin —
                      BTC_USDC-PERPETUAL has a contract size of 0.0001 BTC. Note
                      that on an inverse instrument `base_currency` identifies
                      the underlying and settlement coin and does not indicate
                      the unit of `contract_size`.


                      Distinct from `min_trade_amount`. `contract_size` converts
                      between `amount` and `contracts`. Starbase matching uses
                      the quantity increment, which JSON-RPC exposes as
                      `min_trade_amount` (Starbase REST name: `qty_tick_size`).
                      The two values may currently coincide on some instruments,
                      but that is not a guarantee.
                    required: true
                  - name: lot_size
                    type: number
                    description: >-
                      Lot size for instrument, used as the unit for fee lot
                      counting. Omitted when the instrument has no configured
                      lot size.
                    required: false
                  - name: maker_commission
                    type: number
                    description: Maker commission for instrument.
                    required: false
                  - name: taker_commission
                    type: number
                    description: Taker commission for instrument.
                    required: false
                  - name: max_liquidation_commission
                    type: number
                    description: >-
                      Maximal liquidation trade commission for instrument (only
                      for futures).
                    required: false
                  - name: maker_max_commission
                    type: number
                    description: >-
                      Optional. Maximum maker commission. Returned only when
                      `extended=true` on `public/get_instruments`.
                    required: false
                  - name: taker_max_commission
                    type: number
                    description: >-
                      Optional. Maximum taker commission. Returned only when
                      `extended=true` on `public/get_instruments`.
                    required: false
                  - name: liquidation_max_commission
                    type: number
                    description: >-
                      Optional. Maximum liquidation commission. Returned only
                      when `extended=true` on `public/get_instruments`. Distinct
                      from `max_liquidation_commission`, which is present on
                      futures without `extended`.
                    required: false
                  - name: settlement_max_commission
                    type: number
                    description: >-
                      Optional. Maximum settlement commission. Returned only
                      when `extended=true` on `public/get_instruments`.
                    required: false
                  - name: trading_bandwidth_fraction
                    type: number
                    description: >-
                      Optional (futures only). Trading bandwidth fraction used
                      in mark-price logic. Returned only when `extended=true` on
                      `public/get_instruments`.
                    required: false
                  - name: perpetual_dempener
                    type: number
                    description: >-
                      Optional (perpetual futures only). Perpetual funding
                      dampener. Returned only when `extended=true` on
                      `public/get_instruments`. The JSON field name is spelled
                      `dempener`.
                    required: false
                  - name: perpetual_max_funding
                    type: number
                    description: >-
                      Optional (perpetual futures only). Maximum funding rate.
                      Returned only when `extended=true` on
                      `public/get_instruments`.
                    required: false
                  - name: block_trade_commission
                    type: number
                    description: >-
                      Block Trade commission for instrument. Omitted for spot
                      routed to Coinbase Exchange (CSR), which does not support
                      block trades.
                    required: false
                  - name: block_trade_tick_size
                    type: number
                    description: Specifies minimal price change for block trading.
                    required: false
                  - name: block_trade_min_trade_amount
                    type: number
                    description: Minimum amount for block trading.
                    required: false
                  - name: max_leverage
                    type: integer
                    description: >
                      Maximal leverage for the default risk profile (futures).
                      For spot, present only on cross pairs when spot margin
                      loans are enabled: derived from the loan initial-margin
                      rate for borrowable USDC-quoted pairs, otherwise 1.
                      Omitted on other spots and options.
                    required: false
                  - name: max_non_default_leverage
                    type: integer
                    description: >-
                      Maximal leverage for the non-default risk profile (futures
                      only). Omitted on options and spots.
                    required: false
                  - name: price_index
                    type: string
                    description: Name of price index that is used for this instrument
                    required: true
                  - name: underlying_type
                    type: string
                    description: The type of the underlying asset.
                    enumValues:
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
                    required: true
                  - name: state
                    type: string
                    description: >
                      The state of the order book. Represents the current
                      lifecycle stage of the instrument.


                      **State Lifecycle and Meanings:**


                      - `open`: Default state for running books. In this state
                      book is accepting new orders, edits, cancels; prices
                      should be updated, trading is live.

                      - `settlement`: Books enters to this state during
                      settlement/delivery. New orders, edits, cancels are not
                      accepted. After this state normally next state should be
                      `open` if it was settlement, or `delivered` if it was
                      delivery. On enter to this state good till day orders in
                      book are canceled.

                      - `delivered`: Final state of book that has been
                      delivered. New orders, edits, cancels are not accepted.
                      After some time book process will be terminated and,
                      instrument moved to `expired_instruments` and its
                      `instrument_state` will become archivized. On enter to
                      this all open orders in book are canceled.

                      - `inactive`: After a book is deactivated, this state is
                      set on book. New orders, edits, cancels are not accepted.
                      On enter to this all open orders in book are canceled.
                      Book in this state is not considered as open. This can be
                      also final state for book.

                      - `locked`: New orders, edits, are not accepted, only
                      cancels ARE accepted. In some cases when configured books
                      can start as locked or it may become locked on admin
                      request. Settlement is possible on locked books.

                      - `halted`: The state that books enter as a result of an
                      error. Settlement is not possible when there is at least
                      one book in this state.

                      - `archivized`: Set when instrument is moved to
                      `expired_instruments` table, final state.
                    enumValues:
                      - open
                      - settlement
                      - delivered
                      - inactive
                      - locked
                      - halted
                      - archivized
                    required: false
                  - name: base_currency_uuid
                    type: string
                    description: >-
                      Internal identifier for the base currency. Absent if the
                      base currency does not have an assigned identifier.
                    required: false
                  - name: quote_currency_uuid
                    type: string
                    description: >-
                      Internal identifier for the quote currency. Absent if the
                      quote currency does not have an assigned identifier.
                    required: false
                  - name: index_id
                    type: integer
                    description: >-
                      Numeric identifier of the price index used by this
                      instrument. Derived from the index currency pair, so all
                      instruments sharing the same `price_index` also share the
                      same `index_id`.
                    required: true
                  - name: product_group
                    type: string
                    description: >-
                      Product group classification of the instrument's base
                      currency. Determines gateway and multicast channel
                      assignment — see [Underlying
                      Tiers](https://docs.deribit.com/starbase/underlying-tiers).
                    enumValues:
                      - BTC
                      - ETH
                      - TIER_2
                      - TIER_3
                      - RWA
                    required: true
                  - name: is_csr
                    type: boolean
                    description: >-
                      Optional (only for spot routed to Coinbase Exchange). When
                      present it is always `true`, meaning orders on this
                      instrument are routed to Coinbase Exchange (CBE) for
                      matching instead of the native Deribit matching engine.
                      The field is omitted for every other instrument, so test
                      for its presence rather than for a `false` value.
                    required: false
                  - name: is_cbe_routed
                    type: boolean
                    description: >-
                      Optional (only for spot routed to Coinbase Exchange).
                      Alias of `is_csr` added by `public/get_instrument` and
                      `public/get_instruments`; other surfaces that return
                      instrument metadata, such as the
                      `instrument.creation.{kind}.{currency}` notification,
                      carry `is_csr` only. When present it is always `true` and
                      is omitted for every other instrument, so test for its
                      presence rather than for a `false` value.
                    required: false
                  - name: timestamp
                    type: integer
                    description: >-
                      The time when the instrument was created (milliseconds
                      since the UNIX epoch).
                    required: true
        headers: []
        jsonPayloadSchema:
          type: object
          description: Response containing notification data
          properties:
            data:
              allOf:
                - type: object
                  properties:
                    kind:
                      type: string
                      description: >-
                        Instrument kind: `"future"`, `"option"`, `"spot"`,
                        `"future_combo"`, `"option_combo"`
                      enum:
                        - future
                        - option
                        - spot
                        - future_combo
                        - option_combo
                      x-parser-schema-id: <anonymous-schema-809>
                    settlement_currency:
                      type: string
                      description: >-
                        Optional (omitted for spot). Settlement currency for the
                        instrument. For inverse (reversed) contracts this is the
                        base coin (e.g. BTC); for linear contracts it is
                        typically the quote currency (e.g. USDC).
                      x-parser-schema-id: <anonymous-schema-810>
                    counter_currency:
                      type: string
                      description: >-
                        Counter currency of the instrument's currency pair (e.g.
                        USD or USDC).
                      x-parser-schema-id: <anonymous-schema-811>
                    base_currency:
                      type: string
                      description: >-
                        The underlying currency being traded. Not limited to
                        BTC/ETH — altcoins, RWAs, and other listed bases are
                        returned as their currency symbol.
                      x-parser-schema-id: <anonymous-schema-812>
                    quote_currency:
                      type: string
                      description: >-
                        The currency in which the instrument prices are quoted.
                        Inverse options and futures are typically quoted in USD;
                        linear and spot instruments are typically quoted in USDC
                        or the quote coin.
                      x-parser-schema-id: <anonymous-schema-813>
                    min_trade_amount:
                      type: number
                      description: >
                        Minimum amount for trading and the quantity increment
                        (step size) for order amounts. For perpetual and inverse
                        futures the amount is in USD units. For options and
                        linear futures it is the underlying base currency coin.


                        This is the JSON-RPC name for the Starbase quantity
                        increment (`qty_tick_size` on Starbase REST, SBE
                        `minOrderQuantity × 10^quantityExponent`). JSON-RPC does
                        not return a `qty_tick_size` field. Distinct from
                        `contract_size`; do not assume the two values are equal.
                      example: 0.1
                      x-parser-schema-id: <anonymous-schema-814>
                    instrument_name:
                      type: string
                      description: Unique instrument identifier
                      example: BTC-PERPETUAL
                      x-parser-schema-id: <anonymous-schema-815>
                    instrument_id:
                      type: integer
                      description: Instrument ID
                      x-parser-schema-id: <anonymous-schema-816>
                    is_active:
                      type: boolean
                      description: >
                        `true` while the order book is visible (`open`,
                        `settlement`, `locked`, or `halted`). `false` for
                        `delivered`, `inactive`, and `archivized`.


                        This is not the same as tradable. Only `state` `open`
                        accepts new orders; `locked` allows cancels only, and
                        `settlement` / `halted` reject new orders even when
                        `is_active` is `true`.
                      x-parser-schema-id: <anonymous-schema-817>
                    settlement_period:
                      type: string
                      description: >-
                        Optional (omitted for spot). Calendar unit of the
                        instrument's settlement/expiration period (`minute`,
                        `hour`, `day`, `week`, `month`, or `perpetual`).
                        Biweekly contracts still report `week`.
                      enum:
                        - minute
                        - hour
                        - day
                        - week
                        - month
                        - perpetual
                      x-parser-schema-id: <anonymous-schema-818>
                    creation_timestamp:
                      type: integer
                      description: >-
                        The time when the instrument was first created
                        (milliseconds since the UNIX epoch).
                      example: 1536569522277
                      x-parser-schema-id: <anonymous-schema-819>
                    tick_size:
                      type: number
                      example: 0.0001
                      description: >-
                        Specifies minimal price change and, as follows, the
                        number of decimal places for instrument prices.
                      x-parser-schema-id: <anonymous-schema-820>
                    tick_size_steps:
                      type: object
                      properties:
                        above_price:
                          description: The price from which the increased tick size applies
                          type: number
                          x-parser-schema-id: <anonymous-schema-822>
                        tick_size:
                          description: >-
                            Tick size to be used above the price. It must be
                            multiple of the minimum tick size.
                          type: number
                          x-parser-schema-id: <anonymous-schema-823>
                      x-parser-schema-id: <anonymous-schema-821>
                    expiration_timestamp:
                      type: integer
                      description: >-
                        The time when the instrument will expire (milliseconds
                        since the UNIX epoch). Present for perpetuals as well (a
                        far-future timestamp); do not treat a non-zero value as
                        proof the instrument is dated.
                      x-parser-schema-id: <anonymous-schema-824>
                    strike:
                      type: number
                      description: The strike value (only for options).
                      x-parser-schema-id: <anonymous-schema-825>
                    option_type:
                      type: string
                      description: The option type (only for options).
                      enum:
                        - call
                        - put
                      x-parser-schema-id: <anonymous-schema-826>
                    future_type:
                      type: string
                      description: >-
                        Future type (only for futures)(field is deprecated and
                        will be removed in the future, `instrument_type` should
                        be used instead).
                      enum:
                        - linear
                        - reversed
                      x-parser-schema-id: <anonymous-schema-827>
                    instrument_type:
                      type: string
                      description: >-
                        Type of the instrument. `linear` or `reversed`. Present
                        for options and spots as well as futures; do not assume
                        it is futures-only.
                      x-parser-schema-id: <anonymous-schema-828>
                    contract_size:
                      type: number
                      description: >
                        Contract size for the instrument, expressed in the same
                        unit as the order amount. For inverse (reversed) futures
                        and perpetuals this is USD — BTC-PERPETUAL has a
                        contract size of 10 USD. For options, spots, and for
                        linear futures and perpetuals it is the base currency
                        coin — BTC_USDC-PERPETUAL has a contract size of 0.0001
                        BTC. Note that on an inverse instrument `base_currency`
                        identifies the underlying and settlement coin and does
                        not indicate the unit of `contract_size`.


                        Distinct from `min_trade_amount`. `contract_size`
                        converts between `amount` and `contracts`. Starbase
                        matching uses the quantity increment, which JSON-RPC
                        exposes as `min_trade_amount` (Starbase REST name:
                        `qty_tick_size`). The two values may currently coincide
                        on some instruments, but that is not a guarantee.
                      example: 1
                      x-parser-schema-id: <anonymous-schema-829>
                    lot_size:
                      type: number
                      description: >-
                        Lot size for instrument, used as the unit for fee lot
                        counting. Omitted when the instrument has no configured
                        lot size.
                      example: 1
                      x-parser-schema-id: <anonymous-schema-830>
                    maker_commission:
                      type: number
                      description: Maker commission for instrument.
                      example: 0.0001
                      x-parser-schema-id: <anonymous-schema-831>
                    taker_commission:
                      type: number
                      description: Taker commission for instrument.
                      example: 0.0005
                      x-parser-schema-id: <anonymous-schema-832>
                    max_liquidation_commission:
                      type: number
                      description: >-
                        Maximal liquidation trade commission for instrument
                        (only for futures).
                      example: 0.001
                      x-parser-schema-id: <anonymous-schema-833>
                    maker_max_commission:
                      type: number
                      description: >-
                        Optional. Maximum maker commission. Returned only when
                        `extended=true` on `public/get_instruments`.
                      x-parser-schema-id: <anonymous-schema-834>
                    taker_max_commission:
                      type: number
                      description: >-
                        Optional. Maximum taker commission. Returned only when
                        `extended=true` on `public/get_instruments`.
                      x-parser-schema-id: <anonymous-schema-835>
                    liquidation_max_commission:
                      type: number
                      description: >-
                        Optional. Maximum liquidation commission. Returned only
                        when `extended=true` on `public/get_instruments`.
                        Distinct from `max_liquidation_commission`, which is
                        present on futures without `extended`.
                      x-parser-schema-id: <anonymous-schema-836>
                    settlement_max_commission:
                      type: number
                      description: >-
                        Optional. Maximum settlement commission. Returned only
                        when `extended=true` on `public/get_instruments`.
                      x-parser-schema-id: <anonymous-schema-837>
                    trading_bandwidth_fraction:
                      type: number
                      description: >-
                        Optional (futures only). Trading bandwidth fraction used
                        in mark-price logic. Returned only when `extended=true`
                        on `public/get_instruments`.
                      x-parser-schema-id: <anonymous-schema-838>
                    perpetual_dempener:
                      type: number
                      description: >-
                        Optional (perpetual futures only). Perpetual funding
                        dampener. Returned only when `extended=true` on
                        `public/get_instruments`. The JSON field name is spelled
                        `dempener`.
                      x-parser-schema-id: <anonymous-schema-839>
                    perpetual_max_funding:
                      type: number
                      description: >-
                        Optional (perpetual futures only). Maximum funding rate.
                        Returned only when `extended=true` on
                        `public/get_instruments`.
                      x-parser-schema-id: <anonymous-schema-840>
                    block_trade_commission:
                      type: number
                      description: >-
                        Block Trade commission for instrument. Omitted for spot
                        routed to Coinbase Exchange (CSR), which does not
                        support block trades.
                      example: 0.0005
                      x-parser-schema-id: <anonymous-schema-841>
                    block_trade_tick_size:
                      type: number
                      description: Specifies minimal price change for block trading.
                      example: 0.01
                      x-parser-schema-id: <anonymous-schema-842>
                    block_trade_min_trade_amount:
                      type: number
                      description: Minimum amount for block trading.
                      example: 25
                      x-parser-schema-id: <anonymous-schema-843>
                    max_leverage:
                      type: integer
                      description: >
                        Maximal leverage for the default risk profile (futures).
                        For spot, present only on cross pairs when spot margin
                        loans are enabled: derived from the loan initial-margin
                        rate for borrowable USDC-quoted pairs, otherwise 1.
                        Omitted on other spots and options.
                      example: 100
                      x-parser-schema-id: <anonymous-schema-844>
                    max_non_default_leverage:
                      type: integer
                      description: >-
                        Maximal leverage for the non-default risk profile
                        (futures only). Omitted on options and spots.
                      x-parser-schema-id: <anonymous-schema-845>
                    price_index:
                      type: string
                      example: btc_usdc
                      description: Name of price index that is used for this instrument
                      x-parser-schema-id: <anonymous-schema-846>
                    underlying_type:
                      type: string
                      description: The type of the underlying asset.
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
                      x-parser-schema-id: <anonymous-schema-847>
                    state:
                      description: >
                        The state of the order book. Represents the current
                        lifecycle stage of the instrument.


                        **State Lifecycle and Meanings:**


                        - `open`: Default state for running books. In this state
                        book is accepting new orders, edits, cancels; prices
                        should be updated, trading is live.

                        - `settlement`: Books enters to this state during
                        settlement/delivery. New orders, edits, cancels are not
                        accepted. After this state normally next state should be
                        `open` if it was settlement, or `delivered` if it was
                        delivery. On enter to this state good till day orders in
                        book are canceled.

                        - `delivered`: Final state of book that has been
                        delivered. New orders, edits, cancels are not accepted.
                        After some time book process will be terminated and,
                        instrument moved to `expired_instruments` and its
                        `instrument_state` will become archivized. On enter to
                        this all open orders in book are canceled.

                        - `inactive`: After a book is deactivated, this state is
                        set on book. New orders, edits, cancels are not
                        accepted. On enter to this all open orders in book are
                        canceled. Book in this state is not considered as open.
                        This can be also final state for book.

                        - `locked`: New orders, edits, are not accepted, only
                        cancels ARE accepted. In some cases when configured
                        books can start as locked or it may become locked on
                        admin request. Settlement is possible on locked books.

                        - `halted`: The state that books enter as a result of an
                        error. Settlement is not possible when there is at least
                        one book in this state.

                        - `archivized`: Set when instrument is moved to
                        `expired_instruments` table, final state.
                      type: string
                      enum:
                        - open
                        - settlement
                        - delivered
                        - inactive
                        - locked
                        - halted
                        - archivized
                      x-parser-schema-id: <anonymous-schema-848>
                    base_currency_uuid:
                      type: string
                      description: >-
                        Internal identifier for the base currency. Absent if the
                        base currency does not have an assigned identifier.
                      example: 5b71fc48-3dd3-540c-809b-f8c94d0e68b5
                      x-parser-schema-id: <anonymous-schema-849>
                    quote_currency_uuid:
                      type: string
                      description: >-
                        Internal identifier for the quote currency. Absent if
                        the quote currency does not have an assigned identifier.
                      example: 2b92315d-eab7-5bef-84fa-089a131333f5
                      x-parser-schema-id: <anonymous-schema-850>
                    index_id:
                      type: integer
                      description: >-
                        Numeric identifier of the price index used by this
                        instrument. Derived from the index currency pair, so all
                        instruments sharing the same `price_index` also share
                        the same `index_id`.
                      example: 1000004
                      x-parser-schema-id: <anonymous-schema-851>
                    product_group:
                      type: string
                      description: >-
                        Product group classification of the instrument's base
                        currency. Determines gateway and multicast channel
                        assignment — see [Underlying
                        Tiers](https://docs.deribit.com/starbase/underlying-tiers).
                      enum:
                        - BTC
                        - ETH
                        - TIER_2
                        - TIER_3
                        - RWA
                      example: BTC
                      x-parser-schema-id: <anonymous-schema-852>
                    is_csr:
                      type: boolean
                      description: >-
                        Optional (only for spot routed to Coinbase Exchange).
                        When present it is always `true`, meaning orders on this
                        instrument are routed to Coinbase Exchange (CBE) for
                        matching instead of the native Deribit matching engine.
                        The field is omitted for every other instrument, so test
                        for its presence rather than for a `false` value.
                      x-parser-schema-id: <anonymous-schema-853>
                    is_cbe_routed:
                      type: boolean
                      description: >-
                        Optional (only for spot routed to Coinbase Exchange).
                        Alias of `is_csr` added by `public/get_instrument` and
                        `public/get_instruments`; other surfaces that return
                        instrument metadata, such as the
                        `instrument.creation.{kind}.{currency}` notification,
                        carry `is_csr` only. When present it is always `true`
                        and is omitted for every other instrument, so test for
                        its presence rather than for a `false` value.
                      x-parser-schema-id: <anonymous-schema-854>
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
                  x-parser-schema-id: <anonymous-schema-808>
                - type: object
                  properties:
                    timestamp:
                      type: integer
                      description: >-
                        The time when the instrument was created (milliseconds
                        since the UNIX epoch).
                      x-parser-schema-id: <anonymous-schema-856>
                  required:
                    - timestamp
                  x-parser-schema-id: <anonymous-schema-855>
              x-parser-schema-id: <anonymous-schema-807>
          required:
            - data
          additionalProperties: false
          x-parser-schema-id: <anonymous-schema-806>
        title: Subscription Notification Data
        description: Server sends subscription notification data
        example: |-
          {
            "data": {
              "tick_size": 0.0005,
              "tick_size_steps": [
                {
                  "above_price": 120,
                  "tick_size": 0.001
                }
              ],
              "taker_commission": 0.0003,
              "strike": 16000,
              "settlement_period": "week",
              "settlement_currency": "BTC",
              "quote_currency": "BTC",
              "price_index": "btc_usd",
              "index_id": 1000033,
              "product_group": "BTC",
              "option_type": "put",
              "min_trade_amount": 0.1,
              "maker_commission": 0.0003,
              "kind": "option",
              "is_active": true,
              "instrument_name": "BTC-13JAN23-16000-P",
              "instrument_id": 144613,
              "expiration_timestamp": 1673596800000,
              "creation_timestamp": 1671696002000,
              "timestamp": 1671696002000,
              "counter_currency": "USD",
              "contract_size": 1,
              "lot_size": 1,
              "block_trade_tick_size": 0.0001,
              "block_trade_min_trade_amount": 25,
              "block_trade_commission": 0.00015,
              "base_currency": "BTC",
              "state": "open"
            }
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: subscription_message
    bindings: []
    extensions: &ref_0
      - id: x-parser-unique-object-id
        value: instrument.creation.(kind).(currency)
  - &ref_1
    id: receive_instrument_creation_kind_currency_updates
    title: Receive instrument updates
    description: Client receives instrument update notifications
    type: receive
    messages:
      - &ref_3
        id: subscribe_request
        contentType: application/json
        payload:
          - name: Subscription Request
            description: >-
              Client sends subscription request to subscribe to notification
              channel. Please refer to [Notification
              page](https://docs.deribit.com/articles/notifications) for more
              information.
            type: object
            properties:
              - name: jsonrpc
                type: string
                description: '2.0'
                required: true
              - name: id
                type: integer
                required: true
              - name: method
                type: string
                enumValues:
                  - public/subscribe
                  - private/subscribe
                required: true
              - name: params
                type: object
                required: true
                properties:
                  - name: channels
                    type: array
                    required: true
                    properties:
                      - name: item
                        type: string
                        required: false
        headers: []
        jsonPayloadSchema:
          type: object
          properties:
            jsonrpc:
              type: string
              const: '2.0'
              x-parser-schema-id: <anonymous-schema-800>
            id:
              type: integer
              x-parser-schema-id: <anonymous-schema-801>
            method:
              type: string
              enum:
                - public/subscribe
                - private/subscribe
              x-parser-schema-id: <anonymous-schema-802>
            params:
              type: object
              properties:
                channels:
                  type: array
                  items:
                    type: string
                    x-parser-schema-id: <anonymous-schema-805>
                  x-parser-schema-id: <anonymous-schema-804>
              required:
                - channels
              x-parser-schema-id: <anonymous-schema-803>
          required:
            - jsonrpc
            - id
            - method
            - params
          additionalProperties: false
          x-parser-schema-id: <anonymous-schema-799>
        title: Subscription Request
        description: >-
          Client sends subscription request to subscribe to notification
          channel. Please refer to [Notification
          page](https://docs.deribit.com/articles/notifications) for more
          information.
        example: |-
          {
            "jsonrpc": "2.0",
            "method": "public/subscribe",
            "id": 42,
            "params": {
              "channels": [
                "instrument.creation.future.BTC"
              ]
            }
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: subscribe_request
    bindings: []
    extensions: *ref_0
sendOperations:
  - *ref_1
receiveOperations:
  - *ref_2
sendMessages:
  - *ref_3
receiveMessages:
  - *ref_4
extensions:
  - id: x-parser-unique-object-id
    value: instrument.creation.(kind).(currency)
securitySchemes: []

````

## Related topics

- [Options Data Collection](https://docs.deribit.com/articles/options-data-collection-best-practices.md)
- [Spot Trading: Deribit and Coinbase-Routed Instruments](https://docs.deribit.com/articles/spot-trading-venues.md)
- [public/get_instruments](https://docs.deribit.com/api-reference/market-data/public-get_instruments.md)
- [JSON-RPC API Changelog](https://docs.deribit.com/changelogs/jsonrpc.md)
- [public/get_instrument](https://docs.deribit.com/api-reference/market-data/public-get_instrument.md)