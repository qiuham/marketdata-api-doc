---
api_type: reference
source_type: llms_txt
version: ''
scope: crypto
asset_class: prediction_market
domain: exchanges
provider: polymarket
provider_name: Polymarket
product: api
product_id: polymarket
source_url: 'https://docs.polymarket.com/api-reference/account/get-rate-limit-tier'
updated_at: 2026-11-13
---

# Get rate limit tier

> Returns the [trading rate limit tier](/api-reference/trading-rate-limits) currently assigned to your signer.
The tier returned is the one for the signer address of the API credentials used.

The response reflects the most recent tier refresh, so a change in volume can
take up to three hours to appear.




## OpenAPI

````yaml /api-spec/clob-openapi.yaml get /v1/user/rate-limit-tier
openapi: 3.1.0
info:
  title: Polymarket CLOB API
  description: Polymarket CLOB API Reference
  license:
    name: MIT
    identifier: MIT
  version: 1.0.0
servers:
  - url: https://clob.polymarket.com
    description: Production CLOB API
  - url: https://clob-staging.polymarket.com
    description: Staging CLOB API
security: []
tags:
  - name: Trade
    description: Trade endpoints
  - name: Markets
    description: Market data endpoints
  - name: Account
    description: Account and authentication endpoints
  - name: Notifications
    description: User notification endpoints
  - name: Rewards
    description: Rewards and earnings endpoints
  - name: Rebates
    description: Maker rebate endpoints
paths:
  /v1/user/rate-limit-tier:
    get:
      tags:
        - Account
      summary: Get rate limit tier
      description: >
        Returns the [trading rate limit
        tier](/api-reference/trading-rate-limits) currently assigned to your
        signer.

        The tier returned is the one for the signer address of the API
        credentials used.


        The response reflects the most recent tier refresh, so a change in
        volume can

        take up to three hours to appear.
      operationId: getRateLimitTier
      responses:
        '200':
          description: Successfully retrieved rate limit tier
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/RateLimitTierResponse'
              example:
                tier: gold
                usdc_volume: '612345.67'
                next_tier_threshold: 2500000
                period: 30
                tier_details:
                  name: gold
                  volume_threshold: 500000
                  cancel_rate_per_sec: 800
                  order_rate_per_sec: 400
                  order_burst: 600
                  cancel_burst: 1200
                  allow_negative: true
        '401':
          description: Unauthorized - Missing or invalid L2 credentials
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
              example:
                error: Unauthorized/Invalid api key
        '503':
          description: Service unavailable - Rate limit tiers could not be loaded
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
              example:
                error: rate limit tiers unavailable
      security:
        - polyApiKey: []
          polyAddress: []
          polySignature: []
          polyPassphrase: []
          polyTimestamp: []
components:
  schemas:
    RateLimitTierResponse:
      type: object
      description: Trading rate limit tier currently applied to the signer
      required:
        - tier
        - period
        - tier_details
      properties:
        tier:
          type: string
          description: Tier currently applied to your signer
          example: gold
        usdc_volume:
          type: string
          description: >-
            Trailing-window volume, in USDC, of the maker wallet that set your
            tier. Omitted below the lowest paid tier
          example: '612345.67'
        next_tier_threshold:
          type: integer
          description: >-
            30-day volume needed for the next tier. Omitted at the top tier and
            for manually assigned tiers
          example: 2500000
        period:
          type: integer
          description: Length of the volume window, in days
          example: 30
        tier_details:
          $ref: '#/components/schemas/RateLimitTierDetails'
    ErrorResponse:
      type: object
      required:
        - error
      properties:
        error:
          type: string
          description: Error message
        code:
          type: string
          description: Machine-readable error code, when provided
        retry_after_seconds:
          type: integer
          description: Number of seconds to wait before retrying, when provided
    RateLimitTierDetails:
      type: object
      description: Rate, burst and negative-balance settings for the tier
      properties:
        name:
          type: string
          description: Tier name
          example: gold
        volume_threshold:
          type: integer
          description: 30-day volume required for the tier
          example: 500000
        cancel_rate_per_sec:
          type: integer
          description: Cancel bucket refill rate, in tokens per second
          example: 800
        order_rate_per_sec:
          type: integer
          description: Order bucket refill rate, in tokens per second
          example: 400
        order_burst:
          type: integer
          description: Order bucket burst capacity, in tokens
          example: 600
        cancel_burst:
          type: integer
          description: Cancel bucket burst capacity, in tokens
          example: 1200
        allow_negative:
          type: boolean
          description: Whether the cancel bucket can carry a negative balance
          example: true
  securitySchemes:
    polyApiKey:
      type: apiKey
      in: header
      name: POLY_API_KEY
      description: Your API key
    polyAddress:
      type: apiKey
      in: header
      name: POLY_ADDRESS
      description: Ethereum address associated with the API key
    polySignature:
      type: apiKey
      in: header
      name: POLY_SIGNATURE
      description: HMAC signature of the request
    polyPassphrase:
      type: apiKey
      in: header
      name: POLY_PASSPHRASE
      description: API key passphrase
    polyTimestamp:
      type: apiKey
      in: header
      name: POLY_TIMESTAMP
      description: Unix timestamp of the request

````

This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
