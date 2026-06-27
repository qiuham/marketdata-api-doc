---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/guides/futures-rate-limits
api_type: Guide
updated_at: 2026-05-27 19:57:39.572999
---

# Futures Rate Limits

## REST Request Limits

Request limits are determined from cost associated with each API call and rate limiting budgets depend on which path the endpoint uses. Public endpoints do not have a cost and therefore do not count against any rate limiting budget. For `/derivatives` endpoints, clients can spend up to 500 every 10 seconds.

The below table displays the cost associated with each API call for `/derivatives` endpoints:

Endpoint| Cost  
---|---  
sendorder| 10  
editorder| 10  
cancelorder| 10  
batchorder| 9 + size of batch  
accounts| 2  
openpositions| 2  
fills (without lastFillTime specified)| 2  
fills (with lastFillTime specified)| 25  
cancelallorders| 25  
cancelallordersafter| 25  
withdrawaltospotwallet| 100  
openorders| 2  
orders/status| 1  
unwindqueue| 200  
GET leveragepreferences| 2  
PUT leveragepreferences| 10  
GET pnlpreferences| 2  
PUT pnlpreferences| 10  
transfer| 10  
transfer/subaccount| 10  
subaccount/:subaccountUid/trading-enabled| 2  
self-trade-strategy| 2  
  
On the [Batch Order](/api/docs/futures-api/trading/send-batch-order) endpoint, the cost is 9 + size of the batch of the requests. For example, a batch of 10 order requests, (send, edit, and or cancel) sent through the Batch Order endpoint would cost 19.

If the API limit is exceeded, the API will return `error` equal to `apiLimitExceeded`. For the FIX API the API Limit is done at the `CompID` level.

For `/history` endpoints, clients have a pool of up to 100 tokens that continually replenishes at a rate of 100 every 10 minutes.

The below table displays the cost associated with each API call for `/history` endpoints. The accountlog rate limit cost varies on the optional 'count' parameter (default count is 500):

Endpoint| Cost  
---|---  
historicalorders| 1  
historicaltriggers| 1  
historicalexecutions| 1  
accounglogcsv| 6  
accountlog (count: 1 - 25)| 1  
accountlog (count: 26 - 50)| 2  
accountlog (count: 51 - 1000)| 3  
accountlog (count: 1001 - 5000)| 6  
accountlog (count: 5001 - 100000)| 10  
  
### Example

The following shows the return of call of the `sendorder` endpoint where the API limit has been exceeded.
    
    
    {  
      "result": "error",  
      "serverTime": "2016-02-25T09:45:53.818Z",  
      "error": "apiLimitExceeded"  
    }  
    

## Websocket Limits

There are limits to both the number of connections a client can have open concurrently and the number of requests an individual connection can make. Limit values are subject to change and additional limits may be added in the future.

The current limits are:

Resource| Allowance| Replenish Period  
---|---|---  
Connections| 100| N/A  
Requests| 100| 1 second  
* REST Request Limits
* Example
  * Websocket Limits