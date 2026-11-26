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
source_url: 'https://docs.polymarket.com/cn/api-reference/rebates/get-maker-tiers-for-addresses'
updated_at: 2026-11-26
---

# 获取地址的 Maker 等级

> Maker tier, rebate rate and 30-day weighted volume for up to 100 maker addresses, from the newest daily snapshot (the tier paying each address's fills today). Addresses are case-insensitive and matched as given against the address that made the fills (usually the proxy wallet). An address with no snapshot row returns tier 0 with no snapshot_date. No authentication.




## OpenAPI

````yaml api-spec/gamma-openapi.yaml POST /v1/maker-tier/tiers
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
  /v1/maker-tier/tiers:
    post:
      tags:
        - maker-tier
      summary: Get maker tiers for addresses
      description: >
        Maker tier, rebate rate and 30-day weighted volume for up to 100 maker
        addresses, from the newest daily snapshot (the tier paying each
        address's fills today). Addresses are case-insensitive and matched as
        given against the address that made the fills (usually the proxy
        wallet). An address with no snapshot row returns tier 0 with no
        snapshot_date. No authentication.
      operationId: get-maker-tiers
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
                  description: Maker addresses (proxy wallet or EOA), case-insensitive
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
                    description: >-
                      One entry per distinct requested address, in first-seen
                      request order
                    items:
                      type: object
                      required:
                        - address
                        - tier
                        - rebate_bps
                        - wv_30d
                        - own_wv_30d
                      properties:
                        address:
                          type: string
                          description: Normalized (trimmed, lowercased)
                        snapshot_date:
                          type: string
                          description: >-
                            UTC day (YYYY-MM-DD) whose fills this tier pays;
                            omitted when no snapshot row
                        tier:
                          type: integer
                          description: 0 when no snapshot row
                        rebate_bps:
                          type: integer
                          description: >-
                            Share of the taker fee each maker fill generates, in
                            basis points
                        wv_30d:
                          type: number
                          format: double
                          description: >-
                            30-day weighted volume pooled across the maker link
                            group
                        own_wv_30d:
                          type: number
                          format: double
                          description: This address's own share of wv_30d
              example:
                tiers:
                  - address: '0xa4b7b1814b0da33f2b61be4939976898aa476008'
                    snapshot_date: '2026-11-19'
                    tier: 1
                    rebate_bps: 300
                    wv_30d: 250000
                    own_wv_30d: 250000
        '422':
          description: Empty or invalid address, or more than 100 addresses
      security: []

````

This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
