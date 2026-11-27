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
source_url: 'https://docs.polymarket.com/cn/api-reference/rebates/get-taker-tiers-for-addresses'
updated_at: 2026-11-27
---

# 获取地址的 Taker 等级

> Current taker tier and 30-day weighted volume for up to 100 proxy-wallet (or EOA) addresses. Addresses are case-insensitive; unknown addresses return tier 0. No authentication.




## OpenAPI

````yaml api-spec/gamma-openapi.yaml POST /tiers
openapi: 3.0.3
info:
  title: Markets API
  version: 1.0.0
  description: REST API specification for public endpoints used by the Markets service.
servers:
  - url: https://gamma-api.polymarket.com
    description: Polymarket Gamma API Production Server
security: []
tags:
  - name: Gamma Status
    description: Gamma API status and health check
  - name: Sports
    description: Sports-related endpoints including teams and game data
  - name: Tags
    description: Tag management and related tag operations
  - name: Events
    description: Event management and event-related operations
  - name: Markets
    description: Market data and market-related operations
  - name: Comments
    description: Comment system and user interactions
  - name: Series
    description: Series management and related operations
  - name: Profiles
    description: User profile management
  - name: Search
    description: Search functionality across different entity types
  - name: taker-tier
    description: Taker rebate tiers and weighted volume
  - name: maker-tier
    description: Maker rebate tiers and weighted volume
paths:
  /tiers:
    post:
      tags:
        - taker-tier
      summary: Get taker tiers for addresses
      description: >
        Current taker tier and 30-day weighted volume for up to 100 proxy-wallet
        (or EOA) addresses. Addresses are case-insensitive; unknown addresses
        return tier 0. No authentication.
      operationId: get-taker-tiers
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              additionalProperties: false
              required:
                - addresses
              properties:
                addresses:
                  type: array
                  items:
                    type: string
                  minItems: 1
                  maxItems: 100
            example:
              addresses:
                - '0xa4b7b1814b0da33f2b61be4939976898aa476008'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                type: object
                required:
                  - tiers
                properties:
                  tiers:
                    type: array
                    items:
                      type: object
                      required:
                        - address
                        - tier
                        - tier_name
                        - wv_30d
                      properties:
                        address:
                          type: string
                        tier:
                          type: integer
                        tier_name:
                          type: string
                        wv_30d:
                          type: number
                          format: double
              example:
                tiers:
                  - address: '0xa4b7b1814b0da33f2b61be4939976898aa476008'
                    tier: 6
                    tier_name: Obsidian
                    wv_30d: 17189511.9883
        '422':
          description: Empty or invalid address, or more than 100 addresses
      security: []

````

This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
