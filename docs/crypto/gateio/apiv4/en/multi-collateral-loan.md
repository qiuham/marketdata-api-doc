---
exchange: gateio
source_url: https://www.gate.com/docs/developers/apiv4/en/multi-collateral-loan
api_type: REST
updated_at: 2026-05-27 20:15:26.566254
---

# Multi-collateral-loan

Multi-currency collateral

##  Query multi-currency collateral order list🔒 Authenticated

GET`/loan/multi_collateral/orders`

GET `/loan/multi_collateral/orders`

_Query multi-currency collateral order list_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
page | query | integer | Optional | Page number  
limit | query | integer | Optional | Maximum number of records returned in a single list  
sort | query | string | Optional | Sort type: time_desc - Default descending by creation time, ltv_asc - Ascending by LTV ratio, ltv_desc - Descending by LTV ratio  
order_type | query | string | Optional | Order type: current - Query current orders, fixed - Query fixed orders, defaults to current orders if not specified  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)List retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [MultiCollateralOrder]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | [Multi-Collateral Order]  
» _None_ | MultiCollateralOrder | Multi-Collateral Order  
»» order_id | string | Order ID  
»» order_type | string | current - current, fixed - fixed  
»» fixed_type | string | Fixed interest rate loan periods: 7d - 7 days, 30d - 30 days  
»» fixed_rate | string | Fixed interest rate  
»» expire_time | integer(int64) | Expiration time, timestamp, unit in seconds  
»» auto_renew | boolean | Fixed interest rate, auto-renewal  
»» auto_repay | boolean | Fixed interest rate, auto-repayment  
»» current_ltv | string | Current collateralization rate  
»» status | string | Order status:  
\- initial: Initial state after placing the order  
\- collateral_deducted: Collateral deduction successful  
\- collateral_returning: Loan failed - Collateral return pending  
\- lent: Loan successful  
\- repaying: Repayment in progress  
\- liquidating: Liquidation in progress  
\- finished: Order completed  
\- closed_liquidated: Liquidation and repayment completed  
»» borrow_time | integer(int64) | Borrowing time, timestamp in seconds  
»» total_left_repay_usdt | string | Total outstanding value converted to USDT  
»» total_left_collateral_usdt | string | Total collateral value converted to USDT  
»» borrow_currencies | array | Borrowing Currency List  
»»» BorrowCurrencyInfo | object | none  
»»»» currency | string | Currency  
»»»» index_price | string | Currency Index Price  
»»»» left_repay_principal | string | Outstanding principal  
»»»» left_repay_interest | string | Outstanding interest  
»»»» left_repay_usdt | string | Remaining total outstanding value converted to USDT  
»»» collateral_currencies | array | Collateral Currency List  
»»»» CollateralCurrencyInfo | object | none  
»»»»» currency | string | Currency  
»»»»» index_price | string | Currency Index Price  
»»»»» left_collateral | string | Remaining collateral amount  
»»»»» left_collateral_usdt | string | Remaining collateral value converted to USDT  
  
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
    
    url = '/loan/multi_collateral/orders'
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
    url="/loan/multi_collateral/orders"
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
        "order_id": "10005578",
        "order_type": "fixed",
        "fixed_type": "7d",
        "fixed_rate": 0.00001,
        "expire_time": 1703820105,
        "auto_renew": true,
        "auto_repay": true,
        "current_ltv": "0.0001004349664281",
        "status": "lent",
        "borrow_time": 1702615021,
        "total_left_repay_usdt": "106.491212982",
        "total_left_collateral_usdt": "1060300.18",
        "borrow_currencies": [
          {
            "currency": "GT",
            "index_price": "10.6491",
            "left_repay_principal": "10",
            "left_repay_interest": "0.00002",
            "left_repay_usdt": "106.491212982"
          }
        ],
        "collateral_currencies": [
          {
            "currency": "BTC",
            "index_price": "112794.7",
            "left_collateral": "9.4",
            "left_collateral_usdt": "1060270.18"
          },
          {
            "currency": "USDT",
            "index_price": "1",
            "left_collateral": "30",
            "left_collateral_usdt": "30"
          }
        ]
      }
    ]
    

##  Place multi-currency collateral order🔒 Authenticated

POST`/loan/multi_collateral/orders`

POST `/loan/multi_collateral/orders`

_Place multi-currency collateral order_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | CreateMultiCollateralOrder | Required | none  
↳ order_id | body | string | Optional | Order ID  
↳ order_type | body | string | Optional | current - current rate, fixed - fixed rate, defaults to current if not specified  
↳ fixed_type | body | string | Optional | Fixed interest rate lending period: 7d - 7 days, 30d - 30 days. Required for fixed rate  
↳ fixed_rate | body | string | Optional | Fixed interest rate, required for fixed rate  
↳ auto_renew | body | boolean | Optional | Fixed interest rate, auto-renewal  
↳ auto_repay | body | boolean | Optional | Fixed interest rate, auto-repayment  
↳ borrow_currency | body | string | Required | Borrowed currency  
↳ borrow_amount | body | string | Required | Borrowed amount  
↳ collateral_currencies | body | array | Optional | Collateral currency and amount  
↳ CollateralCurrency | body | object | Optional | none  
↳ currency | body | string | Optional | Currency  
↳ amount | body | string | Optional | Size  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Order placed successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Order placed successfully | OrderResp  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» order_id | integer(int64) | Order ID  
  
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
    
    url = '/loan/multi_collateral/orders'
    query_param = ''
    body='{"order_id":1721387470,"order_type":"fixed","fixed_type":"7d","fixed_rate":0.00001,"auto_renew":true,"auto_repay":true,"borrow_currency":"BTC","borrow_amount":"1","collateral_currencies":[{"currency":"USDT","amount":"1000"}]}'
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
    url="/loan/multi_collateral/orders"
    query_param=""
    body_param='{"order_id":1721387470,"order_type":"fixed","fixed_type":"7d","fixed_rate":0.00001,"auto_renew":true,"auto_repay":true,"borrow_currency":"BTC","borrow_amount":"1","collateral_currencies":[{"currency":"USDT","amount":"1000"}]}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "order_id": 1721387470,
      "order_type": "fixed",
      "fixed_type": "7d",
      "fixed_rate": 0.00001,
      "auto_renew": true,
      "auto_repay": true,
      "borrow_currency": "BTC",
      "borrow_amount": "1",
      "collateral_currencies": [
        {
          "currency": "USDT",
          "amount": "1000"
        }
      ]
    }
    

> Example responses

> 200 Response
    
    
    {
      "order_id": 10005578
    }
    

##  Query order details🔒 Authenticated

GET`/loan/multi_collateral/orders/{order_id}`

GET `/loan/multi_collateral/orders/{order_id}`

_Query order details_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
order_id | path | string | Required | Order ID returned when order is successfully created  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Order details queried successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Order details queried successfully | MultiCollateralOrder  
  
### Response Schema

Status Code **200**

_Multi-Collateral Order_

Name | Type | Description  
---|---|---  
» order_id | string | Order ID  
» order_type | string | current - current, fixed - fixed  
» fixed_type | string | Fixed interest rate loan periods: 7d - 7 days, 30d - 30 days  
» fixed_rate | string | Fixed interest rate  
» expire_time | integer(int64) | Expiration time, timestamp, unit in seconds  
» auto_renew | boolean | Fixed interest rate, auto-renewal  
» auto_repay | boolean | Fixed interest rate, auto-repayment  
» current_ltv | string | Current collateralization rate  
» status | string | Order status:  
\- initial: Initial state after placing the order  
\- collateral_deducted: Collateral deduction successful  
\- collateral_returning: Loan failed - Collateral return pending  
\- lent: Loan successful  
\- repaying: Repayment in progress  
\- liquidating: Liquidation in progress  
\- finished: Order completed  
\- closed_liquidated: Liquidation and repayment completed  
» borrow_time | integer(int64) | Borrowing time, timestamp in seconds  
» total_left_repay_usdt | string | Total outstanding value converted to USDT  
» total_left_collateral_usdt | string | Total collateral value converted to USDT  
» borrow_currencies | array | Borrowing Currency List  
»» BorrowCurrencyInfo | object | none  
»»» currency | string | Currency  
»»» index_price | string | Currency Index Price  
»»» left_repay_principal | string | Outstanding principal  
»»» left_repay_interest | string | Outstanding interest  
»»» left_repay_usdt | string | Remaining total outstanding value converted to USDT  
»» collateral_currencies | array | Collateral Currency List  
»»» CollateralCurrencyInfo | object | none  
»»»» currency | string | Currency  
»»»» index_price | string | Currency Index Price  
»»»» left_collateral | string | Remaining collateral amount  
»»»» left_collateral_usdt | string | Remaining collateral value converted to USDT  
  
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
    
    url = '/loan/multi_collateral/orders/12345'
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
    url="/loan/multi_collateral/orders/12345"
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
      "order_id": "10005578",
      "order_type": "fixed",
      "fixed_type": "7d",
      "fixed_rate": 0.00001,
      "expire_time": 1703820105,
      "auto_renew": true,
      "auto_repay": true,
      "current_ltv": "0.0001004349664281",
      "status": "lent",
      "borrow_time": 1702615021,
      "total_left_repay_usdt": "106.491212982",
      "total_left_collateral_usdt": "1060300.18",
      "borrow_currencies": [
        {
          "currency": "GT",
          "index_price": "10.6491",
          "left_repay_principal": "10",
          "left_repay_interest": "0.00002",
          "left_repay_usdt": "106.491212982"
        }
      ],
      "collateral_currencies": [
        {
          "currency": "BTC",
          "index_price": "112794.7",
          "left_collateral": "9.4",
          "left_collateral_usdt": "1060270.18"
        },
        {
          "currency": "USDT",
          "index_price": "1",
          "left_collateral": "30",
          "left_collateral_usdt": "30"
        }
      ]
    }
    

##  Query multi-currency collateral repayment records🔒 Authenticated

GET`/loan/multi_collateral/repay`

GET `/loan/multi_collateral/repay`

_Query multi-currency collateral repayment records_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
type | query | string | Required | Operation type: repay - Regular repayment, liquidate - Liquidation  
borrow_currency | query | string | Optional | Borrowed currency  
page | query | integer | Optional | Page number  
limit | query | integer | Optional | Maximum number of records returned in a single list  
from | query | integer(int64) | Optional | Start timestamp for the query  
to | query | integer(int64) | Optional | End timestamp for the query, defaults to current time if not specified  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | [MultiRepayRecord]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | [Multi-Collateral Repayment Record]  
» _None_ | MultiRepayRecord | Multi-Collateral Repayment Record  
»» order_id | integer(int64) | Order ID  
»» record_id | integer(int64) | Repayment record ID  
»» init_ltv | string | Initial collateralization rate  
»» before_ltv | string | Ltv before the operation  
»» after_ltv | string | Ltv after the operation  
»» borrow_time | integer(int64) | Borrowing time, timestamp in seconds  
»» repay_time | integer(int64) | Repayment time, timestamp in seconds  
»» borrow_currencies | array | List of borrowing information  
»»» currency | string | Currency  
»»» index_price | string | Currency Index Price  
»»» before_amount | string | Amount before the operation  
»»» before_amount_usdt | string | USDT Amount before the operation  
»»» after_amount | string | Amount after the operation  
»»» after_amount_usdt | string | USDT Amount after the operation  
»» collateral_currencies | array | List of collateral information  
»»» currency | string | Currency  
»»» index_price | string | Currency Index Price  
»»» before_amount | string | Amount before the operation  
»»» before_amount_usdt | string | USDT Amount before the operation  
»»» after_amount | string | Amount after the operation  
»»» after_amount_usdt | string | USDT Amount after the operation  
»» repaid_currencies | array | Repay Currency List  
»»» RepayRecordRepaidCurrency | object | none  
»»»» currency | string | Repayment currency  
»»»» index_price | string | Currency Index Price  
»»»» repaid_amount | string | Repayment amount  
»»»» repaid_principal | string | Principal  
»»»» repaid_interest | string | Interest  
»»»» repaid_amount_usdt | string | Repayment amount converted to USDT  
»»» total_interest_list | array | Total Interest List  
»»»» RepayRecordTotalInterest | object | none  
»»»»» currency | string | Currency  
»»»»» index_price | string | Currency Index Price  
»»»»» amount | string | Interest Amount  
»»»»» amount_usdt | string | Interest amount converted to USDT  
»»»» left_repay_interest_list | array | List of remaining interest to be repaid  
»»»»» RepayRecordLeftInterest | object | none  
»»»»»» currency | string | Currency  
»»»»»» index_price | string | Currency Index Price  
»»»»»» before_amount | string | Interest amount before repayment  
»»»»»» before_amount_usdt | string | Converted value of interest before repayment in USDT  
»»»»»» after_amount | string | Interest amount after repayment  
»»»»»» after_amount_usdt | string | Converted value of interest after repayment in USDT  
  
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
    
    url = '/loan/multi_collateral/repay'
    query_param = 'type=repay'
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
    url="/loan/multi_collateral/repay"
    query_param="type=repay"
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
        "order_id": 10005679,
        "record_id": 1348,
        "init_ltv": "0.2141",
        "before_ltv": "0.215",
        "after_ltv": "0.312",
        "borrow_time": 1702995889,
        "repay_time": 1703053927,
        "borrow_currencies": [
          {
            "currency": "BAT",
            "index_price": "103.02",
            "before_amount": "1",
            "before_amount_usdt": "103.02",
            "after_amount": "0.999017",
            "after_amount_usdt": "102.91873134"
          }
        ],
        "collateral_currencies": [
          {
            "currency": "ETC",
            "index_price": "0.6014228107",
            "before_amount": "1000",
            "before_amount_usdt": "601.4228107",
            "after_amount": "1000",
            "after_amount_usdt": "601.4228107"
          }
        ],
        "repaid_currencies": [
          {
            "currency": "BAT",
            "index_price": "103.02",
            "repaid_amount": "0.001",
            "repaid_principal": "0.000983",
            "repaid_interest": "0.000017",
            "repaid_amount_usdt": "0.10302"
          }
        ],
        "total_interest_list": [
          {
            "currency": "BAT",
            "index_price": "103.02",
            "amount": "0.000017",
            "amount_usdt": "0.00175134"
          }
        ],
        "left_repay_interest_list": [
          {
            "currency": "BAT",
            "index_price": "103.02",
            "before_amount": "0.000017",
            "before_amount_usdt": "0.00175134",
            "after_amount": "0",
            "after_amount_usdt": "0"
          }
        ]
      }
    ]
    

##  Multi-currency collateral repayment🔒 Authenticated

POST`/loan/multi_collateral/repay`

POST `/loan/multi_collateral/repay`

_Multi-currency collateral repayment_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | RepayMultiLoan | Required | none  
↳ order_id | body | integer(int64) | Required | Order ID  
↳ repay_items | body | array | Required | Repay Currency Item  
↳ MultiLoanRepayItem | body | object | Optional | none  
↳ currency | body | string | Optional | Repayment currency  
↳ amount | body | string | Optional | Size  
↳ repaid_all | body | boolean | Required | Repayment method, set to true for full repayment, false for partial repayment  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Operation successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Operation successful | MultiRepayResp  
  
### Response Schema

Status Code **200**

_Multi-currency collateral repayment_

Name | Type | Description  
---|---|---  
» order_id | integer(int64) | Order ID  
» repaid_currencies | array | Repay Currency List  
»» RepayCurrencyRes | object | none  
»»» succeeded | boolean | Whether the repayment was successful  
»»» label | string | Error identifier for failed operations; empty when successful  
»»» message | string | Error description for failed operations; empty when successful  
»»» currency | string | Repayment currency  
»»» repaid_principal | string | Principal  
»»» repaid_interest | string | Principal  
  
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
    
    url = '/loan/multi_collateral/repay'
    query_param = ''
    body='{"order_id":10005578,"repay_items":[{"currency":"btc","amount":"1","repaid_all":false}]}'
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
    url="/loan/multi_collateral/repay"
    query_param=""
    body_param='{"order_id":10005578,"repay_items":[{"currency":"btc","amount":"1","repaid_all":false}]}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "order_id": 10005578,
      "repay_items": [
        {
          "currency": "btc",
          "amount": "1",
          "repaid_all": false
        }
      ]
    }
    

> Example responses

> 200 Response
    
    
    {
      "order_id": 10005679,
      "repaid_currencies": [
        {
          "succeeded": false,
          "label": "INVALID_PARAM_VALUE",
          "message": "Invalid parameter value",
          "currency": "BTC",
          "repaid_principal": "1",
          "repaid_interest": "0.0001"
        },
        {
          "succeeded": true,
          "currency": "BTC",
          "repaid_principal": "1",
          "repaid_interest": "0.0001"
        }
      ]
    }
    

##  Query collateral adjustment records🔒 Authenticated

GET`/loan/multi_collateral/mortgage`

GET `/loan/multi_collateral/mortgage`

_Query collateral adjustment records_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
page | query | integer | Optional | Page number  
limit | query | integer | Optional | Maximum number of records returned in a single list  
from | query | integer(int64) | Optional | Start timestamp for the query  
to | query | integer(int64) | Optional | End timestamp for the query, defaults to current time if not specified  
collateral_currency | query | string | Optional | Collateral currency  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)List retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [MultiCollateralRecord]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | [Multi-Collateral adjustment record]  
» _None_ | MultiCollateralRecord | Multi-Collateral adjustment record  
»» order_id | integer(int64) | Order ID  
»» record_id | integer(int64) | Collateral record ID  
»» before_ltv | string | Collateral ratio before adjustment  
»» after_ltv | string | Collateral ratio before adjustment  
»» operate_time | integer(int64) | Operation time, timestamp in seconds  
»» borrow_currencies | array | Borrowing Currency List  
»»» currency | string | Currency  
»»» index_price | string | Currency Index Price  
»»» before_amount | string | Amount before the operation  
»»» before_amount_usdt | string | USDT Amount before the operation  
»»» after_amount | string | Amount after the operation  
»»» after_amount_usdt | string | USDT Amount after the operation  
»» collateral_currencies | array | Collateral Currency List  
»»» currency | string | Currency  
»»» index_price | string | Currency Index Price  
»»» before_amount | string | Amount before the operation  
»»» before_amount_usdt | string | USDT Amount before the operation  
»»» after_amount | string | Amount after the operation  
»»» after_amount_usdt | string | USDT Amount after the operation  
  
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
    
    url = '/loan/multi_collateral/mortgage'
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
    url="/loan/multi_collateral/mortgage"
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
        "order_id": 10000417,
        "record_id": 10000452,
        "before_ltv": "0.00039345555621480000",
        "after_ltv": "0.00019672777810740000",
        "operate_time": 1688461924,
        "borrow_currencies": [
          {
            "currency": "BTC",
            "index_price": "30000",
            "before_amount": "0.1",
            "before_amount_usdt": "1000",
            "after_amount": "0.6",
            "after_amount_usdt": "1006"
          }
        ],
        "collateral_currencies": [
          {
            "currency": "BTC",
            "index_price": "30000",
            "before_amount": "0.1",
            "before_amount_usdt": "1000",
            "after_amount": "0.6",
            "after_amount_usdt": "1006"
          }
        ]
      }
    ]
    

##  Add or withdraw collateral🔒 Authenticated

POST`/loan/multi_collateral/mortgage`

POST `/loan/multi_collateral/mortgage`

_Add or withdraw collateral_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | CollateralAdjust | Required | none  
↳ order_id | body | integer(int64) | Required | Order ID  
↳ type | body | string | Required | Operation type: append - add collateral, redeem - withdraw collateral  
↳ collaterals | body | array | Optional | Collateral currency list  
↳ currency | body | string | Optional | Currency  
↳ amount | body | string | Optional | Size  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Operation successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Operation successful | CollateralAdjustRes  
  
### Response Schema

Status Code **200**

_Multi-collateral adjustment result_

Name | Type | Description  
---|---|---  
» order_id | integer(int64) | Order ID  
» collateral_currencies | array | Collateral currency information  
»» CollateralCurrencyRes | object | none  
»»» succeeded | boolean | Update success status  
»»» label | string | Error identifier for failed operations; empty when successful  
»»» message | string | Error description for failed operations; empty when successful  
»»» currency | string | Currency  
»»» amount | string | Successfully operated collateral quantity; 0 if operation fails  
  
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
    
    url = '/loan/multi_collateral/mortgage'
    query_param = ''
    body='{"order_id":10005578,"type":"append","collaterals":[{"currency":"btc","amount":"0.5"}]}'
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
    url="/loan/multi_collateral/mortgage"
    query_param=""
    body_param='{"order_id":10005578,"type":"append","collaterals":[{"currency":"btc","amount":"0.5"}]}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "order_id": 10005578,
      "type": "append",
      "collaterals": [
        {
          "currency": "btc",
          "amount": "0.5"
        }
      ]
    }
    

> Example responses

> 200 Response
    
    
    {
      "order_id": 10005679,
      "collateral_currencies": [
        {
          "succeeded": true,
          "currency": "btc",
          "amount": "0.5"
        }
      ]
    }
    

##  Query user's collateral and borrowing currency quota information🔒 Authenticated

GET`/loan/multi_collateral/currency_quota`

GET `/loan/multi_collateral/currency_quota`

_Query user's collateral and borrowing currency quota information_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
type | query | string | Required | Currency type: collateral - Collateral currency, borrow - Borrowing currency  
currency | query | string | Required | When it is a collateral currency, multiple currencies can be passed separated by commas; when it is a borrowing currency, only one currency can be passed  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | [CurrencyQuota]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | [Currency Quota]  
» _None_ | CurrencyQuota | Currency Quota  
»» currency | string | Currency  
»» index_price | string | Currency Index Price  
»» min_quota | string | Minimum borrowing/collateral limit for the currency  
»» left_quota | string | Remaining currency limit for `borrow/collateral` (when input parameter `type` is `borrow`, represents current currency)  
»» left_quote_usdt | string | Remaining currency limit converted to USDT (when input parameter `type` is `borrow`, represents current currency)  
»» left_quota_fixed | string | Remaining `borrow/collateral` limit for fixed-term currency  
»» left_quote_usdt_fixed | string | Remaining currency limit for fixed-term currency converted to USDT  
  
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
    
    url = '/loan/multi_collateral/currency_quota'
    query_param = 'type=collateral&currency=BTC'
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
    url="/loan/multi_collateral/currency_quota"
    query_param="type=collateral&currency=BTC"
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
        "currency": "BTC",
        "index_price": "35306.1",
        "min_quota": "0",
        "left_quota": "2768152.4958445218723677",
        "left_quote_usdt": "97732668833.536273678"
      }
    ]
    

##  Query borrow currencies and collateral currencies supported by multi-currency collateral

GET`/loan/multi_collateral/currencies`

GET `/loan/multi_collateral/currencies`

_Query borrow currencies and collateral currencies supported by multi-currency collateral_

### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | MultiCollateralCurrency  
  
### Response Schema

Status Code **200**

_Borrowing and collateral currencies supported for Multi-Collateral_

Name | Type | Description  
---|---|---  
» loan_currencies | array | List of supported borrowing currencies  
»» MultiLoanItem | object | none  
»»» currency | string | Currency  
»»» price | string | Latest price of the currency  
»» collateral_currencies | array | List of supported collateral currencies  
»»» MultiCollateralItem | object | none  
»»»» currency | string | Currency  
»»»» index_price | string | Currency Index Price  
»»»» discount | string | Discount  
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/loan/multi_collateral/currencies'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/loan/multi_collateral/currencies \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    {
      "loan_currencies": [
        {
          "currency": "BTC",
          "price": "1212"
        },
        {
          "currency": "GT",
          "price": "12"
        }
      ],
      "collateral_currencies": [
        {
          "currency": "BTC",
          "index_price": "1212",
          "discount": "0.7"
        }
      ]
    }
    

##  Query collateralization ratio information

GET`/loan/multi_collateral/ltv`

GET `/loan/multi_collateral/ltv`

_Query collateralization ratio information_

Multi-currency collateral ratio is fixed, independent of currency

### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | CollateralLtv  
  
### Response Schema

Status Code **200**

_Multi-collateral ratio_

Name | Type | Description  
---|---|---  
» init_ltv | string | Initial collateralization rate  
» alert_ltv | string | Warning collateralization rate  
» liquidate_ltv | string | Liquidation collateralization rate  
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/loan/multi_collateral/ltv'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/loan/multi_collateral/ltv \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    {
      "init_ltv": "0.7",
      "alert_ltv": "0.8",
      "liquidate_ltv": "0.9"
    }
    

##  Query currency's 7-day and 30-day fixed interest rates

GET`/loan/multi_collateral/fixed_rate`

GET `/loan/multi_collateral/fixed_rate`

_Query currency's 7-day and 30-day fixed interest rates_

### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | [CollateralFixRate]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | [Multi-collateral fixed interest rate]  
» _None_ | CollateralFixRate | Multi-collateral fixed interest rate  
»» currency | string | Currency  
»» rate_7d | string | Fixed interest rate for 7-day lending period  
»» rate_30d | string | Fixed interest rate for 30-day lending period  
»» update_time | integer(int64) | Update time, timestamp in seconds  
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/loan/multi_collateral/fixed_rate'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/loan/multi_collateral/fixed_rate \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    [
      {
        "currency": "BTC",
        "rate_7d": "0.000023",
        "rate_30d": "0.1",
        "update_time": 1703820105
      }
    ]
    

##  Query currency's current interest rate

GET`/loan/multi_collateral/current_rate`

GET `/loan/multi_collateral/current_rate`

_Query currency's current interest rate_

Query the current interest rate of the currency in the previous hour, the current interest rate is updated every hour

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
currencies | query | array[string] | Required | Specify currency name query array, separated by commas, maximum 100  
vip_level | query | string | Optional | VIP level, defaults to 0 if not specified  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | [CollateralCurrentRate]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | [Multi-collateral current interest rate]  
» _None_ | CollateralCurrentRate | Multi-collateral current interest rate  
»» currency | string | Currency  
»» current_rate | string | Currency current interest rate  
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/loan/multi_collateral/current_rate'
    query_param = 'currencies=BTC,GT'
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/loan/multi_collateral/current_rate?currencies=BTC,GT \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    [
      {
        "currency": "BTC",
        "current_rate": "0.000023"
      }
    ]
    

#  Schemas

##  MultiRepayRecord

_Multi-Collateral Repayment Record_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
order_id | integer(int64) | Optional | none | Order ID  
record_id | integer(int64) | Optional | none | Repayment record ID  
init_ltv | string | Optional | none | Initial collateralization rate  
before_ltv | string | Optional | none | Ltv before the operation  
after_ltv | string | Optional | none | Ltv after the operation  
borrow_time | integer(int64) | Optional | none | Borrowing time, timestamp in seconds  
repay_time | integer(int64) | Optional | none | Repayment time, timestamp in seconds  
borrow_currencies | array | Optional | none | List of borrowing information  
↳ currency | string | Optional | none | Currency  
↳ index_price | string | Optional | none | Currency Index Price  
↳ before_amount | string | Optional | none | Amount before the operation  
↳ before_amount_usdt | string | Optional | none | USDT Amount before the operation  
↳ after_amount | string | Optional | none | Amount after the operation  
↳ after_amount_usdt | string | Optional | none | USDT Amount after the operation  
collateral_currencies | [MultiRepayRecord/properties/borrow_currencies/items] | Optional | none | List of collateral information  
repaid_currencies | array | Optional | none | Repay Currency List  
↳ RepayRecordRepaidCurrency | object | Optional | none | none  
↳ currency | string | Optional | none | Repayment currency  
↳ index_price | string | Optional | none | Currency Index Price  
↳ repaid_amount | string | Optional | none | Repayment amount  
↳ repaid_principal | string | Optional | none | Principal  
↳ repaid_interest | string | Optional | none | Interest  
↳ repaid_amount_usdt | string | Optional | none | Repayment amount converted to USDT  
↳ total_interest_list | array | Optional | none | Total Interest List  
↳ RepayRecordTotalInterest | object | Optional | none | none  
↳ currency | string | Optional | none | Currency  
↳ index_price | string | Optional | none | Currency Index Price  
↳ amount | string | Optional | none | Interest Amount  
↳ amount_usdt | string | Optional | none | Interest amount converted to USDT  
↳ left_repay_interest_list | array | Optional | none | List of remaining interest to be repaid  
↳ RepayRecordLeftInterest | object | Optional | none | none  
↳ currency | string | Optional | none | Currency  
↳ index_price | string | Optional | none | Currency Index Price  
↳ before_amount | string | Optional | none | Interest amount before repayment  
↳ before_amount_usdt | string | Optional | none | Converted value of interest before repayment in USDT  
↳ after_amount | string | Optional | none | Interest amount after repayment  
↳ after_amount_usdt | string | Optional | none | Converted value of interest after repayment in USDT  
      
    
    {
      "order_id": 0,
      "record_id": 0,
      "init_ltv": "string",
      "before_ltv": "string",
      "after_ltv": "string",
      "borrow_time": 0,
      "repay_time": 0,
      "borrow_currencies": [
        {
          "currency": "string",
          "index_price": "string",
          "before_amount": "string",
          "before_amount_usdt": "string",
          "after_amount": "string",
          "after_amount_usdt": "string"
        }
      ],
      "collateral_currencies": [
        {
          "currency": "string",
          "index_price": "string",
          "before_amount": "string",
          "before_amount_usdt": "string",
          "after_amount": "string",
          "after_amount_usdt": "string"
        }
      ],
      "repaid_currencies": [
        {
          "currency": "string",
          "index_price": "string",
          "repaid_amount": "string",
          "repaid_principal": "string",
          "repaid_interest": "string",
          "repaid_amount_usdt": "string"
        }
      ],
      "total_interest_list": [
        {
          "currency": "string",
          "index_price": "string",
          "amount": "string",
          "amount_usdt": "string"
        }
      ],
      "left_repay_interest_list": [
        {
          "currency": "string",
          "index_price": "string",
          "before_amount": "string",
          "before_amount_usdt": "string",
          "after_amount": "string",
          "after_amount_usdt": "string"
        }
      ]
    }
    
    

##  CollateralFixRate

_Multi-collateral fixed interest rate_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
currency | string | Optional | none | Currency  
rate_7d | string | Optional | none | Fixed interest rate for 7-day lending period  
rate_30d | string | Optional | none | Fixed interest rate for 30-day lending period  
update_time | integer(int64) | Optional | none | Update time, timestamp in seconds  
      
    
    {
      "currency": "string",
      "rate_7d": "string",
      "rate_30d": "string",
      "update_time": 0
    }
    
    

##  CreateMultiCollateralOrder

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
order_id | string | Optional | none | Order ID  
order_type | string | Optional | none | current - current rate, fixed - fixed rate, defaults to current if not specified  
fixed_type | string | Optional | none | Fixed interest rate lending period: 7d - 7 days, 30d - 30 days. Required for fixed rate  
fixed_rate | string | Optional | none | Fixed interest rate, required for fixed rate  
auto_renew | boolean | Optional | none | Fixed interest rate, auto-renewal  
auto_repay | boolean | Optional | none | Fixed interest rate, auto-repayment  
borrow_currency | string | Required | none | Borrowed currency  
borrow_amount | string | Required | none | Borrowed amount  
collateral_currencies | array | Optional | none | Collateral currency and amount  
↳ CollateralCurrency | object | Optional | none | none  
↳ currency | string | Optional | none | Currency  
↳ amount | string | Optional | none | Size  
      
    
    {
      "order_id": "string",
      "order_type": "string",
      "fixed_type": "string",
      "fixed_rate": "string",
      "auto_renew": true,
      "auto_repay": true,
      "borrow_currency": "string",
      "borrow_amount": "string",
      "collateral_currencies": [
        {
          "currency": "string",
          "amount": "string"
        }
      ]
    }
    
    

##  CurrencyQuota

_Currency Quota_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
currency | string | Optional | none | Currency  
index_price | string | Optional | none | Currency Index Price  
min_quota | string | Optional | none | Minimum borrowing/collateral limit for the currency  
left_quota | string | Optional | none | Remaining currency limit for `borrow/collateral` (when input parameter `type` is `borrow`, represents current currency)  
left_quote_usdt | string | Optional | none | Remaining currency limit converted to USDT (when input parameter `type` is `borrow`, represents current currency)  
left_quota_fixed | string | Optional | none | Remaining `borrow/collateral` limit for fixed-term currency  
left_quote_usdt_fixed | string | Optional | none | Remaining currency limit for fixed-term currency converted to USDT  
      
    
    {
      "currency": "string",
      "index_price": "string",
      "min_quota": "string",
      "left_quota": "string",
      "left_quote_usdt": "string",
      "left_quota_fixed": "string",
      "left_quote_usdt_fixed": "string"
    }
    
    

##  MultiCollateralRecord

_Multi-Collateral adjustment record_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
order_id | integer(int64) | Optional | none | Order ID  
record_id | integer(int64) | Optional | none | Collateral record ID  
before_ltv | string | Optional | none | Collateral ratio before adjustment  
after_ltv | string | Optional | none | Collateral ratio before adjustment  
operate_time | integer(int64) | Optional | none | Operation time, timestamp in seconds  
borrow_currencies | array | Optional | none | Borrowing Currency List  
↳ currency | string | Optional | none | Currency  
↳ index_price | string | Optional | none | Currency Index Price  
↳ before_amount | string | Optional | none | Amount before the operation  
↳ before_amount_usdt | string | Optional | none | USDT Amount before the operation  
↳ after_amount | string | Optional | none | Amount after the operation  
↳ after_amount_usdt | string | Optional | none | USDT Amount after the operation  
collateral_currencies | [MultiCollateralRecord/properties/borrow_currencies/items] | Optional | none | Collateral Currency List  
      
    
    {
      "order_id": 0,
      "record_id": 0,
      "before_ltv": "string",
      "after_ltv": "string",
      "operate_time": 0,
      "borrow_currencies": [
        {
          "currency": "string",
          "index_price": "string",
          "before_amount": "string",
          "before_amount_usdt": "string",
          "after_amount": "string",
          "after_amount_usdt": "string"
        }
      ],
      "collateral_currencies": [
        {
          "currency": "string",
          "index_price": "string",
          "before_amount": "string",
          "before_amount_usdt": "string",
          "after_amount": "string",
          "after_amount_usdt": "string"
        }
      ]
    }
    
    

##  CollateralCurrentRate

_Multi-collateral current interest rate_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
currency | string | Optional | none | Currency  
current_rate | string | Optional | none | Currency current interest rate  
      
    
    {
      "currency": "string",
      "current_rate": "string"
    }
    
    

##  CollateralAdjust

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
order_id | integer(int64) | Required | none | Order ID  
type | string | Required | none | Operation type: append - add collateral, redeem - withdraw collateral  
collaterals | array | Optional | none | Collateral currency list  
↳ currency | string | Optional | none | Currency  
↳ amount | string | Optional | none | Size  
      
    
    {
      "order_id": 0,
      "type": "string",
      "collaterals": [
        {
          "currency": "string",
          "amount": "string"
        }
      ]
    }
    
    

##  CollateralAdjustRes

_Multi-collateral adjustment result_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
order_id | integer(int64) | Optional | none | Order ID  
collateral_currencies | array | Optional | none | Collateral currency information  
↳ CollateralCurrencyRes | object | Optional | none | none  
↳ succeeded | boolean | Optional | none | Update success status  
↳ label | string | Optional | none | Error identifier for failed operations; empty when successful  
↳ message | string | Optional | none | Error description for failed operations; empty when successful  
↳ currency | string | Optional | none | Currency  
↳ amount | string | Optional | none | Successfully operated collateral quantity; 0 if operation fails  
      
    
    {
      "order_id": 0,
      "collateral_currencies": [
        {
          "succeeded": true,
          "label": "string",
          "message": "string",
          "currency": "string",
          "amount": "string"
        }
      ]
    }
    
    

##  MultiCollateralCurrency

_Borrowing and collateral currencies supported for Multi-Collateral_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
loan_currencies | array | Optional | none | List of supported borrowing currencies  
↳ MultiLoanItem | object | Optional | none | none  
↳ currency | string | Optional | none | Currency  
↳ price | string | Optional | none | Latest price of the currency  
↳ collateral_currencies | array | Optional | none | List of supported collateral currencies  
↳ MultiCollateralItem | object | Optional | none | none  
↳ currency | string | Optional | none | Currency  
↳ index_price | string | Optional | none | Currency Index Price  
↳ discount | string | Optional | none | Discount  
      
    
    {
      "loan_currencies": [
        {
          "currency": "string",
          "price": "string"
        }
      ],
      "collateral_currencies": [
        {
          "currency": "string",
          "index_price": "string",
          "discount": "string"
        }
      ]
    }
    
    

##  RepayMultiLoan

_Multi-currency collateral repayment_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
order_id | integer(int64) | Required | none | Order ID  
repay_items | array | Required | none | Repay Currency Item  
↳ MultiLoanRepayItem | object | Optional | none | none  
↳ currency | string | Optional | none | Repayment currency  
↳ amount | string | Optional | none | Size  
↳ repaid_all | boolean | Required | none | Repayment method, set to true for full repayment, false for partial repayment  
      
    
    {
      "order_id": 0,
      "repay_items": [
        {
          "currency": "string",
          "amount": "string",
          "repaid_all": true
        }
      ]
    }
    
    

##  CollateralLtv

_Multi-collateral ratio_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
init_ltv | string | Optional | none | Initial collateralization rate  
alert_ltv | string | Optional | none | Warning collateralization rate  
liquidate_ltv | string | Optional | none | Liquidation collateralization rate  
      
    
    {
      "init_ltv": "string",
      "alert_ltv": "string",
      "liquidate_ltv": "string"
    }
    
    

##  OrderResp

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
order_id | integer(int64) | Optional | none | Order ID  
      
    
    {
      "order_id": 0
    }
    
    

##  MultiCollateralOrder

_Multi-Collateral Order_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
order_id | string | Optional | none | Order ID  
order_type | string | Optional | none | current - current, fixed - fixed  
fixed_type | string | Optional | none | Fixed interest rate loan periods: 7d - 7 days, 30d - 30 days  
fixed_rate | string | Optional | none | Fixed interest rate  
expire_time | integer(int64) | Optional | none | Expiration time, timestamp, unit in seconds  
auto_renew | boolean | Optional | none | Fixed interest rate, auto-renewal  
auto_repay | boolean | Optional | none | Fixed interest rate, auto-repayment  
current_ltv | string | Optional | none | Current collateralization rate  
status | string | Optional | none | Order status:  
\- initial: Initial state after placing the order  
\- collateral_deducted: Collateral deduction successful  
\- collateral_returning: Loan failed - Collateral return pending  
\- lent: Loan successful  
\- repaying: Repayment in progress  
\- liquidating: Liquidation in progress  
\- finished: Order completed  
\- closed_liquidated: Liquidation and repayment completed  
borrow_time | integer(int64) | Optional | none | Borrowing time, timestamp in seconds  
total_left_repay_usdt | string | Optional | none | Total outstanding value converted to USDT  
total_left_collateral_usdt | string | Optional | none | Total collateral value converted to USDT  
borrow_currencies | array | Optional | none | Borrowing Currency List  
↳ BorrowCurrencyInfo | object | Optional | none | none  
↳ currency | string | Optional | none | Currency  
↳ index_price | string | Optional | none | Currency Index Price  
↳ left_repay_principal | string | Optional | none | Outstanding principal  
↳ left_repay_interest | string | Optional | none | Outstanding interest  
↳ left_repay_usdt | string | Optional | none | Remaining total outstanding value converted to USDT  
↳ collateral_currencies | array | Optional | none | Collateral Currency List  
↳ CollateralCurrencyInfo | object | Optional | none | none  
↳ currency | string | Optional | none | Currency  
↳ index_price | string | Optional | none | Currency Index Price  
↳ left_collateral | string | Optional | none | Remaining collateral amount  
↳ left_collateral_usdt | string | Optional | none | Remaining collateral value converted to USDT  
      
    
    {
      "order_id": "string",
      "order_type": "string",
      "fixed_type": "string",
      "fixed_rate": "string",
      "expire_time": 0,
      "auto_renew": true,
      "auto_repay": true,
      "current_ltv": "string",
      "status": "string",
      "borrow_time": 0,
      "total_left_repay_usdt": "string",
      "total_left_collateral_usdt": "string",
      "borrow_currencies": [
        {
          "currency": "string",
          "index_price": "string",
          "left_repay_principal": "string",
          "left_repay_interest": "string",
          "left_repay_usdt": "string"
        }
      ],
      "collateral_currencies": [
        {
          "currency": "string",
          "index_price": "string",
          "left_collateral": "string",
          "left_collateral_usdt": "string"
        }
      ]
    }
    
    

##  MultiRepayResp

_Multi-currency collateral repayment_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
order_id | integer(int64) | Optional | none | Order ID  
repaid_currencies | array | Optional | none | Repay Currency List  
↳ RepayCurrencyRes | object | Optional | none | none  
↳ succeeded | boolean | Optional | none | Whether the repayment was successful  
↳ label | string | Optional | none | Error identifier for failed operations; empty when successful  
↳ message | string | Optional | none | Error description for failed operations; empty when successful  
↳ currency | string | Optional | none | Repayment currency  
↳ repaid_principal | string | Optional | none | Principal  
↳ repaid_interest | string | Optional | none | Principal  
      
    
    {
      "order_id": 0,
      "repaid_currencies": [
        {
          "succeeded": true,
          "label": "string",
          "message": "string",
          "currency": "string",
          "repaid_principal": "string",
          "repaid_interest": "string"
        }
      ]
    }