---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/rest-api/add-order
api_type: REST
updated_at: 2026-08-25 19:15:00.515124
---

# Add Order

Add Order
    
    
    curl --request POST \
      --url https://api.kraken.com/0/private/AddOrder \
      --header 'API-Key: <api-key>' \
      --header 'API-Sign: <api-key>' \
      --header 'Content-Type: application/json' \
      --data '
    {
      "nonce": 163245617,
      "ordertype": "limit",
      "type": "buy",
      "volume": "1.25",
      "pair": "XBTUSD",
      "price": "27500",
      "cl_ord_id": "6d1b345e-2821-40e2-ad83-4ecb18a06876",
      "trigger": "last",
      "reduce_only": false,
      "stptype": "cancel-newest",
      "timeinforce": "GTC",
      "validate": false
    }
    '
    
    
    import requests
    
    url = "https://api.kraken.com/0/private/AddOrder"
    
    payload = {
        "nonce": 163245617,
        "ordertype": "limit",
        "type": "buy",
        "volume": "1.25",
        "pair": "XBTUSD",
        "price": "27500",
        "cl_ord_id": "6d1b345e-2821-40e2-ad83-4ecb18a06876",
        "trigger": "last",
        "reduce_only": False,
        "stptype": "cancel-newest",
        "timeinforce": "GTC",
        "validate": False
    }
    headers = {
        "API-Key": "<api-key>",
        "API-Sign": "<api-key>",
        "Content-Type": "application/json"
    }
    
    response = requests.post(url, json=payload, headers=headers)
    
    print(response.text)
    
    
    const options = {
      method: 'POST',
      headers: {
        'API-Key': '<api-key>',
        'API-Sign': '<api-key>',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        nonce: 163245617,
        ordertype: 'limit',
        type: 'buy',
        volume: '1.25',
        pair: 'XBTUSD',
        price: '27500',
        cl_ord_id: '6d1b345e-2821-40e2-ad83-4ecb18a06876',
        trigger: 'last',
        reduce_only: false,
        stptype: 'cancel-newest',
        timeinforce: 'GTC',
        validate: false
      })
    };
    
    fetch('https://api.kraken.com/0/private/AddOrder', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    package main
    
    import (
    	"fmt"
    	"strings"
    	"net/http"
    	"io"
    )
    
    func main() {
    
    	url := "https://api.kraken.com/0/private/AddOrder"
    
    	payload := strings.NewReader("{\n  \"nonce\": 163245617,\n  \"ordertype\": \"limit\",\n  \"type\": \"buy\",\n  \"volume\": \"1.25\",\n  \"pair\": \"XBTUSD\",\n  \"price\": \"27500\",\n  \"cl_ord_id\": \"6d1b345e-2821-40e2-ad83-4ecb18a06876\",\n  \"trigger\": \"last\",\n  \"reduce_only\": false,\n  \"stptype\": \"cancel-newest\",\n  \"timeinforce\": \"GTC\",\n  \"validate\": false\n}")
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("API-Key", "<api-key>")
    	req.Header.Add("API-Sign", "<api-key>")
    	req.Header.Add("Content-Type", "application/json")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    {
      "error": [],
      "result": {
        "descr": {
          "order": "buy 2.12340000 XBTUSD @ limit 25000.1 with 2:1 leverage",
          "close": "close position @ stop loss 22000.0 -> limit 21000.0"
        },
        "txid": [
          "OUF4EM-FRGI2-MQMWZD"
        ]
      }
    }

POST

/

private

/

AddOrder

Add Order
    
    
    curl --request POST \
      --url https://api.kraken.com/0/private/AddOrder \
      --header 'API-Key: <api-key>' \
      --header 'API-Sign: <api-key>' \
      --header 'Content-Type: application/json' \
      --data '
    {
      "nonce": 163245617,
      "ordertype": "limit",
      "type": "buy",
      "volume": "1.25",
      "pair": "XBTUSD",
      "price": "27500",
      "cl_ord_id": "6d1b345e-2821-40e2-ad83-4ecb18a06876",
      "trigger": "last",
      "reduce_only": false,
      "stptype": "cancel-newest",
      "timeinforce": "GTC",
      "validate": false
    }
    '
    
    
    import requests
    
    url = "https://api.kraken.com/0/private/AddOrder"
    
    payload = {
        "nonce": 163245617,
        "ordertype": "limit",
        "type": "buy",
        "volume": "1.25",
        "pair": "XBTUSD",
        "price": "27500",
        "cl_ord_id": "6d1b345e-2821-40e2-ad83-4ecb18a06876",
        "trigger": "last",
        "reduce_only": False,
        "stptype": "cancel-newest",
        "timeinforce": "GTC",
        "validate": False
    }
    headers = {
        "API-Key": "<api-key>",
        "API-Sign": "<api-key>",
        "Content-Type": "application/json"
    }
    
    response = requests.post(url, json=payload, headers=headers)
    
    print(response.text)
    
    
    const options = {
      method: 'POST',
      headers: {
        'API-Key': '<api-key>',
        'API-Sign': '<api-key>',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        nonce: 163245617,
        ordertype: 'limit',
        type: 'buy',
        volume: '1.25',
        pair: 'XBTUSD',
        price: '27500',
        cl_ord_id: '6d1b345e-2821-40e2-ad83-4ecb18a06876',
        trigger: 'last',
        reduce_only: false,
        stptype: 'cancel-newest',
        timeinforce: 'GTC',
        validate: false
      })
    };
    
    fetch('https://api.kraken.com/0/private/AddOrder', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    package main
    
    import (
    	"fmt"
    	"strings"
    	"net/http"
    	"io"
    )
    
    func main() {
    
    	url := "https://api.kraken.com/0/private/AddOrder"
    
    	payload := strings.NewReader("{\n  \"nonce\": 163245617,\n  \"ordertype\": \"limit\",\n  \"type\": \"buy\",\n  \"volume\": \"1.25\",\n  \"pair\": \"XBTUSD\",\n  \"price\": \"27500\",\n  \"cl_ord_id\": \"6d1b345e-2821-40e2-ad83-4ecb18a06876\",\n  \"trigger\": \"last\",\n  \"reduce_only\": false,\n  \"stptype\": \"cancel-newest\",\n  \"timeinforce\": \"GTC\",\n  \"validate\": false\n}")
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("API-Key", "<api-key>")
    	req.Header.Add("API-Sign", "<api-key>")
    	req.Header.Add("Content-Type", "application/json")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    {
      "error": [],
      "result": {
        "descr": {
          "order": "buy 2.12340000 XBTUSD @ limit 25000.1 with 2:1 leverage",
          "close": "close position @ stop loss 22000.0 -> limit 21000.0"
        },
        "txid": [
          "OUF4EM-FRGI2-MQMWZD"
        ]
      }
    }

#### Authorizations

API-Key

string

header

required

The "API-Key" header should contain your API key.

API-Sign

string

header

required

Authenticated requests should be signed with the "API-Sign" header, using a signature generated with your private key, nonce, encoded payload, and URI path.

#### Body

application/json

nonce

integer<int64>

required

Nonce used in construction of `API-Sign` header

ordertype

enum<string>

required

The execution model of the order.

Available options:

`market`,

`limit`,

`iceberg`,

`stop-loss`,

`take-profit`,

`stop-loss-limit`,

`take-profit-limit`,

`trailing-stop`,

`trailing-stop-limit`,

`settle-position`

Example:

`"limit"`

type

enum<string>

required

Order direction (buy/sell)

Available options:

`buy`,

`sell`

volume

string

required

Order quantity in terms of the base asset

> Note: Volume can be specified as `0` for closing margin orders to automatically fill the requisite quantity.

Example:

`"1.25"`

pair

string

required

Asset pair `id` or `altname`

Example:

`"XBTUSD"`

userref

integer<int32>

This is an optional non-unique, numeric identifier which can associated with a number of orders by the client. This field is mutually exclusive with `cl_ord_id` parameter.

`userref` is an optional user-specified integer id that can be associated with any number of orders. Many clients choose a `userref` corresponding to a unique integer id generated by their systems (e.g. a timestamp). However, because we don't enforce uniqueness on our side, it can also be used to easily group orders by pair, side, strategy, etc. This allows clients to more readily cancel or query information about orders in a particular group, with fewer API calls by using `userref` instead of our `txid`, where supported.

cl_ord_id

string

Adds an alphanumeric client order identifier which uniquely identifies an open order for each client. This field is mutually exclusive with `userref` parameter.

The `cl_ord_id` parameter can be one of the following formats:

  * • Long UUID: `6d1b345e-2821-40e2-ad83-4ecb18a06876` 32 hex characters separated with 4 dashes.
  * • Short UUID: `da8e4ad59b78481c93e589746b0cf91f` 32 hex characters with no dashes.
  * • Free text: `arb-20240509-00010` Free format ascii text up to 18 characters.

displayvol

string

For `iceberg` orders only, it defines the quantity to show in the book while the rest of order quantity remains hidden. Minimum value is 1 / 15 of `volume`.

asset_class

enum<string>

This parameter is required on requests for non-crypto pairs, i.e. use `tokenized_asset` for xstocks.

Available options:

`tokenized_asset`

price

string

Price:

  * • Limit price for `limit` and `iceberg` orders
  * • Trigger price for `stop-loss`, `stop-loss-limit`, `take-profit`, `take-profit-limit`, `trailing-stop` and `trailing-stop-limit` orders

Notes:

  * • Relative Prices: Either `price` or `price2` can be preceded by `+`, `-`, or `#` to specify the order price as an offset relative to the last traded price. `+` adds the amount to, and `-` subtracts the amount from the last traded price. `#` will either add or subtract the amount to the last traded price, depending on the direction and order type used. Prices can also be suffixed with a `%` to signify the relative amount as a percentage, rather than an absolute price difference.
  * • Trailing Stops: Must use a relative price for this field, namely the `+` prefix, from which the direction will be automatic based on if the original order is a buy or sell (no need to use `-` or `#`). The `%` suffix also works for these order types to use a relative percentage price.

Example:

`"40000.0"`

price2

string

Secondary Price:

  * • Limit price for `stop-loss-limit`, `take-profit-limit` and `trailing-stop-limit` orders

Note:

  * • Trailing Stops: Must use a relative price for this field, namely one of the `+` or `-` prefixes. This will provide the offset from the trigger price to the limit price, i.e. +0 would set the limit price equal to the trigger price. The `%` suffix also works for this field to use a relative percentage limit price.

trigger

enum<string>

default:last

Price signal used to trigger `stop-loss`, `stop-loss-limit`, `take-profit`, `take-profit-limit`, `trailing-stop` and `trailing-stop-limit` orders

Notes:

  * • This `trigger` type will also be used for any associated conditional close orders.
  * • To keep triggers serviceable, the last price will be used as fallback reference price during connectivity issues with external index feeds.

Available options:

`index`,

`last`

leverage

string

Amount of leverage desired (default: none)

Example:

`5`

reduce_only

boolean

default:false

If `true`, order will only reduce a currently open position, not increase it or open a new position.

Example:

`true`

stptype

enum<string>

default:cancel-newest

Self Trade Prevention (STP) is a protection feature to prevent users from inadvertently or deliberately trading against themselves. To prevent a self-match, one of the following STP modes can be used to define which order(s) will be expired:

  * • `cancel-newest`: arriving order will be canceled
  * • `cancel-oldest`: resting order will be canceled
  * • `cancel-both`: both arriving and resting orders will be canceled

Available options:

`cancel-newest`,

`cancel-oldest`,

`cancel-both`

oflags

string

Comma delimited list of order flags

  * • `post` post-only order (available when ordertype = limit)
  * • `fcib` prefer fee in base currency (default if selling)
  * • `fciq` prefer fee in quote currency (default if buying, mutually exclusive with `fcib`)
  * • `nompp` (DEPRECATED) — disabling Market Price Protection for market orders is no longer supported. If supplied, the flag is accepted but ignored.
  * • `viqc` order volume expressed in quote currency. This option is supported only for buy market orders. Also not available on margin orders.

Example:

`"post"`

timeinforce

enum<string>

default:GTC

Time-in-force of the order to specify how long it should remain in the order book before being cancelled. GTC (Good-'til-cancelled) is default if the parameter is omitted. IOC (immediate-or-cancel) will immediately execute the amount possible and cancel any remaining balance rather than resting in the book. GTD (good-'til-date), if specified, must coincide with a desired `expiretm`. FOK (fill-or-kill) will execute the full order immediately or cancel it entirely.

Available options:

`GTC`,

`IOC`,

`GTD`,

`FOK`

starttm

string

Scheduled start time, can be specified as an absolute timestamp or as a number of seconds in the future:

  * • `0` now (default)
  * • `<n>` = unix timestamp of start time
  * • `+<n>` = schedule start time `<n>` seconds from now 
* Note that URL encoding of the `+` character changes it to a space, so please use `%2b` followed by the number of seconds instead of `+`

expiretm

string

Expiry time on GTD orders can be set up to one month in future, it is specified as an absolute timestamp or as a number of seconds from now:

  * • `0` no expiration (default)
  * • `<n>` = unix timestamp of expiration time
  * • `+<n>` = expire `<n>` seconds from now, minimum 5 seconds 
* Note that URL encoding of the `+` character changes it to a space, so please use `%2b` followed by the number of seconds instead of `+`

close[ordertype]

enum<string>

Conditional close order type

> Note: [Conditional close orders](https://support.kraken.com/hc/en-us/articles/360038640052-Conditional-Close) are triggered by execution of the primary order in the same quantity and opposite direction, but once triggered are independent orders that may reduce or increase net position

Available options:

`limit`,

`iceberg`,

`stop-loss`,

`take-profit`,

`stop-loss-limit`,

`take-profit-limit`,

`trailing-stop`,

`trailing-stop-limit`

close[price]

string

Conditional close order `price`

Example:

`"50000.0"`

close[price2]

string

Conditional close order `price2`

deadline

string

RFC3339 timestamp (e.g. 2021-04-01T00:18:45Z) after which the matching engine should reject the new order request, in presence of latency or order queueing: min now() + 2 seconds, max now() + 60 seconds.

validate

boolean

default:false

If set to `true` the order will be validated only, it will not trade in the matching engine.

broker

string | null

Broker IIBAN (Partner's Kraken IIBAN)

#### Response

200 - application/json

Order added.

result

OrderAdded · object

Show child attributes

error

string[][]

Kraken API error

Was this page helpful?

Ctrl+I