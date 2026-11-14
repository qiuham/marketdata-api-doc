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
source_url: 'https://docs.kraken.com/api-reference/transfer/cancel-a-pay-transfer-or-an-unclaimed-paylink'
updated_at: 2026-11-13
---

# Cancel a pay transfer or an unclaimed paylink

> Cancel a pay transfer or an **unclaimed** paylink

**API Key Permissions Required:** `Funds permissions - Query`




## OpenAPI

````yaml /openapi/pay-rest.yaml post /private/Pay/transfer/cancel
openapi: 3.0.0
info:
  title: REST API
  version: 1.1.0
  description: ''
servers:
  - url: https://api.kraken.com/0
    description: Production Server
security:
  - API-Key: []
    API-Sign: []
tags:
  - name: Request
  - name: Transfer
  - name: Paylink
paths:
  /private/Pay/transfer/cancel:
    post:
      tags:
        - Transfer
        - Paylink
      summary: Cancel a pay transfer or an unclaimed paylink
      description: |
        Cancel a pay transfer or an **unclaimed** paylink

        **API Key Permissions Required:** `Funds permissions - Query`
      operationId: cancelPayTransfer
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/cancelPayTransfer'
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/cancelPayTransfer-2'
          description: ''
components:
  schemas:
    cancelPayTransfer:
      type: object
      required:
        - nonce
        - external_id
      properties:
        nonce:
          description: Nonce used in construction of `API-Sign` header
          type: string
        external_id:
          description: >-
            Your (the API user's) unique id to globally identify transfers and
            requests.


            We will accept anything from 1-16 bytes, the format is base64
            without padding (
            <https://en.wikipedia.org/wiki/Base64#Decoding_Base64_without_padding>
            )


            This is the id you will use to identify all transfers and requests
            in the API and also in the callback we send you.


            You MUST make sure this is commited in your database before calling
            our API, that way if you don't get a response, you can make the same
            call again and we'll fail with an error saying your id is already
            used. (this is the only way to prevent double requests or sends)


            We *highly* recommend you generate and send a UUID here, but if
            instead you have a database auto-increment id that is 64 bits, just
            send that, perhaps pre-pended by an application id or something. 
            The format is completely up to you but keep in mind it must be
            forever unique across all your transfers and requests.
          type: string
    cancelPayTransfer-2:
      type: object
      required:
        - error
      properties:
        error:
          type: array
          items:
            description: General API error.
            type: object
            properties:
              severity:
                description: API error severity.
                type: string
                enum:
                  - E
                  - W
              errorClass:
                type: string
              type:
                type: string
              errorMessage:
                nullable: true
                type: string
            required:
              - errorClass
              - severity
              - type
        result:
          nullable: true
          type: object
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
