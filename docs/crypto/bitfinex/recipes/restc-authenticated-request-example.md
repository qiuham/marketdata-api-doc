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
source_url: 'https://docs.bitfinex.com/recipes/restc-authenticated-request-example'
updated_at: 2026-11-27
---

# [REST][C#] Authenticated request example

```csharp C#
using System;
using System.Net.Http;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;
using System.Security.Cryptography;

namespace BitfinexCSdotharp // Note: actual namespace depends on the project name.
{
  internal class Program
  {
    static readonly HttpClient client = new HttpClient();

    static async Task Main(string[] args)
    {
      const string baseUrl = "https://api.bitfinex.com";
      const string apiKey = "";
      const string apiSecret = "";

      string apiPath = "v2/auth/w/order/submit";

      var body = new
      {
        type = "LIMIT",
        symbol = "tBTCUSD",
        price = "15",
        amount = "0.1"
      };
      string bodyJson = JsonSerializer.Serialize(body);

      string nonce = (DateTimeOffset.Now.ToUnixTimeMilliseconds() * 1000).ToString();
      string signature = $"/api/{apiPath}{nonce}{bodyJson}";
      string sig;
      using (var hmac = new HMACSHA384(Encoding.UTF8.GetBytes(apiSecret)))
      {
        byte[] output = hmac.ComputeHash(Encoding.UTF8.GetBytes(signature));
        sig = BitConverter.ToString(output).Replace("-", "").ToLower();
      }

      var request = new HttpRequestMessage(HttpMethod.Post, $"{baseUrl}/{apiPath}");
      request.Content = new StringContent(bodyJson, Encoding.UTF8, "application/json");
      request.Headers.Add("bfx-nonce", nonce);
      request.Headers.Add("bfx-apikey", apiKey);
      request.Headers.Add("bfx-signature", sig);

      try
      {
        HttpResponseMessage response = await client.SendAsync(request);

        string responseBody = await response.Content.ReadAsStringAsync();
        if (response.IsSuccessStatusCode)
        {
          Console.WriteLine(responseBody);
        }
        else
        {
          Console.WriteLine($"Error Status code {response.StatusCode}: {responseBody}");
        }
      }
      catch (HttpRequestException e)
      {
        Console.WriteLine("\nException Caught!");
        Console.WriteLine("Message :{0} ", e.Message);
      }
    }
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

<!-- csharp@1-6 -->

This example uses only native dotnet libraries to make request

# Client setup

<!-- csharp@12 -->

The example uses System.Net.Http.HttpClient to make http requests

# Base URL

<!-- csharp@16 -->

Here we define base url that points to bitfinex api

# API keys

<!-- csharp@17-18 -->

Authenticated requests require a pair of API keys. You can generate these keys in your account settings: https://setting.bitfinex.com/api#new-key

# Endpoint

<!-- csharp@20 -->

Setting the path determines which endpoint you are calling. Path variables are appended to the path.

# Body parameters

<!-- csharp@22-29 -->

Body parameters can be added depending on the endpoint. The documentation provides a list of required and available body parameters for each endpoint.

This example includes the body parameters required to submit an order. The documentation with all the available body parameters for this endpoint can be found here: https://docs.bitfinex.com/reference/rest-auth-submit-order

# Nonce

<!-- csharp@31 -->

A nonce needs to be passed in your request. The only requirement for the nonce is that it needs to increase between subsequent requests.

This example code generates a nonce based on the current UNIX timestamp to ensure an increasing value between subsequent requests.

# Signature

<!-- csharp@32 -->

A signature payload is created by joining '/api/', the apiPath, the nonce, and a JSON string of the body object.

# Signature hash

<!-- csharp@33-38 -->

The signature is hashed using the private key and the HmacSHA384 algorithm

# Sending the request

<!-- csharp@40-48 -->

In case of auth request we need to send json content type and include authentication headers (bfx-nonce, bfx-apikey, bfx-signature)

# Handling the response

<!-- csharp@50-58 -->

The response is always json and we need to parse the raw response from string to json object, however in our case we're just printing raw result for demo purpose
