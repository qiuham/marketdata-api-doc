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
source_url: 'https://docs.bitfinex.com/docs/rest-reading-the-api-documentation'
updated_at: 2026-11-23
---

# Reading the Documentation (REST)

General instructions for the interpretation of API documentation pages.

Each page in our API documentation follows a particular structure so as to make it as easy to use as possible. This article explains the structure of our documentation pages as well as some of the key concepts found in the documentation. The article also shows how the code examples found in our documentation pages can be interpreted and used. We will use the JavaScript examples here.

Our REST endpoint documentation pages have the following structure (click the image for a zoomed view):

![1705](https://files.readme.io/da4eddd-REST_endpoint_trades_with_numbers.png "REST endpoint trades with numbers.png")

1. A title and short description describing the general purpose of the endpoint.
2. A URL example showing the placement of any 'path' parameters.
3. Example code. Examples in different languages can be selected is available. An example cURL will also be available for public endpoints that can be queried in your browser.
4. The response map showing the endpoint response using field names. The field names used correspond to the response fields at 7. Some fields will be marked as placeholder and will come back as null in the actual response. The following structure will be used to indicate repetition in a response that can contain multiple arrays: \[\[FIRST\_ARRAY]\[FIRST\_ARRAY],....]. Please also note that returned arrays can be longer than the response map. If the response has placeholders at the end of the response, these will be omitted from the response map. Any such omissions are indicated with ...
5. An example response showing example data.
6. Path, body, and query parameters that can be used for your query. Mandatory parameters will be marked with a \* and will always be included in the example code.
7. Response fields are specified here. Any field found in the response map at 4. will be shown here with its data type and further clarification.

## Example Code

Each REST endpoint has accompanying example code. The example code is followed by a list of all available parameters that can be altered or added to achieve different responses.

### Example Code for Public Endpoints

Below is the example code for the [Trades](https://docs.bitfinex.com/reference/rest-public-trades)  endpoint in JavaScript. If NodeJS is installed on your system along with the required dependencies for this code ('node-fetch'in this case), you can run this code as is.

Below the example code on our documentation pages, you will find any applicable parameters for your query. For public endpoints these can be either path parameters or query parameters (pathParams and queryParams in the example code).

```javascript
"use strict"

const fetch = require('node-fetch')
const url = 'https://api-pub.bitfinex.com/v2/'

const pathParams = 'trades/tBTCUSD/hist' // Change these based on preferred pairs
const queryParams = 'limit=120&sort=-1' // Change these based on relevant query params

async function request() {
   try {
       const req = await fetch(`${url}/${pathParams}?${queryParams}`)
       const response = await req.json()
       console.log(`STATUS ${req.status} - ${JSON.stringify(response)}`)
   }
   catch (err) {
       console.log(err)
   }
}

request()
```

### Path Parameters

Path parameters are added to the path of the endpoint. At point 2 in the example page image you can see the URL showing the order in which pathParams are added.

For the trades endpoint in the example code above, the pathParams are 'trades', 'tBTCUSD', and 'hist'. To look up a different symbol, you would change the symbol pathParam. If you wish to retrieve the trades for ETH/USD, for example, you would change the pathParams to 'trades/tETHUSD/hist'.

### Query Parameters

Some endpoints also allow the use of query parameters. When using query parameters, the order in which they are added does not matter. Each parameter needs to be connected to the previous with an '&' symbol. The example code shows how the parameters 'limit' (120) and 'sort' (-1) can be used. If you wanted to add an end timestamp, the queryParams in the example code could be changed to 'limit=120\&sort-1\&end=TIMESTAMP'.

### Query Parameters in the cURL

It is also possible to create a cURL to retrieve data in the browser. To do this, start with the base URL and add the pathParams. After the final pathParam, add a '?' followed by the desired queryParams.

For example, say you have the following cURL: cURL: <https://api-pub.bitfinex.com/v2/trades/tBTCUSD/hist>

To limit the results to 120 and sort from old to new, the URL would be changed to: <https://api-pub.bitfinex.com/v@/trades/tBTCUSD/hist?&limit=120&sort=-1>

### Example Code for Authenticated Endpoints

Below you can see the example code of the [Orders History](https://docs.bitfinex.com/reference/rest-auth-orders-history) authenticated endpoint. A request to this endpoint returns a history of your orders, but the code will only run in combination with code that authenticates your connection. You can find the example code for authenticated on this page: [Authenticated Endpoints](https://docs.bitfinex.com/docs/rest-auth).

```javascript
const apiPath = 'v2/auth/r/orders/tBTCUSD/hist' // or 'v2/auth/r/orders/hist'
fetch(`https://api.bitfinex.com/${apiPath}`, {
  method:'POST',
  body: JSON.stringify({}),
  headers: {
    /* auth headers */
  }
})
.then(res => res.json())
.then(json => console.log(json))
```

The example code found in the documentation for specific endpoints can be combined with the authentication code as follows:

1. Edit the url in the apiPath variable found in the authentication code to correspond with the URL found in the example code for the specific endpoint. For the Orders History endpoint above you would edit apiPath to 'v2/auth/r/orders/hist'.
2. If there are any path parameters, add these to apiPath as well. For the Orders History endpoint, you can specify a trading pair. Retrieving historic tBTCUSD orders is done by editing apiPath to 'v2/auth/orders/tBTCUSD/hist'.
3. If there are any Query Parameters applicable for your request, add these to the body object in the authentication code.
4. Lastly, any Form Data fields can be added to the body object. Form data can be required (for example when placing orders) or it can be optional. The Orders History example used here has optional form data to specify the OrderIDs of orders that you would like to retrieve. If there are any mandatory form data fields, these will always be shown in the body of the example code for the specific endpoint.

Below is an example of the authentication code that is edited to retrieve data from the Orders History endpoint using an optional path variable as well as all query parameters (the OrderID form data parameter is not used, but can be used by adding 'id: \<ID\_HERE>' to the body.

```javascript
const CryptoJS = require('crypto-js') // Standard JavaScript cryptography library
const fetch = require('node-fetch') // "Fetch" HTTP req library
   
const apiKey = 'API_KEY_HERE' // const apiKey = 'paste key here'
const apiSecret = 'API_KEY_HERE' // const apiSecret = 'paste secret here'

const apiPath = 'v2/auth/r/orders/tBTCUSD/hist'// Example path

const nonce = (Date.now() * 1000).toString() // Standard nonce generator. Timestamp * 1000

let signature = `/api/${apiPath}${nonce}${JSON.stringify(body)}` 
// Consists of the complete url, nonce, and request body

const sig = CryptoJS.HmacSHA384(signature, apiSecret).toString() 
// The authentication signature is hashed using the private key

fetch(`https://api.bitfinex.com/${apiPath}`, {
  method:'post',
  body: JSON.stringify({
  	start: 1554002000000,
  	end: 1554002216000,
  	limit:10
  }),
  headers: {
    'Content-Type': 'application/json',
    'bfx-nonce': nonce,
    'bfx-apikey': apiKey,
    'bfx-signature': sig
  }
})
.then(res => res.json())
.then(json => console.log(json))
```
