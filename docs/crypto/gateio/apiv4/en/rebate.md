---
exchange: gateio
source_url: https://www.gate.com/docs/developers/apiv4/en/rebate
api_type: Earn
updated_at: 2026-11-28 18:55:34.786887
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

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | AgencyTransactionHistory  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
AgencyTransactionHistory |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
currency_pair | string | Optional |  | Currency pair  
total | integer(int64) | Optional |  | Total  
list | array | Optional |  | List of transaction history  
  
**list**

List of transaction history

Type | Constraints  
---|---  
array |   
  
**list / items**

AgencyTransaction

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
transaction_time | integer(int64) | Optional |  | Transaction Time. (unix timestamp)  
user_id | integer(int64) | Optional |  | User ID  
group_name | string | Optional |  | Group name  
fee | string | Optional |  | Fee  
fee_asset | string | Optional |  | Fee currency  
currency_pair | string | Optional |  | Currency pair  
amount | string | Optional |  | Transaction amount  
amount_asset | string | Optional |  | Transaction amount currency  
source | string | Optional |  | Commission source: SPOT - Spot commission, FUTURES - Futures commission  
  
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

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | AgencyCommissionHistory  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
AgencyCommissionHistory |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
currency_pair | string | Optional |  | Currency pair  
total | integer(int64) | Optional |  | Total  
list | array | Optional |  | List of commission history  
  
**list**

List of commission history

Type | Constraints  
---|---  
array |   
  
**list / items**

AgencyCommission

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
commission_time | integer(int64) | Optional |  | Commission time (Unix timestamp in seconds)  
user_id | integer(int64) | Optional |  | User ID  
group_name | string | Optional |  | Group name  
commission_amount | string | Optional |  | Commission amount  
commission_asset | string | Optional |  | Commission Asset  
source | string | Optional |  | Commission source: SPOT - Spot commission, FUTURES - Futures commission  
  
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

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | PartnerTransactionHistory  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
PartnerTransactionHistory |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
total | integer(int64) | Optional |  | Total  
list | array | Optional |  | List of transaction history  
  
**list**

List of transaction history

Type | Constraints  
---|---  
array |   
  
**list / items**

PartnerTransaction

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
transaction_time | integer(int64) | Optional |  | Transaction Time. (unix timestamp)  
user_id | integer(int64) | Optional |  | User ID  
group_name | string | Optional |  | Group name  
fee | string | Optional |  | Fee  
fee_asset | string | Optional |  | Fee currency  
currency_pair | string | Optional |  | Currency pair  
amount | string | Optional |  | Transaction amount  
amount_asset | string | Optional |  | Transaction amount currency  
source | string | Optional |  | Commission source: SPOT - Spot commission, FUTURES - Futures commission  
  
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

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | PartnerCommissionHistory  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
PartnerCommissionHistory |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
total | integer(int64) | Optional |  | Total  
list | array | Optional |  | List of commission history  
  
**list**

List of commission history

Type | Constraints  
---|---  
array |   
  
**list / items**

PartnerCommission

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
commission_time | integer(int64) | Optional |  | Commission time (Unix timestamp in seconds)  
user_id | integer(int64) | Optional |  | User ID  
group_name | string | Optional |  | Group name  
commission_amount | string | Optional |  | Commission amount  
commission_asset | string | Optional |  | Commission Asset  
source | string | Optional |  | Commission source: SPOT - Spot commission, FUTURES - Futures commission  
  
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

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | PartnerSubList  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
PartnerSubList |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
total | integer(int64) | Optional |  | Total  
list | array | Optional |  | Subordinate list  
  
**list**

Subordinate list

Type | Constraints  
---|---  
array |   
  
**list / items**

PartnerSub

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
user_id | integer(int64) | Optional |  | User ID  
user_join_time | integer(int64) | Optional |  | Time when user joined the system, Unix timestamp in seconds  
type | integer(int64) | Optional |  | Type (1-Sub-agent 2-Indirect direct customer 3-Direct direct customer)  
  
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

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | BrokerCommission  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
BrokerCommission |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
total | integer(int64) | Optional |  | Total  
list | array | Optional |  | List of commission history  
  
**list**

List of commission history

Type | Constraints  
---|---  
array |   
  
**list / items**

BrokerCommissionItem

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
commission_time | integer(int64) | Optional |  | Commission time (Unix timestamp in seconds)  
user_id | integer(int64) | Optional |  | User ID  
group_name | string | Optional |  | Group name  
amount | string | Optional |  | The amount of commission rebates  
fee | string | Optional |  | Fee  
fee_asset | string | Optional |  | Fee currency  
rebate_fee | string | Optional |  | The income from rebates, converted to USDT  
source | string | Optional |  | Commission transaction type: Spot, Futures, Options, Alpha、TradFi  
currency_pair | string | Optional |  | Currency pair  
sub_broker_info | object | Optional |  | Sub-broker information  
alpha_contract_addr | string | Optional |  | Alpha contract address  
  
**list / items / sub_broker_info**

Sub-broker information

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
user_id | integer(int64) | Optional |  | Sub-broker user ID  
original_commission_rate | string | Optional |  | Sub-broker original commission rate  
relative_commission_rate | string | Optional |  | Sub-broker relative commission rate  
commission_rate | string | Optional |  | Sub-broker actual commission rate  
  
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

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | BrokerTransactionHistory  
  
### Response Schema

Status Code **200**

BrokerTransactionHistory

Type | Constraints  
---|---  
BrokerTransactionHistory |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
total | integer(int64) | Optional |  | Total  
list | array | Optional |  | List of transaction history  
  
**list**

List of transaction history

Type | Constraints  
---|---  
array |   
  
**list / items**

BrokerTransaction

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
transaction_time | integer(int64) | Optional |  | Transaction Time. (unix timestamp)  
user_id | integer(int64) | Optional |  | User ID  
group_name | string | Optional |  | Group name  
fee | string | Optional |  | Fee amount (USDT)  
currency_pair | string | Optional |  | Currency pair  
amount | string | Optional |  | Transaction amount  
fee_asset | string | Optional |  | Fee currency  
source | string | Optional |  | Commission transaction type: Spot, Futures, Options, Alpha、TradFi  
sub_broker_info | object | Optional |  | Sub-broker information  
alpha_contract_addr | string | Optional |  | Alpha contract address  
  
**list / items / sub_broker_info**

Sub-broker information

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
user_id | integer(int64) | Optional |  | Sub-broker user ID  
original_commission_rate | string | Optional |  | Sub-broker original commission rate  
relative_commission_rate | string | Optional |  | Sub-broker relative commission rate  
commission_rate | string | Optional |  | Sub-broker actual commission rate  
  
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

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | RebateUserInfo  
  
### Response Schema

Status Code **200**

Retrieve user rebate information

Type | Constraints  
---|---  
RebateUserInfo |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
invite_uid | integer(int64) | Optional |  | My inviter's UID  
  
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

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | UserSubRelation  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
UserSubRelation |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
list | array | Optional |  | Subordinate relationship list  
  
**list**

Subordinate relationship list

Type | Constraints  
---|---  
array |   
  
**list / items**

UserSub

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
uid | integer(int64) | Optional |  | User ID  
belong | string | Optional |  | User's system affiliation (partner/referral). Empty means not belonging to any system  
type | integer(int64) | Optional |  | Type (0-Not in system 1-Direct subordinate agent 2-Indirect subordinate agent 3-Direct direct customer 4-Indirect direct customer 5-Regular user)  
ref_uid | integer(int64) | Optional |  | Inviter user ID  
  
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

_Get recent partner application records_

Get the current user's recent partner application records. This endpoint returns application records within the last 30 days, including application status, review information, application materials, and other details.

### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Successful response | Inline  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
PartnerApplicationResponse |   
  
**allOf[0]**

Type | Constraints  
---|---  
object | required: ["code","message","data","timestamp"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
code | integer | Required |  | Error Code, 0 Indicates Success  
message | string | Required |  | Error message description  
data | object | Required |  | Response data  
timestamp | integer(int64) | Required |  | Unix timestamp  
  
**allOf[1]**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
data | object | Required |  |   
  
**allOf[1] / data**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | integer | Optional |  | Application record ID  
uid | integer | Optional |  | User ID  
language | string | Optional |  | Language code  
country_id | integer | Optional |  | Country ID  
firstname | string | Optional |  | First name  
lastname | string | Optional |  | Last name  
email | string(email) | Optional |  | Email address  
join_uid | integer | Optional |  | Joined user ID  
join_country_id | integer | Optional |  | Joined country ID  
identity_comment | string | Optional |  | Identity description  
promotion_channels | string | Optional |  | Promotion channels, separated by |  
contact_details | string | Optional |  | Contact details (JSON string)  
know_details | string | Optional |  | Learn more  
question_lang | string | Optional |  | Question language  
create_timest | string(date-time) | Optional |  | Created time  
update_timest | string(date-time) | Optional |  | Update time  
apply_type | integer | Optional |  | Application type  
audit_status | integer | Optional |  | Review status (0 - pending, 1 - approved, 2 - rejected)  
edit_counts | integer | Optional |  | Edit count  
proof_images | string | Optional |  | Proof image path  
proof_videos | string | Optional |  | Proof video path  
proof_url | string(uri) | Optional |  | Proof link  
audit_reason | integer | Optional |  | Review reason code  
channel_type | integer | Optional |  | Channel type  
region | string | Optional |  | Region  
phone | string | Optional |  | Phone number  
telegram | string | Optional |  | Telegram account  
other_contact | object | Optional |  | Other contact information  
proof_images_url_list | array | Optional |  | List of proof image URLs  
proof_videos_url_list | array | Optional |  | List of proof video URLs  
apply_msg | string | Optional |  | Application message  
jump_url | string | Optional |  | Redirect URL  
  
**allOf[1] / data / other_contact**

OtherContact

Other contact information

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
type | integer | Optional |  | Contact type  
value | string | Optional |  | Contact value  
  
**allOf[1] / data / proof_images_url_list**

List of proof image URLs

Type | Constraints  
---|---  
array |   
  
**allOf[1] / data / proof_images_url_list / items**

Type | Constraints  
---|---  
string(uri) |   
  
**allOf[1] / data / proof_videos_url_list**

List of proof video URLs

Type | Constraints  
---|---  
array |   
  
**allOf[1] / data / proof_videos_url_list / items**

Type | Constraints  
---|---  
string(uri) |   
  
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

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Successful response | Inline  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
EligibilityResponse |   
  
**allOf[0]**

Type | Constraints  
---|---  
object | required: ["code","message","data","timestamp"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
code | integer | Required |  | Error Code, 0 Indicates Success  
message | string | Required |  | Error message description  
data | object | Required |  | Response data  
timestamp | integer(int64) | Required |  | Unix timestamp  
  
**allOf[1]**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
data | object | Required | required: ["eligible","block_reasons","block_reason_codes"] |   
  
**allOf[1] / data**

Type | Constraints  
---|---  
object | required: ["eligible","block_reasons","block_reason_codes"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
eligible | boolean | Required |  | Whether eligible for application  
block_reasons | array | Required |  | List of ineligibility reason descriptions  
block_reason_codes | array | Required |  | List of ineligibility reason codes  
  
**allOf[1] / data / block_reasons**

List of ineligibility reason descriptions

Type | Constraints  
---|---  
array |   
  
**allOf[1] / data / block_reasons / items**

Type | Constraints  
---|---  
string |   
  
**allOf[1] / data / block_reason_codes**

List of ineligibility reason codes

Type | Constraints  
---|---  
array |   
  
**allOf[1] / data / block_reason_codes / items**

Type | Constraints  
---|---  
string |   
  
**Enumerated Values**

Value  
---  
"user_not_exist"  
"user_blacked"  
"sub_account"  
"already_agent"  
"kyc_incomplete"  
"in_agent_tree"  
"ch_code_conflict"  
  
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

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | Inline  
400 | [Bad Request ](https://tools.ietf.org/html/rfc7231#section-6.5.1) | Invalid request parameters | ErrorResponse  
401 | [Unauthorized ](https://tools.ietf.org/html/rfc7235#section-3.1) | Unauthorized access | ErrorResponse  
403 | [Forbidden ](https://tools.ietf.org/html/rfc7231#section-6.5.3) | Access denied | ErrorResponse  
  
### Response Schema

Status Code **200**

Type | Constraints  
---|---  
PartnerDataAggregatedResponse |   
  
**allOf[0]**

Type | Constraints  
---|---  
object | required: ["code","message","data","timestamp"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
code | integer | Required |  | Error Code, 0 Indicates Success  
message | string | Required |  | Error message description  
data | object | Required |  | Response data  
timestamp | integer(int64) | Required |  | Unix timestamp  
  
**allOf[1]**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
data | object | Required | required: ["rebate_amount","trade_volume","net_fee","customer_count","trading_user_count","time_range_desc","business_type","business_type_desc"] |   
  
**allOf[1] / data**

Type | Constraints  
---|---  
object | required: ["rebate_amount","trade_volume","net_fee","customer_count","trading_user_count","time_range_desc","business_type","business_type_desc"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
rebate_amount | string | Required | pattern: "^\\\d+(\\\\.\\\d{1,6})?$" | Rebate amount as a string for precision.  
Up to 6 decimal places; trailing zeros removed.  
trade_volume | string | Required | pattern: "^\\\d+(\\\\.\\\d{1,6})?$" | Trading volume as a string for precision.  
Up to 6 decimal places; trailing zeros removed.  
net_fee | string | Required | pattern: "^\\\d+(\\\\.\\\d{1,6})?$" | Net fee as a string for precision.  
Up to 6 decimal places; trailing zeros removed.  
customer_count | integer | Required | minimum: 0 | Customer count (invited users)  
trading_user_count | string|null | Required | nullable: true  
pattern: "^\\\d+$" | Transaction participant count (string format, consistent with online JSON serialization) only returns a specific value when business_type=0(all), and returns nullfor other business types.  
time_range_desc | string | Required | pattern: "^\\\d{4}-\\\d{2}-\\\d{2} ~ \\\d{4}-\\\d{2}-\\\d{2}$" | Time range description  
business_type | integer | Required | enum: [0,1,2,3,4,5,6,7,8] | Business Type  
business_type_desc | string | Required |  | Business type description; allowed values: All, Spot, Futures, Alpha, Web3, Perps (DEX), Exchange All, Web3 All, TradFi  
  
Status Code **400**

Type | Constraints  
---|---  
ErrorResponse | required: ["code","message","data","timestamp"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
code | integer | Required |  | Error code  
message | string | Required |  | Error message  
data | object | Required |  | Empty object  
timestamp | integer(int64) | Required |  | Unix timestamp  
  
Status Code **401**

Type | Constraints  
---|---  
ErrorResponse | required: ["code","message","data","timestamp"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
code | integer | Required |  | Error code  
message | string | Required |  | Error message  
data | object | Required |  | Empty object  
timestamp | integer(int64) | Required |  | Unix timestamp  
  
Status Code **403**

Type | Constraints  
---|---  
ErrorResponse | required: ["code","message","data","timestamp"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
code | integer | Required |  | Error code  
message | string | Required |  | Error message  
data | object | Required |  | Empty object  
timestamp | integer(int64) | Required |  | Unix timestamp  
  
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

##  AgencyCommissionHistory

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
currency_pair | string | Optional |  | Currency pair  
total | integer(int64) | Optional |  | Total  
list | array | Optional |  | List of commission history  
  
**list**

List of commission history

Type | Constraints  
---|---  
array |   
  
**list / items**

AgencyCommission

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
commission_time | integer(int64) | Optional |  | Commission time (Unix timestamp in seconds)  
user_id | integer(int64) | Optional |  | User ID  
group_name | string | Optional |  | Group name  
commission_amount | string | Optional |  | Commission amount  
commission_asset | string | Optional |  | Commission Asset  
source | string | Optional |  | Commission source: SPOT - Spot commission, FUTURES - Futures commission  
      
    
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
    
    

##  UserSubRelation

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
list | array | Optional |  | Subordinate relationship list  
  
**list**

Subordinate relationship list

Type | Constraints  
---|---  
array |   
  
**list / items**

UserSub

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
uid | integer(int64) | Optional |  | User ID  
belong | string | Optional |  | User's system affiliation (partner/referral). Empty means not belonging to any system  
type | integer(int64) | Optional |  | Type (0-Not in system 1-Direct subordinate agent 2-Indirect subordinate agent 3-Direct direct customer 4-Indirect direct customer 5-Regular user)  
ref_uid | integer(int64) | Optional |  | Inviter user ID  
      
    
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

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
total | integer(int64) | Optional |  | Total  
list | array | Optional |  | List of commission history  
  
**list**

List of commission history

Type | Constraints  
---|---  
array |   
  
**list / items**

BrokerCommissionItem

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
commission_time | integer(int64) | Optional |  | Commission time (Unix timestamp in seconds)  
user_id | integer(int64) | Optional |  | User ID  
group_name | string | Optional |  | Group name  
amount | string | Optional |  | The amount of commission rebates  
fee | string | Optional |  | Fee  
fee_asset | string | Optional |  | Fee currency  
rebate_fee | string | Optional |  | The income from rebates, converted to USDT  
source | string | Optional |  | Commission transaction type: Spot, Futures, Options, Alpha、TradFi  
currency_pair | string | Optional |  | Currency pair  
sub_broker_info | object | Optional |  | Sub-broker information  
alpha_contract_addr | string | Optional |  | Alpha contract address  
  
**list / items / sub_broker_info**

Sub-broker information

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
user_id | integer(int64) | Optional |  | Sub-broker user ID  
original_commission_rate | string | Optional |  | Sub-broker original commission rate  
relative_commission_rate | string | Optional |  | Sub-broker relative commission rate  
commission_rate | string | Optional |  | Sub-broker actual commission rate  
      
    
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
    
    

##  PartnerDataAggregatedResponse

Type | Constraints  
---|---  
allOf |   
  
**allOf[0]**

Type | Constraints  
---|---  
object | required: ["code","message","data","timestamp"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
code | integer | Required |  | Error Code, 0 Indicates Success  
message | string | Required |  | Error message description  
data | object | Required |  | Response data  
timestamp | integer(int64) | Required |  | Unix timestamp  
  
**allOf[1]**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
data | object | Required | required: ["rebate_amount","trade_volume","net_fee","customer_count","trading_user_count","time_range_desc","business_type","business_type_desc"] |   
  
**allOf[1] / data**

Type | Constraints  
---|---  
object | required: ["rebate_amount","trade_volume","net_fee","customer_count","trading_user_count","time_range_desc","business_type","business_type_desc"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
rebate_amount | string | Required | pattern: "^\\\d+(\\\\.\\\d{1,6})?$" | Rebate amount as a string for precision.  
Up to 6 decimal places; trailing zeros removed.  
trade_volume | string | Required | pattern: "^\\\d+(\\\\.\\\d{1,6})?$" | Trading volume as a string for precision.  
Up to 6 decimal places; trailing zeros removed.  
net_fee | string | Required | pattern: "^\\\d+(\\\\.\\\d{1,6})?$" | Net fee as a string for precision.  
Up to 6 decimal places; trailing zeros removed.  
customer_count | integer | Required | minimum: 0 | Customer count (invited users)  
trading_user_count | string|null | Required | nullable: true  
pattern: "^\\\d+$" | Transaction participant count (string format, consistent with online JSON serialization) only returns a specific value when business_type=0(all), and returns nullfor other business types.  
time_range_desc | string | Required | pattern: "^\\\d{4}-\\\d{2}-\\\d{2} ~ \\\d{4}-\\\d{2}-\\\d{2}$" | Time range description  
business_type | integer | Required | enum: [0,1,2,3,4,5,6,7,8] | Business Type  
business_type_desc | string | Required |  | Business type description; allowed values: All, Spot, Futures, Alpha, Web3, Perps (DEX), Exchange All, Web3 All, TradFi  
      
    
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
    
    

##  ErrorResponse

Type | Constraints  
---|---  
object | required: ["code","message","data","timestamp"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
code | integer | Required |  | Error code  
message | string | Required |  | Error message  
data | object | Required |  | Empty object  
timestamp | integer(int64) | Required |  | Unix timestamp  
      
    
    {
      "code": 401,
      "message": "Unauthorized",
      "data": {},
      "timestamp": 1773637797
    }
    
    

##  BrokerTransactionHistory

BrokerTransactionHistory

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
total | integer(int64) | Optional |  | Total  
list | array | Optional |  | List of transaction history  
  
**list**

List of transaction history

Type | Constraints  
---|---  
array |   
  
**list / items**

BrokerTransaction

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
transaction_time | integer(int64) | Optional |  | Transaction Time. (unix timestamp)  
user_id | integer(int64) | Optional |  | User ID  
group_name | string | Optional |  | Group name  
fee | string | Optional |  | Fee amount (USDT)  
currency_pair | string | Optional |  | Currency pair  
amount | string | Optional |  | Transaction amount  
fee_asset | string | Optional |  | Fee currency  
source | string | Optional |  | Commission transaction type: Spot, Futures, Options, Alpha、TradFi  
sub_broker_info | object | Optional |  | Sub-broker information  
alpha_contract_addr | string | Optional |  | Alpha contract address  
  
**list / items / sub_broker_info**

Sub-broker information

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
user_id | integer(int64) | Optional |  | Sub-broker user ID  
original_commission_rate | string | Optional |  | Sub-broker original commission rate  
relative_commission_rate | string | Optional |  | Sub-broker relative commission rate  
commission_rate | string | Optional |  | Sub-broker actual commission rate  
      
    
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
    
    

##  AgencyTransactionHistory

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
currency_pair | string | Optional |  | Currency pair  
total | integer(int64) | Optional |  | Total  
list | array | Optional |  | List of transaction history  
  
**list**

List of transaction history

Type | Constraints  
---|---  
array |   
  
**list / items**

AgencyTransaction

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
transaction_time | integer(int64) | Optional |  | Transaction Time. (unix timestamp)  
user_id | integer(int64) | Optional |  | User ID  
group_name | string | Optional |  | Group name  
fee | string | Optional |  | Fee  
fee_asset | string | Optional |  | Fee currency  
currency_pair | string | Optional |  | Currency pair  
amount | string | Optional |  | Transaction amount  
amount_asset | string | Optional |  | Transaction amount currency  
source | string | Optional |  | Commission source: SPOT - Spot commission, FUTURES - Futures commission  
      
    
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
    
    

##  PartnerCommissionHistory

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
total | integer(int64) | Optional |  | Total  
list | array | Optional |  | List of commission history  
  
**list**

List of commission history

Type | Constraints  
---|---  
array |   
  
**list / items**

PartnerCommission

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
commission_time | integer(int64) | Optional |  | Commission time (Unix timestamp in seconds)  
user_id | integer(int64) | Optional |  | User ID  
group_name | string | Optional |  | Group name  
commission_amount | string | Optional |  | Commission amount  
commission_asset | string | Optional |  | Commission Asset  
source | string | Optional |  | Commission source: SPOT - Spot commission, FUTURES - Futures commission  
      
    
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
    
    

##  PartnerApplicationResponse

Type | Constraints  
---|---  
allOf |   
  
**allOf[0]**

Type | Constraints  
---|---  
object | required: ["code","message","data","timestamp"]  
  
**allOf[1]**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
data | object | Required |  |   
  
**allOf[1] / data**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | integer | Optional |  | Application record ID  
uid | integer | Optional |  | User ID  
language | string | Optional |  | Language code  
country_id | integer | Optional |  | Country ID  
firstname | string | Optional |  | First name  
lastname | string | Optional |  | Last name  
email | string(email) | Optional |  | Email address  
join_uid | integer | Optional |  | Joined user ID  
join_country_id | integer | Optional |  | Joined country ID  
identity_comment | string | Optional |  | Identity description  
promotion_channels | string | Optional |  | Promotion channels, separated by |  
contact_details | string | Optional |  | Contact details (JSON string)  
know_details | string | Optional |  | Learn more  
question_lang | string | Optional |  | Question language  
create_timest | string(date-time) | Optional |  | Created time  
update_timest | string(date-time) | Optional |  | Update time  
apply_type | integer | Optional |  | Application type  
audit_status | integer | Optional |  | Review status (0 - pending, 1 - approved, 2 - rejected)  
edit_counts | integer | Optional |  | Edit count  
proof_images | string | Optional |  | Proof image path  
proof_videos | string | Optional |  | Proof video path  
proof_url | string(uri) | Optional |  | Proof link  
audit_reason | integer | Optional |  | Review reason code  
channel_type | integer | Optional |  | Channel type  
region | string | Optional |  | Region  
phone | string | Optional |  | Phone number  
telegram | string | Optional |  | Telegram account  
other_contact | object | Optional |  | Other contact information  
proof_images_url_list | array | Optional |  | List of proof image URLs  
proof_videos_url_list | array | Optional |  | List of proof video URLs  
apply_msg | string | Optional |  | Application message  
jump_url | string | Optional |  | Redirect URL  
  
**allOf[1] / data / other_contact**

OtherContact

Other contact information

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
type | integer | Optional |  | Contact type  
value | string | Optional |  | Contact value  
  
**allOf[1] / data / proof_images_url_list**

List of proof image URLs

Type | Constraints  
---|---  
array |   
  
**allOf[1] / data / proof_images_url_list / items**

Type | Constraints  
---|---  
string(uri) |   
  
**allOf[1] / data / proof_videos_url_list**

List of proof video URLs

Type | Constraints  
---|---  
array |   
  
**allOf[1] / data / proof_videos_url_list / items**

Type | Constraints  
---|---  
string(uri) |   
      
    
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
    
    

##  PartnerTransactionHistory

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
total | integer(int64) | Optional |  | Total  
list | array | Optional |  | List of transaction history  
  
**list**

List of transaction history

Type | Constraints  
---|---  
array |   
  
**list / items**

PartnerTransaction

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
transaction_time | integer(int64) | Optional |  | Transaction Time. (unix timestamp)  
user_id | integer(int64) | Optional |  | User ID  
group_name | string | Optional |  | Group name  
fee | string | Optional |  | Fee  
fee_asset | string | Optional |  | Fee currency  
currency_pair | string | Optional |  | Currency pair  
amount | string | Optional |  | Transaction amount  
amount_asset | string | Optional |  | Transaction amount currency  
source | string | Optional |  | Commission source: SPOT - Spot commission, FUTURES - Futures commission  
      
    
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
    
    

##  PartnerSubList

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
total | integer(int64) | Optional |  | Total  
list | array | Optional |  | Subordinate list  
  
**list**

Subordinate list

Type | Constraints  
---|---  
array |   
  
**list / items**

PartnerSub

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
user_id | integer(int64) | Optional |  | User ID  
user_join_time | integer(int64) | Optional |  | Time when user joined the system, Unix timestamp in seconds  
type | integer(int64) | Optional |  | Type (1-Sub-agent 2-Indirect direct customer 3-Direct direct customer)  
      
    
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
    
    

##  EligibilityResponse

Type | Constraints  
---|---  
allOf |   
  
**allOf[0]**

Type | Constraints  
---|---  
object | required: ["code","message","data","timestamp"]  
  
**allOf[1]**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
data | object | Required | required: ["eligible","block_reasons","block_reason_codes"] |   
  
**allOf[1] / data**

Type | Constraints  
---|---  
object | required: ["eligible","block_reasons","block_reason_codes"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
eligible | boolean | Required |  | Whether eligible for application  
block_reasons | array | Required |  | List of ineligibility reason descriptions  
block_reason_codes | array | Required |  | List of ineligibility reason codes  
  
**allOf[1] / data / block_reasons**

List of ineligibility reason descriptions

Type | Constraints  
---|---  
array |   
  
**allOf[1] / data / block_reasons / items**

Type | Constraints  
---|---  
string |   
  
**allOf[1] / data / block_reason_codes**

List of ineligibility reason codes

Type | Constraints  
---|---  
array |   
  
**allOf[1] / data / block_reason_codes / items**

Type | Constraints  
---|---  
string |   
  
**Enumerated Values**

Value  
---  
"user_not_exist"  
"user_blacked"  
"sub_account"  
"already_agent"  
"kyc_incomplete"  
"in_agent_tree"  
"ch_code_conflict"  
      
    
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
    
    

##  RebateUserInfo

Retrieve user rebate information

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
invite_uid | integer(int64) | Optional |  | My inviter's UID  
      
    
    {
      "invite_uid": 0
    }