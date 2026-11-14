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
source_url: 'https://docs.kraken.com/api-reference/settlement/get-prime-settlement-batch'
updated_at: 2026-11-13
---

# Get Prime Settlement Batch

> Retrieves a specific Prime settlement batch by its ID, including all legs, their current settlement status,
external transfers that have settled each leg, and the trade IDs in the batch.

**API Key Permissions Required:** `Orders and trades - Query open orders & trades` and
`Orders and trades - Query closed orders & trades`. Both permissions are required; a key with only one of them
is rejected with `EGeneral:Permission denied`.




## OpenAPI

````yaml /openapi/prime-rest.yaml post /0/private/GetPrimeSettlementBatch
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
  /0/private/GetPrimeSettlementBatch:
    post:
      tags:
        - Settlement
      summary: Get Prime Settlement Batch
      description: >
        Retrieves a specific Prime settlement batch by its ID, including all
        legs, their current settlement status,

        external transfers that have settled each leg, and the trade IDs in the
        batch.


        **API Key Permissions Required:** `Orders and trades - Query open orders
        & trades` and

        `Orders and trades - Query closed orders & trades`. Both permissions are
        required; a key with only one of them

        is rejected with `EGeneral:Permission denied`.
      operationId: getPrimeSettlementBatch
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/GetPrimeSettlementBatch'
      responses:
        '200':
          description: Settlement batch retrieved.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetPrimeSettlementBatch1'
        '500':
          $ref: '#/components/responses/500'
components:
  schemas:
    GetPrimeSettlementBatch:
      title: Get Prime Settlement Batch Request Body
      type: object
      properties:
        nonce:
          $ref: '#/components/schemas/Nonce'
        batch_id:
          type: string
          description: The identifier of the settlement batch to retrieve.
          example: B_Y7T2LPVX
      additionalProperties: false
      required:
        - nonce
        - batch_id
    GetPrimeSettlementBatch1:
      description: Response containing a single Prime settlement batch.
      type: object
      properties:
        result:
          type: object
          properties:
            batch:
              $ref: '#/components/schemas/GetSettlementBatch'
          required:
            - batch
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
    GetSettlementBatch:
      description: Prime settlement batch data returned by Get Prime Settlement Batch.
      allOf:
        - $ref: '#/components/schemas/SettlementBatch'
        - type: object
          properties:
            legs:
              type: array
              description: >-
                Settlement batch legs, including external transfers that have
                settled each leg.
              items:
                $ref: '#/components/schemas/GetBatchLeg'
    Error:
      type: array
      description: Empty on success. On failure, contains one or more error strings.
      items:
        description: Kraken API error string
        type: string
        example: EOTC:Invalid arguments
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
    GetBatchLeg:
      description: A settlement batch leg returned by Get Prime Settlement Batch.
      allOf:
        - $ref: '#/components/schemas/BatchLeg'
        - type: object
          properties:
            transfers:
              type: array
              nullable: true
              description: >-
                External transfers that have settled this leg. Omitted when no
                transfers exist.
              items:
                $ref: '#/components/schemas/BatchLegTransfer'
              example:
                - external_transfer_id: TOH3AS2-LPCWR8-JDQGEU
                  amount: '13'
                - external_transfer_id: TJKLXF-PGMUI-4NTLXU
                  amount: '10'
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
    BatchLegTransfer:
      description: External transfer associated with a batch leg.
      type: object
      properties:
        external_transfer_id:
          type: string
          description: External transfer identifier.
          example: TOH3AS2-LPCWR8-JDQGEU
        amount:
          type: string
          description: Amount transferred.
          example: '13'
      required:
        - external_transfer_id
        - amount
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
