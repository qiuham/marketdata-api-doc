---
exchange: gateio
source_url: https://www.gate.com/docs/developers/apiv4/en/otc
api_type: REST
updated_at: 2026-05-27 20:15:37.983629
---

# OTC

* Python 
  * Shell 


OTC Trading

##  Fiat and stablecoin quote🔒 Authenticated

POST`/otc/quote`

POST `/otc/quote`

_Fiat and stablecoin quote_

Create fiat and stablecoin quotes, supporting both PAY and GET directions

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | OtcQuoteRequest | Required | none  
↳ side | body | string | Required | PAY/GET quote direction. PAY means user inputs pay amount, GET means user inputs get amount. If PAY, pay_amount is required. If GET, get_amount is required  
↳ pay_coin | body | string | Required | Currency the user pays. Supported currencies can be found on the OTC web quote page.  
↳ get_coin | body | string | Required | Currency the user receives. Supported currencies can be found on the OTC web quote page.  
↳ pay_amount | body | string | Optional | User payment currency amount  
↳ get_amount | body | string | Optional | Amount of currency received by the user  
↳ create_quote_token | body | string | Optional | Create quote token: 0: quote preview only; 1: generate quote token for order placement.  
↳ promotion_code | body | string | Optional | Promotion code (optional)  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Quote retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Quote retrieved successfully | OtcQuoteResponse  
  
### Response Schema

Status Code **200**

_OtcQuoteResponse_

Name | Type | Description  
---|---|---  
» code | integer | none  
» message | string | none  
» data | object | none  
»» type | string | BUY (on-ramp) or SELL (off-ramp)  
»» pay_coin | string | Payment currency  
»» get_coin | string | Currency  
»» pay_amount | string | Payment amount  
»» get_amount | string | Redemption Amount  
»» rate | string | Exchange rate  
»» rate_reci | string | Reciprocal of the exchange rate  
»» promotion_code | string | Promotion code  
»» side | string | Quote method  
»» order_type | string | Order type: FIAT (fiat) / STABLE (stablecoin)  
»» quote_token | string | Quote token required when placing an order  
  
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
    
    url = '/otc/quote'
    query_param = ''
    body='{"side":"PAY","pay_coin":"USDT","get_coin":"USD","pay_amount":"30000","get_amount":"30000","create_quote_token":"0","promotion_code":""}'
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
    url="/otc/quote"
    query_param=""
    body_param='{"side":"PAY","pay_coin":"USDT","get_coin":"USD","pay_amount":"30000","get_amount":"30000","create_quote_token":"0","promotion_code":""}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "side": "PAY",
      "pay_coin": "USDT",
      "get_coin": "USD",
      "pay_amount": "30000",
      "get_amount": "30000",
      "create_quote_token": "0",
      "promotion_code": ""
    }
    

> Example responses

> 200 Response
    
    
    {
      "code": 0,
      "message": "success",
      "data": {
        "url": "",
        "memo": "",
        "type": "BUY",
        "pay_coin": "USD",
        "get_coin": "USDT",
        "pay_amount": "30000.00",
        "get_amount": "29891.00",
        "rate": "1.0036",
        "rate_reci": "0.9964",
        "promotion_code": "",
        "side": "PAY",
        "has_signature": "0",
        "validity_period": "300",
        "ex_rate": "0.9967",
        "usdc_rate": "0.99990000",
        "is_need_file": "0",
        "gate_bank_id": "1",
        "gate_bank_name": "",
        "order_type": "FIAT",
        "quote_token": "",
        "refresh_limit": 20,
        "refresh_limit_msg": ""
      },
      "timestamp": 1752051076
    }
    

##  Create fiat order🔒 Authenticated

POST`/otc/order/create`

POST `/otc/order/create`

_Create fiat order_

Create a fiat order, supporting BUY for on-ramp and SELL for off-ramp

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | OtcOrderRequest | Required | none  
↳ type | body | string | Required | BUY (on-ramp) or SELL (off-ramp)  
↳ side | body | string | Required | Quote direction returned by the quote API (used for order validation)  
↳ crypto_currency | body | string | Required | Cryptocurrency (supported currencies can be queried from the OTC web fiat quote page)  
↳ fiat_currency | body | string | Required | Fiat currency (supported currencies can be queried from the OTC web fiat quote page)  
↳ crypto_amount | body | string | Required | Amount of cryptocurrency  
↳ fiat_amount | body | string | Required | Fiat amount  
↳ promotion_code | body | string | Optional | Promotion code  
↳ quote_token | body | string | Required | Parameter returned by the quote API  
↳ bank_id | body | string | Required | Bank card ID used for the order (retrieved via the default bank card API)  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Order created successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Order created successfully | OtcActionResponse  
  
### Response Schema

Status Code **200**

_OtcActionResponse_

Name | Type | Description  
---|---|---  
» code | integer | none  
» message | string | none  
» timestamp | integer | none  
  
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
    
    url = '/otc/order/create'
    query_param = ''
    body='{"type":"BUY","side":"FIAT","crypto_currency":"USDT","fiat_currency":"USD","crypto_amount":"30000","fiat_amount":"30000","promotion_code":"","quote_token":"","bank_id":"2"}'
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
    url="/otc/order/create"
    query_param=""
    body_param='{"type":"BUY","side":"FIAT","crypto_currency":"USDT","fiat_currency":"USD","crypto_amount":"30000","fiat_amount":"30000","promotion_code":"","quote_token":"","bank_id":"2"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "type": "BUY",
      "side": "FIAT",
      "crypto_currency": "USDT",
      "fiat_currency": "USD",
      "crypto_amount": "30000",
      "fiat_amount": "30000",
      "promotion_code": "",
      "quote_token": "",
      "bank_id": "2"
    }
    

> Example responses

> 200 Response
    
    
    {
      "code": 0,
      "message": "success",
      "timestamp": 1752051076
    }
    

##  Create stablecoin order🔒 Authenticated

POST`/otc/stable_coin/order/create`

POST `/otc/stable_coin/order/create`

_Create stablecoin order_

Create stablecoin order

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | OtcStableCoinOrderRequest | Required | none  
↳ pay_coin | body | string | Optional | Currency paid by the user. Supported currencies can be queried from the OTC web stablecoin quote page.  
↳ get_coin | body | string | Optional | Currency to be received by the user. Supported currencies can be queried from the OTC web stablecoin quote page.  
↳ pay_amount | body | string | Optional | User payment currency amount  
↳ get_amount | body | string | Optional | Amount of currency received by the user  
↳ side | body | string | Optional | Quote direction returned by the quote API (used for order validation)  
↳ promotion_code | body | string | Optional | promotion code  
↳ quote_token | body | string | Optional | Parameter returned by the quote API  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Stablecoin order created successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Stablecoin order created successfully | OtcStableCoinOrderCreateResponse  
  
### Response Schema

Status Code **200**

_OtcStableCoinOrderCreateResponse_

Name | Type | Description  
---|---|---  
» code | integer | none  
» message | string | none  
  
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
    
    url = '/otc/stable_coin/order/create'
    query_param = ''
    body='{"pay_coin":"USDC","get_coin":"USDT","pay_amount":"30000","get_amount":"20000","side":"PAY","promotion_code":"","quote_token":"dsafjkdshfjdsjkfah"}'
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
    url="/otc/stable_coin/order/create"
    query_param=""
    body_param='{"pay_coin":"USDC","get_coin":"USDT","pay_amount":"30000","get_amount":"20000","side":"PAY","promotion_code":"","quote_token":"dsafjkdshfjdsjkfah"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "pay_coin": "USDC",
      "get_coin": "USDT",
      "pay_amount": "30000",
      "get_amount": "20000",
      "side": "PAY",
      "promotion_code": "",
      "quote_token": "dsafjkdshfjdsjkfah"
    }
    

> Example responses

> 200 Response
    
    
    {
      "code": 0,
      "message": "string"
    }
    

##  Get user's default bank account information🔒 Authenticated

GET`/otc/get_user_def_bank`

GET `/otc/get_user_def_bank`

Get `user's default bank account information`

Get `user's default bank account information for order placement`

### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | OtcUserDefaultBankResponse  
  
### Response Schema

Status Code **200**

_OtcUserDefaultBankResponse_

Name | Type | Description  
---|---|---  
» code | integer | none  
» message | string | none  
» data | object | none  
»» id | string | Bank ID (required for order placement)  
»» bank_account_name | string | none  
»» bank_name | string | none  
»» bank_country | string | none  
»» bank_address | string | none  
»» bank_code | string | none  
»» branch_code | string | none  
» timestamp | integer | none  
  
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
    
    url = '/otc/get_user_def_bank'
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
    url="/otc/get_user_def_bank"
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
      "code": 0,
      "message": "success",
      "data": {
        "show": 1,
        "message": "test",
        "url": "/otc/apply_person"
      },
      "timestamp": 1751434613
    }
    

##  Get user bank card list🔒 Authenticated

GET`/otc/bank_list`

GET `/otc/bank_list`

Get `user bank card list`

Get `user bank card list for selecting bank card when placing orders`

### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | OtcBankListResponse  
  
### Response Schema

Status Code **200**

_OtcBankListResponse_

Name | Type | Description  
---|---|---  
» code | integer | none  
» message | string | none  
» data | object | none  
»» lists | array | Bank card list  
»»» OtcBankListItem | object | none  
»»»» id | string | Bank ID (required for order placement)  
»»»» bank_account_name | string | Bank account name  
»»»» bank_name | string | Bank name  
»»»» bank_country | string | Bank country  
»»»» bank_address | string | Bank address  
»»»» bank_code | string | Bank code  
»»»» branch_code | string | Branch code  
»»»» iban | string | IBAN number  
»»»» swift | string | SWIFT code  
»»»» remittance_line_number | string | Remittance routing number  
»»»» agent_bank_name | string | Correspondent bank name  
»»»» agent_bank_swift | string | Correspondent bank SWIFT code  
»»»» submit_time | string | Submission time  
»»»» update_time | string | Update time  
»»»» status | string | Status  
»»»» documentation_file_type | string | Document file type  
»»»» memo | string | Remark  
»»»» is_default | integer | Whether it is the default bank card. 1 - Yes, 0 - No  
»»»» bank_id | string | Bank ID  
»»»» documentation_file_key_url | string | Document file URL  
»»» timestamp | integer | none  
  
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
    
    url = '/otc/bank_list'
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
    url="/otc/bank_list"
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
      "code": 0,
      "message": "success",
      "data": {
        "lists": [
          {
            "id": "762",
            "bank_account_name": "hshsbshhh",
            "bank_name": "jjjsjhs",
            "bank_country": "Anguilla",
            "bank_address": "jshhtestaddress879hao",
            "bank_code": "",
            "branch_code": "",
            "iban": "1554 **** 8756",
            "swift": "455876663",
            "remittance_line_number": "4867645497945",
            "agent_bank_name": "",
            "agent_bank_swift": "",
            "submit_time": "2026-01-21 05:56:49",
            "update_time": "2026-01-21 05:57:09",
            "status": "1",
            "documentation_file_type": "",
            "memo": "",
            "is_default": 1,
            "bank_id": "762",
            "documentation_file_key_url": ""
          }
        ]
      },
      "timestamp": 1769998217
    }
    

##  Mark fiat order as paid🔒 Authenticated

POST`/otc/order/paid`

POST `/otc/order/paid`

_Mark fiat order as paid_

Mark fiat order as paid

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | OtcMarkOrderPaidRequest | Required | none  
↳ order_id | body | string | Required | Order ID  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)The order has been marked as paid

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | The order has been marked as paid | OtcActionResponse  
  
### Response Schema

Status Code **200**

_OtcActionResponse_

Name | Type | Description  
---|---|---  
» code | integer | none  
» message | string | none  
» timestamp | integer | none  
  
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
    
    url = '/otc/order/paid'
    query_param = ''
    body='{"order_id":"203"}'
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
    url="/otc/order/paid"
    query_param=""
    body_param='{"order_id":"203"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "order_id": "203"
    }
    

> Example responses

> 200 Response
    
    
    {
      "code": 0,
      "message": "success",
      "timestamp": 1752051076
    }
    

##  Fiat order cancellation🔒 Authenticated

POST`/otc/order/cancel`

POST `/otc/order/cancel`

_Fiat order cancellation_

Cancel fiat order

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
order_id | query | string | Required | Order ID  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Order cancelled successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Order cancelled successfully | OtcActionResponse  
  
### Response Schema

Status Code **200**

_OtcActionResponse_

Name | Type | Description  
---|---|---  
» code | integer | none  
» message | string | none  
» timestamp | integer | none  
  
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
    
    url = '/otc/order/cancel'
    query_param = 'order_id=string'
    # for `gen_sign` implementation, refer to section `Authentication` above
    sign_headers = gen_sign('POST', prefix + url, query_param)
    headers.update(sign_headers)
    r = requests.request('POST', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="POST"
    url="/otc/order/cancel"
    query_param="order_id=string"
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
      "message": "success",
      "timestamp": 1752051076
    }
    

##  Fiat order list🔒 Authenticated

GET`/otc/order/list`

GET `/otc/order/list`

_Fiat order list_

Query the fiat order list with filters such as type, currency, time range, and status

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
type | query | string | Optional | BUY (on-ramp) or SELL (off-ramp)  
fiat_currency | query | string | Optional | Fiat currency  
crypto_currency | query | string | Optional | Digital currency  
start_time | query | string | Optional | Start Time  
end_time | query | string | Optional | End time  
status | query | string | Optional | DONE ：Completed  
pn | query | string | Optional | Page number  
ps | query | string | Optional | Number of items per page  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | OtcOrderListResponse  
  
### Response Schema

Status Code **200**

_OtcOrderListResponse_

Name | Type | Description  
---|---|---  
» code | integer | none  
» message | string | none  
» data | object | none  
»» pn | integer | none  
»» ps | integer | none  
»» total_pn | integer | none  
»» count | integer | none  
»» list | array | none  
»»» OtcOrderListItem | object | none  
»»»» time | string | Current time  
»»»» timestamp | integer | Current timestamp  
»»»» order_id | string | orderId  
»»»» trade_no | string | Trade number  
»»»» type | string | Quote direction buy/sell/all  
»»»» status | string | Order Status  
»»»» db_status | string | none  
»»»» fiat_currency | string | Fiat type  
»»»» fiat_currency_info | object | none  
»»»»» name | string | Name  
»»»»» icon | string | Image  
»»»» fiat_amount | string | Fiat amount  
»»»» crypto_currency | string | Stablecoin  
»»»» crypto_currency_info | object | none  
»»»»» name | string | none  
»»»»» icon | string | none  
»»»» crypto_amount | string | Stablecoin amount  
»»»» rate | string | Exchange rate  
»»»» transfer_remark | string | Remark  
»»»» gate_bank_account_iban | string | Bank account  
»»»» promotion_code | string | Promotion code  
  
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
    
    url = '/otc/order/list'
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
    url="/otc/order/list"
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
      "code": 0,
      "message": "Success",
      "data": {
        "pn": 1,
        "ps": 10,
        "total_pn": 1,
        "count": 2,
        "list": [
          {
            "time": "2025-02-11 07:45:06",
            "timestamp": 1739000013,
            "order_id": "41",
            "trade_no": "20250207043457590939",
            "type": "SELL",
            "status": "PROCESSIONG",
            "db_status": "PAID",
            "fiat_currency": "USD",
            "fiat_currency_info": {
              "name": "USD",
              "icon": "http://icon.url"
            },
            "fiat_amount": "199600",
            "ceypto_currency": "USDT",
            "crypto_currency_info": {
              "name": "USDT",
              "icon": "http://icon.url"
            },
            "crypto_amount": "200000",
            "rate": "0.998000",
            "transfer_remark": "",
            "gate_bank_account_iban": "89b9b9b9b",
            "promotion_code": ""
          }
        ]
      }
    }
    

##  Stablecoin order list🔒 Authenticated

GET`/otc/stable_coin/order/list`

GET `/otc/stable_coin/order/list`

_Stablecoin order list_

Query stablecoin order list with filtering by currency, time range, status, etc.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
page_size | query | string | Optional | Number of records per page  
page_number | query | string | Optional | Page number  
coin_name | query | string | Optional | ordercurrency  
start_time | query | string | Optional | Start Time  
end_time | query | string | Optional | End time  
status | query | string | Optional | Status: PROCESSING: in progress / DONE：completed / FAILED: failed  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | OtcStableCoinOrderListResponse  
  
### Response Schema

Status Code **200**

_OtcStableCoinOrderListResponse_

Name | Type | Description  
---|---|---  
» code | integer | none  
» message | string | none  
» data | object | none  
»» total | integer | none  
»» page_size | integer | none  
»» page_number | integer | none  
»» total_page | integer | none  
»» list | array | none  
»»» OtcStableCoinOrderListItem | object | none  
»»»» id | integer | Order ID  
»»»» trade_no | string | Transaction reference number  
»»»» pay_coin | string | Payment currency  
»»»» pay_amount | string | Payment amount  
»»»» get_coin | string | Received currency  
»»»» get_amount | string | Received amount  
»»»» rate | string | Exchange rate  
»»»» rate_reci | string | Reciprocal of the exchange rate  
»»»» status | string | PROCESSING: in progress / DONE: completed / FAILED: failed  
»»»» create_timest | integer | timetimestamp  
»»»» create_time | string | Created time  
  
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
    
    url = '/otc/stable_coin/order/list'
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
    url="/otc/stable_coin/order/list"
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
      "code": 0,
      "message": "success",
      "data": {
        "total": 20,
        "page_size": 10,
        "page_number": 1,
        "total_page": 10,
        "list": [
          {
            "id": 1,
            "trade_no": "89875324974",
            "pay_coin": "USDT",
            "pay_icon": "https://icon.com",
            "pay_amount": "30000.00",
            "get_coin": "JDUSD",
            "get_icon": "https://icon.com",
            "get_amount": "20000.00",
            "rate": "1.5",
            "rate_reci": "0.6667",
            "status": "PROCESSING",
            "create_timest": 17878979789,
            "create_time": "2025-09-09 10:00:00"
          }
        ]
      }
    }
    

##  Fiat order details🔒 Authenticated

GET`/otc/order/detail`

GET `/otc/order/detail`

_Fiat order details_

Query fiat order details

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
order_id | query | string | Required | Order ID  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | OtcOrderDetailResponse  
  
### Response Schema

Status Code **200**

_OtcOrderDetailResponse_

Name | Type | Description  
---|---|---  
» message | string | none  
» code | integer | none  
» data | object | none  
»» order_id | string | Order ID  
»» uid | string | User ID  
»» type | string | Order Type  
»» fiat_currency | string | Fiat type  
»» fiat_amount | string | Fiat amount  
»» crypto_currency | string | Stablecoin  
»» crypto_amount | string | Stablecoin amount  
»» rate | string | Exchange rate  
»» transfer_remark | string | Remark  
»» status | string | Status  
»» db_status | string | none  
»» create_time | string | Created time  
»» memo | string | Cancellation or rejection reason  
»» side | string | Quote direction  
»» promotion_code | string | Promotion code  
»» trade_no | string | Trade number  
  
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
    
    url = '/otc/order/detail'
    query_param = 'order_id=string'
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
    url="/otc/order/detail"
    query_param="order_id=string"
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
      "message": "成功",
      "code": 0,
      "data": {
        "order_id": "265",
        "uid": "2124269088",
        "type": "BUY",
        "fiat_currency": "USD",
        "fiat_amount": "300000",
        "crypto_currency": "USDT",
        "crypto_amount": "299700",
        "rate": "1.001001",
        "transfer_remark": "Bank Code: 016, Branch Code: 478",
        "status": "PROCESSIONG",
        "db_status": "PAID",
        "create_time": "2025-03-07 07:51:52",
        "memo": "",
        "side": "FIAT",
        "promotion_code": "",
        "trade_no": "20250307075152206853"
      }
    }
    

#  Schemas

##  OtcOrderRequest

_Fiat Order Request Body_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
type | string | Required | none | BUY (on-ramp) or SELL (off-ramp)  
side | string | Required | none | Quote direction returned by the quote API (used for order validation)  
crypto_currency | string | Required | none | Cryptocurrency (supported currencies can be queried from the OTC web fiat quote page)  
fiat_currency | string | Required | none | Fiat currency (supported currencies can be queried from the OTC web fiat quote page)  
crypto_amount | string | Required | none | Amount of cryptocurrency  
fiat_amount | string | Required | none | Fiat amount  
promotion_code | string | Optional | none | Promotion code  
quote_token | string | Required | none | Parameter returned by the quote API  
bank_id | string | Required | none | Bank card ID used for the order (retrieved via the default bank card API)  
      
    
    {
      "type": "BUY",
      "side": "FIAT",
      "crypto_currency": "USDT",
      "fiat_currency": "USD",
      "crypto_amount": "30000",
      "fiat_amount": "30000",
      "promotion_code": "",
      "quote_token": "",
      "bank_id": "2"
    }
    
    

##  OtcQuoteRequest

_Fiat and Stablecoin Quote Request Body_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
side | string | Required | none | PAY/GET quote direction. PAY means user inputs pay amount, GET means user inputs get amount. If PAY, pay_amount is required. If GET, get_amount is required  
pay_coin | string | Required | none | Currency the user pays. Supported currencies can be found on the OTC web quote page.  
get_coin | string | Required | none | Currency the user receives. Supported currencies can be found on the OTC web quote page.  
pay_amount | string | Optional | none | User payment currency amount  
get_amount | string | Optional | none | Amount of currency received by the user  
create_quote_token | string | Optional | none | Create quote token: 0: quote preview only; 1: generate quote token for order placement.  
promotion_code | string | Optional | none | Promotion code (optional)  
      
    
    {
      "side": "PAY",
      "pay_coin": "USDT",
      "get_coin": "USD",
      "pay_amount": "30000",
      "get_amount": "30000",
      "create_quote_token": "0",
      "promotion_code": ""
    }
    
    

##  OtcBankListResponse

_OtcBankListResponse_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
code | integer | Required | none | none  
message | string | Required | none | none  
data | object | Required | none | none  
↳ lists | array | Required | none | Bank card list  
↳ OtcBankListItem | object | Optional | none | none  
↳ id | string | Required | none | Bank ID (required for order placement)  
↳ bank_account_name | string | Required | none | Bank account name  
↳ bank_name | string | Required | none | Bank name  
↳ bank_country | string | Optional | none | Bank country  
↳ bank_address | string | Optional | none | Bank address  
↳ bank_code | string | Optional | none | Bank code  
↳ branch_code | string | Optional | none | Branch code  
↳ iban | string | Optional | none | IBAN number  
↳ swift | string | Optional | none | SWIFT code  
↳ remittance_line_number | string | Optional | none | Remittance routing number  
↳ agent_bank_name | string | Optional | none | Correspondent bank name  
↳ agent_bank_swift | string | Optional | none | Correspondent bank SWIFT code  
↳ submit_time | string | Optional | none | Submission time  
↳ update_time | string | Optional | none | Update time  
↳ status | string | Optional | none | Status  
↳ documentation_file_type | string | Optional | none | Document file type  
↳ memo | string | Optional | none | Remark  
↳ is_default | integer | Optional | none | Whether it is the default bank card. 1 - Yes, 0 - No  
↳ bank_id | string | Optional | none | Bank ID  
↳ documentation_file_key_url | string | Optional | none | Document file URL  
↳ timestamp | integer | Required | none | none  
      
    
    {
      "code": 0,
      "message": "string",
      "data": {
        "lists": [
          {}
        ]
      },
      "timestamp": 0
    }
    
    

##  OtcQuoteResponse

_OtcQuoteResponse_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
code | integer | Required | none | none  
message | string | Required | none | none  
data | object | Required | none | none  
↳ type | string | Required | none | BUY (on-ramp) or SELL (off-ramp)  
↳ pay_coin | string | Required | none | Payment currency  
↳ get_coin | string | Required | none | Currency  
↳ pay_amount | string | Required | none | Payment amount  
↳ get_amount | string | Required | none | Redemption Amount  
↳ rate | string | Required | none | Exchange rate  
↳ rate_reci | string | Required | none | Reciprocal of the exchange rate  
↳ promotion_code | string | Required | none | Promotion code  
↳ side | string | Required | none | Quote method  
↳ order_type | string | Required | none | Order type: FIAT (fiat) / STABLE (stablecoin)  
↳ quote_token | string | Required | none | Quote token required when placing an order  
      
    
    {
      "code": 0,
      "message": "string",
      "data": {
        "type": "string",
        "pay_coin": "string",
        "get_coin": "string",
        "pay_amount": "string",
        "get_amount": "string",
        "rate": "string",
        "rate_reci": "string",
        "promotion_code": "string",
        "side": "string",
        "order_type": "string",
        "quote_token": "string"
      }
    }
    
    

##  OtcOrderListResponse

_OtcOrderListResponse_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
code | integer | Required | none | none  
message | string | Required | none | none  
data | object | Required | none | none  
↳ pn | integer | Required | none | none  
↳ ps | integer | Required | none | none  
↳ total_pn | integer | Required | none | none  
↳ count | integer | Required | none | none  
↳ list | array | Required | none | none  
↳ OtcOrderListItem | object | Optional | none | none  
↳ time | string | Optional | none | Current time  
↳ timestamp | integer | Optional | none | Current timestamp  
↳ order_id | string | Optional | none | orderId  
↳ trade_no | string | Optional | none | Trade number  
↳ type | string | Optional | none | Quote direction buy/sell/all  
↳ status | string | Optional | none | Order Status  
↳ db_status | string | Optional | none | none  
↳ fiat_currency | string | Optional | none | Fiat type  
↳ fiat_currency_info | object | Optional | none | none  
↳ name | string | Required | none | Name  
↳ icon | string | Required | none | Image  
↳ fiat_amount | string | Optional | none | Fiat amount  
↳ crypto_currency | string | Optional | none | Stablecoin  
↳ crypto_currency_info | object | Optional | none | none  
↳ name | string | Required | none | none  
↳ icon | string | Required | none | none  
↳ crypto_amount | string | Optional | none | Stablecoin amount  
↳ rate | string | Optional | none | Exchange rate  
↳ transfer_remark | string | Optional | none | Remark  
↳ gate_bank_account_iban | string | Optional | none | Bank account  
↳ promotion_code | string | Optional | none | Promotion code  
      
    
    {
      "code": 0,
      "message": "string",
      "data": {
        "pn": 0,
        "ps": 0,
        "total_pn": 0,
        "count": 0,
        "list": [
          {}
        ]
      }
    }
    
    

##  OtcActionResponse

_OtcActionResponse_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
code | integer | Required | none | none  
message | string | Required | none | none  
timestamp | integer | Required | none | none  
      
    
    {
      "code": 0,
      "message": "string",
      "timestamp": 0
    }
    
    

##  OtcOrderDetailResponse

_OtcOrderDetailResponse_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
message | string | Required | none | none  
code | integer | Required | none | none  
data | object | Required | none | none  
↳ order_id | string | Required | none | Order ID  
↳ uid | string | Required | none | User ID  
↳ type | string | Required | none | Order Type  
↳ fiat_currency | string | Required | none | Fiat type  
↳ fiat_amount | string | Required | none | Fiat amount  
↳ crypto_currency | string | Required | none | Stablecoin  
↳ crypto_amount | string | Required | none | Stablecoin amount  
↳ rate | string | Required | none | Exchange rate  
↳ transfer_remark | string | Required | none | Remark  
↳ status | string | Required | none | Status  
↳ db_status | string | Required | none | none  
↳ create_time | string | Required | none | Created time  
↳ memo | string | Required | none | Cancellation or rejection reason  
↳ side | string | Required | none | Quote direction  
↳ promotion_code | string | Required | none | Promotion code  
↳ trade_no | string | Required | none | Trade number  
      
    
    {
      "message": "string",
      "code": 0,
      "data": {
        "order_id": "string",
        "uid": "string",
        "type": "string",
        "fiat_currency": "string",
        "fiat_amount": "string",
        "crypto_currency": "string",
        "crypto_amount": "string",
        "rate": "string",
        "transfer_remark": "string",
        "status": "string",
        "db_status": "string",
        "create_time": "string",
        "memo": "string",
        "side": "string",
        "promotion_code": "string",
        "trade_no": "string"
      }
    }
    
    

##  OtcUserDefaultBankResponse

_OtcUserDefaultBankResponse_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
code | integer | Required | none | none  
message | string | Required | none | none  
data | object | Required | none | none  
↳ id | string | Required | none | Bank ID (required for order placement)  
↳ bank_account_name | string | Required | none | none  
↳ bank_name | string | Required | none | none  
↳ bank_country | string | Required | none | none  
↳ bank_address | string | Required | none | none  
↳ bank_code | string | Required | none | none  
↳ branch_code | string | Required | none | none  
timestamp | integer | Required | none | none  
      
    
    {
      "code": 0,
      "message": "string",
      "data": {
        "id": "string",
        "bank_account_name": "string",
        "bank_name": "string",
        "bank_country": "string",
        "bank_address": "string",
        "bank_code": "string",
        "branch_code": "string"
      },
      "timestamp": 0
    }
    
    

##  OtcStableCoinOrderListResponse

_OtcStableCoinOrderListResponse_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
code | integer | Required | none | none  
message | string | Required | none | none  
data | object | Required | none | none  
↳ total | integer | Required | none | none  
↳ page_size | integer | Required | none | none  
↳ page_number | integer | Required | none | none  
↳ total_page | integer | Required | none | none  
↳ list | array | Required | none | none  
↳ OtcStableCoinOrderListItem | object | Optional | none | none  
↳ id | integer | Optional | none | Order ID  
↳ trade_no | string | Optional | none | Transaction reference number  
↳ pay_coin | string | Optional | none | Payment currency  
↳ pay_amount | string | Optional | none | Payment amount  
↳ get_coin | string | Optional | none | Received currency  
↳ get_amount | string | Optional | none | Received amount  
↳ rate | string | Optional | none | Exchange rate  
↳ rate_reci | string | Optional | none | Reciprocal of the exchange rate  
↳ status | string | Optional | none | PROCESSING: in progress / DONE: completed / FAILED: failed  
↳ create_timest | integer | Optional | none | timetimestamp  
↳ create_time | string | Optional | none | Created time  
      
    
    {
      "code": 0,
      "message": "string",
      "data": {
        "total": 0,
        "page_size": 0,
        "page_number": 0,
        "total_page": 0,
        "list": [
          {}
        ]
      }
    }
    
    

##  OtcStableCoinOrderRequest

_Stablecoin Order Request Body_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
pay_coin | string | Optional | none | Currency paid by the user. Supported currencies can be queried from the OTC web stablecoin quote page.  
get_coin | string | Optional | none | Currency to be received by the user. Supported currencies can be queried from the OTC web stablecoin quote page.  
pay_amount | string | Optional | none | User payment currency amount  
get_amount | string | Optional | none | Amount of currency received by the user  
side | string | Optional | none | Quote direction returned by the quote API (used for order validation)  
promotion_code | string | Optional | none | promotion code  
quote_token | string | Optional | none | Parameter returned by the quote API  
      
    
    {
      "pay_coin": "USDC",
      "get_coin": "USDT",
      "pay_amount": "30000",
      "get_amount": "20000",
      "side": "PAY",
      "promotion_code": "",
      "quote_token": "dsafjkdshfjdsjkfah"
    }
    
    

##  OtcStableCoinOrderCreateResponse

_OtcStableCoinOrderCreateResponse_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
code | integer | Required | none | none  
message | string | Required | none | none  
      
    
    {
      "code": 0,
      "message": "string"
    }
    
    

##  OtcMarkOrderPaidRequest

_Fiat Order Set Paid Request Body_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
order_id | string | Required | none | Order ID  
      
    
    {
      "order_id": "203"
    }