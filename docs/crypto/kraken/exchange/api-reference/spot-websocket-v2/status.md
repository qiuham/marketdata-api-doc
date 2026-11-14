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
source_url: 'https://docs.kraken.com/exchange/api-reference/spot-websocket-v2/status'
updated_at: 2026-11-13
---

# Status

> Receive exchange status updates and connection verification

WSS
ws.kraken.com/v2
status

The `status` channel provides a mechanism to verify exchange status and successful initial connection.

There is no option to directly request a `status` update, a status will be automatically generated on successful websocket connection and when the trading engine status changes.

## Update

**channel** `string`

Value: `status`

**type** `string`

One of: `update`

**data** `object[]`

**properties**

**system** `string`

One of: `online`, `cancel_only`, `maintenance`, `post_only`

The status of the trading engine.

* `online`: Markets are operating normally - all order types may be submitted and order matching can occur.
* `maintenance`: Markets are offline for scheduled maintenance - new orders cannot be placed and existing orders cannot be cancelled.
* `cancel_only`: Orders can be cancelled but new orders cannot be placed. No order matching will occur.
* `post_only`: Only limit orders using the `post_only` option can be submitted. Orders can be cancelled. No order matching will occur.

**api\_version** `string`

One of: `v2`

The version of the websockets API.

**connection\_id** `integer`

A unique connection identifier (for debugging).

**version** `string`

The version of the websockets service.

**upcoming\_maintenance** `object[]`

Scheduled maintenance windows that are announced or approaching. Each entry describes a single window and how clients should prepare.

This field and `emergency` are additive and always appear together as JSON arrays (either both present or both absent). They are present only on deployments where the maintenance-status integration is enabled; when there is no maintenance to report the arrays are empty.

**properties**

**event\_id** `integer`

Stable identifier for the maintenance window.

**title** `string`

Human-readable event title. Sourced from Statuspage.

**expected\_start\_utc** `string`

RFC 3339 UTC timestamp for when the window is expected to begin.

**expected\_end\_utc** `string | null`

RFC 3339 UTC timestamp for when the window is expected to end, or `null` if not yet known.

**time\_to\_start\_s** `integer`

Seconds until `expected_start_utc`. Counts down as the window approaches and is clamped to `0` once the start time has passed.

**phase** `string`

One of: `announced`, `reminder_24h`, `approaching_30m`, `imminent_5m`, `final_warning_30s`, `unspecified`

How close the window is, from initial announcement through the final warning before it begins.

**affected\_services** `string[]`

Each of: `spot_ws`, `spot_rest`, `spot_fix`, `spot_trading`, `futures_ws`, `futures_rest`, `futures_fix`, `futures_trading`, `all`, `unspecified`

The services impacted by the window.

**order\_submission** `string`

One of: `allowed`, `discouraged`, `blocked`, `unspecified`

Whether new orders are accepted during the window.

**recommended\_action** `string`

One of: `continue`, `reduce_activity`, `cancel_open_orders`, `stop_new_orders`, `disconnect_and_wait`, `unspecified`

The action clients are advised to take ahead of the window.

**cancel\_before\_utc** `string | null`

RFC 3339 UTC deadline by which open orders should be cancelled, or `null` if not applicable.

**source\_url** `string`

Link to a public incident/status page for the window, or an empty string if none was provided.

**emergency** `object[]`

Unplanned incidents currently affecting one or more services. Each entry describes a single incident and its expected recovery steps.

This field and `upcoming_maintenance` are additive and always appear together as JSON arrays (either both present or both absent).

**properties**

**event\_id** `integer`

Stable identifier for the incident.

**title** `string`

Human-readable incident title. Sourced from Statuspage.

**incident\_status** `string`

One of: `investigating`, `identified`, `monitoring`, `unspecified`

Where the incident sits in its response lifecycle.

**impact** `string`

One of: `none`, `minor`, `major`, `critical`, `unspecified`

The severity of the incident's effect on trading.

**affected\_services** `string[]`

Each of: `spot_ws`, `spot_rest`, `spot_fix`, `spot_trading`, `futures_ws`, `futures_rest`, `futures_fix`, `futures_trading`, `all`, `unspecified`

The services impacted by the incident.

**started\_at\_utc** `string`

RFC 3339 UTC timestamp for when the incident began.

**next\_steps** `object[]`

The expected recovery steps and when each is anticipated.

**properties**

**applies\_to** `string[]`

Each of: `spot_ws`, `spot_rest`, `spot_fix`, `spot_trading`, `futures_ws`, `futures_rest`, `futures_fix`, `futures_trading`, `all`, `unspecified`

The services this step applies to.

**type** `string`

One of: `expected_restart`, `expected_cancel_only`, `expected_post_only`, `expected_online`, `unspecified`

The expected state transition for the affected services.

**expected\_at\_utc** `string`

RFC 3339 UTC timestamp for when the step is expected to occur.

**source\_url** `string`

Link to a public incident/status page for the event, or an empty string if none was provided.

```json Example: Update theme={null}
{
    "channel": "status",
    "data": [
        {
            "api_version": "v2",
            "connection_id": 13834774380200032777,
            "system": "online",
            "version": "2.0.0"
        }
    ],
    "type": "update"
}
```

```json Example: Update with maintenance status theme={null}
{
    "channel": "status",
    "data": [
        {
            "api_version": "v2",
            "connection_id": 13834774380200032777,
            "system": "online",
            "version": "2.0.0",
            "upcoming_maintenance": [
                {
                    "event_id": 21,
                    "title": "Scheduled Maintenance",
                    "expected_start_utc": "2025-08-12T02:00:00Z",
                    "expected_end_utc": "2025-08-12T03:00:00Z",
                    "time_to_start_s": 1800,
                    "phase": "approaching_30m",
                    "affected_services": ["futures_ws", "futures_trading"],
                    "order_submission": "discouraged",
                    "recommended_action": "reduce_activity",
                    "cancel_before_utc": "2025-08-12T01:55:00Z",
                    "source_url": "https://stspg.io/mt18zxvtzz00"
                }
            ],
            "emergency": [
                {
                    "event_id": 4821,
                    "title": "Spot Connectivity Incident",
                    "incident_status": "identified",
                    "impact": "major",
                    "affected_services": ["futures_ws"],
                    "started_at_utc": "2025-08-12T00:14:30Z",
                    "next_steps": [
                        {
                            "applies_to": ["futures_ws"],
                            "type": "expected_restart",
                            "expected_at_utc": "2025-08-12T00:45:00Z"
                        }
                    ],
                    "source_url": "https://status.kraken.com/incidents/4821"
                }
            ]
        }
    ],
    "type": "update"
}
```
