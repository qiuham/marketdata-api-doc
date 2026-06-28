---
exchange: gateio
source_url: https://www.gate.com/docs/developers/apiv4/en/earnuni
api_type: Earn
updated_at: 2026-05-27 20:15:04.719827
---

# EarnUni

Lend & Earn

##  Query lending currency list

GET`/earn/uni/currencies`

GET `/earn/uni/currencies`

_Query lending currency list_

### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | [UniCurrency]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | [Currency detail]  
» _None_ | UniCurrency | Currency detail  
»» currency | string | Currency name  
»» min_lend_amount | string | The minimum lending amount, in the unit of the currency  
»» max_lend_amount | string | The total maximum lending amount, in USDT  
»» max_rate | string | Maximum rate (Hourly)  
»» min_rate | string | Minimum rate (Hourly)  
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/earn/uni/currencies'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/earn/uni/currencies \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    [
      {
        "currency": "AE",
        "min_lend_amount": "100",
        "max_lend_amount": "200000000",
        "max_rate": "0.00057",
        "min_rate": "0.000001"
      }
    ]
    

##  Query single lending currency details

GET`/earn/uni/currencies/{currency}`

GET `/earn/uni/currencies/{currency}`

_Query single lending currency details_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
currency | path | string | Required | Currency  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | UniCurrency  
  
### Response Schema

Status Code **200**

_Currency detail_

Name | Type | Description  
---|---|---  
» currency | string | Currency name  
» min_lend_amount | string | The minimum lending amount, in the unit of the currency  
» max_lend_amount | string | The total maximum lending amount, in USDT  
» max_rate | string | Maximum rate (Hourly)  
» min_rate | string | Minimum rate (Hourly)  
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/earn/uni/currencies/btc'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/earn/uni/currencies/btc \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    {
      "currency": "AE",
      "min_lend_amount": "100",
      "max_lend_amount": "200000000",
      "max_rate": "0.00057",
      "min_rate": "0.000001"
    }
    

##  Query user's lending order list🔒 Authenticated

GET`/earn/uni/lends`

GET `/earn/uni/lends`

_Query user's lending order list_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
currency | query | string | Optional | Query by specified currency name  
page | query | integer(int32) | Optional | Page number  
limit | query | integer(int32) | Optional | Maximum number of items returned. Default: 100, minimum: 1, maximum: 100  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | [UniLend]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | [Loan record]  
» _None_ | UniLend | Loan record  
»» currency | string | Currency  
»» current_amount | string | Current amount  
»» amount | string | Total Lending Amount  
»» lent_amount | string | Lent Amount  
»» frozen_amount | string | Pending Redemption Amount  
»» min_rate | string | Minimum interest rate  
»» interest_status | string | Interest status: interest_dividend - Normal dividend, interest_reinvest - Interest reinvestment  
»» reinvest_left_amount | string | Non-reinvested Amount  
»» create_time | integer(int64) | Lending Order Creation Time  
»» update_time | integer(int64) | Lending Order Last Update Time  
  
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
    
    url = '/earn/uni/lends'
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
    url="/earn/uni/lends"
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
        "current_amount": "20.999992",
        "amount": "20.999992",
        "lent_amount": "0",
        "frozen_amount": "0",
        "min_rate": "0.1",
        "interest_status": "interest_dividend",
        "reinvest_left_amount": 0,
        "create_time": 1673247054000,
        "update_time": 1673247054000
      }
    ]
    

##  Create lending or redemption🔒 Authenticated

POST`/earn/uni/lends`

POST `/earn/uni/lends`

_Create lending or redemption_

Lending: When lending, a minimum lending rate must be set. After successful lending is determined on an hourly basis, earnings will be calculated based on the determined rate. Earnings for each hour will be settled at the top of the hour. If lending fails due to an excessively high interest rate, no interest will be earned for that hour. If funds are redeemed before the hourly for that hour. Priority: Under the same interest rate, wealth management products created or modified earlier will be prioritized for lending. Redemption: For funds that failed to be lent, redemption will be credited immediately. For funds successfully lent, they are entitled to the earnings for that hour, and redemption will be credited in the next hourly interval. Note: The two minutes before and after the hourly mark are the settlement period, during which lending and redemption are prohibited.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | CreateUniLend | Required | none  
↳ currency | body | string | Required | Currency name  
↳ amount | body | string | Required | Amount to deposit into lending pool  
↳ type | body | string | Required | Operation type: lend - Lend, redeem - Redeem  
↳ min_rate | body | string | Optional | Minimum interest rate. If set too high, lending may fail and no interest will be earned. Required for lending operations.  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
» type | lend  
» type | redeem  
  
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
    
    url = '/earn/uni/lends'
    query_param = ''
    body='{"currency":"AE","amount":"100","min_rate":"0.00001","type":"lend"}'
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
    url="/earn/uni/lends"
    query_param=""
    body_param='{"currency":"AE","amount":"100","min_rate":"0.00001","type":"lend"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "currency": "AE",
      "amount": "100",
      "min_rate": "0.00001",
      "type": "lend"
    }
    

##  Amend user lending information🔒 Authenticated

PATCH`/earn/uni/lends`

PATCH `/earn/uni/lends`

_Amend user lending information_

Currently only supports amending minimum interest rate (hourly)

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | PatchUniLend | Required | none  
↳ currency | body | string | Optional | Currency name  
↳ min_rate | body | string | Optional | Minimum interest rate  
  
### Responses

  * 204[No Content ](https://tools.ietf.org/html/rfc7231#section-6.3.5)Updated successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
204 | [No Content ](https://tools.ietf.org/html/rfc7231#section-6.3.5) | Updated successfully | None  
  
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
    
    url = '/earn/uni/lends'
    query_param = ''
    body='{"currency":"AE","min_rate":"0.0001"}'
    # for `gen_sign` implementation, refer to section `Authentication` above
    sign_headers = gen_sign('PATCH', prefix + url, query_param, body)
    headers.update(sign_headers)
    r = requests.request('PATCH', host + prefix + url, headers=headers, data=body)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="PATCH"
    url="/earn/uni/lends"
    query_param=""
    body_param='{"currency":"AE","min_rate":"0.0001"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "currency": "AE",
      "min_rate": "0.0001"
    }
    

##  Query lending transaction records🔒 Authenticated

GET`/earn/uni/lend_records`

GET `/earn/uni/lend_records`

_Query lending transaction records_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
currency | query | string | Optional | Query by specified currency name  
page | query | integer(int32) | Optional | Page number  
limit | query | integer(int32) | Optional | Maximum number of items returned. Default: 100, minimum: 1, maximum: 100  
from | query | integer(int64) | Optional | Start timestamp  
  
Specify start time, time format is Unix timestamp. If not specified, it defaults to (the data start time of the time range actually returned by to and limit)  
to | query | integer(int64) | Optional | Termination Timestamp  
  
Specify the end time. If not specified, it defaults to the current time, and the time format is a Unix timestamp  
type | query | string | Optional | Operation type: lend - Lend, redeem - Redeem  
  
####  Detailed descriptions

**from** : Start timestamp  
  
Specify start time, time format is Unix timestamp. If not specified, it defaults to (the data start time of the time range actually returned by to and limit)

**to** : Termination Timestamp  
  
Specify the end time. If not specified, it defaults to the current time, and the time format is a Unix timestamp

####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
type | lend  
type | redeem  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | [UniLendRecord]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | [Lending Record]  
» _None_ | UniLendRecord | Lending Record  
»» currency | string | Currency name  
»» amount | string | Current Amount  
»» last_wallet_amount | string | Previous Available Amount  
»» last_lent_amount | string | Previous Lent Amount  
»» last_frozen_amount | string | Previous Frozen Amount  
»» type | string | Record Type: lend - Lend, redeem - Redeem  
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
    
    url = '/earn/uni/lend_records'
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
    url="/earn/uni/lend_records"
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
        "type": "lend",
        "currency": "BTC",
        "amount": "1",
        "last_wallet_amount": "0.2",
        "last_lent_amount": "0",
        "last_frozen_amount": "0",
        "create_time": 1673247054000
      }
    ]
    

##  Query user's total interest income for specified currency🔒 Authenticated

GET`/earn/uni/interests/{currency}`

GET `/earn/uni/interests/{currency}`

_Query user's total interest income for specified currency_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
currency | path | string | Required | Currency  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | UniLendInterest  
  
### Response Schema

Status Code **200**

_UniLendInterest_

Name | Type | Description  
---|---|---  
» currency | string | Currency  
» interest | string | Interest income  
  
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
    
    url = '/earn/uni/interests/btc'
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
    url="/earn/uni/interests/btc"
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
      "currency": "AE",
      "interest": "123.345"
    }
    

##  Query user dividend records🔒 Authenticated

GET`/earn/uni/interest_records`

GET `/earn/uni/interest_records`

_Query user dividend records_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
currency | query | string | Optional | Query by specified currency name  
page | query | integer(int32) | Optional | Page number  
limit | query | integer(int32) | Optional | Maximum number of items returned. Default: 100, minimum: 1, maximum: 100  
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
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | [UniInterestRecord]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | [Interest Record]  
» _None_ | UniInterestRecord | Interest Record  
»» status | integer | Status: 0 - fail, 1 - success  
»» currency | string | Currency  
»» actual_rate | string | Actual Rate  
»» interest | string | Interest  
»» interest_status | string | Interest status: interest_dividend - Normal dividend, interest_reinvest - Interest reinvestment  
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
    
    url = '/earn/uni/interest_records'
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
    url="/earn/uni/interest_records"
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
        "currency": "AE",
        "actual_rate": "0.0005",
        "interest": "0.05",
        "interest_status": "interest_dividend",
        "create_time": 1673247054000
      }
    ]
    

##  Query currency interest compounding status🔒 Authenticated

GET`/earn/uni/interest_status/{currency}`

GET `/earn/uni/interest_status/{currency}`

_Query currency interest compounding status_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
currency | path | string | Required | Currency  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | UniCurrencyInterest  
  
### Response Schema

Status Code **200**

_UniCurrencyInterest_

Name | Type | Description  
---|---|---  
» currency | string | Currency  
» interest_status | string | Interest status: interest_dividend - Normal dividend, interest_reinvest - Interest reinvestment  
  
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
    
    url = '/earn/uni/interest_status/btc'
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
    url="/earn/uni/interest_status/btc"
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
      "currency": "BTC",
      "interest_status": "interest_dividend"
    }
    

##  UniLoan currency annualized trend chart🔒 Authenticated

GET`/earn/uni/chart`

GET `/earn/uni/chart`

_UniLoan currency annualized trend chart_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
from | query | integer(int64) | Required | Start timestamp in seconds, maximum span 30 days  
to | query | integer(int64) | Required | End timestamp in seconds, maximum span 30 days  
asset | query | string | Required | Currency name  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)none

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | [Inline]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» UniChartPoint | object | none  
»» time | integer(int64) | none  
»» value | string | none  
  
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
    
    url = '/earn/uni/chart'
    query_param = 'from=1719763200&to=1722441600&asset=BTC'
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
    url="/earn/uni/chart"
    query_param="from=1719763200&to=1722441600&asset=BTC"
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
        "time": 1719705600,
        "value": "0.01"
      }
    ]
    

##  Currency estimated annualized interest rate🔒 Authenticated

GET`/earn/uni/rate`

GET `/earn/uni/rate`

_Currency estimated annualized interest rate_

### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)none

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | [Inline]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» UniEstimatedRate | object | none  
»» currency | string | none  
»» est_rate | string | Estimated Annualized Rate, e.g., `est_rate`: `0.8014` represents an annualized rate of 80.14%  
  
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
    
    url = '/earn/uni/rate'
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
    url="/earn/uni/rate"
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
        "est_rate": "0.0226"
      }
    ]
    

#  Schemas

##  UniLend

_Loan record_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
currency | string | Optional | read-only | Currency  
current_amount | string | Optional | read-only | Current amount  
amount | string | Optional | read-only | Total Lending Amount  
lent_amount | string | Optional | read-only | Lent Amount  
frozen_amount | string | Optional | read-only | Pending Redemption Amount  
min_rate | string | Optional | read-only | Minimum interest rate  
interest_status | string | Optional | read-only | Interest status: interest_dividend - Normal dividend, interest_reinvest - Interest reinvestment  
reinvest_left_amount | string | Optional | read-only | Non-reinvested Amount  
create_time | integer(int64) | Optional | read-only | Lending Order Creation Time  
update_time | integer(int64) | Optional | read-only | Lending Order Last Update Time  
      
    
    {
      "currency": "string",
      "current_amount": "string",
      "amount": "string",
      "lent_amount": "string",
      "frozen_amount": "string",
      "min_rate": "string",
      "interest_status": "string",
      "reinvest_left_amount": "string",
      "create_time": 0,
      "update_time": 0
    }
    
    

##  UniLendRecord

_Lending Record_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
currency | string | Optional | read-only | Currency name  
amount | string | Optional | read-only | Current Amount  
last_wallet_amount | string | Optional | read-only | Previous Available Amount  
last_lent_amount | string | Optional | read-only | Previous Lent Amount  
last_frozen_amount | string | Optional | read-only | Previous Frozen Amount  
type | string | Optional | read-only | Record Type: lend - Lend, redeem - Redeem  
create_time | integer(int64) | Optional | read-only | Created time  
      
    
    {
      "currency": "string",
      "amount": "string",
      "last_wallet_amount": "string",
      "last_lent_amount": "string",
      "last_frozen_amount": "string",
      "type": "string",
      "create_time": 0
    }
    
    

##  UniInterestRecord

_Interest Record_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
status | integer | Optional | read-only | Status: 0 - fail, 1 - success  
currency | string | Optional | read-only | Currency  
actual_rate | string | Optional | read-only | Actual Rate  
interest | string | Optional | read-only | Interest  
interest_status | string | Optional | read-only | Interest status: interest_dividend - Normal dividend, interest_reinvest - Interest reinvestment  
create_time | integer(int64) | Optional | read-only | Created time  
      
    
    {
      "status": 0,
      "currency": "string",
      "actual_rate": "string",
      "interest": "string",
      "interest_status": "string",
      "create_time": 0
    }
    
    

##  UniLendInterest

_UniLendInterest_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
currency | string | Optional | read-only | Currency  
interest | string | Optional | read-only | Interest income  
      
    
    {
      "currency": "string",
      "interest": "string"
    }
    
    

##  PatchUniLend

_PatchUniLend_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
currency | string | Optional | none | Currency name  
min_rate | string | Optional | none | Minimum interest rate  
      
    
    {
      "currency": "string",
      "min_rate": "string"
    }
    
    

##  UniCurrency

_Currency detail_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
currency | string | Optional | read-only | Currency name  
min_lend_amount | string | Optional | read-only | The minimum lending amount, in the unit of the currency  
max_lend_amount | string | Optional | read-only | The total maximum lending amount, in USDT  
max_rate | string | Optional | read-only | Maximum rate (Hourly)  
min_rate | string | Optional | read-only | Minimum rate (Hourly)  
      
    
    {
      "currency": "string",
      "min_lend_amount": "string",
      "max_lend_amount": "string",
      "max_rate": "string",
      "min_rate": "string"
    }
    
    

##  CreateUniLend

_Create lending or redemption_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
currency | string | Required | none | Currency name  
amount | string | Required | none | Amount to deposit into lending pool  
type | string | Required | none | Operation type: lend - Lend, redeem - Redeem  
min_rate | string | Optional | none | Minimum interest rate. If set too high, lending may fail and no interest will be earned. Required for lending operations.  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
type | lend  
type | redeem  
      
    
    {
      "currency": "string",
      "amount": "string",
      "type": "lend",
      "min_rate": "string"
    }
    
    

##  UniCurrencyInterest

_UniCurrencyInterest_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
currency | string | Optional | read-only | Currency  
interest_status | string | Optional | read-only | Interest status: interest_dividend - Normal dividend, interest_reinvest - Interest reinvestment  
      
    
    {
      "currency": "string",
      "interest_status": "string"
    }