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
source_url: 'https://docs.polymarket.com/cn/api-reference/wss/polybolt'
updated_at: 2026-11-13
---

# 实时数据频道

> PolyBolt WebSocket 消息参考，涵盖加密货币、股票类资产和 TWAP 参考价格。



## AsyncAPI

````yaml https://ws-live-v2.polymarket.com/asyncapi.json ws
id: ws
title: Live Data Channel
description: >-
  Send JSON text frames tagged with op. The server answers every op with an ack
  or an error ack (never a close, except for policy breaches, close 4008, and an
  expired Access Token, close 1008) and pushes envelopes for subscribed
  channels. Limits per connection: 64 active (channel, filter) subscriptions, 20
  subscribe or unsubscribe frames per second (a batch frame counts once), 64 KB
  per frame, 8 auth attempts. The server sends a WebSocket ping every 25
  seconds; two missed pongs close 4002. Close codes: 4001 authentication failed
  on a presented credential, 4002 slow consumer or pong timeout, 4003 server
  draining (reconnect once after a uniform 0 to 10 s delay), 4008 policy
  violation (fix the client; do not reconnect blindly), which also closes a
  socket that neither passed authentication nor registered a subscription within
  the server's unengaged timeout (120 seconds by default, reason text unengaged)
  once that rule is enforced, 1008 authentication expired (a connection
  authenticated with an Access Token whose last accepted token expired, 30
  second leeway included, with no renewal; refresh the token and reconnect).
servers:
  - id: production
    protocol: wss
    host: ws-live-v2.polymarket.com
    bindings: []
    variables: []
address: /ws
parameters: []
bindings: []
operations:
  - &ref_8
    id: subscribe
    title: Subscribe
    description: Add one or more (channel, filter) subscriptions
    type: receive
    messages:
      - &ref_20
        id: subscribe
        payload:
          - oneOf: &ref_0
              - type: object
                required:
                  - op
                  - subscriptions
                properties:
                  op:
                    const: subscribe
                    x-parser-schema-id: <anonymous-schema-2>
                  subscriptions:
                    type: array
                    minItems: 1
                    items: &ref_1
                      type: object
                      required:
                        - channel
                        - filter
                      properties:
                        channel:
                          type: string
                          enum:
                            - price.polymarket
                            - price.crypto
                            - price.equity
                            - price.crypto.twap
                            - price.equity.twap
                            - esports.series
                          x-parser-schema-id: <anonymous-schema-4>
                        filter:
                          oneOf:
                            - type: object
                              required:
                                - asset_id
                              properties:
                                asset_id:
                                  type: string
                                  pattern: ^[0-9]{1,78}$
                                  description: >-
                                    Outcome token id (clobTokenIds entry),
                                    decimal string. Leading zeros are
                                    normalized.
                                  x-parser-schema-id: <anonymous-schema-6>
                              x-parser-schema-id: AssetIdFilter
                            - type: object
                              required:
                                - symbol
                              properties:
                                symbol:
                                  type: string
                                  description: >-
                                    Lowercase symbol. Matching is
                                    case-insensitive.
                                  x-parser-schema-id: <anonymous-schema-7>
                                provider:
                                  type: string
                                  enum:
                                    - chainlink
                                    - pyth
                                    - binance
                                  description: >-
                                    Optional provider pin (spec 08b; binance
                                    added by spec 09). While the server's
                                    provider selector is DISABLED
                                    (PRICE_PROVIDER_SELECTOR_ENABLED=false, the
                                    default), this field is accepted and IGNORED
                                    like any unknown key: the lane's owner is
                                    served and the subscribed ack carries no
                                    provider. While it is ENABLED, the value
                                    must be one of the enum tokens; anything
                                    else (including massive, owner, numbers,
                                    null) is a bad_filter error ack. A pin the
                                    catalog serves gets that provider's stream;
                                    a pin it cannot serve falls back to the
                                    owner's stream, and the subscribed ack names
                                    the provider actually served. binance is
                                    price.crypto-only on the SERVING side: the
                                    token parses on every vendor channel, but
                                    only a price.crypto symbol whose operator
                                    config names binance can serve it -
                                    everywhere else (price.equity included) a
                                    binance pin always falls back to the owner.
                                    Ignored on price.polymarket.
                                  x-parser-schema-id: <anonymous-schema-8>
                              x-parser-schema-id: SymbolFilter
                            - type: object
                              required:
                                - symbol
                                - window_seconds
                              properties:
                                symbol:
                                  type: string
                                  x-parser-schema-id: <anonymous-schema-9>
                                window_seconds:
                                  type: integer
                                  minimum: 1
                                  description: >-
                                    Only 60 carries data today, on
                                    price.crypto.twap and price.equity.twap
                                    alike.
                                  x-parser-schema-id: <anonymous-schema-10>
                                provider:
                                  type: string
                                  enum:
                                    - chainlink
                                    - pyth
                                    - binance
                                  description: >-
                                    Optional provider pin (spec 08b; binance
                                    added by spec 09). While the server's
                                    provider selector is DISABLED
                                    (PRICE_PROVIDER_SELECTOR_ENABLED=false, the
                                    default), this field is accepted and IGNORED
                                    like any unknown key: the lane's owner is
                                    served and the subscribed ack carries no
                                    provider. While it is ENABLED, the value
                                    must be one of the enum tokens; anything
                                    else (including massive, owner, numbers,
                                    null) is a bad_filter error ack. A pin the
                                    catalog serves gets that provider's stream;
                                    a pin it cannot serve falls back to the
                                    owner's stream, and the subscribed ack names
                                    the provider actually served. binance is
                                    price.crypto-only on the SERVING side, and
                                    the TWAP channels are Chainlink-produced, so
                                    a binance pin here always falls back to the
                                    owner. Ignored on price.polymarket.
                                  x-parser-schema-id: <anonymous-schema-11>
                              x-parser-schema-id: TwapFilter
                            - type: object
                              required:
                                - event_id
                              properties:
                                event_id:
                                  type: string
                                  pattern: ^[1-9][0-9]{0,9}$
                                  description: >-
                                    Gamma event id, canonical decimal string. A
                                    number or a non-canonical string is a
                                    bad_filter error ack.
                                  x-parser-schema-id: <anonymous-schema-12>
                                provider:
                                  type: string
                                  enum:
                                    - grid
                                    - pandascore
                                  description: >-
                                    Optional provider pin. While the server's
                                    esports provider selector is DISABLED
                                    (ESPORTS_PROVIDER_SELECTOR_ENABLED=false,
                                    the default), this field is accepted and
                                    IGNORED like any unknown key and the default
                                    rule serves. While it is ENABLED, the value
                                    must be one of the enum tokens; anything
                                    else (including numbers, null) is a
                                    bad_filter error ack, and a pin serves only
                                    that provider's document (no fallback;
                                    snapshot null while it holds none). Default
                                    rule (no pin, or selector disabled): the
                                    title's configured owner (GRID unless
                                    configured otherwise), or the other
                                    provider's document while the owner holds
                                    none for the event. When the served provider
                                    changes, the next frame carries
                                    snapshot:true and the full document of the
                                    new provider; documents of two providers
                                    never interleave without one. The document's
                                    source field names its provider. A
                                    connection holding both an unpinned and a
                                    pinned subscription for one event receives
                                    both streams on this channel; demultiplex by
                                    the payload source field (the
                                    never-interleave rule is per subscription).
                                  x-parser-schema-id: <anonymous-schema-13>
                              x-parser-schema-id: EventIdFilter
                          x-parser-schema-id: <anonymous-schema-5>
                      x-parser-schema-id: SubscriptionItem
                    x-parser-schema-id: <anonymous-schema-3>
                  rid:
                    type: string
                    description: >-
                      Client request id, echoed on every ack this frame
                      produces.
                    x-parser-schema-id: <anonymous-schema-14>
                x-parser-schema-id: <anonymous-schema-1>
              - type: object
                required:
                  - op
                  - channel
                  - filter
                properties:
                  op:
                    const: subscribe
                    x-parser-schema-id: <anonymous-schema-16>
                  channel:
                    type: string
                    x-parser-schema-id: <anonymous-schema-17>
                  filter:
                    type: object
                    x-parser-schema-id: <anonymous-schema-18>
                  rid:
                    type: string
                    x-parser-schema-id: <anonymous-schema-19>
                x-parser-schema-id: <anonymous-schema-15>
            x-parser-schema-id: SubscribeRequest
            name: subscribe
        headers: []
        jsonPayloadSchema:
          oneOf: *ref_0
          x-parser-schema-id: SubscribeRequest
        title: Subscribe
        example: |-
          {
            "op": "subscribe",
            "rid": "s1",
            "subscriptions": [
              {
                "channel": "price.polymarket",
                "filter": {
                  "asset_id": "21742633143463906290569050155826241533067272736897614950488156847949938836455"
                }
              },
              {
                "channel": "price.crypto",
                "filter": {
                  "symbol": "btcusd"
                }
              }
            ]
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: subscribe
    bindings: []
    extensions: &ref_3
      - id: x-parser-unique-object-id
        value: ws
  - &ref_9
    id: unsubscribe
    title: Unsubscribe
    description: Remove subscriptions; same singular and batch shapes as subscribe
    type: receive
    messages:
      - &ref_21
        id: unsubscribe
        payload:
          - oneOf: &ref_2
              - type: object
                required:
                  - op
                  - subscriptions
                properties:
                  op:
                    const: unsubscribe
                    x-parser-schema-id: <anonymous-schema-21>
                  subscriptions:
                    type: array
                    minItems: 1
                    items: *ref_1
                    x-parser-schema-id: <anonymous-schema-22>
                  rid:
                    type: string
                    x-parser-schema-id: <anonymous-schema-23>
                x-parser-schema-id: <anonymous-schema-20>
              - type: object
                required:
                  - op
                  - channel
                  - filter
                properties:
                  op:
                    const: unsubscribe
                    x-parser-schema-id: <anonymous-schema-25>
                  channel:
                    type: string
                    x-parser-schema-id: <anonymous-schema-26>
                  filter:
                    type: object
                    x-parser-schema-id: <anonymous-schema-27>
                  rid:
                    type: string
                    x-parser-schema-id: <anonymous-schema-28>
                x-parser-schema-id: <anonymous-schema-24>
            x-parser-schema-id: UnsubscribeRequest
            name: unsubscribe
        headers: []
        jsonPayloadSchema:
          oneOf: *ref_2
          x-parser-schema-id: UnsubscribeRequest
        title: Unsubscribe
        example: |-
          {
            "op": "unsubscribe",
            "channel": "price.crypto",
            "filter": {
              "symbol": "btcusd"
            }
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: unsubscribe
    bindings: []
    extensions: *ref_3
  - &ref_10
    id: auth
    title: Authenticate
    description: >-
      Unlock the gated channels on this connection with an Access Token, CLOB
      API credentials or a web-app ticket
    type: receive
    messages:
      - &ref_22
        id: auth
        payload:
          - name: auth
            type: object
            properties:
              - name: const
                type: string
                description: auth
                required: false
              - name: auth
                type: object
                description: >-
                  CLOB API credentials or an Identity Provider Access Token,
                  never both in one object. An object that mixes the two, or an
                  incomplete set of CLOB credentials, answers the non-closing
                  bad_op.
                required: false
                properties:
                  - name: apiKey
                    type: string
                    required: true
                  - name: secret
                    type: string
                    required: true
                  - name: passphrase
                    type: string
                    required: true
                  - name: accessToken
                    type: string
                    description: >-
                      An Identity Provider Access Token (third-party clients),
                      or a visitor token (logged-out polymarket.com browsers).
                      Verified locally: RS256 under a key of the identity JWKS,
                      the environment's issuer and audience, not expired. The
                      signed header typ picks the profile: at+jwt is an Access
                      Token; visitor+jwt is a visitor token, which must carry
                      sub visitor:<UUID> and client_id polymarket-web, binds no
                      signer and opens the same channels as a web-app ticket. A
                      refused or expired token answers the non-closing
                      auth_invalid; a pod that holds no identity keys answers
                      auth_unavailable (retry later).
                    required: true
              - name: chainlink_api_key
                type: string
                description: >-
                  Optional Chainlink API key, next to an auth credential (also
                  accepted as chainlinkApiKey; both spellings in one frame
                  answer bad_op). Not a credential: a frame with only the key
                  answers bad_op. Recorded when the auth is accepted with CLOB
                  API credentials or a verified Access Token (never a visitor
                  token), and asked for by Chainlink-served price subscriptions
                  on that connection (price.crypto and price.equity symbols
                  Chainlink serves, both TWAP channels). Without it, such a
                  subscription answers the non-closing chainlink_key_required
                  once the deployment enforces the key; until then it is
                  admitted. A key outside this shape, or of another JSON type,
                  is ignored and the credential is still handled. Send it on the
                  first auth frame: the key cannot be added or changed on an
                  authenticated connection, except on a verified Access Token
                  renewal. The web app ticket lane is never asked.
                required: false
              - name: rid
                type: string
                required: false
              - name: ticket
                type: string
                description: >-
                  The one-time ticket from POST /api/ws-ticket (the Polymarket
                  web app's credential), consumed by the attempt whatever the
                  outcome. Minted from a Cloudflare Turnstile solve; when the
                  widget was rendered with this connection's challenge nonce as
                  cData, the ticket verifies only on this socket, whatever IP
                  either request came from. A stale, consumed or unknown ticket,
                  or one minted for another socket, answers the non-closing
                  auth_expired: mint again.
                required: false
        headers: []
        jsonPayloadSchema:
          type: object
          required:
            - op
          properties:
            op:
              const: auth
              x-parser-schema-id: <anonymous-schema-29>
            auth:
              oneOf:
                - type: object
                  required:
                    - apiKey
                    - secret
                    - passphrase
                  properties:
                    apiKey:
                      type: string
                      x-parser-schema-id: <anonymous-schema-31>
                    secret:
                      type: string
                      x-parser-schema-id: <anonymous-schema-32>
                    passphrase:
                      type: string
                      x-parser-schema-id: <anonymous-schema-33>
                  not:
                    required:
                      - accessToken
                    x-parser-schema-id: <anonymous-schema-34>
                  description: >-
                    The CLOB L2 API credential trio, the same credentials used
                    for the CLOB user WebSocket. Never combined with accessToken
                    in one object: the server answers bad_op.
                  x-parser-schema-id: ClobCredentials
                - type: object
                  required:
                    - accessToken
                  properties:
                    accessToken:
                      type: string
                      maxLength: 4096
                      description: >-
                        An Identity Provider Access Token (third-party clients),
                        or a visitor token (logged-out polymarket.com browsers).
                        Verified locally: RS256 under a key of the identity
                        JWKS, the environment's issuer and audience, not
                        expired. The signed header typ picks the profile: at+jwt
                        is an Access Token; visitor+jwt is a visitor token,
                        which must carry sub visitor:<UUID> and client_id
                        polymarket-web, binds no signer and opens the same
                        channels as a web-app ticket. A refused or expired token
                        answers the non-closing auth_invalid; a pod that holds
                        no identity keys answers auth_unavailable (retry later).
                      x-parser-schema-id: <anonymous-schema-35>
                  not:
                    anyOf:
                      - required:
                          - apiKey
                        x-parser-schema-id: <anonymous-schema-37>
                      - required:
                          - secret
                        x-parser-schema-id: <anonymous-schema-38>
                      - required:
                          - passphrase
                        x-parser-schema-id: <anonymous-schema-39>
                    x-parser-schema-id: <anonymous-schema-36>
                  description: >-
                    An Identity Provider Access Token. Never combined with
                    apiKey, secret or passphrase in one object: the server
                    answers bad_op.
                  x-parser-schema-id: AccessTokenCredential
              description: >-
                CLOB API credentials or an Identity Provider Access Token, never
                both in one object. An object that mixes the two, or an
                incomplete set of CLOB credentials, answers the non-closing
                bad_op.
              x-parser-schema-id: <anonymous-schema-30>
            chainlink_api_key:
              type: string
              minLength: 1
              maxLength: 512
              pattern: ^[!-~]+$
              description: >-
                Optional Chainlink API key, next to an auth credential (also
                accepted as chainlinkApiKey; both spellings in one frame answer
                bad_op). Not a credential: a frame with only the key answers
                bad_op. Recorded when the auth is accepted with CLOB API
                credentials or a verified Access Token (never a visitor token),
                and asked for by Chainlink-served price subscriptions on that
                connection (price.crypto and price.equity symbols Chainlink
                serves, both TWAP channels). Without it, such a subscription
                answers the non-closing chainlink_key_required once the
                deployment enforces the key; until then it is admitted. A key
                outside this shape, or of another JSON type, is ignored and the
                credential is still handled. Send it on the first auth frame:
                the key cannot be added or changed on an authenticated
                connection, except on a verified Access Token renewal. The web
                app ticket lane is never asked.
              x-parser-schema-id: <anonymous-schema-40>
            rid:
              type: string
              x-parser-schema-id: <anonymous-schema-41>
            ticket:
              type: string
              maxLength: 128
              description: >-
                The one-time ticket from POST /api/ws-ticket (the Polymarket web
                app's credential), consumed by the attempt whatever the outcome.
                Minted from a Cloudflare Turnstile solve; when the widget was
                rendered with this connection's challenge nonce as cData, the
                ticket verifies only on this socket, whatever IP either request
                came from. A stale, consumed or unknown ticket, or one minted
                for another socket, answers the non-closing auth_expired: mint
                again.
              x-parser-schema-id: <anonymous-schema-42>
          oneOf:
            - required:
                - auth
              x-parser-schema-id: <anonymous-schema-43>
            - required:
                - ticket
              x-parser-schema-id: <anonymous-schema-44>
          description: >-
            Exactly one credential per frame: auth (CLOB API credentials or an
            Identity Provider Access Token, third-party clients) or ticket (the
            web app). Zero or two answer the non-closing bad_op.
          x-parser-schema-id: AuthRequest
        title: Auth
        example: |-
          {
            "op": "auth",
            "rid": "a1",
            "auth": {
              "apiKey": "00000000-0000-4000-8000-000000000000",
              "secret": "<api secret>",
              "passphrase": "<api passphrase>"
            }
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: auth
    bindings: []
    extensions: *ref_3
  - &ref_11
    id: ping
    title: Ping
    description: Optional application-level liveness probe; answered with pong
    type: receive
    messages:
      - &ref_23
        id: ping
        payload:
          - name: ping
            type: object
            properties:
              - name: const
                type: string
                description: ping
                required: false
              - name: rid
                type: string
                required: false
        headers: []
        jsonPayloadSchema:
          type: object
          required:
            - op
          properties:
            op:
              const: ping
              x-parser-schema-id: <anonymous-schema-45>
            rid:
              type: string
              x-parser-schema-id: <anonymous-schema-46>
          x-parser-schema-id: PingRequest
        title: Ping
        example: |-
          {
            "op": "ping",
            "rid": "p1"
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: ping
    bindings: []
    extensions: *ref_3
  - &ref_13
    id: acknowledgements
    title: Acknowledgements
    description: >-
      challenge (on request), subscribed, unsubscribed, authed, pong and error
      acks; rid is echoed when the request carried one
    type: send
    messages:
      - &ref_25
        id: challenge
        payload:
          - name: challenge
            description: >-
              This connection's challenge nonce, the answer to a challenge
              request; never pushed unasked
            type: object
            properties:
              - name: const
                type: string
                description: challenge
                required: false
              - name: nonce
                type: string
                description: >-
                  This connection's challenge nonce (a UUID). Render the
                  Turnstile widget with it as cData before minting a ticket at
                  POST /api/ws-ticket; the ticket then verifies only on this
                  socket, whatever IP either request came from. Not a secret,
                  never rotated for the life of the connection.
                required: true
              - name: rid
                type: string
                required: false
        headers: []
        jsonPayloadSchema:
          type: object
          required:
            - op
            - nonce
          properties:
            op:
              const: challenge
              x-parser-schema-id: <anonymous-schema-256>
            nonce:
              type: string
              pattern: ^[A-Za-z0-9_-]{1,255}$
              description: >-
                This connection's challenge nonce (a UUID). Render the Turnstile
                widget with it as cData before minting a ticket at POST
                /api/ws-ticket; the ticket then verifies only on this socket,
                whatever IP either request came from. Not a secret, never
                rotated for the life of the connection.
              x-parser-schema-id: <anonymous-schema-257>
            rid:
              type: string
              x-parser-schema-id: <anonymous-schema-258>
          x-parser-schema-id: ChallengeAck
        title: Challenge
        description: >-
          This connection's challenge nonce, the answer to a challenge request;
          never pushed unasked
        example: |-
          {
            "op": "challenge",
            "nonce": "3f2b6c1e-9a4d-4c2b-8e1f-0a1b2c3d4e5f",
            "rid": "c1"
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: challenge
      - &ref_26
        id: subscribed
        payload:
          - name: subscribed
            type: object
            properties:
              - name: op
                type: string
                enumValues:
                  - subscribed
                  - unsubscribed
                required: true
              - name: channel
                type: string
                required: true
              - name: rid
                type: string
                required: false
              - name: provider
                type: string
                description: >-
                  subscribed acks only, and only while the channel's provider
                  selector is enabled. esports.series
                  (ESPORTS_PROVIDER_SELECTOR_ENABLED): grid|pandascore, the pin,
                  or without a pin the provider served at subscribe time (absent
                  while the event has no document; later switches arrive as
                  snapshot:true frames). Vendor channels (spec 08b): the
                  provider actually SERVED - the requested pin when the catalog
                  serves it, else the lane's owner (massive is reachable on the
                  omitted path only). binance (spec 09) can be SERVED only on
                  price.crypto - on every other vendor channel a binance pin's
                  ack names the owner it fell back to. Also present on the
                  idempotent duplicate-subscribe ack. Absent everywhere else,
                  including every ack while the selector is disabled.
                enumValues:
                  - pyth
                  - massive
                  - chainlink
                  - binance
                  - grid
                  - pandascore
                required: false
        headers: []
        jsonPayloadSchema: &ref_4
          type: object
          required:
            - op
            - channel
          properties:
            op:
              type: string
              enum:
                - subscribed
                - unsubscribed
              x-parser-schema-id: <anonymous-schema-47>
            channel:
              type: string
              x-parser-schema-id: <anonymous-schema-48>
            rid:
              type: string
              x-parser-schema-id: <anonymous-schema-49>
            provider:
              type: string
              enum:
                - pyth
                - massive
                - chainlink
                - binance
                - grid
                - pandascore
              description: >-
                subscribed acks only, and only while the channel's provider
                selector is enabled. esports.series
                (ESPORTS_PROVIDER_SELECTOR_ENABLED): grid|pandascore, the pin,
                or without a pin the provider served at subscribe time (absent
                while the event has no document; later switches arrive as
                snapshot:true frames). Vendor channels (spec 08b): the provider
                actually SERVED - the requested pin when the catalog serves it,
                else the lane's owner (massive is reachable on the omitted path
                only). binance (spec 09) can be SERVED only on price.crypto - on
                every other vendor channel a binance pin's ack names the owner
                it fell back to. Also present on the idempotent
                duplicate-subscribe ack. Absent everywhere else, including every
                ack while the selector is disabled.
              x-parser-schema-id: <anonymous-schema-50>
          x-parser-schema-id: ChannelAck
        title: Subscribed
        example: |-
          {
            "op": "subscribed",
            "channel": "price.crypto",
            "rid": "s1"
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: subscribed
      - &ref_27
        id: unsubscribed
        payload:
          - name: unsubscribed
            type: object
            properties:
              - name: op
                type: string
                enumValues:
                  - subscribed
                  - unsubscribed
                required: true
              - name: channel
                type: string
                required: true
              - name: rid
                type: string
                required: false
              - name: provider
                type: string
                description: >-
                  subscribed acks only, and only while the channel's provider
                  selector is enabled. esports.series
                  (ESPORTS_PROVIDER_SELECTOR_ENABLED): grid|pandascore, the pin,
                  or without a pin the provider served at subscribe time (absent
                  while the event has no document; later switches arrive as
                  snapshot:true frames). Vendor channels (spec 08b): the
                  provider actually SERVED - the requested pin when the catalog
                  serves it, else the lane's owner (massive is reachable on the
                  omitted path only). binance (spec 09) can be SERVED only on
                  price.crypto - on every other vendor channel a binance pin's
                  ack names the owner it fell back to. Also present on the
                  idempotent duplicate-subscribe ack. Absent everywhere else,
                  including every ack while the selector is disabled.
                enumValues:
                  - pyth
                  - massive
                  - chainlink
                  - binance
                  - grid
                  - pandascore
                required: false
        headers: []
        jsonPayloadSchema: *ref_4
        title: Unsubscribed
        example: |-
          {
            "op": "unsubscribed",
            "channel": "price.crypto"
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: unsubscribed
      - &ref_28
        id: authed
        payload:
          - name: authed
            type: object
            properties:
              - name: op
                type: string
                enumValues:
                  - authed
                  - pong
                required: true
              - name: rid
                type: string
                required: false
        headers: []
        jsonPayloadSchema: &ref_5
          type: object
          required:
            - op
          properties:
            op:
              type: string
              enum:
                - authed
                - pong
              x-parser-schema-id: <anonymous-schema-51>
            rid:
              type: string
              x-parser-schema-id: <anonymous-schema-52>
          x-parser-schema-id: SimpleAck
        title: Authed
        example: |-
          {
            "op": "authed",
            "rid": "a1"
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: authed
      - &ref_29
        id: pong
        payload:
          - name: pong
            type: object
            properties:
              - name: op
                type: string
                enumValues:
                  - authed
                  - pong
                required: true
              - name: rid
                type: string
                required: false
        headers: []
        jsonPayloadSchema: *ref_5
        title: Pong
        example: |-
          {
            "op": "pong",
            "rid": "p1"
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: pong
      - &ref_30
        id: error
        payload:
          - name: error
            type: object
            properties:
              - name: const
                type: string
                description: error
                required: false
              - name: code
                type: string
                description: >-
                  bad_op malformed frame; bad_channel unknown channel;
                  bad_filter missing or invalid filter; sub_limit 65th
                  subscription (followed by close 4008); rate_limited more than
                  20 subscribe/unsubscribe frames per second (followed by close
                  4008); auth_required gated channel before auth; auth_expired
                  consumed or unknown ticket (web app lane); auth_unavailable
                  verifier unreachable, retry later; auth_invalid credentials
                  refused; auth_attempts ninth auth frame (followed by close
                  4008); chainlink_key_required Chainlink-served price
                  subscription on a connection authenticated with CLOB API
                  credentials or a verified Access Token whose auth carried no
                  chainlink_api_key (only where the deployment enforces the key;
                  the connection stays open).
                enumValues:
                  - bad_op
                  - bad_channel
                  - bad_filter
                  - sub_limit
                  - rate_limited
                  - auth_required
                  - auth_expired
                  - auth_unavailable
                  - auth_invalid
                  - auth_attempts
                  - chainlink_key_required
                required: true
              - name: channel
                type: string
                required: false
              - name: rid
                type: string
                required: false
        headers: []
        jsonPayloadSchema:
          type: object
          required:
            - op
            - code
          properties:
            op:
              const: error
              x-parser-schema-id: <anonymous-schema-53>
            code:
              type: string
              enum:
                - bad_op
                - bad_channel
                - bad_filter
                - sub_limit
                - rate_limited
                - auth_required
                - auth_expired
                - auth_unavailable
                - auth_invalid
                - auth_attempts
                - chainlink_key_required
              description: >-
                bad_op malformed frame; bad_channel unknown channel; bad_filter
                missing or invalid filter; sub_limit 65th subscription (followed
                by close 4008); rate_limited more than 20 subscribe/unsubscribe
                frames per second (followed by close 4008); auth_required gated
                channel before auth; auth_expired consumed or unknown ticket
                (web app lane); auth_unavailable verifier unreachable, retry
                later; auth_invalid credentials refused; auth_attempts ninth
                auth frame (followed by close 4008); chainlink_key_required
                Chainlink-served price subscription on a connection
                authenticated with CLOB API credentials or a verified Access
                Token whose auth carried no chainlink_api_key (only where the
                deployment enforces the key; the connection stays open).
              x-parser-schema-id: <anonymous-schema-54>
            channel:
              type: string
              x-parser-schema-id: <anonymous-schema-55>
            rid:
              type: string
              x-parser-schema-id: <anonymous-schema-56>
          x-parser-schema-id: ErrorAck
        title: Error
        example: |-
          {
            "op": "error",
            "code": "auth_required",
            "channel": "price.crypto",
            "rid": "s1"
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: error
    bindings: []
    extensions: *ref_3
  - &ref_14
    id: pricePolymarket
    title: price.polymarket
    description: Best bid and ask per outcome token (public, no auth)
    type: send
    messages:
      - &ref_31
        id: pricePolymarket
        payload:
          - name: price.polymarket envelope
            type: object
            properties:
              - name: v
                type: integer
                description: Envelope version.
                required: true
              - name: channel
                type: string
                description: price.polymarket
                required: true
              - name: seq
                type: integer
                description: >-
                  Dense per-connection, per-channel sequence, assigned at
                  delivery. Resets on every reconnect. Snapshot frames consume a
                  seq.
                required: true
              - name: ts
                type: integer
                description: Producer event time, Unix milliseconds.
                required: true
              - name: snapshot
                type: boolean
                description: >-
                  Present and true on the one snapshot frame sent after each new
                  subscription. Absent on live frames.
                required: false
              - name: dropped
                type: integer
                description: >-
                  Number of frames dropped on this channel since the last
                  delivered frame (slow-consumer signal). Absent when zero.
                required: false
              - name: payload
                type: oneOf
                required: true
                properties:
                  - name: market
                    type: string
                    description: Condition id, 0x-prefixed.
                    required: true
                  - name: asset_id
                    type: string
                    description: Outcome token id, decimal string.
                    required: true
                  - name: best_bid
                    type: string
                    description: Decimal string price.
                    required: true
                  - name: best_ask
                    type: string
                    description: Decimal string price.
                    required: true
                  - name: hash
                    type: string
                    description: Order book hash at this change.
                    required: true
                  - name: timestamp
                    type: integer
                    description: Order book time, Unix milliseconds.
                    required: true
        headers: []
        jsonPayloadSchema:
          type: object
          required:
            - v
            - channel
            - seq
            - ts
            - payload
          properties:
            v:
              type: integer
              const: 1
              description: Envelope version.
              x-parser-schema-id: <anonymous-schema-57>
            channel:
              type: string
              const: price.polymarket
              x-parser-schema-id: <anonymous-schema-58>
            seq:
              type: integer
              description: >-
                Dense per-connection, per-channel sequence, assigned at
                delivery. Resets on every reconnect. Snapshot frames consume a
                seq.
              x-parser-schema-id: <anonymous-schema-59>
            ts:
              type: integer
              description: Producer event time, Unix milliseconds.
              x-parser-schema-id: <anonymous-schema-60>
            snapshot:
              type: boolean
              description: >-
                Present and true on the one snapshot frame sent after each new
                subscription. Absent on live frames.
              x-parser-schema-id: <anonymous-schema-61>
            dropped:
              type: integer
              description: >-
                Number of frames dropped on this channel since the last
                delivered frame (slow-consumer signal). Absent when zero.
              x-parser-schema-id: <anonymous-schema-62>
            payload:
              oneOf:
                - type: object
                  required:
                    - market
                    - asset_id
                    - best_bid
                    - best_ask
                    - hash
                    - timestamp
                  properties:
                    market:
                      type: string
                      description: Condition id, 0x-prefixed.
                      x-parser-schema-id: <anonymous-schema-63>
                    asset_id:
                      type: string
                      description: Outcome token id, decimal string.
                      x-parser-schema-id: <anonymous-schema-64>
                    best_bid:
                      type: string
                      description: Decimal string price.
                      x-parser-schema-id: <anonymous-schema-65>
                    best_ask:
                      type: string
                      description: Decimal string price.
                      x-parser-schema-id: <anonymous-schema-66>
                    hash:
                      type: string
                      description: Order book hash at this change.
                      x-parser-schema-id: <anonymous-schema-67>
                    timestamp:
                      type: integer
                      description: Order book time, Unix milliseconds.
                      x-parser-schema-id: <anonymous-schema-68>
                  x-parser-schema-id: BestBidAsk
                - type: array
                  maxItems: 0
                  description: Empty snapshot for a cold token.
                  x-parser-schema-id: <anonymous-schema-69>
              x-parser-schema-id: PricePolymarketPayload
          description: >-
            Snapshot payload is a BestBidAsk object or an empty array; live
            payload is a BestBidAsk object.
          x-parser-schema-id: PricePolymarketEnvelope
        title: price.polymarket envelope
        example: |-
          {
            "v": 1,
            "channel": "price.polymarket",
            "seq": 1,
            "ts": 1788973000123,
            "snapshot": true,
            "payload": {
              "market": "0x9deb0baac40648821f96f01339229a422e2f5c877de55dc4dbf981f95a1e709c",
              "asset_id": "21742633143463906290569050155826241533067272736897614950488156847949938836455",
              "best_bid": "0.51",
              "best_ask": "0.53",
              "hash": "3f9c1e7a",
              "timestamp": 1788972999871
            }
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: pricePolymarket
    bindings: []
    extensions: *ref_3
  - &ref_15
    id: priceCrypto
    title: price.crypto
    description: Crypto reference prices, about one update per second per symbol (gated)
    type: send
    messages:
      - &ref_32
        id: priceCrypto
        payload:
          - name: price.crypto envelope
            type: object
            properties:
              - name: v
                type: integer
                description: Envelope version.
                required: true
              - name: channel
                type: string
                description: price.crypto
                required: true
              - name: seq
                type: integer
                description: >-
                  Dense per-connection, per-channel sequence, assigned at
                  delivery. Resets on every reconnect. Snapshot frames consume a
                  seq.
                required: true
              - name: ts
                type: integer
                description: Producer event time, Unix milliseconds.
                required: true
              - name: snapshot
                type: boolean
                description: >-
                  Present and true on the one snapshot frame sent after each new
                  subscription. Absent on live frames.
                required: false
              - name: dropped
                type: integer
                description: >-
                  Number of frames dropped on this channel since the last
                  delivered frame (slow-consumer signal). Absent when zero.
                required: false
              - name: payload
                type: object
                required: true
                properties:
                  - name: symbol
                    type: string
                    description: Lowercase symbol, for example btcusd.
                    required: true
                  - name: value
                    type: number
                    description: Price as a float. Prefer full_accuracy_value.
                    required: true
                  - name: full_accuracy_value
                    type: string
                    description: Exact decimal price as published by the source.
                    required: true
                  - name: timestamp
                    type: integer
                    description: Source event time, Unix milliseconds.
                    required: true
                  - name: source
                    type: string
                    description: >-
                      Vendor that produced this price, on every point this
                      server emits. A per-symbol ownership flip rolls the edge
                      fleet, so mid-roll a symbol's consecutive frames can
                      legitimately carry different sources until the roll
                      completes. A binance value (spec 09) is the Binance
                      USDT-quoted close relayed verbatim under the usd-named
                      symbol (no conversion leg): bps-scale delta against
                      pyth/chainlink normally, percent-scale in a USDT depeg -
                      exactly when comparisons are most likely.
                    enumValues:
                      - pyth
                      - chainlink
                      - binance
                    required: true
                  - name: symbol
                    type: string
                    required: true
                  - name: source
                    type: string
                    description: >-
                      Vendor that produced every point in this batch, once at
                      batch level (points are source-free): symbol ownership is
                      fixed for the life of a pod, so one series never mixes
                      vendors. After a reconnect during an ownership flip, the
                      batch can carry a different source than the previous
                      connection's frames. A binance batch (spec 09) is the
                      Binance USDT-quoted close relayed verbatim under the
                      usd-named symbol: bps-scale delta against pyth/chainlink
                      normally, percent-scale in a USDT depeg.
                    enumValues:
                      - pyth
                      - chainlink
                      - binance
                    required: true
                  - name: data
                    type: array
                    description: >-
                      The array holds the previous two minutes of points by
                      event time and is empty for a symbol with no recent data.
                    required: true
                    properties:
                      - name: value
                        type: number
                        description: Price as a float. Prefer full_accuracy_value.
                        required: true
                      - name: full_accuracy_value
                        type: string
                        description: Exact decimal price as published by the source.
                        required: true
                      - name: timestamp
                        type: integer
                        description: Source event time, Unix milliseconds.
                        required: true
        headers: []
        jsonPayloadSchema:
          type: object
          required:
            - v
            - channel
            - seq
            - ts
            - payload
          properties:
            v:
              type: integer
              const: 1
              description: Envelope version.
              x-parser-schema-id: <anonymous-schema-70>
            channel:
              type: string
              const: price.crypto
              x-parser-schema-id: <anonymous-schema-71>
            seq:
              type: integer
              description: >-
                Dense per-connection, per-channel sequence, assigned at
                delivery. Resets on every reconnect. Snapshot frames consume a
                seq.
              x-parser-schema-id: <anonymous-schema-72>
            ts:
              type: integer
              description: Producer event time, Unix milliseconds.
              x-parser-schema-id: <anonymous-schema-73>
            snapshot:
              type: boolean
              description: >-
                Present and true on the one snapshot frame sent after each new
                subscription. Absent on live frames.
              x-parser-schema-id: <anonymous-schema-74>
            dropped:
              type: integer
              description: >-
                Number of frames dropped on this channel since the last
                delivered frame (slow-consumer signal). Absent when zero.
              x-parser-schema-id: <anonymous-schema-75>
            payload:
              oneOf:
                - type: object
                  required:
                    - symbol
                    - value
                    - full_accuracy_value
                    - timestamp
                    - source
                  properties:
                    symbol:
                      type: string
                      description: Lowercase symbol, for example btcusd.
                      x-parser-schema-id: <anonymous-schema-76>
                    value:
                      type: number
                      description: Price as a float. Prefer full_accuracy_value.
                      x-parser-schema-id: <anonymous-schema-77>
                    full_accuracy_value:
                      type: string
                      description: Exact decimal price as published by the source.
                      x-parser-schema-id: <anonymous-schema-78>
                    timestamp:
                      type: integer
                      description: Source event time, Unix milliseconds.
                      x-parser-schema-id: <anonymous-schema-79>
                    source:
                      type: string
                      enum:
                        - pyth
                        - chainlink
                        - binance
                      description: >-
                        Vendor that produced this price, on every point this
                        server emits. A per-symbol ownership flip rolls the edge
                        fleet, so mid-roll a symbol's consecutive frames can
                        legitimately carry different sources until the roll
                        completes. A binance value (spec 09) is the Binance
                        USDT-quoted close relayed verbatim under the usd-named
                        symbol (no conversion leg): bps-scale delta against
                        pyth/chainlink normally, percent-scale in a USDT depeg -
                        exactly when comparisons are most likely.
                      x-parser-schema-id: <anonymous-schema-80>
                  x-parser-schema-id: CryptoPoint
                - type: object
                  required:
                    - symbol
                    - source
                    - data
                  properties:
                    symbol:
                      type: string
                      x-parser-schema-id: <anonymous-schema-82>
                    source:
                      type: string
                      enum:
                        - pyth
                        - chainlink
                        - binance
                      description: >-
                        Vendor that produced every point in this batch, once at
                        batch level (points are source-free): symbol ownership
                        is fixed for the life of a pod, so one series never
                        mixes vendors. After a reconnect during an ownership
                        flip, the batch can carry a different source than the
                        previous connection's frames. A binance batch (spec 09)
                        is the Binance USDT-quoted close relayed verbatim under
                        the usd-named symbol: bps-scale delta against
                        pyth/chainlink normally, percent-scale in a USDT depeg.
                      x-parser-schema-id: <anonymous-schema-83>
                    data:
                      type: array
                      items: &ref_6
                        type: object
                        required:
                          - value
                          - full_accuracy_value
                          - timestamp
                        properties:
                          value:
                            type: number
                            description: Price as a float. Prefer full_accuracy_value.
                            x-parser-schema-id: <anonymous-schema-85>
                          full_accuracy_value:
                            type: string
                            description: Exact decimal price as published by the source.
                            x-parser-schema-id: <anonymous-schema-86>
                          timestamp:
                            type: integer
                            description: Source event time, Unix milliseconds.
                            x-parser-schema-id: <anonymous-schema-87>
                        description: >-
                          One historical point of a snapshot batch. Batch points
                          carry NO symbol and NO source: both live once at batch
                          level (the batch object's own fields), matching what
                          the server actually emits - the retired shared point
                          schema wrongly REQUIRED a symbol on every point.
                        x-parser-schema-id: BatchPoint
                      description: >-
                        The array holds the previous two minutes of points by
                        event time and is empty for a symbol with no recent
                        data.
                      x-parser-schema-id: <anonymous-schema-84>
                  x-parser-schema-id: <anonymous-schema-81>
              x-parser-schema-id: PriceCryptoPayload
          description: Snapshot payload is a symbol batch; live payload is a single point.
          x-parser-schema-id: PriceCryptoEnvelope
        title: price.crypto envelope
        example: |-
          {
            "v": 1,
            "channel": "price.crypto",
            "seq": 1,
            "ts": 1788973000000,
            "snapshot": true,
            "payload": {
              "symbol": "btcusd",
              "source": "pyth",
              "data": [
                {
                  "timestamp": 1788972880000,
                  "value": 64123.5,
                  "full_accuracy_value": "64123.50000000"
                },
                {
                  "timestamp": 1788972881000,
                  "value": 64125.1,
                  "full_accuracy_value": "64125.10000000"
                }
              ]
            }
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: priceCrypto
    bindings: []
    extensions: *ref_3
  - &ref_16
    id: priceEquity
    title: price.equity
    description: Pyth equity, ETF, forex, metals and commodity reference prices (gated)
    type: send
    messages:
      - &ref_33
        id: priceEquity
        payload:
          - name: price.equity envelope
            type: object
            properties:
              - name: v
                type: integer
                description: Envelope version.
                required: true
              - name: channel
                type: string
                description: price.equity
                required: true
              - name: seq
                type: integer
                description: >-
                  Dense per-connection, per-channel sequence, assigned at
                  delivery. Resets on every reconnect. Snapshot frames consume a
                  seq.
                required: true
              - name: ts
                type: integer
                description: Producer event time, Unix milliseconds.
                required: true
              - name: snapshot
                type: boolean
                description: >-
                  Present and true on the one snapshot frame sent after each new
                  subscription. Absent on live frames.
                required: false
              - name: dropped
                type: integer
                description: >-
                  Number of frames dropped on this channel since the last
                  delivered frame (slow-consumer signal). Absent when zero.
                required: false
              - name: payload
                type: object
                required: true
                properties:
                  - name: symbol
                    type: string
                    description: Lowercase symbol, for example btcusd or aapl.
                    required: true
                  - name: value
                    type: number
                    description: Price as a float. Prefer full_accuracy_value.
                    required: true
                  - name: full_accuracy_value
                    type: string
                    description: Exact decimal price as published by the source.
                    required: true
                  - name: timestamp
                    type: integer
                    description: Source event time, Unix milliseconds.
                    required: true
                  - name: source
                    type: string
                    description: >-
                      Vendor that produced this price, on every point this
                      server emits. A per-symbol ownership flip rolls the edge
                      fleet, so mid-roll a symbol's consecutive frames can
                      legitimately carry different sources until the roll
                      completes.
                    enumValues:
                      - pyth
                      - massive
                      - chainlink
                    required: true
                  - name: received_at
                    type: integer
                    description: Ingest receive time, Unix milliseconds. Live frames only.
                    required: false
                  - name: is_carried_forward
                    type: boolean
                    description: >-
                      True when the frame repeats an already-measured price
                      instead of carrying a new one: the upstream redelivered
                      its last measurement (for example a closed session), or
                      the frame is a status change repeating the last price.
                      Live frames only.
                    required: false
                  - name: market_status
                    type: string
                    description: >-
                      State of the market of the instrument this series prices,
                      as its producer states it: open, closed, or unknown (the
                      vendor reported it cannot determine it). Absent means not
                      stated, never open. It describes each provider's own
                      instrument: a continuous-hours product (the Chainlink 24/7
                      streams) reads open outside exchange sessions while an
                      exchange-session feed of the same ticker reads closed, and
                      both are truthful. Every frame renders the series' current
                      status. A status change that repeats the last price
                      arrives as a frame carrying that price (its timestamp
                      unchanged), is_carried_forward true and the new
                      market_status: it is not a duplicate, so never dedup on
                      timestamp alone.
                    enumValues:
                      - open
                      - closed
                      - unknown
                    required: false
                  - name: symbol
                    type: string
                    required: true
                  - name: source
                    type: string
                    description: >-
                      Vendor that produced every point in this batch, once at
                      batch level: symbol ownership is fixed for the life of a
                      pod, so one series never mixes vendors. After a reconnect
                      during an ownership flip, the batch can carry a different
                      source than the previous connection's frames.
                    enumValues:
                      - pyth
                      - massive
                      - chainlink
                    required: true
                  - name: market_status
                    type: string
                    description: >-
                      The series' current market status, once at batch level
                      like source; absent when not stated. While it is closed or
                      unknown, data also carries the series' last price point
                      when that point is older than the two-minute window (the
                      price the market stopped at), and the envelope ts is then
                      that point's time.
                    enumValues:
                      - open
                      - closed
                      - unknown
                    required: false
                  - name: data
                    type: array
                    description: >-
                      The array holds the previous two minutes of points by
                      event time and is empty for a symbol with no recent data,
                      except while market_status is closed or unknown: then it
                      also holds the series' last point when that point is older
                      than the window.
                    required: true
                    properties:
                      - name: value
                        type: number
                        description: Price as a float. Prefer full_accuracy_value.
                        required: true
                      - name: full_accuracy_value
                        type: string
                        description: Exact decimal price as published by the source.
                        required: true
                      - name: timestamp
                        type: integer
                        description: Source event time, Unix milliseconds.
                        required: true
        headers: []
        jsonPayloadSchema:
          type: object
          required:
            - v
            - channel
            - seq
            - ts
            - payload
          properties:
            v:
              type: integer
              const: 1
              description: Envelope version.
              x-parser-schema-id: <anonymous-schema-88>
            channel:
              type: string
              const: price.equity
              x-parser-schema-id: <anonymous-schema-89>
            seq:
              type: integer
              description: >-
                Dense per-connection, per-channel sequence, assigned at
                delivery. Resets on every reconnect. Snapshot frames consume a
                seq.
              x-parser-schema-id: <anonymous-schema-90>
            ts:
              type: integer
              description: Producer event time, Unix milliseconds.
              x-parser-schema-id: <anonymous-schema-91>
            snapshot:
              type: boolean
              description: >-
                Present and true on the one snapshot frame sent after each new
                subscription. Absent on live frames.
              x-parser-schema-id: <anonymous-schema-92>
            dropped:
              type: integer
              description: >-
                Number of frames dropped on this channel since the last
                delivered frame (slow-consumer signal). Absent when zero.
              x-parser-schema-id: <anonymous-schema-93>
            payload:
              oneOf:
                - type: object
                  required:
                    - symbol
                    - value
                    - full_accuracy_value
                    - timestamp
                    - source
                  properties:
                    symbol:
                      type: string
                      description: Lowercase symbol, for example btcusd or aapl.
                      x-parser-schema-id: <anonymous-schema-94>
                    value:
                      type: number
                      description: Price as a float. Prefer full_accuracy_value.
                      x-parser-schema-id: <anonymous-schema-95>
                    full_accuracy_value:
                      type: string
                      description: Exact decimal price as published by the source.
                      x-parser-schema-id: <anonymous-schema-96>
                    timestamp:
                      type: integer
                      description: Source event time, Unix milliseconds.
                      x-parser-schema-id: <anonymous-schema-97>
                    source:
                      type: string
                      enum:
                        - pyth
                        - massive
                        - chainlink
                      description: >-
                        Vendor that produced this price, on every point this
                        server emits. A per-symbol ownership flip rolls the edge
                        fleet, so mid-roll a symbol's consecutive frames can
                        legitimately carry different sources until the roll
                        completes.
                      x-parser-schema-id: <anonymous-schema-98>
                    received_at:
                      type: integer
                      description: >-
                        Ingest receive time, Unix milliseconds. Live frames
                        only.
                      x-parser-schema-id: <anonymous-schema-99>
                    is_carried_forward:
                      type: boolean
                      description: >-
                        True when the frame repeats an already-measured price
                        instead of carrying a new one: the upstream redelivered
                        its last measurement (for example a closed session), or
                        the frame is a status change repeating the last price.
                        Live frames only.
                      x-parser-schema-id: <anonymous-schema-100>
                    market_status:
                      type: string
                      enum:
                        - open
                        - closed
                        - unknown
                      description: >-
                        State of the market of the instrument this series
                        prices, as its producer states it: open, closed, or
                        unknown (the vendor reported it cannot determine it).
                        Absent means not stated, never open. It describes each
                        provider's own instrument: a continuous-hours product
                        (the Chainlink 24/7 streams) reads open outside exchange
                        sessions while an exchange-session feed of the same
                        ticker reads closed, and both are truthful. Every frame
                        renders the series' current status. A status change that
                        repeats the last price arrives as a frame carrying that
                        price (its timestamp unchanged), is_carried_forward true
                        and the new market_status: it is not a duplicate, so
                        never dedup on timestamp alone.
                      x-parser-schema-id: <anonymous-schema-101>
                  x-parser-schema-id: EquityPoint
                - type: object
                  required:
                    - symbol
                    - source
                    - data
                  properties:
                    symbol:
                      type: string
                      x-parser-schema-id: <anonymous-schema-103>
                    source:
                      type: string
                      enum:
                        - pyth
                        - massive
                        - chainlink
                      description: >-
                        Vendor that produced every point in this batch, once at
                        batch level: symbol ownership is fixed for the life of a
                        pod, so one series never mixes vendors. After a
                        reconnect during an ownership flip, the batch can carry
                        a different source than the previous connection's
                        frames.
                      x-parser-schema-id: <anonymous-schema-104>
                    market_status:
                      type: string
                      enum:
                        - open
                        - closed
                        - unknown
                      description: >-
                        The series' current market status, once at batch level
                        like source; absent when not stated. While it is closed
                        or unknown, data also carries the series' last price
                        point when that point is older than the two-minute
                        window (the price the market stopped at), and the
                        envelope ts is then that point's time.
                      x-parser-schema-id: <anonymous-schema-105>
                    data:
                      type: array
                      items: *ref_6
                      description: >-
                        The array holds the previous two minutes of points by
                        event time and is empty for a symbol with no recent
                        data, except while market_status is closed or unknown:
                        then it also holds the series' last point when that
                        point is older than the window.
                      x-parser-schema-id: <anonymous-schema-106>
                  x-parser-schema-id: <anonymous-schema-102>
              x-parser-schema-id: PriceEquityPayload
          description: Snapshot payload is a symbol batch; live payload is a single point.
          x-parser-schema-id: PriceEquityEnvelope
        title: price.equity envelope
        example: |-
          {
            "v": 1,
            "channel": "price.equity",
            "seq": 5,
            "ts": 1788973001200,
            "payload": {
              "symbol": "aapl",
              "value": 189.42,
              "full_accuracy_value": "189.4217",
              "timestamp": 1788973001200,
              "received_at": 1788973001207,
              "is_carried_forward": false,
              "source": "pyth"
            }
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: priceEquity
    bindings: []
    extensions: *ref_3
  - &ref_17
    id: priceCryptoTwap
    title: price.crypto.twap
    description: >-
      Chainlink time-weighted average prices used by crypto up/down market
      resolution (gated)
    type: send
    messages:
      - &ref_34
        id: priceCryptoTwap
        payload:
          - name: price.crypto.twap envelope
            type: object
            properties:
              - name: v
                type: integer
                description: Envelope version.
                required: true
              - name: channel
                type: string
                description: price.crypto.twap
                required: true
              - name: seq
                type: integer
                description: >-
                  Dense per-connection, per-channel sequence, assigned at
                  delivery. Resets on every reconnect. Snapshot frames consume a
                  seq.
                required: true
              - name: ts
                type: integer
                description: Producer event time, Unix milliseconds.
                required: true
              - name: snapshot
                type: boolean
                description: >-
                  Present and true on the one snapshot frame sent after each new
                  subscription. Absent on live frames.
                required: false
              - name: dropped
                type: integer
                description: >-
                  Number of frames dropped on this channel since the last
                  delivered frame (slow-consumer signal). Absent when zero.
                required: false
              - name: payload
                type: object
                required: true
                properties:
                  - name: symbol
                    type: string
                    description: Lowercase symbol, for example btcusd.
                    required: true
                  - name: value
                    type: number
                    description: Price as a float. Prefer full_accuracy_value.
                    required: true
                  - name: full_accuracy_value
                    type: string
                    description: Exact decimal price as published by the source.
                    required: true
                  - name: timestamp
                    type: integer
                    description: Source event time, Unix milliseconds.
                    required: true
                  - name: window_seconds
                    type: integer
                    description: Averaging window of the TWAP series. Only 60 exists today.
                    required: true
                  - name: source
                    type: string
                    description: >-
                      The producing vendor. price.crypto.twap is a
                      single-provider lane, so the value is the topic constant.
                    enumValues:
                      - chainlink
                    required: true
                  - name: symbol
                    type: string
                    required: true
                  - name: data
                    type: array
                    description: >-
                      The array holds the previous two minutes of points by
                      event time and is empty for a symbol with no recent data.
                    required: true
                    properties:
                      - name: value
                        type: number
                        description: Price as a float. Prefer full_accuracy_value.
                        required: true
                      - name: full_accuracy_value
                        type: string
                        description: Exact decimal price as published by the source.
                        required: true
                      - name: timestamp
                        type: integer
                        description: Source event time, Unix milliseconds.
                        required: true
                  - name: window_seconds
                    type: integer
                    description: 60
                    required: true
                  - name: source
                    type: string
                    description: >-
                      The producing vendor, once per batch (points are
                      source-free). Topic constant on this single-provider lane.
                    enumValues:
                      - chainlink
                    required: true
        headers: []
        jsonPayloadSchema:
          type: object
          required:
            - v
            - channel
            - seq
            - ts
            - payload
          properties:
            v:
              type: integer
              const: 1
              description: Envelope version.
              x-parser-schema-id: <anonymous-schema-107>
            channel:
              type: string
              const: price.crypto.twap
              x-parser-schema-id: <anonymous-schema-108>
            seq:
              type: integer
              description: >-
                Dense per-connection, per-channel sequence, assigned at
                delivery. Resets on every reconnect. Snapshot frames consume a
                seq.
              x-parser-schema-id: <anonymous-schema-109>
            ts:
              type: integer
              description: Producer event time, Unix milliseconds.
              x-parser-schema-id: <anonymous-schema-110>
            snapshot:
              type: boolean
              description: >-
                Present and true on the one snapshot frame sent after each new
                subscription. Absent on live frames.
              x-parser-schema-id: <anonymous-schema-111>
            dropped:
              type: integer
              description: >-
                Number of frames dropped on this channel since the last
                delivered frame (slow-consumer signal). Absent when zero.
              x-parser-schema-id: <anonymous-schema-112>
            payload:
              oneOf:
                - type: object
                  required:
                    - symbol
                    - value
                    - full_accuracy_value
                    - timestamp
                    - window_seconds
                    - source
                  properties:
                    symbol:
                      type: string
                      description: Lowercase symbol, for example btcusd.
                      x-parser-schema-id: <anonymous-schema-113>
                    value:
                      type: number
                      description: Price as a float. Prefer full_accuracy_value.
                      x-parser-schema-id: <anonymous-schema-114>
                    full_accuracy_value:
                      type: string
                      description: Exact decimal price as published by the source.
                      x-parser-schema-id: <anonymous-schema-115>
                    timestamp:
                      type: integer
                      description: Source event time, Unix milliseconds.
                      x-parser-schema-id: <anonymous-schema-116>
                    window_seconds:
                      type: integer
                      const: 60
                      description: >-
                        Averaging window of the TWAP series. Only 60 exists
                        today.
                      x-parser-schema-id: <anonymous-schema-117>
                    source:
                      type: string
                      enum:
                        - chainlink
                      description: >-
                        The producing vendor. price.crypto.twap is a
                        single-provider lane, so the value is the topic
                        constant.
                      x-parser-schema-id: <anonymous-schema-118>
                  x-parser-schema-id: TwapPoint
                - type: object
                  required:
                    - symbol
                    - data
                    - window_seconds
                    - source
                  properties:
                    symbol:
                      type: string
                      x-parser-schema-id: <anonymous-schema-120>
                    data:
                      type: array
                      items: *ref_6
                      description: >-
                        The array holds the previous two minutes of points by
                        event time and is empty for a symbol with no recent
                        data.
                      x-parser-schema-id: <anonymous-schema-121>
                    window_seconds:
                      type: integer
                      const: 60
                      x-parser-schema-id: <anonymous-schema-122>
                    source:
                      type: string
                      enum:
                        - chainlink
                      description: >-
                        The producing vendor, once per batch (points are
                        source-free). Topic constant on this single-provider
                        lane.
                      x-parser-schema-id: <anonymous-schema-123>
                  x-parser-schema-id: <anonymous-schema-119>
              x-parser-schema-id: PriceCryptoTwapPayload
          description: >-
            Snapshot payload is a symbol batch carrying window_seconds; live
            payload is a single point carrying window_seconds.
          x-parser-schema-id: PriceCryptoTwapEnvelope
        title: price.crypto.twap envelope
        example: |-
          {
            "v": 1,
            "channel": "price.crypto.twap",
            "seq": 3,
            "ts": 1788973002000,
            "payload": {
              "symbol": "btcusd",
              "value": 64120.7,
              "full_accuracy_value": "64120.70000000",
              "timestamp": 1788973002000,
              "window_seconds": 60,
              "source": "chainlink"
            }
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: priceCryptoTwap
    bindings: []
    extensions: *ref_3
  - &ref_18
    id: priceEquityTwap
    title: price.equity.twap
    description: Chainlink Data Streams FX time-weighted average prices (gated)
    type: send
    messages:
      - &ref_35
        id: priceEquityTwap
        payload:
          - name: price.equity.twap envelope
            type: object
            properties:
              - name: v
                type: integer
                description: Envelope version.
                required: true
              - name: channel
                type: string
                description: price.equity.twap
                required: true
              - name: seq
                type: integer
                description: >-
                  Dense per-connection, per-channel sequence, assigned at
                  delivery. Resets on every reconnect. Snapshot frames consume a
                  seq.
                required: true
              - name: ts
                type: integer
                description: Producer event time, Unix milliseconds.
                required: true
              - name: snapshot
                type: boolean
                description: >-
                  Present and true on the one snapshot frame sent after each new
                  subscription. Absent on live frames.
                required: false
              - name: dropped
                type: integer
                description: >-
                  Number of frames dropped on this channel since the last
                  delivered frame (slow-consumer signal). Absent when zero.
                required: false
              - name: payload
                type: object
                required: true
                properties:
                  - name: symbol
                    type: string
                    description: Lowercase symbol, for example eurusd.
                    required: true
                  - name: value
                    type: number
                    description: Price as a float. Prefer full_accuracy_value.
                    required: true
                  - name: full_accuracy_value
                    type: string
                    description: Exact decimal price as published by the source.
                    required: true
                  - name: timestamp
                    type: integer
                    description: Source event time, Unix milliseconds.
                    required: true
                  - name: window_seconds
                    type: integer
                    description: Averaging window of the TWAP series. Only 60 exists today.
                    required: true
                  - name: source
                    type: string
                    description: >-
                      Vendor that produced this price, on every point this
                      server emits. The channel is Chainlink-only today, so the
                      emitted value is chainlink. Kept as its own schema because
                      this enum is the full vendor set while TwapPoint pins its
                      topic constant.
                    enumValues:
                      - pyth
                      - massive
                      - chainlink
                    required: true
                  - name: market_status
                    type: string
                    description: >-
                      State of the market of the instrument this series prices,
                      as its producer states it; same meaning as on
                      price.equity. Absent means not stated. On this channel it
                      changes only with a new price (a TWAP has one clock). The
                      Chainlink FX TWAPs are continuous-hours products and read
                      open.
                    enumValues:
                      - open
                      - closed
                      - unknown
                    required: false
                  - name: symbol
                    type: string
                    required: true
                  - name: source
                    type: string
                    description: >-
                      Vendor that produced every point in this batch, once at
                      batch level. The channel is Chainlink-only today, so the
                      value is chainlink.
                    enumValues:
                      - pyth
                      - massive
                      - chainlink
                    required: true
                  - name: market_status
                    type: string
                    description: >-
                      The series' current market status, once at batch level
                      like source; absent when not stated. While it is closed or
                      unknown, data also carries the series' last price point
                      when that point is older than the two-minute window (the
                      price the market stopped at), and the envelope ts is then
                      that point's time.
                    enumValues:
                      - open
                      - closed
                      - unknown
                    required: false
                  - name: data
                    type: array
                    description: >-
                      The array holds the previous two minutes of points by
                      event time and is empty for a symbol with no recent data,
                      except while market_status is closed or unknown: then it
                      also holds the series' last point when that point is older
                      than the window.
                    required: true
                    properties:
                      - name: value
                        type: number
                        description: Price as a float. Prefer full_accuracy_value.
                        required: true
                      - name: full_accuracy_value
                        type: string
                        description: Exact decimal price as published by the source.
                        required: true
                      - name: timestamp
                        type: integer
                        description: Source event time, Unix milliseconds.
                        required: true
                  - name: window_seconds
                    type: integer
                    description: 60
                    required: true
        headers: []
        jsonPayloadSchema:
          type: object
          required:
            - v
            - channel
            - seq
            - ts
            - payload
          properties:
            v:
              type: integer
              const: 1
              description: Envelope version.
              x-parser-schema-id: <anonymous-schema-124>
            channel:
              type: string
              const: price.equity.twap
              x-parser-schema-id: <anonymous-schema-125>
            seq:
              type: integer
              description: >-
                Dense per-connection, per-channel sequence, assigned at
                delivery. Resets on every reconnect. Snapshot frames consume a
                seq.
              x-parser-schema-id: <anonymous-schema-126>
            ts:
              type: integer
              description: Producer event time, Unix milliseconds.
              x-parser-schema-id: <anonymous-schema-127>
            snapshot:
              type: boolean
              description: >-
                Present and true on the one snapshot frame sent after each new
                subscription. Absent on live frames.
              x-parser-schema-id: <anonymous-schema-128>
            dropped:
              type: integer
              description: >-
                Number of frames dropped on this channel since the last
                delivered frame (slow-consumer signal). Absent when zero.
              x-parser-schema-id: <anonymous-schema-129>
            payload:
              oneOf:
                - type: object
                  required:
                    - symbol
                    - value
                    - full_accuracy_value
                    - timestamp
                    - window_seconds
                    - source
                  properties:
                    symbol:
                      type: string
                      description: Lowercase symbol, for example eurusd.
                      x-parser-schema-id: <anonymous-schema-130>
                    value:
                      type: number
                      description: Price as a float. Prefer full_accuracy_value.
                      x-parser-schema-id: <anonymous-schema-131>
                    full_accuracy_value:
                      type: string
                      description: Exact decimal price as published by the source.
                      x-parser-schema-id: <anonymous-schema-132>
                    timestamp:
                      type: integer
                      description: Source event time, Unix milliseconds.
                      x-parser-schema-id: <anonymous-schema-133>
                    window_seconds:
                      type: integer
                      const: 60
                      description: >-
                        Averaging window of the TWAP series. Only 60 exists
                        today.
                      x-parser-schema-id: <anonymous-schema-134>
                    source:
                      type: string
                      enum:
                        - pyth
                        - massive
                        - chainlink
                      description: >-
                        Vendor that produced this price, on every point this
                        server emits. The channel is Chainlink-only today, so
                        the emitted value is chainlink. Kept as its own schema
                        because this enum is the full vendor set while TwapPoint
                        pins its topic constant.
                      x-parser-schema-id: <anonymous-schema-135>
                    market_status:
                      type: string
                      enum:
                        - open
                        - closed
                        - unknown
                      description: >-
                        State of the market of the instrument this series
                        prices, as its producer states it; same meaning as on
                        price.equity. Absent means not stated. On this channel
                        it changes only with a new price (a TWAP has one clock).
                        The Chainlink FX TWAPs are continuous-hours products and
                        read open.
                      x-parser-schema-id: <anonymous-schema-136>
                  x-parser-schema-id: EquityTwapPoint
                - type: object
                  required:
                    - symbol
                    - source
                    - data
                    - window_seconds
                  properties:
                    symbol:
                      type: string
                      x-parser-schema-id: <anonymous-schema-138>
                    source:
                      type: string
                      enum:
                        - pyth
                        - massive
                        - chainlink
                      description: >-
                        Vendor that produced every point in this batch, once at
                        batch level. The channel is Chainlink-only today, so the
                        value is chainlink.
                      x-parser-schema-id: <anonymous-schema-139>
                    market_status:
                      type: string
                      enum:
                        - open
                        - closed
                        - unknown
                      description: >-
                        The series' current market status, once at batch level
                        like source; absent when not stated. While it is closed
                        or unknown, data also carries the series' last price
                        point when that point is older than the two-minute
                        window (the price the market stopped at), and the
                        envelope ts is then that point's time.
                      x-parser-schema-id: <anonymous-schema-140>
                    data:
                      type: array
                      items: *ref_6
                      description: >-
                        The array holds the previous two minutes of points by
                        event time and is empty for a symbol with no recent
                        data, except while market_status is closed or unknown:
                        then it also holds the series' last point when that
                        point is older than the window.
                      x-parser-schema-id: <anonymous-schema-141>
                    window_seconds:
                      type: integer
                      const: 60
                      x-parser-schema-id: <anonymous-schema-142>
                  x-parser-schema-id: <anonymous-schema-137>
              x-parser-schema-id: PriceEquityTwapPayload
          description: >-
            Snapshot payload is a symbol batch carrying window_seconds; live
            payload is a single point carrying window_seconds.
          x-parser-schema-id: PriceEquityTwapEnvelope
        title: price.equity.twap envelope
        example: |-
          {
            "v": 1,
            "channel": "price.equity.twap",
            "seq": 3,
            "ts": 1788973002000,
            "payload": {
              "symbol": "eurusd",
              "value": 1.0842,
              "full_accuracy_value": "1.08420000",
              "timestamp": 1788973002000,
              "window_seconds": 60,
              "source": "chainlink"
            }
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: priceEquityTwap
    bindings: []
    extensions: *ref_3
  - &ref_19
    id: esportsSeries
    title: esports.series
    description: >-
      Live esports series state for a Polymarket event: score, games, clock and
      plays (public by default)
    type: send
    messages:
      - &ref_36
        id: esportsSeries
        payload:
          - name: esports.series envelope
            type: object
            properties:
              - name: v
                type: integer
                description: Envelope version.
                required: true
              - name: channel
                type: string
                description: esports.series
                required: true
              - name: seq
                type: integer
                description: >-
                  Dense per-connection, per-channel sequence, assigned at
                  delivery. Resets on every reconnect. Snapshot frames consume a
                  seq.
                required: true
              - name: ts
                type: integer
                description: The document's observed_at_ms; now for a null snapshot.
                required: true
              - name: snapshot
                type: boolean
                description: >-
                  Present and true on the one snapshot frame sent after each new
                  subscription. Absent on live frames.
                required: false
              - name: dropped
                type: integer
                description: >-
                  Number of frames dropped on this channel since the last
                  delivered frame (slow-consumer signal). Absent when zero.
                required: false
              - name: payload
                type: object
                required: true
                properties:
                  - name: event_id
                    type: string
                    description: Gamma event id.
                    required: true
                  - name: title
                    type: string
                    enumValues:
                      - lol
                      - cs2
                      - dota2
                      - valorant
                      - r6siege
                      - mlbb
                    required: true
                  - name: source
                    type: string
                    description: Data provider.
                    enumValues:
                      - grid
                      - pandascore
                    required: true
                  - name: provider_series_id
                    type: string
                    description: Support and tracing only; never key on it.
                    required: true
                  - name: schema_version
                    type: integer
                    required: true
                  - name: binding_revision
                    type: integer
                    description: >-
                      Rises when the event is rebound to another provider
                      series.
                    required: true
                  - name: revision
                    type: integer
                    description: Rises with every published change; never goes back.
                    required: true
                  - name: source_updated_at_ms
                    type: integer
                    description: >-
                      When the provider last changed the state. Absent when not
                      reported.
                    required: false
                  - name: observed_at_ms
                    type: integer
                    description: >-
                      When the producer read this state plus its configurable
                      publish delay: the document is the state as of that delay
                      ago, except feed_status and any live field groups the
                      producer enables (results: phase finished, series
                      games_won/won, game finished/winner_team_id; kills: game
                      team kills/deaths/first_kill), which are current.
                      feed_status live can carry an old observed_at for up to
                      the delay after an outage; judge freshness by observed_at.
                      Freshness is now - observed_at_ms (not applicable once
                      phase is finished); clocks anchor here.
                    required: true
                  - name: published_at_ms
                    type: integer
                    required: false
                  - name: phase
                    type: string
                    enumValues:
                      - upcoming
                      - live
                      - paused
                      - finished
                      - unspecified
                    required: true
                  - name: valid
                    type: boolean
                    description: >-
                      False while the provider reports the state invalid; absent
                      when not reported.
                    required: false
                  - name: invalidation_reason
                    type: string
                    required: true
                  - name: feed_status
                    type: string
                    description: >-
                      live, or delayed/recovering: the document is the last good
                      state.
                    enumValues:
                      - live
                      - delayed
                      - recovering
                      - unspecified
                    required: true
                  - name: capabilities
                    type: array
                    description: >-
                      The optional groups this document fills; an absent field
                      or empty group means unknown, never zero.
                    required: true
                    properties:
                      - name: item
                        type: string
                        enumValues:
                          - series
                          - games
                          - clock
                          - draft
                          - players
                          - objectives
                          - structures
                          - timers
                          - rounds
                          - economy
                          - plays
                        required: false
                  - name: format
                    type: string
                    description: e.g. best-of-3.
                    required: true
                  - name: best_of
                    type: integer
                    required: true
                  - name: current_game
                    type: integer
                    description: >-
                      Game in play, or next between games; the last game once
                      finished; absent until the series starts.
                    required: false
                  - name: legacy_score
                    type: string
                    description: >-
                      Legacy card score string, home first, e.g.
                      21-6,10-11,missing|1-0|Bo3. Empty while either side is
                      unresolved, the doc is invalid, or best-of is unknown.
                    required: true
                  - name: period
                    type: string
                    description: >-
                      Legacy period string: NS until a game starts, then
                      <current_game>/<best_of>, e.g. 2/3. Empty if best-of is
                      unknown. Gate on phase.
                    required: true
                  - name: teams
                    type: array
                    required: true
                    properties:
                      - name: id
                        type: string
                        description: >-
                          Provider team id; games[].teams[].team_id refers to
                          it.
                        required: true
                      - name: name
                        type: string
                        required: true
                      - name: polymarket_side
                        type: string
                        description: Side of the Polymarket event this team is on.
                        enumValues:
                          - home
                          - away
                          - unspecified
                        required: true
                      - name: games_won
                        type: integer
                        description: Games (LoL) or maps (CS2) won.
                        required: true
                      - name: won
                        type: boolean
                        description: Present once the series has a winner.
                        required: false
                  - name: games
                    type: array
                    required: true
                    properties:
                      - name: number
                        type: integer
                        description: Game number in the series.
                        required: true
                      - name: map
                        type: string
                        description: >-
                          Map name; for single-map titles the provider's (LoL:
                          Summoner's Rift) or empty.
                        required: true
                      - name: started
                        type: boolean
                        required: true
                      - name: finished
                        type: boolean
                        required: true
                      - name: paused
                        type: boolean
                        required: true
                      - name: winner_team_id
                        type: string
                        description: >-
                          The provider's explicit winner; empty until there is
                          one.
                        required: true
                      - name: clock
                        type: object
                        required: false
                        properties:
                          - name: seconds
                            type: integer
                            description: >-
                              Seconds on the clock at observed_at_ms. Advance
                              from observed_at_ms only while ticking and the
                              document is fresh.
                            required: true
                          - name: ticking
                            type: boolean
                            required: true
                          - name: counts_down
                            type: boolean
                            description: >-
                              True for a countdown (CS2 round, respawn); false
                              for elapsed game time.
                            required: true
                      - name: teams
                        type: array
                        required: true
                        properties:
                          - name: team_id
                            type: string
                            required: true
                          - name: side
                            type: string
                            description: >-
                              blue/red (LoL), terrorists/counter-terrorists
                              (CS2), ...
                            required: true
                          - name: kills
                            type: integer
                            description: Kills; the per-game score in LoL.
                            required: false
                          - name: deaths
                            type: integer
                            required: false
                          - name: gold
                            type: integer
                            description: Total gold earned (LoL).
                            required: false
                          - name: gold_lead
                            type: integer
                            description: This team's gold minus the opponent's.
                            required: false
                          - name: objectives
                            type: array
                            required: true
                            properties:
                              - name: kind
                                type: string
                                description: >-
                                  lower_snake: tower, inhibitor, dragon, baron,
                                  herald, void_grub, ...
                                required: true
                              - name: variant
                                type: string
                                description: >-
                                  Dragon element where it matters; empty
                                  otherwise.
                                required: true
                              - name: count
                                type: integer
                                required: true
                              - name: first
                                type: boolean
                                description: >-
                                  True when this team took the kind first in the
                                  game.
                                required: false
                          - name: baron_power_play
                            type: integer
                            required: false
                          - name: rounds_won
                            type: integer
                            description: Rounds won; the per-map score in CS2.
                            required: false
                          - name: money
                            type: integer
                            required: false
                          - name: players
                            type: array
                            required: true
                            properties:
                              - name: id
                                type: string
                                required: true
                              - name: name
                                type: string
                                required: true
                              - name: character
                                type: string
                                description: >-
                                  Champion, hero or agent; absent before it is
                                  picked.
                                required: false
                              - name: kills
                                type: integer
                                required: false
                              - name: deaths
                                type: integer
                                required: false
                              - name: assists
                                type: integer
                                required: false
                              - name: alive
                                type: boolean
                                required: false
                              - name: gold
                                type: integer
                                description: Total gold earned (LoL).
                                required: false
                              - name: respawn
                                type: object
                                required: false
                                properties:
                                  - name: seconds
                                    type: integer
                                    description: >-
                                      Seconds on the clock at observed_at_ms.
                                      Advance from observed_at_ms only while
                                      ticking and the document is fresh.
                                    required: true
                                  - name: ticking
                                    type: boolean
                                    required: true
                                  - name: counts_down
                                    type: boolean
                                    description: >-
                                      True for a countdown (CS2 round, respawn);
                                      false for elapsed game time.
                                    required: true
                              - name: buffs
                                type: array
                                required: true
                                properties:
                                  - name: kind
                                    type: string
                                    required: true
                                  - name: clock
                                    type: object
                                    required: false
                                    properties:
                                      - name: seconds
                                        type: integer
                                        description: >-
                                          Seconds on the clock at observed_at_ms.
                                          Advance from observed_at_ms only while
                                          ticking and the document is fresh.
                                        required: true
                                      - name: ticking
                                        type: boolean
                                        required: true
                                      - name: counts_down
                                        type: boolean
                                        description: >-
                                          True for a countdown (CS2 round,
                                          respawn); false for elapsed game time.
                                        required: true
                              - name: health
                                type: integer
                                required: false
                              - name: armor
                                type: integer
                                required: false
                              - name: money
                                type: integer
                                required: false
                              - name: loadout
                                type: array
                                required: true
                                properties:
                                  - name: item
                                    type: string
                                    required: false
                              - name: character_id
                                type: string
                                description: >-
                                  The provider's id for the character (LoL
                                  champion id), for portraits; absent before it
                                  is picked.
                                required: false
                          - name: drakes
                            type: array
                            description: >-
                              Elemental dragons in take order (objective
                              variants); elder excluded.
                            required: true
                            properties:
                              - name: item
                                type: string
                                required: false
                          - name: first_kill
                            type: boolean
                            description: True when this team scored the game's first kill.
                            required: false
                      - name: draft
                        type: array
                        required: true
                        properties:
                          - name: sequence
                            type: integer
                            required: true
                          - name: action
                            type: string
                            description: pick or ban.
                            required: true
                          - name: team_id
                            type: string
                            required: true
                          - name: draftable_type
                            type: string
                            description: character or map.
                            required: true
                          - name: draftable
                            type: string
                            required: true
                          - name: draftable_id
                            type: string
                            description: >-
                              The provider's id for the champion, hero, agent or
                              map, for portraits (the same id space as player
                              character_id); absent when unknown.
                            required: false
                      - name: structures
                        type: array
                        required: true
                        properties:
                          - name: id
                            type: string
                            required: true
                          - name: kind
                            type: string
                            required: true
                          - name: owner_team_id
                            type: string
                            description: The defender, not the destroyer.
                            required: true
                          - name: destroyed
                            type: boolean
                            required: true
                          - name: respawn
                            type: object
                            required: false
                            properties:
                              - name: seconds
                                type: integer
                                description: >-
                                  Seconds on the clock at observed_at_ms.
                                  Advance from observed_at_ms only while ticking
                                  and the document is fresh.
                                required: true
                              - name: ticking
                                type: boolean
                                required: true
                              - name: counts_down
                                type: boolean
                                description: >-
                                  True for a countdown (CS2 round, respawn);
                                  false for elapsed game time.
                                required: true
                      - name: timers
                        type: array
                        required: true
                        properties:
                          - name: kind
                            type: string
                            required: true
                          - name: variant
                            type: string
                            required: true
                          - name: clock
                            type: object
                            required: false
                            properties:
                              - name: seconds
                                type: integer
                                description: >-
                                  Seconds on the clock at observed_at_ms.
                                  Advance from observed_at_ms only while ticking
                                  and the document is fresh.
                                required: true
                              - name: ticking
                                type: boolean
                                required: true
                              - name: counts_down
                                type: boolean
                                description: >-
                                  True for a countdown (CS2 round, respawn);
                                  false for elapsed game time.
                                required: true
                      - name: rounds
                        type: array
                        required: true
                        properties:
                          - name: number
                            type: integer
                            required: true
                          - name: started
                            type: boolean
                            required: true
                          - name: finished
                            type: boolean
                            required: true
                          - name: winner_team_id
                            type: string
                            description: Empty while the round runs.
                            required: true
                          - name: win_type
                            type: string
                            required: true
                  - name: recent_plays
                    type: array
                    description: Last 20 plays across the series, newest last.
                    required: true
                    properties:
                      - name: id
                        type: string
                        description: 'Stable provider event id: render a play once per id.'
                        required: true
                      - name: game
                        type: integer
                        required: true
                      - name: round
                        type: integer
                        required: false
                      - name: clock_seconds
                        type: integer
                        required: false
                      - name: type
                        type: string
                        description: >-
                          Provider actor-action-target type, e.g.
                          player-killed-player.
                        required: true
                      - name: kind
                        type: string
                        description: >-
                          Normalized kind: kill, multikill, tower, dragon,
                          baron, victory, round_end, ...
                        required: true
                      - name: variant
                        type: string
                        description: >-
                          Dragon element, or a round_end's win type; empty
                          otherwise.
                        required: true
                      - name: team_id
                        type: string
                        required: true
                      - name: player_name
                        type: string
                        required: true
                      - name: target
                        type: string
                        required: true
                      - name: occurred_at_ms
                        type: integer
                        description: Unix milliseconds.
                        required: false
                      - name: multikill
                        type: integer
                        description: >-
                          Kills in a multikill play: 2 double, 3 triple, 4
                          quadra, 5 penta. Present only when kind is multikill.
                        required: false
        headers: []
        jsonPayloadSchema:
          type: object
          required:
            - v
            - channel
            - seq
            - ts
            - payload
          properties:
            v:
              type: integer
              const: 1
              description: Envelope version.
              x-parser-schema-id: <anonymous-schema-143>
            channel:
              type: string
              const: esports.series
              x-parser-schema-id: <anonymous-schema-144>
            seq:
              type: integer
              description: >-
                Dense per-connection, per-channel sequence, assigned at
                delivery. Resets on every reconnect. Snapshot frames consume a
                seq.
              x-parser-schema-id: <anonymous-schema-145>
            ts:
              type: integer
              description: The document's observed_at_ms; now for a null snapshot.
              x-parser-schema-id: <anonymous-schema-146>
            snapshot:
              type: boolean
              description: >-
                Present and true on the one snapshot frame sent after each new
                subscription. Absent on live frames.
              x-parser-schema-id: <anonymous-schema-147>
            dropped:
              type: integer
              description: >-
                Number of frames dropped on this channel since the last
                delivered frame (slow-consumer signal). Absent when zero.
              x-parser-schema-id: <anonymous-schema-148>
            payload:
              oneOf:
                - type: object
                  required:
                    - event_id
                    - title
                    - source
                    - provider_series_id
                    - schema_version
                    - binding_revision
                    - revision
                    - observed_at_ms
                    - phase
                    - invalidation_reason
                    - feed_status
                    - capabilities
                    - format
                    - best_of
                    - legacy_score
                    - period
                    - teams
                    - games
                    - recent_plays
                  properties:
                    event_id:
                      type: string
                      description: Gamma event id.
                      x-parser-schema-id: <anonymous-schema-149>
                    title:
                      type: string
                      enum:
                        - lol
                        - cs2
                        - dota2
                        - valorant
                        - r6siege
                        - mlbb
                      x-parser-schema-id: <anonymous-schema-150>
                    source:
                      type: string
                      description: Data provider.
                      enum:
                        - grid
                        - pandascore
                      x-parser-schema-id: <anonymous-schema-151>
                    provider_series_id:
                      type: string
                      description: Support and tracing only; never key on it.
                      x-parser-schema-id: <anonymous-schema-152>
                    schema_version:
                      type: integer
                      x-parser-schema-id: <anonymous-schema-153>
                    binding_revision:
                      type: integer
                      description: >-
                        Rises when the event is rebound to another provider
                        series.
                      x-parser-schema-id: <anonymous-schema-154>
                    revision:
                      type: integer
                      description: Rises with every published change; never goes back.
                      x-parser-schema-id: <anonymous-schema-155>
                    source_updated_at_ms:
                      type: integer
                      description: >-
                        When the provider last changed the state. Absent when
                        not reported.
                      x-parser-schema-id: <anonymous-schema-156>
                    observed_at_ms:
                      type: integer
                      description: >-
                        When the producer read this state plus its configurable
                        publish delay: the document is the state as of that
                        delay ago, except feed_status and any live field groups
                        the producer enables (results: phase finished, series
                        games_won/won, game finished/winner_team_id; kills: game
                        team kills/deaths/first_kill), which are current.
                        feed_status live can carry an old observed_at for up to
                        the delay after an outage; judge freshness by
                        observed_at. Freshness is now - observed_at_ms (not
                        applicable once phase is finished); clocks anchor here.
                      x-parser-schema-id: <anonymous-schema-157>
                    published_at_ms:
                      type: integer
                      x-parser-schema-id: <anonymous-schema-158>
                    phase:
                      type: string
                      enum:
                        - upcoming
                        - live
                        - paused
                        - finished
                        - unspecified
                      x-parser-schema-id: <anonymous-schema-159>
                    valid:
                      type: boolean
                      description: >-
                        False while the provider reports the state invalid;
                        absent when not reported.
                      x-parser-schema-id: <anonymous-schema-160>
                    invalidation_reason:
                      type: string
                      x-parser-schema-id: <anonymous-schema-161>
                    feed_status:
                      type: string
                      description: >-
                        live, or delayed/recovering: the document is the last
                        good state.
                      enum:
                        - live
                        - delayed
                        - recovering
                        - unspecified
                      x-parser-schema-id: <anonymous-schema-162>
                    capabilities:
                      type: array
                      items:
                        type: string
                        enum:
                          - series
                          - games
                          - clock
                          - draft
                          - players
                          - objectives
                          - structures
                          - timers
                          - rounds
                          - economy
                          - plays
                        x-parser-schema-id: <anonymous-schema-164>
                      description: >-
                        The optional groups this document fills; an absent field
                        or empty group means unknown, never zero.
                      x-parser-schema-id: <anonymous-schema-163>
                    format:
                      type: string
                      description: e.g. best-of-3.
                      x-parser-schema-id: <anonymous-schema-165>
                    best_of:
                      type: integer
                      x-parser-schema-id: <anonymous-schema-166>
                    current_game:
                      type: integer
                      description: >-
                        Game in play, or next between games; the last game once
                        finished; absent until the series starts.
                      x-parser-schema-id: <anonymous-schema-167>
                    legacy_score:
                      type: string
                      description: >-
                        Legacy card score string, home first, e.g.
                        21-6,10-11,missing|1-0|Bo3. Empty while either side is
                        unresolved, the doc is invalid, or best-of is unknown.
                      x-parser-schema-id: <anonymous-schema-168>
                    period:
                      type: string
                      description: >-
                        Legacy period string: NS until a game starts, then
                        <current_game>/<best_of>, e.g. 2/3. Empty if best-of is
                        unknown. Gate on phase.
                      x-parser-schema-id: <anonymous-schema-169>
                    teams:
                      type: array
                      items:
                        type: object
                        required:
                          - id
                          - name
                          - polymarket_side
                          - games_won
                        properties:
                          id:
                            type: string
                            description: >-
                              Provider team id; games[].teams[].team_id refers
                              to it.
                            x-parser-schema-id: <anonymous-schema-171>
                          name:
                            type: string
                            x-parser-schema-id: <anonymous-schema-172>
                          polymarket_side:
                            type: string
                            description: Side of the Polymarket event this team is on.
                            enum:
                              - home
                              - away
                              - unspecified
                            x-parser-schema-id: <anonymous-schema-173>
                          games_won:
                            type: integer
                            description: Games (LoL) or maps (CS2) won.
                            x-parser-schema-id: <anonymous-schema-174>
                          won:
                            type: boolean
                            description: Present once the series has a winner.
                            x-parser-schema-id: <anonymous-schema-175>
                        x-parser-schema-id: EsportsSeriesTeam
                      x-parser-schema-id: <anonymous-schema-170>
                    games:
                      type: array
                      items:
                        type: object
                        required:
                          - number
                          - map
                          - started
                          - finished
                          - paused
                          - winner_team_id
                          - teams
                          - draft
                          - structures
                          - timers
                          - rounds
                        properties:
                          number:
                            type: integer
                            description: Game number in the series.
                            x-parser-schema-id: <anonymous-schema-177>
                          map:
                            type: string
                            description: >-
                              Map name; for single-map titles the provider's
                              (LoL: Summoner's Rift) or empty.
                            x-parser-schema-id: <anonymous-schema-178>
                          started:
                            type: boolean
                            x-parser-schema-id: <anonymous-schema-179>
                          finished:
                            type: boolean
                            x-parser-schema-id: <anonymous-schema-180>
                          paused:
                            type: boolean
                            x-parser-schema-id: <anonymous-schema-181>
                          winner_team_id:
                            type: string
                            description: >-
                              The provider's explicit winner; empty until there
                              is one.
                            x-parser-schema-id: <anonymous-schema-182>
                          clock: &ref_7
                            type: object
                            required:
                              - seconds
                              - ticking
                              - counts_down
                            properties:
                              seconds:
                                type: integer
                                description: >-
                                  Seconds on the clock at observed_at_ms.
                                  Advance from observed_at_ms only while ticking
                                  and the document is fresh.
                                x-parser-schema-id: <anonymous-schema-183>
                              ticking:
                                type: boolean
                                x-parser-schema-id: <anonymous-schema-184>
                              counts_down:
                                type: boolean
                                description: >-
                                  True for a countdown (CS2 round, respawn);
                                  false for elapsed game time.
                                x-parser-schema-id: <anonymous-schema-185>
                            x-parser-schema-id: EsportsClock
                          teams:
                            type: array
                            items:
                              type: object
                              required:
                                - team_id
                                - side
                                - objectives
                                - players
                                - drakes
                              properties:
                                team_id:
                                  type: string
                                  x-parser-schema-id: <anonymous-schema-187>
                                side:
                                  type: string
                                  description: >-
                                    blue/red (LoL),
                                    terrorists/counter-terrorists (CS2), ...
                                  x-parser-schema-id: <anonymous-schema-188>
                                kills:
                                  type: integer
                                  description: Kills; the per-game score in LoL.
                                  x-parser-schema-id: <anonymous-schema-189>
                                deaths:
                                  type: integer
                                  x-parser-schema-id: <anonymous-schema-190>
                                gold:
                                  type: integer
                                  description: Total gold earned (LoL).
                                  x-parser-schema-id: <anonymous-schema-191>
                                gold_lead:
                                  type: integer
                                  description: This team's gold minus the opponent's.
                                  x-parser-schema-id: <anonymous-schema-192>
                                objectives:
                                  type: array
                                  items:
                                    type: object
                                    required:
                                      - kind
                                      - variant
                                      - count
                                    properties:
                                      kind:
                                        type: string
                                        description: >-
                                          lower_snake: tower, inhibitor, dragon,
                                          baron, herald, void_grub, ...
                                        x-parser-schema-id: <anonymous-schema-194>
                                      variant:
                                        type: string
                                        description: >-
                                          Dragon element where it matters; empty
                                          otherwise.
                                        x-parser-schema-id: <anonymous-schema-195>
                                      count:
                                        type: integer
                                        x-parser-schema-id: <anonymous-schema-196>
                                      first:
                                        type: boolean
                                        description: >-
                                          True when this team took the kind first
                                          in the game.
                                        x-parser-schema-id: <anonymous-schema-197>
                                    x-parser-schema-id: EsportsObjective
                                  x-parser-schema-id: <anonymous-schema-193>
                                baron_power_play:
                                  type: integer
                                  x-parser-schema-id: <anonymous-schema-198>
                                rounds_won:
                                  type: integer
                                  description: Rounds won; the per-map score in CS2.
                                  x-parser-schema-id: <anonymous-schema-199>
                                money:
                                  type: integer
                                  x-parser-schema-id: <anonymous-schema-200>
                                players:
                                  type: array
                                  items:
                                    type: object
                                    required:
                                      - id
                                      - name
                                      - buffs
                                      - loadout
                                    properties:
                                      id:
                                        type: string
                                        x-parser-schema-id: <anonymous-schema-202>
                                      name:
                                        type: string
                                        x-parser-schema-id: <anonymous-schema-203>
                                      character:
                                        type: string
                                        description: >-
                                          Champion, hero or agent; absent before
                                          it is picked.
                                        x-parser-schema-id: <anonymous-schema-204>
                                      kills:
                                        type: integer
                                        x-parser-schema-id: <anonymous-schema-205>
                                      deaths:
                                        type: integer
                                        x-parser-schema-id: <anonymous-schema-206>
                                      assists:
                                        type: integer
                                        x-parser-schema-id: <anonymous-schema-207>
                                      alive:
                                        type: boolean
                                        x-parser-schema-id: <anonymous-schema-208>
                                      gold:
                                        type: integer
                                        description: Total gold earned (LoL).
                                        x-parser-schema-id: <anonymous-schema-209>
                                      respawn: *ref_7
                                      buffs:
                                        type: array
                                        items:
                                          type: object
                                          required:
                                            - kind
                                          properties:
                                            kind:
                                              type: string
                                              x-parser-schema-id: <anonymous-schema-211>
                                            clock: *ref_7
                                          x-parser-schema-id: EsportsBuff
                                        x-parser-schema-id: <anonymous-schema-210>
                                      health:
                                        type: integer
                                        x-parser-schema-id: <anonymous-schema-212>
                                      armor:
                                        type: integer
                                        x-parser-schema-id: <anonymous-schema-213>
                                      money:
                                        type: integer
                                        x-parser-schema-id: <anonymous-schema-214>
                                      loadout:
                                        type: array
                                        items:
                                          type: string
                                          x-parser-schema-id: <anonymous-schema-216>
                                        x-parser-schema-id: <anonymous-schema-215>
                                      character_id:
                                        type: string
                                        description: >-
                                          The provider's id for the character (LoL
                                          champion id), for portraits; absent
                                          before it is picked.
                                        x-parser-schema-id: <anonymous-schema-217>
                                    description: >-
                                      Title-specific fields are absent for other
                                      titles.
                                    x-parser-schema-id: EsportsPlayer
                                  x-parser-schema-id: <anonymous-schema-201>
                                drakes:
                                  type: array
                                  items:
                                    type: string
                                    x-parser-schema-id: <anonymous-schema-219>
                                  description: >-
                                    Elemental dragons in take order (objective
                                    variants); elder excluded.
                                  x-parser-schema-id: <anonymous-schema-218>
                                first_kill:
                                  type: boolean
                                  description: >-
                                    True when this team scored the game's first
                                    kill.
                                  x-parser-schema-id: <anonymous-schema-220>
                              x-parser-schema-id: EsportsGameTeam
                            x-parser-schema-id: <anonymous-schema-186>
                          draft:
                            type: array
                            items:
                              type: object
                              required:
                                - sequence
                                - action
                                - team_id
                                - draftable_type
                                - draftable
                              properties:
                                sequence:
                                  type: integer
                                  x-parser-schema-id: <anonymous-schema-222>
                                action:
                                  type: string
                                  description: pick or ban.
                                  x-parser-schema-id: <anonymous-schema-223>
                                team_id:
                                  type: string
                                  x-parser-schema-id: <anonymous-schema-224>
                                draftable_type:
                                  type: string
                                  description: character or map.
                                  x-parser-schema-id: <anonymous-schema-225>
                                draftable:
                                  type: string
                                  x-parser-schema-id: <anonymous-schema-226>
                                draftable_id:
                                  type: string
                                  description: >-
                                    The provider's id for the champion, hero,
                                    agent or map, for portraits (the same id
                                    space as player character_id); absent when
                                    unknown.
                                  x-parser-schema-id: <anonymous-schema-227>
                              x-parser-schema-id: EsportsDraftAction
                            x-parser-schema-id: <anonymous-schema-221>
                          structures:
                            type: array
                            items:
                              type: object
                              required:
                                - id
                                - kind
                                - owner_team_id
                                - destroyed
                              properties:
                                id:
                                  type: string
                                  x-parser-schema-id: <anonymous-schema-229>
                                kind:
                                  type: string
                                  x-parser-schema-id: <anonymous-schema-230>
                                owner_team_id:
                                  type: string
                                  description: The defender, not the destroyer.
                                  x-parser-schema-id: <anonymous-schema-231>
                                destroyed:
                                  type: boolean
                                  x-parser-schema-id: <anonymous-schema-232>
                                respawn: *ref_7
                              x-parser-schema-id: EsportsStructure
                            x-parser-schema-id: <anonymous-schema-228>
                          timers:
                            type: array
                            items:
                              type: object
                              required:
                                - kind
                                - variant
                              properties:
                                kind:
                                  type: string
                                  x-parser-schema-id: <anonymous-schema-234>
                                variant:
                                  type: string
                                  x-parser-schema-id: <anonymous-schema-235>
                                clock: *ref_7
                              x-parser-schema-id: EsportsTimer
                            x-parser-schema-id: <anonymous-schema-233>
                          rounds:
                            type: array
                            items:
                              type: object
                              required:
                                - number
                                - started
                                - finished
                                - winner_team_id
                                - win_type
                              properties:
                                number:
                                  type: integer
                                  x-parser-schema-id: <anonymous-schema-237>
                                started:
                                  type: boolean
                                  x-parser-schema-id: <anonymous-schema-238>
                                finished:
                                  type: boolean
                                  x-parser-schema-id: <anonymous-schema-239>
                                winner_team_id:
                                  type: string
                                  description: Empty while the round runs.
                                  x-parser-schema-id: <anonymous-schema-240>
                                win_type:
                                  type: string
                                  x-parser-schema-id: <anonymous-schema-241>
                              x-parser-schema-id: EsportsRound
                            x-parser-schema-id: <anonymous-schema-236>
                        description: >-
                          Exactly one game carries players, draft, structures,
                          timers and rounds: current_game once the provider
                          lists it, else the last game played (between games,
                          after the finish), else game 1. Every other game is a
                          summary.
                        x-parser-schema-id: EsportsGame
                      x-parser-schema-id: <anonymous-schema-176>
                    recent_plays:
                      type: array
                      items:
                        type: object
                        required:
                          - id
                          - game
                          - type
                          - kind
                          - variant
                          - team_id
                          - player_name
                          - target
                        properties:
                          id:
                            type: string
                            description: >-
                              Stable provider event id: render a play once per
                              id.
                            x-parser-schema-id: <anonymous-schema-243>
                          game:
                            type: integer
                            x-parser-schema-id: <anonymous-schema-244>
                          round:
                            type: integer
                            x-parser-schema-id: <anonymous-schema-245>
                          clock_seconds:
                            type: integer
                            x-parser-schema-id: <anonymous-schema-246>
                          type:
                            type: string
                            description: >-
                              Provider actor-action-target type, e.g.
                              player-killed-player.
                            x-parser-schema-id: <anonymous-schema-247>
                          kind:
                            type: string
                            description: >-
                              Normalized kind: kill, multikill, tower, dragon,
                              baron, victory, round_end, ...
                            x-parser-schema-id: <anonymous-schema-248>
                          variant:
                            type: string
                            description: >-
                              Dragon element, or a round_end's win type; empty
                              otherwise.
                            x-parser-schema-id: <anonymous-schema-249>
                          team_id:
                            type: string
                            x-parser-schema-id: <anonymous-schema-250>
                          player_name:
                            type: string
                            x-parser-schema-id: <anonymous-schema-251>
                          target:
                            type: string
                            x-parser-schema-id: <anonymous-schema-252>
                          occurred_at_ms:
                            type: integer
                            description: Unix milliseconds.
                            x-parser-schema-id: <anonymous-schema-253>
                          multikill:
                            type: integer
                            description: >-
                              Kills in a multikill play: 2 double, 3 triple, 4
                              quadra, 5 penta. Present only when kind is
                              multikill.
                            x-parser-schema-id: <anonymous-schema-254>
                        x-parser-schema-id: EsportsPlay
                      description: Last 20 plays across the series, newest last.
                      x-parser-schema-id: <anonymous-schema-242>
                  x-parser-schema-id: EsportsSeriesDoc
                - type: 'null'
                  description: >-
                    Snapshot only: no live document for this event (unbound or
                    not live).
                  x-parser-schema-id: <anonymous-schema-255>
              x-parser-schema-id: EsportsSeriesPayload
          description: Every frame carries the full document; replace, never merge.
          x-parser-schema-id: EsportsSeriesEnvelope
        title: esports.series envelope
        example: |-
          {
            "v": 1,
            "channel": "esports.series",
            "seq": 2,
            "ts": 1790000000000,
            "payload": {
              "event_id": "184213",
              "title": "lol",
              "source": "grid",
              "provider_series_id": "2843071",
              "schema_version": 1,
              "binding_revision": 3,
              "revision": 42,
              "source_updated_at_ms": 1789999998000,
              "observed_at_ms": 1790000000000,
              "published_at_ms": 1790000000005,
              "phase": "live",
              "valid": true,
              "invalidation_reason": "",
              "feed_status": "live",
              "capabilities": [
                "series",
                "plays"
              ],
              "format": "best-of-3",
              "best_of": 3,
              "current_game": 1,
              "legacy_score": "0-0,missing,missing|0-0|Bo3",
              "period": "1/3",
              "teams": [
                {
                  "id": "47",
                  "name": "T1",
                  "polymarket_side": "home",
                  "games_won": 0
                },
                {
                  "id": "48",
                  "name": "G2",
                  "polymarket_side": "away",
                  "games_won": 0
                }
              ],
              "games": [
                {
                  "number": 1,
                  "map": "",
                  "started": true,
                  "finished": false,
                  "paused": false,
                  "winner_team_id": "",
                  "clock": {
                    "seconds": 754,
                    "ticking": true,
                    "counts_down": false
                  },
                  "teams": [
                    {
                      "team_id": "47",
                      "side": "blue",
                      "kills": 0,
                      "objectives": [],
                      "players": [],
                      "drakes": [
                        "infernal"
                      ],
                      "first_kill": false
                    },
                    {
                      "team_id": "48",
                      "side": "red",
                      "kills": 0,
                      "objectives": [],
                      "players": [],
                      "drakes": [],
                      "first_kill": false
                    }
                  ],
                  "draft": [],
                  "structures": [],
                  "timers": [],
                  "rounds": []
                }
              ],
              "recent_plays": [
                {
                  "id": "e1",
                  "game": 1,
                  "type": "player-completed-slayDragon",
                  "kind": "dragon",
                  "variant": "infernal",
                  "team_id": "47",
                  "player_name": "",
                  "target": "",
                  "occurred_at_ms": 1789999999000
                }
              ]
            }
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: esportsSeries
    bindings: []
    extensions: *ref_3
  - &ref_12
    id: challenge
    title: Request the challenge
    description: Ask for this connection's challenge nonce
    type: receive
    messages:
      - &ref_24
        id: challengeRequest
        payload:
          - name: challenge (request)
            description: Ask for this connection's challenge nonce
            type: object
            properties:
              - name: const
                type: string
                description: challenge
                required: false
              - name: rid
                type: string
                required: false
        headers: []
        jsonPayloadSchema:
          type: object
          required:
            - op
          properties:
            op:
              const: challenge
              x-parser-schema-id: <anonymous-schema-259>
            rid:
              type: string
              x-parser-schema-id: <anonymous-schema-260>
          x-parser-schema-id: ChallengeRequest
        title: challenge (request)
        description: Ask for this connection's challenge nonce
        example: |-
          {
            "op": "challenge",
            "rid": "c1"
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: challengeRequest
    bindings: []
    extensions: *ref_3
sendOperations:
  - *ref_8
  - *ref_9
  - *ref_10
  - *ref_11
  - *ref_12
receiveOperations:
  - *ref_13
  - *ref_14
  - *ref_15
  - *ref_16
  - *ref_17
  - *ref_18
  - *ref_19
sendMessages:
  - *ref_20
  - *ref_21
  - *ref_22
  - *ref_23
  - *ref_24
receiveMessages:
  - *ref_25
  - *ref_26
  - *ref_27
  - *ref_28
  - *ref_29
  - *ref_30
  - *ref_31
  - *ref_32
  - *ref_33
  - *ref_34
  - *ref_35
  - *ref_36
extensions:
  - id: x-parser-unique-object-id
    value: ws
securitySchemes: []

````

This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
