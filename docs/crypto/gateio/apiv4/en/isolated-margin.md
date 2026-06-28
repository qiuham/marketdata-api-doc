---
exchange: gateio
source_url: https://www.gate.com/docs/developers/apiv4/en/isolated-margin
api_type: REST
updated_at: 2026-05-27 20:15:21.419927
---

# Isolated-Margin

Isolated Margin

##  Margin account list🔒 Authenticated

GET`/margin/accounts`

GET `/margin/accounts`

_Margin account list_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
currency_pair | query | string | Optional | Currency pair  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)List retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [MarginAccount]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | [Margin account information for a trading pair. `base` corresponds to base currency account information, `quote` corresponds to quote currency account information]  
» _None_ | MarginAccount | Margin account information for a trading pair. `base` corresponds to base currency account information, `quote` corresponds to quote currency account information  
»» currency_pair | string | Currency pair  
»» account_type | string | Account Type mmr: maintenance margin rate account;inactive: market not activated  
»» leverage | string | User's current market leverage multiplier  
»» locked | boolean | Whether the account is locked  
»» risk | string | Deprecated  
»» mmr | string | Current Maintenance Margin Rate of the account  
»» base | MarginAccount/properties/base | Currency account information  
»»» currency | string | Currency name  
»»» available | string | Amount available for margin trading, available = margin + borrowed  
»»» locked | string | Frozen funds, such as amounts already placed in margin market for order trading  
»»» borrowed | string | Borrowed funds  
»»» interest | string | Unpaid interest  
»» quote | MarginAccount/properties/base | Currency account information  
»»» currency | string | Currency name  
»»» available | string | Amount available for margin trading, available = margin + borrowed  
»»» locked | string | Frozen funds, such as amounts already placed in margin market for order trading  
»»» borrowed | string | Borrowed funds  
»»» interest | string | Unpaid interest  
  
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
    
    url = '/margin/accounts'
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
    url="/margin/accounts"
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
        "currency_pair": "BTC_USDT",
        "account_type": "mmr",
        "leverage": "20",
        "locked": false,
        "risk": "1.3318",
        "mmr": "16.5949188975473644",
        "base": {
          "currency": "BTC",
          "available": "0.047060413211",
          "locked": "0",
          "borrowed": "0.047233",
          "interest": "0"
        },
        "quote": {
          "currency": "USDT",
          "available": "1234",
          "locked": "0",
          "borrowed": "0",
          "interest": "0"
        }
      }
    ]
    

##  Query margin account balance change history🔒 Authenticated

GET`/margin/account_book`

GET `/margin/account_book`

_Query margin account balance change history_

Currently only provides transfer history to and from margin accounts. Query time range cannot exceed 30 days

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
currency | query | string | Optional | Query history for specified currency. If `currency` is specified, `currency_pair` must also be specified.  
currency_pair | query | string | Optional | Specify margin account currency pair. Used in combination with `currency`. Ignored if `currency` is not specified  
type | query | string | Optional | Query by specified account change type. If not specified, all change types will be included.  
from | query | integer(int64) | Optional | Start timestamp  
  
Specify start time, time format is Unix timestamp. If not specified, it defaults to (the data start time of the time range actually returned by to and limit)  
to | query | integer(int64) | Optional | Termination Timestamp  
  
Specify the end time. If not specified, it defaults to the current time, and the time format is a Unix timestamp  
page | query | integer(int32) | Optional | Page number  
limit | query | integer | Optional | Maximum number of records returned in a single list  
  
####  Detailed descriptions

**from** : Start timestamp  
  
Specify start time, time format is Unix timestamp. If not specified, it defaults to (the data start time of the time range actually returned by to and limit)

**to** : Termination Timestamp  
  
Specify the end time. If not specified, it defaults to the current time, and the time format is a Unix timestamp

### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)List retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [MarginAccountBook]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | none  
» id | string | Balance change record ID  
» time | string | Account change timestamp  
» time_ms | integer(int64) | The timestamp of the change (in milliseconds)  
» currency | string | Currency changed  
» currency_pair | string | Account trading pair  
» change | string | Amount changed. Positive value means transferring in, while negative out  
» balance | string | Balance after change  
» type | string | Account book type. Please refer to account book type for more detail  
  
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
    
    url = '/margin/account_book'
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
    url="/margin/account_book"
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
        "id": "123456",
        "time": "1547633726",
        "time_ms": 1547633726123,
        "currency": "BTC",
        "currency_pair": "BTC_USDT",
        "change": "1.03",
        "balance": "4.59316525194"
      }
    ]
    

##  Funding account list🔒 Authenticated

GET`/margin/funding_accounts`

GET `/margin/funding_accounts`

_Funding account list_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
currency | query | string | Optional | Query by specified currency name  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)List retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [FundingAccount]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | none  
» currency | string | Currency name  
» available | string | Available assets to lend, which is identical to spot account `available`  
» locked | string | Locked amount. i.e. amount in `open` loans  
» lent | string | Outstanding loan amount yet to be repaid  
» total_lent | string | Amount used for lending. total_lent = lent + locked  
  
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
    
    url = '/margin/funding_accounts'
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
    url="/margin/funding_accounts"
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
        "currency": "BTC",
        "available": "1.238",
        "locked": "0",
        "lent": "3.32",
        "total_lent": "3.32"
      }
    ]
    

##  Query user auto repayment settings🔒 Authenticated

GET`/margin/auto_repay`

GET `/margin/auto_repay`

_Query user auto repayment settings_

### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)User's current auto repayment settings

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | User's current auto repayment settings | Inline  
  
### Response Schema

Status Code **200**

_AutoRepaySetting_

Name | Type | Description  
---|---|---  
» status | string | Auto repayment status: `on` \- enabled, `off` \- disabled  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
status | on  
status | off  
  
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
    
    url = '/margin/auto_repay'
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
    url="/margin/auto_repay"
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
      "status": "on"
    }
    

##  Update user auto repayment settings🔒 Authenticated

POST`/margin/auto_repay`

POST `/margin/auto_repay`

_Update user auto repayment settings_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
status | query | string | Required | Whether to enable auto repayment: `on` \- enabled, `off` \- disabled  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)User's current auto repayment settings

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | User's current auto repayment settings | Inline  
  
### Response Schema

Status Code **200**

_AutoRepaySetting_

Name | Type | Description  
---|---|---  
» status | string | Auto repayment status: `on` \- enabled, `off` \- disabled  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
status | on  
status | off  
  
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
    
    url = '/margin/auto_repay'
    query_param = 'status=on'
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
    url="/margin/auto_repay"
    query_param="status=on"
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
      "status": "on"
    }
    

##  Get maximum transferable amount for isolated margin🔒 Authenticated

GET`/margin/transferable`

GET `/margin/transferable`

Get `maximum transferable amount for isolated margin`

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
currency | query | string | Required | Query by specified currency name  
currency_pair | query | string | Optional | Currency pair  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | MarginTransferable  
  
### Response Schema

Status Code **200**

_MarginTransferable_

Name | Type | Description  
---|---|---  
» currency | string | Currency detail  
» currency_pair | string | Currency pair  
» amount | string | Max transferable amount  
  
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
    
    url = '/margin/transferable'
    query_param = 'currency=BTC'
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
    url="/margin/transferable"
    query_param="currency=BTC"
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
      "currency": "ETH",
      "currency_pair": "ETH_USDT",
      "amount": "10000"
    }
    

##  List lending markets

GET`/margin/uni/currency_pairs`

GET `/margin/uni/currency_pairs`

_List lending markets_

### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | [UniCurrencyPair]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | [Currency pair of the loan]  
» _None_ | UniCurrencyPair | Currency pair of the loan  
»» currency_pair | string | Currency pair  
»» base_min_borrow_amount | string | Minimum borrow amount of base currency  
»» quote_min_borrow_amount | string | Minimum borrow amount of quote currency  
»» leverage | string | Position leverage  
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/margin/uni/currency_pairs'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/margin/uni/currency_pairs \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    [
      {
        "currency_pair": "AE_USDT",
        "base_min_borrow_amount": "100",
        "quote_min_borrow_amount": "100",
        "leverage": "3"
      }
    ]
    

##  Get lending market details

GET`/margin/uni/currency_pairs/{currency_pair}`

GET `/margin/uni/currency_pairs/{currency_pair}`

Get `lending market details`

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
currency_pair | path | string | Required | Currency pair  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | UniCurrencyPair  
  
### Response Schema

Status Code **200**

_Currency pair of the loan_

Name | Type | Description  
---|---|---  
» currency_pair | string | Currency pair  
» base_min_borrow_amount | string | Minimum borrow amount of base currency  
» quote_min_borrow_amount | string | Minimum borrow amount of quote currency  
» leverage | string | Position leverage  
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/margin/uni/currency_pairs/AE_USDT'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/margin/uni/currency_pairs/AE_USDT \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    {
      "currency_pair": "AE_USDT",
      "base_min_borrow_amount": "100",
      "quote_min_borrow_amount": "100",
      "leverage": "3"
    }
    

##  Estimate interest rate for isolated margin currencies🔒 Authenticated

GET`/margin/uni/estimate_rate`

GET `/margin/uni/estimate_rate`

_Estimate interest rate for isolated margin currencies_

Interest rates change hourly based on lending depth, so completely accurate rates cannot be provided.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
currencies | query | array[string] | Required | Array of currency names to query, maximum 10  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | Inline  
  
### Response Schema

Status Code **200**

_Estimate current hourly lending rates, returned by currency_

Name | Type | Description  
---|---|---  
» **additionalProperties** | string | none  
  
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
    
    url = '/margin/uni/estimate_rate'
    query_param = 'currencies=BTC,GT'
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
    url="/margin/uni/estimate_rate"
    query_param="currencies=BTC,GT"
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
      "BTC": "0.000002",
      "GT": "0.000001"
    }
    

##  Query loans🔒 Authenticated

GET`/margin/uni/loans`

GET `/margin/uni/loans`

_Query loans_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
currency_pair | query | string | Optional | Currency pair  
currency | query | string | Optional | Query by specified currency name  
page | query | integer(int32) | Optional | Page number  
limit | query | integer | Optional | Maximum number of records returned in a single list  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | [UniLoan]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | [Borrowing]  
» _None_ | UniLoan | Borrowing  
»» currency | string | Currency  
»» currency_pair | string | Currency pair  
»» amount | string | Amount to Repay  
»» type | string | Loan type: platform borrowing - platform, margin borrowing - margin  
»» create_time | integer(int64) | Created time  
»» update_time | integer(int64) | Last Update Time  
  
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
    
    url = '/margin/uni/loans'
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
    url="/margin/uni/loans"
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
        "currency": "USDT",
        "currency_pari": "GT_USDT",
        "amount": "1",
        "type": "margin",
        "change_time": 1673247054000,
        "create_time": 1673247054000
      }
    ]
    

##  Borrow or repay🔒 Authenticated

POST`/margin/uni/loans`

POST `/margin/uni/loans`

_Borrow or repay_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | CreateUniLoan | Required | none  
↳ currency | body | string | Required | Currency  
↳ type | body | string | Required | Loan Type margin: margin borrowing  
↳ amount | body | string | Required | Borrow or repayment amount  
↳ repaid_all | body | boolean | Optional | Full repayment. For repayment operations only. When `true`, overrides `amount` and repays the full amount  
↳ currency_pair | body | string | Required | Currency pair  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
» type | borrow  
» type | repay  
  
### Responses

  * 204[No Content ](https://tools.ietf.org/html/rfc7231#section-6.3.5)Operation successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
204 | [No Content ](https://tools.ietf.org/html/rfc7231#section-6.3.5) | Operation successful | None  
  
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
    
    url = '/margin/uni/loans'
    query_param = ''
    body='{"currency":"BTC","amount":"0.1","type":"borrow","currency_pair":"BTC_USDT","repaid_all":false}'
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
    url="/margin/uni/loans"
    query_param=""
    body_param='{"currency":"BTC","amount":"0.1","type":"borrow","currency_pair":"BTC_USDT","repaid_all":false}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "currency": "BTC",
      "amount": "0.1",
      "type": "borrow",
      "currency_pair": "BTC_USDT",
      "repaid_all": false
    }
    

##  Query loan records🔒 Authenticated

GET`/margin/uni/loan_records`

GET `/margin/uni/loan_records`

_Query loan records_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
type | query | string | Optional | Type: `borrow` \- borrow, `repay` \- repay  
currency | query | string | Optional | Query by specified currency name  
currency_pair | query | string | Optional | Currency pair  
page | query | integer(int32) | Optional | Page number  
limit | query | integer | Optional | Maximum number of records returned in a single list  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
type | borrow  
type | repay  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | [UniLoanRecord]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | [Borrowing Records]  
» _None_ | UniLoanRecord | Borrowing Records  
»» type | string | Type: `borrow` \- borrow, `repay` \- repay  
»» currency_pair | string | Currency pair  
»» currency | string | Currency  
»» amount | string | Borrow or repayment amount  
»» create_time | integer(int64) | Created time  
  
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
    
    url = '/margin/uni/loan_records'
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
    url="/margin/uni/loan_records"
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
        "type": "borrow",
        "currency_pair": "AE_USDT",
        "currency": "USDT",
        "amount": "1000",
        "create_time": 1673247054000
      }
    ]
    

##  Query interest deduction records🔒 Authenticated

GET`/margin/uni/interest_records`

GET `/margin/uni/interest_records`

_Query interest deduction records_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
currency_pair | query | string | Optional | Currency pair  
currency | query | string | Optional | Query by specified currency name  
page | query | integer(int32) | Optional | Page number  
limit | query | integer | Optional | Maximum number of records returned in a single list  
from | query | integer(int64) | Optional | Start timestamp  
  
Specify start time, time format is Unix timestamp. If not specified, it defaults to (the data start time of the time range actually returned by to and limit)  
to | query | integer(int64) | Optional | Termination Timestamp  
  
Specify the end time. If not specified, it defaults to the current time, and the time format is a Unix timestamp  
  
####  Detailed descriptions

**from** : Start timestamp  
  
Specify start time, time format is Unix timestamp. If not specified, it defaults to (the data start time of the time range actually returned by to and limit)

**to** : Termination Timestamp  
  
Specify the end time. If not specified, it defaults to the current time, and the time format is a Unix timestamp

### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | [UniLoanInterestRecord]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | [Interest Deduction Record]  
» _None_ | UniLoanInterestRecord | Interest Deduction Record  
»» currency | string | Currency name  
»» currency_pair | string | Currency pair  
»» actual_rate | string | Actual Rate  
»» interest | string | Interest  
»» status | integer | Status: 0 - fail, 1 - success  
»» type | string | Loan Type margin: margin borrowing  
»» create_time | integer(int64) | Created time  
  
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
    
    url = '/margin/uni/interest_records'
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
    url="/margin/uni/interest_records"
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
        "status": 1,
        "currency_pair": "BTC_USDT",
        "currency": "USDT",
        "actual_rate": "0.00000236",
        "interest": "0.00006136",
        "type": "platform",
        "create_time": 1673247054000
      }
    ]
    

##  Query maximum borrowable amount by currency🔒 Authenticated

GET`/margin/uni/borrowable`

GET `/margin/uni/borrowable`

_Query maximum borrowable amount by currency_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
currency | query | string | Required | Query by specified currency name  
currency_pair | query | string | Required | Currency pair  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | MaxUniBorrowable  
  
### Response Schema

Status Code **200**

_MaxUniBorrowable_

Name | Type | Description  
---|---|---  
» currency | string | Currency  
» currency_pair | string | Currency pair  
» borrowable | string | Maximum borrowable  
  
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
    
    url = '/margin/uni/borrowable'
    query_param = 'currency=BTC&currency_pair=BTC_USDT'
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
    url="/margin/uni/borrowable"
    query_param="currency=BTC&currency_pair=BTC_USDT"
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
      "currency": "AE",
      "borrowable": "1123.344",
      "currency_pair": "AE_USDT"
    }
    

##  Query user's own leverage lending tiers in current market🔒 Authenticated

GET`/margin/user/loan_margin_tiers`

GET `/margin/user/loan_margin_tiers`

_Query user's own leverage lending tiers in current market_

Query the borrowing tier margin requirements of a specific spot market.For more details about borrowing tier margin requirements, please refer to Underlying Logic of the New Isolated Margin System（https://www.gate.com/en/help/trade/margin-trading/42357）

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
currency_pair | query | string | Required | Currency pair  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | [MarginLeverageTier]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | [Market gradient information]  
» _None_ | MarginLeverageTier | Market gradient information  
»» upper_limit | string | Maximum borrowing limit. Determined by the leverage you set; the lower the leverage, the larger the borrowing limit.  
»» mmr | string | Maintenance margin rate.Under tiered margin requirements(https://www.gate.com/en/help/trade/margin-trading/42357), the maintenance margin rate is a composite value.  
»» leverage | string | the maximum permissible leverage given to the current debt level; the higher the debt level, the lower the maximum leverage.  
  
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
    
    url = '/margin/user/loan_margin_tiers'
    query_param = 'currency_pair=BTC_USDT'
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
    url="/margin/user/loan_margin_tiers"
    query_param="currency_pair=BTC_USDT"
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
        "tier_amount": "100",
        "mmr": "0.9",
        "leverage": "1"
      }
    ]
    

##  Query current market leverage lending tiers

GET`/margin/loan_margin_tiers`

GET `/margin/loan_margin_tiers`

_Query current market leverage lending tiers_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
currency_pair | query | string | Required | Currency pair  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | [MarginLeverageTier]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | [Market gradient information]  
» _None_ | MarginLeverageTier | Market gradient information  
»» upper_limit | string | Maximum borrowing limit. Determined by the leverage you set; the lower the leverage, the larger the borrowing limit.  
»» mmr | string | Maintenance margin rate.Under tiered margin requirements(https://www.gate.com/en/help/trade/margin-trading/42357), the maintenance margin rate is a composite value.  
»» leverage | string | the maximum permissible leverage given to the current debt level; the higher the debt level, the lower the maximum leverage.  
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/margin/loan_margin_tiers'
    query_param = 'currency_pair=BTC_USDT'
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/margin/loan_margin_tiers?currency_pair=BTC_USDT \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    [
      {
        "tier_amount": "100",
        "mmr": "0.9",
        "leverage": "1"
      }
    ]
    

##  Set user market leverage multiplier🔒 Authenticated

POST`/margin/leverage/user_market_setting`

POST `/margin/leverage/user_market_setting`

_Set user market leverage multiplier_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | MarginMarketLeverage | Required | none  
↳ currency_pair | body | string | Optional | Market  
↳ leverage | body | string | Required | Position leverage  
  
### Responses

  * 204[No Content ](https://tools.ietf.org/html/rfc7231#section-6.3.5)Set successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
204 | [No Content ](https://tools.ietf.org/html/rfc7231#section-6.3.5) | Set successfully | None  
  
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
    
    url = '/margin/leverage/user_market_setting'
    query_param = ''
    body='{"currency_pair":"BTC_USDT","leverage":"10"}'
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
    url="/margin/leverage/user_market_setting"
    query_param=""
    body_param='{"currency_pair":"BTC_USDT","leverage":"10"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "currency_pair": "BTC_USDT",
      "leverage": "10"
    }
    

##  Query user's isolated margin account list🔒 Authenticated

GET`/margin/user/account`

GET `/margin/user/account`

_Query user's isolated margin account list_

Supports querying risk ratio isolated accounts and margin ratio isolated accounts

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
currency_pair | query | string | Optional | Currency pair  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)List retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [MarginAccount]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | [Margin account information for a trading pair. `base` corresponds to base currency account information, `quote` corresponds to quote currency account information]  
» _None_ | MarginAccount | Margin account information for a trading pair. `base` corresponds to base currency account information, `quote` corresponds to quote currency account information  
»» currency_pair | string | Currency pair  
»» account_type | string | Account Type mmr: maintenance margin rate account;inactive: market not activated  
»» leverage | string | User's current market leverage multiplier  
»» locked | boolean | Whether the account is locked  
»» risk | string | Deprecated  
»» mmr | string | Current Maintenance Margin Rate of the account  
»» base | MarginAccount/properties/base | Currency account information  
»»» currency | string | Currency name  
»»» available | string | Amount available for margin trading, available = margin + borrowed  
»»» locked | string | Frozen funds, such as amounts already placed in margin market for order trading  
»»» borrowed | string | Borrowed funds  
»»» interest | string | Unpaid interest  
»» quote | MarginAccount/properties/base | Currency account information  
»»» currency | string | Currency name  
»»» available | string | Amount available for margin trading, available = margin + borrowed  
»»» locked | string | Frozen funds, such as amounts already placed in margin market for order trading  
»»» borrowed | string | Borrowed funds  
»»» interest | string | Unpaid interest  
  
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
    
    url = '/margin/user/account'
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
    url="/margin/user/account"
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
        "currency_pair": "BTC_USDT",
        "account_type": "mmr",
        "leverage": "20",
        "locked": false,
        "risk": "1.3318",
        "mmr": "16.5949188975473644",
        "base": {
          "currency": "BTC",
          "available": "0.047060413211",
          "locked": "0",
          "borrowed": "0.047233",
          "interest": "0"
        },
        "quote": {
          "currency": "USDT",
          "available": "1234",
          "locked": "0",
          "borrowed": "0",
          "interest": "0"
        }
      }
    ]
    

#  Schemas

##  EstimateRate

_Estimate current hourly lending rates, returned by currency_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
**additionalProperties** | string | Optional | none | none  
      
    
    {
      "property1": "string",
      "property2": "string"
    }
    
    

##  CreateUniLoan

_Borrow or repay_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
currency | string | Required | none | Currency  
type | string | Required | none | Loan Type margin: margin borrowing  
amount | string | Required | none | Borrow or repayment amount  
repaid_all | boolean | Optional | none | Full repayment. For repayment operations only. When `true`, overrides `amount` and repays the full amount  
currency_pair | string | Required | none | Currency pair  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
type | borrow  
type | repay  
      
    
    {
      "currency": "string",
      "type": "borrow",
      "amount": "string",
      "repaid_all": true,
      "currency_pair": "string"
    }
    
    

##  UniLoanRecord

_Borrowing Records_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
type | string | Optional | read-only | Type: `borrow` \- borrow, `repay` \- repay  
currency_pair | string | Optional | read-only | Currency pair  
currency | string | Optional | read-only | Currency  
amount | string | Optional | read-only | Borrow or repayment amount  
create_time | integer(int64) | Optional | read-only | Created time  
      
    
    {
      "type": "string",
      "currency_pair": "string",
      "currency": "string",
      "amount": "string",
      "create_time": 0
    }
    
    

##  MarginAccountBook

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
id | string | Optional | none | Balance change record ID  
time | string | Optional | none | Account change timestamp  
time_ms | integer(int64) | Optional | none | The timestamp of the change (in milliseconds)  
currency | string | Optional | none | Currency changed  
currency_pair | string | Optional | none | Account trading pair  
change | string | Optional | none | Amount changed. Positive value means transferring in, while negative out  
balance | string | Optional | none | Balance after change  
type | string | Optional | none | Account book type. Please refer to account book type for more detail  
      
    
    {
      "id": "string",
      "time": "string",
      "time_ms": 0,
      "currency": "string",
      "currency_pair": "string",
      "change": "string",
      "balance": "string",
      "type": "string"
    }
    
    

##  UniLoanInterestRecord

_Interest Deduction Record_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
currency | string | Optional | read-only | Currency name  
currency_pair | string | Optional | read-only | Currency pair  
actual_rate | string | Optional | read-only | Actual Rate  
interest | string | Optional | read-only | Interest  
status | integer | Optional | read-only | Status: 0 - fail, 1 - success  
type | string | Optional | read-only | Loan Type margin: margin borrowing  
create_time | integer(int64) | Optional | read-only | Created time  
      
    
    {
      "currency": "string",
      "currency_pair": "string",
      "actual_rate": "string",
      "interest": "string",
      "status": 0,
      "type": "string",
      "create_time": 0
    }
    
    

##  MarginTransferable

_MarginTransferable_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
currency | string | Optional | none | Currency detail  
currency_pair | string | Optional | none | Currency pair  
amount | string | Optional | none | Max transferable amount  
      
    
    {
      "currency": "string",
      "currency_pair": "string",
      "amount": "string"
    }
    
    

##  MarginLeverageTier

_Market gradient information_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
upper_limit | string | Optional | none | Maximum borrowing limit. Determined by the leverage you set; the lower the leverage, the larger the borrowing limit.  
mmr | string | Optional | none | Maintenance margin rate.Under tiered margin requirements(https://www.gate.com/en/help/trade/margin-trading/42357), the maintenance margin rate is a composite value.  
leverage | string | Optional | none | the maximum permissible leverage given to the current debt level; the higher the debt level, the lower the maximum leverage.  
      
    
    {
      "upper_limit": "string",
      "mmr": "string",
      "leverage": "string"
    }
    
    

##  MaxUniBorrowable

_MaxUniBorrowable_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
currency | string | Required | read-only | Currency  
currency_pair | string | Optional | read-only | Currency pair  
borrowable | string | Required | read-only | Maximum borrowable  
      
    
    {
      "currency": "string",
      "currency_pair": "string",
      "borrowable": "string"
    }
    
    

##  FundingAccount

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
currency | string | Optional | none | Currency name  
available | string | Optional | none | Available assets to lend, which is identical to spot account `available`  
locked | string | Optional | none | Locked amount. i.e. amount in `open` loans  
lent | string | Optional | none | Outstanding loan amount yet to be repaid  
total_lent | string | Optional | none | Amount used for lending. total_lent = lent + locked  
      
    
    {
      "currency": "string",
      "available": "string",
      "locked": "string",
      "lent": "string",
      "total_lent": "string"
    }
    
    

##  MarginAccount

_Margin account information for a trading pair.`base` corresponds to base currency account information, `quote` corresponds to quote currency account information_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
currency_pair | string | Optional | none | Currency pair  
account_type | string | Optional | none | Account Type mmr: maintenance margin rate account;inactive: market not activated  
leverage | string | Optional | none | User's current market leverage multiplier  
locked | boolean | Optional | none | Whether the account is locked  
risk | string | Optional | none | Deprecated  
mmr | string | Optional | none | Current Maintenance Margin Rate of the account  
base | object | Optional | none | Currency account information  
↳ currency | string | Optional | none | Currency name  
↳ available | string | Optional | none | Amount available for margin trading, available = margin + borrowed  
↳ locked | string | Optional | none | Frozen funds, such as amounts already placed in margin market for order trading  
↳ borrowed | string | Optional | none | Borrowed funds  
↳ interest | string | Optional | none | Unpaid interest  
quote | MarginAccount/properties/base | Optional | none | Currency account information  
      
    
    {
      "currency_pair": "string",
      "account_type": "string",
      "leverage": "string",
      "locked": true,
      "risk": "string",
      "mmr": "string",
      "base": {
        "currency": "string",
        "available": "string",
        "locked": "string",
        "borrowed": "string",
        "interest": "string"
      },
      "quote": {
        "currency": "string",
        "available": "string",
        "locked": "string",
        "borrowed": "string",
        "interest": "string"
      }
    }
    
    

##  UniCurrencyPair

_Currency pair of the loan_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
currency_pair | string | Optional | read-only | Currency pair  
base_min_borrow_amount | string | Optional | read-only | Minimum borrow amount of base currency  
quote_min_borrow_amount | string | Optional | read-only | Minimum borrow amount of quote currency  
leverage | string | Optional | read-only | Position leverage  
      
    
    {
      "currency_pair": "string",
      "base_min_borrow_amount": "string",
      "quote_min_borrow_amount": "string",
      "leverage": "string"
    }
    
    

##  UniLoan

_Borrowing_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
currency | string | Optional | read-only | Currency  
currency_pair | string | Optional | read-only | Currency pair  
amount | string | Optional | read-only | Amount to Repay  
type | string | Optional | read-only | Loan type: platform borrowing - platform, margin borrowing - margin  
create_time | integer(int64) | Optional | read-only | Created time  
update_time | integer(int64) | Optional | read-only | Last Update Time  
      
    
    {
      "currency": "string",
      "currency_pair": "string",
      "amount": "string",
      "type": "string",
      "create_time": 0,
      "update_time": 0
    }
    
    

##  MarginMarketLeverage

_Market leverage settings_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
currency_pair | string | Optional | none | Market  
leverage | string | Required | none | Position leverage  
      
    
    {
      "currency_pair": "string",
      "leverage": "string"
    }