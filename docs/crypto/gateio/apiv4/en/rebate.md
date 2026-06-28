---
exchange: gateio
source_url: https://www.gate.com/docs/developers/apiv4/en/rebate
api_type: Earn
updated_at: 2026-05-27 20:15:47.788350
---

# Rebate

Commission rebate related APIs, including trading record queries and rebate record queries for agents, partners, and brokers

##  Broker obtains transaction history of recommended users🔒 Authenticated

GET`/rebate/agency/transaction_history`

GET `/rebate/agency/transaction_history`

_Broker obtains transaction history of recommended users_

Record query time range cannot exceed 30 days

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
currency_pair | query | string | Optional | Specify the trading pair. If not specified, returns all trading pairs  
user_id | query | integer(int64) | Optional | User ID. If not specified, all user records will be returned  
from | query | integer(int64) | Optional | Start time for querying records. If not specified, defaults to 7 days before current time  
to | query | integer(int64) | Optional | End timestamp for the query, defaults to current time if not specified  
limit | query | integer | Optional | Maximum number of records returned in a single list  
offset | query | integer | Optional | List offset, starting from 0  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)List retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | Inline  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» currency_pair | string | Currency pair  
» total | integer(int64) | Total  
» list | array | List of transaction history  
»» AgencyTransaction | object | none  
»»» transaction_time | integer(int64) | Transaction Time. (unix timestamp)  
»»» user_id | integer(int64) | User ID  
»»» group_name | string | Group name  
»»» fee | string | Fee  
»»» fee_asset | string | Fee currency  
»»» currency_pair | string | Currency pair  
»»» amount | string | Transaction amount  
»»» amount_asset | string | Transaction amount currency  
»»» source | string | Commission source: SPOT - Spot commission, FUTURES - Futures commission  
  
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
    
    url = '/rebate/agency/transaction_history'
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
    url="/rebate/agency/transaction_history"
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
      "total": 100,
      "list": [
        {
          "transaction_time": 1539852480,
          "user_id": 10000,
          "group_name": "gateio",
          "fee": "1",
          "fee_asset": "GT",
          "currency_pair": "GT_USDT",
          "amount": "1000",
          "source": "SPOT",
          "amount_asset": "GT"
        }
      ]
    }
    

##  Broker obtains rebate history of recommended users🔒 Authenticated

GET`/rebate/agency/commission_history`

GET `/rebate/agency/commission_history`

_Broker obtains rebate history of recommended users_

Record query time range cannot exceed 30 days

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
currency | query | string | Optional | Specify the currency. If not specified, returns all currencies  
commission_type | query | integer | Optional | Rebate type: 1 - Direct rebate, 2 - Indirect rebate, 3 - Self rebate  
user_id | query | integer(int64) | Optional | User ID. If not specified, all user records will be returned  
from | query | integer(int64) | Optional | Start time for querying records. If not specified, defaults to 7 days before current time  
to | query | integer(int64) | Optional | End timestamp for the query, defaults to current time if not specified  
limit | query | integer | Optional | Maximum number of records returned in a single list  
offset | query | integer | Optional | List offset, starting from 0  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)List retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | Inline  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» currency_pair | string | Currency pair  
» total | integer(int64) | Total  
» list | array | List of commission history  
»» AgencyCommission | object | none  
»»» commission_time | integer(int64) | Commission time (Unix timestamp in seconds)  
»»» user_id | integer(int64) | User ID  
»»» group_name | string | Group name  
»»» commission_amount | string | Commission amount  
»»» commission_asset | string | Commission Asset  
»»» source | string | Commission source: SPOT - Spot commission, FUTURES - Futures commission  
  
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
    
    url = '/rebate/agency/commission_history'
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
    url="/rebate/agency/commission_history"
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
      "total": 100,
      "list": [
        {
          "commission_time": 1539852480,
          "user_id": 10000,
          "group_name": "gateio",
          "commission_amount": "1000",
          "source": "SPOT",
          "commission_asset": "GT"
        }
      ]
    }
    

##  Partner obtains transaction history of recommended users🔒 Authenticated

GET`/rebate/partner/transaction_history`

GET `/rebate/partner/transaction_history`

_Partner obtains transaction history of recommended users_

Record query time range cannot exceed 30 days

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
currency_pair | query | string | Optional | Specify the trading pair. If not specified, returns all trading pairs  
user_id | query | integer(int64) | Optional | User ID. If not specified, all user records will be returned  
from | query | integer(int64) | Optional | Start time for querying records. If not specified, defaults to 7 days before current time  
to | query | integer(int64) | Optional | End timestamp for the query, defaults to current time if not specified  
limit | query | integer | Optional | Maximum number of records returned in a single list  
offset | query | integer | Optional | List offset, starting from 0  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)List retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | PartnerTransactionHistory  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» total | integer(int64) | Total  
» list | array | List of transaction history  
»» PartnerTransaction | object | none  
»»» transaction_time | integer(int64) | Transaction Time. (unix timestamp)  
»»» user_id | integer(int64) | User ID  
»»» group_name | string | Group name  
»»» fee | string | Fee  
»»» fee_asset | string | Fee currency  
»»» currency_pair | string | Currency pair  
»»» amount | string | Transaction amount  
»»» amount_asset | string | Transaction amount currency  
»»» source | string | Commission source: SPOT - Spot commission, FUTURES - Futures commission  
  
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
    
    url = '/rebate/partner/transaction_history'
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
    url="/rebate/partner/transaction_history"
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
      "total": 15,
      "list": [
        {
          "user_id": 1879032535,
          "group_name": "test",
          "fee": "0.00044800",
          "transaction_time": 1718615824,
          "amount": "29.98688000",
          "amount_asset": "USDT",
          "currency_pair": "BCH_USDT",
          "source": "SPOT",
          "fee_asset": "BCH"
        }
      ]
    }
    

##  Partner obtains rebate records of recommended users🔒 Authenticated

GET`/rebate/partner/commission_history`

GET `/rebate/partner/commission_history`

_Partner obtains rebate records of recommended users_

Record query time range cannot exceed 30 days

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
currency | query | string | Optional | Specify the currency. If not specified, returns all currencies  
user_id | query | integer(int64) | Optional | User ID. If not specified, all user records will be returned  
from | query | integer(int64) | Optional | Start time for querying records. If not specified, defaults to 7 days before current time  
to | query | integer(int64) | Optional | End timestamp for the query, defaults to current time if not specified  
limit | query | integer | Optional | Maximum number of records returned in a single list  
offset | query | integer | Optional | List offset, starting from 0  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)List retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | PartnerCommissionHistory  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» total | integer(int64) | Total  
» list | array | List of commission history  
»» PartnerCommission | object | none  
»»» commission_time | integer(int64) | Commission time (Unix timestamp in seconds)  
»»» user_id | integer(int64) | User ID  
»»» group_name | string | Group name  
»»» commission_amount | string | Commission amount  
»»» commission_asset | string | Commission Asset  
»»» source | string | Commission source: SPOT - Spot commission, FUTURES - Futures commission  
  
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
    
    url = '/rebate/partner/commission_history'
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
    url="/rebate/partner/commission_history"
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
      "total": 52,
      "list": [
        {
          "user_id": 1879043947,
          "commission_time": 1718616728,
          "commission_amount": "0.2216934846",
          "commission_asset": "USDT",
          "source": "SPOT",
          "group_name": "test"
        }
      ]
    }
    

##  Partner subordinate list🔒 Authenticated

GET`/rebate/partner/sub_list`

GET `/rebate/partner/sub_list`

_Partner subordinate list_

Including sub-agents, direct customers, and indirect customers

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
user_id | query | integer(int64) | Optional | User ID. If not specified, all user records will be returned  
limit | query | integer | Optional | Maximum number of records returned in a single list  
offset | query | integer | Optional | List offset, starting from 0  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)List retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | PartnerSubList  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» total | integer(int64) | Total  
» list | array | Subordinate list  
»» PartnerSub | object | none  
»»» user_id | integer(int64) | User ID  
»»» user_join_time | integer(int64) | Time when user joined the system, Unix timestamp in seconds  
»»» type | integer(int64) | Type (1-Sub-agent 2-Indirect direct customer 3-Direct direct customer)  
  
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
    
    url = '/rebate/partner/sub_list'
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
    url="/rebate/partner/sub_list"
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
      "total": 3,
      "list": [
        {
          "user_id": 1,
          "user_join_time": 1666255731,
          "type": 1
        },
        {
          "user_id": 2,
          "user_join_time": 1666271213,
          "type": 2
        },
        {
          "user_id": 3,
          "user_join_time": 1666422143,
          "type": 3
        }
      ]
    }
    

##  Broker obtains user's rebate records🔒 Authenticated

GET`/rebate/broker/commission_history`

GET `/rebate/broker/commission_history`

_Broker obtains user's rebate records_

Record query time range cannot exceed 30 days

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
limit | query | integer | Optional | Maximum number of records returned in a single list  
offset | query | integer | Optional | List offset, starting from 0  
user_id | query | integer(int64) | Optional | User ID. If not specified, all user records will be returned  
from | query | integer(int64) | Optional | Start time of the query record. If not specified, defaults to 30 days before the current time  
to | query | integer(int64) | Optional | End timestamp for the query, defaults to current time if not specified  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)List retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | Inline  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» total | integer(int64) | Total  
» list | array | List of commission history  
»» BrokerCommissionItem | object | none  
»»» commission_time | integer(int64) | Commission time (Unix timestamp in seconds)  
»»» user_id | integer(int64) | User ID  
»»» group_name | string | Group name  
»»» amount | string | The amount of commission rebates  
»»» fee | string | Fee  
»»» fee_asset | string | Fee currency  
»»» rebate_fee | string | The income from rebates, converted to USDT  
»»» source | string | Commission transaction type: Spot, Futures, Options, Alpha、TradFi  
»»» currency_pair | string | Currency pair  
»»» sub_broker_info | object | Sub-broker information  
»»»» user_id | integer(int64) | Sub-broker user ID  
»»»» original_commission_rate | string | Sub-broker original commission rate  
»»»» relative_commission_rate | string | Sub-broker relative commission rate  
»»»» commission_rate | string | Sub-broker actual commission rate  
»»» alpha_contract_addr | string | Alpha contract address  
  
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
    
    url = '/rebate/broker/commission_history'
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
    url="/rebate/broker/commission_history"
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
      "list": [
        {
          "user_id": 110285113,
          "group_name": "",
          "commission_time": 1702545051,
          "fee": "0.0020000000",
          "source": "SPOT",
          "amount": "0.00040000",
          "rebate_fee": "0.0004000000",
          "fee_asset": "BEAM",
          "currency_pair": "BEAM_USDT",
          "sub_broker_info": {
            "user_id": 110285114,
            "original_commission_rate": "0.2",
            "relative_commission_rate": "0.5",
            "commission_rate": "0.1"
          },
          "alpha_contract_addr": "0x9a26f5433671751c3276a065f57e5a02d2817973"
        }
      ],
      "total": 47
    }
    

##  Broker obtains user's trading history🔒 Authenticated

GET`/rebate/broker/transaction_history`

GET `/rebate/broker/transaction_history`

_Broker obtains user's trading history_

Record query time range cannot exceed 30 days

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
limit | query | integer | Optional | Maximum number of records returned in a single list  
offset | query | integer | Optional | List offset, starting from 0  
user_id | query | integer(int64) | Optional | User ID. If not specified, all user records will be returned  
from | query | integer(int64) | Optional | Start time of the query record. If not specified, defaults to 30 days before the current time  
to | query | integer(int64) | Optional | End timestamp for the query, defaults to current time if not specified  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)List retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | Inline  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» BrokerTransactionHistory | BrokerTransactionHistory | none  
»» total | integer(int64) | Total  
»» list | array | List of transaction history  
»»» BrokerTransaction | object | none  
»»»» transaction_time | integer(int64) | Transaction Time. (unix timestamp)  
»»»» user_id | integer(int64) | User ID  
»»»» group_name | string | Group name  
»»»» fee | string | Fee amount (USDT)  
»»»» currency_pair | string | Currency pair  
»»»» amount | string | Transaction amount  
»»»» fee_asset | string | Fee currency  
»»»» source | string | Commission transaction type: Spot, Futures, Options, Alpha、TradFi  
»»»» sub_broker_info | object | Sub-broker information  
»»»»» user_id | integer(int64) | Sub-broker user ID  
»»»»» original_commission_rate | string | Sub-broker original commission rate  
»»»»» relative_commission_rate | string | Sub-broker relative commission rate  
»»»»» commission_rate | string | Sub-broker actual commission rate  
»»»» alpha_contract_addr | string | Alpha contract address  
  
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
    
    url = '/rebate/broker/transaction_history'
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
    url="/rebate/broker/transaction_history"
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
      "list": [
        {
          "user_id": 110285442,
          "group_name": "",
          "fee": "0.5000045000",
          "transaction_time": 1702545051,
          "amount": "-1000.00900000",
          "currency_pair": "DOGE_USDT",
          "source": "Futures",
          "fee_asset": "USDT",
          "sub_broker_info": {
            "user_id": 110285114,
            "original_commission_rate": "0.2",
            "relative_commission_rate": "0.5",
            "commission_rate": "0.1"
          },
          "alpha_contract_addr": "0x9a26f5433671751c3276a065f57e5a02d2817973"
        }
      ],
      "total": 47
    }
    

##  User obtains rebate information🔒 Authenticated

GET`/rebate/user/info`

GET `/rebate/user/info`

_User obtains rebate information_

### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | Inline  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» _None_ | RebateUserInfo | Retrieve user rebate information  
»» invite_uid | integer(int64) | My inviter's UID  
  
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
    
    url = '/rebate/user/info'
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
    url="/rebate/user/info"
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
      "invite_uid": 987
    }
    

##  User subordinate relationship🔒 Authenticated

GET`/rebate/user/sub_relation`

GET `/rebate/user/sub_relation`

_User subordinate relationship_

Query whether the specified user is within the system

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
user_id_list | query | string | Required | Query user ID list, separated by commas. If more than 100, only 100 will be returned  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)List retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | UserSubRelation  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» list | array | Subordinate relationship list  
»» UserSub | object | none  
»»» uid | integer(int64) | User ID  
»»» belong | string | User's system affiliation (partner/referral). Empty means not belonging to any system  
»»» type | integer(int64) | Type (0-Not in system 1-Direct subordinate agent 2-Indirect subordinate agent 3-Direct direct customer 4-Indirect direct customer 5-Regular user)  
»»» ref_uid | integer(int64) | Inviter user ID  
  
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
    
    url = '/rebate/user/sub_relation'
    query_param = 'user_id_list=1, 2, 3'
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
    url="/rebate/user/sub_relation"
    query_param="user_id_list=1, 2, 3"
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
      "list": [
        {
          "belong": "",
          "ref_uid": 0,
          "type": 0,
          "uid": 9
        },
        {
          "belong": "partner",
          "type": 1,
          "ref_uid": 1,
          "uid": 2
        },
        {
          "belong": "referral",
          "type": 5,
          "ref_uid": 1,
          "uid": 3
        }
      ]
    }
    

##  Get recent partner application records🔒 Authenticated

GET`/rebate/partner/applications/recent`

GET `/rebate/partner/applications/recent`

Get `recent partner application records`

Get `the current user's recent partner application records. This endpoint returns application records within the last 30 days, including application status, review information, application materials, and other details.`

### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Successful response

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Successful response | Inline  
  
### Response Schema

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
    
    url = '/rebate/partner/applications/recent'
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
    url="/rebate/partner/applications/recent"
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

> Successful response
    
    
    {
      "code": 0,
      "message": "success",
      "data": {
        "id": 64779,
        "uid": 19669134,
        "language": "cn",
        "country_id": 37,
        "firstname": "交易员",
        "lastname": "",
        "email": "992937821@qq.com",
        "join_uid": 19669134,
        "join_country_id": 0,
        "identity_comment": "内容创作者",
        "promotion_channels": "19|15|1",
        "contact_details": "{\"4\":\"992937821\",\"2\":\"13169503913\"}",
        "know_details": "",
        "question_lang": "cn",
        "create_timest": "2026-03-16 02:22:28",
        "update_timest": "2026-03-16 02:22:28",
        "apply_type": 1,
        "audit_status": 0,
        "edit_counts": 1,
        "proof_images": "rebate/gateio/referral/apply_partner/69b76933b6583",
        "proof_videos": "",
        "proof_url": "https://mp.weixin.qq.com/s/zotzOCVoxKeukzM7hY4VWA",
        "audit_reason": 0,
        "channel_type": 3,
        "region": "cn",
        "phone": "13169503913",
        "telegram": "",
        "other_contact": {
          "type": 4,
          "value": "992937821"
        },
        "proof_images_url_list": [
          "https://gateio-service-private.gateio.services/rebate/gateio/referral/apply_partner/69b76933b6583?X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&..."
        ],
        "proof_videos_url_list": [],
        "apply_msg": "您的代理申请已成功提交，正在审核中，我们将于 1-3 个工作日内完成审核并与您取得联系",
        "jump_url": "/referral/affiliate/program-application"
      },
      "timestamp": 1773637797
    }
    

##  Check partner application eligibility🔒 Authenticated

GET`/rebate/partner/eligibility`

GET `/rebate/partner/eligibility`

_Check partner application eligibility_

Check whether the current user is eligible to apply as a partner. This endpoint checks multiple conditions: account status (banned or not), whether it is a sub-account, whether already a partner, KYC verification status, whether under another agent's referral chain, whether on the blacklist, and other business rule restrictions

### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Successful response

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Successful response | Inline  
  
### Response Schema

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
    
    url = '/rebate/partner/eligibility'
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
    url="/rebate/partner/eligibility"
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

> Successful response
    
    
    {
      "code": 0,
      "message": "success",
      "data": {
        "eligible": true,
        "block_reasons": [],
        "block_reason_codes": []
      },
      "timestamp": 1738886400
    }
    
    
    
    {
      "code": 0,
      "message": "success",
      "data": {
        "eligible": false,
        "block_reasons": [
          "当前账号为子账号，请您切换至主账号完成申请。"
        ],
        "block_reason_codes": [
          "sub_account"
        ]
      },
      "timestamp": 1738886400
    }
    

##  Aggregated partner agent statistics🔒 Authenticated

GET`/rebate/partner/data/aggregated`

GET `/rebate/partner/data/aggregated`

_Aggregated partner agent statistics_

Query aggregated partner-agent statistics for a time range, including rebate amount, trading volume, net fee, customer count, and trading user count. **Notes:**

  * `trading_user_count` is only returned when `business_type=0` (All).
  * Time parameters use UTC+8.
  * If no time range is passed, the last 7 days are queried by default.
  * Partner agents only; sub-accounts are not allowed.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
start_date | query | string | Optional | Query start time, format: yyyy-mm-dd hh:ii:ss (UTC+8).  
If omitted, defaults to the start of the last 7 days.  
end_date | query | string | Optional | Query end time, format: yyyy-mm-dd hh:ii:ss (UTC+8).  
If omitted, defaults to the end of the last 7 days.  
business_type | query | integer | Optional | Business type filter:  
\- 0: All (default)  
\- 1: Spot  
\- 2: Futures  
\- 3: Alpha  
\- 4: Web3  
\- 5: Perps (DEX)  
\- 6: Exchange All  
\- 7: Web3 All  
\- 8: TradFi  
  
####  Detailed descriptions

**start_date** : Query start time, format: yyyy-mm-dd hh:ii:ss (UTC+8).  
If omitted, defaults to the start of the last 7 days.

**end_date** : Query end time, format: yyyy-mm-dd hh:ii:ss (UTC+8).  
If omitted, defaults to the end of the last 7 days.

**business_type** : Business type filter:  
\- 0: All (default)  
\- 1: Spot  
\- 2: Futures  
\- 3: Alpha  
\- 4: Web3  
\- 5: Perps (DEX)  
\- 6: Exchange All  
\- 7: Web3 All  
\- 8: TradFi

####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
business_type | 0  
business_type | 1  
business_type | 2  
business_type | 3  
business_type | 4  
business_type | 5  
business_type | 6  
business_type | 7  
business_type | 8  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful
  * 400[Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1)Invalid request parameters
  * 401[Unauthorized ](https://tools.ietf.org/html/rfc7235#section-3.1)Unauthorized access
  * 403[Forbidden ](https://tools.ietf.org/html/rfc7231#section-6.5.3)Access denied

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | Inline  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Invalid request parameters | ErrorResponse  
401 | [Unauthorized ](https://tools.ietf.org/html/rfc7235#section-3.1) | Unauthorized access | ErrorResponse  
403 | [Forbidden ](https://tools.ietf.org/html/rfc7231#section-6.5.3) | Access denied | ErrorResponse  
  
### Response Schema

####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
business_type | 0  
business_type | 1  
business_type | 2  
business_type | 3  
business_type | 4  
business_type | 5  
business_type | 6  
business_type | 7  
business_type | 8  
  
Status Code **400**

Name | Type | Description  
---|---|---  
» code | integer | Error code  
» message | string | Error message  
» data | object | Empty object  
» timestamp | integer(int64) | Unix timestamp  
  
Status Code **401**

Name | Type | Description  
---|---|---  
» code | integer | Error code  
» message | string | Error message  
» data | object | Empty object  
» timestamp | integer(int64) | Unix timestamp  
  
Status Code **403**

Name | Type | Description  
---|---|---  
» code | integer | Error code  
» message | string | Error message  
» data | object | Empty object  
» timestamp | integer(int64) | Unix timestamp  
  
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
    
    url = '/rebate/partner/data/aggregated'
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
    url="/rebate/partner/data/aggregated"
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

> Query successful
    
    
    {
      "code": 0,
      "message": "success",
      "data": {
        "rebate_amount": "1234.567890",
        "trade_volume": "9876543.210000",
        "net_fee": "543.210000",
        "customer_count": 150,
        "trading_user_count": "85",
        "time_range_desc": "2024-01-01 ~ 2024-01-07",
        "business_type": 0,
        "business_type_desc": "全部"
      },
      "timestamp": 1738886400
    }
    
    
    
    {
      "code": 0,
      "message": "success",
      "data": {
        "rebate_amount": "456.123000",
        "trade_volume": "2345678.900000",
        "net_fee": "234.560000",
        "customer_count": 75,
        "trading_user_count": null,
        "time_range_desc": "2024-01-01 ~ 2024-01-07",
        "business_type": 1,
        "business_type_desc": "现货"
      },
      "timestamp": 1738886400
    }
    

> Invalid request parameters
    
    
    {
      "code": 400,
      "message": "Invalid time range parameter",
      "data": {},
      "timestamp": 1738886400
    }
    

> Unauthorized access
    
    
    {
      "code": 401,
      "message": "Unauthorized",
      "data": {},
      "timestamp": 1738886400
    }
    

> Access denied
    
    
    {
      "code": 403,
      "message": "Sub-accounts are not allowed to access this API",
      "data": {},
      "timestamp": 1738886400
    }
    
    
    
    {
      "code": 403,
      "message": "Current account is not a partner agent",
      "data": {},
      "timestamp": 1738886400
    }
    

#  Schemas

##  RebateUserInfo

_Retrieve user rebate information_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
invite_uid | integer(int64) | Optional | none | My inviter's UID  
      
    
    {
      "invite_uid": 0
    }
    
    

##  PartnerDataAggregatedResponse

###  Properties

_allOf_

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
_None_ | object | Optional | none | none  
↳ code | integer | Required | none | Error Code, 0 Indicates Success  
↳ message | string | Required | none | Error message description  
↳ data | object | Required | none | Response data  
↳ timestamp | integer(int64) | Required | none | Unix timestamp  
  
_and_

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
_None_ | object | Optional | none | none  
↳ data | object | Optional | none | none  
↳ rebate_amount | string | Required | none | Rebate amount as a string for precision.  
Up to 6 decimal places; trailing zeros removed.  
↳ trade_volume | string | Required | none | Trading volume as a string for precision.  
Up to 6 decimal places; trailing zeros removed.  
↳ net_fee | string | Required | none | Net fee as a string for precision.  
Up to 6 decimal places; trailing zeros removed.  
↳ customer_count | integer | Required | none | Customer count (invited users)  
↳ trading_user_count | string|null | Required | none | Transaction participant count (string format, consistent with online JSON serialization) only returns a specific value when business_type=0(all), and returns nullfor other business types.  
↳ time_range_desc | string | Required | none | Time range description  
↳ business_type | integer | Required | none | Business Type  
↳ business_type_desc | string | Required | none | Business type description; allowed values: All, Spot, Futures, Alpha, Web3, Perps (DEX), Exchange All, Web3 All, TradFi  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
business_type | 0  
business_type | 1  
business_type | 2  
business_type | 3  
business_type | 4  
business_type | 5  
business_type | 6  
business_type | 7  
business_type | 8  
      
    
    {
      "code": 0,
      "message": "success",
      "data": {
        "rebate_amount": "1234.567890",
        "trade_volume": "9876543.210000",
        "net_fee": "543.210000",
        "customer_count": 150,
        "trading_user_count": "85",
        "time_range_desc": "2024-01-01 ~ 2024-01-07",
        "business_type": 0,
        "business_type_desc": "全部"
      },
      "timestamp": 1773637797
    }
    
    

##  PartnerTransactionHistory

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
total | integer(int64) | Optional | none | Total  
list | array | Optional | none | List of transaction history  
↳ PartnerTransaction | object | Optional | none | none  
↳ transaction_time | integer(int64) | Optional | none | Transaction Time. (unix timestamp)  
↳ user_id | integer(int64) | Optional | none | User ID  
↳ group_name | string | Optional | none | Group name  
↳ fee | string | Optional | none | Fee  
↳ fee_asset | string | Optional | none | Fee currency  
↳ currency_pair | string | Optional | none | Currency pair  
↳ amount | string | Optional | none | Transaction amount  
↳ amount_asset | string | Optional | none | Transaction amount currency  
↳ source | string | Optional | none | Commission source: SPOT - Spot commission, FUTURES - Futures commission  
      
    
    {
      "total": 0,
      "list": [
        {
          "transaction_time": 0,
          "user_id": 0,
          "group_name": "string",
          "fee": "string",
          "fee_asset": "string",
          "currency_pair": "string",
          "amount": "string",
          "amount_asset": "string",
          "source": "string"
        }
      ]
    }
    
    

##  AgencyTransactionHistory

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
currency_pair | string | Optional | none | Currency pair  
total | integer(int64) | Optional | none | Total  
list | array | Optional | none | List of transaction history  
↳ AgencyTransaction | object | Optional | none | none  
↳ transaction_time | integer(int64) | Optional | none | Transaction Time. (unix timestamp)  
↳ user_id | integer(int64) | Optional | none | User ID  
↳ group_name | string | Optional | none | Group name  
↳ fee | string | Optional | none | Fee  
↳ fee_asset | string | Optional | none | Fee currency  
↳ currency_pair | string | Optional | none | Currency pair  
↳ amount | string | Optional | none | Transaction amount  
↳ amount_asset | string | Optional | none | Transaction amount currency  
↳ source | string | Optional | none | Commission source: SPOT - Spot commission, FUTURES - Futures commission  
      
    
    {
      "currency_pair": "string",
      "total": 0,
      "list": [
        {
          "transaction_time": 0,
          "user_id": 0,
          "group_name": "string",
          "fee": "string",
          "fee_asset": "string",
          "currency_pair": "string",
          "amount": "string",
          "amount_asset": "string",
          "source": "string"
        }
      ]
    }
    
    

##  PartnerSubList

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
total | integer(int64) | Optional | none | Total  
list | array | Optional | none | Subordinate list  
↳ PartnerSub | object | Optional | none | none  
↳ user_id | integer(int64) | Optional | none | User ID  
↳ user_join_time | integer(int64) | Optional | none | Time when user joined the system, Unix timestamp in seconds  
↳ type | integer(int64) | Optional | none | Type (1-Sub-agent 2-Indirect direct customer 3-Direct direct customer)  
      
    
    {
      "total": 0,
      "list": [
        {
          "user_id": 0,
          "user_join_time": 0,
          "type": 0
        }
      ]
    }
    
    

##  UserSubRelation

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
list | array | Optional | none | Subordinate relationship list  
↳ UserSub | object | Optional | none | none  
↳ uid | integer(int64) | Optional | none | User ID  
↳ belong | string | Optional | none | User's system affiliation (partner/referral). Empty means not belonging to any system  
↳ type | integer(int64) | Optional | none | Type (0-Not in system 1-Direct subordinate agent 2-Indirect subordinate agent 3-Direct direct customer 4-Indirect direct customer 5-Regular user)  
↳ ref_uid | integer(int64) | Optional | none | Inviter user ID  
      
    
    {
      "list": [
        {
          "uid": 0,
          "belong": "string",
          "type": 0,
          "ref_uid": 0
        }
      ]
    }
    
    

##  BrokerCommission

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
total | integer(int64) | Optional | none | Total  
list | array | Optional | none | List of commission history  
↳ BrokerCommissionItem | object | Optional | none | none  
↳ commission_time | integer(int64) | Optional | none | Commission time (Unix timestamp in seconds)  
↳ user_id | integer(int64) | Optional | none | User ID  
↳ group_name | string | Optional | none | Group name  
↳ amount | string | Optional | none | The amount of commission rebates  
↳ fee | string | Optional | none | Fee  
↳ fee_asset | string | Optional | none | Fee currency  
↳ rebate_fee | string | Optional | none | The income from rebates, converted to USDT  
↳ source | string | Optional | none | Commission transaction type: Spot, Futures, Options, Alpha、TradFi  
↳ currency_pair | string | Optional | none | Currency pair  
↳ sub_broker_info | object | Optional | none | Sub-broker information  
↳ user_id | integer(int64) | Optional | none | Sub-broker user ID  
↳ original_commission_rate | string | Optional | none | Sub-broker original commission rate  
↳ relative_commission_rate | string | Optional | none | Sub-broker relative commission rate  
↳ commission_rate | string | Optional | none | Sub-broker actual commission rate  
↳ alpha_contract_addr | string | Optional | none | Alpha contract address  
      
    
    {
      "total": 0,
      "list": [
        {
          "commission_time": 0,
          "user_id": 0,
          "group_name": "string",
          "amount": "string",
          "fee": "string",
          "fee_asset": "string",
          "rebate_fee": "string",
          "source": "string",
          "currency_pair": "string",
          "sub_broker_info": {},
          "alpha_contract_addr": "string"
        }
      ]
    }
    
    

##  PartnerApplicationResponse

###  Properties

_allOf_

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
_None_ | PartnerDataAggregatedResponse/allOf/0 | Optional | none | none  
  
_and_

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
_None_ | object | Optional | none | none  
↳ data | object | Optional | none | none  
↳ id | integer | Optional | none | Application record ID  
↳ uid | integer | Optional | none | User ID  
↳ language | string | Optional | none | Language code  
↳ country_id | integer | Optional | none | Country ID  
↳ firstname | string | Optional | none | First name  
↳ lastname | string | Optional | none | Last name  
↳ email | string(email) | Optional | none | Email address  
↳ join_uid | integer | Optional | none | Joined user ID  
↳ join_country_id | integer | Optional | none | Joined country ID  
↳ identity_comment | string | Optional | none | Identity description  
↳ promotion_channels | string | Optional | none | Promotion channels, separated by  
↳ contact_details | string | Optional | none | Contact details (JSON string)  
↳ know_details | string | Optional | none | Learn more  
↳ question_lang | string | Optional | none | Question language  
↳ create_timest | string(date-time) | Optional | none | Created time  
↳ update_timest | string(date-time) | Optional | none | Update time  
↳ apply_type | integer | Optional | none | Application type  
↳ audit_status | integer | Optional | none | Review status (0 - pending, 1 - approved, 2 - rejected)  
↳ edit_counts | integer | Optional | none | Edit count  
↳ proof_images | string | Optional | none | Proof image path  
↳ proof_videos | string | Optional | none | Proof video path  
↳ proof_url | string(uri) | Optional | none | Proof link  
↳ audit_reason | integer | Optional | none | Review reason code  
↳ channel_type | integer | Optional | none | Channel type  
↳ region | string | Optional | none | Region  
↳ phone | string | Optional | none | Phone number  
↳ telegram | string | Optional | none | Telegram account  
↳ other_contact | object | Optional | none | Other contact information  
↳ type | integer | Optional | none | Contact type  
↳ value | string | Optional | none | Contact value  
↳ proof_images_url_list | array | Optional | none | List of proof image URLs  
↳ proof_videos_url_list | array | Optional | none | List of proof video URLs  
↳ apply_msg | string | Optional | none | Application message  
↳ jump_url | string | Optional | none | Redirect URL  
      
    
    {
      "code": 0,
      "message": "success",
      "data": {
        "id": 64779,
        "uid": 19669134,
        "language": "cn",
        "country_id": 37,
        "firstname": "交易员",
        "lastname": "",
        "email": "992937821@qq.com",
        "join_uid": 19669134,
        "join_country_id": 0,
        "identity_comment": "内容创作者",
        "promotion_channels": "19|15|1",
        "contact_details": "{\"4\":\"992937821\",\"2\":\"13169503913\"}",
        "know_details": "",
        "question_lang": "cn",
        "create_timest": "2026-03-16 02:22:28",
        "update_timest": "2026-03-16 02:22:28",
        "apply_type": 1,
        "audit_status": 0,
        "edit_counts": 1,
        "proof_images": "rebate/gateio/referral/apply_partner/69b76933b6583",
        "proof_videos": "",
        "proof_url": "https://mp.weixin.qq.com/s/zotzOCVoxKeukzM7hY4VWA",
        "audit_reason": 0,
        "channel_type": 3,
        "region": "cn",
        "phone": "13169503913",
        "telegram": "",
        "other_contact": {
          "type": 4,
          "value": "992937821"
        },
        "proof_images_url_list": [
          "https://gateio-service-private.gateio.services/rebate/gateio/referral/apply_partner/69b76933b6583?..."
        ],
        "proof_videos_url_list": [],
        "apply_msg": "您的代理申请已成功提交，正在审核中，我们将于 1-3 个工作日内完成审核并与您取得联系",
        "jump_url": "/referral/affiliate/program-application"
      },
      "timestamp": 1773637797
    }
    
    

##  AgencyCommissionHistory

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
currency_pair | string | Optional | none | Currency pair  
total | integer(int64) | Optional | none | Total  
list | array | Optional | none | List of commission history  
↳ AgencyCommission | object | Optional | none | none  
↳ commission_time | integer(int64) | Optional | none | Commission time (Unix timestamp in seconds)  
↳ user_id | integer(int64) | Optional | none | User ID  
↳ group_name | string | Optional | none | Group name  
↳ commission_amount | string | Optional | none | Commission amount  
↳ commission_asset | string | Optional | none | Commission Asset  
↳ source | string | Optional | none | Commission source: SPOT - Spot commission, FUTURES - Futures commission  
      
    
    {
      "currency_pair": "string",
      "total": 0,
      "list": [
        {
          "commission_time": 0,
          "user_id": 0,
          "group_name": "string",
          "commission_amount": "string",
          "commission_asset": "string",
          "source": "string"
        }
      ]
    }
    
    

##  PartnerCommissionHistory

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
total | integer(int64) | Optional | none | Total  
list | array | Optional | none | List of commission history  
↳ PartnerCommission | object | Optional | none | none  
↳ commission_time | integer(int64) | Optional | none | Commission time (Unix timestamp in seconds)  
↳ user_id | integer(int64) | Optional | none | User ID  
↳ group_name | string | Optional | none | Group name  
↳ commission_amount | string | Optional | none | Commission amount  
↳ commission_asset | string | Optional | none | Commission Asset  
↳ source | string | Optional | none | Commission source: SPOT - Spot commission, FUTURES - Futures commission  
      
    
    {
      "total": 0,
      "list": [
        {
          "commission_time": 0,
          "user_id": 0,
          "group_name": "string",
          "commission_amount": "string",
          "commission_asset": "string",
          "source": "string"
        }
      ]
    }
    
    

##  BrokerTransactionHistory

_BrokerTransactionHistory_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
total | integer(int64) | Optional | none | Total  
list | array | Optional | none | List of transaction history  
↳ BrokerTransaction | object | Optional | none | none  
↳ transaction_time | integer(int64) | Optional | none | Transaction Time. (unix timestamp)  
↳ user_id | integer(int64) | Optional | none | User ID  
↳ group_name | string | Optional | none | Group name  
↳ fee | string | Optional | none | Fee amount (USDT)  
↳ currency_pair | string | Optional | none | Currency pair  
↳ amount | string | Optional | none | Transaction amount  
↳ fee_asset | string | Optional | none | Fee currency  
↳ source | string | Optional | none | Commission transaction type: Spot, Futures, Options, Alpha、TradFi  
↳ sub_broker_info | object | Optional | none | Sub-broker information  
↳ user_id | integer(int64) | Optional | none | Sub-broker user ID  
↳ original_commission_rate | string | Optional | none | Sub-broker original commission rate  
↳ relative_commission_rate | string | Optional | none | Sub-broker relative commission rate  
↳ commission_rate | string | Optional | none | Sub-broker actual commission rate  
↳ alpha_contract_addr | string | Optional | none | Alpha contract address  
      
    
    {
      "total": 0,
      "list": [
        {
          "transaction_time": 0,
          "user_id": 0,
          "group_name": "string",
          "fee": "string",
          "currency_pair": "string",
          "amount": "string",
          "fee_asset": "string",
          "source": "string",
          "sub_broker_info": {},
          "alpha_contract_addr": "string"
        }
      ]
    }
    
    

##  EligibilityResponse

###  Properties

_allOf_

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
_None_ | PartnerDataAggregatedResponse/allOf/0 | Optional | none | none  
  
_and_

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
_None_ | object | Optional | none | none  
↳ data | object | Optional | none | none  
↳ eligible | boolean | Required | none | Whether eligible for application  
↳ block_reasons | array | Required | none | List of ineligibility reason descriptions  
↳ block_reason_codes | array | Required | none | List of ineligibility reason codes  
      
    
    {
      "code": 0,
      "message": "success",
      "data": {
        "eligible": false,
        "block_reasons": [
          "当前账号为子账号，请您切换至主账号完成申请。"
        ],
        "block_reason_codes": [
          "sub_account"
        ]
      },
      "timestamp": 1773637797
    }
    
    

##  ErrorResponse

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
code | integer | Required | none | Error code  
message | string | Required | none | Error message  
data | object | Required | none | Empty object  
timestamp | integer(int64) | Required | none | Unix timestamp  
      
    
    {
      "code": 401,
      "message": "Unauthorized",
      "data": {},
      "timestamp": 1773637797
    }