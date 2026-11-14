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
source_url: 'https://docs.kraken.com/exchange/guides/rest/authentication'
updated_at: 2026-11-13
---

# Spot REST Authentication

> HMAC-SHA512 signature generation, nonce management, API-Key header, and two-factor authentication for the Spot REST API

## Authentication Parameters

For the REST API, the following parameters are used for authentication to endpoints which contain private data:

* `API-Key` HTTP header parameter: the public key from your API key-pair.
* `API-Sign` HTTP header parameter: encrypted signature of message.
* `nonce` payload parameter: always increasing, unsigned 64-bit integer.
* `otp` payload parameter: one-time-password and is only required if additional 2FA is configured for API.

## Setting the API-Key Parameter

The value for the `API-Key` HTTP header parameter is your **public** API key.

An API key-pair is required to access the authenticated endpoints, see [How to Create an API Key](https://support.kraken.com/hc/en-us/articles/360000919966-How-to-create-an-API-key).

> [!WARNING]
>
> From your API key-pair, clearly identify which key is public and which key is private.
>
> * The **public** key is sent in the `API-Key` header parameter.
> * The **private** key is **never** sent, it is only used to encode the signature for `API-Sign` header parameter.

## Setting the API-Sign Parameter

The value for the `API-Sign` HTTP header parameter is a signature generated from encoding your **private** API key, nonce, encoded payload, and URI path.

```text theme={null}
  HMAC-SHA512 of (URI path + SHA256(nonce + POST data)) and base64 decoded secret API key
```

Note: The URI path used for API-Sign should be the part starting with "/0/private" of the API URL.

### Examples

The following is a specific example of a signature generated with a particular private key, nonce, and payload corresponding to a new limit order (buy 1.25 XBTUSD at \$37,500).If your code is generating a different signature (`API-Sign`) for this example, then there is likely an issue with your application of the above methodology. Code snippets for generating the signature in Python, Golang and Node.js follow below.

| Field | Value |
| - | :- |
| Private Key | kQH5HW/8p1uGOVjbgWA7FunAmGO8lsSUXNsu3eow76sz84Q18fWxnyRzBHCd3pd5nE9qa99HAZtuZuj6F1huXg== |
| Nonce | 1616492376594 |
| Encoded Payload | nonce=1616492376594\&ordertype=limit\&pair=XBTUSD\&price=37500\&type=buy\&volume=1.25 |
| URI Path | /0/private/AddOrder |
| **API-Sign** | **4/dpxb3iT4tp/ZCVEwSnEsLxx0bqyhLpdfOpc6fn7OR8+UClSV5n9E6aSS8MPtnRfp32bAb0nmbRn6H8ndwLUQ==** |

> [tab] Python
>
> ```py theme={null}
> import urllib.parse
> import hashlib
> import hmac
> import base64
>
> def get_kraken_signature(urlpath, data, secret):
>
>     if isinstance(data, str):
>         encoded = (str(json.loads(data)["nonce"]) + data).encode()
>     else:
>         encoded = (str(data["nonce"]) + urllib.parse.urlencode(data)).encode()
>     message = urlpath.encode() + hashlib.sha256(encoded).digest()
>
>     mac = hmac.new(base64.b64decode(secret), message, hashlib.sha512)
>     sigdigest = base64.b64encode(mac.digest())
>     return sigdigest.decode()
>
> api_sec = "kQH5HW/8p1uGOVjbgWA7FunAmGO8lsSUXNsu3eow76sz84Q18fWxnyRzBHCd3pd5nE9qa99HAZtuZuj6F1huXg=="
>
> payload = {
>         "nonce": "1616492376594",
>         "ordertype": "limit",
>         "pair": "XBTUSD",
>         "price": 37500,
>         "type": "buy",
>         "volume": 1.25
>         }
>
> signature = get_kraken_signature("/0/private/AddOrder", payload, api_sec)
> print("API-Sign: {}".format(signature))
>
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
>     "net/url"
>     "fmt"
>     "encoding/json"
>     "strings"
>
>     )
>
>     func getKrakenSignature(urlPath string, data interface{}, secret string) (string, error) {
>         var encodedData string
>
>         switch v := data.(type) {
>         case string:
>             var jsonData map[string]interface{}
>             if err := json.Unmarshal([]byte(v), &jsonData); err != nil {
>                 return "", err
>             }
>             encodedData = jsonData["nonce"].(string) + v
>         case map[string]interface{}:
>             dataMap := url.Values{}
>             for key, value := range v {
>                 dataMap.Set(key, fmt.Sprintf("%v", value))
>             }
>             encodedData = v["nonce"].(string) + dataMap.Encode()
>         default:
>             return "", fmt.Errorf("invalid data type")
>         }
>         sha := sha256.New()
>         sha.Write([]byte(encodedData))
>         shaSum := sha.Sum(nil)
>
>         message := append([]byte(urlPath), shaSum...)
>         secretDecoded, err := base64.StdEncoding.DecodeString(secret)
>         if err != nil {
>             return "", err
>         }
>         mac := hmac.New(sha512.New, secretDecoded)
>         mac.Write(message)
>         macSum := mac.Sum(nil)
>         sigDigest := base64.StdEncoding.EncodeToString(macSum)
>         return sigDigest, nil
>     }
>
>     func main() {
>
>         apiSecret := "kQH5HW/8p1uGOVjbgWA7FunAmGO8lsSUXNsu3eow76sz84Q18fWxnyRzBHCd3pd5nE9qa99HAZtuZuj6F1huXg=="
>
>         payload := map[string]interface{}{
>             "nonce":     "1616492376594",
>             "ordertype": "limit",
>             "pair":      "XBTUSD",
>             "price":     37500,
>             "type":      "buy",
>             "volume":    1.25,
>         }
>
>         signature, err := getKrakenSignature("/0/private/AddOrder", payload, apiSecret)
>         if err != nil {
>             fmt.Println("Error generating signature:", err)
>             return
>         }
>         fmt.Printf("API-Sign: %s\n", signature)
>     }
> ```

> [tab] Node JS
>
> ```js theme={null}
> const crypto = require('crypto');
> const querystring = require('querystring');
>
> // Function to get Kraken signature
> function getKrakenSignature(urlPath, data, secret) {
>   let encoded;
>   if (typeof data === 'string') {
>     const jsonData = JSON.parse(data);
>     encoded = jsonData.nonce + data;
>   } else if (typeof data === 'object') {
>     const dataStr = querystring.stringify(data);
>     encoded = data.nonce + dataStr;
>   } else {
>     throw new Error('Invalid data type');
>   }
>
>   const sha256Hash = crypto.createHash('sha256').update(encoded).digest();
>   const message = urlPath + sha256Hash.toString('binary');
>   const secretBuffer = Buffer.from(secret, 'base64');
>   const hmac = crypto.createHmac('sha512', secretBuffer);
>   hmac.update(message, 'binary');
>   const signature = hmac.digest('base64');
>   return signature;
> }
>
> const apiSec = 'kQH5HW/8p1uGOVjbgWA7FunAmGO8lsSUXNsu3eow76sz84Q18fWxnyRzBHCd3pd5nE9qa99HAZtuZuj6F1huXg==';
>
> const payload = {
>   nonce: '1616492376594',
>   ordertype: 'limit',
>   pair: 'XBTUSD',
>   price: 37500,
>   type: 'buy',
>   volume: 1.25,
> };
>
> const signature = getKrakenSignature('/0/private/AddOrder', payload, apiSec);
> console.log(`API-Sign: ${signature}`);
> ```

## Setting the nonce Parameter

The value for the `nonce` payload body parameter is an always increasing, unsigned 64-bit integer for each request that is made with a particular API key.

While a simple counter would provide a valid nonce, a more usual method of generating a valid nonce is to use e.g. a UNIX timestamp in milliseconds. There is no way to reset the nonce for an API key to a lower value, so be sure to use a nonce generation method that won't produce numbers less than the previous nonce.

Too many requests with invalid nonces (EAPI:Invalid nonce) can result in temporary bans.

Problems can arise from requests arriving out of order due to API keys being shared across processes, or from system clock drift/recalibration. An optional "nonce window" can be configured to specify a tolerance between nonce values.

Additional info can be found in our [support pages](https://support.kraken.com/hc/en-us/articles/360000906023-What-is-a-nonce-).

### Examples

The following are some examples of how to generate valid millisecond resolution nonce values in different programming languages:

> [tab] Python
>
> ```py theme={null}
> import time
>
> api_nonce = str(int(time.time() * 1000))
> ```

> [tab] Go
>
> ```go theme={null}
> import (
>     "fmt"
>     "time"
> )
>
> apiNonce := fmt.Sprintf("%d", time.Now().UnixMilli())
> ```

> [tab] Node JS
>
> ```js theme={null}
> const apiNonce = Date.now().toString();
> ```

## Setting the otp Parameter

The optional value for the `otp` payload body parameter is your one-time-password.

This parameter is only required if two-factor authentication (2FA) is enabled for the API key and action in question. The 2FA authentication is not needed for Websocket and FIX APIs.
