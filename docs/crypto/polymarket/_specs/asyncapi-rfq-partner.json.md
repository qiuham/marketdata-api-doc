---
api_type: spec
source_type: llms_txt
version: ''
scope: crypto
asset_class: prediction_market
domain: exchanges
provider: polymarket
provider_name: Polymarket
product: api
product_id: polymarket
source_url: 'https://docs.polymarket.com/asyncapi-rfq-partner.json'
updated_at: 2026-11-13
---

# asyncapi-rfq-partner.json

Source: https://docs.polymarket.com/asyncapi-rfq-partner.json

```json
{
  "asyncapi": "3.0.0",
  "info": {
    "title": "Polymarket RFQ Trades — Partner Stream",
    "version": "1.0.0",
    "description": "Live status of a partner's RFQ trades, so it does not have to poll. On connect the server\nsends one `trade_update` per in-flight trade, then one per status change. Only the partner's\nown trades are sent.\n\nDelivery is lossy by design: the stream is a latency optimisation, not a ledger. After a\nreconnect, or for any trade whose outcome matters, read `GET /v1/rfq-trades/{tradeId}`\n(`openapi.yaml`), which is the source of truth.\n\nThe upgrade request is authenticated like any partner `GET`: sign\n`timestamp + \"GET\" + \"/v1/ws/rfq-trades\"` with an empty body and send the three `RFQ-*`\nheaders. The server pings every 45 seconds and closes a connection that has not answered\nwithin 60. Messages sent by the client are ignored.\n"
  },
  "servers": {
    "production": {
      "host": "external-rfq-partner.polymarket.com",
      "protocol": "wss",
      "description": "Production",
      "security": [
        {
          "$ref": "#/components/securitySchemes/RfqKeyId"
        },
        {
          "$ref": "#/components/securitySchemes/RfqTimestamp"
        },
        {
          "$ref": "#/components/securitySchemes/RfqSignature"
        }
      ]
    }
  },
  "channels": {
    "rfqTrades": {
      "address": "/v1/ws/rfq-trades",
      "messages": {
        "tradeUpdate": {
          "$ref": "#/components/messages/tradeUpdate"
        }
      },
      "bindings": {
        "ws": {
          "method": "GET"
        }
      }
    }
  },
  "operations": {
    "sendTradeUpdates": {
      "action": "send",
      "summary": "The server sends each in-flight trade on connect, then every status change.",
      "channel": {
        "$ref": "#/channels/rfqTrades"
      },
      "messages": [
        {
          "$ref": "#/channels/rfqTrades/messages/tradeUpdate"
        }
      ]
    }
  },
  "components": {
    "securitySchemes": {
      "RfqKeyId": {
        "type": "httpApiKey",
        "name": "RFQ-Key-Id",
        "in": "header",
        "description": "The public half of the partner's API key."
      },
      "RfqTimestamp": {
        "type": "httpApiKey",
        "name": "RFQ-Timestamp",
        "in": "header",
        "description": "Unix seconds, within 30 seconds of server time."
      },
      "RfqSignature": {
        "type": "httpApiKey",
        "name": "RFQ-Signature",
        "in": "header",
        "description": "base64url(HMAC-SHA256(secret, timestamp + method + path + body)), padded."
      }
    },
    "messages": {
      "tradeUpdate": {
        "name": "trade_update",
        "summary": "A trade's current status, the same object `GET /v1/rfq-trades/{tradeId}` returns.",
        "contentType": "application/json",
        "payload": {
          "$ref": "#/components/schemas/TradeUpdateFrame"
        },
        "examples": [
          {
            "name": "filled",
            "payload": {
              "type": "trade_update",
              "trade": {
                "tradeId": "6f1c2b8e-3d4a-4f5b-9c6d-7e8f9a0b1c2d",
                "idempotencyKey": "partner-ref-123",
                "status": "FILLED",
                "transactionHash": "0x5e1c0b2a9f8d7c6b5a4e3d2c1b0a9f8e7d6c5b4a3e2d1c0b9a8f7e6d5c4b3a2e",
                "createdAt": "2026-07-24T12:34:56Z",
                "filledAt": "2026-07-24T12:35:12Z"
              }
            }
          }
        ]
      }
    },
    "schemas": {
      "Combo": {
        "type": "object",
        "description": "A combo's on-chain identity. Present on combo trades only.",
        "required": ["conditionId", "tokenIdYes", "tokenIdNo", "legs"],
        "properties": {
          "conditionId": {
            "type": "string"
          },
          "tokenIdYes": {
            "$ref": "#/components/schemas/Uint256"
          },
          "tokenIdNo": {
            "$ref": "#/components/schemas/Uint256"
          },
          "legs": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/ComboLeg"
            }
          }
        }
      },
      "ComboLeg": {
        "type": "object",
        "required": ["marketId", "outcome"],
        "properties": {
          "marketId": {
            "type": "string",
            "description": "A gamma market id."
          },
          "outcome": {
            "type": "string",
            "enum": ["yes", "no"]
          }
        }
      },
      "RejectionReason": {
        "type": "string",
        "description": "The machine-readable reason a check failed or a request was rejected. New values may be\nadded. See the guardrail and validation guides for each one.\n",
        "enum": [
          "unknown_account",
          "account_restricted",
          "ofac_blocked",
          "insufficient_balance",
          "insufficient_allowance",
          "dependency_unavailable",
          "invalid_order",
          "token_market_mismatch",
          "stale_order",
          "fee_not_accepted",
          "market_not_tradable",
          "price_out_of_band",
          "price_deviation_exceeded",
          "price_mark_missing",
          "transaction_notional_exceeded",
          "taker_notional_below_minimum",
          "counterparty_notional_exceeded"
        ]
      },
      "TradeState": {
        "type": "string",
        "enum": ["PENDING", "FILLED", "REJECTED"],
        "description": "`PENDING` until the trade lands on-chain (`FILLED`) or is refused or fails (`REJECTED`)."
      },
      "TradeStatus": {
        "type": "object",
        "required": ["tradeId", "idempotencyKey", "status", "createdAt"],
        "properties": {
          "tradeId": {
            "type": "string",
            "format": "uuid"
          },
          "combo": {
            "$ref": "#/components/schemas/Combo"
          },
          "idempotencyKey": {
            "type": "string"
          },
          "status": {
            "$ref": "#/components/schemas/TradeState"
          },
          "transactionHash": {
            "type": "string"
          },
          "failureReason": {
            "description": "Why a `REJECTED` trade failed. `execution_failed` is a failure after submission to the exchange.",
            "anyOf": [
              {
                "$ref": "#/components/schemas/RejectionReason"
              },
              {
                "type": "string",
                "enum": ["execution_failed"]
              }
            ]
          },
          "createdAt": {
            "type": "string",
            "format": "date-time"
          },
          "filledAt": {
            "type": "string",
            "format": "date-time"
          }
        }
      },
      "TradeUpdateFrame": {
        "type": "object",
        "description": "One message on the trade status stream.",
        "required": ["type", "trade"],
        "properties": {
          "type": {
            "type": "string",
            "enum": ["trade_update"]
          },
          "trade": {
            "$ref": "#/components/schemas/TradeStatus"
          }
        }
      },
      "Uint256": {
        "type": "string",
        "pattern": "^[0-9]+$",
        "description": "A base-10 uint256."
      }
    }
  }
}
```
