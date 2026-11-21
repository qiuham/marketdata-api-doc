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
source_url: 'https://docs.bitfinex.com/recipes/restjavascript-authenticated-request-example'
updated_at: 2026-11-21
---

# [REST][Javascript] Authenticated request example

```javascript JavaScript
const crypto = require('crypto') 
const fetch = require('node-fetch') //v2.x

const apiKey = '' // const apiKey = 'paste key here'
const apiSecret = '' // const apiSecret = 'paste secret here'

const apiPath = 'v2/auth/w/order/submit'

const nonce = (Date.now() * 1000).toString() 
const body = {
  type: 'LIMIT',
  symbol: 'tBTCUSD',
  price: '15',
  amount: '0.1'
} 

const signaturePayload = `/api/${apiPath}${nonce}${JSON.stringify(body)}` 
const signature = crypto.createHmac('sha384', apiSecret)
  .update(signaturePayload).digest('hex') 

fetch(`https://api.bitfinex.com/${apiPath}`, {
  method: 'POST',
  body: JSON.stringify(body),
  headers: {
    'Content-Type': 'application/json',
    'bfx-nonce': nonce,
    'bfx-apikey': apiKey,
    'bfx-signature': signature
  }
})
.then(res => res.json())
.then(json => console.log(json))
.catch(err => {
    console.log(err)
 })
```

```json Response Example
[
  1682684859,
  'on-req',
  null,
  null,
  [
    [
      1867202615, null,          1682684859447,
      'tBTCUSD',  1682684859447, 1682684859447,
      0.1,        0.1,           'LIMIT',
      null,       null,          null,
      0,          'ACTIVE',      null,
      null,       15,            0,
      0,          0,             null,
      null,       null,          0,
      0,          null,          null,
      null,       'API>BFX',     null,
      null,       {}
    ]
  ],
  null,
  'SUCCESS',
  'Submitting 1 orders.'
]
```

# Libraries

<!-- javascript@1,2 -->

This example uses the native crypto library to hash the signature using the HmacSHA384 algorithm.

This example uses the node-fetch library to perform HTTP requests.

Other libraries with the same functionality can also be used.

# API keys

<!-- javascript@4,5 -->

Authenticated requests require a pair of API keys. You can generate these keys in your account settings: https://setting.bitfinex.com/api#new-key

# Endpoint

<!-- javascript@7 -->

Setting the path determines which endpoint you are calling. Path variables are appended to the path.

# Nonce

<!-- javascript@9 -->

A nonce needs to be passed in your request. The only requirement for the nonce is that it needs to increase between subsequent requests. 

This example code generates a nonce based on the current UNIX timestamp to ensure an increasing value between subsequent requests.

# Body parameters

<!-- javascript@10-15 -->

Body parameters can be added depending on the endpoint. The documentation provides a list of required and available body parameters for each endpoint. 

This example includes the body parameters required to submit an order. The documentation with all the available body parameters for this endpoint can be found here: https://docs.bitfinex.com/reference/rest-auth-submit-order

# Signature

<!-- javascript@17 -->

A signaturePayload is created by joining '/api/', the apiPath, the nonce, and a JSON string of the body object.

# Signature hash

<!-- javascript@18,19 -->

The signature is hashed using the private key and the HmacSHA384 algorithm

# Sending the request

<!-- javascript@21-30 -->

The fetch request has two variables: the URL string and a data object.

# Fetch URL

<!-- javascript@21 -->

The request URL is built by appending the endpoint path ('v2/auth/w/order/submit', in this example) to the base URL used for authenticated requests ('https://api.bitfinex.com/')

# Data object

<!-- javascript@22-29 -->

The data object includes a method, body, and headers object.

Any authenticated request will be a POST request.

The request body is included in the data object as a JSON string.

The headers object needs to include the Content-Type ('application/json'), the nonce, the public api key, and the hashed signature.

# Response

<!-- javascript@31,32 -->

The response is converted to JSON and logged to the console.

# Error handling

<!-- javascript@33-35 -->

.catch() is used to handle and log any errors.
