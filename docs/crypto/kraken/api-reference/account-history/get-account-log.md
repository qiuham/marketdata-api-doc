---
api_type: reference
source_type: llms_txt
version: ''
scope: crypto
asset_class: digital_asset
domain: exchanges
provider: kraken
provider_name: Kraken
product: api
product_id: kraken
source_url: 'https://docs.kraken.com/api-reference/account-history/get-account-log'
updated_at: 2026-11-13
---

# Get account log

> Lists account log entries, paged by timestamp or by ID.

To request entries by time range, use the `since` and `before` parameters.
To request entries by ID range, use the `from` and `to` parameters.
Any combination of `since`, `before`, `from` and `to` can be used to restrict the requested range of entries.




## OpenAPI

````yaml /openapi/futures-history-rest.yaml get /account-log
openapi: 3.1.0
info:
  title: History
  version: '3'
  description: |
    Public history APIs.
servers:
  - url: https://futures.kraken.com/api/history/v3
    description: Kraken Futures
    x-kfOnly: true
security: []
tags:
  - name: Account History
    description: >
      Account History provides account-specific data, including account logs (
      history of all balance and position changes) and history for executions,
      orders, and triggers.


      * The `/account-log` endpoint provides a paginated JSON response, with
      access to all account log history specified by ranges of timestamp or ID.

      * The `/accountlogcsv` endpoint provides a CSV formatted response of
      500,000 rows of most recent account logs.
       See also the websocket feed of account log snapshots
      * The `/executions` endpoint provides a paginated JSON response, with
      access to all private execution history specified by ranges of timestamp
      or ID

      * The `/orders` endpoint provides a paginated JSON response, with access
      to all private order history specified by ranges of timestamp or ID

      * The `/triggers` endpoint provides a paginated JSON response, with access
      to all private trigger history specified by ranges of timestamp or ID
  - name: Market History
paths:
  /account-log:
    get:
      tags:
        - Account History
      summary: Get account log
      description: >
        Lists account log entries, paged by timestamp or by ID.


        To request entries by time range, use the `since` and `before`
        parameters.

        To request entries by ID range, use the `from` and `to` parameters.

        Any combination of `since`, `before`, `from` and `to` can be used to
        restrict the requested range of entries.
      operationId: accountLog
      parameters:
        - description: Unix timestamp in milliseconds.
          name: since
          in: query
          required: false
          schema:
            $ref: '#/components/schemas/TimestampMilliseconds'
        - description: Unix timestamp in milliseconds.
          name: before
          in: query
          required: false
          schema:
            $ref: '#/components/schemas/TimestampMilliseconds'
        - description: ID of the first entry (inclusive). IDs start at 1.
          name: from
          in: query
          required: false
          schema:
            type: integer
            example: 1
        - description: ID of the last entry (inclusive).
          name: to
          in: query
          required: false
          schema:
            type: integer
            example: 100
        - description: >
            Order of events in response. `asc` = chronological, `desc` =
            reverse-chronological.
          name: sort
          in: query
          required: false
          schema:
            type: string
            enum:
              - asc
              - desc
            default: desc
        - description: Types of entry to filter by. Only these types will be returned.
          name: info
          in: query
          required: false
          schema:
            type: array
            items:
              type: string
              enum:
                - deposit
                - withdrawal
                - futures partial liquidation
                - futures assignment
                - futures assignor
                - futures assignee
                - futures liquidation
                - futures_unwind
                - settlement
                - futures trade
                - admin transfer
                - transfer
                - subaccount transfer
                - fee credit
                - legacy
                - transfers fee
                - referral
                - funding rate change
                - revenue share
                - cross-exchange transfer
                - cross-exchange transfer failed
                - spot trade
                - spot fee credit
                - margin trade
                - margin position settlement
                - conversion credit
                - loan transfer
                - conversion
                - interest payment
                - interest payment credit
                - futures unwind bankrupt
                - futures unwind counterparty
                - kfee applied
                - covered liquidation
                - position transfer
                - portfolio auctioning
                - external custody delegation
                - external custody undelegation
                - external custody unbind
                - futures tax withheld
                - futures tax refund
                - tax conversion
                - options trade
                - hedging trade
                - rfq
                - funding rate payment - cash dividend
                - funding rate payment - spin off
                - funding rate payment - rights distribution
                - funding rate payment - cashflow
            example:
              - futures trade
        - description: Amount of entries to be returned.
          name: count
          in: query
          required: false
          schema:
            type: integer
            default: 500
        - description: Include exchange rate and conversion fee for conversions.
          name: conversion_details
          in: query
          required: false
          schema:
            type: boolean
            default: false
      responses:
        '200':
          description: Account log.
          content:
            application/json:
              schema:
                title: Account Log Response
                type: object
                properties:
                  accountUid:
                    $ref: '#/components/schemas/AccountUid'
                  logs:
                    type: array
                    items:
                      $ref: '#/components/schemas/AccountLogEntry'
                required:
                  - accountUid
                  - logs
        '429':
          $ref: '#/components/responses/RateLimited'
      security:
        - general-api-key-read-only: []
          authent: []
components:
  schemas:
    TimestampMilliseconds:
      type: integer
      format: timestamp-milliseconds
      example: 1604937694000
    AccountUid:
      description: UID of the account
      type: string
      format: uuid
    AccountLogEntry:
      description: Account log entry
      type: object
      properties:
        asset:
          description: Asset related with the entry.
          type: string
        booking_uid:
          description: UID of the log entry.
          type: string
          format: uuid
        collateral:
          description: Currency of the associated entry.
          type:
            - string
            - 'null'
        contract:
          type:
            - string
            - 'null'
        date:
          $ref: '#/components/schemas/Rfc3339DateTime'
        execution:
          description: >
            UID of the associated execution or transfer.


            For orders and trades, this is always a UUID. However, this field is
            also populated with

            "cross-exchange transfer" references, which are not always UUIDs.
          type:
            - string
            - 'null'
        fee:
          description: Fee paid
          type:
            - number
            - 'null'
          format: double
        funding_rate:
          description: Absolute funding rate at time of entry.
          type:
            - number
            - 'null'
          format: double
        id:
          description: Log entry ID.
          type: integer
          format: int64
          minimum: 1
        info:
          description: Short description of the entry.
          type: string
          enum:
            - deposit
            - withdrawal
            - futures partial liquidation
            - futures assignment
            - futures assignor
            - futures assignee
            - futures liquidation
            - futures_unwind
            - settlement
            - futures trade
            - admin transfer
            - transfer
            - subaccount transfer
            - fee credit
            - legacy
            - transfers fee
            - referral
            - funding rate change
            - revenue share
            - cross-exchange transfer
            - cross-exchange transfer failed
            - spot trade
            - spot fee credit
            - margin trade
            - margin position settlement
            - conversion credit
            - loan transfer
            - conversion
            - interest payment
            - interest payment credit
            - futures unwind bankrupt
            - futures unwind counterparty
            - kfee applied
            - covered liquidation
            - position transfer
            - portfolio auctioning
            - external custody delegation
            - external custody undelegation
            - external custody unbind
            - futures tax withheld
            - futures tax refund
            - tax conversion
            - options trade
            - hedging trade
            - rfq
            - funding rate payment - cash dividend
            - funding rate payment - spin off
            - funding rate payment - rights distribution
            - funding rate payment - cashflow
        margin_account:
          description: Name of the wallet associated with the entry.
          type: string
        mark_price:
          description: Mark price at the time the trade was executed.
          type:
            - number
            - 'null'
          format: double
        new_average_entry_price:
          description: Average entry price of the position after this trade.
          type:
            - number
            - 'null'
          format: double
        new_balance:
          description: >
            New balance of wallet or new size of the position after the
            described in info action.
          type: number
          format: double
        old_average_entry_price:
          description: Average entry price of the position prior to this trade.
          type:
            - number
            - 'null'
          format: double
        old_balance:
          description: Account balance before the described in info action.
          type: number
          format: double
        realized_funding:
          description: >-
            Funding realized due to change in position size or end of funding
            rate period.
          type:
            - number
            - 'null'
          format: double
        realized_pnl:
          description: PnL that is realized by reducing the position.
          type:
            - number
            - 'null'
          format: double
        trade_price:
          description: Price at which the trade was executed.
          type:
            - number
            - 'null'
          format: double
        conversion_spread_percentage:
          description: Percentage conversion spread used in a currency conversion.
          type:
            - number
            - 'null'
          format: double
        liquidation_fee:
          description: |
            Liquidation fee associated with a liquidation/assignment entry.

            Not applicable for inverse futures.
          type:
            - number
            - 'null'
          format: double
        exchange_rate:
          description: The exchange rate used for the conversion, USD quote.
          type: number
          format: double
        conversion_fee:
          description: The percentage fee charged for the conversion. E.g. 0.05 = 0.05%.
          type: number
          format: double
        exchange_rate_from:
          description: The currency code of the base currency in the exchange rate.
          type: string
      required:
        - asset
        - booking_uid
        - collateral
        - contract
        - date
        - execution
        - fee
        - funding_rate
        - id
        - info
        - margin_account
        - mark_price
        - new_average_entry_price
        - new_balance
        - old_average_entry_price
        - old_balance
        - realized_funding
        - realized_pnl
        - trade_price
        - conversion_spread_percentage
        - liquidation_fee
    Rfc3339DateTime:
      description: RFC 3339 formatted date-time
      type: string
      format: date-time
      example: '2019-08-24T14:15:22Z'
  responses:
    RateLimited:
      description: Rate limited.
      content:
        text/plain:
          schema:
            type: string
      headers:
        rate-limit-reset:
          description: >-
            Time remaining (in seconds) until repeat request (i.e., same cost)
            will be accepted.
          schema:
            type: integer
            minimum: 1
  securitySchemes:
    general-api-key-read-only:
      type: apiKey
      description: General API key with at least **read-only** access
      in: header
      name: APIKey
      x-inlineDescription: true
    authent:
      type: apiKey
      description: Authentication string
      in: header
      name: Authent
      x-inlineDescription: true

````
