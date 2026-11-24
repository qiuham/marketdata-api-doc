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
source_url: 'https://docs.bitfinex.com/recipes/restjava-authenticated-request-example'
updated_at: 2026-11-24
---

# [REST][Java] Authenticated request example

```java Java
package com.bitfinex.program;

import java.util.Date;

import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;

import com.google.gson.GsonBuilder;

import com.squareup.okhttp.MediaType;
import com.squareup.okhttp.OkHttpClient;
import com.squareup.okhttp.Request;
import com.squareup.okhttp.RequestBody;
import com.squareup.okhttp.Response;

class OrderRequest {
    public String type;
    public String symbol;
    public String price;
    public String amount;
}

public final class App {
    public static void main(String[] args) throws Exception {
        final String apiKey = "";
        final String apiSecret = "";
      
        final String baseUrl = "https://api.bitfinex.com";
        OkHttpClient client = new OkHttpClient();

        final String apiPath = "v2/auth/w/order/submit";

        OrderRequest body = new OrderRequest();
        body.type = "LIMIT";
        body.symbol = "tBTCUSD";
        body.price = "15";
        body.amount = "0.1";

        String bodyJson = new GsonBuilder().create().toJson(body);

        String nonce = Long.toString((new Date().getTime()) * 1000l);
        String signature = String.format("/api/%s%s%s", apiPath, nonce, bodyJson);
        String sig = computeSignature(signature, apiSecret);

        RequestBody reqBody = RequestBody.create(MediaType.parse("application/json"), bodyJson);
        Request req = new Request.Builder().url(baseUrl + "/" + apiPath)
                .addHeader("bfx-nonce", nonce)
                .addHeader("bfx-apikey", apiKey)
                .addHeader("bfx-signature", sig)
                .post(reqBody).build();

        Response res = client.newCall(req).execute();
        String result = res.body().string();
        System.out.println(result);
    }

    private static String computeSignature(String input, String secret) throws Exception {
        SecretKeySpec signingKey = new SecretKeySpec(secret.getBytes(), "HmacSHA384");
        final Mac mac = Mac.getInstance("HmacSHA384");
        mac.init(signingKey);

        byte[] digest = mac.doFinal(input.getBytes());
        StringBuffer sb = new StringBuffer();
        for (byte b : digest) {
            String hex = Integer.toHexString(0xff & b);
            if (hex.length() == 1)
                sb.append('0');
            sb.append(hex);
        }
        return sb.toString();
    }
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

<!-- java@3-14 -->

In this example we're using the native java packages Date and crypto to compute signature.

For http requests we're using okhttp package and gson package for data serialization

# Request classes

<!-- java@16-21 -->

In this example we're going to submit a LIMIT order request so we've implemented a simple class that supports minimal required fields

# API Keys

<!-- java@25-26 -->

Authenticated requests require a pair of API keys. You can generate these keys in your account settings: https://setting.bitfinex.com/api#new-key

# Client setup

<!-- java@28-29 -->

Here we've defined base url for bitfinex api and instantiated a new http client with default configuration

# Endpoint

<!-- java@31 -->

Setting the path determines which endpoint you are calling. Path variables are appended to the path.

# Body Parameters

<!-- java@33-39 -->

Body parameters can be added depending on the endpoint. The documentation provides a list of required and available body parameters for each endpoint.

This example includes the body parameters required to submit an order. The documentation with all the available body parameters for this endpoint can be found here: https://docs.bitfinex.com/reference/rest-auth-submit-order

# Nonce

<!-- java@41 -->

A nonce needs to be passed in your request. The only requirement for the nonce is that it needs to increase between subsequent requests.

This example code generates a nonce based on the current UNIX timestamp to ensure an increasing value between subsequent requests.

# Signature

<!-- java@42 -->

A signature payload is created by joining '/api/', the apiPath, the nonce, and a JSON string of the body object.

# Signature hash

<!-- java@43,58-72 -->

The signature is hashed using the private key and the HmacSHA384 algorithm

# Sending the request

<!-- java@45-50 -->

In case of auth request we need to send json content type and include authentication headers (bfx-nonce, bfx-apikey, bfx-signature)

# Handling the response

<!-- java@52-54 -->

The response is always json and we need to parse the raw response from string to json object, however in our case we're just printing raw result for demo purpose
