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
source_url: 'https://docs.kraken.com/api-reference/settlement/settle-prime-settlement-batch-asset'
updated_at: 2026-11-13
---

# Settle Prime Settlement Batch Asset

> Initiates settlement of a specific asset leg within a Prime settlement batch. The batch must be confirmed and the leg must be eligible for settlement (check `can_settle` on the leg).
Only `outgoing` legs (assets you owe to Kraken) are settled with this endpoint. Kraken settles `incoming` legs.
Returns `EOTC:Conflict:settlement batch is not confirmed` if the batch has not been confirmed yet, and `EOTC:Conflict:settlement batch leg is locked` if the leg is already settled or being settled. Calling this endpoint again for a leg that was already settled is therefore safe.

**API Key Permissions Required:** `Orders and trades - Create & modify orders`. API keys that belong to an organization also need `Prime Ops`; an organization key without it is rejected with `EGeneral:Permission denied:prime ops`.




## OpenAPI

````yaml /openapi/prime-rest.yaml post /0/private/SettlePrimeSettlementBatchAsset
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
  /0/private/SettlePrimeSettlementBatchAsset:
    post:
      tags:
        - Settlement
      summary: Settle Prime Settlement Batch Asset
      description: >
        Initiates settlement of a specific asset leg within a Prime settlement
        batch. The batch must be confirmed and the leg must be eligible for
        settlement (check `can_settle` on the leg).

        Only `outgoing` legs (assets you owe to Kraken) are settled with this
        endpoint. Kraken settles `incoming` legs.

        Returns `EOTC:Conflict:settlement batch is not confirmed` if the batch
        has not been confirmed yet, and `EOTC:Conflict:settlement batch leg is
        locked` if the leg is already settled or being settled. Calling this
        endpoint again for a leg that was already settled is therefore safe.


        **API Key Permissions Required:** `Orders and trades - Create & modify
        orders`. API keys that belong to an organization also need `Prime Ops`;
        an organization key without it is rejected with `EGeneral:Permission
        denied:prime ops`.
      operationId: settlePrimeSettlementBatchAsset
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/SettlePrimeSettlementBatchAsset'
      responses:
        '200':
          description: Asset settlement initiated.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SettlePrimeSettlementBatchAsset1'
        '500':
          $ref: '#/components/responses/500'
components:
  schemas:
    SettlePrimeSettlementBatchAsset:
      title: Settle Prime Settlement Batch Asset Request Body
      type: object
      properties:
        nonce:
          $ref: '#/components/schemas/Nonce'
        batch_id:
          type: string
          description: The unique identifier of the settlement batch.
          example: B_Y7T2LPVX
        asset:
          type: string
          description: The asset to settle within the batch.
          example: BTC
      additionalProperties: false
      required:
        - nonce
        - batch_id
        - asset
    SettlePrimeSettlementBatchAsset1:
      description: Response containing the transfer details for the settled asset.
      type: object
      properties:
        result:
          type: object
          properties:
            transfer:
              type: object
              description: Transfer details for the settled asset.
              properties:
                id:
                  type: string
                  description: Unique identifier for the transfer.
                  example: '100'
                attributes:
                  type: object
                  properties:
                    transfer_status:
                      type: string
                      enum:
                        - pending
                        - completed
                        - failed
                      example: pending
                    transfer_amount:
                      type: string
                      description: Amount being transferred.
                      example: '1.5'
                    transfer_asset:
                      type: string
                      description: Asset being transferred.
                      example: BTC
                  required:
                    - transfer_status
                    - transfer_amount
                    - transfer_asset
                relationships:
                  type: object
                  properties:
                    leg:
                      $ref: '#/components/schemas/BatchLeg'
                  required:
                    - leg
              required:
                - id
                - attributes
                - relationships
          required:
            - transfer
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
    Error:
      type: array
      description: Empty on success. On failure, contains one or more error strings.
      items:
        description: Kraken API error string
        type: string
        example: EOTC:Invalid arguments
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
