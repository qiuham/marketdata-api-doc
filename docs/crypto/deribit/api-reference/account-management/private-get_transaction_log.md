---
exchange: deribit
source_url: https://docs.deribit.com/api-reference/account-management/private-get_transaction_log
api_type: JSON-RPC
updated_at: 2026-11-28 18:58:43.129666
---

# private/get_transaction_log

> Retrieves a detailed transaction log for the authenticated account. The log includes all account activities such as trades, deposits, withdrawals, transfers, fees, and other balance-affecting operations.

Results can be filtered by currency, time range, and `query` keywords. `start_timestamp` must not exceed `end_timestamp`; both values are clamped to the current time, so a future `end_timestamp` is treated as now. The matching window includes `end_timestamp`.

`count` defaults to 100 and is capped at 1000. Pass `continuation` (a log id from the previous response) to fetch the next older page. `continuation` is `null` when there are no more entries.

To retrieve transactions for a specific subaccount, pass `subaccount_id` from the main account. Removed subaccounts are accepted. The authenticated user id is always applied as a filter.

Trade entries executed in Starbase include `starbase_match_id`, `starbase_order_id`, and `starbase_timestamp`. Those fields are omitted on spot trades. Block RFQ allocations appear as `type` `trade allocation` rather than `trade`.

When an option expires out of the money, the transaction log type is `expiry`. As there is nothing to settle into futures in this case, this remains the only entry in the transaction log for that expiration. In-the-money expiries use `assignment` or `exercise`, and may be followed by a `future creation` entry.

LSP and ADL position moves are logged as `type` `LSP transfer` / `ADL transfer`. Both the liquidated/deleveraged account and the receiving account get that same `type`. A separate optional `role` field (`source` or `destination`) is present on those transfer entries — and also on `liquidation transfer` and `position move` — and is omitted on all other types, including `LSP commission` / `ADL commission` and ordinary `trade`s. Do not confuse `role` with `user_role` (`maker` / `taker`) on trades.

Correction entries may include a `related` array of the original log entries they correct. While the platform is starting, the method may return `temporarily_unavailable`.

**History Limit:** This API method has **no time limit** - users can query transaction history back to account creation. Note that the CSV export feature available on the website is year-limited to 2023.

**Note - This method has distinct API rate limiting requirements:** Sustained rate: 1 request/second. For more information, see [Rate Limits](https://docs.deribit.com/articles/rate-limits).

**📖 Related Support Article:** [Transaction log](https://support.deribit.com/hc/en-us/articles/25944587269021-Transaction-log)

**📖 Related Article:** [Liquidity Support Program (LSP) API Guide](https://docs.deribit.com/articles/lsp-api-guide)

**Scope:** `account:read`

[Try in API console](https://test.deribit.com/api_console?method=%2Fprivate%2Fget_transaction_log)


## OpenAPI

````yaml /specifications/deribit_openapi.json get /private/get_transaction_log
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
  /private/get_transaction_log:
    get:
      tags:
        - Account Management
        - Private
      description: >+
        Retrieves a detailed transaction log for the authenticated account. The
        log includes all account activities such as trades, deposits,
        withdrawals, transfers, fees, and other balance-affecting operations.


        Results can be filtered by currency, time range, and `query` keywords.
        `start_timestamp` must not exceed `end_timestamp`; both values are
        clamped to the current time, so a future `end_timestamp` is treated as
        now. The matching window includes `end_timestamp`.


        `count` defaults to 100 and is capped at 1000. Pass `continuation` (a
        log id from the previous response) to fetch the next older page.
        `continuation` is `null` when there are no more entries.


        To retrieve transactions for a specific subaccount, pass `subaccount_id`
        from the main account. Removed subaccounts are accepted. The
        authenticated user id is always applied as a filter.


        Trade entries executed in Starbase include `starbase_match_id`,
        `starbase_order_id`, and `starbase_timestamp`. Those fields are omitted
        on spot trades. Block RFQ allocations appear as `type` `trade
        allocation` rather than `trade`.


        When an option expires out of the money, the transaction log type is
        `expiry`. As there is nothing to settle into futures in this case, this
        remains the only entry in the transaction log for that expiration.
        In-the-money expiries use `assignment` or `exercise`, and may be
        followed by a `future creation` entry.


        LSP and ADL position moves are logged as `type` `LSP transfer` / `ADL
        transfer`. Both the liquidated/deleveraged account and the receiving
        account get that same `type`. A separate optional `role` field (`source`
        or `destination`) is present on those transfer entries — and also on
        `liquidation transfer` and `position move` — and is omitted on all other
        types, including `LSP commission` / `ADL commission` and ordinary
        `trade`s. Do not confuse `role` with `user_role` (`maker` / `taker`) on
        trades.


        Correction entries may include a `related` array of the original log
        entries they correct. While the platform is starting, the method may
        return `temporarily_unavailable`.


        **History Limit:** This API method has **no time limit** - users can
        query transaction history back to account creation. Note that the CSV
        export feature available on the website is year-limited to 2023.


        **Note - This method has distinct API rate limiting requirements:**
        Sustained rate: 1 request/second. For more information, see [Rate
        Limits](https://docs.deribit.com/articles/rate-limits).


        **📖 Related Support Article:** [Transaction
        log](https://support.deribit.com/hc/en-us/articles/25944587269021-Transaction-log)


        **📖 Related Article:** [Liquidity Support Program (LSP) API
        Guide](https://docs.deribit.com/articles/lsp-api-guide)


        **Scope:** `account:read`


        [Try in API
        console](https://test.deribit.com/api_console?method=%2Fprivate%2Fget_transaction_log)

      parameters:
        - name: currency
          required: true
          in: query
          schema:
            $ref: '#/components/schemas/wallet_currency'
          description: >
            The currency symbol.


            **📖 Related Article:** [Using the currency
            Parameter](https://docs.deribit.com/articles/currency-parameter)
        - name: start_timestamp
          required: true
          in: query
          schema:
            $ref: '#/components/schemas/timestamp'
          description: >-
            The earliest timestamp to return result from (milliseconds since the
            UNIX epoch)
        - name: end_timestamp
          required: true
          in: query
          schema:
            $ref: '#/components/schemas/timestamp'
          description: >-
            The most recent timestamp to return result from (milliseconds since
            the UNIX epoch)
        - name: query
          in: query
          schema:
            type: string
            example: settlement
          required: false
          description: >
            Space-separated keywords used to filter results. An entry must match
            every keyword. Keywords are case-sensitive.


            Transaction types:


            - ``trade`` - trades

            - ``deposit`` - deposits

            - ``withdrawal`` - withdrawals

            - ``transfer`` - transfers between accounts

            - ``reward`` - reward transfers

            - ``mm_lsp_payment`` - market-maker LSP payout transfers

            - ``settlement`` - funding / session settlement (display type
            `settlement`)

            - ``delivery`` - instrument delivery (display type `delivery`)

            - ``expiry`` - options that expired out of the money

            - ``assignment`` - assigned options

            - ``exercise`` - exercised options

            - ``swap`` - currency swaps

            - ``correction`` - balance corrections

            - ``block_trade`` - block trades

            - ``combo_trade`` - combo trades

            - ``liquidation`` - liquidation trades and liquidation transfers
            (display type `liquidation transfer`)

            - ``lsp`` - LSP position moves and commissions (display types `LSP
            transfer` / `LSP commission`)

            - ``adl`` - ADL position moves and commissions (display types `ADL
            transfer` / `ADL commission`)

            - ``commission`` - LSP/ADL commissions; typically combined with
            ``lsp`` or ``adl``

            - ``position`` - position moves (display type `position move`); also
            matches `position move transfer`

            - ``insurance`` - insurance-related transfers

            - ``insurance_transfer`` - insurance transfers

            - ``affiliate`` - affiliate payouts

            - ``partner`` - partner / application fee payouts

            - ``fee_deposit`` - fee balance deposits

            - ``fee_balance_transfer`` - fee balance transfers

            - ``stake_reward`` - staking rewards

            - ``lock_deposit_balance`` - locked deposit balance

            - ``unlock_deposit_balance`` - unlocked deposit balance

            - ``summary`` - settlement summaries

            - ``options_settlement_summary`` - options settlement summaries

            - ``negative_balance_fee`` - negative balance fees

            - ``creation`` - future creation from expired options (display type
            `future creation`)

            - ``margin_loan`` - margin loan interest, issuance, and repayment

            - ``corporate_action_adjustment`` - stock split, rights offering,
            and spin-off adjustments

            - ``stock_split`` - stock splits

            - ``rights_offering`` - rights offerings

            - ``spin_off`` - spin-offs

            - ``m_and_a`` - mergers and acquisitions (display type `m&a`)

            - ``rename`` - instrument renames

            - ``custody_settlement_fee`` - custody settlement fees

            - ``sweep_isolated_position`` - isolated position sweeps

            - ``structured_product_spread`` - structured product spread

            - ``usdc_reward`` - USDC rewards

            - ``usdc_reward_received`` - USDC rewards received

            - ``usdc_platform_reward`` - USDC platform rewards

            - ``usdc_reward_payment`` - USDC reward payments

            - ``ethena_reward`` - Ethena rewards

            - ``buidl_reward`` - BUIDL rewards

            - ``socialize_loses`` - socialized losses/refunds (display types
            `socialized fund` / `socialized refund`)


            Additional filters:


            - ``maker`` / ``taker`` - trade role

            - ``open`` / ``close`` - trade kind (`close` also matches deliveries
            and liquidations)

            - ``buy`` / ``sell`` - direction

            - ``option`` / ``future`` / ``spot`` - instrument kind

            - ``voice_broker`` - voice-broker trades


            Additional indexed values, depending on type:


            - deposits — destination address (custody deposits also index
            custody name and request id)

            - withdrawals — withdrawal `code` or custody request id (not the
            destination address)

            - transfers — counterparty username
        - name: count
          in: query
          required: false
          schema:
            type: integer
            maximum: 1000
            minimum: 1
          description: >-
            Count of transaction log entries returned, default - `100`, maximum
            - `1000`
        - name: subaccount_id
          in: query
          required: false
          schema:
            type: integer
            example: 9
          description: Id of a subaccount
        - name: continuation
          in: query
          required: false
          schema:
            type: integer
            example: 429946
          description: Continuation token for pagination
      requestBody:
        content:
          application/json:
            examples:
              request:
                summary: JSON-RPC Request Example
                value:
                  jsonrpc: '2.0'
                  id: 4
                  method: private/get_transaction_log
                  params:
                    currency: BTC
                    start_timestamp: '1613657734000'
                    end_timestamp: '1613660407000'
                    count: 5
        description: JSON-RPC request body
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PrivateGetTransactionLogResponse'
              examples:
                response:
                  summary: Response example
                  value:
                    jsonrpc: '2.0'
                    id: 4
                    result:
                      logs:
                        - username: TestUser
                          user_seq: 6010
                          user_id: 7
                          type: LSP transfer
                          role: source
                          side: sell
                          trade_id: null
                          timestamp: 1613659900000
                          price_currency: USD
                          price: 63481.75
                          position: 0
                          order_id: null
                          session_rpl: -12.4
                          total_interest_pl: 0.00000512
                          interest_pl: 0.00000512
                          instrument_name: BTC-PERPETUAL
                          id: 61313
                          equity: 2998.5275869
                          currency: BTC
                          commission: 0
                          change: -2.4
                          cashflow: -2.4
                          balance: 2998.82270418
                          amount: 5000
                        - username: TestUser
                          user_seq: 6009
                          user_id: 7
                          type: transfer
                          trade_id: null
                          timestamp: 1613659830333
                          side: '-'
                          price: null
                          position: null
                          order_id: null
                          interest_pl: null
                          instrument_name: null
                          info:
                            transfer_type: subaccount
                            other_user_id: 27
                            other_user: Subaccount
                          id: 61312
                          equity: 3000.9275869
                          currency: BTC
                          commission: 0
                          change: -2.5
                          cashflow: -2.5
                          balance: 3001.22270418
                        - username: TestUser
                          user_seq: 6008
                          user_id: 7
                          type: settlement
                          trade_id: null
                          total_interest_pl: 0.00001243
                          timestamp: 1613659544153
                          side: long
                          session_upl: 0.00220172
                          session_rpl: -0.00004467
                          price_currency: USD
                          price: 51807.07
                          position: 1520
                          order_id: null
                          interest_pl: 0.00000993
                          instrument_name: BTC-PERPETUAL
                          info:
                            settlement_price: 51807
                            floating_pl: 0.00220172
                          id: 61311
                          equity: 3003.42821428
                          currency: BTC
                          commission: null
                          change: 0.00215706
                          cashflow: 0.00215706
                          balance: 3003.72270418
                          amount: 1520
                        - username: TestUser
                          user_seq: 6007
                          user_id: 7
                          type: deposit
                          trade_id: null
                          timestamp: 1613657828414
                          side: '-'
                          price: null
                          position: null
                          order_id: null
                          interest_pl: null
                          instrument_name: null
                          info:
                            transaction: >-
                              de6eba075855f32c9510f338d3ca0900376cedcb9f7b142caccfbdc292d3237e
                            deposit_type: wallet
                            addr: 2N8prMvpZHr8aYqodX3S4yhz5wMxjY8La3p
                          id: 61291
                          equity: 3003.4876111
                          currency: BTC
                          commission: 0
                          change: 0.65
                          cashflow: 0.65
                          balance: 3003.72054712
                        - username: TestUser
                          user_seq: 6006
                          user_role: maker
                          user_id: 7
                          type: trade
                          ip: 11.222.33.44
                          trade_id: '28349'
                          timestamp: 1613657734620
                          side: open buy
                          profit_as_cashflow: false
                          price_currency: BTC
                          price: 0.1537
                          position: 0.7
                          order_id: '67546'
                          mark_price: 0.04884653215049635
                          interest_pl: 0
                          instrument_name: BTC-19FEB21-49200-C
                          info: 'Source: api'
                          id: 61289
                          equity: 3002.83270455
                          currency: BTC
                          commission: 0
                          change: -0.10759
                          cashflow: -0.10759
                          balance: 3003.07054712
                          amount: 0.7
                        - username: TestUser
                          user_seq: 6005
                          user_role: maker
                          user_id: 7
                          type: trade
                          trade_id: '28349'
                          timestamp: 1613657734620
                          side: close buy
                          profit_as_cashflow: false
                          price_currency: BTC
                          price: 0.1537
                          position: 0
                          order_id: '67546'
                          mark_price: 0.04884653215049635
                          interest_pl: 0
                          instrument_name: BTC-19FEB21-49200-C
                          info: 'Source: api'
                          id: 61288
                          equity: 3002.83270455
                          currency: BTC
                          commission: 0
                          change: -0.04611
                          cashflow: -0.04611
                          balance: 3003.17813712
                          amount: 0.3
                        - username: TestUser
                          user_seq: 6004
                          user_id: 7
                          type: expiry
                          trade_id: null
                          timestamp: 1613657734620
                          side: close buy
                          price_currency: BTC
                          price: 0
                          position: 0
                          order_id: null
                          interest_pl: null
                          instrument_name: BTC-19FEB21-52000-C
                          info: null
                          id: 61287
                          equity: 3002.83270455
                          currency: BTC
                          commission: 0
                          change: 0
                          cashflow: 0
                          balance: 3003.17813712
                          amount: 0.3
                      continuation: 61282
          description: Success response
      x-codeSamples:
        - lang: bash
          label: cURL
          source: |-
            curl --request POST \
              --url https://test.deribit.com/api/v2/private/get_transaction_log \
              --header 'Authorization: Bearer <ACCESS_TOKEN>' \
              --header 'Content-Type: application/json' \
              --data '{
              "jsonrpc": "2.0",
              "id": 4,
              "method": "private/get_transaction_log",
              "params": {
                "currency": "BTC",
                "start_timestamp": "1613657734000",
                "end_timestamp": "1613660407000",
                "count": 5
              }
            }'
components:
  schemas:
    wallet_currency:
      enum:
        - BTC
        - ETH
        - STETH
        - ETHW
        - USDC
        - USDT
        - EURR
        - SOL
        - XRP
        - USYC
        - PAXG
        - BNB
        - USDE
      type: string
      description: Currency, i.e `"BTC"`, `"ETH"`, `"USDC"`
    timestamp:
      example: 1536569522277
      type: integer
      description: The timestamp (milliseconds since the Unix epoch)
    PrivateGetTransactionLogResponse:
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
          type: object
          properties:
            continuation:
              $ref: '#/components/schemas/continuation_with_null'
            logs:
              type: array
              items:
                $ref: '#/components/schemas/transaction_log'
          required:
            - continuation
            - logs
      required:
        - result
        - jsonrpc
      type: object
    continuation_with_null:
      example: 429946
      type: integer
      description: Continuation token for pagination. `NULL` when no continuation.
    transaction_log:
      properties:
        id:
          $ref: '#/components/schemas/id'
        currency:
          $ref: '#/components/schemas/currency'
        timestamp:
          $ref: '#/components/schemas/timestamp'
        user_id:
          $ref: '#/components/schemas/user_id'
        username:
          $ref: '#/components/schemas/username'
        commission:
          $ref: '#/components/schemas/commission'
        cashflow:
          type: number
          description: >
            Signed cash-related amount for this entry, in the log `currency`.
            Meaning depends on `type` and instrument kind:
            deposits/withdrawals/transfers use the moved amount; option trades
            use premium paid/received; future trades use realized session PnL
            when `profit_as_cashflow` is `true`, otherwise the cash movement. Do
            not assume it always equals `change`.
        balance:
          type: number
          description: Cash balance after the transaction
        change:
          type: number
          description: >
            Change in cash balance for this entry. When the platform recorded an
            explicit balance change, that value is used; otherwise `cashflow -
            commission`. On future trades with `profit_as_cashflow` `true`,
            session PnL sits in `cashflow` and `change` reflects the
            cash-balance movement (typically fees).
        user_seq:
          type: integer
          nullable: true
          description: >-
            Sequential identifier of user transaction in this currency. `null`
            on entries that were not assigned a sequence (common for some
            non-trade types).
        type:
          type: string
          description: >
            Transaction category. Present on every log entry. New types can be
            added at any time.


            Common values include `trade`, `deposit`, `withdrawal`,
            `settlement`, `delivery`, `transfer`, `swap`, `correction`,
            `expiry`, `assignment`, `exercise`, `future creation`, `LSP
            transfer`, `LSP commission`, `ADL transfer`, `ADL commission`. Block
            RFQ allocations use `trade allocation` rather than `trade`.


            Display values are not always the same as `query` keywords (for
            example query `lsp` to match `LSP transfer`). See the `query`
            parameter.


            `type` is not a substitute for `role`: both sides of an LSP or ADL
            position move use the same `type` (`LSP transfer` or `ADL
            transfer`). Which side this entry is on is `role`, when that field
            is present.
        role:
          type: string
          enum:
            - source
            - destination
          description: >
            Which side of a position move this log entry represents: `source`
            (the account the position is taken from) or `destination` (the
            account receiving the position).


            Present only on `LSP transfer`, `ADL transfer`, `liquidation
            transfer`, and `position move` entries. Omitted on every other
            `type`, including `LSP commission`, `ADL commission`, `trade`,
            `settlement`, and `transfer`. Not the same as `user_role` (`maker` /
            `taker`) on trade entries.


            Websocket liquidation notifications do not use this field; they
            distinguish sides with `state` (`lsp_transfer` / `adl_transfer` vs
            `adl_transfer_received`).
        info:
          description: >
            Additional information. Shape depends on `type`:

            - trades: a string such as `Source: api` or `Source: voice_broker`
            (not an object)

            - transfers and similar: an object (counterparties, `transfer_type`,
            ...)

            - `null` when there is nothing extra
        related:
          type: array
          items:
            $ref: '#/components/schemas/transaction_log'
          description: >-
            Present on correction entries. The original log entries this
            correction applies to.
        fee_balance:
          $ref: '#/components/schemas/fee_balance'
        equity:
          type: number
          description: Updated equity value after the transaction
        mark_price:
          type: number
          description: Market price during the trade
        settlement_price:
          type: number
          description: The settlement price for the instrument during the delivery
        index_price:
          type: number
          description: >-
            Index price associated with the entry when recorded. Present on
            deliveries and also on some trades, deposits, withdrawals, and
            transfers. Omitted when the log has no index price.
        instrument_name:
          $ref: '#/components/schemas/instrument_name'
        position:
          type: number
          description: Updated position size after the transaction
        side:
          type: string
          description: >
            Directional label. Value depends on `type`:

            - trades: `open buy`, `open sell`, `close buy`, `close sell`
            (liquidation trades use `liquidation buy` / `liquidation sell`)

            - deliveries / exercise: `close buy` or `close sell`

            - settlements: `long`, `short`, or `-` when size is zero

            - position moves: `buy` or `sell` when a direction is set

            - entries with no side: `-`
        amount:
          type: number
          description: >
            Size of the activity when the entry is instrument-related. For
            perpetual and inverse futures the amount is in USD units. For
            options and linear futures it is the underlying base currency coin.
            For spot trades it is the cash amount. `0` or omitted on entries
            with no size (for example a settlement with a flat position).
        price:
          type: number
          description: Settlement/delivery price or the price level of the traded contracts
        price_currency:
          type: string
          description: Currency symbol associated with the `price` field value
        trade_id:
          $ref: '#/components/schemas/trade_id'
        order_id:
          $ref: '#/components/schemas/order_id'
        user_role:
          $ref: '#/components/schemas/role'
        fee_role:
          $ref: '#/components/schemas/fee_role'
        profit_as_cashflow:
          type: boolean
          description: >
            Present on trades. `true` on future trades when realized session PnL
            is carried in `cashflow` and has not yet been settled into the cash
            balance. `false` on option and spot trades, and on future trades
            with no PnL in `cashflow`.
        interest_pl:
          type: number
          description: >-
            Funding PnL amount for the interval between this log entry and the
            previous trade or position change on perpetual instruments
        block_rfq_id:
          type: integer
          description: ID of the Block RFQ - when trade was part of the Block RFQ
        ip:
          type: string
          description: The IP address from which the trade was initiated
        starbase_match_id:
          type: integer
          description: >-
            Starbase match id for `trade` entries executed in Starbase. Omitted
            on spot trades and on Thunder-only trades.
        starbase_order_id:
          type: integer
          example: 103148386170
          description: >-
            Raw Starbase order id for `trade` entries associated with orders
            placed in Starbase. Omitted on spot trades and when the order was
            not placed in Starbase.
        starbase_timestamp:
          $ref: '#/components/schemas/starbase_timestamp'
          description: >-
            Starbase causal timestamp for `trade` entries executed in Starbase.
            Omitted on spot trades and on Thunder-only trades.
        session_rpl:
          $ref: '#/components/schemas/rpl'
        session_upl:
          $ref: '#/components/schemas/upl'
        total_interest_pl:
          type: number
          description: >-
            Total funding PnL accrued in the current trading session since the
            last daily settlement at 08:00 UTC, in the settlement currency.
            Resets at each daily settlement.
        contracts:
          $ref: '#/components/schemas/contracts'
      required:
        - id
        - currency
        - timestamp
        - user_id
        - commission
        - cashflow
        - balance
        - change
        - user_seq
        - type
      type: object
    id:
      example: 5967413
      type: integer
      description: Unique identifier
    currency:
      enum:
        - BTC
        - ETH
        - USDC
        - USDT
        - EURR
      type: string
      description: Currency, i.e `"BTC"`, `"ETH"`, `"USDC"`
    user_id:
      example: 57874
      type: integer
      description: Unique user identifier
    username:
      example: MrTrader
      type: string
      description: System name or user defined subaccount alias
    commission:
      type: number
      description: Commission paid so far (in base currency)
    fee_balance:
      type: number
      description: The account's fee balance (it can be used to pay for fees)
    instrument_name:
      example: BTC-PERPETUAL
      type: string
      description: Unique instrument identifier
    trade_id:
      type: string
      description: Unique (per currency) trade identifier
    order_id:
      example: ETH-100234
      type: string
      description: Unique order identifier
    role:
      enum:
        - maker
        - taker
      type: string
      description: 'Trade role of the user: `maker` or `taker`'
    fee_role:
      enum:
        - maker
        - taker
      type: string
      description: >-
        Fee role of the user: `maker` or `taker`. Can be different from trade
        role of the user when iceberg order was involved in matching.
    starbase_timestamp:
      example: 1536569522277000000
      type: integer
      description: >-
        The Starbase causal timestamp of the trade (nanoseconds since the Unix
        epoch)
    rpl:
      example: 0.1
      type: number
      description: >-
        Realized profit and loss accrued in the current trading session (since
        the last daily settlement). Resets at each daily settlement.
    upl:
      example: 0.846863
      type: number
      description: >-
        Unrealized profit and loss on open positions in the current trading
        session (since the last daily settlement).
    contracts:
      type: number
      description: >-
        It represents the order size in contract units. (Optional, may be absent
        in historical data).

````

## Related topics

- [JSON-RPC API Changelog](https://docs.deribit.com/changelogs/jsonrpc.md)
- [Liquidity Support Program (LSP) API Guide](https://docs.deribit.com/articles/lsp-api-guide.md)
- [Coinbase International Exchange API Migration](https://docs.deribit.com/articles/intx-api-migration.md)
- [Starbase Reference Data and Instrument Definitions](https://docs.deribit.com/starbase/reference-data.md)
- [Rate Limits](https://docs.deribit.com/articles/rate-limits.md)