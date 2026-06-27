---
exchange: gateio
source_url: https://www.gate.com/docs/developers/apiv4/en/account
api_type: Account
updated_at: 2026-05-27 20:14:42.926225
---

# Account

Retrieve user account information

##  Retrieve user account information🔒 Authenticated

GET`/account/detail`

GET `/account/detail`

_Retrieve user account information_

### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Successfully retrieved

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Successfully retrieved | AccountDetail  
  
### Response Schema

Status Code **200**

_AccountDetail_

Name | Type | Description  
---|---|---  
» ip_whitelist | array | IP Whitelist  
» currency_pairs | array | Trading pair whitelist  
» user_id | integer(int64) | User ID  
» tier | integer(int64) | User VIP level  
» key | object | API Key details  
»» mode | integer(int32) | Mode: 1 - Classic mode, 2 - Legacy unified mode  
» copy_trading_role | integer(int32) | User role: 0 - Normal user 1 - Copy trading leader 2 - Copy trading follower 3 - Both leader and follower  
  
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
    
    url = '/account/detail'
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
    url="/account/detail"
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
      "user_id": 1667201533,
      "ip_whitelist": [
        "127.0.0.1"
      ],
      "currency_pairs": [
        "USDT_BTC"
      ],
      "key": {
        "mode": 1
      },
      "tier": 2,
      "copy_trading_role": 1
    }
    

##  Query All Main Account Key Information🔒 Authenticated

GET`/account/main_keys`

GET `/account/main_keys`

_Query All Main Account Key Information_

### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Successfully retrieved

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Successfully retrieved | AccountKeyInfo  
  
### Response Schema

Status Code **200**

_AccountKeyInfo_

Name | Type | Description  
---|---|---  
» state | integer(int32) | API key status: 1 - Normal, 2 - Locked, 3 - Frozen (can only be modified, default is 1 when creating)API Key Status: 1 - Normal, 2 - Locked, 3 - Frozen (can only be modified; default is 1 upon creation)  
» mode | integer(int32) | User mode: 1 - Classic mode, 2 - Legacy unified mode (can only be specified when creating, cannot be modified)  
» name | string | API Key Remark  
» currency_pairs | array | Trading Pair Whitelist, Maximum 30 Pairs  
» user_id | integer(int64) | User ID  
» ip_whitelist | array | IP Whitelist  
» perms | array | none  
»» name | string | Permission function name (no value will be cleared)  
\- `wallet`: wallet  
\- `spot`: spot/margin  
\- `futures`: perpetual contract  
\- `delivery`: delivery contract  
\- `earn`: earn  
\- `custody`: custody  
\- `options`: options  
\- `account`: account information  
\- `loan`: lending  
\- `margin`: margin  
\- `unified`: unified account  
\- `copy`: copy trading- `pilot`: pilot  
\- `otc`: otc  
\- `alpha`: alpha  
\- `crossx`: cross-exchange  
»» read_only | boolean | Read Only  
» key | object | API Key details  
»» mode | integer(int32) | Mode: 1 - Classic mode, 2 - Legacy unified mode  
» created_at | string | Created time  
» updated_at | string | Last Update Time  
» last_access | string | Last Access Time  
  
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
    
    url = '/account/main_keys'
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
    url="/account/main_keys"
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
        "state": 1,
        "mode": 1,
        "name": "test1",
        "user_id": 1,
        "perms": [
          {
            "name": "account",
            "read_only": false
          },
          {
            "name": "spot",
            "read_only": false
          }
        ],
        "ip_whitelist": [],
        "currency_pairs": [
          "BTC_USD",
          "ETH_USD"
        ],
        "key": "c5dcfbf1f3a7*****",
        "created_at": 1753030929,
        "update_at": 1756300567,
        "last_access": 1753030929
      },
      {
        "state": 1,
        "mode": 1,
        "name": "test2",
        "user_id": 1,
        "perms": [
          {
            "name": "spot",
            "read_only": false
          },
          {
            "name": "account",
            "read_only": false
          }
        ],
        "ip_whitelist": [],
        "currency_pairs": [
          "BTC_USD",
          "ETH_USD"
        ],
        "key": "52fd0035f665*****",
        "created_at": 1753897991,
        "update_at": 1756300567,
        "last_access": 1753897991
      }
    ]
    

##  Get user transaction rate limit information🔒 Authenticated

GET`/account/rate_limit`

GET `/account/rate_limit`

Get `user transaction rate limit information`

This interface is not yet open for use

### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Successfully retrieved

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Successfully retrieved | [AccountRateLimit]  
  
### Response Schema

Status Code **200**

_AccountRateLimit_

Name | Type | Description  
---|---|---  
AccountRateLimit | array | Account rate limit  
» tier | string | Frequency limit level (For detailed frequency limit rules, see Transaction ratio frequency limit)  
» ratio | string | Fill rate  
» main_ratio | string | Total fill ratio of main account  
» updated_at | string | Update time  
  
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
    
    url = '/account/rate_limit'
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
    url="/account/rate_limit"
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
        "type": "spot",
        "tier": "1",
        "ratio": "0",
        "main_ratio": "0",
        "updated_at": "1728230400"
      },
      {
        "type": "futures",
        "tier": "1",
        "ratio": "0",
        "main_ratio": "0",
        "updated_at": "1728230400"
      }
    ]
    

##  Query STP user groups created by the user🔒 Authenticated

GET`/account/stp_groups`

GET `/account/stp_groups`

_Query STP user groups created by the user_

Only query STP user groups created by the current main account

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
name | query | string | Optional | Fuzzy search by name  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)List retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [StpGroup]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | none  
» id | integer(int64) | STP Group ID  
» name | string | STP Group name  
» creator_id | integer(int64) | Creator ID  
» create_time | integer(int64) | Created time  
  
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
    
    url = '/account/stp_groups'
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
    url="/account/stp_groups"
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
        "id": 123435,
        "name": "group",
        "create_time": 1548000000,
        "creator_id": 10000
      }
    ]
    

##  Create STP user group🔒 Authenticated

POST`/account/stp_groups`

POST `/account/stp_groups`

_Create STP user group_

Only the main account is allowed to create a new STP user group

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | StpGroup | Required | none  
↳ id | body | integer(int64) | Optional | STP Group ID  
↳ name | body | string | Required | STP Group name  
↳ creator_id | body | integer(int64) | Optional | Creator ID  
↳ create_time | body | integer(int64) | Optional | Created time  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)User added successfully, returning current users in the STP group

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | User added successfully, returning current users in the STP group | StpGroup  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» id | integer(int64) | STP Group ID  
» name | string | STP Group name  
» creator_id | integer(int64) | Creator ID  
» create_time | integer(int64) | Created time  
  
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
    
    url = '/account/stp_groups'
    query_param = ''
    body='{"name":"stp_name"}'
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
    url="/account/stp_groups"
    query_param=""
    body_param='{"name":"stp_name"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "name": "stp_name"
    }
    

> Example responses

> 200 Response
    
    
    {
      "id": 123435,
      "name": "group",
      "create_time": 1548000000,
      "creator_id": 10000
    }
    

##  Query users in the STP user group🔒 Authenticated

GET`/account/stp_groups/{stp_id}/users`

GET `/account/stp_groups/{stp_id}/users`

_Query users in the STP user group_

Only the main account that created this STP group can query the account ID list of the current STP group

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
stp_id | path | integer(int64) | Required | STP Group ID  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)List retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [StpGroupUser]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | none  
» user_id | integer(int64) | User ID  
» stp_id | integer(int64) | STP Group ID  
» create_time | integer(int64) | Created time  
  
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
    
    url = '/account/stp_groups/1/users'
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
    url="/account/stp_groups/1/users"
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
        "user_id": 10000,
        "stp_id": 1,
        "create_time": 1548000000
      }
    ]
    

##  Add users to the STP user group🔒 Authenticated

POST`/account/stp_groups/{stp_id}/users`

POST `/account/stp_groups/{stp_id}/users`

_Add users to the STP user group_

  * Only the main account that created this STP group can add users to the STP user group
  * Only accounts under the current main account are allowed, cross-main account is not permitted

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
stp_id | path | integer(int64) | Required | STP Group ID  
body | body | AddSTPGroupUsersRequest | Required | User ID  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)User added successfully, returning current users in the STP group

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | User added successfully, returning current users in the STP group | [StpGroupUser]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | none  
» user_id | integer(int64) | User ID  
» stp_id | integer(int64) | STP Group ID  
» create_time | integer(int64) | Created time  
  
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
    
    url = '/account/stp_groups/1/users'
    query_param = ''
    body='[1,2,3]'
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
    url="/account/stp_groups/1/users"
    query_param=""
    body_param='[1,2,3]'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    [
      1,
      2,
      3
    ]
    

> Example responses

> 200 Response
    
    
    [
      {
        "user_id": 10000,
        "stp_id": 1,
        "create_time": 1548000000
      }
    ]
    

##  Delete users from the STP user group🔒 Authenticated

DELETE`/account/stp_groups/{stp_id}/users`

DELETE `/account/stp_groups/{stp_id}/users`

Delete `users from the STP user group`

  * Only the main account that created this STP group is allowed to delete users from the STP user group
  * Deletion is limited to accounts under the current main account; cross-account deletion is not permitted

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
stp_id | path | integer(int64) | Required | STP Group ID  
user_id | query | integer(int64) | Required | STP user IDs, multiple IDs can be separated by commas  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Users deleted successfully, returns current users in the STP group

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Users deleted successfully, returns current users in the STP group | [StpGroupUser]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | none  
» user_id | integer(int64) | User ID  
» stp_id | integer(int64) | STP Group ID  
» create_time | integer(int64) | Created time  
  
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
    
    url = '/account/stp_groups/1/users'
    query_param = 'user_id=1'
    # for `gen_sign` implementation, refer to section `Authentication` above
    sign_headers = gen_sign('DELETE', prefix + url, query_param)
    headers.update(sign_headers)
    r = requests.request('DELETE', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="DELETE"
    url="/account/stp_groups/1/users"
    query_param="user_id=1"
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
        "user_id": 10000,
        "stp_id": 1,
        "create_time": 1548000000
      }
    ]
    

##  Query GT fee deduction configuration🔒 Authenticated

GET`/account/debit_fee`

GET `/account/debit_fee`

_Query GT fee deduction configuration_

Query the GT fee deduction configuration for the current account

### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Success

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Success | DebitFee  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» enabled | boolean | Whether GT fee deduction is enabled  
  
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
    
    url = '/account/debit_fee'
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
    url="/account/debit_fee"
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
      "enabled": true
    }
    

##  Configure GT fee deduction🔒 Authenticated

POST`/account/debit_fee`

POST `/account/debit_fee`

_Configure GT fee deduction_

Enable or disable GT fee deduction for the current account

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | DebitFee | Required | none  
↳ enabled | body | boolean | Required | Whether GT fee deduction is enabled  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Success

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Success | None  
  
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
    
    url = '/account/debit_fee'
    query_param = ''
    body='{"enabled":true}'
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
    url="/account/debit_fee"
    query_param=""
    body_param='{"enabled":true}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "enabled": true
    }
    

#  Schemas

##  AccountKeyInfo

_AccountKeyInfo_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
state | integer(int32) | Optional | none | API key status: 1 - Normal, 2 - Locked, 3 - Frozen (can only be modified, default is 1 when creating)API Key Status: 1 - Normal, 2 - Locked, 3 - Frozen (can only be modified; default is 1 upon creation)  
mode | integer(int32) | Optional | none | User mode: 1 - Classic mode, 2 - Legacy unified mode (can only be specified when creating, cannot be modified)  
name | string | Optional | none | API Key Remark  
currency_pairs | array | Optional | none | Trading Pair Whitelist, Maximum 30 Pairs  
user_id | integer(int64) | Optional | none | User ID  
ip_whitelist | array | Optional | none | IP Whitelist  
perms | array | Optional | none | none  
↳ name | string | Optional | none | Permission function name (no value will be cleared)  
\- `wallet`: wallet  
\- `spot`: spot/margin  
\- `futures`: perpetual contract  
\- `delivery`: delivery contract  
\- `earn`: earn  
\- `custody`: custody  
\- `options`: options  
\- `account`: account information  
\- `loan`: lending  
\- `margin`: margin  
\- `unified`: unified account  
\- `copy`: copy trading- `pilot`: pilot  
\- `otc`: otc  
\- `alpha`: alpha  
\- `crossx`: cross-exchange  
↳ read_only | boolean | Optional | none | Read Only  
key | object | Optional | none | API Key details  
↳ mode | integer(int32) | Optional | none | Mode: 1 - Classic mode, 2 - Legacy unified mode  
created_at | string | Optional | read-only | Created time  
updated_at | string | Optional | read-only | Last Update Time  
last_access | string | Optional | read-only | Last Access Time  
      
    
    {
      "state": 0,
      "mode": 0,
      "name": "string",
      "currency_pairs": [
        "string"
      ],
      "user_id": 0,
      "ip_whitelist": [
        "string"
      ],
      "perms": [
        {
          "name": "string",
          "read_only": true
        }
      ],
      "key": {
        "mode": 0
      },
      "created_at": "string",
      "updated_at": "string",
      "last_access": "string"
    }
    
    

##  StpGroupUser

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
user_id | integer(int64) | Optional | none | User ID  
stp_id | integer(int64) | Optional | none | STP Group ID  
create_time | integer(int64) | Optional | none | Created time  
      
    
    {
      "user_id": 0,
      "stp_id": 0,
      "create_time": 0
    }
    
    

##  AddSTPGroupUsersRequest

###  Properties

_None_
    
    
    [
      0
    ]
    
    

##  AccountDetail

_AccountDetail_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
ip_whitelist | array | Optional | none | IP Whitelist  
currency_pairs | array | Optional | none | Trading pair whitelist  
user_id | integer(int64) | Optional | none | User ID  
tier | integer(int64) | Optional | none | User VIP level  
key | object | Optional | none | API Key details  
↳ mode | integer(int32) | Optional | none | Mode: 1 - Classic mode, 2 - Legacy unified mode  
copy_trading_role | integer(int32) | Optional | none | User role: 0 - Normal user 1 - Copy trading leader 2 - Copy trading follower 3 - Both leader and follower  
      
    
    {
      "ip_whitelist": [
        "string"
      ],
      "currency_pairs": [
        "string"
      ],
      "user_id": 0,
      "tier": 0,
      "key": {
        "mode": 0
      },
      "copy_trading_role": 0
    }
    
    

##  AccountRateLimit

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
tier | string | Optional | none | Frequency limit level (For detailed frequency limit rules, see Transaction ratio frequency limit)  
ratio | string | Optional | none | Fill rate  
main_ratio | string | Optional | none | Total fill ratio of main account  
updated_at | string | Optional | none | Update time  
      
    
    {
      "tier": "string",
      "ratio": "string",
      "main_ratio": "string",
      "updated_at": "string"
    }
    
    

##  DebitFee

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
enabled | boolean | Required | none | Whether GT fee deduction is enabled  
      
    
    {
      "enabled": true
    }
    
    

##  StpGroup

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
id | integer(int64) | Optional | none | STP Group ID  
name | string | Required | none | STP Group name  
creator_id | integer(int64) | Optional | none | Creator ID  
create_time | integer(int64) | Optional | none | Created time  
      
    
    {
      "id": 0,
      "name": "string",
      "creator_id": 0,
      "create_time": 0
    }