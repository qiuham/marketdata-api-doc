---
exchange: gateio
source_url: https://www.gate.com/docs/developers/apiv4/en/earn
api_type: Earn
updated_at: 2026-11-22 18:55:44.884388
---

# Earn

Earn service

##  Dual Investment product list

GET`/earn/dual/investment_plan`

GET `/earn/dual/investment_plan`

_Dual Investment product list_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
plan_id | query | integer(int64) | Optional | Financial project ID  
coin | query | string | Optional | Investment Token  
type | query | string | Optional | Type enum: `put` — buy low; `call` — sell high  
quote_currency | query | string | Optional | Settlement currency enum: defaults to USDT; GUSD optional  
sort | query | string | Optional | Sort field enum:  
`apy` — highest APY first  
`short-period` — shortest tenor first  
`multiple` — highest premium first  
page | query | integer | Optional | page number  
page_size | query | integer | Optional | Items per page  
  
####  Detailed descriptions

**sort** : Sort field enum:  
`apy` — highest APY first  
`short-period` — shortest tenor first  
`multiple` — highest premium first

### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Successfully retrieved | [DualGetPlans]  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
array |   
  
**items**

Type | Constraints  
---|---  
DualGetPlans |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | integer(int32) | Optional |  | Product ID  
instrument_name | string | Optional |  | Product Name  
type | string | Optional |  | `call`: sell high; `put`: buy low  
invest_currency | string | Optional |  | Investment Token  
exercise_currency | string | Optional |  | Strike Token  
exercise_price | number(double) | Optional |  | Strike price  
delivery_time | integer(int32) | Optional |  | Settlement time  
apy_display | string | Optional |  | Annual Yield  
min_amount | string | Optional |  | Minimum investment amount  
start_time | integer(int32) | Optional |  | Start Time  
end_time | integer(int32) | Optional |  | End time  
status | string | Optional |  | Status:  
  
`NOTSTARTED` \- Not started  
`ONGOING` \- In progress  
`ENDED` \- Ended  
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/earn/dual/investment_plan'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/earn/dual/investment_plan \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    [
      {
        "id": 272,
        "instrument_name": "DOGE-17NOV23-0.067-P",
        "type": "put",
        "invest_currency": "USDT",
        "exercise_currency": "DOGE",
        "exercise_price": 0.067,
        "delivery_time": 1700208000,
        "start_time": 1697685172,
        "end_time": 1697685172,
        "status": "ONGOING",
        "apy_display": "0.0114000000",
        "min_amount": "1"
      }
    ]
    

##  Dual Investment order list🔒 Authenticated

GET`/earn/dual/orders`

GET `/earn/dual/orders`

_Dual Investment order list_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
from | query | integer(int64) | Optional | Start settlement time  
to | query | integer(int64) | Optional | End settlement time  
type | query | string | Optional | Type enum: `put` — buy low; `call` — sell high  
status | query | string | Optional | Order status enum:  
`HOLD` — open position  
`REPAY` — historical position  
`PROCESSING` — position active  
`SETTLEMENT_PROCESSING` — settlement in progress  
`ALL` — all  
coin | query | string | Optional | Investment Token  
page | query | integer(int32) | Optional | Page number  
limit | query | integer | Optional | Maximum number of records returned in a single list  
  
####  Detailed descriptions

**status** : Order status enum:  
`HOLD` — open position  
`REPAY` — historical position  
`PROCESSING` — position active  
`SETTLEMENT_PROCESSING` — settlement in progress  
`ALL` — all

### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Successfully retrieved | [DualGetOrders]  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
array |   
  
**items**

Type | Constraints  
---|---  
DualGetOrders |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | integer(int32) | Optional |  | Order ID  
plan_id | integer(int32) | Optional |  | Product ID  
invest_amount | string | Optional |  | Investment Quantity  
settlement_amount | string | Optional |  | Settlement Quantity  
create_time | integer(int32) | Optional |  | Created time  
complete_time | integer(int32) | Optional |  | Completed Time  
status | string | Optional |  | Status:  
  
`INIT`-Created  
`SETTLEMENT_SUCCESS`-Settlement Success  
`SETTLEMENT_PROCESSING`-Settlement Processing  
`CANCELED`-Canceled  
`FAILED`-Failed  
invest_currency | string | Optional |  | Investment Token  
exercise_currency | string | Optional |  | Strike Token  
exercise_price | string | Optional |  | Strike price  
settlement_price | string | Optional |  | Settlement price  
settlement_currency | string | Optional |  | Settlement currency  
apy_display | string | Optional |  | Annual Yield  
apy_settlement | string | Optional |  | Settlement Annual Yield  
delivery_time | integer(int32) | Optional |  | Settlement time  
text | string | Optional |  | Custom order information  
  
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
    
    url = '/earn/dual/orders'
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
    url="/earn/dual/orders"
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
        "id": 373,
        "plan_id": 176,
        "invest_amount": "0.0000000000",
        "settlement_amount": "0.0000000000",
        "create_time": 1697685172,
        "complete_time": 1697685172,
        "status": "CANCELED",
        "invest_currency": "USDT",
        "exercise_currency": "BTC",
        "settlement_currency": "",
        "exercise_price": "24500.0000000000",
        "settlement_price": "0.0000000000",
        "delivery_time": 1697685172,
        "apy_display": "0.6800000000",
        "apy_settlement": "0.0000000000",
        "text": "t-custom-text"
      }
    ]
    

##  Place Dual Investment order🔒 Authenticated

POST`/earn/dual/orders`

POST `/earn/dual/orders`

_Place Dual Investment order_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | PlaceDualInvestmentOrderParams | Required | none  
plan_id | body | string | Required | Product ID  
amount | body | string | Required | Subscription amount  
text | body | string | Optional | Order custom information. Users can set custom ID with this field. Custom fields must meet the following conditions:  
  
1\. Must start with `t-`  
2\. Excluding `t-`, length cannot exceed 28 bytes  
3\. Can only contain numbers, letters, underscore(_), hyphen(-) or dot(.)  
  
  
####  Detailed descriptions

** text**: Order custom information. Users can set custom ID with this field. Custom fields must meet the following conditions:  
  
1\. Must start with `t-`  
2\. Excluding `t-`, length cannot exceed 28 bytes  
3\. Can only contain numbers, letters, underscore(_), hyphen(-) or dot(.)  

####  Request Body Schema

Dual Investment Order

Request Body SchemaType | Constraints  
---|---  
PlaceDualInvestmentOrderParams | required: ["plan_id","amount"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
plan_id | string | Required |  | Product ID  
amount | string | Required |  | Subscription amount  
text | string | Optional |  | Order custom information. Users can set custom ID with this field. Custom fields must meet the following conditions:  
  
1\. Must start with `t-`  
2\. Excluding `t-`, length cannot exceed 28 bytes  
3\. Can only contain numbers, letters, underscore(_), hyphen(-) or dot(.)  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Order placed successfully | PlaceDualInvestmentOrder  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
PlaceDualInvestmentOrder |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | integer(int32) | Optional |  | Order ID  
plan_id | integer(int32) | Optional |  | Product ID  
invest_amount | string | Optional |  | Investment Quantity  
settlement_amount | string | Optional |  | Settlement Quantity  
create_time | integer(int32) | Optional |  | Created time  
complete_time | integer(int32) | Optional |  | Completed Time  
status | string | Optional |  | Status:  
  
`INIT`-Created  
`SETTLEMENT_SUCCESS`-Settlement Success  
`SETTLEMENT_PROCESSING`-Settlement Processing  
`CANCELED`-Canceled  
`FAILED`-Failed  
invest_currency | string | Optional |  | Investment Token  
exercise_currency | string | Optional |  | Strike Token  
exercise_price | string | Optional |  | Strike price  
settlement_price | string | Optional |  | Settlement price  
settlement_currency | string | Optional |  | Settlement currency  
apy_display | string | Optional |  | Annual Yield  
apy_settlement | string | Optional |  | Settlement Annual Yield  
delivery_time | integer(int32) | Optional |  | Settlement time  
text | string | Optional |  | Custom order information  
  
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
    
    url = '/earn/dual/orders'
    query_param = ''
    body='{"plan_id":"176","amount":"1","text":"t-custom-text"}'
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
    url="/earn/dual/orders"
    query_param=""
    body_param='{"plan_id":"176","amount":"1","text":"t-custom-text"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "plan_id": "176",
      "amount": "1",
      "text": "t-custom-text"
    }
    

> Example responses

> 200 Response
    
    
    {
      "id": 373,
      "plan_id": 176,
      "invest_amount": "0.0000000000",
      "settlement_amount": "0.0000000000",
      "create_time": 1697685172,
      "complete_time": 1697685172,
      "status": "CANCELED",
      "invest_currency": "USDT",
      "exercise_currency": "BTC",
      "settlement_currency": "",
      "exercise_price": "24500.0000000000",
      "settlement_price": "0.0000000000",
      "delivery_time": 1697685172,
      "apy_display": "0.6800000000",
      "apy_settlement": "0.0000000000",
      "text": "t-custom-text"
    }
    

##  Dual-Currency Earning Assets🔒 Authenticated

GET`/earn/dual/balance`

GET `/earn/dual/balance`

_Dual-Currency Earning Assets_

### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Successfully retrieved | DualGetBalance  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
DualGetBalance |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
user_asset_usdt | string | Optional |  | User Assets in USDT Equivalent  
user_asset_btc | string | Optional |  | User Assets in BTC Equivalent  
user_total_interest_usdt | string | Optional |  | Total User Interest in USDT Equivalent  
user_total_interest_btc | string | Optional |  | Total User Interest in BTC Equivalent  
  
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
    
    url = '/earn/dual/balance'
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
    url="/earn/dual/balance"
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
      "user_asset_usdt": "30.13",
      "user_asset_btc": "0.00032798",
      "user_total_interest_usdt": "581.19003892",
      "user_total_interest_btc": "0.00632655"
    }
    

##  Dual-currency early redemption preview🔒 Authenticated

GET`/earn/dual/order-refund-preview`

GET `/earn/dual/order-refund-preview`

_Dual-currency early redemption preview_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
order_id | query | string | Required | Order ID  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Successfully retrieved | DualOrderRefundPreview  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
DualOrderRefundPreview |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
create_timest | integer(int64) | Optional |  | Order creation timestamp  
delivery_timest | integer(int64) | Optional |  | Order delivery timestamp  
exercise_price | string | Optional |  | Strike price  
invest_amount | string | Optional |  | Investment amount  
invest_currency | string | Optional |  | Investment Token  
name | string | Optional |  | Order name identifier  
order_id | integer(int64) | Optional |  | Order ID  
req_id | string | Optional |  | Request ID used for redemption, returned by GET /earn/dual/order-refund-preview. The request to POST /earn/dual/order-refund requires order_id and req_id.  
refund_service_charge | integer(int64) | Optional |  | Refund fee  
settle_price | string | Optional |  | Settlement price  
settlement_amount | string | Optional |  | Settlement amount  
settlement_currency | string | Optional |  | Settlement currency  
settlement_interest | string | Optional |  | Settlement interest  
settlement_principle | string | Optional |  | Settlement principal  
type | string | Optional |  | `call`: sell high; `put`: buy low  
money_back_timest | integer(int64) | Optional |  | Redemption time  
  
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
    
    url = '/earn/dual/order-refund-preview'
    query_param = 'order_id=9497'
    # for `gen_sign` implementation, refer to section `Authentication` above
    sign_headers = gen_sign('GET', prefix + url, query_param)
    headers.update(sign_headers)
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="GET"
    url="/earn/dual/order-refund-preview"
    query_param="order_id=9497"
    body_param=''
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url?$query_param"
    curl -X $method $full_url \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Example responses

> 200 Response
    
    
    {
      "create_timest": 1775027285,
      "delivery_timest": 1775289600,
      "exercise_price": "71303.44279",
      "invest_amount": "1",
      "invest_currency": "BTC",
      "name": "BTC_USDT-20260404-71303.44279-C",
      "order_id": 9497,
      "req_id": "tIvdY7nh",
      "refund_service_charge": 0,
      "settle_price": "68781.0063",
      "settlement_amount": "0.99486528",
      "settlement_currency": "BTC",
      "settlement_interest": "0",
      "settlement_principle": "0.99486528",
      "type": "call",
      "money_back_timest": 1775027958
    }
    

##  Dual-currency order early redemption🔒 Authenticated

POST`/earn/dual/order-refund`

POST `/earn/dual/order-refund`

_Dual-currency order early redemption_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | DualOrderRefundParams | Required | none  
order_id | body | string | Required | Order ID  
req_id | body | string | Required | Request ID returned by order-refund-preview  
  
####  Request Body Schema

Dual-currency order early redemption request

Request Body SchemaType | Constraints  
---|---  
DualOrderRefundParams | required: ["order_id","req_id"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
order_id | string | Required |  | Order ID  
req_id | string | Required |  | Request ID returned by order-refund-preview  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Redemption successful | None  
  
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
    
    url = '/earn/dual/order-refund'
    query_param = ''
    body='{"order_id":"9487","req_id":"OepRSEfv"}'
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
    url="/earn/dual/order-refund"
    query_param=""
    body_param='{"order_id":"9487","req_id":"OepRSEfv"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "order_id": "9487",
      "req_id": "OepRSEfv"
    }
    

##  Modify dual-currency order reinvest🔒 Authenticated

POST`/earn/dual/modify-order-reinvest`

POST `/earn/dual/modify-order-reinvest`

_Modify dual-currency order reinvest_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | DualModifyOrderReinvestParams | Required | none  
order_id | body | integer(int64) | Optional | Order ID  
status | body | integer(int32) | Optional | `0` — off; `1` — on  
effective_time_duration | body | integer(int64) | Optional | Effective duration in seconds; default 1 day (86400)  
  
####  Request Body Schema

Dual-currency order reinvest modification request

Request Body SchemaType | Constraints  
---|---  
DualModifyOrderReinvestParams |   
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
order_id | integer(int64) | Optional |  | Order ID  
status | integer(int32) | Optional |  | `0` — off; `1` — on  
effective_time_duration | integer(int64) | Optional |  | Effective duration in seconds; default 1 day (86400)  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Updated successfully | None  
  
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
    
    url = '/earn/dual/modify-order-reinvest'
    query_param = ''
    body='{"order_id":9497,"status":1,"effective_time_duration":86400}'
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
    url="/earn/dual/modify-order-reinvest"
    query_param=""
    body_param='{"order_id":9497,"status":1,"effective_time_duration":86400}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "order_id": 9497,
      "status": 1,
      "effective_time_duration": 86400
    }
    

##  Dual-currency recommended projects🔒 Authenticated

GET`/earn/dual/project-recommend`

GET `/earn/dual/project-recommend`

_Dual-currency recommended projects_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
mode | query | string | Optional | Sort mode; default `normal`:  
`senior` — curated picks (APR/tenor)  
`apy_up` — APY ascending  
`ep_down` — target price descending  
`ep_up` — target price ascending  
`dt_down` — maturity time descending  
`dt_up` — maturity time ascending  
coin | query | string | Optional | Investment Token  
type | query | string | Optional | `call`: sell high; `put`: buy low  
history_pids | query | string | Optional | Comma-separated project IDs to exclude already recommended items  
  
####  Detailed descriptions

**mode** : Sort mode; default `normal`:  
`senior` — curated picks (APR/tenor)  
`apy_up` — APY ascending  
`ep_down` — target price descending  
`ep_up` — target price ascending  
`dt_down` — maturity time descending  
`dt_up` — maturity time ascending

### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Successfully retrieved | [DualProjectRecommend]  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
array |   
  
**items**

Type | Constraints  
---|---  
DualProjectRecommend |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | integer(int64) | Optional |  | Product ID  
category | integer(int32) | Optional |  | Strategy category  
type | string | Optional |  | `call`: sell high; `put`: buy low  
invest_currency | string | Optional |  | Investment Token  
exercise_currency | string | Optional |  | Strike Token  
apy_display | string | Optional |  | Annual Yield  
exercise_price | string | Optional |  | Strike price  
delivery_timest | integer(int64) | Optional |  | Settlement time  
min_amount | string | Optional |  | Minimum investment amount  
max_amount | string | Optional |  | Maximum investment amount  
min_copies | integer(int64) | Optional |  | Minimum Units  
max_copies | integer(int64) | Optional |  | Maximum Units  
invest_days | integer(int64) | Optional |  | Lock-up days  
invest_hours | string | Optional |  | Lock-up hours  
  
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
    
    url = '/earn/dual/project-recommend'
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
    url="/earn/dual/project-recommend"
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
        "id": 110669,
        "category": 1,
        "type": "call",
        "invest_currency": "BTC",
        "exercise_currency": "USDT",
        "apy_display": "2.60",
        "exercise_price": "71303.44279",
        "delivery_timest": 1775289600,
        "min_amount": "1",
        "max_amount": "100000",
        "min_copies": 1,
        "max_copies": 100000,
        "invest_days": 2,
        "invest_hours": "70.43458031"
      }
    ]
    

##  List stock dual investment products

GET`/earn/dual/stock/investment_plan`

GET `/earn/dual/stock/investment_plan`

_List stock dual investment products_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
plan_id | query | string | Optional | Product/plan ID. If provided, only the matching product is returned  
coin | query | string | Optional | Underlying currency  
type | query | string | Optional | Type enum: `put` — buy low; `call` — sell high  
quote_currency | query | string | Optional | Settlement currency. Default: USDT  
sort | query | string | Optional | Sort field enum:  
`apy` — highest APY first  
`short-period` — shortest tenor first  
`multiple` — highest premium first  
page | query | integer | Optional | page number  
page_size | query | integer | Optional | Items per page，Maximum 100  
  
####  Detailed descriptions

**sort** : Sort field enum:  
`apy` — highest APY first  
`short-period` — shortest tenor first  
`multiple` — highest premium first

####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
type | call  
type | put  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Successfully retrieved | [DualGetPlans]  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
array |   
  
**items**

Type | Constraints  
---|---  
DualGetPlans |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | integer(int32) | Optional |  | Product ID  
instrument_name | string | Optional |  | Product Name  
type | string | Optional |  | `call`: sell high; `put`: buy low  
invest_currency | string | Optional |  | Investment Token  
exercise_currency | string | Optional |  | Strike Token  
exercise_price | number(double) | Optional |  | Strike price  
delivery_time | integer(int32) | Optional |  | Settlement time  
apy_display | string | Optional |  | Annual Yield  
min_amount | string | Optional |  | Minimum investment amount  
start_time | integer(int32) | Optional |  | Start Time  
end_time | integer(int32) | Optional |  | End time  
status | string | Optional |  | Status:  
  
`NOTSTARTED` \- Not started  
`ONGOING` \- In progress  
`ENDED` \- Ended  
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/earn/dual/stock/investment_plan'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/earn/dual/stock/investment_plan \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    [
      {
        "id": 272,
        "instrument_name": "DOGE-17NOV23-0.067-P",
        "type": "put",
        "invest_currency": "USDT",
        "exercise_currency": "DOGE",
        "exercise_price": 0.067,
        "delivery_time": 1700208000,
        "start_time": 1697685172,
        "end_time": 1697685172,
        "status": "ONGOING",
        "apy_display": "0.0114000000",
        "min_amount": "1"
      }
    ]
    

##  Get recommendations for stock dual investment products

GET`/earn/dual/stock/project-recommend`

GET `/earn/dual/stock/project-recommend`

_Get recommendations for stock dual investment products_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
coin | query | string | Optional | Underlying currency  
type | query | string | Optional | `call`: sell high; `put`: buy low  
mode | query | string | Optional | Recommendation mode. Default: normal  
normal: Regular users  
senior: Experienced users  
history_pids | query | string | Optional | Previously recommended project IDs, separated by commas  
  
####  Detailed descriptions

**mode** : Recommendation mode. Default: normal  
normal: Regular users  
senior: Experienced users

####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
type | call  
type | put  
mode | normal  
mode | senior  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Successfully retrieved | [DualProjectRecommend]  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
array |   
  
**items**

Type | Constraints  
---|---  
DualProjectRecommend |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | integer(int64) | Optional |  | Product ID  
category | integer(int32) | Optional |  | Strategy category  
type | string | Optional |  | `call`: sell high; `put`: buy low  
invest_currency | string | Optional |  | Investment Token  
exercise_currency | string | Optional |  | Strike Token  
apy_display | string | Optional |  | Annual Yield  
exercise_price | string | Optional |  | Strike price  
delivery_timest | integer(int64) | Optional |  | Settlement time  
min_amount | string | Optional |  | Minimum investment amount  
max_amount | string | Optional |  | Maximum investment amount  
min_copies | integer(int64) | Optional |  | Minimum Units  
max_copies | integer(int64) | Optional |  | Maximum Units  
invest_days | integer(int64) | Optional |  | Lock-up days  
invest_hours | string | Optional |  | Lock-up hours  
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/earn/dual/stock/project-recommend'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/earn/dual/stock/project-recommend \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    [
      {
        "id": 110669,
        "category": 1,
        "type": "call",
        "invest_currency": "BTC",
        "exercise_currency": "USDT",
        "apy_display": "2.60",
        "exercise_price": "71303.44279",
        "delivery_timest": 1775289600,
        "min_amount": "1",
        "max_amount": "100000",
        "min_copies": 1,
        "max_copies": 100000,
        "invest_days": 2,
        "invest_hours": "70.43458031"
      }
    ]
    

##  List stock dual investment orders🔒 Authenticated

GET`/earn/dual/stock/orders`

GET `/earn/dual/stock/orders`

_List stock dual investment orders_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
coin | query | string | Optional | Investment Token  
status | query | string | Optional | Filter by order status. Default: ALL  
HOLD: Current holdings  
REPAY: Historical holdings  
PROCESSING: Holding in progress  
SETTLEMENT_PROCESSING: Settlement in progress  
ALL: All orders  
type | query | string | Optional | Type enum: `put` — buy low; `call` — sell high  
from | query | integer(int64) | Optional | Start of the time range, in Unix seconds  
to | query | integer(int64) | Optional | End of the time range, in Unix seconds  
page | query | integer(int32) | Optional | Page number  
page_size | query | integer | Optional | Number of records per page, up to 100. Defaults to 100 when omitted  
limit | query | integer | Optional | Maximum number of records returned in a single list  
  
####  Detailed descriptions

**status** : Filter by order status. Default: ALL  
HOLD: Current holdings  
REPAY: Historical holdings  
PROCESSING: Holding in progress  
SETTLEMENT_PROCESSING: Settlement in progress  
ALL: All orders

####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
type | call  
type | put  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Successfully retrieved | [DualGetOrders]  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
array |   
  
**items**

Type | Constraints  
---|---  
DualGetOrders |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | integer(int32) | Optional |  | Order ID  
plan_id | integer(int32) | Optional |  | Product ID  
invest_amount | string | Optional |  | Investment Quantity  
settlement_amount | string | Optional |  | Settlement Quantity  
create_time | integer(int32) | Optional |  | Created time  
complete_time | integer(int32) | Optional |  | Completed Time  
status | string | Optional |  | Status:  
  
`INIT`-Created  
`SETTLEMENT_SUCCESS`-Settlement Success  
`SETTLEMENT_PROCESSING`-Settlement Processing  
`CANCELED`-Canceled  
`FAILED`-Failed  
invest_currency | string | Optional |  | Investment Token  
exercise_currency | string | Optional |  | Strike Token  
exercise_price | string | Optional |  | Strike price  
settlement_price | string | Optional |  | Settlement price  
settlement_currency | string | Optional |  | Settlement currency  
apy_display | string | Optional |  | Annual Yield  
apy_settlement | string | Optional |  | Settlement Annual Yield  
delivery_time | integer(int32) | Optional |  | Settlement time  
text | string | Optional |  | Custom order information  
  
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
    
    url = '/earn/dual/stock/orders'
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
    url="/earn/dual/stock/orders"
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
        "id": 373,
        "plan_id": 176,
        "invest_amount": "0.0000000000",
        "settlement_amount": "0.0000000000",
        "create_time": 1697685172,
        "complete_time": 1697685172,
        "status": "CANCELED",
        "invest_currency": "USDT",
        "exercise_currency": "BTC",
        "settlement_currency": "",
        "exercise_price": "24500.0000000000",
        "settlement_price": "0.0000000000",
        "delivery_time": 1697685172,
        "apy_display": "0.6800000000",
        "apy_settlement": "0.0000000000",
        "text": "t-custom-text"
      }
    ]
    

##  Place a stock dual investment order🔒 Authenticated

POST`/earn/dual/stock/orders`

POST `/earn/dual/stock/orders`

_Place a stock dual investment order_

For buy-low (put) products, optionally pass `hit_spot`, `hit_stock`, and `hit_simple` (`1` selects the corresponding funding account) to collect funds from the spot, stock, or Simple Earn accounts before subscribing.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | PlaceDualStockInvestmentOrderParams | Required | none  
plan_id | body | string | Required | Product ID  
amount | body | string | Required | Subscription amount  
text | body | string | Optional | Order custom information. Users can set custom ID with this field. Custom fields must meet the following conditions:  
  
1\. Must start with `t-`  
2\. Excluding `t-`, length cannot exceed 28 bytes  
3\. Can only contain numbers, letters, underscore(_), hyphen(-) or dot(.)  
  
hit_spot | body | integer | Optional | Whether to use the spot account to fund a buy-low (put) subscription. `1` selects the account; omitted or other values leave it unselected.  
hit_stock | body | integer | Optional | Whether to use the stock account to fund a buy-low (put) subscription. `1` selects the account; omitted or other values leave it unselected.  
hit_simple | body | integer | Optional | Whether to use the Simple Earn account to fund a buy-low (put) subscription. `1` selects the account; omitted or other values leave it unselected.  
  
####  Detailed descriptions

** text**: Order custom information. Users can set custom ID with this field. Custom fields must meet the following conditions:  
  
1\. Must start with `t-`  
2\. Excluding `t-`, length cannot exceed 28 bytes  
3\. Can only contain numbers, letters, underscore(_), hyphen(-) or dot(.)  

####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
hit_spot | 0  
hit_spot | 1  
hit_stock | 0  
hit_stock | 1  
hit_simple | 0  
hit_simple | 1  
  
####  Request Body Schema

Stock dual investment order request

Request Body SchemaType | Constraints  
---|---  
PlaceDualStockInvestmentOrderParams | required: ["plan_id","amount"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
plan_id | string | Required |  | Product ID  
amount | string | Required |  | Subscription amount  
text | string | Optional |  | Order custom information. Users can set custom ID with this field. Custom fields must meet the following conditions:  
  
1\. Must start with `t-`  
2\. Excluding `t-`, length cannot exceed 28 bytes  
3\. Can only contain numbers, letters, underscore(_), hyphen(-) or dot(.)  
hit_spot | integer | Optional | enum: [0,1] | Whether to use the spot account to fund a buy-low (put) subscription. `1` selects the account; omitted or other values leave it unselected.  
hit_stock | integer | Optional | enum: [0,1] | Whether to use the stock account to fund a buy-low (put) subscription. `1` selects the account; omitted or other values leave it unselected.  
hit_simple | integer | Optional | enum: [0,1] | Whether to use the Simple Earn account to fund a buy-low (put) subscription. `1` selects the account; omitted or other values leave it unselected.  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Order placed successfully | PlaceDualInvestmentOrder  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
PlaceDualInvestmentOrder |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | integer(int32) | Optional |  | Order ID  
plan_id | integer(int32) | Optional |  | Product ID  
invest_amount | string | Optional |  | Investment Quantity  
settlement_amount | string | Optional |  | Settlement Quantity  
create_time | integer(int32) | Optional |  | Created time  
complete_time | integer(int32) | Optional |  | Completed Time  
status | string | Optional |  | Status:  
  
`INIT`-Created  
`SETTLEMENT_SUCCESS`-Settlement Success  
`SETTLEMENT_PROCESSING`-Settlement Processing  
`CANCELED`-Canceled  
`FAILED`-Failed  
invest_currency | string | Optional |  | Investment Token  
exercise_currency | string | Optional |  | Strike Token  
exercise_price | string | Optional |  | Strike price  
settlement_price | string | Optional |  | Settlement price  
settlement_currency | string | Optional |  | Settlement currency  
apy_display | string | Optional |  | Annual Yield  
apy_settlement | string | Optional |  | Settlement Annual Yield  
delivery_time | integer(int32) | Optional |  | Settlement time  
text | string | Optional |  | Custom order information  
  
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
    
    url = '/earn/dual/stock/orders'
    query_param = ''
    body='{"plan_id":"176","amount":"1","text":"t-custom-text","hit_spot":1,"hit_stock":0,"hit_simple":0}'
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
    url="/earn/dual/stock/orders"
    query_param=""
    body_param='{"plan_id":"176","amount":"1","text":"t-custom-text","hit_spot":1,"hit_stock":0,"hit_simple":0}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "plan_id": "176",
      "amount": "1",
      "text": "t-custom-text",
      "hit_spot": 1,
      "hit_stock": 0,
      "hit_simple": 0
    }
    

> Example responses

> 200 Response
    
    
    {
      "id": 373,
      "plan_id": 176,
      "invest_amount": "0.0000000000",
      "settlement_amount": "0.0000000000",
      "create_time": 1697685172,
      "complete_time": 1697685172,
      "status": "CANCELED",
      "invest_currency": "USDT",
      "exercise_currency": "BTC",
      "settlement_currency": "",
      "exercise_price": "24500.0000000000",
      "settlement_price": "0.0000000000",
      "delivery_time": 1697685172,
      "apy_display": "0.6800000000",
      "apy_settlement": "0.0000000000",
      "text": "t-custom-text"
    }
    

##  Get stock dual investment asset statistics🔒 Authenticated

GET`/earn/dual/stock/balance`

GET `/earn/dual/stock/balance`

_Get stock dual investment asset statistics_

### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Successfully retrieved | DualGetBalance  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
DualGetBalance |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
user_asset_usdt | string | Optional |  | User Assets in USDT Equivalent  
user_asset_btc | string | Optional |  | User Assets in BTC Equivalent  
user_total_interest_usdt | string | Optional |  | Total User Interest in USDT Equivalent  
user_total_interest_btc | string | Optional |  | Total User Interest in BTC Equivalent  
  
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
    
    url = '/earn/dual/stock/balance'
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
    url="/earn/dual/stock/balance"
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
      "user_asset_usdt": "30.13",
      "user_asset_btc": "0.00032798",
      "user_total_interest_usdt": "581.19003892",
      "user_total_interest_btc": "0.00632655"
    }
    

##  Preview stock dual investment redemption🔒 Authenticated

GET`/earn/dual/stock/order-refund-preview`

GET `/earn/dual/stock/order-refund-preview`

_Preview stock dual investment redemption_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
order_id | query | string | Required | Order ID  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Successfully retrieved | DualOrderRefundPreview  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
DualOrderRefundPreview |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
create_timest | integer(int64) | Optional |  | Order creation timestamp  
delivery_timest | integer(int64) | Optional |  | Order delivery timestamp  
exercise_price | string | Optional |  | Strike price  
invest_amount | string | Optional |  | Investment amount  
invest_currency | string | Optional |  | Investment Token  
name | string | Optional |  | Order name identifier  
order_id | integer(int64) | Optional |  | Order ID  
req_id | string | Optional |  | Request ID used for redemption, returned by GET /earn/dual/order-refund-preview. The request to POST /earn/dual/order-refund requires order_id and req_id.  
refund_service_charge | integer(int64) | Optional |  | Refund fee  
settle_price | string | Optional |  | Settlement price  
settlement_amount | string | Optional |  | Settlement amount  
settlement_currency | string | Optional |  | Settlement currency  
settlement_interest | string | Optional |  | Settlement interest  
settlement_principle | string | Optional |  | Settlement principal  
type | string | Optional |  | `call`: sell high; `put`: buy low  
money_back_timest | integer(int64) | Optional |  | Redemption time  
  
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
    
    url = '/earn/dual/stock/order-refund-preview'
    query_param = 'order_id=9497'
    # for `gen_sign` implementation, refer to section `Authentication` above
    sign_headers = gen_sign('GET', prefix + url, query_param)
    headers.update(sign_headers)
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="GET"
    url="/earn/dual/stock/order-refund-preview"
    query_param="order_id=9497"
    body_param=''
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url?$query_param"
    curl -X $method $full_url \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Example responses

> 200 Response
    
    
    {
      "create_timest": 1775027285,
      "delivery_timest": 1775289600,
      "exercise_price": "71303.44279",
      "invest_amount": "1",
      "invest_currency": "BTC",
      "name": "BTC_USDT-20260404-71303.44279-C",
      "order_id": 9497,
      "req_id": "tIvdY7nh",
      "refund_service_charge": 0,
      "settle_price": "68781.0063",
      "settlement_amount": "0.99486528",
      "settlement_currency": "BTC",
      "settlement_interest": "0",
      "settlement_principle": "0.99486528",
      "type": "call",
      "money_back_timest": 1775027958
    }
    

##  Redeem a stock dual investment order🔒 Authenticated

POST`/earn/dual/stock/order-refund`

POST `/earn/dual/stock/order-refund`

_Redeem a stock dual investment order_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | DualOrderRefundParams | Required | none  
order_id | body | string | Required | Order ID  
req_id | body | string | Required | Request ID returned by order-refund-preview  
  
####  Request Body Schema

Dual-currency order early redemption request

Request Body SchemaType | Constraints  
---|---  
DualOrderRefundParams | required: ["order_id","req_id"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
order_id | string | Required |  | Order ID  
req_id | string | Required |  | Request ID returned by order-refund-preview  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Redemption successful | None  
  
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
    
    url = '/earn/dual/stock/order-refund'
    query_param = ''
    body='{"order_id":"9487","req_id":"OepRSEfv"}'
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
    url="/earn/dual/stock/order-refund"
    query_param=""
    body_param='{"order_id":"9487","req_id":"OepRSEfv"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "order_id": "9487",
      "req_id": "OepRSEfv"
    }
    

##  Reinvest a stock dual investment order🔒 Authenticated

POST`/earn/dual/stock/modify-order-reinvest`

POST `/earn/dual/stock/modify-order-reinvest`

_Reinvest a stock dual investment order_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | DualModifyOrderReinvestParams | Required | none  
order_id | body | integer(int64) | Optional | Order ID  
status | body | integer(int32) | Optional | `0` — off; `1` — on  
effective_time_duration | body | integer(int64) | Optional | Effective duration in seconds; default 1 day (86400)  
  
####  Request Body Schema

Dual-currency order reinvest modification request

Request Body SchemaType | Constraints  
---|---  
DualModifyOrderReinvestParams |   
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
order_id | integer(int64) | Optional |  | Order ID  
status | integer(int32) | Optional |  | `0` — off; `1` — on  
effective_time_duration | integer(int64) | Optional |  | Effective duration in seconds; default 1 day (86400)  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Updated successfully | None  
  
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
    
    url = '/earn/dual/stock/modify-order-reinvest'
    query_param = ''
    body='{"order_id":9497,"status":1,"effective_time_duration":86400}'
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
    url="/earn/dual/stock/modify-order-reinvest"
    query_param=""
    body_param='{"order_id":9497,"status":1,"effective_time_duration":86400}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "order_id": 9497,
      "status": 1,
      "effective_time_duration": 86400
    }
    

##  Staking coins🔒 Authenticated

GET`/earn/staking/coins`

GET `/earn/staking/coins`

_Staking coins_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
cointype | query | string | Optional | Currency type: swap - voucher; lock - locked position; debt - US Treasury bond.  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Successfully retrieved | [Inline]  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
FindCoinStruct |   
  
**items**

Type | Constraints  
---|---  
object | required: ["pid","currencyRewards","exchangeRate","redeemPeriod","protocolName","maxStakeAmount","minStakeAmount","estimateApr","currency","isDefi","productType","exchangeRateReserve"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
pid | integer | Required |  | Product ID  
productType | integer | Required |  | Project type 0-voucher 1-locked position 2-US Treasury bond  
isDefi | integer | Required |  | Is DEFI protocol 0-no 1-yes  
currency | string | Required |  | Staked currencies (multiple entries separated by commas)  
estimateApr | string | Required |  | Estimated yield rate  
minStakeAmount | string | Required |  | Minimum staked amount  
maxStakeAmount | string | Required |  | Maximum staked amount  
protocolName | string | Required |  | Protocol name  
redeemPeriod | string | Required |  | Redemption period (days)  
exchangeRate | string | Required |  | Exchange rate  
exchangeRateReserve | string | Required |  | Reverse exchange rate  
extraInterest | array | Optional |  | Additional rewards  
currencyRewards | array | Required |  | Reward currency information  
  
**items / extraInterest**

Additional rewards

Type | Constraints  
---|---  
array |   
  
**items / extraInterest / items**

Type | Constraints  
---|---  
object | required: ["start_time","segment_interest","end_time","reward_coin"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
start_time | string | Required |  | Start timestamp  
end_time | string | Required |  | End Timestamp  
reward_coin | string | Required |  | Additional reward currency  
segment_interest | array | Required |  | Tiered reward information  
  
**items / extraInterest / items / segment_interest**

Tiered reward information

Type | Constraints  
---|---  
array |   
  
**items / extraInterest / items / segment_interest / items**

Type | Constraints  
---|---  
object | required: ["money_min","money_rate","money_max"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
money_min | string | Required |  | Tiered lower value  
money_max | string | Required |  | Tiered upper value  
money_rate | string | Required |  | Tiered interest rate  
  
**items / currencyRewards**

Reward currency information

Type | Constraints  
---|---  
array |   
  
**items / currencyRewards / items**

Type | Constraints  
---|---  
object | required: ["apr","reward_delay_days","reward_coin","interest_delay_days"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
apr | string | Required |  | Base interest rate  
reward_coin | string | Required |  | Reward currency  
reward_delay_days | string | Required |  | Dividend day -1 indicates dividends are distributed upon redemption  
interest_delay_days | string | Required |  | Interest accrual day  
  
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
    
    url = '/earn/staking/coins'
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
    url="/earn/staking/coins"
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
        "pid": 1,
        "productType": 0,
        "isDefi": 0,
        "currency": "GT",
        "estimateApr": "36.00",
        "minStakeAmount": "1",
        "maxStakeAmount": 700,
        "protocolName": "Gatechain",
        "redeemPeriod": 0,
        "exchangeRate": "1.00000000",
        "exchangeRateReserve": "1.00000000",
        "extraInterest": [
          {
            "start_time": 1749427201,
            "end_time": 1765497600,
            "reward_coin": "GT",
            "segment_interest": [
              {
                "money_min": "0",
                "money_max": "1000",
                "money_rate": "10.00"
              },
              {
                "money_min": "1000",
                "money_max": "2000",
                "money_rate": "15.00"
              },
              {
                "money_min": "2000",
                "money_max": "3000",
                "money_rate": "30.00"
              }
            ]
          }
        ],
        "currencyRewards": [
          {
            "apr": "6.00",
            "reward_coin": "GT2",
            "reward_delay_days": 1,
            "interest_delay_days": 1
          }
        ]
      }
    ]
    

##  On-chain token swap for earned coins🔒 Authenticated

POST`/earn/staking/swap`

POST `/earn/staking/swap`

_On-chain token swap for earned coins_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | SwapCoin | Required | none  
coin | body | string | Required | Currency  
side | body | integer | Required | 0 - Stake 1 - Redeem  
amount | body | string | Required | Size  
pid | body | integer | Optional | DeFi-type Mining Protocol Identifier  
  
####  Request Body Schema

Blockchain Mining

Request Body SchemaType | Constraints  
---|---  
SwapCoin | required: ["coin","side","amount"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
coin | string | Required |  | Currency  
side | integer | Required |  | 0 - Stake 1 - Redeem  
amount | string | Required |  | Size  
pid | integer | Optional |  | DeFi-type Mining Protocol Identifier  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Swap successful | SwapCoinStruct  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
SwapCoinStruct |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | integer | Optional |  | Order ID  
pid | integer | Optional |  | Product ID  
uid | integer | Optional |  | User ID  
coin | string | Optional |  | Currency  
type | integer | Optional |  | Type 0-Staking 1-Redemption  
subtype | string | Optional |  | SubType  
amount | string | Optional |  | Amount  
exchange_rate | string | Optional |  | Exchange ratio  
exchange_amount | string | Optional |  | Redemption Amount  
updateStamp | integer | Optional |  | Update timestamp  
createStamp | integer | Optional |  | Transaction timestamp  
status | integer | Optional |  | status 1-success  
protocol_type | integer | Optional |  | DEFI Protocol Type  
client_order_id | string | Optional |  | Reference ID  
source | string | Optional |  | Order Origin  
  
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
    
    url = '/earn/staking/swap'
    query_param = ''
    body='{"coin":"GT","side":"0","amount":"1.5"}'
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
    url="/earn/staking/swap"
    query_param=""
    body_param='{"coin":"GT","side":"0","amount":"1.5"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "coin": "GT",
      "side": "0",
      "amount": "1.5"
    }
    

> Example responses

> 200 Response
    
    
    {
      "id": 21000,
      "uid": 12345,
      "coin": "GT",
      "type": 0,
      "exchange_rate": "1.00000000",
      "amount": "2",
      "pid": 1,
      "status": 1,
      "createStamp": 1752200661
    }
    

##  List of on-chain coin-earning orders🔒 Authenticated

GET`/earn/staking/order_list`

GET `/earn/staking/order_list`

_List of on-chain coin-earning orders_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
pid | query | integer | Optional | Product ID  
coin | query | string | Optional | Currency name  
type | query | integer | Optional | Type 0-staking 1-redemption  
page | query | integer(int32) | Optional | Page number  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Successfully retrieved | OrderListStruct  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
OrderListStruct | required: ["page","pageSize","pageCount","totalCount","list"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
page | integer | Required |  | Page  
pageSize | integer | Required |  | Items per page  
pageCount | integer | Required |  | Total pages  
totalCount | integer | Required |  | Total entries  
list | array | Required |  |   
  
**list**

Type | Constraints  
---|---  
array |   
  
**list / items**

Type | Constraints  
---|---  
object | required: ["pid","coin","amount","type","status","redeem_stamp","createStamp","exchange_amount","fee"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
pid | integer | Required |  | Product ID  
coin | string | Required |  | Staked and redeemed currencies  
amount | string | Required |  | Amount  
type | integer | Required |  | Type 0-Staking 1-Redemption  
status | integer | Required |  | Status. 1 - success, 3 - delayed redemption in progress, 6 - redemption cancellation order  
redeem_stamp | integer | Required |  | Redemption credit time  
createStamp | integer | Required |  | Order time  
exchange_amount | string | Required |  | Exchange rate  
fee | string | Required |  | fee  
  
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
    
    url = '/earn/staking/order_list'
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
    url="/earn/staking/order_list"
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
      "page": 1,
      "pageSize": 20,
      "pageCount": 5,
      "totalCount": 90,
      "list": [
        {
          "pid": 2,
          "coin": "SOL",
          "amount": "1.00000000",
          "type": 0,
          "status": 1,
          "redeem_stamp": 0,
          "createStamp": 1756105456,
          "exchange_amount": "1.00000000",
          "fee": "0.0000000000"
        },
        {
          "pid": 2,
          "coin": "SOL",
          "amount": "1.00000000",
          "type": 0,
          "status": 1,
          "redeem_stamp": 0,
          "createStamp": 1755588122,
          "exchange_amount": "0.80000000",
          "fee": "0.0000000000"
        }
      ]
    }
    

##  On-chain coin-earning dividend records🔒 Authenticated

GET`/earn/staking/award_list`

GET `/earn/staking/award_list`

_On-chain coin-earning dividend records_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
pid | query | integer | Optional | Product ID  
coin | query | string | Optional | Currency name  
page | query | integer(int32) | Optional | Page number  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Successfully retrieved | AwardListStruct  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
AwardListStruct | required: ["page","pageSize","pageCount","totalCount","list"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
page | integer | Required |  | Page  
pageSize | integer | Required |  | Items per page  
pageCount | integer | Required |  | Total pages  
totalCount | integer | Required |  | Total entries  
list | array | Required |  |   
  
**list**

Type | Constraints  
---|---  
array |   
  
**list / items**

Type | Constraints  
---|---  
object | required: ["pid","mortgage_coin","amount","reward_coin","interest","fee","status","bonus_date","should_bonus_stamp"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
pid | integer | Required |  | Product ID  
mortgage_coin | string | Required |  | Collateral currency  
amount | string | Required |  | Amount  
reward_coin | string | Required |  | Reward currency  
interest | string | Required |  | Interest amount  
fee | string | Required |  | fee  
status | integer | Required |  | Status. 4 - success  
bonus_date | string | Required |  | Date  
should_bonus_stamp | integer | Required |  | Scheduled distribution timestamp  
  
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
    
    url = '/earn/staking/award_list'
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
    url="/earn/staking/award_list"
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
      "page": 1,
      "pageSize": 20,
      "pageCount": 2,
      "totalCount": 33,
      "list": [
        {
          "pid": 64,
          "mortgage_coin": "USDT",
          "amount": "0.0000019100",
          "reward_coin": "COMP",
          "interest": "0.0000019100",
          "fee": "0.0000000700",
          "status": 4,
          "bonus_date": "2025-08-08 00:00:00",
          "should_bonus_stamp": 1755907200
        },
        {
          "pid": 27,
          "mortgage_coin": "DOT",
          "amount": "0.0023424700",
          "reward_coin": "DOT",
          "interest": "0.0023424700",
          "fee": "0.0001232800",
          "status": 4,
          "bonus_date": "2025-08-11 00:00:00",
          "should_bonus_stamp": 1755043200
        }
      ]
    }
    

##  On-chain coin-earning assets🔒 Authenticated

GET`/earn/staking/assets`

GET `/earn/staking/assets`

_On-chain coin-earning assets_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
coin | query | string | Optional | Currency name  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Successfully retrieved | [Inline]  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
AssetListStruct |   
  
**items**

Type | Constraints  
---|---  
object | required: ["pid","mortgage_coin","mortgage_amount","createStamp","extra_income","freeze_amount","move_income","type","status","income_total","yesterday_income_multi","reward_coins","defi_income"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
pid | integer | Required |  | Product ID  
mortgage_coin | string | Required |  | Staked currencies (multiple entries separated by commas)  
mortgage_amount | string | Required |  | Position amount  
createStamp | integer | Required |  | First timestamp  
extra_income | string | Required |  | Additional rewards converted to USDT amount  
freeze_amount | string | Required |  | Locked amount, used in trading  
move_income | string | Required |  |   
type | integer | Required |  | Type 0-voucher 1-locked position 2-US Treasury bond  
status | integer | Required |  | Status. 1 - currency project listed, 2 - currency project delisted  
income_total | string | Required |  | Total earnings by currency  
yesterday_income_multi | array | Required |  | Yesterday's earnings  
reward_coins | array | Required |  | Currency-specific reward earnings  
defi_income | object | Required | required: ["total"] | DEIF earnings  
  
**items / yesterday_income_multi**

Yesterday's earnings

Type | Constraints  
---|---  
array |   
  
**items / yesterday_income_multi / items**

Type | Constraints  
---|---  
object |   
  
**items / reward_coins**

Currency-specific reward earnings

Type | Constraints  
---|---  
array |   
  
**items / reward_coins / items**

Type | Constraints  
---|---  
object | required: ["reward_coin","interest_delay_days","reward_delay_days"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
reward_coin | string | Required |  | Reward currency  
interest_delay_days | integer | Required |  | Interest accrual day  
reward_delay_days | integer | Required |  | Dividend day -1 indicates dividends are distributed upon redemption  
  
**items / defi_income**

DEIF earnings

Type | Constraints  
---|---  
object | required: ["total"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
total | array | Required |  |   
  
**items / defi_income / total**

Type | Constraints  
---|---  
array |   
  
**items / defi_income / total / items**

Type | Constraints  
---|---  
object | required: ["coin","amount"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
coin | string | Required |  |   
amount | string | Required |  |   
  
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
    
    url = '/earn/staking/assets'
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
    url="/earn/staking/assets"
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
        "pid": 1,
        "mortgage_coin": "GT",
        "mortgage_amount": "111.60000000",
        "createStamp": 1728530266,
        "extra_income": "0",
        "freeze_amount": "0.0000000000",
        "move_income": "0.0000000000",
        "type": 0,
        "status": 1,
        "income_total": "0",
        "yesterday_income_multi": [],
        "reward_coins": [
          {
            "reward_coin": "GT2",
            "interest_delay_days": 1,
            "reward_delay_days": 1
          }
        ]
      },
      {
        "pid": 64,
        "mortgage_coin": "USDT",
        "mortgage_amount": "1.0000000000",
        "createStamp": 1750764156,
        "extra_income": "0",
        "freeze_amount": "0.0000000000",
        "move_income": "0.0000000000",
        "type": 1,
        "status": 1,
        "income_total": "0",
        "yesterday_income_multi": [],
        "defi_income": {
          "total": [
            {
              "coin": "COMP",
              "amount": "0.0000076200"
            }
          ]
        },
        "reward_coins": [
          {
            "reward_coin": "USDT",
            "interest_delay_days": 1,
            "reward_delay_days": -1
          },
          {
            "reward_coin": "COMP",
            "interest_delay_days": 1,
            "reward_delay_days": 15
          }
        ]
      }
    ]
    

##  Create auto invest plan🔒 Authenticated

POST`/earn/autoinvest/plans/create`

POST `/earn/autoinvest/plans/create`

_Create auto invest plan_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | AutoInvestPlanCreate | Required | none  
plan_name | body | string | Optional | Plan name。Length: 0-50 characters  
plan_des | body | string | Optional | Plan description  
plan_money | body | string | Required | Pricing currency，SupportUSDT，BTC  
plan_amount | body | string | Required | Per PeriodAuto InvestAmount，Must > 0，and not exceedThePricing currencyConfigurationSingleMaximumAmount  
plan_period_type | body | string | Required | Enum: daily, weekly, biweekly, monthly, hourly, 4-hourly  
plan_period_day | body | integer(int64) | Required | Cycle day. For monthly: day of month (1-30); For weekly/biweekly: day of week (1-7, 1=Monday); For daily/hourly/4-hourly: ignored  
plan_period_hour | body | integer(int64) | Required | Execution hourAuto Invest 0-23  
items | body | array | Required | Investment portfolio, asset cannot be repeated; Sum of all items' ratios must be 100  
» asset | body | string | Required | Investment currency, e.g., BTC; Must be enabled and market exists; Cannot be repeated within the same plan  
» ratio | body | string | Required | The proportion of this currency in the portfolio，The sum of all items' ratios must be 100  
fund_source | body | string | Optional | Fund source: spot or earn, default: spot  
fund_flow | body | string | Optional | Fund flow direction: auto_invest or earn, default: auto_invest  
type | body | integer(int64) | Optional | 0 Normal creation, 1 QuickInvestment  
  
####  Request Body Schema

Create auto invest planRequest

Request Body SchemaType | Constraints  
---|---  
AutoInvestPlanCreate | required: ["plan_money","plan_amount","plan_period_type","plan_period_day","plan_period_hour","items"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
plan_name | string | Optional |  | Plan name。Length: 0-50 characters  
plan_des | string | Optional |  | Plan description  
plan_money | string | Required |  | Pricing currency，SupportUSDT，BTC  
plan_amount | string | Required |  | Per PeriodAuto InvestAmount，Must > 0，and not exceedThePricing currencyConfigurationSingleMaximumAmount  
plan_period_type | string | Required |  | Enum: daily, weekly, biweekly, monthly, hourly, 4-hourly  
plan_period_day | integer(int64) | Required |  | Cycle day. For monthly: day of month (1-30); For weekly/biweekly: day of week (1-7, 1=Monday); For daily/hourly/4-hourly: ignored  
plan_period_hour | integer(int64) | Required |  | Execution hourAuto Invest 0-23  
items | array | Required |  | Investment portfolio, asset cannot be repeated; Sum of all items' ratios must be 100  
fund_source | string | Optional |  | Fund source: spot or earn, default: spot  
fund_flow | string | Optional |  | Fund flow direction: auto_invest or earn, default: auto_invest  
type | integer(int64) | Optional |  | 0 Normal creation, 1 QuickInvestment  
  
**items**

Investment portfolio, asset cannot be repeated; Sum of all items' ratios must be 100

Request Body SchemaType | Constraints  
---|---  
array |   
  
**items / items**

Request Body SchemaType | Constraints  
---|---  
object | required: ["asset","ratio"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
asset | string | Required |  | Investment currency, e.g., BTC; Must be enabled and market exists; Cannot be repeated within the same plan  
ratio | string | Required |  | The proportion of this currency in the portfolio，The sum of all items' ratios must be 100  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Created successfully | AutoInvestPlanCreateResp  
  
### Response Schema

Status Code **200**

Create auto invest planResponse

Type | Constraints  
---|---  
AutoInvestPlanCreateResp | required: ["id"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | integer(int64) | Required |  | Plan ID  
amount | string | Optional |  | Per PeriodAuto InvestAmount  
money | string | Optional |  | Quote currency  
next_time | integer(int64) | Optional |  | Next execution time  
period_type | string | Optional |  | Cycle type  
period_day | integer(int64) | Optional |  | Cycle day  
period_hour | integer(int64) | Optional |  | CycleHours  
fund_flow | string | Optional |  | Fund Flow Direction  
fund_source | string | Optional |  | Fund source  
  
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
    
    url = '/earn/autoinvest/plans/create'
    query_param = ''
    body='{"plan_name":"","plan_des":"","plan_period_type":"monthly","plan_period_day":1,"plan_period_hour":1,"plan_money":"USDT","plan_amount":"100","type":0,"items":[{"asset":"BTC","ratio":"33"},{"asset":"GT","ratio":"33"},{"asset":"ETH","ratio":"34"}],"fund_source":"spot","fund_flow":"auto_invest"}'
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
    url="/earn/autoinvest/plans/create"
    query_param=""
    body_param='{"plan_name":"","plan_des":"","plan_period_type":"monthly","plan_period_day":1,"plan_period_hour":1,"plan_money":"USDT","plan_amount":"100","type":0,"items":[{"asset":"BTC","ratio":"33"},{"asset":"GT","ratio":"33"},{"asset":"ETH","ratio":"34"}],"fund_source":"spot","fund_flow":"auto_invest"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "plan_name": "",
      "plan_des": "",
      "plan_period_type": "monthly",
      "plan_period_day": 1,
      "plan_period_hour": 1,
      "plan_money": "USDT",
      "plan_amount": "100",
      "type": 0,
      "items": [
        {
          "asset": "BTC",
          "ratio": "33"
        },
        {
          "asset": "GT",
          "ratio": "33"
        },
        {
          "asset": "ETH",
          "ratio": "34"
        }
      ],
      "fund_source": "spot",
      "fund_flow": "auto_invest"
    }
    

> Example responses

> 200 Response
    
    
    {
      "id": 142579,
      "amount": "9",
      "money": "USDT",
      "next_time": 1773734410,
      "period_type": "hourly",
      "period_day": 30,
      "period_hour": 20,
      "fund_flow": "auto_invest",
      "fund_source": "spot"
    }
    

##  UpdateAuto invest plan🔒 Authenticated

POST`/earn/autoinvest/plans/update`

POST `/earn/autoinvest/plans/update`

_UpdateAuto invest plan_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | AutoInvestPlanUpdate | Required | none  
plan_id | body | integer(int64) | Required | Plan ID  
fund_source | body | string | Optional | Fund source Spotspot or Flexible Savingsearn，Default spot  
fund_flow | body | string | Optional | Fund Flow Direction Spotauto_invest or Flexible Savingsearn，Default auto_invest  
  
####  Request Body Schema

Request to update an auto-invest plan. The current model contains plan_id, fund_source, and fund_flow.

Request Body SchemaType | Constraints  
---|---  
AutoInvestPlanUpdate | required: ["plan_id"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
plan_id | integer(int64) | Required |  | Plan ID  
fund_source | string | Optional |  | Fund source Spotspot or Flexible Savingsearn，Default spot  
fund_flow | string | Optional |  | Fund Flow Direction Spotauto_invest or Flexible Savingsearn，Default auto_invest  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Updated successfully | None  
  
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
    
    url = '/earn/autoinvest/plans/update'
    query_param = ''
    body='{"plan_id":142582,"fund_source":"earn","fund_flow":"auto_invest"}'
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
    url="/earn/autoinvest/plans/update"
    query_param=""
    body_param='{"plan_id":142582,"fund_source":"earn","fund_flow":"auto_invest"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "plan_id": 142582,
      "fund_source": "earn",
      "fund_flow": "auto_invest"
    }
    

##  StopAuto invest plan🔒 Authenticated

POST`/earn/autoinvest/plans/stop`

POST `/earn/autoinvest/plans/stop`

_StopAuto invest plan_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | AutoInvestPlanStop | Required | none  
plan_id | body | integer(int64) | Required | Plan ID  
  
####  Request Body Schema

StopAuto invest planRequest

Request Body SchemaType | Constraints  
---|---  
AutoInvestPlanStop | required: ["plan_id"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
plan_id | integer(int64) | Required |  | Plan ID  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Stopped successfully | None  
  
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
    
    url = '/earn/autoinvest/plans/stop'
    query_param = ''
    body='{"plan_id":142582}'
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
    url="/earn/autoinvest/plans/stop"
    query_param=""
    body_param='{"plan_id":142582}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "plan_id": 142582
    }
    

##  Add position immediately🔒 Authenticated

POST`/earn/autoinvest/plans/add_position`

POST `/earn/autoinvest/plans/add_position`

_Add position immediately_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | AutoInvestPlanAddPosition | Required | none  
plan_id | body | integer(int64) | Required | Plan ID  
amount | body | string | Required | Amount  
  
####  Request Body Schema

Add position immediatelyRequest

Request Body SchemaType | Constraints  
---|---  
AutoInvestPlanAddPosition | required: ["plan_id","amount"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
plan_id | integer(int64) | Required |  | Plan ID  
amount | string | Required |  | Amount  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Add PositionSuccess | None  
  
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
    
    url = '/earn/autoinvest/plans/add_position'
    query_param = ''
    body='{"plan_id":142583,"amount":"12.345"}'
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
    url="/earn/autoinvest/plans/add_position"
    query_param=""
    body_param='{"plan_id":142583,"amount":"12.345"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "plan_id": 142583,
      "amount": "12.345"
    }
    

##  QueryCurrencies supporting auto invest🔒 Authenticated

GET`/earn/autoinvest/coins`

GET `/earn/autoinvest/coins`

_QueryCurrencies supporting auto invest_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
plan_money | query | string | Optional | Pricing currency，Optional: USDT or BTC，Default: USDT  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Successfully retrieved | [AutoInvestCoinsItem]  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
array |   
  
**items**

Currency item supporting auto invest

Type | Constraints  
---|---  
AutoInvestCoinsItem | required: ["key","value","asset_icon_url"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
key | string | Required |  | Currency code  
value | string | Required |  | Currency name  
asset_icon_url | string | Required |  | Currency icon URL  
sort | integer(int64) | Optional |  | Sort  
  
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
    
    url = '/earn/autoinvest/coins'
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
    url="/earn/autoinvest/coins"
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
        "key": "BTC",
        "value": "BTC",
        "asset_icon_url": "https://icon.staticimgs.com/images/coin_icon/64/btc.png?v=1743408000",
        "sort": 0
      },
      {
        "key": "ETH",
        "value": "ETH",
        "asset_icon_url": "https://icon.staticimgs.com/images/coin_icon/64/eth.png?v=1743408000",
        "sort": 0
      }
    ]
    

##  Get minimum investment amount🔒 Authenticated

POST`/earn/autoinvest/min_invest_amount`

POST `/earn/autoinvest/min_invest_amount`

_Get minimum investment amount_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | AutoInvestMinInvestAmount | Required | none  
money | body | string | Required | Currency, optional: USDT or BTC  
asset_type | body | integer(int32) | Required | Asset type: 1 for cryptocurrency, 2 for TradFi stocks; must be provided explicitly  
items | body | array | Required | none  
» asset | body | string | Required | Currency  
» ratio | body | string | Required | Ratio，e.g.100  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
asset_type | 1  
asset_type | 2  
  
####  Request Body Schema

QueryAvailableInvestmentMinimumAmountRequest

Request Body SchemaType | Constraints  
---|---  
AutoInvestMinInvestAmount | required: ["money","asset_type","items"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
money | string | Required |  | Currency, optional: USDT or BTC  
asset_type | integer(int32) | Required | enum: [1,2] | Asset type: 1 for cryptocurrency, 2 for TradFi stocks; must be provided explicitly  
items | array | Required |  |   
  
**items**

Request Body SchemaType | Constraints  
---|---  
array |   
  
**items / items**

Request Body SchemaType | Constraints  
---|---  
object | required: ["asset","ratio"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
asset | string | Required |  | Currency  
ratio | string | Required |  | Ratio，e.g.100  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Successfully retrieved | AutoInvestMinInvestAmountResp  
  
### Response Schema

Status Code **200**

AvailableInvestmentMinimumAmountResponse

Type | Constraints  
---|---  
AutoInvestMinInvestAmountResp | required: ["min_amount"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
min_amount | string | Required |  | MinimumAmount  
  
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
    
    url = '/earn/autoinvest/min_invest_amount'
    query_param = ''
    body='{"money":"USDT","asset_type":1,"items":[{"asset":"BTC","ratio":"33"},{"asset":"ETH","ratio":"33"},{"asset":"SOL","ratio":"34"}]}'
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
    url="/earn/autoinvest/min_invest_amount"
    query_param=""
    body_param='{"money":"USDT","asset_type":1,"items":[{"asset":"BTC","ratio":"33"},{"asset":"ETH","ratio":"33"},{"asset":"SOL","ratio":"34"}]}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "money": "USDT",
      "asset_type": 1,
      "items": [
        {
          "asset": "BTC",
          "ratio": "33"
        },
        {
          "asset": "ETH",
          "ratio": "33"
        },
        {
          "asset": "SOL",
          "ratio": "34"
        }
      ]
    }
    

> Example responses

> 200 Response
    
    
    {
      "min_amount": "7.06"
    }
    

##  List plan execution records🔒 Authenticated

GET`/earn/autoinvest/plans/records`

GET `/earn/autoinvest/plans/records`

_List plan execution records_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
plan_id | query | integer(int64) | Required | Plan ID  
page | query | integer(int64) | Optional | page number  
page_size | query | integer(int64) | Optional | Items per page，Maximum 100  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Successfully retrieved | AutoInvestPlanRecordsResp  
  
### Response Schema

Status Code **200**

PlanExecutionRecordPaginatedResponse

Type | Constraints  
---|---  
AutoInvestPlanRecordsResp | required: ["page","page_size","total_page","total","list"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
page | integer(int64) | Required |  | page number  
page_size | integer(int64) | Required |  | Items per page  
total_page | integer(int64) | Required |  | TotalPage number  
total | integer(int64) | Required |  | Total entries  
list | array | Required |  |   
  
**list**

Type | Constraints  
---|---  
array |   
  
**list / items**

Plan execution record item

Type | Constraints  
---|---  
object | required: ["id","type","money","user_id","plan_id","plan_version","amount","create_time","update_time","status","status_type","side","status_message"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | integer(int64) | Required |  | Record ID  
type | string | Required |  | Type  
money | string | Required |  | SourceCurrency  
user_id | integer(int64) | Required |  | User ID  
plan_id | integer(int64) | Required |  | Plan ID  
plan_version | integer(int64) | Required |  | PlanVersion  
amount | string | Required |  | Investment amount  
create_time | integer(int64) | Required |  | Investment time  
update_time | integer(int64) | Required |  | Update time  
status | string | Required |  | Status  
status_type | integer(int64) | Required |  | Status enum  
side | integer(int64) | Required |  | 2 = Buy, Other = Sell  
status_message | string | Required |  | Status description  
detail | string | Optional |  | Details  
asset | string | Optional |  | Currency  
  
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
    
    url = '/earn/autoinvest/plans/records'
    query_param = 'plan_id=141378'
    # for `gen_sign` implementation, refer to section `Authentication` above
    sign_headers = gen_sign('GET', prefix + url, query_param)
    headers.update(sign_headers)
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="GET"
    url="/earn/autoinvest/plans/records"
    query_param="plan_id=141378"
    body_param=''
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url?$query_param"
    curl -X $method $full_url \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Example responses

> 200 Response
    
    
    {
      "page": 1,
      "page_size": 10,
      "total_page": 30,
      "total": 299,
      "list": [
        {
          "id": 1770805384918111,
          "type": "Auto Invest",
          "money": "USDT",
          "asset": "",
          "user_id": 21245786,
          "plan_id": 141378,
          "plan_version": 2,
          "amount": "32.60292",
          "create_time": 1773734410,
          "update_time": 1773734410,
          "status": "Failed",
          "status_type": 2,
          "side": 2,
          "status_message": "put order fail",
          "detail": ""
        }
      ]
    }
    

##  List plan execution recordsDetails（OrderDetails）🔒 Authenticated

GET`/earn/autoinvest/orders`

GET `/earn/autoinvest/orders`

_List plan execution recordsDetails（OrderDetails）_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
plan_id | query | integer(int64) | Required | Plan ID  
record_id | query | integer(int64) | Required | Record ID  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Successfully retrieved | [AutoInvestOrderItem]  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
array |   
  
**items**

Auto invest order item

Type | Constraints  
---|---  
AutoInvestOrderItem | required: ["id","type","amount","plan_id","side","asset","record_id","total_money","market","price","create_time","total","fund_flow","error_code","error_msg","status"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | integer(int64) | Required |  | Order ID  
type | string | Required |  | Type  
amount | string | Required |  | Size  
plan_id | integer(int64) | Required |  | Plan ID  
side | integer(int64) | Required |  | direction  
asset | string | Required |  | Currency  
record_id | integer(int64) | Required |  | Record ID  
total_money | string | Required |  | TotalAmount  
market | string | Required |  | Currency pair  
price | string | Required |  | Price  
create_time | integer(int64) | Required |  | Creation time (Unix timestamp)  
total | string | Required |  | Total  
fund_flow | string | Required |  | Fund Flow Direction  
error_code | integer(int64) | Required |  | Error code  
error_msg | string | Required |  | Error message  
status | integer(int64) | Required |  | Status  
  
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
    
    url = '/earn/autoinvest/orders'
    query_param = 'plan_id=142583&record_id=1770805384904919'
    # for `gen_sign` implementation, refer to section `Authentication` above
    sign_headers = gen_sign('GET', prefix + url, query_param)
    headers.update(sign_headers)
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="GET"
    url="/earn/autoinvest/orders"
    query_param="plan_id=142583&record_id=1770805384904919"
    body_param=''
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url?$query_param"
    curl -X $method $full_url \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Example responses

> 200 Response
    
    
    [
      {
        "id": 6787627,
        "type": "Buy",
        "amount": "0.031",
        "plan_id": 142583,
        "side": 2,
        "asset": "USDT",
        "record_id": 1770805384904919,
        "total_money": "2.72583",
        "market": "SOL/USDT",
        "price": "87.93",
        "create_time": 1773656162,
        "total": "2.72583",
        "fund_flow": "auto_invest",
        "error_code": 0,
        "error_msg": "",
        "status": 1
      },
      {
        "id": 6787626,
        "type": "Buy",
        "amount": "0.001",
        "plan_id": 142583,
        "side": 2,
        "asset": "USDT",
        "record_id": 1770805384904919,
        "total_money": "2.65789",
        "market": "ETH/USDT",
        "price": "2657.89",
        "create_time": 1773656162,
        "total": "2.65789",
        "fund_flow": "auto_invest",
        "error_code": 0,
        "error_msg": "",
        "status": 1
      }
    ]
    

##  List investment currency configuration🔒 Authenticated

GET`/earn/autoinvest/config`

GET `/earn/autoinvest/config`

_List investment currency configuration_

### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Successfully retrieved | [AutoInvestConfigItem]  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
array |   
  
**items**

Investment currency configuration item

Type | Constraints  
---|---  
AutoInvestConfigItem | required: ["coin","max_limit"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
coin | string | Required |  | Currency  
max_limit | string | Required |  | InvestmentLimit  
  
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
    
    url = '/earn/autoinvest/config'
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
    url="/earn/autoinvest/config"
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
        "coin": "BTC",
        "max_limit": "10"
      },
      {
        "coin": "USDT",
        "max_limit": "100000"
      }
    ]
    

##  QueryAuto invest planDetails🔒 Authenticated

GET`/earn/autoinvest/plans/detail`

GET `/earn/autoinvest/plans/detail`

_QueryAuto invest planDetails_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
plan_id | query | integer(int64) | Required | Plan ID  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Successfully retrieved | AutoInvestPlanDetail  
  
### Response Schema

Status Code **200**

Auto invest planDetails

Type | Constraints  
---|---  
AutoInvestPlanDetail | required: ["id","name","create_time","update_time","user_id","money","amount","period_type","period_day","period_hour","portfolio","next_time","period","fund_source","fund_flow"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | integer(int64) | Required |  | Plan ID  
version | integer(int64) | Optional |  | PlanVersion  
name | string | Required |  | Plan name  
create_time | integer(int64) | Required |  | Creation time (Unix timestamp)  
update_time | integer(int64) | Required |  | Update time (Unix timestamp)  
user_id | integer(int64) | Required |  | User ID  
money | string | Required |  | Quote Currency  
amount | string | Required |  | Per PeriodInvestment amount  
period_type | string | Required |  | Cycle type（e.g., monthly）  
period_day | integer(int64) | Required |  | Cycle day  
period_hour | integer(int64) | Required |  | CycleHours  
portfolio | array | Required |  | Portfolio  
next_time | integer(int64) | Required |  | Next execution time (Unix timestamp)  
period | integer(int64) | Required |  | Executed periods  
fund_source | string | Required |  | Fund source（spot/earn）  
fund_flow | string | Required |  | Fund flow direction (auto_invest/earn)  
  
**portfolio**

Portfolio

Type | Constraints  
---|---  
array |   
  
**portfolio / items**

Auto invest plan portfolio item

Type | Constraints  
---|---  
object | required: ["asset","ratio","cum_invest","cum_hold","cum_redeem","avg_price","redeem_status","lend_amount"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
asset | string | Required |  | Currency  
ratio | string | Required |  | Ratio  
cum_invest | string | Required |  | Accumulated investment  
cum_hold | string | Required |  | AccumulatedPosition  
cum_redeem | string | Required |  | Accumulated redemption  
avg_price | string | Required |  | Average Cost Price  
redeem_status | integer(int64) | Required |  | Redemption status  
lend_amount | string | Required |  | LendingQuantity  
  
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
    
    url = '/earn/autoinvest/plans/detail'
    query_param = 'plan_id=142609'
    # for `gen_sign` implementation, refer to section `Authentication` above
    sign_headers = gen_sign('GET', prefix + url, query_param)
    headers.update(sign_headers)
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="GET"
    url="/earn/autoinvest/plans/detail"
    query_param="plan_id=142609"
    body_param=''
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url?$query_param"
    curl -X $method $full_url \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Example responses

> 200 Response
    
    
    {
      "id": 142609,
      "version": 0,
      "name": "Auto Invest BTC",
      "create_time": 1773733133,
      "update_time": 1773733133,
      "user_id": 2124569786,
      "money": "USDT",
      "amount": "100",
      "period_type": "monthly",
      "period_day": 1,
      "period_hour": 1,
      "portfolio": [
        {
          "asset": "BTC",
          "ratio": "33",
          "cum_invest": "0",
          "cum_hold": "0",
          "cum_redeem": "0",
          "avg_price": "0",
          "redeem_status": 0,
          "lend_amount": "0"
        },
        {
          "asset": "GT",
          "ratio": "33",
          "cum_invest": "0",
          "cum_hold": "0",
          "cum_redeem": "0",
          "avg_price": "0",
          "redeem_status": 0,
          "lend_amount": "0"
        },
        {
          "asset": "ETH",
          "ratio": "34",
          "cum_invest": "0",
          "cum_hold": "0",
          "cum_redeem": "0",
          "avg_price": "0",
          "redeem_status": 0,
          "lend_amount": "0"
        }
      ],
      "next_time": 1775005200,
      "period": 0,
      "fund_source": "spot",
      "fund_flow": "auto_invest"
    }
    

##  QueryAuto invest planList🔒 Authenticated

GET`/earn/autoinvest/plans/list_info`

GET `/earn/autoinvest/plans/list_info`

_QueryAuto invest planList_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
status | query | string | Required | Plan status，History history，Active active  
page | query | integer(int64) | Optional | page number  
page_size | query | integer(int64) | Optional | Items per page，Maximum 100  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Successfully retrieved | AutoInvestPlanListInfoResp  
  
### Response Schema

Status Code **200**

Auto invest planListPaginatedResponse

Type | Constraints  
---|---  
AutoInvestPlanListInfoResp | required: ["page","page_size","page_count","total_count","list"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
page | integer(int64) | Required |  | page number  
page_size | integer(int64) | Required |  | Items per page  
page_count | integer(int64) | Required |  | Total pages  
total_count | integer(int64) | Required |  | Total entries  
list | array | Required |  | PlanList  
  
**list**

PlanList

Type | Constraints  
---|---  
array |   
  
**list / items**

Auto invest planDetails

Type | Constraints  
---|---  
object | required: ["id","name","create_time","update_time","user_id","money","amount","period_type","period_day","period_hour","portfolio","next_time","period","fund_source","fund_flow"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | integer(int64) | Required |  | Plan ID  
version | integer(int64) | Optional |  | PlanVersion  
name | string | Required |  | Plan name  
create_time | integer(int64) | Required |  | Creation time (Unix timestamp)  
update_time | integer(int64) | Required |  | Update time (Unix timestamp)  
user_id | integer(int64) | Required |  | User ID  
money | string | Required |  | Quote Currency  
amount | string | Required |  | Per PeriodInvestment amount  
period_type | string | Required |  | Cycle type（e.g., monthly）  
period_day | integer(int64) | Required |  | Cycle day  
period_hour | integer(int64) | Required |  | CycleHours  
portfolio | array | Required |  | Portfolio  
next_time | integer(int64) | Required |  | Next execution time (Unix timestamp)  
period | integer(int64) | Required |  | Executed periods  
fund_source | string | Required |  | Fund source（spot/earn）  
fund_flow | string | Required |  | Fund flow direction (auto_invest/earn)  
  
**list / items / portfolio**

Portfolio

Type | Constraints  
---|---  
array |   
  
**list / items / portfolio / items**

Auto invest plan portfolio item

Type | Constraints  
---|---  
object | required: ["asset","ratio","cum_invest","cum_hold","cum_redeem","avg_price","redeem_status","lend_amount"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
asset | string | Required |  | Currency  
ratio | string | Required |  | Ratio  
cum_invest | string | Required |  | Accumulated investment  
cum_hold | string | Required |  | AccumulatedPosition  
cum_redeem | string | Required |  | Accumulated redemption  
avg_price | string | Required |  | Average Cost Price  
redeem_status | integer(int64) | Required |  | Redemption status  
lend_amount | string | Required |  | LendingQuantity  
  
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
    
    url = '/earn/autoinvest/plans/list_info'
    query_param = 'status=active'
    # for `gen_sign` implementation, refer to section `Authentication` above
    sign_headers = gen_sign('GET', prefix + url, query_param)
    headers.update(sign_headers)
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="GET"
    url="/earn/autoinvest/plans/list_info"
    query_param="status=active"
    body_param=''
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url?$query_param"
    curl -X $method $full_url \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Example responses

> 200 Response
    
    
    {
      "page": 1,
      "page_size": 10,
      "page_count": 3,
      "total_count": 23,
      "list": [
        {
          "id": 142609,
          "version": 1,
          "name": "Auto Invest BTC",
          "create_time": 1773733133,
          "update_time": 1773733133,
          "user_id": 2124569786,
          "money": "USDT",
          "amount": "100",
          "period_type": "monthly",
          "period_day": 1,
          "period_hour": 1,
          "portfolio": [
            {
              "asset": "BTC",
              "ratio": "33",
              "cum_invest": "0",
              "cum_hold": "0",
              "cum_redeem": "0",
              "avg_price": "0",
              "redeem_status": 0,
              "lend_amount": "0"
            },
            {
              "asset": "GT",
              "ratio": "33",
              "cum_invest": "0",
              "cum_hold": "0",
              "cum_redeem": "0",
              "avg_price": "0",
              "redeem_status": 0,
              "lend_amount": "0"
            },
            {
              "asset": "ETH",
              "ratio": "34",
              "cum_invest": "0",
              "cum_hold": "0",
              "cum_redeem": "0",
              "avg_price": "0",
              "redeem_status": 0,
              "lend_amount": "0"
            }
          ],
          "next_time": 1775005200,
          "period": 0,
          "fund_source": "spot",
          "fund_flow": "auto_invest"
        }
      ]
    }
    

##  Get product list

GET`/earn/fixed-term/product`

GET `/earn/fixed-term/product`

_Get product list_

Query fixed-term earn product list. Supports filtering by currency, product type, status, etc. Returns product interest rate, lock-up period, quota, and reward campaign information

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
asset | query | string | Optional | Currency  
type | query | integer | Optional | Product type: 1 for regular, 2 for VIP  
status | query | integer | Optional | Product status filter. Pass 2 for products available for subscription.  
show_status | query | string | Optional | Visibility status filter. Pass "2" for visible products.  
page | query | integer | Required | Page number  
limit | query | integer | Required | Page size  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Product list retrieved successfully | ListEarnFixedTermProductsResponse  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
ListEarnFixedTermProductsResponse | required: ["code","message","data","timestamp"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
code | integer | Required |  | Return code, 0 means success  
message | string | Required |  | Response message  
data | object | Required | required: ["list","total"] | Product list data  
timestamp | integer | Required |  | Response timestamp (in seconds)  
  
**data**

Product list data

Type | Constraints  
---|---  
object | required: ["list","total"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
list | array | Required |  | Product list  
total | integer | Required |  | Total Records  
  
**data / list**

Product list

Type | Constraints  
---|---  
array |   
  
**data / list / items**

Fixed-term earn product

Type | Constraints  
---|---  
FixedTermProduct |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | integer | Optional |  | Product ID  
name | string | Optional |  | Product name  
asset | string | Optional |  | Currency  
lock_up_period | integer | Optional |  | Lock-up period (in days)  
min_lend_amount | string | Optional |  | Minimum earn amount  
user_max_lend_amount | string | Optional |  | User maximum earn limit  
total_lend_amount | string | Optional |  | Platform earn limit  
year_rate | string | Optional |  | Annual interest rate  
type | integer | Optional |  | Product type: 1 for regular, 2 for VIP  
pre_redeem | integer | Optional |  | Whether early redemption is supported: 0 for not supported, 1 for supported  
reinvest | integer | Optional |  | Whether auto-renewal is supported: 0 for not supported, 1 for supported  
redeem_account | integer | Optional |  | Whether fixed-to-flexible conversion is supported: 0 for not supported, 1 for supported  
min_vip | integer | Optional |  | Minimum VIP level requirement, 0-16, 0 means no restriction  
max_vip | integer | Optional |  | Maximum VIP level requirement (0-16), 0 means no restriction  
status | integer | Optional |  | Product status: 1 for unlisted, 2 for listed, 3 for delisted  
create_time | string | Optional |  | Created time  
user_max_lend_volume | string | Optional |  | User maximum earn amount  
user_total_amount | string | Optional |  | Total amount the user has invested in earn products  
sale_status | integer | Optional |  | Sale status: 1 for on sale, 2 for sold out  
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/earn/fixed-term/product'
    query_param = 'page=1&limit=100'
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/earn/fixed-term/product?page=1&limit=100 \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    {
      "code": 0,
      "message": "",
      "data": {
        "list": [
          {
            "id": 11,
            "name": "USDT-TEST",
            "asset": "USDT",
            "lock_up_period": 16,
            "min_lend_amount": "1",
            "user_max_lend_amount": "100000",
            "total_lend_amount": "100000000",
            "year_rate": "0.03",
            "status": 2,
            "create_time": "2024-12-13T03:29:41.103Z",
            "user_total_amount": "0"
          },
          {
            "id": 10,
            "name": "示例",
            "asset": "USDT",
            "lock_up_period": 15,
            "min_lend_amount": "1",
            "user_max_lend_amount": "100000",
            "total_lend_amount": "100000000",
            "year_rate": "0.03",
            "status": 2,
            "create_time": "2024-12-13T03:29:41.103Z",
            "user_total_amount": "0"
          }
        ],
        "total": 12
      },
      "timestamp": 1734338466
    }
    

##  Get product list by single currency

GET`/earn/fixed-term/product/{asset}/list`

GET `/earn/fixed-term/product/{asset}/list`

_Get product list by single currency_

Sort by product term in ascending order

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
asset | path | string | Required | Currency name, e.g., USDT, BTC  
type | query | string | Optional | Product type: "" or 1 for regular product list, 2 for VIP product list, 0 for all products  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Single currency product list retrieved successfully | ListEarnFixedTermProductsByAssetResponse  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
ListEarnFixedTermProductsByAssetResponse | required: ["code","message","data","timestamp"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
code | integer | Required |  | Return code, 0 means success  
message | string | Required |  | Response message  
data | object | Required | required: ["list"] | Product list data  
timestamp | integer | Required |  | Response timestamp (in seconds)  
  
**data**

Product list data

Type | Constraints  
---|---  
object | required: ["list"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
list | array | Required |  | Product list  
  
**data / list**

Product list

Type | Constraints  
---|---  
array |   
  
**data / list / items**

Fixed-term earn product (compact)

Type | Constraints  
---|---  
FixedTermProductSimple |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | integer | Optional |  | Product ID  
asset | string | Optional |  | Currency  
lock_up_period | integer | Optional |  | Lock-up period (in days)  
year_rate | string | Optional |  | Annual interest rate  
type | integer | Optional |  | Product type: 1 for regular, 2 for VIP  
pre_redeem | integer | Optional |  | Whether early redemption is supported: 0 for not supported, 1 for supported  
reinvest | integer | Optional |  | Whether auto-renewal is supported: 0 for not supported, 1 for supported  
simple_earn | integer | Optional |  | Whether fixed-to-flexible conversion is supported: 0 for not supported, 1 for supported  
min_vip | integer | Optional |  | Minimum VIP level requirement, 0 means no restriction  
max_vip | integer | Optional |  | Maximum VIP level requirement, 0 means no restriction  
sale_status | integer | Optional |  | Sale status: 1 for on sale, 2 for sold out  
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/earn/fixed-term/product/USDT/list'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/earn/fixed-term/product/USDT/list \
      -H 'Accept: application/json'
    
    

> Example responses

> Single currency product list retrieved successfully
    
    
    {
      "code": 0,
      "message": "",
      "data": {
        "list": [
          {
            "id": 68,
            "asset": "USDT",
            "lock_up_period": 1,
            "year_rate": "0.0289",
            "sale_status": 1
          },
          {
            "id": 61,
            "asset": "USDT",
            "lock_up_period": 30,
            "year_rate": "0.0395",
            "sale_status": 2
          }
        ]
      },
      "timestamp": 1737944222
    }
    
    
    
    {
      "code": 0,
      "message": "",
      "data": {
        "list": [
          {
            "id": 29,
            "asset": "ATOM",
            "lock_up_period": 7,
            "year_rate": "0.04",
            "sale_status": 1
          }
        ]
      },
      "timestamp": 1737944009
    }
    

##  Subscription list🔒 Authenticated

GET`/earn/fixed-term/user/lend`

GET `/earn/fixed-term/user/lend`

_Subscription list_

Query the user's fixed-term earn subscription order list. Supports filtering by product, currency, order type, etc. Returns order details, earnings, rewards, and interest rate boost coupon information

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
product_id | query | integer | Optional | Product ID  
order_id | query | integer(int64) | Optional | Order ID  
asset | query | string | Optional | Currency  
order_type | query | string | Required | Order type: 1 for current orders, 2 for historical orders  
page | query | integer | Required | Page number  
limit | query | integer | Required | Page size  
sub_business | query | integer | Optional | Sub-business  
business_filter | query | string | Optional | Business filter conditions, JSON array format, e.g., [{"business":1, "sub_business": 0}]. business: 1 for regular, 2 for VIP  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Subscription order list retrieved successfully | ListEarnFixedTermLendsResponse  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
ListEarnFixedTermLendsResponse | required: ["code","message","data","timestamp"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
code | integer | Required |  | Return code, 0 means success  
message | string | Required |  | Response message  
data | object | Required | required: ["list","total"] | Subscription order list data  
timestamp | integer | Required |  | Response timestamp (in seconds)  
  
**data**

Subscription order list data

Type | Constraints  
---|---  
object | required: ["list","total"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
list | array | Required |  | Subscription order list  
total | integer | Required |  | Total Records  
  
**data / list**

Subscription order list

Type | Constraints  
---|---  
array |   
  
**data / list / items**

Fixed-term earn subscription order

Type | Constraints  
---|---  
FixedTermLendOrder |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | integer | Optional |  | Subscription record ID  
business | integer | Optional |  | Business type: 1 for regular, 2 for VIP  
order_id | integer(int64) | Optional |  | Order ID  
user_id | integer(int64) | Optional |  | User ID  
asset | string | Optional |  | Currency  
product_id | integer | Optional |  | Product ID  
lock_up_period | integer | Optional |  | Lock-up period (in days)  
principal | string | Optional |  | Subscription principal  
year_rate | string | Optional |  | Annual interest rate  
product_type | integer | Optional |  | Product type: 1 for regular, 2 for VIP  
interest | string | Optional |  | Accrued interest  
status | integer | Optional |  | Order status: 1 for holding, 2 for redeemed, 3 for matured, 4 for settled  
reinvest_status | integer | Optional |  | Auto-renewal status: 0 for disabled, 1 for enabled  
redeem_account_type | integer | Optional |  | Redemption payout account type: 1 for spot account  
origin_order | string | Optional |  | Original order ID, linked to previous order IDs in auto-renewal scenarios  
redeem_type | integer | Optional |  | Redemption type: 1 for early redemption, 2 for maturity redemption  
redeem_time | string | Optional |  | Redemption time  
finish_time | string | Optional |  | Expiration time  
create_time | string | Optional |  | Created time  
year_rate_perent | string | Optional |  | Annual interest rate percentage display value  
total_year_rate_percent | string | Optional |  | Comprehensive annualized yield percentage (including interest rate boost, rewards, etc.)  
total_interest | string | Optional |  | Total earnings (including interest and bonus rewards)  
product_info | FixedTermProductInfo | Optional | required: ["pre_redeem","reinvest","redeem_account","min_vip","max_vip"] | Product configuration  
bonus_info | FixedTermBonusInfo | Optional |  | Bonus reward campaign information  
coupon_info | FixedTermCouponInfo | Optional | required: ["id","business","user_id","asset","order_id","financial_rate_id","buy_limit_low","buy_limit_high","rate_day","rate_ratio","coupon_days","coupon_principal","coupon_year_rate","coupon_interest","status","finish_time","create_time"] | Interest rate boost coupon information  
redeem_at | integer | Optional |  | Redemption timestamp (in seconds)  
finish_at | integer | Optional |  | Expiration timestamp (in seconds)  
create_at | integer | Optional |  | Creation timestamp (in seconds)  
icon | string | Optional |  | Currency icon URL  
  
**data / list / items / product_info**

Product configuration

Type | Constraints  
---|---  
FixedTermProductInfo | required: ["pre_redeem","reinvest","redeem_account","min_vip","max_vip"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
pre_redeem | integer | Required |  | Whether early redemption is supported: 0 for not supported, 1 for supported  
reinvest | integer | Required |  | Whether auto-renewal is supported: 0 for not supported, 1 for supported  
redeem_account | integer | Required |  | Redemption payout account type  
min_vip | integer | Required |  | Minimum VIP level requirement, 0 means no restriction  
max_vip | integer | Required |  | Maximum VIP level requirement, 0 means no restriction  
  
**data / list / items / bonus_info**

Bonus reward campaign information

Type | Constraints  
---|---  
FixedTermBonusInfo |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | integer | Optional |  | Activity ID  
product_id | integer | Optional |  | Associated product ID  
asset | string | Optional |  | Product currency  
bonus_asset | string | Optional |  | Reward currency  
kyc_limit | string | Optional |  | KYC level restrictions, comma-separated  
ladder_apr | array | Optional |  | Tiered annual interest rate  
total_bonus_amount | string | Optional |  | Total reward amount  
user_total_bonus_amount | string | Optional |  | Maximum reward per user  
status | integer | Optional |  | Activity status: 1 for unlisted, 2 for listed, 3 for delisted  
start_time | string | Optional |  | Activity start time  
end_time | string | Optional |  | Activity end time  
create_time | string | Optional |  | Created time  
start_at | integer | Optional |  | Activity start timestamp (in seconds)  
end_at | integer | Optional |  | Activity end timestamp (in seconds)  
total_issued_amount | string | Optional |  | Total rewards distributed  
user_total_issued_amount | string | Optional |  | Total rewards distributed to the user  
bonus_asset_price | string | Optional |  | Reward currency price (denominated in USDT)  
product_asset_price | string | Optional |  | Product currency price (denominated in USDT)  
product_year_rate | string | Optional |  | Product base annual interest rate  
  
**data / list / items / bonus_info / ladder_apr**

Tiered annual interest rate

Type | Constraints  
---|---  
array |   
  
**data / list / items / bonus_info / ladder_apr / items**

Type | Constraints  
---|---  
LadderApr | required: ["apr","left","right"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
apr | string | Required |  | Annualized interest rate  
left | string | Required |  | Range lower limit  
right | string | Required |  | Range upper limit  
  
**data / list / items / coupon_info**

Interest rate boost coupon information

Type | Constraints  
---|---  
FixedTermCouponInfo | required: ["id","business","user_id","asset","order_id","financial_rate_id","buy_limit_low","buy_limit_high","rate_day","rate_ratio","coupon_days","coupon_principal","coupon_year_rate","coupon_interest","status","finish_time","create_time"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | integer | Required |  | Interest rate boost coupon record ID  
business | integer | Required |  | Business Type  
user_id | integer(int64) | Required |  | User ID  
asset | string | Required |  | Currency  
order_id | integer(int64) | Required |  | Associated order ID  
financial_rate_id | integer | Required |  | Interest rate boost coupon ID  
buy_limit_low | string | Required |  | Minimum subscription amount for interest rate boost coupon  
buy_limit_high | string | Required |  | Maximum subscription amount for interest rate boost coupon  
rate_day | integer | Required |  | Interest rate boost days  
rate_ratio | string | Required |  | Interest rate boost percentage  
coupon_days | integer | Required |  | Actual interest rate boost days  
coupon_principal | string | Required |  | Principal for interest rate boost calculation  
coupon_year_rate | string | Required |  | Interest rate boost APR  
coupon_interest | string | Required |  | Interest generated from rate boost  
status | integer | Required |  | Status: 1 for active, 2 for settled  
finish_time | string | Required |  | Settlement time  
create_time | string | Required |  | Created time  
  
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
    
    url = '/earn/fixed-term/user/lend'
    query_param = 'order_type=1&page=1&limit=10'
    # for `gen_sign` implementation, refer to section `Authentication` above
    sign_headers = gen_sign('GET', prefix + url, query_param)
    headers.update(sign_headers)
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="GET"
    url="/earn/fixed-term/user/lend"
    query_param="order_type=1&page=1&limit=10"
    body_param=''
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url?$query_param"
    curl -X $method $full_url \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Example responses

> Subscription order list retrieved successfully
    
    
    {
      "code": 0,
      "message": "",
      "data": {
        "list": [
          {
            "id": 83402,
            "business": 1,
            "order_id": 5846120275,
            "user_id": 2024103749,
            "asset": "USDT",
            "product_id": 239,
            "lock_up_period": 23,
            "principal": "44.12",
            "year_rate": "0.3",
            "product_type": 2,
            "interest": "0.83404931",
            "status": 1,
            "reinvest_status": 1,
            "redeem_account_type": 1,
            "origin_order": "",
            "redeem_type": 2,
            "redeem_time": "2025-08-08T00:00:00Z",
            "finish_time": "2025-08-08T00:00:00Z",
            "create_time": "2025-07-15T03:55:07.304Z",
            "year_rate_perent": "30",
            "total_year_rate_percent": "63.13",
            "total_interest": "0.83996629",
            "product_info": {
              "pre_redeem": 1,
              "reinvest": 1,
              "redeem_account": 1,
              "min_vip": 1,
              "max_vip": 16
            },
            "bonus_info": {
              "id": 142,
              "product_id": 239,
              "asset": "USDT",
              "bonus_asset": "GT",
              "kyc_limit": "1,2,3,4",
              "ladder_apr": [
                {
                  "apr": "0.1",
                  "left": "0",
                  "right": "1"
                },
                {
                  "apr": "0.2",
                  "left": "1",
                  "right": "2"
                }
              ],
              "total_bonus_amount": "100000",
              "user_total_bonus_amount": "100000",
              "status": 2,
              "start_time": "2025-06-20T06:57:46Z",
              "end_time": "2026-06-29T16:00:00Z",
              "create_time": "2025-06-20T06:57:54.796Z",
              "start_at": 1750402666,
              "end_at": 1782748800,
              "total_issued_amount": "19.49",
              "user_total_issued_amount": "0",
              "bonus_asset_price": "17.66",
              "product_asset_price": "1",
              "product_year_rate": "0.3"
            },
            "coupon_info": {
              "id": 63,
              "business": 1,
              "user_id": 2024103749,
              "asset": "USDT",
              "order_id": 5846120275,
              "financial_rate_id": 1506,
              "buy_limit_low": "1",
              "buy_limit_high": "3",
              "rate_day": 30,
              "rate_ratio": "3.13",
              "coupon_days": 23,
              "coupon_principal": "3",
              "coupon_year_rate": "0.0313",
              "coupon_interest": "0.00591698",
              "status": 2,
              "finish_time": "2025-08-08T00:00:00Z",
              "create_time": "2025-07-15T03:55:07.285Z"
            },
            "redeem_at": 1754611200,
            "finish_at": 1754611200,
            "create_at": 1752551707,
            "icon": "https://icon.gateimg.com/images/coin_icon/64/usdt.png"
          }
        ],
        "total": 51
      },
      "timestamp": 1752564887
    }
    
    
    
    {
      "code": 0,
      "message": "",
      "data": {
        "list": [
          {
            "id": 83392,
            "business": 1,
            "order_id": 5846112514,
            "user_id": 2024103749,
            "asset": "USDT",
            "product_id": 230,
            "lock_up_period": 1,
            "principal": "1",
            "year_rate": "0.0312",
            "product_type": 1,
            "interest": "0.00008547",
            "status": 1,
            "reinvest_status": 1,
            "redeem_account_type": 1,
            "origin_order": "",
            "redeem_type": 2,
            "redeem_time": "2025-07-16T00:00:00Z",
            "finish_time": "2025-07-16T00:00:00Z",
            "create_time": "2025-07-15T00:30:10.515Z",
            "year_rate_perent": "3.12",
            "total_year_rate_percent": "3.12",
            "total_interest": "0.00008547",
            "product_info": {
              "pre_redeem": 0,
              "reinvest": 1,
              "redeem_account": 1,
              "min_vip": 0,
              "max_vip": 0
            },
            "bonus_info": null,
            "coupon_info": null,
            "redeem_at": 1752624000,
            "finish_at": 1752624000,
            "create_at": 1752539410,
            "icon": "https://icon.gateimg.com/images/coin_icon/64/usdt.png"
          }
        ],
        "total": 10
      },
      "timestamp": 1752564887
    }
    

##  Subscription🔒 Authenticated

POST`/earn/fixed-term/user/lend`

POST `/earn/fixed-term/user/lend`

_Subscription_

Subscribe to a fixed-term earn product by specifying the product ID and subscription amount. Optionally enable auto-renewal and apply an interest rate boost coupon

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | FixedTermLendRequest | Optional | none  
product_id | body | integer | Required | Product ID  
amount | body | string | Required | Subscription amount  
year_rate | body | string | Optional | Annual interest rate  
reinvest_status | body | integer | Optional | Auto-renewal status: 0 for disabled, 1 for enabled  
redeem_account_type | body | integer | Optional | Redemption payout account type: 1 for spot account  
financial_rate_id | body | integer | Optional | Interest rate boost coupon ID, 0 means not used  
sub_business | body | integer | Optional | Sub-business type  
  
####  Request Body Schema

Subscription request

Request Body SchemaType | Constraints  
---|---  
FixedTermLendRequest | required: ["product_id","amount"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
product_id | integer | Required |  | Product ID  
amount | string | Required |  | Subscription amount  
year_rate | string | Optional |  | Annual interest rate  
reinvest_status | integer | Optional |  | Auto-renewal status: 0 for disabled, 1 for enabled  
redeem_account_type | integer | Optional |  | Redemption payout account type: 1 for spot account  
financial_rate_id | integer | Optional |  | Interest rate boost coupon ID, 0 means not used  
sub_business | integer | Optional |  | Sub-business type  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Subscription successful | CreateEarnFixedTermLendResponse  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
CreateEarnFixedTermLendResponse |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
code | integer | Optional |  | Return code, 0 means success  
message | string | Optional |  | Response message  
data | object | Optional |  | Subscription result  
timestamp | integer | Optional |  | Response timestamp (in seconds)  
  
**data**

Subscription result

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
order_id | integer(int64) | Optional |  | Subscription order ID  
  
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
    
    url = '/earn/fixed-term/user/lend'
    query_param = ''
    body='{"product_id":476,"amount":"1","year_rate":"0.0100000000","reinvest_status":1,"redeem_account_type":1,"financial_rate_id":0,"sub_business":13}'
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
    url="/earn/fixed-term/user/lend"
    query_param=""
    body_param='{"product_id":476,"amount":"1","year_rate":"0.0100000000","reinvest_status":1,"redeem_account_type":1,"financial_rate_id":0,"sub_business":13}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "product_id": 476,
      "amount": "1",
      "year_rate": "0.0100000000",
      "reinvest_status": 1,
      "redeem_account_type": 1,
      "financial_rate_id": 0,
      "sub_business": 13
    }
    

> Example responses

> 200 Response
    
    
    {
      "code": 0,
      "message": "string",
      "data": {
        "order_id": 0
      },
      "timestamp": 0
    }
    

##  Redeem🔒 Authenticated

POST`/earn/fixed-term/user/pre-redeem`

POST `/earn/fixed-term/user/pre-redeem`

_Redeem_

Early redemption of a fixed-term earn order, order ID is required

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | EarnFixedTermPreRedeemRequest | Optional | none  
order_id | body | string | Required | Order ID  
  
####  Request Body Schema

Request Body SchemaType | Constraints  
---|---  
EarnFixedTermPreRedeemRequest | required: ["order_id"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
order_id | string | Required |  | Order ID  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Redemption successful | CreateEarnFixedTermPreRedeemResponse  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
CreateEarnFixedTermPreRedeemResponse |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
code | integer | Optional |  | Return code, 0 means success  
message | string | Optional |  | Response message  
data | object | Optional |  | Redemption result (empty object on success)  
timestamp | integer | Optional |  | Response timestamp (in seconds)  
  
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
    
    url = '/earn/fixed-term/user/pre-redeem'
    query_param = ''
    body='{"order_id":"5862476630"}'
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
    url="/earn/fixed-term/user/pre-redeem"
    query_param=""
    body_param='{"order_id":"5862476630"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "order_id": "5862476630"
    }
    

> Example responses

> 200 Response
    
    
    {
      "code": 0,
      "message": "string",
      "data": {},
      "timestamp": 0
    }
    

##  Subscription history🔒 Authenticated

GET`/earn/fixed-term/user/history`

GET `/earn/fixed-term/user/history`

_Subscription history_

Query the user's fixed-term earn history records. Supports filtering by type (subscription, redemption, interest, bonus rewards) and time range

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
product_id | query | integer | Optional | Product ID  
order_id | query | string | Optional | Order ID  
asset | query | string | Optional | Currency  
type | query | string | Required | 1 for subscription, 2 for redemption, 3 for interest, 4 for bonus reward  
page | query | integer | Required | Page number  
limit | query | integer | Required | Page size  
start_at | query | integer | Optional | Start timestamp  
end_at | query | integer | Optional | End Timestamp  
sub_business | query | integer | Optional | Sub-business  
business_filter | query | string | Optional | Business filter conditions, JSON array format, e.g., [{"business":1, "sub_business": 0}]. business: 1 for regular, 2 for VIP  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | History records retrieved successfully | ListEarnFixedTermHistoryResponse  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
ListEarnFixedTermHistoryResponse |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
code | integer | Optional |  | Return code, 0 means success  
message | string | Optional |  | Response message  
data | object | Optional |  |   
timestamp | integer | Optional |  | Response timestamp (in seconds)  
  
**data**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
list | array | Optional |  |   
total | integer | Optional |  | Total Records  
  
**data / list**

Type | Constraints  
---|---  
array |   
  
**data / list / items**

Fixed-term earn history records

Type | Constraints  
---|---  
FixedTermHistoryRecord | required: ["id","user_id","asset","product_id","status","create_time","create_at"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | integer | Required |  | Record ID  
order_id | integer(int64) | Optional |  | Order ID  
user_id | integer(int64) | Required |  | User ID  
asset | string | Required |  | Currency  
uniq_time | string | Optional |  | Unique time identifier (date)  
bonus_id | integer | Optional |  | Reward campaign ID  
product_id | integer | Required |  | Product ID  
bonus_asset | string | Optional |  | Reward currency  
total_principal | string | Optional |  | Total principal  
amount | string | Optional |  | Amount  
asset_price | string | Optional |  | Currency price  
status | integer | Required |  | Status  
detail | string | Optional |  | Detail description  
create_time | string | Required |  | Created time  
create_at | integer | Required |  | Creation timestamp (in seconds)  
lock_up_period | integer | Optional |  | Term  
  
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
    
    url = '/earn/fixed-term/user/history'
    query_param = 'type=1&page=1&limit=10'
    # for `gen_sign` implementation, refer to section `Authentication` above
    sign_headers = gen_sign('GET', prefix + url, query_param)
    headers.update(sign_headers)
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="GET"
    url="/earn/fixed-term/user/history"
    query_param="type=1&page=1&limit=10"
    body_param=''
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url?$query_param"
    curl -X $method $full_url \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Example responses

> 200 Response
    
    
    {
      "code": 0,
      "message": "string",
      "data": {
        "list": [
          {}
        ],
        "total": 0
      },
      "timestamp": 0
    }
    

#  Schemas

##  PlaceDualStockInvestmentOrderParams

Stock dual investment order request

Type | Constraints  
---|---  
object | required: ["plan_id","amount"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
plan_id | string | Required |  | Product ID  
amount | string | Required |  | Subscription amount  
text | string | Optional |  | Order custom information. Users can set custom ID with this field. Custom fields must meet the following conditions:  
  
1\. Must start with `t-`  
2\. Excluding `t-`, length cannot exceed 28 bytes  
3\. Can only contain numbers, letters, underscore(_), hyphen(-) or dot(.)  
hit_spot | integer | Optional | enum: [0,1] | Whether to use the spot account to fund a buy-low (put) subscription. `1` selects the account; omitted or other values leave it unselected.  
hit_stock | integer | Optional | enum: [0,1] | Whether to use the stock account to fund a buy-low (put) subscription. `1` selects the account; omitted or other values leave it unselected.  
hit_simple | integer | Optional | enum: [0,1] | Whether to use the Simple Earn account to fund a buy-low (put) subscription. `1` selects the account; omitted or other values leave it unselected.  
      
    
    {
      "plan_id": "string",
      "amount": "string",
      "text": "string",
      "hit_spot": 1,
      "hit_stock": 0,
      "hit_simple": 0
    }
    
    

##  DualGetOrders

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | integer(int32) | Optional |  | Order ID  
plan_id | integer(int32) | Optional |  | Product ID  
invest_amount | string | Optional |  | Investment Quantity  
settlement_amount | string | Optional |  | Settlement Quantity  
create_time | integer(int32) | Optional |  | Created time  
complete_time | integer(int32) | Optional |  | Completed Time  
status | string | Optional |  | Status:  
  
`INIT`-Created  
`SETTLEMENT_SUCCESS`-Settlement Success  
`SETTLEMENT_PROCESSING`-Settlement Processing  
`CANCELED`-Canceled  
`FAILED`-Failed  
invest_currency | string | Optional |  | Investment Token  
exercise_currency | string | Optional |  | Strike Token  
exercise_price | string | Optional |  | Strike price  
settlement_price | string | Optional |  | Settlement price  
settlement_currency | string | Optional |  | Settlement currency  
apy_display | string | Optional |  | Annual Yield  
apy_settlement | string | Optional |  | Settlement Annual Yield  
delivery_time | integer(int32) | Optional |  | Settlement time  
text | string | Optional |  | Custom order information  
      
    
    {
      "id": 0,
      "plan_id": 0,
      "invest_amount": "string",
      "settlement_amount": "string",
      "create_time": 0,
      "complete_time": 0,
      "status": "string",
      "invest_currency": "string",
      "exercise_currency": "string",
      "exercise_price": "string",
      "settlement_price": "string",
      "settlement_currency": "string",
      "apy_display": "string",
      "apy_settlement": "string",
      "delivery_time": 0,
      "text": "string"
    }
    
    

##  AutoInvestMinInvestAmountResp

AvailableInvestmentMinimumAmountResponse

Type | Constraints  
---|---  
object | required: ["min_amount"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
min_amount | string | Required |  | MinimumAmount  
      
    
    {
      "min_amount": "string"
    }
    
    

##  AssetListStruct

Type | Constraints  
---|---  
array |   
  
**items**

Type | Constraints  
---|---  
object | required: ["pid","mortgage_coin","mortgage_amount","createStamp","extra_income","freeze_amount","move_income","type","status","income_total","yesterday_income_multi","reward_coins","defi_income"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
pid | integer | Required |  | Product ID  
mortgage_coin | string | Required |  | Staked currencies (multiple entries separated by commas)  
mortgage_amount | string | Required |  | Position amount  
createStamp | integer | Required |  | First timestamp  
extra_income | string | Required |  | Additional rewards converted to USDT amount  
freeze_amount | string | Required |  | Locked amount, used in trading  
move_income | string | Required |  |   
type | integer | Required |  | Type 0-voucher 1-locked position 2-US Treasury bond  
status | integer | Required |  | Status. 1 - currency project listed, 2 - currency project delisted  
income_total | string | Required |  | Total earnings by currency  
yesterday_income_multi | array | Required |  | Yesterday's earnings  
reward_coins | array | Required |  | Currency-specific reward earnings  
defi_income | object | Required | required: ["total"] | DEIF earnings  
  
**items / yesterday_income_multi**

Yesterday's earnings

Type | Constraints  
---|---  
array |   
  
**items / yesterday_income_multi / items**

Type | Constraints  
---|---  
object |   
  
**items / reward_coins**

Currency-specific reward earnings

Type | Constraints  
---|---  
array |   
  
**items / reward_coins / items**

Type | Constraints  
---|---  
object | required: ["reward_coin","interest_delay_days","reward_delay_days"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
reward_coin | string | Required |  | Reward currency  
interest_delay_days | integer | Required |  | Interest accrual day  
reward_delay_days | integer | Required |  | Dividend day -1 indicates dividends are distributed upon redemption  
  
**items / defi_income**

DEIF earnings

Type | Constraints  
---|---  
object | required: ["total"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
total | array | Required |  |   
  
**items / defi_income / total**

Type | Constraints  
---|---  
array |   
  
**items / defi_income / total / items**

Type | Constraints  
---|---  
object | required: ["coin","amount"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
coin | string | Required |  |   
amount | string | Required |  |   
      
    
    [
      {
        "pid": 0,
        "mortgage_coin": "string",
        "mortgage_amount": "string",
        "createStamp": 0,
        "extra_income": "string",
        "freeze_amount": "string",
        "move_income": "string",
        "type": 0,
        "status": 0,
        "income_total": "string",
        "yesterday_income_multi": [
          {}
        ],
        "reward_coins": [
          {}
        ],
        "defi_income": {
          "total": []
        }
      }
    ]
    
    

##  PlaceDualInvestmentOrderParams

Dual Investment Order

Type | Constraints  
---|---  
object | required: ["plan_id","amount"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
plan_id | string | Required |  | Product ID  
amount | string | Required |  | Subscription amount  
text | string | Optional |  | Order custom information. Users can set custom ID with this field. Custom fields must meet the following conditions:  
  
1\. Must start with `t-`  
2\. Excluding `t-`, length cannot exceed 28 bytes  
3\. Can only contain numbers, letters, underscore(_), hyphen(-) or dot(.)  
      
    
    {
      "plan_id": "string",
      "amount": "string",
      "text": "string"
    }
    
    

##  CreateEarnFixedTermPreRedeemResponse

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
code | integer | Optional |  | Return code, 0 means success  
message | string | Optional |  | Response message  
data | object | Optional |  | Redemption result (empty object on success)  
timestamp | integer | Optional |  | Response timestamp (in seconds)  
      
    
    {
      "code": 0,
      "message": "string",
      "data": {},
      "timestamp": 0
    }
    
    

##  SwapCoinStruct

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | integer | Optional |  | Order ID  
pid | integer | Optional |  | Product ID  
uid | integer | Optional |  | User ID  
coin | string | Optional |  | Currency  
type | integer | Optional |  | Type 0-Staking 1-Redemption  
subtype | string | Optional |  | SubType  
amount | string | Optional |  | Amount  
exchange_rate | string | Optional |  | Exchange ratio  
exchange_amount | string | Optional |  | Redemption Amount  
updateStamp | integer | Optional |  | Update timestamp  
createStamp | integer | Optional |  | Transaction timestamp  
status | integer | Optional |  | status 1-success  
protocol_type | integer | Optional |  | DEFI Protocol Type  
client_order_id | string | Optional |  | Reference ID  
source | string | Optional |  | Order Origin  
      
    
    {
      "id": 0,
      "pid": 0,
      "uid": 0,
      "coin": "string",
      "type": 0,
      "subtype": "string",
      "amount": "string",
      "exchange_rate": "string",
      "exchange_amount": "string",
      "updateStamp": 0,
      "createStamp": 0,
      "status": 0,
      "protocol_type": 0,
      "client_order_id": "string",
      "source": "string"
    }
    
    

##  DualOrderRefundParams

Dual-currency order early redemption request

Type | Constraints  
---|---  
object | required: ["order_id","req_id"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
order_id | string | Required |  | Order ID  
req_id | string | Required |  | Request ID returned by order-refund-preview  
      
    
    {
      "order_id": "string",
      "req_id": "string"
    }
    
    

##  AutoInvestPlanListInfoResp

Auto invest planListPaginatedResponse

Type | Constraints  
---|---  
object | required: ["page","page_size","page_count","total_count","list"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
page | integer(int64) | Required |  | page number  
page_size | integer(int64) | Required |  | Items per page  
page_count | integer(int64) | Required |  | Total pages  
total_count | integer(int64) | Required |  | Total entries  
list | array | Required |  | PlanList  
  
**list**

PlanList

Type | Constraints  
---|---  
array |   
  
**list / items**

Auto invest planDetails

Type | Constraints  
---|---  
object | required: ["id","name","create_time","update_time","user_id","money","amount","period_type","period_day","period_hour","portfolio","next_time","period","fund_source","fund_flow"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | integer(int64) | Required |  | Plan ID  
version | integer(int64) | Optional |  | PlanVersion  
name | string | Required |  | Plan name  
create_time | integer(int64) | Required |  | Creation time (Unix timestamp)  
update_time | integer(int64) | Required |  | Update time (Unix timestamp)  
user_id | integer(int64) | Required |  | User ID  
money | string | Required |  | Quote Currency  
amount | string | Required |  | Per PeriodInvestment amount  
period_type | string | Required |  | Cycle type（e.g., monthly）  
period_day | integer(int64) | Required |  | Cycle day  
period_hour | integer(int64) | Required |  | CycleHours  
portfolio | array | Required |  | Portfolio  
next_time | integer(int64) | Required |  | Next execution time (Unix timestamp)  
period | integer(int64) | Required |  | Executed periods  
fund_source | string | Required |  | Fund source（spot/earn）  
fund_flow | string | Required |  | Fund flow direction (auto_invest/earn)  
  
**list / items / portfolio**

Portfolio

Type | Constraints  
---|---  
array |   
  
**list / items / portfolio / items**

Auto invest plan portfolio item

Type | Constraints  
---|---  
object | required: ["asset","ratio","cum_invest","cum_hold","cum_redeem","avg_price","redeem_status","lend_amount"]  
      
    
    {
      "page": 0,
      "page_size": 0,
      "page_count": 0,
      "total_count": 0,
      "list": [
        {
          "id": 0,
          "version": 0,
          "name": "string",
          "create_time": 0,
          "update_time": 0,
          "user_id": 0,
          "money": "string",
          "amount": "string",
          "period_type": "string",
          "period_day": 0,
          "period_hour": 0,
          "portfolio": [],
          "next_time": 0,
          "period": 0,
          "fund_source": "string",
          "fund_flow": "string"
        }
      ]
    }
    
    

##  AutoInvestPlanStop

StopAuto invest planRequest

Type | Constraints  
---|---  
object | required: ["plan_id"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
plan_id | integer(int64) | Required |  | Plan ID  
      
    
    {
      "plan_id": 0
    }
    
    

##  CreateEarnFixedTermLendResponse

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
code | integer | Optional |  | Return code, 0 means success  
message | string | Optional |  | Response message  
data | object | Optional |  | Subscription result  
timestamp | integer | Optional |  | Response timestamp (in seconds)  
  
**data**

Subscription result

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
order_id | integer(int64) | Optional |  | Subscription order ID  
      
    
    {
      "code": 0,
      "message": "string",
      "data": {
        "order_id": 0
      },
      "timestamp": 0
    }
    
    

##  ListEarnFixedTermLendsResponse

Type | Constraints  
---|---  
object | required: ["code","message","data","timestamp"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
code | integer | Required |  | Return code, 0 means success  
message | string | Required |  | Response message  
data | object | Required | required: ["list","total"] | Subscription order list data  
timestamp | integer | Required |  | Response timestamp (in seconds)  
  
**data**

Subscription order list data

Type | Constraints  
---|---  
object | required: ["list","total"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
list | array | Required |  | Subscription order list  
total | integer | Required |  | Total Records  
  
**data / list**

Subscription order list

Type | Constraints  
---|---  
array |   
  
**data / list / items**

Fixed-term earn subscription order

Type | Constraints  
---|---  
FixedTermLendOrder |   
      
    
    {
      "code": 0,
      "message": "string",
      "data": {
        "list": [
          {}
        ],
        "total": 0
      },
      "timestamp": 0
    }
    
    

##  DualOrderRefundPreview

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
create_timest | integer(int64) | Optional |  | Order creation timestamp  
delivery_timest | integer(int64) | Optional |  | Order delivery timestamp  
exercise_price | string | Optional |  | Strike price  
invest_amount | string | Optional |  | Investment amount  
invest_currency | string | Optional |  | Investment Token  
name | string | Optional |  | Order name identifier  
order_id | integer(int64) | Optional |  | Order ID  
req_id | string | Optional |  | Request ID used for redemption, returned by GET /earn/dual/order-refund-preview. The request to POST /earn/dual/order-refund requires order_id and req_id.  
refund_service_charge | integer(int64) | Optional |  | Refund fee  
settle_price | string | Optional |  | Settlement price  
settlement_amount | string | Optional |  | Settlement amount  
settlement_currency | string | Optional |  | Settlement currency  
settlement_interest | string | Optional |  | Settlement interest  
settlement_principle | string | Optional |  | Settlement principal  
type | string | Optional |  | `call`: sell high; `put`: buy low  
money_back_timest | integer(int64) | Optional |  | Redemption time  
      
    
    {
      "create_timest": 0,
      "delivery_timest": 0,
      "exercise_price": "string",
      "invest_amount": "string",
      "invest_currency": "string",
      "name": "string",
      "order_id": 0,
      "req_id": "string",
      "refund_service_charge": 0,
      "settle_price": "string",
      "settlement_amount": "string",
      "settlement_currency": "string",
      "settlement_interest": "string",
      "settlement_principle": "string",
      "type": "string",
      "money_back_timest": 0
    }
    
    

##  ListEarnFixedTermProductsResponse

Type | Constraints  
---|---  
object | required: ["code","message","data","timestamp"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
code | integer | Required |  | Return code, 0 means success  
message | string | Required |  | Response message  
data | object | Required | required: ["list","total"] | Product list data  
timestamp | integer | Required |  | Response timestamp (in seconds)  
  
**data**

Product list data

Type | Constraints  
---|---  
object | required: ["list","total"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
list | array | Required |  | Product list  
total | integer | Required |  | Total Records  
  
**data / list**

Product list

Type | Constraints  
---|---  
array |   
  
**data / list / items**

Fixed-term earn product

Type | Constraints  
---|---  
FixedTermProduct |   
      
    
    {
      "code": 0,
      "message": "string",
      "data": {
        "list": [
          {}
        ],
        "total": 0
      },
      "timestamp": 0
    }
    
    

##  DualProjectRecommend

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | integer(int64) | Optional |  | Product ID  
category | integer(int32) | Optional |  | Strategy category  
type | string | Optional |  | `call`: sell high; `put`: buy low  
invest_currency | string | Optional |  | Investment Token  
exercise_currency | string | Optional |  | Strike Token  
apy_display | string | Optional |  | Annual Yield  
exercise_price | string | Optional |  | Strike price  
delivery_timest | integer(int64) | Optional |  | Settlement time  
min_amount | string | Optional |  | Minimum investment amount  
max_amount | string | Optional |  | Maximum investment amount  
min_copies | integer(int64) | Optional |  | Minimum Units  
max_copies | integer(int64) | Optional |  | Maximum Units  
invest_days | integer(int64) | Optional |  | Lock-up days  
invest_hours | string | Optional |  | Lock-up hours  
      
    
    {
      "id": 0,
      "category": 0,
      "type": "string",
      "invest_currency": "string",
      "exercise_currency": "string",
      "apy_display": "string",
      "exercise_price": "string",
      "delivery_timest": 0,
      "min_amount": "string",
      "max_amount": "string",
      "min_copies": 0,
      "max_copies": 0,
      "invest_days": 0,
      "invest_hours": "string"
    }
    
    

##  AutoInvestPlanCreate

Create auto invest planRequest

Type | Constraints  
---|---  
object | required: ["plan_money","plan_amount","plan_period_type","plan_period_day","plan_period_hour","items"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
plan_name | string | Optional |  | Plan name。Length: 0-50 characters  
plan_des | string | Optional |  | Plan description  
plan_money | string | Required |  | Pricing currency，SupportUSDT，BTC  
plan_amount | string | Required |  | Per PeriodAuto InvestAmount，Must > 0，and not exceedThePricing currencyConfigurationSingleMaximumAmount  
plan_period_type | string | Required |  | Enum: daily, weekly, biweekly, monthly, hourly, 4-hourly  
plan_period_day | integer(int64) | Required |  | Cycle day. For monthly: day of month (1-30); For weekly/biweekly: day of week (1-7, 1=Monday); For daily/hourly/4-hourly: ignored  
plan_period_hour | integer(int64) | Required |  | Execution hourAuto Invest 0-23  
items | array | Required |  | Investment portfolio, asset cannot be repeated; Sum of all items' ratios must be 100  
fund_source | string | Optional |  | Fund source: spot or earn, default: spot  
fund_flow | string | Optional |  | Fund flow direction: auto_invest or earn, default: auto_invest  
type | integer(int64) | Optional |  | 0 Normal creation, 1 QuickInvestment  
  
**items**

Investment portfolio, asset cannot be repeated; Sum of all items' ratios must be 100

Type | Constraints  
---|---  
array |   
  
**items / items**

Type | Constraints  
---|---  
object | required: ["asset","ratio"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
asset | string | Required |  | Investment currency, e.g., BTC; Must be enabled and market exists; Cannot be repeated within the same plan  
ratio | string | Required |  | The proportion of this currency in the portfolio，The sum of all items' ratios must be 100  
      
    
    {
      "plan_name": "string",
      "plan_des": "string",
      "plan_money": "string",
      "plan_amount": "string",
      "plan_period_type": "string",
      "plan_period_day": 0,
      "plan_period_hour": 0,
      "items": [
        {
          "asset": "string",
          "ratio": "string"
        }
      ],
      "fund_source": "string",
      "fund_flow": "string",
      "type": 0
    }
    
    

##  AutoInvestConfigItem

Investment currency configuration item

Type | Constraints  
---|---  
object | required: ["coin","max_limit"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
coin | string | Required |  | Currency  
max_limit | string | Required |  | InvestmentLimit  
      
    
    {
      "coin": "string",
      "max_limit": "string"
    }
    
    

##  AutoInvestCoinsItem

Currency item supporting auto invest

Type | Constraints  
---|---  
object | required: ["key","value","asset_icon_url"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
key | string | Required |  | Currency code  
value | string | Required |  | Currency name  
asset_icon_url | string | Required |  | Currency icon URL  
sort | integer(int64) | Optional |  | Sort  
      
    
    {
      "key": "string",
      "value": "string",
      "asset_icon_url": "string",
      "sort": 0
    }
    
    

##  AutoInvestMinInvestAmount

QueryAvailableInvestmentMinimumAmountRequest

Type | Constraints  
---|---  
object | required: ["money","asset_type","items"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
money | string | Required |  | Currency, optional: USDT or BTC  
asset_type | integer(int32) | Required | enum: [1,2] | Asset type: 1 for cryptocurrency, 2 for TradFi stocks; must be provided explicitly  
items | array | Required |  |   
  
**items**

Type | Constraints  
---|---  
array |   
  
**items / items**

Type | Constraints  
---|---  
object | required: ["asset","ratio"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
asset | string | Required |  | Currency  
ratio | string | Required |  | Ratio，e.g.100  
      
    
    {
      "money": "string",
      "asset_type": 1,
      "items": [
        {
          "asset": "string",
          "ratio": "string"
        }
      ]
    }
    
    

##  AutoInvestPlanAddPosition

Add position immediatelyRequest

Type | Constraints  
---|---  
object | required: ["plan_id","amount"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
plan_id | integer(int64) | Required |  | Plan ID  
amount | string | Required |  | Amount  
      
    
    {
      "plan_id": 0,
      "amount": "string"
    }
    
    

##  ListEarnFixedTermHistoryResponse

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
code | integer | Optional |  | Return code, 0 means success  
message | string | Optional |  | Response message  
data | object | Optional |  |   
timestamp | integer | Optional |  | Response timestamp (in seconds)  
  
**data**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
list | array | Optional |  |   
total | integer | Optional |  | Total Records  
  
**data / list**

Type | Constraints  
---|---  
array |   
  
**data / list / items**

Fixed-term earn history records

Type | Constraints  
---|---  
FixedTermHistoryRecord | required: ["id","user_id","asset","product_id","status","create_time","create_at"]  
      
    
    {
      "code": 0,
      "message": "string",
      "data": {
        "list": [
          {}
        ],
        "total": 0
      },
      "timestamp": 0
    }
    
    

##  DualGetPlans

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | integer(int32) | Optional |  | Product ID  
instrument_name | string | Optional |  | Product Name  
type | string | Optional |  | `call`: sell high; `put`: buy low  
invest_currency | string | Optional |  | Investment Token  
exercise_currency | string | Optional |  | Strike Token  
exercise_price | number(double) | Optional |  | Strike price  
delivery_time | integer(int32) | Optional |  | Settlement time  
apy_display | string | Optional |  | Annual Yield  
min_amount | string | Optional |  | Minimum investment amount  
start_time | integer(int32) | Optional |  | Start Time  
end_time | integer(int32) | Optional |  | End time  
status | string | Optional |  | Status:  
  
`NOTSTARTED` \- Not started  
`ONGOING` \- In progress  
`ENDED` \- Ended  
      
    
    {
      "id": 0,
      "instrument_name": "string",
      "type": "string",
      "invest_currency": "string",
      "exercise_currency": "string",
      "exercise_price": 0,
      "delivery_time": 0,
      "apy_display": "string",
      "min_amount": "string",
      "start_time": 0,
      "end_time": 0,
      "status": "string"
    }
    
    

##  AutoInvestPlanCreateResp

Create auto invest planResponse

Type | Constraints  
---|---  
object | required: ["id"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | integer(int64) | Required |  | Plan ID  
amount | string | Optional |  | Per PeriodAuto InvestAmount  
money | string | Optional |  | Quote currency  
next_time | integer(int64) | Optional |  | Next execution time  
period_type | string | Optional |  | Cycle type  
period_day | integer(int64) | Optional |  | Cycle day  
period_hour | integer(int64) | Optional |  | CycleHours  
fund_flow | string | Optional |  | Fund Flow Direction  
fund_source | string | Optional |  | Fund source  
      
    
    {
      "id": 0,
      "amount": "string",
      "money": "string",
      "next_time": 0,
      "period_type": "string",
      "period_day": 0,
      "period_hour": 0,
      "fund_flow": "string",
      "fund_source": "string"
    }
    
    

##  ListEarnFixedTermProductsByAssetResponse

Type | Constraints  
---|---  
object | required: ["code","message","data","timestamp"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
code | integer | Required |  | Return code, 0 means success  
message | string | Required |  | Response message  
data | object | Required | required: ["list"] | Product list data  
timestamp | integer | Required |  | Response timestamp (in seconds)  
  
**data**

Product list data

Type | Constraints  
---|---  
object | required: ["list"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
list | array | Required |  | Product list  
  
**data / list**

Product list

Type | Constraints  
---|---  
array |   
  
**data / list / items**

Fixed-term earn product (compact)

Type | Constraints  
---|---  
FixedTermProductSimple |   
      
    
    {
      "code": 0,
      "message": "string",
      "data": {
        "list": [
          {}
        ]
      },
      "timestamp": 0
    }
    
    

##  AwardListStruct

Type | Constraints  
---|---  
object | required: ["page","pageSize","pageCount","totalCount","list"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
page | integer | Required |  | Page  
pageSize | integer | Required |  | Items per page  
pageCount | integer | Required |  | Total pages  
totalCount | integer | Required |  | Total entries  
list | array | Required |  |   
  
**list**

Type | Constraints  
---|---  
array |   
  
**list / items**

Type | Constraints  
---|---  
object | required: ["pid","mortgage_coin","amount","reward_coin","interest","fee","status","bonus_date","should_bonus_stamp"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
pid | integer | Required |  | Product ID  
mortgage_coin | string | Required |  | Collateral currency  
amount | string | Required |  | Amount  
reward_coin | string | Required |  | Reward currency  
interest | string | Required |  | Interest amount  
fee | string | Required |  | fee  
status | integer | Required |  | Status. 4 - success  
bonus_date | string | Required |  | Date  
should_bonus_stamp | integer | Required |  | Scheduled distribution timestamp  
      
    
    {
      "page": 0,
      "pageSize": 0,
      "pageCount": 0,
      "totalCount": 0,
      "list": [
        {
          "pid": 0,
          "mortgage_coin": "string",
          "amount": "string",
          "reward_coin": "string",
          "interest": "string",
          "fee": "string",
          "status": 0,
          "bonus_date": "string",
          "should_bonus_stamp": 0
        }
      ]
    }
    
    

##  SwapCoin

Blockchain Mining

Type | Constraints  
---|---  
object | required: ["coin","side","amount"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
coin | string | Required |  | Currency  
side | integer | Required |  | 0 - Stake 1 - Redeem  
amount | string | Required |  | Size  
pid | integer | Optional |  | DeFi-type Mining Protocol Identifier  
      
    
    {
      "coin": "string",
      "side": 0,
      "amount": "string",
      "pid": 0
    }
    
    

##  DualModifyOrderReinvestParams

Dual-currency order reinvest modification request

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
order_id | integer(int64) | Optional |  | Order ID  
status | integer(int32) | Optional |  | `0` — off; `1` — on  
effective_time_duration | integer(int64) | Optional |  | Effective duration in seconds; default 1 day (86400)  
      
    
    {
      "order_id": 0,
      "status": 0,
      "effective_time_duration": 0
    }
    
    

##  AutoInvestPlanDetail

Auto invest planDetails

Type | Constraints  
---|---  
object | required: ["id","name","create_time","update_time","user_id","money","amount","period_type","period_day","period_hour","portfolio","next_time","period","fund_source","fund_flow"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | integer(int64) | Required |  | Plan ID  
version | integer(int64) | Optional |  | PlanVersion  
name | string | Required |  | Plan name  
create_time | integer(int64) | Required |  | Creation time (Unix timestamp)  
update_time | integer(int64) | Required |  | Update time (Unix timestamp)  
user_id | integer(int64) | Required |  | User ID  
money | string | Required |  | Quote Currency  
amount | string | Required |  | Per PeriodInvestment amount  
period_type | string | Required |  | Cycle type（e.g., monthly）  
period_day | integer(int64) | Required |  | Cycle day  
period_hour | integer(int64) | Required |  | CycleHours  
portfolio | array | Required |  | Portfolio  
next_time | integer(int64) | Required |  | Next execution time (Unix timestamp)  
period | integer(int64) | Required |  | Executed periods  
fund_source | string | Required |  | Fund source（spot/earn）  
fund_flow | string | Required |  | Fund flow direction (auto_invest/earn)  
  
**portfolio**

Portfolio

Type | Constraints  
---|---  
array |   
  
**portfolio / items**

Auto invest plan portfolio item

Type | Constraints  
---|---  
object | required: ["asset","ratio","cum_invest","cum_hold","cum_redeem","avg_price","redeem_status","lend_amount"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
asset | string | Required |  | Currency  
ratio | string | Required |  | Ratio  
cum_invest | string | Required |  | Accumulated investment  
cum_hold | string | Required |  | AccumulatedPosition  
cum_redeem | string | Required |  | Accumulated redemption  
avg_price | string | Required |  | Average Cost Price  
redeem_status | integer(int64) | Required |  | Redemption status  
lend_amount | string | Required |  | LendingQuantity  
      
    
    {
      "id": 0,
      "version": 0,
      "name": "string",
      "create_time": 0,
      "update_time": 0,
      "user_id": 0,
      "money": "string",
      "amount": "string",
      "period_type": "string",
      "period_day": 0,
      "period_hour": 0,
      "portfolio": [
        {
          "asset": "string",
          "ratio": "string",
          "cum_invest": "string",
          "cum_hold": "string",
          "cum_redeem": "string",
          "avg_price": "string",
          "redeem_status": 0,
          "lend_amount": "string"
        }
      ],
      "next_time": 0,
      "period": 0,
      "fund_source": "string",
      "fund_flow": "string"
    }
    
    

##  EarnFixedTermPreRedeemRequest

Type | Constraints  
---|---  
object | required: ["order_id"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
order_id | string | Required |  | Order ID  
      
    
    {
      "order_id": "5862476630"
    }
    
    

##  OrderListStruct

Type | Constraints  
---|---  
object | required: ["page","pageSize","pageCount","totalCount","list"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
page | integer | Required |  | Page  
pageSize | integer | Required |  | Items per page  
pageCount | integer | Required |  | Total pages  
totalCount | integer | Required |  | Total entries  
list | array | Required |  |   
  
**list**

Type | Constraints  
---|---  
array |   
  
**list / items**

Type | Constraints  
---|---  
object | required: ["pid","coin","amount","type","status","redeem_stamp","createStamp","exchange_amount","fee"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
pid | integer | Required |  | Product ID  
coin | string | Required |  | Staked and redeemed currencies  
amount | string | Required |  | Amount  
type | integer | Required |  | Type 0-Staking 1-Redemption  
status | integer | Required |  | Status. 1 - success, 3 - delayed redemption in progress, 6 - redemption cancellation order  
redeem_stamp | integer | Required |  | Redemption credit time  
createStamp | integer | Required |  | Order time  
exchange_amount | string | Required |  | Exchange rate  
fee | string | Required |  | fee  
      
    
    {
      "page": 0,
      "pageSize": 0,
      "pageCount": 0,
      "totalCount": 0,
      "list": [
        {
          "pid": 0,
          "coin": "string",
          "amount": "string",
          "type": 0,
          "status": 0,
          "redeem_stamp": 0,
          "createStamp": 0,
          "exchange_amount": "string",
          "fee": "string"
        }
      ]
    }
    
    

##  AutoInvestOrderItem

Auto invest order item

Type | Constraints  
---|---  
object | required: ["id","type","amount","plan_id","side","asset","record_id","total_money","market","price","create_time","total","fund_flow","error_code","error_msg","status"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | integer(int64) | Required |  | Order ID  
type | string | Required |  | Type  
amount | string | Required |  | Size  
plan_id | integer(int64) | Required |  | Plan ID  
side | integer(int64) | Required |  | direction  
asset | string | Required |  | Currency  
record_id | integer(int64) | Required |  | Record ID  
total_money | string | Required |  | TotalAmount  
market | string | Required |  | Currency pair  
price | string | Required |  | Price  
create_time | integer(int64) | Required |  | Creation time (Unix timestamp)  
total | string | Required |  | Total  
fund_flow | string | Required |  | Fund Flow Direction  
error_code | integer(int64) | Required |  | Error code  
error_msg | string | Required |  | Error message  
status | integer(int64) | Required |  | Status  
      
    
    {
      "id": 0,
      "type": "string",
      "amount": "string",
      "plan_id": 0,
      "side": 0,
      "asset": "string",
      "record_id": 0,
      "total_money": "string",
      "market": "string",
      "price": "string",
      "create_time": 0,
      "total": "string",
      "fund_flow": "string",
      "error_code": 0,
      "error_msg": "string",
      "status": 0
    }
    
    

##  DualGetBalance

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
user_asset_usdt | string | Optional |  | User Assets in USDT Equivalent  
user_asset_btc | string | Optional |  | User Assets in BTC Equivalent  
user_total_interest_usdt | string | Optional |  | Total User Interest in USDT Equivalent  
user_total_interest_btc | string | Optional |  | Total User Interest in BTC Equivalent  
      
    
    {
      "user_asset_usdt": "string",
      "user_asset_btc": "string",
      "user_total_interest_usdt": "string",
      "user_total_interest_btc": "string"
    }
    
    

##  PlaceDualInvestmentOrder

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | integer(int32) | Optional |  | Order ID  
plan_id | integer(int32) | Optional |  | Product ID  
invest_amount | string | Optional |  | Investment Quantity  
settlement_amount | string | Optional |  | Settlement Quantity  
create_time | integer(int32) | Optional |  | Created time  
complete_time | integer(int32) | Optional |  | Completed Time  
status | string | Optional |  | Status:  
  
`INIT`-Created  
`SETTLEMENT_SUCCESS`-Settlement Success  
`SETTLEMENT_PROCESSING`-Settlement Processing  
`CANCELED`-Canceled  
`FAILED`-Failed  
invest_currency | string | Optional |  | Investment Token  
exercise_currency | string | Optional |  | Strike Token  
exercise_price | string | Optional |  | Strike price  
settlement_price | string | Optional |  | Settlement price  
settlement_currency | string | Optional |  | Settlement currency  
apy_display | string | Optional |  | Annual Yield  
apy_settlement | string | Optional |  | Settlement Annual Yield  
delivery_time | integer(int32) | Optional |  | Settlement time  
text | string | Optional |  | Custom order information  
      
    
    {
      "id": 0,
      "plan_id": 0,
      "invest_amount": "string",
      "settlement_amount": "string",
      "create_time": 0,
      "complete_time": 0,
      "status": "string",
      "invest_currency": "string",
      "exercise_currency": "string",
      "exercise_price": "string",
      "settlement_price": "string",
      "settlement_currency": "string",
      "apy_display": "string",
      "apy_settlement": "string",
      "delivery_time": 0,
      "text": "string"
    }
    
    

##  AutoInvestPlanRecordsResp

PlanExecutionRecordPaginatedResponse

Type | Constraints  
---|---  
object | required: ["page","page_size","total_page","total","list"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
page | integer(int64) | Required |  | page number  
page_size | integer(int64) | Required |  | Items per page  
total_page | integer(int64) | Required |  | TotalPage number  
total | integer(int64) | Required |  | Total entries  
list | array | Required |  |   
  
**list**

Type | Constraints  
---|---  
array |   
  
**list / items**

Plan execution record item

Type | Constraints  
---|---  
object | required: ["id","type","money","user_id","plan_id","plan_version","amount","create_time","update_time","status","status_type","side","status_message"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | integer(int64) | Required |  | Record ID  
type | string | Required |  | Type  
money | string | Required |  | SourceCurrency  
user_id | integer(int64) | Required |  | User ID  
plan_id | integer(int64) | Required |  | Plan ID  
plan_version | integer(int64) | Required |  | PlanVersion  
amount | string | Required |  | Investment amount  
create_time | integer(int64) | Required |  | Investment time  
update_time | integer(int64) | Required |  | Update time  
status | string | Required |  | Status  
status_type | integer(int64) | Required |  | Status enum  
side | integer(int64) | Required |  | 2 = Buy, Other = Sell  
status_message | string | Required |  | Status description  
detail | string | Optional |  | Details  
asset | string | Optional |  | Currency  
      
    
    {
      "page": 0,
      "page_size": 0,
      "total_page": 0,
      "total": 0,
      "list": [
        {
          "id": 0,
          "type": "string",
          "money": "string",
          "user_id": 0,
          "plan_id": 0,
          "plan_version": 0,
          "amount": "string",
          "create_time": 0,
          "update_time": 0,
          "status": "string",
          "status_type": 0,
          "side": 0,
          "status_message": "string",
          "detail": "string",
          "asset": "string"
        }
      ]
    }
    
    

##  AutoInvestPlanUpdate

Request to update an auto-invest plan. The current model contains plan_id, fund_source, and fund_flow.

Type | Constraints  
---|---  
object | required: ["plan_id"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
plan_id | integer(int64) | Required |  | Plan ID  
fund_source | string | Optional |  | Fund source Spotspot or Flexible Savingsearn，Default spot  
fund_flow | string | Optional |  | Fund Flow Direction Spotauto_invest or Flexible Savingsearn，Default auto_invest  
      
    
    {
      "plan_id": 0,
      "fund_source": "string",
      "fund_flow": "string"
    }
    
    

##  FixedTermLendOrder

Fixed-term earn subscription order

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | integer | Optional |  | Subscription record ID  
business | integer | Optional |  | Business type: 1 for regular, 2 for VIP  
order_id | integer(int64) | Optional |  | Order ID  
user_id | integer(int64) | Optional |  | User ID  
asset | string | Optional |  | Currency  
product_id | integer | Optional |  | Product ID  
lock_up_period | integer | Optional |  | Lock-up period (in days)  
principal | string | Optional |  | Subscription principal  
year_rate | string | Optional |  | Annual interest rate  
product_type | integer | Optional |  | Product type: 1 for regular, 2 for VIP  
interest | string | Optional |  | Accrued interest  
status | integer | Optional |  | Order status: 1 for holding, 2 for redeemed, 3 for matured, 4 for settled  
reinvest_status | integer | Optional |  | Auto-renewal status: 0 for disabled, 1 for enabled  
redeem_account_type | integer | Optional |  | Redemption payout account type: 1 for spot account  
origin_order | string | Optional |  | Original order ID, linked to previous order IDs in auto-renewal scenarios  
redeem_type | integer | Optional |  | Redemption type: 1 for early redemption, 2 for maturity redemption  
redeem_time | string | Optional |  | Redemption time  
finish_time | string | Optional |  | Expiration time  
create_time | string | Optional |  | Created time  
year_rate_perent | string | Optional |  | Annual interest rate percentage display value  
total_year_rate_percent | string | Optional |  | Comprehensive annualized yield percentage (including interest rate boost, rewards, etc.)  
total_interest | string | Optional |  | Total earnings (including interest and bonus rewards)  
product_info | FixedTermProductInfo | Optional | required: ["pre_redeem","reinvest","redeem_account","min_vip","max_vip"] | Product configuration  
bonus_info | FixedTermBonusInfo | Optional |  | Bonus reward campaign information  
coupon_info | FixedTermCouponInfo | Optional | required: ["id","business","user_id","asset","order_id","financial_rate_id","buy_limit_low","buy_limit_high","rate_day","rate_ratio","coupon_days","coupon_principal","coupon_year_rate","coupon_interest","status","finish_time","create_time"] | Interest rate boost coupon information  
redeem_at | integer | Optional |  | Redemption timestamp (in seconds)  
finish_at | integer | Optional |  | Expiration timestamp (in seconds)  
create_at | integer | Optional |  | Creation timestamp (in seconds)  
icon | string | Optional |  | Currency icon URL  
      
    
    {
      "id": 0,
      "business": 0,
      "order_id": 0,
      "user_id": 0,
      "asset": "string",
      "product_id": 0,
      "lock_up_period": 0,
      "principal": "string",
      "year_rate": "string",
      "product_type": 0,
      "interest": "string",
      "status": 0,
      "reinvest_status": 0,
      "redeem_account_type": 0,
      "origin_order": "string",
      "redeem_type": 0,
      "redeem_time": "string",
      "finish_time": "string",
      "create_time": "string",
      "year_rate_perent": "string",
      "total_year_rate_percent": "string",
      "total_interest": "string",
      "product_info": {
        "pre_redeem": 0,
        "reinvest": 0,
        "redeem_account": 0,
        "min_vip": 0,
        "max_vip": 0
      },
      "bonus_info": {
        "id": 0,
        "product_id": 0,
        "asset": "string",
        "bonus_asset": "string",
        "kyc_limit": "string",
        "ladder_apr": [
          {}
        ],
        "total_bonus_amount": "string",
        "user_total_bonus_amount": "string",
        "status": 0,
        "start_time": "string",
        "end_time": "string",
        "create_time": "string",
        "start_at": 0,
        "end_at": 0,
        "total_issued_amount": "string",
        "user_total_issued_amount": "string",
        "bonus_asset_price": "string",
        "product_asset_price": "string",
        "product_year_rate": "string"
      },
      "coupon_info": {
        "id": 0,
        "business": 0,
        "user_id": 0,
        "asset": "string",
        "order_id": 0,
        "financial_rate_id": 0,
        "buy_limit_low": "string",
        "buy_limit_high": "string",
        "rate_day": 0,
        "rate_ratio": "string",
        "coupon_days": 0,
        "coupon_principal": "string",
        "coupon_year_rate": "string",
        "coupon_interest": "string",
        "status": 0,
        "finish_time": "string",
        "create_time": "string"
      },
      "redeem_at": 0,
      "finish_at": 0,
      "create_at": 0,
      "icon": "string"
    }
    
    

##  FindCoinStruct

Type | Constraints  
---|---  
array |   
  
**items**

Type | Constraints  
---|---  
object | required: ["pid","currencyRewards","exchangeRate","redeemPeriod","protocolName","maxStakeAmount","minStakeAmount","estimateApr","currency","isDefi","productType","exchangeRateReserve"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
pid | integer | Required |  | Product ID  
productType | integer | Required |  | Project type 0-voucher 1-locked position 2-US Treasury bond  
isDefi | integer | Required |  | Is DEFI protocol 0-no 1-yes  
currency | string | Required |  | Staked currencies (multiple entries separated by commas)  
estimateApr | string | Required |  | Estimated yield rate  
minStakeAmount | string | Required |  | Minimum staked amount  
maxStakeAmount | string | Required |  | Maximum staked amount  
protocolName | string | Required |  | Protocol name  
redeemPeriod | string | Required |  | Redemption period (days)  
exchangeRate | string | Required |  | Exchange rate  
exchangeRateReserve | string | Required |  | Reverse exchange rate  
extraInterest | array | Optional |  | Additional rewards  
currencyRewards | array | Required |  | Reward currency information  
  
**items / extraInterest**

Additional rewards

Type | Constraints  
---|---  
array |   
  
**items / extraInterest / items**

Type | Constraints  
---|---  
object | required: ["start_time","segment_interest","end_time","reward_coin"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
start_time | string | Required |  | Start timestamp  
end_time | string | Required |  | End Timestamp  
reward_coin | string | Required |  | Additional reward currency  
segment_interest | array | Required |  | Tiered reward information  
  
**items / extraInterest / items / segment_interest**

Tiered reward information

Type | Constraints  
---|---  
array |   
  
**items / extraInterest / items / segment_interest / items**

Type | Constraints  
---|---  
object | required: ["money_min","money_rate","money_max"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
money_min | string | Required |  | Tiered lower value  
money_max | string | Required |  | Tiered upper value  
money_rate | string | Required |  | Tiered interest rate  
  
**items / currencyRewards**

Reward currency information

Type | Constraints  
---|---  
array |   
  
**items / currencyRewards / items**

Type | Constraints  
---|---  
object | required: ["apr","reward_delay_days","reward_coin","interest_delay_days"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
apr | string | Required |  | Base interest rate  
reward_coin | string | Required |  | Reward currency  
reward_delay_days | string | Required |  | Dividend day -1 indicates dividends are distributed upon redemption  
interest_delay_days | string | Required |  | Interest accrual day  
      
    
    [
      {
        "pid": 0,
        "productType": 0,
        "isDefi": 0,
        "currency": "string",
        "estimateApr": "string",
        "minStakeAmount": "string",
        "maxStakeAmount": "string",
        "protocolName": "string",
        "redeemPeriod": "string",
        "exchangeRate": "string",
        "exchangeRateReserve": "string",
        "extraInterest": [
          {}
        ],
        "currencyRewards": [
          {}
        ]
      }
    ]
    
    

##  FixedTermLendRequest

Subscription request

Type | Constraints  
---|---  
object | required: ["product_id","amount"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
product_id | integer | Required |  | Product ID  
amount | string | Required |  | Subscription amount  
year_rate | string | Optional |  | Annual interest rate  
reinvest_status | integer | Optional |  | Auto-renewal status: 0 for disabled, 1 for enabled  
redeem_account_type | integer | Optional |  | Redemption payout account type: 1 for spot account  
financial_rate_id | integer | Optional |  | Interest rate boost coupon ID, 0 means not used  
sub_business | integer | Optional |  | Sub-business type  
      
    
    {
      "product_id": 0,
      "amount": "string",
      "year_rate": "string",
      "reinvest_status": 0,
      "redeem_account_type": 0,
      "financial_rate_id": 0,
      "sub_business": 0
    }
    
    

##  FixedTermBonusInfo

Bonus reward campaign information

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | integer | Optional |  | Activity ID  
product_id | integer | Optional |  | Associated product ID  
asset | string | Optional |  | Product currency  
bonus_asset | string | Optional |  | Reward currency  
kyc_limit | string | Optional |  | KYC level restrictions, comma-separated  
ladder_apr | array | Optional |  | Tiered annual interest rate  
total_bonus_amount | string | Optional |  | Total reward amount  
user_total_bonus_amount | string | Optional |  | Maximum reward per user  
status | integer | Optional |  | Activity status: 1 for unlisted, 2 for listed, 3 for delisted  
start_time | string | Optional |  | Activity start time  
end_time | string | Optional |  | Activity end time  
create_time | string | Optional |  | Created time  
start_at | integer | Optional |  | Activity start timestamp (in seconds)  
end_at | integer | Optional |  | Activity end timestamp (in seconds)  
total_issued_amount | string | Optional |  | Total rewards distributed  
user_total_issued_amount | string | Optional |  | Total rewards distributed to the user  
bonus_asset_price | string | Optional |  | Reward currency price (denominated in USDT)  
product_asset_price | string | Optional |  | Product currency price (denominated in USDT)  
product_year_rate | string | Optional |  | Product base annual interest rate  
  
**ladder_apr**

Tiered annual interest rate

Type | Constraints  
---|---  
array |   
  
**ladder_apr / items**

Type | Constraints  
---|---  
LadderApr | required: ["apr","left","right"]  
      
    
    {
      "id": 0,
      "product_id": 0,
      "asset": "string",
      "bonus_asset": "string",
      "kyc_limit": "string",
      "ladder_apr": [
        {
          "apr": "string",
          "left": "string",
          "right": "string"
        }
      ],
      "total_bonus_amount": "string",
      "user_total_bonus_amount": "string",
      "status": 0,
      "start_time": "string",
      "end_time": "string",
      "create_time": "string",
      "start_at": 0,
      "end_at": 0,
      "total_issued_amount": "string",
      "user_total_issued_amount": "string",
      "bonus_asset_price": "string",
      "product_asset_price": "string",
      "product_year_rate": "string"
    }
    
    

##  FixedTermProduct

Fixed-term earn product

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | integer | Optional |  | Product ID  
name | string | Optional |  | Product name  
asset | string | Optional |  | Currency  
lock_up_period | integer | Optional |  | Lock-up period (in days)  
min_lend_amount | string | Optional |  | Minimum earn amount  
user_max_lend_amount | string | Optional |  | User maximum earn limit  
total_lend_amount | string | Optional |  | Platform earn limit  
year_rate | string | Optional |  | Annual interest rate  
type | integer | Optional |  | Product type: 1 for regular, 2 for VIP  
pre_redeem | integer | Optional |  | Whether early redemption is supported: 0 for not supported, 1 for supported  
reinvest | integer | Optional |  | Whether auto-renewal is supported: 0 for not supported, 1 for supported  
redeem_account | integer | Optional |  | Whether fixed-to-flexible conversion is supported: 0 for not supported, 1 for supported  
min_vip | integer | Optional |  | Minimum VIP level requirement, 0-16, 0 means no restriction  
max_vip | integer | Optional |  | Maximum VIP level requirement (0-16), 0 means no restriction  
status | integer | Optional |  | Product status: 1 for unlisted, 2 for listed, 3 for delisted  
create_time | string | Optional |  | Created time  
user_max_lend_volume | string | Optional |  | User maximum earn amount  
user_total_amount | string | Optional |  | Total amount the user has invested in earn products  
sale_status | integer | Optional |  | Sale status: 1 for on sale, 2 for sold out  
      
    
    {
      "id": 0,
      "name": "string",
      "asset": "string",
      "lock_up_period": 0,
      "min_lend_amount": "string",
      "user_max_lend_amount": "string",
      "total_lend_amount": "string",
      "year_rate": "string",
      "type": 0,
      "pre_redeem": 0,
      "reinvest": 0,
      "redeem_account": 0,
      "min_vip": 0,
      "max_vip": 0,
      "status": 0,
      "create_time": "string",
      "user_max_lend_volume": "string",
      "user_total_amount": "string",
      "sale_status": 0
    }
    
    

##  FixedTermHistoryRecord

Fixed-term earn history records

Type | Constraints  
---|---  
object | required: ["id","user_id","asset","product_id","status","create_time","create_at"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | integer | Required |  | Record ID  
order_id | integer(int64) | Optional |  | Order ID  
user_id | integer(int64) | Required |  | User ID  
asset | string | Required |  | Currency  
uniq_time | string | Optional |  | Unique time identifier (date)  
bonus_id | integer | Optional |  | Reward campaign ID  
product_id | integer | Required |  | Product ID  
bonus_asset | string | Optional |  | Reward currency  
total_principal | string | Optional |  | Total principal  
amount | string | Optional |  | Amount  
asset_price | string | Optional |  | Currency price  
status | integer | Required |  | Status  
detail | string | Optional |  | Detail description  
create_time | string | Required |  | Created time  
create_at | integer | Required |  | Creation timestamp (in seconds)  
lock_up_period | integer | Optional |  | Term  
      
    
    {
      "id": 0,
      "order_id": 0,
      "user_id": 0,
      "asset": "string",
      "uniq_time": "string",
      "bonus_id": 0,
      "product_id": 0,
      "bonus_asset": "string",
      "total_principal": "string",
      "amount": "string",
      "asset_price": "string",
      "status": 0,
      "detail": "string",
      "create_time": "string",
      "create_at": 0,
      "lock_up_period": 0
    }
    
    

##  FixedTermProductSimple

Fixed-term earn product (compact)

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | integer | Optional |  | Product ID  
asset | string | Optional |  | Currency  
lock_up_period | integer | Optional |  | Lock-up period (in days)  
year_rate | string | Optional |  | Annual interest rate  
type | integer | Optional |  | Product type: 1 for regular, 2 for VIP  
pre_redeem | integer | Optional |  | Whether early redemption is supported: 0 for not supported, 1 for supported  
reinvest | integer | Optional |  | Whether auto-renewal is supported: 0 for not supported, 1 for supported  
simple_earn | integer | Optional |  | Whether fixed-to-flexible conversion is supported: 0 for not supported, 1 for supported  
min_vip | integer | Optional |  | Minimum VIP level requirement, 0 means no restriction  
max_vip | integer | Optional |  | Maximum VIP level requirement, 0 means no restriction  
sale_status | integer | Optional |  | Sale status: 1 for on sale, 2 for sold out  
      
    
    {
      "id": 0,
      "asset": "string",
      "lock_up_period": 0,
      "year_rate": "string",
      "type": 0,
      "pre_redeem": 0,
      "reinvest": 0,
      "simple_earn": 0,
      "min_vip": 0,
      "max_vip": 0,
      "sale_status": 0
    }
    
    

##  LadderApr

Type | Constraints  
---|---  
object | required: ["apr","left","right"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
apr | string | Required |  | Annualized interest rate  
left | string | Required |  | Range lower limit  
right | string | Required |  | Range upper limit  
      
    
    {
      "apr": "string",
      "left": "string",
      "right": "string"
    }
    
    

##  FixedTermCouponInfo

Interest rate boost coupon information

Type | Constraints  
---|---  
object | required: ["id","business","user_id","asset","order_id","financial_rate_id","buy_limit_low","buy_limit_high","rate_day","rate_ratio","coupon_days","coupon_principal","coupon_year_rate","coupon_interest","status","finish_time","create_time"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | integer | Required |  | Interest rate boost coupon record ID  
business | integer | Required |  | Business Type  
user_id | integer(int64) | Required |  | User ID  
asset | string | Required |  | Currency  
order_id | integer(int64) | Required |  | Associated order ID  
financial_rate_id | integer | Required |  | Interest rate boost coupon ID  
buy_limit_low | string | Required |  | Minimum subscription amount for interest rate boost coupon  
buy_limit_high | string | Required |  | Maximum subscription amount for interest rate boost coupon  
rate_day | integer | Required |  | Interest rate boost days  
rate_ratio | string | Required |  | Interest rate boost percentage  
coupon_days | integer | Required |  | Actual interest rate boost days  
coupon_principal | string | Required |  | Principal for interest rate boost calculation  
coupon_year_rate | string | Required |  | Interest rate boost APR  
coupon_interest | string | Required |  | Interest generated from rate boost  
status | integer | Required |  | Status: 1 for active, 2 for settled  
finish_time | string | Required |  | Settlement time  
create_time | string | Required |  | Created time  
      
    
    {
      "id": 0,
      "business": 0,
      "user_id": 0,
      "asset": "string",
      "order_id": 0,
      "financial_rate_id": 0,
      "buy_limit_low": "string",
      "buy_limit_high": "string",
      "rate_day": 0,
      "rate_ratio": "string",
      "coupon_days": 0,
      "coupon_principal": "string",
      "coupon_year_rate": "string",
      "coupon_interest": "string",
      "status": 0,
      "finish_time": "string",
      "create_time": "string"
    }
    
    

##  FixedTermProductInfo

Product configuration

Type | Constraints  
---|---  
object | required: ["pre_redeem","reinvest","redeem_account","min_vip","max_vip"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
pre_redeem | integer | Required |  | Whether early redemption is supported: 0 for not supported, 1 for supported  
reinvest | integer | Required |  | Whether auto-renewal is supported: 0 for not supported, 1 for supported  
redeem_account | integer | Required |  | Redemption payout account type  
min_vip | integer | Required |  | Minimum VIP level requirement, 0 means no restriction  
max_vip | integer | Required |  | Maximum VIP level requirement, 0 means no restriction  
      
    
    {
      "pre_redeem": 0,
      "reinvest": 0,
      "redeem_account": 0,
      "min_vip": 0,
      "max_vip": 0
    }