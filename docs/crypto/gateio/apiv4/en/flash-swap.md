---
exchange: gateio
source_url: https://www.gate.com/docs/developers/apiv4/en/flash-swap
api_type: REST
updated_at: 2026-11-22 18:55:47.948309
---

# Flash_swap

Flash exchange

##  List All Supported Currency Pairs In Flash Swap

GET`/flash_swap/currency_pairs`

GET `/flash_swap/currency_pairs`

_List All Supported Currency Pairs In Flash Swap_

`BTC_GT` represents selling BTC and buying GT. The limits for each currency may vary across different currency pairs.

It is not necessary that two currencies that can be swapped instantaneously can be exchanged with each other. For example, it is possible to sell BTC and buy GT, but it does not necessarily mean that GT can be sold to buy BTC.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
currency | query | string | Optional | Query by specified currency name  
page | query | integer(int32) | Optional | Page number  
limit | query | integer(int32) | Optional | Maximum number of items returned. Default: 1000, minimum: 1, maximum: 1000  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | [FlashSwapCurrencyPair]  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
array |   
  
**items**

List all supported currencies in flash swap

Type | Constraints  
---|---  
FlashSwapCurrencyPair |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
currency_pair | string | Optional | readOnly: true | Currency pair, `BTC_USDT` represents selling `BTC` and buying `USDT`  
sell_currency | string | Optional | readOnly: true | Currency to sell  
buy_currency | string | Optional | readOnly: true | Currency to buy  
sell_min_amount | string | Optional | readOnly: true | Minimum sell quantity  
sell_max_amount | string | Optional | readOnly: true | Maximum sell quantity  
buy_min_amount | string | Optional | readOnly: true | Minimum buy quantity  
buy_max_amount | string | Optional | readOnly: true | Maximum buy quantity  
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/flash_swap/currency_pairs'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/flash_swap/currency_pairs \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    [
      {
        "currency_pair": "BTC_USDT",
        "sell_currency": "BTC",
        "buy_currency": "USDT",
        "sell_min_amount": "0.00001",
        "sell_max_amount": "100",
        "buy_min_amount": "10",
        "buy_max_amount": "10000000"
      }
    ]
    

##  Query flash swap order list🔒 Authenticated

GET`/flash_swap/orders`

GET `/flash_swap/orders`

_Query flash swap order list_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
status | query | integer | Optional | Flash swap order status  
  
`1` \- success  
`2` \- failed  
sell_currency | query | string | Optional | Asset name to sell  
\- Retrieved from API `GET /flash_swap/currencies` for supported flash swap currencies  
buy_currency | query | string | Optional | Asset name to buy  
\- Retrieved from API `GET /flash_swap/currencies` for supported flash swap currencies  
reverse | query | boolean | Optional | Sort by ID in ascending or descending order, default `true`  
\- `true`: ID descending order (most recent data first)  
\- `false`: ID ascending order (oldest data first)  
limit | query | integer | Optional | Maximum number of records returned in a single list  
page | query | integer(int32) | Optional | Page number  
  
####  Detailed descriptions

**status** : Flash swap order status  
  
`1` \- success  
`2` \- failed

**sell_currency** : Asset name to sell  
\- Retrieved from API `GET /flash_swap/currencies` for supported flash swap currencies

**buy_currency** : Asset name to buy  
\- Retrieved from API `GET /flash_swap/currencies` for supported flash swap currencies

**reverse** : Sort by ID in ascending or descending order, default `true`  
\- `true`: ID descending order (most recent data first)  
\- `false`: ID ascending order (oldest data first)

### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [FlashSwapOrder]  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
array |   
  
**items**

Flash swap order

Type | Constraints  
---|---  
FlashSwapOrder |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | integer(int64) | Optional | readOnly: true | Flash swap order ID  
create_time | integer(int64) | Optional | readOnly: true | Creation time of order (in milliseconds)  
user_id | integer(int64) | Optional | readOnly: true | User ID  
sell_currency | string | Optional | readOnly: true | Currency to sell  
sell_amount | string | Optional | readOnly: true | Amount to sell  
buy_currency | string | Optional | readOnly: true | Currency to buy  
buy_amount | string | Optional | readOnly: true | Amount to buy  
price | string | Optional | readOnly: true | Price  
status | integer | Optional | readOnly: true | Flash swap order status  
  
`1` \- success  
`2` \- failure  
  
WARNING

To perform this operation, you must be authenticated by API key and secret

Code samples
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/flash_swap/orders'
    query_param = ''
    # for `gen_sign` implementation, refer to section `Authentication` above
    sign_headers = gen_sign('GET', prefix + url, query_param)
    headers.update(sign_headers)
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="GET"
    url="/flash_swap/orders"
    query_param=""
    body_param=''
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Example responses

> 200 Response
    
    
    [
      {
        "id": 54646,
        "create_time": 1651116876378,
        "update_time": 1651116876378,
        "user_id": 11135567,
        "sell_currency": "BTC",
        "sell_amount": "0.01",
        "buy_currency": "USDT",
        "buy_amount": "10",
        "price": "100",
        "status": 1
      }
    ]
    

##  Create a flash swap order🔒 Authenticated

POST`/flash_swap/orders`

POST `/flash_swap/orders`

_Create a flash swap order_

Initiate a flash swap preview in advance because order creation requires a preview result

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | FlashSwapOrderRequest | Required | none  
preview_id | body | string | Required | Preview result ID  
sell_currency | body | string | Required | Name of the asset to be sold, obtained from the interface GET /flash_swap/currency_pairs: Query the list of all trading pairs supporting flash swap  
sell_amount | body | string | Required | Amount to sell (based on the preview result)  
buy_currency | body | string | Required | Name of the asset to be bought, obtained from the interface GET /flash_swap/currency_pairs: Query the list of all trading pairs supporting flash swap  
buy_amount | body | string | Required | Amount to buy (based on the preview result)  
  
####  Request Body Schema

Parameters of flash swap order creation

Request Body SchemaType | Constraints  
---|---  
FlashSwapOrderRequest | required: ["preview_id","sell_currency","sell_amount","buy_currency","buy_amount"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
preview_id | string | Required |  | Preview result ID  
sell_currency | string | Required |  | Name of the asset to be sold, obtained from the interface GET /flash_swap/currency_pairs: Query the list of all trading pairs supporting flash swap  
sell_amount | string | Required |  | Amount to sell (based on the preview result)  
buy_currency | string | Required |  | Name of the asset to be bought, obtained from the interface GET /flash_swap/currency_pairs: Query the list of all trading pairs supporting flash swap  
buy_amount | string | Required |  | Amount to buy (based on the preview result)  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
201 | [Created ](https://tools.ietf.org/html/rfc7231#section-6.3.2) | Flash swap order created successfully | FlashSwapOrder  
  
### Response Schema

Status Code **201**

Flash swap order

Type | Constraints  
---|---  
FlashSwapOrder |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | integer(int64) | Optional | readOnly: true | Flash swap order ID  
create_time | integer(int64) | Optional | readOnly: true | Creation time of order (in milliseconds)  
user_id | integer(int64) | Optional | readOnly: true | User ID  
sell_currency | string | Optional | readOnly: true | Currency to sell  
sell_amount | string | Optional | readOnly: true | Amount to sell  
buy_currency | string | Optional | readOnly: true | Currency to buy  
buy_amount | string | Optional | readOnly: true | Amount to buy  
price | string | Optional | readOnly: true | Price  
status | integer | Optional | readOnly: true | Flash swap order status  
  
`1` \- success  
`2` \- failure  
  
WARNING

To perform this operation, you must be authenticated by API key and secret

Code samples
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/flash_swap/orders'
    query_param = ''
    body='{"preview_id":"4564564","sell_currency":"BTC","sell_amount":"0.1","buy_currency":"USDT","buy_amount":"10"}'
    # for `gen_sign` implementation, refer to section `Authentication` above
    sign_headers = gen_sign('POST', prefix + url, query_param, body)
    headers.update(sign_headers)
    r = requests.request('POST', host + prefix + url, headers=headers, data=body)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="POST"
    url="/flash_swap/orders"
    query_param=""
    body_param='{"preview_id":"4564564","sell_currency":"BTC","sell_amount":"0.1","buy_currency":"USDT","buy_amount":"10"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "preview_id": "4564564",
      "sell_currency": "BTC",
      "sell_amount": "0.1",
      "buy_currency": "USDT",
      "buy_amount": "10"
    }
    

> Example responses

> 201 Response
    
    
    {
      "id": 54646,
      "create_time": 1651116876378,
      "update_time": 1651116876378,
      "user_id": 11135567,
      "sell_currency": "BTC",
      "sell_amount": "0.01",
      "buy_currency": "USDT",
      "buy_amount": "10",
      "price": "100",
      "status": 1
    }
    

##  Query single flash swap order🔒 Authenticated

GET`/flash_swap/orders/{order_id}`

GET `/flash_swap/orders/{order_id}`

_Query single flash swap order_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
order_id | path | integer | Required | Flash swap order ID  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | FlashSwapOrder  
  
### Response Schema

Status Code **200**

Flash swap order

Type | Constraints  
---|---  
FlashSwapOrder |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | integer(int64) | Optional | readOnly: true | Flash swap order ID  
create_time | integer(int64) | Optional | readOnly: true | Creation time of order (in milliseconds)  
user_id | integer(int64) | Optional | readOnly: true | User ID  
sell_currency | string | Optional | readOnly: true | Currency to sell  
sell_amount | string | Optional | readOnly: true | Amount to sell  
buy_currency | string | Optional | readOnly: true | Currency to buy  
buy_amount | string | Optional | readOnly: true | Amount to buy  
price | string | Optional | readOnly: true | Price  
status | integer | Optional | readOnly: true | Flash swap order status  
  
`1` \- success  
`2` \- failure  
  
WARNING

To perform this operation, you must be authenticated by API key and secret

Code samples
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/flash_swap/orders/1'
    query_param = ''
    # for `gen_sign` implementation, refer to section `Authentication` above
    sign_headers = gen_sign('GET', prefix + url, query_param)
    headers.update(sign_headers)
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="GET"
    url="/flash_swap/orders/1"
    query_param=""
    body_param=''
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Example responses

> 200 Response
    
    
    {
      "id": 54646,
      "create_time": 1651116876378,
      "update_time": 1651116876378,
      "user_id": 11135567,
      "sell_currency": "BTC",
      "sell_amount": "0.01",
      "buy_currency": "USDT",
      "buy_amount": "10",
      "price": "100",
      "status": 1
    }
    

##  Flash swap order preview🔒 Authenticated

POST`/flash_swap/orders/preview`

POST `/flash_swap/orders/preview`

_Flash swap order preview_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | FlashSwapPreviewRequest | Required | none  
sell_currency | body | string | Required | The name of the asset being sold, as obtained from the "GET /flash_swap/currency_pairs" API, which retrieves a list of supported flash swap currency pairs  
sell_amount | body | string | Optional | Amount to sell.  
It is required to choose one parameter between `sell_amount` and `buy_amount`  
buy_currency | body | string | Required | The name of the asset being purchased, as obtained from the "GET /flash_swap/currency_pairs" API, which provides a list of supported flash swap currency pairs  
buy_amount | body | string | Optional | Amount to buy.  
It is required to choose one parameter between `sell_amount` and `buy_amount`  
  
####  Detailed descriptions

** sell_amount**: Amount to sell.  
It is required to choose one parameter between `sell_amount` and `buy_amount`

** buy_amount**: Amount to buy.  
It is required to choose one parameter between `sell_amount` and `buy_amount`

####  Request Body Schema

Parameters of flash swap order creation

Request Body SchemaType | Constraints  
---|---  
FlashSwapPreviewRequest | required: ["sell_currency","buy_currency"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
sell_currency | string | Required |  | The name of the asset being sold, as obtained from the "GET /flash_swap/currency_pairs" API, which retrieves a list of supported flash swap currency pairs  
sell_amount | string | Optional |  | Amount to sell.  
It is required to choose one parameter between `sell_amount` and `buy_amount`  
buy_currency | string | Required |  | The name of the asset being purchased, as obtained from the "GET /flash_swap/currency_pairs" API, which provides a list of supported flash swap currency pairs  
buy_amount | string | Optional |  | Amount to buy.  
It is required to choose one parameter between `sell_amount` and `buy_amount`  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Flash swap order preview successful | FlashSwapOrderPreview  
  
### Response Schema

Status Code **200**

Flash swap order preview

Type | Constraints  
---|---  
FlashSwapOrderPreview |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
preview_id | string | Optional |  | Preview result ID  
sell_currency | string | Optional |  | Name of the sold asset,  
Refer to the interface Query the list of currencies supported for flash swap GET /flash_swap/currenciesto obtain  
sell_amount | string | Optional |  | Amount to sell  
buy_currency | string | Optional |  | Name of the purchased asset,  
Refer to the interface Query the list of currencies supported for flash swap GET /flash_swap/currenciesto obtain  
buy_amount | string | Optional |  | Amount to buy  
price | string | Optional |  | Price  
  
WARNING

To perform this operation, you must be authenticated by API key and secret

Code samples
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/flash_swap/orders/preview'
    query_param = ''
    body='{"sell_currency":"BTC","sell_amount":"0.1","buy_currency":"USDT"}'
    # for `gen_sign` implementation, refer to section `Authentication` above
    sign_headers = gen_sign('POST', prefix + url, query_param, body)
    headers.update(sign_headers)
    r = requests.request('POST', host + prefix + url, headers=headers, data=body)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="POST"
    url="/flash_swap/orders/preview"
    query_param=""
    body_param='{"sell_currency":"BTC","sell_amount":"0.1","buy_currency":"USDT"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "sell_currency": "BTC",
      "sell_amount": "0.1",
      "buy_currency": "USDT"
    }
    

> Example responses

> 200 Response
    
    
    {
      "preview_id": "3453434",
      "sell_currency": "BTC",
      "sell_amount": "0.1",
      "buy_currency": "USDT",
      "buy_amount": "10",
      "price": "100"
    }
    

##  List Flash Swap currency pairs

GET`/flash-swap/v1/currency-pair`

GET `/flash-swap/v1/currency-pair`

_List Flash Swap currency pairs_

List available Flash Swap currency pairs and buy/sell amount limits for the specified currency and trading side

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
asset_name | query | string | Required | Currency name  
side | query | integer(int32) | Required | Trading side  
\- `1`: Sell  
\- `2`: Buy  
X-Gate-Region | header | string | Optional | User region  
  
####  Detailed descriptions

**side** : Trading side  
\- `1`: Sell  
\- `2`: Buy

####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
side | 1  
side | 2  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Successful response | FlashSwapV1CurrencyPairListResp  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Invalid parameters | FlashSwapErrorResponse  
404 | [Not Found ](https://tools.ietf.org/html/rfc7231#section-6.5.4) | Record does not exist | FlashSwapErrorResponse  
  
### Response Schema

Status Code **200**

FlashSwapV1CurrencyPairListResp

Flash Swap V1 currency pair list

Type | Constraints  
---|---  
FlashSwapV1CurrencyPairListResp | required: ["currency_pair"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
currency_pair | array | Required |  | Available currency pairs for Flash Swap  
  
**currency_pair**

Available currency pairs for Flash Swap

Type | Constraints  
---|---  
array |   
  
**currency_pair / items**

FlashSwapV1CurrencyPair

Flash Swap V1 currency pair information

Type | Constraints  
---|---  
FlashSwapV1CurrencyPair | required: ["market","sell_asset","sell_min_amount","sell_max_amount","buy_asset","buy_min_amount","buy_max_amount"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
market | string | Required | readOnly: true | Market identifier, e.g. `BTC_USDT` means selling BTC to buy USDT  
sell_asset | string | Required | readOnly: true | Currency to sell  
sell_min_amount | string | Required | readOnly: true | Minimum sell quantity  
sell_max_amount | string | Required | readOnly: true | Maximum sell quantity  
buy_asset | string | Required | readOnly: true | Currency to buy  
buy_min_amount | string | Required | readOnly: true | Minimum buy quantity  
buy_max_amount | string | Required | readOnly: true | Maximum buy quantity  
  
Status Code **400**

FlashSwapErrorResponse

Type | Constraints  
---|---  
FlashSwapErrorResponse | required: ["code","message"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
code | integer | Required |  | Error code  
message | string | Required |  | Error message  
  
Status Code **404**

FlashSwapErrorResponse

Type | Constraints  
---|---  
FlashSwapErrorResponse | required: ["code","message"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
code | integer | Required |  | Error code  
message | string | Required |  | Error message  
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/flash-swap/v1/currency-pair'
    query_param = 'asset_name=BTC&side=1'
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/flash-swap/v1/currency-pair?asset_name=BTC&side=1 \
      -H 'Accept: application/json' \
      -H 'X-Gate-Region: string'
    
    

> Example responses

> 200 Response
    
    
    {
      "currency_pair": [
        {
          "market": "BTC_USDT",
          "sell_asset": "BTC",
          "sell_min_amount": "0.00001",
          "sell_max_amount": "100",
          "buy_asset": "USDT",
          "buy_min_amount": "10",
          "buy_max_amount": "10000000"
        }
      ]
    }
    

> 400 Response
    
    
    {
      "code": 0,
      "message": "string"
    }
    

#  Schemas

##  FlashSwapOrder

Flash swap order

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | integer(int64) | Optional | readOnly: true | Flash swap order ID  
create_time | integer(int64) | Optional | readOnly: true | Creation time of order (in milliseconds)  
user_id | integer(int64) | Optional | readOnly: true | User ID  
sell_currency | string | Optional | readOnly: true | Currency to sell  
sell_amount | string | Optional | readOnly: true | Amount to sell  
buy_currency | string | Optional | readOnly: true | Currency to buy  
buy_amount | string | Optional | readOnly: true | Amount to buy  
price | string | Optional | readOnly: true | Price  
status | integer | Optional | readOnly: true | Flash swap order status  
  
`1` \- success  
`2` \- failure  
      
    
    {
      "id": 0,
      "create_time": 0,
      "user_id": 0,
      "sell_currency": "string",
      "sell_amount": "string",
      "buy_currency": "string",
      "buy_amount": "string",
      "price": "string",
      "status": 0
    }
    
    

##  FlashSwapErrorResponse

FlashSwapErrorResponse

Type | Constraints  
---|---  
object | required: ["code","message"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
code | integer | Required |  | Error code  
message | string | Required |  | Error message  
      
    
    {
      "code": 0,
      "message": "string"
    }
    
    

##  FlashSwapOrderRequest

Parameters of flash swap order creation

Type | Constraints  
---|---  
object | required: ["preview_id","sell_currency","sell_amount","buy_currency","buy_amount"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
preview_id | string | Required |  | Preview result ID  
sell_currency | string | Required |  | Name of the asset to be sold, obtained from the interface GET /flash_swap/currency_pairs: Query the list of all trading pairs supporting flash swap  
sell_amount | string | Required |  | Amount to sell (based on the preview result)  
buy_currency | string | Required |  | Name of the asset to be bought, obtained from the interface GET /flash_swap/currency_pairs: Query the list of all trading pairs supporting flash swap  
buy_amount | string | Required |  | Amount to buy (based on the preview result)  
      
    
    {
      "preview_id": "string",
      "sell_currency": "string",
      "sell_amount": "string",
      "buy_currency": "string",
      "buy_amount": "string"
    }
    
    

##  FlashSwapV1CurrencyPairListResp

FlashSwapV1CurrencyPairListResp

Flash Swap V1 currency pair list

Type | Constraints  
---|---  
object | required: ["currency_pair"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
currency_pair | array | Required |  | Available currency pairs for Flash Swap  
  
**currency_pair**

Available currency pairs for Flash Swap

Type | Constraints  
---|---  
array |   
  
**currency_pair / items**

FlashSwapV1CurrencyPair

Flash Swap V1 currency pair information

Type | Constraints  
---|---  
FlashSwapV1CurrencyPair | required: ["market","sell_asset","sell_min_amount","sell_max_amount","buy_asset","buy_min_amount","buy_max_amount"]  
      
    
    {
      "currency_pair": [
        {
          "market": "string",
          "sell_asset": "string",
          "sell_min_amount": "string",
          "sell_max_amount": "string",
          "buy_asset": "string",
          "buy_min_amount": "string",
          "buy_max_amount": "string"
        }
      ]
    }
    
    

##  FlashSwapOrderPreview

Flash swap order preview

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
preview_id | string | Optional |  | Preview result ID  
sell_currency | string | Optional |  | Name of the sold asset,  
Refer to the interface Query the list of currencies supported for flash swap GET /flash_swap/currenciesto obtain  
sell_amount | string | Optional |  | Amount to sell  
buy_currency | string | Optional |  | Name of the purchased asset,  
Refer to the interface Query the list of currencies supported for flash swap GET /flash_swap/currenciesto obtain  
buy_amount | string | Optional |  | Amount to buy  
price | string | Optional |  | Price  
      
    
    {
      "preview_id": "string",
      "sell_currency": "string",
      "sell_amount": "string",
      "buy_currency": "string",
      "buy_amount": "string",
      "price": "string"
    }
    
    

##  FlashSwapCurrencyPair

List all supported currencies in flash swap

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
currency_pair | string | Optional | readOnly: true | Currency pair, `BTC_USDT` represents selling `BTC` and buying `USDT`  
sell_currency | string | Optional | readOnly: true | Currency to sell  
buy_currency | string | Optional | readOnly: true | Currency to buy  
sell_min_amount | string | Optional | readOnly: true | Minimum sell quantity  
sell_max_amount | string | Optional | readOnly: true | Maximum sell quantity  
buy_min_amount | string | Optional | readOnly: true | Minimum buy quantity  
buy_max_amount | string | Optional | readOnly: true | Maximum buy quantity  
      
    
    {
      "currency_pair": "string",
      "sell_currency": "BTC",
      "buy_currency": "USDT",
      "sell_min_amount": "0.00001",
      "sell_max_amount": "100",
      "buy_min_amount": "10",
      "buy_max_amount": "10000000"
    }
    
    

##  FlashSwapPreviewRequest

Parameters of flash swap order creation

Type | Constraints  
---|---  
object | required: ["sell_currency","buy_currency"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
sell_currency | string | Required |  | The name of the asset being sold, as obtained from the "GET /flash_swap/currency_pairs" API, which retrieves a list of supported flash swap currency pairs  
sell_amount | string | Optional |  | Amount to sell.  
It is required to choose one parameter between `sell_amount` and `buy_amount`  
buy_currency | string | Required |  | The name of the asset being purchased, as obtained from the "GET /flash_swap/currency_pairs" API, which provides a list of supported flash swap currency pairs  
buy_amount | string | Optional |  | Amount to buy.  
It is required to choose one parameter between `sell_amount` and `buy_amount`  
      
    
    {
      "sell_currency": "string",
      "sell_amount": "string",
      "buy_currency": "string",
      "buy_amount": "string"
    }
    
    

##  FlashSwapV1CurrencyPair

FlashSwapV1CurrencyPair

Flash Swap V1 currency pair information

Type | Constraints  
---|---  
object | required: ["market","sell_asset","sell_min_amount","sell_max_amount","buy_asset","buy_min_amount","buy_max_amount"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
market | string | Required | readOnly: true | Market identifier, e.g. `BTC_USDT` means selling BTC to buy USDT  
sell_asset | string | Required | readOnly: true | Currency to sell  
sell_min_amount | string | Required | readOnly: true | Minimum sell quantity  
sell_max_amount | string | Required | readOnly: true | Maximum sell quantity  
buy_asset | string | Required | readOnly: true | Currency to buy  
buy_min_amount | string | Required | readOnly: true | Minimum buy quantity  
buy_max_amount | string | Required | readOnly: true | Maximum buy quantity  
      
    
    {
      "market": "string",
      "sell_asset": "string",
      "sell_min_amount": "string",
      "sell_max_amount": "string",
      "buy_asset": "string",
      "buy_min_amount": "string",
      "buy_max_amount": "string"
    }