---
exchange: deribit
source_url: https://docs.deribit.com/starbase/account-model
api_type: Starbase
updated_at: 2026-11-25 19:00:46.676349
---

# Account Model

> How the Starbase account and subaccount hierarchy differs from the Deribit main platform for order entry, drop copy, and permission scoping.

| Concept | Description | Mapping to Deribit |
| - | - | - |
| **Portfolio** | Container for positions, funds, and balances across all currencies | 1:1 with account (main- or sub-account) |
| **Member** | Group of portfolios representing a trading participant | Can span multiple subaccounts under one main account |

> [!NOTE]
>
> Members can only be configured from a **main account**. Subaccounts cannot create or manage Members. Additionally, the [Starbase section](https://www.deribit.com/account/BTC/starbase/api-keys) will only appear in your Account Panel once your account has been authorized by a Deribit admin. For the UI and API workflow, see [Creating and Assigning a Member](https://docs.deribit.com/starbase/creating-member.md).

### Manage Members through classic JSON-RPC

Authorized main accounts can manage their Starbase Members programmatically with the [classic JSON-RPC API](https://docs.deribit.com/articles/json-rpc-overview.md):

* [`private/get_members`](https://docs.deribit.com/api-reference/account-management/private-get_members): list the Members configured for the account
* [`private/set_member`](https://docs.deribit.com/api-reference/account-management/private-set_member): create a Member or update its name, assigned accounts, or active state
* [`private/delete_member`](https://docs.deribit.com/api-reference/account-management/private-delete_member): delete a Member

`private/get_members` requires `account:read`. Creating, updating, or deleting a Member requires `account:read_write`, main-account authentication, and Direct Access trading to be enabled.

### Do subaccounts need to belong to a Member?

Only subaccounts you intend to trade on Starbase need to belong to a Member. Starbase API key creation is scoped to a Member (see [Creating and Assigning a Member](https://docs.deribit.com/starbase/creating-member.md)), so a subaccount that isn't added to any Member simply has no way to authenticate against Starbase gateways, and therefore has no Starbase rate limit allocation of its own. A subaccount left outside of every Member is unaffected by anything in this page; it continues to trade exclusively through the standard Deribit APIs under the main platform's own limits.

### Using standard APIs alongside Starbase

Adding a portfolio to a Member enables Starbase access; it does not disable standard WebSocket or REST access for that portfolio. Orders submitted through either path affect the same portfolio balances, positions, margin, MMP, and SMP state, but the protocols are not interchangeable:

* Starbase and standard Deribit API keys are separate.
* Open Starbase orders and their lifecycle events are not available through the standard private WebSocket order feed. Use the originating SBE session or [FIX Drop Copy](https://docs.deribit.com/starbase/fix-drop-copy-api.md).
* Trades and positions resulting from Starbase orders remain available through the standard private APIs.
* Rate-limit allocations for Starbase are separate from the main platform's limits.

> [!WARNING]
>
> **Mass quoting is the exception.** Adding a portfolio to a Member blocks the classic mass quotes API for that portfolio. [`private/mass_quote`](https://docs.deribit.com/api-reference/trading/private-mass_quote) over [classic JSON-RPC](https://docs.deribit.com/articles/json-rpc-overview.md) (WebSocket) and mass quoting over the FIX API stop working. Mass quotes for Member portfolios must be submitted through the [Starbase Binary API](https://docs.deribit.com/starbase/mass-quotes.md).

> [!WARNING]
>
> **Mass quoting uses one operating mode per portfolio.** A portfolio can use either classic JSON-RPC/FIX mass quoting or Starbase mass quoting, but not both concurrently. You can switch the portfolio between Classic and Starbase mass-quote modes in real time through the API or Account Panel. Stop submission and reconcile resting quotes before switching modes.

### Member limits

Rate limits are allocated **per Member** and are shared across all API keys, sessions, and portfolios within that Member. Having more sessions or more portfolios does not increase your rate limits.

See the table below for the Member/Portfolio setup for the three major account types.

| Use Case | Description |
| :- | :- |
| **Directly onboarded client** | These clients use **exactly one Member**. Add every main-account and subaccount UID that needs Starbase access to this Member. |
| **Broker clients** | Brokers can request separate Members for independent end clients. Multi-Member access must first be enabled by Deribit Support. After enablement, each new portfolio or subaccount must be assigned to the appropriate Member. |

> [!NOTE]
>
> The Account Panel may offer an option to add another Member even when the account is limited to one. Unless you are an enabled broker client, assign all UIDs that need Starbase access to the existing Member. Brokers that require multiple Members should contact \[[support@deribit.com](mailto:support@deribit.com)]\(mailto:[support@deribit.com](mailto:support@deribit.com)). Multi-Member setups do not receive higher rate limits than single-Member setups.

### Members and margin mode

A Member is a grouping of portfolios and can contain a mix of margin modes. For example, one subaccount on Standard Margin (SM) can sit alongside others on Segregated Portfolio Margin (S:PM) or Cross Portfolio Margin (X:PM). However, options positions are not supported on Standard Margin, and this restriction is enforced per portfolio regardless of where the order originates:

* **Existing positions**: A subaccount that already holds options positions while on Standard Margin cannot be added to a Member, even if other subaccounts being added to the same Member succeed.
* **New positions**: Once a Standard Margin subaccount is scoped to a Member, no new options positions can be opened on it, whether the order is submitted via Starbase (Direct Access) or via the [classic JSON-RPC](https://docs.deribit.com/articles/json-rpc-overview.md) API.

To trade options on a subaccount that belongs to a Member, switch that subaccount's margin mode to Segregated Portfolio Margin or Cross Portfolio Margin.


## Related topics

- [private/delete_member](https://docs.deribit.com/api-reference/account-management/private-delete_member.md)
- [private/get_members](https://docs.deribit.com/api-reference/account-management/private-get_members.md)
- [private/set_member](https://docs.deribit.com/api-reference/account-management/private-set_member.md)
- [Creating and Assigning a Member](https://docs.deribit.com/starbase/creating-member.md)
- [Starbase Connectivity Quickstart](https://docs.deribit.com/starbase/quickstart.md)