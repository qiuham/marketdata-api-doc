---
exchange: deribit
source_url: https://docs.deribit.com/starbase/smp
api_type: Starbase
updated_at: 2026-11-25 19:00:46.778888
---

# Self Match Prevention (SMP)

> Prevent orders on the same Member, or across all Members of a main account, from matching each other. Configure SMP tokens and choose the cancel behavior.

## Overview

Self Match Prevention (SMP) is a mechanism that prevents orders from matching with each other when they originate from the same member AND share the same SMP token. SMP helps prevent accidental self-trading and allows for more granular control over order matching behavior. On request, Deribit can extend SMP across all Members of the same main account; see [SMP across Members](#smp-across-members).

SMP uses three components to control order matching:

| Component | Description | Required | Scope |
| - | - | - | - |
| **SMP Mode** | Determines which order is cancelled when a self-match is detected | Per order (default configured via the WebSocket API [`private/set_self_trading_config`](https://docs.deribit.com/api-reference/account-management/private-set_self_trading_config)) | Order-level |
| **SMP Token** | Prevents matching between orders with the same token | Mandatory (can be set to null/0) | Order-level |
| **Member ID** | Scopes SMP to a specific member | SMP cannot trigger between Members, unless [extended across Members](#smp-across-members) | Member-level |

> [tab] SMP Mode
>
> SMP mode determines which order is cancelled when a self-match is detected:
>
> | Mode | Behavior |
> | - | - |
> | **CANCEL\_MAKER** | The resting (maker) order is cancelled |
> | **CANCEL\_TAKER** | The incoming (taker) order is cancelled |
>
> The SMP mode should be specified for each order. A default SMP mode can be configured via the WebSocket API [`private/set_self_trading_config`](https://docs.deribit.com/api-reference/account-management/private-set_self_trading_config) method, and users can change their default setting.
>
> > [!WARNING]
> >
> > **Speed-bumped orders always use CANCEL\_MAKER on the SBE gateway.** When a taker order submitted via the SBE gateway is speed-bumped, the SMP mode is overridden to `CANCEL_MAKER` regardless of the value in the request. This is consistent with standard market practice for speed-bumped orders.
> >
> > Orders submitted via the WebSocket API may use `CANCEL_TAKER` regardless of speed-bump state.
>
> > [!NOTE]
> >
> > **SMP Mode Selection**: When a self-match is detected, the SMP mode from the **aggressing order** (the incoming order) will be used to determine which order is cancelled.

> [tab] SMP Token
>
> The SMP token is a mandatory field in order messages that prevents matching between orders with the same token within the same Member. The field must always be present, but can be set to null (0) to allow self-matching.
>
> ### Matching Scenarios
>
> Matching is **prevented** only when **both** of the following conditions are met:
>
> * The same member ID (or both orders lack a member ID)
> * The same SMP token (non-null)
>
> | Scenario | Member | SMP Token | Matching Behavior |
> | - | - | - | - |
> | Same member, same token | Same | Same (non-null) | **Prevented** |
> | Same member, different tokens | Same | Different | **Allowed** |
> | Same member, null token | Same | Null | **Allowed** (self-matching allowed) |
> | Different members | Different | Same (non-null) | **Allowed** |
> | Different members | Different | Different | **Allowed** |
>
> **Key Points:**
>
> * SMP token is a mandatory field that must be specified on each order
> * Setting SMP token to null (0) allows self-matching
> * Orders with the same SMP token (non-null) within the same Member will not match
> * Two orders with the same SMP token from different Members can match, unless SMP is [extended across Members](#smp-across-members)

> [tab] Member
>
> **Self-match prevention is scoped to a Member** (a group of portfolios representing a trading participant). Two orders with the same SMP token within the same Member cannot match, but two orders with the same SMP token from different Members can match, unless SMP is [extended across Members](#smp-across-members) of the same main account.

### Orders from different systems

Orders originating from the WebSocket API, User Interface or other non-Starbase origin will have the SMP Token set based on the table below. To avoid matching with these orders when utilizing Starbase APIs, the same SMP Tokens should be used.

| Setting | SMP Token Value |
| - | - |
| Self-match prevention restricted to portfolio | `portfolio id` (equal to Deribit's User ID) |
| Self-match prevention extended to subaccounts | `member id` of the portfolio's Member |
| Self-match prevention extended across Members | `main portfolio id` (equal to Deribit's main account User ID) |
| Self-matching allowed | `null` (empty) |

## SMP across Members

By default, SMP never triggers between Members, even when they belong to the same main account. On request, Deribit can extend SMP across all Members of a main account. This is mainly relevant to accounts with several Members, such as brokers with multi-Member access. The setting applies to the main account and all of its subaccounts. Only Deribit can change it; [`private/set_self_trading_config`](https://docs.deribit.com/api-reference/account-management/private-set_self_trading_config) leaves it unchanged.

When the setting is enabled:

* **Self-match prevention enabled on the account:** the SBE gateway sets the SMP token of every order and mass quote to the `main portfolio id`, ignoring `selfMatchPreventionId` in the request. Orders submitted via the WebSocket API, FIX API or UI carry the same token. Orders from any Member under the main account do not match each other.
* **Self-matching allowed on the account:** SMP stays opt-in. Orders with the same non-null SMP token do not match each other across all Members of the main account.

The SMP mode of the aggressing order still decides which order is cancelled. While self-match prevention is enabled, [`private/get_account_summary`](https://docs.deribit.com/api-reference/account-management/private-get_account_summary) called with `extended` set to `true` returns `self_trading_extended_across_members: true` when the setting is on.

## API Usage

### Order Entry Messages

SMP fields are mandatory and must be specified in the following order entry messages:

| Message | SMP Token Field | Field Number | Description |
| - | - | - | - |
| [`NewOrderRequest`](https://docs.deribit.com/starbase/placing-new-order#neworderrequest) | `SMPToken` | 7 | This order cannot match with any other orders within the same portfolio with the same token. Set to null to allow self-matching. |
| [`MassQuoteRequest`](https://docs.deribit.com/starbase/mass-quotes#massquoterequest) | `SMPToken` | 4 | This order cannot match with any other orders within the same portfolio with the same token. Set to null to allow self-matching. |

### SMP Cancellation Indicators

When an order is cancelled due to self-match prevention, it will be indicated in the response messages:

| Message | Field | Value | Description |
| - | - | - | - |
| [`NewOrderResponse`](https://docs.deribit.com/starbase/placing-new-order#neworderresponse) | `cancelReason` (field 11) | `1` | `selfMatchPrevention` |
| [`AmendOrderResponse`](https://docs.deribit.com/starbase/amending-order#amendorderresponse) | `cancelReason` (field 12) | `1` | `selfMatchPrevention` |
| [`MassQuoteResponse`](https://docs.deribit.com/starbase/mass-quotes#massquoteresponse) | `buyQuoteStatus` (field 18) | `7` | `CanceledBySelfMatch` |
| [`MassQuoteResponse`](https://docs.deribit.com/starbase/mass-quotes#massquoteresponse) | `sellQuoteStatus` (field 19) | `7` | `CanceledBySelfMatch` |


## Related topics

- [Starbase API Changelog](https://docs.deribit.com/changelogs/starbase.md)
- [API Usage Policy](https://docs.deribit.com/articles/api-usage-policy.md)
- [Starbase API Overview](https://docs.deribit.com/starbase/overview.md)
- [Speed Bumps](https://docs.deribit.com/starbase/speed-bumps.md)
- [private/set_self_trading_config](https://docs.deribit.com/api-reference/account-management/private-set_self_trading_config.md)