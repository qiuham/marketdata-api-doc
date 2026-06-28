---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/guides/spot-rest-intro
api_type: Guide
updated_at: 2026-05-27 19:59:06.438341
---

# Spot REST Introduction

## API Organisation

The Spot REST API is organised by function, covering a wide range of services:

  * [Market Data](/api/docs/rest-api/get-order-book)
  * [Account Data](/api/docs/rest-api/get-account-balance)
  * [Trading](/api/docs/rest-api/add-order)
  * [Funding](/api/docs/rest-api/get-deposit-addresses)
  * [Subaccounts](/api/docs/rest-api/create-subaccount)
  * [Earn](/api/docs/rest-api/allocate-strategy)
  * [Websocket Authentication](/api/docs/rest-api/get-websockets-token)

## Requests, Responses and Errors

### Requests

Request payloads supports Json encoding (`Content-Type: application/json`) as well as form-encoded (`Content-Type: application/x-www-form-urlencoded`). We recommend clients to specify `User-Agent` in the headers of all their requests. This will help us optimize interactions and improve the overall efficiency and security of the API.

### Responses

Responses are JSON encoded and contain one or two top-level keys (`result` and `error` for successful requests or those with warnings, or only `error` for failed or rejected requests)

### Example

Request:
    
    
    GET <https://api.kraken.com/0/public/SystemStatus>  
    

Successful response:
    
    
    {  
        "error": [],  
        "result": {  
            "status": "online",  
            "timestamp": "2021-03-22T17:18:03Z"  
        }  
    }  
    

Error response:
    
    
    {  
        "error": [  
            "EGeneral:Invalid arguments:ordertype"  
        ]  
    }  
    

### Error Details

HTTP status codes are generally not used by our API to convey information about the state of requests and any errors or warnings are denoted in the `error` field of the response as described above. Status codes **other** than 200 indicate that there was an issue with the request reaching our servers.

Error messages follow the general format "<severity><category>: <description>"

  * <severity> : `E` for error, `W` for warning.
  * <category> : `General`, `Auth`, `API`, `Query`, `Order`, `Trade`, `Funding`, or `Service`.
  * <description> : a text string that describes the reason for the error.

    
    
    i.e., "EGeneral: Invalid arguments:ordertype"  
    

Additional information can be found on our [support center](https://support.kraken.com/hc/en-us/articles/360001491786-API-error-messages).

  * API Organisation
  * Requests, Responses and Errors
* Requests
* Responses
* Example
* Error Details