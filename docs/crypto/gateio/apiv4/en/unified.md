---
exchange: gateio
source_url: https://www.gate.com/docs/developers/apiv4/en/unified
api_type: Account
updated_at: 2026-05-27 20:16:16.622605
---

# Unified

Unified account

##  Get unified account information🔒 Authenticated

GET`/unified/accounts`

GET `/unified/accounts`

Get `unified account information`

The assets of each currency in the account will be adjusted according to their liquidity, defined by corresponding adjustment coefficients, and then uniformly converted to USD to calculate the total asset value and position value of the account.

For specific formulas, please refer to Margin Formula

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
currency | query | string | Optional | Query by specified currency name  
sub_uid | query | string | Optional | Sub account user ID  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)List retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | UnifiedAccount  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» mode | string | Unified account mode:  
\- classic: Classic account mode  
\- multi_currency: Multi-currency margin mode  
\- portfolio: Portfolio margin mode  
\- single_currency: Single-currency margin mode  
» user_id | integer(int64) | User ID  
» refresh_time | integer(int64) | Last refresh time  
» locked | boolean | Whether the account is locked, valid in cross-currency margin/combined margin mode, false in other modes such as single-currency margin mode  
» balances | object | none  
»» UnifiedBalance | object | none  
»»» available | string | Cross available balance, deducted futures isolated margin occupation and frozen amount (futures isolated occupation, i.e. futures isolated balance), effective in single-currency/multi-currency/portfolio margin mode.  
»»» freeze | string | Frozen amount, effective in single-currency/multi-currency/portfolio margin mode  
»»» borrowed | string | Borrowed amount, valid in cross-currency margin/combined margin mode, 0 in other modes such as single-currency margin mode  
»»» negative_liab | string | Negative balance borrowing, valid in cross-currency margin/combined margin mode, 0 in other modes such as single-currency margin mode  
»»» futures_pos_liab | string | Contract opening position borrowing currency (abandoned, to be offline field)  
»»» equity | string | Currency equity amount (cross), effective in single-currency/multi-currency/portfolio margin mode  
»»» total_freeze | string | Total frozen (deprecated, to be removed)  
»»» total_liab | string | Total borrowed amount, valid in cross-currency margin/combined margin mode, 0 in other modes such as single-currency margin mode  
»»» spot_in_use | string | The amount of spot hedging is valid in the combined margin mode, and is 0 in other margin modes such as single currency and cross-currency margin modes  
»»» funding | string | Uniloan financial management amount, effective when turned on as a unified account margin switch  
»»» funding_version | string | Funding version  
»»» cross_balance | string | Full margin balance is valid in single currency margin mode, and is 0 in other modes such as cross currency margin/combined margin mode  
»»» iso_balance | string | Futures isolated balance, effective in single-currency and multi-currency margin mode, 0 in portfolio margin mode  
»»» im | string | Cross initial margin, only effective for USDT in single-currency margin mode, 0 in multi-currency/portfolio margin mode  
»»» mm | string | Cross maintenance margin, only effective for USDT in single-currency margin mode, 0 in multi-currency/portfolio margin mode  
»»» imr | string | Cross initial margin rate, only effective for USDT in single-currency margin mode, 0 in multi-currency/portfolio margin mode  
»»» mmr | string | Cross maintenance margin rate, only effective for USDT in single-currency margin mode, 0 in multi-currency/portfolio margin mode  
»»» margin_balance | string | Cross margin balance, only effective for USDT in single-currency margin mode, 0 in multi-currency/portfolio margin mode  
»»» available_margin | string | Cross available margin, only effective for USDT in single-currency margin mode, 0 in multi-currency/portfolio margin mode  
»»» enabled_collateral | boolean | Currency enabled as margin: true - Enabled, false - Disabled  
»»» balance_version | number(int64) | Balance version number  
»» total | string | Total account assets converted to USD, i.e. the sum of `(available + freeze) * price` in all currencies (deprecated, to be removed, replaced by unified_account_total)  
»» borrowed | string | Total borrowed amount converted to USD, i.e. the sum of `borrowed * price` of all currencies (excluding point cards), valid in cross-currency margin/combined margin mode, 0 in other modes such as single-currency margin mode  
»» total_initial_margin | string | Total initial margin (cross), effective in multi-currency margin/portfolio margin mode, 0 in single-currency margin mode  
»» total_margin_balance | string | Total margin balance (cross), effective in multi-currency margin/portfolio margin mode, 0 in single-currency margin mode  
»» total_maintenance_margin | string | Total maintenance margin (cross), effective in multi-currency margin/portfolio margin mode, 0 in single-currency margin mode  
»» total_initial_margin_rate | string | Total initial margin rate (cross), effective in multi-currency margin/portfolio margin mode, 0 in single-currency margin mode  
»» total_maintenance_margin_rate | string | Total maintenance margin rate (cross), effective in multi-currency margin/portfolio margin mode, 0 in single-currency margin mode  
»» total_available_margin | string | Available margin amount, valid in cross-currency margin/combined margin mode, 0 in other modes such as single-currency margin mode  
»» unified_account_total | string | Total unified account assets, includes both cross and isolated total assets in single-currency/multi-currency mode, only cross total assets in portfolio margin mode  
»» unified_account_total_liab | string | Total unified account borrowed, i.e. total cross borrowed, effective in multi-currency margin/portfolio margin mode, 0 in single-currency margin mode  
»» unified_account_total_equity | string | Total unified account equity, includes both cross and isolated total equity in single-currency/multi-currency mode, only cross total equity in portfolio margin mode  
»» leverage | string | Account leverage multiplier, effective in multi-currency/portfolio margin mode (deprecated). Currency leverage query API: GET /unified/leverage/user_currency_setting  
»» spot_order_loss | string | Spot Pending Order Loss, in USDT, effective only in Cross-Currency Margin Mode and Portfolio Margin Mode.  
»» options_order_loss | string | Option Pending Order Loss, in USDT, effective only in Portfolio Margin Mode.  
»» spot_hedge | boolean | Spot hedging status: true - enabled, false - disabled  
»» use_funding | boolean | Whether to use Earn funds as margin  
»» is_all_collateral | boolean | Whether all currencies are used as margin: true - all currencies as margin, false - no  
  
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
    
    url = '/unified/accounts'
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
    url="/unified/accounts"
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
      "user_id": 10001,
      "locked": false,
      "balances": {
        "ETH": {
          "available": "0",
          "freeze": "0",
          "borrowed": "0.075393666654",
          "negative_liab": "0",
          "futures_pos_liab": "0",
          "equity": "1016.1",
          "total_freeze": "0",
          "total_liab": "0",
          "spot_in_use": "1.111"
        },
        "POINT": {
          "available": "9999999999.017023138734",
          "freeze": "0",
          "borrowed": "0",
          "negative_liab": "0",
          "futures_pos_liab": "0",
          "equity": "12016.1",
          "total_freeze": "0",
          "total_liab": "0",
          "spot_in_use": "12"
        },
        "USDT": {
          "available": "0.00000062023",
          "freeze": "0",
          "borrowed": "0",
          "negative_liab": "0",
          "futures_pos_liab": "0",
          "equity": "16.1",
          "total_freeze": "0",
          "total_liab": "0",
          "spot_in_use": "12"
        }
      },
      "total": "230.94621713",
      "borrowed": "161.66395521",
      "total_initial_margin": "1025.0524665088",
      "total_margin_balance": "3382495.944473949183",
      "total_maintenance_margin": "205.01049330176",
      "total_initial_margin_rate": "3299.827135672679",
      "total_maintenance_margin_rate": "16499.135678363399",
      "total_available_margin": "3381470.892007440383",
      "unified_account_total": "3381470.892007440383",
      "unified_account_total_liab": "0",
      "unified_account_total_equity": "100016.1",
      "leverage": "2",
      "spot_order_loss": "12",
      "spot_hedge": false
    }
    

##  Query maximum borrowable amount for unified account🔒 Authenticated

GET`/unified/borrowable`

GET `/unified/borrowable`

_Query maximum borrowable amount for unified account_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
currency | query | string | Required | Query by specified currency name  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | UnifiedBorrowable  
  
### Response Schema

Status Code **200**

_UnifiedBorrowable_

Name | Type | Description  
---|---|---  
» currency | string | Currency detail  
» amount | string | Max borrowable amount  
  
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
    
    url = '/unified/borrowable'
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
    url="/unified/borrowable"
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
      "amount": "10000"
    }
    

##  Query maximum transferable amount for unified account🔒 Authenticated

GET`/unified/transferable`

GET `/unified/transferable`

_Query maximum transferable amount for unified account_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
currency | query | string | Required | Query by specified currency name  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | UnifiedTransferable  
  
### Response Schema

Status Code **200**

_UnifiedTransferable_

Name | Type | Description  
---|---|---  
» currency | string | Currency detail  
» amount | string | Maximum transferable amount  
  
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
    
    url = '/unified/transferable'
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
    url="/unified/transferable"
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
      "amount": "10000"
    }
    

##  Batch query maximum transferable amount for unified accounts. Each currency shows the maximum value. After user withdrawal, the transferable amount for all currencies will change🔒 Authenticated

GET`/unified/transferables`

GET `/unified/transferables`

_Batch query maximum transferable amount for unified accounts. Each currency shows the maximum value. After user withdrawal, the transferable amount for all currencies will change_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
currencies | query | string | Required | Specify the currency name to query in batches, and support up to 100 pass parameters at a time  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | [Inline]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» TransferablesResult | object | Batch query unified account maximum transferable results  
»» currency | string | Currency detail  
»» amount | string | Maximum transferable amount  
  
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
    
    url = '/unified/transferables'
    query_param = 'currencies=BTC,ETH'
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
    url="/unified/transferables"
    query_param="currencies=BTC,ETH"
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
        "amount": "123456"
      }
    ]
    

##  Batch query unified account maximum borrowable amount🔒 Authenticated

GET`/unified/batch_borrowable`

GET `/unified/batch_borrowable`

_Batch query unified account maximum borrowable amount_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
currencies | query | array[string] | Required | Specify currency names for querying in an array, separated by commas, maximum 10 currencies  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | [UnifiedBorrowable]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | [Maximum borrowable amount for unified account]  
» UnifiedBorrowable | UnifiedBorrowable | Maximum borrowable amount for unified account  
»» currency | string | Currency detail  
»» amount | string | Max borrowable amount  
  
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
    
    url = '/unified/batch_borrowable'
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
    url="/unified/batch_borrowable"
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
    
    
    [
      {
        "currency": "BTC",
        "amount": "123456"
      }
    ]
    

##  Query loans🔒 Authenticated

GET`/unified/loans`

GET `/unified/loans`

_Query loans_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
currency | query | string | Optional | Query by specified currency name  
page | query | integer(int32) | Optional | Page number  
limit | query | integer(int32) | Optional | Maximum number of items returned. Default: 100, minimum: 1, maximum: 100  
type | query | string | Optional | Loan type: platform borrowing - platform, margin borrowing - margin  
  
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
    
    url = '/unified/loans'
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
    url="/unified/loans"
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

POST`/unified/loans`

POST `/unified/loans`

_Borrow or repay_

When borrowing, ensure the borrowed amount is not below the minimum borrowing threshold for the specific cryptocurrency and does not exceed the maximum borrowing limit set by the platform and user.

Loan interest will be automatically deducted from the account at regular intervals. Users are responsible for managing repayment of borrowed amounts.

For repayment, use `repaid_all=true` to repay all available amounts

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | UnifiedLoan | Required | none  
↳ currency | body | string | Required | Currency  
↳ type | body | string | Required | Type: `borrow` \- borrow, `repay` \- repay  
↳ amount | body | string | Required | Borrow or repayment amount  
↳ repaid_all | body | boolean | Optional | Full repayment, only used for repayment operations. When set to `true`, overrides `amount` and directly repays the full amount  
↳ text | body | string | Optional | User defined custom ID  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
» type | borrow  
» type | repay  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Operation successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Operation successful | UnifiedLoanResult  
  
### Response Schema

Status Code **200**

_Unified account borrowing and repayment response result_

Name | Type | Description  
---|---|---  
» tran_id | integer(int64) | Transaction ID  
  
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
    
    url = '/unified/loans'
    query_param = ''
    body='{"currency":"BTC","amount":"0.1","type":"borrow","repaid_all":false,"text":"t-test"}'
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
    url="/unified/loans"
    query_param=""
    body_param='{"currency":"BTC","amount":"0.1","type":"borrow","repaid_all":false,"text":"t-test"}'
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
      "repaid_all": false,
      "text": "t-test"
    }
    

> Example responses

> 200 Response
    
    
    {
      "tran_id": 9527
    }
    

##  Query loan records🔒 Authenticated

GET`/unified/loan_records`

GET `/unified/loan_records`

_Query loan records_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
type | query | string | Optional | Loan record type: borrow - borrowing, repay - repayment  
currency | query | string | Optional | Query by specified currency name  
page | query | integer(int32) | Optional | Page number  
limit | query | integer(int32) | Optional | Maximum number of items returned. Default: 100, minimum: 1, maximum: 100  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | [UnifiedLoanRecord]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | [Borrowing Records]  
» _None_ | UnifiedLoanRecord | Borrowing Records  
»» id | integer(int64) | id  
»» type | string | Type: `borrow` \- borrow, `repay` \- repay  
»» repayment_type | string | Repayment type: none - No repayment type, manual_repay - Manual repayment, auto_repay - Automatic repayment, cancel_auto_repay - Automatic repayment after order cancellation, different_currencies_repayment - Cross-currency repayment  
»» borrow_type | string | Borrowing type, returned when querying loan records: manual_borrow - Manual borrowing, auto_borrow - Automatic borrowing  
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
    
    url = '/unified/loan_records'
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
    url="/unified/loan_records"
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
        "id": 16442,
        "type": "borrow",
        "margin_mode": "cross",
        "currency_pair": "AE_USDT",
        "currency": "USDT",
        "amount": "1000",
        "create_time": 1673247054000,
        "repayment_type": "auto_repay"
      }
    ]
    

##  Query interest deduction records🔒 Authenticated

GET`/unified/interest_records`

GET `/unified/interest_records`

_Query interest deduction records_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
currency | query | string | Optional | Query by specified currency name  
page | query | integer(int32) | Optional | Page number  
limit | query | integer(int32) | Optional | Maximum number of items returned. Default: 100, minimum: 1, maximum: 100  
from | query | integer(int64) | Optional | Start timestamp for the query  
to | query | integer(int64) | Optional | End timestamp for the query, defaults to current time if not specified  
type | query | string | Optional | Loan type: platform borrowing - platform, margin borrowing - margin. Defaults to margin if not specified  
  
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
    
    url = '/unified/interest_records'
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
    url="/unified/interest_records"
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
    

##  Get user risk unit details🔒 Authenticated

GET`/unified/risk_units`

GET `/unified/risk_units`

Get `user risk unit details`

Get `user risk unit details, only valid in portfolio margin mode`

### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | UnifiedRiskUnits  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» user_id | integer(int64) | User ID  
» spot_hedge | boolean | Spot hedging status: true - enabled, false - disabled  
» risk_units | array | Risk unit  
»» RiskUnits | object | none  
»»» symbol | string | Risk unit flag  
»»» spot_in_use | string | Spot hedging occupied amount  
»»» maintain_margin | string | Maintenance margin for risk unit  
»»» initial_margin | string | Initial margin for risk unit  
»»» delta | string | Total Delta of risk unit  
»»» gamma | string | Total Gamma of risk unit  
»»» theta | string | Total Theta of risk unit  
»»» vega | string | Total Vega of risk unit  
  
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
    
    url = '/unified/risk_units'
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
    url="/unified/risk_units"
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
      "user_id": 0,
      "spot_hedge": true,
      "risk_units": [
        {
          "symbol": "BTC",
          "spot_in_use": "-13500.000001223",
          "maintain_margin": "2334.002",
          "initial_margin": "2334.002",
          "delta": "0.22",
          "gamma": "0.42",
          "theta": "0.29",
          "vega": "0.22"
        }
      ]
    }
    

##  Query mode of the unified account🔒 Authenticated

GET`/unified/unified_mode`

GET `/unified/unified_mode`

_Query mode of the unified account_

Unified account mode:

  * `classic`: Classic account mode
  * `multi_currency`: Cross-currency margin mode
  * `portfolio`: Portfolio margin mode
  * `single_currency`: Single-currency margin mode

### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | UnifiedModeSet  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» mode | string | Unified account mode:   
\- `classic`: Classic account mode  
\- `multi_currency`: Cross-currency margin mode  
\- `portfolio`: Portfolio margin mode  
\- `single_currency`: Single-currency margin mode  
» settings | object | none  
»» usdt_futures | boolean | USDT futures switch. In cross-currency margin mode, can only be enabled and cannot be disabled  
»» spot_hedge | boolean | Spot hedging switch  
»» use_funding | boolean | Earn switch, when mode is cross-currency margin mode, whether to use Earn funds as margin  
»» options | boolean | Options switch. In cross-currency margin mode, can only be enabled and cannot be disabled  
  
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
    
    url = '/unified/unified_mode'
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
    url="/unified/unified_mode"
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
      "mode": "portfolio",
      "settings": {
        "spot_hedge": true,
        "usdt_futures": true,
        "options": true
      }
    }
    

##  Set unified account mode🔒 Authenticated

PUT`/unified/unified_mode`

PUT `/unified/unified_mode`

_Set unified account mode_

Each account mode switch only requires passing the corresponding account mode parameter, and also supports turning on or off the configuration switches under the corresponding account mode during the switch.

  * When enabling the classic account mode, mode=classic

    
    
     PUT /unified/unified_mode
     {
     "mode": "classic"
     }
    

  * When enabling the cross-currency margin "multi_currency", "settings": { "usdt_futures": true } }

    
    
    - When enabling the portfolio margin mode, mode=portfolio
    

PUT `/unified/unified_mode { "mode": "portfolio", "settings": { "spot_hedge": true } }`
    
    
    - When enabling the single-currency margin mode, mode=single_currency
    

PUT `/unified/unified_mode { "mode": "single_currency" }`
    
    
    <Example>
    
    > Body parameter
    
    ```json
    {
      "mode": "portfolio",
      "settings": {
        "spot_hedge": true,
        "usdt_futures": true,
        "options": true
      }
    }
    

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | UnifiedModeSet | Required | none  
↳ mode | body | string | Required | Unified account mode:   
\- `classic`: Classic account mode  
\- `multi_currency`: Cross-currency margin mode  
\- `portfolio`: Portfolio margin mode  
\- `single_currency`: Single-currency margin mode  
↳ settings | body | object | Optional | none  
↳ usdt_futures | body | boolean | Optional | USDT futures switch. In cross-currency margin mode, can only be enabled and cannot be disabled  
↳ spot_hedge | body | boolean | Optional | Spot hedging switch  
↳ use_funding | body | boolean | Optional | Earn switch, when mode is cross-currency margin mode, whether to use Earn funds as margin  
↳ options | body | boolean | Optional | Options switch. In cross-currency margin mode, can only be enabled and cannot be disabled  
  
####  Detailed descriptions

**» mode** : Unified account mode:   
\- `classic`: Classic account mode  
\- `multi_currency`: Cross-currency margin mode  
\- `portfolio`: Portfolio margin mode  
\- `single_currency`: Single-currency margin mode

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
    
    url = '/unified/unified_mode'
    query_param = ''
    body='{"mode":"portfolio","settings":{"spot_hedge":true,"usdt_futures":true,"options":true}}'
    # for `gen_sign` implementation, refer to section `Authentication` above
    sign_headers = gen_sign('PUT', prefix + url, query_param, body)
    headers.update(sign_headers)
    r = requests.request('PUT', host + prefix + url, headers=headers, data=body)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="PUT"
    url="/unified/unified_mode"
    query_param=""
    body_param='{"mode":"portfolio","settings":{"spot_hedge":true,"usdt_futures":true,"options":true}}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

##  Query unified account estimated interest rate🔒 Authenticated

GET`/unified/estimate_rate`

GET `/unified/estimate_rate`

_Query unified account estimated interest rate_

Interest rates fluctuate hourly based on lending depth, so exact rates cannot be provided. When a currency is not supported, the interest rate returned will be an empty string

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
currencies | query | array[string] | Required | Specify currency names for querying in an array, separated by commas, maximum 10 currencies  
  
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
    
    url = '/unified/estimate_rate'
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
    url="/unified/estimate_rate"
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
      "GT": "0.000001",
      "ETH": ""
    }
    

##  Query unified account tiered

GET`/unified/currency_discount_tiers`

GET `/unified/currency_discount_tiers`

_Query unified account tiered_

### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | [UnifiedDiscount]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | [Unified account tiered discount]  
» _None_ | UnifiedDiscount | Unified account tiered discount  
»» currency | string | Currency name  
»» discount_tiers | array | Tiered discount  
»»» tier | string | Tier  
»»» discount | string | Discount  
»»» lower_limit | string | Lower limit  
»»» upper_limit | string | Upper limit, + indicates positive infinity  
»»» leverage | string | Position leverage  
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/unified/currency_discount_tiers'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/unified/currency_discount_tiers \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    [
      [
        {
          "currency": "USDT",
          "discount_tiers": [
            {
              "tier": "1",
              "discount": "1",
              "lower_limit": "0",
              "leverage": "10",
              "upper_limit": "+"
            }
          ]
        },
        {
          "currency": "USDC",
          "discount_tiers": [
            {
              "tier": "1",
              "discount": "1",
              "lower_limit": "0",
              "leverage": "10",
              "upper_limit": "10000000"
            },
            {
              "tier": "2",
              "discount": "0.98",
              "lower_limit": "10000000",
              "leverage": "10",
              "upper_limit": "15000000"
            },
            {
              "tier": "3",
              "discount": "0.95",
              "lower_limit": "15000000",
              "leverage": "10",
              "upper_limit": "20000000"
            },
            {
              "tier": "4",
              "discount": "0.925",
              "lower_limit": "20000000",
              "leverage": "10",
              "upper_limit": "50000000"
            },
            {
              "tier": "5",
              "discount": "0.9",
              "lower_limit": "50000000",
              "leverage": "10",
              "upper_limit": "100000000"
            },
            {
              "tier": "6",
              "discount": "0",
              "lower_limit": "100000000",
              "leverage": "10",
              "upper_limit": "+"
            }
          ]
        },
        {
          "currency": "BTC",
          "discount_tiers": [
            {
              "tier": "1",
              "discount": "0.98",
              "lower_limit": "0",
              "leverage": "10",
              "upper_limit": "1000"
            },
            {
              "tier": "2",
              "discount": "0.95",
              "lower_limit": "1000",
              "leverage": "10",
              "upper_limit": "10000"
            },
            {
              "tier": "3",
              "discount": "0.9",
              "lower_limit": "10000",
              "leverage": "10",
              "upper_limit": "50000"
            },
            {
              "tier": "4",
              "discount": "0.85",
              "lower_limit": "50000",
              "leverage": "10",
              "upper_limit": "+"
            }
          ]
        },
        {
          "currency": "ETH",
          "discount_tiers": [
            {
              "tier": "1",
              "discount": "0.98",
              "lower_limit": "0",
              "leverage": "10",
              "upper_limit": "1000"
            },
            {
              "tier": "2",
              "discount": "0.95",
              "lower_limit": "1000",
              "leverage": "10",
              "upper_limit": "10000"
            },
            {
              "tier": "3",
              "discount": "0.9",
              "lower_limit": "10000",
              "leverage": "10",
              "upper_limit": "50000"
            },
            {
              "tier": "4",
              "discount": "0.85",
              "lower_limit": "50000",
              "leverage": "10",
              "upper_limit": "+"
            }
          ]
        }
      ]
    ]
    

##  Query unified account tiered loan margin

GET`/unified/loan_margin_tiers`

GET `/unified/loan_margin_tiers`

_Query unified account tiered loan margin_

### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | [UnifiedMarginTiers]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | [Unified account borrowing margin tiers]  
» _None_ | UnifiedMarginTiers | Unified account borrowing margin tiers  
»» currency | string | Currency name  
»» margin_tiers | array | Tiered margin  
»»» MarginTiers | object | none  
»»»» tier | string | Tier  
»»»» margin_rate | string | Discount  
»»»» lower_limit | string | Lower limit  
»»»» upper_limit | string | Upper limit, `` indicates greater than (the last tier)  
»»»» leverage | string | Position leverage  
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/unified/loan_margin_tiers'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/unified/loan_margin_tiers \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    [
      {
        "currency": "USDT",
        "margin_tiers": [
          {
            "tier": "1",
            "margin_rate": "0.02",
            "lower_limit": "200000",
            "upper_limit": "400000",
            "leverage": "3"
          }
        ]
      }
    ]
    

##  Portfolio margin calculator

POST`/unified/portfolio_calculator`

POST `/unified/portfolio_calculator`

_Portfolio margin calculator_

Portfolio Margin Calculator

This interface calculates maintenance and initial margin requirements under the portfolio margin model for custom simulated position and order portfolios. It currently supports all underlying currencies with active options trading. Each simulated position requires a name and holding quantity; each simulated pending order requires a market identifier, price, and quantity. Market orders are not supported.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | UnifiedPortfolioInput | Required | none  
↳ spot_balances | body | array | Optional | Spot  
↳ None | body | object | Optional | Spot  
↳ currency | body | string | Required | Currency name  
↳ equity | body | string | Required | Currency equity, where equity = balance - borrowed, represents the net delta exposure of your spot positions  
↳ spot_orders | body | array | Optional | Spot orders  
↳ None | body | object | Optional | Spot orders  
↳ currency_pairs | body | string | Required | Market  
↳ order_price | body | string | Required | Price  
↳ count | body | string | Optional | Initial order quantity for spot trading pairs, not involved in actual calculation.  
↳ left | body | string | Required | Unfilled quantity, involved in actual calculation  
↳ type | body | string | Required | Order type, sell - sell order, buy - buy order  
↳ futures_positions | body | array | Optional | Futures positions  
↳ None | body | object | Optional | Futures positions  
↳ contract | body | string | Required | Perpetual contract name. Only USDT perpetual contracts for underlying currencies with active options trading are supported.  
↳ size | body | string | Required | Position size, measured in contract quantity  
↳ futures_orders | body | array | Optional | Futures order  
↳ None | body | object | Optional | Futures order  
↳ contract | body | string | Required | Perpetual contract name. Only USDT perpetual contracts for underlying currencies with active options trading are supported.  
↳ size | body | string | Required | Contract quantity, representing the initial order quantity, not involved in actual settlement  
↳ left | body | string | Required | Unfilled contract quantity, involved in actual calculation  
↳ options_positions | body | array | Optional | Options positions  
↳ None | body | object | Optional | Options positions  
↳ options_name | body | string | Required | Options contract name. Currently supports all options contract markets.  
↳ size | body | string | Required | Position size, measured in contract quantity  
↳ options_orders | body | array | Optional | Option orders  
↳ None | body | object | Optional | Option orders  
↳ options_name | body | string | Required | Options contract name. Currently supports all options contract markets.  
↳ size | body | string | Required | Initial order quantity, not involved in actual calculation  
↳ left | body | string | Required | Unfilled contract quantity, involved in actual calculation  
↳ spot_hedge | body | boolean | Optional | Whether to enable spot hedging  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | UnifiedPortfolioOutput  
  
### Response Schema

Status Code **200**

_Portfolio margin calculator output_

Name | Type | Description  
---|---|---  
» maintain_margin_total | string | Total maintenance margin, including only portfolio margin calculation results for positions in risk units, excluding borrowing margin. If borrowing exists, conventional borrowing margin requirements will still apply  
» initial_margin_total | string | Total initial margin, calculated as the maximum of the following three combinations: position, position + positive delta orders, position + negative delta orders  
» calculate_time | integer(int64) | Calculation time  
» risk_unit | array | Risk unit  
»» _None_ | object | Risk unit  
»»» symbol | string | Risk unit name  
»»» spot_in_use | string | Spot hedge usage  
»»» maintain_margin | string | Maintenance margin  
»»» initial_margin | string | Initial margin  
»»» margin_result | array | Margin result  
»»»» _None_ | object | Margin result  
»»»»» type | string | Position combination type  
`original_position` \- Original position  
`long_delta_original_position` \- Positive delta + Original position  
`short_delta_original_position` \- Negative delta + Original position  
»»»»» profit_loss_ranges | array | Results of 33 stress scenarios for MR1  
»»»»»» _None_ | UnifiedPortfolioOutput/properties/risk_unit/items/properties/margin_result/items/properties/profit_loss_ranges/items | Profit and loss range  
»»»»»»» price_percentage | string | Percentage change in price  
»»»»»»» implied_volatility_percentage | string | Percentage change in implied volatility  
»»»»»»» profit_loss | string | PnL  
»»»»»» max_loss | UnifiedPortfolioOutput/properties/risk_unit/items/properties/margin_result/items/properties/profit_loss_ranges/items | Profit and loss range  
»»»»»»» price_percentage | string | Percentage change in price  
»»»»»»» implied_volatility_percentage | string | Percentage change in implied volatility  
»»»»»»» profit_loss | string | PnL  
»»»»»» mr1 | string | Stress testing  
»»»»»» mr2 | string | Basis spread risk  
»»»»»» mr3 | string | Volatility spread risk  
»»»»»» mr4 | string | Option short risk  
»»»»» delta | string | Total Delta of risk unit  
»»»»» gamma | string | Total Gamma of risk unit  
»»»»» theta | string | Total Theta of risk unit  
»»»»» vega | string | Total Vega of risk unit  
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/unified/portfolio_calculator'
    query_param = ''
    body='{"spot_balances":[{"currency":"BTC","equity":"-1","freeze":"10"}],"spot_orders":[{"currency_pairs":"BTC_USDT","order_price":"344","size":"100","left":"100","type":"sell"}],"futures_positions":[{"contract":"BTC_USDT","size":"100"}],"futures_orders":[{"contract":"BTC_USDT","size":"10","left":"8"}],"options_positions":[{"options_name":"BTC_USDT-20240329-32000-C","size":"10"}],"options_orders":[{"options_name":"BTC_USDT-20240329-32000-C","size":"100","left":"80"}],"spot_hedge":false}'
    r = requests.request('POST', host + prefix + url, headers=headers, data=body)
    print(r.json())
    
    
    
    
    curl -X POST https://api.gateio.ws/api/v4/unified/portfolio_calculator \
      -H 'Content-Type: application/json' \
      -H 'Accept: application/json'
    
    

> Body parameter
    
    
    {
      "spot_balances": [
        {
          "currency": "BTC",
          "equity": "-1",
          "freeze": "10"
        }
      ],
      "spot_orders": [
        {
          "currency_pairs": "BTC_USDT",
          "order_price": "344",
          "size": "100",
          "left": "100",
          "type": "sell"
        }
      ],
      "futures_positions": [
        {
          "contract": "BTC_USDT",
          "size": "100"
        }
      ],
      "futures_orders": [
        {
          "contract": "BTC_USDT",
          "size": "10",
          "left": "8"
        }
      ],
      "options_positions": [
        {
          "options_name": "BTC_USDT-20240329-32000-C",
          "size": "10"
        }
      ],
      "options_orders": [
        {
          "options_name": "BTC_USDT-20240329-32000-C",
          "size": "100",
          "left": "80"
        }
      ],
      "spot_hedge": false
    }
    

> Example responses

> 200 Response
    
    
    {
      "maintain_margin_total": "0.000000000000",
      "initial_margin_total": "0.000000000000",
      "calculate_time": "1709014486",
      "risk_unit": [
        {
          "symbol": "BTC",
          "margin_result": [
            {
              "type": "original_position",
              "profit_loss_ranges": [
                {
                  "price_percentage": "-0.200000000000",
                  "implied_volatility_percentage": "-0.300000000000",
                  "profit_loss": "0.000000000000"
                },
                {
                  "price_percentage": "-0.160000000000",
                  "implied_volatility_percentage": "-0.300000000000",
                  "profit_loss": "0.000000000000"
                },
                {
                  "price_percentage": "-0.120000000000",
                  "implied_volatility_percentage": "-0.300000000000",
                  "profit_loss": "0.000000000000"
                },
                {
                  "price_percentage": "-0.080000000000",
                  "implied_volatility_percentage": "-0.300000000000",
                  "profit_loss": "0.000000000000"
                },
                {
                  "price_percentage": "-0.040000000000",
                  "implied_volatility_percentage": "-0.300000000000",
                  "profit_loss": "0.000000000000"
                },
                {
                  "price_percentage": "0.000000000000",
                  "implied_volatility_percentage": "-0.300000000000",
                  "profit_loss": "0.000000000000"
                },
                {
                  "price_percentage": "0.040000000000",
                  "implied_volatility_percentage": "-0.300000000000",
                  "profit_loss": "0.000000000000"
                },
                {
                  "price_percentage": "0.080000000000",
                  "implied_volatility_percentage": "-0.300000000000",
                  "profit_loss": "0.000000000000"
                },
                {
                  "price_percentage": "0.120000000000",
                  "implied_volatility_percentage": "-0.300000000000",
                  "profit_loss": "0.000000000000"
                },
                {
                  "price_percentage": "0.160000000000",
                  "implied_volatility_percentage": "-0.300000000000",
                  "profit_loss": "0.000000000000"
                },
                {
                  "price_percentage": "0.200000000000",
                  "implied_volatility_percentage": "-0.300000000000",
                  "profit_loss": "0.000000000000"
                }
              ],
              "max_loss": {
                "price_percentage": "-0.200000000000",
                "implied_volatility_percentage": "-0.300000000000",
                "profit_loss": "0.000000000000"
              },
              "mr1": "0.000000000000",
              "mr2": "0.000000000000",
              "mr3": "0.000000000000",
              "mr4": "0.000000000000"
            }
          ],
          "maintain_margin": "0.000000000000",
          "initial_margin": "0.000000000000"
        }
      ]
    }
    

##  Maximum and minimum currency leverage that can be set🔒 Authenticated

GET`/unified/leverage/user_currency_config`

GET `/unified/leverage/user_currency_config`

_Maximum and minimum currency leverage that can be set_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
currency | query | string | Required | Currency  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | UnifiedLeverageConfig  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» current_leverage | string | Current leverage ratio  
» min_leverage | string | Minimum adjustable leverage ratio  
» max_leverage | string | Maximum adjustable leverage ratio  
» debit | string | Current liabilities  
» available_margin | string | Available Margin  
» borrowable | string | Maximum borrowable amount at current leverage  
» except_leverage_borrowable | string | Maximum borrowable from margin and maximum borrowable from Earn, whichever is smaller  
  
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
    
    url = '/unified/leverage/user_currency_config'
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
    url="/unified/leverage/user_currency_config"
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
      "current_leverage": "2",
      "min_leverage": "0",
      "max_leverage": "0",
      "debit": "0",
      "available_margin": "0",
      "borrowable": "0",
      "except_leverage_borrowable": "0"
    }
    

##  Get user currency leverage🔒 Authenticated

GET`/unified/leverage/user_currency_setting`

GET `/unified/leverage/user_currency_setting`

Get `user currency leverage`

Get `user currency leverage. If currency is not specified, query all currencies`

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
currency | query | string | Optional | Currency  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | [UnifiedLeverageSetting]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | [Leverage multiplier for borrowing currency]  
» _None_ | UnifiedLeverageSetting | Leverage multiplier for borrowing currency  
»» currency | string | Currency name  
»» leverage | string | Multiplier  
  
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
    
    url = '/unified/leverage/user_currency_setting'
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
    url="/unified/leverage/user_currency_setting"
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
        "leverage": "3"
      }
    ]
    

##  Set loan currency leverage🔒 Authenticated

POST`/unified/leverage/user_currency_setting`

POST `/unified/leverage/user_currency_setting`

_Set loan currency leverage_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | UnifiedLeverageSetting | Required | none  
↳ currency | body | string | Required | Currency name  
↳ leverage | body | string | Required | Multiplier  
  
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
    
    url = '/unified/leverage/user_currency_setting'
    query_param = ''
    body='{"currency":"BTC","leverage":"3"}'
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
    url="/unified/leverage/user_currency_setting"
    query_param=""
    body_param='{"currency":"BTC","leverage":"3"}'
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
      "leverage": "3"
    }
    

##  List of loan currencies supported by unified account

GET`/unified/currencies`

GET `/unified/currencies`

_List of loan currencies supported by unified account_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
currency | query | string | Optional | Currency  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)List retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [UnifiedCurrency]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | none  
» name | string | Currency name  
» prec | string | Currency precision  
» min_borrow_amount | string | Minimum borrowable limit, in currency units  
» user_max_borrow_amount | string | User's maximum borrowable limit, in USDT  
» total_max_borrow_amount | string | Platform's maximum borrowable limit, in USDT  
» loan_status | string | Lending status  
\- `disable` : Lending prohibited  
\- `enable` : Lending supported  
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/unified/currencies'
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/unified/currencies \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    [
      {
        "name": "BTC",
        "prec": "0.000001",
        "min_borrow_amount": "0.01",
        "user_max_borrow_amount": "1000000",
        "total_max_borrow_amount": "1000000",
        "loan_status": "enable"
      }
    ]
    

##  Get historical lending rates

GET`/unified/history_loan_rate`

GET `/unified/history_loan_rate`

Get `historical lending rates`

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
tier | query | string | Optional | VIP level for the floating rate to be queried  
currency | query | string | Required | Currency  
page | query | integer(int32) | Optional | Page number  
limit | query | integer(int32) | Optional | Maximum number of items returned. Default: 100, minimum: 1, maximum: 100  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | UnifiedHistoryLoanRate  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» currency | string | Currency name  
» tier | string | VIP level for the floating rate to be retrieved  
» tier_up_rate | string | Floating rate corresponding to VIP level  
» rates | array | Historical interest rate information, one data point per hour, array size determined by page and limit parameters from the API request, sorted by time from recent to distant  
»» time | integer(int64) | Hourly timestamp corresponding to this interest rate, in milliseconds  
»» rate | string | Historical interest rate for this hour  
  
This operation does not require authentication 

Code samples
    
    
    # coding: utf-8
    import requests
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/unified/history_loan_rate'
    query_param = 'currency=USDT'
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    curl -X GET https://api.gateio.ws/api/v4/unified/history_loan_rate?currency=USDT \
      -H 'Accept: application/json'
    
    

> Example responses

> 200 Response
    
    
    {
      "currency": "USDT",
      "tier": "1",
      "tier_up_rate": "1.18",
      "rates": [
        {
          "time": 1729047616000,
          "rate": "0.00010287"
        }
      ]
    }
    

##  Set collateral currency🔒 Authenticated

POST`/unified/collateral_currencies`

POST `/unified/collateral_currencies`

_Set collateral currency_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | UnifiedCollateralReq | Required | none  
↳ collateral_type | body | integer | Optional | User-set collateral mode: 0(all)-All currencies as collateral, 1(custom)-Custom currencies as collateral. When collateral_type is 0(all), enable_list and disable_list parameters are invalid  
↳ enable_list | body | array | Optional | Currency list, where collateral_type=1(custom) indicates the addition logic  
↳ disable_list | body | array | Optional | Disable list, indicating the disable logic  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
» collateral_type | 0  
» collateral_type | 1  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Updated successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Updated successfully | UnifiedCollateralRes  
  
### Response Schema

Status Code **200**

_Unified account collateral mode settings response_

Name | Type | Description  
---|---|---  
» is_success | boolean | Whether the setting was successful  
  
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
    
    url = '/unified/collateral_currencies'
    query_param = ''
    body='{"collateral_type":1,"enable_list":["BTC","ETH"],"disable_list":["SOL","GT"]}'
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
    url="/unified/collateral_currencies"
    query_param=""
    body_param='{"collateral_type":1,"enable_list":["BTC","ETH"],"disable_list":["SOL","GT"]}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "collateral_type": 1,
      "enable_list": [
        "BTC",
        "ETH"
      ],
      "disable_list": [
        "SOL",
        "GT"
      ]
    }
    

> Example responses

> 200 Response
    
    
    {
      "is_success": true
    }
    

##  Estimated quick repayment details🔒 Authenticated

GET`/unified/estimated_quick_repayment`

GET `/unified/estimated_quick_repayment`

_Estimated quick repayment details_

Available for unified account cross-currency margin mode and portfolio margin mode

### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful
  * 400[Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1)Invalid request parameters
  * 401[Unauthorized ](https://tools.ietf.org/html/rfc7235#section-3.1)Authentication failed
  * 403[Forbidden ](https://tools.ietf.org/html/rfc7231#section-6.5.3)Access denied (e.g. account mode does not support quick repayment)

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | QuickEstimatedRepayment  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Invalid request parameters | GateErrorResponse  
401 | [Unauthorized ](https://tools.ietf.org/html/rfc7235#section-3.1) | Authentication failed | GateErrorResponse  
403 | [Forbidden ](https://tools.ietf.org/html/rfc7231#section-6.5.3) | Access denied (e.g. account mode does not support quick repayment) | GateErrorResponse  
  
### Response Schema

Status Code **200**

_QuickEstimatedRepayment_

Name | Type | Description  
---|---|---  
» debt_currencies | array | Liability currencies  
»» UnifiedDebtCurrencies | object | none  
»»» currency | string | Currency name  
»»» debt_amount | string | Debt Quantity  
»»» estimated_usd | string | Estimated USD value  
»»» borrowed | string | Borrowed amount  
»»» neg_balance | string | Negative balance  
»» available_currencies | array | Currencies available for repayment  
»»» UnifiedAvailableCurrencies | object | none  
»»»» currency | string | Currency name  
»»»» available | string | Available Balance  
»»»» estimated_usd | string | Estimated USD value  
  
Status Code **400**

_error response body format when status code is non-2xx_

Name | Type | Description  
---|---|---  
» label | string | Error label  
» message | string | Detailed error message  
  
Status Code **401**

_error response body format when status code is non-2xx_

Name | Type | Description  
---|---|---  
» label | string | Error label  
» message | string | Detailed error message  
  
Status Code **403**

_error response body format when status code is non-2xx_

Name | Type | Description  
---|---|---  
» label | string | Error label  
» message | string | Detailed error message  
  
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
    
    url = '/unified/estimated_quick_repayment'
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
    url="/unified/estimated_quick_repayment"
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
      "debt_currencies": [
        {
          "currency": "ETH",
          "debt_amount": "1.5",
          "estimated_usd": "4500",
          "borrowed": "1.5",
          "neg_balance": "0"
        }
      ],
      "available_currencies": [
        {
          "currency": "USDT",
          "available": "5000",
          "estimated_usd": "5000"
        }
      ]
    }
    

> 400 Response
    
    
    {
      "label": "INVALID_PARAM",
      "message": "invalid request"
    }
    

> 401 Response
    
    
    {
      "label": "INVALID_KEY",
      "message": "Invalid API key"
    }
    

> 403 Response
    
    
    {
      "label": "FORBIDDEN",
      "message": "quick repayment is only available in cross-currency margin or portfolio margin mode"
    }
    

##  Quick repayment🔒 Authenticated

POST`/unified/quick_repayment`

POST `/unified/quick_repayment`

_Quick repayment_

Available for unified account cross-currency margin mode and portfolio margin mode. Use `GET /unified/estimated_quick_repayment` to query liabilities and pending repayment information.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | QuickRepaymentRequest | Required | none  
↳ debt_currencies | body | array | Required | Liability currencies  
↳ available_currencies | body | array | Required | Currencies to repay with  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Repayment successful
  * 400[Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1)Invalid request parameters
  * 401[Unauthorized ](https://tools.ietf.org/html/rfc7235#section-3.1)Authentication failed
  * 403[Forbidden ](https://tools.ietf.org/html/rfc7231#section-6.5.3)Access denied (e.g. account mode does not support quick repayment)

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Repayment successful | QuickRepaymentResponse  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Invalid request parameters | GateErrorResponse  
401 | [Unauthorized ](https://tools.ietf.org/html/rfc7235#section-3.1) | Authentication failed | GateErrorResponse  
403 | [Forbidden ](https://tools.ietf.org/html/rfc7231#section-6.5.3) | Access denied (e.g. account mode does not support quick repayment) | GateErrorResponse  
  
### Response Schema

Status Code **200**

_QuickRepaymentResp_

Name | Type | Description  
---|---|---  
» order_id | string | Order ID  
» repaid_infos | array | Repaid currency details  
»» RepaidInfo | object | Repayment details  
»»» currency | string | Currency name  
»»» repaid | string | Repaid amount  
»»» left | string | Remaining liability amount  
»» used_infos | array | Currencies used for repayment  
»»» UsedInfo | object | Repayment details  
»»»» currency | string | Currency name  
»»»» used | string | Amount converted  
  
Status Code **400**

_error response body format when status code is non-2xx_

Name | Type | Description  
---|---|---  
» label | string | Error label  
» message | string | Detailed error message  
  
Status Code **401**

_error response body format when status code is non-2xx_

Name | Type | Description  
---|---|---  
» label | string | Error label  
» message | string | Detailed error message  
  
Status Code **403**

_error response body format when status code is non-2xx_

Name | Type | Description  
---|---|---  
» label | string | Error label  
» message | string | Detailed error message  
  
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
    
    url = '/unified/quick_repayment'
    query_param = ''
    body='{"debt_currencies":["ETH"],"available_currencies":["USDT","BTC"]}'
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
    url="/unified/quick_repayment"
    query_param=""
    body_param='{"debt_currencies":["ETH"],"available_currencies":["USDT","BTC"]}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "debt_currencies": [
        "ETH"
      ],
      "available_currencies": [
        "USDT",
        "BTC"
      ]
    }
    

> Example responses

> 200 Response
    
    
    {
      "order_id": "qr_123456",
      "repaid_infos": [
        {
          "currency": "ETH",
          "repaid": "0.5",
          "left": "1.0"
        }
      ],
      "used_infos": [
        {
          "currency": "USDT",
          "used": "1500"
        }
      ]
    }
    

> 400 Response
    
    
    {
      "label": "INVALID_PARAM",
      "message": "invalid request body"
    }
    

> 401 Response
    
    
    {
      "label": "INVALID_KEY",
      "message": "Invalid API key"
    }
    

> 403 Response
    
    
    {
      "label": "FORBIDDEN",
      "message": "quick repayment is only available in cross-currency margin or portfolio margin mode"
    }
    

#  Schemas

##  UnifiedLeverageConfig

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
current_leverage | string | Optional | none | Current leverage ratio  
min_leverage | string | Optional | none | Minimum adjustable leverage ratio  
max_leverage | string | Optional | none | Maximum adjustable leverage ratio  
debit | string | Optional | none | Current liabilities  
available_margin | string | Optional | none | Available Margin  
borrowable | string | Optional | none | Maximum borrowable amount at current leverage  
except_leverage_borrowable | string | Optional | none | Maximum borrowable from margin and maximum borrowable from Earn, whichever is smaller  
      
    
    {
      "current_leverage": "string",
      "min_leverage": "string",
      "max_leverage": "string",
      "debit": "string",
      "available_margin": "string",
      "borrowable": "string",
      "except_leverage_borrowable": "string"
    }
    
    

##  UnifiedCurrency

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
name | string | Optional | none | Currency name  
prec | string | Optional | none | Currency precision  
min_borrow_amount | string | Optional | none | Minimum borrowable limit, in currency units  
user_max_borrow_amount | string | Optional | none | User's maximum borrowable limit, in USDT  
total_max_borrow_amount | string | Optional | none | Platform's maximum borrowable limit, in USDT  
loan_status | string | Optional | none | Lending status  
\- `disable` : Lending prohibited  
\- `enable` : Lending supported  
      
    
    {
      "name": "string",
      "prec": "string",
      "min_borrow_amount": "string",
      "user_max_borrow_amount": "string",
      "total_max_borrow_amount": "string",
      "loan_status": "string"
    }
    
    

##  UnifiedTransferable

_UnifiedTransferable_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
currency | string | Optional | none | Currency detail  
amount | string | Optional | none | Maximum transferable amount  
      
    
    {
      "currency": "string",
      "amount": "string"
    }
    
    

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
    
    

##  QuickEstimatedRepayment

_QuickEstimatedRepayment_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
debt_currencies | array | Optional | none | Liability currencies  
↳ UnifiedDebtCurrencies | object | Optional | none | none  
↳ currency | string | Optional | none | Currency name  
↳ debt_amount | string | Optional | none | Debt Quantity  
↳ estimated_usd | string | Optional | none | Estimated USD value  
↳ borrowed | string | Optional | none | Borrowed amount  
↳ neg_balance | string | Optional | none | Negative balance  
↳ available_currencies | array | Optional | none | Currencies available for repayment  
↳ UnifiedAvailableCurrencies | object | Optional | none | none  
↳ currency | string | Optional | none | Currency name  
↳ available | string | Optional | none | Available Balance  
↳ estimated_usd | string | Optional | none | Estimated USD value  
      
    
    {
      "debt_currencies": [
        {
          "currency": "string",
          "debt_amount": "string",
          "estimated_usd": "string",
          "borrowed": "string",
          "neg_balance": "string"
        }
      ],
      "available_currencies": [
        {
          "currency": "string",
          "available": "string",
          "estimated_usd": "string"
        }
      ]
    }
    
    

##  UnifiedLoan

_Borrow or repay_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
currency | string | Required | none | Currency  
type | string | Required | none | Type: `borrow` \- borrow, `repay` \- repay  
amount | string | Required | none | Borrow or repayment amount  
repaid_all | boolean | Optional | none | Full repayment, only used for repayment operations. When set to `true`, overrides `amount` and directly repays the full amount  
text | string | Optional | none | User defined custom ID  
  
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
      "text": "string"
    }
    
    

##  UnifiedLeverageSetting

_Leverage multiplier for borrowing currency_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
currency | string | Required | none | Currency name  
leverage | string | Required | none | Multiplier  
      
    
    {
      "currency": "string",
      "leverage": "string"
    }
    
    

##  UnifiedCollateralReq

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
collateral_type | integer | Optional | none | User-set collateral mode: 0(all)-All currencies as collateral, 1(custom)-Custom currencies as collateral. When collateral_type is 0(all), enable_list and disable_list parameters are invalid  
enable_list | array | Optional | none | Currency list, where collateral_type=1(custom) indicates the addition logic  
disable_list | array | Optional | none | Disable list, indicating the disable logic  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
collateral_type | 0  
collateral_type | 1  
      
    
    {
      "collateral_type": 0,
      "enable_list": [
        "string"
      ],
      "disable_list": [
        "string"
      ]
    }
    
    

##  UnifiedBorrowable

_UnifiedBorrowable_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
currency | string | Optional | none | Currency detail  
amount | string | Optional | none | Max borrowable amount  
      
    
    {
      "currency": "string",
      "amount": "string"
    }
    
    

##  UnifiedCollateralRes

_Unified account collateral mode settings response_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
is_success | boolean | Optional | none | Whether the setting was successful  
      
    
    {
      "is_success": true
    }
    
    

##  UnifiedModeSet

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
mode | string | Required | none | Unified account mode:   
\- `classic`: Classic account mode  
\- `multi_currency`: Cross-currency margin mode  
\- `portfolio`: Portfolio margin mode  
\- `single_currency`: Single-currency margin mode  
settings | object | Optional | none | none  
↳ usdt_futures | boolean | Optional | none | USDT futures switch. In cross-currency margin mode, can only be enabled and cannot be disabled  
↳ spot_hedge | boolean | Optional | none | Spot hedging switch  
↳ use_funding | boolean | Optional | none | Earn switch, when mode is cross-currency margin mode, whether to use Earn funds as margin  
↳ options | boolean | Optional | none | Options switch. In cross-currency margin mode, can only be enabled and cannot be disabled  
      
    
    {
      "mode": "string",
      "settings": {
        "usdt_futures": true,
        "spot_hedge": true,
        "use_funding": true,
        "options": true
      }
    }
    
    

##  UnifiedAccount

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
mode | string | Optional | none | Unified account mode:  
\- classic: Classic account mode  
\- multi_currency: Multi-currency margin mode  
\- portfolio: Portfolio margin mode  
\- single_currency: Single-currency margin mode  
user_id | integer(int64) | Optional | none | User ID  
refresh_time | integer(int64) | Optional | none | Last refresh time  
locked | boolean | Optional | none | Whether the account is locked, valid in cross-currency margin/combined margin mode, false in other modes such as single-currency margin mode  
balances | object | Optional | none | none  
↳ UnifiedBalance | object | Optional | none | none  
↳ available | string | Optional | none | Cross available balance, deducted futures isolated margin occupation and frozen amount (futures isolated occupation, i.e. futures isolated balance), effective in single-currency/multi-currency/portfolio margin mode.  
↳ freeze | string | Optional | none | Frozen amount, effective in single-currency/multi-currency/portfolio margin mode  
↳ borrowed | string | Optional | none | Borrowed amount, valid in cross-currency margin/combined margin mode, 0 in other modes such as single-currency margin mode  
↳ negative_liab | string | Optional | none | Negative balance borrowing, valid in cross-currency margin/combined margin mode, 0 in other modes such as single-currency margin mode  
↳ futures_pos_liab | string | Optional | none | Contract opening position borrowing currency (abandoned, to be offline field)  
↳ equity | string | Optional | none | Currency equity amount (cross), effective in single-currency/multi-currency/portfolio margin mode  
↳ total_freeze | string | Optional | none | Total frozen (deprecated, to be removed)  
↳ total_liab | string | Optional | none | Total borrowed amount, valid in cross-currency margin/combined margin mode, 0 in other modes such as single-currency margin mode  
↳ spot_in_use | string | Optional | none | The amount of spot hedging is valid in the combined margin mode, and is 0 in other margin modes such as single currency and cross-currency margin modes  
↳ funding | string | Optional | none | Uniloan financial management amount, effective when turned on as a unified account margin switch  
↳ funding_version | string | Optional | none | Funding version  
↳ cross_balance | string | Optional | none | Full margin balance is valid in single currency margin mode, and is 0 in other modes such as cross currency margin/combined margin mode  
↳ iso_balance | string | Optional | none | Futures isolated balance, effective in single-currency and multi-currency margin mode, 0 in portfolio margin mode  
↳ im | string | Optional | none | Cross initial margin, only effective for USDT in single-currency margin mode, 0 in multi-currency/portfolio margin mode  
↳ mm | string | Optional | none | Cross maintenance margin, only effective for USDT in single-currency margin mode, 0 in multi-currency/portfolio margin mode  
↳ imr | string | Optional | none | Cross initial margin rate, only effective for USDT in single-currency margin mode, 0 in multi-currency/portfolio margin mode  
↳ mmr | string | Optional | none | Cross maintenance margin rate, only effective for USDT in single-currency margin mode, 0 in multi-currency/portfolio margin mode  
↳ margin_balance | string | Optional | none | Cross margin balance, only effective for USDT in single-currency margin mode, 0 in multi-currency/portfolio margin mode  
↳ available_margin | string | Optional | none | Cross available margin, only effective for USDT in single-currency margin mode, 0 in multi-currency/portfolio margin mode  
↳ enabled_collateral | boolean | Optional | none | Currency enabled as margin: true - Enabled, false - Disabled  
↳ balance_version | number(int64) | Optional | none | Balance version number  
↳ total | string | Optional | none | Total account assets converted to USD, i.e. the sum of `(available + freeze) * price` in all currencies (deprecated, to be removed, replaced by unified_account_total)  
↳ borrowed | string | Optional | none | Total borrowed amount converted to USD, i.e. the sum of `borrowed * price` of all currencies (excluding point cards), valid in cross-currency margin/combined margin mode, 0 in other modes such as single-currency margin mode  
↳ total_initial_margin | string | Optional | none | Total initial margin (cross), effective in multi-currency margin/portfolio margin mode, 0 in single-currency margin mode  
↳ total_margin_balance | string | Optional | none | Total margin balance (cross), effective in multi-currency margin/portfolio margin mode, 0 in single-currency margin mode  
↳ total_maintenance_margin | string | Optional | none | Total maintenance margin (cross), effective in multi-currency margin/portfolio margin mode, 0 in single-currency margin mode  
↳ total_initial_margin_rate | string | Optional | none | Total initial margin rate (cross), effective in multi-currency margin/portfolio margin mode, 0 in single-currency margin mode  
↳ total_maintenance_margin_rate | string | Optional | none | Total maintenance margin rate (cross), effective in multi-currency margin/portfolio margin mode, 0 in single-currency margin mode  
↳ total_available_margin | string | Optional | none | Available margin amount, valid in cross-currency margin/combined margin mode, 0 in other modes such as single-currency margin mode  
↳ unified_account_total | string | Optional | none | Total unified account assets, includes both cross and isolated total assets in single-currency/multi-currency mode, only cross total assets in portfolio margin mode  
↳ unified_account_total_liab | string | Optional | none | Total unified account borrowed, i.e. total cross borrowed, effective in multi-currency margin/portfolio margin mode, 0 in single-currency margin mode  
↳ unified_account_total_equity | string | Optional | none | Total unified account equity, includes both cross and isolated total equity in single-currency/multi-currency mode, only cross total equity in portfolio margin mode  
↳ leverage | string | Optional | read-only | Account leverage multiplier, effective in multi-currency/portfolio margin mode (deprecated). Currency leverage query API: GET /unified/leverage/user_currency_setting  
↳ spot_order_loss | string | Optional | none | Spot Pending Order Loss, in USDT, effective only in Cross-Currency Margin Mode and Portfolio Margin Mode.  
↳ options_order_loss | string | Optional | none | Option Pending Order Loss, in USDT, effective only in Portfolio Margin Mode.  
↳ spot_hedge | boolean | Optional | none | Spot hedging status: true - enabled, false - disabled  
↳ use_funding | boolean | Optional | none | Whether to use Earn funds as margin  
↳ is_all_collateral | boolean | Optional | none | Whether all currencies are used as margin: true - all currencies as margin, false - no  
      
    
    {
      "mode": "string",
      "user_id": 0,
      "refresh_time": 0,
      "locked": true,
      "balances": {
        "property1": {
          "available": "string",
          "freeze": "string",
          "borrowed": "string",
          "negative_liab": "string",
          "futures_pos_liab": "string",
          "equity": "string",
          "total_freeze": "string",
          "total_liab": "string",
          "spot_in_use": "string",
          "funding": "string",
          "funding_version": "string",
          "cross_balance": "string",
          "iso_balance": "string",
          "im": "string",
          "mm": "string",
          "imr": "string",
          "mmr": "string",
          "margin_balance": "string",
          "available_margin": "string",
          "enabled_collateral": true,
          "balance_version": 0
        },
        "property2": {
          "available": "string",
          "freeze": "string",
          "borrowed": "string",
          "negative_liab": "string",
          "futures_pos_liab": "string",
          "equity": "string",
          "total_freeze": "string",
          "total_liab": "string",
          "spot_in_use": "string",
          "funding": "string",
          "funding_version": "string",
          "cross_balance": "string",
          "iso_balance": "string",
          "im": "string",
          "mm": "string",
          "imr": "string",
          "mmr": "string",
          "margin_balance": "string",
          "available_margin": "string",
          "enabled_collateral": true,
          "balance_version": 0
        }
      },
      "total": "string",
      "borrowed": "string",
      "total_initial_margin": "string",
      "total_margin_balance": "string",
      "total_maintenance_margin": "string",
      "total_initial_margin_rate": "string",
      "total_maintenance_margin_rate": "string",
      "total_available_margin": "string",
      "unified_account_total": "string",
      "unified_account_total_liab": "string",
      "unified_account_total_equity": "string",
      "leverage": "string",
      "spot_order_loss": "string",
      "options_order_loss": "string",
      "spot_hedge": true,
      "use_funding": true,
      "is_all_collateral": true
    }
    
    

##  GateErrorResponse

_error response body format when status code is non-2xx_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
label | string | Optional | none | Error label  
message | string | Optional | none | Detailed error message  
      
    
    {
      "label": "string",
      "message": "string"
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
    
    

##  UnifiedPortfolioOutput

_Portfolio margin calculator output_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
maintain_margin_total | string | Optional | none | Total maintenance margin, including only portfolio margin calculation results for positions in risk units, excluding borrowing margin. If borrowing exists, conventional borrowing margin requirements will still apply  
initial_margin_total | string | Optional | none | Total initial margin, calculated as the maximum of the following three combinations: position, position + positive delta orders, position + negative delta orders  
calculate_time | integer(int64) | Optional | none | Calculation time  
risk_unit | array | Optional | none | Risk unit  
↳ None | object | Optional | none | Risk unit  
↳ symbol | string | Optional | none | Risk unit name  
↳ spot_in_use | string | Optional | none | Spot hedge usage  
↳ maintain_margin | string | Optional | none | Maintenance margin  
↳ initial_margin | string | Optional | none | Initial margin  
↳ margin_result | array | Optional | none | Margin result  
↳ None | object | Optional | none | Margin result  
↳ type | string | Optional | none | Position combination type  
`original_position` \- Original position  
`long_delta_original_position` \- Positive delta + Original position  
`short_delta_original_position` \- Negative delta + Original position  
↳ profit_loss_ranges | array | Optional | none | Results of 33 stress scenarios for MR1  
↳ None | object | Optional | none | Profit and loss range  
↳ price_percentage | string | Optional | none | Percentage change in price  
↳ implied_volatility_percentage | string | Optional | none | Percentage change in implied volatility  
↳ profit_loss | string | Optional | none | PnL  
↳ max_loss | UnifiedPortfolioOutput/properties/risk_unit/items/properties/margin_result/items/properties/profit_loss_ranges/items | Optional | none | Profit and loss range  
↳ mr1 | string | Optional | none | Stress testing  
↳ mr2 | string | Optional | none | Basis spread risk  
↳ mr3 | string | Optional | none | Volatility spread risk  
↳ mr4 | string | Optional | none | Option short risk  
↳ delta | string | Optional | none | Total Delta of risk unit  
↳ gamma | string | Optional | none | Total Gamma of risk unit  
↳ theta | string | Optional | none | Total Theta of risk unit  
↳ vega | string | Optional | none | Total Vega of risk unit  
      
    
    {
      "maintain_margin_total": "string",
      "initial_margin_total": "string",
      "calculate_time": 0,
      "risk_unit": [
        {
          "symbol": "string",
          "spot_in_use": "string",
          "maintain_margin": "string",
          "initial_margin": "string",
          "margin_result": [],
          "delta": "string",
          "gamma": "string",
          "theta": "string",
          "vega": "string"
        }
      ]
    }
    
    

##  UnifiedDiscount

_Unified account tiered discount_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
currency | string | Optional | none | Currency name  
discount_tiers | array | Optional | none | Tiered discount  
↳ tier | string | Optional | none | Tier  
↳ discount | string | Optional | none | Discount  
↳ lower_limit | string | Optional | none | Lower limit  
↳ upper_limit | string | Optional | none | Upper limit, + indicates positive infinity  
↳ leverage | string | Optional | none | Position leverage  
      
    
    {
      "currency": "string",
      "discount_tiers": [
        {
          "tier": "string",
          "discount": "string",
          "lower_limit": "string",
          "upper_limit": "string",
          "leverage": "string"
        }
      ]
    }
    
    

##  QuickRepaymentResponse

_QuickRepaymentResp_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
order_id | string | Required | none | Order ID  
repaid_infos | array | Required | none | Repaid currency details  
↳ RepaidInfo | object | Optional | none | Repayment details  
↳ currency | string | Required | none | Currency name  
↳ repaid | string | Required | none | Repaid amount  
↳ left | string | Required | none | Remaining liability amount  
↳ used_infos | array | Required | none | Currencies used for repayment  
↳ UsedInfo | object | Optional | none | Repayment details  
↳ currency | string | Required | none | Currency name  
↳ used | string | Required | none | Amount converted  
      
    
    {
      "order_id": "string",
      "repaid_infos": [
        {
          "currency": "string",
          "repaid": "string",
          "left": "string"
        }
      ],
      "used_infos": [
        {
          "currency": "string",
          "used": "string"
        }
      ]
    }
    
    

##  UnifiedMarginTiers

_Unified account borrowing margin tiers_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
currency | string | Optional | none | Currency name  
margin_tiers | array | Optional | none | Tiered margin  
↳ MarginTiers | object | Optional | none | none  
↳ tier | string | Optional | none | Tier  
↳ margin_rate | string | Optional | none | Discount  
↳ lower_limit | string | Optional | none | Lower limit  
↳ upper_limit | string | Optional | none | Upper limit, `` indicates greater than (the last tier)  
↳ leverage | string | Optional | none | Position leverage  
      
    
    {
      "currency": "string",
      "margin_tiers": [
        {
          "tier": "string",
          "margin_rate": "string",
          "lower_limit": "string",
          "upper_limit": "string",
          "leverage": "string"
        }
      ]
    }
    
    

##  UnifiedLoanResult

_Unified account borrowing and repayment response result_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
tran_id | integer(int64) | Optional | none | Transaction ID  
      
    
    {
      "tran_id": 0
    }
    
    

##  UnifiedRiskUnits

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
user_id | integer(int64) | Optional | none | User ID  
spot_hedge | boolean | Optional | none | Spot hedging status: true - enabled, false - disabled  
risk_units | array | Optional | none | Risk unit  
↳ RiskUnits | object | Optional | none | none  
↳ symbol | string | Optional | none | Risk unit flag  
↳ spot_in_use | string | Optional | none | Spot hedging occupied amount  
↳ maintain_margin | string | Optional | none | Maintenance margin for risk unit  
↳ initial_margin | string | Optional | none | Initial margin for risk unit  
↳ delta | string | Optional | none | Total Delta of risk unit  
↳ gamma | string | Optional | none | Total Gamma of risk unit  
↳ theta | string | Optional | none | Total Theta of risk unit  
↳ vega | string | Optional | none | Total Vega of risk unit  
      
    
    {
      "user_id": 0,
      "spot_hedge": true,
      "risk_units": [
        {
          "symbol": "BTC_USDT",
          "spot_in_use": "string",
          "maintain_margin": "string",
          "initial_margin": "string",
          "delta": "string",
          "gamma": "string",
          "theta": "string",
          "vega": "string"
        }
      ]
    }
    
    

##  QuickRepaymentRequest

_QuickRepaymentInfo_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
debt_currencies | array | Required | none | Liability currencies  
available_currencies | array | Required | none | Currencies to repay with  
      
    
    {
      "debt_currencies": [
        "string"
      ],
      "available_currencies": [
        "string"
      ]
    }
    
    

##  UnifiedHistoryLoanRate

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
currency | string | Optional | none | Currency name  
tier | string | Optional | none | VIP level for the floating rate to be retrieved  
tier_up_rate | string | Optional | none | Floating rate corresponding to VIP level  
rates | array | Optional | none | Historical interest rate information, one data point per hour, array size determined by page and limit parameters from the API request, sorted by time from recent to distant  
↳ time | integer(int64) | Optional | none | Hourly timestamp corresponding to this interest rate, in milliseconds  
↳ rate | string | Optional | none | Historical interest rate for this hour  
      
    
    {
      "currency": "string",
      "tier": "string",
      "tier_up_rate": "string",
      "rates": [
        {
          "time": 0,
          "rate": "string"
        }
      ]
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
    
    

##  UnifiedLoanRecord

_Borrowing Records_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
id | integer(int64) | Optional | read-only | id  
type | string | Optional | read-only | Type: `borrow` \- borrow, `repay` \- repay  
repayment_type | string | Optional | read-only | Repayment type: none - No repayment type, manual_repay - Manual repayment, auto_repay - Automatic repayment, cancel_auto_repay - Automatic repayment after order cancellation, different_currencies_repayment - Cross-currency repayment  
borrow_type | string | Optional | none | Borrowing type, returned when querying loan records: manual_borrow - Manual borrowing, auto_borrow - Automatic borrowing  
currency_pair | string | Optional | read-only | Currency pair  
currency | string | Optional | read-only | Currency  
amount | string | Optional | read-only | Borrow or repayment amount  
create_time | integer(int64) | Optional | read-only | Created time  
      
    
    {
      "id": 0,
      "type": "string",
      "repayment_type": "string",
      "borrow_type": "string",
      "currency_pair": "string",
      "currency": "string",
      "amount": "string",
      "create_time": 0
    }
    
    

##  UnifiedPortfolioInput

_Portfolio margin calculator input_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
spot_balances | array | Optional | none | Spot  
↳ None | object | Optional | none | Spot  
↳ currency | string | Required | none | Currency name  
↳ equity | string | Required | none | Currency equity, where equity = balance - borrowed, represents the net delta exposure of your spot positions  
↳ spot_orders | array | Optional | none | Spot orders  
↳ None | object | Optional | none | Spot orders  
↳ currency_pairs | string | Required | none | Market  
↳ order_price | string | Required | none | Price  
↳ count | string | Optional | none | Initial order quantity for spot trading pairs, not involved in actual calculation.  
↳ left | string | Required | none | Unfilled quantity, involved in actual calculation  
↳ type | string | Required | none | Order type, sell - sell order, buy - buy order  
↳ futures_positions | array | Optional | none | Futures positions  
↳ None | object | Optional | none | Futures positions  
↳ contract | string | Required | none | Perpetual contract name. Only USDT perpetual contracts for underlying currencies with active options trading are supported.  
↳ size | string | Required | none | Position size, measured in contract quantity  
↳ futures_orders | array | Optional | none | Futures order  
↳ None | object | Optional | none | Futures order  
↳ contract | string | Required | none | Perpetual contract name. Only USDT perpetual contracts for underlying currencies with active options trading are supported.  
↳ size | string | Required | none | Contract quantity, representing the initial order quantity, not involved in actual settlement  
↳ left | string | Required | none | Unfilled contract quantity, involved in actual calculation  
↳ options_positions | array | Optional | none | Options positions  
↳ None | object | Optional | none | Options positions  
↳ options_name | string | Required | none | Options contract name. Currently supports all options contract markets.  
↳ size | string | Required | none | Position size, measured in contract quantity  
↳ options_orders | array | Optional | none | Option orders  
↳ None | object | Optional | none | Option orders  
↳ options_name | string | Required | none | Options contract name. Currently supports all options contract markets.  
↳ size | string | Required | none | Initial order quantity, not involved in actual calculation  
↳ left | string | Required | none | Unfilled contract quantity, involved in actual calculation  
↳ spot_hedge | boolean | Optional | none | Whether to enable spot hedging  
      
    
    {
      "spot_balances": [
        {
          "currency": "string",
          "equity": "string"
        }
      ],
      "spot_orders": [
        {
          "currency_pairs": "string",
          "order_price": "string",
          "count": "string",
          "left": "string",
          "type": "string"
        }
      ],
      "futures_positions": [
        {
          "contract": "string",
          "size": "string"
        }
      ],
      "futures_orders": [
        {
          "contract": "string",
          "size": "string",
          "left": "string"
        }
      ],
      "options_positions": [
        {
          "options_name": "string",
          "size": "string"
        }
      ],
      "options_orders": [
        {
          "options_name": "string",
          "size": "string",
          "left": "string"
        }
      ],
      "spot_hedge": true
    }