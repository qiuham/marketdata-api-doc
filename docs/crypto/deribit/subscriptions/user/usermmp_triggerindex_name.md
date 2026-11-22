---
exchange: deribit
source_url: https://docs.deribit.com/subscriptions/user/usermmp_triggerindex_name
api_type: WebSocket
updated_at: 2026-11-22 18:59:22.646911
---

# user.mmp_trigger.(index_name)

> Real-time notifications for Market Maker Protection (MMP) triggers. This subscription provides feedback when MMP protection is activated for a given index, enabling clients to react promptly when protection is triggered.

Upon MMP being triggered for a given index, the client will receive a trigger notification containing:

- **frozen_until**: Unix timestamp in milliseconds indicating until when the MMP is active (orders remain blocked). If `frozen_until: 0`, it means MMP will remain active until manually reset using the `private/reset_mmp` method.
- **index_name**: Index identifier of derivative instrument on the platform. For Block RFQ MMP, this will be "all" when triggered by trade count limit.
- **mmp_group**: Triggered MMP group (optional, appears only for Mass Quote orders trigger)
- **block_rfq**: If true, indicates that the MMP trigger is for Block RFQ. Block RFQ MMP triggers are completely separate from normal order/quote MMP triggers.

This notification allows the client to track MMP state per index and avoid submitting new orders that would be rejected due to ongoing MMP freeze.

**📖 Related Article:** [Market Maker Protection API Configuration](https://docs.deribit.com/articles/market-maker-protection)


## AsyncAPI

````yaml specifications/deribit_asyncapi.json user.mmp_trigger.(index_name)
id: user.mmp_trigger.(index_name)
title: 'user.mmp_trigger.(index_name) '
description: >
  Real-time notifications for Market Maker Protection (MMP) triggers. This
  subscription provides feedback when MMP protection is activated for a given
  index, enabling clients to react promptly when protection is triggered.


  Upon MMP being triggered for a given index, the client will receive a trigger
  notification containing:


  - **frozen_until**: Unix timestamp in milliseconds indicating until when the
  MMP is active (orders remain blocked). If `frozen_until: 0`, it means MMP will
  remain active until manually reset using the `private/reset_mmp` method.

  - **index_name**: Index identifier of derivative instrument on the platform.
  For Block RFQ MMP, this will be "all" when triggered by trade count limit.

  - **mmp_group**: Triggered MMP group (optional, appears only for Mass Quote
  orders trigger)

  - **block_rfq**: If true, indicates that the MMP trigger is for Block RFQ.
  Block RFQ MMP triggers are completely separate from normal order/quote MMP
  triggers.


  This notification allows the client to track MMP state per index and avoid
  submitting new orders that would be rejected due to ongoing MMP freeze.


  **📖 Related Article:** [Market Maker Protection API
  Configuration](https://docs.deribit.com/articles/market-maker-protection)
servers:
  - id: production
    protocol: wss
    host: deribit.com/ws/api/v2
    bindings: []
    variables: []
  - id: testnet
    protocol: wss
    host: test.deribit.com/ws/api/v2
    bindings: []
    variables: []
address: user.mmp_trigger.(index_name)
parameters:
  - id: index_name
    jsonSchema:
      type: string
      description: Index identifier of derivative instrument on the platform
      enum:
        - btc_usd
        - eth_usd
        - btc_usdc
        - eth_usdc
        - ada_usdc
        - algo_usdc
        - avax_usdc
        - bch_usdc
        - bnb_usdc
        - doge_usdc
        - dot_usdc
        - hype_usdc
        - link_usdc
        - ltc_usdc
        - near_usdc
        - paxg_usdc
        - shib_usdc
        - sol_usdc
        - ton_usdc
        - trx_usdc
        - trump_usdc
        - uni_usdc
        - xrp_usdc
        - usde_usdc
        - buidl_usdc
        - btcdvol_usdc
        - ethdvol_usdc
        - btc_usdt
        - eth_usdt
        - all
    description: Index identifier of derivative instrument on the platform
    type: string
    required: true
    deprecated: false
bindings: []
operations:
  - &ref_2
    id: send_subscribe_user_mmp_trigger_index_name
    title: Send subscribe request for user
    description: Client sends subscription request for user updates
    type: send
    messages:
      - &ref_4
        id: subscription_message
        contentType: application/json
        payload:
          - name: Subscription Notification Data
            description: Server sends subscription notification data
            type: object
            properties:
              - name: data
                type: object
                required: true
                properties:
                  - name: frozen_until
                    type: integer
                    description: >-
                      Timestamp (milliseconds since the UNIX epoch) until the
                      user will be frozen - 0 means that the user is frozen
                      until manual reset.
                    required: true
                  - name: index_name
                    type: string
                    description: >-
                      Index identifier of derivative instrument on the platform.
                      For Block RFQ MMP, this will be "all" when triggered by
                      trade count limit.
                    required: false
                  - name: mmp_group
                    type: string
                    description: >-
                      Triggered mmp group, this parameter is optional (appears
                      only for Mass Quote orders trigger)
                    required: false
                  - name: block_rfq
                    type: boolean
                    description: >-
                      If true, indicates that the MMP trigger is for Block RFQ.
                      Block RFQ MMP triggers are completely separate from normal
                      order/quote MMP triggers.
                    required: false
        headers: []
        jsonPayloadSchema:
          type: object
          description: Response containing notification data
          properties:
            data:
              properties:
                frozen_until:
                  description: >-
                    Timestamp (milliseconds since the UNIX epoch) until the user
                    will be frozen - 0 means that the user is frozen until
                    manual reset.
                  type: integer
                  example: 0
                  x-parser-schema-id: <anonymous-schema-477>
                index_name:
                  description: >-
                    Index identifier of derivative instrument on the platform.
                    For Block RFQ MMP, this will be "all" when triggered by
                    trade count limit.
                  type: string
                  example: eth_usdc
                  x-parser-schema-id: <anonymous-schema-478>
                mmp_group:
                  description: >-
                    Triggered mmp group, this parameter is optional (appears
                    only for Mass Quote orders trigger)
                  type: string
                  example: MassQuoteBot7
                  x-parser-schema-id: <anonymous-schema-479>
                block_rfq:
                  description: >-
                    If true, indicates that the MMP trigger is for Block RFQ.
                    Block RFQ MMP triggers are completely separate from normal
                    order/quote MMP triggers.
                  type: boolean
                  x-parser-schema-id: <anonymous-schema-480>
              required:
                - frozen_until
              type: object
              x-parser-schema-id: <anonymous-schema-476>
          required:
            - data
          additionalProperties: false
          x-parser-schema-id: <anonymous-schema-475>
        title: Subscription Notification Data
        description: Server sends subscription notification data
        example: |-
          {
            "data": {
              "frozen_until": 123,
              "index_name": "<string>",
              "mmp_group": "<string>",
              "block_rfq": true
            }
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: subscription_message
    bindings: []
    extensions: &ref_0
      - id: x-parser-unique-object-id
        value: user.mmp_trigger.(index_name)
  - &ref_1
    id: receive_user_mmp_trigger_index_name_updates
    title: Receive user updates
    description: Client receives user update notifications
    type: receive
    messages:
      - &ref_3
        id: subscribe_request
        contentType: application/json
        payload:
          - name: Subscription Request
            description: >-
              Client sends subscription request to subscribe to notification
              channel. Please refer to [Notification
              page](https://docs.deribit.com/articles/notifications) for more
              information.
            type: object
            properties:
              - name: jsonrpc
                type: string
                description: '2.0'
                required: true
              - name: id
                type: integer
                required: true
              - name: method
                type: string
                enumValues:
                  - public/subscribe
                  - private/subscribe
                required: true
              - name: params
                type: object
                required: true
                properties:
                  - name: channels
                    type: array
                    required: true
                    properties:
                      - name: item
                        type: string
                        required: false
        headers: []
        jsonPayloadSchema:
          type: object
          properties:
            jsonrpc:
              type: string
              const: '2.0'
              x-parser-schema-id: <anonymous-schema-469>
            id:
              type: integer
              x-parser-schema-id: <anonymous-schema-470>
            method:
              type: string
              enum:
                - public/subscribe
                - private/subscribe
              x-parser-schema-id: <anonymous-schema-471>
            params:
              type: object
              properties:
                channels:
                  type: array
                  items:
                    type: string
                    x-parser-schema-id: <anonymous-schema-474>
                  x-parser-schema-id: <anonymous-schema-473>
              required:
                - channels
              x-parser-schema-id: <anonymous-schema-472>
          required:
            - jsonrpc
            - id
            - method
            - params
          additionalProperties: false
          x-parser-schema-id: <anonymous-schema-468>
        title: Subscription Request
        description: >-
          Client sends subscription request to subscribe to notification
          channel. Please refer to [Notification
          page](https://docs.deribit.com/articles/notifications) for more
          information.
        example: |-
          {
            "jsonrpc": "2.0",
            "method": "private/subscribe",
            "id": 42,
            "params": {
              "channels": [
                "user.mmp_trigger.btc_usd"
              ]
            }
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: subscribe_request
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
    value: user.mmp_trigger.(index_name)
securitySchemes: []

````

## Related topics

- [Starbase Market Maker Protection (MMP)](https://docs.deribit.com/starbase/mmp.md)
- [Market Maker Protection (MMP) API Configuration](https://docs.deribit.com/articles/market-maker-protection.md)
- [JSON-RPC API Changelog](https://docs.deribit.com/changelogs/jsonrpc.md)
- [Notifications](https://docs.deribit.com/articles/notifications.md)
- [private/get_mmp_status](https://docs.deribit.com/api-reference/trading/private-get_mmp_status.md)