---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/guides/spot-clordid
api_type: Guide
updated_at: 2026-05-27 19:58:16.302424
---

# Spot Client Order Identifiers

The `cl_ord_id` parameter enables clients to tag orders with their own text or UUID identifiers for tracking and managing transactions across all Kraken APIs.

## Overview

### What is cl_ord_id?

The `cl_ord_id` terminology is borrowed from Financial Information eXchange (FIX) protocol. It is a parameter used as a "client order identifier" for tracking and managing transactions.

### Why is cl_ord_id Important?

It's essential for clients to communicate about specific orders without confusion, and the `cl_ord_id` provides a unique identifier for each open order. The client assigns a `cl_ord_id` on order placement and Kraken uses this identifier to provide status updates back to the client.

Kraken verifies `cl_ord_id` uniqueness across open orders for each client. FIX protocol extends this uniqueness check to across open orders and FIX session.

The `cl_ord_id` is particularly important when it comes to managing flow. If a client wants to cancel or amend an order, they can provide the `cl_ord_id` of that order in the request.

## Comparing Order Identifiers

Kraken has a range of order identifiers with different characteristics. The client can choose the combination of identifiers to best fit their requirements.

Characteristic| cl_ord_id| Kraken Id| Userref  
---|---|---|---  
Format| string| string| number  
Encoding| UUID, free text| Kraken proprietary| +/- integer  
Example| `d15708c1-dbb6-465d-b77d-47258319cc90`| `OCNNCT-MEB2I-2XGM7L`| `123948576`  
Enforced Uniqueness| Open orders (+ FIX session) per client| Open and closed orders for all clients| None  
Assigned By| Client| Kraken| Client  
Good For| Managing daily flow with client preferred id format| Record keeping (unique across all orders over time) and managing flow| Tagging groups of orders with single reference  
  
note

The `cl_ord_id` and `userref` are mutually exclusive—they cannot both be used on the same order.

## Format and Performance

`cl_ord_id` supports 3 different formats, depending on the length of the string:

Format| Description| Example  
---|---|---  
Long UUID| 32 hex characters separated with 4 dashes| `6d1b345e-2821-40e2-ad83-4ecb18a06876`  
Short UUID| 32 hex characters with no dashes| `da8e4ad59b78481c93e589746b0cf91f`  
Free text| Free format ASCII text up to 18 characters| `meme-20240509-00010`  
  
Under the covers, the strings are stored as a 128-bit integer for efficiency and performance. A 128-bit integer is much more space efficient than a 36-character string.

Operations and indexing on integers is more efficient than strings, meaning checking uniqueness and queries for orders can be much faster.

## Example: Order Management with UUID

**New Order:** Client creates a new passive order with UUID as `cl_ord_id`
    
    
    {  
        "method": "add_order",  
        "params": {  
            "order_type": "limit",  
            "side": "buy",  
            "limit_price": 60299.9,  
            "order_qty": 1.0,  
            "symbol": "BTC/USD",  
            "cl_ord_id": "0835958d-c526-4ad8-aea8-af54836de47e"  
        }  
    }  
    

**Cancel Order:** Client cancels the order using `cl_ord_id` (a list of identifiers is supported)
    
    
    {  
        "method": "cancel_order",  
        "params": {  
            "cl_ord_id": [  
                "0835958d-c526-4ad8-aea8-af54836de47e"  
            ]  
        }  
    }  
    

## FIX Protocol Guidelines

In the FIX protocol, the Tags ClOrdID and OrigClOrdID (Tags `11` and `41`) are mapped to the ClOrdID format as described above. This means that these order parameters are no longer limited to INT32. Instead, FIX ClOrdID now supports UUIDs.

The adoption of UUIDs, specifically timestamp-first version 4 UUIDs, significantly improves the efficiency and uniqueness of order identifiers. Unlike traditional INT32 identifiers, UUIDs offer a virtually limitless address space, greatly reducing the risk of identifier collisions and enhancing the robustness of the trading system.

### Timestamp-First v4 UUIDs

  * **Structure** : Timestamp-first v4 UUIDs start with a timestamp, ensuring that each generated UUID is unique and sequential based on the time of creation.
  * **Uniqueness** : These UUIDs combine the uniqueness of version 4 UUIDs with the time-based ordering, making them ideal for high-frequency trading environments.
  * **Compatibility** : They are fully compatible with existing systems that support UUIDs, ensuring a smooth transition and integration.

### Implementation Guidelines

To improve the efficiency of the FIX API, clients are required to send a ClOrdID of either:

  * **Ever-Increasing Positive Numbers** : Clients can use ever-increasing positive numbers, such as nanosecond timestamps, to ensure the uniqueness and sequential nature of the identifiers.
* _Example_ : Using the current microsecond timestamp as the ClOrdID, such as `1623448294234000` (the field is max 18 characters)
  * **Timestamp-First v4 UUIDs** : Alternatively, clients can adopt timestamp-first v4 UUIDs, which provide a robust and scalable solution for order identification.
* _Example_ : A timestamp-first v4 UUID might look like `1b4e28ba-2fa1-11d2-883f-0016d3cca427`, where the initial part (`1b4e28ba-2fa1`) of the UUID represents the timestamp.
* Overview
* What is cl_ord_id?
* Why is cl_ord_id Important?
  * Comparing Order Identifiers
  * Format and Performance
  * Example: Order Management with UUID
  * FIX Protocol Guidelines
* Timestamp-First v4 UUIDs
* Implementation Guidelines