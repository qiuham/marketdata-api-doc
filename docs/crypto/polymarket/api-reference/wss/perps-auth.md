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
source_url: 'https://docs.polymarket.com/api-reference/wss/perps-auth'
updated_at: 2026-11-13
---

# Auth

> Perps WebSocket authentication.



## AsyncAPI

````yaml asyncapi-perps.json auth
id: auth
title: Auth
description: Authentication to access private channels.
servers:
  - id: production
    protocol: wss
    host: ws.perpetuals.polymarket.com
    bindings: []
    variables: []
address: /v1/ws
parameters: []
bindings: []
operations:
  - &ref_1
    id: AuthSend
    title: Auth send
    description: Authenticate connection
    type: receive
    messages:
      - &ref_3
        id: Request
        contentType: application/json
        payload:
          - name: Auth
            description: Authenticate this WebSocket connection for private channels
            type: object
            properties:
              - name: id
                type: integer
                description: Correlation ID for request-response matching
                required: false
              - name: req
                type: string
                description: Request type
                enumValues:
                  - post
                  - sub
                  - unsub
                required: true
              - name: op
                type: object
                required: true
                properties:
                  - name: type
                    type: string
                    enumValues:
                      - auth
                    required: true
                  - name: args
                    type: object
                    required: true
                    properties:
                      - name: proxy
                        type: string
                        description: Proxy address in hex format
                        required: true
                      - name: secret
                        type: string
                        description: API secret
                        required: true
        headers: []
        jsonPayloadSchema:
          type: object
          title: Base Request
          properties:
            id:
              type: integer
              description: Correlation ID for request-response matching
              x-parser-schema-id: <anonymous-schema-218>
            req:
              type: string
              description: Request type
              enum:
                - post
                - sub
                - unsub
              x-parser-schema-id: <anonymous-schema-219>
            op:
              type: object
              required:
                - type
                - args
              properties:
                type:
                  type: string
                  enum:
                    - auth
                  x-parser-schema-id: <anonymous-schema-221>
                args:
                  type: object
                  required:
                    - proxy
                    - secret
                  properties:
                    proxy:
                      type: string
                      description: Proxy address in hex format
                      example: '0x70997970C51812dc3A010C7d01b50e0d17dc79C8'
                      x-parser-schema-id: <anonymous-schema-223>
                    secret:
                      type: string
                      description: API secret
                      example: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
                      x-parser-schema-id: <anonymous-schema-224>
                  x-parser-schema-id: <anonymous-schema-222>
              x-parser-schema-id: <anonymous-schema-220>
          required:
            - req
            - op
          x-parser-schema-id: <anonymous-schema-217>
        title: Auth
        description: Authenticate this WebSocket connection for private channels
        example: |-
          {
            "req": "post",
            "op": {
              "type": "auth",
              "args": {
                "proxy": "0x70997970C51812dc3A010C7d01b50e0d17dc79C8",
                "secret": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
              }
            }
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: Request
    bindings: []
    extensions: &ref_0
      - id: x-parser-unique-object-id
        value: auth
  - &ref_2
    id: AuthReceive
    title: Auth receive
    description: Auth response
    type: send
    messages:
      - &ref_4
        id: Response
        contentType: application/json
        payload:
          - name: Auth Response
            description: Authentication result
            type: object
            properties:
              - name: id
                type: integer
                description: Correlation ID for request-response matching
                required: false
              - name: data
                type: object
                required: true
                properties:
                  - name: status
                    type: string
                    enumValues:
                      - ok
                    required: true
                  - name: pod
                    type: string
                    description: >-
                      Gateway pod identity for log correlation only; pods are
                      not addressable.
                    required: false
                  - name: status
                    type: string
                    enumValues:
                      - err
                    required: true
                  - name: error
                    type: string
                    description: >-
                      Error identifier. For domain rejections and transport
                      errors (`401`/`404`/`429`/`500`) this is a stable,
                      machine-readable snake_case identifier that is part of the
                      API contract and safe to branch on, e.g.
                      `insufficient_margin`, `insufficient_balance`,
                      `order_not_found`, `reduce_only_invalid`,
                      `price_outside_bounds`, `position_not_found`,
                      `position_exists`, `open_orders_exist`,
                      `invalid_margin_mode`, `invalid_margin_amount`,
                      `margin_below_required_initial`, `account_liquidating`,
                      `instrument_close_only`, `instrument_settled`,
                      `settlement_price_unavailable`,
                      `settlement_insurance_insufficient`,
                      `settlement_invalid_state`, `unauthorized`, `not_found`.
                      `instrument_close_only` means user orders must reduce an
                      existing position; `instrument_settled` is permanent.
                      Settlement readiness errors leave the instrument and
                      accounts unchanged. For `400` it is a human-readable
                      validation detail whose wording may change. See the Error
                      handling guide for the domain identifiers. (Post-only /
                      Fill-or-Kill outcomes are order statuses such as
                      `post_only_rejected`, not rejections.)
                    required: true
        headers: []
        jsonPayloadSchema:
          type: object
          title: Base Response
          properties:
            id:
              type: integer
              description: Correlation ID for request-response matching
              x-parser-schema-id: <anonymous-schema-226>
            data:
              oneOf:
                - type: object
                  description: >-
                    Successful auth acknowledgement; pod is optional for
                    compatibility during rolling deploys.
                  required:
                    - status
                  properties:
                    status:
                      type: string
                      enum:
                        - ok
                      x-parser-schema-id: <anonymous-schema-229>
                    pod:
                      type: string
                      description: >-
                        Gateway pod identity for log correlation only; pods are
                        not addressable.
                      example: gateway-ws-7b68c9d4f5-m2n8p
                      x-parser-schema-id: <anonymous-schema-230>
                  x-parser-schema-id: <anonymous-schema-228>
                - type: object
                  required:
                    - status
                    - error
                  properties:
                    status:
                      type: string
                      enum:
                        - err
                      x-parser-schema-id: <anonymous-schema-232>
                    error:
                      type: string
                      description: >-
                        Error identifier. For domain rejections and transport
                        errors (`401`/`404`/`429`/`500`) this is a stable,
                        machine-readable snake_case identifier that is part of
                        the API contract and safe to branch on, e.g.
                        `insufficient_margin`, `insufficient_balance`,
                        `order_not_found`, `reduce_only_invalid`,
                        `price_outside_bounds`, `position_not_found`,
                        `position_exists`, `open_orders_exist`,
                        `invalid_margin_mode`, `invalid_margin_amount`,
                        `margin_below_required_initial`, `account_liquidating`,
                        `instrument_close_only`, `instrument_settled`,
                        `settlement_price_unavailable`,
                        `settlement_insurance_insufficient`,
                        `settlement_invalid_state`, `unauthorized`, `not_found`.
                        `instrument_close_only` means user orders must reduce an
                        existing position; `instrument_settled` is permanent.
                        Settlement readiness errors leave the instrument and
                        accounts unchanged. For `400` it is a human-readable
                        validation detail whose wording may change. See the
                        Error handling guide for the domain identifiers.
                        (Post-only / Fill-or-Kill outcomes are order statuses
                        such as `post_only_rejected`, not rejections.)
                      example: insufficient_margin
                      x-parser-schema-id: <anonymous-schema-233>
                  x-parser-schema-id: <anonymous-schema-231>
              x-parser-schema-id: <anonymous-schema-227>
          required:
            - data
          x-parser-schema-id: <anonymous-schema-225>
        title: Auth Response
        description: Authentication result
        example: |-
          {
            "id": 123,
            "data": {
              "status": "<string>",
              "pod": "<string>",
              "error": "<string>"
            }
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: Response
    bindings: []
    extensions: *ref_0
sendOperations:
  - *ref_1
receiveOperations:
  - *ref_2
sendMessages:
  - *ref_3
receiveMessages:
  - *ref_4
extensions:
  - id: x-parser-unique-object-id
    value: auth
securitySchemes: []

````

This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
