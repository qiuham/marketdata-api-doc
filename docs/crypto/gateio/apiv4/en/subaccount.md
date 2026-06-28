---
exchange: gateio
source_url: https://www.gate.com/docs/developers/apiv4/en/subaccount
api_type: Account
updated_at: 2026-05-27 20:16:05.147431
---

# SubAccount

Sub-account management

##  List sub-accounts🔒 Authenticated

GET`/sub_accounts`

GET `/sub_accounts`

_List sub-accounts_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
type | query | string | Optional | Enter `0` to list all types of sub-accounts (currently supporting cross-margin sub-accounts and regular sub-accounts).  
Enter `1` to query regular sub-accounts only. If no parameter is passed, only regular sub-accounts will be queried by default.  
  
####  Detailed descriptions

**type** : Enter `0` to list all types of sub-accounts (currently supporting cross-margin sub-accounts and regular sub-accounts).  
Enter `1` to query regular sub-accounts only. If no parameter is passed, only regular sub-accounts will be queried by default.

### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)List retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [SubAccount]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | none  
» remark | string | Remark  
» login_name | string | Sub-account login name: Only letters, numbers and underscores are supported, cannot contain other invalid characters  
» password | string | The sub-account's password. (Default: the same as main account's password)  
» email | string | The sub-account's email address. (Default: the same as main account's email address)  
» state | integer(int32) | Sub-account status: 1-normal, 2-locked  
» type | integer(int32) | Sub-account type: 1-Regular sub-account, 3-Cross margin sub-account  
» user_id | integer(int64) | Sub-account user ID  
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
    
    url = '/sub_accounts'
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
    url="/sub_accounts"
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
        "remark": "remark",
        "login_name": "sub_account_for_trades",
        "user_id": 10001,
        "state": 1,
        "create_time": 168888888
      }
    ]
    

##  Create a new sub-account🔒 Authenticated

POST`/sub_accounts`

POST `/sub_accounts`

_Create a new sub-account_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | SubAccount | Required | none  
↳ remark | body | string | Optional | Remark  
↳ login_name | body | string | Required | Sub-account login name: Only letters, numbers and underscores are supported, cannot contain other invalid characters  
↳ password | body | string | Optional | The sub-account's password. (Default: the same as main account's password)  
↳ email | body | string | Optional | The sub-account's email address. (Default: the same as main account's email address)  
  
### Responses

  * 201[Created ](https://tools.ietf.org/html/rfc7231#section-6.3.2)Created successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
201 | [Created ](https://tools.ietf.org/html/rfc7231#section-6.3.2) | Created successfully | SubAccount  
  
### Response Schema

Status Code **201**

Name | Type | Description  
---|---|---  
» remark | string | Remark  
» login_name | string | Sub-account login name: Only letters, numbers and underscores are supported, cannot contain other invalid characters  
» password | string | The sub-account's password. (Default: the same as main account's password)  
» email | string | The sub-account's email address. (Default: the same as main account's email address)  
» state | integer(int32) | Sub-account status: 1-normal, 2-locked  
» type | integer(int32) | Sub-account type: 1-Regular sub-account, 3-Cross margin sub-account  
» user_id | integer(int64) | Sub-account user ID  
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
    
    url = '/sub_accounts'
    query_param = ''
    body='{"remark":"remark","login_name":"sub_account_for_trades"}'
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
    url="/sub_accounts"
    query_param=""
    body_param='{"remark":"remark","login_name":"sub_account_for_trades"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "remark": "remark",
      "login_name": "sub_account_for_trades"
    }
    

> Example responses

> 201 Response
    
    
    {
      "remark": "remark",
      "login_name": "sub_account_for_trades",
      "user_id": 10001,
      "state": 1,
      "create_time": 168888888
    }
    

##  Get sub-account🔒 Authenticated

GET`/sub_accounts/{user_id}`

GET `/sub_accounts/{user_id}`

Get `sub-account`

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
user_id | path | integer(int64) | Required | Sub-account user ID  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Successfully retrieved

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Successfully retrieved | SubAccount  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» remark | string | Remark  
» login_name | string | Sub-account login name: Only letters, numbers and underscores are supported, cannot contain other invalid characters  
» password | string | The sub-account's password. (Default: the same as main account's password)  
» email | string | The sub-account's email address. (Default: the same as main account's email address)  
» state | integer(int32) | Sub-account status: 1-normal, 2-locked  
» type | integer(int32) | Sub-account type: 1-Regular sub-account, 3-Cross margin sub-account  
» user_id | integer(int64) | Sub-account user ID  
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
    
    url = '/sub_accounts/0'
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
    url="/sub_accounts/0"
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
      "remark": "remark",
      "login_name": "sub_account_for_trades",
      "user_id": 10001,
      "state": 1,
      "create_time": 168888888
    }
    

##  List all API key pairs of the sub-account🔒 Authenticated

GET`/sub_accounts/{user_id}/keys`

GET `/sub_accounts/{user_id}/keys`

_List all API key pairs of the sub-account_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
user_id | path | integer | Required | Sub-account user ID  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)List retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | List retrieved successfully | [SubAccountKey]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | none  
» user_id | integer(int64) | User ID  
» mode | integer(int32) | Mode: 1 - classic 2 - portfolio account  
» name | string | API Key Name  
» perms | array | none  
»» name | string | Permission function name (no value will be cleared)  
\- wallet: wallet  
\- spot: spot/margin  
\- futures: perpetual contract  
\- delivery: delivery contract  
\- earn: earn  
\- custody: custody  
\- options: options  
\- account: account information  
\- loan: lending  
\- margin: margin  
\- unified: unified account  
\- copy: copy trading  
»» read_only | boolean | Read Only  
» ip_whitelist | array | IP whitelist (list will be cleared if no value is passed)  
» key | string | API Key  
» state | integer(int32) | Status: 1-Normal 2-Frozen 3-Locked  
» created_at | integer(int64) | Created time  
» updated_at | integer(int64) | Last Update Time  
» last_access | integer(int64) | Last Access Time  
  
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
    
    url = '/sub_accounts/0/keys'
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
    url="/sub_accounts/0/keys"
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
        "name": "spot",
        "user_id": 1000000,
        "perms": [
          {
            "name": "futures",
            "read_only": false
          },
          {
            "name": "wallet",
            "read_only": false
          },
          {
            "name": "delivery",
            "read_only": false
          },
          {
            "name": "options",
            "read_only": false
          },
          {
            "name": "spot",
            "read_only": false
          }
        ],
        "mode": 1,
        "ip_whitelist": [
          "127.0.0.1",
          "127.0.0.2"
        ],
        "key": "75c3264105b74693d8cb5c7f1a8e2420",
        "created_at": 1663642892,
        "last_access": 1663642892,
        "update_at": 1663642892
      }
    ]
    

##  Create new sub-account API key pair🔒 Authenticated

POST`/sub_accounts/{user_id}/keys`

POST `/sub_accounts/{user_id}/keys`

_Create new sub-account API key pair_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
user_id | path | integer(int64) | Required | Sub-account user ID  
body | body | SubAccountKey | Required | none  
↳ mode | body | integer(int32) | Optional | Mode: 1 - classic 2 - portfolio account  
↳ name | body | string | Optional | API Key Name  
↳ perms | body | array | Optional | none  
↳ name | body | string | Optional | Permission function name (no value will be cleared)  
\- wallet: wallet  
\- spot: spot/margin  
\- futures: perpetual contract  
\- delivery: delivery contract  
\- earn: earn  
\- custody: custody  
\- options: options  
\- account: account information  
\- loan: lending  
\- margin: margin  
\- unified: unified account  
\- copy: copy trading  
↳ read_only | body | boolean | Optional | Read Only  
↳ ip_whitelist | body | array | Optional | IP whitelist (list will be cleared if no value is passed)  
  
####  Detailed descriptions

**»» name** : Permission function name (no value will be cleared)  
\- wallet: wallet  
\- spot: spot/margin  
\- futures: perpetual contract  
\- delivery: delivery contract  
\- earn: earn  
\- custody: custody  
\- options: options  
\- account: account information  
\- loan: lending  
\- margin: margin  
\- unified: unified account  
\- copy: copy trading

### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Created successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Created successfully | SubAccountKey  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» user_id | integer(int64) | User ID  
» mode | integer(int32) | Mode: 1 - classic 2 - portfolio account  
» name | string | API Key Name  
» perms | array | none  
»» name | string | Permission function name (no value will be cleared)  
\- wallet: wallet  
\- spot: spot/margin  
\- futures: perpetual contract  
\- delivery: delivery contract  
\- earn: earn  
\- custody: custody  
\- options: options  
\- account: account information  
\- loan: lending  
\- margin: margin  
\- unified: unified account  
\- copy: copy trading  
»» read_only | boolean | Read Only  
» ip_whitelist | array | IP whitelist (list will be cleared if no value is passed)  
» key | string | API Key  
» state | integer(int32) | Status: 1-Normal 2-Frozen 3-Locked  
» created_at | integer(int64) | Created time  
» updated_at | integer(int64) | Last Update Time  
» last_access | integer(int64) | Last Access Time  
  
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
    
    url = '/sub_accounts/0/keys'
    query_param = ''
    body='{"mode":1,"name":"spot","perms":[{"read_only":false,"name":"options"},{"read_only":false,"name":"spot"},{"read_only":false,"name":"delivery"},{"read_only":false,"name":"wallet"},{"read_only":false,"name":"futures"}],"ip_whitelist":["127.0.0.1","127.0.0.2"]}'
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
    url="/sub_accounts/0/keys"
    query_param=""
    body_param='{"mode":1,"name":"spot","perms":[{"read_only":false,"name":"options"},{"read_only":false,"name":"spot"},{"read_only":false,"name":"delivery"},{"read_only":false,"name":"wallet"},{"read_only":false,"name":"futures"}],"ip_whitelist":["127.0.0.1","127.0.0.2"]}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "mode": 1,
      "name": "spot",
      "perms": [
        {
          "read_only": false,
          "name": "options"
        },
        {
          "read_only": false,
          "name": "spot"
        },
        {
          "read_only": false,
          "name": "delivery"
        },
        {
          "read_only": false,
          "name": "wallet"
        },
        {
          "read_only": false,
          "name": "futures"
        }
      ],
      "ip_whitelist": [
        "127.0.0.1",
        "127.0.0.2"
      ]
    }
    

> Example responses

> 200 Response
    
    
    {
      "state": 1,
      "name": "spot",
      "user_id": 100000,
      "perms": [
        {
          "name": "options",
          "read_only": false
        },
        {
          "name": "spot",
          "read_only": false
        },
        {
          "name": "delivery",
          "read_only": false
        },
        {
          "name": "wallet",
          "read_only": false
        },
        {
          "name": "futures",
          "read_only": false
        }
      ],
      "ip_whitelist": [
        "127.0.0.1",
        "127.0.0.2"
      ],
      "mode": 1,
      "secret": "cddcc6e5e78060e013860bdbe5e737830b96821c027664586fb38b411808f4fd",
      "key": "eb8815bf99d7bb5f8ad6497bdc4774a8",
      "created_at": 1663683330,
      "updated_at": 1663683330
    }
    

##  Get specific API key pair of the sub-account🔒 Authenticated

GET`/sub_accounts/{user_id}/keys/{key}`

GET `/sub_accounts/{user_id}/keys/{key}`

Get `specific API key pair of the sub-account`

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
user_id | path | integer | Required | Sub-account user ID  
key | path | string | Required | Sub-account API key  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Successfully retrieved

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Successfully retrieved | SubAccountKey  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
» user_id | integer(int64) | User ID  
» mode | integer(int32) | Mode: 1 - classic 2 - portfolio account  
» name | string | API Key Name  
» perms | array | none  
»» name | string | Permission function name (no value will be cleared)  
\- wallet: wallet  
\- spot: spot/margin  
\- futures: perpetual contract  
\- delivery: delivery contract  
\- earn: earn  
\- custody: custody  
\- options: options  
\- account: account information  
\- loan: lending  
\- margin: margin  
\- unified: unified account  
\- copy: copy trading  
»» read_only | boolean | Read Only  
» ip_whitelist | array | IP whitelist (list will be cleared if no value is passed)  
» key | string | API Key  
» state | integer(int32) | Status: 1-Normal 2-Frozen 3-Locked  
» created_at | integer(int64) | Created time  
» updated_at | integer(int64) | Last Update Time  
» last_access | integer(int64) | Last Access Time  
  
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
    
    url = '/sub_accounts/0/keys/string'
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
    url="/sub_accounts/0/keys/string"
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
      "state": 1,
      "name": "spot",
      "user_id": 1000000,
      "perms": [
        {
          "name": "futures",
          "read_only": false
        },
        {
          "name": "wallet",
          "read_only": false
        },
        {
          "name": "delivery",
          "read_only": false
        },
        {
          "name": "options",
          "read_only": false
        },
        {
          "name": "spot",
          "read_only": false
        }
      ],
      "mode": 1,
      "ip_whitelist": [
        "127.0.0.1",
        "127.0.0.2"
      ],
      "key": "75c3264105b74693d8cb5c7f1a8e2420",
      "created_at": 1663642892,
      "last_access": 1663642892,
      "update_at": 1663642892
    }
    

##  Update sub-account API key pair🔒 Authenticated

PUT`/sub_accounts/{user_id}/keys/{key}`

PUT `/sub_accounts/{user_id}/keys/{key}`

_Update sub-account API key pair_

Modify Sub-account API Key Pair (Note: This interface cannot modify the mode account type attribute)

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
user_id | path | integer | Required | Sub-account user ID  
key | path | string | Required | Sub-account API key  
body | body | SubAccountKey | Required | none  
↳ mode | body | integer(int32) | Optional | Mode: 1 - classic 2 - portfolio account  
↳ name | body | string | Optional | API Key Name  
↳ perms | body | array | Optional | none  
↳ name | body | string | Optional | Permission function name (no value will be cleared)  
\- wallet: wallet  
\- spot: spot/margin  
\- futures: perpetual contract  
\- delivery: delivery contract  
\- earn: earn  
\- custody: custody  
\- options: options  
\- account: account information  
\- loan: lending  
\- margin: margin  
\- unified: unified account  
\- copy: copy trading  
↳ read_only | body | boolean | Optional | Read Only  
↳ ip_whitelist | body | array | Optional | IP whitelist (list will be cleared if no value is passed)  
  
####  Detailed descriptions

**»» name** : Permission function name (no value will be cleared)  
\- wallet: wallet  
\- spot: spot/margin  
\- futures: perpetual contract  
\- delivery: delivery contract  
\- earn: earn  
\- custody: custody  
\- options: options  
\- account: account information  
\- loan: lending  
\- margin: margin  
\- unified: unified account  
\- copy: copy trading

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
    
    url = '/sub_accounts/0/keys/string'
    query_param = ''
    body='{"mode":1,"name":"spot","perms":[{"read_only":false,"name":"options"},{"read_only":false,"name":"spot"},{"read_only":false,"name":"delivery"},{"read_only":false,"name":"wallet"},{"read_only":false,"name":"futures"}],"ip_whitelist":["127.0.0.1","127.0.0.2"]}'
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
    url="/sub_accounts/0/keys/string"
    query_param=""
    body_param='{"mode":1,"name":"spot","perms":[{"read_only":false,"name":"options"},{"read_only":false,"name":"spot"},{"read_only":false,"name":"delivery"},{"read_only":false,"name":"wallet"},{"read_only":false,"name":"futures"}],"ip_whitelist":["127.0.0.1","127.0.0.2"]}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "mode": 1,
      "name": "spot",
      "perms": [
        {
          "read_only": false,
          "name": "options"
        },
        {
          "read_only": false,
          "name": "spot"
        },
        {
          "read_only": false,
          "name": "delivery"
        },
        {
          "read_only": false,
          "name": "wallet"
        },
        {
          "read_only": false,
          "name": "futures"
        }
      ],
      "ip_whitelist": [
        "127.0.0.1",
        "127.0.0.2"
      ]
    }
    

##  Delete sub-account API key pair🔒 Authenticated

DELETE`/sub_accounts/{user_id}/keys/{key}`

DELETE `/sub_accounts/{user_id}/keys/{key}`

Delete `sub-account API key pair`

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
user_id | path | integer | Required | Sub-account user ID  
key | path | string | Required | Sub-account API key  
  
### Responses

  * 204[No Content ](https://tools.ietf.org/html/rfc7231#section-6.3.5)Deleted successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
204 | [No Content ](https://tools.ietf.org/html/rfc7231#section-6.3.5) | Deleted successfully | None  
  
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
    
    url = '/sub_accounts/0/keys/string'
    query_param = ''
    # for `gen_sign` implementation, refer to section `Authentication` above
    sign_headers = gen_sign('DELETE', prefix + url, query_param)
    headers.update(sign_headers)
    r = requests.request('DELETE', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="DELETE"
    url="/sub_accounts/0/keys/string"
    query_param=""
    body_param=''
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

##  Lock sub-account🔒 Authenticated

POST`/sub_accounts/{user_id}/lock`

POST `/sub_accounts/{user_id}/lock`

_Lock sub-account_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
user_id | path | integer(int64) | Required | Sub-account user ID  
  
### Responses

  * 204[No Content ](https://tools.ietf.org/html/rfc7231#section-6.3.5)Locked successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
204 | [No Content ](https://tools.ietf.org/html/rfc7231#section-6.3.5) | Locked successfully | None  
  
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
    
    url = '/sub_accounts/0/lock'
    query_param = ''
    # for `gen_sign` implementation, refer to section `Authentication` above
    sign_headers = gen_sign('POST', prefix + url, query_param)
    headers.update(sign_headers)
    r = requests.request('POST', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="POST"
    url="/sub_accounts/0/lock"
    query_param=""
    body_param=''
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

##  Unlock sub-account🔒 Authenticated

POST`/sub_accounts/{user_id}/unlock`

POST `/sub_accounts/{user_id}/unlock`

_Unlock sub-account_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
user_id | path | integer(int64) | Required | Sub-account user ID  
  
### Responses

  * 204[No Content ](https://tools.ietf.org/html/rfc7231#section-6.3.5)Unlocked successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
204 | [No Content ](https://tools.ietf.org/html/rfc7231#section-6.3.5) | Unlocked successfully | None  
  
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
    
    url = '/sub_accounts/0/unlock'
    query_param = ''
    # for `gen_sign` implementation, refer to section `Authentication` above
    sign_headers = gen_sign('POST', prefix + url, query_param)
    headers.update(sign_headers)
    r = requests.request('POST', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="POST"
    url="/sub_accounts/0/unlock"
    query_param=""
    body_param=''
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

##  Get sub-account mode🔒 Authenticated

GET`/sub_accounts/unified_mode`

GET `/sub_accounts/unified_mode`

Get `sub-account mode`

Unified account mode:

  * `classic`: Classic account mode
  * `multi_currency`: Cross-currency margin mode
  * `portfolio`: Portfolio margin mode
  * `single_currency`: Single-currency margin mode

### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | [SubUserMode]  
  
### Response Schema

Status Code **200**

Name | Type | Description  
---|---|---  
_None_ | array | none  
» user_id | integer(int64) | User ID  
» is_unified | boolean | Whether it is a unified account  
» mode | string | Unified account mode:  
\- `classic`: Classic account mode  
\- `multi_currency`: Cross-currency margin mode  
\- `portfolio`: Portfolio margin mode  
\- `single_currency`: Single-currency margin mode  
  
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
    
    url = '/sub_accounts/unified_mode'
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
    url="/sub_accounts/unified_mode"
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
        "user_id": 110285555,
        "is_unified": true,
        "mode": "multi_currency"
      }
    ]
    

#  Schemas

##  SubAccountKey

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
user_id | integer(int64) | Optional | read-only | User ID  
mode | integer(int32) | Optional | none | Mode: 1 - classic 2 - portfolio account  
name | string | Optional | none | API Key Name  
perms | array | Optional | none | none  
↳ name | string | Optional | none | Permission function name (no value will be cleared)  
\- wallet: wallet  
\- spot: spot/margin  
\- futures: perpetual contract  
\- delivery: delivery contract  
\- earn: earn  
\- custody: custody  
\- options: options  
\- account: account information  
\- loan: lending  
\- margin: margin  
\- unified: unified account  
\- copy: copy trading  
↳ read_only | boolean | Optional | none | Read Only  
ip_whitelist | array | Optional | none | IP whitelist (list will be cleared if no value is passed)  
key | string | Optional | read-only | API Key  
state | integer(int32) | Optional | read-only | Status: 1-Normal 2-Frozen 3-Locked  
created_at | integer(int64) | Optional | read-only | Created time  
updated_at | integer(int64) | Optional | read-only | Last Update Time  
last_access | integer(int64) | Optional | read-only | Last Access Time  
      
    
    {
      "user_id": 0,
      "mode": 0,
      "name": "string",
      "perms": [
        {
          "name": "string",
          "read_only": true
        }
      ],
      "ip_whitelist": [
        "string"
      ],
      "key": "string",
      "state": 0,
      "created_at": 0,
      "updated_at": 0,
      "last_access": 0
    }
    
    

##  SubAccount

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
remark | string | Optional | none | Remark  
login_name | string | Required | none | Sub-account login name: Only letters, numbers and underscores are supported, cannot contain other invalid characters  
password | string | Optional | none | The sub-account's password. (Default: the same as main account's password)  
email | string | Optional | none | The sub-account's email address. (Default: the same as main account's email address)  
state | integer(int32) | Optional | read-only | Sub-account status: 1-normal, 2-locked  
type | integer(int32) | Optional | read-only | Sub-account type: 1-Regular sub-account, 3-Cross margin sub-account  
user_id | integer(int64) | Optional | read-only | Sub-account user ID  
create_time | integer(int64) | Optional | read-only | Created time  
      
    
    {
      "remark": "string",
      "login_name": "string",
      "password": "string",
      "email": "string",
      "state": 0,
      "type": 0,
      "user_id": 0,
      "create_time": 0
    }
    
    

##  SubUserMode

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
user_id | integer(int64) | Optional | none | User ID  
is_unified | boolean | Optional | none | Whether it is a unified account  
mode | string | Optional | none | Unified account mode:  
\- `classic`: Classic account mode  
\- `multi_currency`: Cross-currency margin mode  
\- `portfolio`: Portfolio margin mode  
\- `single_currency`: Single-currency margin mode  
      
    
    {
      "user_id": 0,
      "is_unified": true,
      "mode": "string"
    }