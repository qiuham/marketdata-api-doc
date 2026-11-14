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
source_url: 'https://docs.kraken.com/api-reference/market-history/get-public-order-events'
updated_at: 2026-11-13
---

# Get public order events

> Lists order events for a market.




## OpenAPI

````yaml /openapi/futures-history-rest.yaml get /market/{tradeable}/orders
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
  /market/{tradeable}/orders:
    get:
      tags:
        - Market History
      summary: Get public order events
      description: |
        Lists order events for a market.
      operationId: getPublicOrderEvents
      parameters:
        - $ref: '#/components/parameters/SinceDateFilter'
        - $ref: '#/components/parameters/BeforeDateFilter'
        - $ref: '#/components/parameters/SortOrder'
        - $ref: '#/components/parameters/ContinuationToken'
        - $ref: '#/components/parameters/CountPublic'
        - name: tradeable
          in: path
          required: true
          schema:
            type: string
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: object
                properties:
                  len:
                    type: integer
                    format: uint64
                  elements:
                    type: array
                    items:
                      $ref: '#/components/schemas/HistoricalOrderElementSanitized'
                  continuationToken:
                    $ref: '#/components/schemas/NextContinuationToken'
                required:
                  - len
                  - elements
      security:
        - {}
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
  schemas:
    HistoricalOrderElementSanitized:
      type: object
      properties:
        uid:
          type: string
        timestamp:
          $ref: '#/components/schemas/TimestampMilliseconds'
        event:
          $ref: '#/components/schemas/HistoricalOrderEventSanitized'
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
    HistoricalOrderEventSanitized:
      type: object
      oneOf:
        - type: object
          properties:
            OrderPlaced:
              $ref: '#/components/schemas/OrderPlacedSanitized'
          required:
            - OrderPlaced
        - type: object
          properties:
            OrderUpdated:
              $ref: '#/components/schemas/OrderUpdatedSanitized'
          required:
            - OrderUpdated
        - type: object
          properties:
            OrderCancelled:
              $ref: '#/components/schemas/OrderCancelledSanitized'
          required:
            - OrderCancelled
    OrderPlacedSanitized:
      type: object
      properties:
        order:
          $ref: '#/components/schemas/HistoricalOrderSanitized'
        reason:
          type: string
        reducedQuantity:
          description: always empty string
          type: string
      required:
        - order
        - reason
        - reducedQuantity
    OrderUpdatedSanitized:
      type: object
      properties:
        oldOrder:
          $ref: '#/components/schemas/HistoricalOrderSanitized'
        newOrder:
          $ref: '#/components/schemas/HistoricalOrderSanitized'
        reason:
          type: string
        reducedQuantity:
          $ref: '#/components/schemas/Decimal'
      required:
        - oldOrder
        - newOrder
        - reason
        - reducedQuantity
    OrderCancelledSanitized:
      type: object
      properties:
        order:
          $ref: '#/components/schemas/HistoricalOrderSanitized'
        reason:
          type: string
      required:
        - order
        - reason
    HistoricalOrderSanitized:
      type: object
      properties:
        uid:
          type: string
          format: uuid
        tradeable:
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
        timestamp:
          $ref: '#/components/schemas/TimestampMilliseconds'
        limitPrice:
          $ref: '#/components/schemas/Decimal'
        orderType:
          type: string
        reduceOnly:
          type: boolean
        lastUpdateTimestamp:
          $ref: '#/components/schemas/TimestampMilliseconds'
      required:
        - uid
        - tradeable
        - direction
        - quantity
        - timestamp
        - limitPrice
        - orderType
        - reduceOnly
        - lastUpdateTimestamp
    Decimal:
      type: string
      format: decimal
      example: '1234.56789'

````
