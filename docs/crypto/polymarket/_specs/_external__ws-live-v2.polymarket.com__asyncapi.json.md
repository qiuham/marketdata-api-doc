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
source_url: 'https://ws-live-v2.polymarket.com/asyncapi.json'
updated_at: 2026-11-13
---

# asyncapi.json

Source: https://ws-live-v2.polymarket.com/asyncapi.json

```json
{
  "asyncapi": "3.0.0",
  "info": {
    "title": "Polymarket PolyBolt WebSocket",
    "version": "2.0.0",
    "description": "Real-time push socket for Polymarket market prices and licensed reference prices. One connection carries many channel subscriptions. Every server frame is a uniform envelope with a dense per-channel sequence, a snapshot barrier on subscribe, and typed close codes. Replaces the legacy Real-Time Data Service (RTDS)."
  },
  "servers": {
    "production": {
      "host": "ws-live-v2.polymarket.com",
      "pathname": "/ws",
      "protocol": "wss",
      "description": "Production socket. The same host serves the Polymarket web app's ticket endpoint; third-party clients authenticate gated channels with an Access Token or CLOB API credentials over the socket itself."
    }
  },
  "channels": {
    "ws": {
      "address": "/ws",
      "title": "Live Data Channel",
      "description": "Send JSON text frames tagged with op. The server answers every op with an ack or an error ack (never a close, except for policy breaches, close 4008, and an expired Access Token, close 1008) and pushes envelopes for subscribed channels. Limits per connection: 64 active (channel, filter) subscriptions, 20 subscribe or unsubscribe frames per second (a batch frame counts once), 64 KB per frame, 8 auth attempts. The server sends a WebSocket ping every 25 seconds; two missed pongs close 4002. Close codes: 4001 authentication failed on a presented credential, 4002 slow consumer or pong timeout, 4003 server draining (reconnect once after a uniform 0 to 10 s delay), 4008 policy violation (fix the client; do not reconnect blindly), which also closes a socket that neither passed authentication nor registered a subscription within the server's unengaged timeout (120 seconds by default, reason text unengaged) once that rule is enforced, 1008 authentication expired (a connection authenticated with an Access Token whose last accepted token expired, 30 second leeway included, with no renewal; refresh the token and reconnect).",
      "messages": {
        "subscribe": {
          "$ref": "#/components/messages/subscribe"
        },
        "unsubscribe": {
          "$ref": "#/components/messages/unsubscribe"
        },
        "auth": {
          "$ref": "#/components/messages/auth"
        },
        "ping": {
          "$ref": "#/components/messages/ping"
        },
        "subscribed": {
          "$ref": "#/components/messages/subscribed"
        },
        "unsubscribed": {
          "$ref": "#/components/messages/unsubscribed"
        },
        "authed": {
          "$ref": "#/components/messages/authed"
        },
        "pong": {
          "$ref": "#/components/messages/pong"
        },
        "error": {
          "$ref": "#/components/messages/error"
        },
        "pricePolymarket": {
          "$ref": "#/components/messages/pricePolymarket"
        },
        "priceCrypto": {
          "$ref": "#/components/messages/priceCrypto"
        },
        "priceEquity": {
          "$ref": "#/components/messages/priceEquity"
        },
        "priceCryptoTwap": {
          "$ref": "#/components/messages/priceCryptoTwap"
        },
        "priceEquityTwap": {
          "$ref": "#/components/messages/priceEquityTwap"
        },
        "esportsSeries": {
          "$ref": "#/components/messages/esportsSeries"
        },
        "challenge": {
          "$ref": "#/components/messages/challenge"
        },
        "challengeRequest": {
          "$ref": "#/components/messages/challengeRequest"
        }
      }
    }
  },
  "operations": {
    "subscribe": {
      "action": "receive",
      "channel": {
        "$ref": "#/channels/ws"
      },
      "title": "Subscribe",
      "summary": "Add one or more (channel, filter) subscriptions",
      "description": "Batch form: subscriptions is an array of {channel, filter}. Singular form: {op: subscribe, channel, filter}. Each newly added subscription is acknowledged with subscribed, then receives exactly one snapshot envelope (snapshot: true), then live frames. A duplicate (channel, filter) is acknowledged again without a new snapshot. A gated channel on an unauthenticated connection answers the non-closing error code auth_required; other subscriptions on the same connection are unaffected.",
      "messages": [
        {
          "$ref": "#/channels/ws/messages/subscribe"
        }
      ]
    },
    "unsubscribe": {
      "action": "receive",
      "channel": {
        "$ref": "#/channels/ws"
      },
      "title": "Unsubscribe",
      "summary": "Remove subscriptions; same singular and batch shapes as subscribe",
      "messages": [
        {
          "$ref": "#/channels/ws/messages/unsubscribe"
        }
      ]
    },
    "auth": {
      "action": "receive",
      "channel": {
        "$ref": "#/channels/ws"
      },
      "title": "Authenticate",
      "summary": "Unlock the gated channels on this connection with an Access Token, CLOB API credentials or a web-app ticket",
      "description": "Send before subscribing to price.crypto, price.equity, price.crypto.twap or price.equity.twap. Answered with authed. A refused credential answers the non-closing error code auth_invalid; an unreachable verifier answers auth_unavailable (retry later). Idempotent once authenticated, except on a connection authenticated with an Access Token: there a new Access Token renews the connection. Send it before the current token expires, after refreshing over HTTP (never send the Refresh Token on the socket). The renewal must carry the same sub and client_id (a visitor connection renews with any visitor token; a renewal never switches between visitor and Access Token); it answers authed with its rid, replaces the expiry deadline and keeps every subscription. A refused renewal answers auth_invalid or auth_unavailable and keeps the previous deadline, and CLOB credentials or a ticket on that connection answer bad_op. The server closes the connection 1008 authentication expired when the last accepted token expires, 30 second leeway included, even if the client sends nothing. Lifetime budget of 8 auth frames per connection, accepted renewals excepted; the ninth closes 4008. The Polymarket web app uses a different credential in the same op (a one-time ticket in the ticket field); third-party clients use the auth object, with CLOB API credentials or an Identity Provider Access Token ({\"accessToken\": ...}). A web-app ticket is minted from a Turnstile solve; when the widget carried this connection's challenge nonce (see the challenge frame) the ticket verifies on this socket alone, and one minted for another socket answers the non-closing auth_expired (mint again).",
      "messages": [
        {
          "$ref": "#/channels/ws/messages/auth"
        }
      ]
    },
    "ping": {
      "action": "receive",
      "channel": {
        "$ref": "#/channels/ws"
      },
      "title": "Ping",
      "summary": "Optional application-level liveness probe; answered with pong",
      "description": "Not required for keepalive: the server sends WebSocket ping frames every 25 seconds and standard clients answer them automatically.",
      "messages": [
        {
          "$ref": "#/channels/ws/messages/ping"
        }
      ]
    },
    "acknowledgements": {
      "action": "send",
      "channel": {
        "$ref": "#/channels/ws"
      },
      "title": "Acknowledgements",
      "summary": "challenge (on request), subscribed, unsubscribed, authed, pong and error acks; rid is echoed when the request carried one",
      "messages": [
        {
          "$ref": "#/channels/ws/messages/challenge"
        },
        {
          "$ref": "#/channels/ws/messages/subscribed"
        },
        {
          "$ref": "#/channels/ws/messages/unsubscribed"
        },
        {
          "$ref": "#/channels/ws/messages/authed"
        },
        {
          "$ref": "#/channels/ws/messages/pong"
        },
        {
          "$ref": "#/channels/ws/messages/error"
        }
      ]
    },
    "pricePolymarket": {
      "action": "send",
      "channel": {
        "$ref": "#/channels/ws"
      },
      "title": "price.polymarket",
      "summary": "Best bid and ask per outcome token (public, no auth)",
      "description": "Filter: {asset_id: <outcome token id, decimal string>}. Snapshot payload: the latest best bid and ask for the token, or an empty array [] when the token has not traded within the server's warm window. Live payload: one best-bid-and-ask object per change. Same-token updates are conflated (latest wins) when the client is slow.",
      "messages": [
        {
          "$ref": "#/channels/ws/messages/pricePolymarket"
        }
      ]
    },
    "priceCrypto": {
      "action": "send",
      "channel": {
        "$ref": "#/channels/ws"
      },
      "title": "price.crypto",
      "summary": "Crypto reference prices, about one update per second per symbol (gated)",
      "description": "Filter: {symbol}, lowercase, one of btcusd, ethusd, solusd, dogeusd, xrpusd, bnbusd, hypeusd, zecusd. Snapshot payload: {symbol, source, data: [points for the previous two minutes]}. Live payload: one point. Every payload names the vendor that produced it in source (pyth, chainlink or binance; ownership is a per-symbol operator decision, and this is the ONLY channel that can serve binance - spec 09); during a rolling ownership flip old and new pods serve different vendors for the flipped symbol, so consecutive frames can carry different sources until the roll completes. A binance-sourced value is the Binance USDT-quoted close relayed verbatim under the usd-named symbol (no conversion leg): expect a basis-point-scale delta against pyth/chainlink normally, and a percent-scale divergence during a USDT depeg - exactly the moment comparisons are most likely.",
      "messages": [
        {
          "$ref": "#/channels/ws/messages/priceCrypto"
        }
      ]
    },
    "priceEquity": {
      "action": "send",
      "channel": {
        "$ref": "#/channels/ws"
      },
      "title": "price.equity",
      "summary": "Pyth equity, ETF, forex, metals and commodity reference prices (gated)",
      "description": "Filter: {symbol}, lowercase. Catalog: stocks aapl, tsla, msft, googl, amzn, meta, nvda, nflx, pltr, open, rklb, abnb, coin, hood; ETFs qqq, spy, ewy, vxx; forex eurusd, gbpusd, usdcad, usdjpy, usdkrw; precious metals xauusd, xagusd; commodities wti, cc, ngd (front-month futures, the symbol stays the root while the contract rolls). Snapshot payload: {symbol, source, data: [points for the previous two minutes]}. Live payload: one point with optional received_at and is_carried_forward. Every payload names the vendor that produced it in source (pyth, massive or chainlink; ownership is a per-symbol operator decision); during a rolling ownership flip old and new pods serve different vendors for the flipped symbol, so consecutive frames can carry different sources until the roll completes. Equity payloads also carry market_status (open, closed or unknown) once a producer states it: the market of the instrument the series prices, per provider, absent when not stated. A status change that repeats the last price arrives as a normal live frame with that price, is_carried_forward true and the new market_status, so a frame with an unchanged timestamp is NOT a duplicate when its market_status changed: never dedup on timestamp. While a series is closed or unknown, its snapshot also carries the last price point when it is older than the two-minute window.",
      "messages": [
        {
          "$ref": "#/channels/ws/messages/priceEquity"
        }
      ]
    },
    "priceCryptoTwap": {
      "action": "send",
      "channel": {
        "$ref": "#/channels/ws"
      },
      "title": "price.crypto.twap",
      "summary": "Chainlink time-weighted average prices used by crypto up/down market resolution (gated)",
      "description": "Filter: {symbol, window_seconds}. Only window_seconds 60 exists; symbols btcusd, ethusd, solusd, xrpusd, dogeusd, hypeusd, bnbusd. Another positive window is accepted but never carries data. Snapshot payload: {symbol, window_seconds, data: [points]}. Live payload: one point including window_seconds.",
      "messages": [
        {
          "$ref": "#/channels/ws/messages/priceCryptoTwap"
        }
      ]
    },
    "priceEquityTwap": {
      "action": "send",
      "channel": {
        "$ref": "#/channels/ws"
      },
      "title": "price.equity.twap",
      "summary": "Chainlink Data Streams FX time-weighted average prices (gated)",
      "description": "Filter: {symbol, window_seconds}. Launch feeds eurusd and usdjpy at window_seconds 60; another positive window is accepted but never carries data. Ticket-gated like the other vendor channels and snapshot-then-live like price.crypto.twap. Snapshot payload: {symbol, window_seconds, source, data: [points]}. Live payload: one point including window_seconds and source. Every payload names the vendor that produced it in source; the channel is Chainlink-only today, so the value is chainlink. Payloads also carry market_status (the FX TWAPs are continuous-hours products and read open), absent when not stated; on this channel it changes only with a new price.",
      "messages": [
        {
          "$ref": "#/channels/ws/messages/priceEquityTwap"
        }
      ]
    },
    "esportsSeries": {
      "action": "send",
      "channel": {
        "$ref": "#/channels/ws"
      },
      "title": "esports.series",
      "summary": "Live esports series state for a Polymarket event: score, games, clock and plays (public by default)",
      "description": "Filter: {event_id} (Gamma event id string). Public by default: no auth needed. A deployment may gate it (AUTH_EXTRA_GATED_CHANNELS), and then it answers auth_required until the connection authenticates, like the vendor price channels. The snapshot is the latest document, or null when the event has no live document. Then one frame per new document; the producer's 15 s keep-alive re-sends the same document, which keeps it held but emits no frame (except to complete a served-provider switch, see EventIdFilter.provider); every frame carries the full document (latest wins under backpressure). One shape for every title (lol, cs2, ...): each title fills its own optional groups, listed in capabilities. Freshness is now - observed_at_ms; feed_status delayed or recovering means the document is the last good state. Optional filter provider (grid|pandascore) pins one provider's document; see EventIdFilter.provider.",
      "messages": [
        {
          "$ref": "#/channels/ws/messages/esportsSeries"
        }
      ]
    },
    "challenge": {
      "action": "receive",
      "channel": {
        "$ref": "#/channels/ws"
      },
      "title": "Request the challenge",
      "summary": "Ask for this connection's challenge nonce",
      "description": "Ask for this connection's challenge nonce. The server never pushes it unasked: a client that authenticates with a ticket sends this right after the socket opens, then renders the Turnstile widget with the nonce as cData. Idempotent (the same nonce for the life of the connection, rid echoed) and metered like subscribe and auth. A nonce field in the request is ignored: a client can never choose its own. A server that predates this op answers the non-closing bad_op error ack with no rid (the frame did not parse): treat an uncorrelated bad_op while the request is pending as no nonce served, and render the widget without cData.",
      "messages": [
        {
          "$ref": "#/channels/ws/messages/challengeRequest"
        }
      ]
    }
  },
  "components": {
    "messages": {
      "subscribe": {
        "name": "subscribe",
        "title": "subscribe",
        "payload": {
          "$ref": "#/components/schemas/SubscribeRequest"
        },
        "examples": [
          {
            "name": "batch",
            "summary": "Two channels in one frame",
            "payload": {
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
          },
          {
            "name": "singular",
            "summary": "One subscription",
            "payload": {
              "op": "subscribe",
              "channel": "price.crypto.twap",
              "filter": {
                "symbol": "btcusd",
                "window_seconds": 60
              }
            }
          },
          {
            "name": "pinned-provider",
            "summary": "One subscription pinned to a provider (spec 08b; ignored while the selector is disabled)",
            "payload": {
              "op": "subscribe",
              "channel": "price.equity",
              "filter": {
                "symbol": "xauusd",
                "provider": "pyth"
              },
              "rid": "s3"
            }
          }
        ]
      },
      "unsubscribe": {
        "name": "unsubscribe",
        "title": "unsubscribe",
        "payload": {
          "$ref": "#/components/schemas/UnsubscribeRequest"
        },
        "examples": [
          {
            "name": "singular",
            "payload": {
              "op": "unsubscribe",
              "channel": "price.crypto",
              "filter": {
                "symbol": "btcusd"
              }
            }
          }
        ]
      },
      "auth": {
        "name": "auth",
        "title": "auth",
        "payload": {
          "$ref": "#/components/schemas/AuthRequest"
        },
        "examples": [
          {
            "name": "clob-credentials",
            "summary": "CLOB API credentials (third-party clients)",
            "payload": {
              "op": "auth",
              "rid": "a1",
              "auth": {
                "apiKey": "00000000-0000-4000-8000-000000000000",
                "secret": "<api secret>",
                "passphrase": "<api passphrase>"
              }
            }
          },
          {
            "name": "clob-credentials-chainlink-key",
            "summary": "CLOB API credentials with a Chainlink API key (third-party clients)",
            "payload": {
              "op": "auth",
              "rid": "a4",
              "auth": {
                "apiKey": "00000000-0000-4000-8000-000000000000",
                "secret": "<api secret>",
                "passphrase": "<api passphrase>"
              },
              "chainlink_api_key": "<chainlink api key>"
            }
          },
          {
            "name": "access-token",
            "summary": "Identity Provider Access Token (third-party clients)",
            "payload": {
              "op": "auth",
              "rid": "a3",
              "auth": {
                "accessToken": "<access token>"
              }
            }
          },
          {
            "name": "web-app-ticket",
            "summary": "One-time ticket (the Polymarket web app)",
            "payload": {
              "op": "auth",
              "rid": "a2",
              "ticket": "5c1d2e3f-4a5b-4c6d-8e9f-0a1b2c3d4e5f"
            }
          }
        ]
      },
      "ping": {
        "name": "ping",
        "title": "ping",
        "payload": {
          "$ref": "#/components/schemas/PingRequest"
        },
        "examples": [
          {
            "name": "ping",
            "payload": {
              "op": "ping",
              "rid": "p1"
            }
          }
        ]
      },
      "subscribed": {
        "name": "subscribed",
        "title": "subscribed",
        "payload": {
          "$ref": "#/components/schemas/ChannelAck"
        },
        "examples": [
          {
            "name": "subscribed",
            "payload": {
              "op": "subscribed",
              "channel": "price.crypto",
              "rid": "s1"
            }
          },
          {
            "name": "subscribed-with-provider",
            "summary": "Provider selector enabled: the ack names the SERVED provider",
            "payload": {
              "op": "subscribed",
              "channel": "price.equity",
              "rid": "s2",
              "provider": "chainlink"
            }
          }
        ]
      },
      "unsubscribed": {
        "name": "unsubscribed",
        "title": "unsubscribed",
        "payload": {
          "$ref": "#/components/schemas/ChannelAck"
        },
        "examples": [
          {
            "name": "unsubscribed",
            "payload": {
              "op": "unsubscribed",
              "channel": "price.crypto"
            }
          }
        ]
      },
      "authed": {
        "name": "authed",
        "title": "authed",
        "payload": {
          "$ref": "#/components/schemas/SimpleAck"
        },
        "examples": [
          {
            "name": "authed",
            "payload": {
              "op": "authed",
              "rid": "a1"
            }
          }
        ]
      },
      "pong": {
        "name": "pong",
        "title": "pong",
        "payload": {
          "$ref": "#/components/schemas/SimpleAck"
        },
        "examples": [
          {
            "name": "pong",
            "payload": {
              "op": "pong",
              "rid": "p1"
            }
          }
        ]
      },
      "error": {
        "name": "error",
        "title": "error",
        "payload": {
          "$ref": "#/components/schemas/ErrorAck"
        },
        "examples": [
          {
            "name": "auth_required",
            "summary": "Gated channel subscribed before auth; the connection stays open",
            "payload": {
              "op": "error",
              "code": "auth_required",
              "channel": "price.crypto",
              "rid": "s1"
            }
          },
          {
            "name": "bad_filter",
            "payload": {
              "op": "error",
              "code": "bad_filter",
              "channel": "price.polymarket",
              "rid": "s2"
            }
          },
          {
            "name": "chainlink_key_required",
            "summary": "Chainlink-served subscription without a Chainlink API key; the connection stays open",
            "payload": {
              "op": "error",
              "code": "chainlink_key_required",
              "channel": "price.crypto",
              "rid": "s3"
            }
          }
        ]
      },
      "pricePolymarket": {
        "name": "price.polymarket",
        "title": "price.polymarket envelope",
        "payload": {
          "$ref": "#/components/schemas/PricePolymarketEnvelope"
        },
        "examples": [
          {
            "name": "snapshot",
            "payload": {
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
          },
          {
            "name": "cold snapshot",
            "summary": "Token with no trade inside the warm window",
            "payload": {
              "v": 1,
              "channel": "price.polymarket",
              "seq": 1,
              "ts": 1788973000123,
              "snapshot": true,
              "payload": []
            }
          },
          {
            "name": "live",
            "payload": {
              "v": 1,
              "channel": "price.polymarket",
              "seq": 2,
              "ts": 1788973004501,
              "payload": {
                "market": "0x9deb0baac40648821f96f01339229a422e2f5c877de55dc4dbf981f95a1e709c",
                "asset_id": "21742633143463906290569050155826241533067272736897614950488156847949938836455",
                "best_bid": "0.52",
                "best_ask": "0.53",
                "hash": "a81d02c4",
                "timestamp": 1788973004498
              }
            }
          }
        ]
      },
      "priceCrypto": {
        "name": "price.crypto",
        "title": "price.crypto envelope",
        "payload": {
          "$ref": "#/components/schemas/PriceCryptoEnvelope"
        },
        "examples": [
          {
            "name": "snapshot",
            "payload": {
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
          },
          {
            "name": "live",
            "payload": {
              "v": 1,
              "channel": "price.crypto",
              "seq": 2,
              "ts": 1788973001000,
              "payload": {
                "symbol": "btcusd",
                "value": 64126.0,
                "full_accuracy_value": "64126.00000000",
                "timestamp": 1788973001000,
                "source": "pyth"
              }
            }
          }
        ]
      },
      "priceEquity": {
        "name": "price.equity",
        "title": "price.equity envelope",
        "payload": {
          "$ref": "#/components/schemas/PriceEquityEnvelope"
        },
        "examples": [
          {
            "name": "live",
            "payload": {
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
          },
          {
            "name": "status change",
            "payload": {
              "v": 1,
              "channel": "price.equity",
              "seq": 6,
              "ts": 1788973001200,
              "payload": {
                "symbol": "xauusd",
                "value": 4012.35,
                "full_accuracy_value": "4012.35",
                "timestamp": 1788973001200,
                "received_at": 1788976800000,
                "is_carried_forward": true,
                "market_status": "closed",
                "source": "chainlink"
              }
            }
          }
        ]
      },
      "priceCryptoTwap": {
        "name": "price.crypto.twap",
        "title": "price.crypto.twap envelope",
        "payload": {
          "$ref": "#/components/schemas/PriceCryptoTwapEnvelope"
        },
        "examples": [
          {
            "name": "live",
            "payload": {
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
          }
        ]
      },
      "priceEquityTwap": {
        "name": "price.equity.twap",
        "title": "price.equity.twap envelope",
        "payload": {
          "$ref": "#/components/schemas/PriceEquityTwapEnvelope"
        },
        "examples": [
          {
            "name": "live",
            "payload": {
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
          }
        ]
      },
      "esportsSeries": {
        "name": "esports.series",
        "title": "esports.series envelope",
        "payload": {
          "$ref": "#/components/schemas/EsportsSeriesEnvelope"
        },
        "examples": [
          {
            "name": "live",
            "payload": {
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
          },
          {
            "name": "unbound-snapshot",
            "payload": {
              "v": 1,
              "channel": "esports.series",
              "seq": 1,
              "ts": 1790000000000,
              "snapshot": true,
              "payload": null
            }
          }
        ]
      },
      "challenge": {
        "name": "challenge",
        "title": "challenge",
        "summary": "This connection's challenge nonce, the answer to a challenge request; never pushed unasked",
        "payload": {
          "$ref": "#/components/schemas/ChallengeAck"
        },
        "examples": [
          {
            "name": "answer",
            "summary": "Answer to a challenge request; the same nonce for the life of the connection, rid echoed",
            "payload": {
              "op": "challenge",
              "nonce": "3f2b6c1e-9a4d-4c2b-8e1f-0a1b2c3d4e5f",
              "rid": "c1"
            }
          }
        ]
      },
      "challengeRequest": {
        "name": "challengeRequest",
        "title": "challenge (request)",
        "summary": "Ask for this connection's challenge nonce",
        "payload": {
          "$ref": "#/components/schemas/ChallengeRequest"
        },
        "examples": [
          {
            "name": "request",
            "payload": {
              "op": "challenge",
              "rid": "c1"
            }
          }
        ]
      }
    },
    "schemas": {
      "SubscriptionItem": {
        "type": "object",
        "required": [
          "channel",
          "filter"
        ],
        "properties": {
          "channel": {
            "type": "string",
            "enum": [
              "price.polymarket",
              "price.crypto",
              "price.equity",
              "price.crypto.twap",
              "price.equity.twap",
              "esports.series"
            ]
          },
          "filter": {
            "oneOf": [
              {
                "$ref": "#/components/schemas/AssetIdFilter"
              },
              {
                "$ref": "#/components/schemas/SymbolFilter"
              },
              {
                "$ref": "#/components/schemas/TwapFilter"
              },
              {
                "$ref": "#/components/schemas/EventIdFilter"
              }
            ]
          }
        }
      },
      "AssetIdFilter": {
        "type": "object",
        "required": [
          "asset_id"
        ],
        "properties": {
          "asset_id": {
            "type": "string",
            "pattern": "^[0-9]{1,78}$",
            "description": "Outcome token id (clobTokenIds entry), decimal string. Leading zeros are normalized."
          }
        }
      },
      "SymbolFilter": {
        "type": "object",
        "required": [
          "symbol"
        ],
        "properties": {
          "symbol": {
            "type": "string",
            "description": "Lowercase symbol. Matching is case-insensitive."
          },
          "provider": {
            "type": "string",
            "enum": [
              "chainlink",
              "pyth",
              "binance"
            ],
            "description": "Provider pin (spec 08b; binance added by spec 09). While the server's provider selector is DISABLED (PRICE_PROVIDER_SELECTOR_ENABLED=false, the default), this field is accepted and IGNORED like any unknown key: the lane's owner is served and the subscribed ack carries no provider. While it is ENABLED, the value must be one of the enum tokens; anything else (including massive, owner, numbers, null) is a bad_filter error ack. A pin the catalog serves gets that provider's stream; a pin it cannot serve falls back to the owner's stream, and the subscribed ack names the provider actually served. binance is price.crypto-only on the SERVING side: the token parses on every vendor channel, but only a price.crypto symbol whose operator config names binance can serve it - everywhere else (price.equity included) a binance pin always falls back to the owner. Ignored on price.polymarket. Required wherever the deployment enforces the provider pin (spec 13: staging and production from 2026-11-30 00:00 UTC), on every connection: a subscription without it answers provider_required (status 4011). Chainlink requires its own API key from every subscriber, so the server no longer picks a provider for the client."
          }
        }
      },
      "TwapFilter": {
        "type": "object",
        "required": [
          "symbol",
          "window_seconds"
        ],
        "properties": {
          "symbol": {
            "type": "string"
          },
          "window_seconds": {
            "type": "integer",
            "minimum": 1,
            "description": "Only 60 carries data today, on price.crypto.twap and price.equity.twap alike."
          },
          "provider": {
            "type": "string",
            "enum": [
              "chainlink",
              "pyth",
              "binance"
            ],
            "description": "Provider pin (spec 08b; binance added by spec 09). While the server's provider selector is DISABLED (PRICE_PROVIDER_SELECTOR_ENABLED=false, the default), this field is accepted and IGNORED like any unknown key: the lane's owner is served and the subscribed ack carries no provider. While it is ENABLED, the value must be one of the enum tokens; anything else (including massive, owner, numbers, null) is a bad_filter error ack. A pin the catalog serves gets that provider's stream; a pin it cannot serve falls back to the owner's stream, and the subscribed ack names the provider actually served. binance is price.crypto-only on the SERVING side, and the TWAP channels are Chainlink-produced, so a binance pin here always falls back to the owner. Ignored on price.polymarket. Required wherever the deployment enforces the provider pin (spec 13: staging and production from 2026-11-30 00:00 UTC), on every connection: a subscription without it answers provider_required (status 4011). Chainlink requires its own API key from every subscriber, so the server no longer picks a provider for the client."
          }
        }
      },
      "EventIdFilter": {
        "type": "object",
        "required": [
          "event_id"
        ],
        "properties": {
          "event_id": {
            "type": "string",
            "pattern": "^[1-9][0-9]{0,9}$",
            "description": "Gamma event id, canonical decimal string. A number or a non-canonical string is a bad_filter error ack."
          },
          "provider": {
            "type": "string",
            "enum": [
              "grid",
              "pandascore"
            ],
            "description": "Optional provider pin. While the server's esports provider selector is DISABLED (ESPORTS_PROVIDER_SELECTOR_ENABLED=false, the default), this field is accepted and IGNORED like any unknown key and the default rule serves. While it is ENABLED, the value must be one of the enum tokens; anything else (including numbers, null) is a bad_filter error ack, and a pin serves only that provider's document (no fallback; snapshot null while it holds none). Default rule (no pin, or selector disabled): the title's configured owner (GRID unless configured otherwise), or the other provider's document while the owner holds none for the event. When the served provider changes, the next frame carries snapshot:true and the full document of the new provider; documents of two providers never interleave without one. The document's source field names its provider. A connection holding both an unpinned and a pinned subscription for one event receives both streams on this channel; demultiplex by the payload source field (the never-interleave rule is per subscription)."
          }
        }
      },
      "SubscribeRequest": {
        "oneOf": [
          {
            "type": "object",
            "required": [
              "op",
              "subscriptions"
            ],
            "properties": {
              "op": {
                "const": "subscribe"
              },
              "subscriptions": {
                "type": "array",
                "minItems": 1,
                "items": {
                  "$ref": "#/components/schemas/SubscriptionItem"
                }
              },
              "rid": {
                "type": "string",
                "description": "Client request id, echoed on every ack this frame produces."
              }
            }
          },
          {
            "type": "object",
            "required": [
              "op",
              "channel",
              "filter"
            ],
            "properties": {
              "op": {
                "const": "subscribe"
              },
              "channel": {
                "type": "string"
              },
              "filter": {
                "type": "object"
              },
              "rid": {
                "type": "string"
              }
            }
          }
        ]
      },
      "UnsubscribeRequest": {
        "oneOf": [
          {
            "type": "object",
            "required": [
              "op",
              "subscriptions"
            ],
            "properties": {
              "op": {
                "const": "unsubscribe"
              },
              "subscriptions": {
                "type": "array",
                "minItems": 1,
                "items": {
                  "$ref": "#/components/schemas/SubscriptionItem"
                }
              },
              "rid": {
                "type": "string"
              }
            }
          },
          {
            "type": "object",
            "required": [
              "op",
              "channel",
              "filter"
            ],
            "properties": {
              "op": {
                "const": "unsubscribe"
              },
              "channel": {
                "type": "string"
              },
              "filter": {
                "type": "object"
              },
              "rid": {
                "type": "string"
              }
            }
          }
        ]
      },
      "AuthRequest": {
        "type": "object",
        "required": [
          "op"
        ],
        "properties": {
          "op": {
            "const": "auth"
          },
          "auth": {
            "oneOf": [
              {
                "$ref": "#/components/schemas/ClobCredentials"
              },
              {
                "$ref": "#/components/schemas/AccessTokenCredential"
              }
            ],
            "description": "CLOB API credentials or an Identity Provider Access Token, never both in one object. An object that mixes the two, or an incomplete set of CLOB credentials, answers the non-closing bad_op."
          },
          "chainlink_api_key": {
            "type": "string",
            "minLength": 1,
            "maxLength": 512,
            "pattern": "^[!-~]+$",
            "description": "Optional Chainlink API key, next to an auth credential (also accepted as chainlinkApiKey; both spellings in one frame answer bad_op). Not a credential: a frame with only the key answers bad_op. Recorded when the auth is accepted with CLOB API credentials or a verified Access Token (never a visitor token, nor an Access Token whose client_id is polymarket-web), and asked for by Chainlink-served price subscriptions on that connection (price.crypto and price.equity symbols Chainlink serves, both TWAP channels). Without it, such a subscription answers the non-closing chainlink_key_required once the deployment enforces the key; until then it is admitted. A key outside this shape, or of another JSON type, is ignored and the credential is still handled. Send it on the first auth frame: the key cannot be added or changed on an authenticated connection, except on a verified Access Token renewal. The Polymarket web app is never asked: neither its ticket and visitor tokens nor its logged-in Access Tokens (client_id polymarket-web)."
          },
          "rid": {
            "type": "string"
          },
          "ticket": {
            "type": "string",
            "maxLength": 128,
            "description": "The one-time ticket from POST /api/ws-ticket (the Polymarket web app's credential), consumed by the attempt whatever the outcome. Minted from a Cloudflare Turnstile solve; when the widget was rendered with this connection's challenge nonce as cData, the ticket verifies only on this socket, whatever IP either request came from. A stale, consumed or unknown ticket, or one minted for another socket, answers the non-closing auth_expired: mint again."
          }
        },
        "oneOf": [
          {
            "required": [
              "auth"
            ]
          },
          {
            "required": [
              "ticket"
            ]
          }
        ],
        "description": "Exactly one credential per frame: auth (CLOB API credentials or an Identity Provider Access Token, third-party clients) or ticket (the web app). Zero or two answer the non-closing bad_op."
      },
      "ClobCredentials": {
        "type": "object",
        "required": [
          "apiKey",
          "secret",
          "passphrase"
        ],
        "properties": {
          "apiKey": {
            "type": "string"
          },
          "secret": {
            "type": "string"
          },
          "passphrase": {
            "type": "string"
          }
        },
        "not": {
          "required": [
            "accessToken"
          ]
        },
        "description": "The CLOB L2 API credential trio, the same credentials used for the CLOB user WebSocket. Never combined with accessToken in one object: the server answers bad_op."
      },
      "AccessTokenCredential": {
        "type": "object",
        "required": [
          "accessToken"
        ],
        "properties": {
          "accessToken": {
            "type": "string",
            "maxLength": 4096,
            "description": "An Identity Provider Access Token (third-party clients), or a visitor token (logged-out polymarket.com browsers). Verified locally: RS256 under a key of the identity JWKS, the environment's issuer and audience, not expired. The signed header typ picks the profile: at+jwt is an Access Token; visitor+jwt is a visitor token, which must carry sub visitor:<UUID> and client_id polymarket-web, binds no signer and opens the same channels as a web-app ticket. A refused or expired token answers the non-closing auth_invalid; a pod that holds no identity keys answers auth_unavailable (retry later)."
          }
        },
        "not": {
          "anyOf": [
            {
              "required": [
                "apiKey"
              ]
            },
            {
              "required": [
                "secret"
              ]
            },
            {
              "required": [
                "passphrase"
              ]
            }
          ]
        },
        "description": "An Identity Provider Access Token. Never combined with apiKey, secret or passphrase in one object: the server answers bad_op."
      },
      "PingRequest": {
        "type": "object",
        "required": [
          "op"
        ],
        "properties": {
          "op": {
            "const": "ping"
          },
          "rid": {
            "type": "string"
          }
        }
      },
      "ChannelAck": {
        "type": "object",
        "required": [
          "op",
          "channel"
        ],
        "properties": {
          "op": {
            "type": "string",
            "enum": [
              "subscribed",
              "unsubscribed"
            ]
          },
          "channel": {
            "type": "string"
          },
          "rid": {
            "type": "string"
          },
          "provider": {
            "type": "string",
            "enum": [
              "pyth",
              "massive",
              "chainlink",
              "binance",
              "grid",
              "pandascore"
            ],
            "description": "subscribed acks only, and only while the channel's provider selector is enabled. esports.series (ESPORTS_PROVIDER_SELECTOR_ENABLED): grid|pandascore, the pin, or without a pin the provider served at subscribe time (absent while the event has no document; later switches arrive as snapshot:true frames). Vendor channels (spec 08b): the provider actually SERVED - the requested pin when the catalog serves it, else the lane's owner (massive is reachable on the omitted path only). binance (spec 09) can be SERVED only on price.crypto - on every other vendor channel a binance pin's ack names the owner it fell back to. Also present on the idempotent duplicate-subscribe ack. Absent everywhere else, including every ack while the selector is disabled."
          }
        }
      },
      "SimpleAck": {
        "type": "object",
        "required": [
          "op"
        ],
        "properties": {
          "op": {
            "type": "string",
            "enum": [
              "authed",
              "pong"
            ]
          },
          "rid": {
            "type": "string"
          }
        }
      },
      "ErrorAck": {
        "type": "object",
        "required": [
          "op",
          "code"
        ],
        "properties": {
          "op": {
            "const": "error"
          },
          "code": {
            "type": "string",
            "enum": [
              "bad_op",
              "bad_channel",
              "bad_filter",
              "sub_limit",
              "rate_limited",
              "auth_required",
              "auth_expired",
              "auth_unavailable",
              "auth_invalid",
              "auth_attempts",
              "chainlink_key_required",
              "provider_required"
            ],
            "description": "bad_op malformed frame; bad_channel unknown channel; bad_filter missing or invalid filter; sub_limit 65th subscription (followed by close 4008); rate_limited more than 20 subscribe/unsubscribe frames per second (followed by close 4008); auth_required gated channel before auth; auth_expired consumed or unknown ticket (web app lane); auth_unavailable verifier unreachable, retry later; auth_invalid credentials refused; auth_attempts ninth auth frame (followed by close 4008); chainlink_key_required Chainlink-served price subscription on a connection authenticated with CLOB API credentials or a verified Access Token whose auth carried no chainlink_api_key (only where the deployment enforces the key; the connection stays open; status 4010); provider_required price.crypto, price.equity or TWAP subscription whose filter named no provider (only where the deployment enforces the provider pin, on every connection; the connection stays open; status 4011)."
          },
          "channel": {
            "type": "string"
          },
          "rid": {
            "type": "string"
          },
          "status": {
            "type": "integer",
            "enum": [
              4010,
              4011
            ],
            "description": "A numeric status next to code, on the two price-licensing refusals only: 4010 chainlink_key_required, 4011 provider_required. It shares the 4xxx range with the close codes but closes nothing: the refused item never registers and the connection stays open. Absent on every other error."
          }
        }
      },
      "BestBidAsk": {
        "type": "object",
        "required": [
          "market",
          "asset_id",
          "best_bid",
          "best_ask",
          "hash",
          "timestamp"
        ],
        "properties": {
          "market": {
            "type": "string",
            "description": "Condition id, 0x-prefixed."
          },
          "asset_id": {
            "type": "string",
            "description": "Outcome token id, decimal string."
          },
          "best_bid": {
            "type": "string",
            "description": "Decimal string price."
          },
          "best_ask": {
            "type": "string",
            "description": "Decimal string price."
          },
          "hash": {
            "type": "string",
            "description": "Order book hash at this change."
          },
          "timestamp": {
            "type": "integer",
            "description": "Order book time, Unix milliseconds."
          }
        }
      },
      "BatchPoint": {
        "type": "object",
        "required": [
          "value",
          "full_accuracy_value",
          "timestamp"
        ],
        "properties": {
          "value": {
            "type": "number",
            "description": "Price as a float. Prefer full_accuracy_value."
          },
          "full_accuracy_value": {
            "type": "string",
            "description": "Exact decimal price as published by the source."
          },
          "timestamp": {
            "type": "integer",
            "description": "Source event time, Unix milliseconds."
          }
        },
        "description": "One historical point of a snapshot batch. Batch points carry NO symbol and NO source: both live once at batch level (the batch object's own fields), matching what the server actually emits - the retired shared point schema wrongly REQUIRED a symbol on every point."
      },
      "CryptoPoint": {
        "type": "object",
        "required": [
          "symbol",
          "value",
          "full_accuracy_value",
          "timestamp",
          "source"
        ],
        "properties": {
          "symbol": {
            "type": "string",
            "description": "Lowercase symbol, for example btcusd."
          },
          "value": {
            "type": "number",
            "description": "Price as a float. Prefer full_accuracy_value."
          },
          "full_accuracy_value": {
            "type": "string",
            "description": "Exact decimal price as published by the source."
          },
          "timestamp": {
            "type": "integer",
            "description": "Source event time, Unix milliseconds."
          },
          "source": {
            "type": "string",
            "enum": [
              "pyth",
              "chainlink",
              "binance"
            ],
            "description": "Vendor that produced this price, on every point this server emits. A per-symbol ownership flip rolls the edge fleet, so mid-roll a symbol's consecutive frames can legitimately carry different sources until the roll completes. A binance value (spec 09) is the Binance USDT-quoted close relayed verbatim under the usd-named symbol (no conversion leg): bps-scale delta against pyth/chainlink normally, percent-scale in a USDT depeg - exactly when comparisons are most likely."
          }
        }
      },
      "EquityPoint": {
        "type": "object",
        "required": [
          "symbol",
          "value",
          "full_accuracy_value",
          "timestamp",
          "source"
        ],
        "properties": {
          "symbol": {
            "type": "string",
            "description": "Lowercase symbol, for example btcusd or aapl."
          },
          "value": {
            "type": "number",
            "description": "Price as a float. Prefer full_accuracy_value."
          },
          "full_accuracy_value": {
            "type": "string",
            "description": "Exact decimal price as published by the source."
          },
          "timestamp": {
            "type": "integer",
            "description": "Source event time, Unix milliseconds."
          },
          "source": {
            "type": "string",
            "enum": [
              "pyth",
              "massive",
              "chainlink"
            ],
            "description": "Vendor that produced this price, on every point this server emits. A per-symbol ownership flip rolls the edge fleet, so mid-roll a symbol's consecutive frames can legitimately carry different sources until the roll completes."
          },
          "received_at": {
            "type": "integer",
            "description": "Ingest receive time, Unix milliseconds. Live frames only."
          },
          "is_carried_forward": {
            "type": "boolean",
            "description": "True when the frame repeats an already-measured price instead of carrying a new one: the upstream redelivered its last measurement (for example a closed session), or the frame is a status change repeating the last price. Live frames only."
          },
          "market_status": {
            "type": "string",
            "enum": [
              "open",
              "closed",
              "unknown"
            ],
            "description": "State of the market of the instrument this series prices, as its producer states it: open, closed, or unknown (the vendor reported it cannot determine it). Absent means not stated, never open. It describes each provider's own instrument: a continuous-hours product (the Chainlink 24/7 streams) reads open outside exchange sessions while an exchange-session feed of the same ticker reads closed, and both are truthful. Every frame renders the series' current status. A status change that repeats the last price arrives as a frame carrying that price (its timestamp unchanged), is_carried_forward true and the new market_status: it is not a duplicate, so never dedup on timestamp alone."
          }
        }
      },
      "TwapPoint": {
        "type": "object",
        "required": [
          "symbol",
          "value",
          "full_accuracy_value",
          "timestamp",
          "window_seconds",
          "source"
        ],
        "properties": {
          "symbol": {
            "type": "string",
            "description": "Lowercase symbol, for example btcusd."
          },
          "value": {
            "type": "number",
            "description": "Price as a float. Prefer full_accuracy_value."
          },
          "full_accuracy_value": {
            "type": "string",
            "description": "Exact decimal price as published by the source."
          },
          "timestamp": {
            "type": "integer",
            "description": "Source event time, Unix milliseconds."
          },
          "window_seconds": {
            "type": "integer",
            "const": 60,
            "description": "Averaging window of the TWAP series. Only 60 exists today."
          },
          "source": {
            "type": "string",
            "enum": [
              "chainlink"
            ],
            "description": "The producing vendor. price.crypto.twap is a single-provider lane, so the value is the topic constant."
          }
        }
      },
      "EquityTwapPoint": {
        "type": "object",
        "required": [
          "symbol",
          "value",
          "full_accuracy_value",
          "timestamp",
          "window_seconds",
          "source"
        ],
        "properties": {
          "symbol": {
            "type": "string",
            "description": "Lowercase symbol, for example eurusd."
          },
          "value": {
            "type": "number",
            "description": "Price as a float. Prefer full_accuracy_value."
          },
          "full_accuracy_value": {
            "type": "string",
            "description": "Exact decimal price as published by the source."
          },
          "timestamp": {
            "type": "integer",
            "description": "Source event time, Unix milliseconds."
          },
          "window_seconds": {
            "type": "integer",
            "const": 60,
            "description": "Averaging window of the TWAP series. Only 60 exists today."
          },
          "source": {
            "type": "string",
            "enum": [
              "pyth",
              "massive",
              "chainlink"
            ],
            "description": "Vendor that produced this price, on every point this server emits. The channel is Chainlink-only today, so the emitted value is chainlink. Kept as its own schema because this enum is the full vendor set while TwapPoint pins its topic constant."
          },
          "market_status": {
            "type": "string",
            "enum": [
              "open",
              "closed",
              "unknown"
            ],
            "description": "State of the market of the instrument this series prices, as its producer states it; same meaning as on price.equity. Absent means not stated. On this channel it changes only with a new price (a TWAP has one clock). The Chainlink FX TWAPs are continuous-hours products and read open."
          }
        }
      },
      "PricePolymarketEnvelope": {
        "type": "object",
        "required": [
          "v",
          "channel",
          "seq",
          "ts",
          "payload"
        ],
        "properties": {
          "v": {
            "type": "integer",
            "const": 1,
            "description": "Envelope version."
          },
          "channel": {
            "type": "string",
            "const": "price.polymarket"
          },
          "seq": {
            "type": "integer",
            "description": "Dense per-connection, per-channel sequence, assigned at delivery. Resets on every reconnect. Snapshot frames consume a seq."
          },
          "ts": {
            "type": "integer",
            "description": "Producer event time, Unix milliseconds."
          },
          "snapshot": {
            "type": "boolean",
            "description": "Present and true on the one snapshot frame sent after each new subscription. Absent on live frames."
          },
          "dropped": {
            "type": "integer",
            "description": "Number of frames dropped on this channel since the last delivered frame (slow-consumer signal). Absent when zero."
          },
          "payload": {
            "$ref": "#/components/schemas/PricePolymarketPayload"
          }
        },
        "description": "Snapshot payload is a BestBidAsk object or an empty array; live payload is a BestBidAsk object."
      },
      "PricePolymarketPayload": {
        "oneOf": [
          {
            "$ref": "#/components/schemas/BestBidAsk"
          },
          {
            "type": "array",
            "maxItems": 0,
            "description": "Empty snapshot for a cold token."
          }
        ]
      },
      "PriceCryptoEnvelope": {
        "type": "object",
        "required": [
          "v",
          "channel",
          "seq",
          "ts",
          "payload"
        ],
        "properties": {
          "v": {
            "type": "integer",
            "const": 1,
            "description": "Envelope version."
          },
          "channel": {
            "type": "string",
            "const": "price.crypto"
          },
          "seq": {
            "type": "integer",
            "description": "Dense per-connection, per-channel sequence, assigned at delivery. Resets on every reconnect. Snapshot frames consume a seq."
          },
          "ts": {
            "type": "integer",
            "description": "Producer event time, Unix milliseconds."
          },
          "snapshot": {
            "type": "boolean",
            "description": "Present and true on the one snapshot frame sent after each new subscription. Absent on live frames."
          },
          "dropped": {
            "type": "integer",
            "description": "Number of frames dropped on this channel since the last delivered frame (slow-consumer signal). Absent when zero."
          },
          "payload": {
            "$ref": "#/components/schemas/PriceCryptoPayload"
          }
        },
        "description": "Snapshot payload is a symbol batch; live payload is a single point."
      },
      "PriceCryptoPayload": {
        "oneOf": [
          {
            "$ref": "#/components/schemas/CryptoPoint"
          },
          {
            "type": "object",
            "required": [
              "symbol",
              "source",
              "data"
            ],
            "properties": {
              "symbol": {
                "type": "string"
              },
              "source": {
                "type": "string",
                "enum": [
                  "pyth",
                  "chainlink",
                  "binance"
                ],
                "description": "Vendor that produced every point in this batch, once at batch level (points are source-free): symbol ownership is fixed for the life of a pod, so one series never mixes vendors. After a reconnect during an ownership flip, the batch can carry a different source than the previous connection's frames. A binance batch (spec 09) is the Binance USDT-quoted close relayed verbatim under the usd-named symbol: bps-scale delta against pyth/chainlink normally, percent-scale in a USDT depeg."
              },
              "data": {
                "type": "array",
                "items": {
                  "$ref": "#/components/schemas/BatchPoint"
                },
                "description": "The array holds the previous two minutes of points by event time and is empty for a symbol with no recent data."
              }
            }
          }
        ]
      },
      "PriceEquityEnvelope": {
        "type": "object",
        "required": [
          "v",
          "channel",
          "seq",
          "ts",
          "payload"
        ],
        "properties": {
          "v": {
            "type": "integer",
            "const": 1,
            "description": "Envelope version."
          },
          "channel": {
            "type": "string",
            "const": "price.equity"
          },
          "seq": {
            "type": "integer",
            "description": "Dense per-connection, per-channel sequence, assigned at delivery. Resets on every reconnect. Snapshot frames consume a seq."
          },
          "ts": {
            "type": "integer",
            "description": "Producer event time, Unix milliseconds."
          },
          "snapshot": {
            "type": "boolean",
            "description": "Present and true on the one snapshot frame sent after each new subscription. Absent on live frames."
          },
          "dropped": {
            "type": "integer",
            "description": "Number of frames dropped on this channel since the last delivered frame (slow-consumer signal). Absent when zero."
          },
          "payload": {
            "$ref": "#/components/schemas/PriceEquityPayload"
          }
        },
        "description": "Snapshot payload is a symbol batch; live payload is a single point."
      },
      "PriceEquityPayload": {
        "oneOf": [
          {
            "$ref": "#/components/schemas/EquityPoint"
          },
          {
            "type": "object",
            "required": [
              "symbol",
              "source",
              "data"
            ],
            "properties": {
              "symbol": {
                "type": "string"
              },
              "source": {
                "type": "string",
                "enum": [
                  "pyth",
                  "massive",
                  "chainlink"
                ],
                "description": "Vendor that produced every point in this batch, once at batch level: symbol ownership is fixed for the life of a pod, so one series never mixes vendors. After a reconnect during an ownership flip, the batch can carry a different source than the previous connection's frames."
              },
              "market_status": {
                "type": "string",
                "enum": [
                  "open",
                  "closed",
                  "unknown"
                ],
                "description": "The series' current market status, once at batch level like source; absent when not stated. While it is closed or unknown, data also carries the series' last price point when that point is older than the two-minute window (the price the market stopped at), and the envelope ts is then that point's time."
              },
              "data": {
                "type": "array",
                "items": {
                  "$ref": "#/components/schemas/BatchPoint"
                },
                "description": "The array holds the previous two minutes of points by event time and is empty for a symbol with no recent data, except while market_status is closed or unknown: then it also holds the series' last point when that point is older than the window."
              }
            }
          }
        ]
      },
      "PriceCryptoTwapEnvelope": {
        "type": "object",
        "required": [
          "v",
          "channel",
          "seq",
          "ts",
          "payload"
        ],
        "properties": {
          "v": {
            "type": "integer",
            "const": 1,
            "description": "Envelope version."
          },
          "channel": {
            "type": "string",
            "const": "price.crypto.twap"
          },
          "seq": {
            "type": "integer",
            "description": "Dense per-connection, per-channel sequence, assigned at delivery. Resets on every reconnect. Snapshot frames consume a seq."
          },
          "ts": {
            "type": "integer",
            "description": "Producer event time, Unix milliseconds."
          },
          "snapshot": {
            "type": "boolean",
            "description": "Present and true on the one snapshot frame sent after each new subscription. Absent on live frames."
          },
          "dropped": {
            "type": "integer",
            "description": "Number of frames dropped on this channel since the last delivered frame (slow-consumer signal). Absent when zero."
          },
          "payload": {
            "$ref": "#/components/schemas/PriceCryptoTwapPayload"
          }
        },
        "description": "Snapshot payload is a symbol batch carrying window_seconds; live payload is a single point carrying window_seconds."
      },
      "PriceCryptoTwapPayload": {
        "oneOf": [
          {
            "$ref": "#/components/schemas/TwapPoint"
          },
          {
            "type": "object",
            "required": [
              "symbol",
              "data",
              "window_seconds",
              "source"
            ],
            "properties": {
              "symbol": {
                "type": "string"
              },
              "data": {
                "type": "array",
                "items": {
                  "$ref": "#/components/schemas/BatchPoint"
                },
                "description": "The array holds the previous two minutes of points by event time and is empty for a symbol with no recent data."
              },
              "window_seconds": {
                "type": "integer",
                "const": 60
              },
              "source": {
                "type": "string",
                "enum": [
                  "chainlink"
                ],
                "description": "The producing vendor, once per batch (points are source-free). Topic constant on this single-provider lane."
              }
            }
          }
        ]
      },
      "PriceEquityTwapEnvelope": {
        "type": "object",
        "required": [
          "v",
          "channel",
          "seq",
          "ts",
          "payload"
        ],
        "properties": {
          "v": {
            "type": "integer",
            "const": 1,
            "description": "Envelope version."
          },
          "channel": {
            "type": "string",
            "const": "price.equity.twap"
          },
          "seq": {
            "type": "integer",
            "description": "Dense per-connection, per-channel sequence, assigned at delivery. Resets on every reconnect. Snapshot frames consume a seq."
          },
          "ts": {
            "type": "integer",
            "description": "Producer event time, Unix milliseconds."
          },
          "snapshot": {
            "type": "boolean",
            "description": "Present and true on the one snapshot frame sent after each new subscription. Absent on live frames."
          },
          "dropped": {
            "type": "integer",
            "description": "Number of frames dropped on this channel since the last delivered frame (slow-consumer signal). Absent when zero."
          },
          "payload": {
            "$ref": "#/components/schemas/PriceEquityTwapPayload"
          }
        },
        "description": "Snapshot payload is a symbol batch carrying window_seconds; live payload is a single point carrying window_seconds."
      },
      "PriceEquityTwapPayload": {
        "oneOf": [
          {
            "$ref": "#/components/schemas/EquityTwapPoint"
          },
          {
            "type": "object",
            "required": [
              "symbol",
              "source",
              "data",
              "window_seconds"
            ],
            "properties": {
              "symbol": {
                "type": "string"
              },
              "source": {
                "type": "string",
                "enum": [
                  "pyth",
                  "massive",
                  "chainlink"
                ],
                "description": "Vendor that produced every point in this batch, once at batch level. The channel is Chainlink-only today, so the value is chainlink."
              },
              "market_status": {
                "type": "string",
                "enum": [
                  "open",
                  "closed",
                  "unknown"
                ],
                "description": "The series' current market status, once at batch level like source; absent when not stated. While it is closed or unknown, data also carries the series' last price point when that point is older than the two-minute window (the price the market stopped at), and the envelope ts is then that point's time."
              },
              "data": {
                "type": "array",
                "items": {
                  "$ref": "#/components/schemas/BatchPoint"
                },
                "description": "The array holds the previous two minutes of points by event time and is empty for a symbol with no recent data, except while market_status is closed or unknown: then it also holds the series' last point when that point is older than the window."
              },
              "window_seconds": {
                "type": "integer",
                "const": 60
              }
            }
          }
        ]
      },
      "EsportsSeriesEnvelope": {
        "type": "object",
        "required": [
          "v",
          "channel",
          "seq",
          "ts",
          "payload"
        ],
        "properties": {
          "v": {
            "type": "integer",
            "const": 1,
            "description": "Envelope version."
          },
          "channel": {
            "type": "string",
            "const": "esports.series"
          },
          "seq": {
            "type": "integer",
            "description": "Dense per-connection, per-channel sequence, assigned at delivery. Resets on every reconnect. Snapshot frames consume a seq."
          },
          "ts": {
            "type": "integer",
            "description": "The document's observed_at_ms; now for a null snapshot."
          },
          "snapshot": {
            "type": "boolean",
            "description": "Present and true on the one snapshot frame sent after each new subscription. Absent on live frames."
          },
          "dropped": {
            "type": "integer",
            "description": "Number of frames dropped on this channel since the last delivered frame (slow-consumer signal). Absent when zero."
          },
          "payload": {
            "$ref": "#/components/schemas/EsportsSeriesPayload"
          }
        },
        "description": "Every frame carries the full document; replace, never merge."
      },
      "EsportsSeriesPayload": {
        "oneOf": [
          {
            "$ref": "#/components/schemas/EsportsSeriesDoc"
          },
          {
            "type": "null",
            "description": "Snapshot only: no live document for this event (unbound or not live)."
          }
        ]
      },
      "EsportsSeriesDoc": {
        "type": "object",
        "required": [
          "event_id",
          "title",
          "source",
          "provider_series_id",
          "schema_version",
          "binding_revision",
          "revision",
          "observed_at_ms",
          "phase",
          "invalidation_reason",
          "feed_status",
          "capabilities",
          "format",
          "best_of",
          "legacy_score",
          "period",
          "teams",
          "games",
          "recent_plays"
        ],
        "properties": {
          "event_id": {
            "type": "string",
            "description": "Gamma event id."
          },
          "title": {
            "type": "string",
            "enum": [
              "lol",
              "cs2",
              "dota2",
              "valorant",
              "r6siege",
              "mlbb"
            ]
          },
          "source": {
            "type": "string",
            "description": "Data provider.",
            "enum": [
              "grid",
              "pandascore"
            ]
          },
          "provider_series_id": {
            "type": "string",
            "description": "Support and tracing only; never key on it."
          },
          "schema_version": {
            "type": "integer"
          },
          "binding_revision": {
            "type": "integer",
            "description": "Rises when the event is rebound to another provider series."
          },
          "revision": {
            "type": "integer",
            "description": "Rises with every published change; never goes back."
          },
          "source_updated_at_ms": {
            "type": "integer",
            "description": "When the provider last changed the state. Absent when not reported."
          },
          "observed_at_ms": {
            "type": "integer",
            "description": "When the producer read this state plus its configurable publish delay: the document is the state as of that delay ago, except feed_status and any live field groups the producer enables (results: phase finished, series games_won/won, game finished/winner_team_id; kills: game team kills/deaths/first_kill), which are current. feed_status live can carry an old observed_at for up to the delay after an outage; judge freshness by observed_at. Freshness is now - observed_at_ms (not applicable once phase is finished); clocks anchor here."
          },
          "published_at_ms": {
            "type": "integer"
          },
          "phase": {
            "type": "string",
            "enum": [
              "upcoming",
              "live",
              "paused",
              "finished",
              "unspecified"
            ]
          },
          "valid": {
            "type": "boolean",
            "description": "False while the provider reports the state invalid; absent when not reported."
          },
          "invalidation_reason": {
            "type": "string"
          },
          "feed_status": {
            "type": "string",
            "description": "live, or delayed/recovering: the document is the last good state.",
            "enum": [
              "live",
              "delayed",
              "recovering",
              "unspecified"
            ]
          },
          "capabilities": {
            "type": "array",
            "items": {
              "type": "string",
              "enum": [
                "series",
                "games",
                "clock",
                "draft",
                "players",
                "objectives",
                "structures",
                "timers",
                "rounds",
                "economy",
                "plays"
              ]
            },
            "description": "The optional groups this document fills; an absent field or empty group means unknown, never zero."
          },
          "format": {
            "type": "string",
            "description": "e.g. best-of-3."
          },
          "best_of": {
            "type": "integer"
          },
          "current_game": {
            "type": "integer",
            "description": "Game in play, or next between games; the last game once finished; absent until the series starts."
          },
          "legacy_score": {
            "type": "string",
            "description": "Legacy card score string, home first, e.g. 21-6,10-11,missing|1-0|Bo3. Empty while either side is unresolved, the doc is invalid, or best-of is unknown."
          },
          "period": {
            "type": "string",
            "description": "Legacy period string: NS until a game starts, then <current_game>/<best_of>, e.g. 2/3. Empty if best-of is unknown. Gate on phase."
          },
          "teams": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/EsportsSeriesTeam"
            }
          },
          "games": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/EsportsGame"
            }
          },
          "recent_plays": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/EsportsPlay"
            },
            "description": "Last 20 plays across the series, newest last."
          }
        }
      },
      "EsportsClock": {
        "type": "object",
        "required": [
          "seconds",
          "ticking",
          "counts_down"
        ],
        "properties": {
          "seconds": {
            "type": "integer",
            "description": "Seconds on the clock at observed_at_ms. Advance from observed_at_ms only while ticking and the document is fresh."
          },
          "ticking": {
            "type": "boolean"
          },
          "counts_down": {
            "type": "boolean",
            "description": "True for a countdown (CS2 round, respawn); false for elapsed game time."
          }
        }
      },
      "EsportsSeriesTeam": {
        "type": "object",
        "required": [
          "id",
          "name",
          "polymarket_side",
          "games_won"
        ],
        "properties": {
          "id": {
            "type": "string",
            "description": "Provider team id; games[].teams[].team_id refers to it."
          },
          "name": {
            "type": "string"
          },
          "polymarket_side": {
            "type": "string",
            "description": "Side of the Polymarket event this team is on.",
            "enum": [
              "home",
              "away",
              "unspecified"
            ]
          },
          "games_won": {
            "type": "integer",
            "description": "Games (LoL) or maps (CS2) won."
          },
          "won": {
            "type": "boolean",
            "description": "Present once the series has a winner."
          }
        }
      },
      "EsportsGame": {
        "type": "object",
        "required": [
          "number",
          "map",
          "started",
          "finished",
          "paused",
          "winner_team_id",
          "teams",
          "draft",
          "structures",
          "timers",
          "rounds"
        ],
        "properties": {
          "number": {
            "type": "integer",
            "description": "Game number in the series."
          },
          "map": {
            "type": "string",
            "description": "Map name; for single-map titles the provider's (LoL: Summoner's Rift) or empty."
          },
          "started": {
            "type": "boolean"
          },
          "finished": {
            "type": "boolean"
          },
          "paused": {
            "type": "boolean"
          },
          "winner_team_id": {
            "type": "string",
            "description": "The provider's explicit winner; empty until there is one."
          },
          "clock": {
            "$ref": "#/components/schemas/EsportsClock"
          },
          "teams": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/EsportsGameTeam"
            }
          },
          "draft": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/EsportsDraftAction"
            }
          },
          "structures": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/EsportsStructure"
            }
          },
          "timers": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/EsportsTimer"
            }
          },
          "rounds": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/EsportsRound"
            }
          }
        },
        "description": "Exactly one game carries players, draft, structures, timers and rounds: current_game once the provider lists it, else the last game played (between games, after the finish), else game 1. Every other game is a summary."
      },
      "EsportsGameTeam": {
        "type": "object",
        "required": [
          "team_id",
          "side",
          "objectives",
          "players",
          "drakes"
        ],
        "properties": {
          "team_id": {
            "type": "string"
          },
          "side": {
            "type": "string",
            "description": "blue/red (LoL), terrorists/counter-terrorists (CS2), ..."
          },
          "kills": {
            "type": "integer",
            "description": "Kills; the per-game score in LoL."
          },
          "deaths": {
            "type": "integer"
          },
          "gold": {
            "type": "integer",
            "description": "Total gold earned (LoL)."
          },
          "gold_lead": {
            "type": "integer",
            "description": "This team's gold minus the opponent's."
          },
          "objectives": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/EsportsObjective"
            }
          },
          "baron_power_play": {
            "type": "integer"
          },
          "rounds_won": {
            "type": "integer",
            "description": "Rounds won; the per-map score in CS2."
          },
          "money": {
            "type": "integer"
          },
          "players": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/EsportsPlayer"
            }
          },
          "drakes": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "Elemental dragons in take order (objective variants); elder excluded."
          },
          "first_kill": {
            "type": "boolean",
            "description": "True when this team scored the game's first kill."
          }
        }
      },
      "EsportsPlayer": {
        "type": "object",
        "required": [
          "id",
          "name",
          "buffs",
          "loadout"
        ],
        "properties": {
          "id": {
            "type": "string"
          },
          "name": {
            "type": "string"
          },
          "character": {
            "type": "string",
            "description": "Champion, hero or agent; absent before it is picked."
          },
          "kills": {
            "type": "integer"
          },
          "deaths": {
            "type": "integer"
          },
          "assists": {
            "type": "integer"
          },
          "alive": {
            "type": "boolean"
          },
          "gold": {
            "type": "integer",
            "description": "Total gold earned (LoL)."
          },
          "respawn": {
            "$ref": "#/components/schemas/EsportsClock"
          },
          "buffs": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/EsportsBuff"
            }
          },
          "health": {
            "type": "integer"
          },
          "armor": {
            "type": "integer"
          },
          "money": {
            "type": "integer"
          },
          "loadout": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "character_id": {
            "type": "string",
            "description": "The provider's id for the character (LoL champion id), for portraits; absent before it is picked."
          }
        },
        "description": "Title-specific fields are absent for other titles."
      },
      "EsportsObjective": {
        "type": "object",
        "required": [
          "kind",
          "variant",
          "count"
        ],
        "properties": {
          "kind": {
            "type": "string",
            "description": "lower_snake: tower, inhibitor, dragon, baron, herald, void_grub, ..."
          },
          "variant": {
            "type": "string",
            "description": "Dragon element where it matters; empty otherwise."
          },
          "count": {
            "type": "integer"
          },
          "first": {
            "type": "boolean",
            "description": "True when this team took the kind first in the game."
          }
        }
      },
      "EsportsStructure": {
        "type": "object",
        "required": [
          "id",
          "kind",
          "owner_team_id",
          "destroyed"
        ],
        "properties": {
          "id": {
            "type": "string"
          },
          "kind": {
            "type": "string"
          },
          "owner_team_id": {
            "type": "string",
            "description": "The defender, not the destroyer."
          },
          "destroyed": {
            "type": "boolean"
          },
          "respawn": {
            "$ref": "#/components/schemas/EsportsClock"
          }
        }
      },
      "EsportsTimer": {
        "type": "object",
        "required": [
          "kind",
          "variant"
        ],
        "properties": {
          "kind": {
            "type": "string"
          },
          "variant": {
            "type": "string"
          },
          "clock": {
            "$ref": "#/components/schemas/EsportsClock"
          }
        }
      },
      "EsportsBuff": {
        "type": "object",
        "required": [
          "kind"
        ],
        "properties": {
          "kind": {
            "type": "string"
          },
          "clock": {
            "$ref": "#/components/schemas/EsportsClock"
          }
        }
      },
      "EsportsDraftAction": {
        "type": "object",
        "required": [
          "sequence",
          "action",
          "team_id",
          "draftable_type",
          "draftable"
        ],
        "properties": {
          "sequence": {
            "type": "integer"
          },
          "action": {
            "type": "string",
            "description": "pick or ban."
          },
          "team_id": {
            "type": "string"
          },
          "draftable_type": {
            "type": "string",
            "description": "character or map."
          },
          "draftable": {
            "type": "string"
          },
          "draftable_id": {
            "type": "string",
            "description": "The provider's id for the champion, hero, agent or map, for portraits (the same id space as player character_id); absent when unknown."
          }
        }
      },
      "EsportsRound": {
        "type": "object",
        "required": [
          "number",
          "started",
          "finished",
          "winner_team_id",
          "win_type"
        ],
        "properties": {
          "number": {
            "type": "integer"
          },
          "started": {
            "type": "boolean"
          },
          "finished": {
            "type": "boolean"
          },
          "winner_team_id": {
            "type": "string",
            "description": "Empty while the round runs."
          },
          "win_type": {
            "type": "string"
          }
        }
      },
      "EsportsPlay": {
        "type": "object",
        "required": [
          "id",
          "game",
          "type",
          "kind",
          "variant",
          "team_id",
          "player_name",
          "target"
        ],
        "properties": {
          "id": {
            "type": "string",
            "description": "Stable provider event id: render a play once per id."
          },
          "game": {
            "type": "integer"
          },
          "round": {
            "type": "integer"
          },
          "clock_seconds": {
            "type": "integer"
          },
          "type": {
            "type": "string",
            "description": "Provider actor-action-target type, e.g. player-killed-player."
          },
          "kind": {
            "type": "string",
            "description": "Normalized kind: kill, multikill, tower, dragon, baron, victory, round_end, ..."
          },
          "variant": {
            "type": "string",
            "description": "Dragon element, or a round_end's win type; empty otherwise."
          },
          "team_id": {
            "type": "string"
          },
          "player_name": {
            "type": "string"
          },
          "target": {
            "type": "string"
          },
          "occurred_at_ms": {
            "type": "integer",
            "description": "Unix milliseconds."
          },
          "multikill": {
            "type": "integer",
            "description": "Kills in a multikill play: 2 double, 3 triple, 4 quadra, 5 penta. Present only when kind is multikill."
          }
        }
      },
      "ChallengeAck": {
        "type": "object",
        "required": [
          "op",
          "nonce"
        ],
        "properties": {
          "op": {
            "const": "challenge"
          },
          "nonce": {
            "type": "string",
            "pattern": "^[A-Za-z0-9_-]{1,255}$",
            "description": "This connection's challenge nonce (a UUID). Render the Turnstile widget with it as cData before minting a ticket at POST /api/ws-ticket; the ticket then verifies only on this socket, whatever IP either request came from. Not a secret, never rotated for the life of the connection."
          },
          "rid": {
            "type": "string"
          }
        }
      },
      "ChallengeRequest": {
        "type": "object",
        "required": [
          "op"
        ],
        "properties": {
          "op": {
            "const": "challenge"
          },
          "rid": {
            "type": "string"
          }
        }
      }
    }
  }
}
```
