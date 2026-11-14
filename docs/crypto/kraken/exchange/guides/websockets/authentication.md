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
source_url: 'https://docs.kraken.com/exchange/guides/websockets/authentication'
updated_at: 2026-11-13
---

# Spot WebSocket Authentication

> How to obtain a WebSocket authentication token via the REST API and use it to subscribe to private channels

## Overview

The Spot WebSocket API uses token-based authentication. To subscribe to private channels (`ownTrades`, `openOrders`), first obtain a short-lived token via the REST API, then include it in each subscription message.

> [!NOTE]
>
> Tokens are valid for **15 minutes**. Obtain a fresh token before reconnecting or when the current one nears expiry.

## Step 1: Obtain a WebSocket token

Call the [GetWebSocketsToken](https://docs.kraken.com/api-reference/trading/get-websockets-token.md) REST endpoint using your API key and secret. Authentication uses the same HMAC-SHA512 signing as all other private REST endpoints — see [REST Authentication](https://docs.kraken.com/exchange/guides/rest/authentication.md) for the full algorithm.

> [tab] Python
>
> ```py theme={null}
> import urllib.parse
> import hashlib
> import hmac
> import base64
> import time
> import requests
>
> def get_kraken_signature(urlpath, data, secret):
>     encoded = (str(data["nonce"]) + urllib.parse.urlencode(data)).encode()
>     message = urlpath.encode() + hashlib.sha256(encoded).digest()
>     mac = hmac.new(base64.b64decode(secret), message, hashlib.sha512)
>     return base64.b64encode(mac.digest()).decode()
>
> api_key = "YOUR_API_KEY"
> api_secret = "YOUR_API_SECRET"
>
> nonce = str(int(time.time() * 1000))
> data = {"nonce": nonce}
>
> headers = {
>     "API-Key": api_key,
>     "API-Sign": get_kraken_signature("/0/private/GetWebSocketsToken", data, api_secret),
> }
>
> response = requests.post(
>     "https://api.kraken.com/0/private/GetWebSocketsToken",
>     headers=headers,
>     data=data,
> )
> token = response.json()["result"]["token"]
> print(f"Token: {token}")
> ```

> [tab] Go
>
> ```go theme={null}
> package main
>
> import (
>     "crypto/hmac"
>     "crypto/sha256"
>     "crypto/sha512"
>     "encoding/base64"
>     "encoding/json"
>     "fmt"
>     "io"
>     "net/http"
>     "net/url"
>     "strings"
>     "time"
> )
>
> func getKrakenSignature(urlPath string, data url.Values, secret string) (string, error) {
>     nonce := data.Get("nonce")
>     encoded := nonce + data.Encode()
>     sha := sha256.Sum256([]byte(encoded))
>     message := append([]byte(urlPath), sha[:]...)
>     secretDecoded, err := base64.StdEncoding.DecodeString(secret)
>     if err != nil {
>         return "", err
>     }
>     mac := hmac.New(sha512.New, secretDecoded)
>     mac.Write(message)
>     return base64.StdEncoding.EncodeToString(mac.Sum(nil)), nil
> }
>
> func main() {
>     apiKey := "YOUR_API_KEY"
>     apiSecret := "YOUR_API_SECRET"
>
>     nonce := fmt.Sprintf("%d", time.Now().UnixMilli())
>     data := url.Values{"nonce": {nonce}}
>
>     sig, err := getKrakenSignature("/0/private/GetWebSocketsToken", data, apiSecret)
>     if err != nil {
>         panic(err)
>     }
>
>     req, _ := http.NewRequest("POST",
>         "https://api.kraken.com/0/private/GetWebSocketsToken",
>         strings.NewReader(data.Encode()))
>     req.Header.Set("API-Key", apiKey)
>     req.Header.Set("API-Sign", sig)
>     req.Header.Set("Content-Type", "application/x-www-form-urlencoded")
>
>     resp, err := http.DefaultClient.Do(req)
>     if err != nil {
>         panic(err)
>     }
>     defer resp.Body.Close()
>
>     body, _ := io.ReadAll(resp.Body)
>     var result struct {
>         Result struct {
>             Token string `json:"token"`
>         } `json:"result"`
>     }
>     json.Unmarshal(body, &result)
>     fmt.Printf("Token: %s\n", result.Result.Token)
> }
> ```

> [tab] Node.js
>
> ```js theme={null}
> const crypto = require('crypto');
> const querystring = require('querystring');
>
> function getKrakenSignature(urlPath, data, secret) {
>   const encoded = data.nonce + querystring.stringify(data);
>   const sha256Hash = crypto.createHash('sha256').update(encoded).digest();
>   const message = urlPath + sha256Hash.toString('binary');
>   const secretBuffer = Buffer.from(secret, 'base64');
>   const hmac = crypto.createHmac('sha512', secretBuffer);
>   hmac.update(message, 'binary');
>   return hmac.digest('base64');
> }
>
> async function getWebSocketToken(apiKey, apiSecret) {
>   const nonce = Date.now().toString();
>   const data = { nonce };
>
>   const signature = getKrakenSignature('/0/private/GetWebSocketsToken', data, apiSecret);
>
>   const response = await fetch('https://api.kraken.com/0/private/GetWebSocketsToken', {
>     method: 'POST',
>     headers: {
>       'API-Key': apiKey,
>       'API-Sign': signature,
>       'Content-Type': 'application/x-www-form-urlencoded',
>     },
>     body: new URLSearchParams(data),
>   });
>
>   const result = await response.json();
>   return result.result.token;
> }
>
> const token = await getWebSocketToken('YOUR_API_KEY', 'YOUR_API_SECRET');
> console.log('Token:', token);
> ```

## Step 2: Subscribe to a private channel

Include the token in your WebSocket subscription message:

```json theme={null}
{
  "event": "subscribe",
  "subscription": {
    "name": "ownTrades",
    "token": "WW91ciBhdXRoZW50aWNhdGlvbiB0b2tlbiBnb2VzIGhlcmUu"
  }
}
```

A single token can be used for multiple subscriptions within the same session (e.g., subscribing to both `ownTrades` and `openOrders` simultaneously).

## Token expiry and refresh

Tokens expire **15 minutes** after creation. To maintain uninterrupted access:

* Obtain a new token before the current one expires by calling `GetWebSocketsToken` again
* After reconnecting, re-subscribe using the fresh token

For WebSocket reconnection patterns and session management, see the [Reconnection guide](https://docs.kraken.com/exchange/guides/websockets/reconnection.md).

## Error handling

If you subscribe with an invalid or expired token, the server returns an error in the subscription status message:

```json theme={null}
{
  "errorMessage": "Token is expired",
  "event": "subscriptionStatus",
  "status": "error",
  "subscription": { "name": "ownTrades" }
}
```

On receiving this error, call `GetWebSocketsToken` to obtain a fresh token, then re-subscribe.
