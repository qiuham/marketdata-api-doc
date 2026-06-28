---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/guides/futures-rest
api_type: Guide
updated_at: 2026-05-27 19:57:46.731703
---

# Futures REST

## Authentication

warning

**Authentication Flow for v3 endpoints:** We have updated the authentication flow for `/derivatives/*` endpoints as of 20th February 2024 to align with best practices and ensure higher security standards. For more information, see Upcoming Changes.

Calls to endpoints requiring authentication must include the following HTTP headers: `APIKey` and `Authent`. A third header, `Nonce`, may also be included (this is optional).

Header name| Value|   
---|---|---  
APIKey| Public api key (not the secret!)| required  
Authent| Authentication string| required  
Nonce| A unique incrementing nonce| optional  
  
Some HTTP endpoints allow performing sensitive operations such as placing orders or requesting a digital asset withdrawal. These private endpoints can therefore be called only through encrypted requests, and an authentication string (`Authent`) must be included in each such request. `Authent` is computed from the following inputs:

### PostData

`postData` represents the parameters sent to an HTTP endpoint, formatted as a `&` concatenated string in the form `<argument>=<value>`. The specific parameters required vary by endpoint.

_Example:_ `symbol=fi_xbtusd_180615`

### Nonce

`Nonce` is a continuously incrementing integer parameter. A good nonce is your system time in milliseconds (in string format). Our system tolerates nonces that are out of order for a brief period of time. Nonce is **not** required.

_Example:_ `1415957147987`

Many authentication issues are related with incorrect `Nonce`. A new pair of api keys will automatically reset the nonce and resolve these issues.

### Endpoint Path

`endpointPath` This is the URL extension of the endpoint.

_Example:_ `/api/v3/orderbook`

### API Secret

The `api_secret` is obtained as described under [generate-api-keys].

_Example:_ `rttp4AzwRfYEdQ7R7X8Z/04Y4TZPa97pqCypi3xXxAqftygftnI6H9yGV+OcUOOJeFtZkr8mVwbAndU3Kz4Q+eG`

### Authent

Based on these inputs, `Authent` needs to be computed as follows:

  1. Concatenate `postData` \+ `Nonce` \+ `endpointPath`
  2. Hash the result of step 1 with the [SHA-256 algorithm](https://en.wikipedia.org/wiki/SHA-2)
  3. [Base64-decode](https://en.wikipedia.org/wiki/Base64) your `api_secret`
  4. Use the result of step 3 to hash the result of the step 2 with the [HMAC-SHA-512 algorithm](https://en.wikipedia.org/wiki/Hash-based_message_authentication_code)
  5. [Base64-encode](https://en.wikipedia.org/wiki/Base64) the result of step 4

### Upcoming Changes

Before| After  
---|---  
Users were required to hash query string parameters before url-encoding for Authent generation, e.g., `greeting=hello world`.| The authentication process will now require hashing the full, url-encoded URI component as it appears in the request, e.g., `greeting=hello%20world`.  
  
This update is particularly relevant for the batchorder endpoint, which accepts a JSON body in its query parameters.

tip

For the time being, this change is backward compatible. The API will accept both Authent generation methods described above. However, we aim to phase out the old method (hashing decoded query string parameters) on October 1st, 2025 to maintain the highest security standards. We strongly encourage all users to transition to the new method as soon as possible to ensure seamless service continuity.

### Authentication example

Inclusion of HTTP headers in Java where `apiKey`, `nonce`, and `authent` are determined as described in this section. For full working examples in different programming languages, see [Sample Implementations](https://github.com/cryptofacilities).
    
    
      
    String url = "https://futures.kraken.com/derivatives/api/v3/sendOrder";  
      
    URL obj = new URL(url);  
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();  
    ...  
    con.setRequestProperty("APIKey", apiKey);  
    con.setRequestProperty("Nonce", nonce);  
    con.setRequestProperty("Authent", authent);  
    

## Calls and Returns

### Calls

Calls to endpoints that do not change the state of the server should be submitted with request type `GET` and with request parameters submitted in the URL. Calls to endpoints that do change the state of the server should be submitted with request type `POST` or `PUT` and with request parameters submitted in the request body.

### Returns

> Example response of a successful call to the `sendorder` endpoint.
    
    
    {  
      "result": "success",  
      "serverTime": "2016-02-25T09:45:53.818Z",  
      "sendStatus": {  
        "receivedTime": "2016-02-25T09:45:53.601Z",  
        "status": "placed",  
        "order_id": "c18f0c17-9971-40e6-8e5b10df05d422f0"  
      }  
    }  
    

The API's returns are in JSON format. If the call was successful, the return includes the requested information or feedback on the requested action.

If a call was successful, the `result` key in the root structure will have the value `success`.

> Example response of a successful call to the `sendorder` endpoint where the desired operation was not performed.
    
    
    {  
       "result":"success",  
       "serverTime":"2016-02-25T09:45:53.818Z",  
       "sendStatus":{  
          "receivedTime":"2016-02-25T09:45:53.601Z",  
          "status":"insufficientAvailableFunds"  
       }  
    }  
    

Note that if a call comes back with `result` equal to `success`, this merely means that the request has been received and assessed successfully. It does not necessarily mean that the desired operation has been performed. Details on the operation's status are returned in a status key, where applicable.

  * Authentication
* PostData
* Nonce
* Endpoint Path
* API Secret
* Authent
* Upcoming Changes
* Authentication example
  * Calls and Returns
* Calls
* Returns