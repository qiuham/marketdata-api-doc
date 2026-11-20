---
exchange: gateio
source_url: https://www.gate.com/docs/developers/apiv4/en/otc
api_type: REST
updated_at: 2026-11-20 18:57:03.412516
---

# OTC

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
side | body | string | Required | PAY: specify the payment amount (`pay_amount` is required); GET: specify the receive amount (`get_amount` is required).  
pay_coin | body | string | Required | Payment currency. Supported currencies are available on the OTC web quote page.  
get_coin | body | string | Required | Receive currency. Supported currencies are available on the OTC web quote page.  
pay_amount | body | string | Optional | User payment currency amount  
get_amount | body | string | Optional | Amount of currency received by the user  
create_quote_token | body | string | Optional | Create quote token: 0: quote preview only; 1: generate quote token for order placement.  
promotion_code | body | string | Optional | Promotion code  
  
####  Request Body Schema

Fiat and Stablecoin Quote Request Body

Request Body SchemaType | Constraints  
---|---  
OtcQuoteRequest | required: ["side","pay_coin","get_coin"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
side | string | Required |  | PAY: specify the payment amount (`pay_amount` is required); GET: specify the receive amount (`get_amount` is required).  
pay_coin | string | Required |  | Payment currency. Supported currencies are available on the OTC web quote page.  
get_coin | string | Required |  | Receive currency. Supported currencies are available on the OTC web quote page.  
pay_amount | string | Optional |  | User payment currency amount  
get_amount | string | Optional |  | Amount of currency received by the user  
create_quote_token | string | Optional |  | Create quote token: 0: quote preview only; 1: generate quote token for order placement.  
promotion_code | string | Optional |  | Promotion code  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Quote retrieved successfully | OtcQuoteResponse  
  
### Response Schema

Status Code **200**

OtcQuoteResponse

Type | Constraints  
---|---  
OtcQuoteResponse | required: ["code","message","data","timestamp"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
code | integer | Required |  |   
message | string | Required |  |   
data | object | Required | required: ["type","pay_coin","get_coin","pay_amount","get_amount","rate","rate_reci","promotion_code","side","order_type","quote_token"] |   
timestamp | integer | Required |  | Server Unix timestamp in seconds  
  
**data**

OtcQuoteResult

Type | Constraints  
---|---  
object | required: ["type","pay_coin","get_coin","pay_amount","get_amount","rate","rate_reci","promotion_code","side","order_type","quote_token"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
type | string | Required |  | BUY (on-ramp) or SELL (off-ramp)  
pay_coin | string | Required |  | Payment currency  
get_coin | string | Required |  | Currency  
pay_amount | string | Required |  | Payment amount  
get_amount | string | Required |  | Redemption Amount  
rate | string | Required |  | Exchange rate  
rate_reci | string | Required |  | Reciprocal of the exchange rate  
promotion_code | string | Required |  | Promotion code  
side | string | Required |  | Quote method  
order_type | string | Required |  | Order type: FIAT (fiat) / STABLE (stablecoin)  
quote_token | string | Required |  | Quote token required when placing an order  
validity_period | string | Optional |  | Quote validity period (seconds)  
refresh_limit | integer | Optional |  | Quote refresh limit  
refresh_limit_msg | string | Optional |  | Quote refresh limit message  
  
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
        "type": "BUY",
        "pay_coin": "USD",
        "get_coin": "USDT",
        "pay_amount": "30000.00",
        "get_amount": "29891.00",
        "rate": "1.0036",
        "rate_reci": "0.9964",
        "promotion_code": "",
        "side": "PAY",
        "validity_period": "300",
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
type | body | string | Required | BUY for on-ramp, SELL for off-ramp  
side | body | string | Required | The side returned by the quote endpoint (used for order validation). For backward compatibility, `FIAT`/`CRYPTO` or `PAY`/`GET` are accepted; new integrations should use the value returned by the quote response.  
crypto_currency | body | string | Required | Cryptocurrency (supported currencies can be queried from the OTC web fiat quote page)  
fiat_currency | body | string | Required | Fiat currency (supported currencies can be queried from the OTC web fiat quote page)  
crypto_amount | body | string | Required | Amount of cryptocurrency  
fiat_amount | body | string | Required | Fiat amount  
promotion_code | body | string | Optional | Promotion code  
quote_token | body | string | Required | Parameter returned by the quote API  
bank_id | body | string | Required | Bank card ID used to place the order. Select one from the list returned by `GET /otc/bank/list`; the default card has `is_default=1`.  
receive_type | body | string | Optional | Name used for the remittance. Allowed values depend on the user type:  
Corporate users: YOU (remit in your company's name), GATE (remit in Gate's name), RECIPIENT (remit in the recipient's name);  
Individual users: GATE (remit in Gate's name), PERSON (remit in the user's own name).  
  
####  Detailed descriptions

** receive_type**: Name used for the remittance. Allowed values depend on the user type:  
Corporate users: YOU (remit in your company's name), GATE (remit in Gate's name), RECIPIENT (remit in the recipient's name);  
Individual users: GATE (remit in Gate's name), PERSON (remit in the user's own name).

####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
receive_type | YOU  
receive_type | GATE  
receive_type | RECIPIENT  
receive_type | PERSON  
  
####  Request Body Schema

Fiat Order Request Body

Request Body SchemaType | Constraints  
---|---  
OtcOrderRequest | required: ["type","side","crypto_currency","fiat_currency","crypto_amount","fiat_amount","quote_token","bank_id"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
type | string | Required |  | BUY for on-ramp, SELL for off-ramp  
side | string | Required |  | The side returned by the quote endpoint (used for order validation). For backward compatibility, `FIAT`/`CRYPTO` or `PAY`/`GET` are accepted; new integrations should use the value returned by the quote response.  
crypto_currency | string | Required |  | Cryptocurrency (supported currencies can be queried from the OTC web fiat quote page)  
fiat_currency | string | Required |  | Fiat currency (supported currencies can be queried from the OTC web fiat quote page)  
crypto_amount | string | Required |  | Amount of cryptocurrency  
fiat_amount | string | Required |  | Fiat amount  
promotion_code | string | Optional |  | Promotion code  
quote_token | string | Required |  | Parameter returned by the quote API  
bank_id | string | Required |  | Bank card ID used to place the order. Select one from the list returned by `GET /otc/bank/list`; the default card has `is_default=1`.  
receive_type | string | Optional | enum: ["YOU","GATE","RECIPIENT","PERSON"] | Name used for the remittance. Allowed values depend on the user type:  
Corporate users: YOU (remit in your company's name), GATE (remit in Gate's name), RECIPIENT (remit in the recipient's name);  
Individual users: GATE (remit in Gate's name), PERSON (remit in the user's own name).  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Order created successfully | OtcActionResponse  
  
### Response Schema

Status Code **200**

OtcActionResponse

Type | Constraints  
---|---  
OtcActionResponse | required: ["code","message","timestamp"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
code | integer | Required |  |   
message | string | Required |  |   
timestamp | integer | Required |  |   
  
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
    body='{"type":"BUY","side":"FIAT","crypto_currency":"USDT","fiat_currency":"USD","crypto_amount":"30000","fiat_amount":"30000","promotion_code":"","quote_token":"","bank_id":"2","receive_type":"GATE"}'
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
    body_param='{"type":"BUY","side":"FIAT","crypto_currency":"USDT","fiat_currency":"USD","crypto_amount":"30000","fiat_amount":"30000","promotion_code":"","quote_token":"","bank_id":"2","receive_type":"GATE"}'
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
      "bank_id": "2",
      "receive_type": "GATE"
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

Create a stablecoin order. All request body fields except `promotion_code` are required.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | OtcStableCoinOrderRequest | Required | none  
pay_coin | body | string | Required | Currency paid by the user. Supported currencies can be queried from the OTC web stablecoin quote page.  
get_coin | body | string | Required | Currency to be received by the user. Supported currencies can be queried from the OTC web stablecoin quote page.  
pay_amount | body | string | Required | User payment currency amount  
get_amount | body | string | Required | Amount of currency received by the user  
side | body | string | Required | The side returned by the quote endpoint (used for order validation). For backward compatibility, `PAY`/`GET` are accepted; new integrations should use the value returned by the quote response.  
promotion_code | body | string | Optional | Promotion code (optional)  
quote_token | body | string | Required | Parameter returned by the quote API  
  
####  Request Body Schema

Stablecoin Order Request Body

Request Body SchemaType | Constraints  
---|---  
OtcStableCoinOrderRequest | required: ["pay_coin","get_coin","pay_amount","get_amount","side","quote_token"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
pay_coin | string | Required |  | Currency paid by the user. Supported currencies can be queried from the OTC web stablecoin quote page.  
get_coin | string | Required |  | Currency to be received by the user. Supported currencies can be queried from the OTC web stablecoin quote page.  
pay_amount | string | Required |  | User payment currency amount  
get_amount | string | Required |  | Amount of currency received by the user  
side | string | Required |  | The side returned by the quote endpoint (used for order validation). For backward compatibility, `PAY`/`GET` are accepted; new integrations should use the value returned by the quote response.  
promotion_code | string | Optional |  | Promotion code (optional)  
quote_token | string | Required |  | Parameter returned by the quote API  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Stablecoin order created successfully | OtcStableCoinOrderCreateResponse  
  
### Response Schema

Status Code **200**

OtcStableCoinOrderCreateResponse

Type | Constraints  
---|---  
OtcStableCoinOrderCreateResponse | required: ["code","message","timestamp"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
code | integer | Required |  | Business code; 0 indicates success  
message | string | Required |  | Message  
timestamp | integer | Required |  | Server Unix timestamp in seconds  
  
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
      "message": "success",
      "timestamp": 1752051076
    }
    

##  Get user bank card list🔒 Authenticated

GET`/otc/bank/list`

GET `/otc/bank/list`

_Get user bank card list_

List the user's bank cards for selecting a card when placing an order. **Default card** : use the `is_default` field in each list item (`1` indicates the default). The deprecated standalone default-bank-card endpoint is no longer required.

### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | OtcBankListResponse  
  
### Response Schema

Status Code **200**

OtcBankListResponse

Type | Constraints  
---|---  
OtcBankListResponse | required: ["code","message","data","timestamp"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
code | integer | Required |  |   
message | string | Required |  |   
data | object | Required | required: ["lists"] |   
timestamp | integer | Required |  |   
  
**data**

OtcBankListResult

Type | Constraints  
---|---  
object | required: ["lists"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
lists | array | Required |  | Bank card list  
  
**data / lists**

Bank card list

Type | Constraints  
---|---  
array |   
  
**data / lists / items**

OtcBankListItem

Type | Constraints  
---|---  
object | required: ["id","bank_account_name","bank_name"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | string | Required |  | Bank card ID (used when placing an order; the synonymous `bank_id` field has been consolidated into `id`)  
bank_account_name | string | Required |  | Bank account name  
bank_name | string | Required |  | Bank name  
bank_country | string | Optional |  | Bank country  
bank_address | string | Optional |  | Bank address  
iban | string | Optional |  | IBAN number  
swift | string | Optional |  | SWIFT code  
remittance_line_number | string | Optional |  | Remittance routing number  
agent_bank_name | string | Optional |  | Correspondent bank name  
agent_bank_swift | string | Optional |  | Correspondent bank SWIFT code  
submit_time | string | Optional |  | Submission time  
update_time | string | Optional |  | Update time  
status | string | Optional |  | Status  
is_default | integer | Optional |  | Whether it is the default bank card. 1 - Yes, 0 - No  
  
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
    
    url = '/otc/bank/list'
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
    url="/otc/bank/list"
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
      "message": "string",
      "data": {
        "lists": [
          {}
        ]
      },
      "timestamp": 0
    }
    

##  Create bank card🔒 Authenticated

POST`/otc/bank/create`

POST `/otc/bank/create`

_Create bank card_

Bind a bank card. Under the Global entity, non-same-name accounts may enter manual review (`status` pending) and require supplementary materials later. Corresponds to Inner: `POST /bank/create`. Fields and protocol follow the live form/gateway; `bank_account_name` may be Base64-encoded in some environments—see integration notes.

Account-opening proof supports two methods (choose one):

  1. **Pre-upload (recommended)** : call `POST /otc/upload/pre_upload` (`scene=bank`) to obtain a temporary-bucket Policy and upload directly to S3, then pass `documentation_file_key` \+ `file_type` in this endpoint;
  2. **Multipart direct upload** : pass the `documentation_file` file field; the server writes directly to the production bucket.

When using pre-upload, the server validates object existence and that the uid in the `file_key` path matches the caller; after validation, the object is moved to the production bucket and persisted. Cross-user references return `Invalid parameters file_key`; incomplete direct upload returns `Invalid parameters file not uploaded`.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | OtcBankCreateMultipartRequest | Required | none  
  
####  Request Body Schema

Inner create-bank-card `multipart/form-data`. Account-opening proof file (choose one):

  * **Pre-upload** : `documentation_file_key` \+ `file_type` (call `POST /otc/upload/pre_upload` first, `scene=bank`);
  * **Multipart direct upload** : `documentation_file` file field.

Request Body SchemaType | Constraints  
---|---  
OtcBankCreateMultipartRequest | required: ["bank_account_name","bank_name","bank_country","bank_address","iban","swift"]  
  
**Properties**

Request Body SchemaName | Type | Required in this object | Constraints | Description  
---|---|---|---|---  
bank_account_name | string | true |  |   
bank_name | string | true |  |   
bank_country | string | true |  |   
bank_address | string | true |  |   
iban | string | true |  |   
swift | string | true |  |   
remittance_line_number | string | false |  |   
agent_bank_name | string | false |  |   
agent_bank_swift | string | false |  |   
documentation_file | string | false |  | Multipart direct upload; mutually exclusive with documentation_file_key  
documentation_file_key | string | false |  | Pre-upload mode; file_key returned by pre_upload (plaintext or base64 accepted)  
file_type | string | false |  | Required when using documentation_file_key; plaintext MIME or its base64  
  
**oneOf[0]**

Request Body SchemaType | Constraints  
---|---  
any | required: ["documentation_file"]  
  
**oneOf[1]**

Request Body SchemaType | Constraints  
---|---  
any | required: ["documentation_file_key","file_type"]  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Accepted successfully | OtcBankCreateResponse  
  
### Response Schema

Status Code **200**

Bank card created successfully (Inner returns bank_id and status).

Type | Constraints  
---|---  
OtcBankCreateResponse | required: ["code","message","data"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
code | integer | Required |  |   
message | string | Required |  |   
data | object | Required | required: ["bank_id","status"] |   
timestamp | integer | Optional |  |   
  
**data**

Type | Constraints  
---|---  
object | required: ["bank_id","status"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
bank_id | integer | Required |  | Bank card primary key in otc_rds.  
status | integer | Required |  | Review status (e.g., pending review).  
  
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
    
    url = '/otc/bank/create'
    query_param = ''
    body='{}'
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
    url="/otc/bank/create"
    query_param=""
    body_param='{}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {}
    
    

> Example responses

> 200 Response
    
    
    {
      "code": 0,
      "message": "string",
      "data": {
        "bank_id": 0,
        "status": 0
      },
      "timestamp": 0
    }
    

##  Delete bank card🔒 Authenticated

POST`/otc/bank/delete`

POST `/otc/bank/delete`

_Delete bank card_

Delete the specified bank card. Corresponds to Inner: `POST /bank/delete`.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | OtcBankIdRequest | Required | none  
bank_id | body | string | Required | Bank card ID  
  
####  Request Body Schema

Request Body SchemaType | Constraints  
---|---  
OtcBankIdRequest | required: ["bank_id"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
bank_id | string | Required |  | Bank card ID  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Deleted successfully | OtcActionResponse  
  
### Response Schema

Status Code **200**

OtcActionResponse

Type | Constraints  
---|---  
OtcActionResponse | required: ["code","message","timestamp"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
code | integer | Required |  |   
message | string | Required |  |   
timestamp | integer | Required |  |   
  
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
    
    url = '/otc/bank/delete'
    query_param = ''
    body='{"bank_id":"string"}'
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
    url="/otc/bank/delete"
    query_param=""
    body_param='{"bank_id":"string"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "bank_id": "string"
    }
    

> Example responses

> 200 Response
    
    
    {
      "code": 0,
      "message": "string",
      "timestamp": 0
    }
    

##  Set default bank card🔒 Authenticated

POST`/otc/bank/set_default`

POST `/otc/bank/set_default`

_Set default bank card_

Set the specified bank card as default. Corresponds to Inner: `POST /bank/set_default`.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | OtcBankIdRequest | Required | none  
bank_id | body | string | Required | Bank card ID  
  
####  Request Body Schema

Request Body SchemaType | Constraints  
---|---  
OtcBankIdRequest | required: ["bank_id"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
bank_id | string | Required |  | Bank card ID  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Set successfully | OtcActionResponse  
  
### Response Schema

Status Code **200**

OtcActionResponse

Type | Constraints  
---|---  
OtcActionResponse | required: ["code","message","timestamp"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
code | integer | Required |  |   
message | string | Required |  |   
timestamp | integer | Required |  |   
  
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
    
    url = '/otc/bank/set_default'
    query_param = ''
    body='{"bank_id":"string"}'
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
    url="/otc/bank/set_default"
    query_param=""
    body_param='{"bank_id":"string"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "bank_id": "string"
    }
    

> Example responses

> 200 Response
    
    
    {
      "code": 0,
      "message": "string",
      "timestamp": 0
    }
    

##  Query the checklist of materials to supplement for a bank card🔒 Authenticated

GET`/otc/bank/bank_supplement_checklist`

GET `/otc/bank/bank_supplement_checklist`

_Query the checklist of materials to supplement for a bank card_

**①** `bank_id` must be specified. After verifying that the card belongs to the current user and its status allows supplementary documents, the endpoint returns the required items based on the user's **approved advanced verification type** (personal/enterprise); each item's `description` states the submission requirements. Corresponding Inner endpoint: `GET /bank/bank_supplement_checklist`.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
bank_id | query | string | Required | Bank card ID (otc_rds / the id returned by the list endpoint).  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | OtcBankSupplementChecklistResponse  
  
### Response Schema

Status Code **200**

OtcBankSupplementChecklistResponse

Type | Constraints  
---|---  
OtcBankSupplementChecklistResponse | required: ["code","message","data"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
code | integer | Required |  |   
message | string | Required |  |   
data | object | Required | required: ["user_type","items"] |   
timestamp | integer | Optional |  |   
  
**data**

Type | Constraints  
---|---  
object | required: ["user_type","items"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
user_type | string | Required | enum: ["personal","enterprise"] | `personal` or `enterprise`, matching the supplementary document submission type; `items[].description` describes the submission requirements for each item  
items | array | Required |  |   
  
**data / items**

Type | Constraints  
---|---  
array |   
  
**data / items / items**

Supplementary document item

Type | Constraints  
---|---  
OtcBankSupplementChecklistItem | required: ["description"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
description | string | Required |  | Supplementary document submission description  
  
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
    
    url = '/otc/bank/bank_supplement_checklist'
    query_param = 'bank_id=string'
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
    url="/otc/bank/bank_supplement_checklist"
    query_param="bank_id=string"
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
        "user_type": "personal",
        "items": [
          {}
        ]
      },
      "timestamp": 0
    }
    

##  Submit Bank Card Supplement Materials (Personal)🔒 Authenticated

POST`/otc/bank/personal/bank_supplement`

POST `/otc/bank/personal/bank_supplement`

_Submit Bank Card Supplement Materials (Personal)_

**Personal professional verification (type=1)** users submit non-same-person/supplementary materials. Must match `user_type=personal` from `GET /otc/bank/bank_supplement_checklist?bank_id=`; otherwise rejected.

Two submission methods (can be mixed):

  1. **Pre-upload (recommended)** : call `POST /otc/upload/pre_upload` (`scene=bank`) to upload to the temporary bucket, then fill file items by category in the `relationship_proof` JSON; pass **`key` as plaintext** object path (`base64_decode(pre_upload.file_key)`, e.g. `otc_temp/{uid}/bank/xxx.png`), and `file_type` as plaintext MIME; the server base64-encodes before persistence—do not pass base64 `file_key` directly;
  2. **Multipart direct upload** : one file field per material item; field names match checklist `code` (`id_document_front`, `id_document_back`, `address_proof`).

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | OtcBankPersonalSupplementMultipartRequest | Required | none  
  
####  Request Body Schema

Personal supplement `multipart/form-data`. File field names are fixed: `id_document_front`, `id_document_back`, `address_proof` (aligned with the checklist `code`); the optional string field `relationship_proof` (JSON text) is merged with the upload result.

Request Body SchemaType | Constraints  
---|---  
OtcBankPersonalSupplementMultipartRequest | required: ["bank_id"]  
  
**Properties**

Request Body SchemaName | Type | Required in this object | Constraints | Description  
---|---|---|---|---  
bank_id | string | true |  |   
id_document_front | string | false |  | ID document front-side file content (multipart file field, binary/Base64)  
id_document_back | string | false |  | ID document back-side file content (multipart file field, binary/Base64)  
address_proof | string | false |  | Proof-of-address file content (multipart file field, binary/Base64)  
relationship_proof | string | false |  | Optional. JSON string of relationship_proof.  
  
**anyOf[0]**

Request Body SchemaType | Constraints  
---|---  
any | required: ["relationship_proof"]  
  
**anyOf[1]**

Request Body SchemaType | Constraints  
---|---  
any | required: ["id_document_front","id_document_back","address_proof"]  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Accepted successfully | OtcActionResponse  
  
### Response Schema

Status Code **200**

OtcActionResponse

Type | Constraints  
---|---  
OtcActionResponse | required: ["code","message","timestamp"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
code | integer | Required |  |   
message | string | Required |  |   
timestamp | integer | Required |  |   
  
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
    
    url = '/otc/bank/personal/bank_supplement'
    query_param = ''
    body='{}'
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
    url="/otc/bank/personal/bank_supplement"
    query_param=""
    body_param='{}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {}
    
    

> Example responses

> 200 Response
    
    
    {
      "code": 0,
      "message": "string",
      "timestamp": 0
    }
    

##  Submit Bank Card Supplement Materials (Enterprise)🔒 Authenticated

POST`/otc/bank/enterprise/bank_supplement`

POST `/otc/bank/enterprise/bank_supplement`

_Submit Bank Card Supplement Materials (Enterprise)_

**Enterprise professional verification (type=2)** users submit supplementary materials. Must match `user_type=enterprise` from the checklist.

Two submission methods (can be mixed):

  1. **Pre-upload (recommended)** : call `POST /otc/upload/pre_upload` (`scene=bank`), fill file items by category in `relationship_proof`; pass **`key` as plaintext** object path (`base64_decode(pre_upload.file_key)`), and `file_type` as plaintext MIME;
  2. **Multipart direct upload** : file field names `certificate`, `share_holders`, `passport`, `share_holding_structure`; optional `funds_statement`, `additional`.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | OtcBankEnterpriseSupplementMultipartRequest | Required | none  
  
####  Request Body Schema

Enterprise supplement `multipart/form-data`. File field names: `certificate`, `share_holders`, `passport`, `share_holding_structure`; optional `funds_statement`, `additional`. Optional string field `relationship_proof` (JSON) is merged into the request.

Request Body SchemaType | Constraints  
---|---  
OtcBankEnterpriseSupplementMultipartRequest | required: ["bank_id"]  
  
**Properties**

Request Body SchemaName | Type | Required in this object | Constraints | Description  
---|---|---|---|---  
uid | string | false |  |   
bank_id | string | true |  |   
certificate | string | false |  | Business license / registration certificate file content (multipart file field, binary/Base64)  
share_holders | string | false |  | Register of shareholders file content (multipart file field, binary/Base64)  
passport | string | false |  | Legal representative / shareholder passport file content (multipart file field, binary/Base64)  
share_holding_structure | string | false |  | Ownership structure chart file content (multipart file field, binary/Base64)  
funds_statement | string | false |  | Proof-of-funds file content (multipart file field, binary/Base64, optional)  
additional | string | false |  | Other supplementary material file content (multipart file field, binary/Base64, optional)  
relationship_proof | string | false |  | Optional. JSON string of relationship_proof.  
  
**anyOf[0]**

Request Body SchemaType | Constraints  
---|---  
any | required: ["relationship_proof"]  
  
**anyOf[1]**

Request Body SchemaType | Constraints  
---|---  
any | required: ["certificate","share_holders","passport","share_holding_structure"]  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Accepted successfully | OtcActionResponse  
  
### Response Schema

Status Code **200**

OtcActionResponse

Type | Constraints  
---|---  
OtcActionResponse | required: ["code","message","timestamp"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
code | integer | Required |  |   
message | string | Required |  |   
timestamp | integer | Required |  |   
  
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
    
    url = '/otc/bank/enterprise/bank_supplement'
    query_param = ''
    body='{}'
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
    url="/otc/bank/enterprise/bank_supplement"
    query_param=""
    body_param='{}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {}
    
    

> Example responses

> 200 Response
    
    
    {
      "code": 0,
      "message": "string",
      "timestamp": 0
    }
    

##  Pre-upload file (temporary bucket)🔒 Authenticated

POST`/otc/upload/pre_upload`

POST `/otc/upload/pre_upload`

_Pre-upload file (temporary bucket)_

After selecting a file, the client calls this endpoint first to obtain a temporary-bucket POST Policy and `file_key`; then upload directly to S3 using the returned `url` and `fields` (success HTTP 204); finally, in business submit endpoints (e.g. `POST /otc/order/paid`, `POST /otc/bank/create`), pass the **same base64`file_key` unchanged** (do not decode). The server validates ownership and object existence, then moves to the production bucket and persists. Unsubmitted files remain in the temporary bucket and are reclaimed by lifecycle rules.

Corresponds to Inner: `POST /upload/pre_upload`.

**`content_type` must be sent as base64** (plaintext containing `/` may be blocked by the gateway). Only the following MIME types are supported:

MIME | base64 | Extension  
---|---|---  
image/png | aW1hZ2UvcG5n | .png  
image/jpeg | aW1hZ2UvanBlZw== | .jpeg  
image/jpg | aW1hZ2UvanBn | .jpg  
application/pdf | YXBwbGljYXRpb24vcGRm | .pdf  
  
**`scene` mapping to downstream endpoints**:

scene | Typical use  
---|---  
general | Fiat buy payment receipt (`payment_receipt_file_key` in `POST /otc/order/paid`)  
bank | Add card, bank card supplementary materials  
assessment | Professional verification materials  
credit | Credit limit increase materials  
  
**Credential validity** : response `expires_in` is **5400 seconds (90 minutes)** ; `fields.Policy` `expiration` matches it. Complete the S3 direct upload within this window; after expiry, call this endpoint again for a new credential.

**File size** : the S3 POST Policy enforces `content-length-range` **1 byte ~ 10MB** (10485760 bytes). Uploads exceeding the limit are rejected by S3; all `scene` values share this limit.

**Direct S3 upload** : `url` is the upload address; send each key-value pair in `fields` unchanged as form-data; the `file` field must be last. Object path is generated as `otc_temp/{uid}/{scene}/{unique filename}`; uid is taken from the login session.

This endpoint returns `content type is required.` when `content_type` is missing. Ownership and object-existence checks for `file_key` are performed by the subsequent business submission endpoint.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | OtcUploadPreUploadRequest | Required | none  
content_type | body | string | Required | **Base64** of the file MIME type, required. Only image/png, image/jpeg, image/jpg, and application/pdf are supported.  
scene | body | string | Optional | Business scene, optional, defaults to general; determines temporary path and production directory after relocation  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
content_type | aW1hZ2UvcG5n  
content_type | aW1hZ2UvanBlZw==  
content_type | aW1hZ2UvanBn  
content_type | YXBwbGljYXRpb24vcGRm  
scene | general  
scene | bank  
scene | assessment  
scene | credit  
  
####  Request Body Schema

File pre-upload request body

Request Body SchemaType | Constraints  
---|---  
OtcUploadPreUploadRequest | required: ["content_type"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
content_type | string | Required | enum: ["aW1hZ2UvcG5n","aW1hZ2UvanBlZw==","aW1hZ2UvanBn","YXBwbGljYXRpb24vcGRm"] | **Base64** of the file MIME type, required. Only image/png, image/jpeg, image/jpg, and application/pdf are supported.  
scene | string | Optional | enum: ["general","bank","assessment","credit"]  
default: "general" | Business scene, optional, defaults to general; determines temporary path and production directory after relocation  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Pre-upload credentials issued successfully | OtcUploadPreUploadResponse  
  
### Response Schema

Status Code **200**

OtcUploadPreUploadResponse

Type | Constraints  
---|---  
OtcUploadPreUploadResponse | required: ["code","message","data","timestamp"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
code | integer | Required |  | 0 success; 10010400 parameter error  
message | string | Required |  | Response message  
data | OtcUploadPreUploadData | Required | required: ["file_key","url","fields","expires_in"] | Pre-upload credentials and S3 direct-upload parameters  
timestamp | integer | Required |  | Response timestamp (in seconds)  
  
**data**

Pre-upload credentials and S3 direct-upload parameters

Type | Constraints  
---|---  
OtcUploadPreUploadData | required: ["file_key","url","fields","expires_in"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
file_key | string | Required |  | Base64 temporary object path; pass back **unchanged** on business submit—do not decode  
url | string | Required |  | S3 direct upload URL  
fields | OtcUploadPreUploadPolicyFields | Required | required: ["key","Content-Type","X-Amz-Credential","X-Amz-Algorithm","X-Amz-Date","Policy","X-Amz-Signature"] | S3 POST Policy signature fields; send unchanged as form-data during direct upload  
expires_in | integer | Required |  | Policy validity period in seconds; currently 5400 (90 minutes); aligns with `expiration` in `fields.Policy`; call this endpoint again after expiry  
  
**data / fields**

S3 POST Policy signature fields; send unchanged as form-data during direct upload

Type | Constraints  
---|---  
OtcUploadPreUploadPolicyFields | required: ["key","Content-Type","X-Amz-Credential","X-Amz-Algorithm","X-Amz-Date","Policy","X-Amz-Signature"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
key | string | Required |  | Plaintext temporary object path, identical to base64_decode(file_key)  
Content-Type | string | Required |  | Must match the decoded content_type from the pre-upload request  
X-Amz-Credential | string | Required |  | AWS temporary credential and scope; submit them unchanged during direct upload  
X-Amz-Algorithm | string | Required |  | AWS signing algorithm; submit it unchanged during direct upload  
X-Amz-Date | string | Required |  | AWS signing timestamp; submit it unchanged during direct upload  
Policy | string | Required |  | Base64-encoded S3 POST Policy; submit it unchanged during direct upload  
X-Amz-Signature | string | Required |  | S3 POST Policy signature; submit it unchanged during direct upload  
  
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
    
    url = '/otc/upload/pre_upload'
    query_param = ''
    body='{"content_type":"aW1hZ2UvcG5n","scene":"bank"}'
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
    url="/otc/upload/pre_upload"
    query_param=""
    body_param='{"content_type":"aW1hZ2UvcG5n","scene":"bank"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "content_type": "aW1hZ2UvcG5n",
      "scene": "bank"
    }
    

> Example responses

> 200 Response
    
    
    {
      "code": 0,
      "message": "success",
      "data": {
        "file_key": "b3RjX3RlbXAvMTIzNDU2Nzg5MC9iYW5rLzIwMjYwODMxMDc1MTI1MjgyMjMzOTQ1OS5wbmc=",
        "url": "https://example-bucket.s3.us-east-2.amazonaws.com",
        "fields": {
          "key": "otc_temp/1234567890/bank/202608310751252822339459.png",
          "Content-Type": "image/png",
          "X-Amz-Credential": "AKIAEXAMPLE/20260831/us-east-2/s3/aws4_request",
          "X-Amz-Algorithm": "AWS4-HMAC-SHA256",
          "X-Amz-Date": "20260831T075125Z",
          "Policy": "eyJleHBpcmF0aW9uIjoiMjAyNi0wOC0zMVQwOToyMToyNVoiLCJjb25kaXRpb25zIjpbWyJjb250ZW50LWxlbmd0aC1yYW5nZSIsMSwxMDQ4NTc2MF1dfQ==",
          "X-Amz-Signature": "EXAMPLE_SIGNATURE"
        },
        "expires_in": 5400
      },
      "timestamp": 1788162685
    }
    

##  Mark fiat order as paid (deposit confirmation)🔒 Authenticated

POST`/otc/order/paid`

POST `/otc/order/paid`

_Mark fiat order as paid (deposit confirmation)_

Mark a fiat buy order as paid (deposit confirmation). **A user payment receipt must be uploaded** : `payment_receipt_file_key` is required; supported formats are jpg / jpeg / png / pdf, with a maximum size of 10 MB per file (validated jointly by the service and gateway). The compatible field name `payment_receipt` depends on the gateway and production contract. The persisted field is `otc_trade_record.payment_receipt_file_key`. The Pay Inner path is `POST .../pay/order_set_paid` (which commonly identifies orders by `client_order_id`); the Inner path corresponding to this OpenAPI operation, `POST /order/paid`, still primarily uses `order_id`. If the gateway standardizes on the merchant order ID, follow the gateway documentation.

**Recommended pre-upload flow** : first call `POST /otc/upload/pre_upload` (`scene=general`) and upload directly to the temporary bucket, then pass the returned **base64`file_key` unchanged** (do not decode) to this endpoint. The service validates the uid and object existence before moving the object to the production bucket. A cross-user key returns `Invalid parameters file_key`; an object that has not been uploaded returns `Invalid parameters file not uploaded`. The legacy flow using a base64 key for an object uploaded directly to the production bucket remains supported.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | OtcMarkOrderPaidRequest | Required | none  
order_id | body | string | Required | Order ID  
client_order_id | body | string | Optional | Client order ID (used by some gateway/Inner Pay paths, optional)  
payment_receipt_file_key | body | string | Required | User payment receipt: **required**. Recommended: call `POST /otc/upload/pre_upload` (`scene=general`) to upload to the temporary bucket, then pass the returned **base64 file_key unchanged** (do not decode); the server moves to the production bucket and persists. Still compatible with legacy production-bucket base64 keys. Single file; jpg/jpeg/png/pdf; ≤10MB.  
payment_receipt | body | string | Optional | Alias compatible with `payment_receipt_file_key` (depends on the gateway's external field name)  
  
####  Request Body Schema

Request body for marking a fiat order as paid (deposit confirmation). Must include the user's payment receipt (consistent with §3.2). **`payment_receipt_file_key` is required**; the order primary key for this path is `order_id`. When accessed via the Pay gateway using `client_order_id`, the gateway's rewritten field prevails.

Request Body SchemaType | Constraints  
---|---  
OtcMarkOrderPaidRequest | required: ["order_id","payment_receipt_file_key"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
order_id | string | Required |  | Order ID  
client_order_id | string | Optional |  | Client order ID (used by some gateway/Inner Pay paths, optional)  
payment_receipt_file_key | string | Required |  | User payment receipt: **required**. Recommended: call `POST /otc/upload/pre_upload` (`scene=general`) to upload to the temporary bucket, then pass the returned **base64 file_key unchanged** (do not decode); the server moves to the production bucket and persists. Still compatible with legacy production-bucket base64 keys. Single file; jpg/jpeg/png/pdf; ≤10MB.  
payment_receipt | string | Optional |  | Alias compatible with `payment_receipt_file_key` (depends on the gateway's external field name)  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | The order has been marked as paid | OtcActionResponse  
  
### Response Schema

Status Code **200**

OtcActionResponse

Type | Constraints  
---|---  
OtcActionResponse | required: ["code","message","timestamp"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
code | integer | Required |  |   
message | string | Required |  |   
timestamp | integer | Required |  |   
  
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
    body='{"order_id":"203","client_order_id":"","payment_receipt_file_key":"b3RjX3RlbXAvMTIzNDU2Nzg5MC9nZW5lcmFsLzIwMjYwODMxMjEwMDEyMzQ1Njc4LnBuZw==","payment_receipt":""}'
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
    body_param='{"order_id":"203","client_order_id":"","payment_receipt_file_key":"b3RjX3RlbXAvMTIzNDU2Nzg5MC9nZW5lcmFsLzIwMjYwODMxMjEwMDEyMzQ1Njc4LnBuZw==","payment_receipt":""}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "order_id": "203",
      "client_order_id": "",
      "payment_receipt_file_key": "b3RjX3RlbXAvMTIzNDU2Nzg5MC9nZW5lcmFsLzIwMjYwODMxMjEwMDEyMzQ1Njc4LnBuZw==",
      "payment_receipt": ""
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

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Order cancelled successfully | OtcActionResponse  
  
### Response Schema

Status Code **200**

OtcActionResponse

Type | Constraints  
---|---  
OtcActionResponse | required: ["code","message","timestamp"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
code | integer | Required |  |   
message | string | Required |  |   
timestamp | integer | Required |  |   
  
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
type | query | string | Optional | BUY for on-ramp, SELL for off-ramp  
fiat_currency | query | string | Optional | Fiat currency  
crypto_currency | query | string | Optional | Digital currency  
start_time | query | string | Optional | starttime for example : 2025-09-09  
end_time | query | string | Optional | endtime for example :2025-09-09  
status | query | string | Optional | DONE: completed  
CANCEL: canceled  
PROCESSING: in progress  
DISBURSED: disbursed  
pn | query | string | Optional | Page number  
ps | query | string | Optional | Number of items per page  
  
####  Detailed descriptions

**status** : DONE: completed  
CANCEL: canceled  
PROCESSING: in progress  
DISBURSED: disbursed

### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | OtcOrderListResponse  
  
### Response Schema

Status Code **200**

OtcOrderListResponse

Type | Constraints  
---|---  
OtcOrderListResponse | required: ["code","message","data"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
code | integer | Required |  |   
message | string | Required |  |   
data | object | Required | required: ["pn","ps","total_pn","count","lists"] |   
  
**data**

OtcOrderListResult

Type | Constraints  
---|---  
object | required: ["pn","ps","total_pn","count","lists"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
pn | integer | Required |  |   
ps | integer | Required |  |   
total_pn | integer | Required |  |   
count | integer | Required |  |   
lists | array | Required |  |   
  
**data / lists**

Type | Constraints  
---|---  
array |   
  
**data / lists / items**

OtcOrderListItem

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
time | string | Optional |  | Current time  
timestamp | integer | Optional |  | Current timestamp  
order_id | string | Optional |  | orderId  
trade_no | string | Optional |  | Trade number  
type | string | Optional |  | BUY deposit / SELL withdrawal  
status | string | Optional |  | Order status  
fiat_currency | string | Optional |  | Fiat currency  
fiat_currency_info | object | Optional | required: ["name","icon"] |   
fiat_amount | string | Optional |  | Fiat amount  
crypto_currency | string | Optional |  | Digital currency  
crypto_currency_info | object | Optional | required: ["name","icon"] |   
crypto_amount | string | Optional |  | Cryptocurrency amount  
rate | string | Optional |  | Exchange rate  
promotion_code | string | Optional |  | Promotion code  
  
**data / lists / items / fiat_currency_info**

OtcOrderListFiatCurrencyInfo

Type | Constraints  
---|---  
object | required: ["name","icon"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
name | string | Required |  | Name  
icon | string | Required |  | Image  
  
**data / lists / items / crypto_currency_info**

OtcOrderListCryptoCurrencyInfo

Type | Constraints  
---|---  
object | required: ["name","icon"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
name | string | Required |  |   
icon | string | Required |  |   
  
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
        "lists": [
          {
            "time": "2025-02-11 07:45:06",
            "timestamp": 1739000013,
            "order_id": "41",
            "trade_no": "20250207043457590939",
            "type": "SELL",
            "status": "PROCESSING",
            "fiat_currency": "USD",
            "fiat_currency_info": {
              "name": "USD",
              "icon": "http://icon.url"
            },
            "fiat_amount": "199600",
            "crypto_currency": "USDT",
            "crypto_currency_info": {
              "name": "USDT",
              "icon": "http://icon.url"
            },
            "crypto_amount": "200000",
            "rate": "0.998000",
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

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | OtcStableCoinOrderListResponse  
  
### Response Schema

Status Code **200**

OtcStableCoinOrderListResponse

Type | Constraints  
---|---  
OtcStableCoinOrderListResponse | required: ["code","message","data"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
code | integer | Required |  |   
message | string | Required |  |   
data | object | Required | required: ["total","page_size","page_number","total_page","lists"] |   
  
**data**

OtcStableCoinOrderListResult

Type | Constraints  
---|---  
object | required: ["total","page_size","page_number","total_page","lists"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
total | integer | Required |  |   
page_size | integer | Required |  |   
page_number | integer | Required |  |   
total_page | integer | Required |  |   
lists | array | Required |  |   
  
**data / lists**

Type | Constraints  
---|---  
array |   
  
**data / lists / items**

OtcStableCoinOrderListItem

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | integer | Optional |  | Order ID  
trade_no | string | Optional |  | Transaction reference number  
pay_coin | string | Optional |  | Payment currency  
pay_icon | string | Optional |  | Payment currency icon  
pay_amount | string | Optional |  | Payment amount  
get_coin | string | Optional |  | Received currency  
get_icon | string | Optional |  | Received currency icon  
get_amount | string | Optional |  | Received amount  
rate | string | Optional |  | Exchange rate  
rate_reci | string | Optional |  | Reciprocal of the exchange rate  
status | string | Optional |  | PROCESSING: in progress / DONE: completed / FAILED: failed  
create_timest | integer | Optional |  | Created time  
create_time | string | Optional |  | Created time  
  
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
        "lists": [
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

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | OtcOrderDetailResponse  
  
### Response Schema

Status Code **200**

OtcOrderDetailResponse

Type | Constraints  
---|---  
OtcOrderDetailResponse | required: ["message","code","data"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
message | string | Required |  |   
code | integer | Required |  |   
data | object | Required | required: ["order_id","uid","type","fiat_currency","fiat_amount","crypto_currency","crypto_amount","rate","status","create_time"] |   
  
**data**

OtcOrderDetail

Type | Constraints  
---|---  
object | required: ["order_id","uid","type","fiat_currency","fiat_amount","crypto_currency","crypto_amount","rate","status","create_time"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
order_id | string | Required |  | Order ID  
uid | string | Required |  | User ID  
type | string | Required |  | Order Type  
fiat_currency | string | Required |  | Fiat currency  
fiat_amount | string | Required |  | Fiat amount  
crypto_currency | string | Required |  | Digital currency  
crypto_amount | string | Required |  | Cryptocurrency amount  
rate | string | Required |  | Exchange rate  
bank_account_name | string | Optional |  | User payment/receiving name  
bank_name | string | Optional |  | User payment/receiving bank name  
bank_country | string | Optional |  | User payment/receiving bank country  
bank_address | string | Optional |  | User payment/receiving bank address  
bank_account_number_iban | string | Optional |  | User payment/receiving bank account number/IBAN  
swift_code | string | Optional |  | User payment/receiving bank SWIFT code  
intermediate_bank_name | string | Optional |  | User payment/receiving intermediary bank name  
intermediary_bank_swift_code | string | Optional |  | User payment/receiving intermediary bank SWIFT code  
gate_bank_account_name | string | Optional |  | Gate beneficiary name, shown for BUY only  
gate_bank_name | string | Optional |  | Gate beneficiary bank name, shown for BUY only  
gate_bank_country | string | Optional |  | Gate beneficiary bank country, shown for BUY only  
gate_bank_address | string | Optional |  | Gate beneficiary bank address, shown for BUY only  
gate_bank_account_number_iban | string | Optional |  | Gate beneficiary bank account number/IBAN, shown for BUY only  
gate_swift_code | string | Optional |  | Gate beneficiary bank SWIFT code, shown for BUY only  
gate_intermediary_bank_name | string | Optional |  | Gate beneficiary intermediary bank name, shown for BUY only  
gate_intermediary_bank_swift_code | string | Optional |  | Gate beneficiary intermediary bank SWIFT code, shown for BUY only  
gate_transfer_remark | string | Optional |  | Transfer remark (mutually exclusive with `gate_reference_code`; empty when a BUY deposit order has a reference code), shown for BUY only  
gate_reference_code | string | Optional |  | Be sure to include the reference code when making the transfer so that your order can be processed promptly. (Mutually exclusive with `gate_transfer_remark`.)  
status | string | Required |  | Status  
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
        "bank_account_name": "",
        "bank_name": "",
        "bank_country": "",
        "bank_address": "",
        "bank_account_number_iban": "",
        "swift_code": "",
        "intermediate_bank_name": "",
        "intermediary_bank_swift_code": "",
        "gate_bank_account_name": "",
        "gate_bank_name": "",
        "gate_bank_country": "",
        "gate_bank_address": "",
        "gate_bank_account_number_iban": "",
        "gate_swift_code": "",
        "gate_intermediary_bank_name": "",
        "gate_intermediary_bank_swift_code": "",
        "gate_transfer_remark": "",
        "gate_reference_code": "OTIK7M39QF42",
        "status": "PROCESSING",
        "create_time": "2025-03-07 07:51:52"
      },
      "timestamp": 1752051076
    }
    

#  Schemas

##  OtcBankCreateResponse

Bank card created successfully (Inner returns bank_id and status).

Type | Constraints  
---|---  
object | required: ["code","message","data"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
code | integer | Required |  |   
message | string | Required |  |   
data | object | Required | required: ["bank_id","status"] |   
timestamp | integer | Optional |  |   
  
**data**

Type | Constraints  
---|---  
object | required: ["bank_id","status"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
bank_id | integer | Required |  | Bank card primary key in otc_rds.  
status | integer | Required |  | Review status (e.g., pending review).  
      
    
    {
      "code": 0,
      "message": "string",
      "data": {
        "bank_id": 0,
        "status": 0
      },
      "timestamp": 0
    }
    
    

##  OtcBankPersonalSupplementMultipartRequest

Personal supplement `multipart/form-data`. File field names are fixed: `id_document_front`, `id_document_back`, `address_proof` (aligned with the checklist `code`); the optional string field `relationship_proof` (JSON text) is merged with the upload result.

Type | Constraints  
---|---  
object | required: ["bank_id"]  
  
**Properties**

Name | Type | Required in this object | Constraints | Description  
---|---|---|---|---  
bank_id | string | true |  |   
id_document_front | string | false |  | ID document front-side file content (multipart file field, binary/Base64)  
id_document_back | string | false |  | ID document back-side file content (multipart file field, binary/Base64)  
address_proof | string | false |  | Proof-of-address file content (multipart file field, binary/Base64)  
relationship_proof | string | false |  | Optional. JSON string of relationship_proof.  
  
**anyOf[0]**

Type | Constraints  
---|---  
any | required: ["relationship_proof"]  
  
**anyOf[1]**

Type | Constraints  
---|---  
any | required: ["id_document_front","id_document_back","address_proof"]  
      
    
    {}
    
    

##  OtcStableCoinOrderCreateResponse

OtcStableCoinOrderCreateResponse

Type | Constraints  
---|---  
object | required: ["code","message","timestamp"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
code | integer | Required |  | Business code; 0 indicates success  
message | string | Required |  | Message  
timestamp | integer | Required |  | Server Unix timestamp in seconds  
      
    
    {
      "code": 0,
      "message": "string",
      "timestamp": 0
    }
    
    

##  OtcUploadPreUploadRequest

File pre-upload request body

Type | Constraints  
---|---  
object | required: ["content_type"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
content_type | string | Required | enum: ["aW1hZ2UvcG5n","aW1hZ2UvanBlZw==","aW1hZ2UvanBn","YXBwbGljYXRpb24vcGRm"] | **Base64** of the file MIME type, required. Only image/png, image/jpeg, image/jpg, and application/pdf are supported.  
scene | string | Optional | enum: ["general","bank","assessment","credit"]  
default: "general" | Business scene, optional, defaults to general; determines temporary path and production directory after relocation  
      
    
    {
      "content_type": "aW1hZ2UvcG5n",
      "scene": "bank"
    }
    
    

##  OtcActionResponse

OtcActionResponse

Type | Constraints  
---|---  
object | required: ["code","message","timestamp"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
code | integer | Required |  |   
message | string | Required |  |   
timestamp | integer | Required |  |   
      
    
    {
      "code": 0,
      "message": "string",
      "timestamp": 0
    }
    
    

##  OtcBankIdRequest

Type | Constraints  
---|---  
object | required: ["bank_id"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
bank_id | string | Required |  | Bank card ID  
      
    
    {
      "bank_id": "string"
    }
    
    

##  OtcBankCreateMultipartRequest

Inner create-bank-card `multipart/form-data`. Account-opening proof file (choose one):

  * **Pre-upload** : `documentation_file_key` \+ `file_type` (call `POST /otc/upload/pre_upload` first, `scene=bank`);
  * **Multipart direct upload** : `documentation_file` file field.

Type | Constraints  
---|---  
object | required: ["bank_account_name","bank_name","bank_country","bank_address","iban","swift"]  
  
**Properties**

Name | Type | Required in this object | Constraints | Description  
---|---|---|---|---  
bank_account_name | string | true |  |   
bank_name | string | true |  |   
bank_country | string | true |  |   
bank_address | string | true |  |   
iban | string | true |  |   
swift | string | true |  |   
remittance_line_number | string | false |  |   
agent_bank_name | string | false |  |   
agent_bank_swift | string | false |  |   
documentation_file | string | false |  | Multipart direct upload; mutually exclusive with documentation_file_key  
documentation_file_key | string | false |  | Pre-upload mode; file_key returned by pre_upload (plaintext or base64 accepted)  
file_type | string | false |  | Required when using documentation_file_key; plaintext MIME or its base64  
  
**oneOf[0]**

Type | Constraints  
---|---  
any | required: ["documentation_file"]  
  
**oneOf[1]**

Type | Constraints  
---|---  
any | required: ["documentation_file_key","file_type"]  
      
    
    {}
    
    

##  OtcBankListResponse

OtcBankListResponse

Type | Constraints  
---|---  
object | required: ["code","message","data","timestamp"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
code | integer | Required |  |   
message | string | Required |  |   
data | object | Required | required: ["lists"] |   
timestamp | integer | Required |  |   
  
**data**

OtcBankListResult

Type | Constraints  
---|---  
object | required: ["lists"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
lists | array | Required |  | Bank card list  
  
**data / lists**

Bank card list

Type | Constraints  
---|---  
array |   
  
**data / lists / items**

OtcBankListItem

Type | Constraints  
---|---  
object | required: ["id","bank_account_name","bank_name"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | string | Required |  | Bank card ID (used when placing an order; the synonymous `bank_id` field has been consolidated into `id`)  
bank_account_name | string | Required |  | Bank account name  
bank_name | string | Required |  | Bank name  
bank_country | string | Optional |  | Bank country  
bank_address | string | Optional |  | Bank address  
iban | string | Optional |  | IBAN number  
swift | string | Optional |  | SWIFT code  
remittance_line_number | string | Optional |  | Remittance routing number  
agent_bank_name | string | Optional |  | Correspondent bank name  
agent_bank_swift | string | Optional |  | Correspondent bank SWIFT code  
submit_time | string | Optional |  | Submission time  
update_time | string | Optional |  | Update time  
status | string | Optional |  | Status  
is_default | integer | Optional |  | Whether it is the default bank card. 1 - Yes, 0 - No  
      
    
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
    
    

##  OtcStableCoinOrderRequest

Stablecoin Order Request Body

Type | Constraints  
---|---  
object | required: ["pay_coin","get_coin","pay_amount","get_amount","side","quote_token"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
pay_coin | string | Required |  | Currency paid by the user. Supported currencies can be queried from the OTC web stablecoin quote page.  
get_coin | string | Required |  | Currency to be received by the user. Supported currencies can be queried from the OTC web stablecoin quote page.  
pay_amount | string | Required |  | User payment currency amount  
get_amount | string | Required |  | Amount of currency received by the user  
side | string | Required |  | The side returned by the quote endpoint (used for order validation). For backward compatibility, `PAY`/`GET` are accepted; new integrations should use the value returned by the quote response.  
promotion_code | string | Optional |  | Promotion code (optional)  
quote_token | string | Required |  | Parameter returned by the quote API  
      
    
    {
      "pay_coin": "USDC",
      "get_coin": "USDT",
      "pay_amount": "30000",
      "get_amount": "20000",
      "side": "PAY",
      "promotion_code": "",
      "quote_token": "dsafjkdshfjdsjkfah"
    }
    
    

##  OtcOrderListResponse

OtcOrderListResponse

Type | Constraints  
---|---  
object | required: ["code","message","data"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
code | integer | Required |  |   
message | string | Required |  |   
data | object | Required | required: ["pn","ps","total_pn","count","lists"] |   
  
**data**

OtcOrderListResult

Type | Constraints  
---|---  
object | required: ["pn","ps","total_pn","count","lists"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
pn | integer | Required |  |   
ps | integer | Required |  |   
total_pn | integer | Required |  |   
count | integer | Required |  |   
lists | array | Required |  |   
  
**data / lists**

Type | Constraints  
---|---  
array |   
  
**data / lists / items**

OtcOrderListItem

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
time | string | Optional |  | Current time  
timestamp | integer | Optional |  | Current timestamp  
order_id | string | Optional |  | orderId  
trade_no | string | Optional |  | Trade number  
type | string | Optional |  | BUY deposit / SELL withdrawal  
status | string | Optional |  | Order status  
fiat_currency | string | Optional |  | Fiat currency  
fiat_currency_info | object | Optional | required: ["name","icon"] |   
fiat_amount | string | Optional |  | Fiat amount  
crypto_currency | string | Optional |  | Digital currency  
crypto_currency_info | object | Optional | required: ["name","icon"] |   
crypto_amount | string | Optional |  | Cryptocurrency amount  
rate | string | Optional |  | Exchange rate  
promotion_code | string | Optional |  | Promotion code  
  
**data / lists / items / fiat_currency_info**

OtcOrderListFiatCurrencyInfo

Type | Constraints  
---|---  
object | required: ["name","icon"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
name | string | Required |  | Name  
icon | string | Required |  | Image  
  
**data / lists / items / crypto_currency_info**

OtcOrderListCryptoCurrencyInfo

Type | Constraints  
---|---  
object | required: ["name","icon"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
name | string | Required |  |   
icon | string | Required |  |   
      
    
    {
      "code": 0,
      "message": "string",
      "data": {
        "pn": 0,
        "ps": 0,
        "total_pn": 0,
        "count": 0,
        "lists": [
          {}
        ]
      }
    }
    
    

##  OtcOrderDetailResponse

OtcOrderDetailResponse

Type | Constraints  
---|---  
object | required: ["message","code","data"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
message | string | Required |  |   
code | integer | Required |  |   
data | object | Required | required: ["order_id","uid","type","fiat_currency","fiat_amount","crypto_currency","crypto_amount","rate","status","create_time"] |   
  
**data**

OtcOrderDetail

Type | Constraints  
---|---  
object | required: ["order_id","uid","type","fiat_currency","fiat_amount","crypto_currency","crypto_amount","rate","status","create_time"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
order_id | string | Required |  | Order ID  
uid | string | Required |  | User ID  
type | string | Required |  | Order Type  
fiat_currency | string | Required |  | Fiat currency  
fiat_amount | string | Required |  | Fiat amount  
crypto_currency | string | Required |  | Digital currency  
crypto_amount | string | Required |  | Cryptocurrency amount  
rate | string | Required |  | Exchange rate  
bank_account_name | string | Optional |  | User payment/receiving name  
bank_name | string | Optional |  | User payment/receiving bank name  
bank_country | string | Optional |  | User payment/receiving bank country  
bank_address | string | Optional |  | User payment/receiving bank address  
bank_account_number_iban | string | Optional |  | User payment/receiving bank account number/IBAN  
swift_code | string | Optional |  | User payment/receiving bank SWIFT code  
intermediate_bank_name | string | Optional |  | User payment/receiving intermediary bank name  
intermediary_bank_swift_code | string | Optional |  | User payment/receiving intermediary bank SWIFT code  
gate_bank_account_name | string | Optional |  | Gate beneficiary name, shown for BUY only  
gate_bank_name | string | Optional |  | Gate beneficiary bank name, shown for BUY only  
gate_bank_country | string | Optional |  | Gate beneficiary bank country, shown for BUY only  
gate_bank_address | string | Optional |  | Gate beneficiary bank address, shown for BUY only  
gate_bank_account_number_iban | string | Optional |  | Gate beneficiary bank account number/IBAN, shown for BUY only  
gate_swift_code | string | Optional |  | Gate beneficiary bank SWIFT code, shown for BUY only  
gate_intermediary_bank_name | string | Optional |  | Gate beneficiary intermediary bank name, shown for BUY only  
gate_intermediary_bank_swift_code | string | Optional |  | Gate beneficiary intermediary bank SWIFT code, shown for BUY only  
gate_transfer_remark | string | Optional |  | Transfer remark (mutually exclusive with `gate_reference_code`; empty when a BUY deposit order has a reference code), shown for BUY only  
gate_reference_code | string | Optional |  | Be sure to include the reference code when making the transfer so that your order can be processed promptly. (Mutually exclusive with `gate_transfer_remark`.)  
status | string | Required |  | Status  
create_time | string | Required |  | Created time  
      
    
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
        "bank_account_name": "string",
        "bank_name": "string",
        "bank_country": "string",
        "bank_address": "string",
        "bank_account_number_iban": "string",
        "swift_code": "string",
        "intermediate_bank_name": "string",
        "intermediary_bank_swift_code": "string",
        "gate_bank_account_name": "string",
        "gate_bank_name": "string",
        "gate_bank_country": "string",
        "gate_bank_address": "string",
        "gate_bank_account_number_iban": "string",
        "gate_swift_code": "string",
        "gate_intermediary_bank_name": "string",
        "gate_intermediary_bank_swift_code": "string",
        "gate_transfer_remark": "string",
        "gate_reference_code": "string",
        "status": "string",
        "create_time": "string"
      }
    }
    
    

##  OtcMarkOrderPaidRequest

Request body for marking a fiat order as paid (deposit confirmation). Must include the user's payment receipt (consistent with §3.2). **`payment_receipt_file_key` is required**; the order primary key for this path is `order_id`. When accessed via the Pay gateway using `client_order_id`, the gateway's rewritten field prevails.

Type | Constraints  
---|---  
object | required: ["order_id","payment_receipt_file_key"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
order_id | string | Required |  | Order ID  
client_order_id | string | Optional |  | Client order ID (used by some gateway/Inner Pay paths, optional)  
payment_receipt_file_key | string | Required |  | User payment receipt: **required**. Recommended: call `POST /otc/upload/pre_upload` (`scene=general`) to upload to the temporary bucket, then pass the returned **base64 file_key unchanged** (do not decode); the server moves to the production bucket and persists. Still compatible with legacy production-bucket base64 keys. Single file; jpg/jpeg/png/pdf; ≤10MB.  
payment_receipt | string | Optional |  | Alias compatible with `payment_receipt_file_key` (depends on the gateway's external field name)  
      
    
    {
      "order_id": "203",
      "client_order_id": "",
      "payment_receipt_file_key": "b3RjX3RlbXAvMTIzNDU2Nzg5MC9nZW5lcmFsLzIwMjYwODMxMjEwMDEyMzQ1Njc4LnBuZw==",
      "payment_receipt": ""
    }
    
    

##  OtcStableCoinOrderListResponse

OtcStableCoinOrderListResponse

Type | Constraints  
---|---  
object | required: ["code","message","data"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
code | integer | Required |  |   
message | string | Required |  |   
data | object | Required | required: ["total","page_size","page_number","total_page","lists"] |   
  
**data**

OtcStableCoinOrderListResult

Type | Constraints  
---|---  
object | required: ["total","page_size","page_number","total_page","lists"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
total | integer | Required |  |   
page_size | integer | Required |  |   
page_number | integer | Required |  |   
total_page | integer | Required |  |   
lists | array | Required |  |   
  
**data / lists**

Type | Constraints  
---|---  
array |   
  
**data / lists / items**

OtcStableCoinOrderListItem

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | integer | Optional |  | Order ID  
trade_no | string | Optional |  | Transaction reference number  
pay_coin | string | Optional |  | Payment currency  
pay_icon | string | Optional |  | Payment currency icon  
pay_amount | string | Optional |  | Payment amount  
get_coin | string | Optional |  | Received currency  
get_icon | string | Optional |  | Received currency icon  
get_amount | string | Optional |  | Received amount  
rate | string | Optional |  | Exchange rate  
rate_reci | string | Optional |  | Reciprocal of the exchange rate  
status | string | Optional |  | PROCESSING: in progress / DONE: completed / FAILED: failed  
create_timest | integer | Optional |  | Created time  
create_time | string | Optional |  | Created time  
      
    
    {
      "code": 0,
      "message": "string",
      "data": {
        "total": 0,
        "page_size": 0,
        "page_number": 0,
        "total_page": 0,
        "lists": [
          {}
        ]
      }
    }
    
    

##  OtcUploadPreUploadResponse

OtcUploadPreUploadResponse

Type | Constraints  
---|---  
object | required: ["code","message","data","timestamp"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
code | integer | Required |  | 0 success; 10010400 parameter error  
message | string | Required |  | Response message  
data | OtcUploadPreUploadData | Required | required: ["file_key","url","fields","expires_in"] | Pre-upload credentials and S3 direct-upload parameters  
timestamp | integer | Required |  | Response timestamp (in seconds)  
      
    
    {
      "code": 0,
      "message": "string",
      "data": {
        "file_key": "string",
        "url": "string",
        "fields": {
          "key": "string",
          "Content-Type": "string",
          "X-Amz-Credential": "string",
          "X-Amz-Algorithm": "string",
          "X-Amz-Date": "string",
          "Policy": "string",
          "X-Amz-Signature": "string"
        },
        "expires_in": 0
      },
      "timestamp": 0
    }
    
    

##  OtcQuoteRequest

Fiat and Stablecoin Quote Request Body

Type | Constraints  
---|---  
object | required: ["side","pay_coin","get_coin"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
side | string | Required |  | PAY: specify the payment amount (`pay_amount` is required); GET: specify the receive amount (`get_amount` is required).  
pay_coin | string | Required |  | Payment currency. Supported currencies are available on the OTC web quote page.  
get_coin | string | Required |  | Receive currency. Supported currencies are available on the OTC web quote page.  
pay_amount | string | Optional |  | User payment currency amount  
get_amount | string | Optional |  | Amount of currency received by the user  
create_quote_token | string | Optional |  | Create quote token: 0: quote preview only; 1: generate quote token for order placement.  
promotion_code | string | Optional |  | Promotion code  
      
    
    {
      "side": "PAY",
      "pay_coin": "USDT",
      "get_coin": "USD",
      "pay_amount": "30000",
      "get_amount": "30000",
      "create_quote_token": "0",
      "promotion_code": ""
    }
    
    

##  OtcBankSupplementChecklistResponse

OtcBankSupplementChecklistResponse

Type | Constraints  
---|---  
object | required: ["code","message","data"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
code | integer | Required |  |   
message | string | Required |  |   
data | object | Required | required: ["user_type","items"] |   
timestamp | integer | Optional |  |   
  
**data**

Type | Constraints  
---|---  
object | required: ["user_type","items"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
user_type | string | Required | enum: ["personal","enterprise"] | `personal` or `enterprise`, matching the supplementary document submission type; `items[].description` describes the submission requirements for each item  
items | array | Required |  |   
  
**data / items**

Type | Constraints  
---|---  
array |   
  
**data / items / items**

Supplementary document item

Type | Constraints  
---|---  
OtcBankSupplementChecklistItem | required: ["description"]  
      
    
    {
      "code": 0,
      "message": "string",
      "data": {
        "user_type": "personal",
        "items": [
          {}
        ]
      },
      "timestamp": 0
    }
    
    

##  OtcBankEnterpriseSupplementMultipartRequest

Enterprise supplement `multipart/form-data`. File field names: `certificate`, `share_holders`, `passport`, `share_holding_structure`; optional `funds_statement`, `additional`. Optional string field `relationship_proof` (JSON) is merged into the request.

Type | Constraints  
---|---  
object | required: ["bank_id"]  
  
**Properties**

Name | Type | Required in this object | Constraints | Description  
---|---|---|---|---  
uid | string | false |  |   
bank_id | string | true |  |   
certificate | string | false |  | Business license / registration certificate file content (multipart file field, binary/Base64)  
share_holders | string | false |  | Register of shareholders file content (multipart file field, binary/Base64)  
passport | string | false |  | Legal representative / shareholder passport file content (multipart file field, binary/Base64)  
share_holding_structure | string | false |  | Ownership structure chart file content (multipart file field, binary/Base64)  
funds_statement | string | false |  | Proof-of-funds file content (multipart file field, binary/Base64, optional)  
additional | string | false |  | Other supplementary material file content (multipart file field, binary/Base64, optional)  
relationship_proof | string | false |  | Optional. JSON string of relationship_proof.  
  
**anyOf[0]**

Type | Constraints  
---|---  
any | required: ["relationship_proof"]  
  
**anyOf[1]**

Type | Constraints  
---|---  
any | required: ["certificate","share_holders","passport","share_holding_structure"]  
      
    
    {}
    
    

##  OtcQuoteResponse

OtcQuoteResponse

Type | Constraints  
---|---  
object | required: ["code","message","data","timestamp"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
code | integer | Required |  |   
message | string | Required |  |   
data | object | Required | required: ["type","pay_coin","get_coin","pay_amount","get_amount","rate","rate_reci","promotion_code","side","order_type","quote_token"] |   
timestamp | integer | Required |  | Server Unix timestamp in seconds  
  
**data**

OtcQuoteResult

Type | Constraints  
---|---  
object | required: ["type","pay_coin","get_coin","pay_amount","get_amount","rate","rate_reci","promotion_code","side","order_type","quote_token"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
type | string | Required |  | BUY (on-ramp) or SELL (off-ramp)  
pay_coin | string | Required |  | Payment currency  
get_coin | string | Required |  | Currency  
pay_amount | string | Required |  | Payment amount  
get_amount | string | Required |  | Redemption Amount  
rate | string | Required |  | Exchange rate  
rate_reci | string | Required |  | Reciprocal of the exchange rate  
promotion_code | string | Required |  | Promotion code  
side | string | Required |  | Quote method  
order_type | string | Required |  | Order type: FIAT (fiat) / STABLE (stablecoin)  
quote_token | string | Required |  | Quote token required when placing an order  
validity_period | string | Optional |  | Quote validity period (seconds)  
refresh_limit | integer | Optional |  | Quote refresh limit  
refresh_limit_msg | string | Optional |  | Quote refresh limit message  
      
    
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
        "quote_token": "string",
        "validity_period": "string",
        "refresh_limit": 0,
        "refresh_limit_msg": "string"
      },
      "timestamp": 0
    }
    
    

##  OtcBankSupplementChecklistItem

Supplementary document item

Type | Constraints  
---|---  
object | required: ["description"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
description | string | Required |  | Supplementary document submission description  
      
    
    {
      "description": "string"
    }
    
    

##  OtcOrderRequest

Fiat Order Request Body

Type | Constraints  
---|---  
object | required: ["type","side","crypto_currency","fiat_currency","crypto_amount","fiat_amount","quote_token","bank_id"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
type | string | Required |  | BUY for on-ramp, SELL for off-ramp  
side | string | Required |  | The side returned by the quote endpoint (used for order validation). For backward compatibility, `FIAT`/`CRYPTO` or `PAY`/`GET` are accepted; new integrations should use the value returned by the quote response.  
crypto_currency | string | Required |  | Cryptocurrency (supported currencies can be queried from the OTC web fiat quote page)  
fiat_currency | string | Required |  | Fiat currency (supported currencies can be queried from the OTC web fiat quote page)  
crypto_amount | string | Required |  | Amount of cryptocurrency  
fiat_amount | string | Required |  | Fiat amount  
promotion_code | string | Optional |  | Promotion code  
quote_token | string | Required |  | Parameter returned by the quote API  
bank_id | string | Required |  | Bank card ID used to place the order. Select one from the list returned by `GET /otc/bank/list`; the default card has `is_default=1`.  
receive_type | string | Optional | enum: ["YOU","GATE","RECIPIENT","PERSON"] | Name used for the remittance. Allowed values depend on the user type:  
Corporate users: YOU (remit in your company's name), GATE (remit in Gate's name), RECIPIENT (remit in the recipient's name);  
Individual users: GATE (remit in Gate's name), PERSON (remit in the user's own name).  
      
    
    {
      "type": "BUY",
      "side": "FIAT",
      "crypto_currency": "USDT",
      "fiat_currency": "USD",
      "crypto_amount": "30000",
      "fiat_amount": "30000",
      "promotion_code": "",
      "quote_token": "",
      "bank_id": "2",
      "receive_type": "GATE"
    }
    
    

##  OtcUploadPreUploadData

Pre-upload credentials and S3 direct-upload parameters

Type | Constraints  
---|---  
object | required: ["file_key","url","fields","expires_in"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
file_key | string | Required |  | Base64 temporary object path; pass back **unchanged** on business submit—do not decode  
url | string | Required |  | S3 direct upload URL  
fields | OtcUploadPreUploadPolicyFields | Required | required: ["key","Content-Type","X-Amz-Credential","X-Amz-Algorithm","X-Amz-Date","Policy","X-Amz-Signature"] | S3 POST Policy signature fields; send unchanged as form-data during direct upload  
expires_in | integer | Required |  | Policy validity period in seconds; currently 5400 (90 minutes); aligns with `expiration` in `fields.Policy`; call this endpoint again after expiry  
      
    
    {
      "file_key": "string",
      "url": "string",
      "fields": {
        "key": "string",
        "Content-Type": "string",
        "X-Amz-Credential": "string",
        "X-Amz-Algorithm": "string",
        "X-Amz-Date": "string",
        "Policy": "string",
        "X-Amz-Signature": "string"
      },
      "expires_in": 0
    }
    
    

##  OtcUploadPreUploadPolicyFields

S3 POST Policy signature fields; send unchanged as form-data during direct upload

Type | Constraints  
---|---  
object | required: ["key","Content-Type","X-Amz-Credential","X-Amz-Algorithm","X-Amz-Date","Policy","X-Amz-Signature"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
key | string | Required |  | Plaintext temporary object path, identical to base64_decode(file_key)  
Content-Type | string | Required |  | Must match the decoded content_type from the pre-upload request  
X-Amz-Credential | string | Required |  | AWS temporary credential and scope; submit them unchanged during direct upload  
X-Amz-Algorithm | string | Required |  | AWS signing algorithm; submit it unchanged during direct upload  
X-Amz-Date | string | Required |  | AWS signing timestamp; submit it unchanged during direct upload  
Policy | string | Required |  | Base64-encoded S3 POST Policy; submit it unchanged during direct upload  
X-Amz-Signature | string | Required |  | S3 POST Policy signature; submit it unchanged during direct upload  
      
    
    {
      "key": "string",
      "Content-Type": "string",
      "X-Amz-Credential": "string",
      "X-Amz-Algorithm": "string",
      "X-Amz-Date": "string",
      "Policy": "string",
      "X-Amz-Signature": "string"
    }