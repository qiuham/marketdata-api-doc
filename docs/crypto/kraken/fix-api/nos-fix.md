---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/fix-api/nos-fix
api_type: REST
updated_at: 2026-07-23 19:20:17.379680
---

# Send order

Send order
    
    
    curl --request POST \
      --url https://futures.kraken.com/derivatives/api/v3/sendorder \
      --header 'APIKey: <api-key>' \
      --header 'Authent: <api-key>'
    
    
    import requests  
      
    url = "https://futures.kraken.com/derivatives/api/v3/sendorder"  
      
    headers = {  
        "APIKey": "<api-key>",  
        "Authent": "<api-key>"  
    }  
      
    response = requests.post(url, headers=headers)  
      
    print(response.text)
    
    
    const options = {method: 'POST', headers: {APIKey: '<api-key>', Authent: '<api-key>'}};  
      
    fetch('https://futures.kraken.com/derivatives/api/v3/sendorder', options)  
      .then(res => res.json())  
      .then(res => console.log(res))  
      .catch(err => console.error(err));
    
    
    package main  
      
    import (  
    	"fmt"  
    	"net/http"  
    	"io"  
    )  
      
    func main() {  
      
    	url := "https://futures.kraken.com/derivatives/api/v3/sendorder"  
      
    	req, _ := http.NewRequest("POST", url, nil)  
      
    	req.Header.Add("APIKey", "<api-key>")  
    	req.Header.Add("Authent", "<api-key>")  
      
    	res, _ := http.DefaultClient.Do(req)  
      
    	defer res.Body.Close()  
    	body, _ := io.ReadAll(res.Body)  
      
    	fmt.Println(string(body))  
      
    }
    
    
    {
      "result": "success",
      "sendStatus": {
        "order_id": "179f9af8-e45e-469d-b3e9-2fd4675cb7d0",
        "status": "placed",
        "receivedTime": "2019-09-05T16:33:50.734Z",
        "orderEvents": [
          {
            "type": "PLACE",
            "order": {
              "orderId": "179f9af8-e45e-469d-b3e9-2fd4675cb7d0",
              "cliOrdId": null,
              "type": "lmt",
              "symbol": "PI_XBTUSD",
              "side": "buy",
              "quantity": 10000,
              "filled": 0,
              "limitPrice": 9400,
              "reduceOnly": false,
              "timestamp": "2019-09-05T16:33:50.734Z",
              "lastUpdateTimestamp": "2019-09-05T16:33:50.734Z"
            },
            "reducedQuantity": null
          }
        ]
      },
      "serverTime": "2019-09-05T16:33:50.734Z"
    }

POST

/

sendorder

Send order
    
    
    curl --request POST \
      --url https://futures.kraken.com/derivatives/api/v3/sendorder \
      --header 'APIKey: <api-key>' \
      --header 'Authent: <api-key>'
    
    
    import requests  
      
    url = "https://futures.kraken.com/derivatives/api/v3/sendorder"  
      
    headers = {  
        "APIKey": "<api-key>",  
        "Authent": "<api-key>"  
    }  
      
    response = requests.post(url, headers=headers)  
      
    print(response.text)
    
    
    const options = {method: 'POST', headers: {APIKey: '<api-key>', Authent: '<api-key>'}};  
      
    fetch('https://futures.kraken.com/derivatives/api/v3/sendorder', options)  
      .then(res => res.json())  
      .then(res => console.log(res))  
      .catch(err => console.error(err));
    
    
    package main  
      
    import (  
    	"fmt"  
    	"net/http"  
    	"io"  
    )  
      
    func main() {  
      
    	url := "https://futures.kraken.com/derivatives/api/v3/sendorder"  
      
    	req, _ := http.NewRequest("POST", url, nil)  
      
    	req.Header.Add("APIKey", "<api-key>")  
    	req.Header.Add("Authent", "<api-key>")  
      
    	res, _ := http.DefaultClient.Do(req)  
      
    	defer res.Body.Close()  
    	body, _ := io.ReadAll(res.Body)  
      
    	fmt.Println(string(body))  
      
    }
    
    
    {
      "result": "success",
      "sendStatus": {
        "order_id": "179f9af8-e45e-469d-b3e9-2fd4675cb7d0",
        "status": "placed",
        "receivedTime": "2019-09-05T16:33:50.734Z",
        "orderEvents": [
          {
            "type": "PLACE",
            "order": {
              "orderId": "179f9af8-e45e-469d-b3e9-2fd4675cb7d0",
              "cliOrdId": null,
              "type": "lmt",
              "symbol": "PI_XBTUSD",
              "side": "buy",
              "quantity": 10000,
              "filled": 0,
              "limitPrice": 9400,
              "reduceOnly": false,
              "timestamp": "2019-09-05T16:33:50.734Z",
              "lastUpdateTimestamp": "2019-09-05T16:33:50.734Z"
            },
            "reducedQuantity": null
          }
        ]
      },
      "serverTime": "2019-09-05T16:33:50.734Z"
    }

#### Authorizations

APIKey

string

header

required

General API key with full access

Authent

string

header

required

Authentication string

#### Headers

algoId

string

ID of the algorithm that is making the request.

#### Query Parameters

processBefore

string<date-time>

The time before which the request should be processed, otherwise it is rejected.

orderType

enum<string>

required

The order type:

  * `lmt` \- a limit order

  * `post` \- a post-only limit order

  * `mkt` \- an immediate-or-cancel order with 1% price protection

  * `stp` \- a stop order

  * `take_profit` \- a take profit order

  * `ioc` \- an immediate-or-cancel order

  * `trailing_stop` \- a trailing stop order

  * `fok` \- fill or kill order The order type:

  * `lmt` \- a limit order

  * `post` \- a post-only limit order

  * `mkt` \- an immediate-or-cancel order with 1% price protection

  * `stp` \- a stop order

  * `take_profit` \- a take profit order

  * `ioc` \- an immediate-or-cancel order

  * `trailing_stop` \- a trailing stop order

  * `fok` \- fill-or-kill order

Available options:

`lmt`,

`post`,

`ioc`,

`mkt`,

`stp`,

`take_profit`,

`trailing_stop`,

`fok`

symbol

string

required

The symbol of the Futures

side

enum<string>

required

The direction of the order.

Available options:

`buy`,

`sell`

size

number

required

The size associated with the order. Note that different Futures have different contract sizes.

limitPrice

number

The limit price associated with the order. Note that for stop orders, limitPrice denotes the worst price at which the `stp` or `take_profit` order can get filled at. If no `limitPrice` is provided the `stp` or `take_profit` order will trigger a market order. If placing a `trailing_stop` order then leave undefined.

stopPrice

number

The stop price associated with a stop or take profit order.

Required if orderType is `stp` or `take_profit`, but if placing a `trailing_stop` then leave undefined. Note that for stop orders, limitPrice denotes the worst price at which the `stp` or `take_profit` order can get filled at. If no `limitPrice` is provided the `stp` or `take_profit` order will trigger a market order.

cliOrdId

string

The order identity that is specified from the user. It must be globally unique.

Maximum string length: `100`

triggerSignal

enum<string>

If placing a `stp`, `take_profit` or `trailing_stop`, the signal used for trigger.

  * `mark` \- the mark price
  * `index` \- the index price
  * `last` \- the last executed trade

Available options:

`mark`,

`index`,

`last`

reduceOnly

boolean

Set as true if you wish the order to only reduce an existing position.

Any order which increases an existing position will be rejected. Default false.

trailingStopMaxDeviation

number

Required if the order type is `trailing_stop`. Maximum value of 50%, minimum value of 0.1% for 'PERCENT' 'maxDeviationUnit'.

Is the maximum distance the trailing stop's trigger price may trail behind the requested trigger signal. It defines the threshold at which the trigger price updates.

Required range: `0.1 <= x <= 50`

trailingStopDeviationUnit

enum<string>

Required if the order type is `trailing_stop`.

This defines how the trailing trigger price is calculated from the requested trigger signal. For example, if the max deviation is set to 10, the unit is 'PERCENT', and the underlying order is a sell, then the trigger price will never be more then 10% below the trigger signal. Similarly, if the deviation is 100, the unit is 'QUOTE_CURRENCY', the underlying order is a sell, and the contract is quoted in USD, then the trigger price will never be more than $100 below the trigger signal.

Available options:

`PERCENT`,

`QUOTE_CURRENCY`

limitPriceOffsetValue

number

Can only be set for triggers, e.g. order types `take_profit`, `stop` and `trailing_stop`. If set, `limitPriceOffsetUnit` must be set as well. This defines a relative limit price depending on the trigger `stopPrice`. The price is determined when the trigger is activated by the `triggerSignal`. The offset can be positive or negative, there might be restrictions on the value depending on the `limitPriceOffsetUnit`.

limitPriceOffsetUnit

enum<string>

Can only be set together with `limitPriceOffsetValue`. This defines the unit for the relative limit price distance from the trigger's `stopPrice`.

Available options:

`QUOTE_CURRENCY`,

`PERCENT`

broker

string<iiban>

Valid Broker IIBAN on whose behalf the order is sent. The format must follow the usual IIBAN pattern `XXXX YYYY ZZZZ WWWW` or machine pattern `XXXXYYYYZZZZWWWW`.

Note: This is currently available exclusively in the Kraken pre-prod environments.

#### Response

200 - application/json

  * Success Response

  * Errors

sendStatus

object

required

A structure containing information on the send order request.

Show child attributes

result

enum<string>

required

Available options:

`success`

Example:

`"success"`

serverTime

string<date-time>

required

Server time in Coordinated Universal Time (UTC)

Example:

`"2020-08-27T17:03:33.196Z"`

Was this page helpful?

[Get instrument status](/api-reference/instrument-details/get-instrument-status)[Edit order](/api-reference/order-management/edit-order)

Ctrl+I