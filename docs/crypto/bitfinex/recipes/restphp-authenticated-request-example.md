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
source_url: 'https://docs.bitfinex.com/recipes/restphp-authenticated-request-example'
updated_at: 2026-11-18
---

# [REST][PHP] Authenticated request example

```php PHP
<?php

require __DIR__ . '/vendor/autoload.php';

$baseUrl = 'https://api.bitfinex.com';
$client = new GuzzleHttp\Client([
  'base_uri' => $baseUrl,
  'timeout' => 3.0,
]);

$apiKey = '';
$apiSecret = '';

$apiPath = 'v2/auth/w/order/submit';

$nonce = (string) (time() * 1000 * 1000); // epoch in ms * 1000
$body = [
  'type' => 'LIMIT',
  'symbol' => 'tBTCUSD',
  'price' => '15',
  'amount' => '0.1',
];
$bodyJson = json_encode($body, JSON_UNESCAPED_SLASHES);

$sigPayload = "/api/{$apiPath}{$nonce}{$bodyJson}";
$sig = hash_hmac('sha384', $sigPayload, $apiSecret);

$headers = [
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'bfx-nonce' => $nonce,
  'bfx-apikey' => $apiKey,
  'bfx-signature' => $sig,
];

try {
  $r = $client->post($apiPath, [
    'headers' => $headers,
    'body' => $bodyJson,
  ]);
  $response = $r->getBody()->getContents();
  print_r(json_decode($response));
} catch (\Throwable $ex) {
  print_r($ex->getMessage());
}

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

<!-- php@3 -->

This example uses guzzle http library for making http requests and the native hash_hmac function to hash the signature using the HmacSHA384 algorithm.

# Client setup

<!-- php@5-9 -->

As first step we need to setup a new guzzle client with base url pointing to bitfinex api. Additionally in setup we can define default timeout e.g. 3s

# API Keys

<!-- php@11-12 -->

Authenticated requests require a pair of API keys. You can generate these keys in your account settings: https://setting.bitfinex.com/api#new-key

# Endpoint

<!-- php@14 -->

Setting the path determines which endpoint you are calling. Path variables are appended to the path.

# Nonce

<!-- php@16 -->

A nonce needs to be passed in your request. The only requirement for the nonce is that it needs to increase between subsequent requests.

This example code generates a nonce based on the current UNIX timestamp to ensure an increasing value between subsequent requests.

# Body parameters

<!-- php@17-23 -->

Body parameters can be added depending on the endpoint. The documentation provides a list of required and available body parameters for each endpoint.

This example includes the body parameters required to submit an order. The documentation with all the available body parameters for this endpoint can be found here: https://docs.bitfinex.com/reference/rest-auth-submit-order

# Signature

<!-- php@25 -->

A signature payload is created by joining '/api/', the apiPath, the nonce, and a JSON string of the body object.

# Signature hash

<!-- php@26 -->

The signature is hashed using the private key and the HmacSHA384 algorithm

# Prepare request headers

<!-- php@28-34 -->

In case of auth request we need to send json content type and include authentication headers (bfx-nonce, bfx-apikey, bfx-signature)

# Sending the request

<!-- php@37-40 -->



# Handling the response

<!-- php@41-42 -->

The response is always json and we need to parse the raw response from string to json object

# Error handling

<!-- php@43-45 -->

Sometimes requests might fail so guzzle requests should be caught
