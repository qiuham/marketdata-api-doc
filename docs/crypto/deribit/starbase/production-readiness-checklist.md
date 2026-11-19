---
exchange: deribit
source_url: https://docs.deribit.com/starbase/production-readiness-checklist
api_type: Starbase
updated_at: 2026-11-19 19:05:48.328369
---

# Production Readiness Checklist

> Readiness checklist for clients onboarding to Starbase SBE order entry: Member setup, API key scopes, MMP risk bypass, SBE XMLs, and logon testing.

This checklist is for clients already onboarded to Starbase. Work through the steps below to make sure production order entry is ready.

> [!NOTE]
>
> Read the [Connectivity Quickstart](https://docs.deribit.com/starbase/quickstart.md) first. It covers network access, Member assignment, key creation, and end-to-end validation. This checklist assumes that setup is done and only verifies the points most likely to block production trading.

**1. Confirm Your Member Setup**

A Member groups the portfolios (accounts/subaccounts) that trade on Starbase. Members are managed at the **main-account level only**. Subaccounts cannot create or manage Members.

* Add every main-account or subaccount UID that needs Starbase access to your Member. Most clients can configure exactly **one Member**. Broker clients that require separate Members for independent end clients must contact \[[support@deribit.com](mailto:support@deribit.com)]\(mailto:[support@deribit.com](mailto:support@deribit.com)) to have multi-Member access enabled.
* Verify the setup in the [Starbase section](https://www.deribit.com/account/BTC/starbase/api-keys) of the Account Panel or programmatically with [`private/get_members`](https://docs.deribit.com/api-reference/account-management/private-get_members).

> [!WARNING]
>
> A subaccount that does not belong to an active Member cannot authenticate to Starbase. API key creation for it fails with a **"No active member"** error.

See [Creating and Assigning a Member](https://docs.deribit.com/starbase/creating-member.md), [Account Model](https://docs.deribit.com/starbase/account-model.md), and [Creating a Starbase API Key](https://docs.deribit.com/starbase/creating-api-key.md) for details.

**2. Check API Key Scopes for SBE Order Entry**

Starbase API keys are separate from standard Deribit API keys. A standard key cannot authenticate to Starbase.

* Create keys in the [Starbase section](https://www.deribit.com/account/BTC/starbase/api-keys) of the Account Panel while switched into the **subaccount UID** that will use the key.
* The key needs the **SBE Order Entry** scope to submit, amend, and cancel orders. Add **FIX Drop Copy** and **REST** scopes if your integration uses those APIs.
* Plan your key allocation: up to **8 Starbase API keys per subaccount**, one connection per gateway per key. Reconnecting the same key to the same gateway terminates the existing session.

**3. Configure MMP and Use the Risk Bypass**

The lowest-latency order entry path on Starbase is the [MMP risk bypass](https://docs.deribit.com/starbase/risk-bypass.md): MMP-tagged flow goes straight from the gateway to the matching engine, skipping the risk module. It also reduces load on Deribit's risk and margin engines.

* **Orders**: set the `MMP` flag (field 10, bit 4) on [`NewOrderRequest`](https://docs.deribit.com/starbase/placing-new-order#neworderrequest-100). The bypass applies to both making and taking flow.
* **Mass quotes**: MMP is always enforced through the `mmpGroupId` referenced on every `MassQuoteRequest`, so mass quoting uses the bypass by default.
* Configure your MMP limits (quantity, delta, vega, interval, frozen time, and Max Quote Quantity) with [`private/set_mmp_config`](https://docs.deribit.com/api-reference/trading/private-set_mmp_config). Note the scoping difference: order MMP applies **per subaccount and base/quote pair**, while mass-quote MMP works through an explicit `mmpGroupId`.

> [!WARNING]
>
> The risk bypass requires **Quantity Limit ≤ Max Quote Quantity** in the MMP configuration. If the Quantity Limit is set higher than the Max Quote Quantity, MMP-tagged flow does not bypass the risk engine. Verify your values with [`private/get_mmp_config`](https://docs.deribit.com/api-reference/trading/private-get_mmp_config).

See [Market Maker Protection](https://docs.deribit.com/starbase/mmp.md) for configuration, reset, and monitoring details.

**4. Update to the Latest SBE XMLs**

Download the current integration resources and regenerate your SBE codecs (or update to the latest SDK):

* [SBE order entry XML](https://docs.deribit.com/specifications/deribit-sbe-xmls/deribit-sbe-order-api.xml)
* [SBE market data XML](https://docs.deribit.com/specifications/deribit-sbe-xmls/deribit-sbe-market-data-api.xml)
* [Order entry SDK](https://docs.deribit.com/starbase/starbase-deribit-order-sdk-14.0.zip)
* [Market data SDK](https://docs.deribit.com/starbase/starbase-deribit-md-sdk-2.0.zip)

> [!NOTE]
>
> Confirm the schema versions at the top of each XML file against your local copies and the [Starbase Changelog](https://docs.deribit.com/changelogs/starbase.md). Current published versions:
>
> * **Order entry**: schema `version` **19** (`semanticVersion` **1.5**)
> * **Market data**: schema `version` **1** (`semanticVersion` **1.0**)

Note that reference data is published on the multicast market data feeds, and your integration should be comfortable consuming it from there:

* `InstrumentDefinition`: full instrument definitions on the snapshot channels
* `IndexInfo` (12): index price per currency pair
* `InstrumentInfo` (14): `minSellPrice`, `maxBuyPrice`, and `markPrice` per instrument
* `InstrumentRef` (15): funding, settlement/delivery prices, and open interest per instrument

See [Reference Data](https://docs.deribit.com/starbase/reference-data.md) for full message details.

**5. Test Order Entry Logon and Heartbeats**

Test Logon, Logout, Heartbeat, and Test on the production gateways for each product group you trade.

1. Establish TCP connectivity to the gateway pair for each product group you trade. See [Gateway Connectivity](https://docs.deribit.com/starbase/gateway-connectivity.md).
2. Send a `LogonRequest` and expect a `LogonResponse`. Note the `heartbeatIntervalSeconds` value the server returns.
3. Keep the session alive with `Heartbeat` messages at the expected interval, and use `TestRequest` to elicit a `Heartbeat` echoing your `correlationId`.
4. Repeat on **both the A and B sides** of each required gateway pair.

> [!NOTE]
>
> Do not treat a successful TCP connection as a pass. Authentication and the heartbeat exchange must both work. See [Session Messages](https://docs.deribit.com/starbase/session-messages.md) for the full message flows.

**6. Know Where to Find Fees, Open Orders, and Order History**

Starbase order state is distributed differently from the standard Deribit APIs. Make sure your reconciliation and reporting pull each data type from the right place:

| Data | Where to get it |
| - | - |
| **Open orders** | The originating SBE session, [FIX Drop Copy](https://docs.deribit.com/starbase/fix-drop-copy-api.md), or the Starbase REST `GET /api/v2/private/get_open_orders` snapshot (capped at 10 requests per minute per portfolio on each REST gateway; a recovery tool, not a live feed). Open Starbase orders appear in the web UI, but open orders and pre-trade risk refresh every 10 seconds and may not reflect the latest state immediately. They do **not** appear in the standard WebSocket/FIX order feeds. |
| **Order history** | Standard [`private/get_order_history_*`](https://docs.deribit.com/api-reference/trading/private-get_order_history_by_currency) endpoints return only orders that reached the book or filled. Rejected and zero-fill orders cannot be retrieved retroactively. Persist FIX Drop Copy Execution Reports as they arrive. |
| **Fees** | Trades executed on Starbase appear on the standard private trade feeds, which include per-trade `fee` and `fee_currency` fields. For example [`private/get_user_trades_by_currency`](https://docs.deribit.com/api-reference/trading/private-get_user_trades_by_currency). |

> [!TIP]
>
> If you need to adjust your Member setup, [`private/set_member`](https://docs.deribit.com/api-reference/account-management/private-set_member), [`private/delete_member`](https://docs.deribit.com/api-reference/account-management/private-delete_member), and [`private/get_members`](https://docs.deribit.com/api-reference/account-management/private-get_members) are available on the [classic JSON-RPC API](https://docs.deribit.com/articles/json-rpc-overview.md) and in the Starbase tab of the Account Panel.

## Questions?

If anything on this list is not working as expected:

* Send network and multicast issues to [[colo-support@coinbase.com](mailto:colo-support@coinbase.com)](mailto:colo-support@coinbase.com).
* Send protocol rejects and account-configuration questions to your Technical Account Manager or [[support@deribit.com](mailto:support@deribit.com)](mailto:support@deribit.com).

## Next steps

> [card] [Infrastructure & Best Practices](https://docs.deribit.com/starbase/connectivity-best-practices.md)
>
> Deployment costs, gateway architecture, failover, and protocol selection.

> [card] [Gateway Connectivity](https://docs.deribit.com/starbase/gateway-connectivity.md)
>
> Production and test addresses, ports, and gateway pairs.

> [card] [Risk Bypass](https://docs.deribit.com/starbase/risk-bypass.md)
>
> How MMP-tagged flow bypasses the risk module.

> [card] [Starbase Changelog](https://docs.deribit.com/changelogs/starbase.md)
>
> Release notes and schema announcements.


## Related topics

- [Starbase API Changelog](https://docs.deribit.com/changelogs/starbase.md)
- [Creating and Assigning a Member](https://docs.deribit.com/starbase/creating-member.md)
- [Starbase Connectivity Quickstart](https://docs.deribit.com/starbase/quickstart.md)
- [Starbase API Overview](https://docs.deribit.com/starbase/overview.md)
- [Infrastructure, Connectivity & Best Practices](https://docs.deribit.com/starbase/connectivity-best-practices.md)