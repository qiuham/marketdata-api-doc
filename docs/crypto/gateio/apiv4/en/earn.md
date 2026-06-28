---
exchange: gateio
source_url: https://www.gate.com/docs/developers/apiv4/en/earn
api_type: Earn
updated_at: 2026-05-27 20:15:01.006292
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

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Successfully retrieved

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Successfully retrieved | [DualGetPlans]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | none  
» id | integer(int32) | Product ID  
» instrument_name | string | Product Name  
» invest_currency | string | Investment Token  
» exercise_currency | string | Strike Token  
» exercise_price | number(double) | Strike price  
» delivery_time | integer(int32) | Settlement time  
» apy_display | string | Annual Yield  
» min_amount | string | Minimum investment amount  
» start_time | integer(int32) | Start Time  
» end_time | integer(int32) | End time  
» status | string | Status:  
  
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

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Successfully retrieved

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Successfully retrieved | [DualGetOrders]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | none  
» id | integer(int32) | Order ID  
» plan_id | integer(int32) | Product ID  
» invest_amount | string | Investment Quantity  
» settlement_amount | string | Settlement Quantity  
» create_time | integer(int32) | Created time  
» complete_time | integer(int32) | Completed Time  
» status | string | Status:  
  
`INIT`-Created  
`SETTLEMENT_SUCCESS`-Settlement Success  
`SETTLEMENT_PROCESSING`-Settlement Processing  
`CANCELED`-Canceled  
`FAILED`-Failed  
» invest_currency | string | Investment Token  
» exercise_currency | string | Strike Token  
» exercise_price | string | Strike price  
» settlement_price | string | Settlement price  
» settlement_currency | string | Settlement currency  
» apy_display | string | Annual Yield  
» apy_settlement | string | Settlement Annual Yield  
» delivery_time | integer(int32) | Settlement time  
» text | string | Custom order information  
  
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
↳ plan_id | body | string | Required | Product ID  
↳ amount | body | string | Required | Subscription amount  
↳ text | body | string | Optional | Order custom information. Users can set custom ID with this field. Custom fields must meet the following conditions:  
  
1\. Must start with `t-`  
2\. Excluding `t-`, length cannot exceed 28 bytes  
3\. Can only contain numbers, letters, underscore(_), hyphen(-) or dot(.)  
  
####  Detailed descriptions

**» text** : Order custom information. Users can set custom ID with this field. Custom fields must meet the following conditions:  
  
1\. Must start with `t-`  
2\. Excluding `t-`, length cannot exceed 28 bytes  
3\. Can only contain numbers, letters, underscore(_), hyphen(-) or dot(.)

### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Order placed successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Order placed successfully | PlaceDualInvestmentOrder  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» id | integer(int32) | Order ID  
» plan_id | integer(int32) | Product ID  
» invest_amount | string | Investment Quantity  
» settlement_amount | string | Settlement Quantity  
» create_time | integer(int32) | Created time  
» complete_time | integer(int32) | Completed Time  
» status | string | Status:  
  
`INIT`-Created  
`SETTLEMENT_SUCCESS`-Settlement Success  
`SETTLEMENT_PROCESSING`-Settlement Processing  
`CANCELED`-Canceled  
`FAILED`-Failed  
» invest_currency | string | Investment Token  
» exercise_currency | string | Strike Token  
» exercise_price | string | Strike price  
» settlement_price | string | Settlement price  
» settlement_currency | string | Settlement currency  
» apy_display | string | Annual Yield  
» apy_settlement | string | Settlement Annual Yield  
» delivery_time | integer(int32) | Settlement time  
» text | string | Custom order information  
  
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

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Successfully retrieved

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Successfully retrieved | DualGetBalance  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» user_asset_usdt | string | User Assets in USDT Equivalent  
» user_asset_btc | string | User Assets in BTC Equivalent  
» user_total_interest_usdt | string | Total User Interest in USDT Equivalent  
» user_total_interest_btc | string | Total User Interest in BTC Equivalent  
  
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

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Successfully retrieved

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Successfully retrieved | DualOrderRefundPreview  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» create_timest | integer(int64) | Order creation timestamp  
» delivery_timest | integer(int64) | Order delivery timestamp  
» exercise_price | string | Strike price  
» invest_amount | string | Investment amount  
» invest_currency | string | Investment Token  
» name | string | Order name identifier  
» order_id | integer(int64) | Order ID  
» req_id | string | Request ID used for actual redemption  
» refund_service_charge | integer(int64) | Refund fee  
» settle_price | string | Settlement price  
» settlement_amount | string | Settlement amount  
» settlement_currency | string | Settlement currency  
» settlement_interest | string | Settlement interest  
» settlement_principle | string | Settlement principal  
» type | string | `call`: sell high; `put`: buy low  
» money_back_timest | integer(int64) | Redemption time  
  
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
↳ order_id | body | string | Required | Order ID  
↳ req_id | body | string | Required | Request ID returned by order-refund-preview  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Redemption successful

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
↳ order_id | body | integer(int64) | Optional | Order ID  
↳ status | body | integer(int32) | Optional | `0` — off; `1` — on  
↳ effective_time_duration | body | integer(int64) | Optional | Effective duration in seconds; default 1 day (86400)  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Updated successfully

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

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Successfully retrieved

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Successfully retrieved | [DualProjectRecommend]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | none  
» id | integer(int64) | Product ID  
» category | integer(int32) | Strategy category  
» type | string | `call`: sell high; `put`: buy low  
» invest_currency | string | Investment Token  
» exercise_currency | string | Strike Token  
» apy_display | string | Annual Yield  
» exercise_price | string | Strike price  
» delivery_timest | integer(int64) | Settlement time  
» min_amount | string | Minimum investment amount  
» max_amount | string | Maximum investment amount  
» min_copies | integer(int64) | Minimum Units  
» max_copies | integer(int64) | Maximum Units  
» invest_days | integer(int64) | Lock-up days  
» invest_hours | string | Lock-up hours  
  
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
    

##  Staking coins🔒 Authenticated

GET`/earn/staking/coins`

GET `/earn/staking/coins`

_Staking coins_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
cointype | query | string | Optional | Currency type: swap - voucher; lock - locked position; debt - US Treasury bond.  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Successfully retrieved

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Successfully retrieved | [Inline]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» pid | integer | Product ID  
» productType | integer | Project type 0-voucher 1-locked position 2-US Treasury bond  
» isDefi | integer | Is DEFI protocol 0-no 1-yes  
» currency | string | Staked currencies (multiple entries separated by commas)  
» estimateApr | string | Estimated yield rate  
» minStakeAmount | string | Minimum staked amount  
» maxStakeAmount | string | Maximum staked amount  
» protocolName | string | Protocol name  
» redeemPeriod | string | Redemption period (days)  
» exchangeRate | string | Exchange rate  
» exchangeRateReserve | string | Reverse exchange rate  
» extraInterest | array | Additional rewards  
»» start_time | string | Start timestamp  
»» end_time | string | End Timestamp  
»» reward_coin | string | Additional reward currency  
»» segment_interest | array | Tiered reward information  
»»» money_min | string | Tiered lower value  
»»» money_max | string | Tiered upper value  
»»» money_rate | string | Tiered interest rate  
»» currencyRewards | array | Reward currency information  
»»» apr | string | Base interest rate  
»»» reward_coin | string | Reward currency  
»»» reward_delay_days | string | Dividend day -1 indicates dividends are distributed upon redemption  
»»» interest_delay_days | string | Interest accrual day  
  
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
↳ coin | body | string | Required | Currency  
↳ side | body | integer | Required | 0 - Stake 1 - Redeem  
↳ amount | body | string | Required | Size  
↳ pid | body | integer | Optional | DeFi-type Mining Protocol Identifier  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Swap successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Swap successful | SwapCoinStruct  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» id | integer | Order ID  
» pid | integer | Product ID  
» uid | integer | User ID  
» coin | string | Currency  
» type | integer | Type 0-Staking 1-Redemption  
» subtype | string | SubType  
» amount | string | Amount  
» exchange_rate | string | Exchange ratio  
» exchange_amount | string | Redemption Amount  
» updateStamp | integer | UpdateTimestamp  
» createStamp | integer | Transaction timestamp  
» status | integer | status 1-success  
» protocol_type | integer | DEFI Protocol Type  
» client_order_id | string | Reference ID  
» source | string | Order Origin  
  
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

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Successfully retrieved

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Successfully retrieved | OrderListStruct  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» page | integer | Page  
» pageSize | integer | Items per page  
» pageCount | integer | Total pages  
» totalCount | integer | Total entries  
» list | array | none  
»» pid | integer | Product ID  
»» coin | string | Staked and redeemed currencies  
»» amount | string | Amount  
»» type | integer | Type 0-Staking 1-Redemption  
»» status | integer | Status  
»» redeem_stamp | integer | Redemption credit time  
»» createStamp | integer | Order time  
»» exchange_amount | string | Exchange rate  
»» fee | string | fee  
  
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

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Successfully retrieved

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Successfully retrieved | AwardListStruct  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» page | integer | Page  
» pageSize | integer | Items per page  
» pageCount | integer | Total pages  
» totalCount | integer | Total entries  
» list | array | none  
»» pid | integer | Product ID  
»» mortgage_coin | string | Collateral currency  
»» amount | string | Amount  
»» reward_coin | string | Reward currency  
»» interest | string | Interest amount  
»» fee | string | fee  
»» status | integer | Status  
»» bonus_date | string | Date  
»» should_bonus_stamp | integer | Scheduled distribution timestamp  
  
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

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Successfully retrieved

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Successfully retrieved | [Inline]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» pid | integer | Product ID  
» mortgage_coin | string | Staked currencies (multiple entries separated by commas)  
» mortgage_amount | string | Position amount  
» createStamp | integer | First timestamp  
» extra_income | string | Additional rewards converted to USDT amount  
» freeze_amount | string | Locked amount, used in trading  
» move_income | string | none  
» type | integer | Type 0-voucher 1-locked position 2-US Treasury bond  
» status | integer | Status  
» income_total | string | Total earnings by currency  
» yesterday_income_multi | array | Yesterday's earnings  
» reward_coins | array | Currency-specific reward earnings  
»» reward_coin | string | Reward currency  
»» interest_delay_days | integer | Interest accrual day  
»» reward_delay_days | integer | Dividend day -1 indicates dividends are distributed upon redemption  
» defi_income | object | DEIF earnings  
»» total | array | none  
»»» coin | string | none  
»»» amount | string | none  
  
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
↳ plan_name | body | string | Optional | Plan name。Length: 0-50 characters  
↳ plan_des | body | string | Optional | Plan description  
↳ plan_money | body | string | Required | Pricing currency，SupportUSDT，BTC  
↳ plan_amount | body | string | Required | Per PeriodAuto InvestAmount，Must > 0，and not exceedThePricing currencyConfigurationSingleMaximumAmount  
↳ plan_period_type | body | string | Required | Enum: daily, weekly, biweekly, monthly, hourly, 4-hourly  
↳ plan_period_day | body | integer(int64) | Required | Cycle day. For monthly: day of month (1-30); For weekly/biweekly: day of week (1-7, 1=Monday); For daily/hourly/4-hourly: ignored  
↳ plan_period_hour | body | integer(int64) | Required | Execution hourAuto Invest 0-23  
↳ items | body | array | Required | Investment portfolio, asset cannot be repeated; Sum of all items' ratios must be 100  
↳ asset | body | string | Required | Investment currency, e.g., BTC; Must be enabled and market exists; Cannot be repeated within the same plan  
↳ ratio | body | string | Required | The proportion of this currency in the portfolio，The sum of all items' ratios must be 100  
↳ fund_source | body | string | Optional | Fund source: spot or earn, default: spot  
↳ fund_flow | body | string | Optional | Fund flow direction: auto_invest or earn, default: auto_invest  
↳ type | body | integer(int64) | Optional | 0 Normal creation, 1 QuickInvestment  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Created successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Created successfully | AutoInvestPlanCreateResp  
  
### Response Schema

Status Code **200**

_Create auto invest planResponse_

Name | Type | Description  
---|---|---  
» id | integer(int64) | Plan ID  
» amount | string | Per PeriodAuto InvestAmount  
» money | string | Quote currency  
» next_time | integer(int64) | Next execution time  
» period_type | string | Cycle type  
» period_day | integer(int64) | Cycle day  
» period_hour | integer(int64) | CycleHours  
» fund_flow | string | Fund Flow Direction  
» fund_source | string | Fund source  
  
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
↳ plan_id | body | integer(int64) | Required | Plan ID  
↳ fund_source | body | string | Optional | Fund source Spotspot or Flexible Savingsearn，Default spot  
↳ fund_flow | body | string | Optional | Fund Flow Direction Spotauto_invest or Flexible Savingsearn，Default auto_invest  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Updated successfully

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
↳ plan_id | body | integer(int64) | Required | Plan ID  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Stopped successfully

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
↳ plan_id | body | integer(int64) | Required | Plan ID  
↳ amount | body | string | Required | Amount  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Add PositionSuccess

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

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Successfully retrieved

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Successfully retrieved | [AutoInvestCoinsItem]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | [Currency item supporting auto invest]  
» _None_ | AutoInvestCoinsItem | Currency item supporting auto invest  
»» key | string | Currency code  
»» value | string | Currency name  
»» asset_icon_url | string | Currency icon URL  
»» sort | integer(int64) | Sort  
  
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

Get `minimum investment amount`

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | AutoInvestMinInvestAmount | Required | none  
↳ money | body | string | Required | Currency, optional: USDT or BTC  
↳ items | body | array | Required | none  
↳ asset | body | string | Required | Currency  
↳ ratio | body | string | Required | Ratio，e.g.100  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Successfully retrieved

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Successfully retrieved | AutoInvestMinInvestAmountResp  
  
### Response Schema

Status Code **200**

_AvailableInvestmentMinimumAmountResponse_

Name | Type | Description  
---|---|---  
» min_amount | string | MinimumAmount  
  
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
    body='{"money":"USDT","items":[{"asset":"BTC","ratio":"33"},{"asset":"ETH","ratio":"33"},{"asset":"SOL","ratio":"34"}]}'
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
    body_param='{"money":"USDT","items":[{"asset":"BTC","ratio":"33"},{"asset":"ETH","ratio":"33"},{"asset":"SOL","ratio":"34"}]}'
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

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Successfully retrieved

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Successfully retrieved | AutoInvestPlanRecordsResp  
  
### Response Schema

Status Code **200**

_PlanExecutionRecordPaginatedResponse_

Name | Type | Description  
---|---|---  
» page | integer(int64) | page number  
» page_size | integer(int64) | Items per page  
» total_page | integer(int64) | TotalPage number  
» total | integer(int64) | Total entries  
» list | array | none  
»» _None_ | object | Plan execution record item  
»»» id | integer(int64) | Record ID  
»»» type | string | type  
»»» money | string | SourceCurrency  
»»» user_id | integer(int64) | User ID  
»»» plan_id | integer(int64) | Plan ID  
»»» plan_version | integer(int64) | PlanVersion  
»»» amount | string | Investment amount  
»»» create_time | integer(int64) | Investment time  
»»» update_time | integer(int64) | Update time  
»»» status | string | Status  
»»» status_type | integer(int64) | Status enum  
»»» side | integer(int64) | 2 = Buy, Other = Sell  
»»» status_message | string | Status description  
»»» detail | string | Details  
»»» asset | string | Currency  
  
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

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Successfully retrieved

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Successfully retrieved | [AutoInvestOrderItem]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | [Auto invest order item]  
» _None_ | AutoInvestOrderItem | Auto invest order item  
»» id | integer(int64) | Order ID  
»» type | string | type  
»» amount | string | Size  
»» plan_id | integer(int64) | Plan ID  
»» side | integer(int64) | direction  
»» asset | string | Currency  
»» record_id | integer(int64) | Record ID  
»» total_money | string | TotalAmount  
»» market | string | Currency pair  
»» price | string | Price  
»» create_time | integer(int64) | Creation time (Unix timestamp)  
»» total | string | Total  
»» fund_flow | string | Fund Flow Direction  
»» error_code | integer(int64) | Error code  
»» error_msg | string | Error message  
»» status | integer(int64) | Status  
  
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

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Successfully retrieved

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Successfully retrieved | [AutoInvestConfigItem]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | [Investment currency configuration item]  
» _None_ | AutoInvestConfigItem | Investment currency configuration item  
»» coin | string | Currency  
»» max_limit | string | InvestmentLimit  
  
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

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Successfully retrieved

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Successfully retrieved | AutoInvestPlanDetail  
  
### Response Schema

Status Code **200**

_Auto invest planDetails_

Name | Type | Description  
---|---|---  
» id | integer(int64) | Plan ID  
» version | integer(int64) | PlanVersion  
» name | string | Plan name  
» create_time | integer(int64) | Creation time (Unix timestamp)  
» update_time | integer(int64) | Update time (Unix timestamp)  
» user_id | integer(int64) | User ID  
» money | string | Quote Currency  
» amount | string | Per PeriodInvestment amount  
» period_type | string | Cycle type（e.g., monthly）  
» period_day | integer(int64) | Cycle day  
» period_hour | integer(int64) | CycleHours  
» portfolio | array | InvestmentPortfolio  
»» _None_ | AutoInvestPlanDetail/properties/portfolio/items | Auto invest plan portfolio item  
»»» asset | string | Currency  
»»» ratio | string | Ratio  
»»» cum_invest | string | Accumulated investment  
»»» cum_hold | string | AccumulatedPosition  
»»» cum_redeem | string | Accumulated redemption  
»»» avg_price | string | Average Cost Price  
»»» redeem_status | integer(int64) | Redemption status  
»»» lend_amount | string | LendingQuantity  
»» next_time | integer(int64) | Next execution time (Unix timestamp)  
»» period | integer(int64) | Executed periods  
»» fund_source | string | Fund source（spot/earn）  
»» fund_flow | string | Fund flow direction (auto_invest/earn)  
  
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

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Successfully retrieved

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Successfully retrieved | AutoInvestPlanListInfoResp  
  
### Response Schema

Status Code **200**

_Auto invest planListPaginatedResponse_

Name | Type | Description  
---|---|---  
» page | integer(int64) | page number  
» page_size | integer(int64) | Items per page  
» page_count | integer(int64) | Total pages  
» total_count | integer(int64) | Total entries  
» list | array | PlanList  
»» _None_ | object | Auto invest planDetails  
»»» id | integer(int64) | Plan ID  
»»» version | integer(int64) | PlanVersion  
»»» name | string | Plan name  
»»» create_time | integer(int64) | Creation time (Unix timestamp)  
»»» update_time | integer(int64) | Update time (Unix timestamp)  
»»» user_id | integer(int64) | User ID  
»»» money | string | Quote Currency  
»»» amount | string | Per PeriodInvestment amount  
»»» period_type | string | Cycle type（e.g., monthly）  
»»» period_day | integer(int64) | Cycle day  
»»» period_hour | integer(int64) | CycleHours  
»»» portfolio | array | InvestmentPortfolio  
»»»» _None_ | AutoInvestPlanDetail/properties/portfolio/items | Auto invest plan portfolio item  
»»»»» asset | string | Currency  
»»»»» ratio | string | Ratio  
»»»»» cum_invest | string | Accumulated investment  
»»»»» cum_hold | string | AccumulatedPosition  
»»»»» cum_redeem | string | Accumulated redemption  
»»»»» avg_price | string | Average Cost Price  
»»»»» redeem_status | integer(int64) | Redemption status  
»»»»» lend_amount | string | LendingQuantity  
»»»» next_time | integer(int64) | Next execution time (Unix timestamp)  
»»»» period | integer(int64) | Executed periods  
»»»» fund_source | string | Fund source（spot/earn）  
»»»» fund_flow | string | Fund flow direction (auto_invest/earn)  
  
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

Get `product list`

Query fixed-term earn product list. Supports filtering by currency, product type, status, etc. Returns product interest rate, lock-up period, quota, and reward campaign information

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
asset | query | string | Optional | Currency  
type | query | integer | Optional | Product type: 1 for regular, 2 for VIP  
page | query | integer | Required | Page number  
limit | query | integer | Required | Page size  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Product list retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Product list retrieved successfully | ListEarnFixedTermProductsResponse  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» code | integer | Return code, 0 means success  
» message | string | Response message  
» data | object | Product list data  
»» list | array | Product list  
»»» _None_ | FixedTermProduct | Fixed-term earn product  
»»»» id | integer | Product ID  
»»»» name | string | Product name  
»»»» asset | string | Currency  
»»»» lock_up_period | integer | Lock-up period (in days)  
»»»» min_lend_amount | string | Minimum earn amount  
»»»» user_max_lend_amount | string | User maximum earn limit  
»»»» total_lend_amount | string | Platform earn limit  
»»»» year_rate | string | Annual interest rate  
»»»» type | integer | Product type: 1 for regular, 2 for VIP  
»»»» pre_redeem | integer | Whether early redemption is supported: 0 for not supported, 1 for supported  
»»»» reinvest | integer | Whether auto-renewal is supported: 0 for not supported, 1 for supported  
»»»» redeem_account | integer | Whether fixed-to-flexible conversion is supported: 0 for not supported, 1 for supported  
»»»» min_vip | integer | Minimum VIP level requirement, 0-16, 0 means no restriction  
»»»» max_vip | integer | Maximum VIP level requirement (0-16), 0 means no restriction  
»»»» status | integer | Product status: 1 for unlisted, 2 for listed, 3 for delisted  
»»»» create_time | string | Created time  
»»»» user_max_lend_volume | string | User maximum earn amount  
»»»» user_total_amount | string | Total amount the user has invested in earn products  
»»»» sale_status | integer | Sale status: 1 for on sale, 2 for sold out  
»»» total | integer | Total Records  
»» timestamp | integer | Response timestamp (in seconds)  
  
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

Get `product list by single currency`

Sort by product term in ascending order

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
asset | path | string | Required | Currency name, e.g., USDT, BTC  
type | query | string | Optional | Product type: "" or 1 for regular product list, 2 for VIP product list, 0 for all products  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Single currency product list retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Single currency product list retrieved successfully | ListEarnFixedTermProductsByAssetResponse  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» code | integer | Return code, 0 means success  
» message | string | Response message  
» data | object | Product list data  
»» list | array | Product list  
»»» _None_ | FixedTermProductSimple | Fixed-term earn product (compact)  
»»»» id | integer | Product ID  
»»»» asset | string | Currency  
»»»» lock_up_period | integer | Lock-up period (in days)  
»»»» year_rate | string | Annual interest rate  
»»»» type | integer | Product type: 1 for regular, 2 for VIP  
»»»» pre_redeem | integer | Whether early redemption is supported: 0 for not supported, 1 for supported  
»»»» reinvest | integer | Whether auto-renewal is supported: 0 for not supported, 1 for supported  
»»»» simple_earn | integer | Whether fixed-to-flexible conversion is supported: 0 for not supported, 1 for supported  
»»»» min_vip | integer | Minimum VIP level requirement, 0 means no restriction  
»»»» max_vip | integer | Maximum VIP level requirement, 0 means no restriction  
»»»» sale_status | integer | Sale status: 1 for on sale, 2 for sold out  
»»» timestamp | integer | Response timestamp (in seconds)  
  
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

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Subscription order list retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Subscription order list retrieved successfully | ListEarnFixedTermLendsResponse  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» code | integer | Return code, 0 means success  
» message | string | Response message  
» data | object | Subscription order list data  
»» list | array | Subscription order list  
»»» _None_ | FixedTermLendOrder | Fixed-term earn subscription order  
»»»» id | integer | Subscription record ID  
»»»» business | integer | Business type: 1 for regular, 2 for VIP  
»»»» order_id | integer(int64) | Order ID  
»»»» user_id | integer(int64) | User ID  
»»»» asset | string | Currency  
»»»» product_id | integer | Product ID  
»»»» lock_up_period | integer | Lock-up period (in days)  
»»»» principal | string | Subscription principal  
»»»» year_rate | string | Annual interest rate  
»»»» product_type | integer | Product type: 1 for regular, 2 for VIP  
»»»» interest | string | Accrued interest  
»»»» status | integer | Order status: 1 for holding, 2 for redeemed, 3 for matured, 4 for settled  
»»»» reinvest_status | integer | Auto-renewal status: 0 for disabled, 1 for enabled  
»»»» redeem_account_type | integer | Redemption payout account type: 1 for spot account  
»»»» origin_order | string | Original order ID, linked to previous order IDs in auto-renewal scenarios  
»»»» redeem_type | integer | Redemption type: 1 for early redemption, 2 for maturity redemption  
»»»» redeem_time | string | Redemption time  
»»»» finish_time | string | Expiration time  
»»»» create_time | string | Created time  
»»»» year_rate_perent | string | Annual interest rate percentage display value  
»»»» total_year_rate_percent | string | Comprehensive annualized yield percentage (including interest rate boost, rewards, etc.)  
»»»» total_interest | string | Total earnings (including interest and bonus rewards)  
»»»» product_info | FixedTermProductInfo | Product configuration  
»»»»» pre_redeem | integer | Whether early redemption is supported: 0 for not supported, 1 for supported  
»»»»» reinvest | integer | Whether auto-renewal is supported: 0 for not supported, 1 for supported  
»»»»» redeem_account | integer | Redemption payout account type  
»»»»» min_vip | integer | Minimum VIP level requirement, 0 means no restriction  
»»»»» max_vip | integer | Maximum VIP level requirement, 0 means no restriction  
»»»» bonus_info | FixedTermBonusInfo | Bonus reward campaign information  
»»»»» id | integer | Activity ID  
»»»»» product_id | integer | Associated product ID  
»»»»» asset | string | Product currency  
»»»»» bonus_asset | string | Reward currency  
»»»»» kyc_limit | string | KYC level restrictions, comma-separated  
»»»»» ladder_apr | array | Tiered annual interest rate  
»»»»»» apr | string | Annualized interest rate  
»»»»»» left | string | Range lower limit  
»»»»»» right | string | Range upper limit  
»»»»» total_bonus_amount | string | Total reward amount  
»»»»» user_total_bonus_amount | string | Maximum reward per user  
»»»»» status | integer | Activity status: 1 for unlisted, 2 for listed, 3 for delisted  
»»»»» start_time | string | Activity start time  
»»»»» end_time | string | Activity end time  
»»»»» create_time | string | Created time  
»»»»» start_at | integer | Activity start timestamp (in seconds)  
»»»»» end_at | integer | Activity end timestamp (in seconds)  
»»»»» total_issued_amount | string | Total rewards distributed  
»»»»» user_total_issued_amount | string | Total rewards distributed to the user  
»»»»» bonus_asset_price | string | Reward currency price (denominated in USDT)  
»»»»» product_asset_price | string | Product currency price (denominated in USDT)  
»»»»» product_year_rate | string | Product base annual interest rate  
»»»» coupon_info | FixedTermCouponInfo | Interest rate boost coupon information  
»»»»» id | integer | Interest rate boost coupon record ID  
»»»»» business | integer | Business Type  
»»»»» user_id | integer(int64) | User ID  
»»»»» asset | string | Currency  
»»»»» order_id | integer(int64) | Associated order ID  
»»»»» financial_rate_id | integer | Interest rate boost coupon ID  
»»»»» buy_limit_low | string | Minimum subscription amount for interest rate boost coupon  
»»»»» buy_limit_high | string | Maximum subscription amount for interest rate boost coupon  
»»»»» rate_day | integer | Interest rate boost days  
»»»»» rate_ratio | string | Interest rate boost percentage  
»»»»» coupon_days | integer | Actual interest rate boost days  
»»»»» coupon_principal | string | Principal for interest rate boost calculation  
»»»»» coupon_year_rate | string | Interest rate boost APR  
»»»»» coupon_interest | string | Interest generated from rate boost  
»»»»» status | integer | Status: 1 for active, 2 for settled  
»»»»» finish_time | string | Settlement time  
»»»»» create_time | string | Created time  
»»»» redeem_at | integer | Redemption timestamp (in seconds)  
»»»» finish_at | integer | Expiration timestamp (in seconds)  
»»»» create_at | integer | Creation timestamp (in seconds)  
»»»» icon | string | Currency icon URL  
»»» total | integer | Total Records  
»» timestamp | integer | Response timestamp (in seconds)  
  
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

Subscribe `to a fixed-term earn product by specifying the product ID and subscription amount. Optionally enable auto-renewal and apply an interest rate boost coupon`

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | FixedTermLendRequest | Optional | none  
↳ product_id | body | integer | Required | Product ID  
↳ amount | body | string | Required | Subscription amount  
↳ year_rate | body | string | Optional | Annual interest rate  
↳ reinvest_status | body | integer | Optional | Auto-renewal status: 0 for disabled, 1 for enabled  
↳ redeem_account_type | body | integer | Optional | Redemption payout account type: 1 for spot account  
↳ financial_rate_id | body | integer | Optional | Interest rate boost coupon ID, 0 means not used  
↳ sub_business | body | integer | Optional | Sub-business type  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Subscription successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Subscription successful | CreateEarnFixedTermLendResponse  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» code | integer | Return code, 0 means success  
» message | string | Response message  
» data | object | Subscription result  
»» order_id | integer(int64) | Subscription order ID  
» timestamp | integer | Response timestamp (in seconds)  
  
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
↳ order_id | body | string | Required | Order ID  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Redemption successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Redemption successful | CreateEarnFixedTermPreRedeemResponse  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» code | integer | Return code, 0 means success  
» message | string | Response message  
» data | object | Redemption result (empty object on success)  
» timestamp | integer | Response timestamp (in seconds)  
  
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

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)History records retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | History records retrieved successfully | ListEarnFixedTermHistoryResponse  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» code | integer | Return code, 0 means success  
» message | string | Response message  
» data | object | none  
»» list | array | [Fixed-term earn history records]  
»»» _None_ | FixedTermHistoryRecord | Fixed-term earn history records  
»»»» id | integer | Record ID  
»»»» order_id | integer(int64) | Order ID  
»»»» user_id | integer(int64) | User ID  
»»»» asset | string | Currency  
»»»» uniq_time | string | Unique time identifier (date)  
»»»» bonus_id | integer | Reward campaign ID  
»»»» product_id | integer | Product ID  
»»»» bonus_asset | string | Reward currency  
»»»» total_principal | string | Total principal  
»»»» amount | string | Amount  
»»»» asset_price | string | Currency price  
»»»» status | integer | Status  
»»»» detail | string | Detail description  
»»»» create_time | string | Created time  
»»»» create_at | integer | Creation timestamp (in seconds)  
»»»» lock_up_period | integer | Term  
»»» total | integer | Total Records  
»» timestamp | integer | Response timestamp (in seconds)  
  
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

##  PlaceDualInvestmentOrder

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
id | integer(int32) | Optional | none | Order ID  
plan_id | integer(int32) | Optional | none | Product ID  
invest_amount | string | Optional | none | Investment Quantity  
settlement_amount | string | Optional | none | Settlement Quantity  
create_time | integer(int32) | Optional | none | Created time  
complete_time | integer(int32) | Optional | none | Completed Time  
status | string | Optional | none | Status:  
  
`INIT`-Created  
`SETTLEMENT_SUCCESS`-Settlement Success  
`SETTLEMENT_PROCESSING`-Settlement Processing  
`CANCELED`-Canceled  
`FAILED`-Failed  
invest_currency | string | Optional | none | Investment Token  
exercise_currency | string | Optional | none | Strike Token  
exercise_price | string | Optional | none | Strike price  
settlement_price | string | Optional | none | Settlement price  
settlement_currency | string | Optional | none | Settlement currency  
apy_display | string | Optional | none | Annual Yield  
apy_settlement | string | Optional | none | Settlement Annual Yield  
delivery_time | integer(int32) | Optional | none | Settlement time  
text | string | Optional | none | Custom order information  
      
    
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

_PlanExecutionRecordPaginatedResponse_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
page | integer(int64) | Required | none | page number  
page_size | integer(int64) | Required | none | Items per page  
total_page | integer(int64) | Required | none | TotalPage number  
total | integer(int64) | Required | none | Total entries  
list | array | Required | none | none  
↳ None | object | Optional | none | Plan execution record item  
↳ id | integer(int64) | Required | none | Record ID  
↳ type | string | Required | none | type  
↳ money | string | Required | none | SourceCurrency  
↳ user_id | integer(int64) | Required | none | User ID  
↳ plan_id | integer(int64) | Required | none | Plan ID  
↳ plan_version | integer(int64) | Required | none | PlanVersion  
↳ amount | string | Required | none | Investment amount  
↳ create_time | integer(int64) | Required | none | Investment time  
↳ update_time | integer(int64) | Required | none | Update time  
↳ status | string | Required | none | Status  
↳ status_type | integer(int64) | Required | none | Status enum  
↳ side | integer(int64) | Required | none | 2 = Buy, Other = Sell  
↳ status_message | string | Required | none | Status description  
↳ detail | string | Optional | none | Details  
↳ asset | string | Optional | none | Currency  
      
    
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
    
    

##  AssetListStruct

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
pid | integer | Required | none | Product ID  
mortgage_coin | string | Required | none | Staked currencies (multiple entries separated by commas)  
mortgage_amount | string | Required | none | Position amount  
createStamp | integer | Required | none | First timestamp  
extra_income | string | Required | none | Additional rewards converted to USDT amount  
freeze_amount | string | Required | none | Locked amount, used in trading  
move_income | string | Required | none | none  
type | integer | Required | none | Type 0-voucher 1-locked position 2-US Treasury bond  
status | integer | Required | none | Status  
income_total | string | Required | none | Total earnings by currency  
yesterday_income_multi | array | Required | none | Yesterday's earnings  
reward_coins | array | Required | none | Currency-specific reward earnings  
↳ reward_coin | string | Required | none | Reward currency  
↳ interest_delay_days | integer | Required | none | Interest accrual day  
↳ reward_delay_days | integer | Required | none | Dividend day -1 indicates dividends are distributed upon redemption  
defi_income | object | Required | none | DEIF earnings  
↳ total | array | Required | none | none  
↳ coin | string | Required | none | none  
↳ amount | string | Required | none | none  
      
    
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
    
    

##  FixedTermLendRequest

_Subscription request_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
product_id | integer | Required | none | Product ID  
amount | string | Required | none | Subscription amount  
year_rate | string | Optional | none | Annual interest rate  
reinvest_status | integer | Optional | none | Auto-renewal status: 0 for disabled, 1 for enabled  
redeem_account_type | integer | Optional | none | Redemption payout account type: 1 for spot account  
financial_rate_id | integer | Optional | none | Interest rate boost coupon ID, 0 means not used  
sub_business | integer | Optional | none | Sub-business type  
      
    
    {
      "product_id": 0,
      "amount": "string",
      "year_rate": "string",
      "reinvest_status": 0,
      "redeem_account_type": 0,
      "financial_rate_id": 0,
      "sub_business": 0
    }
    
    

##  AwardListStruct

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
page | integer | Required | none | Page  
pageSize | integer | Required | none | Items per page  
pageCount | integer | Required | none | Total pages  
totalCount | integer | Required | none | Total entries  
list | array | Required | none | none  
↳ pid | integer | Required | none | Product ID  
↳ mortgage_coin | string | Required | none | Collateral currency  
↳ amount | string | Required | none | Amount  
↳ reward_coin | string | Required | none | Reward currency  
↳ interest | string | Required | none | Interest amount  
↳ fee | string | Required | none | fee  
↳ status | integer | Required | none | Status  
↳ bonus_date | string | Required | none | Date  
↳ should_bonus_stamp | integer | Required | none | Scheduled distribution timestamp  
      
    
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
    
    

##  DualProjectRecommend

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
id | integer(int64) | Optional | none | Product ID  
category | integer(int32) | Optional | none | Strategy category  
type | string | Optional | none | `call`: sell high; `put`: buy low  
invest_currency | string | Optional | none | Investment Token  
exercise_currency | string | Optional | none | Strike Token  
apy_display | string | Optional | none | Annual Yield  
exercise_price | string | Optional | none | Strike price  
delivery_timest | integer(int64) | Optional | none | Settlement time  
min_amount | string | Optional | none | Minimum investment amount  
max_amount | string | Optional | none | Maximum investment amount  
min_copies | integer(int64) | Optional | none | Minimum Units  
max_copies | integer(int64) | Optional | none | Maximum Units  
invest_days | integer(int64) | Optional | none | Lock-up days  
invest_hours | string | Optional | none | Lock-up hours  
      
    
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
    
    

##  DualGetOrders

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
id | integer(int32) | Optional | none | Order ID  
plan_id | integer(int32) | Optional | none | Product ID  
invest_amount | string | Optional | none | Investment Quantity  
settlement_amount | string | Optional | none | Settlement Quantity  
create_time | integer(int32) | Optional | none | Created time  
complete_time | integer(int32) | Optional | none | Completed Time  
status | string | Optional | none | Status:  
  
`INIT`-Created  
`SETTLEMENT_SUCCESS`-Settlement Success  
`SETTLEMENT_PROCESSING`-Settlement Processing  
`CANCELED`-Canceled  
`FAILED`-Failed  
invest_currency | string | Optional | none | Investment Token  
exercise_currency | string | Optional | none | Strike Token  
exercise_price | string | Optional | none | Strike price  
settlement_price | string | Optional | none | Settlement price  
settlement_currency | string | Optional | none | Settlement currency  
apy_display | string | Optional | none | Annual Yield  
apy_settlement | string | Optional | none | Settlement Annual Yield  
delivery_time | integer(int32) | Optional | none | Settlement time  
text | string | Optional | none | Custom order information  
      
    
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
    
    

##  AutoInvestPlanAddPosition

_Add position immediatelyRequest_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
plan_id | integer(int64) | Required | none | Plan ID  
amount | string | Required | none | Amount  
      
    
    {
      "plan_id": 0,
      "amount": "string"
    }
    
    

##  CreateEarnFixedTermLendResponse

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
code | integer | Optional | none | Return code, 0 means success  
message | string | Optional | none | Response message  
data | object | Optional | none | Subscription result  
↳ order_id | integer(int64) | Optional | none | Subscription order ID  
timestamp | integer | Optional | none | Response timestamp (in seconds)  
      
    
    {
      "code": 0,
      "message": "string",
      "data": {
        "order_id": 0
      },
      "timestamp": 0
    }
    
    

##  FindCoinStruct

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
pid | integer | Required | none | Product ID  
productType | integer | Required | none | Project type 0-voucher 1-locked position 2-US Treasury bond  
isDefi | integer | Required | none | Is DEFI protocol 0-no 1-yes  
currency | string | Required | none | Staked currencies (multiple entries separated by commas)  
estimateApr | string | Required | none | Estimated yield rate  
minStakeAmount | string | Required | none | Minimum staked amount  
maxStakeAmount | string | Required | none | Maximum staked amount  
protocolName | string | Required | none | Protocol name  
redeemPeriod | string | Required | none | Redemption period (days)  
exchangeRate | string | Required | none | Exchange rate  
exchangeRateReserve | string | Required | none | Reverse exchange rate  
extraInterest | array | Optional | none | Additional rewards  
↳ start_time | string | Required | none | Start timestamp  
↳ end_time | string | Required | none | End Timestamp  
↳ reward_coin | string | Required | none | Additional reward currency  
↳ segment_interest | array | Required | none | Tiered reward information  
↳ money_min | string | Required | none | Tiered lower value  
↳ money_max | string | Required | none | Tiered upper value  
↳ money_rate | string | Required | none | Tiered interest rate  
↳ currencyRewards | array | Required | none | Reward currency information  
↳ apr | string | Required | none | Base interest rate  
↳ reward_coin | string | Required | none | Reward currency  
↳ reward_delay_days | string | Required | none | Dividend day -1 indicates dividends are distributed upon redemption  
↳ interest_delay_days | string | Required | none | Interest accrual day  
      
    
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
    
    

##  AutoInvestPlanListInfoResp

_Auto invest planListPaginatedResponse_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
page | integer(int64) | Required | none | page number  
page_size | integer(int64) | Required | none | Items per page  
page_count | integer(int64) | Required | none | Total pages  
total_count | integer(int64) | Required | none | Total entries  
list | array | Required | none | PlanList  
↳ None | object | Optional | none | Auto invest planDetails  
↳ id | integer(int64) | Required | none | Plan ID  
↳ version | integer(int64) | Optional | none | PlanVersion  
↳ name | string | Required | none | Plan name  
↳ create_time | integer(int64) | Required | none | Creation time (Unix timestamp)  
↳ update_time | integer(int64) | Required | none | Update time (Unix timestamp)  
↳ user_id | integer(int64) | Required | none | User ID  
↳ money | string | Required | none | Quote Currency  
↳ amount | string | Required | none | Per PeriodInvestment amount  
↳ period_type | string | Required | none | Cycle type（e.g., monthly）  
↳ period_day | integer(int64) | Required | none | Cycle day  
↳ period_hour | integer(int64) | Required | none | CycleHours  
↳ portfolio | [AutoInvestPlanDetail/properties/portfolio/items] | Required | none | InvestmentPortfolio  
↳ next_time | integer(int64) | Required | none | Next execution time (Unix timestamp)  
↳ period | integer(int64) | Required | none | Executed periods  
↳ fund_source | string | Required | none | Fund source（spot/earn）  
↳ fund_flow | string | Required | none | Fund flow direction (auto_invest/earn)  
      
    
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
    
    

##  EarnFixedTermPreRedeemRequest

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
order_id | string | Required | none | Order ID  
      
    
    {
      "order_id": "5862476630"
    }
    
    

##  SwapCoin

_Blockchain Mining_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
coin | string | Required | none | Currency  
side | integer | Required | none | 0 - Stake 1 - Redeem  
amount | string | Required | none | Size  
pid | integer | Optional | none | DeFi-type Mining Protocol Identifier  
      
    
    {
      "coin": "string",
      "side": 0,
      "amount": "string",
      "pid": 0
    }
    
    

##  DualGetBalance

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
user_asset_usdt | string | Optional | none | User Assets in USDT Equivalent  
user_asset_btc | string | Optional | none | User Assets in BTC Equivalent  
user_total_interest_usdt | string | Optional | none | Total User Interest in USDT Equivalent  
user_total_interest_btc | string | Optional | none | Total User Interest in BTC Equivalent  
      
    
    {
      "user_asset_usdt": "string",
      "user_asset_btc": "string",
      "user_total_interest_usdt": "string",
      "user_total_interest_btc": "string"
    }
    
    

##  ListEarnFixedTermHistoryResponse

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
code | integer | Optional | none | Return code, 0 means success  
message | string | Optional | none | Response message  
data | object | Optional | none | none  
↳ list | [FixedTermHistoryRecord] | Optional | none | [Fixed-term earn history records]  
↳ total | integer | Optional | none | Total Records  
timestamp | integer | Optional | none | Response timestamp (in seconds)  
      
    
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
    
    

##  DualModifyOrderReinvestParams

_Dual-currency order reinvest modification request_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
order_id | integer(int64) | Optional | none | Order ID  
status | integer(int32) | Optional | none | `0` — off; `1` — on  
effective_time_duration | integer(int64) | Optional | none | Effective duration in seconds; default 1 day (86400)  
      
    
    {
      "order_id": 0,
      "status": 0,
      "effective_time_duration": 0
    }
    
    

##  ListEarnFixedTermProductsByAssetResponse

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
code | integer | Required | none | Return code, 0 means success  
message | string | Required | none | Response message  
data | object | Required | none | Product list data  
↳ list | [FixedTermProductSimple] | Required | none | Product list  
timestamp | integer | Required | none | Response timestamp (in seconds)  
      
    
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
    
    

##  ListEarnFixedTermLendsResponse

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
code | integer | Required | none | Return code, 0 means success  
message | string | Required | none | Response message  
data | object | Required | none | Subscription order list data  
↳ list | [FixedTermLendOrder] | Required | none | Subscription order list  
↳ total | integer | Required | none | Total Records  
timestamp | integer | Required | none | Response timestamp (in seconds)  
      
    
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

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
create_timest | integer(int64) | Optional | none | Order creation timestamp  
delivery_timest | integer(int64) | Optional | none | Order delivery timestamp  
exercise_price | string | Optional | none | Strike price  
invest_amount | string | Optional | none | Investment amount  
invest_currency | string | Optional | none | Investment Token  
name | string | Optional | none | Order name identifier  
order_id | integer(int64) | Optional | none | Order ID  
req_id | string | Optional | none | Request ID used for actual redemption  
refund_service_charge | integer(int64) | Optional | none | Refund fee  
settle_price | string | Optional | none | Settlement price  
settlement_amount | string | Optional | none | Settlement amount  
settlement_currency | string | Optional | none | Settlement currency  
settlement_interest | string | Optional | none | Settlement interest  
settlement_principle | string | Optional | none | Settlement principal  
type | string | Optional | none | `call`: sell high; `put`: buy low  
money_back_timest | integer(int64) | Optional | none | Redemption time  
      
    
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
    
    

##  FixedTermHistoryRecord

_Fixed-term earn history records_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
id | integer | Required | none | Record ID  
order_id | integer(int64) | Optional | none | Order ID  
user_id | integer(int64) | Required | none | User ID  
asset | string | Required | none | Currency  
uniq_time | string | Optional | none | Unique time identifier (date)  
bonus_id | integer | Optional | none | Reward campaign ID  
product_id | integer | Required | none | Product ID  
bonus_asset | string | Optional | none | Reward currency  
total_principal | string | Optional | none | Total principal  
amount | string | Optional | none | Amount  
asset_price | string | Optional | none | Currency price  
status | integer | Required | none | Status  
detail | string | Optional | none | Detail description  
create_time | string | Required | none | Created time  
create_at | integer | Required | none | Creation timestamp (in seconds)  
lock_up_period | integer | Optional | none | Term  
      
    
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
    
    

##  AutoInvestMinInvestAmountResp

_AvailableInvestmentMinimumAmountResponse_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
min_amount | string | Required | none | MinimumAmount  
      
    
    {
      "min_amount": "string"
    }
    
    

##  AutoInvestPlanCreate

_Create auto invest planRequest_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
plan_name | string | Optional | none | Plan name。Length: 0-50 characters  
plan_des | string | Optional | none | Plan description  
plan_money | string | Required | none | Pricing currency，SupportUSDT，BTC  
plan_amount | string | Required | none | Per PeriodAuto InvestAmount，Must > 0，and not exceedThePricing currencyConfigurationSingleMaximumAmount  
plan_period_type | string | Required | none | Enum: daily, weekly, biweekly, monthly, hourly, 4-hourly  
plan_period_day | integer(int64) | Required | none | Cycle day. For monthly: day of month (1-30); For weekly/biweekly: day of week (1-7, 1=Monday); For daily/hourly/4-hourly: ignored  
plan_period_hour | integer(int64) | Required | none | Execution hourAuto Invest 0-23  
items | array | Required | none | Investment portfolio, asset cannot be repeated; Sum of all items' ratios must be 100  
↳ asset | string | Required | none | Investment currency, e.g., BTC; Must be enabled and market exists; Cannot be repeated within the same plan  
↳ ratio | string | Required | none | The proportion of this currency in the portfolio，The sum of all items' ratios must be 100  
fund_source | string | Optional | none | Fund source: spot or earn, default: spot  
fund_flow | string | Optional | none | Fund flow direction: auto_invest or earn, default: auto_invest  
type | integer(int64) | Optional | none | 0 Normal creation, 1 QuickInvestment  
      
    
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
    
    

##  ListEarnFixedTermProductsResponse

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
code | integer | Required | none | Return code, 0 means success  
message | string | Required | none | Response message  
data | object | Required | none | Product list data  
↳ list | [FixedTermProduct] | Required | none | Product list  
↳ total | integer | Required | none | Total Records  
timestamp | integer | Required | none | Response timestamp (in seconds)  
      
    
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
    
    

##  AutoInvestPlanCreateResp

_Create auto invest planResponse_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
id | integer(int64) | Required | none | Plan ID  
amount | string | Optional | none | Per PeriodAuto InvestAmount  
money | string | Optional | none | Quote currency  
next_time | integer(int64) | Optional | none | Next execution time  
period_type | string | Optional | none | Cycle type  
period_day | integer(int64) | Optional | none | Cycle day  
period_hour | integer(int64) | Optional | none | CycleHours  
fund_flow | string | Optional | none | Fund Flow Direction  
fund_source | string | Optional | none | Fund source  
      
    
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
    
    

##  FixedTermLendOrder

_Fixed-term earn subscription order_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
id | integer | Optional | none | Subscription record ID  
business | integer | Optional | none | Business type: 1 for regular, 2 for VIP  
order_id | integer(int64) | Optional | none | Order ID  
user_id | integer(int64) | Optional | none | User ID  
asset | string | Optional | none | Currency  
product_id | integer | Optional | none | Product ID  
lock_up_period | integer | Optional | none | Lock-up period (in days)  
principal | string | Optional | none | Subscription principal  
year_rate | string | Optional | none | Annual interest rate  
product_type | integer | Optional | none | Product type: 1 for regular, 2 for VIP  
interest | string | Optional | none | Accrued interest  
status | integer | Optional | none | Order status: 1 for holding, 2 for redeemed, 3 for matured, 4 for settled  
reinvest_status | integer | Optional | none | Auto-renewal status: 0 for disabled, 1 for enabled  
redeem_account_type | integer | Optional | none | Redemption payout account type: 1 for spot account  
origin_order | string | Optional | none | Original order ID, linked to previous order IDs in auto-renewal scenarios  
redeem_type | integer | Optional | none | Redemption type: 1 for early redemption, 2 for maturity redemption  
redeem_time | string | Optional | none | Redemption time  
finish_time | string | Optional | none | Expiration time  
create_time | string | Optional | none | Created time  
year_rate_perent | string | Optional | none | Annual interest rate percentage display value  
total_year_rate_percent | string | Optional | none | Comprehensive annualized yield percentage (including interest rate boost, rewards, etc.)  
total_interest | string | Optional | none | Total earnings (including interest and bonus rewards)  
product_info | FixedTermProductInfo | Optional | none | Product configuration  
bonus_info | FixedTermBonusInfo | Optional | none | Bonus reward campaign information  
coupon_info | FixedTermCouponInfo | Optional | none | Interest rate boost coupon information  
redeem_at | integer | Optional | none | Redemption timestamp (in seconds)  
finish_at | integer | Optional | none | Expiration timestamp (in seconds)  
create_at | integer | Optional | none | Creation timestamp (in seconds)  
icon | string | Optional | none | Currency icon URL  
      
    
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
    
    

##  DualGetPlans

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
id | integer(int32) | Optional | none | Product ID  
instrument_name | string | Optional | none | Product Name  
invest_currency | string | Optional | none | Investment Token  
exercise_currency | string | Optional | none | Strike Token  
exercise_price | number(double) | Optional | none | Strike price  
delivery_time | integer(int32) | Optional | none | Settlement time  
apy_display | string | Optional | none | Annual Yield  
min_amount | string | Optional | none | Minimum investment amount  
start_time | integer(int32) | Optional | none | Start Time  
end_time | integer(int32) | Optional | none | End time  
status | string | Optional | none | Status:  
  
`NOTSTARTED` \- Not started  
`ONGOING` \- In progress  
`ENDED` \- Ended  
      
    
    {
      "id": 0,
      "instrument_name": "string",
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
    
    

##  AutoInvestPlanUpdate

_Update auto invest plan request_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
plan_id | integer(int64) | Required | none | Plan ID  
fund_source | string | Optional | none | Fund source Spotspot or Flexible Savingsearn，Default spot  
fund_flow | string | Optional | none | Fund Flow Direction Spotauto_invest or Flexible Savingsearn，Default auto_invest  
      
    
    {
      "plan_id": 0,
      "fund_source": "string",
      "fund_flow": "string"
    }
    
    

##  AutoInvestMinInvestAmount

_QueryAvailableInvestmentMinimumAmountRequest_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
money | string | Required | none | Currency, optional: USDT or BTC  
items | array | Required | none | none  
↳ asset | string | Required | none | Currency  
↳ ratio | string | Required | none | Ratio，e.g.100  
      
    
    {
      "money": "string",
      "items": [
        {
          "asset": "string",
          "ratio": "string"
        }
      ]
    }
    
    

##  SwapCoinStruct

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
id | integer | Optional | none | Order ID  
pid | integer | Optional | none | Product ID  
uid | integer | Optional | none | User ID  
coin | string | Optional | none | Currency  
type | integer | Optional | none | Type 0-Staking 1-Redemption  
subtype | string | Optional | none | SubType  
amount | string | Optional | none | Amount  
exchange_rate | string | Optional | none | Exchange ratio  
exchange_amount | string | Optional | none | Redemption Amount  
updateStamp | integer | Optional | none | UpdateTimestamp  
createStamp | integer | Optional | none | Transaction timestamp  
status | integer | Optional | none | status 1-success  
protocol_type | integer | Optional | none | DEFI Protocol Type  
client_order_id | string | Optional | none | Reference ID  
source | string | Optional | none | Order Origin  
      
    
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
    
    

##  CreateEarnFixedTermPreRedeemResponse

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
code | integer | Optional | none | Return code, 0 means success  
message | string | Optional | none | Response message  
data | object | Optional | none | Redemption result (empty object on success)  
timestamp | integer | Optional | none | Response timestamp (in seconds)  
      
    
    {
      "code": 0,
      "message": "string",
      "data": {},
      "timestamp": 0
    }
    
    

##  OrderListStruct

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
page | integer | Required | none | Page  
pageSize | integer | Required | none | Items per page  
pageCount | integer | Required | none | Total pages  
totalCount | integer | Required | none | Total entries  
list | array | Required | none | none  
↳ pid | integer | Required | none | Product ID  
↳ coin | string | Required | none | Staked and redeemed currencies  
↳ amount | string | Required | none | Amount  
↳ type | integer | Required | none | Type 0-Staking 1-Redemption  
↳ status | integer | Required | none | Status  
↳ redeem_stamp | integer | Required | none | Redemption credit time  
↳ createStamp | integer | Required | none | Order time  
↳ exchange_amount | string | Required | none | Exchange rate  
↳ fee | string | Required | none | fee  
      
    
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
    
    

##  DualOrderRefundParams

_Dual-currency order early redemption request_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
order_id | string | Required | none | Order ID  
req_id | string | Required | none | Request ID returned by order-refund-preview  
      
    
    {
      "order_id": "string",
      "req_id": "string"
    }
    
    

##  PlaceDualInvestmentOrderParams

_Dual Investment Order_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
plan_id | string | Required | none | Product ID  
amount | string | Required | none | Subscription amount  
text | string | Optional | none | Order custom information. Users can set custom ID with this field. Custom fields must meet the following conditions:  
  
1\. Must start with `t-`  
2\. Excluding `t-`, length cannot exceed 28 bytes  
3\. Can only contain numbers, letters, underscore(_), hyphen(-) or dot(.)  
      
    
    {
      "plan_id": "string",
      "amount": "string",
      "text": "string"
    }
    
    

##  AutoInvestPlanDetail

_Auto invest planDetails_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
id | integer(int64) | Required | none | Plan ID  
version | integer(int64) | Optional | none | PlanVersion  
name | string | Required | none | Plan name  
create_time | integer(int64) | Required | none | Creation time (Unix timestamp)  
update_time | integer(int64) | Required | none | Update time (Unix timestamp)  
user_id | integer(int64) | Required | none | User ID  
money | string | Required | none | Quote Currency  
amount | string | Required | none | Per PeriodInvestment amount  
period_type | string | Required | none | Cycle type（e.g., monthly）  
period_day | integer(int64) | Required | none | Cycle day  
period_hour | integer(int64) | Required | none | CycleHours  
portfolio | array | Required | none | InvestmentPortfolio  
↳ None | object | Optional | none | Auto invest plan portfolio item  
↳ asset | string | Required | none | Currency  
↳ ratio | string | Required | none | Ratio  
↳ cum_invest | string | Required | none | Accumulated investment  
↳ cum_hold | string | Required | none | AccumulatedPosition  
↳ cum_redeem | string | Required | none | Accumulated redemption  
↳ avg_price | string | Required | none | Average Cost Price  
↳ redeem_status | integer(int64) | Required | none | Redemption status  
↳ lend_amount | string | Required | none | LendingQuantity  
↳ next_time | integer(int64) | Required | none | Next execution time (Unix timestamp)  
↳ period | integer(int64) | Required | none | Executed periods  
↳ fund_source | string | Required | none | Fund source（spot/earn）  
↳ fund_flow | string | Required | none | Fund flow direction (auto_invest/earn)  
      
    
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
    
    

##  AutoInvestCoinsItem

_Currency item supporting auto invest_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
key | string | Required | none | Currency code  
value | string | Required | none | Currency name  
asset_icon_url | string | Required | none | Currency icon URL  
sort | integer(int64) | Optional | none | Sort  
      
    
    {
      "key": "string",
      "value": "string",
      "asset_icon_url": "string",
      "sort": 0
    }
    
    

##  FixedTermProductSimple

_Fixed-term earn product (compact)_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
id | integer | Optional | none | Product ID  
asset | string | Optional | none | Currency  
lock_up_period | integer | Optional | none | Lock-up period (in days)  
year_rate | string | Optional | none | Annual interest rate  
type | integer | Optional | none | Product type: 1 for regular, 2 for VIP  
pre_redeem | integer | Optional | none | Whether early redemption is supported: 0 for not supported, 1 for supported  
reinvest | integer | Optional | none | Whether auto-renewal is supported: 0 for not supported, 1 for supported  
simple_earn | integer | Optional | none | Whether fixed-to-flexible conversion is supported: 0 for not supported, 1 for supported  
min_vip | integer | Optional | none | Minimum VIP level requirement, 0 means no restriction  
max_vip | integer | Optional | none | Maximum VIP level requirement, 0 means no restriction  
sale_status | integer | Optional | none | Sale status: 1 for on sale, 2 for sold out  
      
    
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
    
    

##  AutoInvestConfigItem

_Investment currency configuration item_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
coin | string | Required | none | Currency  
max_limit | string | Required | none | InvestmentLimit  
      
    
    {
      "coin": "string",
      "max_limit": "string"
    }
    
    

##  AutoInvestOrderItem

_Auto invest order item_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
id | integer(int64) | Required | none | Order ID  
type | string | Required | none | type  
amount | string | Required | none | Size  
plan_id | integer(int64) | Required | none | Plan ID  
side | integer(int64) | Required | none | direction  
asset | string | Required | none | Currency  
record_id | integer(int64) | Required | none | Record ID  
total_money | string | Required | none | TotalAmount  
market | string | Required | none | Currency pair  
price | string | Required | none | Price  
create_time | integer(int64) | Required | none | Creation time (Unix timestamp)  
total | string | Required | none | Total  
fund_flow | string | Required | none | Fund Flow Direction  
error_code | integer(int64) | Required | none | Error code  
error_msg | string | Required | none | Error message  
status | integer(int64) | Required | none | Status  
      
    
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
    
    

##  AutoInvestPlanStop

_StopAuto invest planRequest_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
plan_id | integer(int64) | Required | none | Plan ID  
      
    
    {
      "plan_id": 0
    }
    
    

##  FixedTermBonusInfo

_Bonus reward campaign information_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
id | integer | Optional | none | Activity ID  
product_id | integer | Optional | none | Associated product ID  
asset | string | Optional | none | Product currency  
bonus_asset | string | Optional | none | Reward currency  
kyc_limit | string | Optional | none | KYC level restrictions, comma-separated  
ladder_apr | [LadderApr] | Optional | none | Tiered annual interest rate  
total_bonus_amount | string | Optional | none | Total reward amount  
user_total_bonus_amount | string | Optional | none | Maximum reward per user  
status | integer | Optional | none | Activity status: 1 for unlisted, 2 for listed, 3 for delisted  
start_time | string | Optional | none | Activity start time  
end_time | string | Optional | none | Activity end time  
create_time | string | Optional | none | Created time  
start_at | integer | Optional | none | Activity start timestamp (in seconds)  
end_at | integer | Optional | none | Activity end timestamp (in seconds)  
total_issued_amount | string | Optional | none | Total rewards distributed  
user_total_issued_amount | string | Optional | none | Total rewards distributed to the user  
bonus_asset_price | string | Optional | none | Reward currency price (denominated in USDT)  
product_asset_price | string | Optional | none | Product currency price (denominated in USDT)  
product_year_rate | string | Optional | none | Product base annual interest rate  
      
    
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
    
    

##  FixedTermProductInfo

_Product configuration_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
pre_redeem | integer | Required | none | Whether early redemption is supported: 0 for not supported, 1 for supported  
reinvest | integer | Required | none | Whether auto-renewal is supported: 0 for not supported, 1 for supported  
redeem_account | integer | Required | none | Redemption payout account type  
min_vip | integer | Required | none | Minimum VIP level requirement, 0 means no restriction  
max_vip | integer | Required | none | Maximum VIP level requirement, 0 means no restriction  
      
    
    {
      "pre_redeem": 0,
      "reinvest": 0,
      "redeem_account": 0,
      "min_vip": 0,
      "max_vip": 0
    }
    
    

##  LadderApr

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
apr | string | Required | none | Annualized interest rate  
left | string | Required | none | Range lower limit  
right | string | Required | none | Range upper limit  
      
    
    {
      "apr": "string",
      "left": "string",
      "right": "string"
    }
    
    

##  FixedTermCouponInfo

_Interest rate boost coupon information_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
id | integer | Required | none | Interest rate boost coupon record ID  
business | integer | Required | none | Business Type  
user_id | integer(int64) | Required | none | User ID  
asset | string | Required | none | Currency  
order_id | integer(int64) | Required | none | Associated order ID  
financial_rate_id | integer | Required | none | Interest rate boost coupon ID  
buy_limit_low | string | Required | none | Minimum subscription amount for interest rate boost coupon  
buy_limit_high | string | Required | none | Maximum subscription amount for interest rate boost coupon  
rate_day | integer | Required | none | Interest rate boost days  
rate_ratio | string | Required | none | Interest rate boost percentage  
coupon_days | integer | Required | none | Actual interest rate boost days  
coupon_principal | string | Required | none | Principal for interest rate boost calculation  
coupon_year_rate | string | Required | none | Interest rate boost APR  
coupon_interest | string | Required | none | Interest generated from rate boost  
status | integer | Required | none | Status: 1 for active, 2 for settled  
finish_time | string | Required | none | Settlement time  
create_time | string | Required | none | Created time  
      
    
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
    
    

##  FixedTermProduct

_Fixed-term earn product_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
id | integer | Optional | none | Product ID  
name | string | Optional | none | Product name  
asset | string | Optional | none | Currency  
lock_up_period | integer | Optional | none | Lock-up period (in days)  
min_lend_amount | string | Optional | none | Minimum earn amount  
user_max_lend_amount | string | Optional | none | User maximum earn limit  
total_lend_amount | string | Optional | none | Platform earn limit  
year_rate | string | Optional | none | Annual interest rate  
type | integer | Optional | none | Product type: 1 for regular, 2 for VIP  
pre_redeem | integer | Optional | none | Whether early redemption is supported: 0 for not supported, 1 for supported  
reinvest | integer | Optional | none | Whether auto-renewal is supported: 0 for not supported, 1 for supported  
redeem_account | integer | Optional | none | Whether fixed-to-flexible conversion is supported: 0 for not supported, 1 for supported  
min_vip | integer | Optional | none | Minimum VIP level requirement, 0-16, 0 means no restriction  
max_vip | integer | Optional | none | Maximum VIP level requirement (0-16), 0 means no restriction  
status | integer | Optional | none | Product status: 1 for unlisted, 2 for listed, 3 for delisted  
create_time | string | Optional | none | Created time  
user_max_lend_volume | string | Optional | none | User maximum earn amount  
user_total_amount | string | Optional | none | Total amount the user has invested in earn products  
sale_status | integer | Optional | none | Sale status: 1 for on sale, 2 for sold out  
      
    
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