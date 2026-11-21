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
source_url: 'https://docs.polymarket.com/api-reference/markets/list-market-clarifications'
updated_at: 2026-11-21
---

# List market clarifications

> Returns published clarifications, the notes that resolve ambiguity in how a market settles.



## OpenAPI

````yaml /api-spec/gamma-openapi.yaml get /market-clarifications
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
  /market-clarifications:
    get:
      tags:
        - Markets
      summary: List market clarifications
      description: >-
        Returns published clarifications, the notes that resolve ambiguity in
        how a market settles.
      operationId: listMarketClarifications
      parameters:
        - name: limit
          in: query
          schema:
            type: integer
            minimum: 0
            maximum: 100
            default: 20
        - $ref: '#/components/parameters/offset'
        - $ref: '#/components/parameters/order'
        - $ref: '#/components/parameters/ascending'
        - name: market_id
          in: query
          description: Market IDs. Repeat the parameter to pass several.
          style: form
          explode: true
          schema:
            type: array
            items:
              type: integer
        - name: event_id
          in: query
          description: Event IDs. Repeat the parameter to pass several.
          style: form
          explode: true
          schema:
            type: array
            items:
              type: integer
        - name: question_id
          in: query
          description: Question IDs. Repeat the parameter to pass several.
          style: form
          explode: true
          schema:
            type: array
            items:
              type: string
        - name: tx_hash
          in: query
          description: Transaction hash that posted the clarification.
          schema:
            type: string
      responses:
        '200':
          description: Market clarifications
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/MarketClarification'
components:
  parameters:
    offset:
      name: offset
      in: query
      schema:
        type: integer
        minimum: 0
    order:
      name: order
      in: query
      schema:
        type: string
      description: Comma-separated list of fields to order by
    ascending:
      name: ascending
      in: query
      schema:
        type: boolean
  schemas:
    MarketClarification:
      type: object
      properties:
        id:
          type: integer
        marketId:
          type: integer
          nullable: true
        eventId:
          type: integer
          nullable: true
        questionId:
          type: string
          nullable: true
        content:
          type: string
          nullable: true
          description: Clarification text.
        state:
          type: string
          nullable: true
          enum:
            - pending
            - queued
            - success
            - failed
            - cancelled
        clearBook:
          type: boolean
          nullable: true
          description: Whether open orders were cleared when the clarification was posted.
        notifyDiscord:
          type: boolean
          nullable: true
        showInFrontend:
          type: boolean
          nullable: true
        adapterAddress:
          type: string
          nullable: true
        negRiskRequestId:
          type: string
          nullable: true
        txHash:
          type: string
          nullable: true
        createdAt:
          type: string
          format: date-time
          nullable: true
        queuedAt:
          type: string
          format: date-time
          nullable: true
        scheduledFor:
          type: string
          format: date-time
          nullable: true
        txTimestamp:
          type: string
          format: date-time
          nullable: true

````

This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
