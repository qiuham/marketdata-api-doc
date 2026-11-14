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
source_url: 'https://docs.kraken.com/api-reference/settlement/list-prime-settlement-batches'
updated_at: 2026-11-13
---

# List Prime Settlement Batches

> Retrieves a list of Prime settlement batches, optionally filtered by status and time range. Results are sorted by creation time, most recent first.

**API Key Permissions Required:** `Orders and trades - Query open orders & trades` and `Orders and trades - Query closed orders & trades`. Both permissions are required; a key with only one of them is rejected with `EGeneral:Permission denied`.




## OpenAPI

````yaml /openapi/prime-rest.yaml post /0/private/ListPrimeSettlementBatches
openapi: 3.0.0
info:
  title: Prime REST API
  version: 1.0.0
  description: >
    Kraken Prime REST API — institutional-grade settlement and API-user
    management. Companion REST surface to the Prime FIX and Prime WebSocket
    APIs.


    **Authentication.** These endpoints use the standard Kraken REST
    authentication (`API-Key` and `API-Sign` headers, with a `nonce` in the
    request body). Use a standard Kraken API key with the permissions listed on
    each endpoint. Keys created for Prime API users with `CreatePrimeApiUserKey`
    are for the Prime WebSocket API only.
servers:
  - url: https://api.kraken.com
    description: Production Server
security:
  - API-Key: []
    API-Sign: []
tags:
  - name: Settlement
  - name: API Users
  - name: API User Keys
paths:
  /0/private/ListPrimeSettlementBatches:
    post:
      tags:
        - Settlement
      summary: List Prime Settlement Batches
      description: >
        Retrieves a list of Prime settlement batches, optionally filtered by
        status and time range. Results are sorted by creation time, most recent
        first.


        **API Key Permissions Required:** `Orders and trades - Query open orders
        & trades` and `Orders and trades - Query closed orders & trades`. Both
        permissions are required; a key with only one of them is rejected with
        `EGeneral:Permission denied`.
      operationId: listPrimeSettlementBatches
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ListPrimeSettlementBatches'
      responses:
        '200':
          description: Settlement batches retrieved.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListPrimeSettlementBatches1'
        '500':
          $ref: '#/components/responses/500'
components:
  schemas:
    ListPrimeSettlementBatches:
      title: List Prime Settlement Batches Request Body
      type: object
      properties:
        nonce:
          $ref: '#/components/schemas/Nonce'
        statuses:
          type: array
          description: Filter batches by status. If omitted, all statuses are returned.
          items:
            type: string
            enum:
              - unsettled
              - partially_settled
              - settled
              - completed
          example:
            - unsettled
            - partially_settled
        from:
          type: integer
          format: int64
          description: >-
            Unix timestamp in milliseconds. Only return batches created after
            this time (exclusive).
          example: 1700000000000
        until:
          type: integer
          format: int64
          description: >-
            Unix timestamp in milliseconds. Only return batches created before
            or at this time (inclusive).
          example: 1700100000000
        limit:
          type: integer
          format: int64
          description: Maximum number of batches to return. Defaults to 50, maximum 200.
          default: 50
          maximum: 200
          example: 20
        offset:
          type: integer
          format: int64
          description: Number of batches to skip, for pagination.
          example: 0
      additionalProperties: false
      required:
        - nonce
    ListPrimeSettlementBatches1:
      description: Response containing a paginated list of Prime settlement batches.
      type: object
      properties:
        result:
          type: object
          properties:
            data:
              type: array
              description: List of settlement batches.
              items:
                $ref: '#/components/schemas/SettlementBatch'
            pagination:
              type: object
              description: Pagination metadata for the current result set.
              properties:
                has_more:
                  type: boolean
                  description: Whether there are more batches beyond the current page.
                limit:
                  type: integer
                  format: int64
                  description: Maximum number of items requested for the current page.
                offset:
                  type: integer
                  format: int64
                  description: Offset used to fetch the current page.
              required:
                - has_more
                - limit
                - offset
          required:
            - data
            - pagination
          additionalProperties: false
        error:
          $ref: '#/components/schemas/Error'
      required:
        - result
        - error
      additionalProperties: false
    Nonce:
      description: Nonce used in construction of `API-Sign` header
      type: integer
      format: int64
    SettlementBatch:
      description: Prime settlement batch data.
      type: object
      properties:
        id:
          type: string
          description: Unique identifier for the settlement batch.
          example: B_Y7T2LPVX
        attributes:
          type: object
          description: Batch attributes.
          properties:
            status:
              type: string
              description: >
                Current status of the batch.

                - `unsettled` — The batch has no legs settled.

                - `partially_settled` — The batch has some but not all legs
                settled.

                - `settled` — The batch has all legs settled.

                - `completed` — The batch has been settled and fully processed.
              enum:
                - unsettled
                - partially_settled
                - settled
                - completed
              example: unsettled
            confirmed:
              type: boolean
              description: Whether the batch has been confirmed by Prime's system.
              example: false
            created_at:
              type: integer
              format: int64
              description: Unix timestamp in milliseconds when the batch was created.
              example: 1700000000000
            updated_at:
              type: integer
              format: int64
              nullable: true
              description: Unix timestamp in milliseconds when the batch was last updated.
              example: 1700000100000
            trade_count:
              type: integer
              format: int64
              description: Number of trades in the batch.
              example: 5
            asset_kind:
              type: string
              description: |
                Kind of assets included in the settlement batch.
                - `currency` — Fiat and cryptocurrency positions.
                - `tokenized_equity` — Tokenized equity positions.
              enum:
                - currency
                - tokenized_equity
              example: currency
          required:
            - status
            - confirmed
            - created_at
            - trade_count
            - asset_kind
        legs:
          type: array
          description: Settlement batch legs.
          items:
            $ref: '#/components/schemas/BatchLeg'
        trade_ids:
          type: array
          description: >-
            Trade IDs included in the batch. Returned by Get Prime Settlement
            Batch and Create Prime Settlement Batch.
          items:
            type: string
          example:
            - 3f435d6b-62fd-4f26-b1c5-68ef573d93ef
            - 7f6a6d75-6470-4f65-8b24-9858f28ede83
      required:
        - id
        - attributes
        - legs
    Error:
      type: array
      description: Empty on success. On failure, contains one or more error strings.
      items:
        description: Kraken API error string
        type: string
        example: EOTC:Invalid arguments
    BatchLeg:
      description: >-
        A leg of a Prime settlement batch representing a single asset's net
        position.
      type: object
      properties:
        status:
          type: string
          description: >
            Current settlement status of the leg.

            - `unsettled` — No settlement has been initiated for this leg.

            - `partially_settled` — A settlement transfer has completed but did
            not cover the full amount.

            - `in_progress` — A settlement transfer is currently in progress.

            - `settled` — The leg has been fully settled.
          enum:
            - unsettled
            - partially_settled
            - in_progress
            - settled
          example: unsettled
        asset:
          type: string
          description: Asset being settled.
          example: BTC
        amount:
          type: string
          description: Net amount of the asset to be settled.
          example: '1.5'
        direction:
          type: string
          description: |
            Direction of the settlement from the client's perspective.
            - `incoming` — The client will receive this asset from Kraken.
            - `outgoing` — The client owes this asset to Kraken.
          enum:
            - incoming
            - outgoing
          example: outgoing
        can_settle:
          type: boolean
          description: >
            Whether this leg is eligible for settlement right now. Returns
            `false` if a spot transfer is already in progress or the leg is
            already settled. For `incoming` legs (client receives), settlement
            is handled by Kraken and this is always `false`. This flag does not
            reflect batch confirmation: it can be `true` on a batch that is not
            yet confirmed, and settling that leg returns
            `EOTC:Conflict:settlement batch is not confirmed` until the batch is
            confirmed.
          example: true
        settled_at:
          type: integer
          format: int64
          nullable: true
          description: >-
            Unix timestamp in milliseconds when the leg was settled. Null if not
            yet settled.
        latest_spot_transfer:
          nullable: true
          description: The most recent spot transfer associated with this leg, if any.
          type: object
          additionalProperties: true
      required:
        - status
        - asset
        - amount
        - direction
        - can_settle
  responses:
    '500':
      description: Internal Server Error
      content:
        application/json:
          schema:
            type: object
            properties:
              error:
                type: array
                items:
                  type: string
            required:
              - error
  securitySchemes:
    API-Key:
      type: apiKey
      description: The "API-Key" header should contain your API key.
      name: API-Key
      in: header
    API-Sign:
      type: apiKey
      description: >-
        Authenticated requests should be signed with the "API-Sign" header,
        using a signature generated with your private key, nonce, encoded
        payload, and URI path.
      name: API-Sign
      in: header

````
