---
exchange: deribit
source_url: https://docs.deribit.com/starbase/session-messages
api_type: Starbase
updated_at: 2026-11-27 19:00:52.997905
---

# Starbase Session Messages

> Session-level messages in the Starbase Binary API: logon and sequence-number handling, weekly sequence reset, heartbeat, logout, and session rejects.

## Session Messages

Session messages manage the lifecycle of a TCP connection to a Starbase gateway, including authentication, heartbeating, and sequence number recovery.

### Sequence numbers

SBE order-entry sequence numbers are persisted across reconnects unless the client or the exchange resets them. They are **not** recovered like a full FIX session: the gateway **never** sends [`ResendRequest` (20)](#resendrequest-20) to the client.

#### Logon with `resetSeqNum=0`

On reconnect, the `sequenceNum` in the `LogonRequest` header must continue from the previous session. A discontinuous inbound sequence is handled as follows. The two cases are **not** symmetric:

| Client Logon `sequenceNum` | Gateway behavior |
| - | - |
| Too low (replay) | Logon is **rejected**. The gateway sends [`LoggedOut`](#loggedout-5) with reason `sequence number too low` and disconnects. |
| Too high (gap) | The gap is **ignored**. Logon succeeds. The gateway does not request the missing inbound messages. |
| Next expected | Logon succeeds. |

To recover outbound events the client missed, send [`ResendRequest` (20)](#resendrequest-20) after a successful logon to the **same** gateway host.

#### Logon with `resetSeqNum=1`

Both sides reset sequence numbers to `1`. Use this after an exchange-initiated reset (see below), or whenever the client wants a fresh sequence.

#### Weekly sequence reset

The exchange resets SBE order-entry sequence numbers **weekly on Saturday**. The A and B gateways of each pair reset at different times:

| Gateway side | Weekly reset time (US Central) |
| - | - |
| A | approximately 11:55 |
| B | approximately 12:00 (the same default as INTX) |

The staggered times apply to every SBE order gateway pair in production and testnet. All sessions on the resetting gateway are disconnected with reason `SEQUENCE_RESET`. Clients must reconnect with `resetSeqNum=1`. A client connected to both the A and B gateway of a pair keeps one live session throughout, provided it reconnects to A before B resets.

The weekly reset also applies to [FIX Drop Copy](https://docs.deribit.com/starbase/fix-drop-copy-api.md#sequence-numbers), which resets at approximately 12:00 US Central. Reconnect there with `ResetSeqNumFlag` (Tag 141) = `Y`.

> [!NOTE]
>
> The weekly reset tears down the TCP session. [Cancel on Disconnect](https://docs.deribit.com/starbase/cancel-on-disconnect.md) therefore applies as for any other disconnect: CoD-covered orders and quotes on that session are cancelled and are not restored on reconnect.

### LogonRequest (1)

First message sent by client after establishing TCP connection.

| Field | Name | Type | Length | Description |
| - | - | - | - | - |
| 1 | username | char | 16 | Client username |
| 2 | password | char | 48 | Client password |
| 3 | resetSeqNum | int8 | 1 | `0`=no, continue the previous session's sequence numbers. A too-low inbound seqNum is rejected; a gap is ignored. See [Sequence numbers](#sequence-numbers). `1`=yes, reset sequence numbers to `1`. Required after a weekly `SEQUENCE_RESET`. |
| 4 | schemaVersion | uint16 | 2 | Client-negotiated SBE schema (protocol) version. Optional; added in schema version `12`. See the version negotiation note below. |
| 5 | cancelOnDisconnect | int8 | 1 | Session-wide cancel-on-disconnect opt-in: `0`=no, each order and quote carries its own per-message flag `1`=yes, every order and quote submitted on this session is covered. Optional. See [Session-level CoD](https://docs.deribit.com/starbase/cancel-on-disconnect.md#session-level-cod) |
| 6 | liquidationNotifications | int8 | 1 | Session-wide opt-in to unsolicited liquidation notifications for the logged-on portfolio: `0`=no (default) `1`=yes, receive `OrderFilled` fills flagged `isLiquidation` and `PositionMoved` (330). Optional; added in schema version `22`. A logon that sets `1` with a `schemaVersion` below `22` is rejected. See [Liquidation notifications](https://docs.deribit.com/starbase/unsolicited-events.md#liquidation-notifications) |

### LogonResponse (2)

Response to `LogonRequest` on successful logon.

| Field | Name | Type | Length | Description |
| - | - | - | - | - |
| 1 | heartbeatIntervalSeconds | int32 | 4 | Interval in seconds at which the server expects heartbeat messages from the client |
| 2 | schemaVersion | uint16 | 2 | Echoes the schema (protocol) version accepted by the gateway, which is the authoritative negotiated version for the session. Added in schema version `12`. See the version negotiation note below. |

> [!NOTE]
>
> **Schema version negotiation** (schema version `12` and later): `schemaVersion` on `LogonRequest` acts as a gate. It determines whether new messages and new versions of existing messages are sent to the client. A value outside the gateway's accepted range is rejected at logon. The gateway echoes the accepted version in `LogonResponse`.
>
> There are two version numbers on the wire, and they are not equal:
>
> * **Session ceiling**: the `schemaVersion` sent at logon, which is the highest schema version the client can accept. One number per session, echoed back in `LogonResponse.schemaVersion`. This is the authoritative negotiated version for the session.
> * **Per-message stamp**: the `version` field in the header of each message the gateway sends, which is the newest schema version at which that particular message last changed, never above the session ceiling. If a message did not change between schema versions, its stamp is not bumped.
>
> For example, after negotiating version `19`, `LogonResponse` arrives with header `version = 12` because `LogonResponse` has not changed since version `12`. This is expected. Always read the negotiated version from the `schemaVersion` field, never from per-message header stamps.

### LogoutRequest (4)

Request by client to gracefully terminate a connection.

| Field | Name | Type | Length | Description |
| - | - | - | - | - |
| 1 | reasonLength | uint8 | 1 | Length of reason field |
| 2 | reason | char | 0-255 | ASCII-encoded string |

### LoggedOut (5)

Sent in response to `LogonRequest` if logon failed, or in response to `LogoutRequest`, or unsolicited for other reasons.

| Field | Name | Type | Length | Description |
| - | - | - | - | - |
| 1 | reasonLength | uint8 | 1 | Length of reason field |
| 2 | reason | char | 0-255 | ASCII-encoded string. Known values include `sequence number too low` (logon rejected because the inbound seqNum is below the next expected) and `SEQUENCE_RESET` (weekly exchange-initiated sequence reset; reconnect with `resetSeqNum=1`). |

### Heartbeat (10)

Sent by client or server periodically in the absence of other messages.

| Field | Name | Type | Length | Description |
| - | - | - | - | - |
| 1 | correlationId | int64 | 8 | Set if this Heartbeat is in response to a `TestRequest`; `0` if not |

### TestRequest (11)

Request a `Heartbeat` message. Can be sent by either client or server.

| Field | Name | Type | Length | Description |
| - | - | - | - | - |
| 1 | correlationId | int64 | 8 | Value the recipient should echo back in the `correlationId` of the `Heartbeat` response |

### ResendRequest (20)

Sent by the **client** to request resend of a limited number of missed outbound events. Works only when reconnecting to the same gateway host. The **server never sends this message**. Inbound sequence gaps at logon are ignored, not filled. See [Sequence numbers](#sequence-numbers).

| Field | Name | Type | Length | Description |
| - | - | - | - | - |
| 1 | fromSeqNum | int64 | 8 | Sequence number of first message to be resent |
| 2 | toSeqNum | int64 | 8 | Sequence number of the last message to be resent, or `0` if all available messages after `fromSeqNum` should be resent |

### GapFill (21)

Sent by server in lieu of admin/session messages while handling a resend request.

| Field | Name | Type | Length | Description |
| - | - | - | - | - |
| 1 | newSeqNum | int64 | 8 | Sequence number of next message to be sent by server |

### Reject (30)

Sent by the server in response to an unrecognized or malformed message from the client.

| Field | Name | Type | Length | Description |
| - | - | - | - | - |
| 1 | refSeqNum | int64 | 8 | Sequence number of the rejected message |
| 2 | reason | int8 | 1 | Rejection reason code. See the table below. |
| 3 | detailsLength | uint8 | 1 | Length of details field |
| 4 | details | char | 0-255 | ASCII-encoded string |

The table below lists all possible values of the `reason` field.

| Value | Name | Description |
| - | - | - |
| `1` | `INVALID_SCHEMA_ID` | Message schema ID does not match this gateway |
| `2` | `INVALID_TEMPLATE_ID` | Unrecognized message template ID |
| `3` | `INVALID_BLOCK_LENGTH` | Message block length does not match the template |
| `4` | `INVALID_FIELD_VALUE` | A field in the message contains an invalid value |
| `5` | `MESSAGE_DISABLED` | The message being submitted has been administratively disabled |
| `6` | `GATEWAY_NOT_ACTIVE` | The target gateway is not active |


## Related topics

- [Starbase Mass Cancel Messages](https://docs.deribit.com/starbase/mass-cancel.md)
- [Starbase API Changelog](https://docs.deribit.com/changelogs/starbase.md)
- [Creating a Starbase API Key](https://docs.deribit.com/starbase/creating-api-key.md)
- [Starbase Unsolicited Events](https://docs.deribit.com/starbase/unsolicited-events.md)
- [Starbase FIX Drop Copy API](https://docs.deribit.com/starbase/fix-drop-copy-api.md)