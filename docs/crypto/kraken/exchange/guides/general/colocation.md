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
source_url: 'https://docs.kraken.com/exchange/guides/general/colocation'
updated_at: 2026-11-13
---

# Colocation and connectivity

> Low-latency connectivity options for Kraken's trading infrastructure, from cloud to direct cross-connect

Kraken's core trading infrastructure — both Spot and Derivatives engines — is hosted at Equinix in London. This page covers connectivity options and latency expectations.

## Connectivity tiers

| Option | Typical RTT | Requirements | APIs available |
| :- | :- | :- | :- |
| Direct colocation (cross-connect) | \~200 μs | VIP status, NDA, Equinix London presence | FIX, WebSocket, REST |
| Beeks Financial Cloud | \~200 μs | Beeks VPS or Bare Metal subscription | FIX, WebSocket, REST |
| AWS London (eu-west-2) | \~2 ms | IP whitelisting or VPC Peering | FIX, WebSocket, REST |
| BSO / Avelacom (Tokyo) | \~140 ms | Provider subscription | FIX, WebSocket, REST |
| BSO / Avelacom (US ↔ London) | \~60 ms | Provider subscription | FIX, WebSocket, REST |

> [!NOTE]
>
> REST is available at all connectivity tiers but is not optimised for low-latency order entry. Use FIX or WebSocket for latency-sensitive trading.

## Direct colocation

Direct colocation gives you a physical cross-connect to Kraken's infrastructure at Equinix London.

**Requirements:**

* VIP client status (existing volume threshold or qualifying planned volume)
* NDA signed with Kraken (datacenter location and cross-connect specs are disclosed under NDA)
* Infrastructure in Equinix London (or plans to deploy)

Once approved, Kraken issues two Letters of Authorization (LOAs) for provisioning dual diverse cross-connects. Contact your Account Manager to begin the onboarding process.

## Beeks Financial Cloud

Beeks provides managed VPS and Bare Metal hosting in Equinix London, in the same campus as Kraken's infrastructure. Latency is comparable to direct cross-connect (\~200 μs app-level RTT).

Beeks is the recommended path for clients who want ultra-low latency without managing their own Equinix cage. Contact [Beeks](https://www.beeksgroup.com) to set up a subscription, then coordinate with your Kraken Account Manager for connectivity.

## AWS London

Connect via public endpoints with IP whitelisting (all tiers) or VPC Peering (VIP clients).

* Latency: \~2 ms
* IP whitelisting instructions are provided during onboarding
* Suitable for systematic strategies that are not latency-critical

## Global connectivity (BSO / Avelacom)

For clients connecting from Tokyo or the US, Kraken partners with BSO and Avelacom for dedicated low-latency cross-border connectivity.

| Route | Typical latency |
| :- | :- |
| London ↔ Tokyo | \~140 ms |
| London ↔ US | \~60 ms |

Both providers offer private, dedicated fiber — not shared internet. Kraken is provider-agnostic; choose based on your existing relationships and geographic requirements.

## Related guides

> [card] [FIX introduction](https://docs.kraken.com/exchange/guides/fix/introduction.md)
>
> FIX 4.4 session setup, hours of operation, and connectivity details

> [card] [FIX authentication](https://docs.kraken.com/exchange/guides/fix/authentication.md)
>
> Logon message and session authentication

> [card] [Choose your protocol](https://docs.kraken.com/exchange/guides/general/api-comparison.md)
>
> Latency and feature trade-offs across REST, WebSocket, and FIX
