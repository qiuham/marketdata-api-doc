---
api_type: reference
source_type: llms_txt
version: ''
scope: crypto
asset_class: digital_asset
domain: exchanges
provider: bitfinex
provider_name: Bitfinex
product: api
product_id: bitfinex
source_url: 'https://docs.bitfinex.com/recipes/restpython-authenticated-request-example'
updated_at: 2026-11-22
---

# [REST][Python] Authenticated request example

```python Python 3.0+
from datetime import datetime
import os, json, hmac, hashlib
import requests

API = "https://api.bitfinex.com/v2"

API_KEY, API_SECRET = (
    os.getenv("BFX_API_KEY"),
    os.getenv("BFX_API_SECRET")
)

def _build_authentication_headers(endpoint, payload = None):
    nonce = str(round(datetime.now().timestamp() * 1_000))

    message = f"/api/v2/{endpoint}{nonce}"

    if payload != None:
        message += json.dumps(payload)

    signature = hmac.new(
        key=API_SECRET.encode("utf8"),
        msg=message.encode("utf8"),
        digestmod=hashlib.sha384
    ).hexdigest()

    return {
        "bfx-apikey": API_KEY,
        "bfx-nonce": nonce,
        "bfx-signature": signature
    }
  
endpoint = "auth/w/order/submit"

payload = {
    "type": "EXCHANGE LIMIT",
    "symbol": "tBTCUSD",
    "amount": "0.165212",
    "price": "30264.0"
}

headers = {
    "Content-Type": "application/json",
    **_build_authentication_headers(endpoint, payload)
}

response = requests.post(f"{API}/{endpoint}", json=payload, headers=headers)
```

# Choose an HTTP library

<!-- python@3 -->

We suggest using [requests](https://pypi.org/project/requests/) to handle your HTTP requests, but you can use whatever library you want.

You can install the latest version of the library by running the following command:
```bash
python3 -m pip install requests
```

# Store your API-KEY and API-SECRET

<!-- python@7-10,27 -->

To authenticate in your Bitfinex account, you will need a valid API-KEY and API-SECRET (see [How to create and revoke a Bitfinex API Key](https://support.bitfinex.com/hc/en-us/articles/115003363429-How-to-create-and-revoke-a-Bitfinex-API-Key)).

We recommend storing these values in a safe place, such as a local .env (accessing them as environment variables).

# Build the authentication headers

<!-- python@12-30 -->

To authenticate your HTTP requests, you must provide and attach the following triplet of headers:
• bfx-apikey
• bfx-nonce
• bfx-signature

To build these 3 headers, you'll also need the endpoint you're sending the request to and the JSON string that serializes your POST data (if there are any).

This is a step-by-step procedure that you will have to perform every time you are about to send a new HTTP request.

# Generate a valid bfx-nonce

<!-- python@13,27 -->

A nonce is an ever-increasing, single use value which identifies your authentication attempts.

Providing a nonce smaller than that of the last authentication attempt will cause an error to be thrown.

To automatically generate a nonce, users can use the current milliseconds since Unix Epoch (milliseconds since 1970/01/01).

# Compute the signature's message

<!-- python@15-18 -->

This message consists of the URL path + the authentication attempt's bfx-nonce + the JSON string that serializes your POST data (if there are any).

The next step will be signing this string using the HMAC-SHA384 algorithm before providing it in the bfx-signature header.

# Encrypt the message using HMAC-SHA384

<!-- python@20-24,29 -->

You can use the `hmac` and `hashlib` packages to sign the message through the HMAC-SHA384 algorithm.

The starting key for the hash must be equal to your API-SECRET (which must match with the API-KEY you'll provide in the bfx-apikey header).

# Attach the headers to your HTTP request

<!-- python@5,32-46 -->

Before sending your HTTP request, be sure to attach the three headers you have previously built.

If you are sending some POST data within the request, remember to also add the header `"Content-Type": "application/json"`.

You are now ready to try it out!

> **NOTE:** You must generate a unique triplet of headers before sending each of your HTTP requests.
