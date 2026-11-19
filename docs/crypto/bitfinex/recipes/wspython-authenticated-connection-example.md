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
source_url: 'https://docs.bitfinex.com/recipes/wspython-authenticated-connection-example'
updated_at: 2026-11-19
---

# [WS][Python] Authenticated connection example

```python Python 3.0+
from websockets.sync.client import connect
from datetime import datetime
import os, json, hmac, hashlib

URI = "wss://api.bitfinex.com/ws/2"

API_KEY, API_SECRET = (
    os.getenv("BFX_API_KEY"),
    os.getenv("BFX_API_SECRET")
)

def _build_authentication_message(api_key, api_secret):
    message = { "event": "auth" }
    
    message["apiKey"] = api_key

    message["authNonce"] = round(datetime.now().timestamp() * 1_000)

    message["authPayload"] = f"AUTH{message['authNonce']}"

    message["authSig"] = hmac.new(
        key=api_secret.encode("utf8"),
        msg=message["authPayload"].encode("utf8"),
        digestmod=hashlib.sha384
    ).hexdigest()

    return json.dumps(message)

with connect(URI) as websocket:
    websocket.send( \
        _build_authentication_message(API_KEY, API_SECRET))

    for message in websocket:
        data = json.loads(message)

        if isinstance(data, dict):
            if data["event"] == "auth":
                if data["status"] != "OK":
                    raise Exception("Cannot authenticate with given API-KEY and API-SECRET.")

                print(f"Successful login for user <{data['userId']}>.")
```

# Choose a WebSocket client library

<!-- python@1 -->

We suggest using [websockets](https://pypi.org/project/websockets/) to build your WebSocket client, but you can use whatever library you prefer (an alternative could be [websocket-client](https://pypi.org/project/websocket-client/)).

You can install the latest version of **websockets** by executing the following command in your terminal:
```bash
python3 -m pip install websockets
```

# Store your API-KEY and API-SECRET

<!-- python@7-10,15 -->

To authenticate in your Bitfinex account, you will need a valid API-KEY and API-SECRET (see [How to create and revoke a Bitfinex API Key](https://support.bitfinex.com/hc/en-us/articles/115003363429-How-to-create-and-revoke-a-Bitfinex-API-Key)).

We recommend storing these values in a safe place, such as a local .env (accessing them as environment variables).

# Build the authentication message

<!-- python@12-27 -->

To authenticate your WebSocket client, you must send a specific authentication message to the server.

This message must be sent as a JSON string and should contain all of the following properties:
• event
• apiKey
• authNonce
• authPayload
• authSig

You'll need to perform this step-by-step procedure once per connection, the session will only expire when the client disconnects.

> **NOTE:** The event property indicates an authentication attempt and should always be set to "auth".

# Generate a valid authNonce

<!-- python@17 -->

A nonce is an ever-increasing, single use value which identifies your authentication attempts.

Providing a nonce smaller than that of the last authentication attempt will cause an error to be thrown.

To automatically generate a nonce, users can use the current milliseconds since Unix Epoch (milliseconds since 1970/01/01).

# Compute the message's payload

<!-- python@19 -->

The payload simply consists of the "AUTH" prefix + the authNonce value (e.g. "AUTH1685659782288").

In the next step you will sign this string using HMAC-SHA384 to compute a valid signature for the authSig property.

# Encrypt the payload using HMAC-SHA384

<!-- python@21-25 -->

You can use the `hmac` and `hashlib` packages to sign the payload through the HMAC-SHA384 algorithm.

The starting key for the hash must be equal to your API-SECRET (which must match with the API-KEY you'll assign to the `apiKey` property).

# Connect and send the authentication message

<!-- python@5,29-37 -->

After connecting to the WebSocket server, be sure to send the authentication message you have built to gain access to your account.

Authentication will not be complete until the server sends an acknowledgment message back to the client.

Users can identify this message via its event property, which will always be set to "auth".

# Check if authentication is successful

<!-- python@38-41 -->

You can use the message sent back to the client to check if the authentication attempt has been successful.

If the status property is set to "OK" then the authentication was successful and the WebSocket client now has access to your Bitfinex account.

If it is set to "FAILED" then the server couldn't accept the credentials as valid and complete the authentication.

In the case of a failure, a description of the error can be found in the properties code and msg (e.g. `10100` and `apikey: digest invalid`).

You are now ready to try it out!
