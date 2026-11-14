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
source_url: 'https://docs.kraken.com/api-reference/account-history/get-order-events'
updated_at: 2026-11-13
---

# Get order events

> Lists order events for authenticated account.




## OpenAPI

````yaml /openapi/futures-history-rest.yaml get /orders
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
  /orders:
    get:
      tags:
        - Account History
      summary: Get order events
      description: |
        Lists order events for authenticated account.
      operationId: getOrderEvents
      parameters:
        - $ref: '#/components/parameters/SinceDateFilter'
        - $ref: '#/components/parameters/BeforeDateFilter'
        - $ref: '#/components/parameters/SortOrder'
        - $ref: '#/components/parameters/ContinuationToken'
        - $ref: '#/components/parameters/CountPublic'
        - $ref: '#/components/parameters/Tradeable'
        - $ref: '#/components/parameters/OpenedOrder'
        - $ref: '#/components/parameters/ClosedOrder'
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: object
                properties:
                  accountUid:
                    type: string
                    format: uuid
                  len:
                    type: integer
                    format: uint64
                  serverTime:
                    type: string
                    format: date-time
                  elements:
                    type: array
                    items:
                      $ref: '#/components/schemas/HistoricalOrderElement'
                  continuationToken:
                    $ref: '#/components/schemas/NextContinuationToken'
                required:
                  - accountUid
                  - len
                  - elements
      security:
        - general-api-key-read-only: []
          authent: []
components:
  parameters:
    SinceDateFilter:
      name: since
      in: query
      description: Timestamp in milliseconds.
      schema:
        $ref: '#/components/schemas/TimestampMilliseconds'
    BeforeDateFilter:
      name: before
      in: query
      description: Timestamp in milliseconds.
      schema:
        $ref: '#/components/schemas/TimestampMilliseconds'
    SortOrder:
      name: sort
      in: query
      description: |
        Determines the order of events in response(s).

        - `asc` = chronological
        - `desc` = reverse-chronological
      required: false
      schema:
        type: string
        enum:
          - asc
          - desc
        default: desc
        x-exhaustive: true
    ContinuationToken:
      name: continuation_token
      in: query
      description: >
        Opaque token from the `Next-Continuation-Token` header used to continue
        listing events. The

        `sort` parameter must be the same as in the previous request to continue
        listing in the same

        direction.
      schema:
        type: string
        format: base64
    CountPublic:
      name: count
      in: query
      description: >
        The maximum number of results to return. Larger values are not rejected,
        they are silently

        capped at 1000; when more events match, the `Next-Continuation-Token`
        header is returned to

        continue the listing.
      schema:
        type: integer
        format: int64
        minimum: 1
        x-rustType: usize
    Tradeable:
      description: If present events of other tradeables are filtered out.
      name: tradeable
      in: query
      required: false
      schema:
        type: string
    OpenedOrder:
      name: opened
      in: query
      schema:
        type: boolean
      description: >
        Determines status of the orders that should be included in response(s).


        - `true` = return orders that have been placed within given time range.

        - `false` = don't return orders that have been placed within given time
        range.
      required: false
    ClosedOrder:
      name: closed
      in: query
      schema:
        type: boolean
      description: >
        Determines status of the order that should be included in response(s).


        - `true` = return orders that have been closed/cancelled/rejected within
        given time range.

        - `false` = don't return orders that have been closed/cancelled/rejected
        within given time range.
      required: false
  schemas:
    HistoricalOrderElement:
      type: object
      properties:
        uid:
          type: string
        timestamp:
          $ref: '#/components/schemas/TimestampMilliseconds'
        event:
          $ref: '#/components/schemas/HistoricalOrderEvent'
      required:
        - uid
        - timestamp
        - event
    NextContinuationToken:
      description: >
        Opaque token to pass to the next request to continue listing events. The
        `sort` parameter

        must be the same as in the previous request to continue listing in the
        same direction.
      type: string
      format: base64
    TimestampMilliseconds:
      type: integer
      format: timestamp-milliseconds
      example: 1604937694000
    HistoricalOrderEvent:
      type: object
      oneOf:
        - type: object
          properties:
            OrderPlaced:
              $ref: '#/components/schemas/OrderPlaced'
          required:
            - OrderPlaced
        - type: object
          properties:
            OrderUpdated:
              $ref: '#/components/schemas/OrderUpdated'
          required:
            - OrderUpdated
        - type: object
          properties:
            OrderRejected:
              $ref: '#/components/schemas/OrderRejected'
          required:
            - OrderRejected
        - type: object
          properties:
            OrderCancelled:
              $ref: '#/components/schemas/OrderCancelled'
          required:
            - OrderCancelled
        - type: object
          properties:
            OrderNotFound:
              $ref: '#/components/schemas/OrderNotFound'
          required:
            - OrderNotFound
        - type: object
          properties:
            OrderEditRejected:
              $ref: '#/components/schemas/OrderEditRejected'
          required:
            - OrderEditRejected
    OrderPlaced:
      type: object
      properties:
        order:
          $ref: '#/components/schemas/HistoricalOrder'
        reason:
          type: string
        reducedQuantity:
          description: always empty string
          type: string
      required:
        - order
        - reason
        - reducedQuantity
    OrderUpdated:
      type: object
      properties:
        oldOrder:
          $ref: '#/components/schemas/HistoricalOrder'
        newOrder:
          $ref: '#/components/schemas/HistoricalOrder'
        reason:
          type: string
        reducedQuantity:
          $ref: '#/components/schemas/Decimal'
      required:
        - oldOrder
        - newOrder
        - reason
        - reducedQuantity
    OrderRejected:
      type: object
      properties:
        order:
          $ref: '#/components/schemas/HistoricalOrder'
        orderError:
          type: string
        reason:
          type: string
      required:
        - order
        - orderError
        - reason
    OrderCancelled:
      type: object
      properties:
        order:
          $ref: '#/components/schemas/HistoricalOrder'
        reason:
          type: string
      required:
        - order
        - reason
    OrderNotFound:
      type: object
      properties:
        accountUid:
          type: string
          format: uuid
        orderId:
          type: string
          example: Uuid(uuid=2ceb1d31-f619-457b-870c-fd4ddbb10d45)
      required:
        - accountUid
        - orderId
    OrderEditRejected:
      type: object
      properties:
        oldOrder:
          $ref: '#/components/schemas/HistoricalOrder'
        attemptedOrder:
          $ref: '#/components/schemas/HistoricalOrder'
        orderError:
          type: string
      required:
        - oldOrder
        - attemptedOrder
        - orderError
    HistoricalOrder:
      type: object
      properties:
        uid:
          type: string
          format: uuid
        accountUid:
          type: string
          format: uuid
        tradeable:
          type: string
        positionUid:
          type: string
        direction:
          description: >
            `Unknown` is returned when the source value couldn't be decoded;
            this will be replaced with a real value as soon as possible.
          type: string
          enum:
            - Buy
            - Sell
            - Unknown
        quantity:
          $ref: '#/components/schemas/Decimal'
        filled:
          $ref: '#/components/schemas/Decimal'
        timestamp:
          $ref: '#/components/schemas/TimestampMilliseconds'
        limitPrice:
          $ref: '#/components/schemas/Decimal'
        orderType:
          description: >
            `Unknown` is returned when the source value couldn't be decoded;
            this will be replaced with a real value as soon as possible.
          type: string
          enum:
            - Limit
            - IoC
            - Post
            - Liquidation
            - Assignment
            - Stop
            - Unwind
            - Market
            - Block
            - CoveredLiquidation
            - HedgeImmediateOrCancel
            - HedgeAssignment
            - FillOrKill
            - Rfq
            - PartialLiquidation
            - Unknown
        clientId:
          type: string
        reduceOnly:
          type: boolean
        lastUpdateTimestamp:
          $ref: '#/components/schemas/TimestampMilliseconds'
        spotData:
          $ref: '#/components/schemas/SpotOrderData'
        parentOfGroupId:
          type: string
        memberOfGroupId:
          type: string
        partnerOrderId:
          type: string
        regulatoryExternalUid:
          type: string
          format: uuid
      required:
        - uid
        - accountUid
        - tradeable
        - direction
        - quantity
        - filled
        - timestamp
        - limitPrice
        - orderType
        - clientId
        - reduceOnly
        - lastUpdateTimestamp
    Decimal:
      type: string
      format: decimal
      example: '1234.56789'
    SpotOrderData:
      type: object
      properties:
        margin:
          type: boolean
        feePreference:
          oneOf:
            - $ref: '#/components/schemas/BaseOrQuote'
            - type: 'null'
        quantityPreference:
          $ref: '#/components/schemas/BaseOrQuote'
      required:
        - margin
        - feePreference
        - quantityPreference
    BaseOrQuote:
      type: string
      enum:
        - Base
        - Quote
        - Unknown
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
