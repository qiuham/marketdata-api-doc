---
exchange: deribit
source_url: https://docs.deribit.com/starbase/creating-api-key
api_type: Starbase
updated_at: 2026-11-26 19:02:03.320893
---

# Creating a Starbase API Key

> Create Starbase API keys, pick Starbase-specific scopes, and resolve the No active member error after the target account belongs to a Member.

Starbase API keys are created through the [**Starbase section**](https://www.deribit.com/account/BTC/starbase/api-keys) of the Account Panel (not the API section). The creation flow is otherwise the same as standard Deribit API keys, but with a different set of available scopes.

> [card] [Create and assign a Member first](https://docs.deribit.com/starbase/creating-member.md)
>
> Complete [Creating and Assigning a Member](https://docs.deribit.com/starbase/creating-member.md) on the main account before generating any key. Key creation is scoped to a Member; skipping that step is the usual cause of the **"No active member"** error.

> [!WARNING]
>
> The Starbase section is only visible after your account has been authorized by a Deribit admin. If you do not see the section, contact \[[support@deribit.com](mailto:support@deribit.com)]\(mailto:[support@deribit.com](mailto:support@deribit.com)).

> [!NOTE]
>
> **"No active member" error**: If key creation fails with a "No active member" error, the account you are creating the key for does not belong to an active Member. Go back to [Creating and Assigning a Member](https://docs.deribit.com/starbase/creating-member.md), add the account on the **main-account** level, then create the key while switched into the subaccount UID that will use it.

> [!NOTE]
>
> Starbase API key management is a sensitive operation. If your account has Two-Factor Authentication (2FA) enabled, you will be prompted for a security key confirmation. See [Security Keys](https://docs.deribit.com/articles/security-keys.md) for details.

## Front-end interface

**1. Navigate to the Starbase Section**

Open the [**Starbase section**](https://www.deribit.com/account/BTC/starbase/api-keys) in the Account Panel.

The Starbase section is separate from the standard **API** section. Make sure you are in the correct section.

![Starbase Section](https://mintcdn.com/deribit/tO0Fri3Xhug1I2Vk/starbase/starbase_tab.png?fit=max\&auto=format\&n=tO0Fri3Xhug1I2Vk\&q=85\&s=e3a4acdcc5ef7947f66e36ab782074fb)

Switch into the **subaccount UID** that will use the key. The Member must already include this UID. See [Creating and Assigning a Member](https://docs.deribit.com/starbase/creating-member.md) if it does not.

**2. Create a New API Key**

With the Member selected, press **Add new key** to open the key creation dialog.

Provide an optional **Name** for the key, then select one or more scopes from the following:

| Scope | Description |
| - | - |
| **FIX Drop Copy** | Receive a consolidated drop copy of all activity on the portfolio via the [FIX Drop Copy API](https://docs.deribit.com/starbase/fix-drop-copy-api.md) |
| **SBE Order Entry** | Submit, amend, and cancel orders via the [Simple Binary Encoding (SBE) Order Entry API](https://docs.deribit.com/starbase/binary-api-reference.md) |
| **REST** | Access REST endpoints (portfolio management, cancel all, etc.) |

> [!NOTE]
>
> Scopes are not currently enforced on the REST gateway: any Starbase API key belonging to a direct-access-enabled portfolio can call every Starbase REST endpoint (order entry and portfolio management, including `cancel_all`, `lock_portfolio`, and `unlock_portfolio`), regardless of the scopes selected here. Scope-based restrictions may be introduced in the future, so select the scopes that match the key's intended use.

> [!NOTE]
>
> Multicast market data and the retransmit API are unauthenticated. No API key or scope is required to subscribe to them.

![Create API Key Dialog](https://mintcdn.com/deribit/tO0Fri3Xhug1I2Vk/starbase/starbase_api_key.png?fit=max\&auto=format\&n=tO0Fri3Xhug1I2Vk\&q=85\&s=dfbc42e906239bfff26854c18b765dca)

Click **Create API Key** to generate the key.

**3. Save Your Credentials**

Once created, you will receive a **Client ID** and **Client Secret**.

![API Key Created](https://mintcdn.com/deribit/tO0Fri3Xhug1I2Vk/starbase/starbase_credidentials.png?fit=max\&auto=format\&n=tO0Fri3Xhug1I2Vk\&q=85\&s=2f3a88aefd47c68224fe3ce331270680)

> [!WARNING]
>
> The Client Secret is only shown once when the key is created. Store it securely, as you cannot retrieve it later.

For a description of what these credentials are, see the [Client ID and Client Secret](https://docs.deribit.com/articles/creating-api-key.md#client-id) section of the Creating new API key guide.

## API key limits

Each subaccount can have up to **8 Starbase API keys**. Because each gateway connection requires its own API key, plan your key allocation based on the number of gateway connections you intend to maintain.

Each API key can hold **one connection per gateway**. With 5 gateway pairs, that is up to 10 simultaneous connections per key. Reconnecting the same key to the same gateway terminates the existing session. See [Gateway Connectivity](https://docs.deribit.com/starbase/gateway-connectivity.md#api-keys) for the full connection rules.

Starbase API keys use a separate counter from standard Deribit API keys. Starbase API keys do not count toward your standard API key quota, and standard API keys do not count toward your Starbase quota. A standard Deribit API key cannot authenticate to Starbase. You always need a separate Starbase key.

## Next steps

> [card] [Creating and Assigning a Member](https://docs.deribit.com/starbase/creating-member.md)
>
> Required before any Starbase API key can be created

> [card] [Gateway Connectivity](https://docs.deribit.com/starbase/gateway-connectivity.md)
>
> How API keys map to gateway connections and connection rules

> [card] [Binary API Reference](https://docs.deribit.com/starbase/binary-api-reference.md)
>
> SBE protocol structure, message headers, and data types

> [card] [Placing a New Order](https://docs.deribit.com/starbase/placing-new-order.md)
>
> Submit your first order via the SBE Order Entry API

> [card] [FIX Drop Copy API](https://docs.deribit.com/starbase/fix-drop-copy-api.md)
>
> Consolidated drop copy of all portfolio activity

> [card] [Session Messages](https://docs.deribit.com/starbase/session-messages.md)
>
> Logon, logout, and heartbeat session message flows

> [card] [Cancel on Disconnect](https://docs.deribit.com/starbase/cancel-on-disconnect.md)
>
> Automatic order cancellation on connection loss


## Related topics

- [Creating and Assigning a Member](https://docs.deribit.com/starbase/creating-member.md)
- [Starbase Connectivity Quickstart](https://docs.deribit.com/starbase/quickstart.md)
- [Infrastructure, Connectivity & Best Practices](https://docs.deribit.com/starbase/connectivity-best-practices.md)
- [REST Order Gateway Authentication](https://docs.deribit.com/starbase/rest-authentication.md)
- [Gateway Connectivity](https://docs.deribit.com/starbase/gateway-connectivity.md)