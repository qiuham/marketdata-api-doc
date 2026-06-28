---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/guides/embed-deposits-and-withdrawals
api_type: Guide
updated_at: 2026-05-27 19:56:49.082689
---

# Embed: Deposits & Withdrawals

This guide walks you through enabling crypto deposits and withdrawals for your users via the Payward Embed API.

## Prerequisites

  * Payward Embed API credentials (see [Authentication Guide](/api/docs/guides/embed-rest-auth))
  * A verified user with an IIBAN

note

Only **cryptocurrency** deposits are supported. Fiat deposits are not available through the Embed API.

## Crypto Deposits

### Deposit Workflow
    
    
    ┌──────────────────┐    ┌──────────────────┐    ┌──────────────────┐    ┌──────────────────┐    ┌──────────────────┐  
    │ List Deposit     │──▶ │ Create Deposit   │──▶ │ Display Address  │──▶ │ User Sends       │──▶ │ Receive          │  
    │ Methods          │    │ Address          │    │ to User          │    │ Crypto           │    │ Webhooks         │  
    └──────────────────┘    └──────────────────┘    └──────────────────┘    └──────────────────┘    └──────────────────┘  
     GET /funds/deposits/    POST /funds/deposits/   GET /funds/deposits/    (external wallet)       deposit.  
         methods/{asset}         addresses                addresses                                  status_updated  
1. **List Deposit Methods** : Query available networks, fees, and limits for an asset.
  2. **Create Deposit Address** : Generate an address for the chosen method.
  3. **Display Address to User** : Show the address (and any tag/memo) so the user can send crypto from an external wallet.
  4. **Deposit to Address** : Instruct the user to send crypto from their external wallet to the displayed deposit address. Ensure they include any required tag or memo.
  5. **Receive Webhooks** : Get notified via `deposit.status_updated` when the deposit is processed.

note

Completed deposits will appear in `GET /b2b/portfolio/transactions?user={iiban}&types=deposit`.

### Step 1: List Deposit Methods

Query available deposit methods for a crypto asset. Use the `method_id` from the response when creating an address in Step 2.

note

Most cryptocurrency deposits are free, with minimum deposit amounts varying by asset. A few cryptocurrencies are charged an `address_setup_fee` (a one-time fee on the user's first deposit to a new address) or a per-deposit `fee`. See [Cryptocurrency deposit fees and minimums](https://support.kraken.com/articles/360000292886-cryptocurrency-deposit-fees-and-minimums) for a full breakdown.

  * Python
  * JavaScript

    
    
    def list_deposit_methods(user_id, asset):  
        endpoint = f"/b2b/funds/deposits/methods/{asset}"  
        nonce = int(time.time() * 1000000000)  
      
        params = {"user": user_id}  
        signature = get_payward_signature(endpoint, None, API_SECRET, nonce, params)  
      
        headers = {  
            "API-Key": API_KEY,  
            "API-Sign": signature,  
            "API-Nonce": str(nonce),  
        }  
      
        response = requests.get(  
            f"{BASE_URL}{endpoint}",  
            headers=headers,  
            params=params,  
        )  
        return response.json()  
      
      
    methods = list_deposit_methods(user_id, "BTC")  
    for m in methods["result"]["methods"]:  
        print(f"{m['network']} (method_id: {m['method_id']})")  
    
    
    
    async function listDepositMethods(userId, asset) {  
      const endpoint = `/b2b/funds/deposits/methods/${asset}`;  
      const nonce = Date.now() * 1000000;  
      
      const params = { user: userId };  
      const signature = getPaywardSignature(endpoint, null, API_SECRET, nonce, params);  
      
      const url = `${BASE_URL}${endpoint}?user=${userId}`;  
      const response = await fetch(url, {  
        method: 'GET',  
        headers: {  
          'API-Key': API_KEY,  
          'API-Sign': signature,  
          'API-Nonce': String(nonce),  
        },  
      });  
      
      return response.json();  
    }  
      
    const methods = await listDepositMethods(userId, 'BTC');  
    for (const m of methods.result.methods) {  
      console.log(`${m.network} (method_id: ${m.method_id})`);  
    }  
    

#### Response Example
    
    
    {  
      "result": {  
        "methods": [  
          {  
            "method_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",  
            "network": "Bitcoin",  
            "fee": { "asset": "BTC", "amount": "0.00000000" },  
            "fee_percentage": "0.00",  
            "minimum": { "asset": "BTC", "amount": "0.00010000" },  
            "maximum": { "asset": "BTC", "amount": "100.00000000" },  
            "address_setup_fee": { "asset": "BTC", "amount": "0.00000000" },  
            "network_info": {  
              "explorer": "https://blockchair.com/bitcoin",  
              "confirmations": "3",  
              "est_confirmation_time": "45"  
            }  
          }  
        ]  
      }  
    }  
    

Key fields to display to users: `network`, `fee`, `minimum`, and `est_confirmation_time`.

### Step 2: Create a Deposit Address

Generate a deposit address using the `method_id` from Step 1. Display the address to the user so they can send crypto from an external wallet.

  * Python
  * JavaScript

    
    
    def create_deposit_address(user_id, asset, method_id):  
        endpoint = "/b2b/funds/deposits/addresses"  
        nonce = int(time.time() * 1000000000)  
      
        body = {  
            "asset": asset,  
            "method_id": method_id,  
        }  
      
        params = {"user": user_id}  
        signature = get_payward_signature(endpoint, body, API_SECRET, nonce, params)  
      
        headers = {  
            "API-Key": API_KEY,  
            "API-Sign": signature,  
            "API-Nonce": str(nonce),  
            "Content-Type": "application/json",  
        }  
      
        response = requests.post(  
            f"{BASE_URL}{endpoint}",  
            headers=headers,  
            params=params,  
            json=body,  
        )  
        return response.json()  
      
      
    address = create_deposit_address(  
        user_id, "BTC", "3fa85f64-5717-4562-b3fc-2c963f66afa6"  
    )  
    print(f"Deposit address: {address['result']['address']}")  
    
    
    
    async function createDepositAddress(userId, asset, methodId) {  
      const endpoint = '/b2b/funds/deposits/addresses';  
      const nonce = Date.now() * 1000000;  
      
      const body = {  
        asset: asset,  
        method_id: methodId,  
      };  
      
      const params = { user: userId };  
      const signature = getPaywardSignature(endpoint, body, API_SECRET, nonce, params);  
      
      const url = `${BASE_URL}${endpoint}?user=${userId}`;  
      const response = await fetch(url, {  
        method: 'POST',  
        headers: {  
          'API-Key': API_KEY,  
          'API-Sign': signature,  
          'API-Nonce': String(nonce),  
          'Content-Type': 'application/json',  
        },  
        body: JSON.stringify(body),  
      });  
      
      return response.json();  
    }  
      
    const address = await createDepositAddress(  
      userId, 'BTC', '3fa85f64-5717-4562-b3fc-2c963f66afa6'  
    );  
    console.log('Deposit address:', address.result.address);  
    

#### Response Example
    
    
    {  
      "result": {  
        "address": "bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh",  
        "name": "Bitcoin",  
        "tag": null,  
        "memo": null,  
        "expire_time": null,  
        "is_new": true  
      }  
    }  
    

note

Some networks (e.g., XRP, XLM) require a **tag** or **memo** in addition to the address. If `tag` or `memo` is present in the response, your UI must display it and instruct the user to include it when sending funds. Deposits sent without the required tag/memo may be lost.

### Step 3: List Deposit Addresses

Retrieve existing deposit addresses for a given asset and method. Use this to display previously generated addresses to users without creating new ones each time.

  * Python
  * JavaScript

    
    
    def list_deposit_addresses(user_id, asset, method_id, cursor=None):  
        endpoint = "/b2b/funds/deposits/addresses"  
        nonce = int(time.time() * 1000000000)  
      
        params = {  
            "user": user_id,  
            "asset": asset,  
            "method_id": method_id,  
        }  
        if cursor:  
            params["cursor"] = cursor  
      
        signature = get_payward_signature(endpoint, None, API_SECRET, nonce, params)  
      
        headers = {  
            "API-Key": API_KEY,  
            "API-Sign": signature,  
            "API-Nonce": str(nonce),  
        }  
      
        response = requests.get(  
            f"{BASE_URL}{endpoint}",  
            headers=headers,  
            params=params,  
        )  
        return response.json()  
      
      
    addresses = list_deposit_addresses(  
        user_id, "BTC", "3fa85f64-5717-4562-b3fc-2c963f66afa6"  
    )  
    for addr in addresses["result"]["addresses"]:  
        print(f"Address: {addr['address']}")  
    
    
    
    async function listDepositAddresses(userId, asset, methodId, cursor = null) {  
      const endpoint = '/b2b/funds/deposits/addresses';  
      const nonce = Date.now() * 1000000;  
      
      const params = { user: userId, asset, method_id: methodId };  
      if (cursor) params.cursor = cursor;  
      
      const signature = getPaywardSignature(endpoint, null, API_SECRET, nonce, params);  
      
      const searchParams = new URLSearchParams(params);  
      const url = `${BASE_URL}${endpoint}?${searchParams.toString()}`;  
      const response = await fetch(url, {  
        method: 'GET',  
        headers: {  
          'API-Key': API_KEY,  
          'API-Sign': signature,  
          'API-Nonce': String(nonce),  
        },  
      });  
      
      return response.json();  
    }  
      
    const addresses = await listDepositAddresses(  
      userId, 'BTC', '3fa85f64-5717-4562-b3fc-2c963f66afa6'  
    );  
    for (const addr of addresses.result.addresses) {  
      console.log('Address:', addr.address);  
    }  
    

#### Response Example
    
    
    {  
      "result": {  
        "addresses": [  
          {  
            "address": "bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh",  
            "tag": null,  
            "memo": null,  
            "method_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",  
            "asset": "BTC",  
            "fee": { "asset": "BTC", "amount": "0.00000000" },  
            "minimum": { "asset": "BTC", "amount": "0.00010000" },  
            "maximum": { "asset": "BTC", "amount": "100.00000000" },  
            "expire_time": null,  
            "last_deposit_at": null  
          }  
        ],  
        "next_cursor": null  
      }  
    }  
    

### Recommended UI Flow

### Best Practices

  1. **Always display tag/memo** : For networks that require a tag or memo (XRP, XLM, etc.), prominently display it alongside the address. Missing tags/memos can result in lost funds.
  2. **Set expectations** : Show `minimum` amounts and `est_confirmation_time` from the methods response so users know what to expect before sending funds.
  3. **Use fresh responses** : Available methods, addresses and limits are user-specific and may change based on account standing, remaining limits, or regional regulations. Fetch fresh data before displaying options rather than relying on cached results.

## Crypto Withdrawals

Withdrawals are key-based: you save an address once, then use its `key` in each withdrawal request.

### Withdrawal Workflow
    
    
    ┌────────────────────┐    ┌────────────────────┐    ┌────────────────────┐    ┌────────────────────┐    ┌──────────────────────┐  
    │ List Withdrawal    │──▶ │ Validate Address   │──▶ │ Save Address       │──▶ │ Preview / Submit   │──▶ │ Monitor Status       │  
    │ Methods            │    │ (optional)         │    │ (create key)       │    │ Withdrawal         │    │ (webhook / polling)  │  
    └────────────────────┘    └────────────────────┘    └────────────────────┘    └────────────────────┘    └──────────────────────┘  
     GET /funds/withdrawals/   POST /funds/withdrawals/   POST /funds/withdrawals/   POST /funds/withdrawals   withdrawal.status_updated  
          methods/{asset}            addresses/validate          addresses                                      + transaction polling  
1. **List Withdrawal Methods** : Fetch available networks, fees, limits, and `fee_token`.
  2. **Validate Address** : Pre-check address format for the selected method.
  3. **Save Withdrawal Address** : Store destination address under a partner-defined `key`.
  4. **Preview / Submit Withdrawal** : Use `preview=true` to quote fees, then submit with `preview=false`.
  5. **Monitor Status** : Track updates via webhooks or transaction polling.

### Step 1: List Withdrawal Methods

Call this first to determine valid `method_id`, fee estimates, limits, and optional `fee_token`.

  * Python
  * JavaScript

    
    
    def list_withdrawal_methods(user_id, asset):  
        endpoint = f"/b2b/funds/withdrawals/methods/{asset}"  
        nonce = int(time.time() * 1000000000)  
      
        params = {"user": user_id}  
        signature = get_payward_signature(endpoint, None, API_SECRET, nonce, params)  
      
        headers = {  
            "API-Key": API_KEY,  
            "API-Sign": signature,  
            "API-Nonce": str(nonce),  
        }  
      
        response = requests.get(  
            f"{BASE_URL}{endpoint}",  
            headers=headers,  
            params=params,  
        )  
        return response.json()  
    
    
    
    async function listWithdrawalMethods(userId, asset) {  
      const endpoint = `/b2b/funds/withdrawals/methods/${asset}`;  
      const nonce = Date.now() * 1000000;  
      
      const params = { user: userId };  
      const signature = getPaywardSignature(endpoint, null, API_SECRET, nonce, params);  
      
      const url = `${BASE_URL}${endpoint}?user=${userId}`;  
      const response = await fetch(url, {  
        method: 'GET',  
        headers: {  
          'API-Key': API_KEY,  
          'API-Sign': signature,  
          'API-Nonce': String(nonce),  
        },  
      });  
      
      return response.json();  
    }  
    

#### Response Example
    
    
    {  
      "result": {  
        "methods": [  
          {  
            "method_id": "00e4796b-a142-4589-a7c1-8927933788c9",  
            "network": "Bitcoin",  
            "fee": { "asset": "BTC", "amount": "0.00020000" },  
            "fee_token": "wft_abc123",  
            "minimum": { "asset": "BTC", "amount": "0.00050000" },  
            "maximum": { "asset": "BTC", "amount": "1.00000000" }  
          }  
        ]  
      }  
    }  
    

### Step 2: Validate Withdrawal Address (Recommended)

This endpoint validates the destination before you save it.

  * Python
  * JavaScript

    
    
    def validate_withdrawal_address(asset, method_id, address, memo=None):  
        endpoint = "/b2b/funds/withdrawals/addresses/validate"  
        nonce = int(time.time() * 1000000000)  
      
        body = {  
            "asset": asset,  
            "method_id": method_id,  
            "address": address,  
            "memo": memo,  
        }  
        signature = get_payward_signature(endpoint, body, API_SECRET, nonce)  
      
        headers = {  
            "API-Key": API_KEY,  
            "API-Sign": signature,  
            "API-Nonce": str(nonce),  
            "Content-Type": "application/json",  
        }  
      
        response = requests.post(  
            f"{BASE_URL}{endpoint}",  
            headers=headers,  
            json=body,  
        )  
        return response.json()  
    
    
    
    async function validateWithdrawalAddress(asset, methodId, address, memo = null) {  
      const endpoint = '/b2b/funds/withdrawals/addresses/validate';  
      const nonce = Date.now() * 1000000;  
      
      const body = { asset, method_id: methodId, address, memo };  
      const signature = getPaywardSignature(endpoint, body, API_SECRET, nonce);  
      
      const response = await fetch(`${BASE_URL}${endpoint}`, {  
        method: 'POST',  
        headers: {  
          'API-Key': API_KEY,  
          'API-Sign': signature,  
          'API-Nonce': String(nonce),  
          'Content-Type': 'application/json',  
        },  
        body: JSON.stringify(body),  
      });  
      
      return response.json();  
    }  
    

### Step 3: Save Withdrawal Address

Save the address once and keep the returned `key` for future withdrawals.

  * Python
  * JavaScript

    
    
    def save_withdrawal_address(user_id, asset, method_id, key, address, memo=None, tag=None):  
        endpoint = "/b2b/funds/withdrawals/addresses"  
        nonce = int(time.time() * 1000000000)  
      
        body = {  
            "asset": asset,  
            "method_id": method_id,  
            "key": key,  
            "address": address,  
            "memo": memo,  
            "tag": tag,  
        }  
        params = {"user": user_id}  
        signature = get_payward_signature(endpoint, body, API_SECRET, nonce, params)  
      
        headers = {  
            "API-Key": API_KEY,  
            "API-Sign": signature,  
            "API-Nonce": str(nonce),  
            "Content-Type": "application/json",  
        }  
      
        response = requests.post(  
            f"{BASE_URL}{endpoint}",  
            headers=headers,  
            params=params,  
            json=body,  
        )  
        return response.json()  
    
    
    
    async function saveWithdrawalAddress(userId, asset, methodId, key, address, memo = null, tag = null) {  
      const endpoint = '/b2b/funds/withdrawals/addresses';  
      const nonce = Date.now() * 1000000;  
      
      const body = { asset, method_id: methodId, key, address, memo, tag };  
      const params = { user: userId };  
      const signature = getPaywardSignature(endpoint, body, API_SECRET, nonce, params);  
      
      const url = `${BASE_URL}${endpoint}?user=${userId}`;  
      const response = await fetch(url, {  
        method: 'POST',  
        headers: {  
          'API-Key': API_KEY,  
          'API-Sign': signature,  
          'API-Nonce': String(nonce),  
          'Content-Type': 'application/json',  
        },  
        body: JSON.stringify(body),  
      });  
      
      return response.json();  
    }  
    

### Step 4: Preview and Submit a Withdrawal

Use `preview=true` to quote fees and totals without creating a withdrawal, then submit with `preview=false`.

  * Python
  * JavaScript

    
    
    def withdraw_funds(user_id, asset, key, amount, idempotency_token, preview=False, fee_token=None):  
        endpoint = "/b2b/funds/withdrawals"  
        nonce = int(time.time() * 1000000000)  
      
        body = {  
            "asset": asset,  
            "key": key,  
            "amount": amount,  
            "idempotency_token": idempotency_token,  
            "preview": preview,  
            "fee_token": fee_token,  
        }  
        params = {"user": user_id}  
        signature = get_payward_signature(endpoint, body, API_SECRET, nonce, params)  
      
        headers = {  
            "API-Key": API_KEY,  
            "API-Sign": signature,  
            "API-Nonce": str(nonce),  
            "Content-Type": "application/json",  
        }  
      
        response = requests.post(  
            f"{BASE_URL}{endpoint}",  
            headers=headers,  
            params=params,  
            json=body,  
        )  
        return response.json()  
    
    
    
    async function withdrawFunds(userId, asset, key, amount, idempotencyToken, preview = false, feeToken = null) {  
      const endpoint = '/b2b/funds/withdrawals';  
      const nonce = Date.now() * 1000000;  
      
      const body = {  
        asset,  
        key,  
        amount,  
        idempotency_token: idempotencyToken,  
        preview,  
        fee_token: feeToken,  
      };  
      const params = { user: userId };  
      const signature = getPaywardSignature(endpoint, body, API_SECRET, nonce, params);  
      
      const url = `${BASE_URL}${endpoint}?user=${userId}`;  
      const response = await fetch(url, {  
        method: 'POST',  
        headers: {  
          'API-Key': API_KEY,  
          'API-Sign': signature,  
          'API-Nonce': String(nonce),  
          'Content-Type': 'application/json',  
        },  
        body: JSON.stringify(body),  
      });  
      
      return response.json();  
    }  
    

#### Statuses

Status| Description  
---|---  
`pending`| Withdrawal detected and being processed  
`held`| Held for review  
`success`| Completed successfully  
`failure`| Failed (terminal)  
  
### Withdrawal Best Practices

  1. **Use idempotency tokens** : Always generate a unique `idempotency_token` per intended withdrawal to avoid duplicate sends on retries.
  2. **Preview first** : Run a preview request immediately before submit so users can confirm `amount`, `fee`, and `total`.
  3. **Refresh expired fee tokens** : `fee_token` values are short-lived. If a withdrawal is rejected due to an expired/invalid token, fetch withdrawal methods again (or run a fresh preview) to get a new `fee_token` and retry.
  4. **Persist key ownership** : Store which `key` belongs to each user and enforce access checks in your app.
  5. **Handle memo/tag networks** : For XRP/XLM-like networks, capture and persist memo/tag fields when addresses are saved.
  6. **Monitor with webhooks** : Subscribe to `withdrawal.status_updated` and reconcile events against your internal withdrawal records.

### Common Errors

Error| Cause| Solution  
---|---|---  
`EGeneral:Bad data`| Invalid payload (for example malformed key or amount)| Validate request payload before sending  
`ENexus:Unknown asset`| Asset not recognized| Verify the asset code (e.g., `BTC`, `ETH`)  
`EFunding:Unknown withdraw key`| Saved key not found| Re-list addresses and use an existing key  
`EFunding:Duplicate withdraw key`| Key already exists when saving/updating| Choose a unique key per saved address  
  
## API Reference

Endpoint| Method| Description  
---|---|---  
`/b2b/funds/deposits/methods/{asset}`| GET| List deposit methods for an asset  
`/b2b/funds/deposits/addresses`| POST| Create a new deposit address  
`/b2b/funds/deposits/addresses`| GET| List existing deposit addresses  
`/b2b/funds/withdrawals/methods/{asset}`| GET| List withdrawal methods for an asset  
`/b2b/funds/withdrawals/addresses/validate`| POST| Validate a withdrawal address without saving it  
`/b2b/funds/withdrawals/addresses`| POST| Save a withdrawal address  
`/b2b/funds/withdrawals/addresses`| GET| List saved withdrawal addresses  
`/b2b/funds/withdrawals/addresses/{key}`| PATCH| Rename a saved withdrawal key  
`/b2b/funds/withdrawals/addresses/{key}`| DELETE| Delete a saved withdrawal address  
`/b2b/funds/withdrawals`| POST| Preview or submit a withdrawal  
`/b2b/webhooks`| POST| Register for `deposit.status_updated` and `withdrawal.status_updated` webhooks  
* Prerequisites
  * Crypto Deposits
* Deposit Workflow
* Step 1: List Deposit Methods
* Step 2: Create a Deposit Address
* Step 3: List Deposit Addresses
* Recommended UI Flow
* Best Practices
  * Crypto Withdrawals
* Withdrawal Workflow
* Step 1: List Withdrawal Methods
* Step 2: Validate Withdrawal Address (Recommended)
* Step 3: Save Withdrawal Address
* Step 4: Preview and Submit a Withdrawal
* Withdrawal Best Practices
* Common Errors
  * API Reference